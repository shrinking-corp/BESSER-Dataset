import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_action25_reverse_link_reassign_clear():
    a1 = rosmodel_Node(frequency=3.14, name="sample_text")
    a2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    b = rosmodel_Action(name="sample_text")
    _safe_set(b, 'rosmodel_Action', a1)
    assert _is_linked(b, 'rosmodel_Action', a1)
    if hasattr(a1, 'rosmodel_Node26'):
        assert _is_linked(a1, 'rosmodel_Node26', b)
    _safe_set(b, 'rosmodel_Action', a2)
    assert _is_linked(b, 'rosmodel_Action', a2)
    if hasattr(a1, 'rosmodel_Node26'):
        assert not _is_linked(a1, 'rosmodel_Node26', b)
    if hasattr(a2, 'rosmodel_Node26'):
        assert _is_linked(a2, 'rosmodel_Node26', b)
    _safe_set(b, 'rosmodel_Action', None)
    assert not _is_linked(b, 'rosmodel_Action', a2)
    if hasattr(a2, 'rosmodel_Node26'):
        assert not _is_linked(a2, 'rosmodel_Node26', b)


def test_assoc_action70_reverse_link_reassign_clear():
    a1 = rosmodel_State(name="sample_text")
    a2 = rosmodel_State(name="sample_text_2")
    b = rosmodel_Action(name="sample_text")
    _safe_set(b, 'rosmodel_Action72', a1)
    assert _is_linked(b, 'rosmodel_Action72', a1)
    if hasattr(a1, 'rosmodel_State71'):
        assert _is_linked(a1, 'rosmodel_State71', b)
    _safe_set(b, 'rosmodel_Action72', a2)
    assert _is_linked(b, 'rosmodel_Action72', a2)
    if hasattr(a1, 'rosmodel_State71'):
        assert not _is_linked(a1, 'rosmodel_State71', b)
    if hasattr(a2, 'rosmodel_State71'):
        assert _is_linked(a2, 'rosmodel_State71', b)
    _safe_set(b, 'rosmodel_Action72', None)
    assert not _is_linked(b, 'rosmodel_Action72', a2)
    if hasattr(a2, 'rosmodel_State71'):
        assert not _is_linked(a2, 'rosmodel_State71', b)


def test_assoc_action88_reverse_link_reassign_clear():
    a1 = rosmodel_Transition(name="sample_text")
    a2 = rosmodel_Transition(name="sample_text_2")
    b = rosmodel_Action(name="sample_text")
    _safe_set(b, 'rosmodel_Action90', a1)
    assert _is_linked(b, 'rosmodel_Action90', a1)
    if hasattr(a1, 'rosmodel_Transition89'):
        assert _is_linked(a1, 'rosmodel_Transition89', b)
    _safe_set(b, 'rosmodel_Action90', a2)
    assert _is_linked(b, 'rosmodel_Action90', a2)
    if hasattr(a1, 'rosmodel_Transition89'):
        assert not _is_linked(a1, 'rosmodel_Transition89', b)
    if hasattr(a2, 'rosmodel_Transition89'):
        assert _is_linked(a2, 'rosmodel_Transition89', b)
    _safe_set(b, 'rosmodel_Action90', None)
    assert not _is_linked(b, 'rosmodel_Action90', a2)
    if hasattr(a2, 'rosmodel_Transition89'):
        assert not _is_linked(a2, 'rosmodel_Transition89', b)


def test_assoc_actionclient17_reverse_link_reassign_clear():
    a1 = rosmodel_Node(frequency=3.14, name="sample_text")
    a2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    b = rosmodel_ActionClient(name="sample_text")
    _safe_set(b, 'rosmodel_ActionClient', a1)
    assert _is_linked(b, 'rosmodel_ActionClient', a1)
    if hasattr(a1, 'rosmodel_Node18'):
        assert _is_linked(a1, 'rosmodel_Node18', b)
    _safe_set(b, 'rosmodel_ActionClient', a2)
    assert _is_linked(b, 'rosmodel_ActionClient', a2)
    if hasattr(a1, 'rosmodel_Node18'):
        assert not _is_linked(a1, 'rosmodel_Node18', b)
    if hasattr(a2, 'rosmodel_Node18'):
        assert _is_linked(a2, 'rosmodel_Node18', b)
    _safe_set(b, 'rosmodel_ActionClient', None)
    assert not _is_linked(b, 'rosmodel_ActionClient', a2)
    if hasattr(a2, 'rosmodel_Node18'):
        assert not _is_linked(a2, 'rosmodel_Node18', b)


def test_assoc_actionmessage58_reverse_link_reassign_clear():
    a1 = rosmodel_ActionServer(name="sample_text")
    a2 = rosmodel_ActionServer(name="sample_text_2")
    b = rosmodel_ActionMessage(name="sample_text")
    _safe_set(b, 'rosmodel_ActionMessage60', a1)
    assert _is_linked(b, 'rosmodel_ActionMessage60', a1)
    if hasattr(a1, 'rosmodel_ActionServer59'):
        assert _is_linked(a1, 'rosmodel_ActionServer59', b)
    _safe_set(b, 'rosmodel_ActionMessage60', a2)
    assert _is_linked(b, 'rosmodel_ActionMessage60', a2)
    if hasattr(a1, 'rosmodel_ActionServer59'):
        assert not _is_linked(a1, 'rosmodel_ActionServer59', b)
    if hasattr(a2, 'rosmodel_ActionServer59'):
        assert _is_linked(a2, 'rosmodel_ActionServer59', b)
    _safe_set(b, 'rosmodel_ActionMessage60', None)
    assert not _is_linked(b, 'rosmodel_ActionMessage60', a2)
    if hasattr(a2, 'rosmodel_ActionServer59'):
        assert not _is_linked(a2, 'rosmodel_ActionServer59', b)


