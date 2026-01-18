from pydantic import Field
from typing import List, Union
from abc import ABC
from .term import Term

class Predicate():
    predicate: Union[Term, str, 'Predicate']
    def __init__(self, predicate: Union[Term, str, 'Predicate']):
        self.predicate = predicate
        if isinstance(predicate, Predicate):
            return predicate

class InversePredicate(Predicate):
    def __neg__(self):
        return Predicate(self.predicate)

class SequencePredicate(Predicate):
    predicates: List[Predicate]

class AlternativePredicate(Predicate):
    predicates: List[Predicate]

class ZeroOrMorePredicate(Predicate):
    pass

class OneOrMorePredicate(Predicate):
    pass

class ZeroOrOnePredicate(Predicate):
    pass

class NegatedPredicate(Predicate):
    predicate: Union[Term, str, 'Predicate']

# TODO
# NegatedPropertySet






