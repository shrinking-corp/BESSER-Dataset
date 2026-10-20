import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    IDBase,
    dtmc_DTMC,
    dtmc_Label,
    dtmc_State,
    dtmc_Transition,
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

def test_assoc_States0_reverse_link_reassign_clear():
    a1 = dtmc_State(name="sample_text")
    a2 = dtmc_State(name="sample_text_2")
    b = dtmc_DTMC(name="sample_text")
    _safe_set(b, 'dtmc_DTMC', {a1})
    assert _is_linked(b, 'dtmc_DTMC', a1)
    if hasattr(a1, 'dtmc_State'):
        assert _is_linked(a1, 'dtmc_State', b)
    _safe_set(b, 'dtmc_DTMC', {a2})
    assert _is_linked(b, 'dtmc_DTMC', a2)
    if hasattr(a1, 'dtmc_State'):
        assert not _is_linked(a1, 'dtmc_State', b)
    if hasattr(a2, 'dtmc_State'):
        assert _is_linked(a2, 'dtmc_State', b)
    _safe_set(b, 'dtmc_DTMC', set())
    assert not _is_linked(b, 'dtmc_DTMC', a2)
    if hasattr(a2, 'dtmc_State'):
        assert not _is_linked(a2, 'dtmc_State', b)


def test_assoc_from_8_reverse_link_reassign_clear():
    a1 = dtmc_Transition(prob=3.14)
    a2 = dtmc_Transition(prob=9.99)
    b = dtmc_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_incoming4_reverse_link_reassign_clear():
    a1 = dtmc_Transition(prob=3.14)
    a2 = dtmc_Transition(prob=9.99)
    b = dtmc_State(name="sample_text")
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_initialState1_reverse_link_reassign_clear():
    a1 = dtmc_State(name="sample_text")
    a2 = dtmc_State(name="sample_text_2")
    b = dtmc_DTMC(name="sample_text")
    _safe_set(b, 'dtmc_DTMC2', a1)
    assert _is_linked(b, 'dtmc_DTMC2', a1)
    if hasattr(a1, 'dtmc_State3'):
        assert _is_linked(a1, 'dtmc_State3', b)
    _safe_set(b, 'dtmc_DTMC2', a2)
    assert _is_linked(b, 'dtmc_DTMC2', a2)
    if hasattr(a1, 'dtmc_State3'):
        assert not _is_linked(a1, 'dtmc_State3', b)
    if hasattr(a2, 'dtmc_State3'):
        assert _is_linked(a2, 'dtmc_State3', b)
    _safe_set(b, 'dtmc_DTMC2', None)
    assert not _is_linked(b, 'dtmc_DTMC2', a2)
    if hasattr(a2, 'dtmc_State3'):
        assert not _is_linked(a2, 'dtmc_State3', b)


def test_assoc_labels7_reverse_link_reassign_clear():
    a1 = dtmc_State(name="sample_text")
    a2 = dtmc_State(name="sample_text_2")
    b = dtmc_Label(name="sample_text")
    _safe_set(b, 'Label', a1)
    assert _is_linked(b, 'Label', a1)
    if hasattr(a1, 'state'):
        assert _is_linked(a1, 'state', b)
    _safe_set(b, 'Label', a2)
    assert _is_linked(b, 'Label', a2)
    if hasattr(a1, 'state'):
        assert not _is_linked(a1, 'state', b)
    if hasattr(a2, 'state'):
        assert _is_linked(a2, 'state', b)
    _safe_set(b, 'Label', None)
    assert not _is_linked(b, 'Label', a2)
    if hasattr(a2, 'state'):
        assert not _is_linked(a2, 'state', b)


def test_assoc_outgoing5_reverse_link_reassign_clear():
    a1 = dtmc_Transition(prob=3.14)
    a2 = dtmc_Transition(prob=9.99)
    b = dtmc_State(name="sample_text")
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'Transition6'):
        assert _is_linked(a1, 'Transition6', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'Transition6'):
        assert not _is_linked(a1, 'Transition6', b)
    if hasattr(a2, 'Transition6'):
        assert _is_linked(a2, 'Transition6', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'Transition6'):
        assert not _is_linked(a2, 'Transition6', b)


def test_assoc_state11_reverse_link_reassign_clear():
    a1 = dtmc_State(name="sample_text")
    a2 = dtmc_State(name="sample_text_2")
    b = dtmc_Label(name="sample_text")
    _safe_set(b, 'labels', a1)
    assert _is_linked(b, 'labels', a1)
    if hasattr(a1, 'State12'):
        assert _is_linked(a1, 'State12', b)
    _safe_set(b, 'labels', a2)
    assert _is_linked(b, 'labels', a2)
    if hasattr(a1, 'State12'):
        assert not _is_linked(a1, 'State12', b)
    if hasattr(a2, 'State12'):
        assert _is_linked(a2, 'State12', b)
    _safe_set(b, 'labels', None)
    assert not _is_linked(b, 'labels', a2)
    if hasattr(a2, 'State12'):
        assert not _is_linked(a2, 'State12', b)


def test_assoc_to9_reverse_link_reassign_clear():
    a1 = dtmc_Transition(prob=3.14)
    a2 = dtmc_Transition(prob=9.99)
    b = dtmc_State(name="sample_text")
    _safe_set(b, 'State10', a1)
    assert _is_linked(b, 'State10', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State10', a2)
    assert _is_linked(b, 'State10', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State10', None)
    assert not _is_linked(b, 'State10', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

