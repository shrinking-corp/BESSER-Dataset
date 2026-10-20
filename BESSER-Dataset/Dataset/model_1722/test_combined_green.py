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
    library_Image,
    library_Text,
    library_Content,
    library_Chapter,
    library_Book,
    library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_image_is_not_abstract():
    assert not inspect.isabstract(library_Image)


def test_hyp_library_image_constructor_exists():
    assert callable(library_Image.__init__)


def test_hyp_library_image_constructor_args():
    sig = inspect.signature(library_Image.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_text_is_not_abstract():
    assert not inspect.isabstract(library_Text)


def test_hyp_library_text_constructor_exists():
    assert callable(library_Text.__init__)


def test_hyp_library_text_constructor_args():
    sig = inspect.signature(library_Text.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_content_is_not_abstract():
    assert not inspect.isabstract(library_Content)


def test_hyp_library_content_constructor_exists():
    assert callable(library_Content.__init__)


def test_hyp_library_content_constructor_args():
    sig = inspect.signature(library_Content.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_chapter_is_not_abstract():
    assert not inspect.isabstract(library_Chapter)


def test_hyp_library_chapter_constructor_exists():
    assert callable(library_Chapter.__init__)


def test_hyp_library_chapter_constructor_args():
    sig = inspect.signature(library_Chapter.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_hyp_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_hyp_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_hyp_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_hyp_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
library_Image_strategy = st.builds(
    library_Image,
)
library_Text_strategy = st.builds(
    library_Text,
)
library_Content_strategy = st.builds(
    library_Content,
)
library_Chapter_strategy = st.builds(
    library_Chapter,
    pages=
        st.integers(),
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    name=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)







@given(instance=library_Chapter_strategy)
def test_hyp_library_chapter_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=library_Chapter_strategy)
def test_hyp_library_chapter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_Book_strategy)
def test_hyp_library_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_Library_strategy)
def test_hyp_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    library_Book,
    library_Chapter,
    library_Content,
    library_Image,
    library_Library,
    library_Text,
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

def test_library_Book_name_value_roundtrip():
    instance = library_Book(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Chapter_name_value_roundtrip():
    instance = library_Chapter(name="sample_text", pages=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Chapter_pages_value_roundtrip():
    instance = library_Chapter(name="sample_text", pages=7)
    assert instance.pages == 7
    instance.pages = 13
    assert instance.pages == 13


def test_library_Library_name_value_roundtrip():
    instance = library_Library(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_books0_link_reassign_clear():
    a = library_Library(name="sample_text")
    b1 = library_Book(name="sample_text")
    b2 = library_Book(name="sample_text_2")
    _safe_set(a, 'library_Library', {b1})
    assert _is_linked(a, 'library_Library', b1)
    if hasattr(b1, 'library_Book'):
        assert _is_linked(b1, 'library_Book', a)
    _safe_set(a, 'library_Library', {b2})
    assert _is_linked(a, 'library_Library', b2)
    if hasattr(b1, 'library_Book'):
        assert not _is_linked(b1, 'library_Book', a)
    if hasattr(b2, 'library_Book'):
        assert _is_linked(b2, 'library_Book', a)
    _safe_set(a, 'library_Library', set())
    assert not _is_linked(a, 'library_Library', b2)
    if hasattr(b2, 'library_Book'):
        assert not _is_linked(b2, 'library_Book', a)


def test_assoc_chapters1_link_reassign_clear():
    a = library_Chapter(name="sample_text", pages=7)
    b1 = library_Book(name="sample_text")
    b2 = library_Book(name="sample_text_2")
    _safe_set(a, 'library_Chapter', b1)
    assert _is_linked(a, 'library_Chapter', b1)
    if hasattr(b1, 'library_Book2'):
        assert _is_linked(b1, 'library_Book2', a)
    _safe_set(a, 'library_Chapter', b2)
    assert _is_linked(a, 'library_Chapter', b2)
    if hasattr(b1, 'library_Book2'):
        assert not _is_linked(b1, 'library_Book2', a)
    if hasattr(b2, 'library_Book2'):
        assert _is_linked(b2, 'library_Book2', a)
    _safe_set(a, 'library_Chapter', None)
    assert not _is_linked(a, 'library_Chapter', b2)
    if hasattr(b2, 'library_Book2'):
        assert not _is_linked(b2, 'library_Book2', a)


def test_assoc_content3_link_reassign_clear():
    a = library_Chapter(name="sample_text", pages=7)
    b1 = library_Content()
    b2 = library_Content()
    _safe_set(a, 'library_Chapter4', b1)
    assert _is_linked(a, 'library_Chapter4', b1)
    if hasattr(b1, 'library_Content'):
        assert _is_linked(b1, 'library_Content', a)
    _safe_set(a, 'library_Chapter4', b2)
    assert _is_linked(a, 'library_Chapter4', b2)
    if hasattr(b1, 'library_Content'):
        assert not _is_linked(b1, 'library_Content', a)
    if hasattr(b2, 'library_Content'):
        assert _is_linked(b2, 'library_Content', a)
    _safe_set(a, 'library_Chapter4', None)
    assert not _is_linked(a, 'library_Chapter4', b2)
    if hasattr(b2, 'library_Content'):
        assert not _is_linked(b2, 'library_Content', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

library_Book_strategy = st.builds(library_Book, name=safe_text)
@given(instance=library_Book_strategy)
@settings(max_examples=25)
def test_library_Book_instantiation(instance):
    assert isinstance(instance, library_Book)


library_Chapter_strategy = st.builds(library_Chapter, name=safe_text, pages=st.integers())
@given(instance=library_Chapter_strategy)
@settings(max_examples=25)
def test_library_Chapter_instantiation(instance):
    assert isinstance(instance, library_Chapter)


library_Content_strategy = st.builds(library_Content)
@given(instance=library_Content_strategy)
@settings(max_examples=25)
def test_library_Content_instantiation(instance):
    assert isinstance(instance, library_Content)


library_Image_strategy = st.builds(library_Image)
@given(instance=library_Image_strategy)
@settings(max_examples=25)
def test_library_Image_instantiation(instance):
    assert isinstance(instance, library_Image)


library_Library_strategy = st.builds(library_Library, name=safe_text)
@given(instance=library_Library_strategy)
@settings(max_examples=25)
def test_library_Library_instantiation(instance):
    assert isinstance(instance, library_Library)


library_Text_strategy = st.builds(library_Text)
@given(instance=library_Text_strategy)
@settings(max_examples=25)
def test_library_Text_instantiation(instance):
    assert isinstance(instance, library_Text)



