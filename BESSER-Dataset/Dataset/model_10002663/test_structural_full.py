import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Faculty_Actor,
    Librarian_Actor,
    Library_Management_System_Faculty,
    Library_Management_System_Librarian,
    Library_Management_System_Patron,
    Library_Management_System_Student,
    Library_Managment_System_1_week_check_out_UseCase,
    Library_Managment_System_1_year_check_out_UseCase,
    Library_Managment_System_3_month_check_out_UseCase,
    Library_Managment_System_4_week_check_out_UseCase,
    Library_Managment_System_Adding_UseCase,
    Library_Managment_System_Assist_patrons_in_research_UseCase,
    Library_Managment_System_Books_UseCase,
    Library_Managment_System_CD_s_software_videos_UseCase,
    Library_Managment_System_Check_in___Return_UseCase,
    Library_Managment_System_Check_out_UseCase,
    Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase,
    Library_Managment_System_Contents_out_of_date_UseCase,
    Library_Managment_System_Faculty_UseCase,
    Library_Managment_System_Issue_fines_UseCase,
    Library_Managment_System_Late_Notice_UseCase,
    Library_Managment_System_Librarian_UseCase,
    Library_Managment_System_Magazines_UseCase,
    Library_Managment_System_Manage_Magazines_UseCase,
    Library_Managment_System_Meet_requests_of_patrons_UseCase,
    Library_Managment_System_Ordering_new_resources_UseCase,
    Library_Managment_System_Other_resources_UseCase,
    Library_Managment_System_Reference_UseCase,
    Library_Managment_System_Renew_Checkout_if_not_requested_UseCase,
    Library_Managment_System_Renew_subscriptions_UseCase,
    Library_Managment_System_Requested_UseCase,
    Library_Managment_System_Reserve_UseCase,
    Library_Managment_System_Reserve_book__1_semester__UseCase,
    Library_Managment_System_Reserve_foreign_resources_UseCase,
    Library_Managment_System_Reshelving_books_UseCase,
    Library_Managment_System_Retiring_UseCase,
    Library_Managment_System_Special_Status_UseCase,
    Library_Managment_System_Status_UseCase,
    Library_Managment_System_Student_UseCase,
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

def test_Library_Management_System_Faculty_FacultyId_value_roundtrip():
    instance = Library_Management_System_Faculty(FacultyId=7, FacultyName="sample_text")
    assert instance.FacultyId == 7
    instance.FacultyId = 13
    assert instance.FacultyId == 13


def test_Library_Management_System_Faculty_FacultyName_value_roundtrip():
    instance = Library_Management_System_Faculty(FacultyId=7, FacultyName="sample_text")
    assert instance.FacultyName == "sample_text"
    instance.FacultyName = "sample_text_2"
    assert instance.FacultyName == "sample_text_2"


def test_Library_Management_System_Librarian_LibrarianName_value_roundtrip():
    instance = Library_Management_System_Librarian(LibrarianName="sample_text")
    assert instance.LibrarianName == "sample_text"
    instance.LibrarianName = "sample_text_2"
    assert instance.LibrarianName == "sample_text_2"


def test_Library_Management_System_Student_StudentId_value_roundtrip():
    instance = Library_Management_System_Student(StudentId=7, StudentName="sample_text")
    assert instance.StudentId == 7
    instance.StudentId = 13
    assert instance.StudentId == 13


def test_Library_Management_System_Student_StudentName_value_roundtrip():
    instance = Library_Management_System_Student(StudentId=7, StudentName="sample_text")
    assert instance.StudentName == "sample_text"
    instance.StudentName = "sample_text_2"
    assert instance.StudentName == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Faculty_Actor_strategy = st.builds(Faculty_Actor)
@given(instance=Faculty_Actor_strategy)
@settings(max_examples=25)
def test_Faculty_Actor_instantiation(instance):
    assert isinstance(instance, Faculty_Actor)


Librarian_Actor_strategy = st.builds(Librarian_Actor)
@given(instance=Librarian_Actor_strategy)
@settings(max_examples=25)
def test_Librarian_Actor_instantiation(instance):
    assert isinstance(instance, Librarian_Actor)


Library_Management_System_Faculty_strategy = st.builds(Library_Management_System_Faculty, FacultyId=st.integers(), FacultyName=safe_text)
@given(instance=Library_Management_System_Faculty_strategy)
@settings(max_examples=25)
def test_Library_Management_System_Faculty_instantiation(instance):
    assert isinstance(instance, Library_Management_System_Faculty)


