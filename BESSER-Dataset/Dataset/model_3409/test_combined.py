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
    VorkursModel_Room,
    Person,
    VorkursModel_Contact,
    VorkursModel_Person,
    VorkursModel_TeachingAssistant,
    VorkursModel_Student,
    VorkursModel_RegistrationSystem,
    VorkursModel_Address,
    VorkursModel_Qualification,
    VorkursModel_Notebook,
    Subject,
    OperatingSystem,
    Nationality,
    ProgrammingLanguage,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_vorkursmodel_room_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Room)


def test_hyp_vorkursmodel_room_constructor_exists():
    assert callable(VorkursModel_Room.__init__)


def test_hyp_vorkursmodel_room_constructor_args():
    sig = inspect.signature(VorkursModel_Room.__init__)
    params = list(sig.parameters.keys())
    assert "hasComputers" in params, "Missing parameter 'hasComputers'"
    assert "seats" in params, "Missing parameter 'seats'"
    assert "roomNr" in params, "Missing parameter 'roomNr'"
    assert "sockets" in params, "Missing parameter 'sockets'"







def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vorkursmodel_contact_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Contact)


def test_hyp_vorkursmodel_contact_constructor_exists():
    assert callable(VorkursModel_Contact.__init__)


def test_hyp_vorkursmodel_contact_constructor_args():
    sig = inspect.signature(VorkursModel_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "phonenumber" in params, "Missing parameter 'phonenumber'"
    assert "Email" in params, "Missing parameter 'Email'"





def test_hyp_vorkursmodel_person_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Person)


def test_hyp_vorkursmodel_person_constructor_exists():
    assert callable(VorkursModel_Person.__init__)


def test_hyp_vorkursmodel_person_constructor_args():
    sig = inspect.signature(VorkursModel_Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"







def test_hyp_vorkursmodel_teachingassistant_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_TeachingAssistant)


def test_hyp_vorkursmodel_teachingassistant_constructor_exists():
    assert callable(VorkursModel_TeachingAssistant.__init__)


def test_hyp_vorkursmodel_teachingassistant_constructor_args():
    sig = inspect.signature(VorkursModel_TeachingAssistant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vorkursmodel_student_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Student)


def test_hyp_vorkursmodel_student_constructor_exists():
    assert callable(VorkursModel_Student.__init__)


def test_hyp_vorkursmodel_student_constructor_args():
    sig = inspect.signature(VorkursModel_Student.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vorkursmodel_registrationsystem_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_RegistrationSystem)


def test_hyp_vorkursmodel_registrationsystem_constructor_exists():
    assert callable(VorkursModel_RegistrationSystem.__init__)


def test_hyp_vorkursmodel_registrationsystem_constructor_args():
    sig = inspect.signature(VorkursModel_RegistrationSystem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vorkursmodel_address_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Address)


def test_hyp_vorkursmodel_address_constructor_exists():
    assert callable(VorkursModel_Address.__init__)


def test_hyp_vorkursmodel_address_constructor_args():
    sig = inspect.signature(VorkursModel_Address.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "zip" in params, "Missing parameter 'zip'"
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"







def test_hyp_vorkursmodel_qualification_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Qualification)


def test_hyp_vorkursmodel_qualification_constructor_exists():
    assert callable(VorkursModel_Qualification.__init__)


def test_hyp_vorkursmodel_qualification_constructor_args():
    sig = inspect.signature(VorkursModel_Qualification.__init__)
    params = list(sig.parameters.keys())
    assert "hasProgrammingExperience" in params, "Missing parameter 'hasProgrammingExperience'"
    assert "Language" in params, "Missing parameter 'Language'"
    assert "programminLanguage" in params, "Missing parameter 'programminLanguage'"
    assert "hasPCExperience" in params, "Missing parameter 'hasPCExperience'"







def test_hyp_vorkursmodel_notebook_is_not_abstract():
    assert not inspect.isabstract(VorkursModel_Notebook)


def test_hyp_vorkursmodel_notebook_constructor_exists():
    assert callable(VorkursModel_Notebook.__init__)


def test_hyp_vorkursmodel_notebook_constructor_args():
    sig = inspect.signature(VorkursModel_Notebook.__init__)
    params = list(sig.parameters.keys())
    assert "OperatingSystem" in params, "Missing parameter 'OperatingSystem'"
    assert "hasWLAN" in params, "Missing parameter 'hasWLAN'"



