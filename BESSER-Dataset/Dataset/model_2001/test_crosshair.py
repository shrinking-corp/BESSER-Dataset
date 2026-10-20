from python_code import trace_EObject
from python_code import trace_TraceElement

def test_trace_TraceElement___init__():
    assert trace_TraceElement.__init__(trace_TraceElement('', '\x00', trace_TraceElement=trace_EObject()), '\x00\x00', '', trace_TraceElement=trace_EObject()) == None

