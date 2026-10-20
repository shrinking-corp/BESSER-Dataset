from python_code import sgraph_Choice

def test_sgraph_Choice___init__():
    assert sgraph_Choice.__init__(sgraph_Choice(''), '') == None


from python_code import sgraph_Entry

def test_sgraph_Entry___init__():
    assert sgraph_Entry.__init__(sgraph_Entry(''), '') == None


from python_code import sgraph_CompositeElement
from python_code import sgraph_Region
from python_code import sgraph_Vertex

def test_sgraph_Region___init__():
    assert sgraph_Region.__init__(sgraph_Region(0, Region=sgraph_Vertex(), parentRegion=set(), regions=sgraph_CompositeElement(), Region27=sgraph_CompositeElement()), 0, Region=sgraph_Vertex(), parentRegion=set(), regions=sgraph_CompositeElement(), Region27=sgraph_CompositeElement()) == None


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


from python_code import sgraph_Transition
from python_code import sgraph_Vertex

def test_sgraph_Transition___init__():
    assert sgraph_Transition.__init__(sgraph_Transition(0, Transition=sgraph_Vertex(), Transition3=sgraph_Vertex(), incomingTransitions=sgraph_Vertex(), outgoingTransitions=sgraph_Vertex()), 0, Transition=sgraph_Vertex(), Transition3=sgraph_Vertex(), incomingTransitions=sgraph_Vertex(), outgoingTransitions=sgraph_Vertex()) == None

