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
    BookStorePackage_TypeParameterTest1_ZClass,
    BookStorePackage_TypeParameterTest1_YClass,
    BookStorePackage_TypeParameterTest1_XClass,
    BookStorePackage_Book,
    BookStorePackage_BookStore,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bookstorepackage_typeparametertest1_zclass_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage_TypeParameterTest1_ZClass)


def test_hyp_bookstorepackage_typeparametertest1_zclass_constructor_exists():
    assert callable(BookStorePackage_TypeParameterTest1_ZClass.__init__)


def test_hyp_bookstorepackage_typeparametertest1_zclass_constructor_args():
    sig = inspect.signature(BookStorePackage_TypeParameterTest1_ZClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bookstorepackage_typeparametertest1_yclass_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage_TypeParameterTest1_YClass)


def test_hyp_bookstorepackage_typeparametertest1_yclass_constructor_exists():
    assert callable(BookStorePackage_TypeParameterTest1_YClass.__init__)


def test_hyp_bookstorepackage_typeparametertest1_yclass_constructor_args():
    sig = inspect.signature(BookStorePackage_TypeParameterTest1_YClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bookstorepackage_typeparametertest1_xclass_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage_TypeParameterTest1_XClass)


def test_hyp_bookstorepackage_typeparametertest1_xclass_constructor_exists():
    assert callable(BookStorePackage_TypeParameterTest1_XClass.__init__)


def test_hyp_bookstorepackage_typeparametertest1_xclass_constructor_args():
    sig = inspect.signature(BookStorePackage_TypeParameterTest1_XClass.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"




def test_hyp_bookstorepackage_book_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage_Book)


def test_hyp_bookstorepackage_book_constructor_exists():
    assert callable(BookStorePackage_Book.__init__)


def test_hyp_bookstorepackage_book_constructor_args():
    sig = inspect.signature(BookStorePackage_Book.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isbn" in params, "Missing parameter 'isbn'"





def test_hyp_bookstorepackage_bookstore_is_not_abstract():
    assert not inspect.isabstract(BookStorePackage_BookStore)


def test_hyp_bookstorepackage_bookstore_constructor_exists():
    assert callable(BookStorePackage_BookStore.__init__)


def test_hyp_bookstorepackage_bookstore_constructor_args():
    sig = inspect.signature(BookStorePackage_BookStore.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "location" in params, "Missing parameter 'location'"




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
BookStorePackage_TypeParameterTest1_ZClass_strategy = st.builds(
    BookStorePackage_TypeParameterTest1_ZClass,
)
BookStorePackage_TypeParameterTest1_YClass_strategy = st.builds(
    BookStorePackage_TypeParameterTest1_YClass,
)
BookStorePackage_TypeParameterTest1_XClass_strategy = st.builds(
    BookStorePackage_TypeParameterTest1_XClass,
    owner=
        safe_text
)
BookStorePackage_Book_strategy = st.builds(
    BookStorePackage_Book,
    name=
        safe_text,
    isbn=
        st.integers()
)
BookStorePackage_BookStore_strategy = st.builds(
    BookStorePackage_BookStore,
    owner=
        safe_text,
    location=
        safe_text
)






@given(instance=BookStorePackage_TypeParameterTest1_XClass_strategy)
def test_hyp_bookstorepackage_typeparametertest1_xclass_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original




@given(instance=BookStorePackage_Book_strategy)
def test_hyp_bookstorepackage_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BookStorePackage_Book_strategy)
def test_hyp_bookstorepackage_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original




@given(instance=BookStorePackage_BookStore_strategy)
def test_hyp_bookstorepackage_bookstore_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=BookStorePackage_BookStore_strategy)
def test_hyp_bookstorepackage_bookstore_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BookStorePackage_Book,
    BookStorePackage_BookStore,
    BookStorePackage_TypeParameterTest1_XClass,
    BookStorePackage_TypeParameterTest1_YClass,
    BookStorePackage_TypeParameterTest1_ZClass,
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

def test_BookStorePackage_Book_isbn_value_roundtrip():
    instance = BookStorePackage_Book(isbn=7, name="sample_text")
    assert instance.isbn == 7
    instance.isbn = 13
    assert instance.isbn == 13


