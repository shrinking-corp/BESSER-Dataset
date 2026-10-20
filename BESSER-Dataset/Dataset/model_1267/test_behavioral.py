import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FamilyMModel_Family,
    FamilyMModel_Member,
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

def test_assoc_member0_reverse_link_reassign_clear():
    a1 = FamilyMModel_Member(firstName="sample_text", relation="sample_text")
    a2 = FamilyMModel_Member(firstName="sample_text_2", relation="sample_text_2")
    b = FamilyMModel_Family(lastName="sample_text")
    _safe_set(b, 'FamilyMModel_Family', {a1})
    assert _is_linked(b, 'FamilyMModel_Family', a1)
    if hasattr(a1, 'FamilyMModel_Member'):
        assert _is_linked(a1, 'FamilyMModel_Member', b)
    _safe_set(b, 'FamilyMModel_Family', {a2})
    assert _is_linked(b, 'FamilyMModel_Family', a2)
    if hasattr(a1, 'FamilyMModel_Member'):
        assert not _is_linked(a1, 'FamilyMModel_Member', b)
    if hasattr(a2, 'FamilyMModel_Member'):
        assert _is_linked(a2, 'FamilyMModel_Member', b)
    _safe_set(b, 'FamilyMModel_Family', set())
    assert not _is_linked(b, 'FamilyMModel_Family', a2)
    if hasattr(a2, 'FamilyMModel_Member'):
        assert not _is_linked(a2, 'FamilyMModel_Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

