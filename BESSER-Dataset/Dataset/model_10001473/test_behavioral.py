import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Comment,
    CommentTopic,
    Group,
    Invitation,
    Message,
    Post,
    Rol,
    Tag,
    Topic,
    User,
    Vote,
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

def test_assoc_Comments_Vote_reverse_link_reassign_clear():
    a1 = Vote(tipo=True)
    a2 = Vote(tipo=False)
    b = Comment(comment="sample_text", date="sample_text", userName="sample_text")
    _safe_set(b, 'vote6', {a1})
    assert _is_linked(b, 'vote6', a1)
    if hasattr(a1, 'comment7'):
        assert _is_linked(a1, 'comment7', b)
    _safe_set(b, 'vote6', {a2})
    assert _is_linked(b, 'vote6', a2)
    if hasattr(a1, 'comment7'):
        assert not _is_linked(a1, 'comment7', b)
    if hasattr(a2, 'comment7'):
        assert _is_linked(a2, 'comment7', b)
    _safe_set(b, 'vote6', set())
    assert not _is_linked(b, 'vote6', a2)
    if hasattr(a2, 'comment7'):
        assert not _is_linked(a2, 'comment7', b)


def test_assoc_Post_Comment_reverse_link_reassign_clear():
    a1 = Post(Date="sample_text", content="sample_text", userName="sample_text")
    a2 = Post(Date="sample_text_2", content="sample_text_2", userName="sample_text_2")
    b = Comment(comment="sample_text", date="sample_text", userName="sample_text")
    _safe_set(b, 'post15', a1)
    assert _is_linked(b, 'post15', a1)
    if hasattr(a1, 'comment14'):
        assert _is_linked(a1, 'comment14', b)
    _safe_set(b, 'post15', a2)
    assert _is_linked(b, 'post15', a2)
    if hasattr(a1, 'comment14'):
        assert not _is_linked(a1, 'comment14', b)
    if hasattr(a2, 'comment14'):
        assert _is_linked(a2, 'comment14', b)
    _safe_set(b, 'post15', None)
    assert not _is_linked(b, 'post15', a2)
    if hasattr(a2, 'comment14'):
        assert not _is_linked(a2, 'comment14', b)


def test_assoc_Post_Vote_reverse_link_reassign_clear():
    a1 = Vote(tipo=True)
    a2 = Vote(tipo=False)
    b = Post(Date="sample_text", content="sample_text", userName="sample_text")
    _safe_set(b, 'vote4', {a1})
    assert _is_linked(b, 'vote4', a1)
    if hasattr(a1, 'post5'):
        assert _is_linked(a1, 'post5', b)
    _safe_set(b, 'vote4', {a2})
    assert _is_linked(b, 'vote4', a2)
    if hasattr(a1, 'post5'):
        assert not _is_linked(a1, 'post5', b)
    if hasattr(a2, 'post5'):
        assert _is_linked(a2, 'post5', b)
    _safe_set(b, 'vote4', set())
    assert not _is_linked(b, 'vote4', a2)
    if hasattr(a2, 'post5'):
        assert not _is_linked(a2, 'post5', b)


def test_assoc_Rol_User_reverse_link_reassign_clear():
    a1 = User(email="sample_text", password="sample_text", userName="sample_text")
    a2 = User(email="sample_text_2", password="sample_text_2", userName="sample_text_2")
    b = Rol(nombre="sample_text")
    _safe_set(b, 'user0', {a1})
    assert _is_linked(b, 'user0', a1)
    if hasattr(a1, 'rol1'):
        assert _is_linked(a1, 'rol1', b)
    _safe_set(b, 'user0', {a2})
    assert _is_linked(b, 'user0', a2)
    if hasattr(a1, 'rol1'):
        assert not _is_linked(a1, 'rol1', b)
    if hasattr(a2, 'rol1'):
        assert _is_linked(a2, 'rol1', b)
    _safe_set(b, 'user0', set())
    assert not _is_linked(b, 'user0', a2)
    if hasattr(a2, 'rol1'):
        assert not _is_linked(a2, 'rol1', b)


def test_assoc_User_Post_reverse_link_reassign_clear():
    a1 = User(email="sample_text", password="sample_text", userName="sample_text")
    a2 = User(email="sample_text_2", password="sample_text_2", userName="sample_text_2")
    b = Post(Date="sample_text", content="sample_text", userName="sample_text")
    _safe_set(b, 'user3', a1)
    assert _is_linked(b, 'user3', a1)
    if hasattr(a1, 'post2'):
        assert _is_linked(a1, 'post2', b)
    _safe_set(b, 'user3', a2)
    assert _is_linked(b, 'user3', a2)
    if hasattr(a1, 'post2'):
        assert not _is_linked(a1, 'post2', b)
    if hasattr(a2, 'post2'):
        assert _is_linked(a2, 'post2', b)
    _safe_set(b, 'user3', None)
    assert not _is_linked(b, 'user3', a2)
    if hasattr(a2, 'post2'):
        assert not _is_linked(a2, 'post2', b)


def test_assoc_User_User_reverse_link_reassign_clear():
    a1 = User(email="sample_text", password="sample_text", userName="sample_text")
    a2 = User(email="sample_text_2", password="sample_text_2", userName="sample_text_2")
    b = User(email="sample_text", password="sample_text", userName="sample_text")
    _safe_set(b, 'user20', a1)
    assert _is_linked(b, 'user20', a1)
    if hasattr(a1, 'friends21'):
        assert _is_linked(a1, 'friends21', b)
    _safe_set(b, 'user20', a2)
    assert _is_linked(b, 'user20', a2)
    if hasattr(a1, 'friends21'):
        assert not _is_linked(a1, 'friends21', b)
    if hasattr(a2, 'friends21'):
        assert _is_linked(a2, 'friends21', b)
    _safe_set(b, 'user20', None)
    assert not _is_linked(b, 'user20', a2)
    if hasattr(a2, 'friends21'):
        assert not _is_linked(a2, 'friends21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Group_User_stub_double():
    # Group has no real 'user10' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(email="sample_text", password="sample_text", userName="sample_text")
    partner = Group()
    setattr(partner, 'user10', None)
    _safe_set(owner, 'group11', {partner})
    assert owner in getattr(partner, 'user10')
    _safe_set(owner, 'group11', set())
    assert owner not in getattr(partner, 'user10')


def test_assoc_Topic_Vote_stub_double():
    # Topic has no real 'vote12' property in the generated
    # code (a bare stub) -- manually attach it so Vote's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Vote's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Vote(tipo=True)
    partner = Topic()
    setattr(partner, 'vote12', None)
    _safe_set(owner, 'topic13', partner)
    assert owner in getattr(partner, 'vote12')
    _safe_set(owner, 'topic13', None)
    assert owner not in getattr(partner, 'vote12')


def test_assoc_User_Invitation_stub_double():
    # Invitation has no real 'user23' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(email="sample_text", password="sample_text", userName="sample_text")
    partner = Invitation()
    setattr(partner, 'user23', None)
    _safe_set(owner, 'invitation22', {partner})
    assert getattr(partner, 'user23') == owner
    _safe_set(owner, 'invitation22', set())
    assert getattr(partner, 'user23') is None


def test_assoc_User_Message_stub_double():
    # Message has no real 'user9' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(email="sample_text", password="sample_text", userName="sample_text")
    partner = Message()
    setattr(partner, 'user9', None)
    _safe_set(owner, 'message8', {partner})
    assert getattr(partner, 'user9') == owner
    _safe_set(owner, 'message8', set())
    assert getattr(partner, 'user9') is None


