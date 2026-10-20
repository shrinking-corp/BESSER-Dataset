from python_code import viewmodeltrace_JavaObjectMatchArgument

def test_viewmodeltrace_JavaObjectMatchArgument___init__():
    assert viewmodeltrace_JavaObjectMatchArgument.__init__(viewmodeltrace_JavaObjectMatchArgument(''), '') == None


from python_code import viewmodeltrace_MatchArgument
from python_code import viewmodeltrace_MatchArgumentTuple

def test_viewmodeltrace_MatchArgument___init__():
    assert viewmodeltrace_MatchArgument.__init__(viewmodeltrace_MatchArgument('', viewmodeltrace_MatchArgument=viewmodeltrace_MatchArgumentTuple()), '', viewmodeltrace_MatchArgument=viewmodeltrace_MatchArgumentTuple()) == None


from python_code import viewmodeltrace_StringVariablePair
from python_code import viewmodeltrace_Variable
from python_code import viewmodeltrace_VariableInstantiationTrace

def test_viewmodeltrace_StringVariablePair___init__():
    assert viewmodeltrace_StringVariablePair.__init__(viewmodeltrace_StringVariablePair('', viewmodeltrace_StringVariablePair=viewmodeltrace_VariableInstantiationTrace(), viewmodeltrace_StringVariablePair10=viewmodeltrace_Variable()), '', viewmodeltrace_StringVariablePair=viewmodeltrace_VariableInstantiationTrace(), viewmodeltrace_StringVariablePair10=viewmodeltrace_Variable()) == None


from python_code import viewmodeltrace_LogicModel
from python_code import viewmodeltrace_ViewModelTrace

def test_viewmodeltrace_ViewModelTrace___init__():
    assert viewmodeltrace_ViewModelTrace.__init__(viewmodeltrace_ViewModelTrace('', viewmodeltrace_ViewModelTrace=viewmodeltrace_LogicModel(), viewmodeltrace_ViewModelTrace2=set()), '', viewmodeltrace_ViewModelTrace=viewmodeltrace_LogicModel(), viewmodeltrace_ViewModelTrace2=set()) == None

