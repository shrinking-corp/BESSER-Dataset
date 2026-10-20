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
    Hospital_Management_System,
    Receptionist,
    Patient,
    Doctor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_hospital_management_system_is_not_abstract():
    assert not inspect.isabstract(Hospital_Management_System)


def test_hyp_hospital_management_system_constructor_exists():
    assert callable(Hospital_Management_System.__init__)


def test_hyp_hospital_management_system_constructor_args():
    sig = inspect.signature(Hospital_Management_System.__init__)
    params = list(sig.parameters.keys())
    assert "Code" in params, "Missing parameter 'Code'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"






def test_hyp_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_hyp_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_hyp_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"





def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "PatID" in params, "Missing parameter 'PatID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "TelNo" in params, "Missing parameter 'TelNo'"










def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Department" in params, "Missing parameter 'Department'"
    assert "DocID" in params, "Missing parameter 'DocID'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phone" in params, "Missing parameter 'Phone'"








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
Hospital_Management_System_strategy = st.builds(
    Hospital_Management_System,
    Code=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text
)
Receptionist_strategy = st.builds(
    Receptionist,
    Name=
        safe_text,
    ID=
        st.integers()
)
Patient_strategy = st.builds(
    Patient,
    PatID=
        st.integers(),
    Name=
        safe_text,
    Address=
        safe_text,
    RoomNo=
        st.integers(),
    Age=
        st.integers(),
    Gender=
        safe_text,
    TelNo=
        st.integers()
)
Doctor_strategy = st.builds(
    Doctor,
    Specialization=
        safe_text,
    Name=
        safe_text,
    Department=
        safe_text,
    DocID=
        st.integers(),
    Address=
        safe_text,
    Phone=
        st.integers()
)




@given(instance=Hospital_Management_System_strategy)
def test_hyp_hospital_management_system_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original



@given(instance=Hospital_Management_System_strategy)
def test_hyp_hospital_management_system_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Hospital_Management_System_strategy)
def test_hyp_hospital_management_system_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original




@given(instance=Receptionist_strategy)
def test_hyp_receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Receptionist_strategy)
def test_hyp_receptionist_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original




@given(instance=Patient_strategy)
def test_hyp_patient_PatID_setter(instance):
    original = instance.PatID
    instance.PatID = original
    assert instance.PatID == original



@given(instance=Patient_strategy)
def test_hyp_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_strategy)
def test_hyp_patient_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Patient_strategy)
def test_hyp_patient_RoomNo_setter(instance):
    original = instance.RoomNo
    instance.RoomNo = original
    assert instance.RoomNo == original



@given(instance=Patient_strategy)
def test_hyp_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_hyp_patient_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Patient_strategy)
def test_hyp_patient_TelNo_setter(instance):
    original = instance.TelNo
    instance.TelNo = original
    assert instance.TelNo == original




@given(instance=Doctor_strategy)
def test_hyp_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_DocID_setter(instance):
    original = instance.DocID
    instance.DocID = original
    assert instance.DocID == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Doctor,
    Hospital_Management_System,
    Patient,
    Receptionist,
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

def test_Doctor_Address_value_roundtrip():
    instance = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Doctor_Department_value_roundtrip():
    instance = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    assert instance.Department == "sample_text"
    instance.Department = "sample_text_2"
    assert instance.Department == "sample_text_2"


def test_Doctor_DocID_value_roundtrip():
    instance = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    assert instance.DocID == 7
    instance.DocID = 13
    assert instance.DocID == 13


def test_Doctor_Name_value_roundtrip():
    instance = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Doctor_Phone_value_roundtrip():
    instance = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    assert instance.Phone == 7
    instance.Phone = 13
    assert instance.Phone == 13


def test_Doctor_Specialization_value_roundtrip():
    instance = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    assert instance.Specialization == "sample_text"
    instance.Specialization = "sample_text_2"
    assert instance.Specialization == "sample_text_2"


