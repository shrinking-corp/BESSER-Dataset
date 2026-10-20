from python_code import simplejava_BooleanExpression

def test_simplejava_BooleanExpression___init__():
    assert simplejava_BooleanExpression.__init__(simplejava_BooleanExpression(True), False) == None


from python_code import simplejava_Import
from python_code import simplejava_SimpleJava

def test_simplejava_Import___init__():
    assert simplejava_Import.__init__(simplejava_Import('', simplejava_Import=simplejava_SimpleJava()), '', simplejava_Import=simplejava_SimpleJava()) == None


from python_code import simplejava_IntegerExpression

def test_simplejava_IntegerExpression___init__():
    assert simplejava_IntegerExpression.__init__(simplejava_IntegerExpression(0), 0) == None


from python_code import simplejava_PackageDeclaration
from python_code import simplejava_SimpleJava

def test_simplejava_PackageDeclaration___init__():
    assert simplejava_PackageDeclaration.__init__(simplejava_PackageDeclaration('', simplejava_PackageDeclaration=simplejava_SimpleJava()), '', simplejava_PackageDeclaration=simplejava_SimpleJava()) == None


from python_code import simplejava_GenericExpression
from python_code import simplejava_IfStatement
from python_code import simplejava_ParanthesisOrBinaryExpression
from python_code import simplejava_WhileStatement

def test_simplejava_ParanthesisOrBinaryExpression___init__():
    assert simplejava_ParanthesisOrBinaryExpression.__init__(simplejava_ParanthesisOrBinaryExpression('', simplejava_ParanthesisOrBinaryExpression83=simplejava_GenericExpression(), simplejava_ParanthesisOrBinaryExpression86=simplejava_GenericExpression(), simplejava_ParanthesisOrBinaryExpression60=simplejava_WhileStatement(), simplejava_ParanthesisOrBinaryExpression=simplejava_IfStatement()), '', simplejava_ParanthesisOrBinaryExpression83=simplejava_GenericExpression(), simplejava_ParanthesisOrBinaryExpression86=simplejava_GenericExpression(), simplejava_ParanthesisOrBinaryExpression60=simplejava_WhileStatement(), simplejava_ParanthesisOrBinaryExpression=simplejava_IfStatement()) == None


from python_code import simplejava_StringExpression

def test_simplejava_StringExpression___init__():
    assert simplejava_StringExpression.__init__(simplejava_StringExpression(''), '') == None


from python_code import simplejava_GenericExpression
from python_code import simplejava_UnaryExpression

def test_simplejava_UnaryExpression___init__():
    assert simplejava_UnaryExpression.__init__(simplejava_UnaryExpression('', simplejava_UnaryExpression=simplejava_GenericExpression()), '', simplejava_UnaryExpression=simplejava_GenericExpression()) == None

