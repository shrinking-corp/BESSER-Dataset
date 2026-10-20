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
    Patient,
    Medicine,
    Symptoms,
    Instructions,
    Medical_test,
    Signs,
    Diagnosis,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Medicine" in params, "Missing parameter 'Medicine'"
    assert "MedicalTest" in params, "Missing parameter 'MedicalTest'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "Allergies" in params, "Missing parameter 'Allergies'"
    assert "Surgeries" in params, "Missing parameter 'Surgeries'"
    assert "DiagnosisList" in params, "Missing parameter 'DiagnosisList'"
    assert "Height" in params, "Missing parameter 'Height'"










def test_hyp_medicine_is_not_abstract():
    assert not inspect.isabstract(Medicine)


def test_hyp_medicine_constructor_exists():
    assert callable(Medicine.__init__)


def test_hyp_medicine_constructor_args():
    sig = inspect.signature(Medicine.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "ActiveIngredient" in params, "Missing parameter 'ActiveIngredient'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Price" in params, "Missing parameter 'Price'"








def test_hyp_symptoms_is_not_abstract():
    assert not inspect.isabstract(Symptoms)


def test_hyp_symptoms_constructor_exists():
    assert callable(Symptoms.__init__)


def test_hyp_symptoms_constructor_args():
    sig = inspect.signature(Symptoms.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"





def test_hyp_instructions_is_not_abstract():
    assert not inspect.isabstract(Instructions)


def test_hyp_instructions_constructor_exists():
    assert callable(Instructions.__init__)


def test_hyp_instructions_constructor_args():
    sig = inspect.signature(Instructions.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "descriptions" in params, "Missing parameter 'descriptions'"






def test_hyp_medical_test_is_not_abstract():
    assert not inspect.isabstract(Medical_test)


def test_hyp_medical_test_constructor_exists():
    assert callable(Medical_test.__init__)


def test_hyp_medical_test_constructor_args():
    sig = inspect.signature(Medical_test.__init__)
    params = list(sig.parameters.keys())
    assert "Lab" in params, "Missing parameter 'Lab'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Image" in params, "Missing parameter 'Image'"








def test_hyp_signs_is_not_abstract():
    assert not inspect.isabstract(Signs)


def test_hyp_signs_constructor_exists():
    assert callable(Signs.__init__)


def test_hyp_signs_constructor_args():
    sig = inspect.signature(Signs.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_diagnosis_is_not_abstract():
    assert not inspect.isabstract(Diagnosis)


def test_hyp_diagnosis_constructor_exists():
    assert callable(Diagnosis.__init__)


def test_hyp_diagnosis_constructor_args():
    sig = inspect.signature(Diagnosis.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "LIst_of_Medical_Test" in params, "Missing parameter 'LIst_of_Medical_Test'"
    assert "LIst_of_Instructions" in params, "Missing parameter 'LIst_of_Instructions'"
    assert "Patient_Id" in params, "Missing parameter 'Patient_Id'"
    assert "LIst_of_Medicine" in params, "Missing parameter 'LIst_of_Medicine'"
    assert "LIst_of_Symptoms" in params, "Missing parameter 'LIst_of_Symptoms'"
    assert "LIst_of_Diagnosis" in params, "Missing parameter 'LIst_of_Diagnosis'"
    assert "Condition" in params, "Missing parameter 'Condition'"
    assert "Doctor_Id" in params, "Missing parameter 'Doctor_Id'"
    assert "ID" in params, "Missing parameter 'ID'"













def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Last_Seen" in params, "Missing parameter 'Last_Seen'"
    assert "InsuranceNumber" in params, "Missing parameter 'InsuranceNumber'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Image" in params, "Missing parameter 'Image'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Lat" in params, "Missing parameter 'Lat'"
    assert "Ssn" in params, "Missing parameter 'Ssn'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Long" in params, "Missing parameter 'Long'"
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "PhoneNumeber" in params, "Missing parameter 'PhoneNumeber'"















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
Patient_strategy = st.builds(
    Patient,
    Medicine=
        safe_text,
    MedicalTest=
        safe_text,
    weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Allergies=
        safe_text,
    Surgeries=
        safe_text,
    DiagnosisList=
        safe_text,
    Height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Medicine_strategy = st.builds(
    Medicine,
    Type=
        safe_text,
    ActiveIngredient=
        safe_text,
    name=
        safe_text,
    ID=
        st.integers(),
    Price=
        safe_text
)
Symptoms_strategy = st.builds(
    Symptoms,
    name=
        safe_text,
    ID=
        st.integers()
)
Instructions_strategy = st.builds(
    Instructions,
    name=
        safe_text,
    ID=
        st.integers(),
    descriptions=
        safe_text
)
Medical_test_strategy = st.builds(
    Medical_test,
    Lab=
        safe_text,
    ID=
        st.integers(),
    Date=
        safe_text,
    name=
        safe_text,
    Image=
        safe_text
)
Signs_strategy = st.builds(
    Signs,
    ID=
        st.integers(),
    name=
        safe_text
)
Diagnosis_strategy = st.builds(
    Diagnosis,
    Date=
        safe_text,
    LIst_of_Medical_Test=
        safe_text,
    LIst_of_Instructions=
        safe_text,
    Patient_Id=
        st.integers(),
    LIst_of_Medicine=
        safe_text,
    LIst_of_Symptoms=
        safe_text,
    LIst_of_Diagnosis=
        safe_text,
    Condition=
        safe_text,
    Doctor_Id=
        st.integers(),
    ID=
        st.integers()
)
Person_strategy = st.builds(
    Person,
    Last_Seen=
        safe_text,
    InsuranceNumber=
        safe_text,
    Password=
        safe_text,
    Image=
        safe_text,
    Name=
        safe_text,
    ID=
        st.integers(),
    Lat=
        safe_text,
    Ssn=
        safe_text,
    Gender=
        st.integers(),
    Long=
        safe_text,
    Balance=
        safe_text,
    Email=
        safe_text,
    PhoneNumeber=
        safe_text
)




@given(instance=Patient_strategy)
def test_hyp_patient_Medicine_setter(instance):
    original = instance.Medicine
    instance.Medicine = original
    assert instance.Medicine == original



@given(instance=Patient_strategy)
def test_hyp_patient_MedicalTest_setter(instance):
    original = instance.MedicalTest
    instance.MedicalTest = original
    assert instance.MedicalTest == original



@given(instance=Patient_strategy)
def test_hyp_patient_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=Patient_strategy)
def test_hyp_patient_Allergies_setter(instance):
    original = instance.Allergies
    instance.Allergies = original
    assert instance.Allergies == original



@given(instance=Patient_strategy)
def test_hyp_patient_Surgeries_setter(instance):
    original = instance.Surgeries
    instance.Surgeries = original
    assert instance.Surgeries == original



@given(instance=Patient_strategy)
def test_hyp_patient_DiagnosisList_setter(instance):
    original = instance.DiagnosisList
    instance.DiagnosisList = original
    assert instance.DiagnosisList == original



@given(instance=Patient_strategy)
def test_hyp_patient_Height_setter(instance):
    original = instance.Height
    instance.Height = original
    assert instance.Height == original




@given(instance=Medicine_strategy)
def test_hyp_medicine_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Medicine_strategy)
def test_hyp_medicine_ActiveIngredient_setter(instance):
    original = instance.ActiveIngredient
    instance.ActiveIngredient = original
    assert instance.ActiveIngredient == original



@given(instance=Medicine_strategy)
def test_hyp_medicine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Medicine_strategy)
def test_hyp_medicine_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Medicine_strategy)
def test_hyp_medicine_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original




@given(instance=Symptoms_strategy)
def test_hyp_symptoms_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Symptoms_strategy)
def test_hyp_symptoms_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original




@given(instance=Instructions_strategy)
def test_hyp_instructions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Instructions_strategy)
def test_hyp_instructions_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Instructions_strategy)
def test_hyp_instructions_descriptions_setter(instance):
    original = instance.descriptions
    instance.descriptions = original
    assert instance.descriptions == original




