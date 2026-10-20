from python_code import trace_Trace
from python_code import trace_TraceLink

def test_trace_TraceLink___init__():
    assert trace_TraceLink.__init__(trace_TraceLink('', trace_TraceLink=trace_Trace(), trace_TraceLink2=set(), trace_TraceLink4=set()), '', trace_TraceLink=trace_Trace(), trace_TraceLink2=set(), trace_TraceLink4=set()) == None

