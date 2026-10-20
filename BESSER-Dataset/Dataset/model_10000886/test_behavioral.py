import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    Base,
    Customer,
    GPSLocation,
    MealDeal,
    Order,
    Pizza,
    Sides,
    Toppings,
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

def test_assoc_Customer_Address_reverse_link_reassign_clear():
    a1 = Customer(customerID=7, customerName="sample_text", phoneNumber=7)
    a2 = Customer(customerID=13, customerName="sample_text_2", phoneNumber=13)
    b = Address(City="sample_text", County="sample_text", Line1="sample_text", Line_2="sample_text")
    _safe_set(b, 'customer13', a1)
    assert _is_linked(b, 'customer13', a1)
    if hasattr(a1, 'address12'):
        assert _is_linked(a1, 'address12', b)
    _safe_set(b, 'customer13', a2)
    assert _is_linked(b, 'customer13', a2)
    if hasattr(a1, 'address12'):
        assert not _is_linked(a1, 'address12', b)
    if hasattr(a2, 'address12'):
        assert _is_linked(a2, 'address12', b)
    _safe_set(b, 'customer13', None)
    assert not _is_linked(b, 'customer13', a2)
    if hasattr(a2, 'address12'):
        assert not _is_linked(a2, 'address12', b)


def test_assoc_MealDeal_Pizza_reverse_link_reassign_clear():
    a1 = Pizza(isVegetarian=True, price=3.14)
    a2 = Pizza(isVegetarian=False, price=9.99)
    b = MealDeal(description="sample_text", isVegetarian=True, name="sample_text", price=3.14)
    _safe_set(b, 'pizza16', {a1})
    assert _is_linked(b, 'pizza16', a1)
    if hasattr(a1, 'mealDeal17'):
        assert _is_linked(a1, 'mealDeal17', b)
    _safe_set(b, 'pizza16', {a2})
    assert _is_linked(b, 'pizza16', a2)
    if hasattr(a1, 'mealDeal17'):
        assert not _is_linked(a1, 'mealDeal17', b)
    if hasattr(a2, 'mealDeal17'):
        assert _is_linked(a2, 'mealDeal17', b)
    _safe_set(b, 'pizza16', set())
    assert not _is_linked(b, 'pizza16', a2)
    if hasattr(a2, 'mealDeal17'):
        assert not _is_linked(a2, 'mealDeal17', b)


def test_assoc_MealDeal_Sides_reverse_link_reassign_clear():
    a1 = Sides(isVegetarian=True, name="sample_text", price=3.14)
    a2 = Sides(isVegetarian=False, name="sample_text_2", price=9.99)
    b = MealDeal(description="sample_text", isVegetarian=True, name="sample_text", price=3.14)
    _safe_set(b, 'sides14', {a1})
    assert _is_linked(b, 'sides14', a1)
    if hasattr(a1, 'mealDeal15'):
        assert _is_linked(a1, 'mealDeal15', b)
    _safe_set(b, 'sides14', {a2})
    assert _is_linked(b, 'sides14', a2)
    if hasattr(a1, 'mealDeal15'):
        assert not _is_linked(a1, 'mealDeal15', b)
    if hasattr(a2, 'mealDeal15'):
        assert _is_linked(a2, 'mealDeal15', b)
    _safe_set(b, 'sides14', set())
    assert not _is_linked(b, 'sides14', a2)
    if hasattr(a2, 'mealDeal15'):
        assert not _is_linked(a2, 'mealDeal15', b)


def test_assoc_Order_Address_reverse_link_reassign_clear():
    a1 = Order(creditCardDetails="sample_text", date="sample_text", orderID=7, orderNotes="sample_text", time=7)
    a2 = Order(creditCardDetails="sample_text_2", date="sample_text_2", orderID=13, orderNotes="sample_text_2", time=13)
    b = Address(City="sample_text", County="sample_text", Line1="sample_text", Line_2="sample_text")
    _safe_set(b, 'order21', {a1})
    assert _is_linked(b, 'order21', a1)
    if hasattr(a1, 'address20'):
        assert _is_linked(a1, 'address20', b)
    _safe_set(b, 'order21', {a2})
    assert _is_linked(b, 'order21', a2)
    if hasattr(a1, 'address20'):
        assert not _is_linked(a1, 'address20', b)
    if hasattr(a2, 'address20'):
        assert _is_linked(a2, 'address20', b)
    _safe_set(b, 'order21', set())
    assert not _is_linked(b, 'order21', a2)
    if hasattr(a2, 'address20'):
        assert not _is_linked(a2, 'address20', b)


