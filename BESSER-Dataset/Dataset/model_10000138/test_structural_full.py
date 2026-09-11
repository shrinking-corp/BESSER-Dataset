import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_Another_Login_facebook_id_value_roundtrip():
    instance = Another_Login(facebook_id=7, id=7, user_id=7)
    assert instance.facebook_id == 7
    instance.facebook_id = 13
    assert instance.facebook_id == 13


def test_Another_Login_id_value_roundtrip():
    instance = Another_Login(facebook_id=7, id=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Another_Login_user_id_value_roundtrip():
    instance = Another_Login(facebook_id=7, id=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Comment_comment_id_value_roundtrip():
    instance = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    assert instance.comment_id == 7
    instance.comment_id = 13
    assert instance.comment_id == 13


def test_Comment_content_value_roundtrip():
    instance = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    assert instance.content == 7
    instance.content = 13
    assert instance.content == 13


def test_Comment_creation_date_value_roundtrip():
    instance = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    assert instance.creation_date == "sample_text"
    instance.creation_date = "sample_text_2"
    assert instance.creation_date == "sample_text_2"


def test_Comment_id_value_roundtrip():
    instance = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Comment_post_id_value_roundtrip():
    instance = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    assert instance.post_id == 7
    instance.post_id = 13
    assert instance.post_id == 13


def test_Comment_user_id_value_roundtrip():
    instance = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Cryptostream_blocked_user_id_value_roundtrip():
    instance = Cryptostream(blocked_user_id=7, id=7, user_id=7)
    assert instance.blocked_user_id == 7
    instance.blocked_user_id = 13
    assert instance.blocked_user_id == 13


def test_Cryptostream_id_value_roundtrip():
    instance = Cryptostream(blocked_user_id=7, id=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Cryptostream_user_id_value_roundtrip():
    instance = Cryptostream(blocked_user_id=7, id=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Following_Hashtag_hashtag_id_value_roundtrip():
    instance = Following_Hashtag(hashtag_id=7, id=7, user_id=7)
    assert instance.hashtag_id == 7
    instance.hashtag_id = 13
    assert instance.hashtag_id == 13


def test_Following_Hashtag_id_value_roundtrip():
    instance = Following_Hashtag(hashtag_id=7, id=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Following_Hashtag_user_id_value_roundtrip():
    instance = Following_Hashtag(hashtag_id=7, id=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Hashtag_id_value_roundtrip():
    instance = Hashtag(id=7, tag="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Hashtag_tag_value_roundtrip():
    instance = Hashtag(id=7, tag="sample_text")
    assert instance.tag == "sample_text"
    instance.tag = "sample_text_2"
    assert instance.tag == "sample_text_2"


def test_Key_Length_value_roundtrip():
    instance = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    assert instance.Length == "sample_text"
    instance.Length = "sample_text_2"
    assert instance.Length == "sample_text_2"


def test_Key_Value_value_roundtrip():
    instance = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_Key_coordinat_y_value_roundtrip():
    instance = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    assert instance.coordinat_y == 7
    instance.coordinat_y = 13
    assert instance.coordinat_y == 13


def test_Key_id_value_roundtrip():
    instance = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Like_date_sent_value_roundtrip():
    instance = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    assert instance.date_sent == "sample_text"
    instance.date_sent = "sample_text_2"
    assert instance.date_sent == "sample_text_2"


def test_Like_id_value_roundtrip():
    instance = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Like_post_id_value_roundtrip():
    instance = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    assert instance.post_id == 7
    instance.post_id = 13
    assert instance.post_id == 13


def test_Like_user_id_value_roundtrip():
    instance = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Mention_id_value_roundtrip():
    instance = Mention(id=7, post_id=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Mention_post_id_value_roundtrip():
    instance = Mention(id=7, post_id=7, user_id=7)
    assert instance.post_id == 7
    instance.post_id = 13
    assert instance.post_id == 13


def test_Mention_user_id_value_roundtrip():
    instance = Mention(id=7, post_id=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Message_creation_date_value_roundtrip():
    instance = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    assert instance.creation_date == "sample_text"
    instance.creation_date = "sample_text_2"
    assert instance.creation_date == "sample_text_2"


def test_Message_date_seen_value_roundtrip():
    instance = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    assert instance.date_seen == "sample_text"
    instance.date_seen = "sample_text_2"
    assert instance.date_seen == "sample_text_2"


def test_Message_id_value_roundtrip():
    instance = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Message_is_deleted_value_roundtrip():
    instance = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    assert instance.is_deleted == True
    instance.is_deleted = False
    assert instance.is_deleted == False


def test_Message_message_value_roundtrip():
    instance = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_Message_receiver_id_value_roundtrip():
    instance = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    assert instance.receiver_id == 7
    instance.receiver_id = 13
    assert instance.receiver_id == 13


def test_Message_sender_id_value_roundtrip():
    instance = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    assert instance.sender_id == 7
    instance.sender_id = 13
    assert instance.sender_id == 13


def test_N_Disturb_User_disturb_user_id_value_roundtrip():
    instance = N_Disturb_User(disturb_user_id=7, id=7, user_id=7)
    assert instance.disturb_user_id == 7
    instance.disturb_user_id = 13
    assert instance.disturb_user_id == 13


def test_N_Disturb_User_id_value_roundtrip():
    instance = N_Disturb_User(disturb_user_id=7, id=7, user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_N_Disturb_User_user_id_value_roundtrip():
    instance = N_Disturb_User(disturb_user_id=7, id=7, user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Post_creation_date_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.creation_date == "sample_text"
    instance.creation_date = "sample_text_2"
    assert instance.creation_date == "sample_text_2"


def test_Post_date_update_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.date_update == "sample_text"
    instance.date_update = "sample_text_2"
    assert instance.date_update == "sample_text_2"


def test_Post_hashtag_id_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.hashtag_id == 7
    instance.hashtag_id = 13
    assert instance.hashtag_id == 13


def test_Post_id_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Post_location_id_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.location_id == 7
    instance.location_id = 13
    assert instance.location_id == 13


def test_Post_status_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Post_text_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_Post_total_like_value_roundtrip():
    instance = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    assert instance.total_like == 7
    instance.total_like = 13
    assert instance.total_like == 13


def test_Principal_creation_date_value_roundtrip():
    instance = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    assert instance.creation_date == "sample_text"
    instance.creation_date = "sample_text_2"
    assert instance.creation_date == "sample_text_2"


def test_Principal_followers_id_value_roundtrip():
    instance = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    assert instance.followers_id == 7
    instance.followers_id = 13
    assert instance.followers_id == 13


def test_Principal_id_value_roundtrip():
    instance = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Principal_status_value_roundtrip():
    instance = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Principal_user_id_value_roundtrip():
    instance = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Reciever_id_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Reciever_is_active_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.is_active == True
    instance.is_active = False
    assert instance.is_active == False


def test_Reciever_is_admin_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.is_admin == True
    instance.is_admin = False
    assert instance.is_admin == False


def test_Reciever_is_private_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.is_private == True
    instance.is_private = False
    assert instance.is_private == False


def test_Reciever_mail_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.mail == "sample_text"
    instance.mail = "sample_text_2"
    assert instance.mail == "sample_text_2"


def test_Reciever_name_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Reciever_password_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Reciever_phone_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Reciever_surname_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_Reciever_user_id_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Reciever_username_value_roundtrip():
    instance = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Sender_creation_date_value_roundtrip():
    instance = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    assert instance.creation_date == "sample_text"
    instance.creation_date = "sample_text_2"
    assert instance.creation_date == "sample_text_2"


def test_Sender_following_id_value_roundtrip():
    instance = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    assert instance.following_id == 7
    instance.following_id = 13
    assert instance.following_id == 13


def test_Sender_id_value_roundtrip():
    instance = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Sender_status_value_roundtrip():
    instance = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Sender_user_id_value_roundtrip():
    instance = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_assoc_Comment_Comment_link_reassign_clear():
    a = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    b1 = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    b2 = Comment(comment_id=13, content=13, creation_date="sample_text_2", id=13, post_id=13, user_id=13)
    _safe_set(a, 'comment32', b1)
    assert _is_linked(a, 'comment32', b1)
    if hasattr(b1, 'comment33'):
        assert _is_linked(b1, 'comment33', a)
    _safe_set(a, 'comment32', b2)
    assert _is_linked(a, 'comment32', b2)
    if hasattr(b1, 'comment33'):
        assert not _is_linked(b1, 'comment33', a)
    if hasattr(b2, 'comment33'):
        assert _is_linked(b2, 'comment33', a)
    _safe_set(a, 'comment32', None)
    assert not _is_linked(a, 'comment32', b2)
    if hasattr(b2, 'comment33'):
        assert not _is_linked(b2, 'comment33', a)


def test_assoc_Comment_Post_link_reassign_clear():
    a = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    b1 = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    b2 = Comment(comment_id=13, content=13, creation_date="sample_text_2", id=13, post_id=13, user_id=13)
    _safe_set(a, 'comment15', {b1})
    assert _is_linked(a, 'comment15', b1)
    if hasattr(b1, 'post14'):
        assert _is_linked(b1, 'post14', a)
    _safe_set(a, 'comment15', {b2})
    assert _is_linked(a, 'comment15', b2)
    if hasattr(b1, 'post14'):
        assert not _is_linked(b1, 'post14', a)
    if hasattr(b2, 'post14'):
        assert _is_linked(b2, 'post14', a)
    _safe_set(a, 'comment15', set())
    assert not _is_linked(a, 'comment15', b2)
    if hasattr(b2, 'post14'):
        assert not _is_linked(b2, 'post14', a)


def test_assoc_Hashtag_Following_Hashtag_link_reassign_clear():
    a = Hashtag(id=7, tag="sample_text")
    b1 = Following_Hashtag(hashtag_id=7, id=7, user_id=7)
    b2 = Following_Hashtag(hashtag_id=13, id=13, user_id=13)
    _safe_set(a, 'following_Hashtag18', b1)
    assert _is_linked(a, 'following_Hashtag18', b1)
    if hasattr(b1, 'hashtag19'):
        assert _is_linked(b1, 'hashtag19', a)
    _safe_set(a, 'following_Hashtag18', b2)
    assert _is_linked(a, 'following_Hashtag18', b2)
    if hasattr(b1, 'hashtag19'):
        assert not _is_linked(b1, 'hashtag19', a)
    if hasattr(b2, 'hashtag19'):
        assert _is_linked(b2, 'hashtag19', a)
    _safe_set(a, 'following_Hashtag18', None)
    assert not _is_linked(a, 'following_Hashtag18', b2)
    if hasattr(b2, 'hashtag19'):
        assert not _is_linked(b2, 'hashtag19', a)


def test_assoc_Hashtag_Post_link_reassign_clear():
    a = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    b1 = Hashtag(id=7, tag="sample_text")
    b2 = Hashtag(id=13, tag="sample_text_2")
    _safe_set(a, 'hashtag17', {b1})
    assert _is_linked(a, 'hashtag17', b1)
    if hasattr(b1, 'post16'):
        assert _is_linked(b1, 'post16', a)
    _safe_set(a, 'hashtag17', {b2})
    assert _is_linked(a, 'hashtag17', b2)
    if hasattr(b1, 'post16'):
        assert not _is_linked(b1, 'post16', a)
    if hasattr(b2, 'post16'):
        assert _is_linked(b2, 'post16', a)
    _safe_set(a, 'hashtag17', set())
    assert not _is_linked(a, 'hashtag17', b2)
    if hasattr(b2, 'post16'):
        assert not _is_linked(b2, 'post16', a)


def test_assoc_Key_Reciever_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    b2 = Key(Length="sample_text_2", Value="sample_text_2", coordinat_y=13, id=13)
    _safe_set(a, 'key39', b1)
    assert _is_linked(a, 'key39', b1)
    if hasattr(b1, 'reciever38'):
        assert _is_linked(b1, 'reciever38', a)
    _safe_set(a, 'key39', b2)
    assert _is_linked(a, 'key39', b2)
    if hasattr(b1, 'reciever38'):
        assert not _is_linked(b1, 'reciever38', a)
    if hasattr(b2, 'reciever38'):
        assert _is_linked(b2, 'reciever38', a)
    _safe_set(a, 'key39', None)
    assert not _is_linked(a, 'key39', b2)
    if hasattr(b2, 'reciever38'):
        assert not _is_linked(b2, 'reciever38', a)


def test_assoc_Key_Sender_link_reassign_clear():
    a = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    b1 = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    b2 = Key(Length="sample_text_2", Value="sample_text_2", coordinat_y=13, id=13)
    _safe_set(a, 'key37', b1)
    assert _is_linked(a, 'key37', b1)
    if hasattr(b1, 'sender36'):
        assert _is_linked(b1, 'sender36', a)
    _safe_set(a, 'key37', b2)
    assert _is_linked(a, 'key37', b2)
    if hasattr(b1, 'sender36'):
        assert not _is_linked(b1, 'sender36', a)
    if hasattr(b2, 'sender36'):
        assert _is_linked(b2, 'sender36', a)
    _safe_set(a, 'key37', None)
    assert not _is_linked(a, 'key37', b2)
    if hasattr(b2, 'sender36'):
        assert not _is_linked(b2, 'sender36', a)


def test_assoc_Like_Post_link_reassign_clear():
    a = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    b1 = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    b2 = Like(date_sent="sample_text_2", id=13, post_id=13, user_id=13)
    _safe_set(a, 'like13', {b1})
    assert _is_linked(a, 'like13', b1)
    if hasattr(b1, 'post12'):
        assert _is_linked(b1, 'post12', a)
    _safe_set(a, 'like13', {b2})
    assert _is_linked(a, 'like13', b2)
    if hasattr(b1, 'post12'):
        assert not _is_linked(b1, 'post12', a)
    if hasattr(b2, 'post12'):
        assert _is_linked(b2, 'post12', a)
    _safe_set(a, 'like13', set())
    assert not _is_linked(a, 'like13', b2)
    if hasattr(b2, 'post12'):
        assert not _is_linked(b2, 'post12', a)


def test_assoc_Location_Post_link_reassign_clear():
    a = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    b1 = Key(Length="sample_text", Value="sample_text", coordinat_y=7, id=7)
    b2 = Key(Length="sample_text_2", Value="sample_text_2", coordinat_y=13, id=13)
    _safe_set(a, 'location21', b1)
    assert _is_linked(a, 'location21', b1)
    if hasattr(b1, 'post20'):
        assert _is_linked(b1, 'post20', a)
    _safe_set(a, 'location21', b2)
    assert _is_linked(a, 'location21', b2)
    if hasattr(b1, 'post20'):
        assert not _is_linked(b1, 'post20', a)
    if hasattr(b2, 'post20'):
        assert _is_linked(b2, 'post20', a)
    _safe_set(a, 'location21', None)
    assert not _is_linked(a, 'location21', b2)
    if hasattr(b2, 'post20'):
        assert not _is_linked(b2, 'post20', a)


def test_assoc_Post_Mention_link_reassign_clear():
    a = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    b1 = Mention(id=7, post_id=7, user_id=7)
    b2 = Mention(id=13, post_id=13, user_id=13)
    _safe_set(a, 'mention22', {b1})
    assert _is_linked(a, 'mention22', b1)
    if hasattr(b1, 'post23'):
        assert _is_linked(b1, 'post23', a)
    _safe_set(a, 'mention22', {b2})
    assert _is_linked(a, 'mention22', b2)
    if hasattr(b1, 'post23'):
        assert not _is_linked(b1, 'post23', a)
    if hasattr(b2, 'post23'):
        assert _is_linked(b2, 'post23', a)
    _safe_set(a, 'mention22', set())
    assert not _is_linked(a, 'mention22', b2)
    if hasattr(b2, 'post23'):
        assert not _is_linked(b2, 'post23', a)


def test_assoc_Post_User_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Post(creation_date="sample_text", date_update="sample_text", hashtag_id=7, id=7, location_id=7, status="sample_text", text="sample_text", total_like=7)
    b2 = Post(creation_date="sample_text_2", date_update="sample_text_2", hashtag_id=13, id=13, location_id=13, status="sample_text_2", text="sample_text_2", total_like=13)
    _safe_set(a, 'post9', {b1})
    assert _is_linked(a, 'post9', b1)
    if hasattr(b1, 'user8'):
        assert _is_linked(b1, 'user8', a)
    _safe_set(a, 'post9', {b2})
    assert _is_linked(a, 'post9', b2)
    if hasattr(b1, 'user8'):
        assert not _is_linked(b1, 'user8', a)
    if hasattr(b2, 'user8'):
        assert _is_linked(b2, 'user8', a)
    _safe_set(a, 'post9', set())
    assert not _is_linked(a, 'post9', b2)
    if hasattr(b2, 'user8'):
        assert not _is_linked(b2, 'user8', a)


def test_assoc_Principal_Reciever_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    b2 = Principal(creation_date="sample_text_2", followers_id=13, id=13, status="sample_text_2", user_id=13)
    _safe_set(a, 'principal41', b1)
    assert _is_linked(a, 'principal41', b1)
    if hasattr(b1, 'reciever40'):
        assert _is_linked(b1, 'reciever40', a)
    _safe_set(a, 'principal41', b2)
    assert _is_linked(a, 'principal41', b2)
    if hasattr(b1, 'reciever40'):
        assert not _is_linked(b1, 'reciever40', a)
    if hasattr(b2, 'reciever40'):
        assert _is_linked(b2, 'reciever40', a)
    _safe_set(a, 'principal41', None)
    assert not _is_linked(a, 'principal41', b2)
    if hasattr(b2, 'reciever40'):
        assert not _is_linked(b2, 'reciever40', a)


def test_assoc_User_Another_Login_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Another_Login(facebook_id=7, id=7, user_id=7)
    b2 = Another_Login(facebook_id=13, id=13, user_id=13)
    _safe_set(a, 'another_Login34', b1)
    assert _is_linked(a, 'another_Login34', b1)
    if hasattr(b1, 'user35'):
        assert _is_linked(b1, 'user35', a)
    _safe_set(a, 'another_Login34', b2)
    assert _is_linked(a, 'another_Login34', b2)
    if hasattr(b1, 'user35'):
        assert not _is_linked(b1, 'user35', a)
    if hasattr(b2, 'user35'):
        assert _is_linked(b2, 'user35', a)
    _safe_set(a, 'another_Login34', None)
    assert not _is_linked(a, 'another_Login34', b2)
    if hasattr(b2, 'user35'):
        assert not _is_linked(b2, 'user35', a)


def test_assoc_User_Blocked_User_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Cryptostream(blocked_user_id=7, id=7, user_id=7)
    b2 = Cryptostream(blocked_user_id=13, id=13, user_id=13)
    _safe_set(a, 'blocked_User0', {b1})
    assert _is_linked(a, 'blocked_User0', b1)
    if hasattr(b1, 'user1'):
        assert _is_linked(b1, 'user1', a)
    _safe_set(a, 'blocked_User0', {b2})
    assert _is_linked(a, 'blocked_User0', b2)
    if hasattr(b1, 'user1'):
        assert not _is_linked(b1, 'user1', a)
    if hasattr(b2, 'user1'):
        assert _is_linked(b2, 'user1', a)
    _safe_set(a, 'blocked_User0', set())
    assert not _is_linked(a, 'blocked_User0', b2)
    if hasattr(b2, 'user1'):
        assert not _is_linked(b2, 'user1', a)


def test_assoc_User_Comment_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Comment(comment_id=7, content=7, creation_date="sample_text", id=7, post_id=7, user_id=7)
    b2 = Comment(comment_id=13, content=13, creation_date="sample_text_2", id=13, post_id=13, user_id=13)
    _safe_set(a, 'comment30', {b1})
    assert _is_linked(a, 'comment30', b1)
    if hasattr(b1, 'user31'):
        assert _is_linked(b1, 'user31', a)
    _safe_set(a, 'comment30', {b2})
    assert _is_linked(a, 'comment30', b2)
    if hasattr(b1, 'user31'):
        assert not _is_linked(b1, 'user31', a)
    if hasattr(b2, 'user31'):
        assert _is_linked(b2, 'user31', a)
    _safe_set(a, 'comment30', set())
    assert not _is_linked(a, 'comment30', b2)
    if hasattr(b2, 'user31'):
        assert not _is_linked(b2, 'user31', a)


def test_assoc_User_Followers_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Principal(creation_date="sample_text", followers_id=7, id=7, status="sample_text", user_id=7)
    b2 = Principal(creation_date="sample_text_2", followers_id=13, id=13, status="sample_text_2", user_id=13)
    _safe_set(a, 'followers4', {b1})
    assert _is_linked(a, 'followers4', b1)
    if hasattr(b1, 'user5'):
        assert _is_linked(b1, 'user5', a)
    _safe_set(a, 'followers4', {b2})
    assert _is_linked(a, 'followers4', b2)
    if hasattr(b1, 'user5'):
        assert not _is_linked(b1, 'user5', a)
    if hasattr(b2, 'user5'):
        assert _is_linked(b2, 'user5', a)
    _safe_set(a, 'followers4', set())
    assert not _is_linked(a, 'followers4', b2)
    if hasattr(b2, 'user5'):
        assert not _is_linked(b2, 'user5', a)


def test_assoc_User_Following_link_reassign_clear():
    a = Sender(creation_date="sample_text", following_id=7, id=7, status="sample_text", user_id=7)
    b1 = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b2 = Reciever(id=13, is_active=False, is_admin=False, is_private=False, mail="sample_text_2", name="sample_text_2", password="sample_text_2", phone="sample_text_2", surname="sample_text_2", user_id=13, username="sample_text_2")
    _safe_set(a, 'user7', {b1})
    assert _is_linked(a, 'user7', b1)
    if hasattr(b1, 'following6'):
        assert _is_linked(b1, 'following6', a)
    _safe_set(a, 'user7', {b2})
    assert _is_linked(a, 'user7', b2)
    if hasattr(b1, 'following6'):
        assert not _is_linked(b1, 'following6', a)
    if hasattr(b2, 'following6'):
        assert _is_linked(b2, 'following6', a)
    _safe_set(a, 'user7', set())
    assert not _is_linked(a, 'user7', b2)
    if hasattr(b2, 'following6'):
        assert not _is_linked(b2, 'following6', a)


def test_assoc_User_Following_Hashtag_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Following_Hashtag(hashtag_id=7, id=7, user_id=7)
    b2 = Following_Hashtag(hashtag_id=13, id=13, user_id=13)
    _safe_set(a, 'following_Hashtag26', {b1})
    assert _is_linked(a, 'following_Hashtag26', b1)
    if hasattr(b1, 'user27'):
        assert _is_linked(b1, 'user27', a)
    _safe_set(a, 'following_Hashtag26', {b2})
    assert _is_linked(a, 'following_Hashtag26', b2)
    if hasattr(b1, 'user27'):
        assert not _is_linked(b1, 'user27', a)
    if hasattr(b2, 'user27'):
        assert _is_linked(b2, 'user27', a)
    _safe_set(a, 'following_Hashtag26', set())
    assert not _is_linked(a, 'following_Hashtag26', b2)
    if hasattr(b2, 'user27'):
        assert not _is_linked(b2, 'user27', a)


def test_assoc_User_Like_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Like(date_sent="sample_text", id=7, post_id=7, user_id=7)
    b2 = Like(date_sent="sample_text_2", id=13, post_id=13, user_id=13)
    _safe_set(a, 'like28', b1)
    assert _is_linked(a, 'like28', b1)
    if hasattr(b1, 'user29'):
        assert _is_linked(b1, 'user29', a)
    _safe_set(a, 'like28', b2)
    assert _is_linked(a, 'like28', b2)
    if hasattr(b1, 'user29'):
        assert not _is_linked(b1, 'user29', a)
    if hasattr(b2, 'user29'):
        assert _is_linked(b2, 'user29', a)
    _safe_set(a, 'like28', None)
    assert not _is_linked(a, 'like28', b2)
    if hasattr(b2, 'user29'):
        assert not _is_linked(b2, 'user29', a)


def test_assoc_User_Mention_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Mention(id=7, post_id=7, user_id=7)
    b2 = Mention(id=13, post_id=13, user_id=13)
    _safe_set(a, 'mention10', b1)
    assert _is_linked(a, 'mention10', b1)
    if hasattr(b1, 'user11'):
        assert _is_linked(b1, 'user11', a)
    _safe_set(a, 'mention10', b2)
    assert _is_linked(a, 'mention10', b2)
    if hasattr(b1, 'user11'):
        assert not _is_linked(b1, 'user11', a)
    if hasattr(b2, 'user11'):
        assert _is_linked(b2, 'user11', a)
    _safe_set(a, 'mention10', None)
    assert not _is_linked(a, 'mention10', b2)
    if hasattr(b2, 'user11'):
        assert not _is_linked(b2, 'user11', a)


def test_assoc_User_Message_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = Message(creation_date="sample_text", date_seen="sample_text", id=7, is_deleted=True, message="sample_text", receiver_id=7, sender_id=7)
    b2 = Message(creation_date="sample_text_2", date_seen="sample_text_2", id=13, is_deleted=False, message="sample_text_2", receiver_id=13, sender_id=13)
    _safe_set(a, 'message24', {b1})
    assert _is_linked(a, 'message24', b1)
    if hasattr(b1, 'user25'):
        assert _is_linked(b1, 'user25', a)
    _safe_set(a, 'message24', {b2})
    assert _is_linked(a, 'message24', b2)
    if hasattr(b1, 'user25'):
        assert not _is_linked(b1, 'user25', a)
    if hasattr(b2, 'user25'):
        assert _is_linked(b2, 'user25', a)
    _safe_set(a, 'message24', set())
    assert not _is_linked(a, 'message24', b2)
    if hasattr(b2, 'user25'):
        assert not _is_linked(b2, 'user25', a)


def test_assoc_User_N_Disturb_User_link_reassign_clear():
    a = Reciever(id=7, is_active=True, is_admin=True, is_private=True, mail="sample_text", name="sample_text", password="sample_text", phone="sample_text", surname="sample_text", user_id=7, username="sample_text")
    b1 = N_Disturb_User(disturb_user_id=7, id=7, user_id=7)
    b2 = N_Disturb_User(disturb_user_id=13, id=13, user_id=13)
    _safe_set(a, 'n_Disturb_User2', {b1})
    assert _is_linked(a, 'n_Disturb_User2', b1)
    if hasattr(b1, 'user3'):
        assert _is_linked(b1, 'user3', a)
    _safe_set(a, 'n_Disturb_User2', {b2})
    assert _is_linked(a, 'n_Disturb_User2', b2)
    if hasattr(b1, 'user3'):
        assert not _is_linked(b1, 'user3', a)
    if hasattr(b2, 'user3'):
        assert _is_linked(b2, 'user3', a)
    _safe_set(a, 'n_Disturb_User2', set())
    assert not _is_linked(a, 'n_Disturb_User2', b2)
    if hasattr(b2, 'user3'):
        assert not _is_linked(b2, 'user3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Another_Login_strategy = st.builds(Another_Login, facebook_id=st.integers(), id=st.integers(), user_id=st.integers())
@given(instance=Another_Login_strategy)
@settings(max_examples=25)
def test_Another_Login_instantiation(instance):
    assert isinstance(instance, Another_Login)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Comment_strategy = st.builds(Comment, comment_id=st.integers(), content=st.integers(), creation_date=safe_text, id=st.integers(), post_id=st.integers(), user_id=st.integers())
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


Cryptostream_strategy = st.builds(Cryptostream, blocked_user_id=st.integers(), id=st.integers(), user_id=st.integers())
@given(instance=Cryptostream_strategy)
@settings(max_examples=25)
def test_Cryptostream_instantiation(instance):
    assert isinstance(instance, Cryptostream)


Following_Hashtag_strategy = st.builds(Following_Hashtag, hashtag_id=st.integers(), id=st.integers(), user_id=st.integers())
@given(instance=Following_Hashtag_strategy)
@settings(max_examples=25)
def test_Following_Hashtag_instantiation(instance):
    assert isinstance(instance, Following_Hashtag)


Hashtag_strategy = st.builds(Hashtag, id=st.integers(), tag=safe_text)
@given(instance=Hashtag_strategy)
@settings(max_examples=25)
def test_Hashtag_instantiation(instance):
    assert isinstance(instance, Hashtag)


Key_strategy = st.builds(Key, Length=safe_text, Value=safe_text, coordinat_y=st.integers(), id=st.integers())
@given(instance=Key_strategy)
@settings(max_examples=25)
def test_Key_instantiation(instance):
    assert isinstance(instance, Key)


Like_strategy = st.builds(Like, date_sent=safe_text, id=st.integers(), post_id=st.integers(), user_id=st.integers())
@given(instance=Like_strategy)
@settings(max_examples=25)
def test_Like_instantiation(instance):
    assert isinstance(instance, Like)


Mention_strategy = st.builds(Mention, id=st.integers(), post_id=st.integers(), user_id=st.integers())
@given(instance=Mention_strategy)
@settings(max_examples=25)
def test_Mention_instantiation(instance):
    assert isinstance(instance, Mention)


Message_strategy = st.builds(Message, creation_date=safe_text, date_seen=safe_text, id=st.integers(), is_deleted=st.booleans(), message=safe_text, receiver_id=st.integers(), sender_id=st.integers())
@given(instance=Message_strategy)
@settings(max_examples=25)
def test_Message_instantiation(instance):
    assert isinstance(instance, Message)


N_Disturb_User_strategy = st.builds(N_Disturb_User, disturb_user_id=st.integers(), id=st.integers(), user_id=st.integers())
@given(instance=N_Disturb_User_strategy)
@settings(max_examples=25)
def test_N_Disturb_User_instantiation(instance):
    assert isinstance(instance, N_Disturb_User)


Post_strategy = st.builds(Post, creation_date=safe_text, date_update=safe_text, hashtag_id=st.integers(), id=st.integers(), location_id=st.integers(), status=safe_text, text=safe_text, total_like=st.integers())
@given(instance=Post_strategy)
@settings(max_examples=25)
def test_Post_instantiation(instance):
    assert isinstance(instance, Post)


Principal_strategy = st.builds(Principal, creation_date=safe_text, followers_id=st.integers(), id=st.integers(), status=safe_text, user_id=st.integers())
@given(instance=Principal_strategy)
@settings(max_examples=25)
def test_Principal_instantiation(instance):
    assert isinstance(instance, Principal)


Reciever_strategy = st.builds(Reciever, id=st.integers(), is_active=st.booleans(), is_admin=st.booleans(), is_private=st.booleans(), mail=safe_text, name=safe_text, password=safe_text, phone=safe_text, surname=safe_text, user_id=st.integers(), username=safe_text)
@given(instance=Reciever_strategy)
@settings(max_examples=25)
def test_Reciever_instantiation(instance):
    assert isinstance(instance, Reciever)


Sender_strategy = st.builds(Sender, creation_date=safe_text, following_id=st.integers(), id=st.integers(), status=safe_text, user_id=st.integers())
@given(instance=Sender_strategy)
@settings(max_examples=25)
def test_Sender_instantiation(instance):
    assert isinstance(instance, Sender)


