from python_code import fsm_Machine
from python_code import fsm_Model

def test_fsm_Model___init__():
    assert fsm_Model.__init__(fsm_Model('', fsm_Model=set(), fsm_Model2=set(), fsm_Model4=fsm_Machine()), '', fsm_Model=set(), fsm_Model2=set(), fsm_Model4=fsm_Machine()) == None

