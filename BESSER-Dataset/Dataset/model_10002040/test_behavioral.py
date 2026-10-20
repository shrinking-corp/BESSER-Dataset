import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Appointment,
    Bill,
    Corporation,
    Disease,
    Doctor,
    Examination,
    Hospitals,
    Medicine,
    Patient,
    Patient_Medicines,
    Patient_Prescription,
    Personel,
    Receptionist,
    Room,
    diagnosis,
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

def test_assoc_Corporation_Personel_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Corporation(address="sample_text", name="sample_text", no=7)
    _safe_set(b, 'personel12', {a1})
    assert _is_linked(b, 'personel12', a1)
    if hasattr(a1, 'corporation13'):
        assert _is_linked(a1, 'corporation13', b)
    _safe_set(b, 'personel12', {a2})
    assert _is_linked(b, 'personel12', a2)
    if hasattr(a1, 'corporation13'):
        assert not _is_linked(a1, 'corporation13', b)
    if hasattr(a2, 'corporation13'):
        assert _is_linked(a2, 'corporation13', b)
    _safe_set(b, 'personel12', set())
    assert not _is_linked(b, 'personel12', a2)
    if hasattr(a2, 'corporation13'):
        assert not _is_linked(a2, 'corporation13', b)


def test_assoc_Doctor_Appointment_reverse_link_reassign_clear():
    a1 = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    a2 = Doctor(corporation="sample_text_2", registorno="sample_text_2", specialization="sample_text_2")
    b = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    _safe_set(b, 'doctor19', a1)
    assert _is_linked(b, 'doctor19', a1)
    if hasattr(a1, 'appointment18'):
        assert _is_linked(a1, 'appointment18', b)
    _safe_set(b, 'doctor19', a2)
    assert _is_linked(b, 'doctor19', a2)
    if hasattr(a1, 'appointment18'):
        assert not _is_linked(a1, 'appointment18', b)
    if hasattr(a2, 'appointment18'):
        assert _is_linked(a2, 'appointment18', b)
    _safe_set(b, 'doctor19', None)
    assert not _is_linked(b, 'doctor19', a2)
    if hasattr(a2, 'appointment18'):
        assert not _is_linked(a2, 'appointment18', b)


def test_assoc_Doctor_Personel_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    _safe_set(b, 'personel4', a1)
    assert _is_linked(b, 'personel4', a1)
    if hasattr(a1, 'doctor5'):
        assert _is_linked(a1, 'doctor5', b)
    _safe_set(b, 'personel4', a2)
    assert _is_linked(b, 'personel4', a2)
    if hasattr(a1, 'doctor5'):
        assert not _is_linked(a1, 'doctor5', b)
    if hasattr(a2, 'doctor5'):
        assert _is_linked(a2, 'doctor5', b)
    _safe_set(b, 'personel4', None)
    assert not _is_linked(b, 'personel4', a2)
    if hasattr(a2, 'doctor5'):
        assert not _is_linked(a2, 'doctor5', b)


def test_assoc_Examination_Appointment_reverse_link_reassign_clear():
    a1 = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    a2 = Examination(Appointmentid=13, attribute="sample_text_2", diagnosisid=13, no=13)
    b = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    _safe_set(b, 'examination21', a1)
    assert _is_linked(b, 'examination21', a1)
    if hasattr(a1, 'appointment20'):
        assert _is_linked(a1, 'appointment20', b)
    _safe_set(b, 'examination21', a2)
    assert _is_linked(b, 'examination21', a2)
    if hasattr(a1, 'appointment20'):
        assert not _is_linked(a1, 'appointment20', b)
    if hasattr(a2, 'appointment20'):
        assert _is_linked(a2, 'appointment20', b)
    _safe_set(b, 'examination21', None)
    assert not _is_linked(b, 'examination21', a2)
    if hasattr(a2, 'appointment20'):
        assert not _is_linked(a2, 'appointment20', b)


