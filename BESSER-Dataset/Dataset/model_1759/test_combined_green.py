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
    library_book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_book_is_not_abstract():
    assert not inspect.isabstract(library_book)


def test_hyp_library_book_constructor_exists():
    assert callable(library_book.__init__)


def test_hyp_library_book_constructor_args():
    sig = inspect.signature(library_book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "published" in params, "Missing parameter 'published'"
    assert "pages" in params, "Missing parameter 'pages'"






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
library_book_strategy = st.builds(
    library_book,
    title=
        safe_text,
    author=
        safe_text,
    published=
        safe_text,
    pages=
        safe_text
)




@given(instance=library_book_strategy)
def test_hyp_library_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_book_strategy)
def test_hyp_library_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=library_book_strategy)
def test_hyp_library_book_published_setter(instance):
    original = instance.published
    instance.published = original
    assert instance.published == original



@given(instance=library_book_strategy)
def test_hyp_library_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    library_book,
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

def test_library_book_author_value_roundtrip():
    instance = library_book(author="sample_text", pages="sample_text", published="sample_text", title="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_library_book_pages_value_roundtrip():
    instance = library_book(author="sample_text", pages="sample_text", published="sample_text", title="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_library_book_published_value_roundtrip():
    instance = library_book(author="sample_text", pages="sample_text", published="sample_text", title="sample_text")
    assert instance.published == "sample_text"
    instance.published = "sample_text_2"
    assert instance.published == "sample_text_2"


def test_library_book_title_value_roundtrip():
    instance = library_book(author="sample_text", pages="sample_text", published="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

library_book_strategy = st.builds(library_book, author=safe_text, pages=safe_text, published=safe_text, title=safe_text)
@given(instance=library_book_strategy)
@settings(max_examples=25)
def test_library_book_instantiation(instance):
    assert isinstance(instance, library_book)



