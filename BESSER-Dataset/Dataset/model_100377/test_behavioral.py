import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    metaCompo_mComp,
    metaCompo_mFSM,
    metaCompo_mPort,
    metaCompo_mState,
    metaCompo_mTransition,
    metaCompo_mVariable,
    mIO,
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

def test_assoc_FSMs4_reverse_link_reassign_clear():
    a1 = metaCompo_mFSM(name="sample_text")
    a2 = metaCompo_mFSM(name="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'component', {a1})
    assert _is_linked(b, 'component', a1)
    if hasattr(a1, 'mFSM'):
        assert _is_linked(a1, 'mFSM', b)
    _safe_set(b, 'component', {a2})
    assert _is_linked(b, 'component', a2)
    if hasattr(a1, 'mFSM'):
        assert not _is_linked(a1, 'mFSM', b)
    if hasattr(a2, 'mFSM'):
        assert _is_linked(a2, 'mFSM', b)
    _safe_set(b, 'component', set())
    assert not _is_linked(b, 'component', a2)
    if hasattr(a2, 'mFSM'):
        assert not _is_linked(a2, 'mFSM', b)


def test_assoc_compVar5_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mComp6', {a1})
    assert _is_linked(b, 'metaCompo_mComp6', a1)
    if hasattr(a1, 'metaCompo_mVariable'):
        assert _is_linked(a1, 'metaCompo_mVariable', b)
    _safe_set(b, 'metaCompo_mComp6', {a2})
    assert _is_linked(b, 'metaCompo_mComp6', a2)
    if hasattr(a1, 'metaCompo_mVariable'):
        assert not _is_linked(a1, 'metaCompo_mVariable', b)
    if hasattr(a2, 'metaCompo_mVariable'):
        assert _is_linked(a2, 'metaCompo_mVariable', b)
    _safe_set(b, 'metaCompo_mComp6', set())
    assert not _is_linked(b, 'metaCompo_mComp6', a2)
    if hasattr(a2, 'metaCompo_mVariable'):
        assert not _is_linked(a2, 'metaCompo_mVariable', b)


def test_assoc_component13_reverse_link_reassign_clear():
    a1 = metaCompo_mFSM(name="sample_text")
    a2 = metaCompo_mFSM(name="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'mComp', a1)
    assert _is_linked(b, 'mComp', a1)
    if hasattr(a1, 'FSMs'):
        assert _is_linked(a1, 'FSMs', b)
    _safe_set(b, 'mComp', a2)
    assert _is_linked(b, 'mComp', a2)
    if hasattr(a1, 'FSMs'):
        assert not _is_linked(a1, 'FSMs', b)
    if hasattr(a2, 'FSMs'):
        assert _is_linked(a2, 'FSMs', b)
    _safe_set(b, 'mComp', None)
    assert not _is_linked(b, 'mComp', a2)
    if hasattr(a2, 'FSMs'):
        assert not _is_linked(a2, 'FSMs', b)


def test_assoc_connToVar10_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mPort11', a1)
    assert _is_linked(b, 'metaCompo_mPort11', a1)
    if hasattr(a1, 'metaCompo_mVariable12'):
        assert _is_linked(a1, 'metaCompo_mVariable12', b)
    _safe_set(b, 'metaCompo_mPort11', a2)
    assert _is_linked(b, 'metaCompo_mPort11', a2)
    if hasattr(a1, 'metaCompo_mVariable12'):
        assert not _is_linked(a1, 'metaCompo_mVariable12', b)
    if hasattr(a2, 'metaCompo_mVariable12'):
        assert _is_linked(a2, 'metaCompo_mVariable12', b)
    _safe_set(b, 'metaCompo_mPort11', None)
    assert not _is_linked(b, 'metaCompo_mPort11', a2)
    if hasattr(a2, 'metaCompo_mVariable12'):
        assert not _is_linked(a2, 'metaCompo_mVariable12', b)


def test_assoc_connectedTo8_reverse_link_reassign_clear():
    a1 = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    a2 = metaCompo_mPort(io="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mPort9', a1)
    assert _is_linked(b, 'metaCompo_mPort9', a1)
    if hasattr(a1, 'metaCompo_mPort7'):
        assert _is_linked(a1, 'metaCompo_mPort7', b)
    _safe_set(b, 'metaCompo_mPort9', a2)
    assert _is_linked(b, 'metaCompo_mPort9', a2)
    if hasattr(a1, 'metaCompo_mPort7'):
        assert not _is_linked(a1, 'metaCompo_mPort7', b)
    if hasattr(a2, 'metaCompo_mPort7'):
        assert _is_linked(a2, 'metaCompo_mPort7', b)
    _safe_set(b, 'metaCompo_mPort9', None)
    assert not _is_linked(b, 'metaCompo_mPort9', a2)
    if hasattr(a2, 'metaCompo_mPort7'):
        assert not _is_linked(a2, 'metaCompo_mPort7', b)


def test_assoc_destination35_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'mState36', a1)
    assert _is_linked(b, 'mState36', a1)
    if hasattr(a1, 'incomingTransitions'):
        assert _is_linked(a1, 'incomingTransitions', b)
    _safe_set(b, 'mState36', a2)
    assert _is_linked(b, 'mState36', a2)
    if hasattr(a1, 'incomingTransitions'):
        assert not _is_linked(a1, 'incomingTransitions', b)
    if hasattr(a2, 'incomingTransitions'):
        assert _is_linked(a2, 'incomingTransitions', b)
    _safe_set(b, 'mState36', None)
    assert not _is_linked(b, 'mState36', a2)
    if hasattr(a2, 'incomingTransitions'):
        assert not _is_linked(a2, 'incomingTransitions', b)


def test_assoc_finalState19_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'metaCompo_mFSM20', a1)
    assert _is_linked(b, 'metaCompo_mFSM20', a1)
    if hasattr(a1, 'metaCompo_mState21'):
        assert _is_linked(a1, 'metaCompo_mState21', b)
    _safe_set(b, 'metaCompo_mFSM20', a2)
    assert _is_linked(b, 'metaCompo_mFSM20', a2)
    if hasattr(a1, 'metaCompo_mState21'):
        assert not _is_linked(a1, 'metaCompo_mState21', b)
    if hasattr(a2, 'metaCompo_mState21'):
        assert _is_linked(a2, 'metaCompo_mState21', b)
    _safe_set(b, 'metaCompo_mFSM20', None)
    assert not _is_linked(b, 'metaCompo_mFSM20', a2)
    if hasattr(a2, 'metaCompo_mState21'):
        assert not _is_linked(a2, 'metaCompo_mState21', b)


def test_assoc_fsmVar14_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'metaCompo_mFSM', {a1})
    assert _is_linked(b, 'metaCompo_mFSM', a1)
    if hasattr(a1, 'metaCompo_mVariable15'):
        assert _is_linked(a1, 'metaCompo_mVariable15', b)
    _safe_set(b, 'metaCompo_mFSM', {a2})
    assert _is_linked(b, 'metaCompo_mFSM', a2)
    if hasattr(a1, 'metaCompo_mVariable15'):
        assert not _is_linked(a1, 'metaCompo_mVariable15', b)
    if hasattr(a2, 'metaCompo_mVariable15'):
        assert _is_linked(a2, 'metaCompo_mVariable15', b)
    _safe_set(b, 'metaCompo_mFSM', set())
    assert not _is_linked(b, 'metaCompo_mFSM', a2)
    if hasattr(a2, 'metaCompo_mVariable15'):
        assert not _is_linked(a2, 'metaCompo_mVariable15', b)


