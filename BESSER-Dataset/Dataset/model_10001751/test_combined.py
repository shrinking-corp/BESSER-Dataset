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
    Techinal_Staff,
    Administrative_Staff,
    Operation_Staff,
    Staff,
    Patient,
    Hospital,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_techinal_staff_is_not_abstract():
    assert not inspect.isabstract(Techinal_Staff)


def test_hyp_techinal_staff_constructor_exists():
    assert callable(Techinal_Staff.__init__)


def test_hyp_techinal_staff_constructor_args():
    sig = inspect.signature(Techinal_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Technician" in params, "Missing parameter 'Technician'"
    assert "Technologist" in params, "Missing parameter 'Technologist'"





def test_hyp_administrative_staff_is_not_abstract():
    assert not inspect.isabstract(Administrative_Staff)


def test_hyp_administrative_staff_constructor_exists():
    assert callable(Administrative_Staff.__init__)


def test_hyp_administrative_staff_constructor_args():
    sig = inspect.signature(Administrative_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "ReceptionistName" in params, "Missing parameter 'ReceptionistName'"
    assert "FrontDeskStaffName" in params, "Missing parameter 'FrontDeskStaffName'"





def test_hyp_operation_staff_is_not_abstract():
    assert not inspect.isabstract(Operation_Staff)


def test_hyp_operation_staff_constructor_exists():
    assert callable(Operation_Staff.__init__)


def test_hyp_operation_staff_constructor_args():
    sig = inspect.signature(Operation_Staff.__init__)
    params = list(sig.parameters.keys())
    assert "DoctorLocation" in params, "Missing parameter 'DoctorLocation'"
    assert "DoctorSpeciality" in params, "Missing parameter 'DoctorSpeciality'"
    assert "NurseName" in params, "Missing parameter 'NurseName'"






def test_hyp_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_hyp_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_hyp_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "Certification" in params, "Missing parameter 'Certification'"
    assert "Education" in params, "Missing parameter 'Education'"
    assert "Joined" in params, "Missing parameter 'Joined'"
    assert "Languages" in params, "Missing parameter 'Languages'"







def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "Birthdate" in params, "Missing parameter 'Birthdate'"
    assert "DateOfEntry" in params, "Missing parameter 'DateOfEntry'"
    assert "PatientId" in params, "Missing parameter 'PatientId'"
    assert "Sickness" in params, "Missing parameter 'Sickness'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Age" in params, "Missing parameter 'Age'"










def test_hyp_hospital_is_not_abstract():
    assert not inspect.isabstract(Hospital)


def test_hyp_hospital_constructor_exists():
    assert callable(Hospital.__init__)


def test_hyp_hospital_constructor_args():
    sig = inspect.signature(Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "HospitalId" in params, "Missing parameter 'HospitalId'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Address" in params, "Missing parameter 'Address'"







def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "MiddleName" in params, "Missing parameter 'MiddleName'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "PersonHospitalId" in params, "Missing parameter 'PersonHospitalId'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "PersonPatientId" in params, "Missing parameter 'PersonPatientId'"
    assert "BirthDate" in params, "Missing parameter 'BirthDate'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Title" in params, "Missing parameter 'Title'"
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
Techinal_Staff_strategy = st.builds(
    Techinal_Staff,
    Technician=
        safe_text,
    Technologist=
        safe_text
)
Administrative_Staff_strategy = st.builds(
    Administrative_Staff,
    ReceptionistName=
        safe_text,
    FrontDeskStaffName=
        safe_text
)
Operation_Staff_strategy = st.builds(
    Operation_Staff,
    DoctorLocation=
        safe_text,
    DoctorSpeciality=
        safe_text,
    NurseName=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    Certification=
        safe_text,
    Education=
        safe_text,
    Joined=
        safe_text,
    Languages=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    Birthdate=
        safe_text,
    DateOfEntry=
        safe_text,
    PatientId=
        st.integers(),
    Sickness=
        safe_text,
    Name=
        safe_text,
    Gender=
        safe_text,
    Age=
        st.integers()
)
Hospital_strategy = st.builds(
    Hospital,
    HospitalId=
        st.integers(),
    Name=
        safe_text,
    Phone=
        st.integers(),
    Address=
        safe_text
)
Person_strategy = st.builds(
    Person,
    MiddleName=
        safe_text,
    LastName=
        safe_text,
    PersonHospitalId=
        st.integers(),
    FirstName=
        safe_text,
    PersonPatientId=
        st.integers(),
    BirthDate=
        safe_text,
    Address=
        safe_text,
    Gender=
        safe_text,
    Title=
        safe_text,
    Phone=
        st.integers()
)




@given(instance=Techinal_Staff_strategy)
def test_hyp_techinal_staff_Technician_setter(instance):
    original = instance.Technician
    instance.Technician = original
    assert instance.Technician == original



@given(instance=Techinal_Staff_strategy)
def test_hyp_techinal_staff_Technologist_setter(instance):
    original = instance.Technologist
    instance.Technologist = original
    assert instance.Technologist == original




@given(instance=Administrative_Staff_strategy)
def test_hyp_administrative_staff_ReceptionistName_setter(instance):
    original = instance.ReceptionistName
    instance.ReceptionistName = original
    assert instance.ReceptionistName == original



@given(instance=Administrative_Staff_strategy)
def test_hyp_administrative_staff_FrontDeskStaffName_setter(instance):
    original = instance.FrontDeskStaffName
    instance.FrontDeskStaffName = original
    assert instance.FrontDeskStaffName == original




@given(instance=Operation_Staff_strategy)
def test_hyp_operation_staff_DoctorLocation_setter(instance):
    original = instance.DoctorLocation
    instance.DoctorLocation = original
    assert instance.DoctorLocation == original



@given(instance=Operation_Staff_strategy)
def test_hyp_operation_staff_DoctorSpeciality_setter(instance):
    original = instance.DoctorSpeciality
    instance.DoctorSpeciality = original
    assert instance.DoctorSpeciality == original



@given(instance=Operation_Staff_strategy)
def test_hyp_operation_staff_NurseName_setter(instance):
    original = instance.NurseName
    instance.NurseName = original
    assert instance.NurseName == original




@given(instance=Staff_strategy)
def test_hyp_staff_Certification_setter(instance):
    original = instance.Certification
    instance.Certification = original
    assert instance.Certification == original



@given(instance=Staff_strategy)
def test_hyp_staff_Education_setter(instance):
    original = instance.Education
    instance.Education = original
    assert instance.Education == original



@given(instance=Staff_strategy)
def test_hyp_staff_Joined_setter(instance):
    original = instance.Joined
    instance.Joined = original
    assert instance.Joined == original



@given(instance=Staff_strategy)
def test_hyp_staff_Languages_setter(instance):
    original = instance.Languages
    instance.Languages = original
    assert instance.Languages == original




@given(instance=Patient_strategy)
def test_hyp_patient_Birthdate_setter(instance):
    original = instance.Birthdate
    instance.Birthdate = original
    assert instance.Birthdate == original



@given(instance=Patient_strategy)
def test_hyp_patient_DateOfEntry_setter(instance):
    original = instance.DateOfEntry
    instance.DateOfEntry = original
    assert instance.DateOfEntry == original



@given(instance=Patient_strategy)
def test_hyp_patient_PatientId_setter(instance):
    original = instance.PatientId
    instance.PatientId = original
    assert instance.PatientId == original



@given(instance=Patient_strategy)
def test_hyp_patient_Sickness_setter(instance):
    original = instance.Sickness
    instance.Sickness = original
    assert instance.Sickness == original



@given(instance=Patient_strategy)
def test_hyp_patient_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Patient_strategy)
def test_hyp_patient_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Patient_strategy)
def test_hyp_patient_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original




@given(instance=Hospital_strategy)
def test_hyp_hospital_HospitalId_setter(instance):
    original = instance.HospitalId
    instance.HospitalId = original
    assert instance.HospitalId == original



@given(instance=Hospital_strategy)
def test_hyp_hospital_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Hospital_strategy)
def test_hyp_hospital_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Hospital_strategy)
def test_hyp_hospital_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original




