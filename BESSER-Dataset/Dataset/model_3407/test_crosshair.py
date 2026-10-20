from python_code import education_Course
from python_code import education_Teacher

def test_education_Course___init__():
    assert education_Course.__init__(education_Course('', education_Course=set(), education_Course2=education_Teacher()), '', education_Course=set(), education_Course2=education_Teacher()) == None

def test_education_Course_start():
    assert education_Course.start(education_Course('', education_Course=set(), education_Course2=education_Teacher()), '') == None

def test_education_Course_finish():
    assert education_Course.finish(education_Course('', education_Course=set(), education_Course2=education_Teacher()), '') == None


from python_code import education_Person

def test_education_Person___init__():
    assert education_Person.__init__(education_Person('', '\x00'), '\x00\x00', '') == None

