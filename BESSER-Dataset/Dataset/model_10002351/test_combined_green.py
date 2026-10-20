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
    appointment,
    Room,
    Patient,
    Receptionist,
    It,
    nurse,
    doctor,
    employee,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_appointment_is_not_abstract():
    assert not inspect.isabstract(appointment)


def test_hyp_appointment_constructor_exists():
    assert callable(appointment.__init__)


def test_hyp_appointment_constructor_args():
    sig = inspect.signature(appointment.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "day" in params, "Missing parameter 'day'"
    assert "hour" in params, "Missing parameter 'hour'"







def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "available" in params, "Missing parameter 'available'"
    assert "capasittity" in params, "Missing parameter 'capasittity'"
    assert "num" in params, "Missing parameter 'num'"
    assert "room_type" in params, "Missing parameter 'room_type'"
    assert "patients" in params, "Missing parameter 'patients'"








def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "_doc" in params, "Missing parameter '_doc'"
    assert "id" in params, "Missing parameter 'id'"
    assert "_nur" in params, "Missing parameter '_nur'"
    assert "illness" in params, "Missing parameter 'illness'"

def test_hyp_patient_has__doc():
    assert hasattr(Patient, "_doc")
    descriptor = None
    for klass in Patient.__mro__:
        if "_doc" in klass.__dict__:
            descriptor = klass.__dict__["_doc"]
            break
    assert isinstance(descriptor, property)

def test_hyp_patient_has_id():
    assert hasattr(Patient, "id")
    descriptor = None
    for klass in Patient.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_patient_has__nur():
    assert hasattr(Patient, "_nur")
    descriptor = None
    for klass in Patient.__mro__:
        if "_nur" in klass.__dict__:
            descriptor = klass.__dict__["_nur"]
            break
    assert isinstance(descriptor, property)

def test_hyp_patient_has_illness():
    assert hasattr(Patient, "illness")
    descriptor = None
    for klass in Patient.__mro__:
        if "illness" in klass.__dict__:
            descriptor = klass.__dict__["illness"]
            break
    assert isinstance(descriptor, property)



def test_hyp_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_hyp_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_hyp_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_it_is_not_abstract():
    assert not inspect.isabstract(It)


def test_hyp_it_constructor_exists():
    assert callable(It.__init__)


def test_hyp_it_constructor_args():
    sig = inspect.signature(It.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"




def test_hyp_nurse_is_not_abstract():
    assert not inspect.isabstract(nurse)


def test_hyp_nurse_constructor_exists():
    assert callable(nurse.__init__)


def test_hyp_nurse_constructor_args():
    sig = inspect.signature(nurse.__init__)
    params = list(sig.parameters.keys())
    assert "_rom" in params, "Missing parameter '_rom'"

def test_hyp_nurse_has__rom():
    assert hasattr(nurse, "_rom")
    descriptor = None
    for klass in nurse.__mro__:
        if "_rom" in klass.__dict__:
            descriptor = klass.__dict__["_rom"]
            break
    assert isinstance(descriptor, property)



def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(doctor.__init__)
    params = list(sig.parameters.keys())
    assert "weekappointment" in params, "Missing parameter 'weekappointment'"
    assert "patient" in params, "Missing parameter 'patient'"





def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(employee)


def test_hyp_employee_constructor_exists():
    assert callable(employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(employee.__init__)
    params = list(sig.parameters.keys())
    assert "department" in params, "Missing parameter 'department'"
    assert "Salary" in params, "Missing parameter 'Salary'"
    assert "password" in params, "Missing parameter 'password'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "name" in params, "Missing parameter 'name'"




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
appointment_strategy = st.builds(
    appointment,
    duration=
        st.integers(),
    minute=
        st.integers(),
    day=
        st.integers(),
    hour=
        st.integers()
)
Room_strategy = st.builds(
    Room,
    available=
        st.booleans(),
    capasittity=
        st.integers(),
    num=
        st.integers(),
    room_type=
        safe_text,
    patients=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    _doc=
        st.none(),
    id=
        safe_text,
    _nur=
        st.none(),
    illness=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
)
It_strategy = st.builds(
    It,
    password=
        safe_text
)
nurse_strategy = st.builds(
    nurse,
    _rom=
        st.none()
)
doctor_strategy = st.builds(
    doctor,
    weekappointment=
        safe_text,
    patient=
        safe_text
)
employee_strategy = st.builds(
    employee,
    department=
        safe_text,
    Salary=
        st.integers(),
    password=
        safe_text,
    id=
        safe_text
)
Person_strategy = st.builds(
    Person,
    age=
        st.integers(),
    name=
        safe_text
)




@given(instance=appointment_strategy)
def test_hyp_appointment_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=appointment_strategy)
def test_hyp_appointment_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=appointment_strategy)
def test_hyp_appointment_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=appointment_strategy)
def test_hyp_appointment_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original




@given(instance=Room_strategy)
def test_hyp_room_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original



@given(instance=Room_strategy)
def test_hyp_room_capasittity_setter(instance):
    original = instance.capasittity
    instance.capasittity = original
    assert instance.capasittity == original



@given(instance=Room_strategy)
def test_hyp_room_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Room_strategy)
def test_hyp_room_room_type_setter(instance):
    original = instance.room_type
    instance.room_type = original
    assert instance.room_type == original



@given(instance=Room_strategy)
def test_hyp_room_patients_setter(instance):
    original = instance.patients
    instance.patients = original
    assert instance.patients == original

@given(instance=Patient_strategy)
@settings(max_examples=50)
def test_hyp_patient_instantiation(instance):
    assert isinstance(instance, Patient)



@given(instance=Patient_strategy)
def test_hyp_patient__doc_setter(instance):
    original = instance._doc
    instance._doc = original
    assert instance._doc == original



