from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee('', '', '\x00\x00'), '', '', '') == None


from python_code import Invoice

def test_Invoice___init__():
    assert Invoice.__init__(Invoice('', '', 0, 0.0), '', '', 0, 0.0) == None


from python_code import SalariedEmployee

def test_SalariedEmployee___init__():
    assert SalariedEmployee.__init__(SalariedEmployee(0.0), 0.0) == None

