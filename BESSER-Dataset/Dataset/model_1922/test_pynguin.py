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
    Algorithm,
    ColorizableElement,
    CompilableType,
    CompositeFBType,
    ConfigurableObject,
    Connection,
    DataType,
    Enum,
    Event,
    FB,
    FBNetworkElement,
    FBType,
    I4DIACElement,
    IInterfaceElement,
    INamedElement,
    IVarElement,
    Language,
    LibraryElement,
    PositionableElement,
    Primitive,
    TextAlgorithm,
    TypedConfigureableObject,
    VarDeclaration,
    abstractmethod,
    date,
    datetime,
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
    time,
)


def test_0():
    var_0 = python_code_.libraryElement_ResourceTypeFB()
    var_1 = var_0.isResourceTypeFB()
    var_2 = python_code_.libraryElement_ECState(libraryElement_ECState37=var_1)
    assert isinstance(var_2, python_code_.libraryElement_ECState)
    var_3 = python_code_.libraryElement_ConfigurableObject()
    var_3.setParameter(libraryElement_parameterName={}, libraryElement_value=var_1)
    var_6 = python_code_.libraryElement_I4DIACElement()
    assert isinstance(var_6, python_code_.libraryElement_I4DIACElement)
    var_7 = var_6.createAnnotation(libraryElement_name=(False, 996.29, -1437.85))
    var_9 = "sg}J~^"
    var_10 = '2_o2aQZL#T!&\r9><"'
    var_11 = python_code_.libraryElement_ECC
    var_12 = python_code_.libraryElement_ECTransition(
        comment=var_9,
        conditionExpression=var_10,
        outTransitions=var_6,
        inTransitions=var_6,
        libraryElement_ECTransition46=var_7,
        ECTransition=var_11,
    )
    assert isinstance(var_12, python_code_.libraryElement_ECTransition)
    var_12.getConditionText()
    python_code_.libraryElement_DataConnection()


def test_1():
    var_0 = lambda *args, **kwargs: [True]
    var_1 = python_code_.libraryElement_AutomationSystem(
        project=complex(3854.0, 3725.498018), libraryElement_AutomationSystem123=var_0
    )
    assert isinstance(var_1, python_code_.libraryElement_AutomationSystem)
    python_code_.libraryElement_DataConnection()


def test_2():
    python_code_.libraryElement_TypedConfigureableObject()
    var_11 = python_code_.libraryElement_EventConnection()
    var_11.getSource()
    python_code_.libraryElement_InterfaceList(
        libraryElement_InterfaceList63=[False, False, -4.63],
        libraryElement_InterfaceList72="4,E|TCJ&5o_",
    )


def test_3():
    python_code_.libraryElement_ResourceTypeFB()
    python_code_.libraryElement_ConfigurableObject()
    var_6 = python_code_.libraryElement_I4DIACElement()
    assert isinstance(var_6, python_code_.libraryElement_I4DIACElement)
    var_19 = python_code_.libraryElement_AdapterConnection()
    var_21 = python_code_.libraryElement_DataConnection()
    var_22 = var_21.getDestination()
    var_23 = python_code_.libraryElement_DeviceType(
        profile={}, libraryElement_DeviceType=var_22
    )
    assert isinstance(var_23, python_code_.libraryElement_DeviceType)
    var_27 = python_code_.libraryElement_AdapterFBType()
    var_28 = python_code_.libraryElement_AdapterType(libraryElement_AdapterType=var_27)
    assert isinstance(var_28, python_code_.libraryElement_AdapterType)
    var_28.getInterfaceList()
    var_30 = python_code_.libraryElement_FB()
    var_30.isResourceTypeFB()
    var_19.getDestination()


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.libraryElement_EventConnection()
    var_1 = var_0.getSource()
    var_2 = python_code_.libraryElement_SubApp()
    var_3 = "<`4}3epP"
    var_4 = python_code_.libraryElement_LibraryElement()
    python_code_.libraryElement_Identification(
        function=var_2,
        standard=var_1,
        type=var_3,
        applicationDomain=complex(337.619, 3342.1197),
        classification=var_3,
        description=var_0,
        libraryElement_Identification=var_4,
    )
    var_6 = "_libraryElement_ECState__libraryElement_ECState"
    var_7 = "1(|DCshNJG-qs\\"
    python_code_.libraryElement_IInterfaceElement(
        isInput=var_6,
        typeName=var_0,
        IInterfaceElement=var_7,
        IInterfaceElement12=var_3,
        destination138=var_2,
        libraryElement_IInterfaceElement=":\n]Aa>",
    )


