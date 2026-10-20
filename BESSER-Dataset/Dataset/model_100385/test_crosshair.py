from python_code import scxmlxt_AbstractTransitionEvent

def test_scxmlxt_AbstractTransitionEvent___init__():
    assert scxmlxt_AbstractTransitionEvent.__init__(scxmlxt_AbstractTransitionEvent()) == None

def test_scxmlxt_AbstractTransitionEvent_getSource():
    assert scxmlxt_AbstractTransitionEvent.getSource(scxmlxt_AbstractTransitionEvent()) == None

def test_scxmlxt_AbstractTransitionEvent_getTarget():
    assert scxmlxt_AbstractTransitionEvent.getTarget(scxmlxt_AbstractTransitionEvent()) == None


from python_code import scxmlxt_AbstractUriLiteral

def test_scxmlxt_AbstractUriLiteral___init__():
    assert scxmlxt_AbstractUriLiteral.__init__(scxmlxt_AbstractUriLiteral(''), '') == None


from python_code import scxmlxt_BooleanLiteral

def test_scxmlxt_BooleanLiteral___init__():
    assert scxmlxt_BooleanLiteral.__init__(scxmlxt_BooleanLiteral(True), False) == None


from python_code import scxmlxt_AbstractTransition
from python_code import scxmlxt_Condition

def test_scxmlxt_Condition___init__():
    assert scxmlxt_Condition.__init__(scxmlxt_Condition('', scxmlxt_Condition=scxmlxt_AbstractTransition()), '', scxmlxt_Condition=scxmlxt_AbstractTransition()) == None


from python_code import scxmlxt_DelayLiteral

def test_scxmlxt_DelayLiteral___init__():
    assert scxmlxt_DelayLiteral.__init__(scxmlxt_DelayLiteral(''), '') == None


from python_code import scxmlxt_EObjectUriLiteral

def test_scxmlxt_EObjectUriLiteral___init__():
    assert scxmlxt_EObjectUriLiteral.__init__(scxmlxt_EObjectUriLiteral(''), '') == None


from python_code import scxmlxt_FloatLiteral

def test_scxmlxt_FloatLiteral___init__():
    assert scxmlxt_FloatLiteral.__init__(scxmlxt_FloatLiteral(0.0), 0.0) == None


from python_code import scxmlxt_IntLiteral

def test_scxmlxt_IntLiteral___init__():
    assert scxmlxt_IntLiteral.__init__(scxmlxt_IntLiteral(0), 0) == None


from python_code import scxmlxt_ResourceImport
from python_code import scxmlxt_StateMachine

def test_scxmlxt_ResourceImport___init__():
    assert scxmlxt_ResourceImport.__init__(scxmlxt_ResourceImport('', scxmlxt_ResourceImport=scxmlxt_StateMachine()), '', scxmlxt_ResourceImport=scxmlxt_StateMachine()) == None


from python_code import scxmlxt_ResourceUriLiteral

def test_scxmlxt_ResourceUriLiteral___init__():
    assert scxmlxt_ResourceUriLiteral.__init__(scxmlxt_ResourceUriLiteral(''), '') == None


from python_code import scxmlxt_ScriptAction

def test_scxmlxt_ScriptAction___init__():
    assert scxmlxt_ScriptAction.__init__(scxmlxt_ScriptAction(''), '') == None


from python_code import scxmlxt_ScriptEvent

def test_scxmlxt_ScriptEvent___init__():
    assert scxmlxt_ScriptEvent.__init__(scxmlxt_ScriptEvent(''), '') == None


from python_code import scxmlxt_AbstractState
from python_code import scxmlxt_InitialTransition
from python_code import scxmlxt_State
from python_code import scxmlxt_StateMachine
from python_code import scxmlxt_Transition
from python_code import scxmlxt_TransitionEvent

def test_scxmlxt_State___init__():
    assert scxmlxt_State.__init__(scxmlxt_State('', scxmlxt_State=scxmlxt_StateMachine(), scxmlxt_State4=scxmlxt_InitialTransition(), scxmlxt_State8=scxmlxt_AbstractState(), scxmlxt_State21=scxmlxt_Transition(), scxmlxt_State26=scxmlxt_TransitionEvent(), scxmlxt_State23=scxmlxt_TransitionEvent()), '', scxmlxt_State=scxmlxt_StateMachine(), scxmlxt_State4=scxmlxt_InitialTransition(), scxmlxt_State8=scxmlxt_AbstractState(), scxmlxt_State21=scxmlxt_Transition(), scxmlxt_State26=scxmlxt_TransitionEvent(), scxmlxt_State23=scxmlxt_TransitionEvent()) == None


from python_code import scxmlxt_StringLiteral

def test_scxmlxt_StringLiteral___init__():
    assert scxmlxt_StringLiteral.__init__(scxmlxt_StringLiteral(''), '') == None


from python_code import scxmlxt_Expression
from python_code import scxmlxt_SymbolicAction

def test_scxmlxt_SymbolicAction___init__():
    assert scxmlxt_SymbolicAction.__init__(scxmlxt_SymbolicAction('', scxmlxt_SymbolicAction=scxmlxt_Expression()), '', scxmlxt_SymbolicAction=scxmlxt_Expression()) == None


from python_code import scxmlxt_SymbolicEvent

def test_scxmlxt_SymbolicEvent___init__():
    assert scxmlxt_SymbolicEvent.__init__(scxmlxt_SymbolicEvent(''), '') == None


from python_code import scxmlxt_EClassifier
from python_code import scxmlxt_Typed

def test_scxmlxt_Typed___init__():
    assert scxmlxt_Typed.__init__(scxmlxt_Typed(True, scxmlxt_Typed=scxmlxt_EClassifier()), False, scxmlxt_Typed=scxmlxt_EClassifier()) == None


from python_code import scxmlxt_UriLiteral

def test_scxmlxt_UriLiteral___init__():
    assert scxmlxt_UriLiteral.__init__(scxmlxt_UriLiteral(''), '') == None


from python_code import scxmlxt_AbstractState
from python_code import scxmlxt_AssignmentAction
from python_code import scxmlxt_Expression
from python_code import scxmlxt_VarDef
from python_code import scxmlxt_VarRef

def test_scxmlxt_VarDef___init__():
    assert scxmlxt_VarDef.__init__(scxmlxt_VarDef('', scxmlxt_VarDef=scxmlxt_AbstractState(), scxmlxt_VarDef35=scxmlxt_Expression(), scxmlxt_VarDef38=scxmlxt_AssignmentAction(), scxmlxt_VarDef43=scxmlxt_VarRef()), '', scxmlxt_VarDef=scxmlxt_AbstractState(), scxmlxt_VarDef35=scxmlxt_Expression(), scxmlxt_VarDef38=scxmlxt_AssignmentAction(), scxmlxt_VarDef43=scxmlxt_VarRef()) == None

