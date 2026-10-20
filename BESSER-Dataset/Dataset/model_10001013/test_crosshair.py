from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', 0, Customer_Order_00=set()), '', 0, Customer_Order_00=set()) == None


from python_code import Customer1

def test_Customer1___init__():
    assert Customer1.__init__(Customer1('', 0, '', 0, order26=set()), '', 0, '', 0, order26=set()) == None


from python_code import SpecialOrder

def test_SpecialOrder___init__():
    assert SpecialOrder.__init__(SpecialOrder(0, 0), 0, 0) == None

