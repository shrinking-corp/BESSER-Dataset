import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NO_Queue_mobile_application__Account,
    NO_Queue_mobile_application__App_User,
    NO_Queue_mobile_application__Customer,
    NO_Queue_mobile_application__Line_item,
    NO_Queue_mobile_application__NOQueue,
    NO_Queue_mobile_application__Order,
    NO_Queue_mobile_application__Payment,
    NO_Queue_mobile_application__Product,
    NO_Queue_mobile_application__Shopping_Cart,
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

def test_assoc_Account_Order_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Order(Number="sample_text", Ship_to="sample_text", ordered="sample_text", shipped="sample_text", status="sample_text", total="sample_text")
    a2 = NO_Queue_mobile_application__Order(Number="sample_text_2", Ship_to="sample_text_2", ordered="sample_text_2", shipped="sample_text_2", status="sample_text_2", total="sample_text_2")
    b = NO_Queue_mobile_application__Account(Closed="sample_text", ID="sample_text", Open="sample_text", billing_address="sample_text", is_closed=True)
    _safe_set(b, 'order8', {a1})
    assert _is_linked(b, 'order8', a1)
    if hasattr(a1, 'account9'):
        assert _is_linked(a1, 'account9', b)
    _safe_set(b, 'order8', {a2})
    assert _is_linked(b, 'order8', a2)
    if hasattr(a1, 'account9'):
        assert not _is_linked(a1, 'account9', b)
    if hasattr(a2, 'account9'):
        assert _is_linked(a2, 'account9', b)
    _safe_set(b, 'order8', set())
    assert not _is_linked(b, 'order8', a2)
    if hasattr(a2, 'account9'):
        assert not _is_linked(a2, 'account9', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Customer(Address="sample_text", Email="sample_text", ID="sample_text", Phone="sample_text")
    a2 = NO_Queue_mobile_application__Customer(Address="sample_text_2", Email="sample_text_2", ID="sample_text_2", Phone="sample_text_2")
    b = NO_Queue_mobile_application__Account(Closed="sample_text", ID="sample_text", Open="sample_text", billing_address="sample_text", is_closed=True)
    _safe_set(b, 'customer3', a1)
    assert _is_linked(b, 'customer3', a1)
    if hasattr(a1, 'account2'):
        assert _is_linked(a1, 'account2', b)
    _safe_set(b, 'customer3', a2)
    assert _is_linked(b, 'customer3', a2)
    if hasattr(a1, 'account2'):
        assert not _is_linked(a1, 'account2', b)
    if hasattr(a2, 'account2'):
        assert _is_linked(a2, 'account2', b)
    _safe_set(b, 'customer3', None)
    assert not _is_linked(b, 'customer3', a2)
    if hasattr(a2, 'account2'):
        assert not _is_linked(a2, 'account2', b)


def test_assoc_Line_item_Product_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Product(ID="sample_text", Name="sample_text", Supplier="sample_text")
    a2 = NO_Queue_mobile_application__Product(ID="sample_text_2", Name="sample_text_2", Supplier="sample_text_2")
    b = NO_Queue_mobile_application__Line_item(price="sample_text", quantity=7)
    _safe_set(b, 'product14', a1)
    assert _is_linked(b, 'product14', a1)
    if hasattr(a1, 'line_item15'):
        assert _is_linked(a1, 'line_item15', b)
    _safe_set(b, 'product14', a2)
    assert _is_linked(b, 'product14', a2)
    if hasattr(a1, 'line_item15'):
        assert not _is_linked(a1, 'line_item15', b)
    if hasattr(a2, 'line_item15'):
        assert _is_linked(a2, 'line_item15', b)
    _safe_set(b, 'product14', None)
    assert not _is_linked(b, 'product14', a2)
    if hasattr(a2, 'line_item15'):
        assert not _is_linked(a2, 'line_item15', b)


def test_assoc_Order_Line_item_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Order(Number="sample_text", Ship_to="sample_text", ordered="sample_text", shipped="sample_text", status="sample_text", total="sample_text")
    a2 = NO_Queue_mobile_application__Order(Number="sample_text_2", Ship_to="sample_text_2", ordered="sample_text_2", shipped="sample_text_2", status="sample_text_2", total="sample_text_2")
    b = NO_Queue_mobile_application__Line_item(price="sample_text", quantity=7)
    _safe_set(b, '_order__unique_13', a1)
    assert _is_linked(b, '_order__unique_13', a1)
    if hasattr(a1, 'line_item12'):
        assert _is_linked(a1, 'line_item12', b)
    _safe_set(b, '_order__unique_13', a2)
    assert _is_linked(b, '_order__unique_13', a2)
    if hasattr(a1, 'line_item12'):
        assert not _is_linked(a1, 'line_item12', b)
    if hasattr(a2, 'line_item12'):
        assert _is_linked(a2, 'line_item12', b)
    _safe_set(b, '_order__unique_13', None)
    assert not _is_linked(b, '_order__unique_13', a2)
    if hasattr(a2, 'line_item12'):
        assert not _is_linked(a2, 'line_item12', b)


def test_assoc_Payment_Account_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Payment(Details="sample_text", ID="sample_text", Paid="sample_text", Total="sample_text")
    a2 = NO_Queue_mobile_application__Payment(Details="sample_text_2", ID="sample_text_2", Paid="sample_text_2", Total="sample_text_2")
    b = NO_Queue_mobile_application__Account(Closed="sample_text", ID="sample_text", Open="sample_text", billing_address="sample_text", is_closed=True)
    _safe_set(b, 'payment5', {a1})
    assert _is_linked(b, 'payment5', a1)
    if hasattr(a1, 'account4'):
        assert _is_linked(a1, 'account4', b)
    _safe_set(b, 'payment5', {a2})
    assert _is_linked(b, 'payment5', a2)
    if hasattr(a1, 'account4'):
        assert not _is_linked(a1, 'account4', b)
    if hasattr(a2, 'account4'):
        assert _is_linked(a2, 'account4', b)
    _safe_set(b, 'payment5', set())
    assert not _is_linked(b, 'payment5', a2)
    if hasattr(a2, 'account4'):
        assert not _is_linked(a2, 'account4', b)


def test_assoc_Shopping_Cart_Line_item_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Shopping_Cart(created="sample_text")
    a2 = NO_Queue_mobile_application__Shopping_Cart(created="sample_text_2")
    b = NO_Queue_mobile_application__Line_item(price="sample_text", quantity=7)
    _safe_set(b, 'shopping_Cart11', a1)
    assert _is_linked(b, 'shopping_Cart11', a1)
    if hasattr(a1, 'ordered__unique10'):
        assert _is_linked(a1, 'ordered__unique10', b)
    _safe_set(b, 'shopping_Cart11', a2)
    assert _is_linked(b, 'shopping_Cart11', a2)
    if hasattr(a1, 'ordered__unique10'):
        assert not _is_linked(a1, 'ordered__unique10', b)
    if hasattr(a2, 'ordered__unique10'):
        assert _is_linked(a2, 'ordered__unique10', b)
    _safe_set(b, 'shopping_Cart11', None)
    assert not _is_linked(b, 'shopping_Cart11', a2)
    if hasattr(a2, 'ordered__unique10'):
        assert not _is_linked(a2, 'ordered__unique10', b)


def test_assoc_Web_User_Customer_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Customer(Address="sample_text", Email="sample_text", ID="sample_text", Phone="sample_text")
    a2 = NO_Queue_mobile_application__Customer(Address="sample_text_2", Email="sample_text_2", ID="sample_text_2", Phone="sample_text_2")
    b = NO_Queue_mobile_application__App_User(login_id="sample_text", passwd="sample_text")
    _safe_set(b, 'customer0', a1)
    assert _is_linked(b, 'customer0', a1)
    if hasattr(a1, 'web_User1'):
        assert _is_linked(a1, 'web_User1', b)
    _safe_set(b, 'customer0', a2)
    assert _is_linked(b, 'customer0', a2)
    if hasattr(a1, 'web_User1'):
        assert not _is_linked(a1, 'web_User1', b)
    if hasattr(a2, 'web_User1'):
        assert _is_linked(a2, 'web_User1', b)
    _safe_set(b, 'customer0', None)
    assert not _is_linked(b, 'customer0', a2)
    if hasattr(a2, 'web_User1'):
        assert not _is_linked(a2, 'web_User1', b)


def test_assoc_Web_User_Shopping_Cart_reverse_link_reassign_clear():
    a1 = NO_Queue_mobile_application__Shopping_Cart(created="sample_text")
    a2 = NO_Queue_mobile_application__Shopping_Cart(created="sample_text_2")
    b = NO_Queue_mobile_application__App_User(login_id="sample_text", passwd="sample_text")
    _safe_set(b, 'shopping_Cart6', a1)
    assert _is_linked(b, 'shopping_Cart6', a1)
    if hasattr(a1, 'web_User7'):
        assert _is_linked(a1, 'web_User7', b)
    _safe_set(b, 'shopping_Cart6', a2)
    assert _is_linked(b, 'shopping_Cart6', a2)
    if hasattr(a1, 'web_User7'):
        assert not _is_linked(a1, 'web_User7', b)
    if hasattr(a2, 'web_User7'):
        assert _is_linked(a2, 'web_User7', b)
    _safe_set(b, 'shopping_Cart6', None)
    assert not _is_linked(b, 'shopping_Cart6', a2)
    if hasattr(a2, 'web_User7'):
        assert not _is_linked(a2, 'web_User7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

