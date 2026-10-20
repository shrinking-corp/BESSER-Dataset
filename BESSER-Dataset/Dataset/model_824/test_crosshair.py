from python_code import simplefsm_FSM
from python_code import simplefsm_State
from python_code import simplefsm_Transition

def test_simplefsm_State___init__():
    assert simplefsm_State.__init__(simplefsm_State('', State=simplefsm_FSM(), simplefsm_State=simplefsm_FSM(), ownedState=simplefsm_FSM(), source=set(), target=set(), State7=simplefsm_Transition(), State9=simplefsm_Transition()), '', State=simplefsm_FSM(), simplefsm_State=simplefsm_FSM(), ownedState=simplefsm_FSM(), source=set(), target=set(), State7=simplefsm_Transition(), State9=simplefsm_Transition()) == None

