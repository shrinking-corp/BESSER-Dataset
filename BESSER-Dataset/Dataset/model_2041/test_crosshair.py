from python_code import tp1_StateMachine

def test_tp1_StateMachine___init__():
    assert tp1_StateMachine.__init__(tp1_StateMachine('', tp1_StateMachine=set(), tp1_StateMachine2=set()), '', tp1_StateMachine=set(), tp1_StateMachine2=set()) == None

def test_tp1_StateMachine_execute():
    assert tp1_StateMachine.execute(tp1_StateMachine('\x00', tp1_StateMachine=set(), tp1_StateMachine2=set())) == None

