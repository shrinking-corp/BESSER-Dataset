from python_code import Exam
from python_code import Subject

def test_Exam___init__():
    assert Exam.__init__(Exam('', '', 0, Subject('', 0, 0, 0), 0), '', '', 0, Subject('', 0, 0, 0), 0) == None


from python_code import Subject

def test_Subject___init__():
    assert Subject.__init__(Subject('\x00\x00', 0, 0, 0), '', 0, 0, 0) == None