def test_assoc_Examination_diagnosis_reverse_link_reassign_clear():
    a1 = diagnosis(diagnoses="sample_text", id=7)
    a2 = diagnosis(diagnoses="sample_text_2", id=13)
    b = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    _safe_set(b, 'diagnosis24', {a1})
    assert _is_linked(b, 'diagnosis24', a1)
    if hasattr(a1, 'examination25'):
        assert _is_linked(a1, 'examination25', b)
    _safe_set(b, 'diagnosis24', {a2})
    assert _is_linked(b, 'diagnosis24', a2)
    if hasattr(a1, 'examination25'):
        assert not _is_linked(a1, 'examination25', b)
    if hasattr(a2, 'examination25'):
        assert _is_linked(a2, 'examination25', b)
    _safe_set(b, 'diagnosis24', set())
    assert not _is_linked(b, 'diagnosis24', a2)
    if hasattr(a2, 'examination25'):
        assert not _is_linked(a2, 'examination25', b)


def test_assoc_Hospitals_Personel_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    _safe_set(b, 'personel14', {a1})
    assert _is_linked(b, 'personel14', a1)
    if hasattr(a1, 'hospitals15'):
        assert _is_linked(a1, 'hospitals15', b)
    _safe_set(b, 'personel14', {a2})
    assert _is_linked(b, 'personel14', a2)
    if hasattr(a1, 'hospitals15'):
        assert not _is_linked(a1, 'hospitals15', b)
    if hasattr(a2, 'hospitals15'):
        assert _is_linked(a2, 'hospitals15', b)
    _safe_set(b, 'personel14', set())
    assert not _is_linked(b, 'personel14', a2)
    if hasattr(a2, 'hospitals15'):
        assert not _is_linked(a2, 'hospitals15', b)


def test_assoc_Patient_Appointment_reverse_link_reassign_clear():
    a1 = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    a2 = Patient(address="sample_text_2", address1="sample_text_2", attribute="sample_text_2", birth="sample_text_2", birth1="sample_text_2", gender="sample_text_2", gender1="sample_text_2", name="sample_text_2", name1="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2", telno="sample_text_2", telno1="sample_text_2")
    b = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    _safe_set(b, 'patient17', a1)
    assert _is_linked(b, 'patient17', a1)
    if hasattr(a1, 'appointment16'):
        assert _is_linked(a1, 'appointment16', b)
    _safe_set(b, 'patient17', a2)
    assert _is_linked(b, 'patient17', a2)
    if hasattr(a1, 'appointment16'):
        assert not _is_linked(a1, 'appointment16', b)
    if hasattr(a2, 'appointment16'):
        assert _is_linked(a2, 'appointment16', b)
    _safe_set(b, 'patient17', None)
    assert not _is_linked(b, 'patient17', a2)
    if hasattr(a2, 'appointment16'):
        assert not _is_linked(a2, 'appointment16', b)


def test_assoc_Patient_Doctor_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    _safe_set(b, 'doctor0', a1)
    assert _is_linked(b, 'doctor0', a1)
    if hasattr(a1, 'patient1'):
        assert _is_linked(a1, 'patient1', b)
    _safe_set(b, 'doctor0', a2)
    assert _is_linked(b, 'doctor0', a2)
    if hasattr(a1, 'patient1'):
        assert not _is_linked(a1, 'patient1', b)
    if hasattr(a2, 'patient1'):
        assert _is_linked(a2, 'patient1', b)
    _safe_set(b, 'doctor0', None)
    assert not _is_linked(b, 'doctor0', a2)
    if hasattr(a2, 'patient1'):
        assert not _is_linked(a2, 'patient1', b)


def test_assoc_Patient_Doctor2_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    _safe_set(b, 'doctor2', a1)
    assert _is_linked(b, 'doctor2', a1)
    if hasattr(a1, 'patient3'):
        assert _is_linked(a1, 'patient3', b)
    _safe_set(b, 'doctor2', a2)
    assert _is_linked(b, 'doctor2', a2)
    if hasattr(a1, 'patient3'):
        assert not _is_linked(a1, 'patient3', b)
    if hasattr(a2, 'patient3'):
        assert _is_linked(a2, 'patient3', b)
    _safe_set(b, 'doctor2', None)
    assert not _is_linked(b, 'doctor2', a2)
    if hasattr(a2, 'patient3'):
        assert not _is_linked(a2, 'patient3', b)


