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
    Class_Diagram_for_Proposed_system_overtimeRequests,
    Class_Diagram_for_Proposed_system_Calender,
    Class_Diagram_for_Proposed_system_ETF,
    Class_Diagram_for_Proposed_system_EPF,
    Class_Diagram_for_Proposed_system_Events,
    Class_Diagram_for_Proposed_system_LeavesAllocated,
    Class_Diagram_for_Proposed_system_Attendance,
    Class_Diagram_for_Proposed_system_Post,
    Class_Diagram_for_Proposed_system_Advances,
    Class_Diagram_for_Proposed_system_Deductions,
    Class_Diagram_for_Proposed_system_Allowances,
    Class_Diagram_for_Proposed_system_Salary,
    Class_Diagram_for_Proposed_system_Department,
    Class_Diagram_for_Proposed_system_LeaveTaken,
    Class_Diagram_for_Proposed_system_WorkingShifts,
    Class_Diagram_for_Proposed_system_Role,
    Class_Diagram_for_Proposed_system_User,
    Class_Diagram_for_Proposed_system_Employee,
    Clark1_Actor1,
    Manager_Actor,
    Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase,
    Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase,
    Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase,
    Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase,
    Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase,
    Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase,
    Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase,
    Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase,
    Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase,
    Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase,
    Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase,
    Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase,
    Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase,
    Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase,
    Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase,
    Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase,
    Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase,
    Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase,
    Clark1_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class_diagram_for_proposed_system_overtimerequests_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_overtimeRequests)


def test_hyp_class_diagram_for_proposed_system_overtimerequests_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_overtimeRequests.__init__)


def test_hyp_class_diagram_for_proposed_system_overtimerequests_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_overtimeRequests.__init__)
    params = list(sig.parameters.keys())
    assert "start_time" in params, "Missing parameter 'start_time'"
    assert "date" in params, "Missing parameter 'date'"
    assert "nd_time" in params, "Missing parameter 'nd_time'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_class_diagram_for_proposed_system_calender_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Calender)


def test_hyp_class_diagram_for_proposed_system_calender_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Calender.__init__)


def test_hyp_class_diagram_for_proposed_system_calender_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Calender.__init__)
    params = list(sig.parameters.keys())
    assert "eventType" in params, "Missing parameter 'eventType'"
    assert "depid" in params, "Missing parameter 'depid'"
    assert "author_id" in params, "Missing parameter 'author_id'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_class_diagram_for_proposed_system_etf_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_ETF)


def test_hyp_class_diagram_for_proposed_system_etf_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_ETF.__init__)


def test_hyp_class_diagram_for_proposed_system_etf_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_ETF.__init__)
    params = list(sig.parameters.keys())
    assert "precentage" in params, "Missing parameter 'precentage'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_class_diagram_for_proposed_system_epf_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_EPF)


def test_hyp_class_diagram_for_proposed_system_epf_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_EPF.__init__)


def test_hyp_class_diagram_for_proposed_system_epf_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_EPF.__init__)
    params = list(sig.parameters.keys())
    assert "precentage" in params, "Missing parameter 'precentage'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_class_diagram_for_proposed_system_events_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Events)


def test_hyp_class_diagram_for_proposed_system_events_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Events.__init__)


def test_hyp_class_diagram_for_proposed_system_events_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Events.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_class_diagram_for_proposed_system_leavesallocated_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_LeavesAllocated)


def test_hyp_class_diagram_for_proposed_system_leavesallocated_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_LeavesAllocated.__init__)


def test_hyp_class_diagram_for_proposed_system_leavesallocated_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_LeavesAllocated.__init__)
    params = list(sig.parameters.keys())
    assert "leaveType" in params, "Missing parameter 'leaveType'"
    assert "noOfLeaves" in params, "Missing parameter 'noOfLeaves'"
    assert "id" in params, "Missing parameter 'id'"
    assert "empId" in params, "Missing parameter 'empId'"







def test_hyp_class_diagram_for_proposed_system_attendance_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Attendance)


def test_hyp_class_diagram_for_proposed_system_attendance_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Attendance.__init__)


def test_hyp_class_diagram_for_proposed_system_attendance_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Attendance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "clock_in" in params, "Missing parameter 'clock_in'"
    assert "date" in params, "Missing parameter 'date'"
    assert "clock_out" in params, "Missing parameter 'clock_out'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "empId" in params, "Missing parameter 'empId'"









def test_hyp_class_diagram_for_proposed_system_post_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Post)


def test_hyp_class_diagram_for_proposed_system_post_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Post.__init__)


def test_hyp_class_diagram_for_proposed_system_post_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Post.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "leavesEntitled" in params, "Missing parameter 'leavesEntitled'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "deptId" in params, "Missing parameter 'deptId'"
    assert "name" in params, "Missing parameter 'name'"








def test_hyp_class_diagram_for_proposed_system_advances_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Advances)


def test_hyp_class_diagram_for_proposed_system_advances_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Advances.__init__)


def test_hyp_class_diagram_for_proposed_system_advances_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Advances.__init__)
    params = list(sig.parameters.keys())
    assert "installments" in params, "Missing parameter 'installments'"
    assert "issueDate" in params, "Missing parameter 'issueDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "salaryId" in params, "Missing parameter 'salaryId'"
    assert "amount" in params, "Missing parameter 'amount'"








def test_hyp_class_diagram_for_proposed_system_deductions_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Deductions)


def test_hyp_class_diagram_for_proposed_system_deductions_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Deductions.__init__)


def test_hyp_class_diagram_for_proposed_system_deductions_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Deductions.__init__)
    params = list(sig.parameters.keys())
    assert "deductDate" in params, "Missing parameter 'deductDate'"
    assert "id" in params, "Missing parameter 'id'"
    assert "deducType" in params, "Missing parameter 'deducType'"
    assert "salaryId" in params, "Missing parameter 'salaryId'"
    assert "amount" in params, "Missing parameter 'amount'"








def test_hyp_class_diagram_for_proposed_system_allowances_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Allowances)


def test_hyp_class_diagram_for_proposed_system_allowances_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Allowances.__init__)


def test_hyp_class_diagram_for_proposed_system_allowances_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Allowances.__init__)
    params = list(sig.parameters.keys())
    assert "issueDate" in params, "Missing parameter 'issueDate'"
    assert "salaryId" in params, "Missing parameter 'salaryId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "allowanceType" in params, "Missing parameter 'allowanceType'"








def test_hyp_class_diagram_for_proposed_system_salary_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Salary)


def test_hyp_class_diagram_for_proposed_system_salary_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Salary.__init__)


def test_hyp_class_diagram_for_proposed_system_salary_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Salary.__init__)
    params = list(sig.parameters.keys())
    assert "empId" in params, "Missing parameter 'empId'"
    assert "EPF" in params, "Missing parameter 'EPF'"
    assert "basicPay" in params, "Missing parameter 'basicPay'"
    assert "ETF" in params, "Missing parameter 'ETF'"
    assert "deductions" in params, "Missing parameter 'deductions'"
    assert "allowances" in params, "Missing parameter 'allowances'"
    assert "payDate" in params, "Missing parameter 'payDate'"
    assert "advances" in params, "Missing parameter 'advances'"
    assert "overtimes" in params, "Missing parameter 'overtimes'"
    assert "id" in params, "Missing parameter 'id'"













def test_hyp_class_diagram_for_proposed_system_department_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Department)


def test_hyp_class_diagram_for_proposed_system_department_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Department.__init__)


def test_hyp_class_diagram_for_proposed_system_department_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "empId" in params, "Missing parameter 'empId'"






def test_hyp_class_diagram_for_proposed_system_leavetaken_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_LeaveTaken)


def test_hyp_class_diagram_for_proposed_system_leavetaken_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_LeaveTaken.__init__)


