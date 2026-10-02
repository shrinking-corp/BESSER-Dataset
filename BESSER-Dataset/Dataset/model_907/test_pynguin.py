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
    Activity,
    ActivityUseKind,
    Artifact,
    BreakdownElement,
    CapabilityPattern,
    Category,
    Concept,
    ConfigurationPackage,
    ContractKind,
    DescribableElement,
    Enum,
    EstimatingConsideration,
    EstimatingTechnique,
    ExpertiseLevel,
    ExtensibleElement,
    Guidance,
    Kind,
    MethodContentElement,
    MethodContentKind,
    MethodContentPackage,
    MethodContentPackageableElement,
    MethodContentUse,
    MethodLibraryPackageableElement,
    MethodPluginPackageableElement,
    OptionalityKind,
    ParameterDirectionKind,
    Practice,
    Process,
    ProcessElement,
    ProcessPackage,
    ProcessPackageableElement,
    Report,
    RiskLevel,
    RoleUse,
    SupportingMaterial,
    Template,
    ToolMentor,
    VariabilityElement,
    VariabilityType,
    WorkBreakdownElement,
    WorkDefinition,
    WorkDefinitionParameter,
    WorkDefinitionPerformer,
    WorkProductUse,
    WorkSequenceKind,
    abstractmethod,
    date,
    datetime,
    spem_Activity,
    spem_BreakdownElement,
    spem_Category,
    spem_CompositeRole,
    spem_Default_ResponsibilityAssignment,
    spem_Default_TaskDefinitionParameter,
    spem_Default_TaskDefinitionPerformer,
    spem_DescribableElement,
    spem_EObject,
    spem_ExtensibleElement,
    spem_Guidance,
    spem_Kind,
    spem_LifeCycleSpecification,
    spem_MethodConfiguration,
    spem_MethodContentElement,
    spem_MethodContentKind,
    spem_MethodContentPackage,
    spem_MethodContentPackageableElement,
    spem_MethodContentUse,
    spem_MethodLibrary,
    spem_MethodLibraryPackageableElement,
    spem_MethodPlugin,
    spem_MethodPluginPackageableElement,
    spem_Metric,
    spem_Milestone,
    spem_PlanningData,
    spem_ProcessComponent,
    spem_ProcessComponentUse,
    spem_ProcessElement,
    spem_ProcessKind,
    spem_ProcessPackage,
    spem_ProcessPackageableElement,
    spem_ProcessParameter,
    spem_ProcessPerformer,
    spem_ProcessResponsibilityAssignment,
    spem_Qualification,
    spem_RoleDefinition,
    spem_RoleUse,
    spem_Step,
    spem_TaskDefinition,
    spem_TaskUse,
    spem_TeamProfile,
    spem_ToolDefinition,
    spem_VariabilityElement,
    spem_WorkBreakdownElement,
    spem_WorkDefinition,
    spem_WorkDefinitionParameter,
    spem_WorkDefinitionPerformer,
    spem_WorkProductDefinition,
    spem_WorkProductDefinitionRelationship,
    spem_WorkProductKind,
    spem_WorkProductPort,
    spem_WorkProductPortConnector,
    spem_WorkProductUse,
    spem_WorkProductUseRelationship,
    spem_WorkSequence,
    spem_uma_Artifact,
    spem_uma_CapabilityPattern,
    spem_uma_CapabilityPatternPackage,
    spem_uma_CategoryPackage,
    spem_uma_Checklist,
    spem_uma_Concept,
    spem_uma_ConfigurationPackage,
    spem_uma_CustomCategory,
    spem_uma_Deliverable,
    spem_uma_DeliveryProcess,
    spem_uma_DeliveryProcessPackage,
    spem_uma_Discipline,
    spem_uma_DisciplineGrouping,
    spem_uma_DisciplinePackage,
    spem_uma_Domain,
    spem_uma_DomainPackage,
    spem_uma_EstimatingConsideration,
    spem_uma_Example,
    spem_uma_GuidancePackage,
    spem_uma_Guideline,
    spem_uma_Iteration,
    spem_uma_Outcome,
    spem_uma_Phase,
    spem_uma_Practice,
    spem_uma_Process,
    spem_uma_ProcessComponentPackage,
    spem_uma_ProcessPlanningTemplate,
    spem_uma_QualificationPackage,
    spem_uma_Report,
    spem_uma_ReusableAsset,
    spem_uma_Roadmap,
    spem_uma_RoleDefinitionPackage,
    spem_uma_RoleSet,
    spem_uma_RoleSetPackage,
    spem_uma_Root,
    spem_uma_SupportingMaterial,
    spem_uma_TaskDefinitionPackage,
    spem_uma_Template,
    spem_uma_TermDefinition,
    spem_uma_ToolDefinitionPackage,
    spem_uma_ToolMentor,
    spem_uma_Whitepaper,
    spem_uma_WorkProductDefinitionPackage,
    spem_uma_WorkProductKindPackage,
    time,
    uma_spem_Activity,
    uma_spem_MethodConfiguration,
    uma_spem_MethodContentElement,
    uma_spem_MethodLibrary,
    uma_spem_MethodPlugin,
    uma_spem_RoleDefinition,
    uma_spem_TaskDefinition,
    uma_spem_WorkProductDefinition,
    uma_spem_WorkProductPortConnector,
    uma_spem_WorkProductUse,
)


