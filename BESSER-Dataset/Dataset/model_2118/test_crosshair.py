from python_code import testing_TestCase
from python_code import testing_TestCoverage

def test_testing_TestCase___init__():
    assert testing_TestCase.__init__(testing_TestCase('', '\x00', testing_TestCase=testing_TestCoverage()), '\x00\x00', '', testing_TestCase=testing_TestCoverage()) == None


from python_code import testing_Adapter
from python_code import testing_TestSuite

def test_testing_TestSuite___init__():
    assert testing_TestSuite.__init__(testing_TestSuite('', testing_TestSuite=set(), testing_TestSuite2=testing_Adapter()), '', testing_TestSuite=set(), testing_TestSuite2=testing_Adapter()) == None


from python_code import testing_Adapter
from python_code import testing_Transition

def test_testing_Transition___init__():
    assert testing_Transition.__init__(testing_Transition('', '\x00', testing_Transition=testing_Adapter()), '\x00\x00', '', testing_Transition=testing_Adapter()) == None

