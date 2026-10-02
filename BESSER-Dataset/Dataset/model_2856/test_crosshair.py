from python_code import ir_BinaryExpression
from python_code import ir_Expression

def test_ir_BinaryExpression___init__():
    assert ir_BinaryExpression.__init__(ir_BinaryExpression('', ir_BinaryExpression=ir_Expression(), ir_BinaryExpression80=ir_Expression()), '', ir_BinaryExpression=ir_Expression(), ir_BinaryExpression80=ir_Expression()) == None

from python_code import ir_BooleanLiteral

def test_ir_BooleanLiteral___init__():
    assert ir_BooleanLiteral.__init__(ir_BooleanLiteral(True), False) == None

from python_code import ir_FloatLiteral

def test_ir_FloatLiteral___init__():
    assert ir_FloatLiteral.__init__(ir_FloatLiteral(0.0), 0.0) == None

from python_code import ir_IntegerLiteral

def test_ir_IntegerLiteral___init__():
    assert ir_IntegerLiteral.__init__(ir_IntegerLiteral(''), '') == None

from python_code import ir_Member
from python_code import ir_Type
from python_code import ir_VariableExpression
from python_code import ir_VariableReference

def test_ir_Member___init__():
    assert ir_Member.__init__(ir_Member('', ir_Member119=ir_VariableReference(), ir_Member72=set(), ir_Member75=ir_Type(), ir_Member=ir_VariableExpression()), '', ir_Member119=ir_VariableReference(), ir_Member72=set(), ir_Member75=ir_Type(), ir_Member=ir_VariableExpression()) == None

from python_code import ir_Namespace

def test_ir_Namespace___init__():
    assert ir_Namespace.__init__(ir_Namespace('', ir_Namespace=set()), '', ir_Namespace=set()) == None

from python_code import ir_Node

def test_ir_Node___init__():
    assert ir_Node.__init__(ir_Node('', ir_Node=set()), '', ir_Node=set()) == None

from python_code import ir_AbstractActor
from python_code import ir_FromSource
from python_code import ir_Port
from python_code import ir_PortAccess
from python_code import ir_ToSink
from python_code import ir_Type

def test_ir_Port___init__():
    assert ir_Port.__init__(ir_Port('', ir_Port=ir_AbstractActor(), ir_Port13=ir_AbstractActor(), ir_Port106=ir_FromSource(), ir_Port34=ir_Type(), ir_Port111=ir_ToSink(), ir_Port159=ir_PortAccess()), '', ir_Port=ir_AbstractActor(), ir_Port13=ir_AbstractActor(), ir_Port106=ir_FromSource(), ir_Port34=ir_Type(), ir_Port111=ir_ToSink(), ir_Port159=ir_PortAccess()) == None

from python_code import ir_ActorInstance
from python_code import ir_FromSource
from python_code import ir_Point2PointConnection
from python_code import ir_PortInstance
from python_code import ir_ToSink

def test_ir_PortInstance___init__():
    assert ir_PortInstance.__init__(ir_PortInstance('', ir_PortInstance40=ir_ActorInstance(), ir_PortInstance44=set(), ir_PortInstance47=ir_ActorInstance(), ir_PortInstance108=ir_ToSink(), ir_PortInstance=ir_ActorInstance(), ir_PortInstance98=ir_Point2PointConnection(), ir_PortInstance101=ir_Point2PointConnection(), ir_PortInstance103=ir_FromSource()), '', ir_PortInstance40=ir_ActorInstance(), ir_PortInstance44=set(), ir_PortInstance47=ir_ActorInstance(), ir_PortInstance108=ir_ToSink(), ir_PortInstance=ir_ActorInstance(), ir_PortInstance98=ir_Point2PointConnection(), ir_PortInstance101=ir_Point2PointConnection(), ir_PortInstance103=ir_FromSource()) == None

from python_code import ir_Guard
from python_code import ir_PortPeek
from python_code import ir_VariableReference

def test_ir_PortPeek___init__():
    assert ir_PortPeek.__init__(ir_PortPeek(0, ir_PortPeek211=ir_Guard(), ir_PortPeek=ir_VariableReference()), 0, ir_PortPeek211=ir_Guard(), ir_PortPeek=ir_VariableReference()) == None

from python_code import ir_StringLiteral

def test_ir_StringLiteral___init__():
    assert ir_StringLiteral.__init__(ir_StringLiteral(''), '') == None

from python_code import ir_AbstractActor
from python_code import ir_TypeActor

def test_ir_TypeActor___init__():
    assert ir_TypeActor.__init__(ir_TypeActor('', '\x00', ir_TypeActor=ir_AbstractActor()), '\x00\x00', '', ir_TypeActor=ir_AbstractActor()) == None

from python_code import ir_TypeDeclarationImport

def test_ir_TypeDeclarationImport___init__():
    assert ir_TypeDeclarationImport.__init__(ir_TypeDeclarationImport(''), '') == None

from python_code import ir_Expression
from python_code import ir_UnaryExpression

def test_ir_UnaryExpression___init__():
    assert ir_UnaryExpression.__init__(ir_UnaryExpression('', ir_UnaryExpression=ir_Expression()), '', ir_UnaryExpression=ir_Expression()) == None

from python_code import ir_AbstractActor
from python_code import ir_Expression
from python_code import ir_LambdaExpression
from python_code import ir_ProcExpression
from python_code import ir_Type
from python_code import ir_TypeConstructor
from python_code import ir_TypeRecord
from python_code import ir_Variable
from python_code import ir_VariableReference

def test_ir_Variable___init__():
    assert ir_Variable.__init__(ir_Variable(False, False, ir_Variable=ir_AbstractActor(), ir_Variable113=ir_VariableReference(), ir_Variable189=ir_LambdaExpression(), ir_Variable183=ir_Expression(), ir_Variable186=ir_Type(), ir_Variable194=ir_ProcExpression(), ir_Variable197=ir_ProcExpression(), ir_Variable224=ir_TypeRecord(), ir_Variable240=ir_TypeConstructor()), False, False, ir_Variable=ir_AbstractActor(), ir_Variable113=ir_VariableReference(), ir_Variable189=ir_LambdaExpression(), ir_Variable183=ir_Expression(), ir_Variable186=ir_Type(), ir_Variable194=ir_ProcExpression(), ir_Variable197=ir_ProcExpression(), ir_Variable224=ir_TypeRecord(), ir_Variable240=ir_TypeConstructor()) == None

from python_code import ir_VariableImport

def test_ir_VariableImport___init__():
    assert ir_VariableImport.__init__(ir_VariableImport(''), '') == None
