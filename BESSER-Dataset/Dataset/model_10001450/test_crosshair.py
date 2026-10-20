from python_code import Diagnose

def test_Diagnose___init__():
    assert Diagnose.__init__(Diagnose(0, '', '\x00\x00'), 0, '', '') == None


from python_code import Doctor

def test_Doctor___init__():
    assert Doctor.__init__(Doctor(''), '') == None


from python_code import Employee

def test_Employee___init__():
    assert Employee.__init__(Employee(0, '', '', '', '', '', '\x00', ''), 0, '', '', '', '', '', '', '') == None


from python_code import Nurse

def test_Nurse___init__():
    assert Nurse.__init__(Nurse('', bill15=set()), '', bill15=set()) == None


from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient(0.0, 0, '', '', '', '', '', appointment9=set()), 0.0, 0, '', '', '', '', '\x00', appointment9=set()) == None


from python_code import Schedule

def test_Schedule___init__():
    assert Schedule.__init__(Schedule(0, '', '', '', False), 0, '', '', '', False) == None


from python_code import TreatmentList

def test_TreatmentList___init__():
    assert TreatmentList.__init__(TreatmentList(0, '', 0.0, appointmentDiagnose11=set()), 0, '', 0.0, appointmentDiagnose11=set()) == None

