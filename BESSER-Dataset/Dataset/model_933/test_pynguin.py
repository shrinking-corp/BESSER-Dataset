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
    Activity,
    ActivityDescription,
    BreakdownElement,
    BreakdownElementDescription,
    Concept,
    ContentCategory,
    ContentDescription,
    ContentElement,
    DescribableElement,
    Descriptor,
    Element,
    Enum,
    Guidance,
    MethodElement,
    MethodPackage,
    MethodUnit,
    NamedElement,
    PackageableElement,
    Process,
    ProcessDescription,
    ProcessElement,
    ProcessPackage,
    RoleDescriptor,
    VariabilityType,
    WorkBreakdownElement,
    WorkOrderType,
    WorkProduct,
    WorkProductDescription,
    date,
    datetime,
    time,
    uma_Activity,
    uma_ActivityDescription,
    uma_ApplicableMetaClassInfo,
    uma_Artifact,
    uma_ArtifactDescription,
    uma_BreakdownElement,
    uma_BreakdownElementDescription,
    uma_CapabilityPattern,
    uma_Checklist,
    uma_CompositeRole,
    uma_Concept,
    uma_Constraint,
    uma_ContentCategory,
    uma_ContentCategoryPackage,
    uma_ContentDescription,
    uma_ContentElement,
    uma_ContentPackage,
    uma_CustomCategory,
    uma_Deliverable,
    uma_DeliverableDescription,
    uma_DeliveryProcess,
    uma_DeliveryProcessDescription,
    uma_DescribableElement,
    uma_Descriptor,
    uma_DescriptorDescription,
    uma_Discipline,
    uma_DisciplineGrouping,
    uma_DocumentRoot,
    uma_Domain,
    uma_EStringToStringMapEntry,
    uma_Element,
    uma_Estimate,
    uma_EstimatingMetric,
    uma_EstimationConsiderations,
    uma_Example,
    uma_Guidance,
    uma_GuidanceDescription,
    uma_Guideline,
    uma_Iteration,
    uma_Kind,
    uma_MethodConfiguration,
    uma_MethodElement,
    uma_MethodElementProperty,
    uma_MethodLibrary,
    uma_MethodPackage,
    uma_MethodPlugin,
    uma_MethodUnit,
    uma_Milestone,
    uma_NamedElement,
    uma_Outcome,
    uma_PackageableElement,
    uma_Phase,
    uma_PlanningData,
    uma_Practice,
    uma_PracticeDescription,
    uma_Process,
    uma_ProcessComponent,
    uma_ProcessComponentInterface,
    uma_ProcessDescription,
    uma_ProcessElement,
    uma_ProcessPackage,
    uma_ProcessPlanningTemplate,
    uma_Report,
    uma_ReusableAsset,
    uma_Roadmap,
    uma_Role,
    uma_RoleDescription,
    uma_RoleDescriptor,
    uma_RoleSet,
    uma_RoleSetGrouping,
    uma_Section,
    uma_SupportingMaterial,
    uma_Task,
    uma_TaskDescription,
    uma_TaskDescriptor,
    uma_TeamProfile,
    uma_Template,
    uma_TermDefinition,
    uma_Tool,
    uma_ToolMentor,
    uma_Whitepaper,
    uma_WorkBreakdownElement,
    uma_WorkDefinition,
    uma_WorkOrder,
    uma_WorkProduct,
    uma_WorkProductDescription,
    uma_WorkProductDescriptor,
    uma_WorkProductType,
)


def test_0():
    var_0 = python_code_.uma_Tool
    var_1 = python_code_.uma_TeamProfile(
        group2={-797.95},
        role={"vJUxEb~<6cwNg q": -2163.09},
        superTeam=None,
        subTeam=var_0,
    )
    assert isinstance(var_1, python_code_.uma_TeamProfile)
    var_2 = "lC-3&U"
    var_3 = "_@63EVIzv"
    var_4 = python_code_.uma_Section(
        sectionName=var_1,
        predecessor=var_2,
        description=None,
        variabilityBasedOnElement=var_0,
        variabilityType=var_3,
    )
    assert isinstance(var_4, python_code_.uma_Section)
    var_7 = "lj"
    var_10 = "\tL7t&:K-j?]4l:dD/("
    var_19 = python_code_.uma_ContentCategory()
    var_21 = python_code_.uma_RoleDescriptor(role=var_10, responsibleFor=(-2815,))
    assert isinstance(var_21, python_code_.uma_RoleDescriptor)
    var_23 = python_code_.uma_WorkOrder(
        value=var_19,
        id=-1663.88,
        linkType=var_0,
        properties=complex(1994.61559, -4194.96),
        uma_WorkOrder=2168.68,
    )
    assert isinstance(var_23, python_code_.uma_WorkOrder)
    var_24 = "4_[d\nK48B}HRh"
    var_25 = python_code_.uma_Practice(
        activityReference=var_7, group2=var_1, contentReference=var_24
    )
    assert isinstance(var_25, python_code_.uma_Practice)


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = "|Ki>1*wp^k3*>mD'"
    var_1 = python_code_.uma_RoleDescriptor(role=var_0, responsibleFor=set())
    assert isinstance(var_1, python_code_.uma_RoleDescriptor)
    var_3 = "uma_MethodConfiguration"
    var_4 = " z9]Lm[ 4{w* l4ra"
    var_5 = "uma_Artifact.localReplacement.uma_ProcessComponentInterface45"
    var_6 = abs
    var_7 = "5\x0c@<k))P(P\n_"
    var_8 = "V\r.ktL\\FU47A8"
    var_9 = python_code_.uma_Process(
        defaultContext=set(),
        includesPattern=var_6,
        validContext=var_7,
        diagramURI=var_8,
    )
    assert isinstance(var_9, python_code_.uma_Process)
    python_code_.uma_ProcessComponent(
        copyright=var_3,
        authors="@\x0c?E.?#z<\\au>d",
        changeDate=set(),
        changeDescription=var_4,
        version=var_5,
        uma_ProcessComponent41=var_9,
    )


