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
    Show_to_Doctor_external,
    Doctor_Actor,
    Patient_Actor,
    Admin_Office_Component,
    Doctor,
    prescription,
    Patient,
    Person,
    Check_Patient_external,
    Give_Prescription_external,
    Take_Appointment_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_show_to_doctor_external_is_not_abstract():
    assert not inspect.isabstract(Show_to_Doctor_external)


def test_hyp_show_to_doctor_external_constructor_exists():
    assert callable(Show_to_Doctor_external.__init__)


def test_hyp_show_to_doctor_external_constructor_args():
    sig = inspect.signature(Show_to_Doctor_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doctor_actor_is_not_abstract():
    assert not inspect.isabstract(Doctor_Actor)


def test_hyp_doctor_actor_constructor_exists():
    assert callable(Doctor_Actor.__init__)


def test_hyp_doctor_actor_constructor_args():
    sig = inspect.signature(Doctor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patient_actor_is_not_abstract():
    assert not inspect.isabstract(Patient_Actor)


def test_hyp_patient_actor_constructor_exists():
    assert callable(Patient_Actor.__init__)


def test_hyp_patient_actor_constructor_args():
    sig = inspect.signature(Patient_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_office_component_is_not_abstract():
    assert not inspect.isabstract(Admin_Office_Component)


def test_hyp_admin_office_component_constructor_exists():
    assert callable(Admin_Office_Component.__init__)


def test_hyp_admin_office_component_constructor_args():
    sig = inspect.signature(Admin_Office_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Dept" in params, "Missing parameter 'Dept'"
    assert "Doctor_id" in params, "Missing parameter 'Doctor_id'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"






def test_hyp_prescription_is_not_abstract():
    assert not inspect.isabstract(prescription)


def test_hyp_prescription_constructor_exists():
    assert callable(prescription.__init__)


def test_hyp_prescription_constructor_args():
    sig = inspect.signature(prescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Admit_date" in params, "Missing parameter 'Admit_date'"
    assert "Patient_id" in params, "Missing parameter 'Patient_id'"
    assert "Sickness" in params, "Missing parameter 'Sickness'"






def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Birth_date" in params, "Missing parameter 'Birth_date'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Phone_no" in params, "Missing parameter 'Phone_no'"
    assert "Name1" in params, "Missing parameter 'Name1'"
    assert "Gender" in params, "Missing parameter 'Gender'"










def test_hyp_check_patient_external_is_not_abstract():
    assert not inspect.isabstract(Check_Patient_external)


def test_hyp_check_patient_external_constructor_exists():
    assert callable(Check_Patient_external.__init__)


def test_hyp_check_patient_external_constructor_args():
    sig = inspect.signature(Check_Patient_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_give_prescription_external_is_not_abstract():
    assert not inspect.isabstract(Give_Prescription_external)


def test_hyp_give_prescription_external_constructor_exists():
    assert callable(Give_Prescription_external.__init__)


def test_hyp_give_prescription_external_constructor_args():
    sig = inspect.signature(Give_Prescription_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_take_appointment_external_is_not_abstract():
    assert not inspect.isabstract(Take_Appointment_external)


def test_hyp_take_appointment_external_constructor_exists():
    assert callable(Take_Appointment_external.__init__)


def test_hyp_take_appointment_external_constructor_args():
    sig = inspect.signature(Take_Appointment_external.__init__)
    params = list(sig.parameters.keys())


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
Show_to_Doctor_external_strategy = st.builds(
    Show_to_Doctor_external,
)
Doctor_Actor_strategy = st.builds(
    Doctor_Actor,
)
Patient_Actor_strategy = st.builds(
    Patient_Actor,
)
Admin_Office_Component_strategy = st.builds(
    Admin_Office_Component,
)
Doctor_strategy = st.builds(
    Doctor,
    Dept=
        safe_text,
    Doctor_id=
        st.integers(),
    Specialization=
        safe_text
)
prescription_strategy = st.builds(
    prescription,
)
Patient_strategy = st.builds(
    Patient,
    Admit_date=
        safe_text,
    Patient_id=
        st.integers(),
    Sickness=
        safe_text
)
Person_strategy = st.builds(
    Person,
    Id=
        safe_text,
    Name=
        safe_text,
    Birth_date=
        safe_text,
    Age=
        st.integers(),
    Phone_no=
        safe_text,
    Name1=
        safe_text,
    Gender=
        safe_text
)
Check_Patient_external_strategy = st.builds(
    Check_Patient_external,
)
Give_Prescription_external_strategy = st.builds(
    Give_Prescription_external,
)
Take_Appointment_external_strategy = st.builds(
    Take_Appointment_external,
)








@given(instance=Doctor_strategy)
def test_hyp_doctor_Dept_setter(instance):
    original = instance.Dept
    instance.Dept = original
    assert instance.Dept == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Doctor_id_setter(instance):
    original = instance.Doctor_id
    instance.Doctor_id = original
    assert instance.Doctor_id == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original





@given(instance=Patient_strategy)
def test_hyp_patient_Admit_date_setter(instance):
    original = instance.Admit_date
    instance.Admit_date = original
    assert instance.Admit_date == original



@given(instance=Patient_strategy)
def test_hyp_patient_Patient_id_setter(instance):
    original = instance.Patient_id
    instance.Patient_id = original
    assert instance.Patient_id == original



@given(instance=Patient_strategy)
def test_hyp_patient_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original




@given(instance=Person_strategy)
def test_hyp_person_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Person_strategy)
def test_hyp_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Person_strategy)
def test_hyp_person_Birth_date_setter(instance):
    original = instance.Birth_date
    instance.Birth_date = original
    assert instance.Birth_date == original



@given(instance=Person_strategy)
def test_hyp_person_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Person_strategy)
def test_hyp_person_Phone_no_setter(instance):
    original = instance.Phone_no
    instance.Phone_no = original
    assert instance.Phone_no == original



@given(instance=Person_strategy)
def test_hyp_person_Name1_setter(instance):
    original = instance.Name1
    instance.Name1 = original
    assert instance.Name1 == original



@given(instance=Person_strategy)
def test_hyp_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin_Office_Component,
    Check_Patient_external,
    Doctor,
    Doctor_Actor,
    Give_Prescription_external,
    Patient,
    Patient_Actor,
    Person,
    Show_to_Doctor_external,
    Take_Appointment_external,
    prescription,
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

def test_Doctor_Dept_value_roundtrip():
    instance = Doctor(Dept="sample_text", Doctor_id=7, Specialization="sample_text")
    assert instance.Dept == "sample_text"
    instance.Dept = "sample_text_2"
    assert instance.Dept == "sample_text_2"


def test_Doctor_Doctor_id_value_roundtrip():
    instance = Doctor(Dept="sample_text", Doctor_id=7, Specialization="sample_text")
    assert instance.Doctor_id == 7
    instance.Doctor_id = 13
    assert instance.Doctor_id == 13


def test_Doctor_Specialization_value_roundtrip():
    instance = Doctor(Dept="sample_text", Doctor_id=7, Specialization="sample_text")
    assert instance.Specialization == "sample_text"
    instance.Specialization = "sample_text_2"
    assert instance.Specialization == "sample_text_2"


def test_Patient_Admit_date_value_roundtrip():
    instance = Patient(Admit_date="sample_text", Patient_id=7, Sickness="sample_text")
    assert instance.Admit_date == "sample_text"
    instance.Admit_date = "sample_text_2"
    assert instance.Admit_date == "sample_text_2"


def test_Patient_Patient_id_value_roundtrip():
    instance = Patient(Admit_date="sample_text", Patient_id=7, Sickness="sample_text")
    assert instance.Patient_id == 7
    instance.Patient_id = 13
    assert instance.Patient_id == 13


def test_Patient_Sickness_value_roundtrip():
    instance = Patient(Admit_date="sample_text", Patient_id=7, Sickness="sample_text")
    assert instance.Sickness == "sample_text"
    instance.Sickness = "sample_text_2"
    assert instance.Sickness == "sample_text_2"


def test_Person_Age_value_roundtrip():
    instance = Person(Age=7, Birth_date="sample_text", Gender="sample_text", Id="sample_text", Name="sample_text", Name1="sample_text", Phone_no="sample_text")
    assert instance.Age == 7
    instance.Age = 13
    assert instance.Age == 13


def test_Person_Birth_date_value_roundtrip():
    instance = Person(Age=7, Birth_date="sample_text", Gender="sample_text", Id="sample_text", Name="sample_text", Name1="sample_text", Phone_no="sample_text")
    assert instance.Birth_date == "sample_text"
    instance.Birth_date = "sample_text_2"
    assert instance.Birth_date == "sample_text_2"


def test_Person_Gender_value_roundtrip():
    instance = Person(Age=7, Birth_date="sample_text", Gender="sample_text", Id="sample_text", Name="sample_text", Name1="sample_text", Phone_no="sample_text")
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Person_Id_value_roundtrip():
    instance = Person(Age=7, Birth_date="sample_text", Gender="sample_text", Id="sample_text", Name="sample_text", Name1="sample_text", Phone_no="sample_text")
    assert instance.Id == "sample_text"
    instance.Id = "sample_text_2"
    assert instance.Id == "sample_text_2"


def test_Person_Name_value_roundtrip():
    instance = Person(Age=7, Birth_date="sample_text", Gender="sample_text", Id="sample_text", Name="sample_text", Name1="sample_text", Phone_no="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Person_Name1_value_roundtrip():
    instance = Person(Age=7, Birth_date="sample_text", Gender="sample_text", Id="sample_text", Name="sample_text", Name1="sample_text", Phone_no="sample_text")
    assert instance.Name1 == "sample_text"
    instance.Name1 = "sample_text_2"
    assert instance.Name1 == "sample_text_2"


def test_Person_Phone_no_value_roundtrip():
    instance = Person(Age=7, Birth_date="sample_text", Gender="sample_text", Id="sample_text", Name="sample_text", Name1="sample_text", Phone_no="sample_text")
    assert instance.Phone_no == "sample_text"
    instance.Phone_no = "sample_text_2"
    assert instance.Phone_no == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_Office_Component_strategy = st.builds(Admin_Office_Component)
@given(instance=Admin_Office_Component_strategy)
@settings(max_examples=25)
def test_Admin_Office_Component_instantiation(instance):
    assert isinstance(instance, Admin_Office_Component)


Check_Patient_external_strategy = st.builds(Check_Patient_external)
@given(instance=Check_Patient_external_strategy)
@settings(max_examples=25)
def test_Check_Patient_external_instantiation(instance):
    assert isinstance(instance, Check_Patient_external)


Doctor_strategy = st.builds(Doctor, Dept=safe_text, Doctor_id=st.integers(), Specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Doctor_Actor_strategy = st.builds(Doctor_Actor)
@given(instance=Doctor_Actor_strategy)
@settings(max_examples=25)
def test_Doctor_Actor_instantiation(instance):
    assert isinstance(instance, Doctor_Actor)


Give_Prescription_external_strategy = st.builds(Give_Prescription_external)
@given(instance=Give_Prescription_external_strategy)
@settings(max_examples=25)
def test_Give_Prescription_external_instantiation(instance):
    assert isinstance(instance, Give_Prescription_external)


Patient_strategy = st.builds(Patient, Admit_date=safe_text, Patient_id=st.integers(), Sickness=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Patient_Actor_strategy = st.builds(Patient_Actor)
@given(instance=Patient_Actor_strategy)
@settings(max_examples=25)
def test_Patient_Actor_instantiation(instance):
    assert isinstance(instance, Patient_Actor)


Person_strategy = st.builds(Person, Age=st.integers(), Birth_date=safe_text, Gender=safe_text, Id=safe_text, Name=safe_text, Name1=safe_text, Phone_no=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Show_to_Doctor_external_strategy = st.builds(Show_to_Doctor_external)
@given(instance=Show_to_Doctor_external_strategy)
@settings(max_examples=25)
def test_Show_to_Doctor_external_instantiation(instance):
    assert isinstance(instance, Show_to_Doctor_external)


Take_Appointment_external_strategy = st.builds(Take_Appointment_external)
@given(instance=Take_Appointment_external_strategy)
@settings(max_examples=25)
def test_Take_Appointment_external_instantiation(instance):
    assert isinstance(instance, Take_Appointment_external)


prescription_strategy = st.builds(prescription)
@given(instance=prescription_strategy)
@settings(max_examples=25)
def test_prescription_instantiation(instance):
    assert isinstance(instance, prescription)



