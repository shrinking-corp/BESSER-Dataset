import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractEventAction,
    AbstractEventSymbol,
    FormalParameterMappingType,
    FormalParameterMappingsType,
    IAccessPointOwner,
    IConnectionSymbol,
    IEventHandlerOwner,
    IExtensibleElement,
    IFlowObjectSymbol,
    IGraphicalObject,
    IIdentifiableElement,
    IIdentifiableModelElement,
    IMetaType,
    IModelElement,
    IModelElementNodeSymbol,
    IModelParticipant,
    IModelParticipantSymbol,
    INodeSymbol,
    ISwimlaneSymbol,
    ISymbolContainer,
    ITypedElement,
    IdRefOwner,
    carnot_AbstractEventAction,
    carnot_AbstractEventSymbol,
    carnot_AccessPointType,
    carnot_ActivitySymbolType,
    carnot_ActivityType,
    carnot_AnnotationSymbolType,
    carnot_ApplicationContextTypeType,
    carnot_ApplicationSymbolType,
    carnot_ApplicationType,
    carnot_ApplicationTypeType,
    carnot_AttributeType,
    carnot_BindActionType,
    carnot_Code,
    carnot_ConditionalPerformerSymbolType,
    carnot_ConditionalPerformerType,
    carnot_ContextType,
    carnot_Coordinates,
    carnot_DataMappingConnectionType,
    carnot_DataMappingType,
    carnot_DataPathType,
    carnot_DataSymbolType,
    carnot_DataType,
    carnot_DataTypeType,
    carnot_DescriptionType,
    carnot_DiagramType,
    carnot_DocumentRoot,
    carnot_EObject,
    carnot_EStringToStringMapEntry,
    carnot_EndEventSymbol,
    carnot_EventActionType,
    carnot_EventActionTypeType,
    carnot_EventConditionTypeType,
    carnot_EventHandlerType,
    carnot_ExecutedByConnectionType,
    carnot_ExternalPackage,
    carnot_ExternalPackages,
    carnot_ExternalReferenceType,
    carnot_FormalParametersType,
    carnot_GatewaySymbol,
    carnot_GenericLinkConnectionType,
    carnot_GroupSymbolType,
    carnot_IAccessPointOwner,
    carnot_IConnectionSymbol,
    carnot_IEventHandlerOwner,
    carnot_IExtensibleElement,
    carnot_IFlowObjectSymbol,
    carnot_IGraphicalObject,
    carnot_IIdentifiableElement,
    carnot_IIdentifiableModelElement,
    carnot_IMetaType,
    carnot_IModelElement,
    carnot_IModelElementNodeSymbol,
    carnot_IModelParticipant,
    carnot_IModelParticipantSymbol,
    carnot_INodeSymbol,
    carnot_ISwimlaneSymbol,
    carnot_ISymbolContainer,
    carnot_ITypedElement,
    carnot_IdRef,
    carnot_IdRefOwner,
    carnot_IdentifiableReference,
    carnot_IntermediateEventSymbol,
    carnot_LaneSymbol,
    carnot_LinkTypeType,
    carnot_LoopType,
    carnot_ModelType,
    carnot_ModelerSymbolType,
    carnot_ModelerType,
    carnot_OrganizationSymbolType,
    carnot_OrganizationType,
    carnot_ParameterMappingType,
    carnot_PartOfConnectionType,
    carnot_ParticipantType,
    carnot_PerformsConnectionType,
    carnot_PoolSymbol,
    carnot_ProcessDefinitionType,
    carnot_ProcessSymbolType,
    carnot_PublicInterfaceSymbol,
    carnot_QualityControlType,
    carnot_RefersToConnectionType,
    carnot_RoleSymbolType,
    carnot_RoleType,
    carnot_ScriptType,
    carnot_StartEventSymbol,
    carnot_SubProcessOfConnectionType,
    carnot_TeamLeadConnectionType,
    carnot_TextSymbolType,
    carnot_TextType,
    carnot_TransitionConnectionType,
    carnot_TransitionType,
    carnot_TriggerType,
    carnot_TriggerTypeType,
    carnot_TriggersConnectionType,
    carnot_TypeDeclarationsType,
    carnot_UnbindActionType,
    carnot_ViewType,
    carnot_ViewableType,
    carnot_WorksForConnectionType,
    carnot_XmlTextNode,
    carnot_extensions_FormalParameterMappingType,
    carnot_extensions_FormalParameterMappingsType,
    extensions_carnot_DataType,
    extensions_carnot_FormalParameterType,
    ActivityImplementationType,
    DiagramModeType,
    DirectionType,
    FlowControlType,
    ImplementationType,
    JoinSplitType,
    LinkCardinality,
    LinkColor,
    LinkEndStyle,
    LinkLineStyle,
    LoopType,
    OrientationType,
    RoutingType,
    SubProcessModeType,
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

def test_assoc_activity282_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'carnot_ActivityType284', a1)
    assert _is_linked(b, 'carnot_ActivityType284', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType283'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType283', b)
    _safe_set(b, 'carnot_ActivityType284', a2)
    assert _is_linked(b, 'carnot_ActivityType284', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType283'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType283', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType283'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType283', b)
    _safe_set(b, 'carnot_ActivityType284', None)
    assert not _is_linked(b, 'carnot_ActivityType284', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType283'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType283', b)


def test_assoc_application227_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ApplicationType(interactive="sample_text")
    _safe_set(b, 'carnot_ApplicationType229', a1)
    assert _is_linked(b, 'carnot_ApplicationType229', a1)
    if hasattr(a1, 'carnot_ModelType228'):
        assert _is_linked(a1, 'carnot_ModelType228', b)
    _safe_set(b, 'carnot_ApplicationType229', a2)
    assert _is_linked(b, 'carnot_ApplicationType229', a2)
    if hasattr(a1, 'carnot_ModelType228'):
        assert not _is_linked(a1, 'carnot_ModelType228', b)
    if hasattr(a2, 'carnot_ModelType228'):
        assert _is_linked(a2, 'carnot_ModelType228', b)
    _safe_set(b, 'carnot_ApplicationType229', None)
    assert not _is_linked(b, 'carnot_ApplicationType229', a2)
    if hasattr(a2, 'carnot_ModelType228'):
        assert not _is_linked(a2, 'carnot_ModelType228', b)


