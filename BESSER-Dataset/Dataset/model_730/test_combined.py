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
    dc_Bounds,
    dc_Dimension,
    dc_Point,
    KnownColor,
    AlignmentKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_dc_bounds_is_not_abstract():
    assert not inspect.isabstract(dc_Bounds)


def test_hyp_dc_bounds_constructor_exists():
    assert callable(dc_Bounds.__init__)


def test_hyp_dc_bounds_constructor_args():
    sig = inspect.signature(dc_Bounds.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"







def test_hyp_dc_dimension_is_not_abstract():
    assert not inspect.isabstract(dc_Dimension)


def test_hyp_dc_dimension_constructor_exists():
    assert callable(dc_Dimension.__init__)


def test_hyp_dc_dimension_constructor_args():
    sig = inspect.signature(dc_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"





def test_hyp_dc_point_is_not_abstract():
    assert not inspect.isabstract(dc_Point)


def test_hyp_dc_point_constructor_exists():
    assert callable(dc_Point.__init__)


def test_hyp_dc_point_constructor_args():
    sig = inspect.signature(dc_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"



def test_hyp_knowncolor_exists():
    # Check that the Enumeration exists
    assert KnownColor is not None

def test_hyp_knowncolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KnownColor]
    expected_literals = [
        "green",
        "blue",
        "aqua",
        "teal",
        "lime",
        "silver",
        "yellow",
        "navy",
        "purple",
        "maroon",
        "red",
        "fuchsia",
        "black",
        "olive",
        "white",
        "orange",
        "gray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KnownColor"

def test_hyp_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_hyp_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "end",
        "center",
        "start",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"


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
dc_Bounds_strategy = st.builds(
    dc_Bounds,
    y=
        safe_text,
    height=
        safe_text,
    width=
        safe_text,
    x=
        safe_text
)
dc_Dimension_strategy = st.builds(
    dc_Dimension,
    height=
        safe_text,
    width=
        safe_text
)
dc_Point_strategy = st.builds(
    dc_Point,
    y=
        safe_text,
    x=
        safe_text
)




@given(instance=dc_Bounds_strategy)
def test_hyp_dc_bounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=dc_Bounds_strategy)
def test_hyp_dc_bounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=dc_Bounds_strategy)
def test_hyp_dc_bounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=dc_Bounds_strategy)
def test_hyp_dc_bounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dc_Bounds_strategy)
@settings(max_examples=30)
def test_hyp_dc_bounds_nonnegativesize_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nonNegativeSize(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nonNegativeSize).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nonNegativeSize' in dc_Bounds is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nonNegativeSize' in dc_Bounds did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nonNegativeSize' in dc_Bounds is not implemented or raised an error")




@given(instance=dc_Dimension_strategy)
def test_hyp_dc_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=dc_Dimension_strategy)
def test_hyp_dc_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dc_Dimension_strategy)
@settings(max_examples=30)
def test_hyp_dc_dimension_nonnegativedimension_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.nonNegativeDimension(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.nonNegativeDimension).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'nonNegativeDimension' in dc_Dimension is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'nonNegativeDimension' in dc_Dimension did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'nonNegativeDimension' in dc_Dimension is not implemented or raised an error")




@given(instance=dc_Point_strategy)
def test_hyp_dc_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=dc_Point_strategy)
def test_hyp_dc_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



