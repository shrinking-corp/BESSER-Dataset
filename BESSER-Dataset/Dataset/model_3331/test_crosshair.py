from python_code import psample_Object

def test_psample_Object___init__():
    assert psample_Object.__init__(psample_Object(''), '') == None


from python_code import psample_Package

def test_psample_Package___init__():
    assert psample_Package.__init__(psample_Package('', psample_Package=set()), '', psample_Package=set()) == None


from python_code import psample_Class
from python_code import psample_Function
from python_code import psample_PrimitiveTypeVariable

def test_psample_PrimitiveTypeVariable___init__():
    assert psample_PrimitiveTypeVariable.__init__(psample_PrimitiveTypeVariable(True, psample_PrimitiveTypeVariable=psample_Class(), psample_PrimitiveTypeVariable5=psample_Function()), False, psample_PrimitiveTypeVariable=psample_Class(), psample_PrimitiveTypeVariable5=psample_Function()) == None


from python_code import psample_Function
from python_code import psample_Variable

def test_psample_Variable___init__():
    assert psample_Variable.__init__(psample_Variable(True, psample_Variable=psample_Function()), False, psample_Variable=psample_Function()) == None

