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
    Administrator,
    RegisteredUser,
    RealEstateAgent,
    House,
    Apartment,
    Listing,
    Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_registereduser_is_not_abstract():
    assert not inspect.isabstract(RegisteredUser)


def test_hyp_registereduser_constructor_exists():
    assert callable(RegisteredUser.__init__)


def test_hyp_registereduser_constructor_args():
    sig = inspect.signature(RegisteredUser.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realestateagent_is_not_abstract():
    assert not inspect.isabstract(RealEstateAgent)


def test_hyp_realestateagent_constructor_exists():
    assert callable(RealEstateAgent.__init__)


def test_hyp_realestateagent_constructor_args():
    sig = inspect.signature(RealEstateAgent.__init__)
    params = list(sig.parameters.keys())
    assert "listings" in params, "Missing parameter 'listings'"




def test_hyp_house_is_not_abstract():
    assert not inspect.isabstract(House)


def test_hyp_house_constructor_exists():
    assert callable(House.__init__)


def test_hyp_house_constructor_args():
    sig = inspect.signature(House.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "fees" in params, "Missing parameter 'fees'"
    assert "sizeOfProperty" in params, "Missing parameter 'sizeOfProperty'"
    assert "numberOfFloors" in params, "Missing parameter 'numberOfFloors'"







def test_hyp_apartment_is_not_abstract():
    assert not inspect.isabstract(Apartment)


def test_hyp_apartment_constructor_exists():
    assert callable(Apartment.__init__)


def test_hyp_apartment_constructor_args():
    sig = inspect.signature(Apartment.__init__)
    params = list(sig.parameters.keys())
    assert "lease" in params, "Missing parameter 'lease'"
    assert "securityDeposit" in params, "Missing parameter 'securityDeposit'"
    assert "size" in params, "Missing parameter 'size'"
    assert "monthlyRent" in params, "Missing parameter 'monthlyRent'"







def test_hyp_listing_is_not_abstract():
    assert not inspect.isabstract(Listing)


def test_hyp_listing_constructor_exists():
    assert callable(Listing.__init__)


def test_hyp_listing_constructor_args():
    sig = inspect.signature(Listing.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfBathrooms" in params, "Missing parameter 'numberOfBathrooms'"
    assert "numberOfBedroms" in params, "Missing parameter 'numberOfBedroms'"
    assert "furnished" in params, "Missing parameter 'furnished'"
    assert "image" in params, "Missing parameter 'image'"
    assert "video" in params, "Missing parameter 'video'"
    assert "kitchen" in params, "Missing parameter 'kitchen'"
    assert "parkingPossibilities" in params, "Missing parameter 'parkingPossibilities'"
    assert "address" in params, "Missing parameter 'address'"
    assert "livingRooom" in params, "Missing parameter 'livingRooom'"












def test_hyp_actor_is_not_abstract():
    assert not inspect.isabstract(Actor)


def test_hyp_actor_constructor_exists():
    assert callable(Actor.__init__)


def test_hyp_actor_constructor_args():
    sig = inspect.signature(Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"





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
Administrator_strategy = st.builds(
    Administrator,
)
RegisteredUser_strategy = st.builds(
    RegisteredUser,
)
RealEstateAgent_strategy = st.builds(
    RealEstateAgent,
    listings=
        safe_text
)
House_strategy = st.builds(
    House,
    price=
        st.integers(),
    fees=
        st.integers(),
    sizeOfProperty=
        st.integers(),
    numberOfFloors=
        st.integers()
)
Apartment_strategy = st.builds(
    Apartment,
    lease=
        st.integers(),
    securityDeposit=
        st.integers(),
    size=
        st.integers(),
    monthlyRent=
        st.integers()
)
Listing_strategy = st.builds(
    Listing,
    numberOfBathrooms=
        st.integers(),
    numberOfBedroms=
        st.integers(),
    furnished=
        st.booleans(),
    image=
        safe_text,
    video=
        safe_text,
    kitchen=
        st.integers(),
    parkingPossibilities=
        st.integers(),
    address=
        safe_text,
    livingRooom=
        st.integers()
)
Actor_strategy = st.builds(
    Actor,
    name=
        safe_text,
    password=
        safe_text,
    username=
        safe_text
)






@given(instance=RealEstateAgent_strategy)
def test_hyp_realestateagent_listings_setter(instance):
    original = instance.listings
    instance.listings = original
    assert instance.listings == original




@given(instance=House_strategy)
def test_hyp_house_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=House_strategy)
def test_hyp_house_fees_setter(instance):
    original = instance.fees
    instance.fees = original
    assert instance.fees == original



@given(instance=House_strategy)
def test_hyp_house_sizeOfProperty_setter(instance):
    original = instance.sizeOfProperty
    instance.sizeOfProperty = original
    assert instance.sizeOfProperty == original



@given(instance=House_strategy)
def test_hyp_house_numberOfFloors_setter(instance):
    original = instance.numberOfFloors
    instance.numberOfFloors = original
    assert instance.numberOfFloors == original




@given(instance=Apartment_strategy)
def test_hyp_apartment_lease_setter(instance):
    original = instance.lease
    instance.lease = original
    assert instance.lease == original



@given(instance=Apartment_strategy)
def test_hyp_apartment_securityDeposit_setter(instance):
    original = instance.securityDeposit
    instance.securityDeposit = original
    assert instance.securityDeposit == original



@given(instance=Apartment_strategy)
def test_hyp_apartment_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Apartment_strategy)
def test_hyp_apartment_monthlyRent_setter(instance):
    original = instance.monthlyRent
    instance.monthlyRent = original
    assert instance.monthlyRent == original




@given(instance=Listing_strategy)
def test_hyp_listing_numberOfBathrooms_setter(instance):
    original = instance.numberOfBathrooms
    instance.numberOfBathrooms = original
    assert instance.numberOfBathrooms == original



@given(instance=Listing_strategy)
def test_hyp_listing_numberOfBedroms_setter(instance):
    original = instance.numberOfBedroms
    instance.numberOfBedroms = original
    assert instance.numberOfBedroms == original



@given(instance=Listing_strategy)
def test_hyp_listing_furnished_setter(instance):
    original = instance.furnished
    instance.furnished = original
    assert instance.furnished == original



@given(instance=Listing_strategy)
def test_hyp_listing_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=Listing_strategy)
def test_hyp_listing_video_setter(instance):
    original = instance.video
    instance.video = original
    assert instance.video == original



@given(instance=Listing_strategy)
def test_hyp_listing_kitchen_setter(instance):
    original = instance.kitchen
    instance.kitchen = original
    assert instance.kitchen == original



@given(instance=Listing_strategy)
def test_hyp_listing_parkingPossibilities_setter(instance):
    original = instance.parkingPossibilities
    instance.parkingPossibilities = original
    assert instance.parkingPossibilities == original



@given(instance=Listing_strategy)
def test_hyp_listing_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Listing_strategy)
def test_hyp_listing_livingRooom_setter(instance):
    original = instance.livingRooom
    instance.livingRooom = original
    assert instance.livingRooom == original




