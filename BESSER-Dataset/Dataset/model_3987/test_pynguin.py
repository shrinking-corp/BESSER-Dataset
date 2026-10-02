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
    date,
    datetime,
    extensions_carnot_DataType,
    extensions_carnot_FormalParameterType,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.carnot_EndEventSymbol()
    var_1 = "$Y?^A9[[Af)m\\qc"
    var_2 = "carnot_TriggerType"
    var_3 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor=var_1,
        targetAnchor={
            "carnot_EventActionTypeType-carnot_ViewType374-_carnot_ModelType__carnot_ModelType244-carnot_IIdentifiableModelElement": True,
            "_carnot_ModelType__carnot_ModelType.EmptyRhombus._carnot_RoleType__carnot_RoleType": 1287.65,
            "yFxK[ikNz?K=s": 2757,
        },
        routing=var_2,
    )
    assert isinstance(var_3, python_code_.carnot_IConnectionSymbol)
    var_3.setTargetNode(carnot_nodeSymbol=var_1)
    var_5 = python_code_.LinkColor
    var_7 = "l]mtfS,ADs"
    var_8 = python_code_.carnot_DescriptionType(
        mixed=var_7, carnot_DescriptionType=var_5
    )
    var_9 = "_[7j-~}q{o'QB"
    var_10 = "5> e L`\x0c~l(%9-5a"
    var_11 = "'tt5rc;CDF{R"
    var_12 = python_code_.carnot_AttributeType(
        group=var_1,
        any=var_1,
        mixed=var_9,
        name=var_10,
        type=(False,),
        value=var_11,
        AttributeType=var_5,
    )
    var_13 = var_12.setAttributeValue(
        carnot_type=var_3,
        carnot_value=(
            348.22,
            "_carnot_ActivityType__carnot_ActivityType283.ApplicationType126.data153.TransitionType344",
        ),
    )
    var_14 = python_code_.carnot_extensions_FormalParameterMappingsType(
        carnot_extensions_FormalParameterMappingsType=var_5
    )
    assert isinstance(
        var_14, python_code_.carnot_extensions_FormalParameterMappingsType
    )
    var_15 = var_14.setMappedData(
        carnot_formalParameter="=<{%mfO\ry6+S\tjzp]L",
        carnot_data=b"<h\x82\xe15\xd4u(\x08f_\x89\xa9b\xde\xd0\x8c",
    )
    python_code_.carnot_ModelType(
        author=var_2,
        carnotVersion=var_0,
        created=[],
        modelOID=[],
        oid=var_7,
        vendor=var_5,
        carnot_ModelType218=var_5,
        carnot_ModelType224=set(),
        carnot_ModelType227=b"/",
        carnot_ModelType232="_carnot_ActivityType__ActivityType,_carnot_DataTypeType__carnot_DataTypeType212,_carnot_ProcessDefinitionType__implementationProcess",
        carnot_ModelType208=var_8,
        carnot_ModelType216="j\\XD SgAa3vlXH",
        carnot_ModelType234=var_13,
        carnot_ModelType252=var_15,
        carnot_ModelType242=[True, -1290.33],
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = python_code_.carnot_extensions_FormalParameterMappingsType()
    assert isinstance(var_0, python_code_.carnot_extensions_FormalParameterMappingsType)
    var_1 = python_code_.carnot_AttributeType
    var_0.getMappedData(carnot_formalParameter=var_1)
    var_4 = python_code_.carnot_IIdentifiableModelElement()
    var_4.getSymbols()
    var_7 = "/\rw\x0cS:\tu&I$GE\\+)X["
    var_8 = python_code_.carnot_EventHandlerType(
        unbindOnMatch=var_0, autoBind=var_7, consumeOnMatch={}, logHandler=var_7
    )
    assert isinstance(var_8, python_code_.carnot_EventHandlerType)
    var_10 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor=var_1, targetAnchor=var_0, routing=var_4
    )
    assert isinstance(var_10, python_code_.carnot_IConnectionSymbol)
    python_code_.carnot_ApplicationContextTypeType(
        validatorClass=var_7,
        accessPointProviderClass=[],
        hasApplicationPath=set(),
        hasMappingId=var_4,
        panelClass=(),
        type=var_1,
    )


