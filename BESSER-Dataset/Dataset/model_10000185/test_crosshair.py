from python_code import Delivery

def test_Delivery___init__():
    assert Delivery.__init__(Delivery('', '', '\x00\x00'), '', '', '') == None


from python_code import Discription

def test_Discription___init__():
    assert Discription.__init__(Discription('', '\x00'), '\x00\x00', '') == None


from python_code import Order

def test_Order___init__():
    assert Order.__init__(Order(0, '\x00', 0, 0), 0, '', 0, 0) == None


from python_code import Payment

def test_Payment___init__():
    assert Payment.__init__(Payment(0, '\x00'), 0, '\x00') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '', 0, '', 0), '', '', 0, '', 0) == None

