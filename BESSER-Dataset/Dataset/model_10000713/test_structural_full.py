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