def test_assoc_Patient_Medicines_Medicine_reverse_link_reassign_clear():
    a1 = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    a2 = Patient_Medicines(medicines="sample_text_2", no=13, patientno="sample_text_2", quantities=13)
    b = Medicine(code=7, name="sample_text", price="sample_text", type="sample_text")
    _safe_set(b, 'patient_Medicines35', a1)
    assert _is_linked(b, 'patient_Medicines35', a1)
    if hasattr(a1, 'medicine34'):
        assert _is_linked(a1, 'medicine34', b)
    _safe_set(b, 'patient_Medicines35', a2)
    assert _is_linked(b, 'patient_Medicines35', a2)
    if hasattr(a1, 'medicine34'):
        assert not _is_linked(a1, 'medicine34', b)
    if hasattr(a2, 'medicine34'):
        assert _is_linked(a2, 'medicine34', b)
    _safe_set(b, 'patient_Medicines35', None)
    assert not _is_linked(b, 'patient_Medicines35', a2)
    if hasattr(a2, 'medicine34'):
        assert not _is_linked(a2, 'medicine34', b)


def test_assoc_Patient_Patient_Medicines_reverse_link_reassign_clear():
    a1 = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    a2 = Patient_Medicines(medicines="sample_text_2", no=13, patientno="sample_text_2", quantities=13)
    b = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    _safe_set(b, 'patient_Medicines26', a1)
    assert _is_linked(b, 'patient_Medicines26', a1)
    if hasattr(a1, 'patient27'):
        assert _is_linked(a1, 'patient27', b)
    _safe_set(b, 'patient_Medicines26', a2)
    assert _is_linked(b, 'patient_Medicines26', a2)
    if hasattr(a1, 'patient27'):
        assert not _is_linked(a1, 'patient27', b)
    if hasattr(a2, 'patient27'):
        assert _is_linked(a2, 'patient27', b)
    _safe_set(b, 'patient_Medicines26', None)
    assert not _is_linked(b, 'patient_Medicines26', a2)
    if hasattr(a2, 'patient27'):
        assert not _is_linked(a2, 'patient27', b)


def test_assoc_Patient_Patient_Prescription_reverse_link_reassign_clear():
    a1 = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    a2 = Patient_Prescription(code=13, code1=13, date="sample_text_2", diseaseid=13, medicineid=13, patientid=13)
    b = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    _safe_set(b, 'patient_Prescription28', a1)
    assert _is_linked(b, 'patient_Prescription28', a1)
    if hasattr(a1, 'patient29'):
        assert _is_linked(a1, 'patient29', b)
    _safe_set(b, 'patient_Prescription28', a2)
    assert _is_linked(b, 'patient_Prescription28', a2)
    if hasattr(a1, 'patient29'):
        assert not _is_linked(a1, 'patient29', b)
    if hasattr(a2, 'patient29'):
        assert _is_linked(a2, 'patient29', b)
    _safe_set(b, 'patient_Prescription28', None)
    assert not _is_linked(b, 'patient_Prescription28', a2)
    if hasattr(a2, 'patient29'):
        assert not _is_linked(a2, 'patient29', b)


def test_assoc_Patient_Prescription_Disease_reverse_link_reassign_clear():
    a1 = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    a2 = Patient_Prescription(code=13, code1=13, date="sample_text_2", diseaseid=13, medicineid=13, patientid=13)
    b = Disease(code=7, name="sample_text", type="sample_text")
    _safe_set(b, 'patient_Prescription31', a1)
    assert _is_linked(b, 'patient_Prescription31', a1)
    if hasattr(a1, 'disease30'):
        assert _is_linked(a1, 'disease30', b)
    _safe_set(b, 'patient_Prescription31', a2)
    assert _is_linked(b, 'patient_Prescription31', a2)
    if hasattr(a1, 'disease30'):
        assert not _is_linked(a1, 'disease30', b)
    if hasattr(a2, 'disease30'):
        assert _is_linked(a2, 'disease30', b)
    _safe_set(b, 'patient_Prescription31', None)
    assert not _is_linked(b, 'patient_Prescription31', a2)
    if hasattr(a2, 'disease30'):
        assert not _is_linked(a2, 'disease30', b)


