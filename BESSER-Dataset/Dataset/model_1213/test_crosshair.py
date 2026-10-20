from python_code import eol_AnyType
from python_code import eol_MapType

def test_eol_AnyType___init__():
    assert eol_AnyType.__init__(eol_AnyType(False, eol_AnyType=set(), eol_AnyType223=eol_MapType(), eol_AnyType226=eol_MapType()), False, eol_AnyType=set(), eol_AnyType223=eol_MapType(), eol_AnyType226=eol_MapType()) == None


from python_code import eol_BooleanExpression

def test_eol_BooleanExpression___init__():
    assert eol_BooleanExpression.__init__(eol_BooleanExpression(True), False) == None


from python_code import eol_Expression
from python_code import eol_FeatureCallExpression

def test_eol_FeatureCallExpression___init__():
    assert eol_FeatureCallExpression.__init__(eol_FeatureCallExpression(True, eol_FeatureCallExpression=eol_Expression()), False, eol_FeatureCallExpression=eol_Expression()) == None


from python_code import eol_IntegerExpression

def test_eol_IntegerExpression___init__():
    assert eol_IntegerExpression.__init__(eol_IntegerExpression(0), 0) == None


from python_code import eol_RealExpression

def test_eol_RealExpression___init__():
    assert eol_RealExpression.__init__(eol_RealExpression(0.0), 0.0) == None


from python_code import eol_TextPosition
from python_code import eol_TextRegion

def test_eol_TextPosition___init__():
    assert eol_TextPosition.__init__(eol_TextPosition(0, 0, eol_TextPosition=eol_TextRegion(), eol_TextPosition22=eol_TextRegion()), 0, 0, eol_TextPosition=eol_TextRegion(), eol_TextPosition22=eol_TextRegion()) == None

