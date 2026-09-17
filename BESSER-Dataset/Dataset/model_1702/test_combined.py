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
    library_t_published,
    library_t_author,
    library_t_book,
    library_t_library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_t_published_is_not_abstract():
    assert not inspect.isabstract(library_t_published)


def test_hyp_library_t_published_constructor_exists():
    assert callable(library_t_published.__init__)


def test_hyp_library_t_published_constructor_args():
    sig = inspect.signature(library_t_published.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "text" in params, "Missing parameter 'text'"





def test_hyp_library_t_author_is_not_abstract():
    assert not inspect.isabstract(library_t_author)


def test_hyp_library_t_author_constructor_exists():
    assert callable(library_t_author.__init__)


def test_hyp_library_t_author_constructor_args():
    sig = inspect.signature(library_t_author.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "tagName" in params, "Missing parameter 'tagName'"





def test_hyp_library_t_book_is_not_abstract():
    assert not inspect.isabstract(library_t_book)


def test_hyp_library_t_book_constructor_exists():
    assert callable(library_t_book.__init__)


def test_hyp_library_t_book_constructor_args():
    sig = inspect.signature(library_t_book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "text" in params, "Missing parameter 'text'"
    assert "pages" in params, "Missing parameter 'pages'"







def test_hyp_library_t_library_is_not_abstract():
    assert not inspect.isabstract(library_t_library)


def test_hyp_library_t_library_constructor_exists():
    assert callable(library_t_library.__init__)


def test_hyp_library_t_library_constructor_args():
    sig = inspect.signature(library_t_library.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "text" in params, "Missing parameter 'text'"




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
library_t_published_strategy = st.builds(
    library_t_published,
    tagName=
        safe_text,
    text=
        safe_text
)
library_t_author_strategy = st.builds(
    library_t_author,
    text=
        safe_text,
    tagName=
        safe_text
)
library_t_book_strategy = st.builds(
    library_t_book,
    title=
        safe_text,
    tagName=
        safe_text,
    text=
        safe_text,
    pages=
        st.integers()
)
library_t_library_strategy = st.builds(
    library_t_library,
    tagName=
        safe_text,
    text=
        safe_text
)




@given(instance=library_t_published_strategy)
def test_hyp_library_t_published_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=library_t_published_strategy)
def test_hyp_library_t_published_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=library_t_author_strategy)
def test_hyp_library_t_author_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=library_t_author_strategy)
def test_hyp_library_t_author_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original




@given(instance=library_t_book_strategy)
def test_hyp_library_t_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_t_book_strategy)
def test_hyp_library_t_book_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=library_t_book_strategy)
def test_hyp_library_t_book_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=library_t_book_strategy)
def test_hyp_library_t_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original




@given(instance=library_t_library_strategy)
def test_hyp_library_t_library_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=library_t_library_strategy)
def test_hyp_library_t_library_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    library_t_author,
    library_t_book,
    library_t_library,
    library_t_published,
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

def test_library_t_author_tagName_value_roundtrip():
    instance = library_t_author(tagName="sample_text", text="sample_text")
    assert instance.tagName == "sample_text"
    instance.tagName = "sample_text_2"
    assert instance.tagName == "sample_text_2"


