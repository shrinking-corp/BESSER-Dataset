from python_code import Auditorium

def test_Auditorium___init__():
    assert Auditorium.__init__(Auditorium(0, '\x00', 0, False), 0, '', 0, False) == None


from python_code import DocumentStorage

def test_DocumentStorage___init__():
    assert DocumentStorage.__init__(DocumentStorage('\x00\x00', 0, False, 0), '', 0, False, 0) == None


from python_code import EducationalPlan

def test_EducationalPlan___init__():
    assert EducationalPlan.__init__(EducationalPlan(0, 0, 0), 0, 0, 0) == None


from python_code import Group

def test_Group___init__():
    assert Group.__init__(Group(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import Specialty

def test_Specialty___init__():
    assert Specialty.__init__(Specialty(0, 0, '', 0), 0, 0, '', 0) == None


from python_code import Subject

def test_Subject___init__():
    assert Subject.__init__(Subject(0, 0, '', assoc_00=set()), 0, 0, '', assoc_00=set()) == None


from python_code import SubjectShedule

def test_SubjectShedule___init__():
    assert SubjectShedule.__init__(SubjectShedule(0, 0, 0, 0, '', 0, 0), 0, 0, 0, 0, '', 0, 0) == None


from python_code import SubjectSheduleController

def test_SubjectSheduleController___init__():
    assert SubjectSheduleController.__init__(SubjectSheduleController('', 0, 0, '', 0, 0), '', 0, 0, '', 0, 0) == None


from python_code import TimeCreditForEducationalSemester

def test_TimeCreditForEducationalSemester___init__():
    assert TimeCreditForEducationalSemester.__init__(TimeCreditForEducationalSemester(0, 0, 0, 0, 0), 0, 0, 0, 0, 0) == None


from python_code import TimeInterval

def test_TimeInterval___init__():
    assert TimeInterval.__init__(TimeInterval(0, '', 0, 0, 0), 0, '', 0, 0, 0) == None


from python_code import Users

def test_Users___init__():
    assert Users.__init__(Users(0, '', '', '', '', '', 0, '', '\x00', '', '', '', 0), 0, '', '', '', '', '', 0, '', '', '', '', '\x00', 0) == None

