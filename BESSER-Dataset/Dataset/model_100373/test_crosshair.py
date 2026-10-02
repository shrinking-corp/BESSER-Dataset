from python_code import MDAIntermediateStateMachine_Content

def test_MDAIntermediateStateMachine_Content___init__():
    assert MDAIntermediateStateMachine_Content.__init__(MDAIntermediateStateMachine_Content('\x00', MDAIntermediateStateMachine_Content=set(), MDAIntermediateStateMachine_Content2=set(), MDAIntermediateStateMachine_Content4=set(), MDAIntermediateStateMachine_Content6=set(), MDAIntermediateStateMachine_Content8=set()), '', MDAIntermediateStateMachine_Content=set(), MDAIntermediateStateMachine_Content2=set(), MDAIntermediateStateMachine_Content4=set(), MDAIntermediateStateMachine_Content6=set(), MDAIntermediateStateMachine_Content8=set()) == None

from python_code import MDAIntermediateStateMachine_Message
from python_code import MDAIntermediateStateMachine_Transition
from python_code import MDAIntermediateStateMachine_Value

def test_MDAIntermediateStateMachine_Value___init__():
    assert MDAIntermediateStateMachine_Value.__init__(MDAIntermediateStateMachine_Value('', MDAIntermediateStateMachine_Value=MDAIntermediateStateMachine_Transition(), MDAIntermediateStateMachine_Value41=MDAIntermediateStateMachine_Message()), '', MDAIntermediateStateMachine_Value=MDAIntermediateStateMachine_Transition(), MDAIntermediateStateMachine_Value41=MDAIntermediateStateMachine_Message()) == None
