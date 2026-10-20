from python_code import Card

def test_Card___init__():
    assert Card.__init__(Card('', 0, '\x00\x00'), '', 0, '') == None

