from python_code import fsml_FSM

def test_fsml_FSM___init__():
    assert fsml_FSM.__init__(fsml_FSM(fsml_FSM=set()), fsml_FSM=set()) == None

def test_fsml_FSM_hasExactOneInitialState():
    assert fsml_FSM.hasExactOneInitialState(fsml_FSM(fsml_FSM=set()), 0, '\x00\x00') == None

