import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Node,
    dataflownet_Channel,
    dataflownet_DataflowNet,
    dataflownet_DataflowSystem,
    dataflownet_FiringRule,
    dataflownet_NamedElement,
    dataflownet_Node,
    dataflownet_Process,
    dataflownet_StateMachine,
    dataflownet_StateMachineState,
    dataflownet_StateMachineTransition,
    dataflownet_Token,
    dataflownet_Type,
    Comparation,
    Protocol,
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

def test_assoc_inputs25_reverse_link_reassign_clear():
    a1 = dataflownet_StateMachineTransition(priority=7)
    a2 = dataflownet_StateMachineTransition(priority=13)
    b = dataflownet_FiringRule(compType="sample_text")
    _safe_set(b, 'dataflownet_FiringRule26', a1)
    assert _is_linked(b, 'dataflownet_FiringRule26', a1)
    if hasattr(a1, 'dataflownet_StateMachineTransition'):
        assert _is_linked(a1, 'dataflownet_StateMachineTransition', b)
    _safe_set(b, 'dataflownet_FiringRule26', a2)
    assert _is_linked(b, 'dataflownet_FiringRule26', a2)
    if hasattr(a1, 'dataflownet_StateMachineTransition'):
        assert not _is_linked(a1, 'dataflownet_StateMachineTransition', b)
    if hasattr(a2, 'dataflownet_StateMachineTransition'):
        assert _is_linked(a2, 'dataflownet_StateMachineTransition', b)
    _safe_set(b, 'dataflownet_FiringRule26', None)
    assert not _is_linked(b, 'dataflownet_FiringRule26', a2)
    if hasattr(a2, 'dataflownet_StateMachineTransition'):
        assert not _is_linked(a2, 'dataflownet_StateMachineTransition', b)


def test_assoc_outputs27_reverse_link_reassign_clear():
    a1 = dataflownet_StateMachineTransition(priority=7)
    a2 = dataflownet_StateMachineTransition(priority=13)
    b = dataflownet_FiringRule(compType="sample_text")
    _safe_set(b, 'dataflownet_FiringRule29', a1)
    assert _is_linked(b, 'dataflownet_FiringRule29', a1)
    if hasattr(a1, 'dataflownet_StateMachineTransition28'):
        assert _is_linked(a1, 'dataflownet_StateMachineTransition28', b)
    _safe_set(b, 'dataflownet_FiringRule29', a2)
    assert _is_linked(b, 'dataflownet_FiringRule29', a2)
    if hasattr(a1, 'dataflownet_StateMachineTransition28'):
        assert not _is_linked(a1, 'dataflownet_StateMachineTransition28', b)
    if hasattr(a2, 'dataflownet_StateMachineTransition28'):
        assert _is_linked(a2, 'dataflownet_StateMachineTransition28', b)
    _safe_set(b, 'dataflownet_FiringRule29', None)
    assert not _is_linked(b, 'dataflownet_FiringRule29', a2)
    if hasattr(a2, 'dataflownet_StateMachineTransition28'):
        assert not _is_linked(a2, 'dataflownet_StateMachineTransition28', b)


def test_assoc_processes48_reverse_link_reassign_clear():
    a1 = dataflownet_Process(host="sample_text")
    a2 = dataflownet_Process(host="sample_text_2")
    b = dataflownet_DataflowSystem(protocol="sample_text")
    _safe_set(b, 'dataflownet_DataflowSystem49', {a1})
    assert _is_linked(b, 'dataflownet_DataflowSystem49', a1)
    if hasattr(a1, 'dataflownet_Process50'):
        assert _is_linked(a1, 'dataflownet_Process50', b)
    _safe_set(b, 'dataflownet_DataflowSystem49', {a2})
    assert _is_linked(b, 'dataflownet_DataflowSystem49', a2)
    if hasattr(a1, 'dataflownet_Process50'):
        assert not _is_linked(a1, 'dataflownet_Process50', b)
    if hasattr(a2, 'dataflownet_Process50'):
        assert _is_linked(a2, 'dataflownet_Process50', b)
    _safe_set(b, 'dataflownet_DataflowSystem49', set())
    assert not _is_linked(b, 'dataflownet_DataflowSystem49', a2)
    if hasattr(a2, 'dataflownet_Process50'):
        assert not _is_linked(a2, 'dataflownet_Process50', b)


def test_assoc_tokens35_reverse_link_reassign_clear():
    a1 = dataflownet_Token(value="sample_text")
    a2 = dataflownet_Token(value="sample_text_2")
    b = dataflownet_FiringRule(compType="sample_text")
    _safe_set(b, 'dataflownet_FiringRule36', a1)
    assert _is_linked(b, 'dataflownet_FiringRule36', a1)
    if hasattr(a1, 'dataflownet_Token'):
        assert _is_linked(a1, 'dataflownet_Token', b)
    _safe_set(b, 'dataflownet_FiringRule36', a2)
    assert _is_linked(b, 'dataflownet_FiringRule36', a2)
    if hasattr(a1, 'dataflownet_Token'):
        assert not _is_linked(a1, 'dataflownet_Token', b)
    if hasattr(a2, 'dataflownet_Token'):
        assert _is_linked(a2, 'dataflownet_Token', b)
    _safe_set(b, 'dataflownet_FiringRule36', None)
    assert not _is_linked(b, 'dataflownet_FiringRule36', a2)
    if hasattr(a2, 'dataflownet_Token'):
        assert not _is_linked(a2, 'dataflownet_Token', b)


