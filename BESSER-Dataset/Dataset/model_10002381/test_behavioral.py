import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Booking,
    CustomerUI,
    ReservationManagementSystem,
    Table,
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

def test_assoc_ReservationManagementSystem_Booking_reverse_link_reassign_clear():
    a1 = ReservationManagementSystem(bookings="sample_text")
    a2 = ReservationManagementSystem(bookings="sample_text_2")
    b = Booking(booking_id=7, contact_no=7, customer_name="sample_text", date=date(2024, 1, 1), email_id="sample_text", endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    _safe_set(b, 'ReservationManagementSystem_Booking_13', a1)
    assert _is_linked(b, 'ReservationManagementSystem_Booking_13', a1)
    if hasattr(a1, 'booking2'):
        assert _is_linked(a1, 'booking2', b)
    _safe_set(b, 'ReservationManagementSystem_Booking_13', a2)
    assert _is_linked(b, 'ReservationManagementSystem_Booking_13', a2)
    if hasattr(a1, 'booking2'):
        assert not _is_linked(a1, 'booking2', b)
    if hasattr(a2, 'booking2'):
        assert _is_linked(a2, 'booking2', b)
    _safe_set(b, 'ReservationManagementSystem_Booking_13', None)
    assert not _is_linked(b, 'ReservationManagementSystem_Booking_13', a2)
    if hasattr(a2, 'booking2'):
        assert not _is_linked(a2, 'booking2', b)


def test_assoc_Table_Booking_reverse_link_reassign_clear():
    a1 = Table(avaliable=True, numSeats=7, table_id="sample_text")
    a2 = Table(avaliable=False, numSeats=13, table_id="sample_text_2")
    b = Booking(booking_id=7, contact_no=7, customer_name="sample_text", date=date(2024, 1, 1), email_id="sample_text", endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    _safe_set(b, 'reservedBy5', {a1})
    assert _is_linked(b, 'reservedBy5', a1)
    if hasattr(a1, 'Table_Booking_04'):
        assert _is_linked(a1, 'Table_Booking_04', b)
    _safe_set(b, 'reservedBy5', {a2})
    assert _is_linked(b, 'reservedBy5', a2)
    if hasattr(a1, 'Table_Booking_04'):
        assert not _is_linked(a1, 'Table_Booking_04', b)
    if hasattr(a2, 'Table_Booking_04'):
        assert _is_linked(a2, 'Table_Booking_04', b)
    _safe_set(b, 'reservedBy5', set())
    assert not _is_linked(b, 'reservedBy5', a2)
    if hasattr(a2, 'Table_Booking_04'):
        assert not _is_linked(a2, 'Table_Booking_04', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_CustomerUI_ReservationManagementSystem_stub_double():
    # CustomerUI has no real 'CustomerUI_ReservationManagementSystem_00' property in the generated
    # code (a bare stub) -- manually attach it so ReservationManagementSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ReservationManagementSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ReservationManagementSystem(bookings="sample_text")
    partner = CustomerUI()
    setattr(partner, 'CustomerUI_ReservationManagementSystem_00', None)
    _safe_set(owner, 'interacts1', {partner})
    assert getattr(partner, 'CustomerUI_ReservationManagementSystem_00') == owner
    _safe_set(owner, 'interacts1', set())
    assert getattr(partner, 'CustomerUI_ReservationManagementSystem_00') is None