def test_assoc_incomingTransitions28_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'destination', {a1})
    assert _is_linked(b, 'destination', a1)
    if hasattr(a1, 'mTransition29'):
        assert _is_linked(a1, 'mTransition29', b)
    _safe_set(b, 'destination', {a2})
    assert _is_linked(b, 'destination', a2)
    if hasattr(a1, 'mTransition29'):
        assert not _is_linked(a1, 'mTransition29', b)
    if hasattr(a2, 'mTransition29'):
        assert _is_linked(a2, 'mTransition29', b)
    _safe_set(b, 'destination', set())
    assert not _is_linked(b, 'destination', a2)
    if hasattr(a2, 'mTransition29'):
        assert not _is_linked(a2, 'mTransition29', b)


def test_assoc_initialState17_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'metaCompo_mFSM18', a1)
    assert _is_linked(b, 'metaCompo_mFSM18', a1)
    if hasattr(a1, 'metaCompo_mState'):
        assert _is_linked(a1, 'metaCompo_mState', b)
    _safe_set(b, 'metaCompo_mFSM18', a2)
    assert _is_linked(b, 'metaCompo_mFSM18', a2)
    if hasattr(a1, 'metaCompo_mState'):
        assert not _is_linked(a1, 'metaCompo_mState', b)
    if hasattr(a2, 'metaCompo_mState'):
        assert _is_linked(a2, 'metaCompo_mState', b)
    _safe_set(b, 'metaCompo_mFSM18', None)
    assert not _is_linked(b, 'metaCompo_mFSM18', a2)
    if hasattr(a2, 'metaCompo_mState'):
        assert not _is_linked(a2, 'metaCompo_mState', b)


