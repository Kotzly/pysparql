# https://www.w3.org/TR/sparql11-query/#GraphPattern
# When using blank nodes of the form _:abc,  labels for blank nodes are scoped to the basic graph pattern.
# A label can be used in only a single basic graph pattern in any query.

from abc import ABC
from pydantic import Field
from typing import List
from .filter import Filter
from triple import Triple

class GraphPattern(ABC):
    _filters: Filter = Field(..., default_factory=list)
    _triples: List[Triple]

    def union(self):
        pass

class BasicGraphPattern(GraphPattern):
    pass

class GroupGraphPattern(GraphPattern):
    _graph_patterns: List[GraphPattern] = Field(...)

class OptionalGraphPattern(GraphPattern):
    _keyword: str = Field("OPTIONAL")

class AlternativeGraphPattern(GraphPattern):
    # Union
    _graph_patterns: GraphPattern = Field(...)
    
class MinusGraphPattern(GraphPattern):
    pass



# class NamedGraphPattern(GraphPattern):
#    pass

