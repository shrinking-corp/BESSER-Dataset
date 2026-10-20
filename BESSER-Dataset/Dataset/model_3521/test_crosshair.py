from python_code import testenums_Root

def test_testenums_Root___init__():
    assert testenums_Root.__init__(testenums_Root('', '\x00'), '\x00\x00', '') == None

