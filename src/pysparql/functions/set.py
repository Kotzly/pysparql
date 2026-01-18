
from abc import ABC
from pydantic import Field
from typing import List
from .filter import Filter
from triple import Triple

class Aggregate(ABC):
    class Distinct():
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
    _kwargs = {"SEPARATOR": (str, Field(..., ))}

