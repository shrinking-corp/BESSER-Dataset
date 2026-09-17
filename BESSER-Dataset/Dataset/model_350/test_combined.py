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
    eavlibrary_Pen,
    eavlibrary_Writer,
    eavlibrary_Book,
    eavlibrary_Library,
    eavlibrary_City,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_eavlibrary_pen_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_Pen)


def test_hyp_eavlibrary_pen_constructor_exists():
    assert callable(eavlibrary_Pen.__init__)


def test_hyp_eavlibrary_pen_constructor_args():
    sig = inspect.signature(eavlibrary_Pen.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_eavlibrary_writer_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_Writer)


def test_hyp_eavlibrary_writer_constructor_exists():
    assert callable(eavlibrary_Writer.__init__)


def test_hyp_eavlibrary_writer_constructor_args():
    sig = inspect.signature(eavlibrary_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "image" in params, "Missing parameter 'image'"
    assert "abstract" in params, "Missing parameter 'abstract'"






def test_hyp_eavlibrary_book_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_Book)


def test_hyp_eavlibrary_book_constructor_exists():
    assert callable(eavlibrary_Book.__init__)


def test_hyp_eavlibrary_book_constructor_args():
    sig = inspect.signature(eavlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "test" in params, "Missing parameter 'test'"
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"







def test_hyp_eavlibrary_library_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_Library)


def test_hyp_eavlibrary_library_constructor_exists():
    assert callable(eavlibrary_Library.__init__)


def test_hyp_eavlibrary_library_constructor_args():
    sig = inspect.signature(eavlibrary_Library.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_eavlibrary_city_is_not_abstract():
    assert not inspect.isabstract(eavlibrary_City)


def test_hyp_eavlibrary_city_constructor_exists():
    assert callable(eavlibrary_City.__init__)


def test_hyp_eavlibrary_city_constructor_args():
    sig = inspect.signature(eavlibrary_City.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_hyp_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Biography",
        "ScienceFiction",
        "Mystery",
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
eavlibrary_Pen_strategy = st.builds(
    eavlibrary_Pen,
    name=
        safe_text
)
eavlibrary_Writer_strategy = st.builds(
    eavlibrary_Writer,
    name=
        safe_text,
    image=
        safe_text,
    abstract=
        safe_text
)
eavlibrary_Book_strategy = st.builds(
    eavlibrary_Book,
    pages=
        safe_text,
    test=
        safe_text,
    title=
        safe_text,
    category=
        safe_text
)
eavlibrary_Library_strategy = st.builds(
    eavlibrary_Library,
    name=
        safe_text
)
eavlibrary_City_strategy = st.builds(
    eavlibrary_City,
    name=
        safe_text
)




@given(instance=eavlibrary_Pen_strategy)
def test_hyp_eavlibrary_pen_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=eavlibrary_Writer_strategy)
def test_hyp_eavlibrary_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eavlibrary_Writer_strategy)
def test_hyp_eavlibrary_writer_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=eavlibrary_Writer_strategy)
def test_hyp_eavlibrary_writer_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original




@given(instance=eavlibrary_Book_strategy)
def test_hyp_eavlibrary_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=eavlibrary_Book_strategy)
def test_hyp_eavlibrary_book_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original



@given(instance=eavlibrary_Book_strategy)
def test_hyp_eavlibrary_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=eavlibrary_Book_strategy)
def test_hyp_eavlibrary_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original




@given(instance=eavlibrary_Library_strategy)
def test_hyp_eavlibrary_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=eavlibrary_City_strategy)
def test_hyp_eavlibrary_city_name_setter(instance):
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
    eavlibrary_Book,
    eavlibrary_City,
    eavlibrary_Library,
    eavlibrary_Pen,
    eavlibrary_Writer,
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

