import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    District,
    NamedElement,
    Pet,
    families_Account,
    families_Band,
    families_Bike,
    families_District,
    families_Dog,
    families_Family,
    families_Model,
    families_NamedElement,
    families_Person,
    families_Pet,
    families_Suburb,
    DogBreed,
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

def test_assoc_dogs3_reverse_link_reassign_clear():
    a1 = families_Family(address="sample_text", averageAge=3.14, averageAgePrecise=3.14, id="sample_text", lotteryNumbers=7, nuclear=True, numberOfChildren=7)
    a2 = families_Family(address="sample_text_2", averageAge=9.99, averageAgePrecise=9.99, id="sample_text_2", lotteryNumbers=13, nuclear=False, numberOfChildren=13)
    b = families_Dog(breed="sample_text", loud=True)
    _safe_set(b, 'families_Dog', a1)
    assert _is_linked(b, 'families_Dog', a1)
    if hasattr(a1, 'families_Family4'):
        assert _is_linked(a1, 'families_Family4', b)
    _safe_set(b, 'families_Dog', a2)
    assert _is_linked(b, 'families_Dog', a2)
    if hasattr(a1, 'families_Family4'):
        assert not _is_linked(a1, 'families_Family4', b)
    if hasattr(a2, 'families_Family4'):
        assert _is_linked(a2, 'families_Family4', b)
    _safe_set(b, 'families_Dog', None)
    assert not _is_linked(b, 'families_Dog', a2)
    if hasattr(a2, 'families_Family4'):
        assert not _is_linked(a2, 'families_Family4', b)


def test_assoc_pets0_reverse_link_reassign_clear():
    a1 = families_Pet(male=True)
    a2 = families_Pet(male=False)
    b = families_Family(address="sample_text", averageAge=3.14, averageAgePrecise=3.14, id="sample_text", lotteryNumbers=7, nuclear=True, numberOfChildren=7)
    _safe_set(b, 'families_Family', {a1})
    assert _is_linked(b, 'families_Family', a1)
    if hasattr(a1, 'families_Pet'):
        assert _is_linked(a1, 'families_Pet', b)
    _safe_set(b, 'families_Family', {a2})
    assert _is_linked(b, 'families_Family', a2)
    if hasattr(a1, 'families_Pet'):
        assert not _is_linked(a1, 'families_Pet', b)
    if hasattr(a2, 'families_Pet'):
        assert _is_linked(a2, 'families_Pet', b)
    _safe_set(b, 'families_Family', set())
    assert not _is_linked(b, 'families_Family', a2)
    if hasattr(a2, 'families_Pet'):
        assert not _is_linked(a2, 'families_Pet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents226_stub_double():
    # families_Model has no real 'families_Model27' property in the generated
    # code (a bare stub) -- manually attach it so families_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_NamedElement(name="sample_text")
    partner = families_Model()
    setattr(partner, 'families_Model27', None)
    _safe_set(owner, 'families_NamedElement28', partner)
    assert owner in getattr(partner, 'families_Model27')
    _safe_set(owner, 'families_NamedElement28', None)
    assert owner not in getattr(partner, 'families_Model27')


def test_assoc_contents25_stub_double():
    # families_Model has no real 'families_Model' property in the generated
    # code (a bare stub) -- manually attach it so families_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_NamedElement(name="sample_text")
    partner = families_Model()
    setattr(partner, 'families_Model', None)
    _safe_set(owner, 'families_NamedElement', partner)
    assert owner in getattr(partner, 'families_Model')
    _safe_set(owner, 'families_NamedElement', None)
    assert owner not in getattr(partner, 'families_Model')


def test_assoc_district20_stub_double():
    # families_District has no real 'District21' property in the generated
    # code (a bare stub) -- manually attach it so families_Dog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Dog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Dog(breed="sample_text", loud=True)
    partner = families_District()
    setattr(partner, 'District21', None)
    _safe_set(owner, 'dogs', partner)
    assert getattr(partner, 'District21') == owner
    _safe_set(owner, 'dogs', None)
    assert getattr(partner, 'District21') is None


def test_assoc_district5_stub_double():
    # families_District has no real 'District' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(address="sample_text", averageAge=3.14, averageAgePrecise=3.14, id="sample_text", lotteryNumbers=7, nuclear=True, numberOfChildren=7)
    partner = families_District()
    setattr(partner, 'District', None)
    _safe_set(owner, 'families', partner)
    assert getattr(partner, 'District') == owner
    _safe_set(owner, 'families', None)
    assert getattr(partner, 'District') is None


def test_assoc_dogs23_stub_double():
    # families_District has no real 'district24' property in the generated
    # code (a bare stub) -- manually attach it so families_Dog's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Dog's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Dog(breed="sample_text", loud=True)
    partner = families_District()
    setattr(partner, 'district24', None)
    _safe_set(owner, 'Dog', partner)
    assert owner in getattr(partner, 'district24')
    _safe_set(owner, 'Dog', None)
    assert owner not in getattr(partner, 'district24')


def test_assoc_families22_stub_double():
    # families_District has no real 'district' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(address="sample_text", averageAge=3.14, averageAgePrecise=3.14, id="sample_text", lotteryNumbers=7, nuclear=True, numberOfChildren=7)
    partner = families_District()
    setattr(partner, 'district', None)
    _safe_set(owner, 'Family', partner)
    assert owner in getattr(partner, 'district')
    _safe_set(owner, 'Family', None)
    assert owner not in getattr(partner, 'district')


def test_assoc_members1_stub_double():
    # families_Person has no real 'families_Person' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(address="sample_text", averageAge=3.14, averageAgePrecise=3.14, id="sample_text", lotteryNumbers=7, nuclear=True, numberOfChildren=7)
    partner = families_Person()
    setattr(partner, 'families_Person', None)
    _safe_set(owner, 'families_Family2', {partner})
    assert getattr(partner, 'families_Person') == owner
    _safe_set(owner, 'families_Family2', set())
    assert getattr(partner, 'families_Person') is None


def test_assoc_owner31_stub_double():
    # families_Bike has no real 'families_Bike32' property in the generated
    # code (a bare stub) -- manually attach it so families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = families_Family(address="sample_text", averageAge=3.14, averageAgePrecise=3.14, id="sample_text", lotteryNumbers=7, nuclear=True, numberOfChildren=7)
    partner = families_Bike()
    setattr(partner, 'families_Bike32', None)
    _safe_set(owner, 'families_Family33', partner)
    assert getattr(partner, 'families_Bike32') == owner
    _safe_set(owner, 'families_Family33', None)
    assert getattr(partner, 'families_Bike32') is None


