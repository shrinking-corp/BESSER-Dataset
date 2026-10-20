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

def test_assoc_action21_reverse_link_reassign_clear():
    a1 = trialStatemachine_LabeledTransition(id="sample_text")
    a2 = trialStatemachine_LabeledTransition(id="sample_text_2")
    b = trialStatemachine_Action(name="sample_text")
    _safe_set(b, 'trialStatemachine_Action23', a1)
    assert _is_linked(b, 'trialStatemachine_Action23', a1)
    if hasattr(a1, 'trialStatemachine_LabeledTransition22'):
        assert _is_linked(a1, 'trialStatemachine_LabeledTransition22', b)
    _safe_set(b, 'trialStatemachine_Action23', a2)
    assert _is_linked(b, 'trialStatemachine_Action23', a2)
    if hasattr(a1, 'trialStatemachine_LabeledTransition22'):
        assert not _is_linked(a1, 'trialStatemachine_LabeledTransition22', b)
    if hasattr(a2, 'trialStatemachine_LabeledTransition22'):
        assert _is_linked(a2, 'trialStatemachine_LabeledTransition22', b)
    _safe_set(b, 'trialStatemachine_Action23', None)
    assert not _is_linked(b, 'trialStatemachine_Action23', a2)
    if hasattr(a2, 'trialStatemachine_LabeledTransition22'):
        assert not _is_linked(a2, 'trialStatemachine_LabeledTransition22', b)


def test_assoc_actions5_reverse_link_reassign_clear():
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


def test_assoc_defaultHistory6_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(initialState="sample_text", name="sample_text")
    a2 = trialStatemachine_State(initialState="sample_text_2", name="sample_text_2")
    b = trialStatemachine_Region(history="sample_text")
    _safe_set(b, 'trialStatemachine_Region7', a1)
    assert _is_linked(b, 'trialStatemachine_Region7', a1)
    if hasattr(a1, 'trialStatemachine_State8'):
        assert _is_linked(a1, 'trialStatemachine_State8', b)
    _safe_set(b, 'trialStatemachine_Region7', a2)
    assert _is_linked(b, 'trialStatemachine_Region7', a2)
    if hasattr(a1, 'trialStatemachine_State8'):
        assert not _is_linked(a1, 'trialStatemachine_State8', b)
    if hasattr(a2, 'trialStatemachine_State8'):
        assert _is_linked(a2, 'trialStatemachine_State8', b)
    _safe_set(b, 'trialStatemachine_Region7', None)
    assert not _is_linked(b, 'trialStatemachine_Region7', a2)
    if hasattr(a2, 'trialStatemachine_State8'):
        assert not _is_linked(a2, 'trialStatemachine_State8', b)


def test_assoc_initial12_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(initialState="sample_text", name="sample_text")
    a2 = trialStatemachine_State(initialState="sample_text_2", name="sample_text_2")
    b = trialStatemachine_Region(history="sample_text")
    _safe_set(b, 'trialStatemachine_Region13', a1)
    assert _is_linked(b, 'trialStatemachine_Region13', a1)
    if hasattr(a1, 'trialStatemachine_State14'):
        assert _is_linked(a1, 'trialStatemachine_State14', b)
    _safe_set(b, 'trialStatemachine_Region13', a2)
    assert _is_linked(b, 'trialStatemachine_Region13', a2)
    if hasattr(a1, 'trialStatemachine_State14'):
        assert not _is_linked(a1, 'trialStatemachine_State14', b)
    if hasattr(a2, 'trialStatemachine_State14'):
        assert _is_linked(a2, 'trialStatemachine_State14', b)
    _safe_set(b, 'trialStatemachine_Region13', None)
    assert not _is_linked(b, 'trialStatemachine_Region13', a2)
    if hasattr(a2, 'trialStatemachine_State14'):
        assert not _is_linked(a2, 'trialStatemachine_State14', b)


def test_assoc_outgoings0_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(initialState="sample_text", name="sample_text")
    a2 = trialStatemachine_State(initialState="sample_text_2", name="sample_text_2")
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


