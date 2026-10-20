from python_code import Doctor

def test_Doctor___init__():
    assert Doctor.__init__(Doctor('', '\x00'), '\x00\x00', '') == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient(0, '', '', '', ''), 0, '', '', '', '') == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person('', '', '', 0, ''), '', '', '', 0, '') == None


from python_code import Staff

def test_Staff___init__():
    assert Staff.__init__(Staff('', '', '', '', ''), '', '', '', '', '') == None

