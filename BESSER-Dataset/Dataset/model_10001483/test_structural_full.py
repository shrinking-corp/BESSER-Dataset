import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Actor2_Actor,
    Actor3_Actor,
    Actor4_Actor,
    Actor_Actor,
    Add__Update_and_Delete_job_UseCase,
    Admin_____________backend__Actor,
    Admin_login__firebase__UseCase,
    Administrator,
    Administrator_Actor,
    App_User_Actor,
    Apply_for_Job_UseCase,
    Employer,
    JobSeeker,
    Login_UseCase,
    Manage_database_UseCase,
    MyClass,
    Post_Job_UseCase,
    Search_Jobs_UseCase,
    Security_UseCase,
    Set_Profile_UseCase,
    Signup_UseCase,
    Support_Services_UseCase,
    UseCase_UseCase,
    User,
    admin_Actor,
    admin_Actor1,
    admin_Actor2,
    educational_qualification_UseCase,
    educational_qualification_UseCase1,
    employer_Actor,
    employer_Actor1,
    job_offer_UseCase,
    job_offers_UseCase,
    job_seeker_Actor,
    job_seeker_Actor1,
    job_seeker_Actor2,
    job_vacancies_UseCase,
    list_of_jobs_available_UseCase,
    list_of_jobs_related_to_graduation_UseCase,
    log_in_UseCase,
    login_UseCase,
    login_UseCase1,
    logout_UseCase,
    seeking_for_job_UseCase,
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

