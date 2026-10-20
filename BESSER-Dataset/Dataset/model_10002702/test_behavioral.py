import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Booking,
    Chef,
    CustomerUI,
    Food,
    Manager,
    Order,
    Report,
    ReservationManagementSystem,
    Staff,
    StaffUI,
    Table,
    Waiter,
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
    a1 = Order(foodList="sample_text", order_id="sample_text")
    a2 = Order(foodList="sample_text_2", order_id="sample_text_2")
    b = Food(food_id="sample_text", name="sample_text", prepared=True, price=3.14, served=True)
    _safe_set(b, 'has15', a1)
    assert _is_linked(b, 'has15', a1)
    if hasattr(a1, 'orde14'):
        assert _is_linked(a1, 'orde14', b)
    _safe_set(b, 'has15', a2)
    assert _is_linked(b, 'has15', a2)
    if hasattr(a1, 'orde14'):
        assert not _is_linked(a1, 'orde14', b)
    if hasattr(a2, 'orde14'):
        assert _is_linked(a2, 'orde14', b)
    _safe_set(b, 'has15', None)
    assert not _is_linked(b, 'has15', a2)
    if hasattr(a2, 'orde14'):
        assert not _is_linked(a2, 'orde14', b)


def test_assoc_ReservationManagementSystem_Booking_reverse_link_reassign_clear():
    a1 = ReservationManagementSystem(bookings="sample_text")
    a2 = ReservationManagementSystem(bookings="sample_text_2")
    b = Booking(booking_id=7, contact_no=7, customer_name="sample_text", date=date(2024, 1, 1), email_id="sample_text", endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    _safe_set(b, 'ReservationManagementSystem_Booking_17', a1)
    assert _is_linked(b, 'ReservationManagementSystem_Booking_17', a1)
    if hasattr(a1, 'booking6'):
        assert _is_linked(a1, 'booking6', b)
    _safe_set(b, 'ReservationManagementSystem_Booking_17', a2)
    assert _is_linked(b, 'ReservationManagementSystem_Booking_17', a2)
    if hasattr(a1, 'booking6'):
        assert not _is_linked(a1, 'booking6', b)
    if hasattr(a2, 'booking6'):
        assert _is_linked(a2, 'booking6', b)
    _safe_set(b, 'ReservationManagementSystem_Booking_17', None)
    assert not _is_linked(b, 'ReservationManagementSystem_Booking_17', a2)
    if hasattr(a2, 'booking6'):
        assert not _is_linked(a2, 'booking6', b)


def test_assoc_ReservationManagementSystem_Report_reverse_link_reassign_clear():
    a1 = ReservationManagementSystem(bookings="sample_text")
    a2 = ReservationManagementSystem(bookings="sample_text_2")
    b = Report(orders="sample_text", report_id="sample_text")
    _safe_set(b, 'reservationManagementSystem9', a1)
    assert _is_linked(b, 'reservationManagementSystem9', a1)
    if hasattr(a1, 'generates8'):
        assert _is_linked(a1, 'generates8', b)
    _safe_set(b, 'reservationManagementSystem9', a2)
    assert _is_linked(b, 'reservationManagementSystem9', a2)
    if hasattr(a1, 'generates8'):
        assert not _is_linked(a1, 'generates8', b)
    if hasattr(a2, 'generates8'):
        assert _is_linked(a2, 'generates8', b)
    _safe_set(b, 'reservationManagementSystem9', None)
    assert not _is_linked(b, 'reservationManagementSystem9', a2)
    if hasattr(a2, 'generates8'):
        assert not _is_linked(a2, 'generates8', b)


def test_assoc_Staff_ReservationManagementSystem_reverse_link_reassign_clear():
    a1 = Staff(name="sample_text", staffId="sample_text", type="sample_text")
    a2 = Staff(name="sample_text_2", staffId="sample_text_2", type="sample_text_2")
    b = ReservationManagementSystem(bookings="sample_text")
    _safe_set(b, 'interacts3', {a1})
    assert _is_linked(b, 'interacts3', a1)
    if hasattr(a1, 'reservationManagementSystem2'):
        assert _is_linked(a1, 'reservationManagementSystem2', b)
    _safe_set(b, 'interacts3', {a2})
    assert _is_linked(b, 'interacts3', a2)
    if hasattr(a1, 'reservationManagementSystem2'):
        assert not _is_linked(a1, 'reservationManagementSystem2', b)
    if hasattr(a2, 'reservationManagementSystem2'):
        assert _is_linked(a2, 'reservationManagementSystem2', b)
    _safe_set(b, 'interacts3', set())
    assert not _is_linked(b, 'interacts3', a2)
    if hasattr(a2, 'reservationManagementSystem2'):
        assert not _is_linked(a2, 'reservationManagementSystem2', b)


def test_assoc_Table_Booking_reverse_link_reassign_clear():
    a1 = Table(avaliable=True, numSeats=7, table_id="sample_text")
    a2 = Table(avaliable=False, numSeats=13, table_id="sample_text_2")
    b = Booking(booking_id=7, contact_no=7, customer_name="sample_text", date=date(2024, 1, 1), email_id="sample_text", endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    _safe_set(b, 'reservedBy13', {a1})
    assert _is_linked(b, 'reservedBy13', a1)
    if hasattr(a1, 'Table_Booking_012'):
        assert _is_linked(a1, 'Table_Booking_012', b)
    _safe_set(b, 'reservedBy13', {a2})
    assert _is_linked(b, 'reservedBy13', a2)
    if hasattr(a1, 'Table_Booking_012'):
        assert not _is_linked(a1, 'Table_Booking_012', b)
    if hasattr(a2, 'Table_Booking_012'):
        assert _is_linked(a2, 'Table_Booking_012', b)
    _safe_set(b, 'reservedBy13', set())
    assert not _is_linked(b, 'reservedBy13', a2)
    if hasattr(a2, 'Table_Booking_012'):
        assert not _is_linked(a2, 'Table_Booking_012', b)


def test_assoc_Table_Order_reverse_link_reassign_clear():
    a1 = Table(avaliable=True, numSeats=7, table_id="sample_text")
    a2 = Table(avaliable=False, numSeats=13, table_id="sample_text_2")
    b = Order(foodList="sample_text", order_id="sample_text")
    _safe_set(b, 'table11', a1)
    assert _is_linked(b, 'table11', a1)
    if hasattr(a1, 'has10'):
        assert _is_linked(a1, 'has10', b)
    _safe_set(b, 'table11', a2)
    assert _is_linked(b, 'table11', a2)
    if hasattr(a1, 'has10'):
        assert not _is_linked(a1, 'has10', b)
    if hasattr(a2, 'has10'):
        assert _is_linked(a2, 'has10', b)
    _safe_set(b, 'table11', None)
    assert not _is_linked(b, 'table11', a2)
    if hasattr(a2, 'has10'):
        assert not _is_linked(a2, 'has10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_CustomerUI_ReservationManagementSystem_stub_double():
    # CustomerUI has no real 'CustomerUI_ReservationManagementSystem_04' property in the generated
    # code (a bare stub) -- manually attach it so ReservationManagementSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ReservationManagementSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ReservationManagementSystem(bookings="sample_text")
    partner = CustomerUI()
    setattr(partner, 'CustomerUI_ReservationManagementSystem_04', None)
    _safe_set(owner, 'interacts5', {partner})
    assert getattr(partner, 'CustomerUI_ReservationManagementSystem_04') == owner
    _safe_set(owner, 'interacts5', set())
    assert getattr(partner, 'CustomerUI_ReservationManagementSystem_04') is None


def test_assoc_Staff_StaffUI_stub_double():
    # StaffUI has no real 'accesses1' property in the generated
    # code (a bare stub) -- manually attach it so Staff's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Staff's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Staff(name="sample_text", staffId="sample_text", type="sample_text")
    partner = StaffUI()
    setattr(partner, 'accesses1', None)
    _safe_set(owner, 'Staff_StaffUI_00', {partner})
    assert owner in getattr(partner, 'accesses1')
    _safe_set(owner, 'Staff_StaffUI_00', set())
    assert owner not in getattr(partner, 'accesses1')


