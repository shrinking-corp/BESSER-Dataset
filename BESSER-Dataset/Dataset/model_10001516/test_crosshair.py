from python_code import Bank

def test_Bank___init__():
    assert Bank.__init__(Bank(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Cash_on_delievery

def test_Cash_on_delievery___init__():
    assert Cash_on_delievery.__init__(Cash_on_delievery('\x00\x00', '', 0, ''), '', '', 0, '') == None


from python_code import Category

def test_Category___init__():
    assert Category.__init__(Category(0, '\x00', Food_Items_Category_15=set()), 0, '', Food_Items_Category_15=set()) == None


from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment('\x00\x00', 0, System_order_Payment_11=set()), '', 0, System_order_Payment_11=set()) == None


from python_code import Customer
from python_code import System_order

def test_System_order___init__():
    assert System_order.__init__(System_order(0, '', 0, 0, 0, 0, 0, '', System_order_Payment_00=set(), System_order_Customer_02=Customer()), 0, '', 0, 0, 0, 0, 0, '', System_order_Payment_00=set(), System_order_Customer_02=Customer()) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User(0, '\x00', '', ''), 0, '', '', '') == None