def test_0():
    var_2 = "spem_ProcessComponent149"
    var_5 = python_code_.spem_uma_Deliverable(
        externalDescription=var_2,
        packagingGuidance="\r[n|<1i@2\ro%d>SJV0J",
        spem_uma_Deliverable={-1062},
    )
    assert isinstance(var_5, python_code_.spem_uma_Deliverable)


def test_1():
    var_1 = python_code_.uma_spem_TaskDefinition()
    var_2 = "SupportingMaterial,_spem_MethodPlugin__spem_MethodPlugin191,spem_MethodContentElement"
    var_3 = python_code_.spem_MethodPlugin(
        userChangeable=var_1,
        supporting=var_2,
        spem_MethodPlugin191=(
            -426.82,
            "spem_ProcessComponent-_spem_Activity__spem_Activity30-spem_Step92",
            466.89,
        ),
    )
    assert isinstance(var_3, python_code_.spem_MethodPlugin)
    var_5 = python_code_.Template()
    var_8 = python_code_.spem_uma_Deliverable(
        externalDescription=var_5, packagingGuidance="6w9@Xi\x0cl"
    )
    assert isinstance(var_8, python_code_.spem_uma_Deliverable)
    var_52 = ""
    var_53 = "spem_ProcessComponent149"
    var_55 = (True,)
    var_56 = python_code_.spem_uma_Deliverable(
        externalDescription=var_52,
        packagingGuidance=var_53,
        spem_uma_Deliverable=var_55,
    )
    assert isinstance(var_56, python_code_.spem_uma_Deliverable)


def test_2():
    var_0 = python_code_.uma_spem_WorkProductUse()
    var_1 = python_code_.uma_spem_WorkProductUse()
    var_2 = {var_0, var_0, var_0, var_1, var_1}
    var_3 = python_code_.spem_uma_Deliverable(
        externalDescription=(), packagingGuidance=[], spem_uma_Deliverable=var_2
    )
    assert isinstance(var_3, python_code_.spem_uma_Deliverable)
    var_4 = "_spem_RoleDefinition__spem_RoleDefinition136_spem_WorkProductPort__spem_WorkProductPort203out_spem_Activity__spem_Activity19"
    var_5 = python_code_.spem_Guidance(
        attachment=var_4, spem_Guidance=var_4, spem_Guidance57=-1144.65
    )
    assert isinstance(var_5, python_code_.spem_Guidance)
    var_36 = "spem_WorkProductUse:spem_MethodLibrary:spm_ProcessComponentUse153"
    var_37 = python_code_.spem_uma_ReusableAsset
    var_38 = python_code_.spem_WorkSequence(linkKind=var_36, WorkSequence9=var_37)
    assert isinstance(var_38, python_code_.spem_WorkSequence)
    var_40 = "spem_WorkDefinitionParameter3"
    var_41 = "HXU"
    var_42 = python_code_.spem_uma_Discipline()
    var_56 = python_code_.spem_RoleUse()
    var_57 = python_code_.spem_RoleDefinition(
        synonym=var_37, spem_RoleDefinition=var_56
    )
    assert isinstance(var_57, python_code_.spem_RoleDefinition)
    var_43 = python_code_.spem_uma_DeliveryProcess(
        scale=var_36,
        projectCharacteristics=var_40,
        riskLevel={},
        estimatingTechnique=var_40,
        projectMemberExpertise={True, True},
        typeOfContract=var_41,
        Process=var_42,
    )
    assert isinstance(var_43, python_code_.spem_uma_DeliveryProcess)
    var_53 = python_code_.spem_Step(name=var_36)
    assert isinstance(var_53, python_code_.spem_Step)


