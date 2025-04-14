"""
Модели ORM.
Обратите внимание на имитацию высокой связанности между таблицами в PaymentSession.
Чем больше значений будет дублироваться, тем эффективнее будет алгоритм сжатия.

А так же обратите внимание на большие названия атрибутов с пустыми значениями в Order.
Чем больше ключи при пустых значениях, тем эффективнее будет хранение данных без ключей.
"""
from datetime import datetime
import os
from uuid import uuid4

from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    DateTime,
    String, Integer,

)
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata


class User(DeclarativeBase):
    __tablename__ = "user"

    id = Column(String(), primary_key=True, nullable=False, default=str(uuid4()))
    name = Column(
        String(),
        doc="Имя пользователя"
    )
    surname = Column(
        String(),
        doc="Фамилия пользователя"
    )
    email_address = Column(
        String(),
        doc="Адрес электронной почты"
    )
    phone_number = Column(
        String(),
        doc="Номер телефона"
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Order(DeclarativeBase):
    __tablename__ = "order"

    id = Column(String(), primary_key=True, default=str(uuid4()))
    user_id = Column(
        String(),
        nullable=False,
        doc="Пользователь",
    )
    bank_card_id = Column(
        String(),
        nullable=False,
        doc="Банковская карта",
    )
    payment_session_id = Column(
        String(),
        nullable=False,
        doc="Платёжная форма",
    )
    tariff = Column(
        String(),
        nullable=False,
        doc="По какому тарифу продали",
    )
    amount = Column(
        Integer(),
        nullable=False,
        doc="Стоимость",
    )
    currency = Column(
        String(),
        nullable=False,
        doc="Валюта",
    )
    refund_amount = Column(
        Integer(),
        nullable=True,
        doc="Стоимость возврата",
    )
    created_at = Column(
        DateTime(),
        default=datetime.utcnow,
        nullable=False,
        doc="Дата оплаты"
    )

    # Сделаем несколько атрибутов с большими названиями и они будут всегда пустыми.
    # Тем самым продемонстрируем чем отсутствие ключей в схеме так хорошо (src/backups/avro_schemaless.py).
    meta_information_simple_number_1 = Column(
        String(),
        nullable=True
    )
    human_is_all_too_human_coding_for_free_minds = Column(
        String(),
        nullable=True
    )
    in_an_hour_of_unprecedented_heat = Column(
        String(),
        nullable=True
    )
    i_am_part_of_that_force = Column(
        String(),
        nullable=True
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class PaymentSession(DeclarativeBase):
    __tablename__ = "payment_session"

    id = Column(String(), primary_key=True, nullable=False, default=str(uuid4()))
    user_id = Column(
        String(),
        nullable=False,
        doc="Пользователь",
    )
    order_id = Column(
        String(),
        nullable=False,
        doc="Заказ",
    )
    title = Column(
        String(),
        nullable=False,
        doc="Название платёжной формы",
    )
    # Намеренно дублируем данные.
    # Имитируем высокую связанность между таблицами с множеством повторений.
    # Так будет ближе к продовой ситуации + нагляднее покажет эффективность сжатия (src/backups/json_and_zip.py).
    user_name = Column(String())
    user_surname = Column(String())
    user_email_address = Column(String())
    user_phone_number = Column(String())
    bank_card_mask = Column(String())
    order_tariff = Column(String())
    order_amount = Column(Integer())
    order_currency = Column(String())
    order_refund_amount = Column(Integer())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class BackupV1(DeclarativeBase):
    __tablename__ = "backup_v1"

    id = Column(String(), primary_key=True, nullable=False, default=str(uuid4()))
    compress_data = Column(
        BYTEA(),
        doc="Атрибуты бэкапнутых данных"
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


load_dotenv()
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/{db_name}",
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


def create_all_tables():
    metadata.drop_all(engine)
    metadata.create_all(engine)


def generate_records(quantity=10):
    """
    Наполняем тестовое окружение.
    """
    for _ in range(quantity):
        new_user = User(
            id=str(uuid4()),
            name="Иван"
        )

        new_payment_session = PaymentSession(
            id=str(uuid4()),
            user_id=new_user.id,
            order_id=str(uuid4()),
            title="Покупка подписки",
            user_name=new_user.name,
            user_surname=new_user.surname,
            user_email_address=new_user.email_address,
            user_phone_number=new_user.phone_number,
            bank_card_mask="777***666",
            order_tariff="Всё за 300",
            order_amount=300,
            order_currency="RUB"
        )

        new_order = Order(
            id=new_payment_session.order_id,
            user_id=new_user.id,
            bank_card_id=str(uuid4()),
            payment_session_id=new_payment_session.id,
            tariff=new_payment_session.order_tariff,
            amount=new_payment_session.order_amount,
            currency=new_payment_session.order_currency,
            refund_amount=new_payment_session.order_refund_amount
        )
        session.add(new_user)
        session.add(new_payment_session)
        session.add(new_order)

    session.commit()


if __name__ == "__main__":
    create_all_tables()
    generate_records()
