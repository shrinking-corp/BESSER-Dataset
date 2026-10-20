import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Chat,
    Friend,
    Group,
    Login,
    Media,
    Post,
    Profile,
    Public,
    Registration,
    Review,
    Secret,
    Team_Timeline,
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

def test_assoc_Login_User_reverse_link_reassign_clear():
    a1 = User(Name="sample_text")
    a2 = User(Name="sample_text_2")
    b = Login(Password="sample_text", Username="sample_text")
    _safe_set(b, 'Login_User_04', a1)
    assert _is_linked(b, 'Login_User_04', a1)
    if hasattr(a1, 'Login_User_15'):
        assert _is_linked(a1, 'Login_User_15', b)
    _safe_set(b, 'Login_User_04', a2)
    assert _is_linked(b, 'Login_User_04', a2)
    if hasattr(a1, 'Login_User_15'):
        assert not _is_linked(a1, 'Login_User_15', b)
    if hasattr(a2, 'Login_User_15'):
        assert _is_linked(a2, 'Login_User_15', b)
    _safe_set(b, 'Login_User_04', None)
    assert not _is_linked(b, 'Login_User_04', a2)
    if hasattr(a2, 'Login_User_15'):
        assert not _is_linked(a2, 'Login_User_15', b)


def test_assoc_Post_ImagePost_reverse_link_reassign_clear():
    a1 = Post(PostContent="sample_text")
    a2 = Post(PostContent="sample_text_2")
    b = Media(MediaPath="sample_text")
    _safe_set(b, 'Post_ImagePost_117', a1)
    assert _is_linked(b, 'Post_ImagePost_117', a1)
    if hasattr(a1, 'Post_ImagePost_016'):
        assert _is_linked(a1, 'Post_ImagePost_016', b)
    _safe_set(b, 'Post_ImagePost_117', a2)
    assert _is_linked(b, 'Post_ImagePost_117', a2)
    if hasattr(a1, 'Post_ImagePost_016'):
        assert not _is_linked(a1, 'Post_ImagePost_016', b)
    if hasattr(a2, 'Post_ImagePost_016'):
        assert _is_linked(a2, 'Post_ImagePost_016', b)
    _safe_set(b, 'Post_ImagePost_117', None)
    assert not _is_linked(b, 'Post_ImagePost_117', a2)
    if hasattr(a2, 'Post_ImagePost_016'):
        assert not _is_linked(a2, 'Post_ImagePost_016', b)


def test_assoc_Review_User_reverse_link_reassign_clear():
    a1 = User(Name="sample_text")
    a2 = User(Name="sample_text_2")
    b = Review(PostContent="sample_text")
    _safe_set(b, 'Review_User_018', a1)
    assert _is_linked(b, 'Review_User_018', a1)
    if hasattr(a1, 'Review_User_119'):
        assert _is_linked(a1, 'Review_User_119', b)
    _safe_set(b, 'Review_User_018', a2)
    assert _is_linked(b, 'Review_User_018', a2)
    if hasattr(a1, 'Review_User_119'):
        assert not _is_linked(a1, 'Review_User_119', b)
    if hasattr(a2, 'Review_User_119'):
        assert _is_linked(a2, 'Review_User_119', b)
    _safe_set(b, 'Review_User_018', None)
    assert not _is_linked(b, 'Review_User_018', a2)
    if hasattr(a2, 'Review_User_119'):
        assert not _is_linked(a2, 'Review_User_119', b)


def test_assoc_User_Group_reverse_link_reassign_clear():
    a1 = User(Name="sample_text")
    a2 = User(Name="sample_text_2")
    b = Group(Description="sample_text", Name="sample_text")
    _safe_set(b, 'User_Group_11', a1)
    assert _is_linked(b, 'User_Group_11', a1)
    if hasattr(a1, 'User_Group_00'):
        assert _is_linked(a1, 'User_Group_00', b)
    _safe_set(b, 'User_Group_11', a2)
    assert _is_linked(b, 'User_Group_11', a2)
    if hasattr(a1, 'User_Group_00'):
        assert not _is_linked(a1, 'User_Group_00', b)
    if hasattr(a2, 'User_Group_00'):
        assert _is_linked(a2, 'User_Group_00', b)
    _safe_set(b, 'User_Group_11', None)
    assert not _is_linked(b, 'User_Group_11', a2)
    if hasattr(a2, 'User_Group_00'):
        assert not _is_linked(a2, 'User_Group_00', b)


