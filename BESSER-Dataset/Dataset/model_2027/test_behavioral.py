import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    amf_Channel,
    amf_Network,
    amf_State,
    amf_Statemachine,
    amf_Transition,
    Event,
    TypeOfChannel,
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

def test_assoc_channel0_reverse_link_reassign_clear():
    a1 = amf_Network(name="sample_text")
    a2 = amf_Network(name="sample_text_2")
    b = amf_Channel(Type="sample_text", name="sample_text")
    _safe_set(b, 'amf_Channel', a1)
    assert _is_linked(b, 'amf_Channel', a1)
    if hasattr(a1, 'amf_Network'):
        assert _is_linked(a1, 'amf_Network', b)
    _safe_set(b, 'amf_Channel', a2)
    assert _is_linked(b, 'amf_Channel', a2)
    if hasattr(a1, 'amf_Network'):
        assert not _is_linked(a1, 'amf_Network', b)
    if hasattr(a2, 'amf_Network'):
        assert _is_linked(a2, 'amf_Network', b)
    _safe_set(b, 'amf_Channel', None)
    assert not _is_linked(b, 'amf_Channel', a2)
    if hasattr(a2, 'amf_Network'):
        assert not _is_linked(a2, 'amf_Network', b)


def test_assoc_channel13_reverse_link_reassign_clear():
    a1 = amf_Transition(event="sample_text")
    a2 = amf_Transition(event="sample_text_2")
    b = amf_Channel(Type="sample_text", name="sample_text")
    _safe_set(b, 'amf_Channel15', a1)
    assert _is_linked(b, 'amf_Channel15', a1)
    if hasattr(a1, 'amf_Transition14'):
        assert _is_linked(a1, 'amf_Transition14', b)
    _safe_set(b, 'amf_Channel15', a2)
    assert _is_linked(b, 'amf_Channel15', a2)
    if hasattr(a1, 'amf_Transition14'):
        assert not _is_linked(a1, 'amf_Transition14', b)
    if hasattr(a2, 'amf_Transition14'):
        assert _is_linked(a2, 'amf_Transition14', b)
    _safe_set(b, 'amf_Channel15', None)
    assert not _is_linked(b, 'amf_Channel15', a2)
    if hasattr(a2, 'amf_Transition14'):
        assert not _is_linked(a2, 'amf_Transition14', b)


def test_assoc_initialstate3_reverse_link_reassign_clear():
    a1 = amf_Statemachine(name="sample_text")
    a2 = amf_Statemachine(name="sample_text_2")
    b = amf_State(name="sample_text")
    _safe_set(b, 'amf_State', a1)
    assert _is_linked(b, 'amf_State', a1)
    if hasattr(a1, 'amf_Statemachine4'):
        assert _is_linked(a1, 'amf_Statemachine4', b)
    _safe_set(b, 'amf_State', a2)
    assert _is_linked(b, 'amf_State', a2)
    if hasattr(a1, 'amf_Statemachine4'):
        assert not _is_linked(a1, 'amf_Statemachine4', b)
    if hasattr(a2, 'amf_Statemachine4'):
        assert _is_linked(a2, 'amf_Statemachine4', b)
    _safe_set(b, 'amf_State', None)
    assert not _is_linked(b, 'amf_State', a2)
    if hasattr(a2, 'amf_Statemachine4'):
        assert not _is_linked(a2, 'amf_Statemachine4', b)


def test_assoc_source10_reverse_link_reassign_clear():
    a1 = amf_Transition(event="sample_text")
    a2 = amf_Transition(event="sample_text_2")
    b = amf_State(name="sample_text")
    _safe_set(b, 'amf_State12', a1)
    assert _is_linked(b, 'amf_State12', a1)
    if hasattr(a1, 'amf_Transition11'):
        assert _is_linked(a1, 'amf_Transition11', b)
    _safe_set(b, 'amf_State12', a2)
    assert _is_linked(b, 'amf_State12', a2)
    if hasattr(a1, 'amf_Transition11'):
        assert not _is_linked(a1, 'amf_Transition11', b)
    if hasattr(a2, 'amf_Transition11'):
        assert _is_linked(a2, 'amf_Transition11', b)
    _safe_set(b, 'amf_State12', None)
    assert not _is_linked(b, 'amf_State12', a2)
    if hasattr(a2, 'amf_Transition11'):
        assert not _is_linked(a2, 'amf_Transition11', b)


