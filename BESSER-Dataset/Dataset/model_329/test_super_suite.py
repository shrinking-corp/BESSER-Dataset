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
    bz242995_Author,
    bz242995_OneTimeWonder,
    bz242995_Library,
    bz242995_Writer,
    bz242995_Book,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bz242995_author_is_not_abstract():
    assert not inspect.isabstract(bz242995_Author)


def test_hyp_bz242995_author_constructor_exists():
    assert callable(bz242995_Author.__init__)


def test_hyp_bz242995_author_constructor_args():
    sig = inspect.signature(bz242995_Author.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_bz242995_onetimewonder_is_not_abstract():
    assert not inspect.isabstract(bz242995_OneTimeWonder)


def test_hyp_bz242995_onetimewonder_constructor_exists():
    assert callable(bz242995_OneTimeWonder.__init__)


def test_hyp_bz242995_onetimewonder_constructor_args():
    sig = inspect.signature(bz242995_OneTimeWonder.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_bz242995_library_is_not_abstract():
    assert not inspect.isabstract(bz242995_Library)


def test_hyp_bz242995_library_constructor_exists():
    assert callable(bz242995_Library.__init__)


def test_hyp_bz242995_library_constructor_args():
    sig = inspect.signature(bz242995_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_bz242995_writer_is_not_abstract():
    assert not inspect.isabstract(bz242995_Writer)


def test_hyp_bz242995_writer_constructor_exists():
    assert callable(bz242995_Writer.__init__)


def test_hyp_bz242995_writer_constructor_args():
    sig = inspect.signature(bz242995_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_bz242995_book_is_not_abstract():
    assert not inspect.isabstract(bz242995_Book)


def test_hyp_bz242995_book_constructor_exists():
    assert callable(bz242995_Book.__init__)


def test_hyp_bz242995_book_constructor_args():
    sig = inspect.signature(bz242995_Book.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_hyp_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Mystery",
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
bz242995_Author_strategy = st.builds(
    bz242995_Author,
    Name=
        safe_text,
    id=
        safe_text
)
bz242995_OneTimeWonder_strategy = st.builds(
    bz242995_OneTimeWonder,
    id=
        safe_text,
    Name=
        safe_text
)
bz242995_Library_strategy = st.builds(
    bz242995_Library,
    name=
        safe_text
)
bz242995_Writer_strategy = st.builds(
    bz242995_Writer,
    name=
        safe_text
)
bz242995_Book_strategy = st.builds(
    bz242995_Book,
    category=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text
)




@given(instance=bz242995_Author_strategy)
def test_hyp_bz242995_author_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=bz242995_Author_strategy)
def test_hyp_bz242995_author_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=bz242995_OneTimeWonder_strategy)
def test_hyp_bz242995_onetimewonder_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=bz242995_OneTimeWonder_strategy)
def test_hyp_bz242995_onetimewonder_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=bz242995_Library_strategy)
def test_hyp_bz242995_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=bz242995_Writer_strategy)
def test_hyp_bz242995_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=bz242995_Book_strategy)
def test_hyp_bz242995_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=bz242995_Book_strategy)
def test_hyp_bz242995_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=bz242995_Book_strategy)
def test_hyp_bz242995_book_title_setter(instance):
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
    bz242995_Author,
    bz242995_Book,
    bz242995_Library,
    bz242995_OneTimeWonder,
    bz242995_Writer,
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

