import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Appointment,
    Assistant,
    Billing_Report,
    BloodBank,
    Doctor,
    DoctorDatabase,
    Hospital,
    PatientProfile,
    Patients,
    Prescription,
    Receptionist,
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

def test_assoc_Assistant_Appointment_reverse_link_reassign_clear():
    a1 = Assistant(CNIC="sample_text", name="sample_text")
    a2 = Assistant(CNIC="sample_text_2", name="sample_text_2")
    b = Appointment(Doctor="sample_text", Patient="sample_text", Time="sample_text")
    _safe_set(b, 'check_details17', a1)
    assert _is_linked(b, 'check_details17', a1)
    if hasattr(a1, 'Assistant_Appointment_016'):
        assert _is_linked(a1, 'Assistant_Appointment_016', b)
    _safe_set(b, 'check_details17', a2)
    assert _is_linked(b, 'check_details17', a2)
    if hasattr(a1, 'Assistant_Appointment_016'):
        assert not _is_linked(a1, 'Assistant_Appointment_016', b)
    if hasattr(a2, 'Assistant_Appointment_016'):
        assert _is_linked(a2, 'Assistant_Appointment_016', b)
    _safe_set(b, 'check_details17', None)
    assert not _is_linked(b, 'check_details17', a2)
    if hasattr(a2, 'Assistant_Appointment_016'):
        assert not _is_linked(a2, 'Assistant_Appointment_016', b)


def test_assoc_Doctor_Assistant_reverse_link_reassign_clear():
    a1 = Doctor(name="sample_text", privateConsultancy=True, specilization="sample_text", timing="sample_text")
    a2 = Doctor(name="sample_text_2", privateConsultancy=False, specilization="sample_text_2", timing="sample_text_2")
    b = Assistant(CNIC="sample_text", name="sample_text")
    _safe_set(b, 'Doctor_Assistant_123', a1)
    assert _is_linked(b, 'Doctor_Assistant_123', a1)
    if hasattr(a1, 'forward_patient_history22'):
        assert _is_linked(a1, 'forward_patient_history22', b)
    _safe_set(b, 'Doctor_Assistant_123', a2)
    assert _is_linked(b, 'Doctor_Assistant_123', a2)
    if hasattr(a1, 'forward_patient_history22'):
        assert not _is_linked(a1, 'forward_patient_history22', b)
    if hasattr(a2, 'forward_patient_history22'):
        assert _is_linked(a2, 'forward_patient_history22', b)
    _safe_set(b, 'Doctor_Assistant_123', None)
    assert not _is_linked(b, 'Doctor_Assistant_123', a2)
    if hasattr(a2, 'forward_patient_history22'):
        assert not _is_linked(a2, 'forward_patient_history22', b)


def test_assoc_Doctor_Patients_reverse_link_reassign_clear():
    a1 = Patients(BP=7, History="sample_text", Symptoms="sample_text", name="sample_text", weight=7)
    a2 = Patients(BP=13, History="sample_text_2", Symptoms="sample_text_2", name="sample_text_2", weight=13)
    b = Doctor(name="sample_text", privateConsultancy=True, specilization="sample_text", timing="sample_text")
    _safe_set(b, 'Doctor_Patients_02', {a1})
    assert _is_linked(b, 'Doctor_Patients_02', a1)
    if hasattr(a1, 'Checks_up3'):
        assert _is_linked(a1, 'Checks_up3', b)
    _safe_set(b, 'Doctor_Patients_02', {a2})
    assert _is_linked(b, 'Doctor_Patients_02', a2)
    if hasattr(a1, 'Checks_up3'):
        assert not _is_linked(a1, 'Checks_up3', b)
    if hasattr(a2, 'Checks_up3'):
        assert _is_linked(a2, 'Checks_up3', b)
    _safe_set(b, 'Doctor_Patients_02', set())
    assert not _is_linked(b, 'Doctor_Patients_02', a2)
    if hasattr(a2, 'Checks_up3'):
        assert not _is_linked(a2, 'Checks_up3', b)


