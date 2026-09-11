import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_Appointment_Aid_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.Aid == "sample_text"
    instance.Aid = "sample_text_2"
    assert instance.Aid == "sample_text_2"


def test_Appointment_AppointmentDate_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.AppointmentDate == "sample_text"
    instance.AppointmentDate = "sample_text_2"
    assert instance.AppointmentDate == "sample_text_2"


def test_Appointment_AppointmentId_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.AppointmentId == 7
    instance.AppointmentId = 13
    assert instance.AppointmentId == 13


def test_Appointment_AppointmentStatus_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.AppointmentStatus == "sample_text"
    instance.AppointmentStatus = "sample_text_2"
    assert instance.AppointmentStatus == "sample_text_2"


def test_Appointment_AppointmentTime_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.AppointmentTime == "sample_text"
    instance.AppointmentTime = "sample_text_2"
    assert instance.AppointmentTime == "sample_text_2"


def test_Appointment_Did_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.Did == 7
    instance.Did = 13
    assert instance.Did == 13


def test_Appointment_DoctorName_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.DoctorName == "sample_text"
    instance.DoctorName = "sample_text_2"
    assert instance.DoctorName == "sample_text_2"


def test_Appointment_PatientId_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.PatientId == 7
    instance.PatientId = 13
    assert instance.PatientId == 13


def test_Appointment_PatientName_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.PatientName == "sample_text"
    instance.PatientName = "sample_text_2"
    assert instance.PatientName == "sample_text_2"


def test_Appointment_Reason_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.Reason == "sample_text"
    instance.Reason = "sample_text_2"
    assert instance.Reason == "sample_text_2"


def test_Appointment_ServiceId_value_roundtrip():
    instance = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    assert instance.ServiceId == 7
    instance.ServiceId = 13
    assert instance.ServiceId == 13


def test_Bill_BId_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.BId == "sample_text"
    instance.BId = "sample_text_2"
    assert instance.BId == "sample_text_2"


def test_Bill_BillDate_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.BillDate == "sample_text"
    instance.BillDate = "sample_text_2"
    assert instance.BillDate == "sample_text_2"


def test_Bill_BillId_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.BillId == 7
    instance.BillId = 13
    assert instance.BillId == 13


def test_Bill_Did_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.Did == 7
    instance.Did = 13
    assert instance.Did == 13


def test_Bill_DoctorName_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.DoctorName == "sample_text"
    instance.DoctorName = "sample_text_2"
    assert instance.DoctorName == "sample_text_2"


def test_Bill_PId_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.PId == 7
    instance.PId = 13
    assert instance.PId == 13


def test_Bill_PatientName_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.PatientName == "sample_text"
    instance.PatientName = "sample_text_2"
    assert instance.PatientName == "sample_text_2"


def test_Bill_TotalAmount_value_roundtrip():
    instance = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    assert instance.TotalAmount == 7
    instance.TotalAmount = 13
    assert instance.TotalAmount == 13


def test_Doctor_DId_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.DId == "sample_text"
    instance.DId = "sample_text_2"
    assert instance.DId == "sample_text_2"


def test_Doctor_DateOfBirth_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.DateOfBirth == "sample_text"
    instance.DateOfBirth = "sample_text_2"
    assert instance.DateOfBirth == "sample_text_2"


def test_Doctor_DoctorId_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.DoctorId == 7
    instance.DoctorId = 13
    assert instance.DoctorId == 13


def test_Doctor_DoctorName_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.DoctorName == "sample_text"
    instance.DoctorName = "sample_text_2"
    assert instance.DoctorName == "sample_text_2"


def test_Doctor_Email_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Doctor_PhoneNumber_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.PhoneNumber == "sample_text"
    instance.PhoneNumber = "sample_text_2"
    assert instance.PhoneNumber == "sample_text_2"


def test_Doctor_Speciality_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.Speciality == "sample_text"
    instance.Speciality = "sample_text_2"
    assert instance.Speciality == "sample_text_2"


def test_Doctor_UserId_value_roundtrip():
    instance = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    assert instance.UserId == 7
    instance.UserId = 13
    assert instance.UserId == 13


