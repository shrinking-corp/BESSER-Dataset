from python_code import MyClass

def test_MyClass___init__():
    assert MyClass.__init__(MyClass('', '\x00'), '\x00\x00', '') == None

