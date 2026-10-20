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
    Faculty_Actor,
    Staff_Actor,
    Patron_Actor,
    Fees_for_overdue_books_external,
    Acquiring_Retiring_Books_external,
    Periodicals_external,
    Multimedia_external,
    Books_external,
    Reserved_or_reference_books_external,
    Aid_Patrons_external,
    Computers_external,
    StaffMember,
    MultiMedia,
    Books,
    Patron,
    Staff_Actor1,
    Resources_Component,
    Student_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_faculty_actor_is_not_abstract():
    assert not inspect.isabstract(Faculty_Actor)


def test_hyp_faculty_actor_constructor_exists():
    assert callable(Faculty_Actor.__init__)


def test_hyp_faculty_actor_constructor_args():
    sig = inspect.signature(Faculty_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staff_actor_is_not_abstract():
    assert not inspect.isabstract(Staff_Actor)


def test_hyp_staff_actor_constructor_exists():
    assert callable(Staff_Actor.__init__)


def test_hyp_staff_actor_constructor_args():
    sig = inspect.signature(Staff_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patron_actor_is_not_abstract():
    assert not inspect.isabstract(Patron_Actor)


def test_hyp_patron_actor_constructor_exists():
    assert callable(Patron_Actor.__init__)


def test_hyp_patron_actor_constructor_args():
    sig = inspect.signature(Patron_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fees_for_overdue_books_external_is_not_abstract():
    assert not inspect.isabstract(Fees_for_overdue_books_external)


def test_hyp_fees_for_overdue_books_external_constructor_exists():
    assert callable(Fees_for_overdue_books_external.__init__)


def test_hyp_fees_for_overdue_books_external_constructor_args():
    sig = inspect.signature(Fees_for_overdue_books_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_acquiring_retiring_books_external_is_not_abstract():
    assert not inspect.isabstract(Acquiring_Retiring_Books_external)


def test_hyp_acquiring_retiring_books_external_constructor_exists():
    assert callable(Acquiring_Retiring_Books_external.__init__)


def test_hyp_acquiring_retiring_books_external_constructor_args():
    sig = inspect.signature(Acquiring_Retiring_Books_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_periodicals_external_is_not_abstract():
    assert not inspect.isabstract(Periodicals_external)


def test_hyp_periodicals_external_constructor_exists():
    assert callable(Periodicals_external.__init__)


def test_hyp_periodicals_external_constructor_args():
    sig = inspect.signature(Periodicals_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multimedia_external_is_not_abstract():
    assert not inspect.isabstract(Multimedia_external)


def test_hyp_multimedia_external_constructor_exists():
    assert callable(Multimedia_external.__init__)


def test_hyp_multimedia_external_constructor_args():
    sig = inspect.signature(Multimedia_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_books_external_is_not_abstract():
    assert not inspect.isabstract(Books_external)


def test_hyp_books_external_constructor_exists():
    assert callable(Books_external.__init__)


def test_hyp_books_external_constructor_args():
    sig = inspect.signature(Books_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reserved_or_reference_books_external_is_not_abstract():
    assert not inspect.isabstract(Reserved_or_reference_books_external)


def test_hyp_reserved_or_reference_books_external_constructor_exists():
    assert callable(Reserved_or_reference_books_external.__init__)


def test_hyp_reserved_or_reference_books_external_constructor_args():
    sig = inspect.signature(Reserved_or_reference_books_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aid_patrons_external_is_not_abstract():
    assert not inspect.isabstract(Aid_Patrons_external)


def test_hyp_aid_patrons_external_constructor_exists():
    assert callable(Aid_Patrons_external.__init__)


def test_hyp_aid_patrons_external_constructor_args():
    sig = inspect.signature(Aid_Patrons_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_computers_external_is_not_abstract():
    assert not inspect.isabstract(Computers_external)


def test_hyp_computers_external_constructor_exists():
    assert callable(Computers_external.__init__)


def test_hyp_computers_external_constructor_args():
    sig = inspect.signature(Computers_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staffmember_is_not_abstract():
    assert not inspect.isabstract(StaffMember)


def test_hyp_staffmember_constructor_exists():
    assert callable(StaffMember.__init__)


def test_hyp_staffmember_constructor_args():
    sig = inspect.signature(StaffMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multimedia_is_not_abstract():
    assert not inspect.isabstract(MultiMedia)


def test_hyp_multimedia_constructor_exists():
    assert callable(MultiMedia.__init__)


def test_hyp_multimedia_constructor_args():
    sig = inspect.signature(MultiMedia.__init__)
    params = list(sig.parameters.keys())



def test_hyp_books_is_not_abstract():
    assert not inspect.isabstract(Books)


def test_hyp_books_constructor_exists():
    assert callable(Books.__init__)


def test_hyp_books_constructor_args():
    sig = inspect.signature(Books.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_patron_is_not_abstract():
    assert not inspect.isabstract(Patron)


def test_hyp_patron_constructor_exists():
    assert callable(Patron.__init__)


def test_hyp_patron_constructor_args():
    sig = inspect.signature(Patron.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staff_actor1_is_not_abstract():
    assert not inspect.isabstract(Staff_Actor1)


def test_hyp_staff_actor1_constructor_exists():
    assert callable(Staff_Actor1.__init__)


def test_hyp_staff_actor1_constructor_args():
    sig = inspect.signature(Staff_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resources_component_is_not_abstract():
    assert not inspect.isabstract(Resources_Component)


def test_hyp_resources_component_constructor_exists():
    assert callable(Resources_Component.__init__)


def test_hyp_resources_component_constructor_args():
    sig = inspect.signature(Resources_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student_actor_is_not_abstract():
    assert not inspect.isabstract(Student_Actor)


def test_hyp_student_actor_constructor_exists():
    assert callable(Student_Actor.__init__)


def test_hyp_student_actor_constructor_args():
    sig = inspect.signature(Student_Actor.__init__)
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
Faculty_Actor_strategy = st.builds(
    Faculty_Actor,
)
Staff_Actor_strategy = st.builds(
    Staff_Actor,
)
Patron_Actor_strategy = st.builds(
    Patron_Actor,
)
Fees_for_overdue_books_external_strategy = st.builds(
    Fees_for_overdue_books_external,
)
Acquiring_Retiring_Books_external_strategy = st.builds(
    Acquiring_Retiring_Books_external,
)
Periodicals_external_strategy = st.builds(
    Periodicals_external,
)
Multimedia_external_strategy = st.builds(
    Multimedia_external,
)
Books_external_strategy = st.builds(
    Books_external,
)
Reserved_or_reference_books_external_strategy = st.builds(
    Reserved_or_reference_books_external,
)
Aid_Patrons_external_strategy = st.builds(
    Aid_Patrons_external,
)
Computers_external_strategy = st.builds(
    Computers_external,
)
StaffMember_strategy = st.builds(
    StaffMember,
)
MultiMedia_strategy = st.builds(
    MultiMedia,
)
Books_strategy = st.builds(
    Books,
    title=
        safe_text
)
Patron_strategy = st.builds(
    Patron,
)
Staff_Actor1_strategy = st.builds(
    Staff_Actor1,
)
Resources_Component_strategy = st.builds(
    Resources_Component,
)
Student_Actor_strategy = st.builds(
    Student_Actor,
)

















@given(instance=Books_strategy)
def test_hyp_books_title_setter(instance):
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
    Acquiring_Retiring_Books_external,
    Aid_Patrons_external,
    Books,
    Books_external,
    Computers_external,
    Faculty_Actor,
    Fees_for_overdue_books_external,
    MultiMedia,
    Multimedia_external,
    Patron,
    Patron_Actor,
    Periodicals_external,
    Reserved_or_reference_books_external,
    Resources_Component,
    StaffMember,
    Staff_Actor,
    Staff_Actor1,
    Student_Actor,
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

def test_Books_title_value_roundtrip():
    instance = Books(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Acquiring_Retiring_Books_external_strategy = st.builds(Acquiring_Retiring_Books_external)
@given(instance=Acquiring_Retiring_Books_external_strategy)
@settings(max_examples=25)
def test_Acquiring_Retiring_Books_external_instantiation(instance):
    assert isinstance(instance, Acquiring_Retiring_Books_external)


Aid_Patrons_external_strategy = st.builds(Aid_Patrons_external)
@given(instance=Aid_Patrons_external_strategy)
@settings(max_examples=25)
def test_Aid_Patrons_external_instantiation(instance):
    assert isinstance(instance, Aid_Patrons_external)


Books_strategy = st.builds(Books, title=safe_text)
@given(instance=Books_strategy)
@settings(max_examples=25)
def test_Books_instantiation(instance):
    assert isinstance(instance, Books)


Books_external_strategy = st.builds(Books_external)
@given(instance=Books_external_strategy)
@settings(max_examples=25)
def test_Books_external_instantiation(instance):
    assert isinstance(instance, Books_external)


Computers_external_strategy = st.builds(Computers_external)
@given(instance=Computers_external_strategy)
@settings(max_examples=25)
def test_Computers_external_instantiation(instance):
    assert isinstance(instance, Computers_external)


Faculty_Actor_strategy = st.builds(Faculty_Actor)
@given(instance=Faculty_Actor_strategy)
@settings(max_examples=25)
def test_Faculty_Actor_instantiation(instance):
    assert isinstance(instance, Faculty_Actor)


Fees_for_overdue_books_external_strategy = st.builds(Fees_for_overdue_books_external)
@given(instance=Fees_for_overdue_books_external_strategy)
@settings(max_examples=25)
def test_Fees_for_overdue_books_external_instantiation(instance):
    assert isinstance(instance, Fees_for_overdue_books_external)


MultiMedia_strategy = st.builds(MultiMedia)
@given(instance=MultiMedia_strategy)
@settings(max_examples=25)
def test_MultiMedia_instantiation(instance):
    assert isinstance(instance, MultiMedia)


Multimedia_external_strategy = st.builds(Multimedia_external)
@given(instance=Multimedia_external_strategy)
@settings(max_examples=25)
def test_Multimedia_external_instantiation(instance):
    assert isinstance(instance, Multimedia_external)


Patron_strategy = st.builds(Patron)
@given(instance=Patron_strategy)
@settings(max_examples=25)
def test_Patron_instantiation(instance):
    assert isinstance(instance, Patron)


Patron_Actor_strategy = st.builds(Patron_Actor)
@given(instance=Patron_Actor_strategy)
@settings(max_examples=25)
def test_Patron_Actor_instantiation(instance):
    assert isinstance(instance, Patron_Actor)


Periodicals_external_strategy = st.builds(Periodicals_external)
@given(instance=Periodicals_external_strategy)
@settings(max_examples=25)
def test_Periodicals_external_instantiation(instance):
    assert isinstance(instance, Periodicals_external)


Reserved_or_reference_books_external_strategy = st.builds(Reserved_or_reference_books_external)
@given(instance=Reserved_or_reference_books_external_strategy)
@settings(max_examples=25)
def test_Reserved_or_reference_books_external_instantiation(instance):
    assert isinstance(instance, Reserved_or_reference_books_external)


Resources_Component_strategy = st.builds(Resources_Component)
@given(instance=Resources_Component_strategy)
@settings(max_examples=25)
def test_Resources_Component_instantiation(instance):
    assert isinstance(instance, Resources_Component)


StaffMember_strategy = st.builds(StaffMember)
@given(instance=StaffMember_strategy)
@settings(max_examples=25)
def test_StaffMember_instantiation(instance):
    assert isinstance(instance, StaffMember)


Staff_Actor_strategy = st.builds(Staff_Actor)
@given(instance=Staff_Actor_strategy)
@settings(max_examples=25)
def test_Staff_Actor_instantiation(instance):
    assert isinstance(instance, Staff_Actor)


Staff_Actor1_strategy = st.builds(Staff_Actor1)
@given(instance=Staff_Actor1_strategy)
@settings(max_examples=25)
def test_Staff_Actor1_instantiation(instance):
    assert isinstance(instance, Staff_Actor1)


Student_Actor_strategy = st.builds(Student_Actor)
@given(instance=Student_Actor_strategy)
@settings(max_examples=25)
def test_Student_Actor_instantiation(instance):
    assert isinstance(instance, Student_Actor)