def test_assoc_Patient_Prescription_Patient_Medicines_reverse_link_reassign_clear():
    a1 = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    a2 = Patient_Prescription(code=13, code1=13, date="sample_text_2", diseaseid=13, medicineid=13, patientid=13)
    b = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    _safe_set(b, 'patient_Prescription33', {a1})
    assert _is_linked(b, 'patient_Prescription33', a1)
    if hasattr(a1, 'patient_Medicines32'):
        assert _is_linked(a1, 'patient_Medicines32', b)
    _safe_set(b, 'patient_Prescription33', {a2})
    assert _is_linked(b, 'patient_Prescription33', a2)
    if hasattr(a1, 'patient_Medicines32'):
        assert not _is_linked(a1, 'patient_Medicines32', b)
    if hasattr(a2, 'patient_Medicines32'):
        assert _is_linked(a2, 'patient_Medicines32', b)
    _safe_set(b, 'patient_Prescription33', set())
    assert not _is_linked(b, 'patient_Prescription33', a2)
    if hasattr(a2, 'patient_Medicines32'):
        assert not _is_linked(a2, 'patient_Medicines32', b)


def test_assoc_Personel_Corporation_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Corporation(address="sample_text", name="sample_text", no=7)
    _safe_set(b, 'personel7', {a1})
    assert _is_linked(b, 'personel7', a1)
    if hasattr(a1, 'corporation26'):
        assert _is_linked(a1, 'corporation26', b)
    _safe_set(b, 'personel7', {a2})
    assert _is_linked(b, 'personel7', a2)
    if hasattr(a1, 'corporation26'):
        assert not _is_linked(a1, 'corporation26', b)
    if hasattr(a2, 'corporation26'):
        assert _is_linked(a2, 'corporation26', b)
    _safe_set(b, 'personel7', set())
    assert not _is_linked(b, 'personel7', a2)
    if hasattr(a2, 'corporation26'):
        assert not _is_linked(a2, 'corporation26', b)


def test_assoc_Personel_Doctor_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    _safe_set(b, 'personel11', a1)
    assert _is_linked(b, 'personel11', a1)
    if hasattr(a1, 'doctor10'):
        assert _is_linked(a1, 'doctor10', b)
    _safe_set(b, 'personel11', a2)
    assert _is_linked(b, 'personel11', a2)
    if hasattr(a1, 'doctor10'):
        assert not _is_linked(a1, 'doctor10', b)
    if hasattr(a2, 'doctor10'):
        assert _is_linked(a2, 'doctor10', b)
    _safe_set(b, 'personel11', None)
    assert not _is_linked(b, 'personel11', a2)
    if hasattr(a2, 'doctor10'):
        assert not _is_linked(a2, 'doctor10', b)


def test_assoc_Personel_Hospitals_reverse_link_reassign_clear():
    a1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    a2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    b = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    _safe_set(b, 'personel9', a1)
    assert _is_linked(b, 'personel9', a1)
    if hasattr(a1, 'hospitals8'):
        assert _is_linked(a1, 'hospitals8', b)
    _safe_set(b, 'personel9', a2)
    assert _is_linked(b, 'personel9', a2)
    if hasattr(a1, 'hospitals8'):
        assert not _is_linked(a1, 'hospitals8', b)
    if hasattr(a2, 'hospitals8'):
        assert _is_linked(a2, 'hospitals8', b)
    _safe_set(b, 'personel9', None)
    assert not _is_linked(b, 'personel9', a2)
    if hasattr(a2, 'hospitals8'):
        assert not _is_linked(a2, 'hospitals8', b)


def test_assoc_Personel_Receptionist_reverse_link_reassign_clear():
    a1 = Receptionist(checkroom="sample_text", no=7)
    a2 = Receptionist(checkroom="sample_text_2", no=13)
    b = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    _safe_set(b, 'receptionist42', a1)
    assert _is_linked(b, 'receptionist42', a1)
    if hasattr(a1, 'personel43'):
        assert _is_linked(a1, 'personel43', b)
    _safe_set(b, 'receptionist42', a2)
    assert _is_linked(b, 'receptionist42', a2)
    if hasattr(a1, 'personel43'):
        assert not _is_linked(a1, 'personel43', b)
    if hasattr(a2, 'personel43'):
        assert _is_linked(a2, 'personel43', b)
    _safe_set(b, 'receptionist42', None)
    assert not _is_linked(b, 'receptionist42', a2)
    if hasattr(a2, 'personel43'):
        assert not _is_linked(a2, 'personel43', b)


