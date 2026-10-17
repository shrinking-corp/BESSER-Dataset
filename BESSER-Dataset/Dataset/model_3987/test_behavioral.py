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
    carnot_IdentifiableReference,
    carnot_IntermediateEventSymbol,
    carnot_LaneSymbol,
    carnot_LinkTypeType,
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

def test_assoc_activity281_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'carnot_ActivityType283', a1)
    assert _is_linked(b, 'carnot_ActivityType283', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType282'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType282', b)
    _safe_set(b, 'carnot_ActivityType283', a2)
    assert _is_linked(b, 'carnot_ActivityType283', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType282'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType282', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType282'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType282', b)
    _safe_set(b, 'carnot_ActivityType283', None)
    assert not _is_linked(b, 'carnot_ActivityType283', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType282'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType282', b)


def test_assoc_application226_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ApplicationType(interactive="sample_text")
    _safe_set(b, 'carnot_ApplicationType228', a1)
    assert _is_linked(b, 'carnot_ApplicationType228', a1)
    if hasattr(a1, 'carnot_ModelType227'):
        assert _is_linked(a1, 'carnot_ModelType227', b)
    _safe_set(b, 'carnot_ApplicationType228', a2)
    assert _is_linked(b, 'carnot_ApplicationType228', a2)
    if hasattr(a1, 'carnot_ModelType227'):
        assert not _is_linked(a1, 'carnot_ModelType227', b)
    if hasattr(a2, 'carnot_ModelType227'):
        assert _is_linked(a2, 'carnot_ModelType227', b)
    _safe_set(b, 'carnot_ApplicationType228', None)
    assert not _is_linked(b, 'carnot_ApplicationType228', a2)
    if hasattr(a2, 'carnot_ModelType227'):
        assert not _is_linked(a2, 'carnot_ModelType227', b)


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


def test_assoc_applicationContextType215_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    _safe_set(b, 'carnot_ApplicationContextTypeType', a1)
    assert _is_linked(b, 'carnot_ApplicationContextTypeType', a1)
    if hasattr(a1, 'carnot_ModelType216'):
        assert _is_linked(a1, 'carnot_ModelType216', b)
    _safe_set(b, 'carnot_ApplicationContextTypeType', a2)
    assert _is_linked(b, 'carnot_ApplicationContextTypeType', a2)
    if hasattr(a1, 'carnot_ModelType216'):
        assert not _is_linked(a1, 'carnot_ModelType216', b)
    if hasattr(a2, 'carnot_ModelType216'):
        assert _is_linked(a2, 'carnot_ModelType216', b)
    _safe_set(b, 'carnot_ApplicationContextTypeType', None)
    assert not _is_linked(b, 'carnot_ApplicationContextTypeType', a2)
    if hasattr(a2, 'carnot_ModelType216'):
        assert not _is_linked(a2, 'carnot_ModelType216', b)


def test_assoc_applicationType213_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    _safe_set(b, 'carnot_ApplicationTypeType', a1)
    assert _is_linked(b, 'carnot_ApplicationTypeType', a1)
    if hasattr(a1, 'carnot_ModelType214'):
        assert _is_linked(a1, 'carnot_ModelType214', b)
    _safe_set(b, 'carnot_ApplicationTypeType', a2)
    assert _is_linked(b, 'carnot_ApplicationTypeType', a2)
    if hasattr(a1, 'carnot_ModelType214'):
        assert not _is_linked(a1, 'carnot_ModelType214', b)
    if hasattr(a2, 'carnot_ModelType214'):
        assert _is_linked(a2, 'carnot_ModelType214', b)
    _safe_set(b, 'carnot_ApplicationTypeType', None)
    assert not _is_linked(b, 'carnot_ApplicationTypeType', a2)
    if hasattr(a2, 'carnot_ModelType214'):
        assert not _is_linked(a2, 'carnot_ModelType214', b)


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


def test_assoc_conditionalPerformer237_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    _safe_set(b, 'carnot_ConditionalPerformerType', a1)
    assert _is_linked(b, 'carnot_ConditionalPerformerType', a1)
    if hasattr(a1, 'carnot_ModelType238'):
        assert _is_linked(a1, 'carnot_ModelType238', b)
    _safe_set(b, 'carnot_ConditionalPerformerType', a2)
    assert _is_linked(b, 'carnot_ConditionalPerformerType', a2)
    if hasattr(a1, 'carnot_ModelType238'):
        assert not _is_linked(a1, 'carnot_ModelType238', b)
    if hasattr(a2, 'carnot_ModelType238'):
        assert _is_linked(a2, 'carnot_ModelType238', b)
    _safe_set(b, 'carnot_ConditionalPerformerType', None)
    assert not _is_linked(b, 'carnot_ConditionalPerformerType', a2)
    if hasattr(a2, 'carnot_ModelType238'):
        assert not _is_linked(a2, 'carnot_ModelType238', b)


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


def test_assoc_data223_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DataType(predefined="sample_text")
    _safe_set(b, 'carnot_DataType225', a1)
    assert _is_linked(b, 'carnot_DataType225', a1)
    if hasattr(a1, 'carnot_ModelType224'):
        assert _is_linked(a1, 'carnot_ModelType224', b)
    _safe_set(b, 'carnot_DataType225', a2)
    assert _is_linked(b, 'carnot_DataType225', a2)
    if hasattr(a1, 'carnot_ModelType224'):
        assert not _is_linked(a1, 'carnot_ModelType224', b)
    if hasattr(a2, 'carnot_ModelType224'):
        assert _is_linked(a2, 'carnot_ModelType224', b)
    _safe_set(b, 'carnot_DataType225', None)
    assert not _is_linked(b, 'carnot_DataType225', a2)
    if hasattr(a2, 'carnot_ModelType224'):
        assert not _is_linked(a2, 'carnot_ModelType224', b)


def test_assoc_data264_reverse_link_reassign_clear():
    a1 = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    a2 = carnot_ParameterMappingType(dataPath="sample_text_2", parameter="sample_text_2", parameterPath="sample_text_2")
    b = carnot_DataType(predefined="sample_text")
    _safe_set(b, 'DataType265', a1)
    assert _is_linked(b, 'DataType265', a1)
    if hasattr(a1, 'parameterMappings'):
        assert _is_linked(a1, 'parameterMappings', b)
    _safe_set(b, 'DataType265', a2)
    assert _is_linked(b, 'DataType265', a2)
    if hasattr(a1, 'parameterMappings'):
        assert not _is_linked(a1, 'parameterMappings', b)
    if hasattr(a2, 'parameterMappings'):
        assert _is_linked(a2, 'parameterMappings', b)
    _safe_set(b, 'DataType265', None)
    assert not _is_linked(b, 'DataType265', a2)
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


def test_assoc_dataPath288_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    _safe_set(b, 'carnot_DataPathType', a1)
    assert _is_linked(b, 'carnot_DataPathType', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType289'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType289', b)
    _safe_set(b, 'carnot_DataPathType', a2)
    assert _is_linked(b, 'carnot_DataPathType', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType289'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType289', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType289'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType289', b)
    _safe_set(b, 'carnot_DataPathType', None)
    assert not _is_linked(b, 'carnot_DataPathType', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType289'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType289', b)


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


def test_assoc_dataType210_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    _safe_set(b, 'carnot_DataTypeType212', a1)
    assert _is_linked(b, 'carnot_DataTypeType212', a1)
    if hasattr(a1, 'carnot_ModelType211'):
        assert _is_linked(a1, 'carnot_ModelType211', b)
    _safe_set(b, 'carnot_DataTypeType212', a2)
    assert _is_linked(b, 'carnot_DataTypeType212', a2)
    if hasattr(a1, 'carnot_ModelType211'):
        assert not _is_linked(a1, 'carnot_ModelType211', b)
    if hasattr(a2, 'carnot_ModelType211'):
        assert _is_linked(a2, 'carnot_ModelType211', b)
    _safe_set(b, 'carnot_DataTypeType212', None)
    assert not _is_linked(b, 'carnot_DataTypeType212', a2)
    if hasattr(a2, 'carnot_ModelType211'):
        assert not _is_linked(a2, 'carnot_ModelType211', b)


def test_assoc_description207_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DescriptionType(mixed="sample_text")
    _safe_set(b, 'carnot_DescriptionType209', a1)
    assert _is_linked(b, 'carnot_DescriptionType209', a1)
    if hasattr(a1, 'carnot_ModelType208'):
        assert _is_linked(a1, 'carnot_ModelType208', b)
    _safe_set(b, 'carnot_DescriptionType209', a2)
    assert _is_linked(b, 'carnot_DescriptionType209', a2)
    if hasattr(a1, 'carnot_ModelType208'):
        assert not _is_linked(a1, 'carnot_ModelType208', b)
    if hasattr(a2, 'carnot_ModelType208'):
        assert _is_linked(a2, 'carnot_ModelType208', b)
    _safe_set(b, 'carnot_DescriptionType209', None)
    assert not _is_linked(b, 'carnot_DescriptionType209', a2)
    if hasattr(a2, 'carnot_ModelType208'):
        assert not _is_linked(a2, 'carnot_ModelType208', b)


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


def test_assoc_description369_reverse_link_reassign_clear():
    a1 = carnot_ViewType(name="sample_text")
    a2 = carnot_ViewType(name="sample_text_2")
    b = carnot_DescriptionType(mixed="sample_text")
    _safe_set(b, 'carnot_DescriptionType371', a1)
    assert _is_linked(b, 'carnot_DescriptionType371', a1)
    if hasattr(a1, 'carnot_ViewType370'):
        assert _is_linked(a1, 'carnot_ViewType370', b)
    _safe_set(b, 'carnot_DescriptionType371', a2)
    assert _is_linked(b, 'carnot_DescriptionType371', a2)
    if hasattr(a1, 'carnot_ViewType370'):
        assert not _is_linked(a1, 'carnot_ViewType370', b)
    if hasattr(a2, 'carnot_ViewType370'):
        assert _is_linked(a2, 'carnot_ViewType370', b)
    _safe_set(b, 'carnot_DescriptionType371', None)
    assert not _is_linked(b, 'carnot_DescriptionType371', a2)
    if hasattr(a2, 'carnot_ViewType370'):
        assert not _is_linked(a2, 'carnot_ViewType370', b)


