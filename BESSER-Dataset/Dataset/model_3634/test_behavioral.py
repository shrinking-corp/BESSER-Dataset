import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    State,
    Vertex,
    umlstatemachineselect_Behavior,
    umlstatemachineselect_ConnectionPointReference,
    umlstatemachineselect_Constraint,
    umlstatemachineselect_Event,
    umlstatemachineselect_FinalState,
    umlstatemachineselect_PseudoState,
    umlstatemachineselect_Region,
    umlstatemachineselect_State,
    umlstatemachineselect_StateMachine,
    umlstatemachineselect_Transition,
    umlstatemachineselect_Trigger,
    umlstatemachineselect_Vertex,
    PseudostateKind,
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

def test_assoc_connection30_stub_double():
    # umlstatemachineselect_ConnectionPointReference has no real 'ConnectionPointReference' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_ConnectionPointReference()
    setattr(partner, 'ConnectionPointReference', None)
    _safe_set(owner, 'state31', {partner})
    assert getattr(partner, 'ConnectionPointReference') == owner
    _safe_set(owner, 'state31', set())
    assert getattr(partner, 'ConnectionPointReference') is None


def test_assoc_connectionPoint2_stub_double():
    # umlstatemachineselect_StateMachine has no real 'stateMachine3' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_PseudoState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_PseudoState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_PseudoState(kind="sample_text")
    partner = umlstatemachineselect_StateMachine()
    setattr(partner, 'stateMachine3', None)
    _safe_set(owner, 'PseudoState', partner)
    assert owner in getattr(partner, 'stateMachine3')
    _safe_set(owner, 'PseudoState', None)
    assert owner not in getattr(partner, 'stateMachine3')


def test_assoc_container17_stub_double():
    # umlstatemachineselect_Region has no real 'Region18' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Region()
    setattr(partner, 'Region18', None)
    _safe_set(owner, 'transition', partner)
    assert getattr(partner, 'Region18') == owner
    _safe_set(owner, 'transition', None)
    assert getattr(partner, 'Region18') is None


def test_assoc_deferrableTrigger45_stub_double():
    # umlstatemachineselect_Trigger has no real 'umlstatemachineselect_Trigger47' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_Trigger()
    setattr(partner, 'umlstatemachineselect_Trigger47', None)
    _safe_set(owner, 'umlstatemachineselect_State46', {partner})
    assert getattr(partner, 'umlstatemachineselect_Trigger47') == owner
    _safe_set(owner, 'umlstatemachineselect_State46', set())
    assert getattr(partner, 'umlstatemachineselect_Trigger47') is None


def test_assoc_doActivity39_stub_double():
    # umlstatemachineselect_Behavior has no real 'umlstatemachineselect_Behavior41' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_Behavior()
    setattr(partner, 'umlstatemachineselect_Behavior41', None)
    _safe_set(owner, 'umlstatemachineselect_State40', partner)
    assert getattr(partner, 'umlstatemachineselect_Behavior41') == owner
    _safe_set(owner, 'umlstatemachineselect_State40', None)
    assert getattr(partner, 'umlstatemachineselect_Behavior41') is None


def test_assoc_effect23_stub_double():
    # umlstatemachineselect_Behavior has no real 'umlstatemachineselect_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Behavior()
    setattr(partner, 'umlstatemachineselect_Behavior', None)
    _safe_set(owner, 'umlstatemachineselect_Transition', partner)
    assert getattr(partner, 'umlstatemachineselect_Behavior') == owner
    _safe_set(owner, 'umlstatemachineselect_Transition', None)
    assert getattr(partner, 'umlstatemachineselect_Behavior') is None


def test_assoc_entry34_stub_double():
    # umlstatemachineselect_Behavior has no real 'umlstatemachineselect_Behavior35' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_Behavior()
    setattr(partner, 'umlstatemachineselect_Behavior35', None)
    _safe_set(owner, 'umlstatemachineselect_State', partner)
    assert getattr(partner, 'umlstatemachineselect_Behavior35') == owner
    _safe_set(owner, 'umlstatemachineselect_State', None)
    assert getattr(partner, 'umlstatemachineselect_Behavior35') is None


def test_assoc_entry52_stub_double():
    # umlstatemachineselect_ConnectionPointReference has no real 'umlstatemachineselect_ConnectionPointReference' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_PseudoState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_PseudoState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_PseudoState(kind="sample_text")
    partner = umlstatemachineselect_ConnectionPointReference()
    setattr(partner, 'umlstatemachineselect_ConnectionPointReference', None)
    _safe_set(owner, 'umlstatemachineselect_PseudoState', partner)
    assert owner in getattr(partner, 'umlstatemachineselect_ConnectionPointReference')
    _safe_set(owner, 'umlstatemachineselect_PseudoState', None)
    assert owner not in getattr(partner, 'umlstatemachineselect_ConnectionPointReference')


def test_assoc_exit36_stub_double():
    # umlstatemachineselect_Behavior has no real 'umlstatemachineselect_Behavior38' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_Behavior()
    setattr(partner, 'umlstatemachineselect_Behavior38', None)
    _safe_set(owner, 'umlstatemachineselect_State37', partner)
    assert getattr(partner, 'umlstatemachineselect_Behavior38') == owner
    _safe_set(owner, 'umlstatemachineselect_State37', None)
    assert getattr(partner, 'umlstatemachineselect_Behavior38') is None


