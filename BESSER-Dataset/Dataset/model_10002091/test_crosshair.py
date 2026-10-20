from python_code import Hospital

def test_Hospital___init__():
    assert Hospital.__init__(Hospital('\x00\x00', 0, ward0=set()), '', 0, ward0=set()) == None


from python_code import consultant_doctor
from python_code import doctor
from python_code import junior_doctor
from python_code import team

def test_doctor___init__():
    assert doctor.__init__(doctor('', '', '\x00\x00', consultant_doctor2=consultant_doctor(), junior_doctor4=junior_doctor(), team6=team()), '', '', '', consultant_doctor2=consultant_doctor(), junior_doctor4=junior_doctor(), team6=team()) == None

