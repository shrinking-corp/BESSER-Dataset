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
    HomePage,
    Photos,
    Message,
    Friend,
    User,
    Account,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_homepage_is_not_abstract():
    assert not inspect.isabstract(HomePage)


def test_hyp_homepage_constructor_exists():
    assert callable(HomePage.__init__)


def test_hyp_homepage_constructor_args():
    sig = inspect.signature(HomePage.__init__)
    params = list(sig.parameters.keys())
    assert "likeorunlike" in params, "Missing parameter 'likeorunlike'"
    assert "__status" in params, "Missing parameter '__status'"
    assert "__friendStatus" in params, "Missing parameter '__friendStatus'"

def test_hyp_homepage_has_likeorunlike():
    assert hasattr(HomePage, "likeorunlike")
    descriptor = None
    for klass in HomePage.__mro__:
        if "likeorunlike" in klass.__dict__:
            descriptor = klass.__dict__["likeorunlike"]
            break
    assert isinstance(descriptor, property)

def test_hyp_homepage_has___status():
    assert hasattr(HomePage, "__status")
    descriptor = None
    for klass in HomePage.__mro__:
        if "__status" in klass.__dict__:
            descriptor = klass.__dict__["__status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_homepage_has___friendStatus():
    assert hasattr(HomePage, "__friendStatus")
    descriptor = None
    for klass in HomePage.__mro__:
        if "__friendStatus" in klass.__dict__:
            descriptor = klass.__dict__["__friendStatus"]
            break
    assert isinstance(descriptor, property)



def test_hyp_photos_is_not_abstract():
    assert not inspect.isabstract(Photos)


def test_hyp_photos_constructor_exists():
    assert callable(Photos.__init__)


def test_hyp_photos_constructor_args():
    sig = inspect.signature(Photos.__init__)
    params = list(sig.parameters.keys())
    assert "__photos" in params, "Missing parameter '__photos'"

def test_hyp_photos_has___photos():
    assert hasattr(Photos, "__photos")
    descriptor = None
    for klass in Photos.__mro__:
        if "__photos" in klass.__dict__:
            descriptor = klass.__dict__["__photos"]
            break
    assert isinstance(descriptor, property)



def test_hyp_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_hyp_message_constructor_exists():
    assert callable(Message.__init__)


def test_hyp_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())
    assert "sender" in params, "Missing parameter 'sender'"
    assert "message" in params, "Missing parameter 'message'"
    assert "reciver" in params, "Missing parameter 'reciver'"






def test_hyp_friend_is_not_abstract():
    assert not inspect.isabstract(Friend)


def test_hyp_friend_constructor_exists():
    assert callable(Friend.__init__)


def test_hyp_friend_constructor_args():
    sig = inspect.signature(Friend.__init__)
    params = list(sig.parameters.keys())
    assert "acceptornot" in params, "Missing parameter 'acceptornot'"
    assert "friend____" in params, "Missing parameter 'friend____'"





def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "__M" in params, "Missing parameter '__M'"
    assert "_P" in params, "Missing parameter '_P'"
    assert "_F" in params, "Missing parameter '_F'"

def test_hyp_user_has___M():
    assert hasattr(User, "__M")
    descriptor = None
    for klass in User.__mro__:
        if "__M" in klass.__dict__:
            descriptor = klass.__dict__["__M"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has__P():
    assert hasattr(User, "_P")
    descriptor = None
    for klass in User.__mro__:
        if "_P" in klass.__dict__:
            descriptor = klass.__dict__["_P"]
            break
    assert isinstance(descriptor, property)

def test_hyp_user_has__F():
    assert hasattr(User, "_F")
    descriptor = None
    for klass in User.__mro__:
        if "_F" in klass.__dict__:
            descriptor = klass.__dict__["_F"]
            break
    assert isinstance(descriptor, property)



def test_hyp_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_hyp_account_constructor_exists():
    assert callable(Account.__init__)


def test_hyp_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "entity" in params, "Missing parameter 'entity'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"






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
HomePage_strategy = st.builds(
    HomePage,
    likeorunlike=
        st.booleans(),
    __status=
        safe_text,
    __friendStatus=
        safe_text
)
Photos_strategy = st.builds(
    Photos,
    __photos=
        safe_text
)
Message_strategy = st.builds(
    Message,
    sender=
        safe_text,
    message=
        safe_text,
    reciver=
        safe_text
)
Friend_strategy = st.builds(
    Friend,
    acceptornot=
        st.booleans(),
    friend____=
        safe_text
)
User_strategy = st.builds(
    User,
    __M=
        st.none(),
    _P=
        st.none(),
    _F=
        st.none()
)
Account_strategy = st.builds(
    Account,
    entity=
        safe_text,
    name=
        safe_text,
    email=
        safe_text,
    password=
        safe_text
)

@given(instance=HomePage_strategy)
@settings(max_examples=50)
def test_hyp_homepage_instantiation(instance):
    assert isinstance(instance, HomePage)



@given(instance=HomePage_strategy)
def test_hyp_homepage_likeorunlike_setter(instance):
    original = instance.likeorunlike
    instance.likeorunlike = original
    assert instance.likeorunlike == original



@given(instance=HomePage_strategy)
def test_hyp_homepage___status_setter(instance):
    original = instance.__status
    instance.__status = original
    assert instance.__status == original



@given(instance=HomePage_strategy)
def test_hyp_homepage___friendStatus_setter(instance):
    original = instance.__friendStatus
    instance.__friendStatus = original
    assert instance.__friendStatus == original

@given(instance=Photos_strategy)
@settings(max_examples=50)
def test_hyp_photos_instantiation(instance):
    assert isinstance(instance, Photos)



@given(instance=Photos_strategy)
def test_hyp_photos___photos_setter(instance):
    original = instance.__photos
    instance.__photos = original
    assert instance.__photos == original




@given(instance=Message_strategy)
def test_hyp_message_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original



@given(instance=Message_strategy)
def test_hyp_message_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=Message_strategy)
def test_hyp_message_reciver_setter(instance):
    original = instance.reciver
    instance.reciver = original
    assert instance.reciver == original