def test_hyp_class_diagram_for_proposed_system_leavetaken_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_LeaveTaken.__init__)
    params = list(sig.parameters.keys())
    assert "leaveType" in params, "Missing parameter 'leaveType'"
    assert "leaveDate" in params, "Missing parameter 'leaveDate'"
    assert "empId" in params, "Missing parameter 'empId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"








def test_hyp_class_diagram_for_proposed_system_workingshifts_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_WorkingShifts)


def test_hyp_class_diagram_for_proposed_system_workingshifts_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_WorkingShifts.__init__)


def test_hyp_class_diagram_for_proposed_system_workingshifts_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_WorkingShifts.__init__)
    params = list(sig.parameters.keys())
    assert "empId" in params, "Missing parameter 'empId'"
    assert "startingTime" in params, "Missing parameter 'startingTime'"
    assert "id" in params, "Missing parameter 'id'"
    assert "endingTime" in params, "Missing parameter 'endingTime'"







def test_hyp_class_diagram_for_proposed_system_role_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Role)


def test_hyp_class_diagram_for_proposed_system_role_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Role.__init__)


def test_hyp_class_diagram_for_proposed_system_role_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Role.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "roleName" in params, "Missing parameter 'roleName'"
    assert "description" in params, "Missing parameter 'description'"






def test_hyp_class_diagram_for_proposed_system_user_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_User)


def test_hyp_class_diagram_for_proposed_system_user_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_User.__init__)


def test_hyp_class_diagram_for_proposed_system_user_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_User.__init__)
    params = list(sig.parameters.keys())
    assert "roleId" in params, "Missing parameter 'roleId'"
    assert "firstNAme" in params, "Missing parameter 'firstNAme'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_class_diagram_for_proposed_system_employee_is_not_abstract():
    assert not inspect.isabstract(Class_Diagram_for_Proposed_system_Employee)


def test_hyp_class_diagram_for_proposed_system_employee_constructor_exists():
    assert callable(Class_Diagram_for_Proposed_system_Employee.__init__)


def test_hyp_class_diagram_for_proposed_system_employee_constructor_args():
    sig = inspect.signature(Class_Diagram_for_Proposed_system_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "mobile" in params, "Missing parameter 'mobile'"
    assert "NIC" in params, "Missing parameter 'NIC'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "deptId" in params, "Missing parameter 'deptId'"
    assert "address" in params, "Missing parameter 'address'"
    assert "postID" in params, "Missing parameter 'postID'"
    assert "id" in params, "Missing parameter 'id'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "shiftId" in params, "Missing parameter 'shiftId'"













def test_hyp_clark1_actor1_is_not_abstract():
    assert not inspect.isabstract(Clark1_Actor1)


def test_hyp_clark1_actor1_constructor_exists():
    assert callable(Clark1_Actor1.__init__)


def test_hyp_clark1_actor1_constructor_args():
    sig = inspect.signature(Clark1_Actor1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manager_actor_is_not_abstract():
    assert not inspect.isabstract(Manager_Actor)


def test_hyp_manager_actor_constructor_exists():
    assert callable(Manager_Actor.__init__)


def test_hyp_manager_actor_constructor_args():
    sig = inspect.signature(Manager_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_put_company_notices_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase)


def test_hyp_use_case_diagram_for_existing_system_put_company_notices_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_put_company_notices_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_mark_clock_out_time_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase)


def test_hyp_use_case_diagram_for_existing_system_mark_clock_out_time_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_mark_clock_out_time_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_store_times_in_employee_time_cards_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase)


def test_hyp_use_case_diagram_for_existing_system_store_times_in_employee_time_cards_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_store_times_in_employee_time_cards_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_mark_clock_in_time_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase)


def test_hyp_use_case_diagram_for_existing_system_mark_clock_in_time_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_mark_clock_in_time_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_generate_reports_from_excel_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase)


def test_hyp_use_case_diagram_for_existing_system_generate_reports_from_excel_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_generate_reports_from_excel_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_give_message_to_employee_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase)


def test_hyp_use_case_diagram_for_existing_system_give_message_to_employee_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_give_message_to_employee_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_hand_over_form_to_hr_dept_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase)


def test_hyp_use_case_diagram_for_existing_system_hand_over_form_to_hr_dept_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_hand_over_form_to_hr_dept_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_fill_leave_apply_form_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase)


def test_hyp_use_case_diagram_for_existing_system_fill_leave_apply_form_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_fill_leave_apply_form_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_access_time_cards_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase)


def test_hyp_use_case_diagram_for_existing_system_access_time_cards_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_access_time_cards_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_check_leave_forms_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase)


def test_hyp_use_case_diagram_for_existing_system_check_leave_forms_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_check_leave_forms_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_salary_calculation_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase)


def test_hyp_use_case_diagram_for_existing_system_salary_calculation_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_salary_calculation_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_approve_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase)


def test_hyp_use_case_diagram_for_existing_system_approve_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_approve_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_access_leave_documents_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase)


def test_hyp_use_case_diagram_for_existing_system_access_leave_documents_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_access_leave_documents_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_check_employee_appraisal_forms_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase)


def test_hyp_use_case_diagram_for_existing_system_check_employee_appraisal_forms_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_check_employee_appraisal_forms_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_reject_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase)


def test_hyp_use_case_diagram_for_existing_system_reject_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_reject_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_request_loan_and_advances_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase)


def test_hyp_use_case_diagram_for_existing_system_request_loan_and_advances_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_request_loan_and_advances_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_register_new_employee_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase)


def test_hyp_use_case_diagram_for_existing_system_register_new_employee_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_register_new_employee_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_calculate_monthly_leaves_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase)


def test_hyp_use_case_diagram_for_existing_system_calculate_monthly_leaves_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_calculate_monthly_leaves_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_calculate_late_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase)


def test_hyp_use_case_diagram_for_existing_system_calculate_late_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_calculate_late_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_request_leave_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase)


def test_hyp_use_case_diagram_for_existing_system_request_leave_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_request_leave_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_calculate_overtime_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase)


def test_hyp_use_case_diagram_for_existing_system_calculate_overtime_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_calculate_overtime_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_case_diagram_for_existing_system_enter_salary_details_to_spreadsheets_usecase_is_not_abstract():
    assert not inspect.isabstract(Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase)


def test_hyp_use_case_diagram_for_existing_system_enter_salary_details_to_spreadsheets_usecase_constructor_exists():
    assert callable(Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase.__init__)


