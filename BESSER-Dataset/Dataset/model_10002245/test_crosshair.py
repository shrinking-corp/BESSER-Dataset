from python_code import MyClass2
from python_code import MyClass4

def test_MyClass2___init__():
    assert MyClass2.__init__(MyClass2(0, '', '\x00\x00', myClass41=MyClass4()), 0, '', '', myClass41=MyClass4()) == None

