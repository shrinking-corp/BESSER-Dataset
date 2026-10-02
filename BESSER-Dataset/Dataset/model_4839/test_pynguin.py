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
    contentfwk_Container,
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
    contentfwk_Label,
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
    var_1 = "_contentfwk_Process__supportsProcesses,Standard,_contentfwk_DataEntity__DataEntity317,_contentfwk_PhysicalTechnologyComponent__contentfwk_PhysicalTechnologyComponent"
    var_2 = True
    var_5 = python_code_.contentfwk_ApplicationComponent
    var_6 = 'XZ]B"l6ct,'
    var_7 = python_code_.contentfwk_Service()
    var_8 = {var_7}
    var_9 = python_code_.contentfwk_Control
    var_10 = "k`-{9gjVBl7H+Hz%"
    var_11 = python_code_.contentfwk_DataEntity(
        retentionClassification=var_1,
        dataEntityCategory=var_6,
        privacyClassification=var_9,
        contentfwk_DataEntity=set(),
        providesEntities=var_8,
        DataEntity=var_10,
        DataEntity261=var_2,
    )
    assert isinstance(var_11, python_code_.contentfwk_DataEntity)
    python_code_.contentfwk_DataEntity(
        retentionClassification=var_7,
        dataEntityCategory=var_9,
        privacyClassification=var_10,
        suppliesEntities="Location284",
        DataEntity=(),
        operatesOnDataEntities=var_5,
        contentfwk_DataEntity113=var_11,
        contentfwk_DataEntity111=var_1,
        contentfwk_DataEntity114=("}-0", 176, "Qk?I+%"),
        DataEntity319=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_3 = python_code_.contentfwk_Service()
    var_4 = python_code_.contentfwk_Measure()
    var_21 = "\r3"
    var_25 = "}\x0c?ja(S\t+MPCDat\rbaX"
    var_27 = python_code_.contentfwk_DataArchitecture()
    var_28 = python_code_.contentfwk_ServiceQuality
    var_29 = python_code_.contentfwk_BusinessArchitecture()
    var_30 = "jE\nZh"
    var_31 = ",75F_\rBlCom\x0c~\t\x0cmO"
    var_32 = "_contentfwk_Label__Label _contentfwk_Actor__involvesActors"
    var_33 = python_code_.contentfwk_Function()
    var_34 = python_code_.contentfwk_Function()
    var_35 = {var_33, var_34, var_33}
    var_36 = python_code_.contentfwk_Actor(
        FTEs=var_30,
        actorGoal=var_32,
        actorTasks=var_31,
        Actor101=var_28,
        Actor103=None,
        isSuppliedByActors=var_21,
        supportsActors=var_35,
        isResolvedByActors=var_35,
        contentfwk_Actor90=var_25,
        containsActors86={True},
        contentfwk_Actor313=var_21,
    )
    assert isinstance(var_36, python_code_.contentfwk_Actor)
    var_37 = python_code_.contentfwk_DataEntity(
        retentionClassification=var_30,
        dataEntityCategory=var_31,
        privacyClassification=var_28,
        DataEntity=var_36,
        DataEntity72=var_27,
        DataEntity317=var_3,
        DataEntity319=var_3,
    )
    assert isinstance(var_37, python_code_.contentfwk_DataEntity)
    var_38 = {var_37, var_37, var_37, var_37}
    var_39 = python_code_.contentfwk_Actor(
        FTEs=True,
        actorGoal=b"\x9c\xea",
        actorTasks=b"\xcaC\xaa\xb8F",
        contentfwk_Actor=var_29,
        Actor=var_28,
        isConsumedByActors=var_38,
        supportsActors=(),
        isResolvedByActors=var_35,
        contentfwk_Actor92=var_36,
        containsActors86={
            "1BP0L:K5=Sy\\q>e\x0cQ%w",
            "_contentfwk_PhysicalApplicationComponent__contentfwk_PhysicalApplicationComponent",
        },
        Actor128=var_34,
    )
    assert isinstance(var_39, python_code_.contentfwk_Actor)
    var_40 = {var_36, var_39, var_39, var_39, var_39}
    python_code_.contentfwk_OrganizationUnit(
        headcount=var_28,
        isOwnedAndGovernedByOrganizationUnits=var_4,
        belongsTo=var_40,
        OrganizationUnit195=None,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = python_code_.contentfwk_Constraint()
    var_2 = "4Gm1:r8\t1TS"
    var_3 = python_code_.contentfwk_Principle(
        principleCategory=var_2,
        priority="",
        statementOfPrinciple=var_1,
        rationale={
            "CdP": "_contentfwk_Actor__isResolvedByActors,Service298",
            "\\{_O9(M4\x0bm": "1AM~\n\n.UnuT-,nK#w5q",
            "DataEntity": 2228.0,
        },
        implication=var_2,
        metric=var_2,
    )
    assert isinstance(var_3, python_code_.contentfwk_Principle)
    var_4 = python_code_.contentfwk_Assumption()
    var_6 = python_code_.contentfwk_PlatformService(
        categoryTRM=var_2, suppliesPlatformServices=(-310.76, 2380, "\r73l%d=5ni(U7")
    )
    assert isinstance(var_6, python_code_.contentfwk_PlatformService)
    var_7 = python_code_.contentfwk_Service()
    var_8 = {var_7, var_7}
    python_code_.contentfwk_DataEntity(
        retentionClassification=var_2,
        dataEntityCategory=var_2,
        privacyClassification=var_2,
        consumesEntities=var_8,
        encapsulatesDataEntities=var_4,
        operatesOnDataEntities=3227,
        contentfwk_DataEntity111=b'\xa7B\x8c.c\x81|\x80\xb2\x84\x1c\xd4\xb6t"\xacCZ',
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_1 = python_code_.contentfwk_Location()
    python_code_.contentfwk_Label(
        name=var_1,
        id=var_1,
        description={'"Zp5s/<\x0b6LEI~T%TY': -715.98},
        category=complex(-37.75, -1745.0),
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_9 = "LogicalDataComponent"
    var_10 = "SIZV4"
    var_11 = python_code_.contentfwk_Label(
        name=var_10,
        id=var_9,
        description=None,
        labels={
            "_contentfwk_Label__Label:DataEntity72": -6891,
            "_contentfwk_Process__Process134 Product _contentfwk_Actor__Actor103 contentfwk_Element": "_contentfwk_DataEntity__DataEntity319,Retired",
            "V>@pQX^3\x0b6#BP@}j8c": 129.13,
        },
    )
    assert isinstance(var_11, python_code_.contentfwk_Label)
    var_12 = python_code_.contentfwk_PlatformService
    python_code_.contentfwk_Label(
        name=var_12,
        id=b"\t",
        description=var_10,
        category=-2281,
        labels=[1903.71, -1515.4, False],
        Label=-3421.73,
        contentfwk_Label241=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_1 = python_code_.contentfwk_Architecture()
    var_2 = python_code_.contentfwk_InformationSystemService()
    var_4 = python_code_.contentfwk_StrategicArchitecture()
    var_5 = python_code_.contentfwk_ServiceQuality()
    var_6 = "w6,'D\tZ-"
    var_7 = "GDorf"
    var_8 = set()
    var_9 = python_code_.contentfwk_PhysicalTechnologyComponent(
        productName=var_6,
        moduleName=complex(130.928031, -3088.184),
        vendor=var_7,
        version=var_5,
        categoryTRM=var_6,
        contentfwk_PhysicalTechnologyComponent=var_4,
        contentfwk_PhysicalTechnologyComponent183={},
        contentfwk_PhysicalTechnologyComponent188=var_1,
        contentfwk_PhysicalTechnologyComponent191=var_8,
    )
    assert isinstance(var_9, python_code_.contentfwk_PhysicalTechnologyComponent)
    var_10 = python_code_.contentfwk_TechnologyArchitecture()
    var_11 = python_code_.contentfwk_LogicalTechnologyComponent(
        categoryTRM=b'hQ\xd4O\xa1\xcdjx"\x8f',
        contentfwk_LogicalTechnologyComponent=var_10,
        LogicalTechnologyComponent325=var_6,
    )
    assert isinstance(var_11, python_code_.contentfwk_LogicalTechnologyComponent)
    var_12 = python_code_.PrincipleCategory.TechnologyPrinciple
    var_14 = python_code_.contentfwk_Label
    python_code_.contentfwk_Actor(
        FTEs=var_10,
        actorGoal=var_14,
        actorTasks=var_2,
        Actor103=var_12,
        isSuppliedByActors=-331,
        isConsumedByActors=var_11,
        containsActors="bhXBs7S",
        contentfwk_Actor81=var_8,
        isResolvedByActors=var_8,
        isPerformedByActors=var_8,
        contentfwk_Actor90=var_14,
        Actor94=var_4,
        containsActors86=complex(-436.69, -1092.0),
        Actor140=var_4,
    )


def test_6():
    var_1 = python_code_.contentfwk_LogicalDataComponent()
    var_6 = python_code_.contentfwk_Driver()
    var_7 = python_code_.contentfwk_OrganizationUnit(
        headcount=-1588, OrganizationUnit=var_6, OrganizationUnit130=var_1
    )
    assert isinstance(var_7, python_code_.contentfwk_OrganizationUnit)


@pytest.mark.xfail(strict=True)
def test_7():
    var_1 = python_code_.contentfwk_Driver()
    var_2 = python_code_.contentfwk_LogicalApplicationComponent()
    var_3 = "|L[<?s+"
    var_4 = "eDtU9"
    var_5 = python_code_.contentfwk_Principle(
        principleCategory=var_1,
        priority=var_3,
        statementOfPrinciple=var_3,
        rationale=var_3,
        implication=[False, -1, "Actor101"],
        metric=var_4,
    )
    assert isinstance(var_5, python_code_.contentfwk_Principle)
    var_6 = python_code_.contentfwk_Function()
    var_7 = python_code_.contentfwk_Function()
    var_8 = {var_6, var_6, var_6, var_7}
    var_9 = python_code_.contentfwk_Service()
    python_code_.contentfwk_Process(
        processVolumetrics="+k0soao|Ga2 r:-Zp>",
        processCritiality=var_3,
        isAutomated="",
        contentfwk_Process174=var_2,
        isRealizedByProcesses=var_2,
        supportsProcesses=var_8,
        participatesInProcesses163=var_4,
        isGeneratedByProcesses=var_8,
        Process180=var_3,
        Process333=var_9,
    )


def test_8():
    var_1 = "NonStandard Event169"
    var_2 = lambda *args, **kwargs: 1
    var_3 = python_code_.contentfwk_Requirement(
        statementOfRequirement=var_1, rationale=596.39, acceptanceCriteria=var_2
    )
    assert isinstance(var_3, python_code_.contentfwk_Requirement)


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = 'EGc"j,=Jnbu/'
    var_1 = "Actor94"
    var_2 = python_code_.contentfwk_Container(
        name={"_contentfwk_Actor__isPerformedByActors": True},
        id=None,
        description=var_1,
        Container=var_1,
    )
    assert isinstance(var_2, python_code_.contentfwk_Container)
    var_3 = python_code_.contentfwk_Container(
        name=var_0,
        id={-1089.87},
        description=complex(930.4801, -1950.62),
        Container=b"\x03\x90\x08'\xda",
        contentfwk_Container236=var_2,
        contentfwk_Container234=(
            "contentfwk_PhysicalTechnologyComponent188 _contentfwk_Process__Process contentfwk_Process172",
            False,
        ),
    )
    assert isinstance(var_3, python_code_.contentfwk_Container)
    var_4 = python_code_.contentfwk_Label
    python_code_.contentfwk_WorkPackage(workPackageCategory=var_4, isDeliveredBy=574)
