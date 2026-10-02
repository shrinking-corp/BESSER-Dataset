#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    AbstractEventAction,
    AbstractEventSymbol,
    ActivityImplementationType,
    DiagramModeType,
    DirectionType,
    Enum,
    FlowControlType,
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
    abstractmethod,
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
    date,
    datetime,
    extensions_carnot_DataType,
    extensions_carnot_FormalParameterType,
    time,
)


def test_0():
    var_0 = lambda *args, **kwargs: "ecD\x0b,CW=MHzWI]vT9"
    var_1 = python_code_.carnot_TransitionConnectionType(
        points=b"*\xb5\xd9\xcf\xd4\x91\x1a", TransitionConnectionType353=var_0
    )
    assert isinstance(var_1, python_code_.carnot_TransitionConnectionType)
    var_2 = "?d$"
    var_3 = python_code_.carnot_ParameterMappingType(
        dataPath=var_1,
        parameter=var_2,
        parameterPath=var_0,
        ParameterMappingType="carnot_TypeDeclarationsType",
    )
    assert isinstance(var_3, python_code_.carnot_ParameterMappingType)
    var_4 = python_code_.carnot_AbstractEventSymbol(label=set())
    assert isinstance(var_4, python_code_.carnot_AbstractEventSymbol)
    var_6 = python_code_.carnot_extensions_FormalParameterMappingsType()
    assert isinstance(var_6, python_code_.carnot_extensions_FormalParameterMappingsType)
    var_6.setMappedData(carnot_data=(), carnot_formalParameter=var_0)
    var_9 = python_code_.carnot_IIdentifiableModelElement()
    var_9.getSymbols()


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = python_code_.IAccessPointOwner()
    var_4 = python_code_.ISwimlaneSymbol
    python_code_.carnot_PoolSymbol(
        boundaryVisible=var_4,
        PoolSymbol201=var_4,
        carnot_PoolSymbol=True,
        parentPool=var_0,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = python_code_.carnot_ITypedElement()
    var_3 = python_code_.IIdentifiableElement()
    var_6 = "_carnot_AttributeType__carnot_AttributeType"
    var_7 = python_code_.carnot_extensions_FormalParameterMappingsType
    python_code_.carnot_Code(code=var_6, value=var_6, name=var_7)
    var_9 = "carnot_DataType226,_carnot_XmlTextNode__carnot_XmlTextNode,_carnot_DataType__data,carnot_TransitionConnectionType"
    var_10 = "OR"
    var_11 = python_code_.carnot_INodeSymbol(
        shape=var_9, xPos=var_6, yPos={True, "w", 1}, width=var_9, height=var_0
    )
    assert isinstance(var_11, python_code_.carnot_INodeSymbol)
    var_12 = var_11.getInConnectionFeatures()
    var_13 = python_code_.carnot_EventConditionTypeType(
        pullEventEmitterClass=var_6,
        rule=var_9,
        activityCondition=var_9,
        binderClass=var_10,
        implementation=b"\x06u#\x02\x02,U\xa1\x02\xdb\x10\xc1A\x96EN\x91B]",
        panelClass=512,
        processCondition=var_7,
        type178=var_12,
        EventConditionTypeType=True,
        carnot_EventConditionTypeType=var_11,
    )
    assert isinstance(var_13, python_code_.carnot_EventConditionTypeType)
    var_15 = python_code_.carnot_IModelElement(elementOid=var_6)
    assert isinstance(var_15, python_code_.carnot_IModelElement)
    var_16 = python_code_.carnot_IMetaType(isPredefined=var_3)
    assert isinstance(var_16, python_code_.carnot_IMetaType)
    var_17 = var_0.getMetaType()
    var_23 = "\\)eFkB8HD/"
    var_25 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor=["FFV>J"], targetAnchor=var_17, routing=var_23
    )
    assert isinstance(var_25, python_code_.carnot_IConnectionSymbol)
    var_26 = var_25.getTargetNode()
    var_27 = python_code_.carnot_IModelParticipantSymbol
    var_28 = python_code_.carnot_extensions_FormalParameterMappingsType()
    assert isinstance(
        var_28, python_code_.carnot_extensions_FormalParameterMappingsType
    )
    var_29 = python_code_.carnot_GroupSymbolType
    var_30 = var_28.getMappedData(carnot_formalParameter=var_29)
    var_31 = var_25.setSourceNode(carnot_nodeSymbol=var_27)
    var_32 = lambda *args, **kwargs: 816
    var_33 = python_code_.carnot_IModelElementNodeSymbol()
    var_34 = var_33.getModelElement()
    python_code_.carnot_ISymbolContainer(
        nodes=1035.86,
        connections=var_27,
        carnot_ISymbolContainer46=(1231.88,),
        carnot_ISymbolContainer36=True,
        carnot_ISymbolContainer38=var_30,
        carnot_ISymbolContainer=var_26,
        carnot_ISymbolContainer12=var_31,
        carnot_ISymbolContainer26=-123.28,
        carnot_ISymbolContainer14=var_27,
        carnot_ISymbolContainer42=var_32,
        carnot_ISymbolContainer52=var_34,
    )


