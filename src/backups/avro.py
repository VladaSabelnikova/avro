"""
Сериализация через AVRO.
"""
from io import BytesIO
from time import perf_counter

import fastavro

from src.backups.base import BackupProcessBase, COUNT_RECORDS
from src.schemes_for_serialize import BackupItem, avro_schema
from src.models import Order, session, User, BackupV1, SessionLocal, create_all_tables, generate_records, \
    PaymentSession


class BackupAvro(BackupProcessBase):

    def __init__(self, db_session: SessionLocal):
        super().__init__(db_session)
        self.parsed_schema = fastavro.parse_schema(avro_schema)

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        bytes_writer = BytesIO()

        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        fastavro.writer(bytes_writer, self.parsed_schema, [backup_item.model_dump()])
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
    assert not session.query(PaymentSession).all()
    print(f'BYTES avro = {len(backup.compress_data)}')
    print(f'TIME avro = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES avro = 2421
TIME avro = 0.05463860102099716
"""