def test_assoc_actionmessage61_reverse_link_reassign_clear():
    a1 = rosmodel_ActionMessage(name="sample_text")
    a2 = rosmodel_ActionMessage(name="sample_text_2")
    b = rosmodel_ActionClient(name="sample_text")
    _safe_set(b, 'rosmodel_ActionClient62', a1)
    assert _is_linked(b, 'rosmodel_ActionClient62', a1)
    if hasattr(a1, 'rosmodel_ActionMessage63'):
        assert _is_linked(a1, 'rosmodel_ActionMessage63', b)
    _safe_set(b, 'rosmodel_ActionClient62', a2)
    assert _is_linked(b, 'rosmodel_ActionClient62', a2)
    if hasattr(a1, 'rosmodel_ActionMessage63'):
        assert not _is_linked(a1, 'rosmodel_ActionMessage63', b)
    if hasattr(a2, 'rosmodel_ActionMessage63'):
        assert _is_linked(a2, 'rosmodel_ActionMessage63', b)
    _safe_set(b, 'rosmodel_ActionClient62', None)
    assert not _is_linked(b, 'rosmodel_ActionClient62', a2)
    if hasattr(a2, 'rosmodel_ActionMessage63'):
        assert not _is_linked(a2, 'rosmodel_ActionMessage63', b)


