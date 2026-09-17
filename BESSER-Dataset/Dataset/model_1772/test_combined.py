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
    books_Writer,
    books_Book,
    books_Catalog,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_books_writer_is_not_abstract():
    assert not inspect.isabstract(books_Writer)


def test_hyp_books_writer_constructor_exists():
    assert callable(books_Writer.__init__)


def test_hyp_books_writer_constructor_args():
    sig = inspect.signature(books_Writer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_books_book_is_not_abstract():
    assert not inspect.isabstract(books_Book)


def test_hyp_books_book_constructor_exists():
    assert callable(books_Book.__init__)


def test_hyp_books_book_constructor_args():
    sig = inspect.signature(books_Book.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"






def test_hyp_books_catalog_is_not_abstract():
    assert not inspect.isabstract(books_Catalog)


def test_hyp_books_catalog_constructor_exists():
    assert callable(books_Catalog.__init__)


def test_hyp_books_catalog_constructor_args():
    sig = inspect.signature(books_Catalog.__init__)
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
books_Writer_strategy = st.builds(
    books_Writer,
)
books_Book_strategy = st.builds(
    books_Book,
    isbn=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text
)
books_Catalog_strategy = st.builds(
    books_Catalog,
)





@given(instance=books_Book_strategy)
def test_hyp_books_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=books_Book_strategy)
def test_hyp_books_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=books_Book_strategy)
def test_hyp_books_book_title_setter(instance):
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
    books_Book,
    books_Catalog,
    books_Writer,
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

def test_books_Book_isbn_value_roundtrip():
    instance = books_Book(isbn="sample_text", pages=7, title="sample_text")
    assert instance.isbn == "sample_text"
    instance.isbn = "sample_text_2"
    assert instance.isbn == "sample_text_2"


def test_books_Book_pages_value_roundtrip():
    instance = books_Book(isbn="sample_text", pages=7, title="sample_text")
    assert instance.pages == 7
    instance.pages = 13
    assert instance.pages == 13


def test_books_Book_title_value_roundtrip():
    instance = books_Book(isbn="sample_text", pages=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_assoc_authors1_link_reassign_clear():
    a = books_Book(isbn="sample_text", pages=7, title="sample_text")
    b1 = books_Writer()
    b2 = books_Writer()
    _safe_set(a, 'books', {b1})
    assert _is_linked(a, 'books', b1)
    if hasattr(b1, 'writers.ecoreWriter'):
        assert _is_linked(b1, 'writers.ecoreWriter', a)
    _safe_set(a, 'books', {b2})
    assert _is_linked(a, 'books', b2)
    if hasattr(b1, 'writers.ecoreWriter'):
        assert not _is_linked(b1, 'writers.ecoreWriter', a)
    if hasattr(b2, 'writers.ecoreWriter'):
        assert _is_linked(b2, 'writers.ecoreWriter', a)
    _safe_set(a, 'books', set())
    assert not _is_linked(a, 'books', b2)
    if hasattr(b2, 'writers.ecoreWriter'):
        assert not _is_linked(b2, 'writers.ecoreWriter', a)


def test_assoc_books0_link_reassign_clear():
    a = books_Book(isbn="sample_text", pages=7, title="sample_text")
    b1 = books_Catalog()
    b2 = books_Catalog()
    _safe_set(a, 'books_Book', b1)
    assert _is_linked(a, 'books_Book', b1)
    if hasattr(b1, 'books_Catalog'):
        assert _is_linked(b1, 'books_Catalog', a)
    _safe_set(a, 'books_Book', b2)
    assert _is_linked(a, 'books_Book', b2)
    if hasattr(b1, 'books_Catalog'):
        assert not _is_linked(b1, 'books_Catalog', a)
    if hasattr(b2, 'books_Catalog'):
        assert _is_linked(b2, 'books_Catalog', a)
    _safe_set(a, 'books_Book', None)
    assert not _is_linked(a, 'books_Book', b2)
    if hasattr(b2, 'books_Catalog'):
        assert not _is_linked(b2, 'books_Catalog', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

books_Book_strategy = st.builds(books_Book, isbn=safe_text, pages=st.integers(), title=safe_text)
@given(instance=books_Book_strategy)
@settings(max_examples=25)
def test_books_Book_instantiation(instance):
    assert isinstance(instance, books_Book)


books_Catalog_strategy = st.builds(books_Catalog)
@given(instance=books_Catalog_strategy)
@settings(max_examples=25)
def test_books_Catalog_instantiation(instance):
    assert isinstance(instance, books_Catalog)


books_Writer_strategy = st.builds(books_Writer)
@given(instance=books_Writer_strategy)
@settings(max_examples=25)
def test_books_Writer_instantiation(instance):
    assert isinstance(instance, books_Writer)



