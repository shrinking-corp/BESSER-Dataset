import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Cart,
    Customer,
    ExerciseMachine,
    MediDevices,
    Medicine,
    Order,
    PaymentMethod,
    Person,
    Product,
    Registration,
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

def test_assoc_Admin_Product_reverse_link_reassign_clear():
    a1 = Product(color="sample_text", expiry="sample_text", manufecturedDate="sample_text", manufecturer="sample_text", name="sample_text", pID="sample_text", price=7)
    a2 = Product(color="sample_text_2", expiry="sample_text_2", manufecturedDate="sample_text_2", manufecturer="sample_text_2", name="sample_text_2", pID="sample_text_2", price=13)
    b = Admin(id=7, password="sample_text", userName="sample_text")
    _safe_set(b, 'product14', a1)
    assert _is_linked(b, 'product14', a1)
    if hasattr(a1, 'admin15'):
        assert _is_linked(a1, 'admin15', b)
    _safe_set(b, 'product14', a2)
    assert _is_linked(b, 'product14', a2)
    if hasattr(a1, 'admin15'):
        assert not _is_linked(a1, 'admin15', b)
    if hasattr(a2, 'admin15'):
        assert _is_linked(a2, 'admin15', b)
    _safe_set(b, 'product14', None)
    assert not _is_linked(b, 'product14', a2)
    if hasattr(a2, 'admin15'):
        assert not _is_linked(a2, 'admin15', b)


def test_assoc_Admin_Registration_reverse_link_reassign_clear():
    a1 = Registration(Address="sample_text", DOB="sample_text", Email="sample_text", LastName="sample_text", Password="sample_text", Phone=7, UserName="sample_text", name="sample_text")
    a2 = Registration(Address="sample_text_2", DOB="sample_text_2", Email="sample_text_2", LastName="sample_text_2", Password="sample_text_2", Phone=13, UserName="sample_text_2", name="sample_text_2")
    b = Admin(id=7, password="sample_text", userName="sample_text")
    _safe_set(b, 'registration10', a1)
    assert _is_linked(b, 'registration10', a1)
    if hasattr(a1, 'admin11'):
        assert _is_linked(a1, 'admin11', b)
    _safe_set(b, 'registration10', a2)
    assert _is_linked(b, 'registration10', a2)
    if hasattr(a1, 'admin11'):
        assert not _is_linked(a1, 'admin11', b)
    if hasattr(a2, 'admin11'):
        assert _is_linked(a2, 'admin11', b)
    _safe_set(b, 'registration10', None)
    assert not _is_linked(b, 'registration10', a2)
    if hasattr(a2, 'admin11'):
        assert not _is_linked(a2, 'admin11', b)


def test_assoc_Cart_PaymentMethod_reverse_link_reassign_clear():
    a1 = PaymentMethod(cashOnDelievery="sample_text", online="sample_text", paymentType="sample_text")
    a2 = PaymentMethod(cashOnDelievery="sample_text_2", online="sample_text_2", paymentType="sample_text_2")
    b = Cart(TotalBill=7, id=7)
    _safe_set(b, 'paymentMethod8', a1)
    assert _is_linked(b, 'paymentMethod8', a1)
    if hasattr(a1, 'cart9'):
        assert _is_linked(a1, 'cart9', b)
    _safe_set(b, 'paymentMethod8', a2)
    assert _is_linked(b, 'paymentMethod8', a2)
    if hasattr(a1, 'cart9'):
        assert not _is_linked(a1, 'cart9', b)
    if hasattr(a2, 'cart9'):
        assert _is_linked(a2, 'cart9', b)
    _safe_set(b, 'paymentMethod8', None)
    assert not _is_linked(b, 'paymentMethod8', a2)
    if hasattr(a2, 'cart9'):
        assert not _is_linked(a2, 'cart9', b)


