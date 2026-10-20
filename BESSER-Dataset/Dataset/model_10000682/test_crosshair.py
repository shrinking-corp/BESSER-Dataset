from python_code import Lecturer1

def test_Lecturer1___init__():
    assert Lecturer1.__init__(Lecturer1(''), '') == None


from python_code import Society1

def test_Society1___init__():
    assert Society1.__init__(Society1(0), 0) == None


from python_code import Student1

def test_Student1___init__():
    assert Student1.__init__(Student1('', '', 0), '\x00', '', 0) == None

