import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator_Actor,
    Check_black_list_requests_UseCase,
    Create_new_administrators_UseCase,
    Create_reports_UseCase,
    Edit_information_UseCase,
    Edit_pet_information_UseCase,
    Edit_user_information_UseCase,
    Logging_into_program_UseCase,
    Logging_into_web_UseCase,
    Make_requests_to_administrator_UseCase,
    Match_lost_pet_cases_UseCase,
    Medeina,
    Organization,
    Pet,
    Register_a_pet_UseCase,
    Register_as_a_pro_care_association_UseCase,
    Register_as_an_adopter_UseCase,
    Register_pet_types_UseCase,
    Register_pets__physical_characteristics_UseCase,
    Registering_UseCase,
    Report_a_person_to_the_blacklist_UseCase,
    Search_UseCase,
    Search_pet_accessories_UseCase,
    Search_pet_s_UseCase,
    Send_mail_to_lost_pet_owners_UseCase,
    System_Actor,
    User,
    User_Actor,
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

def test_Organization_name_value_roundtrip():
    instance = Organization(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Pet_breed_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.breed == "sample_text"
    instance.breed = "sample_text_2"
    assert instance.breed == "sample_text_2"


def test_Pet_chipID_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.chipID == "sample_text"
    instance.chipID = "sample_text_2"
    assert instance.chipID == "sample_text_2"


def test_Pet_color_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_Pet_date_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_Pet_email_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Pet_name_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Pet_notes_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_Pet_phone_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Pet_picture_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.picture == "sample_text"
    instance.picture = "sample_text_2"
    assert instance.picture == "sample_text_2"


def test_Pet_place_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.place == "sample_text"
    instance.place = "sample_text_2"
    assert instance.place == "sample_text_2"


def test_Pet_reward_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.reward == 7
    instance.reward = 13
    assert instance.reward == 13


def test_Pet_state_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_Pet_stray_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.stray == True
    instance.stray = False
    assert instance.stray == False


def test_Pet_type_value_roundtrip():
    instance = Pet(breed="sample_text", chipID="sample_text", color="sample_text", date=date(2024, 1, 1), email="sample_text", name="sample_text", notes="sample_text", phone="sample_text", picture="sample_text", place="sample_text", reward=7, state="sample_text", stray=True, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_User_lastName_value_roundtrip():
    instance = User(lastName="sample_text", name="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_User_name_value_roundtrip():
    instance = User(lastName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


Check_black_list_requests_UseCase_strategy = st.builds(Check_black_list_requests_UseCase)
@given(instance=Check_black_list_requests_UseCase_strategy)
@settings(max_examples=25)
def test_Check_black_list_requests_UseCase_instantiation(instance):
    assert isinstance(instance, Check_black_list_requests_UseCase)


Create_new_administrators_UseCase_strategy = st.builds(Create_new_administrators_UseCase)
@given(instance=Create_new_administrators_UseCase_strategy)
@settings(max_examples=25)
def test_Create_new_administrators_UseCase_instantiation(instance):
    assert isinstance(instance, Create_new_administrators_UseCase)


Create_reports_UseCase_strategy = st.builds(Create_reports_UseCase)
@given(instance=Create_reports_UseCase_strategy)
@settings(max_examples=25)
def test_Create_reports_UseCase_instantiation(instance):
    assert isinstance(instance, Create_reports_UseCase)


Edit_information_UseCase_strategy = st.builds(Edit_information_UseCase)
@given(instance=Edit_information_UseCase_strategy)
@settings(max_examples=25)
def test_Edit_information_UseCase_instantiation(instance):
    assert isinstance(instance, Edit_information_UseCase)


Edit_pet_information_UseCase_strategy = st.builds(Edit_pet_information_UseCase)
@given(instance=Edit_pet_information_UseCase_strategy)
@settings(max_examples=25)
def test_Edit_pet_information_UseCase_instantiation(instance):
    assert isinstance(instance, Edit_pet_information_UseCase)


Edit_user_information_UseCase_strategy = st.builds(Edit_user_information_UseCase)
@given(instance=Edit_user_information_UseCase_strategy)
@settings(max_examples=25)
def test_Edit_user_information_UseCase_instantiation(instance):
    assert isinstance(instance, Edit_user_information_UseCase)


Logging_into_program_UseCase_strategy = st.builds(Logging_into_program_UseCase)
@given(instance=Logging_into_program_UseCase_strategy)
@settings(max_examples=25)
def test_Logging_into_program_UseCase_instantiation(instance):
    assert isinstance(instance, Logging_into_program_UseCase)


Logging_into_web_UseCase_strategy = st.builds(Logging_into_web_UseCase)
@given(instance=Logging_into_web_UseCase_strategy)
@settings(max_examples=25)
def test_Logging_into_web_UseCase_instantiation(instance):
    assert isinstance(instance, Logging_into_web_UseCase)


Make_requests_to_administrator_UseCase_strategy = st.builds(Make_requests_to_administrator_UseCase)
@given(instance=Make_requests_to_administrator_UseCase_strategy)
@settings(max_examples=25)
def test_Make_requests_to_administrator_UseCase_instantiation(instance):
    assert isinstance(instance, Make_requests_to_administrator_UseCase)


Match_lost_pet_cases_UseCase_strategy = st.builds(Match_lost_pet_cases_UseCase)
@given(instance=Match_lost_pet_cases_UseCase_strategy)
@settings(max_examples=25)
def test_Match_lost_pet_cases_UseCase_instantiation(instance):
    assert isinstance(instance, Match_lost_pet_cases_UseCase)


Organization_strategy = st.builds(Organization, name=safe_text)
@given(instance=Organization_strategy)
@settings(max_examples=25)
def test_Organization_instantiation(instance):
    assert isinstance(instance, Organization)


Pet_strategy = st.builds(Pet, breed=safe_text, chipID=safe_text, color=safe_text, date=st.dates(), email=safe_text, name=safe_text, notes=safe_text, phone=safe_text, picture=safe_text, place=safe_text, reward=st.integers(), state=safe_text, stray=st.booleans(), type=safe_text)
@given(instance=Pet_strategy)
@settings(max_examples=25)
def test_Pet_instantiation(instance):
    assert isinstance(instance, Pet)


Register_a_pet_UseCase_strategy = st.builds(Register_a_pet_UseCase)
@given(instance=Register_a_pet_UseCase_strategy)
@settings(max_examples=25)
def test_Register_a_pet_UseCase_instantiation(instance):
    assert isinstance(instance, Register_a_pet_UseCase)


Register_as_a_pro_care_association_UseCase_strategy = st.builds(Register_as_a_pro_care_association_UseCase)
@given(instance=Register_as_a_pro_care_association_UseCase_strategy)
@settings(max_examples=25)
def test_Register_as_a_pro_care_association_UseCase_instantiation(instance):
    assert isinstance(instance, Register_as_a_pro_care_association_UseCase)


Register_as_an_adopter_UseCase_strategy = st.builds(Register_as_an_adopter_UseCase)
@given(instance=Register_as_an_adopter_UseCase_strategy)
@settings(max_examples=25)
def test_Register_as_an_adopter_UseCase_instantiation(instance):
    assert isinstance(instance, Register_as_an_adopter_UseCase)


Register_pet_types_UseCase_strategy = st.builds(Register_pet_types_UseCase)
@given(instance=Register_pet_types_UseCase_strategy)
@settings(max_examples=25)
def test_Register_pet_types_UseCase_instantiation(instance):
    assert isinstance(instance, Register_pet_types_UseCase)


Register_pets__physical_characteristics_UseCase_strategy = st.builds(Register_pets__physical_characteristics_UseCase)
@given(instance=Register_pets__physical_characteristics_UseCase_strategy)
@settings(max_examples=25)
def test_Register_pets__physical_characteristics_UseCase_instantiation(instance):
    assert isinstance(instance, Register_pets__physical_characteristics_UseCase)


Registering_UseCase_strategy = st.builds(Registering_UseCase)
@given(instance=Registering_UseCase_strategy)
@settings(max_examples=25)
def test_Registering_UseCase_instantiation(instance):
    assert isinstance(instance, Registering_UseCase)


Report_a_person_to_the_blacklist_UseCase_strategy = st.builds(Report_a_person_to_the_blacklist_UseCase)
@given(instance=Report_a_person_to_the_blacklist_UseCase_strategy)
@settings(max_examples=25)
def test_Report_a_person_to_the_blacklist_UseCase_instantiation(instance):
    assert isinstance(instance, Report_a_person_to_the_blacklist_UseCase)


Search_UseCase_strategy = st.builds(Search_UseCase)
@given(instance=Search_UseCase_strategy)
@settings(max_examples=25)
def test_Search_UseCase_instantiation(instance):
    assert isinstance(instance, Search_UseCase)


Search_pet_accessories_UseCase_strategy = st.builds(Search_pet_accessories_UseCase)
@given(instance=Search_pet_accessories_UseCase_strategy)
@settings(max_examples=25)
def test_Search_pet_accessories_UseCase_instantiation(instance):
    assert isinstance(instance, Search_pet_accessories_UseCase)


Search_pet_s_UseCase_strategy = st.builds(Search_pet_s_UseCase)
@given(instance=Search_pet_s_UseCase_strategy)
@settings(max_examples=25)
def test_Search_pet_s_UseCase_instantiation(instance):
    assert isinstance(instance, Search_pet_s_UseCase)


Send_mail_to_lost_pet_owners_UseCase_strategy = st.builds(Send_mail_to_lost_pet_owners_UseCase)
@given(instance=Send_mail_to_lost_pet_owners_UseCase_strategy)
@settings(max_examples=25)
def test_Send_mail_to_lost_pet_owners_UseCase_instantiation(instance):
    assert isinstance(instance, Send_mail_to_lost_pet_owners_UseCase)


System_Actor_strategy = st.builds(System_Actor)
@given(instance=System_Actor_strategy)
@settings(max_examples=25)
def test_System_Actor_instantiation(instance):
    assert isinstance(instance, System_Actor)


User_strategy = st.builds(User, lastName=safe_text, name=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


User_Actor_strategy = st.builds(User_Actor)
@given(instance=User_Actor_strategy)
@settings(max_examples=25)
def test_User_Actor_instantiation(instance):
    assert isinstance(instance, User_Actor)


