from python_code import altarica_AbstractDomain
from python_code import altarica_Domain
from python_code import altarica_DomainRef

def test_altarica_Domain___init__():
    assert altarica_Domain.__init__(altarica_Domain('', altarica_Domain=altarica_AbstractDomain(), altarica_Domain47=altarica_DomainRef()), '', altarica_Domain=altarica_AbstractDomain(), altarica_Domain47=altarica_DomainRef()) == None


from python_code import altarica_EBoolean

def test_altarica_EBoolean___init__():
    assert altarica_EBoolean.__init__(altarica_EBoolean(''), '') == None


from python_code import altarica_EInteger

def test_altarica_EInteger___init__():
    assert altarica_EInteger.__init__(altarica_EInteger(0), 0) == None


from python_code import altarica_EString

def test_altarica_EString___init__():
    assert altarica_EString.__init__(altarica_EString(''), '') == None


from python_code import altarica_ExternalDirective
from python_code import altarica_ExternalSpecification

def test_altarica_ExternalDirective___init__():
    assert altarica_ExternalDirective.__init__(altarica_ExternalDirective('', altarica_ExternalDirective=altarica_ExternalSpecification()), '', altarica_ExternalDirective=altarica_ExternalSpecification()) == None


from python_code import altarica_EventRef
from python_code import altarica_NavigableVariable
from python_code import altarica_NestedQualifiedEventRef
from python_code import altarica_NestedQualifiedVariableRef
from python_code import altarica_VariableRef

def test_altarica_NavigableVariable___init__():
    assert altarica_NavigableVariable.__init__(altarica_NavigableVariable('', altarica_NavigableVariable=altarica_EventRef(), altarica_NavigableVariable106=altarica_VariableRef(), altarica_NavigableVariable176=altarica_NestedQualifiedEventRef(), altarica_NavigableVariable181=altarica_NestedQualifiedVariableRef()), '', altarica_NavigableVariable=altarica_EventRef(), altarica_NavigableVariable106=altarica_VariableRef(), altarica_NavigableVariable176=altarica_NestedQualifiedEventRef(), altarica_NavigableVariable181=altarica_NestedQualifiedVariableRef()) == None


from python_code import altarica_Node
from python_code import altarica_NodeInstanceDeclaration

def test_altarica_Node___init__():
    assert altarica_Node.__init__(altarica_Node(False, '\x00', altarica_Node=set(), altarica_Node53=altarica_NodeInstanceDeclaration()), False, '', altarica_Node=set(), altarica_Node53=altarica_NodeInstanceDeclaration()) == None


from python_code import altarica_PrimitiveType

def test_altarica_PrimitiveType___init__():
    assert altarica_PrimitiveType.__init__(altarica_PrimitiveType(''), '') == None


from python_code import altarica_EventRef
from python_code import altarica_Vector
from python_code import altarica_VectorParameter

def test_altarica_VectorParameter___init__():
    assert altarica_VectorParameter.__init__(altarica_VectorParameter(True, altarica_VectorParameter=altarica_Vector(), altarica_VectorParameter63=altarica_EventRef()), False, altarica_VectorParameter=altarica_Vector(), altarica_VectorParameter63=altarica_EventRef()) == None

