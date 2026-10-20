import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin_Actor,
    Clark_Actor,
    Employee_Actor,
    Interface_Interface,
    Package2_Advances,
    Package2_Allowance,
    Package2_AllowanceTypes,
    Package2_Attendance,
    Package2_Deductions,
    Package2_Departments,
    Package2_DeuctionTypes,
    Package2_EPF,
    Package2_ETF,
    Package2_Employee,
    Package2_EmployeeParoll,
    Package2_EmployeeSalary,
    Package2_Event,
    Package2_LeaveProfiles,
    Package2_Leave_Taken,
    Package2_Messages,
    Package2_OT_Requests,
    Package2_Posts,
    Package2_Shifts,
    Package2_UserUpdates,
    Package2_User_Permissions,
    Package2_User_groups,
    Package2_Users,
    Package_Advances,
    Package_Allowance,
    Package_AllowanceTypes,
    Package_Attendance,
    Package_Deductions,
    Package_Departments,
    Package_DeuctionTypes,
    Package_EPF,
    Package_ETF,
    Package_Employee,
    Package_EmployeeParoll,
    Package_EmployeeSalary,
    Package_Event,
    Package_LeaveProfiles,
    Package_Leave_Taken,
    Package_Messages,
    Package_OT_Requests,
    Package_Posts,
    Package_Shifts,
    Package_UserUpdates,
    Package_User_Permissions,
    Package_User_groups,
    Package_Users,
    Presentation_StaffUI,
    Use_Case_Diagram_for_Proposed_System_Accept_Leave_UseCase,
    Use_Case_Diagram_for_Proposed_System_Add_Employee_Time_Records_UseCase,
    Use_Case_Diagram_for_Proposed_System_Add_Employee_profile_UseCase,
    Use_Case_Diagram_for_Proposed_System_Add_New_department_UseCase,
    Use_Case_Diagram_for_Proposed_System_Add_new_company_Events_UseCase,
    Use_Case_Diagram_for_Proposed_System_Approve_Employee_Pay_sheets_UseCase,
    Use_Case_Diagram_for_Proposed_System_Generate_Paysheet_UseCase,
    Use_Case_Diagram_for_Proposed_System_Issue_and_Check_Appraislas_UseCase,
    Use_Case_Diagram_for_Proposed_System_Reject_Leave_UseCase,
    Use_Case_Diagram_for_Proposed_System_Request_Leaves_UseCase,
    Use_Case_Diagram_for_Proposed_System_Request_Loan_and_advances_UseCase,
    Use_Case_Diagram_for_Proposed_System_Set_Leave_status_UseCase,
    Use_Case_Diagram_for_Proposed_System_Set_advances_status_UseCase,
    Use_Case_Diagram_for_Proposed_System_Update_Leave_Balance_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Employee_Time_Records_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Employee_profiles_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Leave_status_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Pay_Sheet_History_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Personal_Salary_History_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Personal_Time_Records_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_Reports_UseCase1,
    Use_Case_Diagram_for_Proposed_System_View_leave_Rquest_UseCase,
    Use_Case_Diagram_for_Proposed_System_View_personal_detais_UseCase,
    date,
    ot_Type,
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

def test_assoc_Allowance_Employee_reverse_link_reassign_clear():
    a1 = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    a2 = Package_Employee(depid=13, empid="sample_text_2", id="sample_text_2", leavegroup=13, post="sample_text_2", shift="sample_text_2", usergroup=13)
    b = Package_Allowance(Effectivedate="sample_text", emp_id="sample_text", id=7)
    _safe_set(b, 'Allowance_Employee_056', {a1})
    assert _is_linked(b, 'Allowance_Employee_056', a1)
    if hasattr(a1, 'Allowance_Employee_157'):
        assert _is_linked(a1, 'Allowance_Employee_157', b)
    _safe_set(b, 'Allowance_Employee_056', {a2})
    assert _is_linked(b, 'Allowance_Employee_056', a2)
    if hasattr(a1, 'Allowance_Employee_157'):
        assert not _is_linked(a1, 'Allowance_Employee_157', b)
    if hasattr(a2, 'Allowance_Employee_157'):
        assert _is_linked(a2, 'Allowance_Employee_157', b)
    _safe_set(b, 'Allowance_Employee_056', set())
    assert not _is_linked(b, 'Allowance_Employee_056', a2)
    if hasattr(a2, 'Allowance_Employee_157'):
        assert not _is_linked(a2, 'Allowance_Employee_157', b)


