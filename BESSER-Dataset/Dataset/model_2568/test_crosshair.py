from python_code import TestPackage_AbstractTestClass
from python_code import TestPackage_TestIndexEntry

def test_TestPackage_AbstractTestClass___init__():
    assert TestPackage_AbstractTestClass.__init__(TestPackage_AbstractTestClass('', TestPackage_AbstractTestClass=TestPackage_TestIndexEntry()), '', TestPackage_AbstractTestClass=TestPackage_TestIndexEntry()) == None


from python_code import TestPackage_TestClass1

def test_TestPackage_TestClass1___init__():
    assert TestPackage_TestClass1.__init__(TestPackage_TestClass1(''), '') == None

def test_TestPackage_TestClass1_testOperation():
    assert TestPackage_TestClass1.testOperation(TestPackage_TestClass1(''), 0) == None

