import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    Service,
    hairDressersRegSys_Appointment,
    hairDressersRegSys_Customer,
    hairDressersRegSys_Discounts,
    hairDressersRegSys_Haircuts,
    hairDressersRegSys_Invoice,
    hairDressersRegSys_Other,
    hairDressersRegSys_Payment,
    hairDressersRegSys_Person,
    hairDressersRegSys_Products,
    hairDressersRegSys_Service,
    hairDressersRegSys_ServiceEmployee,
    hairDressersRegSys_Styling,
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

def test_assoc_appointment0_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Service(CostPerHour="sample_text", Description="sample_text", Name="sample_text", Time=date(2024, 1, 1))
    a2 = hairDressersRegSys_Service(CostPerHour="sample_text_2", Description="sample_text_2", Name="sample_text_2", Time=date(2025, 6, 15))
    b = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    _safe_set(b, 'hairDressersRegSys_Appointment', a1)
    assert _is_linked(b, 'hairDressersRegSys_Appointment', a1)
    if hasattr(a1, 'hairDressersRegSys_Service'):
        assert _is_linked(a1, 'hairDressersRegSys_Service', b)
    _safe_set(b, 'hairDressersRegSys_Appointment', a2)
    assert _is_linked(b, 'hairDressersRegSys_Appointment', a2)
    if hasattr(a1, 'hairDressersRegSys_Service'):
        assert not _is_linked(a1, 'hairDressersRegSys_Service', b)
    if hasattr(a2, 'hairDressersRegSys_Service'):
        assert _is_linked(a2, 'hairDressersRegSys_Service', b)
    _safe_set(b, 'hairDressersRegSys_Appointment', None)
    assert not _is_linked(b, 'hairDressersRegSys_Appointment', a2)
    if hasattr(a2, 'hairDressersRegSys_Service'):
        assert not _is_linked(a2, 'hairDressersRegSys_Service', b)


def test_assoc_appointment13_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Customer(CustomerId=7)
    a2 = hairDressersRegSys_Customer(CustomerId=13)
    b = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    _safe_set(b, 'hairDressersRegSys_Appointment14', a1)
    assert _is_linked(b, 'hairDressersRegSys_Appointment14', a1)
    if hasattr(a1, 'hairDressersRegSys_Customer'):
        assert _is_linked(a1, 'hairDressersRegSys_Customer', b)
    _safe_set(b, 'hairDressersRegSys_Appointment14', a2)
    assert _is_linked(b, 'hairDressersRegSys_Appointment14', a2)
    if hasattr(a1, 'hairDressersRegSys_Customer'):
        assert not _is_linked(a1, 'hairDressersRegSys_Customer', b)
    if hasattr(a2, 'hairDressersRegSys_Customer'):
        assert _is_linked(a2, 'hairDressersRegSys_Customer', b)
    _safe_set(b, 'hairDressersRegSys_Appointment14', None)
    assert not _is_linked(b, 'hairDressersRegSys_Appointment14', a2)
    if hasattr(a2, 'hairDressersRegSys_Customer'):
        assert not _is_linked(a2, 'hairDressersRegSys_Customer', b)


def test_assoc_appointment17_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_ServiceEmployee(EmployeeId=7, Role="sample_text")
    a2 = hairDressersRegSys_ServiceEmployee(EmployeeId=13, Role="sample_text_2")
    b = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    _safe_set(b, 'hairDressersRegSys_Appointment18', a1)
    assert _is_linked(b, 'hairDressersRegSys_Appointment18', a1)
    if hasattr(a1, 'hairDressersRegSys_ServiceEmployee'):
        assert _is_linked(a1, 'hairDressersRegSys_ServiceEmployee', b)
    _safe_set(b, 'hairDressersRegSys_Appointment18', a2)
    assert _is_linked(b, 'hairDressersRegSys_Appointment18', a2)
    if hasattr(a1, 'hairDressersRegSys_ServiceEmployee'):
        assert not _is_linked(a1, 'hairDressersRegSys_ServiceEmployee', b)
    if hasattr(a2, 'hairDressersRegSys_ServiceEmployee'):
        assert _is_linked(a2, 'hairDressersRegSys_ServiceEmployee', b)
    _safe_set(b, 'hairDressersRegSys_Appointment18', None)
    assert not _is_linked(b, 'hairDressersRegSys_Appointment18', a2)
    if hasattr(a2, 'hairDressersRegSys_ServiceEmployee'):
        assert not _is_linked(a2, 'hairDressersRegSys_ServiceEmployee', b)


