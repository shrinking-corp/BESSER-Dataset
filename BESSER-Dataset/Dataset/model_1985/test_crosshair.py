from python_code import trace_EObject
from python_code import trace_Trace

def test_trace_Trace___init__():
    assert trace_Trace.__init__(trace_Trace(trace_Trace=set(), trace_Trace2=trace_EObject(), trace_Trace4=trace_EObject()), trace_Trace=set(), trace_Trace2=trace_EObject(), trace_Trace4=trace_EObject()) == None

def test_trace_Trace_getAllMappedObjects():
    assert trace_Trace.getAllMappedObjects(trace_Trace(trace_Trace=set(), trace_Trace2=trace_EObject(), trace_Trace4=trace_EObject())) == None
