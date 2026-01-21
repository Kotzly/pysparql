from abc import ABC

from pydantic import Field
from .graph_pattern import GraphPattern


class Filter(ABC):
    _graph_pattern: GraphPattern = Field(...)
    _keyword: str = Field("FILTER")


class AbsenceFilter(Filter):
    _keyword: str = Field("NOT EXISTS")


class PresenceFilter(Filter):
    _keyword: str = Field("EXISTS")


class Minus(ABC):
    _graph_pattern: GraphPattern = Field(...)
    _keyword: str = Field("MINUS    ")
