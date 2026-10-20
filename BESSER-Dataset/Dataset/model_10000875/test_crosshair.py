from python_code import Department

def test_Department___init__():
    assert Department.__init__(Department('', 0, student0=set(), course16=set()), '', 0, student0=set(), course16=set()) == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person('', 0, '\x00', '', '', '', 0, '', course9=set()), '', 0, '', '', '\x00', '', 0, '', course9=set()) == None


from python_code import course

def test_course___init__():
    assert course.__init__(course('', 0, '', 0, student3=set(), admin4=set(), person8=set(), department17=set()), '', 0, '', 0, student3=set(), admin4=set(), person8=set(), department17=set()) == None

