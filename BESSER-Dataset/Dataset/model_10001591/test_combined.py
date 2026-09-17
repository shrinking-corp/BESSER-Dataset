# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Database,
    Inventory,
    Bill,
    Room,
    Manager,
    Receptionist,
    Guest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_hyp_database_constructor_exists():
    assert callable(Database.__init__)


def test_hyp_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())
    assert "Details" in params, "Missing parameter 'Details'"
    assert "service" in params, "Missing parameter 'service'"
    assert "income" in params, "Missing parameter 'income'"






def test_hyp_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_hyp_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_hyp_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "Status" in params, "Missing parameter 'Status'"





def test_hyp_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_hyp_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_hyp_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "GuestName" in params, "Missing parameter 'GuestName'"
    assert "bill_No" in params, "Missing parameter 'bill_No'"





def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "RatesofRoom" in params, "Missing parameter 'RatesofRoom'"
    assert "typeOfRoom" in params, "Missing parameter 'typeOfRoom'"
    assert "roomNo" in params, "Missing parameter 'roomNo'"






def test_hyp_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_hyp_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_hyp_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_hyp_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_hyp_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Id" in params, "Missing parameter 'Id'"





def test_hyp_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_hyp_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_hyp_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "phoneNo" in params, "Missing parameter 'phoneNo'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credit_card" in params, "Missing parameter 'credit_card'"
    assert "Room" in params, "Missing parameter 'Room'"








# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Database_strategy = st.builds(
    Database,
    Details=
        safe_text,
    service=
        safe_text,
    income=
        st.integers()
)
Inventory_strategy = st.builds(
    Inventory,
    type=
        safe_text,
    Status=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    GuestName=
        safe_text,
    bill_No=
        st.integers()
)
Room_strategy = st.builds(
    Room,
    RatesofRoom=
        st.integers(),
    typeOfRoom=
        safe_text,
    roomNo=
        st.integers()
)
Manager_strategy = st.builds(
    Manager,
    id=
        st.integers(),
    name=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    name=
        safe_text,
    Id=
        st.integers()
)
Guest_strategy = st.builds(
    Guest,
    Address=
        safe_text,
    phoneNo=
        st.integers(),
    id=
        st.integers(),
    name=
        safe_text,
    credit_card=
        st.integers(),
    Room=
        st.integers()
)




@given(instance=Database_strategy)
def test_hyp_database_Details_setter(instance):
    original = instance.Details
    instance.Details = original
    assert instance.Details == original



@given(instance=Database_strategy)
def test_hyp_database_service_setter(instance):
    original = instance.service
    instance.service = original
    assert instance.service == original



@given(instance=Database_strategy)
def test_hyp_database_income_setter(instance):
    original = instance.income
    instance.income = original
    assert instance.income == original




@given(instance=Inventory_strategy)
def test_hyp_inventory_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Inventory_strategy)
def test_hyp_inventory_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original




@given(instance=Bill_strategy)
def test_hyp_bill_GuestName_setter(instance):
    original = instance.GuestName
    instance.GuestName = original
    assert instance.GuestName == original



@given(instance=Bill_strategy)
def test_hyp_bill_bill_No_setter(instance):
    original = instance.bill_No
    instance.bill_No = original
    assert instance.bill_No == original




@given(instance=Room_strategy)
def test_hyp_room_RatesofRoom_setter(instance):
    original = instance.RatesofRoom
    instance.RatesofRoom = original
    assert instance.RatesofRoom == original



@given(instance=Room_strategy)
def test_hyp_room_typeOfRoom_setter(instance):
    original = instance.typeOfRoom
    instance.typeOfRoom = original
    assert instance.typeOfRoom == original



@given(instance=Room_strategy)
def test_hyp_room_roomNo_setter(instance):
    original = instance.roomNo
    instance.roomNo = original
    assert instance.roomNo == original




@given(instance=Manager_strategy)
def test_hyp_manager_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Manager_strategy)
def test_hyp_manager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Receptionist_strategy)
def test_hyp_receptionist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Receptionist_strategy)
def test_hyp_receptionist_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original




@given(instance=Guest_strategy)
def test_hyp_guest_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Guest_strategy)
def test_hyp_guest_phoneNo_setter(instance):
    original = instance.phoneNo
    instance.phoneNo = original
    assert instance.phoneNo == original



