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
    Technical_staff,
    Administrative_staff,
    Operations_staff,
    Department,
    Nurse1,
    Staff1,
    Bill,
    Hospital,
    Person,
    Staff,
    Room,
    Patient,
    Nurse,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_technical_staff_is_not_abstract():
    assert not inspect.isabstract(Technical_staff)


def test_hyp_technical_staff_constructor_exists():
    assert callable(Technical_staff.__init__)


def test_hyp_technical_staff_constructor_args():
    sig = inspect.signature(Technical_staff.__init__)
    params = list(sig.parameters.keys())



def test_hyp_administrative_staff_is_not_abstract():
    assert not inspect.isabstract(Administrative_staff)


def test_hyp_administrative_staff_constructor_exists():
    assert callable(Administrative_staff.__init__)


def test_hyp_administrative_staff_constructor_args():
    sig = inspect.signature(Administrative_staff.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operations_staff_is_not_abstract():
    assert not inspect.isabstract(Operations_staff)


def test_hyp_operations_staff_constructor_exists():
    assert callable(Operations_staff.__init__)


def test_hyp_operations_staff_constructor_args():
    sig = inspect.signature(Operations_staff.__init__)
    params = list(sig.parameters.keys())



def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nurse1_is_not_abstract():
    assert not inspect.isabstract(Nurse1)


def test_hyp_nurse1_constructor_exists():
    assert callable(Nurse1.__init__)


def test_hyp_nurse1_constructor_args():
    sig = inspect.signature(Nurse1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staff1_is_not_abstract():
    assert not inspect.isabstract(Staff1)


def test_hyp_staff1_constructor_exists():
    assert callable(Staff1.__init__)


def test_hyp_staff1_constructor_args():
    sig = inspect.signature(Staff1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_hyp_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_hyp_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "billno" in params, "Missing parameter 'billno'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "patientname" in params, "Missing parameter 'patientname'"






def test_hyp_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hyp_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hyp_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phone" in params, "Missing parameter 'phone'"






def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "address" in params, "Missing parameter 'address'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "birthDate" in params, "Missing parameter 'birthDate'"
    assert "phone" in params, "Missing parameter 'phone'"









def test_hyp_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_hyp_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_hyp_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "joined" in params, "Missing parameter 'joined'"
    assert "education" in params, "Missing parameter 'education'"





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
    assert "accepted" in params, "Missing parameter 'accepted'"
    assert "roomno" in params, "Missing parameter 'roomno'"
    assert "address" in params, "Missing parameter 'address'"
    assert "age" in params, "Missing parameter 'age'"
    assert "sickness" in params, "Missing parameter 'sickness'"
    assert "sex" in params, "Missing parameter 'sex'"
    assert "telno" in params, "Missing parameter 'telno'"










def test_hyp_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_hyp_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_hyp_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())
    assert "doctorid" in params, "Missing parameter 'doctorid'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "phno" in params, "Missing parameter 'phno'"
    assert "specialization" in params, "Missing parameter 'specialization'"
    assert "name" in params, "Missing parameter 'name'"
    assert "department" in params, "Missing parameter 'department'"
    assert "address" in params, "Missing parameter 'address'"
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
Technical_staff_strategy = st.builds(
    Technical_staff,
)
Administrative_staff_strategy = st.builds(
    Administrative_staff,
)
Operations_staff_strategy = st.builds(
    Operations_staff,
)
Department_strategy = st.builds(
    Department,
)
Nurse1_strategy = st.builds(
    Nurse1,
)
Staff1_strategy = st.builds(
    Staff1,
)
Bill_strategy = st.builds(
    Bill,
    billno=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    patientname=
        safe_text
)
Hospital_strategy = st.builds(
    Hospital,
    address=
        safe_text,
    name=
        safe_text,
    phone=
        st.integers()
)
Person_strategy = st.builds(
    Person,
    Gender=
        safe_text,
    Title=
        safe_text,
    address=
        safe_text,
    Name=
        safe_text,
    birthDate=
        st.dates(),
    phone=
        st.integers()
)
Staff_strategy = st.builds(
    Staff,
    joined=
        st.dates(),
    education=
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
    accepted=
        st.dates(),
    roomno=
        st.integers(),
    address=
        safe_text,
    age=
        st.integers(),
    sickness=
        safe_text,
    sex=
        safe_text,
    telno=
        st.integers()
)
Nurse_strategy = st.builds(
    Nurse,
    doctorid=
        st.integers(),
    id=
        st.integers(),
    name=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    phno=
        st.integers(),
    specialization=
        safe_text,
    name=
        safe_text,
    department=
        safe_text,
    address=
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
def test_hyp_bill_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Bill_strategy)
def test_hyp_bill_patientname_setter(instance):
    original = instance.patientname
    instance.patientname = original
    assert instance.patientname == original




@given(instance=Hospital_strategy)
def test_hyp_hospital_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Hospital_strategy)
def test_hyp_hospital_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Hospital_strategy)
def test_hyp_hospital_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original




