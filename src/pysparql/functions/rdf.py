from .base import Function


class isIRI(Function):
    _keyword = "isIRI"


class isBlank(Function):
    _keyword = "isBlank"


class isLiteral(Function):
    _keyword = "isLiteral"


class isNumeric(Function):
    _keyword = "isNumeric"


class Str(Function):
    _keyword = "str"


class Lang(Function):
    _keyword = "lang"


class Datatype(Function):
    _keyword = "datatype"


class IRI(Function):
    _keyword = "IRI"


class URI(Function):
    _keyword = "URI"


class BNODE(Function):
    _keyword = "BNODE"


class STRDT(Function):
    _keyword = "STRDT"


class STRLANG(Function):
    _keyword = "STRLANG"


class UUID(Function):
    _keyword = "UUID"


class STRUUID(Function):
    _keyword = "STRUUID"
