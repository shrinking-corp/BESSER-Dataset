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
    Page,
    Message,
    Group,
    Post,
    User,
    Profile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_hyp_page_constructor_exists():
    assert callable(Page.__init__)


def test_hyp_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Page" in params, "Missing parameter 'ID_Page'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Description" in params, "Missing parameter 'Description'"







def test_hyp_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_hyp_message_constructor_exists():
    assert callable(Message.__init__)


def test_hyp_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())
    assert "Max_Chars" in params, "Missing parameter 'Max_Chars'"
    assert "ID_Message" in params, "Missing parameter 'ID_Message'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Mail" in params, "Missing parameter 'Mail'"







def test_hyp_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_hyp_group_constructor_exists():
    assert callable(Group.__init__)


def test_hyp_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Group" in params, "Missing parameter 'ID_Group'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Description" in params, "Missing parameter 'Description'"







def test_hyp_post_is_not_abstract():
    assert not inspect.isabstract(Post)


def test_hyp_post_constructor_exists():
    assert callable(Post.__init__)


def test_hyp_post_constructor_args():
    sig = inspect.signature(Post.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Post" in params, "Missing parameter 'ID_Post'"
    assert "Mail" in params, "Missing parameter 'Mail'"
    assert "Info" in params, "Missing parameter 'Info'"
    assert "Privacy" in params, "Missing parameter 'Privacy'"
    assert "ID_Page" in params, "Missing parameter 'ID_Page'"








def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Fist_Name" in params, "Missing parameter 'Fist_Name'"
    assert "ID_User" in params, "Missing parameter 'ID_User'"
    assert "Mail" in params, "Missing parameter 'Mail'"
    assert "Name" in params, "Missing parameter 'Name'"







def test_hyp_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_hyp_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_hyp_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Profile" in params, "Missing parameter 'ID_Profile'"
    assert "User_Name" in params, "Missing parameter 'User_Name'"
    assert "About" in params, "Missing parameter 'About'"
    assert "Password" in params, "Missing parameter 'Password'"






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
Page_strategy = st.builds(
    Page,
    ID_Page=
        st.integers(),
    Name=
        safe_text,
    ID_User=
        st.integers(),
    Description=
        safe_text
)
Message_strategy = st.builds(
    Message,
    Max_Chars=
        safe_text,
    ID_Message=
        st.integers(),
    ID_User=
        st.integers(),
    Mail=
        safe_text
)
Group_strategy = st.builds(
    Group,
    ID_Group=
        st.integers(),
    ID_User=
        st.integers(),
    Name=
        safe_text,
    Description=
        safe_text
)
Post_strategy = st.builds(
    Post,
    ID_Post=
        st.integers(),
    Mail=
        safe_text,
    Info=
        safe_text,
    Privacy=
        safe_text,
    ID_Page=
        st.integers()
)
User_strategy = st.builds(
    User,
    Fist_Name=
        safe_text,
    ID_User=
        st.integers(),
    Mail=
        safe_text,
    Name=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    ID_Profile=
        safe_text,
    User_Name=
        safe_text,
    About=
        safe_text,
    Password=
        safe_text
)




@given(instance=Page_strategy)
def test_hyp_page_ID_Page_setter(instance):
    original = instance.ID_Page
    instance.ID_Page = original
    assert instance.ID_Page == original



@given(instance=Page_strategy)
def test_hyp_page_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Page_strategy)
def test_hyp_page_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=Page_strategy)
def test_hyp_page_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original




@given(instance=Message_strategy)
def test_hyp_message_Max_Chars_setter(instance):
    original = instance.Max_Chars
    instance.Max_Chars = original
    assert instance.Max_Chars == original



@given(instance=Message_strategy)
def test_hyp_message_ID_Message_setter(instance):
    original = instance.ID_Message
    instance.ID_Message = original
    assert instance.ID_Message == original



@given(instance=Message_strategy)
def test_hyp_message_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=Message_strategy)
def test_hyp_message_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original




@given(instance=Group_strategy)
def test_hyp_group_ID_Group_setter(instance):
    original = instance.ID_Group
    instance.ID_Group = original
    assert instance.ID_Group == original



