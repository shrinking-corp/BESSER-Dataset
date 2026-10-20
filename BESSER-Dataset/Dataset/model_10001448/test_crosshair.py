from python_code import Event

def test_Event___init__():
    assert Event.__init__(Event('\x00\x00', '', lineItems12=set()), '', '', lineItems12=set()) == None

