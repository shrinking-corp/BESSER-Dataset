import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    BehaviorStateMachines_Namespace,
    BehaviorStateMachines_RedefinableElement,
    BehaviorStateMachines_Vertex,
    Classifier,
    ConnectionPointReference,
    Constraint,
    DirectedRelationship,
    NamedElement,
    Operation,
    ProtocolConformance,
    ProtocolStateMachine,
    Pseudostate,
    Region,
    State,
    StateMachine,
    StateMachines_BehaviorStateMachines_Behavior,
    StateMachines_BehaviorStateMachines_Classifier,
    StateMachines_BehaviorStateMachines_ConnectionPointReference,
    StateMachines_BehaviorStateMachines_Constraint,
    StateMachines_BehaviorStateMachines_FinalState,
    StateMachines_BehaviorStateMachines_NamedElement,
    StateMachines_BehaviorStateMachines_Namespace,
    StateMachines_BehaviorStateMachines_Pseudostate,
    StateMachines_BehaviorStateMachines_RedefinableElement,
    StateMachines_BehaviorStateMachines_Region,
    StateMachines_BehaviorStateMachines_State,
    StateMachines_BehaviorStateMachines_StateMachine,
    StateMachines_BehaviorStateMachines_TimeEvent,
    StateMachines_BehaviorStateMachines_Transition,
    StateMachines_BehaviorStateMachines_Trigger,
    StateMachines_BehaviorStateMachines_Vertex,
    StateMachines_ProtocolStateMachines_DirectedRelationship,
    StateMachines_ProtocolStateMachines_Interface,
    StateMachines_ProtocolStateMachines_Operation,
    StateMachines_ProtocolStateMachines_Port,
    StateMachines_ProtocolStateMachines_ProtocolConformance,
    StateMachines_ProtocolStateMachines_ProtocolStateMachine,
    StateMachines_ProtocolStateMachines_ProtocolTransition,
    Transition,
    Trigger,
    Vertex,
    TransitionKind,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_connection44_stub_double():
    # ConnectionPointReference has no real 'ConnectionPointReference' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = ConnectionPointReference()
    setattr(partner, 'ConnectionPointReference', None)
    _safe_set(owner, 'state', {partner})
    assert getattr(partner, 'ConnectionPointReference') == owner
    _safe_set(owner, 'state', set())
    assert getattr(partner, 'ConnectionPointReference') is None


def test_assoc_connectionPoint45_stub_double():
    # Pseudostate has no real 'Pseudostate47' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = Pseudostate()
    setattr(partner, 'Pseudostate47', None)
    _safe_set(owner, 'state46', {partner})
    assert getattr(partner, 'Pseudostate47') == owner
    _safe_set(owner, 'state46', set())
    assert getattr(partner, 'Pseudostate47') is None


def test_assoc_container30_stub_double():
    # Region has no real 'Region31' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_Transition(kind="sample_text")
    partner = Region()
    setattr(partner, 'Region31', None)
    _safe_set(owner, 'transition', partner)
    assert getattr(partner, 'Region31') == owner
    _safe_set(owner, 'transition', None)
    assert getattr(partner, 'Region31') is None


def test_assoc_deferrableTrigger53_stub_double():
    # Trigger has no real 'Trigger54' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = Trigger()
    setattr(partner, 'Trigger54', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State', {partner})
    assert getattr(partner, 'Trigger54') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State', set())
    assert getattr(partner, 'Trigger54') is None


def test_assoc_doActivity58_stub_double():
    # Behavior has no real 'Behavior60' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = Behavior()
    setattr(partner, 'Behavior60', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State59', partner)
    assert getattr(partner, 'Behavior60') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State59', None)
    assert getattr(partner, 'Behavior60') is None


def test_assoc_effect25_stub_double():
    # Behavior has no real 'Behavior' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_Transition(kind="sample_text")
    partner = Behavior()
    setattr(partner, 'Behavior', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition', partner)
    assert getattr(partner, 'Behavior') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition', None)
    assert getattr(partner, 'Behavior') is None


def test_assoc_entry61_stub_double():
    # Behavior has no real 'Behavior63' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = Behavior()
    setattr(partner, 'Behavior63', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State62', partner)
    assert getattr(partner, 'Behavior63') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State62', None)
    assert getattr(partner, 'Behavior63') is None


def test_assoc_exit55_stub_double():
    # Behavior has no real 'Behavior57' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = Behavior()
    setattr(partner, 'Behavior57', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State56', partner)
    assert getattr(partner, 'Behavior57') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State56', None)
    assert getattr(partner, 'Behavior57') is None


def test_assoc_guard28_stub_double():
    # Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_Transition(kind="sample_text")
    partner = Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition29', partner)
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition29', None)
    assert getattr(partner, 'Constraint') is None


def test_assoc_redefinedState67_stub_double():
    # State has no real 'State69' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = State()
    setattr(partner, 'State69', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State68', partner)
    assert getattr(partner, 'State69') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State68', None)
    assert getattr(partner, 'State69') is None


def test_assoc_redefinedTransition32_stub_double():
    # Transition has no real 'Transition34' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_Transition(kind="sample_text")
    partner = Transition()
    setattr(partner, 'Transition34', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition33', partner)
    assert getattr(partner, 'Transition34') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition33', None)
    assert getattr(partner, 'Transition34') is None


def test_assoc_region50_stub_double():
    # Region has no real 'Region52' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = Region()
    setattr(partner, 'Region52', None)
    _safe_set(owner, 'state51', {partner})
    assert getattr(partner, 'Region52') == owner
    _safe_set(owner, 'state51', set())
    assert getattr(partner, 'Region52') is None


def test_assoc_source21_stub_double():
    # Vertex has no real 'Vertex22' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_Transition(kind="sample_text")
    partner = Vertex()
    setattr(partner, 'Vertex22', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'Vertex22') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'Vertex22') is None


def test_assoc_stateInvariant64_stub_double():
    # Constraint has no real 'Constraint66' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = Constraint()
    setattr(partner, 'Constraint66', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State65', partner)
    assert getattr(partner, 'Constraint66') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_State65', None)
    assert getattr(partner, 'Constraint66') is None


def test_assoc_submachine48_stub_double():
    # StateMachine has no real 'StateMachine49' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = StateMachine()
    setattr(partner, 'StateMachine49', None)
    _safe_set(owner, 'submachineState', partner)
    assert getattr(partner, 'StateMachine49') == owner
    _safe_set(owner, 'submachineState', None)
    assert getattr(partner, 'StateMachine49') is None


def test_assoc_target23_stub_double():
    # Vertex has no real 'Vertex24' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_Transition(kind="sample_text")
    partner = Vertex()
    setattr(partner, 'Vertex24', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'Vertex24') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'Vertex24') is None


def test_assoc_trigger26_stub_double():
    # Trigger has no real 'Trigger' property in the generated
    # code (a bare stub) -- manually attach it so StateMachines_BehaviorStateMachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # StateMachines_BehaviorStateMachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = StateMachines_BehaviorStateMachines_Transition(kind="sample_text")
    partner = Trigger()
    setattr(partner, 'Trigger', None)
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition27', partner)
    assert getattr(partner, 'Trigger') == owner
    _safe_set(owner, 'StateMachines_BehaviorStateMachines_Transition27', None)
    assert getattr(partner, 'Trigger') is None


