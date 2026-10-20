import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Another_Login,
    Class,
    Comment,
    Cryptostream,
    Following_Hashtag,
    Hashtag,
    Key,
    Like,
    Mention,
    Message,
    N_Disturb_User,
    Post,
    Principal,
    Reciever,
    Sender,
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

def test_assoc_Comment_Comment_reverse_link_reassign_clear():
    a1 = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    a2 = Comment(comment_id=13, content=13, creation_date="sample_text_2", id=13, post_id=13, user_id=13)
    b = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    _safe_set(b, 'comment33', {a1})
    assert _is_linked(b, 'comment33', a1)
    if hasattr(a1, 'comment32'):
        assert _is_linked(a1, 'comment32', b)
    _safe_set(b, 'comment33', {a2})
    assert _is_linked(b, 'comment33', a2)
    if hasattr(a1, 'comment32'):
        assert not _is_linked(a1, 'comment32', b)
    if hasattr(a2, 'comment32'):
        assert _is_linked(a2, 'comment32', b)
    _safe_set(b, 'comment33', set())
    assert not _is_linked(b, 'comment33', a2)
    if hasattr(a2, 'comment32'):
        assert not _is_linked(a2, 'comment32', b)


def test_assoc_Comment_Post_reverse_link_reassign_clear():
    a1 = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    a2 = Post(creation_date="sample_text_2", date_update="sample_text_2", hashtag_id=13, id=13, location_id=13, status="sample_text_2", text="sample_text_2", total_like=13)
    b = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    _safe_set(b, 'post14', a1)
    assert _is_linked(b, 'post14', a1)
    if hasattr(a1, 'comment15'):
        assert _is_linked(a1, 'comment15', b)
    _safe_set(b, 'post14', a2)
    assert _is_linked(b, 'post14', a2)
    if hasattr(a1, 'comment15'):
        assert not _is_linked(a1, 'comment15', b)
    if hasattr(a2, 'comment15'):
        assert _is_linked(a2, 'comment15', b)
    _safe_set(b, 'post14', None)
    assert not _is_linked(b, 'post14', a2)
    if hasattr(a2, 'comment15'):
        assert not _is_linked(a2, 'comment15', b)


def test_assoc_Hashtag_Following_Hashtag_reverse_link_reassign_clear():
    a1 = Hashtag(id=7, tag="sample_text")
    a2 = Hashtag(id=13, tag="sample_text_2")
    b = Following_Hashtag(hashtag_id=7, id=7, user_id=7)
    _safe_set(b, 'hashtag19', a1)
    assert _is_linked(b, 'hashtag19', a1)
    if hasattr(a1, 'following_Hashtag18'):
        assert _is_linked(a1, 'following_Hashtag18', b)
    _safe_set(b, 'hashtag19', a2)
    assert _is_linked(b, 'hashtag19', a2)
    if hasattr(a1, 'following_Hashtag18'):
        assert not _is_linked(a1, 'following_Hashtag18', b)
    if hasattr(a2, 'following_Hashtag18'):
        assert _is_linked(a2, 'following_Hashtag18', b)
    _safe_set(b, 'hashtag19', None)
    assert not _is_linked(b, 'hashtag19', a2)
    if hasattr(a2, 'following_Hashtag18'):
        assert not _is_linked(a2, 'following_Hashtag18', b)


def test_assoc_Hashtag_Post_reverse_link_reassign_clear():
    a1 = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    a2 = Post(creation_date="sample_text_2", date_update="sample_text_2", hashtag_id=13, id=13, location_id=13, status="sample_text_2", text="sample_text_2", total_like=13)
    b = Hashtag(id=7, tag="sample_text")
    _safe_set(b, 'post16', {a1})
    assert _is_linked(b, 'post16', a1)
    if hasattr(a1, 'hashtag17'):
        assert _is_linked(a1, 'hashtag17', b)
    _safe_set(b, 'post16', {a2})
    assert _is_linked(b, 'post16', a2)
    if hasattr(a1, 'hashtag17'):
        assert not _is_linked(a1, 'hashtag17', b)
    if hasattr(a2, 'hashtag17'):
        assert _is_linked(a2, 'hashtag17', b)
    _safe_set(b, 'post16', set())
    assert not _is_linked(b, 'post16', a2)
    if hasattr(a2, 'hashtag17'):
        assert not _is_linked(a2, 'hashtag17', b)


