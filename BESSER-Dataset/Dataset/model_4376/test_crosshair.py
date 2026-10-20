from python_code import test_Person

def test_test_Person___init__():
    assert test_Person.__init__(test_Person(0), 0) == None

def test_test_Person_isAgeValid():
    assert test_Person.isAgeValid(test_Person(0), 0, '\x00\x00') == None

