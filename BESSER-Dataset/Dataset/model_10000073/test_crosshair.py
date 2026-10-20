from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('', '', lineItems12=set()), '', '', lineItems12=set()) == None

