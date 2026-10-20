from python_code import persons_Person

def test_persons_Person___init__():
    assert persons_Person.__init__(persons_Person('', '', '\x00\x00'), '', '', '') == None

