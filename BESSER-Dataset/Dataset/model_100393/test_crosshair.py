from python_code import sgraph_Choice

def test_sgraph_Choice___init__():
    assert sgraph_Choice.__init__(sgraph_Choice(''), '') == None


from python_code import sgraph_Entry

def test_sgraph_Entry___init__():
    assert sgraph_Entry.__init__(sgraph_Entry(''), '') == None


from python_code import sgraph_ExpressionElement

def test_sgraph_ExpressionElement___init__():
    assert sgraph_ExpressionElement.__init__(sgraph_ExpressionElement(''), '') == None


from python_code import sgraph_NamedElement

def test_sgraph_NamedElement___init__():
    assert sgraph_NamedElement.__init__(sgraph_NamedElement(''), '') == None


from python_code import sgraph_ScopedElement

def test_sgraph_ScopedElement___init__():
    assert sgraph_ScopedElement.__init__(sgraph_ScopedElement('', sgraph_ScopedElement=set()), '', sgraph_ScopedElement=set()) == None


from python_code import sgraph_State
from python_code import sgraph_Statechart

def test_sgraph_State___init__():
    assert sgraph_State.__init__(sgraph_State(False, '\x00', False, False, True, False, sgraph_State=set(), sgraph_State28=sgraph_Statechart()), True, '', False, False, False, False, sgraph_State=set(), sgraph_State28=sgraph_Statechart()) == None


from python_code import sgraph_Transition
from python_code import sgraph_Vertex

def test_sgraph_Transition___init__():
    assert sgraph_Transition.__init__(sgraph_Transition(0, Transition=sgraph_Vertex(), Transition3=sgraph_Vertex(), incomingTransitions=sgraph_Vertex(), outgoingTransitions=sgraph_Vertex()), 0, Transition=sgraph_Vertex(), Transition3=sgraph_Vertex(), incomingTransitions=sgraph_Vertex(), outgoingTransitions=sgraph_Vertex()) == None

