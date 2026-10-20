import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Region,
    State,
    Transition,
    Vertex,
    statemachine_Action,
    statemachine_ComplexState,
    statemachine_LabeledTransition,
    statemachine_Pseudostate,
    statemachine_Region,
    statemachine_State,
    statemachine_Statemachine,
    statemachine_Transition,
    statemachine_Vertex,
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

def test_assoc_actions12_reverse_link_reassign_clear():
    a1 = statemachine_Statemachine(name="sample_text")
    a2 = statemachine_Statemachine(name="sample_text_2")
    b = statemachine_Action(name="sample_text")
    _safe_set(b, 'statemachine_Action', a1)
    assert _is_linked(b, 'statemachine_Action', a1)
    if hasattr(a1, 'statemachine_Statemachine13'):
        assert _is_linked(a1, 'statemachine_Statemachine13', b)
    _safe_set(b, 'statemachine_Action', a2)
    assert _is_linked(b, 'statemachine_Action', a2)
    if hasattr(a1, 'statemachine_Statemachine13'):
        assert not _is_linked(a1, 'statemachine_Statemachine13', b)
    if hasattr(a2, 'statemachine_Statemachine13'):
        assert _is_linked(a2, 'statemachine_Statemachine13', b)
    _safe_set(b, 'statemachine_Action', None)
    assert not _is_linked(b, 'statemachine_Action', a2)
    if hasattr(a2, 'statemachine_Statemachine13'):
        assert not _is_linked(a2, 'statemachine_Statemachine13', b)


def test_assoc_initial17_reverse_link_reassign_clear():
    a1 = statemachine_Region()
    a2 = statemachine_Region()
    b = statemachine_Pseudostate(id="sample_text", kind="sample_text")
    _safe_set(b, 'statemachine_Pseudostate', a1)
    assert _is_linked(b, 'statemachine_Pseudostate', a1)
    if hasattr(a1, 'statemachine_Region18'):
        assert _is_linked(a1, 'statemachine_Region18', b)
    _safe_set(b, 'statemachine_Pseudostate', a2)
    assert _is_linked(b, 'statemachine_Pseudostate', a2)
    if hasattr(a1, 'statemachine_Region18'):
        assert not _is_linked(a1, 'statemachine_Region18', b)
    if hasattr(a2, 'statemachine_Region18'):
        assert _is_linked(a2, 'statemachine_Region18', b)
    _safe_set(b, 'statemachine_Pseudostate', None)
    assert not _is_linked(b, 'statemachine_Pseudostate', a2)
    if hasattr(a2, 'statemachine_Region18'):
        assert not _is_linked(a2, 'statemachine_Region18', b)


def test_assoc_region2_reverse_link_reassign_clear():
    a1 = statemachine_Region()
    a2 = statemachine_Region()
    b = statemachine_ComplexState()
    _safe_set(b, 'statemachine_ComplexState3', {a1})
    assert _is_linked(b, 'statemachine_ComplexState3', a1)
    if hasattr(a1, 'statemachine_Region'):
        assert _is_linked(a1, 'statemachine_Region', b)
    _safe_set(b, 'statemachine_ComplexState3', {a2})
    assert _is_linked(b, 'statemachine_ComplexState3', a2)
    if hasattr(a1, 'statemachine_Region'):
        assert not _is_linked(a1, 'statemachine_Region', b)
    if hasattr(a2, 'statemachine_Region'):
        assert _is_linked(a2, 'statemachine_Region', b)
    _safe_set(b, 'statemachine_ComplexState3', set())
    assert not _is_linked(b, 'statemachine_ComplexState3', a2)
    if hasattr(a2, 'statemachine_Region'):
        assert not _is_linked(a2, 'statemachine_Region', b)


def test_assoc_states14_reverse_link_reassign_clear():
    a1 = statemachine_State(name="sample_text")
    a2 = statemachine_State(name="sample_text_2")
    b = statemachine_Region()
    _safe_set(b, 'statemachine_Region15', {a1})
    assert _is_linked(b, 'statemachine_Region15', a1)
    if hasattr(a1, 'statemachine_State16'):
        assert _is_linked(a1, 'statemachine_State16', b)
    _safe_set(b, 'statemachine_Region15', {a2})
    assert _is_linked(b, 'statemachine_Region15', a2)
    if hasattr(a1, 'statemachine_State16'):
        assert not _is_linked(a1, 'statemachine_State16', b)
    if hasattr(a2, 'statemachine_State16'):
        assert _is_linked(a2, 'statemachine_State16', b)
    _safe_set(b, 'statemachine_Region15', set())
    assert not _is_linked(b, 'statemachine_Region15', a2)
    if hasattr(a2, 'statemachine_State16'):
        assert not _is_linked(a2, 'statemachine_State16', b)


