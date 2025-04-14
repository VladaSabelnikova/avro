"""
Сериализация через AVRO с отсутствующей схемой.
"""
from io import BytesIO
from time import perf_counter

import fastavro

from src.backups.base import BackupProcessBase, COUNT_RECORDS
from src.schemes_for_serialize import BackupItem, avro_schema
from src.models import create_all_tables, generate_records, Order, session, User, BackupV1, SessionLocal, \
    PaymentSession


class BackupAvroSchemaless(BackupProcessBase):

    def __init__(self, db_session: SessionLocal):
        super().__init__(db_session)
        self.parsed_schema = fastavro.parse_schema(avro_schema)

    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        bytes_writer = BytesIO()

        # Расчёт времени выполнения сериализации.
        start = perf_counter()
        fastavro.schemaless_writer(bytes_writer, self.parsed_schema, backup_item.model_dump())
        self.total_execution_time += perf_counter() - start

        compress_data = bytes_writer.getvalue()
        return compress_data


if __name__ == "__main__":
    create_all_tables()
    generate_records(COUNT_RECORDS)

    backup_process = BackupAvroSchemaless(session)
    backup_process.main()

    backup = session.query(BackupV1).first()

    assert backup
    assert not session.query(User).all()
    assert not session.query(Order).all()
    assert not session.query(PaymentSession).all()
    print(f'BYTES schemaless = {len(backup.compress_data)}')
    print(f'TIME schemaless = {backup_process.total_execution_time}')


# Замеры несколькими итерациями.
"""
BYTES schemaless = 449
TIME schemaless = 0.0432378190162126
"""
