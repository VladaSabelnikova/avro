"""
Какой объём от общего кол-ва занимают ключи в JSON?
Не все же поля будут заполнены, а это значит минимум 50% а то и больше.
"""
import pickle

from src.backups.pydantic_models import BackupItem


def main():
    backup_item = BackupItem(order=None, payment_session=None, user=None).dict()

    keys = pickle.dumps([*backup_item.keys()])
    values = pickle.dumps([*backup_item.values()])

    return len(keys), len(values)


if __name__ == "__main__":
    print(main())
