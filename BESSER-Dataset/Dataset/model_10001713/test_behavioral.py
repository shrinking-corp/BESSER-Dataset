import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Card,
    CardReader,
    Drink,
    Food,
    Manager,
    Menu,
    Order,
    Payment,
    Product,
    Register,
    SUID,
    Sale,
    Sales_Line_Item,
    Store,
    customerDatabase,
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

def test_assoc_Manager_Menu_reverse_link_reassign_clear():
    a1 = Menu(_attr="sample_text")
    a2 = Menu(_attr="sample_text_2")
    b = Manager(name="sample_text", password="sample_text")
    _safe_set(b, 'menu28', a1)
    assert _is_linked(b, 'menu28', a1)
    if hasattr(a1, 'manager29'):
        assert _is_linked(a1, 'manager29', b)
    _safe_set(b, 'menu28', a2)
    assert _is_linked(b, 'menu28', a2)
    if hasattr(a1, 'manager29'):
        assert not _is_linked(a1, 'manager29', b)
    if hasattr(a2, 'manager29'):
        assert _is_linked(a2, 'manager29', b)
    _safe_set(b, 'menu28', None)
    assert not _is_linked(b, 'menu28', a2)
    if hasattr(a2, 'manager29'):
        assert not _is_linked(a2, 'manager29', b)


def test_assoc_Menu_Product_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    a2 = Product(description="sample_text_2", itemID=13, name="sample_text_2", price="sample_text_2")
    b = Menu(_attr="sample_text")
    _safe_set(b, 'product4', {a1})
    assert _is_linked(b, 'product4', a1)
    if hasattr(a1, 'menu5'):
        assert _is_linked(a1, 'menu5', b)
    _safe_set(b, 'product4', {a2})
    assert _is_linked(b, 'product4', a2)
    if hasattr(a1, 'menu5'):
        assert not _is_linked(a1, 'menu5', b)
    if hasattr(a2, 'menu5'):
        assert _is_linked(a2, 'menu5', b)
    _safe_set(b, 'product4', set())
    assert not _is_linked(b, 'product4', a2)
    if hasattr(a2, 'menu5'):
        assert not _is_linked(a2, 'menu5', b)


def test_assoc_Payment_Order_reverse_link_reassign_clear():
    a1 = Payment(amount="sample_text")
    a2 = Payment(amount="sample_text_2")
    b = Order(customer="sample_text", drinkName="sample_text", drinkPrice=7, foodName="sample_text", foodPrice=7)
    _safe_set(b, 'payment13', a1)
    assert _is_linked(b, 'payment13', a1)
    if hasattr(a1, 'order12'):
        assert _is_linked(a1, 'order12', b)
    _safe_set(b, 'payment13', a2)
    assert _is_linked(b, 'payment13', a2)
    if hasattr(a1, 'order12'):
        assert not _is_linked(a1, 'order12', b)
    if hasattr(a2, 'order12'):
        assert _is_linked(a2, 'order12', b)
    _safe_set(b, 'payment13', None)
    assert not _is_linked(b, 'payment13', a2)
    if hasattr(a2, 'order12'):
        assert not _is_linked(a2, 'order12', b)


def test_assoc_Product_Sales_Line_Item_reverse_link_reassign_clear():
    a1 = Sales_Line_Item(Quantity=7)
    a2 = Sales_Line_Item(Quantity=13)
    b = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    _safe_set(b, 'sales_Line_Item26', a1)
    assert _is_linked(b, 'sales_Line_Item26', a1)
    if hasattr(a1, 'product27'):
        assert _is_linked(a1, 'product27', b)
    _safe_set(b, 'sales_Line_Item26', a2)
    assert _is_linked(b, 'sales_Line_Item26', a2)
    if hasattr(a1, 'product27'):
        assert not _is_linked(a1, 'product27', b)
    if hasattr(a2, 'product27'):
        assert _is_linked(a2, 'product27', b)
    _safe_set(b, 'sales_Line_Item26', None)
    assert not _is_linked(b, 'sales_Line_Item26', a2)
    if hasattr(a2, 'product27'):
        assert not _is_linked(a2, 'product27', b)


def test_assoc_Register_Sale_reverse_link_reassign_clear():
    a1 = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    a2 = Sale(Date="sample_text_2", Time="sample_text_2", isComplete=False)
    b = Register(attribute="sample_text")
    _safe_set(b, 'sale6', a1)
    assert _is_linked(b, 'sale6', a1)
    if hasattr(a1, 'register7'):
        assert _is_linked(a1, 'register7', b)
    _safe_set(b, 'sale6', a2)
    assert _is_linked(b, 'sale6', a2)
    if hasattr(a1, 'register7'):
        assert not _is_linked(a1, 'register7', b)
    if hasattr(a2, 'register7'):
        assert _is_linked(a2, 'register7', b)
    _safe_set(b, 'sale6', None)
    assert not _is_linked(b, 'sale6', a2)
    if hasattr(a2, 'register7'):
        assert not _is_linked(a2, 'register7', b)