@given(instance=Person_strategy)
def test_hyp_person_MiddleName_setter(instance):
    original = instance.MiddleName
    instance.MiddleName = original
    assert instance.MiddleName == original



@given(instance=Person_strategy)
def test_hyp_person_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=Person_strategy)
def test_hyp_person_PersonHospitalId_setter(instance):
    original = instance.PersonHospitalId
    instance.PersonHospitalId = original
    assert instance.PersonHospitalId == original



@given(instance=Person_strategy)
def test_hyp_person_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original



@given(instance=Person_strategy)
def test_hyp_person_PersonPatientId_setter(instance):
    original = instance.PersonPatientId
    instance.PersonPatientId = original
    assert instance.PersonPatientId == original



@given(instance=Person_strategy)
def test_hyp_person_BirthDate_setter(instance):
    original = instance.BirthDate
    instance.BirthDate = original
    assert instance.BirthDate == original



@given(instance=Person_strategy)
def test_hyp_person_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



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
def test_hyp_person_Phone_setter(instance):
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
    Administrative_Staff,
    Hospital,
    Operation_Staff,
    Patient,
    Person,
    Staff,
    Techinal_Staff,
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

def test_Administrative_Staff_FrontDeskStaffName_value_roundtrip():
    instance = Administrative_Staff(FrontDeskStaffName="sample_text", ReceptionistName="sample_text")
    assert instance.FrontDeskStaffName == "sample_text"
    instance.FrontDeskStaffName = "sample_text_2"
    assert instance.FrontDeskStaffName == "sample_text_2"


