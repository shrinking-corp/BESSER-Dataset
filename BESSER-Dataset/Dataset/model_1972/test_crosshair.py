from python_code import traces_EObject
from python_code import traces_Trace
from python_code import traces_TraceRepository

def test_traces_Trace___init__():
    assert traces_Trace.__init__(traces_Trace('', traces_Trace=traces_EObject(), traces_Trace2=traces_EObject(), traces_Trace5=traces_TraceRepository()), '', traces_Trace=traces_EObject(), traces_Trace2=traces_EObject(), traces_Trace5=traces_TraceRepository()) == None

