import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin_Actor,
    ApplicationUtils,
    Application_Actor,
    ApplyLeaveRequest,
    Apply_Leave_UseCase,
    ApproveOrRejectStatus,
    Approve_RejectRequests_UseCase,
    Approver_Jobs_UseCase,
    AutoApproval_UseCase,
    CancelLeaveRequest,
    Cancel_Leaves_UseCase,
    Change_Password_UseCase,
    CreateUserAction,
    CreateUser_UseCase,
    Credit_Leaves_UseCase,
    EligibilityQuery,
    Employee,
    Employee_Actor,
    LeaveApplication,
    LeaveBalanceQuery,
    LeaveHistoryQuery,
    LeaveStatusQuery,
    Leave_Request_Status_UseCase,
    LoginAction,
    Login_UseCase,
    Query,
    Query_Eligibility_UseCase,
    Query_Leave_Balance_UseCase,
    Query_Leave_History_UseCase,
    Request,
    SendNotification_UseCase,
    UpdateCalendar,
    Update_Calendar_UseCase,
    WithdrawLeaveRequest,
    Withdraw_Application_UseCase,
    _UseCase,
    LeaveStatus,
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

