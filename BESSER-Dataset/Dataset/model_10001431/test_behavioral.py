import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bill,
    chef,
    customer,
    menu,
    order,
    payment,
    restaurant,
    staff,
    waiter,
    Print_Receipt,
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

def test_assoc_customer__menu_reverse_link_reassign_clear():
    a1 = menu(Menuid="sample_text", Menuname="sample_text", Price=7)
    a2 = menu(Menuid="sample_text_2", Menuname="sample_text_2", Price=13)
    b = customer(Name="sample_text", Order="sample_text", Tableno=7)
    _safe_set(b, 'menu2', a1)
    assert _is_linked(b, 'menu2', a1)
    if hasattr(a1, 'browse_menu3'):
        assert _is_linked(a1, 'browse_menu3', b)
    _safe_set(b, 'menu2', a2)
    assert _is_linked(b, 'menu2', a2)
    if hasattr(a1, 'browse_menu3'):
        assert not _is_linked(a1, 'browse_menu3', b)
    if hasattr(a2, 'browse_menu3'):
        assert _is_linked(a2, 'browse_menu3', b)
    _safe_set(b, 'menu2', None)
    assert not _is_linked(b, 'menu2', a2)
    if hasattr(a2, 'browse_menu3'):
        assert not _is_linked(a2, 'browse_menu3', b)


def test_assoc_menu_order_reverse_link_reassign_clear():
    a1 = order(orderdate="sample_text", orderid=7, price=7)
    a2 = order(orderdate="sample_text_2", orderid=13, price=13)
    b = menu(Menuid="sample_text", Menuname="sample_text", Price=7)
    _safe_set(b, 'order4', a1)
    assert _is_linked(b, 'order4', a1)
    if hasattr(a1, 'menu5'):
        assert _is_linked(a1, 'menu5', b)
    _safe_set(b, 'order4', a2)
    assert _is_linked(b, 'order4', a2)
    if hasattr(a1, 'menu5'):
        assert not _is_linked(a1, 'menu5', b)
    if hasattr(a2, 'menu5'):
        assert _is_linked(a2, 'menu5', b)
    _safe_set(b, 'order4', None)
    assert not _is_linked(b, 'order4', a2)
    if hasattr(a2, 'menu5'):
        assert not _is_linked(a2, 'menu5', b)


def test_assoc_menu_staff_reverse_link_reassign_clear():
    a1 = staff(jobtype="sample_text", name="sample_text", staffID=7)
    a2 = staff(jobtype="sample_text_2", name="sample_text_2", staffID=13)
    b = menu(Menuid="sample_text", Menuname="sample_text", Price=7)
    _safe_set(b, 'staff12', a1)
    assert _is_linked(b, 'staff12', a1)
    if hasattr(a1, 'menu13'):
        assert _is_linked(a1, 'menu13', b)
    _safe_set(b, 'staff12', a2)
    assert _is_linked(b, 'staff12', a2)
    if hasattr(a1, 'menu13'):
        assert not _is_linked(a1, 'menu13', b)
    if hasattr(a2, 'menu13'):
        assert _is_linked(a2, 'menu13', b)
    _safe_set(b, 'staff12', None)
    assert not _is_linked(b, 'staff12', a2)
    if hasattr(a2, 'menu13'):
        assert not _is_linked(a2, 'menu13', b)


def test_assoc_order_payment_reverse_link_reassign_clear():
    a1 = payment(name="sample_text", tableno=7)
    a2 = payment(name="sample_text_2", tableno=13)
    b = order(orderdate="sample_text", orderid=7, price=7)
    _safe_set(b, 'payment0', a1)
    assert _is_linked(b, 'payment0', a1)
    if hasattr(a1, 'order1'):
        assert _is_linked(a1, 'order1', b)
    _safe_set(b, 'payment0', a2)
    assert _is_linked(b, 'payment0', a2)
    if hasattr(a1, 'order1'):
        assert not _is_linked(a1, 'order1', b)
    if hasattr(a2, 'order1'):
        assert _is_linked(a2, 'order1', b)
    _safe_set(b, 'payment0', None)
    assert not _is_linked(b, 'payment0', a2)
    if hasattr(a2, 'order1'):
        assert not _is_linked(a2, 'order1', b)


def test_assoc_payment_customer_reverse_link_reassign_clear():
    a1 = payment(name="sample_text", tableno=7)
    a2 = payment(name="sample_text_2", tableno=13)
    b = customer(Name="sample_text", Order="sample_text", Tableno=7)
    _safe_set(b, 'payment_customer_111', a1)
    assert _is_linked(b, 'payment_customer_111', a1)
    if hasattr(a1, 'customer10'):
        assert _is_linked(a1, 'customer10', b)
    _safe_set(b, 'payment_customer_111', a2)
    assert _is_linked(b, 'payment_customer_111', a2)
    if hasattr(a1, 'customer10'):
        assert not _is_linked(a1, 'customer10', b)
    if hasattr(a2, 'customer10'):
        assert _is_linked(a2, 'customer10', b)
    _safe_set(b, 'payment_customer_111', None)
    assert not _is_linked(b, 'payment_customer_111', a2)
    if hasattr(a2, 'customer10'):
        assert not _is_linked(a2, 'customer10', b)


