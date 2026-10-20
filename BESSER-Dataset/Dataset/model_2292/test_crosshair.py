import datetime as _ch_datetime
from python_code import Lecture
from python_code import Tutorial
from python_code import universityextended_administration_Course

def test_universityextended_administration_Course___init__():
    assert universityextended_administration_Course.__init__(universityextended_administration_Course('', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), course=Lecture(), course16=Tutorial(), course19=set()), '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), course=Lecture(), course16=Tutorial(), course19=set()) == None


from python_code import Room
from python_code import Time
from python_code import universityextended_administration_Event

def test_universityextended_administration_Event___init__():
    assert universityextended_administration_Event.__init__(universityextended_administration_Event('', universityextended_administration_Event=Time(), universityextended_administration_Event31=Room()), '', universityextended_administration_Event=Time(), universityextended_administration_Event31=Room()) == None


from python_code import Course
from python_code import Professor
from python_code import universityextended_administration_Lecture

def test_universityextended_administration_Lecture___init__():
    assert universityextended_administration_Lecture.__init__(universityextended_administration_Lecture('', lecture=Course(), lectures=Professor()), '', lecture=Course(), lectures=Professor()) == None


from python_code import universityextended_administration_Room

def test_universityextended_administration_Room___init__():
    assert universityextended_administration_Room.__init__(universityextended_administration_Room('', 0, 0), '\x00', 0, 0) == None


from python_code import universityextended_administration_Time

def test_universityextended_administration_Time___init__():
    assert universityextended_administration_Time.__init__(universityextended_administration_Time('', 0, 0), '\x00', 0, 0) == None


from python_code import Course
from python_code import Student
from python_code import universityextended_connection_Visits

def test_universityextended_connection_Visits___init__():
    assert universityextended_connection_Visits.__init__(universityextended_connection_Visits('', visitor=Course(), courseVisit=Student()), '', visitor=Course(), courseVisit=Student()) == None


from python_code import universityextended_University
from python_code import universityextended_people_Assistant

def test_universityextended_people_Assistant___init__():
    assert universityextended_people_Assistant.__init__(universityextended_people_Assistant(False, tutor=set(), Person=universityextended_University()), False, tutor=set(), Person=universityextended_University()) == None


from python_code import universityextended_people_Person

def test_universityextended_people_Person___init__():
    assert universityextended_people_Person.__init__(universityextended_people_Person(''), '') == None


from python_code import universityextended_University
from python_code import universityextended_people_Professor

def test_universityextended_people_Professor___init__():
    assert universityextended_people_Professor.__init__(universityextended_people_Professor('', lecturer=set(), Person=universityextended_University()), '', lecturer=set(), Person=universityextended_University()) == None


from python_code import universityextended_University
from python_code import universityextended_people_Student

def test_universityextended_people_Student___init__():
    assert universityextended_people_Student.__init__(universityextended_people_Student('', student=set(), Person=universityextended_University()), '', student=set(), Person=universityextended_University()) == None

