from rdflib.term import URIRef as _URIRef, BNode as _BNode, Variable as _Variable, Literal as _Literal
from typing import Union


# Redefine rdflib object`s toPython method as to_string method

class URIRef(_URIRef):
    def to_string(self) -> str:
        return f"<{str(self)}>"

class BNode(_BNode):
    def to_string(self) -> str:
        return f"_:{str(self)}"

class Variable(_Variable):
    def to_string(self) -> str:
        return f"?{str(self)}"

class Literal(_Literal):
    def to_string(self) -> str:
        if self.language:
            return f"\"{str(self)}\"@{self.language}"
        elif self.datatype:
            return f"\"{str(self)}\"^^{self.datatype.to_string()}"
        else:
            return f"\"{str(self)}\""

Term = Union[URIRef, BNode, Variable, Literal]
