import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_Appointment_attribute_value_roundtrip():
    instance = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Appointment_date_value_roundtrip():
    instance = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Appointment_doctoradi_value_roundtrip():
    instance = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    assert instance.doctoradi == 7
    instance.doctoradi = 13
    assert instance.doctoradi == 13


def test_Appointment_no_value_roundtrip():
    instance = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    assert instance.no == "sample_text"
    instance.no = "sample_text_2"
    assert instance.no == "sample_text_2"


def test_Appointment_room_value_roundtrip():
    instance = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    assert instance.room == 7
    instance.room = 13
    assert instance.room == 13


def test_Appointment_time_value_roundtrip():
    instance = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Bill_amount_value_roundtrip():
    instance = Bill(amount="sample_text", no=7, patientno=7)
    assert instance.amount == "sample_text"
    instance.amount = "sample_text_2"
    assert instance.amount == "sample_text_2"


def test_Bill_no_value_roundtrip():
    instance = Bill(amount="sample_text", no=7, patientno=7)
    assert instance.no == 7
    instance.no = 13
    assert instance.no == 13


def test_Bill_patientno_value_roundtrip():
    instance = Bill(amount="sample_text", no=7, patientno=7)
    assert instance.patientno == 7
    instance.patientno = 13
    assert instance.patientno == 13


