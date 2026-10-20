from python_code import Doctor

def test_Doctor___init__():
    assert Doctor.__init__(Doctor('', '\x00'), '\x00\x00', '') == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Department
from python_code import Staff

def test_Staff___init__():
    assert Staff.__init__(Staff('', '', '\x00\x00', department3=Department()), '', '', '', department3=Department()) == None