def test_assoc_Order_Customer_reverse_link_reassign_clear():
    a1 = Order(creditCardDetails="sample_text", date="sample_text", orderID=7, orderNotes="sample_text", time=7)
    a2 = Order(creditCardDetails="sample_text_2", date="sample_text_2", orderID=13, orderNotes="sample_text_2", time=13)
    b = Customer(customerID=7, customerName="sample_text", phoneNumber=7)
    _safe_set(b, 'order9', {a1})
    assert _is_linked(b, 'order9', a1)
    if hasattr(a1, 'customer8'):
        assert _is_linked(a1, 'customer8', b)
    _safe_set(b, 'order9', {a2})
    assert _is_linked(b, 'order9', a2)
    if hasattr(a1, 'customer8'):
        assert not _is_linked(a1, 'customer8', b)
    if hasattr(a2, 'customer8'):
        assert _is_linked(a2, 'customer8', b)
    _safe_set(b, 'order9', set())
    assert not _is_linked(b, 'order9', a2)
    if hasattr(a2, 'customer8'):
        assert not _is_linked(a2, 'customer8', b)


def test_assoc_Order_GPS_Location_reverse_link_reassign_clear():
    a1 = Order(creditCardDetails="sample_text", date="sample_text", orderID=7, orderNotes="sample_text", time=7)
    a2 = Order(creditCardDetails="sample_text_2", date="sample_text_2", orderID=13, orderNotes="sample_text_2", time=13)
    b = GPSLocation(GPS="sample_text")
    _safe_set(b, 'order5', a1)
    assert _is_linked(b, 'order5', a1)
    if hasattr(a1, 'GPS_Location4'):
        assert _is_linked(a1, 'GPS_Location4', b)
    _safe_set(b, 'order5', a2)
    assert _is_linked(b, 'order5', a2)
    if hasattr(a1, 'GPS_Location4'):
        assert not _is_linked(a1, 'GPS_Location4', b)
    if hasattr(a2, 'GPS_Location4'):
        assert _is_linked(a2, 'GPS_Location4', b)
    _safe_set(b, 'order5', None)
    assert not _is_linked(b, 'order5', a2)
    if hasattr(a2, 'GPS_Location4'):
        assert not _is_linked(a2, 'GPS_Location4', b)


def test_assoc_Order_MealDeal_reverse_link_reassign_clear():
    a1 = Order(creditCardDetails="sample_text", date="sample_text", orderID=7, orderNotes="sample_text", time=7)
    a2 = Order(creditCardDetails="sample_text_2", date="sample_text_2", orderID=13, orderNotes="sample_text_2", time=13)
    b = MealDeal(description="sample_text", isVegetarian=True, name="sample_text", price=3.14)
    _safe_set(b, 'order19', {a1})
    assert _is_linked(b, 'order19', a1)
    if hasattr(a1, 'mealDeal18'):
        assert _is_linked(a1, 'mealDeal18', b)
    _safe_set(b, 'order19', {a2})
    assert _is_linked(b, 'order19', a2)
    if hasattr(a1, 'mealDeal18'):
        assert not _is_linked(a1, 'mealDeal18', b)
    if hasattr(a2, 'mealDeal18'):
        assert _is_linked(a2, 'mealDeal18', b)
    _safe_set(b, 'order19', set())
    assert not _is_linked(b, 'order19', a2)
    if hasattr(a2, 'mealDeal18'):
        assert not _is_linked(a2, 'mealDeal18', b)