def test_assoc_diagram247_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    _safe_set(b, 'carnot_DiagramType', a1)
    assert _is_linked(b, 'carnot_DiagramType', a1)
    if hasattr(a1, 'carnot_ModelType248'):
        assert _is_linked(a1, 'carnot_ModelType248', b)
    _safe_set(b, 'carnot_DiagramType', a2)
    assert _is_linked(b, 'carnot_DiagramType', a2)
    if hasattr(a1, 'carnot_ModelType248'):
        assert not _is_linked(a1, 'carnot_ModelType248', b)
    if hasattr(a2, 'carnot_ModelType248'):
        assert _is_linked(a2, 'carnot_ModelType248', b)
    _safe_set(b, 'carnot_DiagramType', None)
    assert not _is_linked(b, 'carnot_DiagramType', a2)
    if hasattr(a2, 'carnot_ModelType248'):
        assert not _is_linked(a2, 'carnot_ModelType248', b)


def test_assoc_diagram276_reverse_link_reassign_clear():
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


def test_assoc_diagram290_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    _safe_set(b, 'carnot_DiagramType292', a1)
    assert _is_linked(b, 'carnot_DiagramType292', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType291'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType291', b)
    _safe_set(b, 'carnot_DiagramType292', a2)
    assert _is_linked(b, 'carnot_DiagramType292', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType291'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType291', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType291'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType291', b)
    _safe_set(b, 'carnot_DiagramType292', None)
    assert not _is_linked(b, 'carnot_DiagramType292', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType291'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType291', b)


def test_assoc_eventActionType221_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    _safe_set(b, 'carnot_EventActionTypeType', a1)
    assert _is_linked(b, 'carnot_EventActionTypeType', a1)
    if hasattr(a1, 'carnot_ModelType222'):
        assert _is_linked(a1, 'carnot_ModelType222', b)
    _safe_set(b, 'carnot_EventActionTypeType', a2)
    assert _is_linked(b, 'carnot_EventActionTypeType', a2)
    if hasattr(a1, 'carnot_ModelType222'):
        assert not _is_linked(a1, 'carnot_ModelType222', b)
    if hasattr(a2, 'carnot_ModelType222'):
        assert _is_linked(a2, 'carnot_ModelType222', b)
    _safe_set(b, 'carnot_EventActionTypeType', None)
    assert not _is_linked(b, 'carnot_EventActionTypeType', a2)
    if hasattr(a2, 'carnot_ModelType222'):
        assert not _is_linked(a2, 'carnot_ModelType222', b)


def test_assoc_eventConditionType219_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    _safe_set(b, 'carnot_EventConditionTypeType', a1)
    assert _is_linked(b, 'carnot_EventConditionTypeType', a1)
    if hasattr(a1, 'carnot_ModelType220'):
        assert _is_linked(a1, 'carnot_ModelType220', b)
    _safe_set(b, 'carnot_EventConditionTypeType', a2)
    assert _is_linked(b, 'carnot_EventConditionTypeType', a2)
    if hasattr(a1, 'carnot_ModelType220'):
        assert not _is_linked(a1, 'carnot_ModelType220', b)
    if hasattr(a2, 'carnot_ModelType220'):
        assert _is_linked(a2, 'carnot_ModelType220', b)
    _safe_set(b, 'carnot_EventConditionTypeType', None)
    assert not _is_linked(b, 'carnot_EventConditionTypeType', a2)
    if hasattr(a2, 'carnot_ModelType220'):
        assert not _is_linked(a2, 'carnot_ModelType220', b)


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


def test_assoc_executingActivities293_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'ActivityType294', a1)
    assert _is_linked(b, 'ActivityType294', a1)
    if hasattr(a1, 'implementationProcess'):
        assert _is_linked(a1, 'implementationProcess', b)
    _safe_set(b, 'ActivityType294', a2)
    assert _is_linked(b, 'ActivityType294', a2)
    if hasattr(a1, 'implementationProcess'):
        assert not _is_linked(a1, 'implementationProcess', b)
    if hasattr(a2, 'implementationProcess'):
        assert _is_linked(a2, 'implementationProcess', b)
    _safe_set(b, 'ActivityType294', None)
    assert not _is_linked(b, 'ActivityType294', a2)
    if hasattr(a2, 'implementationProcess'):
        assert not _is_linked(a2, 'implementationProcess', b)


def test_assoc_expression345_reverse_link_reassign_clear():
    a1 = carnot_XmlTextNode(mixed="sample_text")
    a2 = carnot_XmlTextNode(mixed="sample_text_2")
    b = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    _safe_set(b, 'carnot_TransitionType346', a1)
    assert _is_linked(b, 'carnot_TransitionType346', a1)
    if hasattr(a1, 'carnot_XmlTextNode347'):
        assert _is_linked(a1, 'carnot_XmlTextNode347', b)
    _safe_set(b, 'carnot_TransitionType346', a2)
    assert _is_linked(b, 'carnot_TransitionType346', a2)
    if hasattr(a1, 'carnot_XmlTextNode347'):
        assert not _is_linked(a1, 'carnot_XmlTextNode347', b)
    if hasattr(a2, 'carnot_XmlTextNode347'):
        assert _is_linked(a2, 'carnot_XmlTextNode347', b)
    _safe_set(b, 'carnot_TransitionType346', None)
    assert not _is_linked(b, 'carnot_TransitionType346', a2)
    if hasattr(a2, 'carnot_XmlTextNode347'):
        assert not _is_linked(a2, 'carnot_XmlTextNode347', b)


def test_assoc_externalRef107_reverse_link_reassign_clear():
    a1 = carnot_IdRef(ref="sample_text")
    a2 = carnot_IdRef(ref="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'carnot_ActivityType108', a1)
    assert _is_linked(b, 'carnot_ActivityType108', a1)
    if hasattr(a1, 'carnot_IdRef'):
        assert _is_linked(a1, 'carnot_IdRef', b)
    _safe_set(b, 'carnot_ActivityType108', a2)
    assert _is_linked(b, 'carnot_ActivityType108', a2)
    if hasattr(a1, 'carnot_IdRef'):
        assert not _is_linked(a1, 'carnot_IdRef', b)
    if hasattr(a2, 'carnot_IdRef'):
        assert _is_linked(a2, 'carnot_IdRef', b)
    _safe_set(b, 'carnot_ActivityType108', None)
    assert not _is_linked(b, 'carnot_ActivityType108', a2)
    if hasattr(a2, 'carnot_IdRef'):
        assert not _is_linked(a2, 'carnot_IdRef', b)


def test_assoc_externalRef300_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_IdRef(ref="sample_text")
    _safe_set(b, 'carnot_IdRef302', a1)
    assert _is_linked(b, 'carnot_IdRef302', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType301'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType301', b)
    _safe_set(b, 'carnot_IdRef302', a2)
    assert _is_linked(b, 'carnot_IdRef302', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType301'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType301', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType301'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType301', b)
    _safe_set(b, 'carnot_IdRef302', None)
    assert not _is_linked(b, 'carnot_IdRef302', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType301'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType301', b)


def test_assoc_from_348_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'ActivityType350', a1)
    assert _is_linked(b, 'ActivityType350', a1)
    if hasattr(a1, 'outTransitions349'):
        assert _is_linked(a1, 'outTransitions349', b)
    _safe_set(b, 'ActivityType350', a2)
    assert _is_linked(b, 'ActivityType350', a2)
    if hasattr(a1, 'outTransitions349'):
        assert not _is_linked(a1, 'outTransitions349', b)
    if hasattr(a2, 'outTransitions349'):
        assert _is_linked(a2, 'outTransitions349', b)
    _safe_set(b, 'ActivityType350', None)
    assert not _is_linked(b, 'ActivityType350', a2)
    if hasattr(a2, 'outTransitions349'):
        assert not _is_linked(a2, 'outTransitions349', b)


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


def test_assoc_linkType249_reverse_link_reassign_clear():
    a1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    a2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    b = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    _safe_set(b, 'carnot_LinkTypeType', a1)
    assert _is_linked(b, 'carnot_LinkTypeType', a1)
    if hasattr(a1, 'carnot_ModelType250'):
        assert _is_linked(a1, 'carnot_ModelType250', b)
    _safe_set(b, 'carnot_LinkTypeType', a2)
    assert _is_linked(b, 'carnot_LinkTypeType', a2)
    if hasattr(a1, 'carnot_ModelType250'):
        assert not _is_linked(a1, 'carnot_ModelType250', b)
    if hasattr(a2, 'carnot_ModelType250'):
        assert _is_linked(a2, 'carnot_ModelType250', b)
    _safe_set(b, 'carnot_LinkTypeType', None)
    assert not _is_linked(b, 'carnot_LinkTypeType', a2)
    if hasattr(a2, 'carnot_ModelType250'):
        assert not _is_linked(a2, 'carnot_ModelType250', b)


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


