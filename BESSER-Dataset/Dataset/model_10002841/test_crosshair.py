from python_code import Patient_Check_In__aReceptionist

def test_Patient_Check_In__aReceptionist___init__():
    assert Patient_Check_In__aReceptionist.__init__(Patient_Check_In__aReceptionist(0, '\x00', patients3=set()), 0, '', patients3=set()) == None


from python_code import Patient_Check_In_aDoctor

def test_Patient_Check_In_aDoctor___init__():
    assert Patient_Check_In_aDoctor.__init__(Patient_Check_In_aDoctor(0, '', '', '', patient0=set()), 0, '', '', '', patient0=set()) == None


from python_code import Patient_Check_In_aNurse

def test_Patient_Check_In_aNurse___init__():
    assert Patient_Check_In_aNurse.__init__(Patient_Check_In_aNurse(0, '', '\x00\x00'), 0, '', '') == None

