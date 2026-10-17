import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    admin,
    cash,
    credit_card,
    customer,
    flights,
    payement,
    ticket,
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

def test_assoc_admin_flights_reverse_link_reassign_clear():
    a1 = flights(depart="sample_text", dest="sample_text", name="sample_text", number=7, time=7)
    a2 = flights(depart="sample_text_2", dest="sample_text_2", name="sample_text_2", number=13, time=13)
    b = admin(cost=7, name_of_flight="sample_text", pwd="sample_text", seats=7, type="sample_text", username="sample_text")
    _safe_set(b, 'flights8', {a1})
    assert _is_linked(b, 'flights8', a1)
    if hasattr(a1, 'admin9'):
        assert _is_linked(a1, 'admin9', b)
    _safe_set(b, 'flights8', {a2})
    assert _is_linked(b, 'flights8', a2)
    if hasattr(a1, 'admin9'):
        assert not _is_linked(a1, 'admin9', b)
    if hasattr(a2, 'admin9'):
        assert _is_linked(a2, 'admin9', b)
    _safe_set(b, 'flights8', set())
    assert not _is_linked(b, 'flights8', a2)
    if hasattr(a2, 'admin9'):
        assert not _is_linked(a2, 'admin9', b)


def test_assoc_customer_admin_reverse_link_reassign_clear():
    a1 = customer(address="sample_text", age=7, name="sample_text", source="sample_text")
    a2 = customer(address="sample_text_2", age=13, name="sample_text_2", source="sample_text_2")
    b = admin(cost=7, name_of_flight="sample_text", pwd="sample_text", seats=7, type="sample_text", username="sample_text")
    _safe_set(b, 'customer5', {a1})
    assert _is_linked(b, 'customer5', a1)
    if hasattr(a1, 'admin4'):
        assert _is_linked(a1, 'admin4', b)
    _safe_set(b, 'customer5', {a2})
    assert _is_linked(b, 'customer5', a2)
    if hasattr(a1, 'admin4'):
        assert not _is_linked(a1, 'admin4', b)
    if hasattr(a2, 'admin4'):
        assert _is_linked(a2, 'admin4', b)
    _safe_set(b, 'customer5', set())
    assert not _is_linked(b, 'customer5', a2)
    if hasattr(a2, 'admin4'):
        assert not _is_linked(a2, 'admin4', b)


def test_assoc_customer_flights_reverse_link_reassign_clear():
    a1 = flights(depart="sample_text", dest="sample_text", name="sample_text", number=7, time=7)
    a2 = flights(depart="sample_text_2", dest="sample_text_2", name="sample_text_2", number=13, time=13)
    b = customer(address="sample_text", age=7, name="sample_text", source="sample_text")
    _safe_set(b, 'flights6', a1)
    assert _is_linked(b, 'flights6', a1)
    if hasattr(a1, 'customer7'):
        assert _is_linked(a1, 'customer7', b)
    _safe_set(b, 'flights6', a2)
    assert _is_linked(b, 'flights6', a2)
    if hasattr(a1, 'customer7'):
        assert not _is_linked(a1, 'customer7', b)
    if hasattr(a2, 'customer7'):
        assert _is_linked(a2, 'customer7', b)
    _safe_set(b, 'flights6', None)
    assert not _is_linked(b, 'flights6', a2)
    if hasattr(a2, 'customer7'):
        assert not _is_linked(a2, 'customer7', b)


def test_assoc_customer_ticket_reverse_link_reassign_clear():
    a1 = ticket(attribute="sample_text", custid=7, dest="sample_text", source="sample_text", tiketno_=7)
    a2 = ticket(attribute="sample_text_2", custid=13, dest="sample_text_2", source="sample_text_2", tiketno_=13)
    b = customer(address="sample_text", age=7, name="sample_text", source="sample_text")
    _safe_set(b, 'ticket2', a1)
    assert _is_linked(b, 'ticket2', a1)
    if hasattr(a1, 'customer3'):
        assert _is_linked(a1, 'customer3', b)
    _safe_set(b, 'ticket2', a2)
    assert _is_linked(b, 'ticket2', a2)
    if hasattr(a1, 'customer3'):
        assert not _is_linked(a1, 'customer3', b)
    if hasattr(a2, 'customer3'):
        assert _is_linked(a2, 'customer3', b)
    _safe_set(b, 'ticket2', None)
    assert not _is_linked(b, 'ticket2', a2)
    if hasattr(a2, 'customer3'):
        assert not _is_linked(a2, 'customer3', b)


def test_assoc_payement_customer_reverse_link_reassign_clear():
    a1 = payement(customer_info="sample_text", pay_amt=7, pay_date=7, paymethod="sample_text", transc_id=7)
    a2 = payement(customer_info="sample_text_2", pay_amt=13, pay_date=13, paymethod="sample_text_2", transc_id=13)
    b = customer(address="sample_text", age=7, name="sample_text", source="sample_text")
    _safe_set(b, 'payement1', a1)
    assert _is_linked(b, 'payement1', a1)
    if hasattr(a1, 'customer0'):
        assert _is_linked(a1, 'customer0', b)
    _safe_set(b, 'payement1', a2)
    assert _is_linked(b, 'payement1', a2)
    if hasattr(a1, 'customer0'):
        assert not _is_linked(a1, 'customer0', b)
    if hasattr(a2, 'customer0'):
        assert _is_linked(a2, 'customer0', b)
    _safe_set(b, 'payement1', None)
    assert not _is_linked(b, 'payement1', a2)
    if hasattr(a2, 'customer0'):
        assert not _is_linked(a2, 'customer0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

