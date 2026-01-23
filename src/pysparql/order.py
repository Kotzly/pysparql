from pydantic import Field
from typing import List
from .expression import Expression
from enum import Enum


class OrderModifier(Enum):
    ASC = "ASC"
    DESC = "DESC"


class OrderItem:
    _expression: Expression
    _modifier: Field(None)


class Order:
    _items: List[OrderItem] = Field(..., default_factory=list)