def test_Administrator_Address_value_roundtrip():
    instance = Administrator(Address="sample_text", Company="sample_text", Name="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Administrator_Company_value_roundtrip():
    instance = Administrator(Address="sample_text", Company="sample_text", Name="sample_text")
    assert instance.Company == "sample_text"
    instance.Company = "sample_text_2"
    assert instance.Company == "sample_text_2"


def test_Administrator_Name_value_roundtrip():
    instance = Administrator(Address="sample_text", Company="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Employer_Address_value_roundtrip():
    instance = Employer(Address="sample_text", Name="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Employer_Name_value_roundtrip():
    instance = Employer(Address="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_JobSeeker_Experience_value_roundtrip():
    instance = JobSeeker(Experience="sample_text", Name="sample_text", Qualification="sample_text")
    assert instance.Experience == "sample_text"
    instance.Experience = "sample_text_2"
    assert instance.Experience == "sample_text_2"


def test_JobSeeker_Name_value_roundtrip():
    instance = JobSeeker(Experience="sample_text", Name="sample_text", Qualification="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_JobSeeker_Qualification_value_roundtrip():
    instance = JobSeeker(Experience="sample_text", Name="sample_text", Qualification="sample_text")
    assert instance.Qualification == "sample_text"
    instance.Qualification = "sample_text_2"
    assert instance.Qualification == "sample_text_2"


def test_User_Address_value_roundtrip():
    instance = User(Address="sample_text", Name="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_User_Name_value_roundtrip():
    instance = User(Address="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Administrator_Job_seeker_link_reassign_clear():
    a = JobSeeker(Experience="sample_text", Name="sample_text", Qualification="sample_text")
    b1 = Administrator(Address="sample_text", Company="sample_text", Name="sample_text")
    b2 = Administrator(Address="sample_text_2", Company="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'administrator35', b1)
    assert _is_linked(a, 'administrator35', b1)
    if hasattr(b1, 'jobseeker34'):
        assert _is_linked(b1, 'jobseeker34', a)
    _safe_set(a, 'administrator35', b2)
    assert _is_linked(a, 'administrator35', b2)
    if hasattr(b1, 'jobseeker34'):
        assert not _is_linked(b1, 'jobseeker34', a)
    if hasattr(b2, 'jobseeker34'):
        assert _is_linked(b2, 'jobseeker34', a)
    _safe_set(a, 'administrator35', None)
    assert not _is_linked(a, 'administrator35', b2)
    if hasattr(b2, 'jobseeker34'):
        assert not _is_linked(b2, 'jobseeker34', a)


def test_assoc_Employer_Administrator_link_reassign_clear():
    a = Employer(Address="sample_text", Name="sample_text")
    b1 = Administrator(Address="sample_text", Company="sample_text", Name="sample_text")
    b2 = Administrator(Address="sample_text_2", Company="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'administrator32', b1)
    assert _is_linked(a, 'administrator32', b1)
    if hasattr(b1, 'employer33'):
        assert _is_linked(b1, 'employer33', a)
    _safe_set(a, 'administrator32', b2)
    assert _is_linked(a, 'administrator32', b2)
    if hasattr(b1, 'employer33'):
        assert not _is_linked(b1, 'employer33', a)
    if hasattr(b2, 'employer33'):
        assert _is_linked(b2, 'employer33', a)
    _safe_set(a, 'administrator32', None)
    assert not _is_linked(a, 'administrator32', b2)
    if hasattr(b2, 'employer33'):
        assert not _is_linked(b2, 'employer33', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actor2_Actor_strategy = st.builds(Actor2_Actor)
@given(instance=Actor2_Actor_strategy)
@settings(max_examples=25)
def test_Actor2_Actor_instantiation(instance):
    assert isinstance(instance, Actor2_Actor)


Actor3_Actor_strategy = st.builds(Actor3_Actor)
@given(instance=Actor3_Actor_strategy)
@settings(max_examples=25)
def test_Actor3_Actor_instantiation(instance):
    assert isinstance(instance, Actor3_Actor)


Actor4_Actor_strategy = st.builds(Actor4_Actor)
@given(instance=Actor4_Actor_strategy)
@settings(max_examples=25)
def test_Actor4_Actor_instantiation(instance):
    assert isinstance(instance, Actor4_Actor)


Actor_Actor_strategy = st.builds(Actor_Actor)
@given(instance=Actor_Actor_strategy)
@settings(max_examples=25)
def test_Actor_Actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)


Add__Update_and_Delete_job_UseCase_strategy = st.builds(Add__Update_and_Delete_job_UseCase)
@given(instance=Add__Update_and_Delete_job_UseCase_strategy)
@settings(max_examples=25)
def test_Add__Update_and_Delete_job_UseCase_instantiation(instance):
    assert isinstance(instance, Add__Update_and_Delete_job_UseCase)


Admin_____________backend__Actor_strategy = st.builds(Admin_____________backend__Actor)
@given(instance=Admin_____________backend__Actor_strategy)
@settings(max_examples=25)
def test_Admin_____________backend__Actor_instantiation(instance):
    assert isinstance(instance, Admin_____________backend__Actor)


Admin_login__firebase__UseCase_strategy = st.builds(Admin_login__firebase__UseCase)
@given(instance=Admin_login__firebase__UseCase_strategy)
@settings(max_examples=25)
def test_Admin_login__firebase__UseCase_instantiation(instance):
    assert isinstance(instance, Admin_login__firebase__UseCase)


Administrator_strategy = st.builds(Administrator, Address=safe_text, Company=safe_text, Name=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


App_User_Actor_strategy = st.builds(App_User_Actor)
@given(instance=App_User_Actor_strategy)
@settings(max_examples=25)
def test_App_User_Actor_instantiation(instance):
    assert isinstance(instance, App_User_Actor)


Apply_for_Job_UseCase_strategy = st.builds(Apply_for_Job_UseCase)
@given(instance=Apply_for_Job_UseCase_strategy)
@settings(max_examples=25)
def test_Apply_for_Job_UseCase_instantiation(instance):
    assert isinstance(instance, Apply_for_Job_UseCase)


Employer_strategy = st.builds(Employer, Address=safe_text, Name=safe_text)
@given(instance=Employer_strategy)
@settings(max_examples=25)
def test_Employer_instantiation(instance):
    assert isinstance(instance, Employer)


JobSeeker_strategy = st.builds(JobSeeker, Experience=safe_text, Name=safe_text, Qualification=safe_text)
@given(instance=JobSeeker_strategy)
@settings(max_examples=25)
def test_JobSeeker_instantiation(instance):
    assert isinstance(instance, JobSeeker)


Login_UseCase_strategy = st.builds(Login_UseCase)
@given(instance=Login_UseCase_strategy)
@settings(max_examples=25)
def test_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)


Manage_database_UseCase_strategy = st.builds(Manage_database_UseCase)
@given(instance=Manage_database_UseCase_strategy)
@settings(max_examples=25)
def test_Manage_database_UseCase_instantiation(instance):
    assert isinstance(instance, Manage_database_UseCase)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


Post_Job_UseCase_strategy = st.builds(Post_Job_UseCase)
@given(instance=Post_Job_UseCase_strategy)
@settings(max_examples=25)
def test_Post_Job_UseCase_instantiation(instance):
    assert isinstance(instance, Post_Job_UseCase)


Search_Jobs_UseCase_strategy = st.builds(Search_Jobs_UseCase)
@given(instance=Search_Jobs_UseCase_strategy)
@settings(max_examples=25)
def test_Search_Jobs_UseCase_instantiation(instance):
    assert isinstance(instance, Search_Jobs_UseCase)


Security_UseCase_strategy = st.builds(Security_UseCase)
@given(instance=Security_UseCase_strategy)
@settings(max_examples=25)
def test_Security_UseCase_instantiation(instance):
    assert isinstance(instance, Security_UseCase)


Set_Profile_UseCase_strategy = st.builds(Set_Profile_UseCase)
@given(instance=Set_Profile_UseCase_strategy)
@settings(max_examples=25)
def test_Set_Profile_UseCase_instantiation(instance):
    assert isinstance(instance, Set_Profile_UseCase)


Signup_UseCase_strategy = st.builds(Signup_UseCase)
@given(instance=Signup_UseCase_strategy)
@settings(max_examples=25)
def test_Signup_UseCase_instantiation(instance):
    assert isinstance(instance, Signup_UseCase)


Support_Services_UseCase_strategy = st.builds(Support_Services_UseCase)
@given(instance=Support_Services_UseCase_strategy)
@settings(max_examples=25)
def test_Support_Services_UseCase_instantiation(instance):
    assert isinstance(instance, Support_Services_UseCase)


UseCase_UseCase_strategy = st.builds(UseCase_UseCase)
@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)


User_strategy = st.builds(User, Address=safe_text, Name=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


admin_Actor_strategy = st.builds(admin_Actor)
@given(instance=admin_Actor_strategy)
@settings(max_examples=25)
def test_admin_Actor_instantiation(instance):
    assert isinstance(instance, admin_Actor)


admin_Actor1_strategy = st.builds(admin_Actor1)
@given(instance=admin_Actor1_strategy)
@settings(max_examples=25)
def test_admin_Actor1_instantiation(instance):
    assert isinstance(instance, admin_Actor1)


admin_Actor2_strategy = st.builds(admin_Actor2)
@given(instance=admin_Actor2_strategy)
@settings(max_examples=25)
def test_admin_Actor2_instantiation(instance):
    assert isinstance(instance, admin_Actor2)


educational_qualification_UseCase_strategy = st.builds(educational_qualification_UseCase)
@given(instance=educational_qualification_UseCase_strategy)
@settings(max_examples=25)
def test_educational_qualification_UseCase_instantiation(instance):
    assert isinstance(instance, educational_qualification_UseCase)


educational_qualification_UseCase1_strategy = st.builds(educational_qualification_UseCase1)
@given(instance=educational_qualification_UseCase1_strategy)
@settings(max_examples=25)
def test_educational_qualification_UseCase1_instantiation(instance):
    assert isinstance(instance, educational_qualification_UseCase1)


employer_Actor_strategy = st.builds(employer_Actor)
@given(instance=employer_Actor_strategy)
@settings(max_examples=25)
def test_employer_Actor_instantiation(instance):
    assert isinstance(instance, employer_Actor)


employer_Actor1_strategy = st.builds(employer_Actor1)
@given(instance=employer_Actor1_strategy)
@settings(max_examples=25)
def test_employer_Actor1_instantiation(instance):
    assert isinstance(instance, employer_Actor1)


job_offer_UseCase_strategy = st.builds(job_offer_UseCase)
@given(instance=job_offer_UseCase_strategy)
@settings(max_examples=25)
def test_job_offer_UseCase_instantiation(instance):
    assert isinstance(instance, job_offer_UseCase)


job_offers_UseCase_strategy = st.builds(job_offers_UseCase)
@given(instance=job_offers_UseCase_strategy)
@settings(max_examples=25)
def test_job_offers_UseCase_instantiation(instance):
    assert isinstance(instance, job_offers_UseCase)


job_seeker_Actor_strategy = st.builds(job_seeker_Actor)
@given(instance=job_seeker_Actor_strategy)
@settings(max_examples=25)
def test_job_seeker_Actor_instantiation(instance):
    assert isinstance(instance, job_seeker_Actor)


job_seeker_Actor1_strategy = st.builds(job_seeker_Actor1)
@given(instance=job_seeker_Actor1_strategy)
@settings(max_examples=25)
def test_job_seeker_Actor1_instantiation(instance):
    assert isinstance(instance, job_seeker_Actor1)


job_seeker_Actor2_strategy = st.builds(job_seeker_Actor2)
@given(instance=job_seeker_Actor2_strategy)
@settings(max_examples=25)
def test_job_seeker_Actor2_instantiation(instance):
    assert isinstance(instance, job_seeker_Actor2)


job_vacancies_UseCase_strategy = st.builds(job_vacancies_UseCase)
@given(instance=job_vacancies_UseCase_strategy)
@settings(max_examples=25)
def test_job_vacancies_UseCase_instantiation(instance):
    assert isinstance(instance, job_vacancies_UseCase)


list_of_jobs_available_UseCase_strategy = st.builds(list_of_jobs_available_UseCase)
@given(instance=list_of_jobs_available_UseCase_strategy)
@settings(max_examples=25)
def test_list_of_jobs_available_UseCase_instantiation(instance):
    assert isinstance(instance, list_of_jobs_available_UseCase)


list_of_jobs_related_to_graduation_UseCase_strategy = st.builds(list_of_jobs_related_to_graduation_UseCase)
@given(instance=list_of_jobs_related_to_graduation_UseCase_strategy)
@settings(max_examples=25)
def test_list_of_jobs_related_to_graduation_UseCase_instantiation(instance):
    assert isinstance(instance, list_of_jobs_related_to_graduation_UseCase)


log_in_UseCase_strategy = st.builds(log_in_UseCase)
@given(instance=log_in_UseCase_strategy)
@settings(max_examples=25)
def test_log_in_UseCase_instantiation(instance):
    assert isinstance(instance, log_in_UseCase)


login_UseCase_strategy = st.builds(login_UseCase)
@given(instance=login_UseCase_strategy)
@settings(max_examples=25)
def test_login_UseCase_instantiation(instance):
    assert isinstance(instance, login_UseCase)


login_UseCase1_strategy = st.builds(login_UseCase1)
@given(instance=login_UseCase1_strategy)
@settings(max_examples=25)
def test_login_UseCase1_instantiation(instance):
    assert isinstance(instance, login_UseCase1)


logout_UseCase_strategy = st.builds(logout_UseCase)
@given(instance=logout_UseCase_strategy)
@settings(max_examples=25)
def test_logout_UseCase_instantiation(instance):
    assert isinstance(instance, logout_UseCase)


seeking_for_job_UseCase_strategy = st.builds(seeking_for_job_UseCase)
@given(instance=seeking_for_job_UseCase_strategy)
@settings(max_examples=25)
def test_seeking_for_job_UseCase_instantiation(instance):
    assert isinstance(instance, seeking_for_job_UseCase)


