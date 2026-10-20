from python_code import Account

def test_Account___init__():
    assert Account.__init__(Account('', '', '\x00\x00'), '', '', '') == None


from python_code import Player

def test_Player___init__():
    assert Player.__init__(Player('\x00\x00', '', '', ''), '', '', '', '') == None

