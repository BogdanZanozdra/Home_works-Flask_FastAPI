from typing import List
from pydantic import BaseModel
from datetime import date
from enum import Enum


# class Status(str, Enum):
#     accepted = 'accepted'
#     processing = 'processing'


class OrderIn(BaseModel):
    date_create: date
    user_id: int
    # status: Status | None = None


class OrderOut(OrderIn):
    id: int


class UserIn(BaseModel):
    name: str
    lastname: str
    email: str
    password: str


class UserOut(UserIn):
    id: int


class ItemIn(BaseModel):
    title: str
    description: str
    price: float
    order_id: int


class ItemOut(ItemIn):
    id: int
