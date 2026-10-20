from python_code import altarica_ARBoolean

def test_altarica_ARBoolean___init__():
    assert altarica_ARBoolean.__init__(altarica_ARBoolean(''), '') == None


from python_code import altarica_ARNumber

def test_altarica_ARNumber___init__():
    assert altarica_ARNumber.__init__(altarica_ARNumber(0.0), 0.0) == None


from python_code import altarica_ARString

def test_altarica_ARString___init__():
    assert altarica_ARString.__init__(altarica_ARString(''), '') == None


from python_code import altarica_Addition
from python_code import altarica_Expression

def test_altarica_Addition___init__():
    assert altarica_Addition.__init__(altarica_Addition('', altarica_Addition=altarica_Expression(), altarica_Addition98=altarica_Expression()), '', altarica_Addition=altarica_Expression(), altarica_Addition98=altarica_Expression()) == None


from python_code import altarica_BaseType

def test_altarica_BaseType___init__():
    assert altarica_BaseType.__init__(altarica_BaseType(''), '') == None


from python_code import altarica_Equal
from python_code import altarica_Expression

def test_altarica_Equal___init__():
    assert altarica_Equal.__init__(altarica_Equal('', altarica_Equal=altarica_Expression(), altarica_Equal93=altarica_Expression()), '', altarica_Equal=altarica_Expression(), altarica_Equal93=altarica_Expression()) == None


from python_code import altarica_Error
from python_code import altarica_Model

def test_altarica_Error___init__():
    assert altarica_Error.__init__(altarica_Error('', '\x00', altarica_Error=altarica_Model()), '\x00\x00', '', altarica_Error=altarica_Model()) == None


from python_code import altarica_FunctionCall

def test_altarica_FunctionCall___init__():
    assert altarica_FunctionCall.__init__(altarica_FunctionCall('', altarica_FunctionCall=set()), '', altarica_FunctionCall=set()) == None


from python_code import altarica_Expression
from python_code import altarica_LogicalAnd

def test_altarica_LogicalAnd___init__():
    assert altarica_LogicalAnd.__init__(altarica_LogicalAnd('', altarica_LogicalAnd=altarica_Expression(), altarica_LogicalAnd88=altarica_Expression()), '', altarica_LogicalAnd=altarica_Expression(), altarica_LogicalAnd88=altarica_Expression()) == None


from python_code import altarica_Expression
from python_code import altarica_LogicalOr

def test_altarica_LogicalOr___init__():
    assert altarica_LogicalOr.__init__(altarica_LogicalOr('', altarica_LogicalOr=altarica_Expression(), altarica_LogicalOr83=altarica_Expression()), '', altarica_LogicalOr=altarica_Expression(), altarica_LogicalOr83=altarica_Expression()) == None


from python_code import altarica_Expression
from python_code import altarica_Multiplication

def test_altarica_Multiplication___init__():
    assert altarica_Multiplication.__init__(altarica_Multiplication('', altarica_Multiplication103=altarica_Expression(), altarica_Multiplication=altarica_Expression()), '', altarica_Multiplication103=altarica_Expression(), altarica_Multiplication=altarica_Expression()) == None


from python_code import altarica_Domain
from python_code import altarica_Event
from python_code import altarica_NameRef
from python_code import altarica_NamedElement
from python_code import altarica_NamedType
from python_code import altarica_Variable

def test_altarica_NamedElement___init__():
    assert altarica_NamedElement.__init__(altarica_NamedElement('', altarica_NamedElement=altarica_NamedType(), altarica_NamedElement27=altarica_Domain(), altarica_NamedElement38=altarica_Variable(), altarica_NamedElement42=altarica_Event(), altarica_NamedElement12=altarica_NameRef()), '', altarica_NamedElement=altarica_NamedType(), altarica_NamedElement27=altarica_Domain(), altarica_NamedElement38=altarica_Variable(), altarica_NamedElement42=altarica_Event(), altarica_NamedElement12=altarica_NameRef()) == None

