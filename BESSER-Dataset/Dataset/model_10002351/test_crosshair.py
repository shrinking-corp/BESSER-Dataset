from python_code import It

def test_It___init__():
    assert It.__init__(It(''), '') == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person('', 0), '', 0) == None


from python_code import appointment

def test_appointment___init__():
    assert appointment.__init__(appointment(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import employee

def test_employee___init__():
    assert employee.__init__(employee(0, '\x00', '', ''), 0, '', '', '') == None

