from python_code import z2fsm_Region

def test_z2fsm_Region___init__():
    assert z2fsm_Region.__init__(z2fsm_Region('\x00', z2fsm_Region=set()), '', z2fsm_Region=set()) == None

