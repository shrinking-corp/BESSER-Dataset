from python_code import Administrator

def test_Administrator___init__():
    assert Administrator.__init__(Administrator('', '\x00'), '\x00\x00', '') == None


from python_code import Doctor

def test_Doctor___init__():
    assert Doctor.__init__(Doctor(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import Manager

def test_Manager___init__():
    assert Manager.__init__(Manager(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import Pets

def test_Pets___init__():
    assert Pets.__init__(Pets(0, '\x00', '', 0), 0, '', '', 0) == None


from python_code import User

def test_User___init__():
    assert User.__init__(User('', '\x00'), '\x00\x00', '') == None

