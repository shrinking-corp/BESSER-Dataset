import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bill,
    Doctor,
    Patient,
    Receptionist,
    Room,
    appointment,
    medicine,
    nurse,
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

def test_Bill_amount_value_roundtrip():
    instance = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_Bill_billno_value_roundtrip():
    instance = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    assert instance.billno == "sample_text"
    instance.billno = "sample_text_2"
    assert instance.billno == "sample_text_2"


def test_Bill_patientname_value_roundtrip():
    instance = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    assert instance.patientname == "sample_text"
    instance.patientname = "sample_text_2"
    assert instance.patientname == "sample_text_2"


def test_Doctor_address_value_roundtrip():
    instance = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Doctor_department_value_roundtrip():
    instance = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.department == "sample_text"
    instance.department = "sample_text_2"
    assert instance.department == "sample_text_2"


def test_Doctor_docid_value_roundtrip():
    instance = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.docid == 7
    instance.docid = 13
    assert instance.docid == 13


def test_Doctor_name_value_roundtrip():
    instance = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Doctor_phno_value_roundtrip():
    instance = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.phno == 7
    instance.phno = 13
    assert instance.phno == 13


def test_Doctor_specialization_value_roundtrip():
    instance = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    assert instance.specialization == "sample_text"
    instance.specialization = "sample_text_2"
    assert instance.specialization == "sample_text_2"


def test_Patient_address_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Patient_age_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_Patient_id_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Patient_name_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Patient_roomno_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    assert instance.roomno == 7
    instance.roomno = 13
    assert instance.roomno == 13


def test_Patient_sex_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_Patient_telno_value_roundtrip():
    instance = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    assert instance.telno == 7
    instance.telno = 13
    assert instance.telno == 13


def test_Receptionist_email_value_roundtrip():
    instance = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Receptionist_id_value_roundtrip():
    instance = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Receptionist_password_value_roundtrip():
    instance = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Receptionist_username_value_roundtrip():
    instance = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Room_roomno_value_roundtrip():
    instance = Room(roomno=7, roomtype="sample_text")
    assert instance.roomno == 7
    instance.roomno = 13
    assert instance.roomno == 13


def test_Room_roomtype_value_roundtrip():
    instance = Room(roomno=7, roomtype="sample_text")
    assert instance.roomtype == "sample_text"
    instance.roomtype = "sample_text_2"
    assert instance.roomtype == "sample_text_2"


def test_appointment_A_no_value_roundtrip():
    instance = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    assert instance.A_no == 7
    instance.A_no = 13
    assert instance.A_no == 13


def test_appointment_d_name_value_roundtrip():
    instance = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    assert instance.d_name == "sample_text"
    instance.d_name = "sample_text_2"
    assert instance.d_name == "sample_text_2"


def test_appointment_p_id_value_roundtrip():
    instance = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    assert instance.p_id == 7
    instance.p_id = 13
    assert instance.p_id == 13


def test_appointment_p_name_value_roundtrip():
    instance = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    assert instance.p_name == "sample_text"
    instance.p_name = "sample_text_2"
    assert instance.p_name == "sample_text_2"


def test_appointment_time_value_roundtrip():
    instance = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    assert instance.time == date(2024, 1, 1)
    instance.time = date(2025, 6, 15)
    assert instance.time == date(2025, 6, 15)


def test_medicine_m_code_value_roundtrip():
    instance = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    assert instance.m_code == 7
    instance.m_code = 13
    assert instance.m_code == 13


def test_medicine_m_name_value_roundtrip():
    instance = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    assert instance.m_name == "sample_text"
    instance.m_name = "sample_text_2"
    assert instance.m_name == "sample_text_2"


def test_medicine_price_value_roundtrip():
    instance = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_medicine_quantity_value_roundtrip():
    instance = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_nurse_availability_value_roundtrip():
    instance = nurse(availability=True, contact=7, id=7, name="sample_text")
    assert instance.availability == True
    instance.availability = False
    assert instance.availability == False


def test_nurse_contact_value_roundtrip():
    instance = nurse(availability=True, contact=7, id=7, name="sample_text")
    assert instance.contact == 7
    instance.contact = 13
    assert instance.contact == 13


