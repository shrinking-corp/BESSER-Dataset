from python_code import statemachines_BooleanAttribute
from python_code import statemachines_BooleanAttributeValue

def test_statemachines_BooleanAttributeValue___init__():
    assert statemachines_BooleanAttributeValue.__init__(statemachines_BooleanAttributeValue('', statemachines_BooleanAttributeValue=statemachines_BooleanAttribute()), '', statemachines_BooleanAttributeValue=statemachines_BooleanAttribute()) == None


from python_code import statemachines_Constraint

def test_statemachines_Constraint___init__():
    assert statemachines_Constraint.__init__(statemachines_Constraint(''), '') == None


from python_code import statemachines_IntegerAttribute
from python_code import statemachines_IntegerAttributeValue

def test_statemachines_IntegerAttributeValue___init__():
    assert statemachines_IntegerAttributeValue.__init__(statemachines_IntegerAttributeValue('', statemachines_IntegerAttributeValue=statemachines_IntegerAttribute()), '', statemachines_IntegerAttributeValue=statemachines_IntegerAttribute()) == None


from python_code import statemachines_NamedElement

def test_statemachines_NamedElement___init__():
    assert statemachines_NamedElement.__init__(statemachines_NamedElement(''), '') == None


from python_code import statemachines_CustomSystem
from python_code import statemachines_Region
from python_code import statemachines_StateMachine

def test_statemachines_StateMachine___init__():
    assert statemachines_StateMachine.__init__(statemachines_StateMachine(statemachines_StateMachine=statemachines_CustomSystem(), stateMachine=set(), StateMachine=statemachines_Region()), statemachines_StateMachine=statemachines_CustomSystem(), stateMachine=set(), StateMachine=statemachines_Region()) == None

def test_statemachines_StateMachine_run():
    assert statemachines_StateMachine.run(statemachines_StateMachine(statemachines_StateMachine=statemachines_CustomSystem(), stateMachine=set(), StateMachine=statemachines_Region())) == None

def test_statemachines_StateMachine_eventOccurrenceReceived():
    assert statemachines_StateMachine.eventOccurrenceReceived(statemachines_StateMachine(statemachines_StateMachine=statemachines_CustomSystem(), stateMachine=set(), StateMachine=statemachines_Region()), 0) == None


from python_code import statemachines_StringAttribute
from python_code import statemachines_StringAttributeValue

def test_statemachines_StringAttributeValue___init__():
    assert statemachines_StringAttributeValue.__init__(statemachines_StringAttributeValue('', statemachines_StringAttributeValue=statemachines_StringAttribute()), '', statemachines_StringAttributeValue=statemachines_StringAttribute()) == None


from python_code import statemachines_Behavior
from python_code import statemachines_Region
from python_code import statemachines_Transition
from python_code import statemachines_Vertex

def test_statemachines_Transition___init__():
    assert statemachines_Transition.__init__(statemachines_Transition('', Transition=statemachines_Region(), Transition31=statemachines_Vertex(), Transition33=statemachines_Vertex(), outgoingTransitions=statemachines_Vertex(), incomingTransitions=statemachines_Vertex(), statemachines_Transition=set(), transitions=statemachines_Region(), statemachines_Transition58=statemachines_Behavior()), '', Transition=statemachines_Region(), Transition31=statemachines_Vertex(), Transition33=statemachines_Vertex(), outgoingTransitions=statemachines_Vertex(), incomingTransitions=statemachines_Vertex(), statemachines_Transition=set(), transitions=statemachines_Region(), statemachines_Transition58=statemachines_Behavior()) == None

def test_statemachines_Transition_fire():
    assert statemachines_Transition.fire(statemachines_Transition('', Transition=statemachines_Region(), Transition31=statemachines_Vertex(), Transition33=statemachines_Vertex(), outgoingTransitions=statemachines_Vertex(), incomingTransitions=statemachines_Vertex(), statemachines_Transition=set(), transitions=statemachines_Region(), statemachines_Transition58=statemachines_Behavior()), '') == None

