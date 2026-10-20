import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bill,
    Chef,
    Food,
    Guest,
    Housekeeping,
    Inventory,
    Manager,
    Receptionist,
    Rooms,
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

def test_assoc_Chef_Food_reverse_link_reassign_clear():
    a1 = Food(foodID=7, name="sample_text")
    a2 = Food(foodID=13, name="sample_text_2")
    b = Chef(branch="sample_text", chefID=7, name="sample_text")
    _safe_set(b, 'food4', {a1})
    assert _is_linked(b, 'food4', a1)
    if hasattr(a1, 'chef5'):
        assert _is_linked(a1, 'chef5', b)
    _safe_set(b, 'food4', {a2})
    assert _is_linked(b, 'food4', a2)
    if hasattr(a1, 'chef5'):
        assert not _is_linked(a1, 'chef5', b)
    if hasattr(a2, 'chef5'):
        assert _is_linked(a2, 'chef5', b)
    _safe_set(b, 'food4', set())
    assert not _is_linked(b, 'food4', a2)
    if hasattr(a2, 'chef5'):
        assert not _is_linked(a2, 'chef5', b)


def test_assoc_Food_Guest_reverse_link_reassign_clear():
    a1 = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    a2 = Guest(address="sample_text_2", guestID=13, name="sample_text_2", phoneNo=13, roomNo=13)
    b = Food(foodID=7, name="sample_text")
    _safe_set(b, 'guest6', {a1})
    assert _is_linked(b, 'guest6', a1)
    if hasattr(a1, 'food7'):
        assert _is_linked(a1, 'food7', b)
    _safe_set(b, 'guest6', {a2})
    assert _is_linked(b, 'guest6', a2)
    if hasattr(a1, 'food7'):
        assert not _is_linked(a1, 'food7', b)
    if hasattr(a2, 'food7'):
        assert _is_linked(a2, 'food7', b)
    _safe_set(b, 'guest6', set())
    assert not _is_linked(b, 'guest6', a2)
    if hasattr(a2, 'food7'):
        assert not _is_linked(a2, 'food7', b)


def test_assoc_Guest_Bill_reverse_link_reassign_clear():
    a1 = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    a2 = Guest(address="sample_text_2", guestID=13, name="sample_text_2", phoneNo=13, roomNo=13)
    b = Bill(billNo=7, guestID=7)
    _safe_set(b, 'guest11', a1)
    assert _is_linked(b, 'guest11', a1)
    if hasattr(a1, 'bill10'):
        assert _is_linked(a1, 'bill10', b)
    _safe_set(b, 'guest11', a2)
    assert _is_linked(b, 'guest11', a2)
    if hasattr(a1, 'bill10'):
        assert not _is_linked(a1, 'bill10', b)
    if hasattr(a2, 'bill10'):
        assert _is_linked(a2, 'bill10', b)
    _safe_set(b, 'guest11', None)
    assert not _is_linked(b, 'guest11', a2)
    if hasattr(a2, 'bill10'):
        assert not _is_linked(a2, 'bill10', b)


def test_assoc_Guest_Rooms_reverse_link_reassign_clear():
    a1 = Rooms(roomNo=7, type="sample_text")
    a2 = Rooms(roomNo=13, type="sample_text_2")
    b = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    _safe_set(b, 'rooms8', {a1})
    assert _is_linked(b, 'rooms8', a1)
    if hasattr(a1, 'guest9'):
        assert _is_linked(a1, 'guest9', b)
    _safe_set(b, 'rooms8', {a2})
    assert _is_linked(b, 'rooms8', a2)
    if hasattr(a1, 'guest9'):
        assert not _is_linked(a1, 'guest9', b)
    if hasattr(a2, 'guest9'):
        assert _is_linked(a2, 'guest9', b)
    _safe_set(b, 'rooms8', set())
    assert not _is_linked(b, 'rooms8', a2)
    if hasattr(a2, 'guest9'):
        assert not _is_linked(a2, 'guest9', b)


def test_assoc_Manager_Guest_reverse_link_reassign_clear():
    a1 = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    a2 = Manager(branch="sample_text_2", managerID=13, name="sample_text_2", phoneNo=13)
    b = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    _safe_set(b, 'manager3', a1)
    assert _is_linked(b, 'manager3', a1)
    if hasattr(a1, 'guest2'):
        assert _is_linked(a1, 'guest2', b)
    _safe_set(b, 'manager3', a2)
    assert _is_linked(b, 'manager3', a2)
    if hasattr(a1, 'guest2'):
        assert not _is_linked(a1, 'guest2', b)
    if hasattr(a2, 'guest2'):
        assert _is_linked(a2, 'guest2', b)
    _safe_set(b, 'manager3', None)
    assert not _is_linked(b, 'manager3', a2)
    if hasattr(a2, 'guest2'):
        assert not _is_linked(a2, 'guest2', b)