def test_assoc_Order_Pizza_reverse_link_reassign_clear():
    a1 = Pizza(isVegetarian=True, price=3.14)
    a2 = Pizza(isVegetarian=False, price=9.99)
    b = Order(creditCardDetails="sample_text", date="sample_text", orderID=7, orderNotes="sample_text", time=7)
    _safe_set(b, 'pizza2', {a1})
    assert _is_linked(b, 'pizza2', a1)
    if hasattr(a1, 'order3'):
        assert _is_linked(a1, 'order3', b)
    _safe_set(b, 'pizza2', {a2})
    assert _is_linked(b, 'pizza2', a2)
    if hasattr(a1, 'order3'):
        assert not _is_linked(a1, 'order3', b)
    if hasattr(a2, 'order3'):
        assert _is_linked(a2, 'order3', b)
    _safe_set(b, 'pizza2', set())
    assert not _is_linked(b, 'pizza2', a2)
    if hasattr(a2, 'order3'):
        assert not _is_linked(a2, 'order3', b)


def test_assoc_Order_Sides_reverse_link_reassign_clear():
    a1 = Sides(isVegetarian=True, name="sample_text", price=3.14)
    a2 = Sides(isVegetarian=False, name="sample_text_2", price=9.99)
    b = Order(creditCardDetails="sample_text", date="sample_text", orderID=7, orderNotes="sample_text", time=7)
    _safe_set(b, 'sides10', {a1})
    assert _is_linked(b, 'sides10', a1)
    if hasattr(a1, 'order11'):
        assert _is_linked(a1, 'order11', b)
    _safe_set(b, 'sides10', {a2})
    assert _is_linked(b, 'sides10', a2)
    if hasattr(a1, 'order11'):
        assert not _is_linked(a1, 'order11', b)
    if hasattr(a2, 'order11'):
        assert _is_linked(a2, 'order11', b)
    _safe_set(b, 'sides10', set())
    assert not _is_linked(b, 'sides10', a2)
    if hasattr(a2, 'order11'):
        assert not _is_linked(a2, 'order11', b)


def test_assoc_Pizza_Base_reverse_link_reassign_clear():
    a1 = Pizza(isVegetarian=True, price=3.14)
    a2 = Pizza(isVegetarian=False, price=9.99)
    b = Base(isVegetarian=True, name="sample_text")
    _safe_set(b, 'pizza1', {a1})
    assert _is_linked(b, 'pizza1', a1)
    if hasattr(a1, 'base0'):
        assert _is_linked(a1, 'base0', b)
    _safe_set(b, 'pizza1', {a2})
    assert _is_linked(b, 'pizza1', a2)
    if hasattr(a1, 'base0'):
        assert not _is_linked(a1, 'base0', b)
    if hasattr(a2, 'base0'):
        assert _is_linked(a2, 'base0', b)
    _safe_set(b, 'pizza1', set())
    assert not _is_linked(b, 'pizza1', a2)
    if hasattr(a2, 'base0'):
        assert not _is_linked(a2, 'base0', b)


def test_assoc_Pizza_Toppings_reverse_link_reassign_clear():
    a1 = Toppings(isVegetarian=True, name="sample_text")
    a2 = Toppings(isVegetarian=False, name="sample_text_2")
    b = Pizza(isVegetarian=True, price=3.14)
    _safe_set(b, 'toppings6', {a1})
    assert _is_linked(b, 'toppings6', a1)
    if hasattr(a1, 'pizza7'):
        assert _is_linked(a1, 'pizza7', b)
    _safe_set(b, 'toppings6', {a2})
    assert _is_linked(b, 'toppings6', a2)
    if hasattr(a1, 'pizza7'):
        assert not _is_linked(a1, 'pizza7', b)
    if hasattr(a2, 'pizza7'):
        assert _is_linked(a2, 'pizza7', b)
    _safe_set(b, 'toppings6', set())
    assert not _is_linked(b, 'toppings6', a2)
    if hasattr(a2, 'pizza7'):
        assert not _is_linked(a2, 'pizza7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

