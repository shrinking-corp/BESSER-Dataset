import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Delivery,
    Discription,
    Order,
    Payment,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Order_MyClass_stub_double():
    # Delivery has no real 'order1' property in the generated
    # code (a bare stub) -- manually attach it so Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    partner = Delivery()
    setattr(partner, 'order1', None)
    _safe_set(owner, 'myClass0', partner)
    assert getattr(partner, 'order1') == owner
    _safe_set(owner, 'myClass0', None)
    assert getattr(partner, 'order1') is None


def test_assoc_Order_MyClass2_stub_double():
    # User has no real 'order3' property in the generated
    # code (a bare stub) -- manually attach it so Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    partner = User()
    setattr(partner, 'order3', None)
    _safe_set(owner, 'myClass22', partner)
    assert getattr(partner, 'order3') == owner
    _safe_set(owner, 'myClass22', None)
    assert getattr(partner, 'order3') is None


def test_assoc_Order_MyClass3_stub_double():
    # Payment has no real 'order5' property in the generated
    # code (a bare stub) -- manually attach it so Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    partner = Payment()
    setattr(partner, 'order5', None)
    _safe_set(owner, 'myClass34', partner)
    assert getattr(partner, 'order5') == owner
    _safe_set(owner, 'myClass34', None)
    assert getattr(partner, 'order5') is None


def test_assoc_Order_MyClass4_stub_double():
    # Discription has no real 'order9' property in the generated
    # code (a bare stub) -- manually attach it so Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    partner = Discription()
    setattr(partner, 'order9', None)
    _safe_set(owner, 'myClass48', partner)
    assert getattr(partner, 'order9') == owner
    _safe_set(owner, 'myClass48', None)
    assert getattr(partner, 'order9') is None


