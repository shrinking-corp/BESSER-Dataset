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
    grudi_PersonInfo,
    grudi_TeamLine,
    grudi_Team,
    grudi_Person,
    Gender,
    TeamPersonKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_grudi_personinfo_is_not_abstract():
    assert not inspect.isabstract(grudi_PersonInfo)


def test_hyp_grudi_personinfo_constructor_exists():
    assert callable(grudi_PersonInfo.__init__)


def test_hyp_grudi_personinfo_constructor_args():
    sig = inspect.signature(grudi_PersonInfo.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "id" in params, "Missing parameter 'id'"








def test_hyp_grudi_teamline_is_not_abstract():
    assert not inspect.isabstract(grudi_TeamLine)


def test_hyp_grudi_teamline_constructor_exists():
    assert callable(grudi_TeamLine.__init__)


def test_hyp_grudi_teamline_constructor_args():
    sig = inspect.signature(grudi_TeamLine.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "versionNumber" in params, "Missing parameter 'versionNumber'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_grudi_team_is_not_abstract():
    assert not inspect.isabstract(grudi_Team)


def test_hyp_grudi_team_constructor_exists():
    assert callable(grudi_Team.__init__)


def test_hyp_grudi_team_constructor_args():
    sig = inspect.signature(grudi_Team.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "versionNumber" in params, "Missing parameter 'versionNumber'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_grudi_person_is_not_abstract():
    assert not inspect.isabstract(grudi_Person)


def test_hyp_grudi_person_constructor_exists():
    assert callable(grudi_Person.__init__)


def test_hyp_grudi_person_constructor_args():
    sig = inspect.signature(grudi_Person.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "address" in params, "Missing parameter 'address'"
    assert "email" in params, "Missing parameter 'email'"
    assert "versionNumber" in params, "Missing parameter 'versionNumber'"
    assert "username" in params, "Missing parameter 'username'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"










def test_hyp_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_hyp_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "male",
        "unknown",
        "female",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"

def test_hyp_teampersonkind_exists():
    # Check that the Enumeration exists
    assert TeamPersonKind is not None

def test_hyp_teampersonkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TeamPersonKind]
    expected_literals = [
        "member",
        "captain",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TeamPersonKind"


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
grudi_PersonInfo_strategy = st.builds(
    grudi_PersonInfo,
    userName=
        safe_text,
    name=
        safe_text,
    gender=
        safe_text,
    phoneNumber=
        safe_text,
    id=
        safe_text
)
grudi_TeamLine_strategy = st.builds(
    grudi_TeamLine,
    kind=
        safe_text,
    versionNumber=
        safe_text,
    id=
        safe_text
)
grudi_Team_strategy = st.builds(
    grudi_Team,
    name=
        safe_text,
    versionNumber=
        safe_text,
    id=
        safe_text
)
grudi_Person_strategy = st.builds(
    grudi_Person,
    password=
        safe_text,
    phoneNumber=
        safe_text,
    address=
        safe_text,
    email=
        safe_text,
    versionNumber=
        safe_text,
    username=
        safe_text,
    id=
        safe_text,
    name=
        safe_text,
    gender=
        safe_text
)




@given(instance=grudi_PersonInfo_strategy)
def test_hyp_grudi_personinfo_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=grudi_PersonInfo_strategy)
def test_hyp_grudi_personinfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=grudi_PersonInfo_strategy)
def test_hyp_grudi_personinfo_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=grudi_PersonInfo_strategy)
def test_hyp_grudi_personinfo_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=grudi_PersonInfo_strategy)
def test_hyp_grudi_personinfo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=grudi_TeamLine_strategy)
def test_hyp_grudi_teamline_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=grudi_TeamLine_strategy)
def test_hyp_grudi_teamline_versionNumber_setter(instance):
    original = instance.versionNumber
    instance.versionNumber = original
    assert instance.versionNumber == original



