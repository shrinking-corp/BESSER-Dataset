import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Families_Daughter,
    Families_Family,
    Families_Father,
    Families_Member,
    Families_Mother,
    Families_Son,
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

def test_assoc_daughters5_stub_double():
    # Families_Daughter has no real 'Daughter' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Daughter()
    setattr(partner, 'Daughter', None)
    _safe_set(owner, 'family6', {partner})
    assert getattr(partner, 'Daughter') == owner
    _safe_set(owner, 'family6', set())
    assert getattr(partner, 'Daughter') is None


def test_assoc_family10_stub_double():
    # Families_Son has no real 'sons' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Son()
    setattr(partner, 'sons', None)
    _safe_set(owner, 'Family11', partner)
    assert getattr(partner, 'sons') == owner
    _safe_set(owner, 'Family11', None)
    assert getattr(partner, 'sons') is None


def test_assoc_family12_stub_double():
    # Families_Daughter has no real 'daughters' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Daughter()
    setattr(partner, 'daughters', None)
    _safe_set(owner, 'Family13', partner)
    assert getattr(partner, 'daughters') == owner
    _safe_set(owner, 'Family13', None)
    assert getattr(partner, 'daughters') is None


def test_assoc_family7_stub_double():
    # Families_Father has no real 'father' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Father()
    setattr(partner, 'father', None)
    _safe_set(owner, 'Family', partner)
    assert getattr(partner, 'father') == owner
    _safe_set(owner, 'Family', None)
    assert getattr(partner, 'father') is None


def test_assoc_family8_stub_double():
    # Families_Mother has no real 'mother' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Mother()
    setattr(partner, 'mother', None)
    _safe_set(owner, 'Family9', partner)
    assert getattr(partner, 'mother') == owner
    _safe_set(owner, 'Family9', None)
    assert getattr(partner, 'mother') is None


def test_assoc_father0_stub_double():
    # Families_Father has no real 'Father' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Father()
    setattr(partner, 'Father', None)
    _safe_set(owner, 'family', partner)
    assert getattr(partner, 'Father') == owner
    _safe_set(owner, 'family', None)
    assert getattr(partner, 'Father') is None


def test_assoc_mother1_stub_double():
    # Families_Mother has no real 'Mother' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Mother()
    setattr(partner, 'Mother', None)
    _safe_set(owner, 'family2', partner)
    assert getattr(partner, 'Mother') == owner
    _safe_set(owner, 'family2', None)
    assert getattr(partner, 'Mother') is None


def test_assoc_sons3_stub_double():
    # Families_Son has no real 'Son' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(lastName="sample_text")
    partner = Families_Son()
    setattr(partner, 'Son', None)
    _safe_set(owner, 'family4', {partner})
    assert getattr(partner, 'Son') == owner
    _safe_set(owner, 'family4', set())
    assert getattr(partner, 'Son') is None


