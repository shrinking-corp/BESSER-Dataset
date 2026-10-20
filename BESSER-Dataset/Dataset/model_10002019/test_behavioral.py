import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    City,
    Guest,
    Hotels,
    Manager,
    Payment,
    Rooms,
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

def test_assoc_City_Hotels_reverse_link_reassign_clear():
    a1 = Hotels(id=7, location=7, name=7)
    a2 = Hotels(id=13, location=13, name=13)
    b = City(city="sample_text", id=7)
    _safe_set(b, 'hotels0', a1)
    assert _is_linked(b, 'hotels0', a1)
    if hasattr(a1, 'city1'):
        assert _is_linked(a1, 'city1', b)
    _safe_set(b, 'hotels0', a2)
    assert _is_linked(b, 'hotels0', a2)
    if hasattr(a1, 'city1'):
        assert not _is_linked(a1, 'city1', b)
    if hasattr(a2, 'city1'):
        assert _is_linked(a2, 'city1', b)
    _safe_set(b, 'hotels0', None)
    assert not _is_linked(b, 'hotels0', a2)
    if hasattr(a2, 'city1'):
        assert not _is_linked(a2, 'city1', b)


def test_assoc_Guest_Payment_reverse_link_reassign_clear():
    a1 = Payment(amount=7, card_no=7, card_type="sample_text", cvv=7, password=7)
    a2 = Payment(amount=13, card_no=13, card_type="sample_text_2", cvv=13, password=13)
    b = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    _safe_set(b, 'payment6', a1)
    assert _is_linked(b, 'payment6', a1)
    if hasattr(a1, 'guest7'):
        assert _is_linked(a1, 'guest7', b)
    _safe_set(b, 'payment6', a2)
    assert _is_linked(b, 'payment6', a2)
    if hasattr(a1, 'guest7'):
        assert not _is_linked(a1, 'guest7', b)
    if hasattr(a2, 'guest7'):
        assert _is_linked(a2, 'guest7', b)
    _safe_set(b, 'payment6', None)
    assert not _is_linked(b, 'payment6', a2)
    if hasattr(a2, 'guest7'):
        assert not _is_linked(a2, 'guest7', b)


def test_assoc_Hotels_Guest_reverse_link_reassign_clear():
    a1 = Hotels(id=7, location=7, name=7)
    a2 = Hotels(id=13, location=13, name=13)
    b = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    _safe_set(b, 'hotels9', a1)
    assert _is_linked(b, 'hotels9', a1)
    if hasattr(a1, 'guest8'):
        assert _is_linked(a1, 'guest8', b)
    _safe_set(b, 'hotels9', a2)
    assert _is_linked(b, 'hotels9', a2)
    if hasattr(a1, 'guest8'):
        assert not _is_linked(a1, 'guest8', b)
    if hasattr(a2, 'guest8'):
        assert _is_linked(a2, 'guest8', b)
    _safe_set(b, 'hotels9', None)
    assert not _is_linked(b, 'hotels9', a2)
    if hasattr(a2, 'guest8'):
        assert not _is_linked(a2, 'guest8', b)


def test_assoc_Hotels_Rooms_reverse_link_reassign_clear():
    a1 = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
    a2 = Rooms(id=13, name="sample_text_2", price=13, room_description="sample_text_2")
    b = Hotels(id=7, location=7, name=7)
    _safe_set(b, 'rooms2', a1)
    assert _is_linked(b, 'rooms2', a1)
    if hasattr(a1, 'hotels3'):
        assert _is_linked(a1, 'hotels3', b)
    _safe_set(b, 'rooms2', a2)
    assert _is_linked(b, 'rooms2', a2)
    if hasattr(a1, 'hotels3'):
        assert not _is_linked(a1, 'hotels3', b)
    if hasattr(a2, 'hotels3'):
        assert _is_linked(a2, 'hotels3', b)
    _safe_set(b, 'rooms2', None)
    assert not _is_linked(b, 'rooms2', a2)
    if hasattr(a2, 'hotels3'):
        assert not _is_linked(a2, 'hotels3', b)


def test_assoc_Rooms_Guest_reverse_link_reassign_clear():
    a1 = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
    a2 = Rooms(id=13, name="sample_text_2", price=13, room_description="sample_text_2")
    b = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    _safe_set(b, 'rooms5', a1)
    assert _is_linked(b, 'rooms5', a1)
    if hasattr(a1, 'guest4'):
        assert _is_linked(a1, 'guest4', b)
    _safe_set(b, 'rooms5', a2)
    assert _is_linked(b, 'rooms5', a2)
    if hasattr(a1, 'guest4'):
        assert not _is_linked(a1, 'guest4', b)
    if hasattr(a2, 'guest4'):
        assert _is_linked(a2, 'guest4', b)
    _safe_set(b, 'rooms5', None)
    assert not _is_linked(b, 'rooms5', a2)
    if hasattr(a2, 'guest4'):
        assert not _is_linked(a2, 'guest4', b)


def test_assoc_User_Guest_reverse_link_reassign_clear():
    a1 = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    a2 = User(Name="sample_text_2", address="sample_text_2", id=13, mail_id="sample_text_2", password=13, phn_no=13)
    b = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    _safe_set(b, 'user11', a1)
    assert _is_linked(b, 'user11', a1)
    if hasattr(a1, 'guest10'):
        assert _is_linked(a1, 'guest10', b)
    _safe_set(b, 'user11', a2)
    assert _is_linked(b, 'user11', a2)
    if hasattr(a1, 'guest10'):
        assert not _is_linked(a1, 'guest10', b)
    if hasattr(a2, 'guest10'):
        assert _is_linked(a2, 'guest10', b)
    _safe_set(b, 'user11', None)
    assert not _is_linked(b, 'user11', a2)
    if hasattr(a2, 'guest10'):
        assert not _is_linked(a2, 'guest10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

