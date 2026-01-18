from abc import ABC
from rdflib.term import URIRef, BNode, Variable, Literal
from typing import Union
from pydantic import Field

Term = Union[URIRef, BNode, Variable, Literal]


