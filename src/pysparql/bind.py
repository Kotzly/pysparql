from pydantic import Field
from .expression import Expression


class Binding:
    _keyword = Field("BIND")
    _expression: Expression = Field(...)
