from abc import ABC

from pydantic import Field
from .base import GraphPattern
from .expression import Expression
from typing import Union


class Filter(ABC):
    _match: Union[GraphPattern, Expression] = Field(...)
    _keyword: str = Field("FILTER")


class InnerFilter(Filter):
    _match: Expression = Field(...)


class AbsenceFilter(Filter):
    _keyword: str = Field("NOT EXISTS")


class PresenceFilter(Filter):
    _keyword: str = Field("EXISTS")


class Minus(ABC):
    _graph_pattern: GraphPattern = Field(...)
    _keyword: str = Field("MINUS")
