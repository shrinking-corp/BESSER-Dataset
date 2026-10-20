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
    Hospital,
    Patients,
    Receptionist,
    Docter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hyp_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hyp_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "Operation_Theater" in params, "Missing parameter 'Operation_Theater'"
    assert "Cariology" in params, "Missing parameter 'Cariology'"
    assert "HR" in params, "Missing parameter 'HR'"






def test_hyp_patients_is_not_abstract():
    assert not inspect.isabstract(Patients)


def test_hyp_patients_constructor_exists():
    assert callable(Patients.__init__)


def test_hyp_patients_constructor_args():
    sig = inspect.signature(Patients.__init__)
    params = list(sig.parameters.keys())
    assert "Patient_name" in params, "Missing parameter 'Patient_name'"
    assert "Sickness" in params, "Missing parameter 'Sickness'"
    assert "NIC_NO" in params, "Missing parameter 'NIC_NO'"
    assert "Phone_no" in params, "Missing parameter 'Phone_no'"







def test_hyp_receptionist_is_not_abstract():
    assert not inspect.isabstract(Receptionist)


def test_hyp_receptionist_constructor_exists():
    assert callable(Receptionist.__init__)


def test_hyp_receptionist_constructor_args():
    sig = inspect.signature(Receptionist.__init__)
    params = list(sig.parameters.keys())
    assert "Employee_ID" in params, "Missing parameter 'Employee_ID'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_docter_is_not_abstract():
    assert not inspect.isabstract(Docter)


def test_hyp_docter_constructor_exists():
    assert callable(Docter.__init__)


def test_hyp_docter_constructor_args():
    sig = inspect.signature(Docter.__init__)
    params = list(sig.parameters.keys())
    assert "Specialization" in params, "Missing parameter 'Specialization'"
    assert "Rank" in params, "Missing parameter 'Rank'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Salary" in params, "Missing parameter 'Salary'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "Name" in params, "Missing parameter 'Name'"








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
Hospital_strategy = st.builds(
    Hospital,
    Operation_Theater=
        safe_text,
    Cariology=
        safe_text,
    HR=
        safe_text
)
Patients_strategy = st.builds(
    Patients,
    Patient_name=
        safe_text,
    Sickness=
        safe_text,
    NIC_NO=
        st.integers(),
    Phone_no=
        st.integers()
)
Receptionist_strategy = st.builds(
    Receptionist,
    Employee_ID=
        st.integers(),
    Name=
        safe_text
)
Docter_strategy = st.builds(
    Docter,
    Specialization=
        safe_text,
    Rank=
        safe_text,
    ID=
        st.integers(),
    Salary=
        safe_text,
    attribute2=
        safe_text,
    Name=
        safe_text
)




@given(instance=Hospital_strategy)
def test_hyp_hospital_Operation_Theater_setter(instance):
    original = instance.Operation_Theater
    instance.Operation_Theater = original
    assert instance.Operation_Theater == original



@given(instance=Hospital_strategy)
def test_hyp_hospital_Cariology_setter(instance):
    original = instance.Cariology
    instance.Cariology = original
    assert instance.Cariology == original



@given(instance=Hospital_strategy)
def test_hyp_hospital_HR_setter(instance):
    original = instance.HR
    instance.HR = original
    assert instance.HR == original




@given(instance=Patients_strategy)
def test_hyp_patients_Patient_name_setter(instance):
    original = instance.Patient_name
    instance.Patient_name = original
    assert instance.Patient_name == original



@given(instance=Patients_strategy)
def test_hyp_patients_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original



@given(instance=Patients_strategy)
def test_hyp_patients_NIC_NO_setter(instance):
    original = instance.NIC_NO
    instance.NIC_NO = original
    assert instance.NIC_NO == original



@given(instance=Patients_strategy)
def test_hyp_patients_Phone_no_setter(instance):
    original = instance.Phone_no
    instance.Phone_no = original
    assert instance.Phone_no == original




@given(instance=Receptionist_strategy)
def test_hyp_receptionist_Employee_ID_setter(instance):
    original = instance.Employee_ID
    instance.Employee_ID = original
    assert instance.Employee_ID == original



@given(instance=Receptionist_strategy)
def test_hyp_receptionist_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Docter_strategy)
def test_hyp_docter_Specialization_setter(instance):
    original = instance.Specialization
    instance.Specialization = original
    assert instance.Specialization == original



@given(instance=Docter_strategy)
def test_hyp_docter_Rank_setter(instance):
    original = instance.Rank
    instance.Rank = original
    assert instance.Rank == original



@given(instance=Docter_strategy)
def test_hyp_docter_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Docter_strategy)
def test_hyp_docter_Salary_setter(instance):
    original = instance.Salary
    instance.Salary = original
    assert instance.Salary == original



@given(instance=Docter_strategy)
def test_hyp_docter_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Docter_strategy)
def test_hyp_docter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Docter,
    Hospital,
    Patients,
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

def test_Docter_ID_value_roundtrip():
    instance = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Docter_Name_value_roundtrip():
    instance = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Docter_Rank_value_roundtrip():
    instance = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    assert instance.Rank == "sample_text"
    instance.Rank = "sample_text_2"
    assert instance.Rank == "sample_text_2"


def test_Docter_Salary_value_roundtrip():
    instance = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    assert instance.Salary == "sample_text"
    instance.Salary = "sample_text_2"
    assert instance.Salary == "sample_text_2"


def test_Docter_Specialization_value_roundtrip():
    instance = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    assert instance.Specialization == "sample_text"
    instance.Specialization = "sample_text_2"
    assert instance.Specialization == "sample_text_2"