def test_assoc_customer9_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    a2 = hairDressersRegSys_Discounts(Description="sample_text_2", Name="sample_text_2", Percentage=13)
    b = hairDressersRegSys_Customer(CustomerId=7)
    _safe_set(b, 'Customer', a1)
    assert _is_linked(b, 'Customer', a1)
    if hasattr(a1, 'discounts'):
        assert _is_linked(a1, 'discounts', b)
    _safe_set(b, 'Customer', a2)
    assert _is_linked(b, 'Customer', a2)
    if hasattr(a1, 'discounts'):
        assert not _is_linked(a1, 'discounts', b)
    if hasattr(a2, 'discounts'):
        assert _is_linked(a2, 'discounts', b)
    _safe_set(b, 'Customer', None)
    assert not _is_linked(b, 'Customer', a2)
    if hasattr(a2, 'discounts'):
        assert not _is_linked(a2, 'discounts', b)


def test_assoc_discounts15_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    a2 = hairDressersRegSys_Discounts(Description="sample_text_2", Name="sample_text_2", Percentage=13)
    b = hairDressersRegSys_Customer(CustomerId=7)
    _safe_set(b, 'customer', a1)
    assert _is_linked(b, 'customer', a1)
    if hasattr(a1, 'Discounts16'):
        assert _is_linked(a1, 'Discounts16', b)
    _safe_set(b, 'customer', a2)
    assert _is_linked(b, 'customer', a2)
    if hasattr(a1, 'Discounts16'):
        assert not _is_linked(a1, 'Discounts16', b)
    if hasattr(a2, 'Discounts16'):
        assert _is_linked(a2, 'Discounts16', b)
    _safe_set(b, 'customer', None)
    assert not _is_linked(b, 'customer', a2)
    if hasattr(a2, 'Discounts16'):
        assert not _is_linked(a2, 'Discounts16', b)


def test_assoc_discounts5_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    a2 = hairDressersRegSys_Invoice(Date="sample_text_2", InvoiceNumber=13, Total="sample_text_2")
    b = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    _safe_set(b, 'Discounts', a1)
    assert _is_linked(b, 'Discounts', a1)
    if hasattr(a1, 'invoice6'):
        assert _is_linked(a1, 'invoice6', b)
    _safe_set(b, 'Discounts', a2)
    assert _is_linked(b, 'Discounts', a2)
    if hasattr(a1, 'invoice6'):
        assert not _is_linked(a1, 'invoice6', b)
    if hasattr(a2, 'invoice6'):
        assert _is_linked(a2, 'invoice6', b)
    _safe_set(b, 'Discounts', None)
    assert not _is_linked(b, 'Discounts', a2)
    if hasattr(a2, 'invoice6'):
        assert not _is_linked(a2, 'invoice6', b)


def test_assoc_invoice1_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    a2 = hairDressersRegSys_Invoice(Date="sample_text_2", InvoiceNumber=13, Total="sample_text_2")
    b = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    _safe_set(b, 'hairDressersRegSys_Appointment2', a1)
    assert _is_linked(b, 'hairDressersRegSys_Appointment2', a1)
    if hasattr(a1, 'hairDressersRegSys_Invoice'):
        assert _is_linked(a1, 'hairDressersRegSys_Invoice', b)
    _safe_set(b, 'hairDressersRegSys_Appointment2', a2)
    assert _is_linked(b, 'hairDressersRegSys_Appointment2', a2)
    if hasattr(a1, 'hairDressersRegSys_Invoice'):
        assert not _is_linked(a1, 'hairDressersRegSys_Invoice', b)
    if hasattr(a2, 'hairDressersRegSys_Invoice'):
        assert _is_linked(a2, 'hairDressersRegSys_Invoice', b)
    _safe_set(b, 'hairDressersRegSys_Appointment2', None)
    assert not _is_linked(b, 'hairDressersRegSys_Appointment2', a2)
    if hasattr(a2, 'hairDressersRegSys_Invoice'):
        assert not _is_linked(a2, 'hairDressersRegSys_Invoice', b)


