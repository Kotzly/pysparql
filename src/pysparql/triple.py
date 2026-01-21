from .term import Term
from typing import List, Tuple
from abc import ABC


class TriplePattern(ABC):
    pass


class Triple(TriplePattern):
    def __init__(self, s: Term, p: Term, o: Term):
        self.s = s
        self.p = p
        self.o = o


PredicateObject = Tuple[Term, Term]


class SameSubjectTripleList(TriplePattern):
    def __init__(self, s: Term, po_list: List[PredicateObject]):
        self.s = s
        self.po_list = po_list

    def to_triple_list(self) -> List[Triple]:
        return [Triple(self.s, p, o) for p, o in self.po_list]