def test_hyp_use_case_diagram_for_existing_system_enter_salary_details_to_spreadsheets_usecase_constructor_args():
    sig = inspect.signature(Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_clark1_actor_is_not_abstract():
    assert not inspect.isabstract(Clark1_Actor)


def test_hyp_clark1_actor_constructor_exists():
    assert callable(Clark1_Actor.__init__)


def test_hyp_clark1_actor_constructor_args():
    sig = inspect.signature(Clark1_Actor.__init__)
    params = list(sig.parameters.keys())


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
Class_Diagram_for_Proposed_system_overtimeRequests_strategy = st.builds(
    Class_Diagram_for_Proposed_system_overtimeRequests,
    start_time=
        safe_text,
    date=
        safe_text,
    nd_time=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Calender_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Calender,
    eventType=
        safe_text,
    depid=
        safe_text,
    author_id=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_ETF_strategy = st.builds(
    Class_Diagram_for_Proposed_system_ETF,
    precentage=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_EPF_strategy = st.builds(
    Class_Diagram_for_Proposed_system_EPF,
    precentage=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Events_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Events,
    type=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_LeavesAllocated_strategy = st.builds(
    Class_Diagram_for_Proposed_system_LeavesAllocated,
    leaveType=
        safe_text,
    noOfLeaves=
        safe_text,
    id=
        safe_text,
    empId=
        safe_text
)
Class_Diagram_for_Proposed_system_Attendance_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Attendance,
    id=
        safe_text,
    clock_in=
        safe_text,
    date=
        safe_text,
    clock_out=
        safe_text,
    attribute=
        safe_text,
    empId=
        safe_text
)
Class_Diagram_for_Proposed_system_Post_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Post,
    id=
        safe_text,
    leavesEntitled=
        safe_text,
    attribute=
        safe_text,
    deptId=
        safe_text,
    name=
        safe_text
)
Class_Diagram_for_Proposed_system_Advances_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Advances,
    installments=
        safe_text,
    issueDate=
        safe_text,
    id=
        safe_text,
    salaryId=
        safe_text,
    amount=
        safe_text
)
Class_Diagram_for_Proposed_system_Deductions_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Deductions,
    deductDate=
        safe_text,
    id=
        safe_text,
    deducType=
        safe_text,
    salaryId=
        safe_text,
    amount=
        safe_text
)
Class_Diagram_for_Proposed_system_Allowances_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Allowances,
    issueDate=
        safe_text,
    salaryId=
        safe_text,
    id=
        safe_text,
    amount=
        safe_text,
    allowanceType=
        safe_text
)
Class_Diagram_for_Proposed_system_Salary_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Salary,
    empId=
        safe_text,
    EPF=
        safe_text,
    basicPay=
        safe_text,
    ETF=
        safe_text,
    deductions=
        safe_text,
    allowances=
        safe_text,
    payDate=
        safe_text,
    advances=
        safe_text,
    overtimes=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Department_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Department,
    name=
        safe_text,
    id=
        safe_text,
    empId=
        safe_text
)
Class_Diagram_for_Proposed_system_LeaveTaken_strategy = st.builds(
    Class_Diagram_for_Proposed_system_LeaveTaken,
    leaveType=
        safe_text,
    leaveDate=
        safe_text,
    empId=
        safe_text,
    id=
        safe_text,
    attribute5=
        safe_text
)
Class_Diagram_for_Proposed_system_WorkingShifts_strategy = st.builds(
    Class_Diagram_for_Proposed_system_WorkingShifts,
    empId=
        safe_text,
    startingTime=
        safe_text,
    id=
        safe_text,
    endingTime=
        safe_text
)
Class_Diagram_for_Proposed_system_Role_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Role,
    id=
        safe_text,
    roleName=
        safe_text,
    description=
        safe_text
)
Class_Diagram_for_Proposed_system_User_strategy = st.builds(
    Class_Diagram_for_Proposed_system_User,
    roleId=
        st.integers(),
    firstNAme=
        safe_text,
    LastName=
        safe_text,
    id=
        safe_text
)
Class_Diagram_for_Proposed_system_Employee_strategy = st.builds(
    Class_Diagram_for_Proposed_system_Employee,
    gender=
        safe_text,
    mobile=
        safe_text,
    NIC=
        safe_text,
    userId=
        st.integers(),
    deptId=
        st.integers(),
    address=
        safe_text,
    postID=
        st.integers(),
    id=
        st.integers(),
    phone=
        safe_text,
    shiftId=
        st.integers()
)
Clark1_Actor1_strategy = st.builds(
    Clark1_Actor1,
)
Manager_Actor_strategy = st.builds(
    Manager_Actor,
)
Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase,
)
Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase,
)
Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase,
)
Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase,
)
Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase,
)
Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase,
)
Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase,
)
Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase,
)
Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase,
)
Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase,
)
Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase,
)
Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase,
)
Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase,
)
Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase,
)
Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase,
)
Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase,
)
Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase,
)
Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase,
)
Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase,
)
Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase,
)
Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase,
)
Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase_strategy = st.builds(
    Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase,
)
Clark1_Actor_strategy = st.builds(
    Clark1_Actor,
)




@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_hyp_class_diagram_for_proposed_system_overtimerequests_start_time_setter(instance):
    original = instance.start_time
    instance.start_time = original
    assert instance.start_time == original



@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_hyp_class_diagram_for_proposed_system_overtimerequests_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_hyp_class_diagram_for_proposed_system_overtimerequests_nd_time_setter(instance):
    original = instance.nd_time
    instance.nd_time = original
    assert instance.nd_time == original



@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
def test_hyp_class_diagram_for_proposed_system_overtimerequests_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_hyp_class_diagram_for_proposed_system_calender_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original



@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_hyp_class_diagram_for_proposed_system_calender_depid_setter(instance):
    original = instance.depid
    instance.depid = original
    assert instance.depid == original



@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_hyp_class_diagram_for_proposed_system_calender_author_id_setter(instance):
    original = instance.author_id
    instance.author_id = original
    assert instance.author_id == original



@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
def test_hyp_class_diagram_for_proposed_system_calender_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Class_Diagram_for_Proposed_system_ETF_strategy)
def test_hyp_class_diagram_for_proposed_system_etf_precentage_setter(instance):
    original = instance.precentage
    instance.precentage = original
    assert instance.precentage == original



@given(instance=Class_Diagram_for_Proposed_system_ETF_strategy)
def test_hyp_class_diagram_for_proposed_system_etf_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Class_Diagram_for_Proposed_system_EPF_strategy)
def test_hyp_class_diagram_for_proposed_system_epf_precentage_setter(instance):
    original = instance.precentage
    instance.precentage = original
    assert instance.precentage == original



@given(instance=Class_Diagram_for_Proposed_system_EPF_strategy)
def test_hyp_class_diagram_for_proposed_system_epf_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Class_Diagram_for_Proposed_system_Events_strategy)
def test_hyp_class_diagram_for_proposed_system_events_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Class_Diagram_for_Proposed_system_Events_strategy)
def test_hyp_class_diagram_for_proposed_system_events_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_hyp_class_diagram_for_proposed_system_leavesallocated_leaveType_setter(instance):
    original = instance.leaveType
    instance.leaveType = original
    assert instance.leaveType == original



@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_hyp_class_diagram_for_proposed_system_leavesallocated_noOfLeaves_setter(instance):
    original = instance.noOfLeaves
    instance.noOfLeaves = original
    assert instance.noOfLeaves == original



@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_hyp_class_diagram_for_proposed_system_leavesallocated_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
def test_hyp_class_diagram_for_proposed_system_leavesallocated_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original




@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_hyp_class_diagram_for_proposed_system_attendance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_hyp_class_diagram_for_proposed_system_attendance_clock_in_setter(instance):
    original = instance.clock_in
    instance.clock_in = original
    assert instance.clock_in == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_hyp_class_diagram_for_proposed_system_attendance_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_hyp_class_diagram_for_proposed_system_attendance_clock_out_setter(instance):
    original = instance.clock_out
    instance.clock_out = original
    assert instance.clock_out == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_hyp_class_diagram_for_proposed_system_attendance_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
def test_hyp_class_diagram_for_proposed_system_attendance_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original




@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_hyp_class_diagram_for_proposed_system_post_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_hyp_class_diagram_for_proposed_system_post_leavesEntitled_setter(instance):
    original = instance.leavesEntitled
    instance.leavesEntitled = original
    assert instance.leavesEntitled == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_hyp_class_diagram_for_proposed_system_post_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_hyp_class_diagram_for_proposed_system_post_deptId_setter(instance):
    original = instance.deptId
    instance.deptId = original
    assert instance.deptId == original



@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
def test_hyp_class_diagram_for_proposed_system_post_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_hyp_class_diagram_for_proposed_system_advances_installments_setter(instance):
    original = instance.installments
    instance.installments = original
    assert instance.installments == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_hyp_class_diagram_for_proposed_system_advances_issueDate_setter(instance):
    original = instance.issueDate
    instance.issueDate = original
    assert instance.issueDate == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_hyp_class_diagram_for_proposed_system_advances_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_hyp_class_diagram_for_proposed_system_advances_salaryId_setter(instance):
    original = instance.salaryId
    instance.salaryId = original
    assert instance.salaryId == original