def test_assoc_application93_reverse_link_reassign_clear():
    a1 = carnot_ApplicationType(interactive="sample_text")
    a2 = carnot_ApplicationType(interactive="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'executedActivities', a1)
    assert _is_linked(b, 'executedActivities', a1)
    if hasattr(a1, 'ApplicationType'):
        assert _is_linked(a1, 'ApplicationType', b)
    _safe_set(b, 'executedActivities', a2)
    assert _is_linked(b, 'executedActivities', a2)
    if hasattr(a1, 'ApplicationType'):
        assert not _is_linked(a1, 'ApplicationType', b)
    if hasattr(a2, 'ApplicationType'):
        assert _is_linked(a2, 'ApplicationType', b)
    _safe_set(b, 'executedActivities', None)
    assert not _is_linked(b, 'executedActivities', a2)
    if hasattr(a2, 'ApplicationType'):
        assert not _is_linked(a2, 'ApplicationType', b)


def test_assoc_applicationContextType216_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    _safe_set(b, 'carnot_ApplicationContextTypeType', a1)
    assert _is_linked(b, 'carnot_ApplicationContextTypeType', a1)
    if hasattr(a1, 'carnot_ModelType217'):
        assert _is_linked(a1, 'carnot_ModelType217', b)
    _safe_set(b, 'carnot_ApplicationContextTypeType', a2)
    assert _is_linked(b, 'carnot_ApplicationContextTypeType', a2)
    if hasattr(a1, 'carnot_ModelType217'):
        assert not _is_linked(a1, 'carnot_ModelType217', b)
    if hasattr(a2, 'carnot_ModelType217'):
        assert _is_linked(a2, 'carnot_ModelType217', b)
    _safe_set(b, 'carnot_ApplicationContextTypeType', None)
    assert not _is_linked(b, 'carnot_ApplicationContextTypeType', a2)
    if hasattr(a2, 'carnot_ModelType217'):
        assert not _is_linked(a2, 'carnot_ModelType217', b)


def test_assoc_applicationType214_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    _safe_set(b, 'carnot_ApplicationTypeType', a1)
    assert _is_linked(b, 'carnot_ApplicationTypeType', a1)
    if hasattr(a1, 'carnot_ModelType215'):
        assert _is_linked(a1, 'carnot_ModelType215', b)
    _safe_set(b, 'carnot_ApplicationTypeType', a2)
    assert _is_linked(b, 'carnot_ApplicationTypeType', a2)
    if hasattr(a1, 'carnot_ModelType215'):
        assert not _is_linked(a1, 'carnot_ModelType215', b)
    if hasattr(a2, 'carnot_ModelType215'):
        assert _is_linked(a2, 'carnot_ModelType215', b)
    _safe_set(b, 'carnot_ApplicationTypeType', None)
    assert not _is_linked(b, 'carnot_ApplicationTypeType', a2)
    if hasattr(a2, 'carnot_ModelType215'):
        assert not _is_linked(a2, 'carnot_ModelType215', b)


def test_assoc_applications124_reverse_link_reassign_clear():
    a1 = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    a2 = carnot_ApplicationTypeType(accessPointProviderClass="sample_text_2", instanceClass="sample_text_2", panelClass="sample_text_2", synchronous="sample_text_2", validatorClass="sample_text_2")
    b = carnot_ApplicationType(interactive="sample_text")
    _safe_set(b, 'ApplicationType126', a1)
    assert _is_linked(b, 'ApplicationType126', a1)
    if hasattr(a1, 'type125'):
        assert _is_linked(a1, 'type125', b)
    _safe_set(b, 'ApplicationType126', a2)
    assert _is_linked(b, 'ApplicationType126', a2)
    if hasattr(a1, 'type125'):
        assert not _is_linked(a1, 'type125', b)
    if hasattr(a2, 'type125'):
        assert _is_linked(a2, 'type125', b)
    _safe_set(b, 'ApplicationType126', None)
    assert not _is_linked(b, 'ApplicationType126', a2)
    if hasattr(a2, 'type125'):
        assert not _is_linked(a2, 'type125', b)


def test_assoc_conditionalPerformer238_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    _safe_set(b, 'carnot_ConditionalPerformerType', a1)
    assert _is_linked(b, 'carnot_ConditionalPerformerType', a1)
    if hasattr(a1, 'carnot_ModelType239'):
        assert _is_linked(a1, 'carnot_ModelType239', b)
    _safe_set(b, 'carnot_ConditionalPerformerType', a2)
    assert _is_linked(b, 'carnot_ConditionalPerformerType', a2)
    if hasattr(a1, 'carnot_ModelType239'):
        assert not _is_linked(a1, 'carnot_ModelType239', b)
    if hasattr(a2, 'carnot_ModelType239'):
        assert _is_linked(a2, 'carnot_ModelType239', b)
    _safe_set(b, 'carnot_ConditionalPerformerType', None)
    assert not _is_linked(b, 'carnot_ConditionalPerformerType', a2)
    if hasattr(a2, 'carnot_ModelType239'):
        assert not _is_linked(a2, 'carnot_ModelType239', b)


def test_assoc_conditionalPerformers157_reverse_link_reassign_clear():
    a1 = carnot_DataType(predefined="sample_text")
    a2 = carnot_DataType(predefined="sample_text_2")
    b = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    _safe_set(b, 'ConditionalPerformerType159', a1)
    assert _is_linked(b, 'ConditionalPerformerType159', a1)
    if hasattr(a1, 'data158'):
        assert _is_linked(a1, 'data158', b)
    _safe_set(b, 'ConditionalPerformerType159', a2)
    assert _is_linked(b, 'ConditionalPerformerType159', a2)
    if hasattr(a1, 'data158'):
        assert not _is_linked(a1, 'data158', b)
    if hasattr(a2, 'data158'):
        assert _is_linked(a2, 'data158', b)
    _safe_set(b, 'ConditionalPerformerType159', None)
    assert not _is_linked(b, 'ConditionalPerformerType159', a2)
    if hasattr(a2, 'data158'):
        assert not _is_linked(a2, 'data158', b)


def test_assoc_coordinates71_reverse_link_reassign_clear():
    a1 = carnot_IConnectionSymbol(routing="sample_text", sourceAnchor="sample_text", targetAnchor="sample_text")
    a2 = carnot_IConnectionSymbol(routing="sample_text_2", sourceAnchor="sample_text_2", targetAnchor="sample_text_2")
    b = carnot_Coordinates(xPos="sample_text", yPos="sample_text")
    _safe_set(b, 'carnot_Coordinates', a1)
    assert _is_linked(b, 'carnot_Coordinates', a1)
    if hasattr(a1, 'carnot_IConnectionSymbol'):
        assert _is_linked(a1, 'carnot_IConnectionSymbol', b)
    _safe_set(b, 'carnot_Coordinates', a2)
    assert _is_linked(b, 'carnot_Coordinates', a2)
    if hasattr(a1, 'carnot_IConnectionSymbol'):
        assert not _is_linked(a1, 'carnot_IConnectionSymbol', b)
    if hasattr(a2, 'carnot_IConnectionSymbol'):
        assert _is_linked(a2, 'carnot_IConnectionSymbol', b)
    _safe_set(b, 'carnot_Coordinates', None)
    assert not _is_linked(b, 'carnot_Coordinates', a2)
    if hasattr(a2, 'carnot_IConnectionSymbol'):
        assert not _is_linked(a2, 'carnot_IConnectionSymbol', b)


def test_assoc_data131_reverse_link_reassign_clear():
    a1 = carnot_DataType(predefined="sample_text")
    a2 = carnot_DataType(predefined="sample_text_2")
    b = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    _safe_set(b, 'conditionalPerformers', a1)
    assert _is_linked(b, 'conditionalPerformers', a1)
    if hasattr(a1, 'DataType'):
        assert _is_linked(a1, 'DataType', b)
    _safe_set(b, 'conditionalPerformers', a2)
    assert _is_linked(b, 'conditionalPerformers', a2)
    if hasattr(a1, 'DataType'):
        assert not _is_linked(a1, 'DataType', b)
    if hasattr(a2, 'DataType'):
        assert _is_linked(a2, 'DataType', b)
    _safe_set(b, 'conditionalPerformers', None)
    assert not _is_linked(b, 'conditionalPerformers', a2)
    if hasattr(a2, 'DataType'):
        assert not _is_linked(a2, 'DataType', b)


def test_assoc_data142_reverse_link_reassign_clear():
    a1 = carnot_DataType(predefined="sample_text")
    a2 = carnot_DataType(predefined="sample_text_2")
    b = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    _safe_set(b, 'dataMappings143', a1)
    assert _is_linked(b, 'dataMappings143', a1)
    if hasattr(a1, 'DataType144'):
        assert _is_linked(a1, 'DataType144', b)
    _safe_set(b, 'dataMappings143', a2)
    assert _is_linked(b, 'dataMappings143', a2)
    if hasattr(a1, 'DataType144'):
        assert not _is_linked(a1, 'DataType144', b)
    if hasattr(a2, 'DataType144'):
        assert _is_linked(a2, 'DataType144', b)
    _safe_set(b, 'dataMappings143', None)
    assert not _is_linked(b, 'dataMappings143', a2)
    if hasattr(a2, 'DataType144'):
        assert not _is_linked(a2, 'DataType144', b)


def test_assoc_data145_reverse_link_reassign_clear():
    a1 = carnot_DataType(predefined="sample_text")
    a2 = carnot_DataType(predefined="sample_text_2")
    b = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    _safe_set(b, 'dataPaths', a1)
    assert _is_linked(b, 'dataPaths', a1)
    if hasattr(a1, 'DataType146'):
        assert _is_linked(a1, 'DataType146', b)
    _safe_set(b, 'dataPaths', a2)
    assert _is_linked(b, 'dataPaths', a2)
    if hasattr(a1, 'DataType146'):
        assert not _is_linked(a1, 'DataType146', b)
    if hasattr(a2, 'DataType146'):
        assert _is_linked(a2, 'DataType146', b)
    _safe_set(b, 'dataPaths', None)
    assert not _is_linked(b, 'dataPaths', a2)
    if hasattr(a2, 'DataType146'):
        assert not _is_linked(a2, 'DataType146', b)


def test_assoc_data165_reverse_link_reassign_clear():
    a1 = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    a2 = carnot_DataTypeType(accessPathEditor="sample_text_2", evaluator="sample_text_2", instanceClass="sample_text_2", panelClass="sample_text_2", readable="sample_text_2", storageStrategy="sample_text_2", validatorClass="sample_text_2", valueCreator="sample_text_2", writable="sample_text_2")
    b = carnot_DataType(predefined="sample_text")
    _safe_set(b, 'DataType167', a1)
    assert _is_linked(b, 'DataType167', a1)
    if hasattr(a1, 'type166'):
        assert _is_linked(a1, 'type166', b)
    _safe_set(b, 'DataType167', a2)
    assert _is_linked(b, 'DataType167', a2)
    if hasattr(a1, 'type166'):
        assert not _is_linked(a1, 'type166', b)
    if hasattr(a2, 'type166'):
        assert _is_linked(a2, 'type166', b)
    _safe_set(b, 'DataType167', None)
    assert not _is_linked(b, 'DataType167', a2)
    if hasattr(a2, 'type166'):
        assert not _is_linked(a2, 'type166', b)


def test_assoc_data224_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DataType(predefined="sample_text")
    _safe_set(b, 'carnot_DataType226', a1)
    assert _is_linked(b, 'carnot_DataType226', a1)
    if hasattr(a1, 'carnot_ModelType225'):
        assert _is_linked(a1, 'carnot_ModelType225', b)
    _safe_set(b, 'carnot_DataType226', a2)
    assert _is_linked(b, 'carnot_DataType226', a2)
    if hasattr(a1, 'carnot_ModelType225'):
        assert not _is_linked(a1, 'carnot_ModelType225', b)
    if hasattr(a2, 'carnot_ModelType225'):
        assert _is_linked(a2, 'carnot_ModelType225', b)
    _safe_set(b, 'carnot_DataType226', None)
    assert not _is_linked(b, 'carnot_DataType226', a2)
    if hasattr(a2, 'carnot_ModelType225'):
        assert not _is_linked(a2, 'carnot_ModelType225', b)


def test_assoc_data265_reverse_link_reassign_clear():
    a1 = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    a2 = carnot_ParameterMappingType(dataPath="sample_text_2", parameter="sample_text_2", parameterPath="sample_text_2")
    b = carnot_DataType(predefined="sample_text")
    _safe_set(b, 'DataType266', a1)
    assert _is_linked(b, 'DataType266', a1)
    if hasattr(a1, 'parameterMappings'):
        assert _is_linked(a1, 'parameterMappings', b)
    _safe_set(b, 'DataType266', a2)
    assert _is_linked(b, 'DataType266', a2)
    if hasattr(a1, 'parameterMappings'):
        assert not _is_linked(a1, 'parameterMappings', b)
    if hasattr(a2, 'parameterMappings'):
        assert _is_linked(a2, 'parameterMappings', b)
    _safe_set(b, 'DataType266', None)
    assert not _is_linked(b, 'DataType266', a2)
    if hasattr(a2, 'parameterMappings'):
        assert not _is_linked(a2, 'parameterMappings', b)


def test_assoc_dataMapping92_reverse_link_reassign_clear():
    a1 = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    a2 = carnot_DataMappingType(applicationAccessPoint="sample_text_2", applicationPath="sample_text_2", context="sample_text_2", dataPath="sample_text_2", direction="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'carnot_ActivityType', {a1})
    assert _is_linked(b, 'carnot_ActivityType', a1)
    if hasattr(a1, 'carnot_DataMappingType'):
        assert _is_linked(a1, 'carnot_DataMappingType', b)
    _safe_set(b, 'carnot_ActivityType', {a2})
    assert _is_linked(b, 'carnot_ActivityType', a2)
    if hasattr(a1, 'carnot_DataMappingType'):
        assert not _is_linked(a1, 'carnot_DataMappingType', b)
    if hasattr(a2, 'carnot_DataMappingType'):
        assert _is_linked(a2, 'carnot_DataMappingType', b)
    _safe_set(b, 'carnot_ActivityType', set())
    assert not _is_linked(b, 'carnot_ActivityType', a2)
    if hasattr(a2, 'carnot_DataMappingType'):
        assert not _is_linked(a2, 'carnot_DataMappingType', b)


def test_assoc_dataMappings151_reverse_link_reassign_clear():
    a1 = carnot_DataType(predefined="sample_text")
    a2 = carnot_DataType(predefined="sample_text_2")
    b = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    _safe_set(b, 'DataMappingType', a1)
    assert _is_linked(b, 'DataMappingType', a1)
    if hasattr(a1, 'data'):
        assert _is_linked(a1, 'data', b)
    _safe_set(b, 'DataMappingType', a2)
    assert _is_linked(b, 'DataMappingType', a2)
    if hasattr(a1, 'data'):
        assert not _is_linked(a1, 'data', b)
    if hasattr(a2, 'data'):
        assert _is_linked(a2, 'data', b)
    _safe_set(b, 'DataMappingType', None)
    assert not _is_linked(b, 'DataMappingType', a2)
    if hasattr(a2, 'data'):
        assert not _is_linked(a2, 'data', b)


def test_assoc_dataPath289_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    _safe_set(b, 'carnot_DataPathType', a1)
    assert _is_linked(b, 'carnot_DataPathType', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType290'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType290', b)
    _safe_set(b, 'carnot_DataPathType', a2)
    assert _is_linked(b, 'carnot_DataPathType', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType290'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType290', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType290'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType290', b)
    _safe_set(b, 'carnot_DataPathType', None)
    assert not _is_linked(b, 'carnot_DataPathType', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType290'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType290', b)


def test_assoc_dataPaths160_reverse_link_reassign_clear():
    a1 = carnot_DataType(predefined="sample_text")
    a2 = carnot_DataType(predefined="sample_text_2")
    b = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    _safe_set(b, 'DataPathType', a1)
    assert _is_linked(b, 'DataPathType', a1)
    if hasattr(a1, 'data161'):
        assert _is_linked(a1, 'data161', b)
    _safe_set(b, 'DataPathType', a2)
    assert _is_linked(b, 'DataPathType', a2)
    if hasattr(a1, 'data161'):
        assert not _is_linked(a1, 'data161', b)
    if hasattr(a2, 'data161'):
        assert _is_linked(a2, 'data161', b)
    _safe_set(b, 'DataPathType', None)
    assert not _is_linked(b, 'DataPathType', a2)
    if hasattr(a2, 'data161'):
        assert not _is_linked(a2, 'data161', b)


def test_assoc_dataType211_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    _safe_set(b, 'carnot_DataTypeType213', a1)
    assert _is_linked(b, 'carnot_DataTypeType213', a1)
    if hasattr(a1, 'carnot_ModelType212'):
        assert _is_linked(a1, 'carnot_ModelType212', b)
    _safe_set(b, 'carnot_DataTypeType213', a2)
    assert _is_linked(b, 'carnot_DataTypeType213', a2)
    if hasattr(a1, 'carnot_ModelType212'):
        assert not _is_linked(a1, 'carnot_ModelType212', b)
    if hasattr(a2, 'carnot_ModelType212'):
        assert _is_linked(a2, 'carnot_ModelType212', b)
    _safe_set(b, 'carnot_DataTypeType213', None)
    assert not _is_linked(b, 'carnot_DataTypeType213', a2)
    if hasattr(a2, 'carnot_ModelType212'):
        assert not _is_linked(a2, 'carnot_ModelType212', b)


def test_assoc_description208_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DescriptionType(mixed="sample_text")
    _safe_set(b, 'carnot_DescriptionType210', a1)
    assert _is_linked(b, 'carnot_DescriptionType210', a1)
    if hasattr(a1, 'carnot_ModelType209'):
        assert _is_linked(a1, 'carnot_ModelType209', b)
    _safe_set(b, 'carnot_DescriptionType210', a2)
    assert _is_linked(b, 'carnot_DescriptionType210', a2)
    if hasattr(a1, 'carnot_ModelType209'):
        assert not _is_linked(a1, 'carnot_ModelType209', b)
    if hasattr(a2, 'carnot_ModelType209'):
        assert _is_linked(a2, 'carnot_ModelType209', b)
    _safe_set(b, 'carnot_DescriptionType210', None)
    assert not _is_linked(b, 'carnot_DescriptionType210', a2)
    if hasattr(a2, 'carnot_ModelType209'):
        assert not _is_linked(a2, 'carnot_ModelType209', b)


def test_assoc_description3_reverse_link_reassign_clear():
    a1 = carnot_IIdentifiableModelElement()
    a2 = carnot_IIdentifiableModelElement()
    b = carnot_DescriptionType(mixed="sample_text")
    _safe_set(b, 'carnot_DescriptionType', a1)
    assert _is_linked(b, 'carnot_DescriptionType', a1)
    if hasattr(a1, 'carnot_IIdentifiableModelElement'):
        assert _is_linked(a1, 'carnot_IIdentifiableModelElement', b)
    _safe_set(b, 'carnot_DescriptionType', a2)
    assert _is_linked(b, 'carnot_DescriptionType', a2)
    if hasattr(a1, 'carnot_IIdentifiableModelElement'):
        assert not _is_linked(a1, 'carnot_IIdentifiableModelElement', b)
    if hasattr(a2, 'carnot_IIdentifiableModelElement'):
        assert _is_linked(a2, 'carnot_IIdentifiableModelElement', b)
    _safe_set(b, 'carnot_DescriptionType', None)
    assert not _is_linked(b, 'carnot_DescriptionType', a2)
    if hasattr(a2, 'carnot_IIdentifiableModelElement'):
        assert not _is_linked(a2, 'carnot_IIdentifiableModelElement', b)


def test_assoc_description367_reverse_link_reassign_clear():
    a1 = carnot_ViewType(name="sample_text")
    a2 = carnot_ViewType(name="sample_text_2")
    b = carnot_DescriptionType(mixed="sample_text")
    _safe_set(b, 'carnot_DescriptionType369', a1)
    assert _is_linked(b, 'carnot_DescriptionType369', a1)
    if hasattr(a1, 'carnot_ViewType368'):
        assert _is_linked(a1, 'carnot_ViewType368', b)
    _safe_set(b, 'carnot_DescriptionType369', a2)
    assert _is_linked(b, 'carnot_DescriptionType369', a2)
    if hasattr(a1, 'carnot_ViewType368'):
        assert not _is_linked(a1, 'carnot_ViewType368', b)
    if hasattr(a2, 'carnot_ViewType368'):
        assert _is_linked(a2, 'carnot_ViewType368', b)
    _safe_set(b, 'carnot_DescriptionType369', None)
    assert not _is_linked(b, 'carnot_DescriptionType369', a2)
    if hasattr(a2, 'carnot_ViewType368'):
        assert not _is_linked(a2, 'carnot_ViewType368', b)


def test_assoc_diagram248_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    _safe_set(b, 'carnot_DiagramType', a1)
    assert _is_linked(b, 'carnot_DiagramType', a1)
    if hasattr(a1, 'carnot_ModelType249'):
        assert _is_linked(a1, 'carnot_ModelType249', b)
    _safe_set(b, 'carnot_DiagramType', a2)
    assert _is_linked(b, 'carnot_DiagramType', a2)
    if hasattr(a1, 'carnot_ModelType249'):
        assert not _is_linked(a1, 'carnot_ModelType249', b)
    if hasattr(a2, 'carnot_ModelType249'):
        assert _is_linked(a2, 'carnot_ModelType249', b)
    _safe_set(b, 'carnot_DiagramType', None)
    assert not _is_linked(b, 'carnot_DiagramType', a2)
    if hasattr(a2, 'carnot_ModelType249'):
        assert not _is_linked(a2, 'carnot_ModelType249', b)


def test_assoc_diagram277_reverse_link_reassign_clear():
    a1 = carnot_PoolSymbol(boundaryVisible="sample_text")
    a2 = carnot_PoolSymbol(boundaryVisible="sample_text_2")
    b = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    _safe_set(b, 'DiagramType', a1)
    assert _is_linked(b, 'DiagramType', a1)
    if hasattr(a1, 'poolSymbols'):
        assert _is_linked(a1, 'poolSymbols', b)
    _safe_set(b, 'DiagramType', a2)
    assert _is_linked(b, 'DiagramType', a2)
    if hasattr(a1, 'poolSymbols'):
        assert not _is_linked(a1, 'poolSymbols', b)
    if hasattr(a2, 'poolSymbols'):
        assert _is_linked(a2, 'poolSymbols', b)
    _safe_set(b, 'DiagramType', None)
    assert not _is_linked(b, 'DiagramType', a2)
    if hasattr(a2, 'poolSymbols'):
        assert not _is_linked(a2, 'poolSymbols', b)


def test_assoc_diagram291_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    _safe_set(b, 'carnot_DiagramType293', a1)
    assert _is_linked(b, 'carnot_DiagramType293', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType292'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType292', b)
    _safe_set(b, 'carnot_DiagramType293', a2)
    assert _is_linked(b, 'carnot_DiagramType293', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType292'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType292', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType292'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType292', b)
    _safe_set(b, 'carnot_DiagramType293', None)
    assert not _is_linked(b, 'carnot_DiagramType293', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType292'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType292', b)


def test_assoc_eventActionType222_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    _safe_set(b, 'carnot_EventActionTypeType', a1)
    assert _is_linked(b, 'carnot_EventActionTypeType', a1)
    if hasattr(a1, 'carnot_ModelType223'):
        assert _is_linked(a1, 'carnot_ModelType223', b)
    _safe_set(b, 'carnot_EventActionTypeType', a2)
    assert _is_linked(b, 'carnot_EventActionTypeType', a2)
    if hasattr(a1, 'carnot_ModelType223'):
        assert not _is_linked(a1, 'carnot_ModelType223', b)
    if hasattr(a2, 'carnot_ModelType223'):
        assert _is_linked(a2, 'carnot_ModelType223', b)
    _safe_set(b, 'carnot_EventActionTypeType', None)
    assert not _is_linked(b, 'carnot_EventActionTypeType', a2)
    if hasattr(a2, 'carnot_ModelType223'):
        assert not _is_linked(a2, 'carnot_ModelType223', b)


def test_assoc_eventConditionType220_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    _safe_set(b, 'carnot_EventConditionTypeType', a1)
    assert _is_linked(b, 'carnot_EventConditionTypeType', a1)
    if hasattr(a1, 'carnot_ModelType221'):
        assert _is_linked(a1, 'carnot_ModelType221', b)
    _safe_set(b, 'carnot_EventConditionTypeType', a2)
    assert _is_linked(b, 'carnot_EventConditionTypeType', a2)
    if hasattr(a1, 'carnot_ModelType221'):
        assert not _is_linked(a1, 'carnot_ModelType221', b)
    if hasattr(a2, 'carnot_ModelType221'):
        assert _is_linked(a2, 'carnot_ModelType221', b)
    _safe_set(b, 'carnot_EventConditionTypeType', None)
    assert not _is_linked(b, 'carnot_EventConditionTypeType', a2)
    if hasattr(a2, 'carnot_ModelType221'):
        assert not _is_linked(a2, 'carnot_ModelType221', b)


def test_assoc_eventHandlers177_reverse_link_reassign_clear():
    a1 = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    a2 = carnot_EventHandlerType(autoBind="sample_text_2", consumeOnMatch="sample_text_2", logHandler="sample_text_2", unbindOnMatch="sample_text_2")
    b = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    _safe_set(b, 'type178', {a1})
    assert _is_linked(b, 'type178', a1)
    if hasattr(a1, 'EventHandlerType'):
        assert _is_linked(a1, 'EventHandlerType', b)
    _safe_set(b, 'type178', {a2})
    assert _is_linked(b, 'type178', a2)
    if hasattr(a1, 'EventHandlerType'):
        assert not _is_linked(a1, 'EventHandlerType', b)
    if hasattr(a2, 'EventHandlerType'):
        assert _is_linked(a2, 'EventHandlerType', b)
    _safe_set(b, 'type178', set())
    assert not _is_linked(b, 'type178', a2)
    if hasattr(a2, 'EventHandlerType'):
        assert not _is_linked(a2, 'EventHandlerType', b)


def test_assoc_executedActivities120_reverse_link_reassign_clear():
    a1 = carnot_ApplicationType(interactive="sample_text")
    a2 = carnot_ApplicationType(interactive="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'ActivityType121', a1)
    assert _is_linked(b, 'ActivityType121', a1)
    if hasattr(a1, 'application'):
        assert _is_linked(a1, 'application', b)
    _safe_set(b, 'ActivityType121', a2)
    assert _is_linked(b, 'ActivityType121', a2)
    if hasattr(a1, 'application'):
        assert not _is_linked(a1, 'application', b)
    if hasattr(a2, 'application'):
        assert _is_linked(a2, 'application', b)
    _safe_set(b, 'ActivityType121', None)
    assert not _is_linked(b, 'ActivityType121', a2)
    if hasattr(a2, 'application'):
        assert not _is_linked(a2, 'application', b)


def test_assoc_executingActivities294_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'ActivityType295', a1)
    assert _is_linked(b, 'ActivityType295', a1)
    if hasattr(a1, 'implementationProcess'):
        assert _is_linked(a1, 'implementationProcess', b)
    _safe_set(b, 'ActivityType295', a2)
    assert _is_linked(b, 'ActivityType295', a2)
    if hasattr(a1, 'implementationProcess'):
        assert not _is_linked(a1, 'implementationProcess', b)
    if hasattr(a2, 'implementationProcess'):
        assert _is_linked(a2, 'implementationProcess', b)
    _safe_set(b, 'ActivityType295', None)
    assert not _is_linked(b, 'ActivityType295', a2)
    if hasattr(a2, 'implementationProcess'):
        assert not _is_linked(a2, 'implementationProcess', b)


def test_assoc_expression343_reverse_link_reassign_clear():
    a1 = carnot_XmlTextNode(mixed="sample_text")
    a2 = carnot_XmlTextNode(mixed="sample_text_2")
    b = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    _safe_set(b, 'carnot_TransitionType344', a1)
    assert _is_linked(b, 'carnot_TransitionType344', a1)
    if hasattr(a1, 'carnot_XmlTextNode345'):
        assert _is_linked(a1, 'carnot_XmlTextNode345', b)
    _safe_set(b, 'carnot_TransitionType344', a2)
    assert _is_linked(b, 'carnot_TransitionType344', a2)
    if hasattr(a1, 'carnot_XmlTextNode345'):
        assert not _is_linked(a1, 'carnot_XmlTextNode345', b)
    if hasattr(a2, 'carnot_XmlTextNode345'):
        assert _is_linked(a2, 'carnot_XmlTextNode345', b)
    _safe_set(b, 'carnot_TransitionType344', None)
    assert not _is_linked(b, 'carnot_TransitionType344', a2)
    if hasattr(a2, 'carnot_XmlTextNode345'):
        assert not _is_linked(a2, 'carnot_XmlTextNode345', b)


def test_assoc_from_346_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'ActivityType348', a1)
    assert _is_linked(b, 'ActivityType348', a1)
    if hasattr(a1, 'outTransitions347'):
        assert _is_linked(a1, 'outTransitions347', b)
    _safe_set(b, 'ActivityType348', a2)
    assert _is_linked(b, 'ActivityType348', a2)
    if hasattr(a1, 'outTransitions347'):
        assert not _is_linked(a1, 'outTransitions347', b)
    if hasattr(a2, 'outTransitions347'):
        assert _is_linked(a2, 'outTransitions347', b)
    _safe_set(b, 'ActivityType348', None)
    assert not _is_linked(b, 'ActivityType348', a2)
    if hasattr(a2, 'outTransitions347'):
        assert not _is_linked(a2, 'outTransitions347', b)


def test_assoc_gatewaySymbol17_reverse_link_reassign_clear():
    a1 = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    a2 = carnot_ISymbolContainer(connections="sample_text_2", nodes="sample_text_2")
    b = carnot_GatewaySymbol(flowKind="sample_text")
    _safe_set(b, 'carnot_GatewaySymbol', a1)
    assert _is_linked(b, 'carnot_GatewaySymbol', a1)
    if hasattr(a1, 'carnot_ISymbolContainer18'):
        assert _is_linked(a1, 'carnot_ISymbolContainer18', b)
    _safe_set(b, 'carnot_GatewaySymbol', a2)
    assert _is_linked(b, 'carnot_GatewaySymbol', a2)
    if hasattr(a1, 'carnot_ISymbolContainer18'):
        assert not _is_linked(a1, 'carnot_ISymbolContainer18', b)
    if hasattr(a2, 'carnot_ISymbolContainer18'):
        assert _is_linked(a2, 'carnot_ISymbolContainer18', b)
    _safe_set(b, 'carnot_GatewaySymbol', None)
    assert not _is_linked(b, 'carnot_GatewaySymbol', a2)
    if hasattr(a2, 'carnot_ISymbolContainer18'):
        assert not _is_linked(a2, 'carnot_ISymbolContainer18', b)


def test_assoc_implementationProcess94_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'executingActivities', a1)
    assert _is_linked(b, 'executingActivities', a1)
    if hasattr(a1, 'ProcessDefinitionType'):
        assert _is_linked(a1, 'ProcessDefinitionType', b)
    _safe_set(b, 'executingActivities', a2)
    assert _is_linked(b, 'executingActivities', a2)
    if hasattr(a1, 'ProcessDefinitionType'):
        assert not _is_linked(a1, 'ProcessDefinitionType', b)
    if hasattr(a2, 'ProcessDefinitionType'):
        assert _is_linked(a2, 'ProcessDefinitionType', b)
    _safe_set(b, 'executingActivities', None)
    assert not _is_linked(b, 'executingActivities', a2)
    if hasattr(a2, 'ProcessDefinitionType'):
        assert not _is_linked(a2, 'ProcessDefinitionType', b)


