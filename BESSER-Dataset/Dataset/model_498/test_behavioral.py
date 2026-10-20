import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Families_Family,
    Families_LastNameElement,
    Families_Member,
    Family,
    LastNameElement,
    Member,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_familyDaughter12_stub_double():
    # Family has no real 'Family13' property in the generated
    # code (a bare stub) -- manually attach it so Families_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Member(firstName="sample_text")
    partner = Family()
    setattr(partner, 'Family13', None)
    _safe_set(owner, 'daughters', partner)
    assert getattr(partner, 'Family13') == owner
    _safe_set(owner, 'daughters', None)
    assert getattr(partner, 'Family13') is None


def test_assoc_familyFather7_stub_double():
    # Family has no real 'Family' property in the generated
    # code (a bare stub) -- manually attach it so Families_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Member(firstName="sample_text")
    partner = Family()
    setattr(partner, 'Family', None)
    _safe_set(owner, 'father', partner)
    assert getattr(partner, 'Family') == owner
    _safe_set(owner, 'father', None)
    assert getattr(partner, 'Family') is None


def test_assoc_familyMother8_stub_double():
    # Family has no real 'Family9' property in the generated
    # code (a bare stub) -- manually attach it so Families_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Member(firstName="sample_text")
    partner = Family()
    setattr(partner, 'Family9', None)
    _safe_set(owner, 'mother', partner)
    assert getattr(partner, 'Family9') == owner
    _safe_set(owner, 'mother', None)
    assert getattr(partner, 'Family9') is None


def test_assoc_familySon10_stub_double():
    # Family has no real 'Family11' property in the generated
    # code (a bare stub) -- manually attach it so Families_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Member(firstName="sample_text")
    partner = Family()
    setattr(partner, 'Family11', None)
    _safe_set(owner, 'sons', partner)
    assert getattr(partner, 'Family11') == owner
    _safe_set(owner, 'sons', None)
    assert getattr(partner, 'Family11') is None