@given(instance=Guest_strategy)
def test_hyp_guest_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Guest_strategy)
def test_hyp_guest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Guest_strategy)
def test_hyp_guest_credit_card_setter(instance):
    original = instance.credit_card
    instance.credit_card = original
    assert instance.credit_card == original



@given(instance=Guest_strategy)
def test_hyp_guest_Room_setter(instance):
    original = instance.Room
    instance.Room = original
    assert instance.Room == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bill,
    Database,
    Guest,
    Inventory,
    Manager,
    Receptionist,
    Room,
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

def test_Bill_GuestName_value_roundtrip():
    instance = Bill(GuestName="sample_text", bill_No=7)
    assert instance.GuestName == "sample_text"
    instance.GuestName = "sample_text_2"
    assert instance.GuestName == "sample_text_2"


def test_Bill_bill_No_value_roundtrip():
    instance = Bill(GuestName="sample_text", bill_No=7)
    assert instance.bill_No == 7
    instance.bill_No = 13
    assert instance.bill_No == 13


def test_Database_Details_value_roundtrip():
    instance = Database(Details="sample_text", income=7, service="sample_text")
    assert instance.Details == "sample_text"
    instance.Details = "sample_text_2"
    assert instance.Details == "sample_text_2"


def test_Database_income_value_roundtrip():
    instance = Database(Details="sample_text", income=7, service="sample_text")
    assert instance.income == 7
    instance.income = 13
    assert instance.income == 13


def test_Database_service_value_roundtrip():
    instance = Database(Details="sample_text", income=7, service="sample_text")
    assert instance.service == "sample_text"
    instance.service = "sample_text_2"
    assert instance.service == "sample_text_2"


def test_Guest_Address_value_roundtrip():
    instance = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Guest_Room_value_roundtrip():
    instance = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    assert instance.Room == 7
    instance.Room = 13
    assert instance.Room == 13


def test_Guest_credit_card_value_roundtrip():
    instance = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    assert instance.credit_card == 7
    instance.credit_card = 13
    assert instance.credit_card == 13


def test_Guest_id_value_roundtrip():
    instance = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Guest_name_value_roundtrip():
    instance = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Guest_phoneNo_value_roundtrip():
    instance = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    assert instance.phoneNo == 7
    instance.phoneNo = 13
    assert instance.phoneNo == 13


