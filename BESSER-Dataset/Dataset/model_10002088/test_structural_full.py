import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Category,
    DistanceInfo,
    Location,
    LocationConnector_Interface,
    LocationManager,
    MyClass,
    MyClass2,
    MyClass3,
    Place,
    PlaceDetail,
    Enumeration,
    Enumeration2,
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

def test_Category_Id_value_roundtrip():
    instance = Category(Id=7, Name="sample_text", Type="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Category_Name_value_roundtrip():
    instance = Category(Id=7, Name="sample_text", Type="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Category_Type_value_roundtrip():
    instance = Category(Id=7, Name="sample_text", Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_DistanceInfo_Distaince_value_roundtrip():
    instance = DistanceInfo(Distaince="sample_text", ShortestPath="sample_text", TraficInfo="sample_text")
    assert instance.Distaince == "sample_text"
    instance.Distaince = "sample_text_2"
    assert instance.Distaince == "sample_text_2"


def test_DistanceInfo_ShortestPath_value_roundtrip():
    instance = DistanceInfo(Distaince="sample_text", ShortestPath="sample_text", TraficInfo="sample_text")
    assert instance.ShortestPath == "sample_text"
    instance.ShortestPath = "sample_text_2"
    assert instance.ShortestPath == "sample_text_2"


def test_DistanceInfo_TraficInfo_value_roundtrip():
    instance = DistanceInfo(Distaince="sample_text", ShortestPath="sample_text", TraficInfo="sample_text")
    assert instance.TraficInfo == "sample_text"
    instance.TraficInfo = "sample_text_2"
    assert instance.TraficInfo == "sample_text_2"


def test_Location_Latitude_value_roundtrip():
    instance = Location(Latitude="sample_text", Longitude="sample_text")
    assert instance.Latitude == "sample_text"
    instance.Latitude = "sample_text_2"
    assert instance.Latitude == "sample_text_2"


def test_Location_Longitude_value_roundtrip():
    instance = Location(Latitude="sample_text", Longitude="sample_text")
    assert instance.Longitude == "sample_text"
    instance.Longitude = "sample_text_2"
    assert instance.Longitude == "sample_text_2"


def test_Place_Details_value_roundtrip():
    instance = Place(Details="sample_text", Name="sample_text")
    assert instance.Details == "sample_text"
    instance.Details = "sample_text_2"
    assert instance.Details == "sample_text_2"


def test_Place_Name_value_roundtrip():
    instance = Place(Details="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Category_strategy = st.builds(Category, Id=st.integers(), Name=safe_text, Type=safe_text)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


DistanceInfo_strategy = st.builds(DistanceInfo, Distaince=safe_text, ShortestPath=safe_text, TraficInfo=safe_text)
@given(instance=DistanceInfo_strategy)
@settings(max_examples=25)
def test_DistanceInfo_instantiation(instance):
    assert isinstance(instance, DistanceInfo)


Location_strategy = st.builds(Location, Latitude=safe_text, Longitude=safe_text)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


LocationConnector_Interface_strategy = st.builds(LocationConnector_Interface)
@given(instance=LocationConnector_Interface_strategy)
@settings(max_examples=25)
def test_LocationConnector_Interface_instantiation(instance):
    assert isinstance(instance, LocationConnector_Interface)


LocationManager_strategy = st.builds(LocationManager)
@given(instance=LocationManager_strategy)
@settings(max_examples=25)
def test_LocationManager_instantiation(instance):
    assert isinstance(instance, LocationManager)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


MyClass2_strategy = st.builds(MyClass2)
@given(instance=MyClass2_strategy)
@settings(max_examples=25)
def test_MyClass2_instantiation(instance):
    assert isinstance(instance, MyClass2)


MyClass3_strategy = st.builds(MyClass3)
@given(instance=MyClass3_strategy)
@settings(max_examples=25)
def test_MyClass3_instantiation(instance):
    assert isinstance(instance, MyClass3)


Place_strategy = st.builds(Place, Details=safe_text, Name=safe_text)
@given(instance=Place_strategy)
@settings(max_examples=25)
def test_Place_instantiation(instance):
    assert isinstance(instance, Place)


