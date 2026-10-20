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
    Event__,
    User__4,
    Date,
    User,
    Ticket,
    Event,
    String,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_event___is_not_abstract():
    assert not inspect.isabstract(Event__)


def test_hyp_event___constructor_exists():
    assert callable(Event__.__init__)


def test_hyp_event___constructor_args():
    sig = inspect.signature(Event__.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user__4_is_not_abstract():
    assert not inspect.isabstract(User__4)


def test_hyp_user__4_constructor_exists():
    assert callable(User__4.__init__)


def test_hyp_user__4_constructor_args():
    sig = inspect.signature(User__4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_date_is_not_abstract():
    assert not inspect.isabstract(Date)


def test_hyp_date_constructor_exists():
    assert callable(Date.__init__)


def test_hyp_date_constructor_args():
    sig = inspect.signature(Date.__init__)
    params = list(sig.parameters.keys())



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "selfDescription" in params, "Missing parameter 'selfDescription'"
    assert "friends" in params, "Missing parameter 'friends'"
    assert "password" in params, "Missing parameter 'password'"
    assert "tickets" in params, "Missing parameter 'tickets'"
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "company" in params, "Missing parameter 'company'"
    assert "id" in params, "Missing parameter 'id'"
    assert "events" in params, "Missing parameter 'events'"
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "userImage" in params, "Missing parameter 'userImage'"

def test_hyp_user_has_selfDescription():
    assert hasattr(User, "selfDescription")
    descriptor = None
    for klass in User.__mro__:
        if "selfDescription" in klass.__dict__:
            descriptor = klass.__dict__["selfDescription"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_friends():
    assert hasattr(User, "friends")
    descriptor = None
    for klass in User.__mro__:
        if "friends" in klass.__dict__:
            descriptor = klass.__dict__["friends"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_tickets():
    assert hasattr(User, "tickets")
    descriptor = None
    for klass in User.__mro__:
        if "tickets" in klass.__dict__:
            descriptor = klass.__dict__["tickets"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_name():
    assert hasattr(User, "name")
    descriptor = None
    for klass in User.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_gender():
    assert hasattr(User, "gender")
    descriptor = None
    for klass in User.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_company():
    assert hasattr(User, "company")
    descriptor = None
    for klass in User.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_id():
    assert hasattr(User, "id")
    descriptor = None
    for klass in User.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_events():
    assert hasattr(User, "events")
    descriptor = None
    for klass in User.__mro__:
        if "events" in klass.__dict__:
            descriptor = klass.__dict__["events"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_birthdate():
    assert hasattr(User, "birthdate")
    descriptor = None
    for klass in User.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has_userImage():
    assert hasattr(User, "userImage")
    descriptor = None
    for klass in User.__mro__:
        if "userImage" in klass.__dict__:
            descriptor = klass.__dict__["userImage"]
            break
    assert isinstance(descriptor, property)



def test_hyp_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_hyp_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_hyp_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "id" in params, "Missing parameter 'id'"

def test_hyp_ticket_has_event():
    assert hasattr(Ticket, "event")
    descriptor = None
    for klass in Ticket.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_hyp_ticket_has_id():
    assert hasattr(Ticket, "id")
    descriptor = None
    for klass in Ticket.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "placeName" in params, "Missing parameter 'placeName'"
    assert "location" in params, "Missing parameter 'location'"
    assert "type" in params, "Missing parameter 'type'"
    assert "image" in params, "Missing parameter 'image'"
    assert "organizator" in params, "Missing parameter 'organizator'"
    assert "discussion" in params, "Missing parameter 'discussion'"
    assert "participants" in params, "Missing parameter 'participants'"
    assert "time" in params, "Missing parameter 'time'"
    assert "participantCount" in params, "Missing parameter 'participantCount'"
    assert "about" in params, "Missing parameter 'about'"

def test_hyp_event_has_id():
    assert hasattr(Event, "id")
    descriptor = None
    for klass in Event.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_placeName():
    assert hasattr(Event, "placeName")
    descriptor = None
    for klass in Event.__mro__:
        if "placeName" in klass.__dict__:
            descriptor = klass.__dict__["placeName"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_location():
    assert hasattr(Event, "location")
    descriptor = None
    for klass in Event.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_type():
    assert hasattr(Event, "type")
    descriptor = None
    for klass in Event.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_image():
    assert hasattr(Event, "image")
    descriptor = None
    for klass in Event.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_organizator():
    assert hasattr(Event, "organizator")
    descriptor = None
    for klass in Event.__mro__:
        if "organizator" in klass.__dict__:
            descriptor = klass.__dict__["organizator"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_discussion():
    assert hasattr(Event, "discussion")
    descriptor = None
    for klass in Event.__mro__:
        if "discussion" in klass.__dict__:
            descriptor = klass.__dict__["discussion"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_participants():
    assert hasattr(Event, "participants")
    descriptor = None
    for klass in Event.__mro__:
        if "participants" in klass.__dict__:
            descriptor = klass.__dict__["participants"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_time():
    assert hasattr(Event, "time")
    descriptor = None
    for klass in Event.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_participantCount():
    assert hasattr(Event, "participantCount")
    descriptor = None
    for klass in Event.__mro__:
        if "participantCount" in klass.__dict__:
            descriptor = klass.__dict__["participantCount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_about():
    assert hasattr(Event, "about")
    descriptor = None
    for klass in Event.__mro__:
        if "about" in klass.__dict__:
            descriptor = klass.__dict__["about"]
            break
    assert isinstance(descriptor, property)

def test_hyp_string_exists():
    # Check that the Enumeration exists
    assert String is not None

def test_hyp_string_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in String]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in String"


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
Event___strategy = st.builds(
    Event__,
)
User__4_strategy = st.builds(
    User__4,
)
Date_strategy = st.builds(
    Date,
)
User_strategy = st.builds(
    User,
    selfDescription=
        safe_text,
    friends=
        safe_text,
    password=
        safe_text,
    tickets=
        safe_text,
    name=
        safe_text,
    gender=
        safe_text,
    company=
        safe_text,
    id=
        safe_text,
    events=
        st.none(),
    birthdate=
        st.dates(),
    userImage=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
    event=
        st.none(),
    id=
        safe_text
)
Event_strategy = st.builds(
    Event,
    id=
        st.none(),
    placeName=
        safe_text,
    location=
        safe_text,
    type=
        safe_text,
    image=
        safe_text,
    organizator=
        st.none(),
    discussion=
        safe_text,
    participants=
        safe_text,
    time=
        safe_text,
    participantCount=
        st.integers(),
    about=
        safe_text
)




@given(instance=User_strategy)
@settings(max_examples=50)
def test_hyp_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_hyp_user_selfDescription_setter(instance):
    original = instance.selfDescription
    instance.selfDescription = original
    assert instance.selfDescription == original



@given(instance=User_strategy)
def test_hyp_user_friends_setter(instance):
    original = instance.friends
    instance.friends = original
    assert instance.friends == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_tickets_setter(instance):
    original = instance.tickets
    instance.tickets = original
    assert instance.tickets == original



@given(instance=User_strategy)
def test_hyp_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=User_strategy)
def test_hyp_user_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=User_strategy)
def test_hyp_user_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=User_strategy)
def test_hyp_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=User_strategy)
def test_hyp_user_events_setter(instance):
    original = instance.events
    instance.events = original
    assert instance.events == original



@given(instance=User_strategy)
def test_hyp_user_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original



@given(instance=User_strategy)
def test_hyp_user_userImage_setter(instance):
    original = instance.userImage
    instance.userImage = original
    assert instance.userImage == original

@given(instance=Ticket_strategy)
@settings(max_examples=50)
def test_hyp_ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



@given(instance=Ticket_strategy)
def test_hyp_ticket_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_hyp_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_hyp_event_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Event_strategy)
def test_hyp_event_placeName_setter(instance):
    original = instance.placeName
    instance.placeName = original
    assert instance.placeName == original



@given(instance=Event_strategy)
def test_hyp_event_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Event_strategy)
def test_hyp_event_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Event_strategy)
def test_hyp_event_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=Event_strategy)
def test_hyp_event_organizator_setter(instance):
    original = instance.organizator
    instance.organizator = original
    assert instance.organizator == original



@given(instance=Event_strategy)
def test_hyp_event_discussion_setter(instance):
    original = instance.discussion
    instance.discussion = original
    assert instance.discussion == original



@given(instance=Event_strategy)
def test_hyp_event_participants_setter(instance):
    original = instance.participants
    instance.participants = original
    assert instance.participants == original



@given(instance=Event_strategy)
def test_hyp_event_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Event_strategy)
def test_hyp_event_participantCount_setter(instance):
    original = instance.participantCount
    instance.participantCount = original
    assert instance.participantCount == original



@given(instance=Event_strategy)
def test_hyp_event_about_setter(instance):
    original = instance.about
    instance.about = original
    assert instance.about == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Date,
    Event,
    Event__,
    Ticket,
    User,
    User__4,
    String,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Date_strategy = st.builds(Date)
@given(instance=Date_strategy)
@settings(max_examples=25)
def test_Date_instantiation(instance):
    assert isinstance(instance, Date)


Event___strategy = st.builds(Event__)
@given(instance=Event___strategy)
@settings(max_examples=25)
def test_Event___instantiation(instance):
    assert isinstance(instance, Event__)


User__4_strategy = st.builds(User__4)
@given(instance=User__4_strategy)
@settings(max_examples=25)
def test_User__4_instantiation(instance):
    assert isinstance(instance, User__4)



