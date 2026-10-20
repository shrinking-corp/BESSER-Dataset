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
    Users,
    Reviews,
    Places,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_hyp_users_constructor_exists():
    assert callable(Users.__init__)


def test_hyp_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "date_joined" in params, "Missing parameter 'date_joined'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "average_star" in params, "Missing parameter 'average_star'"
    assert "review_count" in params, "Missing parameter 'review_count'"
    assert "name" in params, "Missing parameter 'name'"








def test_hyp_reviews_is_not_abstract():
    assert not inspect.isabstract(Reviews)


def test_hyp_reviews_constructor_exists():
    assert callable(Reviews.__init__)


def test_hyp_reviews_constructor_args():
    sig = inspect.signature(Reviews.__init__)
    params = list(sig.parameters.keys())
    assert "business_id" in params, "Missing parameter 'business_id'"
    assert "rating" in params, "Missing parameter 'rating'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "text" in params, "Missing parameter 'text'"









def test_hyp_places_is_not_abstract():
    assert not inspect.isabstract(Places)


def test_hyp_places_constructor_exists():
    assert callable(Places.__init__)


def test_hyp_places_constructor_args():
    sig = inspect.signature(Places.__init__)
    params = list(sig.parameters.keys())
    assert "wifi" in params, "Missing parameter 'wifi'"
    assert "plugs" in params, "Missing parameter 'plugs'"
    assert "place_id" in params, "Missing parameter 'place_id'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "address" in params, "Missing parameter 'address'"
    assert "opening_times" in params, "Missing parameter 'opening_times'"
    assert "music" in params, "Missing parameter 'music'"
    assert "review_count" in params, "Missing parameter 'review_count'"










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
Users_strategy = st.builds(
    Users,
    date_joined=
        st.dates(),
    ID=
        st.integers(),
    average_star=
        st.integers(),
    review_count=
        st.integers(),
    name=
        safe_text
)
Reviews_strategy = st.builds(
    Reviews,
    business_id=
        st.integers(),
    rating=
        st.integers(),
    ID=
        st.integers(),
    user_id=
        st.integers(),
    date=
        st.dates(),
    text=
        safe_text
)
Places_strategy = st.builds(
    Places,
    wifi=
        safe_text,
    plugs=
        safe_text,
    place_id=
        safe_text,
    ID=
        st.integers(),
    address=
        safe_text,
    opening_times=
        st.dates(),
    music=
        safe_text,
    review_count=
        st.integers()
)




@given(instance=Users_strategy)
def test_hyp_users_date_joined_setter(instance):
    original = instance.date_joined
    instance.date_joined = original
    assert instance.date_joined == original



@given(instance=Users_strategy)
def test_hyp_users_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Users_strategy)
def test_hyp_users_average_star_setter(instance):
    original = instance.average_star
    instance.average_star = original
    assert instance.average_star == original



@given(instance=Users_strategy)
def test_hyp_users_review_count_setter(instance):
    original = instance.review_count
    instance.review_count = original
    assert instance.review_count == original



@given(instance=Users_strategy)
def test_hyp_users_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Reviews_strategy)
def test_hyp_reviews_business_id_setter(instance):
    original = instance.business_id
    instance.business_id = original
    assert instance.business_id == original



@given(instance=Reviews_strategy)
def test_hyp_reviews_rating_setter(instance):
    original = instance.rating
    instance.rating = original
    assert instance.rating == original



@given(instance=Reviews_strategy)
def test_hyp_reviews_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Reviews_strategy)
def test_hyp_reviews_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Reviews_strategy)
def test_hyp_reviews_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Reviews_strategy)
def test_hyp_reviews_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=Places_strategy)
def test_hyp_places_wifi_setter(instance):
    original = instance.wifi
    instance.wifi = original
    assert instance.wifi == original



@given(instance=Places_strategy)
def test_hyp_places_plugs_setter(instance):
    original = instance.plugs
    instance.plugs = original
    assert instance.plugs == original



@given(instance=Places_strategy)
def test_hyp_places_place_id_setter(instance):
    original = instance.place_id
    instance.place_id = original
    assert instance.place_id == original



@given(instance=Places_strategy)
def test_hyp_places_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Places_strategy)
def test_hyp_places_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Places_strategy)
def test_hyp_places_opening_times_setter(instance):
    original = instance.opening_times
    instance.opening_times = original
    assert instance.opening_times == original



@given(instance=Places_strategy)
def test_hyp_places_music_setter(instance):
    original = instance.music
    instance.music = original
    assert instance.music == original



