from python_code import university_Course
from python_code import university_CourseCatalog

def test_university_Course___init__():
    assert university_Course.__init__(university_Course('', '', 0, university_Course=university_CourseCatalog()), '\x00', '', 0, university_Course=university_CourseCatalog()) == None

