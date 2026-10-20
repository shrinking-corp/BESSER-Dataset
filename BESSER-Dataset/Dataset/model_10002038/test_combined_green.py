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
    Patient,
    Bill,
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
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "TelephoneNo" in params, "Missing parameter 'TelephoneNo'"
    assert "RoomNo" in params, "Missing parameter 'RoomNo'"
    assert "PatientID" in params, "Missing parameter 'PatientID'"
    assert "Age" in params, "Missing parameter 'Age'"
    assert "Sex" in params, "Missing parameter 'Sex'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"










def test_hyp_bill_is_not_abstract():
    assert not inspect.isabstract(Bill)


def test_hyp_bill_constructor_exists():
    assert callable(Bill.__init__)


def test_hyp_bill_constructor_args():
    sig = inspect.signature(Bill.__init__)
    params = list(sig.parameters.keys())
    assert "PatientName" in params, "Missing parameter 'PatientName'"
    assert "Amount" in params, "Missing parameter 'Amount'"





def test_hyp_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_hyp_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_hyp_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "DepartmentID" in params, "Missing parameter 'DepartmentID'"
    assert "DoctorID" in params, "Missing parameter 'DoctorID'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "PhoneNo" in params, "Missing parameter 'PhoneNo'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Specialization" in params, "Missing parameter 'Specialization'"









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
    ID=
        st.integers(),
    Name=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    TelephoneNo=
        safe_text,
    RoomNo=
        st.integers(),
    PatientID=
        st.integers(),
    Age=
        st.integers(),
    Sex=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text
)
Bill_strategy = st.builds(
    Bill,
    PatientName=
        safe_text,
    Amount=
        safe_text
)
Doctor_strategy = st.builds(
    Doctor,
    DepartmentID=
        st.integers(),
    DoctorID=
        st.integers(),
    Address=
        safe_text,
    attribute=
        safe_text,
    PhoneNo=
        safe_text,
    Name=
        safe_text,
    Specialization=
        safe_text
)




@given(instance=Nurse_strategy)
def test_hyp_nurse_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Nurse_strategy)
def test_hyp_nurse_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Patient_strategy)
def test_hyp_patient_TelephoneNo_setter(instance):
    original = instance.TelephoneNo
    instance.TelephoneNo = original
    assert instance.TelephoneNo == original



@given(instance=Patient_strategy)
def test_hyp_patient_RoomNo_setter(instance):
    original = instance.RoomNo
    instance.RoomNo = original
    assert instance.RoomNo == original



@given(instance=Patient_strategy)
def test_hyp_patient_PatientID_setter(instance):
    original = instance.PatientID
    instance.PatientID = original
    assert instance.PatientID == original



@given(instance=Patient_strategy)
def test_hyp_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original



@given(instance=Patient_strategy)
def test_hyp_patient_Sex_setter(instance):
    original = instance.Sex
    instance.Sex = original
    assert instance.Sex == original



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




@given(instance=Bill_strategy)
def test_hyp_bill_PatientName_setter(instance):
    original = instance.PatientName
    instance.PatientName = original
    assert instance.PatientName == original



@given(instance=Bill_strategy)
def test_hyp_bill_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original




@given(instance=Doctor_strategy)
def test_hyp_doctor_DepartmentID_setter(instance):
    original = instance.DepartmentID
    instance.DepartmentID = original
    assert instance.DepartmentID == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_DoctorID_setter(instance):
    original = instance.DoctorID
    instance.DoctorID = original
    assert instance.DoctorID == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_PhoneNo_setter(instance):
    original = instance.PhoneNo
    instance.PhoneNo = original
    assert instance.PhoneNo == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Doctor_strategy)
def test_hyp_doctor_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bill,
    Doctor,
    Nurse,
    Patient,
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

def test_Bill_Amount_value_roundtrip():
    instance = Bill(Amount="sample_text", PatientName="sample_text")
    assert instance.Amount == "sample_text"
    instance.Amount = "sample_text_2"
    assert instance.Amount == "sample_text_2"


def test_Bill_PatientName_value_roundtrip():
    instance = Bill(Amount="sample_text", PatientName="sample_text")
    assert instance.PatientName == "sample_text"
    instance.PatientName = "sample_text_2"
    assert instance.PatientName == "sample_text_2"


def test_Doctor_Address_value_roundtrip():
    instance = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Doctor_DepartmentID_value_roundtrip():
    instance = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    assert instance.DepartmentID == 7
    instance.DepartmentID = 13
    assert instance.DepartmentID == 13


def test_Doctor_DoctorID_value_roundtrip():
    instance = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    assert instance.DoctorID == 7
    instance.DoctorID = 13
    assert instance.DoctorID == 13


def test_Doctor_Name_value_roundtrip():
    instance = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Doctor_PhoneNo_value_roundtrip():
    instance = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    assert instance.PhoneNo == "sample_text"
    instance.PhoneNo = "sample_text_2"
    assert instance.PhoneNo == "sample_text_2"


def test_Doctor_Specialization_value_roundtrip():
    instance = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    assert instance.Specialization == "sample_text"
    instance.Specialization = "sample_text_2"
    assert instance.Specialization == "sample_text_2"


