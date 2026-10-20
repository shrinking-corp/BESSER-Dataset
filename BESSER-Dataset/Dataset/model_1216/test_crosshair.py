from python_code import eol_IntegerExpression

def test_eol_IntegerExpression___init__():
    assert eol_IntegerExpression.__init__(eol_IntegerExpression(0), 0) == None


from python_code import eol_EClassifier
from python_code import eol_ModelDeclarationStatement
from python_code import eol_ModelElementType

def test_eol_ModelElementType___init__():
    assert eol_ModelElementType.__init__(eol_ModelElementType('', '\x00', eol_ModelElementType=eol_EClassifier(), eol_ModelElementType189=eol_ModelDeclarationStatement()), '\x00\x00', '', eol_ModelElementType=eol_EClassifier(), eol_ModelElementType189=eol_ModelDeclarationStatement()) == None


from python_code import eol_RealExpression

def test_eol_RealExpression___init__():
    assert eol_RealExpression.__init__(eol_RealExpression(0.0), 0.0) == None


from python_code import eol_Import
from python_code import eol_ModelDeclarationParameter
from python_code import eol_NativeExpression
from python_code import eol_NativeType
from python_code import eol_SimpleAnnotation
from python_code import eol_StringExpression

def test_eol_StringExpression___init__():
    assert eol_StringExpression.__init__(eol_StringExpression('', eol_StringExpression=eol_Import(), eol_StringExpression180=eol_SimpleAnnotation(), eol_StringExpression192=eol_NativeType(), eol_StringExpression204=eol_ModelDeclarationParameter(), eol_StringExpression227=eol_NativeExpression()), '', eol_StringExpression=eol_Import(), eol_StringExpression180=eol_SimpleAnnotation(), eol_StringExpression192=eol_NativeType(), eol_StringExpression204=eol_ModelDeclarationParameter(), eol_StringExpression227=eol_NativeExpression()) == None


from python_code import eol_TextPosition
from python_code import eol_TextRegion

def test_eol_TextPosition___init__():
    assert eol_TextPosition.__init__(eol_TextPosition(0, 0, eol_TextPosition=eol_TextRegion(), eol_TextPosition8=eol_TextRegion()), 0, 0, eol_TextPosition=eol_TextRegion(), eol_TextPosition8=eol_TextRegion()) == None

