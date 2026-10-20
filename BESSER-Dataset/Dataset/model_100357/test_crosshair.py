from python_code import FSM_MgaObject

def test_FSM_MgaObject___init__():
    assert FSM_MgaObject.__init__(FSM_MgaObject('', '\x00'), '\x00\x00', '') == None


from python_code import FSM_RootFolder

def test_FSM_RootFolder___init__():
    assert FSM_RootFolder.__init__(FSM_RootFolder('', FSM_RootFolder=set(), rootFolder=set()), '', FSM_RootFolder=set(), rootFolder=set()) == None

