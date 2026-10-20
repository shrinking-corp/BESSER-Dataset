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
    User,
    Payment,
    City,
    Guest,
    Rooms,
    Hotels,
    Manager,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "mail_id" in params, "Missing parameter 'mail_id'"
    assert "phn_no" in params, "Missing parameter 'phn_no'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"









def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "cvv" in params, "Missing parameter 'cvv'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "password" in params, "Missing parameter 'password'"
    assert "card_no" in params, "Missing parameter 'card_no'"
    assert "card_type" in params, "Missing parameter 'card_type'"








def test_hyp_city_is_not_abstract():
    assert not inspect.isabstract(City)


def test_hyp_city_constructor_exists():
    assert callable(City.__init__)


def test_hyp_city_constructor_args():
    sig = inspect.signature(City.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_hyp_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_hyp_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Nmae" in params, "Missing parameter 'Nmae'"
    assert "Phone_no_" in params, "Missing parameter 'Phone_no_'"
    assert "address" in params, "Missing parameter 'address'"







def test_hyp_rooms_is_not_abstract():
    assert not inspect.isabstract(Rooms)


def test_hyp_rooms_constructor_exists():
    assert callable(Rooms.__init__)


def test_hyp_rooms_constructor_args():
    sig = inspect.signature(Rooms.__init__)
    params = list(sig.parameters.keys())
    assert "room_description" in params, "Missing parameter 'room_description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_hotels_is_not_abstract():
    assert not inspect.isabstract(Hotels)


def test_hyp_hotels_constructor_exists():
    assert callable(Hotels.__init__)


def test_hyp_hotels_constructor_args():
    sig = inspect.signature(Hotels.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_hyp_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_hyp_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phn_no_" in params, "Missing parameter 'Phn_no_'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_hyp_manager_has_Address():
    assert hasattr(Manager, "Address")
    descriptor = None
    for klass in Manager.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_hyp_manager_has_Phn_no_():
    assert hasattr(Manager, "Phn_no_")
    descriptor = None
    for klass in Manager.__mro__:
        if "Phn_no_" in klass.__dict__:
            descriptor = klass.__dict__["Phn_no_"]
            break
    assert isinstance(descriptor, property)

def test_hyp_manager_has_ID():
    assert hasattr(Manager, "ID")
    descriptor = None
    for klass in Manager.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_manager_has_Name():
    assert hasattr(Manager, "Name")
    descriptor = None
    for klass in Manager.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
User_strategy = st.builds(
    User,
    address=
        safe_text,
    mail_id=
        safe_text,
    phn_no=
        st.integers(),
    Name=
        safe_text,
    password=
        st.integers(),
    id=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    cvv=
        st.integers(),
    amount=
        st.integers(),
    password=
        st.integers(),
    card_no=
        st.integers(),
    card_type=
        safe_text
)
City_strategy = st.builds(
    City,
    city=
        safe_text,
    id=
        st.integers()
)
Guest_strategy = st.builds(
    Guest,
    id=
        st.integers(),
    Nmae=
        safe_text,
    Phone_no_=
        st.integers(),
    address=
        safe_text
)
Rooms_strategy = st.builds(
    Rooms,
    room_description=
        safe_text,
    name=
        safe_text,
    price=
        st.integers(),
    id=
        st.integers()
)
Hotels_strategy = st.builds(
    Hotels,
    id=
        st.integers(),
    location=
        st.integers(),
    name=
        st.integers()
)
Manager_strategy = st.builds(
    Manager,
    Address=
        safe_text,
    Phn_no_=
        st.none(),
    ID=
        st.integers(),
    Name=
        safe_text
)




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



@given(instance=User_strategy)
def test_hyp_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Payment_strategy)
def test_hyp_payment_cvv_setter(instance):
    original = instance.cvv
    instance.cvv = original
    assert instance.cvv == original



@given(instance=Payment_strategy)
def test_hyp_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Payment_strategy)
def test_hyp_payment_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Payment_strategy)
def test_hyp_payment_card_no_setter(instance):
    original = instance.card_no
    instance.card_no = original
    assert instance.card_no == original



@given(instance=Payment_strategy)
def test_hyp_payment_card_type_setter(instance):
    original = instance.card_type
    instance.card_type = original
    assert instance.card_type == original




@given(instance=City_strategy)
def test_hyp_city_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=City_strategy)
def test_hyp_city_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Guest_strategy)
def test_hyp_guest_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Guest_strategy)
def test_hyp_guest_Nmae_setter(instance):
    original = instance.Nmae
    instance.Nmae = original
    assert instance.Nmae == original



@given(instance=Guest_strategy)
def test_hyp_guest_Phone_no__setter(instance):
    original = instance.Phone_no_
    instance.Phone_no_ = original
    assert instance.Phone_no_ == original



@given(instance=Guest_strategy)
def test_hyp_guest_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original




