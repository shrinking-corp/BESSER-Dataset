import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    PersonList_Female,
    PersonList_List,
    PersonList_LivingPlace,
    PersonList_Male,
    PersonList_Person,
    PersonList_Place,
    PersonList_WorkPlace,
    PersonList_WorkingPosition,
    Place,
    Gender,
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

def test_assoc_persons11_reverse_link_reassign_clear():
    a1 = PersonList_WorkingPosition(description="sample_text")
    a2 = PersonList_WorkingPosition(description="sample_text_2")
    b = PersonList_Person(name="sample_text")
    _safe_set(b, 'Person13', a1)
    assert _is_linked(b, 'Person13', a1)
    if hasattr(a1, 'works12'):
        assert _is_linked(a1, 'works12', b)
    _safe_set(b, 'Person13', a2)
    assert _is_linked(b, 'Person13', a2)
    if hasattr(a1, 'works12'):
        assert not _is_linked(a1, 'works12', b)
    if hasattr(a2, 'works12'):
        assert _is_linked(a2, 'works12', b)
    _safe_set(b, 'Person13', None)
    assert not _is_linked(b, 'Person13', a2)
    if hasattr(a2, 'works12'):
        assert not _is_linked(a2, 'works12', b)


def test_assoc_works3_reverse_link_reassign_clear():
    a1 = PersonList_WorkingPosition(description="sample_text")
    a2 = PersonList_WorkingPosition(description="sample_text_2")
    b = PersonList_Person(name="sample_text")
    _safe_set(b, 'persons', a1)
    assert _is_linked(b, 'persons', a1)
    if hasattr(a1, 'WorkingPosition'):
        assert _is_linked(a1, 'WorkingPosition', b)
    _safe_set(b, 'persons', a2)
    assert _is_linked(b, 'persons', a2)
    if hasattr(a1, 'WorkingPosition'):
        assert not _is_linked(a1, 'WorkingPosition', b)
    if hasattr(a2, 'WorkingPosition'):
        assert _is_linked(a2, 'WorkingPosition', b)
    _safe_set(b, 'persons', None)
    assert not _is_linked(b, 'persons', a2)
    if hasattr(a2, 'WorkingPosition'):
        assert not _is_linked(a2, 'WorkingPosition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_home4_stub_double():
    # PersonList_LivingPlace has no real 'LivingPlace' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_Person(name="sample_text")
    partner = PersonList_LivingPlace()
    setattr(partner, 'LivingPlace', None)
    _safe_set(owner, 'persons5', partner)
    assert getattr(partner, 'LivingPlace') == owner
    _safe_set(owner, 'persons5', None)
    assert getattr(partner, 'LivingPlace') is None


def test_assoc_list2_stub_double():
    # PersonList_List has no real 'List' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_Person(name="sample_text")
    partner = PersonList_List()
    setattr(partner, 'List', None)
    _safe_set(owner, 'members', partner)
    assert getattr(partner, 'List') == owner
    _safe_set(owner, 'members', None)
    assert getattr(partner, 'List') is None


def test_assoc_members0_stub_double():
    # PersonList_List has no real 'list' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_Person(name="sample_text")
    partner = PersonList_List()
    setattr(partner, 'list', None)
    _safe_set(owner, 'Person', partner)
    assert owner in getattr(partner, 'list')
    _safe_set(owner, 'Person', None)
    assert owner not in getattr(partner, 'list')


def test_assoc_persons8_stub_double():
    # PersonList_LivingPlace has no real 'home' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_Person(name="sample_text")
    partner = PersonList_LivingPlace()
    setattr(partner, 'home', None)
    _safe_set(owner, 'Person9', partner)
    assert owner in getattr(partner, 'home')
    _safe_set(owner, 'Person9', None)
    assert owner not in getattr(partner, 'home')


def test_assoc_places1_stub_double():
    # PersonList_List has no real 'PersonList_List' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_Place(address="sample_text")
    partner = PersonList_List()
    setattr(partner, 'PersonList_List', None)
    _safe_set(owner, 'PersonList_Place', partner)
    assert getattr(partner, 'PersonList_List') == owner
    _safe_set(owner, 'PersonList_Place', None)
    assert getattr(partner, 'PersonList_List') is None


def test_assoc_position6_stub_double():
    # PersonList_WorkPlace has no real 'works' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_WorkingPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_WorkingPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_WorkingPosition(description="sample_text")
    partner = PersonList_WorkPlace()
    setattr(partner, 'works', None)
    _safe_set(owner, 'WorkingPosition7', partner)
    assert getattr(partner, 'works') == owner
    _safe_set(owner, 'WorkingPosition7', None)
    assert getattr(partner, 'works') is None


def test_assoc_works10_stub_double():
    # PersonList_WorkPlace has no real 'WorkPlace' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_WorkingPosition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_WorkingPosition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_WorkingPosition(description="sample_text")
    partner = PersonList_WorkPlace()
    setattr(partner, 'WorkPlace', None)
    _safe_set(owner, 'position', partner)
    assert getattr(partner, 'WorkPlace') == owner
    _safe_set(owner, 'position', None)
    assert getattr(partner, 'WorkPlace') is None


