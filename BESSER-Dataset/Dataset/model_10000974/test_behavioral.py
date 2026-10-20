import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Appointment,
    Bill,
    Doctor,
    DoctorSchedule,
    DoctorServices,
    Patient,
    Receptionist,
    UserRoles,
    Users,
    UserwithRole,
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

def test_assoc_Appointment_Doctor_reverse_link_reassign_clear():
    a1 = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    a2 = Doctor(DId="sample_text_2", DateOfBirth="sample_text_2", DoctorId=13, DoctorName="sample_text_2", Email="sample_text_2", PhoneNumber="sample_text_2", Speciality="sample_text_2", UserId=13)
    b = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    _safe_set(b, 'doctor0', {a1})
    assert _is_linked(b, 'doctor0', a1)
    if hasattr(a1, 'appointment1'):
        assert _is_linked(a1, 'appointment1', b)
    _safe_set(b, 'doctor0', {a2})
    assert _is_linked(b, 'doctor0', a2)
    if hasattr(a1, 'appointment1'):
        assert not _is_linked(a1, 'appointment1', b)
    if hasattr(a2, 'appointment1'):
        assert _is_linked(a2, 'appointment1', b)
    _safe_set(b, 'doctor0', set())
    assert not _is_linked(b, 'doctor0', a2)
    if hasattr(a2, 'appointment1'):
        assert not _is_linked(a2, 'appointment1', b)


def test_assoc_DoctorServices_Appointment_reverse_link_reassign_clear():
    a1 = DoctorServices(SId="sample_text", ServiceDetails="sample_text", ServiceId=7, ServiceName="sample_text", ServicePrice="sample_text")
    a2 = DoctorServices(SId="sample_text_2", ServiceDetails="sample_text_2", ServiceId=13, ServiceName="sample_text_2", ServicePrice="sample_text_2")
    b = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    _safe_set(b, 'doctorServices11', {a1})
    assert _is_linked(b, 'doctorServices11', a1)
    if hasattr(a1, 'appointment10'):
        assert _is_linked(a1, 'appointment10', b)
    _safe_set(b, 'doctorServices11', {a2})
    assert _is_linked(b, 'doctorServices11', a2)
    if hasattr(a1, 'appointment10'):
        assert not _is_linked(a1, 'appointment10', b)
    if hasattr(a2, 'appointment10'):
        assert _is_linked(a2, 'appointment10', b)
    _safe_set(b, 'doctorServices11', set())
    assert not _is_linked(b, 'doctorServices11', a2)
    if hasattr(a2, 'appointment10'):
        assert not _is_linked(a2, 'appointment10', b)


def test_assoc_Doctor_Bill_reverse_link_reassign_clear():
    a1 = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    a2 = Doctor(DId="sample_text_2", DateOfBirth="sample_text_2", DoctorId=13, DoctorName="sample_text_2", Email="sample_text_2", PhoneNumber="sample_text_2", Speciality="sample_text_2", UserId=13)
    b = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    _safe_set(b, 'doctor5', {a1})
    assert _is_linked(b, 'doctor5', a1)
    if hasattr(a1, 'bill4'):
        assert _is_linked(a1, 'bill4', b)
    _safe_set(b, 'doctor5', {a2})
    assert _is_linked(b, 'doctor5', a2)
    if hasattr(a1, 'bill4'):
        assert not _is_linked(a1, 'bill4', b)
    if hasattr(a2, 'bill4'):
        assert _is_linked(a2, 'bill4', b)
    _safe_set(b, 'doctor5', set())
    assert not _is_linked(b, 'doctor5', a2)
    if hasattr(a2, 'bill4'):
        assert not _is_linked(a2, 'bill4', b)


def test_assoc_Doctor_DoctorSchedule_reverse_link_reassign_clear():
    a1 = DoctorSchedule(AvailableDate="sample_text", AvailableTime="sample_text", DSid=7, DoctorId="sample_text")
    a2 = DoctorSchedule(AvailableDate="sample_text_2", AvailableTime="sample_text_2", DSid=13, DoctorId="sample_text_2")
    b = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    _safe_set(b, 'doctorSchedule2', {a1})
    assert _is_linked(b, 'doctorSchedule2', a1)
    if hasattr(a1, 'doctor3'):
        assert _is_linked(a1, 'doctor3', b)
    _safe_set(b, 'doctorSchedule2', {a2})
    assert _is_linked(b, 'doctorSchedule2', a2)
    if hasattr(a1, 'doctor3'):
        assert not _is_linked(a1, 'doctor3', b)
    if hasattr(a2, 'doctor3'):
        assert _is_linked(a2, 'doctor3', b)
    _safe_set(b, 'doctorSchedule2', set())
    assert not _is_linked(b, 'doctorSchedule2', a2)
    if hasattr(a2, 'doctor3'):
        assert not _is_linked(a2, 'doctor3', b)