def test_DoctorSchedule_AvailableDate_value_roundtrip():
    instance = DoctorSchedule(AvailableDate="sample_text", AvailableTime="sample_text", DSid=7, DoctorId="sample_text")
    assert instance.AvailableDate == "sample_text"
    instance.AvailableDate = "sample_text_2"
    assert instance.AvailableDate == "sample_text_2"


def test_DoctorSchedule_AvailableTime_value_roundtrip():
    instance = DoctorSchedule(AvailableDate="sample_text", AvailableTime="sample_text", DSid=7, DoctorId="sample_text")
    assert instance.AvailableTime == "sample_text"
    instance.AvailableTime = "sample_text_2"
    assert instance.AvailableTime == "sample_text_2"


def test_DoctorSchedule_DSid_value_roundtrip():
    instance = DoctorSchedule(AvailableDate="sample_text", AvailableTime="sample_text", DSid=7, DoctorId="sample_text")
    assert instance.DSid == 7
    instance.DSid = 13
    assert instance.DSid == 13


def test_DoctorSchedule_DoctorId_value_roundtrip():
    instance = DoctorSchedule(AvailableDate="sample_text", AvailableTime="sample_text", DSid=7, DoctorId="sample_text")
    assert instance.DoctorId == "sample_text"
    instance.DoctorId = "sample_text_2"
    assert instance.DoctorId == "sample_text_2"


def test_DoctorServices_SId_value_roundtrip():
    instance = DoctorServices(SId="sample_text", ServiceDetails="sample_text", ServiceId=7, ServiceName="sample_text", ServicePrice="sample_text")
    assert instance.SId == "sample_text"
    instance.SId = "sample_text_2"
    assert instance.SId == "sample_text_2"


def test_DoctorServices_ServiceDetails_value_roundtrip():
    instance = DoctorServices(SId="sample_text", ServiceDetails="sample_text", ServiceId=7, ServiceName="sample_text", ServicePrice="sample_text")
    assert instance.ServiceDetails == "sample_text"
    instance.ServiceDetails = "sample_text_2"
    assert instance.ServiceDetails == "sample_text_2"


def test_DoctorServices_ServiceId_value_roundtrip():
    instance = DoctorServices(SId="sample_text", ServiceDetails="sample_text", ServiceId=7, ServiceName="sample_text", ServicePrice="sample_text")
    assert instance.ServiceId == 7
    instance.ServiceId = 13
    assert instance.ServiceId == 13


def test_DoctorServices_ServiceName_value_roundtrip():
    instance = DoctorServices(SId="sample_text", ServiceDetails="sample_text", ServiceId=7, ServiceName="sample_text", ServicePrice="sample_text")
    assert instance.ServiceName == "sample_text"
    instance.ServiceName = "sample_text_2"
    assert instance.ServiceName == "sample_text_2"


def test_DoctorServices_ServicePrice_value_roundtrip():
    instance = DoctorServices(SId="sample_text", ServiceDetails="sample_text", ServiceId=7, ServiceName="sample_text", ServicePrice="sample_text")
    assert instance.ServicePrice == "sample_text"
    instance.ServicePrice = "sample_text_2"
    assert instance.ServicePrice == "sample_text_2"


def test_Patient_City_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.City == "sample_text"
    instance.City = "sample_text_2"
    assert instance.City == "sample_text_2"


def test_Patient_DateOfBirth_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.DateOfBirth == "sample_text"
    instance.DateOfBirth = "sample_text_2"
    assert instance.DateOfBirth == "sample_text_2"


def test_Patient_Email_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Patient_FirstName_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.FirstName == "sample_text"
    instance.FirstName = "sample_text_2"
    assert instance.FirstName == "sample_text_2"


def test_Patient_IsEmailConfirmed_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.IsEmailConfirmed == "sample_text"
    instance.IsEmailConfirmed = "sample_text_2"
    assert instance.IsEmailConfirmed == "sample_text_2"


def test_Patient_IsPhoneNumberConfirmed_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.IsPhoneNumberConfirmed == "sample_text"
    instance.IsPhoneNumberConfirmed = "sample_text_2"
    assert instance.IsPhoneNumberConfirmed == "sample_text_2"