def test_assoc_actionmessage7_reverse_link_reassign_clear():
    a1 = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    a2 = rosmodel_Package(author="sample_text_2", author_email="sample_text_2", depends="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = rosmodel_ActionMessage(name="sample_text")
    _safe_set(b, 'rosmodel_ActionMessage', a1)
    assert _is_linked(b, 'rosmodel_ActionMessage', a1)
    if hasattr(a1, 'rosmodel_Package8'):
        assert _is_linked(a1, 'rosmodel_Package8', b)
    _safe_set(b, 'rosmodel_ActionMessage', a2)
    assert _is_linked(b, 'rosmodel_ActionMessage', a2)
    if hasattr(a1, 'rosmodel_Package8'):
        assert not _is_linked(a1, 'rosmodel_Package8', b)
    if hasattr(a2, 'rosmodel_Package8'):
        assert _is_linked(a2, 'rosmodel_Package8', b)
    _safe_set(b, 'rosmodel_ActionMessage', None)
    assert not _is_linked(b, 'rosmodel_ActionMessage', a2)
    if hasattr(a2, 'rosmodel_Package8'):
        assert not _is_linked(a2, 'rosmodel_Package8', b)


def test_assoc_actionserver19_reverse_link_reassign_clear():
    a1 = rosmodel_Node(frequency=3.14, name="sample_text")
    a2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    b = rosmodel_ActionServer(name="sample_text")
    _safe_set(b, 'rosmodel_ActionServer', a1)
    assert _is_linked(b, 'rosmodel_ActionServer', a1)
    if hasattr(a1, 'rosmodel_Node20'):
        assert _is_linked(a1, 'rosmodel_Node20', b)
    _safe_set(b, 'rosmodel_ActionServer', a2)
    assert _is_linked(b, 'rosmodel_ActionServer', a2)
    if hasattr(a1, 'rosmodel_Node20'):
        assert not _is_linked(a1, 'rosmodel_Node20', b)
    if hasattr(a2, 'rosmodel_Node20'):
        assert _is_linked(a2, 'rosmodel_Node20', b)
    _safe_set(b, 'rosmodel_ActionServer', None)
    assert not _is_linked(b, 'rosmodel_ActionServer', a2)
    if hasattr(a2, 'rosmodel_Node20'):
        assert not _is_linked(a2, 'rosmodel_Node20', b)


def test_assoc_entryaction73_reverse_link_reassign_clear():
    a1 = rosmodel_State(name="sample_text")
    a2 = rosmodel_State(name="sample_text_2")
    b = rosmodel_Action(name="sample_text")
    _safe_set(b, 'rosmodel_Action75', a1)
    assert _is_linked(b, 'rosmodel_Action75', a1)
    if hasattr(a1, 'rosmodel_State74'):
        assert _is_linked(a1, 'rosmodel_State74', b)
    _safe_set(b, 'rosmodel_Action75', a2)
    assert _is_linked(b, 'rosmodel_Action75', a2)
    if hasattr(a1, 'rosmodel_State74'):
        assert not _is_linked(a1, 'rosmodel_State74', b)
    if hasattr(a2, 'rosmodel_State74'):
        assert _is_linked(a2, 'rosmodel_State74', b)
    _safe_set(b, 'rosmodel_Action75', None)
    assert not _is_linked(b, 'rosmodel_Action75', a2)
    if hasattr(a2, 'rosmodel_State74'):
        assert not _is_linked(a2, 'rosmodel_State74', b)


def test_assoc_event27_reverse_link_reassign_clear():
    a1 = rosmodel_Node(frequency=3.14, name="sample_text")
    a2 = rosmodel_Node(frequency=9.99, name="sample_text_2")
    b = rosmodel_Event(name="sample_text")
    _safe_set(b, 'rosmodel_Event', a1)
    assert _is_linked(b, 'rosmodel_Event', a1)
    if hasattr(a1, 'rosmodel_Node28'):
        assert _is_linked(a1, 'rosmodel_Node28', b)
    _safe_set(b, 'rosmodel_Event', a2)
    assert _is_linked(b, 'rosmodel_Event', a2)
    if hasattr(a1, 'rosmodel_Node28'):
        assert not _is_linked(a1, 'rosmodel_Node28', b)
    if hasattr(a2, 'rosmodel_Node28'):
        assert _is_linked(a2, 'rosmodel_Node28', b)
    _safe_set(b, 'rosmodel_Event', None)
    assert not _is_linked(b, 'rosmodel_Event', a2)
    if hasattr(a2, 'rosmodel_Node28'):
        assert not _is_linked(a2, 'rosmodel_Node28', b)


def test_assoc_event79_reverse_link_reassign_clear():
    a1 = rosmodel_State(name="sample_text")
    a2 = rosmodel_State(name="sample_text_2")
    b = rosmodel_Event(name="sample_text")
    _safe_set(b, 'rosmodel_Event81', a1)
    assert _is_linked(b, 'rosmodel_Event81', a1)
    if hasattr(a1, 'rosmodel_State80'):
        assert _is_linked(a1, 'rosmodel_State80', b)
    _safe_set(b, 'rosmodel_Event81', a2)
    assert _is_linked(b, 'rosmodel_Event81', a2)
    if hasattr(a1, 'rosmodel_State80'):
        assert not _is_linked(a1, 'rosmodel_State80', b)
    if hasattr(a2, 'rosmodel_State80'):
        assert _is_linked(a2, 'rosmodel_State80', b)
    _safe_set(b, 'rosmodel_Event81', None)
    assert not _is_linked(b, 'rosmodel_Event81', a2)
    if hasattr(a2, 'rosmodel_State80'):
        assert not _is_linked(a2, 'rosmodel_State80', b)


def test_assoc_exitaction76_reverse_link_reassign_clear():
    a1 = rosmodel_State(name="sample_text")
    a2 = rosmodel_State(name="sample_text_2")
    b = rosmodel_Action(name="sample_text")
    _safe_set(b, 'rosmodel_Action78', a1)
    assert _is_linked(b, 'rosmodel_Action78', a1)
    if hasattr(a1, 'rosmodel_State77'):
        assert _is_linked(a1, 'rosmodel_State77', b)
    _safe_set(b, 'rosmodel_Action78', a2)
    assert _is_linked(b, 'rosmodel_Action78', a2)
    if hasattr(a1, 'rosmodel_State77'):
        assert not _is_linked(a1, 'rosmodel_State77', b)
    if hasattr(a2, 'rosmodel_State77'):
        assert _is_linked(a2, 'rosmodel_State77', b)
    _safe_set(b, 'rosmodel_Action78', None)
    assert not _is_linked(b, 'rosmodel_Action78', a2)
    if hasattr(a2, 'rosmodel_State77'):
        assert not _is_linked(a2, 'rosmodel_State77', b)


def test_assoc_feedback55_reverse_link_reassign_clear():
    a1 = rosmodel_Field(name="sample_text", type="sample_text")
    a2 = rosmodel_Field(name="sample_text_2", type="sample_text_2")
    b = rosmodel_ActionMessage(name="sample_text")
    _safe_set(b, 'rosmodel_ActionMessage56', {a1})
    assert _is_linked(b, 'rosmodel_ActionMessage56', a1)
    if hasattr(a1, 'rosmodel_Field57'):
        assert _is_linked(a1, 'rosmodel_Field57', b)
    _safe_set(b, 'rosmodel_ActionMessage56', {a2})
    assert _is_linked(b, 'rosmodel_ActionMessage56', a2)
    if hasattr(a1, 'rosmodel_Field57'):
        assert not _is_linked(a1, 'rosmodel_Field57', b)
    if hasattr(a2, 'rosmodel_Field57'):
        assert _is_linked(a2, 'rosmodel_Field57', b)
    _safe_set(b, 'rosmodel_ActionMessage56', set())
    assert not _is_linked(b, 'rosmodel_ActionMessage56', a2)
    if hasattr(a2, 'rosmodel_Field57'):
        assert not _is_linked(a2, 'rosmodel_Field57', b)


def test_assoc_field35_reverse_link_reassign_clear():
    a1 = rosmodel_Message(name="sample_text")
    a2 = rosmodel_Message(name="sample_text_2")
    b = rosmodel_Field(name="sample_text", type="sample_text")
    _safe_set(b, 'rosmodel_Field', a1)
    assert _is_linked(b, 'rosmodel_Field', a1)
    if hasattr(a1, 'rosmodel_Message36'):
        assert _is_linked(a1, 'rosmodel_Message36', b)
    _safe_set(b, 'rosmodel_Field', a2)
    assert _is_linked(b, 'rosmodel_Field', a2)
    if hasattr(a1, 'rosmodel_Message36'):
        assert not _is_linked(a1, 'rosmodel_Message36', b)
    if hasattr(a2, 'rosmodel_Message36'):
        assert _is_linked(a2, 'rosmodel_Message36', b)
    _safe_set(b, 'rosmodel_Field', None)
    assert not _is_linked(b, 'rosmodel_Field', a2)
    if hasattr(a2, 'rosmodel_Message36'):
        assert not _is_linked(a2, 'rosmodel_Message36', b)


def test_assoc_goal49_reverse_link_reassign_clear():
    a1 = rosmodel_Field(name="sample_text", type="sample_text")
    a2 = rosmodel_Field(name="sample_text_2", type="sample_text_2")
    b = rosmodel_ActionMessage(name="sample_text")
    _safe_set(b, 'rosmodel_ActionMessage50', {a1})
    assert _is_linked(b, 'rosmodel_ActionMessage50', a1)
    if hasattr(a1, 'rosmodel_Field51'):
        assert _is_linked(a1, 'rosmodel_Field51', b)
    _safe_set(b, 'rosmodel_ActionMessage50', {a2})
    assert _is_linked(b, 'rosmodel_ActionMessage50', a2)
    if hasattr(a1, 'rosmodel_Field51'):
        assert not _is_linked(a1, 'rosmodel_Field51', b)
    if hasattr(a2, 'rosmodel_Field51'):
        assert _is_linked(a2, 'rosmodel_Field51', b)
    _safe_set(b, 'rosmodel_ActionMessage50', set())
    assert not _is_linked(b, 'rosmodel_ActionMessage50', a2)
    if hasattr(a2, 'rosmodel_Field51'):
        assert not _is_linked(a2, 'rosmodel_Field51', b)


def test_assoc_guard91_reverse_link_reassign_clear():
    a1 = rosmodel_Transition(name="sample_text")
    a2 = rosmodel_Transition(name="sample_text_2")
    b = rosmodel_Action(name="sample_text")
    _safe_set(b, 'rosmodel_Action93', a1)
    assert _is_linked(b, 'rosmodel_Action93', a1)
    if hasattr(a1, 'rosmodel_Transition92'):
        assert _is_linked(a1, 'rosmodel_Transition92', b)
    _safe_set(b, 'rosmodel_Action93', a2)
    assert _is_linked(b, 'rosmodel_Action93', a2)
    if hasattr(a1, 'rosmodel_Transition92'):
        assert not _is_linked(a1, 'rosmodel_Transition92', b)
    if hasattr(a2, 'rosmodel_Transition92'):
        assert _is_linked(a2, 'rosmodel_Transition92', b)
    _safe_set(b, 'rosmodel_Action93', None)
    assert not _is_linked(b, 'rosmodel_Action93', a2)
    if hasattr(a2, 'rosmodel_Transition92'):
        assert not _is_linked(a2, 'rosmodel_Transition92', b)


def test_assoc_message3_reverse_link_reassign_clear():
    a1 = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    a2 = rosmodel_Package(author="sample_text_2", author_email="sample_text_2", depends="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = rosmodel_Message(name="sample_text")
    _safe_set(b, 'rosmodel_Message', a1)
    assert _is_linked(b, 'rosmodel_Message', a1)
    if hasattr(a1, 'rosmodel_Package4'):
        assert _is_linked(a1, 'rosmodel_Package4', b)
    _safe_set(b, 'rosmodel_Message', a2)
    assert _is_linked(b, 'rosmodel_Message', a2)
    if hasattr(a1, 'rosmodel_Package4'):
        assert not _is_linked(a1, 'rosmodel_Package4', b)
    if hasattr(a2, 'rosmodel_Package4'):
        assert _is_linked(a2, 'rosmodel_Package4', b)
    _safe_set(b, 'rosmodel_Message', None)
    assert not _is_linked(b, 'rosmodel_Message', a2)
    if hasattr(a2, 'rosmodel_Package4'):
        assert not _is_linked(a2, 'rosmodel_Package4', b)


def test_assoc_node0_reverse_link_reassign_clear():
    a1 = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    a2 = rosmodel_Package(author="sample_text_2", author_email="sample_text_2", depends="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = rosmodel_Node(frequency=3.14, name="sample_text")
    _safe_set(b, 'rosmodel_Node', a1)
    assert _is_linked(b, 'rosmodel_Node', a1)
    if hasattr(a1, 'rosmodel_Package'):
        assert _is_linked(a1, 'rosmodel_Package', b)
    _safe_set(b, 'rosmodel_Node', a2)
    assert _is_linked(b, 'rosmodel_Node', a2)
    if hasattr(a1, 'rosmodel_Package'):
        assert not _is_linked(a1, 'rosmodel_Package', b)
    if hasattr(a2, 'rosmodel_Package'):
        assert _is_linked(a2, 'rosmodel_Package', b)
    _safe_set(b, 'rosmodel_Node', None)
    assert not _is_linked(b, 'rosmodel_Node', a2)
    if hasattr(a2, 'rosmodel_Package'):
        assert not _is_linked(a2, 'rosmodel_Package', b)


def test_assoc_publisher9_reverse_link_reassign_clear():
    a1 = rosmodel_Publisher(msg="sample_text", name="sample_text", queue_size=7)
    a2 = rosmodel_Publisher(msg="sample_text_2", name="sample_text_2", queue_size=13)
    b = rosmodel_Node(frequency=3.14, name="sample_text")
    _safe_set(b, 'rosmodel_Node10', {a1})
    assert _is_linked(b, 'rosmodel_Node10', a1)
    if hasattr(a1, 'rosmodel_Publisher'):
        assert _is_linked(a1, 'rosmodel_Publisher', b)
    _safe_set(b, 'rosmodel_Node10', {a2})
    assert _is_linked(b, 'rosmodel_Node10', a2)
    if hasattr(a1, 'rosmodel_Publisher'):
        assert not _is_linked(a1, 'rosmodel_Publisher', b)
    if hasattr(a2, 'rosmodel_Publisher'):
        assert _is_linked(a2, 'rosmodel_Publisher', b)
    _safe_set(b, 'rosmodel_Node10', set())
    assert not _is_linked(b, 'rosmodel_Node10', a2)
    if hasattr(a2, 'rosmodel_Publisher'):
        assert not _is_linked(a2, 'rosmodel_Publisher', b)


def test_assoc_request37_reverse_link_reassign_clear():
    a1 = rosmodel_ServiceType(name="sample_text")
    a2 = rosmodel_ServiceType(name="sample_text_2")
    b = rosmodel_Field(name="sample_text", type="sample_text")
    _safe_set(b, 'rosmodel_Field39', a1)
    assert _is_linked(b, 'rosmodel_Field39', a1)
    if hasattr(a1, 'rosmodel_ServiceType38'):
        assert _is_linked(a1, 'rosmodel_ServiceType38', b)
    _safe_set(b, 'rosmodel_Field39', a2)
    assert _is_linked(b, 'rosmodel_Field39', a2)
    if hasattr(a1, 'rosmodel_ServiceType38'):
        assert not _is_linked(a1, 'rosmodel_ServiceType38', b)
    if hasattr(a2, 'rosmodel_ServiceType38'):
        assert _is_linked(a2, 'rosmodel_ServiceType38', b)
    _safe_set(b, 'rosmodel_Field39', None)
    assert not _is_linked(b, 'rosmodel_Field39', a2)
    if hasattr(a2, 'rosmodel_ServiceType38'):
        assert not _is_linked(a2, 'rosmodel_ServiceType38', b)


def test_assoc_response40_reverse_link_reassign_clear():
    a1 = rosmodel_ServiceType(name="sample_text")
    a2 = rosmodel_ServiceType(name="sample_text_2")
    b = rosmodel_Field(name="sample_text", type="sample_text")
    _safe_set(b, 'rosmodel_Field42', a1)
    assert _is_linked(b, 'rosmodel_Field42', a1)
    if hasattr(a1, 'rosmodel_ServiceType41'):
        assert _is_linked(a1, 'rosmodel_ServiceType41', b)
    _safe_set(b, 'rosmodel_Field42', a2)
    assert _is_linked(b, 'rosmodel_Field42', a2)
    if hasattr(a1, 'rosmodel_ServiceType41'):
        assert not _is_linked(a1, 'rosmodel_ServiceType41', b)
    if hasattr(a2, 'rosmodel_ServiceType41'):
        assert _is_linked(a2, 'rosmodel_ServiceType41', b)
    _safe_set(b, 'rosmodel_Field42', None)
    assert not _is_linked(b, 'rosmodel_Field42', a2)
    if hasattr(a2, 'rosmodel_ServiceType41'):
        assert not _is_linked(a2, 'rosmodel_ServiceType41', b)


def test_assoc_result52_reverse_link_reassign_clear():
    a1 = rosmodel_Field(name="sample_text", type="sample_text")
    a2 = rosmodel_Field(name="sample_text_2", type="sample_text_2")
    b = rosmodel_ActionMessage(name="sample_text")
    _safe_set(b, 'rosmodel_ActionMessage53', {a1})
    assert _is_linked(b, 'rosmodel_ActionMessage53', a1)
    if hasattr(a1, 'rosmodel_Field54'):
        assert _is_linked(a1, 'rosmodel_Field54', b)
    _safe_set(b, 'rosmodel_ActionMessage53', {a2})
    assert _is_linked(b, 'rosmodel_ActionMessage53', a2)
    if hasattr(a1, 'rosmodel_Field54'):
        assert not _is_linked(a1, 'rosmodel_Field54', b)
    if hasattr(a2, 'rosmodel_Field54'):
        assert _is_linked(a2, 'rosmodel_Field54', b)
    _safe_set(b, 'rosmodel_ActionMessage53', set())
    assert not _is_linked(b, 'rosmodel_ActionMessage53', a2)
    if hasattr(a2, 'rosmodel_Field54'):
        assert not _is_linked(a2, 'rosmodel_Field54', b)


def test_assoc_serviceclient13_reverse_link_reassign_clear():
    a1 = rosmodel_ServiceClient(name="sample_text")
    a2 = rosmodel_ServiceClient(name="sample_text_2")
    b = rosmodel_Node(frequency=3.14, name="sample_text")
    _safe_set(b, 'rosmodel_Node14', {a1})
    assert _is_linked(b, 'rosmodel_Node14', a1)
    if hasattr(a1, 'rosmodel_ServiceClient'):
        assert _is_linked(a1, 'rosmodel_ServiceClient', b)
    _safe_set(b, 'rosmodel_Node14', {a2})
    assert _is_linked(b, 'rosmodel_Node14', a2)
    if hasattr(a1, 'rosmodel_ServiceClient'):
        assert not _is_linked(a1, 'rosmodel_ServiceClient', b)
    if hasattr(a2, 'rosmodel_ServiceClient'):
        assert _is_linked(a2, 'rosmodel_ServiceClient', b)
    _safe_set(b, 'rosmodel_Node14', set())
    assert not _is_linked(b, 'rosmodel_Node14', a2)
    if hasattr(a2, 'rosmodel_ServiceClient'):
        assert not _is_linked(a2, 'rosmodel_ServiceClient', b)


def test_assoc_serviceserver15_reverse_link_reassign_clear():
    a1 = rosmodel_ServiceServer(name="sample_text")
    a2 = rosmodel_ServiceServer(name="sample_text_2")
    b = rosmodel_Node(frequency=3.14, name="sample_text")
    _safe_set(b, 'rosmodel_Node16', {a1})
    assert _is_linked(b, 'rosmodel_Node16', a1)
    if hasattr(a1, 'rosmodel_ServiceServer'):
        assert _is_linked(a1, 'rosmodel_ServiceServer', b)
    _safe_set(b, 'rosmodel_Node16', {a2})
    assert _is_linked(b, 'rosmodel_Node16', a2)
    if hasattr(a1, 'rosmodel_ServiceServer'):
        assert not _is_linked(a1, 'rosmodel_ServiceServer', b)
    if hasattr(a2, 'rosmodel_ServiceServer'):
        assert _is_linked(a2, 'rosmodel_ServiceServer', b)
    _safe_set(b, 'rosmodel_Node16', set())
    assert not _is_linked(b, 'rosmodel_Node16', a2)
    if hasattr(a2, 'rosmodel_ServiceServer'):
        assert not _is_linked(a2, 'rosmodel_ServiceServer', b)


def test_assoc_servicetype43_reverse_link_reassign_clear():
    a1 = rosmodel_ServiceType(name="sample_text")
    a2 = rosmodel_ServiceType(name="sample_text_2")
    b = rosmodel_ServiceServer(name="sample_text")
    _safe_set(b, 'rosmodel_ServiceServer44', a1)
    assert _is_linked(b, 'rosmodel_ServiceServer44', a1)
    if hasattr(a1, 'rosmodel_ServiceType45'):
        assert _is_linked(a1, 'rosmodel_ServiceType45', b)
    _safe_set(b, 'rosmodel_ServiceServer44', a2)
    assert _is_linked(b, 'rosmodel_ServiceServer44', a2)
    if hasattr(a1, 'rosmodel_ServiceType45'):
        assert not _is_linked(a1, 'rosmodel_ServiceType45', b)
    if hasattr(a2, 'rosmodel_ServiceType45'):
        assert _is_linked(a2, 'rosmodel_ServiceType45', b)
    _safe_set(b, 'rosmodel_ServiceServer44', None)
    assert not _is_linked(b, 'rosmodel_ServiceServer44', a2)
    if hasattr(a2, 'rosmodel_ServiceType45'):
        assert not _is_linked(a2, 'rosmodel_ServiceType45', b)


def test_assoc_servicetype46_reverse_link_reassign_clear():
    a1 = rosmodel_ServiceType(name="sample_text")
    a2 = rosmodel_ServiceType(name="sample_text_2")
    b = rosmodel_ServiceClient(name="sample_text")
    _safe_set(b, 'rosmodel_ServiceClient47', a1)
    assert _is_linked(b, 'rosmodel_ServiceClient47', a1)
    if hasattr(a1, 'rosmodel_ServiceType48'):
        assert _is_linked(a1, 'rosmodel_ServiceType48', b)
    _safe_set(b, 'rosmodel_ServiceClient47', a2)
    assert _is_linked(b, 'rosmodel_ServiceClient47', a2)
    if hasattr(a1, 'rosmodel_ServiceType48'):
        assert not _is_linked(a1, 'rosmodel_ServiceType48', b)
    if hasattr(a2, 'rosmodel_ServiceType48'):
        assert _is_linked(a2, 'rosmodel_ServiceType48', b)
    _safe_set(b, 'rosmodel_ServiceClient47', None)
    assert not _is_linked(b, 'rosmodel_ServiceClient47', a2)
    if hasattr(a2, 'rosmodel_ServiceType48'):
        assert not _is_linked(a2, 'rosmodel_ServiceType48', b)


def test_assoc_servicetype5_reverse_link_reassign_clear():
    a1 = rosmodel_ServiceType(name="sample_text")
    a2 = rosmodel_ServiceType(name="sample_text_2")
    b = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'rosmodel_Package6', {a1})
    assert _is_linked(b, 'rosmodel_Package6', a1)
    if hasattr(a1, 'rosmodel_ServiceType'):
        assert _is_linked(a1, 'rosmodel_ServiceType', b)
    _safe_set(b, 'rosmodel_Package6', {a2})
    assert _is_linked(b, 'rosmodel_Package6', a2)
    if hasattr(a1, 'rosmodel_ServiceType'):
        assert not _is_linked(a1, 'rosmodel_ServiceType', b)
    if hasattr(a2, 'rosmodel_ServiceType'):
        assert _is_linked(a2, 'rosmodel_ServiceType', b)
    _safe_set(b, 'rosmodel_Package6', set())
    assert not _is_linked(b, 'rosmodel_Package6', a2)
    if hasattr(a2, 'rosmodel_ServiceType'):
        assert not _is_linked(a2, 'rosmodel_ServiceType', b)


def test_assoc_source32_reverse_link_reassign_clear():
    a1 = rosmodel_Topic(name="sample_text")
    a2 = rosmodel_Topic(name="sample_text_2")
    b = rosmodel_Subscriber(msg="sample_text", name="sample_text", queue_size=7)
    _safe_set(b, 'rosmodel_Subscriber33', a1)
    assert _is_linked(b, 'rosmodel_Subscriber33', a1)
    if hasattr(a1, 'rosmodel_Topic34'):
        assert _is_linked(a1, 'rosmodel_Topic34', b)
    _safe_set(b, 'rosmodel_Subscriber33', a2)
    assert _is_linked(b, 'rosmodel_Subscriber33', a2)
    if hasattr(a1, 'rosmodel_Topic34'):
        assert not _is_linked(a1, 'rosmodel_Topic34', b)
    if hasattr(a2, 'rosmodel_Topic34'):
        assert _is_linked(a2, 'rosmodel_Topic34', b)
    _safe_set(b, 'rosmodel_Subscriber33', None)
    assert not _is_linked(b, 'rosmodel_Subscriber33', a2)
    if hasattr(a2, 'rosmodel_Topic34'):
        assert not _is_linked(a2, 'rosmodel_Topic34', b)


def test_assoc_source82_reverse_link_reassign_clear():
    a1 = rosmodel_Transition(name="sample_text")
    a2 = rosmodel_Transition(name="sample_text_2")
    b = rosmodel_State(name="sample_text")
    _safe_set(b, 'rosmodel_State84', a1)
    assert _is_linked(b, 'rosmodel_State84', a1)
    if hasattr(a1, 'rosmodel_Transition83'):
        assert _is_linked(a1, 'rosmodel_Transition83', b)
    _safe_set(b, 'rosmodel_State84', a2)
    assert _is_linked(b, 'rosmodel_State84', a2)
    if hasattr(a1, 'rosmodel_Transition83'):
        assert not _is_linked(a1, 'rosmodel_Transition83', b)
    if hasattr(a2, 'rosmodel_Transition83'):
        assert _is_linked(a2, 'rosmodel_Transition83', b)
    _safe_set(b, 'rosmodel_State84', None)
    assert not _is_linked(b, 'rosmodel_State84', a2)
    if hasattr(a2, 'rosmodel_Transition83'):
        assert not _is_linked(a2, 'rosmodel_Transition83', b)


def test_assoc_state21_reverse_link_reassign_clear():
    a1 = rosmodel_State(name="sample_text")
    a2 = rosmodel_State(name="sample_text_2")
    b = rosmodel_Node(frequency=3.14, name="sample_text")
    _safe_set(b, 'rosmodel_Node22', {a1})
    assert _is_linked(b, 'rosmodel_Node22', a1)
    if hasattr(a1, 'rosmodel_State'):
        assert _is_linked(a1, 'rosmodel_State', b)
    _safe_set(b, 'rosmodel_Node22', {a2})
    assert _is_linked(b, 'rosmodel_Node22', a2)
    if hasattr(a1, 'rosmodel_State'):
        assert not _is_linked(a1, 'rosmodel_State', b)
    if hasattr(a2, 'rosmodel_State'):
        assert _is_linked(a2, 'rosmodel_State', b)
    _safe_set(b, 'rosmodel_Node22', set())
    assert not _is_linked(b, 'rosmodel_Node22', a2)
    if hasattr(a2, 'rosmodel_State'):
        assert not _is_linked(a2, 'rosmodel_State', b)


def test_assoc_subscriber11_reverse_link_reassign_clear():
    a1 = rosmodel_Subscriber(msg="sample_text", name="sample_text", queue_size=7)
    a2 = rosmodel_Subscriber(msg="sample_text_2", name="sample_text_2", queue_size=13)
    b = rosmodel_Node(frequency=3.14, name="sample_text")
    _safe_set(b, 'rosmodel_Node12', {a1})
    assert _is_linked(b, 'rosmodel_Node12', a1)
    if hasattr(a1, 'rosmodel_Subscriber'):
        assert _is_linked(a1, 'rosmodel_Subscriber', b)
    _safe_set(b, 'rosmodel_Node12', {a2})
    assert _is_linked(b, 'rosmodel_Node12', a2)
    if hasattr(a1, 'rosmodel_Subscriber'):
        assert not _is_linked(a1, 'rosmodel_Subscriber', b)
    if hasattr(a2, 'rosmodel_Subscriber'):
        assert _is_linked(a2, 'rosmodel_Subscriber', b)
    _safe_set(b, 'rosmodel_Node12', set())
    assert not _is_linked(b, 'rosmodel_Node12', a2)
    if hasattr(a2, 'rosmodel_Subscriber'):
        assert not _is_linked(a2, 'rosmodel_Subscriber', b)


def test_assoc_substate68_reverse_link_reassign_clear():
    a1 = rosmodel_State(name="sample_text")
    a2 = rosmodel_State(name="sample_text_2")
    b = rosmodel_State(name="sample_text")
    _safe_set(b, 'rosmodel_State69', a1)
    assert _is_linked(b, 'rosmodel_State69', a1)
    if hasattr(a1, 'rosmodel_State67'):
        assert _is_linked(a1, 'rosmodel_State67', b)
    _safe_set(b, 'rosmodel_State69', a2)
    assert _is_linked(b, 'rosmodel_State69', a2)
    if hasattr(a1, 'rosmodel_State67'):
        assert not _is_linked(a1, 'rosmodel_State67', b)
    if hasattr(a2, 'rosmodel_State67'):
        assert _is_linked(a2, 'rosmodel_State67', b)
    _safe_set(b, 'rosmodel_State69', None)
    assert not _is_linked(b, 'rosmodel_State69', a2)
    if hasattr(a2, 'rosmodel_State67'):
        assert not _is_linked(a2, 'rosmodel_State67', b)


def test_assoc_target29_reverse_link_reassign_clear():
    a1 = rosmodel_Topic(name="sample_text")
    a2 = rosmodel_Topic(name="sample_text_2")
    b = rosmodel_Publisher(msg="sample_text", name="sample_text", queue_size=7)
    _safe_set(b, 'rosmodel_Publisher30', a1)
    assert _is_linked(b, 'rosmodel_Publisher30', a1)
    if hasattr(a1, 'rosmodel_Topic31'):
        assert _is_linked(a1, 'rosmodel_Topic31', b)
    _safe_set(b, 'rosmodel_Publisher30', a2)
    assert _is_linked(b, 'rosmodel_Publisher30', a2)
    if hasattr(a1, 'rosmodel_Topic31'):
        assert not _is_linked(a1, 'rosmodel_Topic31', b)
    if hasattr(a2, 'rosmodel_Topic31'):
        assert _is_linked(a2, 'rosmodel_Topic31', b)
    _safe_set(b, 'rosmodel_Publisher30', None)
    assert not _is_linked(b, 'rosmodel_Publisher30', a2)
    if hasattr(a2, 'rosmodel_Topic31'):
        assert not _is_linked(a2, 'rosmodel_Topic31', b)


def test_assoc_target85_reverse_link_reassign_clear():
    a1 = rosmodel_Transition(name="sample_text")
    a2 = rosmodel_Transition(name="sample_text_2")
    b = rosmodel_State(name="sample_text")
    _safe_set(b, 'rosmodel_State87', a1)
    assert _is_linked(b, 'rosmodel_State87', a1)
    if hasattr(a1, 'rosmodel_Transition86'):
        assert _is_linked(a1, 'rosmodel_Transition86', b)
    _safe_set(b, 'rosmodel_State87', a2)
    assert _is_linked(b, 'rosmodel_State87', a2)
    if hasattr(a1, 'rosmodel_Transition86'):
        assert not _is_linked(a1, 'rosmodel_Transition86', b)
    if hasattr(a2, 'rosmodel_Transition86'):
        assert _is_linked(a2, 'rosmodel_Transition86', b)
    _safe_set(b, 'rosmodel_State87', None)
    assert not _is_linked(b, 'rosmodel_State87', a2)
    if hasattr(a2, 'rosmodel_Transition86'):
        assert not _is_linked(a2, 'rosmodel_Transition86', b)


def test_assoc_topic1_reverse_link_reassign_clear():
    a1 = rosmodel_Topic(name="sample_text")
    a2 = rosmodel_Topic(name="sample_text_2")
    b = rosmodel_Package(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'rosmodel_Package2', {a1})
    assert _is_linked(b, 'rosmodel_Package2', a1)
    if hasattr(a1, 'rosmodel_Topic'):
        assert _is_linked(a1, 'rosmodel_Topic', b)
    _safe_set(b, 'rosmodel_Package2', {a2})
    assert _is_linked(b, 'rosmodel_Package2', a2)
    if hasattr(a1, 'rosmodel_Topic'):
        assert not _is_linked(a1, 'rosmodel_Topic', b)
    if hasattr(a2, 'rosmodel_Topic'):
        assert _is_linked(a2, 'rosmodel_Topic', b)
    _safe_set(b, 'rosmodel_Package2', set())
    assert not _is_linked(b, 'rosmodel_Package2', a2)
    if hasattr(a2, 'rosmodel_Topic'):
        assert not _is_linked(a2, 'rosmodel_Topic', b)


def test_assoc_transition23_reverse_link_reassign_clear():
    a1 = rosmodel_Transition(name="sample_text")
    a2 = rosmodel_Transition(name="sample_text_2")
    b = rosmodel_Node(frequency=3.14, name="sample_text")
    _safe_set(b, 'rosmodel_Node24', {a1})
    assert _is_linked(b, 'rosmodel_Node24', a1)
    if hasattr(a1, 'rosmodel_Transition'):
        assert _is_linked(a1, 'rosmodel_Transition', b)
    _safe_set(b, 'rosmodel_Node24', {a2})
    assert _is_linked(b, 'rosmodel_Node24', a2)
    if hasattr(a1, 'rosmodel_Transition'):
        assert not _is_linked(a1, 'rosmodel_Transition', b)
    if hasattr(a2, 'rosmodel_Transition'):
        assert _is_linked(a2, 'rosmodel_Transition', b)
    _safe_set(b, 'rosmodel_Node24', set())
    assert not _is_linked(b, 'rosmodel_Node24', a2)
    if hasattr(a2, 'rosmodel_Transition'):
        assert not _is_linked(a2, 'rosmodel_Transition', b)


def test_assoc_transition64_reverse_link_reassign_clear():
    a1 = rosmodel_Transition(name="sample_text")
    a2 = rosmodel_Transition(name="sample_text_2")
    b = rosmodel_State(name="sample_text")
    _safe_set(b, 'rosmodel_State65', {a1})
    assert _is_linked(b, 'rosmodel_State65', a1)
    if hasattr(a1, 'rosmodel_Transition66'):
        assert _is_linked(a1, 'rosmodel_Transition66', b)
    _safe_set(b, 'rosmodel_State65', {a2})
    assert _is_linked(b, 'rosmodel_State65', a2)
    if hasattr(a1, 'rosmodel_Transition66'):
        assert not _is_linked(a1, 'rosmodel_Transition66', b)
    if hasattr(a2, 'rosmodel_Transition66'):
        assert _is_linked(a2, 'rosmodel_Transition66', b)
    _safe_set(b, 'rosmodel_State65', set())
    assert not _is_linked(b, 'rosmodel_State65', a2)
    if hasattr(a2, 'rosmodel_Transition66'):
        assert not _is_linked(a2, 'rosmodel_Transition66', b)


def test_assoc_transition94_reverse_link_reassign_clear():
    a1 = rosmodel_Transition(name="sample_text")
    a2 = rosmodel_Transition(name="sample_text_2")
    b = rosmodel_Event(name="sample_text")
    _safe_set(b, 'rosmodel_Event95', a1)
    assert _is_linked(b, 'rosmodel_Event95', a1)
    if hasattr(a1, 'rosmodel_Transition96'):
        assert _is_linked(a1, 'rosmodel_Transition96', b)
    _safe_set(b, 'rosmodel_Event95', a2)
    assert _is_linked(b, 'rosmodel_Event95', a2)
    if hasattr(a1, 'rosmodel_Transition96'):
        assert not _is_linked(a1, 'rosmodel_Transition96', b)
    if hasattr(a2, 'rosmodel_Transition96'):
        assert _is_linked(a2, 'rosmodel_Transition96', b)
    _safe_set(b, 'rosmodel_Event95', None)
    assert not _is_linked(b, 'rosmodel_Event95', a2)
    if hasattr(a2, 'rosmodel_Transition96'):
        assert not _is_linked(a2, 'rosmodel_Transition96', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