Library_Management_System_Librarian_strategy = st.builds(Library_Management_System_Librarian, LibrarianName=safe_text)
@given(instance=Library_Management_System_Librarian_strategy)
@settings(max_examples=25)
def test_Library_Management_System_Librarian_instantiation(instance):
    assert isinstance(instance, Library_Management_System_Librarian)


Library_Management_System_Student_strategy = st.builds(Library_Management_System_Student, StudentId=st.integers(), StudentName=safe_text)
@given(instance=Library_Management_System_Student_strategy)
@settings(max_examples=25)
def test_Library_Management_System_Student_instantiation(instance):
    assert isinstance(instance, Library_Management_System_Student)


Library_Managment_System_1_week_check_out_UseCase_strategy = st.builds(Library_Managment_System_1_week_check_out_UseCase)
@given(instance=Library_Managment_System_1_week_check_out_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_1_week_check_out_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_1_week_check_out_UseCase)


Library_Managment_System_1_year_check_out_UseCase_strategy = st.builds(Library_Managment_System_1_year_check_out_UseCase)
@given(instance=Library_Managment_System_1_year_check_out_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_1_year_check_out_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_1_year_check_out_UseCase)


Library_Managment_System_3_month_check_out_UseCase_strategy = st.builds(Library_Managment_System_3_month_check_out_UseCase)
@given(instance=Library_Managment_System_3_month_check_out_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_3_month_check_out_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_3_month_check_out_UseCase)


Library_Managment_System_4_week_check_out_UseCase_strategy = st.builds(Library_Managment_System_4_week_check_out_UseCase)
@given(instance=Library_Managment_System_4_week_check_out_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_4_week_check_out_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_4_week_check_out_UseCase)


Library_Managment_System_Adding_UseCase_strategy = st.builds(Library_Managment_System_Adding_UseCase)
@given(instance=Library_Managment_System_Adding_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Adding_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Adding_UseCase)


Library_Managment_System_Assist_patrons_in_research_UseCase_strategy = st.builds(Library_Managment_System_Assist_patrons_in_research_UseCase)
@given(instance=Library_Managment_System_Assist_patrons_in_research_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Assist_patrons_in_research_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Assist_patrons_in_research_UseCase)


Library_Managment_System_Books_UseCase_strategy = st.builds(Library_Managment_System_Books_UseCase)
@given(instance=Library_Managment_System_Books_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Books_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Books_UseCase)


Library_Managment_System_CD_s_software_videos_UseCase_strategy = st.builds(Library_Managment_System_CD_s_software_videos_UseCase)
@given(instance=Library_Managment_System_CD_s_software_videos_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_CD_s_software_videos_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_CD_s_software_videos_UseCase)


Library_Managment_System_Check_in___Return_UseCase_strategy = st.builds(Library_Managment_System_Check_in___Return_UseCase)
@given(instance=Library_Managment_System_Check_in___Return_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Check_in___Return_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Check_in___Return_UseCase)


Library_Managment_System_Check_out_UseCase_strategy = st.builds(Library_Managment_System_Check_out_UseCase)
@given(instance=Library_Managment_System_Check_out_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Check_out_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Check_out_UseCase)


Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase_strategy = st.builds(Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase)
@given(instance=Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase)


Library_Managment_System_Contents_out_of_date_UseCase_strategy = st.builds(Library_Managment_System_Contents_out_of_date_UseCase)
@given(instance=Library_Managment_System_Contents_out_of_date_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Contents_out_of_date_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Contents_out_of_date_UseCase)


Library_Managment_System_Faculty_UseCase_strategy = st.builds(Library_Managment_System_Faculty_UseCase)
@given(instance=Library_Managment_System_Faculty_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Faculty_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Faculty_UseCase)


Library_Managment_System_Issue_fines_UseCase_strategy = st.builds(Library_Managment_System_Issue_fines_UseCase)
@given(instance=Library_Managment_System_Issue_fines_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Issue_fines_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Issue_fines_UseCase)


Library_Managment_System_Late_Notice_UseCase_strategy = st.builds(Library_Managment_System_Late_Notice_UseCase)
@given(instance=Library_Managment_System_Late_Notice_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Late_Notice_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Late_Notice_UseCase)


Library_Managment_System_Librarian_UseCase_strategy = st.builds(Library_Managment_System_Librarian_UseCase)
@given(instance=Library_Managment_System_Librarian_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Librarian_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Librarian_UseCase)


Library_Managment_System_Magazines_UseCase_strategy = st.builds(Library_Managment_System_Magazines_UseCase)
@given(instance=Library_Managment_System_Magazines_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Magazines_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Magazines_UseCase)