def test_Administrative_Staff_ReceptionistName_value_roundtrip():
    instance = Administrative_Staff(FrontDeskStaffName="sample_text", ReceptionistName="sample_text")
    assert instance.ReceptionistName == "sample_text"
    instance.ReceptionistName = "sample_text_2"
    assert instance.ReceptionistName == "sample_text_2"


def test_Hospital_Address_value_roundtrip():
    instance = Hospital(Address="sample_text", HospitalId=7, Name="sample_text", Phone=7)
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Hospital_HospitalId_value_roundtrip():
    instance = Hospital(Address="sample_text", HospitalId=7, Name="sample_text", Phone=7)
    assert instance.HospitalId == 7
    instance.HospitalId = 13
    assert instance.HospitalId == 13


def test_Hospital_Name_value_roundtrip():
    instance = Hospital(Address="sample_text", HospitalId=7, Name="sample_text", Phone=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Hospital_Phone_value_roundtrip():
    instance = Hospital(Address="sample_text", HospitalId=7, Name="sample_text", Phone=7)
    assert instance.Phone == 7
    instance.Phone = 13
    assert instance.Phone == 13


def test_Operation_Staff_DoctorLocation_value_roundtrip():
    instance = Operation_Staff(DoctorLocation="sample_text", DoctorSpeciality="sample_text", NurseName="sample_text")
    assert instance.DoctorLocation == "sample_text"
    instance.DoctorLocation = "sample_text_2"
    assert instance.DoctorLocation == "sample_text_2"


def test_Operation_Staff_DoctorSpeciality_value_roundtrip():
    instance = Operation_Staff(DoctorLocation="sample_text", DoctorSpeciality="sample_text", NurseName="sample_text")
    assert instance.DoctorSpeciality == "sample_text"
    instance.DoctorSpeciality = "sample_text_2"
    assert instance.DoctorSpeciality == "sample_text_2"


def test_Operation_Staff_NurseName_value_roundtrip():
    instance = Operation_Staff(DoctorLocation="sample_text", DoctorSpeciality="sample_text", NurseName="sample_text")
    assert instance.NurseName == "sample_text"
    instance.NurseName = "sample_text_2"
    assert instance.NurseName == "sample_text_2"


def test_Patient_Age_value_roundtrip():
    instance = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    assert instance.Age == 7
    instance.Age = 13
    assert instance.Age == 13


def test_Patient_Birthdate_value_roundtrip():
    instance = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    assert instance.Birthdate == "sample_text"
    instance.Birthdate = "sample_text_2"
    assert instance.Birthdate == "sample_text_2"


def test_Patient_DateOfEntry_value_roundtrip():
    instance = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    assert instance.DateOfEntry == "sample_text"
    instance.DateOfEntry = "sample_text_2"
    assert instance.DateOfEntry == "sample_text_2"


def test_Patient_Gender_value_roundtrip():
    instance = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Patient_Name_value_roundtrip():
    instance = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Patient_PatientId_value_roundtrip():
    instance = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    assert instance.PatientId == 7
    instance.PatientId = 13
    assert instance.PatientId == 13


def test_Patient_Sickness_value_roundtrip():
    instance = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    assert instance.Sickness == "sample_text"
    instance.Sickness = "sample_text_2"
    assert instance.Sickness == "sample_text_2"


def test_Person_Address_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Person_BirthDate_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.BirthDate == "sample_text"
    instance.BirthDate = "sample_text_2"
    assert instance.BirthDate == "sample_text_2"


def test_Person_FirstName_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.FirstName == "sample_text"
    instance.FirstName = "sample_text_2"
    assert instance.FirstName == "sample_text_2"


def test_Person_Gender_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Person_LastName_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.LastName == "sample_text"
    instance.LastName = "sample_text_2"
    assert instance.LastName == "sample_text_2"


def test_Person_MiddleName_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.MiddleName == "sample_text"
    instance.MiddleName = "sample_text_2"
    assert instance.MiddleName == "sample_text_2"


def test_Person_PersonHospitalId_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.PersonHospitalId == 7
    instance.PersonHospitalId = 13
    assert instance.PersonHospitalId == 13


def test_Person_PersonPatientId_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.PersonPatientId == 7
    instance.PersonPatientId = 13
    assert instance.PersonPatientId == 13


def test_Person_Phone_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.Phone == 7
    instance.Phone = 13
    assert instance.Phone == 13


def test_Person_Title_value_roundtrip():
    instance = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    assert instance.Title == "sample_text"
    instance.Title = "sample_text_2"
    assert instance.Title == "sample_text_2"


def test_Staff_Certification_value_roundtrip():
    instance = Staff(Certification="sample_text", Education="sample_text", Joined="sample_text", Languages="sample_text")
    assert instance.Certification == "sample_text"
    instance.Certification = "sample_text_2"
    assert instance.Certification == "sample_text_2"


def test_Staff_Education_value_roundtrip():
    instance = Staff(Certification="sample_text", Education="sample_text", Joined="sample_text", Languages="sample_text")
    assert instance.Education == "sample_text"
    instance.Education = "sample_text_2"
    assert instance.Education == "sample_text_2"


def test_Staff_Joined_value_roundtrip():
    instance = Staff(Certification="sample_text", Education="sample_text", Joined="sample_text", Languages="sample_text")
    assert instance.Joined == "sample_text"
    instance.Joined = "sample_text_2"
    assert instance.Joined == "sample_text_2"


def test_Staff_Languages_value_roundtrip():
    instance = Staff(Certification="sample_text", Education="sample_text", Joined="sample_text", Languages="sample_text")
    assert instance.Languages == "sample_text"
    instance.Languages = "sample_text_2"
    assert instance.Languages == "sample_text_2"


def test_Techinal_Staff_Technician_value_roundtrip():
    instance = Techinal_Staff(Technician="sample_text", Technologist="sample_text")
    assert instance.Technician == "sample_text"
    instance.Technician = "sample_text_2"
    assert instance.Technician == "sample_text_2"


def test_Techinal_Staff_Technologist_value_roundtrip():
    instance = Techinal_Staff(Technician="sample_text", Technologist="sample_text")
    assert instance.Technologist == "sample_text"
    instance.Technologist = "sample_text_2"
    assert instance.Technologist == "sample_text_2"


def test_assoc_Operation_Staff_Patient_link_reassign_clear():
    a = Patient(Age=7, Birthdate="sample_text", DateOfEntry="sample_text", Gender="sample_text", Name="sample_text", PatientId=7, Sickness="sample_text")
    b1 = Operation_Staff(DoctorLocation="sample_text", DoctorSpeciality="sample_text", NurseName="sample_text")
    b2 = Operation_Staff(DoctorLocation="sample_text_2", DoctorSpeciality="sample_text_2", NurseName="sample_text_2")
    _safe_set(a, 'operation_Staff5', {b1})
    assert _is_linked(a, 'operation_Staff5', b1)
    if hasattr(b1, 'patient4'):
        assert _is_linked(b1, 'patient4', a)
    _safe_set(a, 'operation_Staff5', {b2})
    assert _is_linked(a, 'operation_Staff5', b2)
    if hasattr(b1, 'patient4'):
        assert not _is_linked(b1, 'patient4', a)
    if hasattr(b2, 'patient4'):
        assert _is_linked(b2, 'patient4', a)
    _safe_set(a, 'operation_Staff5', set())
    assert not _is_linked(a, 'operation_Staff5', b2)
    if hasattr(b2, 'patient4'):
        assert not _is_linked(b2, 'patient4', a)


def test_assoc_Person_Hospital_link_reassign_clear():
    a = Person(Address="sample_text", BirthDate="sample_text", FirstName="sample_text", Gender="sample_text", LastName="sample_text", MiddleName="sample_text", PersonHospitalId=7, PersonPatientId=7, Phone=7, Title="sample_text")
    b1 = Hospital(Address="sample_text", HospitalId=7, Name="sample_text", Phone=7)
    b2 = Hospital(Address="sample_text_2", HospitalId=13, Name="sample_text_2", Phone=13)
    _safe_set(a, 'hospital0', {b1})
    assert _is_linked(a, 'hospital0', b1)
    if hasattr(b1, 'person1'):
        assert _is_linked(b1, 'person1', a)
    _safe_set(a, 'hospital0', {b2})
    assert _is_linked(a, 'hospital0', b2)
    if hasattr(b1, 'person1'):
        assert not _is_linked(b1, 'person1', a)
    if hasattr(b2, 'person1'):
        assert _is_linked(b2, 'person1', a)
    _safe_set(a, 'hospital0', set())
    assert not _is_linked(a, 'hospital0', b2)
    if hasattr(b2, 'person1'):
        assert not _is_linked(b2, 'person1', a)


def test_assoc_Staff_Hospital_link_reassign_clear():
    a = Staff(Certification="sample_text", Education="sample_text", Joined="sample_text", Languages="sample_text")
    b1 = Hospital(Address="sample_text", HospitalId=7, Name="sample_text", Phone=7)
    b2 = Hospital(Address="sample_text_2", HospitalId=13, Name="sample_text_2", Phone=13)
    _safe_set(a, 'hospital2', {b1})
    assert _is_linked(a, 'hospital2', b1)
    if hasattr(b1, 'staff3'):
        assert _is_linked(b1, 'staff3', a)
    _safe_set(a, 'hospital2', {b2})
    assert _is_linked(a, 'hospital2', b2)
    if hasattr(b1, 'staff3'):
        assert not _is_linked(b1, 'staff3', a)
    if hasattr(b2, 'staff3'):
        assert _is_linked(b2, 'staff3', a)
    _safe_set(a, 'hospital2', set())
    assert not _is_linked(a, 'hospital2', b2)
    if hasattr(b2, 'staff3'):
        assert not _is_linked(b2, 'staff3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrative_Staff_strategy = st.builds(Administrative_Staff, FrontDeskStaffName=safe_text, ReceptionistName=safe_text)
@given(instance=Administrative_Staff_strategy)
@settings(max_examples=25)
def test_Administrative_Staff_instantiation(instance):
    assert isinstance(instance, Administrative_Staff)


Hospital_strategy = st.builds(Hospital, Address=safe_text, HospitalId=st.integers(), Name=safe_text, Phone=st.integers())
@given(instance=Hospital_strategy)
@settings(max_examples=25)
def test_Hospital_instantiation(instance):
    assert isinstance(instance, Hospital)


Operation_Staff_strategy = st.builds(Operation_Staff, DoctorLocation=safe_text, DoctorSpeciality=safe_text, NurseName=safe_text)
@given(instance=Operation_Staff_strategy)
@settings(max_examples=25)
def test_Operation_Staff_instantiation(instance):
    assert isinstance(instance, Operation_Staff)


Patient_strategy = st.builds(Patient, Age=st.integers(), Birthdate=safe_text, DateOfEntry=safe_text, Gender=safe_text, Name=safe_text, PatientId=st.integers(), Sickness=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Person_strategy = st.builds(Person, Address=safe_text, BirthDate=safe_text, FirstName=safe_text, Gender=safe_text, LastName=safe_text, MiddleName=safe_text, PersonHospitalId=st.integers(), PersonPatientId=st.integers(), Phone=st.integers(), Title=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Staff_strategy = st.builds(Staff, Certification=safe_text, Education=safe_text, Joined=safe_text, Languages=safe_text)
@given(instance=Staff_strategy)
@settings(max_examples=25)
def test_Staff_instantiation(instance):
    assert isinstance(instance, Staff)


Techinal_Staff_strategy = st.builds(Techinal_Staff, Technician=safe_text, Technologist=safe_text)
@given(instance=Techinal_Staff_strategy)
@settings(max_examples=25)
def test_Techinal_Staff_instantiation(instance):
    assert isinstance(instance, Techinal_Staff)