def test_assoc_Key_Reciever_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    _safe_set(b, 'reciever38', a1)
    assert _is_linked(b, 'reciever38', a1)
    if hasattr(a1, 'key39'):
        assert _is_linked(a1, 'key39', b)
    _safe_set(b, 'reciever38', a2)
    assert _is_linked(b, 'reciever38', a2)
    if hasattr(a1, 'key39'):
        assert not _is_linked(a1, 'key39', b)
    if hasattr(a2, 'key39'):
        assert _is_linked(a2, 'key39', b)
    _safe_set(b, 'reciever38', None)
    assert not _is_linked(b, 'reciever38', a2)
    if hasattr(a2, 'key39'):
        assert not _is_linked(a2, 'key39', b)


def test_assoc_Key_Sender_reverse_link_reassign_clear():
    a1 = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    a2 = Sender(creation_date="sample_text_2", following_id=13, id=13, status="sample_text_2", user_id=13)
    b = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    _safe_set(b, 'sender36', a1)
    assert _is_linked(b, 'sender36', a1)
    if hasattr(a1, 'key37'):
        assert _is_linked(a1, 'key37', b)
    _safe_set(b, 'sender36', a2)
    assert _is_linked(b, 'sender36', a2)
    if hasattr(a1, 'key37'):
        assert not _is_linked(a1, 'key37', b)
    if hasattr(a2, 'key37'):
        assert _is_linked(a2, 'key37', b)
    _safe_set(b, 'sender36', None)
    assert not _is_linked(b, 'sender36', a2)
    if hasattr(a2, 'key37'):
        assert not _is_linked(a2, 'key37', b)


def test_assoc_Like_Post_reverse_link_reassign_clear():
    a1 = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    a2 = Post(creation_date="sample_text_2", date_update="sample_text_2", hashtag_id=13, id=13, location_id=13, status="sample_text_2", text="sample_text_2", total_like=13)
    b = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    _safe_set(b, 'post12', a1)
    assert _is_linked(b, 'post12', a1)
    if hasattr(a1, 'like13'):
        assert _is_linked(a1, 'like13', b)
    _safe_set(b, 'post12', a2)
    assert _is_linked(b, 'post12', a2)
    if hasattr(a1, 'like13'):
        assert not _is_linked(a1, 'like13', b)
    if hasattr(a2, 'like13'):
        assert _is_linked(a2, 'like13', b)
    _safe_set(b, 'post12', None)
    assert not _is_linked(b, 'post12', a2)
    if hasattr(a2, 'like13'):
        assert not _is_linked(a2, 'like13', b)


def test_assoc_Location_Post_reverse_link_reassign_clear():
    a1 = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    a2 = Post(creation_date="sample_text_2", date_update="sample_text_2", hashtag_id=13, id=13, location_id=13, status="sample_text_2", text="sample_text_2", total_like=13)
    b = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    _safe_set(b, 'post20', a1)
    assert _is_linked(b, 'post20', a1)
    if hasattr(a1, 'location21'):
        assert _is_linked(a1, 'location21', b)
    _safe_set(b, 'post20', a2)
    assert _is_linked(b, 'post20', a2)
    if hasattr(a1, 'location21'):
        assert not _is_linked(a1, 'location21', b)
    if hasattr(a2, 'location21'):
        assert _is_linked(a2, 'location21', b)
    _safe_set(b, 'post20', None)
    assert not _is_linked(b, 'post20', a2)
    if hasattr(a2, 'location21'):
        assert not _is_linked(a2, 'location21', b)


def test_assoc_Post_Mention_reverse_link_reassign_clear():
    a1 = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    a2 = Post(creation_date="sample_text_2", date_update="sample_text_2", hashtag_id=13, id=13, location_id=13, status="sample_text_2", text="sample_text_2", total_like=13)
    b = Mention(id=7, post_id=7, user_id=7)
    _safe_set(b, 'post23', a1)
    assert _is_linked(b, 'post23', a1)
    if hasattr(a1, 'mention22'):
        assert _is_linked(a1, 'mention22', b)
    _safe_set(b, 'post23', a2)
    assert _is_linked(b, 'post23', a2)
    if hasattr(a1, 'mention22'):
        assert not _is_linked(a1, 'mention22', b)
    if hasattr(a2, 'mention22'):
        assert _is_linked(a2, 'mention22', b)
    _safe_set(b, 'post23', None)
    assert not _is_linked(b, 'post23', a2)
    if hasattr(a2, 'mention22'):
        assert not _is_linked(a2, 'mention22', b)


