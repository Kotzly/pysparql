from .base import Function
from pydantic import Field
from .graph_pattern import GraphPattern
from typing import List


class Bound(Function):
    _keyword = "BOUND"

class If(Function):
    _keyword = "IF"

class Coalesce(Function):
    _keyword = "COALESCE"