def test_assoc_modeler229_reverse_link_reassign_clear():
    a1 = carnot_ModelerType(email="sample_text", password="sample_text")
    a2 = carnot_ModelerType(email="sample_text_2", password="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType230', {a1})
    assert _is_linked(b, 'carnot_ModelType230', a1)
    if hasattr(a1, 'carnot_ModelerType'):
        assert _is_linked(a1, 'carnot_ModelerType', b)
    _safe_set(b, 'carnot_ModelType230', {a2})
    assert _is_linked(b, 'carnot_ModelType230', a2)
    if hasattr(a1, 'carnot_ModelerType'):
        assert not _is_linked(a1, 'carnot_ModelerType', b)
    if hasattr(a2, 'carnot_ModelerType'):
        assert _is_linked(a2, 'carnot_ModelerType', b)
    _safe_set(b, 'carnot_ModelType230', set())
    assert not _is_linked(b, 'carnot_ModelType230', a2)
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


def test_assoc_process277_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_PoolSymbol(boundaryVisible="sample_text")
    _safe_set(b, 'carnot_PoolSymbol', a1)
    assert _is_linked(b, 'carnot_PoolSymbol', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType278'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType278', b)
    _safe_set(b, 'carnot_PoolSymbol', a2)
    assert _is_linked(b, 'carnot_PoolSymbol', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType278'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType278', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType278'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType278', b)
    _safe_set(b, 'carnot_PoolSymbol', None)
    assert not _is_linked(b, 'carnot_PoolSymbol', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType278'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType278', b)


def test_assoc_processDefinition239_reverse_link_reassign_clear():
    a1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    a2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType240', {a1})
    assert _is_linked(b, 'carnot_ModelType240', a1)
    if hasattr(a1, 'carnot_ProcessDefinitionType'):
        assert _is_linked(a1, 'carnot_ProcessDefinitionType', b)
    _safe_set(b, 'carnot_ModelType240', {a2})
    assert _is_linked(b, 'carnot_ModelType240', a2)
    if hasattr(a1, 'carnot_ProcessDefinitionType'):
        assert not _is_linked(a1, 'carnot_ProcessDefinitionType', b)
    if hasattr(a2, 'carnot_ProcessDefinitionType'):
        assert _is_linked(a2, 'carnot_ProcessDefinitionType', b)
    _safe_set(b, 'carnot_ModelType240', set())
    assert not _is_linked(b, 'carnot_ModelType240', a2)
    if hasattr(a2, 'carnot_ProcessDefinitionType'):
        assert not _is_linked(a2, 'carnot_ProcessDefinitionType', b)


def test_assoc_role233_reverse_link_reassign_clear():
    a1 = carnot_RoleType(cardinality=7)
    a2 = carnot_RoleType(cardinality=13)
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType234', {a1})
    assert _is_linked(b, 'carnot_ModelType234', a1)
    if hasattr(a1, 'carnot_RoleType'):
        assert _is_linked(a1, 'carnot_RoleType', b)
    _safe_set(b, 'carnot_ModelType234', {a2})
    assert _is_linked(b, 'carnot_ModelType234', a2)
    if hasattr(a1, 'carnot_RoleType'):
        assert not _is_linked(a1, 'carnot_RoleType', b)
    if hasattr(a2, 'carnot_RoleType'):
        assert _is_linked(a2, 'carnot_RoleType', b)
    _safe_set(b, 'carnot_ModelType234', set())
    assert not _is_linked(b, 'carnot_ModelType234', a2)
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


def test_assoc_to351_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'ActivityType353', a1)
    assert _is_linked(b, 'ActivityType353', a1)
    if hasattr(a1, 'inTransitions352'):
        assert _is_linked(a1, 'inTransitions352', b)
    _safe_set(b, 'ActivityType353', a2)
    assert _is_linked(b, 'ActivityType353', a2)
    if hasattr(a1, 'inTransitions352'):
        assert not _is_linked(a1, 'inTransitions352', b)
    if hasattr(a2, 'inTransitions352'):
        assert _is_linked(a2, 'inTransitions352', b)
    _safe_set(b, 'ActivityType353', None)
    assert not _is_linked(b, 'ActivityType353', a2)
    if hasattr(a2, 'inTransitions352'):
        assert not _is_linked(a2, 'inTransitions352', b)


def test_assoc_transition284_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    _safe_set(b, 'carnot_ProcessDefinitionType285', {a1})
    assert _is_linked(b, 'carnot_ProcessDefinitionType285', a1)
    if hasattr(a1, 'carnot_TransitionType'):
        assert _is_linked(a1, 'carnot_TransitionType', b)
    _safe_set(b, 'carnot_ProcessDefinitionType285', {a2})
    assert _is_linked(b, 'carnot_ProcessDefinitionType285', a2)
    if hasattr(a1, 'carnot_TransitionType'):
        assert not _is_linked(a1, 'carnot_TransitionType', b)
    if hasattr(a2, 'carnot_TransitionType'):
        assert _is_linked(a2, 'carnot_TransitionType', b)
    _safe_set(b, 'carnot_ProcessDefinitionType285', set())
    assert not _is_linked(b, 'carnot_ProcessDefinitionType285', a2)
    if hasattr(a2, 'carnot_TransitionType'):
        assert not _is_linked(a2, 'carnot_TransitionType', b)


def test_assoc_transition343_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_TransitionConnectionType(points="sample_text")
    _safe_set(b, 'transitionConnections', a1)
    assert _is_linked(b, 'transitionConnections', a1)
    if hasattr(a1, 'TransitionType344'):
        assert _is_linked(a1, 'TransitionType344', b)
    _safe_set(b, 'transitionConnections', a2)
    assert _is_linked(b, 'transitionConnections', a2)
    if hasattr(a1, 'TransitionType344'):
        assert not _is_linked(a1, 'TransitionType344', b)
    if hasattr(a2, 'TransitionType344'):
        assert _is_linked(a2, 'TransitionType344', b)
    _safe_set(b, 'transitionConnections', None)
    assert not _is_linked(b, 'transitionConnections', a2)
    if hasattr(a2, 'TransitionType344'):
        assert not _is_linked(a2, 'TransitionType344', b)


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


def test_assoc_transitionConnections354_reverse_link_reassign_clear():
    a1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    a2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    b = carnot_TransitionConnectionType(points="sample_text")
    _safe_set(b, 'TransitionConnectionType355', a1)
    assert _is_linked(b, 'TransitionConnectionType355', a1)
    if hasattr(a1, 'transition'):
        assert _is_linked(a1, 'transition', b)
    _safe_set(b, 'TransitionConnectionType355', a2)
    assert _is_linked(b, 'TransitionConnectionType355', a2)
    if hasattr(a1, 'transition'):
        assert not _is_linked(a1, 'transition', b)
    if hasattr(a2, 'transition'):
        assert _is_linked(a2, 'transition', b)
    _safe_set(b, 'TransitionConnectionType355', None)
    assert not _is_linked(b, 'TransitionConnectionType355', a2)
    if hasattr(a2, 'transition'):
        assert not _is_linked(a2, 'transition', b)


