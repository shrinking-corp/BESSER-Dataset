from python_code import classrooms

def test_classrooms___init__():
    assert classrooms.__init__(classrooms(0, '', '\x00\x00'), 0, '', '') == None


from python_code import conflictCheck

def test_conflictCheck___init__():
    assert conflictCheck.__init__(conflictCheck(False, '\x00'), False, '\x00') == None


from python_code import constraints
from python_code import subjects

def test_constraints___init__():
    assert constraints.__init__(constraints(subjects(0, '', '', ''), subjects(0, '', '\x00', '')), subjects(0, '', '', ''), subjects(0, '', '', '')) == None


from python_code import classrooms
from python_code import leftOuts
from python_code import subjects
from python_code import teachers

def test_leftOuts___init__():
    assert leftOuts.__init__(leftOuts(subjects(0, '', '', ''), classrooms(0, '', ''), teachers('', '', 0, '\x00'), ''), subjects(0, '', '', ''), classrooms(0, '', ''), teachers('', '', 0, ''), '') == None


from python_code import subjects

def test_subjects___init__():
    assert subjects.__init__(subjects(0, '\x00', '', ''), 0, '', '', '') == None


from python_code import teachers

def test_teachers___init__():
    assert teachers.__init__(teachers('\x00\x00', '', 0, ''), '', '', 0, '') == None

