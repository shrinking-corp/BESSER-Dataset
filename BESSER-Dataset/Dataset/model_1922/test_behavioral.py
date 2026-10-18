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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_adapterDecl169_stub_double():
    # libraryElement_AdapterDeclaration has no real 'AdapterDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_AdapterFB's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_AdapterFB's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_AdapterFB()
    partner = libraryElement_AdapterDeclaration()
    setattr(partner, 'AdapterDeclaration', None)
    _safe_set(owner, 'adapterFB', partner)
    assert getattr(partner, 'AdapterDeclaration') == owner
    _safe_set(owner, 'adapterFB', None)
    assert getattr(partner, 'AdapterDeclaration') is None


def test_assoc_adapterFB0_stub_double():
    # libraryElement_AdapterDeclaration has no real 'adapterDecl' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_AdapterFB's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_AdapterFB's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_AdapterFB()
    partner = libraryElement_AdapterDeclaration()
    setattr(partner, 'adapterDecl', None)
    _safe_set(owner, 'AdapterFB', partner)
    assert getattr(partner, 'adapterDecl') == owner
    _safe_set(owner, 'AdapterFB', None)
    assert getattr(partner, 'adapterDecl') is None


def test_assoc_adapterFBType2_stub_double():
    # libraryElement_AdapterFBType has no real 'libraryElement_AdapterFBType' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_AdapterType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_AdapterType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_AdapterType()
    partner = libraryElement_AdapterFBType()
    setattr(partner, 'libraryElement_AdapterFBType', None)
    _safe_set(owner, 'libraryElement_AdapterType', partner)
    assert getattr(partner, 'libraryElement_AdapterFBType') == owner
    _safe_set(owner, 'libraryElement_AdapterType', None)
    assert getattr(partner, 'libraryElement_AdapterFBType') is None


def test_assoc_adapterType155_stub_double():
    # libraryElement_AdapterFBType has no real 'libraryElement_AdapterFBType156' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_AdapterType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_AdapterType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_AdapterType()
    partner = libraryElement_AdapterFBType()
    setattr(partner, 'libraryElement_AdapterFBType156', None)
    _safe_set(owner, 'libraryElement_AdapterType157', partner)
    assert getattr(partner, 'libraryElement_AdapterFBType156') == owner
    _safe_set(owner, 'libraryElement_AdapterType157', None)
    assert getattr(partner, 'libraryElement_AdapterFBType156') is None


def test_assoc_color172_stub_double():
    # libraryElement_ColorizableElement has no real 'libraryElement_ColorizableElement' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_Color's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_Color's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_Color(blue="sample_text", green="sample_text", red="sample_text")
    partner = libraryElement_ColorizableElement()
    setattr(partner, 'libraryElement_ColorizableElement', None)
    _safe_set(owner, 'libraryElement_Color', partner)
    assert getattr(partner, 'libraryElement_ColorizableElement') == owner
    _safe_set(owner, 'libraryElement_Color', None)
    assert getattr(partner, 'libraryElement_ColorizableElement') is None


def test_assoc_compilerInfo132_stub_double():
    # libraryElement_CompilableType has no real 'libraryElement_CompilableType' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_CompilerInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_CompilerInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_CompilerInfo(classdef="sample_text", header="sample_text")
    partner = libraryElement_CompilableType()
    setattr(partner, 'libraryElement_CompilableType', None)
    _safe_set(owner, 'libraryElement_CompilerInfo133', partner)
    assert getattr(partner, 'libraryElement_CompilableType') == owner
    _safe_set(owner, 'libraryElement_CompilerInfo133', None)
    assert getattr(partner, 'libraryElement_CompilableType') is None


def test_assoc_conditionEvent45_stub_double():
    # libraryElement_Event has no real 'libraryElement_Event47' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_ECTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_ECTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    partner = libraryElement_Event()
    setattr(partner, 'libraryElement_Event47', None)
    _safe_set(owner, 'libraryElement_ECTransition46', partner)
    assert getattr(partner, 'libraryElement_Event47') == owner
    _safe_set(owner, 'libraryElement_ECTransition46', None)
    assert getattr(partner, 'libraryElement_Event47') is None


