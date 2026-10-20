import datetime as _ch_datetime
from python_code import types_ManyTypes

def test_types_ManyTypes___init__():
    assert types_ManyTypes.__init__(types_ManyTypes('', '', '', '', '', '', '\x00', '', '', '', '', '', '', '', _ch_datetime.date(1, 1, 1)), '', '', '', '', '', '', '', '\x00', '', '', '', '', '', '', _ch_datetime.date(1, 1, 1)) == None


import datetime as _ch_datetime
from python_code import types_SingleTypes

def test_types_SingleTypes___init__():
    assert types_SingleTypes.__init__(types_SingleTypes('', '', float('inf'), '', 0.0, '', '', '', '', '', '', '', '', '', '', _ch_datetime.date(1, 1, 1), '', 0, '\x01', '', '', ''), '', '', 0.0, '', 0.0, '', '', '', '', '', '', '', '', '', '', _ch_datetime.date(1, 1, 1), '', 0, '', '', '', '') == None

