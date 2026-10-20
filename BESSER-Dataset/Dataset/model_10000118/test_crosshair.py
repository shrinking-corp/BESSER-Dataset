from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', '', 0.0, lineItems12=set()), '', '', 0.0, lineItems12=set()) == None

