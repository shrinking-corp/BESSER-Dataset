from python_code import Account

def test_Account___init__():
    assert Account.__init__(Account('\x00\x00', '', '', ''), '', '', '', '') == None

