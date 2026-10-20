from python_code import Recollector

def test_Recollector___init__():
    assert Recollector.__init__(Recollector('', '', '', '', ''), '', '', '', '', '') == None


from python_code import User_Account

def test_User_Account___init__():
    assert User_Account.__init__(User_Account('\x00\x00', '', '', ''), '', '', '', '') == None

