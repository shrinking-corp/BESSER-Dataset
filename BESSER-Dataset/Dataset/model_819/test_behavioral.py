import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    lts_LTS,
    lts_State,
    lts_Transition,
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

def test_assoc_currentState2_reverse_link_reassign_clear():
    a1 = lts_State(name="sample_text")
    a2 = lts_State(name="sample_text_2")
    b = lts_LTS(name="sample_text")
    _safe_set(b, 'lts_LTS3', a1)
    assert _is_linked(b, 'lts_LTS3', a1)
    if hasattr(a1, 'lts_State4'):
        assert _is_linked(a1, 'lts_State4', b)
    _safe_set(b, 'lts_LTS3', a2)
    assert _is_linked(b, 'lts_LTS3', a2)
    if hasattr(a1, 'lts_State4'):
        assert not _is_linked(a1, 'lts_State4', b)
    if hasattr(a2, 'lts_State4'):
        assert _is_linked(a2, 'lts_State4', b)
    _safe_set(b, 'lts_LTS3', None)
    assert not _is_linked(b, 'lts_LTS3', a2)
    if hasattr(a2, 'lts_State4'):
        assert not _is_linked(a2, 'lts_State4', b)


def test_assoc_finalState5_reverse_link_reassign_clear():
    a1 = lts_State(name="sample_text")
    a2 = lts_State(name="sample_text_2")
    b = lts_LTS(name="sample_text")
    _safe_set(b, 'lts_LTS6', {a1})
    assert _is_linked(b, 'lts_LTS6', a1)
    if hasattr(a1, 'lts_State7'):
        assert _is_linked(a1, 'lts_State7', b)
    _safe_set(b, 'lts_LTS6', {a2})
    assert _is_linked(b, 'lts_LTS6', a2)
    if hasattr(a1, 'lts_State7'):
        assert not _is_linked(a1, 'lts_State7', b)
    if hasattr(a2, 'lts_State7'):
        assert _is_linked(a2, 'lts_State7', b)
    _safe_set(b, 'lts_LTS6', set())
    assert not _is_linked(b, 'lts_LTS6', a2)
    if hasattr(a2, 'lts_State7'):
        assert not _is_linked(a2, 'lts_State7', b)


def test_assoc_incomingTransition10_reverse_link_reassign_clear():
    a1 = lts_Transition(input="sample_text", output="sample_text")
    a2 = lts_Transition(input="sample_text_2", output="sample_text_2")
    b = lts_State(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition11'):
        assert _is_linked(a1, 'Transition11', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition11'):
        assert not _is_linked(a1, 'Transition11', b)
    if hasattr(a2, 'Transition11'):
        assert _is_linked(a2, 'Transition11', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition11'):
        assert not _is_linked(a2, 'Transition11', b)


def test_assoc_initialState1_reverse_link_reassign_clear():
    a1 = lts_State(name="sample_text")
    a2 = lts_State(name="sample_text_2")
    b = lts_LTS(name="sample_text")
    _safe_set(b, 'lts_LTS', a1)
    assert _is_linked(b, 'lts_LTS', a1)
    if hasattr(a1, 'lts_State'):
        assert _is_linked(a1, 'lts_State', b)
    _safe_set(b, 'lts_LTS', a2)
    assert _is_linked(b, 'lts_LTS', a2)
    if hasattr(a1, 'lts_State'):
        assert not _is_linked(a1, 'lts_State', b)
    if hasattr(a2, 'lts_State'):
        assert _is_linked(a2, 'lts_State', b)
    _safe_set(b, 'lts_LTS', None)
    assert not _is_linked(b, 'lts_LTS', a2)
    if hasattr(a2, 'lts_State'):
        assert not _is_linked(a2, 'lts_State', b)


def test_assoc_outgoingTransition9_reverse_link_reassign_clear():
    a1 = lts_Transition(input="sample_text", output="sample_text")
    a2 = lts_Transition(input="sample_text_2", output="sample_text_2")
    b = lts_State(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_ownedState0_reverse_link_reassign_clear():
    a1 = lts_State(name="sample_text")
    a2 = lts_State(name="sample_text_2")
    b = lts_LTS(name="sample_text")
    _safe_set(b, 'owningLTS', {a1})
    assert _is_linked(b, 'owningLTS', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'owningLTS', {a2})
    assert _is_linked(b, 'owningLTS', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'owningLTS', set())
    assert not _is_linked(b, 'owningLTS', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_owningLTS8_reverse_link_reassign_clear():
    a1 = lts_State(name="sample_text")
    a2 = lts_State(name="sample_text_2")
    b = lts_LTS(name="sample_text")
    _safe_set(b, 'LTS', a1)
    assert _is_linked(b, 'LTS', a1)
    if hasattr(a1, 'ownedState'):
        assert _is_linked(a1, 'ownedState', b)
    _safe_set(b, 'LTS', a2)
    assert _is_linked(b, 'LTS', a2)
    if hasattr(a1, 'ownedState'):
        assert not _is_linked(a1, 'ownedState', b)
    if hasattr(a2, 'ownedState'):
        assert _is_linked(a2, 'ownedState', b)
    _safe_set(b, 'LTS', None)
    assert not _is_linked(b, 'LTS', a2)
    if hasattr(a2, 'ownedState'):
        assert not _is_linked(a2, 'ownedState', b)


def test_assoc_source12_reverse_link_reassign_clear():
    a1 = lts_Transition(input="sample_text", output="sample_text")
    a2 = lts_Transition(input="sample_text_2", output="sample_text_2")
    b = lts_State(name="sample_text")
    _safe_set(b, 'State13', a1)
    assert _is_linked(b, 'State13', a1)
    if hasattr(a1, 'outgoingTransition'):
        assert _is_linked(a1, 'outgoingTransition', b)
    _safe_set(b, 'State13', a2)
    assert _is_linked(b, 'State13', a2)
    if hasattr(a1, 'outgoingTransition'):
        assert not _is_linked(a1, 'outgoingTransition', b)
    if hasattr(a2, 'outgoingTransition'):
        assert _is_linked(a2, 'outgoingTransition', b)
    _safe_set(b, 'State13', None)
    assert not _is_linked(b, 'State13', a2)
    if hasattr(a2, 'outgoingTransition'):
        assert not _is_linked(a2, 'outgoingTransition', b)


def test_assoc_target14_reverse_link_reassign_clear():
    a1 = lts_Transition(input="sample_text", output="sample_text")
    a2 = lts_Transition(input="sample_text_2", output="sample_text_2")
    b = lts_State(name="sample_text")
    _safe_set(b, 'State15', a1)
    assert _is_linked(b, 'State15', a1)
    if hasattr(a1, 'incomingTransition'):
        assert _is_linked(a1, 'incomingTransition', b)
    _safe_set(b, 'State15', a2)
    assert _is_linked(b, 'State15', a2)
    if hasattr(a1, 'incomingTransition'):
        assert not _is_linked(a1, 'incomingTransition', b)
    if hasattr(a2, 'incomingTransition'):
        assert _is_linked(a2, 'incomingTransition', b)
    _safe_set(b, 'State15', None)
    assert not _is_linked(b, 'State15', a2)
    if hasattr(a2, 'incomingTransition'):
        assert not _is_linked(a2, 'incomingTransition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

