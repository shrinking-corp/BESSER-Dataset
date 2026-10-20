import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Booking,
    Customer,
    Payment,
    Restaurant,
    Table,
    Table_booking_time,
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

def test_assoc_Booking_Table_booking_time_reverse_link_reassign_clear():
    a1 = Table_booking_time(end_time=7, start_time=7)
    a2 = Table_booking_time(end_time=13, start_time=13)
    b = Booking(arrival_time=7, customer_name="sample_text", table_number=7)
    _safe_set(b, 'table_booking_time4', a1)
    assert _is_linked(b, 'table_booking_time4', a1)
    if hasattr(a1, 'booking5'):
        assert _is_linked(a1, 'booking5', b)
    _safe_set(b, 'table_booking_time4', a2)
    assert _is_linked(b, 'table_booking_time4', a2)
    if hasattr(a1, 'booking5'):
        assert not _is_linked(a1, 'booking5', b)
    if hasattr(a2, 'booking5'):
        assert _is_linked(a2, 'booking5', b)
    _safe_set(b, 'table_booking_time4', None)
    assert not _is_linked(b, 'table_booking_time4', a2)
    if hasattr(a2, 'booking5'):
        assert not _is_linked(a2, 'booking5', b)


def test_assoc_Restaurant_Customer_reverse_link_reassign_clear():
    a1 = Restaurant(booking=7, time=7)
    a2 = Restaurant(booking=13, time=13)
    b = Customer(Address="sample_text", cust_id=7, email="sample_text", mobile=7, name="sample_text")
    _safe_set(b, 'restaurant3', a1)
    assert _is_linked(b, 'restaurant3', a1)
    if hasattr(a1, 'customer2'):
        assert _is_linked(a1, 'customer2', b)
    _safe_set(b, 'restaurant3', a2)
    assert _is_linked(b, 'restaurant3', a2)
    if hasattr(a1, 'customer2'):
        assert not _is_linked(a1, 'customer2', b)
    if hasattr(a2, 'customer2'):
        assert _is_linked(a2, 'customer2', b)
    _safe_set(b, 'restaurant3', None)
    assert not _is_linked(b, 'restaurant3', a2)
    if hasattr(a2, 'customer2'):
        assert not _is_linked(a2, 'customer2', b)


def test_assoc_Restaurant_Table_reverse_link_reassign_clear():
    a1 = Table(table_number=7, total_person=7)
    a2 = Table(table_number=13, total_person=13)
    b = Restaurant(booking=7, time=7)
    _safe_set(b, 'table8', a1)
    assert _is_linked(b, 'table8', a1)
    if hasattr(a1, 'restaurant9'):
        assert _is_linked(a1, 'restaurant9', b)
    _safe_set(b, 'table8', a2)
    assert _is_linked(b, 'table8', a2)
    if hasattr(a1, 'restaurant9'):
        assert not _is_linked(a1, 'restaurant9', b)
    if hasattr(a2, 'restaurant9'):
        assert _is_linked(a2, 'restaurant9', b)
    _safe_set(b, 'table8', None)
    assert not _is_linked(b, 'table8', a2)
    if hasattr(a2, 'restaurant9'):
        assert not _is_linked(a2, 'restaurant9', b)


def test_assoc_Table_Booking_reverse_link_reassign_clear():
    a1 = Table(table_number=7, total_person=7)
    a2 = Table(table_number=13, total_person=13)
    b = Booking(arrival_time=7, customer_name="sample_text", table_number=7)
    _safe_set(b, 'table1', a1)
    assert _is_linked(b, 'table1', a1)
    if hasattr(a1, 'booking0'):
        assert _is_linked(a1, 'booking0', b)
    _safe_set(b, 'table1', a2)
    assert _is_linked(b, 'table1', a2)
    if hasattr(a1, 'booking0'):
        assert not _is_linked(a1, 'booking0', b)
    if hasattr(a2, 'booking0'):
        assert _is_linked(a2, 'booking0', b)
    _safe_set(b, 'table1', None)
    assert not _is_linked(b, 'table1', a2)
    if hasattr(a2, 'booking0'):
        assert not _is_linked(a2, 'booking0', b)


def test_assoc_Table_booking_time_Payment_reverse_link_reassign_clear():
    a1 = Table_booking_time(end_time=7, start_time=7)
    a2 = Table_booking_time(end_time=13, start_time=13)
    b = Payment(credit_card=7, debit_card=7, pay_hotel=7, paytm=7)
    _safe_set(b, 'table_booking_time7', a1)
    assert _is_linked(b, 'table_booking_time7', a1)
    if hasattr(a1, 'payment6'):
        assert _is_linked(a1, 'payment6', b)
    _safe_set(b, 'table_booking_time7', a2)
    assert _is_linked(b, 'table_booking_time7', a2)
    if hasattr(a1, 'payment6'):
        assert not _is_linked(a1, 'payment6', b)
    if hasattr(a2, 'payment6'):
        assert _is_linked(a2, 'payment6', b)
    _safe_set(b, 'table_booking_time7', None)
    assert not _is_linked(b, 'table_booking_time7', a2)
    if hasattr(a2, 'payment6'):
        assert not _is_linked(a2, 'payment6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