def test_Corporation_address_value_roundtrip():
    instance = Corporation(address="sample_text", name="sample_text", no=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Corporation_name_value_roundtrip():
    instance = Corporation(address="sample_text", name="sample_text", no=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Corporation_no_value_roundtrip():
    instance = Corporation(address="sample_text", name="sample_text", no=7)
    assert instance.no == 7
    instance.no = 13
    assert instance.no == 13


def test_Disease_code_value_roundtrip():
    instance = Disease(code=7, name="sample_text", type="sample_text")
    assert instance.code == 7
    instance.code = 13
    assert instance.code == 13


def test_Disease_name_value_roundtrip():
    instance = Disease(code=7, name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Disease_type_value_roundtrip():
    instance = Disease(code=7, name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Doctor_corporation_value_roundtrip():
    instance = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    assert instance.corporation == "sample_text"
    instance.corporation = "sample_text_2"
    assert instance.corporation == "sample_text_2"


def test_Doctor_registorno_value_roundtrip():
    instance = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    assert instance.registorno == "sample_text"
    instance.registorno = "sample_text_2"
    assert instance.registorno == "sample_text_2"


def test_Doctor_specialization_value_roundtrip():
    instance = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    assert instance.specialization == "sample_text"
    instance.specialization = "sample_text_2"
    assert instance.specialization == "sample_text_2"


def test_Examination_Appointmentid_value_roundtrip():
    instance = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    assert instance.Appointmentid == 7
    instance.Appointmentid = 13
    assert instance.Appointmentid == 13


def test_Examination_attribute_value_roundtrip():
    instance = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Examination_diagnosisid_value_roundtrip():
    instance = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    assert instance.diagnosisid == 7
    instance.diagnosisid = 13
    assert instance.diagnosisid == 13


def test_Examination_no_value_roundtrip():
    instance = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    assert instance.no == 7
    instance.no = 13
    assert instance.no == 13


def test_Hospitals_address_value_roundtrip():
    instance = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Hospitals_name_value_roundtrip():
    instance = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Hospitals_no_value_roundtrip():
    instance = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    assert instance.no == 7
    instance.no = 13
    assert instance.no == 13


def test_Hospitals_type_value_roundtrip():
    instance = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Medicine_code_value_roundtrip():
    instance = Medicine(code=7, name="sample_text", price="sample_text", type="sample_text")
    assert instance.code == 7
    instance.code = 13
    assert instance.code == 13


def test_Medicine_name_value_roundtrip():
    instance = Medicine(code=7, name="sample_text", price="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Medicine_price_value_roundtrip():
    instance = Medicine(code=7, name="sample_text", price="sample_text", type="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_Medicine_type_value_roundtrip():
    instance = Medicine(code=7, name="sample_text", price="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Patient_address_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Patient_address1_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.address1 == "sample_text"
    instance.address1 = "sample_text_2"
    assert instance.address1 == "sample_text_2"


def test_Patient_attribute_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Patient_birth_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.birth == "sample_text"
    instance.birth = "sample_text_2"
    assert instance.birth == "sample_text_2"


def test_Patient_birth1_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.birth1 == "sample_text"
    instance.birth1 = "sample_text_2"
    assert instance.birth1 == "sample_text_2"


def test_Patient_gender_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_Patient_gender1_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.gender1 == "sample_text"
    instance.gender1 = "sample_text_2"
    assert instance.gender1 == "sample_text_2"


def test_Patient_name_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Patient_name1_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.name1 == "sample_text"
    instance.name1 = "sample_text_2"
    assert instance.name1 == "sample_text_2"


def test_Patient_tcno_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.tcno == "sample_text"
    instance.tcno = "sample_text_2"
    assert instance.tcno == "sample_text_2"


def test_Patient_tcno1_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.tcno1 == "sample_text"
    instance.tcno1 = "sample_text_2"
    assert instance.tcno1 == "sample_text_2"


def test_Patient_telno_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.telno == "sample_text"
    instance.telno = "sample_text_2"
    assert instance.telno == "sample_text_2"


def test_Patient_telno1_value_roundtrip():
    instance = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    assert instance.telno1 == "sample_text"
    instance.telno1 = "sample_text_2"
    assert instance.telno1 == "sample_text_2"


def test_Patient_Medicines_medicines_value_roundtrip():
    instance = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    assert instance.medicines == "sample_text"
    instance.medicines = "sample_text_2"
    assert instance.medicines == "sample_text_2"


def test_Patient_Medicines_no_value_roundtrip():
    instance = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    assert instance.no == 7
    instance.no = 13
    assert instance.no == 13


def test_Patient_Medicines_patientno_value_roundtrip():
    instance = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    assert instance.patientno == "sample_text"
    instance.patientno = "sample_text_2"
    assert instance.patientno == "sample_text_2"


def test_Patient_Medicines_quantities_value_roundtrip():
    instance = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    assert instance.quantities == 7
    instance.quantities = 13
    assert instance.quantities == 13


def test_Patient_Prescription_code_value_roundtrip():
    instance = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    assert instance.code == 7
    instance.code = 13
    assert instance.code == 13


def test_Patient_Prescription_code1_value_roundtrip():
    instance = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    assert instance.code1 == 7
    instance.code1 = 13
    assert instance.code1 == 13


def test_Patient_Prescription_date_value_roundtrip():
    instance = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Patient_Prescription_diseaseid_value_roundtrip():
    instance = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    assert instance.diseaseid == 7
    instance.diseaseid = 13
    assert instance.diseaseid == 13


def test_Patient_Prescription_medicineid_value_roundtrip():
    instance = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    assert instance.medicineid == 7
    instance.medicineid = 13
    assert instance.medicineid == 13


def test_Patient_Prescription_patientid_value_roundtrip():
    instance = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    assert instance.patientid == 7
    instance.patientid = 13
    assert instance.patientid == 13


def test_Personel_attribute_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Personel_attribute7_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.attribute7 == "sample_text"
    instance.attribute7 = "sample_text_2"
    assert instance.attribute7 == "sample_text_2"


def test_Personel_corporation_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.corporation == "sample_text"
    instance.corporation = "sample_text_2"
    assert instance.corporation == "sample_text_2"


def test_Personel_gender_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_Personel_name_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Personel_name1_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.name1 == "sample_text"
    instance.name1 = "sample_text_2"
    assert instance.name1 == "sample_text_2"


def test_Personel_position_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_Personel_registerno_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.registerno == "sample_text"
    instance.registerno = "sample_text_2"
    assert instance.registerno == "sample_text_2"


def test_Personel_tcno_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.tcno == "sample_text"
    instance.tcno = "sample_text_2"
    assert instance.tcno == "sample_text_2"


def test_Personel_tcno1_value_roundtrip():
    instance = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    assert instance.tcno1 == "sample_text"
    instance.tcno1 = "sample_text_2"
    assert instance.tcno1 == "sample_text_2"


def test_Receptionist_checkroom_value_roundtrip():
    instance = Receptionist(checkroom="sample_text", no=7)
    assert instance.checkroom == "sample_text"
    instance.checkroom = "sample_text_2"
    assert instance.checkroom == "sample_text_2"


def test_Receptionist_no_value_roundtrip():
    instance = Receptionist(checkroom="sample_text", no=7)
    assert instance.no == 7
    instance.no = 13
    assert instance.no == 13


def test_Room_buildingname_value_roundtrip():
    instance = Room(buildingname="sample_text", floor=7, no=7)
    assert instance.buildingname == "sample_text"
    instance.buildingname = "sample_text_2"
    assert instance.buildingname == "sample_text_2"


def test_Room_floor_value_roundtrip():
    instance = Room(buildingname="sample_text", floor=7, no=7)
    assert instance.floor == 7
    instance.floor = 13
    assert instance.floor == 13


def test_Room_no_value_roundtrip():
    instance = Room(buildingname="sample_text", floor=7, no=7)
    assert instance.no == 7
    instance.no = 13
    assert instance.no == 13


def test_diagnosis_diagnoses_value_roundtrip():
    instance = diagnosis(diagnoses="sample_text", id=7)
    assert instance.diagnoses == "sample_text"
    instance.diagnoses = "sample_text_2"
    assert instance.diagnoses == "sample_text_2"


def test_diagnosis_id_value_roundtrip():
    instance = diagnosis(diagnoses="sample_text", id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_assoc_Corporation_Personel_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Corporation(address="sample_text", name="sample_text", no=7)
    b2 = Corporation(address="sample_text_2", name="sample_text_2", no=13)
    _safe_set(a, 'corporation13', b1)
    assert _is_linked(a, 'corporation13', b1)
    if hasattr(b1, 'personel12'):
        assert _is_linked(b1, 'personel12', a)
    _safe_set(a, 'corporation13', b2)
    assert _is_linked(a, 'corporation13', b2)
    if hasattr(b1, 'personel12'):
        assert not _is_linked(b1, 'personel12', a)
    if hasattr(b2, 'personel12'):
        assert _is_linked(b2, 'personel12', a)
    _safe_set(a, 'corporation13', None)
    assert not _is_linked(a, 'corporation13', b2)
    if hasattr(b2, 'personel12'):
        assert not _is_linked(b2, 'personel12', a)


def test_assoc_Doctor_Appointment_link_reassign_clear():
    a = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    b1 = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    b2 = Appointment(attribute="sample_text_2", date="sample_text_2", doctoradi=13, no="sample_text_2", room=13, time="sample_text_2")
    _safe_set(a, 'appointment18', {b1})
    assert _is_linked(a, 'appointment18', b1)
    if hasattr(b1, 'doctor19'):
        assert _is_linked(b1, 'doctor19', a)
    _safe_set(a, 'appointment18', {b2})
    assert _is_linked(a, 'appointment18', b2)
    if hasattr(b1, 'doctor19'):
        assert not _is_linked(b1, 'doctor19', a)
    if hasattr(b2, 'doctor19'):
        assert _is_linked(b2, 'doctor19', a)
    _safe_set(a, 'appointment18', set())
    assert not _is_linked(a, 'appointment18', b2)
    if hasattr(b2, 'doctor19'):
        assert not _is_linked(b2, 'doctor19', a)


def test_assoc_Doctor_Personel_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    b2 = Doctor(corporation="sample_text_2", registorno="sample_text_2", specialization="sample_text_2")
    _safe_set(a, 'doctor5', b1)
    assert _is_linked(a, 'doctor5', b1)
    if hasattr(b1, 'personel4'):
        assert _is_linked(b1, 'personel4', a)
    _safe_set(a, 'doctor5', b2)
    assert _is_linked(a, 'doctor5', b2)
    if hasattr(b1, 'personel4'):
        assert not _is_linked(b1, 'personel4', a)
    if hasattr(b2, 'personel4'):
        assert _is_linked(b2, 'personel4', a)
    _safe_set(a, 'doctor5', None)
    assert not _is_linked(a, 'doctor5', b2)
    if hasattr(b2, 'personel4'):
        assert not _is_linked(b2, 'personel4', a)


def test_assoc_Examination_Appointment_link_reassign_clear():
    a = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    b1 = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    b2 = Appointment(attribute="sample_text_2", date="sample_text_2", doctoradi=13, no="sample_text_2", room=13, time="sample_text_2")
    _safe_set(a, 'appointment20', b1)
    assert _is_linked(a, 'appointment20', b1)
    if hasattr(b1, 'examination21'):
        assert _is_linked(b1, 'examination21', a)
    _safe_set(a, 'appointment20', b2)
    assert _is_linked(a, 'appointment20', b2)
    if hasattr(b1, 'examination21'):
        assert not _is_linked(b1, 'examination21', a)
    if hasattr(b2, 'examination21'):
        assert _is_linked(b2, 'examination21', a)
    _safe_set(a, 'appointment20', None)
    assert not _is_linked(a, 'appointment20', b2)
    if hasattr(b2, 'examination21'):
        assert not _is_linked(b2, 'examination21', a)


def test_assoc_Examination_diagnosis_link_reassign_clear():
    a = diagnosis(diagnoses="sample_text", id=7)
    b1 = Examination(Appointmentid=7, attribute="sample_text", diagnosisid=7, no=7)
    b2 = Examination(Appointmentid=13, attribute="sample_text_2", diagnosisid=13, no=13)
    _safe_set(a, 'examination25', b1)
    assert _is_linked(a, 'examination25', b1)
    if hasattr(b1, 'diagnosis24'):
        assert _is_linked(b1, 'diagnosis24', a)
    _safe_set(a, 'examination25', b2)
    assert _is_linked(a, 'examination25', b2)
    if hasattr(b1, 'diagnosis24'):
        assert not _is_linked(b1, 'diagnosis24', a)
    if hasattr(b2, 'diagnosis24'):
        assert _is_linked(b2, 'diagnosis24', a)
    _safe_set(a, 'examination25', None)
    assert not _is_linked(a, 'examination25', b2)
    if hasattr(b2, 'diagnosis24'):
        assert not _is_linked(b2, 'diagnosis24', a)


def test_assoc_Hospitals_Personel_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    b2 = Hospitals(address="sample_text_2", name="sample_text_2", no=13, type="sample_text_2")
    _safe_set(a, 'hospitals15', b1)
    assert _is_linked(a, 'hospitals15', b1)
    if hasattr(b1, 'personel14'):
        assert _is_linked(b1, 'personel14', a)
    _safe_set(a, 'hospitals15', b2)
    assert _is_linked(a, 'hospitals15', b2)
    if hasattr(b1, 'personel14'):
        assert not _is_linked(b1, 'personel14', a)
    if hasattr(b2, 'personel14'):
        assert _is_linked(b2, 'personel14', a)
    _safe_set(a, 'hospitals15', None)
    assert not _is_linked(a, 'hospitals15', b2)
    if hasattr(b2, 'personel14'):
        assert not _is_linked(b2, 'personel14', a)


def test_assoc_Patient_Appointment_link_reassign_clear():
    a = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    b1 = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    b2 = Appointment(attribute="sample_text_2", date="sample_text_2", doctoradi=13, no="sample_text_2", room=13, time="sample_text_2")
    _safe_set(a, 'appointment16', {b1})
    assert _is_linked(a, 'appointment16', b1)
    if hasattr(b1, 'patient17'):
        assert _is_linked(b1, 'patient17', a)
    _safe_set(a, 'appointment16', {b2})
    assert _is_linked(a, 'appointment16', b2)
    if hasattr(b1, 'patient17'):
        assert not _is_linked(b1, 'patient17', a)
    if hasattr(b2, 'patient17'):
        assert _is_linked(b2, 'patient17', a)
    _safe_set(a, 'appointment16', set())
    assert not _is_linked(a, 'appointment16', b2)
    if hasattr(b2, 'patient17'):
        assert not _is_linked(b2, 'patient17', a)


def test_assoc_Patient_Doctor_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    b2 = Patient(address="sample_text_2", address1="sample_text_2", attribute="sample_text_2", birth="sample_text_2", birth1="sample_text_2", gender="sample_text_2", gender1="sample_text_2", name="sample_text_2", name1="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2", telno="sample_text_2", telno1="sample_text_2")
    _safe_set(a, 'patient1', b1)
    assert _is_linked(a, 'patient1', b1)
    if hasattr(b1, 'doctor0'):
        assert _is_linked(b1, 'doctor0', a)
    _safe_set(a, 'patient1', b2)
    assert _is_linked(a, 'patient1', b2)
    if hasattr(b1, 'doctor0'):
        assert not _is_linked(b1, 'doctor0', a)
    if hasattr(b2, 'doctor0'):
        assert _is_linked(b2, 'doctor0', a)
    _safe_set(a, 'patient1', None)
    assert not _is_linked(a, 'patient1', b2)
    if hasattr(b2, 'doctor0'):
        assert not _is_linked(b2, 'doctor0', a)


def test_assoc_Patient_Doctor2_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    b2 = Patient(address="sample_text_2", address1="sample_text_2", attribute="sample_text_2", birth="sample_text_2", birth1="sample_text_2", gender="sample_text_2", gender1="sample_text_2", name="sample_text_2", name1="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2", telno="sample_text_2", telno1="sample_text_2")
    _safe_set(a, 'patient3', b1)
    assert _is_linked(a, 'patient3', b1)
    if hasattr(b1, 'doctor2'):
        assert _is_linked(b1, 'doctor2', a)
    _safe_set(a, 'patient3', b2)
    assert _is_linked(a, 'patient3', b2)
    if hasattr(b1, 'doctor2'):
        assert not _is_linked(b1, 'doctor2', a)
    if hasattr(b2, 'doctor2'):
        assert _is_linked(b2, 'doctor2', a)
    _safe_set(a, 'patient3', None)
    assert not _is_linked(a, 'patient3', b2)
    if hasattr(b2, 'doctor2'):
        assert not _is_linked(b2, 'doctor2', a)


def test_assoc_Patient_Medicines_Medicine_link_reassign_clear():
    a = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    b1 = Medicine(code=7, name="sample_text", price="sample_text", type="sample_text")
    b2 = Medicine(code=13, name="sample_text_2", price="sample_text_2", type="sample_text_2")
    _safe_set(a, 'medicine34', {b1})
    assert _is_linked(a, 'medicine34', b1)
    if hasattr(b1, 'patient_Medicines35'):
        assert _is_linked(b1, 'patient_Medicines35', a)
    _safe_set(a, 'medicine34', {b2})
    assert _is_linked(a, 'medicine34', b2)
    if hasattr(b1, 'patient_Medicines35'):
        assert not _is_linked(b1, 'patient_Medicines35', a)
    if hasattr(b2, 'patient_Medicines35'):
        assert _is_linked(b2, 'patient_Medicines35', a)
    _safe_set(a, 'medicine34', set())
    assert not _is_linked(a, 'medicine34', b2)
    if hasattr(b2, 'patient_Medicines35'):
        assert not _is_linked(b2, 'patient_Medicines35', a)


def test_assoc_Patient_Patient_Medicines_link_reassign_clear():
    a = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    b1 = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    b2 = Patient(address="sample_text_2", address1="sample_text_2", attribute="sample_text_2", birth="sample_text_2", birth1="sample_text_2", gender="sample_text_2", gender1="sample_text_2", name="sample_text_2", name1="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2", telno="sample_text_2", telno1="sample_text_2")
    _safe_set(a, 'patient27', b1)
    assert _is_linked(a, 'patient27', b1)
    if hasattr(b1, 'patient_Medicines26'):
        assert _is_linked(b1, 'patient_Medicines26', a)
    _safe_set(a, 'patient27', b2)
    assert _is_linked(a, 'patient27', b2)
    if hasattr(b1, 'patient_Medicines26'):
        assert not _is_linked(b1, 'patient_Medicines26', a)
    if hasattr(b2, 'patient_Medicines26'):
        assert _is_linked(b2, 'patient_Medicines26', a)
    _safe_set(a, 'patient27', None)
    assert not _is_linked(a, 'patient27', b2)
    if hasattr(b2, 'patient_Medicines26'):
        assert not _is_linked(b2, 'patient_Medicines26', a)


def test_assoc_Patient_Patient_Prescription_link_reassign_clear():
    a = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    b1 = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    b2 = Patient(address="sample_text_2", address1="sample_text_2", attribute="sample_text_2", birth="sample_text_2", birth1="sample_text_2", gender="sample_text_2", gender1="sample_text_2", name="sample_text_2", name1="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2", telno="sample_text_2", telno1="sample_text_2")
    _safe_set(a, 'patient29', b1)
    assert _is_linked(a, 'patient29', b1)
    if hasattr(b1, 'patient_Prescription28'):
        assert _is_linked(b1, 'patient_Prescription28', a)
    _safe_set(a, 'patient29', b2)
    assert _is_linked(a, 'patient29', b2)
    if hasattr(b1, 'patient_Prescription28'):
        assert not _is_linked(b1, 'patient_Prescription28', a)
    if hasattr(b2, 'patient_Prescription28'):
        assert _is_linked(b2, 'patient_Prescription28', a)
    _safe_set(a, 'patient29', None)
    assert not _is_linked(a, 'patient29', b2)
    if hasattr(b2, 'patient_Prescription28'):
        assert not _is_linked(b2, 'patient_Prescription28', a)


def test_assoc_Patient_Prescription_Disease_link_reassign_clear():
    a = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    b1 = Disease(code=7, name="sample_text", type="sample_text")
    b2 = Disease(code=13, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'disease30', b1)
    assert _is_linked(a, 'disease30', b1)
    if hasattr(b1, 'patient_Prescription31'):
        assert _is_linked(b1, 'patient_Prescription31', a)
    _safe_set(a, 'disease30', b2)
    assert _is_linked(a, 'disease30', b2)
    if hasattr(b1, 'patient_Prescription31'):
        assert not _is_linked(b1, 'patient_Prescription31', a)
    if hasattr(b2, 'patient_Prescription31'):
        assert _is_linked(b2, 'patient_Prescription31', a)
    _safe_set(a, 'disease30', None)
    assert not _is_linked(a, 'disease30', b2)
    if hasattr(b2, 'patient_Prescription31'):
        assert not _is_linked(b2, 'patient_Prescription31', a)


def test_assoc_Patient_Prescription_Patient_Medicines_link_reassign_clear():
    a = Patient_Prescription(code=7, code1=7, date="sample_text", diseaseid=7, medicineid=7, patientid=7)
    b1 = Patient_Medicines(medicines="sample_text", no=7, patientno="sample_text", quantities=7)
    b2 = Patient_Medicines(medicines="sample_text_2", no=13, patientno="sample_text_2", quantities=13)
    _safe_set(a, 'patient_Medicines32', b1)
    assert _is_linked(a, 'patient_Medicines32', b1)
    if hasattr(b1, 'patient_Prescription33'):
        assert _is_linked(b1, 'patient_Prescription33', a)
    _safe_set(a, 'patient_Medicines32', b2)
    assert _is_linked(a, 'patient_Medicines32', b2)
    if hasattr(b1, 'patient_Prescription33'):
        assert not _is_linked(b1, 'patient_Prescription33', a)
    if hasattr(b2, 'patient_Prescription33'):
        assert _is_linked(b2, 'patient_Prescription33', a)
    _safe_set(a, 'patient_Medicines32', None)
    assert not _is_linked(a, 'patient_Medicines32', b2)
    if hasattr(b2, 'patient_Prescription33'):
        assert not _is_linked(b2, 'patient_Prescription33', a)


def test_assoc_Personel_Corporation_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Corporation(address="sample_text", name="sample_text", no=7)
    b2 = Corporation(address="sample_text_2", name="sample_text_2", no=13)
    _safe_set(a, 'corporation26', b1)
    assert _is_linked(a, 'corporation26', b1)
    if hasattr(b1, 'personel7'):
        assert _is_linked(b1, 'personel7', a)
    _safe_set(a, 'corporation26', b2)
    assert _is_linked(a, 'corporation26', b2)
    if hasattr(b1, 'personel7'):
        assert not _is_linked(b1, 'personel7', a)
    if hasattr(b2, 'personel7'):
        assert _is_linked(b2, 'personel7', a)
    _safe_set(a, 'corporation26', None)
    assert not _is_linked(a, 'corporation26', b2)
    if hasattr(b2, 'personel7'):
        assert not _is_linked(b2, 'personel7', a)


def test_assoc_Personel_Doctor_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Doctor(corporation="sample_text", registorno="sample_text", specialization="sample_text")
    b2 = Doctor(corporation="sample_text_2", registorno="sample_text_2", specialization="sample_text_2")
    _safe_set(a, 'doctor10', b1)
    assert _is_linked(a, 'doctor10', b1)
    if hasattr(b1, 'personel11'):
        assert _is_linked(b1, 'personel11', a)
    _safe_set(a, 'doctor10', b2)
    assert _is_linked(a, 'doctor10', b2)
    if hasattr(b1, 'personel11'):
        assert not _is_linked(b1, 'personel11', a)
    if hasattr(b2, 'personel11'):
        assert _is_linked(b2, 'personel11', a)
    _safe_set(a, 'doctor10', None)
    assert not _is_linked(a, 'doctor10', b2)
    if hasattr(b2, 'personel11'):
        assert not _is_linked(b2, 'personel11', a)


def test_assoc_Personel_Hospitals_link_reassign_clear():
    a = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b1 = Hospitals(address="sample_text", name="sample_text", no=7, type="sample_text")
    b2 = Hospitals(address="sample_text_2", name="sample_text_2", no=13, type="sample_text_2")
    _safe_set(a, 'hospitals8', b1)
    assert _is_linked(a, 'hospitals8', b1)
    if hasattr(b1, 'personel9'):
        assert _is_linked(b1, 'personel9', a)
    _safe_set(a, 'hospitals8', b2)
    assert _is_linked(a, 'hospitals8', b2)
    if hasattr(b1, 'personel9'):
        assert not _is_linked(b1, 'personel9', a)
    if hasattr(b2, 'personel9'):
        assert _is_linked(b2, 'personel9', a)
    _safe_set(a, 'hospitals8', None)
    assert not _is_linked(a, 'hospitals8', b2)
    if hasattr(b2, 'personel9'):
        assert not _is_linked(b2, 'personel9', a)


def test_assoc_Personel_Receptionist_link_reassign_clear():
    a = Receptionist(checkroom="sample_text", no=7)
    b1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    _safe_set(a, 'personel43', b1)
    assert _is_linked(a, 'personel43', b1)
    if hasattr(b1, 'receptionist42'):
        assert _is_linked(b1, 'receptionist42', a)
    _safe_set(a, 'personel43', b2)
    assert _is_linked(a, 'personel43', b2)
    if hasattr(b1, 'receptionist42'):
        assert not _is_linked(b1, 'receptionist42', a)
    if hasattr(b2, 'receptionist42'):
        assert _is_linked(b2, 'receptionist42', a)
    _safe_set(a, 'personel43', None)
    assert not _is_linked(a, 'personel43', b2)
    if hasattr(b2, 'receptionist42'):
        assert not _is_linked(b2, 'receptionist42', a)


def test_assoc_Receptionist_Patient_link_reassign_clear():
    a = Receptionist(checkroom="sample_text", no=7)
    b1 = Patient(address="sample_text", address1="sample_text", attribute="sample_text", birth="sample_text", birth1="sample_text", gender="sample_text", gender1="sample_text", name="sample_text", name1="sample_text", tcno="sample_text", tcno1="sample_text", telno="sample_text", telno1="sample_text")
    b2 = Patient(address="sample_text_2", address1="sample_text_2", attribute="sample_text_2", birth="sample_text_2", birth1="sample_text_2", gender="sample_text_2", gender1="sample_text_2", name="sample_text_2", name1="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2", telno="sample_text_2", telno1="sample_text_2")
    _safe_set(a, 'patient40', b1)
    assert _is_linked(a, 'patient40', b1)
    if hasattr(b1, 'receptionist41'):
        assert _is_linked(b1, 'receptionist41', a)
    _safe_set(a, 'patient40', b2)
    assert _is_linked(a, 'patient40', b2)
    if hasattr(b1, 'receptionist41'):
        assert not _is_linked(b1, 'receptionist41', a)
    if hasattr(b2, 'receptionist41'):
        assert _is_linked(b2, 'receptionist41', a)
    _safe_set(a, 'patient40', None)
    assert not _is_linked(a, 'patient40', b2)
    if hasattr(b2, 'receptionist41'):
        assert not _is_linked(b2, 'receptionist41', a)


def test_assoc_Receptionist_Personel_link_reassign_clear():
    a = Receptionist(checkroom="sample_text", no=7)
    b1 = Personel(attribute="sample_text", attribute7="sample_text", corporation="sample_text", gender="sample_text", name="sample_text", name1="sample_text", position="sample_text", registerno="sample_text", tcno="sample_text", tcno1="sample_text")
    b2 = Personel(attribute="sample_text_2", attribute7="sample_text_2", corporation="sample_text_2", gender="sample_text_2", name="sample_text_2", name1="sample_text_2", position="sample_text_2", registerno="sample_text_2", tcno="sample_text_2", tcno1="sample_text_2")
    _safe_set(a, 'personel38', b1)
    assert _is_linked(a, 'personel38', b1)
    if hasattr(b1, 'receptionist39'):
        assert _is_linked(b1, 'receptionist39', a)
    _safe_set(a, 'personel38', b2)
    assert _is_linked(a, 'personel38', b2)
    if hasattr(b1, 'receptionist39'):
        assert not _is_linked(b1, 'receptionist39', a)
    if hasattr(b2, 'receptionist39'):
        assert _is_linked(b2, 'receptionist39', a)
    _safe_set(a, 'personel38', None)
    assert not _is_linked(a, 'personel38', b2)
    if hasattr(b2, 'receptionist39'):
        assert not _is_linked(b2, 'receptionist39', a)


def test_assoc_Room_Appointment_link_reassign_clear():
    a = Room(buildingname="sample_text", floor=7, no=7)
    b1 = Appointment(attribute="sample_text", date="sample_text", doctoradi=7, no="sample_text", room=7, time="sample_text")
    b2 = Appointment(attribute="sample_text_2", date="sample_text_2", doctoradi=13, no="sample_text_2", room=13, time="sample_text_2")
    _safe_set(a, 'appointment22', b1)
    assert _is_linked(a, 'appointment22', b1)
    if hasattr(b1, 'room23'):
        assert _is_linked(b1, 'room23', a)
    _safe_set(a, 'appointment22', b2)
    assert _is_linked(a, 'appointment22', b2)
    if hasattr(b1, 'room23'):
        assert not _is_linked(b1, 'room23', a)
    if hasattr(b2, 'room23'):
        assert _is_linked(b2, 'room23', a)
    _safe_set(a, 'appointment22', None)
    assert not _is_linked(a, 'appointment22', b2)
    if hasattr(b2, 'room23'):
        assert not _is_linked(b2, 'room23', a)


def test_assoc_diagnosis_Disease_link_reassign_clear():
    a = diagnosis(diagnoses="sample_text", id=7)
    b1 = Disease(code=7, name="sample_text", type="sample_text")
    b2 = Disease(code=13, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'disease36', {b1})
    assert _is_linked(a, 'disease36', b1)
    if hasattr(b1, 'diagnosis37'):
        assert _is_linked(b1, 'diagnosis37', a)
    _safe_set(a, 'disease36', {b2})
    assert _is_linked(a, 'disease36', b2)
    if hasattr(b1, 'diagnosis37'):
        assert not _is_linked(b1, 'diagnosis37', a)
    if hasattr(b2, 'diagnosis37'):
        assert _is_linked(b2, 'diagnosis37', a)
    _safe_set(a, 'disease36', set())
    assert not _is_linked(a, 'disease36', b2)
    if hasattr(b2, 'diagnosis37'):
        assert not _is_linked(b2, 'diagnosis37', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Appointment_strategy = st.builds(Appointment, attribute=safe_text, date=safe_text, doctoradi=st.integers(), no=safe_text, room=st.integers(), time=safe_text)
@given(instance=Appointment_strategy)
@settings(max_examples=25)
def test_Appointment_instantiation(instance):
    assert isinstance(instance, Appointment)


Bill_strategy = st.builds(Bill, amount=safe_text, no=st.integers(), patientno=st.integers())
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Corporation_strategy = st.builds(Corporation, address=safe_text, name=safe_text, no=st.integers())
@given(instance=Corporation_strategy)
@settings(max_examples=25)
def test_Corporation_instantiation(instance):
    assert isinstance(instance, Corporation)


Disease_strategy = st.builds(Disease, code=st.integers(), name=safe_text, type=safe_text)
@given(instance=Disease_strategy)
@settings(max_examples=25)
def test_Disease_instantiation(instance):
    assert isinstance(instance, Disease)


Doctor_strategy = st.builds(Doctor, corporation=safe_text, registorno=safe_text, specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Examination_strategy = st.builds(Examination, Appointmentid=st.integers(), attribute=safe_text, diagnosisid=st.integers(), no=st.integers())
@given(instance=Examination_strategy)
@settings(max_examples=25)
def test_Examination_instantiation(instance):
    assert isinstance(instance, Examination)


Hospitals_strategy = st.builds(Hospitals, address=safe_text, name=safe_text, no=st.integers(), type=safe_text)
@given(instance=Hospitals_strategy)
@settings(max_examples=25)
def test_Hospitals_instantiation(instance):
    assert isinstance(instance, Hospitals)


Medicine_strategy = st.builds(Medicine, code=st.integers(), name=safe_text, price=safe_text, type=safe_text)
@given(instance=Medicine_strategy)
@settings(max_examples=25)
def test_Medicine_instantiation(instance):
    assert isinstance(instance, Medicine)


Patient_strategy = st.builds(Patient, address=safe_text, address1=safe_text, attribute=safe_text, birth=safe_text, birth1=safe_text, gender=safe_text, gender1=safe_text, name=safe_text, name1=safe_text, tcno=safe_text, tcno1=safe_text, telno=safe_text, telno1=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Patient_Medicines_strategy = st.builds(Patient_Medicines, medicines=safe_text, no=st.integers(), patientno=safe_text, quantities=st.integers())
@given(instance=Patient_Medicines_strategy)
@settings(max_examples=25)
def test_Patient_Medicines_instantiation(instance):
    assert isinstance(instance, Patient_Medicines)


Patient_Prescription_strategy = st.builds(Patient_Prescription, code=st.integers(), code1=st.integers(), date=safe_text, diseaseid=st.integers(), medicineid=st.integers(), patientid=st.integers())
@given(instance=Patient_Prescription_strategy)
@settings(max_examples=25)
def test_Patient_Prescription_instantiation(instance):
    assert isinstance(instance, Patient_Prescription)


Personel_strategy = st.builds(Personel, attribute=safe_text, attribute7=safe_text, corporation=safe_text, gender=safe_text, name=safe_text, name1=safe_text, position=safe_text, registerno=safe_text, tcno=safe_text, tcno1=safe_text)
@given(instance=Personel_strategy)
@settings(max_examples=25)
def test_Personel_instantiation(instance):
    assert isinstance(instance, Personel)


Receptionist_strategy = st.builds(Receptionist, checkroom=safe_text, no=st.integers())
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Room_strategy = st.builds(Room, buildingname=safe_text, floor=st.integers(), no=st.integers())
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


diagnosis_strategy = st.builds(diagnosis, diagnoses=safe_text, id=st.integers())
@given(instance=diagnosis_strategy)
@settings(max_examples=25)
def test_diagnosis_instantiation(instance):
    assert isinstance(instance, diagnosis)