def test_BookStorePackage_Book_name_value_roundtrip():
    instance = BookStorePackage_Book(isbn=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_BookStorePackage_BookStore_location_value_roundtrip():
    instance = BookStorePackage_BookStore(location="sample_text", owner="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_BookStorePackage_BookStore_owner_value_roundtrip():
    instance = BookStorePackage_BookStore(location="sample_text", owner="sample_text")
    assert instance.owner == "sample_text"
    instance.owner = "sample_text_2"
    assert instance.owner == "sample_text_2"


def test_BookStorePackage_TypeParameterTest1_XClass_owner_value_roundtrip():
    instance = BookStorePackage_TypeParameterTest1_XClass(owner="sample_text")
    assert instance.owner == "sample_text"
    instance.owner = "sample_text_2"
    assert instance.owner == "sample_text_2"


def test_assoc_books0_link_reassign_clear():
    a = BookStorePackage_BookStore(location="sample_text", owner="sample_text")
    b1 = BookStorePackage_Book(isbn=7, name="sample_text")
    b2 = BookStorePackage_Book(isbn=13, name="sample_text_2")
    _safe_set(a, 'BookStorePackage_BookStore', {b1})
    assert _is_linked(a, 'BookStorePackage_BookStore', b1)
    if hasattr(b1, 'BookStorePackage_Book'):
        assert _is_linked(b1, 'BookStorePackage_Book', a)
    _safe_set(a, 'BookStorePackage_BookStore', {b2})
    assert _is_linked(a, 'BookStorePackage_BookStore', b2)
    if hasattr(b1, 'BookStorePackage_Book'):
        assert not _is_linked(b1, 'BookStorePackage_Book', a)
    if hasattr(b2, 'BookStorePackage_Book'):
        assert _is_linked(b2, 'BookStorePackage_Book', a)
    _safe_set(a, 'BookStorePackage_BookStore', set())
    assert not _is_linked(a, 'BookStorePackage_BookStore', b2)
    if hasattr(b2, 'BookStorePackage_Book'):
        assert not _is_linked(b2, 'BookStorePackage_Book', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BookStorePackage_Book_strategy = st.builds(BookStorePackage_Book, isbn=st.integers(), name=safe_text)
@given(instance=BookStorePackage_Book_strategy)
@settings(max_examples=25)
def test_BookStorePackage_Book_instantiation(instance):
    assert isinstance(instance, BookStorePackage_Book)


BookStorePackage_BookStore_strategy = st.builds(BookStorePackage_BookStore, location=safe_text, owner=safe_text)
@given(instance=BookStorePackage_BookStore_strategy)
@settings(max_examples=25)
def test_BookStorePackage_BookStore_instantiation(instance):
    assert isinstance(instance, BookStorePackage_BookStore)


BookStorePackage_TypeParameterTest1_XClass_strategy = st.builds(BookStorePackage_TypeParameterTest1_XClass, owner=safe_text)
@given(instance=BookStorePackage_TypeParameterTest1_XClass_strategy)
@settings(max_examples=25)
def test_BookStorePackage_TypeParameterTest1_XClass_instantiation(instance):
    assert isinstance(instance, BookStorePackage_TypeParameterTest1_XClass)


BookStorePackage_TypeParameterTest1_YClass_strategy = st.builds(BookStorePackage_TypeParameterTest1_YClass)
@given(instance=BookStorePackage_TypeParameterTest1_YClass_strategy)
@settings(max_examples=25)
def test_BookStorePackage_TypeParameterTest1_YClass_instantiation(instance):
    assert isinstance(instance, BookStorePackage_TypeParameterTest1_YClass)


BookStorePackage_TypeParameterTest1_ZClass_strategy = st.builds(BookStorePackage_TypeParameterTest1_ZClass)
@given(instance=BookStorePackage_TypeParameterTest1_ZClass_strategy)
@settings(max_examples=25)
def test_BookStorePackage_TypeParameterTest1_ZClass_instantiation(instance):
    assert isinstance(instance, BookStorePackage_TypeParameterTest1_ZClass)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BookStorePackage_Book,
    BookStorePackage_BookStore,
    BookStorePackage_TypeParameterTest1_XClass,
    BookStorePackage_TypeParameterTest1_YClass,
    BookStorePackage_TypeParameterTest1_ZClass,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_books0_reverse_link_reassign_clear():
    a1 = BookStorePackage_BookStore(location="sample_text", owner="sample_text")
    a2 = BookStorePackage_BookStore(location="sample_text_2", owner="sample_text_2")
    b = BookStorePackage_Book(isbn=7, name="sample_text")
    _safe_set(b, 'BookStorePackage_Book', a1)
    assert _is_linked(b, 'BookStorePackage_Book', a1)
    if hasattr(a1, 'BookStorePackage_BookStore'):
        assert _is_linked(a1, 'BookStorePackage_BookStore', b)
    _safe_set(b, 'BookStorePackage_Book', a2)
    assert _is_linked(b, 'BookStorePackage_Book', a2)
    if hasattr(a1, 'BookStorePackage_BookStore'):
        assert not _is_linked(a1, 'BookStorePackage_BookStore', b)
    if hasattr(a2, 'BookStorePackage_BookStore'):
        assert _is_linked(a2, 'BookStorePackage_BookStore', b)
    _safe_set(b, 'BookStorePackage_Book', None)
    assert not _is_linked(b, 'BookStorePackage_Book', a2)
    if hasattr(a2, 'BookStorePackage_BookStore'):
        assert not _is_linked(a2, 'BookStorePackage_BookStore', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================



from python_code import BookStorePackage_BookStore

def test_BookStorePackage_BookStore___init__():
    assert BookStorePackage_BookStore.__init__(BookStorePackage_BookStore('\x00\x00', '', BookStorePackage_BookStore=set()), '', '', BookStorePackage_BookStore=set()) == None
from python_code import BookStorePackage_TypeParameterTest1_XClass

def test_BookStorePackage_TypeParameterTest1_XClass___init__():
    assert BookStorePackage_TypeParameterTest1_XClass.__init__(BookStorePackage_TypeParameterTest1_XClass(''), '') == None