def test_2():
    var_0 = python_code_.uma_Discipline(
        group2=None,
        task=True,
        referenceWorkflow=1,
        uma_Discipline="uma_DescribableElement",
    )
    assert isinstance(var_0, python_code_.uma_Discipline)
    var_1 = "oZDC<)"
    var_2 = lambda *args, **kwargs: 1
    var_3 = python_code_.uma_Domain(
        group2=var_1,
        workProduct=var_2,
        uma_Domain21="_uma_ContentElement__uma_ContentElement:uma_MethodLibrary27",
    )
    assert isinstance(var_3, python_code_.uma_Domain)
    var_4 = python_code_.uma_ProcessPackage(group2=None)
    assert isinstance(var_4, python_code_.uma_ProcessPackage)
    var_5 = "YM3Zy<Y\x0b^Fzl1w\ty.n\n"
    var_6 = "_uma_Section__uma_Section47_uma_ContentPackage__uma_ContentPackageuma_MethodPlugin35_uma_Domain__uma_Domain21"
    var_7 = "uma_WorkOrder.uma_Section47._uma_MethodPlugin__uma_MethodPlugin35.uma_MethodPlugin"
    var_8 = python_code_.uma_ProcessComponent(
        copyright=var_5,
        authors=var_6,
        changeDate=var_7,
        changeDescription=var_1,
        version=var_1,
    )
    assert isinstance(var_8, python_code_.uma_ProcessComponent)
    var_9 = python_code_.WorkBreakdownElement()
    var_10 = "ev"
    var_11 = "hS]VlzEARb-OA=T++J7"
    var_12 = "`XR"
    var_13 = python_code_.uma_TaskDescriptor(
        assistedBy=var_10,
        task=var_11,
        group3=None,
        performedPrimarilyBy=-1065.48,
        additionallyPerformedBy=var_2,
        externalInput=var_9,
        mandatoryInput=var_12,
        optionalInput=var_7,
        output=var_8,
        isSynchronizedWithSource=var_11,
        uma_TaskDescriptor51=(1070.14, 2013.43),
    )
    assert isinstance(var_13, python_code_.uma_TaskDescriptor)
    var_14 = python_code_.uma_DescribableElement(
        fulfill=var_11,
        isAbstract=("_uma_WorkBreakdownElement__uma_WorkBreakdownElement",),
        nodeicon=var_3,
        shapeicon=var_1,
    )
    assert isinstance(var_14, python_code_.uma_DescribableElement)
    var_17 = '$\tfQ,f\r"Azu'
    var_18 = ""
    var_19 = python_code_.uma_WorkProductDescription(
        impactOfNotHaving=var_17, purpose=var_18, reasonsForNotNeeding=var_11
    )
    assert isinstance(var_19, python_code_.uma_WorkProductDescription)
    var_21 = python_code_.uma_ContentCategoryPackage(group2=[True, 1, "=O"])
    assert isinstance(var_21, python_code_.uma_ContentCategoryPackage)
    var_22 = python_code_.uma_CustomCategory(
        group2=-3290,
        categorizedElement=b"P\xeb\xbf\xb2\xefZi\nq\xc3n@\xcd\xed\xd3",
        subCategory=var_18,
    )
    assert isinstance(var_22, python_code_.uma_CustomCategory)


def test_3():
    var_0 = python_code_.uma_Tool
    var_1 = python_code_.uma_TeamProfile(
        group2={-797.95},
        role={"vJUxEb~<6cwNg q": -2163.09},
        superTeam=None,
        subTeam=var_0,
    )
    assert isinstance(var_1, python_code_.uma_TeamProfile)
    var_2 = "lC-3&U"
    var_3 = "_@63EVI$zv"
    var_4 = python_code_.uma_Section(
        sectionName=var_1,
        predecessor=var_2,
        description=None,
        variabilityBasedOnElement=var_0,
        variabilityType=var_3,
    )
    assert isinstance(var_4, python_code_.uma_Section)
    var_5 = "7F|lVOtAd"
    var_6 = python_code_.uma_MethodPackage(
        group1=var_5, reusedPackage=265, global_=var_5, uma_MethodPackage32=var_3
    )
    assert isinstance(var_6, python_code_.uma_MethodPackage)
    var_7 = "lj"
    var_8 = python_code_.uma_Domain(group2=var_7, workProduct=var_5)
    assert isinstance(var_8, python_code_.uma_Domain)
    var_9 = python_code_.uma_Domain(group2=var_7, workProduct=var_0, uma_Domain=var_8)
    assert isinstance(var_9, python_code_.uma_Domain)
    var_10 = "\tL7t&:K-j?]4l:dD/("
    var_11 = "_uma_MethodElementProperty__uma_MethodElementProperty._uma_Section__uma_Section49.uma_DocumentRoot18._uma_MethodLibrary__uma_MethodLibrary27"
    var_12 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface45._uma_MethodElement__uma_MethodElement.uma_Section52"
    var_13 = "_uma_Discipline__uma_Discipline9"
    var_14 = "_uma_Work`ProductDescriptor__uma_WorkProductDescriptor"
    var_15 = python_code_.uma_MethodConfiguration(
        defaultView=var_11,
        baseConfiguration=var_12,
        methodPluginSelection=complex(1186.16, -1033.6198),
        methodPackageSelection=var_13,
        processView=var_9,
        subtractedCategory=var_0,
        addedCategory=var_14,
    )
    assert isinstance(var_15, python_code_.uma_MethodConfiguration)
    var_16 = {var_15, var_15, var_15}
    var_17 = python_code_.uma_DocumentRoot(
        mixed="_uma_ProcessComponent__uma_ProcessComponent",
        uma_DocumentRoot20={"h<s1q\\9zbe`{(W"},
        uma_DocumentRoot=var_16,
        uma_DocumentRoot13=var_16,
        uma_DocumentRoot16=set(),
    )
    assert isinstance(var_17, python_code_.uma_DocumentRoot)
    var_21 = python_code_.uma_RoleDescriptor(role=var_10, responsibleFor=(-2815,))
    assert isinstance(var_21, python_code_.uma_RoleDescriptor)


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.uma_Tool(group2={-1771.85, 220, 105}, toolMentor=["y"])
    assert isinstance(var_0, python_code_.uma_Tool)
    var_1 = python_code_.MethodPackage()
    var_3 = set()
    var_4 = python_code_.uma_ProcessComponentInterface(
        group2=var_1, uma_ProcessComponentInterface45=var_3
    )
    assert isinstance(var_4, python_code_.uma_ProcessComponentInterface)
    var_5 = "_uma_DocumentRoot__uma_DocumentRoot"
    var_6 = "_uma_DocumentRoot__uma_DocumentRoot16uma_Practice37"
    var_7 = "PcpWht/^\\Gx~'\x0b&Mq"
    var_8 = "i\rr|["
    var_9 = python_code_.uma_BreakdownElement(
        planningData=var_1,
        presentedAfter=var_5,
        presentedBefore=[],
        prefix=var_5,
        superActivity=var_3,
        group1=complex(-5570.1, -247.3084263),
        checklist=var_6,
        concept=var_5,
        example=var_3,
        guideline=var_7,
        reusableAsset=var_6,
        supportingMaterial={-2097.27, False, False},
        whitepaper=var_7,
        hasMultipleOccurrences=var_6,
        isOptional=var_8,
        isPlanned=var_6,
    )
    assert isinstance(var_9, python_code_.uma_BreakdownElement)
    var_10 = python_code_.uma_DeliveryProcess(
        group4=var_5,
        communicationsMaterial=None,
        educationMaterial=complex(-397.76, -3455.324243),
    )
    assert isinstance(var_10, python_code_.uma_DeliveryProcess)
    var_11 = lambda *args, **kwargs: -876
    var_12 = python_code_.uma_MethodElement(
        suppressed=var_11,
        group=-947.41,
        briefDescription=set(),
        id={},
        orderingGuide=-325,
        presentationName=var_5,
    )
    assert isinstance(var_12, python_code_.uma_MethodElement)
    var_13 = python_code_.uma_Constraint(mainDescription=var_5, uma_Constraint=var_12)
    assert isinstance(var_13, python_code_.uma_Constraint)
    var_15 = "lB"
    var_16 = python_code_.uma_NamedElement(name=var_15)
    assert isinstance(var_16, python_code_.uma_NamedElement)
    var_18 = "_uma_MethodElementProperty__uma_MethodElementProperty"
    var_19 = python_code_.uma_WorkProductDescription(
        impactOfNotHaving=var_5, purpose=var_18, reasonsForNotNeeding={"": -5007}
    )
    assert isinstance(var_19, python_code_.uma_WorkProductDescription)
    var_21 = "extendsReplaces,uma_ProcessComponentInterface45"
    python_code_.uma_DocumentRoot(mixed=var_21, uma_DocumentRoot18=var_11)


