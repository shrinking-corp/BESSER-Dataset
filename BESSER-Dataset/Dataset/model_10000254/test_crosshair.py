from python_code import Event

def test_Event___init__():
    assert Event.__init__(Event(0.0, '\x00\x00'), 0.0, '') == None

