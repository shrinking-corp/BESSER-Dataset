from python_code import b_Abstraction
from python_code import b_ConcreteConstants
from python_code import b_Definitions
from python_code import b_Imports
from python_code import b_Operations
from python_code import b_Properties
from python_code import b_Sees

def test_b_Abstraction___init__():
    assert b_Abstraction.__init__(b_Abstraction('', b_Abstraction28=b_Sees(), b_Abstraction31=b_Imports(), b_Abstraction=b_Sees(), b_Abstraction2=b_ConcreteConstants(), b_Abstraction4=b_Definitions(), b_Abstraction6=b_Properties(), b_Abstraction8=b_Operations()), '', b_Abstraction28=b_Sees(), b_Abstraction31=b_Imports(), b_Abstraction=b_Sees(), b_Abstraction2=b_ConcreteConstants(), b_Abstraction4=b_Definitions(), b_Abstraction6=b_Properties(), b_Abstraction8=b_Operations()) == None


from python_code import b_BoolLiteral

def test_b_BoolLiteral___init__():
    assert b_BoolLiteral.__init__(b_BoolLiteral('', '\x00'), '\x00\x00', '') == None


from python_code import b_ConstantExpr

def test_b_ConstantExpr___init__():
    assert b_ConstantExpr.__init__(b_ConstantExpr(''), '') == None


from python_code import b_Definition
from python_code import b_DefinitionCall
from python_code import b_Definitions
from python_code import b_LogicalExpr

def test_b_Definition___init__():
    assert b_Definition.__init__(b_Definition('', b_Definition83=b_DefinitionCall(), b_Definition=b_Definitions(), b_Definition78=set(), b_Definition81=b_LogicalExpr()), '', b_Definition83=b_DefinitionCall(), b_Definition=b_Definitions(), b_Definition78=set(), b_Definition81=b_LogicalExpr()) == None


from python_code import b_InequalityExpr
from python_code import b_LogicalExpr

def test_b_InequalityExpr___init__():
    assert b_InequalityExpr.__init__(b_InequalityExpr('', b_InequalityExpr=b_LogicalExpr(), b_InequalityExpr184=b_LogicalExpr()), '', b_InequalityExpr=b_LogicalExpr(), b_InequalityExpr184=b_LogicalExpr()) == None


from python_code import b_IntLiteral

def test_b_IntLiteral___init__():
    assert b_IntLiteral.__init__(b_IntLiteral(0), 0) == None


from python_code import b_Body
from python_code import b_Call
from python_code import b_LocalOperations
from python_code import b_Operation
from python_code import b_Operations
from python_code import b_SimpleCall

def test_b_Operation___init__():
    assert b_Operation.__init__(b_Operation('', b_Operation158=b_SimpleCall(), b_Operation164=b_LocalOperations(), b_Operation=b_Operations(), b_Operation97=set(), b_Operation100=set(), b_Operation103=b_Body(), b_Operation153=b_Call()), '', b_Operation158=b_SimpleCall(), b_Operation164=b_LocalOperations(), b_Operation=b_Operations(), b_Operation97=set(), b_Operation100=set(), b_Operation103=b_Body(), b_Operation153=b_Call()) == None


from python_code import b_PrimitiveType

def test_b_PrimitiveType___init__():
    assert b_PrimitiveType.__init__(b_PrimitiveType(''), '') == None


from python_code import b_StringLiteral

def test_b_StringLiteral___init__():
    assert b_StringLiteral.__init__(b_StringLiteral(''), '') == None

