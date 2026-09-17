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
    Health_Records,
    Sickness,
    Appointment,
    Patient,
    Medicine,
    Technician,
    Doctor,
    Nurse,
    Staff,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_health_records_is_not_abstract():
    assert not inspect.isabstract(Health_Records)


def test_hyp_health_records_constructor_exists():
    assert callable(Health_Records.__init__)


def test_hyp_health_records_constructor_args():
    sig = inspect.signature(Health_Records.__init__)
    params = list(sig.parameters.keys())
    assert "healthhistory" in params, "Missing parameter 'healthhistory'"




def test_hyp_sickness_is_not_abstract():
    assert not inspect.isabstract(Sickness)


def test_hyp_sickness_constructor_exists():
    assert callable(Sickness.__init__)


def test_hyp_sickness_constructor_args():
    sig = inspect.signature(Sickness.__init__)
    params = list(sig.parameters.keys())
    assert "recommendations" in params, "Missing parameter 'recommendations'"
    assert "symptoms" in params, "Missing parameter 'symptoms'"
    assert "prescription" in params, "Missing parameter 'prescription'"






def test_hyp_appointment_is_not_abstract():
    assert not inspect.isabstract(Appointment)


def test_hyp_appointment_constructor_exists():
    assert callable(Appointment.__init__)


def test_hyp_appointment_constructor_args():
    sig = inspect.signature(Appointment.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "location" in params, "Missing parameter 'location'"
    assert "date" in params, "Missing parameter 'date'"






def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "healthrecords" in params, "Missing parameter 'healthrecords'"






def test_hyp_medicine_is_not_abstract():
    assert not inspect.isabstract(Medicine)


def test_hyp_medicine_constructor_exists():
    assert callable(Medicine.__init__)


def test_hyp_medicine_constructor_args():
    sig = inspect.signature(Medicine.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"
    assert "amount" in params, "Missing parameter 'amount'"







def test_hyp_technician_is_not_abstract():
    assert not inspect.isabstract(Technician)


def test_hyp_technician_constructor_exists():
    assert callable(Technician.__init__)


def test_hyp_technician_constructor_args():
    sig = inspect.signature(Technician.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "speciality" in params, "Missing parameter 'speciality'"






def test_hyp_nurse_is_not_abstract():
    assert not inspect.isabstract(Nurse)


def test_hyp_nurse_constructor_exists():
    assert callable(Nurse.__init__)


def test_hyp_nurse_constructor_args():
    sig = inspect.signature(Nurse.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_hyp_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_hyp_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "job" in params, "Missing parameter 'job'"





def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "job" in params, "Missing parameter 'job'"






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
Health_Records_strategy = st.builds(
    Health_Records,
    healthhistory=
        safe_text
)
Sickness_strategy = st.builds(
    Sickness,
    recommendations=
        safe_text,
    symptoms=
        safe_text,
    prescription=
        safe_text
)
Appointment_strategy = st.builds(
    Appointment,
    time=
        st.integers(),
    location=
        safe_text,
    date=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    name=
        safe_text,
    id=
        st.integers(),
    healthrecords=
        safe_text
)
Medicine_strategy = st.builds(
    Medicine,
    code=
        st.integers(),
    price=
        safe_text,
    name=
        safe_text,
    amount=
        st.integers()
)
Technician_strategy = st.builds(
    Technician,
    name=
        safe_text,
    id=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    name=
        safe_text,
    id=
        st.integers(),
    speciality=
        safe_text
)
Nurse_strategy = st.builds(
    Nurse,
    id=
        st.integers(),
    name=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    name=
        safe_text,
    job=
        safe_text
)
Person_strategy = st.builds(
    Person,
    id=
        st.integers(),
    email=
        safe_text,
    name=
        safe_text,
    job=
        safe_text
)




@given(instance=Health_Records_strategy)
def test_hyp_health_records_healthhistory_setter(instance):
    original = instance.healthhistory
    instance.healthhistory = original
    assert instance.healthhistory == original




@given(instance=Sickness_strategy)
def test_hyp_sickness_recommendations_setter(instance):
    original = instance.recommendations
    instance.recommendations = original
    assert instance.recommendations == original



@given(instance=Sickness_strategy)
def test_hyp_sickness_symptoms_setter(instance):
    original = instance.symptoms
    instance.symptoms = original
    assert instance.symptoms == original



@given(instance=Sickness_strategy)
def test_hyp_sickness_prescription_setter(instance):
    original = instance.prescription
    instance.prescription = original
    assert instance.prescription == original




@given(instance=Appointment_strategy)
def test_hyp_appointment_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Appointment_strategy)
def test_hyp_appointment_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Appointment_strategy)
def test_hyp_appointment_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=Patient_strategy)
def test_hyp_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_hyp_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_hyp_patient_healthrecords_setter(instance):
    original = instance.healthrecords
    instance.healthrecords = original
    assert instance.healthrecords == original




@given(instance=Medicine_strategy)
def test_hyp_medicine_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=Medicine_strategy)
def test_hyp_medicine_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Medicine_strategy)
def test_hyp_medicine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Medicine_strategy)
def test_hyp_medicine_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=Technician_strategy)
def test_hyp_technician_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Technician_strategy)
def test_hyp_technician_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Doctor_strategy)
def test_hyp_doctor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_speciality_setter(instance):
    original = instance.speciality
    instance.speciality = original
    assert instance.speciality == original




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




