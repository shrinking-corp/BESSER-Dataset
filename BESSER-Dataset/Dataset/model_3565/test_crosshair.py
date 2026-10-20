from python_code import go_Atrib
from python_code import go_Atrib_Aux
from python_code import go_DecVar
from python_code import go_EObject

def test_go_Atrib___init__():
    assert go_Atrib.__init__(go_Atrib('', '', '\x00\x00', go_Atrib15=go_Atrib_Aux(), go_Atrib18=go_EObject(), go_Atrib=go_DecVar()), '', '', '', go_Atrib15=go_Atrib_Aux(), go_Atrib18=go_EObject(), go_Atrib=go_DecVar()) == None


from python_code import go_AtribVar
from python_code import go_DecVar

def test_go_AtribVar___init__():
    assert go_AtribVar.__init__(go_AtribVar('\x00\x00', '', go_AtribVar=go_DecVar(), go_AtribVar9=set()), '', '', go_AtribVar=go_DecVar(), go_AtribVar9=set()) == None


from python_code import go_Bool
from python_code import go_Literal

def test_go_Bool___init__():
    assert go_Bool.__init__(go_Bool('', go_Bool=go_Literal()), '', go_Bool=go_Literal()) == None


from python_code import go_DataType

def test_go_DataType___init__():
    assert go_DataType.__init__(go_DataType(''), '') == None


from python_code import go_DecVars

def test_go_DecVars___init__():
    assert go_DecVars.__init__(go_DecVars('', go_DecVars=set()), '', go_DecVars=set()) == None


from python_code import go_DecVar
from python_code import go_Decl

def test_go_Decl___init__():
    assert go_Decl.__init__(go_Decl('', '\x00', go_Decl=go_DecVar()), '\x00\x00', '', go_Decl=go_DecVar()) == None


from python_code import go_Double
from python_code import go_Numbers

def test_go_Double___init__():
    assert go_Double.__init__(go_Double(0, go_Double=go_Numbers()), 0, go_Double=go_Numbers()) == None


from python_code import go_Intg
from python_code import go_Numbers

def test_go_Intg___init__():
    assert go_Intg.__init__(go_Intg(0, go_Intg=go_Numbers()), 0, go_Intg=go_Numbers()) == None


from python_code import go_MultDecVars
from python_code import go_TypeValue

def test_go_MultDecVars___init__():
    assert go_MultDecVars.__init__(go_MultDecVars('', '\x00', go_MultDecVars=go_TypeValue()), '\x00\x00', '', go_MultDecVars=go_TypeValue()) == None


from python_code import go_Atrib_Aux
from python_code import go_DecVar
from python_code import go_EObject
from python_code import go_ReAtrib

def test_go_ReAtrib___init__():
    assert go_ReAtrib.__init__(go_ReAtrib('', go_ReAtrib=go_DecVar(), go_ReAtrib20=go_Atrib_Aux(), go_ReAtrib23=go_EObject()), '', go_ReAtrib=go_DecVar(), go_ReAtrib20=go_Atrib_Aux(), go_ReAtrib23=go_EObject()) == None


from python_code import go_Str

def test_go_Str___init__():
    assert go_Str.__init__(go_Str(''), '') == None


from python_code import go_Cases
from python_code import go_Greeting
from python_code import go_Variable

def test_go_Variable___init__():
    assert go_Variable.__init__(go_Variable('', go_Variable=go_Cases(), go_Variable12=go_Greeting()), '', go_Variable=go_Cases(), go_Variable12=go_Greeting()) == None

