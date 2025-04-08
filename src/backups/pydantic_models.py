from datetime import datetime

from pydantic import BaseModel, field_validator


class UserItem(BaseModel):
    id: str
    name: str
    surname: str


class OrderItem(BaseModel):
    id: str
    user_id: str | None
    user_name: str | None
    user_surname: str | None
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
    __tablename__ = "payment_session"

    id: str
    user_id: str | None
    order_id: str | None
    title: str | None
    amount: int
    currency: str


class BackupItem(BaseModel):
    user: UserItem | None
    order: OrderItem | None
    payment_session: PaymentSessionItem | None