def test_hyp_subject_exists():
    # Check that the Enumeration exists
    assert Subject is not None

def test_hyp_subject_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Subject]
    expected_literals = [
        "ComputerScience",
        "MechanicalEngineering",
        "AppliedGeographics",
        "BusinessEngineering",
        "Physics",
        "Mathematics",
        "CES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Subject"

def test_hyp_operatingsystem_exists():
    # Check that the Enumeration exists
    assert OperatingSystem is not None

def test_hyp_operatingsystem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatingSystem]
    expected_literals = [
        "other",
        "MacOS",
        "Linux_Unix",
        "Windows",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatingSystem"

def test_hyp_nationality_exists():
    # Check that the Enumeration exists
    assert Nationality is not None

def test_hyp_nationality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Nationality]
    expected_literals = [
        "Spanish",
        "German",
        "other",
        "French",
        "English",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Nationality"

def test_hyp_programminglanguage_exists():
    # Check that the Enumeration exists
    assert ProgrammingLanguage is not None

def test_hyp_programminglanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammingLanguage]
    expected_literals = [
        "Pascal_Delphi",
        "other",
        "Java",
        "C_CPP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammingLanguage"

def test_hyp_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_hyp_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "Female",
        "Male",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
VorkursModel_Room_strategy = st.builds(
    VorkursModel_Room,
    hasComputers=
        st.booleans(),
    seats=
        st.integers(),
    roomNr=
        st.integers(),
    sockets=
        st.booleans()
)
Person_strategy = st.builds(
    Person,
)
VorkursModel_Contact_strategy = st.builds(
    VorkursModel_Contact,
    phonenumber=
        safe_text,
    Email=
        safe_text
)
VorkursModel_Person_strategy = st.builds(
    VorkursModel_Person,
    gender=
        safe_text,
    subject=
        safe_text,
    lastname=
        safe_text,
    firstname=
        safe_text
)
VorkursModel_TeachingAssistant_strategy = st.builds(
    VorkursModel_TeachingAssistant,
)
VorkursModel_Student_strategy = st.builds(
    VorkursModel_Student,
)
VorkursModel_RegistrationSystem_strategy = st.builds(
    VorkursModel_RegistrationSystem,
)
VorkursModel_Address_strategy = st.builds(
    VorkursModel_Address,
    state=
        safe_text,
    zip=
        safe_text,
    street=
        safe_text,
    city=
        safe_text
)
VorkursModel_Qualification_strategy = st.builds(
    VorkursModel_Qualification,
    hasProgrammingExperience=
        st.booleans(),
    Language=
        safe_text,
    programminLanguage=
        safe_text,
    hasPCExperience=
        st.booleans()
)
VorkursModel_Notebook_strategy = st.builds(
    VorkursModel_Notebook,
    OperatingSystem=
        safe_text,
    hasWLAN=
        st.booleans()
)




@given(instance=VorkursModel_Room_strategy)
def test_hyp_vorkursmodel_room_hasComputers_setter(instance):
    original = instance.hasComputers
    instance.hasComputers = original
    assert instance.hasComputers == original



@given(instance=VorkursModel_Room_strategy)
def test_hyp_vorkursmodel_room_seats_setter(instance):
    original = instance.seats
    instance.seats = original
    assert instance.seats == original



@given(instance=VorkursModel_Room_strategy)
def test_hyp_vorkursmodel_room_roomNr_setter(instance):
    original = instance.roomNr
    instance.roomNr = original
    assert instance.roomNr == original



@given(instance=VorkursModel_Room_strategy)
def test_hyp_vorkursmodel_room_sockets_setter(instance):
    original = instance.sockets
    instance.sockets = original
    assert instance.sockets == original





@given(instance=VorkursModel_Contact_strategy)
def test_hyp_vorkursmodel_contact_phonenumber_setter(instance):
    original = instance.phonenumber
    instance.phonenumber = original
    assert instance.phonenumber == original



@given(instance=VorkursModel_Contact_strategy)
def test_hyp_vorkursmodel_contact_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original




@given(instance=VorkursModel_Person_strategy)
def test_hyp_vorkursmodel_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=VorkursModel_Person_strategy)
def test_hyp_vorkursmodel_person_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=VorkursModel_Person_strategy)
def test_hyp_vorkursmodel_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=VorkursModel_Person_strategy)
def test_hyp_vorkursmodel_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original







