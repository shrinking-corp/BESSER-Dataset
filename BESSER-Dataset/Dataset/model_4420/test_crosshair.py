from python_code import arduino_Bench

def test_arduino_Bench___init__():
    assert arduino_Bench.__init__(arduino_Bench('', arduino_Bench=set()), '', arduino_Bench=set()) == None


from python_code import arduino_Port

def test_arduino_Port___init__():
    assert arduino_Port.__init__(arduino_Port('\x00\x00', '', 0, ''), '', '', 0, '') == None