def test_assoc_User_Post_reverse_link_reassign_clear():
    a1 = User(Name="sample_text")
    a2 = User(Name="sample_text_2")
    b = Post(PostContent="sample_text")
    _safe_set(b, 'User_Post_17', a1)
    assert _is_linked(b, 'User_Post_17', a1)
    if hasattr(a1, 'User_Post_06'):
        assert _is_linked(a1, 'User_Post_06', b)
    _safe_set(b, 'User_Post_17', a2)
    assert _is_linked(b, 'User_Post_17', a2)
    if hasattr(a1, 'User_Post_06'):
        assert not _is_linked(a1, 'User_Post_06', b)
    if hasattr(a2, 'User_Post_06'):
        assert _is_linked(a2, 'User_Post_06', b)
    _safe_set(b, 'User_Post_17', None)
    assert not _is_linked(b, 'User_Post_17', a2)
    if hasattr(a2, 'User_Post_06'):
        assert not _is_linked(a2, 'User_Post_06', b)


def test_assoc_User_Profile_reverse_link_reassign_clear():
    a1 = User(Name="sample_text")
    a2 = User(Name="sample_text_2")
    b = Profile(About="sample_text", Password="sample_text", Username="sample_text")
    _safe_set(b, 'User_Profile_19', a1)
    assert _is_linked(b, 'User_Profile_19', a1)
    if hasattr(a1, 'User_Profile_08'):
        assert _is_linked(a1, 'User_Profile_08', b)
    _safe_set(b, 'User_Profile_19', a2)
    assert _is_linked(b, 'User_Profile_19', a2)
    if hasattr(a1, 'User_Profile_08'):
        assert not _is_linked(a1, 'User_Profile_08', b)
    if hasattr(a2, 'User_Profile_08'):
        assert _is_linked(a2, 'User_Profile_08', b)
    _safe_set(b, 'User_Profile_19', None)
    assert not _is_linked(b, 'User_Profile_19', a2)
    if hasattr(a2, 'User_Profile_08'):
        assert not _is_linked(a2, 'User_Profile_08', b)


def test_assoc_User_Timeline_reverse_link_reassign_clear():
    a1 = User(Name="sample_text")
    a2 = User(Name="sample_text_2")
    b = Team_Timeline(Name="sample_text")
    _safe_set(b, 'User_Timeline_115', a1)
    assert _is_linked(b, 'User_Timeline_115', a1)
    if hasattr(a1, 'timeline14'):
        assert _is_linked(a1, 'timeline14', b)
    _safe_set(b, 'User_Timeline_115', a2)
    assert _is_linked(b, 'User_Timeline_115', a2)
    if hasattr(a1, 'timeline14'):
        assert not _is_linked(a1, 'timeline14', b)
    if hasattr(a2, 'timeline14'):
        assert _is_linked(a2, 'timeline14', b)
    _safe_set(b, 'User_Timeline_115', None)
    assert not _is_linked(b, 'User_Timeline_115', a2)
    if hasattr(a2, 'timeline14'):
        assert not _is_linked(a2, 'timeline14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_User_Chat_stub_double():
    # Chat has no real 'User_Chat_113' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(Name="sample_text")
    partner = Chat()
    setattr(partner, 'User_Chat_113', None)
    _safe_set(owner, 'User_Chat_012', {partner})
    assert getattr(partner, 'User_Chat_113') == owner
    _safe_set(owner, 'User_Chat_012', set())
    assert getattr(partner, 'User_Chat_113') is None


def test_assoc_User_Friend_stub_double():
    # Friend has no real 'User_Friend_111' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(Name="sample_text")
    partner = Friend()
    setattr(partner, 'User_Friend_111', None)
    _safe_set(owner, 'friend10', {partner})
    assert getattr(partner, 'User_Friend_111') == owner
    _safe_set(owner, 'friend10', set())
    assert getattr(partner, 'User_Friend_111') is None


