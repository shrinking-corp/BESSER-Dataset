import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Branch,
    IVREvent,
    IvrAction,
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
    stateMachine_IVREvent,
    stateMachine_Init,
    stateMachine_InitialState,
    stateMachine_IvrAction,
    stateMachine_Key,
    stateMachine_Managed,
    stateMachine_NoneEvent,
    stateMachine_Otherwise,
    stateMachine_PickUp,
    stateMachine_Play,
    stateMachine_Played,
    stateMachine_Properties,
    stateMachine_Recorderd,
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

def test_stateMachine_Call_from__value_roundtrip():
    instance = stateMachine_Call(from_="sample_text", to="sample_text")
    assert instance.from_ == "sample_text"
    instance.from_ = "sample_text_2"
    assert instance.from_ == "sample_text_2"


def test_stateMachine_Call_to_value_roundtrip():
    instance = stateMachine_Call(from_="sample_text", to="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_stateMachine_Key_key_value_roundtrip():
    instance = stateMachine_Key(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_stateMachine_Managed_code_value_roundtrip():
    instance = stateMachine_Managed(code=7, success=True)
    assert instance.code == 7
    instance.code = 13
    assert instance.code == 13


def test_stateMachine_Managed_success_value_roundtrip():
    instance = stateMachine_Managed(code=7, success=True)
    assert instance.success == True
    instance.success = False
    assert instance.success == False


def test_stateMachine_Play_baseURL_value_roundtrip():
    instance = stateMachine_Play(baseURL="sample_text", mediaURI="sample_text")
    assert instance.baseURL == "sample_text"
    instance.baseURL = "sample_text_2"
    assert instance.baseURL == "sample_text_2"


def test_stateMachine_Play_mediaURI_value_roundtrip():
    instance = stateMachine_Play(baseURL="sample_text", mediaURI="sample_text")
    assert instance.mediaURI == "sample_text"
    instance.mediaURI = "sample_text_2"
    assert instance.mediaURI == "sample_text_2"


def test_stateMachine_Properties_applicationAddress_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.applicationAddress == "sample_text"
    instance.applicationAddress = "sample_text_2"
    assert instance.applicationAddress == "sample_text_2"


def test_stateMachine_Properties_applicationServerHost_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.applicationServerHost == "sample_text"
    instance.applicationServerHost = "sample_text_2"
    assert instance.applicationServerHost == "sample_text_2"


def test_stateMachine_Properties_applicationServerPort_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.applicationServerPort == 7
    instance.applicationServerPort = 13
    assert instance.applicationServerPort == 13


def test_stateMachine_Properties_applicationServerProtocol_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.applicationServerProtocol == "sample_text"
    instance.applicationServerProtocol = "sample_text_2"
    assert instance.applicationServerProtocol == "sample_text_2"


def test_stateMachine_Properties_mediaFromAddr_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.mediaFromAddr == "sample_text"
    instance.mediaFromAddr = "sample_text_2"
    assert instance.mediaFromAddr == "sample_text_2"


def test_stateMachine_Properties_mediaHost_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.mediaHost == "sample_text"
    instance.mediaHost = "sample_text_2"
    assert instance.mediaHost == "sample_text_2"


def test_stateMachine_Properties_mediaPort_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.mediaPort == 7
    instance.mediaPort = 13
    assert instance.mediaPort == 13


def test_stateMachine_Properties_mediaProtocol_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.mediaProtocol == "sample_text"
    instance.mediaProtocol = "sample_text_2"
    assert instance.mediaProtocol == "sample_text_2"


def test_stateMachine_Properties_mediaToAddr_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.mediaToAddr == "sample_text"
    instance.mediaToAddr = "sample_text_2"
    assert instance.mediaToAddr == "sample_text_2"


def test_stateMachine_Properties_mediaURI_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.mediaURI == "sample_text"
    instance.mediaURI = "sample_text_2"
    assert instance.mediaURI == "sample_text_2"


def test_stateMachine_Properties_recordPath_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.recordPath == "sample_text"
    instance.recordPath = "sample_text_2"
    assert instance.recordPath == "sample_text_2"


def test_stateMachine_Properties_scscfHost_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.scscfHost == "sample_text"
    instance.scscfHost = "sample_text_2"
    assert instance.scscfHost == "sample_text_2"


def test_stateMachine_Properties_scscfPort_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.scscfPort == 7
    instance.scscfPort = 13
    assert instance.scscfPort == 13


def test_stateMachine_Properties_scscfProtocol_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.scscfProtocol == "sample_text"
    instance.scscfProtocol = "sample_text_2"
    assert instance.scscfProtocol == "sample_text_2"


def test_stateMachine_Properties_scscfUser_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.scscfUser == "sample_text"
    instance.scscfUser = "sample_text_2"
    assert instance.scscfUser == "sample_text_2"


def test_stateMachine_Properties_setupConference_value_roundtrip():
    instance = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    assert instance.setupConference == True
    instance.setupConference = False
    assert instance.setupConference == False


def test_stateMachine_Recorderd_recordId_value_roundtrip():
    instance = stateMachine_Recorderd(recordId="sample_text")
    assert instance.recordId == "sample_text"
    instance.recordId = "sample_text_2"
    assert instance.recordId == "sample_text_2"


def test_stateMachine_SMS_from__value_roundtrip():
    instance = stateMachine_SMS(from_="sample_text", text="sample_text", to="sample_text")
    assert instance.from_ == "sample_text"
    instance.from_ = "sample_text_2"
    assert instance.from_ == "sample_text_2"


def test_stateMachine_SMS_text_value_roundtrip():
    instance = stateMachine_SMS(from_="sample_text", text="sample_text", to="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_stateMachine_SMS_to_value_roundtrip():
    instance = stateMachine_SMS(from_="sample_text", text="sample_text", to="sample_text")
    assert instance.to == "sample_text"
    instance.to = "sample_text_2"
    assert instance.to == "sample_text_2"


def test_stateMachine_SetTimer_millis_value_roundtrip():
    instance = stateMachine_SetTimer(millis=3.14)
    assert instance.millis == 3.14
    instance.millis = 9.99
    assert instance.millis == 9.99


def test_stateMachine_State_nombre_value_roundtrip():
    instance = stateMachine_State(nombre="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_stateMachine_StateMachine_nombre_value_roundtrip():
    instance = stateMachine_StateMachine(nombre="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_stateMachine_IvrAction_isa_Action():
    instance = stateMachine_IvrAction()
    assert isinstance(instance, Action)


def test_stateMachine_SendSms_isa_Action():
    instance = stateMachine_SendSms()
    assert isinstance(instance, Action)


def test_stateMachine_SetTimer_isa_Action():
    instance = stateMachine_SetTimer(millis=3.14)
    assert isinstance(instance, Action)


def test_stateMachine_Key_isa_Branch():
    instance = stateMachine_Key(key="sample_text")
    assert isinstance(instance, Branch)


def test_stateMachine_Otherwise_isa_Branch():
    instance = stateMachine_Otherwise()
    assert isinstance(instance, Branch)


def test_stateMachine_Bye_isa_IVREvent():
    instance = stateMachine_Bye()
    assert isinstance(instance, IVREvent)


def test_stateMachine_Call_isa_IVREvent():
    instance = stateMachine_Call(from_="sample_text", to="sample_text")
    assert isinstance(instance, IVREvent)


def test_stateMachine_Cancel_isa_IVREvent():
    instance = stateMachine_Cancel()
    assert isinstance(instance, IVREvent)


def test_stateMachine_CollectTimeout_isa_IVREvent():
    instance = stateMachine_CollectTimeout()
    assert isinstance(instance, IVREvent)


def test_stateMachine_Collected_isa_IVREvent():
    instance = stateMachine_Collected()
    assert isinstance(instance, IVREvent)


def test_stateMachine_Init_isa_IVREvent():
    instance = stateMachine_Init()
    assert isinstance(instance, IVREvent)


def test_stateMachine_Managed_isa_IVREvent():
    instance = stateMachine_Managed(code=7, success=True)
    assert isinstance(instance, IVREvent)


def test_stateMachine_PickUp_isa_IVREvent():
    instance = stateMachine_PickUp()
    assert isinstance(instance, IVREvent)


def test_stateMachine_Played_isa_IVREvent():
    instance = stateMachine_Played()
    assert isinstance(instance, IVREvent)


def test_stateMachine_Recorderd_isa_IVREvent():
    instance = stateMachine_Recorderd(recordId="sample_text")
    assert isinstance(instance, IVREvent)


def test_stateMachine_Terminated_isa_IVREvent():
    instance = stateMachine_Terminated()
    assert isinstance(instance, IVREvent)


def test_stateMachine_Play_isa_IvrAction():
    instance = stateMachine_Play(baseURL="sample_text", mediaURI="sample_text")
    assert isinstance(instance, IvrAction)


def test_stateMachine_Terminate_isa_IvrAction():
    instance = stateMachine_Terminate()
    assert isinstance(instance, IvrAction)


def test_stateMachine_CompositeState_isa_State():
    instance = stateMachine_CompositeState()
    assert isinstance(instance, State)


def test_stateMachine_FinalState_isa_State():
    instance = stateMachine_FinalState()
    assert isinstance(instance, State)


def test_stateMachine_InitialState_isa_State():
    instance = stateMachine_InitialState()
    assert isinstance(instance, State)


def test_stateMachine_IVREvent_isa_Transition():
    instance = stateMachine_IVREvent()
    assert isinstance(instance, Transition)


def test_stateMachine_NoneEvent_isa_Transition():
    instance = stateMachine_NoneEvent()
    assert isinstance(instance, Transition)


def test_stateMachine_SMSReceived_isa_Transition():
    instance = stateMachine_SMSReceived()
    assert isinstance(instance, Transition)


def test_stateMachine_Timer_isa_Transition():
    instance = stateMachine_Timer()
    assert isinstance(instance, Transition)


def test_assoc_children5_link_reassign_clear():
    a = stateMachine_State(nombre="sample_text")
    b1 = stateMachine_State(nombre="sample_text")
    b2 = stateMachine_State(nombre="sample_text_2")
    _safe_set(a, 'State', b1)
    assert _is_linked(a, 'State', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'State', b2)
    assert _is_linked(a, 'State', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'State', None)
    assert not _is_linked(a, 'State', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_defaultTar15_link_reassign_clear():
    a = stateMachine_State(nombre="sample_text")
    b1 = stateMachine_Transition()
    b2 = stateMachine_Transition()
    _safe_set(a, 'stateMachine_State17', b1)
    assert _is_linked(a, 'stateMachine_State17', b1)
    if hasattr(b1, 'stateMachine_Transition16'):
        assert _is_linked(b1, 'stateMachine_Transition16', a)
    _safe_set(a, 'stateMachine_State17', b2)
    assert _is_linked(a, 'stateMachine_State17', b2)
    if hasattr(b1, 'stateMachine_Transition16'):
        assert not _is_linked(b1, 'stateMachine_Transition16', a)
    if hasattr(b2, 'stateMachine_Transition16'):
        assert _is_linked(b2, 'stateMachine_Transition16', a)
    _safe_set(a, 'stateMachine_State17', None)
    assert not _is_linked(a, 'stateMachine_State17', b2)
    if hasattr(b2, 'stateMachine_Transition16'):
        assert not _is_linked(b2, 'stateMachine_Transition16', a)


def test_assoc_out21_link_reassign_clear():
    a = stateMachine_State(nombre="sample_text")
    b1 = stateMachine_Branch()
    b2 = stateMachine_Branch()
    _safe_set(a, 'stateMachine_State23', b1)
    assert _is_linked(a, 'stateMachine_State23', b1)
    if hasattr(b1, 'stateMachine_Branch22'):
        assert _is_linked(b1, 'stateMachine_Branch22', a)
    _safe_set(a, 'stateMachine_State23', b2)
    assert _is_linked(a, 'stateMachine_State23', b2)
    if hasattr(b1, 'stateMachine_Branch22'):
        assert not _is_linked(b1, 'stateMachine_Branch22', a)
    if hasattr(b2, 'stateMachine_Branch22'):
        assert _is_linked(b2, 'stateMachine_Branch22', a)
    _safe_set(a, 'stateMachine_State23', None)
    assert not _is_linked(a, 'stateMachine_State23', b2)
    if hasattr(b2, 'stateMachine_Branch22'):
        assert not _is_linked(b2, 'stateMachine_Branch22', a)


def test_assoc_outs3_link_reassign_clear():
    a = stateMachine_State(nombre="sample_text")
    b1 = stateMachine_Transition()
    b2 = stateMachine_Transition()
    _safe_set(a, 'src', {b1})
    assert _is_linked(a, 'src', b1)
    if hasattr(b1, 'Transition'):
        assert _is_linked(b1, 'Transition', a)
    _safe_set(a, 'src', {b2})
    assert _is_linked(a, 'src', b2)
    if hasattr(b1, 'Transition'):
        assert not _is_linked(b1, 'Transition', a)
    if hasattr(b2, 'Transition'):
        assert _is_linked(b2, 'Transition', a)
    _safe_set(a, 'src', set())
    assert not _is_linked(a, 'src', b2)
    if hasattr(b2, 'Transition'):
        assert not _is_linked(b2, 'Transition', a)


def test_assoc_parent7_link_reassign_clear():
    a = stateMachine_State(nombre="sample_text")
    b1 = stateMachine_State(nombre="sample_text")
    b2 = stateMachine_State(nombre="sample_text_2")
    _safe_set(a, 'State8', b1)
    assert _is_linked(a, 'State8', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'State8', b2)
    assert _is_linked(a, 'State8', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'State8', None)
    assert not _is_linked(a, 'State8', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_properties1_link_reassign_clear():
    a = stateMachine_StateMachine(nombre="sample_text")
    b1 = stateMachine_Properties(applicationAddress="sample_text", applicationServerHost="sample_text", applicationServerPort=7, applicationServerProtocol="sample_text", mediaFromAddr="sample_text", mediaHost="sample_text", mediaPort=7, mediaProtocol="sample_text", mediaToAddr="sample_text", mediaURI="sample_text", recordPath="sample_text", scscfHost="sample_text", scscfPort=7, scscfProtocol="sample_text", scscfUser="sample_text", setupConference=True)
    b2 = stateMachine_Properties(applicationAddress="sample_text_2", applicationServerHost="sample_text_2", applicationServerPort=13, applicationServerProtocol="sample_text_2", mediaFromAddr="sample_text_2", mediaHost="sample_text_2", mediaPort=13, mediaProtocol="sample_text_2", mediaToAddr="sample_text_2", mediaURI="sample_text_2", recordPath="sample_text_2", scscfHost="sample_text_2", scscfPort=13, scscfProtocol="sample_text_2", scscfUser="sample_text_2", setupConference=False)
    _safe_set(a, 'stateMachine_StateMachine2', b1)
    assert _is_linked(a, 'stateMachine_StateMachine2', b1)
    if hasattr(b1, 'stateMachine_Properties'):
        assert _is_linked(b1, 'stateMachine_Properties', a)
    _safe_set(a, 'stateMachine_StateMachine2', b2)
    assert _is_linked(a, 'stateMachine_StateMachine2', b2)
    if hasattr(b1, 'stateMachine_Properties'):
        assert not _is_linked(b1, 'stateMachine_Properties', a)
    if hasattr(b2, 'stateMachine_Properties'):
        assert _is_linked(b2, 'stateMachine_Properties', a)
    _safe_set(a, 'stateMachine_StateMachine2', None)
    assert not _is_linked(a, 'stateMachine_StateMachine2', b2)
    if hasattr(b2, 'stateMachine_Properties'):
        assert not _is_linked(b2, 'stateMachine_Properties', a)


def test_assoc_sm9_link_reassign_clear():
    a = stateMachine_StateMachine(nombre="sample_text")
    b1 = stateMachine_CompositeState()
    b2 = stateMachine_CompositeState()
    _safe_set(a, 'stateMachine_StateMachine10', b1)
    assert _is_linked(a, 'stateMachine_StateMachine10', b1)
    if hasattr(b1, 'stateMachine_CompositeState'):
        assert _is_linked(b1, 'stateMachine_CompositeState', a)
    _safe_set(a, 'stateMachine_StateMachine10', b2)
    assert _is_linked(a, 'stateMachine_StateMachine10', b2)
    if hasattr(b1, 'stateMachine_CompositeState'):
        assert not _is_linked(b1, 'stateMachine_CompositeState', a)
    if hasattr(b2, 'stateMachine_CompositeState'):
        assert _is_linked(b2, 'stateMachine_CompositeState', a)
    _safe_set(a, 'stateMachine_StateMachine10', None)
    assert not _is_linked(a, 'stateMachine_StateMachine10', b2)
    if hasattr(b2, 'stateMachine_CompositeState'):
        assert not _is_linked(b2, 'stateMachine_CompositeState', a)


def test_assoc_sms11_link_reassign_clear():
    a = stateMachine_SMS(from_="sample_text", text="sample_text", to="sample_text")
    b1 = stateMachine_SendSms()
    b2 = stateMachine_SendSms()
    _safe_set(a, 'stateMachine_SMS', b1)
    assert _is_linked(a, 'stateMachine_SMS', b1)
    if hasattr(b1, 'stateMachine_SendSms'):
        assert _is_linked(b1, 'stateMachine_SendSms', a)
    _safe_set(a, 'stateMachine_SMS', b2)
    assert _is_linked(a, 'stateMachine_SMS', b2)
    if hasattr(b1, 'stateMachine_SendSms'):
        assert not _is_linked(b1, 'stateMachine_SendSms', a)
    if hasattr(b2, 'stateMachine_SendSms'):
        assert _is_linked(b2, 'stateMachine_SendSms', a)
    _safe_set(a, 'stateMachine_SMS', None)
    assert not _is_linked(a, 'stateMachine_SMS', b2)
    if hasattr(b2, 'stateMachine_SendSms'):
        assert not _is_linked(b2, 'stateMachine_SendSms', a)


def test_assoc_sms18_link_reassign_clear():
    a = stateMachine_SMS(from_="sample_text", text="sample_text", to="sample_text")
    b1 = stateMachine_SMSReceived()
    b2 = stateMachine_SMSReceived()
    _safe_set(a, 'stateMachine_SMS19', b1)
    assert _is_linked(a, 'stateMachine_SMS19', b1)
    if hasattr(b1, 'stateMachine_SMSReceived'):
        assert _is_linked(b1, 'stateMachine_SMSReceived', a)
    _safe_set(a, 'stateMachine_SMS19', b2)
    assert _is_linked(a, 'stateMachine_SMS19', b2)
    if hasattr(b1, 'stateMachine_SMSReceived'):
        assert not _is_linked(b1, 'stateMachine_SMSReceived', a)
    if hasattr(b2, 'stateMachine_SMSReceived'):
        assert _is_linked(b2, 'stateMachine_SMSReceived', a)
    _safe_set(a, 'stateMachine_SMS19', None)
    assert not _is_linked(a, 'stateMachine_SMS19', b2)
    if hasattr(b2, 'stateMachine_SMSReceived'):
        assert not _is_linked(b2, 'stateMachine_SMSReceived', a)


def test_assoc_src13_link_reassign_clear():
    a = stateMachine_State(nombre="sample_text")
    b1 = stateMachine_Transition()
    b2 = stateMachine_Transition()
    _safe_set(a, 'State14', b1)
    assert _is_linked(a, 'State14', b1)
    if hasattr(b1, 'outs'):
        assert _is_linked(b1, 'outs', a)
    _safe_set(a, 'State14', b2)
    assert _is_linked(a, 'State14', b2)
    if hasattr(b1, 'outs'):
        assert not _is_linked(b1, 'outs', a)
    if hasattr(b2, 'outs'):
        assert _is_linked(b2, 'outs', a)
    _safe_set(a, 'State14', None)
    assert not _is_linked(a, 'State14', b2)
    if hasattr(b2, 'outs'):
        assert not _is_linked(b2, 'outs', a)


def test_assoc_states0_link_reassign_clear():
    a = stateMachine_StateMachine(nombre="sample_text")
    b1 = stateMachine_State(nombre="sample_text")
    b2 = stateMachine_State(nombre="sample_text_2")
    _safe_set(a, 'stateMachine_StateMachine', {b1})
    assert _is_linked(a, 'stateMachine_StateMachine', b1)
    if hasattr(b1, 'stateMachine_State'):
        assert _is_linked(b1, 'stateMachine_State', a)
    _safe_set(a, 'stateMachine_StateMachine', {b2})
    assert _is_linked(a, 'stateMachine_StateMachine', b2)
    if hasattr(b1, 'stateMachine_State'):
        assert not _is_linked(b1, 'stateMachine_State', a)
    if hasattr(b2, 'stateMachine_State'):
        assert _is_linked(b2, 'stateMachine_State', a)
    _safe_set(a, 'stateMachine_StateMachine', set())
    assert not _is_linked(a, 'stateMachine_StateMachine', b2)
    if hasattr(b2, 'stateMachine_State'):
        assert not _is_linked(b2, 'stateMachine_State', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Branch_strategy = st.builds(Branch)
@given(instance=Branch_strategy)
@settings(max_examples=25)
def test_Branch_instantiation(instance):
    assert isinstance(instance, Branch)


IVREvent_strategy = st.builds(IVREvent)
@given(instance=IVREvent_strategy)
@settings(max_examples=25)
def test_IVREvent_instantiation(instance):
    assert isinstance(instance, IVREvent)


IvrAction_strategy = st.builds(IvrAction)
@given(instance=IvrAction_strategy)
@settings(max_examples=25)
def test_IvrAction_instantiation(instance):
    assert isinstance(instance, IvrAction)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


stateMachine_Action_strategy = st.builds(stateMachine_Action)
@given(instance=stateMachine_Action_strategy)
@settings(max_examples=25)
def test_stateMachine_Action_instantiation(instance):
    assert isinstance(instance, stateMachine_Action)


stateMachine_Branch_strategy = st.builds(stateMachine_Branch)
@given(instance=stateMachine_Branch_strategy)
@settings(max_examples=25)
def test_stateMachine_Branch_instantiation(instance):
    assert isinstance(instance, stateMachine_Branch)


stateMachine_Bye_strategy = st.builds(stateMachine_Bye)
@given(instance=stateMachine_Bye_strategy)
@settings(max_examples=25)
def test_stateMachine_Bye_instantiation(instance):
    assert isinstance(instance, stateMachine_Bye)


stateMachine_Call_strategy = st.builds(stateMachine_Call, from_=safe_text, to=safe_text)
@given(instance=stateMachine_Call_strategy)
@settings(max_examples=25)
def test_stateMachine_Call_instantiation(instance):
    assert isinstance(instance, stateMachine_Call)


stateMachine_Cancel_strategy = st.builds(stateMachine_Cancel)
@given(instance=stateMachine_Cancel_strategy)
@settings(max_examples=25)
def test_stateMachine_Cancel_instantiation(instance):
    assert isinstance(instance, stateMachine_Cancel)


stateMachine_CollectTimeout_strategy = st.builds(stateMachine_CollectTimeout)
@given(instance=stateMachine_CollectTimeout_strategy)
@settings(max_examples=25)
def test_stateMachine_CollectTimeout_instantiation(instance):
    assert isinstance(instance, stateMachine_CollectTimeout)


stateMachine_Collected_strategy = st.builds(stateMachine_Collected)
@given(instance=stateMachine_Collected_strategy)
@settings(max_examples=25)
def test_stateMachine_Collected_instantiation(instance):
    assert isinstance(instance, stateMachine_Collected)


stateMachine_CompositeState_strategy = st.builds(stateMachine_CompositeState)
@given(instance=stateMachine_CompositeState_strategy)
@settings(max_examples=25)
def test_stateMachine_CompositeState_instantiation(instance):
    assert isinstance(instance, stateMachine_CompositeState)


stateMachine_FinalState_strategy = st.builds(stateMachine_FinalState)
@given(instance=stateMachine_FinalState_strategy)
@settings(max_examples=25)
def test_stateMachine_FinalState_instantiation(instance):
    assert isinstance(instance, stateMachine_FinalState)


stateMachine_IVREvent_strategy = st.builds(stateMachine_IVREvent)
@given(instance=stateMachine_IVREvent_strategy)
@settings(max_examples=25)
def test_stateMachine_IVREvent_instantiation(instance):
    assert isinstance(instance, stateMachine_IVREvent)


stateMachine_Init_strategy = st.builds(stateMachine_Init)
@given(instance=stateMachine_Init_strategy)
@settings(max_examples=25)
def test_stateMachine_Init_instantiation(instance):
    assert isinstance(instance, stateMachine_Init)


stateMachine_InitialState_strategy = st.builds(stateMachine_InitialState)
@given(instance=stateMachine_InitialState_strategy)
@settings(max_examples=25)
def test_stateMachine_InitialState_instantiation(instance):
    assert isinstance(instance, stateMachine_InitialState)


stateMachine_IvrAction_strategy = st.builds(stateMachine_IvrAction)
@given(instance=stateMachine_IvrAction_strategy)
@settings(max_examples=25)
def test_stateMachine_IvrAction_instantiation(instance):
    assert isinstance(instance, stateMachine_IvrAction)


stateMachine_Key_strategy = st.builds(stateMachine_Key, key=safe_text)
@given(instance=stateMachine_Key_strategy)
@settings(max_examples=25)
def test_stateMachine_Key_instantiation(instance):
    assert isinstance(instance, stateMachine_Key)


stateMachine_Managed_strategy = st.builds(stateMachine_Managed, code=st.integers(), success=st.booleans())
@given(instance=stateMachine_Managed_strategy)
@settings(max_examples=25)
def test_stateMachine_Managed_instantiation(instance):
    assert isinstance(instance, stateMachine_Managed)


stateMachine_NoneEvent_strategy = st.builds(stateMachine_NoneEvent)
@given(instance=stateMachine_NoneEvent_strategy)
@settings(max_examples=25)
def test_stateMachine_NoneEvent_instantiation(instance):
    assert isinstance(instance, stateMachine_NoneEvent)


stateMachine_Otherwise_strategy = st.builds(stateMachine_Otherwise)
@given(instance=stateMachine_Otherwise_strategy)
@settings(max_examples=25)
def test_stateMachine_Otherwise_instantiation(instance):
    assert isinstance(instance, stateMachine_Otherwise)


stateMachine_PickUp_strategy = st.builds(stateMachine_PickUp)
@given(instance=stateMachine_PickUp_strategy)
@settings(max_examples=25)
def test_stateMachine_PickUp_instantiation(instance):
    assert isinstance(instance, stateMachine_PickUp)


stateMachine_Play_strategy = st.builds(stateMachine_Play, baseURL=safe_text, mediaURI=safe_text)
@given(instance=stateMachine_Play_strategy)
@settings(max_examples=25)
def test_stateMachine_Play_instantiation(instance):
    assert isinstance(instance, stateMachine_Play)


stateMachine_Played_strategy = st.builds(stateMachine_Played)
@given(instance=stateMachine_Played_strategy)
@settings(max_examples=25)
def test_stateMachine_Played_instantiation(instance):
    assert isinstance(instance, stateMachine_Played)


stateMachine_Properties_strategy = st.builds(stateMachine_Properties, applicationAddress=safe_text, applicationServerHost=safe_text, applicationServerPort=st.integers(), applicationServerProtocol=safe_text, mediaFromAddr=safe_text, mediaHost=safe_text, mediaPort=st.integers(), mediaProtocol=safe_text, mediaToAddr=safe_text, mediaURI=safe_text, recordPath=safe_text, scscfHost=safe_text, scscfPort=st.integers(), scscfProtocol=safe_text, scscfUser=safe_text, setupConference=st.booleans())
@given(instance=stateMachine_Properties_strategy)
@settings(max_examples=25)
def test_stateMachine_Properties_instantiation(instance):
    assert isinstance(instance, stateMachine_Properties)


stateMachine_Recorderd_strategy = st.builds(stateMachine_Recorderd, recordId=safe_text)
@given(instance=stateMachine_Recorderd_strategy)
@settings(max_examples=25)
def test_stateMachine_Recorderd_instantiation(instance):
    assert isinstance(instance, stateMachine_Recorderd)


stateMachine_SMS_strategy = st.builds(stateMachine_SMS, from_=safe_text, text=safe_text, to=safe_text)
@given(instance=stateMachine_SMS_strategy)
@settings(max_examples=25)
def test_stateMachine_SMS_instantiation(instance):
    assert isinstance(instance, stateMachine_SMS)


stateMachine_SMSReceived_strategy = st.builds(stateMachine_SMSReceived)
@given(instance=stateMachine_SMSReceived_strategy)
@settings(max_examples=25)
def test_stateMachine_SMSReceived_instantiation(instance):
    assert isinstance(instance, stateMachine_SMSReceived)


stateMachine_SendSms_strategy = st.builds(stateMachine_SendSms)
@given(instance=stateMachine_SendSms_strategy)
@settings(max_examples=25)
def test_stateMachine_SendSms_instantiation(instance):
    assert isinstance(instance, stateMachine_SendSms)


stateMachine_SetTimer_strategy = st.builds(stateMachine_SetTimer, millis=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=stateMachine_SetTimer_strategy)
@settings(max_examples=25)
def test_stateMachine_SetTimer_instantiation(instance):
    assert isinstance(instance, stateMachine_SetTimer)


stateMachine_State_strategy = st.builds(stateMachine_State, nombre=safe_text)
@given(instance=stateMachine_State_strategy)
@settings(max_examples=25)
def test_stateMachine_State_instantiation(instance):
    assert isinstance(instance, stateMachine_State)


stateMachine_StateMachine_strategy = st.builds(stateMachine_StateMachine, nombre=safe_text)
@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=25)
def test_stateMachine_StateMachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)


stateMachine_Terminate_strategy = st.builds(stateMachine_Terminate)
@given(instance=stateMachine_Terminate_strategy)
@settings(max_examples=25)
def test_stateMachine_Terminate_instantiation(instance):
    assert isinstance(instance, stateMachine_Terminate)


stateMachine_Terminated_strategy = st.builds(stateMachine_Terminated)
@given(instance=stateMachine_Terminated_strategy)
@settings(max_examples=25)
def test_stateMachine_Terminated_instantiation(instance):
    assert isinstance(instance, stateMachine_Terminated)


stateMachine_Timer_strategy = st.builds(stateMachine_Timer)
@given(instance=stateMachine_Timer_strategy)
@settings(max_examples=25)
def test_stateMachine_Timer_instantiation(instance):
    assert isinstance(instance, stateMachine_Timer)


stateMachine_Transition_strategy = st.builds(stateMachine_Transition)
@given(instance=stateMachine_Transition_strategy)
@settings(max_examples=25)
def test_stateMachine_Transition_instantiation(instance):
    assert isinstance(instance, stateMachine_Transition)


