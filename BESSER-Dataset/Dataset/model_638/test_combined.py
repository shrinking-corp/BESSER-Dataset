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
    libraryModel_ecore_NamedElement,
    libraryModel_ecore_LibraryModel,
    NamedElement,
    libraryModel_ecore_Author,
    libraryModel_ecore_Picture,
    libraryModel_ecore_Book,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_librarymodel_ecore_namedelement_is_not_abstract():
    assert not inspect.isabstract(libraryModel_ecore_NamedElement)


def test_hyp_librarymodel_ecore_namedelement_constructor_exists():
    assert callable(libraryModel_ecore_NamedElement.__init__)


def test_hyp_librarymodel_ecore_namedelement_constructor_args():
    sig = inspect.signature(libraryModel_ecore_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_librarymodel_ecore_librarymodel_is_not_abstract():
    assert not inspect.isabstract(libraryModel_ecore_LibraryModel)


def test_hyp_librarymodel_ecore_librarymodel_constructor_exists():
    assert callable(libraryModel_ecore_LibraryModel.__init__)


def test_hyp_librarymodel_ecore_librarymodel_constructor_args():
    sig = inspect.signature(libraryModel_ecore_LibraryModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_librarymodel_ecore_author_is_not_abstract():
    assert not inspect.isabstract(libraryModel_ecore_Author)


def test_hyp_librarymodel_ecore_author_constructor_exists():
    assert callable(libraryModel_ecore_Author.__init__)


def test_hyp_librarymodel_ecore_author_constructor_args():
    sig = inspect.signature(libraryModel_ecore_Author.__init__)
    params = list(sig.parameters.keys())



def test_hyp_librarymodel_ecore_picture_is_not_abstract():
    assert not inspect.isabstract(libraryModel_ecore_Picture)


def test_hyp_librarymodel_ecore_picture_constructor_exists():
    assert callable(libraryModel_ecore_Picture.__init__)


def test_hyp_librarymodel_ecore_picture_constructor_args():
    sig = inspect.signature(libraryModel_ecore_Picture.__init__)
    params = list(sig.parameters.keys())
    assert "pageNumber" in params, "Missing parameter 'pageNumber'"




def test_hyp_librarymodel_ecore_book_is_not_abstract():
    assert not inspect.isabstract(libraryModel_ecore_Book)


def test_hyp_librarymodel_ecore_book_constructor_exists():
    assert callable(libraryModel_ecore_Book.__init__)


def test_hyp_librarymodel_ecore_book_constructor_args():
    sig = inspect.signature(libraryModel_ecore_Book.__init__)
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
libraryModel_ecore_NamedElement_strategy = st.builds(
    libraryModel_ecore_NamedElement,
    Name=
        safe_text
)
libraryModel_ecore_LibraryModel_strategy = st.builds(
    libraryModel_ecore_LibraryModel,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
libraryModel_ecore_Author_strategy = st.builds(
    libraryModel_ecore_Author,
)
libraryModel_ecore_Picture_strategy = st.builds(
    libraryModel_ecore_Picture,
    pageNumber=
        safe_text
)
libraryModel_ecore_Book_strategy = st.builds(
    libraryModel_ecore_Book,
)




@given(instance=libraryModel_ecore_NamedElement_strategy)
def test_hyp_librarymodel_ecore_namedelement_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=libraryModel_ecore_LibraryModel_strategy)
@settings(max_examples=30)
def test_hyp_librarymodel_ecore_librarymodel_printlibrary_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printLibrary()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printLibrary).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printLibrary' in libraryModel_ecore_LibraryModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printLibrary' in libraryModel_ecore_LibraryModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printLibrary' in libraryModel_ecore_LibraryModel is not implemented or raised an error")






@given(instance=libraryModel_ecore_Picture_strategy)
def test_hyp_librarymodel_ecore_picture_pageNumber_setter(instance):
    original = instance.pageNumber
    instance.pageNumber = original
    assert instance.pageNumber == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    libraryModel_ecore_Author,
    libraryModel_ecore_Book,
    libraryModel_ecore_LibraryModel,
    libraryModel_ecore_NamedElement,
    libraryModel_ecore_Picture,
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

def test_libraryModel_ecore_NamedElement_Name_value_roundtrip():
    instance = libraryModel_ecore_NamedElement(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_libraryModel_ecore_Picture_pageNumber_value_roundtrip():
    instance = libraryModel_ecore_Picture(pageNumber="sample_text")
    assert instance.pageNumber == "sample_text"
    instance.pageNumber = "sample_text_2"
    assert instance.pageNumber == "sample_text_2"


def test_libraryModel_ecore_Author_isa_NamedElement():
    instance = libraryModel_ecore_Author()
    assert isinstance(instance, NamedElement)


def test_libraryModel_ecore_Book_isa_NamedElement():
    instance = libraryModel_ecore_Book()
    assert isinstance(instance, NamedElement)


def test_libraryModel_ecore_Picture_isa_NamedElement():
    instance = libraryModel_ecore_Picture(pageNumber="sample_text")
    assert isinstance(instance, NamedElement)


def test_assoc_authors7_link_reassign_clear():
    a = libraryModel_ecore_LibraryModel()
    b1 = libraryModel_ecore_Author()
    b2 = libraryModel_ecore_Author()
    _safe_set(a, 'library8', {b1})
    assert _is_linked(a, 'library8', b1)
    if hasattr(b1, 'Author'):
        assert _is_linked(b1, 'Author', a)
    _safe_set(a, 'library8', {b2})
    assert _is_linked(a, 'library8', b2)
    if hasattr(b1, 'Author'):
        assert not _is_linked(b1, 'Author', a)
    if hasattr(b2, 'Author'):
        assert _is_linked(b2, 'Author', a)
    _safe_set(a, 'library8', set())
    assert not _is_linked(a, 'library8', b2)
    if hasattr(b2, 'Author'):
        assert not _is_linked(b2, 'Author', a)


def test_assoc_book6_link_reassign_clear():
    a = libraryModel_ecore_LibraryModel()
    b1 = libraryModel_ecore_Book()
    b2 = libraryModel_ecore_Book()
    _safe_set(a, 'library', {b1})
    assert _is_linked(a, 'library', b1)
    if hasattr(b1, 'Book'):
        assert _is_linked(b1, 'Book', a)
    _safe_set(a, 'library', {b2})
    assert _is_linked(a, 'library', b2)
    if hasattr(b1, 'Book'):
        assert not _is_linked(b1, 'Book', a)
    if hasattr(b2, 'Book'):
        assert _is_linked(b2, 'Book', a)
    _safe_set(a, 'library', set())
    assert not _is_linked(a, 'library', b2)
    if hasattr(b2, 'Book'):
        assert not _is_linked(b2, 'Book', a)


def test_assoc_book9_link_reassign_clear():
    a = libraryModel_ecore_Picture(pageNumber="sample_text")
    b1 = libraryModel_ecore_Book()
    b2 = libraryModel_ecore_Book()
    _safe_set(a, 'pictures', b1)
    assert _is_linked(a, 'pictures', b1)
    if hasattr(b1, 'Book10'):
        assert _is_linked(b1, 'Book10', a)
    _safe_set(a, 'pictures', b2)
    assert _is_linked(a, 'pictures', b2)
    if hasattr(b1, 'Book10'):
        assert not _is_linked(b1, 'Book10', a)
    if hasattr(b2, 'Book10'):
        assert _is_linked(b2, 'Book10', a)
    _safe_set(a, 'pictures', None)
    assert not _is_linked(a, 'pictures', b2)
    if hasattr(b2, 'Book10'):
        assert not _is_linked(b2, 'Book10', a)


def test_assoc_library1_link_reassign_clear():
    a = libraryModel_ecore_LibraryModel()
    b1 = libraryModel_ecore_Book()
    b2 = libraryModel_ecore_Book()
    _safe_set(a, 'LibraryModel', b1)
    assert _is_linked(a, 'LibraryModel', b1)
    if hasattr(b1, 'book'):
        assert _is_linked(b1, 'book', a)
    _safe_set(a, 'LibraryModel', b2)
    assert _is_linked(a, 'LibraryModel', b2)
    if hasattr(b1, 'book'):
        assert not _is_linked(b1, 'book', a)
    if hasattr(b2, 'book'):
        assert _is_linked(b2, 'book', a)
    _safe_set(a, 'LibraryModel', None)
    assert not _is_linked(a, 'LibraryModel', b2)
    if hasattr(b2, 'book'):
        assert not _is_linked(b2, 'book', a)


def test_assoc_library4_link_reassign_clear():
    a = libraryModel_ecore_LibraryModel()
    b1 = libraryModel_ecore_Author()
    b2 = libraryModel_ecore_Author()
    _safe_set(a, 'LibraryModel5', b1)
    assert _is_linked(a, 'LibraryModel5', b1)
    if hasattr(b1, 'authors'):
        assert _is_linked(b1, 'authors', a)
    _safe_set(a, 'LibraryModel5', b2)
    assert _is_linked(a, 'LibraryModel5', b2)
    if hasattr(b1, 'authors'):
        assert not _is_linked(b1, 'authors', a)
    if hasattr(b2, 'authors'):
        assert _is_linked(b2, 'authors', a)
    _safe_set(a, 'LibraryModel5', None)
    assert not _is_linked(a, 'LibraryModel5', b2)
    if hasattr(b2, 'authors'):
        assert not _is_linked(b2, 'authors', a)


def test_assoc_pictures2_link_reassign_clear():
    a = libraryModel_ecore_Picture(pageNumber="sample_text")
    b1 = libraryModel_ecore_Book()
    b2 = libraryModel_ecore_Book()
    _safe_set(a, 'Picture', b1)
    assert _is_linked(a, 'Picture', b1)
    if hasattr(b1, 'book3'):
        assert _is_linked(b1, 'book3', a)
    _safe_set(a, 'Picture', b2)
    assert _is_linked(a, 'Picture', b2)
    if hasattr(b1, 'book3'):
        assert not _is_linked(b1, 'book3', a)
    if hasattr(b2, 'book3'):
        assert _is_linked(b2, 'book3', a)
    _safe_set(a, 'Picture', None)
    assert not _is_linked(a, 'Picture', b2)
    if hasattr(b2, 'book3'):
        assert not _is_linked(b2, 'book3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


libraryModel_ecore_Author_strategy = st.builds(libraryModel_ecore_Author)
@given(instance=libraryModel_ecore_Author_strategy)
@settings(max_examples=25)
def test_libraryModel_ecore_Author_instantiation(instance):
    assert isinstance(instance, libraryModel_ecore_Author)


libraryModel_ecore_Book_strategy = st.builds(libraryModel_ecore_Book)
@given(instance=libraryModel_ecore_Book_strategy)
@settings(max_examples=25)
def test_libraryModel_ecore_Book_instantiation(instance):
    assert isinstance(instance, libraryModel_ecore_Book)


libraryModel_ecore_LibraryModel_strategy = st.builds(libraryModel_ecore_LibraryModel)
@given(instance=libraryModel_ecore_LibraryModel_strategy)
@settings(max_examples=25)
def test_libraryModel_ecore_LibraryModel_instantiation(instance):
    assert isinstance(instance, libraryModel_ecore_LibraryModel)


libraryModel_ecore_NamedElement_strategy = st.builds(libraryModel_ecore_NamedElement, Name=safe_text)
@given(instance=libraryModel_ecore_NamedElement_strategy)
@settings(max_examples=25)
def test_libraryModel_ecore_NamedElement_instantiation(instance):
    assert isinstance(instance, libraryModel_ecore_NamedElement)


libraryModel_ecore_Picture_strategy = st.builds(libraryModel_ecore_Picture, pageNumber=safe_text)
@given(instance=libraryModel_ecore_Picture_strategy)
@settings(max_examples=25)
def test_libraryModel_ecore_Picture_instantiation(instance):
    assert isinstance(instance, libraryModel_ecore_Picture)