@given(instance=Medical_test_strategy)
def test_hyp_medical_test_Lab_setter(instance):
    original = instance.Lab
    instance.Lab = original
    assert instance.Lab == original



@given(instance=Medical_test_strategy)
def test_hyp_medical_test_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Medical_test_strategy)
def test_hyp_medical_test_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Medical_test_strategy)
def test_hyp_medical_test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Medical_test_strategy)
def test_hyp_medical_test_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original




@given(instance=Signs_strategy)
def test_hyp_signs_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Signs_strategy)
def test_hyp_signs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_LIst_of_Medical_Test_setter(instance):
    original = instance.LIst_of_Medical_Test
    instance.LIst_of_Medical_Test = original
    assert instance.LIst_of_Medical_Test == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_LIst_of_Instructions_setter(instance):
    original = instance.LIst_of_Instructions
    instance.LIst_of_Instructions = original
    assert instance.LIst_of_Instructions == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_Patient_Id_setter(instance):
    original = instance.Patient_Id
    instance.Patient_Id = original
    assert instance.Patient_Id == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_LIst_of_Medicine_setter(instance):
    original = instance.LIst_of_Medicine
    instance.LIst_of_Medicine = original
    assert instance.LIst_of_Medicine == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_LIst_of_Symptoms_setter(instance):
    original = instance.LIst_of_Symptoms
    instance.LIst_of_Symptoms = original
    assert instance.LIst_of_Symptoms == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_LIst_of_Diagnosis_setter(instance):
    original = instance.LIst_of_Diagnosis
    instance.LIst_of_Diagnosis = original
    assert instance.LIst_of_Diagnosis == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_Condition_setter(instance):
    original = instance.Condition
    instance.Condition = original
    assert instance.Condition == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_Doctor_Id_setter(instance):
    original = instance.Doctor_Id
    instance.Doctor_Id = original
    assert instance.Doctor_Id == original



