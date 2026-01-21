# https://www.w3.org/TR/sparql11-query/#GraphPattern
# When using blank nodes of the form _:abc,  labels for blank nodes are scoped to the basic graph pattern.
# A label can be used in only a single basic graph pattern in any query.

from abc import ABC
from pydantic import Field
from typing import List
from .filter import Filter
from .triple import TriplePattern


class GraphPattern(ABC):
    def union(self):
        pass


class BasicGraphPattern(GraphPattern):
    # https://www.w3.org/TR/sparql11-query/#BasicGraphPatterns
    _triple_patterns: List[TriplePattern] = Field(..., default_factory=list)


class GroupGraphPattern(GraphPattern):
    _filters: List[Filter] = Field(..., default_factory=list)
    _graph_patterns: List[GraphPattern] = Field(...)


class OptionalGraphPattern(BasicGraphPattern):
    _keyword: str = Field("OPTIONAL")


class AlternativeGraphPattern(GraphPattern):
    # Union
    _graph_patterns: GraphPattern = Field(...)


class EmptyGroupPattern(GraphPattern):
    _graph_patterns = Field(..., default_factory=list)


class MinusGraphPattern(GraphPattern):
    pass


# class NamedGraphPattern(GraphPattern):
#    pass
