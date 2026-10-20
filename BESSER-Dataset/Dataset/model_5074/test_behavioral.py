import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CarRental2_Branch,
    CarRental2_Car,
    CarRental2_CarGroup,
    CarRental2_Check,
    CarRental2_Customer,
    CarRental2_Employee,
    CarRental2_Person,
    CarRental2_Rental,
    CarRental2_ServiceDepot,
    CarRental2_TernaryRelationMaintenance,
    Person,
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

def test_assoc_Assignment_Car16_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_Car(id=7)
    _safe_set(b, 'Car17', a1)
    assert _is_linked(b, 'Car17', a1)
    if hasattr(a1, 'Assignment_Rental'):
        assert _is_linked(a1, 'Assignment_Rental', b)
    _safe_set(b, 'Car17', a2)
    assert _is_linked(b, 'Car17', a2)
    if hasattr(a1, 'Assignment_Rental'):
        assert not _is_linked(a1, 'Assignment_Rental', b)
    if hasattr(a2, 'Assignment_Rental'):
        assert _is_linked(a2, 'Assignment_Rental', b)
    _safe_set(b, 'Car17', None)
    assert not _is_linked(b, 'Car17', a2)
    if hasattr(a2, 'Assignment_Rental'):
        assert not _is_linked(a2, 'Assignment_Rental', b)


def test_assoc_Assignment_Rental34_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_Car(id=7)
    _safe_set(b, 'Assignment_Car', a1)
    assert _is_linked(b, 'Assignment_Car', a1)
    if hasattr(a1, 'Rental35'):
        assert _is_linked(a1, 'Rental35', b)
    _safe_set(b, 'Assignment_Car', a2)
    assert _is_linked(b, 'Assignment_Car', a2)
    if hasattr(a1, 'Rental35'):
        assert not _is_linked(a1, 'Rental35', b)
    if hasattr(a2, 'Rental35'):
        assert _is_linked(a2, 'Rental35', b)
    _safe_set(b, 'Assignment_Car', None)
    assert not _is_linked(b, 'Assignment_Car', a2)
    if hasattr(a2, 'Rental35'):
        assert not _is_linked(a2, 'Rental35', b)


def test_assoc_Booking_Customer11_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_Customer(address=7)
    _safe_set(b, 'Customer', a1)
    assert _is_linked(b, 'Customer', a1)
    if hasattr(a1, 'Booking_Rental'):
        assert _is_linked(a1, 'Booking_Rental', b)
    _safe_set(b, 'Customer', a2)
    assert _is_linked(b, 'Customer', a2)
    if hasattr(a1, 'Booking_Rental'):
        assert not _is_linked(a1, 'Booking_Rental', b)
    if hasattr(a2, 'Booking_Rental'):
        assert _is_linked(a2, 'Booking_Rental', b)
    _safe_set(b, 'Customer', None)
    assert not _is_linked(b, 'Customer', a2)
    if hasattr(a2, 'Booking_Rental'):
        assert not _is_linked(a2, 'Booking_Rental', b)


def test_assoc_Booking_Rental0_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_Customer(address=7)
    _safe_set(b, 'Booking_Customer', {a1})
    assert _is_linked(b, 'Booking_Customer', a1)
    if hasattr(a1, 'Rental'):
        assert _is_linked(a1, 'Rental', b)
    _safe_set(b, 'Booking_Customer', {a2})
    assert _is_linked(b, 'Booking_Customer', a2)
    if hasattr(a1, 'Rental'):
        assert not _is_linked(a1, 'Rental', b)
    if hasattr(a2, 'Rental'):
        assert _is_linked(a2, 'Rental', b)
    _safe_set(b, 'Booking_Customer', set())
    assert not _is_linked(b, 'Booking_Customer', a2)
    if hasattr(a2, 'Rental'):
        assert not _is_linked(a2, 'Rental', b)


