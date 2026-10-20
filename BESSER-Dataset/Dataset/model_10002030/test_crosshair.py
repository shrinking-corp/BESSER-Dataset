from python_code import vendor

def test_vendor___init__():
    assert vendor.__init__(vendor('\x00\x00', '', '', ''), '', '', '', '') == None

