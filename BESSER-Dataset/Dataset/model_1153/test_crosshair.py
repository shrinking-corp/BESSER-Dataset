from python_code import gemoc_FSM

def test_gemoc_FSM___init__():
    assert gemoc_FSM.__init__(gemoc_FSM('', gemoc_FSM=set(), gemoc_FSM2=set()), '', gemoc_FSM=set(), gemoc_FSM2=set()) == None

def test_gemoc_FSM_print():
    assert gemoc_FSM.print(gemoc_FSM('\x00', gemoc_FSM=set(), gemoc_FSM2=set())) == None

