from python_code import hairDressersRegSys_Haircuts

def test_hairDressersRegSys_Haircuts___init__():
    assert hairDressersRegSys_Haircuts.__init__(hairDressersRegSys_Haircuts(False, False, False), False, False, False) == None


from python_code import hairDressersRegSys_Other

def test_hairDressersRegSys_Other___init__():
    assert hairDressersRegSys_Other.__init__(hairDressersRegSys_Other(''), '') == None


import datetime as _ch_datetime
from python_code import hairDressersRegSys_Person

def test_hairDressersRegSys_Person___init__():
    assert hairDressersRegSys_Person.__init__(hairDressersRegSys_Person('', '', '\x00\x00', _ch_datetime.date(1, 1, 1)), '', '', '', _ch_datetime.date(1, 1, 1)) == None

def test_hairDressersRegSys_Person_GetAge():
    assert hairDressersRegSys_Person.GetAge(hairDressersRegSys_Person('', '', '\x00', _ch_datetime.date(1, 1, 3))) == None


from python_code import hairDressersRegSys_Styling

def test_hairDressersRegSys_Styling___init__():
    assert hairDressersRegSys_Styling.__init__(hairDressersRegSys_Styling(True), False) == None

