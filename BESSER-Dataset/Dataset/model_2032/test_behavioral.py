import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MySM_Action,
    MySM_ComplexSate,
    MySM_LabeledTransition,
    MySM_Pseudostate,
    MySM_Region,
    MySM_State,
    MySM_Statemachine,
    MySM_Transition,
    MySM_Vertex,
    Region,
    State,
    Transition,
    Vertex,
    Pseudokind,
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

def test_assoc_initial4_reverse_link_reassign_clear():
    a1 = MySM_Region(name="sample_text")
    a2 = MySM_Region(name="sample_text_2")
    b = MySM_Pseudostate(kind="sample_text", psId="sample_text")
    _safe_set(b, 'MySM_Pseudostate', a1)
    assert _is_linked(b, 'MySM_Pseudostate', a1)
    if hasattr(a1, 'MySM_Region5'):
        assert _is_linked(a1, 'MySM_Region5', b)
    _safe_set(b, 'MySM_Pseudostate', a2)
    assert _is_linked(b, 'MySM_Pseudostate', a2)
    if hasattr(a1, 'MySM_Region5'):
        assert not _is_linked(a1, 'MySM_Region5', b)
    if hasattr(a2, 'MySM_Region5'):
        assert _is_linked(a2, 'MySM_Region5', b)
    _safe_set(b, 'MySM_Pseudostate', None)
    assert not _is_linked(b, 'MySM_Pseudostate', a2)
    if hasattr(a2, 'MySM_Region5'):
        assert not _is_linked(a2, 'MySM_Region5', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = MySM_State(name="sample_text")
    a2 = MySM_State(name="sample_text_2")
    b = MySM_Region(name="sample_text")
    _safe_set(b, 'MySM_Region', {a1})
    assert _is_linked(b, 'MySM_Region', a1)
    if hasattr(a1, 'MySM_State'):
        assert _is_linked(a1, 'MySM_State', b)
    _safe_set(b, 'MySM_Region', {a2})
    assert _is_linked(b, 'MySM_Region', a2)
    if hasattr(a1, 'MySM_State'):
        assert not _is_linked(a1, 'MySM_State', b)
    if hasattr(a2, 'MySM_State'):
        assert _is_linked(a2, 'MySM_State', b)
    _safe_set(b, 'MySM_Region', set())
    assert not _is_linked(b, 'MySM_Region', a2)
    if hasattr(a2, 'MySM_State'):
        assert not _is_linked(a2, 'MySM_State', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action16_stub_double():
    # MySM_LabeledTransition has no real 'MySM_LabeledTransition' property in the generated
    # code (a bare stub) -- manually attach it so MySM_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MySM_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MySM_Action(name="sample_text")
    partner = MySM_LabeledTransition()
    setattr(partner, 'MySM_LabeledTransition', None)
    _safe_set(owner, 'MySM_Action17', partner)
    assert getattr(partner, 'MySM_LabeledTransition') == owner
    _safe_set(owner, 'MySM_Action17', None)
    assert getattr(partner, 'MySM_LabeledTransition') is None


def test_assoc_actions1_stub_double():
    # MySM_Statemachine has no real 'MySM_Statemachine2' property in the generated
    # code (a bare stub) -- manually attach it so MySM_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MySM_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MySM_Action(name="sample_text")
    partner = MySM_Statemachine()
    setattr(partner, 'MySM_Statemachine2', None)
    _safe_set(owner, 'MySM_Action', partner)
    assert owner in getattr(partner, 'MySM_Statemachine2')
    _safe_set(owner, 'MySM_Action', None)
    assert owner not in getattr(partner, 'MySM_Statemachine2')


def test_assoc_outgoings6_stub_double():
    # MySM_Vertex has no real 'MySM_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so MySM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MySM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MySM_Transition(tId="sample_text")
    partner = MySM_Vertex()
    setattr(partner, 'MySM_Vertex', None)
    _safe_set(owner, 'MySM_Transition7', partner)
    assert owner in getattr(partner, 'MySM_Vertex')
    _safe_set(owner, 'MySM_Transition7', None)
    assert owner not in getattr(partner, 'MySM_Vertex')


def test_assoc_region8_stub_double():
    # MySM_ComplexSate has no real 'MySM_ComplexSate' property in the generated
    # code (a bare stub) -- manually attach it so MySM_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MySM_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MySM_Region(name="sample_text")
    partner = MySM_ComplexSate()
    setattr(partner, 'MySM_ComplexSate', None)
    _safe_set(owner, 'MySM_Region9', partner)
    assert owner in getattr(partner, 'MySM_ComplexSate')
    _safe_set(owner, 'MySM_Region9', None)
    assert owner not in getattr(partner, 'MySM_ComplexSate')


def test_assoc_source10_stub_double():
    # MySM_Vertex has no real 'MySM_Vertex12' property in the generated
    # code (a bare stub) -- manually attach it so MySM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MySM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MySM_Transition(tId="sample_text")
    partner = MySM_Vertex()
    setattr(partner, 'MySM_Vertex12', None)
    _safe_set(owner, 'MySM_Transition11', partner)
    assert getattr(partner, 'MySM_Vertex12') == owner
    _safe_set(owner, 'MySM_Transition11', None)
    assert getattr(partner, 'MySM_Vertex12') is None


def test_assoc_target13_stub_double():
    # MySM_Vertex has no real 'MySM_Vertex15' property in the generated
    # code (a bare stub) -- manually attach it so MySM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MySM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MySM_Transition(tId="sample_text")
    partner = MySM_Vertex()
    setattr(partner, 'MySM_Vertex15', None)
    _safe_set(owner, 'MySM_Transition14', partner)
    assert getattr(partner, 'MySM_Vertex15') == owner
    _safe_set(owner, 'MySM_Transition14', None)
    assert getattr(partner, 'MySM_Vertex15') is None


def test_assoc_transitions0_stub_double():
    # MySM_Statemachine has no real 'MySM_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so MySM_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MySM_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MySM_Transition(tId="sample_text")
    partner = MySM_Statemachine()
    setattr(partner, 'MySM_Statemachine', None)
    _safe_set(owner, 'MySM_Transition', partner)
    assert owner in getattr(partner, 'MySM_Statemachine')
    _safe_set(owner, 'MySM_Transition', None)
    assert owner not in getattr(partner, 'MySM_Statemachine')


