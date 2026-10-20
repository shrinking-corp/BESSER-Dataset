from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product(0, '', '\x00\x00'), 0, '', '') == None

