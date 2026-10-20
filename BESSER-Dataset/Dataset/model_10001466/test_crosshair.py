from python_code import Guest

def test_Guest___init__():
    assert Guest.__init__(Guest(''), '') == None


from python_code import Meals

def test_Meals___init__():
    assert Meals.__init__(Meals('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '', '\x00\x00'), '', '', '') == None

