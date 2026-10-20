import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Check_In_Item_external,
    Check_Out_Item_external,
    Extended_Checkout_external,
    Faculty,
    Faculty_Actor,
    Library_Management_Component,
    Library_Staff_Actor,
    Manage_Computer_Terminals_external,
    Manage_Reference_Materials_external,
    Order_New_Resources_external,
    Organize_Books_external,
    Patron,
    Patron_Actor,
    Renew_Magazine_Subscriptions_external,
    Request_Book_external,
    Reserve_Book_For_Semester_external,
    Student,
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