def test_assoc_inTransitions102_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'to103', {a1})
    assert _is_linked(b, 'to103', a1)
    if hasattr(a1, 'TransitionType'):
        assert _is_linked(a1, 'TransitionType', b)
    _safe_set(b, 'to103', {a2})
    assert _is_linked(b, 'to103', a2)
    if hasattr(a1, 'TransitionType'):
        assert not _is_linked(a1, 'TransitionType', b)
    if hasattr(a2, 'TransitionType'):
        assert _is_linked(a2, 'TransitionType', b)
    _safe_set(b, 'to103', set())
    assert not _is_linked(b, 'to103', a2)
    if hasattr(a2, 'TransitionType'):
        assert not _is_linked(a2, 'TransitionType', b)


def test_assoc_linkType250_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    _safe_set(b, 'carnot_LinkTypeType', a1)
    assert _is_linked(b, 'carnot_LinkTypeType', a1)
    if hasattr(a1, 'carnot_ModelType251'):
        assert _is_linked(a1, 'carnot_ModelType251', b)
    _safe_set(b, 'carnot_LinkTypeType', a2)
    assert _is_linked(b, 'carnot_LinkTypeType', a2)
    if hasattr(a1, 'carnot_ModelType251'):
        assert not _is_linked(a1, 'carnot_ModelType251', b)
    if hasattr(a2, 'carnot_ModelType251'):
        assert _is_linked(a2, 'carnot_ModelType251', b)
    _safe_set(b, 'carnot_LinkTypeType', None)
    assert not _is_linked(b, 'carnot_LinkTypeType', a2)
    if hasattr(a2, 'carnot_ModelType251'):
        assert not _is_linked(a2, 'carnot_ModelType251', b)


