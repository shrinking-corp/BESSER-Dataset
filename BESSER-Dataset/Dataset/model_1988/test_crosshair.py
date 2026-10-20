from python_code import trace_BoolAny

def test_trace_BoolAny___init__():
    assert trace_BoolAny.__init__(trace_BoolAny(True), False) == None


from python_code import trace_DecimalAny

def test_trace_DecimalAny___init__():
    assert trace_DecimalAny.__init__(trace_DecimalAny(''), '') == None


from python_code import trace_IntAny

def test_trace_IntAny___init__():
    assert trace_IntAny.__init__(trace_IntAny(''), '') == None


from python_code import trace_StringAny

def test_trace_StringAny___init__():
    assert trace_StringAny.__init__(trace_StringAny(''), '') == None


from python_code import trace_EObject
from python_code import trace_Trace

def test_trace_Trace___init__():
    assert trace_Trace.__init__(trace_Trace('', trace_Trace=set(), trace_Trace2=trace_EObject(), trace_Trace4=set()), '', trace_Trace=set(), trace_Trace2=trace_EObject(), trace_Trace4=set()) == None