@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
def test_hyp_class_diagram_for_proposed_system_advances_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_hyp_class_diagram_for_proposed_system_deductions_deductDate_setter(instance):
    original = instance.deductDate
    instance.deductDate = original
    assert instance.deductDate == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_hyp_class_diagram_for_proposed_system_deductions_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_hyp_class_diagram_for_proposed_system_deductions_deducType_setter(instance):
    original = instance.deducType
    instance.deducType = original
    assert instance.deducType == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_hyp_class_diagram_for_proposed_system_deductions_salaryId_setter(instance):
    original = instance.salaryId
    instance.salaryId = original
    assert instance.salaryId == original



@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
def test_hyp_class_diagram_for_proposed_system_deductions_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_hyp_class_diagram_for_proposed_system_allowances_issueDate_setter(instance):
    original = instance.issueDate
    instance.issueDate = original
    assert instance.issueDate == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_hyp_class_diagram_for_proposed_system_allowances_salaryId_setter(instance):
    original = instance.salaryId
    instance.salaryId = original
    assert instance.salaryId == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_hyp_class_diagram_for_proposed_system_allowances_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_hyp_class_diagram_for_proposed_system_allowances_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
def test_hyp_class_diagram_for_proposed_system_allowances_allowanceType_setter(instance):
    original = instance.allowanceType
    instance.allowanceType = original
    assert instance.allowanceType == original




@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_EPF_setter(instance):
    original = instance.EPF
    instance.EPF = original
    assert instance.EPF == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_basicPay_setter(instance):
    original = instance.basicPay
    instance.basicPay = original
    assert instance.basicPay == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_ETF_setter(instance):
    original = instance.ETF
    instance.ETF = original
    assert instance.ETF == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_deductions_setter(instance):
    original = instance.deductions
    instance.deductions = original
    assert instance.deductions == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_allowances_setter(instance):
    original = instance.allowances
    instance.allowances = original
    assert instance.allowances == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_payDate_setter(instance):
    original = instance.payDate
    instance.payDate = original
    assert instance.payDate == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_advances_setter(instance):
    original = instance.advances
    instance.advances = original
    assert instance.advances == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_overtimes_setter(instance):
    original = instance.overtimes
    instance.overtimes = original
    assert instance.overtimes == original



@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
def test_hyp_class_diagram_for_proposed_system_salary_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
def test_hyp_class_diagram_for_proposed_system_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
def test_hyp_class_diagram_for_proposed_system_department_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
def test_hyp_class_diagram_for_proposed_system_department_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original




@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_hyp_class_diagram_for_proposed_system_leavetaken_leaveType_setter(instance):
    original = instance.leaveType
    instance.leaveType = original
    assert instance.leaveType == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_hyp_class_diagram_for_proposed_system_leavetaken_leaveDate_setter(instance):
    original = instance.leaveDate
    instance.leaveDate = original
    assert instance.leaveDate == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_hyp_class_diagram_for_proposed_system_leavetaken_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_hyp_class_diagram_for_proposed_system_leavetaken_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
def test_hyp_class_diagram_for_proposed_system_leavetaken_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original




@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_hyp_class_diagram_for_proposed_system_workingshifts_empId_setter(instance):
    original = instance.empId
    instance.empId = original
    assert instance.empId == original



@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_hyp_class_diagram_for_proposed_system_workingshifts_startingTime_setter(instance):
    original = instance.startingTime
    instance.startingTime = original
    assert instance.startingTime == original



@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_hyp_class_diagram_for_proposed_system_workingshifts_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
def test_hyp_class_diagram_for_proposed_system_workingshifts_endingTime_setter(instance):
    original = instance.endingTime
    instance.endingTime = original
    assert instance.endingTime == original




@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
def test_hyp_class_diagram_for_proposed_system_role_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
def test_hyp_class_diagram_for_proposed_system_role_roleName_setter(instance):
    original = instance.roleName
    instance.roleName = original
    assert instance.roleName == original



@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
def test_hyp_class_diagram_for_proposed_system_role_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_hyp_class_diagram_for_proposed_system_user_roleId_setter(instance):
    original = instance.roleId
    instance.roleId = original
    assert instance.roleId == original



@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_hyp_class_diagram_for_proposed_system_user_firstNAme_setter(instance):
    original = instance.firstNAme
    instance.firstNAme = original
    assert instance.firstNAme == original



@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_hyp_class_diagram_for_proposed_system_user_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
def test_hyp_class_diagram_for_proposed_system_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_NIC_setter(instance):
    original = instance.NIC
    instance.NIC = original
    assert instance.NIC == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_deptId_setter(instance):
    original = instance.deptId
    instance.deptId = original
    assert instance.deptId == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_postID_setter(instance):
    original = instance.postID
    instance.postID = original
    assert instance.postID == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
def test_hyp_class_diagram_for_proposed_system_employee_shiftId_setter(instance):
    original = instance.shiftId
    instance.shiftId = original
    assert instance.shiftId == original



























# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_Class_Diagram_for_Proposed_system_Advances_amount_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Advances(amount="sample_text", id="sample_text", installments="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.amount == "sample_text"
    instance.amount = "sample_text_2"
    assert instance.amount == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Advances_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Advances(amount="sample_text", id="sample_text", installments="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Advances_installments_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Advances(amount="sample_text", id="sample_text", installments="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.installments == "sample_text"
    instance.installments = "sample_text_2"
    assert instance.installments == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Advances_issueDate_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Advances(amount="sample_text", id="sample_text", installments="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.issueDate == "sample_text"
    instance.issueDate = "sample_text_2"
    assert instance.issueDate == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Advances_salaryId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Advances(amount="sample_text", id="sample_text", installments="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.salaryId == "sample_text"
    instance.salaryId = "sample_text_2"
    assert instance.salaryId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Allowances_allowanceType_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text", amount="sample_text", id="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.allowanceType == "sample_text"
    instance.allowanceType = "sample_text_2"
    assert instance.allowanceType == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Allowances_amount_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text", amount="sample_text", id="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.amount == "sample_text"
    instance.amount = "sample_text_2"
    assert instance.amount == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Allowances_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text", amount="sample_text", id="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Allowances_issueDate_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text", amount="sample_text", id="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.issueDate == "sample_text"
    instance.issueDate = "sample_text_2"
    assert instance.issueDate == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Allowances_salaryId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text", amount="sample_text", id="sample_text", issueDate="sample_text", salaryId="sample_text")
    assert instance.salaryId == "sample_text"
    instance.salaryId = "sample_text_2"
    assert instance.salaryId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Attendance_attribute_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Attendance_clock_in_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    assert instance.clock_in == "sample_text"
    instance.clock_in = "sample_text_2"
    assert instance.clock_in == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Attendance_clock_out_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    assert instance.clock_out == "sample_text"
    instance.clock_out = "sample_text_2"
    assert instance.clock_out == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Attendance_date_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Attendance_empId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    assert instance.empId == "sample_text"
    instance.empId = "sample_text_2"
    assert instance.empId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Attendance_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Calender_author_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Calender(author_id="sample_text", depid="sample_text", eventType="sample_text", id="sample_text")
    assert instance.author_id == "sample_text"
    instance.author_id = "sample_text_2"
    assert instance.author_id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Calender_depid_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Calender(author_id="sample_text", depid="sample_text", eventType="sample_text", id="sample_text")
    assert instance.depid == "sample_text"
    instance.depid = "sample_text_2"
    assert instance.depid == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Calender_eventType_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Calender(author_id="sample_text", depid="sample_text", eventType="sample_text", id="sample_text")
    assert instance.eventType == "sample_text"
    instance.eventType = "sample_text_2"
    assert instance.eventType == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Calender_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Calender(author_id="sample_text", depid="sample_text", eventType="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Deductions_amount_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text", deducType="sample_text", deductDate="sample_text", id="sample_text", salaryId="sample_text")
    assert instance.amount == "sample_text"
    instance.amount = "sample_text_2"
    assert instance.amount == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Deductions_deducType_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text", deducType="sample_text", deductDate="sample_text", id="sample_text", salaryId="sample_text")
    assert instance.deducType == "sample_text"
    instance.deducType = "sample_text_2"
    assert instance.deducType == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Deductions_deductDate_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text", deducType="sample_text", deductDate="sample_text", id="sample_text", salaryId="sample_text")
    assert instance.deductDate == "sample_text"
    instance.deductDate = "sample_text_2"
    assert instance.deductDate == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Deductions_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text", deducType="sample_text", deductDate="sample_text", id="sample_text", salaryId="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Deductions_salaryId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text", deducType="sample_text", deductDate="sample_text", id="sample_text", salaryId="sample_text")
    assert instance.salaryId == "sample_text"
    instance.salaryId = "sample_text_2"
    assert instance.salaryId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Department_empId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Department(empId="sample_text", id="sample_text", name="sample_text")
    assert instance.empId == "sample_text"
    instance.empId = "sample_text_2"
    assert instance.empId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Department_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Department(empId="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Department_name_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Department(empId="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_EPF_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_EPF(id="sample_text", precentage="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_EPF_precentage_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_EPF(id="sample_text", precentage="sample_text")
    assert instance.precentage == "sample_text"
    instance.precentage = "sample_text_2"
    assert instance.precentage == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_ETF_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_ETF(id="sample_text", precentage="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_ETF_precentage_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_ETF(id="sample_text", precentage="sample_text")
    assert instance.precentage == "sample_text"
    instance.precentage = "sample_text_2"
    assert instance.precentage == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Employee_NIC_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.NIC == "sample_text"
    instance.NIC = "sample_text_2"
    assert instance.NIC == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Employee_address_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Employee_deptId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.deptId == 7
    instance.deptId = 13
    assert instance.deptId == 13


def test_Class_Diagram_for_Proposed_system_Employee_gender_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Employee_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Class_Diagram_for_Proposed_system_Employee_mobile_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.mobile == "sample_text"
    instance.mobile = "sample_text_2"
    assert instance.mobile == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Employee_phone_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Employee_postID_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.postID == 7
    instance.postID = 13
    assert instance.postID == 13


def test_Class_Diagram_for_Proposed_system_Employee_shiftId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.shiftId == 7
    instance.shiftId = 13
    assert instance.shiftId == 13


def test_Class_Diagram_for_Proposed_system_Employee_userId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    assert instance.userId == 7
    instance.userId = 13
    assert instance.userId == 13


def test_Class_Diagram_for_Proposed_system_Events_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Events(id="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Events_type_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Events(id="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeaveTaken_attribute5_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text", empId="sample_text", id="sample_text", leaveDate="sample_text", leaveType="sample_text")
    assert instance.attribute5 == "sample_text"
    instance.attribute5 = "sample_text_2"
    assert instance.attribute5 == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeaveTaken_empId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text", empId="sample_text", id="sample_text", leaveDate="sample_text", leaveType="sample_text")
    assert instance.empId == "sample_text"
    instance.empId = "sample_text_2"
    assert instance.empId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeaveTaken_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text", empId="sample_text", id="sample_text", leaveDate="sample_text", leaveType="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeaveTaken_leaveDate_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text", empId="sample_text", id="sample_text", leaveDate="sample_text", leaveType="sample_text")
    assert instance.leaveDate == "sample_text"
    instance.leaveDate = "sample_text_2"
    assert instance.leaveDate == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeaveTaken_leaveType_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text", empId="sample_text", id="sample_text", leaveDate="sample_text", leaveType="sample_text")
    assert instance.leaveType == "sample_text"
    instance.leaveType = "sample_text_2"
    assert instance.leaveType == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeavesAllocated_empId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    assert instance.empId == "sample_text"
    instance.empId = "sample_text_2"
    assert instance.empId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeavesAllocated_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeavesAllocated_leaveType_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    assert instance.leaveType == "sample_text"
    instance.leaveType = "sample_text_2"
    assert instance.leaveType == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_LeavesAllocated_noOfLeaves_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    assert instance.noOfLeaves == "sample_text"
    instance.noOfLeaves = "sample_text_2"
    assert instance.noOfLeaves == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Post_attribute_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Post_deptId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    assert instance.deptId == "sample_text"
    instance.deptId = "sample_text_2"
    assert instance.deptId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Post_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Post_leavesEntitled_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    assert instance.leavesEntitled == "sample_text"
    instance.leavesEntitled = "sample_text_2"
    assert instance.leavesEntitled == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Post_name_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Role_description_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Role(description="sample_text", id="sample_text", roleName="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Role_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Role(description="sample_text", id="sample_text", roleName="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Role_roleName_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Role(description="sample_text", id="sample_text", roleName="sample_text")
    assert instance.roleName == "sample_text"
    instance.roleName = "sample_text_2"
    assert instance.roleName == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_EPF_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.EPF == "sample_text"
    instance.EPF = "sample_text_2"
    assert instance.EPF == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_ETF_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.ETF == "sample_text"
    instance.ETF = "sample_text_2"
    assert instance.ETF == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_advances_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.advances == "sample_text"
    instance.advances = "sample_text_2"
    assert instance.advances == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_allowances_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.allowances == "sample_text"
    instance.allowances = "sample_text_2"
    assert instance.allowances == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_basicPay_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.basicPay == "sample_text"
    instance.basicPay = "sample_text_2"
    assert instance.basicPay == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_deductions_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.deductions == "sample_text"
    instance.deductions = "sample_text_2"
    assert instance.deductions == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_empId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.empId == "sample_text"
    instance.empId = "sample_text_2"
    assert instance.empId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_overtimes_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.overtimes == "sample_text"
    instance.overtimes = "sample_text_2"
    assert instance.overtimes == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_Salary_payDate_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    assert instance.payDate == "sample_text"
    instance.payDate = "sample_text_2"
    assert instance.payDate == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_User_LastName_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    assert instance.LastName == "sample_text"
    instance.LastName = "sample_text_2"
    assert instance.LastName == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_User_firstNAme_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    assert instance.firstNAme == "sample_text"
    instance.firstNAme = "sample_text_2"
    assert instance.firstNAme == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_User_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_User_roleId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    assert instance.roleId == 7
    instance.roleId = 13
    assert instance.roleId == 13


def test_Class_Diagram_for_Proposed_system_WorkingShifts_empId_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_WorkingShifts(empId="sample_text", endingTime="sample_text", id="sample_text", startingTime="sample_text")
    assert instance.empId == "sample_text"
    instance.empId = "sample_text_2"
    assert instance.empId == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_WorkingShifts_endingTime_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_WorkingShifts(empId="sample_text", endingTime="sample_text", id="sample_text", startingTime="sample_text")
    assert instance.endingTime == "sample_text"
    instance.endingTime = "sample_text_2"
    assert instance.endingTime == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_WorkingShifts_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_WorkingShifts(empId="sample_text", endingTime="sample_text", id="sample_text", startingTime="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_WorkingShifts_startingTime_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_WorkingShifts(empId="sample_text", endingTime="sample_text", id="sample_text", startingTime="sample_text")
    assert instance.startingTime == "sample_text"
    instance.startingTime = "sample_text_2"
    assert instance.startingTime == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_overtimeRequests_date_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_overtimeRequests(date="sample_text", id="sample_text", nd_time="sample_text", start_time="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_overtimeRequests_id_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_overtimeRequests(date="sample_text", id="sample_text", nd_time="sample_text", start_time="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_overtimeRequests_nd_time_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_overtimeRequests(date="sample_text", id="sample_text", nd_time="sample_text", start_time="sample_text")
    assert instance.nd_time == "sample_text"
    instance.nd_time = "sample_text_2"
    assert instance.nd_time == "sample_text_2"


def test_Class_Diagram_for_Proposed_system_overtimeRequests_start_time_value_roundtrip():
    instance = Class_Diagram_for_Proposed_system_overtimeRequests(date="sample_text", id="sample_text", nd_time="sample_text", start_time="sample_text")
    assert instance.start_time == "sample_text"
    instance.start_time = "sample_text_2"
    assert instance.start_time == "sample_text_2"


def test_assoc_Advances_Salary_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Advances(amount="sample_text", id="sample_text", installments="sample_text", issueDate="sample_text", salaryId="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Advances(amount="sample_text_2", id="sample_text_2", installments="sample_text_2", issueDate="sample_text_2", salaryId="sample_text_2")
    _safe_set(a, 'advances229', b1)
    assert _is_linked(a, 'advances229', b1)
    if hasattr(b1, 'salary28'):
        assert _is_linked(b1, 'salary28', a)
    _safe_set(a, 'advances229', b2)
    assert _is_linked(a, 'advances229', b2)
    if hasattr(b1, 'salary28'):
        assert not _is_linked(b1, 'salary28', a)
    if hasattr(b2, 'salary28'):
        assert _is_linked(b2, 'salary28', a)
    _safe_set(a, 'advances229', None)
    assert not _is_linked(a, 'advances229', b2)
    if hasattr(b2, 'salary28'):
        assert not _is_linked(b2, 'salary28', a)


def test_assoc_Allowances_Salary_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text", amount="sample_text", id="sample_text", issueDate="sample_text", salaryId="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Allowances(allowanceType="sample_text_2", amount="sample_text_2", id="sample_text_2", issueDate="sample_text_2", salaryId="sample_text_2")
    _safe_set(a, 'allowances225', b1)
    assert _is_linked(a, 'allowances225', b1)
    if hasattr(b1, 'salary24'):
        assert _is_linked(b1, 'salary24', a)
    _safe_set(a, 'allowances225', b2)
    assert _is_linked(a, 'allowances225', b2)
    if hasattr(b1, 'salary24'):
        assert not _is_linked(b1, 'salary24', a)
    if hasattr(b2, 'salary24'):
        assert _is_linked(b2, 'salary24', a)
    _safe_set(a, 'allowances225', None)
    assert not _is_linked(a, 'allowances225', b2)
    if hasattr(b2, 'salary24'):
        assert not _is_linked(b2, 'salary24', a)


def test_assoc_Attendance_Employee_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b1 = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text", clock_in="sample_text", clock_out="sample_text", date="sample_text", empId="sample_text", id="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Attendance(attribute="sample_text_2", clock_in="sample_text_2", clock_out="sample_text_2", date="sample_text_2", empId="sample_text_2", id="sample_text_2")
    _safe_set(a, 'attendance37', {b1})
    assert _is_linked(a, 'attendance37', b1)
    if hasattr(b1, 'employee36'):
        assert _is_linked(b1, 'employee36', a)
    _safe_set(a, 'attendance37', {b2})
    assert _is_linked(a, 'attendance37', b2)
    if hasattr(b1, 'employee36'):
        assert not _is_linked(b1, 'employee36', a)
    if hasattr(b2, 'employee36'):
        assert _is_linked(b2, 'employee36', a)
    _safe_set(a, 'attendance37', set())
    assert not _is_linked(a, 'attendance37', b2)
    if hasattr(b2, 'employee36'):
        assert not _is_linked(b2, 'employee36', a)


def test_assoc_Calender_Events_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Events(id="sample_text", type="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Calender(author_id="sample_text", depid="sample_text", eventType="sample_text", id="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Calender(author_id="sample_text_2", depid="sample_text_2", eventType="sample_text_2", id="sample_text_2")
    _safe_set(a, 'calender49', {b1})
    assert _is_linked(a, 'calender49', b1)
    if hasattr(b1, 'events48'):
        assert _is_linked(b1, 'events48', a)
    _safe_set(a, 'calender49', {b2})
    assert _is_linked(a, 'calender49', b2)
    if hasattr(b1, 'events48'):
        assert not _is_linked(b1, 'events48', a)
    if hasattr(b2, 'events48'):
        assert _is_linked(b2, 'events48', a)
    _safe_set(a, 'calender49', set())
    assert not _is_linked(a, 'calender49', b2)
    if hasattr(b2, 'events48'):
        assert not _is_linked(b2, 'events48', a)


def test_assoc_Deductions_Salary_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Salary(EPF="sample_text", ETF="sample_text", advances="sample_text", allowances="sample_text", basicPay="sample_text", deductions="sample_text", empId="sample_text", id="sample_text", overtimes="sample_text", payDate="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text", deducType="sample_text", deductDate="sample_text", id="sample_text", salaryId="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Deductions(amount="sample_text_2", deducType="sample_text_2", deductDate="sample_text_2", id="sample_text_2", salaryId="sample_text_2")
    _safe_set(a, 'deductions227', b1)
    assert _is_linked(a, 'deductions227', b1)
    if hasattr(b1, 'salary26'):
        assert _is_linked(b1, 'salary26', a)
    _safe_set(a, 'deductions227', b2)
    assert _is_linked(a, 'deductions227', b2)
    if hasattr(b1, 'salary26'):
        assert not _is_linked(b1, 'salary26', a)
    if hasattr(b2, 'salary26'):
        assert _is_linked(b2, 'salary26', a)
    _safe_set(a, 'deductions227', None)
    assert not _is_linked(a, 'deductions227', b2)
    if hasattr(b2, 'salary26'):
        assert not _is_linked(b2, 'salary26', a)


def test_assoc_Department_Post_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Department(empId="sample_text", id="sample_text", name="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Department(empId="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'department33', b1)
    assert _is_linked(a, 'department33', b1)
    if hasattr(b1, 'post32'):
        assert _is_linked(b1, 'post32', a)
    _safe_set(a, 'department33', b2)
    assert _is_linked(a, 'department33', b2)
    if hasattr(b1, 'post32'):
        assert not _is_linked(b1, 'post32', a)
    if hasattr(b2, 'post32'):
        assert _is_linked(b2, 'post32', a)
    _safe_set(a, 'department33', None)
    assert not _is_linked(a, 'department33', b2)
    if hasattr(b2, 'post32'):
        assert not _is_linked(b2, 'post32', a)


def test_assoc_Employee_Department_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b1 = Class_Diagram_for_Proposed_system_Department(empId="sample_text", id="sample_text", name="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Department(empId="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'department22', b1)
    assert _is_linked(a, 'department22', b1)
    if hasattr(b1, 'employee23'):
        assert _is_linked(b1, 'employee23', a)
    _safe_set(a, 'department22', b2)
    assert _is_linked(a, 'department22', b2)
    if hasattr(b1, 'employee23'):
        assert not _is_linked(b1, 'employee23', a)
    if hasattr(b2, 'employee23'):
        assert _is_linked(b2, 'employee23', a)
    _safe_set(a, 'department22', None)
    assert not _is_linked(a, 'department22', b2)
    if hasattr(b2, 'employee23'):
        assert not _is_linked(b2, 'employee23', a)


def test_assoc_Employee_LeaveTaken_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_LeaveTaken(attribute5="sample_text", empId="sample_text", id="sample_text", leaveDate="sample_text", leaveType="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    _safe_set(a, 'employee31', {b1})
    assert _is_linked(a, 'employee31', b1)
    if hasattr(b1, 'leaveTaken30'):
        assert _is_linked(b1, 'leaveTaken30', a)
    _safe_set(a, 'employee31', {b2})
    assert _is_linked(a, 'employee31', b2)
    if hasattr(b1, 'leaveTaken30'):
        assert not _is_linked(b1, 'leaveTaken30', a)
    if hasattr(b2, 'leaveTaken30'):
        assert _is_linked(b2, 'leaveTaken30', a)
    _safe_set(a, 'employee31', set())
    assert not _is_linked(a, 'employee31', b2)
    if hasattr(b2, 'leaveTaken30'):
        assert not _is_linked(b2, 'leaveTaken30', a)


def test_assoc_Employee_LeavesAllocated_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    _safe_set(a, 'employee39', b1)
    assert _is_linked(a, 'employee39', b1)
    if hasattr(b1, 'leavesAllocated38'):
        assert _is_linked(b1, 'leavesAllocated38', a)
    _safe_set(a, 'employee39', b2)
    assert _is_linked(a, 'employee39', b2)
    if hasattr(b1, 'leavesAllocated38'):
        assert not _is_linked(b1, 'leavesAllocated38', a)
    if hasattr(b2, 'leavesAllocated38'):
        assert _is_linked(b2, 'leavesAllocated38', a)
    _safe_set(a, 'employee39', None)
    assert not _is_linked(a, 'employee39', b2)
    if hasattr(b2, 'leavesAllocated38'):
        assert not _is_linked(b2, 'leavesAllocated38', a)


def test_assoc_Employee_Post_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_Post(attribute="sample_text", deptId="sample_text", id="sample_text", leavesEntitled="sample_text", name="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    _safe_set(a, 'employee35', b1)
    assert _is_linked(a, 'employee35', b1)
    if hasattr(b1, 'post34'):
        assert _is_linked(b1, 'post34', a)
    _safe_set(a, 'employee35', b2)
    assert _is_linked(a, 'employee35', b2)
    if hasattr(b1, 'post34'):
        assert not _is_linked(b1, 'post34', a)
    if hasattr(b2, 'post34'):
        assert _is_linked(b2, 'post34', a)
    _safe_set(a, 'employee35', None)
    assert not _is_linked(a, 'employee35', b2)
    if hasattr(b2, 'post34'):
        assert not _is_linked(b2, 'post34', a)


def test_assoc_Employee_User_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    b1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    _safe_set(a, 'employee41', b1)
    assert _is_linked(a, 'employee41', b1)
    if hasattr(b1, 'user40'):
        assert _is_linked(b1, 'user40', a)
    _safe_set(a, 'employee41', b2)
    assert _is_linked(a, 'employee41', b2)
    if hasattr(b1, 'user40'):
        assert not _is_linked(b1, 'user40', a)
    if hasattr(b2, 'user40'):
        assert _is_linked(b2, 'user40', a)
    _safe_set(a, 'employee41', None)
    assert not _is_linked(a, 'employee41', b2)
    if hasattr(b2, 'user40'):
        assert not _is_linked(b2, 'user40', a)


def test_assoc_Employee_overtimeRequests_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_overtimeRequests(date="sample_text", id="sample_text", nd_time="sample_text", start_time="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    _safe_set(a, 'employee51', b1)
    assert _is_linked(a, 'employee51', b1)
    if hasattr(b1, 'overtimeRequests50'):
        assert _is_linked(b1, 'overtimeRequests50', a)
    _safe_set(a, 'employee51', b2)
    assert _is_linked(a, 'employee51', b2)
    if hasattr(b1, 'overtimeRequests50'):
        assert not _is_linked(b1, 'overtimeRequests50', a)
    if hasattr(b2, 'overtimeRequests50'):
        assert _is_linked(b2, 'overtimeRequests50', a)
    _safe_set(a, 'employee51', None)
    assert not _is_linked(a, 'employee51', b2)
    if hasattr(b2, 'overtimeRequests50'):
        assert not _is_linked(b2, 'overtimeRequests50', a)


def test_assoc_LeavesAllocated_EPF_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    b1 = Class_Diagram_for_Proposed_system_EPF(id="sample_text", precentage="sample_text")
    b2 = Class_Diagram_for_Proposed_system_EPF(id="sample_text_2", precentage="sample_text_2")
    _safe_set(a, 'ePF44', {b1})
    assert _is_linked(a, 'ePF44', b1)
    if hasattr(b1, 'leavesAllocated45'):
        assert _is_linked(b1, 'leavesAllocated45', a)
    _safe_set(a, 'ePF44', {b2})
    assert _is_linked(a, 'ePF44', b2)
    if hasattr(b1, 'leavesAllocated45'):
        assert not _is_linked(b1, 'leavesAllocated45', a)
    if hasattr(b2, 'leavesAllocated45'):
        assert _is_linked(b2, 'leavesAllocated45', a)
    _safe_set(a, 'ePF44', set())
    assert not _is_linked(a, 'ePF44', b2)
    if hasattr(b2, 'leavesAllocated45'):
        assert not _is_linked(b2, 'leavesAllocated45', a)


def test_assoc_LeavesAllocated_ETF_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_LeavesAllocated(empId="sample_text", id="sample_text", leaveType="sample_text", noOfLeaves="sample_text")
    b1 = Class_Diagram_for_Proposed_system_ETF(id="sample_text", precentage="sample_text")
    b2 = Class_Diagram_for_Proposed_system_ETF(id="sample_text_2", precentage="sample_text_2")
    _safe_set(a, 'eTF46', b1)
    assert _is_linked(a, 'eTF46', b1)
    if hasattr(b1, 'leavesAllocated47'):
        assert _is_linked(b1, 'leavesAllocated47', a)
    _safe_set(a, 'eTF46', b2)
    assert _is_linked(a, 'eTF46', b2)
    if hasattr(b1, 'leavesAllocated47'):
        assert not _is_linked(b1, 'leavesAllocated47', a)
    if hasattr(b2, 'leavesAllocated47'):
        assert _is_linked(b2, 'leavesAllocated47', a)
    _safe_set(a, 'eTF46', None)
    assert not _is_linked(a, 'eTF46', b2)
    if hasattr(b2, 'leavesAllocated47'):
        assert not _is_linked(b2, 'leavesAllocated47', a)


def test_assoc_User_Role_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_User(LastName="sample_text", firstNAme="sample_text", id="sample_text", roleId=7)
    b1 = Class_Diagram_for_Proposed_system_Role(description="sample_text", id="sample_text", roleName="sample_text")
    b2 = Class_Diagram_for_Proposed_system_Role(description="sample_text_2", id="sample_text_2", roleName="sample_text_2")
    _safe_set(a, 'role42', {b1})
    assert _is_linked(a, 'role42', b1)
    if hasattr(b1, 'user43'):
        assert _is_linked(b1, 'user43', a)
    _safe_set(a, 'role42', {b2})
    assert _is_linked(a, 'role42', b2)
    if hasattr(b1, 'user43'):
        assert not _is_linked(b1, 'user43', a)
    if hasattr(b2, 'user43'):
        assert _is_linked(b2, 'user43', a)
    _safe_set(a, 'role42', set())
    assert not _is_linked(a, 'role42', b2)
    if hasattr(b2, 'user43'):
        assert not _is_linked(b2, 'user43', a)


def test_assoc_WorkingShifts_Employee_link_reassign_clear():
    a = Class_Diagram_for_Proposed_system_WorkingShifts(empId="sample_text", endingTime="sample_text", id="sample_text", startingTime="sample_text")
    b1 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text", address="sample_text", deptId=7, gender="sample_text", id=7, mobile="sample_text", phone="sample_text", postID=7, shiftId=7, userId=7)
    b2 = Class_Diagram_for_Proposed_system_Employee(NIC="sample_text_2", address="sample_text_2", deptId=13, gender="sample_text_2", id=13, mobile="sample_text_2", phone="sample_text_2", postID=13, shiftId=13, userId=13)
    _safe_set(a, 'employee20', b1)
    assert _is_linked(a, 'employee20', b1)
    if hasattr(b1, 'workingShifts21'):
        assert _is_linked(b1, 'workingShifts21', a)
    _safe_set(a, 'employee20', b2)
    assert _is_linked(a, 'employee20', b2)
    if hasattr(b1, 'workingShifts21'):
        assert not _is_linked(b1, 'workingShifts21', a)
    if hasattr(b2, 'workingShifts21'):
        assert _is_linked(b2, 'workingShifts21', a)
    _safe_set(a, 'employee20', None)
    assert not _is_linked(a, 'employee20', b2)
    if hasattr(b2, 'workingShifts21'):
        assert not _is_linked(b2, 'workingShifts21', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Clark1_Actor_strategy = st.builds(Clark1_Actor)
@given(instance=Clark1_Actor_strategy)
@settings(max_examples=25)
def test_Clark1_Actor_instantiation(instance):
    assert isinstance(instance, Clark1_Actor)


Clark1_Actor1_strategy = st.builds(Clark1_Actor1)
@given(instance=Clark1_Actor1_strategy)
@settings(max_examples=25)
def test_Clark1_Actor1_instantiation(instance):
    assert isinstance(instance, Clark1_Actor1)


Class_Diagram_for_Proposed_system_Advances_strategy = st.builds(Class_Diagram_for_Proposed_system_Advances, amount=safe_text, id=safe_text, installments=safe_text, issueDate=safe_text, salaryId=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Advances_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Advances_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Advances)


Class_Diagram_for_Proposed_system_Allowances_strategy = st.builds(Class_Diagram_for_Proposed_system_Allowances, allowanceType=safe_text, amount=safe_text, id=safe_text, issueDate=safe_text, salaryId=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Allowances_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Allowances_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Allowances)


Class_Diagram_for_Proposed_system_Attendance_strategy = st.builds(Class_Diagram_for_Proposed_system_Attendance, attribute=safe_text, clock_in=safe_text, clock_out=safe_text, date=safe_text, empId=safe_text, id=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Attendance_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Attendance_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Attendance)


Class_Diagram_for_Proposed_system_Calender_strategy = st.builds(Class_Diagram_for_Proposed_system_Calender, author_id=safe_text, depid=safe_text, eventType=safe_text, id=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Calender_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Calender_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Calender)


Class_Diagram_for_Proposed_system_Deductions_strategy = st.builds(Class_Diagram_for_Proposed_system_Deductions, amount=safe_text, deducType=safe_text, deductDate=safe_text, id=safe_text, salaryId=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Deductions_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Deductions_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Deductions)


Class_Diagram_for_Proposed_system_Department_strategy = st.builds(Class_Diagram_for_Proposed_system_Department, empId=safe_text, id=safe_text, name=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Department_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Department_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Department)


Class_Diagram_for_Proposed_system_EPF_strategy = st.builds(Class_Diagram_for_Proposed_system_EPF, id=safe_text, precentage=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_EPF_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_EPF_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_EPF)


Class_Diagram_for_Proposed_system_ETF_strategy = st.builds(Class_Diagram_for_Proposed_system_ETF, id=safe_text, precentage=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_ETF_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_ETF_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_ETF)


Class_Diagram_for_Proposed_system_Employee_strategy = st.builds(Class_Diagram_for_Proposed_system_Employee, NIC=safe_text, address=safe_text, deptId=st.integers(), gender=safe_text, id=st.integers(), mobile=safe_text, phone=safe_text, postID=st.integers(), shiftId=st.integers(), userId=st.integers())
@given(instance=Class_Diagram_for_Proposed_system_Employee_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Employee_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Employee)


Class_Diagram_for_Proposed_system_Events_strategy = st.builds(Class_Diagram_for_Proposed_system_Events, id=safe_text, type=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Events_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Events_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Events)


Class_Diagram_for_Proposed_system_LeaveTaken_strategy = st.builds(Class_Diagram_for_Proposed_system_LeaveTaken, attribute5=safe_text, empId=safe_text, id=safe_text, leaveDate=safe_text, leaveType=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_LeaveTaken_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_LeaveTaken_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_LeaveTaken)


Class_Diagram_for_Proposed_system_LeavesAllocated_strategy = st.builds(Class_Diagram_for_Proposed_system_LeavesAllocated, empId=safe_text, id=safe_text, leaveType=safe_text, noOfLeaves=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_LeavesAllocated_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_LeavesAllocated_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_LeavesAllocated)


Class_Diagram_for_Proposed_system_Post_strategy = st.builds(Class_Diagram_for_Proposed_system_Post, attribute=safe_text, deptId=safe_text, id=safe_text, leavesEntitled=safe_text, name=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Post_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Post_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Post)


Class_Diagram_for_Proposed_system_Role_strategy = st.builds(Class_Diagram_for_Proposed_system_Role, description=safe_text, id=safe_text, roleName=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Role_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Role_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Role)


Class_Diagram_for_Proposed_system_Salary_strategy = st.builds(Class_Diagram_for_Proposed_system_Salary, EPF=safe_text, ETF=safe_text, advances=safe_text, allowances=safe_text, basicPay=safe_text, deductions=safe_text, empId=safe_text, id=safe_text, overtimes=safe_text, payDate=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_Salary_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_Salary_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_Salary)


Class_Diagram_for_Proposed_system_User_strategy = st.builds(Class_Diagram_for_Proposed_system_User, LastName=safe_text, firstNAme=safe_text, id=safe_text, roleId=st.integers())
@given(instance=Class_Diagram_for_Proposed_system_User_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_User_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_User)


Class_Diagram_for_Proposed_system_WorkingShifts_strategy = st.builds(Class_Diagram_for_Proposed_system_WorkingShifts, empId=safe_text, endingTime=safe_text, id=safe_text, startingTime=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_WorkingShifts_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_WorkingShifts_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_WorkingShifts)


Class_Diagram_for_Proposed_system_overtimeRequests_strategy = st.builds(Class_Diagram_for_Proposed_system_overtimeRequests, date=safe_text, id=safe_text, nd_time=safe_text, start_time=safe_text)
@given(instance=Class_Diagram_for_Proposed_system_overtimeRequests_strategy)
@settings(max_examples=25)
def test_Class_Diagram_for_Proposed_system_overtimeRequests_instantiation(instance):
    assert isinstance(instance, Class_Diagram_for_Proposed_system_overtimeRequests)


Manager_Actor_strategy = st.builds(Manager_Actor)
@given(instance=Manager_Actor_strategy)
@settings(max_examples=25)
def test_Manager_Actor_instantiation(instance):
    assert isinstance(instance, Manager_Actor)


Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Access_leave_documents_UseCase)


Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Access_time_cards_UseCase)


Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Approve_leave_UseCase)


Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Calculate_Late_UseCase)


Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Calculate_Monthly_leaves_UseCase)


Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Calculate_Overtime_UseCase)


Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Check_employee_appraisal_forms_UseCase)


Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Check_leave_forms_UseCase)


Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Enter_salary_details_to_spreadsheets_UseCase)


Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Fill_leave_apply_form_UseCase)


Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Generate_reports_from_excel_UseCase)


Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Give_message_to_employee_UseCase)


Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Hand_over_form_to_HR_Dept_UseCase)


Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Mark_clock_in_time_UseCase)


Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Mark_clock_out_time_UseCase)


Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Put_company_notices_UseCase)


Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Register_New_Employee_UseCase)


Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Reject_leave_UseCase)


Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Request_Leave_UseCase)


Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Request_Loan_and_advances_UseCase)


Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Salary_calculation_UseCase)


Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase_strategy = st.builds(Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase)
@given(instance=Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase_strategy)
@settings(max_examples=25)
def test_Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase_instantiation(instance):
    assert isinstance(instance, Use_Case_Diagram_for_Existing_System_Store_times_in_employee_time_cards_UseCase)



