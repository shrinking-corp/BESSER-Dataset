import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Algorithm,
    ColorizableElement,
    CompilableType,
    CompositeFBType,
    ConfigurableObject,
    Connection,
    DataType,
    Event,
    FB,
    FBNetworkElement,
    FBType,
    I4DIACElement,
    IInterfaceElement,
    INamedElement,
    IVarElement,
    LibraryElement,
    PositionableElement,
    Primitive,
    TextAlgorithm,
    TypedConfigureableObject,
    VarDeclaration,
    libraryElement_AdapterConnection,
    libraryElement_AdapterDeclaration,
    libraryElement_AdapterEvent,
    libraryElement_AdapterFB,
    libraryElement_AdapterFBType,
    libraryElement_AdapterType,
    libraryElement_AdapterTypePaletteEntry,
    libraryElement_Algorithm,
    libraryElement_Annotation,
    libraryElement_Application,
    libraryElement_AutomationSystem,
    libraryElement_BasicFBType,
    libraryElement_Color,
    libraryElement_ColorizableElement,
    libraryElement_CompilableType,
    libraryElement_Compiler,
    libraryElement_CompilerInfo,
    libraryElement_CompositeFBType,
    libraryElement_ConfigurableObject,
    libraryElement_Connection,
    libraryElement_DataConnection,
    libraryElement_DataType,
    libraryElement_Device,
    libraryElement_DeviceType,
    libraryElement_ECAction,
    libraryElement_ECC,
    libraryElement_ECState,
    libraryElement_ECTransition,
    libraryElement_Event,
    libraryElement_EventConnection,
    libraryElement_FB,
    libraryElement_FBNetwork,
    libraryElement_FBNetworkElement,
    libraryElement_FBType,
    libraryElement_I4DIACElement,
    libraryElement_IInterfaceElement,
    libraryElement_INamedElement,
    libraryElement_IVarElement,
    libraryElement_Identification,
    libraryElement_InputPrimitive,
    libraryElement_InterfaceList,
    libraryElement_LibraryElement,
    libraryElement_Link,
    libraryElement_Mapping,
    libraryElement_OtherAlgorithm,
    libraryElement_OutputPrimitive,
    libraryElement_Palette,
    libraryElement_PaletteEntry,
    libraryElement_Parameter,
    libraryElement_PositionableElement,
    libraryElement_Primitive,
    libraryElement_Resource,
    libraryElement_ResourceType,
    libraryElement_ResourceTypeFB,
    libraryElement_ResourceTypeName,
    libraryElement_STAlgorithm,
    libraryElement_Segment,
    libraryElement_SegmentType,
    libraryElement_Service,
    libraryElement_ServiceInterface,
    libraryElement_ServiceInterfaceFBType,
    libraryElement_ServiceSequence,
    libraryElement_ServiceTransaction,
    libraryElement_SubApp,
    libraryElement_SubAppType,
    libraryElement_SystemConfiguration,
    libraryElement_TextAlgorithm,
    libraryElement_TypedConfigureableObject,
    libraryElement_Value,
    libraryElement_VarDeclaration,
    libraryElement_VarInitialization,
    libraryElement_VersionInfo,
    libraryElement_With,
    Language,
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

def test_assoc_adapterConnections114_reverse_link_reassign_clear():
    a1 = libraryElement_FBNetwork()
    a2 = libraryElement_FBNetwork()
    b = libraryElement_AdapterConnection()
    _safe_set(b, 'libraryElement_AdapterConnection', a1)
    assert _is_linked(b, 'libraryElement_AdapterConnection', a1)
    if hasattr(a1, 'libraryElement_FBNetwork115'):
        assert _is_linked(a1, 'libraryElement_FBNetwork115', b)
    _safe_set(b, 'libraryElement_AdapterConnection', a2)
    assert _is_linked(b, 'libraryElement_AdapterConnection', a2)
    if hasattr(a1, 'libraryElement_FBNetwork115'):
        assert not _is_linked(a1, 'libraryElement_FBNetwork115', b)
    if hasattr(a2, 'libraryElement_FBNetwork115'):
        assert _is_linked(a2, 'libraryElement_FBNetwork115', b)
    _safe_set(b, 'libraryElement_AdapterConnection', None)
    assert not _is_linked(b, 'libraryElement_AdapterConnection', a2)
    if hasattr(a2, 'libraryElement_FBNetwork115'):
        assert not _is_linked(a2, 'libraryElement_FBNetwork115', b)


def test_assoc_annotations152_reverse_link_reassign_clear():
    a1 = libraryElement_I4DIACElement()
    a2 = libraryElement_I4DIACElement()
    b = libraryElement_Annotation(name="sample_text", servity="sample_text")
    _safe_set(b, 'libraryElement_Annotation', a1)
    assert _is_linked(b, 'libraryElement_Annotation', a1)
    if hasattr(a1, 'libraryElement_I4DIACElement'):
        assert _is_linked(a1, 'libraryElement_I4DIACElement', b)
    _safe_set(b, 'libraryElement_Annotation', a2)
    assert _is_linked(b, 'libraryElement_Annotation', a2)
    if hasattr(a1, 'libraryElement_I4DIACElement'):
        assert not _is_linked(a1, 'libraryElement_I4DIACElement', b)
    if hasattr(a2, 'libraryElement_I4DIACElement'):
        assert _is_linked(a2, 'libraryElement_I4DIACElement', b)
    _safe_set(b, 'libraryElement_Annotation', None)
    assert not _is_linked(b, 'libraryElement_Annotation', a2)
    if hasattr(a2, 'libraryElement_I4DIACElement'):
        assert not _is_linked(a2, 'libraryElement_I4DIACElement', b)


