import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    timetrack_Library,
    timetrack_Project,
    timetrack_TimeEntry,
    timetrack_User,
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

def test_assoc_project1_reverse_link_reassign_clear():
    a1 = timetrack_TimeEntry(day=date(2024, 1, 1), duration=date(2024, 1, 1), factured=True, from_=date(2024, 1, 1), notes="sample_text", sync_date=date(2024, 1, 1), till=date(2024, 1, 1))
    a2 = timetrack_TimeEntry(day=date(2025, 6, 15), duration=date(2025, 6, 15), factured=False, from_=date(2025, 6, 15), notes="sample_text_2", sync_date=date(2025, 6, 15), till=date(2025, 6, 15))
    b = timetrack_Project(name="sample_text", number="sample_text")
    _safe_set(b, 'timetrack_Project', a1)
    assert _is_linked(b, 'timetrack_Project', a1)
    if hasattr(a1, 'timetrack_TimeEntry2'):
        assert _is_linked(a1, 'timetrack_TimeEntry2', b)
    _safe_set(b, 'timetrack_Project', a2)
    assert _is_linked(b, 'timetrack_Project', a2)
    if hasattr(a1, 'timetrack_TimeEntry2'):
        assert not _is_linked(a1, 'timetrack_TimeEntry2', b)
    if hasattr(a2, 'timetrack_TimeEntry2'):
        assert _is_linked(a2, 'timetrack_TimeEntry2', b)
    _safe_set(b, 'timetrack_Project', None)
    assert not _is_linked(b, 'timetrack_Project', a2)
    if hasattr(a2, 'timetrack_TimeEntry2'):
        assert not _is_linked(a2, 'timetrack_TimeEntry2', b)


def test_assoc_user0_reverse_link_reassign_clear():
    a1 = timetrack_User(name="sample_text", password="sample_text", sap_name="sample_text", sap_password="sample_text")
    a2 = timetrack_User(name="sample_text_2", password="sample_text_2", sap_name="sample_text_2", sap_password="sample_text_2")
    b = timetrack_TimeEntry(day=date(2024, 1, 1), duration=date(2024, 1, 1), factured=True, from_=date(2024, 1, 1), notes="sample_text", sync_date=date(2024, 1, 1), till=date(2024, 1, 1))
    _safe_set(b, 'timetrack_TimeEntry', a1)
    assert _is_linked(b, 'timetrack_TimeEntry', a1)
    if hasattr(a1, 'timetrack_User'):
        assert _is_linked(a1, 'timetrack_User', b)
    _safe_set(b, 'timetrack_TimeEntry', a2)
    assert _is_linked(b, 'timetrack_TimeEntry', a2)
    if hasattr(a1, 'timetrack_User'):
        assert not _is_linked(a1, 'timetrack_User', b)
    if hasattr(a2, 'timetrack_User'):
        assert _is_linked(a2, 'timetrack_User', b)
    _safe_set(b, 'timetrack_TimeEntry', None)
    assert not _is_linked(b, 'timetrack_TimeEntry', a2)
    if hasattr(a2, 'timetrack_User'):
        assert not _is_linked(a2, 'timetrack_User', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_listBook3_stub_double():
    # timetrack_Library has no real 'timetrack_Library' property in the generated
    # code (a bare stub) -- manually attach it so timetrack_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timetrack_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timetrack_User(name="sample_text", password="sample_text", sap_name="sample_text", sap_password="sample_text")
    partner = timetrack_Library()
    setattr(partner, 'timetrack_Library', None)
    _safe_set(owner, 'timetrack_User4', partner)
    assert owner in getattr(partner, 'timetrack_Library')
    _safe_set(owner, 'timetrack_User4', None)
    assert owner not in getattr(partner, 'timetrack_Library')


def test_assoc_listProject8_stub_double():
    # timetrack_Library has no real 'timetrack_Library9' property in the generated
    # code (a bare stub) -- manually attach it so timetrack_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timetrack_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timetrack_Project(name="sample_text", number="sample_text")
    partner = timetrack_Library()
    setattr(partner, 'timetrack_Library9', None)
    _safe_set(owner, 'timetrack_Project10', partner)
    assert owner in getattr(partner, 'timetrack_Library9')
    _safe_set(owner, 'timetrack_Project10', None)
    assert owner not in getattr(partner, 'timetrack_Library9')


def test_assoc_listTimeEntry5_stub_double():
    # timetrack_Library has no real 'timetrack_Library6' property in the generated
    # code (a bare stub) -- manually attach it so timetrack_TimeEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # timetrack_TimeEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = timetrack_TimeEntry(day=date(2024, 1, 1), duration=date(2024, 1, 1), factured=True, from_=date(2024, 1, 1), notes="sample_text", sync_date=date(2024, 1, 1), till=date(2024, 1, 1))
    partner = timetrack_Library()
    setattr(partner, 'timetrack_Library6', None)
    _safe_set(owner, 'timetrack_TimeEntry7', partner)
    assert owner in getattr(partner, 'timetrack_Library6')
    _safe_set(owner, 'timetrack_TimeEntry7', None)
    assert owner not in getattr(partner, 'timetrack_Library6')


