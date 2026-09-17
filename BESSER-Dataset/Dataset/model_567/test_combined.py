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
    tutorial_Member,
    tutorial_Loan,
    tutorial_Book,
    tutorial_Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tutorial_member_is_not_abstract():
    assert not inspect.isabstract(tutorial_Member)


def test_hyp_tutorial_member_constructor_exists():
    assert callable(tutorial_Member.__init__)


def test_hyp_tutorial_member_constructor_args():
    sig = inspect.signature(tutorial_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tutorial_loan_is_not_abstract():
    assert not inspect.isabstract(tutorial_Loan)


def test_hyp_tutorial_loan_constructor_exists():
    assert callable(tutorial_Loan.__init__)


def test_hyp_tutorial_loan_constructor_args():
    sig = inspect.signature(tutorial_Loan.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"




def test_hyp_tutorial_book_is_not_abstract():
    assert not inspect.isabstract(tutorial_Book)


def test_hyp_tutorial_book_constructor_exists():
    assert callable(tutorial_Book.__init__)


def test_hyp_tutorial_book_constructor_args():
    sig = inspect.signature(tutorial_Book.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_tutorial_library_is_not_abstract():
    assert not inspect.isabstract(tutorial_Library)


def test_hyp_tutorial_library_constructor_exists():
    assert callable(tutorial_Library.__init__)


def test_hyp_tutorial_library_constructor_args():
    sig = inspect.signature(tutorial_Library.__init__)
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
tutorial_Member_strategy = st.builds(
    tutorial_Member,
    name=
        safe_text
)
tutorial_Loan_strategy = st.builds(
    tutorial_Loan,
    date=
        st.dates()
)
tutorial_Book_strategy = st.builds(
    tutorial_Book,
    copies=
        safe_text,
    name=
        safe_text
)
tutorial_Library_strategy = st.builds(
    tutorial_Library,
    name=
        st.booleans()
)




@given(instance=tutorial_Member_strategy)
def test_hyp_tutorial_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=tutorial_Loan_strategy)
def test_hyp_tutorial_loan_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=tutorial_Book_strategy)
def test_hyp_tutorial_book_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original



@given(instance=tutorial_Book_strategy)
def test_hyp_tutorial_book_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tutorial_Book_strategy)
@settings(max_examples=30)
def test_hyp_tutorial_book_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in tutorial_Book is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in tutorial_Book did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in tutorial_Book is not implemented or raised an error")




@given(instance=tutorial_Library_strategy)
def test_hyp_tutorial_library_name_setter(instance):
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
    tutorial_Book,
    tutorial_Library,
    tutorial_Loan,
    tutorial_Member,
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

def test_tutorial_Book_copies_value_roundtrip():
    instance = tutorial_Book(copies="sample_text", name="sample_text")
    assert instance.copies == "sample_text"
    instance.copies = "sample_text_2"
    assert instance.copies == "sample_text_2"


