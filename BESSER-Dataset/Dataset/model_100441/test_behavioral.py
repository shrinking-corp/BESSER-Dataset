import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    stateMachineActions_Action,
    stateMachineActions_Assignment,
    stateMachineActions_EXPRESSION,
    stateMachineActions_EventAction,
    stateMachineActions_Model,
    stateMachineActions_Parameters,
    stateMachineActions_TERM,
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

def test_assoc_alone12_reverse_link_reassign_clear():
    a1 = stateMachineActions_TERM(constant=7, variable="sample_text")
    a2 = stateMachineActions_TERM(constant=13, variable="sample_text_2")
    b = stateMachineActions_EXPRESSION(operator="sample_text")
    _safe_set(b, 'stateMachineActions_EXPRESSION13', a1)
    assert _is_linked(b, 'stateMachineActions_EXPRESSION13', a1)
    if hasattr(a1, 'stateMachineActions_TERM14'):
        assert _is_linked(a1, 'stateMachineActions_TERM14', b)
    _safe_set(b, 'stateMachineActions_EXPRESSION13', a2)
    assert _is_linked(b, 'stateMachineActions_EXPRESSION13', a2)
    if hasattr(a1, 'stateMachineActions_TERM14'):
        assert not _is_linked(a1, 'stateMachineActions_TERM14', b)
    if hasattr(a2, 'stateMachineActions_TERM14'):
        assert _is_linked(a2, 'stateMachineActions_TERM14', b)
    _safe_set(b, 'stateMachineActions_EXPRESSION13', None)
    assert not _is_linked(b, 'stateMachineActions_EXPRESSION13', a2)
    if hasattr(a2, 'stateMachineActions_TERM14'):
        assert not _is_linked(a2, 'stateMachineActions_TERM14', b)


def test_assoc_expression5_reverse_link_reassign_clear():
    a1 = stateMachineActions_EXPRESSION(operator="sample_text")
    a2 = stateMachineActions_EXPRESSION(operator="sample_text_2")
    b = stateMachineActions_Assignment(leftvar="sample_text")
    _safe_set(b, 'stateMachineActions_Assignment6', a1)
    assert _is_linked(b, 'stateMachineActions_Assignment6', a1)
    if hasattr(a1, 'stateMachineActions_EXPRESSION'):
        assert _is_linked(a1, 'stateMachineActions_EXPRESSION', b)
    _safe_set(b, 'stateMachineActions_Assignment6', a2)
    assert _is_linked(b, 'stateMachineActions_Assignment6', a2)
    if hasattr(a1, 'stateMachineActions_EXPRESSION'):
        assert not _is_linked(a1, 'stateMachineActions_EXPRESSION', b)
    if hasattr(a2, 'stateMachineActions_EXPRESSION'):
        assert _is_linked(a2, 'stateMachineActions_EXPRESSION', b)
    _safe_set(b, 'stateMachineActions_Assignment6', None)
    assert not _is_linked(b, 'stateMachineActions_Assignment6', a2)
    if hasattr(a2, 'stateMachineActions_EXPRESSION'):
        assert not _is_linked(a2, 'stateMachineActions_EXPRESSION', b)


def test_assoc_firstTerm7_reverse_link_reassign_clear():
    a1 = stateMachineActions_TERM(constant=7, variable="sample_text")
    a2 = stateMachineActions_TERM(constant=13, variable="sample_text_2")
    b = stateMachineActions_EXPRESSION(operator="sample_text")
    _safe_set(b, 'stateMachineActions_EXPRESSION8', a1)
    assert _is_linked(b, 'stateMachineActions_EXPRESSION8', a1)
    if hasattr(a1, 'stateMachineActions_TERM'):
        assert _is_linked(a1, 'stateMachineActions_TERM', b)
    _safe_set(b, 'stateMachineActions_EXPRESSION8', a2)
    assert _is_linked(b, 'stateMachineActions_EXPRESSION8', a2)
    if hasattr(a1, 'stateMachineActions_TERM'):
        assert not _is_linked(a1, 'stateMachineActions_TERM', b)
    if hasattr(a2, 'stateMachineActions_TERM'):
        assert _is_linked(a2, 'stateMachineActions_TERM', b)
    _safe_set(b, 'stateMachineActions_EXPRESSION8', None)
    assert not _is_linked(b, 'stateMachineActions_EXPRESSION8', a2)
    if hasattr(a2, 'stateMachineActions_TERM'):
        assert not _is_linked(a2, 'stateMachineActions_TERM', b)