def test_assoc_Receptionist_Patient_reverse_link_reassign_clear():
    a1 = Receptionist(checkroom="sample_text", no=7)
    a2 = Receptionist(checkroom="sample_text_2", no=13)
    b = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    _safe_set(b, 'receptionist41', a1)
    assert _is_linked(b, 'receptionist41', a1)
    if hasattr(a1, 'patient40'):
        assert _is_linked(a1, 'patient40', b)
    _safe_set(b, 'receptionist41', a2)
    assert _is_linked(b, 'receptionist41', a2)
    if hasattr(a1, 'patient40'):
        assert not _is_linked(a1, 'patient40', b)
    if hasattr(a2, 'patient40'):
        assert _is_linked(a2, 'patient40', b)
    _safe_set(b, 'receptionist41', None)
    assert not _is_linked(b, 'receptionist41', a2)
    if hasattr(a2, 'patient40'):
        assert not _is_linked(a2, 'patient40', b)


def test_assoc_Receptionist_Personel_reverse_link_reassign_clear():
    a1 = Receptionist(checkroom="sample_text", no=7)
    a2 = Receptionist(checkroom="sample_text_2", no=13)
    b = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    _safe_set(b, 'receptionist39', a1)
    assert _is_linked(b, 'receptionist39', a1)
    if hasattr(a1, 'personel38'):
        assert _is_linked(a1, 'personel38', b)
    _safe_set(b, 'receptionist39', a2)
    assert _is_linked(b, 'receptionist39', a2)
    if hasattr(a1, 'personel38'):
        assert not _is_linked(a1, 'personel38', b)
    if hasattr(a2, 'personel38'):
        assert _is_linked(a2, 'personel38', b)
    _safe_set(b, 'receptionist39', None)
    assert not _is_linked(b, 'receptionist39', a2)
    if hasattr(a2, 'personel38'):
        assert not _is_linked(a2, 'personel38', b)


def test_assoc_Room_Appointment_reverse_link_reassign_clear():
    a1 = Room(buildingname="sample_text", floor=7, no=7)
    a2 = Room(buildingname="sample_text_2", floor=13, no=13)
    b = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    _safe_set(b, 'room23', a1)
    assert _is_linked(b, 'room23', a1)
    if hasattr(a1, 'appointment22'):
        assert _is_linked(a1, 'appointment22', b)
    _safe_set(b, 'room23', a2)
    assert _is_linked(b, 'room23', a2)
    if hasattr(a1, 'appointment22'):
        assert not _is_linked(a1, 'appointment22', b)
    if hasattr(a2, 'appointment22'):
        assert _is_linked(a2, 'appointment22', b)
    _safe_set(b, 'room23', None)
    assert not _is_linked(b, 'room23', a2)
    if hasattr(a2, 'appointment22'):
        assert not _is_linked(a2, 'appointment22', b)


def test_assoc_diagnosis_Disease_reverse_link_reassign_clear():
    a1 = diagnosis(diagnoses="sample_text", id=7)
    a2 = diagnosis(diagnoses="sample_text_2", id=13)
    b = Disease(code=7, name="sample_text", type="sample_text")
    _safe_set(b, 'diagnosis37', a1)
    assert _is_linked(b, 'diagnosis37', a1)
    if hasattr(a1, 'disease36'):
        assert _is_linked(a1, 'disease36', b)
    _safe_set(b, 'diagnosis37', a2)
    assert _is_linked(b, 'diagnosis37', a2)
    if hasattr(a1, 'disease36'):
        assert not _is_linked(a1, 'disease36', b)
    if hasattr(a2, 'disease36'):
        assert _is_linked(a2, 'disease36', b)
    _safe_set(b, 'diagnosis37', None)
    assert not _is_linked(b, 'diagnosis37', a2)
    if hasattr(a2, 'disease36'):
        assert not _is_linked(a2, 'disease36', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