def test_5():
    var_0 = "oI1jiqVri"
    var_1 = python_code_.uma_ApplicableMetaClassInfo(isPrimaryExtension=var_0)
    assert isinstance(var_1, python_code_.uma_ApplicableMetaClassInfo)
    var_3 = python_code_.uma_BreakdownElementDescription(usageGuidance=var_0)
    assert isinstance(var_3, python_code_.uma_BreakdownElementDescription)
    var_5 = python_code_.DescribableElement
    var_6 = python_code_.uma_CompositeRole(group2=var_5)
    assert isinstance(var_6, python_code_.uma_CompositeRole)
    var_9 = python_code_.uma_Milestone(requiredResult=var_5)
    assert isinstance(var_9, python_code_.uma_Milestone)
    var_10 = "?Dc"
    var_11 = python_code_.uma_Tool(group2=var_10, toolMentor=[])
    assert isinstance(var_11, python_code_.uma_Tool)
    var_12 = "_uma_Practice__uma_Practice _uma_ProcessComponentInterface__uma_ProcessComponentInterface43 uma_MethodPackage32"
    var_13 = "/k"
    var_14 = python_code_.uma_WorkBreakdownElement(
        group2=var_12, isEventDriven=var_10, isOngoing=var_9, isRepeatable=var_13
    )
    assert isinstance(var_14, python_code_.uma_WorkBreakdownElement)
    var_15 = python_code_.uma_ContentPackage(group2=None)
    assert isinstance(var_15, python_code_.uma_ContentPackage)
    var_19 = python_code_.uma_ArtifactDescription(
        briefOutline=var_13,
        representationOptions=var_10,
        representation=set(),
        notation=var_13,
    )
    assert isinstance(var_19, python_code_.uma_ArtifactDescription)
    var_23 = "uma_Section47"
    var_24 = "_uma_MethodPlugin__uma_MethodPlugin35.localContribution._uma_MethodPlugin__uma_MethodPlugin35.replaces"
    var_25 = python_code_.uma_ProcessDescription(scope=var_23, usageNotes=var_24)
    assert isinstance(var_25, python_code_.uma_ProcessDescription)
    var_26 = "@8!{]YP0Zpjy-1Rb-E|"
    var_27 = "_uma_MethodPlugin__uma_MethodPlugin28,_uma_MethodPlugin__uma_MethodPlugin,uma_DocumentRoot,_uma_WorkOrder__uma_WorkOrder"
    var_28 = python_code_.uma_Estimate(
        group2=var_26, estimationMetric=var_9, estimationConsiderations=var_27
    )
    assert isinstance(var_28, python_code_.uma_Estimate)


def test_6():
    var_0 = python_code_.uma_Tool(group2={-1771.85, 220, 105}, toolMentor=["y"])
    assert isinstance(var_0, python_code_.uma_Tool)
    var_1 = python_code_.MethodPackage()
    var_3 = set()
    var_4 = python_code_.uma_ProcessComponentInterface(
        group2=var_1, uma_ProcessComponentInterface45=var_3
    )
    assert isinstance(var_4, python_code_.uma_ProcessComponentInterface)
    var_5 = "_uma_DocumentRoot__uma_DocumentRoot"
    var_6 = "_uma_DocumentRoot__uma_DocumentRoot16uma_Practice37"
    var_7 = "PcpWht/^\\Gx~'\x0b&Mq"
    var_8 = "i\rr|["
    var_9 = python_code_.uma_BreakdownElement(
        planningData=var_1,
        presentedAfter=var_5,
        presentedBefore=[],
        prefix=var_5,
        superActivity=var_3,
        group1=complex(-5570.1, -247.3084263),
        checklist=var_6,
        concept=var_5,
        example=var_3,
        guideline=var_7,
        reusableAsset=var_6,
        supportingMaterial={-2097.27, False, False},
        whitepaper=var_7,
        hasMultipleOccurrences=var_6,
        isOptional=var_8,
        isPlanned=var_6,
    )
    assert isinstance(var_9, python_code_.uma_BreakdownElement)
    var_10 = python_code_.uma_DeliveryProcess(
        group4=var_5,
        communicationsMaterial=None,
        educationMaterial=complex(-397.76, -3455.324243),
    )
    assert isinstance(var_10, python_code_.uma_DeliveryProcess)


