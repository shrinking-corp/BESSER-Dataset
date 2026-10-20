from python_code import sgraph_Choice

def test_sgraph_Choice___init__():
    assert sgraph_Choice.__init__(sgraph_Choice(''), '') == None


from python_code import sgraph_Entry

def test_sgraph_Entry___init__():
    assert sgraph_Entry.__init__(sgraph_Entry(''), '') == None


from python_code import sgraph_Import
from python_code import sgraph_Statechart

def test_sgraph_Import___init__():
    assert sgraph_Import.__init__(sgraph_Import('', sgraph_Import=sgraph_Statechart()), '', sgraph_Import=sgraph_Statechart()) == None


from python_code import sgraph_ScopedElement

def test_sgraph_ScopedElement___init__():
    assert sgraph_ScopedElement.__init__(sgraph_ScopedElement('', sgraph_ScopedElement=set()), '', sgraph_ScopedElement=set()) == None


from python_code import sgraph_SpecificationElement

def test_sgraph_SpecificationElement___init__():
    assert sgraph_SpecificationElement.__init__(sgraph_SpecificationElement(''), '') == None


from python_code import sgraph_State
from python_code import sgraph_Statechart

def test_sgraph_State___init__():
    assert sgraph_State.__init__(sgraph_State(False, '', False, True, False, False, sgraph_State=sgraph_Statechart()), False, '', False, False, False, False, sgraph_State=sgraph_Statechart()) == None

