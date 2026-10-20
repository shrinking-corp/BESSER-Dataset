from python_code import SubTestClass
from python_code import TestPackage_TestClass

def test_TestPackage_TestClass___init__():
    assert TestPackage_TestClass.__init__(TestPackage_TestClass(True, TestPackage_TestClass=SubTestClass()), False, TestPackage_TestClass=SubTestClass()) == None

def test_TestPackage_TestClass_testOp():
    assert TestPackage_TestClass.testOp(TestPackage_TestClass(False, TestPackage_TestClass=SubTestClass())) == None