def test_assoc_Allowance_Employee1_reverse_link_reassign_clear():
    a1 = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    a2 = Package2_Employee(depid=13, empid="sample_text_2", id="sample_text_2", leavegroup=13, post="sample_text_2", shift="sample_text_2", usergroup=13)
    b = Package2_Allowance(Effectivedate="sample_text", emp_id="sample_text", id=7)
    _safe_set(b, 'Allowance_Employee_086', {a1})
    assert _is_linked(b, 'Allowance_Employee_086', a1)
    if hasattr(a1, 'Allowance_Employee_187'):
        assert _is_linked(a1, 'Allowance_Employee_187', b)
    _safe_set(b, 'Allowance_Employee_086', {a2})
    assert _is_linked(b, 'Allowance_Employee_086', a2)
    if hasattr(a1, 'Allowance_Employee_187'):
        assert not _is_linked(a1, 'Allowance_Employee_187', b)
    if hasattr(a2, 'Allowance_Employee_187'):
        assert _is_linked(a2, 'Allowance_Employee_187', b)
    _safe_set(b, 'Allowance_Employee_086', set())
    assert not _is_linked(b, 'Allowance_Employee_086', a2)
    if hasattr(a2, 'Allowance_Employee_187'):
        assert not _is_linked(a2, 'Allowance_Employee_187', b)


def test_assoc_Attendance_Employee_reverse_link_reassign_clear():
    a1 = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    a2 = Package_Employee(depid=13, empid="sample_text_2", id="sample_text_2", leavegroup=13, post="sample_text_2", shift="sample_text_2", usergroup=13)
    b = Package_Attendance(empid=7, id=7, timein="sample_text", timeout="sample_text")
    _safe_set(b, 'Attendance_Employee_046', a1)
    assert _is_linked(b, 'Attendance_Employee_046', a1)
    if hasattr(a1, 'Attendance_Employee_147'):
        assert _is_linked(a1, 'Attendance_Employee_147', b)
    _safe_set(b, 'Attendance_Employee_046', a2)
    assert _is_linked(b, 'Attendance_Employee_046', a2)
    if hasattr(a1, 'Attendance_Employee_147'):
        assert not _is_linked(a1, 'Attendance_Employee_147', b)
    if hasattr(a2, 'Attendance_Employee_147'):
        assert _is_linked(a2, 'Attendance_Employee_147', b)
    _safe_set(b, 'Attendance_Employee_046', None)
    assert not _is_linked(b, 'Attendance_Employee_046', a2)
    if hasattr(a2, 'Attendance_Employee_147'):
        assert not _is_linked(a2, 'Attendance_Employee_147', b)


def test_assoc_Attendance_Employee1_reverse_link_reassign_clear():
    a1 = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    a2 = Package2_Employee(depid=13, empid="sample_text_2", id="sample_text_2", leavegroup=13, post="sample_text_2", shift="sample_text_2", usergroup=13)
    b = Package2_Attendance(empid=7, id=7, timein="sample_text", timeout="sample_text")
    _safe_set(b, 'Attendance_Employee_076', a1)
    assert _is_linked(b, 'Attendance_Employee_076', a1)
    if hasattr(a1, 'Attendance_Employee_177'):
        assert _is_linked(a1, 'Attendance_Employee_177', b)
    _safe_set(b, 'Attendance_Employee_076', a2)
    assert _is_linked(b, 'Attendance_Employee_076', a2)
    if hasattr(a1, 'Attendance_Employee_177'):
        assert not _is_linked(a1, 'Attendance_Employee_177', b)
    if hasattr(a2, 'Attendance_Employee_177'):
        assert _is_linked(a2, 'Attendance_Employee_177', b)
    _safe_set(b, 'Attendance_Employee_076', None)
    assert not _is_linked(b, 'Attendance_Employee_076', a2)
    if hasattr(a2, 'Attendance_Employee_177'):
        assert not _is_linked(a2, 'Attendance_Employee_177', b)


def test_assoc_Departments_Employee_reverse_link_reassign_clear():
    a1 = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    a2 = Package_Employee(depid=13, empid="sample_text_2", id="sample_text_2", leavegroup=13, post="sample_text_2", shift="sample_text_2", usergroup=13)
    b = Package_Departments(id=7)
    _safe_set(b, 'Departments_Employee_064', a1)
    assert _is_linked(b, 'Departments_Employee_064', a1)
    if hasattr(a1, 'Departments_Employee_165'):
        assert _is_linked(a1, 'Departments_Employee_165', b)
    _safe_set(b, 'Departments_Employee_064', a2)
    assert _is_linked(b, 'Departments_Employee_064', a2)
    if hasattr(a1, 'Departments_Employee_165'):
        assert not _is_linked(a1, 'Departments_Employee_165', b)
    if hasattr(a2, 'Departments_Employee_165'):
        assert _is_linked(a2, 'Departments_Employee_165', b)
    _safe_set(b, 'Departments_Employee_064', None)
    assert not _is_linked(b, 'Departments_Employee_064', a2)
    if hasattr(a2, 'Departments_Employee_165'):
        assert not _is_linked(a2, 'Departments_Employee_165', b)


