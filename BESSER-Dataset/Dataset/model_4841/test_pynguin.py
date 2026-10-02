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
    var_0 = ""
    var_1 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=b"\xa8A\xd7\xa2~\xa8o\t\xf9\xb7\xa7",
        capabilityDelivered=var_0,
    )
    assert isinstance(var_1, python_code_.contentfwk_WorkPackage)
    var_3 = "m"
    var_4 = python_code_.contentfwk_Event
    var_6 = "JG1G[.!]P!H-h"
    var_7 = "M%}29}"
    var_8 = python_code_.contentfwk_Element(
        name=var_7,
        description="~ff",
        sourceDescr=var_3,
        ownerDescr='xC&9Dl7_zU"#a}vzr',
        ID="Process206",
        category=var_3,
        Element=None,
        Element270=var_4,
        delegates={-1, var_6},
    )
    assert isinstance(var_8, python_code_.contentfwk_Element)
    python_code_.contentfwk_Element(
        name=var_3,
        description=var_4,
        sourceDescr={
            "q_)'^(?7r%tm": "LogicalDataComponent,NonStandard,_contentfwk_Role__isDecomposedByRoles,_contentfwk_LogicalTechnologyComponent__isImplementedOnLogicalTechnologyComponents",
            "O(b;G\x0b`MUw6q\rFBS\x0c": False,
        },
        ownerDescr={},
        ID=var_3,
        category=var_3,
        isDelegatedBy=var_1,
        Element270=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_1 = "N\r`jYyN"
    var_2 = python_code_.contentfwk_WorkPackage(
        workPackageCategory=var_1, capabilityDelivered=var_1
    )
    assert isinstance(var_2, python_code_.contentfwk_WorkPackage)
    var_3 = python_code_.contentfwk_DataComponent()
    var_7 = "qa"
    var_8 = sorted
    var_9 = python_code_.contentfwk_Role(
        estimatedFTEs=var_7,
        canBeAccessedByRoles=b"#\x0c*\xcc\xbb8\xdf\xcd\x97\xea\xb8\xd7",
        isDecomposedByRoles=var_2,
        Role117=var_7,
        Role162=var_8,
    )
    assert isinstance(var_9, python_code_.contentfwk_Role)
    var_10 = python_code_.contentfwk_LogicalDataComponent()
    var_11 = python_code_.contentfwk_ApplicationComponent()
    var_12 = "wS#h{ti%T\t4Xf"
    var_13 = python_code_.contentfwk_Element(
        name=var_8,
        description=var_7,
        sourceDescr=var_1,
        ownerDescr=var_10,
        ID=var_11,
        category=var_1,
    )
    assert isinstance(var_13, python_code_.contentfwk_Element)
    var_14 = python_code_.contentfwk_Element(
        name=var_12,
        description=var_1,
        sourceDescr=var_12,
        ownerDescr=var_1,
        ID=var_8,
        category={-1, "\x0bzR87{\x0c)^U"},
        Element=-56.5,
        Element270=var_13,
    )
    assert isinstance(var_14, python_code_.contentfwk_Element)
    var_17 = python_code_.contentfwk_Event()
    var_18 = python_code_.contentfwk_Product()
    var_21 = "=BEqGQ8m5}*xz\\^"
    var_22 = python_code_.contentfwk_DataEntity(
        dataEntityCategory=var_18,
        privacyClassification=var_21,
        retentionClassification=var_1,
        DataEntity=var_8,
        contentfwk_DataEntity135=b"\x19\xf6\x82 \xd1c\x10\xa1\xe6\xc1\xb5",
        contentfwk_DataEntity129={},
        DataEntity291=var_8,
    )
    assert isinstance(var_22, python_code_.contentfwk_DataEntity)
    var_23 = {var_22, var_22, var_22, var_22}
    var_24 = python_code_.contentfwk_Service()
    python_code_.contentfwk_Actor(
        FTEs=None,
        actorGoal=var_8,
        actorTasks=-1,
        isSuppliedByActors=var_17,
        isConsumedByActors=var_23,
        containsActors=var_3,
        Actor=(),
        isDecomposedByActors={"s]M2R7s{g#,,$Itg": False},
        decomposesActor=var_23,
        Actor109=var_9,
        supportsActors=var_13,
        involvesActors=var_23,
        Actor263=var_17,
        Actor272=var_11,
        Actor353=var_24,
    )


def test_2():
    var_0 = python_code_.contentfwk_BusinessService()
    var_1 = python_code_.contentfwk_Capability(
        businessValue=var_0, increments=(-6815, False)
    )
    assert isinstance(var_1, python_code_.contentfwk_Capability)


@pytest.mark.xfail(strict=True)
def test_3():
    var_6 = "WorkStream"
    var_7 = "6]~\\\nV*nbR'_\"J\x0c"
    var_8 = python_code_.contentfwk_LogicalTechnologyComponent(
        categoryTRM=var_7, isDependentOnLogicalTechnologyComponents=b"\xfa"
    )
    assert isinstance(var_8, python_code_.contentfwk_LogicalTechnologyComponent)
    python_code_.contentfwk_LogicalTechnologyComponent(
        categoryTRM=var_7,
        contentfwk_LogicalTechnologyComponent={},
        isSuppliedByLogicalTechnologyComponents=var_6,
        decomposesLogicalTechnologyComponent=var_6,
        isDecomposedByLogicalTechnologyComponents=var_8,
    )


def test_4():
    var_0 = python_code_.contentfwk_BusinessService()
    var_1 = python_code_.contentfwk_Capability(
        businessValue=var_0, increments=(-6815, False)
    )
    assert isinstance(var_1, python_code_.contentfwk_Capability)
    var_6 = python_code_.contentfwk_StrategicArchitecture()
    var_7 = python_code_.PrincipleCategory.DataPrinciple
    var_8 = "Role117"
    var_9 = python_code_.contentfwk_PlatformService(
        categoryTRM=var_6, standardClass=var_8, PlatformService=var_7
    )
    assert isinstance(var_9, python_code_.contentfwk_PlatformService)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.contentfwk_BusinessService()
    var_9 = python_code_.StrategicElement()
    var_13 = python_code_.contentfwk_Driver()
    var_14 = {var_13, var_13}
    var_15 = "%LE|_}wXc\tgLi9TP\x0cs9"
    var_16 = set()
    var_17 = python_code_.LifeCycleStatus
    var_18 = python_code_.contentfwk_Location()
    python_code_.contentfwk_Actor(
        FTEs=True,
        actorGoal=var_15,
        actorTasks=var_9,
        isSuppliedByActors=var_16,
        contentfwk_Actor=var_0,
        Actor={
            "Program:IntegrationPrinciple:contentfwk_WorkPackage:contentfwk_WorkPackage": -2282.2
        },
        Actor107=var_17,
        isAssumedByActors=set(),
        involvesActors=var_14,
        isGeneratedByActors=4230.5,
        containsActors98=var_18,
        Actor190=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_2 = lambda *args, **kwargs: [-280, "PhysicalApplicationComponent325", False]
    var_4 = "/O*+\x0cN $:9<CaTj\n?h"
    var_6 = python_code_.contentfwk_Role(
        estimatedFTEs=var_2,
        canBeAccessedByRoles=set(),
        Role117=complex(-214.23157, 2457.9),
    )
    assert isinstance(var_6, python_code_.contentfwk_Role)
    var_10 = python_code_.PrincipleCategory.DataPrinciple
    var_11 = python_code_.contentfwk_Function()
    var_12 = python_code_.contentfwk_Function()
    var_13 = {var_11, var_12, var_12, var_11}
    python_code_.contentfwk_OrganizationUnit(
        headcount=var_4,
        containsOrganizationUnits=var_2,
        OrganizationUnit81=var_10,
        contentfwk_OrganizationUnit=var_2,
        motivatesOrganizationUnits=var_13,
        OrganizationUnit86=[False, 1451.16],
        isOwnedAndGovernedByOrganizationUnits=var_2,
        involvesOrganizationUnits=var_13,
        OrganizationUnit230=var_2,
        OrganizationUnit369=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_2 = "E\tdZIlvowy,'R"
    var_5 = python_code_.contentfwk_PhysicalApplicationComponent
    var_6 = python_code_.contentfwk_Driver()
    var_7 = python_code_.contentfwk_Service()
    var_8 = {var_7}
    var_9 = python_code_.contentfwk_Product()
    python_code_.contentfwk_OrganizationUnit(
        headcount=var_2,
        decomposesOrganizationUnit=var_5,
        OrganizationUnit=var_6,
        OrganizationUnit86={True, "v|\r\x0c/!}5@MvPDjtc;"},
        isOwnedAndGovernedByOrganizationUnits=var_8,
        OrganizationUnit230=var_9,
    )


def test_8():
    python_code_.contentfwk_Driver()


def test_9():
    var_0 = ""
    var_1 = python_code_.contentfwk_TechnologyArchitecture
    var_2 = "orchestratesServices-_contentfwk_DataEntity__DataEntity291-_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent322-_contentfwk_Contract__Contract"
    var_3 = "R1p0Jyr(0Sd\x0bX5,8H.w"
    var_4 = python_code_.contentfwk_Element(
        name="_contentfwk_Process__Process91",
        description=var_0,
        sourceDescr=var_1,
        ownerDescr=var_1,
        ID=var_2,
        category=var_3,
    )
    assert isinstance(var_4, python_code_.contentfwk_Element)
    var_7 = "_contentfwk_PhysicalTechnologyComponent__PhysicalTechnologyComponent322,contentfwk_BusinessArchitecture11,LogicalApplicationComponent,isHostedInLocation"
    var_8 = "_contentfwk_PhysicalApplicationComponent__PhysicalApplicationComponent-_contentfwk_Process__Process200-Element"
    var_9 = python_code_.contentfwk_Principle(
        principleCategory=var_4,
        priority=var_1,
        statementOfPrinciple=var_7,
        rationale=-539.01,
        implication=var_0,
        metric=var_8,
    )
    assert isinstance(var_9, python_code_.contentfwk_Principle)


@pytest.mark.xfail(strict=True)
def test_10():
    var_4 = python_code_.StandardsClass.Provisional
    var_15 = python_code_.contentfwk_Principle
    var_17 = "\x0b%wDS aDj0"
    var_18 = python_code_.contentfwk_Service
    var_19 = "Process203"
    var_20 = "+k \x0b"
    var_21 = "pm}JM>\x0c=7S}Gk"
    var_22 = ".&G"
    var_23 = "Vi"
    var_24 = "\x0c?#<f{~kmfI\\\\X"
    var_25 = ""
    var_26 = "YCj\x0b<{4qh^G=f"
    var_27 = python_code_.contentfwk_ServiceQuality()
    python_code_.contentfwk_Contract(
        internationalizationCharacteristics=b"BQ\xe9\xdb\xf9C\xf3\xd3\xd9Wk#\xd7",
        interoperabilityCharacteristics=-91,
        scalabilityCharacteristics=var_17,
        portabilityCharacteristics=var_17,
        extensibilityCharacteristics=var_18,
        capacityCharacteristics=var_15,
        throughput=[],
        throughputPeriod=var_15,
        growth=var_17,
        growthPeriod=None,
        peakProfileShortTerm=var_19,
        peakProfileLongTerm=var_19,
        responseCharacteristics=var_20,
        reliabilityCharacteristics=-1635,
        qualityOfInformationRequired=var_20,
        contractControlRequirements=var_18,
        resultControlRequirements=var_21,
        recoverabilityCharacteristics=var_18,
        locatabilityCharacteristics=var_22,
        behaviorCharacteristics=var_23,
        serviceNameCaller=var_24,
        serviceNameCalled=1,
        serviceQualityCharacteristics=var_4,
        availabilityQualityCharacteristics=var_21,
        servicesTimes=var_18,
        manageabilityCharacteristics=var_25,
        serviceabilityCharacteristics=complex(1326.631, 1620.00192),
        performanceCharacteristics=var_23,
        securityCharacteristics=var_26,
        privacyCharacteristics=3487.87,
        integrityCharacteristics=False,
        credibilityCharacteristics=var_20,
        localizationCharacteristics=set(),
        Contract=var_27,
        isGovernedAndMeasuredByContracts=var_18,
        Contract361=set(),
    )