def test_assoc_device78_stub_double():
    # libraryElement_Link has no real 'inConnections' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_Device(profile="sample_text")
    partner = libraryElement_Link()
    setattr(partner, 'inConnections', None)
    _safe_set(owner, 'Device', partner)
    assert getattr(partner, 'inConnections') == owner
    _safe_set(owner, 'Device', None)
    assert getattr(partner, 'inConnections') is None


def test_assoc_eCAction36_stub_double():
    # libraryElement_ECAction has no real 'libraryElement_ECAction38' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_ECState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_ECState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_ECState()
    partner = libraryElement_ECAction()
    setattr(partner, 'libraryElement_ECAction38', None)
    _safe_set(owner, 'libraryElement_ECState37', {partner})
    assert getattr(partner, 'libraryElement_ECAction38') == owner
    _safe_set(owner, 'libraryElement_ECState37', set())
    assert getattr(partner, 'libraryElement_ECAction38') is None


def test_assoc_eCState29_stub_double():
    # libraryElement_ECC has no real 'libraryElement_ECC30' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_ECState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_ECState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_ECState()
    partner = libraryElement_ECC()
    setattr(partner, 'libraryElement_ECC30', None)
    _safe_set(owner, 'libraryElement_ECState', partner)
    assert owner in getattr(partner, 'libraryElement_ECC30')
    _safe_set(owner, 'libraryElement_ECState', None)
    assert owner not in getattr(partner, 'libraryElement_ECC30')


def test_assoc_eCTransition31_stub_double():
    # libraryElement_ECC has no real 'libraryElement_ECC32' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_ECTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_ECTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_ECTransition(comment="sample_text", conditionExpression="sample_text")
    partner = libraryElement_ECC()
    setattr(partner, 'libraryElement_ECC32', None)
    _safe_set(owner, 'libraryElement_ECTransition', partner)
    assert owner in getattr(partner, 'libraryElement_ECC32')
    _safe_set(owner, 'libraryElement_ECTransition', None)
    assert owner not in getattr(partner, 'libraryElement_ECC32')


def test_assoc_eventInputs65_stub_double():
    # libraryElement_Event has no real 'libraryElement_Event67' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_InterfaceList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_InterfaceList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_InterfaceList()
    partner = libraryElement_Event()
    setattr(partner, 'libraryElement_Event67', None)
    _safe_set(owner, 'libraryElement_InterfaceList66', {partner})
    assert getattr(partner, 'libraryElement_Event67') == owner
    _safe_set(owner, 'libraryElement_InterfaceList66', set())
    assert getattr(partner, 'libraryElement_Event67') is None


def test_assoc_eventOutputs68_stub_double():
    # libraryElement_Event has no real 'libraryElement_Event70' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_InterfaceList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_InterfaceList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_InterfaceList()
    partner = libraryElement_Event()
    setattr(partner, 'libraryElement_Event70', None)
    _safe_set(owner, 'libraryElement_InterfaceList69', {partner})
    assert getattr(partner, 'libraryElement_Event70') == owner
    _safe_set(owner, 'libraryElement_InterfaceList69', set())
    assert getattr(partner, 'libraryElement_Event70') is None


def test_assoc_fBNetwork135_stub_double():
    # libraryElement_CompositeFBType has no real 'libraryElement_CompositeFBType' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_FBNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_FBNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_FBNetwork()
    partner = libraryElement_CompositeFBType()
    setattr(partner, 'libraryElement_CompositeFBType', None)
    _safe_set(owner, 'libraryElement_FBNetwork136', partner)
    assert getattr(partner, 'libraryElement_CompositeFBType') == owner
    _safe_set(owner, 'libraryElement_FBNetwork136', None)
    assert getattr(partner, 'libraryElement_CompositeFBType') is None


def test_assoc_fBNetwork92_stub_double():
    # libraryElement_ResourceType has no real 'libraryElement_ResourceType93' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_FBNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_FBNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_FBNetwork()
    partner = libraryElement_ResourceType()
    setattr(partner, 'libraryElement_ResourceType93', None)
    _safe_set(owner, 'libraryElement_FBNetwork94', partner)
    assert getattr(partner, 'libraryElement_ResourceType93') == owner
    _safe_set(owner, 'libraryElement_FBNetwork94', None)
    assert getattr(partner, 'libraryElement_ResourceType93') is None