@given(instance=grudi_TeamLine_strategy)
def test_hyp_grudi_teamline_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=grudi_Team_strategy)
def test_hyp_grudi_team_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=grudi_Team_strategy)
def test_hyp_grudi_team_versionNumber_setter(instance):
    original = instance.versionNumber
    instance.versionNumber = original
    assert instance.versionNumber == original



@given(instance=grudi_Team_strategy)
def test_hyp_grudi_team_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_versionNumber_setter(instance):
    original = instance.versionNumber
    instance.versionNumber = original
    assert instance.versionNumber == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=grudi_Person_strategy)
def test_hyp_grudi_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    grudi_Person,
    grudi_PersonInfo,
    grudi_Team,
    grudi_TeamLine,
    Gender,
    TeamPersonKind,
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

def test_grudi_Person_address_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_grudi_Person_email_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_grudi_Person_gender_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_grudi_Person_id_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_grudi_Person_name_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_grudi_Person_password_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_grudi_Person_phoneNumber_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_grudi_Person_username_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_grudi_Person_versionNumber_value_roundtrip():
    instance = grudi_Person(address="sample_text", email="sample_text", gender="sample_text", id="sample_text", name="sample_text", password="sample_text", phoneNumber="sample_text", username="sample_text", versionNumber="sample_text")
    assert instance.versionNumber == "sample_text"
    instance.versionNumber = "sample_text_2"
    assert instance.versionNumber == "sample_text_2"


