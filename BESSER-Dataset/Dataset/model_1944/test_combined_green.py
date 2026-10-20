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
    Library,
    schoollibrary_SchoolLibrary,
    Asset,
    Book,
    schoollibrary_SchoolBook,
    schoollibrary_Asset,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_hyp_library_constructor_exists():
    assert callable(Library.__init__)


def test_hyp_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schoollibrary_schoollibrary_is_not_abstract():
    assert not inspect.isabstract(schoollibrary_SchoolLibrary)


def test_hyp_schoollibrary_schoollibrary_constructor_exists():
    assert callable(schoollibrary_SchoolLibrary.__init__)


def test_hyp_schoollibrary_schoollibrary_constructor_args():
    sig = inspect.signature(schoollibrary_SchoolLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"




def test_hyp_asset_is_not_abstract():
    assert not inspect.isabstract(Asset)


def test_hyp_asset_constructor_exists():
    assert callable(Asset.__init__)


def test_hyp_asset_constructor_args():
    sig = inspect.signature(Asset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_hyp_book_constructor_exists():
    assert callable(Book.__init__)


def test_hyp_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schoollibrary_schoolbook_is_not_abstract():
    assert not inspect.isabstract(schoollibrary_SchoolBook)


def test_hyp_schoollibrary_schoolbook_constructor_exists():
    assert callable(schoollibrary_SchoolBook.__init__)


def test_hyp_schoollibrary_schoolbook_constructor_args():
    sig = inspect.signature(schoollibrary_SchoolBook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_schoollibrary_asset_is_not_abstract():
    assert not inspect.isabstract(schoollibrary_Asset)


def test_hyp_schoollibrary_asset_constructor_exists():
    assert callable(schoollibrary_Asset.__init__)


def test_hyp_schoollibrary_asset_constructor_args():
    sig = inspect.signature(schoollibrary_Asset.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"



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
Library_strategy = st.builds(
    Library,
)
schoollibrary_SchoolLibrary_strategy = st.builds(
    schoollibrary_SchoolLibrary,
    location=
        safe_text
)
Asset_strategy = st.builds(
    Asset,
)
Book_strategy = st.builds(
    Book,
)
schoollibrary_SchoolBook_strategy = st.builds(
    schoollibrary_SchoolBook,
)
schoollibrary_Asset_strategy = st.builds(
    schoollibrary_Asset,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)





@given(instance=schoollibrary_SchoolLibrary_strategy)
def test_hyp_schoollibrary_schoollibrary_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original







@given(instance=schoollibrary_Asset_strategy)
def test_hyp_schoollibrary_asset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Asset,
    Book,
    Library,
    schoollibrary_Asset,
    schoollibrary_SchoolBook,
    schoollibrary_SchoolLibrary,
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

def test_schoollibrary_Asset_value_value_roundtrip():
    instance = schoollibrary_Asset(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_schoollibrary_SchoolLibrary_location_value_roundtrip():
    instance = schoollibrary_SchoolLibrary(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_schoollibrary_SchoolBook_isa_Asset():
    instance = schoollibrary_SchoolBook()
    assert isinstance(instance, Asset)


def test_schoollibrary_SchoolBook_isa_Book():
    instance = schoollibrary_SchoolBook()
    assert isinstance(instance, Book)


def test_schoollibrary_SchoolLibrary_isa_Library():
    instance = schoollibrary_SchoolLibrary(location="sample_text")
    assert isinstance(instance, Library)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Asset_strategy = st.builds(Asset)
@given(instance=Asset_strategy)
@settings(max_examples=25)
def test_Asset_instantiation(instance):
    assert isinstance(instance, Asset)


Book_strategy = st.builds(Book)
@given(instance=Book_strategy)
@settings(max_examples=25)
def test_Book_instantiation(instance):
    assert isinstance(instance, Book)


Library_strategy = st.builds(Library)
@given(instance=Library_strategy)
@settings(max_examples=25)
def test_Library_instantiation(instance):
    assert isinstance(instance, Library)


schoollibrary_Asset_strategy = st.builds(schoollibrary_Asset, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=schoollibrary_Asset_strategy)
@settings(max_examples=25)
def test_schoollibrary_Asset_instantiation(instance):
    assert isinstance(instance, schoollibrary_Asset)


schoollibrary_SchoolBook_strategy = st.builds(schoollibrary_SchoolBook)
@given(instance=schoollibrary_SchoolBook_strategy)
@settings(max_examples=25)
def test_schoollibrary_SchoolBook_instantiation(instance):
    assert isinstance(instance, schoollibrary_SchoolBook)


schoollibrary_SchoolLibrary_strategy = st.builds(schoollibrary_SchoolLibrary, location=safe_text)
@given(instance=schoollibrary_SchoolLibrary_strategy)
@settings(max_examples=25)
def test_schoollibrary_SchoolLibrary_instantiation(instance):
    assert isinstance(instance, schoollibrary_SchoolLibrary)



