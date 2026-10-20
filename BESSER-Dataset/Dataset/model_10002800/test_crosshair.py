from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person(0, '', '\x00\x00'), 0, '', '') == None