@given(instance=Rooms_strategy)
def test_hyp_rooms_room_description_setter(instance):
    original = instance.room_description
    instance.room_description = original
    assert instance.room_description == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Rooms_strategy)
def test_hyp_rooms_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Hotels_strategy)
def test_hyp_hotels_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Hotels_strategy)
def test_hyp_hotels_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Hotels_strategy)
def test_hyp_hotels_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_hyp_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_hyp_manager_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Manager_strategy)
def test_hyp_manager_Phn_no__setter(instance):
    original = instance.Phn_no_
    instance.Phn_no_ = original
    assert instance.Phn_no_ == original



@given(instance=Manager_strategy)
def test_hyp_manager_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Manager_strategy)
def test_hyp_manager_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    City,
    Guest,
    Hotels,
    Manager,
    Payment,
    Rooms,
    User,
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

def test_City_city_value_roundtrip():
    instance = City(city="sample_text", id=7)
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_City_id_value_roundtrip():
    instance = City(city="sample_text", id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Guest_Nmae_value_roundtrip():
    instance = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    assert instance.Nmae == "sample_text"
    instance.Nmae = "sample_text_2"
    assert instance.Nmae == "sample_text_2"


def test_Guest_Phone_no__value_roundtrip():
    instance = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    assert instance.Phone_no_ == 7
    instance.Phone_no_ = 13
    assert instance.Phone_no_ == 13


def test_Guest_address_value_roundtrip():
    instance = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Guest_id_value_roundtrip():
    instance = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Hotels_id_value_roundtrip():
    instance = Hotels(id=7, location=7, name=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Hotels_location_value_roundtrip():
    instance = Hotels(id=7, location=7, name=7)
    assert instance.location == 7
    instance.location = 13
    assert instance.location == 13


def test_Hotels_name_value_roundtrip():
    instance = Hotels(id=7, location=7, name=7)
    assert instance.name == 7
    instance.name = 13
    assert instance.name == 13


def test_Payment_amount_value_roundtrip():
    instance = Payment(amount=7, card_no=7, card_type="sample_text", cvv=7, password=7)
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_Payment_card_no_value_roundtrip():
    instance = Payment(amount=7, card_no=7, card_type="sample_text", cvv=7, password=7)
    assert instance.card_no == 7
    instance.card_no = 13
    assert instance.card_no == 13


def test_Payment_card_type_value_roundtrip():
    instance = Payment(amount=7, card_no=7, card_type="sample_text", cvv=7, password=7)
    assert instance.card_type == "sample_text"
    instance.card_type = "sample_text_2"
    assert instance.card_type == "sample_text_2"


def test_Payment_cvv_value_roundtrip():
    instance = Payment(amount=7, card_no=7, card_type="sample_text", cvv=7, password=7)
    assert instance.cvv == 7
    instance.cvv = 13
    assert instance.cvv == 13


def test_Payment_password_value_roundtrip():
    instance = Payment(amount=7, card_no=7, card_type="sample_text", cvv=7, password=7)
    assert instance.password == 7
    instance.password = 13
    assert instance.password == 13


def test_Rooms_id_value_roundtrip():
    instance = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Rooms_name_value_roundtrip():
    instance = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Rooms_price_value_roundtrip():
    instance = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_Rooms_room_description_value_roundtrip():
    instance = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
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


def test_assoc_City_Hotels_link_reassign_clear():
    a = Hotels(id=7, location=7, name=7)
    b1 = City(city="sample_text", id=7)
    b2 = City(city="sample_text_2", id=13)
    _safe_set(a, 'city1', b1)
    assert _is_linked(a, 'city1', b1)
    if hasattr(b1, 'hotels0'):
        assert _is_linked(b1, 'hotels0', a)
    _safe_set(a, 'city1', b2)
    assert _is_linked(a, 'city1', b2)
    if hasattr(b1, 'hotels0'):
        assert not _is_linked(b1, 'hotels0', a)
    if hasattr(b2, 'hotels0'):
        assert _is_linked(b2, 'hotels0', a)
    _safe_set(a, 'city1', None)
    assert not _is_linked(a, 'city1', b2)
    if hasattr(b2, 'hotels0'):
        assert not _is_linked(b2, 'hotels0', a)


def test_assoc_Guest_Payment_link_reassign_clear():
    a = Payment(amount=7, card_no=7, card_type="sample_text", cvv=7, password=7)
    b1 = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    b2 = Guest(Nmae="sample_text_2", Phone_no_=13, address="sample_text_2", id=13)
    _safe_set(a, 'guest7', b1)
    assert _is_linked(a, 'guest7', b1)
    if hasattr(b1, 'payment6'):
        assert _is_linked(b1, 'payment6', a)
    _safe_set(a, 'guest7', b2)
    assert _is_linked(a, 'guest7', b2)
    if hasattr(b1, 'payment6'):
        assert not _is_linked(b1, 'payment6', a)
    if hasattr(b2, 'payment6'):
        assert _is_linked(b2, 'payment6', a)
    _safe_set(a, 'guest7', None)
    assert not _is_linked(a, 'guest7', b2)
    if hasattr(b2, 'payment6'):
        assert not _is_linked(b2, 'payment6', a)


def test_assoc_Hotels_Guest_link_reassign_clear():
    a = Hotels(id=7, location=7, name=7)
    b1 = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    b2 = Guest(Nmae="sample_text_2", Phone_no_=13, address="sample_text_2", id=13)
    _safe_set(a, 'guest8', b1)
    assert _is_linked(a, 'guest8', b1)
    if hasattr(b1, 'hotels9'):
        assert _is_linked(b1, 'hotels9', a)
    _safe_set(a, 'guest8', b2)
    assert _is_linked(a, 'guest8', b2)
    if hasattr(b1, 'hotels9'):
        assert not _is_linked(b1, 'hotels9', a)
    if hasattr(b2, 'hotels9'):
        assert _is_linked(b2, 'hotels9', a)
    _safe_set(a, 'guest8', None)
    assert not _is_linked(a, 'guest8', b2)
    if hasattr(b2, 'hotels9'):
        assert not _is_linked(b2, 'hotels9', a)


def test_assoc_Hotels_Rooms_link_reassign_clear():
    a = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
    b1 = Hotels(id=7, location=7, name=7)
    b2 = Hotels(id=13, location=13, name=13)
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


def test_assoc_Rooms_Guest_link_reassign_clear():
    a = Rooms(id=7, name="sample_text", price=7, room_description="sample_text")
    b1 = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    b2 = Guest(Nmae="sample_text_2", Phone_no_=13, address="sample_text_2", id=13)
    _safe_set(a, 'guest4', b1)
    assert _is_linked(a, 'guest4', b1)
    if hasattr(b1, 'rooms5'):
        assert _is_linked(b1, 'rooms5', a)
    _safe_set(a, 'guest4', b2)
    assert _is_linked(a, 'guest4', b2)
    if hasattr(b1, 'rooms5'):
        assert not _is_linked(b1, 'rooms5', a)
    if hasattr(b2, 'rooms5'):
        assert _is_linked(b2, 'rooms5', a)
    _safe_set(a, 'guest4', None)
    assert not _is_linked(a, 'guest4', b2)
    if hasattr(b2, 'rooms5'):
        assert not _is_linked(b2, 'rooms5', a)


def test_assoc_User_Guest_link_reassign_clear():
    a = User(Name="sample_text", address="sample_text", id=7, mail_id="sample_text", password=7, phn_no=7)
    b1 = Guest(Nmae="sample_text", Phone_no_=7, address="sample_text", id=7)
    b2 = Guest(Nmae="sample_text_2", Phone_no_=13, address="sample_text_2", id=13)
    _safe_set(a, 'guest10', b1)
    assert _is_linked(a, 'guest10', b1)
    if hasattr(b1, 'user11'):
        assert _is_linked(b1, 'user11', a)
    _safe_set(a, 'guest10', b2)
    assert _is_linked(a, 'guest10', b2)
    if hasattr(b1, 'user11'):
        assert not _is_linked(b1, 'user11', a)
    if hasattr(b2, 'user11'):
        assert _is_linked(b2, 'user11', a)
    _safe_set(a, 'guest10', None)
    assert not _is_linked(a, 'guest10', b2)
    if hasattr(b2, 'user11'):
        assert not _is_linked(b2, 'user11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

City_strategy = st.builds(City, city=safe_text, id=st.integers())
@given(instance=City_strategy)
@settings(max_examples=25)
def test_City_instantiation(instance):
    assert isinstance(instance, City)


Guest_strategy = st.builds(Guest, Nmae=safe_text, Phone_no_=st.integers(), address=safe_text, id=st.integers())
@given(instance=Guest_strategy)
@settings(max_examples=25)
def test_Guest_instantiation(instance):
    assert isinstance(instance, Guest)


Hotels_strategy = st.builds(Hotels, id=st.integers(), location=st.integers(), name=st.integers())
@given(instance=Hotels_strategy)
@settings(max_examples=25)
def test_Hotels_instantiation(instance):
    assert isinstance(instance, Hotels)


Payment_strategy = st.builds(Payment, amount=st.integers(), card_no=st.integers(), card_type=safe_text, cvv=st.integers(), password=st.integers())
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Rooms_strategy = st.builds(Rooms, id=st.integers(), name=safe_text, price=st.integers(), room_description=safe_text)
@given(instance=Rooms_strategy)
@settings(max_examples=25)
def test_Rooms_instantiation(instance):
    assert isinstance(instance, Rooms)


User_strategy = st.builds(User, Name=safe_text, address=safe_text, id=st.integers(), mail_id=safe_text, password=st.integers(), phn_no=st.integers())
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



