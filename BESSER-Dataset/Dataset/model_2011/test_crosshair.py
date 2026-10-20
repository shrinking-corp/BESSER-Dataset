import datetime as _ch_datetime
from python_code import trace_Log
from python_code import trace_Trace

def test_trace_Log___init__():
    assert trace_Log.__init__(trace_Log('', '', '', _ch_datetime.date(1, 1, 1), trace_Log2=set(), trace_Log=trace_Trace()), '', '', '', _ch_datetime.date(1, 1, 1), trace_Log2=set(), trace_Log=trace_Trace()) == None