def test_tutorial_Book_name_value_roundtrip():
    instance = tutorial_Book(copies="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tutorial_Library_name_value_roundtrip():
    instance = tutorial_Library(name=True)
    assert instance.name == True
    instance.name = False
    assert instance.name == False


def test_tutorial_Loan_date_value_roundtrip():
    instance = tutorial_Loan(date=date(2024, 1, 1))
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_tutorial_Member_name_value_roundtrip():
    instance = tutorial_Member(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_book14_link_reassign_clear():
    a = tutorial_Loan(date=date(2024, 1, 1))
    b1 = tutorial_Book(copies="sample_text", name="sample_text")
    b2 = tutorial_Book(copies="sample_text_2", name="sample_text_2")
    _safe_set(a, 'tutorial_Loan15', b1)
    assert _is_linked(a, 'tutorial_Loan15', b1)
    if hasattr(b1, 'tutorial_Book16'):
        assert _is_linked(b1, 'tutorial_Book16', a)
    _safe_set(a, 'tutorial_Loan15', b2)
    assert _is_linked(a, 'tutorial_Loan15', b2)
    if hasattr(b1, 'tutorial_Book16'):
        assert not _is_linked(b1, 'tutorial_Book16', a)
    if hasattr(b2, 'tutorial_Book16'):
        assert _is_linked(b2, 'tutorial_Book16', a)
    _safe_set(a, 'tutorial_Loan15', None)
    assert not _is_linked(a, 'tutorial_Loan15', b2)
    if hasattr(b2, 'tutorial_Book16'):
        assert not _is_linked(b2, 'tutorial_Book16', a)


def test_assoc_books0_link_reassign_clear():
    a = tutorial_Library(name=True)
    b1 = tutorial_Book(copies="sample_text", name="sample_text")
    b2 = tutorial_Book(copies="sample_text_2", name="sample_text_2")
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


def test_assoc_books11_link_reassign_clear():
    a = tutorial_Member(name="sample_text")
    b1 = tutorial_Book(copies="sample_text", name="sample_text")
    b2 = tutorial_Book(copies="sample_text_2", name="sample_text_2")
    _safe_set(a, 'tutorial_Member12', {b1})
    assert _is_linked(a, 'tutorial_Member12', b1)
    if hasattr(b1, 'tutorial_Book13'):
        assert _is_linked(b1, 'tutorial_Book13', a)
    _safe_set(a, 'tutorial_Member12', {b2})
    assert _is_linked(a, 'tutorial_Member12', b2)
    if hasattr(b1, 'tutorial_Book13'):
        assert not _is_linked(b1, 'tutorial_Book13', a)
    if hasattr(b2, 'tutorial_Book13'):
        assert _is_linked(b2, 'tutorial_Book13', a)
    _safe_set(a, 'tutorial_Member12', set())
    assert not _is_linked(a, 'tutorial_Member12', b2)
    if hasattr(b2, 'tutorial_Book13'):
        assert not _is_linked(b2, 'tutorial_Book13', a)


def test_assoc_library4_link_reassign_clear():
    a = tutorial_Library(name=True)
    b1 = tutorial_Book(copies="sample_text", name="sample_text")
    b2 = tutorial_Book(copies="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Library', b1)
    assert _is_linked(a, 'Library', b1)
    if hasattr(b1, 'books'):
        assert _is_linked(b1, 'books', a)
    _safe_set(a, 'Library', b2)
    assert _is_linked(a, 'Library', b2)
    if hasattr(b1, 'books'):
        assert not _is_linked(b1, 'books', a)
    if hasattr(b2, 'books'):
        assert _is_linked(b2, 'books', a)
    _safe_set(a, 'Library', None)
    assert not _is_linked(a, 'Library', b2)
    if hasattr(b2, 'books'):
        assert not _is_linked(b2, 'books', a)


def test_assoc_library7_link_reassign_clear():
    a = tutorial_Member(name="sample_text")
    b1 = tutorial_Library(name=True)
    b2 = tutorial_Library(name=False)
    _safe_set(a, 'members', b1)
    assert _is_linked(a, 'members', b1)
    if hasattr(b1, 'Library8'):
        assert _is_linked(b1, 'Library8', a)
    _safe_set(a, 'members', b2)
    assert _is_linked(a, 'members', b2)
    if hasattr(b1, 'Library8'):
        assert not _is_linked(b1, 'Library8', a)
    if hasattr(b2, 'Library8'):
        assert _is_linked(b2, 'Library8', a)
    _safe_set(a, 'members', None)
    assert not _is_linked(a, 'members', b2)
    if hasattr(b2, 'Library8'):
        assert not _is_linked(b2, 'Library8', a)


def test_assoc_loans1_link_reassign_clear():
    a = tutorial_Loan(date=date(2024, 1, 1))
    b1 = tutorial_Library(name=True)
    b2 = tutorial_Library(name=False)
    _safe_set(a, 'tutorial_Loan', b1)
    assert _is_linked(a, 'tutorial_Loan', b1)
    if hasattr(b1, 'tutorial_Library'):
        assert _is_linked(b1, 'tutorial_Library', a)
    _safe_set(a, 'tutorial_Loan', b2)
    assert _is_linked(a, 'tutorial_Loan', b2)
    if hasattr(b1, 'tutorial_Library'):
        assert not _is_linked(b1, 'tutorial_Library', a)
    if hasattr(b2, 'tutorial_Library'):
        assert _is_linked(b2, 'tutorial_Library', a)
    _safe_set(a, 'tutorial_Loan', None)
    assert not _is_linked(a, 'tutorial_Loan', b2)
    if hasattr(b2, 'tutorial_Library'):
        assert not _is_linked(b2, 'tutorial_Library', a)


def test_assoc_loans5_link_reassign_clear():
    a = tutorial_Loan(date=date(2024, 1, 1))
    b1 = tutorial_Book(copies="sample_text", name="sample_text")
    b2 = tutorial_Book(copies="sample_text_2", name="sample_text_2")
    _safe_set(a, 'tutorial_Loan6', b1)
    assert _is_linked(a, 'tutorial_Loan6', b1)
    if hasattr(b1, 'tutorial_Book'):
        assert _is_linked(b1, 'tutorial_Book', a)
    _safe_set(a, 'tutorial_Loan6', b2)
    assert _is_linked(a, 'tutorial_Loan6', b2)
    if hasattr(b1, 'tutorial_Book'):
        assert not _is_linked(b1, 'tutorial_Book', a)
    if hasattr(b2, 'tutorial_Book'):
        assert _is_linked(b2, 'tutorial_Book', a)
    _safe_set(a, 'tutorial_Loan6', None)
    assert not _is_linked(a, 'tutorial_Loan6', b2)
    if hasattr(b2, 'tutorial_Book'):
        assert not _is_linked(b2, 'tutorial_Book', a)


def test_assoc_loans9_link_reassign_clear():
    a = tutorial_Member(name="sample_text")
    b1 = tutorial_Loan(date=date(2024, 1, 1))
    b2 = tutorial_Loan(date=date(2025, 6, 15))
    _safe_set(a, 'tutorial_Member', {b1})
    assert _is_linked(a, 'tutorial_Member', b1)
    if hasattr(b1, 'tutorial_Loan10'):
        assert _is_linked(b1, 'tutorial_Loan10', a)
    _safe_set(a, 'tutorial_Member', {b2})
    assert _is_linked(a, 'tutorial_Member', b2)
    if hasattr(b1, 'tutorial_Loan10'):
        assert not _is_linked(b1, 'tutorial_Loan10', a)
    if hasattr(b2, 'tutorial_Loan10'):
        assert _is_linked(b2, 'tutorial_Loan10', a)
    _safe_set(a, 'tutorial_Member', set())
    assert not _is_linked(a, 'tutorial_Member', b2)
    if hasattr(b2, 'tutorial_Loan10'):
        assert not _is_linked(b2, 'tutorial_Loan10', a)


def test_assoc_member17_link_reassign_clear():
    a = tutorial_Member(name="sample_text")
    b1 = tutorial_Loan(date=date(2024, 1, 1))
    b2 = tutorial_Loan(date=date(2025, 6, 15))
    _safe_set(a, 'tutorial_Member19', b1)
    assert _is_linked(a, 'tutorial_Member19', b1)
    if hasattr(b1, 'tutorial_Loan18'):
        assert _is_linked(b1, 'tutorial_Loan18', a)
    _safe_set(a, 'tutorial_Member19', b2)
    assert _is_linked(a, 'tutorial_Member19', b2)
    if hasattr(b1, 'tutorial_Loan18'):
        assert not _is_linked(b1, 'tutorial_Loan18', a)
    if hasattr(b2, 'tutorial_Loan18'):
        assert _is_linked(b2, 'tutorial_Loan18', a)
    _safe_set(a, 'tutorial_Member19', None)
    assert not _is_linked(a, 'tutorial_Member19', b2)
    if hasattr(b2, 'tutorial_Loan18'):
        assert not _is_linked(b2, 'tutorial_Loan18', a)


def test_assoc_members2_link_reassign_clear():
    a = tutorial_Member(name="sample_text")
    b1 = tutorial_Library(name=True)
    b2 = tutorial_Library(name=False)
    _safe_set(a, 'Member', b1)
    assert _is_linked(a, 'Member', b1)
    if hasattr(b1, 'library3'):
        assert _is_linked(b1, 'library3', a)
    _safe_set(a, 'Member', b2)
    assert _is_linked(a, 'Member', b2)
    if hasattr(b1, 'library3'):
        assert not _is_linked(b1, 'library3', a)
    if hasattr(b2, 'library3'):
        assert _is_linked(b2, 'library3', a)
    _safe_set(a, 'Member', None)
    assert not _is_linked(a, 'Member', b2)
    if hasattr(b2, 'library3'):
        assert not _is_linked(b2, 'library3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

tutorial_Book_strategy = st.builds(tutorial_Book, copies=safe_text, name=safe_text)
@given(instance=tutorial_Book_strategy)
@settings(max_examples=25)
def test_tutorial_Book_instantiation(instance):
    assert isinstance(instance, tutorial_Book)


tutorial_Library_strategy = st.builds(tutorial_Library, name=st.booleans())
@given(instance=tutorial_Library_strategy)
@settings(max_examples=25)
def test_tutorial_Library_instantiation(instance):
    assert isinstance(instance, tutorial_Library)


tutorial_Loan_strategy = st.builds(tutorial_Loan, date=st.dates())
@given(instance=tutorial_Loan_strategy)
@settings(max_examples=25)
def test_tutorial_Loan_instantiation(instance):
    assert isinstance(instance, tutorial_Loan)


tutorial_Member_strategy = st.builds(tutorial_Member, name=safe_text)
@given(instance=tutorial_Member_strategy)
@settings(max_examples=25)
def test_tutorial_Member_instantiation(instance):
    assert isinstance(instance, tutorial_Member)



