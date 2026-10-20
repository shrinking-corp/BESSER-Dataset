import datetime as _ch_datetime
from python_code import timeBasedRouting_DailyOccursModel

def test_timeBasedRouting_DailyOccursModel___init__():
    assert timeBasedRouting_DailyOccursModel.__init__(timeBasedRouting_DailyOccursModel(0, _ch_datetime.date(1, 1, 1)), 0, _ch_datetime.date(1, 1, 2)) == None


import datetime as _ch_datetime
from python_code import timeBasedRouting_MonthlyOccursModel

def test_timeBasedRouting_MonthlyOccursModel___init__():
    assert timeBasedRouting_MonthlyOccursModel.__init__(timeBasedRouting_MonthlyOccursModel(False, 0, 0, '', '', _ch_datetime.date(1, 1, 1)), False, 0, 0, '', '', _ch_datetime.date(1, 1, 1)) == None


from python_code import timeBasedRouting_TimeBasedRouting
from python_code import timeBasedRouting_TimeItem

def test_timeBasedRouting_TimeItem___init__():
    assert timeBasedRouting_TimeItem.__init__(timeBasedRouting_TimeItem('', timeBasedRouting_TimeItem=timeBasedRouting_TimeBasedRouting()), '', timeBasedRouting_TimeItem=timeBasedRouting_TimeBasedRouting()) == None


import datetime as _ch_datetime
from python_code import timeBasedRouting_WeeklyOccursModel

def test_timeBasedRouting_WeeklyOccursModel___init__():
    assert timeBasedRouting_WeeklyOccursModel.__init__(timeBasedRouting_WeeklyOccursModel(0, '\x00', _ch_datetime.date(1, 1, 3)), 0, '', _ch_datetime.date(1, 1, 1)) == None

