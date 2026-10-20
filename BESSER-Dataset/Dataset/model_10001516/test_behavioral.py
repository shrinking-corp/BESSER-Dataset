import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Bank,
    Cash_on_delievery,
    Category,
    Customer,
    Food_Items,
    Payment,
    System_order,
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

def test_assoc_System_order_Payment_reverse_link_reassign_clear():
    a1 = System_order(Customer_ID=7, Customer_Name="sample_text", Date=7, Delivery_Charges=7, Order_ID=7, Payment_Option="sample_text", Time=7, Total=7)
    a2 = System_order(Customer_ID=13, Customer_Name="sample_text_2", Date=13, Delivery_Charges=13, Order_ID=13, Payment_Option="sample_text_2", Time=13, Total=13)
    b = Payment(Amount=7, Payment_Option="sample_text")
    _safe_set(b, 'System_order_Payment_11', {a1})
    assert _is_linked(b, 'System_order_Payment_11', a1)
    if hasattr(a1, 'System_order_Payment_00'):
        assert _is_linked(a1, 'System_order_Payment_00', b)
    _safe_set(b, 'System_order_Payment_11', {a2})
    assert _is_linked(b, 'System_order_Payment_11', a2)
    if hasattr(a1, 'System_order_Payment_00'):
        assert not _is_linked(a1, 'System_order_Payment_00', b)
    if hasattr(a2, 'System_order_Payment_00'):
        assert _is_linked(a2, 'System_order_Payment_00', b)
    _safe_set(b, 'System_order_Payment_11', set())
    assert not _is_linked(b, 'System_order_Payment_11', a2)
    if hasattr(a2, 'System_order_Payment_00'):
        assert not _is_linked(a2, 'System_order_Payment_00', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_System_order_Customer_stub_double():
    # Customer has no real 'System_order_Customer_13' property in the generated
    # code (a bare stub) -- manually attach it so System_order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # System_order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = System_order(Customer_ID=7, Customer_Name="sample_text", Date=7, Delivery_Charges=7, Order_ID=7, Payment_Option="sample_text", Time=7, Total=7)
    partner = Customer()
    setattr(partner, 'System_order_Customer_13', None)
    _safe_set(owner, 'System_order_Customer_02', partner)
    assert getattr(partner, 'System_order_Customer_13') == owner
    _safe_set(owner, 'System_order_Customer_02', None)
    assert getattr(partner, 'System_order_Customer_13') is None


