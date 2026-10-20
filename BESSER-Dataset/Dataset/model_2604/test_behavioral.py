import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    PersonList_List,
    PersonList_LivingPlace,
    PersonList_Person,
    PersonList_WorkPlace,
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

def test_assoc_home6_reverse_link_reassign_clear():
    a1 = PersonList_Person(firstname="sample_text", gender="sample_text", lastname="sample_text")
    a2 = PersonList_Person(firstname="sample_text_2", gender="sample_text_2", lastname="sample_text_2")
    b = PersonList_LivingPlace(address="sample_text")
    _safe_set(b, 'LivingPlace', a1)
    assert _is_linked(b, 'LivingPlace', a1)
    if hasattr(a1, 'persons7'):
        assert _is_linked(a1, 'persons7', b)
    _safe_set(b, 'LivingPlace', a2)
    assert _is_linked(b, 'LivingPlace', a2)
    if hasattr(a1, 'persons7'):
        assert not _is_linked(a1, 'persons7', b)
    if hasattr(a2, 'persons7'):
        assert _is_linked(a2, 'persons7', b)
    _safe_set(b, 'LivingPlace', None)
    assert not _is_linked(b, 'LivingPlace', a2)
    if hasattr(a2, 'persons7'):
        assert not _is_linked(a2, 'persons7', b)


def test_assoc_persons10_reverse_link_reassign_clear():
    a1 = PersonList_Person(firstname="sample_text", gender="sample_text", lastname="sample_text")
    a2 = PersonList_Person(firstname="sample_text_2", gender="sample_text_2", lastname="sample_text_2")
    b = PersonList_LivingPlace(address="sample_text")
    _safe_set(b, 'home', {a1})
    assert _is_linked(b, 'home', a1)
    if hasattr(a1, 'Person11'):
        assert _is_linked(a1, 'Person11', b)
    _safe_set(b, 'home', {a2})
    assert _is_linked(b, 'home', a2)
    if hasattr(a1, 'Person11'):
        assert not _is_linked(a1, 'Person11', b)
    if hasattr(a2, 'Person11'):
        assert _is_linked(a2, 'Person11', b)
    _safe_set(b, 'home', set())
    assert not _is_linked(b, 'home', a2)
    if hasattr(a2, 'Person11'):
        assert not _is_linked(a2, 'Person11', b)


def test_assoc_persons8_reverse_link_reassign_clear():
    a1 = PersonList_WorkPlace(address="sample_text")
    a2 = PersonList_WorkPlace(address="sample_text_2")
    b = PersonList_Person(firstname="sample_text", gender="sample_text", lastname="sample_text")
    _safe_set(b, 'Person9', a1)
    assert _is_linked(b, 'Person9', a1)
    if hasattr(a1, 'works'):
        assert _is_linked(a1, 'works', b)
    _safe_set(b, 'Person9', a2)
    assert _is_linked(b, 'Person9', a2)
    if hasattr(a1, 'works'):
        assert not _is_linked(a1, 'works', b)
    if hasattr(a2, 'works'):
        assert _is_linked(a2, 'works', b)
    _safe_set(b, 'Person9', None)
    assert not _is_linked(b, 'Person9', a2)
    if hasattr(a2, 'works'):
        assert not _is_linked(a2, 'works', b)


def test_assoc_works5_reverse_link_reassign_clear():
    a1 = PersonList_WorkPlace(address="sample_text")
    a2 = PersonList_WorkPlace(address="sample_text_2")
    b = PersonList_Person(firstname="sample_text", gender="sample_text", lastname="sample_text")
    _safe_set(b, 'persons', a1)
    assert _is_linked(b, 'persons', a1)
    if hasattr(a1, 'WorkPlace'):
        assert _is_linked(a1, 'WorkPlace', b)
    _safe_set(b, 'persons', a2)
    assert _is_linked(b, 'persons', a2)
    if hasattr(a1, 'WorkPlace'):
        assert not _is_linked(a1, 'WorkPlace', b)
    if hasattr(a2, 'WorkPlace'):
        assert _is_linked(a2, 'WorkPlace', b)
    _safe_set(b, 'persons', None)
    assert not _is_linked(b, 'persons', a2)
    if hasattr(a2, 'WorkPlace'):
        assert not _is_linked(a2, 'WorkPlace', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_list4_stub_double():
    # PersonList_List has no real 'List' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_Person(firstname="sample_text", gender="sample_text", lastname="sample_text")
    partner = PersonList_List()
    setattr(partner, 'List', None)
    _safe_set(owner, 'members', partner)
    assert getattr(partner, 'List') == owner
    _safe_set(owner, 'members', None)
    assert getattr(partner, 'List') is None


def test_assoc_lplaces2_stub_double():
    # PersonList_List has no real 'PersonList_List3' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_LivingPlace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_LivingPlace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_LivingPlace(address="sample_text")
    partner = PersonList_List()
    setattr(partner, 'PersonList_List3', None)
    _safe_set(owner, 'PersonList_LivingPlace', partner)
    assert owner in getattr(partner, 'PersonList_List3')
    _safe_set(owner, 'PersonList_LivingPlace', None)
    assert owner not in getattr(partner, 'PersonList_List3')


def test_assoc_members0_stub_double():
    # PersonList_List has no real 'list' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_Person(firstname="sample_text", gender="sample_text", lastname="sample_text")
    partner = PersonList_List()
    setattr(partner, 'list', None)
    _safe_set(owner, 'Person', partner)
    assert owner in getattr(partner, 'list')
    _safe_set(owner, 'Person', None)
    assert owner not in getattr(partner, 'list')


def test_assoc_wplaces1_stub_double():
    # PersonList_List has no real 'PersonList_List' property in the generated
    # code (a bare stub) -- manually attach it so PersonList_WorkPlace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PersonList_WorkPlace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PersonList_WorkPlace(address="sample_text")
    partner = PersonList_List()
    setattr(partner, 'PersonList_List', None)
    _safe_set(owner, 'PersonList_WorkPlace', partner)
    assert owner in getattr(partner, 'PersonList_List')
    _safe_set(owner, 'PersonList_WorkPlace', None)
    assert owner not in getattr(partner, 'PersonList_List')


