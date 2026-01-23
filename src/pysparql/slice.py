from pydantic import Field


class LimitClause:
    _keyword: str = Field("LIMIT")
    _n: int = Field(...)

    def __init__(self, n: int):
        self._n = n


class OffsetClause:
    _keyword: str = Field("OFFSET")
