from python_code import trace_EObject
from python_code import trace_OutputFile
from python_code import trace_Trace

def test_trace_OutputFile___init__():
    assert trace_OutputFile.__init__(trace_OutputFile('\x00\x00', '', trace_OutputFile=trace_Trace(), trace_OutputFile2=set(), trace_OutputFile4=trace_EObject()), '', '', trace_OutputFile=trace_Trace(), trace_OutputFile2=set(), trace_OutputFile4=trace_EObject()) == None

