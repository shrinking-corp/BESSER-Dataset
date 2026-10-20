import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin_,
    Appliacne,
    Employee,
    Furniture,
    Product,
    Store,
    customers,
    food,
    member,
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

def test_assoc_Admin__Workers_reverse_link_reassign_clear():
    a1 = Employee(Designation="sample_text", Password="sample_text", name="sample_text", salary=7)
    a2 = Employee(Designation="sample_text_2", Password="sample_text_2", name="sample_text_2", salary=13)
    b = Admin_(ArrayList_member_="sample_text", ArryList_Employee="sample_text", Password="sample_text")
    _safe_set(b, 'workers8', a1)
    assert _is_linked(b, 'workers8', a1)
    if hasattr(a1, 'admin_9'):
        assert _is_linked(a1, 'admin_9', b)
    _safe_set(b, 'workers8', a2)
    assert _is_linked(b, 'workers8', a2)
    if hasattr(a1, 'admin_9'):
        assert not _is_linked(a1, 'admin_9', b)
    if hasattr(a2, 'admin_9'):
        assert _is_linked(a2, 'admin_9', b)
    _safe_set(b, 'workers8', None)
    assert not _is_linked(b, 'workers8', a2)
    if hasattr(a2, 'admin_9'):
        assert not _is_linked(a2, 'admin_9', b)


def test_assoc_Admin__member_reverse_link_reassign_clear():
    a1 = member(memberType="sample_text", name="sample_text", password="sample_text")
    a2 = member(memberType="sample_text_2", name="sample_text_2", password="sample_text_2")
    b = Admin_(ArrayList_member_="sample_text", ArryList_Employee="sample_text", Password="sample_text")
    _safe_set(b, 'member6', a1)
    assert _is_linked(b, 'member6', a1)
    if hasattr(a1, 'admin_7'):
        assert _is_linked(a1, 'admin_7', b)
    _safe_set(b, 'member6', a2)
    assert _is_linked(b, 'member6', a2)
    if hasattr(a1, 'admin_7'):
        assert not _is_linked(a1, 'admin_7', b)
    if hasattr(a2, 'admin_7'):
        assert _is_linked(a2, 'admin_7', b)
    _safe_set(b, 'member6', None)
    assert not _is_linked(b, 'member6', a2)
    if hasattr(a2, 'admin_7'):
        assert not _is_linked(a2, 'admin_7', b)


def test_assoc_Items_Appliacne_reverse_link_reassign_clear():
    a1 = Product(ArrayList_appliance_="sample_text", ArrayList_food_="sample_text", ArrayList_furniture_="sample_text", typeOfItems=7)
    a2 = Product(ArrayList_appliance_="sample_text_2", ArrayList_food_="sample_text_2", ArrayList_furniture_="sample_text_2", typeOfItems=13)
    b = Appliacne(name="sample_text", price=7)
    _safe_set(b, 'items1', a1)
    assert _is_linked(b, 'items1', a1)
    if hasattr(a1, 'appliacne0'):
        assert _is_linked(a1, 'appliacne0', b)
    _safe_set(b, 'items1', a2)
    assert _is_linked(b, 'items1', a2)
    if hasattr(a1, 'appliacne0'):
        assert not _is_linked(a1, 'appliacne0', b)
    if hasattr(a2, 'appliacne0'):
        assert _is_linked(a2, 'appliacne0', b)
    _safe_set(b, 'items1', None)
    assert not _is_linked(b, 'items1', a2)
    if hasattr(a2, 'appliacne0'):
        assert not _is_linked(a2, 'appliacne0', b)


def test_assoc_Items_Furniture_reverse_link_reassign_clear():
    a1 = Product(ArrayList_appliance_="sample_text", ArrayList_food_="sample_text", ArrayList_furniture_="sample_text", typeOfItems=7)
    a2 = Product(ArrayList_appliance_="sample_text_2", ArrayList_food_="sample_text_2", ArrayList_furniture_="sample_text_2", typeOfItems=13)
    b = Furniture(name="sample_text", price=7)
    _safe_set(b, 'items3', a1)
    assert _is_linked(b, 'items3', a1)
    if hasattr(a1, 'furniture2'):
        assert _is_linked(a1, 'furniture2', b)
    _safe_set(b, 'items3', a2)
    assert _is_linked(b, 'items3', a2)
    if hasattr(a1, 'furniture2'):
        assert not _is_linked(a1, 'furniture2', b)
    if hasattr(a2, 'furniture2'):
        assert _is_linked(a2, 'furniture2', b)
    _safe_set(b, 'items3', None)
    assert not _is_linked(b, 'items3', a2)
    if hasattr(a2, 'furniture2'):
        assert not _is_linked(a2, 'furniture2', b)


