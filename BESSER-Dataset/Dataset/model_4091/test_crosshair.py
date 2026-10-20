from python_code import StateMachine
from python_code import statemachines_CustomSystem

def test_statemachines_CustomSystem___init__():
    assert statemachines_CustomSystem.__init__(statemachines_CustomSystem(statemachines_CustomSystem2=set(), statemachines_CustomSystem=StateMachine()), statemachines_CustomSystem2=set(), statemachines_CustomSystem=StateMachine()) == None

def test_statemachines_CustomSystem_initialize():
    assert statemachines_CustomSystem.initialize(statemachines_CustomSystem(statemachines_CustomSystem2=set(), statemachines_CustomSystem=StateMachine()), 0) == None

def test_statemachines_CustomSystem_main():
    assert statemachines_CustomSystem.main(statemachines_CustomSystem(statemachines_CustomSystem2=set(), statemachines_CustomSystem=StateMachine())) == None


from python_code import statemachines_Util

def test_statemachines_Util___init__():
    assert statemachines_Util.__init__(statemachines_Util()) == None

def test_statemachines_Util_log():
    assert statemachines_Util.log(statemachines_Util(), '') == None


from python_code import State
from python_code import StateMachine
from python_code import statemachines_almostuml_FinalState
from python_code import statemachines_almostuml_Region

def test_statemachines_almostuml_FinalState___init__():
    assert statemachines_almostuml_FinalState.__init__(statemachines_almostuml_FinalState(State=statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State())), State=statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State())) == None

def test_statemachines_almostuml_FinalState_handle():
    assert statemachines_almostuml_FinalState.handle(statemachines_almostuml_FinalState(State=statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State())), '\x00\x00') == None


from python_code import statemachines_almostuml_NamedElement

def test_statemachines_almostuml_NamedElement___init__():
    assert statemachines_almostuml_NamedElement.__init__(statemachines_almostuml_NamedElement(''), '') == None


from python_code import State
from python_code import StateMachine
from python_code import statemachines_almostuml_Pseudostate
from python_code import statemachines_almostuml_Region

def test_statemachines_almostuml_Pseudostate___init__():
    assert statemachines_almostuml_Pseudostate.__init__(statemachines_almostuml_Pseudostate('', State=statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State())), '', State=statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State())) == None


from python_code import State
from python_code import StateMachine
from python_code import statemachines_almostuml_Region

def test_statemachines_almostuml_Region___init__():
    assert statemachines_almostuml_Region.__init__(statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State()), container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State()) == None

def test_statemachines_almostuml_Region_handleEvent():
    assert statemachines_almostuml_Region.handleEvent(statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State()), '\x00\x00') == None

def test_statemachines_almostuml_Region_initialize():
    assert statemachines_almostuml_Region.initialize(statemachines_almostuml_Region(container=set(), statemachines_almostuml_Region=set(), region=StateMachine(), statemachines_almostuml_Region12=State())) == None


from python_code import Behavior
from python_code import statemachines_almostuml_State

def test_statemachines_almostuml_State___init__():
    assert statemachines_almostuml_State.__init__(statemachines_almostuml_State(statemachines_almostuml_State=Behavior(), statemachines_almostuml_State15=Behavior(), statemachines_almostuml_State18=Behavior(), statemachines_almostuml_State21=set()), statemachines_almostuml_State=Behavior(), statemachines_almostuml_State15=Behavior(), statemachines_almostuml_State18=Behavior(), statemachines_almostuml_State21=set()) == None

def test_statemachines_almostuml_State_handle():
    assert statemachines_almostuml_State.handle(statemachines_almostuml_State(statemachines_almostuml_State=Behavior(), statemachines_almostuml_State15=Behavior(), statemachines_almostuml_State18=Behavior(), statemachines_almostuml_State21=set()), 0) == None

def test_statemachines_almostuml_State_setAsCurrent():
    assert statemachines_almostuml_State.setAsCurrent(statemachines_almostuml_State(statemachines_almostuml_State=Behavior(), statemachines_almostuml_State15=Behavior(), statemachines_almostuml_State18=Behavior(), statemachines_almostuml_State21=set())) == None


from python_code import statemachines_almostuml_StateMachine

def test_statemachines_almostuml_StateMachine___init__():
    assert statemachines_almostuml_StateMachine.__init__(statemachines_almostuml_StateMachine(stateMachine=set(), statemachines_almostuml_StateMachine=set()), stateMachine=set(), statemachines_almostuml_StateMachine=set()) == None

def test_statemachines_almostuml_StateMachine_run():
    assert statemachines_almostuml_StateMachine.run(statemachines_almostuml_StateMachine(stateMachine=set(), statemachines_almostuml_StateMachine=set())) == None


from python_code import Behavior
from python_code import Constraint
from python_code import Vertex
from python_code import statemachines_almostuml_Transition

def test_statemachines_almostuml_Transition___init__():
    assert statemachines_almostuml_Transition.__init__(statemachines_almostuml_Transition(statemachines_almostuml_Transition=Vertex(), statemachines_almostuml_Transition28=Vertex(), statemachines_almostuml_Transition31=set(), statemachines_almostuml_Transition33=Constraint(), statemachines_almostuml_Transition35=Behavior()), statemachines_almostuml_Transition=Vertex(), statemachines_almostuml_Transition28=Vertex(), statemachines_almostuml_Transition31=set(), statemachines_almostuml_Transition33=Constraint(), statemachines_almostuml_Transition35=Behavior()) == None

def test_statemachines_almostuml_Transition_fire():
    assert statemachines_almostuml_Transition.fire(statemachines_almostuml_Transition(statemachines_almostuml_Transition=Vertex(), statemachines_almostuml_Transition28=Vertex(), statemachines_almostuml_Transition31=set(), statemachines_almostuml_Transition33=Constraint(), statemachines_almostuml_Transition35=Behavior())) == None