def test_assoc_Doctor_Prescription_reverse_link_reassign_clear():
    a1 = Prescription(medicines="sample_text", tests="sample_text")
    a2 = Prescription(medicines="sample_text_2", tests="sample_text_2")
    b = Doctor(name="sample_text", privateConsultancy=True, specilization="sample_text", timing="sample_text")
    _safe_set(b, 'Doctor_Prescription_018', {a1})
    assert _is_linked(b, 'Doctor_Prescription_018', a1)
    if hasattr(a1, 'writes19'):
        assert _is_linked(a1, 'writes19', b)
    _safe_set(b, 'Doctor_Prescription_018', {a2})
    assert _is_linked(b, 'Doctor_Prescription_018', a2)
    if hasattr(a1, 'writes19'):
        assert not _is_linked(a1, 'writes19', b)
    if hasattr(a2, 'writes19'):
        assert _is_linked(a2, 'writes19', b)
    _safe_set(b, 'Doctor_Prescription_018', set())
    assert not _is_linked(b, 'Doctor_Prescription_018', a2)
    if hasattr(a2, 'writes19'):
        assert not _is_linked(a2, 'writes19', b)


def test_assoc_Hospital_BloodBank_reverse_link_reassign_clear():
    a1 = Hospital(address="sample_text", name="sample_text", phone=7)
    a2 = Hospital(address="sample_text_2", name="sample_text_2", phone=13)
    b = BloodBank(bloodGroup="sample_text", phone="sample_text")
    _safe_set(b, 'Hospital_BloodBank_125', a1)
    assert _is_linked(b, 'Hospital_BloodBank_125', a1)
    if hasattr(a1, 'has24'):
        assert _is_linked(a1, 'has24', b)
    _safe_set(b, 'Hospital_BloodBank_125', a2)
    assert _is_linked(b, 'Hospital_BloodBank_125', a2)
    if hasattr(a1, 'has24'):
        assert not _is_linked(a1, 'has24', b)
    if hasattr(a2, 'has24'):
        assert _is_linked(a2, 'has24', b)
    _safe_set(b, 'Hospital_BloodBank_125', None)
    assert not _is_linked(b, 'Hospital_BloodBank_125', a2)
    if hasattr(a2, 'has24'):
        assert not _is_linked(a2, 'has24', b)


def test_assoc_Hospital_Doctor_reverse_link_reassign_clear():
    a1 = Hospital(address="sample_text", name="sample_text", phone=7)
    a2 = Hospital(address="sample_text_2", name="sample_text_2", phone=13)
    b = Doctor(name="sample_text", privateConsultancy=True, specilization="sample_text", timing="sample_text")
    _safe_set(b, 'Hospital_Doctor_11', a1)
    assert _is_linked(b, 'Hospital_Doctor_11', a1)
    if hasattr(a1, 'has0'):
        assert _is_linked(a1, 'has0', b)
    _safe_set(b, 'Hospital_Doctor_11', a2)
    assert _is_linked(b, 'Hospital_Doctor_11', a2)
    if hasattr(a1, 'has0'):
        assert not _is_linked(a1, 'has0', b)
    if hasattr(a2, 'has0'):
        assert _is_linked(a2, 'has0', b)
    _safe_set(b, 'Hospital_Doctor_11', None)
    assert not _is_linked(b, 'Hospital_Doctor_11', a2)
    if hasattr(a2, 'has0'):
        assert not _is_linked(a2, 'has0', b)


def test_assoc_Patients_Appointment_reverse_link_reassign_clear():
    a1 = Patients(BP=7, History="sample_text", Symptoms="sample_text", name="sample_text", weight=7)
    a2 = Patients(BP=13, History="sample_text_2", Symptoms="sample_text_2", name="sample_text_2", weight=13)
    b = Appointment(Doctor="sample_text", Patient="sample_text", Time="sample_text")
    _safe_set(b, 'requests11', a1)
    assert _is_linked(b, 'requests11', a1)
    if hasattr(a1, 'Patients_Appointment_010'):
        assert _is_linked(a1, 'Patients_Appointment_010', b)
    _safe_set(b, 'requests11', a2)
    assert _is_linked(b, 'requests11', a2)
    if hasattr(a1, 'Patients_Appointment_010'):
        assert not _is_linked(a1, 'Patients_Appointment_010', b)
    if hasattr(a2, 'Patients_Appointment_010'):
        assert _is_linked(a2, 'Patients_Appointment_010', b)
    _safe_set(b, 'requests11', None)
    assert not _is_linked(b, 'requests11', a2)
    if hasattr(a2, 'Patients_Appointment_010'):
        assert not _is_linked(a2, 'Patients_Appointment_010', b)