def test_5():
    var_0 = python_code_.libraryElement_AdapterEvent()
    var_1 = python_code_.libraryElement_Mapping()
    var_2 = "_libraryElement_Segment__libraryElement_Segment"
    var_3 = python_code_.libraryElement_Connection(
        dx1=var_0,
        dx2=(),
        dy=var_2,
        resTypeConnection=var_1,
        brokenConnection="/",
        Connection=b"\x83L\x92\xf9\xe3t\xcf",
        Connection141=var_1,
    )
    assert isinstance(var_3, python_code_.libraryElement_Connection)
    var_3.getSourceElement()


def test_6():
    var_0 = python_code_.libraryElement_Link
    var_1 = python_code_.libraryElement_AdapterType(libraryElement_AdapterType157=var_0)
    assert isinstance(var_1, python_code_.libraryElement_AdapterType)
    var_1.getSocketType()
    var_3 = python_code_.libraryElement_InterfaceList()
    var_3.getInterfaceElement(libraryElement_name=var_0)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.libraryElement_FBNetworkElement(
        libraryElement_FBNetworkElement81={1155.49, 0, True},
        libraryElement_FBNetworkElement84={
            "'": -5124.25,
            "libraryElement_FBNetworkElement81": False,
        },
    )
    assert isinstance(var_0, python_code_.libraryElement_FBNetworkElement)
    python_code_.libraryElement_InterfaceList(libraryElement_InterfaceList=var_0)


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = lambda *args, **kwargs: [True]
    var_1 = python_code_.libraryElement_AutomationSystem(
        project=complex(3854.0, 3725.498018), libraryElement_AutomationSystem123=var_0
    )
    assert isinstance(var_1, python_code_.libraryElement_AutomationSystem)
    var_2 = python_code_.libraryElement_Application(libraryElement_Application117=var_1)
    assert isinstance(var_2, python_code_.libraryElement_Application)
    var_3 = python_code_.libraryElement_FBNetworkElement(
        libraryElement_FBNetworkElement52=var_2,
        libraryElement_FBNetworkElement81=complex(-244.405, 622.6632446),
    )
    assert isinstance(var_3, python_code_.libraryElement_FBNetworkElement)
    var_4 = var_3.getInterfaceElement(libraryElement_name=var_3)
    python_code_.libraryElement_DataConnection()
    var_9 = python_code_.libraryElement_SubApp(libraryElement_SubApp=var_4)
    assert isinstance(var_9, python_code_.libraryElement_SubApp)
    python_code_.libraryElement_FBNetwork(
        libraryElement_FBNetwork24=426.87,
        libraryElement_FBNetwork54=var_9,
        libraryElement_FBNetwork94=b"\xd4c\xf1\x87\x00\x83\xb4\xd2",
        libraryElement_FBNetwork113=var_4,
    )


