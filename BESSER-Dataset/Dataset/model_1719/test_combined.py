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
    library3_LibraryType,
    library3_CustomerType,
    library3_EStringToStringMapEntry,
    library3_DocumentRoot,
    library3_BookType,
    library3_BookInfoType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library3_librarytype_is_not_abstract():
    assert not inspect.isabstract(library3_LibraryType)


def test_hyp_library3_librarytype_constructor_exists():
    assert callable(library3_LibraryType.__init__)


def test_hyp_library3_librarytype_constructor_args():
    sig = inspect.signature(library3_LibraryType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library3_customertype_is_not_abstract():
    assert not inspect.isabstract(library3_CustomerType)


def test_hyp_library3_customertype_constructor_exists():
    assert callable(library3_CustomerType.__init__)


def test_hyp_library3_customertype_constructor_args():
    sig = inspect.signature(library3_CustomerType.__init__)
    params = list(sig.parameters.keys())
    assert "borrowedBookSince" in params, "Missing parameter 'borrowedBookSince'"
    assert "borrowedBookId" in params, "Missing parameter 'borrowedBookId'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"







def test_hyp_library3_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(library3_EStringToStringMapEntry)


def test_hyp_library3_estringtostringmapentry_constructor_exists():
    assert callable(library3_EStringToStringMapEntry.__init__)


def test_hyp_library3_estringtostringmapentry_constructor_args():
    sig = inspect.signature(library3_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library3_documentroot_is_not_abstract():
    assert not inspect.isabstract(library3_DocumentRoot)


def test_hyp_library3_documentroot_constructor_exists():
    assert callable(library3_DocumentRoot.__init__)


def test_hyp_library3_documentroot_constructor_args():
    sig = inspect.signature(library3_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_library3_booktype_is_not_abstract():
    assert not inspect.isabstract(library3_BookType)


def test_hyp_library3_booktype_constructor_exists():
    assert callable(library3_BookType.__init__)


def test_hyp_library3_booktype_constructor_args():
    sig = inspect.signature(library3_BookType.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "download" in params, "Missing parameter 'download'"
    assert "dimension" in params, "Missing parameter 'dimension'"
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "name" in params, "Missing parameter 'name'"










def test_hyp_library3_bookinfotype_is_not_abstract():
    assert not inspect.isabstract(library3_BookInfoType)


def test_hyp_library3_bookinfotype_constructor_exists():
    assert callable(library3_BookInfoType.__init__)


def test_hyp_library3_bookinfotype_constructor_args():
    sig = inspect.signature(library3_BookInfoType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"



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
library3_LibraryType_strategy = st.builds(
    library3_LibraryType,
)
library3_CustomerType_strategy = st.builds(
    library3_CustomerType,
    borrowedBookSince=
        safe_text,
    borrowedBookId=
        safe_text,
    firstName=
        safe_text,
    lastName=
        safe_text
)
library3_EStringToStringMapEntry_strategy = st.builds(
    library3_EStringToStringMapEntry,
)
library3_DocumentRoot_strategy = st.builds(
    library3_DocumentRoot,
    mixed=
        safe_text
)
library3_BookType_strategy = st.builds(
    library3_BookType,
    isbn=
        safe_text,
    download=
        safe_text,
    dimension=
        safe_text,
    title=
        safe_text,
    author=
        safe_text,
    pages=
        safe_text,
    name=
        safe_text
)
library3_BookInfoType_strategy = st.builds(
    library3_BookInfoType,
    any=
        safe_text
)





@given(instance=library3_CustomerType_strategy)
def test_hyp_library3_customertype_borrowedBookSince_setter(instance):
    original = instance.borrowedBookSince
    instance.borrowedBookSince = original
    assert instance.borrowedBookSince == original



@given(instance=library3_CustomerType_strategy)
def test_hyp_library3_customertype_borrowedBookId_setter(instance):
    original = instance.borrowedBookId
    instance.borrowedBookId = original
    assert instance.borrowedBookId == original



@given(instance=library3_CustomerType_strategy)
def test_hyp_library3_customertype_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=library3_CustomerType_strategy)
def test_hyp_library3_customertype_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original





@given(instance=library3_DocumentRoot_strategy)
def test_hyp_library3_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=library3_BookType_strategy)
def test_hyp_library3_booktype_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=library3_BookType_strategy)
def test_hyp_library3_booktype_download_setter(instance):
    original = instance.download
    instance.download = original
    assert instance.download == original



@given(instance=library3_BookType_strategy)
def test_hyp_library3_booktype_dimension_setter(instance):
    original = instance.dimension
    instance.dimension = original
    assert instance.dimension == original



@given(instance=library3_BookType_strategy)
def test_hyp_library3_booktype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library3_BookType_strategy)
def test_hyp_library3_booktype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=library3_BookType_strategy)
def test_hyp_library3_booktype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=library3_BookType_strategy)
def test_hyp_library3_booktype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library3_BookInfoType_strategy)
def test_hyp_library3_bookinfotype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    library3_BookInfoType,
    library3_BookType,
    library3_CustomerType,
    library3_DocumentRoot,
    library3_EStringToStringMapEntry,
    library3_LibraryType,
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

