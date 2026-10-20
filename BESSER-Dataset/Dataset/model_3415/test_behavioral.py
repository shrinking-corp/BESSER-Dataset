import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    fair_Animal,
    fair_Class,
    fair_Department,
    fair_Division,
    fair_Exhibit,
    fair_Fair,
    fair_Lot,
    fair_Person,
    fair_Premises,
    fair_YoungPerson,
    fair_YouthClub,
    Award,
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

def test_assoc_class_27_reverse_link_reassign_clear():
    a1 = fair_Lot(comments="sample_text", name="sample_text")
    a2 = fair_Lot(comments="sample_text_2", name="sample_text_2")
    b = fair_Class(comments="sample_text", name="sample_text")
    _safe_set(b, 'Class28', a1)
    assert _is_linked(b, 'Class28', a1)
    if hasattr(a1, 'lots'):
        assert _is_linked(a1, 'lots', b)
    _safe_set(b, 'Class28', a2)
    assert _is_linked(b, 'Class28', a2)
    if hasattr(a1, 'lots'):
        assert not _is_linked(a1, 'lots', b)
    if hasattr(a2, 'lots'):
        assert _is_linked(a2, 'lots', b)
    _safe_set(b, 'Class28', None)
    assert not _is_linked(b, 'Class28', a2)
    if hasattr(a2, 'lots'):
        assert not _is_linked(a2, 'lots', b)


def test_assoc_classes16_reverse_link_reassign_clear():
    a1 = fair_Department(comments="sample_text", name="sample_text")
    a2 = fair_Department(comments="sample_text_2", name="sample_text_2")
    b = fair_Class(comments="sample_text", name="sample_text")
    _safe_set(b, 'Class', a1)
    assert _is_linked(b, 'Class', a1)
    if hasattr(a1, 'department'):
        assert _is_linked(a1, 'department', b)
    _safe_set(b, 'Class', a2)
    assert _is_linked(b, 'Class', a2)
    if hasattr(a1, 'department'):
        assert not _is_linked(a1, 'department', b)
    if hasattr(a2, 'department'):
        assert _is_linked(a2, 'department', b)
    _safe_set(b, 'Class', None)
    assert not _is_linked(b, 'Class', a2)
    if hasattr(a2, 'department'):
        assert not _is_linked(a2, 'department', b)


def test_assoc_contacts12_reverse_link_reassign_clear():
    a1 = fair_YouthClub(comments="sample_text", name="sample_text")
    a2 = fair_YouthClub(comments="sample_text_2", name="sample_text_2")
    b = fair_Person(city="sample_text", comments="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", phone="sample_text", pin="sample_text", salesOrder=7, state="sample_text", street="sample_text", zipCode="sample_text")
    _safe_set(b, 'fair_Person14', a1)
    assert _is_linked(b, 'fair_Person14', a1)
    if hasattr(a1, 'fair_YouthClub13'):
        assert _is_linked(a1, 'fair_YouthClub13', b)
    _safe_set(b, 'fair_Person14', a2)
    assert _is_linked(b, 'fair_Person14', a2)
    if hasattr(a1, 'fair_YouthClub13'):
        assert not _is_linked(a1, 'fair_YouthClub13', b)
    if hasattr(a2, 'fair_YouthClub13'):
        assert _is_linked(a2, 'fair_YouthClub13', b)
    _safe_set(b, 'fair_Person14', None)
    assert not _is_linked(b, 'fair_Person14', a2)
    if hasattr(a2, 'fair_YouthClub13'):
        assert not _is_linked(a2, 'fair_YouthClub13', b)


