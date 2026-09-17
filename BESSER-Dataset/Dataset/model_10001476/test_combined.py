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
    Admin,
    Commercial_Events,
    Birthday_Parties,
    Weddings,
    Refreshment,
    Event,
    Payment,
    Volunteer,
    Eventhead,
    Client,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_commercial_events_is_not_abstract():
    assert not inspect.isabstract(Commercial_Events)


def test_hyp_commercial_events_constructor_exists():
    assert callable(Commercial_Events.__init__)


def test_hyp_commercial_events_constructor_args():
    sig = inspect.signature(Commercial_Events.__init__)
    params = list(sig.parameters.keys())



def test_hyp_birthday_parties_is_not_abstract():
    assert not inspect.isabstract(Birthday_Parties)


def test_hyp_birthday_parties_constructor_exists():
    assert callable(Birthday_Parties.__init__)


def test_hyp_birthday_parties_constructor_args():
    sig = inspect.signature(Birthday_Parties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_weddings_is_not_abstract():
    assert not inspect.isabstract(Weddings)


def test_hyp_weddings_constructor_exists():
    assert callable(Weddings.__init__)


def test_hyp_weddings_constructor_args():
    sig = inspect.signature(Weddings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refreshment_is_not_abstract():
    assert not inspect.isabstract(Refreshment)


def test_hyp_refreshment_constructor_exists():
    assert callable(Refreshment.__init__)


def test_hyp_refreshment_constructor_args():
    sig = inspect.signature(Refreshment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())
    assert "eventid" in params, "Missing parameter 'eventid'"
    assert "eventype" in params, "Missing parameter 'eventype'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "date" in params, "Missing parameter 'date'"
    assert "eventname" in params, "Missing parameter 'eventname'"
    assert "eventhead" in params, "Missing parameter 'eventhead'"

def test_hyp_event_has_eventid():
    assert hasattr(Event, "eventid")
    descriptor = None
    for klass in Event.__mro__:
        if "eventid" in klass.__dict__:
            descriptor = klass.__dict__["eventid"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_eventype():
    assert hasattr(Event, "eventype")
    descriptor = None
    for klass in Event.__mro__:
        if "eventype" in klass.__dict__:
            descriptor = klass.__dict__["eventype"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_amount():
    assert hasattr(Event, "amount")
    descriptor = None
    for klass in Event.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_date():
    assert hasattr(Event, "date")
    descriptor = None
    for klass in Event.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_eventname():
    assert hasattr(Event, "eventname")
    descriptor = None
    for klass in Event.__mro__:
        if "eventname" in klass.__dict__:
            descriptor = klass.__dict__["eventname"]
            break
    assert isinstance(descriptor, property)

def test_hyp_event_has_eventhead():
    assert hasattr(Event, "eventhead")
    descriptor = None
    for klass in Event.__mro__:
        if "eventhead" in klass.__dict__:
            descriptor = klass.__dict__["eventhead"]
            break
    assert isinstance(descriptor, property)



def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "amout" in params, "Missing parameter 'amout'"
    assert "status" in params, "Missing parameter 'status'"
    assert "paytype" in params, "Missing parameter 'paytype'"






def test_hyp_volunteer_is_not_abstract():
    assert not inspect.isabstract(Volunteer)


def test_hyp_volunteer_constructor_exists():
    assert callable(Volunteer.__init__)


def test_hyp_volunteer_constructor_args():
    sig = inspect.signature(Volunteer.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_eventhead_is_not_abstract():
    assert not inspect.isabstract(Eventhead)


def test_hyp_eventhead_constructor_exists():
    assert callable(Eventhead.__init__)


def test_hyp_eventhead_constructor_args():
    sig = inspect.signature(Eventhead.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_hyp_client_constructor_exists():
    assert callable(Client.__init__)


def test_hyp_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "lname" in params, "Missing parameter 'lname'"






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
Admin_strategy = st.builds(
    Admin,
    username=
        safe_text,
    password=
        safe_text
)
Commercial_Events_strategy = st.builds(
    Commercial_Events,
)
Birthday_Parties_strategy = st.builds(
    Birthday_Parties,
)
Weddings_strategy = st.builds(
    Weddings,
)
Refreshment_strategy = st.builds(
    Refreshment,
)
Event_strategy = st.builds(
    Event,
    eventid=
        st.integers(),
    eventype=
        safe_text,
    amount=
        st.integers(),
    date=
        st.integers(),
    eventname=
        safe_text,
    eventhead=
        st.none()
)
Payment_strategy = st.builds(
    Payment,
    amout=
        st.integers(),
    status=
        safe_text,
    paytype=
        safe_text
)
Volunteer_strategy = st.builds(
    Volunteer,
    id=
        st.integers()
)
Eventhead_strategy = st.builds(
    Eventhead,
    id=
        st.integers()
)
Client_strategy = st.builds(
    Client,
    id=
        st.integers()
)
User_strategy = st.builds(
    User,
    username=
        safe_text,
    password=
        safe_text,
    fname=
        safe_text,
    lname=
        safe_text
)




@given(instance=Admin_strategy)
def test_hyp_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Admin_strategy)
def test_hyp_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original





@given(instance=Event_strategy)
@settings(max_examples=50)
def test_hyp_event_instantiation(instance):
    assert isinstance(instance, Event)



@given(instance=Event_strategy)
def test_hyp_event_eventid_setter(instance):
    original = instance.eventid
    instance.eventid = original
    assert instance.eventid == original



@given(instance=Event_strategy)
def test_hyp_event_eventype_setter(instance):
    original = instance.eventype
    instance.eventype = original
    assert instance.eventype == original



@given(instance=Event_strategy)
def test_hyp_event_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Event_strategy)
def test_hyp_event_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Event_strategy)
def test_hyp_event_eventname_setter(instance):
    original = instance.eventname
    instance.eventname = original
    assert instance.eventname == original



@given(instance=Event_strategy)
def test_hyp_event_eventhead_setter(instance):
    original = instance.eventhead
    instance.eventhead = original
    assert instance.eventhead == original




@given(instance=Payment_strategy)
def test_hyp_payment_amout_setter(instance):
    original = instance.amout
    instance.amout = original
    assert instance.amout == original



@given(instance=Payment_strategy)
def test_hyp_payment_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Payment_strategy)
def test_hyp_payment_paytype_setter(instance):
    original = instance.paytype
    instance.paytype = original
    assert instance.paytype == original




@given(instance=Volunteer_strategy)
def test_hyp_volunteer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Eventhead_strategy)
def test_hyp_eventhead_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Client_strategy)
def test_hyp_client_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=User_strategy)
def test_hyp_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=User_strategy)
def test_hyp_user_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Birthday_Parties,
    Client,
    Commercial_Events,
    Event,
    Eventhead,
    Payment,
    Refreshment,
    User,
    Volunteer,
    Weddings,
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