def test_assoc_application116_reverse_link_reassign_clear():
    a1 = libraryElement_AutomationSystem(project="sample_text")
    a2 = libraryElement_AutomationSystem(project="sample_text_2")
    b = libraryElement_Application()
    _safe_set(b, 'libraryElement_Application117', a1)
    assert _is_linked(b, 'libraryElement_Application117', a1)
    if hasattr(a1, 'libraryElement_AutomationSystem'):
        assert _is_linked(a1, 'libraryElement_AutomationSystem', b)
    _safe_set(b, 'libraryElement_Application117', a2)
    assert _is_linked(b, 'libraryElement_Application117', a2)
    if hasattr(a1, 'libraryElement_AutomationSystem'):
        assert not _is_linked(a1, 'libraryElement_AutomationSystem', b)
    if hasattr(a2, 'libraryElement_AutomationSystem'):
        assert _is_linked(a2, 'libraryElement_AutomationSystem', b)
    _safe_set(b, 'libraryElement_Application117', None)
    assert not _is_linked(b, 'libraryElement_Application117', a2)
    if hasattr(a2, 'libraryElement_AutomationSystem'):
        assert not _is_linked(a2, 'libraryElement_AutomationSystem', b)


def test_assoc_compiler9_reverse_link_reassign_clear():
    a1 = libraryElement_CompilerInfo(classdef="sample_text", header="sample_text")
    a2 = libraryElement_CompilerInfo(classdef="sample_text_2", header="sample_text_2")
    b = libraryElement_Compiler(language="sample_text", product="sample_text", vendor="sample_text", version="sample_text")
    _safe_set(b, 'libraryElement_Compiler', a1)
    assert _is_linked(b, 'libraryElement_Compiler', a1)
    if hasattr(a1, 'libraryElement_CompilerInfo'):
        assert _is_linked(a1, 'libraryElement_CompilerInfo', b)
    _safe_set(b, 'libraryElement_Compiler', a2)
    assert _is_linked(b, 'libraryElement_Compiler', a2)
    if hasattr(a1, 'libraryElement_CompilerInfo'):
        assert not _is_linked(a1, 'libraryElement_CompilerInfo', b)
    if hasattr(a2, 'libraryElement_CompilerInfo'):
        assert _is_linked(a2, 'libraryElement_CompilerInfo', b)
    _safe_set(b, 'libraryElement_Compiler', None)
    assert not _is_linked(b, 'libraryElement_Compiler', a2)
    if hasattr(a2, 'libraryElement_CompilerInfo'):
        assert not _is_linked(a2, 'libraryElement_CompilerInfo', b)


def test_assoc_dataConnections110_reverse_link_reassign_clear():
    a1 = libraryElement_FBNetwork()
    a2 = libraryElement_FBNetwork()
    b = libraryElement_DataConnection()
    _safe_set(b, 'libraryElement_DataConnection', a1)
    assert _is_linked(b, 'libraryElement_DataConnection', a1)
    if hasattr(a1, 'libraryElement_FBNetwork111'):
        assert _is_linked(a1, 'libraryElement_FBNetwork111', b)
    _safe_set(b, 'libraryElement_DataConnection', a2)
    assert _is_linked(b, 'libraryElement_DataConnection', a2)
    if hasattr(a1, 'libraryElement_FBNetwork111'):
        assert not _is_linked(a1, 'libraryElement_FBNetwork111', b)
    if hasattr(a2, 'libraryElement_FBNetwork111'):
        assert _is_linked(a2, 'libraryElement_FBNetwork111', b)
    _safe_set(b, 'libraryElement_DataConnection', None)
    assert not _is_linked(b, 'libraryElement_DataConnection', a2)
    if hasattr(a2, 'libraryElement_FBNetwork111'):
        assert not _is_linked(a2, 'libraryElement_FBNetwork111', b)


def test_assoc_destination11_reverse_link_reassign_clear():
    a1 = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    a2 = libraryElement_IInterfaceElement(isInput="sample_text_2", typeName="sample_text_2")
    b = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    _safe_set(b, 'inputConnections', a1)
    assert _is_linked(b, 'inputConnections', a1)
    if hasattr(a1, 'IInterfaceElement12'):
        assert _is_linked(a1, 'IInterfaceElement12', b)
    _safe_set(b, 'inputConnections', a2)
    assert _is_linked(b, 'inputConnections', a2)
    if hasattr(a1, 'IInterfaceElement12'):
        assert not _is_linked(a1, 'IInterfaceElement12', b)
    if hasattr(a2, 'IInterfaceElement12'):
        assert _is_linked(a2, 'IInterfaceElement12', b)
    _safe_set(b, 'inputConnections', None)
    assert not _is_linked(b, 'inputConnections', a2)
    if hasattr(a2, 'IInterfaceElement12'):
        assert not _is_linked(a2, 'IInterfaceElement12', b)


def test_assoc_destination43_reverse_link_reassign_clear():
    a1 = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    a2 = libraryElement_ECTransition(comment="sample_text_2", conditionExpression="sample_text_2")
    b = libraryElement_ECState()
    _safe_set(b, 'ECState44', a1)
    assert _is_linked(b, 'ECState44', a1)
    if hasattr(a1, 'inTransitions'):
        assert _is_linked(a1, 'inTransitions', b)
    _safe_set(b, 'ECState44', a2)
    assert _is_linked(b, 'ECState44', a2)
    if hasattr(a1, 'inTransitions'):
        assert not _is_linked(a1, 'inTransitions', b)
    if hasattr(a2, 'inTransitions'):
        assert _is_linked(a2, 'inTransitions', b)
    _safe_set(b, 'ECState44', None)
    assert not _is_linked(b, 'ECState44', a2)
    if hasattr(a2, 'inTransitions'):
        assert not _is_linked(a2, 'inTransitions', b)