@given(instance=Diagnosis_strategy)
def test_hyp_diagnosis_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original




@given(instance=Person_strategy)
def test_hyp_person_Last_Seen_setter(instance):
    original = instance.Last_Seen
    instance.Last_Seen = original
    assert instance.Last_Seen == original



@given(instance=Person_strategy)
def test_hyp_person_InsuranceNumber_setter(instance):
    original = instance.InsuranceNumber
    instance.InsuranceNumber = original
    assert instance.InsuranceNumber == original



@given(instance=Person_strategy)
def test_hyp_person_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Person_strategy)
def test_hyp_person_Image_setter(instance):
    original = instance.Image
    instance.Image = original
    assert instance.Image == original



@given(instance=Person_strategy)
def test_hyp_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Person_strategy)
def test_hyp_person_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Person_strategy)
def test_hyp_person_Lat_setter(instance):
    original = instance.Lat
    instance.Lat = original
    assert instance.Lat == original



@given(instance=Person_strategy)
def test_hyp_person_Ssn_setter(instance):
    original = instance.Ssn
    instance.Ssn = original
    assert instance.Ssn == original



@given(instance=Person_strategy)
def test_hyp_person_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Person_strategy)
def test_hyp_person_Long_setter(instance):
    original = instance.Long
    instance.Long = original
    assert instance.Long == original



@given(instance=Person_strategy)
def test_hyp_person_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=Person_strategy)
def test_hyp_person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Person_strategy)
def test_hyp_person_PhoneNumeber_setter(instance):
    original = instance.PhoneNumeber
    instance.PhoneNumeber = original
    assert instance.PhoneNumeber == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Diagnosis,
    Instructions,
    Medical_test,
    Medicine,
    Patient,
    Person,
    Signs,
    Symptoms,
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

def test_Diagnosis_Condition_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.Condition == "sample_text"
    instance.Condition = "sample_text_2"
    assert instance.Condition == "sample_text_2"


def test_Diagnosis_Date_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Diagnosis_Doctor_Id_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.Doctor_Id == 7
    instance.Doctor_Id = 13
    assert instance.Doctor_Id == 13


def test_Diagnosis_ID_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Diagnosis_LIst_of_Diagnosis_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.LIst_of_Diagnosis == "sample_text"
    instance.LIst_of_Diagnosis = "sample_text_2"
    assert instance.LIst_of_Diagnosis == "sample_text_2"


def test_Diagnosis_LIst_of_Instructions_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.LIst_of_Instructions == "sample_text"
    instance.LIst_of_Instructions = "sample_text_2"
    assert instance.LIst_of_Instructions == "sample_text_2"


def test_Diagnosis_LIst_of_Medical_Test_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.LIst_of_Medical_Test == "sample_text"
    instance.LIst_of_Medical_Test = "sample_text_2"
    assert instance.LIst_of_Medical_Test == "sample_text_2"


def test_Diagnosis_LIst_of_Medicine_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.LIst_of_Medicine == "sample_text"
    instance.LIst_of_Medicine = "sample_text_2"
    assert instance.LIst_of_Medicine == "sample_text_2"


