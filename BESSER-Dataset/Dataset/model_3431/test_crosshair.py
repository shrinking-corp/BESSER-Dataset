from python_code import school_Named

def test_school_Named___init__():
    assert school_Named.__init__(school_Named(''), '') == None

from python_code import school_Student

def test_school_Student___init__():
    assert school_Student.__init__(school_Student(0, school_Student=set()), 0, school_Student=set()) == None
