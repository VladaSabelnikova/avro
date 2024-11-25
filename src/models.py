from datetime import datetime
import os
from uuid import uuid4

from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    DateTime,
    String, Integer,

)
from sqlalchemy.dialects.postgresql import BYTEA, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata


class Order(DeclarativeBase):
    __tablename__ = "order"

    id = Column(String(), primary_key=True, default=str(uuid4()))
    user_id = Column(
        String(),
        nullable=False,
        doc="Пользователь",
    )
    user_name = Column(
        String(),
        nullable=False,
        doc="имя пользователя",
    )
    user_surname = Column(
        String(),
        nullable=False,
        doc="фамилия пользователя",
    )
    created_at = Column(
        DateTime(),
        default=datetime.utcnow,
        nullable=False,
        doc="Дата оплаты"
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(DeclarativeBase):
    __tablename__ = "user"

    id = Column(String(), primary_key=True, nullable=False, default=str(uuid4()))
    name = Column(String())
    surname = Column(String())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class PaymentSession(DeclarativeBase):
    __tablename__ = "payment_session"

    id = Column(String(), primary_key=True, nullable=False, default=str(uuid4()))
    user_id = Column(
        String(),
        nullable=True,
        doc="Пользователь",
    )
    order_id = Column(
        String(),
        nullable=True,
        doc="Заказ",
    )
    title = Column(
        String(),
        nullable=True,
        doc="Заказ",
    )
    amount = Column(
        Integer(),
        nullable=False,
        doc="Заказ",
    )
    title = Column(
        String(),
        nullable=True,
        doc="Заказ",
    )

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
    Хитрость в том, что мы сделаем много повторяющихся значений.
    Имитируем большую связность между таблицами.
    """
    for _ in range(quantity):
        new_user = User(id=str(uuid4()), name="Иван", surname="Иванов")
        new_order = Order(
            id=str(uuid4()),
            user_id=new_user.id,
            user_name=new_user.name,
            user_surname=new_user.surname
        )
        session.add(new_user)
        session.add(new_order)

    session.commit()


if __name__ == "__main__":
    create_all_tables()
    generate_records()
