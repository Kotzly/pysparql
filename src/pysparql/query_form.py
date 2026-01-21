from pydantic import Field
from typing import List
from abc import ABC
from .dataset import Dataset
from .prologue import Prologue


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
    dataset: List[Dataset] = Field(...)
    query: QueryForm = Field(...)
    values: Values = Field(...)
    group_by = Field(...)
    having = Field(...)
    order = Field(...)
    limit = Field(...)
