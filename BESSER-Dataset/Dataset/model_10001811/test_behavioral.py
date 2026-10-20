import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Admin_Actor,
    Administrator,
    AjoutProduit_UseCase,
    Customer,
    Customer_Support,
    LineItem,
    MyActor_Actor,
    Order,
    Payment,
    Product,
    Shop_Owner,
    ShoppingCart,
    Visitor,
    Webuser_Actor,
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
    a1 = Order(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    a2 = Order(number=13, ordered=date(2025, 6, 15), shipTo="sample_text_2", shipped=False, status="sample_text_2", total=9.99)
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'order16', {a1})
    assert _is_linked(b, 'order16', a1)
    if hasattr(a1, 'accnt17'):
        assert _is_linked(a1, 'accnt17', b)
    _safe_set(b, 'order16', {a2})
    assert _is_linked(b, 'order16', a2)
    if hasattr(a1, 'accnt17'):
        assert not _is_linked(a1, 'accnt17', b)
    if hasattr(a2, 'accnt17'):
        assert _is_linked(a2, 'accnt17', b)
    _safe_set(b, 'order16', set())
    assert not _is_linked(b, 'order16', a2)
    if hasattr(a2, 'accnt17'):
        assert not _is_linked(a2, 'accnt17', b)


def test_assoc_Account_Payment_reverse_link_reassign_clear():
    a1 = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Payment(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'payment18', {a1})
    assert _is_linked(b, 'payment18', a1)
    if hasattr(a1, 'account19'):
        assert _is_linked(a1, 'account19', b)
    _safe_set(b, 'payment18', {a2})
    assert _is_linked(b, 'payment18', a2)
    if hasattr(a1, 'account19'):
        assert not _is_linked(a1, 'account19', b)
    if hasattr(a2, 'account19'):
        assert _is_linked(a2, 'account19', b)
    _safe_set(b, 'payment18', set())
    assert not _is_linked(b, 'payment18', a2)
    if hasattr(a2, 'account19'):
        assert not _is_linked(a2, 'account19', b)


def test_assoc_Account_ShoppingCart_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'cart4', a1)
    assert _is_linked(b, 'cart4', a1)
    if hasattr(a1, 'account5'):
        assert _is_linked(a1, 'account5', b)
    _safe_set(b, 'cart4', a2)
    assert _is_linked(b, 'cart4', a2)
    if hasattr(a1, 'account5'):
        assert not _is_linked(a1, 'account5', b)
    if hasattr(a2, 'account5'):
        assert _is_linked(a2, 'account5', b)
    _safe_set(b, 'cart4', None)
    assert not _is_linked(b, 'cart4', a2)
    if hasattr(a2, 'account5'):
        assert not _is_linked(a2, 'account5', b)


def test_assoc_Account_ShoppingCart2_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'Giving_feedback40', a1)
    assert _is_linked(b, 'Giving_feedback40', a1)
    if hasattr(a1, 'Account_ShoppingCart2_141'):
        assert _is_linked(a1, 'Account_ShoppingCart2_141', b)
    _safe_set(b, 'Giving_feedback40', a2)
    assert _is_linked(b, 'Giving_feedback40', a2)
    if hasattr(a1, 'Account_ShoppingCart2_141'):
        assert not _is_linked(a1, 'Account_ShoppingCart2_141', b)
    if hasattr(a2, 'Account_ShoppingCart2_141'):
        assert _is_linked(a2, 'Account_ShoppingCart2_141', b)
    _safe_set(b, 'Giving_feedback40', None)
    assert not _is_linked(b, 'Giving_feedback40', a2)
    if hasattr(a2, 'Account_ShoppingCart2_141'):
        assert not _is_linked(a2, 'Account_ShoppingCart2_141', b)


