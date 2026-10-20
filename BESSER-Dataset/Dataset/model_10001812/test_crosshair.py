from python_code import CreditCardPayment

def test_CreditCardPayment___init__():
    assert CreditCardPayment.__init__(CreditCardPayment('', 0), '', 0) == None


from python_code import PayLater1

def test_PayLater1___init__():
    assert PayLater1.__init__(PayLater1(''), '') == None


from python_code import SMS

def test_SMS___init__():
    assert SMS.__init__(SMS(0), 0) == None


from python_code import Vendor

def test_Vendor___init__():
    assert Vendor.__init__(Vendor('', '\x00'), '\x00\x00', '') == None


from python_code import email

def test_email___init__():
    assert email.__init__(email(''), '') == None

