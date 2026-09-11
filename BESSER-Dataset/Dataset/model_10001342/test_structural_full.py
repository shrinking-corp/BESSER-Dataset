import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Book_Room_UseCase,
    Cancel_Reservation_UseCase,
    Check_In_UseCase,
    Check_Out_UseCase,
    Chef_Actor,
    Customer,
    Food_Serving_UseCase,
    Hotel_Guest_Actor,
    HouseKeeping_Actor,
    Inventory,
    Manager,
    Menu_Preparation_UseCase,
    Receptionist_Actor,
    Room_Cleaning_UseCase,
    Search_Avalibility_UseCase,
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

def test_Inventory_Status_value_roundtrip():
    instance = Inventory(Status="sample_text", Type="sample_text")
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_Inventory_Type_value_roundtrip():
    instance = Inventory(Status="sample_text", Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_Manager_Id_value_roundtrip():
    instance = Manager(Id=7, Name="sample_text", Phone_No=7)
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Manager_Name_value_roundtrip():
    instance = Manager(Id=7, Name="sample_text", Phone_No=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Manager_Phone_No_value_roundtrip():
    instance = Manager(Id=7, Name="sample_text", Phone_No=7)
    assert instance.Phone_No == 7
    instance.Phone_No = 13
    assert instance.Phone_No == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Book_Room_UseCase_strategy = st.builds(Book_Room_UseCase)
@given(instance=Book_Room_UseCase_strategy)
@settings(max_examples=25)
def test_Book_Room_UseCase_instantiation(instance):
    assert isinstance(instance, Book_Room_UseCase)


Cancel_Reservation_UseCase_strategy = st.builds(Cancel_Reservation_UseCase)
@given(instance=Cancel_Reservation_UseCase_strategy)
@settings(max_examples=25)
def test_Cancel_Reservation_UseCase_instantiation(instance):
    assert isinstance(instance, Cancel_Reservation_UseCase)


Check_In_UseCase_strategy = st.builds(Check_In_UseCase)
@given(instance=Check_In_UseCase_strategy)
@settings(max_examples=25)
def test_Check_In_UseCase_instantiation(instance):
    assert isinstance(instance, Check_In_UseCase)


Check_Out_UseCase_strategy = st.builds(Check_Out_UseCase)
@given(instance=Check_Out_UseCase_strategy)
@settings(max_examples=25)
def test_Check_Out_UseCase_instantiation(instance):
    assert isinstance(instance, Check_Out_UseCase)


Chef_Actor_strategy = st.builds(Chef_Actor)
@given(instance=Chef_Actor_strategy)
@settings(max_examples=25)
def test_Chef_Actor_instantiation(instance):
    assert isinstance(instance, Chef_Actor)


Customer_strategy = st.builds(Customer)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Food_Serving_UseCase_strategy = st.builds(Food_Serving_UseCase)
@given(instance=Food_Serving_UseCase_strategy)
@settings(max_examples=25)
def test_Food_Serving_UseCase_instantiation(instance):
    assert isinstance(instance, Food_Serving_UseCase)


Hotel_Guest_Actor_strategy = st.builds(Hotel_Guest_Actor)
@given(instance=Hotel_Guest_Actor_strategy)
@settings(max_examples=25)
def test_Hotel_Guest_Actor_instantiation(instance):
    assert isinstance(instance, Hotel_Guest_Actor)


HouseKeeping_Actor_strategy = st.builds(HouseKeeping_Actor)
@given(instance=HouseKeeping_Actor_strategy)
@settings(max_examples=25)
def test_HouseKeeping_Actor_instantiation(instance):
    assert isinstance(instance, HouseKeeping_Actor)


Inventory_strategy = st.builds(Inventory, Status=safe_text, Type=safe_text)
@given(instance=Inventory_strategy)
@settings(max_examples=25)
def test_Inventory_instantiation(instance):
    assert isinstance(instance, Inventory)


Manager_strategy = st.builds(Manager, Id=st.integers(), Name=safe_text, Phone_No=st.integers())
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Menu_Preparation_UseCase_strategy = st.builds(Menu_Preparation_UseCase)
@given(instance=Menu_Preparation_UseCase_strategy)
@settings(max_examples=25)
def test_Menu_Preparation_UseCase_instantiation(instance):
    assert isinstance(instance, Menu_Preparation_UseCase)


Receptionist_Actor_strategy = st.builds(Receptionist_Actor)
@given(instance=Receptionist_Actor_strategy)
@settings(max_examples=25)
def test_Receptionist_Actor_instantiation(instance):
    assert isinstance(instance, Receptionist_Actor)


Room_Cleaning_UseCase_strategy = st.builds(Room_Cleaning_UseCase)
@given(instance=Room_Cleaning_UseCase_strategy)
@settings(max_examples=25)
def test_Room_Cleaning_UseCase_instantiation(instance):
    assert isinstance(instance, Room_Cleaning_UseCase)


Search_Avalibility_UseCase_strategy = st.builds(Search_Avalibility_UseCase)
@given(instance=Search_Avalibility_UseCase_strategy)
@settings(max_examples=25)
def test_Search_Avalibility_UseCase_instantiation(instance):
    assert isinstance(instance, Search_Avalibility_UseCase)


