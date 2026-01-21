from abc import ABC
from pydantic import Field


class Aggregate(ABC):
    class Distinct:
        pass


class Count(Aggregate):
    pass


class Sum(Aggregate):
    pass


class Avg(Aggregate):
    pass


class Min(Aggregate):
    pass


class Max(Aggregate):
    pass


class Sample(Aggregate):
    pass


class GroupConcat(Aggregate):
    _kwargs = {
        "SEPARATOR": (
            str,
            Field(
                ...,
            ),
        )
    }