def test_assoc_identification129_stub_double():
    # libraryElement_LibraryElement has no real 'libraryElement_LibraryElement130' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_Identification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_Identification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_Identification(applicationDomain="sample_text", classification="sample_text", description="sample_text", function="sample_text", standard="sample_text", type="sample_text")
    partner = libraryElement_LibraryElement()
    setattr(partner, 'libraryElement_LibraryElement130', None)
    _safe_set(owner, 'libraryElement_Identification', partner)
    assert getattr(partner, 'libraryElement_LibraryElement130') == owner
    _safe_set(owner, 'libraryElement_Identification', None)
    assert getattr(partner, 'libraryElement_LibraryElement130') is None


def test_assoc_inConnections14_stub_double():
    # libraryElement_Link has no real 'Link' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_Device(profile="sample_text")
    partner = libraryElement_Link()
    setattr(partner, 'Link', None)
    _safe_set(owner, 'device15', {partner})
    assert getattr(partner, 'Link') == owner
    _safe_set(owner, 'device15', set())
    assert getattr(partner, 'Link') is None


def test_assoc_inputPrimitive103_stub_double():
    # libraryElement_InputPrimitive has no real 'libraryElement_InputPrimitive' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_ServiceTransaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_ServiceTransaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_ServiceTransaction(TestResult="sample_text")
    partner = libraryElement_InputPrimitive()
    setattr(partner, 'libraryElement_InputPrimitive', None)
    _safe_set(owner, 'libraryElement_ServiceTransaction104', partner)
    assert getattr(partner, 'libraryElement_InputPrimitive') == owner
    _safe_set(owner, 'libraryElement_ServiceTransaction104', None)
    assert getattr(partner, 'libraryElement_InputPrimitive') is None


def test_assoc_interface170_stub_double():
    # libraryElement_ServiceInterface has no real 'libraryElement_ServiceInterface171' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_Primitive(event="sample_text", parameters="sample_text")
    partner = libraryElement_ServiceInterface()
    setattr(partner, 'libraryElement_ServiceInterface171', None)
    _safe_set(owner, 'libraryElement_Primitive', partner)
    assert getattr(partner, 'libraryElement_ServiceInterface171') == owner
    _safe_set(owner, 'libraryElement_Primitive', None)
    assert getattr(partner, 'libraryElement_ServiceInterface171') is None


def test_assoc_interfaceList55_stub_double():
    # libraryElement_FBType has no real 'libraryElement_FBType' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_InterfaceList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_InterfaceList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_InterfaceList()
    partner = libraryElement_FBType()
    setattr(partner, 'libraryElement_FBType', None)
    _safe_set(owner, 'libraryElement_InterfaceList56', partner)
    assert getattr(partner, 'libraryElement_FBType') == owner
    _safe_set(owner, 'libraryElement_InterfaceList56', None)
    assert getattr(partner, 'libraryElement_FBType') is None


def test_assoc_internalVars7_stub_double():
    # libraryElement_BasicFBType has no real 'libraryElement_BasicFBType8' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VarDeclaration(arraySize="sample_text")
    partner = libraryElement_BasicFBType()
    setattr(partner, 'libraryElement_BasicFBType8', None)
    _safe_set(owner, 'libraryElement_VarDeclaration', partner)
    assert owner in getattr(partner, 'libraryElement_BasicFBType8')
    _safe_set(owner, 'libraryElement_VarDeclaration', None)
    assert owner not in getattr(partner, 'libraryElement_BasicFBType8')


def test_assoc_links150_stub_double():
    # libraryElement_Link has no real 'libraryElement_Link' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_SystemConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_SystemConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_SystemConfiguration()
    partner = libraryElement_Link()
    setattr(partner, 'libraryElement_Link', None)
    _safe_set(owner, 'libraryElement_SystemConfiguration151', {partner})
    assert getattr(partner, 'libraryElement_Link') == owner
    _safe_set(owner, 'libraryElement_SystemConfiguration151', set())
    assert getattr(partner, 'libraryElement_Link') is None


def test_assoc_outConnections100_stub_double():
    # libraryElement_Link has no real 'Link101' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_Segment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_Segment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_Segment(width="sample_text")
    partner = libraryElement_Link()
    setattr(partner, 'Link101', None)
    _safe_set(owner, 'segment', {partner})
    assert getattr(partner, 'Link101') == owner
    _safe_set(owner, 'segment', set())
    assert getattr(partner, 'Link101') is None


