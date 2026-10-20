from python_code import Express

def test_Express___init__():
    assert Express.__init__(Express('', '\x00'), '\x00\x00', '') == None


from python_code import Express1

def test_Express1___init__():
    assert Express1.__init__(Express1(''), '') == None


from python_code import Pessanger

def test_Pessanger___init__():
    assert Pessanger.__init__(Pessanger(0, 0), 0, 0) == None


from python_code import SuperFast

def test_SuperFast___init__():
    assert SuperFast.__init__(SuperFast('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import SuperFast1

def test_SuperFast1___init__():
    assert SuperFast1.__init__(SuperFast1('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