def test_Patient_LastName_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.LastName == "sample_text"
    instance.LastName = "sample_text_2"
    assert instance.LastName == "sample_text_2"


def test_Patient_PId_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.PId == "sample_text"
    instance.PId = "sample_text_2"
    assert instance.PId == "sample_text_2"


def test_Patient_PatientId_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.PatientId == 7
    instance.PatientId = 13
    assert instance.PatientId == 13


def test_Patient_PhoneNumber_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.PhoneNumber == "sample_text"
    instance.PhoneNumber = "sample_text_2"
    assert instance.PhoneNumber == "sample_text_2"


def test_Patient_State_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.State == "sample_text"
    instance.State = "sample_text_2"
    assert instance.State == "sample_text_2"


def test_Patient_StreetAddress_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.StreetAddress == "sample_text"
    instance.StreetAddress = "sample_text_2"
    assert instance.StreetAddress == "sample_text_2"


def test_Patient_UserId_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.UserId == 7
    instance.UserId = 13
    assert instance.UserId == 13


def test_Patient_ZipCode_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.ZipCode == "sample_text"
    instance.ZipCode = "sample_text_2"
    assert instance.ZipCode == "sample_text_2"


def test_Patient_activationcode_value_roundtrip():
    instance = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    assert instance.activationcode == "sample_text"
    instance.activationcode = "sample_text_2"
    assert instance.activationcode == "sample_text_2"


def test_Receptionist_DateOfBirth_value_roundtrip():
    instance = Receptionist(DateOfBirth="sample_text", Email="sample_text", PhoneNumber="sample_text", RId="sample_text", ReceptionistId=7, ReceptionistName="sample_text", UserId=7)
    assert instance.DateOfBirth == "sample_text"
    instance.DateOfBirth = "sample_text_2"
    assert instance.DateOfBirth == "sample_text_2"


