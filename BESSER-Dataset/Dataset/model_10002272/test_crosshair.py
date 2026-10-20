from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee('', '\x00'), '\x00\x00', '') == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient('', '\x00'), '\x00\x00', '') == None


from python_code import inPatient

def test_inPatient___init__():
    assert inPatient.__init__(inPatient('', '', '\x00\x00'), '', '', '') == None


from python_code import outPatient

def test_outPatient___init__():
    assert outPatient.__init__(outPatient('', '', '\x00\x00'), '', '', '') == None

