from python_code import Customer

def test_Customer___init__():
    assert Customer.__init__(Customer('', '', '\x00\x00'), '', '', '') == None

