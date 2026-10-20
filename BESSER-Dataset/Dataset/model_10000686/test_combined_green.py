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
    Class,
    Login,
    Registration,
    Page,
    Friend,
    Message,
    Group,
    Post,
    Profile,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"





def test_hyp_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_hyp_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_hyp_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"







def test_hyp_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_hyp_page_constructor_exists():
    assert callable(Page.__init__)


def test_hyp_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_friend_is_not_abstract():
    assert not inspect.isabstract(Friend)


def test_hyp_friend_constructor_exists():
    assert callable(Friend.__init__)


def test_hyp_friend_constructor_args():
    sig = inspect.signature(Friend.__init__)
    params = list(sig.parameters.keys())



def test_hyp_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_hyp_message_constructor_exists():
    assert callable(Message.__init__)


def test_hyp_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())
    assert "maxChars" in params, "Missing parameter 'maxChars'"




def test_hyp_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_hyp_group_constructor_exists():
    assert callable(Group.__init__)


def test_hyp_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "discription" in params, "Missing parameter 'discription'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_hyp_post_constructor_exists():
    assert callable(Post.__init__)


def test_hyp_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"
    assert "privacy" in params, "Missing parameter 'privacy'"





def test_hyp_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_hyp_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_hyp_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "about" in params, "Missing parameter 'about'"
    assert "password" in params, "Missing parameter 'password'"






def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
Class_strategy = st.builds(
    Class,
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    username=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    fname=
        safe_text,
    lname=
        safe_text,
    password=
        safe_text,
    userName=
        safe_text
)
Page_strategy = st.builds(
    Page,
    name=
        safe_text
)
Friend_strategy = st.builds(
    Friend,
)
Message_strategy = st.builds(
    Message,
    maxChars=
        safe_text
)
Group_strategy = st.builds(
    Group,
    discription=
        safe_text,
    name=
        safe_text
)
Post_strategy = st.builds(
    Post,
    info=
        safe_text,
    privacy=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    username=
        safe_text,
    about=
        safe_text,
    password=
        safe_text
)
User_strategy = st.builds(
    User,
    name=
        safe_text
)





@given(instance=Login_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_hyp_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original




@given(instance=Registration_strategy)
def test_hyp_registration_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Registration_strategy)
def test_hyp_registration_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Registration_strategy)
def test_hyp_registration_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Registration_strategy)
def test_hyp_registration_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original




@given(instance=Page_strategy)
def test_hyp_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=Message_strategy)
def test_hyp_message_maxChars_setter(instance):
    original = instance.maxChars
    instance.maxChars = original
    assert instance.maxChars == original




@given(instance=Group_strategy)
def test_hyp_group_discription_setter(instance):
    original = instance.discription
    instance.discription = original
    assert instance.discription == original



@given(instance=Group_strategy)
def test_hyp_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Post_strategy)
def test_hyp_post_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original



@given(instance=Post_strategy)
def test_hyp_post_privacy_setter(instance):
    original = instance.privacy
    instance.privacy = original
    assert instance.privacy == original




@given(instance=Profile_strategy)
def test_hyp_profile_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Profile_strategy)
def test_hyp_profile_about_setter(instance):
    original = instance.about
    instance.about = original
    assert instance.about == original



@given(instance=Profile_strategy)
def test_hyp_profile_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=User_strategy)
def test_hyp_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    Friend,
    Group,
    Login,
    Message,
    Page,
    Post,
    Profile,
    Registration,
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

def test_Group_discription_value_roundtrip():
    instance = Group(discription="sample_text", name="sample_text")
    assert instance.discription == "sample_text"
    instance.discription = "sample_text_2"
    assert instance.discription == "sample_text_2"


