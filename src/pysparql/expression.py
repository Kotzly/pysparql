from typing import List, Union
from enum import Enum
from .functions.base import Function


class NumericOperator(Enum):
    EQ = "="
    GEQ = ">="
    LEQ = "<="
    GT = ">"
    LT = "<"
    NEQ = "!="


class SetOperator(Enum):
    IN = "IN"
    NOT_IN = "NOT IN"


class BoolOperator(Enum):
    AND = "&&"
    OR = "||"
    NOT = "!"
    NOP = ""


class AlgebraicOperator(Enum):
    MULT = "*"
    DIV = "/"
    ADD = "+"
    SUB = "-"
    NOP = ""


class Expression:
    def __init__(self, expression: Union["Expression", str]):
        self.expression = expression


class UnaryAlgExpression(Expression):
    _lhs = None
    _rhs: Union["NumericExpression", Function]
    _op: Union[AlgebraicOperator.ADD, AlgebraicOperator.SUB]


class UnaryBoolExpression(Expression):
    _lhs = None
    _rhs: Union["RelationalExpression", Function]
    _op: Union[BoolOperator.NOT, BoolOperator.NOP]


UnaryExpression = Union[UnaryAlgExpression, UnaryBoolExpression]


class NumericExpression(Expression):
    _lhs: Union["NumericExpression", Function]
    _rhs: Union["NumericExpression", Function]
    _op: AlgebraicOperator


class RelationalExpression(Expression):
    _lhs: Union["NumericExpression", Function]
    _rhs: Union["NumericExpression", Function]
    _op: NumericOperator


class SetExpression(Expression):
    _lhs: Union["NumericExpression", Function]
    _rhs: List[NumericExpression]
    _op: NumericOperator
