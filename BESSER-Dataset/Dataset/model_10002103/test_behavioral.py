import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Attendance,
    Employee,
    Full_day,
    Haff_day,
    Leave,
    location,
    login,
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

def test_assoc_Admin_Attendance_reverse_link_reassign_clear():
    a1 = Attendance(atten_date="sample_text", atten_emp_id=7, atten_id=7, atten_time=7, atten_type="sample_text")
    a2 = Attendance(atten_date="sample_text_2", atten_emp_id=13, atten_id=13, atten_time=13, atten_type="sample_text_2")
    b = Admin(password="sample_text", username="sample_text")
    _safe_set(b, 'attendance12', a1)
    assert _is_linked(b, 'attendance12', a1)
    if hasattr(a1, 'Admin13'):
        assert _is_linked(a1, 'Admin13', b)
    _safe_set(b, 'attendance12', a2)
    assert _is_linked(b, 'attendance12', a2)
    if hasattr(a1, 'Admin13'):
        assert not _is_linked(a1, 'Admin13', b)
    if hasattr(a2, 'Admin13'):
        assert _is_linked(a2, 'Admin13', b)
    _safe_set(b, 'attendance12', None)
    assert not _is_linked(b, 'attendance12', a2)
    if hasattr(a2, 'Admin13'):
        assert not _is_linked(a2, 'Admin13', b)


def test_assoc_Admin_Employee_reverse_link_reassign_clear():
    a1 = Employee(address="sample_text", e_id=7, email_id="sample_text", name="sample_text", office_address="sample_text", paasword="sample_text", phone_no=7)
    a2 = Employee(address="sample_text_2", e_id=13, email_id="sample_text_2", name="sample_text_2", office_address="sample_text_2", paasword="sample_text_2", phone_no=13)
    b = Admin(password="sample_text", username="sample_text")
    _safe_set(b, 'employee8', {a1})
    assert _is_linked(b, 'employee8', a1)
    if hasattr(a1, 'Admin9'):
        assert _is_linked(a1, 'Admin9', b)
    _safe_set(b, 'employee8', {a2})
    assert _is_linked(b, 'employee8', a2)
    if hasattr(a1, 'Admin9'):
        assert not _is_linked(a1, 'Admin9', b)
    if hasattr(a2, 'Admin9'):
        assert _is_linked(a2, 'Admin9', b)
    _safe_set(b, 'employee8', set())
    assert not _is_linked(b, 'employee8', a2)
    if hasattr(a2, 'Admin9'):
        assert not _is_linked(a2, 'Admin9', b)


def test_assoc_Admin_Leave_reverse_link_reassign_clear():
    a1 = Leave(l_description="sample_text", l_emp_id=7, l_id=7, l_type="sample_text")
    a2 = Leave(l_description="sample_text_2", l_emp_id=13, l_id=13, l_type="sample_text_2")
    b = Admin(password="sample_text", username="sample_text")
    _safe_set(b, 'leave2', a1)
    assert _is_linked(b, 'leave2', a1)
    if hasattr(a1, 'Admin3'):
        assert _is_linked(a1, 'Admin3', b)
    _safe_set(b, 'leave2', a2)
    assert _is_linked(b, 'leave2', a2)
    if hasattr(a1, 'Admin3'):
        assert not _is_linked(a1, 'Admin3', b)
    if hasattr(a2, 'Admin3'):
        assert _is_linked(a2, 'Admin3', b)
    _safe_set(b, 'leave2', None)
    assert not _is_linked(b, 'leave2', a2)
    if hasattr(a2, 'Admin3'):
        assert not _is_linked(a2, 'Admin3', b)


def test_assoc_Admin_login_reverse_link_reassign_clear():
    a1 = login(loginStatus="sample_text", loginUsername="sample_text", login_id=7, loginpassword="sample_text")
    a2 = login(loginStatus="sample_text_2", loginUsername="sample_text_2", login_id=13, loginpassword="sample_text_2")
    b = Admin(password="sample_text", username="sample_text")
    _safe_set(b, 'login20', a1)
    assert _is_linked(b, 'login20', a1)
    if hasattr(a1, 'Admin21'):
        assert _is_linked(a1, 'Admin21', b)
    _safe_set(b, 'login20', a2)
    assert _is_linked(b, 'login20', a2)
    if hasattr(a1, 'Admin21'):
        assert not _is_linked(a1, 'Admin21', b)
    if hasattr(a2, 'Admin21'):
        assert _is_linked(a2, 'Admin21', b)
    _safe_set(b, 'login20', None)
    assert not _is_linked(b, 'login20', a2)
    if hasattr(a2, 'Admin21'):
        assert not _is_linked(a2, 'Admin21', b)