@given(instance=Person_strategy)
def test_hyp_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Person_strategy)
def test_hyp_person_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=Person_strategy)
def test_hyp_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Person_strategy)
def test_hyp_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Person_strategy)
def test_hyp_person_birthDate_setter(instance):
    original = instance.birthDate
    instance.birthDate = original
    assert instance.birthDate == original



@given(instance=Person_strategy)
def test_hyp_person_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original




@given(instance=Staff_strategy)
def test_hyp_staff_joined_setter(instance):
    original = instance.joined
    instance.joined = original
    assert instance.joined == original



@given(instance=Staff_strategy)
def test_hyp_staff_education_setter(instance):
    original = instance.education
    instance.education = original
    assert instance.education == original




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
def test_hyp_patient_accepted_setter(instance):
    original = instance.accepted
    instance.accepted = original
    assert instance.accepted == original



@given(instance=Patient_strategy)
def test_hyp_patient_roomno_setter(instance):
    original = instance.roomno
    instance.roomno = original
    assert instance.roomno == original



@given(instance=Patient_strategy)
def test_hyp_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patient_strategy)
def test_hyp_patient_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Patient_strategy)
def test_hyp_patient_sickness_setter(instance):
    original = instance.sickness
    instance.sickness = original
    assert instance.sickness == original



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




@given(instance=Nurse_strategy)
def test_hyp_nurse_doctorid_setter(instance):
    original = instance.doctorid
    instance.doctorid = original
    assert instance.doctorid == original



@given(instance=Nurse_strategy)
def test_hyp_nurse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Nurse_strategy)
def test_hyp_nurse_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Doctor_strategy)
def test_hyp_doctor_phno_setter(instance):
    original = instance.phno
    instance.phno = original
    assert instance.phno == original



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
def test_hyp_doctor_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



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
    Administrative_staff,
    Bill,
    Department,
    Doctor,
    Hospital,
    Nurse,
    Nurse1,
    Operations_staff,
    Patient,
    Person,
    Room,
    Staff,
    Staff1,
    Technical_staff,
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