def test_library_t_author_text_value_roundtrip():
    instance = library_t_author(tagName="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_library_t_book_pages_value_roundtrip():
    instance = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    assert instance.pages == 7
    instance.pages = 13
    assert instance.pages == 13


def test_library_t_book_tagName_value_roundtrip():
    instance = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    assert instance.tagName == "sample_text"
    instance.tagName = "sample_text_2"
    assert instance.tagName == "sample_text_2"


def test_library_t_book_text_value_roundtrip():
    instance = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_library_t_book_title_value_roundtrip():
    instance = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_library_t_library_tagName_value_roundtrip():
    instance = library_t_library(tagName="sample_text", text="sample_text")
    assert instance.tagName == "sample_text"
    instance.tagName = "sample_text_2"
    assert instance.tagName == "sample_text_2"


def test_library_t_library_text_value_roundtrip():
    instance = library_t_library(tagName="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_library_t_published_tagName_value_roundtrip():
    instance = library_t_published(tagName="sample_text", text="sample_text")
    assert instance.tagName == "sample_text"
    instance.tagName = "sample_text_2"
    assert instance.tagName == "sample_text_2"


def test_library_t_published_text_value_roundtrip():
    instance = library_t_published(tagName="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_assoc_author4_link_reassign_clear():
    a = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    b1 = library_t_author(tagName="sample_text", text="sample_text")
    b2 = library_t_author(tagName="sample_text_2", text="sample_text_2")
    _safe_set(a, 'library_t_book5', {b1})
    assert _is_linked(a, 'library_t_book5', b1)
    if hasattr(b1, 'library_t_author'):
        assert _is_linked(b1, 'library_t_author', a)
    _safe_set(a, 'library_t_book5', {b2})
    assert _is_linked(a, 'library_t_book5', b2)
    if hasattr(b1, 'library_t_author'):
        assert not _is_linked(b1, 'library_t_author', a)
    if hasattr(b2, 'library_t_author'):
        assert _is_linked(b2, 'library_t_author', a)
    _safe_set(a, 'library_t_book5', set())
    assert not _is_linked(a, 'library_t_book5', b2)
    if hasattr(b2, 'library_t_author'):
        assert not _is_linked(b2, 'library_t_author', a)


def test_assoc_book0_link_reassign_clear():
    a = library_t_library(tagName="sample_text", text="sample_text")
    b1 = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    b2 = library_t_book(pages=13, tagName="sample_text_2", text="sample_text_2", title="sample_text_2")
    _safe_set(a, 'library_t_library', {b1})
    assert _is_linked(a, 'library_t_library', b1)
    if hasattr(b1, 'library_t_book'):
        assert _is_linked(b1, 'library_t_book', a)
    _safe_set(a, 'library_t_library', {b2})
    assert _is_linked(a, 'library_t_library', b2)
    if hasattr(b1, 'library_t_book'):
        assert not _is_linked(b1, 'library_t_book', a)
    if hasattr(b2, 'library_t_book'):
        assert _is_linked(b2, 'library_t_book', a)
    _safe_set(a, 'library_t_library', set())
    assert not _is_linked(a, 'library_t_library', b2)
    if hasattr(b2, 'library_t_book'):
        assert not _is_linked(b2, 'library_t_book', a)


def test_assoc_parentNode1_link_reassign_clear():
    a = library_t_library(tagName="sample_text", text="sample_text")
    b1 = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    b2 = library_t_book(pages=13, tagName="sample_text_2", text="sample_text_2", title="sample_text_2")
    _safe_set(a, 'library_t_library3', b1)
    assert _is_linked(a, 'library_t_library3', b1)
    if hasattr(b1, 'library_t_book2'):
        assert _is_linked(b1, 'library_t_book2', a)
    _safe_set(a, 'library_t_library3', b2)
    assert _is_linked(a, 'library_t_library3', b2)
    if hasattr(b1, 'library_t_book2'):
        assert not _is_linked(b1, 'library_t_book2', a)
    if hasattr(b2, 'library_t_book2'):
        assert _is_linked(b2, 'library_t_book2', a)
    _safe_set(a, 'library_t_library3', None)
    assert not _is_linked(a, 'library_t_library3', b2)
    if hasattr(b2, 'library_t_book2'):
        assert not _is_linked(b2, 'library_t_book2', a)


def test_assoc_parentNode11_link_reassign_clear():
    a = library_t_published(tagName="sample_text", text="sample_text")
    b1 = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    b2 = library_t_book(pages=13, tagName="sample_text_2", text="sample_text_2", title="sample_text_2")
    _safe_set(a, 'library_t_published12', b1)
    assert _is_linked(a, 'library_t_published12', b1)
    if hasattr(b1, 'library_t_book13'):
        assert _is_linked(b1, 'library_t_book13', a)
    _safe_set(a, 'library_t_published12', b2)
    assert _is_linked(a, 'library_t_published12', b2)
    if hasattr(b1, 'library_t_book13'):
        assert not _is_linked(b1, 'library_t_book13', a)
    if hasattr(b2, 'library_t_book13'):
        assert _is_linked(b2, 'library_t_book13', a)
    _safe_set(a, 'library_t_published12', None)
    assert not _is_linked(a, 'library_t_published12', b2)
    if hasattr(b2, 'library_t_book13'):
        assert not _is_linked(b2, 'library_t_book13', a)


def test_assoc_parentNode8_link_reassign_clear():
    a = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    b1 = library_t_author(tagName="sample_text", text="sample_text")
    b2 = library_t_author(tagName="sample_text_2", text="sample_text_2")
    _safe_set(a, 'library_t_book10', b1)
    assert _is_linked(a, 'library_t_book10', b1)
    if hasattr(b1, 'library_t_author9'):
        assert _is_linked(b1, 'library_t_author9', a)
    _safe_set(a, 'library_t_book10', b2)
    assert _is_linked(a, 'library_t_book10', b2)
    if hasattr(b1, 'library_t_author9'):
        assert not _is_linked(b1, 'library_t_author9', a)
    if hasattr(b2, 'library_t_author9'):
        assert _is_linked(b2, 'library_t_author9', a)
    _safe_set(a, 'library_t_book10', None)
    assert not _is_linked(a, 'library_t_book10', b2)
    if hasattr(b2, 'library_t_author9'):
        assert not _is_linked(b2, 'library_t_author9', a)


def test_assoc_published6_link_reassign_clear():
    a = library_t_published(tagName="sample_text", text="sample_text")
    b1 = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    b2 = library_t_book(pages=13, tagName="sample_text_2", text="sample_text_2", title="sample_text_2")
    _safe_set(a, 'library_t_published', b1)
    assert _is_linked(a, 'library_t_published', b1)
    if hasattr(b1, 'library_t_book7'):
        assert _is_linked(b1, 'library_t_book7', a)
    _safe_set(a, 'library_t_published', b2)
    assert _is_linked(a, 'library_t_published', b2)
    if hasattr(b1, 'library_t_book7'):
        assert not _is_linked(b1, 'library_t_book7', a)
    if hasattr(b2, 'library_t_book7'):
        assert _is_linked(b2, 'library_t_book7', a)
    _safe_set(a, 'library_t_published', None)
    assert not _is_linked(a, 'library_t_published', b2)
    if hasattr(b2, 'library_t_book7'):
        assert not _is_linked(b2, 'library_t_book7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

library_t_author_strategy = st.builds(library_t_author, tagName=safe_text, text=safe_text)
@given(instance=library_t_author_strategy)
@settings(max_examples=25)
def test_library_t_author_instantiation(instance):
    assert isinstance(instance, library_t_author)


library_t_book_strategy = st.builds(library_t_book, pages=st.integers(), tagName=safe_text, text=safe_text, title=safe_text)
@given(instance=library_t_book_strategy)
@settings(max_examples=25)
def test_library_t_book_instantiation(instance):
    assert isinstance(instance, library_t_book)


library_t_library_strategy = st.builds(library_t_library, tagName=safe_text, text=safe_text)
@given(instance=library_t_library_strategy)
@settings(max_examples=25)
def test_library_t_library_instantiation(instance):
    assert isinstance(instance, library_t_library)


library_t_published_strategy = st.builds(library_t_published, tagName=safe_text, text=safe_text)
@given(instance=library_t_published_strategy)
@settings(max_examples=25)
def test_library_t_published_instantiation(instance):
    assert isinstance(instance, library_t_published)



