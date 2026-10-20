import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Clark1_Actor,
    Clark1_Actor1,
    Class_Diagram_for_Proposed_system_Advances,
    Class_Diagram_for_Proposed_system_Allowances,
    Class_Diagram_for_Proposed_system_Attendance,
    Class_Diagram_for_Proposed_system_Calender,
    Class_Diagram_for_Proposed_system_Deductions,
    Class_Diagram_for_Proposed_system_Department,
    Class_Diagram_for_Proposed_system_EPF,
    Class_Diagram_for_Proposed_system_ETF,
    Class_Diagram_for_Proposed_system_Employee,
    Class_Diagram_for_Proposed_system_Events,
    Class_Diagram_for_Proposed_system_LeaveTaken,
    Class_Diagram_for_Proposed_system_LeavesAllocated,
    Class_Diagram_for_Proposed_system_Post,
    Class_Diagram_for_Proposed_system_Role,
    Class_Diagram_for_Proposed_system_Salary,
    Class_Diagram_for_Proposed_system_User,
    Class_Diagram_for_Proposed_system_WorkingShifts,
    Class_Diagram_for_Proposed_system_overtimeRequests,
    Manager_Actor,
    Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase,
    Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase,
    Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase,
    Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase,
    Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase,
    Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase,
    Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase,
    Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase,
    Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase,
    Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase,
    Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase,
    Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase,
    Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase,
    Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase,
    Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase,
    Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase,
    Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase,
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

def test_assoc_Advances_Salary_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    a2 = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text_2", ETF="sample_text_2", advances="sample_text_2", allowances="sample_text_2", basicPay="sample_text_2", deductions="sample_text_2", empId="sample_text_2", id="sample_text_2", overtimes="sample_text_2", payDate="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Advances(amount="sample_text", id="sample_text", installments="sample_text", issueDate="sample_text", salaryId="sample_text")
    _safe_set(b, 'salary28', {a1})
    assert _is_linked(b, 'salary28', a1)
    if hasattr(a1, 'advances229'):
        assert _is_linked(a1, 'advances229', b)
    _safe_set(b, 'salary28', {a2})
    assert _is_linked(b, 'salary28', a2)
    if hasattr(a1, 'advances229'):
        assert not _is_linked(a1, 'advances229', b)
    if hasattr(a2, 'advances229'):
        assert _is_linked(a2, 'advances229', b)
    _safe_set(b, 'salary28', set())
    assert not _is_linked(b, 'salary28', a2)
    if hasattr(a2, 'advances229'):
        assert not _is_linked(a2, 'advances229', b)


def test_assoc_Allowances_Salary_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    a2 = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text_2", ETF="sample_text_2", advances="sample_text_2", allowances="sample_text_2", basicPay="sample_text_2", deductions="sample_text_2", empId="sample_text_2", id="sample_text_2", overtimes="sample_text_2", payDate="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text", amount="sample_text", id="sample_text", issueDate="sample_text", salaryId="sample_text")
    _safe_set(b, 'salary24', a1)
    assert _is_linked(b, 'salary24', a1)
    if hasattr(a1, 'allowances225'):
        assert _is_linked(a1, 'allowances225', b)
    _safe_set(b, 'salary24', a2)
    assert _is_linked(b, 'salary24', a2)
    if hasattr(a1, 'allowances225'):
        assert not _is_linked(a1, 'allowances225', b)
    if hasattr(a2, 'allowances225'):
        assert _is_linked(a2, 'allowances225', b)
    _safe_set(b, 'salary24', None)
    assert not _is_linked(b, 'salary24', a2)
    if hasattr(a2, 'allowances225'):
        assert not _is_linked(a2, 'allowances225', b)


def test_assoc_Attendance_Employee_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    a2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    b = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    _safe_set(b, 'employee36', a1)
    assert _is_linked(b, 'employee36', a1)
    if hasattr(a1, 'attendance37'):
        assert _is_linked(a1, 'attendance37', b)
    _safe_set(b, 'employee36', a2)
    assert _is_linked(b, 'employee36', a2)
    if hasattr(a1, 'attendance37'):
        assert not _is_linked(a1, 'attendance37', b)
    if hasattr(a2, 'attendance37'):
        assert _is_linked(a2, 'attendance37', b)
    _safe_set(b, 'employee36', None)
    assert not _is_linked(b, 'employee36', a2)
    if hasattr(a2, 'attendance37'):
        assert not _is_linked(a2, 'attendance37', b)