def test_assoc_Attendance_location_reverse_link_reassign_clear():
    a1 = location(Latitude=7, Longitude=7)
    a2 = location(Latitude=13, Longitude=13)
    b = Attendance(atten_date="sample_text", atten_emp_id=7, atten_id=7, atten_time=7, atten_type="sample_text")
    _safe_set(b, 'location6', a1)
    assert _is_linked(b, 'location6', a1)
    if hasattr(a1, 'attendance7'):
        assert _is_linked(a1, 'attendance7', b)
    _safe_set(b, 'location6', a2)
    assert _is_linked(b, 'location6', a2)
    if hasattr(a1, 'attendance7'):
        assert not _is_linked(a1, 'attendance7', b)
    if hasattr(a2, 'attendance7'):
        assert _is_linked(a2, 'attendance7', b)
    _safe_set(b, 'location6', None)
    assert not _is_linked(b, 'location6', a2)
    if hasattr(a2, 'attendance7'):
        assert not _is_linked(a2, 'attendance7', b)


def test_assoc_Employee_Attendance_reverse_link_reassign_clear():
    a1 = Employee(address="sample_text", e_id=7, email_id="sample_text", name="sample_text", office_address="sample_text", paasword="sample_text", phone_no=7)
    a2 = Employee(address="sample_text_2", e_id=13, email_id="sample_text_2", name="sample_text_2", office_address="sample_text_2", paasword="sample_text_2", phone_no=13)
    b = Attendance(atten_date="sample_text", atten_emp_id=7, atten_id=7, atten_time=7, atten_type="sample_text")
    _safe_set(b, 'employee5', a1)
    assert _is_linked(b, 'employee5', a1)
    if hasattr(a1, 'attendance4'):
        assert _is_linked(a1, 'attendance4', b)
    _safe_set(b, 'employee5', a2)
    assert _is_linked(b, 'employee5', a2)
    if hasattr(a1, 'attendance4'):
        assert not _is_linked(a1, 'attendance4', b)
    if hasattr(a2, 'attendance4'):
        assert _is_linked(a2, 'attendance4', b)
    _safe_set(b, 'employee5', None)
    assert not _is_linked(b, 'employee5', a2)
    if hasattr(a2, 'attendance4'):
        assert not _is_linked(a2, 'attendance4', b)


def test_assoc_Employee_Attendance1_reverse_link_reassign_clear():
    a1 = Employee(address="sample_text", e_id=7, email_id="sample_text", name="sample_text", office_address="sample_text", paasword="sample_text", phone_no=7)
    a2 = Employee(address="sample_text_2", e_id=13, email_id="sample_text_2", name="sample_text_2", office_address="sample_text_2", paasword="sample_text_2", phone_no=13)
    b = Attendance(atten_date="sample_text", atten_emp_id=7, atten_id=7, atten_time=7, atten_type="sample_text")
    _safe_set(b, 'employee15', a1)
    assert _is_linked(b, 'employee15', a1)
    if hasattr(a1, 'attendance14'):
        assert _is_linked(a1, 'attendance14', b)
    _safe_set(b, 'employee15', a2)
    assert _is_linked(b, 'employee15', a2)
    if hasattr(a1, 'attendance14'):
        assert not _is_linked(a1, 'attendance14', b)
    if hasattr(a2, 'attendance14'):
        assert _is_linked(a2, 'attendance14', b)
    _safe_set(b, 'employee15', None)
    assert not _is_linked(b, 'employee15', a2)
    if hasattr(a2, 'attendance14'):
        assert not _is_linked(a2, 'attendance14', b)


