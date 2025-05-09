"""
Сериализация через pickle.
"""
import pickle
from time import perf_counter

from src.backups.base import BackupProcessBase, COUNT_RECORDS
from src.schemes_for_serialize import BackupItem
from src.models import create_all_tables, generate_records, Order, session, User, BackupV1, PaymentSession


class BackupPickle(BackupProcessBase):

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        compress_data = pickle.dumps(backup_item.model_dump())
        self.total_execution_time += perf_counter() - start

        return compress_data


if __name__ == "__main__":
    create_all_tables()
    generate_records(COUNT_RECORDS)

    backup_process = BackupPickle(session)
    backup_process.main()

    backup = session.query(BackupV1).first()

    assert backup
    assert not session.query(User).all()
    assert not session.query(Order).all()
    assert not session.query(PaymentSession).all()
    print(f'BYTES pickle = {len(backup.compress_data)}')
    print(f'TIME pickle = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES pickle = 1015
TIME pickle = 0.01143019502342213
"""
