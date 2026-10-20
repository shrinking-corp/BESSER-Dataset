from python_code import trace_EReference
from python_code import trace_EStructuralFeature
from python_code import trace_ReferenceMapping
from python_code import trace_Trace

def test_trace_ReferenceMapping___init__():
    assert trace_ReferenceMapping.__init__(trace_ReferenceMapping('', trace_ReferenceMapping16=trace_EReference(), trace_ReferenceMapping18=trace_EStructuralFeature(), trace_ReferenceMapping=trace_Trace()), '', trace_ReferenceMapping16=trace_EReference(), trace_ReferenceMapping18=trace_EStructuralFeature(), trace_ReferenceMapping=trace_Trace()) == None

