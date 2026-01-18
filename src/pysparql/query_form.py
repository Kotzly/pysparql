from pydantic import Field
from typing import List, Union
from abc import ABC


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



class Prologue():
    base: str = Field(...)
    prefix_list: List[str] = Field(...)
    

class Values():
    pass



class QueryUnit():
    prologue: Prologue = Field(...)
    query: QueryForm = Field(...)
    values: Values = Field(...)