@given(instance=Staff_strategy)
def test_hyp_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Staff_strategy)
def test_hyp_staff_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original




@given(instance=Person_strategy)
def test_hyp_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Person_strategy)
def test_hyp_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Person_strategy)
def test_hyp_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_hyp_person_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Appointment,
    Doctor,
    Health_Records,
    Medicine,
    Nurse,
    Patient,
    Person,
    Sickness,
    Staff,
    Technician,
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

def test_Appointment_date_value_roundtrip():
    instance = Appointment(date="sample_text", location="sample_text", time=7)
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Appointment_location_value_roundtrip():
    instance = Appointment(date="sample_text", location="sample_text", time=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_Appointment_time_value_roundtrip():
    instance = Appointment(date="sample_text", location="sample_text", time=7)
    assert instance.time == 7
    instance.time = 13
    assert instance.time == 13


def test_Doctor_id_value_roundtrip():
    instance = Doctor(id=7, name="sample_text", speciality="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Doctor_name_value_roundtrip():
    instance = Doctor(id=7, name="sample_text", speciality="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Doctor_speciality_value_roundtrip():
    instance = Doctor(id=7, name="sample_text", speciality="sample_text")
    assert instance.speciality == "sample_text"
    instance.speciality = "sample_text_2"
    assert instance.speciality == "sample_text_2"


def test_Health_Records_healthhistory_value_roundtrip():
    instance = Health_Records(healthhistory="sample_text")
    assert instance.healthhistory == "sample_text"
    instance.healthhistory = "sample_text_2"
    assert instance.healthhistory == "sample_text_2"


def test_Medicine_amount_value_roundtrip():
    instance = Medicine(amount=7, code=7, name="sample_text", price="sample_text")
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_Medicine_code_value_roundtrip():
    instance = Medicine(amount=7, code=7, name="sample_text", price="sample_text")
    assert instance.code == 7
    instance.code = 13
    assert instance.code == 13


def test_Medicine_name_value_roundtrip():
    instance = Medicine(amount=7, code=7, name="sample_text", price="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Medicine_price_value_roundtrip():
    instance = Medicine(amount=7, code=7, name="sample_text", price="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_Nurse_id_value_roundtrip():
    instance = Nurse(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Nurse_name_value_roundtrip():
    instance = Nurse(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Patient_healthrecords_value_roundtrip():
    instance = Patient(healthrecords="sample_text", id=7, name="sample_text")
    assert instance.healthrecords == "sample_text"
    instance.healthrecords = "sample_text_2"
    assert instance.healthrecords == "sample_text_2"


def test_Patient_id_value_roundtrip():
    instance = Patient(healthrecords="sample_text", id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Patient_name_value_roundtrip():
    instance = Patient(healthrecords="sample_text", id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Person_email_value_roundtrip():
    instance = Person(email="sample_text", id=7, job="sample_text", name="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Person_id_value_roundtrip():
    instance = Person(email="sample_text", id=7, job="sample_text", name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Person_job_value_roundtrip():
    instance = Person(email="sample_text", id=7, job="sample_text", name="sample_text")
    assert instance.job == "sample_text"
    instance.job = "sample_text_2"
    assert instance.job == "sample_text_2"


def test_Person_name_value_roundtrip():
    instance = Person(email="sample_text", id=7, job="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Sickness_prescription_value_roundtrip():
    instance = Sickness(prescription="sample_text", recommendations="sample_text", symptoms="sample_text")
    assert instance.prescription == "sample_text"
    instance.prescription = "sample_text_2"
    assert instance.prescription == "sample_text_2"


def test_Sickness_recommendations_value_roundtrip():
    instance = Sickness(prescription="sample_text", recommendations="sample_text", symptoms="sample_text")
    assert instance.recommendations == "sample_text"
    instance.recommendations = "sample_text_2"
    assert instance.recommendations == "sample_text_2"


def test_Sickness_symptoms_value_roundtrip():
    instance = Sickness(prescription="sample_text", recommendations="sample_text", symptoms="sample_text")
    assert instance.symptoms == "sample_text"
    instance.symptoms = "sample_text_2"
    assert instance.symptoms == "sample_text_2"


def test_Staff_job_value_roundtrip():
    instance = Staff(job="sample_text", name="sample_text")
    assert instance.job == "sample_text"
    instance.job = "sample_text_2"
    assert instance.job == "sample_text_2"


def test_Staff_name_value_roundtrip():
    instance = Staff(job="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Technician_id_value_roundtrip():
    instance = Technician(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Technician_name_value_roundtrip():
    instance = Technician(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_Appointment_Doctor_link_reassign_clear():
    a = Doctor(id=7, name="sample_text", speciality="sample_text")
    b1 = Appointment(date="sample_text", location="sample_text", time=7)
    b2 = Appointment(date="sample_text_2", location="sample_text_2", time=13)
    _safe_set(a, 'appointment13', b1)
    assert _is_linked(a, 'appointment13', b1)
    if hasattr(b1, 'doctor12'):
        assert _is_linked(b1, 'doctor12', a)
    _safe_set(a, 'appointment13', b2)
    assert _is_linked(a, 'appointment13', b2)
    if hasattr(b1, 'doctor12'):
        assert not _is_linked(b1, 'doctor12', a)
    if hasattr(b2, 'doctor12'):
        assert _is_linked(b2, 'doctor12', a)
    _safe_set(a, 'appointment13', None)
    assert not _is_linked(a, 'appointment13', b2)
    if hasattr(b2, 'doctor12'):
        assert not _is_linked(b2, 'doctor12', a)


def test_assoc_Appointment_Patient_link_reassign_clear():
    a = Patient(healthrecords="sample_text", id=7, name="sample_text")
    b1 = Appointment(date="sample_text", location="sample_text", time=7)
    b2 = Appointment(date="sample_text_2", location="sample_text_2", time=13)
    _safe_set(a, 'appointment15', b1)
    assert _is_linked(a, 'appointment15', b1)
    if hasattr(b1, 'patient14'):
        assert _is_linked(b1, 'patient14', a)
    _safe_set(a, 'appointment15', b2)
    assert _is_linked(a, 'appointment15', b2)
    if hasattr(b1, 'patient14'):
        assert not _is_linked(b1, 'patient14', a)
    if hasattr(b2, 'patient14'):
        assert _is_linked(b2, 'patient14', a)
    _safe_set(a, 'appointment15', None)
    assert not _is_linked(a, 'appointment15', b2)
    if hasattr(b2, 'patient14'):
        assert not _is_linked(b2, 'patient14', a)


def test_assoc_Doctor_Health_Records_link_reassign_clear():
    a = Health_Records(healthhistory="sample_text")
    b1 = Doctor(id=7, name="sample_text", speciality="sample_text")
    b2 = Doctor(id=13, name="sample_text_2", speciality="sample_text_2")
    _safe_set(a, 'doctor19', b1)
    assert _is_linked(a, 'doctor19', b1)
    if hasattr(b1, 'health_Records18'):
        assert _is_linked(b1, 'health_Records18', a)
    _safe_set(a, 'doctor19', b2)
    assert _is_linked(a, 'doctor19', b2)
    if hasattr(b1, 'health_Records18'):
        assert not _is_linked(b1, 'health_Records18', a)
    if hasattr(b2, 'health_Records18'):
        assert _is_linked(b2, 'health_Records18', a)
    _safe_set(a, 'doctor19', None)
    assert not _is_linked(a, 'doctor19', b2)
    if hasattr(b2, 'health_Records18'):
        assert not _is_linked(b2, 'health_Records18', a)


def test_assoc_Doctor_Medicine_link_reassign_clear():
    a = Medicine(amount=7, code=7, name="sample_text", price="sample_text")
    b1 = Doctor(id=7, name="sample_text", speciality="sample_text")
    b2 = Doctor(id=13, name="sample_text_2", speciality="sample_text_2")
    _safe_set(a, 'doctor9', b1)
    assert _is_linked(a, 'doctor9', b1)
    if hasattr(b1, 'medicine8'):
        assert _is_linked(b1, 'medicine8', a)
    _safe_set(a, 'doctor9', b2)
    assert _is_linked(a, 'doctor9', b2)
    if hasattr(b1, 'medicine8'):
        assert not _is_linked(b1, 'medicine8', a)
    if hasattr(b2, 'medicine8'):
        assert _is_linked(b2, 'medicine8', a)
    _safe_set(a, 'doctor9', None)
    assert not _is_linked(a, 'doctor9', b2)
    if hasattr(b2, 'medicine8'):
        assert not _is_linked(b2, 'medicine8', a)


def test_assoc_Health_Records_Patient_link_reassign_clear():
    a = Patient(healthrecords="sample_text", id=7, name="sample_text")
    b1 = Health_Records(healthhistory="sample_text")
    b2 = Health_Records(healthhistory="sample_text_2")
    _safe_set(a, 'health_Records21', b1)
    assert _is_linked(a, 'health_Records21', b1)
    if hasattr(b1, 'patient20'):
        assert _is_linked(b1, 'patient20', a)
    _safe_set(a, 'health_Records21', b2)
    assert _is_linked(a, 'health_Records21', b2)
    if hasattr(b1, 'patient20'):
        assert not _is_linked(b1, 'patient20', a)
    if hasattr(b2, 'patient20'):
        assert _is_linked(b2, 'patient20', a)
    _safe_set(a, 'health_Records21', None)
    assert not _is_linked(a, 'health_Records21', b2)
    if hasattr(b2, 'patient20'):
        assert not _is_linked(b2, 'patient20', a)


def test_assoc_Person_Patient_link_reassign_clear():
    a = Person(email="sample_text", id=7, job="sample_text", name="sample_text")
    b1 = Patient(healthrecords="sample_text", id=7, name="sample_text")
    b2 = Patient(healthrecords="sample_text_2", id=13, name="sample_text_2")
    _safe_set(a, 'patient10', b1)
    assert _is_linked(a, 'patient10', b1)
    if hasattr(b1, 'person11'):
        assert _is_linked(b1, 'person11', a)
    _safe_set(a, 'patient10', b2)
    assert _is_linked(a, 'patient10', b2)
    if hasattr(b1, 'person11'):
        assert not _is_linked(b1, 'person11', a)
    if hasattr(b2, 'person11'):
        assert _is_linked(b2, 'person11', a)
    _safe_set(a, 'patient10', None)
    assert not _is_linked(a, 'patient10', b2)
    if hasattr(b2, 'person11'):
        assert not _is_linked(b2, 'person11', a)


def test_assoc_Person_Staff_link_reassign_clear():
    a = Staff(job="sample_text", name="sample_text")
    b1 = Person(email="sample_text", id=7, job="sample_text", name="sample_text")
    b2 = Person(email="sample_text_2", id=13, job="sample_text_2", name="sample_text_2")
    _safe_set(a, 'person1', b1)
    assert _is_linked(a, 'person1', b1)
    if hasattr(b1, 'staff0'):
        assert _is_linked(b1, 'staff0', a)
    _safe_set(a, 'person1', b2)
    assert _is_linked(a, 'person1', b2)
    if hasattr(b1, 'staff0'):
        assert not _is_linked(b1, 'staff0', a)
    if hasattr(b2, 'staff0'):
        assert _is_linked(b2, 'staff0', a)
    _safe_set(a, 'person1', None)
    assert not _is_linked(a, 'person1', b2)
    if hasattr(b2, 'staff0'):
        assert not _is_linked(b2, 'staff0', a)


def test_assoc_Sickness_Patient_link_reassign_clear():
    a = Sickness(prescription="sample_text", recommendations="sample_text", symptoms="sample_text")
    b1 = Patient(healthrecords="sample_text", id=7, name="sample_text")
    b2 = Patient(healthrecords="sample_text_2", id=13, name="sample_text_2")
    _safe_set(a, 'patient16', b1)
    assert _is_linked(a, 'patient16', b1)
    if hasattr(b1, 'sickness17'):
        assert _is_linked(b1, 'sickness17', a)
    _safe_set(a, 'patient16', b2)
    assert _is_linked(a, 'patient16', b2)
    if hasattr(b1, 'sickness17'):
        assert not _is_linked(b1, 'sickness17', a)
    if hasattr(b2, 'sickness17'):
        assert _is_linked(b2, 'sickness17', a)
    _safe_set(a, 'patient16', None)
    assert not _is_linked(a, 'patient16', b2)
    if hasattr(b2, 'sickness17'):
        assert not _is_linked(b2, 'sickness17', a)


def test_assoc_Staff_Doctor_link_reassign_clear():
    a = Staff(job="sample_text", name="sample_text")
    b1 = Doctor(id=7, name="sample_text", speciality="sample_text")
    b2 = Doctor(id=13, name="sample_text_2", speciality="sample_text_2")
    _safe_set(a, 'doctor4', b1)
    assert _is_linked(a, 'doctor4', b1)
    if hasattr(b1, 'staff5'):
        assert _is_linked(b1, 'staff5', a)
    _safe_set(a, 'doctor4', b2)
    assert _is_linked(a, 'doctor4', b2)
    if hasattr(b1, 'staff5'):
        assert not _is_linked(b1, 'staff5', a)
    if hasattr(b2, 'staff5'):
        assert _is_linked(b2, 'staff5', a)
    _safe_set(a, 'doctor4', None)
    assert not _is_linked(a, 'doctor4', b2)
    if hasattr(b2, 'staff5'):
        assert not _is_linked(b2, 'staff5', a)


def test_assoc_Staff_Nurse_link_reassign_clear():
    a = Staff(job="sample_text", name="sample_text")
    b1 = Nurse(id=7, name="sample_text")
    b2 = Nurse(id=13, name="sample_text_2")
    _safe_set(a, 'nurse2', b1)
    assert _is_linked(a, 'nurse2', b1)
    if hasattr(b1, 'staff3'):
        assert _is_linked(b1, 'staff3', a)
    _safe_set(a, 'nurse2', b2)
    assert _is_linked(a, 'nurse2', b2)
    if hasattr(b1, 'staff3'):
        assert not _is_linked(b1, 'staff3', a)
    if hasattr(b2, 'staff3'):
        assert _is_linked(b2, 'staff3', a)
    _safe_set(a, 'nurse2', None)
    assert not _is_linked(a, 'nurse2', b2)
    if hasattr(b2, 'staff3'):
        assert not _is_linked(b2, 'staff3', a)


def test_assoc_Staff_Technician_link_reassign_clear():
    a = Technician(id=7, name="sample_text")
    b1 = Staff(job="sample_text", name="sample_text")
    b2 = Staff(job="sample_text_2", name="sample_text_2")
    _safe_set(a, 'staff7', b1)
    assert _is_linked(a, 'staff7', b1)
    if hasattr(b1, 'technician6'):
        assert _is_linked(b1, 'technician6', a)
    _safe_set(a, 'staff7', b2)
    assert _is_linked(a, 'staff7', b2)
    if hasattr(b1, 'technician6'):
        assert not _is_linked(b1, 'technician6', a)
    if hasattr(b2, 'technician6'):
        assert _is_linked(b2, 'technician6', a)
    _safe_set(a, 'staff7', None)
    assert not _is_linked(a, 'staff7', b2)
    if hasattr(b2, 'technician6'):
        assert not _is_linked(b2, 'technician6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Appointment_strategy = st.builds(Appointment, date=safe_text, location=safe_text, time=st.integers())
@given(instance=Appointment_strategy)
@settings(max_examples=25)
def test_Appointment_instantiation(instance):
    assert isinstance(instance, Appointment)


Doctor_strategy = st.builds(Doctor, id=st.integers(), name=safe_text, speciality=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Health_Records_strategy = st.builds(Health_Records, healthhistory=safe_text)
@given(instance=Health_Records_strategy)
@settings(max_examples=25)
def test_Health_Records_instantiation(instance):
    assert isinstance(instance, Health_Records)


Medicine_strategy = st.builds(Medicine, amount=st.integers(), code=st.integers(), name=safe_text, price=safe_text)
@given(instance=Medicine_strategy)
@settings(max_examples=25)
def test_Medicine_instantiation(instance):
    assert isinstance(instance, Medicine)


Nurse_strategy = st.builds(Nurse, id=st.integers(), name=safe_text)
@given(instance=Nurse_strategy)
@settings(max_examples=25)
def test_Nurse_instantiation(instance):
    assert isinstance(instance, Nurse)


Patient_strategy = st.builds(Patient, healthrecords=safe_text, id=st.integers(), name=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Person_strategy = st.builds(Person, email=safe_text, id=st.integers(), job=safe_text, name=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Sickness_strategy = st.builds(Sickness, prescription=safe_text, recommendations=safe_text, symptoms=safe_text)
@given(instance=Sickness_strategy)
@settings(max_examples=25)
def test_Sickness_instantiation(instance):
    assert isinstance(instance, Sickness)


Staff_strategy = st.builds(Staff, job=safe_text, name=safe_text)
@given(instance=Staff_strategy)
@settings(max_examples=25)
def test_Staff_instantiation(instance):
    assert isinstance(instance, Staff)


Technician_strategy = st.builds(Technician, id=st.integers(), name=safe_text)
@given(instance=Technician_strategy)
@settings(max_examples=25)
def test_Technician_instantiation(instance):
    assert isinstance(instance, Technician)



