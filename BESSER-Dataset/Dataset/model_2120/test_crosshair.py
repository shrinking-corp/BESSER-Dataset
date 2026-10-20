from python_code import ValidationModel_TestContainer
from python_code import ValidationModel_UnitTest

def test_ValidationModel_UnitTest___init__():
    assert ValidationModel_UnitTest.__init__(ValidationModel_UnitTest('', '', False, ValidationModel_UnitTest=ValidationModel_TestContainer()), '\x00', '', False, ValidationModel_UnitTest=ValidationModel_TestContainer()) == None

