from python_code import Professor

def test_Professor___init__():
    assert Professor.__init__(Professor(0, '\x00'), 0, '\x00') == None


from python_code import Student

def test_Student___init__():
    assert Student.__init__(Student(0, 0), 0, 0) == None

