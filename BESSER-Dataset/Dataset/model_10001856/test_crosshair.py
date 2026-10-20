from python_code import Department

def test_Department___init__():
    assert Department.__init__(Department(0, '\x00', 0, ''), 0, '', 0, '') == None


from python_code import Mark
from python_code import Student

def test_Mark___init__():
    assert Mark.__init__(Mark(Student('', 0), 0), Student('\x00', 0), 0) == None


from python_code import Quiz

def test_Quiz___init__():
    assert Quiz.__init__(Quiz('', '', '\x00\x00'), '', '', '') == None


from python_code import Student

def test_Student___init__():
    assert Student.__init__(Student('', 0), '', 0) == None


from python_code import news

def test_news___init__():
    assert news.__init__(news('', '\x00'), '\x00\x00', '') == None


from python_code import teacher

def test_teacher___init__():
    assert teacher.__init__(teacher(0, '\x00'), 0, '\x00') == None


from python_code import user

def test_user___init__():
    assert user.__init__(user(0, '\x00'), 0, '\x00') == None