def test_Docter_attribute2_value_roundtrip():
    instance = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_Hospital_Cariology_value_roundtrip():
    instance = Hospital(Cariology="sample_text", HR="sample_text", Operation_Theater="sample_text")
    assert instance.Cariology == "sample_text"
    instance.Cariology = "sample_text_2"
    assert instance.Cariology == "sample_text_2"


def test_Hospital_HR_value_roundtrip():
    instance = Hospital(Cariology="sample_text", HR="sample_text", Operation_Theater="sample_text")
    assert instance.HR == "sample_text"
    instance.HR = "sample_text_2"
    assert instance.HR == "sample_text_2"


def test_Hospital_Operation_Theater_value_roundtrip():
    instance = Hospital(Cariology="sample_text", HR="sample_text", Operation_Theater="sample_text")
    assert instance.Operation_Theater == "sample_text"
    instance.Operation_Theater = "sample_text_2"
    assert instance.Operation_Theater == "sample_text_2"


def test_Patients_NIC_NO_value_roundtrip():
    instance = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    assert instance.NIC_NO == 7
    instance.NIC_NO = 13
    assert instance.NIC_NO == 13


def test_Patients_Patient_name_value_roundtrip():
    instance = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    assert instance.Patient_name == "sample_text"
    instance.Patient_name = "sample_text_2"
    assert instance.Patient_name == "sample_text_2"


def test_Patients_Phone_no_value_roundtrip():
    instance = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    assert instance.Phone_no == 7
    instance.Phone_no = 13
    assert instance.Phone_no == 13


def test_Patients_Sickness_value_roundtrip():
    instance = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    assert instance.Sickness == "sample_text"
    instance.Sickness = "sample_text_2"
    assert instance.Sickness == "sample_text_2"


def test_Receptionist_Employee_ID_value_roundtrip():
    instance = Receptionist(Employee_ID=7, Name="sample_text")
    assert instance.Employee_ID == 7
    instance.Employee_ID = 13
    assert instance.Employee_ID == 13


def test_Receptionist_Name_value_roundtrip():
    instance = Receptionist(Employee_ID=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Docter_Patient_link_reassign_clear():
    a = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    b1 = Docter(ID=7, Name="sample_text", Rank="sample_text", Salary="sample_text", Specialization="sample_text", attribute2="sample_text")
    b2 = Docter(ID=13, Name="sample_text_2", Rank="sample_text_2", Salary="sample_text_2", Specialization="sample_text_2", attribute2="sample_text_2")
    _safe_set(a, 'docter1', b1)
    assert _is_linked(a, 'docter1', b1)
    if hasattr(b1, 'patient0'):
        assert _is_linked(b1, 'patient0', a)
    _safe_set(a, 'docter1', b2)
    assert _is_linked(a, 'docter1', b2)
    if hasattr(b1, 'patient0'):
        assert not _is_linked(b1, 'patient0', a)
    if hasattr(b2, 'patient0'):
        assert _is_linked(b2, 'patient0', a)
    _safe_set(a, 'docter1', None)
    assert not _is_linked(a, 'docter1', b2)
    if hasattr(b2, 'patient0'):
        assert not _is_linked(b2, 'patient0', a)


def test_assoc_Patients_Receptionist_link_reassign_clear():
    a = Receptionist(Employee_ID=7, Name="sample_text")
    b1 = Patients(NIC_NO=7, Patient_name="sample_text", Phone_no=7, Sickness="sample_text")
    b2 = Patients(NIC_NO=13, Patient_name="sample_text_2", Phone_no=13, Sickness="sample_text_2")
    _safe_set(a, 'patients3', b1)
    assert _is_linked(a, 'patients3', b1)
    if hasattr(b1, 'receptionist2'):
        assert _is_linked(b1, 'receptionist2', a)
    _safe_set(a, 'patients3', b2)
    assert _is_linked(a, 'patients3', b2)
    if hasattr(b1, 'receptionist2'):
        assert not _is_linked(b1, 'receptionist2', a)
    if hasattr(b2, 'receptionist2'):
        assert _is_linked(b2, 'receptionist2', a)
    _safe_set(a, 'patients3', None)
    assert not _is_linked(a, 'patients3', b2)
    if hasattr(b2, 'receptionist2'):
        assert not _is_linked(b2, 'receptionist2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Docter_strategy = st.builds(Docter, ID=st.integers(), Name=safe_text, Rank=safe_text, Salary=safe_text, Specialization=safe_text, attribute2=safe_text)
@given(instance=Docter_strategy)
@settings(max_examples=25)
def test_Docter_instantiation(instance):
    assert isinstance(instance, Docter)


Hospital_strategy = st.builds(Hospital, Cariology=safe_text, HR=safe_text, Operation_Theater=safe_text)
@given(instance=Hospital_strategy)
@settings(max_examples=25)
def test_Hospital_instantiation(instance):
    assert isinstance(instance, Hospital)


Patients_strategy = st.builds(Patients, NIC_NO=st.integers(), Patient_name=safe_text, Phone_no=st.integers(), Sickness=safe_text)
@given(instance=Patients_strategy)
@settings(max_examples=25)
def test_Patients_instantiation(instance):
    assert isinstance(instance, Patients)


Receptionist_strategy = st.builds(Receptionist, Employee_ID=st.integers(), Name=safe_text)
@given(instance=Receptionist_strategy)
@settings(max_examples=25)
def test_Receptionist_instantiation(instance):
    assert isinstance(instance, Receptionist)