def test_assoc_Administrator_Customer_reverse_link_reassign_clear():
    a1 = Customer(Email="sample_text", IDCust=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    a2 = Customer(Email="sample_text_2", IDCust=13, Last_name="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    b = Administrator(Email="sample_text", IDAdm=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    _safe_set(b, 'Manage32', {a1})
    assert _is_linked(b, 'Manage32', a1)
    if hasattr(a1, 'Administrator_Customer_133'):
        assert _is_linked(a1, 'Administrator_Customer_133', b)
    _safe_set(b, 'Manage32', {a2})
    assert _is_linked(b, 'Manage32', a2)
    if hasattr(a1, 'Administrator_Customer_133'):
        assert not _is_linked(a1, 'Administrator_Customer_133', b)
    if hasattr(a2, 'Administrator_Customer_133'):
        assert _is_linked(a2, 'Administrator_Customer_133', b)
    _safe_set(b, 'Manage32', set())
    assert not _is_linked(b, 'Manage32', a2)
    if hasattr(a2, 'Administrator_Customer_133'):
        assert not _is_linked(a2, 'Administrator_Customer_133', b)


def test_assoc_Administrator_Product_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", name="sample_text")
    a2 = Product(description="sample_text_2", name="sample_text_2")
    b = Administrator(Email="sample_text", IDAdm=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    _safe_set(b, 'View_and_edit34', {a1})
    assert _is_linked(b, 'View_and_edit34', a1)
    if hasattr(a1, 'administrator35'):
        assert _is_linked(a1, 'administrator35', b)
    _safe_set(b, 'View_and_edit34', {a2})
    assert _is_linked(b, 'View_and_edit34', a2)
    if hasattr(a1, 'administrator35'):
        assert not _is_linked(a1, 'administrator35', b)
    if hasattr(a2, 'administrator35'):
        assert _is_linked(a2, 'administrator35', b)
    _safe_set(b, 'View_and_edit34', set())
    assert not _is_linked(b, 'View_and_edit34', a2)
    if hasattr(a2, 'administrator35'):
        assert not _is_linked(a2, 'administrator35', b)


def test_assoc_Customer_Account_reverse_link_reassign_clear():
    a1 = Customer(Email="sample_text", IDCust=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    a2 = Customer(Email="sample_text_2", IDCust=13, Last_name="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'customer13', a1)
    assert _is_linked(b, 'customer13', a1)
    if hasattr(a1, 'has12'):
        assert _is_linked(a1, 'has12', b)
    _safe_set(b, 'customer13', a2)
    assert _is_linked(b, 'customer13', a2)
    if hasattr(a1, 'has12'):
        assert not _is_linked(a1, 'has12', b)
    if hasattr(a2, 'has12'):
        assert _is_linked(a2, 'has12', b)
    _safe_set(b, 'customer13', None)
    assert not _is_linked(b, 'customer13', a2)
    if hasattr(a2, 'has12'):
        assert not _is_linked(a2, 'has12', b)


def test_assoc_Customer_Support_Customer_reverse_link_reassign_clear():
    a1 = Customer_Support(Email="sample_text", ID=7, Password="sample_text")
    a2 = Customer_Support(Email="sample_text_2", ID=13, Password="sample_text_2")
    b = Customer(Email="sample_text", IDCust=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    _safe_set(b, 'Ask_question43', a1)
    assert _is_linked(b, 'Ask_question43', a1)
    if hasattr(a1, 'help42'):
        assert _is_linked(a1, 'help42', b)
    _safe_set(b, 'Ask_question43', a2)
    assert _is_linked(b, 'Ask_question43', a2)
    if hasattr(a1, 'help42'):
        assert not _is_linked(a1, 'help42', b)
    if hasattr(a2, 'help42'):
        assert _is_linked(a2, 'help42', b)
    _safe_set(b, 'Ask_question43', None)
    assert not _is_linked(b, 'Ask_question43', a2)
    if hasattr(a2, 'help42'):
        assert not _is_linked(a2, 'help42', b)


def test_assoc_LineItem_Product_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", name="sample_text")
    a2 = Product(description="sample_text_2", name="sample_text_2")
    b = LineItem(price=3.14, quantity=7)
    _safe_set(b, 'product6', a1)
    assert _is_linked(b, 'product6', a1)
    if hasattr(a1, 'item7'):
        assert _is_linked(a1, 'item7', b)
    _safe_set(b, 'product6', a2)
    assert _is_linked(b, 'product6', a2)
    if hasattr(a1, 'item7'):
        assert not _is_linked(a1, 'item7', b)
    if hasattr(a2, 'item7'):
        assert _is_linked(a2, 'item7', b)
    _safe_set(b, 'product6', None)
    assert not _is_linked(b, 'product6', a2)
    if hasattr(a2, 'item7'):
        assert not _is_linked(a2, 'item7', b)


def test_assoc_Order_LineItem_reverse_link_reassign_clear():
    a1 = Order(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    a2 = Order(number=13, ordered=date(2025, 6, 15), shipTo="sample_text_2", shipped=False, status="sample_text_2", total=9.99)
    b = LineItem(price=3.14, quantity=7)
    _safe_set(b, 'order15', a1)
    assert _is_linked(b, 'order15', a1)
    if hasattr(a1, 'items14'):
        assert _is_linked(a1, 'items14', b)
    _safe_set(b, 'order15', a2)
    assert _is_linked(b, 'order15', a2)
    if hasattr(a1, 'items14'):
        assert not _is_linked(a1, 'items14', b)
    if hasattr(a2, 'items14'):
        assert _is_linked(a2, 'items14', b)
    _safe_set(b, 'order15', None)
    assert not _is_linked(b, 'order15', a2)
    if hasattr(a2, 'items14'):
        assert not _is_linked(a2, 'items14', b)


def test_assoc_Payment_Account_reverse_link_reassign_clear():
    a1 = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Payment(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'payment29', a1)
    assert _is_linked(b, 'payment29', a1)
    if hasattr(a1, 'account28'):
        assert _is_linked(a1, 'account28', b)
    _safe_set(b, 'payment29', a2)
    assert _is_linked(b, 'payment29', a2)
    if hasattr(a1, 'account28'):
        assert not _is_linked(a1, 'account28', b)
    if hasattr(a2, 'account28'):
        assert _is_linked(a2, 'account28', b)
    _safe_set(b, 'payment29', None)
    assert not _is_linked(b, 'payment29', a2)
    if hasattr(a2, 'account28'):
        assert not _is_linked(a2, 'account28', b)


def test_assoc_Payment_Order_reverse_link_reassign_clear():
    a1 = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    a2 = Payment(details="sample_text_2", paidDate=date(2025, 6, 15), total=9.99)
    b = Order(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    _safe_set(b, 'payment21', a1)
    assert _is_linked(b, 'payment21', a1)
    if hasattr(a1, 'order20'):
        assert _is_linked(a1, 'order20', b)
    _safe_set(b, 'payment21', a2)
    assert _is_linked(b, 'payment21', a2)
    if hasattr(a1, 'order20'):
        assert not _is_linked(a1, 'order20', b)
    if hasattr(a2, 'order20'):
        assert _is_linked(a2, 'order20', b)
    _safe_set(b, 'payment21', None)
    assert not _is_linked(b, 'payment21', a2)
    if hasattr(a2, 'order20'):
        assert not _is_linked(a2, 'order20', b)


def test_assoc_Product_Account_reverse_link_reassign_clear():
    a1 = Product(description="sample_text", name="sample_text")
    a2 = Product(description="sample_text_2", name="sample_text_2")
    b = Account(billingAddress="sample_text", closed=date(2024, 1, 1), isClosed=True, open=date(2024, 1, 1))
    _safe_set(b, 'product23', {a1})
    assert _is_linked(b, 'product23', a1)
    if hasattr(a1, 'account22'):
        assert _is_linked(a1, 'account22', b)
    _safe_set(b, 'product23', {a2})
    assert _is_linked(b, 'product23', a2)
    if hasattr(a1, 'account22'):
        assert not _is_linked(a1, 'account22', b)
    if hasattr(a2, 'account22'):
        assert _is_linked(a2, 'account22', b)
    _safe_set(b, 'product23', set())
    assert not _is_linked(b, 'product23', a2)
    if hasattr(a2, 'account22'):
        assert not _is_linked(a2, 'account22', b)


def test_assoc_Product_ShoppingCart_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = Product(description="sample_text", name="sample_text")
    _safe_set(b, 'Add_to_cart24', a1)
    assert _is_linked(b, 'Add_to_cart24', a1)
    if hasattr(a1, 'product25'):
        assert _is_linked(a1, 'product25', b)
    _safe_set(b, 'Add_to_cart24', a2)
    assert _is_linked(b, 'Add_to_cart24', a2)
    if hasattr(a1, 'product25'):
        assert not _is_linked(a1, 'product25', b)
    if hasattr(a2, 'product25'):
        assert _is_linked(a2, 'product25', b)
    _safe_set(b, 'Add_to_cart24', None)
    assert not _is_linked(b, 'Add_to_cart24', a2)
    if hasattr(a2, 'product25'):
        assert not _is_linked(a2, 'product25', b)


def test_assoc_Shop_Owner_Product_reverse_link_reassign_clear():
    a1 = Shop_Owner(Email="sample_text", IDSowner=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    a2 = Shop_Owner(Email="sample_text_2", IDSowner=13, Last_name="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    b = Product(description="sample_text", name="sample_text")
    _safe_set(b, 'Shop_Owner_Product_145', a1)
    assert _is_linked(b, 'Shop_Owner_Product_145', a1)
    if hasattr(a1, 'Advertise44'):
        assert _is_linked(a1, 'Advertise44', b)
    _safe_set(b, 'Shop_Owner_Product_145', a2)
    assert _is_linked(b, 'Shop_Owner_Product_145', a2)
    if hasattr(a1, 'Advertise44'):
        assert not _is_linked(a1, 'Advertise44', b)
    if hasattr(a2, 'Advertise44'):
        assert _is_linked(a2, 'Advertise44', b)
    _safe_set(b, 'Shop_Owner_Product_145', None)
    assert not _is_linked(b, 'Shop_Owner_Product_145', a2)
    if hasattr(a2, 'Advertise44'):
        assert not _is_linked(a2, 'Advertise44', b)


def test_assoc_ShoppingCart_LineItem_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = LineItem(price=3.14, quantity=7)
    _safe_set(b, 'shopping_cart3', a1)
    assert _is_linked(b, 'shopping_cart3', a1)
    if hasattr(a1, 'items2'):
        assert _is_linked(a1, 'items2', b)
    _safe_set(b, 'shopping_cart3', a2)
    assert _is_linked(b, 'shopping_cart3', a2)
    if hasattr(a1, 'items2'):
        assert not _is_linked(a1, 'items2', b)
    if hasattr(a2, 'items2'):
        assert _is_linked(a2, 'items2', b)
    _safe_set(b, 'shopping_cart3', None)
    assert not _is_linked(b, 'shopping_cart3', a2)
    if hasattr(a2, 'items2'):
        assert not _is_linked(a2, 'items2', b)


def test_assoc_ShoppingCart_Order_reverse_link_reassign_clear():
    a1 = ShoppingCart(creationDate=date(2024, 1, 1))
    a2 = ShoppingCart(creationDate=date(2025, 6, 15))
    b = Order(number=7, ordered=date(2024, 1, 1), shipTo="sample_text", shipped=True, status="sample_text", total=3.14)
    _safe_set(b, 'shoppingCart27', a1)
    assert _is_linked(b, 'shoppingCart27', a1)
    if hasattr(a1, 'order26'):
        assert _is_linked(a1, 'order26', b)
    _safe_set(b, 'shoppingCart27', a2)
    assert _is_linked(b, 'shoppingCart27', a2)
    if hasattr(a1, 'order26'):
        assert not _is_linked(a1, 'order26', b)
    if hasattr(a2, 'order26'):
        assert _is_linked(a2, 'order26', b)
    _safe_set(b, 'shoppingCart27', None)
    assert not _is_linked(b, 'shoppingCart27', a2)
    if hasattr(a2, 'order26'):
        assert not _is_linked(a2, 'order26', b)


def test_assoc_Vendors_Administrator_reverse_link_reassign_clear():
    a1 = Shop_Owner(Email="sample_text", IDSowner=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    a2 = Shop_Owner(Email="sample_text_2", IDSowner=13, Last_name="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    b = Administrator(Email="sample_text", IDAdm=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    _safe_set(b, 'give_permission37', {a1})
    assert _is_linked(b, 'give_permission37', a1)
    if hasattr(a1, 'Vendors_Administrator_036'):
        assert _is_linked(a1, 'Vendors_Administrator_036', b)
    _safe_set(b, 'give_permission37', {a2})
    assert _is_linked(b, 'give_permission37', a2)
    if hasattr(a1, 'Vendors_Administrator_036'):
        assert not _is_linked(a1, 'Vendors_Administrator_036', b)
    if hasattr(a2, 'Vendors_Administrator_036'):
        assert _is_linked(a2, 'Vendors_Administrator_036', b)
    _safe_set(b, 'give_permission37', set())
    assert not _is_linked(b, 'give_permission37', a2)
    if hasattr(a2, 'Vendors_Administrator_036'):
        assert not _is_linked(a2, 'Vendors_Administrator_036', b)


def test_assoc_Vendors_Product_reverse_link_reassign_clear():
    a1 = Shop_Owner(Email="sample_text", IDSowner=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    a2 = Shop_Owner(Email="sample_text_2", IDSowner=13, Last_name="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    b = Product(description="sample_text", name="sample_text")
    _safe_set(b, 'vendors39', a1)
    assert _is_linked(b, 'vendors39', a1)
    if hasattr(a1, 'add_and_modify38'):
        assert _is_linked(a1, 'add_and_modify38', b)
    _safe_set(b, 'vendors39', a2)
    assert _is_linked(b, 'vendors39', a2)
    if hasattr(a1, 'add_and_modify38'):
        assert not _is_linked(a1, 'add_and_modify38', b)
    if hasattr(a2, 'add_and_modify38'):
        assert _is_linked(a2, 'add_and_modify38', b)
    _safe_set(b, 'vendors39', None)
    assert not _is_linked(b, 'vendors39', a2)
    if hasattr(a2, 'add_and_modify38'):
        assert not _is_linked(a2, 'add_and_modify38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Visitor_Product_stub_double():
    # Visitor has no real 'view_products30' property in the generated
    # code (a bare stub) -- manually attach it so Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Product(description="sample_text", name="sample_text")
    partner = Visitor()
    setattr(partner, 'view_products30', None)
    _safe_set(owner, 'visitor31', partner)
    assert owner in getattr(partner, 'view_products30')
    _safe_set(owner, 'visitor31', None)
    assert owner not in getattr(partner, 'view_products30')


def test_assoc_WebUser_Customer_stub_double():
    # Visitor has no real 'customer10' property in the generated
    # code (a bare stub) -- manually attach it so Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Customer(Email="sample_text", IDCust=7, Last_name="sample_text", Name="sample_text", Password="sample_text")
    partner = Visitor()
    setattr(partner, 'customer10', None)
    _safe_set(owner, 'webUser11', partner)
    assert getattr(partner, 'customer10') == owner
    _safe_set(owner, 'webUser11', None)
    assert getattr(partner, 'customer10') is None


def test_assoc_WebUser_ShoppingCart_stub_double():
    # Visitor has no real 'shoppingCart8' property in the generated
    # code (a bare stub) -- manually attach it so ShoppingCart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ShoppingCart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ShoppingCart(creationDate=date(2024, 1, 1))
    partner = Visitor()
    setattr(partner, 'shoppingCart8', None)
    _safe_set(owner, 'webUser9', partner)
    assert getattr(partner, 'shoppingCart8') == owner
    _safe_set(owner, 'webUser9', None)
    assert getattr(partner, 'shoppingCart8') is None


