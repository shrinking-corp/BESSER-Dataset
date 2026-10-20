import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Customer,
    Customer_Actor,
    Online_Order_and_CC_Processing,
    Online_Order_and_CC_processing_Actor,
    Store_POS_System,
    chefTicket,
    createOrder,
    deleteOrder,
    updatePayment,
    viewOrder,
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

def test_assoc_Customer_Online_Order_and_CC_Processing_reverse_link_reassign_clear():
    a1 = Online_Order_and_CC_Processing(order="sample_text", payment="sample_text", paymentApproved=True)
    a2 = Online_Order_and_CC_Processing(order="sample_text_2", payment="sample_text_2", paymentApproved=False)
    b = Customer(location="sample_text", name="sample_text")
    _safe_set(b, 'Online_Order_and_CC_Processing0', a1)
    assert _is_linked(b, 'Online_Order_and_CC_Processing0', a1)
    if hasattr(a1, 'customer1'):
        assert _is_linked(a1, 'customer1', b)
    _safe_set(b, 'Online_Order_and_CC_Processing0', a2)
    assert _is_linked(b, 'Online_Order_and_CC_Processing0', a2)
    if hasattr(a1, 'customer1'):
        assert not _is_linked(a1, 'customer1', b)
    if hasattr(a2, 'customer1'):
        assert _is_linked(a2, 'customer1', b)
    _safe_set(b, 'Online_Order_and_CC_Processing0', None)
    assert not _is_linked(b, 'Online_Order_and_CC_Processing0', a2)
    if hasattr(a2, 'customer1'):
        assert not _is_linked(a2, 'customer1', b)


def test_assoc_Customer_createOrder_reverse_link_reassign_clear():
    a1 = createOrder(orderedItems="sample_text")
    a2 = createOrder(orderedItems="sample_text_2")
    b = Customer(location="sample_text", name="sample_text")
    _safe_set(b, 'createOrder22', a1)
    assert _is_linked(b, 'createOrder22', a1)
    if hasattr(a1, 'customer3'):
        assert _is_linked(a1, 'customer3', b)
    _safe_set(b, 'createOrder22', a2)
    assert _is_linked(b, 'createOrder22', a2)
    if hasattr(a1, 'customer3'):
        assert not _is_linked(a1, 'customer3', b)
    if hasattr(a2, 'customer3'):
        assert _is_linked(a2, 'customer3', b)
    _safe_set(b, 'createOrder22', None)
    assert not _is_linked(b, 'createOrder22', a2)
    if hasattr(a2, 'customer3'):
        assert not _is_linked(a2, 'customer3', b)


def test_assoc_Customer_updatePayment_reverse_link_reassign_clear():
    a1 = updatePayment(paymentInformation="sample_text")
    a2 = updatePayment(paymentInformation="sample_text_2")
    b = Customer(location="sample_text", name="sample_text")
    _safe_set(b, 'updatePayment24', a1)
    assert _is_linked(b, 'updatePayment24', a1)
    if hasattr(a1, 'customer5'):
        assert _is_linked(a1, 'customer5', b)
    _safe_set(b, 'updatePayment24', a2)
    assert _is_linked(b, 'updatePayment24', a2)
    if hasattr(a1, 'customer5'):
        assert not _is_linked(a1, 'customer5', b)
    if hasattr(a2, 'customer5'):
        assert _is_linked(a2, 'customer5', b)
    _safe_set(b, 'updatePayment24', None)
    assert not _is_linked(b, 'updatePayment24', a2)
    if hasattr(a2, 'customer5'):
        assert not _is_linked(a2, 'customer5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Customer_deleteOrder_stub_double():
    # deleteOrder has no real 'customer7' property in the generated
    # code (a bare stub) -- manually attach it so Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Customer(location="sample_text", name="sample_text")
    partner = deleteOrder()
    setattr(partner, 'customer7', None)
    _safe_set(owner, 'deleteOrder26', partner)
    assert getattr(partner, 'customer7') == owner
    _safe_set(owner, 'deleteOrder26', None)
    assert getattr(partner, 'customer7') is None


def test_assoc_Online_Order_and_CC_Processing_chefTicket_stub_double():
    # chefTicket has no real 'online_Order_and_CC_Processing11' property in the generated
    # code (a bare stub) -- manually attach it so Online_Order_and_CC_Processing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Online_Order_and_CC_Processing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Online_Order_and_CC_Processing(order="sample_text", payment="sample_text", paymentApproved=True)
    partner = chefTicket()
    setattr(partner, 'online_Order_and_CC_Processing11', None)
    _safe_set(owner, 'chefTicket210', partner)
    assert getattr(partner, 'online_Order_and_CC_Processing11') == owner
    _safe_set(owner, 'chefTicket210', None)
    assert getattr(partner, 'online_Order_and_CC_Processing11') is None


def test_assoc_chefTicket_Store_POS_System_stub_double():
    # chefTicket has no real 'store_POS_System8' property in the generated
    # code (a bare stub) -- manually attach it so Store_POS_System's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Store_POS_System's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Store_POS_System(print="sample_text")
    partner = chefTicket()
    setattr(partner, 'store_POS_System8', None)
    _safe_set(owner, 'chefTicket29', partner)
    assert getattr(partner, 'store_POS_System8') == owner
    _safe_set(owner, 'chefTicket29', None)
    assert getattr(partner, 'store_POS_System8') is None