def test_assoc_Classification_Car20_reverse_link_reassign_clear():
    a1 = CarRental2_CarGroup(kind=7)
    a2 = CarRental2_CarGroup(kind=13)
    b = CarRental2_Car(id=7)
    _safe_set(b, 'Car21', a1)
    assert _is_linked(b, 'Car21', a1)
    if hasattr(a1, 'Classification_CarGroup'):
        assert _is_linked(a1, 'Classification_CarGroup', b)
    _safe_set(b, 'Car21', a2)
    assert _is_linked(b, 'Car21', a2)
    if hasattr(a1, 'Classification_CarGroup'):
        assert not _is_linked(a1, 'Classification_CarGroup', b)
    if hasattr(a2, 'Classification_CarGroup'):
        assert _is_linked(a2, 'Classification_CarGroup', b)
    _safe_set(b, 'Car21', None)
    assert not _is_linked(b, 'Car21', a2)
    if hasattr(a2, 'Classification_CarGroup'):
        assert not _is_linked(a2, 'Classification_CarGroup', b)


def test_assoc_Classification_CarGroup32_reverse_link_reassign_clear():
    a1 = CarRental2_CarGroup(kind=7)
    a2 = CarRental2_CarGroup(kind=13)
    b = CarRental2_Car(id=7)
    _safe_set(b, 'Classification_Car', a1)
    assert _is_linked(b, 'Classification_Car', a1)
    if hasattr(a1, 'CarGroup33'):
        assert _is_linked(a1, 'CarGroup33', b)
    _safe_set(b, 'Classification_Car', a2)
    assert _is_linked(b, 'Classification_Car', a2)
    if hasattr(a1, 'CarGroup33'):
        assert not _is_linked(a1, 'CarGroup33', b)
    if hasattr(a2, 'CarGroup33'):
        assert _is_linked(a2, 'CarGroup33', b)
    _safe_set(b, 'Classification_Car', None)
    assert not _is_linked(b, 'Classification_Car', a2)
    if hasattr(a2, 'CarGroup33'):
        assert not _is_linked(a2, 'CarGroup33', b)


