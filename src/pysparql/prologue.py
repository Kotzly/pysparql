from pydantic import List, Field
from .term import URIRef
from typing import Optional


class Prefix:
    _prefix_name: str
    _uri: URIRef


class Prologue:
    _base: Optional[URIRef] = Field(..., default_factory=list)
    _prefix_list: List[Prefix]
