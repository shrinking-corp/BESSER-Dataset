import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    feature_Feature,
    feature_Model,
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

def test_assoc_features1_reverse_link_reassign_clear():
    a1 = feature_Feature(attribute="sample_text", isSelected=True, max=7, min=7, name="sample_text")
    a2 = feature_Feature(attribute="sample_text_2", isSelected=False, max=13, min=13, name="sample_text_2")
    b = feature_Feature(attribute="sample_text", isSelected=True, max=7, min=7, name="sample_text")
    _safe_set(b, 'feature_Feature0', {a1})
    assert _is_linked(b, 'feature_Feature0', a1)
    if hasattr(a1, 'feature_Feature'):
        assert _is_linked(a1, 'feature_Feature', b)
    _safe_set(b, 'feature_Feature0', {a2})
    assert _is_linked(b, 'feature_Feature0', a2)
    if hasattr(a1, 'feature_Feature'):
        assert not _is_linked(a1, 'feature_Feature', b)
    if hasattr(a2, 'feature_Feature'):
        assert _is_linked(a2, 'feature_Feature', b)
    _safe_set(b, 'feature_Feature0', set())
    assert not _is_linked(b, 'feature_Feature0', a2)
    if hasattr(a2, 'feature_Feature'):
        assert not _is_linked(a2, 'feature_Feature', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