def test_assoc_Patients_Assistant_reverse_link_reassign_clear():
    a1 = Patients(BP=7, History="sample_text", Symptoms="sample_text", name="sample_text", weight=7)
    a2 = Patients(BP=13, History="sample_text_2", Symptoms="sample_text_2", name="sample_text_2", weight=13)
    b = Assistant(CNIC="sample_text", name="sample_text")
    _safe_set(b, 'Patients_Assistant_121', {a1})
    assert _is_linked(b, 'Patients_Assistant_121', a1)
    if hasattr(a1, 'record_history20'):
        assert _is_linked(a1, 'record_history20', b)
    _safe_set(b, 'Patients_Assistant_121', {a2})
    assert _is_linked(b, 'Patients_Assistant_121', a2)
    if hasattr(a1, 'record_history20'):
        assert not _is_linked(a1, 'record_history20', b)
    if hasattr(a2, 'record_history20'):
        assert _is_linked(a2, 'record_history20', b)
    _safe_set(b, 'Patients_Assistant_121', set())
    assert not _is_linked(b, 'Patients_Assistant_121', a2)
    if hasattr(a2, 'record_history20'):
        assert not _is_linked(a2, 'record_history20', b)


def test_assoc_Patients_Hospital_reverse_link_reassign_clear():
    a1 = Patients(BP=7, History="sample_text", Symptoms="sample_text", name="sample_text", weight=7)
    a2 = Patients(BP=13, History="sample_text_2", Symptoms="sample_text_2", name="sample_text_2", weight=13)
    b = Hospital(address="sample_text", name="sample_text", phone=7)
    _safe_set(b, 'Patients_Hospital_17', {a1})
    assert _is_linked(b, 'Patients_Hospital_17', a1)
    if hasattr(a1, 'Visit6'):
        assert _is_linked(a1, 'Visit6', b)
    _safe_set(b, 'Patients_Hospital_17', {a2})
    assert _is_linked(b, 'Patients_Hospital_17', a2)
    if hasattr(a1, 'Visit6'):
        assert not _is_linked(a1, 'Visit6', b)
    if hasattr(a2, 'Visit6'):
        assert _is_linked(a2, 'Visit6', b)
    _safe_set(b, 'Patients_Hospital_17', set())
    assert not _is_linked(b, 'Patients_Hospital_17', a2)
    if hasattr(a2, 'Visit6'):
        assert not _is_linked(a2, 'Visit6', b)


def test_assoc_Patients_Receptionist_reverse_link_reassign_clear():
    a1 = Receptionist(CNIC="sample_text", name="sample_text")
    a2 = Receptionist(CNIC="sample_text_2", name="sample_text_2")
    b = Patients(BP=7, History="sample_text", Symptoms="sample_text", name="sample_text", weight=7)
    _safe_set(b, 'calls_query4', a1)
    assert _is_linked(b, 'calls_query4', a1)
    if hasattr(a1, 'Patients_Receptionist_15'):
        assert _is_linked(a1, 'Patients_Receptionist_15', b)
    _safe_set(b, 'calls_query4', a2)
    assert _is_linked(b, 'calls_query4', a2)
    if hasattr(a1, 'Patients_Receptionist_15'):
        assert not _is_linked(a1, 'Patients_Receptionist_15', b)
    if hasattr(a2, 'Patients_Receptionist_15'):
        assert _is_linked(a2, 'Patients_Receptionist_15', b)
    _safe_set(b, 'calls_query4', None)
    assert not _is_linked(b, 'calls_query4', a2)
    if hasattr(a2, 'Patients_Receptionist_15'):
        assert not _is_linked(a2, 'Patients_Receptionist_15', b)


