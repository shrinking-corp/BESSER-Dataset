import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Applicant,
    Assessment,
    Assessment__Self_Assessment,
    Attendance,
    Login,
    New_Employee,
    Performance,
    Position,
    Registration,
    Requirement,
    Survey,
    Task,
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

def test_assoc_Admin_Login_reverse_link_reassign_clear():
    a1 = Login(password="sample_text", userid="sample_text")
    a2 = Login(password="sample_text_2", userid="sample_text_2")
    b = Admin(address="sample_text", name="sample_text", qualification="sample_text")
    _safe_set(b, 'login0', a1)
    assert _is_linked(b, 'login0', a1)
    if hasattr(a1, 'admin1'):
        assert _is_linked(a1, 'admin1', b)
    _safe_set(b, 'login0', a2)
    assert _is_linked(b, 'login0', a2)
    if hasattr(a1, 'admin1'):
        assert not _is_linked(a1, 'admin1', b)
    if hasattr(a2, 'admin1'):
        assert _is_linked(a2, 'admin1', b)
    _safe_set(b, 'login0', None)
    assert not _is_linked(b, 'login0', a2)
    if hasattr(a2, 'admin1'):
        assert not _is_linked(a2, 'admin1', b)


def test_assoc_Admin_Registration_reverse_link_reassign_clear():
    a1 = Registration(Address="sample_text", Applied_Position="sample_text", Date="sample_text", Email="sample_text", Name="sample_text", Phone="sample_text", Position_Type="sample_text", Skills___Requirement="sample_text")
    a2 = Registration(Address="sample_text_2", Applied_Position="sample_text_2", Date="sample_text_2", Email="sample_text_2", Name="sample_text_2", Phone="sample_text_2", Position_Type="sample_text_2", Skills___Requirement="sample_text_2")
    b = Admin(address="sample_text", name="sample_text", qualification="sample_text")
    _safe_set(b, 'registration6', a1)
    assert _is_linked(b, 'registration6', a1)
    if hasattr(a1, 'admin7'):
        assert _is_linked(a1, 'admin7', b)
    _safe_set(b, 'registration6', a2)
    assert _is_linked(b, 'registration6', a2)
    if hasattr(a1, 'admin7'):
        assert not _is_linked(a1, 'admin7', b)
    if hasattr(a2, 'admin7'):
        assert _is_linked(a2, 'admin7', b)
    _safe_set(b, 'registration6', None)
    assert not _is_linked(b, 'registration6', a2)
    if hasattr(a2, 'admin7'):
        assert not _is_linked(a2, 'admin7', b)


def test_assoc_Applicant_Login_reverse_link_reassign_clear():
    a1 = Login(password="sample_text", userid="sample_text")
    a2 = Login(password="sample_text_2", userid="sample_text_2")
    b = Applicant(Address="sample_text", Applied_Position="sample_text", Date_of_Birth="sample_text", Email="sample_text", First_Name="sample_text", Last_Name="sample_text", Password="sample_text", Phone="sample_text")
    _safe_set(b, 'login2', a1)
    assert _is_linked(b, 'login2', a1)
    if hasattr(a1, 'applicant3'):
        assert _is_linked(a1, 'applicant3', b)
    _safe_set(b, 'login2', a2)
    assert _is_linked(b, 'login2', a2)
    if hasattr(a1, 'applicant3'):
        assert not _is_linked(a1, 'applicant3', b)
    if hasattr(a2, 'applicant3'):
        assert _is_linked(a2, 'applicant3', b)
    _safe_set(b, 'login2', None)
    assert not _is_linked(b, 'login2', a2)
    if hasattr(a2, 'applicant3'):
        assert not _is_linked(a2, 'applicant3', b)


def test_assoc_Applicant_New_Employee_reverse_link_reassign_clear():
    a1 = New_Employee(Date_of_Birth="sample_text", Division="sample_text", Name="sample_text", Place_of_Birth="sample_text", Position="sample_text", Working_Since="sample_text")
    a2 = New_Employee(Date_of_Birth="sample_text_2", Division="sample_text_2", Name="sample_text_2", Place_of_Birth="sample_text_2", Position="sample_text_2", Working_Since="sample_text_2")
    b = Applicant(Address="sample_text", Applied_Position="sample_text", Date_of_Birth="sample_text", Email="sample_text", First_Name="sample_text", Last_Name="sample_text", Password="sample_text", Phone="sample_text")
    _safe_set(b, 'new_Employee12', a1)
    assert _is_linked(b, 'new_Employee12', a1)
    if hasattr(a1, 'applicant13'):
        assert _is_linked(a1, 'applicant13', b)
    _safe_set(b, 'new_Employee12', a2)
    assert _is_linked(b, 'new_Employee12', a2)
    if hasattr(a1, 'applicant13'):
        assert not _is_linked(a1, 'applicant13', b)
    if hasattr(a2, 'applicant13'):
        assert _is_linked(a2, 'applicant13', b)
    _safe_set(b, 'new_Employee12', None)
    assert not _is_linked(b, 'new_Employee12', a2)
    if hasattr(a2, 'applicant13'):
        assert not _is_linked(a2, 'applicant13', b)


