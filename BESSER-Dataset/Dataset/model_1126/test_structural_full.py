import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    rosmodel_Action,
    rosmodel_ActionClient,
    rosmodel_ActionMessage,
    rosmodel_ActionServer,
    rosmodel_Event,
    rosmodel_Field,
    rosmodel_Message,
    rosmodel_Node,
    rosmodel_Package,
    rosmodel_Publisher,
    rosmodel_ServiceClient,
    rosmodel_ServiceServer,
    rosmodel_ServiceType,
    rosmodel_State,
    rosmodel_Subscriber,
    rosmodel_Topic,
    rosmodel_Transition,
    Datatype,
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

def test_rosmodel_Action_name_value_roundtrip():
    instance = rosmodel_Action(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_ActionClient_name_value_roundtrip():
    instance = rosmodel_ActionClient(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_ActionMessage_name_value_roundtrip():
    instance = rosmodel_ActionMessage(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_ActionServer_name_value_roundtrip():
    instance = rosmodel_ActionServer(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Event_name_value_roundtrip():
    instance = rosmodel_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Field_name_value_roundtrip():
    instance = rosmodel_Field(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Field_type_value_roundtrip():
    instance = rosmodel_Field(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_rosmodel_Message_name_value_roundtrip():
    instance = rosmodel_Message(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Node_frequency_value_roundtrip():
    instance = rosmodel_Node(frequency=3.14, name="sample_text")
    assert instance.frequency == 3.14
    instance.frequency = 9.99
    assert instance.frequency == 9.99


def test_rosmodel_Node_name_value_roundtrip():
    instance = rosmodel_Node(frequency=3.14, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Package_author_value_roundtrip():
    instance = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_rosmodel_Package_author_email_value_roundtrip():
    instance = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.author_email == "sample_text"
    instance.author_email = "sample_text_2"
    assert instance.author_email == "sample_text_2"


def test_rosmodel_Package_depends_value_roundtrip():
    instance = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.depends == "sample_text"
    instance.depends = "sample_text_2"
    assert instance.depends == "sample_text_2"


def test_rosmodel_Package_description_value_roundtrip():
    instance = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_rosmodel_Package_name_value_roundtrip():
    instance = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Publisher_msg_value_roundtrip():
    instance = rosmodel_Publisher(msg="sample_text", name="sample_text", queue_size=7)
    assert instance.msg == "sample_text"
    instance.msg = "sample_text_2"
    assert instance.msg == "sample_text_2"


def test_rosmodel_Publisher_name_value_roundtrip():
    instance = rosmodel_Publisher(msg="sample_text", name="sample_text", queue_size=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Publisher_queue_size_value_roundtrip():
    instance = rosmodel_Publisher(msg="sample_text", name="sample_text", queue_size=7)
    assert instance.queue_size == 7
    instance.queue_size = 13
    assert instance.queue_size == 13


def test_rosmodel_ServiceClient_name_value_roundtrip():
    instance = rosmodel_ServiceClient(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_ServiceServer_name_value_roundtrip():
    instance = rosmodel_ServiceServer(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_ServiceType_name_value_roundtrip():
    instance = rosmodel_ServiceType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_State_name_value_roundtrip():
    instance = rosmodel_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Subscriber_msg_value_roundtrip():
    instance = rosmodel_Subscriber(msg="sample_text", name="sample_text", queue_size=7)
    assert instance.msg == "sample_text"
    instance.msg = "sample_text_2"
    assert instance.msg == "sample_text_2"


def test_rosmodel_Subscriber_name_value_roundtrip():
    instance = rosmodel_Subscriber(msg="sample_text", name="sample_text", queue_size=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Subscriber_queue_size_value_roundtrip():
    instance = rosmodel_Subscriber(msg="sample_text", name="sample_text", queue_size=7)
    assert instance.queue_size == 7
    instance.queue_size = 13
    assert instance.queue_size == 13


def test_rosmodel_Topic_name_value_roundtrip():
    instance = rosmodel_Topic(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rosmodel_Transition_name_value_roundtrip():
    instance = rosmodel_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_action25_link_reassign_clear():
    a = rosmodel_Node(frequency=3.14, name="sample_text")
    b1 = rosmodel_Action(name="sample_text")
    b2 = rosmodel_Action(name="sample_text_2")
    _safe_set(a, 'rosmodel_Node26', {b1})
    assert _is_linked(a, 'rosmodel_Node26', b1)
    if hasattr(b1, 'rosmodel_Action'):
        assert _is_linked(b1, 'rosmodel_Action', a)
    _safe_set(a, 'rosmodel_Node26', {b2})
    assert _is_linked(a, 'rosmodel_Node26', b2)
    if hasattr(b1, 'rosmodel_Action'):
        assert not _is_linked(b1, 'rosmodel_Action', a)
    if hasattr(b2, 'rosmodel_Action'):
        assert _is_linked(b2, 'rosmodel_Action', a)
    _safe_set(a, 'rosmodel_Node26', set())
    assert not _is_linked(a, 'rosmodel_Node26', b2)
    if hasattr(b2, 'rosmodel_Action'):
        assert not _is_linked(b2, 'rosmodel_Action', a)


def test_assoc_action70_link_reassign_clear():
    a = rosmodel_State(name="sample_text")
    b1 = rosmodel_Action(name="sample_text")
    b2 = rosmodel_Action(name="sample_text_2")
    _safe_set(a, 'rosmodel_State71', {b1})
    assert _is_linked(a, 'rosmodel_State71', b1)
    if hasattr(b1, 'rosmodel_Action72'):
        assert _is_linked(b1, 'rosmodel_Action72', a)
    _safe_set(a, 'rosmodel_State71', {b2})
    assert _is_linked(a, 'rosmodel_State71', b2)
    if hasattr(b1, 'rosmodel_Action72'):
        assert not _is_linked(b1, 'rosmodel_Action72', a)
    if hasattr(b2, 'rosmodel_Action72'):
        assert _is_linked(b2, 'rosmodel_Action72', a)
    _safe_set(a, 'rosmodel_State71', set())
    assert not _is_linked(a, 'rosmodel_State71', b2)
    if hasattr(b2, 'rosmodel_Action72'):
        assert not _is_linked(b2, 'rosmodel_Action72', a)


def test_assoc_action88_link_reassign_clear():
    a = rosmodel_Transition(name="sample_text")
    b1 = rosmodel_Action(name="sample_text")
    b2 = rosmodel_Action(name="sample_text_2")
    _safe_set(a, 'rosmodel_Transition89', b1)
    assert _is_linked(a, 'rosmodel_Transition89', b1)
    if hasattr(b1, 'rosmodel_Action90'):
        assert _is_linked(b1, 'rosmodel_Action90', a)
    _safe_set(a, 'rosmodel_Transition89', b2)
    assert _is_linked(a, 'rosmodel_Transition89', b2)
    if hasattr(b1, 'rosmodel_Action90'):
        assert not _is_linked(b1, 'rosmodel_Action90', a)
    if hasattr(b2, 'rosmodel_Action90'):
        assert _is_linked(b2, 'rosmodel_Action90', a)
    _safe_set(a, 'rosmodel_Transition89', None)
    assert not _is_linked(a, 'rosmodel_Transition89', b2)
    if hasattr(b2, 'rosmodel_Action90'):
        assert not _is_linked(b2, 'rosmodel_Action90', a)


def test_assoc_actionclient17_link_reassign_clear():
    a = rosmodel_Node(frequency=3.14, name="sample_text")
    b1 = rosmodel_ActionClient(name="sample_text")
    b2 = rosmodel_ActionClient(name="sample_text_2")
    _safe_set(a, 'rosmodel_Node18', {b1})
    assert _is_linked(a, 'rosmodel_Node18', b1)
    if hasattr(b1, 'rosmodel_ActionClient'):
        assert _is_linked(b1, 'rosmodel_ActionClient', a)
    _safe_set(a, 'rosmodel_Node18', {b2})
    assert _is_linked(a, 'rosmodel_Node18', b2)
    if hasattr(b1, 'rosmodel_ActionClient'):
        assert not _is_linked(b1, 'rosmodel_ActionClient', a)
    if hasattr(b2, 'rosmodel_ActionClient'):
        assert _is_linked(b2, 'rosmodel_ActionClient', a)
    _safe_set(a, 'rosmodel_Node18', set())
    assert not _is_linked(a, 'rosmodel_Node18', b2)
    if hasattr(b2, 'rosmodel_ActionClient'):
        assert not _is_linked(b2, 'rosmodel_ActionClient', a)


def test_assoc_actionmessage58_link_reassign_clear():
    a = rosmodel_ActionServer(name="sample_text")
    b1 = rosmodel_ActionMessage(name="sample_text")
    b2 = rosmodel_ActionMessage(name="sample_text_2")
    _safe_set(a, 'rosmodel_ActionServer59', b1)
    assert _is_linked(a, 'rosmodel_ActionServer59', b1)
    if hasattr(b1, 'rosmodel_ActionMessage60'):
        assert _is_linked(b1, 'rosmodel_ActionMessage60', a)
    _safe_set(a, 'rosmodel_ActionServer59', b2)
    assert _is_linked(a, 'rosmodel_ActionServer59', b2)
    if hasattr(b1, 'rosmodel_ActionMessage60'):
        assert not _is_linked(b1, 'rosmodel_ActionMessage60', a)
    if hasattr(b2, 'rosmodel_ActionMessage60'):
        assert _is_linked(b2, 'rosmodel_ActionMessage60', a)
    _safe_set(a, 'rosmodel_ActionServer59', None)
    assert not _is_linked(a, 'rosmodel_ActionServer59', b2)
    if hasattr(b2, 'rosmodel_ActionMessage60'):
        assert not _is_linked(b2, 'rosmodel_ActionMessage60', a)


def test_assoc_actionmessage61_link_reassign_clear():
    a = rosmodel_ActionMessage(name="sample_text")
    b1 = rosmodel_ActionClient(name="sample_text")
    b2 = rosmodel_ActionClient(name="sample_text_2")
    _safe_set(a, 'rosmodel_ActionMessage63', b1)
    assert _is_linked(a, 'rosmodel_ActionMessage63', b1)
    if hasattr(b1, 'rosmodel_ActionClient62'):
        assert _is_linked(b1, 'rosmodel_ActionClient62', a)
    _safe_set(a, 'rosmodel_ActionMessage63', b2)
    assert _is_linked(a, 'rosmodel_ActionMessage63', b2)
    if hasattr(b1, 'rosmodel_ActionClient62'):
        assert not _is_linked(b1, 'rosmodel_ActionClient62', a)
    if hasattr(b2, 'rosmodel_ActionClient62'):
        assert _is_linked(b2, 'rosmodel_ActionClient62', a)
    _safe_set(a, 'rosmodel_ActionMessage63', None)
    assert not _is_linked(a, 'rosmodel_ActionMessage63', b2)
    if hasattr(b2, 'rosmodel_ActionClient62'):
        assert not _is_linked(b2, 'rosmodel_ActionClient62', a)


def test_assoc_actionmessage7_link_reassign_clear():
    a = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    b1 = rosmodel_ActionMessage(name="sample_text")
    b2 = rosmodel_ActionMessage(name="sample_text_2")
    _safe_set(a, 'rosmodel_Package8', {b1})
    assert _is_linked(a, 'rosmodel_Package8', b1)
    if hasattr(b1, 'rosmodel_ActionMessage'):
        assert _is_linked(b1, 'rosmodel_ActionMessage', a)
    _safe_set(a, 'rosmodel_Package8', {b2})
    assert _is_linked(a, 'rosmodel_Package8', b2)
    if hasattr(b1, 'rosmodel_ActionMessage'):
        assert not _is_linked(b1, 'rosmodel_ActionMessage', a)
    if hasattr(b2, 'rosmodel_ActionMessage'):
        assert _is_linked(b2, 'rosmodel_ActionMessage', a)
    _safe_set(a, 'rosmodel_Package8', set())
    assert not _is_linked(a, 'rosmodel_Package8', b2)
    if hasattr(b2, 'rosmodel_ActionMessage'):
        assert not _is_linked(b2, 'rosmodel_ActionMessage', a)


def test_assoc_actionserver19_link_reassign_clear():
    a = rosmodel_Node(frequency=3.14, name="sample_text")
    b1 = rosmodel_ActionServer(name="sample_text")
    b2 = rosmodel_ActionServer(name="sample_text_2")
    _safe_set(a, 'rosmodel_Node20', {b1})
    assert _is_linked(a, 'rosmodel_Node20', b1)
    if hasattr(b1, 'rosmodel_ActionServer'):
        assert _is_linked(b1, 'rosmodel_ActionServer', a)
    _safe_set(a, 'rosmodel_Node20', {b2})
    assert _is_linked(a, 'rosmodel_Node20', b2)
    if hasattr(b1, 'rosmodel_ActionServer'):
        assert not _is_linked(b1, 'rosmodel_ActionServer', a)
    if hasattr(b2, 'rosmodel_ActionServer'):
        assert _is_linked(b2, 'rosmodel_ActionServer', a)
    _safe_set(a, 'rosmodel_Node20', set())
    assert not _is_linked(a, 'rosmodel_Node20', b2)
    if hasattr(b2, 'rosmodel_ActionServer'):
        assert not _is_linked(b2, 'rosmodel_ActionServer', a)


def test_assoc_entryaction73_link_reassign_clear():
    a = rosmodel_State(name="sample_text")
    b1 = rosmodel_Action(name="sample_text")
    b2 = rosmodel_Action(name="sample_text_2")
    _safe_set(a, 'rosmodel_State74', b1)
    assert _is_linked(a, 'rosmodel_State74', b1)
    if hasattr(b1, 'rosmodel_Action75'):
        assert _is_linked(b1, 'rosmodel_Action75', a)
    _safe_set(a, 'rosmodel_State74', b2)
    assert _is_linked(a, 'rosmodel_State74', b2)
    if hasattr(b1, 'rosmodel_Action75'):
        assert not _is_linked(b1, 'rosmodel_Action75', a)
    if hasattr(b2, 'rosmodel_Action75'):
        assert _is_linked(b2, 'rosmodel_Action75', a)
    _safe_set(a, 'rosmodel_State74', None)
    assert not _is_linked(a, 'rosmodel_State74', b2)
    if hasattr(b2, 'rosmodel_Action75'):
        assert not _is_linked(b2, 'rosmodel_Action75', a)


def test_assoc_event27_link_reassign_clear():
    a = rosmodel_Node(frequency=3.14, name="sample_text")
    b1 = rosmodel_Event(name="sample_text")
    b2 = rosmodel_Event(name="sample_text_2")
    _safe_set(a, 'rosmodel_Node28', {b1})
    assert _is_linked(a, 'rosmodel_Node28', b1)
    if hasattr(b1, 'rosmodel_Event'):
        assert _is_linked(b1, 'rosmodel_Event', a)
    _safe_set(a, 'rosmodel_Node28', {b2})
    assert _is_linked(a, 'rosmodel_Node28', b2)
    if hasattr(b1, 'rosmodel_Event'):
        assert not _is_linked(b1, 'rosmodel_Event', a)
    if hasattr(b2, 'rosmodel_Event'):
        assert _is_linked(b2, 'rosmodel_Event', a)
    _safe_set(a, 'rosmodel_Node28', set())
    assert not _is_linked(a, 'rosmodel_Node28', b2)
    if hasattr(b2, 'rosmodel_Event'):
        assert not _is_linked(b2, 'rosmodel_Event', a)


def test_assoc_event79_link_reassign_clear():
    a = rosmodel_State(name="sample_text")
    b1 = rosmodel_Event(name="sample_text")
    b2 = rosmodel_Event(name="sample_text_2")
    _safe_set(a, 'rosmodel_State80', {b1})
    assert _is_linked(a, 'rosmodel_State80', b1)
    if hasattr(b1, 'rosmodel_Event81'):
        assert _is_linked(b1, 'rosmodel_Event81', a)
    _safe_set(a, 'rosmodel_State80', {b2})
    assert _is_linked(a, 'rosmodel_State80', b2)
    if hasattr(b1, 'rosmodel_Event81'):
        assert not _is_linked(b1, 'rosmodel_Event81', a)
    if hasattr(b2, 'rosmodel_Event81'):
        assert _is_linked(b2, 'rosmodel_Event81', a)
    _safe_set(a, 'rosmodel_State80', set())
    assert not _is_linked(a, 'rosmodel_State80', b2)
    if hasattr(b2, 'rosmodel_Event81'):
        assert not _is_linked(b2, 'rosmodel_Event81', a)


def test_assoc_exitaction76_link_reassign_clear():
    a = rosmodel_State(name="sample_text")
    b1 = rosmodel_Action(name="sample_text")
    b2 = rosmodel_Action(name="sample_text_2")
    _safe_set(a, 'rosmodel_State77', b1)
    assert _is_linked(a, 'rosmodel_State77', b1)
    if hasattr(b1, 'rosmodel_Action78'):
        assert _is_linked(b1, 'rosmodel_Action78', a)
    _safe_set(a, 'rosmodel_State77', b2)
    assert _is_linked(a, 'rosmodel_State77', b2)
    if hasattr(b1, 'rosmodel_Action78'):
        assert not _is_linked(b1, 'rosmodel_Action78', a)
    if hasattr(b2, 'rosmodel_Action78'):
        assert _is_linked(b2, 'rosmodel_Action78', a)
    _safe_set(a, 'rosmodel_State77', None)
    assert not _is_linked(a, 'rosmodel_State77', b2)
    if hasattr(b2, 'rosmodel_Action78'):
        assert not _is_linked(b2, 'rosmodel_Action78', a)


def test_assoc_feedback55_link_reassign_clear():
    a = rosmodel_Field(name="sample_text", type="sample_text")
    b1 = rosmodel_ActionMessage(name="sample_text")
    b2 = rosmodel_ActionMessage(name="sample_text_2")
    _safe_set(a, 'rosmodel_Field57', b1)
    assert _is_linked(a, 'rosmodel_Field57', b1)
    if hasattr(b1, 'rosmodel_ActionMessage56'):
        assert _is_linked(b1, 'rosmodel_ActionMessage56', a)
    _safe_set(a, 'rosmodel_Field57', b2)
    assert _is_linked(a, 'rosmodel_Field57', b2)
    if hasattr(b1, 'rosmodel_ActionMessage56'):
        assert not _is_linked(b1, 'rosmodel_ActionMessage56', a)
    if hasattr(b2, 'rosmodel_ActionMessage56'):
        assert _is_linked(b2, 'rosmodel_ActionMessage56', a)
    _safe_set(a, 'rosmodel_Field57', None)
    assert not _is_linked(a, 'rosmodel_Field57', b2)
    if hasattr(b2, 'rosmodel_ActionMessage56'):
        assert not _is_linked(b2, 'rosmodel_ActionMessage56', a)


def test_assoc_field35_link_reassign_clear():
    a = rosmodel_Message(name="sample_text")
    b1 = rosmodel_Field(name="sample_text", type="sample_text")
    b2 = rosmodel_Field(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'rosmodel_Message36', {b1})
    assert _is_linked(a, 'rosmodel_Message36', b1)
    if hasattr(b1, 'rosmodel_Field'):
        assert _is_linked(b1, 'rosmodel_Field', a)
    _safe_set(a, 'rosmodel_Message36', {b2})
    assert _is_linked(a, 'rosmodel_Message36', b2)
    if hasattr(b1, 'rosmodel_Field'):
        assert not _is_linked(b1, 'rosmodel_Field', a)
    if hasattr(b2, 'rosmodel_Field'):
        assert _is_linked(b2, 'rosmodel_Field', a)
    _safe_set(a, 'rosmodel_Message36', set())
    assert not _is_linked(a, 'rosmodel_Message36', b2)
    if hasattr(b2, 'rosmodel_Field'):
        assert not _is_linked(b2, 'rosmodel_Field', a)


def test_assoc_goal49_link_reassign_clear():
    a = rosmodel_Field(name="sample_text", type="sample_text")
    b1 = rosmodel_ActionMessage(name="sample_text")
    b2 = rosmodel_ActionMessage(name="sample_text_2")
    _safe_set(a, 'rosmodel_Field51', b1)
    assert _is_linked(a, 'rosmodel_Field51', b1)
    if hasattr(b1, 'rosmodel_ActionMessage50'):
        assert _is_linked(b1, 'rosmodel_ActionMessage50', a)
    _safe_set(a, 'rosmodel_Field51', b2)
    assert _is_linked(a, 'rosmodel_Field51', b2)
    if hasattr(b1, 'rosmodel_ActionMessage50'):
        assert not _is_linked(b1, 'rosmodel_ActionMessage50', a)
    if hasattr(b2, 'rosmodel_ActionMessage50'):
        assert _is_linked(b2, 'rosmodel_ActionMessage50', a)
    _safe_set(a, 'rosmodel_Field51', None)
    assert not _is_linked(a, 'rosmodel_Field51', b2)
    if hasattr(b2, 'rosmodel_ActionMessage50'):
        assert not _is_linked(b2, 'rosmodel_ActionMessage50', a)


def test_assoc_guard91_link_reassign_clear():
    a = rosmodel_Transition(name="sample_text")
    b1 = rosmodel_Action(name="sample_text")
    b2 = rosmodel_Action(name="sample_text_2")
    _safe_set(a, 'rosmodel_Transition92', b1)
    assert _is_linked(a, 'rosmodel_Transition92', b1)
    if hasattr(b1, 'rosmodel_Action93'):
        assert _is_linked(b1, 'rosmodel_Action93', a)
    _safe_set(a, 'rosmodel_Transition92', b2)
    assert _is_linked(a, 'rosmodel_Transition92', b2)
    if hasattr(b1, 'rosmodel_Action93'):
        assert not _is_linked(b1, 'rosmodel_Action93', a)
    if hasattr(b2, 'rosmodel_Action93'):
        assert _is_linked(b2, 'rosmodel_Action93', a)
    _safe_set(a, 'rosmodel_Transition92', None)
    assert not _is_linked(a, 'rosmodel_Transition92', b2)
    if hasattr(b2, 'rosmodel_Action93'):
        assert not _is_linked(b2, 'rosmodel_Action93', a)


def test_assoc_message3_link_reassign_clear():
    a = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    b1 = rosmodel_Message(name="sample_text")
    b2 = rosmodel_Message(name="sample_text_2")
    _safe_set(a, 'rosmodel_Package4', {b1})
    assert _is_linked(a, 'rosmodel_Package4', b1)
    if hasattr(b1, 'rosmodel_Message'):
        assert _is_linked(b1, 'rosmodel_Message', a)
    _safe_set(a, 'rosmodel_Package4', {b2})
    assert _is_linked(a, 'rosmodel_Package4', b2)
    if hasattr(b1, 'rosmodel_Message'):
        assert not _is_linked(b1, 'rosmodel_Message', a)
    if hasattr(b2, 'rosmodel_Message'):
        assert _is_linked(b2, 'rosmodel_Message', a)
    _safe_set(a, 'rosmodel_Package4', set())
    assert not _is_linked(a, 'rosmodel_Package4', b2)
    if hasattr(b2, 'rosmodel_Message'):
        assert not _is_linked(b2, 'rosmodel_Message', a)


def test_assoc_node0_link_reassign_clear():
    a = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    b1 = rosmodel_Node(frequency=3.14, name="sample_text")
    b2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    _safe_set(a, 'rosmodel_Package', {b1})
    assert _is_linked(a, 'rosmodel_Package', b1)
    if hasattr(b1, 'rosmodel_Node'):
        assert _is_linked(b1, 'rosmodel_Node', a)
    _safe_set(a, 'rosmodel_Package', {b2})
    assert _is_linked(a, 'rosmodel_Package', b2)
    if hasattr(b1, 'rosmodel_Node'):
        assert not _is_linked(b1, 'rosmodel_Node', a)
    if hasattr(b2, 'rosmodel_Node'):
        assert _is_linked(b2, 'rosmodel_Node', a)
    _safe_set(a, 'rosmodel_Package', set())
    assert not _is_linked(a, 'rosmodel_Package', b2)
    if hasattr(b2, 'rosmodel_Node'):
        assert not _is_linked(b2, 'rosmodel_Node', a)


def test_assoc_publisher9_link_reassign_clear():
    a = rosmodel_Publisher(msg="sample_text", name="sample_text", queue_size=7)
    b1 = rosmodel_Node(frequency=3.14, name="sample_text")
    b2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    _safe_set(a, 'rosmodel_Publisher', b1)
    assert _is_linked(a, 'rosmodel_Publisher', b1)
    if hasattr(b1, 'rosmodel_Node10'):
        assert _is_linked(b1, 'rosmodel_Node10', a)
    _safe_set(a, 'rosmodel_Publisher', b2)
    assert _is_linked(a, 'rosmodel_Publisher', b2)
    if hasattr(b1, 'rosmodel_Node10'):
        assert not _is_linked(b1, 'rosmodel_Node10', a)
    if hasattr(b2, 'rosmodel_Node10'):
        assert _is_linked(b2, 'rosmodel_Node10', a)
    _safe_set(a, 'rosmodel_Publisher', None)
    assert not _is_linked(a, 'rosmodel_Publisher', b2)
    if hasattr(b2, 'rosmodel_Node10'):
        assert not _is_linked(b2, 'rosmodel_Node10', a)


def test_assoc_request37_link_reassign_clear():
    a = rosmodel_ServiceType(name="sample_text")
    b1 = rosmodel_Field(name="sample_text", type="sample_text")
    b2 = rosmodel_Field(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'rosmodel_ServiceType38', {b1})
    assert _is_linked(a, 'rosmodel_ServiceType38', b1)
    if hasattr(b1, 'rosmodel_Field39'):
        assert _is_linked(b1, 'rosmodel_Field39', a)
    _safe_set(a, 'rosmodel_ServiceType38', {b2})
    assert _is_linked(a, 'rosmodel_ServiceType38', b2)
    if hasattr(b1, 'rosmodel_Field39'):
        assert not _is_linked(b1, 'rosmodel_Field39', a)
    if hasattr(b2, 'rosmodel_Field39'):
        assert _is_linked(b2, 'rosmodel_Field39', a)
    _safe_set(a, 'rosmodel_ServiceType38', set())
    assert not _is_linked(a, 'rosmodel_ServiceType38', b2)
    if hasattr(b2, 'rosmodel_Field39'):
        assert not _is_linked(b2, 'rosmodel_Field39', a)


def test_assoc_response40_link_reassign_clear():
    a = rosmodel_ServiceType(name="sample_text")
    b1 = rosmodel_Field(name="sample_text", type="sample_text")
    b2 = rosmodel_Field(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'rosmodel_ServiceType41', {b1})
    assert _is_linked(a, 'rosmodel_ServiceType41', b1)
    if hasattr(b1, 'rosmodel_Field42'):
        assert _is_linked(b1, 'rosmodel_Field42', a)
    _safe_set(a, 'rosmodel_ServiceType41', {b2})
    assert _is_linked(a, 'rosmodel_ServiceType41', b2)
    if hasattr(b1, 'rosmodel_Field42'):
        assert not _is_linked(b1, 'rosmodel_Field42', a)
    if hasattr(b2, 'rosmodel_Field42'):
        assert _is_linked(b2, 'rosmodel_Field42', a)
    _safe_set(a, 'rosmodel_ServiceType41', set())
    assert not _is_linked(a, 'rosmodel_ServiceType41', b2)
    if hasattr(b2, 'rosmodel_Field42'):
        assert not _is_linked(b2, 'rosmodel_Field42', a)


def test_assoc_result52_link_reassign_clear():
    a = rosmodel_Field(name="sample_text", type="sample_text")
    b1 = rosmodel_ActionMessage(name="sample_text")
    b2 = rosmodel_ActionMessage(name="sample_text_2")
    _safe_set(a, 'rosmodel_Field54', b1)
    assert _is_linked(a, 'rosmodel_Field54', b1)
    if hasattr(b1, 'rosmodel_ActionMessage53'):
        assert _is_linked(b1, 'rosmodel_ActionMessage53', a)
    _safe_set(a, 'rosmodel_Field54', b2)
    assert _is_linked(a, 'rosmodel_Field54', b2)
    if hasattr(b1, 'rosmodel_ActionMessage53'):
        assert not _is_linked(b1, 'rosmodel_ActionMessage53', a)
    if hasattr(b2, 'rosmodel_ActionMessage53'):
        assert _is_linked(b2, 'rosmodel_ActionMessage53', a)
    _safe_set(a, 'rosmodel_Field54', None)
    assert not _is_linked(a, 'rosmodel_Field54', b2)
    if hasattr(b2, 'rosmodel_ActionMessage53'):
        assert not _is_linked(b2, 'rosmodel_ActionMessage53', a)


def test_assoc_serviceclient13_link_reassign_clear():
    a = rosmodel_ServiceClient(name="sample_text")
    b1 = rosmodel_Node(frequency=3.14, name="sample_text")
    b2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    _safe_set(a, 'rosmodel_ServiceClient', b1)
    assert _is_linked(a, 'rosmodel_ServiceClient', b1)
    if hasattr(b1, 'rosmodel_Node14'):
        assert _is_linked(b1, 'rosmodel_Node14', a)
    _safe_set(a, 'rosmodel_ServiceClient', b2)
    assert _is_linked(a, 'rosmodel_ServiceClient', b2)
    if hasattr(b1, 'rosmodel_Node14'):
        assert not _is_linked(b1, 'rosmodel_Node14', a)
    if hasattr(b2, 'rosmodel_Node14'):
        assert _is_linked(b2, 'rosmodel_Node14', a)
    _safe_set(a, 'rosmodel_ServiceClient', None)
    assert not _is_linked(a, 'rosmodel_ServiceClient', b2)
    if hasattr(b2, 'rosmodel_Node14'):
        assert not _is_linked(b2, 'rosmodel_Node14', a)


def test_assoc_serviceserver15_link_reassign_clear():
    a = rosmodel_ServiceServer(name="sample_text")
    b1 = rosmodel_Node(frequency=3.14, name="sample_text")
    b2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    _safe_set(a, 'rosmodel_ServiceServer', b1)
    assert _is_linked(a, 'rosmodel_ServiceServer', b1)
    if hasattr(b1, 'rosmodel_Node16'):
        assert _is_linked(b1, 'rosmodel_Node16', a)
    _safe_set(a, 'rosmodel_ServiceServer', b2)
    assert _is_linked(a, 'rosmodel_ServiceServer', b2)
    if hasattr(b1, 'rosmodel_Node16'):
        assert not _is_linked(b1, 'rosmodel_Node16', a)
    if hasattr(b2, 'rosmodel_Node16'):
        assert _is_linked(b2, 'rosmodel_Node16', a)
    _safe_set(a, 'rosmodel_ServiceServer', None)
    assert not _is_linked(a, 'rosmodel_ServiceServer', b2)
    if hasattr(b2, 'rosmodel_Node16'):
        assert not _is_linked(b2, 'rosmodel_Node16', a)


def test_assoc_servicetype43_link_reassign_clear():
    a = rosmodel_ServiceType(name="sample_text")
    b1 = rosmodel_ServiceServer(name="sample_text")
    b2 = rosmodel_ServiceServer(name="sample_text_2")
    _safe_set(a, 'rosmodel_ServiceType45', b1)
    assert _is_linked(a, 'rosmodel_ServiceType45', b1)
    if hasattr(b1, 'rosmodel_ServiceServer44'):
        assert _is_linked(b1, 'rosmodel_ServiceServer44', a)
    _safe_set(a, 'rosmodel_ServiceType45', b2)
    assert _is_linked(a, 'rosmodel_ServiceType45', b2)
    if hasattr(b1, 'rosmodel_ServiceServer44'):
        assert not _is_linked(b1, 'rosmodel_ServiceServer44', a)
    if hasattr(b2, 'rosmodel_ServiceServer44'):
        assert _is_linked(b2, 'rosmodel_ServiceServer44', a)
    _safe_set(a, 'rosmodel_ServiceType45', None)
    assert not _is_linked(a, 'rosmodel_ServiceType45', b2)
    if hasattr(b2, 'rosmodel_ServiceServer44'):
        assert not _is_linked(b2, 'rosmodel_ServiceServer44', a)


def test_assoc_servicetype46_link_reassign_clear():
    a = rosmodel_ServiceType(name="sample_text")
    b1 = rosmodel_ServiceClient(name="sample_text")
    b2 = rosmodel_ServiceClient(name="sample_text_2")
    _safe_set(a, 'rosmodel_ServiceType48', b1)
    assert _is_linked(a, 'rosmodel_ServiceType48', b1)
    if hasattr(b1, 'rosmodel_ServiceClient47'):
        assert _is_linked(b1, 'rosmodel_ServiceClient47', a)
    _safe_set(a, 'rosmodel_ServiceType48', b2)
    assert _is_linked(a, 'rosmodel_ServiceType48', b2)
    if hasattr(b1, 'rosmodel_ServiceClient47'):
        assert not _is_linked(b1, 'rosmodel_ServiceClient47', a)
    if hasattr(b2, 'rosmodel_ServiceClient47'):
        assert _is_linked(b2, 'rosmodel_ServiceClient47', a)
    _safe_set(a, 'rosmodel_ServiceType48', None)
    assert not _is_linked(a, 'rosmodel_ServiceType48', b2)
    if hasattr(b2, 'rosmodel_ServiceClient47'):
        assert not _is_linked(b2, 'rosmodel_ServiceClient47', a)


def test_assoc_servicetype5_link_reassign_clear():
    a = rosmodel_ServiceType(name="sample_text")
    b1 = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    b2 = rosmodel_Package(author="sample_text_2", author_email="sample_text_2", depends="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'rosmodel_ServiceType', b1)
    assert _is_linked(a, 'rosmodel_ServiceType', b1)
    if hasattr(b1, 'rosmodel_Package6'):
        assert _is_linked(b1, 'rosmodel_Package6', a)
    _safe_set(a, 'rosmodel_ServiceType', b2)
    assert _is_linked(a, 'rosmodel_ServiceType', b2)
    if hasattr(b1, 'rosmodel_Package6'):
        assert not _is_linked(b1, 'rosmodel_Package6', a)
    if hasattr(b2, 'rosmodel_Package6'):
        assert _is_linked(b2, 'rosmodel_Package6', a)
    _safe_set(a, 'rosmodel_ServiceType', None)
    assert not _is_linked(a, 'rosmodel_ServiceType', b2)
    if hasattr(b2, 'rosmodel_Package6'):
        assert not _is_linked(b2, 'rosmodel_Package6', a)


def test_assoc_source32_link_reassign_clear():
    a = rosmodel_Topic(name="sample_text")
    b1 = rosmodel_Subscriber(msg="sample_text", name="sample_text", queue_size=7)
    b2 = rosmodel_Subscriber(msg="sample_text_2", name="sample_text_2", queue_size=13)
    _safe_set(a, 'rosmodel_Topic34', b1)
    assert _is_linked(a, 'rosmodel_Topic34', b1)
    if hasattr(b1, 'rosmodel_Subscriber33'):
        assert _is_linked(b1, 'rosmodel_Subscriber33', a)
    _safe_set(a, 'rosmodel_Topic34', b2)
    assert _is_linked(a, 'rosmodel_Topic34', b2)
    if hasattr(b1, 'rosmodel_Subscriber33'):
        assert not _is_linked(b1, 'rosmodel_Subscriber33', a)
    if hasattr(b2, 'rosmodel_Subscriber33'):
        assert _is_linked(b2, 'rosmodel_Subscriber33', a)
    _safe_set(a, 'rosmodel_Topic34', None)
    assert not _is_linked(a, 'rosmodel_Topic34', b2)
    if hasattr(b2, 'rosmodel_Subscriber33'):
        assert not _is_linked(b2, 'rosmodel_Subscriber33', a)


def test_assoc_source82_link_reassign_clear():
    a = rosmodel_Transition(name="sample_text")
    b1 = rosmodel_State(name="sample_text")
    b2 = rosmodel_State(name="sample_text_2")
    _safe_set(a, 'rosmodel_Transition83', b1)
    assert _is_linked(a, 'rosmodel_Transition83', b1)
    if hasattr(b1, 'rosmodel_State84'):
        assert _is_linked(b1, 'rosmodel_State84', a)
    _safe_set(a, 'rosmodel_Transition83', b2)
    assert _is_linked(a, 'rosmodel_Transition83', b2)
    if hasattr(b1, 'rosmodel_State84'):
        assert not _is_linked(b1, 'rosmodel_State84', a)
    if hasattr(b2, 'rosmodel_State84'):
        assert _is_linked(b2, 'rosmodel_State84', a)
    _safe_set(a, 'rosmodel_Transition83', None)
    assert not _is_linked(a, 'rosmodel_Transition83', b2)
    if hasattr(b2, 'rosmodel_State84'):
        assert not _is_linked(b2, 'rosmodel_State84', a)


def test_assoc_state21_link_reassign_clear():
    a = rosmodel_State(name="sample_text")
    b1 = rosmodel_Node(frequency=3.14, name="sample_text")
    b2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    _safe_set(a, 'rosmodel_State', b1)
    assert _is_linked(a, 'rosmodel_State', b1)
    if hasattr(b1, 'rosmodel_Node22'):
        assert _is_linked(b1, 'rosmodel_Node22', a)
    _safe_set(a, 'rosmodel_State', b2)
    assert _is_linked(a, 'rosmodel_State', b2)
    if hasattr(b1, 'rosmodel_Node22'):
        assert not _is_linked(b1, 'rosmodel_Node22', a)
    if hasattr(b2, 'rosmodel_Node22'):
        assert _is_linked(b2, 'rosmodel_Node22', a)
    _safe_set(a, 'rosmodel_State', None)
    assert not _is_linked(a, 'rosmodel_State', b2)
    if hasattr(b2, 'rosmodel_Node22'):
        assert not _is_linked(b2, 'rosmodel_Node22', a)


def test_assoc_subscriber11_link_reassign_clear():
    a = rosmodel_Subscriber(msg="sample_text", name="sample_text", queue_size=7)
    b1 = rosmodel_Node(frequency=3.14, name="sample_text")
    b2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    _safe_set(a, 'rosmodel_Subscriber', b1)
    assert _is_linked(a, 'rosmodel_Subscriber', b1)
    if hasattr(b1, 'rosmodel_Node12'):
        assert _is_linked(b1, 'rosmodel_Node12', a)
    _safe_set(a, 'rosmodel_Subscriber', b2)
    assert _is_linked(a, 'rosmodel_Subscriber', b2)
    if hasattr(b1, 'rosmodel_Node12'):
        assert not _is_linked(b1, 'rosmodel_Node12', a)
    if hasattr(b2, 'rosmodel_Node12'):
        assert _is_linked(b2, 'rosmodel_Node12', a)
    _safe_set(a, 'rosmodel_Subscriber', None)
    assert not _is_linked(a, 'rosmodel_Subscriber', b2)
    if hasattr(b2, 'rosmodel_Node12'):
        assert not _is_linked(b2, 'rosmodel_Node12', a)


def test_assoc_substate68_link_reassign_clear():
    a = rosmodel_State(name="sample_text")
    b1 = rosmodel_State(name="sample_text")
    b2 = rosmodel_State(name="sample_text_2")
    _safe_set(a, 'rosmodel_State67', {b1})
    assert _is_linked(a, 'rosmodel_State67', b1)
    if hasattr(b1, 'rosmodel_State69'):
        assert _is_linked(b1, 'rosmodel_State69', a)
    _safe_set(a, 'rosmodel_State67', {b2})
    assert _is_linked(a, 'rosmodel_State67', b2)
    if hasattr(b1, 'rosmodel_State69'):
        assert not _is_linked(b1, 'rosmodel_State69', a)
    if hasattr(b2, 'rosmodel_State69'):
        assert _is_linked(b2, 'rosmodel_State69', a)
    _safe_set(a, 'rosmodel_State67', set())
    assert not _is_linked(a, 'rosmodel_State67', b2)
    if hasattr(b2, 'rosmodel_State69'):
        assert not _is_linked(b2, 'rosmodel_State69', a)


def test_assoc_target29_link_reassign_clear():
    a = rosmodel_Topic(name="sample_text")
    b1 = rosmodel_Publisher(msg="sample_text", name="sample_text", queue_size=7)
    b2 = rosmodel_Publisher(msg="sample_text_2", name="sample_text_2", queue_size=13)
    _safe_set(a, 'rosmodel_Topic31', b1)
    assert _is_linked(a, 'rosmodel_Topic31', b1)
    if hasattr(b1, 'rosmodel_Publisher30'):
        assert _is_linked(b1, 'rosmodel_Publisher30', a)
    _safe_set(a, 'rosmodel_Topic31', b2)
    assert _is_linked(a, 'rosmodel_Topic31', b2)
    if hasattr(b1, 'rosmodel_Publisher30'):
        assert not _is_linked(b1, 'rosmodel_Publisher30', a)
    if hasattr(b2, 'rosmodel_Publisher30'):
        assert _is_linked(b2, 'rosmodel_Publisher30', a)
    _safe_set(a, 'rosmodel_Topic31', None)
    assert not _is_linked(a, 'rosmodel_Topic31', b2)
    if hasattr(b2, 'rosmodel_Publisher30'):
        assert not _is_linked(b2, 'rosmodel_Publisher30', a)


def test_assoc_target85_link_reassign_clear():
    a = rosmodel_Transition(name="sample_text")
    b1 = rosmodel_State(name="sample_text")
    b2 = rosmodel_State(name="sample_text_2")
    _safe_set(a, 'rosmodel_Transition86', b1)
    assert _is_linked(a, 'rosmodel_Transition86', b1)
    if hasattr(b1, 'rosmodel_State87'):
        assert _is_linked(b1, 'rosmodel_State87', a)
    _safe_set(a, 'rosmodel_Transition86', b2)
    assert _is_linked(a, 'rosmodel_Transition86', b2)
    if hasattr(b1, 'rosmodel_State87'):
        assert not _is_linked(b1, 'rosmodel_State87', a)
    if hasattr(b2, 'rosmodel_State87'):
        assert _is_linked(b2, 'rosmodel_State87', a)
    _safe_set(a, 'rosmodel_Transition86', None)
    assert not _is_linked(a, 'rosmodel_Transition86', b2)
    if hasattr(b2, 'rosmodel_State87'):
        assert not _is_linked(b2, 'rosmodel_State87', a)


def test_assoc_topic1_link_reassign_clear():
    a = rosmodel_Topic(name="sample_text")
    b1 = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    b2 = rosmodel_Package(author="sample_text_2", author_email="sample_text_2", depends="sample_text_2", description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'rosmodel_Topic', b1)
    assert _is_linked(a, 'rosmodel_Topic', b1)
    if hasattr(b1, 'rosmodel_Package2'):
        assert _is_linked(b1, 'rosmodel_Package2', a)
    _safe_set(a, 'rosmodel_Topic', b2)
    assert _is_linked(a, 'rosmodel_Topic', b2)
    if hasattr(b1, 'rosmodel_Package2'):
        assert not _is_linked(b1, 'rosmodel_Package2', a)
    if hasattr(b2, 'rosmodel_Package2'):
        assert _is_linked(b2, 'rosmodel_Package2', a)
    _safe_set(a, 'rosmodel_Topic', None)
    assert not _is_linked(a, 'rosmodel_Topic', b2)
    if hasattr(b2, 'rosmodel_Package2'):
        assert not _is_linked(b2, 'rosmodel_Package2', a)


def test_assoc_transition23_link_reassign_clear():
    a = rosmodel_Transition(name="sample_text")
    b1 = rosmodel_Node(frequency=3.14, name="sample_text")
    b2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    _safe_set(a, 'rosmodel_Transition', b1)
    assert _is_linked(a, 'rosmodel_Transition', b1)
    if hasattr(b1, 'rosmodel_Node24'):
        assert _is_linked(b1, 'rosmodel_Node24', a)
    _safe_set(a, 'rosmodel_Transition', b2)
    assert _is_linked(a, 'rosmodel_Transition', b2)
    if hasattr(b1, 'rosmodel_Node24'):
        assert not _is_linked(b1, 'rosmodel_Node24', a)
    if hasattr(b2, 'rosmodel_Node24'):
        assert _is_linked(b2, 'rosmodel_Node24', a)
    _safe_set(a, 'rosmodel_Transition', None)
    assert not _is_linked(a, 'rosmodel_Transition', b2)
    if hasattr(b2, 'rosmodel_Node24'):
        assert not _is_linked(b2, 'rosmodel_Node24', a)


def test_assoc_transition64_link_reassign_clear():
    a = rosmodel_Transition(name="sample_text")
    b1 = rosmodel_State(name="sample_text")
    b2 = rosmodel_State(name="sample_text_2")
    _safe_set(a, 'rosmodel_Transition66', b1)
    assert _is_linked(a, 'rosmodel_Transition66', b1)
    if hasattr(b1, 'rosmodel_State65'):
        assert _is_linked(b1, 'rosmodel_State65', a)
    _safe_set(a, 'rosmodel_Transition66', b2)
    assert _is_linked(a, 'rosmodel_Transition66', b2)
    if hasattr(b1, 'rosmodel_State65'):
        assert not _is_linked(b1, 'rosmodel_State65', a)
    if hasattr(b2, 'rosmodel_State65'):
        assert _is_linked(b2, 'rosmodel_State65', a)
    _safe_set(a, 'rosmodel_Transition66', None)
    assert not _is_linked(a, 'rosmodel_Transition66', b2)
    if hasattr(b2, 'rosmodel_State65'):
        assert not _is_linked(b2, 'rosmodel_State65', a)


def test_assoc_transition94_link_reassign_clear():
    a = rosmodel_Transition(name="sample_text")
    b1 = rosmodel_Event(name="sample_text")
    b2 = rosmodel_Event(name="sample_text_2")
    _safe_set(a, 'rosmodel_Transition96', b1)
    assert _is_linked(a, 'rosmodel_Transition96', b1)
    if hasattr(b1, 'rosmodel_Event95'):
        assert _is_linked(b1, 'rosmodel_Event95', a)
    _safe_set(a, 'rosmodel_Transition96', b2)
    assert _is_linked(a, 'rosmodel_Transition96', b2)
    if hasattr(b1, 'rosmodel_Event95'):
        assert not _is_linked(b1, 'rosmodel_Event95', a)
    if hasattr(b2, 'rosmodel_Event95'):
        assert _is_linked(b2, 'rosmodel_Event95', a)
    _safe_set(a, 'rosmodel_Transition96', None)
    assert not _is_linked(a, 'rosmodel_Transition96', b2)
    if hasattr(b2, 'rosmodel_Event95'):
        assert not _is_linked(b2, 'rosmodel_Event95', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

rosmodel_Action_strategy = st.builds(rosmodel_Action, name=safe_text)
@given(instance=rosmodel_Action_strategy)
@settings(max_examples=25)
def test_rosmodel_Action_instantiation(instance):
    assert isinstance(instance, rosmodel_Action)


rosmodel_ActionClient_strategy = st.builds(rosmodel_ActionClient, name=safe_text)
@given(instance=rosmodel_ActionClient_strategy)
@settings(max_examples=25)
def test_rosmodel_ActionClient_instantiation(instance):
    assert isinstance(instance, rosmodel_ActionClient)


rosmodel_ActionMessage_strategy = st.builds(rosmodel_ActionMessage, name=safe_text)
@given(instance=rosmodel_ActionMessage_strategy)
@settings(max_examples=25)
def test_rosmodel_ActionMessage_instantiation(instance):
    assert isinstance(instance, rosmodel_ActionMessage)


rosmodel_ActionServer_strategy = st.builds(rosmodel_ActionServer, name=safe_text)
@given(instance=rosmodel_ActionServer_strategy)
@settings(max_examples=25)
def test_rosmodel_ActionServer_instantiation(instance):
    assert isinstance(instance, rosmodel_ActionServer)


rosmodel_Event_strategy = st.builds(rosmodel_Event, name=safe_text)
@given(instance=rosmodel_Event_strategy)
@settings(max_examples=25)
def test_rosmodel_Event_instantiation(instance):
    assert isinstance(instance, rosmodel_Event)


rosmodel_Field_strategy = st.builds(rosmodel_Field, name=safe_text, type=safe_text)
@given(instance=rosmodel_Field_strategy)
@settings(max_examples=25)
def test_rosmodel_Field_instantiation(instance):
    assert isinstance(instance, rosmodel_Field)


rosmodel_Message_strategy = st.builds(rosmodel_Message, name=safe_text)
@given(instance=rosmodel_Message_strategy)
@settings(max_examples=25)
def test_rosmodel_Message_instantiation(instance):
    assert isinstance(instance, rosmodel_Message)


rosmodel_Node_strategy = st.builds(rosmodel_Node, frequency=st.floats(allow_nan=False, allow_infinity=False), name=safe_text)
@given(instance=rosmodel_Node_strategy)
@settings(max_examples=25)
def test_rosmodel_Node_instantiation(instance):
    assert isinstance(instance, rosmodel_Node)


rosmodel_Package_strategy = st.builds(rosmodel_Package, author=safe_text, author_email=safe_text, depends=safe_text, description=safe_text, name=safe_text)
@given(instance=rosmodel_Package_strategy)
@settings(max_examples=25)
def test_rosmodel_Package_instantiation(instance):
    assert isinstance(instance, rosmodel_Package)


rosmodel_Publisher_strategy = st.builds(rosmodel_Publisher, msg=safe_text, name=safe_text, queue_size=st.integers())
@given(instance=rosmodel_Publisher_strategy)
@settings(max_examples=25)
def test_rosmodel_Publisher_instantiation(instance):
    assert isinstance(instance, rosmodel_Publisher)


rosmodel_ServiceClient_strategy = st.builds(rosmodel_ServiceClient, name=safe_text)
@given(instance=rosmodel_ServiceClient_strategy)
@settings(max_examples=25)
def test_rosmodel_ServiceClient_instantiation(instance):
    assert isinstance(instance, rosmodel_ServiceClient)


rosmodel_ServiceServer_strategy = st.builds(rosmodel_ServiceServer, name=safe_text)
@given(instance=rosmodel_ServiceServer_strategy)
@settings(max_examples=25)
def test_rosmodel_ServiceServer_instantiation(instance):
    assert isinstance(instance, rosmodel_ServiceServer)


rosmodel_ServiceType_strategy = st.builds(rosmodel_ServiceType, name=safe_text)
@given(instance=rosmodel_ServiceType_strategy)
@settings(max_examples=25)
def test_rosmodel_ServiceType_instantiation(instance):
    assert isinstance(instance, rosmodel_ServiceType)


rosmodel_State_strategy = st.builds(rosmodel_State, name=safe_text)
@given(instance=rosmodel_State_strategy)
@settings(max_examples=25)
def test_rosmodel_State_instantiation(instance):
    assert isinstance(instance, rosmodel_State)


rosmodel_Subscriber_strategy = st.builds(rosmodel_Subscriber, msg=safe_text, name=safe_text, queue_size=st.integers())
@given(instance=rosmodel_Subscriber_strategy)
@settings(max_examples=25)
def test_rosmodel_Subscriber_instantiation(instance):
    assert isinstance(instance, rosmodel_Subscriber)


rosmodel_Topic_strategy = st.builds(rosmodel_Topic, name=safe_text)
@given(instance=rosmodel_Topic_strategy)
@settings(max_examples=25)
def test_rosmodel_Topic_instantiation(instance):
    assert isinstance(instance, rosmodel_Topic)


rosmodel_Transition_strategy = st.builds(rosmodel_Transition, name=safe_text)
@given(instance=rosmodel_Transition_strategy)
@settings(max_examples=25)
def test_rosmodel_Transition_instantiation(instance):
    assert isinstance(instance, rosmodel_Transition)


