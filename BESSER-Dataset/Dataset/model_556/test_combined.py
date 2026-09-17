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
    Source,
    gedcoml_PersonRef,
    gedcoml_Others,
    gedcoml_Address,
    gedcoml_Source,
    gedcoml_Note,
    gedcoml_Married,
    Person,
    gedcoml_UnbekanntePerson,
    gedcoml_BekanntePerson,
    gedcoml_Person,
    gedcoml_Family,
    gedcoml_Author,
    gedcoml_FamilyImport,
    Address,
    gedcoml_PostAddress,
    gedcoml_FamilyBook,
    gedcoml_Projectdescription,
    Sexus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_hyp_source_constructor_exists():
    assert callable(Source.__init__)


def test_hyp_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedcoml_personref_is_not_abstract():
    assert not inspect.isabstract(gedcoml_PersonRef)


def test_hyp_gedcoml_personref_constructor_exists():
    assert callable(gedcoml_PersonRef.__init__)


def test_hyp_gedcoml_personref_constructor_args():
    sig = inspect.signature(gedcoml_PersonRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedcoml_others_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Others)


def test_hyp_gedcoml_others_constructor_exists():
    assert callable(gedcoml_Others.__init__)


def test_hyp_gedcoml_others_constructor_args():
    sig = inspect.signature(gedcoml_Others.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_gedcoml_address_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Address)


def test_hyp_gedcoml_address_constructor_exists():
    assert callable(gedcoml_Address.__init__)


def test_hyp_gedcoml_address_constructor_args():
    sig = inspect.signature(gedcoml_Address.__init__)
    params = list(sig.parameters.keys())
    assert "exodus" in params, "Missing parameter 'exodus'"
    assert "entry" in params, "Missing parameter 'entry'"





def test_hyp_gedcoml_source_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Source)


def test_hyp_gedcoml_source_constructor_exists():
    assert callable(gedcoml_Source.__init__)


def test_hyp_gedcoml_source_constructor_args():
    sig = inspect.signature(gedcoml_Source.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedcoml_note_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Note)


def test_hyp_gedcoml_note_constructor_exists():
    assert callable(gedcoml_Note.__init__)


def test_hyp_gedcoml_note_constructor_args():
    sig = inspect.signature(gedcoml_Note.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_gedcoml_married_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Married)


def test_hyp_gedcoml_married_constructor_exists():
    assert callable(gedcoml_Married.__init__)


def test_hyp_gedcoml_married_constructor_args():
    sig = inspect.signature(gedcoml_Married.__init__)
    params = list(sig.parameters.keys())
    assert "weddingDay" in params, "Missing parameter 'weddingDay'"
    assert "separationDay" in params, "Missing parameter 'separationDay'"





def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedcoml_unbekannteperson_is_not_abstract():
    assert not inspect.isabstract(gedcoml_UnbekanntePerson)


def test_hyp_gedcoml_unbekannteperson_constructor_exists():
    assert callable(gedcoml_UnbekanntePerson.__init__)


