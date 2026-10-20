from python_code import reqLanguage_Actor

def test_reqLanguage_Actor___init__():
    assert reqLanguage_Actor.__init__(reqLanguage_Actor('', '\x00'), '\x00\x00', '') == None


from python_code import reqLanguage_Attribute
from python_code import reqLanguage_MainAttributes

def test_reqLanguage_Attribute___init__():
    assert reqLanguage_Attribute.__init__(reqLanguage_Attribute('', '', '\x00\x00', reqLanguage_Attribute=reqLanguage_MainAttributes()), '', '', '', reqLanguage_Attribute=reqLanguage_MainAttributes()) == None


from python_code import reqLanguage_Function
from python_code import reqLanguage_MainFunctions

def test_reqLanguage_Function___init__():
    assert reqLanguage_Function.__init__(reqLanguage_Function('', '', '\x00\x00', reqLanguage_Function=reqLanguage_MainFunctions()), '', '', '', reqLanguage_Function=reqLanguage_MainFunctions()) == None


from python_code import reqLanguage_EObject
from python_code import reqLanguage_PrefixEvent

def test_reqLanguage_PrefixEvent___init__():
    assert reqLanguage_PrefixEvent.__init__(reqLanguage_PrefixEvent('', reqLanguage_PrefixEvent=reqLanguage_EObject()), '', reqLanguage_PrefixEvent=reqLanguage_EObject()) == None


from python_code import reqLanguage_EObject
from python_code import reqLanguage_Prefix
from python_code import reqLanguage_PrefixRightOperand

def test_reqLanguage_PrefixRightOperand___init__():
    assert reqLanguage_PrefixRightOperand.__init__(reqLanguage_PrefixRightOperand('', reqLanguage_PrefixRightOperand=reqLanguage_Prefix(), reqLanguage_PrefixRightOperand13=reqLanguage_EObject()), '', reqLanguage_PrefixRightOperand=reqLanguage_Prefix(), reqLanguage_PrefixRightOperand13=reqLanguage_EObject()) == None


from python_code import reqLanguage_EObject
from python_code import reqLanguage_PrefixState

def test_reqLanguage_PrefixState___init__():
    assert reqLanguage_PrefixState.__init__(reqLanguage_PrefixState('', reqLanguage_PrefixState=reqLanguage_EObject()), '', reqLanguage_PrefixState=reqLanguage_EObject()) == None


from python_code import reqLanguage_ReqID
from python_code import reqLanguage_Requirement

def test_reqLanguage_ReqID___init__():
    assert reqLanguage_ReqID.__init__(reqLanguage_ReqID('', '\x00', reqLanguage_ReqID=reqLanguage_Requirement()), '\x00\x00', '', reqLanguage_ReqID=reqLanguage_Requirement()) == None


from python_code import reqLanguage_State
from python_code import reqLanguage_StateEvent

def test_reqLanguage_State___init__():
    assert reqLanguage_State.__init__(reqLanguage_State('', '\x00', reqLanguage_State=reqLanguage_StateEvent()), '\x00\x00', '', reqLanguage_State=reqLanguage_StateEvent()) == None


from python_code import reqLanguage_MainAttributes
from python_code import reqLanguage_MainComposition
from python_code import reqLanguage_MainFunctions
from python_code import reqLanguage_MainStateTransition
from python_code import reqLanguage_StateEvent
from python_code import reqLanguage_System

def test_reqLanguage_System___init__():
    assert reqLanguage_System.__init__(reqLanguage_System('', '\x00', reqLanguage_System=reqLanguage_StateEvent(), reqLanguage_System49=reqLanguage_MainComposition(), reqLanguage_System52=reqLanguage_MainComposition(), reqLanguage_System54=reqLanguage_MainStateTransition(), reqLanguage_System62=reqLanguage_MainAttributes(), reqLanguage_System66=reqLanguage_MainFunctions()), '\x00\x00', '', reqLanguage_System=reqLanguage_StateEvent(), reqLanguage_System49=reqLanguage_MainComposition(), reqLanguage_System52=reqLanguage_MainComposition(), reqLanguage_System54=reqLanguage_MainStateTransition(), reqLanguage_System62=reqLanguage_MainAttributes(), reqLanguage_System66=reqLanguage_MainFunctions()) == None


from python_code import reqLanguage_User

def test_reqLanguage_User___init__():
    assert reqLanguage_User.__init__(reqLanguage_User('', '\x00'), '\x00\x00', '') == None

