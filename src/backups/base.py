"""
Логика поиска нужных записей в БД и создания новой записи в таблице Backup будет одинаковой,
разница будет исключительно в реализации сериализации.

Поэтому общий функционал вынесен в отдельный класс,
чтобы не рябило в глазах от лишнего функционала в demo сериализаторов.
"""
from abc import ABC, abstractmethod
from uuid import uuid4

from src.backups.pydantic_models import UserItem, OrderItem, BackupItem
from src.models import Order, User, SessionLocal, BackupV1

COUNT_RECORDS = 100


class BackupProcessBase(ABC):

    def __init__(self, db_session: SessionLocal):
        self.db_session = db_session
        self.total_execution_time = 0

    def main(self):
        """
        Основной процесс создания бэкапа.
        Примитивная версия того, как это должно работать в проде.
        Ищем записи, обогащаем связями, сохраняем бэкап, удаляем найденное.
        """
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
        return self.db_session.get(User, user_id)

    def _delete_data(self, backup_item: BackupItem):
        self.db_session.query(User).filter(
            User.id == backup_item.user.id
        ).delete()

        self.db_session.query(Order).filter(
            Order.id == backup_item.order.id
        ).delete()

    def _save_backup(self, backup_item: BackupItem):
        compress_data = self._serialize_data(backup_item)
        backup = BackupV1(
            id=str(uuid4()),
            compress_data=compress_data
        )
        self.db_session.add(backup)

    @abstractmethod
    def _serialize_data(self, backup_item: BackupItem) -> bytes:
        """
        В этом методе реализация сериализации с подсчётом времени выполнения.
        Предполагается, что self.total_execution_time будет накапливаться тут.
        :param backup_item: Агрегированные данные для сериализации
        :return Каким-то образом сериализованные данные
        """
        pass