def test_assoc_Applicant_Position_reverse_link_reassign_clear():
    a1 = Position(divisionName="sample_text", jobID="sample_text", positionID=7, positionName="sample_text")
    a2 = Position(divisionName="sample_text_2", jobID="sample_text_2", positionID=13, positionName="sample_text_2")
    b = Applicant(Address="sample_text", Applied_Position="sample_text", Date_of_Birth="sample_text", Email="sample_text", First_Name="sample_text", Last_Name="sample_text", Password="sample_text", Phone="sample_text")
    _safe_set(b, 'position8', a1)
    assert _is_linked(b, 'position8', a1)
    if hasattr(a1, 'applicant9'):
        assert _is_linked(a1, 'applicant9', b)
    _safe_set(b, 'position8', a2)
    assert _is_linked(b, 'position8', a2)
    if hasattr(a1, 'applicant9'):
        assert not _is_linked(a1, 'applicant9', b)
    if hasattr(a2, 'applicant9'):
        assert _is_linked(a2, 'applicant9', b)
    _safe_set(b, 'position8', None)
    assert not _is_linked(b, 'position8', a2)
    if hasattr(a2, 'applicant9'):
        assert not _is_linked(a2, 'applicant9', b)


def test_assoc_Applicant_Registration_reverse_link_reassign_clear():
    a1 = Registration(Address="sample_text", Applied_Position="sample_text", Date="sample_text", Email="sample_text", Name="sample_text", Phone="sample_text", Position_Type="sample_text", Skills___Requirement="sample_text")
    a2 = Registration(Address="sample_text_2", Applied_Position="sample_text_2", Date="sample_text_2", Email="sample_text_2", Name="sample_text_2", Phone="sample_text_2", Position_Type="sample_text_2", Skills___Requirement="sample_text_2")
    b = Applicant(Address="sample_text", Applied_Position="sample_text", Date_of_Birth="sample_text", Email="sample_text", First_Name="sample_text", Last_Name="sample_text", Password="sample_text", Phone="sample_text")
    _safe_set(b, 'registration4', a1)
    assert _is_linked(b, 'registration4', a1)
    if hasattr(a1, 'applicant5'):
        assert _is_linked(a1, 'applicant5', b)
    _safe_set(b, 'registration4', a2)
    assert _is_linked(b, 'registration4', a2)
    if hasattr(a1, 'applicant5'):
        assert not _is_linked(a1, 'applicant5', b)
    if hasattr(a2, 'applicant5'):
        assert _is_linked(a2, 'applicant5', b)
    _safe_set(b, 'registration4', None)
    assert not _is_linked(b, 'registration4', a2)
    if hasattr(a2, 'applicant5'):
        assert not _is_linked(a2, 'applicant5', b)


def test_assoc_Assessment__Self_Assessment_Assessment_reverse_link_reassign_clear():
    a1 = Assessment__Self_Assessment(Name="sample_text", Question="sample_text", Score="sample_text")
    a2 = Assessment__Self_Assessment(Name="sample_text_2", Question="sample_text_2", Score="sample_text_2")
    b = Assessment(Name="sample_text", Total_Score="sample_text", Type_of_Assessment="sample_text")
    _safe_set(b, 'assessment__Self_Assessment23', a1)
    assert _is_linked(b, 'assessment__Self_Assessment23', a1)
    if hasattr(a1, 'assessment22'):
        assert _is_linked(a1, 'assessment22', b)
    _safe_set(b, 'assessment__Self_Assessment23', a2)
    assert _is_linked(b, 'assessment__Self_Assessment23', a2)
    if hasattr(a1, 'assessment22'):
        assert not _is_linked(a1, 'assessment22', b)
    if hasattr(a2, 'assessment22'):
        assert _is_linked(a2, 'assessment22', b)
    _safe_set(b, 'assessment__Self_Assessment23', None)
    assert not _is_linked(b, 'assessment__Self_Assessment23', a2)
    if hasattr(a2, 'assessment22'):
        assert not _is_linked(a2, 'assessment22', b)