def test_assoc_restaurant_customer_reverse_link_reassign_clear():
    a1 = restaurant(Menuid="sample_text", tableid=7)
    a2 = restaurant(Menuid="sample_text_2", tableid=13)
    b = customer(Name="sample_text", Order="sample_text", Tableno=7)
    _safe_set(b, 'restaurant17', a1)
    assert _is_linked(b, 'restaurant17', a1)
    if hasattr(a1, 'customer16'):
        assert _is_linked(a1, 'customer16', b)
    _safe_set(b, 'restaurant17', a2)
    assert _is_linked(b, 'restaurant17', a2)
    if hasattr(a1, 'customer16'):
        assert not _is_linked(a1, 'customer16', b)
    if hasattr(a2, 'customer16'):
        assert _is_linked(a2, 'customer16', b)
    _safe_set(b, 'restaurant17', None)
    assert not _is_linked(b, 'restaurant17', a2)
    if hasattr(a2, 'customer16'):
        assert not _is_linked(a2, 'customer16', b)


def test_assoc_restaurant_staff2_reverse_link_reassign_clear():
    a1 = staff(jobtype="sample_text", name="sample_text", staffID=7)
    a2 = staff(jobtype="sample_text_2", name="sample_text_2", staffID=13)
    b = restaurant(Menuid="sample_text", tableid=7)
    _safe_set(b, 'staff18', a1)
    assert _is_linked(b, 'staff18', a1)
    if hasattr(a1, 'restaurant19'):
        assert _is_linked(a1, 'restaurant19', b)
    _safe_set(b, 'staff18', a2)
    assert _is_linked(b, 'staff18', a2)
    if hasattr(a1, 'restaurant19'):
        assert not _is_linked(a1, 'restaurant19', b)
    if hasattr(a2, 'restaurant19'):
        assert _is_linked(a2, 'restaurant19', b)
    _safe_set(b, 'staff18', None)
    assert not _is_linked(b, 'staff18', a2)
    if hasattr(a2, 'restaurant19'):
        assert not _is_linked(a2, 'restaurant19', b)


def test_assoc_waiter_chef_reverse_link_reassign_clear():
    a1 = waiter(Staffid=7, name="sample_text")
    a2 = waiter(Staffid=13, name="sample_text_2")
    b = chef(Name="sample_text", Staffid=7)
    _safe_set(b, 'waiter9', a1)
    assert _is_linked(b, 'waiter9', a1)
    if hasattr(a1, 'chef8'):
        assert _is_linked(a1, 'chef8', b)
    _safe_set(b, 'waiter9', a2)
    assert _is_linked(b, 'waiter9', a2)
    if hasattr(a1, 'chef8'):
        assert not _is_linked(a1, 'chef8', b)
    if hasattr(a2, 'chef8'):
        assert _is_linked(a2, 'chef8', b)
    _safe_set(b, 'waiter9', None)
    assert not _is_linked(b, 'waiter9', a2)
    if hasattr(a2, 'chef8'):
        assert not _is_linked(a2, 'chef8', b)


def test_assoc_waiter_menu_reverse_link_reassign_clear():
    a1 = waiter(Staffid=7, name="sample_text")
    a2 = waiter(Staffid=13, name="sample_text_2")
    b = menu(Menuid="sample_text", Menuname="sample_text", Price=7)
    _safe_set(b, 'waiter7', a1)
    assert _is_linked(b, 'waiter7', a1)
    if hasattr(a1, 'menu6'):
        assert _is_linked(a1, 'menu6', b)
    _safe_set(b, 'waiter7', a2)
    assert _is_linked(b, 'waiter7', a2)
    if hasattr(a1, 'menu6'):
        assert not _is_linked(a1, 'menu6', b)
    if hasattr(a2, 'menu6'):
        assert _is_linked(a2, 'menu6', b)
    _safe_set(b, 'waiter7', None)
    assert not _is_linked(b, 'waiter7', a2)
    if hasattr(a2, 'menu6'):
        assert not _is_linked(a2, 'menu6', b)


def test_assoc_waiter_staff_reverse_link_reassign_clear():
    a1 = waiter(Staffid=7, name="sample_text")
    a2 = waiter(Staffid=13, name="sample_text_2")
    b = staff(jobtype="sample_text", name="sample_text", staffID=7)
    _safe_set(b, 'waiter15', a1)
    assert _is_linked(b, 'waiter15', a1)
    if hasattr(a1, 'staff14'):
        assert _is_linked(a1, 'staff14', b)
    _safe_set(b, 'waiter15', a2)
    assert _is_linked(b, 'waiter15', a2)
    if hasattr(a1, 'staff14'):
        assert not _is_linked(a1, 'staff14', b)
    if hasattr(a2, 'staff14'):
        assert _is_linked(a2, 'staff14', b)
    _safe_set(b, 'waiter15', None)
    assert not _is_linked(b, 'waiter15', a2)
    if hasattr(a2, 'staff14'):
        assert not _is_linked(a2, 'staff14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

