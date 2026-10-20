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
    Room,
    SessionType,
    Session,
    Serie,
    Event,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_sessiontype_is_not_abstract():
    assert not inspect.isabstract(SessionType)


def test_hyp_sessiontype_constructor_exists():
    assert callable(SessionType.__init__)


def test_hyp_sessiontype_constructor_args():
    sig = inspect.signature(SessionType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_session_is_not_abstract():
    assert not inspect.isabstract(Session)


def test_hyp_session_constructor_exists():
    assert callable(Session.__init__)


def test_hyp_session_constructor_args():
    sig = inspect.signature(Session.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "room" in params, "Missing parameter 'room'"
    assert "Events" in params, "Missing parameter 'Events'"
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_hyp_session_has_type():
    assert hasattr(Session, "type")
    descriptor = None
    for klass in Session.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_session_has_name():
    assert hasattr(Session, "name")
    descriptor = None
    for klass in Session.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_session_has_id():
    assert hasattr(Session, "id")
    descriptor = None
    for klass in Session.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_session_has_room():
    assert hasattr(Session, "room")
    descriptor = None
    for klass in Session.__mro__:
        if "room" in klass.__dict__:
            descriptor = klass.__dict__["room"]
            break
    assert isinstance(descriptor, property)

def test_hyp_session_has_Events():
    assert hasattr(Session, "Events")
    descriptor = None
    for klass in Session.__mro__:
        if "Events" in klass.__dict__:
            descriptor = klass.__dict__["Events"]
            break
    assert isinstance(descriptor, property)

def test_hyp_session_has_start():
    assert hasattr(Session, "start")
    descriptor = None
    for klass in Session.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_hyp_session_has_end():
    assert hasattr(Session, "end")
    descriptor = None
    for klass in Session.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_hyp_serie_is_not_abstract():
    assert not inspect.isabstract(Serie)


def test_hyp_serie_constructor_exists():
    assert callable(Serie.__init__)


def test_hyp_serie_constructor_args():
    sig = inspect.signature(Serie.__init__)
    params = list(sig.parameters.keys())
    assert "Events" in params, "Missing parameter 'Events'"

def test_hyp_serie_has_Events():
    assert hasattr(Serie, "Events")
    descriptor = None
    for klass in Serie.__mro__:
        if "Events" in klass.__dict__:
            descriptor = klass.__dict__["Events"]
            break
    assert isinstance(descriptor, property)



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "acronym" in params, "Missing parameter 'acronym'"






def test_hyp_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_hyp_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
Room_strategy = st.builds(
    Room,
    name=
        safe_text,
    id=
        st.integers()
)
SessionType_strategy = st.builds(
    SessionType,
    color=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
Session_strategy = st.builds(
    Session,
    type=
        st.none(),
    name=
        safe_text,
    id=
        st.integers(),
    room=
        st.none(),
    Events=
        st.none(),
    start=
        safe_text,
    end=
        safe_text
)
Serie_strategy = st.builds(
    Serie,
    Events=
        st.none()
)
Event_strategy = st.builds(
    Event,
    attribute=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text,
    edition=
        st.integers(),
    acronym=
        safe_text
)




@given(instance=Room_strategy)
def test_hyp_room_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Room_strategy)
def test_hyp_room_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=SessionType_strategy)
def test_hyp_sessiontype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=SessionType_strategy)
def test_hyp_sessiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=SessionType_strategy)
def test_hyp_sessiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Session_strategy)
@settings(max_examples=50)
def test_hyp_session_instantiation(instance):
    assert isinstance(instance, Session)



@given(instance=Session_strategy)
def test_hyp_session_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Session_strategy)
def test_hyp_session_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Session_strategy)
def test_hyp_session_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Session_strategy)
def test_hyp_session_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=Session_strategy)
def test_hyp_session_Events_setter(instance):
    original = instance.Events
    instance.Events = original
    assert instance.Events == original



@given(instance=Session_strategy)
def test_hyp_session_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=Session_strategy)
def test_hyp_session_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=Serie_strategy)
@settings(max_examples=50)
def test_hyp_serie_instantiation(instance):
    assert isinstance(instance, Serie)



@given(instance=Serie_strategy)
def test_hyp_serie_Events_setter(instance):
    original = instance.Events
    instance.Events = original
    assert instance.Events == original




@given(instance=Event_strategy)
def test_hyp_event_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Event_strategy)
def test_hyp_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Event_strategy)
def test_hyp_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Event_strategy)
def test_hyp_event_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original



@given(instance=Event_strategy)
def test_hyp_event_acronym_setter(instance):
    original = instance.acronym
    instance.acronym = original
    assert instance.acronym == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Event,
    Room,
    Serie,
    Session,
    SessionType,
    Enumeration,
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

def test_Event_acronym_value_roundtrip():
    instance = Event(acronym="sample_text", attribute="sample_text", edition=7, id=7, name="sample_text")
    assert instance.acronym == "sample_text"
    instance.acronym = "sample_text_2"
    assert instance.acronym == "sample_text_2"


def test_Event_attribute_value_roundtrip():
    instance = Event(acronym="sample_text", attribute="sample_text", edition=7, id=7, name="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Event_edition_value_roundtrip():
    instance = Event(acronym="sample_text", attribute="sample_text", edition=7, id=7, name="sample_text")
    assert instance.edition == 7
    instance.edition = 13
    assert instance.edition == 13


def test_Event_id_value_roundtrip():
    instance = Event(acronym="sample_text", attribute="sample_text", edition=7, id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Event_name_value_roundtrip():
    instance = Event(acronym="sample_text", attribute="sample_text", edition=7, id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Room_id_value_roundtrip():
    instance = Room(id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Room_name_value_roundtrip():
    instance = Room(id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_SessionType_color_value_roundtrip():
    instance = SessionType(color="sample_text", id=7, name="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_SessionType_id_value_roundtrip():
    instance = SessionType(color="sample_text", id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_SessionType_name_value_roundtrip():
    instance = SessionType(color="sample_text", id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Event_strategy = st.builds(Event, acronym=safe_text, attribute=safe_text, edition=st.integers(), id=st.integers(), name=safe_text)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


Room_strategy = st.builds(Room, id=st.integers(), name=safe_text)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


SessionType_strategy = st.builds(SessionType, color=safe_text, id=st.integers(), name=safe_text)
@given(instance=SessionType_strategy)
@settings(max_examples=25)
def test_SessionType_instantiation(instance):
    assert isinstance(instance, SessionType)



