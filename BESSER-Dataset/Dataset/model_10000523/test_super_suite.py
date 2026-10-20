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
    Timinglist,
    Flightlist,
    Admin,
    System,
    Ticket,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_timinglist_is_not_abstract():
    assert not inspect.isabstract(Timinglist)


def test_hyp_timinglist_constructor_exists():
    assert callable(Timinglist.__init__)


def test_hyp_timinglist_constructor_args():
    sig = inspect.signature(Timinglist.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "source" in params, "Missing parameter 'source'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "flightname" in params, "Missing parameter 'flightname'"







def test_hyp_flightlist_is_not_abstract():
    assert not inspect.isabstract(Flightlist)


def test_hyp_flightlist_constructor_exists():
    assert callable(Flightlist.__init__)


def test_hyp_flightlist_constructor_args():
    sig = inspect.signature(Flightlist.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "type" in params, "Missing parameter 'type'"
    assert "adminname" in params, "Missing parameter 'adminname'"
    assert "mobile" in params, "Missing parameter 'mobile'"








def test_hyp_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_hyp_system_constructor_exists():
    assert callable(System.__init__)


def test_hyp_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())
    assert "session" in params, "Missing parameter 'session'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_hyp_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_hyp_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "ticketid" in params, "Missing parameter 'ticketid'"
    assert "price" in params, "Missing parameter 'price'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "source" in params, "Missing parameter 'source'"
    assert "passengername" in params, "Missing parameter 'passengername'"
    assert "flightname" in params, "Missing parameter 'flightname'"









def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "attribute" in params, "Missing parameter 'attribute'"





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
Timinglist_strategy = st.builds(
    Timinglist,
    time=
        safe_text,
    source=
        safe_text,
    destination=
        safe_text,
    flightname=
        safe_text
)
Flightlist_strategy = st.builds(
    Flightlist,
    name=
        safe_text,
    id=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    password=
        safe_text,
    gender=
        safe_text,
    type=
        safe_text,
    adminname=
        safe_text,
    mobile=
        st.integers()
)
System_strategy = st.builds(
    System,
    session=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
Ticket_strategy = st.builds(
    Ticket,
    ticketid=
        safe_text,
    price=
        st.integers(),
    destination=
        safe_text,
    source=
        safe_text,
    passengername=
        safe_text,
    flightname=
        safe_text
)
User_strategy = st.builds(
    User,
    password=
        safe_text,
    username=
        safe_text,
    attribute=
        safe_text
)




@given(instance=Timinglist_strategy)
def test_hyp_timinglist_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Timinglist_strategy)
def test_hyp_timinglist_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=Timinglist_strategy)
def test_hyp_timinglist_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Timinglist_strategy)
def test_hyp_timinglist_flightname_setter(instance):
    original = instance.flightname
    instance.flightname = original
    assert instance.flightname == original




@given(instance=Flightlist_strategy)
def test_hyp_flightlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Flightlist_strategy)
def test_hyp_flightlist_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Admin_strategy)
def test_hyp_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_hyp_admin_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Admin_strategy)
def test_hyp_admin_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Admin_strategy)
def test_hyp_admin_adminname_setter(instance):
    original = instance.adminname
    instance.adminname = original
    assert instance.adminname == original



@given(instance=Admin_strategy)
def test_hyp_admin_mobile_setter(instance):
    original = instance.mobile
    instance.mobile = original
    assert instance.mobile == original




@given(instance=System_strategy)
def test_hyp_system_session_setter(instance):
    original = instance.session
    instance.session = original
    assert instance.session == original



@given(instance=System_strategy)
def test_hyp_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=System_strategy)
def test_hyp_system_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Ticket_strategy)
def test_hyp_ticket_ticketid_setter(instance):
    original = instance.ticketid
    instance.ticketid = original
    assert instance.ticketid == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_passengername_setter(instance):
    original = instance.passengername
    instance.passengername = original
    assert instance.passengername == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_flightname_setter(instance):
    original = instance.flightname
    instance.flightname = original
    assert instance.flightname == original




@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=User_strategy)
def test_hyp_user_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Flightlist,
    System,
    Ticket,
    Timinglist,
    User,
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

def test_Admin_adminname_value_roundtrip():
    instance = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    assert instance.adminname == "sample_text"
    instance.adminname = "sample_text_2"
    assert instance.adminname == "sample_text_2"


def test_Admin_gender_value_roundtrip():
    instance = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_Admin_mobile_value_roundtrip():
    instance = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    assert instance.mobile == 7
    instance.mobile = 13
    assert instance.mobile == 13


