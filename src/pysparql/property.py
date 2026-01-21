from typing import List, Union
from .term import Term


class Predicate:
    predicate: Union[Term, str, "Predicate"]

    def __init__(self, predicate: Union[Term, str, "Predicate"]):
        self.predicate = predicate
        if isinstance(predicate, Predicate):
            return predicate


class InversePredicate(Predicate):
    _prefix = "^"

    def __neg__(self):
        return Predicate(self.predicate)


class SequencePredicate(Predicate):
    _delimiter = "/"
    predicates: List[Predicate]


class AlternativePredicate(Predicate):
    _delimiter = "|"
    predicates: List[Predicate]


class ZeroOrMorePredicate(Predicate):
    _suffix = "*"
    pass


class OneOrMorePredicate(Predicate):
    _suffix = "+"
    pass


class ZeroOrOnePredicate(Predicate):
    _suffix = "?"
    pass


class NegatedPredicate(Predicate):
    predicate: Union[Term, str, "Predicate"]


# TODO
# NegatedPropertySet
