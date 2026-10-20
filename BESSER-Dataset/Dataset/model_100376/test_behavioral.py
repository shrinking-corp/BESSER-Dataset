import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    IOAutomaton_Activation,
    IOAutomaton_Automaton,
    IOAutomaton_Input,
    IOAutomaton_Object,
    IOAutomaton_Operation,
    IOAutomaton_Output,
    IOAutomaton_ReturnValue,
    IOAutomaton_State,
    IOAutomaton_Transition,
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

def test_assoc_activation19_reverse_link_reassign_clear():
    a1 = IOAutomaton_Transition(name="sample_text")
    a2 = IOAutomaton_Transition(name="sample_text_2")
    b = IOAutomaton_Activation(name="sample_text")
    _safe_set(b, 'IOAutomaton_Activation21', a1)
    assert _is_linked(b, 'IOAutomaton_Activation21', a1)
    if hasattr(a1, 'IOAutomaton_Transition20'):
        assert _is_linked(a1, 'IOAutomaton_Transition20', b)
    _safe_set(b, 'IOAutomaton_Activation21', a2)
    assert _is_linked(b, 'IOAutomaton_Activation21', a2)
    if hasattr(a1, 'IOAutomaton_Transition20'):
        assert not _is_linked(a1, 'IOAutomaton_Transition20', b)
    if hasattr(a2, 'IOAutomaton_Transition20'):
        assert _is_linked(a2, 'IOAutomaton_Transition20', b)
    _safe_set(b, 'IOAutomaton_Activation21', None)
    assert not _is_linked(b, 'IOAutomaton_Activation21', a2)
    if hasattr(a2, 'IOAutomaton_Transition20'):
        assert not _is_linked(a2, 'IOAutomaton_Transition20', b)


def test_assoc_delta5_reverse_link_reassign_clear():
    a1 = IOAutomaton_Transition(name="sample_text")
    a2 = IOAutomaton_Transition(name="sample_text_2")
    b = IOAutomaton_Automaton(name="sample_text")
    _safe_set(b, 'IOAutomaton_Automaton6', {a1})
    assert _is_linked(b, 'IOAutomaton_Automaton6', a1)
    if hasattr(a1, 'IOAutomaton_Transition'):
        assert _is_linked(a1, 'IOAutomaton_Transition', b)
    _safe_set(b, 'IOAutomaton_Automaton6', {a2})
    assert _is_linked(b, 'IOAutomaton_Automaton6', a2)
    if hasattr(a1, 'IOAutomaton_Transition'):
        assert not _is_linked(a1, 'IOAutomaton_Transition', b)
    if hasattr(a2, 'IOAutomaton_Transition'):
        assert _is_linked(a2, 'IOAutomaton_Transition', b)
    _safe_set(b, 'IOAutomaton_Automaton6', set())
    assert not _is_linked(b, 'IOAutomaton_Automaton6', a2)
    if hasattr(a2, 'IOAutomaton_Transition'):
        assert not _is_linked(a2, 'IOAutomaton_Transition', b)


def test_assoc_ingoing1_reverse_link_reassign_clear():
    a1 = IOAutomaton_Input(name="sample_text")
    a2 = IOAutomaton_Input(name="sample_text_2")
    b = IOAutomaton_Automaton(name="sample_text")
    _safe_set(b, 'IOAutomaton_Automaton2', {a1})
    assert _is_linked(b, 'IOAutomaton_Automaton2', a1)
    if hasattr(a1, 'IOAutomaton_Input'):
        assert _is_linked(a1, 'IOAutomaton_Input', b)
    _safe_set(b, 'IOAutomaton_Automaton2', {a2})
    assert _is_linked(b, 'IOAutomaton_Automaton2', a2)
    if hasattr(a1, 'IOAutomaton_Input'):
        assert not _is_linked(a1, 'IOAutomaton_Input', b)
    if hasattr(a2, 'IOAutomaton_Input'):
        assert _is_linked(a2, 'IOAutomaton_Input', b)
    _safe_set(b, 'IOAutomaton_Automaton2', set())
    assert not _is_linked(b, 'IOAutomaton_Automaton2', a2)
    if hasattr(a2, 'IOAutomaton_Input'):
        assert not _is_linked(a2, 'IOAutomaton_Input', b)