def test_7():
    var_0 = python_code_.BreakdownElementDescription()
    var_1 = "_uma_ProcessPackage__uma_ProcessPackage _uma_Discipline__uma_Discipline9"
    var_2 = "uma_Domain21"
    var_3 = python_code_.uma_Milestone
    var_4 = python_code_.uma_DeliveryProcessDescription(
        scale=var_1,
        projectCharacteristics="",
        riskLevel=var_2,
        estimatingTechnique=False,
        projectMemberExpertise=var_3,
        typeOfContract=var_2,
    )
    assert isinstance(var_4, python_code_.uma_DeliveryProcessDescription)
    var_5 = python_code_.uma_Discipline
    var_6 = python_code_.uma_BreakdownElementDescription(usageGuidance=var_5)
    assert isinstance(var_6, python_code_.uma_BreakdownElementDescription)
    var_7 = python_code_.uma_MethodPackage(
        group1=var_2, reusedPackage=var_5, global_=set()
    )
    assert isinstance(var_7, python_code_.uma_MethodPackage)
    var_8 = {var_7}
    var_9 = python_code_.uma_MethodPlugin(
        referencedMethodPlugin=var_1,
        supporting=var_0,
        userChangeable=var_1,
        uma_MethodPlugin35=var_8,
    )
    assert isinstance(var_9, python_code_.uma_MethodPlugin)
    var_11 = python_code_.uma_EstimatingMetric()
    var_12 = python_code_.uma_GuidanceDescription(attachment=var_5)
    assert isinstance(var_12, python_code_.uma_GuidanceDescription)
    var_15 = "7~[qdKw!U&@){UN;hob"
    var_16 = python_code_.uma_RoleSet(group2=var_15, role=var_15)
    assert isinstance(var_16, python_code_.uma_RoleSet)
    var_18 = "B/7K'=|[7RTS{"
    var_19 = python_code_.uma_ProcessComponentInterface(
        group2=var_18,
        uma_ProcessComponentInterface="uma_Artifact0_uma_MethodPlugin__uma_MethodPlugin28_uma_Constraint__uma_Constraint_uma_MethodElement__uma_MethodElement25",
    )
    assert isinstance(var_19, python_code_.uma_ProcessComponentInterface)
    var_25 = python_code_.uma_EStringToStringMapEntry()
    var_26 = "uma_Artifact0-_uma_Artifact__uma_Artifact"
    var_27 = python_code_.uma_DescriptorDescription(refinedDescription=var_26)
    assert isinstance(var_27, python_code_.uma_DescriptorDescription)
    var_28 = "contributes-_uma_Constraint__uma_Constraint-uma_MethodLibrary30"
    var_29 = python_code_.uma_MethodUnit(
        copyright=var_16,
        authors=(),
        changeDate=var_3,
        changeDescription=var_28,
        version=None,
    )
    assert isinstance(var_29, python_code_.uma_MethodUnit)
    var_32 = python_code_.uma_ContentPackage(group2=var_26)
    assert isinstance(var_32, python_code_.uma_ContentPackage)
    var_33 = python_code_.uma_ProcessPlanningTemplate
    var_34 = "dkFvVE[S0#80"
    var_35 = python_code_.uma_MethodUnit(
        copyright=-2381.6,
        authors=var_11,
        changeDate=var_33,
        changeDescription=var_18,
        version=var_34,
    )
    var_37 = python_code_.uma_RoleDescription(
        assignmentApproaches=[],
        skills=b"u\xc9\xd4\x92\xb3\xfed\xec\xaa\x13\n\xb0v\x15IZN",
        synonyms=var_15,
    )
    assert isinstance(var_37, python_code_.uma_RoleDescription)
    var_41 = "uma_Section49,_uma_MethodElement__uma_MethodElement,uma_DocumentRoot16,_uma_ContentElement__uma_ContentElement"
    var_42 = "uW-j5\nru "
    var_43 = python_code_.uma_Task(
        estimate={-3660.34, 3},
        precondition=var_33,
        postcondition=var_35,
        performedBy=var_9,
        group2=var_3,
        mandatoryInput=var_41,
        output=var_33,
        additionallyPerformedBy=complex(674.53, 6.0876),
        optionalInput=1254.21,
        estimationConsiderations=var_3,
        toolMentor=var_42,
    )
    assert isinstance(var_43, python_code_.uma_Task)
    var_44 = "OP"
    var_45 = python_code_.uma_ProcessDescription(scope=var_44, usageNotes=var_25)
    assert isinstance(var_45, python_code_.uma_ProcessDescription)


def test_8():
    var_0 = python_code_.uma_Tool
    var_1 = python_code_.uma_TeamProfile(
        group2={-797.95},
        role={"vJUxEb~<6cwNg q": -2163.09},
        superTeam=None,
        subTeam=var_0,
    )
    assert isinstance(var_1, python_code_.uma_TeamProfile)
    var_2 = "lC-\n3&U"
    var_3 = "_@63EVIzv"
    var_4 = python_code_.uma_Section(
        sectionName=var_1,
        predecessor=var_2,
        description=None,
        variabilityBasedOnElement=var_0,
        variabilityType=var_3,
    )
    assert isinstance(var_4, python_code_.uma_Section)
    var_5 = "7F|lVOtAd"
    var_6 = python_code_.uma_MethodPackage(
        group1=var_5, reusedPackage=265, global_=var_5, uma_MethodPackage32=var_3
    )
    assert isinstance(var_6, python_code_.uma_MethodPackage)
    var_7 = "lj"
    var_8 = python_code_.uma_Domain(group2=var_7, workProduct=var_5)
    assert isinstance(var_8, python_code_.uma_Domain)
    var_9 = python_code_.uma_Domain(group2=var_7, workProduct=var_0, uma_Domain=var_8)
    assert isinstance(var_9, python_code_.uma_Domain)
    var_11 = "_uma_MethodElementProperty__uma_MethodElementProperty._uma_Section__uma_Section49.uma_DocumentRoot18._uma_MethodLibrary__uma_MethodLibrary27"
    var_12 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface45._uma_MethodElement__uma_MethodElement.uma_Section52"
    var_13 = "_uma_Discipline__uma_Discipline9"
    var_14 = "_uma_WorkProductDescriptor__uma_WorkProductDescriptor"
    var_15 = python_code_.uma_MethodConfiguration(
        defaultView=var_11,
        baseConfiguration=var_12,
        methodPluginSelection=complex(1186.16, -1033.6198),
        methodPackageSelection=var_13,
        processView=var_9,
        subtractedCategory=var_0,
        addedCategory=var_14,
    )
    assert isinstance(var_15, python_code_.uma_MethodConfiguration)


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.uma_Whitepaper
    var_1 = python_code_.uma_ProcessPackage(group2=var_0)
    assert isinstance(var_1, python_code_.uma_ProcessPackage)
    var_2 = python_code_.ContentElement()
    var_3 = "g"
    var_4 = "?ck_/] ~H`f"
    var_5 = python_code_.uma_ContentElement(
        reusableAsset=var_0,
        group1=var_3,
        checklist=(-835.92,),
        concept=var_0,
        example=var_3,
        guideline=var_0,
        supportingMaterial=var_4,
        whitepaper="_uma_ProcessComponentInterface__uma_ProcessComponentInterface43:_uma_ProcessComponentInterface__uma_ProcessComponentInterface:_uma_ProcessPackage__uma_ProcessPackage:_uma_ContentCategoryPackage__uma_ContentCategoryPackage",
        variabilityBasedOnElement=var_4,
        variabilityType=var_3,
    )
    assert isinstance(var_5, python_code_.uma_ContentElement)
    var_6 = python_code_.Concept()
    var_8 = "uma_Practice"
    var_9 = python_code_.uma_RoleDescription(
        assignmentApproaches=var_4,
        skills=var_8,
        synonyms={"0p035I": True, "7": -475, "TdE/*F~$d": True},
    )
    assert isinstance(var_9, python_code_.uma_RoleDescription)
    var_10 = "Sf==_Rj\x0b(z`o\\q"
    var_11 = "uma_WorkBreakdownElement uma_CompositeRole _uma_DocumentRoot__uma_DocumentRoot16"
    var_12 = "hNpKl:*(frQ?,%( =X"
    python_code_.uma_ContentElement(
        reusableAsset=var_10,
        group1=var_2,
        checklist=var_1,
        concept=var_3,
        example=var_6,
        guideline=var_4,
        supportingMaterial=var_9,
        whitepaper=var_11,
        variabilityBasedOnElement=var_12,
        variabilityType=var_4,
        uma_ContentElement=var_4,
    )
    var_15 = "_uma_Role__uma_Role"
    var_16 = python_code_.uma_Deliverable(group3=var_0, deliveredWorkProduct=var_15)
    assert isinstance(var_16, python_code_.uma_Deliverable)
    var_17 = "uma_ProcessComponentuma_Discipline9_uma_CompositeRole__uma_CompositeRole_uma_DocumentRoot__uma_DocumentRoot"
    var_18 = python_code_.uma_TaskDescription(alternatives=var_0, purpose=var_17)
    assert isinstance(var_18, python_code_.uma_TaskDescription)
    var_21 = python_code_.uma_RoleSetGrouping(
        group2={"uma_MethodLibrary27finishToFinish": 198.24, '2EL=<"\r uhJ~A': 1986},
        roleSet=var_1,
    )
    assert isinstance(var_21, python_code_.uma_RoleSetGrouping)
    var_23 = "uma_ContentDescription8,uma_CompositeRole"
    var_24 = python_code_.uma_WorkBreakdownElement(
        group2=var_23, isEventDriven=var_0, isOngoing=var_23, isRepeatable=var_0
    )
    assert isinstance(var_24, python_code_.uma_WorkBreakdownElement)
    var_26 = python_code_.uma_Template()
    var_27 = "`-A^wi"
    var_28 = "<UHvCj\t}/f7-j$9"
    var_29 = python_code_.uma_PracticeDescription(
        additionalInfo=var_0,
        application=var_27,
        background=var_28,
        goals=4256,
        levelsOfAdoption=var_26,
        problem={"K|-i\tI/f^_AK176]=\n5": -1927.28},
    )
    assert isinstance(var_29, python_code_.uma_PracticeDescription)
    var_32 = "\x0bn|ZW&"
    python_code_.uma_TaskDescriptor(
        assistedBy=var_2,
        task=False,
        group3=False,
        performedPrimarilyBy=var_0,
        additionallyPerformedBy=var_32,
        externalInput=["Nt.lu/9l\x0b))C2N2E[r"],
        mandatoryInput=var_4,
        optionalInput=[],
        output=var_10,
        isSynchronizedWithSource=var_23,
        uma_TaskDescriptor=var_0,
        uma_TaskDescriptor51=var_0,
    )


