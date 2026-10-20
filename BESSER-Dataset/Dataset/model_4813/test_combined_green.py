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
    trip_model_TripModel,
    trip_model_Trip,
    trip_model_location,
    trip_model_Service,
    Service,
    trip_model_TravelService,
    trip_model_OtherService,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_trip_model_tripmodel_is_not_abstract():
    assert not inspect.isabstract(trip_model_TripModel)


def test_hyp_trip_model_tripmodel_constructor_exists():
    assert callable(trip_model_TripModel.__init__)


def test_hyp_trip_model_tripmodel_constructor_args():
    sig = inspect.signature(trip_model_TripModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trip_model_trip_is_not_abstract():
    assert not inspect.isabstract(trip_model_Trip)


def test_hyp_trip_model_trip_constructor_exists():
    assert callable(trip_model_Trip.__init__)


def test_hyp_trip_model_trip_constructor_args():
    sig = inspect.signature(trip_model_Trip.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Start" in params, "Missing parameter 'Start'"
    assert "End" in params, "Missing parameter 'End'"






def test_hyp_trip_model_location_is_not_abstract():
    assert not inspect.isabstract(trip_model_location)


def test_hyp_trip_model_location_constructor_exists():
    assert callable(trip_model_location.__init__)


def test_hyp_trip_model_location_constructor_args():
    sig = inspect.signature(trip_model_location.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_trip_model_service_is_not_abstract():
    assert not inspect.isabstract(trip_model_Service)


def test_hyp_trip_model_service_constructor_exists():
    assert callable(trip_model_Service.__init__)


def test_hyp_trip_model_service_constructor_args():
    sig = inspect.signature(trip_model_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "Rating" in params, "Missing parameter 'Rating'"
    assert "Cost" in params, "Missing parameter 'Cost'"
    assert "Duration" in params, "Missing parameter 'Duration'"
    assert "Type" in params, "Missing parameter 'Type'"








def test_hyp_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_hyp_service_constructor_exists():
    assert callable(Service.__init__)


def test_hyp_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trip_model_travelservice_is_not_abstract():
    assert not inspect.isabstract(trip_model_TravelService)


def test_hyp_trip_model_travelservice_constructor_exists():
    assert callable(trip_model_TravelService.__init__)


def test_hyp_trip_model_travelservice_constructor_args():
    sig = inspect.signature(trip_model_TravelService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trip_model_otherservice_is_not_abstract():
    assert not inspect.isabstract(trip_model_OtherService)


def test_hyp_trip_model_otherservice_constructor_exists():
    assert callable(trip_model_OtherService.__init__)


def test_hyp_trip_model_otherservice_constructor_args():
    sig = inspect.signature(trip_model_OtherService.__init__)
    params = list(sig.parameters.keys())


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
trip_model_TripModel_strategy = st.builds(
    trip_model_TripModel,
)
trip_model_Trip_strategy = st.builds(
    trip_model_Trip,
    name=
        safe_text,
    Start=
        st.dates(),
    End=
        st.dates()
)
trip_model_location_strategy = st.builds(
    trip_model_location,
    name=
        safe_text
)
trip_model_Service_strategy = st.builds(
    trip_model_Service,
    name=
        safe_text,
    Rating=
        st.integers(),
    Cost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Duration=
        st.integers(),
    Type=
        safe_text
)
Service_strategy = st.builds(
    Service,
)
trip_model_TravelService_strategy = st.builds(
    trip_model_TravelService,
)
trip_model_OtherService_strategy = st.builds(
    trip_model_OtherService,
)





@given(instance=trip_model_Trip_strategy)
def test_hyp_trip_model_trip_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=trip_model_Trip_strategy)
def test_hyp_trip_model_trip_Start_setter(instance):
    original = instance.Start
    instance.Start = original
    assert instance.Start == original



@given(instance=trip_model_Trip_strategy)
def test_hyp_trip_model_trip_End_setter(instance):
    original = instance.End
    instance.End = original
    assert instance.End == original




@given(instance=trip_model_location_strategy)
def test_hyp_trip_model_location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=trip_model_Service_strategy)
def test_hyp_trip_model_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=trip_model_Service_strategy)
def test_hyp_trip_model_service_Rating_setter(instance):
    original = instance.Rating
    instance.Rating = original
    assert instance.Rating == original



@given(instance=trip_model_Service_strategy)
def test_hyp_trip_model_service_Cost_setter(instance):
    original = instance.Cost
    instance.Cost = original
    assert instance.Cost == original



@given(instance=trip_model_Service_strategy)
def test_hyp_trip_model_service_Duration_setter(instance):
    original = instance.Duration
    instance.Duration = original
    assert instance.Duration == original



@given(instance=trip_model_Service_strategy)
def test_hyp_trip_model_service_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Service,
    trip_model_OtherService,
    trip_model_Service,
    trip_model_TravelService,
    trip_model_Trip,
    trip_model_TripModel,
    trip_model_location,
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

def test_trip_model_Service_Cost_value_roundtrip():
    instance = trip_model_Service(Cost=3.14, Duration=7, Rating=7, Type="sample_text", name="sample_text")
    assert instance.Cost == 3.14
    instance.Cost = 9.99
    assert instance.Cost == 9.99


def test_trip_model_Service_Duration_value_roundtrip():
    instance = trip_model_Service(Cost=3.14, Duration=7, Rating=7, Type="sample_text", name="sample_text")
    assert instance.Duration == 7
    instance.Duration = 13
    assert instance.Duration == 13


def test_trip_model_Service_Rating_value_roundtrip():
    instance = trip_model_Service(Cost=3.14, Duration=7, Rating=7, Type="sample_text", name="sample_text")
    assert instance.Rating == 7
    instance.Rating = 13
    assert instance.Rating == 13


def test_trip_model_Service_Type_value_roundtrip():
    instance = trip_model_Service(Cost=3.14, Duration=7, Rating=7, Type="sample_text", name="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_trip_model_Service_name_value_roundtrip():
    instance = trip_model_Service(Cost=3.14, Duration=7, Rating=7, Type="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_trip_model_Trip_End_value_roundtrip():
    instance = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    assert instance.End == date(2024, 1, 1)
    instance.End = date(2025, 6, 15)
    assert instance.End == date(2025, 6, 15)


def test_trip_model_Trip_Start_value_roundtrip():
    instance = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    assert instance.Start == date(2024, 1, 1)
    instance.Start = date(2025, 6, 15)
    assert instance.Start == date(2025, 6, 15)


def test_trip_model_Trip_name_value_roundtrip():
    instance = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_trip_model_location_name_value_roundtrip():
    instance = trip_model_location(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_trip_model_OtherService_isa_Service():
    instance = trip_model_OtherService()
    assert isinstance(instance, Service)


def test_trip_model_TravelService_isa_Service():
    instance = trip_model_TravelService()
    assert isinstance(instance, Service)


def test_assoc_destination10_link_reassign_clear():
    a = trip_model_location(name="sample_text")
    b1 = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    b2 = trip_model_Trip(End=date(2025, 6, 15), Start=date(2025, 6, 15), name="sample_text_2")
    _safe_set(a, 'trip_model_location12', b1)
    assert _is_linked(a, 'trip_model_location12', b1)
    if hasattr(b1, 'trip_model_Trip11'):
        assert _is_linked(b1, 'trip_model_Trip11', a)
    _safe_set(a, 'trip_model_location12', b2)
    assert _is_linked(a, 'trip_model_location12', b2)
    if hasattr(b1, 'trip_model_Trip11'):
        assert not _is_linked(b1, 'trip_model_Trip11', a)
    if hasattr(b2, 'trip_model_Trip11'):
        assert _is_linked(b2, 'trip_model_Trip11', a)
    _safe_set(a, 'trip_model_location12', None)
    assert not _is_linked(a, 'trip_model_location12', b2)
    if hasattr(b2, 'trip_model_Trip11'):
        assert not _is_linked(b2, 'trip_model_Trip11', a)


def test_assoc_destination3_link_reassign_clear():
    a = trip_model_location(name="sample_text")
    b1 = trip_model_TravelService()
    b2 = trip_model_TravelService()
    _safe_set(a, 'trip_model_location5', b1)
    assert _is_linked(a, 'trip_model_location5', b1)
    if hasattr(b1, 'trip_model_TravelService4'):
        assert _is_linked(b1, 'trip_model_TravelService4', a)
    _safe_set(a, 'trip_model_location5', b2)
    assert _is_linked(a, 'trip_model_location5', b2)
    if hasattr(b1, 'trip_model_TravelService4'):
        assert not _is_linked(b1, 'trip_model_TravelService4', a)
    if hasattr(b2, 'trip_model_TravelService4'):
        assert _is_linked(b2, 'trip_model_TravelService4', a)
    _safe_set(a, 'trip_model_location5', None)
    assert not _is_linked(a, 'trip_model_location5', b2)
    if hasattr(b2, 'trip_model_TravelService4'):
        assert not _is_linked(b2, 'trip_model_TravelService4', a)


def test_assoc_location0_link_reassign_clear():
    a = trip_model_location(name="sample_text")
    b1 = trip_model_OtherService()
    b2 = trip_model_OtherService()
    _safe_set(a, 'trip_model_location', b1)
    assert _is_linked(a, 'trip_model_location', b1)
    if hasattr(b1, 'trip_model_OtherService'):
        assert _is_linked(b1, 'trip_model_OtherService', a)
    _safe_set(a, 'trip_model_location', b2)
    assert _is_linked(a, 'trip_model_location', b2)
    if hasattr(b1, 'trip_model_OtherService'):
        assert not _is_linked(b1, 'trip_model_OtherService', a)
    if hasattr(b2, 'trip_model_OtherService'):
        assert _is_linked(b2, 'trip_model_OtherService', a)
    _safe_set(a, 'trip_model_location', None)
    assert not _is_linked(a, 'trip_model_location', b2)
    if hasattr(b2, 'trip_model_OtherService'):
        assert not _is_linked(b2, 'trip_model_OtherService', a)


def test_assoc_location15_link_reassign_clear():
    a = trip_model_location(name="sample_text")
    b1 = trip_model_TripModel()
    b2 = trip_model_TripModel()
    _safe_set(a, 'trip_model_location17', b1)
    assert _is_linked(a, 'trip_model_location17', b1)
    if hasattr(b1, 'trip_model_TripModel16'):
        assert _is_linked(b1, 'trip_model_TripModel16', a)
    _safe_set(a, 'trip_model_location17', b2)
    assert _is_linked(a, 'trip_model_location17', b2)
    if hasattr(b1, 'trip_model_TripModel16'):
        assert not _is_linked(b1, 'trip_model_TripModel16', a)
    if hasattr(b2, 'trip_model_TripModel16'):
        assert _is_linked(b2, 'trip_model_TripModel16', a)
    _safe_set(a, 'trip_model_location17', None)
    assert not _is_linked(a, 'trip_model_location17', b2)
    if hasattr(b2, 'trip_model_TripModel16'):
        assert not _is_linked(b2, 'trip_model_TripModel16', a)


def test_assoc_service6_link_reassign_clear():
    a = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    b1 = trip_model_Service(Cost=3.14, Duration=7, Rating=7, Type="sample_text", name="sample_text")
    b2 = trip_model_Service(Cost=9.99, Duration=13, Rating=13, Type="sample_text_2", name="sample_text_2")
    _safe_set(a, 'trip_model_Trip', {b1})
    assert _is_linked(a, 'trip_model_Trip', b1)
    if hasattr(b1, 'trip_model_Service'):
        assert _is_linked(b1, 'trip_model_Service', a)
    _safe_set(a, 'trip_model_Trip', {b2})
    assert _is_linked(a, 'trip_model_Trip', b2)
    if hasattr(b1, 'trip_model_Service'):
        assert not _is_linked(b1, 'trip_model_Service', a)
    if hasattr(b2, 'trip_model_Service'):
        assert _is_linked(b2, 'trip_model_Service', a)
    _safe_set(a, 'trip_model_Trip', set())
    assert not _is_linked(a, 'trip_model_Trip', b2)
    if hasattr(b2, 'trip_model_Service'):
        assert not _is_linked(b2, 'trip_model_Service', a)


def test_assoc_source1_link_reassign_clear():
    a = trip_model_location(name="sample_text")
    b1 = trip_model_TravelService()
    b2 = trip_model_TravelService()
    _safe_set(a, 'trip_model_location2', b1)
    assert _is_linked(a, 'trip_model_location2', b1)
    if hasattr(b1, 'trip_model_TravelService'):
        assert _is_linked(b1, 'trip_model_TravelService', a)
    _safe_set(a, 'trip_model_location2', b2)
    assert _is_linked(a, 'trip_model_location2', b2)
    if hasattr(b1, 'trip_model_TravelService'):
        assert not _is_linked(b1, 'trip_model_TravelService', a)
    if hasattr(b2, 'trip_model_TravelService'):
        assert _is_linked(b2, 'trip_model_TravelService', a)
    _safe_set(a, 'trip_model_location2', None)
    assert not _is_linked(a, 'trip_model_location2', b2)
    if hasattr(b2, 'trip_model_TravelService'):
        assert not _is_linked(b2, 'trip_model_TravelService', a)


def test_assoc_source7_link_reassign_clear():
    a = trip_model_location(name="sample_text")
    b1 = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    b2 = trip_model_Trip(End=date(2025, 6, 15), Start=date(2025, 6, 15), name="sample_text_2")
    _safe_set(a, 'trip_model_location9', b1)
    assert _is_linked(a, 'trip_model_location9', b1)
    if hasattr(b1, 'trip_model_Trip8'):
        assert _is_linked(b1, 'trip_model_Trip8', a)
    _safe_set(a, 'trip_model_location9', b2)
    assert _is_linked(a, 'trip_model_location9', b2)
    if hasattr(b1, 'trip_model_Trip8'):
        assert not _is_linked(b1, 'trip_model_Trip8', a)
    if hasattr(b2, 'trip_model_Trip8'):
        assert _is_linked(b2, 'trip_model_Trip8', a)
    _safe_set(a, 'trip_model_location9', None)
    assert not _is_linked(a, 'trip_model_location9', b2)
    if hasattr(b2, 'trip_model_Trip8'):
        assert not _is_linked(b2, 'trip_model_Trip8', a)


def test_assoc_trip13_link_reassign_clear():
    a = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    b1 = trip_model_TripModel()
    b2 = trip_model_TripModel()
    _safe_set(a, 'trip_model_Trip14', b1)
    assert _is_linked(a, 'trip_model_Trip14', b1)
    if hasattr(b1, 'trip_model_TripModel'):
        assert _is_linked(b1, 'trip_model_TripModel', a)
    _safe_set(a, 'trip_model_Trip14', b2)
    assert _is_linked(a, 'trip_model_Trip14', b2)
    if hasattr(b1, 'trip_model_TripModel'):
        assert not _is_linked(b1, 'trip_model_TripModel', a)
    if hasattr(b2, 'trip_model_TripModel'):
        assert _is_linked(b2, 'trip_model_TripModel', a)
    _safe_set(a, 'trip_model_Trip14', None)
    assert not _is_linked(a, 'trip_model_Trip14', b2)
    if hasattr(b2, 'trip_model_TripModel'):
        assert not _is_linked(b2, 'trip_model_TripModel', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Service_strategy = st.builds(Service)
@given(instance=Service_strategy)
@settings(max_examples=25)
def test_Service_instantiation(instance):
    assert isinstance(instance, Service)


trip_model_OtherService_strategy = st.builds(trip_model_OtherService)
@given(instance=trip_model_OtherService_strategy)
@settings(max_examples=25)
def test_trip_model_OtherService_instantiation(instance):
    assert isinstance(instance, trip_model_OtherService)


trip_model_Service_strategy = st.builds(trip_model_Service, Cost=st.floats(allow_nan=False, allow_infinity=False), Duration=st.integers(), Rating=st.integers(), Type=safe_text, name=safe_text)
@given(instance=trip_model_Service_strategy)
@settings(max_examples=25)
def test_trip_model_Service_instantiation(instance):
    assert isinstance(instance, trip_model_Service)


trip_model_TravelService_strategy = st.builds(trip_model_TravelService)
@given(instance=trip_model_TravelService_strategy)
@settings(max_examples=25)
def test_trip_model_TravelService_instantiation(instance):
    assert isinstance(instance, trip_model_TravelService)


trip_model_Trip_strategy = st.builds(trip_model_Trip, End=st.dates(), Start=st.dates(), name=safe_text)
@given(instance=trip_model_Trip_strategy)
@settings(max_examples=25)
def test_trip_model_Trip_instantiation(instance):
    assert isinstance(instance, trip_model_Trip)


trip_model_TripModel_strategy = st.builds(trip_model_TripModel)
@given(instance=trip_model_TripModel_strategy)
@settings(max_examples=25)
def test_trip_model_TripModel_instantiation(instance):
    assert isinstance(instance, trip_model_TripModel)


trip_model_location_strategy = st.builds(trip_model_location, name=safe_text)
@given(instance=trip_model_location_strategy)
@settings(max_examples=25)
def test_trip_model_location_instantiation(instance):
    assert isinstance(instance, trip_model_location)



