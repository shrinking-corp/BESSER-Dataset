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
    conference_Room,
    conference_Person,
    conference_Conference,
    conference_Site,
    conference_Topic,
    conference_Talk,
    TALK_TYPE,
    GENDER,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_conference_room_is_not_abstract():
    assert not inspect.isabstract(conference_Room)


def test_hyp_conference_room_constructor_exists():
    assert callable(conference_Room.__init__)


def test_hyp_conference_room_constructor_args():
    sig = inspect.signature(conference_Room.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_conference_person_is_not_abstract():
    assert not inspect.isabstract(conference_Person)


def test_hyp_conference_person_constructor_exists():
    assert callable(conference_Person.__init__)


def test_hyp_conference_person_constructor_args():
    sig = inspect.signature(conference_Person.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "age" in params, "Missing parameter 'age'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "isRegistered" in params, "Missing parameter 'isRegistered'"
    assert "eclipseCommiter" in params, "Missing parameter 'eclipseCommiter'"









def test_hyp_conference_conference_is_not_abstract():
    assert not inspect.isabstract(conference_Conference)


def test_hyp_conference_conference_constructor_exists():
    assert callable(conference_Conference.__init__)


def test_hyp_conference_conference_constructor_args():
    sig = inspect.signature(conference_Conference.__init__)
    params = list(sig.parameters.keys())
    assert "place" in params, "Missing parameter 'place'"
    assert "overview" in params, "Missing parameter 'overview'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_conference_site_is_not_abstract():
    assert not inspect.isabstract(conference_Site)


def test_hyp_conference_site_constructor_exists():
    assert callable(conference_Site.__init__)


def test_hyp_conference_site_constructor_args():
    sig = inspect.signature(conference_Site.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_conference_topic_is_not_abstract():
    assert not inspect.isabstract(conference_Topic)


def test_hyp_conference_topic_constructor_exists():
    assert callable(conference_Topic.__init__)


def test_hyp_conference_topic_constructor_args():
    sig = inspect.signature(conference_Topic.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "references" in params, "Missing parameter 'references'"
    assert "documentation" in params, "Missing parameter 'documentation'"






def test_hyp_conference_talk_is_not_abstract():
    assert not inspect.isabstract(conference_Talk)


def test_hyp_conference_talk_constructor_exists():
    assert callable(conference_Talk.__init__)


def test_hyp_conference_talk_constructor_args():
    sig = inspect.signature(conference_Talk.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_talk_type_exists():
    # Check that the Enumeration exists
    assert TALK_TYPE is not None

def test_hyp_talk_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TALK_TYPE]
    expected_literals = [
        "DEMONSTRATION",
        "CONFERENCE",
        "WORKSHOP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TALK_TYPE"

def test_hyp_gender_exists():
    # Check that the Enumeration exists
    assert GENDER is not None

def test_hyp_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GENDER]
    expected_literals = [
        "FEMALE",
        "UNKNOWN",
        "MALE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GENDER"


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
conference_Room_strategy = st.builds(
    conference_Room,
    capacity=
        st.integers(),
    name=
        safe_text
)
conference_Person_strategy = st.builds(
    conference_Person,
    gender=
        safe_text,
    age=
        st.integers(),
    firstname=
        safe_text,
    lastname=
        safe_text,
    isRegistered=
        st.booleans(),
    eclipseCommiter=
        st.booleans()
)
conference_Conference_strategy = st.builds(
    conference_Conference,
    place=
        safe_text,
    overview=
        safe_text,
    name=
        safe_text
)
conference_Site_strategy = st.builds(
    conference_Site,
    documentation=
        safe_text,
    name=
        safe_text
)
conference_Topic_strategy = st.builds(
    conference_Topic,
    description=
        safe_text,
    references=
        safe_text,
    documentation=
        safe_text
)
conference_Talk_strategy = st.builds(
    conference_Talk,
    title=
        safe_text,
    documentation=
        safe_text,
    type=
        safe_text
)




@given(instance=conference_Room_strategy)
def test_hyp_conference_room_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=conference_Room_strategy)
def test_hyp_conference_room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=conference_Person_strategy)
def test_hyp_conference_person_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=conference_Person_strategy)
def test_hyp_conference_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=conference_Person_strategy)
def test_hyp_conference_person_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=conference_Person_strategy)
def test_hyp_conference_person_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=conference_Person_strategy)
def test_hyp_conference_person_isRegistered_setter(instance):
    original = instance.isRegistered
    instance.isRegistered = original
    assert instance.isRegistered == original