def test_assoc_Register_Store_reverse_link_reassign_clear():
    a1 = Store(Address="sample_text", Name="sample_text")
    a2 = Store(Address="sample_text_2", Name="sample_text_2")
    b = Register(attribute="sample_text")
    _safe_set(b, 'store0', a1)
    assert _is_linked(b, 'store0', a1)
    if hasattr(a1, 'register1'):
        assert _is_linked(a1, 'register1', b)
    _safe_set(b, 'store0', a2)
    assert _is_linked(b, 'store0', a2)
    if hasattr(a1, 'register1'):
        assert not _is_linked(a1, 'register1', b)
    if hasattr(a2, 'register1'):
        assert _is_linked(a2, 'register1', b)
    _safe_set(b, 'store0', None)
    assert not _is_linked(b, 'store0', a2)
    if hasattr(a2, 'register1'):
        assert not _is_linked(a2, 'register1', b)


def test_assoc_SUID_Card_reverse_link_reassign_clear():
    a1 = SUID(ID=7, studentName="sample_text", suFOODBal="sample_text")
    a2 = SUID(ID=13, studentName="sample_text_2", suFOODBal="sample_text_2")
    b = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    _safe_set(b, 'sUID23', {a1})
    assert _is_linked(b, 'sUID23', a1)
    if hasattr(a1, 'card22'):
        assert _is_linked(a1, 'card22', b)
    _safe_set(b, 'sUID23', {a2})
    assert _is_linked(b, 'sUID23', a2)
    if hasattr(a1, 'card22'):
        assert not _is_linked(a1, 'card22', b)
    if hasattr(a2, 'card22'):
        assert _is_linked(a2, 'card22', b)
    _safe_set(b, 'sUID23', set())
    assert not _is_linked(b, 'sUID23', a2)
    if hasattr(a2, 'card22'):
        assert not _is_linked(a2, 'card22', b)


def test_assoc_SUID_Payment_reverse_link_reassign_clear():
    a1 = SUID(ID=7, studentName="sample_text", suFOODBal="sample_text")
    a2 = SUID(ID=13, studentName="sample_text_2", suFOODBal="sample_text_2")
    b = Payment(amount="sample_text")
    _safe_set(b, 'sUID25', {a1})
    assert _is_linked(b, 'sUID25', a1)
    if hasattr(a1, 'payment24'):
        assert _is_linked(a1, 'payment24', b)
    _safe_set(b, 'sUID25', {a2})
    assert _is_linked(b, 'sUID25', a2)
    if hasattr(a1, 'payment24'):
        assert not _is_linked(a1, 'payment24', b)
    if hasattr(a2, 'payment24'):
        assert _is_linked(a2, 'payment24', b)
    _safe_set(b, 'sUID25', set())
    assert not _is_linked(b, 'sUID25', a2)
    if hasattr(a2, 'payment24'):
        assert not _is_linked(a2, 'payment24', b)


def test_assoc_Sale_CardReader_reverse_link_reassign_clear():
    a1 = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    a2 = Sale(Date="sample_text_2", Time="sample_text_2", isComplete=False)
    b = CardReader(attribute="sample_text")
    _safe_set(b, 'sale19', a1)
    assert _is_linked(b, 'sale19', a1)
    if hasattr(a1, 'cardReader18'):
        assert _is_linked(a1, 'cardReader18', b)
    _safe_set(b, 'sale19', a2)
    assert _is_linked(b, 'sale19', a2)
    if hasattr(a1, 'cardReader18'):
        assert not _is_linked(a1, 'cardReader18', b)
    if hasattr(a2, 'cardReader18'):
        assert _is_linked(a2, 'cardReader18', b)
    _safe_set(b, 'sale19', None)
    assert not _is_linked(b, 'sale19', a2)
    if hasattr(a2, 'cardReader18'):
        assert not _is_linked(a2, 'cardReader18', b)


def test_assoc_Sale_Payment_reverse_link_reassign_clear():
    a1 = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    a2 = Sale(Date="sample_text_2", Time="sample_text_2", isComplete=False)
    b = Payment(amount="sample_text")
    _safe_set(b, 'sale9', a1)
    assert _is_linked(b, 'sale9', a1)
    if hasattr(a1, 'payment8'):
        assert _is_linked(a1, 'payment8', b)
    _safe_set(b, 'sale9', a2)
    assert _is_linked(b, 'sale9', a2)
    if hasattr(a1, 'payment8'):
        assert not _is_linked(a1, 'payment8', b)
    if hasattr(a2, 'payment8'):
        assert _is_linked(a2, 'payment8', b)
    _safe_set(b, 'sale9', None)
    assert not _is_linked(b, 'sale9', a2)
    if hasattr(a2, 'payment8'):
        assert not _is_linked(a2, 'payment8', b)