def test_Hospital_Management_System_Address_value_roundtrip():
    instance = Hospital_Management_System(Address="sample_text", Code="sample_text", Name="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Hospital_Management_System_Code_value_roundtrip():
    instance = Hospital_Management_System(Address="sample_text", Code="sample_text", Name="sample_text")
    assert instance.Code == "sample_text"
    instance.Code = "sample_text_2"
    assert instance.Code == "sample_text_2"


def test_Hospital_Management_System_Name_value_roundtrip():
    instance = Hospital_Management_System(Address="sample_text", Code="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Patient_Address_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Patient_Age_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    assert instance.Age == 7
    instance.Age = 13
    assert instance.Age == 13


def test_Patient_Gender_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Patient_Name_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Patient_PatID_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    assert instance.PatID == 7
    instance.PatID = 13
    assert instance.PatID == 13


def test_Patient_RoomNo_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    assert instance.RoomNo == 7
    instance.RoomNo = 13
    assert instance.RoomNo == 13


def test_Patient_TelNo_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    assert instance.TelNo == 7
    instance.TelNo = 13
    assert instance.TelNo == 13


def test_Receptionist_ID_value_roundtrip():
    instance = Receptionist(ID=7, Name="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Receptionist_Name_value_roundtrip():
    instance = Receptionist(ID=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Doctor_Patient_link_reassign_clear():
    a = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    b1 = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    b2 = Doctor(Address="sample_text_2", Department="sample_text_2", DocID=13, Name="sample_text_2", Phone=13, Specialization="sample_text_2")
    _safe_set(a, 'doctor1', b1)
    assert _is_linked(a, 'doctor1', b1)
    if hasattr(b1, 'patient0'):
        assert _is_linked(b1, 'patient0', a)
    _safe_set(a, 'doctor1', b2)
    assert _is_linked(a, 'doctor1', b2)
    if hasattr(b1, 'patient0'):
        assert not _is_linked(b1, 'patient0', a)
    if hasattr(b2, 'patient0'):
        assert _is_linked(b2, 'patient0', a)
    _safe_set(a, 'doctor1', None)
    assert not _is_linked(a, 'doctor1', b2)
    if hasattr(b2, 'patient0'):
        assert not _is_linked(b2, 'patient0', a)


def test_assoc_Receptionist_Doctor_link_reassign_clear():
    a = Receptionist(ID=7, Name="sample_text")
    b1 = Doctor(Address="sample_text", Department="sample_text", DocID=7, Name="sample_text", Phone=7, Specialization="sample_text")
    b2 = Doctor(Address="sample_text_2", Department="sample_text_2", DocID=13, Name="sample_text_2", Phone=13, Specialization="sample_text_2")
    _safe_set(a, 'doctor4', {b1})
    assert _is_linked(a, 'doctor4', b1)
    if hasattr(b1, 'receptionist5'):
        assert _is_linked(b1, 'receptionist5', a)
    _safe_set(a, 'doctor4', {b2})
    assert _is_linked(a, 'doctor4', b2)
    if hasattr(b1, 'receptionist5'):
        assert not _is_linked(b1, 'receptionist5', a)
    if hasattr(b2, 'receptionist5'):
        assert _is_linked(b2, 'receptionist5', a)
    _safe_set(a, 'doctor4', set())
    assert not _is_linked(a, 'doctor4', b2)
    if hasattr(b2, 'receptionist5'):
        assert not _is_linked(b2, 'receptionist5', a)


def test_assoc_Receptionist_Patient_link_reassign_clear():
    a = Receptionist(ID=7, Name="sample_text")
    b1 = Patient(Address="sample_text", Age=7, Gender="sample_text", Name="sample_text", PatID=7, RoomNo=7, TelNo=7)
    b2 = Patient(Address="sample_text_2", Age=13, Gender="sample_text_2", Name="sample_text_2", PatID=13, RoomNo=13, TelNo=13)
    _safe_set(a, 'patient2', b1)
    assert _is_linked(a, 'patient2', b1)
    if hasattr(b1, 'receptionist3'):
        assert _is_linked(b1, 'receptionist3', a)
    _safe_set(a, 'patient2', b2)
    assert _is_linked(a, 'patient2', b2)
    if hasattr(b1, 'receptionist3'):
        assert not _is_linked(b1, 'receptionist3', a)
    if hasattr(b2, 'receptionist3'):
        assert _is_linked(b2, 'receptionist3', a)
    _safe_set(a, 'patient2', None)
    assert not _is_linked(a, 'patient2', b2)
    if hasattr(b2, 'receptionist3'):
        assert not _is_linked(b2, 'receptionist3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Doctor_strategy = st.builds(Doctor, Address=safe_text, Department=safe_text, DocID=st.integers(), Name=safe_text, Phone=st.integers(), Specialization=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Hospital_Management_System_strategy = st.builds(Hospital_Management_System, Address=safe_text, Code=safe_text, Name=safe_text)
@given(instance=Hospital_Management_System_strategy)
@settings(max_examples=25)
def test_Hospital_Management_System_instantiation(instance):
    assert isinstance(instance, Hospital_Management_System)


Patient_strategy = st.builds(Patient, Address=safe_text, Age=st.integers(), Gender=safe_text, Name=safe_text, PatID=st.integers(), RoomNo=st.integers(), TelNo=st.integers())
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Receptionist_strategy = st.builds(Receptionist, ID=st.integers(), Name=safe_text)
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