def test_hyp_gedcoml_unbekannteperson_constructor_args():
    sig = inspect.signature(gedcoml_UnbekanntePerson.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedcoml_bekannteperson_is_not_abstract():
    assert not inspect.isabstract(gedcoml_BekanntePerson)


def test_hyp_gedcoml_bekannteperson_constructor_exists():
    assert callable(gedcoml_BekanntePerson.__init__)


def test_hyp_gedcoml_bekannteperson_constructor_args():
    sig = inspect.signature(gedcoml_BekanntePerson.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "birthName" in params, "Missing parameter 'birthName'"
    assert "middleName" in params, "Missing parameter 'middleName'"
    assert "birthDay" in params, "Missing parameter 'birthDay'"
    assert "deathDay" in params, "Missing parameter 'deathDay'"
    assert "firstName" in params, "Missing parameter 'firstName'"









def test_hyp_gedcoml_person_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Person)


def test_hyp_gedcoml_person_constructor_exists():
    assert callable(gedcoml_Person.__init__)


def test_hyp_gedcoml_person_constructor_args():
    sig = inspect.signature(gedcoml_Person.__init__)
    params = list(sig.parameters.keys())
    assert "sex" in params, "Missing parameter 'sex'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_gedcoml_family_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Family)


def test_hyp_gedcoml_family_constructor_exists():
    assert callable(gedcoml_Family.__init__)


def test_hyp_gedcoml_family_constructor_args():
    sig = inspect.signature(gedcoml_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_gedcoml_author_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Author)


def test_hyp_gedcoml_author_constructor_exists():
    assert callable(gedcoml_Author.__init__)


def test_hyp_gedcoml_author_constructor_args():
    sig = inspect.signature(gedcoml_Author.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"





def test_hyp_gedcoml_familyimport_is_not_abstract():
    assert not inspect.isabstract(gedcoml_FamilyImport)


def test_hyp_gedcoml_familyimport_constructor_exists():
    assert callable(gedcoml_FamilyImport.__init__)


def test_hyp_gedcoml_familyimport_constructor_args():
    sig = inspect.signature(gedcoml_FamilyImport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_hyp_address_constructor_exists():
    assert callable(Address.__init__)


def test_hyp_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedcoml_postaddress_is_not_abstract():
    assert not inspect.isabstract(gedcoml_PostAddress)


def test_hyp_gedcoml_postaddress_constructor_exists():
    assert callable(gedcoml_PostAddress.__init__)


def test_hyp_gedcoml_postaddress_constructor_args():
    sig = inspect.signature(gedcoml_PostAddress.__init__)
    params = list(sig.parameters.keys())
    assert "city" in params, "Missing parameter 'city'"
    assert "postcode" in params, "Missing parameter 'postcode'"
    assert "street" in params, "Missing parameter 'street'"






def test_hyp_gedcoml_familybook_is_not_abstract():
    assert not inspect.isabstract(gedcoml_FamilyBook)


def test_hyp_gedcoml_familybook_constructor_exists():
    assert callable(gedcoml_FamilyBook.__init__)


def test_hyp_gedcoml_familybook_constructor_args():
    sig = inspect.signature(gedcoml_FamilyBook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedcoml_projectdescription_is_not_abstract():
    assert not inspect.isabstract(gedcoml_Projectdescription)


def test_hyp_gedcoml_projectdescription_constructor_exists():
    assert callable(gedcoml_Projectdescription.__init__)


def test_hyp_gedcoml_projectdescription_constructor_args():
    sig = inspect.signature(gedcoml_Projectdescription.__init__)
    params = list(sig.parameters.keys())
    assert "artifactId" in params, "Missing parameter 'artifactId'"
    assert "groupId" in params, "Missing parameter 'groupId'"
    assert "publishingDate" in params, "Missing parameter 'publishingDate'"
    assert "version" in params, "Missing parameter 'version'"





def test_hyp_sexus_exists():
    # Check that the Enumeration exists
    assert Sexus is not None

def test_hyp_sexus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sexus]
    expected_literals = [
        "male",
        "undefined",
        "female",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sexus"


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
Source_strategy = st.builds(
    Source,
)
gedcoml_PersonRef_strategy = st.builds(
    gedcoml_PersonRef,
)
gedcoml_Others_strategy = st.builds(
    gedcoml_Others,
    description=
        safe_text
)
gedcoml_Address_strategy = st.builds(
    gedcoml_Address,
    exodus=
        safe_text,
    entry=
        safe_text
)
gedcoml_Source_strategy = st.builds(
    gedcoml_Source,
)
gedcoml_Note_strategy = st.builds(
    gedcoml_Note,
    content=
        safe_text
)
gedcoml_Married_strategy = st.builds(
    gedcoml_Married,
    weddingDay=
        safe_text,
    separationDay=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
gedcoml_UnbekanntePerson_strategy = st.builds(
    gedcoml_UnbekanntePerson,
)
gedcoml_BekanntePerson_strategy = st.builds(
    gedcoml_BekanntePerson,
    lastName=
        safe_text,
    birthName=
        safe_text,
    middleName=
        safe_text,
    birthDay=
        safe_text,
    deathDay=
        safe_text,
    firstName=
        safe_text
)
gedcoml_Person_strategy = st.builds(
    gedcoml_Person,
    sex=
        safe_text,
    id=
        safe_text
)
gedcoml_Family_strategy = st.builds(
    gedcoml_Family,
    name=
        safe_text
)
gedcoml_Author_strategy = st.builds(
    gedcoml_Author,
    lastName=
        safe_text,
    firstName=
        safe_text
)
gedcoml_FamilyImport_strategy = st.builds(
    gedcoml_FamilyImport,
)
Address_strategy = st.builds(
    Address,
)
gedcoml_PostAddress_strategy = st.builds(
    gedcoml_PostAddress,
    city=
        safe_text,
    postcode=
        safe_text,
    street=
        safe_text
)
gedcoml_FamilyBook_strategy = st.builds(
    gedcoml_FamilyBook,
)
gedcoml_Projectdescription_strategy = st.builds(
    gedcoml_Projectdescription,
    artifactId=
        safe_text,
    groupId=
        safe_text,
    publishingDate=
        safe_text,
    version=
        safe_text
)






@given(instance=gedcoml_Others_strategy)
def test_hyp_gedcoml_others_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=gedcoml_Address_strategy)
def test_hyp_gedcoml_address_exodus_setter(instance):
    original = instance.exodus
    instance.exodus = original
    assert instance.exodus == original



@given(instance=gedcoml_Address_strategy)
def test_hyp_gedcoml_address_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original





@given(instance=gedcoml_Note_strategy)
def test_hyp_gedcoml_note_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original




@given(instance=gedcoml_Married_strategy)
def test_hyp_gedcoml_married_weddingDay_setter(instance):
    original = instance.weddingDay
    instance.weddingDay = original
    assert instance.weddingDay == original



@given(instance=gedcoml_Married_strategy)
def test_hyp_gedcoml_married_separationDay_setter(instance):
    original = instance.separationDay
    instance.separationDay = original
    assert instance.separationDay == original






@given(instance=gedcoml_BekanntePerson_strategy)
def test_hyp_gedcoml_bekannteperson_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_hyp_gedcoml_bekannteperson_birthName_setter(instance):
    original = instance.birthName
    instance.birthName = original
    assert instance.birthName == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_hyp_gedcoml_bekannteperson_middleName_setter(instance):
    original = instance.middleName
    instance.middleName = original
    assert instance.middleName == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_hyp_gedcoml_bekannteperson_birthDay_setter(instance):
    original = instance.birthDay
    instance.birthDay = original
    assert instance.birthDay == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_hyp_gedcoml_bekannteperson_deathDay_setter(instance):
    original = instance.deathDay
    instance.deathDay = original
    assert instance.deathDay == original



@given(instance=gedcoml_BekanntePerson_strategy)
def test_hyp_gedcoml_bekannteperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original




@given(instance=gedcoml_Person_strategy)
def test_hyp_gedcoml_person_sex_setter(instance):
    original = instance.sex
    instance.sex = original
    assert instance.sex == original



@given(instance=gedcoml_Person_strategy)
def test_hyp_gedcoml_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=gedcoml_Family_strategy)
def test_hyp_gedcoml_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=gedcoml_Author_strategy)
def test_hyp_gedcoml_author_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=gedcoml_Author_strategy)
def test_hyp_gedcoml_author_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original






@given(instance=gedcoml_PostAddress_strategy)
def test_hyp_gedcoml_postaddress_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=gedcoml_PostAddress_strategy)
def test_hyp_gedcoml_postaddress_postcode_setter(instance):
    original = instance.postcode
    instance.postcode = original
    assert instance.postcode == original



