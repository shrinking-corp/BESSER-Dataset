from python_code import claas1
from python_code import teachers

def test_claas1___init__():
    assert claas1.__init__(claas1(0, '', subject6=set(), student8=set(), teachers1=teachers()), 0, '', subject6=set(), student8=set(), teachers1=teachers()) == None


from python_code import user

def test_user___init__():
    assert user.__init__(user('', '', '\x00\x00'), '', '', '') == None

