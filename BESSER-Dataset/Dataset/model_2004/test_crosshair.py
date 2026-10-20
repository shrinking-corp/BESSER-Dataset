from python_code import trace_Trace
from python_code import trace_TraceElement

def test_trace_TraceElement___init__():
    assert trace_TraceElement.__init__(trace_TraceElement('', 0, trace_TraceElement=trace_Trace()), '', 0, trace_TraceElement=trace_Trace()) == None

