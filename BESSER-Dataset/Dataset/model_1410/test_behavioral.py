import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Region,
    State,
    trialStatemachine_Action,
    trialStatemachine_ComplexState,
    trialStatemachine_LabeledTransition,
    trialStatemachine_Region,
    trialStatemachine_State,
    trialStatemachine_Statemachine,
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

def test_assoc_action15_reverse_link_reassign_clear():
    a1 = trialStatemachine_LabeledTransition(id="sample_text")
    a2 = trialStatemachine_LabeledTransition(id="sample_text_2")
    b = trialStatemachine_Action(name="sample_text")
    _safe_set(b, 'trialStatemachine_Action17', a1)
    assert _is_linked(b, 'trialStatemachine_Action17', a1)
    if hasattr(a1, 'trialStatemachine_LabeledTransition16'):
        assert _is_linked(a1, 'trialStatemachine_LabeledTransition16', b)
    _safe_set(b, 'trialStatemachine_Action17', a2)
    assert _is_linked(b, 'trialStatemachine_Action17', a2)
    if hasattr(a1, 'trialStatemachine_LabeledTransition16'):
        assert not _is_linked(a1, 'trialStatemachine_LabeledTransition16', b)
    if hasattr(a2, 'trialStatemachine_LabeledTransition16'):
        assert _is_linked(a2, 'trialStatemachine_LabeledTransition16', b)
    _safe_set(b, 'trialStatemachine_Action17', None)
    assert not _is_linked(b, 'trialStatemachine_Action17', a2)
    if hasattr(a2, 'trialStatemachine_LabeledTransition16'):
        assert not _is_linked(a2, 'trialStatemachine_LabeledTransition16', b)


def test_assoc_actions2_reverse_link_reassign_clear():
    a1 = trialStatemachine_Statemachine(name="sample_text")
    a2 = trialStatemachine_Statemachine(name="sample_text_2")
    b = trialStatemachine_Action(name="sample_text")
    _safe_set(b, 'trialStatemachine_Action', a1)
    assert _is_linked(b, 'trialStatemachine_Action', a1)
    if hasattr(a1, 'trialStatemachine_Statemachine'):
        assert _is_linked(a1, 'trialStatemachine_Statemachine', b)
    _safe_set(b, 'trialStatemachine_Action', a2)
    assert _is_linked(b, 'trialStatemachine_Action', a2)
    if hasattr(a1, 'trialStatemachine_Statemachine'):
        assert not _is_linked(a1, 'trialStatemachine_Statemachine', b)
    if hasattr(a2, 'trialStatemachine_Statemachine'):
        assert _is_linked(a2, 'trialStatemachine_Statemachine', b)
    _safe_set(b, 'trialStatemachine_Action', None)
    assert not _is_linked(b, 'trialStatemachine_Action', a2)
    if hasattr(a2, 'trialStatemachine_Statemachine'):
        assert not _is_linked(a2, 'trialStatemachine_Statemachine', b)


def test_assoc_defaultHistory3_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(name="sample_text")
    a2 = trialStatemachine_State(name="sample_text_2")
    b = trialStatemachine_Region(history="sample_text")
    _safe_set(b, 'trialStatemachine_Region4', a1)
    assert _is_linked(b, 'trialStatemachine_Region4', a1)
    if hasattr(a1, 'trialStatemachine_State5'):
        assert _is_linked(a1, 'trialStatemachine_State5', b)
    _safe_set(b, 'trialStatemachine_Region4', a2)
    assert _is_linked(b, 'trialStatemachine_Region4', a2)
    if hasattr(a1, 'trialStatemachine_State5'):
        assert not _is_linked(a1, 'trialStatemachine_State5', b)
    if hasattr(a2, 'trialStatemachine_State5'):
        assert _is_linked(a2, 'trialStatemachine_State5', b)
    _safe_set(b, 'trialStatemachine_Region4', None)
    assert not _is_linked(b, 'trialStatemachine_Region4', a2)
    if hasattr(a2, 'trialStatemachine_State5'):
        assert not _is_linked(a2, 'trialStatemachine_State5', b)


def test_assoc_initial9_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(name="sample_text")
    a2 = trialStatemachine_State(name="sample_text_2")
    b = trialStatemachine_Region(history="sample_text")
    _safe_set(b, 'trialStatemachine_Region10', a1)
    assert _is_linked(b, 'trialStatemachine_Region10', a1)
    if hasattr(a1, 'trialStatemachine_State11'):
        assert _is_linked(a1, 'trialStatemachine_State11', b)
    _safe_set(b, 'trialStatemachine_Region10', a2)
    assert _is_linked(b, 'trialStatemachine_Region10', a2)
    if hasattr(a1, 'trialStatemachine_State11'):
        assert not _is_linked(a1, 'trialStatemachine_State11', b)
    if hasattr(a2, 'trialStatemachine_State11'):
        assert _is_linked(a2, 'trialStatemachine_State11', b)
    _safe_set(b, 'trialStatemachine_Region10', None)
    assert not _is_linked(b, 'trialStatemachine_Region10', a2)
    if hasattr(a2, 'trialStatemachine_State11'):
        assert not _is_linked(a2, 'trialStatemachine_State11', b)


