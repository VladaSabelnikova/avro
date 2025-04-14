"""
Сериализация через JSON.
"""
import json

from time import perf_counter

from src.backups.base import BackupProcessBase, COUNT_RECORDS
from src.schemes_for_serialize import BackupItem
from src.models import generate_records, create_all_tables, session, BackupV1, Order, PaymentSession, User


class BackupJson(BackupProcessBase):

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        compress_data = json.dumps(backup_item.model_dump(), default=str).encode()
        self.total_execution_time += perf_counter() - start

        return compress_data


if __name__ == "__main__":
    create_all_tables()
    generate_records(COUNT_RECORDS)

    backup_process = BackupJson(session)
    backup_process.main()

    backup = session.query(BackupV1).first()

    assert backup
    assert not session.query(User).all()
    assert not session.query(Order).all()
    assert not session.query(PaymentSession).all()
    print(f'BYTES json = {len(backup.compress_data)}')
    print(f'TOTAL TIME json = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES json = 1254
TOTAL TIME json = 0.029032764003204647
"""
