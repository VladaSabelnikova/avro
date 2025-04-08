"""
Сериализация через protobuff.
backup_item_pb2 нужно сначала было скомпилировать командой:
protoc --python_out=. proto_files/backup_item.proto
"""
from src.backups.base import COUNT_RECORDS, BackupProcessBase
from src.backups.proto_files import backup_item_pb2

from time import perf_counter

from src.backups.pydantic_models import BackupItem
from src.models import create_all_tables, generate_records, Order, session, User, BackupV1


class BackupProtobuff(BackupProcessBase):

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        backup = backup_item_pb2.BackupItem(**backup_item.dict())
        compress_data = backup.SerializeToString()
        self.total_execution_time += perf_counter() - start

        return compress_data


if __name__ == "__main__":
    create_all_tables()
    generate_records(COUNT_RECORDS)

    backup_process = BackupProtobuff(session)
    backup_process.main()

    backup = session.query(BackupV1).first()

    assert backup
    assert not session.query(User).all()
    assert not session.query(Order).all()
    print(f'BYTES protobuff = {len(backup.compress_data)}')
    print(f'TIME protobuff = {backup_process.total_execution_time}')

# Замеры несколькими итерациями.
"""
BYTES protobuff = 195
TIME protobuff = 0.025126114953309298

BYTES protobuff = 195
TIME protobuff = 0.028885017010907177

BYTES protobuff = 195
TIME protobuff = 0.03136103400902357
"""