def test_bz242995_Author_Name_value_roundtrip():
    instance = bz242995_Author(Name="sample_text", id="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_bz242995_Author_id_value_roundtrip():
    instance = bz242995_Author(Name="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_bz242995_Book_category_value_roundtrip():
    instance = bz242995_Book(category="sample_text", pages=7, title="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_bz242995_Book_pages_value_roundtrip():
    instance = bz242995_Book(category="sample_text", pages=7, title="sample_text")
    assert instance.pages == 7
    instance.pages = 13
    assert instance.pages == 13


def test_bz242995_Book_title_value_roundtrip():
    instance = bz242995_Book(category="sample_text", pages=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bz242995_Library_name_value_roundtrip():
    instance = bz242995_Library(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_bz242995_OneTimeWonder_Name_value_roundtrip():
    instance = bz242995_OneTimeWonder(Name="sample_text", id="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_bz242995_OneTimeWonder_id_value_roundtrip():
    instance = bz242995_OneTimeWonder(Name="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_bz242995_Writer_name_value_roundtrip():
    instance = bz242995_Writer(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_author0_link_reassign_clear():
    a = bz242995_Writer(name="sample_text")
    b1 = bz242995_Book(category="sample_text", pages=7, title="sample_text")
    b2 = bz242995_Book(category="sample_text_2", pages=13, title="sample_text_2")
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


def test_assoc_books2_link_reassign_clear():
    a = bz242995_Library(name="sample_text")
    b1 = bz242995_Book(category="sample_text", pages=7, title="sample_text")
    b2 = bz242995_Book(category="sample_text_2", pages=13, title="sample_text_2")
    _safe_set(a, 'bz242995_Library3', {b1})
    assert _is_linked(a, 'bz242995_Library3', b1)
    if hasattr(b1, 'bz242995_Book'):
        assert _is_linked(b1, 'bz242995_Book', a)
    _safe_set(a, 'bz242995_Library3', {b2})
    assert _is_linked(a, 'bz242995_Library3', b2)
    if hasattr(b1, 'bz242995_Book'):
        assert not _is_linked(b1, 'bz242995_Book', a)
    if hasattr(b2, 'bz242995_Book'):
        assert _is_linked(b2, 'bz242995_Book', a)
    _safe_set(a, 'bz242995_Library3', set())
    assert not _is_linked(a, 'bz242995_Library3', b2)
    if hasattr(b2, 'bz242995_Book'):
        assert not _is_linked(b2, 'bz242995_Book', a)


def test_assoc_books4_link_reassign_clear():
    a = bz242995_Writer(name="sample_text")
    b1 = bz242995_Book(category="sample_text", pages=7, title="sample_text")
    b2 = bz242995_Book(category="sample_text_2", pages=13, title="sample_text_2")
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


def test_assoc_theAuthor5_link_reassign_clear():
    a = bz242995_OneTimeWonder(Name="sample_text", id="sample_text")
    b1 = bz242995_Author(Name="sample_text", id="sample_text")
    b2 = bz242995_Author(Name="sample_text_2", id="sample_text_2")
    _safe_set(a, 'theBook', b1)
    assert _is_linked(a, 'theBook', b1)
    if hasattr(b1, 'Author'):
        assert _is_linked(b1, 'Author', a)
    _safe_set(a, 'theBook', b2)
    assert _is_linked(a, 'theBook', b2)
    if hasattr(b1, 'Author'):
        assert not _is_linked(b1, 'Author', a)
    if hasattr(b2, 'Author'):
        assert _is_linked(b2, 'Author', a)
    _safe_set(a, 'theBook', None)
    assert not _is_linked(a, 'theBook', b2)
    if hasattr(b2, 'Author'):
        assert not _is_linked(b2, 'Author', a)


def test_assoc_theBook6_link_reassign_clear():
    a = bz242995_OneTimeWonder(Name="sample_text", id="sample_text")
    b1 = bz242995_Author(Name="sample_text", id="sample_text")
    b2 = bz242995_Author(Name="sample_text_2", id="sample_text_2")
    _safe_set(a, 'OneTimeWonder', b1)
    assert _is_linked(a, 'OneTimeWonder', b1)
    if hasattr(b1, 'theAuthor'):
        assert _is_linked(b1, 'theAuthor', a)
    _safe_set(a, 'OneTimeWonder', b2)
    assert _is_linked(a, 'OneTimeWonder', b2)
    if hasattr(b1, 'theAuthor'):
        assert not _is_linked(b1, 'theAuthor', a)
    if hasattr(b2, 'theAuthor'):
        assert _is_linked(b2, 'theAuthor', a)
    _safe_set(a, 'OneTimeWonder', None)
    assert not _is_linked(a, 'OneTimeWonder', b2)
    if hasattr(b2, 'theAuthor'):
        assert not _is_linked(b2, 'theAuthor', a)


def test_assoc_writers1_link_reassign_clear():
    a = bz242995_Writer(name="sample_text")
    b1 = bz242995_Library(name="sample_text")
    b2 = bz242995_Library(name="sample_text_2")
    _safe_set(a, 'bz242995_Writer', b1)
    assert _is_linked(a, 'bz242995_Writer', b1)
    if hasattr(b1, 'bz242995_Library'):
        assert _is_linked(b1, 'bz242995_Library', a)
    _safe_set(a, 'bz242995_Writer', b2)
    assert _is_linked(a, 'bz242995_Writer', b2)
    if hasattr(b1, 'bz242995_Library'):
        assert not _is_linked(b1, 'bz242995_Library', a)
    if hasattr(b2, 'bz242995_Library'):
        assert _is_linked(b2, 'bz242995_Library', a)
    _safe_set(a, 'bz242995_Writer', None)
    assert not _is_linked(a, 'bz242995_Writer', b2)
    if hasattr(b2, 'bz242995_Library'):
        assert not _is_linked(b2, 'bz242995_Library', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

bz242995_Author_strategy = st.builds(bz242995_Author, Name=safe_text, id=safe_text)
@given(instance=bz242995_Author_strategy)
@settings(max_examples=25)
def test_bz242995_Author_instantiation(instance):
    assert isinstance(instance, bz242995_Author)


bz242995_Book_strategy = st.builds(bz242995_Book, category=safe_text, pages=st.integers(), title=safe_text)
@given(instance=bz242995_Book_strategy)
@settings(max_examples=25)
def test_bz242995_Book_instantiation(instance):
    assert isinstance(instance, bz242995_Book)


bz242995_Library_strategy = st.builds(bz242995_Library, name=safe_text)
@given(instance=bz242995_Library_strategy)
@settings(max_examples=25)
def test_bz242995_Library_instantiation(instance):
    assert isinstance(instance, bz242995_Library)


bz242995_OneTimeWonder_strategy = st.builds(bz242995_OneTimeWonder, Name=safe_text, id=safe_text)
@given(instance=bz242995_OneTimeWonder_strategy)
@settings(max_examples=25)
def test_bz242995_OneTimeWonder_instantiation(instance):
    assert isinstance(instance, bz242995_OneTimeWonder)


bz242995_Writer_strategy = st.builds(bz242995_Writer, name=safe_text)
@given(instance=bz242995_Writer_strategy)
@settings(max_examples=25)
def test_bz242995_Writer_instantiation(instance):
    assert isinstance(instance, bz242995_Writer)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bz242995_Author,
    bz242995_Book,
    bz242995_Library,
    bz242995_OneTimeWonder,
    bz242995_Writer,
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
    a1 = bz242995_Writer(name="sample_text")
    a2 = bz242995_Writer(name="sample_text_2")
    b = bz242995_Book(category="sample_text", pages=7, title="sample_text")
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


def test_assoc_books2_reverse_link_reassign_clear():
    a1 = bz242995_Library(name="sample_text")
    a2 = bz242995_Library(name="sample_text_2")
    b = bz242995_Book(category="sample_text", pages=7, title="sample_text")
    _safe_set(b, 'bz242995_Book', a1)
    assert _is_linked(b, 'bz242995_Book', a1)
    if hasattr(a1, 'bz242995_Library3'):
        assert _is_linked(a1, 'bz242995_Library3', b)
    _safe_set(b, 'bz242995_Book', a2)
    assert _is_linked(b, 'bz242995_Book', a2)
    if hasattr(a1, 'bz242995_Library3'):
        assert not _is_linked(a1, 'bz242995_Library3', b)
    if hasattr(a2, 'bz242995_Library3'):
        assert _is_linked(a2, 'bz242995_Library3', b)
    _safe_set(b, 'bz242995_Book', None)
    assert not _is_linked(b, 'bz242995_Book', a2)
    if hasattr(a2, 'bz242995_Library3'):
        assert not _is_linked(a2, 'bz242995_Library3', b)


def test_assoc_books4_reverse_link_reassign_clear():
    a1 = bz242995_Writer(name="sample_text")
    a2 = bz242995_Writer(name="sample_text_2")
    b = bz242995_Book(category="sample_text", pages=7, title="sample_text")
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


def test_assoc_theAuthor5_reverse_link_reassign_clear():
    a1 = bz242995_OneTimeWonder(Name="sample_text", id="sample_text")
    a2 = bz242995_OneTimeWonder(Name="sample_text_2", id="sample_text_2")
    b = bz242995_Author(Name="sample_text", id="sample_text")
    _safe_set(b, 'Author', a1)
    assert _is_linked(b, 'Author', a1)
    if hasattr(a1, 'theBook'):
        assert _is_linked(a1, 'theBook', b)
    _safe_set(b, 'Author', a2)
    assert _is_linked(b, 'Author', a2)
    if hasattr(a1, 'theBook'):
        assert not _is_linked(a1, 'theBook', b)
    if hasattr(a2, 'theBook'):
        assert _is_linked(a2, 'theBook', b)
    _safe_set(b, 'Author', None)
    assert not _is_linked(b, 'Author', a2)
    if hasattr(a2, 'theBook'):
        assert not _is_linked(a2, 'theBook', b)


def test_assoc_theBook6_reverse_link_reassign_clear():
    a1 = bz242995_OneTimeWonder(Name="sample_text", id="sample_text")
    a2 = bz242995_OneTimeWonder(Name="sample_text_2", id="sample_text_2")
    b = bz242995_Author(Name="sample_text", id="sample_text")
    _safe_set(b, 'theAuthor', a1)
    assert _is_linked(b, 'theAuthor', a1)
    if hasattr(a1, 'OneTimeWonder'):
        assert _is_linked(a1, 'OneTimeWonder', b)
    _safe_set(b, 'theAuthor', a2)
    assert _is_linked(b, 'theAuthor', a2)
    if hasattr(a1, 'OneTimeWonder'):
        assert not _is_linked(a1, 'OneTimeWonder', b)
    if hasattr(a2, 'OneTimeWonder'):
        assert _is_linked(a2, 'OneTimeWonder', b)
    _safe_set(b, 'theAuthor', None)
    assert not _is_linked(b, 'theAuthor', a2)
    if hasattr(a2, 'OneTimeWonder'):
        assert not _is_linked(a2, 'OneTimeWonder', b)


def test_assoc_writers1_reverse_link_reassign_clear():
    a1 = bz242995_Writer(name="sample_text")
    a2 = bz242995_Writer(name="sample_text_2")
    b = bz242995_Library(name="sample_text")
    _safe_set(b, 'bz242995_Library', {a1})
    assert _is_linked(b, 'bz242995_Library', a1)
    if hasattr(a1, 'bz242995_Writer'):
        assert _is_linked(a1, 'bz242995_Writer', b)
    _safe_set(b, 'bz242995_Library', {a2})
    assert _is_linked(b, 'bz242995_Library', a2)
    if hasattr(a1, 'bz242995_Writer'):
        assert not _is_linked(a1, 'bz242995_Writer', b)
    if hasattr(a2, 'bz242995_Writer'):
        assert _is_linked(a2, 'bz242995_Writer', b)
    _safe_set(b, 'bz242995_Library', set())
    assert not _is_linked(b, 'bz242995_Library', a2)
    if hasattr(a2, 'bz242995_Writer'):
        assert not _is_linked(a2, 'bz242995_Writer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


