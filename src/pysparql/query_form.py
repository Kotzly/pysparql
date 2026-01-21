from pydantic import Field
from typing import List, Optional
from abc import ABC
from .dataset import Dataset
from .prologue import Prologue
from .filter import Filter
from .graph_pattern import GroupGraphPattern
from .slice import Limit, Offset
from .order import Order
from .group_by import GroupBy


class QueryForm(ABC):
    pass


class SelectQuery(QueryForm):
    pass


class ConstructQuery(QueryForm):
    pass


class DescribeQuery(QueryForm):
    pass


class AskQuery(QueryForm):
    pass


class Values:
    pass


# In this step, we process clauses on the query level in the following order:
# Grouping
# Aggregates
# HAVING
# VALUES
# Select expressions

# Solutions modifiers apply to the processing of a SPARQL query after pattern matching. The solution modifiers are applied to a query in the following order:
# Order by
# Projection
# Distinct
# Reduced
# Offset
# Limit


class QueryUnit:
    prologue: Prologue = Field(...)
    datasets: List[Dataset] = Field(...)
    where: GroupGraphPattern = Field(...)
    group_by: Optional[GroupBy] = Field(...)
    having: Optional[Filter] = Field(...)
    order: Optional[Order] = Field(None)
    offset: Optional[Offset] = Field(None)
    limit: Optional[Limit] = Field(None)
