from python_code import tdt4250_Answer

def test_tdt4250_Answer___init__():
    assert tdt4250_Answer.__init__(tdt4250_Answer(''), '') == None


from python_code import tdt4250_Assignment

def test_tdt4250_Assignment___init__():
    assert tdt4250_Assignment.__init__(tdt4250_Assignment(0, '', '', True, tdt4250_Assignment=set()), 0, '', '', False, tdt4250_Assignment=set()) == None


from python_code import tdt4250_Course

def test_tdt4250_Course___init__():
    assert tdt4250_Course.__init__(tdt4250_Course(0, 0, '', tdt4250_Course4=set(), tdt4250_Course=set(), tdt4250_Course2=set()), 0, 0, '', tdt4250_Course4=set(), tdt4250_Course=set(), tdt4250_Course2=set()) == None


from python_code import tdt4250_Person

def test_tdt4250_Person___init__():
    assert tdt4250_Person.__init__(tdt4250_Person(0, '\x00'), 0, '\x00') == None


from python_code import tdt4250_Teacher

def test_tdt4250_Teacher___init__():
    assert tdt4250_Teacher.__init__(tdt4250_Teacher('', tdt4250_Teacher=set()), '', tdt4250_Teacher=set()) == None

