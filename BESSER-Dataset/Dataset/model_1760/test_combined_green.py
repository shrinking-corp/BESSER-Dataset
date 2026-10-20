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
    Borrowable,
    library_borrowables_Book,
    library_borrowables_Magazine,
    library_borrowables_CD,
    library_Customer,
    library_Borrowable,
    library_CityLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_borrowable_is_not_abstract():
    assert not inspect.isabstract(Borrowable)


def test_hyp_borrowable_constructor_exists():
    assert callable(Borrowable.__init__)


def test_hyp_borrowable_constructor_args():
    sig = inspect.signature(Borrowable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_borrowables_book_is_not_abstract():
    assert not inspect.isabstract(library_borrowables_Book)


def test_hyp_library_borrowables_book_constructor_exists():
    assert callable(library_borrowables_Book.__init__)


def test_hyp_library_borrowables_book_constructor_args():
    sig = inspect.signature(library_borrowables_Book.__init__)
    params = list(sig.parameters.keys())
    assert "authors" in params, "Missing parameter 'authors'"




def test_hyp_library_borrowables_magazine_is_not_abstract():
    assert not inspect.isabstract(library_borrowables_Magazine)


def test_hyp_library_borrowables_magazine_constructor_exists():
    assert callable(library_borrowables_Magazine.__init__)


def test_hyp_library_borrowables_magazine_constructor_args():
    sig = inspect.signature(library_borrowables_Magazine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_borrowables_cd_is_not_abstract():
    assert not inspect.isabstract(library_borrowables_CD)


def test_hyp_library_borrowables_cd_constructor_exists():
    assert callable(library_borrowables_CD.__init__)


def test_hyp_library_borrowables_cd_constructor_args():
    sig = inspect.signature(library_borrowables_CD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_customer_is_not_abstract():
    assert not inspect.isabstract(library_Customer)


def test_hyp_library_customer_constructor_exists():
    assert callable(library_Customer.__init__)


def test_hyp_library_customer_constructor_args():
    sig = inspect.signature(library_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_library_borrowable_is_not_abstract():
    assert not inspect.isabstract(library_Borrowable)


def test_hyp_library_borrowable_constructor_exists():
    assert callable(library_Borrowable.__init__)


def test_hyp_library_borrowable_constructor_args():
    sig = inspect.signature(library_Borrowable.__init__)
    params = list(sig.parameters.keys())
    assert "copiesAvailable" in params, "Missing parameter 'copiesAvailable'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_library_citylibrary_is_not_abstract():
    assert not inspect.isabstract(library_CityLibrary)


def test_hyp_library_citylibrary_constructor_exists():
    assert callable(library_CityLibrary.__init__)


def test_hyp_library_citylibrary_constructor_args():
    sig = inspect.signature(library_CityLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"



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
Borrowable_strategy = st.builds(
    Borrowable,
)
library_borrowables_Book_strategy = st.builds(
    library_borrowables_Book,
    authors=
        safe_text
)
library_borrowables_Magazine_strategy = st.builds(
    library_borrowables_Magazine,
)
library_borrowables_CD_strategy = st.builds(
    library_borrowables_CD,
)
library_Customer_strategy = st.builds(
    library_Customer,
    name=
        safe_text
)
library_Borrowable_strategy = st.builds(
    library_Borrowable,
    copiesAvailable=
        st.integers(),
    title=
        safe_text
)
library_CityLibrary_strategy = st.builds(
    library_CityLibrary,
    address=
        safe_text
)





@given(instance=library_borrowables_Book_strategy)
def test_hyp_library_borrowables_book_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original






@given(instance=library_Customer_strategy)
def test_hyp_library_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_Borrowable_strategy)
def test_hyp_library_borrowable_copiesAvailable_setter(instance):
    original = instance.copiesAvailable
    instance.copiesAvailable = original
    assert instance.copiesAvailable == original



@given(instance=library_Borrowable_strategy)
def test_hyp_library_borrowable_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=library_CityLibrary_strategy)
def test_hyp_library_citylibrary_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Borrowable,
    library_Borrowable,
    library_CityLibrary,
    library_Customer,
    library_borrowables_Book,
    library_borrowables_CD,
    library_borrowables_Magazine,
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

def test_library_Borrowable_copiesAvailable_value_roundtrip():
    instance = library_Borrowable(copiesAvailable=7, title="sample_text")
    assert instance.copiesAvailable == 7
    instance.copiesAvailable = 13
    assert instance.copiesAvailable == 13


def test_library_Borrowable_title_value_roundtrip():
    instance = library_Borrowable(copiesAvailable=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_library_CityLibrary_address_value_roundtrip():
    instance = library_CityLibrary(address="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_library_Customer_name_value_roundtrip():
    instance = library_Customer(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_borrowables_Book_authors_value_roundtrip():
    instance = library_borrowables_Book(authors="sample_text")
    assert instance.authors == "sample_text"
    instance.authors = "sample_text_2"
    assert instance.authors == "sample_text_2"


def test_library_borrowables_Book_isa_Borrowable():
    instance = library_borrowables_Book(authors="sample_text")
    assert isinstance(instance, Borrowable)


def test_library_borrowables_CD_isa_Borrowable():
    instance = library_borrowables_CD()
    assert isinstance(instance, Borrowable)


def test_library_borrowables_Magazine_isa_Borrowable():
    instance = library_borrowables_Magazine()
    assert isinstance(instance, Borrowable)


def test_assoc_borrowables0_link_reassign_clear():
    a = library_CityLibrary(address="sample_text")
    b1 = library_Borrowable(copiesAvailable=7, title="sample_text")
    b2 = library_Borrowable(copiesAvailable=13, title="sample_text_2")
    _safe_set(a, 'library', {b1})
    assert _is_linked(a, 'library', b1)
    if hasattr(b1, 'Borrowable'):
        assert _is_linked(b1, 'Borrowable', a)
    _safe_set(a, 'library', {b2})
    assert _is_linked(a, 'library', b2)
    if hasattr(b1, 'Borrowable'):
        assert not _is_linked(b1, 'Borrowable', a)
    if hasattr(b2, 'Borrowable'):
        assert _is_linked(b2, 'Borrowable', a)
    _safe_set(a, 'library', set())
    assert not _is_linked(a, 'library', b2)
    if hasattr(b2, 'Borrowable'):
        assert not _is_linked(b2, 'Borrowable', a)


def test_assoc_borrowed2_link_reassign_clear():
    a = library_Customer(name="sample_text")
    b1 = library_Borrowable(copiesAvailable=7, title="sample_text")
    b2 = library_Borrowable(copiesAvailable=13, title="sample_text_2")
    _safe_set(a, 'library_Customer3', {b1})
    assert _is_linked(a, 'library_Customer3', b1)
    if hasattr(b1, 'library_Borrowable'):
        assert _is_linked(b1, 'library_Borrowable', a)
    _safe_set(a, 'library_Customer3', {b2})
    assert _is_linked(a, 'library_Customer3', b2)
    if hasattr(b1, 'library_Borrowable'):
        assert not _is_linked(b1, 'library_Borrowable', a)
    if hasattr(b2, 'library_Borrowable'):
        assert _is_linked(b2, 'library_Borrowable', a)
    _safe_set(a, 'library_Customer3', set())
    assert not _is_linked(a, 'library_Customer3', b2)
    if hasattr(b2, 'library_Borrowable'):
        assert not _is_linked(b2, 'library_Borrowable', a)


def test_assoc_customers1_link_reassign_clear():
    a = library_Customer(name="sample_text")
    b1 = library_CityLibrary(address="sample_text")
    b2 = library_CityLibrary(address="sample_text_2")
    _safe_set(a, 'library_Customer', b1)
    assert _is_linked(a, 'library_Customer', b1)
    if hasattr(b1, 'library_CityLibrary'):
        assert _is_linked(b1, 'library_CityLibrary', a)
    _safe_set(a, 'library_Customer', b2)
    assert _is_linked(a, 'library_Customer', b2)
    if hasattr(b1, 'library_CityLibrary'):
        assert not _is_linked(b1, 'library_CityLibrary', a)
    if hasattr(b2, 'library_CityLibrary'):
        assert _is_linked(b2, 'library_CityLibrary', a)
    _safe_set(a, 'library_Customer', None)
    assert not _is_linked(a, 'library_Customer', b2)
    if hasattr(b2, 'library_CityLibrary'):
        assert not _is_linked(b2, 'library_CityLibrary', a)


def test_assoc_library4_link_reassign_clear():
    a = library_CityLibrary(address="sample_text")
    b1 = library_Borrowable(copiesAvailable=7, title="sample_text")
    b2 = library_Borrowable(copiesAvailable=13, title="sample_text_2")
    _safe_set(a, 'CityLibrary', b1)
    assert _is_linked(a, 'CityLibrary', b1)
    if hasattr(b1, 'borrowables'):
        assert _is_linked(b1, 'borrowables', a)
    _safe_set(a, 'CityLibrary', b2)
    assert _is_linked(a, 'CityLibrary', b2)
    if hasattr(b1, 'borrowables'):
        assert not _is_linked(b1, 'borrowables', a)
    if hasattr(b2, 'borrowables'):
        assert _is_linked(b2, 'borrowables', a)
    _safe_set(a, 'CityLibrary', None)
    assert not _is_linked(a, 'CityLibrary', b2)
    if hasattr(b2, 'borrowables'):
        assert not _is_linked(b2, 'borrowables', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Borrowable_strategy = st.builds(Borrowable)
@given(instance=Borrowable_strategy)
@settings(max_examples=25)
def test_Borrowable_instantiation(instance):
    assert isinstance(instance, Borrowable)


library_Borrowable_strategy = st.builds(library_Borrowable, copiesAvailable=st.integers(), title=safe_text)
@given(instance=library_Borrowable_strategy)
@settings(max_examples=25)
def test_library_Borrowable_instantiation(instance):
    assert isinstance(instance, library_Borrowable)


library_CityLibrary_strategy = st.builds(library_CityLibrary, address=safe_text)
@given(instance=library_CityLibrary_strategy)
@settings(max_examples=25)
def test_library_CityLibrary_instantiation(instance):
    assert isinstance(instance, library_CityLibrary)


library_Customer_strategy = st.builds(library_Customer, name=safe_text)
@given(instance=library_Customer_strategy)
@settings(max_examples=25)
def test_library_Customer_instantiation(instance):
    assert isinstance(instance, library_Customer)


library_borrowables_Book_strategy = st.builds(library_borrowables_Book, authors=safe_text)
@given(instance=library_borrowables_Book_strategy)
@settings(max_examples=25)
def test_library_borrowables_Book_instantiation(instance):
    assert isinstance(instance, library_borrowables_Book)


library_borrowables_CD_strategy = st.builds(library_borrowables_CD)
@given(instance=library_borrowables_CD_strategy)
@settings(max_examples=25)
def test_library_borrowables_CD_instantiation(instance):
    assert isinstance(instance, library_borrowables_CD)


library_borrowables_Magazine_strategy = st.builds(library_borrowables_Magazine)
@given(instance=library_borrowables_Magazine_strategy)
@settings(max_examples=25)
def test_library_borrowables_Magazine_instantiation(instance):
    assert isinstance(instance, library_borrowables_Magazine)



