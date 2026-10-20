from python_code import ASM_AccessUpdateFunction

def test_ASM_AccessUpdateFunction___init__():
    assert ASM_AccessUpdateFunction.__init__(ASM_AccessUpdateFunction('', ASM_AccessUpdateFunction=set()), '', ASM_AccessUpdateFunction=set()) == None


from python_code import ASM_Argument
from python_code import ASM_ChooseRule
from python_code import ASM_DoForallRule
from python_code import ASM_Extension

def test_ASM_Argument___init__():
    assert ASM_Argument.__init__(ASM_Argument('', VariableDecl88=ASM_Extension(), VariableDecl=ASM_ChooseRule(), VariableDecl52=ASM_DoForallRule()), '', VariableDecl88=ASM_Extension(), VariableDecl=ASM_ChooseRule(), VariableDecl52=ASM_DoForallRule()) == None


from python_code import ASM_Asm
from python_code import Body
from python_code import MetaInformation
from python_code import Signature

def test_ASM_Asm___init__():
    assert ASM_Asm.__init__(ASM_Asm('', ASM_Asm=Signature(), ASM_Asm3=MetaInformation(), ASM_Asm5=Body()), '', ASM_Asm=Signature(), ASM_Asm3=MetaInformation(), ASM_Asm5=Body()) == None


from python_code import ASM_BooleanConstant

def test_ASM_BooleanConstant___init__():
    assert ASM_BooleanConstant.__init__(ASM_BooleanConstant(''), '') == None


from python_code import ASM_ElementDecl

def test_ASM_ElementDecl___init__():
    assert ASM_ElementDecl.__init__(ASM_ElementDecl(''), '') == None


from python_code import ASM_IntegerConstant

def test_ASM_IntegerConstant___init__():
    assert ASM_IntegerConstant.__init__(ASM_IntegerConstant(''), '') == None


from python_code import ASM_LocatedElement

def test_ASM_LocatedElement___init__():
    assert ASM_LocatedElement.__init__(ASM_LocatedElement(''), '') == None


from python_code import ASM_MetaInformation

def test_ASM_MetaInformation___init__():
    assert ASM_MetaInformation.__init__(ASM_MetaInformation('', ASM_MetaInformation=set(), ASM_MetaInformation15=set()), '', ASM_MetaInformation=set(), ASM_MetaInformation15=set()) == None


from python_code import ASM_Parameter

def test_ASM_Parameter___init__():
    assert ASM_Parameter.__init__(ASM_Parameter('', '\x00'), '\x00\x00', '') == None


from python_code import ASM_Rule

def test_ASM_Rule___init__():
    assert ASM_Rule.__init__(ASM_Rule(''), '') == None


from python_code import ASM_Signature

def test_ASM_Signature___init__():
    assert ASM_Signature.__init__(ASM_Signature('\x00\x00', '', ASM_Signature=set()), '', '', ASM_Signature=set()) == None


from python_code import ASM_StringConstant

def test_ASM_StringConstant___init__():
    assert ASM_StringConstant.__init__(ASM_StringConstant(''), '') == None


from python_code import ASM_Body
from python_code import ASM_Universe

def test_ASM_Universe___init__():
    assert ASM_Universe.__init__(ASM_Universe('\x00\x00', '', ASM_Universe=set(), Declaration=ASM_Body()), '', '', ASM_Universe=set(), Declaration=ASM_Body()) == None