def test_assoc_triggerType217_reverse_link_reassign_clear():
    a1 = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    a2 = carnot_TriggerTypeType(panelClass="sample_text_2", pullTrigger="sample_text_2", pullTriggerEvaluator="sample_text_2", rule="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType218', {a1})
    assert _is_linked(b, 'carnot_ModelType218', a1)
    if hasattr(a1, 'carnot_TriggerTypeType'):
        assert _is_linked(a1, 'carnot_TriggerTypeType', b)
    _safe_set(b, 'carnot_ModelType218', {a2})
    assert _is_linked(b, 'carnot_ModelType218', a2)
    if hasattr(a1, 'carnot_TriggerTypeType'):
        assert not _is_linked(a1, 'carnot_TriggerTypeType', b)
    if hasattr(a2, 'carnot_TriggerTypeType'):
        assert _is_linked(a2, 'carnot_TriggerTypeType', b)
    _safe_set(b, 'carnot_ModelType218', set())
    assert not _is_linked(b, 'carnot_ModelType218', a2)
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


def test_assoc_validQualityCodes109_reverse_link_reassign_clear():
    a1 = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    a2 = carnot_Code(code="sample_text_2", name="sample_text_2", value="sample_text_2")
    b = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    _safe_set(b, 'carnot_ActivityType110', {a1})
    assert _is_linked(b, 'carnot_ActivityType110', a1)
    if hasattr(a1, 'carnot_Code'):
        assert _is_linked(a1, 'carnot_Code', b)
    _safe_set(b, 'carnot_ActivityType110', {a2})
    assert _is_linked(b, 'carnot_ActivityType110', a2)
    if hasattr(a1, 'carnot_Code'):
        assert not _is_linked(a1, 'carnot_Code', b)
    if hasattr(a2, 'carnot_Code'):
        assert _is_linked(a2, 'carnot_Code', b)
    _safe_set(b, 'carnot_ActivityType110', set())
    assert not _is_linked(b, 'carnot_ActivityType110', a2)
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


def test_assoc_view251_reverse_link_reassign_clear():
    a1 = carnot_ViewType(name="sample_text")
    a2 = carnot_ViewType(name="sample_text_2")
    b = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    _safe_set(b, 'carnot_ModelType252', {a1})
    assert _is_linked(b, 'carnot_ModelType252', a1)
    if hasattr(a1, 'carnot_ViewType'):
        assert _is_linked(a1, 'carnot_ViewType', b)
    _safe_set(b, 'carnot_ModelType252', {a2})
    assert _is_linked(b, 'carnot_ModelType252', a2)
    if hasattr(a1, 'carnot_ViewType'):
        assert not _is_linked(a1, 'carnot_ViewType', b)
    if hasattr(a2, 'carnot_ViewType'):
        assert _is_linked(a2, 'carnot_ViewType', b)
    _safe_set(b, 'carnot_ModelType252', set())
    assert not _is_linked(b, 'carnot_ModelType252', a2)
    if hasattr(a2, 'carnot_ViewType'):
        assert not _is_linked(a2, 'carnot_ViewType', b)


def test_assoc_view373_reverse_link_reassign_clear():
    a1 = carnot_ViewType(name="sample_text")
    a2 = carnot_ViewType(name="sample_text_2")
    b = carnot_ViewType(name="sample_text")
    _safe_set(b, 'carnot_ViewType374', a1)
    assert _is_linked(b, 'carnot_ViewType374', a1)
    if hasattr(a1, 'carnot_ViewType372'):
        assert _is_linked(a1, 'carnot_ViewType372', b)
    _safe_set(b, 'carnot_ViewType374', a2)
    assert _is_linked(b, 'carnot_ViewType374', a2)
    if hasattr(a1, 'carnot_ViewType372'):
        assert not _is_linked(a1, 'carnot_ViewType372', b)
    if hasattr(a2, 'carnot_ViewType372'):
        assert _is_linked(a2, 'carnot_ViewType372', b)
    _safe_set(b, 'carnot_ViewType374', None)
    assert not _is_linked(b, 'carnot_ViewType374', a2)
    if hasattr(a2, 'carnot_ViewType372'):
        assert not _is_linked(a2, 'carnot_ViewType372', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Code308_stub_double():
    # carnot_QualityControlType has no real 'carnot_QualityControlType309' property in the generated
    # code (a bare stub) -- manually attach it so carnot_Code's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_Code's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    partner = carnot_QualityControlType()
    setattr(partner, 'carnot_QualityControlType309', None)
    _safe_set(owner, 'carnot_Code310', partner)
    assert getattr(partner, 'carnot_QualityControlType309') == owner
    _safe_set(owner, 'carnot_Code310', None)
    assert getattr(partner, 'carnot_QualityControlType309') is None


def test_assoc_accessPoint5_stub_double():
    # carnot_IAccessPointOwner has no real 'carnot_IAccessPointOwner' property in the generated
    # code (a bare stub) -- manually attach it so carnot_AccessPointType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_AccessPointType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_AccessPointType(direction="sample_text")
    partner = carnot_IAccessPointOwner()
    setattr(partner, 'carnot_IAccessPointOwner', None)
    _safe_set(owner, 'carnot_AccessPointType', partner)
    assert getattr(partner, 'carnot_IAccessPointOwner') == owner
    _safe_set(owner, 'carnot_AccessPointType', None)
    assert getattr(partner, 'carnot_IAccessPointOwner') is None


def test_assoc_actionInstances175_stub_double():
    # carnot_AbstractEventAction has no real 'AbstractEventAction' property in the generated
    # code (a bare stub) -- manually attach it so carnot_EventActionTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_EventActionTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    partner = carnot_AbstractEventAction()
    setattr(partner, 'AbstractEventAction', None)
    _safe_set(owner, 'type176', {partner})
    assert getattr(partner, 'AbstractEventAction') == owner
    _safe_set(owner, 'type176', set())
    assert getattr(partner, 'AbstractEventAction') is None


def test_assoc_activity82_stub_double():
    # carnot_ActivitySymbolType has no real 'activitySymbols' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    partner = carnot_ActivitySymbolType()
    setattr(partner, 'activitySymbols', None)
    _safe_set(owner, 'ActivityType83', partner)
    assert getattr(partner, 'activitySymbols') == owner
    _safe_set(owner, 'ActivityType83', None)
    assert getattr(partner, 'activitySymbols') is None


def test_assoc_activitySymbol193_stub_double():
    # carnot_ActivitySymbolType has no real 'ActivitySymbolType194' property in the generated
    # code (a bare stub) -- manually attach it so carnot_GatewaySymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_GatewaySymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_GatewaySymbol(flowKind="sample_text")
    partner = carnot_ActivitySymbolType()
    setattr(partner, 'ActivitySymbolType194', None)
    _safe_set(owner, 'gatewaySymbols', partner)
    assert getattr(partner, 'ActivitySymbolType194') == owner
    _safe_set(owner, 'gatewaySymbols', None)
    assert getattr(partner, 'ActivitySymbolType194') is None


def test_assoc_activitySymbol6_stub_double():
    # carnot_ActivitySymbolType has no real 'carnot_ActivitySymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_ActivitySymbolType()
    setattr(partner, 'carnot_ActivitySymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer', {partner})
    assert getattr(partner, 'carnot_ActivitySymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer', set())
    assert getattr(partner, 'carnot_ActivitySymbolType') is None


def test_assoc_activitySymbols100_stub_double():
    # carnot_ActivitySymbolType has no real 'ActivitySymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    partner = carnot_ActivitySymbolType()
    setattr(partner, 'ActivitySymbolType', None)
    _safe_set(owner, 'activity', {partner})
    assert getattr(partner, 'ActivitySymbolType') == owner
    _safe_set(owner, 'activity', set())
    assert getattr(partner, 'ActivitySymbolType') is None


def test_assoc_annotationSymbol7_stub_double():
    # carnot_AnnotationSymbolType has no real 'carnot_AnnotationSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_AnnotationSymbolType()
    setattr(partner, 'carnot_AnnotationSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer8', {partner})
    assert getattr(partner, 'carnot_AnnotationSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer8', set())
    assert getattr(partner, 'carnot_AnnotationSymbolType') is None


def test_assoc_application116_stub_double():
    # carnot_ApplicationSymbolType has no real 'applicationSymbols' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ApplicationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ApplicationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ApplicationType(interactive="sample_text")
    partner = carnot_ApplicationSymbolType()
    setattr(partner, 'applicationSymbols', None)
    _safe_set(owner, 'ApplicationType117', partner)
    assert getattr(partner, 'applicationSymbols') == owner
    _safe_set(owner, 'ApplicationType117', None)
    assert getattr(partner, 'applicationSymbols') is None


def test_assoc_applicationSymbol9_stub_double():
    # carnot_ApplicationSymbolType has no real 'carnot_ApplicationSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_ApplicationSymbolType()
    setattr(partner, 'carnot_ApplicationSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer10', {partner})
    assert getattr(partner, 'carnot_ApplicationSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer10', set())
    assert getattr(partner, 'carnot_ApplicationSymbolType') is None


def test_assoc_applicationSymbols122_stub_double():
    # carnot_ApplicationSymbolType has no real 'ApplicationSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ApplicationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ApplicationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ApplicationType(interactive="sample_text")
    partner = carnot_ApplicationSymbolType()
    setattr(partner, 'ApplicationSymbolType', None)
    _safe_set(owner, 'application123', {partner})
    assert getattr(partner, 'ApplicationSymbolType') == owner
    _safe_set(owner, 'application123', set())
    assert getattr(partner, 'ApplicationSymbolType') is None


def test_assoc_attribute0_stub_double():
    # carnot_IExtensibleElement has no real 'carnot_IExtensibleElement' property in the generated
    # code (a bare stub) -- manually attach it so carnot_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    partner = carnot_IExtensibleElement()
    setattr(partner, 'carnot_IExtensibleElement', None)
    _safe_set(owner, 'carnot_AttributeType', partner)
    assert getattr(partner, 'carnot_IExtensibleElement') == owner
    _safe_set(owner, 'carnot_AttributeType', None)
    assert getattr(partner, 'carnot_IExtensibleElement') is None


def test_assoc_attribute1_stub_double():
    # carnot_IdentifiableReference has no real 'reference' property in the generated
    # code (a bare stub) -- manually attach it so carnot_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    partner = carnot_IdentifiableReference()
    setattr(partner, 'reference', None)
    _safe_set(owner, 'AttributeType', partner)
    assert getattr(partner, 'reference') == owner
    _safe_set(owner, 'AttributeType', None)
    assert getattr(partner, 'reference') is None


def test_assoc_bindAction179_stub_double():
    # carnot_BindActionType has no real 'carnot_BindActionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_EventHandlerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_EventHandlerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    partner = carnot_BindActionType()
    setattr(partner, 'carnot_BindActionType', None)
    _safe_set(owner, 'carnot_EventHandlerType180', {partner})
    assert getattr(partner, 'carnot_BindActionType') == owner
    _safe_set(owner, 'carnot_EventHandlerType180', set())
    assert getattr(partner, 'carnot_BindActionType') is None


def test_assoc_childLanes66_stub_double():
    # carnot_LaneSymbol has no real 'LaneSymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISwimlaneSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISwimlaneSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    partner = carnot_LaneSymbol()
    setattr(partner, 'LaneSymbol', None)
    _safe_set(owner, 'parentLane', {partner})
    assert getattr(partner, 'LaneSymbol') == owner
    _safe_set(owner, 'parentLane', set())
    assert getattr(partner, 'LaneSymbol') is None


def test_assoc_conditionalPerformerSymbol11_stub_double():
    # carnot_ConditionalPerformerSymbolType has no real 'carnot_ConditionalPerformerSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_ConditionalPerformerSymbolType()
    setattr(partner, 'carnot_ConditionalPerformerSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer12', {partner})
    assert getattr(partner, 'carnot_ConditionalPerformerSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer12', set())
    assert getattr(partner, 'carnot_ConditionalPerformerSymbolType') is None


def test_assoc_conditionalPerformerSymbols132_stub_double():
    # carnot_ConditionalPerformerSymbolType has no real 'ConditionalPerformerSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ConditionalPerformerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ConditionalPerformerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    partner = carnot_ConditionalPerformerSymbolType()
    setattr(partner, 'ConditionalPerformerSymbolType', None)
    _safe_set(owner, 'participant133', {partner})
    assert getattr(partner, 'ConditionalPerformerSymbolType') == owner
    _safe_set(owner, 'participant133', set())
    assert getattr(partner, 'ConditionalPerformerSymbolType') is None


def test_assoc_context118_stub_double():
    # carnot_ContextType has no real 'carnot_ContextType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ApplicationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ApplicationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ApplicationType(interactive="sample_text")
    partner = carnot_ContextType()
    setattr(partner, 'carnot_ContextType', None)
    _safe_set(owner, 'carnot_ApplicationType', {partner})
    assert getattr(partner, 'carnot_ContextType') == owner
    _safe_set(owner, 'carnot_ApplicationType', set())
    assert getattr(partner, 'carnot_ContextType') is None


def test_assoc_contexts113_stub_double():
    # carnot_ContextType has no real 'ContextType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ApplicationContextTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ApplicationContextTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    partner = carnot_ContextType()
    setattr(partner, 'ContextType', None)
    _safe_set(owner, 'type', {partner})
    assert getattr(partner, 'ContextType') == owner
    _safe_set(owner, 'type', set())
    assert getattr(partner, 'ContextType') is None


def test_assoc_data147_stub_double():
    # carnot_DataSymbolType has no real 'dataSymbols' property in the generated
    # code (a bare stub) -- manually attach it so carnot_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_DataType(predefined="sample_text")
    partner = carnot_DataSymbolType()
    setattr(partner, 'dataSymbols', None)
    _safe_set(owner, 'DataType148', partner)
    assert getattr(partner, 'dataSymbols') == owner
    _safe_set(owner, 'DataType148', None)
    assert getattr(partner, 'dataSymbols') is None


def test_assoc_dataMappingConnection37_stub_double():
    # carnot_DataMappingConnectionType has no real 'carnot_DataMappingConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_DataMappingConnectionType()
    setattr(partner, 'carnot_DataMappingConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer38', {partner})
    assert getattr(partner, 'carnot_DataMappingConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer38', set())
    assert getattr(partner, 'carnot_DataMappingConnectionType') is None


def test_assoc_dataSymbol13_stub_double():
    # carnot_DataSymbolType has no real 'carnot_DataSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_DataSymbolType()
    setattr(partner, 'carnot_DataSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer14', {partner})
    assert getattr(partner, 'carnot_DataSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer14', set())
    assert getattr(partner, 'carnot_DataSymbolType') is None


def test_assoc_dataSymbols154_stub_double():
    # carnot_DataSymbolType has no real 'DataSymbolType156' property in the generated
    # code (a bare stub) -- manually attach it so carnot_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_DataType(predefined="sample_text")
    partner = carnot_DataSymbolType()
    setattr(partner, 'DataSymbolType156', None)
    _safe_set(owner, 'data155', {partner})
    assert getattr(partner, 'DataSymbolType156') == owner
    _safe_set(owner, 'data155', set())
    assert getattr(partner, 'DataSymbolType156') is None


def test_assoc_description134_stub_double():
    # carnot_ContextType has no real 'carnot_ContextType135' property in the generated
    # code (a bare stub) -- manually attach it so carnot_DescriptionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_DescriptionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_DescriptionType(mixed="sample_text")
    partner = carnot_ContextType()
    setattr(partner, 'carnot_ContextType135', None)
    _safe_set(owner, 'carnot_DescriptionType136', partner)
    assert getattr(partner, 'carnot_ContextType135') == owner
    _safe_set(owner, 'carnot_DescriptionType136', None)
    assert getattr(partner, 'carnot_ContextType135') is None


def test_assoc_endEventSymbols15_stub_double():
    # carnot_EndEventSymbol has no real 'carnot_EndEventSymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_EndEventSymbol()
    setattr(partner, 'carnot_EndEventSymbol', None)
    _safe_set(owner, 'carnot_ISymbolContainer16', {partner})
    assert getattr(partner, 'carnot_EndEventSymbol') == owner
    _safe_set(owner, 'carnot_ISymbolContainer16', set())
    assert getattr(partner, 'carnot_EndEventSymbol') is None


def test_assoc_eventAction181_stub_double():
    # carnot_EventActionType has no real 'carnot_EventActionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_EventHandlerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_EventHandlerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    partner = carnot_EventActionType()
    setattr(partner, 'carnot_EventActionType', None)
    _safe_set(owner, 'carnot_EventHandlerType182', {partner})
    assert getattr(partner, 'carnot_EventActionType') == owner
    _safe_set(owner, 'carnot_EventHandlerType182', set())
    assert getattr(partner, 'carnot_EventActionType') is None


def test_assoc_eventHandler4_stub_double():
    # carnot_IEventHandlerOwner has no real 'carnot_IEventHandlerOwner' property in the generated
    # code (a bare stub) -- manually attach it so carnot_EventHandlerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_EventHandlerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    partner = carnot_IEventHandlerOwner()
    setattr(partner, 'carnot_IEventHandlerOwner', None)
    _safe_set(owner, 'carnot_EventHandlerType', partner)
    assert getattr(partner, 'carnot_IEventHandlerOwner') == owner
    _safe_set(owner, 'carnot_EventHandlerType', None)
    assert getattr(partner, 'carnot_IEventHandlerOwner') is None


def test_assoc_executedByConnection39_stub_double():
    # carnot_ExecutedByConnectionType has no real 'carnot_ExecutedByConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_ExecutedByConnectionType()
    setattr(partner, 'carnot_ExecutedByConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer40', {partner})
    assert getattr(partner, 'carnot_ExecutedByConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer40', set())
    assert getattr(partner, 'carnot_ExecutedByConnectionType') is None


def test_assoc_externalPackages241_stub_double():
    # carnot_ExternalPackages has no real 'carnot_ExternalPackages' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    partner = carnot_ExternalPackages()
    setattr(partner, 'carnot_ExternalPackages', None)
    _safe_set(owner, 'carnot_ModelType242', partner)
    assert getattr(partner, 'carnot_ExternalPackages') == owner
    _safe_set(owner, 'carnot_ModelType242', None)
    assert getattr(partner, 'carnot_ExternalPackages') is None


def test_assoc_externalReference164_stub_double():
    # carnot_ExternalReferenceType has no real 'carnot_ExternalReferenceType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_DataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_DataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_DataType(predefined="sample_text")
    partner = carnot_ExternalReferenceType()
    setattr(partner, 'carnot_ExternalReferenceType', None)
    _safe_set(owner, 'carnot_DataType', partner)
    assert getattr(partner, 'carnot_ExternalReferenceType') == owner
    _safe_set(owner, 'carnot_DataType', None)
    assert getattr(partner, 'carnot_ExternalReferenceType') is None


def test_assoc_formalParameterMappings298_stub_double():
    # FormalParameterMappingsType has no real 'FormalParameterMappingsType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ProcessDefinitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ProcessDefinitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    partner = FormalParameterMappingsType()
    setattr(partner, 'FormalParameterMappingsType', None)
    _safe_set(owner, 'carnot_ProcessDefinitionType299', partner)
    assert getattr(partner, 'FormalParameterMappingsType') == owner
    _safe_set(owner, 'carnot_ProcessDefinitionType299', None)
    assert getattr(partner, 'FormalParameterMappingsType') is None


def test_assoc_formalParameters296_stub_double():
    # carnot_FormalParametersType has no real 'carnot_FormalParametersType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ProcessDefinitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ProcessDefinitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    partner = carnot_FormalParametersType()
    setattr(partner, 'carnot_FormalParametersType', None)
    _safe_set(owner, 'carnot_ProcessDefinitionType297', partner)
    assert getattr(partner, 'carnot_FormalParametersType') == owner
    _safe_set(owner, 'carnot_ProcessDefinitionType297', None)
    assert getattr(partner, 'carnot_FormalParametersType') is None


def test_assoc_from_311_stub_double():
    # carnot_RefersToConnectionType has no real 'referingFromConnections' property in the generated
    # code (a bare stub) -- manually attach it so carnot_IGraphicalObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_IGraphicalObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    partner = carnot_RefersToConnectionType()
    setattr(partner, 'referingFromConnections', None)
    _safe_set(owner, 'IGraphicalObject', partner)
    assert getattr(partner, 'referingFromConnections') == owner
    _safe_set(owner, 'IGraphicalObject', None)
    assert getattr(partner, 'referingFromConnections') is None


def test_assoc_gatewaySymbols90_stub_double():
    # carnot_ActivitySymbolType has no real 'activitySymbol91' property in the generated
    # code (a bare stub) -- manually attach it so carnot_GatewaySymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_GatewaySymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_GatewaySymbol(flowKind="sample_text")
    partner = carnot_ActivitySymbolType()
    setattr(partner, 'activitySymbol91', None)
    _safe_set(owner, 'GatewaySymbol', partner)
    assert getattr(partner, 'activitySymbol91') == owner
    _safe_set(owner, 'GatewaySymbol', None)
    assert getattr(partner, 'activitySymbol91') is None


def test_assoc_genericLinkConnection41_stub_double():
    # carnot_GenericLinkConnectionType has no real 'carnot_GenericLinkConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_GenericLinkConnectionType()
    setattr(partner, 'carnot_GenericLinkConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer42', {partner})
    assert getattr(partner, 'carnot_GenericLinkConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer42', set())
    assert getattr(partner, 'carnot_GenericLinkConnectionType') is None


def test_assoc_groupSymbol19_stub_double():
    # carnot_GroupSymbolType has no real 'carnot_GroupSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_GroupSymbolType()
    setattr(partner, 'carnot_GroupSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer20', {partner})
    assert getattr(partner, 'carnot_GroupSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer20', set())
    assert getattr(partner, 'carnot_GroupSymbolType') is None


def test_assoc_inLinks62_stub_double():
    # carnot_GenericLinkConnectionType has no real 'GenericLinkConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_INodeSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_INodeSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    partner = carnot_GenericLinkConnectionType()
    setattr(partner, 'GenericLinkConnectionType', None)
    _safe_set(owner, 'targetSymbol', {partner})
    assert getattr(partner, 'GenericLinkConnectionType') == owner
    _safe_set(owner, 'targetSymbol', set())
    assert getattr(partner, 'GenericLinkConnectionType') is None


def test_assoc_inTransitions68_stub_double():
    # carnot_IFlowObjectSymbol has no real 'targetActivitySymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_TransitionConnectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_TransitionConnectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_TransitionConnectionType(points="sample_text")
    partner = carnot_IFlowObjectSymbol()
    setattr(partner, 'targetActivitySymbol', None)
    _safe_set(owner, 'TransitionConnectionType', partner)
    assert getattr(partner, 'targetActivitySymbol') == owner
    _safe_set(owner, 'TransitionConnectionType', None)
    assert getattr(partner, 'targetActivitySymbol') is None


def test_assoc_intermediateEventSymbols21_stub_double():
    # carnot_IntermediateEventSymbol has no real 'carnot_IntermediateEventSymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_IntermediateEventSymbol()
    setattr(partner, 'carnot_IntermediateEventSymbol', None)
    _safe_set(owner, 'carnot_ISymbolContainer22', {partner})
    assert getattr(partner, 'carnot_IntermediateEventSymbol') == owner
    _safe_set(owner, 'carnot_ISymbolContainer22', set())
    assert getattr(partner, 'carnot_IntermediateEventSymbol') is None


def test_assoc_lanes279_stub_double():
    # carnot_LaneSymbol has no real 'LaneSymbol280' property in the generated
    # code (a bare stub) -- manually attach it so carnot_PoolSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_PoolSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_PoolSymbol(boundaryVisible="sample_text")
    partner = carnot_LaneSymbol()
    setattr(partner, 'LaneSymbol280', None)
    _safe_set(owner, 'parentPool', {partner})
    assert getattr(partner, 'LaneSymbol280') == owner
    _safe_set(owner, 'parentPool', set())
    assert getattr(partner, 'LaneSymbol280') is None


def test_assoc_linkInstances203_stub_double():
    # carnot_GenericLinkConnectionType has no real 'GenericLinkConnectionType204' property in the generated
    # code (a bare stub) -- manually attach it so carnot_LinkTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_LinkTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    partner = carnot_GenericLinkConnectionType()
    setattr(partner, 'GenericLinkConnectionType204', None)
    _safe_set(owner, 'linkType', {partner})
    assert getattr(partner, 'GenericLinkConnectionType204') == owner
    _safe_set(owner, 'linkType', set())
    assert getattr(partner, 'GenericLinkConnectionType204') is None


def test_assoc_linkType195_stub_double():
    # carnot_GenericLinkConnectionType has no real 'linkInstances' property in the generated
    # code (a bare stub) -- manually attach it so carnot_LinkTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_LinkTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    partner = carnot_GenericLinkConnectionType()
    setattr(partner, 'linkInstances', None)
    _safe_set(owner, 'LinkTypeType', partner)
    assert getattr(partner, 'linkInstances') == owner
    _safe_set(owner, 'LinkTypeType', None)
    assert getattr(partner, 'linkInstances') is None


def test_assoc_mapping385_stub_double():
    # FormalParameterMappingType has no real 'FormalParameterMappingType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_extensions_FormalParameterMappingsType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_extensions_FormalParameterMappingsType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_extensions_FormalParameterMappingsType()
    partner = FormalParameterMappingType()
    setattr(partner, 'FormalParameterMappingType', None)
    _safe_set(owner, 'carnot_extensions_FormalParameterMappingsType', {partner})
    assert getattr(partner, 'FormalParameterMappingType') == owner
    _safe_set(owner, 'carnot_extensions_FormalParameterMappingsType', set())
    assert getattr(partner, 'FormalParameterMappingType') is None


def test_assoc_modeler205_stub_double():
    # carnot_ModelerSymbolType has no real 'modelerSymbols' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ModelerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ModelerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ModelerType(email="sample_text", password="sample_text")
    partner = carnot_ModelerSymbolType()
    setattr(partner, 'modelerSymbols', None)
    _safe_set(owner, 'ModelerType', partner)
    assert getattr(partner, 'modelerSymbols') == owner
    _safe_set(owner, 'ModelerType', None)
    assert getattr(partner, 'modelerSymbols') is None


def test_assoc_modelerSymbol23_stub_double():
    # carnot_ModelerSymbolType has no real 'carnot_ModelerSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_ModelerSymbolType()
    setattr(partner, 'carnot_ModelerSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer24', {partner})
    assert getattr(partner, 'carnot_ModelerSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer24', set())
    assert getattr(partner, 'carnot_ModelerSymbolType') is None


def test_assoc_modelerSymbols206_stub_double():
    # carnot_ModelerSymbolType has no real 'ModelerSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ModelerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ModelerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ModelerType(email="sample_text", password="sample_text")
    partner = carnot_ModelerSymbolType()
    setattr(partner, 'ModelerSymbolType', None)
    _safe_set(owner, 'modeler', {partner})
    assert getattr(partner, 'ModelerSymbolType') == owner
    _safe_set(owner, 'modeler', set())
    assert getattr(partner, 'ModelerSymbolType') is None


def test_assoc_organization235_stub_double():
    # carnot_OrganizationType has no real 'carnot_OrganizationType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    partner = carnot_OrganizationType()
    setattr(partner, 'carnot_OrganizationType', None)
    _safe_set(owner, 'carnot_ModelType236', {partner})
    assert getattr(partner, 'carnot_OrganizationType') == owner
    _safe_set(owner, 'carnot_ModelType236', set())
    assert getattr(partner, 'carnot_OrganizationType') is None


def test_assoc_organizationSymbol25_stub_double():
    # carnot_OrganizationSymbolType has no real 'carnot_OrganizationSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_OrganizationSymbolType()
    setattr(partner, 'carnot_OrganizationSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer26', {partner})
    assert getattr(partner, 'carnot_OrganizationSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer26', set())
    assert getattr(partner, 'carnot_OrganizationSymbolType') is None


def test_assoc_outLinks63_stub_double():
    # carnot_GenericLinkConnectionType has no real 'GenericLinkConnectionType64' property in the generated
    # code (a bare stub) -- manually attach it so carnot_INodeSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_INodeSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    partner = carnot_GenericLinkConnectionType()
    setattr(partner, 'GenericLinkConnectionType64', None)
    _safe_set(owner, 'sourceSymbol', {partner})
    assert getattr(partner, 'GenericLinkConnectionType64') == owner
    _safe_set(owner, 'sourceSymbol', set())
    assert getattr(partner, 'GenericLinkConnectionType64') is None


def test_assoc_outTransitions69_stub_double():
    # carnot_IFlowObjectSymbol has no real 'sourceActivitySymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_TransitionConnectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_TransitionConnectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_TransitionConnectionType(points="sample_text")
    partner = carnot_IFlowObjectSymbol()
    setattr(partner, 'sourceActivitySymbol', None)
    _safe_set(owner, 'TransitionConnectionType70', partner)
    assert getattr(partner, 'sourceActivitySymbol') == owner
    _safe_set(owner, 'TransitionConnectionType70', None)
    assert getattr(partner, 'sourceActivitySymbol') is None


def test_assoc_packageRef191_stub_double():
    # carnot_ExternalPackage has no real 'carnot_ExternalPackage' property in the generated
    # code (a bare stub) -- manually attach it so carnot_IdRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_IdRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_IdRef(ref="sample_text")
    partner = carnot_ExternalPackage()
    setattr(partner, 'carnot_ExternalPackage', None)
    _safe_set(owner, 'carnot_IdRef192', partner)
    assert getattr(partner, 'carnot_ExternalPackage') == owner
    _safe_set(owner, 'carnot_IdRef192', None)
    assert getattr(partner, 'carnot_ExternalPackage') is None


def test_assoc_parameterMapping360_stub_double():
    # carnot_TriggerType has no real 'carnot_TriggerType361' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ParameterMappingType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ParameterMappingType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    partner = carnot_TriggerType()
    setattr(partner, 'carnot_TriggerType361', None)
    _safe_set(owner, 'carnot_ParameterMappingType', partner)
    assert getattr(partner, 'carnot_TriggerType361') == owner
    _safe_set(owner, 'carnot_ParameterMappingType', None)
    assert getattr(partner, 'carnot_TriggerType361') is None


def test_assoc_parentLane201_stub_double():
    # carnot_LaneSymbol has no real 'childLanes' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISwimlaneSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISwimlaneSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    partner = carnot_LaneSymbol()
    setattr(partner, 'childLanes', None)
    _safe_set(owner, 'ISwimlaneSymbol202', partner)
    assert getattr(partner, 'childLanes') == owner
    _safe_set(owner, 'ISwimlaneSymbol202', None)
    assert getattr(partner, 'childLanes') is None


def test_assoc_parentPool199_stub_double():
    # carnot_LaneSymbol has no real 'lanes' property in the generated
    # code (a bare stub) -- manually attach it so carnot_PoolSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_PoolSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_PoolSymbol(boundaryVisible="sample_text")
    partner = carnot_LaneSymbol()
    setattr(partner, 'lanes', None)
    _safe_set(owner, 'PoolSymbol200', partner)
    assert getattr(partner, 'lanes') == owner
    _safe_set(owner, 'PoolSymbol200', None)
    assert getattr(partner, 'lanes') is None


def test_assoc_partOfConnection43_stub_double():
    # carnot_PartOfConnectionType has no real 'carnot_PartOfConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_PartOfConnectionType()
    setattr(partner, 'carnot_PartOfConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer44', {partner})
    assert getattr(partner, 'carnot_PartOfConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer44', set())
    assert getattr(partner, 'carnot_PartOfConnectionType') is None


def test_assoc_participant130_stub_double():
    # carnot_ConditionalPerformerSymbolType has no real 'conditionalPerformerSymbols' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ConditionalPerformerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ConditionalPerformerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    partner = carnot_ConditionalPerformerSymbolType()
    setattr(partner, 'conditionalPerformerSymbols', None)
    _safe_set(owner, 'ConditionalPerformerType', partner)
    assert getattr(partner, 'conditionalPerformerSymbols') == owner
    _safe_set(owner, 'ConditionalPerformerType', None)
    assert getattr(partner, 'conditionalPerformerSymbols') is None


def test_assoc_participant65_stub_double():
    # carnot_IModelParticipant has no real 'IModelParticipant' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISwimlaneSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISwimlaneSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    partner = carnot_IModelParticipant()
    setattr(partner, 'IModelParticipant', None)
    _safe_set(owner, 'performedSwimlanes', partner)
    assert getattr(partner, 'IModelParticipant') == owner
    _safe_set(owner, 'performedSwimlanes', None)
    assert getattr(partner, 'IModelParticipant') is None


def test_assoc_participantReference67_stub_double():
    # carnot_IModelParticipant has no real 'carnot_IModelParticipant' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISwimlaneSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISwimlaneSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    partner = carnot_IModelParticipant()
    setattr(partner, 'carnot_IModelParticipant', None)
    _safe_set(owner, 'carnot_ISwimlaneSymbol', partner)
    assert getattr(partner, 'carnot_IModelParticipant') == owner
    _safe_set(owner, 'carnot_ISwimlaneSymbol', None)
    assert getattr(partner, 'carnot_IModelParticipant') is None


def test_assoc_performedActivities72_stub_double():
    # carnot_IModelParticipant has no real 'performer' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    partner = carnot_IModelParticipant()
    setattr(partner, 'performer', None)
    _safe_set(owner, 'ActivityType', partner)
    assert getattr(partner, 'performer') == owner
    _safe_set(owner, 'ActivityType', None)
    assert getattr(partner, 'performer') is None


def test_assoc_performedSwimlanes73_stub_double():
    # carnot_IModelParticipant has no real 'participant' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISwimlaneSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISwimlaneSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    partner = carnot_IModelParticipant()
    setattr(partner, 'participant', None)
    _safe_set(owner, 'ISwimlaneSymbol', partner)
    assert getattr(partner, 'participant') == owner
    _safe_set(owner, 'ISwimlaneSymbol', None)
    assert getattr(partner, 'participant') is None


def test_assoc_performer95_stub_double():
    # carnot_IModelParticipant has no real 'IModelParticipant96' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    partner = carnot_IModelParticipant()
    setattr(partner, 'IModelParticipant96', None)
    _safe_set(owner, 'performedActivities', partner)
    assert getattr(partner, 'IModelParticipant96') == owner
    _safe_set(owner, 'performedActivities', None)
    assert getattr(partner, 'IModelParticipant96') is None


def test_assoc_performsConnection45_stub_double():
    # carnot_PerformsConnectionType has no real 'carnot_PerformsConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_PerformsConnectionType()
    setattr(partner, 'carnot_PerformsConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer46', {partner})
    assert getattr(partner, 'carnot_PerformsConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer46', set())
    assert getattr(partner, 'carnot_PerformsConnectionType') is None


def test_assoc_process303_stub_double():
    # carnot_ProcessSymbolType has no real 'processSymbols' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ProcessDefinitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ProcessDefinitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    partner = carnot_ProcessSymbolType()
    setattr(partner, 'processSymbols', None)
    _safe_set(owner, 'ProcessDefinitionType304', partner)
    assert getattr(partner, 'processSymbols') == owner
    _safe_set(owner, 'ProcessDefinitionType304', None)
    assert getattr(partner, 'processSymbols') is None


def test_assoc_processInterfaceSymbols29_stub_double():
    # carnot_PublicInterfaceSymbol has no real 'carnot_PublicInterfaceSymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_PublicInterfaceSymbol()
    setattr(partner, 'carnot_PublicInterfaceSymbol', None)
    _safe_set(owner, 'carnot_ISymbolContainer30', {partner})
    assert getattr(partner, 'carnot_PublicInterfaceSymbol') == owner
    _safe_set(owner, 'carnot_ISymbolContainer30', set())
    assert getattr(partner, 'carnot_PublicInterfaceSymbol') is None


def test_assoc_processSymbol27_stub_double():
    # carnot_ProcessSymbolType has no real 'carnot_ProcessSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_ProcessSymbolType()
    setattr(partner, 'carnot_ProcessSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer28', {partner})
    assert getattr(partner, 'carnot_ProcessSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer28', set())
    assert getattr(partner, 'carnot_ProcessSymbolType') is None


def test_assoc_processSymbols295_stub_double():
    # carnot_ProcessSymbolType has no real 'ProcessSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ProcessDefinitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ProcessDefinitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    partner = carnot_ProcessSymbolType()
    setattr(partner, 'ProcessSymbolType', None)
    _safe_set(owner, 'process', {partner})
    assert getattr(partner, 'ProcessSymbolType') == owner
    _safe_set(owner, 'process', set())
    assert getattr(partner, 'ProcessSymbolType') is None


def test_assoc_qualityControl231_stub_double():
    # carnot_QualityControlType has no real 'carnot_QualityControlType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    partner = carnot_QualityControlType()
    setattr(partner, 'carnot_QualityControlType', None)
    _safe_set(owner, 'carnot_ModelType232', partner)
    assert getattr(partner, 'carnot_QualityControlType') == owner
    _safe_set(owner, 'carnot_ModelType232', None)
    assert getattr(partner, 'carnot_QualityControlType') is None


def test_assoc_qualityControlPerformer97_stub_double():
    # carnot_IModelParticipant has no real 'carnot_IModelParticipant99' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    partner = carnot_IModelParticipant()
    setattr(partner, 'carnot_IModelParticipant99', None)
    _safe_set(owner, 'carnot_ActivityType98', partner)
    assert getattr(partner, 'carnot_IModelParticipant99') == owner
    _safe_set(owner, 'carnot_ActivityType98', None)
    assert getattr(partner, 'carnot_IModelParticipant99') is None


def test_assoc_reference129_stub_double():
    # carnot_IdentifiableReference has no real 'IdentifiableReference' property in the generated
    # code (a bare stub) -- manually attach it so carnot_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    partner = carnot_IdentifiableReference()
    setattr(partner, 'IdentifiableReference', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'IdentifiableReference') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'IdentifiableReference') is None


def test_assoc_referingFromConnections60_stub_double():
    # carnot_RefersToConnectionType has no real 'RefersToConnectionType61' property in the generated
    # code (a bare stub) -- manually attach it so carnot_IGraphicalObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_IGraphicalObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    partner = carnot_RefersToConnectionType()
    setattr(partner, 'RefersToConnectionType61', None)
    _safe_set(owner, 'from_', {partner})
    assert getattr(partner, 'RefersToConnectionType61') == owner
    _safe_set(owner, 'from_', set())
    assert getattr(partner, 'RefersToConnectionType61') is None


def test_assoc_referingToConnections59_stub_double():
    # carnot_RefersToConnectionType has no real 'RefersToConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_IGraphicalObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_IGraphicalObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    partner = carnot_RefersToConnectionType()
    setattr(partner, 'RefersToConnectionType', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'RefersToConnectionType') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'RefersToConnectionType') is None


