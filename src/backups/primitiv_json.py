"""
Сериализация через JSON.
"""
import json

from time import perf_counter

from src.backups.base import BackupProcessBase, COUNT_RECORDS
from src.backups.pydantic_models import BackupItem
from src.models import Order, session, User, BackupV1, create_all_tables, generate_records


class BackupJson(BackupProcessBase):

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        compress_data = json.dumps(backup_item.dict(), default=str).encode()
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
    print(f'BYTES json = {len(backup.compress_data)}')
    print(f'TIME json = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES json = 417
TIME json = 0.007674127984500956

BYTES json = 417
TIME json = 0.007634660985786468

BYTES json = 417
TIME json = 0.007488315990485717
"""