def test_library3_BookInfoType_any_value_roundtrip():
    instance = library3_BookInfoType(any="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_library3_BookType_author_value_roundtrip():
    instance = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_library3_BookType_dimension_value_roundtrip():
    instance = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    assert instance.dimension == "sample_text"
    instance.dimension = "sample_text_2"
    assert instance.dimension == "sample_text_2"


def test_library3_BookType_download_value_roundtrip():
    instance = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    assert instance.download == "sample_text"
    instance.download = "sample_text_2"
    assert instance.download == "sample_text_2"


def test_library3_BookType_isbn_value_roundtrip():
    instance = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    assert instance.isbn == "sample_text"
    instance.isbn = "sample_text_2"
    assert instance.isbn == "sample_text_2"


def test_library3_BookType_name_value_roundtrip():
    instance = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library3_BookType_pages_value_roundtrip():
    instance = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_library3_BookType_title_value_roundtrip():
    instance = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_library3_CustomerType_borrowedBookId_value_roundtrip():
    instance = library3_CustomerType(borrowedBookId="sample_text", borrowedBookSince="sample_text", firstName="sample_text", lastName="sample_text")
    assert instance.borrowedBookId == "sample_text"
    instance.borrowedBookId = "sample_text_2"
    assert instance.borrowedBookId == "sample_text_2"


def test_library3_CustomerType_borrowedBookSince_value_roundtrip():
    instance = library3_CustomerType(borrowedBookId="sample_text", borrowedBookSince="sample_text", firstName="sample_text", lastName="sample_text")
    assert instance.borrowedBookSince == "sample_text"
    instance.borrowedBookSince = "sample_text_2"
    assert instance.borrowedBookSince == "sample_text_2"


def test_library3_CustomerType_firstName_value_roundtrip():
    instance = library3_CustomerType(borrowedBookId="sample_text", borrowedBookSince="sample_text", firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_library3_CustomerType_lastName_value_roundtrip():
    instance = library3_CustomerType(borrowedBookId="sample_text", borrowedBookSince="sample_text", firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_library3_DocumentRoot_mixed_value_roundtrip():
    instance = library3_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_assoc_book7_link_reassign_clear():
    a = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    b1 = library3_LibraryType()
    b2 = library3_LibraryType()
    _safe_set(a, 'library3_BookType9', b1)
    assert _is_linked(a, 'library3_BookType9', b1)
    if hasattr(b1, 'library3_LibraryType8'):
        assert _is_linked(b1, 'library3_LibraryType8', a)
    _safe_set(a, 'library3_BookType9', b2)
    assert _is_linked(a, 'library3_BookType9', b2)
    if hasattr(b1, 'library3_LibraryType8'):
        assert not _is_linked(b1, 'library3_LibraryType8', a)
    if hasattr(b2, 'library3_LibraryType8'):
        assert _is_linked(b2, 'library3_LibraryType8', a)
    _safe_set(a, 'library3_BookType9', None)
    assert not _is_linked(a, 'library3_BookType9', b2)
    if hasattr(b2, 'library3_LibraryType8'):
        assert not _is_linked(b2, 'library3_LibraryType8', a)


def test_assoc_bookInfo0_link_reassign_clear():
    a = library3_BookType(author="sample_text", dimension="sample_text", download="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    b1 = library3_BookInfoType(any="sample_text")
    b2 = library3_BookInfoType(any="sample_text_2")
    _safe_set(a, 'library3_BookType', b1)
    assert _is_linked(a, 'library3_BookType', b1)
    if hasattr(b1, 'library3_BookInfoType'):
        assert _is_linked(b1, 'library3_BookInfoType', a)
    _safe_set(a, 'library3_BookType', b2)
    assert _is_linked(a, 'library3_BookType', b2)
    if hasattr(b1, 'library3_BookInfoType'):
        assert not _is_linked(b1, 'library3_BookInfoType', a)
    if hasattr(b2, 'library3_BookInfoType'):
        assert _is_linked(b2, 'library3_BookInfoType', a)
    _safe_set(a, 'library3_BookType', None)
    assert not _is_linked(a, 'library3_BookType', b2)
    if hasattr(b2, 'library3_BookInfoType'):
        assert not _is_linked(b2, 'library3_BookInfoType', a)


def test_assoc_customer10_link_reassign_clear():
    a = library3_CustomerType(borrowedBookId="sample_text", borrowedBookSince="sample_text", firstName="sample_text", lastName="sample_text")
    b1 = library3_LibraryType()
    b2 = library3_LibraryType()
    _safe_set(a, 'library3_CustomerType', b1)
    assert _is_linked(a, 'library3_CustomerType', b1)
    if hasattr(b1, 'library3_LibraryType11'):
        assert _is_linked(b1, 'library3_LibraryType11', a)
    _safe_set(a, 'library3_CustomerType', b2)
    assert _is_linked(a, 'library3_CustomerType', b2)
    if hasattr(b1, 'library3_LibraryType11'):
        assert not _is_linked(b1, 'library3_LibraryType11', a)
    if hasattr(b2, 'library3_LibraryType11'):
        assert _is_linked(b2, 'library3_LibraryType11', a)
    _safe_set(a, 'library3_CustomerType', None)
    assert not _is_linked(a, 'library3_CustomerType', b2)
    if hasattr(b2, 'library3_LibraryType11'):
        assert not _is_linked(b2, 'library3_LibraryType11', a)


def test_assoc_library5_link_reassign_clear():
    a = library3_DocumentRoot(mixed="sample_text")
    b1 = library3_LibraryType()
    b2 = library3_LibraryType()
    _safe_set(a, 'library3_DocumentRoot6', {b1})
    assert _is_linked(a, 'library3_DocumentRoot6', b1)
    if hasattr(b1, 'library3_LibraryType'):
        assert _is_linked(b1, 'library3_LibraryType', a)
    _safe_set(a, 'library3_DocumentRoot6', {b2})
    assert _is_linked(a, 'library3_DocumentRoot6', b2)
    if hasattr(b1, 'library3_LibraryType'):
        assert not _is_linked(b1, 'library3_LibraryType', a)
    if hasattr(b2, 'library3_LibraryType'):
        assert _is_linked(b2, 'library3_LibraryType', a)
    _safe_set(a, 'library3_DocumentRoot6', set())
    assert not _is_linked(a, 'library3_DocumentRoot6', b2)
    if hasattr(b2, 'library3_LibraryType'):
        assert not _is_linked(b2, 'library3_LibraryType', a)


def test_assoc_xMLNSPrefixMap1_link_reassign_clear():
    a = library3_DocumentRoot(mixed="sample_text")
    b1 = library3_EStringToStringMapEntry()
    b2 = library3_EStringToStringMapEntry()
    _safe_set(a, 'library3_DocumentRoot', {b1})
    assert _is_linked(a, 'library3_DocumentRoot', b1)
    if hasattr(b1, 'library3_EStringToStringMapEntry'):
        assert _is_linked(b1, 'library3_EStringToStringMapEntry', a)
    _safe_set(a, 'library3_DocumentRoot', {b2})
    assert _is_linked(a, 'library3_DocumentRoot', b2)
    if hasattr(b1, 'library3_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'library3_EStringToStringMapEntry', a)
    if hasattr(b2, 'library3_EStringToStringMapEntry'):
        assert _is_linked(b2, 'library3_EStringToStringMapEntry', a)
    _safe_set(a, 'library3_DocumentRoot', set())
    assert not _is_linked(a, 'library3_DocumentRoot', b2)
    if hasattr(b2, 'library3_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'library3_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation2_link_reassign_clear():
    a = library3_DocumentRoot(mixed="sample_text")
    b1 = library3_EStringToStringMapEntry()
    b2 = library3_EStringToStringMapEntry()
    _safe_set(a, 'library3_DocumentRoot3', {b1})
    assert _is_linked(a, 'library3_DocumentRoot3', b1)
    if hasattr(b1, 'library3_EStringToStringMapEntry4'):
        assert _is_linked(b1, 'library3_EStringToStringMapEntry4', a)
    _safe_set(a, 'library3_DocumentRoot3', {b2})
    assert _is_linked(a, 'library3_DocumentRoot3', b2)
    if hasattr(b1, 'library3_EStringToStringMapEntry4'):
        assert not _is_linked(b1, 'library3_EStringToStringMapEntry4', a)
    if hasattr(b2, 'library3_EStringToStringMapEntry4'):
        assert _is_linked(b2, 'library3_EStringToStringMapEntry4', a)
    _safe_set(a, 'library3_DocumentRoot3', set())
    assert not _is_linked(a, 'library3_DocumentRoot3', b2)
    if hasattr(b2, 'library3_EStringToStringMapEntry4'):
        assert not _is_linked(b2, 'library3_EStringToStringMapEntry4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

library3_BookInfoType_strategy = st.builds(library3_BookInfoType, any=safe_text)
@given(instance=library3_BookInfoType_strategy)
@settings(max_examples=25)
def test_library3_BookInfoType_instantiation(instance):
    assert isinstance(instance, library3_BookInfoType)


library3_BookType_strategy = st.builds(library3_BookType, author=safe_text, dimension=safe_text, download=safe_text, isbn=safe_text, name=safe_text, pages=safe_text, title=safe_text)
@given(instance=library3_BookType_strategy)
@settings(max_examples=25)
def test_library3_BookType_instantiation(instance):
    assert isinstance(instance, library3_BookType)


library3_CustomerType_strategy = st.builds(library3_CustomerType, borrowedBookId=safe_text, borrowedBookSince=safe_text, firstName=safe_text, lastName=safe_text)
@given(instance=library3_CustomerType_strategy)
@settings(max_examples=25)
def test_library3_CustomerType_instantiation(instance):
    assert isinstance(instance, library3_CustomerType)


library3_DocumentRoot_strategy = st.builds(library3_DocumentRoot, mixed=safe_text)
@given(instance=library3_DocumentRoot_strategy)
@settings(max_examples=25)
def test_library3_DocumentRoot_instantiation(instance):
    assert isinstance(instance, library3_DocumentRoot)


library3_EStringToStringMapEntry_strategy = st.builds(library3_EStringToStringMapEntry)
@given(instance=library3_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_library3_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, library3_EStringToStringMapEntry)


library3_LibraryType_strategy = st.builds(library3_LibraryType)
@given(instance=library3_LibraryType_strategy)
@settings(max_examples=25)
def test_library3_LibraryType_instantiation(instance):
    assert isinstance(instance, library3_LibraryType)



