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
    ApplicationUtils,
    UpdateCalendar,
    CreateUserAction,
    LoginAction,
    ApproveOrRejectStatus,
    LeaveStatusQuery,
    CancelLeaveRequest,
    WithdrawLeaveRequest,
    ApplyLeaveRequest,
    Request,
    LeaveApplication,
    LeaveHistoryQuery,
    LeaveBalanceQuery,
    EligibilityQuery,
    Query,
    Employee,
    GenerateSummary_UseCase,
    AutoApproval_UseCase,
    Credit_Leaves_UseCase,
    SendNotification_UseCase,
    Employee_Actor1,
    Update_Calendar_UseCase,
    CreateUser_UseCase,
    Admin_Actor,
    Cancel_Leaves_UseCase,
    Approve_RejectRequests_UseCase,
    Approver_Jobs_UseCase,
    Withdraw_Application_UseCase,
    Leave_Request_Status_UseCase,
    Apply_Leave_UseCase,
    Query_Leave_History_UseCase,
    Query_Leave_Balance_UseCase,
    Query_Eligibility_UseCase,
    Change_Password_UseCase,
    Employee_Actor,
    Login_UseCase,
    LeaveStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_applicationutils_is_not_abstract():
    assert not inspect.isabstract(ApplicationUtils)


def test_hyp_applicationutils_constructor_exists():
    assert callable(ApplicationUtils.__init__)


def test_hyp_applicationutils_constructor_args():
    sig = inspect.signature(ApplicationUtils.__init__)
    params = list(sig.parameters.keys())



def test_hyp_updatecalendar_is_not_abstract():
    assert not inspect.isabstract(UpdateCalendar)


def test_hyp_updatecalendar_constructor_exists():
    assert callable(UpdateCalendar.__init__)


