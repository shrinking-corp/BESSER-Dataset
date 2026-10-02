from python_code import operators_OclExpression
from python_code import operators_OperationCallExp

def test_operators_OperationCallExp___init__():
    assert operators_OperationCallExp.__init__(operators_OperationCallExp('', operators_OperationCallExp=operators_OclExpression(), operators_OperationCallExp4=set()), '', operators_OperationCallExp=operators_OclExpression(), operators_OperationCallExp4=set()) == None

from python_code import operators_OclExpression
from python_code import operators_Type

def test_operators_Type___init__():
    assert operators_Type.__init__(operators_Type(operators_Type=operators_OclExpression()), operators_Type=operators_OclExpression()) == None

def test_operators_Type_isSameType():
    assert operators_Type.isSameType(operators_Type(operators_Type=operators_OclExpression()), '') == None

def test_operators_Type_isSuperTypeOf():
    assert operators_Type.isSuperTypeOf(operators_Type(operators_Type=operators_OclExpression()), '') == None
