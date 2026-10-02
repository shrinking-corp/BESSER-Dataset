from python_code import Customer_User

def test_Customer_User___init__():
    assert Customer_User.__init__(Customer_User('', '\x00'), '\x00\x00', '') == None
