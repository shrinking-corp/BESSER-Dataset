import datetime as _ch_datetime
from python_code import lobj_LearningObject

def test_lobj_LearningObject___init__():
    assert lobj_LearningObject.__init__(lobj_LearningObject('', _ch_datetime.date(1, 1, 2), False), '\x00\x00', _ch_datetime.date(1, 1, 1), False) == None

