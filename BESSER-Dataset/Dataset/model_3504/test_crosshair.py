from python_code import ale_Apply
from python_code import ale_Expression
from python_code import ale_typeLiteral

def test_ale_Apply___init__():
    assert ale_Apply.__init__(ale_Apply('\x00\x00', '', ale_Apply=ale_Expression(), ale_Apply103=ale_typeLiteral(), ale_Apply106=ale_Expression(), ale_Apply109=set()), '', '', ale_Apply=ale_Expression(), ale_Apply103=ale_typeLiteral(), ale_Apply106=ale_Expression(), ale_Apply109=set()) == None


from python_code import ale_Call
from python_code import ale_Expression

def test_ale_Call___init__():
    assert ale_Call.__init__(ale_Call('', ale_Call96=set(), ale_Call=ale_Expression()), '', ale_Call96=set(), ale_Call=ale_Expression()) == None


from python_code import ale_ClassifierType

def test_ale_ClassifierType___init__():
    assert ale_ClassifierType.__init__(ale_ClassifierType('', '\x00'), '\x00\x00', '') == None


from python_code import ale_Comp
from python_code import ale_Expression

def test_ale_Comp___init__():
    assert ale_Comp.__init__(ale_Comp('', ale_Comp=ale_Expression(), ale_Comp124=ale_Expression()), '', ale_Comp=ale_Expression(), ale_Comp124=ale_Expression()) == None


from python_code import ale_ExtendedClass

def test_ale_ExtendedClass___init__():
    assert ale_ExtendedClass.__init__(ale_ExtendedClass(''), '') == None


from python_code import ale_Expression
from python_code import ale_Feature

def test_ale_Feature___init__():
    assert ale_Feature.__init__(ale_Feature('', ale_Feature=ale_Expression()), '', ale_Feature=ale_Expression()) == None


from python_code import ale_Int

def test_ale_Int___init__():
    assert ale_Int.__init__(ale_Int(0), 0) == None


from python_code import ale_Real

def test_ale_Real___init__():
    assert ale_Real.__init__(ale_Real(''), '') == None


from python_code import ale_String

def test_ale_String___init__():
    assert ale_String.__init__(ale_String(''), '') == None


from python_code import ale_VarRef

def test_ale_VarRef___init__():
    assert ale_VarRef.__init__(ale_VarRef(''), '') == None