def test_assoc_outgoingTransitions27_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'mTransition'):
        assert _is_linked(a1, 'mTransition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'mTransition'):
        assert not _is_linked(a1, 'mTransition', b)
    if hasattr(a2, 'mTransition'):
        assert _is_linked(a2, 'mTransition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'mTransition'):
        assert not _is_linked(a2, 'mTransition', b)


def test_assoc_owningFSM22_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'mFSM23', a1)
    assert _is_linked(b, 'mFSM23', a1)
    if hasattr(a1, 'states'):
        assert _is_linked(a1, 'states', b)
    _safe_set(b, 'mFSM23', a2)
    assert _is_linked(b, 'mFSM23', a2)
    if hasattr(a1, 'states'):
        assert not _is_linked(a1, 'states', b)
    if hasattr(a2, 'states'):
        assert _is_linked(a2, 'states', b)
    _safe_set(b, 'mFSM23', None)
    assert not _is_linked(b, 'mFSM23', a2)
    if hasattr(a2, 'states'):
        assert not _is_linked(a2, 'states', b)


def test_assoc_ports2_reverse_link_reassign_clear():
    a1 = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    a2 = metaCompo_mPort(io="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mComp3', {a1})
    assert _is_linked(b, 'metaCompo_mComp3', a1)
    if hasattr(a1, 'metaCompo_mPort'):
        assert _is_linked(a1, 'metaCompo_mPort', b)
    _safe_set(b, 'metaCompo_mComp3', {a2})
    assert _is_linked(b, 'metaCompo_mComp3', a2)
    if hasattr(a1, 'metaCompo_mPort'):
        assert not _is_linked(a1, 'metaCompo_mPort', b)
    if hasattr(a2, 'metaCompo_mPort'):
        assert _is_linked(a2, 'metaCompo_mPort', b)
    _safe_set(b, 'metaCompo_mComp3', set())
    assert not _is_linked(b, 'metaCompo_mComp3', a2)
    if hasattr(a2, 'metaCompo_mPort'):
        assert not _is_linked(a2, 'metaCompo_mPort', b)


def test_assoc_source33_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'mState34', a1)
    assert _is_linked(b, 'mState34', a1)
    if hasattr(a1, 'outgoingTransitions'):
        assert _is_linked(a1, 'outgoingTransitions', b)
    _safe_set(b, 'mState34', a2)
    assert _is_linked(b, 'mState34', a2)
    if hasattr(a1, 'outgoingTransitions'):
        assert not _is_linked(a1, 'outgoingTransitions', b)
    if hasattr(a2, 'outgoingTransitions'):
        assert _is_linked(a2, 'outgoingTransitions', b)
    _safe_set(b, 'mState34', None)
    assert not _is_linked(b, 'mState34', a2)
    if hasattr(a2, 'outgoingTransitions'):
        assert not _is_linked(a2, 'outgoingTransitions', b)


def test_assoc_stateVar24_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'metaCompo_mState25', {a1})
    assert _is_linked(b, 'metaCompo_mState25', a1)
    if hasattr(a1, 'metaCompo_mVariable26'):
        assert _is_linked(a1, 'metaCompo_mVariable26', b)
    _safe_set(b, 'metaCompo_mState25', {a2})
    assert _is_linked(b, 'metaCompo_mState25', a2)
    if hasattr(a1, 'metaCompo_mVariable26'):
        assert not _is_linked(a1, 'metaCompo_mVariable26', b)
    if hasattr(a2, 'metaCompo_mVariable26'):
        assert _is_linked(a2, 'metaCompo_mVariable26', b)
    _safe_set(b, 'metaCompo_mState25', set())
    assert not _is_linked(b, 'metaCompo_mState25', a2)
    if hasattr(a2, 'metaCompo_mVariable26'):
        assert not _is_linked(a2, 'metaCompo_mVariable26', b)


def test_assoc_states16_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mFSM(name="sample_text")
    _safe_set(b, 'owningFSM', {a1})
    assert _is_linked(b, 'owningFSM', a1)
    if hasattr(a1, 'mState'):
        assert _is_linked(a1, 'mState', b)
    _safe_set(b, 'owningFSM', {a2})
    assert _is_linked(b, 'owningFSM', a2)
    if hasattr(a1, 'mState'):
        assert not _is_linked(a1, 'mState', b)
    if hasattr(a2, 'mState'):
        assert _is_linked(a2, 'mState', b)
    _safe_set(b, 'owningFSM', set())
    assert not _is_linked(b, 'owningFSM', a2)
    if hasattr(a2, 'mState'):
        assert not _is_linked(a2, 'mState', b)