def test_10():
    var_0 = "oI1jiqVi"
    var_1 = python_code_.uma_ApplicableMetaClassInfo(isPrimaryExtension=var_0)
    assert isinstance(var_1, python_code_.uma_ApplicableMetaClassInfo)
    var_3 = python_code_.uma_BreakdownElementDescription(
        usageGuidance="_uma_MethodPlugin__uma_MethodPlugin:uma_DocumentRoot18:_uma_Role__uma_Role"
    )
    assert isinstance(var_3, python_code_.uma_BreakdownElementDescription)
    var_4 = python_code_.Descriptor()
    var_5 = python_code_.DescribableElement
    var_6 = python_code_.uma_CompositeRole(group2=var_5)
    assert isinstance(var_6, python_code_.uma_CompositeRole)
    var_7 = "uma_ProcessElement-_uma_ProcessComponent__uma_ProcessComponent-uma_Discipline-uma_WorkProductDescriptor"
    var_8 = python_code_.uma_Task(
        estimate=var_0,
        precondition=complex(2279.93, 2918.13),
        postcondition=var_0,
        performedBy=var_4,
        group2=var_4,
        mandatoryInput=var_3,
        output=var_4,
        additionallyPerformedBy=var_0,
        optionalInput=var_5,
        estimationConsiderations=var_7,
        toolMentor=var_5,
    )
    assert isinstance(var_8, python_code_.uma_Task)
    var_9 = python_code_.uma_Milestone(requiredResult=var_5)
    assert isinstance(var_9, python_code_.uma_Milestone)
    var_10 = "?Dc"
    var_11 = python_code_.uma_Tool(group2=var_10, toolMentor=[])
    assert isinstance(var_11, python_code_.uma_Tool)
    var_12 = "_uma_Practice__uma_Practice _uma_ProcessComponentInterface__uma_ProcessComponentInterface43 uma_MethodPackage32"
    var_13 = "/k"
    var_14 = python_code_.uma_WorkBreakdownElement(
        group2=var_12, isEventDriven=var_10, isOngoing=var_9, isRepeatable=var_13
    )
    assert isinstance(var_14, python_code_.uma_WorkBreakdownElement)
    var_15 = python_code_.uma_ContentPackage(group2=None)
    assert isinstance(var_15, python_code_.uma_ContentPackage)
    var_16 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface43"
    var_17 = python_code_.uma_MethodPlugin(
        referencedMethodPlugin=var_5,
        supporting=var_12,
        userChangeable=var_16,
        uma_MethodPlugin=var_8,
    )
    assert isinstance(var_17, python_code_.uma_MethodPlugin)
    var_19 = python_code_.uma_ArtifactDescription(
        briefOutline=var_13,
        representationOptions=var_10,
        representation=set(),
        notation=var_13,
    )
    assert isinstance(var_19, python_code_.uma_ArtifactDescription)
    var_22 = python_code_.uma_ProcessPlanningTemplate(group4=var_13, baseProcess=var_12)
    assert isinstance(var_22, python_code_.uma_ProcessPlanningTemplate)
    var_23 = "uma_Section47"
    var_24 = "_uma_MethodPlugin__uma_MethodPlugin35.localContribution._uma_MethodPlugin__uma_MethodPlugin35.replaces"
    var_25 = python_code_.uma_ProcessDescription(scope=var_23, usageNotes=var_24)
    assert isinstance(var_25, python_code_.uma_ProcessDescription)


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = python_code_.uma_Tool
    var_1 = python_code_.uma_TeamProfile(
        group2={-797.95},
        role={"vJUxEb~<6cwNg q": -2163.09},
        superTeam=None,
        subTeam=var_0,
    )
    assert isinstance(var_1, python_code_.uma_TeamProfile)
    var_2 = "lC-3&U"
    var_3 = "_@63EVIzv"
    var_4 = python_code_.uma_Section(
        sectionName=var_1,
        predecessor=var_2,
        description=None,
        variabilityBasedOnElement=var_0,
        variabilityType=var_3,
    )
    assert isinstance(var_4, python_code_.uma_Section)
    var_5 = "7F|lVOtAd"
    var_6 = python_code_.uma_MethodPackage(
        group1=var_5, reusedPackage=265, global_=var_5, uma_MethodPackage32=var_3
    )
    assert isinstance(var_6, python_code_.uma_MethodPackage)
    var_7 = "lj"
    var_8 = python_code_.uma_Domain(group2=var_7, workProduct=var_5)
    assert isinstance(var_8, python_code_.uma_Domain)
    var_9 = python_code_.uma_Domain(group2=var_7, workProduct=var_0, uma_Domain=var_8)
    assert isinstance(var_9, python_code_.uma_Domain)
    var_10 = "\tL7t&:K-j?]4l:dD/("
    var_11 = "_uma_MethodElementProperty__uma_MethodElementProperty._uma_Section__uma_Section49.uma_DocumentRoot18._uma_MethodLibrary__uma_MethodLibrary27"
    var_12 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface45._uma_MethodElement__uma_MethodElement.uma_Section52"
    var_13 = "_uma_Discipline__uma_Discipline9"
    var_14 = "_uma_WorkProductDescriptor__uma_WorkProductDescriptor"
    var_15 = python_code_.uma_MethodConfiguration(
        defaultView=var_11,
        baseConfiguration=var_12,
        methodPluginSelection=complex(1186.16, -1033.6198),
        methodPackageSelection=var_13,
        processView=var_9,
        subtractedCategory=var_0,
        addedCategory=var_14,
    )
    assert isinstance(var_15, python_code_.uma_MethodConfiguration)
    var_16 = {var_15, var_15, var_15}
    var_17 = python_code_.uma_DocumentRoot(mixed=var_10, uma_DocumentRoot16=var_16)
    assert isinstance(var_17, python_code_.uma_DocumentRoot)
    var_19 = python_code_.uma_ContentCategory()
    var_21 = python_code_.uma_RoleDescriptor(role=var_10, responsibleFor=(-2815,))
    assert isinstance(var_21, python_code_.uma_RoleDescriptor)
    var_23 = python_code_.uma_WorkOrder(
        value=var_19,
        id=-1663.88,
        linkType=var_0,
        properties=complex(1994.61559, -4194.96),
        uma_WorkOrder=2168.68,
    )
    assert isinstance(var_23, python_code_.uma_WorkOrder)
    var_24 = "4_[d\nK48B}HRh"
    var_25 = python_code_.uma_Practice(
        activityReference=var_7, group2=var_1, contentReference=var_24
    )
    assert isinstance(var_25, python_code_.uma_Practice)
    python_code_.uma_MethodLibrary(
        tool=var_2, uma_MethodLibrary=var_15, uma_MethodLibrary27=1386
    )


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.uma_Tool
    var_1 = python_code_.uma_TeamProfile(
        group2={-797.95},
        role={"vJUxEb~<6cwNg q": -2163.09},
        superTeam=None,
        subTeam=var_0,
    )
    assert isinstance(var_1, python_code_.uma_TeamProfile)
    var_2 = "lC-3&tU"
    var_3 = "_@63EVI$zv"
    var_4 = python_code_.uma_Section(
        sectionName=var_1,
        predecessor=var_2,
        description=None,
        variabilityBasedOnElement=var_0,
        variabilityType=var_3,
    )
    assert isinstance(var_4, python_code_.uma_Section)
    var_5 = "7F|lVOtAd"
    var_6 = python_code_.uma_MethodPackage(
        group1=var_2, reusedPackage="{\nd&8\rA", global_=var_2, uma_MethodPackage=var_5
    )
    assert isinstance(var_6, python_code_.uma_MethodPackage)
    var_7 = "lj"
    var_8 = python_code_.uma_Domain(group2=var_7, workProduct=var_5)
    assert isinstance(var_8, python_code_.uma_Domain)
    var_9 = python_code_.uma_Domain(group2=var_7, workProduct=var_0, uma_Domain=var_8)
    assert isinstance(var_9, python_code_.uma_Domain)
    var_10 = "\tL7t&:K-j?]4l:dD/("
    var_11 = "_uma_MethodElementProperty__uma_MethodElementProperty._uma_Section__uma_Section49.uma_DocumentRoot18._uma_MethodLibrary__uma_MethodLibrary27"
    var_12 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface45._uma_MethodElement__uma_MethodElement.uma_Section52"
    var_13 = "_uma_Discipline__uma_Discipline9"
    var_14 = "_uma_WorkProductDescriptor__uma_WorkProductDescriptor"
    var_15 = python_code_.uma_MethodConfiguration(
        defaultView=var_11,
        baseConfiguration=var_12,
        methodPluginSelection=complex(1186.16, -1033.6198),
        methodPackageSelection=var_13,
        processView=var_9,
        subtractedCategory=var_0,
        addedCategory=var_14,
    )
    assert isinstance(var_15, python_code_.uma_MethodConfiguration)
    var_16 = {var_15, var_15, var_15}
    var_17 = python_code_.uma_DocumentRoot(
        mixed="_uma_ProcessComponent__uma_ProcessComponent",
        uma_DocumentRoot20={"h<s1q\\9zbe`{(W"},
        uma_DocumentRoot=var_16,
        uma_DocumentRoot13=var_16,
        uma_DocumentRoot16=set(),
    )
    assert isinstance(var_17, python_code_.uma_DocumentRoot)
    var_19 = python_code_.uma_ContentCategory()
    var_21 = python_code_.uma_RoleDescriptor(role=var_10, responsibleFor=(-2815,))
    assert isinstance(var_21, python_code_.uma_RoleDescriptor)
    var_23 = python_code_.uma_WorkOrder(
        value=var_19,
        id=-1663.88,
        linkType=var_0,
        properties=complex(1994.61559, -4194.96),
        uma_WorkOrder=2168.68,
    )
    assert isinstance(var_23, python_code_.uma_WorkOrder)
    var_24 = "4_[d\nK48B}HRh"
    var_25 = python_code_.uma_Practice(
        activityReference=var_7, group2=var_1, contentReference=var_24
    )
    assert isinstance(var_25, python_code_.uma_Practice)
    python_code_.uma_MethodLibrary(
        tool=var_2, uma_MethodLibrary=var_15, uma_MethodLibrary27=1386
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_0 = "c[7{"
    var_1 = set()
    var_2 = python_code_.uma_ContentDescription(
        mainDescription=set(),
        keyConsiderations=var_0,
        externalId=var_0,
        uma_ContentDescription=var_1,
    )
    assert isinstance(var_2, python_code_.uma_ContentDescription)
    python_code_.uma_CompositeRole(
        group2=var_0, uma_CompositeRole=complex(394.35, 956.62734)
    )


def test_14():
    var_3 = "uma_MethodConfiguation"
    var_21 = "lB"
    var_22 = python_code_.uma_NamedElement(name=var_21)
    assert isinstance(var_22, python_code_.uma_NamedElement)
    var_38 = "/k"
    var_39 = python_code_.uma_ContentPackage(group2=None)
    assert isinstance(var_39, python_code_.uma_ContentPackage)
    var_40 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface43"
    var_42 = python_code_.uma_ArtifactDescription(
        briefOutline=var_38,
        representationOptions=var_3,
        representation=set(),
        notation=var_38,
    )
    assert isinstance(var_42, python_code_.uma_ArtifactDescription)
    var_45 = python_code_.uma_ProcessPlanningTemplate(group4=var_38, baseProcess=var_40)
    assert isinstance(var_45, python_code_.uma_ProcessPlanningTemplate)
    var_46 = "uma_Section47"
    var_47 = "_uma_MethodPlugin__uma_MethodPlugin35.localContribution._uma_MethodPlugin__uma_MethodPlugin35.replaces"
    var_48 = python_code_.uma_ProcessDescription(scope=var_46, usageNotes=var_47)
    assert isinstance(var_48, python_code_.uma_ProcessDescription)


def test_15():
    var_0 = python_code_.uma_Milestone(requiredResult=())
    assert isinstance(var_0, python_code_.uma_Milestone)
    var_1 = python_code_.uma_MethodPackage(
        group1={1855.16, True},
        reusedPackage=var_0,
        global_="_uma_MethodPackage__uma_MethodPackage",
    )
    assert isinstance(var_1, python_code_.uma_MethodPackage)
    var_2 = python_code_.uma_ArtifactDescription
    var_3 = "bCKG^\x0cyxz"
    var_4 = python_code_.uma_WorkProductType(group2=var_2, workProduct=var_3)
    assert isinstance(var_4, python_code_.uma_WorkProductType)
    var_5 = python_code_.uma_ApplicableMetaClassInfo(
        isPrimaryExtension=b"\x9c\xe4\xed\x05o$\x13\xa2r\x1e\xc9\x90\xabt\xde\xf6\xe3l\x01"
    )
    assert isinstance(var_5, python_code_.uma_ApplicableMetaClassInfo)


def test_16():
    var_0 = "Rr$/i:kBNCD{y"
    var_1 = python_code_.uma_ProcessDescription(scope=var_0, usageNotes=var_0)
    assert isinstance(var_1, python_code_.uma_ProcessDescription)
    var_2 = "ykbl(p7>,@&UZ^T"
    var_3 = "/"
    var_4 = python_code_.uma_RoleSetGrouping
    var_5 = "uma_Section47"
    var_6 = python_code_.uma_MethodElement(
        suppressed=var_3,
        group=[],
        briefDescription=var_4,
        id=var_4,
        orderingGuide=var_5,
        presentationName=var_2,
    )
    assert isinstance(var_6, python_code_.uma_MethodElement)
    var_7 = python_code_.uma_Constraint(mainDescription=var_2, uma_Constraint=var_6)
    assert isinstance(var_7, python_code_.uma_Constraint)
    var_8 = python_code_.uma_ActivityDescription(
        alternatives=-107.97, howToStaff={}, purpose=var_6
    )
    assert isinstance(var_8, python_code_.uma_ActivityDescription)
    var_9 = python_code_.uma_GuidanceDescription(attachment=var_2)
    assert isinstance(var_9, python_code_.uma_GuidanceDescription)
    var_10 = "n\n'.eT\n[+"
    var_11 = python_code_.uma_WorkProduct(
        group2=var_0,
        estimate=var_7,
        estimationConsiderations=var_7,
        report=set(),
        template=var_5,
        toolMentor=var_10,
    )
    assert isinstance(var_11, python_code_.uma_WorkProduct)
    var_13 = lambda *args, **kwargs: "KpD{i<Ev2\t14_#f=jn]"
    var_14 = "uma_MethodPackage"
    var_15 = python_code_.uma_Role(
        group2=b"\x9a\xcd\xa5H\xb4\xe9p_y\x13x\xf8l*\xfa\x99\x00", responsibleFor=var_14
    )
    assert isinstance(var_15, python_code_.uma_Role)
    var_16 = {var_15}
    var_17 = python_code_.uma_CompositeRole(group2=var_13, uma_CompositeRole=var_16)
    assert isinstance(var_17, python_code_.uma_CompositeRole)


def test_17():
    var_21 = "lB"
    var_22 = python_code_.uma_NamedElement(name=var_21)
    assert isinstance(var_22, python_code_.uma_NamedElement)
    var_29 = python_code_.uma_DescriptorDescription(
        refinedDescription=complex(-1438.8809, 58.025553)
    )
    assert isinstance(var_29, python_code_.uma_DescriptorDescription)
    var_35 = '\nLTY+S3M`+3q\\"A'
    var_36 = python_code_.uma_DeliverableDescription(
        externalDescription=var_35, packagingGuidance=var_29
    )
    assert isinstance(var_36, python_code_.uma_DeliverableDescription)


def test_18():
    var_0 = "oI1jiqVri"
    var_1 = python_code_.uma_ApplicableMetaClassInfo(isPrimaryExtension=var_0)
    assert isinstance(var_1, python_code_.uma_ApplicableMetaClassInfo)
    var_3 = python_code_.uma_BreakdownElementDescription(
        usageGuidance="_uma_MethodPlugin__uma_MethodPlugin:uma_DocumentRoot18:_uma_Role__uma_Role"
    )
    assert isinstance(var_3, python_code_.uma_BreakdownElementDescription)
    var_10 = "?Dc"
    var_11 = python_code_.uma_Tool(group2=var_10, toolMentor=[])
    assert isinstance(var_11, python_code_.uma_Tool)
    var_12 = "_uma_Practice__uma_Practice _uma_ProcessComponentInterface__uma_ProcessComponentInterface43 uma_MethodPackage32"
    var_13 = "/k"
    var_15 = python_code_.uma_ContentPackage(group2=None)
    assert isinstance(var_15, python_code_.uma_ContentPackage)
    var_19 = python_code_.uma_ArtifactDescription(
        briefOutline=var_13,
        representationOptions=var_10,
        representation=set(),
        notation=var_13,
    )
    assert isinstance(var_19, python_code_.uma_ArtifactDescription)
    var_22 = python_code_.uma_ProcessPlanningTemplate(group4=var_13, baseProcess=var_12)
    assert isinstance(var_22, python_code_.uma_ProcessPlanningTemplate)
    var_23 = "uma_Section47"
    var_24 = "_uma_MethodPlugin__uma_MethodPlugin35.localContribution._uma_MethodPlugin__uma_MethodPlugin35.replaces"
    var_25 = python_code_.uma_ProcessDescription(scope=var_23, usageNotes=var_24)
    assert isinstance(var_25, python_code_.uma_ProcessDescription)


def test_19():
    var_0 = python_code_.uma_Tool
    var_1 = python_code_.uma_TeamProfile(
        group2={-797.95},
        role={"vJUxEb~<6cwNg q": -2163.09},
        superTeam=None,
        subTeam=var_0,
    )
    assert isinstance(var_1, python_code_.uma_TeamProfile)
    var_2 = "lC-\n3&U"
    var_3 = "_@63EVIzv"
    var_4 = python_code_.uma_Section(
        sectionName=var_1,
        predecessor=var_2,
        description=None,
        variabilityBasedOnElement=var_0,
        variabilityType=var_3,
    )
    assert isinstance(var_4, python_code_.uma_Section)
    var_5 = "7F|lVOtAd"
    var_6 = python_code_.uma_MethodPackage(
        group1=var_5, reusedPackage=265, global_=var_5, uma_MethodPackage32=var_3
    )
    assert isinstance(var_6, python_code_.uma_MethodPackage)
    var_7 = "lj"
    var_8 = python_code_.uma_Domain(group2=var_7, workProduct=var_5)
    assert isinstance(var_8, python_code_.uma_Domain)
    var_9 = python_code_.uma_Domain(group2=var_7, workProduct=var_0, uma_Domain=var_8)
    assert isinstance(var_9, python_code_.uma_Domain)
    var_11 = "_uma_MethodElementProperty__uma_MethodElementProperty._uma_Section__uma_Section49.uma_DocumentRoot18._uma_MethodLibrary__uma_MethodLibrary27"
    var_12 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface45._uma_MethodElement__uma_MethodElement.uma_Section52"
    var_13 = "_uma_Discipline__uma_Discipline9"
    var_14 = "_uma_WorkProductDescriptor__uma_WorkProductDescriptor"
    var_15 = python_code_.uma_MethodConfiguration(
        defaultView=var_11,
        baseConfiguration=var_12,
        methodPluginSelection=complex(1186.16, -1033.6198),
        methodPackageSelection=var_13,
        processView=var_9,
        subtractedCategory=var_0,
        addedCategory=var_14,
    )
    assert isinstance(var_15, python_code_.uma_MethodConfiguration)
    var_44 = "V\r.ktL\\FU47A8"
    var_51 = python_code_.uma_CustomCategory(
        group2=var_44,
        categorizedElement=var_0,
        subCategory={"]": "uma_Role", "uma_WorkProductDescriptor": True, "": True},
    )
    assert isinstance(var_51, python_code_.uma_CustomCategory)


def test_20():
    var_0 = "oI1jiqVri"
    var_1 = python_code_.uma_ApplicableMetaClassInfo(isPrimaryExtension=var_0)
    assert isinstance(var_1, python_code_.uma_ApplicableMetaClassInfo)
    var_3 = python_code_.uma_BreakdownElementDescription(
        usageGuidance="_uma_MethodPlugin__uma_MethodPlugin:uma_DocumentRoot18:_uma_Role__uma_Role"
    )
    assert isinstance(var_3, python_code_.uma_BreakdownElementDescription)
    var_4 = python_code_.Descriptor()
    var_5 = python_code_.DescribableElement
    var_6 = python_code_.uma_CompositeRole(group2=var_5)
    assert isinstance(var_6, python_code_.uma_CompositeRole)
    var_7 = "uma_ProcessElement-_uma_ProcessComponent__uma_ProcessComponent-uma_Discipline-uma_WorkProductDescriptor"
    var_8 = python_code_.uma_Task(
        estimate=var_0,
        precondition=complex(2279.93, 2918.13),
        postcondition=var_0,
        performedBy=var_4,
        group2=var_4,
        mandatoryInput=var_3,
        output=var_4,
        additionallyPerformedBy=var_0,
        optionalInput=var_5,
        estimationConsiderations=var_7,
        toolMentor=var_5,
    )
    assert isinstance(var_8, python_code_.uma_Task)
    var_9 = python_code_.uma_Milestone(requiredResult=var_5)
    assert isinstance(var_9, python_code_.uma_Milestone)
    var_10 = "?Dc"
    var_11 = python_code_.uma_Tool(group2=var_10, toolMentor=[])
    assert isinstance(var_11, python_code_.uma_Tool)
    var_12 = "_uma_Practice__uma_Practice _uma_ProcessComponentInterface__uma_ProcessComponentInterface43 uma_MethodPackage32"
    var_13 = "/k"
    var_14 = python_code_.uma_WorkBreakdownElement(
        group2=var_12, isEventDriven=var_10, isOngoing=var_9, isRepeatable=var_13
    )
    assert isinstance(var_14, python_code_.uma_WorkBreakdownElement)
    var_15 = python_code_.uma_ContentPackage(group2=None)
    assert isinstance(var_15, python_code_.uma_ContentPackage)
    var_16 = "_uma_ProcessComponentInterface__uma_ProcessComponentInterface43"
    var_17 = python_code_.uma_MethodPlugin(
        referencedMethodPlugin=var_5,
        supporting=var_12,
        userChangeable=var_16,
        uma_MethodPlugin=var_8,
    )
    assert isinstance(var_17, python_code_.uma_MethodPlugin)
    var_19 = python_code_.uma_ArtifactDescription(
        briefOutline=var_13,
        representationOptions=var_10,
        representation=set(),
        notation=var_13,
    )
    assert isinstance(var_19, python_code_.uma_ArtifactDescription)
    var_22 = python_code_.uma_ProcessPlanningTemplate(group4=var_13, baseProcess=var_12)
    assert isinstance(var_22, python_code_.uma_ProcessPlanningTemplate)
    var_23 = "uma_Section47"
    var_24 = "_uma_MethodPlugin__uma_MethodPlugin35.localContribution._uma_MethodPlugin__uma_MethodPlugin35.replaces"
    var_25 = python_code_.uma_ProcessDescription(scope=var_23, usageNotes=var_24)
    assert isinstance(var_25, python_code_.uma_ProcessDescription)
    var_26 = "@8!{]YP0Zpjy-1Rb-E|"
    var_27 = "_uma_MethodPlugin__uma_MethodPlugin28,_uma_MethodPlugin__uma_MethodPlugin,uma_DocumentRoot,_uma_WorkOrder__uma_WorkOrder"
    var_28 = python_code_.uma_Estimate(
        group2=var_26, estimationMetric=var_9, estimationConsiderations=var_27
    )
    assert isinstance(var_28, python_code_.uma_Estimate)
    var_30 = python_code_.uma_MethodElementProperty(value=False)
    assert isinstance(var_30, python_code_.uma_MethodElementProperty)
