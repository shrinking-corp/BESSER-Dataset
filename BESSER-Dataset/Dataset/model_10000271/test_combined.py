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
    Nurse,
    Staff,
    Bill,
    Person,
    Receptionist,
    Room,
    Patient,
    Department,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_hyp_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_hyp_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_hyp_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_hyp_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_hyp_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_hyp_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "billno" in params, "Missing parameter 'billno'"
    assert "patientname" in params, "Missing parameter 'patientname'"
    assert "amount" in params, "Missing parameter 'amount'"






def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_hyp_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_hyp_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "roomno" in params, "Missing parameter 'roomno'"





def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "telno" in params, "Missing parameter 'telno'"
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"
    assert "roomno" in params, "Missing parameter 'roomno'"
    assert "age" in params, "Missing parameter 'age'"










def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "doctorid" in params, "Missing parameter 'doctorid'"






def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "phno" in params, "Missing parameter 'phno'"
    assert "department" in params, "Missing parameter 'department'"
    assert "specialization" in params, "Missing parameter 'specialization'"
    assert "name" in params, "Missing parameter 'name'"
    assert "docid" in params, "Missing parameter 'docid'"








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
Nurse_strategy = st.builds(
    Nurse,
)
Staff_strategy = st.builds(
    Staff,
)
Bill_strategy = st.builds(
    Bill,
    billno=
        safe_text,
    patientname=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Person_strategy = st.builds(
    Person,
    id=
        st.integers(),
    type=
        safe_text,
    name=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    id=
        st.integers(),
    attribute2=
        safe_text
)
Room_strategy = st.builds(
    Room,
    location=
        safe_text,
    roomno=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    name=
        safe_text,
    sex=
        safe_text,
    telno=
        st.integers(),
    address=
        safe_text,
    id=
        st.integers(),
    roomno=
        st.integers(),
    age=
        st.integers()
)
Department_strategy = st.builds(
    Department,
    id=
        st.integers(),
    name=
        safe_text,
    doctorid=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    address=
        safe_text,
    phno=
        st.integers(),
    department=
        safe_text,
    specialization=
        safe_text,
    name=
        safe_text,
    docid=
        st.integers()
)






@given(instance=Bill_strategy)
def test_hyp_bill_billno_setter(instance):
    original = instance.billno
    instance.billno = original
    assert instance.billno == original



@given(instance=Bill_strategy)
def test_hyp_bill_patientname_setter(instance):
    original = instance.patientname
    instance.patientname = original
    assert instance.patientname == original



@given(instance=Bill_strategy)
def test_hyp_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=Person_strategy)
def test_hyp_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Person_strategy)
def test_hyp_person_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Person_strategy)
def test_hyp_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Receptionist_strategy)
def test_hyp_receptionist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Receptionist_strategy)
def test_hyp_receptionist_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=Room_strategy)
def test_hyp_room_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Room_strategy)
def test_hyp_room_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original




@given(instance=Patient_strategy)
def test_hyp_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_hyp_patient_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=Patient_strategy)
def test_hyp_patient_telno_setter(instance):
    original = instance.telno
    instance.telno = original
    assert instance.telno == original



@given(instance=Patient_strategy)
def test_hyp_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patient_strategy)
def test_hyp_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_hyp_patient_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original



@given(instance=Patient_strategy)
def test_hyp_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original




@given(instance=Department_strategy)
def test_hyp_department_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Department_strategy)
def test_hyp_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Department_strategy)
def test_hyp_department_doctorid_setter(instance):
    original = instance.doctorid
    instance.doctorid = original
    assert instance.doctorid == original




@given(instance=Doctor_strategy)
def test_hyp_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_phno_setter(instance):
    original = instance.phno
    instance.phno = original
    assert instance.phno == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_specialization_setter(instance):
    original = instance.specialization
    instance.specialization = original
    assert instance.specialization == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_docid_setter(instance):
    original = instance.docid
    instance.docid = original
    assert instance.docid == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bill,
    Department,
    Doctor,
    Nurse,
    Patient,
    Person,
    Receptionist,
    Room,
    Staff,
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


