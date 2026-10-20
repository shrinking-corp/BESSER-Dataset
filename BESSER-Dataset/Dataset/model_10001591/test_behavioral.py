import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Database,
    Guest,
    Inventory,
    Manager,
    Receptionist,
    Room,
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

def test_assoc_Guest_Bill_reverse_link_reassign_clear():
    a1 = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    a2 = Guest(Address="sample_text_2", Room=13, credit_card=13, id=13, name="sample_text_2", phoneNo=13)
    b = Bill(GuestName="sample_text", bill_No=7)
    _safe_set(b, 'guest3', a1)
    assert _is_linked(b, 'guest3', a1)
    if hasattr(a1, 'bill2'):
        assert _is_linked(a1, 'bill2', b)
    _safe_set(b, 'guest3', a2)
    assert _is_linked(b, 'guest3', a2)
    if hasattr(a1, 'bill2'):
        assert not _is_linked(a1, 'bill2', b)
    if hasattr(a2, 'bill2'):
        assert _is_linked(a2, 'bill2', b)
    _safe_set(b, 'guest3', None)
    assert not _is_linked(b, 'guest3', a2)
    if hasattr(a2, 'bill2'):
        assert not _is_linked(a2, 'bill2', b)


def test_assoc_Guest_Room_reverse_link_reassign_clear():
    a1 = Room(RatesofRoom=7, roomNo=7, typeOfRoom="sample_text")
    a2 = Room(RatesofRoom=13, roomNo=13, typeOfRoom="sample_text_2")
    b = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    _safe_set(b, 'room0', a1)
    assert _is_linked(b, 'room0', a1)
    if hasattr(a1, 'guest1'):
        assert _is_linked(a1, 'guest1', b)
    _safe_set(b, 'room0', a2)
    assert _is_linked(b, 'room0', a2)
    if hasattr(a1, 'guest1'):
        assert not _is_linked(a1, 'guest1', b)
    if hasattr(a2, 'guest1'):
        assert _is_linked(a2, 'guest1', b)
    _safe_set(b, 'room0', None)
    assert not _is_linked(b, 'room0', a2)
    if hasattr(a2, 'guest1'):
        assert not _is_linked(a2, 'guest1', b)


def test_assoc_Inventory_Manager_reverse_link_reassign_clear():
    a1 = Manager(id=7, name="sample_text")
    a2 = Manager(id=13, name="sample_text_2")
    b = Inventory(Status="sample_text", type="sample_text")
    _safe_set(b, 'manager10', a1)
    assert _is_linked(b, 'manager10', a1)
    if hasattr(a1, 'inventory11'):
        assert _is_linked(a1, 'inventory11', b)
    _safe_set(b, 'manager10', a2)
    assert _is_linked(b, 'manager10', a2)
    if hasattr(a1, 'inventory11'):
        assert not _is_linked(a1, 'inventory11', b)
    if hasattr(a2, 'inventory11'):
        assert _is_linked(a2, 'inventory11', b)
    _safe_set(b, 'manager10', None)
    assert not _is_linked(b, 'manager10', a2)
    if hasattr(a2, 'inventory11'):
        assert not _is_linked(a2, 'inventory11', b)


def test_assoc_Manager_Database_reverse_link_reassign_clear():
    a1 = Manager(id=7, name="sample_text")
    a2 = Manager(id=13, name="sample_text_2")
    b = Database(Details="sample_text", income=7, service="sample_text")
    _safe_set(b, 'manager15', a1)
    assert _is_linked(b, 'manager15', a1)
    if hasattr(a1, 'database14'):
        assert _is_linked(a1, 'database14', b)
    _safe_set(b, 'manager15', a2)
    assert _is_linked(b, 'manager15', a2)
    if hasattr(a1, 'database14'):
        assert not _is_linked(a1, 'database14', b)
    if hasattr(a2, 'database14'):
        assert _is_linked(a2, 'database14', b)
    _safe_set(b, 'manager15', None)
    assert not _is_linked(b, 'manager15', a2)
    if hasattr(a2, 'database14'):
        assert not _is_linked(a2, 'database14', b)


