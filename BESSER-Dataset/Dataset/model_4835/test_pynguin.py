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
    ApplicationComponent,
    Architecture,
    DataComponent,
    DataEntityCategory,
    Element,
    Enum,
    LifeCycleStatus,
    PrincipleCategory,
    Service,
    Standard,
    StandardsClass,
    StrategicElement,
    TechnologyComponent,
    WorkPackageCategory,
    abstractmethod,
    contentfwk_Actor,
    contentfwk_ApplicationArchitecture,
    contentfwk_ApplicationComponent,
    contentfwk_Architecture,
    contentfwk_Assumption,
    contentfwk_BusinessArchitecture,
    contentfwk_BusinessService,
    contentfwk_Capability,
    contentfwk_Constraint,
    contentfwk_Contract,
    contentfwk_Control,
    contentfwk_DataArchitecture,
    contentfwk_DataComponent,
    contentfwk_DataEntity,
    contentfwk_Driver,
    contentfwk_Element,
    contentfwk_EnterpriseArchitecture,
    contentfwk_Event,
    contentfwk_Function,
    contentfwk_Gap,
    contentfwk_Goal,
    contentfwk_InformationSystemService,
    contentfwk_Location,
    contentfwk_LogicalApplicationComponent,
    contentfwk_LogicalDataComponent,
    contentfwk_LogicalTechnologyComponent,
    contentfwk_Measure,
    contentfwk_Objective,
    contentfwk_OrganizationUnit,
    contentfwk_PhysicalApplicationComponent,
    contentfwk_PhysicalDataComponent,
    contentfwk_PhysicalTechnologyComponent,
    contentfwk_PlatformService,
    contentfwk_Principle,
    contentfwk_Process,
    contentfwk_Product,
    contentfwk_Requirement,
    contentfwk_Role,
    contentfwk_Service,
    contentfwk_ServiceQuality,
    contentfwk_Standard,
    contentfwk_StrategicArchitecture,
    contentfwk_StrategicElement,
    contentfwk_TechnologyArchitecture,
    contentfwk_TechnologyComponent,
    contentfwk_WorkPackage,
    date,
    datetime,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_2 = ".Hg=I\t"
    var_3 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=var_2, capabilityDelivered="\x0c4JF6sJ\tp/e"
    )
    assert isinstance(var_3, python_code_.contentfwk_WorkPackage)
    var_5 = tuple
    var_6 = python_code_.contentfwk_BusinessArchitecture()
    var_7 = python_code_.contentfwk_Location()
    python_code_.contentfwk_OrganizationUnit(
        headcount=var_2,
        contentfwk_OrganizationUnit=var_6,
        OrganizationUnit=var_5,
        isProducedByOrganizationUnits=var_5,
        containsOrganizationUnits=var_7,
        isOwnedAndGovernedByOrganizationUnits=False,
    )


def test_1():
    var_43 = python_code_.contentfwk_LogicalTechnologyComponent
    var_44 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=var_43,
        capabilityDelivered=None,
        WorkPackage="governsAndMeasuresBusinessServices-_contentfwk_Actor__isAssumedByActors",
    )
    assert isinstance(var_44, python_code_.contentfwk_WorkPackage)
    var_47 = python_code_.contentfwk_Architecture(ID=False)
    assert isinstance(var_47, python_code_.contentfwk_Architecture)
    var_47.forceID(contentfwk_newID=var_43)
    var_51 = ":a#l-!i*'p"
    var_52 = python_code_.contentfwk_EnterpriseArchitecture(ID=var_51)
    var_52.forceID(contentfwk_newID=523)


