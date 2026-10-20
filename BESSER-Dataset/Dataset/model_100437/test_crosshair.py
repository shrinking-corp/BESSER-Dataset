from python_code import statemachine_Call
from python_code import statemachine_CallAction

def test_statemachine_Call___init__():
    assert statemachine_Call.__init__(statemachine_Call('', statemachine_Call=statemachine_CallAction()), '', statemachine_Call=statemachine_CallAction()) == None


from python_code import statemachine_ConstantValue

def test_statemachine_ConstantValue___init__():
    assert statemachine_ConstantValue.__init__(statemachine_ConstantValue(''), '') == None


from python_code import statemachine_GAbstractAction
from python_code import statemachine_GAbstractState

def test_statemachine_GAbstractAction___init__():
    assert statemachine_GAbstractAction.__init__(statemachine_GAbstractAction('', statemachine_GAbstractAction=statemachine_GAbstractState()), '', statemachine_GAbstractAction=statemachine_GAbstractState()) == None


from python_code import statemachine_GStatemachine

def test_statemachine_GStatemachine___init__():
    assert statemachine_GStatemachine.__init__(statemachine_GStatemachine('', statemachine_GStatemachine=set()), '', statemachine_GStatemachine=set()) == None


from python_code import statemachine_Named

def test_statemachine_Named___init__():
    assert statemachine_Named.__init__(statemachine_Named('', '\x00'), '\x00\x00', '') == None


from python_code import statemachine_GAbstractState
from python_code import statemachine_GCompositeState
from python_code import statemachine_Transition
from python_code import statemachine_Value

def test_statemachine_Transition___init__():
    assert statemachine_Transition.__init__(statemachine_Transition(False, statemachine_Transition9=statemachine_Value(), statemachine_Transition12=set(), statemachine_Transition=statemachine_GAbstractState(), statemachine_Transition4=statemachine_GAbstractState(), statemachine_Transition7=statemachine_Value(), statemachine_Transition18=statemachine_GCompositeState()), False, statemachine_Transition9=statemachine_Value(), statemachine_Transition12=set(), statemachine_Transition=statemachine_GAbstractState(), statemachine_Transition4=statemachine_GAbstractState(), statemachine_Transition7=statemachine_Value(), statemachine_Transition18=statemachine_GCompositeState()) == None

