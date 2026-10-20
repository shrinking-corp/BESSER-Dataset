from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin(''), '') == None


from python_code import Course

def test_Course___init__():
    assert Course.__init__(Course('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import Email

def test_Email___init__():
    assert Email.__init__(Email(''), '') == None


from python_code import Exam

def test_Exam___init__():
    assert Exam.__init__(Exam('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Finance

def test_Finance___init__():
    assert Finance.__init__(Finance('', '\x00'), '\x00\x00', '') == None


from python_code import Insturctor

def test_Insturctor___init__():
    assert Insturctor.__init__(Insturctor(''), '') == None