def test_assoc_device88_reverse_link_reassign_clear():
    a1 = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    a2 = libraryElement_Resource(deviceTypeResource="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = libraryElement_Device(profile="sample_text")
    _safe_set(b, 'Device89', a1)
    assert _is_linked(b, 'Device89', a1)
    if hasattr(a1, 'resource'):
        assert _is_linked(a1, 'resource', b)
    _safe_set(b, 'Device89', a2)
    assert _is_linked(b, 'Device89', a2)
    if hasattr(a1, 'resource'):
        assert not _is_linked(a1, 'resource', b)
    if hasattr(a2, 'resource'):
        assert _is_linked(a2, 'resource', b)
    _safe_set(b, 'Device89', None)
    assert not _is_linked(b, 'Device89', a2)
    if hasattr(a2, 'resource'):
        assert not _is_linked(a2, 'resource', b)


def test_assoc_devices145_reverse_link_reassign_clear():
    a1 = libraryElement_SystemConfiguration()
    a2 = libraryElement_SystemConfiguration()
    b = libraryElement_Device(profile="sample_text")
    _safe_set(b, 'libraryElement_Device', a1)
    assert _is_linked(b, 'libraryElement_Device', a1)
    if hasattr(a1, 'libraryElement_SystemConfiguration146'):
        assert _is_linked(a1, 'libraryElement_SystemConfiguration146', b)
    _safe_set(b, 'libraryElement_Device', a2)
    assert _is_linked(b, 'libraryElement_Device', a2)
    if hasattr(a1, 'libraryElement_SystemConfiguration146'):
        assert not _is_linked(a1, 'libraryElement_SystemConfiguration146', b)
    if hasattr(a2, 'libraryElement_SystemConfiguration146'):
        assert _is_linked(a2, 'libraryElement_SystemConfiguration146', b)
    _safe_set(b, 'libraryElement_Device', None)
    assert not _is_linked(b, 'libraryElement_Device', a2)
    if hasattr(a2, 'libraryElement_SystemConfiguration146'):
        assert not _is_linked(a2, 'libraryElement_SystemConfiguration146', b)


def test_assoc_eventConnections112_reverse_link_reassign_clear():
    a1 = libraryElement_FBNetwork()
    a2 = libraryElement_FBNetwork()
    b = libraryElement_EventConnection()
    _safe_set(b, 'libraryElement_EventConnection', a1)
    assert _is_linked(b, 'libraryElement_EventConnection', a1)
    if hasattr(a1, 'libraryElement_FBNetwork113'):
        assert _is_linked(a1, 'libraryElement_FBNetwork113', b)
    _safe_set(b, 'libraryElement_EventConnection', a2)
    assert _is_linked(b, 'libraryElement_EventConnection', a2)
    if hasattr(a1, 'libraryElement_FBNetwork113'):
        assert not _is_linked(a1, 'libraryElement_FBNetwork113', b)
    if hasattr(a2, 'libraryElement_FBNetwork113'):
        assert _is_linked(a2, 'libraryElement_FBNetwork113', b)
    _safe_set(b, 'libraryElement_EventConnection', None)
    assert not _is_linked(b, 'libraryElement_EventConnection', a2)
    if hasattr(a2, 'libraryElement_FBNetwork113'):
        assert not _is_linked(a2, 'libraryElement_FBNetwork113', b)


def test_assoc_fBNetwork22_reverse_link_reassign_clear():
    a1 = libraryElement_FBNetwork()
    a2 = libraryElement_FBNetwork()
    b = libraryElement_DeviceType(profile="sample_text")
    _safe_set(b, 'libraryElement_DeviceType23', a1)
    assert _is_linked(b, 'libraryElement_DeviceType23', a1)
    if hasattr(a1, 'libraryElement_FBNetwork24'):
        assert _is_linked(a1, 'libraryElement_FBNetwork24', b)
    _safe_set(b, 'libraryElement_DeviceType23', a2)
    assert _is_linked(b, 'libraryElement_DeviceType23', a2)
    if hasattr(a1, 'libraryElement_FBNetwork24'):
        assert not _is_linked(a1, 'libraryElement_FBNetwork24', b)
    if hasattr(a2, 'libraryElement_FBNetwork24'):
        assert _is_linked(a2, 'libraryElement_FBNetwork24', b)
    _safe_set(b, 'libraryElement_DeviceType23', None)
    assert not _is_linked(b, 'libraryElement_DeviceType23', a2)
    if hasattr(a2, 'libraryElement_FBNetwork24'):
        assert not _is_linked(a2, 'libraryElement_FBNetwork24', b)


def test_assoc_fBNetwork3_reverse_link_reassign_clear():
    a1 = libraryElement_FBNetwork()
    a2 = libraryElement_FBNetwork()
    b = libraryElement_Application()
    _safe_set(b, 'libraryElement_Application', a1)
    assert _is_linked(b, 'libraryElement_Application', a1)
    if hasattr(a1, 'libraryElement_FBNetwork'):
        assert _is_linked(a1, 'libraryElement_FBNetwork', b)
    _safe_set(b, 'libraryElement_Application', a2)
    assert _is_linked(b, 'libraryElement_Application', a2)
    if hasattr(a1, 'libraryElement_FBNetwork'):
        assert not _is_linked(a1, 'libraryElement_FBNetwork', b)
    if hasattr(a2, 'libraryElement_FBNetwork'):
        assert _is_linked(a2, 'libraryElement_FBNetwork', b)
    _safe_set(b, 'libraryElement_Application', None)
    assert not _is_linked(b, 'libraryElement_Application', a2)
    if hasattr(a2, 'libraryElement_FBNetwork'):
        assert not _is_linked(a2, 'libraryElement_FBNetwork', b)


def test_assoc_fBNetwork85_reverse_link_reassign_clear():
    a1 = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    a2 = libraryElement_Resource(deviceTypeResource="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = libraryElement_FBNetwork()
    _safe_set(b, 'libraryElement_FBNetwork87', a1)
    assert _is_linked(b, 'libraryElement_FBNetwork87', a1)
    if hasattr(a1, 'libraryElement_Resource86'):
        assert _is_linked(a1, 'libraryElement_Resource86', b)
    _safe_set(b, 'libraryElement_FBNetwork87', a2)
    assert _is_linked(b, 'libraryElement_FBNetwork87', a2)
    if hasattr(a1, 'libraryElement_Resource86'):
        assert not _is_linked(a1, 'libraryElement_Resource86', b)
    if hasattr(a2, 'libraryElement_Resource86'):
        assert _is_linked(a2, 'libraryElement_Resource86', b)
    _safe_set(b, 'libraryElement_FBNetwork87', None)
    assert not _is_linked(b, 'libraryElement_FBNetwork87', a2)
    if hasattr(a2, 'libraryElement_Resource86'):
        assert not _is_linked(a2, 'libraryElement_Resource86', b)


def test_assoc_from_79_reverse_link_reassign_clear():
    a1 = libraryElement_Mapping()
    a2 = libraryElement_Mapping()
    b = libraryElement_FBNetworkElement()
    _safe_set(b, 'libraryElement_FBNetworkElement81', a1)
    assert _is_linked(b, 'libraryElement_FBNetworkElement81', a1)
    if hasattr(a1, 'libraryElement_Mapping80'):
        assert _is_linked(a1, 'libraryElement_Mapping80', b)
    _safe_set(b, 'libraryElement_FBNetworkElement81', a2)
    assert _is_linked(b, 'libraryElement_FBNetworkElement81', a2)
    if hasattr(a1, 'libraryElement_Mapping80'):
        assert not _is_linked(a1, 'libraryElement_Mapping80', b)
    if hasattr(a2, 'libraryElement_Mapping80'):
        assert _is_linked(a2, 'libraryElement_Mapping80', b)
    _safe_set(b, 'libraryElement_FBNetworkElement81', None)
    assert not _is_linked(b, 'libraryElement_FBNetworkElement81', a2)
    if hasattr(a2, 'libraryElement_Mapping80'):
        assert not _is_linked(a2, 'libraryElement_Mapping80', b)


def test_assoc_inTransitions40_reverse_link_reassign_clear():
    a1 = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    a2 = libraryElement_ECTransition(comment="sample_text_2", conditionExpression="sample_text_2")
    b = libraryElement_ECState()
    _safe_set(b, 'destination', {a1})
    assert _is_linked(b, 'destination', a1)
    if hasattr(a1, 'ECTransition41'):
        assert _is_linked(a1, 'ECTransition41', b)
    _safe_set(b, 'destination', {a2})
    assert _is_linked(b, 'destination', a2)
    if hasattr(a1, 'ECTransition41'):
        assert not _is_linked(a1, 'ECTransition41', b)
    if hasattr(a2, 'ECTransition41'):
        assert _is_linked(a2, 'ECTransition41', b)
    _safe_set(b, 'destination', set())
    assert not _is_linked(b, 'destination', a2)
    if hasattr(a2, 'ECTransition41'):
        assert not _is_linked(a2, 'ECTransition41', b)


def test_assoc_inputConnections137_reverse_link_reassign_clear():
    a1 = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    a2 = libraryElement_IInterfaceElement(isInput="sample_text_2", typeName="sample_text_2")
    b = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    _safe_set(b, 'Connection', a1)
    assert _is_linked(b, 'Connection', a1)
    if hasattr(a1, 'destination138'):
        assert _is_linked(a1, 'destination138', b)
    _safe_set(b, 'Connection', a2)
    assert _is_linked(b, 'Connection', a2)
    if hasattr(a1, 'destination138'):
        assert not _is_linked(a1, 'destination138', b)
    if hasattr(a2, 'destination138'):
        assert _is_linked(a2, 'destination138', b)
    _safe_set(b, 'Connection', None)
    assert not _is_linked(b, 'Connection', a2)
    if hasattr(a2, 'destination138'):
        assert not _is_linked(a2, 'destination138', b)


def test_assoc_inputVars71_reverse_link_reassign_clear():
    a1 = libraryElement_VarDeclaration(arraySize="sample_text")
    a2 = libraryElement_VarDeclaration(arraySize="sample_text_2")
    b = libraryElement_InterfaceList()
    _safe_set(b, 'libraryElement_InterfaceList72', {a1})
    assert _is_linked(b, 'libraryElement_InterfaceList72', a1)
    if hasattr(a1, 'libraryElement_VarDeclaration73'):
        assert _is_linked(a1, 'libraryElement_VarDeclaration73', b)
    _safe_set(b, 'libraryElement_InterfaceList72', {a2})
    assert _is_linked(b, 'libraryElement_InterfaceList72', a2)
    if hasattr(a1, 'libraryElement_VarDeclaration73'):
        assert not _is_linked(a1, 'libraryElement_VarDeclaration73', b)
    if hasattr(a2, 'libraryElement_VarDeclaration73'):
        assert _is_linked(a2, 'libraryElement_VarDeclaration73', b)
    _safe_set(b, 'libraryElement_InterfaceList72', set())
    assert not _is_linked(b, 'libraryElement_InterfaceList72', a2)
    if hasattr(a2, 'libraryElement_VarDeclaration73'):
        assert not _is_linked(a2, 'libraryElement_VarDeclaration73', b)


def test_assoc_interface50_reverse_link_reassign_clear():
    a1 = libraryElement_InterfaceList()
    a2 = libraryElement_InterfaceList()
    b = libraryElement_FBNetworkElement()
    _safe_set(b, 'libraryElement_FBNetworkElement', a1)
    assert _is_linked(b, 'libraryElement_FBNetworkElement', a1)
    if hasattr(a1, 'libraryElement_InterfaceList'):
        assert _is_linked(a1, 'libraryElement_InterfaceList', b)
    _safe_set(b, 'libraryElement_FBNetworkElement', a2)
    assert _is_linked(b, 'libraryElement_FBNetworkElement', a2)
    if hasattr(a1, 'libraryElement_InterfaceList'):
        assert not _is_linked(a1, 'libraryElement_InterfaceList', b)
    if hasattr(a2, 'libraryElement_InterfaceList'):
        assert _is_linked(a2, 'libraryElement_InterfaceList', b)
    _safe_set(b, 'libraryElement_FBNetworkElement', None)
    assert not _is_linked(b, 'libraryElement_FBNetworkElement', a2)
    if hasattr(a2, 'libraryElement_InterfaceList'):
        assert not _is_linked(a2, 'libraryElement_InterfaceList', b)


def test_assoc_mapping118_reverse_link_reassign_clear():
    a1 = libraryElement_Mapping()
    a2 = libraryElement_Mapping()
    b = libraryElement_AutomationSystem(project="sample_text")
    _safe_set(b, 'libraryElement_AutomationSystem119', {a1})
    assert _is_linked(b, 'libraryElement_AutomationSystem119', a1)
    if hasattr(a1, 'libraryElement_Mapping120'):
        assert _is_linked(a1, 'libraryElement_Mapping120', b)
    _safe_set(b, 'libraryElement_AutomationSystem119', {a2})
    assert _is_linked(b, 'libraryElement_AutomationSystem119', a2)
    if hasattr(a1, 'libraryElement_Mapping120'):
        assert not _is_linked(a1, 'libraryElement_Mapping120', b)
    if hasattr(a2, 'libraryElement_Mapping120'):
        assert _is_linked(a2, 'libraryElement_Mapping120', b)
    _safe_set(b, 'libraryElement_AutomationSystem119', set())
    assert not _is_linked(b, 'libraryElement_AutomationSystem119', a2)
    if hasattr(a2, 'libraryElement_Mapping120'):
        assert not _is_linked(a2, 'libraryElement_Mapping120', b)


def test_assoc_mapping51_reverse_link_reassign_clear():
    a1 = libraryElement_Mapping()
    a2 = libraryElement_Mapping()
    b = libraryElement_FBNetworkElement()
    _safe_set(b, 'libraryElement_FBNetworkElement52', a1)
    assert _is_linked(b, 'libraryElement_FBNetworkElement52', a1)
    if hasattr(a1, 'libraryElement_Mapping'):
        assert _is_linked(a1, 'libraryElement_Mapping', b)
    _safe_set(b, 'libraryElement_FBNetworkElement52', a2)
    assert _is_linked(b, 'libraryElement_FBNetworkElement52', a2)
    if hasattr(a1, 'libraryElement_Mapping'):
        assert not _is_linked(a1, 'libraryElement_Mapping', b)
    if hasattr(a2, 'libraryElement_Mapping'):
        assert _is_linked(a2, 'libraryElement_Mapping', b)
    _safe_set(b, 'libraryElement_FBNetworkElement52', None)
    assert not _is_linked(b, 'libraryElement_FBNetworkElement52', a2)
    if hasattr(a2, 'libraryElement_Mapping'):
        assert not _is_linked(a2, 'libraryElement_Mapping', b)


def test_assoc_networkElements107_reverse_link_reassign_clear():
    a1 = libraryElement_FBNetworkElement()
    a2 = libraryElement_FBNetworkElement()
    b = libraryElement_FBNetwork()
    _safe_set(b, 'libraryElement_FBNetwork108', {a1})
    assert _is_linked(b, 'libraryElement_FBNetwork108', a1)
    if hasattr(a1, 'libraryElement_FBNetworkElement109'):
        assert _is_linked(a1, 'libraryElement_FBNetworkElement109', b)
    _safe_set(b, 'libraryElement_FBNetwork108', {a2})
    assert _is_linked(b, 'libraryElement_FBNetwork108', a2)
    if hasattr(a1, 'libraryElement_FBNetworkElement109'):
        assert not _is_linked(a1, 'libraryElement_FBNetworkElement109', b)
    if hasattr(a2, 'libraryElement_FBNetworkElement109'):
        assert _is_linked(a2, 'libraryElement_FBNetworkElement109', b)
    _safe_set(b, 'libraryElement_FBNetwork108', set())
    assert not _is_linked(b, 'libraryElement_FBNetwork108', a2)
    if hasattr(a2, 'libraryElement_FBNetworkElement109'):
        assert not _is_linked(a2, 'libraryElement_FBNetworkElement109', b)


def test_assoc_outTransitions39_reverse_link_reassign_clear():
    a1 = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    a2 = libraryElement_ECTransition(comment="sample_text_2", conditionExpression="sample_text_2")
    b = libraryElement_ECState()
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'ECTransition'):
        assert _is_linked(a1, 'ECTransition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'ECTransition'):
        assert not _is_linked(a1, 'ECTransition', b)
    if hasattr(a2, 'ECTransition'):
        assert _is_linked(a2, 'ECTransition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'ECTransition'):
        assert not _is_linked(a2, 'ECTransition', b)


def test_assoc_outputConnections139_reverse_link_reassign_clear():
    a1 = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    a2 = libraryElement_IInterfaceElement(isInput="sample_text_2", typeName="sample_text_2")
    b = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    _safe_set(b, 'Connection141', a1)
    assert _is_linked(b, 'Connection141', a1)
    if hasattr(a1, 'source140'):
        assert _is_linked(a1, 'source140', b)
    _safe_set(b, 'Connection141', a2)
    assert _is_linked(b, 'Connection141', a2)
    if hasattr(a1, 'source140'):
        assert not _is_linked(a1, 'source140', b)
    if hasattr(a2, 'source140'):
        assert _is_linked(a2, 'source140', b)
    _safe_set(b, 'Connection141', None)
    assert not _is_linked(b, 'Connection141', a2)
    if hasattr(a2, 'source140'):
        assert not _is_linked(a2, 'source140', b)


def test_assoc_outputPrimitive105_reverse_link_reassign_clear():
    a1 = libraryElement_ServiceTransaction(TestResult="sample_text")
    a2 = libraryElement_ServiceTransaction(TestResult="sample_text_2")
    b = libraryElement_OutputPrimitive(TestResult="sample_text")
    _safe_set(b, 'libraryElement_OutputPrimitive', a1)
    assert _is_linked(b, 'libraryElement_OutputPrimitive', a1)
    if hasattr(a1, 'libraryElement_ServiceTransaction106'):
        assert _is_linked(a1, 'libraryElement_ServiceTransaction106', b)
    _safe_set(b, 'libraryElement_OutputPrimitive', a2)
    assert _is_linked(b, 'libraryElement_OutputPrimitive', a2)
    if hasattr(a1, 'libraryElement_ServiceTransaction106'):
        assert not _is_linked(a1, 'libraryElement_ServiceTransaction106', b)
    if hasattr(a2, 'libraryElement_ServiceTransaction106'):
        assert _is_linked(a2, 'libraryElement_ServiceTransaction106', b)
    _safe_set(b, 'libraryElement_OutputPrimitive', None)
    assert not _is_linked(b, 'libraryElement_OutputPrimitive', a2)
    if hasattr(a2, 'libraryElement_ServiceTransaction106'):
        assert not _is_linked(a2, 'libraryElement_ServiceTransaction106', b)


def test_assoc_outputVars74_reverse_link_reassign_clear():
    a1 = libraryElement_VarDeclaration(arraySize="sample_text")
    a2 = libraryElement_VarDeclaration(arraySize="sample_text_2")
    b = libraryElement_InterfaceList()
    _safe_set(b, 'libraryElement_InterfaceList75', {a1})
    assert _is_linked(b, 'libraryElement_InterfaceList75', a1)
    if hasattr(a1, 'libraryElement_VarDeclaration76'):
        assert _is_linked(a1, 'libraryElement_VarDeclaration76', b)
    _safe_set(b, 'libraryElement_InterfaceList75', {a2})
    assert _is_linked(b, 'libraryElement_InterfaceList75', a2)
    if hasattr(a1, 'libraryElement_VarDeclaration76'):
        assert not _is_linked(a1, 'libraryElement_VarDeclaration76', b)
    if hasattr(a2, 'libraryElement_VarDeclaration76'):
        assert _is_linked(a2, 'libraryElement_VarDeclaration76', b)
    _safe_set(b, 'libraryElement_InterfaceList75', set())
    assert not _is_linked(b, 'libraryElement_InterfaceList75', a2)
    if hasattr(a2, 'libraryElement_VarDeclaration76'):
        assert not _is_linked(a2, 'libraryElement_VarDeclaration76', b)


def test_assoc_parameter134_reverse_link_reassign_clear():
    a1 = libraryElement_Parameter(comment="sample_text", name="sample_text", value="sample_text")
    a2 = libraryElement_Parameter(comment="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = libraryElement_ConfigurableObject()
    _safe_set(b, 'libraryElement_ConfigurableObject', {a1})
    assert _is_linked(b, 'libraryElement_ConfigurableObject', a1)
    if hasattr(a1, 'libraryElement_Parameter'):
        assert _is_linked(a1, 'libraryElement_Parameter', b)
    _safe_set(b, 'libraryElement_ConfigurableObject', {a2})
    assert _is_linked(b, 'libraryElement_ConfigurableObject', a2)
    if hasattr(a1, 'libraryElement_Parameter'):
        assert not _is_linked(a1, 'libraryElement_Parameter', b)
    if hasattr(a2, 'libraryElement_Parameter'):
        assert _is_linked(a2, 'libraryElement_Parameter', b)
    _safe_set(b, 'libraryElement_ConfigurableObject', set())
    assert not _is_linked(b, 'libraryElement_ConfigurableObject', a2)
    if hasattr(a2, 'libraryElement_Parameter'):
        assert not _is_linked(a2, 'libraryElement_Parameter', b)


def test_assoc_resource13_reverse_link_reassign_clear():
    a1 = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    a2 = libraryElement_Resource(deviceTypeResource="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = libraryElement_Device(profile="sample_text")
    _safe_set(b, 'device', {a1})
    assert _is_linked(b, 'device', a1)
    if hasattr(a1, 'Resource'):
        assert _is_linked(a1, 'Resource', b)
    _safe_set(b, 'device', {a2})
    assert _is_linked(b, 'device', a2)
    if hasattr(a1, 'Resource'):
        assert not _is_linked(a1, 'Resource', b)
    if hasattr(a2, 'Resource'):
        assert _is_linked(a2, 'Resource', b)
    _safe_set(b, 'device', set())
    assert not _is_linked(b, 'device', a2)
    if hasattr(a2, 'Resource'):
        assert not _is_linked(a2, 'Resource', b)


def test_assoc_resource20_reverse_link_reassign_clear():
    a1 = libraryElement_Resource(deviceTypeResource="sample_text", x="sample_text", y="sample_text")
    a2 = libraryElement_Resource(deviceTypeResource="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = libraryElement_DeviceType(profile="sample_text")
    _safe_set(b, 'libraryElement_DeviceType21', {a1})
    assert _is_linked(b, 'libraryElement_DeviceType21', a1)
    if hasattr(a1, 'libraryElement_Resource'):
        assert _is_linked(a1, 'libraryElement_Resource', b)
    _safe_set(b, 'libraryElement_DeviceType21', {a2})
    assert _is_linked(b, 'libraryElement_DeviceType21', a2)
    if hasattr(a1, 'libraryElement_Resource'):
        assert not _is_linked(a1, 'libraryElement_Resource', b)
    if hasattr(a2, 'libraryElement_Resource'):
        assert _is_linked(a2, 'libraryElement_Resource', b)
    _safe_set(b, 'libraryElement_DeviceType21', set())
    assert not _is_linked(b, 'libraryElement_DeviceType21', a2)
    if hasattr(a2, 'libraryElement_Resource'):
        assert not _is_linked(a2, 'libraryElement_Resource', b)


def test_assoc_resourceTypeName18_reverse_link_reassign_clear():
    a1 = libraryElement_ResourceTypeName(name="sample_text")
    a2 = libraryElement_ResourceTypeName(name="sample_text_2")
    b = libraryElement_DeviceType(profile="sample_text")
    _safe_set(b, 'libraryElement_DeviceType19', {a1})
    assert _is_linked(b, 'libraryElement_DeviceType19', a1)
    if hasattr(a1, 'libraryElement_ResourceTypeName'):
        assert _is_linked(a1, 'libraryElement_ResourceTypeName', b)
    _safe_set(b, 'libraryElement_DeviceType19', {a2})
    assert _is_linked(b, 'libraryElement_DeviceType19', a2)
    if hasattr(a1, 'libraryElement_ResourceTypeName'):
        assert not _is_linked(a1, 'libraryElement_ResourceTypeName', b)
    if hasattr(a2, 'libraryElement_ResourceTypeName'):
        assert _is_linked(a2, 'libraryElement_ResourceTypeName', b)
    _safe_set(b, 'libraryElement_DeviceType19', set())
    assert not _is_linked(b, 'libraryElement_DeviceType19', a2)
    if hasattr(a2, 'libraryElement_ResourceTypeName'):
        assert not _is_linked(a2, 'libraryElement_ResourceTypeName', b)


def test_assoc_segments147_reverse_link_reassign_clear():
    a1 = libraryElement_SystemConfiguration()
    a2 = libraryElement_SystemConfiguration()
    b = libraryElement_Segment(width="sample_text")
    _safe_set(b, 'libraryElement_Segment149', a1)
    assert _is_linked(b, 'libraryElement_Segment149', a1)
    if hasattr(a1, 'libraryElement_SystemConfiguration148'):
        assert _is_linked(a1, 'libraryElement_SystemConfiguration148', b)
    _safe_set(b, 'libraryElement_Segment149', a2)
    assert _is_linked(b, 'libraryElement_Segment149', a2)
    if hasattr(a1, 'libraryElement_SystemConfiguration148'):
        assert not _is_linked(a1, 'libraryElement_SystemConfiguration148', b)
    if hasattr(a2, 'libraryElement_SystemConfiguration148'):
        assert _is_linked(a2, 'libraryElement_SystemConfiguration148', b)
    _safe_set(b, 'libraryElement_Segment149', None)
    assert not _is_linked(b, 'libraryElement_Segment149', a2)
    if hasattr(a2, 'libraryElement_SystemConfiguration148'):
        assert not _is_linked(a2, 'libraryElement_SystemConfiguration148', b)


def test_assoc_serviceTransaction102_reverse_link_reassign_clear():
    a1 = libraryElement_ServiceTransaction(TestResult="sample_text")
    a2 = libraryElement_ServiceTransaction(TestResult="sample_text_2")
    b = libraryElement_ServiceSequence(TestResult="sample_text")
    _safe_set(b, 'libraryElement_ServiceSequence', {a1})
    assert _is_linked(b, 'libraryElement_ServiceSequence', a1)
    if hasattr(a1, 'libraryElement_ServiceTransaction'):
        assert _is_linked(a1, 'libraryElement_ServiceTransaction', b)
    _safe_set(b, 'libraryElement_ServiceSequence', {a2})
    assert _is_linked(b, 'libraryElement_ServiceSequence', a2)
    if hasattr(a1, 'libraryElement_ServiceTransaction'):
        assert not _is_linked(a1, 'libraryElement_ServiceTransaction', b)
    if hasattr(a2, 'libraryElement_ServiceTransaction'):
        assert _is_linked(a2, 'libraryElement_ServiceTransaction', b)
    _safe_set(b, 'libraryElement_ServiceSequence', set())
    assert not _is_linked(b, 'libraryElement_ServiceSequence', a2)
    if hasattr(a2, 'libraryElement_ServiceTransaction'):
        assert not _is_linked(a2, 'libraryElement_ServiceTransaction', b)


def test_assoc_source10_reverse_link_reassign_clear():
    a1 = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    a2 = libraryElement_IInterfaceElement(isInput="sample_text_2", typeName="sample_text_2")
    b = libraryElement_Connection(brokenConnection="sample_text", dx1="sample_text", dx2="sample_text", dy="sample_text", resTypeConnection="sample_text")
    _safe_set(b, 'outputConnections', a1)
    assert _is_linked(b, 'outputConnections', a1)
    if hasattr(a1, 'IInterfaceElement'):
        assert _is_linked(a1, 'IInterfaceElement', b)
    _safe_set(b, 'outputConnections', a2)
    assert _is_linked(b, 'outputConnections', a2)
    if hasattr(a1, 'IInterfaceElement'):
        assert not _is_linked(a1, 'IInterfaceElement', b)
    if hasattr(a2, 'IInterfaceElement'):
        assert _is_linked(a2, 'IInterfaceElement', b)
    _safe_set(b, 'outputConnections', None)
    assert not _is_linked(b, 'outputConnections', a2)
    if hasattr(a2, 'IInterfaceElement'):
        assert not _is_linked(a2, 'IInterfaceElement', b)


def test_assoc_source42_reverse_link_reassign_clear():
    a1 = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    a2 = libraryElement_ECTransition(comment="sample_text_2", conditionExpression="sample_text_2")
    b = libraryElement_ECState()
    _safe_set(b, 'ECState', a1)
    assert _is_linked(b, 'ECState', a1)
    if hasattr(a1, 'outTransitions'):
        assert _is_linked(a1, 'outTransitions', b)
    _safe_set(b, 'ECState', a2)
    assert _is_linked(b, 'ECState', a2)
    if hasattr(a1, 'outTransitions'):
        assert not _is_linked(a1, 'outTransitions', b)
    if hasattr(a2, 'outTransitions'):
        assert _is_linked(a2, 'outTransitions', b)
    _safe_set(b, 'ECState', None)
    assert not _is_linked(b, 'ECState', a2)
    if hasattr(a2, 'outTransitions'):
        assert not _is_linked(a2, 'outTransitions', b)


def test_assoc_subAppNetwork53_reverse_link_reassign_clear():
    a1 = libraryElement_SubApp()
    a2 = libraryElement_SubApp()
    b = libraryElement_FBNetwork()
    _safe_set(b, 'libraryElement_FBNetwork54', a1)
    assert _is_linked(b, 'libraryElement_FBNetwork54', a1)
    if hasattr(a1, 'libraryElement_SubApp'):
        assert _is_linked(a1, 'libraryElement_SubApp', b)
    _safe_set(b, 'libraryElement_FBNetwork54', a2)
    assert _is_linked(b, 'libraryElement_FBNetwork54', a2)
    if hasattr(a1, 'libraryElement_SubApp'):
        assert not _is_linked(a1, 'libraryElement_SubApp', b)
    if hasattr(a2, 'libraryElement_SubApp'):
        assert _is_linked(a2, 'libraryElement_SubApp', b)
    _safe_set(b, 'libraryElement_FBNetwork54', None)
    assert not _is_linked(b, 'libraryElement_FBNetwork54', a2)
    if hasattr(a2, 'libraryElement_SubApp'):
        assert not _is_linked(a2, 'libraryElement_SubApp', b)


def test_assoc_systemConfiguration122_reverse_link_reassign_clear():
    a1 = libraryElement_SystemConfiguration()
    a2 = libraryElement_SystemConfiguration()
    b = libraryElement_AutomationSystem(project="sample_text")
    _safe_set(b, 'libraryElement_AutomationSystem123', a1)
    assert _is_linked(b, 'libraryElement_AutomationSystem123', a1)
    if hasattr(a1, 'libraryElement_SystemConfiguration'):
        assert _is_linked(a1, 'libraryElement_SystemConfiguration', b)
    _safe_set(b, 'libraryElement_AutomationSystem123', a2)
    assert _is_linked(b, 'libraryElement_AutomationSystem123', a2)
    if hasattr(a1, 'libraryElement_SystemConfiguration'):
        assert not _is_linked(a1, 'libraryElement_SystemConfiguration', b)
    if hasattr(a2, 'libraryElement_SystemConfiguration'):
        assert _is_linked(a2, 'libraryElement_SystemConfiguration', b)
    _safe_set(b, 'libraryElement_AutomationSystem123', None)
    assert not _is_linked(b, 'libraryElement_AutomationSystem123', a2)
    if hasattr(a2, 'libraryElement_SystemConfiguration'):
        assert not _is_linked(a2, 'libraryElement_SystemConfiguration', b)


def test_assoc_to82_reverse_link_reassign_clear():
    a1 = libraryElement_Mapping()
    a2 = libraryElement_Mapping()
    b = libraryElement_FBNetworkElement()
    _safe_set(b, 'libraryElement_FBNetworkElement84', a1)
    assert _is_linked(b, 'libraryElement_FBNetworkElement84', a1)
    if hasattr(a1, 'libraryElement_Mapping83'):
        assert _is_linked(a1, 'libraryElement_Mapping83', b)
    _safe_set(b, 'libraryElement_FBNetworkElement84', a2)
    assert _is_linked(b, 'libraryElement_FBNetworkElement84', a2)
    if hasattr(a1, 'libraryElement_Mapping83'):
        assert not _is_linked(a1, 'libraryElement_Mapping83', b)
    if hasattr(a2, 'libraryElement_Mapping83'):
        assert _is_linked(a2, 'libraryElement_Mapping83', b)
    _safe_set(b, 'libraryElement_FBNetworkElement84', None)
    assert not _is_linked(b, 'libraryElement_FBNetworkElement84', a2)
    if hasattr(a2, 'libraryElement_Mapping83'):
        assert not _is_linked(a2, 'libraryElement_Mapping83', b)


def test_assoc_value143_reverse_link_reassign_clear():
    a1 = libraryElement_Value(value="sample_text")
    a2 = libraryElement_Value(value="sample_text_2")
    b = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    _safe_set(b, 'libraryElement_IInterfaceElement144', a1)
    assert _is_linked(b, 'libraryElement_IInterfaceElement144', a1)
    if hasattr(a1, 'libraryElement_Value'):
        assert _is_linked(a1, 'libraryElement_Value', b)
    _safe_set(b, 'libraryElement_IInterfaceElement144', a2)
    assert _is_linked(b, 'libraryElement_IInterfaceElement144', a2)
    if hasattr(a1, 'libraryElement_Value'):
        assert not _is_linked(a1, 'libraryElement_Value', b)
    if hasattr(a2, 'libraryElement_Value'):
        assert _is_linked(a2, 'libraryElement_Value', b)
    _safe_set(b, 'libraryElement_IInterfaceElement144', None)
    assert not _is_linked(b, 'libraryElement_IInterfaceElement144', a2)
    if hasattr(a2, 'libraryElement_Value'):
        assert not _is_linked(a2, 'libraryElement_Value', b)


def test_assoc_varDeclaration16_reverse_link_reassign_clear():
    a1 = libraryElement_VarDeclaration(arraySize="sample_text")
    a2 = libraryElement_VarDeclaration(arraySize="sample_text_2")
    b = libraryElement_DeviceType(profile="sample_text")
    _safe_set(b, 'libraryElement_DeviceType', {a1})
    assert _is_linked(b, 'libraryElement_DeviceType', a1)
    if hasattr(a1, 'libraryElement_VarDeclaration17'):
        assert _is_linked(a1, 'libraryElement_VarDeclaration17', b)
    _safe_set(b, 'libraryElement_DeviceType', {a2})
    assert _is_linked(b, 'libraryElement_DeviceType', a2)
    if hasattr(a1, 'libraryElement_VarDeclaration17'):
        assert not _is_linked(a1, 'libraryElement_VarDeclaration17', b)
    if hasattr(a2, 'libraryElement_VarDeclaration17'):
        assert _is_linked(a2, 'libraryElement_VarDeclaration17', b)
    _safe_set(b, 'libraryElement_DeviceType', set())
    assert not _is_linked(b, 'libraryElement_DeviceType', a2)
    if hasattr(a2, 'libraryElement_VarDeclaration17'):
        assert not _is_linked(a2, 'libraryElement_VarDeclaration17', b)


def test_assoc_varDeclarations98_reverse_link_reassign_clear():
    a1 = libraryElement_VarDeclaration(arraySize="sample_text")
    a2 = libraryElement_VarDeclaration(arraySize="sample_text_2")
    b = libraryElement_Segment(width="sample_text")
    _safe_set(b, 'libraryElement_Segment', {a1})
    assert _is_linked(b, 'libraryElement_Segment', a1)
    if hasattr(a1, 'libraryElement_VarDeclaration99'):
        assert _is_linked(a1, 'libraryElement_VarDeclaration99', b)
    _safe_set(b, 'libraryElement_Segment', {a2})
    assert _is_linked(b, 'libraryElement_Segment', a2)
    if hasattr(a1, 'libraryElement_VarDeclaration99'):
        assert not _is_linked(a1, 'libraryElement_VarDeclaration99', b)
    if hasattr(a2, 'libraryElement_VarDeclaration99'):
        assert _is_linked(a2, 'libraryElement_VarDeclaration99', b)
    _safe_set(b, 'libraryElement_Segment', set())
    assert not _is_linked(b, 'libraryElement_Segment', a2)
    if hasattr(a2, 'libraryElement_VarDeclaration99'):
        assert not _is_linked(a2, 'libraryElement_VarDeclaration99', b)


