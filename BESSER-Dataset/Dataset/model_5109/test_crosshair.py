from python_code import testPackage_Container
from python_code import testPackage_TestElementA
from python_code import testPackage_TestElementB

def test_testPackage_TestElementA___init__():
    assert testPackage_TestElementA.__init__(testPackage_TestElementA('', 0, testPackage_TestElementA=testPackage_Container(), testPackage_TestElementA2=testPackage_TestElementB()), '', 0, testPackage_TestElementA=testPackage_Container(), testPackage_TestElementA2=testPackage_TestElementB()) == None

