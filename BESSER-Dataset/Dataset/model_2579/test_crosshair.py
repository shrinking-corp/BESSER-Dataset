from python_code import events_AtomicEventPattern

def test_events_AtomicEventPattern___init__():
    assert events_AtomicEventPattern.__init__(events_AtomicEventPattern(''), '') == None


from python_code import events_Multiplicity

def test_events_Multiplicity___init__():
    assert events_Multiplicity.__init__(events_Multiplicity(0), 0) == None


from python_code import events_ComplexEventPattern
from python_code import events_Timewindow

def test_events_Timewindow___init__():
    assert events_Timewindow.__init__(events_Timewindow('', events_Timewindow=events_ComplexEventPattern()), '', events_Timewindow=events_ComplexEventPattern()) == None