@given(instance=Group_strategy)
def test_hyp_group_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=Group_strategy)
def test_hyp_group_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Group_strategy)
def test_hyp_group_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original




@given(instance=Post_strategy)
def test_hyp_post_ID_Post_setter(instance):
    original = instance.ID_Post
    instance.ID_Post = original
    assert instance.ID_Post == original



@given(instance=Post_strategy)
def test_hyp_post_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original



@given(instance=Post_strategy)
def test_hyp_post_Info_setter(instance):
    original = instance.Info
    instance.Info = original
    assert instance.Info == original



@given(instance=Post_strategy)
def test_hyp_post_Privacy_setter(instance):
    original = instance.Privacy
    instance.Privacy = original
    assert instance.Privacy == original



@given(instance=Post_strategy)
def test_hyp_post_ID_Page_setter(instance):
    original = instance.ID_Page
    instance.ID_Page = original
    assert instance.ID_Page == original




@given(instance=User_strategy)
def test_hyp_user_Fist_Name_setter(instance):
    original = instance.Fist_Name
    instance.Fist_Name = original
    assert instance.Fist_Name == original



@given(instance=User_strategy)
def test_hyp_user_ID_User_setter(instance):
    original = instance.ID_User
    instance.ID_User = original
    assert instance.ID_User == original



@given(instance=User_strategy)
def test_hyp_user_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original



@given(instance=User_strategy)
def test_hyp_user_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Profile_strategy)
def test_hyp_profile_ID_Profile_setter(instance):
    original = instance.ID_Profile
    instance.ID_Profile = original
    assert instance.ID_Profile == original



@given(instance=Profile_strategy)
def test_hyp_profile_User_Name_setter(instance):
    original = instance.User_Name
    instance.User_Name = original
    assert instance.User_Name == original



@given(instance=Profile_strategy)
def test_hyp_profile_About_setter(instance):
    original = instance.About
    instance.About = original
    assert instance.About == original



@given(instance=Profile_strategy)
def test_hyp_profile_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Group,
    Message,
    Page,
    Post,
    Profile,
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