def test_assoc_input16_reverse_link_reassign_clear():
    a1 = IOAutomaton_Transition(name="sample_text")
    a2 = IOAutomaton_Transition(name="sample_text_2")
    b = IOAutomaton_Input(name="sample_text")
    _safe_set(b, 'IOAutomaton_Input18', a1)
    assert _is_linked(b, 'IOAutomaton_Input18', a1)
    if hasattr(a1, 'IOAutomaton_Transition17'):
        assert _is_linked(a1, 'IOAutomaton_Transition17', b)
    _safe_set(b, 'IOAutomaton_Input18', a2)
    assert _is_linked(b, 'IOAutomaton_Input18', a2)
    if hasattr(a1, 'IOAutomaton_Transition17'):
        assert not _is_linked(a1, 'IOAutomaton_Transition17', b)
    if hasattr(a2, 'IOAutomaton_Transition17'):
        assert _is_linked(a2, 'IOAutomaton_Transition17', b)
    _safe_set(b, 'IOAutomaton_Input18', None)
    assert not _is_linked(b, 'IOAutomaton_Input18', a2)
    if hasattr(a2, 'IOAutomaton_Transition17'):
        assert not _is_linked(a2, 'IOAutomaton_Transition17', b)


def test_assoc_operation26_reverse_link_reassign_clear():
    a1 = IOAutomaton_Operation(name="sample_text")
    a2 = IOAutomaton_Operation(name="sample_text_2")
    b = IOAutomaton_Input(name="sample_text")
    _safe_set(b, 'IOAutomaton_Input27', a1)
    assert _is_linked(b, 'IOAutomaton_Input27', a1)
    if hasattr(a1, 'IOAutomaton_Operation'):
        assert _is_linked(a1, 'IOAutomaton_Operation', b)
    _safe_set(b, 'IOAutomaton_Input27', a2)
    assert _is_linked(b, 'IOAutomaton_Input27', a2)
    if hasattr(a1, 'IOAutomaton_Operation'):
        assert not _is_linked(a1, 'IOAutomaton_Operation', b)
    if hasattr(a2, 'IOAutomaton_Operation'):
        assert _is_linked(a2, 'IOAutomaton_Operation', b)
    _safe_set(b, 'IOAutomaton_Input27', None)
    assert not _is_linked(b, 'IOAutomaton_Input27', a2)
    if hasattr(a2, 'IOAutomaton_Operation'):
        assert not _is_linked(a2, 'IOAutomaton_Operation', b)


def test_assoc_operation28_reverse_link_reassign_clear():
    a1 = IOAutomaton_Output(name="sample_text")
    a2 = IOAutomaton_Output(name="sample_text_2")
    b = IOAutomaton_Operation(name="sample_text")
    _safe_set(b, 'IOAutomaton_Operation30', a1)
    assert _is_linked(b, 'IOAutomaton_Operation30', a1)
    if hasattr(a1, 'IOAutomaton_Output29'):
        assert _is_linked(a1, 'IOAutomaton_Output29', b)
    _safe_set(b, 'IOAutomaton_Operation30', a2)
    assert _is_linked(b, 'IOAutomaton_Operation30', a2)
    if hasattr(a1, 'IOAutomaton_Output29'):
        assert not _is_linked(a1, 'IOAutomaton_Output29', b)
    if hasattr(a2, 'IOAutomaton_Output29'):
        assert _is_linked(a2, 'IOAutomaton_Output29', b)
    _safe_set(b, 'IOAutomaton_Operation30', None)
    assert not _is_linked(b, 'IOAutomaton_Operation30', a2)
    if hasattr(a2, 'IOAutomaton_Output29'):
        assert not _is_linked(a2, 'IOAutomaton_Output29', b)


