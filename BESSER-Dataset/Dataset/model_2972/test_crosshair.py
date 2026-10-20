from python_code import My2_TestClass2

def test_My2_TestClass2___init__():
    assert My2_TestClass2.__init__(My2_TestClass2('', '\x00'), '\x00\x00', '') == None

