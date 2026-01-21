from .base import Function


class StrStarts(Function):
    _keyword = "STRSTARTS"


class StrEnds(Function):
    _keyword = "STRENDS"


class Contains(Function):
    _keyword = "CONTAINS"


class StrBefore(Function):
    _keyword = "STRBEFORE"


class StrAfter(Function):
    _keyword = "STRAFTER"


class StrLen(Function):
    _keyword = "STRLEN"


class SubStr(Function):
    _keyword = "SUBSTR"


class UCase(Function):
    _keyword = "UCASE"


class LCase(Function):
    _keyword = "LCASE"


class EncodeForUri(Function):
    _keyword = "ENCODE_FOR_URI"


class Concat(Function):
    _keyword = "CONCAT"


class langMatches(Function):
    _keyword = "langMatches"


class Replace(Function):
    _keyword = "REPLACE"
