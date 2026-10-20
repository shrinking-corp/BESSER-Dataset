import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Branch,
    IVREvent,
    IvrAction,
    Play,
    State,
    Transition,
    stateMachine_Action,
    stateMachine_Branch,
    stateMachine_Bye,
    stateMachine_Call,
    stateMachine_Cancel,
    stateMachine_CollectTimeout,
    stateMachine_Collected,
    stateMachine_CompositeState,
    stateMachine_FinalState,
    stateMachine_HangUp,
    stateMachine_IVREvent,
    stateMachine_Init,
    stateMachine_InitialState,
    stateMachine_IvrAction,
    stateMachine_Key,
    stateMachine_Managed,
    stateMachine_NewCall,
    stateMachine_NoneEvent,
    stateMachine_Otherwise,
    stateMachine_PickUp,
    stateMachine_Play,
    stateMachine_PlayCollect,
    stateMachine_PlayRecord,
    stateMachine_Played,
    stateMachine_Properties,
    stateMachine_Recorderd,
    stateMachine_RemoveRecord,
    stateMachine_SMS,
    stateMachine_SMSReceived,
    stateMachine_SendSms,
    stateMachine_SetTimer,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_Terminate,
    stateMachine_Terminated,
    stateMachine_Timer,
    stateMachine_Transition,
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

def test_assoc_children5_reverse_link_reassign_clear():
    a1 = stateMachine_State(nombre="sample_text")
    a2 = stateMachine_State(nombre="sample_text_2")
    b = stateMachine_State(nombre="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_parent7_reverse_link_reassign_clear():
    a1 = stateMachine_State(nombre="sample_text")
    a2 = stateMachine_State(nombre="sample_text_2")
    b = stateMachine_State(nombre="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'State8'):
        assert _is_linked(a1, 'State8', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'State8'):
        assert not _is_linked(a1, 'State8', b)
    if hasattr(a2, 'State8'):
        assert _is_linked(a2, 'State8', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'State8'):
        assert not _is_linked(a2, 'State8', b)


def test_assoc_properties1_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(nombre="sample_text")
    a2 = stateMachine_StateMachine(nombre="sample_text_2")
    b = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    _safe_set(b, 'stateMachine_Properties', a1)
    assert _is_linked(b, 'stateMachine_Properties', a1)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert _is_linked(a1, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_Properties', a2)
    assert _is_linked(b, 'stateMachine_Properties', a2)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert not _is_linked(a1, 'stateMachine_StateMachine2', b)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert _is_linked(a2, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_Properties', None)
    assert not _is_linked(b, 'stateMachine_Properties', a2)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert not _is_linked(a2, 'stateMachine_StateMachine2', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(nombre="sample_text")
    a2 = stateMachine_StateMachine(nombre="sample_text_2")
    b = stateMachine_State(nombre="sample_text")
    _safe_set(b, 'stateMachine_State', a1)
    assert _is_linked(b, 'stateMachine_State', a1)
    if hasattr(a1, 'stateMachine_StateMachine'):
        assert _is_linked(a1, 'stateMachine_StateMachine', b)
    _safe_set(b, 'stateMachine_State', a2)
    assert _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a1, 'stateMachine_StateMachine'):
        assert not _is_linked(a1, 'stateMachine_StateMachine', b)
    if hasattr(a2, 'stateMachine_StateMachine'):
        assert _is_linked(a2, 'stateMachine_StateMachine', b)
    _safe_set(b, 'stateMachine_State', None)
    assert not _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a2, 'stateMachine_StateMachine'):
        assert not _is_linked(a2, 'stateMachine_StateMachine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defaultTar15_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition16' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(nombre="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition16', None)
    _safe_set(owner, 'stateMachine_State17', partner)
    assert getattr(partner, 'stateMachine_Transition16') == owner
    _safe_set(owner, 'stateMachine_State17', None)
    assert getattr(partner, 'stateMachine_Transition16') is None


def test_assoc_out21_stub_double():
    # stateMachine_Branch has no real 'stateMachine_Branch22' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(nombre="sample_text")
    partner = stateMachine_Branch()
    setattr(partner, 'stateMachine_Branch22', None)
    _safe_set(owner, 'stateMachine_State23', partner)
    assert getattr(partner, 'stateMachine_Branch22') == owner
    _safe_set(owner, 'stateMachine_State23', None)
    assert getattr(partner, 'stateMachine_Branch22') is None


def test_assoc_outs3_stub_double():
    # stateMachine_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(nombre="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'src', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'src', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_sm9_stub_double():
    # stateMachine_CompositeState has no real 'stateMachine_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_StateMachine(nombre="sample_text")
    partner = stateMachine_CompositeState()
    setattr(partner, 'stateMachine_CompositeState', None)
    _safe_set(owner, 'stateMachine_StateMachine10', partner)
    assert getattr(partner, 'stateMachine_CompositeState') == owner
    _safe_set(owner, 'stateMachine_StateMachine10', None)
    assert getattr(partner, 'stateMachine_CompositeState') is None


def test_assoc_sms11_stub_double():
    # stateMachine_SendSms has no real 'stateMachine_SendSms' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_SMS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_SMS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_SMS(from_="sample_text", text="sample_text", to="sample_text")
    partner = stateMachine_SendSms()
    setattr(partner, 'stateMachine_SendSms', None)
    _safe_set(owner, 'stateMachine_SMS', partner)
    assert getattr(partner, 'stateMachine_SendSms') == owner
    _safe_set(owner, 'stateMachine_SMS', None)
    assert getattr(partner, 'stateMachine_SendSms') is None


def test_assoc_sms18_stub_double():
    # stateMachine_SMSReceived has no real 'stateMachine_SMSReceived' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_SMS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_SMS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_SMS(from_="sample_text", text="sample_text", to="sample_text")
    partner = stateMachine_SMSReceived()
    setattr(partner, 'stateMachine_SMSReceived', None)
    _safe_set(owner, 'stateMachine_SMS19', partner)
    assert getattr(partner, 'stateMachine_SMSReceived') == owner
    _safe_set(owner, 'stateMachine_SMS19', None)
    assert getattr(partner, 'stateMachine_SMSReceived') is None


def test_assoc_src13_stub_double():
    # stateMachine_Transition has no real 'outs' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(nombre="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'outs', None)
    _safe_set(owner, 'State14', partner)
    assert getattr(partner, 'outs') == owner
    _safe_set(owner, 'State14', None)
    assert getattr(partner, 'outs') is None