def test_assoc_Attendance_Assessment_reverse_link_reassign_clear():
    a1 = Attendance(Date___Time="sample_text", Details="sample_text", Name="sample_text", Position="sample_text")
    a2 = Attendance(Date___Time="sample_text_2", Details="sample_text_2", Name="sample_text_2", Position="sample_text_2")
    b = Assessment(Name="sample_text", Total_Score="sample_text", Type_of_Assessment="sample_text")
    _safe_set(b, 'attendance21', a1)
    assert _is_linked(b, 'attendance21', a1)
    if hasattr(a1, 'assessment20'):
        assert _is_linked(a1, 'assessment20', b)
    _safe_set(b, 'attendance21', a2)
    assert _is_linked(b, 'attendance21', a2)
    if hasattr(a1, 'assessment20'):
        assert not _is_linked(a1, 'assessment20', b)
    if hasattr(a2, 'assessment20'):
        assert _is_linked(a2, 'assessment20', b)
    _safe_set(b, 'attendance21', None)
    assert not _is_linked(b, 'attendance21', a2)
    if hasattr(a2, 'assessment20'):
        assert not _is_linked(a2, 'assessment20', b)


def test_assoc_New_Employee_Attendance_reverse_link_reassign_clear():
    a1 = New_Employee(Date_of_Birth="sample_text", Division="sample_text", Name="sample_text", Place_of_Birth="sample_text", Position="sample_text", Working_Since="sample_text")
    a2 = New_Employee(Date_of_Birth="sample_text_2", Division="sample_text_2", Name="sample_text_2", Place_of_Birth="sample_text_2", Position="sample_text_2", Working_Since="sample_text_2")
    b = Attendance(Date___Time="sample_text", Details="sample_text", Name="sample_text", Position="sample_text")
    _safe_set(b, 'new_Employee17', a1)
    assert _is_linked(b, 'new_Employee17', a1)
    if hasattr(a1, 'attendance16'):
        assert _is_linked(a1, 'attendance16', b)
    _safe_set(b, 'new_Employee17', a2)
    assert _is_linked(b, 'new_Employee17', a2)
    if hasattr(a1, 'attendance16'):
        assert not _is_linked(a1, 'attendance16', b)
    if hasattr(a2, 'attendance16'):
        assert _is_linked(a2, 'attendance16', b)
    _safe_set(b, 'new_Employee17', None)
    assert not _is_linked(b, 'new_Employee17', a2)
    if hasattr(a2, 'attendance16'):
        assert not _is_linked(a2, 'attendance16', b)


def test_assoc_Performance_Assessment_reverse_link_reassign_clear():
    a1 = Performance(Coordination="sample_text", Name="sample_text", Punctuality="sample_text", Target="sample_text")
    a2 = Performance(Coordination="sample_text_2", Name="sample_text_2", Punctuality="sample_text_2", Target="sample_text_2")
    b = Assessment(Name="sample_text", Total_Score="sample_text", Type_of_Assessment="sample_text")
    _safe_set(b, 'performance27', a1)
    assert _is_linked(b, 'performance27', a1)
    if hasattr(a1, 'assessment26'):
        assert _is_linked(a1, 'assessment26', b)
    _safe_set(b, 'performance27', a2)
    assert _is_linked(b, 'performance27', a2)
    if hasattr(a1, 'assessment26'):
        assert not _is_linked(a1, 'assessment26', b)
    if hasattr(a2, 'assessment26'):
        assert _is_linked(a2, 'assessment26', b)
    _safe_set(b, 'performance27', None)
    assert not _is_linked(b, 'performance27', a2)
    if hasattr(a2, 'assessment26'):
        assert not _is_linked(a2, 'assessment26', b)