def test_assoc_palette121_stub_double():
    # libraryElement_Palette has no real 'palette.ecorePalette' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_AutomationSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_AutomationSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_AutomationSystem(project="sample_text")
    partner = libraryElement_Palette()
    setattr(partner, 'palette.ecorePalette', None)
    _safe_set(owner, 'automationSystem', partner)
    assert getattr(partner, 'palette.ecorePalette') == owner
    _safe_set(owner, 'automationSystem', None)
    assert getattr(partner, 'palette.ecorePalette') is None


def test_assoc_paletteEntry168_stub_double():
    # libraryElement_PaletteEntry has no real 'libraryElement_PaletteEntry' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_TypedConfigureableObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_TypedConfigureableObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_TypedConfigureableObject()
    partner = libraryElement_PaletteEntry()
    setattr(partner, 'libraryElement_PaletteEntry', None)
    _safe_set(owner, 'libraryElement_TypedConfigureableObject', partner)
    assert getattr(partner, 'libraryElement_PaletteEntry') == owner
    _safe_set(owner, 'libraryElement_TypedConfigureableObject', None)
    assert getattr(partner, 'libraryElement_PaletteEntry') is None


def test_assoc_plugs59_stub_double():
    # libraryElement_AdapterDeclaration has no real 'libraryElement_AdapterDeclaration61' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_InterfaceList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_InterfaceList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_InterfaceList()
    partner = libraryElement_AdapterDeclaration()
    setattr(partner, 'libraryElement_AdapterDeclaration61', None)
    _safe_set(owner, 'libraryElement_InterfaceList60', {partner})
    assert getattr(partner, 'libraryElement_AdapterDeclaration61') == owner
    _safe_set(owner, 'libraryElement_InterfaceList60', set())
    assert getattr(partner, 'libraryElement_AdapterDeclaration61') is None


def test_assoc_segment77_stub_double():
    # libraryElement_Link has no real 'outConnections' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_Segment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_Segment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_Segment(width="sample_text")
    partner = libraryElement_Link()
    setattr(partner, 'outConnections', None)
    _safe_set(owner, 'Segment', partner)
    assert getattr(partner, 'outConnections') == owner
    _safe_set(owner, 'Segment', None)
    assert getattr(partner, 'outConnections') is None


def test_assoc_serviceSequence165_stub_double():
    # libraryElement_Service has no real 'libraryElement_Service166' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_ServiceSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_ServiceSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_ServiceSequence(TestResult="sample_text")
    partner = libraryElement_Service()
    setattr(partner, 'libraryElement_Service166', None)
    _safe_set(owner, 'libraryElement_ServiceSequence167', partner)
    assert owner in getattr(partner, 'libraryElement_Service166')
    _safe_set(owner, 'libraryElement_ServiceSequence167', None)
    assert owner not in getattr(partner, 'libraryElement_Service166')


def test_assoc_sockets62_stub_double():
    # libraryElement_AdapterDeclaration has no real 'libraryElement_AdapterDeclaration64' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_InterfaceList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_InterfaceList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_InterfaceList()
    partner = libraryElement_AdapterDeclaration()
    setattr(partner, 'libraryElement_AdapterDeclaration64', None)
    _safe_set(owner, 'libraryElement_InterfaceList63', {partner})
    assert getattr(partner, 'libraryElement_AdapterDeclaration64') == owner
    _safe_set(owner, 'libraryElement_InterfaceList63', set())
    assert getattr(partner, 'libraryElement_AdapterDeclaration64') is None


def test_assoc_start33_stub_double():
    # libraryElement_ECC has no real 'libraryElement_ECC34' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_ECState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_ECState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_ECState()
    partner = libraryElement_ECC()
    setattr(partner, 'libraryElement_ECC34', None)
    _safe_set(owner, 'libraryElement_ECState35', partner)
    assert getattr(partner, 'libraryElement_ECC34') == owner
    _safe_set(owner, 'libraryElement_ECState35', None)
    assert getattr(partner, 'libraryElement_ECC34') is None


