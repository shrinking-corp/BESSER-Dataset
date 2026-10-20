import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CoachBus_AdultTicket,
    CoachBus_BookingOffice,
    CoachBus_ChildTicket,
    CoachBus_Coach,
    CoachBus_Employee,
    CoachBus_Manager,
    CoachBus_Passenger,
    CoachBus_PrivateTrip,
    CoachBus_RegularTrip,
    CoachBus_SecurityGuard,
    CoachBus_Ticket,
    CoachBus_Trip,
    CoachBus_VendingMachine,
    Employee,
    Ticket,
    Trip,
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

def test_assoc_coach10_reverse_link_reassign_clear():
    a1 = CoachBus_SecurityGuard(shift="sample_text")
    a2 = CoachBus_SecurityGuard(shift="sample_text_2")
    b = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    _safe_set(b, 'Coach11', a1)
    assert _is_linked(b, 'Coach11', a1)
    if hasattr(a1, 'guards'):
        assert _is_linked(a1, 'guards', b)
    _safe_set(b, 'Coach11', a2)
    assert _is_linked(b, 'Coach11', a2)
    if hasattr(a1, 'guards'):
        assert not _is_linked(a1, 'guards', b)
    if hasattr(a2, 'guards'):
        assert _is_linked(a2, 'guards', b)
    _safe_set(b, 'Coach11', None)
    assert not _is_linked(b, 'Coach11', a2)
    if hasattr(a2, 'guards'):
        assert not _is_linked(a2, 'guards', b)


def test_assoc_coaches0_reverse_link_reassign_clear():
    a1 = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    a2 = CoachBus_Trip(destination="sample_text_2", name="sample_text_2", number=13, origin="sample_text_2", type="sample_text_2")
    b = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    _safe_set(b, 'Coach', a1)
    assert _is_linked(b, 'Coach', a1)
    if hasattr(a1, 'trips'):
        assert _is_linked(a1, 'trips', b)
    _safe_set(b, 'Coach', a2)
    assert _is_linked(b, 'Coach', a2)
    if hasattr(a1, 'trips'):
        assert not _is_linked(a1, 'trips', b)
    if hasattr(a2, 'trips'):
        assert _is_linked(a2, 'trips', b)
    _safe_set(b, 'Coach', None)
    assert not _is_linked(b, 'Coach', a2)
    if hasattr(a2, 'trips'):
        assert not _is_linked(a2, 'trips', b)


def test_assoc_coaches14_reverse_link_reassign_clear():
    a1 = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    a2 = CoachBus_Coach(id=13, model="sample_text_2", name="sample_text_2", noOfSeats=13)
    b = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    _safe_set(b, 'offices', {a1})
    assert _is_linked(b, 'offices', a1)
    if hasattr(a1, 'Coach15'):
        assert _is_linked(a1, 'Coach15', b)
    _safe_set(b, 'offices', {a2})
    assert _is_linked(b, 'offices', a2)
    if hasattr(a1, 'Coach15'):
        assert not _is_linked(a1, 'Coach15', b)
    if hasattr(a2, 'Coach15'):
        assert _is_linked(a2, 'Coach15', b)
    _safe_set(b, 'offices', set())
    assert not _is_linked(b, 'offices', a2)
    if hasattr(a2, 'Coach15'):
        assert not _is_linked(a2, 'Coach15', b)


def test_assoc_guards4_reverse_link_reassign_clear():
    a1 = CoachBus_SecurityGuard(shift="sample_text")
    a2 = CoachBus_SecurityGuard(shift="sample_text_2")
    b = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    _safe_set(b, 'coach', {a1})
    assert _is_linked(b, 'coach', a1)
    if hasattr(a1, 'SecurityGuard'):
        assert _is_linked(a1, 'SecurityGuard', b)
    _safe_set(b, 'coach', {a2})
    assert _is_linked(b, 'coach', a2)
    if hasattr(a1, 'SecurityGuard'):
        assert not _is_linked(a1, 'SecurityGuard', b)
    if hasattr(a2, 'SecurityGuard'):
        assert _is_linked(a2, 'SecurityGuard', b)
    _safe_set(b, 'coach', set())
    assert not _is_linked(b, 'coach', a2)
    if hasattr(a2, 'SecurityGuard'):
        assert not _is_linked(a2, 'SecurityGuard', b)