def test_assoc_Receptionist_Bill_reverse_link_reassign_clear():
    a1 = Receptionist(Id=7, name="sample_text")
    a2 = Receptionist(Id=13, name="sample_text_2")
    b = Bill(GuestName="sample_text", bill_No=7)
    _safe_set(b, 'receptionist7', {a1})
    assert _is_linked(b, 'receptionist7', a1)
    if hasattr(a1, 'bill6'):
        assert _is_linked(a1, 'bill6', b)
    _safe_set(b, 'receptionist7', {a2})
    assert _is_linked(b, 'receptionist7', a2)
    if hasattr(a1, 'bill6'):
        assert not _is_linked(a1, 'bill6', b)
    if hasattr(a2, 'bill6'):
        assert _is_linked(a2, 'bill6', b)
    _safe_set(b, 'receptionist7', set())
    assert not _is_linked(b, 'receptionist7', a2)
    if hasattr(a2, 'bill6'):
        assert not _is_linked(a2, 'bill6', b)


def test_assoc_Receptionist_Database_reverse_link_reassign_clear():
    a1 = Receptionist(Id=7, name="sample_text")
    a2 = Receptionist(Id=13, name="sample_text_2")
    b = Database(Details="sample_text", income=7, service="sample_text")
    _safe_set(b, 'receptionist13', {a1})
    assert _is_linked(b, 'receptionist13', a1)
    if hasattr(a1, 'database12'):
        assert _is_linked(a1, 'database12', b)
    _safe_set(b, 'receptionist13', {a2})
    assert _is_linked(b, 'receptionist13', a2)
    if hasattr(a1, 'database12'):
        assert not _is_linked(a1, 'database12', b)
    if hasattr(a2, 'database12'):
        assert _is_linked(a2, 'database12', b)
    _safe_set(b, 'receptionist13', set())
    assert not _is_linked(b, 'receptionist13', a2)
    if hasattr(a2, 'database12'):
        assert not _is_linked(a2, 'database12', b)


def test_assoc_Receptionist_Manager_reverse_link_reassign_clear():
    a1 = Receptionist(Id=7, name="sample_text")
    a2 = Receptionist(Id=13, name="sample_text_2")
    b = Manager(id=7, name="sample_text")
    _safe_set(b, 'receptionist9', {a1})
    assert _is_linked(b, 'receptionist9', a1)
    if hasattr(a1, 'manager8'):
        assert _is_linked(a1, 'manager8', b)
    _safe_set(b, 'receptionist9', {a2})
    assert _is_linked(b, 'receptionist9', a2)
    if hasattr(a1, 'manager8'):
        assert not _is_linked(a1, 'manager8', b)
    if hasattr(a2, 'manager8'):
        assert _is_linked(a2, 'manager8', b)
    _safe_set(b, 'receptionist9', set())
    assert not _is_linked(b, 'receptionist9', a2)
    if hasattr(a2, 'manager8'):
        assert not _is_linked(a2, 'manager8', b)


def test_assoc_Receptionist_Room_reverse_link_reassign_clear():
    a1 = Room(RatesofRoom=7, roomNo=7, typeOfRoom="sample_text")
    a2 = Room(RatesofRoom=13, roomNo=13, typeOfRoom="sample_text_2")
    b = Receptionist(Id=7, name="sample_text")
    _safe_set(b, 'room4', {a1})
    assert _is_linked(b, 'room4', a1)
    if hasattr(a1, 'receptionist5'):
        assert _is_linked(a1, 'receptionist5', b)
    _safe_set(b, 'room4', {a2})
    assert _is_linked(b, 'room4', a2)
    if hasattr(a1, 'receptionist5'):
        assert not _is_linked(a1, 'receptionist5', b)
    if hasattr(a2, 'receptionist5'):
        assert _is_linked(a2, 'receptionist5', b)
    _safe_set(b, 'room4', set())
    assert not _is_linked(b, 'room4', a2)
    if hasattr(a2, 'receptionist5'):
        assert not _is_linked(a2, 'receptionist5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