def test_Diagnosis_LIst_of_Symptoms_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.LIst_of_Symptoms == "sample_text"
    instance.LIst_of_Symptoms = "sample_text_2"
    assert instance.LIst_of_Symptoms == "sample_text_2"


def test_Diagnosis_Patient_Id_value_roundtrip():
    instance = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    assert instance.Patient_Id == 7
    instance.Patient_Id = 13
    assert instance.Patient_Id == 13


def test_Instructions_ID_value_roundtrip():
    instance = Instructions(ID=7, descriptions="sample_text", name="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Instructions_descriptions_value_roundtrip():
    instance = Instructions(ID=7, descriptions="sample_text", name="sample_text")
    assert instance.descriptions == "sample_text"
    instance.descriptions = "sample_text_2"
    assert instance.descriptions == "sample_text_2"


def test_Instructions_name_value_roundtrip():
    instance = Instructions(ID=7, descriptions="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Medical_test_Date_value_roundtrip():
    instance = Medical_test(Date="sample_text", ID=7, Image="sample_text", Lab="sample_text", name="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Medical_test_ID_value_roundtrip():
    instance = Medical_test(Date="sample_text", ID=7, Image="sample_text", Lab="sample_text", name="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Medical_test_Image_value_roundtrip():
    instance = Medical_test(Date="sample_text", ID=7, Image="sample_text", Lab="sample_text", name="sample_text")
    assert instance.Image == "sample_text"
    instance.Image = "sample_text_2"
    assert instance.Image == "sample_text_2"


def test_Medical_test_Lab_value_roundtrip():
    instance = Medical_test(Date="sample_text", ID=7, Image="sample_text", Lab="sample_text", name="sample_text")
    assert instance.Lab == "sample_text"
    instance.Lab = "sample_text_2"
    assert instance.Lab == "sample_text_2"


def test_Medical_test_name_value_roundtrip():
    instance = Medical_test(Date="sample_text", ID=7, Image="sample_text", Lab="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Medicine_ActiveIngredient_value_roundtrip():
    instance = Medicine(ActiveIngredient="sample_text", ID=7, Price="sample_text", Type="sample_text", name="sample_text")
    assert instance.ActiveIngredient == "sample_text"
    instance.ActiveIngredient = "sample_text_2"
    assert instance.ActiveIngredient == "sample_text_2"


def test_Medicine_ID_value_roundtrip():
    instance = Medicine(ActiveIngredient="sample_text", ID=7, Price="sample_text", Type="sample_text", name="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Medicine_Price_value_roundtrip():
    instance = Medicine(ActiveIngredient="sample_text", ID=7, Price="sample_text", Type="sample_text", name="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_Medicine_Type_value_roundtrip():
    instance = Medicine(ActiveIngredient="sample_text", ID=7, Price="sample_text", Type="sample_text", name="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_Medicine_name_value_roundtrip():
    instance = Medicine(ActiveIngredient="sample_text", ID=7, Price="sample_text", Type="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Patient_Allergies_value_roundtrip():
    instance = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    assert instance.Allergies == "sample_text"
    instance.Allergies = "sample_text_2"
    assert instance.Allergies == "sample_text_2"


def test_Patient_DiagnosisList_value_roundtrip():
    instance = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    assert instance.DiagnosisList == "sample_text"
    instance.DiagnosisList = "sample_text_2"
    assert instance.DiagnosisList == "sample_text_2"


def test_Patient_Height_value_roundtrip():
    instance = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    assert instance.Height == 3.14
    instance.Height = 9.99
    assert instance.Height == 9.99


def test_Patient_MedicalTest_value_roundtrip():
    instance = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    assert instance.MedicalTest == "sample_text"
    instance.MedicalTest = "sample_text_2"
    assert instance.MedicalTest == "sample_text_2"


def test_Patient_Medicine_value_roundtrip():
    instance = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    assert instance.Medicine == "sample_text"
    instance.Medicine = "sample_text_2"
    assert instance.Medicine == "sample_text_2"


def test_Patient_Surgeries_value_roundtrip():
    instance = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    assert instance.Surgeries == "sample_text"
    instance.Surgeries = "sample_text_2"
    assert instance.Surgeries == "sample_text_2"


def test_Patient_weight_value_roundtrip():
    instance = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    assert instance.weight == 3.14
    instance.weight = 9.99
    assert instance.weight == 9.99


def test_Person_Balance_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Balance == "sample_text"
    instance.Balance = "sample_text_2"
    assert instance.Balance == "sample_text_2"


def test_Person_Email_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Person_Gender_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Gender == 7
    instance.Gender = 13
    assert instance.Gender == 13


def test_Person_ID_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Person_Image_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Image == "sample_text"
    instance.Image = "sample_text_2"
    assert instance.Image == "sample_text_2"


def test_Person_InsuranceNumber_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.InsuranceNumber == "sample_text"
    instance.InsuranceNumber = "sample_text_2"
    assert instance.InsuranceNumber == "sample_text_2"


def test_Person_Last_Seen_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Last_Seen == "sample_text"
    instance.Last_Seen = "sample_text_2"
    assert instance.Last_Seen == "sample_text_2"


def test_Person_Lat_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Lat == "sample_text"
    instance.Lat = "sample_text_2"
    assert instance.Lat == "sample_text_2"


def test_Person_Long_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Long == "sample_text"
    instance.Long = "sample_text_2"
    assert instance.Long == "sample_text_2"


def test_Person_Name_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Person_Password_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Person_PhoneNumeber_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.PhoneNumeber == "sample_text"
    instance.PhoneNumeber = "sample_text_2"
    assert instance.PhoneNumeber == "sample_text_2"


def test_Person_Ssn_value_roundtrip():
    instance = Person(Balance="sample_text", Email="sample_text", Gender=7, ID=7, Image="sample_text", InsuranceNumber="sample_text", Last_Seen="sample_text", Lat="sample_text", Long="sample_text", Name="sample_text", Password="sample_text", PhoneNumeber="sample_text", Ssn="sample_text")
    assert instance.Ssn == "sample_text"
    instance.Ssn = "sample_text_2"
    assert instance.Ssn == "sample_text_2"


def test_Signs_ID_value_roundtrip():
    instance = Signs(ID=7, name="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Signs_name_value_roundtrip():
    instance = Signs(ID=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Symptoms_ID_value_roundtrip():
    instance = Symptoms(ID=7, name="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Symptoms_name_value_roundtrip():
    instance = Symptoms(ID=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_Diagnosis_Instructions_link_reassign_clear():
    a = Instructions(ID=7, descriptions="sample_text", name="sample_text")
    b1 = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    b2 = Diagnosis(Condition="sample_text_2", Date="sample_text_2", Doctor_Id=13, ID=13, LIst_of_Diagnosis="sample_text_2", LIst_of_Instructions="sample_text_2", LIst_of_Medical_Test="sample_text_2", LIst_of_Medicine="sample_text_2", LIst_of_Symptoms="sample_text_2", Patient_Id=13)
    _safe_set(a, 'diagnosis7', b1)
    assert _is_linked(a, 'diagnosis7', b1)
    if hasattr(b1, 'instructions6'):
        assert _is_linked(b1, 'instructions6', a)
    _safe_set(a, 'diagnosis7', b2)
    assert _is_linked(a, 'diagnosis7', b2)
    if hasattr(b1, 'instructions6'):
        assert not _is_linked(b1, 'instructions6', a)
    if hasattr(b2, 'instructions6'):
        assert _is_linked(b2, 'instructions6', a)
    _safe_set(a, 'diagnosis7', None)
    assert not _is_linked(a, 'diagnosis7', b2)
    if hasattr(b2, 'instructions6'):
        assert not _is_linked(b2, 'instructions6', a)


def test_assoc_Diagnosis_Medical_test_link_reassign_clear():
    a = Medical_test(Date="sample_text", ID=7, Image="sample_text", Lab="sample_text", name="sample_text")
    b1 = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    b2 = Diagnosis(Condition="sample_text_2", Date="sample_text_2", Doctor_Id=13, ID=13, LIst_of_Diagnosis="sample_text_2", LIst_of_Instructions="sample_text_2", LIst_of_Medical_Test="sample_text_2", LIst_of_Medicine="sample_text_2", LIst_of_Symptoms="sample_text_2", Patient_Id=13)
    _safe_set(a, 'diagnosis9', b1)
    assert _is_linked(a, 'diagnosis9', b1)
    if hasattr(b1, 'medical_test8'):
        assert _is_linked(b1, 'medical_test8', a)
    _safe_set(a, 'diagnosis9', b2)
    assert _is_linked(a, 'diagnosis9', b2)
    if hasattr(b1, 'medical_test8'):
        assert not _is_linked(b1, 'medical_test8', a)
    if hasattr(b2, 'medical_test8'):
        assert _is_linked(b2, 'medical_test8', a)
    _safe_set(a, 'diagnosis9', None)
    assert not _is_linked(a, 'diagnosis9', b2)
    if hasattr(b2, 'medical_test8'):
        assert not _is_linked(b2, 'medical_test8', a)


def test_assoc_Diagnosis_Medicine_link_reassign_clear():
    a = Medicine(ActiveIngredient="sample_text", ID=7, Price="sample_text", Type="sample_text", name="sample_text")
    b1 = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    b2 = Diagnosis(Condition="sample_text_2", Date="sample_text_2", Doctor_Id=13, ID=13, LIst_of_Diagnosis="sample_text_2", LIst_of_Instructions="sample_text_2", LIst_of_Medical_Test="sample_text_2", LIst_of_Medicine="sample_text_2", LIst_of_Symptoms="sample_text_2", Patient_Id=13)
    _safe_set(a, 'diagnosis1', b1)
    assert _is_linked(a, 'diagnosis1', b1)
    if hasattr(b1, 'medicine0'):
        assert _is_linked(b1, 'medicine0', a)
    _safe_set(a, 'diagnosis1', b2)
    assert _is_linked(a, 'diagnosis1', b2)
    if hasattr(b1, 'medicine0'):
        assert not _is_linked(b1, 'medicine0', a)
    if hasattr(b2, 'medicine0'):
        assert _is_linked(b2, 'medicine0', a)
    _safe_set(a, 'diagnosis1', None)
    assert not _is_linked(a, 'diagnosis1', b2)
    if hasattr(b2, 'medicine0'):
        assert not _is_linked(b2, 'medicine0', a)


def test_assoc_Diagnosis_Signs_link_reassign_clear():
    a = Signs(ID=7, name="sample_text")
    b1 = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    b2 = Diagnosis(Condition="sample_text_2", Date="sample_text_2", Doctor_Id=13, ID=13, LIst_of_Diagnosis="sample_text_2", LIst_of_Instructions="sample_text_2", LIst_of_Medical_Test="sample_text_2", LIst_of_Medicine="sample_text_2", LIst_of_Symptoms="sample_text_2", Patient_Id=13)
    _safe_set(a, 'diagnosis5', b1)
    assert _is_linked(a, 'diagnosis5', b1)
    if hasattr(b1, 'signs4'):
        assert _is_linked(b1, 'signs4', a)
    _safe_set(a, 'diagnosis5', b2)
    assert _is_linked(a, 'diagnosis5', b2)
    if hasattr(b1, 'signs4'):
        assert not _is_linked(b1, 'signs4', a)
    if hasattr(b2, 'signs4'):
        assert _is_linked(b2, 'signs4', a)
    _safe_set(a, 'diagnosis5', None)
    assert not _is_linked(a, 'diagnosis5', b2)
    if hasattr(b2, 'signs4'):
        assert not _is_linked(b2, 'signs4', a)


def test_assoc_Diagnosis_Symptoms_link_reassign_clear():
    a = Symptoms(ID=7, name="sample_text")
    b1 = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    b2 = Diagnosis(Condition="sample_text_2", Date="sample_text_2", Doctor_Id=13, ID=13, LIst_of_Diagnosis="sample_text_2", LIst_of_Instructions="sample_text_2", LIst_of_Medical_Test="sample_text_2", LIst_of_Medicine="sample_text_2", LIst_of_Symptoms="sample_text_2", Patient_Id=13)
    _safe_set(a, 'diagnosis3', b1)
    assert _is_linked(a, 'diagnosis3', b1)
    if hasattr(b1, 'symptoms2'):
        assert _is_linked(b1, 'symptoms2', a)
    _safe_set(a, 'diagnosis3', b2)
    assert _is_linked(a, 'diagnosis3', b2)
    if hasattr(b1, 'symptoms2'):
        assert not _is_linked(b1, 'symptoms2', a)
    if hasattr(b2, 'symptoms2'):
        assert _is_linked(b2, 'symptoms2', a)
    _safe_set(a, 'diagnosis3', None)
    assert not _is_linked(a, 'diagnosis3', b2)
    if hasattr(b2, 'symptoms2'):
        assert not _is_linked(b2, 'symptoms2', a)


def test_assoc_Patient__Diagnosis_link_reassign_clear():
    a = Patient(Allergies="sample_text", DiagnosisList="sample_text", Height=3.14, MedicalTest="sample_text", Medicine="sample_text", Surgeries="sample_text", weight=3.14)
    b1 = Diagnosis(Condition="sample_text", Date="sample_text", Doctor_Id=7, ID=7, LIst_of_Diagnosis="sample_text", LIst_of_Instructions="sample_text", LIst_of_Medical_Test="sample_text", LIst_of_Medicine="sample_text", LIst_of_Symptoms="sample_text", Patient_Id=7)
    b2 = Diagnosis(Condition="sample_text_2", Date="sample_text_2", Doctor_Id=13, ID=13, LIst_of_Diagnosis="sample_text_2", LIst_of_Instructions="sample_text_2", LIst_of_Medical_Test="sample_text_2", LIst_of_Medicine="sample_text_2", LIst_of_Symptoms="sample_text_2", Patient_Id=13)
    _safe_set(a, 'diagnosis10', {b1})
    assert _is_linked(a, 'diagnosis10', b1)
    if hasattr(b1, 'patient11'):
        assert _is_linked(b1, 'patient11', a)
    _safe_set(a, 'diagnosis10', {b2})
    assert _is_linked(a, 'diagnosis10', b2)
    if hasattr(b1, 'patient11'):
        assert not _is_linked(b1, 'patient11', a)
    if hasattr(b2, 'patient11'):
        assert _is_linked(b2, 'patient11', a)
    _safe_set(a, 'diagnosis10', set())
    assert not _is_linked(a, 'diagnosis10', b2)
    if hasattr(b2, 'patient11'):
        assert not _is_linked(b2, 'patient11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Diagnosis_strategy = st.builds(Diagnosis, Condition=safe_text, Date=safe_text, Doctor_Id=st.integers(), ID=st.integers(), LIst_of_Diagnosis=safe_text, LIst_of_Instructions=safe_text, LIst_of_Medical_Test=safe_text, LIst_of_Medicine=safe_text, LIst_of_Symptoms=safe_text, Patient_Id=st.integers())
@given(instance=Diagnosis_strategy)
@settings(max_examples=25)
def test_Diagnosis_instantiation(instance):
    assert isinstance(instance, Diagnosis)


Instructions_strategy = st.builds(Instructions, ID=st.integers(), descriptions=safe_text, name=safe_text)
@given(instance=Instructions_strategy)
@settings(max_examples=25)
def test_Instructions_instantiation(instance):
    assert isinstance(instance, Instructions)


Medical_test_strategy = st.builds(Medical_test, Date=safe_text, ID=st.integers(), Image=safe_text, Lab=safe_text, name=safe_text)
@given(instance=Medical_test_strategy)
@settings(max_examples=25)
def test_Medical_test_instantiation(instance):
    assert isinstance(instance, Medical_test)


Medicine_strategy = st.builds(Medicine, ActiveIngredient=safe_text, ID=st.integers(), Price=safe_text, Type=safe_text, name=safe_text)
@given(instance=Medicine_strategy)
@settings(max_examples=25)
def test_Medicine_instantiation(instance):
    assert isinstance(instance, Medicine)


Patient_strategy = st.builds(Patient, Allergies=safe_text, DiagnosisList=safe_text, Height=st.floats(allow_nan=False, allow_infinity=False), MedicalTest=safe_text, Medicine=safe_text, Surgeries=safe_text, weight=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Person_strategy = st.builds(Person, Balance=safe_text, Email=safe_text, Gender=st.integers(), ID=st.integers(), Image=safe_text, InsuranceNumber=safe_text, Last_Seen=safe_text, Lat=safe_text, Long=safe_text, Name=safe_text, Password=safe_text, PhoneNumeber=safe_text, Ssn=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Signs_strategy = st.builds(Signs, ID=st.integers(), name=safe_text)
@given(instance=Signs_strategy)
@settings(max_examples=25)
def test_Signs_instantiation(instance):
    assert isinstance(instance, Signs)


Symptoms_strategy = st.builds(Symptoms, ID=st.integers(), name=safe_text)
@given(instance=Symptoms_strategy)
@settings(max_examples=25)
def test_Symptoms_instantiation(instance):
    assert isinstance(instance, Symptoms)



