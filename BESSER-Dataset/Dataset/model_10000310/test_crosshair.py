from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator('\x00\x00', '', employee1=set()), '', '', employee1=set()) == None


from python_code import Buyer

def test_Buyer___init__():
    assert Buyer.__init__(Buyer('', property7=set()), '', property7=set()) == None


from python_code import Reg_User

def test_Reg_User___init__():
    assert Reg_User.__init__(Reg_User('', '', '', requirement8=set()), '', '', '', requirement8=set()) == None


from python_code import Requirement

def test_Requirement___init__():
    assert Requirement.__init__(Requirement('', '', '', '', user9=set()), '', '', '', '', user9=set()) == None


from python_code import Seller

def test_Seller___init__():
    assert Seller.__init__(Seller('\x00\x00', '', property3=set()), '', '', property3=set()) == None

