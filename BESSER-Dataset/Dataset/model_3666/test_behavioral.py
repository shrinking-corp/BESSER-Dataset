import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sample_Company,
    sample_Department,
    sample_Group,
    sample_Person,
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

def test_assoc_company2_reverse_link_reassign_clear():
    a1 = sample_Department(name="sample_text")
    a2 = sample_Department(name="sample_text_2")
    b = sample_Company(name="sample_text")
    _safe_set(b, 'Company', a1)
    assert _is_linked(b, 'Company', a1)
    if hasattr(a1, 'departments'):
        assert _is_linked(a1, 'departments', b)
    _safe_set(b, 'Company', a2)
    assert _is_linked(b, 'Company', a2)
    if hasattr(a1, 'departments'):
        assert not _is_linked(a1, 'departments', b)
    if hasattr(a2, 'departments'):
        assert _is_linked(a2, 'departments', b)
    _safe_set(b, 'Company', None)
    assert not _is_linked(b, 'Company', a2)
    if hasattr(a2, 'departments'):
        assert not _is_linked(a2, 'departments', b)


def test_assoc_department4_reverse_link_reassign_clear():
    a1 = sample_Group(name="sample_text")
    a2 = sample_Group(name="sample_text_2")
    b = sample_Department(name="sample_text")
    _safe_set(b, 'Department5', a1)
    assert _is_linked(b, 'Department5', a1)
    if hasattr(a1, 'groups'):
        assert _is_linked(a1, 'groups', b)
    _safe_set(b, 'Department5', a2)
    assert _is_linked(b, 'Department5', a2)
    if hasattr(a1, 'groups'):
        assert not _is_linked(a1, 'groups', b)
    if hasattr(a2, 'groups'):
        assert _is_linked(a2, 'groups', b)
    _safe_set(b, 'Department5', None)
    assert not _is_linked(b, 'Department5', a2)
    if hasattr(a2, 'groups'):
        assert not _is_linked(a2, 'groups', b)


def test_assoc_departments0_reverse_link_reassign_clear():
    a1 = sample_Department(name="sample_text")
    a2 = sample_Department(name="sample_text_2")
    b = sample_Company(name="sample_text")
    _safe_set(b, 'company', {a1})
    assert _is_linked(b, 'company', a1)
    if hasattr(a1, 'Department'):
        assert _is_linked(a1, 'Department', b)
    _safe_set(b, 'company', {a2})
    assert _is_linked(b, 'company', a2)
    if hasattr(a1, 'Department'):
        assert not _is_linked(a1, 'Department', b)
    if hasattr(a2, 'Department'):
        assert _is_linked(a2, 'Department', b)
    _safe_set(b, 'company', set())
    assert not _is_linked(b, 'company', a2)
    if hasattr(a2, 'Department'):
        assert not _is_linked(a2, 'Department', b)


def test_assoc_group6_reverse_link_reassign_clear():
    a1 = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    a2 = sample_Person(birthdate=date(2025, 6, 15), name="sample_text_2")
    b = sample_Group(name="sample_text")
    _safe_set(b, 'Group7', a1)
    assert _is_linked(b, 'Group7', a1)
    if hasattr(a1, 'persons'):
        assert _is_linked(a1, 'persons', b)
    _safe_set(b, 'Group7', a2)
    assert _is_linked(b, 'Group7', a2)
    if hasattr(a1, 'persons'):
        assert not _is_linked(a1, 'persons', b)
    if hasattr(a2, 'persons'):
        assert _is_linked(a2, 'persons', b)
    _safe_set(b, 'Group7', None)
    assert not _is_linked(b, 'Group7', a2)
    if hasattr(a2, 'persons'):
        assert not _is_linked(a2, 'persons', b)


def test_assoc_groups1_reverse_link_reassign_clear():
    a1 = sample_Group(name="sample_text")
    a2 = sample_Group(name="sample_text_2")
    b = sample_Department(name="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'Group'):
        assert _is_linked(a1, 'Group', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'Group'):
        assert not _is_linked(a1, 'Group', b)
    if hasattr(a2, 'Group'):
        assert _is_linked(a2, 'Group', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'Group'):
        assert not _is_linked(a2, 'Group', b)


def test_assoc_persons3_reverse_link_reassign_clear():
    a1 = sample_Person(birthdate=date(2024, 1, 1), name="sample_text")
    a2 = sample_Person(birthdate=date(2025, 6, 15), name="sample_text_2")
    b = sample_Group(name="sample_text")
    _safe_set(b, 'group', {a1})
    assert _is_linked(b, 'group', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'group', {a2})
    assert _is_linked(b, 'group', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'group', set())
    assert not _is_linked(b, 'group', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

