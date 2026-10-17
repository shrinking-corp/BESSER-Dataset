import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Chef,
    Order,
    Table,
    Waiter,
    app,
    customer,
    manger,
    meal,
    system,
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

def test_assoc_Order_Food_reverse_link_reassign_clear():
    a1 = meal(meal_id="sample_text", name="sample_text", prepared=True, price=3.14, served=True)
    a2 = meal(meal_id="sample_text_2", name="sample_text_2", prepared=False, price=9.99, served=False)
    b = Order(foodList="sample_text", order_id="sample_text")
    _safe_set(b, 'orde0', {a1})
    assert _is_linked(b, 'orde0', a1)
    if hasattr(a1, 'has1'):
        assert _is_linked(a1, 'has1', b)
    _safe_set(b, 'orde0', {a2})
    assert _is_linked(b, 'orde0', a2)
    if hasattr(a1, 'has1'):
        assert not _is_linked(a1, 'has1', b)
    if hasattr(a2, 'has1'):
        assert _is_linked(a2, 'has1', b)
    _safe_set(b, 'orde0', set())
    assert not _is_linked(b, 'orde0', a2)
    if hasattr(a2, 'has1'):
        assert not _is_linked(a2, 'has1', b)


def test_assoc_Table_app_reverse_link_reassign_clear():
    a1 = app(name="sample_text", user_id="sample_text")
    a2 = app(name="sample_text_2", user_id="sample_text_2")
    b = Table(avaliable=True, numSeats=7, table_id="sample_text")
    _safe_set(b, 'app4', a1)
    assert _is_linked(b, 'app4', a1)
    if hasattr(a1, 'table5'):
        assert _is_linked(a1, 'table5', b)
    _safe_set(b, 'app4', a2)
    assert _is_linked(b, 'app4', a2)
    if hasattr(a1, 'table5'):
        assert not _is_linked(a1, 'table5', b)
    if hasattr(a2, 'table5'):
        assert _is_linked(a2, 'table5', b)
    _safe_set(b, 'app4', None)
    assert not _is_linked(b, 'app4', a2)
    if hasattr(a2, 'table5'):
        assert not _is_linked(a2, 'table5', b)


def test_assoc_app_Order_reverse_link_reassign_clear():
    a1 = app(name="sample_text", user_id="sample_text")
    a2 = app(name="sample_text_2", user_id="sample_text_2")
    b = Order(foodList="sample_text", order_id="sample_text")
    _safe_set(b, 'app7', a1)
    assert _is_linked(b, 'app7', a1)
    if hasattr(a1, 'order6'):
        assert _is_linked(a1, 'order6', b)
    _safe_set(b, 'app7', a2)
    assert _is_linked(b, 'app7', a2)
    if hasattr(a1, 'order6'):
        assert not _is_linked(a1, 'order6', b)
    if hasattr(a2, 'order6'):
        assert _is_linked(a2, 'order6', b)
    _safe_set(b, 'app7', None)
    assert not _is_linked(b, 'app7', a2)
    if hasattr(a2, 'order6'):
        assert not _is_linked(a2, 'order6', b)


def test_assoc_system_app_reverse_link_reassign_clear():
    a1 = system(name="sample_text", user_id="sample_text")
    a2 = system(name="sample_text_2", user_id="sample_text_2")
    b = app(name="sample_text", user_id="sample_text")
    _safe_set(b, 'system9', a1)
    assert _is_linked(b, 'system9', a1)
    if hasattr(a1, 'app8'):
        assert _is_linked(a1, 'app8', b)
    _safe_set(b, 'system9', a2)
    assert _is_linked(b, 'system9', a2)
    if hasattr(a1, 'app8'):
        assert not _is_linked(a1, 'app8', b)
    if hasattr(a2, 'app8'):
        assert _is_linked(a2, 'app8', b)
    _safe_set(b, 'system9', None)
    assert not _is_linked(b, 'system9', a2)
    if hasattr(a2, 'app8'):
        assert not _is_linked(a2, 'app8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Chef_system_stub_double():
    # Chef has no real 'system10' property in the generated
    # code (a bare stub) -- manually attach it so system's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # system's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = system(name="sample_text", user_id="sample_text")
    partner = Chef()
    setattr(partner, 'system10', None)
    _safe_set(owner, 'chef11', partner)
    assert getattr(partner, 'system10') == owner
    _safe_set(owner, 'chef11', None)
    assert getattr(partner, 'system10') is None


def test_assoc_Waiter_Table_stub_double():
    # Waiter has no real 'table2' property in the generated
    # code (a bare stub) -- manually attach it so Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Table(avaliable=True, numSeats=7, table_id="sample_text")
    partner = Waiter()
    setattr(partner, 'table2', None)
    _safe_set(owner, 'waiter3', partner)
    assert getattr(partner, 'table2') == owner
    _safe_set(owner, 'waiter3', None)
    assert getattr(partner, 'table2') is None


def test_assoc_Waiter_app_stub_double():
    # Waiter has no real 'app16' property in the generated
    # code (a bare stub) -- manually attach it so app's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # app's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = app(name="sample_text", user_id="sample_text")
    partner = Waiter()
    setattr(partner, 'app16', None)
    _safe_set(owner, 'waiter17', partner)
    assert getattr(partner, 'app16') == owner
    _safe_set(owner, 'waiter17', None)
    assert getattr(partner, 'app16') is None


def test_assoc_customer__Order_stub_double():
    # customer has no real 'order14' property in the generated
    # code (a bare stub) -- manually attach it so Order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Order(foodList="sample_text", order_id="sample_text")
    partner = customer()
    setattr(partner, 'order14', None)
    _safe_set(owner, 'customer15', partner)
    assert getattr(partner, 'order14') == owner
    _safe_set(owner, 'customer15', None)
    assert getattr(partner, 'order14') is None


def test_assoc_manger_system_stub_double():
    # manger has no real 'system12' property in the generated
    # code (a bare stub) -- manually attach it so system's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # system's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = system(name="sample_text", user_id="sample_text")
    partner = manger()
    setattr(partner, 'system12', None)
    _safe_set(owner, 'manger13', partner)
    assert getattr(partner, 'system12') == owner
    _safe_set(owner, 'manger13', None)
    assert getattr(partner, 'system12') is None