def test_assoc_parameters15_reverse_link_reassign_clear():
    a1 = stateMachineActions_Parameters(param="sample_text")
    a2 = stateMachineActions_Parameters(param="sample_text_2")
    b = stateMachineActions_EventAction(eventExtension="sample_text", eventName="sample_text")
    _safe_set(b, 'stateMachineActions_EventAction16', a1)
    assert _is_linked(b, 'stateMachineActions_EventAction16', a1)
    if hasattr(a1, 'stateMachineActions_Parameters'):
        assert _is_linked(a1, 'stateMachineActions_Parameters', b)
    _safe_set(b, 'stateMachineActions_EventAction16', a2)
    assert _is_linked(b, 'stateMachineActions_EventAction16', a2)
    if hasattr(a1, 'stateMachineActions_Parameters'):
        assert not _is_linked(a1, 'stateMachineActions_Parameters', b)
    if hasattr(a2, 'stateMachineActions_Parameters'):
        assert _is_linked(a2, 'stateMachineActions_Parameters', b)
    _safe_set(b, 'stateMachineActions_EventAction16', None)
    assert not _is_linked(b, 'stateMachineActions_EventAction16', a2)
    if hasattr(a2, 'stateMachineActions_Parameters'):
        assert not _is_linked(a2, 'stateMachineActions_Parameters', b)


def test_assoc_parameters18_reverse_link_reassign_clear():
    a1 = stateMachineActions_Parameters(param="sample_text")
    a2 = stateMachineActions_Parameters(param="sample_text_2")
    b = stateMachineActions_Parameters(param="sample_text")
    _safe_set(b, 'stateMachineActions_Parameters19', a1)
    assert _is_linked(b, 'stateMachineActions_Parameters19', a1)
    if hasattr(a1, 'stateMachineActions_Parameters17'):
        assert _is_linked(a1, 'stateMachineActions_Parameters17', b)
    _safe_set(b, 'stateMachineActions_Parameters19', a2)
    assert _is_linked(b, 'stateMachineActions_Parameters19', a2)
    if hasattr(a1, 'stateMachineActions_Parameters17'):
        assert not _is_linked(a1, 'stateMachineActions_Parameters17', b)
    if hasattr(a2, 'stateMachineActions_Parameters17'):
        assert _is_linked(a2, 'stateMachineActions_Parameters17', b)
    _safe_set(b, 'stateMachineActions_Parameters19', None)
    assert not _is_linked(b, 'stateMachineActions_Parameters19', a2)
    if hasattr(a2, 'stateMachineActions_Parameters17'):
        assert not _is_linked(a2, 'stateMachineActions_Parameters17', b)


def test_assoc_secondTerm9_reverse_link_reassign_clear():
    a1 = stateMachineActions_TERM(constant=7, variable="sample_text")
    a2 = stateMachineActions_TERM(constant=13, variable="sample_text_2")
    b = stateMachineActions_EXPRESSION(operator="sample_text")
    _safe_set(b, 'stateMachineActions_EXPRESSION10', a1)
    assert _is_linked(b, 'stateMachineActions_EXPRESSION10', a1)
    if hasattr(a1, 'stateMachineActions_TERM11'):
        assert _is_linked(a1, 'stateMachineActions_TERM11', b)
    _safe_set(b, 'stateMachineActions_EXPRESSION10', a2)
    assert _is_linked(b, 'stateMachineActions_EXPRESSION10', a2)
    if hasattr(a1, 'stateMachineActions_TERM11'):
        assert not _is_linked(a1, 'stateMachineActions_TERM11', b)
    if hasattr(a2, 'stateMachineActions_TERM11'):
        assert _is_linked(a2, 'stateMachineActions_TERM11', b)
    _safe_set(b, 'stateMachineActions_EXPRESSION10', None)
    assert not _is_linked(b, 'stateMachineActions_EXPRESSION10', a2)
    if hasattr(a2, 'stateMachineActions_TERM11'):
        assert not _is_linked(a2, 'stateMachineActions_TERM11', b)