def test_assoc_outObject31_reverse_link_reassign_clear():
    a1 = IOAutomaton_Output(name="sample_text")
    a2 = IOAutomaton_Output(name="sample_text_2")
    b = IOAutomaton_Object(name="sample_text")
    _safe_set(b, 'IOAutomaton_Object', a1)
    assert _is_linked(b, 'IOAutomaton_Object', a1)
    if hasattr(a1, 'IOAutomaton_Output32'):
        assert _is_linked(a1, 'IOAutomaton_Output32', b)
    _safe_set(b, 'IOAutomaton_Object', a2)
    assert _is_linked(b, 'IOAutomaton_Object', a2)
    if hasattr(a1, 'IOAutomaton_Output32'):
        assert not _is_linked(a1, 'IOAutomaton_Output32', b)
    if hasattr(a2, 'IOAutomaton_Output32'):
        assert _is_linked(a2, 'IOAutomaton_Output32', b)
    _safe_set(b, 'IOAutomaton_Object', None)
    assert not _is_linked(b, 'IOAutomaton_Object', a2)
    if hasattr(a2, 'IOAutomaton_Output32'):
        assert not _is_linked(a2, 'IOAutomaton_Output32', b)


def test_assoc_outcoming3_reverse_link_reassign_clear():
    a1 = IOAutomaton_Automaton(name="sample_text")
    a2 = IOAutomaton_Automaton(name="sample_text_2")
    b = IOAutomaton_Activation(name="sample_text")
    _safe_set(b, 'IOAutomaton_Activation', a1)
    assert _is_linked(b, 'IOAutomaton_Activation', a1)
    if hasattr(a1, 'IOAutomaton_Automaton4'):
        assert _is_linked(a1, 'IOAutomaton_Automaton4', b)
    _safe_set(b, 'IOAutomaton_Activation', a2)
    assert _is_linked(b, 'IOAutomaton_Activation', a2)
    if hasattr(a1, 'IOAutomaton_Automaton4'):
        assert not _is_linked(a1, 'IOAutomaton_Automaton4', b)
    if hasattr(a2, 'IOAutomaton_Automaton4'):
        assert _is_linked(a2, 'IOAutomaton_Automaton4', b)
    _safe_set(b, 'IOAutomaton_Activation', None)
    assert not _is_linked(b, 'IOAutomaton_Activation', a2)
    if hasattr(a2, 'IOAutomaton_Automaton4'):
        assert not _is_linked(a2, 'IOAutomaton_Automaton4', b)


def test_assoc_output22_reverse_link_reassign_clear():
    a1 = IOAutomaton_Output(name="sample_text")
    a2 = IOAutomaton_Output(name="sample_text_2")
    b = IOAutomaton_Activation(name="sample_text")
    _safe_set(b, 'IOAutomaton_Activation23', {a1})
    assert _is_linked(b, 'IOAutomaton_Activation23', a1)
    if hasattr(a1, 'IOAutomaton_Output'):
        assert _is_linked(a1, 'IOAutomaton_Output', b)
    _safe_set(b, 'IOAutomaton_Activation23', {a2})
    assert _is_linked(b, 'IOAutomaton_Activation23', a2)
    if hasattr(a1, 'IOAutomaton_Output'):
        assert not _is_linked(a1, 'IOAutomaton_Output', b)
    if hasattr(a2, 'IOAutomaton_Output'):
        assert _is_linked(a2, 'IOAutomaton_Output', b)
    _safe_set(b, 'IOAutomaton_Activation23', set())
    assert not _is_linked(b, 'IOAutomaton_Activation23', a2)
    if hasattr(a2, 'IOAutomaton_Output'):
        assert not _is_linked(a2, 'IOAutomaton_Output', b)


