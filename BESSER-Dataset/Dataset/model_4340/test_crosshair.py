from python_code import tExp_Cardinality

def test_tExp_Cardinality___init__():
    assert tExp_Cardinality.__init__(tExp_Cardinality(0, 0), 0, 0) == None

from python_code import tExp_NumberExpression

def test_tExp_NumberExpression___init__():
    assert tExp_NumberExpression.__init__(tExp_NumberExpression(''), '') == None

from python_code import tExp_Singletons

def test_tExp_Singletons___init__():
    assert tExp_Singletons.__init__(tExp_Singletons(0, 0), 0, 0) == None

from python_code import tExp_Size

def test_tExp_Size___init__():
    assert tExp_Size.__init__(tExp_Size(0, 0), 0, 0) == None

from python_code import tExp_StringExpression

def test_tExp_StringExpression___init__():
    assert tExp_StringExpression.__init__(tExp_StringExpression(''), '') == None

from python_code import tExp_VariableExpression

def test_tExp_VariableExpression___init__():
    assert tExp_VariableExpression.__init__(tExp_VariableExpression(''), '') == None