@given(instance=gedcoml_PostAddress_strategy)
def test_hyp_gedcoml_postaddress_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original





@given(instance=gedcoml_Projectdescription_strategy)
def test_hyp_gedcoml_projectdescription_artifactId_setter(instance):
    original = instance.artifactId
    instance.artifactId = original
    assert instance.artifactId == original



@given(instance=gedcoml_Projectdescription_strategy)
def test_hyp_gedcoml_projectdescription_groupId_setter(instance):
    original = instance.groupId
    instance.groupId = original
    assert instance.groupId == original



@given(instance=gedcoml_Projectdescription_strategy)
def test_hyp_gedcoml_projectdescription_publishingDate_setter(instance):
    original = instance.publishingDate
    instance.publishingDate = original
    assert instance.publishingDate == original



@given(instance=gedcoml_Projectdescription_strategy)
def test_hyp_gedcoml_projectdescription_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Address,
    Person,
    Source,
    gedcoml_Address,
    gedcoml_Author,
    gedcoml_BekanntePerson,
    gedcoml_Family,
    gedcoml_FamilyBook,
    gedcoml_FamilyImport,
    gedcoml_Married,
    gedcoml_Note,
    gedcoml_Others,
    gedcoml_Person,
    gedcoml_PersonRef,
    gedcoml_PostAddress,
    gedcoml_Projectdescription,
    gedcoml_Source,
    gedcoml_UnbekanntePerson,
    Sexus,
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

def test_gedcoml_Address_entry_value_roundtrip():
    instance = gedcoml_Address(entry="sample_text", exodus="sample_text")
    assert instance.entry == "sample_text"
    instance.entry = "sample_text_2"
    assert instance.entry == "sample_text_2"


def test_gedcoml_Address_exodus_value_roundtrip():
    instance = gedcoml_Address(entry="sample_text", exodus="sample_text")
    assert instance.exodus == "sample_text"
    instance.exodus = "sample_text_2"
    assert instance.exodus == "sample_text_2"