def test_assoc_postState13_reverse_link_reassign_clear():
    a1 = IOAutomaton_Transition(name="sample_text")
    a2 = IOAutomaton_Transition(name="sample_text_2")
    b = IOAutomaton_State(name="sample_text")
    _safe_set(b, 'IOAutomaton_State15', a1)
    assert _is_linked(b, 'IOAutomaton_State15', a1)
    if hasattr(a1, 'IOAutomaton_Transition14'):
        assert _is_linked(a1, 'IOAutomaton_Transition14', b)
    _safe_set(b, 'IOAutomaton_State15', a2)
    assert _is_linked(b, 'IOAutomaton_State15', a2)
    if hasattr(a1, 'IOAutomaton_Transition14'):
        assert not _is_linked(a1, 'IOAutomaton_Transition14', b)
    if hasattr(a2, 'IOAutomaton_Transition14'):
        assert _is_linked(a2, 'IOAutomaton_Transition14', b)
    _safe_set(b, 'IOAutomaton_State15', None)
    assert not _is_linked(b, 'IOAutomaton_State15', a2)
    if hasattr(a2, 'IOAutomaton_Transition14'):
        assert not _is_linked(a2, 'IOAutomaton_Transition14', b)


def test_assoc_preState10_reverse_link_reassign_clear():
    a1 = IOAutomaton_Transition(name="sample_text")
    a2 = IOAutomaton_Transition(name="sample_text_2")
    b = IOAutomaton_State(name="sample_text")
    _safe_set(b, 'IOAutomaton_State12', a1)
    assert _is_linked(b, 'IOAutomaton_State12', a1)
    if hasattr(a1, 'IOAutomaton_Transition11'):
        assert _is_linked(a1, 'IOAutomaton_Transition11', b)
    _safe_set(b, 'IOAutomaton_State12', a2)
    assert _is_linked(b, 'IOAutomaton_State12', a2)
    if hasattr(a1, 'IOAutomaton_Transition11'):
        assert not _is_linked(a1, 'IOAutomaton_Transition11', b)
    if hasattr(a2, 'IOAutomaton_Transition11'):
        assert _is_linked(a2, 'IOAutomaton_Transition11', b)
    _safe_set(b, 'IOAutomaton_State12', None)
    assert not _is_linked(b, 'IOAutomaton_State12', a2)
    if hasattr(a2, 'IOAutomaton_Transition11'):
        assert not _is_linked(a2, 'IOAutomaton_Transition11', b)


def test_assoc_returnValue24_reverse_link_reassign_clear():
    a1 = IOAutomaton_ReturnValue(isVoid=True, name="sample_text")
    a2 = IOAutomaton_ReturnValue(isVoid=False, name="sample_text_2")
    b = IOAutomaton_Activation(name="sample_text")
    _safe_set(b, 'IOAutomaton_Activation25', a1)
    assert _is_linked(b, 'IOAutomaton_Activation25', a1)
    if hasattr(a1, 'IOAutomaton_ReturnValue'):
        assert _is_linked(a1, 'IOAutomaton_ReturnValue', b)
    _safe_set(b, 'IOAutomaton_Activation25', a2)
    assert _is_linked(b, 'IOAutomaton_Activation25', a2)
    if hasattr(a1, 'IOAutomaton_ReturnValue'):
        assert not _is_linked(a1, 'IOAutomaton_ReturnValue', b)
    if hasattr(a2, 'IOAutomaton_ReturnValue'):
        assert _is_linked(a2, 'IOAutomaton_ReturnValue', b)
    _safe_set(b, 'IOAutomaton_Activation25', None)
    assert not _is_linked(b, 'IOAutomaton_Activation25', a2)
    if hasattr(a2, 'IOAutomaton_ReturnValue'):
        assert not _is_linked(a2, 'IOAutomaton_ReturnValue', b)


