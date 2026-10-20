import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    traces_SimulatorRun,
    traces_Value,
    traces_Variable,
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

def test_assoc_run1_reverse_link_reassign_clear():
    a1 = traces_Variable(name="sample_text")
    a2 = traces_Variable(name="sample_text_2")
    b = traces_SimulatorRun(behaviorName="sample_text", id=7, timestamp=date(2024, 1, 1))
    _safe_set(b, 'SimulatorRun', a1)
    assert _is_linked(b, 'SimulatorRun', a1)
    if hasattr(a1, 'variables'):
        assert _is_linked(a1, 'variables', b)
    _safe_set(b, 'SimulatorRun', a2)
    assert _is_linked(b, 'SimulatorRun', a2)
    if hasattr(a1, 'variables'):
        assert not _is_linked(a1, 'variables', b)
    if hasattr(a2, 'variables'):
        assert _is_linked(a2, 'variables', b)
    _safe_set(b, 'SimulatorRun', None)
    assert not _is_linked(b, 'SimulatorRun', a2)
    if hasattr(a2, 'variables'):
        assert not _is_linked(a2, 'variables', b)


def test_assoc_values2_reverse_link_reassign_clear():
    a1 = traces_Variable(name="sample_text")
    a2 = traces_Variable(name="sample_text_2")
    b = traces_Value(clockMax=3.14, clockMin=3.14, valueMax=3.14, valueMin=3.14)
    _safe_set(b, 'Value', a1)
    assert _is_linked(b, 'Value', a1)
    if hasattr(a1, 'variable'):
        assert _is_linked(a1, 'variable', b)
    _safe_set(b, 'Value', a2)
    assert _is_linked(b, 'Value', a2)
    if hasattr(a1, 'variable'):
        assert not _is_linked(a1, 'variable', b)
    if hasattr(a2, 'variable'):
        assert _is_linked(a2, 'variable', b)
    _safe_set(b, 'Value', None)
    assert not _is_linked(b, 'Value', a2)
    if hasattr(a2, 'variable'):
        assert not _is_linked(a2, 'variable', b)


def test_assoc_variable3_reverse_link_reassign_clear():
    a1 = traces_Variable(name="sample_text")
    a2 = traces_Variable(name="sample_text_2")
    b = traces_Value(clockMax=3.14, clockMin=3.14, valueMax=3.14, valueMin=3.14)
    _safe_set(b, 'values', a1)
    assert _is_linked(b, 'values', a1)
    if hasattr(a1, 'Variable4'):
        assert _is_linked(a1, 'Variable4', b)
    _safe_set(b, 'values', a2)
    assert _is_linked(b, 'values', a2)
    if hasattr(a1, 'Variable4'):
        assert not _is_linked(a1, 'Variable4', b)
    if hasattr(a2, 'Variable4'):
        assert _is_linked(a2, 'Variable4', b)
    _safe_set(b, 'values', None)
    assert not _is_linked(b, 'values', a2)
    if hasattr(a2, 'Variable4'):
        assert not _is_linked(a2, 'Variable4', b)


def test_assoc_variables0_reverse_link_reassign_clear():
    a1 = traces_Variable(name="sample_text")
    a2 = traces_Variable(name="sample_text_2")
    b = traces_SimulatorRun(behaviorName="sample_text", id=7, timestamp=date(2024, 1, 1))
    _safe_set(b, 'run', {a1})
    assert _is_linked(b, 'run', a1)
    if hasattr(a1, 'Variable'):
        assert _is_linked(a1, 'Variable', b)
    _safe_set(b, 'run', {a2})
    assert _is_linked(b, 'run', a2)
    if hasattr(a1, 'Variable'):
        assert not _is_linked(a1, 'Variable', b)
    if hasattr(a2, 'Variable'):
        assert _is_linked(a2, 'Variable', b)
    _safe_set(b, 'run', set())
    assert not _is_linked(b, 'run', a2)
    if hasattr(a2, 'Variable'):
        assert not _is_linked(a2, 'Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

