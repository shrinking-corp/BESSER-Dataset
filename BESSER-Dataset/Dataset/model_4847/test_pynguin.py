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
    CapabilityType,
    EnterpriseObject,
    EnterpriseObjectiveType,
    EnterpriseProcessor,
    EnterpriseResource,
    Enum,
    ObjectView,
    ObjectiveNature,
    OrganisationCell,
    Origin,
    ProductNature,
    ProductState,
    RequirementNature,
    RequirementOrigin,
    RoleType,
    SIPME_object,
    ServiceState,
    Stakeholder,
    StakeholderType,
    abstractmethod,
    date,
    datetime,
    sipme_Activity,
    sipme_Application,
    sipme_BusinessProcess,
    sipme_BusinessRules,
    sipme_Capability,
    sipme_Capacity,
    sipme_CompanyMember,
    sipme_Device_Machine,
    sipme_Domain,
    sipme_Enterprise,
    sipme_EnterpriseObject,
    sipme_EnterpriseProcessor,
    sipme_EnterpriseProduct,
    sipme_EnterpriseResource,
    sipme_EnterpriseService,
    sipme_Event,
    sipme_ObjectView,
    sipme_Objective,
    sipme_ObjectsFileView,
    sipme_OrganisationCell,
    sipme_Requirement,
    sipme_Role_Function,
    sipme_SIPME_object,
    sipme_Stakeholder,
    sipme_Task,
    sipme_Workstation,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_1 = python_code_.ProductNature.Information
    var_2 = python_code_.sipme_Task
    python_code_.sipme_ObjectsFileView(
        filePriority=var_1,
        fileState=(True,),
        sipme_ObjectsFileView=var_2,
        sipme_ObjectsFileView94={},
    )


def test_1():
    var_0 = python_code_.sipme_BusinessRules()
    var_1 = {var_0, var_0, var_0, var_0}
    var_5 = "n\tMqQN\\soqeU0"
    var_8 = set()
    var_12 = python_code_.sipme_EnterpriseService(serviceState=set())
    assert isinstance(var_12, python_code_.sipme_EnterpriseService)
    var_23 = python_code_.sipme_Enterprise(
        acronym=1,
        status=var_5,
        sipme_Enterprise=var_8,
        sipme_Enterprise24=var_5,
        sipme_Enterprise30=var_1,
        sipme_Enterprise32=var_8,
    )
    assert isinstance(var_23, python_code_.sipme_Enterprise)
    var_17 = "(O+K)\x0cH#\tpHT-F"
    var_19 = python_code_.sipme_ObjectsFileView(filePriority=var_8, fileState=var_17)
    assert isinstance(var_19, python_code_.sipme_ObjectsFileView)
    var_21 = python_code_.sipme_Workstation(ProfileDeescription=True, responsibleOf=[])
    assert isinstance(var_21, python_code_.sipme_Workstation)


