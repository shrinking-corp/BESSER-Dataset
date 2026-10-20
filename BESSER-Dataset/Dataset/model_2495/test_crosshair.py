from python_code import fsm_State

def test_fsm_State___init__():
    assert fsm_State.__init__(fsm_State('', 0, True, '', '', 0.0, 0.0), '', 0, False, '', '', 0.0, 0.0) == None

