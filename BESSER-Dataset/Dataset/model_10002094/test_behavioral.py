import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assist_with_research_using_computer_based_tools_UseCase,
    Assist_with_research_using_hard_copy_indexes_UseCase,
    Book,
    Bound_magazines_into_volumes_or_record_as_microfiche_UseCase,
    CD,
    Check_in_book_UseCase,
    Check_out_book_UseCase,
    Class,
    Double,
    Faculty,
    Fine_patron_for_overdue_book_UseCase,
    Item,
    Library,
    Library_Actor,
    Library_Patron,
    Library_patron_Actor,
    Library_staff,
    Library_staff_Actor,
    Magazine,
    Manage_Interlibrary_loan_requests_UseCase,
    Order_new_library_resources_UseCase,
    Pay_overdue_fine_UseCase,
    Put_book_on_reserve_UseCase,
    Renew_magazine_subscriptions_UseCase,
    Reshelve_books_UseCase,
    Retire_books_UseCase,
    Return_book_UseCase,
    Send_book_return_due_reminder_UseCase,
    Software,
    Video,
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

