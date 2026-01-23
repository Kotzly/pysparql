# https://www.w3.org/TR/sparql11-query/#GraphPattern
# When using blank nodes of the form _:abc,  labels for blank nodes are scoped to the basic graph pattern.
# A label can be used in only a single basic graph pattern in any query.

from abc import ABC
from pydantic import Field
from typing import List
from .filter import Filter
from .triple import TriplePattern
from .bind import Binding
from .values import Values
from .term import Term





class BasicGraphPattern(GraphPattern):
    # https://www.w3.org/TR/sparql11-query/#BasicGraphPatterns
    _triple_patterns: List[TriplePattern] = Field(..., default_factory=list)
    _binds: Binding = Field(...)
    _values: Values = Field(...)
    _graph: Term = Field(...)

    def to_string(self) -> str:
        parts = []
        if self._graph:
            parts.append(f"GRAPH {self._graph.to_string()} {{")
        for tp in self._triple_patterns:
            parts.append(tp.to_string())
        if self._binds:
            parts.append(self._binds.to_string())
        if self._values:
            parts.append(self._values.to_string())
        if self._graph:
            parts.append("}")
        return "\n".join(parts)


class GroupGraphPattern(GraphPattern):
    _filters: List[Filter] = Field(..., default_factory=list)
    _graph_patterns: List[GraphPattern] = Field(...)


class OptionalGraphPattern(BasicGraphPattern):
    _keyword: str = Field("OPTIONAL")


class AlternativeGraphPattern(GraphPattern):
    # Union
    _graph_patterns: List[GraphPattern] = Field(..., default_factory=list)


class EmptyGroupPattern(GraphPattern):
    _graph_patterns: List[GraphPattern] = Field(..., default_factory=list)


class MinusGraphPattern(GraphPattern):
    _keyword: str = Field("MINUS")


# class NamedGraphPattern(GraphPattern):
#    pass

class ServiceGraphPattern(GraphPattern):
    _keyword: str = Field("SERVICE")
    _silent: bool = Field(False)
    _service_iri: Term = Field(...)
    _graph_pattern: GraphPattern = Field(...)

if __name__ == "__main__":
    from .term import URIRef, Literal, Variable
    from .triple import Triple
    from .filter import Filter

    s = URIRef("http://example.org/subject")
    p = URIRef("http://example.org/predicate")
    o = Literal("Object")

    triple = Triple(s, p, o)

    bgp = BasicGraphPattern(
        _triple_patterns=[triple]
    )

    print(bgp.to_string()) 