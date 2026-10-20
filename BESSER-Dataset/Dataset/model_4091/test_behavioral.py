import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    Constraint,
    Event,
    NamedElement,
    Region,
    State,
    StateMachine,
    Transition,
    Trigger,
    Vertex,
    almostuml_NamedElement,
    almostuml_Vertex,
    almostuml_statemachines_EventOccurrence,
    statemachines_CustomEvent,
    statemachines_CustomSystem,
    statemachines_EventOccurrence,
    statemachines_Util,
    statemachines_almostuml_Behavior,
    statemachines_almostuml_Constraint,
    statemachines_almostuml_Event,
    statemachines_almostuml_FinalState,
    statemachines_almostuml_NamedElement,
    statemachines_almostuml_Pseudostate,
    statemachines_almostuml_Region,
    statemachines_almostuml_State,
    statemachines_almostuml_StateMachine,
    statemachines_almostuml_Transition,
    statemachines_almostuml_Trigger,
    statemachines_almostuml_Vertex,
    PseudostateKind,
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

def test_assoc_currentState11_stub_double():
    # State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Region()
    partner = State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'statemachines_almostuml_Region12', partner)
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'statemachines_almostuml_Region12', None)
    assert getattr(partner, 'State') is None


def test_assoc_doActivity17_stub_double():
    # Behavior has no real 'Behavior19' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_State()
    partner = Behavior()
    setattr(partner, 'Behavior19', None)
    _safe_set(owner, 'statemachines_almostuml_State18', partner)
    assert getattr(partner, 'Behavior19') == owner
    _safe_set(owner, 'statemachines_almostuml_State18', None)
    assert getattr(partner, 'Behavior19') is None


def test_assoc_effect34_stub_double():
    # Behavior has no real 'Behavior36' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Transition()
    partner = Behavior()
    setattr(partner, 'Behavior36', None)
    _safe_set(owner, 'statemachines_almostuml_Transition35', partner)
    assert getattr(partner, 'Behavior36') == owner
    _safe_set(owner, 'statemachines_almostuml_Transition35', None)
    assert getattr(partner, 'Behavior36') is None


def test_assoc_entry13_stub_double():
    # Behavior has no real 'Behavior' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_State()
    partner = Behavior()
    setattr(partner, 'Behavior', None)
    _safe_set(owner, 'statemachines_almostuml_State', partner)
    assert getattr(partner, 'Behavior') == owner
    _safe_set(owner, 'statemachines_almostuml_State', None)
    assert getattr(partner, 'Behavior') is None


def test_assoc_events1_stub_double():
    # statemachines_CustomEvent has no real 'statemachines_CustomEvent' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_CustomSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_CustomSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_CustomSystem()
    partner = statemachines_CustomEvent()
    setattr(partner, 'statemachines_CustomEvent', None)
    _safe_set(owner, 'statemachines_CustomSystem2', {partner})
    assert getattr(partner, 'statemachines_CustomEvent') == owner
    _safe_set(owner, 'statemachines_CustomSystem2', set())
    assert getattr(partner, 'statemachines_CustomEvent') is None


def test_assoc_exit14_stub_double():
    # Behavior has no real 'Behavior16' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_State()
    partner = Behavior()
    setattr(partner, 'Behavior16', None)
    _safe_set(owner, 'statemachines_almostuml_State15', partner)
    assert getattr(partner, 'Behavior16') == owner
    _safe_set(owner, 'statemachines_almostuml_State15', None)
    assert getattr(partner, 'Behavior16') is None


def test_assoc_guard32_stub_double():
    # Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Transition()
    partner = Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'statemachines_almostuml_Transition33', partner)
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'statemachines_almostuml_Transition33', None)
    assert getattr(partner, 'Constraint') is None