def test_2():
    var_0 = python_code_.sipme_ObjectView(
        viewPoint=(),
        sipme_ObjectView47=complex(-1005.87224, 1290.6),
        hasAssociatedEvents=None,
    )
    assert isinstance(var_0, python_code_.sipme_ObjectView)


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = "70\n~~"
    var_1 = python_code_.sipme_EnterpriseService(serviceState=var_0)
    assert isinstance(var_1, python_code_.sipme_EnterpriseService)
    var_3 = -64.69
    var_4 = lambda *args, **kwargs: []
    var_5 = python_code_.sipme_Domain(
        domainCharacterization=var_0,
        performanceIndicators=var_3,
        sipme_Domain20=var_0,
        sipme_Domain25=var_4,
    )
    assert isinstance(var_5, python_code_.sipme_Domain)
    var_6 = "*|O"
    var_7 = object
    python_code_.sipme_Event(
        occurenceProbability=var_7,
        frequency=var_6,
        timeStamp=None,
        source=var_7,
        generates=var_7,
        Event84=[-3014],
        sipme_Event71=b"Ab\x07\xa6\xf9\xc71S\x046\x0f\xa5|/\x91\x02",
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.sipme_BusinessRules()
    var_1 = {var_0, var_0, var_0, var_0}
    var_2 = python_code_.sipme_Role_Function(
        roleType={"w!O7!yl@rNL35\\^HWZ)", -2713.39, False},
        plays=b"\x98\x01\x19",
        isAbleToPlay=set(),
        sipme_Role_Function121=var_1,
    )
    assert isinstance(var_2, python_code_.sipme_Role_Function)
    var_3 = hash
    python_code_.sipme_Objective(
        objectiveType=[],
        objectiveNature=var_3,
        Objective=var_3,
        subObjectives=complex(955.0, -1120.8),
        associatedObjective=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "_sipme_Objective__Objective100sipme_Workstation"
    var_1 = python_code_.sipme_BusinessProcess
    var_2 = python_code_.sipme_Workstation(
        ProfileDeescription=var_0, responsibleOf=var_1
    )
    assert isinstance(var_2, python_code_.sipme_Workstation)
    var_6 = -1489
    var_7 = python_code_.sipme_BusinessRules()
    var_8 = python_code_.sipme_Task(taskDuration=var_6, sipme_Task127=var_7)
    assert isinstance(var_8, python_code_.sipme_Task)
    var_9 = python_code_.sipme_Device_Machine(
        manufacturer=[
            "_sipme_CompanyMember__cellResponsible,sipme_Workstation",
            -553.64,
            912.51,
        ],
        machineMaintainer=var_0,
    )
    assert isinstance(var_9, python_code_.sipme_Device_Machine)
    var_13 = -2274
    var_14 = "Event49,_sipme_EnterpriseResource__EnterpriseResource,coveredBy"
    python_code_.sipme_CompanyMember(
        fullName=(-1856.6, 529, True),
        socialSecurityNumber=var_13,
        address=var_14,
        responsible=-745.83,
        cellResponsible=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = python_code_.sipme_SIPME_object(
        name=[
            True,
            "_sipme_Event__generates.Functional.Controle",
            "_sipme_EnterpriseObject__sipme_EnterpriseObject28",
        ],
        description={"/}'=X"},
        UUID=1,
    )
    assert isinstance(var_0, python_code_.sipme_SIPME_object)
    var_1 = "organisationCell"
    var_2 = python_code_.sipme_BusinessRules()
    var_3 = python_code_.sipme_Task(taskDuration=var_0, sipme_Task127=var_2)
    assert isinstance(var_3, python_code_.sipme_Task)
    python_code_.sipme_Activity(
        endingStatus=var_1, ActivityDuration=var_1, taskOf=var_1, Activity130=var_3
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_38 = ">r"
    var_39 = python_code_.sipme_Device_Machine(
        manufacturer=var_38, machineMaintainer=var_38
    )
    assert isinstance(var_39, python_code_.sipme_Device_Machine)
    var_5 = python_code_.ProductState
    var_14 = python_code_.sipme_BusinessRules()
    var_19 = "sipme_OrganisationCell91"
    var_20 = python_code_.sipme_Device_Machine(
        manufacturer=b"\xd45q\x7f\x87\xc8\x8f\xd3\xa6\xd7\xf6M%\xbf\xbf",
        machineMaintainer=var_19,
    )
    var_21 = "$d^C7`p]l%{"
    var_22 = "]=|sUTE0(8#?='zp"
    var_23 = python_code_.sipme_Stakeholder(
        stakeholderType=var_21, stakeholderOrganism=var_22
    )
    assert isinstance(var_23, python_code_.sipme_Stakeholder)
    var_24 = "V(s%rG@qlyb@"
    var_25 = python_code_.sipme_Enterprise(acronym=var_20, status=var_24)
    assert isinstance(var_25, python_code_.sipme_Enterprise)
    var_26 = "EaNwc"
    var_27 = python_code_.sipme_EnterpriseProduct(
        productState=var_24, productNarure=var_26
    )
    assert isinstance(var_27, python_code_.sipme_EnterpriseProduct)
    var_28 = python_code_.sipme_Application(
        applicationEditor=(3,), applicationMaintainer=var_25
    )
    assert isinstance(var_28, python_code_.sipme_Application)
    var_30 = 55
    var_31 = python_code_.sipme_Activity(
        endingStatus=var_14,
        ActivityDuration={},
        sipme_Activity=var_30,
        Activity130=var_5,
    )
    assert isinstance(var_31, python_code_.sipme_Activity)
    python_code_.sipme_BusinessProcess(ProcessPriority=var_30, BusinessProcess=var_31)


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = python_code_.sipme_BusinessRules()
    var_12 = python_code_.sipme_EnterpriseService(serviceState=set())
    assert isinstance(var_12, python_code_.sipme_EnterpriseService)
    var_24 = complex
    python_code_.sipme_EnterpriseProcessor(
        processorOrigin=var_0,
        EnterpriseProcessor=var_24,
        implementedBy=var_12,
        sipme_EnterpriseProcessor58=var_24,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.sipme_BusinessRules()
    var_1 = {var_0, var_0, var_0, var_0}
    var_32 = 61
    var_34 = "Event49,_sipme_EnterpriseResource__EnterpriseResource,coveredBy"
    python_code_.sipme_EnterpriseProcessor(
        processorOrigin=var_34,
        generatedBy=var_1,
        sipme_EnterpriseProcessor46=var_32,
        sipme_EnterpriseProcessor110=var_34,
        initiates=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_1 = python_code_.EnterpriseProcessor()
    var_4 = "#N<KVbDe?8%EP4!_xOk"
    var_5 = python_code_.sipme_OrganisationCell
    var_6 = python_code_.sipme_Objective(
        objectiveType=var_4,
        objectiveNature=var_1,
        sipme_Objective=var_5,
        refines=(),
        Objective100=var_5,
    )
    assert isinstance(var_6, python_code_.sipme_Objective)
    python_code_.sipme_Objective(
        objectiveType=var_1, objectiveNature=var_1, Objective79=var_6
    )


def test_11():
    var_4 = -1149
    var_26 = "cellReLponsible"
    var_27 = python_code_.sipme_Device_Machine
    var_30 = "H#=#*3XbViRprz.[H "
    var_31 = "c9WcF'`D}!s [bD}B\n"
    var_32 = python_code_.sipme_Objective(
        objectiveType=var_27,
        objectiveNature=var_4,
        subObjectives={"&s|n;0<$2N8": 567.94},
        associatedObjective={},
    )
    assert isinstance(var_32, python_code_.sipme_Objective)
    var_33 = python_code_.sipme_Requirement(
        requirementVersion=var_30,
        requirementDate={-130.6, "_sipme_Event__Event84"},
        requirementStatement=-3658,
        requirementPriority=var_26,
        requirementMaturity=var_4,
        requirementStatus=var_31,
        requirementOrigin=var_26,
        requirementNature=var_27,
        Requirement=var_32,
    )
    assert isinstance(var_33, python_code_.sipme_Requirement)


def test_12():
    var_1 = "_sipme_Act`ivity__taskOfSystem_requiremenkt_sipme_EnterpriseResource__EnterpriseResource"
    var_77 = lambda *args, **kwargs: "!K=ZPA9\x0b;5\x0c<(V"
    var_78 = python_code_.sipme_Capacity(value=var_77, unit=var_1)
    assert isinstance(var_78, python_code_.sipme_Capacity)


def test_13():
    var_0 = python_code_.sipme_SIPME_object(
        name="A5q", description="\nQJ0(XgX\x0ckS7_DGf", UUID="fLPy'gd\"jV@%$Xf["
    )
    assert isinstance(var_0, python_code_.sipme_SIPME_object)
    var_1 = "organisationCell"
    var_6 = bool
    var_7 = python_code_.sipme_Application(
        applicationEditor=var_6, applicationMaintainer=var_1
    )
    assert isinstance(var_7, python_code_.sipme_Application)
    var_42 = python_code_.sipme_Capability(capabilityType=set())
    assert isinstance(var_42, python_code_.sipme_Capability)


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = -1306
    var_1 = lambda *args, **kwargs: []
    python_code_.sipme_Workstation(
        ProfileDeescription={False},
        Workstation11=var_0,
        responsibleOf=var_0,
        inChargeOf=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_15():
    var_14 = 489
    var_15 = python_code_.sipme_OrganisationCell(
        organisationLevel=var_14,
        responsibleOfCell={
            "XPOmz$)_nG\t|@X": "Jg[Sl{]L:}Ct+,j",
            "L;5\n$U7nIg": 1077.73,
        },
    )
    assert isinstance(var_15, python_code_.sipme_OrganisationCell)
    var_16 = python_code_.EnterpriseResource()
    var_25 = lambda *args, **kwargs: False
    python_code_.sipme_OrganisationCell(
        organisationLevel=var_16,
        OrganisationCell18=var_25,
        coveredBy=complex(-2222.02, 1370.173377),
    )


@pytest.mark.xfail(strict=True)
def test_16():
    var_1 = python_code_.ProductNature.Information
    var_2 = python_code_.EnterpriseResource
    var_3 = python_code_.sipme_ObjectsFileView(
        filePriority=-1, fileState="(gx@Sf$r\x0bR/V", responsibleOfFile=None
    )
    assert isinstance(var_3, python_code_.sipme_ObjectsFileView)
    var_5 = "sipme_Task133-_sipme_EnterpriseObject__EnterpriseObject42-_sipme_Task__sipme_Task127-_sipme_Role_Function__Role_Function64"
    var_6 = python_code_.sipme_EnterpriseProduct(
        productState=var_2, productNarure=var_5
    )
    assert isinstance(var_6, python_code_.sipme_EnterpriseProduct)
    var_7 = python_code_.sipme_Capability(capabilityType=set())
    assert isinstance(var_7, python_code_.sipme_Capability)
    var_8 = python_code_.sipme_Capacity(value=var_1, unit=var_2)
    assert isinstance(var_8, python_code_.sipme_Capacity)
    python_code_.sipme_Capability(capabilityType=True, sipme_Capability=var_8)