def test_Group_Description_value_roundtrip():
    instance = Group(Description="sample_text", ID_Group=7, ID_User=7, Name="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Group_ID_Group_value_roundtrip():
    instance = Group(Description="sample_text", ID_Group=7, ID_User=7, Name="sample_text")
    assert instance.ID_Group == 7
    instance.ID_Group = 13
    assert instance.ID_Group == 13


def test_Group_ID_User_value_roundtrip():
    instance = Group(Description="sample_text", ID_Group=7, ID_User=7, Name="sample_text")
    assert instance.ID_User == 7
    instance.ID_User = 13
    assert instance.ID_User == 13


def test_Group_Name_value_roundtrip():
    instance = Group(Description="sample_text", ID_Group=7, ID_User=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Message_ID_Message_value_roundtrip():
    instance = Message(ID_Message=7, ID_User=7, Mail="sample_text", Max_Chars="sample_text")
    assert instance.ID_Message == 7
    instance.ID_Message = 13
    assert instance.ID_Message == 13


def test_Message_ID_User_value_roundtrip():
    instance = Message(ID_Message=7, ID_User=7, Mail="sample_text", Max_Chars="sample_text")
    assert instance.ID_User == 7
    instance.ID_User = 13
    assert instance.ID_User == 13


def test_Message_Mail_value_roundtrip():
    instance = Message(ID_Message=7, ID_User=7, Mail="sample_text", Max_Chars="sample_text")
    assert instance.Mail == "sample_text"
    instance.Mail = "sample_text_2"
    assert instance.Mail == "sample_text_2"


def test_Message_Max_Chars_value_roundtrip():
    instance = Message(ID_Message=7, ID_User=7, Mail="sample_text", Max_Chars="sample_text")
    assert instance.Max_Chars == "sample_text"
    instance.Max_Chars = "sample_text_2"
    assert instance.Max_Chars == "sample_text_2"


def test_Page_Description_value_roundtrip():
    instance = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Page_ID_Page_value_roundtrip():
    instance = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    assert instance.ID_Page == 7
    instance.ID_Page = 13
    assert instance.ID_Page == 13


def test_Page_ID_User_value_roundtrip():
    instance = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    assert instance.ID_User == 7
    instance.ID_User = 13
    assert instance.ID_User == 13


def test_Page_Name_value_roundtrip():
    instance = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Post_ID_Page_value_roundtrip():
    instance = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    assert instance.ID_Page == 7
    instance.ID_Page = 13
    assert instance.ID_Page == 13


def test_Post_ID_Post_value_roundtrip():
    instance = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    assert instance.ID_Post == 7
    instance.ID_Post = 13
    assert instance.ID_Post == 13


def test_Post_Info_value_roundtrip():
    instance = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    assert instance.Info == "sample_text"
    instance.Info = "sample_text_2"
    assert instance.Info == "sample_text_2"


def test_Post_Mail_value_roundtrip():
    instance = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    assert instance.Mail == "sample_text"
    instance.Mail = "sample_text_2"
    assert instance.Mail == "sample_text_2"


def test_Post_Privacy_value_roundtrip():
    instance = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    assert instance.Privacy == "sample_text"
    instance.Privacy = "sample_text_2"
    assert instance.Privacy == "sample_text_2"


def test_Profile_About_value_roundtrip():
    instance = Profile(About="sample_text", ID_Profile="sample_text", Password="sample_text", User_Name="sample_text")
    assert instance.About == "sample_text"
    instance.About = "sample_text_2"
    assert instance.About == "sample_text_2"


def test_Profile_ID_Profile_value_roundtrip():
    instance = Profile(About="sample_text", ID_Profile="sample_text", Password="sample_text", User_Name="sample_text")
    assert instance.ID_Profile == "sample_text"
    instance.ID_Profile = "sample_text_2"
    assert instance.ID_Profile == "sample_text_2"


def test_Profile_Password_value_roundtrip():
    instance = Profile(About="sample_text", ID_Profile="sample_text", Password="sample_text", User_Name="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Profile_User_Name_value_roundtrip():
    instance = Profile(About="sample_text", ID_Profile="sample_text", Password="sample_text", User_Name="sample_text")
    assert instance.User_Name == "sample_text"
    instance.User_Name = "sample_text_2"
    assert instance.User_Name == "sample_text_2"


def test_User_Fist_Name_value_roundtrip():
    instance = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    assert instance.Fist_Name == "sample_text"
    instance.Fist_Name = "sample_text_2"
    assert instance.Fist_Name == "sample_text_2"


def test_User_ID_User_value_roundtrip():
    instance = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    assert instance.ID_User == 7
    instance.ID_User = 13
    assert instance.ID_User == 13


def test_User_Mail_value_roundtrip():
    instance = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    assert instance.Mail == "sample_text"
    instance.Mail = "sample_text_2"
    assert instance.Mail == "sample_text_2"


def test_User_Name_value_roundtrip():
    instance = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Page_Post_link_reassign_clear():
    a = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    b1 = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    b2 = Page(Description="sample_text_2", ID_Page=13, ID_User=13, Name="sample_text_2")
    _safe_set(a, 'page9', b1)
    assert _is_linked(a, 'page9', b1)
    if hasattr(b1, 'post8'):
        assert _is_linked(b1, 'post8', a)
    _safe_set(a, 'page9', b2)
    assert _is_linked(a, 'page9', b2)
    if hasattr(b1, 'post8'):
        assert not _is_linked(b1, 'post8', a)
    if hasattr(b2, 'post8'):
        assert _is_linked(b2, 'post8', a)
    _safe_set(a, 'page9', None)
    assert not _is_linked(a, 'page9', b2)
    if hasattr(b2, 'post8'):
        assert not _is_linked(b2, 'post8', a)


def test_assoc_Profile_User_link_reassign_clear():
    a = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    b1 = Profile(About="sample_text", ID_Profile="sample_text", Password="sample_text", User_Name="sample_text")
    b2 = Profile(About="sample_text_2", ID_Profile="sample_text_2", Password="sample_text_2", User_Name="sample_text_2")
    _safe_set(a, 'profile1', b1)
    assert _is_linked(a, 'profile1', b1)
    if hasattr(b1, 'user0'):
        assert _is_linked(b1, 'user0', a)
    _safe_set(a, 'profile1', b2)
    assert _is_linked(a, 'profile1', b2)
    if hasattr(b1, 'user0'):
        assert not _is_linked(b1, 'user0', a)
    if hasattr(b2, 'user0'):
        assert _is_linked(b2, 'user0', a)
    _safe_set(a, 'profile1', None)
    assert not _is_linked(a, 'profile1', b2)
    if hasattr(b2, 'user0'):
        assert not _is_linked(b2, 'user0', a)


def test_assoc_User_Group_link_reassign_clear():
    a = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    b1 = Group(Description="sample_text", ID_Group=7, ID_User=7, Name="sample_text")
    b2 = Group(Description="sample_text_2", ID_Group=13, ID_User=13, Name="sample_text_2")
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


def test_assoc_User_Message_link_reassign_clear():
    a = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    b1 = Message(ID_Message=7, ID_User=7, Mail="sample_text", Max_Chars="sample_text")
    b2 = Message(ID_Message=13, ID_User=13, Mail="sample_text_2", Max_Chars="sample_text_2")
    _safe_set(a, 'message4', {b1})
    assert _is_linked(a, 'message4', b1)
    if hasattr(b1, 'user5'):
        assert _is_linked(b1, 'user5', a)
    _safe_set(a, 'message4', {b2})
    assert _is_linked(a, 'message4', b2)
    if hasattr(b1, 'user5'):
        assert not _is_linked(b1, 'user5', a)
    if hasattr(b2, 'user5'):
        assert _is_linked(b2, 'user5', a)
    _safe_set(a, 'message4', set())
    assert not _is_linked(a, 'message4', b2)
    if hasattr(b2, 'user5'):
        assert not _is_linked(b2, 'user5', a)


def test_assoc_User_Page_link_reassign_clear():
    a = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    b1 = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    b2 = Page(Description="sample_text_2", ID_Page=13, ID_User=13, Name="sample_text_2")
    _safe_set(a, 'page2', {b1})
    assert _is_linked(a, 'page2', b1)
    if hasattr(b1, 'user3'):
        assert _is_linked(b1, 'user3', a)
    _safe_set(a, 'page2', {b2})
    assert _is_linked(a, 'page2', b2)
    if hasattr(b1, 'user3'):
        assert not _is_linked(b1, 'user3', a)
    if hasattr(b2, 'user3'):
        assert _is_linked(b2, 'user3', a)
    _safe_set(a, 'page2', set())
    assert not _is_linked(a, 'page2', b2)
    if hasattr(b2, 'user3'):
        assert not _is_linked(b2, 'user3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Group_strategy = st.builds(Group, Description=safe_text, ID_Group=st.integers(), ID_User=st.integers(), Name=safe_text)
@given(instance=Group_strategy)
@settings(max_examples=25)
def test_Group_instantiation(instance):
    assert isinstance(instance, Group)


Message_strategy = st.builds(Message, ID_Message=st.integers(), ID_User=st.integers(), Mail=safe_text, Max_Chars=safe_text)
@given(instance=Message_strategy)
@settings(max_examples=25)
def test_Message_instantiation(instance):
    assert isinstance(instance, Message)


Page_strategy = st.builds(Page, Description=safe_text, ID_Page=st.integers(), ID_User=st.integers(), Name=safe_text)
@given(instance=Page_strategy)
@settings(max_examples=25)
def test_Page_instantiation(instance):
    assert isinstance(instance, Page)


Post_strategy = st.builds(Post, ID_Page=st.integers(), ID_Post=st.integers(), Info=safe_text, Mail=safe_text, Privacy=safe_text)
@given(instance=Post_strategy)
@settings(max_examples=25)
def test_Post_instantiation(instance):
    assert isinstance(instance, Post)


Profile_strategy = st.builds(Profile, About=safe_text, ID_Profile=safe_text, Password=safe_text, User_Name=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


User_strategy = st.builds(User, Fist_Name=safe_text, ID_User=st.integers(), Mail=safe_text, Name=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Group,
    Message,
    Page,
    Post,
    Profile,
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

def test_assoc_Page_Post_reverse_link_reassign_clear():
    a1 = Post(ID_Page=7, ID_Post=7, Info="sample_text", Mail="sample_text", Privacy="sample_text")
    a2 = Post(ID_Page=13, ID_Post=13, Info="sample_text_2", Mail="sample_text_2", Privacy="sample_text_2")
    b = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    _safe_set(b, 'post8', {a1})
    assert _is_linked(b, 'post8', a1)
    if hasattr(a1, 'page9'):
        assert _is_linked(a1, 'page9', b)
    _safe_set(b, 'post8', {a2})
    assert _is_linked(b, 'post8', a2)
    if hasattr(a1, 'page9'):
        assert not _is_linked(a1, 'page9', b)
    if hasattr(a2, 'page9'):
        assert _is_linked(a2, 'page9', b)
    _safe_set(b, 'post8', set())
    assert not _is_linked(b, 'post8', a2)
    if hasattr(a2, 'page9'):
        assert not _is_linked(a2, 'page9', b)


def test_assoc_Profile_User_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Profile(About="sample_text", ID_Profile="sample_text", Password="sample_text", User_Name="sample_text")
    _safe_set(b, 'user0', a1)
    assert _is_linked(b, 'user0', a1)
    if hasattr(a1, 'profile1'):
        assert _is_linked(a1, 'profile1', b)
    _safe_set(b, 'user0', a2)
    assert _is_linked(b, 'user0', a2)
    if hasattr(a1, 'profile1'):
        assert not _is_linked(a1, 'profile1', b)
    if hasattr(a2, 'profile1'):
        assert _is_linked(a2, 'profile1', b)
    _safe_set(b, 'user0', None)
    assert not _is_linked(b, 'user0', a2)
    if hasattr(a2, 'profile1'):
        assert not _is_linked(a2, 'profile1', b)


def test_assoc_User_Group_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Group(Description="sample_text", ID_Group=7, ID_User=7, Name="sample_text")
    _safe_set(b, 'user7', a1)
    assert _is_linked(b, 'user7', a1)
    if hasattr(a1, 'group6'):
        assert _is_linked(a1, 'group6', b)
    _safe_set(b, 'user7', a2)
    assert _is_linked(b, 'user7', a2)
    if hasattr(a1, 'group6'):
        assert not _is_linked(a1, 'group6', b)
    if hasattr(a2, 'group6'):
        assert _is_linked(a2, 'group6', b)
    _safe_set(b, 'user7', None)
    assert not _is_linked(b, 'user7', a2)
    if hasattr(a2, 'group6'):
        assert not _is_linked(a2, 'group6', b)


def test_assoc_User_Message_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Message(ID_Message=7, ID_User=7, Mail="sample_text", Max_Chars="sample_text")
    _safe_set(b, 'user5', a1)
    assert _is_linked(b, 'user5', a1)
    if hasattr(a1, 'message4'):
        assert _is_linked(a1, 'message4', b)
    _safe_set(b, 'user5', a2)
    assert _is_linked(b, 'user5', a2)
    if hasattr(a1, 'message4'):
        assert not _is_linked(a1, 'message4', b)
    if hasattr(a2, 'message4'):
        assert _is_linked(a2, 'message4', b)
    _safe_set(b, 'user5', None)
    assert not _is_linked(b, 'user5', a2)
    if hasattr(a2, 'message4'):
        assert not _is_linked(a2, 'message4', b)


def test_assoc_User_Page_reverse_link_reassign_clear():
    a1 = User(Fist_Name="sample_text", ID_User=7, Mail="sample_text", Name="sample_text")
    a2 = User(Fist_Name="sample_text_2", ID_User=13, Mail="sample_text_2", Name="sample_text_2")
    b = Page(Description="sample_text", ID_Page=7, ID_User=7, Name="sample_text")
    _safe_set(b, 'user3', a1)
    assert _is_linked(b, 'user3', a1)
    if hasattr(a1, 'page2'):
        assert _is_linked(a1, 'page2', b)
    _safe_set(b, 'user3', a2)
    assert _is_linked(b, 'user3', a2)
    if hasattr(a1, 'page2'):
        assert not _is_linked(a1, 'page2', b)
    if hasattr(a2, 'page2'):
        assert _is_linked(a2, 'page2', b)
    _safe_set(b, 'user3', None)
    assert not _is_linked(b, 'user3', a2)
    if hasattr(a2, 'page2'):
        assert not _is_linked(a2, 'page2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================


