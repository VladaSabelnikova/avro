"""
Сериализация через protobuff.
backup_item_pb2 нужно сначала было скомпилировать командой:
protoc --python_out=. proto_files/backup_item.proto
"""
from src.backups.proto_files import backup_item_pb2

from time import perf_counter
from uuid import uuid4


from src.backups.pydantic_models import BackupItem, UserItem, OrderItem
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
        compress_data = self._compress_data(backup_item.dict())
        self.total_execution_time += perf_counter() - start

        backup = BackupV1(
            id=str(uuid4()),
            compress_data=compress_data
        )
        self.db_session.add(backup)

    def _compress_data(self, data: dict) -> bytes:
        backup = backup_item_pb2.BackupItem(**data)
        return backup.SerializeToString()

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