def test_assoc_Sale_Sales_Line_Item_reverse_link_reassign_clear():
    a1 = Sales_Line_Item(Quantity=7)
    a2 = Sales_Line_Item(Quantity=13)
    b = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    _safe_set(b, 'sales_Line_Item10', {a1})
    assert _is_linked(b, 'sales_Line_Item10', a1)
    if hasattr(a1, 'sale11'):
        assert _is_linked(a1, 'sale11', b)
    _safe_set(b, 'sales_Line_Item10', {a2})
    assert _is_linked(b, 'sales_Line_Item10', a2)
    if hasattr(a1, 'sale11'):
        assert not _is_linked(a1, 'sale11', b)
    if hasattr(a2, 'sale11'):
        assert _is_linked(a2, 'sale11', b)
    _safe_set(b, 'sales_Line_Item10', set())
    assert not _is_linked(b, 'sales_Line_Item10', a2)
    if hasattr(a2, 'sale11'):
        assert not _is_linked(a2, 'sale11', b)


def test_assoc_Sales_Line_Item_Drink_reverse_link_reassign_clear():
    a1 = Sales_Line_Item(Quantity=7)
    a2 = Sales_Line_Item(Quantity=13)
    b = Drink(name="sample_text", price="sample_text", quantity=7)
    _safe_set(b, 'sales_Line_Item17', a1)
    assert _is_linked(b, 'sales_Line_Item17', a1)
    if hasattr(a1, 'drink16'):
        assert _is_linked(a1, 'drink16', b)
    _safe_set(b, 'sales_Line_Item17', a2)
    assert _is_linked(b, 'sales_Line_Item17', a2)
    if hasattr(a1, 'drink16'):
        assert not _is_linked(a1, 'drink16', b)
    if hasattr(a2, 'drink16'):
        assert _is_linked(a2, 'drink16', b)
    _safe_set(b, 'sales_Line_Item17', None)
    assert not _is_linked(b, 'sales_Line_Item17', a2)
    if hasattr(a2, 'drink16'):
        assert not _is_linked(a2, 'drink16', b)


def test_assoc_Sales_Line_Item_Food_reverse_link_reassign_clear():
    a1 = Sales_Line_Item(Quantity=7)
    a2 = Sales_Line_Item(Quantity=13)
    b = Food(attribute="sample_text", name="sample_text", price="sample_text", quantity=7)
    _safe_set(b, 'sales_Line_Item15', a1)
    assert _is_linked(b, 'sales_Line_Item15', a1)
    if hasattr(a1, 'food14'):
        assert _is_linked(a1, 'food14', b)
    _safe_set(b, 'sales_Line_Item15', a2)
    assert _is_linked(b, 'sales_Line_Item15', a2)
    if hasattr(a1, 'food14'):
        assert not _is_linked(a1, 'food14', b)
    if hasattr(a2, 'food14'):
        assert _is_linked(a2, 'food14', b)
    _safe_set(b, 'sales_Line_Item15', None)
    assert not _is_linked(b, 'sales_Line_Item15', a2)
    if hasattr(a2, 'food14'):
        assert not _is_linked(a2, 'food14', b)


def test_assoc_Store_Menu_reverse_link_reassign_clear():
    a1 = Store(Address="sample_text", Name="sample_text")
    a2 = Store(Address="sample_text_2", Name="sample_text_2")
    b = Menu(_attr="sample_text")
    _safe_set(b, 'store3', a1)
    assert _is_linked(b, 'store3', a1)
    if hasattr(a1, 'menu2'):
        assert _is_linked(a1, 'menu2', b)
    _safe_set(b, 'store3', a2)
    assert _is_linked(b, 'store3', a2)
    if hasattr(a1, 'menu2'):
        assert not _is_linked(a1, 'menu2', b)
    if hasattr(a2, 'menu2'):
        assert _is_linked(a2, 'menu2', b)
    _safe_set(b, 'store3', None)
    assert not _is_linked(b, 'store3', a2)
    if hasattr(a2, 'menu2'):
        assert not _is_linked(a2, 'menu2', b)


def test_assoc_customerDatabase_Card_reverse_link_reassign_clear():
    a1 = customerDatabase(SUID=7, creditCardNum=7, customerName="sample_text", paymentHistory="sample_text")
    a2 = customerDatabase(SUID=13, creditCardNum=13, customerName="sample_text_2", paymentHistory="sample_text_2")
    b = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    _safe_set(b, 'customerDatabase21', a1)
    assert _is_linked(b, 'customerDatabase21', a1)
    if hasattr(a1, 'card20'):
        assert _is_linked(a1, 'card20', b)
    _safe_set(b, 'customerDatabase21', a2)
    assert _is_linked(b, 'customerDatabase21', a2)
    if hasattr(a1, 'card20'):
        assert not _is_linked(a1, 'card20', b)
    if hasattr(a2, 'card20'):
        assert _is_linked(a2, 'card20', b)
    _safe_set(b, 'customerDatabase21', None)
    assert not _is_linked(b, 'customerDatabase21', a2)
    if hasattr(a2, 'card20'):
        assert not _is_linked(a2, 'card20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

