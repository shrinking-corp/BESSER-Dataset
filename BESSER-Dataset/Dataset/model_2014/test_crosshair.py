from python_code import trace_CompositParameterList

def test_trace_CompositParameterList___init__():
    assert trace_CompositParameterList.__init__(trace_CompositParameterList(0, trace_CompositParameterList=set()), 0, trace_CompositParameterList=set()) == None


from python_code import trace_CompositeObjectState

def test_trace_CompositeObjectState___init__():
    assert trace_CompositeObjectState.__init__(trace_CompositeObjectState(0, trace_CompositeObjectState=set()), 0, trace_CompositeObjectState=set()) == None


from python_code import trace_LiteralBoolean

def test_trace_LiteralBoolean___init__():
    assert trace_LiteralBoolean.__init__(trace_LiteralBoolean(True), False) == None


from python_code import trace_LiteralFloat

def test_trace_LiteralFloat___init__():
    assert trace_LiteralFloat.__init__(trace_LiteralFloat(0.0), 0.0) == None


from python_code import trace_LiteralInteger

def test_trace_LiteralInteger___init__():
    assert trace_LiteralInteger.__init__(trace_LiteralInteger(0), 0) == None


from python_code import trace_LiteralString

def test_trace_LiteralString___init__():
    assert trace_LiteralString.__init__(trace_LiteralString(''), '') == None


from python_code import trace_ParameterList
from python_code import trace_ParameterValue
from python_code import trace_Trace

def test_trace_ParameterValue___init__():
    assert trace_ParameterValue.__init__(trace_ParameterValue('', trace_ParameterValue68=set(), trace_ParameterValue87=trace_ParameterList(), trace_ParameterValue=trace_Trace()), '', trace_ParameterValue68=set(), trace_ParameterValue87=trace_ParameterList(), trace_ParameterValue=trace_Trace()) == None


from python_code import trace_PatternOcurrence
from python_code import trace_StepPattern

def test_trace_PatternOcurrence___init__():
    assert trace_PatternOcurrence.__init__(trace_PatternOcurrence(0, trace_PatternOcurrence=trace_StepPattern(), trace_PatternOcurrence45=set()), 0, trace_PatternOcurrence=trace_StepPattern(), trace_PatternOcurrence45=set()) == None


from python_code import trace_StepSpec
from python_code import trace_StepType
from python_code import trace_Trace

def test_trace_StepType___init__():
    assert trace_StepType.__init__(trace_StepType('', trace_StepType=trace_Trace(), trace_StepType59=trace_StepSpec()), '', trace_StepType=trace_Trace(), trace_StepType59=trace_StepSpec()) == None