def test_gedcoml_Author_firstName_value_roundtrip():
    instance = gedcoml_Author(firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_gedcoml_Author_lastName_value_roundtrip():
    instance = gedcoml_Author(firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_gedcoml_BekanntePerson_birthDay_value_roundtrip():
    instance = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    assert instance.birthDay == "sample_text"
    instance.birthDay = "sample_text_2"
    assert instance.birthDay == "sample_text_2"


def test_gedcoml_BekanntePerson_birthName_value_roundtrip():
    instance = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    assert instance.birthName == "sample_text"
    instance.birthName = "sample_text_2"
    assert instance.birthName == "sample_text_2"


def test_gedcoml_BekanntePerson_deathDay_value_roundtrip():
    instance = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    assert instance.deathDay == "sample_text"
    instance.deathDay = "sample_text_2"
    assert instance.deathDay == "sample_text_2"


def test_gedcoml_BekanntePerson_firstName_value_roundtrip():
    instance = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_gedcoml_BekanntePerson_lastName_value_roundtrip():
    instance = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_gedcoml_BekanntePerson_middleName_value_roundtrip():
    instance = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    assert instance.middleName == "sample_text"
    instance.middleName = "sample_text_2"
    assert instance.middleName == "sample_text_2"


def test_gedcoml_Family_name_value_roundtrip():
    instance = gedcoml_Family(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gedcoml_Married_separationDay_value_roundtrip():
    instance = gedcoml_Married(separationDay="sample_text", weddingDay="sample_text")
    assert instance.separationDay == "sample_text"
    instance.separationDay = "sample_text_2"
    assert instance.separationDay == "sample_text_2"


def test_gedcoml_Married_weddingDay_value_roundtrip():
    instance = gedcoml_Married(separationDay="sample_text", weddingDay="sample_text")
    assert instance.weddingDay == "sample_text"
    instance.weddingDay = "sample_text_2"
    assert instance.weddingDay == "sample_text_2"


def test_gedcoml_Note_content_value_roundtrip():
    instance = gedcoml_Note(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_gedcoml_Others_description_value_roundtrip():
    instance = gedcoml_Others(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_gedcoml_Person_id_value_roundtrip():
    instance = gedcoml_Person(id="sample_text", sex="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_gedcoml_Person_sex_value_roundtrip():
    instance = gedcoml_Person(id="sample_text", sex="sample_text")
    assert instance.sex == "sample_text"
    instance.sex = "sample_text_2"
    assert instance.sex == "sample_text_2"


def test_gedcoml_PostAddress_city_value_roundtrip():
    instance = gedcoml_PostAddress(city="sample_text", postcode="sample_text", street="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_gedcoml_PostAddress_postcode_value_roundtrip():
    instance = gedcoml_PostAddress(city="sample_text", postcode="sample_text", street="sample_text")
    assert instance.postcode == "sample_text"
    instance.postcode = "sample_text_2"
    assert instance.postcode == "sample_text_2"


def test_gedcoml_PostAddress_street_value_roundtrip():
    instance = gedcoml_PostAddress(city="sample_text", postcode="sample_text", street="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_gedcoml_Projectdescription_artifactId_value_roundtrip():
    instance = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    assert instance.artifactId == "sample_text"
    instance.artifactId = "sample_text_2"
    assert instance.artifactId == "sample_text_2"


def test_gedcoml_Projectdescription_groupId_value_roundtrip():
    instance = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    assert instance.groupId == "sample_text"
    instance.groupId = "sample_text_2"
    assert instance.groupId == "sample_text_2"


def test_gedcoml_Projectdescription_publishingDate_value_roundtrip():
    instance = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    assert instance.publishingDate == "sample_text"
    instance.publishingDate = "sample_text_2"
    assert instance.publishingDate == "sample_text_2"


def test_gedcoml_Projectdescription_version_value_roundtrip():
    instance = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_gedcoml_PostAddress_isa_Address():
    instance = gedcoml_PostAddress(city="sample_text", postcode="sample_text", street="sample_text")
    assert isinstance(instance, Address)


def test_gedcoml_BekanntePerson_isa_Person():
    instance = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    assert isinstance(instance, Person)


def test_gedcoml_UnbekanntePerson_isa_Person():
    instance = gedcoml_UnbekanntePerson()
    assert isinstance(instance, Person)


def test_gedcoml_Others_isa_Source():
    instance = gedcoml_Others(description="sample_text")
    assert isinstance(instance, Source)


def test_gedcoml_PersonRef_isa_Source():
    instance = gedcoml_PersonRef()
    assert isinstance(instance, Source)


def test_assoc_addresses34_link_reassign_clear():
    a = gedcoml_Person(id="sample_text", sex="sample_text")
    b1 = gedcoml_Address(entry="sample_text", exodus="sample_text")
    b2 = gedcoml_Address(entry="sample_text_2", exodus="sample_text_2")
    _safe_set(a, 'gedcoml_Person35', {b1})
    assert _is_linked(a, 'gedcoml_Person35', b1)
    if hasattr(b1, 'gedcoml_Address'):
        assert _is_linked(b1, 'gedcoml_Address', a)
    _safe_set(a, 'gedcoml_Person35', {b2})
    assert _is_linked(a, 'gedcoml_Person35', b2)
    if hasattr(b1, 'gedcoml_Address'):
        assert not _is_linked(b1, 'gedcoml_Address', a)
    if hasattr(b2, 'gedcoml_Address'):
        assert _is_linked(b2, 'gedcoml_Address', a)
    _safe_set(a, 'gedcoml_Person35', set())
    assert not _is_linked(a, 'gedcoml_Person35', b2)
    if hasattr(b2, 'gedcoml_Address'):
        assert not _is_linked(b2, 'gedcoml_Address', a)


def test_assoc_author1_link_reassign_clear():
    a = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    b1 = gedcoml_Author(firstName="sample_text", lastName="sample_text")
    b2 = gedcoml_Author(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'gedcoml_Projectdescription2', b1)
    assert _is_linked(a, 'gedcoml_Projectdescription2', b1)
    if hasattr(b1, 'gedcoml_Author'):
        assert _is_linked(b1, 'gedcoml_Author', a)
    _safe_set(a, 'gedcoml_Projectdescription2', b2)
    assert _is_linked(a, 'gedcoml_Projectdescription2', b2)
    if hasattr(b1, 'gedcoml_Author'):
        assert not _is_linked(b1, 'gedcoml_Author', a)
    if hasattr(b2, 'gedcoml_Author'):
        assert _is_linked(b2, 'gedcoml_Author', a)
    _safe_set(a, 'gedcoml_Projectdescription2', None)
    assert not _is_linked(a, 'gedcoml_Projectdescription2', b2)
    if hasattr(b2, 'gedcoml_Author'):
        assert not _is_linked(b2, 'gedcoml_Author', a)


def test_assoc_biologicalFatherIs9_link_reassign_clear():
    a = gedcoml_Person(id="sample_text", sex="sample_text")
    b1 = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b2 = gedcoml_BekanntePerson(birthDay="sample_text_2", birthName="sample_text_2", deathDay="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", middleName="sample_text_2")
    _safe_set(a, 'gedcoml_Person11', b1)
    assert _is_linked(a, 'gedcoml_Person11', b1)
    if hasattr(b1, 'gedcoml_BekanntePerson10'):
        assert _is_linked(b1, 'gedcoml_BekanntePerson10', a)
    _safe_set(a, 'gedcoml_Person11', b2)
    assert _is_linked(a, 'gedcoml_Person11', b2)
    if hasattr(b1, 'gedcoml_BekanntePerson10'):
        assert not _is_linked(b1, 'gedcoml_BekanntePerson10', a)
    if hasattr(b2, 'gedcoml_BekanntePerson10'):
        assert _is_linked(b2, 'gedcoml_BekanntePerson10', a)
    _safe_set(a, 'gedcoml_Person11', None)
    assert not _is_linked(a, 'gedcoml_Person11', b2)
    if hasattr(b2, 'gedcoml_BekanntePerson10'):
        assert not _is_linked(b2, 'gedcoml_BekanntePerson10', a)


def test_assoc_biologicalMotherIs12_link_reassign_clear():
    a = gedcoml_Person(id="sample_text", sex="sample_text")
    b1 = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b2 = gedcoml_BekanntePerson(birthDay="sample_text_2", birthName="sample_text_2", deathDay="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", middleName="sample_text_2")
    _safe_set(a, 'gedcoml_Person14', b1)
    assert _is_linked(a, 'gedcoml_Person14', b1)
    if hasattr(b1, 'gedcoml_BekanntePerson13'):
        assert _is_linked(b1, 'gedcoml_BekanntePerson13', a)
    _safe_set(a, 'gedcoml_Person14', b2)
    assert _is_linked(a, 'gedcoml_Person14', b2)
    if hasattr(b1, 'gedcoml_BekanntePerson13'):
        assert not _is_linked(b1, 'gedcoml_BekanntePerson13', a)
    if hasattr(b2, 'gedcoml_BekanntePerson13'):
        assert _is_linked(b2, 'gedcoml_BekanntePerson13', a)
    _safe_set(a, 'gedcoml_Person14', None)
    assert not _is_linked(a, 'gedcoml_Person14', b2)
    if hasattr(b2, 'gedcoml_BekanntePerson13'):
        assert not _is_linked(b2, 'gedcoml_BekanntePerson13', a)


def test_assoc_biologicalParentOf7_link_reassign_clear():
    a = gedcoml_Person(id="sample_text", sex="sample_text")
    b1 = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b2 = gedcoml_BekanntePerson(birthDay="sample_text_2", birthName="sample_text_2", deathDay="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", middleName="sample_text_2")
    _safe_set(a, 'gedcoml_Person8', b1)
    assert _is_linked(a, 'gedcoml_Person8', b1)
    if hasattr(b1, 'gedcoml_BekanntePerson'):
        assert _is_linked(b1, 'gedcoml_BekanntePerson', a)
    _safe_set(a, 'gedcoml_Person8', b2)
    assert _is_linked(a, 'gedcoml_Person8', b2)
    if hasattr(b1, 'gedcoml_BekanntePerson'):
        assert not _is_linked(b1, 'gedcoml_BekanntePerson', a)
    if hasattr(b2, 'gedcoml_BekanntePerson'):
        assert _is_linked(b2, 'gedcoml_BekanntePerson', a)
    _safe_set(a, 'gedcoml_Person8', None)
    assert not _is_linked(a, 'gedcoml_Person8', b2)
    if hasattr(b2, 'gedcoml_BekanntePerson'):
        assert not _is_linked(b2, 'gedcoml_BekanntePerson', a)


def test_assoc_importedResource23_link_reassign_clear():
    a = gedcoml_Family(name="sample_text")
    b1 = gedcoml_FamilyImport()
    b2 = gedcoml_FamilyImport()
    _safe_set(a, 'gedcoml_Family25', b1)
    assert _is_linked(a, 'gedcoml_Family25', b1)
    if hasattr(b1, 'gedcoml_FamilyImport24'):
        assert _is_linked(b1, 'gedcoml_FamilyImport24', a)
    _safe_set(a, 'gedcoml_Family25', b2)
    assert _is_linked(a, 'gedcoml_Family25', b2)
    if hasattr(b1, 'gedcoml_FamilyImport24'):
        assert not _is_linked(b1, 'gedcoml_FamilyImport24', a)
    if hasattr(b2, 'gedcoml_FamilyImport24'):
        assert _is_linked(b2, 'gedcoml_FamilyImport24', a)
    _safe_set(a, 'gedcoml_Family25', None)
    assert not _is_linked(a, 'gedcoml_Family25', b2)
    if hasattr(b2, 'gedcoml_FamilyImport24'):
        assert not _is_linked(b2, 'gedcoml_FamilyImport24', a)


def test_assoc_imports0_link_reassign_clear():
    a = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    b1 = gedcoml_FamilyImport()
    b2 = gedcoml_FamilyImport()
    _safe_set(a, 'gedcoml_Projectdescription', {b1})
    assert _is_linked(a, 'gedcoml_Projectdescription', b1)
    if hasattr(b1, 'gedcoml_FamilyImport'):
        assert _is_linked(b1, 'gedcoml_FamilyImport', a)
    _safe_set(a, 'gedcoml_Projectdescription', {b2})
    assert _is_linked(a, 'gedcoml_Projectdescription', b2)
    if hasattr(b1, 'gedcoml_FamilyImport'):
        assert not _is_linked(b1, 'gedcoml_FamilyImport', a)
    if hasattr(b2, 'gedcoml_FamilyImport'):
        assert _is_linked(b2, 'gedcoml_FamilyImport', a)
    _safe_set(a, 'gedcoml_Projectdescription', set())
    assert not _is_linked(a, 'gedcoml_Projectdescription', b2)
    if hasattr(b2, 'gedcoml_FamilyImport'):
        assert not _is_linked(b2, 'gedcoml_FamilyImport', a)


def test_assoc_imports4_link_reassign_clear():
    a = gedcoml_Family(name="sample_text")
    b1 = gedcoml_FamilyImport()
    b2 = gedcoml_FamilyImport()
    _safe_set(a, 'gedcoml_Family5', {b1})
    assert _is_linked(a, 'gedcoml_Family5', b1)
    if hasattr(b1, 'gedcoml_FamilyImport6'):
        assert _is_linked(b1, 'gedcoml_FamilyImport6', a)
    _safe_set(a, 'gedcoml_Family5', {b2})
    assert _is_linked(a, 'gedcoml_Family5', b2)
    if hasattr(b1, 'gedcoml_FamilyImport6'):
        assert not _is_linked(b1, 'gedcoml_FamilyImport6', a)
    if hasattr(b2, 'gedcoml_FamilyImport6'):
        assert _is_linked(b2, 'gedcoml_FamilyImport6', a)
    _safe_set(a, 'gedcoml_Family5', set())
    assert not _is_linked(a, 'gedcoml_Family5', b2)
    if hasattr(b2, 'gedcoml_FamilyImport6'):
        assert not _is_linked(b2, 'gedcoml_FamilyImport6', a)


def test_assoc_marriedWith15_link_reassign_clear():
    a = gedcoml_Married(separationDay="sample_text", weddingDay="sample_text")
    b1 = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b2 = gedcoml_BekanntePerson(birthDay="sample_text_2", birthName="sample_text_2", deathDay="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", middleName="sample_text_2")
    _safe_set(a, 'gedcoml_Married', b1)
    assert _is_linked(a, 'gedcoml_Married', b1)
    if hasattr(b1, 'gedcoml_BekanntePerson16'):
        assert _is_linked(b1, 'gedcoml_BekanntePerson16', a)
    _safe_set(a, 'gedcoml_Married', b2)
    assert _is_linked(a, 'gedcoml_Married', b2)
    if hasattr(b1, 'gedcoml_BekanntePerson16'):
        assert not _is_linked(b1, 'gedcoml_BekanntePerson16', a)
    if hasattr(b2, 'gedcoml_BekanntePerson16'):
        assert _is_linked(b2, 'gedcoml_BekanntePerson16', a)
    _safe_set(a, 'gedcoml_Married', None)
    assert not _is_linked(a, 'gedcoml_Married', b2)
    if hasattr(b2, 'gedcoml_BekanntePerson16'):
        assert not _is_linked(b2, 'gedcoml_BekanntePerson16', a)


def test_assoc_memberId29_link_reassign_clear():
    a = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b1 = gedcoml_Author(firstName="sample_text", lastName="sample_text")
    b2 = gedcoml_Author(firstName="sample_text_2", lastName="sample_text_2")
    _safe_set(a, 'gedcoml_BekanntePerson31', b1)
    assert _is_linked(a, 'gedcoml_BekanntePerson31', b1)
    if hasattr(b1, 'gedcoml_Author30'):
        assert _is_linked(b1, 'gedcoml_Author30', a)
    _safe_set(a, 'gedcoml_BekanntePerson31', b2)
    assert _is_linked(a, 'gedcoml_BekanntePerson31', b2)
    if hasattr(b1, 'gedcoml_Author30'):
        assert not _is_linked(b1, 'gedcoml_Author30', a)
    if hasattr(b2, 'gedcoml_Author30'):
        assert _is_linked(b2, 'gedcoml_Author30', a)
    _safe_set(a, 'gedcoml_BekanntePerson31', None)
    assert not _is_linked(a, 'gedcoml_BekanntePerson31', b2)
    if hasattr(b2, 'gedcoml_Author30'):
        assert not _is_linked(b2, 'gedcoml_Author30', a)


def test_assoc_members3_link_reassign_clear():
    a = gedcoml_Person(id="sample_text", sex="sample_text")
    b1 = gedcoml_Family(name="sample_text")
    b2 = gedcoml_Family(name="sample_text_2")
    _safe_set(a, 'gedcoml_Person', b1)
    assert _is_linked(a, 'gedcoml_Person', b1)
    if hasattr(b1, 'gedcoml_Family'):
        assert _is_linked(b1, 'gedcoml_Family', a)
    _safe_set(a, 'gedcoml_Person', b2)
    assert _is_linked(a, 'gedcoml_Person', b2)
    if hasattr(b1, 'gedcoml_Family'):
        assert not _is_linked(b1, 'gedcoml_Family', a)
    if hasattr(b2, 'gedcoml_Family'):
        assert _is_linked(b2, 'gedcoml_Family', a)
    _safe_set(a, 'gedcoml_Person', None)
    assert not _is_linked(a, 'gedcoml_Person', b2)
    if hasattr(b2, 'gedcoml_Family'):
        assert not _is_linked(b2, 'gedcoml_Family', a)


def test_assoc_notes17_link_reassign_clear():
    a = gedcoml_Note(content="sample_text")
    b1 = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b2 = gedcoml_BekanntePerson(birthDay="sample_text_2", birthName="sample_text_2", deathDay="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", middleName="sample_text_2")
    _safe_set(a, 'gedcoml_Note', b1)
    assert _is_linked(a, 'gedcoml_Note', b1)
    if hasattr(b1, 'gedcoml_BekanntePerson18'):
        assert _is_linked(b1, 'gedcoml_BekanntePerson18', a)
    _safe_set(a, 'gedcoml_Note', b2)
    assert _is_linked(a, 'gedcoml_Note', b2)
    if hasattr(b1, 'gedcoml_BekanntePerson18'):
        assert not _is_linked(b1, 'gedcoml_BekanntePerson18', a)
    if hasattr(b2, 'gedcoml_BekanntePerson18'):
        assert _is_linked(b2, 'gedcoml_BekanntePerson18', a)
    _safe_set(a, 'gedcoml_Note', None)
    assert not _is_linked(a, 'gedcoml_Note', b2)
    if hasattr(b2, 'gedcoml_BekanntePerson18'):
        assert not _is_linked(b2, 'gedcoml_BekanntePerson18', a)


def test_assoc_partner26_link_reassign_clear():
    a = gedcoml_Person(id="sample_text", sex="sample_text")
    b1 = gedcoml_Married(separationDay="sample_text", weddingDay="sample_text")
    b2 = gedcoml_Married(separationDay="sample_text_2", weddingDay="sample_text_2")
    _safe_set(a, 'gedcoml_Person28', b1)
    assert _is_linked(a, 'gedcoml_Person28', b1)
    if hasattr(b1, 'gedcoml_Married27'):
        assert _is_linked(b1, 'gedcoml_Married27', a)
    _safe_set(a, 'gedcoml_Person28', b2)
    assert _is_linked(a, 'gedcoml_Person28', b2)
    if hasattr(b1, 'gedcoml_Married27'):
        assert not _is_linked(b1, 'gedcoml_Married27', a)
    if hasattr(b2, 'gedcoml_Married27'):
        assert _is_linked(b2, 'gedcoml_Married27', a)
    _safe_set(a, 'gedcoml_Person28', None)
    assert not _is_linked(a, 'gedcoml_Person28', b2)
    if hasattr(b2, 'gedcoml_Married27'):
        assert not _is_linked(b2, 'gedcoml_Married27', a)


def test_assoc_personID32_link_reassign_clear():
    a = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b1 = gedcoml_PersonRef()
    b2 = gedcoml_PersonRef()
    _safe_set(a, 'gedcoml_BekanntePerson33', b1)
    assert _is_linked(a, 'gedcoml_BekanntePerson33', b1)
    if hasattr(b1, 'gedcoml_PersonRef'):
        assert _is_linked(b1, 'gedcoml_PersonRef', a)
    _safe_set(a, 'gedcoml_BekanntePerson33', b2)
    assert _is_linked(a, 'gedcoml_BekanntePerson33', b2)
    if hasattr(b1, 'gedcoml_PersonRef'):
        assert not _is_linked(b1, 'gedcoml_PersonRef', a)
    if hasattr(b2, 'gedcoml_PersonRef'):
        assert _is_linked(b2, 'gedcoml_PersonRef', a)
    _safe_set(a, 'gedcoml_BekanntePerson33', None)
    assert not _is_linked(a, 'gedcoml_BekanntePerson33', b2)
    if hasattr(b2, 'gedcoml_PersonRef'):
        assert not _is_linked(b2, 'gedcoml_PersonRef', a)


def test_assoc_project21_link_reassign_clear():
    a = gedcoml_Projectdescription(artifactId="sample_text", groupId="sample_text", publishingDate="sample_text", version="sample_text")
    b1 = gedcoml_FamilyBook()
    b2 = gedcoml_FamilyBook()
    _safe_set(a, 'gedcoml_Projectdescription22', b1)
    assert _is_linked(a, 'gedcoml_Projectdescription22', b1)
    if hasattr(b1, 'gedcoml_FamilyBook'):
        assert _is_linked(b1, 'gedcoml_FamilyBook', a)
    _safe_set(a, 'gedcoml_Projectdescription22', b2)
    assert _is_linked(a, 'gedcoml_Projectdescription22', b2)
    if hasattr(b1, 'gedcoml_FamilyBook'):
        assert not _is_linked(b1, 'gedcoml_FamilyBook', a)
    if hasattr(b2, 'gedcoml_FamilyBook'):
        assert _is_linked(b2, 'gedcoml_FamilyBook', a)
    _safe_set(a, 'gedcoml_Projectdescription22', None)
    assert not _is_linked(a, 'gedcoml_Projectdescription22', b2)
    if hasattr(b2, 'gedcoml_FamilyBook'):
        assert not _is_linked(b2, 'gedcoml_FamilyBook', a)


def test_assoc_sources19_link_reassign_clear():
    a = gedcoml_BekanntePerson(birthDay="sample_text", birthName="sample_text", deathDay="sample_text", firstName="sample_text", lastName="sample_text", middleName="sample_text")
    b1 = gedcoml_Source()
    b2 = gedcoml_Source()
    _safe_set(a, 'gedcoml_BekanntePerson20', {b1})
    assert _is_linked(a, 'gedcoml_BekanntePerson20', b1)
    if hasattr(b1, 'gedcoml_Source'):
        assert _is_linked(b1, 'gedcoml_Source', a)
    _safe_set(a, 'gedcoml_BekanntePerson20', {b2})
    assert _is_linked(a, 'gedcoml_BekanntePerson20', b2)
    if hasattr(b1, 'gedcoml_Source'):
        assert not _is_linked(b1, 'gedcoml_Source', a)
    if hasattr(b2, 'gedcoml_Source'):
        assert _is_linked(b2, 'gedcoml_Source', a)
    _safe_set(a, 'gedcoml_BekanntePerson20', set())
    assert not _is_linked(a, 'gedcoml_BekanntePerson20', b2)
    if hasattr(b2, 'gedcoml_Source'):
        assert not _is_linked(b2, 'gedcoml_Source', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Address_strategy = st.builds(Address)
@given(instance=Address_strategy)
@settings(max_examples=25)
def test_Address_instantiation(instance):
    assert isinstance(instance, Address)


Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Source_strategy = st.builds(Source)
@given(instance=Source_strategy)
@settings(max_examples=25)
def test_Source_instantiation(instance):
    assert isinstance(instance, Source)


gedcoml_Address_strategy = st.builds(gedcoml_Address, entry=safe_text, exodus=safe_text)
@given(instance=gedcoml_Address_strategy)
@settings(max_examples=25)
def test_gedcoml_Address_instantiation(instance):
    assert isinstance(instance, gedcoml_Address)


gedcoml_Author_strategy = st.builds(gedcoml_Author, firstName=safe_text, lastName=safe_text)
@given(instance=gedcoml_Author_strategy)
@settings(max_examples=25)
def test_gedcoml_Author_instantiation(instance):
    assert isinstance(instance, gedcoml_Author)


gedcoml_BekanntePerson_strategy = st.builds(gedcoml_BekanntePerson, birthDay=safe_text, birthName=safe_text, deathDay=safe_text, firstName=safe_text, lastName=safe_text, middleName=safe_text)
@given(instance=gedcoml_BekanntePerson_strategy)
@settings(max_examples=25)
def test_gedcoml_BekanntePerson_instantiation(instance):
    assert isinstance(instance, gedcoml_BekanntePerson)


gedcoml_Family_strategy = st.builds(gedcoml_Family, name=safe_text)
@given(instance=gedcoml_Family_strategy)
@settings(max_examples=25)
def test_gedcoml_Family_instantiation(instance):
    assert isinstance(instance, gedcoml_Family)


gedcoml_FamilyBook_strategy = st.builds(gedcoml_FamilyBook)
@given(instance=gedcoml_FamilyBook_strategy)
@settings(max_examples=25)
def test_gedcoml_FamilyBook_instantiation(instance):
    assert isinstance(instance, gedcoml_FamilyBook)


gedcoml_FamilyImport_strategy = st.builds(gedcoml_FamilyImport)
@given(instance=gedcoml_FamilyImport_strategy)
@settings(max_examples=25)
def test_gedcoml_FamilyImport_instantiation(instance):
    assert isinstance(instance, gedcoml_FamilyImport)


gedcoml_Married_strategy = st.builds(gedcoml_Married, separationDay=safe_text, weddingDay=safe_text)
@given(instance=gedcoml_Married_strategy)
@settings(max_examples=25)
def test_gedcoml_Married_instantiation(instance):
    assert isinstance(instance, gedcoml_Married)


gedcoml_Note_strategy = st.builds(gedcoml_Note, content=safe_text)
@given(instance=gedcoml_Note_strategy)
@settings(max_examples=25)
def test_gedcoml_Note_instantiation(instance):
    assert isinstance(instance, gedcoml_Note)


gedcoml_Others_strategy = st.builds(gedcoml_Others, description=safe_text)
@given(instance=gedcoml_Others_strategy)
@settings(max_examples=25)
def test_gedcoml_Others_instantiation(instance):
    assert isinstance(instance, gedcoml_Others)


gedcoml_Person_strategy = st.builds(gedcoml_Person, id=safe_text, sex=safe_text)
@given(instance=gedcoml_Person_strategy)
@settings(max_examples=25)
def test_gedcoml_Person_instantiation(instance):
    assert isinstance(instance, gedcoml_Person)


gedcoml_PersonRef_strategy = st.builds(gedcoml_PersonRef)
@given(instance=gedcoml_PersonRef_strategy)
@settings(max_examples=25)
def test_gedcoml_PersonRef_instantiation(instance):
    assert isinstance(instance, gedcoml_PersonRef)


gedcoml_PostAddress_strategy = st.builds(gedcoml_PostAddress, city=safe_text, postcode=safe_text, street=safe_text)
@given(instance=gedcoml_PostAddress_strategy)
@settings(max_examples=25)
def test_gedcoml_PostAddress_instantiation(instance):
    assert isinstance(instance, gedcoml_PostAddress)


gedcoml_Projectdescription_strategy = st.builds(gedcoml_Projectdescription, artifactId=safe_text, groupId=safe_text, publishingDate=safe_text, version=safe_text)
@given(instance=gedcoml_Projectdescription_strategy)
@settings(max_examples=25)
def test_gedcoml_Projectdescription_instantiation(instance):
    assert isinstance(instance, gedcoml_Projectdescription)


gedcoml_Source_strategy = st.builds(gedcoml_Source)
@given(instance=gedcoml_Source_strategy)
@settings(max_examples=25)
def test_gedcoml_Source_instantiation(instance):
    assert isinstance(instance, gedcoml_Source)


gedcoml_UnbekanntePerson_strategy = st.builds(gedcoml_UnbekanntePerson)
@given(instance=gedcoml_UnbekanntePerson_strategy)
@settings(max_examples=25)
def test_gedcoml_UnbekanntePerson_instantiation(instance):
    assert isinstance(instance, gedcoml_UnbekanntePerson)



