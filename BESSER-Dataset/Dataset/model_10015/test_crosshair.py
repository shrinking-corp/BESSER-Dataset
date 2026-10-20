from python_code import operators_ASSIGN
from python_code import operators_EAttribute
from python_code import operators_Referrable

def test_operators_ASSIGN___init__():
    assert operators_ASSIGN.__init__(operators_ASSIGN('', operators_ASSIGN=operators_EAttribute(), operators_ASSIGN14=operators_Referrable()), '', operators_ASSIGN=operators_EAttribute(), operators_ASSIGN14=operators_Referrable()) == None

def test_operators_ASSIGN_execute():
    assert operators_ASSIGN.execute(operators_ASSIGN('', operators_ASSIGN=operators_EAttribute(), operators_ASSIGN14=operators_Referrable())) == None


from python_code import operators_CREATE
from python_code import operators_EReference
from python_code import operators_Referrable
from python_code import operators_TypeVariable

def test_operators_CREATE___init__():
    assert operators_CREATE.__init__(operators_CREATE(operators_CREATE=operators_TypeVariable(), operators_CREATE3=operators_Referrable(), operators_CREATE5=operators_EReference()), operators_CREATE=operators_TypeVariable(), operators_CREATE3=operators_Referrable(), operators_CREATE5=operators_EReference()) == None

def test_operators_CREATE_execute():
    assert operators_CREATE.execute(operators_CREATE(operators_CREATE=operators_TypeVariable(), operators_CREATE3=operators_Referrable(), operators_CREATE5=operators_EReference())) == None


from python_code import operators_DELETE
from python_code import operators_Referrable

def test_operators_DELETE___init__():
    assert operators_DELETE.__init__(operators_DELETE(operators_DELETE=operators_Referrable()), operators_DELETE=operators_Referrable()) == None

def test_operators_DELETE_execute():
    assert operators_DELETE.execute(operators_DELETE(operators_DELETE=operators_Referrable())) == None


from python_code import operators_EReference
from python_code import operators_MOVE
from python_code import operators_Referrable

def test_operators_MOVE___init__():
    assert operators_MOVE.__init__(operators_MOVE(operators_MOVE=operators_Referrable(), operators_MOVE30=operators_EReference(), operators_MOVE33=operators_Referrable()), operators_MOVE=operators_Referrable(), operators_MOVE30=operators_EReference(), operators_MOVE33=operators_Referrable()) == None

def test_operators_MOVE_execute():
    assert operators_MOVE.execute(operators_MOVE(operators_MOVE=operators_Referrable(), operators_MOVE30=operators_EReference(), operators_MOVE33=operators_Referrable())) == None


from python_code import operators_Operator
from python_code import operators_Result

def test_operators_Operator___init__():
    assert operators_Operator.__init__(operators_Operator(True, operators_Operator=operators_Result()), False, operators_Operator=operators_Result()) == None

def test_operators_Operator_execute():
    assert operators_Operator.execute(operators_Operator(False, operators_Operator=operators_Result())) == None


from python_code import operators_PrimitiveReference

def test_operators_PrimitiveReference___init__():
    assert operators_PrimitiveReference.__init__(operators_PrimitiveReference(''), '') == None


from python_code import operators_EReference
from python_code import operators_Referrable
from python_code import operators_SET

def test_operators_SET___init__():
    assert operators_SET.__init__(operators_SET(operators_SET=operators_EReference(), operators_SET21=operators_Referrable(), operators_SET24=operators_Referrable()), operators_SET=operators_EReference(), operators_SET21=operators_Referrable(), operators_SET24=operators_Referrable()) == None

def test_operators_SET_execute():
    assert operators_SET.execute(operators_SET(operators_SET=operators_EReference(), operators_SET21=operators_Referrable(), operators_SET24=operators_Referrable())) == None


from python_code import operators_QueryVariable
from python_code import operators_VAR

def test_operators_VAR___init__():
    assert operators_VAR.__init__(operators_VAR(operators_VAR=operators_QueryVariable()), operators_VAR=operators_QueryVariable()) == None

def test_operators_VAR_execute():
    assert operators_VAR.execute(operators_VAR(operators_VAR=operators_QueryVariable())) == None


from python_code import operators_Variable
from python_code import operators_VariableReference

def test_operators_Variable___init__():
    assert operators_Variable.__init__(operators_Variable('', operators_Variable=operators_VariableReference()), '', operators_Variable=operators_VariableReference()) == None

