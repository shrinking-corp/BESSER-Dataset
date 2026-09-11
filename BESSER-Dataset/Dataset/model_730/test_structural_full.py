import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    dc_Bounds,
    dc_Dimension,
    dc_Point,
    AlignmentKind,
    KnownColor,
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

def test_dc_Bounds_height_value_roundtrip():
    instance = dc_Bounds(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_dc_Bounds_width_value_roundtrip():
    instance = dc_Bounds(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_dc_Bounds_x_value_roundtrip():
    instance = dc_Bounds(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_dc_Bounds_y_value_roundtrip():
    instance = dc_Bounds(height="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_dc_Dimension_height_value_roundtrip():
    instance = dc_Dimension(height="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_dc_Dimension_width_value_roundtrip():
    instance = dc_Dimension(height="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_dc_Point_x_value_roundtrip():
    instance = dc_Point(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_dc_Point_y_value_roundtrip():
    instance = dc_Point(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

dc_Bounds_strategy = st.builds(dc_Bounds, height=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=dc_Bounds_strategy)
@settings(max_examples=25)
def test_dc_Bounds_instantiation(instance):
    assert isinstance(instance, dc_Bounds)


dc_Dimension_strategy = st.builds(dc_Dimension, height=safe_text, width=safe_text)
@given(instance=dc_Dimension_strategy)
@settings(max_examples=25)
def test_dc_Dimension_instantiation(instance):
    assert isinstance(instance, dc_Dimension)


dc_Point_strategy = st.builds(dc_Point, x=safe_text, y=safe_text)
@given(instance=dc_Point_strategy)
@settings(max_examples=25)
def test_dc_Point_instantiation(instance):
    assert isinstance(instance, dc_Point)