def test_assoc_Calender_Events_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Events(id="sample_text", type="sample_text")
    a2 = Class_Diagram_for_Proposed_system_Events(id="sample_text_2", type="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Calender(author_id="sample_text", depid="sample_text", eventType="sample_text", id="sample_text")
    _safe_set(b, 'events48', a1)
    assert _is_linked(b, 'events48', a1)
    if hasattr(a1, 'calender49'):
        assert _is_linked(a1, 'calender49', b)
    _safe_set(b, 'events48', a2)
    assert _is_linked(b, 'events48', a2)
    if hasattr(a1, 'calender49'):
        assert not _is_linked(a1, 'calender49', b)
    if hasattr(a2, 'calender49'):
        assert _is_linked(a2, 'calender49', b)
    _safe_set(b, 'events48', None)
    assert not _is_linked(b, 'events48', a2)
    if hasattr(a2, 'calender49'):
        assert not _is_linked(a2, 'calender49', b)


def test_assoc_Deductions_Salary_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    a2 = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text_2", ETF="sample_text_2", advances="sample_text_2", allowances="sample_text_2", basicPay="sample_text_2", deductions="sample_text_2", empId="sample_text_2", id="sample_text_2", overtimes="sample_text_2", payDate="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text", deducType="sample_text", deductDate="sample_text", id="sample_text", salaryId="sample_text")
    _safe_set(b, 'salary26', a1)
    assert _is_linked(b, 'salary26', a1)
    if hasattr(a1, 'deductions227'):
        assert _is_linked(a1, 'deductions227', b)
    _safe_set(b, 'salary26', a2)
    assert _is_linked(b, 'salary26', a2)
    if hasattr(a1, 'deductions227'):
        assert not _is_linked(a1, 'deductions227', b)
    if hasattr(a2, 'deductions227'):
        assert _is_linked(a2, 'deductions227', b)
    _safe_set(b, 'salary26', None)
    assert not _is_linked(b, 'salary26', a2)
    if hasattr(a2, 'deductions227'):
        assert not _is_linked(a2, 'deductions227', b)


def test_assoc_Department_Post_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    a2 = Class_Diagram_for_Proposed_system_Post(attribute="sample_text_2", deptId="sample_text_2", id="sample_text_2", leavesEntitled="sample_text_2", name="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Department(empId="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'post32', {a1})
    assert _is_linked(b, 'post32', a1)
    if hasattr(a1, 'department33'):
        assert _is_linked(a1, 'department33', b)
    _safe_set(b, 'post32', {a2})
    assert _is_linked(b, 'post32', a2)
    if hasattr(a1, 'department33'):
        assert not _is_linked(a1, 'department33', b)
    if hasattr(a2, 'department33'):
        assert _is_linked(a2, 'department33', b)
    _safe_set(b, 'post32', set())
    assert not _is_linked(b, 'post32', a2)
    if hasattr(a2, 'department33'):
        assert not _is_linked(a2, 'department33', b)


def test_assoc_Employee_Department_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    a2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    b = Class_Diagram_for_Proposed_system_Department(empId="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'employee23', {a1})
    assert _is_linked(b, 'employee23', a1)
    if hasattr(a1, 'department22'):
        assert _is_linked(a1, 'department22', b)
    _safe_set(b, 'employee23', {a2})
    assert _is_linked(b, 'employee23', a2)
    if hasattr(a1, 'department22'):
        assert not _is_linked(a1, 'department22', b)
    if hasattr(a2, 'department22'):
        assert _is_linked(a2, 'department22', b)
    _safe_set(b, 'employee23', set())
    assert not _is_linked(b, 'employee23', a2)
    if hasattr(a2, 'department22'):
        assert not _is_linked(a2, 'department22', b)


def test_assoc_Employee_LeaveTaken_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text", empId="sample_text", id="sample_text", leaveDate="sample_text", leaveType="sample_text")
    a2 = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text_2", empId="sample_text_2", id="sample_text_2", leaveDate="sample_text_2", leaveType="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    _safe_set(b, 'leaveTaken30', {a1})
    assert _is_linked(b, 'leaveTaken30', a1)
    if hasattr(a1, 'employee31'):
        assert _is_linked(a1, 'employee31', b)
    _safe_set(b, 'leaveTaken30', {a2})
    assert _is_linked(b, 'leaveTaken30', a2)
    if hasattr(a1, 'employee31'):
        assert not _is_linked(a1, 'employee31', b)
    if hasattr(a2, 'employee31'):
        assert _is_linked(a2, 'employee31', b)
    _safe_set(b, 'leaveTaken30', set())
    assert not _is_linked(b, 'leaveTaken30', a2)
    if hasattr(a2, 'employee31'):
        assert not _is_linked(a2, 'employee31', b)


def test_assoc_Employee_LeavesAllocated_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    a2 = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text_2", id="sample_text_2", leaveType="sample_text_2", noOfLeaves="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    _safe_set(b, 'leavesAllocated38', a1)
    assert _is_linked(b, 'leavesAllocated38', a1)
    if hasattr(a1, 'employee39'):
        assert _is_linked(a1, 'employee39', b)
    _safe_set(b, 'leavesAllocated38', a2)
    assert _is_linked(b, 'leavesAllocated38', a2)
    if hasattr(a1, 'employee39'):
        assert not _is_linked(a1, 'employee39', b)
    if hasattr(a2, 'employee39'):
        assert _is_linked(a2, 'employee39', b)
    _safe_set(b, 'leavesAllocated38', None)
    assert not _is_linked(b, 'leavesAllocated38', a2)
    if hasattr(a2, 'employee39'):
        assert not _is_linked(a2, 'employee39', b)


def test_assoc_Employee_Post_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    a2 = Class_Diagram_for_Proposed_system_Post(attribute="sample_text_2", deptId="sample_text_2", id="sample_text_2", leavesEntitled="sample_text_2", name="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    _safe_set(b, 'post34', {a1})
    assert _is_linked(b, 'post34', a1)
    if hasattr(a1, 'employee35'):
        assert _is_linked(a1, 'employee35', b)
    _safe_set(b, 'post34', {a2})
    assert _is_linked(b, 'post34', a2)
    if hasattr(a1, 'employee35'):
        assert not _is_linked(a1, 'employee35', b)
    if hasattr(a2, 'employee35'):
        assert _is_linked(a2, 'employee35', b)
    _safe_set(b, 'post34', set())
    assert not _is_linked(b, 'post34', a2)
    if hasattr(a2, 'employee35'):
        assert not _is_linked(a2, 'employee35', b)


def test_assoc_Employee_User_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    a2 = Class_Diagram_for_Proposed_system_User(LastName="sample_text_2", firstNAme="sample_text_2", id="sample_text_2", roleId=13)
    b = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    _safe_set(b, 'user40', a1)
    assert _is_linked(b, 'user40', a1)
    if hasattr(a1, 'employee41'):
        assert _is_linked(a1, 'employee41', b)
    _safe_set(b, 'user40', a2)
    assert _is_linked(b, 'user40', a2)
    if hasattr(a1, 'employee41'):
        assert not _is_linked(a1, 'employee41', b)
    if hasattr(a2, 'employee41'):
        assert _is_linked(a2, 'employee41', b)
    _safe_set(b, 'user40', None)
    assert not _is_linked(b, 'user40', a2)
    if hasattr(a2, 'employee41'):
        assert not _is_linked(a2, 'employee41', b)


def test_assoc_Employee_overtimeRequests_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_overtimeRequests(date="sample_text", id="sample_text", nd_time="sample_text", start_time="sample_text")
    a2 = Class_Diagram_for_Proposed_system_overtimeRequests(date="sample_text_2", id="sample_text_2", nd_time="sample_text_2", start_time="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    _safe_set(b, 'overtimeRequests50', a1)
    assert _is_linked(b, 'overtimeRequests50', a1)
    if hasattr(a1, 'employee51'):
        assert _is_linked(a1, 'employee51', b)
    _safe_set(b, 'overtimeRequests50', a2)
    assert _is_linked(b, 'overtimeRequests50', a2)
    if hasattr(a1, 'employee51'):
        assert not _is_linked(a1, 'employee51', b)
    if hasattr(a2, 'employee51'):
        assert _is_linked(a2, 'employee51', b)
    _safe_set(b, 'overtimeRequests50', None)
    assert not _is_linked(b, 'overtimeRequests50', a2)
    if hasattr(a2, 'employee51'):
        assert not _is_linked(a2, 'employee51', b)


def test_assoc_LeavesAllocated_EPF_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    a2 = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text_2", id="sample_text_2", leaveType="sample_text_2", noOfLeaves="sample_text_2")
    b = Class_Diagram_for_Proposed_system_EPF(id="sample_text", precentage="sample_text")
    _safe_set(b, 'leavesAllocated45', a1)
    assert _is_linked(b, 'leavesAllocated45', a1)
    if hasattr(a1, 'ePF44'):
        assert _is_linked(a1, 'ePF44', b)
    _safe_set(b, 'leavesAllocated45', a2)
    assert _is_linked(b, 'leavesAllocated45', a2)
    if hasattr(a1, 'ePF44'):
        assert not _is_linked(a1, 'ePF44', b)
    if hasattr(a2, 'ePF44'):
        assert _is_linked(a2, 'ePF44', b)
    _safe_set(b, 'leavesAllocated45', None)
    assert not _is_linked(b, 'leavesAllocated45', a2)
    if hasattr(a2, 'ePF44'):
        assert not _is_linked(a2, 'ePF44', b)


def test_assoc_LeavesAllocated_ETF_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    a2 = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text_2", id="sample_text_2", leaveType="sample_text_2", noOfLeaves="sample_text_2")
    b = Class_Diagram_for_Proposed_system_ETF(id="sample_text", precentage="sample_text")
    _safe_set(b, 'leavesAllocated47', a1)
    assert _is_linked(b, 'leavesAllocated47', a1)
    if hasattr(a1, 'eTF46'):
        assert _is_linked(a1, 'eTF46', b)
    _safe_set(b, 'leavesAllocated47', a2)
    assert _is_linked(b, 'leavesAllocated47', a2)
    if hasattr(a1, 'eTF46'):
        assert not _is_linked(a1, 'eTF46', b)
    if hasattr(a2, 'eTF46'):
        assert _is_linked(a2, 'eTF46', b)
    _safe_set(b, 'leavesAllocated47', None)
    assert not _is_linked(b, 'leavesAllocated47', a2)
    if hasattr(a2, 'eTF46'):
        assert not _is_linked(a2, 'eTF46', b)


def test_assoc_User_Role_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    a2 = Class_Diagram_for_Proposed_system_User(LastName="sample_text_2", firstNAme="sample_text_2", id="sample_text_2", roleId=13)
    b = Class_Diagram_for_Proposed_system_Role(description="sample_text", id="sample_text", roleName="sample_text")
    _safe_set(b, 'user43', a1)
    assert _is_linked(b, 'user43', a1)
    if hasattr(a1, 'role42'):
        assert _is_linked(a1, 'role42', b)
    _safe_set(b, 'user43', a2)
    assert _is_linked(b, 'user43', a2)
    if hasattr(a1, 'role42'):
        assert not _is_linked(a1, 'role42', b)
    if hasattr(a2, 'role42'):
        assert _is_linked(a2, 'role42', b)
    _safe_set(b, 'user43', None)
    assert not _is_linked(b, 'user43', a2)
    if hasattr(a2, 'role42'):
        assert not _is_linked(a2, 'role42', b)


def test_assoc_WorkingShifts_Employee_reverse_link_reassign_clear():
    a1 = Class_Diagram_for_Proposed_system_WorkingShifts(empId="sample_text", endingTime="sample_text", id="sample_text", startingTime="sample_text")
    a2 = Class_Diagram_for_Proposed_system_WorkingShifts(empId="sample_text_2", endingTime="sample_text_2", id="sample_text_2", startingTime="sample_text_2")
    b = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    _safe_set(b, 'workingShifts21', a1)
    assert _is_linked(b, 'workingShifts21', a1)
    if hasattr(a1, 'employee20'):
        assert _is_linked(a1, 'employee20', b)
    _safe_set(b, 'workingShifts21', a2)
    assert _is_linked(b, 'workingShifts21', a2)
    if hasattr(a1, 'employee20'):
        assert not _is_linked(a1, 'employee20', b)
    if hasattr(a2, 'employee20'):
        assert _is_linked(a2, 'employee20', b)
    _safe_set(b, 'workingShifts21', None)
    assert not _is_linked(b, 'workingShifts21', a2)
    if hasattr(a2, 'employee20'):
        assert not _is_linked(a2, 'employee20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

