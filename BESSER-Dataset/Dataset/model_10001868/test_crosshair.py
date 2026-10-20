from python_code import Doctor

def test_Doctor___init__():
    assert Doctor.__init__(Doctor('', '\x00'), '\x00\x00', '') == None


from python_code import Hospital

def test_Hospital___init__():
    assert Hospital.__init__(Hospital('', '', '', person1=set(), department2=set()), '', '', '', person1=set(), department2=set()) == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient('', '', '', '', 0, '', '', '', '', '', operations_Staff6=set()), '\x00', '', '', '', 0, '', '', '', '', '', operations_Staff6=set()) == None


from python_code import Person

def test_Person___init__():
    assert Person.__init__(Person('\x00', '', '', '', '', '', '', '', '', hospital0=set()), '', '\x00', '', '', '', '', '', '', '', hospital0=set()) == None


from python_code import Department
from python_code import Staff

def test_Staff___init__():
    assert Staff.__init__(Staff('\x00\x00', '', '', '', department5=Department()), '', '', '', '', department5=Department()) == None