def test_3():
    var_33 = python_code_.spem_uma_Discipline()
    var_40 = lambda *args, **kwargs: -1769
    var_46 = python_code_.spem_MethodPlugin(
        userChangeable=b"H\xb9\xca", supporting=var_33, spem_MethodPlugin=False
    )
    assert isinstance(var_46, python_code_.spem_MethodPlugin)
    var_53 = "_spem_DescribableElement__spem_DescribableElement63.spem_WorkProductPort.OTHER.ConfigurationPackage"
    var_54 = "4'\"`J4l|!oTH2"
    var_55 = "_g"
    var_56 = "-e"
    var_57 = python_code_.spem_WorkDefinition(
        preCondition=var_56, postCondition=var_40, spem_WorkDefinition=set()
    )
    assert isinstance(var_57, python_code_.spem_WorkDefinition)
    python_code_.spem_WorkDefinitionParameter(
        name=var_53,
        direction=var_54,
        optionality=var_55,
        spem_WorkDefinitionParameter=var_57,
        spem_WorkDefinitionParameter3=var_33,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.spem_MethodContentPackage()
    var_2 = python_code_.spem_MethodContentUse(isSynchronizedWithSource=var_0)
    assert isinstance(var_2, python_code_.spem_MethodContentUse)
    var_4 = python_code_.spem_CompositeRole()
    var_5 = python_code_.EstimatingTechnique.TIME
    var_8 = "*IR<"
    var_9 = python_code_.spem_TaskUse(
        preCondition=var_8,
        postCondition=var_8,
        spem_TaskUse=var_0,
        spem_TaskUse127=[
            "_spem_MethodContentElement__spem_MethodContentElement76",
            True,
            "/q1:j%7Sb",
        ],
    )
    assert isinstance(var_9, python_code_.spem_TaskUse)
    var_10 = python_code_.spem_MethodContentPackageableElement(name=var_8)
    assert isinstance(var_10, python_code_.spem_MethodContentPackageableElement)
    var_12 = python_code_.spem_uma_Discipline()
    var_19 = lambda *args, **kwargs: -1769
    var_20 = False
    var_21 = python_code_.spem_WorkProductPort(
        isOptional=var_20, portKind=var_19, spem_WorkProductPort154=var_10
    )
    assert isinstance(var_21, python_code_.spem_WorkProductPort)
    var_22 = {var_21, var_21, var_21}
    var_23 = python_code_.spem_ProcessComponent(
        copyright=var_2,
        author=var_4,
        version=var_12,
        changeDate=var_19,
        changeDescription=var_5,
        spem_ProcessComponent=-265,
        spem_ProcessComponent149=var_22,
        spem_ProcessComponent151=var_19,
    )
    assert isinstance(var_23, python_code_.spem_ProcessComponent)
    var_25 = python_code_.spem_Metric(expression=var_8)
    assert isinstance(var_25, python_code_.spem_Metric)
    var_26 = python_code_.spem_MethodPlugin(
        userChangeable=b"H\xb9\xca", supporting=var_12, spem_MethodPlugin=False
    )
    assert isinstance(var_26, python_code_.spem_MethodPlugin)
    var_33 = "_spem_DescribableElement__spem_DescribableElement63.spem_WorkProductPort.OTHER.ConfigurationPackage"
    var_34 = "4'\"`J4l|!oTH2"
    var_35 = "_g"
    var_36 = "-e"
    var_37 = python_code_.spem_WorkDefinition(
        preCondition=var_36, postCondition=var_19, spem_WorkDefinition=set()
    )
    assert isinstance(var_37, python_code_.spem_WorkDefinition)
    var_38 = python_code_.spem_WorkDefinitionParameter(
        name=var_33,
        direction=var_34,
        optionality=var_35,
        spem_WorkDefinitionParameter=var_37,
        spem_WorkDefinitionParameter3=var_12,
    )
    python_code_.spem_WorkProductDefinition(
        impactOfNotHaving=set(),
        reasonForNotNeeding=var_8,
        spem_WorkProductDefinition=var_38,
    )


def test_5():
    var_1 = python_code_.uma_spem_TaskDefinition()
    var_2 = "SupportingMaterial,_spem_MethodPlugin__spem_MethodPlugin191,spem_MethodContentElement"
    var_3 = python_code_.spem_MethodPlugin(
        userChangeable=var_1,
        supporting=var_2,
        spem_MethodPlugin191=(
            -426.82,
            "spem_ProcessComponent-_spem_Activity__spem_Activity30-spem_Step92",
            466.89,
        ),
    )
    assert isinstance(var_3, python_code_.spem_MethodPlugin)
    var_5 = python_code_.Template()
    var_6 = python_code_.uma_spem_MethodPlugin()
    var_7 = python_code_.uma_spem_TaskDefinition()
    var_8 = python_code_.spem_uma_Deliverable(
        externalDescription=var_5, packagingGuidance="6w9@Xi\x0cl"
    )
    assert isinstance(var_8, python_code_.spem_uma_Deliverable)
    var_30 = python_code_.spem_uma_Concept()
    var_32 = lambda *args, **kwargs: -2999
    var_33 = "BLj&u!.G'jU"
    var_39 = python_code_.spem_VariabilityElement(variabilityType=var_33)
    assert isinstance(var_39, python_code_.spem_VariabilityElement)
    var_42 = python_code_.spem_TaskDefinition()
    var_43 = python_code_.spem_TaskUse(
        preCondition=210.06,
        postCondition=var_32,
        spem_TaskUse=var_30,
        spem_TaskUse127=var_42,
    )
    assert isinstance(var_43, python_code_.spem_TaskUse)
    var_44 = python_code_.spem_WorkProductDefinitionRelationship()
    var_45 = python_code_.spem_WorkProductDefinition(
        impactOfNotHaving=var_2,
        reasonForNotNeeding=var_39,
        spem_WorkProductDefinition45=[],
        spem_WorkProductDefinition107=var_44,
    )
    assert isinstance(var_45, python_code_.spem_WorkProductDefinition)
    var_46 = python_code_.spem_Metric(expression=var_7, spem_Metric=var_6)
    assert isinstance(var_46, python_code_.spem_Metric)


@pytest.mark.xfail(strict=True)
def test_6():
    var_4 = python_code_.CapabilityPattern()
    var_6 = python_code_.spem_WorkProductUseRelationship
    var_7 = lambda *args, **kwargs: False
    var_12 = python_code_.spem_Metric(expression=var_7)
    assert isinstance(var_12, python_code_.spem_Metric)
    var_13 = python_code_.BreakdownElement()
    var_15 = False
    var_16 = python_code_.spem_BreakdownElement(
        hasMultipleOccurrences=var_15,
        isOptional=var_15,
        isPlanned=var_15,
        spem_BreakdownElement=var_12,
    )
    assert isinstance(var_16, python_code_.spem_BreakdownElement)
    python_code_.spem_Activity(
        useKind=var_6,
        howToStaff=var_6,
        isEnactable=var_15,
        spem_Activity30=var_13,
        spem_Activity13=-1910.08,
        spem_Activity22=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_33 = python_code_.WorkDefinition()
    var_35 = "*IR<"
    var_68 = python_code_.spem_Step(name=var_35, spem_Step90=var_33)
    assert isinstance(var_68, python_code_.spem_Step)
    var_36 = python_code_.spem_MethodContentPackageableElement(name=var_35)
    assert isinstance(var_36, python_code_.spem_MethodContentPackageableElement)
    var_38 = python_code_.spem_uma_Discipline()
    var_45 = lambda *args, **kwargs: -1769
    var_46 = False
    var_47 = python_code_.spem_WorkProductPort(
        isOptional=var_46, portKind=var_45, spem_WorkProductPort154=var_36
    )
    assert isinstance(var_47, python_code_.spem_WorkProductPort)
    var_50 = python_code_.spem_Metric(expression=var_35)
    assert isinstance(var_50, python_code_.spem_Metric)
    var_51 = python_code_.spem_MethodPlugin(
        userChangeable=b"H\xb9\xca", supporting=var_38, spem_MethodPlugin=False
    )
    assert isinstance(var_51, python_code_.spem_MethodPlugin)
    var_58 = "_spem_DescribableElement__spem_DescribableElement63.spem_WorkProductPort.OTHER.ConfigurationPackage"
    var_59 = "4'\"`J4l|!oTH2"
    var_60 = "_g"
    var_61 = "-e"
    var_62 = python_code_.spem_WorkDefinition(
        preCondition=var_61, postCondition=var_45, spem_WorkDefinition=set()
    )
    assert isinstance(var_62, python_code_.spem_WorkDefinition)
    var_63 = python_code_.spem_WorkDefinitionParameter(
        name=var_58,
        direction=var_59,
        optionality=var_60,
        spem_WorkDefinitionParameter=var_62,
        spem_WorkDefinitionParameter3=var_38,
    )
    python_code_.spem_WorkProductDefinition(
        impactOfNotHaving=set(),
        reasonForNotNeeding=var_35,
        spem_WorkProductDefinition=var_63,
    )


def test_8():
    var_1 = python_code_.uma_spem_TaskDefinition()
    var_2 = "SupportingMaterial,_spem_MethodPlugin__spem_MethodPlugin191,spem_MethodContentElement"
    var_3 = python_code_.spem_MethodPlugin(
        userChangeable=var_1,
        supporting=var_2,
        spem_MethodPlugin191=(
            -426.82,
            "spem_ProcessComponent-_spem_Activity__spem_Activity30-spem_Step92",
            466.89,
        ),
    )
    assert isinstance(var_3, python_code_.spem_MethodPlugin)
    var_5 = python_code_.Template()
    var_6 = python_code_.uma_spem_MethodPlugin()
    var_7 = python_code_.uma_spem_TaskDefinition()
    var_8 = python_code_.spem_uma_Deliverable(
        externalDescription=var_5, packagingGuidance="6w9@Xi\x0cl"
    )
    assert isinstance(var_8, python_code_.spem_uma_Deliverable)
    var_32 = lambda *args, **kwargs: -2999
    var_33 = "BLj&u!.I'jU"
    var_39 = python_code_.spem_VariabilityElement(variabilityType=var_33)
    assert isinstance(var_39, python_code_.spem_VariabilityElement)
    var_44 = python_code_.spem_WorkProductDefinitionRelationship()
    var_45 = python_code_.spem_WorkProductDefinition(
        impactOfNotHaving=var_2,
        reasonForNotNeeding=var_39,
        spem_WorkProductDefinition45=[],
        spem_WorkProductDefinition107=var_44,
    )
    assert isinstance(var_45, python_code_.spem_WorkProductDefinition)
    var_46 = python_code_.spem_Metric(expression=var_7, spem_Metric=var_6)
    assert isinstance(var_46, python_code_.spem_Metric)
    var_47 = "spem_RoleUse-HIGH-SupportingMaterial-spem_Activity16"
    var_48 = python_code_.spem_MethodContentElement(
        copyright=var_32,
        author=var_47,
        changeDate={},
        changeDescription=var_2,
        version=var_3,
        spem_MethodContentElement73={},
    )
    assert isinstance(var_48, python_code_.spem_MethodContentElement)


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.spem_Default_TaskDefinitionPerformer()
    var_1 = python_code_.uma_spem_TaskDefinition()
    var_2 = "SupportingMaterial,_spem_MethodPlugin__spem_MethodPlugin191,spem_MethodContentElement"
    var_3 = python_code_.spem_MethodPlugin(
        userChangeable=var_1,
        supporting=var_2,
        spem_MethodPlugin191=(
            -426.82,
            "spem_ProcessComponent-_spem_Activity__spem_Activity30-spem_Step92",
            466.89,
        ),
    )
    assert isinstance(var_3, python_code_.spem_MethodPlugin)
    var_5 = python_code_.Template()
    var_8 = python_code_.spem_uma_Deliverable(
        externalDescription=var_5, packagingGuidance="6w9@Xi\x0cl"
    )
    assert isinstance(var_8, python_code_.spem_uma_Deliverable)
    var_10 = "spem_WorkProductUse:spem_MethodLibrary:spem_ProcessComponentUse153"
    var_11 = python_code_.spem_uma_ReusableAsset
    var_12 = python_code_.spem_WorkSequence(linkKind=var_10, WorkSequence9=var_11)
    assert isinstance(var_12, python_code_.spem_WorkSequence)
    var_14 = "spem_WorkDefinitionParameter3"
    var_15 = "HXU"
    var_16 = python_code_.spem_uma_Discipline()
    var_17 = python_code_.spem_uma_DeliveryProcess(
        scale=var_10,
        projectCharacteristics=var_2,
        riskLevel={},
        estimatingTechnique=var_14,
        projectMemberExpertise={True, True},
        typeOfContract=var_15,
        Process=var_16,
    )
    assert isinstance(var_17, python_code_.spem_uma_DeliveryProcess)
    var_27 = python_code_.spem_Step(name=var_10)
    assert isinstance(var_27, python_code_.spem_Step)
    python_code_.spem_TaskUse(
        preCondition=var_11, postCondition=set(), spem_TaskUse130=var_0
    )


def test_10():
    var_15 = python_code_.spem_uma_Concept()
    var_17 = lambda *args, **kwargs: -2999
    var_18 = "BLj&u!.G'jU"
    var_24 = python_code_.spem_VariabilityElement(variabilityType=var_18)
    assert isinstance(var_24, python_code_.spem_VariabilityElement)
    var_27 = python_code_.spem_TaskDefinition()
    var_28 = python_code_.spem_TaskUse(
        preCondition=210.06,
        postCondition=var_17,
        spem_TaskUse=var_15,
        spem_TaskUse127=var_27,
    )
    assert isinstance(var_28, python_code_.spem_TaskUse)
    var_29 = python_code_.spem_WorkProductDefinitionRelationship()
    var_30 = python_code_.spem_WorkProductDefinition(
        impactOfNotHaving=var_18,
        reasonForNotNeeding=var_24,
        spem_WorkProductDefinition45=[],
        spem_WorkProductDefinition107=var_29,
    )
    assert isinstance(var_30, python_code_.spem_WorkProductDefinition)


def test_11():
    var_0 = python_code_.spem_uma_Concept()
    var_4 = python_code_.spem_Step(name=var_0, spem_Step=False, spem_Step90=False)
    assert isinstance(var_4, python_code_.spem_Step)


def test_12():
    var_4 = "COST,spem_WorkProductUse44"
    var_5 = python_code_.spem_Guidance(
        attachment=var_4, spem_Guidance57='G:)V"\rbE@FEIykYXu'
    )
    assert isinstance(var_5, python_code_.spem_Guidance)


def test_13():
    var_5 = python_code_.spem_uma_DeliveryProcessPackage()
    var_11 = True
    var_12 = python_code_.spem_MethodContentUse(isSynchronizedWithSource=var_11)
    assert isinstance(var_12, python_code_.spem_MethodContentUse)
    var_20 = python_code_.WorkDefinition()
    var_24 = python_code_.spem_PlanningData(
        startDate=var_5, finishDate=var_20, rank=False, duration=set()
    )
    assert isinstance(var_24, python_code_.spem_PlanningData)


def test_14():
    var_12 = python_code_.ExtensibleElement()
    var_39 = False
    var_40 = python_code_.spem_WorkProductPort(
        isOptional=var_39,
        portKind="SupportingMaterial uma_spem_MethodContentElement LEVEL",
        spem_WorkProductPort154=var_12,
    )
    assert isinstance(var_40, python_code_.spem_WorkProductPort)


@pytest.mark.xfail(strict=True)
def test_15():
    var_2 = "startToFinish"
    var_3 = python_code_.spem_Step(name=var_2)
    assert isinstance(var_3, python_code_.spem_Step)
    var_4 = python_code_.CapabilityPattern()
    var_5 = "Z>0UZ&XCZfHoM"
    var_6 = python_code_.spem_WorkProductUseRelationship
    var_7 = lambda *args, **kwargs: False
    var_8 = python_code_.EstimatingConsideration()
    var_9 = {var_8}
    var_10 = python_code_.spem_WorkProductDefinitionRelationship()
    var_11 = python_code_.spem_WorkProductDefinition(
        impactOfNotHaving=var_5,
        reasonForNotNeeding=var_6,
        spem_WorkProductDefinition45=var_7,
        spem_WorkProductDefinition=var_6,
        spem_WorkProductDefinition204=True,
        spem_WorkProductDefinition94=var_9,
        spem_WorkProductDefinition101=b"\x8f\x98\xb2VV\xf53zh",
        spem_WorkProductDefinition110=var_10,
    )
    assert isinstance(var_11, python_code_.spem_WorkProductDefinition)
    var_12 = python_code_.spem_Metric(expression=var_7)
    assert isinstance(var_12, python_code_.spem_Metric)
    var_13 = python_code_.BreakdownElement()
    var_15 = False
    var_16 = python_code_.spem_BreakdownElement(
        hasMultipleOccurrences=var_15,
        isOptional=var_15,
        isPlanned=var_15,
        spem_BreakdownElement=var_12,
    )
    assert isinstance(var_16, python_code_.spem_BreakdownElement)
    python_code_.spem_Activity(
        useKind=var_6,
        howToStaff=var_6,
        isEnactable=var_15,
        spem_Activity30=var_13,
        spem_Activity13=-1910.08,
        spem_Activity22=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_16():
    var_35 = python_code_.spem_uma_Discipline()
    var_42 = lambda *args, **kwargs: -1769
    var_45 = python_code_.spem_MethodPlugin(
        userChangeable=b"H\xb9\xca", supporting=var_35, spem_MethodPlugin=False
    )
    assert isinstance(var_45, python_code_.spem_MethodPlugin)
    var_52 = "_spem_DescribableElement__spem_DescribableElement63.spem_WorkProductPort.OTHER.ConfigurationPackage"
    var_53 = "4'\"`J4l|!oTH2"
    var_54 = "_g"
    var_55 = "-e"
    var_56 = python_code_.spem_WorkDefinition(
        preCondition=var_55, postCondition=var_42, spem_WorkDefinition=set()
    )
    assert isinstance(var_56, python_code_.spem_WorkDefinition)
    var_57 = python_code_.spem_WorkDefinitionParameter(
        name=var_52,
        direction=var_53,
        optionality=var_54,
        spem_WorkDefinitionParameter=var_56,
        spem_WorkDefinitionParameter3=var_35,
    )
    python_code_.spem_WorkProductDefinition(
        impactOfNotHaving=set(),
        reasonForNotNeeding=var_53,
        spem_WorkProductDefinition=var_57,
    )


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = python_code_.uma_spem_WorkProductUse()
    var_1 = python_code_.uma_spem_WorkProductUse()
    var_2 = {var_0, var_0, var_0, var_1, var_1}
    var_3 = python_code_.spem_uma_Deliverable(
        externalDescription=(), packagingGuidance=[], spem_uma_Deliverable=var_2
    )
    assert isinstance(var_3, python_code_.spem_uma_Deliverable)
    var_4 = "_spem_RoleDefinition__spem_RoleDefinition136_spem_WorkProductPort__spem_WorkProductPort203out_spem_Activity__spem_Activity19"
    var_5 = python_code_.spem_Guidance(
        attachment=var_4, spem_Guidance=var_4, spem_Guidance57=-1144.65
    )
    assert isinstance(var_5, python_code_.spem_Guidance)
    var_14 = lambda *args, **kwargs: -2999
    var_15 = "BLj&u!.G'jU"
    var_16 = "Pu30\\Q6/_\rQhd"
    var_17 = python_code_.spem_DescribableElement(
        presentationName=var_15,
        briefDescription=var_16,
        purpose=var_16,
        mainDescription=True,
        spem_DescribableElement59=var_2,
        spem_DescribableElement63=var_0,
    )
    assert isinstance(var_17, python_code_.spem_DescribableElement)
    python_code_.spem_DescribableElement(
        presentationName=1797,
        briefDescription=var_4,
        purpose=var_14,
        mainDescription=var_14,
        spem_DescribableElement60=var_14,
        spem_DescribableElement63=var_17,
    )


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = python_code_.spem_uma_Example()
    var_1 = python_code_.spem_uma_DeliveryProcessPackage()
    var_5 = python_code_.spem_WorkDefinitionPerformer()
    var_11 = (
        "_spem_uma_Process__spem_uma_Process211_spem_uma_Process__spem_uma_Process211"
    )
    var_12 = python_code_.spem_TaskUse(
        preCondition=[], postCondition=var_11, spem_TaskUse127=False
    )
    assert isinstance(var_12, python_code_.spem_TaskUse)
    var_20 = python_code_.spem_uma_CategoryPackage()
    var_25 = python_code_.spem_Metric(expression=var_5)
    assert isinstance(var_25, python_code_.spem_Metric)
    var_26 = {var_25, var_25, var_25, var_25}
    var_28 = ":;zmJzx\\%\tj,\\YgI^I"
    var_29 = "&\x0c0_\rI&vTRcn&atPv"
    var_30 = python_code_.spem_DescribableElement(
        presentationName={
            "": -2254,
            '"t\r}@-9s.?y"J_J(L|E': "vsXj1bb0rJW",
            '>Zoj\x0csg"h;cv2>^': -1,
        },
        briefDescription=set(),
        purpose=var_29,
        mainDescription=True,
        spem_DescribableElement69=var_26,
        spem_DescribableElement59=var_26,
    )
    assert isinstance(var_30, python_code_.spem_DescribableElement)
    python_code_.spem_DescribableElement(
        presentationName=var_20,
        briefDescription=var_0,
        purpose=var_28,
        mainDescription=var_29,
        spem_DescribableElement60=var_1,
        spem_DescribableElement65=var_30,
        spem_DescribableElement63=var_30,
    )


def test_19():
    python_code_.EstimatingConsideration()


def test_20():
    var_2 = "linkToSuccessor"
    var_5 = lambda *args, **kwargs: True
    var_25 = True
    var_26 = python_code_.spem_WorkProductPort(
        isOptional=var_25,
        portKind=var_2,
        spem_WorkProductPort206=var_5,
        spem_WorkProductPort154=complex(2029.9391049, -822.0),
    )
    assert isinstance(var_26, python_code_.spem_WorkProductPort)


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = python_code_.spem_uma_Concept()
    var_4 = python_code_.spem_Step(name=var_0, spem_Step=False, spem_Step90=False)
    assert isinstance(var_4, python_code_.spem_Step)
    var_15 = python_code_.spem_ProcessPerformer()
    var_16 = True
    var_17 = list
    python_code_.spem_WorkBreakdownElement(
        isRepeatable=var_16,
        isOngoing=var_16,
        isEventDriven=2713,
        WorkBreakdownElement=var_15,
        successor=var_17,
    )
