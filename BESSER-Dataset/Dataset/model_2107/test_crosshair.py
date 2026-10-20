from python_code import tests_Test
from python_code import tests_TestsModel

def test_tests_Test___init__():
    assert tests_Test.__init__(tests_Test('', '\x00', tests_Test=tests_TestsModel()), '\x00\x00', '', tests_Test=tests_TestsModel()) == None

