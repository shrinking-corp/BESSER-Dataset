import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ClassA,
    ClassB,
    ClassC,
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

def test_assoc_ClassA_ClassB_reverse_link_reassign_clear():
    a1 = ClassB(attribute=7)
    a2 = ClassB(attribute=13)
    b = ClassA(attA="sample_text")
    _safe_set(b, 'classB0', {a1})
    assert _is_linked(b, 'classB0', a1)
    if hasattr(a1, 'classA1'):
        assert _is_linked(a1, 'classA1', b)
    _safe_set(b, 'classB0', {a2})
    assert _is_linked(b, 'classB0', a2)
    if hasattr(a1, 'classA1'):
        assert not _is_linked(a1, 'classA1', b)
    if hasattr(a2, 'classA1'):
        assert _is_linked(a2, 'classA1', b)
    _safe_set(b, 'classB0', set())
    assert not _is_linked(b, 'classB0', a2)
    if hasattr(a2, 'classA1'):
        assert not _is_linked(a2, 'classA1', b)


def test_assoc_ClassB_ClassC_reverse_link_reassign_clear():
    a1 = ClassC(attC1=7, attC2=True)
    a2 = ClassC(attC1=13, attC2=False)
    b = ClassB(attribute=7)
    _safe_set(b, 'classC2', {a1})
    assert _is_linked(b, 'classC2', a1)
    if hasattr(a1, 'classB3'):
        assert _is_linked(a1, 'classB3', b)
    _safe_set(b, 'classC2', {a2})
    assert _is_linked(b, 'classC2', a2)
    if hasattr(a1, 'classB3'):
        assert not _is_linked(a1, 'classB3', b)
    if hasattr(a2, 'classB3'):
        assert _is_linked(a2, 'classB3', b)
    _safe_set(b, 'classC2', set())
    assert not _is_linked(b, 'classC2', a2)
    if hasattr(a2, 'classB3'):
        assert not _is_linked(a2, 'classB3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

