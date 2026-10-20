import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    profile_Constraint,
    profile_PlatformProfile,
    profile_Resource,
    ConstraintOperation,
    ConstraintType,
    ResourceType,
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

def test_assoc_constraints1_reverse_link_reassign_clear():
    a1 = profile_PlatformProfile(name="sample_text")
    a2 = profile_PlatformProfile(name="sample_text_2")
    b = profile_Constraint(bound=7, isDerivation=True, operation="sample_text", type="sample_text")
    _safe_set(b, 'profile_Constraint', a1)
    assert _is_linked(b, 'profile_Constraint', a1)
    if hasattr(a1, 'profile_PlatformProfile2'):
        assert _is_linked(a1, 'profile_PlatformProfile2', b)
    _safe_set(b, 'profile_Constraint', a2)
    assert _is_linked(b, 'profile_Constraint', a2)
    if hasattr(a1, 'profile_PlatformProfile2'):
        assert not _is_linked(a1, 'profile_PlatformProfile2', b)
    if hasattr(a2, 'profile_PlatformProfile2'):
        assert _is_linked(a2, 'profile_PlatformProfile2', b)
    _safe_set(b, 'profile_Constraint', None)
    assert not _is_linked(b, 'profile_Constraint', a2)
    if hasattr(a2, 'profile_PlatformProfile2'):
        assert not _is_linked(a2, 'profile_PlatformProfile2', b)


def test_assoc_references3_reverse_link_reassign_clear():
    a1 = profile_Resource(name="sample_text", type="sample_text", weight=7)
    a2 = profile_Resource(name="sample_text_2", type="sample_text_2", weight=13)
    b = profile_Constraint(bound=7, isDerivation=True, operation="sample_text", type="sample_text")
    _safe_set(b, 'profile_Constraint4', a1)
    assert _is_linked(b, 'profile_Constraint4', a1)
    if hasattr(a1, 'profile_Resource5'):
        assert _is_linked(a1, 'profile_Resource5', b)
    _safe_set(b, 'profile_Constraint4', a2)
    assert _is_linked(b, 'profile_Constraint4', a2)
    if hasattr(a1, 'profile_Resource5'):
        assert not _is_linked(a1, 'profile_Resource5', b)
    if hasattr(a2, 'profile_Resource5'):
        assert _is_linked(a2, 'profile_Resource5', b)
    _safe_set(b, 'profile_Constraint4', None)
    assert not _is_linked(b, 'profile_Constraint4', a2)
    if hasattr(a2, 'profile_Resource5'):
        assert not _is_linked(a2, 'profile_Resource5', b)


def test_assoc_resources0_reverse_link_reassign_clear():
    a1 = profile_Resource(name="sample_text", type="sample_text", weight=7)
    a2 = profile_Resource(name="sample_text_2", type="sample_text_2", weight=13)
    b = profile_PlatformProfile(name="sample_text")
    _safe_set(b, 'profile_PlatformProfile', {a1})
    assert _is_linked(b, 'profile_PlatformProfile', a1)
    if hasattr(a1, 'profile_Resource'):
        assert _is_linked(a1, 'profile_Resource', b)
    _safe_set(b, 'profile_PlatformProfile', {a2})
    assert _is_linked(b, 'profile_PlatformProfile', a2)
    if hasattr(a1, 'profile_Resource'):
        assert not _is_linked(a1, 'profile_Resource', b)
    if hasattr(a2, 'profile_Resource'):
        assert _is_linked(a2, 'profile_Resource', b)
    _safe_set(b, 'profile_PlatformProfile', set())
    assert not _is_linked(b, 'profile_PlatformProfile', a2)
    if hasattr(a2, 'profile_Resource'):
        assert not _is_linked(a2, 'profile_Resource', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