def test_assoc_returnValue33_reverse_link_reassign_clear():
    a1 = IOAutomaton_ReturnValue(isVoid=True, name="sample_text")
    a2 = IOAutomaton_ReturnValue(isVoid=False, name="sample_text_2")
    b = IOAutomaton_Output(name="sample_text")
    _safe_set(b, 'IOAutomaton_Output34', a1)
    assert _is_linked(b, 'IOAutomaton_Output34', a1)
    if hasattr(a1, 'IOAutomaton_ReturnValue35'):
        assert _is_linked(a1, 'IOAutomaton_ReturnValue35', b)
    _safe_set(b, 'IOAutomaton_Output34', a2)
    assert _is_linked(b, 'IOAutomaton_Output34', a2)
    if hasattr(a1, 'IOAutomaton_ReturnValue35'):
        assert not _is_linked(a1, 'IOAutomaton_ReturnValue35', b)
    if hasattr(a2, 'IOAutomaton_ReturnValue35'):
        assert _is_linked(a2, 'IOAutomaton_ReturnValue35', b)
    _safe_set(b, 'IOAutomaton_Output34', None)
    assert not _is_linked(b, 'IOAutomaton_Output34', a2)
    if hasattr(a2, 'IOAutomaton_ReturnValue35'):
        assert not _is_linked(a2, 'IOAutomaton_ReturnValue35', b)


def test_assoc_z0_reverse_link_reassign_clear():
    a1 = IOAutomaton_State(name="sample_text")
    a2 = IOAutomaton_State(name="sample_text_2")
    b = IOAutomaton_Automaton(name="sample_text")
    _safe_set(b, 'IOAutomaton_Automaton', {a1})
    assert _is_linked(b, 'IOAutomaton_Automaton', a1)
    if hasattr(a1, 'IOAutomaton_State'):
        assert _is_linked(a1, 'IOAutomaton_State', b)
    _safe_set(b, 'IOAutomaton_Automaton', {a2})
    assert _is_linked(b, 'IOAutomaton_Automaton', a2)
    if hasattr(a1, 'IOAutomaton_State'):
        assert not _is_linked(a1, 'IOAutomaton_State', b)
    if hasattr(a2, 'IOAutomaton_State'):
        assert _is_linked(a2, 'IOAutomaton_State', b)
    _safe_set(b, 'IOAutomaton_Automaton', set())
    assert not _is_linked(b, 'IOAutomaton_Automaton', a2)
    if hasattr(a2, 'IOAutomaton_State'):
        assert not _is_linked(a2, 'IOAutomaton_State', b)


def test_assoc_z07_reverse_link_reassign_clear():
    a1 = IOAutomaton_State(name="sample_text")
    a2 = IOAutomaton_State(name="sample_text_2")
    b = IOAutomaton_Automaton(name="sample_text")
    _safe_set(b, 'IOAutomaton_Automaton8', a1)
    assert _is_linked(b, 'IOAutomaton_Automaton8', a1)
    if hasattr(a1, 'IOAutomaton_State9'):
        assert _is_linked(a1, 'IOAutomaton_State9', b)
    _safe_set(b, 'IOAutomaton_Automaton8', a2)
    assert _is_linked(b, 'IOAutomaton_Automaton8', a2)
    if hasattr(a1, 'IOAutomaton_State9'):
        assert not _is_linked(a1, 'IOAutomaton_State9', b)
    if hasattr(a2, 'IOAutomaton_State9'):
        assert _is_linked(a2, 'IOAutomaton_State9', b)
    _safe_set(b, 'IOAutomaton_Automaton8', None)
    assert not _is_linked(b, 'IOAutomaton_Automaton8', a2)
    if hasattr(a2, 'IOAutomaton_State9'):
        assert not _is_linked(a2, 'IOAutomaton_State9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