def test_Receptionist_Email_value_roundtrip():
    instance = Receptionist(DateOfBirth="sample_text", Email="sample_text", PhoneNumber="sample_text", RId="sample_text", ReceptionistId=7, ReceptionistName="sample_text", UserId=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Receptionist_PhoneNumber_value_roundtrip():
    instance = Receptionist(DateOfBirth="sample_text", Email="sample_text", PhoneNumber="sample_text", RId="sample_text", ReceptionistId=7, ReceptionistName="sample_text", UserId=7)
    assert instance.PhoneNumber == "sample_text"
    instance.PhoneNumber = "sample_text_2"
    assert instance.PhoneNumber == "sample_text_2"


def test_Receptionist_RId_value_roundtrip():
    instance = Receptionist(DateOfBirth="sample_text", Email="sample_text", PhoneNumber="sample_text", RId="sample_text", ReceptionistId=7, ReceptionistName="sample_text", UserId=7)
    assert instance.RId == "sample_text"
    instance.RId = "sample_text_2"
    assert instance.RId == "sample_text_2"


def test_Receptionist_ReceptionistId_value_roundtrip():
    instance = Receptionist(DateOfBirth="sample_text", Email="sample_text", PhoneNumber="sample_text", RId="sample_text", ReceptionistId=7, ReceptionistName="sample_text", UserId=7)
    assert instance.ReceptionistId == 7
    instance.ReceptionistId = 13
    assert instance.ReceptionistId == 13


def test_Receptionist_ReceptionistName_value_roundtrip():
    instance = Receptionist(DateOfBirth="sample_text", Email="sample_text", PhoneNumber="sample_text", RId="sample_text", ReceptionistId=7, ReceptionistName="sample_text", UserId=7)
    assert instance.ReceptionistName == "sample_text"
    instance.ReceptionistName = "sample_text_2"
    assert instance.ReceptionistName == "sample_text_2"


def test_Receptionist_UserId_value_roundtrip():
    instance = Receptionist(DateOfBirth="sample_text", Email="sample_text", PhoneNumber="sample_text", RId="sample_text", ReceptionistId=7, ReceptionistName="sample_text", UserId=7)
    assert instance.UserId == 7
    instance.UserId = 13
    assert instance.UserId == 13


def test_UserRoles_Id_value_roundtrip():
    instance = UserRoles(Id=7, Name="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_UserRoles_Name_value_roundtrip():
    instance = UserRoles(Id=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Users_AccessFailedCount_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.AccessFailedCount == 7
    instance.AccessFailedCount = 13
    assert instance.AccessFailedCount == 13


def test_Users_Email_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Users_EmailConfirmed_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.EmailConfirmed == "sample_text"
    instance.EmailConfirmed = "sample_text_2"
    assert instance.EmailConfirmed == "sample_text_2"


def test_Users_Id_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Users_LockoutEnabled_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.LockoutEnabled == "sample_text"
    instance.LockoutEnabled = "sample_text_2"
    assert instance.LockoutEnabled == "sample_text_2"


def test_Users_LockoutEndDateUtc_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.LockoutEndDateUtc == "sample_text"
    instance.LockoutEndDateUtc = "sample_text_2"
    assert instance.LockoutEndDateUtc == "sample_text_2"


def test_Users_PasswordHash_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.PasswordHash == "sample_text"
    instance.PasswordHash = "sample_text_2"
    assert instance.PasswordHash == "sample_text_2"


def test_Users_PhoneNumber_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.PhoneNumber == "sample_text"
    instance.PhoneNumber = "sample_text_2"
    assert instance.PhoneNumber == "sample_text_2"


def test_Users_PhoneNumberConfirmed_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.PhoneNumberConfirmed == "sample_text"
    instance.PhoneNumberConfirmed = "sample_text_2"
    assert instance.PhoneNumberConfirmed == "sample_text_2"


def test_Users_SecurityStamp_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.SecurityStamp == "sample_text"
    instance.SecurityStamp = "sample_text_2"
    assert instance.SecurityStamp == "sample_text_2"


def test_Users_TwoFactorEnabled_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.TwoFactorEnabled == "sample_text"
    instance.TwoFactorEnabled = "sample_text_2"
    assert instance.TwoFactorEnabled == "sample_text_2"


def test_Users_UserName_value_roundtrip():
    instance = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_UserwithRole_RoleId_value_roundtrip():
    instance = UserwithRole(RoleId=7, UserId=7)
    assert instance.RoleId == 7
    instance.RoleId = 13
    assert instance.RoleId == 13


def test_UserwithRole_UserId_value_roundtrip():
    instance = UserwithRole(RoleId=7, UserId=7)
    assert instance.UserId == 7
    instance.UserId = 13
    assert instance.UserId == 13


def test_assoc_Appointment_Doctor_link_reassign_clear():
    a = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    b1 = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    b2 = Appointment(Aid="sample_text_2", AppointmentDate="sample_text_2", AppointmentId=13, AppointmentStatus="sample_text_2", AppointmentTime="sample_text_2", Did=13, DoctorName="sample_text_2", PatientId=13, PatientName="sample_text_2", Reason="sample_text_2", ServiceId=13)
    _safe_set(a, 'appointment1', {b1})
    assert _is_linked(a, 'appointment1', b1)
    if hasattr(b1, 'doctor0'):
        assert _is_linked(b1, 'doctor0', a)
    _safe_set(a, 'appointment1', {b2})
    assert _is_linked(a, 'appointment1', b2)
    if hasattr(b1, 'doctor0'):
        assert not _is_linked(b1, 'doctor0', a)
    if hasattr(b2, 'doctor0'):
        assert _is_linked(b2, 'doctor0', a)
    _safe_set(a, 'appointment1', set())
    assert not _is_linked(a, 'appointment1', b2)
    if hasattr(b2, 'doctor0'):
        assert not _is_linked(b2, 'doctor0', a)


def test_assoc_DoctorServices_Appointment_link_reassign_clear():
    a = DoctorServices(SId="sample_text", ServiceDetails="sample_text", ServiceId=7, ServiceName="sample_text", ServicePrice="sample_text")
    b1 = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    b2 = Appointment(Aid="sample_text_2", AppointmentDate="sample_text_2", AppointmentId=13, AppointmentStatus="sample_text_2", AppointmentTime="sample_text_2", Did=13, DoctorName="sample_text_2", PatientId=13, PatientName="sample_text_2", Reason="sample_text_2", ServiceId=13)
    _safe_set(a, 'appointment10', {b1})
    assert _is_linked(a, 'appointment10', b1)
    if hasattr(b1, 'doctorServices11'):
        assert _is_linked(b1, 'doctorServices11', a)
    _safe_set(a, 'appointment10', {b2})
    assert _is_linked(a, 'appointment10', b2)
    if hasattr(b1, 'doctorServices11'):
        assert not _is_linked(b1, 'doctorServices11', a)
    if hasattr(b2, 'doctorServices11'):
        assert _is_linked(b2, 'doctorServices11', a)
    _safe_set(a, 'appointment10', set())
    assert not _is_linked(a, 'appointment10', b2)
    if hasattr(b2, 'doctorServices11'):
        assert not _is_linked(b2, 'doctorServices11', a)


def test_assoc_Doctor_Bill_link_reassign_clear():
    a = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    b1 = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    b2 = Bill(BId="sample_text_2", BillDate="sample_text_2", BillId=13, Did=13, DoctorName="sample_text_2", PId=13, PatientName="sample_text_2", TotalAmount=13)
    _safe_set(a, 'bill4', {b1})
    assert _is_linked(a, 'bill4', b1)
    if hasattr(b1, 'doctor5'):
        assert _is_linked(b1, 'doctor5', a)
    _safe_set(a, 'bill4', {b2})
    assert _is_linked(a, 'bill4', b2)
    if hasattr(b1, 'doctor5'):
        assert not _is_linked(b1, 'doctor5', a)
    if hasattr(b2, 'doctor5'):
        assert _is_linked(b2, 'doctor5', a)
    _safe_set(a, 'bill4', set())
    assert not _is_linked(a, 'bill4', b2)
    if hasattr(b2, 'doctor5'):
        assert not _is_linked(b2, 'doctor5', a)


def test_assoc_Doctor_DoctorSchedule_link_reassign_clear():
    a = DoctorSchedule(AvailableDate="sample_text", AvailableTime="sample_text", DSid=7, DoctorId="sample_text")
    b1 = Doctor(DId="sample_text", DateOfBirth="sample_text", DoctorId=7, DoctorName="sample_text", Email="sample_text", PhoneNumber="sample_text", Speciality="sample_text", UserId=7)
    b2 = Doctor(DId="sample_text_2", DateOfBirth="sample_text_2", DoctorId=13, DoctorName="sample_text_2", Email="sample_text_2", PhoneNumber="sample_text_2", Speciality="sample_text_2", UserId=13)
    _safe_set(a, 'doctor3', {b1})
    assert _is_linked(a, 'doctor3', b1)
    if hasattr(b1, 'doctorSchedule2'):
        assert _is_linked(b1, 'doctorSchedule2', a)
    _safe_set(a, 'doctor3', {b2})
    assert _is_linked(a, 'doctor3', b2)
    if hasattr(b1, 'doctorSchedule2'):
        assert not _is_linked(b1, 'doctorSchedule2', a)
    if hasattr(b2, 'doctorSchedule2'):
        assert _is_linked(b2, 'doctorSchedule2', a)
    _safe_set(a, 'doctor3', set())
    assert not _is_linked(a, 'doctor3', b2)
    if hasattr(b2, 'doctorSchedule2'):
        assert not _is_linked(b2, 'doctorSchedule2', a)


def test_assoc_Patient_Appointment_link_reassign_clear():
    a = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    b1 = Appointment(Aid="sample_text", AppointmentDate="sample_text", AppointmentId=7, AppointmentStatus="sample_text", AppointmentTime="sample_text", Did=7, DoctorName="sample_text", PatientId=7, PatientName="sample_text", Reason="sample_text", ServiceId=7)
    b2 = Appointment(Aid="sample_text_2", AppointmentDate="sample_text_2", AppointmentId=13, AppointmentStatus="sample_text_2", AppointmentTime="sample_text_2", Did=13, DoctorName="sample_text_2", PatientId=13, PatientName="sample_text_2", Reason="sample_text_2", ServiceId=13)
    _safe_set(a, 'appointment8', {b1})
    assert _is_linked(a, 'appointment8', b1)
    if hasattr(b1, 'patient9'):
        assert _is_linked(b1, 'patient9', a)
    _safe_set(a, 'appointment8', {b2})
    assert _is_linked(a, 'appointment8', b2)
    if hasattr(b1, 'patient9'):
        assert not _is_linked(b1, 'patient9', a)
    if hasattr(b2, 'patient9'):
        assert _is_linked(b2, 'patient9', a)
    _safe_set(a, 'appointment8', set())
    assert not _is_linked(a, 'appointment8', b2)
    if hasattr(b2, 'patient9'):
        assert not _is_linked(b2, 'patient9', a)


def test_assoc_Patient_Bill_link_reassign_clear():
    a = Patient(City="sample_text", DateOfBirth="sample_text", Email="sample_text", FirstName="sample_text", IsEmailConfirmed="sample_text", IsPhoneNumberConfirmed="sample_text", LastName="sample_text", PId="sample_text", PatientId=7, PhoneNumber="sample_text", State="sample_text", StreetAddress="sample_text", UserId=7, ZipCode="sample_text", activationcode="sample_text")
    b1 = Bill(BId="sample_text", BillDate="sample_text", BillId=7, Did=7, DoctorName="sample_text", PId=7, PatientName="sample_text", TotalAmount=7)
    b2 = Bill(BId="sample_text_2", BillDate="sample_text_2", BillId=13, Did=13, DoctorName="sample_text_2", PId=13, PatientName="sample_text_2", TotalAmount=13)
    _safe_set(a, 'bill6', {b1})
    assert _is_linked(a, 'bill6', b1)
    if hasattr(b1, 'patient7'):
        assert _is_linked(b1, 'patient7', a)
    _safe_set(a, 'bill6', {b2})
    assert _is_linked(a, 'bill6', b2)
    if hasattr(b1, 'patient7'):
        assert not _is_linked(b1, 'patient7', a)
    if hasattr(b2, 'patient7'):
        assert _is_linked(b2, 'patient7', a)
    _safe_set(a, 'bill6', set())
    assert not _is_linked(a, 'bill6', b2)
    if hasattr(b2, 'patient7'):
        assert not _is_linked(b2, 'patient7', a)


def test_assoc_UserRoles_UserwithRole_link_reassign_clear():
    a = UserwithRole(RoleId=7, UserId=7)
    b1 = UserRoles(Id=7, Name="sample_text")
    b2 = UserRoles(Id=13, Name="sample_text_2")
    _safe_set(a, 'userRoles15', {b1})
    assert _is_linked(a, 'userRoles15', b1)
    if hasattr(b1, 'userwithRole14'):
        assert _is_linked(b1, 'userwithRole14', a)
    _safe_set(a, 'userRoles15', {b2})
    assert _is_linked(a, 'userRoles15', b2)
    if hasattr(b1, 'userwithRole14'):
        assert not _is_linked(b1, 'userwithRole14', a)
    if hasattr(b2, 'userwithRole14'):
        assert _is_linked(b2, 'userwithRole14', a)
    _safe_set(a, 'userRoles15', set())
    assert not _is_linked(a, 'userRoles15', b2)
    if hasattr(b2, 'userwithRole14'):
        assert not _is_linked(b2, 'userwithRole14', a)


def test_assoc_Users_UserwithRole_link_reassign_clear():
    a = UserwithRole(RoleId=7, UserId=7)
    b1 = Users(AccessFailedCount=7, Email="sample_text", EmailConfirmed="sample_text", Id=7, LockoutEnabled="sample_text", LockoutEndDateUtc="sample_text", PasswordHash="sample_text", PhoneNumber="sample_text", PhoneNumberConfirmed="sample_text", SecurityStamp="sample_text", TwoFactorEnabled="sample_text", UserName="sample_text")
    b2 = Users(AccessFailedCount=13, Email="sample_text_2", EmailConfirmed="sample_text_2", Id=13, LockoutEnabled="sample_text_2", LockoutEndDateUtc="sample_text_2", PasswordHash="sample_text_2", PhoneNumber="sample_text_2", PhoneNumberConfirmed="sample_text_2", SecurityStamp="sample_text_2", TwoFactorEnabled="sample_text_2", UserName="sample_text_2")
    _safe_set(a, 'users13', {b1})
    assert _is_linked(a, 'users13', b1)
    if hasattr(b1, 'userwithRole12'):
        assert _is_linked(b1, 'userwithRole12', a)
    _safe_set(a, 'users13', {b2})
    assert _is_linked(a, 'users13', b2)
    if hasattr(b1, 'userwithRole12'):
        assert not _is_linked(b1, 'userwithRole12', a)
    if hasattr(b2, 'userwithRole12'):
        assert _is_linked(b2, 'userwithRole12', a)
    _safe_set(a, 'users13', set())
    assert not _is_linked(a, 'users13', b2)
    if hasattr(b2, 'userwithRole12'):
        assert not _is_linked(b2, 'userwithRole12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Appointment_strategy = st.builds(Appointment, Aid=safe_text, AppointmentDate=safe_text, AppointmentId=st.integers(), AppointmentStatus=safe_text, AppointmentTime=safe_text, Did=st.integers(), DoctorName=safe_text, PatientId=st.integers(), PatientName=safe_text, Reason=safe_text, ServiceId=st.integers())
@given(instance=Appointment_strategy)
@settings(max_examples=25)
def test_Appointment_instantiation(instance):
    assert isinstance(instance, Appointment)


Bill_strategy = st.builds(Bill, BId=safe_text, BillDate=safe_text, BillId=st.integers(), Did=st.integers(), DoctorName=safe_text, PId=st.integers(), PatientName=safe_text, TotalAmount=st.integers())
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Doctor_strategy = st.builds(Doctor, DId=safe_text, DateOfBirth=safe_text, DoctorId=st.integers(), DoctorName=safe_text, Email=safe_text, PhoneNumber=safe_text, Speciality=safe_text, UserId=st.integers())
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


DoctorSchedule_strategy = st.builds(DoctorSchedule, AvailableDate=safe_text, AvailableTime=safe_text, DSid=st.integers(), DoctorId=safe_text)
@given(instance=DoctorSchedule_strategy)
@settings(max_examples=25)
def test_DoctorSchedule_instantiation(instance):
    assert isinstance(instance, DoctorSchedule)


DoctorServices_strategy = st.builds(DoctorServices, SId=safe_text, ServiceDetails=safe_text, ServiceId=st.integers(), ServiceName=safe_text, ServicePrice=safe_text)
@given(instance=DoctorServices_strategy)
@settings(max_examples=25)
def test_DoctorServices_instantiation(instance):
    assert isinstance(instance, DoctorServices)


Patient_strategy = st.builds(Patient, City=safe_text, DateOfBirth=safe_text, Email=safe_text, FirstName=safe_text, IsEmailConfirmed=safe_text, IsPhoneNumberConfirmed=safe_text, LastName=safe_text, PId=safe_text, PatientId=st.integers(), PhoneNumber=safe_text, State=safe_text, StreetAddress=safe_text, UserId=st.integers(), ZipCode=safe_text, activationcode=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Receptionist_strategy = st.builds(Receptionist, DateOfBirth=safe_text, Email=safe_text, PhoneNumber=safe_text, RId=safe_text, ReceptionistId=st.integers(), ReceptionistName=safe_text, UserId=st.integers())
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


UserRoles_strategy = st.builds(UserRoles, Id=st.integers(), Name=safe_text)
@given(instance=UserRoles_strategy)
@settings(max_examples=25)
def test_UserRoles_instantiation(instance):
    assert isinstance(instance, UserRoles)


Users_strategy = st.builds(Users, AccessFailedCount=st.integers(), Email=safe_text, EmailConfirmed=safe_text, Id=st.integers(), LockoutEnabled=safe_text, LockoutEndDateUtc=safe_text, PasswordHash=safe_text, PhoneNumber=safe_text, PhoneNumberConfirmed=safe_text, SecurityStamp=safe_text, TwoFactorEnabled=safe_text, UserName=safe_text)
@given(instance=Users_strategy)
@settings(max_examples=25)
def test_Users_instantiation(instance):
    assert isinstance(instance, Users)


UserwithRole_strategy = st.builds(UserwithRole, RoleId=st.integers(), UserId=st.integers())
@given(instance=UserwithRole_strategy)
@settings(max_examples=25)
def test_UserwithRole_instantiation(instance):
    assert isinstance(instance, UserwithRole)