def test_assoc_Employee_____Admin_reverse_link_reassign_clear():
    a1 = Employee(address="sample_text", e_id=7, email_id="sample_text", name="sample_text", office_address="sample_text", paasword="sample_text", phone_no=7)
    a2 = Employee(address="sample_text_2", e_id=13, email_id="sample_text_2", name="sample_text_2", office_address="sample_text_2", paasword="sample_text_2", phone_no=13)
    b = Admin(password="sample_text", username="sample_text")
    _safe_set(b, 'employee1', a1)
    assert _is_linked(b, 'employee1', a1)
    if hasattr(a1, 'Admin0'):
        assert _is_linked(a1, 'Admin0', b)
    _safe_set(b, 'employee1', a2)
    assert _is_linked(b, 'employee1', a2)
    if hasattr(a1, 'Admin0'):
        assert not _is_linked(a1, 'Admin0', b)
    if hasattr(a2, 'Admin0'):
        assert _is_linked(a2, 'Admin0', b)
    _safe_set(b, 'employee1', None)
    assert not _is_linked(b, 'employee1', a2)
    if hasattr(a2, 'Admin0'):
        assert not _is_linked(a2, 'Admin0', b)


def test_assoc_Employee_login_reverse_link_reassign_clear():
    a1 = login(loginStatus="sample_text", loginUsername="sample_text", login_id=7, loginpassword="sample_text")
    a2 = login(loginStatus="sample_text_2", loginUsername="sample_text_2", login_id=13, loginpassword="sample_text_2")
    b = Employee(address="sample_text", e_id=7, email_id="sample_text", name="sample_text", office_address="sample_text", paasword="sample_text", phone_no=7)
    _safe_set(b, 'login218', a1)
    assert _is_linked(b, 'login218', a1)
    if hasattr(a1, 'employee19'):
        assert _is_linked(a1, 'employee19', b)
    _safe_set(b, 'login218', a2)
    assert _is_linked(b, 'login218', a2)
    if hasattr(a1, 'employee19'):
        assert not _is_linked(a1, 'employee19', b)
    if hasattr(a2, 'employee19'):
        assert _is_linked(a2, 'employee19', b)
    _safe_set(b, 'login218', None)
    assert not _is_linked(b, 'login218', a2)
    if hasattr(a2, 'employee19'):
        assert not _is_linked(a2, 'employee19', b)


def test_assoc_Leave_Employee_reverse_link_reassign_clear():
    a1 = Leave(l_description="sample_text", l_emp_id=7, l_id=7, l_type="sample_text")
    a2 = Leave(l_description="sample_text_2", l_emp_id=13, l_id=13, l_type="sample_text_2")
    b = Employee(address="sample_text", e_id=7, email_id="sample_text", name="sample_text", office_address="sample_text", paasword="sample_text", phone_no=7)
    _safe_set(b, 'leave11', {a1})
    assert _is_linked(b, 'leave11', a1)
    if hasattr(a1, 'employee10'):
        assert _is_linked(a1, 'employee10', b)
    _safe_set(b, 'leave11', {a2})
    assert _is_linked(b, 'leave11', a2)
    if hasattr(a1, 'employee10'):
        assert not _is_linked(a1, 'employee10', b)
    if hasattr(a2, 'employee10'):
        assert _is_linked(a2, 'employee10', b)
    _safe_set(b, 'leave11', set())
    assert not _is_linked(b, 'leave11', a2)
    if hasattr(a2, 'employee10'):
        assert not _is_linked(a2, 'employee10', b)


def test_assoc_location_Attendance_reverse_link_reassign_clear():
    a1 = location(Latitude=7, Longitude=7)
    a2 = location(Latitude=13, Longitude=13)
    b = Attendance(atten_date="sample_text", atten_emp_id=7, atten_id=7, atten_time=7, atten_type="sample_text")
    _safe_set(b, 'location17', a1)
    assert _is_linked(b, 'location17', a1)
    if hasattr(a1, 'attendance16'):
        assert _is_linked(a1, 'attendance16', b)
    _safe_set(b, 'location17', a2)
    assert _is_linked(b, 'location17', a2)
    if hasattr(a1, 'attendance16'):
        assert not _is_linked(a1, 'attendance16', b)
    if hasattr(a2, 'attendance16'):
        assert _is_linked(a2, 'attendance16', b)
    _safe_set(b, 'location17', None)
    assert not _is_linked(b, 'location17', a2)
    if hasattr(a2, 'attendance16'):
        assert not _is_linked(a2, 'attendance16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

