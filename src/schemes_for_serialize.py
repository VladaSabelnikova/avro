"""
Разные модели для сериализаторов.
Тут есть пидантик и авро схемы.
"""
from datetime import datetime

from pydantic import BaseModel, field_validator


class UserItem(BaseModel):
    id: str
    name: str | None
    surname: str | None
    email_address: str | None
    phone_number: str | None


class OrderItem(BaseModel):
    id: str
    user_id: str
    bank_card_id: str
    payment_session_id: str
    tariff: str
    amount: int
    currency: str
    refund_amount: int | None
    meta_information_simple_number_1: str | None
    human_is_all_too_human_coding_for_free_minds: str | None
    in_an_hour_of_unprecedented_heat: str | None
    i_am_part_of_that_force: str | None
    created_at: str | datetime = None

    @field_validator('created_at')
    @classmethod
    def set_created_at(cls, created_at):
        if isinstance(created_at, datetime):
            return created_at.isoformat()
        return created_at

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat(timespec='seconds'),
        }


class PaymentSessionItem(BaseModel):

    id: str
    user_id: str
    order_id: str
    title: str
    user_name: str | None
    user_surname: str | None
    user_email_address: str | None
    user_phone_number: str | None
    bank_card_mask: str | None
    order_tariff: str | None
    order_amount: int | None
    order_currency: str | None
    order_refund_amount: int | None


class BackupItem(BaseModel):
    user: UserItem | None
    order: OrderItem | None
    payment_session: PaymentSessionItem | None


# AVRO схемы.
payment_session_schema = {
    "type": "record",
    "name": "payment_session",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "user_id", "type": "string"},
        {"name": "order_id", "type": "string"},
        {"name": "title", "type": "string"},
        {"name": "user_name", "type": ["null", "string"]},
        {"name": "user_surname", "type": ["null", "string"]},
        {"name": "user_email_address", "type": ["null", "string"]},
        {"name": "user_phone_number", "type": ["null", "string"]},
        {"name": "bank_card_mask", "type": ["null", "string"]},
        {"name": "order_tariff", "type": ["null", "string"]},
        {"name": "order_amount", "type": ["null", "int"]},
        {"name": "order_currency", "type": ["null", "string"]},
        {"name": "order_refund_amount", "type": ["null", "int"]},
    ]
}

order_schema = {
    "type": "record",
    "name": "order",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "user_id", "type": "string"},
        {"name": "bank_card_id", "type": "string"},
        {"name": "payment_session_id", "type": "string"},
        {"name": "tariff", "type": "string"},
        {"name": "amount", "type": "int"},
        {"name": "currency", "type": "string"},
        {"name": "refund_amount", "type": ["null", "string"]},
        {"name": "created_at", "type": "string"},
        {"name": "meta_information_simple_number_1", "type": ["null", "string"]},
        {"name": "human_is_all_too_human_coding_for_free_minds", "type": ["null", "string"]},
        {"name": "in_an_hour_of_unprecedented_heat", "type": ["null", "string"]},
        {"name": "i_am_part_of_that_force", "type": ["null", "string"]},
    ]
}

user_schema = {
    "type": "record",
    "name": "user",
    "fields": [
        {"name": "id", "type": ["null", "string"]},
        {"name": "name", "type": ["null", "string"]},
        {"name": "surname", "type": ["null", "string"]},
        {"name": "email_address", "type": ["null", "string"]},
        {"name": "phone_number", "type": ["null", "string"]},
    ]
}


avro_schema = {
    "type": "record",
    "name": "BackupItem",
    "fields": [
        {"name": "order", "type": ["null", order_schema]},
        {"name": "user", "type": ["null", user_schema]},
        {"name": "payment_session", "type": ["null", payment_session_schema]},
    ]
}
