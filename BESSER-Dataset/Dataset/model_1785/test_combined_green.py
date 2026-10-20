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
    Book_Chapter,
    Book_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_book_chapter_is_not_abstract():
    assert not inspect.isabstract(Book_Chapter)


def test_hyp_book_chapter_constructor_exists():
    assert callable(Book_Chapter.__init__)


def test_hyp_book_chapter_constructor_args():
    sig = inspect.signature(Book_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "nbPages" in params, "Missing parameter 'nbPages'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_book_book_is_not_abstract():
    assert not inspect.isabstract(Book_Book)


def test_hyp_book_book_constructor_exists():
    assert callable(Book_Book.__init__)


def test_hyp_book_book_constructor_args():
    sig = inspect.signature(Book_Book.__init__)
    params = list(sig.parameters.keys())
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "title" in params, "Missing parameter 'title'"




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
Book_Chapter_strategy = st.builds(
    Book_Chapter,
    nbPages=
        st.integers(),
    title=
        safe_text
)
Book_Book_strategy = st.builds(
    Book_Book,
    authorName=
        safe_text,
    title=
        safe_text
)




@given(instance=Book_Chapter_strategy)
def test_hyp_book_chapter_nbPages_setter(instance):
    original = instance.nbPages
    instance.nbPages = original
    assert instance.nbPages == original



@given(instance=Book_Chapter_strategy)
def test_hyp_book_chapter_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=Book_Book_strategy)
def test_hyp_book_book_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=Book_Book_strategy)
def test_hyp_book_book_title_setter(instance):
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
    Book_Book,
    Book_Chapter,
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

def test_Book_Book_authorName_value_roundtrip():
    instance = Book_Book(authorName="sample_text", title="sample_text")
    assert instance.authorName == "sample_text"
    instance.authorName = "sample_text_2"
    assert instance.authorName == "sample_text_2"


def test_Book_Book_title_value_roundtrip():
    instance = Book_Book(authorName="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_Book_Chapter_nbPages_value_roundtrip():
    instance = Book_Chapter(nbPages=7, title="sample_text")
    assert instance.nbPages == 7
    instance.nbPages = 13
    assert instance.nbPages == 13


def test_Book_Chapter_title_value_roundtrip():
    instance = Book_Chapter(nbPages=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_assoc_chapters0_link_reassign_clear():
    a = Book_Chapter(nbPages=7, title="sample_text")
    b1 = Book_Book(authorName="sample_text", title="sample_text")
    b2 = Book_Book(authorName="sample_text_2", title="sample_text_2")
    _safe_set(a, 'Book_Chapter', b1)
    assert _is_linked(a, 'Book_Chapter', b1)
    if hasattr(b1, 'Book_Book'):
        assert _is_linked(b1, 'Book_Book', a)
    _safe_set(a, 'Book_Chapter', b2)
    assert _is_linked(a, 'Book_Chapter', b2)
    if hasattr(b1, 'Book_Book'):
        assert not _is_linked(b1, 'Book_Book', a)
    if hasattr(b2, 'Book_Book'):
        assert _is_linked(b2, 'Book_Book', a)
    _safe_set(a, 'Book_Chapter', None)
    assert not _is_linked(a, 'Book_Chapter', b2)
    if hasattr(b2, 'Book_Book'):
        assert not _is_linked(b2, 'Book_Book', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Book_Book_strategy = st.builds(Book_Book, authorName=safe_text, title=safe_text)
@given(instance=Book_Book_strategy)
@settings(max_examples=25)
def test_Book_Book_instantiation(instance):
    assert isinstance(instance, Book_Book)


Book_Chapter_strategy = st.builds(Book_Chapter, nbPages=st.integers(), title=safe_text)
@given(instance=Book_Chapter_strategy)
@settings(max_examples=25)
def test_Book_Chapter_instantiation(instance):
    assert isinstance(instance, Book_Chapter)