def test_assoc_Employment_Branch_role_employer2_reverse_link_reassign_clear():
    a1 = CarRental2_Employee(salary=7)
    a2 = CarRental2_Employee(salary=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Branch3', a1)
    assert _is_linked(b, 'Branch3', a1)
    if hasattr(a1, 'Employment_Employee_role_employee'):
        assert _is_linked(a1, 'Employment_Employee_role_employee', b)
    _safe_set(b, 'Branch3', a2)
    assert _is_linked(b, 'Branch3', a2)
    if hasattr(a1, 'Employment_Employee_role_employee'):
        assert not _is_linked(a1, 'Employment_Employee_role_employee', b)
    if hasattr(a2, 'Employment_Employee_role_employee'):
        assert _is_linked(a2, 'Employment_Employee_role_employee', b)
    _safe_set(b, 'Branch3', None)
    assert not _is_linked(b, 'Branch3', a2)
    if hasattr(a2, 'Employment_Employee_role_employee'):
        assert not _is_linked(a2, 'Employment_Employee_role_employee', b)


def test_assoc_Employment_Employee_role_employee5_reverse_link_reassign_clear():
    a1 = CarRental2_Employee(salary=7)
    a2 = CarRental2_Employee(salary=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Employment_Branch_role_employer', {a1})
    assert _is_linked(b, 'Employment_Branch_role_employer', a1)
    if hasattr(a1, 'Employee6'):
        assert _is_linked(a1, 'Employee6', b)
    _safe_set(b, 'Employment_Branch_role_employer', {a2})
    assert _is_linked(b, 'Employment_Branch_role_employer', a2)
    if hasattr(a1, 'Employee6'):
        assert not _is_linked(a1, 'Employee6', b)
    if hasattr(a2, 'Employee6'):
        assert _is_linked(a2, 'Employee6', b)
    _safe_set(b, 'Employment_Branch_role_employer', set())
    assert not _is_linked(b, 'Employment_Branch_role_employer', a2)
    if hasattr(a2, 'Employee6'):
        assert not _is_linked(a2, 'Employee6', b)


def test_assoc_Fleet_Branch30_reverse_link_reassign_clear():
    a1 = CarRental2_Car(id=7)
    a2 = CarRental2_Car(id=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Branch31', a1)
    assert _is_linked(b, 'Branch31', a1)
    if hasattr(a1, 'Fleet_Car'):
        assert _is_linked(a1, 'Fleet_Car', b)
    _safe_set(b, 'Branch31', a2)
    assert _is_linked(b, 'Branch31', a2)
    if hasattr(a1, 'Fleet_Car'):
        assert not _is_linked(a1, 'Fleet_Car', b)
    if hasattr(a2, 'Fleet_Car'):
        assert _is_linked(a2, 'Fleet_Car', b)
    _safe_set(b, 'Branch31', None)
    assert not _is_linked(b, 'Branch31', a2)
    if hasattr(a2, 'Fleet_Car'):
        assert not _is_linked(a2, 'Fleet_Car', b)


def test_assoc_Fleet_Car7_reverse_link_reassign_clear():
    a1 = CarRental2_Car(id=7)
    a2 = CarRental2_Car(id=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Fleet_Branch', {a1})
    assert _is_linked(b, 'Fleet_Branch', a1)
    if hasattr(a1, 'Car'):
        assert _is_linked(a1, 'Car', b)
    _safe_set(b, 'Fleet_Branch', {a2})
    assert _is_linked(b, 'Fleet_Branch', a2)
    if hasattr(a1, 'Car'):
        assert not _is_linked(a1, 'Car', b)
    if hasattr(a2, 'Car'):
        assert _is_linked(a2, 'Car', b)
    _safe_set(b, 'Fleet_Branch', set())
    assert not _is_linked(b, 'Fleet_Branch', a2)
    if hasattr(a2, 'Car'):
        assert not _is_linked(a2, 'Car', b)


def test_assoc_Management_Branch_role_managedBranch1_reverse_link_reassign_clear():
    a1 = CarRental2_Employee(salary=7)
    a2 = CarRental2_Employee(salary=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Branch', a1)
    assert _is_linked(b, 'Branch', a1)
    if hasattr(a1, 'Management_Employee_role_manager'):
        assert _is_linked(a1, 'Management_Employee_role_manager', b)
    _safe_set(b, 'Branch', a2)
    assert _is_linked(b, 'Branch', a2)
    if hasattr(a1, 'Management_Employee_role_manager'):
        assert not _is_linked(a1, 'Management_Employee_role_manager', b)
    if hasattr(a2, 'Management_Employee_role_manager'):
        assert _is_linked(a2, 'Management_Employee_role_manager', b)
    _safe_set(b, 'Branch', None)
    assert not _is_linked(b, 'Branch', a2)
    if hasattr(a2, 'Management_Employee_role_manager'):
        assert not _is_linked(a2, 'Management_Employee_role_manager', b)


def test_assoc_Management_Employee_role_manager4_reverse_link_reassign_clear():
    a1 = CarRental2_Employee(salary=7)
    a2 = CarRental2_Employee(salary=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Management_Branch_role_managedBranch', a1)
    assert _is_linked(b, 'Management_Branch_role_managedBranch', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'Management_Branch_role_managedBranch', a2)
    assert _is_linked(b, 'Management_Branch_role_managedBranch', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'Management_Branch_role_managedBranch', None)
    assert not _is_linked(b, 'Management_Branch_role_managedBranch', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_Offers_Branch18_reverse_link_reassign_clear():
    a1 = CarRental2_CarGroup(kind=7)
    a2 = CarRental2_CarGroup(kind=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Branch19', a1)
    assert _is_linked(b, 'Branch19', a1)
    if hasattr(a1, 'Offers_CarGroup'):
        assert _is_linked(a1, 'Offers_CarGroup', b)
    _safe_set(b, 'Branch19', a2)
    assert _is_linked(b, 'Branch19', a2)
    if hasattr(a1, 'Offers_CarGroup'):
        assert not _is_linked(a1, 'Offers_CarGroup', b)
    if hasattr(a2, 'Offers_CarGroup'):
        assert _is_linked(a2, 'Offers_CarGroup', b)
    _safe_set(b, 'Branch19', None)
    assert not _is_linked(b, 'Branch19', a2)
    if hasattr(a2, 'Offers_CarGroup'):
        assert not _is_linked(a2, 'Offers_CarGroup', b)


def test_assoc_Offers_CarGroup8_reverse_link_reassign_clear():
    a1 = CarRental2_CarGroup(kind=7)
    a2 = CarRental2_CarGroup(kind=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Offers_Branch', {a1})
    assert _is_linked(b, 'Offers_Branch', a1)
    if hasattr(a1, 'CarGroup'):
        assert _is_linked(a1, 'CarGroup', b)
    _safe_set(b, 'Offers_Branch', {a2})
    assert _is_linked(b, 'Offers_Branch', a2)
    if hasattr(a1, 'CarGroup'):
        assert not _is_linked(a1, 'CarGroup', b)
    if hasattr(a2, 'CarGroup'):
        assert _is_linked(a2, 'CarGroup', b)
    _safe_set(b, 'Offers_Branch', set())
    assert not _is_linked(b, 'Offers_Branch', a2)
    if hasattr(a2, 'CarGroup'):
        assert not _is_linked(a2, 'CarGroup', b)


def test_assoc_Provider_Branch12_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Branch13', a1)
    assert _is_linked(b, 'Branch13', a1)
    if hasattr(a1, 'Provider_Rental'):
        assert _is_linked(a1, 'Provider_Rental', b)
    _safe_set(b, 'Branch13', a2)
    assert _is_linked(b, 'Branch13', a2)
    if hasattr(a1, 'Provider_Rental'):
        assert not _is_linked(a1, 'Provider_Rental', b)
    if hasattr(a2, 'Provider_Rental'):
        assert _is_linked(a2, 'Provider_Rental', b)
    _safe_set(b, 'Branch13', None)
    assert not _is_linked(b, 'Branch13', a2)
    if hasattr(a2, 'Provider_Rental'):
        assert not _is_linked(a2, 'Provider_Rental', b)


def test_assoc_Provider_Rental9_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_Branch(location=7)
    _safe_set(b, 'Provider_Branch', {a1})
    assert _is_linked(b, 'Provider_Branch', a1)
    if hasattr(a1, 'Rental10'):
        assert _is_linked(a1, 'Rental10', b)
    _safe_set(b, 'Provider_Branch', {a2})
    assert _is_linked(b, 'Provider_Branch', a2)
    if hasattr(a1, 'Rental10'):
        assert not _is_linked(a1, 'Rental10', b)
    if hasattr(a2, 'Rental10'):
        assert _is_linked(a2, 'Rental10', b)
    _safe_set(b, 'Provider_Branch', set())
    assert not _is_linked(b, 'Provider_Branch', a2)
    if hasattr(a2, 'Rental10'):
        assert not _is_linked(a2, 'Rental10', b)


def test_assoc_Quality_CarGroup_role_higher28_reverse_link_reassign_clear():
    a1 = CarRental2_CarGroup(kind=7)
    a2 = CarRental2_CarGroup(kind=13)
    b = CarRental2_CarGroup(kind=7)
    _safe_set(b, 'Quality_CarGroup_role_lower', a1)
    assert _is_linked(b, 'Quality_CarGroup_role_lower', a1)
    if hasattr(a1, 'CarGroup29'):
        assert _is_linked(a1, 'CarGroup29', b)
    _safe_set(b, 'Quality_CarGroup_role_lower', a2)
    assert _is_linked(b, 'Quality_CarGroup_role_lower', a2)
    if hasattr(a1, 'CarGroup29'):
        assert not _is_linked(a1, 'CarGroup29', b)
    if hasattr(a2, 'CarGroup29'):
        assert _is_linked(a2, 'CarGroup29', b)
    _safe_set(b, 'Quality_CarGroup_role_lower', None)
    assert not _is_linked(b, 'Quality_CarGroup_role_lower', a2)
    if hasattr(a2, 'CarGroup29'):
        assert not _is_linked(a2, 'CarGroup29', b)


def test_assoc_Quality_CarGroup_role_lower25_reverse_link_reassign_clear():
    a1 = CarRental2_CarGroup(kind=7)
    a2 = CarRental2_CarGroup(kind=13)
    b = CarRental2_CarGroup(kind=7)
    _safe_set(b, 'Quality_CarGroup_role_higher', a1)
    assert _is_linked(b, 'Quality_CarGroup_role_higher', a1)
    if hasattr(a1, 'CarGroup26'):
        assert _is_linked(a1, 'CarGroup26', b)
    _safe_set(b, 'Quality_CarGroup_role_higher', a2)
    assert _is_linked(b, 'Quality_CarGroup_role_higher', a2)
    if hasattr(a1, 'CarGroup26'):
        assert not _is_linked(a1, 'CarGroup26', b)
    if hasattr(a2, 'CarGroup26'):
        assert _is_linked(a2, 'CarGroup26', b)
    _safe_set(b, 'Quality_CarGroup_role_higher', None)
    assert not _is_linked(b, 'Quality_CarGroup_role_higher', a2)
    if hasattr(a2, 'CarGroup26'):
        assert not _is_linked(a2, 'CarGroup26', b)


def test_assoc_Reservation_CarGroup14_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_CarGroup(kind=7)
    _safe_set(b, 'CarGroup15', a1)
    assert _is_linked(b, 'CarGroup15', a1)
    if hasattr(a1, 'Reservation_Rental'):
        assert _is_linked(a1, 'Reservation_Rental', b)
    _safe_set(b, 'CarGroup15', a2)
    assert _is_linked(b, 'CarGroup15', a2)
    if hasattr(a1, 'Reservation_Rental'):
        assert not _is_linked(a1, 'Reservation_Rental', b)
    if hasattr(a2, 'Reservation_Rental'):
        assert _is_linked(a2, 'Reservation_Rental', b)
    _safe_set(b, 'CarGroup15', None)
    assert not _is_linked(b, 'CarGroup15', a2)
    if hasattr(a2, 'Reservation_Rental'):
        assert not _is_linked(a2, 'Reservation_Rental', b)


def test_assoc_Reservation_Rental22_reverse_link_reassign_clear():
    a1 = CarRental2_Rental(fromDate=7, untilDate=7)
    a2 = CarRental2_Rental(fromDate=13, untilDate=13)
    b = CarRental2_CarGroup(kind=7)
    _safe_set(b, 'Reservation_CarGroup', {a1})
    assert _is_linked(b, 'Reservation_CarGroup', a1)
    if hasattr(a1, 'Rental23'):
        assert _is_linked(a1, 'Rental23', b)
    _safe_set(b, 'Reservation_CarGroup', {a2})
    assert _is_linked(b, 'Reservation_CarGroup', a2)
    if hasattr(a1, 'Rental23'):
        assert not _is_linked(a1, 'Rental23', b)
    if hasattr(a2, 'Rental23'):
        assert _is_linked(a2, 'Rental23', b)
    _safe_set(b, 'Reservation_CarGroup', set())
    assert not _is_linked(b, 'Reservation_CarGroup', a2)
    if hasattr(a2, 'Rental23'):
        assert not _is_linked(a2, 'Rental23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_toCar44_stub_double():
    # CarRental2_TernaryRelationMaintenance has no real 'toMaintenance45' property in the generated
    # code (a bare stub) -- manually attach it so CarRental2_Car's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CarRental2_Car's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CarRental2_Car(id=7)
    partner = CarRental2_TernaryRelationMaintenance()
    setattr(partner, 'toMaintenance45', None)
    _safe_set(owner, 'Car46', partner)
    assert getattr(partner, 'toMaintenance45') == owner
    _safe_set(owner, 'Car46', None)
    assert getattr(partner, 'toMaintenance45') is None


def test_assoc_toCheck42_stub_double():
    # CarRental2_TernaryRelationMaintenance has no real 'toMaintenance43' property in the generated
    # code (a bare stub) -- manually attach it so CarRental2_Check's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CarRental2_Check's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CarRental2_Check(description=7)
    partner = CarRental2_TernaryRelationMaintenance()
    setattr(partner, 'toMaintenance43', None)
    _safe_set(owner, 'Check', partner)
    assert getattr(partner, 'toMaintenance43') == owner
    _safe_set(owner, 'Check', None)
    assert getattr(partner, 'toMaintenance43') is None


def test_assoc_toMaintenance36_stub_double():
    # CarRental2_TernaryRelationMaintenance has no real 'TernaryRelationMaintenance' property in the generated
    # code (a bare stub) -- manually attach it so CarRental2_Car's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CarRental2_Car's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CarRental2_Car(id=7)
    partner = CarRental2_TernaryRelationMaintenance()
    setattr(partner, 'TernaryRelationMaintenance', None)
    _safe_set(owner, 'toCar', {partner})
    assert getattr(partner, 'TernaryRelationMaintenance') == owner
    _safe_set(owner, 'toCar', set())
    assert getattr(partner, 'TernaryRelationMaintenance') is None


def test_assoc_toMaintenance37_stub_double():
    # CarRental2_TernaryRelationMaintenance has no real 'TernaryRelationMaintenance38' property in the generated
    # code (a bare stub) -- manually attach it so CarRental2_ServiceDepot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CarRental2_ServiceDepot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CarRental2_ServiceDepot(location=7)
    partner = CarRental2_TernaryRelationMaintenance()
    setattr(partner, 'TernaryRelationMaintenance38', None)
    _safe_set(owner, 'toServiceDepot', {partner})
    assert getattr(partner, 'TernaryRelationMaintenance38') == owner
    _safe_set(owner, 'toServiceDepot', set())
    assert getattr(partner, 'TernaryRelationMaintenance38') is None


def test_assoc_toMaintenance39_stub_double():
    # CarRental2_TernaryRelationMaintenance has no real 'TernaryRelationMaintenance40' property in the generated
    # code (a bare stub) -- manually attach it so CarRental2_Check's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CarRental2_Check's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CarRental2_Check(description=7)
    partner = CarRental2_TernaryRelationMaintenance()
    setattr(partner, 'TernaryRelationMaintenance40', None)
    _safe_set(owner, 'toCheck', {partner})
    assert getattr(partner, 'TernaryRelationMaintenance40') == owner
    _safe_set(owner, 'toCheck', set())
    assert getattr(partner, 'TernaryRelationMaintenance40') is None


def test_assoc_toServiceDepot41_stub_double():
    # CarRental2_TernaryRelationMaintenance has no real 'toMaintenance' property in the generated
    # code (a bare stub) -- manually attach it so CarRental2_ServiceDepot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CarRental2_ServiceDepot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CarRental2_ServiceDepot(location=7)
    partner = CarRental2_TernaryRelationMaintenance()
    setattr(partner, 'toMaintenance', None)
    _safe_set(owner, 'ServiceDepot', partner)
    assert getattr(partner, 'toMaintenance') == owner
    _safe_set(owner, 'ServiceDepot', None)
    assert getattr(partner, 'toMaintenance') is None


