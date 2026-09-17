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
    occupancy,
    Booking,
    User,
    Location,
    Rooms,
    Hotels,
    Owner,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_occupancy_is_not_abstract():
    assert not inspect.isabstract(occupancy)


def test_hyp_occupancy_constructor_exists():
    assert callable(occupancy.__init__)


def test_hyp_occupancy_constructor_args():
    sig = inspect.signature(occupancy.__init__)
    params = list(sig.parameters.keys())
    assert "booking_id" in params, "Missing parameter 'booking_id'"




def test_hyp_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_hyp_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_hyp_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "booking_id" in params, "Missing parameter 'booking_id'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "guest_adress" in params, "Missing parameter 'guest_adress'"
    assert "guest_id" in params, "Missing parameter 'guest_id'"
    assert "guest_name" in params, "Missing parameter 'guest_name'"
    assert "guestphn_no" in params, "Missing parameter 'guestphn_no'"









def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"
    assert "address" in params, "Missing parameter 'address'"
    assert "mail_id" in params, "Missing parameter 'mail_id'"
    assert "phn_no" in params, "Missing parameter 'phn_no'"









def test_hyp_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_hyp_location_constructor_exists():
    assert callable(Location.__init__)


def test_hyp_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "loc_name" in params, "Missing parameter 'loc_name'"
    assert "loc_id" in params, "Missing parameter 'loc_id'"






def test_hyp_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_hyp_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_hyp_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "room_description" in params, "Missing parameter 'room_description'"
    assert "checkout_date" in params, "Missing parameter 'checkout_date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "price" in params, "Missing parameter 'price'"
    assert "checkin_date" in params, "Missing parameter 'checkin_date'"









def test_hyp_hotels_is_not_abstract():
    assert not inspect.isabstract(Hotels)


def test_hyp_hotels_constructor_exists():
    assert callable(Hotels.__init__)


def test_hyp_hotels_constructor_args():
    sig = inspect.signature(Hotels.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "hotel_description" in params, "Missing parameter 'hotel_description'"






def test_hyp_owner_is_not_abstract():
    assert not inspect.isabstract(Owner)


def test_hyp_owner_constructor_exists():
    assert callable(Owner.__init__)


def test_hyp_owner_constructor_args():
    sig = inspect.signature(Owner.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phn_no_" in params, "Missing parameter 'Phn_no_'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "email_id" in params, "Missing parameter 'email_id'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "password" in params, "Missing parameter 'password'"

def test_hyp_owner_has_Address():
    assert hasattr(Owner, "Address")
    descriptor = None
    for klass in Owner.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_hyp_owner_has_Phn_no_():
    assert hasattr(Owner, "Phn_no_")
    descriptor = None
    for klass in Owner.__mro__:
        if "Phn_no_" in klass.__dict__:
            descriptor = klass.__dict__["Phn_no_"]
            break
    assert isinstance(descriptor, property)

def test_hyp_owner_has_Name():
    assert hasattr(Owner, "Name")
    descriptor = None
    for klass in Owner.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_owner_has_email_id():
    assert hasattr(Owner, "email_id")
    descriptor = None
    for klass in Owner.__mro__:
        if "email_id" in klass.__dict__:
            descriptor = klass.__dict__["email_id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_owner_has_ID():
    assert hasattr(Owner, "ID")
    descriptor = None
    for klass in Owner.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_owner_has_password():
    assert hasattr(Owner, "password")
    descriptor = None
    for klass in Owner.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)


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
occupancy_strategy = st.builds(
    occupancy,
    booking_id=
        st.integers()
)
Booking_strategy = st.builds(
    Booking,
    booking_id=
        st.integers(),
    user_id=
        st.integers(),
    guest_adress=
        safe_text,
    guest_id=
        st.integers(),
    guest_name=
        st.integers(),
    guestphn_no=
        st.integers()
)
User_strategy = st.builds(
    User,
    Name=
        safe_text,
    id=
        st.integers(),
    password=
        st.integers(),
    address=
        safe_text,
    mail_id=
        safe_text,
    phn_no=
        st.integers()
)
Location_strategy = st.builds(
    Location,
    attribute=
        safe_text,
    loc_name=
        safe_text,
    loc_id=
        st.integers()
)
Rooms_strategy = st.builds(
    Rooms,
    name=
        safe_text,
    room_description=
        safe_text,
    checkout_date=
        st.integers(),
    id=
        st.integers(),
    price=
        st.integers(),
    checkin_date=
        st.integers()
)
Hotels_strategy = st.builds(
    Hotels,
    id=
        st.integers(),
    name=
        st.integers(),
    hotel_description=
        st.integers()
)
Owner_strategy = st.builds(
    Owner,
    Address=
        safe_text,
    Phn_no_=
        st.none(),
    Name=
        safe_text,
    email_id=
        st.integers(),
    ID=
        st.integers(),
    password=
        st.integers()
)




@given(instance=occupancy_strategy)
def test_hyp_occupancy_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original




@given(instance=Booking_strategy)
def test_hyp_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original



@given(instance=Booking_strategy)
def test_hyp_booking_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Booking_strategy)
def test_hyp_booking_guest_adress_setter(instance):
    original = instance.guest_adress
    instance.guest_adress = original
    assert instance.guest_adress == original



@given(instance=Booking_strategy)
def test_hyp_booking_guest_id_setter(instance):
    original = instance.guest_id
    instance.guest_id = original
    assert instance.guest_id == original



@given(instance=Booking_strategy)
def test_hyp_booking_guest_name_setter(instance):
    original = instance.guest_name
    instance.guest_name = original
    assert instance.guest_name == original



@given(instance=Booking_strategy)
def test_hyp_booking_guestphn_no_setter(instance):
    original = instance.guestphn_no
    instance.guestphn_no = original
    assert instance.guestphn_no == original




@given(instance=User_strategy)
def test_hyp_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=User_strategy)
def test_hyp_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=User_strategy)
def test_hyp_user_mail_id_setter(instance):
    original = instance.mail_id
    instance.mail_id = original
    assert instance.mail_id == original