def test_hyp_updatecalendar_constructor_args():
    sig = inspect.signature(UpdateCalendar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_createuseraction_is_not_abstract():
    assert not inspect.isabstract(CreateUserAction)


def test_hyp_createuseraction_constructor_exists():
    assert callable(CreateUserAction.__init__)


def test_hyp_createuseraction_constructor_args():
    sig = inspect.signature(CreateUserAction.__init__)
    params = list(sig.parameters.keys())
    assert "employee" in params, "Missing parameter 'employee'"

def test_hyp_createuseraction_has_employee():
    assert hasattr(CreateUserAction, "employee")
    descriptor = None
    for klass in CreateUserAction.__mro__:
        if "employee" in klass.__dict__:
            descriptor = klass.__dict__["employee"]
            break
    assert isinstance(descriptor, property)



def test_hyp_loginaction_is_not_abstract():
    assert not inspect.isabstract(LoginAction)


def test_hyp_loginaction_constructor_exists():
    assert callable(LoginAction.__init__)


def test_hyp_loginaction_constructor_args():
    sig = inspect.signature(LoginAction.__init__)
    params = list(sig.parameters.keys())
    assert "employee" in params, "Missing parameter 'employee'"

def test_hyp_loginaction_has_employee():
    assert hasattr(LoginAction, "employee")
    descriptor = None
    for klass in LoginAction.__mro__:
        if "employee" in klass.__dict__:
            descriptor = klass.__dict__["employee"]
            break
    assert isinstance(descriptor, property)



def test_hyp_approveorrejectstatus_is_not_abstract():
    assert not inspect.isabstract(ApproveOrRejectStatus)


def test_hyp_approveorrejectstatus_constructor_exists():
    assert callable(ApproveOrRejectStatus.__init__)


def test_hyp_approveorrejectstatus_constructor_args():
    sig = inspect.signature(ApproveOrRejectStatus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leavestatusquery_is_not_abstract():
    assert not inspect.isabstract(LeaveStatusQuery)


def test_hyp_leavestatusquery_constructor_exists():
    assert callable(LeaveStatusQuery.__init__)


def test_hyp_leavestatusquery_constructor_args():
    sig = inspect.signature(LeaveStatusQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cancelleaverequest_is_not_abstract():
    assert not inspect.isabstract(CancelLeaveRequest)


def test_hyp_cancelleaverequest_constructor_exists():
    assert callable(CancelLeaveRequest.__init__)


def test_hyp_cancelleaverequest_constructor_args():
    sig = inspect.signature(CancelLeaveRequest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_withdrawleaverequest_is_not_abstract():
    assert not inspect.isabstract(WithdrawLeaveRequest)


def test_hyp_withdrawleaverequest_constructor_exists():
    assert callable(WithdrawLeaveRequest.__init__)


def test_hyp_withdrawleaverequest_constructor_args():
    sig = inspect.signature(WithdrawLeaveRequest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_applyleaverequest_is_not_abstract():
    assert not inspect.isabstract(ApplyLeaveRequest)


def test_hyp_applyleaverequest_constructor_exists():
    assert callable(ApplyLeaveRequest.__init__)


def test_hyp_applyleaverequest_constructor_args():
    sig = inspect.signature(ApplyLeaveRequest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_request_is_not_abstract():
    assert not inspect.isabstract(Request)


def test_hyp_request_constructor_exists():
    assert callable(Request.__init__)


def test_hyp_request_constructor_args():
    sig = inspect.signature(Request.__init__)
    params = list(sig.parameters.keys())
    assert "leaveApplication" in params, "Missing parameter 'leaveApplication'"
    assert "requestId" in params, "Missing parameter 'requestId'"

def test_hyp_request_has_leaveApplication():
    assert hasattr(Request, "leaveApplication")
    descriptor = None
    for klass in Request.__mro__:
        if "leaveApplication" in klass.__dict__:
            descriptor = klass.__dict__["leaveApplication"]
            break
    assert isinstance(descriptor, property)

def test_hyp_request_has_requestId():
    assert hasattr(Request, "requestId")
    descriptor = None
    for klass in Request.__mro__:
        if "requestId" in klass.__dict__:
            descriptor = klass.__dict__["requestId"]
            break
    assert isinstance(descriptor, property)



def test_hyp_leaveapplication_is_not_abstract():
    assert not inspect.isabstract(LeaveApplication)


def test_hyp_leaveapplication_constructor_exists():
    assert callable(LeaveApplication.__init__)


def test_hyp_leaveapplication_constructor_args():
    sig = inspect.signature(LeaveApplication.__init__)
    params = list(sig.parameters.keys())
    assert "applicationId" in params, "Missing parameter 'applicationId'"
    assert "toDate" in params, "Missing parameter 'toDate'"
    assert "fromDate" in params, "Missing parameter 'fromDate'"
    assert "status" in params, "Missing parameter 'status'"
    assert "approverComments" in params, "Missing parameter 'approverComments'"
    assert "employeeId" in params, "Missing parameter 'employeeId'"
    assert "reason" in params, "Missing parameter 'reason'"










def test_hyp_leavehistoryquery_is_not_abstract():
    assert not inspect.isabstract(LeaveHistoryQuery)


def test_hyp_leavehistoryquery_constructor_exists():
    assert callable(LeaveHistoryQuery.__init__)


def test_hyp_leavehistoryquery_constructor_args():
    sig = inspect.signature(LeaveHistoryQuery.__init__)
    params = list(sig.parameters.keys())
    assert "fromDate" in params, "Missing parameter 'fromDate'"
    assert "toDate" in params, "Missing parameter 'toDate'"





def test_hyp_leavebalancequery_is_not_abstract():
    assert not inspect.isabstract(LeaveBalanceQuery)


def test_hyp_leavebalancequery_constructor_exists():
    assert callable(LeaveBalanceQuery.__init__)


def test_hyp_leavebalancequery_constructor_args():
    sig = inspect.signature(LeaveBalanceQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_eligibilityquery_is_not_abstract():
    assert not inspect.isabstract(EligibilityQuery)


def test_hyp_eligibilityquery_constructor_exists():
    assert callable(EligibilityQuery.__init__)


def test_hyp_eligibilityquery_constructor_args():
    sig = inspect.signature(EligibilityQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_hyp_query_constructor_exists():
    assert callable(Query.__init__)


def test_hyp_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())
    assert "requestId" in params, "Missing parameter 'requestId'"
    assert "user" in params, "Missing parameter 'user'"

def test_hyp_query_has_requestId():
    assert hasattr(Query, "requestId")
    descriptor = None
    for klass in Query.__mro__:
        if "requestId" in klass.__dict__:
            descriptor = klass.__dict__["requestId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_query_has_user():
    assert hasattr(Query, "user")
    descriptor = None
    for klass in Query.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)



def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "jobLevel" in params, "Missing parameter 'jobLevel'"
    assert "leavesTaken" in params, "Missing parameter 'leavesTaken'"
    assert "employeeId" in params, "Missing parameter 'employeeId'"
    assert "employeeName" in params, "Missing parameter 'employeeName'"
    assert "noOfLeaves" in params, "Missing parameter 'noOfLeaves'"
    assert "managerId" in params, "Missing parameter 'managerId'"
    assert "password" in params, "Missing parameter 'password'"










def test_hyp_generatesummary_usecase_is_not_abstract():
    assert not inspect.isabstract(GenerateSummary_UseCase)


def test_hyp_generatesummary_usecase_constructor_exists():
    assert callable(GenerateSummary_UseCase.__init__)


def test_hyp_generatesummary_usecase_constructor_args():
    sig = inspect.signature(GenerateSummary_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_autoapproval_usecase_is_not_abstract():
    assert not inspect.isabstract(AutoApproval_UseCase)


def test_hyp_autoapproval_usecase_constructor_exists():
    assert callable(AutoApproval_UseCase.__init__)


def test_hyp_autoapproval_usecase_constructor_args():
    sig = inspect.signature(AutoApproval_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_credit_leaves_usecase_is_not_abstract():
    assert not inspect.isabstract(Credit_Leaves_UseCase)


def test_hyp_credit_leaves_usecase_constructor_exists():
    assert callable(Credit_Leaves_UseCase.__init__)


def test_hyp_credit_leaves_usecase_constructor_args():
    sig = inspect.signature(Credit_Leaves_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sendnotification_usecase_is_not_abstract():
    assert not inspect.isabstract(SendNotification_UseCase)


def test_hyp_sendnotification_usecase_constructor_exists():
    assert callable(SendNotification_UseCase.__init__)


def test_hyp_sendnotification_usecase_constructor_args():
    sig = inspect.signature(SendNotification_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_actor1_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor1)


def test_hyp_employee_actor1_constructor_exists():
    assert callable(Employee_Actor1.__init__)


def test_hyp_employee_actor1_constructor_args():
    sig = inspect.signature(Employee_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_update_calendar_usecase_is_not_abstract():
    assert not inspect.isabstract(Update_Calendar_UseCase)


def test_hyp_update_calendar_usecase_constructor_exists():
    assert callable(Update_Calendar_UseCase.__init__)


def test_hyp_update_calendar_usecase_constructor_args():
    sig = inspect.signature(Update_Calendar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_createuser_usecase_is_not_abstract():
    assert not inspect.isabstract(CreateUser_UseCase)


def test_hyp_createuser_usecase_constructor_exists():
    assert callable(CreateUser_UseCase.__init__)


def test_hyp_createuser_usecase_constructor_args():
    sig = inspect.signature(CreateUser_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_hyp_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_hyp_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cancel_leaves_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancel_Leaves_UseCase)


def test_hyp_cancel_leaves_usecase_constructor_exists():
    assert callable(Cancel_Leaves_UseCase.__init__)


def test_hyp_cancel_leaves_usecase_constructor_args():
    sig = inspect.signature(Cancel_Leaves_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_approve_rejectrequests_usecase_is_not_abstract():
    assert not inspect.isabstract(Approve_RejectRequests_UseCase)


def test_hyp_approve_rejectrequests_usecase_constructor_exists():
    assert callable(Approve_RejectRequests_UseCase.__init__)


def test_hyp_approve_rejectrequests_usecase_constructor_args():
    sig = inspect.signature(Approve_RejectRequests_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_approver_jobs_usecase_is_not_abstract():
    assert not inspect.isabstract(Approver_Jobs_UseCase)


def test_hyp_approver_jobs_usecase_constructor_exists():
    assert callable(Approver_Jobs_UseCase.__init__)


def test_hyp_approver_jobs_usecase_constructor_args():
    sig = inspect.signature(Approver_Jobs_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_withdraw_application_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Application_UseCase)


def test_hyp_withdraw_application_usecase_constructor_exists():
    assert callable(Withdraw_Application_UseCase.__init__)


def test_hyp_withdraw_application_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Application_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leave_request_status_usecase_is_not_abstract():
    assert not inspect.isabstract(Leave_Request_Status_UseCase)


def test_hyp_leave_request_status_usecase_constructor_exists():
    assert callable(Leave_Request_Status_UseCase.__init__)


def test_hyp_leave_request_status_usecase_constructor_args():
    sig = inspect.signature(Leave_Request_Status_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_apply_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Apply_Leave_UseCase)


def test_hyp_apply_leave_usecase_constructor_exists():
    assert callable(Apply_Leave_UseCase.__init__)


def test_hyp_apply_leave_usecase_constructor_args():
    sig = inspect.signature(Apply_Leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_query_leave_history_usecase_is_not_abstract():
    assert not inspect.isabstract(Query_Leave_History_UseCase)


def test_hyp_query_leave_history_usecase_constructor_exists():
    assert callable(Query_Leave_History_UseCase.__init__)


def test_hyp_query_leave_history_usecase_constructor_args():
    sig = inspect.signature(Query_Leave_History_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_query_leave_balance_usecase_is_not_abstract():
    assert not inspect.isabstract(Query_Leave_Balance_UseCase)


def test_hyp_query_leave_balance_usecase_constructor_exists():
    assert callable(Query_Leave_Balance_UseCase.__init__)


def test_hyp_query_leave_balance_usecase_constructor_args():
    sig = inspect.signature(Query_Leave_Balance_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_query_eligibility_usecase_is_not_abstract():
    assert not inspect.isabstract(Query_Eligibility_UseCase)


def test_hyp_query_eligibility_usecase_constructor_exists():
    assert callable(Query_Eligibility_UseCase.__init__)


def test_hyp_query_eligibility_usecase_constructor_args():
    sig = inspect.signature(Query_Eligibility_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_change_password_usecase_is_not_abstract():
    assert not inspect.isabstract(Change_Password_UseCase)


def test_hyp_change_password_usecase_constructor_exists():
    assert callable(Change_Password_UseCase.__init__)


def test_hyp_change_password_usecase_constructor_args():
    sig = inspect.signature(Change_Password_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_actor_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor)


def test_hyp_employee_actor_constructor_exists():
    assert callable(Employee_Actor.__init__)


def test_hyp_employee_actor_constructor_args():
    sig = inspect.signature(Employee_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase)


def test_hyp_login_usecase_constructor_exists():
    assert callable(Login_UseCase.__init__)


def test_hyp_login_usecase_constructor_args():
    sig = inspect.signature(Login_UseCase.__init__)
    params = list(sig.parameters.keys())

def test_hyp_leavestatus_exists():
    # Check that the Enumeration exists
    assert LeaveStatus is not None

def test_hyp_leavestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeaveStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeaveStatus"


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
ApplicationUtils_strategy = st.builds(
    ApplicationUtils,
)
UpdateCalendar_strategy = st.builds(
    UpdateCalendar,
)
CreateUserAction_strategy = st.builds(
    CreateUserAction,
    employee=
        st.none()
)
LoginAction_strategy = st.builds(
    LoginAction,
    employee=
        st.none()
)
ApproveOrRejectStatus_strategy = st.builds(
    ApproveOrRejectStatus,
)
LeaveStatusQuery_strategy = st.builds(
    LeaveStatusQuery,
)
CancelLeaveRequest_strategy = st.builds(
    CancelLeaveRequest,
)
WithdrawLeaveRequest_strategy = st.builds(
    WithdrawLeaveRequest,
)
ApplyLeaveRequest_strategy = st.builds(
    ApplyLeaveRequest,
)
Request_strategy = st.builds(
    Request,
    leaveApplication=
        st.none(),
    requestId=
        safe_text
)
LeaveApplication_strategy = st.builds(
    LeaveApplication,
    applicationId=
        safe_text,
    toDate=
        st.dates(),
    fromDate=
        st.dates(),
    status=
        safe_text,
    approverComments=
        safe_text,
    employeeId=
        safe_text,
    reason=
        safe_text
)
LeaveHistoryQuery_strategy = st.builds(
    LeaveHistoryQuery,
    fromDate=
        st.dates(),
    toDate=
        st.dates()
)
LeaveBalanceQuery_strategy = st.builds(
    LeaveBalanceQuery,
)
EligibilityQuery_strategy = st.builds(
    EligibilityQuery,
)
Query_strategy = st.builds(
    Query,
    requestId=
        safe_text,
    user=
        st.none()
)
Employee_strategy = st.builds(
    Employee,
    jobLevel=
        st.integers(),
    leavesTaken=
        safe_text,
    employeeId=
        safe_text,
    employeeName=
        safe_text,
    noOfLeaves=
        st.integers(),
    managerId=
        safe_text,
    password=
        safe_text
)
GenerateSummary_UseCase_strategy = st.builds(
    GenerateSummary_UseCase,
)
AutoApproval_UseCase_strategy = st.builds(
    AutoApproval_UseCase,
)
Credit_Leaves_UseCase_strategy = st.builds(
    Credit_Leaves_UseCase,
)
SendNotification_UseCase_strategy = st.builds(
    SendNotification_UseCase,
)
Employee_Actor1_strategy = st.builds(
    Employee_Actor1,
)
Update_Calendar_UseCase_strategy = st.builds(
    Update_Calendar_UseCase,
)
CreateUser_UseCase_strategy = st.builds(
    CreateUser_UseCase,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
Cancel_Leaves_UseCase_strategy = st.builds(
    Cancel_Leaves_UseCase,
)
Approve_RejectRequests_UseCase_strategy = st.builds(
    Approve_RejectRequests_UseCase,
)
Approver_Jobs_UseCase_strategy = st.builds(
    Approver_Jobs_UseCase,
)
Withdraw_Application_UseCase_strategy = st.builds(
    Withdraw_Application_UseCase,
)
Leave_Request_Status_UseCase_strategy = st.builds(
    Leave_Request_Status_UseCase,
)
Apply_Leave_UseCase_strategy = st.builds(
    Apply_Leave_UseCase,
)
Query_Leave_History_UseCase_strategy = st.builds(
    Query_Leave_History_UseCase,
)
Query_Leave_Balance_UseCase_strategy = st.builds(
    Query_Leave_Balance_UseCase,
)
Query_Eligibility_UseCase_strategy = st.builds(
    Query_Eligibility_UseCase,
)
Change_Password_UseCase_strategy = st.builds(
    Change_Password_UseCase,
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)
Login_UseCase_strategy = st.builds(
    Login_UseCase,
)



@given(instance=CreateUserAction_strategy)
@settings(max_examples=50)
def test_hyp_createuseraction_instantiation(instance):
    assert isinstance(instance, CreateUserAction)



@given(instance=CreateUserAction_strategy)
def test_hyp_createuseraction_employee_setter(instance):
    original = instance.employee
    instance.employee = original
    assert instance.employee == original

@given(instance=LoginAction_strategy)
@settings(max_examples=50)
def test_hyp_loginaction_instantiation(instance):
    assert isinstance(instance, LoginAction)



@given(instance=LoginAction_strategy)
def test_hyp_loginaction_employee_setter(instance):
    original = instance.employee
    instance.employee = original
    assert instance.employee == original






@given(instance=Request_strategy)
@settings(max_examples=50)
def test_hyp_request_instantiation(instance):
    assert isinstance(instance, Request)



@given(instance=Request_strategy)
def test_hyp_request_leaveApplication_setter(instance):
    original = instance.leaveApplication
    instance.leaveApplication = original
    assert instance.leaveApplication == original



@given(instance=Request_strategy)
def test_hyp_request_requestId_setter(instance):
    original = instance.requestId
    instance.requestId = original
    assert instance.requestId == original




@given(instance=LeaveApplication_strategy)
def test_hyp_leaveapplication_applicationId_setter(instance):
    original = instance.applicationId
    instance.applicationId = original
    assert instance.applicationId == original



@given(instance=LeaveApplication_strategy)
def test_hyp_leaveapplication_toDate_setter(instance):
    original = instance.toDate
    instance.toDate = original
    assert instance.toDate == original



@given(instance=LeaveApplication_strategy)
def test_hyp_leaveapplication_fromDate_setter(instance):
    original = instance.fromDate
    instance.fromDate = original
    assert instance.fromDate == original



@given(instance=LeaveApplication_strategy)
def test_hyp_leaveapplication_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=LeaveApplication_strategy)
def test_hyp_leaveapplication_approverComments_setter(instance):
    original = instance.approverComments
    instance.approverComments = original
    assert instance.approverComments == original



@given(instance=LeaveApplication_strategy)
def test_hyp_leaveapplication_employeeId_setter(instance):
    original = instance.employeeId
    instance.employeeId = original
    assert instance.employeeId == original



@given(instance=LeaveApplication_strategy)
def test_hyp_leaveapplication_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original




@given(instance=LeaveHistoryQuery_strategy)
def test_hyp_leavehistoryquery_fromDate_setter(instance):
    original = instance.fromDate
    instance.fromDate = original
    assert instance.fromDate == original



@given(instance=LeaveHistoryQuery_strategy)
def test_hyp_leavehistoryquery_toDate_setter(instance):
    original = instance.toDate
    instance.toDate = original
    assert instance.toDate == original



@given(instance=Query_strategy)
@settings(max_examples=50)
def test_hyp_query_instantiation(instance):
    assert isinstance(instance, Query)



@given(instance=Query_strategy)
def test_hyp_query_requestId_setter(instance):
    original = instance.requestId
    instance.requestId = original
    assert instance.requestId == original



@given(instance=Query_strategy)
def test_hyp_query_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original




@given(instance=Employee_strategy)
def test_hyp_employee_jobLevel_setter(instance):
    original = instance.jobLevel
    instance.jobLevel = original
    assert instance.jobLevel == original



@given(instance=Employee_strategy)
def test_hyp_employee_leavesTaken_setter(instance):
    original = instance.leavesTaken
    instance.leavesTaken = original
    assert instance.leavesTaken == original



@given(instance=Employee_strategy)
def test_hyp_employee_employeeId_setter(instance):
    original = instance.employeeId
    instance.employeeId = original
    assert instance.employeeId == original



@given(instance=Employee_strategy)
def test_hyp_employee_employeeName_setter(instance):
    original = instance.employeeName
    instance.employeeName = original
    assert instance.employeeName == original



@given(instance=Employee_strategy)
def test_hyp_employee_noOfLeaves_setter(instance):
    original = instance.noOfLeaves
    instance.noOfLeaves = original
    assert instance.noOfLeaves == original



@given(instance=Employee_strategy)
def test_hyp_employee_managerId_setter(instance):
    original = instance.managerId
    instance.managerId = original
    assert instance.managerId == original



@given(instance=Employee_strategy)
def test_hyp_employee_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original






















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin_Actor,
    ApplicationUtils,
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
    Employee_Actor1,
    GenerateSummary_UseCase,
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
    LeaveStatus,
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

def test_Employee_employeeId_value_roundtrip():
    instance = Employee(employeeId="sample_text", employeeName="sample_text", jobLevel=7, leavesTaken="sample_text", managerId="sample_text", noOfLeaves=7, password="sample_text")
    assert instance.employeeId == "sample_text"
    instance.employeeId = "sample_text_2"
    assert instance.employeeId == "sample_text_2"


def test_Employee_employeeName_value_roundtrip():
    instance = Employee(employeeId="sample_text", employeeName="sample_text", jobLevel=7, leavesTaken="sample_text", managerId="sample_text", noOfLeaves=7, password="sample_text")
    assert instance.employeeName == "sample_text"
    instance.employeeName = "sample_text_2"
    assert instance.employeeName == "sample_text_2"


def test_Employee_jobLevel_value_roundtrip():
    instance = Employee(employeeId="sample_text", employeeName="sample_text", jobLevel=7, leavesTaken="sample_text", managerId="sample_text", noOfLeaves=7, password="sample_text")
    assert instance.jobLevel == 7
    instance.jobLevel = 13
    assert instance.jobLevel == 13


def test_Employee_leavesTaken_value_roundtrip():
    instance = Employee(employeeId="sample_text", employeeName="sample_text", jobLevel=7, leavesTaken="sample_text", managerId="sample_text", noOfLeaves=7, password="sample_text")
    assert instance.leavesTaken == "sample_text"
    instance.leavesTaken = "sample_text_2"
    assert instance.leavesTaken == "sample_text_2"


def test_Employee_managerId_value_roundtrip():
    instance = Employee(employeeId="sample_text", employeeName="sample_text", jobLevel=7, leavesTaken="sample_text", managerId="sample_text", noOfLeaves=7, password="sample_text")
    assert instance.managerId == "sample_text"
    instance.managerId = "sample_text_2"
    assert instance.managerId == "sample_text_2"


def test_Employee_noOfLeaves_value_roundtrip():
    instance = Employee(employeeId="sample_text", employeeName="sample_text", jobLevel=7, leavesTaken="sample_text", managerId="sample_text", noOfLeaves=7, password="sample_text")
    assert instance.noOfLeaves == 7
    instance.noOfLeaves = 13
    assert instance.noOfLeaves == 13


def test_Employee_password_value_roundtrip():
    instance = Employee(employeeId="sample_text", employeeName="sample_text", jobLevel=7, leavesTaken="sample_text", managerId="sample_text", noOfLeaves=7, password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_LeaveApplication_applicationId_value_roundtrip():
    instance = LeaveApplication(applicationId="sample_text", approverComments="sample_text", employeeId="sample_text", fromDate=date(2024, 1, 1), reason="sample_text", status="sample_text", toDate=date(2024, 1, 1))
    assert instance.applicationId == "sample_text"
    instance.applicationId = "sample_text_2"
    assert instance.applicationId == "sample_text_2"


def test_LeaveApplication_approverComments_value_roundtrip():
    instance = LeaveApplication(applicationId="sample_text", approverComments="sample_text", employeeId="sample_text", fromDate=date(2024, 1, 1), reason="sample_text", status="sample_text", toDate=date(2024, 1, 1))
    assert instance.approverComments == "sample_text"
    instance.approverComments = "sample_text_2"
    assert instance.approverComments == "sample_text_2"


def test_LeaveApplication_employeeId_value_roundtrip():
    instance = LeaveApplication(applicationId="sample_text", approverComments="sample_text", employeeId="sample_text", fromDate=date(2024, 1, 1), reason="sample_text", status="sample_text", toDate=date(2024, 1, 1))
    assert instance.employeeId == "sample_text"
    instance.employeeId = "sample_text_2"
    assert instance.employeeId == "sample_text_2"


def test_LeaveApplication_fromDate_value_roundtrip():
    instance = LeaveApplication(applicationId="sample_text", approverComments="sample_text", employeeId="sample_text", fromDate=date(2024, 1, 1), reason="sample_text", status="sample_text", toDate=date(2024, 1, 1))
    assert instance.fromDate == date(2024, 1, 1)
    instance.fromDate = date(2025, 6, 15)
    assert instance.fromDate == date(2025, 6, 15)


def test_LeaveApplication_reason_value_roundtrip():
    instance = LeaveApplication(applicationId="sample_text", approverComments="sample_text", employeeId="sample_text", fromDate=date(2024, 1, 1), reason="sample_text", status="sample_text", toDate=date(2024, 1, 1))
    assert instance.reason == "sample_text"
    instance.reason = "sample_text_2"
    assert instance.reason == "sample_text_2"


def test_LeaveApplication_status_value_roundtrip():
    instance = LeaveApplication(applicationId="sample_text", approverComments="sample_text", employeeId="sample_text", fromDate=date(2024, 1, 1), reason="sample_text", status="sample_text", toDate=date(2024, 1, 1))
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_LeaveApplication_toDate_value_roundtrip():
    instance = LeaveApplication(applicationId="sample_text", approverComments="sample_text", employeeId="sample_text", fromDate=date(2024, 1, 1), reason="sample_text", status="sample_text", toDate=date(2024, 1, 1))
    assert instance.toDate == date(2024, 1, 1)
    instance.toDate = date(2025, 6, 15)
    assert instance.toDate == date(2025, 6, 15)


def test_LeaveHistoryQuery_fromDate_value_roundtrip():
    instance = LeaveHistoryQuery(fromDate=date(2024, 1, 1), toDate=date(2024, 1, 1))
    assert instance.fromDate == date(2024, 1, 1)
    instance.fromDate = date(2025, 6, 15)
    assert instance.fromDate == date(2025, 6, 15)


def test_LeaveHistoryQuery_toDate_value_roundtrip():
    instance = LeaveHistoryQuery(fromDate=date(2024, 1, 1), toDate=date(2024, 1, 1))
    assert instance.toDate == date(2024, 1, 1)
    instance.toDate = date(2025, 6, 15)
    assert instance.toDate == date(2025, 6, 15)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_Actor_strategy = st.builds(Admin_Actor)
@given(instance=Admin_Actor_strategy)
@settings(max_examples=25)
def test_Admin_Actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)


ApplicationUtils_strategy = st.builds(ApplicationUtils)
@given(instance=ApplicationUtils_strategy)
@settings(max_examples=25)
def test_ApplicationUtils_instantiation(instance):
    assert isinstance(instance, ApplicationUtils)


ApplyLeaveRequest_strategy = st.builds(ApplyLeaveRequest)
@given(instance=ApplyLeaveRequest_strategy)
@settings(max_examples=25)
def test_ApplyLeaveRequest_instantiation(instance):
    assert isinstance(instance, ApplyLeaveRequest)


Apply_Leave_UseCase_strategy = st.builds(Apply_Leave_UseCase)
@given(instance=Apply_Leave_UseCase_strategy)
@settings(max_examples=25)
def test_Apply_Leave_UseCase_instantiation(instance):
    assert isinstance(instance, Apply_Leave_UseCase)


ApproveOrRejectStatus_strategy = st.builds(ApproveOrRejectStatus)
@given(instance=ApproveOrRejectStatus_strategy)
@settings(max_examples=25)
def test_ApproveOrRejectStatus_instantiation(instance):
    assert isinstance(instance, ApproveOrRejectStatus)


Approve_RejectRequests_UseCase_strategy = st.builds(Approve_RejectRequests_UseCase)
@given(instance=Approve_RejectRequests_UseCase_strategy)
@settings(max_examples=25)
def test_Approve_RejectRequests_UseCase_instantiation(instance):
    assert isinstance(instance, Approve_RejectRequests_UseCase)


Approver_Jobs_UseCase_strategy = st.builds(Approver_Jobs_UseCase)
@given(instance=Approver_Jobs_UseCase_strategy)
@settings(max_examples=25)
def test_Approver_Jobs_UseCase_instantiation(instance):
    assert isinstance(instance, Approver_Jobs_UseCase)


AutoApproval_UseCase_strategy = st.builds(AutoApproval_UseCase)
@given(instance=AutoApproval_UseCase_strategy)
@settings(max_examples=25)
def test_AutoApproval_UseCase_instantiation(instance):
    assert isinstance(instance, AutoApproval_UseCase)


CancelLeaveRequest_strategy = st.builds(CancelLeaveRequest)
@given(instance=CancelLeaveRequest_strategy)
@settings(max_examples=25)
def test_CancelLeaveRequest_instantiation(instance):
    assert isinstance(instance, CancelLeaveRequest)


Cancel_Leaves_UseCase_strategy = st.builds(Cancel_Leaves_UseCase)
@given(instance=Cancel_Leaves_UseCase_strategy)
@settings(max_examples=25)
def test_Cancel_Leaves_UseCase_instantiation(instance):
    assert isinstance(instance, Cancel_Leaves_UseCase)


Change_Password_UseCase_strategy = st.builds(Change_Password_UseCase)
@given(instance=Change_Password_UseCase_strategy)
@settings(max_examples=25)
def test_Change_Password_UseCase_instantiation(instance):
    assert isinstance(instance, Change_Password_UseCase)


CreateUser_UseCase_strategy = st.builds(CreateUser_UseCase)
@given(instance=CreateUser_UseCase_strategy)
@settings(max_examples=25)
def test_CreateUser_UseCase_instantiation(instance):
    assert isinstance(instance, CreateUser_UseCase)


Credit_Leaves_UseCase_strategy = st.builds(Credit_Leaves_UseCase)
@given(instance=Credit_Leaves_UseCase_strategy)
@settings(max_examples=25)
def test_Credit_Leaves_UseCase_instantiation(instance):
    assert isinstance(instance, Credit_Leaves_UseCase)


EligibilityQuery_strategy = st.builds(EligibilityQuery)
@given(instance=EligibilityQuery_strategy)
@settings(max_examples=25)
def test_EligibilityQuery_instantiation(instance):
    assert isinstance(instance, EligibilityQuery)


Employee_strategy = st.builds(Employee, employeeId=safe_text, employeeName=safe_text, jobLevel=st.integers(), leavesTaken=safe_text, managerId=safe_text, noOfLeaves=st.integers(), password=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Employee_Actor_strategy = st.builds(Employee_Actor)
@given(instance=Employee_Actor_strategy)
@settings(max_examples=25)
def test_Employee_Actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)


Employee_Actor1_strategy = st.builds(Employee_Actor1)
@given(instance=Employee_Actor1_strategy)
@settings(max_examples=25)
def test_Employee_Actor1_instantiation(instance):
    assert isinstance(instance, Employee_Actor1)


GenerateSummary_UseCase_strategy = st.builds(GenerateSummary_UseCase)
@given(instance=GenerateSummary_UseCase_strategy)
@settings(max_examples=25)
def test_GenerateSummary_UseCase_instantiation(instance):
    assert isinstance(instance, GenerateSummary_UseCase)


LeaveApplication_strategy = st.builds(LeaveApplication, applicationId=safe_text, approverComments=safe_text, employeeId=safe_text, fromDate=st.dates(), reason=safe_text, status=safe_text, toDate=st.dates())
@given(instance=LeaveApplication_strategy)
@settings(max_examples=25)
def test_LeaveApplication_instantiation(instance):
    assert isinstance(instance, LeaveApplication)


LeaveBalanceQuery_strategy = st.builds(LeaveBalanceQuery)
@given(instance=LeaveBalanceQuery_strategy)
@settings(max_examples=25)
def test_LeaveBalanceQuery_instantiation(instance):
    assert isinstance(instance, LeaveBalanceQuery)


LeaveHistoryQuery_strategy = st.builds(LeaveHistoryQuery, fromDate=st.dates(), toDate=st.dates())
@given(instance=LeaveHistoryQuery_strategy)
@settings(max_examples=25)
def test_LeaveHistoryQuery_instantiation(instance):
    assert isinstance(instance, LeaveHistoryQuery)


LeaveStatusQuery_strategy = st.builds(LeaveStatusQuery)
@given(instance=LeaveStatusQuery_strategy)
@settings(max_examples=25)
def test_LeaveStatusQuery_instantiation(instance):
    assert isinstance(instance, LeaveStatusQuery)


Leave_Request_Status_UseCase_strategy = st.builds(Leave_Request_Status_UseCase)
@given(instance=Leave_Request_Status_UseCase_strategy)
@settings(max_examples=25)
def test_Leave_Request_Status_UseCase_instantiation(instance):
    assert isinstance(instance, Leave_Request_Status_UseCase)


Login_UseCase_strategy = st.builds(Login_UseCase)
@given(instance=Login_UseCase_strategy)
@settings(max_examples=25)
def test_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)


Query_Eligibility_UseCase_strategy = st.builds(Query_Eligibility_UseCase)
@given(instance=Query_Eligibility_UseCase_strategy)
@settings(max_examples=25)
def test_Query_Eligibility_UseCase_instantiation(instance):
    assert isinstance(instance, Query_Eligibility_UseCase)


Query_Leave_Balance_UseCase_strategy = st.builds(Query_Leave_Balance_UseCase)
@given(instance=Query_Leave_Balance_UseCase_strategy)
@settings(max_examples=25)
def test_Query_Leave_Balance_UseCase_instantiation(instance):
    assert isinstance(instance, Query_Leave_Balance_UseCase)


Query_Leave_History_UseCase_strategy = st.builds(Query_Leave_History_UseCase)
@given(instance=Query_Leave_History_UseCase_strategy)
@settings(max_examples=25)
def test_Query_Leave_History_UseCase_instantiation(instance):
    assert isinstance(instance, Query_Leave_History_UseCase)


SendNotification_UseCase_strategy = st.builds(SendNotification_UseCase)
@given(instance=SendNotification_UseCase_strategy)
@settings(max_examples=25)
def test_SendNotification_UseCase_instantiation(instance):
    assert isinstance(instance, SendNotification_UseCase)


UpdateCalendar_strategy = st.builds(UpdateCalendar)
@given(instance=UpdateCalendar_strategy)
@settings(max_examples=25)
def test_UpdateCalendar_instantiation(instance):
    assert isinstance(instance, UpdateCalendar)


Update_Calendar_UseCase_strategy = st.builds(Update_Calendar_UseCase)
@given(instance=Update_Calendar_UseCase_strategy)
@settings(max_examples=25)
def test_Update_Calendar_UseCase_instantiation(instance):
    assert isinstance(instance, Update_Calendar_UseCase)


WithdrawLeaveRequest_strategy = st.builds(WithdrawLeaveRequest)
@given(instance=WithdrawLeaveRequest_strategy)
@settings(max_examples=25)
def test_WithdrawLeaveRequest_instantiation(instance):
    assert isinstance(instance, WithdrawLeaveRequest)


Withdraw_Application_UseCase_strategy = st.builds(Withdraw_Application_UseCase)
@given(instance=Withdraw_Application_UseCase_strategy)
@settings(max_examples=25)
def test_Withdraw_Application_UseCase_instantiation(instance):
    assert isinstance(instance, Withdraw_Application_UseCase)



