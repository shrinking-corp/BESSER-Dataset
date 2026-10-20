from python_code import FSM_MgaObject

def test_FSM_MgaObject___init__():
    assert FSM_MgaObject.__init__(FSM_MgaObject('', '\x00'), '\x00\x00', '') == None

