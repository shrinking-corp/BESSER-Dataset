from python_code import B_B

def test_B_B___init__():
    assert B_B.__init__(B_B('', '', '\x00\x00'), '', '', '') == None

