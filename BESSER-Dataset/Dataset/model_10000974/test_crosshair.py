from python_code import Bill

def test_Bill___init__():
    assert Bill.__init__(Bill(0, '', 0, '', '', 0, '', 0, doctor5=set(), patient7=set()), 0, '', 0, '', '', 0, '', 0, doctor5=set(), patient7=set()) == None


from python_code import Doctor

def test_Doctor___init__():
    assert Doctor.__init__(Doctor(0, '', 0, '', '', '', '\x00', '', appointment1=set(), doctorSchedule2=set(), bill4=set()), 0, '', 0, '', '', '', '', '', appointment1=set(), doctorSchedule2=set(), bill4=set()) == None


from python_code import DoctorSchedule

def test_DoctorSchedule___init__():
    assert DoctorSchedule.__init__(DoctorSchedule(0, '', '', '', doctor3=set()), 0, '', '', '', doctor3=set()) == None


from python_code import DoctorServices

def test_DoctorServices___init__():
    assert DoctorServices.__init__(DoctorServices(0, '', '', '', '', appointment10=set()), 0, '', '', '\x00', '', appointment10=set()) == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient(0, '', 0, '', '', '', '', '', '', '', '', '', '', '', '\x00', bill6=set(), appointment8=set()), 0, '', 0, '', '', '', '', '', '', '', '', '', '', '', '', bill6=set(), appointment8=set()) == None


from python_code import Receptionist

def test_Receptionist___init__():
    assert Receptionist.__init__(Receptionist(0, '', 0, '', '', '', ''), 0, '\x00', 0, '', '', '', '') == None


from python_code import UserRoles

def test_UserRoles___init__():
    assert UserRoles.__init__(UserRoles(0, '\x00', userwithRole14=set()), 0, '', userwithRole14=set()) == None


from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users(0, '', '', '', '', '', '\x00', '', '', '', 0, '', userwithRole12=set()), 0, '', '', '', '', '', '', '', '', '', 0, '', userwithRole12=set()) == None


from python_code import UserwithRole

def test_UserwithRole___init__():
    assert UserwithRole.__init__(UserwithRole(0, 0, users13=set(), userRoles15=set()), 0, 0, users13=set(), userRoles15=set()) == None

