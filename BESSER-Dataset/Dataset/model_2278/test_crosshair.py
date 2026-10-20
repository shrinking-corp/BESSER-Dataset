from python_code import edu_Course
from python_code import edu_Take_Course

def test_edu_Course___init__():
    assert edu_Course.__init__(edu_Course(0, '\x00', edu_Course=edu_Take_Course()), 0, '\x00', edu_Course=edu_Take_Course()) == None


import datetime as _ch_datetime
from python_code import edu_Student
from python_code import edu_Take_Course

def test_edu_Student___init__():
    assert edu_Student.__init__(edu_Student(0, '\x00', _ch_datetime.date(1, 1, 3), edu_Student=edu_Take_Course()), 0, '', _ch_datetime.date(1, 1, 1), edu_Student=edu_Take_Course()) == None

def test_edu_Student_getAge():
    assert edu_Student.getAge(edu_Student(0, '', _ch_datetime.date(1, 1, 1), edu_Student=edu_Take_Course())) == None