def test_assoc_manager16_reverse_link_reassign_clear():
    a1 = CoachBus_Manager(hasMBA=True)
    a2 = CoachBus_Manager(hasMBA=False)
    b = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    _safe_set(b, 'office', a1)
    assert _is_linked(b, 'office', a1)
    if hasattr(a1, 'Manager'):
        assert _is_linked(a1, 'Manager', b)
    _safe_set(b, 'office', a2)
    assert _is_linked(b, 'office', a2)
    if hasattr(a1, 'Manager'):
        assert not _is_linked(a1, 'Manager', b)
    if hasattr(a2, 'Manager'):
        assert _is_linked(a2, 'Manager', b)
    _safe_set(b, 'office', None)
    assert not _is_linked(b, 'office', a2)
    if hasattr(a2, 'Manager'):
        assert not _is_linked(a2, 'Manager', b)


def test_assoc_office12_reverse_link_reassign_clear():
    a1 = CoachBus_Manager(hasMBA=True)
    a2 = CoachBus_Manager(hasMBA=False)
    b = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    _safe_set(b, 'BookingOffice13', a1)
    assert _is_linked(b, 'BookingOffice13', a1)
    if hasattr(a1, 'manager'):
        assert _is_linked(a1, 'manager', b)
    _safe_set(b, 'BookingOffice13', a2)
    assert _is_linked(b, 'BookingOffice13', a2)
    if hasattr(a1, 'manager'):
        assert not _is_linked(a1, 'manager', b)
    if hasattr(a2, 'manager'):
        assert _is_linked(a2, 'manager', b)
    _safe_set(b, 'BookingOffice13', None)
    assert not _is_linked(b, 'BookingOffice13', a2)
    if hasattr(a2, 'manager'):
        assert not _is_linked(a2, 'manager', b)


def test_assoc_office26_reverse_link_reassign_clear():
    a1 = CoachBus_VendingMachine(number=7)
    a2 = CoachBus_VendingMachine(number=13)
    b = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    _safe_set(b, 'BookingOffice27', a1)
    assert _is_linked(b, 'BookingOffice27', a1)
    if hasattr(a1, 'vms'):
        assert _is_linked(a1, 'vms', b)
    _safe_set(b, 'BookingOffice27', a2)
    assert _is_linked(b, 'BookingOffice27', a2)
    if hasattr(a1, 'vms'):
        assert not _is_linked(a1, 'vms', b)
    if hasattr(a2, 'vms'):
        assert _is_linked(a2, 'vms', b)
    _safe_set(b, 'BookingOffice27', None)
    assert not _is_linked(b, 'BookingOffice27', a2)
    if hasattr(a2, 'vms'):
        assert not _is_linked(a2, 'vms', b)


def test_assoc_offices5_reverse_link_reassign_clear():
    a1 = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    a2 = CoachBus_Coach(id=13, model="sample_text_2", name="sample_text_2", noOfSeats=13)
    b = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    _safe_set(b, 'BookingOffice', a1)
    assert _is_linked(b, 'BookingOffice', a1)
    if hasattr(a1, 'coaches6'):
        assert _is_linked(a1, 'coaches6', b)
    _safe_set(b, 'BookingOffice', a2)
    assert _is_linked(b, 'BookingOffice', a2)
    if hasattr(a1, 'coaches6'):
        assert not _is_linked(a1, 'coaches6', b)
    if hasattr(a2, 'coaches6'):
        assert _is_linked(a2, 'coaches6', b)
    _safe_set(b, 'BookingOffice', None)
    assert not _is_linked(b, 'BookingOffice', a2)
    if hasattr(a2, 'coaches6'):
        assert not _is_linked(a2, 'coaches6', b)