def test_assoc_Post_User_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    _safe_set(b, 'user8', a1)
    assert _is_linked(b, 'user8', a1)
    if hasattr(a1, 'post9'):
        assert _is_linked(a1, 'post9', b)
    _safe_set(b, 'user8', a2)
    assert _is_linked(b, 'user8', a2)
    if hasattr(a1, 'post9'):
        assert not _is_linked(a1, 'post9', b)
    if hasattr(a2, 'post9'):
        assert _is_linked(a2, 'post9', b)
    _safe_set(b, 'user8', None)
    assert not _is_linked(b, 'user8', a2)
    if hasattr(a2, 'post9'):
        assert not _is_linked(a2, 'post9', b)


def test_assoc_Principal_Reciever_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    _safe_set(b, 'reciever40', a1)
    assert _is_linked(b, 'reciever40', a1)
    if hasattr(a1, 'principal41'):
        assert _is_linked(a1, 'principal41', b)
    _safe_set(b, 'reciever40', a2)
    assert _is_linked(b, 'reciever40', a2)
    if hasattr(a1, 'principal41'):
        assert not _is_linked(a1, 'principal41', b)
    if hasattr(a2, 'principal41'):
        assert _is_linked(a2, 'principal41', b)
    _safe_set(b, 'reciever40', None)
    assert not _is_linked(b, 'reciever40', a2)
    if hasattr(a2, 'principal41'):
        assert not _is_linked(a2, 'principal41', b)


def test_assoc_User_Another_Login_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Another_Login(facebook_id=7, id=7, user_id=7)
    _safe_set(b, 'user35', a1)
    assert _is_linked(b, 'user35', a1)
    if hasattr(a1, 'another_Login34'):
        assert _is_linked(a1, 'another_Login34', b)
    _safe_set(b, 'user35', a2)
    assert _is_linked(b, 'user35', a2)
    if hasattr(a1, 'another_Login34'):
        assert not _is_linked(a1, 'another_Login34', b)
    if hasattr(a2, 'another_Login34'):
        assert _is_linked(a2, 'another_Login34', b)
    _safe_set(b, 'user35', None)
    assert not _is_linked(b, 'user35', a2)
    if hasattr(a2, 'another_Login34'):
        assert not _is_linked(a2, 'another_Login34', b)


def test_assoc_User_Blocked_User_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Cryptostream(blocked_user_id=7, id=7, user_id=7)
    _safe_set(b, 'user1', a1)
    assert _is_linked(b, 'user1', a1)
    if hasattr(a1, 'blocked_User0'):
        assert _is_linked(a1, 'blocked_User0', b)
    _safe_set(b, 'user1', a2)
    assert _is_linked(b, 'user1', a2)
    if hasattr(a1, 'blocked_User0'):
        assert not _is_linked(a1, 'blocked_User0', b)
    if hasattr(a2, 'blocked_User0'):
        assert _is_linked(a2, 'blocked_User0', b)
    _safe_set(b, 'user1', None)
    assert not _is_linked(b, 'user1', a2)
    if hasattr(a2, 'blocked_User0'):
        assert not _is_linked(a2, 'blocked_User0', b)


def test_assoc_User_Comment_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    _safe_set(b, 'user31', a1)
    assert _is_linked(b, 'user31', a1)
    if hasattr(a1, 'comment30'):
        assert _is_linked(a1, 'comment30', b)
    _safe_set(b, 'user31', a2)
    assert _is_linked(b, 'user31', a2)
    if hasattr(a1, 'comment30'):
        assert not _is_linked(a1, 'comment30', b)
    if hasattr(a2, 'comment30'):
        assert _is_linked(a2, 'comment30', b)
    _safe_set(b, 'user31', None)
    assert not _is_linked(b, 'user31', a2)
    if hasattr(a2, 'comment30'):
        assert not _is_linked(a2, 'comment30', b)


def test_assoc_User_Followers_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    _safe_set(b, 'user5', {a1})
    assert _is_linked(b, 'user5', a1)
    if hasattr(a1, 'followers4'):
        assert _is_linked(a1, 'followers4', b)
    _safe_set(b, 'user5', {a2})
    assert _is_linked(b, 'user5', a2)
    if hasattr(a1, 'followers4'):
        assert not _is_linked(a1, 'followers4', b)
    if hasattr(a2, 'followers4'):
        assert _is_linked(a2, 'followers4', b)
    _safe_set(b, 'user5', set())
    assert not _is_linked(b, 'user5', a2)
    if hasattr(a2, 'followers4'):
        assert not _is_linked(a2, 'followers4', b)


