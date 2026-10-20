from python_code import trace_EClass
from python_code import trace_EPackage
from python_code import trace_Trace

def test_trace_Trace___init__():
    assert trace_Trace.__init__(trace_Trace(trace_Trace=trace_EPackage(), trace_Trace2=trace_EPackage(), trace_Trace5=trace_EClass(), trace_Trace7=trace_EClass(), trace_Trace10=set(), trace_Trace12=set(), trace_Trace14=set()), trace_Trace=trace_EPackage(), trace_Trace2=trace_EPackage(), trace_Trace5=trace_EClass(), trace_Trace7=trace_EClass(), trace_Trace10=set(), trace_Trace12=set(), trace_Trace14=set()) == None

def test_trace_Trace_addClassMapping():
    assert trace_Trace.addClassMapping(trace_Trace(trace_Trace=trace_EPackage(), trace_Trace2=trace_EPackage(), trace_Trace5=trace_EClass(), trace_Trace7=trace_EClass(), trace_Trace10=set(), trace_Trace12=set(), trace_Trace14=set()), '\x00', '') == None

def test_trace_Trace_addAttributeMapping():
    assert trace_Trace.addAttributeMapping(trace_Trace(trace_Trace=trace_EPackage(), trace_Trace2=trace_EPackage(), trace_Trace5=trace_EClass(), trace_Trace7=trace_EClass(), trace_Trace10=set(), trace_Trace12=set(), trace_Trace14=set()), '\x00', '') == None

def test_trace_Trace_addReferenceMapping():
    assert trace_Trace.addReferenceMapping(trace_Trace(trace_Trace=trace_EPackage(), trace_Trace2=trace_EPackage(), trace_Trace5=trace_EClass(), trace_Trace7=trace_EClass(), trace_Trace10=set(), trace_Trace12=set(), trace_Trace14=set()), '\x00', '', '') == None

