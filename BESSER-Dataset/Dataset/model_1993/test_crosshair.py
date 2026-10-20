from python_code import MappingOperation
from python_code import trace_EMappingOperation
from python_code import trace_TraceRecord

def test_trace_EMappingOperation___init__():
    assert trace_EMappingOperation.__init__(trace_EMappingOperation('', '', '\x00\x00', trace_EMappingOperation=trace_TraceRecord(), trace_EMappingOperation23=MappingOperation()), '', '', '', trace_EMappingOperation=trace_TraceRecord(), trace_EMappingOperation23=MappingOperation()) == None

