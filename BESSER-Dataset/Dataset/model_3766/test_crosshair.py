from python_code import merge_Clazz
from python_code import merge_EObject

def test_merge_Clazz___init__():
    assert merge_Clazz.__init__(merge_Clazz(0.0, merge_Clazz=merge_EObject()), 0.0, merge_Clazz=merge_EObject()) == None

def test_merge_Clazz_operation2():
    assert merge_Clazz.operation2(merge_Clazz(0.0, merge_Clazz=merge_EObject()), '') == None

def test_merge_Clazz_operation():
    assert merge_Clazz.operation(merge_Clazz(0.0, merge_Clazz=merge_EObject())) == None

