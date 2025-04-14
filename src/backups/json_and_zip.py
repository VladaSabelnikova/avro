"""
Сериализация через JSON + ZIP (сейчас примерно так работает).
"""
import gzip
import json
from time import perf_counter

from src.backups.base import BackupProcessBase, COUNT_RECORDS
from src.schemes_for_serialize import BackupItem
from src.models import Order, session, User, BackupV1, create_all_tables, generate_records, PaymentSession


class BackupJsonZip(BackupProcessBase):

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        bytes_data = json.dumps(backup_item.model_dump(), default=str).encode()
        compress_data = gzip.compress(bytes_data)
        self.total_execution_time += perf_counter() - start

        return compress_data


if __name__ == "__main__":
    create_all_tables()
    generate_records(COUNT_RECORDS)

    backup_process = BackupJsonZip(session)
    backup_process.main()

    backup = session.query(BackupV1).first()

    assert backup
    assert not session.query(User).all()
    assert not session.query(Order).all()
    assert not session.query(PaymentSession).all()
    print(f'BYTES json + zip = {len(backup.compress_data)}')
    print(f'TIME json + zip = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES json + zip = 517
TIME json + zip = 0.04228171402064618
"""
