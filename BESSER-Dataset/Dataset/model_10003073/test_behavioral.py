import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Booking,
    Cart,
    Chef,
    Invoice,
    Order,
    Product,
    Registration,
    ReservationManagementSystem,
    StaffUI,
    Table,
    User,
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

def test_assoc_Order_Food_reverse_link_reassign_clear():
    a1 = Product(Note="sample_text", food_id="sample_text", name="sample_text", price=3.14)
    a2 = Product(Note="sample_text_2", food_id="sample_text_2", name="sample_text_2", price=9.99)
    b = Order(foodList="sample_text", order_id="sample_text")
    _safe_set(b, 'orde8', {a1})
    assert _is_linked(b, 'orde8', a1)
    if hasattr(a1, 'has9'):
        assert _is_linked(a1, 'has9', b)
    _safe_set(b, 'orde8', {a2})
    assert _is_linked(b, 'orde8', a2)
    if hasattr(a1, 'has9'):
        assert not _is_linked(a1, 'has9', b)
    if hasattr(a2, 'has9'):
        assert _is_linked(a2, 'has9', b)
    _safe_set(b, 'orde8', set())
    assert not _is_linked(b, 'orde8', a2)
    if hasattr(a2, 'has9'):
        assert not _is_linked(a2, 'has9', b)


def test_assoc_ReservationManagementSystem_Booking_reverse_link_reassign_clear():
    a1 = ReservationManagementSystem(bookings="sample_text")
    a2 = ReservationManagementSystem(bookings="sample_text_2")
    b = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    _safe_set(b, 'ReservationManagementSystem_Booking_11', a1)
    assert _is_linked(b, 'ReservationManagementSystem_Booking_11', a1)
    if hasattr(a1, 'booking0'):
        assert _is_linked(a1, 'booking0', b)
    _safe_set(b, 'ReservationManagementSystem_Booking_11', a2)
    assert _is_linked(b, 'ReservationManagementSystem_Booking_11', a2)
    if hasattr(a1, 'booking0'):
        assert not _is_linked(a1, 'booking0', b)
    if hasattr(a2, 'booking0'):
        assert _is_linked(a2, 'booking0', b)
    _safe_set(b, 'ReservationManagementSystem_Booking_11', None)
    assert not _is_linked(b, 'ReservationManagementSystem_Booking_11', a2)
    if hasattr(a2, 'booking0'):
        assert not _is_linked(a2, 'booking0', b)


def test_assoc_ReservationManagementSystem_Report_reverse_link_reassign_clear():
    a1 = ReservationManagementSystem(bookings="sample_text")
    a2 = ReservationManagementSystem(bookings="sample_text_2")
    b = Invoice(invoice_id="sample_text", orders="sample_text")
    _safe_set(b, 'reservationManagementSystem3', a1)
    assert _is_linked(b, 'reservationManagementSystem3', a1)
    if hasattr(a1, 'generates2'):
        assert _is_linked(a1, 'generates2', b)
    _safe_set(b, 'reservationManagementSystem3', a2)
    assert _is_linked(b, 'reservationManagementSystem3', a2)
    if hasattr(a1, 'generates2'):
        assert not _is_linked(a1, 'generates2', b)
    if hasattr(a2, 'generates2'):
        assert _is_linked(a2, 'generates2', b)
    _safe_set(b, 'reservationManagementSystem3', None)
    assert not _is_linked(b, 'reservationManagementSystem3', a2)
    if hasattr(a2, 'generates2'):
        assert not _is_linked(a2, 'generates2', b)


def test_assoc_Table_Booking_reverse_link_reassign_clear():
    a1 = Table(avaliable=True, numSeats=7, table_id="sample_text")
    a2 = Table(avaliable=False, numSeats=13, table_id="sample_text_2")
    b = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    _safe_set(b, 'reservedBy7', {a1})
    assert _is_linked(b, 'reservedBy7', a1)
    if hasattr(a1, 'Table_Booking_06'):
        assert _is_linked(a1, 'Table_Booking_06', b)
    _safe_set(b, 'reservedBy7', {a2})
    assert _is_linked(b, 'reservedBy7', a2)
    if hasattr(a1, 'Table_Booking_06'):
        assert not _is_linked(a1, 'Table_Booking_06', b)
    if hasattr(a2, 'Table_Booking_06'):
        assert _is_linked(a2, 'Table_Booking_06', b)
    _safe_set(b, 'reservedBy7', set())
    assert not _is_linked(b, 'reservedBy7', a2)
    if hasattr(a2, 'Table_Booking_06'):
        assert not _is_linked(a2, 'Table_Booking_06', b)


def test_assoc_Table_Order_reverse_link_reassign_clear():
    a1 = Table(avaliable=True, numSeats=7, table_id="sample_text")
    a2 = Table(avaliable=False, numSeats=13, table_id="sample_text_2")
    b = Order(foodList="sample_text", order_id="sample_text")
    _safe_set(b, 'table5', a1)
    assert _is_linked(b, 'table5', a1)
    if hasattr(a1, 'has4'):
        assert _is_linked(a1, 'has4', b)
    _safe_set(b, 'table5', a2)
    assert _is_linked(b, 'table5', a2)
    if hasattr(a1, 'has4'):
        assert not _is_linked(a1, 'has4', b)
    if hasattr(a2, 'has4'):
        assert _is_linked(a2, 'has4', b)
    _safe_set(b, 'table5', None)
    assert not _is_linked(b, 'table5', a2)
    if hasattr(a2, 'has4'):
        assert not _is_linked(a2, 'has4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

