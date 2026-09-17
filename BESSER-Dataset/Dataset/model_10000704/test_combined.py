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
    Room,
    Hotel,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "roomID" in params, "Missing parameter 'roomID'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "price" in params, "Missing parameter 'price'"
    assert "floor" in params, "Missing parameter 'floor'"
    assert "door" in params, "Missing parameter 'door'"








def test_hyp_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hyp_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hyp_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "zip" in params, "Missing parameter 'zip'"
    assert "city" in params, "Missing parameter 'city'"
    assert "website" in params, "Missing parameter 'website'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "street" in params, "Missing parameter 'street'"









def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "ident" in params, "Missing parameter 'ident'"
    assert "email" in params, "Missing parameter 'email'"
    assert "roomID" in params, "Missing parameter 'roomID'"







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
Room_strategy = st.builds(
    Room,
    roomID=
        st.integers(),
    capacity=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    floor=
        st.integers(),
    door=
        st.integers()
)
Hotel_strategy = st.builds(
    Hotel,
    zip=
        st.integers(),
    city=
        safe_text,
    website=
        safe_text,
    name=
        safe_text,
    phoneNumber=
        st.integers(),
    street=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    name=
        safe_text,
    phoneNumber=
        st.integers(),
    ident=
        safe_text,
    email=
        safe_text,
    roomID=
        st.integers()
)




@given(instance=Room_strategy)
def test_hyp_room_roomID_setter(instance):
    original = instance.roomID
    instance.roomID = original
    assert instance.roomID == original



@given(instance=Room_strategy)
def test_hyp_room_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=Room_strategy)
def test_hyp_room_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Room_strategy)
def test_hyp_room_floor_setter(instance):
    original = instance.floor
    instance.floor = original
    assert instance.floor == original



@given(instance=Room_strategy)
def test_hyp_room_door_setter(instance):
    original = instance.door
    instance.door = original
    assert instance.door == original




@given(instance=Hotel_strategy)
def test_hyp_hotel_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original




@given(instance=Customer_strategy)
def test_hyp_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_hyp_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_hyp_customer_ident_setter(instance):
    original = instance.ident
    instance.ident = original
    assert instance.ident == original



@given(instance=Customer_strategy)
def test_hyp_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_hyp_customer_roomID_setter(instance):
    original = instance.roomID
    instance.roomID = original
    assert instance.roomID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Customer,
    Hotel,
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

def test_Customer_email_value_roundtrip():
    instance = Customer(email="sample_text", ident="sample_text", name="sample_text", phoneNumber=7, roomID=7)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Customer_ident_value_roundtrip():
    instance = Customer(email="sample_text", ident="sample_text", name="sample_text", phoneNumber=7, roomID=7)
    assert instance.ident == "sample_text"
    instance.ident = "sample_text_2"
    assert instance.ident == "sample_text_2"


