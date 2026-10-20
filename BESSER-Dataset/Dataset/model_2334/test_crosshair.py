from python_code import personDsl_Person
from python_code import personDsl_PersonContainer

def test_personDsl_Person___init__():
    assert personDsl_Person.__init__(personDsl_Person(0, '\x00', personDsl_Person=personDsl_PersonContainer()), 0, '\x00', personDsl_Person=personDsl_PersonContainer()) == None

