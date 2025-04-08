"""
Какой объём от общего кол-ва занимают ключи в JSON?
Не все же поля будут заполнены, а это значит минимум 50% а то и больше.
Посмотрим худший вариант, когда у ключей все значения None.
"""
import pickle

from src.backups.pydantic_models import BackupItem


def main():
    backup_item = BackupItem(order=None, payment_session=None, user=None).model_dump()

    keys = pickle.dumps([*backup_item.keys()])
    values = pickle.dumps([*backup_item.values()])

    return f'KEYS = {len(keys)}', f'VALUES = {len(values)}'


if __name__ == "__main__":
    print(main())