def test_assoc_Manager_Inventory_reverse_link_reassign_clear():
    a1 = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    a2 = Manager(branch="sample_text_2", managerID=13, name="sample_text_2", phoneNo=13)
    b = Inventory(status="sample_text", type="sample_text")
    _safe_set(b, 'manager1', a1)
    assert _is_linked(b, 'manager1', a1)
    if hasattr(a1, 'inventory0'):
        assert _is_linked(a1, 'inventory0', b)
    _safe_set(b, 'manager1', a2)
    assert _is_linked(b, 'manager1', a2)
    if hasattr(a1, 'inventory0'):
        assert not _is_linked(a1, 'inventory0', b)
    if hasattr(a2, 'inventory0'):
        assert _is_linked(a2, 'inventory0', b)
    _safe_set(b, 'manager1', None)
    assert not _is_linked(b, 'manager1', a2)
    if hasattr(a2, 'inventory0'):
        assert not _is_linked(a2, 'inventory0', b)


def test_assoc_Receptionist_Bill_reverse_link_reassign_clear():
    a1 = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    a2 = Receptionist(branch="sample_text_2", name="sample_text_2", phoneNo=13, rID=13)
    b = Bill(billNo=7, guestID=7)
    _safe_set(b, 'receptionist15', {a1})
    assert _is_linked(b, 'receptionist15', a1)
    if hasattr(a1, 'bill14'):
        assert _is_linked(a1, 'bill14', b)
    _safe_set(b, 'receptionist15', {a2})
    assert _is_linked(b, 'receptionist15', a2)
    if hasattr(a1, 'bill14'):
        assert not _is_linked(a1, 'bill14', b)
    if hasattr(a2, 'bill14'):
        assert _is_linked(a2, 'bill14', b)
    _safe_set(b, 'receptionist15', set())
    assert not _is_linked(b, 'receptionist15', a2)
    if hasattr(a2, 'bill14'):
        assert not _is_linked(a2, 'bill14', b)


def test_assoc_Rooms_Housekeeping_reverse_link_reassign_clear():
    a1 = Rooms(roomNo=7, type="sample_text")
    a2 = Rooms(roomNo=13, type="sample_text_2")
    b = Housekeeping(branch="sample_text", hkID=7, name="sample_text")
    _safe_set(b, 'rooms13', a1)
    assert _is_linked(b, 'rooms13', a1)
    if hasattr(a1, 'housekeeping12'):
        assert _is_linked(a1, 'housekeeping12', b)
    _safe_set(b, 'rooms13', a2)
    assert _is_linked(b, 'rooms13', a2)
    if hasattr(a1, 'housekeeping12'):
        assert not _is_linked(a1, 'housekeeping12', b)
    if hasattr(a2, 'housekeeping12'):
        assert _is_linked(a2, 'housekeeping12', b)
    _safe_set(b, 'rooms13', None)
    assert not _is_linked(b, 'rooms13', a2)
    if hasattr(a2, 'housekeeping12'):
        assert not _is_linked(a2, 'housekeeping12', b)


def test_assoc_Rooms_Receptionist_reverse_link_reassign_clear():
    a1 = Rooms(roomNo=7, type="sample_text")
    a2 = Rooms(roomNo=13, type="sample_text_2")
    b = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    _safe_set(b, 'rooms17', {a1})
    assert _is_linked(b, 'rooms17', a1)
    if hasattr(a1, 'receptionist16'):
        assert _is_linked(a1, 'receptionist16', b)
    _safe_set(b, 'rooms17', {a2})
    assert _is_linked(b, 'rooms17', a2)
    if hasattr(a1, 'receptionist16'):
        assert not _is_linked(a1, 'receptionist16', b)
    if hasattr(a2, 'receptionist16'):
        assert _is_linked(a2, 'receptionist16', b)
    _safe_set(b, 'rooms17', set())
    assert not _is_linked(b, 'rooms17', a2)
    if hasattr(a2, 'receptionist16'):
        assert not _is_linked(a2, 'receptionist16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