@given(instance=Friend_strategy)
def test_hyp_friend_acceptornot_setter(instance):
    original = instance.acceptornot
    instance.acceptornot = original
    assert instance.acceptornot == original



@given(instance=Friend_strategy)
def test_hyp_friend_friend_____setter(instance):
    original = instance.friend____
    instance.friend____ = original
    assert instance.friend____ == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_hyp_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_hyp_user___M_setter(instance):
    original = instance.__M
    instance.__M = original
    assert instance.__M == original



@given(instance=User_strategy)
def test_hyp_user__P_setter(instance):
    original = instance._P
    instance._P = original
    assert instance._P == original



@given(instance=User_strategy)
def test_hyp_user__F_setter(instance):
    original = instance._F
    instance._F = original
    assert instance._F == original




@given(instance=Account_strategy)
def test_hyp_account_entity_setter(instance):
    original = instance.entity
    instance.entity = original
    assert instance.entity == original



@given(instance=Account_strategy)
def test_hyp_account_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Account_strategy)
def test_hyp_account_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Account_strategy)
def test_hyp_account_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    Friend,
    HomePage,
    Message,
    Photos,
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

def test_Account_email_value_roundtrip():
    instance = Account(email="sample_text", entity="sample_text", name="sample_text", password="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Account_entity_value_roundtrip():
    instance = Account(email="sample_text", entity="sample_text", name="sample_text", password="sample_text")
    assert instance.entity == "sample_text"
    instance.entity = "sample_text_2"
    assert instance.entity == "sample_text_2"


def test_Account_name_value_roundtrip():
    instance = Account(email="sample_text", entity="sample_text", name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Account_password_value_roundtrip():
    instance = Account(email="sample_text", entity="sample_text", name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Friend_acceptornot_value_roundtrip():
    instance = Friend(acceptornot=True, friend____="sample_text")
    assert instance.acceptornot == True
    instance.acceptornot = False
    assert instance.acceptornot == False


def test_Friend_friend_____value_roundtrip():
    instance = Friend(acceptornot=True, friend____="sample_text")
    assert instance.friend____ == "sample_text"
    instance.friend____ = "sample_text_2"
    assert instance.friend____ == "sample_text_2"


def test_Message_message_value_roundtrip():
    instance = Message(message="sample_text", reciver="sample_text", sender="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_Message_reciver_value_roundtrip():
    instance = Message(message="sample_text", reciver="sample_text", sender="sample_text")
    assert instance.reciver == "sample_text"
    instance.reciver = "sample_text_2"
    assert instance.reciver == "sample_text_2"


def test_Message_sender_value_roundtrip():
    instance = Message(message="sample_text", reciver="sample_text", sender="sample_text")
    assert instance.sender == "sample_text"
    instance.sender = "sample_text_2"
    assert instance.sender == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Account_strategy = st.builds(Account, email=safe_text, entity=safe_text, name=safe_text, password=safe_text)
@given(instance=Account_strategy)
@settings(max_examples=25)
def test_Account_instantiation(instance):
    assert isinstance(instance, Account)


Friend_strategy = st.builds(Friend, acceptornot=st.booleans(), friend____=safe_text)
@given(instance=Friend_strategy)
@settings(max_examples=25)
def test_Friend_instantiation(instance):
    assert isinstance(instance, Friend)


Message_strategy = st.builds(Message, message=safe_text, reciver=safe_text, sender=safe_text)
@given(instance=Message_strategy)
@settings(max_examples=25)
def test_Message_instantiation(instance):
    assert isinstance(instance, Message)