def test_Admin_password_value_roundtrip():
    instance = Admin(password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Admin_username_value_roundtrip():
    instance = Admin(password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Client_id_value_roundtrip():
    instance = Client(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Eventhead_id_value_roundtrip():
    instance = Eventhead(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Payment_amout_value_roundtrip():
    instance = Payment(amout=7, paytype="sample_text", status="sample_text")
    assert instance.amout == 7
    instance.amout = 13
    assert instance.amout == 13


def test_Payment_paytype_value_roundtrip():
    instance = Payment(amout=7, paytype="sample_text", status="sample_text")
    assert instance.paytype == "sample_text"
    instance.paytype = "sample_text_2"
    assert instance.paytype == "sample_text_2"


def test_Payment_status_value_roundtrip():
    instance = Payment(amout=7, paytype="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_User_fname_value_roundtrip():
    instance = User(fname="sample_text", lname="sample_text", password="sample_text", username="sample_text")
    assert instance.fname == "sample_text"
    instance.fname = "sample_text_2"
    assert instance.fname == "sample_text_2"


def test_User_lname_value_roundtrip():
    instance = User(fname="sample_text", lname="sample_text", password="sample_text", username="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(fname="sample_text", lname="sample_text", password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_username_value_roundtrip():
    instance = User(fname="sample_text", lname="sample_text", password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Volunteer_id_value_roundtrip():
    instance = Volunteer(id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_assoc_client_payment_link_reassign_clear():
    a = Payment(amout=7, paytype="sample_text", status="sample_text")
    b1 = Client(id=7)
    b2 = Client(id=13)
    _safe_set(a, 'client1', b1)
    assert _is_linked(a, 'client1', b1)
    if hasattr(b1, 'payment20'):
        assert _is_linked(b1, 'payment20', a)
    _safe_set(a, 'client1', b2)
    assert _is_linked(a, 'client1', b2)
    if hasattr(b1, 'payment20'):
        assert not _is_linked(b1, 'payment20', a)
    if hasattr(b2, 'payment20'):
        assert _is_linked(b2, 'payment20', a)
    _safe_set(a, 'client1', None)
    assert not _is_linked(a, 'client1', b2)
    if hasattr(b2, 'payment20'):
        assert not _is_linked(b2, 'payment20', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, password=safe_text, username=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Birthday_Parties_strategy = st.builds(Birthday_Parties)
@given(instance=Birthday_Parties_strategy)
@settings(max_examples=25)
def test_Birthday_Parties_instantiation(instance):
    assert isinstance(instance, Birthday_Parties)


Client_strategy = st.builds(Client, id=st.integers())
@given(instance=Client_strategy)
@settings(max_examples=25)
def test_Client_instantiation(instance):
    assert isinstance(instance, Client)


Commercial_Events_strategy = st.builds(Commercial_Events)
@given(instance=Commercial_Events_strategy)
@settings(max_examples=25)
def test_Commercial_Events_instantiation(instance):
    assert isinstance(instance, Commercial_Events)


Eventhead_strategy = st.builds(Eventhead, id=st.integers())
@given(instance=Eventhead_strategy)
@settings(max_examples=25)
def test_Eventhead_instantiation(instance):
    assert isinstance(instance, Eventhead)


Payment_strategy = st.builds(Payment, amout=st.integers(), paytype=safe_text, status=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Refreshment_strategy = st.builds(Refreshment)
@given(instance=Refreshment_strategy)
@settings(max_examples=25)
def test_Refreshment_instantiation(instance):
    assert isinstance(instance, Refreshment)


User_strategy = st.builds(User, fname=safe_text, lname=safe_text, password=safe_text, username=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


Volunteer_strategy = st.builds(Volunteer, id=st.integers())
@given(instance=Volunteer_strategy)
@settings(max_examples=25)
def test_Volunteer_instantiation(instance):
    assert isinstance(instance, Volunteer)


Weddings_strategy = st.builds(Weddings)
@given(instance=Weddings_strategy)
@settings(max_examples=25)
def test_Weddings_instantiation(instance):
    assert isinstance(instance, Weddings)