def test_9():
    var_9 = python_code_.libraryElement_SubApp()
    var_9.getType()
    var_11 = python_code_.libraryElement_ConfigurableObject(
        libraryElement_ConfigurableObject=set()
    )
    assert isinstance(var_11, python_code_.libraryElement_ConfigurableObject)
    var_11.getParameter(libraryElement_parameterName=None)
    var_20 = python_code_.libraryElement_AdapterType(
        libraryElement_AdapterType157="U/{D\t)<DPp"
    )
    assert isinstance(var_20, python_code_.libraryElement_AdapterType)
    var_20.getInterfaceList()


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = python_code_.libraryElement_ResourceTypeFB()
    var_1 = var_0.isResourceTypeFB()
    var_2 = python_code_.libraryElement_ECState(libraryElement_ECState37=var_1)
    assert isinstance(var_2, python_code_.libraryElement_ECState)
    python_code_.libraryElement_ConfigurableObject()
    var_19 = python_code_.libraryElement_CompositeFBType()
    python_code_.libraryElement_FBNetwork(
        libraryElement_FBNetwork87="a\tl\"Jw1'>]K-=Q,EX_J",
        libraryElement_FBNetwork136=var_19,
    )
    var_21 = python_code_.libraryElement_EventConnection()
    var_21.getDestination()
    var_23 = python_code_.libraryElement_FBNetworkElement(
        libraryElement_FBNetworkElement109=complex(-3743.4502, -493.5)
    )
    assert isinstance(var_23, python_code_.libraryElement_FBNetworkElement)
    python_code_.libraryElement_Application()
    var_28 = lambda *args, **kwargs: [False, -632]
    var_29 = python_code_.libraryElement_Device(profile=var_28)
    assert isinstance(var_29, python_code_.libraryElement_Device)
    var_30 = var_29.getAutomationSystem()
    var_31 = "libraryElement_ServiceTransaction"
    var_32 = python_code_.libraryElement_AutomationSystem(
        project=var_31,
        automationSystem=var_30,
        libraryElement_AutomationSystem123=(".5~p,{Zz_fEycI[\x0c",),
    )
    assert isinstance(var_32, python_code_.libraryElement_AutomationSystem)
    var_33 = python_code_.libraryElement_AdapterDeclaration()
    var_34 = python_code_.libraryElement_AdapterFB(AdapterFB=var_33)
    assert isinstance(var_34, python_code_.libraryElement_AdapterFB)
    var_35 = var_34.getType()
    python_code_.libraryElement_SystemConfiguration(
        libraryElement_SystemConfiguration=var_32,
        libraryElement_SystemConfiguration148=var_35,
    )