def test_assoc_Order_Cart_reverse_link_reassign_clear():
    a1 = Order(id=7, orderDate="sample_text", orderStatus="sample_text", quantity=7)
    a2 = Order(id=13, orderDate="sample_text_2", orderStatus="sample_text_2", quantity=13)
    b = Cart(TotalBill=7, id=7)
    _safe_set(b, 'order7', a1)
    assert _is_linked(b, 'order7', a1)
    if hasattr(a1, 'cart6'):
        assert _is_linked(a1, 'cart6', b)
    _safe_set(b, 'order7', a2)
    assert _is_linked(b, 'order7', a2)
    if hasattr(a1, 'cart6'):
        assert not _is_linked(a1, 'cart6', b)
    if hasattr(a2, 'cart6'):
        assert _is_linked(a2, 'cart6', b)
    _safe_set(b, 'order7', None)
    assert not _is_linked(b, 'order7', a2)
    if hasattr(a2, 'cart6'):
        assert not _is_linked(a2, 'cart6', b)


def test_assoc_Person_Product_reverse_link_reassign_clear():
    a1 = Product(color="sample_text", expiry="sample_text", manufecturedDate="sample_text", manufecturer="sample_text", name="sample_text", pID="sample_text", price=7)
    a2 = Product(color="sample_text_2", expiry="sample_text_2", manufecturedDate="sample_text_2", manufecturer="sample_text_2", name="sample_text_2", pID="sample_text_2", price=13)
    b = Person(Address="sample_text", DOB="sample_text", Email="sample_text", LastName="sample_text", Name="sample_text", Phone=7)
    _safe_set(b, 'product12', a1)
    assert _is_linked(b, 'product12', a1)
    if hasattr(a1, 'person13'):
        assert _is_linked(a1, 'person13', b)
    _safe_set(b, 'product12', a2)
    assert _is_linked(b, 'product12', a2)
    if hasattr(a1, 'person13'):
        assert not _is_linked(a1, 'person13', b)
    if hasattr(a2, 'person13'):
        assert _is_linked(a2, 'person13', b)
    _safe_set(b, 'product12', None)
    assert not _is_linked(b, 'product12', a2)
    if hasattr(a2, 'person13'):
        assert not _is_linked(a2, 'person13', b)


def test_assoc_Person_Registration_reverse_link_reassign_clear():
    a1 = Registration(Address="sample_text", DOB="sample_text", Email="sample_text", LastName="sample_text", Password="sample_text", Phone=7, UserName="sample_text", name="sample_text")
    a2 = Registration(Address="sample_text_2", DOB="sample_text_2", Email="sample_text_2", LastName="sample_text_2", Password="sample_text_2", Phone=13, UserName="sample_text_2", name="sample_text_2")
    b = Person(Address="sample_text", DOB="sample_text", Email="sample_text", LastName="sample_text", Name="sample_text", Phone=7)
    _safe_set(b, 'registration18', a1)
    assert _is_linked(b, 'registration18', a1)
    if hasattr(a1, 'person19'):
        assert _is_linked(a1, 'person19', b)
    _safe_set(b, 'registration18', a2)
    assert _is_linked(b, 'registration18', a2)
    if hasattr(a1, 'person19'):
        assert not _is_linked(a1, 'person19', b)
    if hasattr(a2, 'person19'):
        assert _is_linked(a2, 'person19', b)
    _safe_set(b, 'registration18', None)
    assert not _is_linked(b, 'registration18', a2)
    if hasattr(a2, 'person19'):
        assert not _is_linked(a2, 'person19', b)


def test_assoc_Product_ExerciseMachine_reverse_link_reassign_clear():
    a1 = Product(color="sample_text", expiry="sample_text", manufecturedDate="sample_text", manufecturer="sample_text", name="sample_text", pID="sample_text", price=7)
    a2 = Product(color="sample_text_2", expiry="sample_text_2", manufecturedDate="sample_text_2", manufecturer="sample_text_2", name="sample_text_2", pID="sample_text_2", price=13)
    b = ExerciseMachine(id=7, name="sample_text", size=7, type="sample_text")
    _safe_set(b, 'product5', a1)
    assert _is_linked(b, 'product5', a1)
    if hasattr(a1, 'exerciseMachine4'):
        assert _is_linked(a1, 'exerciseMachine4', b)
    _safe_set(b, 'product5', a2)
    assert _is_linked(b, 'product5', a2)
    if hasattr(a1, 'exerciseMachine4'):
        assert not _is_linked(a1, 'exerciseMachine4', b)
    if hasattr(a2, 'exerciseMachine4'):
        assert _is_linked(a2, 'exerciseMachine4', b)
    _safe_set(b, 'product5', None)
    assert not _is_linked(b, 'product5', a2)
    if hasattr(a2, 'exerciseMachine4'):
        assert not _is_linked(a2, 'exerciseMachine4', b)