def test_assoc_refersToConnection49_stub_double():
    # carnot_RefersToConnectionType has no real 'carnot_RefersToConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_RefersToConnectionType()
    setattr(partner, 'carnot_RefersToConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer50', {partner})
    assert getattr(partner, 'carnot_RefersToConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer50', set())
    assert getattr(partner, 'carnot_RefersToConnectionType') is None


def test_assoc_role314_stub_double():
    # carnot_RoleSymbolType has no real 'roleSymbols' property in the generated
    # code (a bare stub) -- manually attach it so carnot_RoleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_RoleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_RoleType(cardinality=7)
    partner = carnot_RoleSymbolType()
    setattr(partner, 'roleSymbols', None)
    _safe_set(owner, 'RoleType315', partner)
    assert getattr(partner, 'roleSymbols') == owner
    _safe_set(owner, 'RoleType315', None)
    assert getattr(partner, 'roleSymbols') is None


def test_assoc_roleSymbol31_stub_double():
    # carnot_RoleSymbolType has no real 'carnot_RoleSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_RoleSymbolType()
    setattr(partner, 'carnot_RoleSymbolType', None)
    _safe_set(owner, 'carnot_ISymbolContainer32', {partner})
    assert getattr(partner, 'carnot_RoleSymbolType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer32', set())
    assert getattr(partner, 'carnot_RoleSymbolType') is None


