from python_code import Portal

def test_Portal___init__():
    assert Portal.__init__(Portal('', '', '', users7=set()), '', '', '', users7=set()) == None


from python_code import PremiumCustomer

def test_PremiumCustomer___init__():
    assert PremiumCustomer.__init__(PremiumCustomer(''), '') == None


from python_code import Product

def test_Product___init__():
    assert Product.__init__(Product(0, '', '', 0.0, '', 0, orderDetails2=set()), 0, '', '', 0.0, '', 0, orderDetails2=set()) == None

