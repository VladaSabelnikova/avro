import gzip
import json

from io import BytesIO
from time import perf_counter
from uuid import uuid4

import fastavro


from src.backups.pydantic_models import UserItem, OrderItem, BackupItem
from src.models import create_all_tables, generate_records, Order, session, User, BackupV1, SessionLocal


# AVRO схема для наших моделей.

payment_session_schema = {
    "type": "record",
    "name": "payment_session",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "user_id", "type": ["null", "string"]},
        {"name": "order_id", "type": ["null", "string"]},
        {"name": "title", "type": ["null", "string"]},
        {"name": "amount", "type": "int"},
        {"name": "currency", "type": "string"},
    ]
}

order_item_schema = {
    "type": "record",
    "name": "order",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "user_id", "type": ["null", "string"]},
        {"name": "user_name", "type": ["null", "string"]},
        {"name": "user_surname", "type": ["null", "string"]},
        {"name": "created_at", "type": "string"},
    ]
}

user_item_schema = {
    "type": "record",
    "name": "user",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "name", "type": ["null", "string"]},
        {"name": "surname", "type": "string"},
    ]
}


schema = {
    "type": "record",
    "name": "BackupItem",
    "fields": [
        {"name": "order", "type": ["null", order_item_schema]},
        {"name": "user", "type": ["null", user_item_schema]},
        {"name": "payment_session", "type": ["null", payment_session_schema]},
    ]
}


class BackupProcess:

    def __init__(self, db_session: SessionLocal):
        self.db_session = db_session
        self.parsed_schema = fastavro.parse_schema(schema)
        self.total_execution_time = 0

        create_all_tables()
        generate_records(100)

    def main(self):
        try:
            for order in self._find_orders():

                user = self._get_user_by_id(order.user_id)
                backup_item = BackupItem(
                    user=UserItem(**user.as_dict()),
                    order=OrderItem(**order.as_dict()),
                    payment_session=None
                )
                self._save_backup(backup_item)
                self._delete_data(backup_item)
            self.db_session.commit()

        except BaseException:
            self.db_session.rollback()

    def _find_orders(self):
        return self.db_session.query(Order).all()

    def _get_user_by_id(self, user_id: str):
        return self.db_session.query(User).get(user_id)

    def _save_backup(self, backup_item: BackupItem):
        bytes_writer = BytesIO()

        # Расчёт времени выполнения
        start = perf_counter()
        fastavro.writer(bytes_writer, self.parsed_schema, [backup_item.dict()])
        self.total_execution_time += perf_counter() - start

        compress_data = bytes_writer.getvalue()

        backup = BackupV1(
            id=str(uuid4()),
            compress_data=compress_data
        )
        self.db_session.add(backup)

    def _compress_data(self, data: dict) -> bytes:
        bytes_data = json.dumps(data, default=str).encode()
        return gzip.compress(bytes_data)

    def _delete_data(self, backup_item: BackupItem):
        self.db_session.query(User).filter(
            User.id == backup_item.user.id
        ).delete()

        self.db_session.query(Order).filter(
            Order.id == backup_item.order.id
        ).delete()


if __name__ == "__main__":
    backup_process = BackupProcess(session)
    backup_process.main()

    backup = session.query(BackupV1).first()

    assert backup
    assert not session.query(User).all()
    assert not session.query(Order).all()
    print(f'BYTES avro = {len(backup.compress_data)}')
    print(f'TIME avro = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES avro = 1192
TIME avro = 0.02129821001290111

BYTES avro = 1192
TIME avro = 0.021948814974166453

BYTES avro = 1192
TIME avro = 0.027923238994844723
"""