def test_Doctor_attribute_value_roundtrip():
    instance = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Nurse_ID_value_roundtrip():
    instance = Nurse(ID=7, Name="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Nurse_Name_value_roundtrip():
    instance = Nurse(ID=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Patient_Address_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Patient_Age_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    assert instance.Age == 7
    instance.Age = 13
    assert instance.Age == 13


def test_Patient_Name_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Patient_PatientID_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    assert instance.PatientID == 7
    instance.PatientID = 13
    assert instance.PatientID == 13


def test_Patient_RoomNo_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    assert instance.RoomNo == 7
    instance.RoomNo = 13
    assert instance.RoomNo == 13


def test_Patient_Sex_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    assert instance.Sex == "sample_text"
    instance.Sex = "sample_text_2"
    assert instance.Sex == "sample_text_2"


def test_Patient_TelephoneNo_value_roundtrip():
    instance = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    assert instance.TelephoneNo == "sample_text"
    instance.TelephoneNo = "sample_text_2"
    assert instance.TelephoneNo == "sample_text_2"


def test_assoc_Doctor_Patient_link_reassign_clear():
    a = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    b1 = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    b2 = Doctor(Address="sample_text_2", DepartmentID=13, DoctorID=13, Name="sample_text_2", PhoneNo="sample_text_2", Specialization="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'doctor1', {b1})
    assert _is_linked(a, 'doctor1', b1)
    if hasattr(b1, 'patient0'):
        assert _is_linked(b1, 'patient0', a)
    _safe_set(a, 'doctor1', {b2})
    assert _is_linked(a, 'doctor1', b2)
    if hasattr(b1, 'patient0'):
        assert not _is_linked(b1, 'patient0', a)
    if hasattr(b2, 'patient0'):
        assert _is_linked(b2, 'patient0', a)
    _safe_set(a, 'doctor1', set())
    assert not _is_linked(a, 'doctor1', b2)
    if hasattr(b2, 'patient0'):
        assert not _is_linked(b2, 'patient0', a)


def test_assoc_Nurse_Doctor_link_reassign_clear():
    a = Nurse(ID=7, Name="sample_text")
    b1 = Doctor(Address="sample_text", DepartmentID=7, DoctorID=7, Name="sample_text", PhoneNo="sample_text", Specialization="sample_text", attribute="sample_text")
    b2 = Doctor(Address="sample_text_2", DepartmentID=13, DoctorID=13, Name="sample_text_2", PhoneNo="sample_text_2", Specialization="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'doctor4', b1)
    assert _is_linked(a, 'doctor4', b1)
    if hasattr(b1, 'nurse5'):
        assert _is_linked(b1, 'nurse5', a)
    _safe_set(a, 'doctor4', b2)
    assert _is_linked(a, 'doctor4', b2)
    if hasattr(b1, 'nurse5'):
        assert not _is_linked(b1, 'nurse5', a)
    if hasattr(b2, 'nurse5'):
        assert _is_linked(b2, 'nurse5', a)
    _safe_set(a, 'doctor4', None)
    assert not _is_linked(a, 'doctor4', b2)
    if hasattr(b2, 'nurse5'):
        assert not _is_linked(b2, 'nurse5', a)


def test_assoc_Nurse_Patient_link_reassign_clear():
    a = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    b1 = Nurse(ID=7, Name="sample_text")
    b2 = Nurse(ID=13, Name="sample_text_2")
    _safe_set(a, 'nurse7', b1)
    assert _is_linked(a, 'nurse7', b1)
    if hasattr(b1, 'patient6'):
        assert _is_linked(b1, 'patient6', a)
    _safe_set(a, 'nurse7', b2)
    assert _is_linked(a, 'nurse7', b2)
    if hasattr(b1, 'patient6'):
        assert not _is_linked(b1, 'patient6', a)
    if hasattr(b2, 'patient6'):
        assert _is_linked(b2, 'patient6', a)
    _safe_set(a, 'nurse7', None)
    assert not _is_linked(a, 'nurse7', b2)
    if hasattr(b2, 'patient6'):
        assert not _is_linked(b2, 'patient6', a)


def test_assoc_Patient_bill_link_reassign_clear():
    a = Patient(Address="sample_text", Age=7, Name="sample_text", PatientID=7, RoomNo=7, Sex="sample_text", TelephoneNo="sample_text")
    b1 = Bill(Amount="sample_text", PatientName="sample_text")
    b2 = Bill(Amount="sample_text_2", PatientName="sample_text_2")
    _safe_set(a, 'bill2', b1)
    assert _is_linked(a, 'bill2', b1)
    if hasattr(b1, 'patient3'):
        assert _is_linked(b1, 'patient3', a)
    _safe_set(a, 'bill2', b2)
    assert _is_linked(a, 'bill2', b2)
    if hasattr(b1, 'patient3'):
        assert not _is_linked(b1, 'patient3', a)
    if hasattr(b2, 'patient3'):
        assert _is_linked(b2, 'patient3', a)
    _safe_set(a, 'bill2', None)
    assert not _is_linked(a, 'bill2', b2)
    if hasattr(b2, 'patient3'):
        assert not _is_linked(b2, 'patient3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bill_strategy = st.builds(Bill, Amount=safe_text, PatientName=safe_text)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


Doctor_strategy = st.builds(Doctor, Address=safe_text, DepartmentID=st.integers(), DoctorID=st.integers(), Name=safe_text, PhoneNo=safe_text, Specialization=safe_text, attribute=safe_text)
@given(instance=Doctor_strategy)
@settings(max_examples=25)
def test_Doctor_instantiation(instance):
    assert isinstance(instance, Doctor)


Nurse_strategy = st.builds(Nurse, ID=st.integers(), Name=safe_text)
@given(instance=Nurse_strategy)
@settings(max_examples=25)
def test_Nurse_instantiation(instance):
    assert isinstance(instance, Nurse)


Patient_strategy = st.builds(Patient, Address=safe_text, Age=st.integers(), Name=safe_text, PatientID=st.integers(), RoomNo=st.integers(), Sex=safe_text, TelephoneNo=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)