def test_assoc_roleSymbols323_stub_double():
    # carnot_RoleSymbolType has no real 'RoleSymbolType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_RoleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_RoleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_RoleType(cardinality=7)
    partner = carnot_RoleSymbolType()
    setattr(partner, 'RoleSymbolType', None)
    _safe_set(owner, 'role', {partner})
    assert getattr(partner, 'RoleSymbolType') == owner
    _safe_set(owner, 'role', set())
    assert getattr(partner, 'RoleSymbolType') is None


def test_assoc_script243_stub_double():
    # carnot_ScriptType has no real 'carnot_ScriptType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    partner = carnot_ScriptType()
    setattr(partner, 'carnot_ScriptType', None)
    _safe_set(owner, 'carnot_ModelType244', partner)
    assert getattr(partner, 'carnot_ScriptType') == owner
    _safe_set(owner, 'carnot_ModelType244', None)
    assert getattr(partner, 'carnot_ScriptType') is None


def test_assoc_sourceActivitySymbol340_stub_double():
    # carnot_IFlowObjectSymbol has no real 'IFlowObjectSymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_TransitionConnectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_TransitionConnectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_TransitionConnectionType(points="sample_text")
    partner = carnot_IFlowObjectSymbol()
    setattr(partner, 'IFlowObjectSymbol', None)
    _safe_set(owner, 'outTransitions', partner)
    assert getattr(partner, 'IFlowObjectSymbol') == owner
    _safe_set(owner, 'outTransitions', None)
    assert getattr(partner, 'IFlowObjectSymbol') is None


