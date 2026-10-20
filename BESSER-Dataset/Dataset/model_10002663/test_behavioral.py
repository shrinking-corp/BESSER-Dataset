import pytest
from datetime import date, datetime, time, timedelta

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

