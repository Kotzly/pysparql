from .term import Variable, Term
from typing import List
from pydantic import Field


class ValueList:
    _values: List[Term]


class Values:
    _keyword = Field("VALUES")

    _variables: List[Variable]
    _values: List[ValueList]
