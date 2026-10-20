from python_code import robochart_AnyType

def test_robochart_AnyType___init__():
    assert robochart_AnyType.__init__(robochart_AnyType(''), '') == None


from python_code import robochart_BasicPackage

def test_robochart_BasicPackage___init__():
    assert robochart_BasicPackage.__init__(robochart_BasicPackage('\x00', robochart_BasicPackage=set()), '', robochart_BasicPackage=set()) == None


from python_code import robochart_BooleanExp

def test_robochart_BooleanExp___init__():
    assert robochart_BooleanExp.__init__(robochart_BooleanExp(''), '') == None


from python_code import robochart_Exists

def test_robochart_Exists___init__():
    assert robochart_Exists.__init__(robochart_Exists(True), False) == None


from python_code import robochart_FloatExp

def test_robochart_FloatExp___init__():
    assert robochart_FloatExp.__init__(robochart_FloatExp(0.0), 0.0) == None


from python_code import robochart_IntegerExp

def test_robochart_IntegerExp___init__():
    assert robochart_IntegerExp.__init__(robochart_IntegerExp(0), 0) == None


from python_code import robochart_MatrixType
from python_code import robochart_Type

def test_robochart_MatrixType___init__():
    assert robochart_MatrixType.__init__(robochart_MatrixType(0, 0, robochart_MatrixType=robochart_Type()), 0, 0, robochart_MatrixType=robochart_Type()) == None


from python_code import robochart_NamedElement

def test_robochart_NamedElement___init__():
    assert robochart_NamedElement.__init__(robochart_NamedElement(''), '') == None


from python_code import robochart_BasicContext
from python_code import robochart_Call
from python_code import robochart_OperationSig

def test_robochart_OperationSig___init__():
    assert robochart_OperationSig.__init__(robochart_OperationSig(False, robochart_OperationSig=set(), robochart_OperationSig51=set(), robochart_OperationSig54=set(), robochart_OperationSig62=robochart_BasicContext(), robochart_OperationSig183=robochart_Call()), True, robochart_OperationSig=set(), robochart_OperationSig51=set(), robochart_OperationSig54=set(), robochart_OperationSig62=robochart_BasicContext(), robochart_OperationSig183=robochart_Call()) == None


from python_code import robochart_Expression
from python_code import robochart_RangeExp

def test_robochart_RangeExp___init__():
    assert robochart_RangeExp.__init__(robochart_RangeExp('', '\x00', robochart_RangeExp=robochart_Expression(), robochart_RangeExp292=robochart_Expression()), '\x00\x00', '', robochart_RangeExp=robochart_Expression(), robochart_RangeExp292=robochart_Expression()) == None


from python_code import robochart_StringExp

def test_robochart_StringExp___init__():
    assert robochart_StringExp.__init__(robochart_StringExp(''), '') == None


from python_code import robochart_BasicContext
from python_code import robochart_VariableList

def test_robochart_VariableList___init__():
    assert robochart_VariableList.__init__(robochart_VariableList('', robochart_VariableList=set(), robochart_VariableList59=robochart_BasicContext()), '', robochart_VariableList=set(), robochart_VariableList59=robochart_BasicContext()) == None


from python_code import robochart_Type
from python_code import robochart_VectorType

def test_robochart_VectorType___init__():
    assert robochart_VectorType.__init__(robochart_VectorType(0, robochart_VectorType=robochart_Type()), 0, robochart_VectorType=robochart_Type()) == None

