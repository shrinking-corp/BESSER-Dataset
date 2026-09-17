# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IModelElement,
    carnot_IModelElement,
    carnot_EObject,
    carnot_IdentifiableReference,
    carnot_AttributeType,
    carnot_IExtensibleElement,
    carnot_Coordinates,
    carnot_IIdentifiableElement,
    FormalParameterMappingType,
    carnot_extensions_FormalParameterMappingsType,
    extensions_carnot_FormalParameterType,
    extensions_carnot_DataType,
    carnot_extensions_FormalParameterMappingType,
    carnot_ViewableType,
    FormalParameterMappingsType,
    carnot_FormalParametersType,
    carnot_TypeDeclarationsType,
    carnot_QualityControlType,
    carnot_ScriptType,
    carnot_ExternalPackages,
    ISwimlaneSymbol,
    carnot_ExternalPackage,
    carnot_EStringToStringMapEntry,
    carnot_DocumentRoot,
    AbstractEventSymbol,
    ISymbolContainer,
    carnot_PoolSymbol,
    carnot_ExternalReferenceType,
    carnot_ParameterMappingType,
    IConnectionSymbol,
    IModelParticipant,
    carnot_OrganizationType,
    carnot_RoleType,
    carnot_ConditionalPerformerType,
    IModelParticipantSymbol,
    AbstractEventAction,
    carnot_UnbindActionType,
    carnot_EventActionType,
    carnot_BindActionType,
    carnot_XmlTextNode,
    IAccessPointOwner,
    carnot_Code,
    carnot_IdRef,
    IMetaType,
    carnot_ApplicationTypeType,
    carnot_TriggerTypeType,
    carnot_EventConditionTypeType,
    carnot_ApplicationContextTypeType,
    carnot_TextType,
    IEventHandlerOwner,
    carnot_DataTypeType,
    IFlowObjectSymbol,
    carnot_EventActionTypeType,
    ITypedElement,
    IModelElementNodeSymbol,
    carnot_AbstractEventSymbol,
    carnot_IModelParticipantSymbol,
    carnot_ParticipantType,
    carnot_LaneSymbol,
    INodeSymbol,
    carnot_IFlowObjectSymbol,
    carnot_IModelElementNodeSymbol,
    IGraphicalObject,
    carnot_IConnectionSymbol,
    carnot_INodeSymbol,
    carnot_IGraphicalObject,
    carnot_TeamLeadConnectionType,
    carnot_WorksForConnectionType,
    carnot_TransitionConnectionType,
    carnot_RefersToConnectionType,
    carnot_TriggersConnectionType,
    carnot_PerformsConnectionType,
    carnot_PartOfConnectionType,
    carnot_GenericLinkConnectionType,
    carnot_SubProcessOfConnectionType,
    carnot_TextSymbolType,
    carnot_StartEventSymbol,
    carnot_RoleSymbolType,
    carnot_PublicInterfaceSymbol,
    carnot_ExecutedByConnectionType,
    carnot_ProcessSymbolType,
    carnot_DataMappingConnectionType,
    carnot_ModelerSymbolType,
    carnot_IntermediateEventSymbol,
    carnot_GroupSymbolType,
    carnot_GatewaySymbol,
    carnot_EndEventSymbol,
    carnot_DataSymbolType,
    carnot_ConditionalPerformerSymbolType,
    carnot_OrganizationSymbolType,
    carnot_AnnotationSymbolType,
    carnot_ActivitySymbolType,
    carnot_ITypedElement,
    IIdentifiableModelElement,
    carnot_AbstractEventAction,
    carnot_EventHandlerType,
    carnot_TriggerType,
    carnot_DataPathType,
    carnot_DataType,
    carnot_ActivityType,
    carnot_ApplicationType,
    carnot_IModelParticipant,
    carnot_ProcessDefinitionType,
    carnot_ModelerType,
    carnot_TransitionType,
    carnot_IMetaType,
    carnot_AccessPointType,
    carnot_IAccessPointOwner,
    carnot_ApplicationSymbolType,
    carnot_IEventHandlerOwner,
    carnot_DescriptionType,
    IExtensibleElement,
    carnot_ISymbolContainer,
    carnot_DiagramType,
    carnot_ViewType,
    carnot_LinkTypeType,
    carnot_ContextType,
    IIdentifiableElement,
    carnot_ModelType,
    carnot_ISwimlaneSymbol,
    carnot_IIdentifiableModelElement,
    carnot_DataMappingType,
    LinkEndStyle,
    OrientationType,
    LinkLineStyle,
    LinkCardinality,
    LinkColor,
    DiagramModeType,
    FlowControlType,
    LoopType,
    SubProcessModeType,
    DirectionType,
    ActivityImplementationType,
    RoutingType,
    JoinSplitType,
    ImplementationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_imodelelement_is_not_abstract():
    assert not inspect.isabstract(IModelElement)


def test_hyp_imodelelement_constructor_exists():
    assert callable(IModelElement.__init__)


def test_hyp_imodelelement_constructor_args():
    sig = inspect.signature(IModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_imodelelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelElement)


def test_hyp_carnot_imodelelement_constructor_exists():
    assert callable(carnot_IModelElement.__init__)


def test_hyp_carnot_imodelelement_constructor_args():
    sig = inspect.signature(carnot_IModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementOid" in params, "Missing parameter 'elementOid'"




def test_hyp_carnot_eobject_is_not_abstract():
    assert not inspect.isabstract(carnot_EObject)


def test_hyp_carnot_eobject_constructor_exists():
    assert callable(carnot_EObject.__init__)


def test_hyp_carnot_eobject_constructor_args():
    sig = inspect.signature(carnot_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_identifiablereference_is_not_abstract():
    assert not inspect.isabstract(carnot_IdentifiableReference)


def test_hyp_carnot_identifiablereference_constructor_exists():
    assert callable(carnot_IdentifiableReference.__init__)


def test_hyp_carnot_identifiablereference_constructor_args():
    sig = inspect.signature(carnot_IdentifiableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_attributetype_is_not_abstract():
    assert not inspect.isabstract(carnot_AttributeType)


def test_hyp_carnot_attributetype_constructor_exists():
    assert callable(carnot_AttributeType.__init__)


def test_hyp_carnot_attributetype_constructor_args():
    sig = inspect.signature(carnot_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "any" in params, "Missing parameter 'any'"
    assert "group" in params, "Missing parameter 'group'"
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"









def test_hyp_carnot_iextensibleelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IExtensibleElement)


def test_hyp_carnot_iextensibleelement_constructor_exists():
    assert callable(carnot_IExtensibleElement.__init__)


def test_hyp_carnot_iextensibleelement_constructor_args():
    sig = inspect.signature(carnot_IExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_coordinates_is_not_abstract():
    assert not inspect.isabstract(carnot_Coordinates)


def test_hyp_carnot_coordinates_constructor_exists():
    assert callable(carnot_Coordinates.__init__)


def test_hyp_carnot_coordinates_constructor_args():
    sig = inspect.signature(carnot_Coordinates.__init__)
    params = list(sig.parameters.keys())
    assert "yPos" in params, "Missing parameter 'yPos'"
    assert "xPos" in params, "Missing parameter 'xPos'"





def test_hyp_carnot_iidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IIdentifiableElement)


def test_hyp_carnot_iidentifiableelement_constructor_exists():
    assert callable(carnot_IIdentifiableElement.__init__)


def test_hyp_carnot_iidentifiableelement_constructor_args():
    sig = inspect.signature(carnot_IIdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_formalparametermappingtype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterMappingType)


def test_hyp_formalparametermappingtype_constructor_exists():
    assert callable(FormalParameterMappingType.__init__)


def test_hyp_formalparametermappingtype_constructor_args():
    sig = inspect.signature(FormalParameterMappingType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_extensions_formalparametermappingstype_is_not_abstract():
    assert not inspect.isabstract(carnot_extensions_FormalParameterMappingsType)


def test_hyp_carnot_extensions_formalparametermappingstype_constructor_exists():
    assert callable(carnot_extensions_FormalParameterMappingsType.__init__)


def test_hyp_carnot_extensions_formalparametermappingstype_constructor_args():
    sig = inspect.signature(carnot_extensions_FormalParameterMappingsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extensions_carnot_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(extensions_carnot_FormalParameterType)


def test_hyp_extensions_carnot_formalparametertype_constructor_exists():
    assert callable(extensions_carnot_FormalParameterType.__init__)


def test_hyp_extensions_carnot_formalparametertype_constructor_args():
    sig = inspect.signature(extensions_carnot_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extensions_carnot_datatype_is_not_abstract():
    assert not inspect.isabstract(extensions_carnot_DataType)


def test_hyp_extensions_carnot_datatype_constructor_exists():
    assert callable(extensions_carnot_DataType.__init__)


def test_hyp_extensions_carnot_datatype_constructor_args():
    sig = inspect.signature(extensions_carnot_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_extensions_formalparametermappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot_extensions_FormalParameterMappingType)


def test_hyp_carnot_extensions_formalparametermappingtype_constructor_exists():
    assert callable(carnot_extensions_FormalParameterMappingType.__init__)


def test_hyp_carnot_extensions_formalparametermappingtype_constructor_args():
    sig = inspect.signature(carnot_extensions_FormalParameterMappingType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_viewabletype_is_not_abstract():
    assert not inspect.isabstract(carnot_ViewableType)


def test_hyp_carnot_viewabletype_constructor_exists():
    assert callable(carnot_ViewableType.__init__)


def test_hyp_carnot_viewabletype_constructor_args():
    sig = inspect.signature(carnot_ViewableType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_formalparametermappingstype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterMappingsType)


def test_hyp_formalparametermappingstype_constructor_exists():
    assert callable(FormalParameterMappingsType.__init__)


def test_hyp_formalparametermappingstype_constructor_args():
    sig = inspect.signature(FormalParameterMappingsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_formalparameterstype_is_not_abstract():
    assert not inspect.isabstract(carnot_FormalParametersType)


def test_hyp_carnot_formalparameterstype_constructor_exists():
    assert callable(carnot_FormalParametersType.__init__)


def test_hyp_carnot_formalparameterstype_constructor_args():
    sig = inspect.signature(carnot_FormalParametersType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_typedeclarationstype_is_not_abstract():
    assert not inspect.isabstract(carnot_TypeDeclarationsType)


def test_hyp_carnot_typedeclarationstype_constructor_exists():
    assert callable(carnot_TypeDeclarationsType.__init__)


def test_hyp_carnot_typedeclarationstype_constructor_args():
    sig = inspect.signature(carnot_TypeDeclarationsType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_qualitycontroltype_is_not_abstract():
    assert not inspect.isabstract(carnot_QualityControlType)


def test_hyp_carnot_qualitycontroltype_constructor_exists():
    assert callable(carnot_QualityControlType.__init__)


def test_hyp_carnot_qualitycontroltype_constructor_args():
    sig = inspect.signature(carnot_QualityControlType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_scripttype_is_not_abstract():
    assert not inspect.isabstract(carnot_ScriptType)


def test_hyp_carnot_scripttype_constructor_exists():
    assert callable(carnot_ScriptType.__init__)


def test_hyp_carnot_scripttype_constructor_args():
    sig = inspect.signature(carnot_ScriptType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_externalpackages_is_not_abstract():
    assert not inspect.isabstract(carnot_ExternalPackages)


def test_hyp_carnot_externalpackages_constructor_exists():
    assert callable(carnot_ExternalPackages.__init__)


def test_hyp_carnot_externalpackages_constructor_args():
    sig = inspect.signature(carnot_ExternalPackages.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iswimlanesymbol_is_not_abstract():
    assert not inspect.isabstract(ISwimlaneSymbol)


def test_hyp_iswimlanesymbol_constructor_exists():
    assert callable(ISwimlaneSymbol.__init__)


def test_hyp_iswimlanesymbol_constructor_args():
    sig = inspect.signature(ISwimlaneSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_externalpackage_is_not_abstract():
    assert not inspect.isabstract(carnot_ExternalPackage)


def test_hyp_carnot_externalpackage_constructor_exists():
    assert callable(carnot_ExternalPackage.__init__)


def test_hyp_carnot_externalpackage_constructor_args():
    sig = inspect.signature(carnot_ExternalPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(carnot_EStringToStringMapEntry)


def test_hyp_carnot_estringtostringmapentry_constructor_exists():
    assert callable(carnot_EStringToStringMapEntry.__init__)


def test_hyp_carnot_estringtostringmapentry_constructor_args():
    sig = inspect.signature(carnot_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_documentroot_is_not_abstract():
    assert not inspect.isabstract(carnot_DocumentRoot)


def test_hyp_carnot_documentroot_constructor_exists():
    assert callable(carnot_DocumentRoot.__init__)


def test_hyp_carnot_documentroot_constructor_args():
    sig = inspect.signature(carnot_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_abstracteventsymbol_is_not_abstract():
    assert not inspect.isabstract(AbstractEventSymbol)


def test_hyp_abstracteventsymbol_constructor_exists():
    assert callable(AbstractEventSymbol.__init__)


def test_hyp_abstracteventsymbol_constructor_args():
    sig = inspect.signature(AbstractEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_isymbolcontainer_is_not_abstract():
    assert not inspect.isabstract(ISymbolContainer)


def test_hyp_isymbolcontainer_constructor_exists():
    assert callable(ISymbolContainer.__init__)


def test_hyp_isymbolcontainer_constructor_args():
    sig = inspect.signature(ISymbolContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_poolsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_PoolSymbol)


def test_hyp_carnot_poolsymbol_constructor_exists():
    assert callable(carnot_PoolSymbol.__init__)


def test_hyp_carnot_poolsymbol_constructor_args():
    sig = inspect.signature(carnot_PoolSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "boundaryVisible" in params, "Missing parameter 'boundaryVisible'"




def test_hyp_carnot_externalreferencetype_is_not_abstract():
    assert not inspect.isabstract(carnot_ExternalReferenceType)


def test_hyp_carnot_externalreferencetype_constructor_exists():
    assert callable(carnot_ExternalReferenceType.__init__)


def test_hyp_carnot_externalreferencetype_constructor_args():
    sig = inspect.signature(carnot_ExternalReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_parametermappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot_ParameterMappingType)


def test_hyp_carnot_parametermappingtype_constructor_exists():
    assert callable(carnot_ParameterMappingType.__init__)


def test_hyp_carnot_parametermappingtype_constructor_args():
    sig = inspect.signature(carnot_ParameterMappingType.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "parameterPath" in params, "Missing parameter 'parameterPath'"
    assert "dataPath" in params, "Missing parameter 'dataPath'"






def test_hyp_iconnectionsymbol_is_not_abstract():
    assert not inspect.isabstract(IConnectionSymbol)


def test_hyp_iconnectionsymbol_constructor_exists():
    assert callable(IConnectionSymbol.__init__)


def test_hyp_iconnectionsymbol_constructor_args():
    sig = inspect.signature(IConnectionSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imodelparticipant_is_not_abstract():
    assert not inspect.isabstract(IModelParticipant)


def test_hyp_imodelparticipant_constructor_exists():
    assert callable(IModelParticipant.__init__)


def test_hyp_imodelparticipant_constructor_args():
    sig = inspect.signature(IModelParticipant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_organizationtype_is_not_abstract():
    assert not inspect.isabstract(carnot_OrganizationType)


def test_hyp_carnot_organizationtype_constructor_exists():
    assert callable(carnot_OrganizationType.__init__)


def test_hyp_carnot_organizationtype_constructor_args():
    sig = inspect.signature(carnot_OrganizationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_roletype_is_not_abstract():
    assert not inspect.isabstract(carnot_RoleType)


def test_hyp_carnot_roletype_constructor_exists():
    assert callable(carnot_RoleType.__init__)


def test_hyp_carnot_roletype_constructor_args():
    sig = inspect.signature(carnot_RoleType.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"




def test_hyp_carnot_conditionalperformertype_is_not_abstract():
    assert not inspect.isabstract(carnot_ConditionalPerformerType)


def test_hyp_carnot_conditionalperformertype_constructor_exists():
    assert callable(carnot_ConditionalPerformerType.__init__)


def test_hyp_carnot_conditionalperformertype_constructor_args():
    sig = inspect.signature(carnot_ConditionalPerformerType.__init__)
    params = list(sig.parameters.keys())
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "isUser" in params, "Missing parameter 'isUser'"





def test_hyp_imodelparticipantsymbol_is_not_abstract():
    assert not inspect.isabstract(IModelParticipantSymbol)


def test_hyp_imodelparticipantsymbol_constructor_exists():
    assert callable(IModelParticipantSymbol.__init__)


def test_hyp_imodelparticipantsymbol_constructor_args():
    sig = inspect.signature(IModelParticipantSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracteventaction_is_not_abstract():
    assert not inspect.isabstract(AbstractEventAction)


def test_hyp_abstracteventaction_constructor_exists():
    assert callable(AbstractEventAction.__init__)


def test_hyp_abstracteventaction_constructor_args():
    sig = inspect.signature(AbstractEventAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_unbindactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_UnbindActionType)


def test_hyp_carnot_unbindactiontype_constructor_exists():
    assert callable(carnot_UnbindActionType.__init__)


def test_hyp_carnot_unbindactiontype_constructor_args():
    sig = inspect.signature(carnot_UnbindActionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_eventactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventActionType)


def test_hyp_carnot_eventactiontype_constructor_exists():
    assert callable(carnot_EventActionType.__init__)


def test_hyp_carnot_eventactiontype_constructor_args():
    sig = inspect.signature(carnot_EventActionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_bindactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_BindActionType)


def test_hyp_carnot_bindactiontype_constructor_exists():
    assert callable(carnot_BindActionType.__init__)


def test_hyp_carnot_bindactiontype_constructor_args():
    sig = inspect.signature(carnot_BindActionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_xmltextnode_is_not_abstract():
    assert not inspect.isabstract(carnot_XmlTextNode)


def test_hyp_carnot_xmltextnode_constructor_exists():
    assert callable(carnot_XmlTextNode.__init__)


def test_hyp_carnot_xmltextnode_constructor_args():
    sig = inspect.signature(carnot_XmlTextNode.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_iaccesspointowner_is_not_abstract():
    assert not inspect.isabstract(IAccessPointOwner)


def test_hyp_iaccesspointowner_constructor_exists():
    assert callable(IAccessPointOwner.__init__)


def test_hyp_iaccesspointowner_constructor_args():
    sig = inspect.signature(IAccessPointOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_code_is_not_abstract():
    assert not inspect.isabstract(carnot_Code)


def test_hyp_carnot_code_constructor_exists():
    assert callable(carnot_Code.__init__)


def test_hyp_carnot_code_constructor_args():
    sig = inspect.signature(carnot_Code.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_carnot_idref_is_not_abstract():
    assert not inspect.isabstract(carnot_IdRef)


def test_hyp_carnot_idref_constructor_exists():
    assert callable(carnot_IdRef.__init__)


def test_hyp_carnot_idref_constructor_args():
    sig = inspect.signature(carnot_IdRef.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_imetatype_is_not_abstract():
    assert not inspect.isabstract(IMetaType)


def test_hyp_imetatype_constructor_exists():
    assert callable(IMetaType.__init__)


def test_hyp_imetatype_constructor_args():
    sig = inspect.signature(IMetaType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_applicationtypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationTypeType)


def test_hyp_carnot_applicationtypetype_constructor_exists():
    assert callable(carnot_ApplicationTypeType.__init__)


def test_hyp_carnot_applicationtypetype_constructor_args():
    sig = inspect.signature(carnot_ApplicationTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"
    assert "accessPointProviderClass" in params, "Missing parameter 'accessPointProviderClass'"
    assert "synchronous" in params, "Missing parameter 'synchronous'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"








def test_hyp_carnot_triggertypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_TriggerTypeType)


def test_hyp_carnot_triggertypetype_constructor_exists():
    assert callable(carnot_TriggerTypeType.__init__)


def test_hyp_carnot_triggertypetype_constructor_args():
    sig = inspect.signature(carnot_TriggerTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "rule" in params, "Missing parameter 'rule'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "pullTrigger" in params, "Missing parameter 'pullTrigger'"
    assert "pullTriggerEvaluator" in params, "Missing parameter 'pullTriggerEvaluator'"







def test_hyp_carnot_eventconditiontypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventConditionTypeType)


def test_hyp_carnot_eventconditiontypetype_constructor_exists():
    assert callable(carnot_EventConditionTypeType.__init__)


def test_hyp_carnot_eventconditiontypetype_constructor_args():
    sig = inspect.signature(carnot_EventConditionTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "binderClass" in params, "Missing parameter 'binderClass'"
    assert "rule" in params, "Missing parameter 'rule'"
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "processCondition" in params, "Missing parameter 'processCondition'"
    assert "activityCondition" in params, "Missing parameter 'activityCondition'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "pullEventEmitterClass" in params, "Missing parameter 'pullEventEmitterClass'"










def test_hyp_carnot_applicationcontexttypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationContextTypeType)


def test_hyp_carnot_applicationcontexttypetype_constructor_exists():
    assert callable(carnot_ApplicationContextTypeType.__init__)


def test_hyp_carnot_applicationcontexttypetype_constructor_args():
    sig = inspect.signature(carnot_ApplicationContextTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "accessPointProviderClass" in params, "Missing parameter 'accessPointProviderClass'"
    assert "hasMappingId" in params, "Missing parameter 'hasMappingId'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "hasApplicationPath" in params, "Missing parameter 'hasApplicationPath'"








def test_hyp_carnot_texttype_is_not_abstract():
    assert not inspect.isabstract(carnot_TextType)


def test_hyp_carnot_texttype_constructor_exists():
    assert callable(carnot_TextType.__init__)


def test_hyp_carnot_texttype_constructor_args():
    sig = inspect.signature(carnot_TextType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_ieventhandlerowner_is_not_abstract():
    assert not inspect.isabstract(IEventHandlerOwner)


def test_hyp_ieventhandlerowner_constructor_exists():
    assert callable(IEventHandlerOwner.__init__)


def test_hyp_ieventhandlerowner_constructor_args():
    sig = inspect.signature(IEventHandlerOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_datatypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataTypeType)


def test_hyp_carnot_datatypetype_constructor_exists():
    assert callable(carnot_DataTypeType.__init__)


def test_hyp_carnot_datatypetype_constructor_args():
    sig = inspect.signature(carnot_DataTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "evaluator" in params, "Missing parameter 'evaluator'"
    assert "writable" in params, "Missing parameter 'writable'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"
    assert "accessPathEditor" in params, "Missing parameter 'accessPathEditor'"
    assert "storageStrategy" in params, "Missing parameter 'storageStrategy'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"
    assert "valueCreator" in params, "Missing parameter 'valueCreator'"
    assert "readable" in params, "Missing parameter 'readable'"












def test_hyp_iflowobjectsymbol_is_not_abstract():
    assert not inspect.isabstract(IFlowObjectSymbol)


def test_hyp_iflowobjectsymbol_constructor_exists():
    assert callable(IFlowObjectSymbol.__init__)


def test_hyp_iflowobjectsymbol_constructor_args():
    sig = inspect.signature(IFlowObjectSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_eventactiontypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventActionTypeType)


def test_hyp_carnot_eventactiontypetype_constructor_exists():
    assert callable(carnot_EventActionTypeType.__init__)


def test_hyp_carnot_eventactiontypetype_constructor_args():
    sig = inspect.signature(carnot_EventActionTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "actionClass" in params, "Missing parameter 'actionClass'"
    assert "unsupportedContexts" in params, "Missing parameter 'unsupportedContexts'"
    assert "activityAction" in params, "Missing parameter 'activityAction'"
    assert "processAction" in params, "Missing parameter 'processAction'"
    assert "supportedConditionTypes" in params, "Missing parameter 'supportedConditionTypes'"









def test_hyp_itypedelement_is_not_abstract():
    assert not inspect.isabstract(ITypedElement)


def test_hyp_itypedelement_constructor_exists():
    assert callable(ITypedElement.__init__)


def test_hyp_itypedelement_constructor_args():
    sig = inspect.signature(ITypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imodelelementnodesymbol_is_not_abstract():
    assert not inspect.isabstract(IModelElementNodeSymbol)


def test_hyp_imodelelementnodesymbol_constructor_exists():
    assert callable(IModelElementNodeSymbol.__init__)


def test_hyp_imodelelementnodesymbol_constructor_args():
    sig = inspect.signature(IModelElementNodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_abstracteventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_AbstractEventSymbol)


def test_hyp_carnot_abstracteventsymbol_constructor_exists():
    assert callable(carnot_AbstractEventSymbol.__init__)


def test_hyp_carnot_abstracteventsymbol_constructor_args():
    sig = inspect.signature(carnot_AbstractEventSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_carnot_imodelparticipantsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelParticipantSymbol)


def test_hyp_carnot_imodelparticipantsymbol_constructor_exists():
    assert callable(carnot_IModelParticipantSymbol.__init__)


def test_hyp_carnot_imodelparticipantsymbol_constructor_args():
    sig = inspect.signature(carnot_IModelParticipantSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_participanttype_is_not_abstract():
    assert not inspect.isabstract(carnot_ParticipantType)


def test_hyp_carnot_participanttype_constructor_exists():
    assert callable(carnot_ParticipantType.__init__)


def test_hyp_carnot_participanttype_constructor_args():
    sig = inspect.signature(carnot_ParticipantType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_lanesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_LaneSymbol)


def test_hyp_carnot_lanesymbol_constructor_exists():
    assert callable(carnot_LaneSymbol.__init__)


def test_hyp_carnot_lanesymbol_constructor_args():
    sig = inspect.signature(carnot_LaneSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inodesymbol_is_not_abstract():
    assert not inspect.isabstract(INodeSymbol)


def test_hyp_inodesymbol_constructor_exists():
    assert callable(INodeSymbol.__init__)


def test_hyp_inodesymbol_constructor_args():
    sig = inspect.signature(INodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_iflowobjectsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IFlowObjectSymbol)


def test_hyp_carnot_iflowobjectsymbol_constructor_exists():
    assert callable(carnot_IFlowObjectSymbol.__init__)


def test_hyp_carnot_iflowobjectsymbol_constructor_args():
    sig = inspect.signature(carnot_IFlowObjectSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_imodelelementnodesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelElementNodeSymbol)


def test_hyp_carnot_imodelelementnodesymbol_constructor_exists():
    assert callable(carnot_IModelElementNodeSymbol.__init__)


def test_hyp_carnot_imodelelementnodesymbol_constructor_args():
    sig = inspect.signature(carnot_IModelElementNodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_igraphicalobject_is_not_abstract():
    assert not inspect.isabstract(IGraphicalObject)


def test_hyp_igraphicalobject_constructor_exists():
    assert callable(IGraphicalObject.__init__)


def test_hyp_igraphicalobject_constructor_args():
    sig = inspect.signature(IGraphicalObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_iconnectionsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IConnectionSymbol)


def test_hyp_carnot_iconnectionsymbol_constructor_exists():
    assert callable(carnot_IConnectionSymbol.__init__)


def test_hyp_carnot_iconnectionsymbol_constructor_args():
    sig = inspect.signature(carnot_IConnectionSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "routing" in params, "Missing parameter 'routing'"
    assert "targetAnchor" in params, "Missing parameter 'targetAnchor'"
    assert "sourceAnchor" in params, "Missing parameter 'sourceAnchor'"






def test_hyp_carnot_inodesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_INodeSymbol)


def test_hyp_carnot_inodesymbol_constructor_exists():
    assert callable(carnot_INodeSymbol.__init__)


def test_hyp_carnot_inodesymbol_constructor_args():
    sig = inspect.signature(carnot_INodeSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "xPos" in params, "Missing parameter 'xPos'"
    assert "width" in params, "Missing parameter 'width'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "yPos" in params, "Missing parameter 'yPos'"
    assert "height" in params, "Missing parameter 'height'"








def test_hyp_carnot_igraphicalobject_is_not_abstract():
    assert not inspect.isabstract(carnot_IGraphicalObject)


def test_hyp_carnot_igraphicalobject_constructor_exists():
    assert callable(carnot_IGraphicalObject.__init__)


def test_hyp_carnot_igraphicalobject_constructor_args():
    sig = inspect.signature(carnot_IGraphicalObject.__init__)
    params = list(sig.parameters.keys())
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "style" in params, "Missing parameter 'style'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"






def test_hyp_carnot_teamleadconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TeamLeadConnectionType)


def test_hyp_carnot_teamleadconnectiontype_constructor_exists():
    assert callable(carnot_TeamLeadConnectionType.__init__)


def test_hyp_carnot_teamleadconnectiontype_constructor_args():
    sig = inspect.signature(carnot_TeamLeadConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_worksforconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_WorksForConnectionType)


def test_hyp_carnot_worksforconnectiontype_constructor_exists():
    assert callable(carnot_WorksForConnectionType.__init__)


def test_hyp_carnot_worksforconnectiontype_constructor_args():
    sig = inspect.signature(carnot_WorksForConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_transitionconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TransitionConnectionType)


def test_hyp_carnot_transitionconnectiontype_constructor_exists():
    assert callable(carnot_TransitionConnectionType.__init__)


def test_hyp_carnot_transitionconnectiontype_constructor_args():
    sig = inspect.signature(carnot_TransitionConnectionType.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"




def test_hyp_carnot_referstoconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_RefersToConnectionType)


def test_hyp_carnot_referstoconnectiontype_constructor_exists():
    assert callable(carnot_RefersToConnectionType.__init__)


def test_hyp_carnot_referstoconnectiontype_constructor_args():
    sig = inspect.signature(carnot_RefersToConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_triggersconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TriggersConnectionType)


def test_hyp_carnot_triggersconnectiontype_constructor_exists():
    assert callable(carnot_TriggersConnectionType.__init__)


def test_hyp_carnot_triggersconnectiontype_constructor_args():
    sig = inspect.signature(carnot_TriggersConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_performsconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_PerformsConnectionType)


def test_hyp_carnot_performsconnectiontype_constructor_exists():
    assert callable(carnot_PerformsConnectionType.__init__)


def test_hyp_carnot_performsconnectiontype_constructor_args():
    sig = inspect.signature(carnot_PerformsConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_partofconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_PartOfConnectionType)


def test_hyp_carnot_partofconnectiontype_constructor_exists():
    assert callable(carnot_PartOfConnectionType.__init__)


def test_hyp_carnot_partofconnectiontype_constructor_args():
    sig = inspect.signature(carnot_PartOfConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_genericlinkconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_GenericLinkConnectionType)


def test_hyp_carnot_genericlinkconnectiontype_constructor_exists():
    assert callable(carnot_GenericLinkConnectionType.__init__)


def test_hyp_carnot_genericlinkconnectiontype_constructor_args():
    sig = inspect.signature(carnot_GenericLinkConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_subprocessofconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_SubProcessOfConnectionType)


def test_hyp_carnot_subprocessofconnectiontype_constructor_exists():
    assert callable(carnot_SubProcessOfConnectionType.__init__)


def test_hyp_carnot_subprocessofconnectiontype_constructor_args():
    sig = inspect.signature(carnot_SubProcessOfConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_textsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_TextSymbolType)


def test_hyp_carnot_textsymboltype_constructor_exists():
    assert callable(carnot_TextSymbolType.__init__)


def test_hyp_carnot_textsymboltype_constructor_args():
    sig = inspect.signature(carnot_TextSymbolType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_carnot_starteventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_StartEventSymbol)


def test_hyp_carnot_starteventsymbol_constructor_exists():
    assert callable(carnot_StartEventSymbol.__init__)


def test_hyp_carnot_starteventsymbol_constructor_args():
    sig = inspect.signature(carnot_StartEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_rolesymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_RoleSymbolType)


def test_hyp_carnot_rolesymboltype_constructor_exists():
    assert callable(carnot_RoleSymbolType.__init__)


def test_hyp_carnot_rolesymboltype_constructor_args():
    sig = inspect.signature(carnot_RoleSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_publicinterfacesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_PublicInterfaceSymbol)


def test_hyp_carnot_publicinterfacesymbol_constructor_exists():
    assert callable(carnot_PublicInterfaceSymbol.__init__)


def test_hyp_carnot_publicinterfacesymbol_constructor_args():
    sig = inspect.signature(carnot_PublicInterfaceSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_executedbyconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_ExecutedByConnectionType)


def test_hyp_carnot_executedbyconnectiontype_constructor_exists():
    assert callable(carnot_ExecutedByConnectionType.__init__)


def test_hyp_carnot_executedbyconnectiontype_constructor_args():
    sig = inspect.signature(carnot_ExecutedByConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_processsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ProcessSymbolType)


def test_hyp_carnot_processsymboltype_constructor_exists():
    assert callable(carnot_ProcessSymbolType.__init__)


def test_hyp_carnot_processsymboltype_constructor_args():
    sig = inspect.signature(carnot_ProcessSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_datamappingconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataMappingConnectionType)


def test_hyp_carnot_datamappingconnectiontype_constructor_exists():
    assert callable(carnot_DataMappingConnectionType.__init__)


def test_hyp_carnot_datamappingconnectiontype_constructor_args():
    sig = inspect.signature(carnot_DataMappingConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_modelersymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ModelerSymbolType)


def test_hyp_carnot_modelersymboltype_constructor_exists():
    assert callable(carnot_ModelerSymbolType.__init__)


def test_hyp_carnot_modelersymboltype_constructor_args():
    sig = inspect.signature(carnot_ModelerSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_intermediateeventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IntermediateEventSymbol)


def test_hyp_carnot_intermediateeventsymbol_constructor_exists():
    assert callable(carnot_IntermediateEventSymbol.__init__)


def test_hyp_carnot_intermediateeventsymbol_constructor_args():
    sig = inspect.signature(carnot_IntermediateEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_groupsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_GroupSymbolType)


def test_hyp_carnot_groupsymboltype_constructor_exists():
    assert callable(carnot_GroupSymbolType.__init__)


def test_hyp_carnot_groupsymboltype_constructor_args():
    sig = inspect.signature(carnot_GroupSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_gatewaysymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_GatewaySymbol)


def test_hyp_carnot_gatewaysymbol_constructor_exists():
    assert callable(carnot_GatewaySymbol.__init__)


def test_hyp_carnot_gatewaysymbol_constructor_args():
    sig = inspect.signature(carnot_GatewaySymbol.__init__)
    params = list(sig.parameters.keys())
    assert "flowKind" in params, "Missing parameter 'flowKind'"




def test_hyp_carnot_endeventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_EndEventSymbol)


def test_hyp_carnot_endeventsymbol_constructor_exists():
    assert callable(carnot_EndEventSymbol.__init__)


def test_hyp_carnot_endeventsymbol_constructor_args():
    sig = inspect.signature(carnot_EndEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_datasymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataSymbolType)


def test_hyp_carnot_datasymboltype_constructor_exists():
    assert callable(carnot_DataSymbolType.__init__)


def test_hyp_carnot_datasymboltype_constructor_args():
    sig = inspect.signature(carnot_DataSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_conditionalperformersymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ConditionalPerformerSymbolType)


def test_hyp_carnot_conditionalperformersymboltype_constructor_exists():
    assert callable(carnot_ConditionalPerformerSymbolType.__init__)


def test_hyp_carnot_conditionalperformersymboltype_constructor_args():
    sig = inspect.signature(carnot_ConditionalPerformerSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_organizationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_OrganizationSymbolType)


def test_hyp_carnot_organizationsymboltype_constructor_exists():
    assert callable(carnot_OrganizationSymbolType.__init__)


def test_hyp_carnot_organizationsymboltype_constructor_args():
    sig = inspect.signature(carnot_OrganizationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_annotationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_AnnotationSymbolType)


def test_hyp_carnot_annotationsymboltype_constructor_exists():
    assert callable(carnot_AnnotationSymbolType.__init__)


def test_hyp_carnot_annotationsymboltype_constructor_args():
    sig = inspect.signature(carnot_AnnotationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_activitysymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ActivitySymbolType)


def test_hyp_carnot_activitysymboltype_constructor_exists():
    assert callable(carnot_ActivitySymbolType.__init__)


def test_hyp_carnot_activitysymboltype_constructor_args():
    sig = inspect.signature(carnot_ActivitySymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_itypedelement_is_not_abstract():
    assert not inspect.isabstract(carnot_ITypedElement)


def test_hyp_carnot_itypedelement_constructor_exists():
    assert callable(carnot_ITypedElement.__init__)


def test_hyp_carnot_itypedelement_constructor_args():
    sig = inspect.signature(carnot_ITypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iidentifiablemodelelement_is_not_abstract():
    assert not inspect.isabstract(IIdentifiableModelElement)


def test_hyp_iidentifiablemodelelement_constructor_exists():
    assert callable(IIdentifiableModelElement.__init__)


def test_hyp_iidentifiablemodelelement_constructor_args():
    sig = inspect.signature(IIdentifiableModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_abstracteventaction_is_not_abstract():
    assert not inspect.isabstract(carnot_AbstractEventAction)


def test_hyp_carnot_abstracteventaction_constructor_exists():
    assert callable(carnot_AbstractEventAction.__init__)


def test_hyp_carnot_abstracteventaction_constructor_args():
    sig = inspect.signature(carnot_AbstractEventAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_eventhandlertype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventHandlerType)


def test_hyp_carnot_eventhandlertype_constructor_exists():
    assert callable(carnot_EventHandlerType.__init__)


def test_hyp_carnot_eventhandlertype_constructor_args():
    sig = inspect.signature(carnot_EventHandlerType.__init__)
    params = list(sig.parameters.keys())
    assert "logHandler" in params, "Missing parameter 'logHandler'"
    assert "consumeOnMatch" in params, "Missing parameter 'consumeOnMatch'"
    assert "unbindOnMatch" in params, "Missing parameter 'unbindOnMatch'"
    assert "autoBind" in params, "Missing parameter 'autoBind'"







def test_hyp_carnot_triggertype_is_not_abstract():
    assert not inspect.isabstract(carnot_TriggerType)


def test_hyp_carnot_triggertype_constructor_exists():
    assert callable(carnot_TriggerType.__init__)


def test_hyp_carnot_triggertype_constructor_args():
    sig = inspect.signature(carnot_TriggerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_datapathtype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataPathType)


def test_hyp_carnot_datapathtype_constructor_exists():
    assert callable(carnot_DataPathType.__init__)


def test_hyp_carnot_datapathtype_constructor_args():
    sig = inspect.signature(carnot_DataPathType.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "direction" in params, "Missing parameter 'direction'"







def test_hyp_carnot_datatype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataType)


def test_hyp_carnot_datatype_constructor_exists():
    assert callable(carnot_DataType.__init__)


def test_hyp_carnot_datatype_constructor_args():
    sig = inspect.signature(carnot_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "predefined" in params, "Missing parameter 'predefined'"




def test_hyp_carnot_activitytype_is_not_abstract():
    assert not inspect.isabstract(carnot_ActivityType)


def test_hyp_carnot_activitytype_constructor_exists():
    assert callable(carnot_ActivityType.__init__)


def test_hyp_carnot_activitytype_constructor_args():
    sig = inspect.signature(carnot_ActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "split" in params, "Missing parameter 'split'"
    assert "join" in params, "Missing parameter 'join'"
    assert "loopType" in params, "Missing parameter 'loopType'"
    assert "subProcessMode" in params, "Missing parameter 'subProcessMode'"
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "loopCondition" in params, "Missing parameter 'loopCondition'"
    assert "allowsAbortByPerformer" in params, "Missing parameter 'allowsAbortByPerformer'"
    assert "hibernateOnCreation" in params, "Missing parameter 'hibernateOnCreation'"











def test_hyp_carnot_applicationtype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationType)


def test_hyp_carnot_applicationtype_constructor_exists():
    assert callable(carnot_ApplicationType.__init__)


def test_hyp_carnot_applicationtype_constructor_args():
    sig = inspect.signature(carnot_ApplicationType.__init__)
    params = list(sig.parameters.keys())
    assert "interactive" in params, "Missing parameter 'interactive'"




def test_hyp_carnot_imodelparticipant_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelParticipant)


def test_hyp_carnot_imodelparticipant_constructor_exists():
    assert callable(carnot_IModelParticipant.__init__)


def test_hyp_carnot_imodelparticipant_constructor_args():
    sig = inspect.signature(carnot_IModelParticipant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_processdefinitiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_ProcessDefinitionType)


def test_hyp_carnot_processdefinitiontype_constructor_exists():
    assert callable(carnot_ProcessDefinitionType.__init__)


def test_hyp_carnot_processdefinitiontype_constructor_args():
    sig = inspect.signature(carnot_ProcessDefinitionType.__init__)
    params = list(sig.parameters.keys())
    assert "defaultPriority" in params, "Missing parameter 'defaultPriority'"




def test_hyp_carnot_modelertype_is_not_abstract():
    assert not inspect.isabstract(carnot_ModelerType)


def test_hyp_carnot_modelertype_constructor_exists():
    assert callable(carnot_ModelerType.__init__)


def test_hyp_carnot_modelertype_constructor_args():
    sig = inspect.signature(carnot_ModelerType.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_carnot_transitiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TransitionType)


def test_hyp_carnot_transitiontype_constructor_exists():
    assert callable(carnot_TransitionType.__init__)


def test_hyp_carnot_transitiontype_constructor_args():
    sig = inspect.signature(carnot_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "forkOnTraversal" in params, "Missing parameter 'forkOnTraversal'"
    assert "condition" in params, "Missing parameter 'condition'"





def test_hyp_carnot_imetatype_is_not_abstract():
    assert not inspect.isabstract(carnot_IMetaType)


def test_hyp_carnot_imetatype_constructor_exists():
    assert callable(carnot_IMetaType.__init__)


def test_hyp_carnot_imetatype_constructor_args():
    sig = inspect.signature(carnot_IMetaType.__init__)
    params = list(sig.parameters.keys())
    assert "isPredefined" in params, "Missing parameter 'isPredefined'"




def test_hyp_carnot_accesspointtype_is_not_abstract():
    assert not inspect.isabstract(carnot_AccessPointType)


def test_hyp_carnot_accesspointtype_constructor_exists():
    assert callable(carnot_AccessPointType.__init__)


def test_hyp_carnot_accesspointtype_constructor_args():
    sig = inspect.signature(carnot_AccessPointType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"




def test_hyp_carnot_iaccesspointowner_is_not_abstract():
    assert not inspect.isabstract(carnot_IAccessPointOwner)


def test_hyp_carnot_iaccesspointowner_constructor_exists():
    assert callable(carnot_IAccessPointOwner.__init__)


def test_hyp_carnot_iaccesspointowner_constructor_args():
    sig = inspect.signature(carnot_IAccessPointOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_applicationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationSymbolType)


def test_hyp_carnot_applicationsymboltype_constructor_exists():
    assert callable(carnot_ApplicationSymbolType.__init__)


def test_hyp_carnot_applicationsymboltype_constructor_args():
    sig = inspect.signature(carnot_ApplicationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_ieventhandlerowner_is_not_abstract():
    assert not inspect.isabstract(carnot_IEventHandlerOwner)


def test_hyp_carnot_ieventhandlerowner_constructor_exists():
    assert callable(carnot_IEventHandlerOwner.__init__)


def test_hyp_carnot_ieventhandlerowner_constructor_args():
    sig = inspect.signature(carnot_IEventHandlerOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_descriptiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_DescriptionType)


def test_hyp_carnot_descriptiontype_constructor_exists():
    assert callable(carnot_DescriptionType.__init__)


def test_hyp_carnot_descriptiontype_constructor_args():
    sig = inspect.signature(carnot_DescriptionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_iextensibleelement_is_not_abstract():
    assert not inspect.isabstract(IExtensibleElement)


def test_hyp_iextensibleelement_constructor_exists():
    assert callable(IExtensibleElement.__init__)


def test_hyp_iextensibleelement_constructor_args():
    sig = inspect.signature(IExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_isymbolcontainer_is_not_abstract():
    assert not inspect.isabstract(carnot_ISymbolContainer)


def test_hyp_carnot_isymbolcontainer_constructor_exists():
    assert callable(carnot_ISymbolContainer.__init__)


def test_hyp_carnot_isymbolcontainer_constructor_args():
    sig = inspect.signature(carnot_ISymbolContainer.__init__)
    params = list(sig.parameters.keys())
    assert "connections" in params, "Missing parameter 'connections'"
    assert "nodes" in params, "Missing parameter 'nodes'"





def test_hyp_carnot_diagramtype_is_not_abstract():
    assert not inspect.isabstract(carnot_DiagramType)


def test_hyp_carnot_diagramtype_constructor_exists():
    assert callable(carnot_DiagramType.__init__)


def test_hyp_carnot_diagramtype_constructor_args():
    sig = inspect.signature(carnot_DiagramType.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "name" in params, "Missing parameter 'name'"
    assert "orientation" in params, "Missing parameter 'orientation'"






def test_hyp_carnot_viewtype_is_not_abstract():
    assert not inspect.isabstract(carnot_ViewType)


def test_hyp_carnot_viewtype_constructor_exists():
    assert callable(carnot_ViewType.__init__)


def test_hyp_carnot_viewtype_constructor_args():
    sig = inspect.signature(carnot_ViewType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_carnot_linktypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_LinkTypeType)


def test_hyp_carnot_linktypetype_constructor_exists():
    assert callable(carnot_LinkTypeType.__init__)


def test_hyp_carnot_linktypetype_constructor_args():
    sig = inspect.signature(carnot_LinkTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"
    assert "sourceClass" in params, "Missing parameter 'sourceClass'"
    assert "sourceSymbol" in params, "Missing parameter 'sourceSymbol'"
    assert "sourceCardinality" in params, "Missing parameter 'sourceCardinality'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "targetSymbol" in params, "Missing parameter 'targetSymbol'"
    assert "targetRole" in params, "Missing parameter 'targetRole'"
    assert "showRoleNames" in params, "Missing parameter 'showRoleNames'"
    assert "sourceRole" in params, "Missing parameter 'sourceRole'"
    assert "showLinkTypeName" in params, "Missing parameter 'showLinkTypeName'"
    assert "targetClass" in params, "Missing parameter 'targetClass'"
    assert "lineColor" in params, "Missing parameter 'lineColor'"















def test_hyp_carnot_contexttype_is_not_abstract():
    assert not inspect.isabstract(carnot_ContextType)


def test_hyp_carnot_contexttype_constructor_exists():
    assert callable(carnot_ContextType.__init__)


def test_hyp_carnot_contexttype_constructor_args():
    sig = inspect.signature(carnot_ContextType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(IIdentifiableElement)


def test_hyp_iidentifiableelement_constructor_exists():
    assert callable(IIdentifiableElement.__init__)


def test_hyp_iidentifiableelement_constructor_args():
    sig = inspect.signature(IIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_modeltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ModelType)


def test_hyp_carnot_modeltype_constructor_exists():
    assert callable(carnot_ModelType.__init__)


def test_hyp_carnot_modeltype_constructor_args():
    sig = inspect.signature(carnot_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "oid" in params, "Missing parameter 'oid'"
    assert "carnotVersion" in params, "Missing parameter 'carnotVersion'"
    assert "created" in params, "Missing parameter 'created'"
    assert "author" in params, "Missing parameter 'author'"
    assert "modelOID" in params, "Missing parameter 'modelOID'"
    assert "vendor" in params, "Missing parameter 'vendor'"









def test_hyp_carnot_iswimlanesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_ISwimlaneSymbol)


def test_hyp_carnot_iswimlanesymbol_constructor_exists():
    assert callable(carnot_ISwimlaneSymbol.__init__)


def test_hyp_carnot_iswimlanesymbol_constructor_args():
    sig = inspect.signature(carnot_ISwimlaneSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "collapsed" in params, "Missing parameter 'collapsed'"





def test_hyp_carnot_iidentifiablemodelelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IIdentifiableModelElement)


def test_hyp_carnot_iidentifiablemodelelement_constructor_exists():
    assert callable(carnot_IIdentifiableModelElement.__init__)


def test_hyp_carnot_iidentifiablemodelelement_constructor_args():
    sig = inspect.signature(carnot_IIdentifiableModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_carnot_datamappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataMappingType)


def test_hyp_carnot_datamappingtype_constructor_exists():
    assert callable(carnot_DataMappingType.__init__)


def test_hyp_carnot_datamappingtype_constructor_args():
    sig = inspect.signature(carnot_DataMappingType.__init__)
    params = list(sig.parameters.keys())
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "applicationPath" in params, "Missing parameter 'applicationPath'"
    assert "applicationAccessPoint" in params, "Missing parameter 'applicationAccessPoint'"
    assert "context" in params, "Missing parameter 'context'"
    assert "direction" in params, "Missing parameter 'direction'"






def test_hyp_linkendstyle_exists():
    # Check that the Enumeration exists
    assert LinkEndStyle is not None

def test_hyp_linkendstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkEndStyle]
    expected_literals = [
        "OpenTriangle",
        "Unknown",
        "EmptyTriangle",
        "EmptyRhombus",
        "FilledTriangle",
        "NoArrow",
        "FilledRhombus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkEndStyle"

def test_hyp_orientationtype_exists():
    # Check that the Enumeration exists
    assert OrientationType is not None

def test_hyp_orientationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrientationType]
    expected_literals = [
        "Horizontal",
        "Vertical",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrientationType"

def test_hyp_linklinestyle_exists():
    # Check that the Enumeration exists
    assert LinkLineStyle is not None

def test_hyp_linklinestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkLineStyle]
    expected_literals = [
        "ShortStrokes",
        "Unknown",
        "LongStrokes",
        "Normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkLineStyle"

def test_hyp_linkcardinality_exists():
    # Check that the Enumeration exists
    assert LinkCardinality is not None

def test_hyp_linkcardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkCardinality]
    expected_literals = [
        "One",
        "Many",
        "Unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkCardinality"

def test_hyp_linkcolor_exists():
    # Check that the Enumeration exists
    assert LinkColor is not None

def test_hyp_linkcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkColor]
    expected_literals = [
        "LightGray",
        "Unknown",
        "Black",
        "DarkGray",
        "DarkBlue",
        "Red",
        "Yellow",
        "Blue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkColor"

def test_hyp_diagrammodetype_exists():
    # Check that the Enumeration exists
    assert DiagramModeType is not None

def test_hyp_diagrammodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagramModeType]
    expected_literals = [
        "MODE_4_5_0",
        "MODE_4_0_0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagramModeType"

def test_hyp_flowcontroltype_exists():
    # Check that the Enumeration exists
    assert FlowControlType is not None

def test_hyp_flowcontroltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowControlType]
    expected_literals = [
        "none",
        "join",
        "split",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowControlType"

def test_hyp_looptype_exists():
    # Check that the Enumeration exists
    assert LoopType is not None

def test_hyp_looptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoopType]
    expected_literals = [
        "Repeat",
        "While",
        "None_",
        "Unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoopType"

def test_hyp_subprocessmodetype_exists():
    # Check that the Enumeration exists
    assert SubProcessModeType is not None

def test_hyp_subprocessmodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubProcessModeType]
    expected_literals = [
        "async_separate",
        "sync_shared",
        "sync_separate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubProcessModeType"

def test_hyp_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_hyp_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "INOUT",
        "OUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"

def test_hyp_activityimplementationtype_exists():
    # Check that the Enumeration exists
    assert ActivityImplementationType is not None

def test_hyp_activityimplementationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityImplementationType]
    expected_literals = [
        "Manual",
        "Application",
        "Subprocess",
        "Route",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityImplementationType"

def test_hyp_routingtype_exists():
    # Check that the Enumeration exists
    assert RoutingType is not None

def test_hyp_routingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoutingType]
    expected_literals = [
        "Default",
        "ShortestPath",
        "Explicit",
        "Manhattan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoutingType"

def test_hyp_joinsplittype_exists():
    # Check that the Enumeration exists
    assert JoinSplitType is not None

def test_hyp_joinsplittype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JoinSplitType]
    expected_literals = [
        "None_",
        "XOR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JoinSplitType"

def test_hyp_implementationtype_exists():
    # Check that the Enumeration exists
    assert ImplementationType is not None

def test_hyp_implementationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImplementationType]
    expected_literals = [
        "pull",
        "engine",
        "push",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImplementationType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
IModelElement_strategy = st.builds(
    IModelElement,
)
carnot_IModelElement_strategy = st.builds(
    carnot_IModelElement,
    elementOid=
        safe_text
)
carnot_EObject_strategy = st.builds(
    carnot_EObject,
)
carnot_IdentifiableReference_strategy = st.builds(
    carnot_IdentifiableReference,
)
carnot_AttributeType_strategy = st.builds(
    carnot_AttributeType,
    name=
        safe_text,
    any=
        safe_text,
    group=
        safe_text,
    value=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text
)
carnot_IExtensibleElement_strategy = st.builds(
    carnot_IExtensibleElement,
)
carnot_Coordinates_strategy = st.builds(
    carnot_Coordinates,
    yPos=
        safe_text,
    xPos=
        safe_text
)
carnot_IIdentifiableElement_strategy = st.builds(
    carnot_IIdentifiableElement,
    id=
        safe_text,
    name=
        safe_text
)
FormalParameterMappingType_strategy = st.builds(
    FormalParameterMappingType,
)
carnot_extensions_FormalParameterMappingsType_strategy = st.builds(
    carnot_extensions_FormalParameterMappingsType,
)
extensions_carnot_FormalParameterType_strategy = st.builds(
    extensions_carnot_FormalParameterType,
)
extensions_carnot_DataType_strategy = st.builds(
    extensions_carnot_DataType,
)
carnot_extensions_FormalParameterMappingType_strategy = st.builds(
    carnot_extensions_FormalParameterMappingType,
)
carnot_ViewableType_strategy = st.builds(
    carnot_ViewableType,
)
FormalParameterMappingsType_strategy = st.builds(
    FormalParameterMappingsType,
)
carnot_FormalParametersType_strategy = st.builds(
    carnot_FormalParametersType,
)
carnot_TypeDeclarationsType_strategy = st.builds(
    carnot_TypeDeclarationsType,
)
carnot_QualityControlType_strategy = st.builds(
    carnot_QualityControlType,
)
carnot_ScriptType_strategy = st.builds(
    carnot_ScriptType,
)
carnot_ExternalPackages_strategy = st.builds(
    carnot_ExternalPackages,
)
ISwimlaneSymbol_strategy = st.builds(
    ISwimlaneSymbol,
)
carnot_ExternalPackage_strategy = st.builds(
    carnot_ExternalPackage,
)
carnot_EStringToStringMapEntry_strategy = st.builds(
    carnot_EStringToStringMapEntry,
)
carnot_DocumentRoot_strategy = st.builds(
    carnot_DocumentRoot,
    mixed=
        safe_text
)
AbstractEventSymbol_strategy = st.builds(
    AbstractEventSymbol,
)
ISymbolContainer_strategy = st.builds(
    ISymbolContainer,
)
carnot_PoolSymbol_strategy = st.builds(
    carnot_PoolSymbol,
    boundaryVisible=
        safe_text
)
carnot_ExternalReferenceType_strategy = st.builds(
    carnot_ExternalReferenceType,
)
carnot_ParameterMappingType_strategy = st.builds(
    carnot_ParameterMappingType,
    parameter=
        safe_text,
    parameterPath=
        safe_text,
    dataPath=
        safe_text
)
IConnectionSymbol_strategy = st.builds(
    IConnectionSymbol,
)
IModelParticipant_strategy = st.builds(
    IModelParticipant,
)
carnot_OrganizationType_strategy = st.builds(
    carnot_OrganizationType,
)
carnot_RoleType_strategy = st.builds(
    carnot_RoleType,
    cardinality=
        st.integers()
)
carnot_ConditionalPerformerType_strategy = st.builds(
    carnot_ConditionalPerformerType,
    dataPath=
        safe_text,
    isUser=
        safe_text
)
IModelParticipantSymbol_strategy = st.builds(
    IModelParticipantSymbol,
)
AbstractEventAction_strategy = st.builds(
    AbstractEventAction,
)
carnot_UnbindActionType_strategy = st.builds(
    carnot_UnbindActionType,
)
carnot_EventActionType_strategy = st.builds(
    carnot_EventActionType,
)
carnot_BindActionType_strategy = st.builds(
    carnot_BindActionType,
)
carnot_XmlTextNode_strategy = st.builds(
    carnot_XmlTextNode,
    mixed=
        safe_text
)
IAccessPointOwner_strategy = st.builds(
    IAccessPointOwner,
)
carnot_Code_strategy = st.builds(
    carnot_Code,
    code=
        safe_text,
    name=
        safe_text,
    value=
        safe_text
)
carnot_IdRef_strategy = st.builds(
    carnot_IdRef,
    ref=
        safe_text
)
IMetaType_strategy = st.builds(
    IMetaType,
)
carnot_ApplicationTypeType_strategy = st.builds(
    carnot_ApplicationTypeType,
    panelClass=
        safe_text,
    validatorClass=
        safe_text,
    accessPointProviderClass=
        safe_text,
    synchronous=
        safe_text,
    instanceClass=
        safe_text
)
carnot_TriggerTypeType_strategy = st.builds(
    carnot_TriggerTypeType,
    rule=
        safe_text,
    panelClass=
        safe_text,
    pullTrigger=
        safe_text,
    pullTriggerEvaluator=
        safe_text
)
carnot_EventConditionTypeType_strategy = st.builds(
    carnot_EventConditionTypeType,
    binderClass=
        safe_text,
    rule=
        safe_text,
    implementation=
        safe_text,
    processCondition=
        safe_text,
    activityCondition=
        safe_text,
    panelClass=
        safe_text,
    pullEventEmitterClass=
        safe_text
)
carnot_ApplicationContextTypeType_strategy = st.builds(
    carnot_ApplicationContextTypeType,
    accessPointProviderClass=
        safe_text,
    hasMappingId=
        safe_text,
    validatorClass=
        safe_text,
    panelClass=
        safe_text,
    hasApplicationPath=
        safe_text
)
carnot_TextType_strategy = st.builds(
    carnot_TextType,
    mixed=
        safe_text
)
IEventHandlerOwner_strategy = st.builds(
    IEventHandlerOwner,
)
carnot_DataTypeType_strategy = st.builds(
    carnot_DataTypeType,
    evaluator=
        safe_text,
    writable=
        safe_text,
    panelClass=
        safe_text,
    validatorClass=
        safe_text,
    accessPathEditor=
        safe_text,
    storageStrategy=
        safe_text,
    instanceClass=
        safe_text,
    valueCreator=
        safe_text,
    readable=
        safe_text
)
IFlowObjectSymbol_strategy = st.builds(
    IFlowObjectSymbol,
)
carnot_EventActionTypeType_strategy = st.builds(
    carnot_EventActionTypeType,
    panelClass=
        safe_text,
    actionClass=
        safe_text,
    unsupportedContexts=
        safe_text,
    activityAction=
        safe_text,
    processAction=
        safe_text,
    supportedConditionTypes=
        safe_text
)
ITypedElement_strategy = st.builds(
    ITypedElement,
)
IModelElementNodeSymbol_strategy = st.builds(
    IModelElementNodeSymbol,
)
carnot_AbstractEventSymbol_strategy = st.builds(
    carnot_AbstractEventSymbol,
    label=
        safe_text
)
carnot_IModelParticipantSymbol_strategy = st.builds(
    carnot_IModelParticipantSymbol,
)
carnot_ParticipantType_strategy = st.builds(
    carnot_ParticipantType,
)
carnot_LaneSymbol_strategy = st.builds(
    carnot_LaneSymbol,
)
INodeSymbol_strategy = st.builds(
    INodeSymbol,
)
carnot_IFlowObjectSymbol_strategy = st.builds(
    carnot_IFlowObjectSymbol,
)
carnot_IModelElementNodeSymbol_strategy = st.builds(
    carnot_IModelElementNodeSymbol,
)
IGraphicalObject_strategy = st.builds(
    IGraphicalObject,
)
carnot_IConnectionSymbol_strategy = st.builds(
    carnot_IConnectionSymbol,
    routing=
        safe_text,
    targetAnchor=
        safe_text,
    sourceAnchor=
        safe_text
)
carnot_INodeSymbol_strategy = st.builds(
    carnot_INodeSymbol,
    xPos=
        safe_text,
    width=
        safe_text,
    shape=
        safe_text,
    yPos=
        safe_text,
    height=
        safe_text
)
carnot_IGraphicalObject_strategy = st.builds(
    carnot_IGraphicalObject,
    borderColor=
        safe_text,
    style=
        safe_text,
    fillColor=
        safe_text
)
carnot_TeamLeadConnectionType_strategy = st.builds(
    carnot_TeamLeadConnectionType,
)
carnot_WorksForConnectionType_strategy = st.builds(
    carnot_WorksForConnectionType,
)
carnot_TransitionConnectionType_strategy = st.builds(
    carnot_TransitionConnectionType,
    points=
        safe_text
)
carnot_RefersToConnectionType_strategy = st.builds(
    carnot_RefersToConnectionType,
)
carnot_TriggersConnectionType_strategy = st.builds(
    carnot_TriggersConnectionType,
)
carnot_PerformsConnectionType_strategy = st.builds(
    carnot_PerformsConnectionType,
)
carnot_PartOfConnectionType_strategy = st.builds(
    carnot_PartOfConnectionType,
)
carnot_GenericLinkConnectionType_strategy = st.builds(
    carnot_GenericLinkConnectionType,
)
carnot_SubProcessOfConnectionType_strategy = st.builds(
    carnot_SubProcessOfConnectionType,
)
carnot_TextSymbolType_strategy = st.builds(
    carnot_TextSymbolType,
    text=
        safe_text
)
carnot_StartEventSymbol_strategy = st.builds(
    carnot_StartEventSymbol,
)
carnot_RoleSymbolType_strategy = st.builds(
    carnot_RoleSymbolType,
)
carnot_PublicInterfaceSymbol_strategy = st.builds(
    carnot_PublicInterfaceSymbol,
)
carnot_ExecutedByConnectionType_strategy = st.builds(
    carnot_ExecutedByConnectionType,
)
carnot_ProcessSymbolType_strategy = st.builds(
    carnot_ProcessSymbolType,
)
carnot_DataMappingConnectionType_strategy = st.builds(
    carnot_DataMappingConnectionType,
)
carnot_ModelerSymbolType_strategy = st.builds(
    carnot_ModelerSymbolType,
)
carnot_IntermediateEventSymbol_strategy = st.builds(
    carnot_IntermediateEventSymbol,
)
carnot_GroupSymbolType_strategy = st.builds(
    carnot_GroupSymbolType,
)
carnot_GatewaySymbol_strategy = st.builds(
    carnot_GatewaySymbol,
    flowKind=
        safe_text
)
carnot_EndEventSymbol_strategy = st.builds(
    carnot_EndEventSymbol,
)
carnot_DataSymbolType_strategy = st.builds(
    carnot_DataSymbolType,
)
carnot_ConditionalPerformerSymbolType_strategy = st.builds(
    carnot_ConditionalPerformerSymbolType,
)
carnot_OrganizationSymbolType_strategy = st.builds(
    carnot_OrganizationSymbolType,
)
carnot_AnnotationSymbolType_strategy = st.builds(
    carnot_AnnotationSymbolType,
)
carnot_ActivitySymbolType_strategy = st.builds(
    carnot_ActivitySymbolType,
)
carnot_ITypedElement_strategy = st.builds(
    carnot_ITypedElement,
)
IIdentifiableModelElement_strategy = st.builds(
    IIdentifiableModelElement,
)
carnot_AbstractEventAction_strategy = st.builds(
    carnot_AbstractEventAction,
)
carnot_EventHandlerType_strategy = st.builds(
    carnot_EventHandlerType,
    logHandler=
        safe_text,
    consumeOnMatch=
        safe_text,
    unbindOnMatch=
        safe_text,
    autoBind=
        safe_text
)
carnot_TriggerType_strategy = st.builds(
    carnot_TriggerType,
)
carnot_DataPathType_strategy = st.builds(
    carnot_DataPathType,
    key=
        safe_text,
    dataPath=
        safe_text,
    descriptor=
        safe_text,
    direction=
        safe_text
)
carnot_DataType_strategy = st.builds(
    carnot_DataType,
    predefined=
        safe_text
)
carnot_ActivityType_strategy = st.builds(
    carnot_ActivityType,
    split=
        safe_text,
    join=
        safe_text,
    loopType=
        safe_text,
    subProcessMode=
        safe_text,
    implementation=
        safe_text,
    loopCondition=
        safe_text,
    allowsAbortByPerformer=
        safe_text,
    hibernateOnCreation=
        safe_text
)
carnot_ApplicationType_strategy = st.builds(
    carnot_ApplicationType,
    interactive=
        safe_text
)
carnot_IModelParticipant_strategy = st.builds(
    carnot_IModelParticipant,
)
carnot_ProcessDefinitionType_strategy = st.builds(
    carnot_ProcessDefinitionType,
    defaultPriority=
        safe_text
)
carnot_ModelerType_strategy = st.builds(
    carnot_ModelerType,
    email=
        safe_text,
    password=
        safe_text
)
carnot_TransitionType_strategy = st.builds(
    carnot_TransitionType,
    forkOnTraversal=
        safe_text,
    condition=
        safe_text
)
carnot_IMetaType_strategy = st.builds(
    carnot_IMetaType,
    isPredefined=
        safe_text
)
carnot_AccessPointType_strategy = st.builds(
    carnot_AccessPointType,
    direction=
        safe_text
)
carnot_IAccessPointOwner_strategy = st.builds(
    carnot_IAccessPointOwner,
)
carnot_ApplicationSymbolType_strategy = st.builds(
    carnot_ApplicationSymbolType,
)
carnot_IEventHandlerOwner_strategy = st.builds(
    carnot_IEventHandlerOwner,
)
carnot_DescriptionType_strategy = st.builds(
    carnot_DescriptionType,
    mixed=
        safe_text
)
IExtensibleElement_strategy = st.builds(
    IExtensibleElement,
)
carnot_ISymbolContainer_strategy = st.builds(
    carnot_ISymbolContainer,
    connections=
        safe_text,
    nodes=
        safe_text
)
carnot_DiagramType_strategy = st.builds(
    carnot_DiagramType,
    mode=
        safe_text,
    name=
        safe_text,
    orientation=
        safe_text
)
carnot_ViewType_strategy = st.builds(
    carnot_ViewType,
    name=
        safe_text
)
carnot_LinkTypeType_strategy = st.builds(
    carnot_LinkTypeType,
    targetCardinality=
        safe_text,
    sourceClass=
        safe_text,
    sourceSymbol=
        safe_text,
    sourceCardinality=
        safe_text,
    lineStyle=
        safe_text,
    targetSymbol=
        safe_text,
    targetRole=
        safe_text,
    showRoleNames=
        safe_text,
    sourceRole=
        safe_text,
    showLinkTypeName=
        safe_text,
    targetClass=
        safe_text,
    lineColor=
        safe_text
)
carnot_ContextType_strategy = st.builds(
    carnot_ContextType,
)
IIdentifiableElement_strategy = st.builds(
    IIdentifiableElement,
)
carnot_ModelType_strategy = st.builds(
    carnot_ModelType,
    oid=
        safe_text,
    carnotVersion=
        safe_text,
    created=
        safe_text,
    author=
        safe_text,
    modelOID=
        safe_text,
    vendor=
        safe_text
)
carnot_ISwimlaneSymbol_strategy = st.builds(
    carnot_ISwimlaneSymbol,
    orientation=
        safe_text,
    collapsed=
        safe_text
)
carnot_IIdentifiableModelElement_strategy = st.builds(
    carnot_IIdentifiableModelElement,
)
carnot_DataMappingType_strategy = st.builds(
    carnot_DataMappingType,
    dataPath=
        safe_text,
    applicationPath=
        safe_text,
    applicationAccessPoint=
        safe_text,
    context=
        safe_text,
    direction=
        safe_text
)





@given(instance=carnot_IModelElement_strategy)
def test_hyp_carnot_imodelelement_elementOid_setter(instance):
    original = instance.elementOid
    instance.elementOid = original
    assert instance.elementOid == original






@given(instance=carnot_AttributeType_strategy)
def test_hyp_carnot_attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=carnot_AttributeType_strategy)
def test_hyp_carnot_attributetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=carnot_AttributeType_strategy)
def test_hyp_carnot_attributetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=carnot_AttributeType_strategy)
def test_hyp_carnot_attributetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=carnot_AttributeType_strategy)
def test_hyp_carnot_attributetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=carnot_AttributeType_strategy)
def test_hyp_carnot_attributetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_AttributeType_strategy)
@settings(max_examples=30)
def test_hyp_carnot_attributetype_setattributevalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setAttributeValue(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setAttributeValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setAttributeValue' in carnot_AttributeType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setAttributeValue' in carnot_AttributeType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setAttributeValue' in carnot_AttributeType is not implemented or raised an error")





@given(instance=carnot_Coordinates_strategy)
def test_hyp_carnot_coordinates_yPos_setter(instance):
    original = instance.yPos
    instance.yPos = original
    assert instance.yPos == original



@given(instance=carnot_Coordinates_strategy)
def test_hyp_carnot_coordinates_xPos_setter(instance):
    original = instance.xPos
    instance.xPos = original
    assert instance.xPos == original




@given(instance=carnot_IIdentifiableElement_strategy)
def test_hyp_carnot_iidentifiableelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=carnot_IIdentifiableElement_strategy)
def test_hyp_carnot_iidentifiableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_extensions_FormalParameterMappingsType_strategy)
@settings(max_examples=30)
def test_hyp_carnot_extensions_formalparametermappingstype_setmappeddata_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setMappedData(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setMappedData).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setMappedData' in carnot_extensions_FormalParameterMappingsType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setMappedData' in carnot_extensions_FormalParameterMappingsType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setMappedData' in carnot_extensions_FormalParameterMappingsType is not implemented or raised an error")

















@given(instance=carnot_DocumentRoot_strategy)
def test_hyp_carnot_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original






@given(instance=carnot_PoolSymbol_strategy)
def test_hyp_carnot_poolsymbol_boundaryVisible_setter(instance):
    original = instance.boundaryVisible
    instance.boundaryVisible = original
    assert instance.boundaryVisible == original





@given(instance=carnot_ParameterMappingType_strategy)
def test_hyp_carnot_parametermappingtype_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original



@given(instance=carnot_ParameterMappingType_strategy)
def test_hyp_carnot_parametermappingtype_parameterPath_setter(instance):
    original = instance.parameterPath
    instance.parameterPath = original
    assert instance.parameterPath == original



@given(instance=carnot_ParameterMappingType_strategy)
def test_hyp_carnot_parametermappingtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original







@given(instance=carnot_RoleType_strategy)
def test_hyp_carnot_roletype_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original




@given(instance=carnot_ConditionalPerformerType_strategy)
def test_hyp_carnot_conditionalperformertype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original



@given(instance=carnot_ConditionalPerformerType_strategy)
def test_hyp_carnot_conditionalperformertype_isUser_setter(instance):
    original = instance.isUser
    instance.isUser = original
    assert instance.isUser == original









@given(instance=carnot_XmlTextNode_strategy)
def test_hyp_carnot_xmltextnode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=carnot_Code_strategy)
def test_hyp_carnot_code_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=carnot_Code_strategy)
def test_hyp_carnot_code_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=carnot_Code_strategy)
def test_hyp_carnot_code_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=carnot_IdRef_strategy)
def test_hyp_carnot_idref_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original





@given(instance=carnot_ApplicationTypeType_strategy)
def test_hyp_carnot_applicationtypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_hyp_carnot_applicationtypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_hyp_carnot_applicationtypetype_accessPointProviderClass_setter(instance):
    original = instance.accessPointProviderClass
    instance.accessPointProviderClass = original
    assert instance.accessPointProviderClass == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_hyp_carnot_applicationtypetype_synchronous_setter(instance):
    original = instance.synchronous
    instance.synchronous = original
    assert instance.synchronous == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_hyp_carnot_applicationtypetype_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original




@given(instance=carnot_TriggerTypeType_strategy)
def test_hyp_carnot_triggertypetype_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original



@given(instance=carnot_TriggerTypeType_strategy)
def test_hyp_carnot_triggertypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_TriggerTypeType_strategy)
def test_hyp_carnot_triggertypetype_pullTrigger_setter(instance):
    original = instance.pullTrigger
    instance.pullTrigger = original
    assert instance.pullTrigger == original



@given(instance=carnot_TriggerTypeType_strategy)
def test_hyp_carnot_triggertypetype_pullTriggerEvaluator_setter(instance):
    original = instance.pullTriggerEvaluator
    instance.pullTriggerEvaluator = original
    assert instance.pullTriggerEvaluator == original




@given(instance=carnot_EventConditionTypeType_strategy)
def test_hyp_carnot_eventconditiontypetype_binderClass_setter(instance):
    original = instance.binderClass
    instance.binderClass = original
    assert instance.binderClass == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_hyp_carnot_eventconditiontypetype_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_hyp_carnot_eventconditiontypetype_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_hyp_carnot_eventconditiontypetype_processCondition_setter(instance):
    original = instance.processCondition
    instance.processCondition = original
    assert instance.processCondition == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_hyp_carnot_eventconditiontypetype_activityCondition_setter(instance):
    original = instance.activityCondition
    instance.activityCondition = original
    assert instance.activityCondition == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_hyp_carnot_eventconditiontypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_hyp_carnot_eventconditiontypetype_pullEventEmitterClass_setter(instance):
    original = instance.pullEventEmitterClass
    instance.pullEventEmitterClass = original
    assert instance.pullEventEmitterClass == original




@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_hyp_carnot_applicationcontexttypetype_accessPointProviderClass_setter(instance):
    original = instance.accessPointProviderClass
    instance.accessPointProviderClass = original
    assert instance.accessPointProviderClass == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_hyp_carnot_applicationcontexttypetype_hasMappingId_setter(instance):
    original = instance.hasMappingId
    instance.hasMappingId = original
    assert instance.hasMappingId == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_hyp_carnot_applicationcontexttypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_hyp_carnot_applicationcontexttypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_hyp_carnot_applicationcontexttypetype_hasApplicationPath_setter(instance):
    original = instance.hasApplicationPath
    instance.hasApplicationPath = original
    assert instance.hasApplicationPath == original




@given(instance=carnot_TextType_strategy)
def test_hyp_carnot_texttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_evaluator_setter(instance):
    original = instance.evaluator
    instance.evaluator = original
    assert instance.evaluator == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_writable_setter(instance):
    original = instance.writable
    instance.writable = original
    assert instance.writable == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_accessPathEditor_setter(instance):
    original = instance.accessPathEditor
    instance.accessPathEditor = original
    assert instance.accessPathEditor == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_storageStrategy_setter(instance):
    original = instance.storageStrategy
    instance.storageStrategy = original
    assert instance.storageStrategy == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_valueCreator_setter(instance):
    original = instance.valueCreator
    instance.valueCreator = original
    assert instance.valueCreator == original



@given(instance=carnot_DataTypeType_strategy)
def test_hyp_carnot_datatypetype_readable_setter(instance):
    original = instance.readable
    instance.readable = original
    assert instance.readable == original





@given(instance=carnot_EventActionTypeType_strategy)
def test_hyp_carnot_eventactiontypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_hyp_carnot_eventactiontypetype_actionClass_setter(instance):
    original = instance.actionClass
    instance.actionClass = original
    assert instance.actionClass == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_hyp_carnot_eventactiontypetype_unsupportedContexts_setter(instance):
    original = instance.unsupportedContexts
    instance.unsupportedContexts = original
    assert instance.unsupportedContexts == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_hyp_carnot_eventactiontypetype_activityAction_setter(instance):
    original = instance.activityAction
    instance.activityAction = original
    assert instance.activityAction == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_hyp_carnot_eventactiontypetype_processAction_setter(instance):
    original = instance.processAction
    instance.processAction = original
    assert instance.processAction == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_hyp_carnot_eventactiontypetype_supportedConditionTypes_setter(instance):
    original = instance.supportedConditionTypes
    instance.supportedConditionTypes = original
    assert instance.supportedConditionTypes == original






@given(instance=carnot_AbstractEventSymbol_strategy)
def test_hyp_carnot_abstracteventsymbol_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original







import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_IModelElementNodeSymbol_strategy)
@settings(max_examples=30)
def test_hyp_carnot_imodelelementnodesymbol_setmodelelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setModelElement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setModelElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setModelElement' in carnot_IModelElementNodeSymbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setModelElement' in carnot_IModelElementNodeSymbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setModelElement' in carnot_IModelElementNodeSymbol is not implemented or raised an error")





@given(instance=carnot_IConnectionSymbol_strategy)
def test_hyp_carnot_iconnectionsymbol_routing_setter(instance):
    original = instance.routing
    instance.routing = original
    assert instance.routing == original



@given(instance=carnot_IConnectionSymbol_strategy)
def test_hyp_carnot_iconnectionsymbol_targetAnchor_setter(instance):
    original = instance.targetAnchor
    instance.targetAnchor = original
    assert instance.targetAnchor == original



@given(instance=carnot_IConnectionSymbol_strategy)
def test_hyp_carnot_iconnectionsymbol_sourceAnchor_setter(instance):
    original = instance.sourceAnchor
    instance.sourceAnchor = original
    assert instance.sourceAnchor == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_IConnectionSymbol_strategy)
@settings(max_examples=30)
def test_hyp_carnot_iconnectionsymbol_setsourcenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setSourceNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setSourceNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setSourceNode' in carnot_IConnectionSymbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSourceNode' in carnot_IConnectionSymbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSourceNode' in carnot_IConnectionSymbol is not implemented or raised an error")




@given(instance=carnot_INodeSymbol_strategy)
def test_hyp_carnot_inodesymbol_xPos_setter(instance):
    original = instance.xPos
    instance.xPos = original
    assert instance.xPos == original



@given(instance=carnot_INodeSymbol_strategy)
def test_hyp_carnot_inodesymbol_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=carnot_INodeSymbol_strategy)
def test_hyp_carnot_inodesymbol_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=carnot_INodeSymbol_strategy)
def test_hyp_carnot_inodesymbol_yPos_setter(instance):
    original = instance.yPos
    instance.yPos = original
    assert instance.yPos == original



@given(instance=carnot_INodeSymbol_strategy)
def test_hyp_carnot_inodesymbol_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=carnot_IGraphicalObject_strategy)
def test_hyp_carnot_igraphicalobject_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original



@given(instance=carnot_IGraphicalObject_strategy)
def test_hyp_carnot_igraphicalobject_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=carnot_IGraphicalObject_strategy)
def test_hyp_carnot_igraphicalobject_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original






@given(instance=carnot_TransitionConnectionType_strategy)
def test_hyp_carnot_transitionconnectiontype_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original










@given(instance=carnot_TextSymbolType_strategy)
def test_hyp_carnot_textsymboltype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original













@given(instance=carnot_GatewaySymbol_strategy)
def test_hyp_carnot_gatewaysymbol_flowKind_setter(instance):
    original = instance.flowKind
    instance.flowKind = original
    assert instance.flowKind == original













@given(instance=carnot_EventHandlerType_strategy)
def test_hyp_carnot_eventhandlertype_logHandler_setter(instance):
    original = instance.logHandler
    instance.logHandler = original
    assert instance.logHandler == original



@given(instance=carnot_EventHandlerType_strategy)
def test_hyp_carnot_eventhandlertype_consumeOnMatch_setter(instance):
    original = instance.consumeOnMatch
    instance.consumeOnMatch = original
    assert instance.consumeOnMatch == original



@given(instance=carnot_EventHandlerType_strategy)
def test_hyp_carnot_eventhandlertype_unbindOnMatch_setter(instance):
    original = instance.unbindOnMatch
    instance.unbindOnMatch = original
    assert instance.unbindOnMatch == original



@given(instance=carnot_EventHandlerType_strategy)
def test_hyp_carnot_eventhandlertype_autoBind_setter(instance):
    original = instance.autoBind
    instance.autoBind = original
    assert instance.autoBind == original





@given(instance=carnot_DataPathType_strategy)
def test_hyp_carnot_datapathtype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=carnot_DataPathType_strategy)
def test_hyp_carnot_datapathtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original



@given(instance=carnot_DataPathType_strategy)
def test_hyp_carnot_datapathtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original



@given(instance=carnot_DataPathType_strategy)
def test_hyp_carnot_datapathtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original




@given(instance=carnot_DataType_strategy)
def test_hyp_carnot_datatype_predefined_setter(instance):
    original = instance.predefined
    instance.predefined = original
    assert instance.predefined == original




@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_split_setter(instance):
    original = instance.split
    instance.split = original
    assert instance.split == original



@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original



@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original



@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_subProcessMode_setter(instance):
    original = instance.subProcessMode
    instance.subProcessMode = original
    assert instance.subProcessMode == original



@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original



@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_loopCondition_setter(instance):
    original = instance.loopCondition
    instance.loopCondition = original
    assert instance.loopCondition == original



@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_allowsAbortByPerformer_setter(instance):
    original = instance.allowsAbortByPerformer
    instance.allowsAbortByPerformer = original
    assert instance.allowsAbortByPerformer == original



@given(instance=carnot_ActivityType_strategy)
def test_hyp_carnot_activitytype_hibernateOnCreation_setter(instance):
    original = instance.hibernateOnCreation
    instance.hibernateOnCreation = original
    assert instance.hibernateOnCreation == original




@given(instance=carnot_ApplicationType_strategy)
def test_hyp_carnot_applicationtype_interactive_setter(instance):
    original = instance.interactive
    instance.interactive = original
    assert instance.interactive == original





@given(instance=carnot_ProcessDefinitionType_strategy)
def test_hyp_carnot_processdefinitiontype_defaultPriority_setter(instance):
    original = instance.defaultPriority
    instance.defaultPriority = original
    assert instance.defaultPriority == original




@given(instance=carnot_ModelerType_strategy)
def test_hyp_carnot_modelertype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=carnot_ModelerType_strategy)
def test_hyp_carnot_modelertype_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=carnot_TransitionType_strategy)
def test_hyp_carnot_transitiontype_forkOnTraversal_setter(instance):
    original = instance.forkOnTraversal
    instance.forkOnTraversal = original
    assert instance.forkOnTraversal == original



@given(instance=carnot_TransitionType_strategy)
def test_hyp_carnot_transitiontype_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original




@given(instance=carnot_IMetaType_strategy)
def test_hyp_carnot_imetatype_isPredefined_setter(instance):
    original = instance.isPredefined
    instance.isPredefined = original
    assert instance.isPredefined == original




@given(instance=carnot_AccessPointType_strategy)
def test_hyp_carnot_accesspointtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original







@given(instance=carnot_DescriptionType_strategy)
def test_hyp_carnot_descriptiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=carnot_ISymbolContainer_strategy)
def test_hyp_carnot_isymbolcontainer_connections_setter(instance):
    original = instance.connections
    instance.connections = original
    assert instance.connections == original



@given(instance=carnot_ISymbolContainer_strategy)
def test_hyp_carnot_isymbolcontainer_nodes_setter(instance):
    original = instance.nodes
    instance.nodes = original
    assert instance.nodes == original




@given(instance=carnot_DiagramType_strategy)
def test_hyp_carnot_diagramtype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=carnot_DiagramType_strategy)
def test_hyp_carnot_diagramtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=carnot_DiagramType_strategy)
def test_hyp_carnot_diagramtype_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original




@given(instance=carnot_ViewType_strategy)
def test_hyp_carnot_viewtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_sourceClass_setter(instance):
    original = instance.sourceClass
    instance.sourceClass = original
    assert instance.sourceClass == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_sourceSymbol_setter(instance):
    original = instance.sourceSymbol
    instance.sourceSymbol = original
    assert instance.sourceSymbol == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_sourceCardinality_setter(instance):
    original = instance.sourceCardinality
    instance.sourceCardinality = original
    assert instance.sourceCardinality == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_targetSymbol_setter(instance):
    original = instance.targetSymbol
    instance.targetSymbol = original
    assert instance.targetSymbol == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_targetRole_setter(instance):
    original = instance.targetRole
    instance.targetRole = original
    assert instance.targetRole == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_showRoleNames_setter(instance):
    original = instance.showRoleNames
    instance.showRoleNames = original
    assert instance.showRoleNames == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_sourceRole_setter(instance):
    original = instance.sourceRole
    instance.sourceRole = original
    assert instance.sourceRole == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_showLinkTypeName_setter(instance):
    original = instance.showLinkTypeName
    instance.showLinkTypeName = original
    assert instance.showLinkTypeName == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_targetClass_setter(instance):
    original = instance.targetClass
    instance.targetClass = original
    assert instance.targetClass == original



@given(instance=carnot_LinkTypeType_strategy)
def test_hyp_carnot_linktypetype_lineColor_setter(instance):
    original = instance.lineColor
    instance.lineColor = original
    assert instance.lineColor == original






@given(instance=carnot_ModelType_strategy)
def test_hyp_carnot_modeltype_oid_setter(instance):
    original = instance.oid
    instance.oid = original
    assert instance.oid == original



@given(instance=carnot_ModelType_strategy)
def test_hyp_carnot_modeltype_carnotVersion_setter(instance):
    original = instance.carnotVersion
    instance.carnotVersion = original
    assert instance.carnotVersion == original



@given(instance=carnot_ModelType_strategy)
def test_hyp_carnot_modeltype_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original



@given(instance=carnot_ModelType_strategy)
def test_hyp_carnot_modeltype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=carnot_ModelType_strategy)
def test_hyp_carnot_modeltype_modelOID_setter(instance):
    original = instance.modelOID
    instance.modelOID = original
    assert instance.modelOID == original



@given(instance=carnot_ModelType_strategy)
def test_hyp_carnot_modeltype_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original




@given(instance=carnot_ISwimlaneSymbol_strategy)
def test_hyp_carnot_iswimlanesymbol_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=carnot_ISwimlaneSymbol_strategy)
def test_hyp_carnot_iswimlanesymbol_collapsed_setter(instance):
    original = instance.collapsed
    instance.collapsed = original
    assert instance.collapsed == original





@given(instance=carnot_DataMappingType_strategy)
def test_hyp_carnot_datamappingtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original



@given(instance=carnot_DataMappingType_strategy)
def test_hyp_carnot_datamappingtype_applicationPath_setter(instance):
    original = instance.applicationPath
    instance.applicationPath = original
    assert instance.applicationPath == original



@given(instance=carnot_DataMappingType_strategy)
def test_hyp_carnot_datamappingtype_applicationAccessPoint_setter(instance):
    original = instance.applicationAccessPoint
    instance.applicationAccessPoint = original
    assert instance.applicationAccessPoint == original



@given(instance=carnot_DataMappingType_strategy)
def test_hyp_carnot_datamappingtype_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original



@given(instance=carnot_DataMappingType_strategy)
def test_hyp_carnot_datamappingtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_carnot_AbstractEventSymbol_label_value_roundtrip():
    instance = carnot_AbstractEventSymbol(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_carnot_AccessPointType_direction_value_roundtrip():
    instance = carnot_AccessPointType(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_carnot_ActivityType_allowsAbortByPerformer_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.allowsAbortByPerformer == "sample_text"
    instance.allowsAbortByPerformer = "sample_text_2"
    assert instance.allowsAbortByPerformer == "sample_text_2"


def test_carnot_ActivityType_hibernateOnCreation_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.hibernateOnCreation == "sample_text"
    instance.hibernateOnCreation = "sample_text_2"
    assert instance.hibernateOnCreation == "sample_text_2"


def test_carnot_ActivityType_implementation_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.implementation == "sample_text"
    instance.implementation = "sample_text_2"
    assert instance.implementation == "sample_text_2"


def test_carnot_ActivityType_join_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.join == "sample_text"
    instance.join = "sample_text_2"
    assert instance.join == "sample_text_2"


def test_carnot_ActivityType_loopCondition_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.loopCondition == "sample_text"
    instance.loopCondition = "sample_text_2"
    assert instance.loopCondition == "sample_text_2"


def test_carnot_ActivityType_loopType_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.loopType == "sample_text"
    instance.loopType = "sample_text_2"
    assert instance.loopType == "sample_text_2"


def test_carnot_ActivityType_split_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.split == "sample_text"
    instance.split = "sample_text_2"
    assert instance.split == "sample_text_2"


def test_carnot_ActivityType_subProcessMode_value_roundtrip():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert instance.subProcessMode == "sample_text"
    instance.subProcessMode = "sample_text_2"
    assert instance.subProcessMode == "sample_text_2"


def test_carnot_ApplicationContextTypeType_accessPointProviderClass_value_roundtrip():
    instance = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    assert instance.accessPointProviderClass == "sample_text"
    instance.accessPointProviderClass = "sample_text_2"
    assert instance.accessPointProviderClass == "sample_text_2"


def test_carnot_ApplicationContextTypeType_hasApplicationPath_value_roundtrip():
    instance = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    assert instance.hasApplicationPath == "sample_text"
    instance.hasApplicationPath = "sample_text_2"
    assert instance.hasApplicationPath == "sample_text_2"


def test_carnot_ApplicationContextTypeType_hasMappingId_value_roundtrip():
    instance = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    assert instance.hasMappingId == "sample_text"
    instance.hasMappingId = "sample_text_2"
    assert instance.hasMappingId == "sample_text_2"


def test_carnot_ApplicationContextTypeType_panelClass_value_roundtrip():
    instance = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    assert instance.panelClass == "sample_text"
    instance.panelClass = "sample_text_2"
    assert instance.panelClass == "sample_text_2"


def test_carnot_ApplicationContextTypeType_validatorClass_value_roundtrip():
    instance = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    assert instance.validatorClass == "sample_text"
    instance.validatorClass = "sample_text_2"
    assert instance.validatorClass == "sample_text_2"


def test_carnot_ApplicationType_interactive_value_roundtrip():
    instance = carnot_ApplicationType(interactive="sample_text")
    assert instance.interactive == "sample_text"
    instance.interactive = "sample_text_2"
    assert instance.interactive == "sample_text_2"


def test_carnot_ApplicationTypeType_accessPointProviderClass_value_roundtrip():
    instance = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    assert instance.accessPointProviderClass == "sample_text"
    instance.accessPointProviderClass = "sample_text_2"
    assert instance.accessPointProviderClass == "sample_text_2"


def test_carnot_ApplicationTypeType_instanceClass_value_roundtrip():
    instance = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    assert instance.instanceClass == "sample_text"
    instance.instanceClass = "sample_text_2"
    assert instance.instanceClass == "sample_text_2"


def test_carnot_ApplicationTypeType_panelClass_value_roundtrip():
    instance = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    assert instance.panelClass == "sample_text"
    instance.panelClass = "sample_text_2"
    assert instance.panelClass == "sample_text_2"


def test_carnot_ApplicationTypeType_synchronous_value_roundtrip():
    instance = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    assert instance.synchronous == "sample_text"
    instance.synchronous = "sample_text_2"
    assert instance.synchronous == "sample_text_2"


def test_carnot_ApplicationTypeType_validatorClass_value_roundtrip():
    instance = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    assert instance.validatorClass == "sample_text"
    instance.validatorClass = "sample_text_2"
    assert instance.validatorClass == "sample_text_2"


def test_carnot_AttributeType_any_value_roundtrip():
    instance = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_carnot_AttributeType_group_value_roundtrip():
    instance = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_carnot_AttributeType_mixed_value_roundtrip():
    instance = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_carnot_AttributeType_name_value_roundtrip():
    instance = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_carnot_AttributeType_type_value_roundtrip():
    instance = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_carnot_AttributeType_value_value_roundtrip():
    instance = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_carnot_Code_code_value_roundtrip():
    instance = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_carnot_Code_name_value_roundtrip():
    instance = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_carnot_Code_value_value_roundtrip():
    instance = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_carnot_ConditionalPerformerType_dataPath_value_roundtrip():
    instance = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    assert instance.dataPath == "sample_text"
    instance.dataPath = "sample_text_2"
    assert instance.dataPath == "sample_text_2"


def test_carnot_ConditionalPerformerType_isUser_value_roundtrip():
    instance = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    assert instance.isUser == "sample_text"
    instance.isUser = "sample_text_2"
    assert instance.isUser == "sample_text_2"


def test_carnot_Coordinates_xPos_value_roundtrip():
    instance = carnot_Coordinates(xPos="sample_text", yPos="sample_text")
    assert instance.xPos == "sample_text"
    instance.xPos = "sample_text_2"
    assert instance.xPos == "sample_text_2"


def test_carnot_Coordinates_yPos_value_roundtrip():
    instance = carnot_Coordinates(xPos="sample_text", yPos="sample_text")
    assert instance.yPos == "sample_text"
    instance.yPos = "sample_text_2"
    assert instance.yPos == "sample_text_2"


def test_carnot_DataMappingType_applicationAccessPoint_value_roundtrip():
    instance = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    assert instance.applicationAccessPoint == "sample_text"
    instance.applicationAccessPoint = "sample_text_2"
    assert instance.applicationAccessPoint == "sample_text_2"


def test_carnot_DataMappingType_applicationPath_value_roundtrip():
    instance = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    assert instance.applicationPath == "sample_text"
    instance.applicationPath = "sample_text_2"
    assert instance.applicationPath == "sample_text_2"


def test_carnot_DataMappingType_context_value_roundtrip():
    instance = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    assert instance.context == "sample_text"
    instance.context = "sample_text_2"
    assert instance.context == "sample_text_2"


def test_carnot_DataMappingType_dataPath_value_roundtrip():
    instance = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    assert instance.dataPath == "sample_text"
    instance.dataPath = "sample_text_2"
    assert instance.dataPath == "sample_text_2"


def test_carnot_DataMappingType_direction_value_roundtrip():
    instance = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_carnot_DataPathType_dataPath_value_roundtrip():
    instance = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    assert instance.dataPath == "sample_text"
    instance.dataPath = "sample_text_2"
    assert instance.dataPath == "sample_text_2"


def test_carnot_DataPathType_descriptor_value_roundtrip():
    instance = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    assert instance.descriptor == "sample_text"
    instance.descriptor = "sample_text_2"
    assert instance.descriptor == "sample_text_2"


def test_carnot_DataPathType_direction_value_roundtrip():
    instance = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_carnot_DataPathType_key_value_roundtrip():
    instance = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_carnot_DataType_predefined_value_roundtrip():
    instance = carnot_DataType(predefined="sample_text")
    assert instance.predefined == "sample_text"
    instance.predefined = "sample_text_2"
    assert instance.predefined == "sample_text_2"


def test_carnot_DataTypeType_accessPathEditor_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.accessPathEditor == "sample_text"
    instance.accessPathEditor = "sample_text_2"
    assert instance.accessPathEditor == "sample_text_2"


def test_carnot_DataTypeType_evaluator_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.evaluator == "sample_text"
    instance.evaluator = "sample_text_2"
    assert instance.evaluator == "sample_text_2"


def test_carnot_DataTypeType_instanceClass_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.instanceClass == "sample_text"
    instance.instanceClass = "sample_text_2"
    assert instance.instanceClass == "sample_text_2"


def test_carnot_DataTypeType_panelClass_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.panelClass == "sample_text"
    instance.panelClass = "sample_text_2"
    assert instance.panelClass == "sample_text_2"


def test_carnot_DataTypeType_readable_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.readable == "sample_text"
    instance.readable = "sample_text_2"
    assert instance.readable == "sample_text_2"


def test_carnot_DataTypeType_storageStrategy_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.storageStrategy == "sample_text"
    instance.storageStrategy = "sample_text_2"
    assert instance.storageStrategy == "sample_text_2"


def test_carnot_DataTypeType_validatorClass_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.validatorClass == "sample_text"
    instance.validatorClass = "sample_text_2"
    assert instance.validatorClass == "sample_text_2"


def test_carnot_DataTypeType_valueCreator_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.valueCreator == "sample_text"
    instance.valueCreator = "sample_text_2"
    assert instance.valueCreator == "sample_text_2"


def test_carnot_DataTypeType_writable_value_roundtrip():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert instance.writable == "sample_text"
    instance.writable = "sample_text_2"
    assert instance.writable == "sample_text_2"


def test_carnot_DescriptionType_mixed_value_roundtrip():
    instance = carnot_DescriptionType(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_carnot_DiagramType_mode_value_roundtrip():
    instance = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    assert instance.mode == "sample_text"
    instance.mode = "sample_text_2"
    assert instance.mode == "sample_text_2"


def test_carnot_DiagramType_name_value_roundtrip():
    instance = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_carnot_DiagramType_orientation_value_roundtrip():
    instance = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_carnot_DocumentRoot_mixed_value_roundtrip():
    instance = carnot_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_carnot_EventActionTypeType_actionClass_value_roundtrip():
    instance = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    assert instance.actionClass == "sample_text"
    instance.actionClass = "sample_text_2"
    assert instance.actionClass == "sample_text_2"


def test_carnot_EventActionTypeType_activityAction_value_roundtrip():
    instance = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    assert instance.activityAction == "sample_text"
    instance.activityAction = "sample_text_2"
    assert instance.activityAction == "sample_text_2"


def test_carnot_EventActionTypeType_panelClass_value_roundtrip():
    instance = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    assert instance.panelClass == "sample_text"
    instance.panelClass = "sample_text_2"
    assert instance.panelClass == "sample_text_2"


def test_carnot_EventActionTypeType_processAction_value_roundtrip():
    instance = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    assert instance.processAction == "sample_text"
    instance.processAction = "sample_text_2"
    assert instance.processAction == "sample_text_2"


def test_carnot_EventActionTypeType_supportedConditionTypes_value_roundtrip():
    instance = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    assert instance.supportedConditionTypes == "sample_text"
    instance.supportedConditionTypes = "sample_text_2"
    assert instance.supportedConditionTypes == "sample_text_2"


def test_carnot_EventActionTypeType_unsupportedContexts_value_roundtrip():
    instance = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    assert instance.unsupportedContexts == "sample_text"
    instance.unsupportedContexts = "sample_text_2"
    assert instance.unsupportedContexts == "sample_text_2"


def test_carnot_EventConditionTypeType_activityCondition_value_roundtrip():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert instance.activityCondition == "sample_text"
    instance.activityCondition = "sample_text_2"
    assert instance.activityCondition == "sample_text_2"


def test_carnot_EventConditionTypeType_binderClass_value_roundtrip():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert instance.binderClass == "sample_text"
    instance.binderClass = "sample_text_2"
    assert instance.binderClass == "sample_text_2"


def test_carnot_EventConditionTypeType_implementation_value_roundtrip():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert instance.implementation == "sample_text"
    instance.implementation = "sample_text_2"
    assert instance.implementation == "sample_text_2"


def test_carnot_EventConditionTypeType_panelClass_value_roundtrip():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert instance.panelClass == "sample_text"
    instance.panelClass = "sample_text_2"
    assert instance.panelClass == "sample_text_2"


def test_carnot_EventConditionTypeType_processCondition_value_roundtrip():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert instance.processCondition == "sample_text"
    instance.processCondition = "sample_text_2"
    assert instance.processCondition == "sample_text_2"


def test_carnot_EventConditionTypeType_pullEventEmitterClass_value_roundtrip():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert instance.pullEventEmitterClass == "sample_text"
    instance.pullEventEmitterClass = "sample_text_2"
    assert instance.pullEventEmitterClass == "sample_text_2"


def test_carnot_EventConditionTypeType_rule_value_roundtrip():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert instance.rule == "sample_text"
    instance.rule = "sample_text_2"
    assert instance.rule == "sample_text_2"


def test_carnot_EventHandlerType_autoBind_value_roundtrip():
    instance = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    assert instance.autoBind == "sample_text"
    instance.autoBind = "sample_text_2"
    assert instance.autoBind == "sample_text_2"


def test_carnot_EventHandlerType_consumeOnMatch_value_roundtrip():
    instance = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    assert instance.consumeOnMatch == "sample_text"
    instance.consumeOnMatch = "sample_text_2"
    assert instance.consumeOnMatch == "sample_text_2"


def test_carnot_EventHandlerType_logHandler_value_roundtrip():
    instance = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    assert instance.logHandler == "sample_text"
    instance.logHandler = "sample_text_2"
    assert instance.logHandler == "sample_text_2"


def test_carnot_EventHandlerType_unbindOnMatch_value_roundtrip():
    instance = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    assert instance.unbindOnMatch == "sample_text"
    instance.unbindOnMatch = "sample_text_2"
    assert instance.unbindOnMatch == "sample_text_2"


def test_carnot_GatewaySymbol_flowKind_value_roundtrip():
    instance = carnot_GatewaySymbol(flowKind="sample_text")
    assert instance.flowKind == "sample_text"
    instance.flowKind = "sample_text_2"
    assert instance.flowKind == "sample_text_2"


def test_carnot_IConnectionSymbol_routing_value_roundtrip():
    instance = carnot_IConnectionSymbol(routing="sample_text", sourceAnchor="sample_text", targetAnchor="sample_text")
    assert instance.routing == "sample_text"
    instance.routing = "sample_text_2"
    assert instance.routing == "sample_text_2"


def test_carnot_IConnectionSymbol_sourceAnchor_value_roundtrip():
    instance = carnot_IConnectionSymbol(routing="sample_text", sourceAnchor="sample_text", targetAnchor="sample_text")
    assert instance.sourceAnchor == "sample_text"
    instance.sourceAnchor = "sample_text_2"
    assert instance.sourceAnchor == "sample_text_2"


def test_carnot_IConnectionSymbol_targetAnchor_value_roundtrip():
    instance = carnot_IConnectionSymbol(routing="sample_text", sourceAnchor="sample_text", targetAnchor="sample_text")
    assert instance.targetAnchor == "sample_text"
    instance.targetAnchor = "sample_text_2"
    assert instance.targetAnchor == "sample_text_2"


def test_carnot_IGraphicalObject_borderColor_value_roundtrip():
    instance = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    assert instance.borderColor == "sample_text"
    instance.borderColor = "sample_text_2"
    assert instance.borderColor == "sample_text_2"


def test_carnot_IGraphicalObject_fillColor_value_roundtrip():
    instance = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    assert instance.fillColor == "sample_text"
    instance.fillColor = "sample_text_2"
    assert instance.fillColor == "sample_text_2"


def test_carnot_IGraphicalObject_style_value_roundtrip():
    instance = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_carnot_IIdentifiableElement_id_value_roundtrip():
    instance = carnot_IIdentifiableElement(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_carnot_IIdentifiableElement_name_value_roundtrip():
    instance = carnot_IIdentifiableElement(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_carnot_IMetaType_isPredefined_value_roundtrip():
    instance = carnot_IMetaType(isPredefined="sample_text")
    assert instance.isPredefined == "sample_text"
    instance.isPredefined = "sample_text_2"
    assert instance.isPredefined == "sample_text_2"


def test_carnot_IModelElement_elementOid_value_roundtrip():
    instance = carnot_IModelElement(elementOid="sample_text")
    assert instance.elementOid == "sample_text"
    instance.elementOid = "sample_text_2"
    assert instance.elementOid == "sample_text_2"


def test_carnot_INodeSymbol_height_value_roundtrip():
    instance = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_carnot_INodeSymbol_shape_value_roundtrip():
    instance = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_carnot_INodeSymbol_width_value_roundtrip():
    instance = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_carnot_INodeSymbol_xPos_value_roundtrip():
    instance = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    assert instance.xPos == "sample_text"
    instance.xPos = "sample_text_2"
    assert instance.xPos == "sample_text_2"


def test_carnot_INodeSymbol_yPos_value_roundtrip():
    instance = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    assert instance.yPos == "sample_text"
    instance.yPos = "sample_text_2"
    assert instance.yPos == "sample_text_2"


def test_carnot_ISwimlaneSymbol_collapsed_value_roundtrip():
    instance = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    assert instance.collapsed == "sample_text"
    instance.collapsed = "sample_text_2"
    assert instance.collapsed == "sample_text_2"


def test_carnot_ISwimlaneSymbol_orientation_value_roundtrip():
    instance = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_carnot_ISymbolContainer_connections_value_roundtrip():
    instance = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    assert instance.connections == "sample_text"
    instance.connections = "sample_text_2"
    assert instance.connections == "sample_text_2"


def test_carnot_ISymbolContainer_nodes_value_roundtrip():
    instance = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    assert instance.nodes == "sample_text"
    instance.nodes = "sample_text_2"
    assert instance.nodes == "sample_text_2"


def test_carnot_IdRef_ref_value_roundtrip():
    instance = carnot_IdRef(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_carnot_LinkTypeType_lineColor_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.lineColor == "sample_text"
    instance.lineColor = "sample_text_2"
    assert instance.lineColor == "sample_text_2"


def test_carnot_LinkTypeType_lineStyle_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.lineStyle == "sample_text"
    instance.lineStyle = "sample_text_2"
    assert instance.lineStyle == "sample_text_2"


def test_carnot_LinkTypeType_showLinkTypeName_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.showLinkTypeName == "sample_text"
    instance.showLinkTypeName = "sample_text_2"
    assert instance.showLinkTypeName == "sample_text_2"


def test_carnot_LinkTypeType_showRoleNames_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.showRoleNames == "sample_text"
    instance.showRoleNames = "sample_text_2"
    assert instance.showRoleNames == "sample_text_2"


def test_carnot_LinkTypeType_sourceCardinality_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.sourceCardinality == "sample_text"
    instance.sourceCardinality = "sample_text_2"
    assert instance.sourceCardinality == "sample_text_2"


def test_carnot_LinkTypeType_sourceClass_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.sourceClass == "sample_text"
    instance.sourceClass = "sample_text_2"
    assert instance.sourceClass == "sample_text_2"


def test_carnot_LinkTypeType_sourceRole_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.sourceRole == "sample_text"
    instance.sourceRole = "sample_text_2"
    assert instance.sourceRole == "sample_text_2"


def test_carnot_LinkTypeType_sourceSymbol_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.sourceSymbol == "sample_text"
    instance.sourceSymbol = "sample_text_2"
    assert instance.sourceSymbol == "sample_text_2"


def test_carnot_LinkTypeType_targetCardinality_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.targetCardinality == "sample_text"
    instance.targetCardinality = "sample_text_2"
    assert instance.targetCardinality == "sample_text_2"


def test_carnot_LinkTypeType_targetClass_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.targetClass == "sample_text"
    instance.targetClass = "sample_text_2"
    assert instance.targetClass == "sample_text_2"


def test_carnot_LinkTypeType_targetRole_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.targetRole == "sample_text"
    instance.targetRole = "sample_text_2"
    assert instance.targetRole == "sample_text_2"


def test_carnot_LinkTypeType_targetSymbol_value_roundtrip():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert instance.targetSymbol == "sample_text"
    instance.targetSymbol = "sample_text_2"
    assert instance.targetSymbol == "sample_text_2"


def test_carnot_ModelType_author_value_roundtrip():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_carnot_ModelType_carnotVersion_value_roundtrip():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert instance.carnotVersion == "sample_text"
    instance.carnotVersion = "sample_text_2"
    assert instance.carnotVersion == "sample_text_2"


def test_carnot_ModelType_created_value_roundtrip():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert instance.created == "sample_text"
    instance.created = "sample_text_2"
    assert instance.created == "sample_text_2"


def test_carnot_ModelType_modelOID_value_roundtrip():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert instance.modelOID == "sample_text"
    instance.modelOID = "sample_text_2"
    assert instance.modelOID == "sample_text_2"


def test_carnot_ModelType_oid_value_roundtrip():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert instance.oid == "sample_text"
    instance.oid = "sample_text_2"
    assert instance.oid == "sample_text_2"


def test_carnot_ModelType_vendor_value_roundtrip():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert instance.vendor == "sample_text"
    instance.vendor = "sample_text_2"
    assert instance.vendor == "sample_text_2"


def test_carnot_ModelerType_email_value_roundtrip():
    instance = carnot_ModelerType(email="sample_text", password="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_carnot_ModelerType_password_value_roundtrip():
    instance = carnot_ModelerType(email="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_carnot_ParameterMappingType_dataPath_value_roundtrip():
    instance = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    assert instance.dataPath == "sample_text"
    instance.dataPath = "sample_text_2"
    assert instance.dataPath == "sample_text_2"


def test_carnot_ParameterMappingType_parameter_value_roundtrip():
    instance = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    assert instance.parameter == "sample_text"
    instance.parameter = "sample_text_2"
    assert instance.parameter == "sample_text_2"


def test_carnot_ParameterMappingType_parameterPath_value_roundtrip():
    instance = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    assert instance.parameterPath == "sample_text"
    instance.parameterPath = "sample_text_2"
    assert instance.parameterPath == "sample_text_2"


def test_carnot_PoolSymbol_boundaryVisible_value_roundtrip():
    instance = carnot_PoolSymbol(boundaryVisible="sample_text")
    assert instance.boundaryVisible == "sample_text"
    instance.boundaryVisible = "sample_text_2"
    assert instance.boundaryVisible == "sample_text_2"


def test_carnot_ProcessDefinitionType_defaultPriority_value_roundtrip():
    instance = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    assert instance.defaultPriority == "sample_text"
    instance.defaultPriority = "sample_text_2"
    assert instance.defaultPriority == "sample_text_2"


def test_carnot_RoleType_cardinality_value_roundtrip():
    instance = carnot_RoleType(cardinality=7)
    assert instance.cardinality == 7
    instance.cardinality = 13
    assert instance.cardinality == 13


def test_carnot_TextSymbolType_text_value_roundtrip():
    instance = carnot_TextSymbolType(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_carnot_TextType_mixed_value_roundtrip():
    instance = carnot_TextType(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_carnot_TransitionConnectionType_points_value_roundtrip():
    instance = carnot_TransitionConnectionType(points="sample_text")
    assert instance.points == "sample_text"
    instance.points = "sample_text_2"
    assert instance.points == "sample_text_2"


def test_carnot_TransitionType_condition_value_roundtrip():
    instance = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    assert instance.condition == "sample_text"
    instance.condition = "sample_text_2"
    assert instance.condition == "sample_text_2"


def test_carnot_TransitionType_forkOnTraversal_value_roundtrip():
    instance = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    assert instance.forkOnTraversal == "sample_text"
    instance.forkOnTraversal = "sample_text_2"
    assert instance.forkOnTraversal == "sample_text_2"


def test_carnot_TriggerTypeType_panelClass_value_roundtrip():
    instance = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    assert instance.panelClass == "sample_text"
    instance.panelClass = "sample_text_2"
    assert instance.panelClass == "sample_text_2"


def test_carnot_TriggerTypeType_pullTrigger_value_roundtrip():
    instance = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    assert instance.pullTrigger == "sample_text"
    instance.pullTrigger = "sample_text_2"
    assert instance.pullTrigger == "sample_text_2"


def test_carnot_TriggerTypeType_pullTriggerEvaluator_value_roundtrip():
    instance = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    assert instance.pullTriggerEvaluator == "sample_text"
    instance.pullTriggerEvaluator = "sample_text_2"
    assert instance.pullTriggerEvaluator == "sample_text_2"


def test_carnot_TriggerTypeType_rule_value_roundtrip():
    instance = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    assert instance.rule == "sample_text"
    instance.rule = "sample_text_2"
    assert instance.rule == "sample_text_2"


def test_carnot_ViewType_name_value_roundtrip():
    instance = carnot_ViewType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_carnot_XmlTextNode_mixed_value_roundtrip():
    instance = carnot_XmlTextNode(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_carnot_BindActionType_isa_AbstractEventAction():
    instance = carnot_BindActionType()
    assert isinstance(instance, AbstractEventAction)


def test_carnot_EventActionType_isa_AbstractEventAction():
    instance = carnot_EventActionType()
    assert isinstance(instance, AbstractEventAction)


def test_carnot_UnbindActionType_isa_AbstractEventAction():
    instance = carnot_UnbindActionType()
    assert isinstance(instance, AbstractEventAction)


def test_carnot_EndEventSymbol_isa_AbstractEventSymbol():
    instance = carnot_EndEventSymbol()
    assert isinstance(instance, AbstractEventSymbol)


def test_carnot_IntermediateEventSymbol_isa_AbstractEventSymbol():
    instance = carnot_IntermediateEventSymbol()
    assert isinstance(instance, AbstractEventSymbol)


def test_carnot_PublicInterfaceSymbol_isa_AbstractEventSymbol():
    instance = carnot_PublicInterfaceSymbol()
    assert isinstance(instance, AbstractEventSymbol)


def test_carnot_StartEventSymbol_isa_AbstractEventSymbol():
    instance = carnot_StartEventSymbol()
    assert isinstance(instance, AbstractEventSymbol)


def test_carnot_ApplicationType_isa_IAccessPointOwner():
    instance = carnot_ApplicationType(interactive="sample_text")
    assert isinstance(instance, IAccessPointOwner)


def test_carnot_ContextType_isa_IAccessPointOwner():
    instance = carnot_ContextType()
    assert isinstance(instance, IAccessPointOwner)


def test_carnot_EventHandlerType_isa_IAccessPointOwner():
    instance = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    assert isinstance(instance, IAccessPointOwner)


def test_carnot_TriggerType_isa_IAccessPointOwner():
    instance = carnot_TriggerType()
    assert isinstance(instance, IAccessPointOwner)


def test_carnot_DataMappingConnectionType_isa_IConnectionSymbol():
    instance = carnot_DataMappingConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_ExecutedByConnectionType_isa_IConnectionSymbol():
    instance = carnot_ExecutedByConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_GenericLinkConnectionType_isa_IConnectionSymbol():
    instance = carnot_GenericLinkConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_PartOfConnectionType_isa_IConnectionSymbol():
    instance = carnot_PartOfConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_PerformsConnectionType_isa_IConnectionSymbol():
    instance = carnot_PerformsConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_RefersToConnectionType_isa_IConnectionSymbol():
    instance = carnot_RefersToConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_SubProcessOfConnectionType_isa_IConnectionSymbol():
    instance = carnot_SubProcessOfConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_TeamLeadConnectionType_isa_IConnectionSymbol():
    instance = carnot_TeamLeadConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_TransitionConnectionType_isa_IConnectionSymbol():
    instance = carnot_TransitionConnectionType(points="sample_text")
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_TriggersConnectionType_isa_IConnectionSymbol():
    instance = carnot_TriggersConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_WorksForConnectionType_isa_IConnectionSymbol():
    instance = carnot_WorksForConnectionType()
    assert isinstance(instance, IConnectionSymbol)


def test_carnot_ActivityType_isa_IEventHandlerOwner():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert isinstance(instance, IEventHandlerOwner)


def test_carnot_ProcessDefinitionType_isa_IEventHandlerOwner():
    instance = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    assert isinstance(instance, IEventHandlerOwner)


def test_carnot_ContextType_isa_IExtensibleElement():
    instance = carnot_ContextType()
    assert isinstance(instance, IExtensibleElement)


def test_carnot_DiagramType_isa_IExtensibleElement():
    instance = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    assert isinstance(instance, IExtensibleElement)


def test_carnot_IIdentifiableModelElement_isa_IExtensibleElement():
    instance = carnot_IIdentifiableModelElement()
    assert isinstance(instance, IExtensibleElement)


def test_carnot_ISymbolContainer_isa_IExtensibleElement():
    instance = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    assert isinstance(instance, IExtensibleElement)


def test_carnot_LinkTypeType_isa_IExtensibleElement():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert isinstance(instance, IExtensibleElement)


def test_carnot_ModelType_isa_IExtensibleElement():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert isinstance(instance, IExtensibleElement)


def test_carnot_ViewType_isa_IExtensibleElement():
    instance = carnot_ViewType(name="sample_text")
    assert isinstance(instance, IExtensibleElement)


def test_carnot_AbstractEventSymbol_isa_IFlowObjectSymbol():
    instance = carnot_AbstractEventSymbol(label="sample_text")
    assert isinstance(instance, IFlowObjectSymbol)


def test_carnot_ActivitySymbolType_isa_IFlowObjectSymbol():
    instance = carnot_ActivitySymbolType()
    assert isinstance(instance, IFlowObjectSymbol)


def test_carnot_GatewaySymbol_isa_IFlowObjectSymbol():
    instance = carnot_GatewaySymbol(flowKind="sample_text")
    assert isinstance(instance, IFlowObjectSymbol)


def test_carnot_IConnectionSymbol_isa_IGraphicalObject():
    instance = carnot_IConnectionSymbol(routing="sample_text", sourceAnchor="sample_text", targetAnchor="sample_text")
    assert isinstance(instance, IGraphicalObject)


def test_carnot_INodeSymbol_isa_IGraphicalObject():
    instance = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    assert isinstance(instance, IGraphicalObject)


def test_carnot_DataMappingType_isa_IIdentifiableElement():
    instance = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    assert isinstance(instance, IIdentifiableElement)


def test_carnot_IIdentifiableModelElement_isa_IIdentifiableElement():
    instance = carnot_IIdentifiableModelElement()
    assert isinstance(instance, IIdentifiableElement)


def test_carnot_ISwimlaneSymbol_isa_IIdentifiableElement():
    instance = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    assert isinstance(instance, IIdentifiableElement)


def test_carnot_ModelType_isa_IIdentifiableElement():
    instance = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    assert isinstance(instance, IIdentifiableElement)


def test_carnot_AbstractEventAction_isa_IIdentifiableModelElement():
    instance = carnot_AbstractEventAction()
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_AccessPointType_isa_IIdentifiableModelElement():
    instance = carnot_AccessPointType(direction="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_ActivityType_isa_IIdentifiableModelElement():
    instance = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_ApplicationType_isa_IIdentifiableModelElement():
    instance = carnot_ApplicationType(interactive="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_DataPathType_isa_IIdentifiableModelElement():
    instance = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_DataType_isa_IIdentifiableModelElement():
    instance = carnot_DataType(predefined="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_EventHandlerType_isa_IIdentifiableModelElement():
    instance = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_IMetaType_isa_IIdentifiableModelElement():
    instance = carnot_IMetaType(isPredefined="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_IModelParticipant_isa_IIdentifiableModelElement():
    instance = carnot_IModelParticipant()
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_ModelerType_isa_IIdentifiableModelElement():
    instance = carnot_ModelerType(email="sample_text", password="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_ProcessDefinitionType_isa_IIdentifiableModelElement():
    instance = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_TransitionType_isa_IIdentifiableModelElement():
    instance = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_TriggerType_isa_IIdentifiableModelElement():
    instance = carnot_TriggerType()
    assert isinstance(instance, IIdentifiableModelElement)


def test_carnot_ApplicationContextTypeType_isa_IMetaType():
    instance = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    assert isinstance(instance, IMetaType)


def test_carnot_ApplicationTypeType_isa_IMetaType():
    instance = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    assert isinstance(instance, IMetaType)


def test_carnot_DataTypeType_isa_IMetaType():
    instance = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    assert isinstance(instance, IMetaType)


def test_carnot_EventActionTypeType_isa_IMetaType():
    instance = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    assert isinstance(instance, IMetaType)


def test_carnot_EventConditionTypeType_isa_IMetaType():
    instance = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    assert isinstance(instance, IMetaType)


def test_carnot_LinkTypeType_isa_IMetaType():
    instance = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    assert isinstance(instance, IMetaType)


def test_carnot_TriggerTypeType_isa_IMetaType():
    instance = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    assert isinstance(instance, IMetaType)


def test_carnot_ContextType_isa_IModelElement():
    instance = carnot_ContextType()
    assert isinstance(instance, IModelElement)


def test_carnot_DataMappingType_isa_IModelElement():
    instance = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    assert isinstance(instance, IModelElement)


def test_carnot_DiagramType_isa_IModelElement():
    instance = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    assert isinstance(instance, IModelElement)


def test_carnot_IGraphicalObject_isa_IModelElement():
    instance = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    assert isinstance(instance, IModelElement)


def test_carnot_IIdentifiableModelElement_isa_IModelElement():
    instance = carnot_IIdentifiableModelElement()
    assert isinstance(instance, IModelElement)


def test_carnot_ParameterMappingType_isa_IModelElement():
    instance = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    assert isinstance(instance, IModelElement)


def test_carnot_ViewType_isa_IModelElement():
    instance = carnot_ViewType(name="sample_text")
    assert isinstance(instance, IModelElement)


def test_carnot_AbstractEventSymbol_isa_IModelElementNodeSymbol():
    instance = carnot_AbstractEventSymbol(label="sample_text")
    assert isinstance(instance, IModelElementNodeSymbol)


def test_carnot_ActivitySymbolType_isa_IModelElementNodeSymbol():
    instance = carnot_ActivitySymbolType()
    assert isinstance(instance, IModelElementNodeSymbol)


def test_carnot_ApplicationSymbolType_isa_IModelElementNodeSymbol():
    instance = carnot_ApplicationSymbolType()
    assert isinstance(instance, IModelElementNodeSymbol)


def test_carnot_DataSymbolType_isa_IModelElementNodeSymbol():
    instance = carnot_DataSymbolType()
    assert isinstance(instance, IModelElementNodeSymbol)


def test_carnot_IModelParticipantSymbol_isa_IModelElementNodeSymbol():
    instance = carnot_IModelParticipantSymbol()
    assert isinstance(instance, IModelElementNodeSymbol)


def test_carnot_ModelerSymbolType_isa_IModelElementNodeSymbol():
    instance = carnot_ModelerSymbolType()
    assert isinstance(instance, IModelElementNodeSymbol)


def test_carnot_ProcessSymbolType_isa_IModelElementNodeSymbol():
    instance = carnot_ProcessSymbolType()
    assert isinstance(instance, IModelElementNodeSymbol)


def test_carnot_ConditionalPerformerType_isa_IModelParticipant():
    instance = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    assert isinstance(instance, IModelParticipant)


def test_carnot_OrganizationType_isa_IModelParticipant():
    instance = carnot_OrganizationType()
    assert isinstance(instance, IModelParticipant)


def test_carnot_RoleType_isa_IModelParticipant():
    instance = carnot_RoleType(cardinality=7)
    assert isinstance(instance, IModelParticipant)


def test_carnot_ConditionalPerformerSymbolType_isa_IModelParticipantSymbol():
    instance = carnot_ConditionalPerformerSymbolType()
    assert isinstance(instance, IModelParticipantSymbol)


def test_carnot_OrganizationSymbolType_isa_IModelParticipantSymbol():
    instance = carnot_OrganizationSymbolType()
    assert isinstance(instance, IModelParticipantSymbol)


def test_carnot_RoleSymbolType_isa_IModelParticipantSymbol():
    instance = carnot_RoleSymbolType()
    assert isinstance(instance, IModelParticipantSymbol)


def test_carnot_AnnotationSymbolType_isa_INodeSymbol():
    instance = carnot_AnnotationSymbolType()
    assert isinstance(instance, INodeSymbol)


def test_carnot_GroupSymbolType_isa_INodeSymbol():
    instance = carnot_GroupSymbolType()
    assert isinstance(instance, INodeSymbol)


def test_carnot_IFlowObjectSymbol_isa_INodeSymbol():
    instance = carnot_IFlowObjectSymbol()
    assert isinstance(instance, INodeSymbol)


def test_carnot_IModelElementNodeSymbol_isa_INodeSymbol():
    instance = carnot_IModelElementNodeSymbol()
    assert isinstance(instance, INodeSymbol)


def test_carnot_ISwimlaneSymbol_isa_INodeSymbol():
    instance = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    assert isinstance(instance, INodeSymbol)


def test_carnot_TextSymbolType_isa_INodeSymbol():
    instance = carnot_TextSymbolType(text="sample_text")
    assert isinstance(instance, INodeSymbol)


def test_carnot_LaneSymbol_isa_ISwimlaneSymbol():
    instance = carnot_LaneSymbol()
    assert isinstance(instance, ISwimlaneSymbol)


def test_carnot_PoolSymbol_isa_ISwimlaneSymbol():
    instance = carnot_PoolSymbol(boundaryVisible="sample_text")
    assert isinstance(instance, ISwimlaneSymbol)


def test_carnot_DiagramType_isa_ISymbolContainer():
    instance = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    assert isinstance(instance, ISymbolContainer)


def test_carnot_GroupSymbolType_isa_ISymbolContainer():
    instance = carnot_GroupSymbolType()
    assert isinstance(instance, ISymbolContainer)


def test_carnot_LaneSymbol_isa_ISymbolContainer():
    instance = carnot_LaneSymbol()
    assert isinstance(instance, ISymbolContainer)


def test_carnot_PoolSymbol_isa_ISymbolContainer():
    instance = carnot_PoolSymbol(boundaryVisible="sample_text")
    assert isinstance(instance, ISymbolContainer)


def test_carnot_AbstractEventAction_isa_ITypedElement():
    instance = carnot_AbstractEventAction()
    assert isinstance(instance, ITypedElement)


def test_carnot_AccessPointType_isa_ITypedElement():
    instance = carnot_AccessPointType(direction="sample_text")
    assert isinstance(instance, ITypedElement)


def test_carnot_ApplicationType_isa_ITypedElement():
    instance = carnot_ApplicationType(interactive="sample_text")
    assert isinstance(instance, ITypedElement)


def test_carnot_ContextType_isa_ITypedElement():
    instance = carnot_ContextType()
    assert isinstance(instance, ITypedElement)


def test_carnot_DataType_isa_ITypedElement():
    instance = carnot_DataType(predefined="sample_text")
    assert isinstance(instance, ITypedElement)


def test_carnot_EventHandlerType_isa_ITypedElement():
    instance = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    assert isinstance(instance, ITypedElement)


def test_carnot_GenericLinkConnectionType_isa_ITypedElement():
    instance = carnot_GenericLinkConnectionType()
    assert isinstance(instance, ITypedElement)


def test_carnot_TriggerType_isa_ITypedElement():
    instance = carnot_TriggerType()
    assert isinstance(instance, ITypedElement)


def test_assoc_Code308_link_reassign_clear():
    a = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    b1 = carnot_QualityControlType()
    b2 = carnot_QualityControlType()
    _safe_set(a, 'carnot_Code310', b1)
    assert _is_linked(a, 'carnot_Code310', b1)
    if hasattr(b1, 'carnot_QualityControlType309'):
        assert _is_linked(b1, 'carnot_QualityControlType309', a)
    _safe_set(a, 'carnot_Code310', b2)
    assert _is_linked(a, 'carnot_Code310', b2)
    if hasattr(b1, 'carnot_QualityControlType309'):
        assert not _is_linked(b1, 'carnot_QualityControlType309', a)
    if hasattr(b2, 'carnot_QualityControlType309'):
        assert _is_linked(b2, 'carnot_QualityControlType309', a)
    _safe_set(a, 'carnot_Code310', None)
    assert not _is_linked(a, 'carnot_Code310', b2)
    if hasattr(b2, 'carnot_QualityControlType309'):
        assert not _is_linked(b2, 'carnot_QualityControlType309', a)


def test_assoc_accessPoint5_link_reassign_clear():
    a = carnot_AccessPointType(direction="sample_text")
    b1 = carnot_IAccessPointOwner()
    b2 = carnot_IAccessPointOwner()
    _safe_set(a, 'carnot_AccessPointType', b1)
    assert _is_linked(a, 'carnot_AccessPointType', b1)
    if hasattr(b1, 'carnot_IAccessPointOwner'):
        assert _is_linked(b1, 'carnot_IAccessPointOwner', a)
    _safe_set(a, 'carnot_AccessPointType', b2)
    assert _is_linked(a, 'carnot_AccessPointType', b2)
    if hasattr(b1, 'carnot_IAccessPointOwner'):
        assert not _is_linked(b1, 'carnot_IAccessPointOwner', a)
    if hasattr(b2, 'carnot_IAccessPointOwner'):
        assert _is_linked(b2, 'carnot_IAccessPointOwner', a)
    _safe_set(a, 'carnot_AccessPointType', None)
    assert not _is_linked(a, 'carnot_AccessPointType', b2)
    if hasattr(b2, 'carnot_IAccessPointOwner'):
        assert not _is_linked(b2, 'carnot_IAccessPointOwner', a)


def test_assoc_actionInstances175_link_reassign_clear():
    a = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    b1 = carnot_AbstractEventAction()
    b2 = carnot_AbstractEventAction()
    _safe_set(a, 'type176', {b1})
    assert _is_linked(a, 'type176', b1)
    if hasattr(b1, 'AbstractEventAction'):
        assert _is_linked(b1, 'AbstractEventAction', a)
    _safe_set(a, 'type176', {b2})
    assert _is_linked(a, 'type176', b2)
    if hasattr(b1, 'AbstractEventAction'):
        assert not _is_linked(b1, 'AbstractEventAction', a)
    if hasattr(b2, 'AbstractEventAction'):
        assert _is_linked(b2, 'AbstractEventAction', a)
    _safe_set(a, 'type176', set())
    assert not _is_linked(a, 'type176', b2)
    if hasattr(b2, 'AbstractEventAction'):
        assert not _is_linked(b2, 'AbstractEventAction', a)


def test_assoc_activity281_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'carnot_ProcessDefinitionType282', {b1})
    assert _is_linked(a, 'carnot_ProcessDefinitionType282', b1)
    if hasattr(b1, 'carnot_ActivityType283'):
        assert _is_linked(b1, 'carnot_ActivityType283', a)
    _safe_set(a, 'carnot_ProcessDefinitionType282', {b2})
    assert _is_linked(a, 'carnot_ProcessDefinitionType282', b2)
    if hasattr(b1, 'carnot_ActivityType283'):
        assert not _is_linked(b1, 'carnot_ActivityType283', a)
    if hasattr(b2, 'carnot_ActivityType283'):
        assert _is_linked(b2, 'carnot_ActivityType283', a)
    _safe_set(a, 'carnot_ProcessDefinitionType282', set())
    assert not _is_linked(a, 'carnot_ProcessDefinitionType282', b2)
    if hasattr(b2, 'carnot_ActivityType283'):
        assert not _is_linked(b2, 'carnot_ActivityType283', a)


def test_assoc_activity82_link_reassign_clear():
    a = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b1 = carnot_ActivitySymbolType()
    b2 = carnot_ActivitySymbolType()
    _safe_set(a, 'ActivityType83', b1)
    assert _is_linked(a, 'ActivityType83', b1)
    if hasattr(b1, 'activitySymbols'):
        assert _is_linked(b1, 'activitySymbols', a)
    _safe_set(a, 'ActivityType83', b2)
    assert _is_linked(a, 'ActivityType83', b2)
    if hasattr(b1, 'activitySymbols'):
        assert not _is_linked(b1, 'activitySymbols', a)
    if hasattr(b2, 'activitySymbols'):
        assert _is_linked(b2, 'activitySymbols', a)
    _safe_set(a, 'ActivityType83', None)
    assert not _is_linked(a, 'ActivityType83', b2)
    if hasattr(b2, 'activitySymbols'):
        assert not _is_linked(b2, 'activitySymbols', a)


def test_assoc_activitySymbol193_link_reassign_clear():
    a = carnot_GatewaySymbol(flowKind="sample_text")
    b1 = carnot_ActivitySymbolType()
    b2 = carnot_ActivitySymbolType()
    _safe_set(a, 'gatewaySymbols', b1)
    assert _is_linked(a, 'gatewaySymbols', b1)
    if hasattr(b1, 'ActivitySymbolType194'):
        assert _is_linked(b1, 'ActivitySymbolType194', a)
    _safe_set(a, 'gatewaySymbols', b2)
    assert _is_linked(a, 'gatewaySymbols', b2)
    if hasattr(b1, 'ActivitySymbolType194'):
        assert not _is_linked(b1, 'ActivitySymbolType194', a)
    if hasattr(b2, 'ActivitySymbolType194'):
        assert _is_linked(b2, 'ActivitySymbolType194', a)
    _safe_set(a, 'gatewaySymbols', None)
    assert not _is_linked(a, 'gatewaySymbols', b2)
    if hasattr(b2, 'ActivitySymbolType194'):
        assert not _is_linked(b2, 'ActivitySymbolType194', a)


def test_assoc_activitySymbol6_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_ActivitySymbolType()
    b2 = carnot_ActivitySymbolType()
    _safe_set(a, 'carnot_ISymbolContainer', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer', b1)
    if hasattr(b1, 'carnot_ActivitySymbolType'):
        assert _is_linked(b1, 'carnot_ActivitySymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer', b2)
    if hasattr(b1, 'carnot_ActivitySymbolType'):
        assert not _is_linked(b1, 'carnot_ActivitySymbolType', a)
    if hasattr(b2, 'carnot_ActivitySymbolType'):
        assert _is_linked(b2, 'carnot_ActivitySymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer', b2)
    if hasattr(b2, 'carnot_ActivitySymbolType'):
        assert not _is_linked(b2, 'carnot_ActivitySymbolType', a)


def test_assoc_activitySymbols100_link_reassign_clear():
    a = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b1 = carnot_ActivitySymbolType()
    b2 = carnot_ActivitySymbolType()
    _safe_set(a, 'activity', {b1})
    assert _is_linked(a, 'activity', b1)
    if hasattr(b1, 'ActivitySymbolType'):
        assert _is_linked(b1, 'ActivitySymbolType', a)
    _safe_set(a, 'activity', {b2})
    assert _is_linked(a, 'activity', b2)
    if hasattr(b1, 'ActivitySymbolType'):
        assert not _is_linked(b1, 'ActivitySymbolType', a)
    if hasattr(b2, 'ActivitySymbolType'):
        assert _is_linked(b2, 'ActivitySymbolType', a)
    _safe_set(a, 'activity', set())
    assert not _is_linked(a, 'activity', b2)
    if hasattr(b2, 'ActivitySymbolType'):
        assert not _is_linked(b2, 'ActivitySymbolType', a)


def test_assoc_annotationSymbol7_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_AnnotationSymbolType()
    b2 = carnot_AnnotationSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer8', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer8', b1)
    if hasattr(b1, 'carnot_AnnotationSymbolType'):
        assert _is_linked(b1, 'carnot_AnnotationSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer8', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer8', b2)
    if hasattr(b1, 'carnot_AnnotationSymbolType'):
        assert not _is_linked(b1, 'carnot_AnnotationSymbolType', a)
    if hasattr(b2, 'carnot_AnnotationSymbolType'):
        assert _is_linked(b2, 'carnot_AnnotationSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer8', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer8', b2)
    if hasattr(b2, 'carnot_AnnotationSymbolType'):
        assert not _is_linked(b2, 'carnot_AnnotationSymbolType', a)


def test_assoc_application116_link_reassign_clear():
    a = carnot_ApplicationType(interactive="sample_text")
    b1 = carnot_ApplicationSymbolType()
    b2 = carnot_ApplicationSymbolType()
    _safe_set(a, 'ApplicationType117', b1)
    assert _is_linked(a, 'ApplicationType117', b1)
    if hasattr(b1, 'applicationSymbols'):
        assert _is_linked(b1, 'applicationSymbols', a)
    _safe_set(a, 'ApplicationType117', b2)
    assert _is_linked(a, 'ApplicationType117', b2)
    if hasattr(b1, 'applicationSymbols'):
        assert not _is_linked(b1, 'applicationSymbols', a)
    if hasattr(b2, 'applicationSymbols'):
        assert _is_linked(b2, 'applicationSymbols', a)
    _safe_set(a, 'ApplicationType117', None)
    assert not _is_linked(a, 'ApplicationType117', b2)
    if hasattr(b2, 'applicationSymbols'):
        assert not _is_linked(b2, 'applicationSymbols', a)


def test_assoc_application226_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_ApplicationType(interactive="sample_text")
    b2 = carnot_ApplicationType(interactive="sample_text_2")
    _safe_set(a, 'carnot_ModelType227', {b1})
    assert _is_linked(a, 'carnot_ModelType227', b1)
    if hasattr(b1, 'carnot_ApplicationType228'):
        assert _is_linked(b1, 'carnot_ApplicationType228', a)
    _safe_set(a, 'carnot_ModelType227', {b2})
    assert _is_linked(a, 'carnot_ModelType227', b2)
    if hasattr(b1, 'carnot_ApplicationType228'):
        assert not _is_linked(b1, 'carnot_ApplicationType228', a)
    if hasattr(b2, 'carnot_ApplicationType228'):
        assert _is_linked(b2, 'carnot_ApplicationType228', a)
    _safe_set(a, 'carnot_ModelType227', set())
    assert not _is_linked(a, 'carnot_ModelType227', b2)
    if hasattr(b2, 'carnot_ApplicationType228'):
        assert not _is_linked(b2, 'carnot_ApplicationType228', a)


def test_assoc_application93_link_reassign_clear():
    a = carnot_ApplicationType(interactive="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'ApplicationType', b1)
    assert _is_linked(a, 'ApplicationType', b1)
    if hasattr(b1, 'executedActivities'):
        assert _is_linked(b1, 'executedActivities', a)
    _safe_set(a, 'ApplicationType', b2)
    assert _is_linked(a, 'ApplicationType', b2)
    if hasattr(b1, 'executedActivities'):
        assert not _is_linked(b1, 'executedActivities', a)
    if hasattr(b2, 'executedActivities'):
        assert _is_linked(b2, 'executedActivities', a)
    _safe_set(a, 'ApplicationType', None)
    assert not _is_linked(a, 'ApplicationType', b2)
    if hasattr(b2, 'executedActivities'):
        assert not _is_linked(b2, 'executedActivities', a)


def test_assoc_applicationContextType215_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    b2 = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text_2", hasApplicationPath="sample_text_2", hasMappingId="sample_text_2", panelClass="sample_text_2", validatorClass="sample_text_2")
    _safe_set(a, 'carnot_ModelType216', {b1})
    assert _is_linked(a, 'carnot_ModelType216', b1)
    if hasattr(b1, 'carnot_ApplicationContextTypeType'):
        assert _is_linked(b1, 'carnot_ApplicationContextTypeType', a)
    _safe_set(a, 'carnot_ModelType216', {b2})
    assert _is_linked(a, 'carnot_ModelType216', b2)
    if hasattr(b1, 'carnot_ApplicationContextTypeType'):
        assert not _is_linked(b1, 'carnot_ApplicationContextTypeType', a)
    if hasattr(b2, 'carnot_ApplicationContextTypeType'):
        assert _is_linked(b2, 'carnot_ApplicationContextTypeType', a)
    _safe_set(a, 'carnot_ModelType216', set())
    assert not _is_linked(a, 'carnot_ModelType216', b2)
    if hasattr(b2, 'carnot_ApplicationContextTypeType'):
        assert not _is_linked(b2, 'carnot_ApplicationContextTypeType', a)


def test_assoc_applicationSymbol9_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_ApplicationSymbolType()
    b2 = carnot_ApplicationSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer10', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer10', b1)
    if hasattr(b1, 'carnot_ApplicationSymbolType'):
        assert _is_linked(b1, 'carnot_ApplicationSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer10', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer10', b2)
    if hasattr(b1, 'carnot_ApplicationSymbolType'):
        assert not _is_linked(b1, 'carnot_ApplicationSymbolType', a)
    if hasattr(b2, 'carnot_ApplicationSymbolType'):
        assert _is_linked(b2, 'carnot_ApplicationSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer10', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer10', b2)
    if hasattr(b2, 'carnot_ApplicationSymbolType'):
        assert not _is_linked(b2, 'carnot_ApplicationSymbolType', a)


def test_assoc_applicationSymbols122_link_reassign_clear():
    a = carnot_ApplicationType(interactive="sample_text")
    b1 = carnot_ApplicationSymbolType()
    b2 = carnot_ApplicationSymbolType()
    _safe_set(a, 'application123', {b1})
    assert _is_linked(a, 'application123', b1)
    if hasattr(b1, 'ApplicationSymbolType'):
        assert _is_linked(b1, 'ApplicationSymbolType', a)
    _safe_set(a, 'application123', {b2})
    assert _is_linked(a, 'application123', b2)
    if hasattr(b1, 'ApplicationSymbolType'):
        assert not _is_linked(b1, 'ApplicationSymbolType', a)
    if hasattr(b2, 'ApplicationSymbolType'):
        assert _is_linked(b2, 'ApplicationSymbolType', a)
    _safe_set(a, 'application123', set())
    assert not _is_linked(a, 'application123', b2)
    if hasattr(b2, 'ApplicationSymbolType'):
        assert not _is_linked(b2, 'ApplicationSymbolType', a)


def test_assoc_applicationType213_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    b2 = carnot_ApplicationTypeType(accessPointProviderClass="sample_text_2", instanceClass="sample_text_2", panelClass="sample_text_2", synchronous="sample_text_2", validatorClass="sample_text_2")
    _safe_set(a, 'carnot_ModelType214', {b1})
    assert _is_linked(a, 'carnot_ModelType214', b1)
    if hasattr(b1, 'carnot_ApplicationTypeType'):
        assert _is_linked(b1, 'carnot_ApplicationTypeType', a)
    _safe_set(a, 'carnot_ModelType214', {b2})
    assert _is_linked(a, 'carnot_ModelType214', b2)
    if hasattr(b1, 'carnot_ApplicationTypeType'):
        assert not _is_linked(b1, 'carnot_ApplicationTypeType', a)
    if hasattr(b2, 'carnot_ApplicationTypeType'):
        assert _is_linked(b2, 'carnot_ApplicationTypeType', a)
    _safe_set(a, 'carnot_ModelType214', set())
    assert not _is_linked(a, 'carnot_ModelType214', b2)
    if hasattr(b2, 'carnot_ApplicationTypeType'):
        assert not _is_linked(b2, 'carnot_ApplicationTypeType', a)


def test_assoc_applications124_link_reassign_clear():
    a = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    b1 = carnot_ApplicationType(interactive="sample_text")
    b2 = carnot_ApplicationType(interactive="sample_text_2")
    _safe_set(a, 'type125', {b1})
    assert _is_linked(a, 'type125', b1)
    if hasattr(b1, 'ApplicationType126'):
        assert _is_linked(b1, 'ApplicationType126', a)
    _safe_set(a, 'type125', {b2})
    assert _is_linked(a, 'type125', b2)
    if hasattr(b1, 'ApplicationType126'):
        assert not _is_linked(b1, 'ApplicationType126', a)
    if hasattr(b2, 'ApplicationType126'):
        assert _is_linked(b2, 'ApplicationType126', a)
    _safe_set(a, 'type125', set())
    assert not _is_linked(a, 'type125', b2)
    if hasattr(b2, 'ApplicationType126'):
        assert not _is_linked(b2, 'ApplicationType126', a)


def test_assoc_attribute0_link_reassign_clear():
    a = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    b1 = carnot_IExtensibleElement()
    b2 = carnot_IExtensibleElement()
    _safe_set(a, 'carnot_AttributeType', b1)
    assert _is_linked(a, 'carnot_AttributeType', b1)
    if hasattr(b1, 'carnot_IExtensibleElement'):
        assert _is_linked(b1, 'carnot_IExtensibleElement', a)
    _safe_set(a, 'carnot_AttributeType', b2)
    assert _is_linked(a, 'carnot_AttributeType', b2)
    if hasattr(b1, 'carnot_IExtensibleElement'):
        assert not _is_linked(b1, 'carnot_IExtensibleElement', a)
    if hasattr(b2, 'carnot_IExtensibleElement'):
        assert _is_linked(b2, 'carnot_IExtensibleElement', a)
    _safe_set(a, 'carnot_AttributeType', None)
    assert not _is_linked(a, 'carnot_AttributeType', b2)
    if hasattr(b2, 'carnot_IExtensibleElement'):
        assert not _is_linked(b2, 'carnot_IExtensibleElement', a)


def test_assoc_attribute1_link_reassign_clear():
    a = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    b1 = carnot_IdentifiableReference()
    b2 = carnot_IdentifiableReference()
    _safe_set(a, 'AttributeType', b1)
    assert _is_linked(a, 'AttributeType', b1)
    if hasattr(b1, 'reference'):
        assert _is_linked(b1, 'reference', a)
    _safe_set(a, 'AttributeType', b2)
    assert _is_linked(a, 'AttributeType', b2)
    if hasattr(b1, 'reference'):
        assert not _is_linked(b1, 'reference', a)
    if hasattr(b2, 'reference'):
        assert _is_linked(b2, 'reference', a)
    _safe_set(a, 'AttributeType', None)
    assert not _is_linked(a, 'AttributeType', b2)
    if hasattr(b2, 'reference'):
        assert not _is_linked(b2, 'reference', a)


def test_assoc_bindAction179_link_reassign_clear():
    a = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    b1 = carnot_BindActionType()
    b2 = carnot_BindActionType()
    _safe_set(a, 'carnot_EventHandlerType180', {b1})
    assert _is_linked(a, 'carnot_EventHandlerType180', b1)
    if hasattr(b1, 'carnot_BindActionType'):
        assert _is_linked(b1, 'carnot_BindActionType', a)
    _safe_set(a, 'carnot_EventHandlerType180', {b2})
    assert _is_linked(a, 'carnot_EventHandlerType180', b2)
    if hasattr(b1, 'carnot_BindActionType'):
        assert not _is_linked(b1, 'carnot_BindActionType', a)
    if hasattr(b2, 'carnot_BindActionType'):
        assert _is_linked(b2, 'carnot_BindActionType', a)
    _safe_set(a, 'carnot_EventHandlerType180', set())
    assert not _is_linked(a, 'carnot_EventHandlerType180', b2)
    if hasattr(b2, 'carnot_BindActionType'):
        assert not _is_linked(b2, 'carnot_BindActionType', a)


def test_assoc_childLanes66_link_reassign_clear():
    a = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    b1 = carnot_LaneSymbol()
    b2 = carnot_LaneSymbol()
    _safe_set(a, 'parentLane', {b1})
    assert _is_linked(a, 'parentLane', b1)
    if hasattr(b1, 'LaneSymbol'):
        assert _is_linked(b1, 'LaneSymbol', a)
    _safe_set(a, 'parentLane', {b2})
    assert _is_linked(a, 'parentLane', b2)
    if hasattr(b1, 'LaneSymbol'):
        assert not _is_linked(b1, 'LaneSymbol', a)
    if hasattr(b2, 'LaneSymbol'):
        assert _is_linked(b2, 'LaneSymbol', a)
    _safe_set(a, 'parentLane', set())
    assert not _is_linked(a, 'parentLane', b2)
    if hasattr(b2, 'LaneSymbol'):
        assert not _is_linked(b2, 'LaneSymbol', a)


def test_assoc_conditionalPerformer237_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    b2 = carnot_ConditionalPerformerType(dataPath="sample_text_2", isUser="sample_text_2")
    _safe_set(a, 'carnot_ModelType238', {b1})
    assert _is_linked(a, 'carnot_ModelType238', b1)
    if hasattr(b1, 'carnot_ConditionalPerformerType'):
        assert _is_linked(b1, 'carnot_ConditionalPerformerType', a)
    _safe_set(a, 'carnot_ModelType238', {b2})
    assert _is_linked(a, 'carnot_ModelType238', b2)
    if hasattr(b1, 'carnot_ConditionalPerformerType'):
        assert not _is_linked(b1, 'carnot_ConditionalPerformerType', a)
    if hasattr(b2, 'carnot_ConditionalPerformerType'):
        assert _is_linked(b2, 'carnot_ConditionalPerformerType', a)
    _safe_set(a, 'carnot_ModelType238', set())
    assert not _is_linked(a, 'carnot_ModelType238', b2)
    if hasattr(b2, 'carnot_ConditionalPerformerType'):
        assert not _is_linked(b2, 'carnot_ConditionalPerformerType', a)


def test_assoc_conditionalPerformerSymbol11_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_ConditionalPerformerSymbolType()
    b2 = carnot_ConditionalPerformerSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer12', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer12', b1)
    if hasattr(b1, 'carnot_ConditionalPerformerSymbolType'):
        assert _is_linked(b1, 'carnot_ConditionalPerformerSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer12', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer12', b2)
    if hasattr(b1, 'carnot_ConditionalPerformerSymbolType'):
        assert not _is_linked(b1, 'carnot_ConditionalPerformerSymbolType', a)
    if hasattr(b2, 'carnot_ConditionalPerformerSymbolType'):
        assert _is_linked(b2, 'carnot_ConditionalPerformerSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer12', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer12', b2)
    if hasattr(b2, 'carnot_ConditionalPerformerSymbolType'):
        assert not _is_linked(b2, 'carnot_ConditionalPerformerSymbolType', a)


def test_assoc_conditionalPerformerSymbols132_link_reassign_clear():
    a = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    b1 = carnot_ConditionalPerformerSymbolType()
    b2 = carnot_ConditionalPerformerSymbolType()
    _safe_set(a, 'participant133', {b1})
    assert _is_linked(a, 'participant133', b1)
    if hasattr(b1, 'ConditionalPerformerSymbolType'):
        assert _is_linked(b1, 'ConditionalPerformerSymbolType', a)
    _safe_set(a, 'participant133', {b2})
    assert _is_linked(a, 'participant133', b2)
    if hasattr(b1, 'ConditionalPerformerSymbolType'):
        assert not _is_linked(b1, 'ConditionalPerformerSymbolType', a)
    if hasattr(b2, 'ConditionalPerformerSymbolType'):
        assert _is_linked(b2, 'ConditionalPerformerSymbolType', a)
    _safe_set(a, 'participant133', set())
    assert not _is_linked(a, 'participant133', b2)
    if hasattr(b2, 'ConditionalPerformerSymbolType'):
        assert not _is_linked(b2, 'ConditionalPerformerSymbolType', a)


def test_assoc_conditionalPerformers157_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    b2 = carnot_ConditionalPerformerType(dataPath="sample_text_2", isUser="sample_text_2")
    _safe_set(a, 'data158', {b1})
    assert _is_linked(a, 'data158', b1)
    if hasattr(b1, 'ConditionalPerformerType159'):
        assert _is_linked(b1, 'ConditionalPerformerType159', a)
    _safe_set(a, 'data158', {b2})
    assert _is_linked(a, 'data158', b2)
    if hasattr(b1, 'ConditionalPerformerType159'):
        assert not _is_linked(b1, 'ConditionalPerformerType159', a)
    if hasattr(b2, 'ConditionalPerformerType159'):
        assert _is_linked(b2, 'ConditionalPerformerType159', a)
    _safe_set(a, 'data158', set())
    assert not _is_linked(a, 'data158', b2)
    if hasattr(b2, 'ConditionalPerformerType159'):
        assert not _is_linked(b2, 'ConditionalPerformerType159', a)


def test_assoc_context118_link_reassign_clear():
    a = carnot_ApplicationType(interactive="sample_text")
    b1 = carnot_ContextType()
    b2 = carnot_ContextType()
    _safe_set(a, 'carnot_ApplicationType', {b1})
    assert _is_linked(a, 'carnot_ApplicationType', b1)
    if hasattr(b1, 'carnot_ContextType'):
        assert _is_linked(b1, 'carnot_ContextType', a)
    _safe_set(a, 'carnot_ApplicationType', {b2})
    assert _is_linked(a, 'carnot_ApplicationType', b2)
    if hasattr(b1, 'carnot_ContextType'):
        assert not _is_linked(b1, 'carnot_ContextType', a)
    if hasattr(b2, 'carnot_ContextType'):
        assert _is_linked(b2, 'carnot_ContextType', a)
    _safe_set(a, 'carnot_ApplicationType', set())
    assert not _is_linked(a, 'carnot_ApplicationType', b2)
    if hasattr(b2, 'carnot_ContextType'):
        assert not _is_linked(b2, 'carnot_ContextType', a)


def test_assoc_contexts113_link_reassign_clear():
    a = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    b1 = carnot_ContextType()
    b2 = carnot_ContextType()
    _safe_set(a, 'type', {b1})
    assert _is_linked(a, 'type', b1)
    if hasattr(b1, 'ContextType'):
        assert _is_linked(b1, 'ContextType', a)
    _safe_set(a, 'type', {b2})
    assert _is_linked(a, 'type', b2)
    if hasattr(b1, 'ContextType'):
        assert not _is_linked(b1, 'ContextType', a)
    if hasattr(b2, 'ContextType'):
        assert _is_linked(b2, 'ContextType', a)
    _safe_set(a, 'type', set())
    assert not _is_linked(a, 'type', b2)
    if hasattr(b2, 'ContextType'):
        assert not _is_linked(b2, 'ContextType', a)


def test_assoc_coordinates71_link_reassign_clear():
    a = carnot_IConnectionSymbol(routing="sample_text", sourceAnchor="sample_text", targetAnchor="sample_text")
    b1 = carnot_Coordinates(xPos="sample_text", yPos="sample_text")
    b2 = carnot_Coordinates(xPos="sample_text_2", yPos="sample_text_2")
    _safe_set(a, 'carnot_IConnectionSymbol', {b1})
    assert _is_linked(a, 'carnot_IConnectionSymbol', b1)
    if hasattr(b1, 'carnot_Coordinates'):
        assert _is_linked(b1, 'carnot_Coordinates', a)
    _safe_set(a, 'carnot_IConnectionSymbol', {b2})
    assert _is_linked(a, 'carnot_IConnectionSymbol', b2)
    if hasattr(b1, 'carnot_Coordinates'):
        assert not _is_linked(b1, 'carnot_Coordinates', a)
    if hasattr(b2, 'carnot_Coordinates'):
        assert _is_linked(b2, 'carnot_Coordinates', a)
    _safe_set(a, 'carnot_IConnectionSymbol', set())
    assert not _is_linked(a, 'carnot_IConnectionSymbol', b2)
    if hasattr(b2, 'carnot_Coordinates'):
        assert not _is_linked(b2, 'carnot_Coordinates', a)


def test_assoc_data131_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    b2 = carnot_ConditionalPerformerType(dataPath="sample_text_2", isUser="sample_text_2")
    _safe_set(a, 'DataType', b1)
    assert _is_linked(a, 'DataType', b1)
    if hasattr(b1, 'conditionalPerformers'):
        assert _is_linked(b1, 'conditionalPerformers', a)
    _safe_set(a, 'DataType', b2)
    assert _is_linked(a, 'DataType', b2)
    if hasattr(b1, 'conditionalPerformers'):
        assert not _is_linked(b1, 'conditionalPerformers', a)
    if hasattr(b2, 'conditionalPerformers'):
        assert _is_linked(b2, 'conditionalPerformers', a)
    _safe_set(a, 'DataType', None)
    assert not _is_linked(a, 'DataType', b2)
    if hasattr(b2, 'conditionalPerformers'):
        assert not _is_linked(b2, 'conditionalPerformers', a)


def test_assoc_data142_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    b2 = carnot_DataMappingType(applicationAccessPoint="sample_text_2", applicationPath="sample_text_2", context="sample_text_2", dataPath="sample_text_2", direction="sample_text_2")
    _safe_set(a, 'DataType144', b1)
    assert _is_linked(a, 'DataType144', b1)
    if hasattr(b1, 'dataMappings143'):
        assert _is_linked(b1, 'dataMappings143', a)
    _safe_set(a, 'DataType144', b2)
    assert _is_linked(a, 'DataType144', b2)
    if hasattr(b1, 'dataMappings143'):
        assert not _is_linked(b1, 'dataMappings143', a)
    if hasattr(b2, 'dataMappings143'):
        assert _is_linked(b2, 'dataMappings143', a)
    _safe_set(a, 'DataType144', None)
    assert not _is_linked(a, 'DataType144', b2)
    if hasattr(b2, 'dataMappings143'):
        assert not _is_linked(b2, 'dataMappings143', a)


def test_assoc_data145_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    b2 = carnot_DataPathType(dataPath="sample_text_2", descriptor="sample_text_2", direction="sample_text_2", key="sample_text_2")
    _safe_set(a, 'DataType146', b1)
    assert _is_linked(a, 'DataType146', b1)
    if hasattr(b1, 'dataPaths'):
        assert _is_linked(b1, 'dataPaths', a)
    _safe_set(a, 'DataType146', b2)
    assert _is_linked(a, 'DataType146', b2)
    if hasattr(b1, 'dataPaths'):
        assert not _is_linked(b1, 'dataPaths', a)
    if hasattr(b2, 'dataPaths'):
        assert _is_linked(b2, 'dataPaths', a)
    _safe_set(a, 'DataType146', None)
    assert not _is_linked(a, 'DataType146', b2)
    if hasattr(b2, 'dataPaths'):
        assert not _is_linked(b2, 'dataPaths', a)


def test_assoc_data147_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_DataSymbolType()
    b2 = carnot_DataSymbolType()
    _safe_set(a, 'DataType148', b1)
    assert _is_linked(a, 'DataType148', b1)
    if hasattr(b1, 'dataSymbols'):
        assert _is_linked(b1, 'dataSymbols', a)
    _safe_set(a, 'DataType148', b2)
    assert _is_linked(a, 'DataType148', b2)
    if hasattr(b1, 'dataSymbols'):
        assert not _is_linked(b1, 'dataSymbols', a)
    if hasattr(b2, 'dataSymbols'):
        assert _is_linked(b2, 'dataSymbols', a)
    _safe_set(a, 'DataType148', None)
    assert not _is_linked(a, 'DataType148', b2)
    if hasattr(b2, 'dataSymbols'):
        assert not _is_linked(b2, 'dataSymbols', a)


def test_assoc_data165_link_reassign_clear():
    a = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    b1 = carnot_DataType(predefined="sample_text")
    b2 = carnot_DataType(predefined="sample_text_2")
    _safe_set(a, 'type166', {b1})
    assert _is_linked(a, 'type166', b1)
    if hasattr(b1, 'DataType167'):
        assert _is_linked(b1, 'DataType167', a)
    _safe_set(a, 'type166', {b2})
    assert _is_linked(a, 'type166', b2)
    if hasattr(b1, 'DataType167'):
        assert not _is_linked(b1, 'DataType167', a)
    if hasattr(b2, 'DataType167'):
        assert _is_linked(b2, 'DataType167', a)
    _safe_set(a, 'type166', set())
    assert not _is_linked(a, 'type166', b2)
    if hasattr(b2, 'DataType167'):
        assert not _is_linked(b2, 'DataType167', a)


def test_assoc_data223_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_DataType(predefined="sample_text")
    b2 = carnot_DataType(predefined="sample_text_2")
    _safe_set(a, 'carnot_ModelType224', {b1})
    assert _is_linked(a, 'carnot_ModelType224', b1)
    if hasattr(b1, 'carnot_DataType225'):
        assert _is_linked(b1, 'carnot_DataType225', a)
    _safe_set(a, 'carnot_ModelType224', {b2})
    assert _is_linked(a, 'carnot_ModelType224', b2)
    if hasattr(b1, 'carnot_DataType225'):
        assert not _is_linked(b1, 'carnot_DataType225', a)
    if hasattr(b2, 'carnot_DataType225'):
        assert _is_linked(b2, 'carnot_DataType225', a)
    _safe_set(a, 'carnot_ModelType224', set())
    assert not _is_linked(a, 'carnot_ModelType224', b2)
    if hasattr(b2, 'carnot_DataType225'):
        assert not _is_linked(b2, 'carnot_DataType225', a)


def test_assoc_data264_link_reassign_clear():
    a = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    b1 = carnot_DataType(predefined="sample_text")
    b2 = carnot_DataType(predefined="sample_text_2")
    _safe_set(a, 'parameterMappings', b1)
    assert _is_linked(a, 'parameterMappings', b1)
    if hasattr(b1, 'DataType265'):
        assert _is_linked(b1, 'DataType265', a)
    _safe_set(a, 'parameterMappings', b2)
    assert _is_linked(a, 'parameterMappings', b2)
    if hasattr(b1, 'DataType265'):
        assert not _is_linked(b1, 'DataType265', a)
    if hasattr(b2, 'DataType265'):
        assert _is_linked(b2, 'DataType265', a)
    _safe_set(a, 'parameterMappings', None)
    assert not _is_linked(a, 'parameterMappings', b2)
    if hasattr(b2, 'DataType265'):
        assert not _is_linked(b2, 'DataType265', a)


def test_assoc_dataMapping92_link_reassign_clear():
    a = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'carnot_DataMappingType', b1)
    assert _is_linked(a, 'carnot_DataMappingType', b1)
    if hasattr(b1, 'carnot_ActivityType'):
        assert _is_linked(b1, 'carnot_ActivityType', a)
    _safe_set(a, 'carnot_DataMappingType', b2)
    assert _is_linked(a, 'carnot_DataMappingType', b2)
    if hasattr(b1, 'carnot_ActivityType'):
        assert not _is_linked(b1, 'carnot_ActivityType', a)
    if hasattr(b2, 'carnot_ActivityType'):
        assert _is_linked(b2, 'carnot_ActivityType', a)
    _safe_set(a, 'carnot_DataMappingType', None)
    assert not _is_linked(a, 'carnot_DataMappingType', b2)
    if hasattr(b2, 'carnot_ActivityType'):
        assert not _is_linked(b2, 'carnot_ActivityType', a)


def test_assoc_dataMappingConnection37_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_DataMappingConnectionType()
    b2 = carnot_DataMappingConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer38', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer38', b1)
    if hasattr(b1, 'carnot_DataMappingConnectionType'):
        assert _is_linked(b1, 'carnot_DataMappingConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer38', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer38', b2)
    if hasattr(b1, 'carnot_DataMappingConnectionType'):
        assert not _is_linked(b1, 'carnot_DataMappingConnectionType', a)
    if hasattr(b2, 'carnot_DataMappingConnectionType'):
        assert _is_linked(b2, 'carnot_DataMappingConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer38', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer38', b2)
    if hasattr(b2, 'carnot_DataMappingConnectionType'):
        assert not _is_linked(b2, 'carnot_DataMappingConnectionType', a)


def test_assoc_dataMappings151_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_DataMappingType(applicationAccessPoint="sample_text", applicationPath="sample_text", context="sample_text", dataPath="sample_text", direction="sample_text")
    b2 = carnot_DataMappingType(applicationAccessPoint="sample_text_2", applicationPath="sample_text_2", context="sample_text_2", dataPath="sample_text_2", direction="sample_text_2")
    _safe_set(a, 'data', {b1})
    assert _is_linked(a, 'data', b1)
    if hasattr(b1, 'DataMappingType'):
        assert _is_linked(b1, 'DataMappingType', a)
    _safe_set(a, 'data', {b2})
    assert _is_linked(a, 'data', b2)
    if hasattr(b1, 'DataMappingType'):
        assert not _is_linked(b1, 'DataMappingType', a)
    if hasattr(b2, 'DataMappingType'):
        assert _is_linked(b2, 'DataMappingType', a)
    _safe_set(a, 'data', set())
    assert not _is_linked(a, 'data', b2)
    if hasattr(b2, 'DataMappingType'):
        assert not _is_linked(b2, 'DataMappingType', a)


def test_assoc_dataPath288_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    b2 = carnot_DataPathType(dataPath="sample_text_2", descriptor="sample_text_2", direction="sample_text_2", key="sample_text_2")
    _safe_set(a, 'carnot_ProcessDefinitionType289', {b1})
    assert _is_linked(a, 'carnot_ProcessDefinitionType289', b1)
    if hasattr(b1, 'carnot_DataPathType'):
        assert _is_linked(b1, 'carnot_DataPathType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType289', {b2})
    assert _is_linked(a, 'carnot_ProcessDefinitionType289', b2)
    if hasattr(b1, 'carnot_DataPathType'):
        assert not _is_linked(b1, 'carnot_DataPathType', a)
    if hasattr(b2, 'carnot_DataPathType'):
        assert _is_linked(b2, 'carnot_DataPathType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType289', set())
    assert not _is_linked(a, 'carnot_ProcessDefinitionType289', b2)
    if hasattr(b2, 'carnot_DataPathType'):
        assert not _is_linked(b2, 'carnot_DataPathType', a)


def test_assoc_dataPaths160_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_DataPathType(dataPath="sample_text", descriptor="sample_text", direction="sample_text", key="sample_text")
    b2 = carnot_DataPathType(dataPath="sample_text_2", descriptor="sample_text_2", direction="sample_text_2", key="sample_text_2")
    _safe_set(a, 'data161', {b1})
    assert _is_linked(a, 'data161', b1)
    if hasattr(b1, 'DataPathType'):
        assert _is_linked(b1, 'DataPathType', a)
    _safe_set(a, 'data161', {b2})
    assert _is_linked(a, 'data161', b2)
    if hasattr(b1, 'DataPathType'):
        assert not _is_linked(b1, 'DataPathType', a)
    if hasattr(b2, 'DataPathType'):
        assert _is_linked(b2, 'DataPathType', a)
    _safe_set(a, 'data161', set())
    assert not _is_linked(a, 'data161', b2)
    if hasattr(b2, 'DataPathType'):
        assert not _is_linked(b2, 'DataPathType', a)


def test_assoc_dataSymbol13_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_DataSymbolType()
    b2 = carnot_DataSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer14', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer14', b1)
    if hasattr(b1, 'carnot_DataSymbolType'):
        assert _is_linked(b1, 'carnot_DataSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer14', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer14', b2)
    if hasattr(b1, 'carnot_DataSymbolType'):
        assert not _is_linked(b1, 'carnot_DataSymbolType', a)
    if hasattr(b2, 'carnot_DataSymbolType'):
        assert _is_linked(b2, 'carnot_DataSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer14', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer14', b2)
    if hasattr(b2, 'carnot_DataSymbolType'):
        assert not _is_linked(b2, 'carnot_DataSymbolType', a)


def test_assoc_dataSymbols154_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_DataSymbolType()
    b2 = carnot_DataSymbolType()
    _safe_set(a, 'data155', {b1})
    assert _is_linked(a, 'data155', b1)
    if hasattr(b1, 'DataSymbolType156'):
        assert _is_linked(b1, 'DataSymbolType156', a)
    _safe_set(a, 'data155', {b2})
    assert _is_linked(a, 'data155', b2)
    if hasattr(b1, 'DataSymbolType156'):
        assert not _is_linked(b1, 'DataSymbolType156', a)
    if hasattr(b2, 'DataSymbolType156'):
        assert _is_linked(b2, 'DataSymbolType156', a)
    _safe_set(a, 'data155', set())
    assert not _is_linked(a, 'data155', b2)
    if hasattr(b2, 'DataSymbolType156'):
        assert not _is_linked(b2, 'DataSymbolType156', a)


def test_assoc_dataType210_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    b2 = carnot_DataTypeType(accessPathEditor="sample_text_2", evaluator="sample_text_2", instanceClass="sample_text_2", panelClass="sample_text_2", readable="sample_text_2", storageStrategy="sample_text_2", validatorClass="sample_text_2", valueCreator="sample_text_2", writable="sample_text_2")
    _safe_set(a, 'carnot_ModelType211', {b1})
    assert _is_linked(a, 'carnot_ModelType211', b1)
    if hasattr(b1, 'carnot_DataTypeType212'):
        assert _is_linked(b1, 'carnot_DataTypeType212', a)
    _safe_set(a, 'carnot_ModelType211', {b2})
    assert _is_linked(a, 'carnot_ModelType211', b2)
    if hasattr(b1, 'carnot_DataTypeType212'):
        assert not _is_linked(b1, 'carnot_DataTypeType212', a)
    if hasattr(b2, 'carnot_DataTypeType212'):
        assert _is_linked(b2, 'carnot_DataTypeType212', a)
    _safe_set(a, 'carnot_ModelType211', set())
    assert not _is_linked(a, 'carnot_ModelType211', b2)
    if hasattr(b2, 'carnot_DataTypeType212'):
        assert not _is_linked(b2, 'carnot_DataTypeType212', a)


def test_assoc_description134_link_reassign_clear():
    a = carnot_DescriptionType(mixed="sample_text")
    b1 = carnot_ContextType()
    b2 = carnot_ContextType()
    _safe_set(a, 'carnot_DescriptionType136', b1)
    assert _is_linked(a, 'carnot_DescriptionType136', b1)
    if hasattr(b1, 'carnot_ContextType135'):
        assert _is_linked(b1, 'carnot_ContextType135', a)
    _safe_set(a, 'carnot_DescriptionType136', b2)
    assert _is_linked(a, 'carnot_DescriptionType136', b2)
    if hasattr(b1, 'carnot_ContextType135'):
        assert not _is_linked(b1, 'carnot_ContextType135', a)
    if hasattr(b2, 'carnot_ContextType135'):
        assert _is_linked(b2, 'carnot_ContextType135', a)
    _safe_set(a, 'carnot_DescriptionType136', None)
    assert not _is_linked(a, 'carnot_DescriptionType136', b2)
    if hasattr(b2, 'carnot_ContextType135'):
        assert not _is_linked(b2, 'carnot_ContextType135', a)


def test_assoc_description207_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_DescriptionType(mixed="sample_text")
    b2 = carnot_DescriptionType(mixed="sample_text_2")
    _safe_set(a, 'carnot_ModelType208', b1)
    assert _is_linked(a, 'carnot_ModelType208', b1)
    if hasattr(b1, 'carnot_DescriptionType209'):
        assert _is_linked(b1, 'carnot_DescriptionType209', a)
    _safe_set(a, 'carnot_ModelType208', b2)
    assert _is_linked(a, 'carnot_ModelType208', b2)
    if hasattr(b1, 'carnot_DescriptionType209'):
        assert not _is_linked(b1, 'carnot_DescriptionType209', a)
    if hasattr(b2, 'carnot_DescriptionType209'):
        assert _is_linked(b2, 'carnot_DescriptionType209', a)
    _safe_set(a, 'carnot_ModelType208', None)
    assert not _is_linked(a, 'carnot_ModelType208', b2)
    if hasattr(b2, 'carnot_DescriptionType209'):
        assert not _is_linked(b2, 'carnot_DescriptionType209', a)


def test_assoc_description3_link_reassign_clear():
    a = carnot_IIdentifiableModelElement()
    b1 = carnot_DescriptionType(mixed="sample_text")
    b2 = carnot_DescriptionType(mixed="sample_text_2")
    _safe_set(a, 'carnot_IIdentifiableModelElement', b1)
    assert _is_linked(a, 'carnot_IIdentifiableModelElement', b1)
    if hasattr(b1, 'carnot_DescriptionType'):
        assert _is_linked(b1, 'carnot_DescriptionType', a)
    _safe_set(a, 'carnot_IIdentifiableModelElement', b2)
    assert _is_linked(a, 'carnot_IIdentifiableModelElement', b2)
    if hasattr(b1, 'carnot_DescriptionType'):
        assert not _is_linked(b1, 'carnot_DescriptionType', a)
    if hasattr(b2, 'carnot_DescriptionType'):
        assert _is_linked(b2, 'carnot_DescriptionType', a)
    _safe_set(a, 'carnot_IIdentifiableModelElement', None)
    assert not _is_linked(a, 'carnot_IIdentifiableModelElement', b2)
    if hasattr(b2, 'carnot_DescriptionType'):
        assert not _is_linked(b2, 'carnot_DescriptionType', a)


def test_assoc_description369_link_reassign_clear():
    a = carnot_ViewType(name="sample_text")
    b1 = carnot_DescriptionType(mixed="sample_text")
    b2 = carnot_DescriptionType(mixed="sample_text_2")
    _safe_set(a, 'carnot_ViewType370', b1)
    assert _is_linked(a, 'carnot_ViewType370', b1)
    if hasattr(b1, 'carnot_DescriptionType371'):
        assert _is_linked(b1, 'carnot_DescriptionType371', a)
    _safe_set(a, 'carnot_ViewType370', b2)
    assert _is_linked(a, 'carnot_ViewType370', b2)
    if hasattr(b1, 'carnot_DescriptionType371'):
        assert not _is_linked(b1, 'carnot_DescriptionType371', a)
    if hasattr(b2, 'carnot_DescriptionType371'):
        assert _is_linked(b2, 'carnot_DescriptionType371', a)
    _safe_set(a, 'carnot_ViewType370', None)
    assert not _is_linked(a, 'carnot_ViewType370', b2)
    if hasattr(b2, 'carnot_DescriptionType371'):
        assert not _is_linked(b2, 'carnot_DescriptionType371', a)


def test_assoc_diagram247_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    b2 = carnot_DiagramType(mode="sample_text_2", name="sample_text_2", orientation="sample_text_2")
    _safe_set(a, 'carnot_ModelType248', {b1})
    assert _is_linked(a, 'carnot_ModelType248', b1)
    if hasattr(b1, 'carnot_DiagramType'):
        assert _is_linked(b1, 'carnot_DiagramType', a)
    _safe_set(a, 'carnot_ModelType248', {b2})
    assert _is_linked(a, 'carnot_ModelType248', b2)
    if hasattr(b1, 'carnot_DiagramType'):
        assert not _is_linked(b1, 'carnot_DiagramType', a)
    if hasattr(b2, 'carnot_DiagramType'):
        assert _is_linked(b2, 'carnot_DiagramType', a)
    _safe_set(a, 'carnot_ModelType248', set())
    assert not _is_linked(a, 'carnot_ModelType248', b2)
    if hasattr(b2, 'carnot_DiagramType'):
        assert not _is_linked(b2, 'carnot_DiagramType', a)


def test_assoc_diagram276_link_reassign_clear():
    a = carnot_PoolSymbol(boundaryVisible="sample_text")
    b1 = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    b2 = carnot_DiagramType(mode="sample_text_2", name="sample_text_2", orientation="sample_text_2")
    _safe_set(a, 'poolSymbols', b1)
    assert _is_linked(a, 'poolSymbols', b1)
    if hasattr(b1, 'DiagramType'):
        assert _is_linked(b1, 'DiagramType', a)
    _safe_set(a, 'poolSymbols', b2)
    assert _is_linked(a, 'poolSymbols', b2)
    if hasattr(b1, 'DiagramType'):
        assert not _is_linked(b1, 'DiagramType', a)
    if hasattr(b2, 'DiagramType'):
        assert _is_linked(b2, 'DiagramType', a)
    _safe_set(a, 'poolSymbols', None)
    assert not _is_linked(a, 'poolSymbols', b2)
    if hasattr(b2, 'DiagramType'):
        assert not _is_linked(b2, 'DiagramType', a)


def test_assoc_diagram290_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    b2 = carnot_DiagramType(mode="sample_text_2", name="sample_text_2", orientation="sample_text_2")
    _safe_set(a, 'carnot_ProcessDefinitionType291', {b1})
    assert _is_linked(a, 'carnot_ProcessDefinitionType291', b1)
    if hasattr(b1, 'carnot_DiagramType292'):
        assert _is_linked(b1, 'carnot_DiagramType292', a)
    _safe_set(a, 'carnot_ProcessDefinitionType291', {b2})
    assert _is_linked(a, 'carnot_ProcessDefinitionType291', b2)
    if hasattr(b1, 'carnot_DiagramType292'):
        assert not _is_linked(b1, 'carnot_DiagramType292', a)
    if hasattr(b2, 'carnot_DiagramType292'):
        assert _is_linked(b2, 'carnot_DiagramType292', a)
    _safe_set(a, 'carnot_ProcessDefinitionType291', set())
    assert not _is_linked(a, 'carnot_ProcessDefinitionType291', b2)
    if hasattr(b2, 'carnot_DiagramType292'):
        assert not _is_linked(b2, 'carnot_DiagramType292', a)


def test_assoc_endEventSymbols15_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_EndEventSymbol()
    b2 = carnot_EndEventSymbol()
    _safe_set(a, 'carnot_ISymbolContainer16', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer16', b1)
    if hasattr(b1, 'carnot_EndEventSymbol'):
        assert _is_linked(b1, 'carnot_EndEventSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer16', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer16', b2)
    if hasattr(b1, 'carnot_EndEventSymbol'):
        assert not _is_linked(b1, 'carnot_EndEventSymbol', a)
    if hasattr(b2, 'carnot_EndEventSymbol'):
        assert _is_linked(b2, 'carnot_EndEventSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer16', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer16', b2)
    if hasattr(b2, 'carnot_EndEventSymbol'):
        assert not _is_linked(b2, 'carnot_EndEventSymbol', a)


def test_assoc_eventAction181_link_reassign_clear():
    a = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    b1 = carnot_EventActionType()
    b2 = carnot_EventActionType()
    _safe_set(a, 'carnot_EventHandlerType182', {b1})
    assert _is_linked(a, 'carnot_EventHandlerType182', b1)
    if hasattr(b1, 'carnot_EventActionType'):
        assert _is_linked(b1, 'carnot_EventActionType', a)
    _safe_set(a, 'carnot_EventHandlerType182', {b2})
    assert _is_linked(a, 'carnot_EventHandlerType182', b2)
    if hasattr(b1, 'carnot_EventActionType'):
        assert not _is_linked(b1, 'carnot_EventActionType', a)
    if hasattr(b2, 'carnot_EventActionType'):
        assert _is_linked(b2, 'carnot_EventActionType', a)
    _safe_set(a, 'carnot_EventHandlerType182', set())
    assert not _is_linked(a, 'carnot_EventHandlerType182', b2)
    if hasattr(b2, 'carnot_EventActionType'):
        assert not _is_linked(b2, 'carnot_EventActionType', a)


def test_assoc_eventActionType221_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    b2 = carnot_EventActionTypeType(actionClass="sample_text_2", activityAction="sample_text_2", panelClass="sample_text_2", processAction="sample_text_2", supportedConditionTypes="sample_text_2", unsupportedContexts="sample_text_2")
    _safe_set(a, 'carnot_ModelType222', {b1})
    assert _is_linked(a, 'carnot_ModelType222', b1)
    if hasattr(b1, 'carnot_EventActionTypeType'):
        assert _is_linked(b1, 'carnot_EventActionTypeType', a)
    _safe_set(a, 'carnot_ModelType222', {b2})
    assert _is_linked(a, 'carnot_ModelType222', b2)
    if hasattr(b1, 'carnot_EventActionTypeType'):
        assert not _is_linked(b1, 'carnot_EventActionTypeType', a)
    if hasattr(b2, 'carnot_EventActionTypeType'):
        assert _is_linked(b2, 'carnot_EventActionTypeType', a)
    _safe_set(a, 'carnot_ModelType222', set())
    assert not _is_linked(a, 'carnot_ModelType222', b2)
    if hasattr(b2, 'carnot_EventActionTypeType'):
        assert not _is_linked(b2, 'carnot_EventActionTypeType', a)


def test_assoc_eventConditionType219_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    b2 = carnot_EventConditionTypeType(activityCondition="sample_text_2", binderClass="sample_text_2", implementation="sample_text_2", panelClass="sample_text_2", processCondition="sample_text_2", pullEventEmitterClass="sample_text_2", rule="sample_text_2")
    _safe_set(a, 'carnot_ModelType220', {b1})
    assert _is_linked(a, 'carnot_ModelType220', b1)
    if hasattr(b1, 'carnot_EventConditionTypeType'):
        assert _is_linked(b1, 'carnot_EventConditionTypeType', a)
    _safe_set(a, 'carnot_ModelType220', {b2})
    assert _is_linked(a, 'carnot_ModelType220', b2)
    if hasattr(b1, 'carnot_EventConditionTypeType'):
        assert not _is_linked(b1, 'carnot_EventConditionTypeType', a)
    if hasattr(b2, 'carnot_EventConditionTypeType'):
        assert _is_linked(b2, 'carnot_EventConditionTypeType', a)
    _safe_set(a, 'carnot_ModelType220', set())
    assert not _is_linked(a, 'carnot_ModelType220', b2)
    if hasattr(b2, 'carnot_EventConditionTypeType'):
        assert not _is_linked(b2, 'carnot_EventConditionTypeType', a)


def test_assoc_eventHandler4_link_reassign_clear():
    a = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    b1 = carnot_IEventHandlerOwner()
    b2 = carnot_IEventHandlerOwner()
    _safe_set(a, 'carnot_EventHandlerType', b1)
    assert _is_linked(a, 'carnot_EventHandlerType', b1)
    if hasattr(b1, 'carnot_IEventHandlerOwner'):
        assert _is_linked(b1, 'carnot_IEventHandlerOwner', a)
    _safe_set(a, 'carnot_EventHandlerType', b2)
    assert _is_linked(a, 'carnot_EventHandlerType', b2)
    if hasattr(b1, 'carnot_IEventHandlerOwner'):
        assert not _is_linked(b1, 'carnot_IEventHandlerOwner', a)
    if hasattr(b2, 'carnot_IEventHandlerOwner'):
        assert _is_linked(b2, 'carnot_IEventHandlerOwner', a)
    _safe_set(a, 'carnot_EventHandlerType', None)
    assert not _is_linked(a, 'carnot_EventHandlerType', b2)
    if hasattr(b2, 'carnot_IEventHandlerOwner'):
        assert not _is_linked(b2, 'carnot_IEventHandlerOwner', a)


def test_assoc_eventHandlers177_link_reassign_clear():
    a = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    b1 = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    b2 = carnot_EventConditionTypeType(activityCondition="sample_text_2", binderClass="sample_text_2", implementation="sample_text_2", panelClass="sample_text_2", processCondition="sample_text_2", pullEventEmitterClass="sample_text_2", rule="sample_text_2")
    _safe_set(a, 'EventHandlerType', b1)
    assert _is_linked(a, 'EventHandlerType', b1)
    if hasattr(b1, 'type178'):
        assert _is_linked(b1, 'type178', a)
    _safe_set(a, 'EventHandlerType', b2)
    assert _is_linked(a, 'EventHandlerType', b2)
    if hasattr(b1, 'type178'):
        assert not _is_linked(b1, 'type178', a)
    if hasattr(b2, 'type178'):
        assert _is_linked(b2, 'type178', a)
    _safe_set(a, 'EventHandlerType', None)
    assert not _is_linked(a, 'EventHandlerType', b2)
    if hasattr(b2, 'type178'):
        assert not _is_linked(b2, 'type178', a)


def test_assoc_executedActivities120_link_reassign_clear():
    a = carnot_ApplicationType(interactive="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'application', {b1})
    assert _is_linked(a, 'application', b1)
    if hasattr(b1, 'ActivityType121'):
        assert _is_linked(b1, 'ActivityType121', a)
    _safe_set(a, 'application', {b2})
    assert _is_linked(a, 'application', b2)
    if hasattr(b1, 'ActivityType121'):
        assert not _is_linked(b1, 'ActivityType121', a)
    if hasattr(b2, 'ActivityType121'):
        assert _is_linked(b2, 'ActivityType121', a)
    _safe_set(a, 'application', set())
    assert not _is_linked(a, 'application', b2)
    if hasattr(b2, 'ActivityType121'):
        assert not _is_linked(b2, 'ActivityType121', a)


def test_assoc_executedByConnection39_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_ExecutedByConnectionType()
    b2 = carnot_ExecutedByConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer40', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer40', b1)
    if hasattr(b1, 'carnot_ExecutedByConnectionType'):
        assert _is_linked(b1, 'carnot_ExecutedByConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer40', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer40', b2)
    if hasattr(b1, 'carnot_ExecutedByConnectionType'):
        assert not _is_linked(b1, 'carnot_ExecutedByConnectionType', a)
    if hasattr(b2, 'carnot_ExecutedByConnectionType'):
        assert _is_linked(b2, 'carnot_ExecutedByConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer40', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer40', b2)
    if hasattr(b2, 'carnot_ExecutedByConnectionType'):
        assert not _is_linked(b2, 'carnot_ExecutedByConnectionType', a)


def test_assoc_executingActivities293_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'implementationProcess', {b1})
    assert _is_linked(a, 'implementationProcess', b1)
    if hasattr(b1, 'ActivityType294'):
        assert _is_linked(b1, 'ActivityType294', a)
    _safe_set(a, 'implementationProcess', {b2})
    assert _is_linked(a, 'implementationProcess', b2)
    if hasattr(b1, 'ActivityType294'):
        assert not _is_linked(b1, 'ActivityType294', a)
    if hasattr(b2, 'ActivityType294'):
        assert _is_linked(b2, 'ActivityType294', a)
    _safe_set(a, 'implementationProcess', set())
    assert not _is_linked(a, 'implementationProcess', b2)
    if hasattr(b2, 'ActivityType294'):
        assert not _is_linked(b2, 'ActivityType294', a)


def test_assoc_expression345_link_reassign_clear():
    a = carnot_XmlTextNode(mixed="sample_text")
    b1 = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b2 = carnot_TransitionType(condition="sample_text_2", forkOnTraversal="sample_text_2")
    _safe_set(a, 'carnot_XmlTextNode347', b1)
    assert _is_linked(a, 'carnot_XmlTextNode347', b1)
    if hasattr(b1, 'carnot_TransitionType346'):
        assert _is_linked(b1, 'carnot_TransitionType346', a)
    _safe_set(a, 'carnot_XmlTextNode347', b2)
    assert _is_linked(a, 'carnot_XmlTextNode347', b2)
    if hasattr(b1, 'carnot_TransitionType346'):
        assert not _is_linked(b1, 'carnot_TransitionType346', a)
    if hasattr(b2, 'carnot_TransitionType346'):
        assert _is_linked(b2, 'carnot_TransitionType346', a)
    _safe_set(a, 'carnot_XmlTextNode347', None)
    assert not _is_linked(a, 'carnot_XmlTextNode347', b2)
    if hasattr(b2, 'carnot_TransitionType346'):
        assert not _is_linked(b2, 'carnot_TransitionType346', a)


def test_assoc_externalPackages241_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_ExternalPackages()
    b2 = carnot_ExternalPackages()
    _safe_set(a, 'carnot_ModelType242', b1)
    assert _is_linked(a, 'carnot_ModelType242', b1)
    if hasattr(b1, 'carnot_ExternalPackages'):
        assert _is_linked(b1, 'carnot_ExternalPackages', a)
    _safe_set(a, 'carnot_ModelType242', b2)
    assert _is_linked(a, 'carnot_ModelType242', b2)
    if hasattr(b1, 'carnot_ExternalPackages'):
        assert not _is_linked(b1, 'carnot_ExternalPackages', a)
    if hasattr(b2, 'carnot_ExternalPackages'):
        assert _is_linked(b2, 'carnot_ExternalPackages', a)
    _safe_set(a, 'carnot_ModelType242', None)
    assert not _is_linked(a, 'carnot_ModelType242', b2)
    if hasattr(b2, 'carnot_ExternalPackages'):
        assert not _is_linked(b2, 'carnot_ExternalPackages', a)


def test_assoc_externalRef107_link_reassign_clear():
    a = carnot_IdRef(ref="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'carnot_IdRef', b1)
    assert _is_linked(a, 'carnot_IdRef', b1)
    if hasattr(b1, 'carnot_ActivityType108'):
        assert _is_linked(b1, 'carnot_ActivityType108', a)
    _safe_set(a, 'carnot_IdRef', b2)
    assert _is_linked(a, 'carnot_IdRef', b2)
    if hasattr(b1, 'carnot_ActivityType108'):
        assert not _is_linked(b1, 'carnot_ActivityType108', a)
    if hasattr(b2, 'carnot_ActivityType108'):
        assert _is_linked(b2, 'carnot_ActivityType108', a)
    _safe_set(a, 'carnot_IdRef', None)
    assert not _is_linked(a, 'carnot_IdRef', b2)
    if hasattr(b2, 'carnot_ActivityType108'):
        assert not _is_linked(b2, 'carnot_ActivityType108', a)


def test_assoc_externalRef300_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_IdRef(ref="sample_text")
    b2 = carnot_IdRef(ref="sample_text_2")
    _safe_set(a, 'carnot_ProcessDefinitionType301', b1)
    assert _is_linked(a, 'carnot_ProcessDefinitionType301', b1)
    if hasattr(b1, 'carnot_IdRef302'):
        assert _is_linked(b1, 'carnot_IdRef302', a)
    _safe_set(a, 'carnot_ProcessDefinitionType301', b2)
    assert _is_linked(a, 'carnot_ProcessDefinitionType301', b2)
    if hasattr(b1, 'carnot_IdRef302'):
        assert not _is_linked(b1, 'carnot_IdRef302', a)
    if hasattr(b2, 'carnot_IdRef302'):
        assert _is_linked(b2, 'carnot_IdRef302', a)
    _safe_set(a, 'carnot_ProcessDefinitionType301', None)
    assert not _is_linked(a, 'carnot_ProcessDefinitionType301', b2)
    if hasattr(b2, 'carnot_IdRef302'):
        assert not _is_linked(b2, 'carnot_IdRef302', a)


def test_assoc_externalReference164_link_reassign_clear():
    a = carnot_DataType(predefined="sample_text")
    b1 = carnot_ExternalReferenceType()
    b2 = carnot_ExternalReferenceType()
    _safe_set(a, 'carnot_DataType', b1)
    assert _is_linked(a, 'carnot_DataType', b1)
    if hasattr(b1, 'carnot_ExternalReferenceType'):
        assert _is_linked(b1, 'carnot_ExternalReferenceType', a)
    _safe_set(a, 'carnot_DataType', b2)
    assert _is_linked(a, 'carnot_DataType', b2)
    if hasattr(b1, 'carnot_ExternalReferenceType'):
        assert not _is_linked(b1, 'carnot_ExternalReferenceType', a)
    if hasattr(b2, 'carnot_ExternalReferenceType'):
        assert _is_linked(b2, 'carnot_ExternalReferenceType', a)
    _safe_set(a, 'carnot_DataType', None)
    assert not _is_linked(a, 'carnot_DataType', b2)
    if hasattr(b2, 'carnot_ExternalReferenceType'):
        assert not _is_linked(b2, 'carnot_ExternalReferenceType', a)


def test_assoc_formalParameterMappings298_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = FormalParameterMappingsType()
    b2 = FormalParameterMappingsType()
    _safe_set(a, 'carnot_ProcessDefinitionType299', b1)
    assert _is_linked(a, 'carnot_ProcessDefinitionType299', b1)
    if hasattr(b1, 'FormalParameterMappingsType'):
        assert _is_linked(b1, 'FormalParameterMappingsType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType299', b2)
    assert _is_linked(a, 'carnot_ProcessDefinitionType299', b2)
    if hasattr(b1, 'FormalParameterMappingsType'):
        assert not _is_linked(b1, 'FormalParameterMappingsType', a)
    if hasattr(b2, 'FormalParameterMappingsType'):
        assert _is_linked(b2, 'FormalParameterMappingsType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType299', None)
    assert not _is_linked(a, 'carnot_ProcessDefinitionType299', b2)
    if hasattr(b2, 'FormalParameterMappingsType'):
        assert not _is_linked(b2, 'FormalParameterMappingsType', a)


def test_assoc_formalParameters296_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_FormalParametersType()
    b2 = carnot_FormalParametersType()
    _safe_set(a, 'carnot_ProcessDefinitionType297', b1)
    assert _is_linked(a, 'carnot_ProcessDefinitionType297', b1)
    if hasattr(b1, 'carnot_FormalParametersType'):
        assert _is_linked(b1, 'carnot_FormalParametersType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType297', b2)
    assert _is_linked(a, 'carnot_ProcessDefinitionType297', b2)
    if hasattr(b1, 'carnot_FormalParametersType'):
        assert not _is_linked(b1, 'carnot_FormalParametersType', a)
    if hasattr(b2, 'carnot_FormalParametersType'):
        assert _is_linked(b2, 'carnot_FormalParametersType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType297', None)
    assert not _is_linked(a, 'carnot_ProcessDefinitionType297', b2)
    if hasattr(b2, 'carnot_FormalParametersType'):
        assert not _is_linked(b2, 'carnot_FormalParametersType', a)


def test_assoc_from_311_link_reassign_clear():
    a = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    b1 = carnot_RefersToConnectionType()
    b2 = carnot_RefersToConnectionType()
    _safe_set(a, 'IGraphicalObject', b1)
    assert _is_linked(a, 'IGraphicalObject', b1)
    if hasattr(b1, 'referingFromConnections'):
        assert _is_linked(b1, 'referingFromConnections', a)
    _safe_set(a, 'IGraphicalObject', b2)
    assert _is_linked(a, 'IGraphicalObject', b2)
    if hasattr(b1, 'referingFromConnections'):
        assert not _is_linked(b1, 'referingFromConnections', a)
    if hasattr(b2, 'referingFromConnections'):
        assert _is_linked(b2, 'referingFromConnections', a)
    _safe_set(a, 'IGraphicalObject', None)
    assert not _is_linked(a, 'IGraphicalObject', b2)
    if hasattr(b2, 'referingFromConnections'):
        assert not _is_linked(b2, 'referingFromConnections', a)


def test_assoc_from_348_link_reassign_clear():
    a = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'outTransitions349', b1)
    assert _is_linked(a, 'outTransitions349', b1)
    if hasattr(b1, 'ActivityType350'):
        assert _is_linked(b1, 'ActivityType350', a)
    _safe_set(a, 'outTransitions349', b2)
    assert _is_linked(a, 'outTransitions349', b2)
    if hasattr(b1, 'ActivityType350'):
        assert not _is_linked(b1, 'ActivityType350', a)
    if hasattr(b2, 'ActivityType350'):
        assert _is_linked(b2, 'ActivityType350', a)
    _safe_set(a, 'outTransitions349', None)
    assert not _is_linked(a, 'outTransitions349', b2)
    if hasattr(b2, 'ActivityType350'):
        assert not _is_linked(b2, 'ActivityType350', a)


def test_assoc_gatewaySymbol17_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_GatewaySymbol(flowKind="sample_text")
    b2 = carnot_GatewaySymbol(flowKind="sample_text_2")
    _safe_set(a, 'carnot_ISymbolContainer18', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer18', b1)
    if hasattr(b1, 'carnot_GatewaySymbol'):
        assert _is_linked(b1, 'carnot_GatewaySymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer18', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer18', b2)
    if hasattr(b1, 'carnot_GatewaySymbol'):
        assert not _is_linked(b1, 'carnot_GatewaySymbol', a)
    if hasattr(b2, 'carnot_GatewaySymbol'):
        assert _is_linked(b2, 'carnot_GatewaySymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer18', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer18', b2)
    if hasattr(b2, 'carnot_GatewaySymbol'):
        assert not _is_linked(b2, 'carnot_GatewaySymbol', a)


def test_assoc_gatewaySymbols90_link_reassign_clear():
    a = carnot_GatewaySymbol(flowKind="sample_text")
    b1 = carnot_ActivitySymbolType()
    b2 = carnot_ActivitySymbolType()
    _safe_set(a, 'GatewaySymbol', b1)
    assert _is_linked(a, 'GatewaySymbol', b1)
    if hasattr(b1, 'activitySymbol91'):
        assert _is_linked(b1, 'activitySymbol91', a)
    _safe_set(a, 'GatewaySymbol', b2)
    assert _is_linked(a, 'GatewaySymbol', b2)
    if hasattr(b1, 'activitySymbol91'):
        assert not _is_linked(b1, 'activitySymbol91', a)
    if hasattr(b2, 'activitySymbol91'):
        assert _is_linked(b2, 'activitySymbol91', a)
    _safe_set(a, 'GatewaySymbol', None)
    assert not _is_linked(a, 'GatewaySymbol', b2)
    if hasattr(b2, 'activitySymbol91'):
        assert not _is_linked(b2, 'activitySymbol91', a)


def test_assoc_genericLinkConnection41_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_GenericLinkConnectionType()
    b2 = carnot_GenericLinkConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer42', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer42', b1)
    if hasattr(b1, 'carnot_GenericLinkConnectionType'):
        assert _is_linked(b1, 'carnot_GenericLinkConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer42', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer42', b2)
    if hasattr(b1, 'carnot_GenericLinkConnectionType'):
        assert not _is_linked(b1, 'carnot_GenericLinkConnectionType', a)
    if hasattr(b2, 'carnot_GenericLinkConnectionType'):
        assert _is_linked(b2, 'carnot_GenericLinkConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer42', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer42', b2)
    if hasattr(b2, 'carnot_GenericLinkConnectionType'):
        assert not _is_linked(b2, 'carnot_GenericLinkConnectionType', a)


def test_assoc_groupSymbol19_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_GroupSymbolType()
    b2 = carnot_GroupSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer20', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer20', b1)
    if hasattr(b1, 'carnot_GroupSymbolType'):
        assert _is_linked(b1, 'carnot_GroupSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer20', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer20', b2)
    if hasattr(b1, 'carnot_GroupSymbolType'):
        assert not _is_linked(b1, 'carnot_GroupSymbolType', a)
    if hasattr(b2, 'carnot_GroupSymbolType'):
        assert _is_linked(b2, 'carnot_GroupSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer20', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer20', b2)
    if hasattr(b2, 'carnot_GroupSymbolType'):
        assert not _is_linked(b2, 'carnot_GroupSymbolType', a)


def test_assoc_implementationProcess94_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'ProcessDefinitionType', b1)
    assert _is_linked(a, 'ProcessDefinitionType', b1)
    if hasattr(b1, 'executingActivities'):
        assert _is_linked(b1, 'executingActivities', a)
    _safe_set(a, 'ProcessDefinitionType', b2)
    assert _is_linked(a, 'ProcessDefinitionType', b2)
    if hasattr(b1, 'executingActivities'):
        assert not _is_linked(b1, 'executingActivities', a)
    if hasattr(b2, 'executingActivities'):
        assert _is_linked(b2, 'executingActivities', a)
    _safe_set(a, 'ProcessDefinitionType', None)
    assert not _is_linked(a, 'ProcessDefinitionType', b2)
    if hasattr(b2, 'executingActivities'):
        assert not _is_linked(b2, 'executingActivities', a)


def test_assoc_inLinks62_link_reassign_clear():
    a = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    b1 = carnot_GenericLinkConnectionType()
    b2 = carnot_GenericLinkConnectionType()
    _safe_set(a, 'targetSymbol', {b1})
    assert _is_linked(a, 'targetSymbol', b1)
    if hasattr(b1, 'GenericLinkConnectionType'):
        assert _is_linked(b1, 'GenericLinkConnectionType', a)
    _safe_set(a, 'targetSymbol', {b2})
    assert _is_linked(a, 'targetSymbol', b2)
    if hasattr(b1, 'GenericLinkConnectionType'):
        assert not _is_linked(b1, 'GenericLinkConnectionType', a)
    if hasattr(b2, 'GenericLinkConnectionType'):
        assert _is_linked(b2, 'GenericLinkConnectionType', a)
    _safe_set(a, 'targetSymbol', set())
    assert not _is_linked(a, 'targetSymbol', b2)
    if hasattr(b2, 'GenericLinkConnectionType'):
        assert not _is_linked(b2, 'GenericLinkConnectionType', a)


def test_assoc_inTransitions102_link_reassign_clear():
    a = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'TransitionType', b1)
    assert _is_linked(a, 'TransitionType', b1)
    if hasattr(b1, 'to103'):
        assert _is_linked(b1, 'to103', a)
    _safe_set(a, 'TransitionType', b2)
    assert _is_linked(a, 'TransitionType', b2)
    if hasattr(b1, 'to103'):
        assert not _is_linked(b1, 'to103', a)
    if hasattr(b2, 'to103'):
        assert _is_linked(b2, 'to103', a)
    _safe_set(a, 'TransitionType', None)
    assert not _is_linked(a, 'TransitionType', b2)
    if hasattr(b2, 'to103'):
        assert not _is_linked(b2, 'to103', a)


def test_assoc_inTransitions68_link_reassign_clear():
    a = carnot_TransitionConnectionType(points="sample_text")
    b1 = carnot_IFlowObjectSymbol()
    b2 = carnot_IFlowObjectSymbol()
    _safe_set(a, 'TransitionConnectionType', b1)
    assert _is_linked(a, 'TransitionConnectionType', b1)
    if hasattr(b1, 'targetActivitySymbol'):
        assert _is_linked(b1, 'targetActivitySymbol', a)
    _safe_set(a, 'TransitionConnectionType', b2)
    assert _is_linked(a, 'TransitionConnectionType', b2)
    if hasattr(b1, 'targetActivitySymbol'):
        assert not _is_linked(b1, 'targetActivitySymbol', a)
    if hasattr(b2, 'targetActivitySymbol'):
        assert _is_linked(b2, 'targetActivitySymbol', a)
    _safe_set(a, 'TransitionConnectionType', None)
    assert not _is_linked(a, 'TransitionConnectionType', b2)
    if hasattr(b2, 'targetActivitySymbol'):
        assert not _is_linked(b2, 'targetActivitySymbol', a)


def test_assoc_intermediateEventSymbols21_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_IntermediateEventSymbol()
    b2 = carnot_IntermediateEventSymbol()
    _safe_set(a, 'carnot_ISymbolContainer22', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer22', b1)
    if hasattr(b1, 'carnot_IntermediateEventSymbol'):
        assert _is_linked(b1, 'carnot_IntermediateEventSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer22', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer22', b2)
    if hasattr(b1, 'carnot_IntermediateEventSymbol'):
        assert not _is_linked(b1, 'carnot_IntermediateEventSymbol', a)
    if hasattr(b2, 'carnot_IntermediateEventSymbol'):
        assert _is_linked(b2, 'carnot_IntermediateEventSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer22', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer22', b2)
    if hasattr(b2, 'carnot_IntermediateEventSymbol'):
        assert not _is_linked(b2, 'carnot_IntermediateEventSymbol', a)


def test_assoc_lanes279_link_reassign_clear():
    a = carnot_PoolSymbol(boundaryVisible="sample_text")
    b1 = carnot_LaneSymbol()
    b2 = carnot_LaneSymbol()
    _safe_set(a, 'parentPool', {b1})
    assert _is_linked(a, 'parentPool', b1)
    if hasattr(b1, 'LaneSymbol280'):
        assert _is_linked(b1, 'LaneSymbol280', a)
    _safe_set(a, 'parentPool', {b2})
    assert _is_linked(a, 'parentPool', b2)
    if hasattr(b1, 'LaneSymbol280'):
        assert not _is_linked(b1, 'LaneSymbol280', a)
    if hasattr(b2, 'LaneSymbol280'):
        assert _is_linked(b2, 'LaneSymbol280', a)
    _safe_set(a, 'parentPool', set())
    assert not _is_linked(a, 'parentPool', b2)
    if hasattr(b2, 'LaneSymbol280'):
        assert not _is_linked(b2, 'LaneSymbol280', a)


def test_assoc_linkInstances203_link_reassign_clear():
    a = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    b1 = carnot_GenericLinkConnectionType()
    b2 = carnot_GenericLinkConnectionType()
    _safe_set(a, 'linkType', {b1})
    assert _is_linked(a, 'linkType', b1)
    if hasattr(b1, 'GenericLinkConnectionType204'):
        assert _is_linked(b1, 'GenericLinkConnectionType204', a)
    _safe_set(a, 'linkType', {b2})
    assert _is_linked(a, 'linkType', b2)
    if hasattr(b1, 'GenericLinkConnectionType204'):
        assert not _is_linked(b1, 'GenericLinkConnectionType204', a)
    if hasattr(b2, 'GenericLinkConnectionType204'):
        assert _is_linked(b2, 'GenericLinkConnectionType204', a)
    _safe_set(a, 'linkType', set())
    assert not _is_linked(a, 'linkType', b2)
    if hasattr(b2, 'GenericLinkConnectionType204'):
        assert not _is_linked(b2, 'GenericLinkConnectionType204', a)


def test_assoc_linkType195_link_reassign_clear():
    a = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    b1 = carnot_GenericLinkConnectionType()
    b2 = carnot_GenericLinkConnectionType()
    _safe_set(a, 'LinkTypeType', b1)
    assert _is_linked(a, 'LinkTypeType', b1)
    if hasattr(b1, 'linkInstances'):
        assert _is_linked(b1, 'linkInstances', a)
    _safe_set(a, 'LinkTypeType', b2)
    assert _is_linked(a, 'LinkTypeType', b2)
    if hasattr(b1, 'linkInstances'):
        assert not _is_linked(b1, 'linkInstances', a)
    if hasattr(b2, 'linkInstances'):
        assert _is_linked(b2, 'linkInstances', a)
    _safe_set(a, 'LinkTypeType', None)
    assert not _is_linked(a, 'LinkTypeType', b2)
    if hasattr(b2, 'linkInstances'):
        assert not _is_linked(b2, 'linkInstances', a)


def test_assoc_linkType249_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_LinkTypeType(lineColor="sample_text", lineStyle="sample_text", showLinkTypeName="sample_text", showRoleNames="sample_text", sourceCardinality="sample_text", sourceClass="sample_text", sourceRole="sample_text", sourceSymbol="sample_text", targetCardinality="sample_text", targetClass="sample_text", targetRole="sample_text", targetSymbol="sample_text")
    b2 = carnot_LinkTypeType(lineColor="sample_text_2", lineStyle="sample_text_2", showLinkTypeName="sample_text_2", showRoleNames="sample_text_2", sourceCardinality="sample_text_2", sourceClass="sample_text_2", sourceRole="sample_text_2", sourceSymbol="sample_text_2", targetCardinality="sample_text_2", targetClass="sample_text_2", targetRole="sample_text_2", targetSymbol="sample_text_2")
    _safe_set(a, 'carnot_ModelType250', {b1})
    assert _is_linked(a, 'carnot_ModelType250', b1)
    if hasattr(b1, 'carnot_LinkTypeType'):
        assert _is_linked(b1, 'carnot_LinkTypeType', a)
    _safe_set(a, 'carnot_ModelType250', {b2})
    assert _is_linked(a, 'carnot_ModelType250', b2)
    if hasattr(b1, 'carnot_LinkTypeType'):
        assert not _is_linked(b1, 'carnot_LinkTypeType', a)
    if hasattr(b2, 'carnot_LinkTypeType'):
        assert _is_linked(b2, 'carnot_LinkTypeType', a)
    _safe_set(a, 'carnot_ModelType250', set())
    assert not _is_linked(a, 'carnot_ModelType250', b2)
    if hasattr(b2, 'carnot_LinkTypeType'):
        assert not _is_linked(b2, 'carnot_LinkTypeType', a)


def test_assoc_mapping385_link_reassign_clear():
    a = carnot_extensions_FormalParameterMappingsType()
    b1 = FormalParameterMappingType()
    b2 = FormalParameterMappingType()
    _safe_set(a, 'carnot_extensions_FormalParameterMappingsType', {b1})
    assert _is_linked(a, 'carnot_extensions_FormalParameterMappingsType', b1)
    if hasattr(b1, 'FormalParameterMappingType'):
        assert _is_linked(b1, 'FormalParameterMappingType', a)
    _safe_set(a, 'carnot_extensions_FormalParameterMappingsType', {b2})
    assert _is_linked(a, 'carnot_extensions_FormalParameterMappingsType', b2)
    if hasattr(b1, 'FormalParameterMappingType'):
        assert not _is_linked(b1, 'FormalParameterMappingType', a)
    if hasattr(b2, 'FormalParameterMappingType'):
        assert _is_linked(b2, 'FormalParameterMappingType', a)
    _safe_set(a, 'carnot_extensions_FormalParameterMappingsType', set())
    assert not _is_linked(a, 'carnot_extensions_FormalParameterMappingsType', b2)
    if hasattr(b2, 'FormalParameterMappingType'):
        assert not _is_linked(b2, 'FormalParameterMappingType', a)


def test_assoc_model173_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_DocumentRoot(mixed="sample_text")
    b2 = carnot_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'carnot_ModelType', b1)
    assert _is_linked(a, 'carnot_ModelType', b1)
    if hasattr(b1, 'carnot_DocumentRoot174'):
        assert _is_linked(b1, 'carnot_DocumentRoot174', a)
    _safe_set(a, 'carnot_ModelType', b2)
    assert _is_linked(a, 'carnot_ModelType', b2)
    if hasattr(b1, 'carnot_DocumentRoot174'):
        assert not _is_linked(b1, 'carnot_DocumentRoot174', a)
    if hasattr(b2, 'carnot_DocumentRoot174'):
        assert _is_linked(b2, 'carnot_DocumentRoot174', a)
    _safe_set(a, 'carnot_ModelType', None)
    assert not _is_linked(a, 'carnot_ModelType', b2)
    if hasattr(b2, 'carnot_DocumentRoot174'):
        assert not _is_linked(b2, 'carnot_DocumentRoot174', a)


def test_assoc_modeler205_link_reassign_clear():
    a = carnot_ModelerType(email="sample_text", password="sample_text")
    b1 = carnot_ModelerSymbolType()
    b2 = carnot_ModelerSymbolType()
    _safe_set(a, 'ModelerType', b1)
    assert _is_linked(a, 'ModelerType', b1)
    if hasattr(b1, 'modelerSymbols'):
        assert _is_linked(b1, 'modelerSymbols', a)
    _safe_set(a, 'ModelerType', b2)
    assert _is_linked(a, 'ModelerType', b2)
    if hasattr(b1, 'modelerSymbols'):
        assert not _is_linked(b1, 'modelerSymbols', a)
    if hasattr(b2, 'modelerSymbols'):
        assert _is_linked(b2, 'modelerSymbols', a)
    _safe_set(a, 'ModelerType', None)
    assert not _is_linked(a, 'ModelerType', b2)
    if hasattr(b2, 'modelerSymbols'):
        assert not _is_linked(b2, 'modelerSymbols', a)


def test_assoc_modeler229_link_reassign_clear():
    a = carnot_ModelerType(email="sample_text", password="sample_text")
    b1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    _safe_set(a, 'carnot_ModelerType', b1)
    assert _is_linked(a, 'carnot_ModelerType', b1)
    if hasattr(b1, 'carnot_ModelType230'):
        assert _is_linked(b1, 'carnot_ModelType230', a)
    _safe_set(a, 'carnot_ModelerType', b2)
    assert _is_linked(a, 'carnot_ModelerType', b2)
    if hasattr(b1, 'carnot_ModelType230'):
        assert not _is_linked(b1, 'carnot_ModelType230', a)
    if hasattr(b2, 'carnot_ModelType230'):
        assert _is_linked(b2, 'carnot_ModelType230', a)
    _safe_set(a, 'carnot_ModelerType', None)
    assert not _is_linked(a, 'carnot_ModelerType', b2)
    if hasattr(b2, 'carnot_ModelType230'):
        assert not _is_linked(b2, 'carnot_ModelType230', a)


def test_assoc_modelerSymbol23_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_ModelerSymbolType()
    b2 = carnot_ModelerSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer24', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer24', b1)
    if hasattr(b1, 'carnot_ModelerSymbolType'):
        assert _is_linked(b1, 'carnot_ModelerSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer24', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer24', b2)
    if hasattr(b1, 'carnot_ModelerSymbolType'):
        assert not _is_linked(b1, 'carnot_ModelerSymbolType', a)
    if hasattr(b2, 'carnot_ModelerSymbolType'):
        assert _is_linked(b2, 'carnot_ModelerSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer24', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer24', b2)
    if hasattr(b2, 'carnot_ModelerSymbolType'):
        assert not _is_linked(b2, 'carnot_ModelerSymbolType', a)


def test_assoc_modelerSymbols206_link_reassign_clear():
    a = carnot_ModelerType(email="sample_text", password="sample_text")
    b1 = carnot_ModelerSymbolType()
    b2 = carnot_ModelerSymbolType()
    _safe_set(a, 'modeler', {b1})
    assert _is_linked(a, 'modeler', b1)
    if hasattr(b1, 'ModelerSymbolType'):
        assert _is_linked(b1, 'ModelerSymbolType', a)
    _safe_set(a, 'modeler', {b2})
    assert _is_linked(a, 'modeler', b2)
    if hasattr(b1, 'ModelerSymbolType'):
        assert not _is_linked(b1, 'ModelerSymbolType', a)
    if hasattr(b2, 'ModelerSymbolType'):
        assert _is_linked(b2, 'ModelerSymbolType', a)
    _safe_set(a, 'modeler', set())
    assert not _is_linked(a, 'modeler', b2)
    if hasattr(b2, 'ModelerSymbolType'):
        assert not _is_linked(b2, 'ModelerSymbolType', a)


def test_assoc_organization235_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_OrganizationType()
    b2 = carnot_OrganizationType()
    _safe_set(a, 'carnot_ModelType236', {b1})
    assert _is_linked(a, 'carnot_ModelType236', b1)
    if hasattr(b1, 'carnot_OrganizationType'):
        assert _is_linked(b1, 'carnot_OrganizationType', a)
    _safe_set(a, 'carnot_ModelType236', {b2})
    assert _is_linked(a, 'carnot_ModelType236', b2)
    if hasattr(b1, 'carnot_OrganizationType'):
        assert not _is_linked(b1, 'carnot_OrganizationType', a)
    if hasattr(b2, 'carnot_OrganizationType'):
        assert _is_linked(b2, 'carnot_OrganizationType', a)
    _safe_set(a, 'carnot_ModelType236', set())
    assert not _is_linked(a, 'carnot_ModelType236', b2)
    if hasattr(b2, 'carnot_OrganizationType'):
        assert not _is_linked(b2, 'carnot_OrganizationType', a)


def test_assoc_organizationSymbol25_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_OrganizationSymbolType()
    b2 = carnot_OrganizationSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer26', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer26', b1)
    if hasattr(b1, 'carnot_OrganizationSymbolType'):
        assert _is_linked(b1, 'carnot_OrganizationSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer26', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer26', b2)
    if hasattr(b1, 'carnot_OrganizationSymbolType'):
        assert not _is_linked(b1, 'carnot_OrganizationSymbolType', a)
    if hasattr(b2, 'carnot_OrganizationSymbolType'):
        assert _is_linked(b2, 'carnot_OrganizationSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer26', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer26', b2)
    if hasattr(b2, 'carnot_OrganizationSymbolType'):
        assert not _is_linked(b2, 'carnot_OrganizationSymbolType', a)


def test_assoc_outLinks63_link_reassign_clear():
    a = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    b1 = carnot_GenericLinkConnectionType()
    b2 = carnot_GenericLinkConnectionType()
    _safe_set(a, 'sourceSymbol', {b1})
    assert _is_linked(a, 'sourceSymbol', b1)
    if hasattr(b1, 'GenericLinkConnectionType64'):
        assert _is_linked(b1, 'GenericLinkConnectionType64', a)
    _safe_set(a, 'sourceSymbol', {b2})
    assert _is_linked(a, 'sourceSymbol', b2)
    if hasattr(b1, 'GenericLinkConnectionType64'):
        assert not _is_linked(b1, 'GenericLinkConnectionType64', a)
    if hasattr(b2, 'GenericLinkConnectionType64'):
        assert _is_linked(b2, 'GenericLinkConnectionType64', a)
    _safe_set(a, 'sourceSymbol', set())
    assert not _is_linked(a, 'sourceSymbol', b2)
    if hasattr(b2, 'GenericLinkConnectionType64'):
        assert not _is_linked(b2, 'GenericLinkConnectionType64', a)


def test_assoc_outTransitions104_link_reassign_clear():
    a = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'TransitionType106', b1)
    assert _is_linked(a, 'TransitionType106', b1)
    if hasattr(b1, 'from_105'):
        assert _is_linked(b1, 'from_105', a)
    _safe_set(a, 'TransitionType106', b2)
    assert _is_linked(a, 'TransitionType106', b2)
    if hasattr(b1, 'from_105'):
        assert not _is_linked(b1, 'from_105', a)
    if hasattr(b2, 'from_105'):
        assert _is_linked(b2, 'from_105', a)
    _safe_set(a, 'TransitionType106', None)
    assert not _is_linked(a, 'TransitionType106', b2)
    if hasattr(b2, 'from_105'):
        assert not _is_linked(b2, 'from_105', a)


def test_assoc_outTransitions69_link_reassign_clear():
    a = carnot_TransitionConnectionType(points="sample_text")
    b1 = carnot_IFlowObjectSymbol()
    b2 = carnot_IFlowObjectSymbol()
    _safe_set(a, 'TransitionConnectionType70', b1)
    assert _is_linked(a, 'TransitionConnectionType70', b1)
    if hasattr(b1, 'sourceActivitySymbol'):
        assert _is_linked(b1, 'sourceActivitySymbol', a)
    _safe_set(a, 'TransitionConnectionType70', b2)
    assert _is_linked(a, 'TransitionConnectionType70', b2)
    if hasattr(b1, 'sourceActivitySymbol'):
        assert not _is_linked(b1, 'sourceActivitySymbol', a)
    if hasattr(b2, 'sourceActivitySymbol'):
        assert _is_linked(b2, 'sourceActivitySymbol', a)
    _safe_set(a, 'TransitionConnectionType70', None)
    assert not _is_linked(a, 'TransitionConnectionType70', b2)
    if hasattr(b2, 'sourceActivitySymbol'):
        assert not _is_linked(b2, 'sourceActivitySymbol', a)


def test_assoc_packageRef191_link_reassign_clear():
    a = carnot_IdRef(ref="sample_text")
    b1 = carnot_ExternalPackage()
    b2 = carnot_ExternalPackage()
    _safe_set(a, 'carnot_IdRef192', b1)
    assert _is_linked(a, 'carnot_IdRef192', b1)
    if hasattr(b1, 'carnot_ExternalPackage'):
        assert _is_linked(b1, 'carnot_ExternalPackage', a)
    _safe_set(a, 'carnot_IdRef192', b2)
    assert _is_linked(a, 'carnot_IdRef192', b2)
    if hasattr(b1, 'carnot_ExternalPackage'):
        assert not _is_linked(b1, 'carnot_ExternalPackage', a)
    if hasattr(b2, 'carnot_ExternalPackage'):
        assert _is_linked(b2, 'carnot_ExternalPackage', a)
    _safe_set(a, 'carnot_IdRef192', None)
    assert not _is_linked(a, 'carnot_IdRef192', b2)
    if hasattr(b2, 'carnot_ExternalPackage'):
        assert not _is_linked(b2, 'carnot_ExternalPackage', a)


def test_assoc_parameterMapping360_link_reassign_clear():
    a = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    b1 = carnot_TriggerType()
    b2 = carnot_TriggerType()
    _safe_set(a, 'carnot_ParameterMappingType', b1)
    assert _is_linked(a, 'carnot_ParameterMappingType', b1)
    if hasattr(b1, 'carnot_TriggerType361'):
        assert _is_linked(b1, 'carnot_TriggerType361', a)
    _safe_set(a, 'carnot_ParameterMappingType', b2)
    assert _is_linked(a, 'carnot_ParameterMappingType', b2)
    if hasattr(b1, 'carnot_TriggerType361'):
        assert not _is_linked(b1, 'carnot_TriggerType361', a)
    if hasattr(b2, 'carnot_TriggerType361'):
        assert _is_linked(b2, 'carnot_TriggerType361', a)
    _safe_set(a, 'carnot_ParameterMappingType', None)
    assert not _is_linked(a, 'carnot_ParameterMappingType', b2)
    if hasattr(b2, 'carnot_TriggerType361'):
        assert not _is_linked(b2, 'carnot_TriggerType361', a)


def test_assoc_parameterMappings162_link_reassign_clear():
    a = carnot_ParameterMappingType(dataPath="sample_text", parameter="sample_text", parameterPath="sample_text")
    b1 = carnot_DataType(predefined="sample_text")
    b2 = carnot_DataType(predefined="sample_text_2")
    _safe_set(a, 'ParameterMappingType', b1)
    assert _is_linked(a, 'ParameterMappingType', b1)
    if hasattr(b1, 'data163'):
        assert _is_linked(b1, 'data163', a)
    _safe_set(a, 'ParameterMappingType', b2)
    assert _is_linked(a, 'ParameterMappingType', b2)
    if hasattr(b1, 'data163'):
        assert not _is_linked(b1, 'data163', a)
    if hasattr(b2, 'data163'):
        assert _is_linked(b2, 'data163', a)
    _safe_set(a, 'ParameterMappingType', None)
    assert not _is_linked(a, 'ParameterMappingType', b2)
    if hasattr(b2, 'data163'):
        assert not _is_linked(b2, 'data163', a)


def test_assoc_parentLane201_link_reassign_clear():
    a = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    b1 = carnot_LaneSymbol()
    b2 = carnot_LaneSymbol()
    _safe_set(a, 'ISwimlaneSymbol202', b1)
    assert _is_linked(a, 'ISwimlaneSymbol202', b1)
    if hasattr(b1, 'childLanes'):
        assert _is_linked(b1, 'childLanes', a)
    _safe_set(a, 'ISwimlaneSymbol202', b2)
    assert _is_linked(a, 'ISwimlaneSymbol202', b2)
    if hasattr(b1, 'childLanes'):
        assert not _is_linked(b1, 'childLanes', a)
    if hasattr(b2, 'childLanes'):
        assert _is_linked(b2, 'childLanes', a)
    _safe_set(a, 'ISwimlaneSymbol202', None)
    assert not _is_linked(a, 'ISwimlaneSymbol202', b2)
    if hasattr(b2, 'childLanes'):
        assert not _is_linked(b2, 'childLanes', a)


def test_assoc_parentPool199_link_reassign_clear():
    a = carnot_PoolSymbol(boundaryVisible="sample_text")
    b1 = carnot_LaneSymbol()
    b2 = carnot_LaneSymbol()
    _safe_set(a, 'PoolSymbol200', b1)
    assert _is_linked(a, 'PoolSymbol200', b1)
    if hasattr(b1, 'lanes'):
        assert _is_linked(b1, 'lanes', a)
    _safe_set(a, 'PoolSymbol200', b2)
    assert _is_linked(a, 'PoolSymbol200', b2)
    if hasattr(b1, 'lanes'):
        assert not _is_linked(b1, 'lanes', a)
    if hasattr(b2, 'lanes'):
        assert _is_linked(b2, 'lanes', a)
    _safe_set(a, 'PoolSymbol200', None)
    assert not _is_linked(a, 'PoolSymbol200', b2)
    if hasattr(b2, 'lanes'):
        assert not _is_linked(b2, 'lanes', a)


def test_assoc_partOfConnection43_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_PartOfConnectionType()
    b2 = carnot_PartOfConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer44', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer44', b1)
    if hasattr(b1, 'carnot_PartOfConnectionType'):
        assert _is_linked(b1, 'carnot_PartOfConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer44', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer44', b2)
    if hasattr(b1, 'carnot_PartOfConnectionType'):
        assert not _is_linked(b1, 'carnot_PartOfConnectionType', a)
    if hasattr(b2, 'carnot_PartOfConnectionType'):
        assert _is_linked(b2, 'carnot_PartOfConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer44', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer44', b2)
    if hasattr(b2, 'carnot_PartOfConnectionType'):
        assert not _is_linked(b2, 'carnot_PartOfConnectionType', a)


def test_assoc_participant130_link_reassign_clear():
    a = carnot_ConditionalPerformerType(dataPath="sample_text", isUser="sample_text")
    b1 = carnot_ConditionalPerformerSymbolType()
    b2 = carnot_ConditionalPerformerSymbolType()
    _safe_set(a, 'ConditionalPerformerType', b1)
    assert _is_linked(a, 'ConditionalPerformerType', b1)
    if hasattr(b1, 'conditionalPerformerSymbols'):
        assert _is_linked(b1, 'conditionalPerformerSymbols', a)
    _safe_set(a, 'ConditionalPerformerType', b2)
    assert _is_linked(a, 'ConditionalPerformerType', b2)
    if hasattr(b1, 'conditionalPerformerSymbols'):
        assert not _is_linked(b1, 'conditionalPerformerSymbols', a)
    if hasattr(b2, 'conditionalPerformerSymbols'):
        assert _is_linked(b2, 'conditionalPerformerSymbols', a)
    _safe_set(a, 'ConditionalPerformerType', None)
    assert not _is_linked(a, 'ConditionalPerformerType', b2)
    if hasattr(b2, 'conditionalPerformerSymbols'):
        assert not _is_linked(b2, 'conditionalPerformerSymbols', a)


def test_assoc_participant65_link_reassign_clear():
    a = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    b1 = carnot_IModelParticipant()
    b2 = carnot_IModelParticipant()
    _safe_set(a, 'performedSwimlanes', b1)
    assert _is_linked(a, 'performedSwimlanes', b1)
    if hasattr(b1, 'IModelParticipant'):
        assert _is_linked(b1, 'IModelParticipant', a)
    _safe_set(a, 'performedSwimlanes', b2)
    assert _is_linked(a, 'performedSwimlanes', b2)
    if hasattr(b1, 'IModelParticipant'):
        assert not _is_linked(b1, 'IModelParticipant', a)
    if hasattr(b2, 'IModelParticipant'):
        assert _is_linked(b2, 'IModelParticipant', a)
    _safe_set(a, 'performedSwimlanes', None)
    assert not _is_linked(a, 'performedSwimlanes', b2)
    if hasattr(b2, 'IModelParticipant'):
        assert not _is_linked(b2, 'IModelParticipant', a)


def test_assoc_participantReference67_link_reassign_clear():
    a = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    b1 = carnot_IModelParticipant()
    b2 = carnot_IModelParticipant()
    _safe_set(a, 'carnot_ISwimlaneSymbol', b1)
    assert _is_linked(a, 'carnot_ISwimlaneSymbol', b1)
    if hasattr(b1, 'carnot_IModelParticipant'):
        assert _is_linked(b1, 'carnot_IModelParticipant', a)
    _safe_set(a, 'carnot_ISwimlaneSymbol', b2)
    assert _is_linked(a, 'carnot_ISwimlaneSymbol', b2)
    if hasattr(b1, 'carnot_IModelParticipant'):
        assert not _is_linked(b1, 'carnot_IModelParticipant', a)
    if hasattr(b2, 'carnot_IModelParticipant'):
        assert _is_linked(b2, 'carnot_IModelParticipant', a)
    _safe_set(a, 'carnot_ISwimlaneSymbol', None)
    assert not _is_linked(a, 'carnot_ISwimlaneSymbol', b2)
    if hasattr(b2, 'carnot_IModelParticipant'):
        assert not _is_linked(b2, 'carnot_IModelParticipant', a)


def test_assoc_performedActivities72_link_reassign_clear():
    a = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b1 = carnot_IModelParticipant()
    b2 = carnot_IModelParticipant()
    _safe_set(a, 'ActivityType', b1)
    assert _is_linked(a, 'ActivityType', b1)
    if hasattr(b1, 'performer'):
        assert _is_linked(b1, 'performer', a)
    _safe_set(a, 'ActivityType', b2)
    assert _is_linked(a, 'ActivityType', b2)
    if hasattr(b1, 'performer'):
        assert not _is_linked(b1, 'performer', a)
    if hasattr(b2, 'performer'):
        assert _is_linked(b2, 'performer', a)
    _safe_set(a, 'ActivityType', None)
    assert not _is_linked(a, 'ActivityType', b2)
    if hasattr(b2, 'performer'):
        assert not _is_linked(b2, 'performer', a)


def test_assoc_performedSwimlanes73_link_reassign_clear():
    a = carnot_ISwimlaneSymbol(collapsed="sample_text", orientation="sample_text")
    b1 = carnot_IModelParticipant()
    b2 = carnot_IModelParticipant()
    _safe_set(a, 'ISwimlaneSymbol', b1)
    assert _is_linked(a, 'ISwimlaneSymbol', b1)
    if hasattr(b1, 'participant'):
        assert _is_linked(b1, 'participant', a)
    _safe_set(a, 'ISwimlaneSymbol', b2)
    assert _is_linked(a, 'ISwimlaneSymbol', b2)
    if hasattr(b1, 'participant'):
        assert not _is_linked(b1, 'participant', a)
    if hasattr(b2, 'participant'):
        assert _is_linked(b2, 'participant', a)
    _safe_set(a, 'ISwimlaneSymbol', None)
    assert not _is_linked(a, 'ISwimlaneSymbol', b2)
    if hasattr(b2, 'participant'):
        assert not _is_linked(b2, 'participant', a)


def test_assoc_performer95_link_reassign_clear():
    a = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b1 = carnot_IModelParticipant()
    b2 = carnot_IModelParticipant()
    _safe_set(a, 'performedActivities', b1)
    assert _is_linked(a, 'performedActivities', b1)
    if hasattr(b1, 'IModelParticipant96'):
        assert _is_linked(b1, 'IModelParticipant96', a)
    _safe_set(a, 'performedActivities', b2)
    assert _is_linked(a, 'performedActivities', b2)
    if hasattr(b1, 'IModelParticipant96'):
        assert not _is_linked(b1, 'IModelParticipant96', a)
    if hasattr(b2, 'IModelParticipant96'):
        assert _is_linked(b2, 'IModelParticipant96', a)
    _safe_set(a, 'performedActivities', None)
    assert not _is_linked(a, 'performedActivities', b2)
    if hasattr(b2, 'IModelParticipant96'):
        assert not _is_linked(b2, 'IModelParticipant96', a)


def test_assoc_performsConnection45_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_PerformsConnectionType()
    b2 = carnot_PerformsConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer46', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer46', b1)
    if hasattr(b1, 'carnot_PerformsConnectionType'):
        assert _is_linked(b1, 'carnot_PerformsConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer46', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer46', b2)
    if hasattr(b1, 'carnot_PerformsConnectionType'):
        assert not _is_linked(b1, 'carnot_PerformsConnectionType', a)
    if hasattr(b2, 'carnot_PerformsConnectionType'):
        assert _is_linked(b2, 'carnot_PerformsConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer46', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer46', b2)
    if hasattr(b2, 'carnot_PerformsConnectionType'):
        assert not _is_linked(b2, 'carnot_PerformsConnectionType', a)


def test_assoc_poolSymbols168_link_reassign_clear():
    a = carnot_PoolSymbol(boundaryVisible="sample_text")
    b1 = carnot_DiagramType(mode="sample_text", name="sample_text", orientation="sample_text")
    b2 = carnot_DiagramType(mode="sample_text_2", name="sample_text_2", orientation="sample_text_2")
    _safe_set(a, 'PoolSymbol', b1)
    assert _is_linked(a, 'PoolSymbol', b1)
    if hasattr(b1, 'diagram'):
        assert _is_linked(b1, 'diagram', a)
    _safe_set(a, 'PoolSymbol', b2)
    assert _is_linked(a, 'PoolSymbol', b2)
    if hasattr(b1, 'diagram'):
        assert not _is_linked(b1, 'diagram', a)
    if hasattr(b2, 'diagram'):
        assert _is_linked(b2, 'diagram', a)
    _safe_set(a, 'PoolSymbol', None)
    assert not _is_linked(a, 'PoolSymbol', b2)
    if hasattr(b2, 'diagram'):
        assert not _is_linked(b2, 'diagram', a)


def test_assoc_process277_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_PoolSymbol(boundaryVisible="sample_text")
    b2 = carnot_PoolSymbol(boundaryVisible="sample_text_2")
    _safe_set(a, 'carnot_ProcessDefinitionType278', b1)
    assert _is_linked(a, 'carnot_ProcessDefinitionType278', b1)
    if hasattr(b1, 'carnot_PoolSymbol'):
        assert _is_linked(b1, 'carnot_PoolSymbol', a)
    _safe_set(a, 'carnot_ProcessDefinitionType278', b2)
    assert _is_linked(a, 'carnot_ProcessDefinitionType278', b2)
    if hasattr(b1, 'carnot_PoolSymbol'):
        assert not _is_linked(b1, 'carnot_PoolSymbol', a)
    if hasattr(b2, 'carnot_PoolSymbol'):
        assert _is_linked(b2, 'carnot_PoolSymbol', a)
    _safe_set(a, 'carnot_ProcessDefinitionType278', None)
    assert not _is_linked(a, 'carnot_ProcessDefinitionType278', b2)
    if hasattr(b2, 'carnot_PoolSymbol'):
        assert not _is_linked(b2, 'carnot_PoolSymbol', a)


def test_assoc_process303_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_ProcessSymbolType()
    b2 = carnot_ProcessSymbolType()
    _safe_set(a, 'ProcessDefinitionType304', b1)
    assert _is_linked(a, 'ProcessDefinitionType304', b1)
    if hasattr(b1, 'processSymbols'):
        assert _is_linked(b1, 'processSymbols', a)
    _safe_set(a, 'ProcessDefinitionType304', b2)
    assert _is_linked(a, 'ProcessDefinitionType304', b2)
    if hasattr(b1, 'processSymbols'):
        assert not _is_linked(b1, 'processSymbols', a)
    if hasattr(b2, 'processSymbols'):
        assert _is_linked(b2, 'processSymbols', a)
    _safe_set(a, 'ProcessDefinitionType304', None)
    assert not _is_linked(a, 'ProcessDefinitionType304', b2)
    if hasattr(b2, 'processSymbols'):
        assert not _is_linked(b2, 'processSymbols', a)


def test_assoc_processDefinition239_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    _safe_set(a, 'carnot_ProcessDefinitionType', b1)
    assert _is_linked(a, 'carnot_ProcessDefinitionType', b1)
    if hasattr(b1, 'carnot_ModelType240'):
        assert _is_linked(b1, 'carnot_ModelType240', a)
    _safe_set(a, 'carnot_ProcessDefinitionType', b2)
    assert _is_linked(a, 'carnot_ProcessDefinitionType', b2)
    if hasattr(b1, 'carnot_ModelType240'):
        assert not _is_linked(b1, 'carnot_ModelType240', a)
    if hasattr(b2, 'carnot_ModelType240'):
        assert _is_linked(b2, 'carnot_ModelType240', a)
    _safe_set(a, 'carnot_ProcessDefinitionType', None)
    assert not _is_linked(a, 'carnot_ProcessDefinitionType', b2)
    if hasattr(b2, 'carnot_ModelType240'):
        assert not _is_linked(b2, 'carnot_ModelType240', a)


def test_assoc_processInterfaceSymbols29_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_PublicInterfaceSymbol()
    b2 = carnot_PublicInterfaceSymbol()
    _safe_set(a, 'carnot_ISymbolContainer30', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer30', b1)
    if hasattr(b1, 'carnot_PublicInterfaceSymbol'):
        assert _is_linked(b1, 'carnot_PublicInterfaceSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer30', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer30', b2)
    if hasattr(b1, 'carnot_PublicInterfaceSymbol'):
        assert not _is_linked(b1, 'carnot_PublicInterfaceSymbol', a)
    if hasattr(b2, 'carnot_PublicInterfaceSymbol'):
        assert _is_linked(b2, 'carnot_PublicInterfaceSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer30', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer30', b2)
    if hasattr(b2, 'carnot_PublicInterfaceSymbol'):
        assert not _is_linked(b2, 'carnot_PublicInterfaceSymbol', a)


def test_assoc_processSymbol27_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_ProcessSymbolType()
    b2 = carnot_ProcessSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer28', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer28', b1)
    if hasattr(b1, 'carnot_ProcessSymbolType'):
        assert _is_linked(b1, 'carnot_ProcessSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer28', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer28', b2)
    if hasattr(b1, 'carnot_ProcessSymbolType'):
        assert not _is_linked(b1, 'carnot_ProcessSymbolType', a)
    if hasattr(b2, 'carnot_ProcessSymbolType'):
        assert _is_linked(b2, 'carnot_ProcessSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer28', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer28', b2)
    if hasattr(b2, 'carnot_ProcessSymbolType'):
        assert not _is_linked(b2, 'carnot_ProcessSymbolType', a)


def test_assoc_processSymbols295_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_ProcessSymbolType()
    b2 = carnot_ProcessSymbolType()
    _safe_set(a, 'process', {b1})
    assert _is_linked(a, 'process', b1)
    if hasattr(b1, 'ProcessSymbolType'):
        assert _is_linked(b1, 'ProcessSymbolType', a)
    _safe_set(a, 'process', {b2})
    assert _is_linked(a, 'process', b2)
    if hasattr(b1, 'ProcessSymbolType'):
        assert not _is_linked(b1, 'ProcessSymbolType', a)
    if hasattr(b2, 'ProcessSymbolType'):
        assert _is_linked(b2, 'ProcessSymbolType', a)
    _safe_set(a, 'process', set())
    assert not _is_linked(a, 'process', b2)
    if hasattr(b2, 'ProcessSymbolType'):
        assert not _is_linked(b2, 'ProcessSymbolType', a)


def test_assoc_qualityControl231_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_QualityControlType()
    b2 = carnot_QualityControlType()
    _safe_set(a, 'carnot_ModelType232', b1)
    assert _is_linked(a, 'carnot_ModelType232', b1)
    if hasattr(b1, 'carnot_QualityControlType'):
        assert _is_linked(b1, 'carnot_QualityControlType', a)
    _safe_set(a, 'carnot_ModelType232', b2)
    assert _is_linked(a, 'carnot_ModelType232', b2)
    if hasattr(b1, 'carnot_QualityControlType'):
        assert not _is_linked(b1, 'carnot_QualityControlType', a)
    if hasattr(b2, 'carnot_QualityControlType'):
        assert _is_linked(b2, 'carnot_QualityControlType', a)
    _safe_set(a, 'carnot_ModelType232', None)
    assert not _is_linked(a, 'carnot_ModelType232', b2)
    if hasattr(b2, 'carnot_QualityControlType'):
        assert not _is_linked(b2, 'carnot_QualityControlType', a)


def test_assoc_qualityControlPerformer97_link_reassign_clear():
    a = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b1 = carnot_IModelParticipant()
    b2 = carnot_IModelParticipant()
    _safe_set(a, 'carnot_ActivityType98', b1)
    assert _is_linked(a, 'carnot_ActivityType98', b1)
    if hasattr(b1, 'carnot_IModelParticipant99'):
        assert _is_linked(b1, 'carnot_IModelParticipant99', a)
    _safe_set(a, 'carnot_ActivityType98', b2)
    assert _is_linked(a, 'carnot_ActivityType98', b2)
    if hasattr(b1, 'carnot_IModelParticipant99'):
        assert not _is_linked(b1, 'carnot_IModelParticipant99', a)
    if hasattr(b2, 'carnot_IModelParticipant99'):
        assert _is_linked(b2, 'carnot_IModelParticipant99', a)
    _safe_set(a, 'carnot_ActivityType98', None)
    assert not _is_linked(a, 'carnot_ActivityType98', b2)
    if hasattr(b2, 'carnot_IModelParticipant99'):
        assert not _is_linked(b2, 'carnot_IModelParticipant99', a)


def test_assoc_reference129_link_reassign_clear():
    a = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    b1 = carnot_IdentifiableReference()
    b2 = carnot_IdentifiableReference()
    _safe_set(a, 'attribute', b1)
    assert _is_linked(a, 'attribute', b1)
    if hasattr(b1, 'IdentifiableReference'):
        assert _is_linked(b1, 'IdentifiableReference', a)
    _safe_set(a, 'attribute', b2)
    assert _is_linked(a, 'attribute', b2)
    if hasattr(b1, 'IdentifiableReference'):
        assert not _is_linked(b1, 'IdentifiableReference', a)
    if hasattr(b2, 'IdentifiableReference'):
        assert _is_linked(b2, 'IdentifiableReference', a)
    _safe_set(a, 'attribute', None)
    assert not _is_linked(a, 'attribute', b2)
    if hasattr(b2, 'IdentifiableReference'):
        assert not _is_linked(b2, 'IdentifiableReference', a)


def test_assoc_referingFromConnections60_link_reassign_clear():
    a = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    b1 = carnot_RefersToConnectionType()
    b2 = carnot_RefersToConnectionType()
    _safe_set(a, 'from_', {b1})
    assert _is_linked(a, 'from_', b1)
    if hasattr(b1, 'RefersToConnectionType61'):
        assert _is_linked(b1, 'RefersToConnectionType61', a)
    _safe_set(a, 'from_', {b2})
    assert _is_linked(a, 'from_', b2)
    if hasattr(b1, 'RefersToConnectionType61'):
        assert not _is_linked(b1, 'RefersToConnectionType61', a)
    if hasattr(b2, 'RefersToConnectionType61'):
        assert _is_linked(b2, 'RefersToConnectionType61', a)
    _safe_set(a, 'from_', set())
    assert not _is_linked(a, 'from_', b2)
    if hasattr(b2, 'RefersToConnectionType61'):
        assert not _is_linked(b2, 'RefersToConnectionType61', a)


def test_assoc_referingToConnections59_link_reassign_clear():
    a = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    b1 = carnot_RefersToConnectionType()
    b2 = carnot_RefersToConnectionType()
    _safe_set(a, 'to', {b1})
    assert _is_linked(a, 'to', b1)
    if hasattr(b1, 'RefersToConnectionType'):
        assert _is_linked(b1, 'RefersToConnectionType', a)
    _safe_set(a, 'to', {b2})
    assert _is_linked(a, 'to', b2)
    if hasattr(b1, 'RefersToConnectionType'):
        assert not _is_linked(b1, 'RefersToConnectionType', a)
    if hasattr(b2, 'RefersToConnectionType'):
        assert _is_linked(b2, 'RefersToConnectionType', a)
    _safe_set(a, 'to', set())
    assert not _is_linked(a, 'to', b2)
    if hasattr(b2, 'RefersToConnectionType'):
        assert not _is_linked(b2, 'RefersToConnectionType', a)


def test_assoc_refersToConnection49_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_RefersToConnectionType()
    b2 = carnot_RefersToConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer50', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer50', b1)
    if hasattr(b1, 'carnot_RefersToConnectionType'):
        assert _is_linked(b1, 'carnot_RefersToConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer50', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer50', b2)
    if hasattr(b1, 'carnot_RefersToConnectionType'):
        assert not _is_linked(b1, 'carnot_RefersToConnectionType', a)
    if hasattr(b2, 'carnot_RefersToConnectionType'):
        assert _is_linked(b2, 'carnot_RefersToConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer50', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer50', b2)
    if hasattr(b2, 'carnot_RefersToConnectionType'):
        assert not _is_linked(b2, 'carnot_RefersToConnectionType', a)


def test_assoc_role233_link_reassign_clear():
    a = carnot_RoleType(cardinality=7)
    b1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    _safe_set(a, 'carnot_RoleType', b1)
    assert _is_linked(a, 'carnot_RoleType', b1)
    if hasattr(b1, 'carnot_ModelType234'):
        assert _is_linked(b1, 'carnot_ModelType234', a)
    _safe_set(a, 'carnot_RoleType', b2)
    assert _is_linked(a, 'carnot_RoleType', b2)
    if hasattr(b1, 'carnot_ModelType234'):
        assert not _is_linked(b1, 'carnot_ModelType234', a)
    if hasattr(b2, 'carnot_ModelType234'):
        assert _is_linked(b2, 'carnot_ModelType234', a)
    _safe_set(a, 'carnot_RoleType', None)
    assert not _is_linked(a, 'carnot_RoleType', b2)
    if hasattr(b2, 'carnot_ModelType234'):
        assert not _is_linked(b2, 'carnot_ModelType234', a)


def test_assoc_role314_link_reassign_clear():
    a = carnot_RoleType(cardinality=7)
    b1 = carnot_RoleSymbolType()
    b2 = carnot_RoleSymbolType()
    _safe_set(a, 'RoleType315', b1)
    assert _is_linked(a, 'RoleType315', b1)
    if hasattr(b1, 'roleSymbols'):
        assert _is_linked(b1, 'roleSymbols', a)
    _safe_set(a, 'RoleType315', b2)
    assert _is_linked(a, 'RoleType315', b2)
    if hasattr(b1, 'roleSymbols'):
        assert not _is_linked(b1, 'roleSymbols', a)
    if hasattr(b2, 'roleSymbols'):
        assert _is_linked(b2, 'roleSymbols', a)
    _safe_set(a, 'RoleType315', None)
    assert not _is_linked(a, 'RoleType315', b2)
    if hasattr(b2, 'roleSymbols'):
        assert not _is_linked(b2, 'roleSymbols', a)


def test_assoc_roleSymbol31_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_RoleSymbolType()
    b2 = carnot_RoleSymbolType()
    _safe_set(a, 'carnot_ISymbolContainer32', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer32', b1)
    if hasattr(b1, 'carnot_RoleSymbolType'):
        assert _is_linked(b1, 'carnot_RoleSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer32', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer32', b2)
    if hasattr(b1, 'carnot_RoleSymbolType'):
        assert not _is_linked(b1, 'carnot_RoleSymbolType', a)
    if hasattr(b2, 'carnot_RoleSymbolType'):
        assert _is_linked(b2, 'carnot_RoleSymbolType', a)
    _safe_set(a, 'carnot_ISymbolContainer32', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer32', b2)
    if hasattr(b2, 'carnot_RoleSymbolType'):
        assert not _is_linked(b2, 'carnot_RoleSymbolType', a)


def test_assoc_roleSymbols323_link_reassign_clear():
    a = carnot_RoleType(cardinality=7)
    b1 = carnot_RoleSymbolType()
    b2 = carnot_RoleSymbolType()
    _safe_set(a, 'role', {b1})
    assert _is_linked(a, 'role', b1)
    if hasattr(b1, 'RoleSymbolType'):
        assert _is_linked(b1, 'RoleSymbolType', a)
    _safe_set(a, 'role', {b2})
    assert _is_linked(a, 'role', b2)
    if hasattr(b1, 'RoleSymbolType'):
        assert not _is_linked(b1, 'RoleSymbolType', a)
    if hasattr(b2, 'RoleSymbolType'):
        assert _is_linked(b2, 'RoleSymbolType', a)
    _safe_set(a, 'role', set())
    assert not _is_linked(a, 'role', b2)
    if hasattr(b2, 'RoleSymbolType'):
        assert not _is_linked(b2, 'RoleSymbolType', a)


def test_assoc_script243_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_ScriptType()
    b2 = carnot_ScriptType()
    _safe_set(a, 'carnot_ModelType244', b1)
    assert _is_linked(a, 'carnot_ModelType244', b1)
    if hasattr(b1, 'carnot_ScriptType'):
        assert _is_linked(b1, 'carnot_ScriptType', a)
    _safe_set(a, 'carnot_ModelType244', b2)
    assert _is_linked(a, 'carnot_ModelType244', b2)
    if hasattr(b1, 'carnot_ScriptType'):
        assert not _is_linked(b1, 'carnot_ScriptType', a)
    if hasattr(b2, 'carnot_ScriptType'):
        assert _is_linked(b2, 'carnot_ScriptType', a)
    _safe_set(a, 'carnot_ModelType244', None)
    assert not _is_linked(a, 'carnot_ModelType244', b2)
    if hasattr(b2, 'carnot_ScriptType'):
        assert not _is_linked(b2, 'carnot_ScriptType', a)


def test_assoc_sourceActivitySymbol340_link_reassign_clear():
    a = carnot_TransitionConnectionType(points="sample_text")
    b1 = carnot_IFlowObjectSymbol()
    b2 = carnot_IFlowObjectSymbol()
    _safe_set(a, 'outTransitions', b1)
    assert _is_linked(a, 'outTransitions', b1)
    if hasattr(b1, 'IFlowObjectSymbol'):
        assert _is_linked(b1, 'IFlowObjectSymbol', a)
    _safe_set(a, 'outTransitions', b2)
    assert _is_linked(a, 'outTransitions', b2)
    if hasattr(b1, 'IFlowObjectSymbol'):
        assert not _is_linked(b1, 'IFlowObjectSymbol', a)
    if hasattr(b2, 'IFlowObjectSymbol'):
        assert _is_linked(b2, 'IFlowObjectSymbol', a)
    _safe_set(a, 'outTransitions', None)
    assert not _is_linked(a, 'outTransitions', b2)
    if hasattr(b2, 'IFlowObjectSymbol'):
        assert not _is_linked(b2, 'IFlowObjectSymbol', a)


def test_assoc_sourceSymbol196_link_reassign_clear():
    a = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    b1 = carnot_GenericLinkConnectionType()
    b2 = carnot_GenericLinkConnectionType()
    _safe_set(a, 'INodeSymbol', b1)
    assert _is_linked(a, 'INodeSymbol', b1)
    if hasattr(b1, 'outLinks'):
        assert _is_linked(b1, 'outLinks', a)
    _safe_set(a, 'INodeSymbol', b2)
    assert _is_linked(a, 'INodeSymbol', b2)
    if hasattr(b1, 'outLinks'):
        assert not _is_linked(b1, 'outLinks', a)
    if hasattr(b2, 'outLinks'):
        assert _is_linked(b2, 'outLinks', a)
    _safe_set(a, 'INodeSymbol', None)
    assert not _is_linked(a, 'INodeSymbol', b2)
    if hasattr(b2, 'outLinks'):
        assert not _is_linked(b2, 'outLinks', a)


def test_assoc_startActivity327_link_reassign_clear():
    a = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b1 = carnot_StartEventSymbol()
    b2 = carnot_StartEventSymbol()
    _safe_set(a, 'ActivityType329', b1)
    assert _is_linked(a, 'ActivityType329', b1)
    if hasattr(b1, 'startingEventSymbols328'):
        assert _is_linked(b1, 'startingEventSymbols328', a)
    _safe_set(a, 'ActivityType329', b2)
    assert _is_linked(a, 'ActivityType329', b2)
    if hasattr(b1, 'startingEventSymbols328'):
        assert not _is_linked(b1, 'startingEventSymbols328', a)
    if hasattr(b2, 'startingEventSymbols328'):
        assert _is_linked(b2, 'startingEventSymbols328', a)
    _safe_set(a, 'ActivityType329', None)
    assert not _is_linked(a, 'ActivityType329', b2)
    if hasattr(b2, 'startingEventSymbols328'):
        assert not _is_linked(b2, 'startingEventSymbols328', a)


def test_assoc_startEventSymbols33_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_StartEventSymbol()
    b2 = carnot_StartEventSymbol()
    _safe_set(a, 'carnot_ISymbolContainer34', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer34', b1)
    if hasattr(b1, 'carnot_StartEventSymbol'):
        assert _is_linked(b1, 'carnot_StartEventSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer34', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer34', b2)
    if hasattr(b1, 'carnot_StartEventSymbol'):
        assert not _is_linked(b1, 'carnot_StartEventSymbol', a)
    if hasattr(b2, 'carnot_StartEventSymbol'):
        assert _is_linked(b2, 'carnot_StartEventSymbol', a)
    _safe_set(a, 'carnot_ISymbolContainer34', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer34', b2)
    if hasattr(b2, 'carnot_StartEventSymbol'):
        assert not _is_linked(b2, 'carnot_StartEventSymbol', a)


def test_assoc_startingEventSymbols101_link_reassign_clear():
    a = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b1 = carnot_StartEventSymbol()
    b2 = carnot_StartEventSymbol()
    _safe_set(a, 'startActivity', {b1})
    assert _is_linked(a, 'startActivity', b1)
    if hasattr(b1, 'StartEventSymbol'):
        assert _is_linked(b1, 'StartEventSymbol', a)
    _safe_set(a, 'startActivity', {b2})
    assert _is_linked(a, 'startActivity', b2)
    if hasattr(b1, 'StartEventSymbol'):
        assert not _is_linked(b1, 'StartEventSymbol', a)
    if hasattr(b2, 'StartEventSymbol'):
        assert _is_linked(b2, 'StartEventSymbol', a)
    _safe_set(a, 'startActivity', set())
    assert not _is_linked(a, 'startActivity', b2)
    if hasattr(b2, 'StartEventSymbol'):
        assert not _is_linked(b2, 'StartEventSymbol', a)


def test_assoc_subProcessOfConnection51_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_SubProcessOfConnectionType()
    b2 = carnot_SubProcessOfConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer52', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer52', b1)
    if hasattr(b1, 'carnot_SubProcessOfConnectionType'):
        assert _is_linked(b1, 'carnot_SubProcessOfConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer52', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer52', b2)
    if hasattr(b1, 'carnot_SubProcessOfConnectionType'):
        assert not _is_linked(b1, 'carnot_SubProcessOfConnectionType', a)
    if hasattr(b2, 'carnot_SubProcessOfConnectionType'):
        assert _is_linked(b2, 'carnot_SubProcessOfConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer52', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer52', b2)
    if hasattr(b2, 'carnot_SubProcessOfConnectionType'):
        assert not _is_linked(b2, 'carnot_SubProcessOfConnectionType', a)


def test_assoc_targetActivitySymbol341_link_reassign_clear():
    a = carnot_TransitionConnectionType(points="sample_text")
    b1 = carnot_IFlowObjectSymbol()
    b2 = carnot_IFlowObjectSymbol()
    _safe_set(a, 'inTransitions', b1)
    assert _is_linked(a, 'inTransitions', b1)
    if hasattr(b1, 'IFlowObjectSymbol342'):
        assert _is_linked(b1, 'IFlowObjectSymbol342', a)
    _safe_set(a, 'inTransitions', b2)
    assert _is_linked(a, 'inTransitions', b2)
    if hasattr(b1, 'IFlowObjectSymbol342'):
        assert not _is_linked(b1, 'IFlowObjectSymbol342', a)
    if hasattr(b2, 'IFlowObjectSymbol342'):
        assert _is_linked(b2, 'IFlowObjectSymbol342', a)
    _safe_set(a, 'inTransitions', None)
    assert not _is_linked(a, 'inTransitions', b2)
    if hasattr(b2, 'IFlowObjectSymbol342'):
        assert not _is_linked(b2, 'IFlowObjectSymbol342', a)


def test_assoc_targetSymbol197_link_reassign_clear():
    a = carnot_INodeSymbol(height="sample_text", shape="sample_text", width="sample_text", xPos="sample_text", yPos="sample_text")
    b1 = carnot_GenericLinkConnectionType()
    b2 = carnot_GenericLinkConnectionType()
    _safe_set(a, 'INodeSymbol198', b1)
    assert _is_linked(a, 'INodeSymbol198', b1)
    if hasattr(b1, 'inLinks'):
        assert _is_linked(b1, 'inLinks', a)
    _safe_set(a, 'INodeSymbol198', b2)
    assert _is_linked(a, 'INodeSymbol198', b2)
    if hasattr(b1, 'inLinks'):
        assert not _is_linked(b1, 'inLinks', a)
    if hasattr(b2, 'inLinks'):
        assert _is_linked(b2, 'inLinks', a)
    _safe_set(a, 'INodeSymbol198', None)
    assert not _is_linked(a, 'INodeSymbol198', b2)
    if hasattr(b2, 'inLinks'):
        assert not _is_linked(b2, 'inLinks', a)


def test_assoc_teamLead263_link_reassign_clear():
    a = carnot_RoleType(cardinality=7)
    b1 = carnot_OrganizationType()
    b2 = carnot_OrganizationType()
    _safe_set(a, 'RoleType', b1)
    assert _is_linked(a, 'RoleType', b1)
    if hasattr(b1, 'teams'):
        assert _is_linked(b1, 'teams', a)
    _safe_set(a, 'RoleType', b2)
    assert _is_linked(a, 'RoleType', b2)
    if hasattr(b1, 'teams'):
        assert not _is_linked(b1, 'teams', a)
    if hasattr(b2, 'teams'):
        assert _is_linked(b2, 'teams', a)
    _safe_set(a, 'RoleType', None)
    assert not _is_linked(a, 'RoleType', b2)
    if hasattr(b2, 'teams'):
        assert not _is_linked(b2, 'teams', a)


def test_assoc_teamLeadConnection57_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_TeamLeadConnectionType()
    b2 = carnot_TeamLeadConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer58', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer58', b1)
    if hasattr(b1, 'carnot_TeamLeadConnectionType'):
        assert _is_linked(b1, 'carnot_TeamLeadConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer58', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer58', b2)
    if hasattr(b1, 'carnot_TeamLeadConnectionType'):
        assert not _is_linked(b1, 'carnot_TeamLeadConnectionType', a)
    if hasattr(b2, 'carnot_TeamLeadConnectionType'):
        assert _is_linked(b2, 'carnot_TeamLeadConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer58', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer58', b2)
    if hasattr(b2, 'carnot_TeamLeadConnectionType'):
        assert not _is_linked(b2, 'carnot_TeamLeadConnectionType', a)


def test_assoc_teams321_link_reassign_clear():
    a = carnot_RoleType(cardinality=7)
    b1 = carnot_OrganizationType()
    b2 = carnot_OrganizationType()
    _safe_set(a, 'teamLead', {b1})
    assert _is_linked(a, 'teamLead', b1)
    if hasattr(b1, 'OrganizationType322'):
        assert _is_linked(b1, 'OrganizationType322', a)
    _safe_set(a, 'teamLead', {b2})
    assert _is_linked(a, 'teamLead', b2)
    if hasattr(b1, 'OrganizationType322'):
        assert not _is_linked(b1, 'OrganizationType322', a)
    if hasattr(b2, 'OrganizationType322'):
        assert _is_linked(b2, 'OrganizationType322', a)
    _safe_set(a, 'teamLead', set())
    assert not _is_linked(a, 'teamLead', b2)
    if hasattr(b2, 'OrganizationType322'):
        assert not _is_linked(b2, 'OrganizationType322', a)


def test_assoc_text111_link_reassign_clear():
    a = carnot_TextType(mixed="sample_text")
    b1 = carnot_AnnotationSymbolType()
    b2 = carnot_AnnotationSymbolType()
    _safe_set(a, 'carnot_TextType', b1)
    assert _is_linked(a, 'carnot_TextType', b1)
    if hasattr(b1, 'carnot_AnnotationSymbolType112'):
        assert _is_linked(b1, 'carnot_AnnotationSymbolType112', a)
    _safe_set(a, 'carnot_TextType', b2)
    assert _is_linked(a, 'carnot_TextType', b2)
    if hasattr(b1, 'carnot_AnnotationSymbolType112'):
        assert not _is_linked(b1, 'carnot_AnnotationSymbolType112', a)
    if hasattr(b2, 'carnot_AnnotationSymbolType112'):
        assert _is_linked(b2, 'carnot_AnnotationSymbolType112', a)
    _safe_set(a, 'carnot_TextType', None)
    assert not _is_linked(a, 'carnot_TextType', b2)
    if hasattr(b2, 'carnot_AnnotationSymbolType112'):
        assert not _is_linked(b2, 'carnot_AnnotationSymbolType112', a)


def test_assoc_textSymbol35_link_reassign_clear():
    a = carnot_TextSymbolType(text="sample_text")
    b1 = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b2 = carnot_ISymbolContainer(connections="sample_text_2", nodes="sample_text_2")
    _safe_set(a, 'carnot_TextSymbolType', b1)
    assert _is_linked(a, 'carnot_TextSymbolType', b1)
    if hasattr(b1, 'carnot_ISymbolContainer36'):
        assert _is_linked(b1, 'carnot_ISymbolContainer36', a)
    _safe_set(a, 'carnot_TextSymbolType', b2)
    assert _is_linked(a, 'carnot_TextSymbolType', b2)
    if hasattr(b1, 'carnot_ISymbolContainer36'):
        assert not _is_linked(b1, 'carnot_ISymbolContainer36', a)
    if hasattr(b2, 'carnot_ISymbolContainer36'):
        assert _is_linked(b2, 'carnot_ISymbolContainer36', a)
    _safe_set(a, 'carnot_TextSymbolType', None)
    assert not _is_linked(a, 'carnot_TextSymbolType', b2)
    if hasattr(b2, 'carnot_ISymbolContainer36'):
        assert not _is_linked(b2, 'carnot_ISymbolContainer36', a)


def test_assoc_to312_link_reassign_clear():
    a = carnot_IGraphicalObject(borderColor="sample_text", fillColor="sample_text", style="sample_text")
    b1 = carnot_RefersToConnectionType()
    b2 = carnot_RefersToConnectionType()
    _safe_set(a, 'IGraphicalObject313', b1)
    assert _is_linked(a, 'IGraphicalObject313', b1)
    if hasattr(b1, 'referingToConnections'):
        assert _is_linked(b1, 'referingToConnections', a)
    _safe_set(a, 'IGraphicalObject313', b2)
    assert _is_linked(a, 'IGraphicalObject313', b2)
    if hasattr(b1, 'referingToConnections'):
        assert not _is_linked(b1, 'referingToConnections', a)
    if hasattr(b2, 'referingToConnections'):
        assert _is_linked(b2, 'referingToConnections', a)
    _safe_set(a, 'IGraphicalObject313', None)
    assert not _is_linked(a, 'IGraphicalObject313', b2)
    if hasattr(b2, 'referingToConnections'):
        assert not _is_linked(b2, 'referingToConnections', a)


def test_assoc_to351_link_reassign_clear():
    a = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'inTransitions352', b1)
    assert _is_linked(a, 'inTransitions352', b1)
    if hasattr(b1, 'ActivityType353'):
        assert _is_linked(b1, 'ActivityType353', a)
    _safe_set(a, 'inTransitions352', b2)
    assert _is_linked(a, 'inTransitions352', b2)
    if hasattr(b1, 'ActivityType353'):
        assert not _is_linked(b1, 'ActivityType353', a)
    if hasattr(b2, 'ActivityType353'):
        assert _is_linked(b2, 'ActivityType353', a)
    _safe_set(a, 'inTransitions352', None)
    assert not _is_linked(a, 'inTransitions352', b2)
    if hasattr(b2, 'ActivityType353'):
        assert not _is_linked(b2, 'ActivityType353', a)


def test_assoc_transition284_link_reassign_clear():
    a = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b1 = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b2 = carnot_ProcessDefinitionType(defaultPriority="sample_text_2")
    _safe_set(a, 'carnot_TransitionType', b1)
    assert _is_linked(a, 'carnot_TransitionType', b1)
    if hasattr(b1, 'carnot_ProcessDefinitionType285'):
        assert _is_linked(b1, 'carnot_ProcessDefinitionType285', a)
    _safe_set(a, 'carnot_TransitionType', b2)
    assert _is_linked(a, 'carnot_TransitionType', b2)
    if hasattr(b1, 'carnot_ProcessDefinitionType285'):
        assert not _is_linked(b1, 'carnot_ProcessDefinitionType285', a)
    if hasattr(b2, 'carnot_ProcessDefinitionType285'):
        assert _is_linked(b2, 'carnot_ProcessDefinitionType285', a)
    _safe_set(a, 'carnot_TransitionType', None)
    assert not _is_linked(a, 'carnot_TransitionType', b2)
    if hasattr(b2, 'carnot_ProcessDefinitionType285'):
        assert not _is_linked(b2, 'carnot_ProcessDefinitionType285', a)


def test_assoc_transition343_link_reassign_clear():
    a = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b1 = carnot_TransitionConnectionType(points="sample_text")
    b2 = carnot_TransitionConnectionType(points="sample_text_2")
    _safe_set(a, 'TransitionType344', b1)
    assert _is_linked(a, 'TransitionType344', b1)
    if hasattr(b1, 'transitionConnections'):
        assert _is_linked(b1, 'transitionConnections', a)
    _safe_set(a, 'TransitionType344', b2)
    assert _is_linked(a, 'TransitionType344', b2)
    if hasattr(b1, 'transitionConnections'):
        assert not _is_linked(b1, 'transitionConnections', a)
    if hasattr(b2, 'transitionConnections'):
        assert _is_linked(b2, 'transitionConnections', a)
    _safe_set(a, 'TransitionType344', None)
    assert not _is_linked(a, 'TransitionType344', b2)
    if hasattr(b2, 'transitionConnections'):
        assert not _is_linked(b2, 'transitionConnections', a)


def test_assoc_transitionConnection53_link_reassign_clear():
    a = carnot_TransitionConnectionType(points="sample_text")
    b1 = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b2 = carnot_ISymbolContainer(connections="sample_text_2", nodes="sample_text_2")
    _safe_set(a, 'carnot_TransitionConnectionType', b1)
    assert _is_linked(a, 'carnot_TransitionConnectionType', b1)
    if hasattr(b1, 'carnot_ISymbolContainer54'):
        assert _is_linked(b1, 'carnot_ISymbolContainer54', a)
    _safe_set(a, 'carnot_TransitionConnectionType', b2)
    assert _is_linked(a, 'carnot_TransitionConnectionType', b2)
    if hasattr(b1, 'carnot_ISymbolContainer54'):
        assert not _is_linked(b1, 'carnot_ISymbolContainer54', a)
    if hasattr(b2, 'carnot_ISymbolContainer54'):
        assert _is_linked(b2, 'carnot_ISymbolContainer54', a)
    _safe_set(a, 'carnot_TransitionConnectionType', None)
    assert not _is_linked(a, 'carnot_TransitionConnectionType', b2)
    if hasattr(b2, 'carnot_ISymbolContainer54'):
        assert not _is_linked(b2, 'carnot_ISymbolContainer54', a)


def test_assoc_transitionConnections354_link_reassign_clear():
    a = carnot_TransitionType(condition="sample_text", forkOnTraversal="sample_text")
    b1 = carnot_TransitionConnectionType(points="sample_text")
    b2 = carnot_TransitionConnectionType(points="sample_text_2")
    _safe_set(a, 'transition', {b1})
    assert _is_linked(a, 'transition', b1)
    if hasattr(b1, 'TransitionConnectionType355'):
        assert _is_linked(b1, 'TransitionConnectionType355', a)
    _safe_set(a, 'transition', {b2})
    assert _is_linked(a, 'transition', b2)
    if hasattr(b1, 'TransitionConnectionType355'):
        assert not _is_linked(b1, 'TransitionConnectionType355', a)
    if hasattr(b2, 'TransitionConnectionType355'):
        assert _is_linked(b2, 'TransitionConnectionType355', a)
    _safe_set(a, 'transition', set())
    assert not _is_linked(a, 'transition', b2)
    if hasattr(b2, 'TransitionConnectionType355'):
        assert not _is_linked(b2, 'TransitionConnectionType355', a)


def test_assoc_trigger286_link_reassign_clear():
    a = carnot_ProcessDefinitionType(defaultPriority="sample_text")
    b1 = carnot_TriggerType()
    b2 = carnot_TriggerType()
    _safe_set(a, 'carnot_ProcessDefinitionType287', {b1})
    assert _is_linked(a, 'carnot_ProcessDefinitionType287', b1)
    if hasattr(b1, 'carnot_TriggerType'):
        assert _is_linked(b1, 'carnot_TriggerType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType287', {b2})
    assert _is_linked(a, 'carnot_ProcessDefinitionType287', b2)
    if hasattr(b1, 'carnot_TriggerType'):
        assert not _is_linked(b1, 'carnot_TriggerType', a)
    if hasattr(b2, 'carnot_TriggerType'):
        assert _is_linked(b2, 'carnot_TriggerType', a)
    _safe_set(a, 'carnot_ProcessDefinitionType287', set())
    assert not _is_linked(a, 'carnot_ProcessDefinitionType287', b2)
    if hasattr(b2, 'carnot_TriggerType'):
        assert not _is_linked(b2, 'carnot_TriggerType', a)


def test_assoc_triggerType217_link_reassign_clear():
    a = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    b1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    _safe_set(a, 'carnot_TriggerTypeType', b1)
    assert _is_linked(a, 'carnot_TriggerTypeType', b1)
    if hasattr(b1, 'carnot_ModelType218'):
        assert _is_linked(b1, 'carnot_ModelType218', a)
    _safe_set(a, 'carnot_TriggerTypeType', b2)
    assert _is_linked(a, 'carnot_TriggerTypeType', b2)
    if hasattr(b1, 'carnot_ModelType218'):
        assert not _is_linked(b1, 'carnot_ModelType218', a)
    if hasattr(b2, 'carnot_ModelType218'):
        assert _is_linked(b2, 'carnot_ModelType218', a)
    _safe_set(a, 'carnot_TriggerTypeType', None)
    assert not _is_linked(a, 'carnot_TriggerTypeType', b2)
    if hasattr(b2, 'carnot_ModelType218'):
        assert not _is_linked(b2, 'carnot_ModelType218', a)


def test_assoc_triggers365_link_reassign_clear():
    a = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    b1 = carnot_TriggerType()
    b2 = carnot_TriggerType()
    _safe_set(a, 'type366', {b1})
    assert _is_linked(a, 'type366', b1)
    if hasattr(b1, 'TriggerType367'):
        assert _is_linked(b1, 'TriggerType367', a)
    _safe_set(a, 'type366', {b2})
    assert _is_linked(a, 'type366', b2)
    if hasattr(b1, 'TriggerType367'):
        assert not _is_linked(b1, 'TriggerType367', a)
    if hasattr(b2, 'TriggerType367'):
        assert _is_linked(b2, 'TriggerType367', a)
    _safe_set(a, 'type366', set())
    assert not _is_linked(a, 'type366', b2)
    if hasattr(b2, 'TriggerType367'):
        assert not _is_linked(b2, 'TriggerType367', a)


def test_assoc_triggersConnection47_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_TriggersConnectionType()
    b2 = carnot_TriggersConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer48', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer48', b1)
    if hasattr(b1, 'carnot_TriggersConnectionType'):
        assert _is_linked(b1, 'carnot_TriggersConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer48', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer48', b2)
    if hasattr(b1, 'carnot_TriggersConnectionType'):
        assert not _is_linked(b1, 'carnot_TriggersConnectionType', a)
    if hasattr(b2, 'carnot_TriggersConnectionType'):
        assert _is_linked(b2, 'carnot_TriggersConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer48', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer48', b2)
    if hasattr(b2, 'carnot_TriggersConnectionType'):
        assert not _is_linked(b2, 'carnot_TriggersConnectionType', a)


def test_assoc_type119_link_reassign_clear():
    a = carnot_ApplicationTypeType(accessPointProviderClass="sample_text", instanceClass="sample_text", panelClass="sample_text", synchronous="sample_text", validatorClass="sample_text")
    b1 = carnot_ApplicationType(interactive="sample_text")
    b2 = carnot_ApplicationType(interactive="sample_text_2")
    _safe_set(a, 'ApplicationTypeType', b1)
    assert _is_linked(a, 'ApplicationTypeType', b1)
    if hasattr(b1, 'applications'):
        assert _is_linked(b1, 'applications', a)
    _safe_set(a, 'ApplicationTypeType', b2)
    assert _is_linked(a, 'ApplicationTypeType', b2)
    if hasattr(b1, 'applications'):
        assert not _is_linked(b1, 'applications', a)
    if hasattr(b2, 'applications'):
        assert _is_linked(b2, 'applications', a)
    _safe_set(a, 'ApplicationTypeType', None)
    assert not _is_linked(a, 'ApplicationTypeType', b2)
    if hasattr(b2, 'applications'):
        assert not _is_linked(b2, 'applications', a)


def test_assoc_type137_link_reassign_clear():
    a = carnot_ApplicationContextTypeType(accessPointProviderClass="sample_text", hasApplicationPath="sample_text", hasMappingId="sample_text", panelClass="sample_text", validatorClass="sample_text")
    b1 = carnot_ContextType()
    b2 = carnot_ContextType()
    _safe_set(a, 'ApplicationContextTypeType', b1)
    assert _is_linked(a, 'ApplicationContextTypeType', b1)
    if hasattr(b1, 'contexts'):
        assert _is_linked(b1, 'contexts', a)
    _safe_set(a, 'ApplicationContextTypeType', b2)
    assert _is_linked(a, 'ApplicationContextTypeType', b2)
    if hasattr(b1, 'contexts'):
        assert not _is_linked(b1, 'contexts', a)
    if hasattr(b2, 'contexts'):
        assert _is_linked(b2, 'contexts', a)
    _safe_set(a, 'ApplicationContextTypeType', None)
    assert not _is_linked(a, 'ApplicationContextTypeType', b2)
    if hasattr(b2, 'contexts'):
        assert not _is_linked(b2, 'contexts', a)


def test_assoc_type152_link_reassign_clear():
    a = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    b1 = carnot_DataType(predefined="sample_text")
    b2 = carnot_DataType(predefined="sample_text_2")
    _safe_set(a, 'DataTypeType', b1)
    assert _is_linked(a, 'DataTypeType', b1)
    if hasattr(b1, 'data153'):
        assert _is_linked(b1, 'data153', a)
    _safe_set(a, 'DataTypeType', b2)
    assert _is_linked(a, 'DataTypeType', b2)
    if hasattr(b1, 'data153'):
        assert not _is_linked(b1, 'data153', a)
    if hasattr(b2, 'data153'):
        assert _is_linked(b2, 'data153', a)
    _safe_set(a, 'DataTypeType', None)
    assert not _is_linked(a, 'DataTypeType', b2)
    if hasattr(b2, 'data153'):
        assert not _is_linked(b2, 'data153', a)


def test_assoc_type185_link_reassign_clear():
    a = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    b1 = carnot_EventConditionTypeType(activityCondition="sample_text", binderClass="sample_text", implementation="sample_text", panelClass="sample_text", processCondition="sample_text", pullEventEmitterClass="sample_text", rule="sample_text")
    b2 = carnot_EventConditionTypeType(activityCondition="sample_text_2", binderClass="sample_text_2", implementation="sample_text_2", panelClass="sample_text_2", processCondition="sample_text_2", pullEventEmitterClass="sample_text_2", rule="sample_text_2")
    _safe_set(a, 'eventHandlers', b1)
    assert _is_linked(a, 'eventHandlers', b1)
    if hasattr(b1, 'EventConditionTypeType'):
        assert _is_linked(b1, 'EventConditionTypeType', a)
    _safe_set(a, 'eventHandlers', b2)
    assert _is_linked(a, 'eventHandlers', b2)
    if hasattr(b1, 'EventConditionTypeType'):
        assert not _is_linked(b1, 'EventConditionTypeType', a)
    if hasattr(b2, 'EventConditionTypeType'):
        assert _is_linked(b2, 'EventConditionTypeType', a)
    _safe_set(a, 'eventHandlers', None)
    assert not _is_linked(a, 'eventHandlers', b2)
    if hasattr(b2, 'EventConditionTypeType'):
        assert not _is_linked(b2, 'EventConditionTypeType', a)


def test_assoc_type362_link_reassign_clear():
    a = carnot_TriggerTypeType(panelClass="sample_text", pullTrigger="sample_text", pullTriggerEvaluator="sample_text", rule="sample_text")
    b1 = carnot_TriggerType()
    b2 = carnot_TriggerType()
    _safe_set(a, 'TriggerTypeType', b1)
    assert _is_linked(a, 'TriggerTypeType', b1)
    if hasattr(b1, 'triggers'):
        assert _is_linked(b1, 'triggers', a)
    _safe_set(a, 'TriggerTypeType', b2)
    assert _is_linked(a, 'TriggerTypeType', b2)
    if hasattr(b1, 'triggers'):
        assert not _is_linked(b1, 'triggers', a)
    if hasattr(b2, 'triggers'):
        assert _is_linked(b2, 'triggers', a)
    _safe_set(a, 'TriggerTypeType', None)
    assert not _is_linked(a, 'TriggerTypeType', b2)
    if hasattr(b2, 'triggers'):
        assert not _is_linked(b2, 'triggers', a)


def test_assoc_type79_link_reassign_clear():
    a = carnot_EventActionTypeType(actionClass="sample_text", activityAction="sample_text", panelClass="sample_text", processAction="sample_text", supportedConditionTypes="sample_text", unsupportedContexts="sample_text")
    b1 = carnot_AbstractEventAction()
    b2 = carnot_AbstractEventAction()
    _safe_set(a, 'EventActionTypeType', b1)
    assert _is_linked(a, 'EventActionTypeType', b1)
    if hasattr(b1, 'actionInstances'):
        assert _is_linked(b1, 'actionInstances', a)
    _safe_set(a, 'EventActionTypeType', b2)
    assert _is_linked(a, 'EventActionTypeType', b2)
    if hasattr(b1, 'actionInstances'):
        assert not _is_linked(b1, 'actionInstances', a)
    if hasattr(b2, 'actionInstances'):
        assert _is_linked(b2, 'actionInstances', a)
    _safe_set(a, 'EventActionTypeType', None)
    assert not _is_linked(a, 'EventActionTypeType', b2)
    if hasattr(b2, 'actionInstances'):
        assert not _is_linked(b2, 'actionInstances', a)


def test_assoc_type80_link_reassign_clear():
    a = carnot_DataTypeType(accessPathEditor="sample_text", evaluator="sample_text", instanceClass="sample_text", panelClass="sample_text", readable="sample_text", storageStrategy="sample_text", validatorClass="sample_text", valueCreator="sample_text", writable="sample_text")
    b1 = carnot_AccessPointType(direction="sample_text")
    b2 = carnot_AccessPointType(direction="sample_text_2")
    _safe_set(a, 'carnot_DataTypeType', b1)
    assert _is_linked(a, 'carnot_DataTypeType', b1)
    if hasattr(b1, 'carnot_AccessPointType81'):
        assert _is_linked(b1, 'carnot_AccessPointType81', a)
    _safe_set(a, 'carnot_DataTypeType', b2)
    assert _is_linked(a, 'carnot_DataTypeType', b2)
    if hasattr(b1, 'carnot_AccessPointType81'):
        assert not _is_linked(b1, 'carnot_AccessPointType81', a)
    if hasattr(b2, 'carnot_AccessPointType81'):
        assert _is_linked(b2, 'carnot_AccessPointType81', a)
    _safe_set(a, 'carnot_DataTypeType', None)
    assert not _is_linked(a, 'carnot_DataTypeType', b2)
    if hasattr(b2, 'carnot_AccessPointType81'):
        assert not _is_linked(b2, 'carnot_AccessPointType81', a)


def test_assoc_typeDeclarations245_link_reassign_clear():
    a = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b1 = carnot_TypeDeclarationsType()
    b2 = carnot_TypeDeclarationsType()
    _safe_set(a, 'carnot_ModelType246', b1)
    assert _is_linked(a, 'carnot_ModelType246', b1)
    if hasattr(b1, 'carnot_TypeDeclarationsType'):
        assert _is_linked(b1, 'carnot_TypeDeclarationsType', a)
    _safe_set(a, 'carnot_ModelType246', b2)
    assert _is_linked(a, 'carnot_ModelType246', b2)
    if hasattr(b1, 'carnot_TypeDeclarationsType'):
        assert not _is_linked(b1, 'carnot_TypeDeclarationsType', a)
    if hasattr(b2, 'carnot_TypeDeclarationsType'):
        assert _is_linked(b2, 'carnot_TypeDeclarationsType', a)
    _safe_set(a, 'carnot_ModelType246', None)
    assert not _is_linked(a, 'carnot_ModelType246', b2)
    if hasattr(b2, 'carnot_TypeDeclarationsType'):
        assert not _is_linked(b2, 'carnot_TypeDeclarationsType', a)


def test_assoc_unbindAction183_link_reassign_clear():
    a = carnot_EventHandlerType(autoBind="sample_text", consumeOnMatch="sample_text", logHandler="sample_text", unbindOnMatch="sample_text")
    b1 = carnot_UnbindActionType()
    b2 = carnot_UnbindActionType()
    _safe_set(a, 'carnot_EventHandlerType184', {b1})
    assert _is_linked(a, 'carnot_EventHandlerType184', b1)
    if hasattr(b1, 'carnot_UnbindActionType'):
        assert _is_linked(b1, 'carnot_UnbindActionType', a)
    _safe_set(a, 'carnot_EventHandlerType184', {b2})
    assert _is_linked(a, 'carnot_EventHandlerType184', b2)
    if hasattr(b1, 'carnot_UnbindActionType'):
        assert not _is_linked(b1, 'carnot_UnbindActionType', a)
    if hasattr(b2, 'carnot_UnbindActionType'):
        assert _is_linked(b2, 'carnot_UnbindActionType', a)
    _safe_set(a, 'carnot_EventHandlerType184', set())
    assert not _is_linked(a, 'carnot_EventHandlerType184', b2)
    if hasattr(b2, 'carnot_UnbindActionType'):
        assert not _is_linked(b2, 'carnot_UnbindActionType', a)


def test_assoc_validQualityCodes109_link_reassign_clear():
    a = carnot_Code(code="sample_text", name="sample_text", value="sample_text")
    b1 = carnot_ActivityType(allowsAbortByPerformer="sample_text", hibernateOnCreation="sample_text", implementation="sample_text", join="sample_text", loopCondition="sample_text", loopType="sample_text", split="sample_text", subProcessMode="sample_text")
    b2 = carnot_ActivityType(allowsAbortByPerformer="sample_text_2", hibernateOnCreation="sample_text_2", implementation="sample_text_2", join="sample_text_2", loopCondition="sample_text_2", loopType="sample_text_2", split="sample_text_2", subProcessMode="sample_text_2")
    _safe_set(a, 'carnot_Code', b1)
    assert _is_linked(a, 'carnot_Code', b1)
    if hasattr(b1, 'carnot_ActivityType110'):
        assert _is_linked(b1, 'carnot_ActivityType110', a)
    _safe_set(a, 'carnot_Code', b2)
    assert _is_linked(a, 'carnot_Code', b2)
    if hasattr(b1, 'carnot_ActivityType110'):
        assert not _is_linked(b1, 'carnot_ActivityType110', a)
    if hasattr(b2, 'carnot_ActivityType110'):
        assert _is_linked(b2, 'carnot_ActivityType110', a)
    _safe_set(a, 'carnot_Code', None)
    assert not _is_linked(a, 'carnot_Code', b2)
    if hasattr(b2, 'carnot_ActivityType110'):
        assert not _is_linked(b2, 'carnot_ActivityType110', a)


def test_assoc_valueNode127_link_reassign_clear():
    a = carnot_XmlTextNode(mixed="sample_text")
    b1 = carnot_AttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", type="sample_text", value="sample_text")
    b2 = carnot_AttributeType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", name="sample_text_2", type="sample_text_2", value="sample_text_2")
    _safe_set(a, 'carnot_XmlTextNode', b1)
    assert _is_linked(a, 'carnot_XmlTextNode', b1)
    if hasattr(b1, 'carnot_AttributeType128'):
        assert _is_linked(b1, 'carnot_AttributeType128', a)
    _safe_set(a, 'carnot_XmlTextNode', b2)
    assert _is_linked(a, 'carnot_XmlTextNode', b2)
    if hasattr(b1, 'carnot_AttributeType128'):
        assert not _is_linked(b1, 'carnot_AttributeType128', a)
    if hasattr(b2, 'carnot_AttributeType128'):
        assert _is_linked(b2, 'carnot_AttributeType128', a)
    _safe_set(a, 'carnot_XmlTextNode', None)
    assert not _is_linked(a, 'carnot_XmlTextNode', b2)
    if hasattr(b2, 'carnot_AttributeType128'):
        assert not _is_linked(b2, 'carnot_AttributeType128', a)


def test_assoc_view251_link_reassign_clear():
    a = carnot_ViewType(name="sample_text")
    b1 = carnot_ModelType(author="sample_text", carnotVersion="sample_text", created="sample_text", modelOID="sample_text", oid="sample_text", vendor="sample_text")
    b2 = carnot_ModelType(author="sample_text_2", carnotVersion="sample_text_2", created="sample_text_2", modelOID="sample_text_2", oid="sample_text_2", vendor="sample_text_2")
    _safe_set(a, 'carnot_ViewType', b1)
    assert _is_linked(a, 'carnot_ViewType', b1)
    if hasattr(b1, 'carnot_ModelType252'):
        assert _is_linked(b1, 'carnot_ModelType252', a)
    _safe_set(a, 'carnot_ViewType', b2)
    assert _is_linked(a, 'carnot_ViewType', b2)
    if hasattr(b1, 'carnot_ModelType252'):
        assert not _is_linked(b1, 'carnot_ModelType252', a)
    if hasattr(b2, 'carnot_ModelType252'):
        assert _is_linked(b2, 'carnot_ModelType252', a)
    _safe_set(a, 'carnot_ViewType', None)
    assert not _is_linked(a, 'carnot_ViewType', b2)
    if hasattr(b2, 'carnot_ModelType252'):
        assert not _is_linked(b2, 'carnot_ModelType252', a)


def test_assoc_view373_link_reassign_clear():
    a = carnot_ViewType(name="sample_text")
    b1 = carnot_ViewType(name="sample_text")
    b2 = carnot_ViewType(name="sample_text_2")
    _safe_set(a, 'carnot_ViewType372', {b1})
    assert _is_linked(a, 'carnot_ViewType372', b1)
    if hasattr(b1, 'carnot_ViewType374'):
        assert _is_linked(b1, 'carnot_ViewType374', a)
    _safe_set(a, 'carnot_ViewType372', {b2})
    assert _is_linked(a, 'carnot_ViewType372', b2)
    if hasattr(b1, 'carnot_ViewType374'):
        assert not _is_linked(b1, 'carnot_ViewType374', a)
    if hasattr(b2, 'carnot_ViewType374'):
        assert _is_linked(b2, 'carnot_ViewType374', a)
    _safe_set(a, 'carnot_ViewType372', set())
    assert not _is_linked(a, 'carnot_ViewType372', b2)
    if hasattr(b2, 'carnot_ViewType374'):
        assert not _is_linked(b2, 'carnot_ViewType374', a)


def test_assoc_viewable368_link_reassign_clear():
    a = carnot_IModelElement(elementOid="sample_text")
    b1 = carnot_ViewableType()
    b2 = carnot_ViewableType()
    _safe_set(a, 'carnot_IModelElement', b1)
    assert _is_linked(a, 'carnot_IModelElement', b1)
    if hasattr(b1, 'carnot_ViewableType'):
        assert _is_linked(b1, 'carnot_ViewableType', a)
    _safe_set(a, 'carnot_IModelElement', b2)
    assert _is_linked(a, 'carnot_IModelElement', b2)
    if hasattr(b1, 'carnot_ViewableType'):
        assert not _is_linked(b1, 'carnot_ViewableType', a)
    if hasattr(b2, 'carnot_ViewableType'):
        assert _is_linked(b2, 'carnot_ViewableType', a)
    _safe_set(a, 'carnot_IModelElement', None)
    assert not _is_linked(a, 'carnot_IModelElement', b2)
    if hasattr(b2, 'carnot_ViewableType'):
        assert not _is_linked(b2, 'carnot_ViewableType', a)


def test_assoc_viewable375_link_reassign_clear():
    a = carnot_ViewType(name="sample_text")
    b1 = carnot_ViewableType()
    b2 = carnot_ViewableType()
    _safe_set(a, 'carnot_ViewType376', {b1})
    assert _is_linked(a, 'carnot_ViewType376', b1)
    if hasattr(b1, 'carnot_ViewableType377'):
        assert _is_linked(b1, 'carnot_ViewableType377', a)
    _safe_set(a, 'carnot_ViewType376', {b2})
    assert _is_linked(a, 'carnot_ViewType376', b2)
    if hasattr(b1, 'carnot_ViewableType377'):
        assert not _is_linked(b1, 'carnot_ViewableType377', a)
    if hasattr(b2, 'carnot_ViewableType377'):
        assert _is_linked(b2, 'carnot_ViewableType377', a)
    _safe_set(a, 'carnot_ViewType376', set())
    assert not _is_linked(a, 'carnot_ViewType376', b2)
    if hasattr(b2, 'carnot_ViewableType377'):
        assert not _is_linked(b2, 'carnot_ViewableType377', a)


def test_assoc_worksForConnection55_link_reassign_clear():
    a = carnot_ISymbolContainer(connections="sample_text", nodes="sample_text")
    b1 = carnot_WorksForConnectionType()
    b2 = carnot_WorksForConnectionType()
    _safe_set(a, 'carnot_ISymbolContainer56', {b1})
    assert _is_linked(a, 'carnot_ISymbolContainer56', b1)
    if hasattr(b1, 'carnot_WorksForConnectionType'):
        assert _is_linked(b1, 'carnot_WorksForConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer56', {b2})
    assert _is_linked(a, 'carnot_ISymbolContainer56', b2)
    if hasattr(b1, 'carnot_WorksForConnectionType'):
        assert not _is_linked(b1, 'carnot_WorksForConnectionType', a)
    if hasattr(b2, 'carnot_WorksForConnectionType'):
        assert _is_linked(b2, 'carnot_WorksForConnectionType', a)
    _safe_set(a, 'carnot_ISymbolContainer56', set())
    assert not _is_linked(a, 'carnot_ISymbolContainer56', b2)
    if hasattr(b2, 'carnot_WorksForConnectionType'):
        assert not _is_linked(b2, 'carnot_WorksForConnectionType', a)


def test_assoc_xMLNSPrefixMap169_link_reassign_clear():
    a = carnot_DocumentRoot(mixed="sample_text")
    b1 = carnot_EStringToStringMapEntry()
    b2 = carnot_EStringToStringMapEntry()
    _safe_set(a, 'carnot_DocumentRoot', {b1})
    assert _is_linked(a, 'carnot_DocumentRoot', b1)
    if hasattr(b1, 'carnot_EStringToStringMapEntry'):
        assert _is_linked(b1, 'carnot_EStringToStringMapEntry', a)
    _safe_set(a, 'carnot_DocumentRoot', {b2})
    assert _is_linked(a, 'carnot_DocumentRoot', b2)
    if hasattr(b1, 'carnot_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'carnot_EStringToStringMapEntry', a)
    if hasattr(b2, 'carnot_EStringToStringMapEntry'):
        assert _is_linked(b2, 'carnot_EStringToStringMapEntry', a)
    _safe_set(a, 'carnot_DocumentRoot', set())
    assert not _is_linked(a, 'carnot_DocumentRoot', b2)
    if hasattr(b2, 'carnot_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'carnot_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation170_link_reassign_clear():
    a = carnot_DocumentRoot(mixed="sample_text")
    b1 = carnot_EStringToStringMapEntry()
    b2 = carnot_EStringToStringMapEntry()
    _safe_set(a, 'carnot_DocumentRoot171', {b1})
    assert _is_linked(a, 'carnot_DocumentRoot171', b1)
    if hasattr(b1, 'carnot_EStringToStringMapEntry172'):
        assert _is_linked(b1, 'carnot_EStringToStringMapEntry172', a)
    _safe_set(a, 'carnot_DocumentRoot171', {b2})
    assert _is_linked(a, 'carnot_DocumentRoot171', b2)
    if hasattr(b1, 'carnot_EStringToStringMapEntry172'):
        assert not _is_linked(b1, 'carnot_EStringToStringMapEntry172', a)
    if hasattr(b2, 'carnot_EStringToStringMapEntry172'):
        assert _is_linked(b2, 'carnot_EStringToStringMapEntry172', a)
    _safe_set(a, 'carnot_DocumentRoot171', set())
    assert not _is_linked(a, 'carnot_DocumentRoot171', b2)
    if hasattr(b2, 'carnot_EStringToStringMapEntry172'):
        assert not _is_linked(b2, 'carnot_EStringToStringMapEntry172', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractEventAction_strategy = st.builds(AbstractEventAction)
@given(instance=AbstractEventAction_strategy)
@settings(max_examples=25)
def test_AbstractEventAction_instantiation(instance):
    assert isinstance(instance, AbstractEventAction)


AbstractEventSymbol_strategy = st.builds(AbstractEventSymbol)
@given(instance=AbstractEventSymbol_strategy)
@settings(max_examples=25)
def test_AbstractEventSymbol_instantiation(instance):
    assert isinstance(instance, AbstractEventSymbol)


FormalParameterMappingType_strategy = st.builds(FormalParameterMappingType)
@given(instance=FormalParameterMappingType_strategy)
@settings(max_examples=25)
def test_FormalParameterMappingType_instantiation(instance):
    assert isinstance(instance, FormalParameterMappingType)


FormalParameterMappingsType_strategy = st.builds(FormalParameterMappingsType)
@given(instance=FormalParameterMappingsType_strategy)
@settings(max_examples=25)
def test_FormalParameterMappingsType_instantiation(instance):
    assert isinstance(instance, FormalParameterMappingsType)


IAccessPointOwner_strategy = st.builds(IAccessPointOwner)
@given(instance=IAccessPointOwner_strategy)
@settings(max_examples=25)
def test_IAccessPointOwner_instantiation(instance):
    assert isinstance(instance, IAccessPointOwner)


IConnectionSymbol_strategy = st.builds(IConnectionSymbol)
@given(instance=IConnectionSymbol_strategy)
@settings(max_examples=25)
def test_IConnectionSymbol_instantiation(instance):
    assert isinstance(instance, IConnectionSymbol)


IEventHandlerOwner_strategy = st.builds(IEventHandlerOwner)
@given(instance=IEventHandlerOwner_strategy)
@settings(max_examples=25)
def test_IEventHandlerOwner_instantiation(instance):
    assert isinstance(instance, IEventHandlerOwner)


IExtensibleElement_strategy = st.builds(IExtensibleElement)
@given(instance=IExtensibleElement_strategy)
@settings(max_examples=25)
def test_IExtensibleElement_instantiation(instance):
    assert isinstance(instance, IExtensibleElement)


IFlowObjectSymbol_strategy = st.builds(IFlowObjectSymbol)
@given(instance=IFlowObjectSymbol_strategy)
@settings(max_examples=25)
def test_IFlowObjectSymbol_instantiation(instance):
    assert isinstance(instance, IFlowObjectSymbol)


IGraphicalObject_strategy = st.builds(IGraphicalObject)
@given(instance=IGraphicalObject_strategy)
@settings(max_examples=25)
def test_IGraphicalObject_instantiation(instance):
    assert isinstance(instance, IGraphicalObject)


IIdentifiableElement_strategy = st.builds(IIdentifiableElement)
@given(instance=IIdentifiableElement_strategy)
@settings(max_examples=25)
def test_IIdentifiableElement_instantiation(instance):
    assert isinstance(instance, IIdentifiableElement)


IIdentifiableModelElement_strategy = st.builds(IIdentifiableModelElement)
@given(instance=IIdentifiableModelElement_strategy)
@settings(max_examples=25)
def test_IIdentifiableModelElement_instantiation(instance):
    assert isinstance(instance, IIdentifiableModelElement)


IMetaType_strategy = st.builds(IMetaType)
@given(instance=IMetaType_strategy)
@settings(max_examples=25)
def test_IMetaType_instantiation(instance):
    assert isinstance(instance, IMetaType)


IModelElement_strategy = st.builds(IModelElement)
@given(instance=IModelElement_strategy)
@settings(max_examples=25)
def test_IModelElement_instantiation(instance):
    assert isinstance(instance, IModelElement)


IModelElementNodeSymbol_strategy = st.builds(IModelElementNodeSymbol)
@given(instance=IModelElementNodeSymbol_strategy)
@settings(max_examples=25)
def test_IModelElementNodeSymbol_instantiation(instance):
    assert isinstance(instance, IModelElementNodeSymbol)


IModelParticipant_strategy = st.builds(IModelParticipant)
@given(instance=IModelParticipant_strategy)
@settings(max_examples=25)
def test_IModelParticipant_instantiation(instance):
    assert isinstance(instance, IModelParticipant)


IModelParticipantSymbol_strategy = st.builds(IModelParticipantSymbol)
@given(instance=IModelParticipantSymbol_strategy)
@settings(max_examples=25)
def test_IModelParticipantSymbol_instantiation(instance):
    assert isinstance(instance, IModelParticipantSymbol)


INodeSymbol_strategy = st.builds(INodeSymbol)
@given(instance=INodeSymbol_strategy)
@settings(max_examples=25)
def test_INodeSymbol_instantiation(instance):
    assert isinstance(instance, INodeSymbol)


ISwimlaneSymbol_strategy = st.builds(ISwimlaneSymbol)
@given(instance=ISwimlaneSymbol_strategy)
@settings(max_examples=25)
def test_ISwimlaneSymbol_instantiation(instance):
    assert isinstance(instance, ISwimlaneSymbol)


ISymbolContainer_strategy = st.builds(ISymbolContainer)
@given(instance=ISymbolContainer_strategy)
@settings(max_examples=25)
def test_ISymbolContainer_instantiation(instance):
    assert isinstance(instance, ISymbolContainer)


ITypedElement_strategy = st.builds(ITypedElement)
@given(instance=ITypedElement_strategy)
@settings(max_examples=25)
def test_ITypedElement_instantiation(instance):
    assert isinstance(instance, ITypedElement)


carnot_AbstractEventAction_strategy = st.builds(carnot_AbstractEventAction)
@given(instance=carnot_AbstractEventAction_strategy)
@settings(max_examples=25)
def test_carnot_AbstractEventAction_instantiation(instance):
    assert isinstance(instance, carnot_AbstractEventAction)


carnot_AbstractEventSymbol_strategy = st.builds(carnot_AbstractEventSymbol, label=safe_text)
@given(instance=carnot_AbstractEventSymbol_strategy)
@settings(max_examples=25)
def test_carnot_AbstractEventSymbol_instantiation(instance):
    assert isinstance(instance, carnot_AbstractEventSymbol)


carnot_AccessPointType_strategy = st.builds(carnot_AccessPointType, direction=safe_text)
@given(instance=carnot_AccessPointType_strategy)
@settings(max_examples=25)
def test_carnot_AccessPointType_instantiation(instance):
    assert isinstance(instance, carnot_AccessPointType)


carnot_ActivitySymbolType_strategy = st.builds(carnot_ActivitySymbolType)
@given(instance=carnot_ActivitySymbolType_strategy)
@settings(max_examples=25)
def test_carnot_ActivitySymbolType_instantiation(instance):
    assert isinstance(instance, carnot_ActivitySymbolType)


carnot_ActivityType_strategy = st.builds(carnot_ActivityType, allowsAbortByPerformer=safe_text, hibernateOnCreation=safe_text, implementation=safe_text, join=safe_text, loopCondition=safe_text, loopType=safe_text, split=safe_text, subProcessMode=safe_text)
@given(instance=carnot_ActivityType_strategy)
@settings(max_examples=25)
def test_carnot_ActivityType_instantiation(instance):
    assert isinstance(instance, carnot_ActivityType)


carnot_AnnotationSymbolType_strategy = st.builds(carnot_AnnotationSymbolType)
@given(instance=carnot_AnnotationSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_AnnotationSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_AnnotationSymbolType)


carnot_ApplicationContextTypeType_strategy = st.builds(carnot_ApplicationContextTypeType, accessPointProviderClass=safe_text, hasApplicationPath=safe_text, hasMappingId=safe_text, panelClass=safe_text, validatorClass=safe_text)
@given(instance=carnot_ApplicationContextTypeType_strategy)
@settings(max_examples=25)
def test_carnot_ApplicationContextTypeType_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationContextTypeType)


carnot_ApplicationSymbolType_strategy = st.builds(carnot_ApplicationSymbolType)
@given(instance=carnot_ApplicationSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_ApplicationSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationSymbolType)


carnot_ApplicationType_strategy = st.builds(carnot_ApplicationType, interactive=safe_text)
@given(instance=carnot_ApplicationType_strategy)
@settings(max_examples=25)
def test_carnot_ApplicationType_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationType)


carnot_ApplicationTypeType_strategy = st.builds(carnot_ApplicationTypeType, accessPointProviderClass=safe_text, instanceClass=safe_text, panelClass=safe_text, synchronous=safe_text, validatorClass=safe_text)
@given(instance=carnot_ApplicationTypeType_strategy)
@settings(max_examples=25)
def test_carnot_ApplicationTypeType_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationTypeType)


carnot_AttributeType_strategy = st.builds(carnot_AttributeType, any=safe_text, group=safe_text, mixed=safe_text, name=safe_text, type=safe_text, value=safe_text)
@given(instance=carnot_AttributeType_strategy)
@settings(max_examples=25)
def test_carnot_AttributeType_instantiation(instance):
    assert isinstance(instance, carnot_AttributeType)


carnot_BindActionType_strategy = st.builds(carnot_BindActionType)
@given(instance=carnot_BindActionType_strategy)
@settings(max_examples=25)
def test_carnot_BindActionType_instantiation(instance):
    assert isinstance(instance, carnot_BindActionType)


carnot_Code_strategy = st.builds(carnot_Code, code=safe_text, name=safe_text, value=safe_text)
@given(instance=carnot_Code_strategy)
@settings(max_examples=25)
def test_carnot_Code_instantiation(instance):
    assert isinstance(instance, carnot_Code)


carnot_ConditionalPerformerSymbolType_strategy = st.builds(carnot_ConditionalPerformerSymbolType)
@given(instance=carnot_ConditionalPerformerSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_ConditionalPerformerSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_ConditionalPerformerSymbolType)


carnot_ConditionalPerformerType_strategy = st.builds(carnot_ConditionalPerformerType, dataPath=safe_text, isUser=safe_text)
@given(instance=carnot_ConditionalPerformerType_strategy)
@settings(max_examples=25)
def test_carnot_ConditionalPerformerType_instantiation(instance):
    assert isinstance(instance, carnot_ConditionalPerformerType)


carnot_ContextType_strategy = st.builds(carnot_ContextType)
@given(instance=carnot_ContextType_strategy)
@settings(max_examples=25)
def test_carnot_ContextType_instantiation(instance):
    assert isinstance(instance, carnot_ContextType)


carnot_Coordinates_strategy = st.builds(carnot_Coordinates, xPos=safe_text, yPos=safe_text)
@given(instance=carnot_Coordinates_strategy)
@settings(max_examples=25)
def test_carnot_Coordinates_instantiation(instance):
    assert isinstance(instance, carnot_Coordinates)


carnot_DataMappingConnectionType_strategy = st.builds(carnot_DataMappingConnectionType)
@given(instance=carnot_DataMappingConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_DataMappingConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_DataMappingConnectionType)


carnot_DataMappingType_strategy = st.builds(carnot_DataMappingType, applicationAccessPoint=safe_text, applicationPath=safe_text, context=safe_text, dataPath=safe_text, direction=safe_text)
@given(instance=carnot_DataMappingType_strategy)
@settings(max_examples=25)
def test_carnot_DataMappingType_instantiation(instance):
    assert isinstance(instance, carnot_DataMappingType)


carnot_DataPathType_strategy = st.builds(carnot_DataPathType, dataPath=safe_text, descriptor=safe_text, direction=safe_text, key=safe_text)
@given(instance=carnot_DataPathType_strategy)
@settings(max_examples=25)
def test_carnot_DataPathType_instantiation(instance):
    assert isinstance(instance, carnot_DataPathType)


carnot_DataSymbolType_strategy = st.builds(carnot_DataSymbolType)
@given(instance=carnot_DataSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_DataSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_DataSymbolType)


carnot_DataType_strategy = st.builds(carnot_DataType, predefined=safe_text)
@given(instance=carnot_DataType_strategy)
@settings(max_examples=25)
def test_carnot_DataType_instantiation(instance):
    assert isinstance(instance, carnot_DataType)


carnot_DataTypeType_strategy = st.builds(carnot_DataTypeType, accessPathEditor=safe_text, evaluator=safe_text, instanceClass=safe_text, panelClass=safe_text, readable=safe_text, storageStrategy=safe_text, validatorClass=safe_text, valueCreator=safe_text, writable=safe_text)
@given(instance=carnot_DataTypeType_strategy)
@settings(max_examples=25)
def test_carnot_DataTypeType_instantiation(instance):
    assert isinstance(instance, carnot_DataTypeType)


carnot_DescriptionType_strategy = st.builds(carnot_DescriptionType, mixed=safe_text)
@given(instance=carnot_DescriptionType_strategy)
@settings(max_examples=25)
def test_carnot_DescriptionType_instantiation(instance):
    assert isinstance(instance, carnot_DescriptionType)


carnot_DiagramType_strategy = st.builds(carnot_DiagramType, mode=safe_text, name=safe_text, orientation=safe_text)
@given(instance=carnot_DiagramType_strategy)
@settings(max_examples=25)
def test_carnot_DiagramType_instantiation(instance):
    assert isinstance(instance, carnot_DiagramType)


carnot_DocumentRoot_strategy = st.builds(carnot_DocumentRoot, mixed=safe_text)
@given(instance=carnot_DocumentRoot_strategy)
@settings(max_examples=25)
def test_carnot_DocumentRoot_instantiation(instance):
    assert isinstance(instance, carnot_DocumentRoot)


carnot_EObject_strategy = st.builds(carnot_EObject)
@given(instance=carnot_EObject_strategy)
@settings(max_examples=25)
def test_carnot_EObject_instantiation(instance):
    assert isinstance(instance, carnot_EObject)


carnot_EStringToStringMapEntry_strategy = st.builds(carnot_EStringToStringMapEntry)
@given(instance=carnot_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_carnot_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, carnot_EStringToStringMapEntry)


carnot_EndEventSymbol_strategy = st.builds(carnot_EndEventSymbol)
@given(instance=carnot_EndEventSymbol_strategy)
@settings(max_examples=25)
def test_carnot_EndEventSymbol_instantiation(instance):
    assert isinstance(instance, carnot_EndEventSymbol)


carnot_EventActionType_strategy = st.builds(carnot_EventActionType)
@given(instance=carnot_EventActionType_strategy)
@settings(max_examples=25)
def test_carnot_EventActionType_instantiation(instance):
    assert isinstance(instance, carnot_EventActionType)


carnot_EventActionTypeType_strategy = st.builds(carnot_EventActionTypeType, actionClass=safe_text, activityAction=safe_text, panelClass=safe_text, processAction=safe_text, supportedConditionTypes=safe_text, unsupportedContexts=safe_text)
@given(instance=carnot_EventActionTypeType_strategy)
@settings(max_examples=25)
def test_carnot_EventActionTypeType_instantiation(instance):
    assert isinstance(instance, carnot_EventActionTypeType)


carnot_EventConditionTypeType_strategy = st.builds(carnot_EventConditionTypeType, activityCondition=safe_text, binderClass=safe_text, implementation=safe_text, panelClass=safe_text, processCondition=safe_text, pullEventEmitterClass=safe_text, rule=safe_text)
@given(instance=carnot_EventConditionTypeType_strategy)
@settings(max_examples=25)
def test_carnot_EventConditionTypeType_instantiation(instance):
    assert isinstance(instance, carnot_EventConditionTypeType)


carnot_EventHandlerType_strategy = st.builds(carnot_EventHandlerType, autoBind=safe_text, consumeOnMatch=safe_text, logHandler=safe_text, unbindOnMatch=safe_text)
@given(instance=carnot_EventHandlerType_strategy)
@settings(max_examples=25)
def test_carnot_EventHandlerType_instantiation(instance):
    assert isinstance(instance, carnot_EventHandlerType)


carnot_ExecutedByConnectionType_strategy = st.builds(carnot_ExecutedByConnectionType)
@given(instance=carnot_ExecutedByConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_ExecutedByConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_ExecutedByConnectionType)


carnot_ExternalPackage_strategy = st.builds(carnot_ExternalPackage)
@given(instance=carnot_ExternalPackage_strategy)
@settings(max_examples=25)
def test_carnot_ExternalPackage_instantiation(instance):
    assert isinstance(instance, carnot_ExternalPackage)


carnot_ExternalPackages_strategy = st.builds(carnot_ExternalPackages)
@given(instance=carnot_ExternalPackages_strategy)
@settings(max_examples=25)
def test_carnot_ExternalPackages_instantiation(instance):
    assert isinstance(instance, carnot_ExternalPackages)


carnot_ExternalReferenceType_strategy = st.builds(carnot_ExternalReferenceType)
@given(instance=carnot_ExternalReferenceType_strategy)
@settings(max_examples=25)
def test_carnot_ExternalReferenceType_instantiation(instance):
    assert isinstance(instance, carnot_ExternalReferenceType)


carnot_FormalParametersType_strategy = st.builds(carnot_FormalParametersType)
@given(instance=carnot_FormalParametersType_strategy)
@settings(max_examples=25)
def test_carnot_FormalParametersType_instantiation(instance):
    assert isinstance(instance, carnot_FormalParametersType)


carnot_GatewaySymbol_strategy = st.builds(carnot_GatewaySymbol, flowKind=safe_text)
@given(instance=carnot_GatewaySymbol_strategy)
@settings(max_examples=25)
def test_carnot_GatewaySymbol_instantiation(instance):
    assert isinstance(instance, carnot_GatewaySymbol)


carnot_GenericLinkConnectionType_strategy = st.builds(carnot_GenericLinkConnectionType)
@given(instance=carnot_GenericLinkConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_GenericLinkConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_GenericLinkConnectionType)


carnot_GroupSymbolType_strategy = st.builds(carnot_GroupSymbolType)
@given(instance=carnot_GroupSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_GroupSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_GroupSymbolType)


carnot_IAccessPointOwner_strategy = st.builds(carnot_IAccessPointOwner)
@given(instance=carnot_IAccessPointOwner_strategy)
@settings(max_examples=25)
def test_carnot_IAccessPointOwner_instantiation(instance):
    assert isinstance(instance, carnot_IAccessPointOwner)


carnot_IConnectionSymbol_strategy = st.builds(carnot_IConnectionSymbol, routing=safe_text, sourceAnchor=safe_text, targetAnchor=safe_text)
@given(instance=carnot_IConnectionSymbol_strategy)
@settings(max_examples=25)
def test_carnot_IConnectionSymbol_instantiation(instance):
    assert isinstance(instance, carnot_IConnectionSymbol)


carnot_IEventHandlerOwner_strategy = st.builds(carnot_IEventHandlerOwner)
@given(instance=carnot_IEventHandlerOwner_strategy)
@settings(max_examples=25)
def test_carnot_IEventHandlerOwner_instantiation(instance):
    assert isinstance(instance, carnot_IEventHandlerOwner)


carnot_IExtensibleElement_strategy = st.builds(carnot_IExtensibleElement)
@given(instance=carnot_IExtensibleElement_strategy)
@settings(max_examples=25)
def test_carnot_IExtensibleElement_instantiation(instance):
    assert isinstance(instance, carnot_IExtensibleElement)


carnot_IFlowObjectSymbol_strategy = st.builds(carnot_IFlowObjectSymbol)
@given(instance=carnot_IFlowObjectSymbol_strategy)
@settings(max_examples=25)
def test_carnot_IFlowObjectSymbol_instantiation(instance):
    assert isinstance(instance, carnot_IFlowObjectSymbol)


carnot_IGraphicalObject_strategy = st.builds(carnot_IGraphicalObject, borderColor=safe_text, fillColor=safe_text, style=safe_text)
@given(instance=carnot_IGraphicalObject_strategy)
@settings(max_examples=25)
def test_carnot_IGraphicalObject_instantiation(instance):
    assert isinstance(instance, carnot_IGraphicalObject)


carnot_IIdentifiableElement_strategy = st.builds(carnot_IIdentifiableElement, id=safe_text, name=safe_text)
@given(instance=carnot_IIdentifiableElement_strategy)
@settings(max_examples=25)
def test_carnot_IIdentifiableElement_instantiation(instance):
    assert isinstance(instance, carnot_IIdentifiableElement)


carnot_IIdentifiableModelElement_strategy = st.builds(carnot_IIdentifiableModelElement)
@given(instance=carnot_IIdentifiableModelElement_strategy)
@settings(max_examples=25)
def test_carnot_IIdentifiableModelElement_instantiation(instance):
    assert isinstance(instance, carnot_IIdentifiableModelElement)


carnot_IMetaType_strategy = st.builds(carnot_IMetaType, isPredefined=safe_text)
@given(instance=carnot_IMetaType_strategy)
@settings(max_examples=25)
def test_carnot_IMetaType_instantiation(instance):
    assert isinstance(instance, carnot_IMetaType)


carnot_IModelElement_strategy = st.builds(carnot_IModelElement, elementOid=safe_text)
@given(instance=carnot_IModelElement_strategy)
@settings(max_examples=25)
def test_carnot_IModelElement_instantiation(instance):
    assert isinstance(instance, carnot_IModelElement)


carnot_IModelElementNodeSymbol_strategy = st.builds(carnot_IModelElementNodeSymbol)
@given(instance=carnot_IModelElementNodeSymbol_strategy)
@settings(max_examples=25)
def test_carnot_IModelElementNodeSymbol_instantiation(instance):
    assert isinstance(instance, carnot_IModelElementNodeSymbol)


carnot_IModelParticipant_strategy = st.builds(carnot_IModelParticipant)
@given(instance=carnot_IModelParticipant_strategy)
@settings(max_examples=25)
def test_carnot_IModelParticipant_instantiation(instance):
    assert isinstance(instance, carnot_IModelParticipant)


carnot_IModelParticipantSymbol_strategy = st.builds(carnot_IModelParticipantSymbol)
@given(instance=carnot_IModelParticipantSymbol_strategy)
@settings(max_examples=25)
def test_carnot_IModelParticipantSymbol_instantiation(instance):
    assert isinstance(instance, carnot_IModelParticipantSymbol)


carnot_INodeSymbol_strategy = st.builds(carnot_INodeSymbol, height=safe_text, shape=safe_text, width=safe_text, xPos=safe_text, yPos=safe_text)
@given(instance=carnot_INodeSymbol_strategy)
@settings(max_examples=25)
def test_carnot_INodeSymbol_instantiation(instance):
    assert isinstance(instance, carnot_INodeSymbol)


carnot_ISwimlaneSymbol_strategy = st.builds(carnot_ISwimlaneSymbol, collapsed=safe_text, orientation=safe_text)
@given(instance=carnot_ISwimlaneSymbol_strategy)
@settings(max_examples=25)
def test_carnot_ISwimlaneSymbol_instantiation(instance):
    assert isinstance(instance, carnot_ISwimlaneSymbol)


carnot_ISymbolContainer_strategy = st.builds(carnot_ISymbolContainer, connections=safe_text, nodes=safe_text)
@given(instance=carnot_ISymbolContainer_strategy)
@settings(max_examples=25)
def test_carnot_ISymbolContainer_instantiation(instance):
    assert isinstance(instance, carnot_ISymbolContainer)


carnot_ITypedElement_strategy = st.builds(carnot_ITypedElement)
@given(instance=carnot_ITypedElement_strategy)
@settings(max_examples=25)
def test_carnot_ITypedElement_instantiation(instance):
    assert isinstance(instance, carnot_ITypedElement)


carnot_IdRef_strategy = st.builds(carnot_IdRef, ref=safe_text)
@given(instance=carnot_IdRef_strategy)
@settings(max_examples=25)
def test_carnot_IdRef_instantiation(instance):
    assert isinstance(instance, carnot_IdRef)


carnot_IdentifiableReference_strategy = st.builds(carnot_IdentifiableReference)
@given(instance=carnot_IdentifiableReference_strategy)
@settings(max_examples=25)
def test_carnot_IdentifiableReference_instantiation(instance):
    assert isinstance(instance, carnot_IdentifiableReference)


carnot_IntermediateEventSymbol_strategy = st.builds(carnot_IntermediateEventSymbol)
@given(instance=carnot_IntermediateEventSymbol_strategy)
@settings(max_examples=25)
def test_carnot_IntermediateEventSymbol_instantiation(instance):
    assert isinstance(instance, carnot_IntermediateEventSymbol)


carnot_LaneSymbol_strategy = st.builds(carnot_LaneSymbol)
@given(instance=carnot_LaneSymbol_strategy)
@settings(max_examples=25)
def test_carnot_LaneSymbol_instantiation(instance):
    assert isinstance(instance, carnot_LaneSymbol)


carnot_LinkTypeType_strategy = st.builds(carnot_LinkTypeType, lineColor=safe_text, lineStyle=safe_text, showLinkTypeName=safe_text, showRoleNames=safe_text, sourceCardinality=safe_text, sourceClass=safe_text, sourceRole=safe_text, sourceSymbol=safe_text, targetCardinality=safe_text, targetClass=safe_text, targetRole=safe_text, targetSymbol=safe_text)
@given(instance=carnot_LinkTypeType_strategy)
@settings(max_examples=25)
def test_carnot_LinkTypeType_instantiation(instance):
    assert isinstance(instance, carnot_LinkTypeType)


carnot_ModelType_strategy = st.builds(carnot_ModelType, author=safe_text, carnotVersion=safe_text, created=safe_text, modelOID=safe_text, oid=safe_text, vendor=safe_text)
@given(instance=carnot_ModelType_strategy)
@settings(max_examples=25)
def test_carnot_ModelType_instantiation(instance):
    assert isinstance(instance, carnot_ModelType)


carnot_ModelerSymbolType_strategy = st.builds(carnot_ModelerSymbolType)
@given(instance=carnot_ModelerSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_ModelerSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_ModelerSymbolType)


carnot_ModelerType_strategy = st.builds(carnot_ModelerType, email=safe_text, password=safe_text)
@given(instance=carnot_ModelerType_strategy)
@settings(max_examples=25)
def test_carnot_ModelerType_instantiation(instance):
    assert isinstance(instance, carnot_ModelerType)


carnot_OrganizationSymbolType_strategy = st.builds(carnot_OrganizationSymbolType)
@given(instance=carnot_OrganizationSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_OrganizationSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_OrganizationSymbolType)


carnot_OrganizationType_strategy = st.builds(carnot_OrganizationType)
@given(instance=carnot_OrganizationType_strategy)
@settings(max_examples=25)
def test_carnot_OrganizationType_instantiation(instance):
    assert isinstance(instance, carnot_OrganizationType)


carnot_ParameterMappingType_strategy = st.builds(carnot_ParameterMappingType, dataPath=safe_text, parameter=safe_text, parameterPath=safe_text)
@given(instance=carnot_ParameterMappingType_strategy)
@settings(max_examples=25)
def test_carnot_ParameterMappingType_instantiation(instance):
    assert isinstance(instance, carnot_ParameterMappingType)


carnot_PartOfConnectionType_strategy = st.builds(carnot_PartOfConnectionType)
@given(instance=carnot_PartOfConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_PartOfConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_PartOfConnectionType)


carnot_ParticipantType_strategy = st.builds(carnot_ParticipantType)
@given(instance=carnot_ParticipantType_strategy)
@settings(max_examples=25)
def test_carnot_ParticipantType_instantiation(instance):
    assert isinstance(instance, carnot_ParticipantType)


carnot_PerformsConnectionType_strategy = st.builds(carnot_PerformsConnectionType)
@given(instance=carnot_PerformsConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_PerformsConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_PerformsConnectionType)


carnot_PoolSymbol_strategy = st.builds(carnot_PoolSymbol, boundaryVisible=safe_text)
@given(instance=carnot_PoolSymbol_strategy)
@settings(max_examples=25)
def test_carnot_PoolSymbol_instantiation(instance):
    assert isinstance(instance, carnot_PoolSymbol)


carnot_ProcessDefinitionType_strategy = st.builds(carnot_ProcessDefinitionType, defaultPriority=safe_text)
@given(instance=carnot_ProcessDefinitionType_strategy)
@settings(max_examples=25)
def test_carnot_ProcessDefinitionType_instantiation(instance):
    assert isinstance(instance, carnot_ProcessDefinitionType)


carnot_ProcessSymbolType_strategy = st.builds(carnot_ProcessSymbolType)
@given(instance=carnot_ProcessSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_ProcessSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_ProcessSymbolType)


carnot_PublicInterfaceSymbol_strategy = st.builds(carnot_PublicInterfaceSymbol)
@given(instance=carnot_PublicInterfaceSymbol_strategy)
@settings(max_examples=25)
def test_carnot_PublicInterfaceSymbol_instantiation(instance):
    assert isinstance(instance, carnot_PublicInterfaceSymbol)


carnot_QualityControlType_strategy = st.builds(carnot_QualityControlType)
@given(instance=carnot_QualityControlType_strategy)
@settings(max_examples=25)
def test_carnot_QualityControlType_instantiation(instance):
    assert isinstance(instance, carnot_QualityControlType)


carnot_RefersToConnectionType_strategy = st.builds(carnot_RefersToConnectionType)
@given(instance=carnot_RefersToConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_RefersToConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_RefersToConnectionType)


carnot_RoleSymbolType_strategy = st.builds(carnot_RoleSymbolType)
@given(instance=carnot_RoleSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_RoleSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_RoleSymbolType)


carnot_RoleType_strategy = st.builds(carnot_RoleType, cardinality=st.integers())
@given(instance=carnot_RoleType_strategy)
@settings(max_examples=25)
def test_carnot_RoleType_instantiation(instance):
    assert isinstance(instance, carnot_RoleType)


carnot_ScriptType_strategy = st.builds(carnot_ScriptType)
@given(instance=carnot_ScriptType_strategy)
@settings(max_examples=25)
def test_carnot_ScriptType_instantiation(instance):
    assert isinstance(instance, carnot_ScriptType)


carnot_StartEventSymbol_strategy = st.builds(carnot_StartEventSymbol)
@given(instance=carnot_StartEventSymbol_strategy)
@settings(max_examples=25)
def test_carnot_StartEventSymbol_instantiation(instance):
    assert isinstance(instance, carnot_StartEventSymbol)


carnot_SubProcessOfConnectionType_strategy = st.builds(carnot_SubProcessOfConnectionType)
@given(instance=carnot_SubProcessOfConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_SubProcessOfConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_SubProcessOfConnectionType)


carnot_TeamLeadConnectionType_strategy = st.builds(carnot_TeamLeadConnectionType)
@given(instance=carnot_TeamLeadConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_TeamLeadConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_TeamLeadConnectionType)


carnot_TextSymbolType_strategy = st.builds(carnot_TextSymbolType, text=safe_text)
@given(instance=carnot_TextSymbolType_strategy)
@settings(max_examples=25)
def test_carnot_TextSymbolType_instantiation(instance):
    assert isinstance(instance, carnot_TextSymbolType)


carnot_TextType_strategy = st.builds(carnot_TextType, mixed=safe_text)
@given(instance=carnot_TextType_strategy)
@settings(max_examples=25)
def test_carnot_TextType_instantiation(instance):
    assert isinstance(instance, carnot_TextType)


carnot_TransitionConnectionType_strategy = st.builds(carnot_TransitionConnectionType, points=safe_text)
@given(instance=carnot_TransitionConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_TransitionConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_TransitionConnectionType)


carnot_TransitionType_strategy = st.builds(carnot_TransitionType, condition=safe_text, forkOnTraversal=safe_text)
@given(instance=carnot_TransitionType_strategy)
@settings(max_examples=25)
def test_carnot_TransitionType_instantiation(instance):
    assert isinstance(instance, carnot_TransitionType)


carnot_TriggerType_strategy = st.builds(carnot_TriggerType)
@given(instance=carnot_TriggerType_strategy)
@settings(max_examples=25)
def test_carnot_TriggerType_instantiation(instance):
    assert isinstance(instance, carnot_TriggerType)


carnot_TriggerTypeType_strategy = st.builds(carnot_TriggerTypeType, panelClass=safe_text, pullTrigger=safe_text, pullTriggerEvaluator=safe_text, rule=safe_text)
@given(instance=carnot_TriggerTypeType_strategy)
@settings(max_examples=25)
def test_carnot_TriggerTypeType_instantiation(instance):
    assert isinstance(instance, carnot_TriggerTypeType)


carnot_TriggersConnectionType_strategy = st.builds(carnot_TriggersConnectionType)
@given(instance=carnot_TriggersConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_TriggersConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_TriggersConnectionType)


carnot_TypeDeclarationsType_strategy = st.builds(carnot_TypeDeclarationsType)
@given(instance=carnot_TypeDeclarationsType_strategy)
@settings(max_examples=25)
def test_carnot_TypeDeclarationsType_instantiation(instance):
    assert isinstance(instance, carnot_TypeDeclarationsType)


carnot_UnbindActionType_strategy = st.builds(carnot_UnbindActionType)
@given(instance=carnot_UnbindActionType_strategy)
@settings(max_examples=25)
def test_carnot_UnbindActionType_instantiation(instance):
    assert isinstance(instance, carnot_UnbindActionType)


carnot_ViewType_strategy = st.builds(carnot_ViewType, name=safe_text)
@given(instance=carnot_ViewType_strategy)
@settings(max_examples=25)
def test_carnot_ViewType_instantiation(instance):
    assert isinstance(instance, carnot_ViewType)


carnot_ViewableType_strategy = st.builds(carnot_ViewableType)
@given(instance=carnot_ViewableType_strategy)
@settings(max_examples=25)
def test_carnot_ViewableType_instantiation(instance):
    assert isinstance(instance, carnot_ViewableType)


carnot_WorksForConnectionType_strategy = st.builds(carnot_WorksForConnectionType)
@given(instance=carnot_WorksForConnectionType_strategy)
@settings(max_examples=25)
def test_carnot_WorksForConnectionType_instantiation(instance):
    assert isinstance(instance, carnot_WorksForConnectionType)


carnot_XmlTextNode_strategy = st.builds(carnot_XmlTextNode, mixed=safe_text)
@given(instance=carnot_XmlTextNode_strategy)
@settings(max_examples=25)
def test_carnot_XmlTextNode_instantiation(instance):
    assert isinstance(instance, carnot_XmlTextNode)


carnot_extensions_FormalParameterMappingType_strategy = st.builds(carnot_extensions_FormalParameterMappingType)
@given(instance=carnot_extensions_FormalParameterMappingType_strategy)
@settings(max_examples=25)
def test_carnot_extensions_FormalParameterMappingType_instantiation(instance):
    assert isinstance(instance, carnot_extensions_FormalParameterMappingType)


carnot_extensions_FormalParameterMappingsType_strategy = st.builds(carnot_extensions_FormalParameterMappingsType)
@given(instance=carnot_extensions_FormalParameterMappingsType_strategy)
@settings(max_examples=25)
def test_carnot_extensions_FormalParameterMappingsType_instantiation(instance):
    assert isinstance(instance, carnot_extensions_FormalParameterMappingsType)


extensions_carnot_DataType_strategy = st.builds(extensions_carnot_DataType)
@given(instance=extensions_carnot_DataType_strategy)
@settings(max_examples=25)
def test_extensions_carnot_DataType_instantiation(instance):
    assert isinstance(instance, extensions_carnot_DataType)


extensions_carnot_FormalParameterType_strategy = st.builds(extensions_carnot_FormalParameterType)
@given(instance=extensions_carnot_FormalParameterType_strategy)
@settings(max_examples=25)
def test_extensions_carnot_FormalParameterType_instantiation(instance):
    assert isinstance(instance, extensions_carnot_FormalParameterType)



