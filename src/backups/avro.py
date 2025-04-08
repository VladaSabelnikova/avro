"""
Сериализация через AVRO.
"""
from io import BytesIO
from time import perf_counter

import fastavro

from src.backups.base import BackupProcessBase, COUNT_RECORDS
from src.backups.pydantic_models import BackupItem
from src.models import Order, session, User, BackupV1, SessionLocal, create_all_tables, generate_records

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


class BackupAvro(BackupProcessBase):

    def __init__(self, db_session: SessionLocal):
        super().__init__(db_session)
        self.parsed_schema = fastavro.parse_schema(schema)

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        bytes_writer = BytesIO()

        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        fastavro.writer(bytes_writer, self.parsed_schema, [backup_item.dict()])
        self.total_execution_time += perf_counter() - start

        compress_data = bytes_writer.getvalue()
        return compress_data


if __name__ == "__main__":
    create_all_tables()
    generate_records(COUNT_RECORDS)

    backup_process = BackupAvro(session)
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
