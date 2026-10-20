from python_code import Licor

def test_Licor___init__():
    assert Licor.__init__(Licor('\x00\x00', '', lineItems12=set()), '', '', lineItems12=set()) == None