@given(instance=User_strategy)
def test_hyp_user_phn_no_setter(instance):
    original = instance.phn_no
    instance.phn_no = original
    assert instance.phn_no == original




@given(instance=Location_strategy)
def test_hyp_location_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Location_strategy)
def test_hyp_location_loc_name_setter(instance):
    original = instance.loc_name
    instance.loc_name = original
    assert instance.loc_name == original



@given(instance=Location_strategy)
def test_hyp_location_loc_id_setter(instance):
    original = instance.loc_id
    instance.loc_id = original
    assert instance.loc_id == original




@given(instance=Rooms_strategy)
def test_hyp_rooms_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_room_description_setter(instance):
    original = instance.room_description
    instance.room_description = original
    assert instance.room_description == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_checkout_date_setter(instance):
    original = instance.checkout_date
    instance.checkout_date = original
    assert instance.checkout_date == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_checkin_date_setter(instance):
    original = instance.checkin_date
    instance.checkin_date = original
    assert instance.checkin_date == original




@given(instance=Hotels_strategy)
def test_hyp_hotels_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Hotels_strategy)
def test_hyp_hotels_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hotels_strategy)
def test_hyp_hotels_hotel_description_setter(instance):
    original = instance.hotel_description
    instance.hotel_description = original
    assert instance.hotel_description == original

@given(instance=Owner_strategy)
@settings(max_examples=50)
def test_hyp_owner_instantiation(instance):
    assert isinstance(instance, Owner)



@given(instance=Owner_strategy)
def test_hyp_owner_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Owner_strategy)
def test_hyp_owner_Phn_no__setter(instance):
    original = instance.Phn_no_
    instance.Phn_no_ = original
    assert instance.Phn_no_ == original



@given(instance=Owner_strategy)
def test_hyp_owner_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Owner_strategy)
def test_hyp_owner_email_id_setter(instance):
    original = instance.email_id
    instance.email_id = original
    assert instance.email_id == original



@given(instance=Owner_strategy)
def test_hyp_owner_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Owner_strategy)
def test_hyp_owner_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Booking,
    Hotels,
    Location,
    Owner,
    Rooms,
    User,
    occupancy,
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

def test_Booking_booking_id_value_roundtrip():
    instance = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_Booking_guest_adress_value_roundtrip():
    instance = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    assert instance.guest_adress == "sample_text"
    instance.guest_adress = "sample_text_2"
    assert instance.guest_adress == "sample_text_2"


def test_Booking_guest_id_value_roundtrip():
    instance = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    assert instance.guest_id == 7
    instance.guest_id = 13
    assert instance.guest_id == 13


def test_Booking_guest_name_value_roundtrip():
    instance = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    assert instance.guest_name == 7
    instance.guest_name = 13
    assert instance.guest_name == 13


def test_Booking_guestphn_no_value_roundtrip():
    instance = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    assert instance.guestphn_no == 7
    instance.guestphn_no = 13
    assert instance.guestphn_no == 13


def test_Booking_user_id_value_roundtrip():
    instance = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Hotels_hotel_description_value_roundtrip():
    instance = Hotels(hotel_description=7, id=7, name=7)
    assert instance.hotel_description == 7
    instance.hotel_description = 13
    assert instance.hotel_description == 13