def test_11():
    var_3 = python_code_.libraryElement_ConfigurableObject()
    var_3.setParameter(libraryElement_parameterName=1380.3, libraryElement_value=244.26)
    var_6 = python_code_.libraryElement_I4DIACElement()
    assert isinstance(var_6, python_code_.libraryElement_I4DIACElement)
    var_6.createAnnotation(libraryElement_name=(False, 996.29, -1437.85))
    var_9 = "sg}~^"
    var_17 = python_code_.libraryElement_ResourceTypeFB()
    var_24 = python_code_.libraryElement_DataType
    var_25 = "zPfw&N"
    var_26 = python_code_.libraryElement_IInterfaceElement(
        isInput=var_9, typeName=var_9
    )
    assert isinstance(var_26, python_code_.libraryElement_IInterfaceElement)
    var_27 = python_code_.libraryElement_Connection(
        dx1=var_17,
        dx2=var_24,
        dy=var_24,
        resTypeConnection=var_25,
        brokenConnection=var_9,
        Connection=var_26,
        Connection141=var_24,
    )
    assert isinstance(var_27, python_code_.libraryElement_Connection)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.libraryElement_DataConnection()
    var_1 = var_0.getSource()
    var_2 = lambda *args, **kwargs: [-550, False]
    var_3 = "C-_libraryElement_Color__libraryElement_Color"
    var_4 = python_code_.libraryElement_IInterfaceElement(isInput=var_3, typeName=var_3)
    assert isinstance(var_4, python_code_.libraryElement_IInterfaceElement)
    python_code_.libraryElement_Connection(
        dx1=var_1,
        dx2=var_2,
        dy=var_1,
        resTypeConnection=var_2,
        brokenConnection=var_3,
        inputConnections=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = ""
    var_1 = "abJ<M~h.-\t|r.]j^"
    var_2 = "##l8,/x"
    var_3 = "libraryElement_Segment"
    var_4 = "source_libraryElement_ECTransition__outTransitionslibraryElement_ServiceSequence"
    var_5 = "X!}iA}}DO^3@"
    var_6 = python_code_.libraryElement_IInterfaceElement(isInput=var_5, typeName=var_0)
    assert isinstance(var_6, python_code_.libraryElement_IInterfaceElement)
    var_7 = python_code_.libraryElement_Connection(
        dx1=["FB"],
        dx2=var_3,
        dy=var_2,
        resTypeConnection=var_4,
        brokenConnection=774,
        inputConnections="!dlxpDf(-C\x0b10B8oI\x0b",
        Connection=var_6,
    )
    assert isinstance(var_7, python_code_.libraryElement_Connection)
    var_8 = python_code_.libraryElement_DataType()
    python_code_.libraryElement_IInterfaceElement(
        isInput=var_2,
        typeName=b"7\xf2\xbdA\xd80",
        IInterfaceElement=var_7,
        destination138=var_1,
        libraryElement_IInterfaceElement=var_8,
    )


def test_14():
    var_3 = "_libraryElement_InterfaceList__libraryElement_InterfaceList69"
    var_4 = python_code_.libraryElement_IInterfaceElement(
        isInput="_libraryElement_Segment__libraryElement_Segment149C_libraryElement_DeviceType__libraryElement_DeviceTypeClibraryElement_IInterfaceElement144",
        typeName=var_3,
    )
    assert isinstance(var_4, python_code_.libraryElement_IInterfaceElement)
    var_11 = python_code_.libraryElement_InterfaceList(
        libraryElement_InterfaceList63=[False, False, -4.63],
        libraryElement_InterfaceList72="4,E|TCJ&5o_",
    )
    var_11.getVariable(libraryElement_name=None)


def test_15():
    var_0 = "libraryElement_Palette"
    var_1 = "&}to:fe%)buAEz04T,4"
    var_2 = python_code_.libraryElement_ResourceTypeFB
    var_3 = python_code_.libraryElement_Connection(
        dx1=var_0,
        dx2=var_0,
        dy=var_0,
        resTypeConnection=var_1,
        brokenConnection=var_0,
        outputConnections=var_2,
        Connection=[3],
    )
    assert isinstance(var_3, python_code_.libraryElement_Connection)
    var_3.getSourceElement()


@pytest.mark.xfail(strict=True)
def test_16():
    var_0 = python_code_.libraryElement_I4DIACElement()
    assert isinstance(var_0, python_code_.libraryElement_I4DIACElement)
    var_1 = python_code_.ConfigurableObject
    var_0.createAnnotation(libraryElement_name=var_1)
    var_6 = "s"
    var_10 = "\\cFX>#OJ\\"
    var_11 = python_code_.libraryElement_Connection(
        dx1=var_6,
        dx2=var_6,
        dy="libraryElement_FBNetworkElement81C_libraryElement_SystemConfiguration__libraryElement_SystemConfiguration146",
        resTypeConnection=var_10,
        brokenConnection="p.00R+QK>IE O,",
        Connection="iPy\\fz7zSF%= .$A|j",
        Connection141=False,
    )
    assert isinstance(var_11, python_code_.libraryElement_Connection)
    var_14 = python_code_.libraryElement_CompositeFBType()
    var_15 = python_code_.libraryElement_FBNetwork(
        libraryElement_FBNetwork87="a\tl\"Jw1'>]K-=Q,EX_J",
        libraryElement_FBNetwork136=var_14,
    )
    var_16 = python_code_.libraryElement_FBNetworkElement(
        libraryElement_FBNetworkElement=var_11,
        libraryElement_FBNetworkElement109=var_15,
        libraryElement_FBNetworkElement81=-748.9,
    )
    assert isinstance(var_16, python_code_.libraryElement_FBNetworkElement)
    var_19 = python_code_.libraryElement_EventConnection()
    var_19.getDestination()
    python_code_.libraryElement_FBNetworkElement(
        libraryElement_FBNetworkElement109=complex(-3743.4502, -493.5)
    )
    python_code_.libraryElement_Application()
    var_30 = lambda *args, **kwargs: [False, -632]
    var_31 = python_code_.libraryElement_Device(profile=var_30)
    assert isinstance(var_31, python_code_.libraryElement_Device)
    var_32 = var_31.getAutomationSystem()
    var_33 = python_code_.libraryElement_Annotation(
        name=var_10, servity=var_1, libraryElement_Annotation=var_0
    )
    assert isinstance(var_33, python_code_.libraryElement_Annotation)
    var_34 = "libraryElement_ServiceTransaction"
    var_35 = python_code_.libraryElement_AutomationSystem(
        project=var_34,
        automationSystem=var_32,
        libraryElement_AutomationSystem123=(".5~p,{Zz_fEycI[\x0c",),
    )
    assert isinstance(var_35, python_code_.libraryElement_AutomationSystem)
    var_36 = python_code_.libraryElement_AdapterDeclaration()
    var_37 = python_code_.libraryElement_AdapterFB(AdapterFB=var_36)
    assert isinstance(var_37, python_code_.libraryElement_AdapterFB)
    var_38 = var_37.getType()
    python_code_.libraryElement_SystemConfiguration(
        libraryElement_SystemConfiguration=var_35,
        libraryElement_SystemConfiguration148=var_38,
    )


@pytest.mark.xfail(strict=True)
def test_17():
    var_4 = python_code_.libraryElement_VarInitialization()
    python_code_.libraryElement_ResourceTypeFB()
    var_7 = lambda *args, **kwargs: []
    var_8 = python_code_.libraryElement_EventConnection(
        libraryElement_EventConnection=var_7
    )
    assert isinstance(var_8, python_code_.libraryElement_EventConnection)
    var_10 = python_code_.libraryElement_Value(
        value=[1260.47, -1580, "re.wZ\t8r(>Q~d#YV4"]
    )
    python_code_.libraryElement_IInterfaceElement(
        isInput=var_4, typeName=-2471, libraryElement_IInterfaceElement144=var_10
    )


def test_18():
    python_code_.libraryElement_TypedConfigureableObject()
    var_1 = python_code_.libraryElement_EventConnection()
    var_1.getSource()
    var_6 = python_code_.libraryElement_EventConnection()
    var_6.getDestination()


@pytest.mark.xfail(strict=True)
def test_19():
    var_4 = python_code_.libraryElement_VarInitialization()
    var_5 = python_code_.libraryElement_ResourceTypeFB()
    var_33 = python_code_.Algorithm
    python_code_.libraryElement_Parameter(
        comment=var_33, name=var_5, value=var_33, libraryElement_Parameter=var_33
    )
    var_7 = lambda *args, **kwargs: []
    var_8 = python_code_.libraryElement_EventConnection(
        libraryElement_EventConnection=var_7
    )
    assert isinstance(var_8, python_code_.libraryElement_EventConnection)
    var_10 = python_code_.libraryElement_Value(
        value=[1260.47, -1580, "re.wZ\t8r(>Q~d#YV4"]
    )
    python_code_.libraryElement_IInterfaceElement(
        isInput=var_4, typeName=-2471, libraryElement_IInterfaceElement144=var_10
    )


@pytest.mark.xfail(strict=True)
def test_20():
    var_0 = python_code_.libraryElement_ConfigurableObject()
    var_0.getParameter(libraryElement_parameterName=var_0)
    var_2 = python_code_.libraryElement_ECState()
    var_3 = var_2.isStartState()
    var_4 = python_code_.libraryElement_ECAction()
    var_5 = python_code_.libraryElement_AdapterType(libraryElement_AdapterType=-152.9)
    assert isinstance(var_5, python_code_.libraryElement_AdapterType)
    var_5.getPlugType()
    var_7 = "=0"
    var_8 = python_code_.libraryElement_ECTransition(
        comment=var_7,
        conditionExpression=var_5,
        libraryElement_ECTransition46=var_3,
        ECTransition=var_2,
    )
    assert isinstance(var_8, python_code_.libraryElement_ECTransition)
    var_9 = python_code_.libraryElement_Link()
    var_10 = "y4gMxnTO]SNjxEXmnq"
    var_11 = python_code_.libraryElement_DeviceType(
        profile=var_10,
        libraryElement_DeviceType=b"Go\x1a$Ui;\x7f\x00\xa1\x12\x14\x17\xd3",
        libraryElement_DeviceType23=var_3,
    )
    assert isinstance(var_11, python_code_.libraryElement_DeviceType)
    var_12 = python_code_.libraryElement_Resource(
        x=3934, y=var_10, deviceTypeResource=var_4, libraryElement_Resource=var_11
    )
    assert isinstance(var_12, python_code_.libraryElement_Resource)
    var_13 = lambda *args, **kwargs: False
    var_14 = python_code_.libraryElement_CompositeFBType()
    python_code_.libraryElement_FBNetwork(
        libraryElement_FBNetwork24=var_11,
        libraryElement_FBNetwork87=var_13,
        libraryElement_FBNetwork115=var_9,
        libraryElement_FBNetwork136=var_14,
    )


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = python_code_.libraryElement_I4DIACElement()
    assert isinstance(var_0, python_code_.libraryElement_I4DIACElement)
    var_1 = python_code_.ConfigurableObject
    var_0.createAnnotation(libraryElement_name=var_1)
    var_6 = "s"
    var_10 = "\\cFX>#OJ\\"
    var_11 = python_code_.libraryElement_Connection(
        dx1=var_6,
        dx2=var_6,
        dy="libraryElement_FBNetworkElement81C_libraryElement_SystemConfiguration__libraryElement_SystemConfiguration146",
        resTypeConnection=var_10,
        brokenConnection="p.00R+QK>IE O,",
        Connection="iPy\\fz7zSF%= .$A|j",
        Connection141=False,
    )
    assert isinstance(var_11, python_code_.libraryElement_Connection)
    var_15 = python_code_.libraryElement_FBNetwork(
        libraryElement_FBNetwork=var_0, libraryElement_FBNetwork87=None
    )
    var_16 = python_code_.libraryElement_FBNetworkElement(
        libraryElement_FBNetworkElement=var_11,
        libraryElement_FBNetworkElement109=var_15,
        libraryElement_FBNetworkElement81=-748.9,
    )
    assert isinstance(var_16, python_code_.libraryElement_FBNetworkElement)
    var_19 = python_code_.libraryElement_EventConnection()
    var_19.getDestination()
    python_code_.libraryElement_FBNetworkElement(
        libraryElement_FBNetworkElement109=complex(-3743.4502, -493.5)
    )
    python_code_.libraryElement_Application()
    var_30 = lambda *args, **kwargs: [False, -632]
    var_31 = python_code_.libraryElement_Device(profile=var_30)
    assert isinstance(var_31, python_code_.libraryElement_Device)
    var_32 = var_31.getAutomationSystem()
    var_33 = python_code_.libraryElement_Annotation(
        name=var_10, servity=var_1, libraryElement_Annotation=var_0
    )
    assert isinstance(var_33, python_code_.libraryElement_Annotation)
    var_34 = "libraryElement_ServiceTransaction"
    var_35 = python_code_.libraryElement_AutomationSystem(
        project=var_34,
        automationSystem=var_32,
        libraryElement_AutomationSystem123=(".5~p,{Zz_fEycI[\x0c",),
    )
    assert isinstance(var_35, python_code_.libraryElement_AutomationSystem)
    var_36 = python_code_.libraryElement_AdapterDeclaration()
    var_37 = python_code_.libraryElement_AdapterFB(AdapterFB=var_36)
    assert isinstance(var_37, python_code_.libraryElement_AdapterFB)
    var_38 = var_37.getType()
    python_code_.libraryElement_SystemConfiguration(
        libraryElement_SystemConfiguration=var_35,
        libraryElement_SystemConfiguration148=var_38,
    )


def test_22():
    var_0 = python_code_.libraryElement_I4DIACElement()
    assert isinstance(var_0, python_code_.libraryElement_I4DIACElement)
    var_6 = "s"
    var_10 = "\\cFX>#OJ\\"
    var_11 = python_code_.libraryElement_Connection(
        dx1=var_6,
        dx2=var_6,
        dy="libraryElement_FBNetworkElement81C_libraryElement_SystemConfiguration__libraryElement_SystemConfiguration146",
        resTypeConnection=var_10,
        brokenConnection="p.00R+QK>IE O,",
        Connection="iPy\\fz7zSF%= .$A|j",
        Connection141=False,
    )
    assert isinstance(var_11, python_code_.libraryElement_Connection)
    var_48 = python_code_.libraryElement_I4DIACElement()
    var_49 = var_48.createAnnotation(libraryElement_name=(False, 996.29, -1437.85))
    var_51 = "sg}J~^"
    var_52 = '2_o2aQZL#T!&\r9><"'
    var_53 = python_code_.libraryElement_ECC
    var_54 = python_code_.libraryElement_ECTransition(
        comment=var_51,
        conditionExpression=var_52,
        outTransitions=var_48,
        inTransitions=var_48,
        libraryElement_ECTransition46=var_49,
        ECTransition=var_53,
    )
    assert isinstance(var_54, python_code_.libraryElement_ECTransition)
    var_54.getConditionText()
    python_code_.libraryElement_DataConnection()
    var_62 = python_code_.libraryElement_ServiceSequence(TestResult=var_10)
    assert isinstance(var_62, python_code_.libraryElement_ServiceSequence)