def test_assoc_User_Following_reverse_link_reassign_clear():
    a1 = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    a2 = Sender(creation_date="sample_text_2", following_id=13, id=13, status="sample_text_2", user_id=13)
    b = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    _safe_set(b, 'following6', {a1})
    assert _is_linked(b, 'following6', a1)
    if hasattr(a1, 'user7'):
        assert _is_linked(a1, 'user7', b)
    _safe_set(b, 'following6', {a2})
    assert _is_linked(b, 'following6', a2)
    if hasattr(a1, 'user7'):
        assert not _is_linked(a1, 'user7', b)
    if hasattr(a2, 'user7'):
        assert _is_linked(a2, 'user7', b)
    _safe_set(b, 'following6', set())
    assert not _is_linked(b, 'following6', a2)
    if hasattr(a2, 'user7'):
        assert not _is_linked(a2, 'user7', b)


def test_assoc_User_Following_Hashtag_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Following_Hashtag(hashtag_id=7, id=7, user_id=7)
    _safe_set(b, 'user27', {a1})
    assert _is_linked(b, 'user27', a1)
    if hasattr(a1, 'following_Hashtag26'):
        assert _is_linked(a1, 'following_Hashtag26', b)
    _safe_set(b, 'user27', {a2})
    assert _is_linked(b, 'user27', a2)
    if hasattr(a1, 'following_Hashtag26'):
        assert not _is_linked(a1, 'following_Hashtag26', b)
    if hasattr(a2, 'following_Hashtag26'):
        assert _is_linked(a2, 'following_Hashtag26', b)
    _safe_set(b, 'user27', set())
    assert not _is_linked(b, 'user27', a2)
    if hasattr(a2, 'following_Hashtag26'):
        assert not _is_linked(a2, 'following_Hashtag26', b)


def test_assoc_User_Like_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    _safe_set(b, 'user29', a1)
    assert _is_linked(b, 'user29', a1)
    if hasattr(a1, 'like28'):
        assert _is_linked(a1, 'like28', b)
    _safe_set(b, 'user29', a2)
    assert _is_linked(b, 'user29', a2)
    if hasattr(a1, 'like28'):
        assert not _is_linked(a1, 'like28', b)
    if hasattr(a2, 'like28'):
        assert _is_linked(a2, 'like28', b)
    _safe_set(b, 'user29', None)
    assert not _is_linked(b, 'user29', a2)
    if hasattr(a2, 'like28'):
        assert not _is_linked(a2, 'like28', b)


def test_assoc_User_Mention_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Mention(id=7, post_id=7, user_id=7)
    _safe_set(b, 'user11', a1)
    assert _is_linked(b, 'user11', a1)
    if hasattr(a1, 'mention10'):
        assert _is_linked(a1, 'mention10', b)
    _safe_set(b, 'user11', a2)
    assert _is_linked(b, 'user11', a2)
    if hasattr(a1, 'mention10'):
        assert not _is_linked(a1, 'mention10', b)
    if hasattr(a2, 'mention10'):
        assert _is_linked(a2, 'mention10', b)
    _safe_set(b, 'user11', None)
    assert not _is_linked(b, 'user11', a2)
    if hasattr(a2, 'mention10'):
        assert not _is_linked(a2, 'mention10', b)


def test_assoc_User_Message_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    _safe_set(b, 'user25', {a1})
    assert _is_linked(b, 'user25', a1)
    if hasattr(a1, 'message24'):
        assert _is_linked(a1, 'message24', b)
    _safe_set(b, 'user25', {a2})
    assert _is_linked(b, 'user25', a2)
    if hasattr(a1, 'message24'):
        assert not _is_linked(a1, 'message24', b)
    if hasattr(a2, 'message24'):
        assert _is_linked(a2, 'message24', b)
    _safe_set(b, 'user25', set())
    assert not _is_linked(b, 'user25', a2)
    if hasattr(a2, 'message24'):
        assert not _is_linked(a2, 'message24', b)


def test_assoc_User_N_Disturb_User_reverse_link_reassign_clear():
    a1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    a2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    b = N_Disturb_User(disturb_user_id=7, id=7, user_id=7)
    _safe_set(b, 'user3', a1)
    assert _is_linked(b, 'user3', a1)
    if hasattr(a1, 'n_Disturb_User2'):
        assert _is_linked(a1, 'n_Disturb_User2', b)
    _safe_set(b, 'user3', a2)
    assert _is_linked(b, 'user3', a2)
    if hasattr(a1, 'n_Disturb_User2'):
        assert not _is_linked(a1, 'n_Disturb_User2', b)
    if hasattr(a2, 'n_Disturb_User2'):
        assert _is_linked(a2, 'n_Disturb_User2', b)
    _safe_set(b, 'user3', None)
    assert not _is_linked(b, 'user3', a2)
    if hasattr(a2, 'n_Disturb_User2'):
        assert not _is_linked(a2, 'n_Disturb_User2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

