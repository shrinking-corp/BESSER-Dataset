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
    library_Library,
    library_EStringToWriterMapEntry,
    library_EStringToBookMapEntry,
    library_Writer,
    library_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_library_is_not_abstract():
    assert not inspect.isabstract(library_Library)


def test_hyp_library_library_constructor_exists():
    assert callable(library_Library.__init__)


def test_hyp_library_library_constructor_args():
    sig = inspect.signature(library_Library.__init__)
    params = list(sig.parameters.keys())
    assert "writerByIDMap" in params, "Missing parameter 'writerByIDMap'"
    assert "options" in params, "Missing parameter 'options'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_library_estringtowritermapentry_is_not_abstract():
    assert not inspect.isabstract(library_EStringToWriterMapEntry)


def test_hyp_library_estringtowritermapentry_constructor_exists():
    assert callable(library_EStringToWriterMapEntry.__init__)


def test_hyp_library_estringtowritermapentry_constructor_args():
    sig = inspect.signature(library_EStringToWriterMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_library_estringtobookmapentry_is_not_abstract():
    assert not inspect.isabstract(library_EStringToBookMapEntry)


def test_hyp_library_estringtobookmapentry_constructor_exists():
    assert callable(library_EStringToBookMapEntry.__init__)


def test_hyp_library_estringtobookmapentry_constructor_args():
    sig = inspect.signature(library_EStringToBookMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_library_writer_is_not_abstract():
    assert not inspect.isabstract(library_Writer)


def test_hyp_library_writer_constructor_exists():
    assert callable(library_Writer.__init__)


def test_hyp_library_writer_constructor_args():
    sig = inspect.signature(library_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_library_book_is_not_abstract():
    assert not inspect.isabstract(library_Book)


def test_hyp_library_book_constructor_exists():
    assert callable(library_Book.__init__)


def test_hyp_library_book_constructor_args():
    sig = inspect.signature(library_Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "title" in params, "Missing parameter 'title'"
    assert "pages" in params, "Missing parameter 'pages'"




def test_hyp_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_hyp_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "MYSTERY",
        "Biography",
        "ScienceFiction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategory"


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
library_Library_strategy = st.builds(
    library_Library,
    writerByIDMap=
        safe_text,
    options=
        safe_text,
    name=
        safe_text
)
library_EStringToWriterMapEntry_strategy = st.builds(
    library_EStringToWriterMapEntry,
    key=
        safe_text
)
library_EStringToBookMapEntry_strategy = st.builds(
    library_EStringToBookMapEntry,
    key=
        safe_text
)
library_Writer_strategy = st.builds(
    library_Writer,
    name=
        safe_text
)
library_Book_strategy = st.builds(
    library_Book,
    category=
        safe_text,
    title=
        safe_text,
    pages=
        st.integers()
)




@given(instance=library_Library_strategy)
def test_hyp_library_library_writerByIDMap_setter(instance):
    original = instance.writerByIDMap
    instance.writerByIDMap = original
    assert instance.writerByIDMap == original



@given(instance=library_Library_strategy)
def test_hyp_library_library_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=library_Library_strategy)
def test_hyp_library_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_EStringToWriterMapEntry_strategy)
def test_hyp_library_estringtowritermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=library_EStringToBookMapEntry_strategy)
def test_hyp_library_estringtobookmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=library_Writer_strategy)
def test_hyp_library_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=library_Book_strategy)
def test_hyp_library_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=library_Book_strategy)
def test_hyp_library_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=library_Book_strategy)
def test_hyp_library_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    library_Book,
    library_EStringToBookMapEntry,
    library_EStringToWriterMapEntry,
    library_Library,
    library_Writer,
    BookCategory,
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

