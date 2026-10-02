from python_code import Account

def test_Account___init__():
    assert Account.__init__(Account('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

from python_code import Account1

def test_Account1___init__():
    assert Account1.__init__(Account1('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

from python_code import Account_for_employee

def test_Account_for_employee___init__():
    assert Account_for_employee.__init__(Account_for_employee('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

from python_code import Catering

def test_Catering___init__():
    assert Catering.__init__(Catering('', '\x00'), '\x00\x00', '') == None

from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', 0, '', '', '', '', 0), '', 0, '', '', '', '', 0) == None

from python_code import Customer_Balance

def test_Customer_Balance___init__():
    assert Customer_Balance.__init__(Customer_Balance(0, '', '', '', ''), 0, '', '', '', '') == None

from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee('', '', '', 0, '\x00', storage0=set(), plan2=set()), '', '', '', 0, '', storage0=set(), plan2=set()) == None

from python_code import Employee1

def test_Employee1___init__():
    assert Employee1.__init__(Employee1('', '', '', '', ''), '', '', '', '', '') == None

from python_code import Menu

def test_Menu___init__():
    assert Menu.__init__(Menu('\x00\x00', '', '', ''), '', '', '', '') == None

from python_code import Order

def test_Order___init__():
    assert Order.__init__(Order(0, 0, '', '', ''), 0, 0, '', '', '') == None

from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment(0, '', 0, 0, '', ''), 0, '', 0, 0, '\x00', '') == None

from python_code import Plan

def test_Plan___init__():
    assert Plan.__init__(Plan('', '', '', employee3=set()), '', '', '', employee3=set()) == None

from python_code import PrintRecipts

def test_PrintRecipts___init__():
    assert PrintRecipts.__init__(PrintRecipts('', '', '', 0, '', '', 0), '', '\x00', '', 0, '', '', 0) == None

from python_code import Shopping_cart

def test_Shopping_cart___init__():
    assert Shopping_cart.__init__(Shopping_cart('', 0, 0, '', ''), '', 0, 0, '', '') == None

from python_code import Storage

def test_Storage___init__():
    assert Storage.__init__(Storage(0, '\x00', employee1=set()), 0, '', employee1=set()) == None

from python_code import account_type

def test_account_type___init__():
    assert account_type.__init__(account_type('', '', '', '', ''), '', '', '', '', '') == None

from python_code import chef2
from python_code import dayplan

def test_dayplan___init__():
    assert dayplan.__init__(dayplan('', '', '', '', '', '', '', '', weekly_planning_of_dishes__by_waiter134=set(), chef136=chef2(), chef151=chef2()), '', '', '', '', '', '', '', '', weekly_planning_of_dishes__by_waiter134=set(), chef136=chef2(), chef151=chef2()) == None

from python_code import payment
from python_code import shopping_cart

def test_payment___init__():
    assert payment.__init__(payment('', '', '', shopping_cart133=set(), shopping_cart171=shopping_cart()), '', '', '', shopping_cart133=set(), shopping_cart171=shopping_cart()) == None

from python_code import solid1

def test_solid1___init__():
    assert solid1.__init__(solid1('\x00\x00', '', 0, ''), '', '', 0, '') == None