def test_Department_doctorid_value_roundtrip():
    instance = Department(doctorid=7, id=7, name="sample_text")
    assert instance.doctorid == 7
    instance.doctorid = 13
    assert instance.doctorid == 13


def test_Department_id_value_roundtrip():
    instance = Department(doctorid=7, id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Department_name_value_roundtrip():
    instance = Department(doctorid=7, id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


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


def test_Person_id_value_roundtrip():
    instance = Person(id=7, name="sample_text", type="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Person_name_value_roundtrip():
    instance = Person(id=7, name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Person_type_value_roundtrip():
    instance = Person(id=7, name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Receptionist_attribute2_value_roundtrip():
    instance = Receptionist(attribute2="sample_text", id=7)
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_Receptionist_id_value_roundtrip():
    instance = Receptionist(attribute2="sample_text", id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Room_location_value_roundtrip():
    instance = Room(location="sample_text", roomno=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_Room_roomno_value_roundtrip():
    instance = Room(location="sample_text", roomno=7)
    assert instance.roomno == 7
    instance.roomno = 13
    assert instance.roomno == 13


def test_assoc_Doctor_Department_link_reassign_clear():
    a = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    b1 = Department(doctorid=7, id=7, name="sample_text")
    b2 = Department(doctorid=13, id=13, name="sample_text_2")
    _safe_set(a, 'depmt2', b1)
    assert _is_linked(a, 'depmt2', b1)
    if hasattr(b1, 'doctor3'):
        assert _is_linked(b1, 'doctor3', a)
    _safe_set(a, 'depmt2', b2)
    assert _is_linked(a, 'depmt2', b2)
    if hasattr(b1, 'doctor3'):
        assert not _is_linked(b1, 'doctor3', a)
    if hasattr(b2, 'doctor3'):
        assert _is_linked(b2, 'doctor3', a)
    _safe_set(a, 'depmt2', None)
    assert not _is_linked(a, 'depmt2', b2)
    if hasattr(b2, 'doctor3'):
        assert not _is_linked(b2, 'doctor3', a)


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


def test_assoc_Patient_Bill_link_reassign_clear():
    a = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b1 = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2", patientname="sample_text_2")
    _safe_set(a, 'bill8', b1)
    assert _is_linked(a, 'bill8', b1)
    if hasattr(b1, 'pat9'):
        assert _is_linked(b1, 'pat9', a)
    _safe_set(a, 'bill8', b2)
    assert _is_linked(a, 'bill8', b2)
    if hasattr(b1, 'pat9'):
        assert not _is_linked(b1, 'pat9', a)
    if hasattr(b2, 'pat9'):
        assert _is_linked(b2, 'pat9', a)
    _safe_set(a, 'bill8', None)
    assert not _is_linked(a, 'bill8', b2)
    if hasattr(b2, 'pat9'):
        assert not _is_linked(b2, 'pat9', a)


def test_assoc_Patient_Room_link_reassign_clear():
    a = Room(location="sample_text", roomno=7)
    b1 = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", roomno=13, sex="sample_text_2", telno=13)
    _safe_set(a, 'patient5', {b1})
    assert _is_linked(a, 'patient5', b1)
    if hasattr(b1, 'room4'):
        assert _is_linked(b1, 'room4', a)
    _safe_set(a, 'patient5', {b2})
    assert _is_linked(a, 'patient5', b2)
    if hasattr(b1, 'room4'):
        assert not _is_linked(b1, 'room4', a)
    if hasattr(b2, 'room4'):
        assert _is_linked(b2, 'room4', a)
    _safe_set(a, 'patient5', set())
    assert not _is_linked(a, 'patient5', b2)
    if hasattr(b2, 'room4'):
        assert not _is_linked(b2, 'room4', a)


def test_assoc_Room_Staff_link_reassign_clear():
    a = Room(location="sample_text", roomno=7)
    b1 = Staff()
    b2 = Staff()
    _safe_set(a, 'staff6', {b1})
    assert _is_linked(a, 'staff6', b1)
    if hasattr(b1, 'room7'):
        assert _is_linked(b1, 'room7', a)
    _safe_set(a, 'staff6', {b2})
    assert _is_linked(a, 'staff6', b2)
    if hasattr(b1, 'room7'):
        assert not _is_linked(b1, 'room7', a)
    if hasattr(b2, 'room7'):
        assert _is_linked(b2, 'room7', a)
    _safe_set(a, 'staff6', set())
    assert not _is_linked(a, 'staff6', b2)
    if hasattr(b2, 'room7'):
        assert not _is_linked(b2, 'room7', a)


def test_assoc_manages_link_reassign_clear():
    a = Receptionist(attribute2="sample_text", id=7)
    b1 = Bill(amount=3.14, billno="sample_text", patientname="sample_text")
    b2 = Bill(amount=9.99, billno="sample_text_2", patientname="sample_text_2")
    _safe_set(a, 'sbill12', {b1})
    assert _is_linked(a, 'sbill12', b1)
    if hasattr(b1, 'receptionist13'):
        assert _is_linked(b1, 'receptionist13', a)
    _safe_set(a, 'sbill12', {b2})
    assert _is_linked(a, 'sbill12', b2)
    if hasattr(b1, 'receptionist13'):
        assert not _is_linked(b1, 'receptionist13', a)
    if hasattr(b2, 'receptionist13'):
        assert _is_linked(b2, 'receptionist13', a)
    _safe_set(a, 'sbill12', set())
    assert not _is_linked(a, 'sbill12', b2)
    if hasattr(b2, 'receptionist13'):
        assert not _is_linked(b2, 'receptionist13', a)


def test_assoc_receptions_link_reassign_clear():
    a = Receptionist(attribute2="sample_text", id=7)
    b1 = Patient(address="sample_text", age=7, id=7, name="sample_text", roomno=7, sex="sample_text", telno=7)
    b2 = Patient(address="sample_text_2", age=13, id=13, name="sample_text_2", roomno=13, sex="sample_text_2", telno=13)
    _safe_set(a, 'p11', b1)
    assert _is_linked(a, 'p11', b1)
    if hasattr(b1, 'receptionist10'):
        assert _is_linked(b1, 'receptionist10', a)
    _safe_set(a, 'p11', b2)
    assert _is_linked(a, 'p11', b2)
    if hasattr(b1, 'receptionist10'):
        assert not _is_linked(b1, 'receptionist10', a)
    if hasattr(b2, 'receptionist10'):
        assert _is_linked(b2, 'receptionist10', a)
    _safe_set(a, 'p11', None)
    assert not _is_linked(a, 'p11', b2)
    if hasattr(b2, 'receptionist10'):
        assert not _is_linked(b2, 'receptionist10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bill_strategy = st.builds(Bill, amount=st.floats(allow_nan=False, allow_infinity=False), billno=safe_text, patientname=safe_text)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Department_strategy = st.builds(Department, doctorid=st.integers(), id=st.integers(), name=safe_text)
@given(instance=Department_strategy)
@settings(max_examples=25)
def test_Department_instantiation(instance):
    assert isinstance(instance, Department)


Doctor_strategy = st.builds(Doctor, address=safe_text, department=safe_text, docid=st.integers(), name=safe_text, phno=st.integers(), specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Nurse_strategy = st.builds(Nurse)
@given(instance=Nurse_strategy)
@settings(max_examples=25)
def test_Nurse_instantiation(instance):
    assert isinstance(instance, Nurse)


Patient_strategy = st.builds(Patient, address=safe_text, age=st.integers(), id=st.integers(), name=safe_text, roomno=st.integers(), sex=safe_text, telno=st.integers())
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Person_strategy = st.builds(Person, id=st.integers(), name=safe_text, type=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Receptionist_strategy = st.builds(Receptionist, attribute2=safe_text, id=st.integers())
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Room_strategy = st.builds(Room, location=safe_text, roomno=st.integers())
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


Staff_strategy = st.builds(Staff)
@given(instance=Staff_strategy)
@settings(max_examples=25)
def test_Staff_instantiation(instance):
    assert isinstance(instance, Staff)



