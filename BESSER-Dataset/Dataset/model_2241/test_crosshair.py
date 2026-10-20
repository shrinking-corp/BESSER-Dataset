import datetime as _ch_datetime
from python_code import coursePages_CourseWork
from python_code import coursePages_CourseWorkObject

def test_coursePages_CourseWorkObject___init__():
    assert coursePages_CourseWorkObject.__init__(coursePages_CourseWorkObject('', '', '\x00\x00', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), coursePages_CourseWorkObject=coursePages_CourseWork()), '', '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), coursePages_CourseWorkObject=coursePages_CourseWork()) == None


import datetime as _ch_datetime
from python_code import coursePages_EvaluationObject
from python_code import coursePages_Evaluations

def test_coursePages_EvaluationObject___init__():
    assert coursePages_EvaluationObject.__init__(coursePages_EvaluationObject('', '', 0, _ch_datetime.date(1, 1, 2), coursePages_EvaluationObject=coursePages_Evaluations()), '', '', 0, _ch_datetime.date(1, 1, 1), coursePages_EvaluationObject=coursePages_Evaluations()) == None


from python_code import coursePages_Person

def test_coursePages_Person___init__():
    assert coursePages_Person.__init__(coursePages_Person('\x00\x00', '', '', ''), '', '', '', '') == None

