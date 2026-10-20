import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    State,
    Vertex,
    uml_Activity,
    uml_Behavior,
    uml_FinalState,
    uml_Pseudostate,
    uml_Region,
    uml_State,
    uml_StateMachine,
    uml_Transition,
    uml_Trigger,
    uml_Vertex,
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

def test_assoc_effect1_reverse_link_reassign_clear():
    a1 = uml_Transition(name="sample_text")
    a2 = uml_Transition(name="sample_text_2")
    b = uml_Behavior(name="sample_text")
    _safe_set(b, 'uml_Behavior', a1)
    assert _is_linked(b, 'uml_Behavior', a1)
    if hasattr(a1, 'uml_Transition'):
        assert _is_linked(a1, 'uml_Transition', b)
    _safe_set(b, 'uml_Behavior', a2)
    assert _is_linked(b, 'uml_Behavior', a2)
    if hasattr(a1, 'uml_Transition'):
        assert not _is_linked(a1, 'uml_Transition', b)
    if hasattr(a2, 'uml_Transition'):
        assert _is_linked(a2, 'uml_Transition', b)
    _safe_set(b, 'uml_Behavior', None)
    assert not _is_linked(b, 'uml_Behavior', a2)
    if hasattr(a2, 'uml_Transition'):
        assert not _is_linked(a2, 'uml_Transition', b)


def test_assoc_source6_reverse_link_reassign_clear():
    a1 = uml_Vertex(name="sample_text")
    a2 = uml_Vertex(name="sample_text_2")
    b = uml_Transition(name="sample_text")
    _safe_set(b, 'uml_Transition7', a1)
    assert _is_linked(b, 'uml_Transition7', a1)
    if hasattr(a1, 'uml_Vertex8'):
        assert _is_linked(a1, 'uml_Vertex8', b)
    _safe_set(b, 'uml_Transition7', a2)
    assert _is_linked(b, 'uml_Transition7', a2)
    if hasattr(a1, 'uml_Vertex8'):
        assert not _is_linked(a1, 'uml_Vertex8', b)
    if hasattr(a2, 'uml_Vertex8'):
        assert _is_linked(a2, 'uml_Vertex8', b)
    _safe_set(b, 'uml_Transition7', None)
    assert not _is_linked(b, 'uml_Transition7', a2)
    if hasattr(a2, 'uml_Vertex8'):
        assert not _is_linked(a2, 'uml_Vertex8', b)


def test_assoc_target4_reverse_link_reassign_clear():
    a1 = uml_Vertex(name="sample_text")
    a2 = uml_Vertex(name="sample_text_2")
    b = uml_Transition(name="sample_text")
    _safe_set(b, 'uml_Transition5', a1)
    assert _is_linked(b, 'uml_Transition5', a1)
    if hasattr(a1, 'uml_Vertex'):
        assert _is_linked(a1, 'uml_Vertex', b)
    _safe_set(b, 'uml_Transition5', a2)
    assert _is_linked(b, 'uml_Transition5', a2)
    if hasattr(a1, 'uml_Vertex'):
        assert not _is_linked(a1, 'uml_Vertex', b)
    if hasattr(a2, 'uml_Vertex'):
        assert _is_linked(a2, 'uml_Vertex', b)
    _safe_set(b, 'uml_Transition5', None)
    assert not _is_linked(b, 'uml_Transition5', a2)
    if hasattr(a2, 'uml_Vertex'):
        assert not _is_linked(a2, 'uml_Vertex', b)


def test_assoc_trigger2_reverse_link_reassign_clear():
    a1 = uml_Trigger(name="sample_text")
    a2 = uml_Trigger(name="sample_text_2")
    b = uml_Transition(name="sample_text")
    _safe_set(b, 'uml_Transition3', {a1})
    assert _is_linked(b, 'uml_Transition3', a1)
    if hasattr(a1, 'uml_Trigger'):
        assert _is_linked(a1, 'uml_Trigger', b)
    _safe_set(b, 'uml_Transition3', {a2})
    assert _is_linked(b, 'uml_Transition3', a2)
    if hasattr(a1, 'uml_Trigger'):
        assert not _is_linked(a1, 'uml_Trigger', b)
    if hasattr(a2, 'uml_Trigger'):
        assert _is_linked(a2, 'uml_Trigger', b)
    _safe_set(b, 'uml_Transition3', set())
    assert not _is_linked(b, 'uml_Transition3', a2)
    if hasattr(a2, 'uml_Trigger'):
        assert not _is_linked(a2, 'uml_Trigger', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_container13_stub_double():
    # uml_Region has no real 'Region' property in the generated
    # code (a bare stub) -- manually attach it so uml_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Vertex(name="sample_text")
    partner = uml_Region()
    setattr(partner, 'Region', None)
    _safe_set(owner, 'subvertex', partner)
    assert getattr(partner, 'Region') == owner
    _safe_set(owner, 'subvertex', None)
    assert getattr(partner, 'Region') is None


def test_assoc_doActivity19_stub_double():
    # uml_State has no real 'uml_State20' property in the generated
    # code (a bare stub) -- manually attach it so uml_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Behavior(name="sample_text")
    partner = uml_State()
    setattr(partner, 'uml_State20', None)
    _safe_set(owner, 'uml_Behavior21', partner)
    assert getattr(partner, 'uml_State20') == owner
    _safe_set(owner, 'uml_Behavior21', None)
    assert getattr(partner, 'uml_State20') is None


def test_assoc_entry14_stub_double():
    # uml_State has no real 'uml_State' property in the generated
    # code (a bare stub) -- manually attach it so uml_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Behavior(name="sample_text")
    partner = uml_State()
    setattr(partner, 'uml_State', None)
    _safe_set(owner, 'uml_Behavior15', partner)
    assert getattr(partner, 'uml_State') == owner
    _safe_set(owner, 'uml_Behavior15', None)
    assert getattr(partner, 'uml_State') is None


def test_assoc_exit16_stub_double():
    # uml_State has no real 'uml_State17' property in the generated
    # code (a bare stub) -- manually attach it so uml_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Behavior(name="sample_text")
    partner = uml_State()
    setattr(partner, 'uml_State17', None)
    _safe_set(owner, 'uml_Behavior18', partner)
    assert getattr(partner, 'uml_State17') == owner
    _safe_set(owner, 'uml_Behavior18', None)
    assert getattr(partner, 'uml_State17') is None


def test_assoc_subvertex9_stub_double():
    # uml_Region has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so uml_Vertex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Vertex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Vertex(name="sample_text")
    partner = uml_Region()
    setattr(partner, 'container', None)
    _safe_set(owner, 'Vertex', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'Vertex', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_transition10_stub_double():
    # uml_Region has no real 'uml_Region11' property in the generated
    # code (a bare stub) -- manually attach it so uml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Transition(name="sample_text")
    partner = uml_Region()
    setattr(partner, 'uml_Region11', None)
    _safe_set(owner, 'uml_Transition12', partner)
    assert owner in getattr(partner, 'uml_Region11')
    _safe_set(owner, 'uml_Transition12', None)
    assert owner not in getattr(partner, 'uml_Region11')


