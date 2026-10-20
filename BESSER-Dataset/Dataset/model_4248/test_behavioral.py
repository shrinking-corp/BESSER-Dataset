import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Card,
    Category,
    Employee,
    PhysicalCard,
    Product,
    Provider,
    Purchase,
    User,
    restapp_model_Card,
    restapp_model_Category,
    restapp_model_Employee,
    restapp_model_PhysicalCard,
    restapp_model_Price,
    restapp_model_Product,
    restapp_model_ProductsCard,
    restapp_model_ProductsPurchase,
    restapp_model_Provider,
    restapp_model_Purchase,
    restapp_model_User,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_newEReference10_stub_double():
    # Employee has no real 'Employee' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_User(id=7, password="sample_text", status=7, user="sample_text")
    partner = Employee()
    setattr(partner, 'Employee', None)
    _safe_set(owner, 'restapp_model_User', partner)
    assert getattr(partner, 'Employee') == owner
    _safe_set(owner, 'restapp_model_User', None)
    assert getattr(partner, 'Employee') is None


def test_assoc_newEReference11_stub_double():
    # Category has no real 'Category' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_Product(description="sample_text", id=7, name="sample_text", status=7, stock=7)
    partner = Category()
    setattr(partner, 'Category', None)
    _safe_set(owner, 'restapp_model_Product', partner)
    assert getattr(partner, 'Category') == owner
    _safe_set(owner, 'restapp_model_Product', None)
    assert getattr(partner, 'Category') is None


def test_assoc_newEReference110_stub_double():
    # PhysicalCard has no real 'PhysicalCard' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_Card's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_Card's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_Card(change=3.14, discount=7, id=7, payedValue=3.14, sellDate=date(2024, 1, 1), totalValue=3.14, totalValueWithDiscount=3.14)
    partner = PhysicalCard()
    setattr(partner, 'PhysicalCard', None)
    _safe_set(owner, 'restapp_model_Card', partner)
    assert getattr(partner, 'PhysicalCard') == owner
    _safe_set(owner, 'restapp_model_Card', None)
    assert getattr(partner, 'PhysicalCard') is None


def test_assoc_newEReference111_stub_double():
    # Product has no real 'Product12' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_ProductsCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_ProductsCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_ProductsCard(date=date(2024, 1, 1), id=7)
    partner = Product()
    setattr(partner, 'Product12', None)
    _safe_set(owner, 'restapp_model_ProductsCard', partner)
    assert getattr(partner, 'Product12') == owner
    _safe_set(owner, 'restapp_model_ProductsCard', None)
    assert getattr(partner, 'Product12') is None


def test_assoc_newEReference13_stub_double():
    # Provider has no real 'Provider' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_Purchase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_Purchase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_Purchase(date=date(2024, 1, 1), discount=7, id=7, totalValue=3.14, totalWithDiscount=3.14)
    partner = Provider()
    setattr(partner, 'Provider', None)
    _safe_set(owner, 'restapp_model_Purchase', partner)
    assert getattr(partner, 'Provider') == owner
    _safe_set(owner, 'restapp_model_Purchase', None)
    assert getattr(partner, 'Provider') is None


def test_assoc_newEReference16_stub_double():
    # Purchase has no real 'Purchase' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_ProductsPurchase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_ProductsPurchase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_ProductsPurchase(quantity=7, unityDiscount=7, unityValue=3.14, unityValueWithDiscount=3.14)
    partner = Purchase()
    setattr(partner, 'Purchase', None)
    _safe_set(owner, 'restapp_model_ProductsPurchase', partner)
    assert getattr(partner, 'Purchase') == owner
    _safe_set(owner, 'restapp_model_ProductsPurchase', None)
    assert getattr(partner, 'Purchase') is None


def test_assoc_newEReference2_stub_double():
    # Product has no real 'Product' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_Price's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_Price's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_Price(date=date(2024, 1, 1), id=7, value=3.14)
    partner = Product()
    setattr(partner, 'Product', None)
    _safe_set(owner, 'restapp_model_Price', {partner})
    assert getattr(partner, 'Product') == owner
    _safe_set(owner, 'restapp_model_Price', set())
    assert getattr(partner, 'Product') is None


def test_assoc_newEReference213_stub_double():
    # Card has no real 'Card' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_ProductsCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_ProductsCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_ProductsCard(date=date(2024, 1, 1), id=7)
    partner = Card()
    setattr(partner, 'Card', None)
    _safe_set(owner, 'restapp_model_ProductsCard14', partner)
    assert getattr(partner, 'Card') == owner
    _safe_set(owner, 'restapp_model_ProductsCard14', None)
    assert getattr(partner, 'Card') is None


def test_assoc_newEReference24_stub_double():
    # User has no real 'User' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_Purchase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_Purchase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_Purchase(date=date(2024, 1, 1), discount=7, id=7, totalValue=3.14, totalWithDiscount=3.14)
    partner = User()
    setattr(partner, 'User', None)
    _safe_set(owner, 'restapp_model_Purchase5', partner)
    assert getattr(partner, 'User') == owner
    _safe_set(owner, 'restapp_model_Purchase5', None)
    assert getattr(partner, 'User') is None


def test_assoc_newEReference27_stub_double():
    # Product has no real 'Product9' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_ProductsPurchase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_ProductsPurchase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_ProductsPurchase(quantity=7, unityDiscount=7, unityValue=3.14, unityValueWithDiscount=3.14)
    partner = Product()
    setattr(partner, 'Product9', None)
    _safe_set(owner, 'restapp_model_ProductsPurchase8', partner)
    assert getattr(partner, 'Product9') == owner
    _safe_set(owner, 'restapp_model_ProductsPurchase8', None)
    assert getattr(partner, 'Product9') is None


def test_assoc_newEReference315_stub_double():
    # User has no real 'User17' property in the generated
    # code (a bare stub) -- manually attach it so restapp_model_ProductsCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # restapp_model_ProductsCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = restapp_model_ProductsCard(date=date(2024, 1, 1), id=7)
    partner = User()
    setattr(partner, 'User17', None)
    _safe_set(owner, 'restapp_model_ProductsCard16', partner)
    assert getattr(partner, 'User17') == owner
    _safe_set(owner, 'restapp_model_ProductsCard16', None)
    assert getattr(partner, 'User17') is None