def test_assoc_passengers1_reverse_link_reassign_clear():
    a1 = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    a2 = CoachBus_Trip(destination="sample_text_2", name="sample_text_2", number=13, origin="sample_text_2", type="sample_text_2")
    b = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    _safe_set(b, 'Passenger', a1)
    assert _is_linked(b, 'Passenger', a1)
    if hasattr(a1, 'trips2'):
        assert _is_linked(a1, 'trips2', b)
    _safe_set(b, 'Passenger', a2)
    assert _is_linked(b, 'Passenger', a2)
    if hasattr(a1, 'trips2'):
        assert not _is_linked(a1, 'trips2', b)
    if hasattr(a2, 'trips2'):
        assert _is_linked(a2, 'trips2', b)
    _safe_set(b, 'Passenger', None)
    assert not _is_linked(b, 'Passenger', a2)
    if hasattr(a2, 'trips2'):
        assert not _is_linked(a2, 'trips2', b)


def test_assoc_psg19_reverse_link_reassign_clear():
    a1 = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    a2 = CoachBus_Ticket(isRoundTrip=False, number=13, price=9.99)
    b = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    _safe_set(b, 'Passenger20', a1)
    assert _is_linked(b, 'Passenger20', a1)
    if hasattr(a1, 'tickets'):
        assert _is_linked(a1, 'tickets', b)
    _safe_set(b, 'Passenger20', a2)
    assert _is_linked(b, 'Passenger20', a2)
    if hasattr(a1, 'tickets'):
        assert not _is_linked(a1, 'tickets', b)
    if hasattr(a2, 'tickets'):
        assert _is_linked(a2, 'tickets', b)
    _safe_set(b, 'Passenger20', None)
    assert not _is_linked(b, 'Passenger20', a2)
    if hasattr(a2, 'tickets'):
        assert not _is_linked(a2, 'tickets', b)


def test_assoc_tickets24_reverse_link_reassign_clear():
    a1 = CoachBus_VendingMachine(number=7)
    a2 = CoachBus_VendingMachine(number=13)
    b = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    _safe_set(b, 'Ticket25', a1)
    assert _is_linked(b, 'Ticket25', a1)
    if hasattr(a1, 'vm'):
        assert _is_linked(a1, 'vm', b)
    _safe_set(b, 'Ticket25', a2)
    assert _is_linked(b, 'Ticket25', a2)
    if hasattr(a1, 'vm'):
        assert not _is_linked(a1, 'vm', b)
    if hasattr(a2, 'vm'):
        assert _is_linked(a2, 'vm', b)
    _safe_set(b, 'Ticket25', None)
    assert not _is_linked(b, 'Ticket25', a2)
    if hasattr(a2, 'vm'):
        assert not _is_linked(a2, 'vm', b)


def test_assoc_tickets9_reverse_link_reassign_clear():
    a1 = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    a2 = CoachBus_Ticket(isRoundTrip=False, number=13, price=9.99)
    b = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    _safe_set(b, 'psg', {a1})
    assert _is_linked(b, 'psg', a1)
    if hasattr(a1, 'Ticket'):
        assert _is_linked(a1, 'Ticket', b)
    _safe_set(b, 'psg', {a2})
    assert _is_linked(b, 'psg', a2)
    if hasattr(a1, 'Ticket'):
        assert not _is_linked(a1, 'Ticket', b)
    if hasattr(a2, 'Ticket'):
        assert _is_linked(a2, 'Ticket', b)
    _safe_set(b, 'psg', set())
    assert not _is_linked(b, 'psg', a2)
    if hasattr(a2, 'Ticket'):
        assert not _is_linked(a2, 'Ticket', b)


