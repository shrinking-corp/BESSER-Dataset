from python_code import course_CourseInstance
from python_code import course_CourseWork

def test_course_CourseWork___init__():
    assert course_CourseWork.__init__(course_CourseWork(0, 0, CourseWork=course_CourseInstance(), courseWork=course_CourseInstance()), 0, 0, CourseWork=course_CourseInstance(), courseWork=course_CourseInstance()) == None


from python_code import course_CourseInstance
from python_code import course_Evaluation
from python_code import course_Student

def test_course_Evaluation___init__():
    assert course_Evaluation.__init__(course_Evaluation(0, 0, 0, Evaluation=course_CourseInstance(), evaluation=course_CourseInstance(), evaluation30=set(), Evaluation51=course_Student()), 0, 0, 0, Evaluation=course_CourseInstance(), evaluation=course_CourseInstance(), evaluation30=set(), Evaluation51=course_Student()) == None


from python_code import course_Person

def test_course_Person___init__():
    assert course_Person.__init__(course_Person(''), '') == None

