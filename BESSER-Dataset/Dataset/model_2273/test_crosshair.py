from python_code import university_Course
from python_code import university_CourseCatalog

def test_university_Course___init__():
    assert university_Course.__init__(university_Course('', '', 0, university_Course=university_CourseCatalog()), '\x00', '', 0, university_Course=university_CourseCatalog()) == None


from python_code import university_Person

def test_university_Person___init__():
    assert university_Person.__init__(university_Person('', university_Person=set()), '', university_Person=set()) == None


from python_code import university_Staff

def test_university_Staff___init__():
    assert university_Staff.__init__(university_Staff('', university_Staff3=set(), university_Staff=set()), '', university_Staff3=set(), university_Staff=set()) == None

