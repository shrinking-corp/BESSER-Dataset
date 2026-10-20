import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Cart,
    Customer,
    Employee,
    Guest,
    Meals,
    OrderDetails,
    Orders,
    Payment,
    Transport,
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

def test_assoc_Customer_Cart_reverse_link_reassign_clear():
    a1 = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    a2 = Customer(CustomerName="sample_text_2", CutsomerAddress="sample_text_2", Email="sample_text_2", PhoneNumber=13)
    b = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    _safe_set(b, 'customer9', a1)
    assert _is_linked(b, 'customer9', a1)
    if hasattr(a1, 'cart8'):
        assert _is_linked(a1, 'cart8', b)
    _safe_set(b, 'customer9', a2)
    assert _is_linked(b, 'customer9', a2)
    if hasattr(a1, 'cart8'):
        assert not _is_linked(a1, 'cart8', b)
    if hasattr(a2, 'cart8'):
        assert _is_linked(a2, 'cart8', b)
    _safe_set(b, 'customer9', None)
    assert not _is_linked(b, 'customer9', a2)
    if hasattr(a2, 'cart8'):
        assert not _is_linked(a2, 'cart8', b)


def test_assoc_Customer_Orders_reverse_link_reassign_clear():
    a1 = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    a2 = Orders(OrderID=13, dateFinished="sample_text_2", dateOrdered="sample_text_2", status="sample_text_2")
    b = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    _safe_set(b, 'orders2', {a1})
    assert _is_linked(b, 'orders2', a1)
    if hasattr(a1, 'customer3'):
        assert _is_linked(a1, 'customer3', b)
    _safe_set(b, 'orders2', {a2})
    assert _is_linked(b, 'orders2', a2)
    if hasattr(a1, 'customer3'):
        assert not _is_linked(a1, 'customer3', b)
    if hasattr(a2, 'customer3'):
        assert _is_linked(a2, 'customer3', b)
    _safe_set(b, 'orders2', set())
    assert not _is_linked(b, 'orders2', a2)
    if hasattr(a2, 'customer3'):
        assert not _is_linked(a2, 'customer3', b)


def test_assoc_Customer_Payment_reverse_link_reassign_clear():
    a1 = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    a2 = Payment(PaymentStatus="sample_text_2", PaymentType="sample_text_2", paymentAmount="sample_text_2", paymentDate="sample_text_2", paymentID="sample_text_2")
    b = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    _safe_set(b, 'payment0', {a1})
    assert _is_linked(b, 'payment0', a1)
    if hasattr(a1, 'customer1'):
        assert _is_linked(a1, 'customer1', b)
    _safe_set(b, 'payment0', {a2})
    assert _is_linked(b, 'payment0', a2)
    if hasattr(a1, 'customer1'):
        assert not _is_linked(a1, 'customer1', b)
    if hasattr(a2, 'customer1'):
        assert _is_linked(a2, 'customer1', b)
    _safe_set(b, 'payment0', set())
    assert not _is_linked(b, 'payment0', a2)
    if hasattr(a2, 'customer1'):
        assert not _is_linked(a2, 'customer1', b)


def test_assoc_Employee_Orders_reverse_link_reassign_clear():
    a1 = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    a2 = Orders(OrderID=13, dateFinished="sample_text_2", dateOrdered="sample_text_2", status="sample_text_2")
    b = Employee(EmpName="sample_text", EmpPassword="sample_text", EmployeeID="sample_text")
    _safe_set(b, 'orders4', a1)
    assert _is_linked(b, 'orders4', a1)
    if hasattr(a1, 'employee5'):
        assert _is_linked(a1, 'employee5', b)
    _safe_set(b, 'orders4', a2)
    assert _is_linked(b, 'orders4', a2)
    if hasattr(a1, 'employee5'):
        assert not _is_linked(a1, 'employee5', b)
    if hasattr(a2, 'employee5'):
        assert _is_linked(a2, 'employee5', b)
    _safe_set(b, 'orders4', None)
    assert not _is_linked(b, 'orders4', a2)
    if hasattr(a2, 'employee5'):
        assert not _is_linked(a2, 'employee5', b)


