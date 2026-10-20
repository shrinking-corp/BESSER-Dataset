from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product('\x00\x00', '', item12=set()), '', '', item12=set()) == None

