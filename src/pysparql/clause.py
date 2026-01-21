from enum import Enum, auto
from pydantic import Field


class Clause:
    pass


class SelectClause:
    class Modifier(Enum):
        DISTINCT = auto()
        REDUCED = auto()

    _keyword: str = Field("SELECT")
    modifier: Modifier = Field(...)


class WhereClause:
    _keyword: str = Field("WHERE")


class GroupByClause:
    _keyword: str = Field("GROUP BY")


class HavingClause:
    _keyword: str = Field("HAVING")


class OrderClause:
    _keyword: str = Field("ORDER")


# LimitOffsetClause = Union[LimitClause, OffsetClause]


# Modifier = Union[GroupClause, HavingClause, OrderClause, LimitOffsetClause]