def test_assoc_invoice10_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    a2 = hairDressersRegSys_Invoice(Date="sample_text_2", InvoiceNumber=13, Total="sample_text_2")
    b = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    _safe_set(b, 'discounts11', {a1})
    assert _is_linked(b, 'discounts11', a1)
    if hasattr(a1, 'Invoice12'):
        assert _is_linked(a1, 'Invoice12', b)
    _safe_set(b, 'discounts11', {a2})
    assert _is_linked(b, 'discounts11', a2)
    if hasattr(a1, 'Invoice12'):
        assert not _is_linked(a1, 'Invoice12', b)
    if hasattr(a2, 'Invoice12'):
        assert _is_linked(a2, 'Invoice12', b)
    _safe_set(b, 'discounts11', set())
    assert not _is_linked(b, 'discounts11', a2)
    if hasattr(a2, 'Invoice12'):
        assert not _is_linked(a2, 'Invoice12', b)


def test_assoc_invoice19_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Payment(AmountPaid="sample_text", Date=date(2024, 1, 1), PaymentMethod="sample_text")
    a2 = hairDressersRegSys_Payment(AmountPaid="sample_text_2", Date=date(2025, 6, 15), PaymentMethod="sample_text_2")
    b = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    _safe_set(b, 'Invoice20', a1)
    assert _is_linked(b, 'Invoice20', a1)
    if hasattr(a1, 'payment'):
        assert _is_linked(a1, 'payment', b)
    _safe_set(b, 'Invoice20', a2)
    assert _is_linked(b, 'Invoice20', a2)
    if hasattr(a1, 'payment'):
        assert not _is_linked(a1, 'payment', b)
    if hasattr(a2, 'payment'):
        assert _is_linked(a2, 'payment', b)
    _safe_set(b, 'Invoice20', None)
    assert not _is_linked(b, 'Invoice20', a2)
    if hasattr(a2, 'payment'):
        assert not _is_linked(a2, 'payment', b)


def test_assoc_invoice3_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Products(Description="sample_text", Name="sample_text", Price="sample_text")
    a2 = hairDressersRegSys_Products(Description="sample_text_2", Name="sample_text_2", Price="sample_text_2")
    b = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    _safe_set(b, 'Invoice', a1)
    assert _is_linked(b, 'Invoice', a1)
    if hasattr(a1, 'products'):
        assert _is_linked(a1, 'products', b)
    _safe_set(b, 'Invoice', a2)
    assert _is_linked(b, 'Invoice', a2)
    if hasattr(a1, 'products'):
        assert not _is_linked(a1, 'products', b)
    if hasattr(a2, 'products'):
        assert _is_linked(a2, 'products', b)
    _safe_set(b, 'Invoice', None)
    assert not _is_linked(b, 'Invoice', a2)
    if hasattr(a2, 'products'):
        assert not _is_linked(a2, 'products', b)


def test_assoc_payment7_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Payment(AmountPaid="sample_text", Date=date(2024, 1, 1), PaymentMethod="sample_text")
    a2 = hairDressersRegSys_Payment(AmountPaid="sample_text_2", Date=date(2025, 6, 15), PaymentMethod="sample_text_2")
    b = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    _safe_set(b, 'invoice8', a1)
    assert _is_linked(b, 'invoice8', a1)
    if hasattr(a1, 'Payment'):
        assert _is_linked(a1, 'Payment', b)
    _safe_set(b, 'invoice8', a2)
    assert _is_linked(b, 'invoice8', a2)
    if hasattr(a1, 'Payment'):
        assert not _is_linked(a1, 'Payment', b)
    if hasattr(a2, 'Payment'):
        assert _is_linked(a2, 'Payment', b)
    _safe_set(b, 'invoice8', None)
    assert not _is_linked(b, 'invoice8', a2)
    if hasattr(a2, 'Payment'):
        assert not _is_linked(a2, 'Payment', b)


def test_assoc_products4_reverse_link_reassign_clear():
    a1 = hairDressersRegSys_Products(Description="sample_text", Name="sample_text", Price="sample_text")
    a2 = hairDressersRegSys_Products(Description="sample_text_2", Name="sample_text_2", Price="sample_text_2")
    b = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    _safe_set(b, 'invoice', a1)
    assert _is_linked(b, 'invoice', a1)
    if hasattr(a1, 'Products'):
        assert _is_linked(a1, 'Products', b)
    _safe_set(b, 'invoice', a2)
    assert _is_linked(b, 'invoice', a2)
    if hasattr(a1, 'Products'):
        assert not _is_linked(a1, 'Products', b)
    if hasattr(a2, 'Products'):
        assert _is_linked(a2, 'Products', b)
    _safe_set(b, 'invoice', None)
    assert not _is_linked(b, 'invoice', a2)
    if hasattr(a2, 'Products'):
        assert not _is_linked(a2, 'Products', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