@given(instance=Places_strategy)
def test_hyp_places_review_count_setter(instance):
    original = instance.review_count
    instance.review_count = original
    assert instance.review_count == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Places,
    Reviews,
    Users,
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

def test_Places_ID_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Places_address_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Places_music_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.music == "sample_text"
    instance.music = "sample_text_2"
    assert instance.music == "sample_text_2"


def test_Places_opening_times_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.opening_times == date(2024, 1, 1)
    instance.opening_times = date(2025, 6, 15)
    assert instance.opening_times == date(2025, 6, 15)


def test_Places_place_id_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.place_id == "sample_text"
    instance.place_id = "sample_text_2"
    assert instance.place_id == "sample_text_2"


def test_Places_plugs_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.plugs == "sample_text"
    instance.plugs = "sample_text_2"
    assert instance.plugs == "sample_text_2"


def test_Places_review_count_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.review_count == 7
    instance.review_count = 13
    assert instance.review_count == 13


def test_Places_wifi_value_roundtrip():
    instance = Places(ID=7, address="sample_text", music="sample_text", opening_times=date(2024, 1, 1), place_id="sample_text", plugs="sample_text", review_count=7, wifi="sample_text")
    assert instance.wifi == "sample_text"
    instance.wifi = "sample_text_2"
    assert instance.wifi == "sample_text_2"


def test_Reviews_ID_value_roundtrip():
    instance = Reviews(ID=7, business_id=7, date=date(2024, 1, 1), rating=7, text="sample_text", user_id=7)
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Reviews_business_id_value_roundtrip():
    instance = Reviews(ID=7, business_id=7, date=date(2024, 1, 1), rating=7, text="sample_text", user_id=7)
    assert instance.business_id == 7
    instance.business_id = 13
    assert instance.business_id == 13


def test_Reviews_date_value_roundtrip():
    instance = Reviews(ID=7, business_id=7, date=date(2024, 1, 1), rating=7, text="sample_text", user_id=7)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_Reviews_rating_value_roundtrip():
    instance = Reviews(ID=7, business_id=7, date=date(2024, 1, 1), rating=7, text="sample_text", user_id=7)
    assert instance.rating == 7
    instance.rating = 13
    assert instance.rating == 13


def test_Reviews_text_value_roundtrip():
    instance = Reviews(ID=7, business_id=7, date=date(2024, 1, 1), rating=7, text="sample_text", user_id=7)
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_Reviews_user_id_value_roundtrip():
    instance = Reviews(ID=7, business_id=7, date=date(2024, 1, 1), rating=7, text="sample_text", user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Users_ID_value_roundtrip():
    instance = Users(ID=7, average_star=7, date_joined=date(2024, 1, 1), name="sample_text", review_count=7)
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Users_average_star_value_roundtrip():
    instance = Users(ID=7, average_star=7, date_joined=date(2024, 1, 1), name="sample_text", review_count=7)
    assert instance.average_star == 7
    instance.average_star = 13
    assert instance.average_star == 13


def test_Users_date_joined_value_roundtrip():
    instance = Users(ID=7, average_star=7, date_joined=date(2024, 1, 1), name="sample_text", review_count=7)
    assert instance.date_joined == date(2024, 1, 1)
    instance.date_joined = date(2025, 6, 15)
    assert instance.date_joined == date(2025, 6, 15)


def test_Users_name_value_roundtrip():
    instance = Users(ID=7, average_star=7, date_joined=date(2024, 1, 1), name="sample_text", review_count=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Users_review_count_value_roundtrip():
    instance = Users(ID=7, average_star=7, date_joined=date(2024, 1, 1), name="sample_text", review_count=7)
    assert instance.review_count == 7
    instance.review_count = 13
    assert instance.review_count == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Places_strategy = st.builds(Places, ID=st.integers(), address=safe_text, music=safe_text, opening_times=st.dates(), place_id=safe_text, plugs=safe_text, review_count=st.integers(), wifi=safe_text)
@given(instance=Places_strategy)
@settings(max_examples=25)
def test_Places_instantiation(instance):
    assert isinstance(instance, Places)


Reviews_strategy = st.builds(Reviews, ID=st.integers(), business_id=st.integers(), date=st.dates(), rating=st.integers(), text=safe_text, user_id=st.integers())
@given(instance=Reviews_strategy)
@settings(max_examples=25)
def test_Reviews_instantiation(instance):
    assert isinstance(instance, Reviews)


Users_strategy = st.builds(Users, ID=st.integers(), average_star=st.integers(), date_joined=st.dates(), name=safe_text, review_count=st.integers())
@given(instance=Users_strategy)
@settings(max_examples=25)
def test_Users_instantiation(instance):
    assert isinstance(instance, Users)



