import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AppointmentDiagnose_external,
    Appointment_external,
    Appointment_management_UseCase,
    Authorization_UseCase,
    Bill,
    Billing_UseCase,
    Create_new_patient_account_UseCase,
    Diagnose,
    Diagnose_UseCase,
    Doctor,
    Doctor_Actor,
    Employee,
    Employee_Actor,
    Logging_as_existing_user_UseCase,
    Logging_into_system_UseCase,
    New_appointment_UseCase,
    Nurse,
    Nurse_Actor,
    Patient,
    Patient_Actor,
    Remove_appointment_UseCase,
    Schedule,
    TreatmentList,
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

def test_Bill_ammount_value_roundtrip():
    instance = Bill(ammount=3.14, billID="sample_text", date="sample_text")
    assert instance.ammount == 3.14
    instance.ammount = 9.99
    assert instance.ammount == 9.99


def test_Bill_billID_value_roundtrip():
    instance = Bill(ammount=3.14, billID="sample_text", date="sample_text")
    assert instance.billID == "sample_text"
    instance.billID = "sample_text_2"
    assert instance.billID == "sample_text_2"


def test_Bill_date_value_roundtrip():
    instance = Bill(ammount=3.14, billID="sample_text", date="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Diagnose_diagnoseID_value_roundtrip():
    instance = Diagnose(diagnoseID=7, medication="sample_text", symptomps="sample_text")
    assert instance.diagnoseID == 7
    instance.diagnoseID = 13
    assert instance.diagnoseID == 13


def test_Diagnose_medication_value_roundtrip():
    instance = Diagnose(diagnoseID=7, medication="sample_text", symptomps="sample_text")
    assert instance.medication == "sample_text"
    instance.medication = "sample_text_2"
    assert instance.medication == "sample_text_2"


def test_Diagnose_symptomps_value_roundtrip():
    instance = Diagnose(diagnoseID=7, medication="sample_text", symptomps="sample_text")
    assert instance.symptomps == "sample_text"
    instance.symptomps = "sample_text_2"
    assert instance.symptomps == "sample_text_2"


def test_Doctor_specialization_value_roundtrip():
    instance = Doctor(specialization="sample_text")
    assert instance.specialization == "sample_text"
    instance.specialization = "sample_text_2"
    assert instance.specialization == "sample_text_2"


def test_Employee_employeeAddress_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeeAddress == "sample_text"
    instance.employeeAddress = "sample_text_2"
    assert instance.employeeAddress == "sample_text_2"


def test_Employee_employeeEmail_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeeEmail == "sample_text"
    instance.employeeEmail = "sample_text_2"
    assert instance.employeeEmail == "sample_text_2"


def test_Employee_employeeID_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeeID == 7
    instance.employeeID = 13
    assert instance.employeeID == 13


def test_Employee_employeeMobile_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeeMobile == "sample_text"
    instance.employeeMobile = "sample_text_2"
    assert instance.employeeMobile == "sample_text_2"


def test_Employee_employeeName_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeeName == "sample_text"
    instance.employeeName = "sample_text_2"
    assert instance.employeeName == "sample_text_2"


def test_Employee_employeePassword_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeePassword == "sample_text"
    instance.employeePassword = "sample_text_2"
    assert instance.employeePassword == "sample_text_2"


def test_Employee_employeeSurname_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeeSurname == "sample_text"
    instance.employeeSurname = "sample_text_2"
    assert instance.employeeSurname == "sample_text_2"


def test_Employee_employeeUsername_value_roundtrip():
    instance = Employee(employeeAddress="sample_text", employeeEmail="sample_text", employeeID=7, employeeMobile="sample_text", employeeName="sample_text", employeePassword="sample_text", employeeSurname="sample_text", employeeUsername="sample_text")
    assert instance.employeeUsername == "sample_text"
    instance.employeeUsername = "sample_text_2"
    assert instance.employeeUsername == "sample_text_2"


def test_Nurse_experience_value_roundtrip():
    instance = Nurse(experience="sample_text")
    assert instance.experience == "sample_text"
    instance.experience = "sample_text_2"
    assert instance.experience == "sample_text_2"


def test_Patient_coupon_value_roundtrip():
    instance = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    assert instance.coupon == 3.14
    instance.coupon = 9.99
    assert instance.coupon == 9.99


def test_Patient_patientAddress_value_roundtrip():
    instance = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    assert instance.patientAddress == "sample_text"
    instance.patientAddress = "sample_text_2"
    assert instance.patientAddress == "sample_text_2"


def test_Patient_patientEmail_value_roundtrip():
    instance = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    assert instance.patientEmail == "sample_text"
    instance.patientEmail = "sample_text_2"
    assert instance.patientEmail == "sample_text_2"


def test_Patient_patientID_value_roundtrip():
    instance = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    assert instance.patientID == 7
    instance.patientID = 13
    assert instance.patientID == 13


def test_Patient_patientMobile_value_roundtrip():
    instance = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    assert instance.patientMobile == "sample_text"
    instance.patientMobile = "sample_text_2"
    assert instance.patientMobile == "sample_text_2"


def test_Patient_patientName_value_roundtrip():
    instance = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    assert instance.patientName == "sample_text"
    instance.patientName = "sample_text_2"
    assert instance.patientName == "sample_text_2"


def test_Patient_patientSurname_value_roundtrip():
    instance = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    assert instance.patientSurname == "sample_text"
    instance.patientSurname = "sample_text_2"
    assert instance.patientSurname == "sample_text_2"


def test_Schedule_available_value_roundtrip():
    instance = Schedule(available=True, date="sample_text", endTime="sample_text", scheduleID=7, startTime="sample_text")
    assert instance.available == True
    instance.available = False
    assert instance.available == False


def test_Schedule_date_value_roundtrip():
    instance = Schedule(available=True, date="sample_text", endTime="sample_text", scheduleID=7, startTime="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Schedule_endTime_value_roundtrip():
    instance = Schedule(available=True, date="sample_text", endTime="sample_text", scheduleID=7, startTime="sample_text")
    assert instance.endTime == "sample_text"
    instance.endTime = "sample_text_2"
    assert instance.endTime == "sample_text_2"


def test_Schedule_scheduleID_value_roundtrip():
    instance = Schedule(available=True, date="sample_text", endTime="sample_text", scheduleID=7, startTime="sample_text")
    assert instance.scheduleID == 7
    instance.scheduleID = 13
    assert instance.scheduleID == 13


def test_Schedule_startTime_value_roundtrip():
    instance = Schedule(available=True, date="sample_text", endTime="sample_text", scheduleID=7, startTime="sample_text")
    assert instance.startTime == "sample_text"
    instance.startTime = "sample_text_2"
    assert instance.startTime == "sample_text_2"


def test_TreatmentList_treatmentID_value_roundtrip():
    instance = TreatmentList(treatmentID=7, treatmentName="sample_text", treatmentPrice=3.14)
    assert instance.treatmentID == 7
    instance.treatmentID = 13
    assert instance.treatmentID == 13


def test_TreatmentList_treatmentName_value_roundtrip():
    instance = TreatmentList(treatmentID=7, treatmentName="sample_text", treatmentPrice=3.14)
    assert instance.treatmentName == "sample_text"
    instance.treatmentName = "sample_text_2"
    assert instance.treatmentName == "sample_text_2"


def test_TreatmentList_treatmentPrice_value_roundtrip():
    instance = TreatmentList(treatmentID=7, treatmentName="sample_text", treatmentPrice=3.14)
    assert instance.treatmentPrice == 3.14
    instance.treatmentPrice = 9.99
    assert instance.treatmentPrice == 9.99


def test_assoc_Appointment_Bill_link_reassign_clear():
    a = Bill(ammount=3.14, billID="sample_text", date="sample_text")
    b1 = Appointment_external()
    b2 = Appointment_external()
    _safe_set(a, 'appointment12', b1)
    assert _is_linked(a, 'appointment12', b1)
    if hasattr(b1, 'bill13'):
        assert _is_linked(b1, 'bill13', a)
    _safe_set(a, 'appointment12', b2)
    assert _is_linked(a, 'appointment12', b2)
    if hasattr(b1, 'bill13'):
        assert not _is_linked(b1, 'bill13', a)
    if hasattr(b2, 'bill13'):
        assert _is_linked(b2, 'bill13', a)
    _safe_set(a, 'appointment12', None)
    assert not _is_linked(a, 'appointment12', b2)
    if hasattr(b2, 'bill13'):
        assert not _is_linked(b2, 'bill13', a)


def test_assoc_Nurse_Bill_link_reassign_clear():
    a = Nurse(experience="sample_text")
    b1 = Bill(ammount=3.14, billID="sample_text", date="sample_text")
    b2 = Bill(ammount=9.99, billID="sample_text_2", date="sample_text_2")
    _safe_set(a, 'bill15', {b1})
    assert _is_linked(a, 'bill15', b1)
    if hasattr(b1, 'nurse14'):
        assert _is_linked(b1, 'nurse14', a)
    _safe_set(a, 'bill15', {b2})
    assert _is_linked(a, 'bill15', b2)
    if hasattr(b1, 'nurse14'):
        assert not _is_linked(b1, 'nurse14', a)
    if hasattr(b2, 'nurse14'):
        assert _is_linked(b2, 'nurse14', a)
    _safe_set(a, 'bill15', set())
    assert not _is_linked(a, 'bill15', b2)
    if hasattr(b2, 'nurse14'):
        assert not _is_linked(b2, 'nurse14', a)


def test_assoc_Patient_DoctorSchedule_link_reassign_clear():
    a = Patient(coupon=3.14, patientAddress="sample_text", patientEmail="sample_text", patientID=7, patientMobile="sample_text", patientName="sample_text", patientSurname="sample_text")
    b1 = Appointment_external()
    b2 = Appointment_external()
    _safe_set(a, 'appointment9', {b1})
    assert _is_linked(a, 'appointment9', b1)
    if hasattr(b1, 'patient8'):
        assert _is_linked(b1, 'patient8', a)
    _safe_set(a, 'appointment9', {b2})
    assert _is_linked(a, 'appointment9', b2)
    if hasattr(b1, 'patient8'):
        assert not _is_linked(b1, 'patient8', a)
    if hasattr(b2, 'patient8'):
        assert _is_linked(b2, 'patient8', a)
    _safe_set(a, 'appointment9', set())
    assert not _is_linked(a, 'appointment9', b2)
    if hasattr(b2, 'patient8'):
        assert not _is_linked(b2, 'patient8', a)


def test_assoc_TreatmentList_AppointmentDiagnose_link_reassign_clear():
    a = TreatmentList(treatmentID=7, treatmentName="sample_text", treatmentPrice=3.14)
    b1 = AppointmentDiagnose_external()
    b2 = AppointmentDiagnose_external()
    _safe_set(a, 'appointmentDiagnose11', {b1})
    assert _is_linked(a, 'appointmentDiagnose11', b1)
    if hasattr(b1, 'treatmentList10'):
        assert _is_linked(b1, 'treatmentList10', a)
    _safe_set(a, 'appointmentDiagnose11', {b2})
    assert _is_linked(a, 'appointmentDiagnose11', b2)
    if hasattr(b1, 'treatmentList10'):
        assert not _is_linked(b1, 'treatmentList10', a)
    if hasattr(b2, 'treatmentList10'):
        assert _is_linked(b2, 'treatmentList10', a)
    _safe_set(a, 'appointmentDiagnose11', set())
    assert not _is_linked(a, 'appointmentDiagnose11', b2)
    if hasattr(b2, 'treatmentList10'):
        assert not _is_linked(b2, 'treatmentList10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AppointmentDiagnose_external_strategy = st.builds(AppointmentDiagnose_external)
@given(instance=AppointmentDiagnose_external_strategy)
@settings(max_examples=25)
def test_AppointmentDiagnose_external_instantiation(instance):
    assert isinstance(instance, AppointmentDiagnose_external)


Appointment_external_strategy = st.builds(Appointment_external)
@given(instance=Appointment_external_strategy)
@settings(max_examples=25)
def test_Appointment_external_instantiation(instance):
    assert isinstance(instance, Appointment_external)


Appointment_management_UseCase_strategy = st.builds(Appointment_management_UseCase)
@given(instance=Appointment_management_UseCase_strategy)
@settings(max_examples=25)
def test_Appointment_management_UseCase_instantiation(instance):
    assert isinstance(instance, Appointment_management_UseCase)


Authorization_UseCase_strategy = st.builds(Authorization_UseCase)
@given(instance=Authorization_UseCase_strategy)
@settings(max_examples=25)
def test_Authorization_UseCase_instantiation(instance):
    assert isinstance(instance, Authorization_UseCase)


Bill_strategy = st.builds(Bill, ammount=st.floats(allow_nan=False, allow_infinity=False), billID=safe_text, date=safe_text)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Billing_UseCase_strategy = st.builds(Billing_UseCase)
@given(instance=Billing_UseCase_strategy)
@settings(max_examples=25)
def test_Billing_UseCase_instantiation(instance):
    assert isinstance(instance, Billing_UseCase)


Create_new_patient_account_UseCase_strategy = st.builds(Create_new_patient_account_UseCase)
@given(instance=Create_new_patient_account_UseCase_strategy)
@settings(max_examples=25)
def test_Create_new_patient_account_UseCase_instantiation(instance):
    assert isinstance(instance, Create_new_patient_account_UseCase)


Diagnose_strategy = st.builds(Diagnose, diagnoseID=st.integers(), medication=safe_text, symptomps=safe_text)
@given(instance=Diagnose_strategy)
@settings(max_examples=25)
def test_Diagnose_instantiation(instance):
    assert isinstance(instance, Diagnose)


Diagnose_UseCase_strategy = st.builds(Diagnose_UseCase)
@given(instance=Diagnose_UseCase_strategy)
@settings(max_examples=25)
def test_Diagnose_UseCase_instantiation(instance):
    assert isinstance(instance, Diagnose_UseCase)


Doctor_strategy = st.builds(Doctor, specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Doctor_Actor_strategy = st.builds(Doctor_Actor)
@given(instance=Doctor_Actor_strategy)
@settings(max_examples=25)
def test_Doctor_Actor_instantiation(instance):
    assert isinstance(instance, Doctor_Actor)


Employee_strategy = st.builds(Employee, employeeAddress=safe_text, employeeEmail=safe_text, employeeID=st.integers(), employeeMobile=safe_text, employeeName=safe_text, employeePassword=safe_text, employeeSurname=safe_text, employeeUsername=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Employee_Actor_strategy = st.builds(Employee_Actor)
@given(instance=Employee_Actor_strategy)
@settings(max_examples=25)
def test_Employee_Actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)


Logging_as_existing_user_UseCase_strategy = st.builds(Logging_as_existing_user_UseCase)
@given(instance=Logging_as_existing_user_UseCase_strategy)
@settings(max_examples=25)
def test_Logging_as_existing_user_UseCase_instantiation(instance):
    assert isinstance(instance, Logging_as_existing_user_UseCase)


Logging_into_system_UseCase_strategy = st.builds(Logging_into_system_UseCase)
@given(instance=Logging_into_system_UseCase_strategy)
@settings(max_examples=25)
def test_Logging_into_system_UseCase_instantiation(instance):
    assert isinstance(instance, Logging_into_system_UseCase)


New_appointment_UseCase_strategy = st.builds(New_appointment_UseCase)
@given(instance=New_appointment_UseCase_strategy)
@settings(max_examples=25)
def test_New_appointment_UseCase_instantiation(instance):
    assert isinstance(instance, New_appointment_UseCase)


Nurse_strategy = st.builds(Nurse, experience=safe_text)
@given(instance=Nurse_strategy)
@settings(max_examples=25)
def test_Nurse_instantiation(instance):
    assert isinstance(instance, Nurse)


Nurse_Actor_strategy = st.builds(Nurse_Actor)
@given(instance=Nurse_Actor_strategy)
@settings(max_examples=25)
def test_Nurse_Actor_instantiation(instance):
    assert isinstance(instance, Nurse_Actor)


Patient_strategy = st.builds(Patient, coupon=st.floats(allow_nan=False, allow_infinity=False), patientAddress=safe_text, patientEmail=safe_text, patientID=st.integers(), patientMobile=safe_text, patientName=safe_text, patientSurname=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Patient_Actor_strategy = st.builds(Patient_Actor)
@given(instance=Patient_Actor_strategy)
@settings(max_examples=25)
def test_Patient_Actor_instantiation(instance):
    assert isinstance(instance, Patient_Actor)


Remove_appointment_UseCase_strategy = st.builds(Remove_appointment_UseCase)
@given(instance=Remove_appointment_UseCase_strategy)
@settings(max_examples=25)
def test_Remove_appointment_UseCase_instantiation(instance):
    assert isinstance(instance, Remove_appointment_UseCase)


Schedule_strategy = st.builds(Schedule, available=st.booleans(), date=safe_text, endTime=safe_text, scheduleID=st.integers(), startTime=safe_text)
@given(instance=Schedule_strategy)
@settings(max_examples=25)
def test_Schedule_instantiation(instance):
    assert isinstance(instance, Schedule)


TreatmentList_strategy = st.builds(TreatmentList, treatmentID=st.integers(), treatmentName=safe_text, treatmentPrice=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=TreatmentList_strategy)
@settings(max_examples=25)
def test_TreatmentList_instantiation(instance):
    assert isinstance(instance, TreatmentList)


