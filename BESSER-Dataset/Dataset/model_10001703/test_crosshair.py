from python_code import user_Address

def test_user_Address___init__():
    assert user_Address.__init__(user_Address('', '', '', '', ''), '', '', '', '', '') == None

from python_code import user_Provider

def test_user_Provider___init__():
    assert user_Provider.__init__(user_Provider('', '', '', '', ''), '', '', '', '', '') == None

from python_code import user_Tags

def test_user_Tags___init__():
    assert user_Tags.__init__(user_Tags('', '\x00'), '\x00\x00', '') == None