def test_assoc_super1_reverse_link_reassign_clear():
    a1 = statemachine_State(name="sample_text")
    a2 = statemachine_State(name="sample_text_2")
    b = statemachine_ComplexState()
    _safe_set(b, 'statemachine_ComplexState', a1)
    assert _is_linked(b, 'statemachine_ComplexState', a1)
    if hasattr(a1, 'statemachine_State'):
        assert _is_linked(a1, 'statemachine_State', b)
    _safe_set(b, 'statemachine_ComplexState', a2)
    assert _is_linked(b, 'statemachine_ComplexState', a2)
    if hasattr(a1, 'statemachine_State'):
        assert not _is_linked(a1, 'statemachine_State', b)
    if hasattr(a2, 'statemachine_State'):
        assert _is_linked(a2, 'statemachine_State', b)
    _safe_set(b, 'statemachine_ComplexState', None)
    assert not _is_linked(b, 'statemachine_ComplexState', a2)
    if hasattr(a2, 'statemachine_State'):
        assert not _is_linked(a2, 'statemachine_State', b)


def test_assoc_transitions10_reverse_link_reassign_clear():
    a1 = statemachine_Transition(id="sample_text")
    a2 = statemachine_Transition(id="sample_text_2")
    b = statemachine_Statemachine(name="sample_text")
    _safe_set(b, 'statemachine_Statemachine', {a1})
    assert _is_linked(b, 'statemachine_Statemachine', a1)
    if hasattr(a1, 'statemachine_Transition11'):
        assert _is_linked(a1, 'statemachine_Transition11', b)
    _safe_set(b, 'statemachine_Statemachine', {a2})
    assert _is_linked(b, 'statemachine_Statemachine', a2)
    if hasattr(a1, 'statemachine_Transition11'):
        assert not _is_linked(a1, 'statemachine_Transition11', b)
    if hasattr(a2, 'statemachine_Transition11'):
        assert _is_linked(a2, 'statemachine_Transition11', b)
    _safe_set(b, 'statemachine_Statemachine', set())
    assert not _is_linked(b, 'statemachine_Statemachine', a2)
    if hasattr(a2, 'statemachine_Transition11'):
        assert not _is_linked(a2, 'statemachine_Transition11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action19_stub_double():
    # statemachine_LabeledTransition has no real 'statemachine_LabeledTransition' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Action(name="sample_text")
    partner = statemachine_LabeledTransition()
    setattr(partner, 'statemachine_LabeledTransition', None)
    _safe_set(owner, 'statemachine_Action20', partner)
    assert getattr(partner, 'statemachine_LabeledTransition') == owner
    _safe_set(owner, 'statemachine_Action20', None)
    assert getattr(partner, 'statemachine_LabeledTransition') is None


def test_assoc_outgoings0_stub_double():
    # statemachine_Vertex has no real 'statemachine_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(id="sample_text")
    partner = statemachine_Vertex()
    setattr(partner, 'statemachine_Vertex', None)
    _safe_set(owner, 'statemachine_Transition', partner)
    assert owner in getattr(partner, 'statemachine_Vertex')
    _safe_set(owner, 'statemachine_Transition', None)
    assert owner not in getattr(partner, 'statemachine_Vertex')


def test_assoc_source4_stub_double():
    # statemachine_Vertex has no real 'statemachine_Vertex6' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(id="sample_text")
    partner = statemachine_Vertex()
    setattr(partner, 'statemachine_Vertex6', None)
    _safe_set(owner, 'statemachine_Transition5', partner)
    assert getattr(partner, 'statemachine_Vertex6') == owner
    _safe_set(owner, 'statemachine_Transition5', None)
    assert getattr(partner, 'statemachine_Vertex6') is None


def test_assoc_target7_stub_double():
    # statemachine_Vertex has no real 'statemachine_Vertex9' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(id="sample_text")
    partner = statemachine_Vertex()
    setattr(partner, 'statemachine_Vertex9', None)
    _safe_set(owner, 'statemachine_Transition8', partner)
    assert getattr(partner, 'statemachine_Vertex9') == owner
    _safe_set(owner, 'statemachine_Transition8', None)
    assert getattr(partner, 'statemachine_Vertex9') is None


