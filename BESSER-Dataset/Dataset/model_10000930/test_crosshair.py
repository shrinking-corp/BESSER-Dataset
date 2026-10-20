from python_code import Login
from python_code import Profile

def test_Login___init__():
    assert Login.__init__(Login(Profile('', '', '', ''), '', ''), Profile('', '', '', ''), '\x00', '') == None


from python_code import Profile

def test_Profile___init__():
    assert Profile.__init__(Profile('\x00\x00', '', '', ''), '', '', '', '') == None