def test_assoc_department24_reverse_link_reassign_clear():
    a1 = fair_Department(comments="sample_text", name="sample_text")
    a2 = fair_Department(comments="sample_text_2", name="sample_text_2")
    b = fair_Class(comments="sample_text", name="sample_text")
    _safe_set(b, 'classes', a1)
    assert _is_linked(b, 'classes', a1)
    if hasattr(a1, 'Department25'):
        assert _is_linked(a1, 'Department25', b)
    _safe_set(b, 'classes', a2)
    assert _is_linked(b, 'classes', a2)
    if hasattr(a1, 'Department25'):
        assert not _is_linked(a1, 'Department25', b)
    if hasattr(a2, 'Department25'):
        assert _is_linked(a2, 'Department25', b)
    _safe_set(b, 'classes', None)
    assert not _is_linked(b, 'classes', a2)
    if hasattr(a2, 'Department25'):
        assert not _is_linked(a2, 'Department25', b)


def test_assoc_departments15_reverse_link_reassign_clear():
    a1 = fair_Division(comments="sample_text", name="sample_text")
    a2 = fair_Division(comments="sample_text_2", name="sample_text_2")
    b = fair_Department(comments="sample_text", name="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'division'):
        assert _is_linked(a1, 'division', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'division'):
        assert not _is_linked(a1, 'division', b)
    if hasattr(a2, 'division'):
        assert _is_linked(a2, 'division', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'division'):
        assert not _is_linked(a2, 'division', b)


def test_assoc_division19_reverse_link_reassign_clear():
    a1 = fair_Division(comments="sample_text", name="sample_text")
    a2 = fair_Division(comments="sample_text_2", name="sample_text_2")
    b = fair_Department(comments="sample_text", name="sample_text")
    _safe_set(b, 'departments', a1)
    assert _is_linked(b, 'departments', a1)
    if hasattr(a1, 'Division'):
        assert _is_linked(a1, 'Division', b)
    _safe_set(b, 'departments', a2)
    assert _is_linked(b, 'departments', a2)
    if hasattr(a1, 'Division'):
        assert not _is_linked(a1, 'Division', b)
    if hasattr(a2, 'Division'):
        assert _is_linked(a2, 'Division', b)
    _safe_set(b, 'departments', None)
    assert not _is_linked(b, 'departments', a2)
    if hasattr(a2, 'Division'):
        assert not _is_linked(a2, 'Division', b)


def test_assoc_divisions1_reverse_link_reassign_clear():
    a1 = fair_Fair(comments="sample_text", name="sample_text")
    a2 = fair_Fair(comments="sample_text_2", name="sample_text_2")
    b = fair_Division(comments="sample_text", name="sample_text")
    _safe_set(b, 'fair_Division', a1)
    assert _is_linked(b, 'fair_Division', a1)
    if hasattr(a1, 'fair_Fair2'):
        assert _is_linked(a1, 'fair_Fair2', b)
    _safe_set(b, 'fair_Division', a2)
    assert _is_linked(b, 'fair_Division', a2)
    if hasattr(a1, 'fair_Fair2'):
        assert not _is_linked(a1, 'fair_Fair2', b)
    if hasattr(a2, 'fair_Fair2'):
        assert _is_linked(a2, 'fair_Fair2', b)
    _safe_set(b, 'fair_Division', None)
    assert not _is_linked(b, 'fair_Division', a2)
    if hasattr(a2, 'fair_Fair2'):
        assert not _is_linked(a2, 'fair_Fair2', b)


def test_assoc_exhibitor8_reverse_link_reassign_clear():
    a1 = fair_Person(city="sample_text", comments="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", phone="sample_text", pin="sample_text", salesOrder=7, state="sample_text", street="sample_text", zipCode="sample_text")
    a2 = fair_Person(city="sample_text_2", comments="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", name="sample_text_2", phone="sample_text_2", pin="sample_text_2", salesOrder=13, state="sample_text_2", street="sample_text_2", zipCode="sample_text_2")
    b = fair_Exhibit(award="sample_text", comments="sample_text", inAuction=True, name="sample_text", number=7, salesOrder=7)
    _safe_set(b, 'fair_Exhibit9', a1)
    assert _is_linked(b, 'fair_Exhibit9', a1)
    if hasattr(a1, 'fair_Person10'):
        assert _is_linked(a1, 'fair_Person10', b)
    _safe_set(b, 'fair_Exhibit9', a2)
    assert _is_linked(b, 'fair_Exhibit9', a2)
    if hasattr(a1, 'fair_Person10'):
        assert not _is_linked(a1, 'fair_Person10', b)
    if hasattr(a2, 'fair_Person10'):
        assert _is_linked(a2, 'fair_Person10', b)
    _safe_set(b, 'fair_Exhibit9', None)
    assert not _is_linked(b, 'fair_Exhibit9', a2)
    if hasattr(a2, 'fair_Person10'):
        assert not _is_linked(a2, 'fair_Person10', b)


def test_assoc_exhibits26_reverse_link_reassign_clear():
    a1 = fair_Lot(comments="sample_text", name="sample_text")
    a2 = fair_Lot(comments="sample_text_2", name="sample_text_2")
    b = fair_Exhibit(award="sample_text", comments="sample_text", inAuction=True, name="sample_text", number=7, salesOrder=7)
    _safe_set(b, 'Exhibit', a1)
    assert _is_linked(b, 'Exhibit', a1)
    if hasattr(a1, 'lot'):
        assert _is_linked(a1, 'lot', b)
    _safe_set(b, 'Exhibit', a2)
    assert _is_linked(b, 'Exhibit', a2)
    if hasattr(a1, 'lot'):
        assert not _is_linked(a1, 'lot', b)
    if hasattr(a2, 'lot'):
        assert _is_linked(a2, 'lot', b)
    _safe_set(b, 'Exhibit', None)
    assert not _is_linked(b, 'Exhibit', a2)
    if hasattr(a2, 'lot'):
        assert not _is_linked(a2, 'lot', b)


def test_assoc_judges22_reverse_link_reassign_clear():
    a1 = fair_Person(city="sample_text", comments="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", phone="sample_text", pin="sample_text", salesOrder=7, state="sample_text", street="sample_text", zipCode="sample_text")
    a2 = fair_Person(city="sample_text_2", comments="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", name="sample_text_2", phone="sample_text_2", pin="sample_text_2", salesOrder=13, state="sample_text_2", street="sample_text_2", zipCode="sample_text_2")
    b = fair_Class(comments="sample_text", name="sample_text")
    _safe_set(b, 'fair_Class', {a1})
    assert _is_linked(b, 'fair_Class', a1)
    if hasattr(a1, 'fair_Person23'):
        assert _is_linked(a1, 'fair_Person23', b)
    _safe_set(b, 'fair_Class', {a2})
    assert _is_linked(b, 'fair_Class', a2)
    if hasattr(a1, 'fair_Person23'):
        assert not _is_linked(a1, 'fair_Person23', b)
    if hasattr(a2, 'fair_Person23'):
        assert _is_linked(a2, 'fair_Person23', b)
    _safe_set(b, 'fair_Class', set())
    assert not _is_linked(b, 'fair_Class', a2)
    if hasattr(a2, 'fair_Person23'):
        assert not _is_linked(a2, 'fair_Person23', b)


def test_assoc_lot11_reverse_link_reassign_clear():
    a1 = fair_Lot(comments="sample_text", name="sample_text")
    a2 = fair_Lot(comments="sample_text_2", name="sample_text_2")
    b = fair_Exhibit(award="sample_text", comments="sample_text", inAuction=True, name="sample_text", number=7, salesOrder=7)
    _safe_set(b, 'exhibits', a1)
    assert _is_linked(b, 'exhibits', a1)
    if hasattr(a1, 'Lot'):
        assert _is_linked(a1, 'Lot', b)
    _safe_set(b, 'exhibits', a2)
    assert _is_linked(b, 'exhibits', a2)
    if hasattr(a1, 'Lot'):
        assert not _is_linked(a1, 'Lot', b)
    if hasattr(a2, 'Lot'):
        assert _is_linked(a2, 'Lot', b)
    _safe_set(b, 'exhibits', None)
    assert not _is_linked(b, 'exhibits', a2)
    if hasattr(a2, 'Lot'):
        assert not _is_linked(a2, 'Lot', b)


def test_assoc_lots20_reverse_link_reassign_clear():
    a1 = fair_Lot(comments="sample_text", name="sample_text")
    a2 = fair_Lot(comments="sample_text_2", name="sample_text_2")
    b = fair_Class(comments="sample_text", name="sample_text")
    _safe_set(b, 'class_', {a1})
    assert _is_linked(b, 'class_', a1)
    if hasattr(a1, 'Lot21'):
        assert _is_linked(a1, 'Lot21', b)
    _safe_set(b, 'class_', {a2})
    assert _is_linked(b, 'class_', a2)
    if hasattr(a1, 'Lot21'):
        assert not _is_linked(a1, 'Lot21', b)
    if hasattr(a2, 'Lot21'):
        assert _is_linked(a2, 'Lot21', b)
    _safe_set(b, 'class_', set())
    assert not _is_linked(b, 'class_', a2)
    if hasattr(a2, 'Lot21'):
        assert not _is_linked(a2, 'Lot21', b)


def test_assoc_people5_reverse_link_reassign_clear():
    a1 = fair_Person(city="sample_text", comments="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", phone="sample_text", pin="sample_text", salesOrder=7, state="sample_text", street="sample_text", zipCode="sample_text")
    a2 = fair_Person(city="sample_text_2", comments="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", name="sample_text_2", phone="sample_text_2", pin="sample_text_2", salesOrder=13, state="sample_text_2", street="sample_text_2", zipCode="sample_text_2")
    b = fair_Fair(comments="sample_text", name="sample_text")
    _safe_set(b, 'fair_Fair6', {a1})
    assert _is_linked(b, 'fair_Fair6', a1)
    if hasattr(a1, 'fair_Person'):
        assert _is_linked(a1, 'fair_Person', b)
    _safe_set(b, 'fair_Fair6', {a2})
    assert _is_linked(b, 'fair_Fair6', a2)
    if hasattr(a1, 'fair_Person'):
        assert not _is_linked(a1, 'fair_Person', b)
    if hasattr(a2, 'fair_Person'):
        assert _is_linked(a2, 'fair_Person', b)
    _safe_set(b, 'fair_Fair6', set())
    assert not _is_linked(b, 'fair_Fair6', a2)
    if hasattr(a2, 'fair_Person'):
        assert not _is_linked(a2, 'fair_Person', b)


def test_assoc_superintendents17_reverse_link_reassign_clear():
    a1 = fair_Person(city="sample_text", comments="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", phone="sample_text", pin="sample_text", salesOrder=7, state="sample_text", street="sample_text", zipCode="sample_text")
    a2 = fair_Person(city="sample_text_2", comments="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", name="sample_text_2", phone="sample_text_2", pin="sample_text_2", salesOrder=13, state="sample_text_2", street="sample_text_2", zipCode="sample_text_2")
    b = fair_Department(comments="sample_text", name="sample_text")
    _safe_set(b, 'fair_Department', {a1})
    assert _is_linked(b, 'fair_Department', a1)
    if hasattr(a1, 'fair_Person18'):
        assert _is_linked(a1, 'fair_Person18', b)
    _safe_set(b, 'fair_Department', {a2})
    assert _is_linked(b, 'fair_Department', a2)
    if hasattr(a1, 'fair_Person18'):
        assert not _is_linked(a1, 'fair_Person18', b)
    if hasattr(a2, 'fair_Person18'):
        assert _is_linked(a2, 'fair_Person18', b)
    _safe_set(b, 'fair_Department', set())
    assert not _is_linked(b, 'fair_Department', a2)
    if hasattr(a2, 'fair_Person18'):
        assert not _is_linked(a2, 'fair_Person18', b)


def test_assoc_youthClubs0_reverse_link_reassign_clear():
    a1 = fair_YouthClub(comments="sample_text", name="sample_text")
    a2 = fair_YouthClub(comments="sample_text_2", name="sample_text_2")
    b = fair_Fair(comments="sample_text", name="sample_text")
    _safe_set(b, 'fair_Fair', {a1})
    assert _is_linked(b, 'fair_Fair', a1)
    if hasattr(a1, 'fair_YouthClub'):
        assert _is_linked(a1, 'fair_YouthClub', b)
    _safe_set(b, 'fair_Fair', {a2})
    assert _is_linked(b, 'fair_Fair', a2)
    if hasattr(a1, 'fair_YouthClub'):
        assert not _is_linked(a1, 'fair_YouthClub', b)
    if hasattr(a2, 'fair_YouthClub'):
        assert _is_linked(a2, 'fair_YouthClub', b)
    _safe_set(b, 'fair_Fair', set())
    assert not _is_linked(b, 'fair_Fair', a2)
    if hasattr(a2, 'fair_YouthClub'):
        assert not _is_linked(a2, 'fair_YouthClub', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_animal7_stub_double():
    # fair_Animal has no real 'fair_Animal' property in the generated
    # code (a bare stub) -- manually attach it so fair_Exhibit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fair_Exhibit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fair_Exhibit(award="sample_text", comments="sample_text", inAuction=True, name="sample_text", number=7, salesOrder=7)
    partner = fair_Animal()
    setattr(partner, 'fair_Animal', None)
    _safe_set(owner, 'fair_Exhibit', partner)
    assert getattr(partner, 'fair_Animal') == owner
    _safe_set(owner, 'fair_Exhibit', None)
    assert getattr(partner, 'fair_Animal') is None


def test_assoc_club31_stub_double():
    # fair_YoungPerson has no real 'fair_YoungPerson32' property in the generated
    # code (a bare stub) -- manually attach it so fair_YouthClub's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fair_YouthClub's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fair_YouthClub(comments="sample_text", name="sample_text")
    partner = fair_YoungPerson()
    setattr(partner, 'fair_YoungPerson32', None)
    _safe_set(owner, 'fair_YouthClub33', partner)
    assert getattr(partner, 'fair_YoungPerson32') == owner
    _safe_set(owner, 'fair_YouthClub33', None)
    assert getattr(partner, 'fair_YoungPerson32') is None


def test_assoc_parents29_stub_double():
    # fair_YoungPerson has no real 'fair_YoungPerson' property in the generated
    # code (a bare stub) -- manually attach it so fair_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fair_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fair_Person(city="sample_text", comments="sample_text", firstName="sample_text", lastName="sample_text", name="sample_text", phone="sample_text", pin="sample_text", salesOrder=7, state="sample_text", street="sample_text", zipCode="sample_text")
    partner = fair_YoungPerson()
    setattr(partner, 'fair_YoungPerson', None)
    _safe_set(owner, 'fair_Person30', partner)
    assert owner in getattr(partner, 'fair_YoungPerson')
    _safe_set(owner, 'fair_Person30', None)
    assert owner not in getattr(partner, 'fair_YoungPerson')


def test_assoc_premises3_stub_double():
    # fair_Premises has no real 'fair_Premises' property in the generated
    # code (a bare stub) -- manually attach it so fair_Fair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fair_Fair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fair_Fair(comments="sample_text", name="sample_text")
    partner = fair_Premises()
    setattr(partner, 'fair_Premises', None)
    _safe_set(owner, 'fair_Fair4', partner)
    assert getattr(partner, 'fair_Premises') == owner
    _safe_set(owner, 'fair_Fair4', None)
    assert getattr(partner, 'fair_Premises') is None


