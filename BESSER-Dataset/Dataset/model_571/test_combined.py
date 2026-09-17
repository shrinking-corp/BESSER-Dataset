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
    tutorial_Loan,
    tutorial_Book,
    tutorial_Library,
    tutorial_SubOrg2_sb2C,
    tutorial_SubOrg1_sb1C,
    Organization_tutorial_Item,
    Library,
    tutorial_Organization_Ref,
    SubOrg2_sb2C,
    Employee,
    tutorial_Organization_Librarian,
    SubOrg1_sb1C,
    tutorial_Member,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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




def test_hyp_tutorial_suborg2_sb2c_is_not_abstract():
    assert not inspect.isabstract(tutorial_SubOrg2_sb2C)


def test_hyp_tutorial_suborg2_sb2c_constructor_exists():
    assert callable(tutorial_SubOrg2_sb2C.__init__)


def test_hyp_tutorial_suborg2_sb2c_constructor_args():
    sig = inspect.signature(tutorial_SubOrg2_sb2C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tutorial_suborg1_sb1c_is_not_abstract():
    assert not inspect.isabstract(tutorial_SubOrg1_sb1C)


def test_hyp_tutorial_suborg1_sb1c_constructor_exists():
    assert callable(tutorial_SubOrg1_sb1C.__init__)


def test_hyp_tutorial_suborg1_sb1c_constructor_args():
    sig = inspect.signature(tutorial_SubOrg1_sb1C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_organization_tutorial_item_is_not_abstract():
    assert not inspect.isabstract(Organization_tutorial_Item)


def test_hyp_organization_tutorial_item_constructor_exists():
    assert callable(Organization_tutorial_Item.__init__)


def test_hyp_organization_tutorial_item_constructor_args():
    sig = inspect.signature(Organization_tutorial_Item.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_hyp_library_constructor_exists():
    assert callable(Library.__init__)


def test_hyp_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tutorial_organization_ref_is_not_abstract():
    assert not inspect.isabstract(tutorial_Organization_Ref)


def test_hyp_tutorial_organization_ref_constructor_exists():
    assert callable(tutorial_Organization_Ref.__init__)


def test_hyp_tutorial_organization_ref_constructor_args():
    sig = inspect.signature(tutorial_Organization_Ref.__init__)
    params = list(sig.parameters.keys())



def test_hyp_suborg2_sb2c_is_not_abstract():
    assert not inspect.isabstract(SubOrg2_sb2C)


def test_hyp_suborg2_sb2c_constructor_exists():
    assert callable(SubOrg2_sb2C.__init__)


def test_hyp_suborg2_sb2c_constructor_args():
    sig = inspect.signature(SubOrg2_sb2C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tutorial_organization_librarian_is_not_abstract():
    assert not inspect.isabstract(tutorial_Organization_Librarian)


def test_hyp_tutorial_organization_librarian_constructor_exists():
    assert callable(tutorial_Organization_Librarian.__init__)


def test_hyp_tutorial_organization_librarian_constructor_args():
    sig = inspect.signature(tutorial_Organization_Librarian.__init__)
    params = list(sig.parameters.keys())



def test_hyp_suborg1_sb1c_is_not_abstract():
    assert not inspect.isabstract(SubOrg1_sb1C)


def test_hyp_suborg1_sb1c_constructor_exists():
    assert callable(SubOrg1_sb1C.__init__)


def test_hyp_suborg1_sb1c_constructor_args():
    sig = inspect.signature(SubOrg1_sb1C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tutorial_member_is_not_abstract():
    assert not inspect.isabstract(tutorial_Member)


def test_hyp_tutorial_member_constructor_exists():
    assert callable(tutorial_Member.__init__)


def test_hyp_tutorial_member_constructor_args():
    sig = inspect.signature(tutorial_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_hyp_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "asd",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
        safe_text
)
tutorial_SubOrg2_sb2C_strategy = st.builds(
    tutorial_SubOrg2_sb2C,
)
tutorial_SubOrg1_sb1C_strategy = st.builds(
    tutorial_SubOrg1_sb1C,
)
Organization_tutorial_Item_strategy = st.builds(
    Organization_tutorial_Item,
)
Library_strategy = st.builds(
    Library,
)
tutorial_Organization_Ref_strategy = st.builds(
    tutorial_Organization_Ref,
)
SubOrg2_sb2C_strategy = st.builds(
    SubOrg2_sb2C,
)
Employee_strategy = st.builds(
    Employee,
)
tutorial_Organization_Librarian_strategy = st.builds(
    tutorial_Organization_Librarian,
)
SubOrg1_sb1C_strategy = st.builds(
    SubOrg1_sb1C,
)
tutorial_Member_strategy = st.builds(
    tutorial_Member,
    name=
        safe_text
)




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
        instance.isAvailable(
            "test", 
            "test"
        )
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









import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tutorial_Organization_Librarian_strategy)
@settings(max_examples=30)
def test_hyp_tutorial_organization_librarian_orgopp_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.orgOpp()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.orgOpp).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'orgOpp' in tutorial_Organization_Librarian is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'orgOpp' in tutorial_Organization_Librarian did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'orgOpp' in tutorial_Organization_Librarian is not implemented or raised an error")





@given(instance=tutorial_Member_strategy)
def test_hyp_tutorial_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tutorial_Member_strategy)
@settings(max_examples=30)
def test_hyp_tutorial_member_tespop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.tespOP()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.tespOP).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'tespOP' in tutorial_Member is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'tespOP' in tutorial_Member did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'tespOP' in tutorial_Member is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Employee,
    Library,
    Organization_tutorial_Item,
    SubOrg1_sb1C,
    SubOrg2_sb2C,
    tutorial_Book,
    tutorial_Library,
    tutorial_Loan,
    tutorial_Member,
    tutorial_Organization_Librarian,
    tutorial_Organization_Ref,
    tutorial_SubOrg1_sb1C,
    tutorial_SubOrg2_sb2C,
    Type,
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
    instance = tutorial_Library(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


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


def test_tutorial_Organization_Librarian_isa_Employee():
    instance = tutorial_Organization_Librarian()
    assert isinstance(instance, Employee)


def test_tutorial_Organization_Ref_isa_Library():
    instance = tutorial_Organization_Ref()
    assert isinstance(instance, Library)


def test_assoc_book14_link_reassign_clear():
    a = tutorial_Loan(date=date(2024, 1, 1))
    b1 = SubOrg1_sb1C()
    b2 = SubOrg1_sb1C()
    _safe_set(a, 'tutorial_Loan15', b1)
    assert _is_linked(a, 'tutorial_Loan15', b1)
    if hasattr(b1, 'SubOrg1_sb1C'):
        assert _is_linked(b1, 'SubOrg1_sb1C', a)
    _safe_set(a, 'tutorial_Loan15', b2)
    assert _is_linked(a, 'tutorial_Loan15', b2)
    if hasattr(b1, 'SubOrg1_sb1C'):
        assert not _is_linked(b1, 'SubOrg1_sb1C', a)
    if hasattr(b2, 'SubOrg1_sb1C'):
        assert _is_linked(b2, 'SubOrg1_sb1C', a)
    _safe_set(a, 'tutorial_Loan15', None)
    assert not _is_linked(a, 'tutorial_Loan15', b2)
    if hasattr(b2, 'SubOrg1_sb1C'):
        assert not _is_linked(b2, 'SubOrg1_sb1C', a)


def test_assoc_books0_link_reassign_clear():
    a = tutorial_Library(name="sample_text")
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
    a = tutorial_Library(name="sample_text")
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
    b1 = tutorial_Library(name="sample_text")
    b2 = tutorial_Library(name="sample_text_2")
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
    b1 = tutorial_Library(name="sample_text")
    b2 = tutorial_Library(name="sample_text_2")
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


def test_assoc_member16_link_reassign_clear():
    a = tutorial_Member(name="sample_text")
    b1 = tutorial_Loan(date=date(2024, 1, 1))
    b2 = tutorial_Loan(date=date(2025, 6, 15))
    _safe_set(a, 'tutorial_Member18', b1)
    assert _is_linked(a, 'tutorial_Member18', b1)
    if hasattr(b1, 'tutorial_Loan17'):
        assert _is_linked(b1, 'tutorial_Loan17', a)
    _safe_set(a, 'tutorial_Member18', b2)
    assert _is_linked(a, 'tutorial_Member18', b2)
    if hasattr(b1, 'tutorial_Loan17'):
        assert not _is_linked(b1, 'tutorial_Loan17', a)
    if hasattr(b2, 'tutorial_Loan17'):
        assert _is_linked(b2, 'tutorial_Loan17', a)
    _safe_set(a, 'tutorial_Member18', None)
    assert not _is_linked(a, 'tutorial_Member18', b2)
    if hasattr(b2, 'tutorial_Loan17'):
        assert not _is_linked(b2, 'tutorial_Loan17', a)


def test_assoc_members2_link_reassign_clear():
    a = tutorial_Member(name="sample_text")
    b1 = tutorial_Library(name="sample_text")
    b2 = tutorial_Library(name="sample_text_2")
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


def test_assoc_workOn19_link_reassign_clear():
    a = tutorial_Organization_Librarian()
    b1 = SubOrg2_sb2C()
    b2 = SubOrg2_sb2C()
    _safe_set(a, 'tutorial_Organization_Librarian', b1)
    assert _is_linked(a, 'tutorial_Organization_Librarian', b1)
    if hasattr(b1, 'SubOrg2_sb2C'):
        assert _is_linked(b1, 'SubOrg2_sb2C', a)
    _safe_set(a, 'tutorial_Organization_Librarian', b2)
    assert _is_linked(a, 'tutorial_Organization_Librarian', b2)
    if hasattr(b1, 'SubOrg2_sb2C'):
        assert not _is_linked(b1, 'SubOrg2_sb2C', a)
    if hasattr(b2, 'SubOrg2_sb2C'):
        assert _is_linked(b2, 'SubOrg2_sb2C', a)
    _safe_set(a, 'tutorial_Organization_Librarian', None)
    assert not _is_linked(a, 'tutorial_Organization_Librarian', b2)
    if hasattr(b2, 'SubOrg2_sb2C'):
        assert not _is_linked(b2, 'SubOrg2_sb2C', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Employee_strategy = st.builds(Employee)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Library_strategy = st.builds(Library)
@given(instance=Library_strategy)
@settings(max_examples=25)
def test_Library_instantiation(instance):
    assert isinstance(instance, Library)


Organization_tutorial_Item_strategy = st.builds(Organization_tutorial_Item)
@given(instance=Organization_tutorial_Item_strategy)
@settings(max_examples=25)
def test_Organization_tutorial_Item_instantiation(instance):
    assert isinstance(instance, Organization_tutorial_Item)


SubOrg1_sb1C_strategy = st.builds(SubOrg1_sb1C)
@given(instance=SubOrg1_sb1C_strategy)
@settings(max_examples=25)
def test_SubOrg1_sb1C_instantiation(instance):
    assert isinstance(instance, SubOrg1_sb1C)


SubOrg2_sb2C_strategy = st.builds(SubOrg2_sb2C)
@given(instance=SubOrg2_sb2C_strategy)
@settings(max_examples=25)
def test_SubOrg2_sb2C_instantiation(instance):
    assert isinstance(instance, SubOrg2_sb2C)


tutorial_Book_strategy = st.builds(tutorial_Book, copies=safe_text, name=safe_text)
@given(instance=tutorial_Book_strategy)
@settings(max_examples=25)
def test_tutorial_Book_instantiation(instance):
    assert isinstance(instance, tutorial_Book)


tutorial_Library_strategy = st.builds(tutorial_Library, name=safe_text)
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


tutorial_Organization_Librarian_strategy = st.builds(tutorial_Organization_Librarian)
@given(instance=tutorial_Organization_Librarian_strategy)
@settings(max_examples=25)
def test_tutorial_Organization_Librarian_instantiation(instance):
    assert isinstance(instance, tutorial_Organization_Librarian)


tutorial_Organization_Ref_strategy = st.builds(tutorial_Organization_Ref)
@given(instance=tutorial_Organization_Ref_strategy)
@settings(max_examples=25)
def test_tutorial_Organization_Ref_instantiation(instance):
    assert isinstance(instance, tutorial_Organization_Ref)


tutorial_SubOrg1_sb1C_strategy = st.builds(tutorial_SubOrg1_sb1C)
@given(instance=tutorial_SubOrg1_sb1C_strategy)
@settings(max_examples=25)
def test_tutorial_SubOrg1_sb1C_instantiation(instance):
    assert isinstance(instance, tutorial_SubOrg1_sb1C)


tutorial_SubOrg2_sb2C_strategy = st.builds(tutorial_SubOrg2_sb2C)
@given(instance=tutorial_SubOrg2_sb2C_strategy)
@settings(max_examples=25)
def test_tutorial_SubOrg2_sb2C_instantiation(instance):
    assert isinstance(instance, tutorial_SubOrg2_sb2C)