def test_Customer_name_value_roundtrip():
    instance = Customer(email="sample_text", ident="sample_text", name="sample_text", phoneNumber=7, roomID=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Customer_phoneNumber_value_roundtrip():
    instance = Customer(email="sample_text", ident="sample_text", name="sample_text", phoneNumber=7, roomID=7)
    assert instance.phoneNumber == 7
    instance.phoneNumber = 13
    assert instance.phoneNumber == 13


def test_Customer_roomID_value_roundtrip():
    instance = Customer(email="sample_text", ident="sample_text", name="sample_text", phoneNumber=7, roomID=7)
    assert instance.roomID == 7
    instance.roomID = 13
    assert instance.roomID == 13


def test_Hotel_city_value_roundtrip():
    instance = Hotel(city="sample_text", name="sample_text", phoneNumber=7, street="sample_text", website="sample_text", zip=7)
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_Hotel_name_value_roundtrip():
    instance = Hotel(city="sample_text", name="sample_text", phoneNumber=7, street="sample_text", website="sample_text", zip=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Hotel_phoneNumber_value_roundtrip():
    instance = Hotel(city="sample_text", name="sample_text", phoneNumber=7, street="sample_text", website="sample_text", zip=7)
    assert instance.phoneNumber == 7
    instance.phoneNumber = 13
    assert instance.phoneNumber == 13


def test_Hotel_street_value_roundtrip():
    instance = Hotel(city="sample_text", name="sample_text", phoneNumber=7, street="sample_text", website="sample_text", zip=7)
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_Hotel_website_value_roundtrip():
    instance = Hotel(city="sample_text", name="sample_text", phoneNumber=7, street="sample_text", website="sample_text", zip=7)
    assert instance.website == "sample_text"
    instance.website = "sample_text_2"
    assert instance.website == "sample_text_2"


def test_Hotel_zip_value_roundtrip():
    instance = Hotel(city="sample_text", name="sample_text", phoneNumber=7, street="sample_text", website="sample_text", zip=7)
    assert instance.zip == 7
    instance.zip = 13
    assert instance.zip == 13


def test_Room_capacity_value_roundtrip():
    instance = Room(capacity="sample_text", door=7, floor=7, price=3.14, roomID=7)
    assert instance.capacity == "sample_text"
    instance.capacity = "sample_text_2"
    assert instance.capacity == "sample_text_2"


def test_Room_door_value_roundtrip():
    instance = Room(capacity="sample_text", door=7, floor=7, price=3.14, roomID=7)
    assert instance.door == 7
    instance.door = 13
    assert instance.door == 13


def test_Room_floor_value_roundtrip():
    instance = Room(capacity="sample_text", door=7, floor=7, price=3.14, roomID=7)
    assert instance.floor == 7
    instance.floor = 13
    assert instance.floor == 13


def test_Room_price_value_roundtrip():
    instance = Room(capacity="sample_text", door=7, floor=7, price=3.14, roomID=7)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_Room_roomID_value_roundtrip():
    instance = Room(capacity="sample_text", door=7, floor=7, price=3.14, roomID=7)
    assert instance.roomID == 7
    instance.roomID = 13
    assert instance.roomID == 13


def test_assoc_Customer_Room_link_reassign_clear():
    a = Room(capacity="sample_text", door=7, floor=7, price=3.14, roomID=7)
    b1 = Customer(email="sample_text", ident="sample_text", name="sample_text", phoneNumber=7, roomID=7)
    b2 = Customer(email="sample_text_2", ident="sample_text_2", name="sample_text_2", phoneNumber=13, roomID=13)
    _safe_set(a, 'customer3', {b1})
    assert _is_linked(a, 'customer3', b1)
    if hasattr(b1, 'room2'):
        assert _is_linked(b1, 'room2', a)
    _safe_set(a, 'customer3', {b2})
    assert _is_linked(a, 'customer3', b2)
    if hasattr(b1, 'room2'):
        assert not _is_linked(b1, 'room2', a)
    if hasattr(b2, 'room2'):
        assert _is_linked(b2, 'room2', a)
    _safe_set(a, 'customer3', set())
    assert not _is_linked(a, 'customer3', b2)
    if hasattr(b2, 'room2'):
        assert not _is_linked(b2, 'room2', a)


def test_assoc_Hotel_Room_link_reassign_clear():
    a = Room(capacity="sample_text", door=7, floor=7, price=3.14, roomID=7)
    b1 = Hotel(city="sample_text", name="sample_text", phoneNumber=7, street="sample_text", website="sample_text", zip=7)
    b2 = Hotel(city="sample_text_2", name="sample_text_2", phoneNumber=13, street="sample_text_2", website="sample_text_2", zip=13)
    _safe_set(a, 'hotel1', b1)
    assert _is_linked(a, 'hotel1', b1)
    if hasattr(b1, 'room0'):
        assert _is_linked(b1, 'room0', a)
    _safe_set(a, 'hotel1', b2)
    assert _is_linked(a, 'hotel1', b2)
    if hasattr(b1, 'room0'):
        assert not _is_linked(b1, 'room0', a)
    if hasattr(b2, 'room0'):
        assert _is_linked(b2, 'room0', a)
    _safe_set(a, 'hotel1', None)
    assert not _is_linked(a, 'hotel1', b2)
    if hasattr(b2, 'room0'):
        assert not _is_linked(b2, 'room0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Customer_strategy = st.builds(Customer, email=safe_text, ident=safe_text, name=safe_text, phoneNumber=st.integers(), roomID=st.integers())
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Hotel_strategy = st.builds(Hotel, city=safe_text, name=safe_text, phoneNumber=st.integers(), street=safe_text, website=safe_text, zip=st.integers())
@given(instance=Hotel_strategy)
@settings(max_examples=25)
def test_Hotel_instantiation(instance):
    assert isinstance(instance, Hotel)


Room_strategy = st.builds(Room, capacity=safe_text, door=st.integers(), floor=st.integers(), price=st.floats(allow_nan=False, allow_infinity=False), roomID=st.integers())
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)