def test_2():
    var_1 = "!O3O#W,djj?OYYK)"
    var_2 = python_code_.carnot_DocumentRoot(mixed=var_1)
    assert isinstance(var_2, python_code_.carnot_DocumentRoot)
    var_4 = python_code_.carnot_AccessPointType(
        direction=var_1, carnot_AccessPointType=(0,)
    )
    assert isinstance(var_4, python_code_.carnot_AccessPointType)
    var_7 = python_code_.carnot_GroupSymbolType()
    var_8 = python_code_.carnot_ApplicationSymbolType()
    var_12 = python_code_.carnot_IIdentifiableModelElement()
    var_12.getSymbols()
    var_16 = "ac(~-"
    var_17 = python_code_.carnot_ITypedElement()
    var_18 = var_17.getMetaType()
    var_19 = python_code_.carnot_IGraphicalObject(
        fillColor=b"oVOH\xd4+\x96", style=var_16, borderColor=var_8, to=var_18
    )
    assert isinstance(var_19, python_code_.carnot_IGraphicalObject)
    var_21 = python_code_.carnot_extensions_FormalParameterMappingType
    var_22 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor="", targetAnchor=var_21, routing=var_1
    )
    assert isinstance(var_22, python_code_.carnot_IConnectionSymbol)
    var_25 = python_code_.carnot_IModelElementNodeSymbol()
    var_25.setModelElement(carnot_element=var_7)


