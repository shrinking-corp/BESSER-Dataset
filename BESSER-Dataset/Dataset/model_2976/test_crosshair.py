from python_code import CompleteDSLPckg_ArithmeticExpression
from python_code import CompleteDSLPckg_Expression

def test_CompleteDSLPckg_ArithmeticExpression___init__():
    assert CompleteDSLPckg_ArithmeticExpression.__init__(CompleteDSLPckg_ArithmeticExpression('', CompleteDSLPckg_ArithmeticExpression=CompleteDSLPckg_Expression(), CompleteDSLPckg_ArithmeticExpression2=CompleteDSLPckg_Expression()), '', CompleteDSLPckg_ArithmeticExpression=CompleteDSLPckg_Expression(), CompleteDSLPckg_ArithmeticExpression2=CompleteDSLPckg_Expression()) == None


from python_code import CompleteDSLPckg_BoolLit

def test_CompleteDSLPckg_BoolLit___init__():
    assert CompleteDSLPckg_BoolLit.__init__(CompleteDSLPckg_BoolLit(True), False) == None


from python_code import CompleteDSLPckg_ConsoleOutput

def test_CompleteDSLPckg_ConsoleOutput___init__():
    assert CompleteDSLPckg_ConsoleOutput.__init__(CompleteDSLPckg_ConsoleOutput(''), '') == None


from python_code import CompleteDSLPckg_IntegerLit

def test_CompleteDSLPckg_IntegerLit___init__():
    assert CompleteDSLPckg_IntegerLit.__init__(CompleteDSLPckg_IntegerLit(0), 0) == None


from python_code import CompleteDSLPckg_NamedElement

def test_CompleteDSLPckg_NamedElement___init__():
    assert CompleteDSLPckg_NamedElement.__init__(CompleteDSLPckg_NamedElement(''), '') == None


from python_code import CompleteDSLPckg_Expression
from python_code import CompleteDSLPckg_RelationalExpression

def test_CompleteDSLPckg_RelationalExpression___init__():
    assert CompleteDSLPckg_RelationalExpression.__init__(CompleteDSLPckg_RelationalExpression('', CompleteDSLPckg_RelationalExpression=CompleteDSLPckg_Expression(), CompleteDSLPckg_RelationalExpression7=CompleteDSLPckg_Expression()), '', CompleteDSLPckg_RelationalExpression=CompleteDSLPckg_Expression(), CompleteDSLPckg_RelationalExpression7=CompleteDSLPckg_Expression()) == None


from python_code import CompleteDSLPckg_StringLit

def test_CompleteDSLPckg_StringLit___init__():
    assert CompleteDSLPckg_StringLit.__init__(CompleteDSLPckg_StringLit(''), '') == None


from python_code import CompleteDSLPckg_AndTrigger
from python_code import CompleteDSLPckg_NotTrigger
from python_code import CompleteDSLPckg_OrTrigger
from python_code import CompleteDSLPckg_Transition
from python_code import CompleteDSLPckg_Trigger

def test_CompleteDSLPckg_Trigger___init__():
    assert CompleteDSLPckg_Trigger.__init__(CompleteDSLPckg_Trigger('', CompleteDSLPckg_Trigger=CompleteDSLPckg_Transition(), CompleteDSLPckg_Trigger61=CompleteDSLPckg_NotTrigger(), CompleteDSLPckg_Trigger63=CompleteDSLPckg_AndTrigger(), CompleteDSLPckg_Trigger66=CompleteDSLPckg_AndTrigger(), CompleteDSLPckg_Trigger68=CompleteDSLPckg_OrTrigger(), CompleteDSLPckg_Trigger71=CompleteDSLPckg_OrTrigger()), '', CompleteDSLPckg_Trigger=CompleteDSLPckg_Transition(), CompleteDSLPckg_Trigger61=CompleteDSLPckg_NotTrigger(), CompleteDSLPckg_Trigger63=CompleteDSLPckg_AndTrigger(), CompleteDSLPckg_Trigger66=CompleteDSLPckg_AndTrigger(), CompleteDSLPckg_Trigger68=CompleteDSLPckg_OrTrigger(), CompleteDSLPckg_Trigger71=CompleteDSLPckg_OrTrigger()) == None


from python_code import CompleteDSLPckg_Assignation
from python_code import CompleteDSLPckg_Expression
from python_code import CompleteDSLPckg_VarDecl

def test_CompleteDSLPckg_VarDecl___init__():
    assert CompleteDSLPckg_VarDecl.__init__(CompleteDSLPckg_VarDecl('', CompleteDSLPckg_VarDecl=CompleteDSLPckg_Expression(), CompleteDSLPckg_VarDecl23=CompleteDSLPckg_Assignation()), '', CompleteDSLPckg_VarDecl=CompleteDSLPckg_Expression(), CompleteDSLPckg_VarDecl23=CompleteDSLPckg_Assignation()) == None


from python_code import CompleteDSLPckg_VarRef

def test_CompleteDSLPckg_VarRef___init__():
    assert CompleteDSLPckg_VarRef.__init__(CompleteDSLPckg_VarRef(''), '') == None


from python_code import CompleteDSLPckg_Wait

def test_CompleteDSLPckg_Wait___init__():
    assert CompleteDSLPckg_Wait.__init__(CompleteDSLPckg_Wait(''), '') == None