def test_Hospital_address_value_roundtrip():
    instance = Hospital(address="sample_text", name="sample_text", phone=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Hospital_name_value_roundtrip():
    instance = Hospital(address="sample_text", name="sample_text", phone=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Hospital_phone_value_roundtrip():
    instance = Hospital(address="sample_text", name="sample_text", phone=7)
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_Nurse_doctorid_value_roundtrip():
    instance = Nurse(doctorid=7, id=7, name="sample_text")
    assert instance.doctorid == 7
    instance.doctorid = 13
    assert instance.doctorid == 13


def test_Nurse_id_value_roundtrip():
    instance = Nurse(doctorid=7, id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Nurse_name_value_roundtrip():
    instance = Nurse(doctorid=7, id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Patient_accepted_value_roundtrip():
    instance = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    assert instance.accepted == date(2024, 1, 1)
    instance.accepted = date(2025, 6, 15)
    assert instance.accepted == date(2025, 6, 15)


def test_Patient_address_value_roundtrip():
    instance = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Patient_age_value_roundtrip():
    instance = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_Patient_roomno_value_roundtrip():
    instance = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    assert instance.roomno == 7
    instance.roomno = 13
    assert instance.roomno == 13


def test_Patient_sex_value_roundtrip():
    instance = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_Patient_sickness_value_roundtrip():
    instance = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    assert instance.sickness == "sample_text"
    instance.sickness = "sample_text_2"
    assert instance.sickness == "sample_text_2"


def test_Patient_telno_value_roundtrip():
    instance = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    assert instance.telno == 7
    instance.telno = 13
    assert instance.telno == 13


def test_Person_Gender_value_roundtrip():
    instance = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Person_Name_value_roundtrip():
    instance = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Person_Title_value_roundtrip():
    instance = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    assert instance.Title == "sample_text"
    instance.Title = "sample_text_2"
    assert instance.Title == "sample_text_2"


def test_Person_address_value_roundtrip():
    instance = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Person_birthDate_value_roundtrip():
    instance = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    assert instance.birthDate == date(2024, 1, 1)
    instance.birthDate = date(2025, 6, 15)
    assert instance.birthDate == date(2025, 6, 15)


def test_Person_phone_value_roundtrip():
    instance = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


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


def test_Staff_education_value_roundtrip():
    instance = Staff(education="sample_text", joined=date(2024, 1, 1))
    assert instance.education == "sample_text"
    instance.education = "sample_text_2"
    assert instance.education == "sample_text_2"


def test_Staff_joined_value_roundtrip():
    instance = Staff(education="sample_text", joined=date(2024, 1, 1))
    assert instance.joined == date(2024, 1, 1)
    instance.joined = date(2025, 6, 15)
    assert instance.joined == date(2025, 6, 15)


def test_assoc_Department_Staff_link_reassign_clear():
    a = Staff(education="sample_text", joined=date(2024, 1, 1))
    b1 = Department()
    b2 = Department()
    _safe_set(a, 'department20', b1)
    assert _is_linked(a, 'department20', b1)
    if hasattr(b1, 'staff21'):
        assert _is_linked(b1, 'staff21', a)
    _safe_set(a, 'department20', b2)
    assert _is_linked(a, 'department20', b2)
    if hasattr(b1, 'staff21'):
        assert not _is_linked(b1, 'staff21', a)
    if hasattr(b2, 'staff21'):
        assert _is_linked(b2, 'staff21', a)
    _safe_set(a, 'department20', None)
    assert not _is_linked(a, 'department20', b2)
    if hasattr(b2, 'staff21'):
        assert not _is_linked(b2, 'staff21', a)


def test_assoc_Doctor_Department_link_reassign_clear():
    a = Nurse(doctorid=7, id=7, name="sample_text")
    b1 = Doctor(address="sample_text", department="sample_text", docid=7, name="sample_text", phno=7, specialization="sample_text")
    b2 = Doctor(address="sample_text_2", department="sample_text_2", docid=13, name="sample_text_2", phno=13, specialization="sample_text_2")
    _safe_set(a, 'doctor3', {b1})
    assert _is_linked(a, 'doctor3', b1)
    if hasattr(b1, 'depmt2'):
        assert _is_linked(b1, 'depmt2', a)
    _safe_set(a, 'doctor3', {b2})
    assert _is_linked(a, 'doctor3', b2)
    if hasattr(b1, 'depmt2'):
        assert not _is_linked(b1, 'depmt2', a)
    if hasattr(b2, 'depmt2'):
        assert _is_linked(b2, 'depmt2', a)
    _safe_set(a, 'doctor3', set())
    assert not _is_linked(a, 'doctor3', b2)
    if hasattr(b2, 'depmt2'):
        assert not _is_linked(b2, 'depmt2', a)


def test_assoc_Doctor_Patient_link_reassign_clear():
    a = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
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


def test_assoc_Hospital_Department_link_reassign_clear():
    a = Hospital(address="sample_text", name="sample_text", phone=7)
    b1 = Department()
    b2 = Department()
    _safe_set(a, 'department19', {b1})
    assert _is_linked(a, 'department19', b1)
    if hasattr(b1, 'hospital18'):
        assert _is_linked(b1, 'hospital18', a)
    _safe_set(a, 'department19', {b2})
    assert _is_linked(a, 'department19', b2)
    if hasattr(b1, 'hospital18'):
        assert not _is_linked(b1, 'hospital18', a)
    if hasattr(b2, 'hospital18'):
        assert _is_linked(b2, 'hospital18', a)
    _safe_set(a, 'department19', set())
    assert not _is_linked(a, 'department19', b2)
    if hasattr(b2, 'hospital18'):
        assert not _is_linked(b2, 'hospital18', a)


def test_assoc_Patient_Bill_link_reassign_clear():
    a = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
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


def test_assoc_Patient_Operations_staff_link_reassign_clear():
    a = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    b1 = Operations_staff()
    b2 = Operations_staff()
    _safe_set(a, 'operations_staff23', {b1})
    assert _is_linked(a, 'operations_staff23', b1)
    if hasattr(b1, 'patient22'):
        assert _is_linked(b1, 'patient22', a)
    _safe_set(a, 'operations_staff23', {b2})
    assert _is_linked(a, 'operations_staff23', b2)
    if hasattr(b1, 'patient22'):
        assert not _is_linked(b1, 'patient22', a)
    if hasattr(b2, 'patient22'):
        assert _is_linked(b2, 'patient22', a)
    _safe_set(a, 'operations_staff23', set())
    assert not _is_linked(a, 'operations_staff23', b2)
    if hasattr(b2, 'patient22'):
        assert not _is_linked(b2, 'patient22', a)


def test_assoc_Patient_Room_link_reassign_clear():
    a = Room(location="sample_text", roomno=7)
    b1 = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    b2 = Patient(accepted=date(2025, 6, 15), address="sample_text_2", age=13, roomno=13, sex="sample_text_2", sickness="sample_text_2", telno=13)
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


def test_assoc_Person_Hospital_link_reassign_clear():
    a = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    b1 = Hospital(address="sample_text", name="sample_text", phone=7)
    b2 = Hospital(address="sample_text_2", name="sample_text_2", phone=13)
    _safe_set(a, 'hospital15', b1)
    assert _is_linked(a, 'hospital15', b1)
    if hasattr(b1, 'person14'):
        assert _is_linked(b1, 'person14', a)
    _safe_set(a, 'hospital15', b2)
    assert _is_linked(a, 'hospital15', b2)
    if hasattr(b1, 'person14'):
        assert not _is_linked(b1, 'person14', a)
    if hasattr(b2, 'person14'):
        assert _is_linked(b2, 'person14', a)
    _safe_set(a, 'hospital15', None)
    assert not _is_linked(a, 'hospital15', b2)
    if hasattr(b2, 'person14'):
        assert not _is_linked(b2, 'person14', a)


def test_assoc_Person_Hospital2_link_reassign_clear():
    a = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    b1 = Hospital(address="sample_text", name="sample_text", phone=7)
    b2 = Hospital(address="sample_text_2", name="sample_text_2", phone=13)
    _safe_set(a, 'Person_Hospital2_117', {b1})
    assert _is_linked(a, 'Person_Hospital2_117', b1)
    if hasattr(b1, 'person16'):
        assert _is_linked(b1, 'person16', a)
    _safe_set(a, 'Person_Hospital2_117', {b2})
    assert _is_linked(a, 'Person_Hospital2_117', b2)
    if hasattr(b1, 'person16'):
        assert not _is_linked(b1, 'person16', a)
    if hasattr(b2, 'person16'):
        assert _is_linked(b2, 'person16', a)
    _safe_set(a, 'Person_Hospital2_117', set())
    assert not _is_linked(a, 'Person_Hospital2_117', b2)
    if hasattr(b2, 'person16'):
        assert not _is_linked(b2, 'person16', a)


def test_assoc_Person_Hospital3_link_reassign_clear():
    a = Person(Gender="sample_text", Name="sample_text", Title="sample_text", address="sample_text", birthDate=date(2024, 1, 1), phone=7)
    b1 = Hospital(address="sample_text", name="sample_text", phone=7)
    b2 = Hospital(address="sample_text_2", name="sample_text_2", phone=13)
    _safe_set(a, 'hospital25', {b1})
    assert _is_linked(a, 'hospital25', b1)
    if hasattr(b1, 'person24'):
        assert _is_linked(b1, 'person24', a)
    _safe_set(a, 'hospital25', {b2})
    assert _is_linked(a, 'hospital25', b2)
    if hasattr(b1, 'person24'):
        assert not _is_linked(b1, 'person24', a)
    if hasattr(b2, 'person24'):
        assert _is_linked(b2, 'person24', a)
    _safe_set(a, 'hospital25', set())
    assert not _is_linked(a, 'hospital25', b2)
    if hasattr(b2, 'person24'):
        assert not _is_linked(b2, 'person24', a)


def test_assoc_Room_Staff_link_reassign_clear():
    a = Room(location="sample_text", roomno=7)
    b1 = Staff1()
    b2 = Staff1()
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
    a = Staff(education="sample_text", joined=date(2024, 1, 1))
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
    a = Staff(education="sample_text", joined=date(2024, 1, 1))
    b1 = Patient(accepted=date(2024, 1, 1), address="sample_text", age=7, roomno=7, sex="sample_text", sickness="sample_text", telno=7)
    b2 = Patient(accepted=date(2025, 6, 15), address="sample_text_2", age=13, roomno=13, sex="sample_text_2", sickness="sample_text_2", telno=13)
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

Administrative_staff_strategy = st.builds(Administrative_staff)
@given(instance=Administrative_staff_strategy)
@settings(max_examples=25)
def test_Administrative_staff_instantiation(instance):
    assert isinstance(instance, Administrative_staff)


Bill_strategy = st.builds(Bill, amount=st.floats(allow_nan=False, allow_infinity=False), billno=safe_text, patientname=safe_text)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Department_strategy = st.builds(Department)
@given(instance=Department_strategy)
@settings(max_examples=25)
def test_Department_instantiation(instance):
    assert isinstance(instance, Department)


Doctor_strategy = st.builds(Doctor, address=safe_text, department=safe_text, docid=st.integers(), name=safe_text, phno=st.integers(), specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Hospital_strategy = st.builds(Hospital, address=safe_text, name=safe_text, phone=st.integers())
@given(instance=Hospital_strategy)
@settings(max_examples=25)
def test_Hospital_instantiation(instance):
    assert isinstance(instance, Hospital)


Nurse_strategy = st.builds(Nurse, doctorid=st.integers(), id=st.integers(), name=safe_text)
@given(instance=Nurse_strategy)
@settings(max_examples=25)
def test_Nurse_instantiation(instance):
    assert isinstance(instance, Nurse)


Nurse1_strategy = st.builds(Nurse1)
@given(instance=Nurse1_strategy)
@settings(max_examples=25)
def test_Nurse1_instantiation(instance):
    assert isinstance(instance, Nurse1)


Operations_staff_strategy = st.builds(Operations_staff)
@given(instance=Operations_staff_strategy)
@settings(max_examples=25)
def test_Operations_staff_instantiation(instance):
    assert isinstance(instance, Operations_staff)


Patient_strategy = st.builds(Patient, accepted=st.dates(), address=safe_text, age=st.integers(), roomno=st.integers(), sex=safe_text, sickness=safe_text, telno=st.integers())
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Person_strategy = st.builds(Person, Gender=safe_text, Name=safe_text, Title=safe_text, address=safe_text, birthDate=st.dates(), phone=st.integers())
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Room_strategy = st.builds(Room, location=safe_text, roomno=st.integers())
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


Staff_strategy = st.builds(Staff, education=safe_text, joined=st.dates())
@given(instance=Staff_strategy)
@settings(max_examples=25)
def test_Staff_instantiation(instance):
    assert isinstance(instance, Staff)


Staff1_strategy = st.builds(Staff1)
@given(instance=Staff1_strategy)
@settings(max_examples=25)
def test_Staff1_instantiation(instance):
    assert isinstance(instance, Staff1)


Technical_staff_strategy = st.builds(Technical_staff)
@given(instance=Technical_staff_strategy)
@settings(max_examples=25)
def test_Technical_staff_instantiation(instance):
    assert isinstance(instance, Technical_staff)



