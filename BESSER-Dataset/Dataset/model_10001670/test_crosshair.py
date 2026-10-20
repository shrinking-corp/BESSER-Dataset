from python_code import Custom_Login

def test_Custom_Login___init__():
    assert Custom_Login.__init__(Custom_Login('', '\x00'), '\x00\x00', '') == None


from python_code import Social_Login

def test_Social_Login___init__():
    assert Social_Login.__init__(Social_Login('', '\x00'), '\x00\x00', '') == None

