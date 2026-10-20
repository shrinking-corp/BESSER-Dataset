from python_code import Presales_team

def test_Presales_team___init__():
    assert Presales_team.__init__(Presales_team('', '\x00'), '\x00\x00', '') == None


from python_code import Property1

def test_Property1___init__():
    assert Property1.__init__(Property1('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Reg_User

def test_Reg_User___init__():
    assert Reg_User.__init__(Reg_User('', '', '\x00\x00'), '', '', '') == None


from python_code import Rent

def test_Rent___init__():
    assert Rent.__init__(Rent(''), '') == None


from python_code import ResidentialApartment

def test_ResidentialApartment___init__():
    assert ResidentialApartment.__init__(ResidentialApartment('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Seller

def test_Seller___init__():
    assert Seller.__init__(Seller('\x00\x00', '', property1=set()), '', '', property1=set()) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '\x00'), '\x00\x00', '') == None


from python_code import User1

def test_User1___init__():
    assert User1.__init__(User1('', '\x00'), '\x00\x00', '') == None

