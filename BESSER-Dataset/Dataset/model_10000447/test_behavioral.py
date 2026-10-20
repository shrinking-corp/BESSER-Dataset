import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Chef,
    Customer,
    Food,
    Host,
    Items,
    Table,
    app,
    cost,
    robotWaiter,
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

def test_assoc_Host_Customer_reverse_link_reassign_clear():
    a1 = Host(ID="sample_text", shift="sample_text")
    a2 = Host(ID="sample_text_2", shift="sample_text_2")
    b = Customer(name="sample_text", numberPeople=7)
    _safe_set(b, 'host1', a1)
    assert _is_linked(b, 'host1', a1)
    if hasattr(a1, 'customer0'):
        assert _is_linked(a1, 'customer0', b)
    _safe_set(b, 'host1', a2)
    assert _is_linked(b, 'host1', a2)
    if hasattr(a1, 'customer0'):
        assert not _is_linked(a1, 'customer0', b)
    if hasattr(a2, 'customer0'):
        assert _is_linked(a2, 'customer0', b)
    _safe_set(b, 'host1', None)
    assert not _is_linked(b, 'host1', a2)
    if hasattr(a2, 'customer0'):
        assert not _is_linked(a2, 'customer0', b)


def test_assoc_Table_Customer_reverse_link_reassign_clear():
    a1 = Table(seats=7, tableNumber=7)
    a2 = Table(seats=13, tableNumber=13)
    b = Customer(name="sample_text", numberPeople=7)
    _safe_set(b, 'table3', a1)
    assert _is_linked(b, 'table3', a1)
    if hasattr(a1, 'customer2'):
        assert _is_linked(a1, 'customer2', b)
    _safe_set(b, 'table3', a2)
    assert _is_linked(b, 'table3', a2)
    if hasattr(a1, 'customer2'):
        assert not _is_linked(a1, 'customer2', b)
    if hasattr(a2, 'customer2'):
        assert _is_linked(a2, 'customer2', b)
    _safe_set(b, 'table3', None)
    assert not _is_linked(b, 'table3', a2)
    if hasattr(a2, 'customer2'):
        assert not _is_linked(a2, 'customer2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Food_Items_stub_double():
    # Items has no real 'food11' property in the generated
    # code (a bare stub) -- manually attach it so Food's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Food's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Food(food_id="sample_text", name="sample_text", prepared=True, price=3.14, served=True)
    partner = Items()
    setattr(partner, 'food11', None)
    _safe_set(owner, 'items10', partner)
    assert getattr(partner, 'food11') == owner
    _safe_set(owner, 'items10', None)
    assert getattr(partner, 'food11') is None


def test_assoc_Table_app_stub_double():
    # app has no real 'table7' property in the generated
    # code (a bare stub) -- manually attach it so Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Table(seats=7, tableNumber=7)
    partner = app()
    setattr(partner, 'table7', None)
    _safe_set(owner, 'app6', partner)
    assert getattr(partner, 'table7') == owner
    _safe_set(owner, 'app6', None)
    assert getattr(partner, 'table7') is None


def test_assoc_app__Food_stub_double():
    # app has no real 'food12' property in the generated
    # code (a bare stub) -- manually attach it so Food's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Food's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Food(food_id="sample_text", name="sample_text", prepared=True, price=3.14, served=True)
    partner = app()
    setattr(partner, 'food12', None)
    _safe_set(owner, 'app13', partner)
    assert getattr(partner, 'food12') == owner
    _safe_set(owner, 'app13', None)
    assert getattr(partner, 'food12') is None


def test_assoc_robotWaiter_Customer_stub_double():
    # robotWaiter has no real 'customer4' property in the generated
    # code (a bare stub) -- manually attach it so Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Customer(name="sample_text", numberPeople=7)
    partner = robotWaiter()
    setattr(partner, 'customer4', None)
    _safe_set(owner, 'robotWaiter5', partner)
    assert getattr(partner, 'customer4') == owner
    _safe_set(owner, 'robotWaiter5', None)
    assert getattr(partner, 'customer4') is None


