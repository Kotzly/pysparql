from .base import Function
from typing import List


class Abs(Function):
    _keyword = "abs"

class Round(Function):
    _keyword = "round"

class Ceil(Function):
    _keyword = "ceil"

class Floor(Function):
    _keyword = "floor"

class Rand(Function):
    _keyword = "RAND"