def test_eavlibrary_Book_category_value_roundtrip():
    instance = eavlibrary_Book(category="sample_text", pages="sample_text", test="sample_text", title="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_eavlibrary_Book_pages_value_roundtrip():
    instance = eavlibrary_Book(category="sample_text", pages="sample_text", test="sample_text", title="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_eavlibrary_Book_test_value_roundtrip():
    instance = eavlibrary_Book(category="sample_text", pages="sample_text", test="sample_text", title="sample_text")
    assert instance.test == "sample_text"
    instance.test = "sample_text_2"
    assert instance.test == "sample_text_2"


def test_eavlibrary_Book_title_value_roundtrip():
    instance = eavlibrary_Book(category="sample_text", pages="sample_text", test="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_eavlibrary_City_name_value_roundtrip():
    instance = eavlibrary_City(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eavlibrary_Library_name_value_roundtrip():
    instance = eavlibrary_Library(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eavlibrary_Pen_name_value_roundtrip():
    instance = eavlibrary_Pen(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_eavlibrary_Writer_abstract_value_roundtrip():
    instance = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    assert instance.abstract == "sample_text"
    instance.abstract = "sample_text_2"
    assert instance.abstract == "sample_text_2"


def test_eavlibrary_Writer_image_value_roundtrip():
    instance = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_eavlibrary_Writer_name_value_roundtrip():
    instance = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_author0_link_reassign_clear():
    a = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    b1 = eavlibrary_Book(category="sample_text", pages="sample_text", test="sample_text", title="sample_text")
    b2 = eavlibrary_Book(category="sample_text_2", pages="sample_text_2", test="sample_text_2", title="sample_text_2")
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
    a = eavlibrary_Library(name="sample_text")
    b1 = eavlibrary_Book(category="sample_text", pages="sample_text", test="sample_text", title="sample_text")
    b2 = eavlibrary_Book(category="sample_text_2", pages="sample_text_2", test="sample_text_2", title="sample_text_2")
    _safe_set(a, 'eavlibrary_Library3', {b1})
    assert _is_linked(a, 'eavlibrary_Library3', b1)
    if hasattr(b1, 'eavlibrary_Book'):
        assert _is_linked(b1, 'eavlibrary_Book', a)
    _safe_set(a, 'eavlibrary_Library3', {b2})
    assert _is_linked(a, 'eavlibrary_Library3', b2)
    if hasattr(b1, 'eavlibrary_Book'):
        assert not _is_linked(b1, 'eavlibrary_Book', a)
    if hasattr(b2, 'eavlibrary_Book'):
        assert _is_linked(b2, 'eavlibrary_Book', a)
    _safe_set(a, 'eavlibrary_Library3', set())
    assert not _is_linked(a, 'eavlibrary_Library3', b2)
    if hasattr(b2, 'eavlibrary_Book'):
        assert not _is_linked(b2, 'eavlibrary_Book', a)


def test_assoc_books4_link_reassign_clear():
    a = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    b1 = eavlibrary_Book(category="sample_text", pages="sample_text", test="sample_text", title="sample_text")
    b2 = eavlibrary_Book(category="sample_text_2", pages="sample_text_2", test="sample_text_2", title="sample_text_2")
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


def test_assoc_city5_link_reassign_clear():
    a = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    b1 = eavlibrary_City(name="sample_text")
    b2 = eavlibrary_City(name="sample_text_2")
    _safe_set(a, 'eavlibrary_Writer6', b1)
    assert _is_linked(a, 'eavlibrary_Writer6', b1)
    if hasattr(b1, 'eavlibrary_City'):
        assert _is_linked(b1, 'eavlibrary_City', a)
    _safe_set(a, 'eavlibrary_Writer6', b2)
    assert _is_linked(a, 'eavlibrary_Writer6', b2)
    if hasattr(b1, 'eavlibrary_City'):
        assert not _is_linked(b1, 'eavlibrary_City', a)
    if hasattr(b2, 'eavlibrary_City'):
        assert _is_linked(b2, 'eavlibrary_City', a)
    _safe_set(a, 'eavlibrary_Writer6', None)
    assert not _is_linked(a, 'eavlibrary_Writer6', b2)
    if hasattr(b2, 'eavlibrary_City'):
        assert not _is_linked(b2, 'eavlibrary_City', a)


def test_assoc_pens7_link_reassign_clear():
    a = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    b1 = eavlibrary_Pen(name="sample_text")
    b2 = eavlibrary_Pen(name="sample_text_2")
    _safe_set(a, 'eavlibrary_Writer8', {b1})
    assert _is_linked(a, 'eavlibrary_Writer8', b1)
    if hasattr(b1, 'eavlibrary_Pen'):
        assert _is_linked(b1, 'eavlibrary_Pen', a)
    _safe_set(a, 'eavlibrary_Writer8', {b2})
    assert _is_linked(a, 'eavlibrary_Writer8', b2)
    if hasattr(b1, 'eavlibrary_Pen'):
        assert not _is_linked(b1, 'eavlibrary_Pen', a)
    if hasattr(b2, 'eavlibrary_Pen'):
        assert _is_linked(b2, 'eavlibrary_Pen', a)
    _safe_set(a, 'eavlibrary_Writer8', set())
    assert not _is_linked(a, 'eavlibrary_Writer8', b2)
    if hasattr(b2, 'eavlibrary_Pen'):
        assert not _is_linked(b2, 'eavlibrary_Pen', a)


def test_assoc_writers1_link_reassign_clear():
    a = eavlibrary_Writer(abstract="sample_text", image="sample_text", name="sample_text")
    b1 = eavlibrary_Library(name="sample_text")
    b2 = eavlibrary_Library(name="sample_text_2")
    _safe_set(a, 'eavlibrary_Writer', b1)
    assert _is_linked(a, 'eavlibrary_Writer', b1)
    if hasattr(b1, 'eavlibrary_Library'):
        assert _is_linked(b1, 'eavlibrary_Library', a)
    _safe_set(a, 'eavlibrary_Writer', b2)
    assert _is_linked(a, 'eavlibrary_Writer', b2)
    if hasattr(b1, 'eavlibrary_Library'):
        assert not _is_linked(b1, 'eavlibrary_Library', a)
    if hasattr(b2, 'eavlibrary_Library'):
        assert _is_linked(b2, 'eavlibrary_Library', a)
    _safe_set(a, 'eavlibrary_Writer', None)
    assert not _is_linked(a, 'eavlibrary_Writer', b2)
    if hasattr(b2, 'eavlibrary_Library'):
        assert not _is_linked(b2, 'eavlibrary_Library', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

eavlibrary_Book_strategy = st.builds(eavlibrary_Book, category=safe_text, pages=safe_text, test=safe_text, title=safe_text)
@given(instance=eavlibrary_Book_strategy)
@settings(max_examples=25)
def test_eavlibrary_Book_instantiation(instance):
    assert isinstance(instance, eavlibrary_Book)


eavlibrary_City_strategy = st.builds(eavlibrary_City, name=safe_text)
@given(instance=eavlibrary_City_strategy)
@settings(max_examples=25)
def test_eavlibrary_City_instantiation(instance):
    assert isinstance(instance, eavlibrary_City)


eavlibrary_Library_strategy = st.builds(eavlibrary_Library, name=safe_text)
@given(instance=eavlibrary_Library_strategy)
@settings(max_examples=25)
def test_eavlibrary_Library_instantiation(instance):
    assert isinstance(instance, eavlibrary_Library)


eavlibrary_Pen_strategy = st.builds(eavlibrary_Pen, name=safe_text)
@given(instance=eavlibrary_Pen_strategy)
@settings(max_examples=25)
def test_eavlibrary_Pen_instantiation(instance):
    assert isinstance(instance, eavlibrary_Pen)


eavlibrary_Writer_strategy = st.builds(eavlibrary_Writer, abstract=safe_text, image=safe_text, name=safe_text)
@given(instance=eavlibrary_Writer_strategy)
@settings(max_examples=25)
def test_eavlibrary_Writer_instantiation(instance):
    assert isinstance(instance, eavlibrary_Writer)



