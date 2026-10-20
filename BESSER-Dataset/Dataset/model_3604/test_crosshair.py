from python_code import thingML_BooleanLiteral

def test_thingML_BooleanLiteral___init__():
    assert thingML_BooleanLiteral.__init__(thingML_BooleanLiteral(True), False) == None


from python_code import thingML_ByteLiteral

def test_thingML_ByteLiteral___init__():
    assert thingML_ByteLiteral.__init__(thingML_ByteLiteral(''), '') == None


from python_code import thingML_CastExpression
from python_code import thingML_Expression
from python_code import thingML_Type

def test_thingML_CastExpression___init__():
    assert thingML_CastExpression.__init__(thingML_CastExpression(True, thingML_CastExpression=thingML_Expression(), thingML_CastExpression294=thingML_Type()), False, thingML_CastExpression=thingML_Expression(), thingML_CastExpression294=thingML_Type()) == None


from python_code import thingML_CharLiteral

def test_thingML_CharLiteral___init__():
    assert thingML_CharLiteral.__init__(thingML_CharLiteral(''), '') == None


from python_code import thingML_DoubleLiteral

def test_thingML_DoubleLiteral___init__():
    assert thingML_DoubleLiteral.__init__(thingML_DoubleLiteral(0.0), 0.0) == None


from python_code import thingML_ErrorAction

def test_thingML_ErrorAction___init__():
    assert thingML_ErrorAction.__init__(thingML_ErrorAction(False, thingML_ErrorAction=set()), False, thingML_ErrorAction=set()) == None


from python_code import thingML_ExternExpression

def test_thingML_ExternExpression___init__():
    assert thingML_ExternExpression.__init__(thingML_ExternExpression('', thingML_ExternExpression=set()), '', thingML_ExternExpression=set()) == None


from python_code import thingML_ExternStatement

def test_thingML_ExternStatement___init__():
    assert thingML_ExternStatement.__init__(thingML_ExternStatement('', thingML_ExternStatement=set()), '', thingML_ExternStatement=set()) == None


from python_code import thingML_Import
from python_code import thingML_ThingMLModel

def test_thingML_Import___init__():
    assert thingML_Import.__init__(thingML_Import('', '\x00', thingML_Import=thingML_ThingMLModel()), '\x00\x00', '', thingML_Import=thingML_ThingMLModel()) == None


from python_code import thingML_IntegerLiteral

def test_thingML_IntegerLiteral___init__():
    assert thingML_IntegerLiteral.__init__(thingML_IntegerLiteral(''), '') == None


from python_code import thingML_Expression
from python_code import thingML_LocalVariable

def test_thingML_LocalVariable___init__():
    assert thingML_LocalVariable.__init__(thingML_LocalVariable(True, thingML_LocalVariable=thingML_Expression()), False, thingML_LocalVariable=thingML_Expression()) == None


from python_code import thingML_NamedElement

def test_thingML_NamedElement___init__():
    assert thingML_NamedElement.__init__(thingML_NamedElement(''), '') == None


from python_code import thingML_AnnotatedElement
from python_code import thingML_ConfigPropertyAssign
from python_code import thingML_PlatformAnnotation

def test_thingML_PlatformAnnotation___init__():
    assert thingML_PlatformAnnotation.__init__(thingML_PlatformAnnotation('', '\x00', thingML_PlatformAnnotation=thingML_AnnotatedElement(), thingML_PlatformAnnotation208=thingML_ConfigPropertyAssign()), '\x00\x00', '', thingML_PlatformAnnotation=thingML_AnnotatedElement(), thingML_PlatformAnnotation208=thingML_ConfigPropertyAssign()) == None


from python_code import thingML_PrimitiveType

def test_thingML_PrimitiveType___init__():
    assert thingML_PrimitiveType.__init__(thingML_PrimitiveType(''), '') == None


from python_code import thingML_PrintAction

def test_thingML_PrintAction___init__():
    assert thingML_PrintAction.__init__(thingML_PrintAction(False, thingML_PrintAction=set()), False, thingML_PrintAction=set()) == None


from python_code import thingML_Connector
from python_code import thingML_RequiredPort

def test_thingML_RequiredPort___init__():
    assert thingML_RequiredPort.__init__(thingML_RequiredPort(True, thingML_RequiredPort=thingML_Connector()), False, thingML_RequiredPort=thingML_Connector()) == None


from python_code import thingML_State
from python_code import thingML_StateContainer

def test_thingML_StateContainer___init__():
    assert thingML_StateContainer.__init__(thingML_StateContainer(False, thingML_StateContainer=thingML_State(), thingML_StateContainer94=set()), False, thingML_StateContainer=thingML_State(), thingML_StateContainer94=set()) == None


from python_code import thingML_StringLiteral

def test_thingML_StringLiteral___init__():
    assert thingML_StringLiteral.__init__(thingML_StringLiteral(''), '') == None

