from python_code import UserProperties

def test_UserProperties___init__():
    assert UserProperties.__init__(UserProperties('', '\x00'), '\x00\x00', '') == None