def test_3():
    var_1 = python_code_.carnot_IFlowObjectSymbol()
    var_2 = "_carnot_ISymbolContainer__carnot_ISymbolContainer50._carnot_IGraphicalObject__to"
    var_3 = python_code_.carnot_IGraphicalObject
    var_4 = python_code_.carnot_ApplicationTypeType(
        synchronous=None,
        validatorClass=var_2,
        accessPointProviderClass=var_1,
        instanceClass=var_3,
        panelClass="_carnot_GatewaySymbol__carnot_GatewaySymbol",
        carnot_ApplicationTypeType=(-993, False),
    )
    assert isinstance(var_4, python_code_.carnot_ApplicationTypeType)
    var_8 = "1=6EtpoS/8G~<Q!"
    var_9 = python_code_.carnot_GenericLinkConnectionType()
    var_10 = python_code_.carnot_INodeSymbol(
        shape=(),
        xPos=var_4,
        yPos=-1533,
        width="U5=,G<Sp%Xa$7",
        height=var_8,
        INodeSymbol=var_9,
    )
    assert isinstance(var_10, python_code_.carnot_INodeSymbol)
    var_10.getOutConnectionFeatures()


def test_4():
    var_3 = "_carnot_TriggerTypeType__TriggerTypeType,_carnot_ISymbolContainer__carnot_ISymbolContainer34,_carnot_ISymbolContainer__carnot_ISymbolContainer30"
    var_4 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor=var_3, targetAnchor=2700.9, routing=var_3
    )
    assert isinstance(var_4, python_code_.carnot_IConnectionSymbol)
    var_6 = python_code_.carnot_IIdentifiableElement
    var_7 = python_code_.carnot_EventActionTypeType(
        actionClass=var_3,
        activityAction=None,
        panelClass=var_3,
        processAction=var_3,
        supportedConditionTypes=var_6,
        unsupportedContexts=complex(1025.2, 1004.6),
        EventActionTypeType=False,
    )
    assert isinstance(var_7, python_code_.carnot_EventActionTypeType)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.AbstractEventSymbol()
    var_3 = (
        "_carnot_ModelType__carnot_ModelType219-_carnot_ModelType__carnot_ModelType231"
    )
    var_5 = 'T3OZ@;"s~n+X\x0bpU'
    var_6 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor=var_3,
        targetAnchor=3278,
        routing=var_5,
        carnot_IConnectionSymbol=b"\xa0FX\x06\x02\x13\x1d*",
    )
    assert isinstance(var_6, python_code_.carnot_IConnectionSymbol)
    var_6.getSourceNode()
    var_8 = python_code_.carnot_DescriptionType(mixed=var_0)
    var_9 = python_code_.carnot_IModelElementNodeSymbol()
    var_9.getModelElement()
    python_code_.carnot_IIdentifiableModelElement(
        carnot_IIdentifiableModelElement=var_8
    )


def test_6():
    var_0 = python_code_.carnot_IdentifiableReference()
    var_1 = "//a4>"
    var_2 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor=var_0, targetAnchor=var_1, routing=var_1
    )
    assert isinstance(var_2, python_code_.carnot_IConnectionSymbol)
    var_3 = "targetActivitySymbol_carnot_ViewType__carnot_ViewType372carnot_RoleType"
    var_4 = python_code_.carnot_INodeSymbol(
        shape=var_2, xPos=var_1, yPos=var_2, width=None, height=var_3
    )
    assert isinstance(var_4, python_code_.carnot_INodeSymbol)
    var_4.getInConnectionFeatures()
    var_7 = "_carnot_DataType__DataType146 _carnot_ParameterMappingType__ParameterMappingType"
    var_8 = python_code_.carnot_ModelerSymbolType()
    var_9 = python_code_.carnot_ModelerType(
        email=var_4, password=var_7, ModelerType=var_8
    )
    assert isinstance(var_9, python_code_.carnot_ModelerType)


def test_7():
    var_2 = python_code_.carnot_StartEventSymbol()
    var_3 = "-#]hA[L$cP8kvZ: Xq-"
    var_4 = python_code_.carnot_IMetaType(isPredefined=var_3)
    assert isinstance(var_4, python_code_.carnot_IMetaType)
    var_4.getExtensionPointId()
    var_7 = python_code_.carnot_TextSymbolType(text=var_2)
    assert isinstance(var_7, python_code_.carnot_TextSymbolType)
