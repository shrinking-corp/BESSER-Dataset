from python_code import Administrative_Staff

def test_Administrative_Staff___init__():
    assert Administrative_Staff.__init__(Administrative_Staff('', '\x00'), '\x00\x00', '') == None


from python_code import Hospital

def test_Hospital___init__():
    assert Hospital.__init__(Hospital('', 0, 0, '', person1=set(), staff3=set()), '', 0, 0, '', person1=set(), staff3=set()) == None


from python_code import Operation_Staff

def test_Operation_Staff___init__():
    assert Operation_Staff.__init__(Operation_Staff('', '', '', patient4=set()), '', '', '', patient4=set()) == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient(0, '', '', '', 0, '', '', operation_Staff5=set()), 0, '', '', '', 0, '', '', operation_Staff5=set()) == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person(0, '', '', '', '', 0, '', '', '', 0, hospital0=set()), 0, '', '', '', '', 0, '', '', '', 0, hospital0=set()) == None


from python_code import Staff

def test_Staff___init__():
    assert Staff.__init__(Staff('', '', '', '', hospital2=set()), '', '', '', '', hospital2=set()) == None


from python_code import Techinal_Staff

def test_Techinal_Staff___init__():
    assert Techinal_Staff.__init__(Techinal_Staff('', '\x00'), '\x00\x00', '') == None