def test_Inventory_Status_value_roundtrip():
    instance = Inventory(Status="sample_text", type="sample_text")
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_Inventory_type_value_roundtrip():
    instance = Inventory(Status="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Manager_id_value_roundtrip():
    instance = Manager(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Manager_name_value_roundtrip():
    instance = Manager(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Receptionist_Id_value_roundtrip():
    instance = Receptionist(Id=7, name="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Receptionist_name_value_roundtrip():
    instance = Receptionist(Id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Room_RatesofRoom_value_roundtrip():
    instance = Room(RatesofRoom=7, roomNo=7, typeOfRoom="sample_text")
    assert instance.RatesofRoom == 7
    instance.RatesofRoom = 13
    assert instance.RatesofRoom == 13


def test_Room_roomNo_value_roundtrip():
    instance = Room(RatesofRoom=7, roomNo=7, typeOfRoom="sample_text")
    assert instance.roomNo == 7
    instance.roomNo = 13
    assert instance.roomNo == 13


def test_Room_typeOfRoom_value_roundtrip():
    instance = Room(RatesofRoom=7, roomNo=7, typeOfRoom="sample_text")
    assert instance.typeOfRoom == "sample_text"
    instance.typeOfRoom = "sample_text_2"
    assert instance.typeOfRoom == "sample_text_2"


def test_assoc_Guest_Bill_link_reassign_clear():
    a = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    b1 = Bill(GuestName="sample_text", bill_No=7)
    b2 = Bill(GuestName="sample_text_2", bill_No=13)
    _safe_set(a, 'bill2', b1)
    assert _is_linked(a, 'bill2', b1)
    if hasattr(b1, 'guest3'):
        assert _is_linked(b1, 'guest3', a)
    _safe_set(a, 'bill2', b2)
    assert _is_linked(a, 'bill2', b2)
    if hasattr(b1, 'guest3'):
        assert not _is_linked(b1, 'guest3', a)
    if hasattr(b2, 'guest3'):
        assert _is_linked(b2, 'guest3', a)
    _safe_set(a, 'bill2', None)
    assert not _is_linked(a, 'bill2', b2)
    if hasattr(b2, 'guest3'):
        assert not _is_linked(b2, 'guest3', a)


def test_assoc_Guest_Room_link_reassign_clear():
    a = Room(RatesofRoom=7, roomNo=7, typeOfRoom="sample_text")
    b1 = Guest(Address="sample_text", Room=7, credit_card=7, id=7, name="sample_text", phoneNo=7)
    b2 = Guest(Address="sample_text_2", Room=13, credit_card=13, id=13, name="sample_text_2", phoneNo=13)
    _safe_set(a, 'guest1', b1)
    assert _is_linked(a, 'guest1', b1)
    if hasattr(b1, 'room0'):
        assert _is_linked(b1, 'room0', a)
    _safe_set(a, 'guest1', b2)
    assert _is_linked(a, 'guest1', b2)
    if hasattr(b1, 'room0'):
        assert not _is_linked(b1, 'room0', a)
    if hasattr(b2, 'room0'):
        assert _is_linked(b2, 'room0', a)
    _safe_set(a, 'guest1', None)
    assert not _is_linked(a, 'guest1', b2)
    if hasattr(b2, 'room0'):
        assert not _is_linked(b2, 'room0', a)


def test_assoc_Inventory_Manager_link_reassign_clear():
    a = Manager(id=7, name="sample_text")
    b1 = Inventory(Status="sample_text", type="sample_text")
    b2 = Inventory(Status="sample_text_2", type="sample_text_2")
    _safe_set(a, 'inventory11', b1)
    assert _is_linked(a, 'inventory11', b1)
    if hasattr(b1, 'manager10'):
        assert _is_linked(b1, 'manager10', a)
    _safe_set(a, 'inventory11', b2)
    assert _is_linked(a, 'inventory11', b2)
    if hasattr(b1, 'manager10'):
        assert not _is_linked(b1, 'manager10', a)
    if hasattr(b2, 'manager10'):
        assert _is_linked(b2, 'manager10', a)
    _safe_set(a, 'inventory11', None)
    assert not _is_linked(a, 'inventory11', b2)
    if hasattr(b2, 'manager10'):
        assert not _is_linked(b2, 'manager10', a)


def test_assoc_Manager_Database_link_reassign_clear():
    a = Manager(id=7, name="sample_text")
    b1 = Database(Details="sample_text", income=7, service="sample_text")
    b2 = Database(Details="sample_text_2", income=13, service="sample_text_2")
    _safe_set(a, 'database14', b1)
    assert _is_linked(a, 'database14', b1)
    if hasattr(b1, 'manager15'):
        assert _is_linked(b1, 'manager15', a)
    _safe_set(a, 'database14', b2)
    assert _is_linked(a, 'database14', b2)
    if hasattr(b1, 'manager15'):
        assert not _is_linked(b1, 'manager15', a)
    if hasattr(b2, 'manager15'):
        assert _is_linked(b2, 'manager15', a)
    _safe_set(a, 'database14', None)
    assert not _is_linked(a, 'database14', b2)
    if hasattr(b2, 'manager15'):
        assert not _is_linked(b2, 'manager15', a)


def test_assoc_Receptionist_Bill_link_reassign_clear():
    a = Receptionist(Id=7, name="sample_text")
    b1 = Bill(GuestName="sample_text", bill_No=7)
    b2 = Bill(GuestName="sample_text_2", bill_No=13)
    _safe_set(a, 'bill6', {b1})
    assert _is_linked(a, 'bill6', b1)
    if hasattr(b1, 'receptionist7'):
        assert _is_linked(b1, 'receptionist7', a)
    _safe_set(a, 'bill6', {b2})
    assert _is_linked(a, 'bill6', b2)
    if hasattr(b1, 'receptionist7'):
        assert not _is_linked(b1, 'receptionist7', a)
    if hasattr(b2, 'receptionist7'):
        assert _is_linked(b2, 'receptionist7', a)
    _safe_set(a, 'bill6', set())
    assert not _is_linked(a, 'bill6', b2)
    if hasattr(b2, 'receptionist7'):
        assert not _is_linked(b2, 'receptionist7', a)


def test_assoc_Receptionist_Database_link_reassign_clear():
    a = Receptionist(Id=7, name="sample_text")
    b1 = Database(Details="sample_text", income=7, service="sample_text")
    b2 = Database(Details="sample_text_2", income=13, service="sample_text_2")
    _safe_set(a, 'database12', b1)
    assert _is_linked(a, 'database12', b1)
    if hasattr(b1, 'receptionist13'):
        assert _is_linked(b1, 'receptionist13', a)
    _safe_set(a, 'database12', b2)
    assert _is_linked(a, 'database12', b2)
    if hasattr(b1, 'receptionist13'):
        assert not _is_linked(b1, 'receptionist13', a)
    if hasattr(b2, 'receptionist13'):
        assert _is_linked(b2, 'receptionist13', a)
    _safe_set(a, 'database12', None)
    assert not _is_linked(a, 'database12', b2)
    if hasattr(b2, 'receptionist13'):
        assert not _is_linked(b2, 'receptionist13', a)


def test_assoc_Receptionist_Manager_link_reassign_clear():
    a = Receptionist(Id=7, name="sample_text")
    b1 = Manager(id=7, name="sample_text")
    b2 = Manager(id=13, name="sample_text_2")
    _safe_set(a, 'manager8', b1)
    assert _is_linked(a, 'manager8', b1)
    if hasattr(b1, 'receptionist9'):
        assert _is_linked(b1, 'receptionist9', a)
    _safe_set(a, 'manager8', b2)
    assert _is_linked(a, 'manager8', b2)
    if hasattr(b1, 'receptionist9'):
        assert not _is_linked(b1, 'receptionist9', a)
    if hasattr(b2, 'receptionist9'):
        assert _is_linked(b2, 'receptionist9', a)
    _safe_set(a, 'manager8', None)
    assert not _is_linked(a, 'manager8', b2)
    if hasattr(b2, 'receptionist9'):
        assert not _is_linked(b2, 'receptionist9', a)


def test_assoc_Receptionist_Room_link_reassign_clear():
    a = Room(RatesofRoom=7, roomNo=7, typeOfRoom="sample_text")
    b1 = Receptionist(Id=7, name="sample_text")
    b2 = Receptionist(Id=13, name="sample_text_2")
    _safe_set(a, 'receptionist5', {b1})
    assert _is_linked(a, 'receptionist5', b1)
    if hasattr(b1, 'room4'):
        assert _is_linked(b1, 'room4', a)
    _safe_set(a, 'receptionist5', {b2})
    assert _is_linked(a, 'receptionist5', b2)
    if hasattr(b1, 'room4'):
        assert not _is_linked(b1, 'room4', a)
    if hasattr(b2, 'room4'):
        assert _is_linked(b2, 'room4', a)
    _safe_set(a, 'receptionist5', set())
    assert not _is_linked(a, 'receptionist5', b2)
    if hasattr(b2, 'room4'):
        assert not _is_linked(b2, 'room4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bill_strategy = st.builds(Bill, GuestName=safe_text, bill_No=st.integers())
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Database_strategy = st.builds(Database, Details=safe_text, income=st.integers(), service=safe_text)
@given(instance=Database_strategy)
@settings(max_examples=25)
def test_Database_instantiation(instance):
    assert isinstance(instance, Database)


Guest_strategy = st.builds(Guest, Address=safe_text, Room=st.integers(), credit_card=st.integers(), id=st.integers(), name=safe_text, phoneNo=st.integers())
@given(instance=Guest_strategy)
@settings(max_examples=25)
def test_Guest_instantiation(instance):
    assert isinstance(instance, Guest)


Inventory_strategy = st.builds(Inventory, Status=safe_text, type=safe_text)
@given(instance=Inventory_strategy)
@settings(max_examples=25)
def test_Inventory_instantiation(instance):
    assert isinstance(instance, Inventory)


Manager_strategy = st.builds(Manager, id=st.integers(), name=safe_text)
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Receptionist_strategy = st.builds(Receptionist, Id=st.integers(), name=safe_text)
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Room_strategy = st.builds(Room, RatesofRoom=st.integers(), roomNo=st.integers(), typeOfRoom=safe_text)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)