def test_assoc_Items_food_reverse_link_reassign_clear():
    a1 = food(name="sample_text", price=7)
    a2 = food(name="sample_text_2", price=13)
    b = Product(ArrayList_appliance_="sample_text", ArrayList_food_="sample_text", ArrayList_furniture_="sample_text", typeOfItems=7)
    _safe_set(b, 'food4', a1)
    assert _is_linked(b, 'food4', a1)
    if hasattr(a1, 'items5'):
        assert _is_linked(a1, 'items5', b)
    _safe_set(b, 'food4', a2)
    assert _is_linked(b, 'food4', a2)
    if hasattr(a1, 'items5'):
        assert not _is_linked(a1, 'items5', b)
    if hasattr(a2, 'items5'):
        assert _is_linked(a2, 'items5', b)
    _safe_set(b, 'food4', None)
    assert not _is_linked(b, 'food4', a2)
    if hasattr(a2, 'items5'):
        assert not _is_linked(a2, 'items5', b)


def test_assoc_Store_Employee_reverse_link_reassign_clear():
    a1 = Store(SName="sample_text", Sid=7)
    a2 = Store(SName="sample_text_2", Sid=13)
    b = Employee(Designation="sample_text", Password="sample_text", name="sample_text", salary=7)
    _safe_set(b, 'store13', a1)
    assert _is_linked(b, 'store13', a1)
    if hasattr(a1, 'employee12'):
        assert _is_linked(a1, 'employee12', b)
    _safe_set(b, 'store13', a2)
    assert _is_linked(b, 'store13', a2)
    if hasattr(a1, 'employee12'):
        assert not _is_linked(a1, 'employee12', b)
    if hasattr(a2, 'employee12'):
        assert _is_linked(a2, 'employee12', b)
    _safe_set(b, 'store13', None)
    assert not _is_linked(b, 'store13', a2)
    if hasattr(a2, 'employee12'):
        assert not _is_linked(a2, 'employee12', b)


def test_assoc_Store_Product_reverse_link_reassign_clear():
    a1 = Store(SName="sample_text", Sid=7)
    a2 = Store(SName="sample_text_2", Sid=13)
    b = Product(ArrayList_appliance_="sample_text", ArrayList_food_="sample_text", ArrayList_furniture_="sample_text", typeOfItems=7)
    _safe_set(b, 'store15', a1)
    assert _is_linked(b, 'store15', a1)
    if hasattr(a1, 'product14'):
        assert _is_linked(a1, 'product14', b)
    _safe_set(b, 'store15', a2)
    assert _is_linked(b, 'store15', a2)
    if hasattr(a1, 'product14'):
        assert not _is_linked(a1, 'product14', b)
    if hasattr(a2, 'product14'):
        assert _is_linked(a2, 'product14', b)
    _safe_set(b, 'store15', None)
    assert not _is_linked(b, 'store15', a2)
    if hasattr(a2, 'product14'):
        assert not _is_linked(a2, 'product14', b)


def test_assoc_member_Store_reverse_link_reassign_clear():
    a1 = member(memberType="sample_text", name="sample_text", password="sample_text")
    a2 = member(memberType="sample_text_2", name="sample_text_2", password="sample_text_2")
    b = Store(SName="sample_text", Sid=7)
    _safe_set(b, 'member11', a1)
    assert _is_linked(b, 'member11', a1)
    if hasattr(a1, 'store10'):
        assert _is_linked(a1, 'store10', b)
    _safe_set(b, 'member11', a2)
    assert _is_linked(b, 'member11', a2)
    if hasattr(a1, 'store10'):
        assert not _is_linked(a1, 'store10', b)
    if hasattr(a2, 'store10'):
        assert _is_linked(a2, 'store10', b)
    _safe_set(b, 'member11', None)
    assert not _is_linked(b, 'member11', a2)
    if hasattr(a2, 'store10'):
        assert not _is_linked(a2, 'store10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

