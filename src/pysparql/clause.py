from typing import Union
from enum import Enum, auto
from abc import ABC
from pydantic import Field

class Clause:
    pass

class SelectClause:
    class Modifier(Enum):
        DISTINCT = auto()
        REDUCED = auto()

    modifier: Modifier = Field(...)

class DatasetClause:
    pass

class WhereClause:
    pass

class GroupClause:
    pass

class HavingClause:
    pass

class LimitClause:
    _keyword: str = Field("LIMIT")

class OffsetClause:
    _keyword: str = Field("OFFSET")

class OrderClause:
    _keyword: str = Field("ORDER")


LimitOffsetClause = Union[LimitClause, OffsetClause]


Modifier = Union[GroupClause, HavingClause, OrderClause, LimitOffsetClause]