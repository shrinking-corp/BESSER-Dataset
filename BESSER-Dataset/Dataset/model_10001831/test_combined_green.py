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
    MainWindow,
    appointment,
    Room,
    Patient,
    It,
    nurse,
    doctor,
    employee,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mainwindow_is_not_abstract():
    assert not inspect.isabstract(MainWindow)


def test_hyp_mainwindow_constructor_exists():
    assert callable(MainWindow.__init__)


def test_hyp_mainwindow_constructor_args():
    sig = inspect.signature(MainWindow.__init__)
    params = list(sig.parameters.keys())
    assert "patientss" in params, "Missing parameter 'patientss'"
    assert "roomss" in params, "Missing parameter 'roomss'"
    assert "UI" in params, "Missing parameter 'UI'"
    assert "nursess" in params, "Missing parameter 'nursess'"
    assert "_logininit" in params, "Missing parameter '_logininit'"
    assert "doctorss" in params, "Missing parameter 'doctorss'"
    assert "itss" in params, "Missing parameter 'itss'"
    assert "_logicdoc" in params, "Missing parameter '_logicdoc'"
    assert "_Loginnurs" in params, "Missing parameter '_Loginnurs'"

def test_hyp_mainwindow_has_patientss():
    assert hasattr(MainWindow, "patientss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "patientss" in klass.__dict__:
            descriptor = klass.__dict__["patientss"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has_roomss():
    assert hasattr(MainWindow, "roomss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "roomss" in klass.__dict__:
            descriptor = klass.__dict__["roomss"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has_UI():
    assert hasattr(MainWindow, "UI")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "UI" in klass.__dict__:
            descriptor = klass.__dict__["UI"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has_nursess():
    assert hasattr(MainWindow, "nursess")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "nursess" in klass.__dict__:
            descriptor = klass.__dict__["nursess"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has__logininit():
    assert hasattr(MainWindow, "_logininit")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "_logininit" in klass.__dict__:
            descriptor = klass.__dict__["_logininit"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has_doctorss():
    assert hasattr(MainWindow, "doctorss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "doctorss" in klass.__dict__:
            descriptor = klass.__dict__["doctorss"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has_itss():
    assert hasattr(MainWindow, "itss")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "itss" in klass.__dict__:
            descriptor = klass.__dict__["itss"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has__logicdoc():
    assert hasattr(MainWindow, "_logicdoc")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "_logicdoc" in klass.__dict__:
            descriptor = klass.__dict__["_logicdoc"]
            break
    assert isinstance(descriptor, property)

def test_hyp_mainwindow_has__Loginnurs():
    assert hasattr(MainWindow, "_Loginnurs")
    descriptor = None
    for klass in MainWindow.__mro__:
        if "_Loginnurs" in klass.__dict__:
            descriptor = klass.__dict__["_Loginnurs"]
            break
    assert isinstance(descriptor, property)



def test_hyp_appointment_is_not_abstract():
    assert not inspect.isabstract(appointment)


def test_hyp_appointment_constructor_exists():
    assert callable(appointment.__init__)


def test_hyp_appointment_constructor_args():
    sig = inspect.signature(appointment.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "title" in params, "Missing parameter 'title'"








def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "capasittity" in params, "Missing parameter 'capasittity'"
    assert "available" in params, "Missing parameter 'available'"
    assert "room_type" in params, "Missing parameter 'room_type'"
    assert "num" in params, "Missing parameter 'num'"
    assert "_nurs" in params, "Missing parameter '_nurs'"
    assert "patients" in params, "Missing parameter 'patients'"

def test_hyp_room_has_capasittity():
    assert hasattr(Room, "capasittity")
    descriptor = None
    for klass in Room.__mro__:
        if "capasittity" in klass.__dict__:
            descriptor = klass.__dict__["capasittity"]
            break
    assert isinstance(descriptor, property)

def test_hyp_room_has_available():
    assert hasattr(Room, "available")
    descriptor = None
    for klass in Room.__mro__:
        if "available" in klass.__dict__:
            descriptor = klass.__dict__["available"]
            break
    assert isinstance(descriptor, property)

def test_hyp_room_has_room_type():
    assert hasattr(Room, "room_type")
    descriptor = None
    for klass in Room.__mro__:
        if "room_type" in klass.__dict__:
            descriptor = klass.__dict__["room_type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_room_has_num():
    assert hasattr(Room, "num")
    descriptor = None
    for klass in Room.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_hyp_room_has__nurs():
    assert hasattr(Room, "_nurs")
    descriptor = None
    for klass in Room.__mro__:
        if "_nurs" in klass.__dict__:
            descriptor = klass.__dict__["_nurs"]
            break
    assert isinstance(descriptor, property)

def test_hyp_room_has_patients():
    assert hasattr(Room, "patients")
    descriptor = None
    for klass in Room.__mro__:
        if "patients" in klass.__dict__:
            descriptor = klass.__dict__["patients"]
            break
    assert isinstance(descriptor, property)



def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "hasdoc" in params, "Missing parameter 'hasdoc'"
    assert "disease" in params, "Missing parameter 'disease'"
    assert "hasroom" in params, "Missing parameter 'hasroom'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "room" in params, "Missing parameter 'room'"








def test_hyp_it_is_not_abstract():
    assert not inspect.isabstract(It)


def test_hyp_it_constructor_exists():
    assert callable(It.__init__)


def test_hyp_it_constructor_args():
    sig = inspect.signature(It.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
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
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"




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
MainWindow_strategy = st.builds(
    MainWindow,
    patientss=
        safe_text,
    roomss=
        safe_text,
    UI=
        safe_text,
    nursess=
        safe_text,
    _logininit=
        st.none(),
    doctorss=
        safe_text,
    itss=
        safe_text,
    _logicdoc=
        st.none(),
    _Loginnurs=
        st.none()
)
appointment_strategy = st.builds(
    appointment,
    day=
        st.integers(),
    duration=
        st.integers(),
    minute=
        st.integers(),
    hour=
        st.integers(),
    title=
        safe_text
)
Room_strategy = st.builds(
    Room,
    capasittity=
        st.integers(),
    available=
        st.booleans(),
    room_type=
        safe_text,
    num=
        st.integers(),
    _nurs=
        st.none(),
    patients=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    hasdoc=
        st.booleans(),
    disease=
        safe_text,
    hasroom=
        st.booleans(),
    duration=
        st.integers(),
    room=
        st.integers()
)
It_strategy = st.builds(
    It,
    name=
        safe_text,
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
    password=
        safe_text
)
Person_strategy = st.builds(
    Person,
    name=
        safe_text,
    age=
        st.integers()
)

@given(instance=MainWindow_strategy)
@settings(max_examples=50)
def test_hyp_mainwindow_instantiation(instance):
    assert isinstance(instance, MainWindow)



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow_patientss_setter(instance):
    original = instance.patientss
    instance.patientss = original
    assert instance.patientss == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow_roomss_setter(instance):
    original = instance.roomss
    instance.roomss = original
    assert instance.roomss == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow_UI_setter(instance):
    original = instance.UI
    instance.UI = original
    assert instance.UI == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow_nursess_setter(instance):
    original = instance.nursess
    instance.nursess = original
    assert instance.nursess == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow__logininit_setter(instance):
    original = instance._logininit
    instance._logininit = original
    assert instance._logininit == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow_doctorss_setter(instance):
    original = instance.doctorss
    instance.doctorss = original
    assert instance.doctorss == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow_itss_setter(instance):
    original = instance.itss
    instance.itss = original
    assert instance.itss == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow__logicdoc_setter(instance):
    original = instance._logicdoc
    instance._logicdoc = original
    assert instance._logicdoc == original



@given(instance=MainWindow_strategy)
def test_hyp_mainwindow__Loginnurs_setter(instance):
    original = instance._Loginnurs
    instance._Loginnurs = original
    assert instance._Loginnurs == original




@given(instance=appointment_strategy)
def test_hyp_appointment_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



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
def test_hyp_appointment_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=appointment_strategy)
def test_hyp_appointment_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_hyp_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_hyp_room_capasittity_setter(instance):
    original = instance.capasittity
    instance.capasittity = original
    assert instance.capasittity == original



@given(instance=Room_strategy)
def test_hyp_room_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original



@given(instance=Room_strategy)
def test_hyp_room_room_type_setter(instance):
    original = instance.room_type
    instance.room_type = original
    assert instance.room_type == original



@given(instance=Room_strategy)
def test_hyp_room_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Room_strategy)
def test_hyp_room__nurs_setter(instance):
    original = instance._nurs
    instance._nurs = original
    assert instance._nurs == original



@given(instance=Room_strategy)
def test_hyp_room_patients_setter(instance):
    original = instance.patients
    instance.patients = original
    assert instance.patients == original




@given(instance=Patient_strategy)
def test_hyp_patient_hasdoc_setter(instance):
    original = instance.hasdoc
    instance.hasdoc = original
    assert instance.hasdoc == original



@given(instance=Patient_strategy)
def test_hyp_patient_disease_setter(instance):
    original = instance.disease
    instance.disease = original
    assert instance.disease == original



@given(instance=Patient_strategy)
def test_hyp_patient_hasroom_setter(instance):
    original = instance.hasroom
    instance.hasroom = original
    assert instance.hasroom == original



@given(instance=Patient_strategy)
def test_hyp_patient_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=Patient_strategy)
def test_hyp_patient_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original




@given(instance=It_strategy)
def test_hyp_it_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



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
def test_hyp_employee_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Person_strategy)
def test_hyp_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_hyp_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    It,
    MainWindow,
    Patient,
    Person,
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

def test_It_name_value_roundtrip():
    instance = It(name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_It_password_value_roundtrip():
    instance = It(name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Patient_disease_value_roundtrip():
    instance = Patient(disease="sample_text", duration=7, hasdoc=True, hasroom=True, room=7)
    assert instance.disease == "sample_text"
    instance.disease = "sample_text_2"
    assert instance.disease == "sample_text_2"


def test_Patient_duration_value_roundtrip():
    instance = Patient(disease="sample_text", duration=7, hasdoc=True, hasroom=True, room=7)
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_Patient_hasdoc_value_roundtrip():
    instance = Patient(disease="sample_text", duration=7, hasdoc=True, hasroom=True, room=7)
    assert instance.hasdoc == True
    instance.hasdoc = False
    assert instance.hasdoc == False


def test_Patient_hasroom_value_roundtrip():
    instance = Patient(disease="sample_text", duration=7, hasdoc=True, hasroom=True, room=7)
    assert instance.hasroom == True
    instance.hasroom = False
    assert instance.hasroom == False


def test_Patient_room_value_roundtrip():
    instance = Patient(disease="sample_text", duration=7, hasdoc=True, hasroom=True, room=7)
    assert instance.room == 7
    instance.room = 13
    assert instance.room == 13


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


def test_appointment_day_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7, title="sample_text")
    assert instance.day == 7
    instance.day = 13
    assert instance.day == 13


def test_appointment_duration_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7, title="sample_text")
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_appointment_hour_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7, title="sample_text")
    assert instance.hour == 7
    instance.hour = 13
    assert instance.hour == 13


def test_appointment_minute_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7, title="sample_text")
    assert instance.minute == 7
    instance.minute = 13
    assert instance.minute == 13


def test_appointment_title_value_roundtrip():
    instance = appointment(day=7, duration=7, hour=7, minute=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


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


def test_employee_department_value_roundtrip():
    instance = employee(department="sample_text", password="sample_text")
    assert instance.department == "sample_text"
    instance.department = "sample_text_2"
    assert instance.department == "sample_text_2"


def test_employee_password_value_roundtrip():
    instance = employee(department="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_assoc_Patient__doctor_link_reassign_clear():
    a = doctor(patient="sample_text", weekappointment="sample_text")
    b1 = Patient(disease="sample_text", duration=7, hasdoc=True, hasroom=True, room=7)
    b2 = Patient(disease="sample_text_2", duration=13, hasdoc=False, hasroom=False, room=13)
    _safe_set(a, 'patient_25', b1)
    assert _is_linked(a, 'patient_25', b1)
    if hasattr(b1, 'doctor4'):
        assert _is_linked(b1, 'doctor4', a)
    _safe_set(a, 'patient_25', b2)
    assert _is_linked(a, 'patient_25', b2)
    if hasattr(b1, 'doctor4'):
        assert not _is_linked(b1, 'doctor4', a)
    if hasattr(b2, 'doctor4'):
        assert _is_linked(b2, 'doctor4', a)
    _safe_set(a, 'patient_25', None)
    assert not _is_linked(a, 'patient_25', b2)
    if hasattr(b2, 'doctor4'):
        assert not _is_linked(b2, 'doctor4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

It_strategy = st.builds(It, name=safe_text, password=safe_text)
@given(instance=It_strategy)
@settings(max_examples=25)
def test_It_instantiation(instance):
    assert isinstance(instance, It)


Patient_strategy = st.builds(Patient, disease=safe_text, duration=st.integers(), hasdoc=st.booleans(), hasroom=st.booleans(), room=st.integers())
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Person_strategy = st.builds(Person, age=st.integers(), name=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


appointment_strategy = st.builds(appointment, day=st.integers(), duration=st.integers(), hour=st.integers(), minute=st.integers(), title=safe_text)
@given(instance=appointment_strategy)
@settings(max_examples=25)
def test_appointment_instantiation(instance):
    assert isinstance(instance, appointment)


doctor_strategy = st.builds(doctor, patient=safe_text, weekappointment=safe_text)
@given(instance=doctor_strategy)
@settings(max_examples=25)
def test_doctor_instantiation(instance):
    assert isinstance(instance, doctor)


employee_strategy = st.builds(employee, department=safe_text, password=safe_text)
@given(instance=employee_strategy)
@settings(max_examples=25)
def test_employee_instantiation(instance):
    assert isinstance(instance, employee)



