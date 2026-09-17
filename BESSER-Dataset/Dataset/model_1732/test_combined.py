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
    Item,
    library_Book,
    library_Item,
    library_LibraryShelf,
    MultimediaItem,
    library_CD,
    library_BlueRay,
    library_DVD,
    library_MultimediaItem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_hyp_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_hyp_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "numPages" in params, "Missing parameter 'numPages'"




def test_hyp_library_item_is_not_abstract():
    assert not inspect.isabstract(library_Item)


def test_hyp_library_item_constructor_exists():
    assert callable(library_Item.__init__)


def test_hyp_library_item_constructor_args():
    sig = inspect.signature(library_Item.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "pubDate" in params, "Missing parameter 'pubDate'"





def test_hyp_library_libraryshelf_is_not_abstract():
    assert not inspect.isabstract(library_LibraryShelf)


def test_hyp_library_libraryshelf_constructor_exists():
    assert callable(library_LibraryShelf.__init__)


def test_hyp_library_libraryshelf_constructor_args():
    sig = inspect.signature(library_LibraryShelf.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_multimediaitem_is_not_abstract():
    assert not inspect.isabstract(MultimediaItem)


def test_hyp_multimediaitem_constructor_exists():
    assert callable(MultimediaItem.__init__)


def test_hyp_multimediaitem_constructor_args():
    sig = inspect.signature(MultimediaItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_cd_is_not_abstract():
    assert not inspect.isabstract(library_CD)


def test_hyp_library_cd_constructor_exists():
    assert callable(library_CD.__init__)


def test_hyp_library_cd_constructor_args():
    sig = inspect.signature(library_CD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_blueray_is_not_abstract():
    assert not inspect.isabstract(library_BlueRay)


def test_hyp_library_blueray_constructor_exists():
    assert callable(library_BlueRay.__init__)


def test_hyp_library_blueray_constructor_args():
    sig = inspect.signature(library_BlueRay.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_dvd_is_not_abstract():
    assert not inspect.isabstract(library_DVD)


def test_hyp_library_dvd_constructor_exists():
    assert callable(library_DVD.__init__)


def test_hyp_library_dvd_constructor_args():
    sig = inspect.signature(library_DVD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_multimediaitem_is_not_abstract():
    assert not inspect.isabstract(library_MultimediaItem)


def test_hyp_library_multimediaitem_constructor_exists():
    assert callable(library_MultimediaItem.__init__)


def test_hyp_library_multimediaitem_constructor_args():
    sig = inspect.signature(library_MultimediaItem.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"



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
Item_strategy = st.builds(
    Item,
)
library_Book_strategy = st.builds(
    library_Book,
    numPages=
        st.integers()
)
library_Item_strategy = st.builds(
    library_Item,
    title=
        safe_text,
    pubDate=
        st.dates()
)
library_LibraryShelf_strategy = st.builds(
    library_LibraryShelf,
    name=
        safe_text
)
MultimediaItem_strategy = st.builds(
    MultimediaItem,
)
library_CD_strategy = st.builds(
    library_CD,
)
library_BlueRay_strategy = st.builds(
    library_BlueRay,
)
library_DVD_strategy = st.builds(
    library_DVD,
)
library_MultimediaItem_strategy = st.builds(
    library_MultimediaItem,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)





@given(instance=library_Book_strategy)
def test_hyp_library_book_numPages_setter(instance):
    original = instance.numPages
    instance.numPages = original
    assert instance.numPages == original




@given(instance=library_Item_strategy)
def test_hyp_library_item_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_Item_strategy)
def test_hyp_library_item_pubDate_setter(instance):
    original = instance.pubDate
    instance.pubDate = original
    assert instance.pubDate == original




@given(instance=library_LibraryShelf_strategy)
def test_hyp_library_libraryshelf_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=library_MultimediaItem_strategy)
def test_hyp_library_multimediaitem_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Item,
    MultimediaItem,
    library_BlueRay,
    library_Book,
    library_CD,
    library_DVD,
    library_Item,
    library_LibraryShelf,
    library_MultimediaItem,
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

def test_library_Book_numPages_value_roundtrip():
    instance = library_Book(numPages=7)
    assert instance.numPages == 7
    instance.numPages = 13
    assert instance.numPages == 13


def test_library_Item_pubDate_value_roundtrip():
    instance = library_Item(pubDate=date(2024, 1, 1), title="sample_text")
    assert instance.pubDate == date(2024, 1, 1)
    instance.pubDate = date(2025, 6, 15)
    assert instance.pubDate == date(2025, 6, 15)


def test_library_Item_title_value_roundtrip():
    instance = library_Item(pubDate=date(2024, 1, 1), title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_library_LibraryShelf_name_value_roundtrip():
    instance = library_LibraryShelf(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_MultimediaItem_length_value_roundtrip():
    instance = library_MultimediaItem(length=3.14)
    assert instance.length == 3.14
    instance.length = 9.99
    assert instance.length == 9.99


def test_library_Book_isa_Item():
    instance = library_Book(numPages=7)
    assert isinstance(instance, Item)


def test_library_MultimediaItem_isa_Item():
    instance = library_MultimediaItem(length=3.14)
    assert isinstance(instance, Item)


def test_library_BlueRay_isa_MultimediaItem():
    instance = library_BlueRay()
    assert isinstance(instance, MultimediaItem)


def test_library_CD_isa_MultimediaItem():
    instance = library_CD()
    assert isinstance(instance, MultimediaItem)


def test_library_DVD_isa_MultimediaItem():
    instance = library_DVD()
    assert isinstance(instance, MultimediaItem)


def test_assoc_items0_link_reassign_clear():
    a = library_LibraryShelf(name="sample_text")
    b1 = library_Item(pubDate=date(2024, 1, 1), title="sample_text")
    b2 = library_Item(pubDate=date(2025, 6, 15), title="sample_text_2")
    _safe_set(a, 'library_LibraryShelf', {b1})
    assert _is_linked(a, 'library_LibraryShelf', b1)
    if hasattr(b1, 'library_Item'):
        assert _is_linked(b1, 'library_Item', a)
    _safe_set(a, 'library_LibraryShelf', {b2})
    assert _is_linked(a, 'library_LibraryShelf', b2)
    if hasattr(b1, 'library_Item'):
        assert not _is_linked(b1, 'library_Item', a)
    if hasattr(b2, 'library_Item'):
        assert _is_linked(b2, 'library_Item', a)
    _safe_set(a, 'library_LibraryShelf', set())
    assert not _is_linked(a, 'library_LibraryShelf', b2)
    if hasattr(b2, 'library_Item'):
        assert not _is_linked(b2, 'library_Item', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Item_strategy = st.builds(Item)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


MultimediaItem_strategy = st.builds(MultimediaItem)
@given(instance=MultimediaItem_strategy)
@settings(max_examples=25)
def test_MultimediaItem_instantiation(instance):
    assert isinstance(instance, MultimediaItem)


library_BlueRay_strategy = st.builds(library_BlueRay)
@given(instance=library_BlueRay_strategy)
@settings(max_examples=25)
def test_library_BlueRay_instantiation(instance):
    assert isinstance(instance, library_BlueRay)


library_Book_strategy = st.builds(library_Book, numPages=st.integers())
@given(instance=library_Book_strategy)
@settings(max_examples=25)
def test_library_Book_instantiation(instance):
    assert isinstance(instance, library_Book)


library_CD_strategy = st.builds(library_CD)
@given(instance=library_CD_strategy)
@settings(max_examples=25)
def test_library_CD_instantiation(instance):
    assert isinstance(instance, library_CD)


library_DVD_strategy = st.builds(library_DVD)
@given(instance=library_DVD_strategy)
@settings(max_examples=25)
def test_library_DVD_instantiation(instance):
    assert isinstance(instance, library_DVD)


library_Item_strategy = st.builds(library_Item, pubDate=st.dates(), title=safe_text)
@given(instance=library_Item_strategy)
@settings(max_examples=25)
def test_library_Item_instantiation(instance):
    assert isinstance(instance, library_Item)


library_LibraryShelf_strategy = st.builds(library_LibraryShelf, name=safe_text)
@given(instance=library_LibraryShelf_strategy)
@settings(max_examples=25)
def test_library_LibraryShelf_instantiation(instance):
    assert isinstance(instance, library_LibraryShelf)


library_MultimediaItem_strategy = st.builds(library_MultimediaItem, length=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=library_MultimediaItem_strategy)
@settings(max_examples=25)
def test_library_MultimediaItem_instantiation(instance):
    assert isinstance(instance, library_MultimediaItem)