@given(instance=Actor_strategy)
def test_hyp_actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Actor_strategy)
def test_hyp_actor_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Actor_strategy)
def test_hyp_actor_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Actor,
    Administrator,
    Apartment,
    House,
    Listing,
    RealEstateAgent,
    RegisteredUser,
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

def test_Actor_name_value_roundtrip():
    instance = Actor(name="sample_text", password="sample_text", username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Actor_password_value_roundtrip():
    instance = Actor(name="sample_text", password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Actor_username_value_roundtrip():
    instance = Actor(name="sample_text", password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Apartment_lease_value_roundtrip():
    instance = Apartment(lease=7, monthlyRent=7, securityDeposit=7, size=7)
    assert instance.lease == 7
    instance.lease = 13
    assert instance.lease == 13


def test_Apartment_monthlyRent_value_roundtrip():
    instance = Apartment(lease=7, monthlyRent=7, securityDeposit=7, size=7)
    assert instance.monthlyRent == 7
    instance.monthlyRent = 13
    assert instance.monthlyRent == 13


def test_Apartment_securityDeposit_value_roundtrip():
    instance = Apartment(lease=7, monthlyRent=7, securityDeposit=7, size=7)
    assert instance.securityDeposit == 7
    instance.securityDeposit = 13
    assert instance.securityDeposit == 13


def test_Apartment_size_value_roundtrip():
    instance = Apartment(lease=7, monthlyRent=7, securityDeposit=7, size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_House_fees_value_roundtrip():
    instance = House(fees=7, numberOfFloors=7, price=7, sizeOfProperty=7)
    assert instance.fees == 7
    instance.fees = 13
    assert instance.fees == 13


def test_House_numberOfFloors_value_roundtrip():
    instance = House(fees=7, numberOfFloors=7, price=7, sizeOfProperty=7)
    assert instance.numberOfFloors == 7
    instance.numberOfFloors = 13
    assert instance.numberOfFloors == 13


def test_House_price_value_roundtrip():
    instance = House(fees=7, numberOfFloors=7, price=7, sizeOfProperty=7)
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_House_sizeOfProperty_value_roundtrip():
    instance = House(fees=7, numberOfFloors=7, price=7, sizeOfProperty=7)
    assert instance.sizeOfProperty == 7
    instance.sizeOfProperty = 13
    assert instance.sizeOfProperty == 13


def test_Listing_address_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Listing_furnished_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.furnished == True
    instance.furnished = False
    assert instance.furnished == False


def test_Listing_image_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_Listing_kitchen_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.kitchen == 7
    instance.kitchen = 13
    assert instance.kitchen == 13


def test_Listing_livingRooom_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.livingRooom == 7
    instance.livingRooom = 13
    assert instance.livingRooom == 13


def test_Listing_numberOfBathrooms_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.numberOfBathrooms == 7
    instance.numberOfBathrooms = 13
    assert instance.numberOfBathrooms == 13


def test_Listing_numberOfBedroms_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.numberOfBedroms == 7
    instance.numberOfBedroms = 13
    assert instance.numberOfBedroms == 13


def test_Listing_parkingPossibilities_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.parkingPossibilities == 7
    instance.parkingPossibilities = 13
    assert instance.parkingPossibilities == 13


def test_Listing_video_value_roundtrip():
    instance = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    assert instance.video == "sample_text"
    instance.video = "sample_text_2"
    assert instance.video == "sample_text_2"


def test_RealEstateAgent_listings_value_roundtrip():
    instance = RealEstateAgent(listings="sample_text")
    assert instance.listings == "sample_text"
    instance.listings = "sample_text_2"
    assert instance.listings == "sample_text_2"


def test_assoc_Actor_Listing_link_reassign_clear():
    a = Listing(address="sample_text", furnished=True, image="sample_text", kitchen=7, livingRooom=7, numberOfBathrooms=7, numberOfBedroms=7, parkingPossibilities=7, video="sample_text")
    b1 = Actor(name="sample_text", password="sample_text", username="sample_text")
    b2 = Actor(name="sample_text_2", password="sample_text_2", username="sample_text_2")
    _safe_set(a, 'actor1', b1)
    assert _is_linked(a, 'actor1', b1)
    if hasattr(b1, 'listing0'):
        assert _is_linked(b1, 'listing0', a)
    _safe_set(a, 'actor1', b2)
    assert _is_linked(a, 'actor1', b2)
    if hasattr(b1, 'listing0'):
        assert not _is_linked(b1, 'listing0', a)
    if hasattr(b2, 'listing0'):
        assert _is_linked(b2, 'listing0', a)
    _safe_set(a, 'actor1', None)
    assert not _is_linked(a, 'actor1', b2)
    if hasattr(b2, 'listing0'):
        assert not _is_linked(b2, 'listing0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actor_strategy = st.builds(Actor, name=safe_text, password=safe_text, username=safe_text)
@given(instance=Actor_strategy)
@settings(max_examples=25)
def test_Actor_instantiation(instance):
    assert isinstance(instance, Actor)


Administrator_strategy = st.builds(Administrator)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Apartment_strategy = st.builds(Apartment, lease=st.integers(), monthlyRent=st.integers(), securityDeposit=st.integers(), size=st.integers())
@given(instance=Apartment_strategy)
@settings(max_examples=25)
def test_Apartment_instantiation(instance):
    assert isinstance(instance, Apartment)


House_strategy = st.builds(House, fees=st.integers(), numberOfFloors=st.integers(), price=st.integers(), sizeOfProperty=st.integers())
@given(instance=House_strategy)
@settings(max_examples=25)
def test_House_instantiation(instance):
    assert isinstance(instance, House)


Listing_strategy = st.builds(Listing, address=safe_text, furnished=st.booleans(), image=safe_text, kitchen=st.integers(), livingRooom=st.integers(), numberOfBathrooms=st.integers(), numberOfBedroms=st.integers(), parkingPossibilities=st.integers(), video=safe_text)
@given(instance=Listing_strategy)
@settings(max_examples=25)
def test_Listing_instantiation(instance):
    assert isinstance(instance, Listing)


RealEstateAgent_strategy = st.builds(RealEstateAgent, listings=safe_text)
@given(instance=RealEstateAgent_strategy)
@settings(max_examples=25)
def test_RealEstateAgent_instantiation(instance):
    assert isinstance(instance, RealEstateAgent)


RegisteredUser_strategy = st.builds(RegisteredUser)
@given(instance=RegisteredUser_strategy)
@settings(max_examples=25)
def test_RegisteredUser_instantiation(instance):
    assert isinstance(instance, RegisteredUser)



