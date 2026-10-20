from python_code import statemachines_Fork

def test_statemachines_Fork___init__():
    assert statemachines_Fork.__init__(statemachines_Fork()) == None

def test_statemachines_Fork_isJoin():
    assert statemachines_Fork.isJoin(statemachines_Fork()) == None

def test_statemachines_Fork_isFork():
    assert statemachines_Fork.isFork(statemachines_Fork()) == None

