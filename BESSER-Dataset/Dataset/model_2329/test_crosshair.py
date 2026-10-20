from python_code import My_TestClass

def test_My_TestClass___init__():
    assert My_TestClass.__init__(My_TestClass('', '\x00'), '\x00\x00', '') == None

