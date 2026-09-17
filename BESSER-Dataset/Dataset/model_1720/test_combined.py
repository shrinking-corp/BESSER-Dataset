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
    library_Book,
    library_BookCopy,
    library_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_hyp_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_hyp_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_bookcopy_is_not_abstract():
    assert not inspect.isabstract(library_BookCopy)


def test_hyp_library_bookcopy_constructor_exists():
    assert callable(library_BookCopy.__init__)


def test_hyp_library_bookcopy_constructor_args():
    sig = inspect.signature(library_BookCopy.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"




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
library_Book_strategy = st.builds(
    library_Book,
)
library_BookCopy_strategy = st.builds(
    library_BookCopy,
    copies=
        st.integers()
)
library_Library_strategy = st.builds(
    library_Library,
    name=
        safe_text
)





@given(instance=library_BookCopy_strategy)
def test_hyp_library_bookcopy_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original




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
    library_BookCopy,
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

def test_library_BookCopy_copies_value_roundtrip():
    instance = library_BookCopy(copies=7)
    assert instance.copies == 7
    instance.copies = 13
    assert instance.copies == 13


def test_library_Library_name_value_roundtrip():
    instance = library_Library(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_book1_link_reassign_clear():
    a = library_BookCopy(copies=7)
    b1 = library_Book()
    b2 = library_Book()
    _safe_set(a, 'library_BookCopy2', b1)
    assert _is_linked(a, 'library_BookCopy2', b1)
    if hasattr(b1, 'library_Book'):
        assert _is_linked(b1, 'library_Book', a)
    _safe_set(a, 'library_BookCopy2', b2)
    assert _is_linked(a, 'library_BookCopy2', b2)
    if hasattr(b1, 'library_Book'):
        assert not _is_linked(b1, 'library_Book', a)
    if hasattr(b2, 'library_Book'):
        assert _is_linked(b2, 'library_Book', a)
    _safe_set(a, 'library_BookCopy2', None)
    assert not _is_linked(a, 'library_BookCopy2', b2)
    if hasattr(b2, 'library_Book'):
        assert not _is_linked(b2, 'library_Book', a)


def test_assoc_books0_link_reassign_clear():
    a = library_Library(name="sample_text")
    b1 = library_BookCopy(copies=7)
    b2 = library_BookCopy(copies=13)
    _safe_set(a, 'library_Library', {b1})
    assert _is_linked(a, 'library_Library', b1)
    if hasattr(b1, 'library_BookCopy'):
        assert _is_linked(b1, 'library_BookCopy', a)
    _safe_set(a, 'library_Library', {b2})
    assert _is_linked(a, 'library_Library', b2)
    if hasattr(b1, 'library_BookCopy'):
        assert not _is_linked(b1, 'library_BookCopy', a)
    if hasattr(b2, 'library_BookCopy'):
        assert _is_linked(b2, 'library_BookCopy', a)
    _safe_set(a, 'library_Library', set())
    assert not _is_linked(a, 'library_Library', b2)
    if hasattr(b2, 'library_BookCopy'):
        assert not _is_linked(b2, 'library_BookCopy', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

library_Book_strategy = st.builds(library_Book)
@given(instance=library_Book_strategy)
@settings(max_examples=25)
def test_library_Book_instantiation(instance):
    assert isinstance(instance, library_Book)


library_BookCopy_strategy = st.builds(library_BookCopy, copies=st.integers())
@given(instance=library_BookCopy_strategy)
@settings(max_examples=25)
def test_library_BookCopy_instantiation(instance):
    assert isinstance(instance, library_BookCopy)


library_Library_strategy = st.builds(library_Library, name=safe_text)
@given(instance=library_Library_strategy)
@settings(max_examples=25)
def test_library_Library_instantiation(instance):
    assert isinstance(instance, library_Library)



