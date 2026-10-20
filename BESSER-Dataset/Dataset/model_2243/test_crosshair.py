from python_code import course_desc_CourseWork
from python_code import course_desc_Timetable

def test_course_desc_CourseWork___init__():
    assert course_desc_CourseWork.__init__(course_desc_CourseWork(0, '', False, False, '', course_desc_CourseWork=course_desc_Timetable()), 0, '', False, False, '', course_desc_CourseWork=course_desc_Timetable()) == None


from python_code import course_desc_EvaluationWithDeadline

def test_course_desc_EvaluationWithDeadline___init__():
    assert course_desc_EvaluationWithDeadline.__init__(course_desc_EvaluationWithDeadline(''), '') == None


from python_code import course_desc_Person
from python_code import course_desc_PersonRole
from python_code import course_desc_Univ

def test_course_desc_Person___init__():
    assert course_desc_Person.__init__(course_desc_Person('', '', '', '', Person=course_desc_PersonRole(), linkedTo=set(), course_desc_Person=course_desc_Univ()), '', '', '', '', Person=course_desc_PersonRole(), linkedTo=set(), course_desc_Person=course_desc_Univ()) == None

