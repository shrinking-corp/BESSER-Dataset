from python_code import EventAutomatonModel_ConstantBinding
from python_code import EventAutomatonModel_Event
from python_code import EventAutomatonModel_FixParameter

def test_EventAutomatonModel_FixParameter___init__():
    assert EventAutomatonModel_FixParameter.__init__(EventAutomatonModel_FixParameter('', EventAutomatonModel_FixParameter=EventAutomatonModel_ConstantBinding(), EventAutomatonModel_FixParameter36=EventAutomatonModel_Event()), '', EventAutomatonModel_FixParameter=EventAutomatonModel_ConstantBinding(), EventAutomatonModel_FixParameter36=EventAutomatonModel_Event()) == None


from python_code import EventAutomatonModel_FreeParameter

def test_EventAutomatonModel_FreeParameter___init__():
    assert EventAutomatonModel_FreeParameter.__init__(EventAutomatonModel_FreeParameter(''), '') == None


from python_code import EventAutomatonModel_SetTimerAction

def test_EventAutomatonModel_SetTimerAction___init__():
    assert EventAutomatonModel_SetTimerAction.__init__(EventAutomatonModel_SetTimerAction(0), 0) == None


from python_code import EventAutomatonModel_ComplexEventProcessor
from python_code import EventAutomatonModel_SymbolicInputEvent

def test_EventAutomatonModel_SymbolicInputEvent___init__():
    assert EventAutomatonModel_SymbolicInputEvent.__init__(EventAutomatonModel_SymbolicInputEvent('', EventAutomatonModel_SymbolicInputEvent=EventAutomatonModel_ComplexEventProcessor()), '', EventAutomatonModel_SymbolicInputEvent=EventAutomatonModel_ComplexEventProcessor()) == None