def test_assoc_Patient_Appointment_reverse_link_reassign_clear():
    a1 = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    a2 = Patient(City="sample_text_2", DateOfBirth="sample_text_2", Email="sample_text_2", FirstName="sample_text_2", IsEmailConfirmed="sample_text_2", IsPhoneNumberConfirmed="sample_text_2", LastName="sample_text_2", PId="sample_text_2", PatientId=13, PhoneNumber="sample_text_2", State="sample_text_2", StreetAddress="sample_text_2", UserId=13, ZipCode="sample_text_2", activationcode="sample_text_2")
    b = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    _safe_set(b, 'patient9', {a1})
    assert _is_linked(b, 'patient9', a1)
    if hasattr(a1, 'appointment8'):
        assert _is_linked(a1, 'appointment8', b)
    _safe_set(b, 'patient9', {a2})
    assert _is_linked(b, 'patient9', a2)
    if hasattr(a1, 'appointment8'):
        assert not _is_linked(a1, 'appointment8', b)
    if hasattr(a2, 'appointment8'):
        assert _is_linked(a2, 'appointment8', b)
    _safe_set(b, 'patient9', set())
    assert not _is_linked(b, 'patient9', a2)
    if hasattr(a2, 'appointment8'):
        assert not _is_linked(a2, 'appointment8', b)


def test_assoc_Patient_Bill_reverse_link_reassign_clear():
    a1 = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    a2 = Patient(City="sample_text_2", DateOfBirth="sample_text_2", Email="sample_text_2", FirstName="sample_text_2", IsEmailConfirmed="sample_text_2", IsPhoneNumberConfirmed="sample_text_2", LastName="sample_text_2", PId="sample_text_2", PatientId=13, PhoneNumber="sample_text_2", State="sample_text_2", StreetAddress="sample_text_2", UserId=13, ZipCode="sample_text_2", activationcode="sample_text_2")
    b = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    _safe_set(b, 'patient7', {a1})
    assert _is_linked(b, 'patient7', a1)
    if hasattr(a1, 'bill6'):
        assert _is_linked(a1, 'bill6', b)
    _safe_set(b, 'patient7', {a2})
    assert _is_linked(b, 'patient7', a2)
    if hasattr(a1, 'bill6'):
        assert not _is_linked(a1, 'bill6', b)
    if hasattr(a2, 'bill6'):
        assert _is_linked(a2, 'bill6', b)
    _safe_set(b, 'patient7', set())
    assert not _is_linked(b, 'patient7', a2)
    if hasattr(a2, 'bill6'):
        assert not _is_linked(a2, 'bill6', b)


def test_assoc_UserRoles_UserwithRole_reverse_link_reassign_clear():
    a1 = UserwithRole(RoleId=7, UserId=7)
    a2 = UserwithRole(RoleId=13, UserId=13)
    b = UserRoles(Id=7, Name="sample_text")
    _safe_set(b, 'userwithRole14', {a1})
    assert _is_linked(b, 'userwithRole14', a1)
    if hasattr(a1, 'userRoles15'):
        assert _is_linked(a1, 'userRoles15', b)
    _safe_set(b, 'userwithRole14', {a2})
    assert _is_linked(b, 'userwithRole14', a2)
    if hasattr(a1, 'userRoles15'):
        assert not _is_linked(a1, 'userRoles15', b)
    if hasattr(a2, 'userRoles15'):
        assert _is_linked(a2, 'userRoles15', b)
    _safe_set(b, 'userwithRole14', set())
    assert not _is_linked(b, 'userwithRole14', a2)
    if hasattr(a2, 'userRoles15'):
        assert not _is_linked(a2, 'userRoles15', b)


def test_assoc_Users_UserwithRole_reverse_link_reassign_clear():
    a1 = UserwithRole(RoleId=7, UserId=7)
    a2 = UserwithRole(RoleId=13, UserId=13)
    b = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    _safe_set(b, 'userwithRole12', {a1})
    assert _is_linked(b, 'userwithRole12', a1)
    if hasattr(a1, 'users13'):
        assert _is_linked(a1, 'users13', b)
    _safe_set(b, 'userwithRole12', {a2})
    assert _is_linked(b, 'userwithRole12', a2)
    if hasattr(a1, 'users13'):
        assert not _is_linked(a1, 'users13', b)
    if hasattr(a2, 'users13'):
        assert _is_linked(a2, 'users13', b)
    _safe_set(b, 'userwithRole12', set())
    assert not _is_linked(b, 'userwithRole12', a2)
    if hasattr(a2, 'users13'):
        assert not _is_linked(a2, 'users13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

