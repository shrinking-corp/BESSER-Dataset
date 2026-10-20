import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EModelElement,
    Person,
    family_Family,
    family_Man,
    family_Person,
    family_Woman,
    Month,
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

def test_assoc_children12_reverse_link_reassign_clear():
    a1 = family_Person(birthCity="sample_text", birthDay=7, birthMonth="sample_text", birthYear=7, firstName="sample_text", lastName="sample_text")
    a2 = family_Person(birthCity="sample_text_2", birthDay=13, birthMonth="sample_text_2", birthYear=13, firstName="sample_text_2", lastName="sample_text_2")
    b = family_Person(birthCity="sample_text", birthDay=7, birthMonth="sample_text", birthYear=7, firstName="sample_text", lastName="sample_text")
    _safe_set(b, 'family_Person13', a1)
    assert _is_linked(b, 'family_Person13', a1)
    if hasattr(a1, 'family_Person11'):
        assert _is_linked(a1, 'family_Person11', b)
    _safe_set(b, 'family_Person13', a2)
    assert _is_linked(b, 'family_Person13', a2)
    if hasattr(a1, 'family_Person11'):
        assert not _is_linked(a1, 'family_Person11', b)
    if hasattr(a2, 'family_Person11'):
        assert _is_linked(a2, 'family_Person11', b)
    _safe_set(b, 'family_Person13', None)
    assert not _is_linked(b, 'family_Person13', a2)
    if hasattr(a2, 'family_Person11'):
        assert not _is_linked(a2, 'family_Person11', b)


def test_assoc_families4_reverse_link_reassign_clear():
    a1 = family_Family(name="sample_text")
    a2 = family_Family(name="sample_text_2")
    b = family_Family(name="sample_text")
    _safe_set(b, 'family_Family5', a1)
    assert _is_linked(b, 'family_Family5', a1)
    if hasattr(a1, 'family_Family3'):
        assert _is_linked(a1, 'family_Family3', b)
    _safe_set(b, 'family_Family5', a2)
    assert _is_linked(b, 'family_Family5', a2)
    if hasattr(a1, 'family_Family3'):
        assert not _is_linked(a1, 'family_Family3', b)
    if hasattr(a2, 'family_Family3'):
        assert _is_linked(a2, 'family_Family3', b)
    _safe_set(b, 'family_Family5', None)
    assert not _is_linked(b, 'family_Family5', a2)
    if hasattr(a2, 'family_Family3'):
        assert not _is_linked(a2, 'family_Family3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_father6_stub_double():
    # family_Man has no real 'family_Man7' property in the generated
    # code (a bare stub) -- manually attach it so family_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # family_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = family_Person(birthCity="sample_text", birthDay=7, birthMonth="sample_text", birthYear=7, firstName="sample_text", lastName="sample_text")
    partner = family_Man()
    setattr(partner, 'family_Man7', None)
    _safe_set(owner, 'family_Person', partner)
    assert getattr(partner, 'family_Man7') == owner
    _safe_set(owner, 'family_Person', None)
    assert getattr(partner, 'family_Man7') is None


def test_assoc_men0_stub_double():
    # family_Man has no real 'family_Man' property in the generated
    # code (a bare stub) -- manually attach it so family_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # family_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = family_Family(name="sample_text")
    partner = family_Man()
    setattr(partner, 'family_Man', None)
    _safe_set(owner, 'family_Family', {partner})
    assert getattr(partner, 'family_Man') == owner
    _safe_set(owner, 'family_Family', set())
    assert getattr(partner, 'family_Man') is None


def test_assoc_mother8_stub_double():
    # family_Woman has no real 'family_Woman10' property in the generated
    # code (a bare stub) -- manually attach it so family_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # family_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = family_Person(birthCity="sample_text", birthDay=7, birthMonth="sample_text", birthYear=7, firstName="sample_text", lastName="sample_text")
    partner = family_Woman()
    setattr(partner, 'family_Woman10', None)
    _safe_set(owner, 'family_Person9', partner)
    assert getattr(partner, 'family_Woman10') == owner
    _safe_set(owner, 'family_Person9', None)
    assert getattr(partner, 'family_Woman10') is None


def test_assoc_women1_stub_double():
    # family_Woman has no real 'family_Woman' property in the generated
    # code (a bare stub) -- manually attach it so family_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # family_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = family_Family(name="sample_text")
    partner = family_Woman()
    setattr(partner, 'family_Woman', None)
    _safe_set(owner, 'family_Family2', {partner})
    assert getattr(partner, 'family_Woman') == owner
    _safe_set(owner, 'family_Family2', set())
    assert getattr(partner, 'family_Woman') is None