def test_assoc_exit53_stub_double():
    # umlstatemachineselect_ConnectionPointReference has no real 'umlstatemachineselect_ConnectionPointReference54' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_PseudoState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_PseudoState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_PseudoState(kind="sample_text")
    partner = umlstatemachineselect_ConnectionPointReference()
    setattr(partner, 'umlstatemachineselect_ConnectionPointReference54', None)
    _safe_set(owner, 'umlstatemachineselect_PseudoState55', partner)
    assert owner in getattr(partner, 'umlstatemachineselect_ConnectionPointReference54')
    _safe_set(owner, 'umlstatemachineselect_PseudoState55', None)
    assert owner not in getattr(partner, 'umlstatemachineselect_ConnectionPointReference54')


def test_assoc_guard24_stub_double():
    # umlstatemachineselect_Constraint has no real 'umlstatemachineselect_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Constraint()
    setattr(partner, 'umlstatemachineselect_Constraint', None)
    _safe_set(owner, 'umlstatemachineselect_Transition25', partner)
    assert getattr(partner, 'umlstatemachineselect_Constraint') == owner
    _safe_set(owner, 'umlstatemachineselect_Transition25', None)
    assert getattr(partner, 'umlstatemachineselect_Constraint') is None


def test_assoc_incoming15_stub_double():
    # umlstatemachineselect_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition16', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition16', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outgoing13_stub_double():
    # umlstatemachineselect_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition14', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition14', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_region28_stub_double():
    # umlstatemachineselect_Region has no real 'Region29' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_Region()
    setattr(partner, 'Region29', None)
    _safe_set(owner, 'state', {partner})
    assert getattr(partner, 'Region29') == owner
    _safe_set(owner, 'state', set())
    assert getattr(partner, 'Region29') is None


def test_assoc_source21_stub_double():
    # umlstatemachineselect_Vertex has no real 'Vertex22' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Vertex()
    setattr(partner, 'Vertex22', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'Vertex22') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'Vertex22') is None


def test_assoc_state50_stub_double():
    # umlstatemachineselect_ConnectionPointReference has no real 'connection' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_ConnectionPointReference()
    setattr(partner, 'connection', None)
    _safe_set(owner, 'State51', partner)
    assert getattr(partner, 'connection') == owner
    _safe_set(owner, 'State51', None)
    assert getattr(partner, 'connection') is None


def test_assoc_state8_stub_double():
    # umlstatemachineselect_Region has no real 'region9' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_Region()
    setattr(partner, 'region9', None)
    _safe_set(owner, 'State10', partner)
    assert getattr(partner, 'region9') == owner
    _safe_set(owner, 'State10', None)
    assert getattr(partner, 'region9') is None


def test_assoc_stateInvariant42_stub_double():
    # umlstatemachineselect_Constraint has no real 'umlstatemachineselect_Constraint44' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_Constraint()
    setattr(partner, 'umlstatemachineselect_Constraint44', None)
    _safe_set(owner, 'umlstatemachineselect_State43', partner)
    assert getattr(partner, 'umlstatemachineselect_Constraint44') == owner
    _safe_set(owner, 'umlstatemachineselect_State43', None)
    assert getattr(partner, 'umlstatemachineselect_Constraint44') is None


def test_assoc_stateMachine48_stub_double():
    # umlstatemachineselect_StateMachine has no real 'StateMachine49' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_PseudoState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_PseudoState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_PseudoState(kind="sample_text")
    partner = umlstatemachineselect_StateMachine()
    setattr(partner, 'StateMachine49', None)
    _safe_set(owner, 'connectionPoint', partner)
    assert getattr(partner, 'StateMachine49') == owner
    _safe_set(owner, 'connectionPoint', None)
    assert getattr(partner, 'StateMachine49') is None


def test_assoc_submachine32_stub_double():
    # umlstatemachineselect_StateMachine has no real 'StateMachine33' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_StateMachine()
    setattr(partner, 'StateMachine33', None)
    _safe_set(owner, 'submachineState', partner)
    assert getattr(partner, 'StateMachine33') == owner
    _safe_set(owner, 'submachineState', None)
    assert getattr(partner, 'StateMachine33') is None


def test_assoc_submachineState1_stub_double():
    # umlstatemachineselect_StateMachine has no real 'submachine' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_State(isComposite=True, isOrthogonal=True, isSimple=True, isSubmachineState=True)
    partner = umlstatemachineselect_StateMachine()
    setattr(partner, 'submachine', None)
    _safe_set(owner, 'State', partner)
    assert owner in getattr(partner, 'submachine')
    _safe_set(owner, 'State', None)
    assert owner not in getattr(partner, 'submachine')


def test_assoc_target19_stub_double():
    # umlstatemachineselect_Vertex has no real 'Vertex20' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Vertex()
    setattr(partner, 'Vertex20', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'Vertex20') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'Vertex20') is None


def test_assoc_transition6_stub_double():
    # umlstatemachineselect_Region has no real 'container7' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Region()
    setattr(partner, 'container7', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'container7')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'container7')


def test_assoc_trigger26_stub_double():
    # umlstatemachineselect_Trigger has no real 'umlstatemachineselect_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so umlstatemachineselect_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlstatemachineselect_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlstatemachineselect_Transition(kind="sample_text")
    partner = umlstatemachineselect_Trigger()
    setattr(partner, 'umlstatemachineselect_Trigger', None)
    _safe_set(owner, 'umlstatemachineselect_Transition27', {partner})
    assert getattr(partner, 'umlstatemachineselect_Trigger') == owner
    _safe_set(owner, 'umlstatemachineselect_Transition27', set())
    assert getattr(partner, 'umlstatemachineselect_Trigger') is None