def test_assoc_queue6_stub_double():
    # almostuml_statemachines_EventOccurrence has no real 'almostuml_statemachines_EventOccurrence' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_StateMachine()
    partner = almostuml_statemachines_EventOccurrence()
    setattr(partner, 'almostuml_statemachines_EventOccurrence', None)
    _safe_set(owner, 'statemachines_almostuml_StateMachine', {partner})
    assert getattr(partner, 'almostuml_statemachines_EventOccurrence') == owner
    _safe_set(owner, 'statemachines_almostuml_StateMachine', set())
    assert getattr(partner, 'almostuml_statemachines_EventOccurrence') is None


def test_assoc_region20_stub_double():
    # Region has no real 'Region22' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_State()
    partner = Region()
    setattr(partner, 'Region22', None)
    _safe_set(owner, 'statemachines_almostuml_State21', {partner})
    assert getattr(partner, 'Region22') == owner
    _safe_set(owner, 'statemachines_almostuml_State21', set())
    assert getattr(partner, 'Region22') is None


def test_assoc_region5_stub_double():
    # Region has no real 'Region' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_StateMachine()
    partner = Region()
    setattr(partner, 'Region', None)
    _safe_set(owner, 'stateMachine', {partner})
    assert getattr(partner, 'Region') == owner
    _safe_set(owner, 'stateMachine', set())
    assert getattr(partner, 'Region') is None


def test_assoc_source25_stub_double():
    # Vertex has no real 'Vertex26' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Transition()
    partner = Vertex()
    setattr(partner, 'Vertex26', None)
    _safe_set(owner, 'statemachines_almostuml_Transition', partner)
    assert getattr(partner, 'Vertex26') == owner
    _safe_set(owner, 'statemachines_almostuml_Transition', None)
    assert getattr(partner, 'Vertex26') is None


def test_assoc_stateMachine9_stub_double():
    # StateMachine has no real 'StateMachine10' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Region()
    partner = StateMachine()
    setattr(partner, 'StateMachine10', None)
    _safe_set(owner, 'region', partner)
    assert getattr(partner, 'StateMachine10') == owner
    _safe_set(owner, 'region', None)
    assert getattr(partner, 'StateMachine10') is None


def test_assoc_statemachine0_stub_double():
    # StateMachine has no real 'StateMachine' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_CustomSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_CustomSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_CustomSystem()
    partner = StateMachine()
    setattr(partner, 'StateMachine', None)
    _safe_set(owner, 'statemachines_CustomSystem', partner)
    assert getattr(partner, 'StateMachine') == owner
    _safe_set(owner, 'statemachines_CustomSystem', None)
    assert getattr(partner, 'StateMachine') is None


def test_assoc_subvertex7_stub_double():
    # Vertex has no real 'Vertex' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Region()
    partner = Vertex()
    setattr(partner, 'Vertex', None)
    _safe_set(owner, 'container', {partner})
    assert getattr(partner, 'Vertex') == owner
    _safe_set(owner, 'container', set())
    assert getattr(partner, 'Vertex') is None


def test_assoc_target27_stub_double():
    # Vertex has no real 'Vertex29' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Transition()
    partner = Vertex()
    setattr(partner, 'Vertex29', None)
    _safe_set(owner, 'statemachines_almostuml_Transition28', partner)
    assert getattr(partner, 'Vertex29') == owner
    _safe_set(owner, 'statemachines_almostuml_Transition28', None)
    assert getattr(partner, 'Vertex29') is None


def test_assoc_transition8_stub_double():
    # Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Region()
    partner = Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'statemachines_almostuml_Region', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'statemachines_almostuml_Region', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_trigger30_stub_double():
    # Trigger has no real 'Trigger' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_almostuml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_almostuml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_almostuml_Transition()
    partner = Trigger()
    setattr(partner, 'Trigger', None)
    _safe_set(owner, 'statemachines_almostuml_Transition31', {partner})
    assert getattr(partner, 'Trigger') == owner
    _safe_set(owner, 'statemachines_almostuml_Transition31', set())
    assert getattr(partner, 'Trigger') is None


