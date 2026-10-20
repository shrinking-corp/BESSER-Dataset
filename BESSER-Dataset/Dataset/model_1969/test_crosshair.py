from python_code import trace_M2CTraceItem

def test_trace_M2CTraceItem___init__():
    assert trace_M2CTraceItem.__init__(trace_M2CTraceItem('', '\x00'), '\x00\x00', '') == None


from python_code import trace_TraceBySource
from python_code import trace_TraceItem
from python_code import trace_TraceList

def test_trace_TraceItem___init__():
    assert trace_TraceItem.__init__(trace_TraceItem('', trace_TraceItem=trace_TraceList(), trace_TraceItem6=set(), trace_TraceItem12=trace_TraceBySource()), '', trace_TraceItem=trace_TraceList(), trace_TraceItem6=set(), trace_TraceItem12=trace_TraceBySource()) == None