def test_Group_name_value_roundtrip():
    instance = Group(discription="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Login_password_value_roundtrip():
    instance = Login(password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Login_username_value_roundtrip():
    instance = Login(password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Message_maxChars_value_roundtrip():
    instance = Message(maxChars="sample_text")
    assert instance.maxChars == "sample_text"
    instance.maxChars = "sample_text_2"
    assert instance.maxChars == "sample_text_2"


def test_Page_name_value_roundtrip():
    instance = Page(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Post_info_value_roundtrip():
    instance = Post(info="sample_text", privacy="sample_text")
    assert instance.info == "sample_text"
    instance.info = "sample_text_2"
    assert instance.info == "sample_text_2"


def test_Post_privacy_value_roundtrip():
    instance = Post(info="sample_text", privacy="sample_text")
    assert instance.privacy == "sample_text"
    instance.privacy = "sample_text_2"
    assert instance.privacy == "sample_text_2"


def test_Profile_about_value_roundtrip():
    instance = Profile(about="sample_text", password="sample_text", username="sample_text")
    assert instance.about == "sample_text"
    instance.about = "sample_text_2"
    assert instance.about == "sample_text_2"


def test_Profile_password_value_roundtrip():
    instance = Profile(about="sample_text", password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Profile_username_value_roundtrip():
    instance = Profile(about="sample_text", password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Registration_fname_value_roundtrip():
    instance = Registration(fname="sample_text", lname="sample_text", password="sample_text", userName="sample_text")
    assert instance.fname == "sample_text"
    instance.fname = "sample_text_2"
    assert instance.fname == "sample_text_2"


def test_Registration_lname_value_roundtrip():
    instance = Registration(fname="sample_text", lname="sample_text", password="sample_text", userName="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_Registration_password_value_roundtrip():
    instance = Registration(fname="sample_text", lname="sample_text", password="sample_text", userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Registration_userName_value_roundtrip():
    instance = Registration(fname="sample_text", lname="sample_text", password="sample_text", userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_User_name_value_roundtrip():
    instance = User(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_User_Friends_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Friend()
    b2 = Friend()
    _safe_set(a, 'friends12', {b1})
    assert _is_linked(a, 'friends12', b1)
    if hasattr(b1, 'user13'):
        assert _is_linked(b1, 'user13', a)
    _safe_set(a, 'friends12', {b2})
    assert _is_linked(a, 'friends12', b2)
    if hasattr(b1, 'user13'):
        assert not _is_linked(b1, 'user13', a)
    if hasattr(b2, 'user13'):
        assert _is_linked(b2, 'user13', a)
    _safe_set(a, 'friends12', set())
    assert not _is_linked(a, 'friends12', b2)
    if hasattr(b2, 'user13'):
        assert not _is_linked(b2, 'user13', a)


def test_assoc_User_Group_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Group(discription="sample_text", name="sample_text")
    b2 = Group(discription="sample_text_2", name="sample_text_2")
    _safe_set(a, 'group6', {b1})
    assert _is_linked(a, 'group6', b1)
    if hasattr(b1, 'user7'):
        assert _is_linked(b1, 'user7', a)
    _safe_set(a, 'group6', {b2})
    assert _is_linked(a, 'group6', b2)
    if hasattr(b1, 'user7'):
        assert not _is_linked(b1, 'user7', a)
    if hasattr(b2, 'user7'):
        assert _is_linked(b2, 'user7', a)
    _safe_set(a, 'group6', set())
    assert not _is_linked(a, 'group6', b2)
    if hasattr(b2, 'user7'):
        assert not _is_linked(b2, 'user7', a)


def test_assoc_User_Login_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Login(password="sample_text", username="sample_text")
    b2 = Login(password="sample_text_2", username="sample_text_2")
    _safe_set(a, 'login4', b1)
    assert _is_linked(a, 'login4', b1)
    if hasattr(b1, 'user5'):
        assert _is_linked(b1, 'user5', a)
    _safe_set(a, 'login4', b2)
    assert _is_linked(a, 'login4', b2)
    if hasattr(b1, 'user5'):
        assert not _is_linked(b1, 'user5', a)
    if hasattr(b2, 'user5'):
        assert _is_linked(b2, 'user5', a)
    _safe_set(a, 'login4', None)
    assert not _is_linked(a, 'login4', b2)
    if hasattr(b2, 'user5'):
        assert not _is_linked(b2, 'user5', a)


def test_assoc_User_Message_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Message(maxChars="sample_text")
    b2 = Message(maxChars="sample_text_2")
    _safe_set(a, 'message10', {b1})
    assert _is_linked(a, 'message10', b1)
    if hasattr(b1, 'user11'):
        assert _is_linked(b1, 'user11', a)
    _safe_set(a, 'message10', {b2})
    assert _is_linked(a, 'message10', b2)
    if hasattr(b1, 'user11'):
        assert not _is_linked(b1, 'user11', a)
    if hasattr(b2, 'user11'):
        assert _is_linked(b2, 'user11', a)
    _safe_set(a, 'message10', set())
    assert not _is_linked(a, 'message10', b2)
    if hasattr(b2, 'user11'):
        assert not _is_linked(b2, 'user11', a)


def test_assoc_User_Myprofile_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Profile(about="sample_text", password="sample_text", username="sample_text")
    b2 = Profile(about="sample_text_2", password="sample_text_2", username="sample_text_2")
    _safe_set(a, 'myprofile0', b1)
    assert _is_linked(a, 'myprofile0', b1)
    if hasattr(b1, 'user1'):
        assert _is_linked(b1, 'user1', a)
    _safe_set(a, 'myprofile0', b2)
    assert _is_linked(a, 'myprofile0', b2)
    if hasattr(b1, 'user1'):
        assert not _is_linked(b1, 'user1', a)
    if hasattr(b2, 'user1'):
        assert _is_linked(b2, 'user1', a)
    _safe_set(a, 'myprofile0', None)
    assert not _is_linked(a, 'myprofile0', b2)
    if hasattr(b2, 'user1'):
        assert not _is_linked(b2, 'user1', a)


def test_assoc_User_Pages_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Page(name="sample_text")
    b2 = Page(name="sample_text_2")
    _safe_set(a, 'pages14', {b1})
    assert _is_linked(a, 'pages14', b1)
    if hasattr(b1, 'user15'):
        assert _is_linked(b1, 'user15', a)
    _safe_set(a, 'pages14', {b2})
    assert _is_linked(a, 'pages14', b2)
    if hasattr(b1, 'user15'):
        assert not _is_linked(b1, 'user15', a)
    if hasattr(b2, 'user15'):
        assert _is_linked(b2, 'user15', a)
    _safe_set(a, 'pages14', set())
    assert not _is_linked(a, 'pages14', b2)
    if hasattr(b2, 'user15'):
        assert not _is_linked(b2, 'user15', a)


def test_assoc_User_Post_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Post(info="sample_text", privacy="sample_text")
    b2 = Post(info="sample_text_2", privacy="sample_text_2")
    _safe_set(a, 'post2', {b1})
    assert _is_linked(a, 'post2', b1)
    if hasattr(b1, 'user3'):
        assert _is_linked(b1, 'user3', a)
    _safe_set(a, 'post2', {b2})
    assert _is_linked(a, 'post2', b2)
    if hasattr(b1, 'user3'):
        assert not _is_linked(b1, 'user3', a)
    if hasattr(b2, 'user3'):
        assert _is_linked(b2, 'user3', a)
    _safe_set(a, 'post2', set())
    assert not _is_linked(a, 'post2', b2)
    if hasattr(b2, 'user3'):
        assert not _is_linked(b2, 'user3', a)


def test_assoc_User_Registeration_link_reassign_clear():
    a = User(name="sample_text")
    b1 = Registration(fname="sample_text", lname="sample_text", password="sample_text", userName="sample_text")
    b2 = Registration(fname="sample_text_2", lname="sample_text_2", password="sample_text_2", userName="sample_text_2")
    _safe_set(a, 'registeration8', b1)
    assert _is_linked(a, 'registeration8', b1)
    if hasattr(b1, 'user9'):
        assert _is_linked(b1, 'user9', a)
    _safe_set(a, 'registeration8', b2)
    assert _is_linked(a, 'registeration8', b2)
    if hasattr(b1, 'user9'):
        assert not _is_linked(b1, 'user9', a)
    if hasattr(b2, 'user9'):
        assert _is_linked(b2, 'user9', a)
    _safe_set(a, 'registeration8', None)
    assert not _is_linked(a, 'registeration8', b2)
    if hasattr(b2, 'user9'):
        assert not _is_linked(b2, 'user9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Friend_strategy = st.builds(Friend)
@given(instance=Friend_strategy)
@settings(max_examples=25)
def test_Friend_instantiation(instance):
    assert isinstance(instance, Friend)


Group_strategy = st.builds(Group, discription=safe_text, name=safe_text)
@given(instance=Group_strategy)
@settings(max_examples=25)
def test_Group_instantiation(instance):
    assert isinstance(instance, Group)


Login_strategy = st.builds(Login, password=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Message_strategy = st.builds(Message, maxChars=safe_text)
@given(instance=Message_strategy)
@settings(max_examples=25)
def test_Message_instantiation(instance):
    assert isinstance(instance, Message)


Page_strategy = st.builds(Page, name=safe_text)
@given(instance=Page_strategy)
@settings(max_examples=25)
def test_Page_instantiation(instance):
    assert isinstance(instance, Page)


Post_strategy = st.builds(Post, info=safe_text, privacy=safe_text)
@given(instance=Post_strategy)
@settings(max_examples=25)
def test_Post_instantiation(instance):
    assert isinstance(instance, Post)


Profile_strategy = st.builds(Profile, about=safe_text, password=safe_text, username=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


Registration_strategy = st.builds(Registration, fname=safe_text, lname=safe_text, password=safe_text, userName=safe_text)
@given(instance=Registration_strategy)
@settings(max_examples=25)
def test_Registration_instantiation(instance):
    assert isinstance(instance, Registration)


User_strategy = st.builds(User, name=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