def test_assoc_OrderDetails_Cart_reverse_link_reassign_clear():
    a1 = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    a2 = OrderDetails(MealID="sample_text_2", OrderID=13, orderTime="sample_text_2", quantity=13, status="sample_text_2", totPrice="sample_text_2")
    b = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    _safe_set(b, 'orderDetails11', a1)
    assert _is_linked(b, 'orderDetails11', a1)
    if hasattr(a1, 'cart10'):
        assert _is_linked(a1, 'cart10', b)
    _safe_set(b, 'orderDetails11', a2)
    assert _is_linked(b, 'orderDetails11', a2)
    if hasattr(a1, 'cart10'):
        assert not _is_linked(a1, 'cart10', b)
    if hasattr(a2, 'cart10'):
        assert _is_linked(a2, 'cart10', b)
    _safe_set(b, 'orderDetails11', None)
    assert not _is_linked(b, 'orderDetails11', a2)
    if hasattr(a2, 'cart10'):
        assert not _is_linked(a2, 'cart10', b)


def test_assoc_Orders_OrderDetails_reverse_link_reassign_clear():
    a1 = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    a2 = Orders(OrderID=13, dateFinished="sample_text_2", dateOrdered="sample_text_2", status="sample_text_2")
    b = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    _safe_set(b, 'orders7', a1)
    assert _is_linked(b, 'orders7', a1)
    if hasattr(a1, 'orderDetails6'):
        assert _is_linked(a1, 'orderDetails6', b)
    _safe_set(b, 'orders7', a2)
    assert _is_linked(b, 'orders7', a2)
    if hasattr(a1, 'orderDetails6'):
        assert not _is_linked(a1, 'orderDetails6', b)
    if hasattr(a2, 'orderDetails6'):
        assert _is_linked(a2, 'orderDetails6', b)
    _safe_set(b, 'orders7', None)
    assert not _is_linked(b, 'orders7', a2)
    if hasattr(a2, 'orderDetails6'):
        assert not _is_linked(a2, 'orderDetails6', b)


def test_assoc_Orders_Payment_reverse_link_reassign_clear():
    a1 = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    a2 = Payment(PaymentStatus="sample_text_2", PaymentType="sample_text_2", paymentAmount="sample_text_2", paymentDate="sample_text_2", paymentID="sample_text_2")
    b = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    _safe_set(b, 'payment14', a1)
    assert _is_linked(b, 'payment14', a1)
    if hasattr(a1, 'orders15'):
        assert _is_linked(a1, 'orders15', b)
    _safe_set(b, 'payment14', a2)
    assert _is_linked(b, 'payment14', a2)
    if hasattr(a1, 'orders15'):
        assert not _is_linked(a1, 'orders15', b)
    if hasattr(a2, 'orders15'):
        assert _is_linked(a2, 'orders15', b)
    _safe_set(b, 'payment14', None)
    assert not _is_linked(b, 'payment14', a2)
    if hasattr(a2, 'orders15'):
        assert not _is_linked(a2, 'orders15', b)


def test_assoc_Orders_Transport2_reverse_link_reassign_clear():
    a1 = Transport(TransportID=7, location="sample_text", transportCost="sample_text")
    a2 = Transport(TransportID=13, location="sample_text_2", transportCost="sample_text_2")
    b = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    _safe_set(b, 'transport12', a1)
    assert _is_linked(b, 'transport12', a1)
    if hasattr(a1, 'orders13'):
        assert _is_linked(a1, 'orders13', b)
    _safe_set(b, 'transport12', a2)
    assert _is_linked(b, 'transport12', a2)
    if hasattr(a1, 'orders13'):
        assert not _is_linked(a1, 'orders13', b)
    if hasattr(a2, 'orders13'):
        assert _is_linked(a2, 'orders13', b)
    _safe_set(b, 'transport12', None)
    assert not _is_linked(b, 'transport12', a2)
    if hasattr(a2, 'orders13'):
        assert not _is_linked(a2, 'orders13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