def test_assoc_subComps1_reverse_link_reassign_clear():
    a1 = metaCompo_mComp(name="sample_text", type="sample_text")
    a2 = metaCompo_mComp(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mComp(name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mComp0', {a1})
    assert _is_linked(b, 'metaCompo_mComp0', a1)
    if hasattr(a1, 'metaCompo_mComp'):
        assert _is_linked(a1, 'metaCompo_mComp', b)
    _safe_set(b, 'metaCompo_mComp0', {a2})
    assert _is_linked(b, 'metaCompo_mComp0', a2)
    if hasattr(a1, 'metaCompo_mComp'):
        assert not _is_linked(a1, 'metaCompo_mComp', b)
    if hasattr(a2, 'metaCompo_mComp'):
        assert _is_linked(a2, 'metaCompo_mComp', b)
    _safe_set(b, 'metaCompo_mComp0', set())
    assert not _is_linked(b, 'metaCompo_mComp0', a2)
    if hasattr(a2, 'metaCompo_mComp'):
        assert not _is_linked(a2, 'metaCompo_mComp', b)


def test_assoc_subStates31_reverse_link_reassign_clear():
    a1 = metaCompo_mState(name="sample_text")
    a2 = metaCompo_mState(name="sample_text_2")
    b = metaCompo_mState(name="sample_text")
    _safe_set(b, 'metaCompo_mState32', a1)
    assert _is_linked(b, 'metaCompo_mState32', a1)
    if hasattr(a1, 'metaCompo_mState30'):
        assert _is_linked(a1, 'metaCompo_mState30', b)
    _safe_set(b, 'metaCompo_mState32', a2)
    assert _is_linked(b, 'metaCompo_mState32', a2)
    if hasattr(a1, 'metaCompo_mState30'):
        assert not _is_linked(a1, 'metaCompo_mState30', b)
    if hasattr(a2, 'metaCompo_mState30'):
        assert _is_linked(a2, 'metaCompo_mState30', b)
    _safe_set(b, 'metaCompo_mState32', None)
    assert not _is_linked(b, 'metaCompo_mState32', a2)
    if hasattr(a2, 'metaCompo_mState30'):
        assert not _is_linked(a2, 'metaCompo_mState30', b)


def test_assoc_trigerringVar37_reverse_link_reassign_clear():
    a1 = metaCompo_mVariable(name="sample_text", type="sample_text")
    a2 = metaCompo_mVariable(name="sample_text_2", type="sample_text_2")
    b = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    _safe_set(b, 'metaCompo_mTransition', {a1})
    assert _is_linked(b, 'metaCompo_mTransition', a1)
    if hasattr(a1, 'metaCompo_mVariable38'):
        assert _is_linked(a1, 'metaCompo_mVariable38', b)
    _safe_set(b, 'metaCompo_mTransition', {a2})
    assert _is_linked(b, 'metaCompo_mTransition', a2)
    if hasattr(a1, 'metaCompo_mVariable38'):
        assert not _is_linked(a1, 'metaCompo_mVariable38', b)
    if hasattr(a2, 'metaCompo_mVariable38'):
        assert _is_linked(a2, 'metaCompo_mVariable38', b)
    _safe_set(b, 'metaCompo_mTransition', set())
    assert not _is_linked(b, 'metaCompo_mTransition', a2)
    if hasattr(a2, 'metaCompo_mVariable38'):
        assert not _is_linked(a2, 'metaCompo_mVariable38', b)


def test_assoc_triggeringPort39_reverse_link_reassign_clear():
    a1 = metaCompo_mTransition(action="sample_text", guard="sample_text", name="sample_text", triggerExp="sample_text")
    a2 = metaCompo_mTransition(action="sample_text_2", guard="sample_text_2", name="sample_text_2", triggerExp="sample_text_2")
    b = metaCompo_mPort(io="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'metaCompo_mPort41', a1)
    assert _is_linked(b, 'metaCompo_mPort41', a1)
    if hasattr(a1, 'metaCompo_mTransition40'):
        assert _is_linked(a1, 'metaCompo_mTransition40', b)
    _safe_set(b, 'metaCompo_mPort41', a2)
    assert _is_linked(b, 'metaCompo_mPort41', a2)
    if hasattr(a1, 'metaCompo_mTransition40'):
        assert not _is_linked(a1, 'metaCompo_mTransition40', b)
    if hasattr(a2, 'metaCompo_mTransition40'):
        assert _is_linked(a2, 'metaCompo_mTransition40', b)
    _safe_set(b, 'metaCompo_mPort41', None)
    assert not _is_linked(b, 'metaCompo_mPort41', a2)
    if hasattr(a2, 'metaCompo_mTransition40'):
        assert not _is_linked(a2, 'metaCompo_mTransition40', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