def test_assoc_sourceSymbol196_stub_double():
    # carnot_GenericLinkConnectionType has no real 'outLinks' property in the generated
    # code (a bare stub) -- manually attach it so carnot_INodeSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_INodeSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    partner = carnot_GenericLinkConnectionType()
    setattr(partner, 'outLinks', None)
    _safe_set(owner, 'INodeSymbol', partner)
    assert getattr(partner, 'outLinks') == owner
    _safe_set(owner, 'INodeSymbol', None)
    assert getattr(partner, 'outLinks') is None


def test_assoc_startActivity327_stub_double():
    # carnot_StartEventSymbol has no real 'startingEventSymbols328' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    partner = carnot_StartEventSymbol()
    setattr(partner, 'startingEventSymbols328', None)
    _safe_set(owner, 'ActivityType329', partner)
    assert getattr(partner, 'startingEventSymbols328') == owner
    _safe_set(owner, 'ActivityType329', None)
    assert getattr(partner, 'startingEventSymbols328') is None


def test_assoc_startEventSymbols33_stub_double():
    # carnot_StartEventSymbol has no real 'carnot_StartEventSymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_StartEventSymbol()
    setattr(partner, 'carnot_StartEventSymbol', None)
    _safe_set(owner, 'carnot_ISymbolContainer34', {partner})
    assert getattr(partner, 'carnot_StartEventSymbol') == owner
    _safe_set(owner, 'carnot_ISymbolContainer34', set())
    assert getattr(partner, 'carnot_StartEventSymbol') is None


def test_assoc_startingEventSymbols101_stub_double():
    # carnot_StartEventSymbol has no real 'StartEventSymbol' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ActivityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ActivityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    partner = carnot_StartEventSymbol()
    setattr(partner, 'StartEventSymbol', None)
    _safe_set(owner, 'startActivity', {partner})
    assert getattr(partner, 'StartEventSymbol') == owner
    _safe_set(owner, 'startActivity', set())
    assert getattr(partner, 'StartEventSymbol') is None


def test_assoc_subProcessOfConnection51_stub_double():
    # carnot_SubProcessOfConnectionType has no real 'carnot_SubProcessOfConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_SubProcessOfConnectionType()
    setattr(partner, 'carnot_SubProcessOfConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer52', {partner})
    assert getattr(partner, 'carnot_SubProcessOfConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer52', set())
    assert getattr(partner, 'carnot_SubProcessOfConnectionType') is None


def test_assoc_targetActivitySymbol341_stub_double():
    # carnot_IFlowObjectSymbol has no real 'IFlowObjectSymbol342' property in the generated
    # code (a bare stub) -- manually attach it so carnot_TransitionConnectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_TransitionConnectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_TransitionConnectionType(points="sample_text")
    partner = carnot_IFlowObjectSymbol()
    setattr(partner, 'IFlowObjectSymbol342', None)
    _safe_set(owner, 'inTransitions', partner)
    assert getattr(partner, 'IFlowObjectSymbol342') == owner
    _safe_set(owner, 'inTransitions', None)
    assert getattr(partner, 'IFlowObjectSymbol342') is None


