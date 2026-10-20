from python_code import logiclanguage_Assertion
from python_code import logiclanguage_Term

def test_logiclanguage_Assertion___init__():
    assert logiclanguage_Assertion.__init__(logiclanguage_Assertion('', logiclanguage_Assertion=logiclanguage_Term(), target75=set()), '', logiclanguage_Assertion=logiclanguage_Term(), target75=set()) == None


from python_code import logiclanguage_BoolLiteral

def test_logiclanguage_BoolLiteral___init__():
    assert logiclanguage_BoolLiteral.__init__(logiclanguage_BoolLiteral(True), False) == None


from python_code import logiclanguage_IntLiteral

def test_logiclanguage_IntLiteral___init__():
    assert logiclanguage_IntLiteral.__init__(logiclanguage_IntLiteral(0), 0) == None


from python_code import logiclanguage_ProjectedAggregateExpression

def test_logiclanguage_ProjectedAggregateExpression___init__():
    assert logiclanguage_ProjectedAggregateExpression.__init__(logiclanguage_ProjectedAggregateExpression(0), 0) == None


from python_code import logiclanguage_RealLiteral

def test_logiclanguage_RealLiteral___init__():
    assert logiclanguage_RealLiteral.__init__(logiclanguage_RealLiteral(''), '') == None


from python_code import logiclanguage_StringLiteral

def test_logiclanguage_StringLiteral___init__():
    assert logiclanguage_StringLiteral.__init__(logiclanguage_StringLiteral(''), '') == None


from python_code import logiclanguage_SymbolicDeclaration
from python_code import logiclanguage_SymbolicValue

def test_logiclanguage_SymbolicDeclaration___init__():
    assert logiclanguage_SymbolicDeclaration.__init__(logiclanguage_SymbolicDeclaration('', logiclanguage_SymbolicDeclaration=logiclanguage_SymbolicValue()), '', logiclanguage_SymbolicDeclaration=logiclanguage_SymbolicValue()) == None