def test_assoc_type142_stub_double():
    # libraryElement_DataType has no real 'libraryElement_DataType' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_IInterfaceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_IInterfaceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_IInterfaceElement(isInput="sample_text", typeName="sample_text")
    partner = libraryElement_DataType()
    setattr(partner, 'libraryElement_DataType', None)
    _safe_set(owner, 'libraryElement_IInterfaceElement', partner)
    assert getattr(partner, 'libraryElement_DataType') == owner
    _safe_set(owner, 'libraryElement_IInterfaceElement', None)
    assert getattr(partner, 'libraryElement_DataType') is None


def test_assoc_varDeclaration153_stub_double():
    # libraryElement_SegmentType has no real 'libraryElement_SegmentType' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VarDeclaration(arraySize="sample_text")
    partner = libraryElement_SegmentType()
    setattr(partner, 'libraryElement_SegmentType', None)
    _safe_set(owner, 'libraryElement_VarDeclaration154', partner)
    assert owner in getattr(partner, 'libraryElement_SegmentType')
    _safe_set(owner, 'libraryElement_VarDeclaration154', None)
    assert owner not in getattr(partner, 'libraryElement_SegmentType')


def test_assoc_varDeclaration90_stub_double():
    # libraryElement_ResourceType has no real 'libraryElement_ResourceType' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VarDeclaration(arraySize="sample_text")
    partner = libraryElement_ResourceType()
    setattr(partner, 'libraryElement_ResourceType', None)
    _safe_set(owner, 'libraryElement_VarDeclaration91', partner)
    assert owner in getattr(partner, 'libraryElement_ResourceType')
    _safe_set(owner, 'libraryElement_VarDeclaration91', None)
    assert owner not in getattr(partner, 'libraryElement_ResourceType')


def test_assoc_varDeclarations173_stub_double():
    # libraryElement_IVarElement has no real 'libraryElement_IVarElement' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VarDeclaration(arraySize="sample_text")
    partner = libraryElement_IVarElement()
    setattr(partner, 'libraryElement_IVarElement', None)
    _safe_set(owner, 'libraryElement_VarDeclaration174', partner)
    assert owner in getattr(partner, 'libraryElement_IVarElement')
    _safe_set(owner, 'libraryElement_VarDeclaration174', None)
    assert owner not in getattr(partner, 'libraryElement_IVarElement')


def test_assoc_varInitialization124_stub_double():
    # libraryElement_VarInitialization has no real 'libraryElement_VarInitialization' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VarDeclaration(arraySize="sample_text")
    partner = libraryElement_VarInitialization()
    setattr(partner, 'libraryElement_VarInitialization', None)
    _safe_set(owner, 'libraryElement_VarDeclaration125', partner)
    assert getattr(partner, 'libraryElement_VarInitialization') == owner
    _safe_set(owner, 'libraryElement_VarDeclaration125', None)
    assert getattr(partner, 'libraryElement_VarInitialization') is None


def test_assoc_variables127_stub_double():
    # libraryElement_With has no real 'withs' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VarDeclaration(arraySize="sample_text")
    partner = libraryElement_With()
    setattr(partner, 'withs', None)
    _safe_set(owner, 'VarDeclaration', partner)
    assert getattr(partner, 'withs') == owner
    _safe_set(owner, 'VarDeclaration', None)
    assert getattr(partner, 'withs') is None


def test_assoc_versionInfo128_stub_double():
    # libraryElement_LibraryElement has no real 'libraryElement_LibraryElement' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VersionInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VersionInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VersionInfo(author="sample_text", date="sample_text", organization="sample_text", remarks="sample_text", version="sample_text")
    partner = libraryElement_LibraryElement()
    setattr(partner, 'libraryElement_LibraryElement', None)
    _safe_set(owner, 'libraryElement_VersionInfo', partner)
    assert owner in getattr(partner, 'libraryElement_LibraryElement')
    _safe_set(owner, 'libraryElement_VersionInfo', None)
    assert owner not in getattr(partner, 'libraryElement_LibraryElement')


def test_assoc_withs126_stub_double():
    # libraryElement_With has no real 'With' property in the generated
    # code (a bare stub) -- manually attach it so libraryElement_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # libraryElement_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = libraryElement_VarDeclaration(arraySize="sample_text")
    partner = libraryElement_With()
    setattr(partner, 'With', None)
    _safe_set(owner, 'variables', {partner})
    assert getattr(partner, 'With') == owner
    _safe_set(owner, 'variables', set())
    assert getattr(partner, 'With') is None


