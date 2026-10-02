from python_code import department

def test_department___init__():
    assert department.__init__(department('\x00\x00', '', '', ''), '', '', '', '') == None

from python_code import students

def test_students___init__():
    assert students.__init__(students('\x00\x00', '', datetime.date(1, 1, 1), '', ''), '', '', datetime.date(1, 1, 1), '', '') == None

from python_code import subject

def test_subject___init__():
    assert subject.__init__(subject('', '\x00'), '\x00\x00', '') == None