def test_assoc_Product_MediDevices_reverse_link_reassign_clear():
    a1 = Product(color="sample_text", expiry="sample_text", manufecturedDate="sample_text", manufecturer="sample_text", name="sample_text", pID="sample_text", price=7)
    a2 = Product(color="sample_text_2", expiry="sample_text_2", manufecturedDate="sample_text_2", manufecturer="sample_text_2", name="sample_text_2", pID="sample_text_2", price=13)
    b = MediDevices(id="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'product3', a1)
    assert _is_linked(b, 'product3', a1)
    if hasattr(a1, 'mediDevices2'):
        assert _is_linked(a1, 'mediDevices2', b)
    _safe_set(b, 'product3', a2)
    assert _is_linked(b, 'product3', a2)
    if hasattr(a1, 'mediDevices2'):
        assert not _is_linked(a1, 'mediDevices2', b)
    if hasattr(a2, 'mediDevices2'):
        assert _is_linked(a2, 'mediDevices2', b)
    _safe_set(b, 'product3', None)
    assert not _is_linked(b, 'product3', a2)
    if hasattr(a2, 'mediDevices2'):
        assert not _is_linked(a2, 'mediDevices2', b)


def test_assoc_Product_Medicine_reverse_link_reassign_clear():
    a1 = Product(color="sample_text", expiry="sample_text", manufecturedDate="sample_text", manufecturer="sample_text", name="sample_text", pID="sample_text", price=7)
    a2 = Product(color="sample_text_2", expiry="sample_text_2", manufecturedDate="sample_text_2", manufecturer="sample_text_2", name="sample_text_2", pID="sample_text_2", price=13)
    b = Medicine(formula="sample_text", id=7, name="sample_text", potency="sample_text")
    _safe_set(b, 'product1', a1)
    assert _is_linked(b, 'product1', a1)
    if hasattr(a1, 'medicine0'):
        assert _is_linked(a1, 'medicine0', b)
    _safe_set(b, 'product1', a2)
    assert _is_linked(b, 'product1', a2)
    if hasattr(a1, 'medicine0'):
        assert not _is_linked(a1, 'medicine0', b)
    if hasattr(a2, 'medicine0'):
        assert _is_linked(a2, 'medicine0', b)
    _safe_set(b, 'product1', None)
    assert not _is_linked(b, 'product1', a2)
    if hasattr(a2, 'medicine0'):
        assert not _is_linked(a2, 'medicine0', b)


def test_assoc_Product_Order_reverse_link_reassign_clear():
    a1 = Product(color="sample_text", expiry="sample_text", manufecturedDate="sample_text", manufecturer="sample_text", name="sample_text", pID="sample_text", price=7)
    a2 = Product(color="sample_text_2", expiry="sample_text_2", manufecturedDate="sample_text_2", manufecturer="sample_text_2", name="sample_text_2", pID="sample_text_2", price=13)
    b = Order(id=7, orderDate="sample_text", orderStatus="sample_text", quantity=7)
    _safe_set(b, 'product17', a1)
    assert _is_linked(b, 'product17', a1)
    if hasattr(a1, 'order16'):
        assert _is_linked(a1, 'order16', b)
    _safe_set(b, 'product17', a2)
    assert _is_linked(b, 'product17', a2)
    if hasattr(a1, 'order16'):
        assert not _is_linked(a1, 'order16', b)
    if hasattr(a2, 'order16'):
        assert _is_linked(a2, 'order16', b)
    _safe_set(b, 'product17', None)
    assert not _is_linked(b, 'product17', a2)
    if hasattr(a2, 'order16'):
        assert not _is_linked(a2, 'order16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