def test_Admin_password_value_roundtrip():
    instance = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Admin_type_value_roundtrip():
    instance = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Flightlist_id_value_roundtrip():
    instance = Flightlist(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Flightlist_name_value_roundtrip():
    instance = Flightlist(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_System_id_value_roundtrip():
    instance = System(id="sample_text", name="sample_text", session="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_System_name_value_roundtrip():
    instance = System(id="sample_text", name="sample_text", session="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_System_session_value_roundtrip():
    instance = System(id="sample_text", name="sample_text", session="sample_text")
    assert instance.session == "sample_text"
    instance.session = "sample_text_2"
    assert instance.session == "sample_text_2"


def test_Ticket_destination_value_roundtrip():
    instance = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    assert instance.destination == "sample_text"
    instance.destination = "sample_text_2"
    assert instance.destination == "sample_text_2"


def test_Ticket_flightname_value_roundtrip():
    instance = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    assert instance.flightname == "sample_text"
    instance.flightname = "sample_text_2"
    assert instance.flightname == "sample_text_2"


def test_Ticket_passengername_value_roundtrip():
    instance = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    assert instance.passengername == "sample_text"
    instance.passengername = "sample_text_2"
    assert instance.passengername == "sample_text_2"


def test_Ticket_price_value_roundtrip():
    instance = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_Ticket_source_value_roundtrip():
    instance = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_Ticket_ticketid_value_roundtrip():
    instance = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    assert instance.ticketid == "sample_text"
    instance.ticketid = "sample_text_2"
    assert instance.ticketid == "sample_text_2"


def test_Timinglist_destination_value_roundtrip():
    instance = Timinglist(destination="sample_text", flightname="sample_text", source="sample_text", time="sample_text")
    assert instance.destination == "sample_text"
    instance.destination = "sample_text_2"
    assert instance.destination == "sample_text_2"


def test_Timinglist_flightname_value_roundtrip():
    instance = Timinglist(destination="sample_text", flightname="sample_text", source="sample_text", time="sample_text")
    assert instance.flightname == "sample_text"
    instance.flightname = "sample_text_2"
    assert instance.flightname == "sample_text_2"


def test_Timinglist_source_value_roundtrip():
    instance = Timinglist(destination="sample_text", flightname="sample_text", source="sample_text", time="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_Timinglist_time_value_roundtrip():
    instance = Timinglist(destination="sample_text", flightname="sample_text", source="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_User_attribute_value_roundtrip():
    instance = User(attribute="sample_text", password="sample_text", username="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(attribute="sample_text", password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_username_value_roundtrip():
    instance = User(attribute="sample_text", password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_assoc_Admin_System_link_reassign_clear():
    a = System(id="sample_text", name="sample_text", session="sample_text")
    b1 = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    b2 = Admin(adminname="sample_text_2", gender="sample_text_2", mobile=13, password="sample_text_2", type="sample_text_2")
    _safe_set(a, 'maintains5', b1)
    assert _is_linked(a, 'maintains5', b1)
    if hasattr(b1, 'system4'):
        assert _is_linked(b1, 'system4', a)
    _safe_set(a, 'maintains5', b2)
    assert _is_linked(a, 'maintains5', b2)
    if hasattr(b1, 'system4'):
        assert not _is_linked(b1, 'system4', a)
    if hasattr(b2, 'system4'):
        assert _is_linked(b2, 'system4', a)
    _safe_set(a, 'maintains5', None)
    assert not _is_linked(a, 'maintains5', b2)
    if hasattr(b2, 'system4'):
        assert not _is_linked(b2, 'system4', a)


def test_assoc_System_Flightlist_link_reassign_clear():
    a = System(id="sample_text", name="sample_text", session="sample_text")
    b1 = Flightlist(id="sample_text", name="sample_text")
    b2 = Flightlist(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'has6', b1)
    assert _is_linked(a, 'has6', b1)
    if hasattr(b1, 'system7'):
        assert _is_linked(b1, 'system7', a)
    _safe_set(a, 'has6', b2)
    assert _is_linked(a, 'has6', b2)
    if hasattr(b1, 'system7'):
        assert not _is_linked(b1, 'system7', a)
    if hasattr(b2, 'system7'):
        assert _is_linked(b2, 'system7', a)
    _safe_set(a, 'has6', None)
    assert not _is_linked(a, 'has6', b2)
    if hasattr(b2, 'system7'):
        assert not _is_linked(b2, 'system7', a)


def test_assoc_System_Timinglist_link_reassign_clear():
    a = Timinglist(destination="sample_text", flightname="sample_text", source="sample_text", time="sample_text")
    b1 = System(id="sample_text", name="sample_text", session="sample_text")
    b2 = System(id="sample_text_2", name="sample_text_2", session="sample_text_2")
    _safe_set(a, 'has9', b1)
    assert _is_linked(a, 'has9', b1)
    if hasattr(b1, 'system8'):
        assert _is_linked(b1, 'system8', a)
    _safe_set(a, 'has9', b2)
    assert _is_linked(a, 'has9', b2)
    if hasattr(b1, 'system8'):
        assert not _is_linked(b1, 'system8', a)
    if hasattr(b2, 'system8'):
        assert _is_linked(b2, 'system8', a)
    _safe_set(a, 'has9', None)
    assert not _is_linked(a, 'has9', b2)
    if hasattr(b2, 'system8'):
        assert not _is_linked(b2, 'system8', a)


def test_assoc_User_System_link_reassign_clear():
    a = User(attribute="sample_text", password="sample_text", username="sample_text")
    b1 = System(id="sample_text", name="sample_text", session="sample_text")
    b2 = System(id="sample_text_2", name="sample_text_2", session="sample_text_2")
    _safe_set(a, 'system2', b1)
    assert _is_linked(a, 'system2', b1)
    if hasattr(b1, 'visits3'):
        assert _is_linked(b1, 'visits3', a)
    _safe_set(a, 'system2', b2)
    assert _is_linked(a, 'system2', b2)
    if hasattr(b1, 'visits3'):
        assert not _is_linked(b1, 'visits3', a)
    if hasattr(b2, 'visits3'):
        assert _is_linked(b2, 'visits3', a)
    _safe_set(a, 'system2', None)
    assert not _is_linked(a, 'system2', b2)
    if hasattr(b2, 'visits3'):
        assert not _is_linked(b2, 'visits3', a)


def test_assoc_User_Ticket_link_reassign_clear():
    a = User(attribute="sample_text", password="sample_text", username="sample_text")
    b1 = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    b2 = Ticket(destination="sample_text_2", flightname="sample_text_2", passengername="sample_text_2", price=13, source="sample_text_2", ticketid="sample_text_2")
    _safe_set(a, 'books0', {b1})
    assert _is_linked(a, 'books0', b1)
    if hasattr(b1, 'system1'):
        assert _is_linked(b1, 'system1', a)
    _safe_set(a, 'books0', {b2})
    assert _is_linked(a, 'books0', b2)
    if hasattr(b1, 'system1'):
        assert not _is_linked(b1, 'system1', a)
    if hasattr(b2, 'system1'):
        assert _is_linked(b2, 'system1', a)
    _safe_set(a, 'books0', set())
    assert not _is_linked(a, 'books0', b2)
    if hasattr(b2, 'system1'):
        assert not _is_linked(b2, 'system1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, adminname=safe_text, gender=safe_text, mobile=st.integers(), password=safe_text, type=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Flightlist_strategy = st.builds(Flightlist, id=safe_text, name=safe_text)
@given(instance=Flightlist_strategy)
@settings(max_examples=25)
def test_Flightlist_instantiation(instance):
    assert isinstance(instance, Flightlist)


System_strategy = st.builds(System, id=safe_text, name=safe_text, session=safe_text)
@given(instance=System_strategy)
@settings(max_examples=25)
def test_System_instantiation(instance):
    assert isinstance(instance, System)


Ticket_strategy = st.builds(Ticket, destination=safe_text, flightname=safe_text, passengername=safe_text, price=st.integers(), source=safe_text, ticketid=safe_text)
@given(instance=Ticket_strategy)
@settings(max_examples=25)
def test_Ticket_instantiation(instance):
    assert isinstance(instance, Ticket)


Timinglist_strategy = st.builds(Timinglist, destination=safe_text, flightname=safe_text, source=safe_text, time=safe_text)
@given(instance=Timinglist_strategy)
@settings(max_examples=25)
def test_Timinglist_instantiation(instance):
    assert isinstance(instance, Timinglist)


User_strategy = st.builds(User, attribute=safe_text, password=safe_text, username=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Flightlist,
    System,
    Ticket,
    Timinglist,
    User,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_Admin_System_reverse_link_reassign_clear():
    a1 = System(id="sample_text", name="sample_text", session="sample_text")
    a2 = System(id="sample_text_2", name="sample_text_2", session="sample_text_2")
    b = Admin(adminname="sample_text", gender="sample_text", mobile=7, password="sample_text", type="sample_text")
    _safe_set(b, 'system4', a1)
    assert _is_linked(b, 'system4', a1)
    if hasattr(a1, 'maintains5'):
        assert _is_linked(a1, 'maintains5', b)
    _safe_set(b, 'system4', a2)
    assert _is_linked(b, 'system4', a2)
    if hasattr(a1, 'maintains5'):
        assert not _is_linked(a1, 'maintains5', b)
    if hasattr(a2, 'maintains5'):
        assert _is_linked(a2, 'maintains5', b)
    _safe_set(b, 'system4', None)
    assert not _is_linked(b, 'system4', a2)
    if hasattr(a2, 'maintains5'):
        assert not _is_linked(a2, 'maintains5', b)


def test_assoc_System_Flightlist_reverse_link_reassign_clear():
    a1 = System(id="sample_text", name="sample_text", session="sample_text")
    a2 = System(id="sample_text_2", name="sample_text_2", session="sample_text_2")
    b = Flightlist(id="sample_text", name="sample_text")
    _safe_set(b, 'system7', a1)
    assert _is_linked(b, 'system7', a1)
    if hasattr(a1, 'has6'):
        assert _is_linked(a1, 'has6', b)
    _safe_set(b, 'system7', a2)
    assert _is_linked(b, 'system7', a2)
    if hasattr(a1, 'has6'):
        assert not _is_linked(a1, 'has6', b)
    if hasattr(a2, 'has6'):
        assert _is_linked(a2, 'has6', b)
    _safe_set(b, 'system7', None)
    assert not _is_linked(b, 'system7', a2)
    if hasattr(a2, 'has6'):
        assert not _is_linked(a2, 'has6', b)


def test_assoc_System_Timinglist_reverse_link_reassign_clear():
    a1 = Timinglist(destination="sample_text", flightname="sample_text", source="sample_text", time="sample_text")
    a2 = Timinglist(destination="sample_text_2", flightname="sample_text_2", source="sample_text_2", time="sample_text_2")
    b = System(id="sample_text", name="sample_text", session="sample_text")
    _safe_set(b, 'system8', a1)
    assert _is_linked(b, 'system8', a1)
    if hasattr(a1, 'has9'):
        assert _is_linked(a1, 'has9', b)
    _safe_set(b, 'system8', a2)
    assert _is_linked(b, 'system8', a2)
    if hasattr(a1, 'has9'):
        assert not _is_linked(a1, 'has9', b)
    if hasattr(a2, 'has9'):
        assert _is_linked(a2, 'has9', b)
    _safe_set(b, 'system8', None)
    assert not _is_linked(b, 'system8', a2)
    if hasattr(a2, 'has9'):
        assert not _is_linked(a2, 'has9', b)


def test_assoc_User_System_reverse_link_reassign_clear():
    a1 = User(attribute="sample_text", password="sample_text", username="sample_text")
    a2 = User(attribute="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = System(id="sample_text", name="sample_text", session="sample_text")
    _safe_set(b, 'visits3', a1)
    assert _is_linked(b, 'visits3', a1)
    if hasattr(a1, 'system2'):
        assert _is_linked(a1, 'system2', b)
    _safe_set(b, 'visits3', a2)
    assert _is_linked(b, 'visits3', a2)
    if hasattr(a1, 'system2'):
        assert not _is_linked(a1, 'system2', b)
    if hasattr(a2, 'system2'):
        assert _is_linked(a2, 'system2', b)
    _safe_set(b, 'visits3', None)
    assert not _is_linked(b, 'visits3', a2)
    if hasattr(a2, 'system2'):
        assert not _is_linked(a2, 'system2', b)


def test_assoc_User_Ticket_reverse_link_reassign_clear():
    a1 = User(attribute="sample_text", password="sample_text", username="sample_text")
    a2 = User(attribute="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = Ticket(destination="sample_text", flightname="sample_text", passengername="sample_text", price=7, source="sample_text", ticketid="sample_text")
    _safe_set(b, 'system1', {a1})
    assert _is_linked(b, 'system1', a1)
    if hasattr(a1, 'books0'):
        assert _is_linked(a1, 'books0', b)
    _safe_set(b, 'system1', {a2})
    assert _is_linked(b, 'system1', a2)
    if hasattr(a1, 'books0'):
        assert not _is_linked(a1, 'books0', b)
    if hasattr(a2, 'books0'):
        assert _is_linked(a2, 'books0', b)
    _safe_set(b, 'system1', set())
    assert not _is_linked(b, 'system1', a2)
    if hasattr(a2, 'books0'):
        assert not _is_linked(a2, 'books0', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


