from python_code import testSuite_Model
from python_code import testSuite_Test

def test_testSuite_Test___init__():
    assert testSuite_Test.__init__(testSuite_Test('', testSuite_Test=testSuite_Model()), '', testSuite_Test=testSuite_Model()) == None