@pytest.mark.xfail(strict=True)
def test_2():
    var_2 = python_code_.contentfwk_LogicalDataComponent()
    var_3 = python_code_.Service()
    var_4 = python_code_.contentfwk_BusinessArchitecture()
    var_5 = (
        lambda *args, **kwargs: "Standard._contentfwk_Element__Element.isHostedInLocation"
    )
    var_6 = "Product197-realizesPhysicalApplicationComponents-contentfwk_DataEntity132-contentfwk_PhysicalApplicationComponent"
    var_7 = "decomposesProcess,_contentfwk_DataEntity__DataEntity357,deliversCapabilities,_contentfwk_DataEntity__consumesDataEntities"
    var_8 = python_code_.contentfwk_Element(
        ID=var_6,
        category=var_7,
        name=1025.51,
        description=[],
        sourceDescr=var_3,
        ownerDescr=var_7,
        isDelegatedBy=var_6,
    )
    assert isinstance(var_8, python_code_.contentfwk_Element)
    var_9 = python_code_.contentfwk_Element(
        ID=[True, 3229.65, 3628],
        category=var_2,
        name=3814,
        description=367.4,
        sourceDescr=False,
        ownerDescr=var_5,
        Element=var_8,
        isDelegatedBy=[],
        delegates={},
    )
    assert isinstance(var_9, python_code_.contentfwk_Element)
    var_10 = var_8.forceID(contentfwk_newID=var_5)
    python_code_.contentfwk_OrganizationUnit(
        headcount=False,
        contentfwk_OrganizationUnit=var_4,
        isOwnedAndGovernedByOrganizationUnits=var_10,
        isOwnedByOrganizationUnit=var_4,
        OrganizationUnit275=var_8,
    )


def test_3():
    var_0 = python_code_.contentfwk_TechnologyComponent
    var_1 = "contentfwk_Driver"
    var_2 = "isRequiredByLogicalTechnologyComponents-_contentfwk_OrganizationUnit__isProducedByOrganizationUnits"
    var_3 = "Element270-_contentfwk_Element__Element270"
    var_4 = "8"
    var_5 = "\rYl*0Enyj\x0czU\r=>7"
    var_6 = python_code_.contentfwk_EnterpriseArchitecture(ID=var_3)
    var_7 = python_code_.contentfwk_Architecture(
        ID=var_5, contentfwk_Architecture=var_6
    )
    assert isinstance(var_7, python_code_.contentfwk_Architecture)
    var_8 = var_7.forceID(contentfwk_newID=var_0)
    var_9 = python_code_.contentfwk_Element(
        ID=var_2,
        category=var_3,
        name=var_2,
        description=var_4,
        sourceDescr=var_1,
        ownerDescr=var_3,
        isDelegatedBy=var_8,
    )
    assert isinstance(var_9, python_code_.contentfwk_Element)
    var_10 = var_9.forceID(contentfwk_newID=var_7)
    var_11 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=var_0, capabilityDelivered=var_1, isDeliveredBy=var_10
    )
    assert isinstance(var_11, python_code_.contentfwk_WorkPackage)


