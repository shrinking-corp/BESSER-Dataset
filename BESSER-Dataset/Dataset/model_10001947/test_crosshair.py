from python_code import Doctor
from python_code import Model

def test_Doctor___init__():
    assert Doctor.__init__(Doctor('', model10=Model(), treatment12=set()), '', model10=Model(), treatment12=set()) == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient(0, '', '\x00\x00'), 0, '', '') == None


from python_code import user

def test_user___init__():
    assert user.__init__(user('\x00\x00', '', input_Data8=set()), '', '', input_Data8=set()) == None