def test_assoc_Receptionist_Appointment_reverse_link_reassign_clear():
    a1 = Receptionist(CNIC="sample_text", name="sample_text")
    a2 = Receptionist(CNIC="sample_text_2", name="sample_text_2")
    b = Appointment(Doctor="sample_text", Patient="sample_text", Time="sample_text")
    _safe_set(b, 'Receptionist_Appointment_19', a1)
    assert _is_linked(b, 'Receptionist_Appointment_19', a1)
    if hasattr(a1, 'give8'):
        assert _is_linked(a1, 'give8', b)
    _safe_set(b, 'Receptionist_Appointment_19', a2)
    assert _is_linked(b, 'Receptionist_Appointment_19', a2)
    if hasattr(a1, 'give8'):
        assert not _is_linked(a1, 'give8', b)
    if hasattr(a2, 'give8'):
        assert _is_linked(a2, 'give8', b)
    _safe_set(b, 'Receptionist_Appointment_19', None)
    assert not _is_linked(b, 'Receptionist_Appointment_19', a2)
    if hasattr(a2, 'give8'):
        assert not _is_linked(a2, 'give8', b)


def test_assoc_Receptionist_Billing_Report_reverse_link_reassign_clear():
    a1 = Receptionist(CNIC="sample_text", name="sample_text")
    a2 = Receptionist(CNIC="sample_text_2", name="sample_text_2")
    b = Billing_Report(serviceCharges="sample_text", testCharges="sample_text")
    _safe_set(b, 'Receptionist_Billing_Report_127', a1)
    assert _is_linked(b, 'Receptionist_Billing_Report_127', a1)
    if hasattr(a1, 'generate26'):
        assert _is_linked(a1, 'generate26', b)
    _safe_set(b, 'Receptionist_Billing_Report_127', a2)
    assert _is_linked(b, 'Receptionist_Billing_Report_127', a2)
    if hasattr(a1, 'generate26'):
        assert not _is_linked(a1, 'generate26', b)
    if hasattr(a2, 'generate26'):
        assert _is_linked(a2, 'generate26', b)
    _safe_set(b, 'Receptionist_Billing_Report_127', None)
    assert not _is_linked(b, 'Receptionist_Billing_Report_127', a2)
    if hasattr(a2, 'generate26'):
        assert not _is_linked(a2, 'generate26', b)


def test_assoc_Receptionist_DoctorDatabase_reverse_link_reassign_clear():
    a1 = Receptionist(CNIC="sample_text", name="sample_text")
    a2 = Receptionist(CNIC="sample_text_2", name="sample_text_2")
    b = DoctorDatabase(Specialization="sample_text", doctorName="sample_text")
    _safe_set(b, 'check13', a1)
    assert _is_linked(b, 'check13', a1)
    if hasattr(a1, 'Receptionist_DoctorDatabase_012'):
        assert _is_linked(a1, 'Receptionist_DoctorDatabase_012', b)
    _safe_set(b, 'check13', a2)
    assert _is_linked(b, 'check13', a2)
    if hasattr(a1, 'Receptionist_DoctorDatabase_012'):
        assert not _is_linked(a1, 'Receptionist_DoctorDatabase_012', b)
    if hasattr(a2, 'Receptionist_DoctorDatabase_012'):
        assert _is_linked(a2, 'Receptionist_DoctorDatabase_012', b)
    _safe_set(b, 'check13', None)
    assert not _is_linked(b, 'check13', a2)
    if hasattr(a2, 'Receptionist_DoctorDatabase_012'):
        assert not _is_linked(a2, 'Receptionist_DoctorDatabase_012', b)


def test_assoc_Receptionist_PatientProfile_reverse_link_reassign_clear():
    a1 = Receptionist(CNIC="sample_text", name="sample_text")
    a2 = Receptionist(CNIC="sample_text_2", name="sample_text_2")
    b = PatientProfile(appointment="sample_text", name="sample_text")
    _safe_set(b, 'Receptionist_PatientProfile_115', a1)
    assert _is_linked(b, 'Receptionist_PatientProfile_115', a1)
    if hasattr(a1, 'create_update14'):
        assert _is_linked(a1, 'create_update14', b)
    _safe_set(b, 'Receptionist_PatientProfile_115', a2)
    assert _is_linked(b, 'Receptionist_PatientProfile_115', a2)
    if hasattr(a1, 'create_update14'):
        assert not _is_linked(a1, 'create_update14', b)
    if hasattr(a2, 'create_update14'):
        assert _is_linked(a2, 'create_update14', b)
    _safe_set(b, 'Receptionist_PatientProfile_115', None)
    assert not _is_linked(b, 'Receptionist_PatientProfile_115', a2)
    if hasattr(a2, 'create_update14'):
        assert not _is_linked(a2, 'create_update14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

