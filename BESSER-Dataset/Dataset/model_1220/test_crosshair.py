from python_code import eol_AnyType
from python_code import eol_MapType

def test_eol_AnyType___init__():
    assert eol_AnyType.__init__(eol_AnyType(False, eol_AnyType184=eol_MapType(), eol_AnyType187=eol_MapType(), eol_AnyType=set()), False, eol_AnyType184=eol_MapType(), eol_AnyType187=eol_MapType(), eol_AnyType=set()) == None


from python_code import eol_BooleanExpression

def test_eol_BooleanExpression___init__():
    assert eol_BooleanExpression.__init__(eol_BooleanExpression(True), False) == None


from python_code import eol_IntegerExpression

def test_eol_IntegerExpression___init__():
    assert eol_IntegerExpression.__init__(eol_IntegerExpression(0), 0) == None


from python_code import eol_ModelType

def test_eol_ModelType___init__():
    assert eol_ModelType.__init__(eol_ModelType('', '\x00'), '\x00\x00', '') == None


from python_code import eol_RealExpression

def test_eol_RealExpression___init__():
    assert eol_RealExpression.__init__(eol_RealExpression(0.0), 0.0) == None


from python_code import eol_NativeType
from python_code import eol_SimpleAnnotationStatement
from python_code import eol_StringExpression

def test_eol_StringExpression___init__():
    assert eol_StringExpression.__init__(eol_StringExpression('', eol_StringExpression=eol_SimpleAnnotationStatement(), eol_StringExpression189=eol_NativeType()), '', eol_StringExpression=eol_SimpleAnnotationStatement(), eol_StringExpression189=eol_NativeType()) == None