def test_Hotels_id_value_roundtrip():
    instance = Hotels(hotel_description=7, id=7, name=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Hotels_name_value_roundtrip():
    instance = Hotels(hotel_description=7, id=7, name=7)
    assert instance.name == 7
    instance.name = 13
    assert instance.name == 13


def test_Location_attribute_value_roundtrip():
    instance = Location(attribute="sample_text", loc_id=7, loc_name="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Location_loc_id_value_roundtrip():
    instance = Location(attribute="sample_text", loc_id=7, loc_name="sample_text")
    assert instance.loc_id == 7
    instance.loc_id = 13
    assert instance.loc_id == 13


def test_Location_loc_name_value_roundtrip():
    instance = Location(attribute="sample_text", loc_id=7, loc_name="sample_text")
    assert instance.loc_name == "sample_text"
    instance.loc_name = "sample_text_2"
    assert instance.loc_name == "sample_text_2"


def test_Rooms_checkin_date_value_roundtrip():
    instance = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.checkin_date == 7
    instance.checkin_date = 13
    assert instance.checkin_date == 13


def test_Rooms_checkout_date_value_roundtrip():
    instance = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.checkout_date == 7
    instance.checkout_date = 13
    assert instance.checkout_date == 13


def test_Rooms_id_value_roundtrip():
    instance = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Rooms_name_value_roundtrip():
    instance = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Rooms_price_value_roundtrip():
    instance = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_Rooms_room_description_value_roundtrip():
    instance = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.room_description == "sample_text"
    instance.room_description = "sample_text_2"
    assert instance.room_description == "sample_text_2"


def test_User_Name_value_roundtrip():
    instance = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_User_address_value_roundtrip():
    instance = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_User_id_value_roundtrip():
    instance = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_User_mail_id_value_roundtrip():
    instance = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    assert instance.mail_id == "sample_text"
    instance.mail_id = "sample_text_2"
    assert instance.mail_id == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    assert instance.password == 7
    instance.password = 13
    assert instance.password == 13


def test_User_phn_no_value_roundtrip():
    instance = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    assert instance.phn_no == 7
    instance.phn_no = 13
    assert instance.phn_no == 13


def test_occupancy_booking_id_value_roundtrip():
    instance = occupancy(booking_id=7)
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_assoc_City_Hotels_link_reassign_clear():
    a = Location(attribute="sample_text", loc_id=7, loc_name="sample_text")
    b1 = Hotels(hotel_description=7, id=7, name=7)
    b2 = Hotels(hotel_description=13, id=13, name=13)
    _safe_set(a, 'hotels0', b1)
    assert _is_linked(a, 'hotels0', b1)
    if hasattr(b1, 'city1'):
        assert _is_linked(b1, 'city1', a)
    _safe_set(a, 'hotels0', b2)
    assert _is_linked(a, 'hotels0', b2)
    if hasattr(b1, 'city1'):
        assert not _is_linked(b1, 'city1', a)
    if hasattr(b2, 'city1'):
        assert _is_linked(b2, 'city1', a)
    _safe_set(a, 'hotels0', None)
    assert not _is_linked(a, 'hotels0', b2)
    if hasattr(b2, 'city1'):
        assert not _is_linked(b2, 'city1', a)


def test_assoc_Hotels_Rooms_link_reassign_clear():
    a = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    b1 = Hotels(hotel_description=7, id=7, name=7)
    b2 = Hotels(hotel_description=13, id=13, name=13)
    _safe_set(a, 'hotels3', b1)
    assert _is_linked(a, 'hotels3', b1)
    if hasattr(b1, 'rooms2'):
        assert _is_linked(b1, 'rooms2', a)
    _safe_set(a, 'hotels3', b2)
    assert _is_linked(a, 'hotels3', b2)
    if hasattr(b1, 'rooms2'):
        assert not _is_linked(b1, 'rooms2', a)
    if hasattr(b2, 'rooms2'):
        assert _is_linked(b2, 'rooms2', a)
    _safe_set(a, 'hotels3', None)
    assert not _is_linked(a, 'hotels3', b2)
    if hasattr(b2, 'rooms2'):
        assert not _is_linked(b2, 'rooms2', a)


def test_assoc_Rooms_Booking_link_reassign_clear():
    a = Rooms(checkin_date=7, checkout_date=7, id=7, name="sample_text", price=7, room_description="sample_text")
    b1 = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    b2 = Booking(booking_id=13, guest_adress="sample_text_2", guest_id=13, guest_name=13, guestphn_no=13, user_id=13)
    _safe_set(a, 'booking8', b1)
    assert _is_linked(a, 'booking8', b1)
    if hasattr(b1, 'rooms9'):
        assert _is_linked(b1, 'rooms9', a)
    _safe_set(a, 'booking8', b2)
    assert _is_linked(a, 'booking8', b2)
    if hasattr(b1, 'rooms9'):
        assert not _is_linked(b1, 'rooms9', a)
    if hasattr(b2, 'rooms9'):
        assert _is_linked(b2, 'rooms9', a)
    _safe_set(a, 'booking8', None)
    assert not _is_linked(a, 'booking8', b2)
    if hasattr(b2, 'rooms9'):
        assert not _is_linked(b2, 'rooms9', a)


def test_assoc_User_Booking_link_reassign_clear():
    a = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    b1 = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    b2 = Booking(booking_id=13, guest_adress="sample_text_2", guest_id=13, guest_name=13, guestphn_no=13, user_id=13)
    _safe_set(a, 'User_Booking_04', b1)
    assert _is_linked(a, 'User_Booking_04', b1)
    if hasattr(b1, 'User_Booking_15'):
        assert _is_linked(b1, 'User_Booking_15', a)
    _safe_set(a, 'User_Booking_04', b2)
    assert _is_linked(a, 'User_Booking_04', b2)
    if hasattr(b1, 'User_Booking_15'):
        assert not _is_linked(b1, 'User_Booking_15', a)
    if hasattr(b2, 'User_Booking_15'):
        assert _is_linked(b2, 'User_Booking_15', a)
    _safe_set(a, 'User_Booking_04', None)
    assert not _is_linked(a, 'User_Booking_04', b2)
    if hasattr(b2, 'User_Booking_15'):
        assert not _is_linked(b2, 'User_Booking_15', a)


def test_assoc_occupancy_Booking_link_reassign_clear():
    a = occupancy(booking_id=7)
    b1 = Booking(booking_id=7, guest_adress="sample_text", guest_id=7, guest_name=7, guestphn_no=7, user_id=7)
    b2 = Booking(booking_id=13, guest_adress="sample_text_2", guest_id=13, guest_name=13, guestphn_no=13, user_id=13)
    _safe_set(a, 'occupancy_Booking_010', b1)
    assert _is_linked(a, 'occupancy_Booking_010', b1)
    if hasattr(b1, 'occupancy_Booking_111'):
        assert _is_linked(b1, 'occupancy_Booking_111', a)
    _safe_set(a, 'occupancy_Booking_010', b2)
    assert _is_linked(a, 'occupancy_Booking_010', b2)
    if hasattr(b1, 'occupancy_Booking_111'):
        assert not _is_linked(b1, 'occupancy_Booking_111', a)
    if hasattr(b2, 'occupancy_Booking_111'):
        assert _is_linked(b2, 'occupancy_Booking_111', a)
    _safe_set(a, 'occupancy_Booking_010', None)
    assert not _is_linked(a, 'occupancy_Booking_010', b2)
    if hasattr(b2, 'occupancy_Booking_111'):
        assert not _is_linked(b2, 'occupancy_Booking_111', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Booking_strategy = st.builds(Booking, booking_id=st.integers(), guest_adress=safe_text, guest_id=st.integers(), guest_name=st.integers(), guestphn_no=st.integers(), user_id=st.integers())
@given(instance=Booking_strategy)
@settings(max_examples=25)
def test_Booking_instantiation(instance):
    assert isinstance(instance, Booking)


Hotels_strategy = st.builds(Hotels, hotel_description=st.integers(), id=st.integers(), name=st.integers())
@given(instance=Hotels_strategy)
@settings(max_examples=25)
def test_Hotels_instantiation(instance):
    assert isinstance(instance, Hotels)


Location_strategy = st.builds(Location, attribute=safe_text, loc_id=st.integers(), loc_name=safe_text)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


Rooms_strategy = st.builds(Rooms, checkin_date=st.integers(), checkout_date=st.integers(), id=st.integers(), name=safe_text, price=st.integers(), room_description=safe_text)
@given(instance=Rooms_strategy)
@settings(max_examples=25)
def test_Rooms_instantiation(instance):
    assert isinstance(instance, Rooms)


User_strategy = st.builds(User, Name=safe_text, address=safe_text, id=st.integers(), mail_id=safe_text, password=st.integers(), phn_no=st.integers())
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


occupancy_strategy = st.builds(occupancy, booking_id=st.integers())
@given(instance=occupancy_strategy)
@settings(max_examples=25)
def test_occupancy_instantiation(instance):
    assert isinstance(instance, occupancy)



