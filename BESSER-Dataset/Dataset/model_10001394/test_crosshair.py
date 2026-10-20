from python_code import Hospital

def test_Hospital___init__():
    assert Hospital.__init__(Hospital('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Hospital_Doctor

def test_Hospital_Doctor___init__():
    assert Hospital_Doctor.__init__(Hospital_Doctor(0, '', '', '', 0, patient0=set()), 0, '', '', '\x00', 0, patient0=set()) == None


from python_code import Hospital__Receptionist

def test_Hospital__Receptionist___init__():
    assert Hospital__Receptionist.__init__(Hospital__Receptionist(0, '\x00', patients3=set()), 0, '', patients3=set()) == None