def test_4():
    var_2 = python_code_.contentfwk_DataArchitecture()
    var_8 = python_code_.contentfwk_Service()
    var_9 = "l'&F#z-=>!"
    var_10 = bool
    var_11 = "MEI0X-F,n[\t{>"
    var_12 = "28{T"
    var_13 = python_code_.contentfwk_Element(
        ID=var_9,
        category=var_11,
        name=var_12,
        description=var_12,
        sourceDescr=-3800,
        ownerDescr=[],
    )
    assert isinstance(var_13, python_code_.contentfwk_Element)
    var_14 = var_13.forceID(contentfwk_newID={})
    var_15 = python_code_.contentfwk_Element(
        ID=var_8,
        category=var_2,
        name=None,
        description=var_9,
        sourceDescr=var_9,
        ownerDescr=var_10,
        Element270=-797.24,
        delegates=var_14,
    )
    assert isinstance(var_15, python_code_.contentfwk_Element)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "LogicalTechnologyComponent348"
    var_1 = python_code_.contentfwk_Goal
    var_2 = "_contentfwk_Process__Process373_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent339"
    var_3 = "o"
    var_4 = python_code_.contentfwk_Element(
        ID=None,
        category=var_0,
        name=var_1,
        description=var_2,
        sourceDescr=var_2,
        ownerDescr=var_3,
        Element270=var_1,
    )
    assert isinstance(var_4, python_code_.contentfwk_Element)
    var_5 = var_4.forceID(contentfwk_newID=var_1)
    var_6 = python_code_.contentfwk_DataEntity(
        dataEntityCategory=var_0,
        privacyClassification=var_0,
        retentionClassification=None,
        contentfwk_DataEntity135="XPl~A8",
        providesDataEntities=var_5,
    )
    assert isinstance(var_6, python_code_.contentfwk_DataEntity)
    var_10 = "TechnologyPrinciple"
    var_11 = "1RBeue"
    var_12 = "<uta%Ql"
    var_13 = python_code_.contentfwk_EnterpriseArchitecture(
        ID=var_0, contentfwk_EnterpriseArchitecture=var_10
    )
    var_14 = python_code_.contentfwk_Architecture(
        ID=-582.15, contentfwk_Architecture=var_13
    )
    assert isinstance(var_14, python_code_.contentfwk_Architecture)
    var_15 = var_14.forceID(contentfwk_newID=var_5)
    var_16 = python_code_.contentfwk_LogicalTechnologyComponent(categoryTRM=var_3)
    assert isinstance(var_16, python_code_.contentfwk_LogicalTechnologyComponent)
    var_17 = var_4.forceID(contentfwk_newID=var_1)
    var_18 = var_14.forceID(contentfwk_newID=var_17)
    var_19 = python_code_.contentfwk_LogicalTechnologyComponent(
        categoryTRM=(True,),
        contentfwk_LogicalTechnologyComponent=var_3,
        isRequiredByLogicalTechnologyComponents=var_15,
        LogicalTechnologyComponent345=var_16,
        isImplementedOnLogicalTechnologyComponents=var_17,
        isSuppliedByLogicalTechnologyComponents=var_18,
    )
    assert isinstance(var_19, python_code_.contentfwk_LogicalTechnologyComponent)
    var_20 = python_code_.contentfwk_LogicalTechnologyComponent(
        categoryTRM=var_12,
        contentfwk_LogicalTechnologyComponent=var_1,
        LogicalTechnologyComponent348=var_16,
    )
    assert isinstance(var_20, python_code_.contentfwk_LogicalTechnologyComponent)
    python_code_.contentfwk_PhysicalTechnologyComponent(
        productName=var_10,
        moduleName={},
        vendor=var_11,
        version=var_1,
        categoryTRM=var_2,
        containsPhysicalTechnologyComponents=163.23,
        isDecomposedByPhysicalTechnologyComponents=2390.94,
        PhysicalTechnologyComponent222=var_0,
        contentfwk_PhysicalTechnologyComponent342=var_16,
        PhysicalTechnologyComponent281=615,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = "c)N{+}1\nQV"
    var_1 = python_code_.contentfwk_Principle(
        priority=b"\n\xec\xe0f\xc1\xf1\xd4\xcdDP",
        statementOfPrinciple=var_0,
        rationale=var_0,
        implication=var_0,
        metric=var_0,
        principleCategory=complex(1020.7707, -85.8),
    )
    assert isinstance(var_1, python_code_.contentfwk_Principle)
    var_3 = python_code_.WorkPackageCategory.Program
    var_4 = python_code_.contentfwk_Architecture(ID=var_0)
    assert isinstance(var_4, python_code_.contentfwk_Architecture)
    var_8 = bool
    var_9 = "_contentfwk_DataEntity__contentfwk_DataEntity134"
    var_10 = "V;p8<xGzQ}lZ;?*]SM"
    var_11 = python_code_.contentfwk_Principle(
        priority=var_8,
        statementOfPrinciple=[True],
        rationale=var_9,
        implication=var_9,
        metric=var_10,
        principleCategory=var_3,
    )
    var_12 = "5[.7Jn{S^wo&R'0>$-7"
    var_13 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=var_12,
        capabilityDelivered=var_12,
        WorkPackage="lSa;Wu]*e)IO$\x0b2r\x0b7",
    )
    assert isinstance(var_13, python_code_.contentfwk_WorkPackage)
    var_15 = python_code_.contentfwk_PlatformService(
        standardClass=var_11, categoryTRM=var_9
    )
    assert isinstance(var_15, python_code_.contentfwk_PlatformService)
    var_17 = "_contentfwk_Process__Process233"
    python_code_.contentfwk_EnterpriseArchitecture(
        ID=var_17, contentfwk_EnterpriseArchitecture=var_1
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_2 = python_code_.contentfwk_LogicalTechnologyComponent
    var_3 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=var_2,
        capabilityDelivered=None,
        WorkPackage="governsAndMeasuresBusinessServices-_contentfwk_Actor__isAssumedByActors",
    )
    assert isinstance(var_3, python_code_.contentfwk_WorkPackage)
    var_4 = "EIv5!F2,1Lg"
    var_6 = python_code_.contentfwk_Architecture(ID=False)
    assert isinstance(var_6, python_code_.contentfwk_Architecture)
    var_6.forceID(contentfwk_newID=var_2)
    var_8 = "LogicalTechnologyComponent339,InternallyStoredEntity,_contentfwk_Actor__isPerformedByActors"
    var_9 = "_contentfwk_OrganizationUnit__decomposesOrganizationUnit-Product197-contentfwk_Process"
    var_10 = ":a#l-!i*'p"
    var_11 = python_code_.contentfwk_EnterpriseArchitecture(ID=var_10)
    var_12 = var_11.forceID(contentfwk_newID=var_2)
    var_13 = var_11.forceID(contentfwk_newID=var_12)
    python_code_.contentfwk_DataEntity(
        dataEntityCategory=var_4,
        privacyClassification=var_8,
        retentionClassification=var_9,
        DataEntity=var_6,
        operatesOnDataEntities=2285.05,
        contentfwk_DataEntity135=var_12,
        encapsulatesDataEntities=3590,
        contentfwk_DataEntity132=var_13,
    )