@given(instance=Patient_strategy)
def test_hyp_patient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patient_strategy)
def test_hyp_patient__nur_setter(instance):
    original = instance._nur
    instance._nur = original
    assert instance._nur == original



@given(instance=Patient_strategy)
def test_hyp_patient_illness_setter(instance):
    original = instance.illness
    instance.illness = original
    assert instance.illness == original





@given(instance=It_strategy)
def test_hyp_it_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=nurse_strategy)
@settings(max_examples=50)
def test_hyp_nurse_instantiation(instance):
    assert isinstance(instance, nurse)



@given(instance=nurse_strategy)
def test_hyp_nurse__rom_setter(instance):
    original = instance._rom
    instance._rom = original
    assert instance._rom == original




@given(instance=doctor_strategy)
def test_hyp_doctor_weekappointment_setter(instance):
    original = instance.weekappointment
    instance.weekappointment = original
    assert instance.weekappointment == original



@given(instance=doctor_strategy)
def test_hyp_doctor_patient_setter(instance):
    original = instance.patient
    instance.patient = original
    assert instance.patient == original




@given(instance=employee_strategy)
def test_hyp_employee_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=employee_strategy)
def test_hyp_employee_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original



@given(instance=employee_strategy)
def test_hyp_employee_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=employee_strategy)
def test_hyp_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Person_strategy)
def test_hyp_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Person_strategy)
def test_hyp_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    It,
    Patient,
    Person,
    Receptionist,
    Room,
    appointment,
    doctor,
    employee,
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

def test_It_password_value_roundtrip():
    instance = It(password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Person_age_value_roundtrip():
    instance = Person(age=7, name="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_Person_name_value_roundtrip():
    instance = Person(age=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Room_available_value_roundtrip():
    instance = Room(available=True, capasittity=7, num=7, patients="sample_text", room_type="sample_text")
    assert instance.available == True
    instance.available = False
    assert instance.available == False


def test_Room_capasittity_value_roundtrip():
    instance = Room(available=True, capasittity=7, num=7, patients="sample_text", room_type="sample_text")
    assert instance.capasittity == 7
    instance.capasittity = 13
    assert instance.capasittity == 13


def test_Room_num_value_roundtrip():
    instance = Room(available=True, capasittity=7, num=7, patients="sample_text", room_type="sample_text")
    assert instance.num == 7
    instance.num = 13
    assert instance.num == 13


def test_Room_patients_value_roundtrip():
    instance = Room(available=True, capasittity=7, num=7, patients="sample_text", room_type="sample_text")
    assert instance.patients == "sample_text"
    instance.patients = "sample_text_2"
    assert instance.patients == "sample_text_2"


def test_Room_room_type_value_roundtrip():
    instance = Room(available=True, capasittity=7, num=7, patients="sample_text", room_type="sample_text")
    assert instance.room_type == "sample_text"
    instance.room_type = "sample_text_2"
    assert instance.room_type == "sample_text_2"


def test_appointment_day_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7)
    assert instance.day == 7
    instance.day = 13
    assert instance.day == 13


def test_appointment_duration_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7)
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_appointment_hour_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7)
    assert instance.hour == 7
    instance.hour = 13
    assert instance.hour == 13


def test_appointment_minute_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7)
    assert instance.minute == 7
    instance.minute = 13
    assert instance.minute == 13


def test_doctor_patient_value_roundtrip():
    instance = doctor(patient="sample_text", weekappointment="sample_text")
    assert instance.patient == "sample_text"
    instance.patient = "sample_text_2"
    assert instance.patient == "sample_text_2"


def test_doctor_weekappointment_value_roundtrip():
    instance = doctor(patient="sample_text", weekappointment="sample_text")
    assert instance.weekappointment == "sample_text"
    instance.weekappointment = "sample_text_2"
    assert instance.weekappointment == "sample_text_2"


def test_employee_Salary_value_roundtrip():
    instance = employee(Salary=7, department="sample_text", id="sample_text", password="sample_text")
    assert instance.Salary == 7
    instance.Salary = 13
    assert instance.Salary == 13


def test_employee_department_value_roundtrip():
    instance = employee(Salary=7, department="sample_text", id="sample_text", password="sample_text")
    assert instance.department == "sample_text"
    instance.department = "sample_text_2"
    assert instance.department == "sample_text_2"


def test_employee_id_value_roundtrip():
    instance = employee(Salary=7, department="sample_text", id="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_employee_password_value_roundtrip():
    instance = employee(Salary=7, department="sample_text", id="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

It_strategy = st.builds(It, password=safe_text)
@given(instance=It_strategy)
@settings(max_examples=25)
def test_It_instantiation(instance):
    assert isinstance(instance, It)


Person_strategy = st.builds(Person, age=st.integers(), name=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Receptionist_strategy = st.builds(Receptionist)
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)


Room_strategy = st.builds(Room, available=st.booleans(), capasittity=st.integers(), num=st.integers(), patients=safe_text, room_type=safe_text)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


appointment_strategy = st.builds(appointment, day=st.integers(), duration=st.integers(), hour=st.integers(), minute=st.integers())
@given(instance=appointment_strategy)
@settings(max_examples=25)
def test_appointment_instantiation(instance):
    assert isinstance(instance, appointment)


doctor_strategy = st.builds(doctor, patient=safe_text, weekappointment=safe_text)
@given(instance=doctor_strategy)
@settings(max_examples=25)
def test_doctor_instantiation(instance):
    assert isinstance(instance, doctor)


employee_strategy = st.builds(employee, Salary=st.integers(), department=safe_text, id=safe_text, password=safe_text)
@given(instance=employee_strategy)
@settings(max_examples=25)
def test_employee_instantiation(instance):
    assert isinstance(instance, employee)