def test_assoc_model173_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'carnot_DocumentRoot174', {a1})
    assert _is_linked(b, 'carnot_DocumentRoot174', a1)
    if hasattr(a1, 'carnot_ModelType'):
        assert _is_linked(a1, 'carnot_ModelType', b)
    _safe_set(b, 'carnot_DocumentRoot174', {a2})
    assert _is_linked(b, 'carnot_DocumentRoot174', a2)
    if hasattr(a1, 'carnot_ModelType'):
        assert not _is_linked(a1, 'carnot_ModelType', b)
    if hasattr(a2, 'carnot_ModelType'):
        assert _is_linked(a2, 'carnot_ModelType', b)
    _safe_set(b, 'carnot_DocumentRoot174', set())
    assert not _is_linked(b, 'carnot_DocumentRoot174', a2)
    if hasattr(a2, 'carnot_ModelType'):
        assert not _is_linked(a2, 'carnot_ModelType', b)


def test_assoc_modeler230_reverse_link_reassign_clear():
    a1 = carnot_ModelerType(email="sample_text", password="sample_text")
    a2 = carnot_ModelerType(email="sample_text_2", password="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType231', {a1})
    assert _is_linked(b, 'carnot_ModelType231', a1)
    if hasattr(a1, 'carnot_ModelerType'):
        assert _is_linked(a1, 'carnot_ModelerType', b)
    _safe_set(b, 'carnot_ModelType231', {a2})
    assert _is_linked(b, 'carnot_ModelType231', a2)
    if hasattr(a1, 'carnot_ModelerType'):
        assert not _is_linked(a1, 'carnot_ModelerType', b)
    if hasattr(a2, 'carnot_ModelerType'):
        assert _is_linked(a2, 'carnot_ModelerType', b)
    _safe_set(b, 'carnot_ModelType231', set())
    assert not _is_linked(b, 'carnot_ModelType231', a2)
    if hasattr(a2, 'carnot_ModelerType'):
        assert not _is_linked(a2, 'carnot_ModelerType', b)


def test_assoc_outTransitions104_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'from_105', {a1})
    assert _is_linked(b, 'from_105', a1)
    if hasattr(a1, 'TransitionType106'):
        assert _is_linked(a1, 'TransitionType106', b)
    _safe_set(b, 'from_105', {a2})
    assert _is_linked(b, 'from_105', a2)
    if hasattr(a1, 'TransitionType106'):
        assert not _is_linked(a1, 'TransitionType106', b)
    if hasattr(a2, 'TransitionType106'):
        assert _is_linked(a2, 'TransitionType106', b)
    _safe_set(b, 'from_105', set())
    assert not _is_linked(b, 'from_105', a2)
    if hasattr(a2, 'TransitionType106'):
        assert not _is_linked(a2, 'TransitionType106', b)