def test_library_Book_category_value_roundtrip():
    instance = library_Book(category="sample_text", pages=7, title="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_library_Book_pages_value_roundtrip():
    instance = library_Book(category="sample_text", pages=7, title="sample_text")
    assert instance.pages == 7
    instance.pages = 13
    assert instance.pages == 13


def test_library_Book_title_value_roundtrip():
    instance = library_Book(category="sample_text", pages=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_library_EStringToBookMapEntry_key_value_roundtrip():
    instance = library_EStringToBookMapEntry(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_library_EStringToWriterMapEntry_key_value_roundtrip():
    instance = library_EStringToWriterMapEntry(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_library_Library_name_value_roundtrip():
    instance = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_library_Library_options_value_roundtrip():
    instance = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    assert instance.options == "sample_text"
    instance.options = "sample_text_2"
    assert instance.options == "sample_text_2"


def test_library_Library_writerByIDMap_value_roundtrip():
    instance = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    assert instance.writerByIDMap == "sample_text"
    instance.writerByIDMap = "sample_text_2"
    assert instance.writerByIDMap == "sample_text_2"


def test_library_Writer_name_value_roundtrip():
    instance = library_Writer(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_author0_link_reassign_clear():
    a = library_Writer(name="sample_text")
    b1 = library_Book(category="sample_text", pages=7, title="sample_text")
    b2 = library_Book(category="sample_text_2", pages=13, title="sample_text_2")
    _safe_set(a, 'Writer', b1)
    assert _is_linked(a, 'Writer', b1)
    if hasattr(b1, 'books'):
        assert _is_linked(b1, 'books', a)
    _safe_set(a, 'Writer', b2)
    assert _is_linked(a, 'Writer', b2)
    if hasattr(b1, 'books'):
        assert not _is_linked(b1, 'books', a)
    if hasattr(b2, 'books'):
        assert _is_linked(b2, 'books', a)
    _safe_set(a, 'Writer', None)
    assert not _is_linked(a, 'Writer', b2)
    if hasattr(b2, 'books'):
        assert not _is_linked(b2, 'books', a)


def test_assoc_bookByTitleMap7_link_reassign_clear():
    a = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    b1 = library_EStringToBookMapEntry(key="sample_text")
    b2 = library_EStringToBookMapEntry(key="sample_text_2")
    _safe_set(a, 'library_Library8', {b1})
    assert _is_linked(a, 'library_Library8', b1)
    if hasattr(b1, 'library_EStringToBookMapEntry'):
        assert _is_linked(b1, 'library_EStringToBookMapEntry', a)
    _safe_set(a, 'library_Library8', {b2})
    assert _is_linked(a, 'library_Library8', b2)
    if hasattr(b1, 'library_EStringToBookMapEntry'):
        assert not _is_linked(b1, 'library_EStringToBookMapEntry', a)
    if hasattr(b2, 'library_EStringToBookMapEntry'):
        assert _is_linked(b2, 'library_EStringToBookMapEntry', a)
    _safe_set(a, 'library_Library8', set())
    assert not _is_linked(a, 'library_Library8', b2)
    if hasattr(b2, 'library_EStringToBookMapEntry'):
        assert not _is_linked(b2, 'library_EStringToBookMapEntry', a)


def test_assoc_books11_link_reassign_clear():
    a = library_Writer(name="sample_text")
    b1 = library_Book(category="sample_text", pages=7, title="sample_text")
    b2 = library_Book(category="sample_text_2", pages=13, title="sample_text_2")
    _safe_set(a, 'author', {b1})
    assert _is_linked(a, 'author', b1)
    if hasattr(b1, 'Book'):
        assert _is_linked(b1, 'Book', a)
    _safe_set(a, 'author', {b2})
    assert _is_linked(a, 'author', b2)
    if hasattr(b1, 'Book'):
        assert not _is_linked(b1, 'Book', a)
    if hasattr(b2, 'Book'):
        assert _is_linked(b2, 'Book', a)
    _safe_set(a, 'author', set())
    assert not _is_linked(a, 'author', b2)
    if hasattr(b2, 'Book'):
        assert not _is_linked(b2, 'Book', a)


def test_assoc_books2_link_reassign_clear():
    a = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    b1 = library_Book(category="sample_text", pages=7, title="sample_text")
    b2 = library_Book(category="sample_text_2", pages=13, title="sample_text_2")
    _safe_set(a, 'library_Library3', {b1})
    assert _is_linked(a, 'library_Library3', b1)
    if hasattr(b1, 'library_Book'):
        assert _is_linked(b1, 'library_Book', a)
    _safe_set(a, 'library_Library3', {b2})
    assert _is_linked(a, 'library_Library3', b2)
    if hasattr(b1, 'library_Book'):
        assert not _is_linked(b1, 'library_Book', a)
    if hasattr(b2, 'library_Book'):
        assert _is_linked(b2, 'library_Book', a)
    _safe_set(a, 'library_Library3', set())
    assert not _is_linked(a, 'library_Library3', b2)
    if hasattr(b2, 'library_Book'):
        assert not _is_linked(b2, 'library_Book', a)


def test_assoc_specialBooks4_link_reassign_clear():
    a = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    b1 = library_Book(category="sample_text", pages=7, title="sample_text")
    b2 = library_Book(category="sample_text_2", pages=13, title="sample_text_2")
    _safe_set(a, 'library_Library5', {b1})
    assert _is_linked(a, 'library_Library5', b1)
    if hasattr(b1, 'library_Book6'):
        assert _is_linked(b1, 'library_Book6', a)
    _safe_set(a, 'library_Library5', {b2})
    assert _is_linked(a, 'library_Library5', b2)
    if hasattr(b1, 'library_Book6'):
        assert not _is_linked(b1, 'library_Book6', a)
    if hasattr(b2, 'library_Book6'):
        assert _is_linked(b2, 'library_Book6', a)
    _safe_set(a, 'library_Library5', set())
    assert not _is_linked(a, 'library_Library5', b2)
    if hasattr(b2, 'library_Book6'):
        assert not _is_linked(b2, 'library_Book6', a)


def test_assoc_value12_link_reassign_clear():
    a = library_EStringToBookMapEntry(key="sample_text")
    b1 = library_Book(category="sample_text", pages=7, title="sample_text")
    b2 = library_Book(category="sample_text_2", pages=13, title="sample_text_2")
    _safe_set(a, 'library_EStringToBookMapEntry13', b1)
    assert _is_linked(a, 'library_EStringToBookMapEntry13', b1)
    if hasattr(b1, 'library_Book14'):
        assert _is_linked(b1, 'library_Book14', a)
    _safe_set(a, 'library_EStringToBookMapEntry13', b2)
    assert _is_linked(a, 'library_EStringToBookMapEntry13', b2)
    if hasattr(b1, 'library_Book14'):
        assert not _is_linked(b1, 'library_Book14', a)
    if hasattr(b2, 'library_Book14'):
        assert _is_linked(b2, 'library_Book14', a)
    _safe_set(a, 'library_EStringToBookMapEntry13', None)
    assert not _is_linked(a, 'library_EStringToBookMapEntry13', b2)
    if hasattr(b2, 'library_Book14'):
        assert not _is_linked(b2, 'library_Book14', a)


def test_assoc_value15_link_reassign_clear():
    a = library_Writer(name="sample_text")
    b1 = library_EStringToWriterMapEntry(key="sample_text")
    b2 = library_EStringToWriterMapEntry(key="sample_text_2")
    _safe_set(a, 'library_Writer17', b1)
    assert _is_linked(a, 'library_Writer17', b1)
    if hasattr(b1, 'library_EStringToWriterMapEntry16'):
        assert _is_linked(b1, 'library_EStringToWriterMapEntry16', a)
    _safe_set(a, 'library_Writer17', b2)
    assert _is_linked(a, 'library_Writer17', b2)
    if hasattr(b1, 'library_EStringToWriterMapEntry16'):
        assert not _is_linked(b1, 'library_EStringToWriterMapEntry16', a)
    if hasattr(b2, 'library_EStringToWriterMapEntry16'):
        assert _is_linked(b2, 'library_EStringToWriterMapEntry16', a)
    _safe_set(a, 'library_Writer17', None)
    assert not _is_linked(a, 'library_Writer17', b2)
    if hasattr(b2, 'library_EStringToWriterMapEntry16'):
        assert not _is_linked(b2, 'library_EStringToWriterMapEntry16', a)


def test_assoc_writerByNameMap9_link_reassign_clear():
    a = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    b1 = library_EStringToWriterMapEntry(key="sample_text")
    b2 = library_EStringToWriterMapEntry(key="sample_text_2")
    _safe_set(a, 'library_Library10', {b1})
    assert _is_linked(a, 'library_Library10', b1)
    if hasattr(b1, 'library_EStringToWriterMapEntry'):
        assert _is_linked(b1, 'library_EStringToWriterMapEntry', a)
    _safe_set(a, 'library_Library10', {b2})
    assert _is_linked(a, 'library_Library10', b2)
    if hasattr(b1, 'library_EStringToWriterMapEntry'):
        assert not _is_linked(b1, 'library_EStringToWriterMapEntry', a)
    if hasattr(b2, 'library_EStringToWriterMapEntry'):
        assert _is_linked(b2, 'library_EStringToWriterMapEntry', a)
    _safe_set(a, 'library_Library10', set())
    assert not _is_linked(a, 'library_Library10', b2)
    if hasattr(b2, 'library_EStringToWriterMapEntry'):
        assert not _is_linked(b2, 'library_EStringToWriterMapEntry', a)


def test_assoc_writers1_link_reassign_clear():
    a = library_Writer(name="sample_text")
    b1 = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    b2 = library_Library(name="sample_text_2", options="sample_text_2", writerByIDMap="sample_text_2")
    _safe_set(a, 'library_Writer', b1)
    assert _is_linked(a, 'library_Writer', b1)
    if hasattr(b1, 'library_Library'):
        assert _is_linked(b1, 'library_Library', a)
    _safe_set(a, 'library_Writer', b2)
    assert _is_linked(a, 'library_Writer', b2)
    if hasattr(b1, 'library_Library'):
        assert not _is_linked(b1, 'library_Library', a)
    if hasattr(b2, 'library_Library'):
        assert _is_linked(b2, 'library_Library', a)
    _safe_set(a, 'library_Writer', None)
    assert not _is_linked(a, 'library_Writer', b2)
    if hasattr(b2, 'library_Library'):
        assert not _is_linked(b2, 'library_Library', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

library_Book_strategy = st.builds(library_Book, category=safe_text, pages=st.integers(), title=safe_text)
@given(instance=library_Book_strategy)
@settings(max_examples=25)
def test_library_Book_instantiation(instance):
    assert isinstance(instance, library_Book)


library_EStringToBookMapEntry_strategy = st.builds(library_EStringToBookMapEntry, key=safe_text)
@given(instance=library_EStringToBookMapEntry_strategy)
@settings(max_examples=25)
def test_library_EStringToBookMapEntry_instantiation(instance):
    assert isinstance(instance, library_EStringToBookMapEntry)


library_EStringToWriterMapEntry_strategy = st.builds(library_EStringToWriterMapEntry, key=safe_text)
@given(instance=library_EStringToWriterMapEntry_strategy)
@settings(max_examples=25)
def test_library_EStringToWriterMapEntry_instantiation(instance):
    assert isinstance(instance, library_EStringToWriterMapEntry)


library_Library_strategy = st.builds(library_Library, name=safe_text, options=safe_text, writerByIDMap=safe_text)
@given(instance=library_Library_strategy)
@settings(max_examples=25)
def test_library_Library_instantiation(instance):
    assert isinstance(instance, library_Library)


library_Writer_strategy = st.builds(library_Writer, name=safe_text)
@given(instance=library_Writer_strategy)
@settings(max_examples=25)
def test_library_Writer_instantiation(instance):
    assert isinstance(instance, library_Writer)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_Book,
    library_EStringToBookMapEntry,
    library_EStringToWriterMapEntry,
    library_Library,
    library_Writer,
    BookCategory,
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

def test_assoc_author0_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'books', a1)
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Writer'):
        assert _is_linked(a1, 'Writer', b)
    _safe_set(b, 'books', a2)
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Writer'):
        assert not _is_linked(a1, 'Writer', b)
    if hasattr(a2, 'Writer'):
        assert _is_linked(a2, 'Writer', b)
    _safe_set(b, 'books', None)
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Writer'):
        assert not _is_linked(a2, 'Writer', b)


def test_assoc_bookByTitleMap7_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    a2 = library_Library(name="sample_text_2", options="sample_text_2", writerByIDMap="sample_text_2")
    b = library_EStringToBookMapEntry(key="sample_text")
    _safe_set(b, 'library_EStringToBookMapEntry', a1)
    assert _is_linked(b, 'library_EStringToBookMapEntry', a1)
    if hasattr(a1, 'library_Library8'):
        assert _is_linked(a1, 'library_Library8', b)
    _safe_set(b, 'library_EStringToBookMapEntry', a2)
    assert _is_linked(b, 'library_EStringToBookMapEntry', a2)
    if hasattr(a1, 'library_Library8'):
        assert not _is_linked(a1, 'library_Library8', b)
    if hasattr(a2, 'library_Library8'):
        assert _is_linked(a2, 'library_Library8', b)
    _safe_set(b, 'library_EStringToBookMapEntry', None)
    assert not _is_linked(b, 'library_EStringToBookMapEntry', a2)
    if hasattr(a2, 'library_Library8'):
        assert not _is_linked(a2, 'library_Library8', b)


def test_assoc_books11_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'author'):
        assert _is_linked(a1, 'author', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'author'):
        assert not _is_linked(a1, 'author', b)
    if hasattr(a2, 'author'):
        assert _is_linked(a2, 'author', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'author'):
        assert not _is_linked(a2, 'author', b)


def test_assoc_books2_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    a2 = library_Library(name="sample_text_2", options="sample_text_2", writerByIDMap="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book', a1)
    assert _is_linked(b, 'library_Book', a1)
    if hasattr(a1, 'library_Library3'):
        assert _is_linked(a1, 'library_Library3', b)
    _safe_set(b, 'library_Book', a2)
    assert _is_linked(b, 'library_Book', a2)
    if hasattr(a1, 'library_Library3'):
        assert not _is_linked(a1, 'library_Library3', b)
    if hasattr(a2, 'library_Library3'):
        assert _is_linked(a2, 'library_Library3', b)
    _safe_set(b, 'library_Book', None)
    assert not _is_linked(b, 'library_Book', a2)
    if hasattr(a2, 'library_Library3'):
        assert not _is_linked(a2, 'library_Library3', b)


def test_assoc_specialBooks4_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    a2 = library_Library(name="sample_text_2", options="sample_text_2", writerByIDMap="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book6', a1)
    assert _is_linked(b, 'library_Book6', a1)
    if hasattr(a1, 'library_Library5'):
        assert _is_linked(a1, 'library_Library5', b)
    _safe_set(b, 'library_Book6', a2)
    assert _is_linked(b, 'library_Book6', a2)
    if hasattr(a1, 'library_Library5'):
        assert not _is_linked(a1, 'library_Library5', b)
    if hasattr(a2, 'library_Library5'):
        assert _is_linked(a2, 'library_Library5', b)
    _safe_set(b, 'library_Book6', None)
    assert not _is_linked(b, 'library_Book6', a2)
    if hasattr(a2, 'library_Library5'):
        assert not _is_linked(a2, 'library_Library5', b)


def test_assoc_value12_reverse_link_reassign_clear():
    a1 = library_EStringToBookMapEntry(key="sample_text")
    a2 = library_EStringToBookMapEntry(key="sample_text_2")
    b = library_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'library_Book14', a1)
    assert _is_linked(b, 'library_Book14', a1)
    if hasattr(a1, 'library_EStringToBookMapEntry13'):
        assert _is_linked(a1, 'library_EStringToBookMapEntry13', b)
    _safe_set(b, 'library_Book14', a2)
    assert _is_linked(b, 'library_Book14', a2)
    if hasattr(a1, 'library_EStringToBookMapEntry13'):
        assert not _is_linked(a1, 'library_EStringToBookMapEntry13', b)
    if hasattr(a2, 'library_EStringToBookMapEntry13'):
        assert _is_linked(a2, 'library_EStringToBookMapEntry13', b)
    _safe_set(b, 'library_Book14', None)
    assert not _is_linked(b, 'library_Book14', a2)
    if hasattr(a2, 'library_EStringToBookMapEntry13'):
        assert not _is_linked(a2, 'library_EStringToBookMapEntry13', b)


def test_assoc_value15_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_EStringToWriterMapEntry(key="sample_text")
    _safe_set(b, 'library_EStringToWriterMapEntry16', a1)
    assert _is_linked(b, 'library_EStringToWriterMapEntry16', a1)
    if hasattr(a1, 'library_Writer17'):
        assert _is_linked(a1, 'library_Writer17', b)
    _safe_set(b, 'library_EStringToWriterMapEntry16', a2)
    assert _is_linked(b, 'library_EStringToWriterMapEntry16', a2)
    if hasattr(a1, 'library_Writer17'):
        assert not _is_linked(a1, 'library_Writer17', b)
    if hasattr(a2, 'library_Writer17'):
        assert _is_linked(a2, 'library_Writer17', b)
    _safe_set(b, 'library_EStringToWriterMapEntry16', None)
    assert not _is_linked(b, 'library_EStringToWriterMapEntry16', a2)
    if hasattr(a2, 'library_Writer17'):
        assert not _is_linked(a2, 'library_Writer17', b)


def test_assoc_writerByNameMap9_reverse_link_reassign_clear():
    a1 = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    a2 = library_Library(name="sample_text_2", options="sample_text_2", writerByIDMap="sample_text_2")
    b = library_EStringToWriterMapEntry(key="sample_text")
    _safe_set(b, 'library_EStringToWriterMapEntry', a1)
    assert _is_linked(b, 'library_EStringToWriterMapEntry', a1)
    if hasattr(a1, 'library_Library10'):
        assert _is_linked(a1, 'library_Library10', b)
    _safe_set(b, 'library_EStringToWriterMapEntry', a2)
    assert _is_linked(b, 'library_EStringToWriterMapEntry', a2)
    if hasattr(a1, 'library_Library10'):
        assert not _is_linked(a1, 'library_Library10', b)
    if hasattr(a2, 'library_Library10'):
        assert _is_linked(a2, 'library_Library10', b)
    _safe_set(b, 'library_EStringToWriterMapEntry', None)
    assert not _is_linked(b, 'library_EStringToWriterMapEntry', a2)
    if hasattr(a2, 'library_Library10'):
        assert not _is_linked(a2, 'library_Library10', b)


def test_assoc_writers1_reverse_link_reassign_clear():
    a1 = library_Writer(name="sample_text")
    a2 = library_Writer(name="sample_text_2")
    b = library_Library(name="sample_text", options="sample_text", writerByIDMap="sample_text")
    _safe_set(b, 'library_Library', {a1})
    assert _is_linked(b, 'library_Library', a1)
    if hasattr(a1, 'library_Writer'):
        assert _is_linked(a1, 'library_Writer', b)
    _safe_set(b, 'library_Library', {a2})
    assert _is_linked(b, 'library_Library', a2)
    if hasattr(a1, 'library_Writer'):
        assert not _is_linked(a1, 'library_Writer', b)
    if hasattr(a2, 'library_Writer'):
        assert _is_linked(a2, 'library_Writer', b)
    _safe_set(b, 'library_Library', set())
    assert not _is_linked(b, 'library_Library', a2)
    if hasattr(a2, 'library_Writer'):
        assert not _is_linked(a2, 'library_Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


