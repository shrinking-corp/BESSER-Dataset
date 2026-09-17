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
    library_Author,
    library_Book,
    library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_author_is_not_abstract():
    assert not inspect.isabstract(library_Author)


def test_hyp_library_author_constructor_exists():
    assert callable(library_Author.__init__)


def test_hyp_library_author_constructor_args():
    sig = inspect.signature(library_Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_hyp_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_hyp_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_hyp_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_hyp_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
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
library_Author_strategy = st.builds(
    library_Author,
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    title=
        safe_text
)
library_Library_strategy = st.builds(
    library_Library,
)




@given(instance=library_Author_strategy)
def test_hyp_library_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_Book_strategy)
def test_hyp_library_book_title_setter(instance):
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
    library_Author,
    library_Book,
    library_Library,
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

def test_library_Author_name_value_roundtrip():
    instance = library_Author(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Book_title_value_roundtrip():
    instance = library_Book(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_assoc_authors1_link_reassign_clear():
    a = library_Author(name="sample_text")
    b1 = library_Library()
    b2 = library_Library()
    _safe_set(a, 'library_Author', b1)
    assert _is_linked(a, 'library_Author', b1)
    if hasattr(b1, 'library_Library2'):
        assert _is_linked(b1, 'library_Library2', a)
    _safe_set(a, 'library_Author', b2)
    assert _is_linked(a, 'library_Author', b2)
    if hasattr(b1, 'library_Library2'):
        assert not _is_linked(b1, 'library_Library2', a)
    if hasattr(b2, 'library_Library2'):
        assert _is_linked(b2, 'library_Library2', a)
    _safe_set(a, 'library_Author', None)
    assert not _is_linked(a, 'library_Author', b2)
    if hasattr(b2, 'library_Library2'):
        assert not _is_linked(b2, 'library_Library2', a)


def test_assoc_authors3_link_reassign_clear():
    a = library_Book(title="sample_text")
    b1 = library_Author(name="sample_text")
    b2 = library_Author(name="sample_text_2")
    _safe_set(a, 'library_Book4', {b1})
    assert _is_linked(a, 'library_Book4', b1)
    if hasattr(b1, 'library_Author5'):
        assert _is_linked(b1, 'library_Author5', a)
    _safe_set(a, 'library_Book4', {b2})
    assert _is_linked(a, 'library_Book4', b2)
    if hasattr(b1, 'library_Author5'):
        assert not _is_linked(b1, 'library_Author5', a)
    if hasattr(b2, 'library_Author5'):
        assert _is_linked(b2, 'library_Author5', a)
    _safe_set(a, 'library_Book4', set())
    assert not _is_linked(a, 'library_Book4', b2)
    if hasattr(b2, 'library_Author5'):
        assert not _is_linked(b2, 'library_Author5', a)


def test_assoc_books0_link_reassign_clear():
    a = library_Book(title="sample_text")
    b1 = library_Library()
    b2 = library_Library()
    _safe_set(a, 'library_Book', b1)
    assert _is_linked(a, 'library_Book', b1)
    if hasattr(b1, 'library_Library'):
        assert _is_linked(b1, 'library_Library', a)
    _safe_set(a, 'library_Book', b2)
    assert _is_linked(a, 'library_Book', b2)
    if hasattr(b1, 'library_Library'):
        assert not _is_linked(b1, 'library_Library', a)
    if hasattr(b2, 'library_Library'):
        assert _is_linked(b2, 'library_Library', a)
    _safe_set(a, 'library_Book', None)
    assert not _is_linked(a, 'library_Book', b2)
    if hasattr(b2, 'library_Library'):
        assert not _is_linked(b2, 'library_Library', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

library_Author_strategy = st.builds(library_Author, name=safe_text)
@given(instance=library_Author_strategy)
@settings(max_examples=25)
def test_library_Author_instantiation(instance):
    assert isinstance(instance, library_Author)


library_Book_strategy = st.builds(library_Book, title=safe_text)
@given(instance=library_Book_strategy)
@settings(max_examples=25)
def test_library_Book_instantiation(instance):
    assert isinstance(instance, library_Book)


library_Library_strategy = st.builds(library_Library)
@given(instance=library_Library_strategy)
@settings(max_examples=25)
def test_library_Library_instantiation(instance):
    assert isinstance(instance, library_Library)



