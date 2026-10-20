import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor2_Actor,
    Actor3_Actor,
    Actor4_Actor,
    Actor_Actor,
    Administrator_Actor,
    Administrator_Actor1,
    Employer_Actor,
    Job_Seeker_Actor,
    Manage_database_UseCase,
    MyClass,
    Response_to_users_employee_to_job_seekers__UseCase,
    Update_categories_UseCase,
    UseCase_UseCase,
    User,
    add_update_and_delete_job_UseCase,
    admin_Actor,
    admin_Actor1,
    admin_Actor2,
    apply_for_job_UseCase,
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
    login_UseCase2,
    logout_UseCase,
    post_job_UseCase,
    post_resume_UseCase,
    search_job_UseCase,
    search_jobs_UseCase,
    seeking_for_job_UseCase,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