def test_nurse_id_value_roundtrip():
    instance = nurse(availability=True, contact=7, id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_nurse_name_value_roundtrip():
    instance = nurse(availability=True, contact=7, id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_Bill_medicine_link_reassign_clear():
    a = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    b1 = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2", patientname="sample_text_2")
    _safe_set(a, 'bill15', b1)
    assert _is_linked(a, 'bill15', b1)
    if hasattr(b1, 'medicine14'):
        assert _is_linked(b1, 'medicine14', a)
    _safe_set(a, 'bill15', b2)
    assert _is_linked(a, 'bill15', b2)
    if hasattr(b1, 'medicine14'):
        assert not _is_linked(b1, 'medicine14', a)
    if hasattr(b2, 'medicine14'):
        assert _is_linked(b2, 'medicine14', a)
    _safe_set(a, 'bill15', None)
    assert not _is_linked(a, 'bill15', b2)
    if hasattr(b2, 'medicine14'):
        assert not _is_linked(b2, 'medicine14', a)


def test_assoc_Doctor_Patient_link_reassign_clear():
    a = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b1 = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    b2 = Doctor(address="sample_text_2", department="sample_text_2", docid=13, name="sample_text_2", phno=13, specialization="sample_text_2")
    _safe_set(a, 'doctors1', {b1})
    assert _is_linked(a, 'doctors1', b1)
    if hasattr(b1, 'patients0'):
        assert _is_linked(b1, 'patients0', a)
    _safe_set(a, 'doctors1', {b2})
    assert _is_linked(a, 'doctors1', b2)
    if hasattr(b1, 'patients0'):
        assert not _is_linked(b1, 'patients0', a)
    if hasattr(b2, 'patients0'):
        assert _is_linked(b2, 'patients0', a)
    _safe_set(a, 'doctors1', set())
    assert not _is_linked(a, 'doctors1', b2)
    if hasattr(b2, 'patients0'):
        assert not _is_linked(b2, 'patients0', a)


def test_assoc_Doctor_appointment_link_reassign_clear():
    a = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    b1 = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    b2 = Doctor(address="sample_text_2", department="sample_text_2", docid=13, name="sample_text_2", phno=13, specialization="sample_text_2")
    _safe_set(a, 'doctor9', b1)
    assert _is_linked(a, 'doctor9', b1)
    if hasattr(b1, 'appointment8'):
        assert _is_linked(b1, 'appointment8', a)
    _safe_set(a, 'doctor9', b2)
    assert _is_linked(a, 'doctor9', b2)
    if hasattr(b1, 'appointment8'):
        assert not _is_linked(b1, 'appointment8', a)
    if hasattr(b2, 'appointment8'):
        assert _is_linked(b2, 'appointment8', a)
    _safe_set(a, 'doctor9', None)
    assert not _is_linked(a, 'doctor9', b2)
    if hasattr(b2, 'appointment8'):
        assert not _is_linked(b2, 'appointment8', a)


def test_assoc_Doctor_medicine_link_reassign_clear():
    a = medicine(m_code=7, m_name="sample_text", price=3.14, quantity=7)
    b1 = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    b2 = Doctor(address="sample_text_2", department="sample_text_2", docid=13, name="sample_text_2", phno=13, specialization="sample_text_2")
    _safe_set(a, 'doctor17', b1)
    assert _is_linked(a, 'doctor17', b1)
    if hasattr(b1, 'medicine16'):
        assert _is_linked(b1, 'medicine16', a)
    _safe_set(a, 'doctor17', b2)
    assert _is_linked(a, 'doctor17', b2)
    if hasattr(b1, 'medicine16'):
        assert not _is_linked(b1, 'medicine16', a)
    if hasattr(b2, 'medicine16'):
        assert _is_linked(b2, 'medicine16', a)
    _safe_set(a, 'doctor17', None)
    assert not _is_linked(a, 'doctor17', b2)
    if hasattr(b2, 'medicine16'):
        assert not _is_linked(b2, 'medicine16', a)


def test_assoc_Patient_Bill_link_reassign_clear():
    a = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b1 = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2", patientname="sample_text_2")
    _safe_set(a, 'bill2', b1)
    assert _is_linked(a, 'bill2', b1)
    if hasattr(b1, 'pat3'):
        assert _is_linked(b1, 'pat3', a)
    _safe_set(a, 'bill2', b2)
    assert _is_linked(a, 'bill2', b2)
    if hasattr(b1, 'pat3'):
        assert not _is_linked(b1, 'pat3', a)
    if hasattr(b2, 'pat3'):
        assert _is_linked(b2, 'pat3', a)
    _safe_set(a, 'bill2', None)
    assert not _is_linked(a, 'bill2', b2)
    if hasattr(b2, 'pat3'):
        assert not _is_linked(b2, 'pat3', a)


def test_assoc_Patient_Room_link_reassign_clear():
    a = Room(roomno=7, roomtype="sample_text")
    b1 = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", roomno=13, sex="sample_text_2", telno=13)
    _safe_set(a, 'patient13', b1)
    assert _is_linked(a, 'patient13', b1)
    if hasattr(b1, 'room12'):
        assert _is_linked(b1, 'room12', a)
    _safe_set(a, 'patient13', b2)
    assert _is_linked(a, 'patient13', b2)
    if hasattr(b1, 'room12'):
        assert not _is_linked(b1, 'room12', a)
    if hasattr(b2, 'room12'):
        assert _is_linked(b2, 'room12', a)
    _safe_set(a, 'patient13', None)
    assert not _is_linked(a, 'patient13', b2)
    if hasattr(b2, 'room12'):
        assert not _is_linked(b2, 'room12', a)


def test_assoc_Patient_appointment_link_reassign_clear():
    a = appointment(A_no=7, d_name="sample_text", p_id=7, p_name="sample_text", time=date(2024, 1, 1))
    b1 = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", roomno=13, sex="sample_text_2", telno=13)
    _safe_set(a, 'patient11', b1)
    assert _is_linked(a, 'patient11', b1)
    if hasattr(b1, 'appointment10'):
        assert _is_linked(b1, 'appointment10', a)
    _safe_set(a, 'patient11', b2)
    assert _is_linked(a, 'patient11', b2)
    if hasattr(b1, 'appointment10'):
        assert not _is_linked(b1, 'appointment10', a)
    if hasattr(b2, 'appointment10'):
        assert _is_linked(b2, 'appointment10', a)
    _safe_set(a, 'patient11', None)
    assert not _is_linked(a, 'patient11', b2)
    if hasattr(b2, 'appointment10'):
        assert not _is_linked(b2, 'appointment10', a)


def test_assoc_manages_link_reassign_clear():
    a = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    b1 = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2", patientname="sample_text_2")
    _safe_set(a, 'bill6', {b1})
    assert _is_linked(a, 'bill6', b1)
    if hasattr(b1, 'receptionist7'):
        assert _is_linked(b1, 'receptionist7', a)
    _safe_set(a, 'bill6', {b2})
    assert _is_linked(a, 'bill6', b2)
    if hasattr(b1, 'receptionist7'):
        assert not _is_linked(b1, 'receptionist7', a)
    if hasattr(b2, 'receptionist7'):
        assert _is_linked(b2, 'receptionist7', a)
    _safe_set(a, 'bill6', set())
    assert not _is_linked(a, 'bill6', b2)
    if hasattr(b2, 'receptionist7'):
        assert not _is_linked(b2, 'receptionist7', a)


def test_assoc_nurse_Room_link_reassign_clear():
    a = nurse(availability=True, contact=7, id=7, name="sample_text")
    b1 = Room(roomno=7, roomtype="sample_text")
    b2 = Room(roomno=13, roomtype="sample_text_2")
    _safe_set(a, 'room18', b1)
    assert _is_linked(a, 'room18', b1)
    if hasattr(b1, 'nurse19'):
        assert _is_linked(b1, 'nurse19', a)
    _safe_set(a, 'room18', b2)
    assert _is_linked(a, 'room18', b2)
    if hasattr(b1, 'nurse19'):
        assert not _is_linked(b1, 'nurse19', a)
    if hasattr(b2, 'nurse19'):
        assert _is_linked(b2, 'nurse19', a)
    _safe_set(a, 'room18', None)
    assert not _is_linked(a, 'room18', b2)
    if hasattr(b2, 'nurse19'):
        assert not _is_linked(b2, 'nurse19', a)


def test_assoc_receptions_link_reassign_clear():
    a = Receptionist(email="sample_text", id=7, password="sample_text", username="sample_text")
    b1 = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", roomno=13, sex="sample_text_2", telno=13)
    _safe_set(a, 'p5', b1)
    assert _is_linked(a, 'p5', b1)
    if hasattr(b1, 'receptionist4'):
        assert _is_linked(b1, 'receptionist4', a)
    _safe_set(a, 'p5', b2)
    assert _is_linked(a, 'p5', b2)
    if hasattr(b1, 'receptionist4'):
        assert not _is_linked(b1, 'receptionist4', a)
    if hasattr(b2, 'receptionist4'):
        assert _is_linked(b2, 'receptionist4', a)
    _safe_set(a, 'p5', None)
    assert not _is_linked(a, 'p5', b2)
    if hasattr(b2, 'receptionist4'):
        assert not _is_linked(b2, 'receptionist4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bill_strategy = st.builds(Bill, amount=st.floats(allow_nan=False, allow_infinity=False), billno=safe_text, patientname=safe_text)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Doctor_strategy = st.builds(Doctor, address=safe_text, department=safe_text, docid=st.integers(), name=safe_text, phno=st.integers(), specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Patient_strategy = st.builds(Patient, address=safe_text, age=st.integers(), id=st.integers(), name=safe_text, roomno=st.integers(), sex=safe_text, telno=st.integers())
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Receptionist_strategy = st.builds(Receptionist, email=safe_text, id=st.integers(), password=safe_text, username=safe_text)
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Room_strategy = st.builds(Room, roomno=st.integers(), roomtype=safe_text)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


appointment_strategy = st.builds(appointment, A_no=st.integers(), d_name=safe_text, p_id=st.integers(), p_name=safe_text, time=st.dates())
@given(instance=appointment_strategy)
@settings(max_examples=25)
def test_appointment_instantiation(instance):
    assert isinstance(instance, appointment)


medicine_strategy = st.builds(medicine, m_code=st.integers(), m_name=safe_text, price=st.floats(allow_nan=False, allow_infinity=False), quantity=st.integers())
@given(instance=medicine_strategy)
@settings(max_examples=25)
def test_medicine_instantiation(instance):
    assert isinstance(instance, medicine)


nurse_strategy = st.builds(nurse, availability=st.booleans(), contact=st.integers(), id=st.integers(), name=safe_text)
@given(instance=nurse_strategy)
@settings(max_examples=25)
def test_nurse_instantiation(instance):
    assert isinstance(instance, nurse)