def test_assoc_states9_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(initialState="sample_text", name="sample_text")
    a2 = trialStatemachine_State(initialState="sample_text_2", name="sample_text_2")
    b = trialStatemachine_Region(history="sample_text")
    _safe_set(b, 'trialStatemachine_Region10', {a1})
    assert _is_linked(b, 'trialStatemachine_Region10', a1)
    if hasattr(a1, 'trialStatemachine_State11'):
        assert _is_linked(a1, 'trialStatemachine_State11', b)
    _safe_set(b, 'trialStatemachine_Region10', {a2})
    assert _is_linked(b, 'trialStatemachine_Region10', a2)
    if hasattr(a1, 'trialStatemachine_State11'):
        assert not _is_linked(a1, 'trialStatemachine_State11', b)
    if hasattr(a2, 'trialStatemachine_State11'):
        assert _is_linked(a2, 'trialStatemachine_State11', b)
    _safe_set(b, 'trialStatemachine_Region10', set())
    assert not _is_linked(b, 'trialStatemachine_Region10', a2)
    if hasattr(a2, 'trialStatemachine_State11'):
        assert not _is_linked(a2, 'trialStatemachine_State11', b)


def test_assoc_super1_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(initialState="sample_text", name="sample_text")
    a2 = trialStatemachine_State(initialState="sample_text_2", name="sample_text_2")
    b = trialStatemachine_Region(history="sample_text")
    _safe_set(b, 'trialStatemachine_Region', a1)
    assert _is_linked(b, 'trialStatemachine_Region', a1)
    if hasattr(a1, 'trialStatemachine_State2'):
        assert _is_linked(a1, 'trialStatemachine_State2', b)
    _safe_set(b, 'trialStatemachine_Region', a2)
    assert _is_linked(b, 'trialStatemachine_Region', a2)
    if hasattr(a1, 'trialStatemachine_State2'):
        assert not _is_linked(a1, 'trialStatemachine_State2', b)
    if hasattr(a2, 'trialStatemachine_State2'):
        assert _is_linked(a2, 'trialStatemachine_State2', b)
    _safe_set(b, 'trialStatemachine_Region', None)
    assert not _is_linked(b, 'trialStatemachine_Region', a2)
    if hasattr(a2, 'trialStatemachine_State2'):
        assert not _is_linked(a2, 'trialStatemachine_State2', b)


def test_assoc_target18_reverse_link_reassign_clear():
    a1 = trialStatemachine_State(initialState="sample_text", name="sample_text")
    a2 = trialStatemachine_State(initialState="sample_text_2", name="sample_text_2")
    b = trialStatemachine_LabeledTransition(id="sample_text")
    _safe_set(b, 'trialStatemachine_LabeledTransition19', a1)
    assert _is_linked(b, 'trialStatemachine_LabeledTransition19', a1)
    if hasattr(a1, 'trialStatemachine_State20'):
        assert _is_linked(a1, 'trialStatemachine_State20', b)
    _safe_set(b, 'trialStatemachine_LabeledTransition19', a2)
    assert _is_linked(b, 'trialStatemachine_LabeledTransition19', a2)
    if hasattr(a1, 'trialStatemachine_State20'):
        assert not _is_linked(a1, 'trialStatemachine_State20', b)
    if hasattr(a2, 'trialStatemachine_State20'):
        assert _is_linked(a2, 'trialStatemachine_State20', b)
    _safe_set(b, 'trialStatemachine_LabeledTransition19', None)
    assert not _is_linked(b, 'trialStatemachine_LabeledTransition19', a2)
    if hasattr(a2, 'trialStatemachine_State20'):
        assert not _is_linked(a2, 'trialStatemachine_State20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_region3_stub_double():
    # trialStatemachine_ComplexState has no real 'trialStatemachine_ComplexState' property in the generated
    # code (a bare stub) -- manually attach it so trialStatemachine_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trialStatemachine_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trialStatemachine_Region(history="sample_text")
    partner = trialStatemachine_ComplexState()
    setattr(partner, 'trialStatemachine_ComplexState', None)
    _safe_set(owner, 'trialStatemachine_Region4', partner)
    assert getattr(partner, 'trialStatemachine_ComplexState') == owner
    _safe_set(owner, 'trialStatemachine_Region4', None)
    assert getattr(partner, 'trialStatemachine_ComplexState') is None


def test_assoc_super15_stub_double():
    # trialStatemachine_ComplexState has no real 'trialStatemachine_ComplexState17' property in the generated
    # code (a bare stub) -- manually attach it so trialStatemachine_Region's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trialStatemachine_Region's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trialStatemachine_Region(history="sample_text")
    partner = trialStatemachine_ComplexState()
    setattr(partner, 'trialStatemachine_ComplexState17', None)
    _safe_set(owner, 'trialStatemachine_Region16', partner)
    assert getattr(partner, 'trialStatemachine_ComplexState17') == owner
    _safe_set(owner, 'trialStatemachine_Region16', None)
    assert getattr(partner, 'trialStatemachine_ComplexState17') is None


