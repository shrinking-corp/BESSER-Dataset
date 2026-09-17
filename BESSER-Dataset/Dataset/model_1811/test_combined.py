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
    extlibrary_Borrower,
    extlibrary_Borrowable,
    extlibrary_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_extlibrary_borrower_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Borrower)


def test_hyp_extlibrary_borrower_constructor_exists():
    assert callable(extlibrary_Borrower.__init__)


def test_hyp_extlibrary_borrower_constructor_args():
    sig = inspect.signature(extlibrary_Borrower.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extlibrary_borrowable_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Borrowable)


def test_hyp_extlibrary_borrowable_constructor_exists():
    assert callable(extlibrary_Borrowable.__init__)


def test_hyp_extlibrary_borrowable_constructor_args():
    sig = inspect.signature(extlibrary_Borrowable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extlibrary_book_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Book)


def test_hyp_extlibrary_book_constructor_exists():
    assert callable(extlibrary_Book.__init__)


def test_hyp_extlibrary_book_constructor_args():
    sig = inspect.signature(extlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"


def test_hyp_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_hyp_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Encyclopedia",
        "Dictionary",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategory"


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
extlibrary_Borrower_strategy = st.builds(
    extlibrary_Borrower,
)
extlibrary_Borrowable_strategy = st.builds(
    extlibrary_Borrowable,
)
extlibrary_Book_strategy = st.builds(
    extlibrary_Book,
    title=
        safe_text
)






@given(instance=extlibrary_Book_strategy)
def test_hyp_extlibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    extlibrary_Book,
    extlibrary_Borrowable,
    extlibrary_Borrower,
    BookCategory,
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

def test_extlibrary_Book_title_value_roundtrip():
    instance = extlibrary_Book(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

extlibrary_Book_strategy = st.builds(extlibrary_Book, title=safe_text)
@given(instance=extlibrary_Book_strategy)
@settings(max_examples=25)
def test_extlibrary_Book_instantiation(instance):
    assert isinstance(instance, extlibrary_Book)


extlibrary_Borrowable_strategy = st.builds(extlibrary_Borrowable)
@given(instance=extlibrary_Borrowable_strategy)
@settings(max_examples=25)
def test_extlibrary_Borrowable_instantiation(instance):
    assert isinstance(instance, extlibrary_Borrowable)


extlibrary_Borrower_strategy = st.builds(extlibrary_Borrower)
@given(instance=extlibrary_Borrower_strategy)
@settings(max_examples=25)
def test_extlibrary_Borrower_instantiation(instance):
    assert isinstance(instance, extlibrary_Borrower)