@pytest.mark.xfail(strict=True)
def test_3():
    var_2 = python_code_.LinkColor.Yellow
    var_3 = "\x0c@AEHMg&\r>cd-"
    var_4 = dict
    var_5 = python_code_.carnot_DataPathType(
        dataPath=var_2,
        descriptor=complex(-6022.0, 1567.2486),
        key=var_3,
        direction=var_3,
        DataPathType=var_4,
    )
    assert isinstance(var_5, python_code_.carnot_DataPathType)
    var_8 = python_code_.carnot_extensions_FormalParameterMappingsType(
        carnot_extensions_FormalParameterMappingsType=None
    )
    assert isinstance(var_8, python_code_.carnot_extensions_FormalParameterMappingsType)
    var_8.getMappedData(carnot_formalParameter=var_4)
    var_10 = python_code_.carnot_ModelerSymbolType()
    python_code_.carnot_IdRef(ref=complex(-1393.100361, -68.513), carnot_IdRef192=var_8)
    var_13 = "OpenTriangle-_carnot_ISwimlaneSymbol__carnot_ISwimlaneSymbol-_carnot_ISymbolContainer__carnot_ISymbolContainer44-_carnot_ViewType__carnot_ViewType"
    var_14 = python_code_.carnot_PoolSymbol(boundaryVisible=var_13)
    assert isinstance(var_14, python_code_.carnot_PoolSymbol)
    var_16 = "+5F=L@1-%{a{p.=F"
    var_17 = "poolSymbols-carnot_DocumentRoot-_carnot_ApplicationContextTypeType__type"
    var_18 = python_code_.carnot_GenericLinkConnectionType()
    python_code_.carnot_INodeSymbol(
        xPos=var_16,
        yPos=var_16,
        width=var_17,
        height=var_3,
        shape="2*",
        targetSymbol=var_4,
        sourceSymbol=var_10,
        INodeSymbol=var_18,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = ""
    var_1 = ""
    var_2 = python_code_.carnot_XmlTextNode(
        mixed=[937.46],
        carnot_XmlTextNode347={
            "StartEventSymbol,_carnot_ISymbolContainer__carnot_ISymbolContainer56,RefersToConnectionType,_carnot_DiagramType__DiagramType"
        },
    )
    python_code_.carnot_AttributeType(
        group=var_0,
        any=var_0,
        mixed=var_1,
        name=None,
        type=var_1,
        value=var_0,
        carnot_AttributeType128=var_2,
        attribute=set(),
    )


def test_5():
    var_0 = python_code_.carnot_BindActionType()
    python_code_.carnot_TextType(mixed="")
    var_3 = python_code_.IIdentifiableModelElement()
    var_4 = "_carnot_TransitionType__TransitionTypeexecutedActivities_carnot_IdRef__carnot_IdRef192carnot_DataPathType"
    var_5 = python_code_.carnot_ITypedElement()
    var_6 = var_5.getMetaType()
    var_7 = python_code_.carnot_INodeSymbol(
        xPos=var_4,
        yPos=var_3,
        width=var_4,
        height=var_0,
        shape=var_4,
        sourceSymbol=var_6,
    )
    assert isinstance(var_7, python_code_.carnot_INodeSymbol)
    var_7.getOutConnectionFeatures()


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.carnot_TeamLeadConnectionType()
    var_1 = python_code_.carnot_IModelElementNodeSymbol()
    var_2 = var_1.getModelElement()
    var_3 = "#`6*7oq\r#j~"
    var_4 = lambda *args, **kwargs: [True, -357.92, 1462.41]
    var_5 = python_code_.carnot_DataPathType(
        dataPath=var_3, descriptor=var_4, key={}, direction=var_3, DataPathType=var_4
    )
    assert isinstance(var_5, python_code_.carnot_DataPathType)
    var_6 = python_code_.carnot_IMetaType(isPredefined=var_2)
    assert isinstance(var_6, python_code_.carnot_IMetaType)
    var_7 = var_6.getTypedElements()
    var_8 = python_code_.carnot_ExternalReferenceType()
    python_code_.carnot_DataType(
        predefined=var_0,
        data=var_2,
        DataType146=var_5,
        data155=var_7,
        carnot_DataType=var_8,
    )


def test_7():
    var_2 = "_carnot_ParameterMappingType__ParameterMappingType"
    var_3 = python_code_.carnot_IAccessPointOwner()
    var_4 = python_code_.carnot_AccessPointType(
        direction=var_2, carnot_AccessPointType=var_3
    )
    assert isinstance(var_4, python_code_.carnot_AccessPointType)


@pytest.mark.xfail(strict=True)
def test_8():
    var_1 = python_code_.carnot_LaneSymbol()
    var_2 = python_code_.carnot_ISwimlaneSymbol(
        orientation=complex(-428.3818, -3624.26169),
        collapsed=2,
        ISwimlaneSymbol202=var_1,
    )
    assert isinstance(var_2, python_code_.carnot_ISwimlaneSymbol)
    var_3 = "_carnot_IdRef__carnot_IdRef,dataMappings143,_carnot_ISymbolContainer__carnot_ISymbolContainer"
    var_4 = python_code_.carnot_IConnectionSymbol(
        sourceAnchor=complex(2829.8792, -1360.476874), targetAnchor=var_3, routing=var_3
    )
    assert isinstance(var_4, python_code_.carnot_IConnectionSymbol)
    var_5 = python_code_.IEventHandlerOwner
    var_6 = var_4.setSourceNode(carnot_nodeSymbol=var_5)
    var_7 = python_code_.carnot_GenericLinkConnectionType()
    var_8 = python_code_.carnot_AbstractEventSymbol(label=var_7)
    assert isinstance(var_8, python_code_.carnot_AbstractEventSymbol)
    var_10 = python_code_.carnot_ITypedElement()
    var_13 = python_code_.carnot_IModelElementNodeSymbol()
    var_14 = var_13.setModelElement(carnot_element=var_4)
    var_17 = "5|7FF76%J}pFg"
    var_18 = "_carnot_IGraphicalObject__from_.carnot_ModelType230._carnot_IModelElement__carnot_IModelElement"
    var_19 = var_10.getMetaType()
    var_20 = "cw-\\"
    var_21 = python_code_.carnot_IMetaType(isPredefined=var_20)
    assert isinstance(var_21, python_code_.carnot_IMetaType)
    var_22 = var_21.getTypedElements()
    var_23 = python_code_.carnot_INodeSymbol(
        xPos={
            "(}uf}<1u6a": 'S^$73?z8"k;AkZk7',
            "FilledTriangle,_carnot_DocumentRoot__carnot_DocumentRoot174": 3438.27,
        },
        yPos={},
        width=var_17,
        height=var_1,
        shape=var_17,
        INodeSymbol198=var_14,
    )
    assert isinstance(var_23, python_code_.carnot_INodeSymbol)
    var_24 = var_23.getOutConnectionFeatures()
    var_25 = python_code_.carnot_extensions_FormalParameterMappingsType()
    assert isinstance(
        var_25, python_code_.carnot_extensions_FormalParameterMappingsType
    )
    var_26 = (
        lambda *args, **kwargs: "carnot_DataMappingConnectionType_carnot_DataType__DataType146"
    )
    var_27 = var_25.getMappedData(carnot_formalParameter=var_26)
    var_28 = python_code_.carnot_AttributeType(
        group=var_18,
        any="=9rB+G!!Mm\x0c*ck/\\C",
        mixed=var_3,
        name=set(),
        type=var_7,
        value=var_6,
        carnot_AttributeType=(),
        attribute=var_26,
    )
    var_29 = var_28.getAttributeValue()
    var_30 = var_21.getTypedElements()
    python_code_.carnot_ISymbolContainer(
        nodes=var_17,
        connections=var_18,
        carnot_ISymbolContainer56=var_19,
        carnot_ISymbolContainer58=var_22,
        carnot_ISymbolContainer16=var_5,
        carnot_ISymbolContainer22=var_1,
        carnot_ISymbolContainer26=var_24,
        carnot_ISymbolContainer32=var_27,
        carnot_ISymbolContainer38=1,
        carnot_ISymbolContainer52=var_29,
        carnot_ISymbolContainer48=var_30,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = ";macwL#F>Gpcyr"
    var_1 = "IModelParticipant96-_carnot_ISymbolContainer__carnot_ISymbolContainer44"
    var_2 = "ActivitySymbolType,carnot_AccessPointType,participant"
    var_3 = lambda *args, **kwargs: "$H;;%(uKu&HPB\\g"
    var_4 = python_code_.carnot_IdentifiableReference()
    var_5 = python_code_.carnot_AttributeType(
        group=-1,
        any=var_0,
        mixed=var_0,
        name=var_1,
        type=var_1,
        value=var_2,
        carnot_AttributeType128=var_3,
        attribute=var_4,
    )
    var_6 = var_5.setAttributeValue(carnot_type=var_3, carnot_value=set())
    var_8 = python_code_.carnot_IModelElementNodeSymbol()
    var_9 = python_code_.IExtensibleElement()
    var_11 = python_code_.carnot_IMetaType(isPredefined=var_8)
    assert isinstance(var_11, python_code_.carnot_IMetaType)
    var_12 = var_11.getTypedElements()
    var_11.getExtensionPointId()
    var_14 = "carnot_Coordinates"
    var_15 = python_code_.carnot_INodeSymbol(
        xPos={-482.45, "E.y#\x0bKxmks%rC;'"},
        yPos=var_3,
        width=var_14,
        height=var_12,
        shape=var_2,
    )
    assert isinstance(var_15, python_code_.carnot_INodeSymbol)
    var_16 = var_15.getOutConnectionFeatures()
    var_17 = var_8.getModelElement()
    var_18 = var_5.getAttributeValue()
    var_19 = var_5.setAttributeValue(carnot_type=None, carnot_value=var_3)
    var_20 = var_5.getAttributeValue()
    var_21 = var_15.getInConnectionFeatures()
    var_22 = var_15.getOutConnectionFeatures()
    var_23 = var_11.getTypedElements()
    python_code_.carnot_ISymbolContainer(
        nodes=var_0,
        connections=var_5,
        carnot_ISymbolContainer16=var_16,
        carnot_ISymbolContainer=var_17,
        carnot_ISymbolContainer12=var_18,
        carnot_ISymbolContainer30=var_19,
        carnot_ISymbolContainer20=var_20,
        carnot_ISymbolContainer22=var_21,
        carnot_ISymbolContainer24=var_22,
        carnot_ISymbolContainer26=var_23,
        carnot_ISymbolContainer28="*\x0bU/-!B>Urcg,wv9",
        carnot_ISymbolContainer32=var_9,
        carnot_ISymbolContainer46=1199.85,
        carnot_ISymbolContainer50=var_6,
    )
