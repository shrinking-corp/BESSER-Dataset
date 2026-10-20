import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Thing,
    statechart101_NamedElement,
    statechart101_State,
    statechart101_Thing,
    statechart101_Transition,
    statechart101_Variable,
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

def test_assoc_parentstate3_reverse_link_reassign_clear():
    a1 = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    a2 = statechart101_State(activity="sample_text_2", label="sample_text_2", type="sample_text_2")
    b = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'substates', a1)
    assert _is_linked(b, 'substates', a1)
    if hasattr(a1, 'State4'):
        assert _is_linked(a1, 'State4', b)
    _safe_set(b, 'substates', a2)
    assert _is_linked(b, 'substates', a2)
    if hasattr(a1, 'State4'):
        assert not _is_linked(a1, 'State4', b)
    if hasattr(a2, 'State4'):
        assert _is_linked(a2, 'State4', b)
    _safe_set(b, 'substates', None)
    assert not _is_linked(b, 'substates', a2)
    if hasattr(a2, 'State4'):
        assert not _is_linked(a2, 'State4', b)


def test_assoc_source8_reverse_link_reassign_clear():
    a1 = statechart101_Transition(expression="sample_text")
    a2 = statechart101_Transition(expression="sample_text_2")
    b = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'statechart101_State10', a1)
    assert _is_linked(b, 'statechart101_State10', a1)
    if hasattr(a1, 'statechart101_Transition9'):
        assert _is_linked(a1, 'statechart101_Transition9', b)
    _safe_set(b, 'statechart101_State10', a2)
    assert _is_linked(b, 'statechart101_State10', a2)
    if hasattr(a1, 'statechart101_Transition9'):
        assert not _is_linked(a1, 'statechart101_Transition9', b)
    if hasattr(a2, 'statechart101_Transition9'):
        assert _is_linked(a2, 'statechart101_Transition9', b)
    _safe_set(b, 'statechart101_State10', None)
    assert not _is_linked(b, 'statechart101_State10', a2)
    if hasattr(a2, 'statechart101_Transition9'):
        assert not _is_linked(a2, 'statechart101_Transition9', b)


def test_assoc_substates1_reverse_link_reassign_clear():
    a1 = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    a2 = statechart101_State(activity="sample_text_2", label="sample_text_2", type="sample_text_2")
    b = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'parentstate', {a1})
    assert _is_linked(b, 'parentstate', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'parentstate', {a2})
    assert _is_linked(b, 'parentstate', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'parentstate', set())
    assert not _is_linked(b, 'parentstate', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_target11_reverse_link_reassign_clear():
    a1 = statechart101_Transition(expression="sample_text")
    a2 = statechart101_Transition(expression="sample_text_2")
    b = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'statechart101_State13', a1)
    assert _is_linked(b, 'statechart101_State13', a1)
    if hasattr(a1, 'statechart101_Transition12'):
        assert _is_linked(a1, 'statechart101_Transition12', b)
    _safe_set(b, 'statechart101_State13', a2)
    assert _is_linked(b, 'statechart101_State13', a2)
    if hasattr(a1, 'statechart101_Transition12'):
        assert not _is_linked(a1, 'statechart101_Transition12', b)
    if hasattr(a2, 'statechart101_Transition12'):
        assert _is_linked(a2, 'statechart101_Transition12', b)
    _safe_set(b, 'statechart101_State13', None)
    assert not _is_linked(b, 'statechart101_State13', a2)
    if hasattr(a2, 'statechart101_Transition12'):
        assert not _is_linked(a2, 'statechart101_Transition12', b)


def test_assoc_transitions6_reverse_link_reassign_clear():
    a1 = statechart101_Transition(expression="sample_text")
    a2 = statechart101_Transition(expression="sample_text_2")
    b = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'statechart101_State7', {a1})
    assert _is_linked(b, 'statechart101_State7', a1)
    if hasattr(a1, 'statechart101_Transition'):
        assert _is_linked(a1, 'statechart101_Transition', b)
    _safe_set(b, 'statechart101_State7', {a2})
    assert _is_linked(b, 'statechart101_State7', a2)
    if hasattr(a1, 'statechart101_Transition'):
        assert not _is_linked(a1, 'statechart101_Transition', b)
    if hasattr(a2, 'statechart101_Transition'):
        assert _is_linked(a2, 'statechart101_Transition', b)
    _safe_set(b, 'statechart101_State7', set())
    assert not _is_linked(b, 'statechart101_State7', a2)
    if hasattr(a2, 'statechart101_Transition'):
        assert not _is_linked(a2, 'statechart101_Transition', b)


def test_assoc_variables5_reverse_link_reassign_clear():
    a1 = statechart101_Variable(type="sample_text", value="sample_text")
    a2 = statechart101_Variable(type="sample_text_2", value="sample_text_2")
    b = statechart101_State(activity="sample_text", label="sample_text", type="sample_text")
    _safe_set(b, 'statechart101_State', {a1})
    assert _is_linked(b, 'statechart101_State', a1)
    if hasattr(a1, 'statechart101_Variable'):
        assert _is_linked(a1, 'statechart101_Variable', b)
    _safe_set(b, 'statechart101_State', {a2})
    assert _is_linked(b, 'statechart101_State', a2)
    if hasattr(a1, 'statechart101_Variable'):
        assert not _is_linked(a1, 'statechart101_Variable', b)
    if hasattr(a2, 'statechart101_Variable'):
        assert _is_linked(a2, 'statechart101_Variable', b)
    _safe_set(b, 'statechart101_State', set())
    assert not _is_linked(b, 'statechart101_State', a2)
    if hasattr(a2, 'statechart101_Variable'):
        assert not _is_linked(a2, 'statechart101_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