def test_8():
    var_0 = "LogicalTechnologyComponent348"
    var_1 = python_code_.contentfwk_Goal
    var_2 = "_contentfwk_Process__Process373_contentfwk_LogicalTechnologyComponent__LogicalTechnologyComponent339"
    var_3 = "o"
    var_4 = python_code_.contentfwk_Element(
        ID=None,
        category=var_0,
        name=var_1,
        description=var_2,
        sourceDescr=var_2,
        ownerDescr=var_3,
        Element270=var_1,
    )
    assert isinstance(var_4, python_code_.contentfwk_Element)
    var_5 = var_4.forceID(contentfwk_newID=var_1)
    var_6 = python_code_.contentfwk_DataEntity(
        dataEntityCategory=var_0,
        privacyClassification=var_0,
        retentionClassification=None,
        contentfwk_DataEntity135="XPl~A8",
        providesDataEntities=var_5,
    )
    assert isinstance(var_6, python_code_.contentfwk_DataEntity)
    var_41 = "l'&F#z-=>!"
    var_43 = "MEI0X-F,n[\t{>"
    var_44 = "28{T"
    python_code_.contentfwk_Element(
        ID=var_41,
        category=var_43,
        name=var_44,
        description=var_44,
        sourceDescr=-3800,
        ownerDescr=[],
    )


