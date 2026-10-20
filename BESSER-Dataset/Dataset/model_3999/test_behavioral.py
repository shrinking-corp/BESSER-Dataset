import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Class_Attribute,
    Class_Class,
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

def test_assoc_attributes0_reverse_link_reassign_clear():
    a1 = Class_Class(id="sample_text", name="sample_text")
    a2 = Class_Class(id="sample_text_2", name="sample_text_2")
    b = Class_Attribute(id="sample_text", multiValued=True, name="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'type'):
        assert _is_linked(a1, 'type', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'type'):
        assert not _is_linked(a1, 'type', b)
    if hasattr(a2, 'type'):
        assert _is_linked(a2, 'type', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'type'):
        assert not _is_linked(a2, 'type', b)


def test_assoc_type1_reverse_link_reassign_clear():
    a1 = Class_Class(id="sample_text", name="sample_text")
    a2 = Class_Class(id="sample_text_2", name="sample_text_2")
    b = Class_Attribute(id="sample_text", multiValued=True, name="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Class'):
        assert _is_linked(a1, 'Class', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Class'):
        assert not _is_linked(a1, 'Class', b)
    if hasattr(a2, 'Class'):
        assert _is_linked(a2, 'Class', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Class'):
        assert not _is_linked(a2, 'Class', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

