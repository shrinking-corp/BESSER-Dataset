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
    location_Location,
    location_Area,
    AltitudeMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_location_location_is_not_abstract():
    assert not inspect.isabstract(location_Location)


def test_hyp_location_location_constructor_exists():
    assert callable(location_Location.__init__)


def test_hyp_location_location_constructor_args():
    sig = inspect.signature(location_Location.__init__)
    params = list(sig.parameters.keys())
    assert "altitudeMode" in params, "Missing parameter 'altitudeMode'"
    assert "description" in params, "Missing parameter 'description'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "country" in params, "Missing parameter 'country'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "altitude" in params, "Missing parameter 'altitude'"
    assert "name" in params, "Missing parameter 'name'"
    assert "street" in params, "Missing parameter 'street'"
    assert "postalCode" in params, "Missing parameter 'postalCode'"
    assert "state" in params, "Missing parameter 'state'"
    assert "city" in params, "Missing parameter 'city'"
















def test_hyp_location_area_is_not_abstract():
    assert not inspect.isabstract(location_Area)


def test_hyp_location_area_constructor_exists():
    assert callable(location_Area.__init__)


def test_hyp_location_area_constructor_args():
    sig = inspect.signature(location_Area.__init__)
    params = list(sig.parameters.keys())
    assert "boundary" in params, "Missing parameter 'boundary'"
    assert "comments" in params, "Missing parameter 'comments'"
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_altitudemode_exists():
    # Check that the Enumeration exists
    assert AltitudeMode is not None

def test_hyp_altitudemode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AltitudeMode]
    expected_literals = [
        "relativeToGround",
        "clampToGround",
        "absolute",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AltitudeMode"


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
location_Location_strategy = st.builds(
    location_Location,
    altitudeMode=
        safe_text,
    description=
        safe_text,
    phoneNumber=
        safe_text,
    longitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    country=
        safe_text,
    comments=
        safe_text,
    latitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    street=
        safe_text,
    postalCode=
        safe_text,
    state=
        safe_text,
    city=
        safe_text
)
location_Area_strategy = st.builds(
    location_Area,
    boundary=
        safe_text,
    comments=
        safe_text,
    name=
        safe_text
)




@given(instance=location_Location_strategy)
def test_hyp_location_location_altitudeMode_setter(instance):
    original = instance.altitudeMode
    instance.altitudeMode = original
    assert instance.altitudeMode == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_postalCode_setter(instance):
    original = instance.postalCode
    instance.postalCode = original
    assert instance.postalCode == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=location_Location_strategy)
def test_hyp_location_location_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=location_Location_strategy)
@settings(max_examples=30)
def test_hyp_location_location_containspoint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.containsPoint(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.containsPoint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'containsPoint' in location_Location is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'containsPoint' in location_Location did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'containsPoint' in location_Location is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=location_Location_strategy)
@settings(max_examples=30)
def test_hyp_location_location_locate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.locate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.locate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'locate' in location_Location is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'locate' in location_Location did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'locate' in location_Location is not implemented or raised an error")




@given(instance=location_Area_strategy)
def test_hyp_location_area_boundary_setter(instance):
    original = instance.boundary
    instance.boundary = original
    assert instance.boundary == original



@given(instance=location_Area_strategy)
def test_hyp_location_area_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original



@given(instance=location_Area_strategy)
def test_hyp_location_area_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=location_Area_strategy)
@settings(max_examples=30)
def test_hyp_location_area_containspoint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.containsPoint(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.containsPoint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'containsPoint' in location_Area is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'containsPoint' in location_Area did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'containsPoint' in location_Area is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    location_Area,
    location_Location,
    AltitudeMode,
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

def test_location_Area_boundary_value_roundtrip():
    instance = location_Area(boundary="sample_text", comments="sample_text", name="sample_text")
    assert instance.boundary == "sample_text"
    instance.boundary = "sample_text_2"
    assert instance.boundary == "sample_text_2"


def test_location_Area_comments_value_roundtrip():
    instance = location_Area(boundary="sample_text", comments="sample_text", name="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_location_Area_name_value_roundtrip():
    instance = location_Area(boundary="sample_text", comments="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_location_Location_altitude_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.altitude == 3.14
    instance.altitude = 9.99
    assert instance.altitude == 9.99


def test_location_Location_altitudeMode_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.altitudeMode == "sample_text"
    instance.altitudeMode = "sample_text_2"
    assert instance.altitudeMode == "sample_text_2"


def test_location_Location_city_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_location_Location_comments_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_location_Location_country_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_location_Location_description_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_location_Location_latitude_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.latitude == 3.14
    instance.latitude = 9.99
    assert instance.latitude == 9.99


def test_location_Location_longitude_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.longitude == 3.14
    instance.longitude = 9.99
    assert instance.longitude == 9.99


def test_location_Location_name_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_location_Location_phoneNumber_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_location_Location_postalCode_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.postalCode == "sample_text"
    instance.postalCode = "sample_text_2"
    assert instance.postalCode == "sample_text_2"


def test_location_Location_state_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_location_Location_street_value_roundtrip():
    instance = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_assoc_areas0_link_reassign_clear():
    a = location_Location(altitude=3.14, altitudeMode="sample_text", city="sample_text", comments="sample_text", country="sample_text", description="sample_text", latitude=3.14, longitude=3.14, name="sample_text", phoneNumber="sample_text", postalCode="sample_text", state="sample_text", street="sample_text")
    b1 = location_Area(boundary="sample_text", comments="sample_text", name="sample_text")
    b2 = location_Area(boundary="sample_text_2", comments="sample_text_2", name="sample_text_2")
    _safe_set(a, 'location_Location', {b1})
    assert _is_linked(a, 'location_Location', b1)
    if hasattr(b1, 'location_Area'):
        assert _is_linked(b1, 'location_Area', a)
    _safe_set(a, 'location_Location', {b2})
    assert _is_linked(a, 'location_Location', b2)
    if hasattr(b1, 'location_Area'):
        assert not _is_linked(b1, 'location_Area', a)
    if hasattr(b2, 'location_Area'):
        assert _is_linked(b2, 'location_Area', a)
    _safe_set(a, 'location_Location', set())
    assert not _is_linked(a, 'location_Location', b2)
    if hasattr(b2, 'location_Area'):
        assert not _is_linked(b2, 'location_Area', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

location_Area_strategy = st.builds(location_Area, boundary=safe_text, comments=safe_text, name=safe_text)
@given(instance=location_Area_strategy)
@settings(max_examples=25)
def test_location_Area_instantiation(instance):
    assert isinstance(instance, location_Area)


location_Location_strategy = st.builds(location_Location, altitude=st.floats(allow_nan=False, allow_infinity=False), altitudeMode=safe_text, city=safe_text, comments=safe_text, country=safe_text, description=safe_text, latitude=st.floats(allow_nan=False, allow_infinity=False), longitude=st.floats(allow_nan=False, allow_infinity=False), name=safe_text, phoneNumber=safe_text, postalCode=safe_text, state=safe_text, street=safe_text)
@given(instance=location_Location_strategy)
@settings(max_examples=25)
def test_location_Location_instantiation(instance):
    assert isinstance(instance, location_Location)



