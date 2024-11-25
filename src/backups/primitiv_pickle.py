import gzip
import json
import pickle
from datetime import datetime
from io import BytesIO
from time import perf_counter
from uuid import uuid4

import fastavro
from pydantic import BaseModel, field_validator

from src.backups.pydantic_models import UserItem, OrderItem, BackupItem
from src.models import create_all_tables, generate_records, Order, session, User, BackupV1, SessionLocal


class BackupProcess:

    def __init__(self, db_session: SessionLocal):
        self.db_session = db_session
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
        # Расчёт времени выполнения
        start = perf_counter()
        compress_data = pickle.dumps(backup_item.dict())
        self.total_execution_time += perf_counter() - start

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
    print(f'BYTES pickle = {len(backup.compress_data)}')
    print(f'TIME pickle = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES pickle = 330
TIME pickle = 0.005690999983926304

BYTES pickle = 330
TIME pickle = 0.0057266049916506745

BYTES pickle = 330
TIME pickle = 0.0052484079787973315
"""