from python_code import Bill
from python_code import Discount

def test_Discount___init__():
    assert Discount.__init__(Discount(0, bill9=Bill()), 0, bill9=Bill()) == None


from python_code import Drinks
from python_code import Order

def test_Drinks___init__():
    assert Drinks.__init__(Drinks('', '', '', '', '', Order_Drinks_17=Order()), '', '', '', '', '', Order_Drinks_17=Order()) == None


from python_code import Menu
from python_code import Order

def test_Menu___init__():
    assert Menu.__init__(Menu('\x00\x00', '', '', '', Order_Menu_15=Order()), '', '', '', '', Order_Menu_15=Order()) == None


from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment('', bill1=set()), '', bill1=set()) == None

