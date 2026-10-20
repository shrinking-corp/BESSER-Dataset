from python_code import test_C
from python_code import test_D

def test_test_D___init__():
    assert test_D.__init__(test_D('', 0, test_D=test_C()), '', 0, test_D=test_C()) == None


from python_code import test_C
from python_code import test_EClass
from python_code import test_EClassToEStringMap

def test_test_EClassToEStringMap___init__():
    assert test_EClassToEStringMap.__init__(test_EClassToEStringMap('', test_EClassToEStringMap=test_C(), test_EClassToEStringMap16=test_EClass()), '', test_EClassToEStringMap=test_C(), test_EClassToEStringMap16=test_EClass()) == None