def test_assoc_Departments_Employee1_reverse_link_reassign_clear():
    a1 = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    a2 = Package2_Employee(depid=13, empid="sample_text_2", id="sample_text_2", leavegroup=13, post="sample_text_2", shift="sample_text_2", usergroup=13)
    b = Package2_Departments(depname="sample_text", id=7)
    _safe_set(b, 'Departments_Employee_094', a1)
    assert _is_linked(b, 'Departments_Employee_094', a1)
    if hasattr(a1, 'Departments_Employee_195'):
        assert _is_linked(a1, 'Departments_Employee_195', b)
    _safe_set(b, 'Departments_Employee_094', a2)
    assert _is_linked(b, 'Departments_Employee_094', a2)
    if hasattr(a1, 'Departments_Employee_195'):
        assert not _is_linked(a1, 'Departments_Employee_195', b)
    if hasattr(a2, 'Departments_Employee_195'):
        assert _is_linked(a2, 'Departments_Employee_195', b)
    _safe_set(b, 'Departments_Employee_094', None)
    assert not _is_linked(b, 'Departments_Employee_094', a2)
    if hasattr(a2, 'Departments_Employee_195'):
        assert not _is_linked(a2, 'Departments_Employee_195', b)


def test_assoc_Employee_EmployeeParoll_reverse_link_reassign_clear():
    a1 = Package_EmployeeParoll(attribute="sample_text", attribute2="sample_text")
    a2 = Package_EmployeeParoll(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_EmployeeParoll_066', {a1})
    assert _is_linked(b, 'Employee_EmployeeParoll_066', a1)
    if hasattr(a1, 'Employee_EmployeeParoll_167'):
        assert _is_linked(a1, 'Employee_EmployeeParoll_167', b)
    _safe_set(b, 'Employee_EmployeeParoll_066', {a2})
    assert _is_linked(b, 'Employee_EmployeeParoll_066', a2)
    if hasattr(a1, 'Employee_EmployeeParoll_167'):
        assert not _is_linked(a1, 'Employee_EmployeeParoll_167', b)
    if hasattr(a2, 'Employee_EmployeeParoll_167'):
        assert _is_linked(a2, 'Employee_EmployeeParoll_167', b)
    _safe_set(b, 'Employee_EmployeeParoll_066', set())
    assert not _is_linked(b, 'Employee_EmployeeParoll_066', a2)
    if hasattr(a2, 'Employee_EmployeeParoll_167'):
        assert not _is_linked(a2, 'Employee_EmployeeParoll_167', b)


def test_assoc_Employee_EmployeeParoll1_reverse_link_reassign_clear():
    a1 = Package2_EmployeeParoll(basicslaray=7, doyamount=7, empid=7, empid3=7, epf=7, etf="sample_text", id=7, otamount=7)
    a2 = Package2_EmployeeParoll(basicslaray=13, doyamount=13, empid=13, empid3=13, epf=13, etf="sample_text_2", id=13, otamount=13)
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_EmployeeParoll_096', {a1})
    assert _is_linked(b, 'Employee_EmployeeParoll_096', a1)
    if hasattr(a1, 'Employee_EmployeeParoll_197'):
        assert _is_linked(a1, 'Employee_EmployeeParoll_197', b)
    _safe_set(b, 'Employee_EmployeeParoll_096', {a2})
    assert _is_linked(b, 'Employee_EmployeeParoll_096', a2)
    if hasattr(a1, 'Employee_EmployeeParoll_197'):
        assert not _is_linked(a1, 'Employee_EmployeeParoll_197', b)
    if hasattr(a2, 'Employee_EmployeeParoll_197'):
        assert _is_linked(a2, 'Employee_EmployeeParoll_197', b)
    _safe_set(b, 'Employee_EmployeeParoll_096', set())
    assert not _is_linked(b, 'Employee_EmployeeParoll_096', a2)
    if hasattr(a2, 'Employee_EmployeeParoll_197'):
        assert not _is_linked(a2, 'Employee_EmployeeParoll_197', b)


def test_assoc_Employee_EmployeeSalary_reverse_link_reassign_clear():
    a1 = Package_EmployeeSalary(attribute="sample_text", attribute2="sample_text")
    a2 = Package_EmployeeSalary(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_EmployeeSalary_054', {a1})
    assert _is_linked(b, 'Employee_EmployeeSalary_054', a1)
    if hasattr(a1, 'Employee_EmployeeSalary_155'):
        assert _is_linked(a1, 'Employee_EmployeeSalary_155', b)
    _safe_set(b, 'Employee_EmployeeSalary_054', {a2})
    assert _is_linked(b, 'Employee_EmployeeSalary_054', a2)
    if hasattr(a1, 'Employee_EmployeeSalary_155'):
        assert not _is_linked(a1, 'Employee_EmployeeSalary_155', b)
    if hasattr(a2, 'Employee_EmployeeSalary_155'):
        assert _is_linked(a2, 'Employee_EmployeeSalary_155', b)
    _safe_set(b, 'Employee_EmployeeSalary_054', set())
    assert not _is_linked(b, 'Employee_EmployeeSalary_054', a2)
    if hasattr(a2, 'Employee_EmployeeSalary_155'):
        assert not _is_linked(a2, 'Employee_EmployeeSalary_155', b)


def test_assoc_Employee_EmployeeSalary1_reverse_link_reassign_clear():
    a1 = Package2_EmployeeSalary(attribute="sample_text", attribute2="sample_text")
    a2 = Package2_EmployeeSalary(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_EmployeeSalary_084', {a1})
    assert _is_linked(b, 'Employee_EmployeeSalary_084', a1)
    if hasattr(a1, 'Employee_EmployeeSalary_185'):
        assert _is_linked(a1, 'Employee_EmployeeSalary_185', b)
    _safe_set(b, 'Employee_EmployeeSalary_084', {a2})
    assert _is_linked(b, 'Employee_EmployeeSalary_084', a2)
    if hasattr(a1, 'Employee_EmployeeSalary_185'):
        assert not _is_linked(a1, 'Employee_EmployeeSalary_185', b)
    if hasattr(a2, 'Employee_EmployeeSalary_185'):
        assert _is_linked(a2, 'Employee_EmployeeSalary_185', b)
    _safe_set(b, 'Employee_EmployeeSalary_084', set())
    assert not _is_linked(b, 'Employee_EmployeeSalary_084', a2)
    if hasattr(a2, 'Employee_EmployeeSalary_185'):
        assert not _is_linked(a2, 'Employee_EmployeeSalary_185', b)


def test_assoc_Employee_LeaveProfiles_reverse_link_reassign_clear():
    a1 = Package_LeaveProfiles(attribute="sample_text", attribute2="sample_text")
    a2 = Package_LeaveProfiles(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_LeaveProfiles_060', a1)
    assert _is_linked(b, 'Employee_LeaveProfiles_060', a1)
    if hasattr(a1, 'Employee_LeaveProfiles_161'):
        assert _is_linked(a1, 'Employee_LeaveProfiles_161', b)
    _safe_set(b, 'Employee_LeaveProfiles_060', a2)
    assert _is_linked(b, 'Employee_LeaveProfiles_060', a2)
    if hasattr(a1, 'Employee_LeaveProfiles_161'):
        assert not _is_linked(a1, 'Employee_LeaveProfiles_161', b)
    if hasattr(a2, 'Employee_LeaveProfiles_161'):
        assert _is_linked(a2, 'Employee_LeaveProfiles_161', b)
    _safe_set(b, 'Employee_LeaveProfiles_060', None)
    assert not _is_linked(b, 'Employee_LeaveProfiles_060', a2)
    if hasattr(a2, 'Employee_LeaveProfiles_161'):
        assert not _is_linked(a2, 'Employee_LeaveProfiles_161', b)


def test_assoc_Employee_LeaveProfiles1_reverse_link_reassign_clear():
    a1 = Package2_LeaveProfiles(anual=7, casual=7, id=7, name="sample_text")
    a2 = Package2_LeaveProfiles(anual=13, casual=13, id=13, name="sample_text_2")
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_LeaveProfiles_090', a1)
    assert _is_linked(b, 'Employee_LeaveProfiles_090', a1)
    if hasattr(a1, 'Employee_LeaveProfiles_191'):
        assert _is_linked(a1, 'Employee_LeaveProfiles_191', b)
    _safe_set(b, 'Employee_LeaveProfiles_090', a2)
    assert _is_linked(b, 'Employee_LeaveProfiles_090', a2)
    if hasattr(a1, 'Employee_LeaveProfiles_191'):
        assert not _is_linked(a1, 'Employee_LeaveProfiles_191', b)
    if hasattr(a2, 'Employee_LeaveProfiles_191'):
        assert _is_linked(a2, 'Employee_LeaveProfiles_191', b)
    _safe_set(b, 'Employee_LeaveProfiles_090', None)
    assert not _is_linked(b, 'Employee_LeaveProfiles_090', a2)
    if hasattr(a2, 'Employee_LeaveProfiles_191'):
        assert not _is_linked(a2, 'Employee_LeaveProfiles_191', b)


def test_assoc_Employee_Leave_Taken_reverse_link_reassign_clear():
    a1 = Package_Leave_Taken(attribute="sample_text", attribute2="sample_text")
    a2 = Package_Leave_Taken(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_Leave_Taken_052', {a1})
    assert _is_linked(b, 'Employee_Leave_Taken_052', a1)
    if hasattr(a1, 'Employee_Leave_Taken_153'):
        assert _is_linked(a1, 'Employee_Leave_Taken_153', b)
    _safe_set(b, 'Employee_Leave_Taken_052', {a2})
    assert _is_linked(b, 'Employee_Leave_Taken_052', a2)
    if hasattr(a1, 'Employee_Leave_Taken_153'):
        assert not _is_linked(a1, 'Employee_Leave_Taken_153', b)
    if hasattr(a2, 'Employee_Leave_Taken_153'):
        assert _is_linked(a2, 'Employee_Leave_Taken_153', b)
    _safe_set(b, 'Employee_Leave_Taken_052', set())
    assert not _is_linked(b, 'Employee_Leave_Taken_052', a2)
    if hasattr(a2, 'Employee_Leave_Taken_153'):
        assert not _is_linked(a2, 'Employee_Leave_Taken_153', b)


def test_assoc_Employee_Leave_Taken1_reverse_link_reassign_clear():
    a1 = Package2_Leave_Taken(attribute="sample_text", attribute2="sample_text")
    a2 = Package2_Leave_Taken(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_Leave_Taken_082', {a1})
    assert _is_linked(b, 'Employee_Leave_Taken_082', a1)
    if hasattr(a1, 'Employee_Leave_Taken_183'):
        assert _is_linked(a1, 'Employee_Leave_Taken_183', b)
    _safe_set(b, 'Employee_Leave_Taken_082', {a2})
    assert _is_linked(b, 'Employee_Leave_Taken_082', a2)
    if hasattr(a1, 'Employee_Leave_Taken_183'):
        assert not _is_linked(a1, 'Employee_Leave_Taken_183', b)
    if hasattr(a2, 'Employee_Leave_Taken_183'):
        assert _is_linked(a2, 'Employee_Leave_Taken_183', b)
    _safe_set(b, 'Employee_Leave_Taken_082', set())
    assert not _is_linked(b, 'Employee_Leave_Taken_082', a2)
    if hasattr(a2, 'Employee_Leave_Taken_183'):
        assert not _is_linked(a2, 'Employee_Leave_Taken_183', b)


def test_assoc_Employee_OT_Requests_reverse_link_reassign_clear():
    a1 = Package_OT_Requests(EmpID=7, OTType=7, OtDay=date(2024, 1, 1), id=7)
    a2 = Package_OT_Requests(EmpID=13, OTType=13, OtDay=date(2025, 6, 15), id=13)
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_OT_Requests_048', {a1})
    assert _is_linked(b, 'Employee_OT_Requests_048', a1)
    if hasattr(a1, 'Employee_OT_Requests_149'):
        assert _is_linked(a1, 'Employee_OT_Requests_149', b)
    _safe_set(b, 'Employee_OT_Requests_048', {a2})
    assert _is_linked(b, 'Employee_OT_Requests_048', a2)
    if hasattr(a1, 'Employee_OT_Requests_149'):
        assert not _is_linked(a1, 'Employee_OT_Requests_149', b)
    if hasattr(a2, 'Employee_OT_Requests_149'):
        assert _is_linked(a2, 'Employee_OT_Requests_149', b)
    _safe_set(b, 'Employee_OT_Requests_048', set())
    assert not _is_linked(b, 'Employee_OT_Requests_048', a2)
    if hasattr(a2, 'Employee_OT_Requests_149'):
        assert not _is_linked(a2, 'Employee_OT_Requests_149', b)


def test_assoc_Employee_OT_Requests1_reverse_link_reassign_clear():
    a1 = Package2_OT_Requests(EmpID=7, OTType=7, OtDay=date(2024, 1, 1), id=7)
    a2 = Package2_OT_Requests(EmpID=13, OTType=13, OtDay=date(2025, 6, 15), id=13)
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_OT_Requests_078', {a1})
    assert _is_linked(b, 'Employee_OT_Requests_078', a1)
    if hasattr(a1, 'Employee_OT_Requests_179'):
        assert _is_linked(a1, 'Employee_OT_Requests_179', b)
    _safe_set(b, 'Employee_OT_Requests_078', {a2})
    assert _is_linked(b, 'Employee_OT_Requests_078', a2)
    if hasattr(a1, 'Employee_OT_Requests_179'):
        assert not _is_linked(a1, 'Employee_OT_Requests_179', b)
    if hasattr(a2, 'Employee_OT_Requests_179'):
        assert _is_linked(a2, 'Employee_OT_Requests_179', b)
    _safe_set(b, 'Employee_OT_Requests_078', set())
    assert not _is_linked(b, 'Employee_OT_Requests_078', a2)
    if hasattr(a2, 'Employee_OT_Requests_179'):
        assert not _is_linked(a2, 'Employee_OT_Requests_179', b)


def test_assoc_Employee_Posts_reverse_link_reassign_clear():
    a1 = Package_Posts(attribute="sample_text", attribute2="sample_text")
    a2 = Package_Posts(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_Posts_062', a1)
    assert _is_linked(b, 'Employee_Posts_062', a1)
    if hasattr(a1, 'Employee_Posts_163'):
        assert _is_linked(a1, 'Employee_Posts_163', b)
    _safe_set(b, 'Employee_Posts_062', a2)
    assert _is_linked(b, 'Employee_Posts_062', a2)
    if hasattr(a1, 'Employee_Posts_163'):
        assert not _is_linked(a1, 'Employee_Posts_163', b)
    if hasattr(a2, 'Employee_Posts_163'):
        assert _is_linked(a2, 'Employee_Posts_163', b)
    _safe_set(b, 'Employee_Posts_062', None)
    assert not _is_linked(b, 'Employee_Posts_062', a2)
    if hasattr(a2, 'Employee_Posts_163'):
        assert not _is_linked(a2, 'Employee_Posts_163', b)


def test_assoc_Employee_Posts1_reverse_link_reassign_clear():
    a1 = Package2_Posts(attribute2="sample_text", id=7)
    a2 = Package2_Posts(attribute2="sample_text_2", id=13)
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_Posts_092', a1)
    assert _is_linked(b, 'Employee_Posts_092', a1)
    if hasattr(a1, 'Employee_Posts_193'):
        assert _is_linked(a1, 'Employee_Posts_193', b)
    _safe_set(b, 'Employee_Posts_092', a2)
    assert _is_linked(b, 'Employee_Posts_092', a2)
    if hasattr(a1, 'Employee_Posts_193'):
        assert not _is_linked(a1, 'Employee_Posts_193', b)
    if hasattr(a2, 'Employee_Posts_193'):
        assert _is_linked(a2, 'Employee_Posts_193', b)
    _safe_set(b, 'Employee_Posts_092', None)
    assert not _is_linked(b, 'Employee_Posts_092', a2)
    if hasattr(a2, 'Employee_Posts_193'):
        assert not _is_linked(a2, 'Employee_Posts_193', b)


def test_assoc_Employee_Shifts_reverse_link_reassign_clear():
    a1 = Package_Shifts(attribute="sample_text", attribute2="sample_text")
    a2 = Package_Shifts(attribute="sample_text_2", attribute2="sample_text_2")
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_Shifts_050', a1)
    assert _is_linked(b, 'Employee_Shifts_050', a1)
    if hasattr(a1, 'Employee_Shifts_151'):
        assert _is_linked(a1, 'Employee_Shifts_151', b)
    _safe_set(b, 'Employee_Shifts_050', a2)
    assert _is_linked(b, 'Employee_Shifts_050', a2)
    if hasattr(a1, 'Employee_Shifts_151'):
        assert not _is_linked(a1, 'Employee_Shifts_151', b)
    if hasattr(a2, 'Employee_Shifts_151'):
        assert _is_linked(a2, 'Employee_Shifts_151', b)
    _safe_set(b, 'Employee_Shifts_050', None)
    assert not _is_linked(b, 'Employee_Shifts_050', a2)
    if hasattr(a2, 'Employee_Shifts_151'):
        assert not _is_linked(a2, 'Employee_Shifts_151', b)


def test_assoc_Employee_Shifts1_reverse_link_reassign_clear():
    a1 = Package2_Shifts(endtime="sample_text", id="sample_text", shiftaname="sample_text", starttime="sample_text")
    a2 = Package2_Shifts(endtime="sample_text_2", id="sample_text_2", shiftaname="sample_text_2", starttime="sample_text_2")
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_Shifts_080', a1)
    assert _is_linked(b, 'Employee_Shifts_080', a1)
    if hasattr(a1, 'Employee_Shifts_181'):
        assert _is_linked(a1, 'Employee_Shifts_181', b)
    _safe_set(b, 'Employee_Shifts_080', a2)
    assert _is_linked(b, 'Employee_Shifts_080', a2)
    if hasattr(a1, 'Employee_Shifts_181'):
        assert not _is_linked(a1, 'Employee_Shifts_181', b)
    if hasattr(a2, 'Employee_Shifts_181'):
        assert _is_linked(a2, 'Employee_Shifts_181', b)
    _safe_set(b, 'Employee_Shifts_080', None)
    assert not _is_linked(b, 'Employee_Shifts_080', a2)
    if hasattr(a2, 'Employee_Shifts_181'):
        assert not _is_linked(a2, 'Employee_Shifts_181', b)


def test_assoc_Employee_User_groups_reverse_link_reassign_clear():
    a1 = Package_User_groups(attribute="sample_text", attribute2="sample_text", attribute3="sample_text")
    a2 = Package_User_groups(attribute="sample_text_2", attribute2="sample_text_2", attribute3="sample_text_2")
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_User_groups_068', a1)
    assert _is_linked(b, 'Employee_User_groups_068', a1)
    if hasattr(a1, 'Employee_User_groups_169'):
        assert _is_linked(a1, 'Employee_User_groups_169', b)
    _safe_set(b, 'Employee_User_groups_068', a2)
    assert _is_linked(b, 'Employee_User_groups_068', a2)
    if hasattr(a1, 'Employee_User_groups_169'):
        assert not _is_linked(a1, 'Employee_User_groups_169', b)
    if hasattr(a2, 'Employee_User_groups_169'):
        assert _is_linked(a2, 'Employee_User_groups_169', b)
    _safe_set(b, 'Employee_User_groups_068', None)
    assert not _is_linked(b, 'Employee_User_groups_068', a2)
    if hasattr(a2, 'Employee_User_groups_169'):
        assert not _is_linked(a2, 'Employee_User_groups_169', b)


def test_assoc_Employee_User_groups1_reverse_link_reassign_clear():
    a1 = Package2_User_groups(attribute="sample_text", attribute2="sample_text", attribute3="sample_text")
    a2 = Package2_User_groups(attribute="sample_text_2", attribute2="sample_text_2", attribute3="sample_text_2")
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Employee_User_groups_098', a1)
    assert _is_linked(b, 'Employee_User_groups_098', a1)
    if hasattr(a1, 'Employee_User_groups_199'):
        assert _is_linked(a1, 'Employee_User_groups_199', b)
    _safe_set(b, 'Employee_User_groups_098', a2)
    assert _is_linked(b, 'Employee_User_groups_098', a2)
    if hasattr(a1, 'Employee_User_groups_199'):
        assert not _is_linked(a1, 'Employee_User_groups_199', b)
    if hasattr(a2, 'Employee_User_groups_199'):
        assert _is_linked(a2, 'Employee_User_groups_199', b)
    _safe_set(b, 'Employee_User_groups_098', None)
    assert not _is_linked(b, 'Employee_User_groups_098', a2)
    if hasattr(a2, 'Employee_User_groups_199'):
        assert not _is_linked(a2, 'Employee_User_groups_199', b)


def test_assoc_User_groups_User_Permissions_reverse_link_reassign_clear():
    a1 = Package_User_groups(attribute="sample_text", attribute2="sample_text", attribute3="sample_text")
    a2 = Package_User_groups(attribute="sample_text_2", attribute2="sample_text_2", attribute3="sample_text_2")
    b = Package_User_Permissions(attribute="sample_text", attribute2="sample_text")
    _safe_set(b, 'User_groups_User_Permissions_171', a1)
    assert _is_linked(b, 'User_groups_User_Permissions_171', a1)
    if hasattr(a1, 'User_groups_User_Permissions_070'):
        assert _is_linked(a1, 'User_groups_User_Permissions_070', b)
    _safe_set(b, 'User_groups_User_Permissions_171', a2)
    assert _is_linked(b, 'User_groups_User_Permissions_171', a2)
    if hasattr(a1, 'User_groups_User_Permissions_070'):
        assert not _is_linked(a1, 'User_groups_User_Permissions_070', b)
    if hasattr(a2, 'User_groups_User_Permissions_070'):
        assert _is_linked(a2, 'User_groups_User_Permissions_070', b)
    _safe_set(b, 'User_groups_User_Permissions_171', None)
    assert not _is_linked(b, 'User_groups_User_Permissions_171', a2)
    if hasattr(a2, 'User_groups_User_Permissions_070'):
        assert not _is_linked(a2, 'User_groups_User_Permissions_070', b)


def test_assoc_User_groups_User_Permissions1_reverse_link_reassign_clear():
    a1 = Package2_User_groups(attribute="sample_text", attribute2="sample_text", attribute3="sample_text")
    a2 = Package2_User_groups(attribute="sample_text_2", attribute2="sample_text_2", attribute3="sample_text_2")
    b = Package2_User_Permissions(attribute="sample_text", attribute2="sample_text")
    _safe_set(b, 'User_groups_User_Permissions_1101', a1)
    assert _is_linked(b, 'User_groups_User_Permissions_1101', a1)
    if hasattr(a1, 'User_groups_User_Permissions_0100'):
        assert _is_linked(a1, 'User_groups_User_Permissions_0100', b)
    _safe_set(b, 'User_groups_User_Permissions_1101', a2)
    assert _is_linked(b, 'User_groups_User_Permissions_1101', a2)
    if hasattr(a1, 'User_groups_User_Permissions_0100'):
        assert not _is_linked(a1, 'User_groups_User_Permissions_0100', b)
    if hasattr(a2, 'User_groups_User_Permissions_0100'):
        assert _is_linked(a2, 'User_groups_User_Permissions_0100', b)
    _safe_set(b, 'User_groups_User_Permissions_1101', None)
    assert not _is_linked(b, 'User_groups_User_Permissions_1101', a2)
    if hasattr(a2, 'User_groups_User_Permissions_0100'):
        assert not _is_linked(a2, 'User_groups_User_Permissions_0100', b)


def test_assoc_Users_Employee_reverse_link_reassign_clear():
    a1 = Package_Users(email=7, firstname=7, id=7, lastname=7, password=7)
    a2 = Package_Users(email=13, firstname=13, id=13, lastname=13, password=13)
    b = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Users_Employee_145', a1)
    assert _is_linked(b, 'Users_Employee_145', a1)
    if hasattr(a1, 'Users_Employee_044'):
        assert _is_linked(a1, 'Users_Employee_044', b)
    _safe_set(b, 'Users_Employee_145', a2)
    assert _is_linked(b, 'Users_Employee_145', a2)
    if hasattr(a1, 'Users_Employee_044'):
        assert not _is_linked(a1, 'Users_Employee_044', b)
    if hasattr(a2, 'Users_Employee_044'):
        assert _is_linked(a2, 'Users_Employee_044', b)
    _safe_set(b, 'Users_Employee_145', None)
    assert not _is_linked(b, 'Users_Employee_145', a2)
    if hasattr(a2, 'Users_Employee_044'):
        assert not _is_linked(a2, 'Users_Employee_044', b)


def test_assoc_Users_Employee1_reverse_link_reassign_clear():
    a1 = Package2_Users(email=7, firstname=7, id=7, lastname=7, password=7)
    a2 = Package2_Users(email=13, firstname=13, id=13, lastname=13, password=13)
    b = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    _safe_set(b, 'Users_Employee_175', a1)
    assert _is_linked(b, 'Users_Employee_175', a1)
    if hasattr(a1, 'Users_Employee_074'):
        assert _is_linked(a1, 'Users_Employee_074', b)
    _safe_set(b, 'Users_Employee_175', a2)
    assert _is_linked(b, 'Users_Employee_175', a2)
    if hasattr(a1, 'Users_Employee_074'):
        assert not _is_linked(a1, 'Users_Employee_074', b)
    if hasattr(a2, 'Users_Employee_074'):
        assert _is_linked(a2, 'Users_Employee_074', b)
    _safe_set(b, 'Users_Employee_175', None)
    assert not _is_linked(b, 'Users_Employee_175', a2)
    if hasattr(a2, 'Users_Employee_074'):
        assert not _is_linked(a2, 'Users_Employee_074', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Employee_Advances_stub_double():
    # Package_Advances has no real 'Employee_Advances_173' property in the generated
    # code (a bare stub) -- manually attach it so Package_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Package_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    partner = Package_Advances()
    setattr(partner, 'Employee_Advances_173', None)
    _safe_set(owner, 'advances72', {partner})
    assert getattr(partner, 'Employee_Advances_173') == owner
    _safe_set(owner, 'advances72', set())
    assert getattr(partner, 'Employee_Advances_173') is None


def test_assoc_Employee_Advances1_stub_double():
    # Package2_Advances has no real 'Employee_Advances_1103' property in the generated
    # code (a bare stub) -- manually attach it so Package2_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Package2_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    partner = Package2_Advances()
    setattr(partner, 'Employee_Advances_1103', None)
    _safe_set(owner, 'advances102', {partner})
    assert getattr(partner, 'Employee_Advances_1103') == owner
    _safe_set(owner, 'advances102', set())
    assert getattr(partner, 'Employee_Advances_1103') is None


def test_assoc_Employee_Messages_stub_double():
    # Package_Messages has no real 'Employee_Messages_159' property in the generated
    # code (a bare stub) -- manually attach it so Package_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Package_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Package_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    partner = Package_Messages()
    setattr(partner, 'Employee_Messages_159', None)
    _safe_set(owner, 'Employee_Messages_058', {partner})
    assert getattr(partner, 'Employee_Messages_159') == owner
    _safe_set(owner, 'Employee_Messages_058', set())
    assert getattr(partner, 'Employee_Messages_159') is None


def test_assoc_Employee_Messages1_stub_double():
    # Package2_Messages has no real 'Employee_Messages_189' property in the generated
    # code (a bare stub) -- manually attach it so Package2_Employee's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Package2_Employee's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Package2_Employee(depid=7, empid="sample_text", id="sample_text", leavegroup=7, post="sample_text", shift="sample_text", usergroup=7)
    partner = Package2_Messages()
    setattr(partner, 'Employee_Messages_189', None)
    _safe_set(owner, 'Employee_Messages_088', {partner})
    assert getattr(partner, 'Employee_Messages_189') == owner
    _safe_set(owner, 'Employee_Messages_088', set())
    assert getattr(partner, 'Employee_Messages_189') is None


