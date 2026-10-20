from python_code import z3fsm_Region

def test_z3fsm_Region___init__():
    assert z3fsm_Region.__init__(z3fsm_Region('\x00', z3fsm_Region=set()), '', z3fsm_Region=set()) == None

