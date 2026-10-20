from python_code import Department

def test_Department___init__():
    assert Department.__init__(Department(0, '\x00', doctor3=set()), 0, '', doctor3=set()) == None