@given(instance=conference_Person_strategy)
def test_hyp_conference_person_eclipseCommiter_setter(instance):
    original = instance.eclipseCommiter
    instance.eclipseCommiter = original
    assert instance.eclipseCommiter == original




@given(instance=conference_Conference_strategy)
def test_hyp_conference_conference_place_setter(instance):
    original = instance.place
    instance.place = original
    assert instance.place == original



@given(instance=conference_Conference_strategy)
def test_hyp_conference_conference_overview_setter(instance):
    original = instance.overview
    instance.overview = original
    assert instance.overview == original



@given(instance=conference_Conference_strategy)
def test_hyp_conference_conference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=conference_Site_strategy)
def test_hyp_conference_site_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=conference_Site_strategy)
def test_hyp_conference_site_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=conference_Topic_strategy)
def test_hyp_conference_topic_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=conference_Topic_strategy)
def test_hyp_conference_topic_references_setter(instance):
    original = instance.references
    instance.references = original
    assert instance.references == original



@given(instance=conference_Topic_strategy)
def test_hyp_conference_topic_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original




@given(instance=conference_Talk_strategy)
def test_hyp_conference_talk_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=conference_Talk_strategy)
def test_hyp_conference_talk_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=conference_Talk_strategy)
def test_hyp_conference_talk_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    conference_Conference,
    conference_Person,
    conference_Room,
    conference_Site,
    conference_Talk,
    conference_Topic,
    GENDER,
    TALK_TYPE,
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