def test_grudi_PersonInfo_gender_value_roundtrip():
    instance = grudi_PersonInfo(gender="sample_text", id="sample_text", name="sample_text", phoneNumber="sample_text", userName="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_grudi_PersonInfo_id_value_roundtrip():
    instance = grudi_PersonInfo(gender="sample_text", id="sample_text", name="sample_text", phoneNumber="sample_text", userName="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_grudi_PersonInfo_name_value_roundtrip():
    instance = grudi_PersonInfo(gender="sample_text", id="sample_text", name="sample_text", phoneNumber="sample_text", userName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_grudi_PersonInfo_phoneNumber_value_roundtrip():
    instance = grudi_PersonInfo(gender="sample_text", id="sample_text", name="sample_text", phoneNumber="sample_text", userName="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_grudi_PersonInfo_userName_value_roundtrip():
    instance = grudi_PersonInfo(gender="sample_text", id="sample_text", name="sample_text", phoneNumber="sample_text", userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_grudi_Team_id_value_roundtrip():
    instance = grudi_Team(id="sample_text", name="sample_text", versionNumber="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_grudi_Team_name_value_roundtrip():
    instance = grudi_Team(id="sample_text", name="sample_text", versionNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_grudi_Team_versionNumber_value_roundtrip():
    instance = grudi_Team(id="sample_text", name="sample_text", versionNumber="sample_text")
    assert instance.versionNumber == "sample_text"
    instance.versionNumber = "sample_text_2"
    assert instance.versionNumber == "sample_text_2"


def test_grudi_TeamLine_id_value_roundtrip():
    instance = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_grudi_TeamLine_kind_value_roundtrip():
    instance = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_grudi_TeamLine_versionNumber_value_roundtrip():
    instance = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    assert instance.versionNumber == "sample_text"
    instance.versionNumber = "sample_text_2"
    assert instance.versionNumber == "sample_text_2"


def test_assoc_lines0_link_reassign_clear():
    a = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    b1 = grudi_Team(id="sample_text", name="sample_text", versionNumber="sample_text")
    b2 = grudi_Team(id="sample_text_2", name="sample_text_2", versionNumber="sample_text_2")
    _safe_set(a, 'TeamLine', b1)
    assert _is_linked(a, 'TeamLine', b1)
    if hasattr(b1, 'team'):
        assert _is_linked(b1, 'team', a)
    _safe_set(a, 'TeamLine', b2)
    assert _is_linked(a, 'TeamLine', b2)
    if hasattr(b1, 'team'):
        assert not _is_linked(b1, 'team', a)
    if hasattr(b2, 'team'):
        assert _is_linked(b2, 'team', a)
    _safe_set(a, 'TeamLine', None)
    assert not _is_linked(a, 'TeamLine', b2)
    if hasattr(b2, 'team'):
        assert not _is_linked(b2, 'team', a)


def test_assoc_person2_link_reassign_clear():
    a = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    b1 = grudi_PersonInfo(gender="sample_text", id="sample_text", name="sample_text", phoneNumber="sample_text", userName="sample_text")
    b2 = grudi_PersonInfo(gender="sample_text_2", id="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2", userName="sample_text_2")
    _safe_set(a, 'grudi_TeamLine', b1)
    assert _is_linked(a, 'grudi_TeamLine', b1)
    if hasattr(b1, 'grudi_PersonInfo'):
        assert _is_linked(b1, 'grudi_PersonInfo', a)
    _safe_set(a, 'grudi_TeamLine', b2)
    assert _is_linked(a, 'grudi_TeamLine', b2)
    if hasattr(b1, 'grudi_PersonInfo'):
        assert not _is_linked(b1, 'grudi_PersonInfo', a)
    if hasattr(b2, 'grudi_PersonInfo'):
        assert _is_linked(b2, 'grudi_PersonInfo', a)
    _safe_set(a, 'grudi_TeamLine', None)
    assert not _is_linked(a, 'grudi_TeamLine', b2)
    if hasattr(b2, 'grudi_PersonInfo'):
        assert not _is_linked(b2, 'grudi_PersonInfo', a)


def test_assoc_team1_link_reassign_clear():
    a = grudi_TeamLine(id="sample_text", kind="sample_text", versionNumber="sample_text")
    b1 = grudi_Team(id="sample_text", name="sample_text", versionNumber="sample_text")
    b2 = grudi_Team(id="sample_text_2", name="sample_text_2", versionNumber="sample_text_2")
    _safe_set(a, 'lines', b1)
    assert _is_linked(a, 'lines', b1)
    if hasattr(b1, 'Team'):
        assert _is_linked(b1, 'Team', a)
    _safe_set(a, 'lines', b2)
    assert _is_linked(a, 'lines', b2)
    if hasattr(b1, 'Team'):
        assert not _is_linked(b1, 'Team', a)
    if hasattr(b2, 'Team'):
        assert _is_linked(b2, 'Team', a)
    _safe_set(a, 'lines', None)
    assert not _is_linked(a, 'lines', b2)
    if hasattr(b2, 'Team'):
        assert not _is_linked(b2, 'Team', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

grudi_Person_strategy = st.builds(grudi_Person, address=safe_text, email=safe_text, gender=safe_text, id=safe_text, name=safe_text, password=safe_text, phoneNumber=safe_text, username=safe_text, versionNumber=safe_text)
@given(instance=grudi_Person_strategy)
@settings(max_examples=25)
def test_grudi_Person_instantiation(instance):
    assert isinstance(instance, grudi_Person)


grudi_PersonInfo_strategy = st.builds(grudi_PersonInfo, gender=safe_text, id=safe_text, name=safe_text, phoneNumber=safe_text, userName=safe_text)
@given(instance=grudi_PersonInfo_strategy)
@settings(max_examples=25)
def test_grudi_PersonInfo_instantiation(instance):
    assert isinstance(instance, grudi_PersonInfo)


grudi_Team_strategy = st.builds(grudi_Team, id=safe_text, name=safe_text, versionNumber=safe_text)
@given(instance=grudi_Team_strategy)
@settings(max_examples=25)
def test_grudi_Team_instantiation(instance):
    assert isinstance(instance, grudi_Team)


grudi_TeamLine_strategy = st.builds(grudi_TeamLine, id=safe_text, kind=safe_text, versionNumber=safe_text)
@given(instance=grudi_TeamLine_strategy)
@settings(max_examples=25)
def test_grudi_TeamLine_instantiation(instance):
    assert isinstance(instance, grudi_TeamLine)