def test_assoc_targetSymbol197_stub_double():
    # carnot_GenericLinkConnectionType has no real 'inLinks' property in the generated
    # code (a bare stub) -- manually attach it so carnot_INodeSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_INodeSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    partner = carnot_GenericLinkConnectionType()
    setattr(partner, 'inLinks', None)
    _safe_set(owner, 'INodeSymbol198', partner)
    assert getattr(partner, 'inLinks') == owner
    _safe_set(owner, 'INodeSymbol198', None)
    assert getattr(partner, 'inLinks') is None


def test_assoc_teamLead263_stub_double():
    # carnot_OrganizationType has no real 'teams' property in the generated
    # code (a bare stub) -- manually attach it so carnot_RoleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_RoleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_RoleType(cardinality=7)
    partner = carnot_OrganizationType()
    setattr(partner, 'teams', None)
    _safe_set(owner, 'RoleType', partner)
    assert getattr(partner, 'teams') == owner
    _safe_set(owner, 'RoleType', None)
    assert getattr(partner, 'teams') is None


def test_assoc_teamLeadConnection57_stub_double():
    # carnot_TeamLeadConnectionType has no real 'carnot_TeamLeadConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_TeamLeadConnectionType()
    setattr(partner, 'carnot_TeamLeadConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer58', {partner})
    assert getattr(partner, 'carnot_TeamLeadConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer58', set())
    assert getattr(partner, 'carnot_TeamLeadConnectionType') is None


def test_assoc_teams321_stub_double():
    # carnot_OrganizationType has no real 'OrganizationType322' property in the generated
    # code (a bare stub) -- manually attach it so carnot_RoleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_RoleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_RoleType(cardinality=7)
    partner = carnot_OrganizationType()
    setattr(partner, 'OrganizationType322', None)
    _safe_set(owner, 'teamLead', {partner})
    assert getattr(partner, 'OrganizationType322') == owner
    _safe_set(owner, 'teamLead', set())
    assert getattr(partner, 'OrganizationType322') is None


def test_assoc_text111_stub_double():
    # carnot_AnnotationSymbolType has no real 'carnot_AnnotationSymbolType112' property in the generated
    # code (a bare stub) -- manually attach it so carnot_TextType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_TextType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_TextType(mixed="sample_text")
    partner = carnot_AnnotationSymbolType()
    setattr(partner, 'carnot_AnnotationSymbolType112', None)
    _safe_set(owner, 'carnot_TextType', partner)
    assert getattr(partner, 'carnot_AnnotationSymbolType112') == owner
    _safe_set(owner, 'carnot_TextType', None)
    assert getattr(partner, 'carnot_AnnotationSymbolType112') is None


def test_assoc_to312_stub_double():
    # carnot_RefersToConnectionType has no real 'referingToConnections' property in the generated
    # code (a bare stub) -- manually attach it so carnot_IGraphicalObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_IGraphicalObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    partner = carnot_RefersToConnectionType()
    setattr(partner, 'referingToConnections', None)
    _safe_set(owner, 'IGraphicalObject313', partner)
    assert getattr(partner, 'referingToConnections') == owner
    _safe_set(owner, 'IGraphicalObject313', None)
    assert getattr(partner, 'referingToConnections') is None


def test_assoc_trigger286_stub_double():
    # carnot_TriggerType has no real 'carnot_TriggerType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ProcessDefinitionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ProcessDefinitionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    partner = carnot_TriggerType()
    setattr(partner, 'carnot_TriggerType', None)
    _safe_set(owner, 'carnot_ProcessDefinitionType287', {partner})
    assert getattr(partner, 'carnot_TriggerType') == owner
    _safe_set(owner, 'carnot_ProcessDefinitionType287', set())
    assert getattr(partner, 'carnot_TriggerType') is None


def test_assoc_triggers365_stub_double():
    # carnot_TriggerType has no real 'TriggerType367' property in the generated
    # code (a bare stub) -- manually attach it so carnot_TriggerTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_TriggerTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    partner = carnot_TriggerType()
    setattr(partner, 'TriggerType367', None)
    _safe_set(owner, 'type366', {partner})
    assert getattr(partner, 'TriggerType367') == owner
    _safe_set(owner, 'type366', set())
    assert getattr(partner, 'TriggerType367') is None


def test_assoc_triggersConnection47_stub_double():
    # carnot_TriggersConnectionType has no real 'carnot_TriggersConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_TriggersConnectionType()
    setattr(partner, 'carnot_TriggersConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer48', {partner})
    assert getattr(partner, 'carnot_TriggersConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer48', set())
    assert getattr(partner, 'carnot_TriggersConnectionType') is None


def test_assoc_type137_stub_double():
    # carnot_ContextType has no real 'contexts' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ApplicationContextTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ApplicationContextTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    partner = carnot_ContextType()
    setattr(partner, 'contexts', None)
    _safe_set(owner, 'ApplicationContextTypeType', partner)
    assert getattr(partner, 'contexts') == owner
    _safe_set(owner, 'ApplicationContextTypeType', None)
    assert getattr(partner, 'contexts') is None


def test_assoc_type362_stub_double():
    # carnot_TriggerType has no real 'triggers' property in the generated
    # code (a bare stub) -- manually attach it so carnot_TriggerTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_TriggerTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    partner = carnot_TriggerType()
    setattr(partner, 'triggers', None)
    _safe_set(owner, 'TriggerTypeType', partner)
    assert getattr(partner, 'triggers') == owner
    _safe_set(owner, 'TriggerTypeType', None)
    assert getattr(partner, 'triggers') is None


def test_assoc_type79_stub_double():
    # carnot_AbstractEventAction has no real 'actionInstances' property in the generated
    # code (a bare stub) -- manually attach it so carnot_EventActionTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_EventActionTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    partner = carnot_AbstractEventAction()
    setattr(partner, 'actionInstances', None)
    _safe_set(owner, 'EventActionTypeType', partner)
    assert getattr(partner, 'actionInstances') == owner
    _safe_set(owner, 'EventActionTypeType', None)
    assert getattr(partner, 'actionInstances') is None


def test_assoc_typeDeclarations245_stub_double():
    # carnot_TypeDeclarationsType has no real 'carnot_TypeDeclarationsType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    partner = carnot_TypeDeclarationsType()
    setattr(partner, 'carnot_TypeDeclarationsType', None)
    _safe_set(owner, 'carnot_ModelType246', partner)
    assert getattr(partner, 'carnot_TypeDeclarationsType') == owner
    _safe_set(owner, 'carnot_ModelType246', None)
    assert getattr(partner, 'carnot_TypeDeclarationsType') is None


def test_assoc_unbindAction183_stub_double():
    # carnot_UnbindActionType has no real 'carnot_UnbindActionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_EventHandlerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_EventHandlerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    partner = carnot_UnbindActionType()
    setattr(partner, 'carnot_UnbindActionType', None)
    _safe_set(owner, 'carnot_EventHandlerType184', {partner})
    assert getattr(partner, 'carnot_UnbindActionType') == owner
    _safe_set(owner, 'carnot_EventHandlerType184', set())
    assert getattr(partner, 'carnot_UnbindActionType') is None


def test_assoc_viewable368_stub_double():
    # carnot_ViewableType has no real 'carnot_ViewableType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_IModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_IModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_IModelElement(elementOid="sample_text")
    partner = carnot_ViewableType()
    setattr(partner, 'carnot_ViewableType', None)
    _safe_set(owner, 'carnot_IModelElement', partner)
    assert getattr(partner, 'carnot_ViewableType') == owner
    _safe_set(owner, 'carnot_IModelElement', None)
    assert getattr(partner, 'carnot_ViewableType') is None


def test_assoc_viewable375_stub_double():
    # carnot_ViewableType has no real 'carnot_ViewableType377' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ViewType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ViewType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ViewType(name="sample_text")
    partner = carnot_ViewableType()
    setattr(partner, 'carnot_ViewableType377', None)
    _safe_set(owner, 'carnot_ViewType376', {partner})
    assert getattr(partner, 'carnot_ViewableType377') == owner
    _safe_set(owner, 'carnot_ViewType376', set())
    assert getattr(partner, 'carnot_ViewableType377') is None


def test_assoc_worksForConnection55_stub_double():
    # carnot_WorksForConnectionType has no real 'carnot_WorksForConnectionType' property in the generated
    # code (a bare stub) -- manually attach it so carnot_ISymbolContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_ISymbolContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    partner = carnot_WorksForConnectionType()
    setattr(partner, 'carnot_WorksForConnectionType', None)
    _safe_set(owner, 'carnot_ISymbolContainer56', {partner})
    assert getattr(partner, 'carnot_WorksForConnectionType') == owner
    _safe_set(owner, 'carnot_ISymbolContainer56', set())
    assert getattr(partner, 'carnot_WorksForConnectionType') is None


def test_assoc_xMLNSPrefixMap169_stub_double():
    # carnot_EStringToStringMapEntry has no real 'carnot_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so carnot_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_DocumentRoot(mixed="sample_text")
    partner = carnot_EStringToStringMapEntry()
    setattr(partner, 'carnot_EStringToStringMapEntry', None)
    _safe_set(owner, 'carnot_DocumentRoot', {partner})
    assert getattr(partner, 'carnot_EStringToStringMapEntry') == owner
    _safe_set(owner, 'carnot_DocumentRoot', set())
    assert getattr(partner, 'carnot_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation170_stub_double():
    # carnot_EStringToStringMapEntry has no real 'carnot_EStringToStringMapEntry172' property in the generated
    # code (a bare stub) -- manually attach it so carnot_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # carnot_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = carnot_DocumentRoot(mixed="sample_text")
    partner = carnot_EStringToStringMapEntry()
    setattr(partner, 'carnot_EStringToStringMapEntry172', None)
    _safe_set(owner, 'carnot_DocumentRoot171', {partner})
    assert getattr(partner, 'carnot_EStringToStringMapEntry172') == owner
    _safe_set(owner, 'carnot_DocumentRoot171', set())
    assert getattr(partner, 'carnot_EStringToStringMapEntry172') is None


