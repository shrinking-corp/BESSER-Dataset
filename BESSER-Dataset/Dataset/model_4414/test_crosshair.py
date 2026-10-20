from python_code import arduino_Pin

def test_arduino_Pin___init__():
    assert arduino_Pin.__init__(arduino_Pin('', '\x00'), '\x00\x00', '') == None

