from .base import Function


class Bound(Function):
    _keyword = "BOUND"


class If(Function):
    _keyword = "IF"


class Coalesce(Function):
    _keyword = "COALESCE"
