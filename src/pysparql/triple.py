from pysparql.functions.rdf import IRI
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

    def to_string(self) -> str:
        return f"{self.s.to_string()} {self.p.to_string()} {self.o.to_string()} ."


PredicateObject = Tuple[Term, Term]


class SameSubjectTripleList(TriplePattern):
    def __init__(self, s: Term, po_list: List[PredicateObject]):
        self.s = s
        self.po_list = po_list

    def to_triple_list(self) -> List[Triple]:
        return [Triple(self.s, p, o) for p, o in self.po_list]

    def to_string(self) -> str:
        po_strings = [f"{p.to_string()} {o.to_string()}" for p, o in self.po_list]
        return f"{self.s.to_string()} " + " ;\n\t".join(po_strings) + " .\n"


class SameSubjectPredicateTripleList(TriplePattern):
    def __init__(self, s: Term, p: Term, o_list: List[Term]):
        self.s = s
        self.p = p
        self.o_list = o_list

    def to_triple_list(self) -> List[Triple]:
        return [Triple(self.s, self.p, o) for p, o in self.o_list]

    def to_string(self) -> str:
        o_strings = [o.to_string() for o in self.o_list]
        return f"{self.s.to_string()} {self.p.to_string()} " + " , ".join(o_strings) + " ."
    
if __name__ == "__main__":
    from .term import URIRef, Literal, Variable

    s = URIRef("http://example.org/subject")
    p1 = URIRef("http://example.org/predicate1")
    p2 = URIRef("http://example.org/predicate2")
    o1 = Literal("Object1")
    o2 = Literal("Object2")
    o3 = Variable("varObject")

    triple = Triple(s, p1, o1)
    print(triple.to_string())

    same_subject_triple_list = SameSubjectTripleList(s, [(p1, o1), (p2, o2)])
    print(same_subject_triple_list.to_string())

    same_subject_predicate_triple_list = SameSubjectPredicateTripleList(s, p1, [o1, o3])
    print(same_subject_predicate_triple_list.to_string())# https://www.w3.org/TR/sparql11-query/#GraphPattern