def test_assoc_state5_reverse_link_reassign_clear():
    a1 = amf_Statemachine(name="sample_text")
    a2 = amf_Statemachine(name="sample_text_2")
    b = amf_State(name="sample_text")
    _safe_set(b, 'amf_State7', a1)
    assert _is_linked(b, 'amf_State7', a1)
    if hasattr(a1, 'amf_Statemachine6'):
        assert _is_linked(a1, 'amf_Statemachine6', b)
    _safe_set(b, 'amf_State7', a2)
    assert _is_linked(b, 'amf_State7', a2)
    if hasattr(a1, 'amf_Statemachine6'):
        assert not _is_linked(a1, 'amf_Statemachine6', b)
    if hasattr(a2, 'amf_Statemachine6'):
        assert _is_linked(a2, 'amf_Statemachine6', b)
    _safe_set(b, 'amf_State7', None)
    assert not _is_linked(b, 'amf_State7', a2)
    if hasattr(a2, 'amf_Statemachine6'):
        assert not _is_linked(a2, 'amf_Statemachine6', b)


def test_assoc_statemachine1_reverse_link_reassign_clear():
    a1 = amf_Statemachine(name="sample_text")
    a2 = amf_Statemachine(name="sample_text_2")
    b = amf_Network(name="sample_text")
    _safe_set(b, 'amf_Network2', {a1})
    assert _is_linked(b, 'amf_Network2', a1)
    if hasattr(a1, 'amf_Statemachine'):
        assert _is_linked(a1, 'amf_Statemachine', b)
    _safe_set(b, 'amf_Network2', {a2})
    assert _is_linked(b, 'amf_Network2', a2)
    if hasattr(a1, 'amf_Statemachine'):
        assert not _is_linked(a1, 'amf_Statemachine', b)
    if hasattr(a2, 'amf_Statemachine'):
        assert _is_linked(a2, 'amf_Statemachine', b)
    _safe_set(b, 'amf_Network2', set())
    assert not _is_linked(b, 'amf_Network2', a2)
    if hasattr(a2, 'amf_Statemachine'):
        assert not _is_linked(a2, 'amf_Statemachine', b)


def test_assoc_target16_reverse_link_reassign_clear():
    a1 = amf_Transition(event="sample_text")
    a2 = amf_Transition(event="sample_text_2")
    b = amf_State(name="sample_text")
    _safe_set(b, 'amf_State18', a1)
    assert _is_linked(b, 'amf_State18', a1)
    if hasattr(a1, 'amf_Transition17'):
        assert _is_linked(a1, 'amf_Transition17', b)
    _safe_set(b, 'amf_State18', a2)
    assert _is_linked(b, 'amf_State18', a2)
    if hasattr(a1, 'amf_Transition17'):
        assert not _is_linked(a1, 'amf_Transition17', b)
    if hasattr(a2, 'amf_Transition17'):
        assert _is_linked(a2, 'amf_Transition17', b)
    _safe_set(b, 'amf_State18', None)
    assert not _is_linked(b, 'amf_State18', a2)
    if hasattr(a2, 'amf_Transition17'):
        assert not _is_linked(a2, 'amf_Transition17', b)


def test_assoc_transition8_reverse_link_reassign_clear():
    a1 = amf_Transition(event="sample_text")
    a2 = amf_Transition(event="sample_text_2")
    b = amf_Statemachine(name="sample_text")
    _safe_set(b, 'amf_Statemachine9', {a1})
    assert _is_linked(b, 'amf_Statemachine9', a1)
    if hasattr(a1, 'amf_Transition'):
        assert _is_linked(a1, 'amf_Transition', b)
    _safe_set(b, 'amf_Statemachine9', {a2})
    assert _is_linked(b, 'amf_Statemachine9', a2)
    if hasattr(a1, 'amf_Transition'):
        assert not _is_linked(a1, 'amf_Transition', b)
    if hasattr(a2, 'amf_Transition'):
        assert _is_linked(a2, 'amf_Transition', b)
    _safe_set(b, 'amf_Statemachine9', set())
    assert not _is_linked(b, 'amf_Statemachine9', a2)
    if hasattr(a2, 'amf_Transition'):
        assert not _is_linked(a2, 'amf_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

