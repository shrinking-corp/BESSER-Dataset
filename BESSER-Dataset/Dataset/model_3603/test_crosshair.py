from python_code import thingML_BooleanLiteral

def test_thingML_BooleanLiteral___init__():
    assert thingML_BooleanLiteral.__init__(thingML_BooleanLiteral(''), '') == None

from python_code import thingML_DoubleLiteral

def test_thingML_DoubleLiteral___init__():
    assert thingML_DoubleLiteral.__init__(thingML_DoubleLiteral(0.0), 0.0) == None

from python_code import thingML_EnumLiteralRef
from python_code import thingML_Enumeration
from python_code import thingML_EnumerationLiteral

def test_thingML_EnumerationLiteral___init__():
    assert thingML_EnumerationLiteral.__init__(thingML_EnumerationLiteral('', thingML_EnumerationLiteral=thingML_Enumeration(), thingML_EnumerationLiteral14=set(), thingML_EnumerationLiteral224=thingML_EnumLiteralRef()), '', thingML_EnumerationLiteral=thingML_Enumeration(), thingML_EnumerationLiteral14=set(), thingML_EnumerationLiteral224=thingML_EnumLiteralRef()) == None

from python_code import thingML_ExternExpression

def test_thingML_ExternExpression___init__():
    assert thingML_ExternExpression.__init__(thingML_ExternExpression('', thingML_ExternExpression=set()), '', thingML_ExternExpression=set()) == None

from python_code import thingML_ExternStatement

def test_thingML_ExternStatement___init__():
    assert thingML_ExternStatement.__init__(thingML_ExternStatement('', thingML_ExternStatement=set()), '', thingML_ExternStatement=set()) == None

from python_code import thingML_Action
from python_code import thingML_Expression
from python_code import thingML_Handler

def test_thingML_Handler___init__():
    assert thingML_Handler.__init__(thingML_Handler('', thingML_Handler=set(), thingML_Handler147=thingML_Expression(), thingML_Handler150=thingML_Action()), '', thingML_Handler=set(), thingML_Handler147=thingML_Expression(), thingML_Handler150=thingML_Action()) == None

from python_code import thingML_Import
from python_code import thingML_ThingMLModel

def test_thingML_Import___init__():
    assert thingML_Import.__init__(thingML_Import('', thingML_Import=thingML_ThingMLModel()), '', thingML_Import=thingML_ThingMLModel()) == None

from python_code import thingML_IntegerLiteral

def test_thingML_IntegerLiteral___init__():
    assert thingML_IntegerLiteral.__init__(thingML_IntegerLiteral(0), 0) == None

from python_code import thingML_PrimitiveType

def test_thingML_PrimitiveType___init__():
    assert thingML_PrimitiveType.__init__(thingML_PrimitiveType(0), 0) == None

from python_code import thingML_ExternalConnector
from python_code import thingML_Protocol
from python_code import thingML_ThingMLModel

def test_thingML_Protocol___init__():
    assert thingML_Protocol.__init__(thingML_Protocol('', thingML_Protocol=thingML_ThingMLModel(), thingML_Protocol274=thingML_ExternalConnector()), '', thingML_Protocol=thingML_ThingMLModel(), thingML_Protocol274=thingML_ExternalConnector()) == None

from python_code import thingML_Connector
from python_code import thingML_RequiredPort

def test_thingML_RequiredPort___init__():
    assert thingML_RequiredPort.__init__(thingML_RequiredPort(True, thingML_RequiredPort=thingML_Connector()), False, thingML_RequiredPort=thingML_Connector()) == None

from python_code import thingML_StringLiteral

def test_thingML_StringLiteral___init__():
    assert thingML_StringLiteral.__init__(thingML_StringLiteral(''), '') == None