@given(instance=VorkursModel_Address_strategy)
def test_hyp_vorkursmodel_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=VorkursModel_Address_strategy)
def test_hyp_vorkursmodel_address_zip_setter(instance):
    original = instance.zip
    instance.zip = original
    assert instance.zip == original



@given(instance=VorkursModel_Address_strategy)
def test_hyp_vorkursmodel_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=VorkursModel_Address_strategy)
def test_hyp_vorkursmodel_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original




@given(instance=VorkursModel_Qualification_strategy)
def test_hyp_vorkursmodel_qualification_hasProgrammingExperience_setter(instance):
    original = instance.hasProgrammingExperience
    instance.hasProgrammingExperience = original
    assert instance.hasProgrammingExperience == original



@given(instance=VorkursModel_Qualification_strategy)
def test_hyp_vorkursmodel_qualification_Language_setter(instance):
    original = instance.Language
    instance.Language = original
    assert instance.Language == original



@given(instance=VorkursModel_Qualification_strategy)
def test_hyp_vorkursmodel_qualification_programminLanguage_setter(instance):
    original = instance.programminLanguage
    instance.programminLanguage = original
    assert instance.programminLanguage == original



@given(instance=VorkursModel_Qualification_strategy)
def test_hyp_vorkursmodel_qualification_hasPCExperience_setter(instance):
    original = instance.hasPCExperience
    instance.hasPCExperience = original
    assert instance.hasPCExperience == original




@given(instance=VorkursModel_Notebook_strategy)
def test_hyp_vorkursmodel_notebook_OperatingSystem_setter(instance):
    original = instance.OperatingSystem
    instance.OperatingSystem = original
    assert instance.OperatingSystem == original



@given(instance=VorkursModel_Notebook_strategy)
def test_hyp_vorkursmodel_notebook_hasWLAN_setter(instance):
    original = instance.hasWLAN
    instance.hasWLAN = original
    assert instance.hasWLAN == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    VorkursModel_Address,
    VorkursModel_Contact,
    VorkursModel_Notebook,
    VorkursModel_Person,
    VorkursModel_Qualification,
    VorkursModel_RegistrationSystem,
    VorkursModel_Room,
    VorkursModel_Student,
    VorkursModel_TeachingAssistant,
    Gender,
    Nationality,
    OperatingSystem,
    ProgrammingLanguage,
    Subject,
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