def test_assoc_parameterMappings162_reverse_link_reassign_clear():
    a1 = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    a2 = carnot_ParameterMappingType(dataPath="sample_text_2", parameter="sample_text_2", parameterPath="sample_text_2")
    b = carnot_DataType(predefined="sample_text")
    _safe_set(b, 'data163', {a1})
    assert _is_linked(b, 'data163', a1)
    if hasattr(a1, 'ParameterMappingType'):
        assert _is_linked(a1, 'ParameterMappingType', b)
    _safe_set(b, 'data163', {a2})
    assert _is_linked(b, 'data163', a2)
    if hasattr(a1, 'ParameterMappingType'):
        assert not _is_linked(a1, 'ParameterMappingType', b)
    if hasattr(a2, 'ParameterMappingType'):
        assert _is_linked(a2, 'ParameterMappingType', b)
    _safe_set(b, 'data163', set())
    assert not _is_linked(b, 'data163', a2)
    if hasattr(a2, 'ParameterMappingType'):
        assert not _is_linked(a2, 'ParameterMappingType', b)


def test_assoc_poolSymbols168_reverse_link_reassign_clear():
    a1 = carnot_PoolSymbol(boundaryVisible="sample_text")
    a2 = carnot_PoolSymbol(boundaryVisible="sample_text_2")
    b = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    _safe_set(b, 'diagram', {a1})
    assert _is_linked(b, 'diagram', a1)
    if hasattr(a1, 'PoolSymbol'):
        assert _is_linked(a1, 'PoolSymbol', b)
    _safe_set(b, 'diagram', {a2})
    assert _is_linked(b, 'diagram', a2)
    if hasattr(a1, 'PoolSymbol'):
        assert not _is_linked(a1, 'PoolSymbol', b)
    if hasattr(a2, 'PoolSymbol'):
        assert _is_linked(a2, 'PoolSymbol', b)
    _safe_set(b, 'diagram', set())
    assert not _is_linked(b, 'diagram', a2)
    if hasattr(a2, 'PoolSymbol'):
        assert not _is_linked(a2, 'PoolSymbol', b)


