from python_code import Example_Member

def test_Example_Member___init__():
    assert Example_Member.__init__(Example_Member('', '\x00'), '\x00\x00', '') == None

