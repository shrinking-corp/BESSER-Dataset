from python_code import Entrega_producto

def test_Entrega_producto___init__():
    assert Entrega_producto.__init__(Entrega_producto('\x00\x00', '', lineItems12=set()), '', '', lineItems12=set()) == None