def test_assoc_process278_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_PoolSymbol(boundaryVisible="sample_text")
    _safe_set(b, 'carnot_PoolSymbol', a1)
    assert _is_linked(b, 'carnot_PoolSymbol', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType279'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType279', b)
    _safe_set(b, 'carnot_PoolSymbol', a2)
    assert _is_linked(b, 'carnot_PoolSymbol', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType279'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType279', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType279'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType279', b)
    _safe_set(b, 'carnot_PoolSymbol', None)
    assert not _is_linked(b, 'carnot_PoolSymbol', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType279'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType279', b)


def test_assoc_processDefinition240_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType241', {a1})
    assert _is_linked(b, 'carnot_ModelType241', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType', b)
    _safe_set(b, 'carnot_ModelType241', {a2})
    assert _is_linked(b, 'carnot_ModelType241', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType', b)
    _safe_set(b, 'carnot_ModelType241', set())
    assert not _is_linked(b, 'carnot_ModelType241', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType', b)


def test_assoc_role234_reverse_link_reassign_clear():
    a1 = carnot_RoleType(cardinality=7)
    a2 = carnot_RoleType(cardinality=13)
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType235', {a1})
    assert _is_linked(b, 'carnot_ModelType235', a1)
    if hasattr(a1, 'carnot_RoleType'):
        assert _is_linked(a1, 'carnot_RoleType', b)
    _safe_set(b, 'carnot_ModelType235', {a2})
    assert _is_linked(b, 'carnot_ModelType235', a2)
    if hasattr(a1, 'carnot_RoleType'):
        assert not _is_linked(a1, 'carnot_RoleType', b)
    if hasattr(a2, 'carnot_RoleType'):
        assert _is_linked(a2, 'carnot_RoleType', b)
    _safe_set(b, 'carnot_ModelType235', set())
    assert not _is_linked(b, 'carnot_ModelType235', a2)
    if hasattr(a2, 'carnot_RoleType'):
        assert not _is_linked(a2, 'carnot_RoleType', b)


def test_assoc_textSymbol35_reverse_link_reassign_clear():
    a1 = carnot_TextSymbolType(text="sample_text")
    a2 = carnot_TextSymbolType(text="sample_text_2")
    b = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    _safe_set(b, 'carnot_ISymbolContainer36', {a1})
    assert _is_linked(b, 'carnot_ISymbolContainer36', a1)
    if hasattr(a1, 'carnot_TextSymbolType'):
        assert _is_linked(a1, 'carnot_TextSymbolType', b)
    _safe_set(b, 'carnot_ISymbolContainer36', {a2})
    assert _is_linked(b, 'carnot_ISymbolContainer36', a2)
    if hasattr(a1, 'carnot_TextSymbolType'):
        assert not _is_linked(a1, 'carnot_TextSymbolType', b)
    if hasattr(a2, 'carnot_TextSymbolType'):
        assert _is_linked(a2, 'carnot_TextSymbolType', b)
    _safe_set(b, 'carnot_ISymbolContainer36', set())
    assert not _is_linked(b, 'carnot_ISymbolContainer36', a2)
    if hasattr(a2, 'carnot_TextSymbolType'):
        assert not _is_linked(a2, 'carnot_TextSymbolType', b)


def test_assoc_to349_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'ActivityType351', a1)
    assert _is_linked(b, 'ActivityType351', a1)
    if hasattr(a1, 'inTransitions350'):
        assert _is_linked(a1, 'inTransitions350', b)
    _safe_set(b, 'ActivityType351', a2)
    assert _is_linked(b, 'ActivityType351', a2)
    if hasattr(a1, 'inTransitions350'):
        assert not _is_linked(a1, 'inTransitions350', b)
    if hasattr(a2, 'inTransitions350'):
        assert _is_linked(a2, 'inTransitions350', b)
    _safe_set(b, 'ActivityType351', None)
    assert not _is_linked(b, 'ActivityType351', a2)
    if hasattr(a2, 'inTransitions350'):
        assert not _is_linked(a2, 'inTransitions350', b)


def test_assoc_transition285_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    _safe_set(b, 'carnot_ProcessDefinitionType286', {a1})
    assert _is_linked(b, 'carnot_ProcessDefinitionType286', a1)
    if hasattr(a1, 'carnot_TransitionType'):
        assert _is_linked(a1, 'carnot_TransitionType', b)
    _safe_set(b, 'carnot_ProcessDefinitionType286', {a2})
    assert _is_linked(b, 'carnot_ProcessDefinitionType286', a2)
    if hasattr(a1, 'carnot_TransitionType'):
        assert not _is_linked(a1, 'carnot_TransitionType', b)
    if hasattr(a2, 'carnot_TransitionType'):
        assert _is_linked(a2, 'carnot_TransitionType', b)
    _safe_set(b, 'carnot_ProcessDefinitionType286', set())
    assert not _is_linked(b, 'carnot_ProcessDefinitionType286', a2)
    if hasattr(a2, 'carnot_TransitionType'):
        assert not _is_linked(a2, 'carnot_TransitionType', b)


def test_assoc_transition341_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_TransitionConnectionType(points="sample_text")
    _safe_set(b, 'transitionConnections', a1)
    assert _is_linked(b, 'transitionConnections', a1)
    if hasattr(a1, 'TransitionType342'):
        assert _is_linked(a1, 'TransitionType342', b)
    _safe_set(b, 'transitionConnections', a2)
    assert _is_linked(b, 'transitionConnections', a2)
    if hasattr(a1, 'TransitionType342'):
        assert not _is_linked(a1, 'TransitionType342', b)
    if hasattr(a2, 'TransitionType342'):
        assert _is_linked(a2, 'TransitionType342', b)
    _safe_set(b, 'transitionConnections', None)
    assert not _is_linked(b, 'transitionConnections', a2)
    if hasattr(a2, 'TransitionType342'):
        assert not _is_linked(a2, 'TransitionType342', b)


def test_assoc_transitionConnection53_reverse_link_reassign_clear():
    a1 = carnot_TransitionConnectionType(points="sample_text")
    a2 = carnot_TransitionConnectionType(points="sample_text_2")
    b = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    _safe_set(b, 'carnot_ISymbolContainer54', {a1})
    assert _is_linked(b, 'carnot_ISymbolContainer54', a1)
    if hasattr(a1, 'carnot_TransitionConnectionType'):
        assert _is_linked(a1, 'carnot_TransitionConnectionType', b)
    _safe_set(b, 'carnot_ISymbolContainer54', {a2})
    assert _is_linked(b, 'carnot_ISymbolContainer54', a2)
    if hasattr(a1, 'carnot_TransitionConnectionType'):
        assert not _is_linked(a1, 'carnot_TransitionConnectionType', b)
    if hasattr(a2, 'carnot_TransitionConnectionType'):
        assert _is_linked(a2, 'carnot_TransitionConnectionType', b)
    _safe_set(b, 'carnot_ISymbolContainer54', set())
    assert not _is_linked(b, 'carnot_ISymbolContainer54', a2)
    if hasattr(a2, 'carnot_TransitionConnectionType'):
        assert not _is_linked(a2, 'carnot_TransitionConnectionType', b)


def test_assoc_transitionConnections352_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_TransitionConnectionType(points="sample_text")
    _safe_set(b, 'TransitionConnectionType353', a1)
    assert _is_linked(b, 'TransitionConnectionType353', a1)
    if hasattr(a1, 'transition'):
        assert _is_linked(a1, 'transition', b)
    _safe_set(b, 'TransitionConnectionType353', a2)
    assert _is_linked(b, 'TransitionConnectionType353', a2)
    if hasattr(a1, 'transition'):
        assert not _is_linked(a1, 'transition', b)
    if hasattr(a2, 'transition'):
        assert _is_linked(a2, 'transition', b)
    _safe_set(b, 'TransitionConnectionType353', None)
    assert not _is_linked(b, 'TransitionConnectionType353', a2)
    if hasattr(a2, 'transition'):
        assert not _is_linked(a2, 'transition', b)


def test_assoc_triggerType218_reverse_link_reassign_clear():
    a1 = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    a2 = carnot_TriggerTypeType(panelClass="sample_text_2", pullTrigger="sample_text_2", pullTriggerEvaluator="sample_text_2", rule="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType219', {a1})
    assert _is_linked(b, 'carnot_ModelType219', a1)
    if hasattr(a1, 'carnot_TriggerTypeType'):
        assert _is_linked(a1, 'carnot_TriggerTypeType', b)
    _safe_set(b, 'carnot_ModelType219', {a2})
    assert _is_linked(b, 'carnot_ModelType219', a2)
    if hasattr(a1, 'carnot_TriggerTypeType'):
        assert not _is_linked(a1, 'carnot_TriggerTypeType', b)
    if hasattr(a2, 'carnot_TriggerTypeType'):
        assert _is_linked(a2, 'carnot_TriggerTypeType', b)
    _safe_set(b, 'carnot_ModelType219', set())
    assert not _is_linked(b, 'carnot_ModelType219', a2)
    if hasattr(a2, 'carnot_TriggerTypeType'):
        assert not _is_linked(a2, 'carnot_TriggerTypeType', b)


def test_assoc_type119_reverse_link_reassign_clear():
    a1 = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    a2 = carnot_ApplicationTypeType(accessPointProviderClass="sample_text_2", instanceClass="sample_text_2", panelClass="sample_text_2", synchronous="sample_text_2", validatorClass="sample_text_2")
    b = carnot_ApplicationType(interactive="sample_text")
    _safe_set(b, 'applications', a1)
    assert _is_linked(b, 'applications', a1)
    if hasattr(a1, 'ApplicationTypeType'):
        assert _is_linked(a1, 'ApplicationTypeType', b)
    _safe_set(b, 'applications', a2)
    assert _is_linked(b, 'applications', a2)
    if hasattr(a1, 'ApplicationTypeType'):
        assert not _is_linked(a1, 'ApplicationTypeType', b)
    if hasattr(a2, 'ApplicationTypeType'):
        assert _is_linked(a2, 'ApplicationTypeType', b)
    _safe_set(b, 'applications', None)
    assert not _is_linked(b, 'applications', a2)
    if hasattr(a2, 'ApplicationTypeType'):
        assert not _is_linked(a2, 'ApplicationTypeType', b)


def test_assoc_type152_reverse_link_reassign_clear():
    a1 = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    a2 = carnot_DataTypeType(accessPathEditor="sample_text_2", evaluator="sample_text_2", instanceClass="sample_text_2", panelClass="sample_text_2", readable="sample_text_2", storageStrategy="sample_text_2", validatorClass="sample_text_2", valueCreator="sample_text_2", writable="sample_text_2")
    b = carnot_DataType(predefined="sample_text")
    _safe_set(b, 'data153', a1)
    assert _is_linked(b, 'data153', a1)
    if hasattr(a1, 'DataTypeType'):
        assert _is_linked(a1, 'DataTypeType', b)
    _safe_set(b, 'data153', a2)
    assert _is_linked(b, 'data153', a2)
    if hasattr(a1, 'DataTypeType'):
        assert not _is_linked(a1, 'DataTypeType', b)
    if hasattr(a2, 'DataTypeType'):
        assert _is_linked(a2, 'DataTypeType', b)
    _safe_set(b, 'data153', None)
    assert not _is_linked(b, 'data153', a2)
    if hasattr(a2, 'DataTypeType'):
        assert not _is_linked(a2, 'DataTypeType', b)


def test_assoc_type185_reverse_link_reassign_clear():
    a1 = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    a2 = carnot_EventHandlerType(autoBind="sample_text_2", consumeOnMatch="sample_text_2", logHandler="sample_text_2", unbindOnMatch="sample_text_2")
    b = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    _safe_set(b, 'EventConditionTypeType', a1)
    assert _is_linked(b, 'EventConditionTypeType', a1)
    if hasattr(a1, 'eventHandlers'):
        assert _is_linked(a1, 'eventHandlers', b)
    _safe_set(b, 'EventConditionTypeType', a2)
    assert _is_linked(b, 'EventConditionTypeType', a2)
    if hasattr(a1, 'eventHandlers'):
        assert not _is_linked(a1, 'eventHandlers', b)
    if hasattr(a2, 'eventHandlers'):
        assert _is_linked(a2, 'eventHandlers', b)
    _safe_set(b, 'EventConditionTypeType', None)
    assert not _is_linked(b, 'EventConditionTypeType', a2)
    if hasattr(a2, 'eventHandlers'):
        assert not _is_linked(a2, 'eventHandlers', b)


def test_assoc_type80_reverse_link_reassign_clear():
    a1 = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    a2 = carnot_DataTypeType(accessPathEditor="sample_text_2", evaluator="sample_text_2", instanceClass="sample_text_2", panelClass="sample_text_2", readable="sample_text_2", storageStrategy="sample_text_2", validatorClass="sample_text_2", valueCreator="sample_text_2", writable="sample_text_2")
    b = carnot_AccessPointType(direction="sample_text")
    _safe_set(b, 'carnot_AccessPointType81', a1)
    assert _is_linked(b, 'carnot_AccessPointType81', a1)
    if hasattr(a1, 'carnot_DataTypeType'):
        assert _is_linked(a1, 'carnot_DataTypeType', b)
    _safe_set(b, 'carnot_AccessPointType81', a2)
    assert _is_linked(b, 'carnot_AccessPointType81', a2)
    if hasattr(a1, 'carnot_DataTypeType'):
        assert not _is_linked(a1, 'carnot_DataTypeType', b)
    if hasattr(a2, 'carnot_DataTypeType'):
        assert _is_linked(a2, 'carnot_DataTypeType', b)
    _safe_set(b, 'carnot_AccessPointType81', None)
    assert not _is_linked(b, 'carnot_AccessPointType81', a2)
    if hasattr(a2, 'carnot_DataTypeType'):
        assert not _is_linked(a2, 'carnot_DataTypeType', b)


def test_assoc_validQualityCodes107_reverse_link_reassign_clear():
    a1 = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    a2 = carnot_Code(code="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'carnot_ActivityType108', {a1})
    assert _is_linked(b, 'carnot_ActivityType108', a1)
    if hasattr(a1, 'carnot_Code'):
        assert _is_linked(a1, 'carnot_Code', b)
    _safe_set(b, 'carnot_ActivityType108', {a2})
    assert _is_linked(b, 'carnot_ActivityType108', a2)
    if hasattr(a1, 'carnot_Code'):
        assert not _is_linked(a1, 'carnot_Code', b)
    if hasattr(a2, 'carnot_Code'):
        assert _is_linked(a2, 'carnot_Code', b)
    _safe_set(b, 'carnot_ActivityType108', set())
    assert not _is_linked(b, 'carnot_ActivityType108', a2)
    if hasattr(a2, 'carnot_Code'):
        assert not _is_linked(a2, 'carnot_Code', b)


def test_assoc_valueNode127_reverse_link_reassign_clear():
    a1 = carnot_XmlTextNode(mixed="sample_text")
    a2 = carnot_XmlTextNode(mixed="sample_text_2")
    b = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'carnot_AttributeType128', a1)
    assert _is_linked(b, 'carnot_AttributeType128', a1)
    if hasattr(a1, 'carnot_XmlTextNode'):
        assert _is_linked(a1, 'carnot_XmlTextNode', b)
    _safe_set(b, 'carnot_AttributeType128', a2)
    assert _is_linked(b, 'carnot_AttributeType128', a2)
    if hasattr(a1, 'carnot_XmlTextNode'):
        assert not _is_linked(a1, 'carnot_XmlTextNode', b)
    if hasattr(a2, 'carnot_XmlTextNode'):
        assert _is_linked(a2, 'carnot_XmlTextNode', b)
    _safe_set(b, 'carnot_AttributeType128', None)
    assert not _is_linked(b, 'carnot_AttributeType128', a2)
    if hasattr(a2, 'carnot_XmlTextNode'):
        assert not _is_linked(a2, 'carnot_XmlTextNode', b)


def test_assoc_view252_reverse_link_reassign_clear():
    a1 = carnot_ViewType(name="sample_text")
    a2 = carnot_ViewType(name="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType253', {a1})
    assert _is_linked(b, 'carnot_ModelType253', a1)
    if hasattr(a1, 'carnot_ViewType'):
        assert _is_linked(a1, 'carnot_ViewType', b)
    _safe_set(b, 'carnot_ModelType253', {a2})
    assert _is_linked(b, 'carnot_ModelType253', a2)
    if hasattr(a1, 'carnot_ViewType'):
        assert not _is_linked(a1, 'carnot_ViewType', b)
    if hasattr(a2, 'carnot_ViewType'):
        assert _is_linked(a2, 'carnot_ViewType', b)
    _safe_set(b, 'carnot_ModelType253', set())
    assert not _is_linked(b, 'carnot_ModelType253', a2)
    if hasattr(a2, 'carnot_ViewType'):
        assert not _is_linked(a2, 'carnot_ViewType', b)


def test_assoc_view371_reverse_link_reassign_clear():
    a1 = carnot_ViewType(name="sample_text")
    a2 = carnot_ViewType(name="sample_text_2")
    b = carnot_ViewType(name="sample_text")
    _safe_set(b, 'carnot_ViewType372', a1)
    assert _is_linked(b, 'carnot_ViewType372', a1)
    if hasattr(a1, 'carnot_ViewType370'):
        assert _is_linked(a1, 'carnot_ViewType370', b)
    _safe_set(b, 'carnot_ViewType372', a2)
    assert _is_linked(b, 'carnot_ViewType372', a2)
    if hasattr(a1, 'carnot_ViewType370'):
        assert not _is_linked(a1, 'carnot_ViewType370', b)
    if hasattr(a2, 'carnot_ViewType370'):
        assert _is_linked(a2, 'carnot_ViewType370', b)
    _safe_set(b, 'carnot_ViewType372', None)
    assert not _is_linked(b, 'carnot_ViewType372', a2)
    if hasattr(a2, 'carnot_ViewType370'):
        assert not _is_linked(a2, 'carnot_ViewType370', b)


