from python_code import sAAP_StateMachine

def test_sAAP_StateMachine___init__():
    assert sAAP_StateMachine.__init__(sAAP_StateMachine('', sAAP_StateMachine=set(), sAAP_StateMachine5=set()), '', sAAP_StateMachine=set(), sAAP_StateMachine5=set()) == None

def test_sAAP_StateMachine_execute():
    assert sAAP_StateMachine.execute(sAAP_StateMachine('\x00', sAAP_StateMachine=set(), sAAP_StateMachine5=set())) == None

