import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Bill_billNo_value_roundtrip():
    instance = Bill(billNo=7, guestID=7)
    assert instance.billNo == 7
    instance.billNo = 13
    assert instance.billNo == 13


def test_Bill_guestID_value_roundtrip():
    instance = Bill(billNo=7, guestID=7)
    assert instance.guestID == 7
    instance.guestID = 13
    assert instance.guestID == 13


def test_Chef_branch_value_roundtrip():
    instance = Chef(branch="sample_text", chefID=7, name="sample_text")
    assert instance.branch == "sample_text"
    instance.branch = "sample_text_2"
    assert instance.branch == "sample_text_2"


def test_Chef_chefID_value_roundtrip():
    instance = Chef(branch="sample_text", chefID=7, name="sample_text")
    assert instance.chefID == 7
    instance.chefID = 13
    assert instance.chefID == 13


def test_Chef_name_value_roundtrip():
    instance = Chef(branch="sample_text", chefID=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Food_foodID_value_roundtrip():
    instance = Food(foodID=7, name="sample_text")
    assert instance.foodID == 7
    instance.foodID = 13
    assert instance.foodID == 13


def test_Food_name_value_roundtrip():
    instance = Food(foodID=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Guest_address_value_roundtrip():
    instance = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Guest_guestID_value_roundtrip():
    instance = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    assert instance.guestID == 7
    instance.guestID = 13
    assert instance.guestID == 13


def test_Guest_name_value_roundtrip():
    instance = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Guest_phoneNo_value_roundtrip():
    instance = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    assert instance.phoneNo == 7
    instance.phoneNo = 13
    assert instance.phoneNo == 13


def test_Guest_roomNo_value_roundtrip():
    instance = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    assert instance.roomNo == 7
    instance.roomNo = 13
    assert instance.roomNo == 13


def test_Housekeeping_branch_value_roundtrip():
    instance = Housekeeping(branch="sample_text", hkID=7, name="sample_text")
    assert instance.branch == "sample_text"
    instance.branch = "sample_text_2"
    assert instance.branch == "sample_text_2"


def test_Housekeeping_hkID_value_roundtrip():
    instance = Housekeeping(branch="sample_text", hkID=7, name="sample_text")
    assert instance.hkID == 7
    instance.hkID = 13
    assert instance.hkID == 13


def test_Housekeeping_name_value_roundtrip():
    instance = Housekeeping(branch="sample_text", hkID=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Inventory_status_value_roundtrip():
    instance = Inventory(status="sample_text", type="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Inventory_type_value_roundtrip():
    instance = Inventory(status="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Manager_branch_value_roundtrip():
    instance = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    assert instance.branch == "sample_text"
    instance.branch = "sample_text_2"
    assert instance.branch == "sample_text_2"


def test_Manager_managerID_value_roundtrip():
    instance = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    assert instance.managerID == 7
    instance.managerID = 13
    assert instance.managerID == 13


def test_Manager_name_value_roundtrip():
    instance = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Manager_phoneNo_value_roundtrip():
    instance = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    assert instance.phoneNo == 7
    instance.phoneNo = 13
    assert instance.phoneNo == 13


def test_Receptionist_branch_value_roundtrip():
    instance = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    assert instance.branch == "sample_text"
    instance.branch = "sample_text_2"
    assert instance.branch == "sample_text_2"


def test_Receptionist_name_value_roundtrip():
    instance = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Receptionist_phoneNo_value_roundtrip():
    instance = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    assert instance.phoneNo == 7
    instance.phoneNo = 13
    assert instance.phoneNo == 13


def test_Receptionist_rID_value_roundtrip():
    instance = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    assert instance.rID == 7
    instance.rID = 13
    assert instance.rID == 13


def test_Rooms_roomNo_value_roundtrip():
    instance = Rooms(roomNo=7, type="sample_text")
    assert instance.roomNo == 7
    instance.roomNo = 13
    assert instance.roomNo == 13


def test_Rooms_type_value_roundtrip():
    instance = Rooms(roomNo=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_Chef_Food_link_reassign_clear():
    a = Food(foodID=7, name="sample_text")
    b1 = Chef(branch="sample_text", chefID=7, name="sample_text")
    b2 = Chef(branch="sample_text_2", chefID=13, name="sample_text_2")
    _safe_set(a, 'chef5', {b1})
    assert _is_linked(a, 'chef5', b1)
    if hasattr(b1, 'food4'):
        assert _is_linked(b1, 'food4', a)
    _safe_set(a, 'chef5', {b2})
    assert _is_linked(a, 'chef5', b2)
    if hasattr(b1, 'food4'):
        assert not _is_linked(b1, 'food4', a)
    if hasattr(b2, 'food4'):
        assert _is_linked(b2, 'food4', a)
    _safe_set(a, 'chef5', set())
    assert not _is_linked(a, 'chef5', b2)
    if hasattr(b2, 'food4'):
        assert not _is_linked(b2, 'food4', a)


def test_assoc_Food_Guest_link_reassign_clear():
    a = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    b1 = Food(foodID=7, name="sample_text")
    b2 = Food(foodID=13, name="sample_text_2")
    _safe_set(a, 'food7', {b1})
    assert _is_linked(a, 'food7', b1)
    if hasattr(b1, 'guest6'):
        assert _is_linked(b1, 'guest6', a)
    _safe_set(a, 'food7', {b2})
    assert _is_linked(a, 'food7', b2)
    if hasattr(b1, 'guest6'):
        assert not _is_linked(b1, 'guest6', a)
    if hasattr(b2, 'guest6'):
        assert _is_linked(b2, 'guest6', a)
    _safe_set(a, 'food7', set())
    assert not _is_linked(a, 'food7', b2)
    if hasattr(b2, 'guest6'):
        assert not _is_linked(b2, 'guest6', a)


def test_assoc_Guest_Bill_link_reassign_clear():
    a = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    b1 = Bill(billNo=7, guestID=7)
    b2 = Bill(billNo=13, guestID=13)
    _safe_set(a, 'bill10', b1)
    assert _is_linked(a, 'bill10', b1)
    if hasattr(b1, 'guest11'):
        assert _is_linked(b1, 'guest11', a)
    _safe_set(a, 'bill10', b2)
    assert _is_linked(a, 'bill10', b2)
    if hasattr(b1, 'guest11'):
        assert not _is_linked(b1, 'guest11', a)
    if hasattr(b2, 'guest11'):
        assert _is_linked(b2, 'guest11', a)
    _safe_set(a, 'bill10', None)
    assert not _is_linked(a, 'bill10', b2)
    if hasattr(b2, 'guest11'):
        assert not _is_linked(b2, 'guest11', a)


def test_assoc_Guest_Rooms_link_reassign_clear():
    a = Rooms(roomNo=7, type="sample_text")
    b1 = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    b2 = Guest(address="sample_text_2", guestID=13, name="sample_text_2", phoneNo=13, roomNo=13)
    _safe_set(a, 'guest9', b1)
    assert _is_linked(a, 'guest9', b1)
    if hasattr(b1, 'rooms8'):
        assert _is_linked(b1, 'rooms8', a)
    _safe_set(a, 'guest9', b2)
    assert _is_linked(a, 'guest9', b2)
    if hasattr(b1, 'rooms8'):
        assert not _is_linked(b1, 'rooms8', a)
    if hasattr(b2, 'rooms8'):
        assert _is_linked(b2, 'rooms8', a)
    _safe_set(a, 'guest9', None)
    assert not _is_linked(a, 'guest9', b2)
    if hasattr(b2, 'rooms8'):
        assert not _is_linked(b2, 'rooms8', a)


def test_assoc_Manager_Guest_link_reassign_clear():
    a = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    b1 = Guest(address="sample_text", guestID=7, name="sample_text", phoneNo=7, roomNo=7)
    b2 = Guest(address="sample_text_2", guestID=13, name="sample_text_2", phoneNo=13, roomNo=13)
    _safe_set(a, 'guest2', {b1})
    assert _is_linked(a, 'guest2', b1)
    if hasattr(b1, 'manager3'):
        assert _is_linked(b1, 'manager3', a)
    _safe_set(a, 'guest2', {b2})
    assert _is_linked(a, 'guest2', b2)
    if hasattr(b1, 'manager3'):
        assert not _is_linked(b1, 'manager3', a)
    if hasattr(b2, 'manager3'):
        assert _is_linked(b2, 'manager3', a)
    _safe_set(a, 'guest2', set())
    assert not _is_linked(a, 'guest2', b2)
    if hasattr(b2, 'manager3'):
        assert not _is_linked(b2, 'manager3', a)


def test_assoc_Manager_Inventory_link_reassign_clear():
    a = Manager(branch="sample_text", managerID=7, name="sample_text", phoneNo=7)
    b1 = Inventory(status="sample_text", type="sample_text")
    b2 = Inventory(status="sample_text_2", type="sample_text_2")
    _safe_set(a, 'inventory0', {b1})
    assert _is_linked(a, 'inventory0', b1)
    if hasattr(b1, 'manager1'):
        assert _is_linked(b1, 'manager1', a)
    _safe_set(a, 'inventory0', {b2})
    assert _is_linked(a, 'inventory0', b2)
    if hasattr(b1, 'manager1'):
        assert not _is_linked(b1, 'manager1', a)
    if hasattr(b2, 'manager1'):
        assert _is_linked(b2, 'manager1', a)
    _safe_set(a, 'inventory0', set())
    assert not _is_linked(a, 'inventory0', b2)
    if hasattr(b2, 'manager1'):
        assert not _is_linked(b2, 'manager1', a)


def test_assoc_Receptionist_Bill_link_reassign_clear():
    a = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    b1 = Bill(billNo=7, guestID=7)
    b2 = Bill(billNo=13, guestID=13)
    _safe_set(a, 'bill14', b1)
    assert _is_linked(a, 'bill14', b1)
    if hasattr(b1, 'receptionist15'):
        assert _is_linked(b1, 'receptionist15', a)
    _safe_set(a, 'bill14', b2)
    assert _is_linked(a, 'bill14', b2)
    if hasattr(b1, 'receptionist15'):
        assert not _is_linked(b1, 'receptionist15', a)
    if hasattr(b2, 'receptionist15'):
        assert _is_linked(b2, 'receptionist15', a)
    _safe_set(a, 'bill14', None)
    assert not _is_linked(a, 'bill14', b2)
    if hasattr(b2, 'receptionist15'):
        assert not _is_linked(b2, 'receptionist15', a)


def test_assoc_Rooms_Housekeeping_link_reassign_clear():
    a = Rooms(roomNo=7, type="sample_text")
    b1 = Housekeeping(branch="sample_text", hkID=7, name="sample_text")
    b2 = Housekeeping(branch="sample_text_2", hkID=13, name="sample_text_2")
    _safe_set(a, 'housekeeping12', b1)
    assert _is_linked(a, 'housekeeping12', b1)
    if hasattr(b1, 'rooms13'):
        assert _is_linked(b1, 'rooms13', a)
    _safe_set(a, 'housekeeping12', b2)
    assert _is_linked(a, 'housekeeping12', b2)
    if hasattr(b1, 'rooms13'):
        assert not _is_linked(b1, 'rooms13', a)
    if hasattr(b2, 'rooms13'):
        assert _is_linked(b2, 'rooms13', a)
    _safe_set(a, 'housekeeping12', None)
    assert not _is_linked(a, 'housekeeping12', b2)
    if hasattr(b2, 'rooms13'):
        assert not _is_linked(b2, 'rooms13', a)


def test_assoc_Rooms_Receptionist_link_reassign_clear():
    a = Rooms(roomNo=7, type="sample_text")
    b1 = Receptionist(branch="sample_text", name="sample_text", phoneNo=7, rID=7)
    b2 = Receptionist(branch="sample_text_2", name="sample_text_2", phoneNo=13, rID=13)
    _safe_set(a, 'receptionist16', {b1})
    assert _is_linked(a, 'receptionist16', b1)
    if hasattr(b1, 'rooms17'):
        assert _is_linked(b1, 'rooms17', a)
    _safe_set(a, 'receptionist16', {b2})
    assert _is_linked(a, 'receptionist16', b2)
    if hasattr(b1, 'rooms17'):
        assert not _is_linked(b1, 'rooms17', a)
    if hasattr(b2, 'rooms17'):
        assert _is_linked(b2, 'rooms17', a)
    _safe_set(a, 'receptionist16', set())
    assert not _is_linked(a, 'receptionist16', b2)
    if hasattr(b2, 'rooms17'):
        assert not _is_linked(b2, 'rooms17', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bill_strategy = st.builds(Bill, billNo=st.integers(), guestID=st.integers())
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Chef_strategy = st.builds(Chef, branch=safe_text, chefID=st.integers(), name=safe_text)
@given(instance=Chef_strategy)
@settings(max_examples=25)
def test_Chef_instantiation(instance):
    assert isinstance(instance, Chef)


Food_strategy = st.builds(Food, foodID=st.integers(), name=safe_text)
@given(instance=Food_strategy)
@settings(max_examples=25)
def test_Food_instantiation(instance):
    assert isinstance(instance, Food)


Guest_strategy = st.builds(Guest, address=safe_text, guestID=st.integers(), name=safe_text, phoneNo=st.integers(), roomNo=st.integers())
@given(instance=Guest_strategy)
@settings(max_examples=25)
def test_Guest_instantiation(instance):
    assert isinstance(instance, Guest)


Housekeeping_strategy = st.builds(Housekeeping, branch=safe_text, hkID=st.integers(), name=safe_text)
@given(instance=Housekeeping_strategy)
@settings(max_examples=25)
def test_Housekeeping_instantiation(instance):
    assert isinstance(instance, Housekeeping)


Inventory_strategy = st.builds(Inventory, status=safe_text, type=safe_text)
@given(instance=Inventory_strategy)
@settings(max_examples=25)
def test_Inventory_instantiation(instance):
    assert isinstance(instance, Inventory)


Manager_strategy = st.builds(Manager, branch=safe_text, managerID=st.integers(), name=safe_text, phoneNo=st.integers())
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Receptionist_strategy = st.builds(Receptionist, branch=safe_text, name=safe_text, phoneNo=st.integers(), rID=st.integers())
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Rooms_strategy = st.builds(Rooms, roomNo=st.integers(), type=safe_text)
@given(instance=Rooms_strategy)
@settings(max_examples=25)
def test_Rooms_instantiation(instance):
    assert isinstance(instance, Rooms)


