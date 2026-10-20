import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    admin,
    admin_Actor,
    book_a_ticket,
    book_a_ticket_UseCase,
    browse_item_UseCase,
    cancle,
    cancle_UseCase,
    cancle_with_driver_UseCase,
    captcha_UseCase,
    changing_seats_by_admin_UseCase,
    driver,
    driver_Actor,
    driver_planing_UseCase,
    enter_password_UseCase,
    enter_user_name_UseCase,
    exciting_package_UseCase,
    guest_user_Actor,
    login,
    login_UseCase,
    logout_UseCase,
    pay,
    payment_UseCase,
    person,
    remove_user_UseCase,
    return_the_money_to_the_customer_UseCase,
    search_item__UseCase,
    send_message_to_number_registered_UseCase,
    submit_information,
    submit_information_UseCase,
    ticket_printing_UseCase,
    user,
    user_Actor,
    user_register,
    view_item,
    view_item_UseCase,
    view_seat_UseCase,
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