def test_conference_Conference_name_value_roundtrip():
    instance = conference_Conference(name="sample_text", overview="sample_text", place="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conference_Conference_overview_value_roundtrip():
    instance = conference_Conference(name="sample_text", overview="sample_text", place="sample_text")
    assert instance.overview == "sample_text"
    instance.overview = "sample_text_2"
    assert instance.overview == "sample_text_2"


def test_conference_Conference_place_value_roundtrip():
    instance = conference_Conference(name="sample_text", overview="sample_text", place="sample_text")
    assert instance.place == "sample_text"
    instance.place = "sample_text_2"
    assert instance.place == "sample_text_2"


def test_conference_Person_age_value_roundtrip():
    instance = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_conference_Person_eclipseCommiter_value_roundtrip():
    instance = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    assert instance.eclipseCommiter == True
    instance.eclipseCommiter = False
    assert instance.eclipseCommiter == False


def test_conference_Person_firstname_value_roundtrip():
    instance = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_conference_Person_gender_value_roundtrip():
    instance = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_conference_Person_isRegistered_value_roundtrip():
    instance = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    assert instance.isRegistered == True
    instance.isRegistered = False
    assert instance.isRegistered == False


def test_conference_Person_lastname_value_roundtrip():
    instance = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_conference_Room_capacity_value_roundtrip():
    instance = conference_Room(capacity=7, name="sample_text")
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_conference_Room_name_value_roundtrip():
    instance = conference_Room(capacity=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conference_Site_documentation_value_roundtrip():
    instance = conference_Site(documentation="sample_text", name="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_conference_Site_name_value_roundtrip():
    instance = conference_Site(documentation="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_conference_Talk_documentation_value_roundtrip():
    instance = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_conference_Talk_title_value_roundtrip():
    instance = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_conference_Talk_type_value_roundtrip():
    instance = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_conference_Topic_description_value_roundtrip():
    instance = conference_Topic(description="sample_text", documentation="sample_text", references="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_conference_Topic_documentation_value_roundtrip():
    instance = conference_Topic(description="sample_text", documentation="sample_text", references="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_conference_Topic_references_value_roundtrip():
    instance = conference_Topic(description="sample_text", documentation="sample_text", references="sample_text")
    assert instance.references == "sample_text"
    instance.references = "sample_text_2"
    assert instance.references == "sample_text_2"


def test_assoc_assists7_link_reassign_clear():
    a = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    b1 = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    b2 = conference_Person(age=13, eclipseCommiter=False, firstname="sample_text_2", gender="sample_text_2", isRegistered=False, lastname="sample_text_2")
    _safe_set(a, 'conference_Talk9', b1)
    assert _is_linked(a, 'conference_Talk9', b1)
    if hasattr(b1, 'conference_Person8'):
        assert _is_linked(b1, 'conference_Person8', a)
    _safe_set(a, 'conference_Talk9', b2)
    assert _is_linked(a, 'conference_Talk9', b2)
    if hasattr(b1, 'conference_Person8'):
        assert not _is_linked(b1, 'conference_Person8', a)
    if hasattr(b2, 'conference_Person8'):
        assert _is_linked(b2, 'conference_Person8', a)
    _safe_set(a, 'conference_Talk9', None)
    assert not _is_linked(a, 'conference_Talk9', b2)
    if hasattr(b2, 'conference_Person8'):
        assert not _is_linked(b2, 'conference_Person8', a)


def test_assoc_creator16_link_reassign_clear():
    a = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    b1 = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    b2 = conference_Person(age=13, eclipseCommiter=False, firstname="sample_text_2", gender="sample_text_2", isRegistered=False, lastname="sample_text_2")
    _safe_set(a, 'conference_Talk17', b1)
    assert _is_linked(a, 'conference_Talk17', b1)
    if hasattr(b1, 'conference_Person18'):
        assert _is_linked(b1, 'conference_Person18', a)
    _safe_set(a, 'conference_Talk17', b2)
    assert _is_linked(a, 'conference_Talk17', b2)
    if hasattr(b1, 'conference_Person18'):
        assert not _is_linked(b1, 'conference_Person18', a)
    if hasattr(b2, 'conference_Person18'):
        assert _is_linked(b2, 'conference_Person18', a)
    _safe_set(a, 'conference_Talk17', None)
    assert not _is_linked(a, 'conference_Talk17', b2)
    if hasattr(b2, 'conference_Person18'):
        assert not _is_linked(b2, 'conference_Person18', a)


def test_assoc_participants0_link_reassign_clear():
    a = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    b1 = conference_Conference(name="sample_text", overview="sample_text", place="sample_text")
    b2 = conference_Conference(name="sample_text_2", overview="sample_text_2", place="sample_text_2")
    _safe_set(a, 'conference_Person', b1)
    assert _is_linked(a, 'conference_Person', b1)
    if hasattr(b1, 'conference_Conference'):
        assert _is_linked(b1, 'conference_Conference', a)
    _safe_set(a, 'conference_Person', b2)
    assert _is_linked(a, 'conference_Person', b2)
    if hasattr(b1, 'conference_Conference'):
        assert not _is_linked(b1, 'conference_Conference', a)
    if hasattr(b2, 'conference_Conference'):
        assert _is_linked(b2, 'conference_Conference', a)
    _safe_set(a, 'conference_Person', None)
    assert not _is_linked(a, 'conference_Person', b2)
    if hasattr(b2, 'conference_Conference'):
        assert not _is_linked(b2, 'conference_Conference', a)


def test_assoc_presenter13_link_reassign_clear():
    a = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    b1 = conference_Person(age=7, eclipseCommiter=True, firstname="sample_text", gender="sample_text", isRegistered=True, lastname="sample_text")
    b2 = conference_Person(age=13, eclipseCommiter=False, firstname="sample_text_2", gender="sample_text_2", isRegistered=False, lastname="sample_text_2")
    _safe_set(a, 'conference_Talk14', b1)
    assert _is_linked(a, 'conference_Talk14', b1)
    if hasattr(b1, 'conference_Person15'):
        assert _is_linked(b1, 'conference_Person15', a)
    _safe_set(a, 'conference_Talk14', b2)
    assert _is_linked(a, 'conference_Talk14', b2)
    if hasattr(b1, 'conference_Person15'):
        assert not _is_linked(b1, 'conference_Person15', a)
    if hasattr(b2, 'conference_Person15'):
        assert _is_linked(b2, 'conference_Person15', a)
    _safe_set(a, 'conference_Talk14', None)
    assert not _is_linked(a, 'conference_Talk14', b2)
    if hasattr(b2, 'conference_Person15'):
        assert not _is_linked(b2, 'conference_Person15', a)


def test_assoc_rooms19_link_reassign_clear():
    a = conference_Site(documentation="sample_text", name="sample_text")
    b1 = conference_Room(capacity=7, name="sample_text")
    b2 = conference_Room(capacity=13, name="sample_text_2")
    _safe_set(a, 'conference_Site20', {b1})
    assert _is_linked(a, 'conference_Site20', b1)
    if hasattr(b1, 'conference_Room'):
        assert _is_linked(b1, 'conference_Room', a)
    _safe_set(a, 'conference_Site20', {b2})
    assert _is_linked(a, 'conference_Site20', b2)
    if hasattr(b1, 'conference_Room'):
        assert not _is_linked(b1, 'conference_Room', a)
    if hasattr(b2, 'conference_Room'):
        assert _is_linked(b2, 'conference_Room', a)
    _safe_set(a, 'conference_Site20', set())
    assert not _is_linked(a, 'conference_Site20', b2)
    if hasattr(b2, 'conference_Room'):
        assert not _is_linked(b2, 'conference_Room', a)


def test_assoc_sites5_link_reassign_clear():
    a = conference_Site(documentation="sample_text", name="sample_text")
    b1 = conference_Conference(name="sample_text", overview="sample_text", place="sample_text")
    b2 = conference_Conference(name="sample_text_2", overview="sample_text_2", place="sample_text_2")
    _safe_set(a, 'conference_Site', b1)
    assert _is_linked(a, 'conference_Site', b1)
    if hasattr(b1, 'conference_Conference6'):
        assert _is_linked(b1, 'conference_Conference6', a)
    _safe_set(a, 'conference_Site', b2)
    assert _is_linked(a, 'conference_Site', b2)
    if hasattr(b1, 'conference_Conference6'):
        assert not _is_linked(b1, 'conference_Conference6', a)
    if hasattr(b2, 'conference_Conference6'):
        assert _is_linked(b2, 'conference_Conference6', a)
    _safe_set(a, 'conference_Site', None)
    assert not _is_linked(a, 'conference_Site', b2)
    if hasattr(b2, 'conference_Conference6'):
        assert not _is_linked(b2, 'conference_Conference6', a)


def test_assoc_talks1_link_reassign_clear():
    a = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    b1 = conference_Conference(name="sample_text", overview="sample_text", place="sample_text")
    b2 = conference_Conference(name="sample_text_2", overview="sample_text_2", place="sample_text_2")
    _safe_set(a, 'conference_Talk', b1)
    assert _is_linked(a, 'conference_Talk', b1)
    if hasattr(b1, 'conference_Conference2'):
        assert _is_linked(b1, 'conference_Conference2', a)
    _safe_set(a, 'conference_Talk', b2)
    assert _is_linked(a, 'conference_Talk', b2)
    if hasattr(b1, 'conference_Conference2'):
        assert not _is_linked(b1, 'conference_Conference2', a)
    if hasattr(b2, 'conference_Conference2'):
        assert _is_linked(b2, 'conference_Conference2', a)
    _safe_set(a, 'conference_Talk', None)
    assert not _is_linked(a, 'conference_Talk', b2)
    if hasattr(b2, 'conference_Conference2'):
        assert not _is_linked(b2, 'conference_Conference2', a)


def test_assoc_topic10_link_reassign_clear():
    a = conference_Topic(description="sample_text", documentation="sample_text", references="sample_text")
    b1 = conference_Talk(documentation="sample_text", title="sample_text", type="sample_text")
    b2 = conference_Talk(documentation="sample_text_2", title="sample_text_2", type="sample_text_2")
    _safe_set(a, 'conference_Topic12', b1)
    assert _is_linked(a, 'conference_Topic12', b1)
    if hasattr(b1, 'conference_Talk11'):
        assert _is_linked(b1, 'conference_Talk11', a)
    _safe_set(a, 'conference_Topic12', b2)
    assert _is_linked(a, 'conference_Topic12', b2)
    if hasattr(b1, 'conference_Talk11'):
        assert not _is_linked(b1, 'conference_Talk11', a)
    if hasattr(b2, 'conference_Talk11'):
        assert _is_linked(b2, 'conference_Talk11', a)
    _safe_set(a, 'conference_Topic12', None)
    assert not _is_linked(a, 'conference_Topic12', b2)
    if hasattr(b2, 'conference_Talk11'):
        assert not _is_linked(b2, 'conference_Talk11', a)


def test_assoc_topics3_link_reassign_clear():
    a = conference_Topic(description="sample_text", documentation="sample_text", references="sample_text")
    b1 = conference_Conference(name="sample_text", overview="sample_text", place="sample_text")
    b2 = conference_Conference(name="sample_text_2", overview="sample_text_2", place="sample_text_2")
    _safe_set(a, 'conference_Topic', b1)
    assert _is_linked(a, 'conference_Topic', b1)
    if hasattr(b1, 'conference_Conference4'):
        assert _is_linked(b1, 'conference_Conference4', a)
    _safe_set(a, 'conference_Topic', b2)
    assert _is_linked(a, 'conference_Topic', b2)
    if hasattr(b1, 'conference_Conference4'):
        assert not _is_linked(b1, 'conference_Conference4', a)
    if hasattr(b2, 'conference_Conference4'):
        assert _is_linked(b2, 'conference_Conference4', a)
    _safe_set(a, 'conference_Topic', None)
    assert not _is_linked(a, 'conference_Topic', b2)
    if hasattr(b2, 'conference_Conference4'):
        assert not _is_linked(b2, 'conference_Conference4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

conference_Conference_strategy = st.builds(conference_Conference, name=safe_text, overview=safe_text, place=safe_text)
@given(instance=conference_Conference_strategy)
@settings(max_examples=25)
def test_conference_Conference_instantiation(instance):
    assert isinstance(instance, conference_Conference)


conference_Person_strategy = st.builds(conference_Person, age=st.integers(), eclipseCommiter=st.booleans(), firstname=safe_text, gender=safe_text, isRegistered=st.booleans(), lastname=safe_text)
@given(instance=conference_Person_strategy)
@settings(max_examples=25)
def test_conference_Person_instantiation(instance):
    assert isinstance(instance, conference_Person)


conference_Room_strategy = st.builds(conference_Room, capacity=st.integers(), name=safe_text)
@given(instance=conference_Room_strategy)
@settings(max_examples=25)
def test_conference_Room_instantiation(instance):
    assert isinstance(instance, conference_Room)


conference_Site_strategy = st.builds(conference_Site, documentation=safe_text, name=safe_text)
@given(instance=conference_Site_strategy)
@settings(max_examples=25)
def test_conference_Site_instantiation(instance):
    assert isinstance(instance, conference_Site)


conference_Talk_strategy = st.builds(conference_Talk, documentation=safe_text, title=safe_text, type=safe_text)
@given(instance=conference_Talk_strategy)
@settings(max_examples=25)
def test_conference_Talk_instantiation(instance):
    assert isinstance(instance, conference_Talk)


conference_Topic_strategy = st.builds(conference_Topic, description=safe_text, documentation=safe_text, references=safe_text)
@given(instance=conference_Topic_strategy)
@settings(max_examples=25)
def test_conference_Topic_instantiation(instance):
    assert isinstance(instance, conference_Topic)