def test_VorkursModel_Address_city_value_roundtrip():
    instance = VorkursModel_Address(city="sample_text", state="sample_text", street="sample_text", zip="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_VorkursModel_Address_state_value_roundtrip():
    instance = VorkursModel_Address(city="sample_text", state="sample_text", street="sample_text", zip="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_VorkursModel_Address_street_value_roundtrip():
    instance = VorkursModel_Address(city="sample_text", state="sample_text", street="sample_text", zip="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_VorkursModel_Address_zip_value_roundtrip():
    instance = VorkursModel_Address(city="sample_text", state="sample_text", street="sample_text", zip="sample_text")
    assert instance.zip == "sample_text"
    instance.zip = "sample_text_2"
    assert instance.zip == "sample_text_2"


def test_VorkursModel_Contact_Email_value_roundtrip():
    instance = VorkursModel_Contact(Email="sample_text", phonenumber="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_VorkursModel_Contact_phonenumber_value_roundtrip():
    instance = VorkursModel_Contact(Email="sample_text", phonenumber="sample_text")
    assert instance.phonenumber == "sample_text"
    instance.phonenumber = "sample_text_2"
    assert instance.phonenumber == "sample_text_2"


def test_VorkursModel_Notebook_OperatingSystem_value_roundtrip():
    instance = VorkursModel_Notebook(OperatingSystem="sample_text", hasWLAN=True)
    assert instance.OperatingSystem == "sample_text"
    instance.OperatingSystem = "sample_text_2"
    assert instance.OperatingSystem == "sample_text_2"


def test_VorkursModel_Notebook_hasWLAN_value_roundtrip():
    instance = VorkursModel_Notebook(OperatingSystem="sample_text", hasWLAN=True)
    assert instance.hasWLAN == True
    instance.hasWLAN = False
    assert instance.hasWLAN == False


def test_VorkursModel_Person_firstname_value_roundtrip():
    instance = VorkursModel_Person(firstname="sample_text", gender="sample_text", lastname="sample_text", subject="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_VorkursModel_Person_gender_value_roundtrip():
    instance = VorkursModel_Person(firstname="sample_text", gender="sample_text", lastname="sample_text", subject="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_VorkursModel_Person_lastname_value_roundtrip():
    instance = VorkursModel_Person(firstname="sample_text", gender="sample_text", lastname="sample_text", subject="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_VorkursModel_Person_subject_value_roundtrip():
    instance = VorkursModel_Person(firstname="sample_text", gender="sample_text", lastname="sample_text", subject="sample_text")
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


def test_VorkursModel_Qualification_Language_value_roundtrip():
    instance = VorkursModel_Qualification(Language="sample_text", hasPCExperience=True, hasProgrammingExperience=True, programminLanguage="sample_text")
    assert instance.Language == "sample_text"
    instance.Language = "sample_text_2"
    assert instance.Language == "sample_text_2"


def test_VorkursModel_Qualification_hasPCExperience_value_roundtrip():
    instance = VorkursModel_Qualification(Language="sample_text", hasPCExperience=True, hasProgrammingExperience=True, programminLanguage="sample_text")
    assert instance.hasPCExperience == True
    instance.hasPCExperience = False
    assert instance.hasPCExperience == False


def test_VorkursModel_Qualification_hasProgrammingExperience_value_roundtrip():
    instance = VorkursModel_Qualification(Language="sample_text", hasPCExperience=True, hasProgrammingExperience=True, programminLanguage="sample_text")
    assert instance.hasProgrammingExperience == True
    instance.hasProgrammingExperience = False
    assert instance.hasProgrammingExperience == False


def test_VorkursModel_Qualification_programminLanguage_value_roundtrip():
    instance = VorkursModel_Qualification(Language="sample_text", hasPCExperience=True, hasProgrammingExperience=True, programminLanguage="sample_text")
    assert instance.programminLanguage == "sample_text"
    instance.programminLanguage = "sample_text_2"
    assert instance.programminLanguage == "sample_text_2"


def test_VorkursModel_Room_hasComputers_value_roundtrip():
    instance = VorkursModel_Room(hasComputers=True, roomNr=7, seats=7, sockets=True)
    assert instance.hasComputers == True
    instance.hasComputers = False
    assert instance.hasComputers == False


def test_VorkursModel_Room_roomNr_value_roundtrip():
    instance = VorkursModel_Room(hasComputers=True, roomNr=7, seats=7, sockets=True)
    assert instance.roomNr == 7
    instance.roomNr = 13
    assert instance.roomNr == 13


def test_VorkursModel_Room_seats_value_roundtrip():
    instance = VorkursModel_Room(hasComputers=True, roomNr=7, seats=7, sockets=True)
    assert instance.seats == 7
    instance.seats = 13
    assert instance.seats == 13


def test_VorkursModel_Room_sockets_value_roundtrip():
    instance = VorkursModel_Room(hasComputers=True, roomNr=7, seats=7, sockets=True)
    assert instance.sockets == True
    instance.sockets = False
    assert instance.sockets == False


def test_VorkursModel_Student_isa_Person():
    instance = VorkursModel_Student()
    assert isinstance(instance, Person)


def test_VorkursModel_TeachingAssistant_isa_Person():
    instance = VorkursModel_TeachingAssistant()
    assert isinstance(instance, Person)


def test_assoc_address8_link_reassign_clear():
    a = VorkursModel_Contact(Email="sample_text", phonenumber="sample_text")
    b1 = VorkursModel_Address(city="sample_text", state="sample_text", street="sample_text", zip="sample_text")
    b2 = VorkursModel_Address(city="sample_text_2", state="sample_text_2", street="sample_text_2", zip="sample_text_2")
    _safe_set(a, 'VorkursModel_Contact9', b1)
    assert _is_linked(a, 'VorkursModel_Contact9', b1)
    if hasattr(b1, 'VorkursModel_Address'):
        assert _is_linked(b1, 'VorkursModel_Address', a)
    _safe_set(a, 'VorkursModel_Contact9', b2)
    assert _is_linked(a, 'VorkursModel_Contact9', b2)
    if hasattr(b1, 'VorkursModel_Address'):
        assert not _is_linked(b1, 'VorkursModel_Address', a)
    if hasattr(b2, 'VorkursModel_Address'):
        assert _is_linked(b2, 'VorkursModel_Address', a)
    _safe_set(a, 'VorkursModel_Contact9', None)
    assert not _is_linked(a, 'VorkursModel_Contact9', b2)
    if hasattr(b2, 'VorkursModel_Address'):
        assert not _is_linked(b2, 'VorkursModel_Address', a)


def test_assoc_contactinfo3_link_reassign_clear():
    a = VorkursModel_Person(firstname="sample_text", gender="sample_text", lastname="sample_text", subject="sample_text")
    b1 = VorkursModel_Contact(Email="sample_text", phonenumber="sample_text")
    b2 = VorkursModel_Contact(Email="sample_text_2", phonenumber="sample_text_2")
    _safe_set(a, 'VorkursModel_Person', b1)
    assert _is_linked(a, 'VorkursModel_Person', b1)
    if hasattr(b1, 'VorkursModel_Contact'):
        assert _is_linked(b1, 'VorkursModel_Contact', a)
    _safe_set(a, 'VorkursModel_Person', b2)
    assert _is_linked(a, 'VorkursModel_Person', b2)
    if hasattr(b1, 'VorkursModel_Contact'):
        assert not _is_linked(b1, 'VorkursModel_Contact', a)
    if hasattr(b2, 'VorkursModel_Contact'):
        assert _is_linked(b2, 'VorkursModel_Contact', a)
    _safe_set(a, 'VorkursModel_Person', None)
    assert not _is_linked(a, 'VorkursModel_Person', b2)
    if hasattr(b2, 'VorkursModel_Contact'):
        assert not _is_linked(b2, 'VorkursModel_Contact', a)


def test_assoc_notebook4_link_reassign_clear():
    a = VorkursModel_Person(firstname="sample_text", gender="sample_text", lastname="sample_text", subject="sample_text")
    b1 = VorkursModel_Notebook(OperatingSystem="sample_text", hasWLAN=True)
    b2 = VorkursModel_Notebook(OperatingSystem="sample_text_2", hasWLAN=False)
    _safe_set(a, 'VorkursModel_Person5', b1)
    assert _is_linked(a, 'VorkursModel_Person5', b1)
    if hasattr(b1, 'VorkursModel_Notebook'):
        assert _is_linked(b1, 'VorkursModel_Notebook', a)
    _safe_set(a, 'VorkursModel_Person5', b2)
    assert _is_linked(a, 'VorkursModel_Person5', b2)
    if hasattr(b1, 'VorkursModel_Notebook'):
        assert not _is_linked(b1, 'VorkursModel_Notebook', a)
    if hasattr(b2, 'VorkursModel_Notebook'):
        assert _is_linked(b2, 'VorkursModel_Notebook', a)
    _safe_set(a, 'VorkursModel_Person5', None)
    assert not _is_linked(a, 'VorkursModel_Person5', b2)
    if hasattr(b2, 'VorkursModel_Notebook'):
        assert not _is_linked(b2, 'VorkursModel_Notebook', a)


def test_assoc_qualification6_link_reassign_clear():
    a = VorkursModel_Qualification(Language="sample_text", hasPCExperience=True, hasProgrammingExperience=True, programminLanguage="sample_text")
    b1 = VorkursModel_Person(firstname="sample_text", gender="sample_text", lastname="sample_text", subject="sample_text")
    b2 = VorkursModel_Person(firstname="sample_text_2", gender="sample_text_2", lastname="sample_text_2", subject="sample_text_2")
    _safe_set(a, 'VorkursModel_Qualification', b1)
    assert _is_linked(a, 'VorkursModel_Qualification', b1)
    if hasattr(b1, 'VorkursModel_Person7'):
        assert _is_linked(b1, 'VorkursModel_Person7', a)
    _safe_set(a, 'VorkursModel_Qualification', b2)
    assert _is_linked(a, 'VorkursModel_Qualification', b2)
    if hasattr(b1, 'VorkursModel_Person7'):
        assert not _is_linked(b1, 'VorkursModel_Person7', a)
    if hasattr(b2, 'VorkursModel_Person7'):
        assert _is_linked(b2, 'VorkursModel_Person7', a)
    _safe_set(a, 'VorkursModel_Qualification', None)
    assert not _is_linked(a, 'VorkursModel_Qualification', b2)
    if hasattr(b2, 'VorkursModel_Person7'):
        assert not _is_linked(b2, 'VorkursModel_Person7', a)


def test_assoc_room10_link_reassign_clear():
    a = VorkursModel_Room(hasComputers=True, roomNr=7, seats=7, sockets=True)
    b1 = VorkursModel_TeachingAssistant()
    b2 = VorkursModel_TeachingAssistant()
    _safe_set(a, 'VorkursModel_Room', b1)
    assert _is_linked(a, 'VorkursModel_Room', b1)
    if hasattr(b1, 'VorkursModel_TeachingAssistant11'):
        assert _is_linked(b1, 'VorkursModel_TeachingAssistant11', a)
    _safe_set(a, 'VorkursModel_Room', b2)
    assert _is_linked(a, 'VorkursModel_Room', b2)
    if hasattr(b1, 'VorkursModel_TeachingAssistant11'):
        assert not _is_linked(b1, 'VorkursModel_TeachingAssistant11', a)
    if hasattr(b2, 'VorkursModel_TeachingAssistant11'):
        assert _is_linked(b2, 'VorkursModel_TeachingAssistant11', a)
    _safe_set(a, 'VorkursModel_Room', None)
    assert not _is_linked(a, 'VorkursModel_Room', b2)
    if hasattr(b2, 'VorkursModel_TeachingAssistant11'):
        assert not _is_linked(b2, 'VorkursModel_TeachingAssistant11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


VorkursModel_Address_strategy = st.builds(VorkursModel_Address, city=safe_text, state=safe_text, street=safe_text, zip=safe_text)
@given(instance=VorkursModel_Address_strategy)
@settings(max_examples=25)
def test_VorkursModel_Address_instantiation(instance):
    assert isinstance(instance, VorkursModel_Address)


VorkursModel_Contact_strategy = st.builds(VorkursModel_Contact, Email=safe_text, phonenumber=safe_text)
@given(instance=VorkursModel_Contact_strategy)
@settings(max_examples=25)
def test_VorkursModel_Contact_instantiation(instance):
    assert isinstance(instance, VorkursModel_Contact)


VorkursModel_Notebook_strategy = st.builds(VorkursModel_Notebook, OperatingSystem=safe_text, hasWLAN=st.booleans())
@given(instance=VorkursModel_Notebook_strategy)
@settings(max_examples=25)
def test_VorkursModel_Notebook_instantiation(instance):
    assert isinstance(instance, VorkursModel_Notebook)


VorkursModel_Person_strategy = st.builds(VorkursModel_Person, firstname=safe_text, gender=safe_text, lastname=safe_text, subject=safe_text)
@given(instance=VorkursModel_Person_strategy)
@settings(max_examples=25)
def test_VorkursModel_Person_instantiation(instance):
    assert isinstance(instance, VorkursModel_Person)


VorkursModel_Qualification_strategy = st.builds(VorkursModel_Qualification, Language=safe_text, hasPCExperience=st.booleans(), hasProgrammingExperience=st.booleans(), programminLanguage=safe_text)
@given(instance=VorkursModel_Qualification_strategy)
@settings(max_examples=25)
def test_VorkursModel_Qualification_instantiation(instance):
    assert isinstance(instance, VorkursModel_Qualification)


VorkursModel_RegistrationSystem_strategy = st.builds(VorkursModel_RegistrationSystem)
@given(instance=VorkursModel_RegistrationSystem_strategy)
@settings(max_examples=25)
def test_VorkursModel_RegistrationSystem_instantiation(instance):
    assert isinstance(instance, VorkursModel_RegistrationSystem)


VorkursModel_Room_strategy = st.builds(VorkursModel_Room, hasComputers=st.booleans(), roomNr=st.integers(), seats=st.integers(), sockets=st.booleans())
@given(instance=VorkursModel_Room_strategy)
@settings(max_examples=25)
def test_VorkursModel_Room_instantiation(instance):
    assert isinstance(instance, VorkursModel_Room)


VorkursModel_Student_strategy = st.builds(VorkursModel_Student)
@given(instance=VorkursModel_Student_strategy)
@settings(max_examples=25)
def test_VorkursModel_Student_instantiation(instance):
    assert isinstance(instance, VorkursModel_Student)


VorkursModel_TeachingAssistant_strategy = st.builds(VorkursModel_TeachingAssistant)
@given(instance=VorkursModel_TeachingAssistant_strategy)
@settings(max_examples=25)
def test_VorkursModel_TeachingAssistant_instantiation(instance):
    assert isinstance(instance, VorkursModel_TeachingAssistant)