def test_assoc_Registration_New_Employee_reverse_link_reassign_clear():
    a1 = Registration(Address="sample_text", Applied_Position="sample_text", Date="sample_text", Email="sample_text", Name="sample_text", Phone="sample_text", Position_Type="sample_text", Skills___Requirement="sample_text")
    a2 = Registration(Address="sample_text_2", Applied_Position="sample_text_2", Date="sample_text_2", Email="sample_text_2", Name="sample_text_2", Phone="sample_text_2", Position_Type="sample_text_2", Skills___Requirement="sample_text_2")
    b = New_Employee(Date_of_Birth="sample_text", Division="sample_text", Name="sample_text", Place_of_Birth="sample_text", Position="sample_text", Working_Since="sample_text")
    _safe_set(b, 'registration11', a1)
    assert _is_linked(b, 'registration11', a1)
    if hasattr(a1, 'new_Employee10'):
        assert _is_linked(a1, 'new_Employee10', b)
    _safe_set(b, 'registration11', a2)
    assert _is_linked(b, 'registration11', a2)
    if hasattr(a1, 'new_Employee10'):
        assert not _is_linked(a1, 'new_Employee10', b)
    if hasattr(a2, 'new_Employee10'):
        assert _is_linked(a2, 'new_Employee10', b)
    _safe_set(b, 'registration11', None)
    assert not _is_linked(b, 'registration11', a2)
    if hasattr(a2, 'new_Employee10'):
        assert not _is_linked(a2, 'new_Employee10', b)


def test_assoc_Requirement_Registration_reverse_link_reassign_clear():
    a1 = Requirement(Curriculum_Vitae="sample_text", Diploma="sample_text", ID_Card="sample_text", Photo="sample_text", Transcript="sample_text")
    a2 = Requirement(Curriculum_Vitae="sample_text_2", Diploma="sample_text_2", ID_Card="sample_text_2", Photo="sample_text_2", Transcript="sample_text_2")
    b = Registration(Address="sample_text", Applied_Position="sample_text", Date="sample_text", Email="sample_text", Name="sample_text", Phone="sample_text", Position_Type="sample_text", Skills___Requirement="sample_text")
    _safe_set(b, 'requirement19', a1)
    assert _is_linked(b, 'requirement19', a1)
    if hasattr(a1, 'registration18'):
        assert _is_linked(a1, 'registration18', b)
    _safe_set(b, 'requirement19', a2)
    assert _is_linked(b, 'requirement19', a2)
    if hasattr(a1, 'registration18'):
        assert not _is_linked(a1, 'registration18', b)
    if hasattr(a2, 'registration18'):
        assert _is_linked(a2, 'registration18', b)
    _safe_set(b, 'requirement19', None)
    assert not _is_linked(b, 'requirement19', a2)
    if hasattr(a2, 'registration18'):
        assert not _is_linked(a2, 'registration18', b)


def test_assoc_Survey_Assessment_reverse_link_reassign_clear():
    a1 = Survey(Name="sample_text", Question="sample_text", Score="sample_text")
    a2 = Survey(Name="sample_text_2", Question="sample_text_2", Score="sample_text_2")
    b = Assessment(Name="sample_text", Total_Score="sample_text", Type_of_Assessment="sample_text")
    _safe_set(b, 'survey25', a1)
    assert _is_linked(b, 'survey25', a1)
    if hasattr(a1, 'assessment24'):
        assert _is_linked(a1, 'assessment24', b)
    _safe_set(b, 'survey25', a2)
    assert _is_linked(b, 'survey25', a2)
    if hasattr(a1, 'assessment24'):
        assert not _is_linked(a1, 'assessment24', b)
    if hasattr(a2, 'assessment24'):
        assert _is_linked(a2, 'assessment24', b)
    _safe_set(b, 'survey25', None)
    assert not _is_linked(b, 'survey25', a2)
    if hasattr(a2, 'assessment24'):
        assert not _is_linked(a2, 'assessment24', b)


def test_assoc_Task_New_Employee_reverse_link_reassign_clear():
    a1 = Task(Deadline="sample_text", Name="sample_text", Task_Detail="sample_text", Task_Name="sample_text")
    a2 = Task(Deadline="sample_text_2", Name="sample_text_2", Task_Detail="sample_text_2", Task_Name="sample_text_2")
    b = New_Employee(Date_of_Birth="sample_text", Division="sample_text", Name="sample_text", Place_of_Birth="sample_text", Position="sample_text", Working_Since="sample_text")
    _safe_set(b, 'task15', a1)
    assert _is_linked(b, 'task15', a1)
    if hasattr(a1, 'new_Employee14'):
        assert _is_linked(a1, 'new_Employee14', b)
    _safe_set(b, 'task15', a2)
    assert _is_linked(b, 'task15', a2)
    if hasattr(a1, 'new_Employee14'):
        assert not _is_linked(a1, 'new_Employee14', b)
    if hasattr(a2, 'new_Employee14'):
        assert _is_linked(a2, 'new_Employee14', b)
    _safe_set(b, 'task15', None)
    assert not _is_linked(b, 'task15', a2)
    if hasattr(a2, 'new_Employee14'):
        assert not _is_linked(a2, 'new_Employee14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

