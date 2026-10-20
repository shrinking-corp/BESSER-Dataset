import datetime as _ch_datetime
from python_code import ChangingOverTime_TimeStampedElement

def test_ChangingOverTime_TimeStampedElement___init__():
    assert ChangingOverTime_TimeStampedElement.__init__(ChangingOverTime_TimeStampedElement(_ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1)), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1)) == None

