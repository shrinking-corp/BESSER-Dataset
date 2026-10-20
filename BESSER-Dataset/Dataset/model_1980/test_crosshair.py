from python_code import MRPTrace_NamedElement

def test_MRPTrace_NamedElement___init__():
    assert MRPTrace_NamedElement.__init__(MRPTrace_NamedElement(''), '') == None


from python_code import MRPTrace_Trace
from python_code import MRPTrace_TraceModel

def test_MRPTrace_Trace___init__():
    assert MRPTrace_Trace.__init__(MRPTrace_Trace('', MRPTrace_Trace=MRPTrace_TraceModel(), MRPTrace_Trace2=set()), '', MRPTrace_Trace=MRPTrace_TraceModel(), MRPTrace_Trace2=set()) == None