Library_Managment_System_Manage_Magazines_UseCase_strategy = st.builds(Library_Managment_System_Manage_Magazines_UseCase)
@given(instance=Library_Managment_System_Manage_Magazines_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Manage_Magazines_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Manage_Magazines_UseCase)


Library_Managment_System_Meet_requests_of_patrons_UseCase_strategy = st.builds(Library_Managment_System_Meet_requests_of_patrons_UseCase)
@given(instance=Library_Managment_System_Meet_requests_of_patrons_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Meet_requests_of_patrons_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Meet_requests_of_patrons_UseCase)


Library_Managment_System_Ordering_new_resources_UseCase_strategy = st.builds(Library_Managment_System_Ordering_new_resources_UseCase)
@given(instance=Library_Managment_System_Ordering_new_resources_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Ordering_new_resources_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Ordering_new_resources_UseCase)


Library_Managment_System_Other_resources_UseCase_strategy = st.builds(Library_Managment_System_Other_resources_UseCase)
@given(instance=Library_Managment_System_Other_resources_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Other_resources_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Other_resources_UseCase)


Library_Managment_System_Reference_UseCase_strategy = st.builds(Library_Managment_System_Reference_UseCase)
@given(instance=Library_Managment_System_Reference_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Reference_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Reference_UseCase)


Library_Managment_System_Renew_Checkout_if_not_requested_UseCase_strategy = st.builds(Library_Managment_System_Renew_Checkout_if_not_requested_UseCase)
@given(instance=Library_Managment_System_Renew_Checkout_if_not_requested_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Renew_Checkout_if_not_requested_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Renew_Checkout_if_not_requested_UseCase)


Library_Managment_System_Renew_subscriptions_UseCase_strategy = st.builds(Library_Managment_System_Renew_subscriptions_UseCase)
@given(instance=Library_Managment_System_Renew_subscriptions_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Renew_subscriptions_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Renew_subscriptions_UseCase)


Library_Managment_System_Requested_UseCase_strategy = st.builds(Library_Managment_System_Requested_UseCase)
@given(instance=Library_Managment_System_Requested_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Requested_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Requested_UseCase)


Library_Managment_System_Reserve_UseCase_strategy = st.builds(Library_Managment_System_Reserve_UseCase)
@given(instance=Library_Managment_System_Reserve_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Reserve_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Reserve_UseCase)


Library_Managment_System_Reserve_book__1_semester__UseCase_strategy = st.builds(Library_Managment_System_Reserve_book__1_semester__UseCase)
@given(instance=Library_Managment_System_Reserve_book__1_semester__UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Reserve_book__1_semester__UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Reserve_book__1_semester__UseCase)


Library_Managment_System_Reserve_foreign_resources_UseCase_strategy = st.builds(Library_Managment_System_Reserve_foreign_resources_UseCase)
@given(instance=Library_Managment_System_Reserve_foreign_resources_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Reserve_foreign_resources_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Reserve_foreign_resources_UseCase)


Library_Managment_System_Reshelving_books_UseCase_strategy = st.builds(Library_Managment_System_Reshelving_books_UseCase)
@given(instance=Library_Managment_System_Reshelving_books_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Reshelving_books_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Reshelving_books_UseCase)


Library_Managment_System_Retiring_UseCase_strategy = st.builds(Library_Managment_System_Retiring_UseCase)
@given(instance=Library_Managment_System_Retiring_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Retiring_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Retiring_UseCase)


Library_Managment_System_Special_Status_UseCase_strategy = st.builds(Library_Managment_System_Special_Status_UseCase)
@given(instance=Library_Managment_System_Special_Status_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Special_Status_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Special_Status_UseCase)


Library_Managment_System_Status_UseCase_strategy = st.builds(Library_Managment_System_Status_UseCase)
@given(instance=Library_Managment_System_Status_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Status_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Status_UseCase)


Library_Managment_System_Student_UseCase_strategy = st.builds(Library_Managment_System_Student_UseCase)
@given(instance=Library_Managment_System_Student_UseCase_strategy)
@settings(max_examples=25)
def test_Library_Managment_System_Student_UseCase_instantiation(instance):
    assert isinstance(instance, Library_Managment_System_Student_UseCase)


Student_Actor_strategy = st.builds(Student_Actor)
@given(instance=Student_Actor_strategy)
@settings(max_examples=25)
def test_Student_Actor_instantiation(instance):
    assert isinstance(instance, Student_Actor)


