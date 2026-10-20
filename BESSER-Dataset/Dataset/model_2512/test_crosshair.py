from python_code import test_A

def test_test_A___init__():
    assert test_A.__init__(test_A()) == None

def test_test_A_op1():
    assert test_A.op1(test_A()) == None


from python_code import test_D

def test_test_D___init__():
    assert test_D.__init__(test_D(''), '') == None


from python_code import test_OptionTestClass

def test_test_OptionTestClass___init__():
    assert test_OptionTestClass.__init__(test_OptionTestClass('', '\x00'), '\x00\x00', '') == None