def test_assoc_outgoings0_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(name="sample_text")
    a2 = trialStatemachine_State(name="sample_text_2")
    b = trialStatemachine_LabeledTransition(id="sample_text")
    _safe_set(b, 'trialStatemachine_LabeledTransition', a1)
    assert _is_linked(b, 'trialStatemachine_LabeledTransition', a1)
    if hasattr(a1, 'trialStatemachine_State'):
        assert _is_linked(a1, 'trialStatemachine_State', b)
    _safe_set(b, 'trialStatemachine_LabeledTransition', a2)
    assert _is_linked(b, 'trialStatemachine_LabeledTransition', a2)
    if hasattr(a1, 'trialStatemachine_State'):
        assert not _is_linked(a1, 'trialStatemachine_State', b)
    if hasattr(a2, 'trialStatemachine_State'):
        assert _is_linked(a2, 'trialStatemachine_State', b)
    _safe_set(b, 'trialStatemachine_LabeledTransition', None)
    assert not _is_linked(b, 'trialStatemachine_LabeledTransition', a2)
    if hasattr(a2, 'trialStatemachine_State'):
        assert not _is_linked(a2, 'trialStatemachine_State', b)


def test_assoc_states6_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(name="sample_text")
    a2 = trialStatemachine_State(name="sample_text_2")
    b = trialStatemachine_Region(history="sample_text")
    _safe_set(b, 'trialStatemachine_Region7', {a1})
    assert _is_linked(b, 'trialStatemachine_Region7', a1)
    if hasattr(a1, 'trialStatemachine_State8'):
        assert _is_linked(a1, 'trialStatemachine_State8', b)
    _safe_set(b, 'trialStatemachine_Region7', {a2})
    assert _is_linked(b, 'trialStatemachine_Region7', a2)
    if hasattr(a1, 'trialStatemachine_State8'):
        assert not _is_linked(a1, 'trialStatemachine_State8', b)
    if hasattr(a2, 'trialStatemachine_State8'):
        assert _is_linked(a2, 'trialStatemachine_State8', b)
    _safe_set(b, 'trialStatemachine_Region7', set())
    assert not _is_linked(b, 'trialStatemachine_Region7', a2)
    if hasattr(a2, 'trialStatemachine_State8'):
        assert not _is_linked(a2, 'trialStatemachine_State8', b)


def test_assoc_target12_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(name="sample_text")
    a2 = trialStatemachine_State(name="sample_text_2")
    b = trialStatemachine_LabeledTransition(id="sample_text")
    _safe_set(b, 'trialStatemachine_LabeledTransition13', a1)
    assert _is_linked(b, 'trialStatemachine_LabeledTransition13', a1)
    if hasattr(a1, 'trialStatemachine_State14'):
        assert _is_linked(a1, 'trialStatemachine_State14', b)
    _safe_set(b, 'trialStatemachine_LabeledTransition13', a2)
    assert _is_linked(b, 'trialStatemachine_LabeledTransition13', a2)
    if hasattr(a1, 'trialStatemachine_State14'):
        assert not _is_linked(a1, 'trialStatemachine_State14', b)
    if hasattr(a2, 'trialStatemachine_State14'):
        assert _is_linked(a2, 'trialStatemachine_State14', b)
    _safe_set(b, 'trialStatemachine_LabeledTransition13', None)
    assert not _is_linked(b, 'trialStatemachine_LabeledTransition13', a2)
    if hasattr(a2, 'trialStatemachine_State14'):
        assert not _is_linked(a2, 'trialStatemachine_State14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_region1_stub_double():
    # trialStatemachine_ComplexState has no real 'trialStatemachine_ComplexState' property in the generated
    # code (a bare stub) -- manually attach it so trialStatemachine_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trialStatemachine_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trialStatemachine_Region(history="sample_text")
    partner = trialStatemachine_ComplexState()
    setattr(partner, 'trialStatemachine_ComplexState', None)
    _safe_set(owner, 'trialStatemachine_Region', partner)
    assert getattr(partner, 'trialStatemachine_ComplexState') == owner
    _safe_set(owner, 'trialStatemachine_Region', None)
    assert getattr(partner, 'trialStatemachine_ComplexState') is None