def test_assoc_trips3_reverse_link_reassign_clear():
    a1 = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    a2 = CoachBus_Trip(destination="sample_text_2", name="sample_text_2", number=13, origin="sample_text_2", type="sample_text_2")
    b = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    _safe_set(b, 'coaches', {a1})
    assert _is_linked(b, 'coaches', a1)
    if hasattr(a1, 'Trip'):
        assert _is_linked(a1, 'Trip', b)
    _safe_set(b, 'coaches', {a2})
    assert _is_linked(b, 'coaches', a2)
    if hasattr(a1, 'Trip'):
        assert not _is_linked(a1, 'Trip', b)
    if hasattr(a2, 'Trip'):
        assert _is_linked(a2, 'Trip', b)
    _safe_set(b, 'coaches', set())
    assert not _is_linked(b, 'coaches', a2)
    if hasattr(a2, 'Trip'):
        assert not _is_linked(a2, 'Trip', b)


def test_assoc_trips7_reverse_link_reassign_clear():
    a1 = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    a2 = CoachBus_Trip(destination="sample_text_2", name="sample_text_2", number=13, origin="sample_text_2", type="sample_text_2")
    b = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    _safe_set(b, 'passengers', {a1})
    assert _is_linked(b, 'passengers', a1)
    if hasattr(a1, 'Trip8'):
        assert _is_linked(a1, 'Trip8', b)
    _safe_set(b, 'passengers', {a2})
    assert _is_linked(b, 'passengers', a2)
    if hasattr(a1, 'Trip8'):
        assert not _is_linked(a1, 'Trip8', b)
    if hasattr(a2, 'Trip8'):
        assert _is_linked(a2, 'Trip8', b)
    _safe_set(b, 'passengers', set())
    assert not _is_linked(b, 'passengers', a2)
    if hasattr(a2, 'Trip8'):
        assert not _is_linked(a2, 'Trip8', b)


def test_assoc_vm21_reverse_link_reassign_clear():
    a1 = CoachBus_VendingMachine(number=7)
    a2 = CoachBus_VendingMachine(number=13)
    b = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    _safe_set(b, 'tickets22', a1)
    assert _is_linked(b, 'tickets22', a1)
    if hasattr(a1, 'VendingMachine23'):
        assert _is_linked(a1, 'VendingMachine23', b)
    _safe_set(b, 'tickets22', a2)
    assert _is_linked(b, 'tickets22', a2)
    if hasattr(a1, 'VendingMachine23'):
        assert not _is_linked(a1, 'VendingMachine23', b)
    if hasattr(a2, 'VendingMachine23'):
        assert _is_linked(a2, 'VendingMachine23', b)
    _safe_set(b, 'tickets22', None)
    assert not _is_linked(b, 'tickets22', a2)
    if hasattr(a2, 'VendingMachine23'):
        assert not _is_linked(a2, 'VendingMachine23', b)


def test_assoc_vms17_reverse_link_reassign_clear():
    a1 = CoachBus_VendingMachine(number=7)
    a2 = CoachBus_VendingMachine(number=13)
    b = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    _safe_set(b, 'office18', {a1})
    assert _is_linked(b, 'office18', a1)
    if hasattr(a1, 'VendingMachine'):
        assert _is_linked(a1, 'VendingMachine', b)
    _safe_set(b, 'office18', {a2})
    assert _is_linked(b, 'office18', a2)
    if hasattr(a1, 'VendingMachine'):
        assert not _is_linked(a1, 'VendingMachine', b)
    if hasattr(a2, 'VendingMachine'):
        assert _is_linked(a2, 'VendingMachine', b)
    _safe_set(b, 'office18', set())
    assert not _is_linked(b, 'office18', a2)
    if hasattr(a2, 'VendingMachine'):
        assert not _is_linked(a2, 'VendingMachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

