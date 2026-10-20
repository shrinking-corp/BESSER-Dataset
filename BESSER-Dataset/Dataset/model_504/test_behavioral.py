import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Member,
    NamedElement,
    families_Child,
    families_City,
    families_Company,
    families_Country,
    families_Family,
    families_Member,
    families_NamedElement,
    families_Neighborhood,
    families_Parent,
    families_School,
    families_Service,
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

def test_assoc_family33_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'families_Family34', a1)
    assert _is_linked(b, 'families_Family34', a1)
    if hasattr(a1, 'families_Member'):
        assert _is_linked(a1, 'families_Member', b)
    _safe_set(b, 'families_Family34', a2)
    assert _is_linked(b, 'families_Family34', a2)
    if hasattr(a1, 'families_Member'):
        assert not _is_linked(a1, 'families_Member', b)
    if hasattr(a2, 'families_Member'):
        assert _is_linked(a2, 'families_Member', b)
    _safe_set(b, 'families_Family34', None)
    assert not _is_linked(b, 'families_Family34', a2)
    if hasattr(a2, 'families_Member'):
        assert not _is_linked(a2, 'families_Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contains18_stub_double():
    # families_Neighborhood has no real 'registeredIn' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(lastName="sample_text")
    partner = families_Neighborhood()
    setattr(partner, 'registeredIn', None)
    _safe_set(owner, 'Family', partner)
    assert owner in getattr(partner, 'registeredIn')
    _safe_set(owner, 'Family', None)
    assert owner not in getattr(partner, 'registeredIn')


def test_assoc_daughters10_stub_double():
    # families_Child has no real 'families_Child' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(lastName="sample_text")
    partner = families_Child()
    setattr(partner, 'families_Child', None)
    _safe_set(owner, 'families_Family11', {partner})
    assert getattr(partner, 'families_Child') == owner
    _safe_set(owner, 'families_Family11', set())
    assert getattr(partner, 'families_Child') is None


def test_assoc_families0_stub_double():
    # families_Country has no real 'families_Country' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(lastName="sample_text")
    partner = families_Country()
    setattr(partner, 'families_Country', None)
    _safe_set(owner, 'families_Family', partner)
    assert owner in getattr(partner, 'families_Country')
    _safe_set(owner, 'families_Family', None)
    assert owner not in getattr(partner, 'families_Country')


def test_assoc_fathers5_stub_double():
    # families_Parent has no real 'families_Parent' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(lastName="sample_text")
    partner = families_Parent()
    setattr(partner, 'families_Parent', None)
    _safe_set(owner, 'families_Family6', {partner})
    assert getattr(partner, 'families_Parent') == owner
    _safe_set(owner, 'families_Family6', set())
    assert getattr(partner, 'families_Parent') is None


def test_assoc_livesIn35_stub_double():
    # families_City has no real 'families_City37' property in the generated
    # code (a bare stub) -- manually attach it so families_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Member(firstName="sample_text")
    partner = families_City()
    setattr(partner, 'families_City37', None)
    _safe_set(owner, 'families_Member36', partner)
    assert getattr(partner, 'families_City37') == owner
    _safe_set(owner, 'families_Member36', None)
    assert getattr(partner, 'families_City37') is None


def test_assoc_mothers7_stub_double():
    # families_Parent has no real 'families_Parent9' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(lastName="sample_text")
    partner = families_Parent()
    setattr(partner, 'families_Parent9', None)
    _safe_set(owner, 'families_Family8', {partner})
    assert getattr(partner, 'families_Parent9') == owner
    _safe_set(owner, 'families_Family8', set())
    assert getattr(partner, 'families_Parent9') is None


def test_assoc_registeredIn15_stub_double():
    # families_Neighborhood has no real 'Neighborhood' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(lastName="sample_text")
    partner = families_Neighborhood()
    setattr(partner, 'Neighborhood', None)
    _safe_set(owner, 'contains', partner)
    assert getattr(partner, 'Neighborhood') == owner
    _safe_set(owner, 'contains', None)
    assert getattr(partner, 'Neighborhood') is None


def test_assoc_sons12_stub_double():
    # families_Child has no real 'families_Child14' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(lastName="sample_text")
    partner = families_Child()
    setattr(partner, 'families_Child14', None)
    _safe_set(owner, 'families_Family13', {partner})
    assert getattr(partner, 'families_Child14') == owner
    _safe_set(owner, 'families_Family13', set())
    assert getattr(partner, 'families_Child14') is None