def test_9():
    var_35 = python_code_.contentfwk_ServiceQuality()
    var_36 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=(), capabilityDelivered=var_35
    )
    assert isinstance(var_36, python_code_.contentfwk_WorkPackage)
    var_38 = python_code_.contentfwk_Service()
    var_40 = python_code_.contentfwk_PhysicalApplicationComponent
    var_41 = "v\tao-ac0?L&"
    var_44 = "isRequiredByPhysicalTechnologyComponent,_contentfwk_Role__Role162,OrganizationUnit78"
    var_45 = python_code_.contentfwk_Architecture(
        ID=-1481, contentfwk_Architecture=(-1463, "]PCx|)t3Ho]V\x0b", 1)
    )
    assert isinstance(var_45, python_code_.contentfwk_Architecture)
    var_45.forceID(contentfwk_newID=var_41)
    var_49 = python_code_.contentfwk_Event()
    var_51 = python_code_.Element
    var_52 = python_code_.contentfwk_OrganizationUnit(
        headcount=var_41,
        OrganizationUnit81=var_51,
        OrganizationUnit275=var_40,
        OrganizationUnit369=var_38,
    )
    assert isinstance(var_52, python_code_.contentfwk_OrganizationUnit)
    var_58 = python_code_.contentfwk_BusinessArchitecture()
    var_59 = python_code_.contentfwk_Actor(
        actorGoal=var_44,
        actorTasks=var_41,
        FTEs={5197.21, ""},
        contentfwk_Actor=var_58,
        Actor260=var_49,
        Actor263=var_49,
        Actor272=set(),
    )
    assert isinstance(var_59, python_code_.contentfwk_Actor)


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = python_code_.contentfwk_TechnologyArchitecture()
    var_1 = python_code_.contentfwk_Gap()
    var_2 = python_code_.contentfwk_ServiceQuality()
    var_3 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=(), capabilityDelivered=var_2
    )
    assert isinstance(var_3, python_code_.contentfwk_WorkPackage)
    var_5 = python_code_.contentfwk_Service()
    var_7 = python_code_.contentfwk_PhysicalApplicationComponent
    var_8 = "v\tao-ac0?L&"
    var_9 = "Z%xu*sPK]x={\\X+j)z"
    var_10 = "~C-\x0bW\r@1Md4c(6hJR9I"
    var_11 = "isRequiredByPhysicalTechnologyComponent,_contentfwk_Role__Role162,OrganizationUnit78"
    var_12 = python_code_.contentfwk_Element(
        ID=var_1,
        category={True, 25.81},
        name=var_10,
        description=None,
        sourceDescr=1878.75,
        ownerDescr=False,
    )
    assert isinstance(var_12, python_code_.contentfwk_Element)
    var_13 = python_code_.contentfwk_Architecture(
        ID=-1481, contentfwk_Architecture=(-1463, "]PCx|)t3Ho]V\x0b", 1)
    )
    assert isinstance(var_13, python_code_.contentfwk_Architecture)
    var_14 = var_13.forceID(contentfwk_newID=var_8)
    var_15 = python_code_.contentfwk_Element(
        ID=var_0,
        category=var_7,
        name=var_8,
        description=var_11,
        sourceDescr=var_10,
        ownerDescr=var_9,
        Element=var_12,
        isDelegatedBy=var_14,
    )
    assert isinstance(var_15, python_code_.contentfwk_Element)
    var_18 = "cW\r@Be+w3,)}4_BpY"
    var_19 = var_12.forceID(contentfwk_newID=var_7)
    var_20 = python_code_.contentfwk_Function()
    var_21 = python_code_.contentfwk_Event()
    python_code_.contentfwk_Actor(
        actorGoal=None,
        actorTasks=var_8,
        FTEs=var_18,
        isPerformedByActors=var_19,
        Actor107=var_7,
        isProvidedToActors=var_7,
        Actor164=var_7,
        Actor152=var_20,
        Actor260=var_21,
        Actor353=var_5,
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_2 = "_contentfwk_Process__Process375_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent333_contentfwk_DataEntity__DataEntity141_contentfwk_Process__isRealizedByProcesses"
    var_3 = 'kQlGYG!"T!f-Le'
    var_4 = 'F,Mh|,p=}%y8"|_z34'
    var_5 = "x 8QB?KKv"
    var_6 = python_code_.contentfwk_Standard
    var_7 = python_code_.contentfwk_Element(
        ID=var_2,
        category={
            "\x0c *[5,<`enER>~Z6nu": True,
            "Service187": "operatesInLocation274:decomposesOrganizationUnit:_contentfwk_PhysicalApplicationComponent__encapsulatesPhysicalApplicationComponents",
        },
        name=-300.92,
        description=var_3,
        sourceDescr=var_4,
        ownerDescr=var_5,
        isDelegatedBy=var_3,
        Element270=var_6,
    )
    assert isinstance(var_7, python_code_.contentfwk_Element)
    var_8 = python_code_.StrategicElement()
    var_9 = "\x0b_1s"
    var_11 = python_code_.contentfwk_Architecture(ID=var_5)
    assert isinstance(var_11, python_code_.contentfwk_Architecture)
    var_13 = True
    var_14 = "_contentfwk_PhysicalTechnologyComponent__isRealizedByPhysicalTechnologyComponents214._contentfwk_Capability__contentfwk_Capability"
    var_15 = python_code_.contentfwk_BusinessArchitecture()
    var_16 = var_11.forceID(contentfwk_newID=var_6)
    var_17 = var_7.forceID(
        contentfwk_newID={
            "qB2t@": False,
            "contentfwk_DataEntity": "Product197Process200contentfwk_BusinessArchitecture_contentfwk_DataEntity__contentfwk_DataEntity135",
        }
    )
    python_code_.contentfwk_Process(
        processCritiality=var_9,
        isAutomated=var_13,
        processVolumetrics=var_14,
        contentfwk_Process=var_15,
        ensuresCorrectOperationOfProcesses=var_8,
        isGeneratedByProcesses=var_16,
        isDecomposedByProcesses={"NqsYb_[wB=k\x0bN\r": 2517},
        Process206=var_11,
        precedesProcesses=var_17,
        Process209=var_4,
        decomposesProcess=False,
        Process233=[-4837, -4291],
        supportsProcesses=var_17,
    )


def test_12():
    var_0 = python_code_.contentfwk_TechnologyComponent
    var_3 = "Element270-_contentfwk_Element__Element270"
    var_5 = "\rYl*0Enyj\x0czU\r=>7"
    var_6 = python_code_.contentfwk_EnterpriseArchitecture(ID=var_3)
    var_7 = python_code_.contentfwk_Architecture(
        ID=var_5, contentfwk_Architecture=var_6
    )
    assert isinstance(var_7, python_code_.contentfwk_Architecture)
    var_7.forceID(contentfwk_newID=var_0)


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = python_code_.contentfwk_TechnologyArchitecture()
    var_1 = python_code_.contentfwk_Gap()
    var_2 = python_code_.contentfwk_ServiceQuality()
    var_3 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=(), capabilityDelivered=var_2
    )
    assert isinstance(var_3, python_code_.contentfwk_WorkPackage)
    var_5 = python_code_.contentfwk_Service()
    var_7 = python_code_.contentfwk_PhysicalApplicationComponent
    var_8 = "v\tao-ac0?L&"
    var_9 = "Z%xu*sPK]x={\\X+j)z"
    var_10 = "~C-\x0bW\r@1Md4c(6hJR9I"
    var_11 = "isRequiredByPhysicalTechnologyComponent,_contentfwk_Role__Role162,OrganizationUnit78"
    var_12 = python_code_.contentfwk_Element(
        ID=var_1,
        category={True, 25.81},
        name=var_10,
        description=None,
        sourceDescr=1878.75,
        ownerDescr=False,
    )
    assert isinstance(var_12, python_code_.contentfwk_Element)
    var_13 = python_code_.contentfwk_Architecture(
        ID=-1481, contentfwk_Architecture=(-1463, "]PCx|)t3Ho]V\x0b", 1)
    )
    assert isinstance(var_13, python_code_.contentfwk_Architecture)
    var_14 = var_13.forceID(contentfwk_newID=var_8)
    var_15 = python_code_.contentfwk_Element(
        ID=var_0,
        category=var_7,
        name=var_8,
        description=var_11,
        sourceDescr=var_10,
        ownerDescr=var_9,
        Element=var_12,
        isDelegatedBy=var_14,
    )
    assert isinstance(var_15, python_code_.contentfwk_Element)
    var_12.forceID(contentfwk_newID=var_7)
    var_24 = python_code_.Architecture
    var_25 = var_13.forceID(contentfwk_newID=var_12)
    var_26 = python_code_.contentfwk_Role(
        estimatedFTEs=var_24,
        canBeAccessedByRoles=var_25,
        decomposesRole=b"D\xbe\x02Z\x11E?wMz",
    )
    assert isinstance(var_26, python_code_.contentfwk_Role)
    var_27 = python_code_.Element
    var_28 = python_code_.contentfwk_OrganizationUnit(
        headcount=var_8,
        OrganizationUnit81=var_27,
        OrganizationUnit275=var_7,
        OrganizationUnit369=var_5,
    )
    assert isinstance(var_28, python_code_.contentfwk_OrganizationUnit)
    python_code_.contentfwk_Role(
        estimatedFTEs=var_8, Role=var_8, Role114=var_26, isDecomposedByRoles=False
    )
