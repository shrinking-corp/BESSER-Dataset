from python_code import thingml_BooleanLiteral

def test_thingml_BooleanLiteral___init__():
    assert thingml_BooleanLiteral.__init__(thingml_BooleanLiteral(True), False) == None


from python_code import thingml_ConfigInclude
from python_code import thingml_Configuration
from python_code import thingml_ThingMLModel

def test_thingml_Configuration___init__():
    assert thingml_Configuration.__init__(thingml_Configuration(False, thingml_Configuration=thingml_ThingMLModel(), thingml_Configuration151=set(), thingml_Configuration153=set(), thingml_Configuration155=set(), thingml_Configuration157=set(), thingml_Configuration187=thingml_ConfigInclude()), False, thingml_Configuration=thingml_ThingMLModel(), thingml_Configuration151=set(), thingml_Configuration153=set(), thingml_Configuration155=set(), thingml_Configuration157=set(), thingml_Configuration187=thingml_ConfigInclude()) == None


from python_code import thingml_DoubleLiteral

def test_thingml_DoubleLiteral___init__():
    assert thingml_DoubleLiteral.__init__(thingml_DoubleLiteral(0.0), 0.0) == None


from python_code import thingml_ExternExpression

def test_thingml_ExternExpression___init__():
    assert thingml_ExternExpression.__init__(thingml_ExternExpression('', thingml_ExternExpression=set()), '', thingml_ExternExpression=set()) == None


from python_code import thingml_ExternStatement

def test_thingml_ExternStatement___init__():
    assert thingml_ExternStatement.__init__(thingml_ExternStatement('', thingml_ExternStatement=set()), '', thingml_ExternStatement=set()) == None


from python_code import thingml_IntegerLiteral

def test_thingml_IntegerLiteral___init__():
    assert thingml_IntegerLiteral.__init__(thingml_IntegerLiteral(0), 0) == None


from python_code import thingml_Expression
from python_code import thingml_LocalVariable

def test_thingml_LocalVariable___init__():
    assert thingml_LocalVariable.__init__(thingml_LocalVariable(True, thingml_LocalVariable=thingml_Expression()), False, thingml_LocalVariable=thingml_Expression()) == None


from python_code import thingml_AnnotatedElement
from python_code import thingml_PlatformAnnotation

def test_thingml_PlatformAnnotation___init__():
    assert thingml_PlatformAnnotation.__init__(thingml_PlatformAnnotation('', thingml_PlatformAnnotation=thingml_AnnotatedElement()), '', thingml_PlatformAnnotation=thingml_AnnotatedElement()) == None


from python_code import thingml_Region
from python_code import thingml_State

def test_thingml_Region___init__():
    assert thingml_Region.__init__(thingml_Region(False, thingml_Region=set(), thingml_Region77=thingml_State()), False, thingml_Region=set(), thingml_Region77=thingml_State()) == None


from python_code import thingml_Connector
from python_code import thingml_RequiredPort

def test_thingml_RequiredPort___init__():
    assert thingml_RequiredPort.__init__(thingml_RequiredPort(True, thingml_RequiredPort=thingml_Connector()), False, thingml_RequiredPort=thingml_Connector()) == None


from python_code import thingml_StringLiteral

def test_thingml_StringLiteral___init__():
    assert thingml_StringLiteral.__init__(thingml_StringLiteral(''), '') == None


from python_code import thingml_ThingMLElement

def test_thingml_ThingMLElement___init__():
    assert thingml_ThingMLElement.__init__(thingml_ThingMLElement(''), '') == None

