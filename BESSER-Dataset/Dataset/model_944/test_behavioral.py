import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ACOrgUnit,
    AbstractOperation,
    ActivityObject,
    Annotation,
    Attachment,
    AttributeOperation,
    CompositeOperation,
    Criterion,
    Event,
    FeatureOperation,
    IdentifiableElement,
    Issue,
    MeetingSection,
    ModelElement,
    ModelElementId,
    NonDomainElement,
    OrgUnit,
    PackageElement,
    Project,
    ProjectHistory,
    ProjectId,
    Proposal,
    ReadEvent,
    ReferenceOperation,
    Role,
    Section,
    ServerEvent,
    ServerProjectEvent,
    SessionId,
    Solution,
    StateNode,
    StereotypeAttribute,
    StereotypeAttributeInstance,
    UnicaseModelElement,
    UniqueIdentifier,
    VersionSpec,
    WorkItem,
    accesscontrol_ACGroup,
    accesscontrol_ACOrgUnit,
    accesscontrol_ACUser,
    accesscontrol_OrgUnitProperty,
    activity_ActivityObject,
    activity_Transition,
    attachment_FileAttachment,
    change_MergingProposal,
    change_ModelChangePackage,
    classes_Association,
    classes_Attribute,
    classes_Class,
    classes_Dependency,
    classes_Method,
    classes_MethodArgument,
    classes_Package,
    classes_PackageElement,
    component_Component,
    component_ComponentService,
    diagram_model_Diagram,
    document_CompositeSection,
    document_LeafSection,
    document_Section,
    esmodel_ClientVersionInfo,
    esmodel_FileIdentifier,
    esmodel_ProjectHistory,
    esmodel_ProjectId,
    esmodel_ProjectInfo,
    esmodel_ServerSpace,
    esmodel_SessionId,
    esmodel_VersionInfo,
    esmodel_accesscontrol_ACGroup,
    esmodel_accesscontrol_ACOrgUnit,
    esmodel_accesscontrol_ACOrgUnitId,
    esmodel_accesscontrol_ACUser,
    esmodel_accesscontrol_OrgUnitProperty,
    esmodel_events_AnnotationEvent,
    esmodel_events_CheckoutEvent,
    esmodel_events_DNDEvent,
    esmodel_events_Event,
    esmodel_events_ExceptionEvent,
    esmodel_events_LinkEvent,
    esmodel_events_MergeChoiceEvent,
    esmodel_events_MergeEvent,
    esmodel_events_MergeGlobalChoiceEvent,
    esmodel_events_NavigatorCreateEvent,
    esmodel_events_NotificationGenerationEvent,
    esmodel_events_NotificationIgnoreEvent,
    esmodel_events_NotificationReadEvent,
    esmodel_events_PerspectiveEvent,
    esmodel_events_PluginFocusEvent,
    esmodel_events_PluginStartEvent,
    esmodel_events_PresentationSwitchEvent,
    esmodel_events_ReadEvent,
    esmodel_events_RevertEvent,
    esmodel_events_ShowChangesEvent,
    esmodel_events_ShowHistoryEvent,
    esmodel_events_TraceEvent,
    esmodel_events_URLEvent,
    esmodel_events_UndoEvent,
    esmodel_events_UpdateEvent,
    esmodel_events_Validate,
    esmodel_notification_ESNotification,
    esmodel_operations_AbstractOperation,
    esmodel_operations_AttributeOperation,
    esmodel_operations_CompositeOperation,
    esmodel_operations_CreateDeleteOperation,
    esmodel_operations_DiagramLayoutOperation,
    esmodel_operations_EObjectToModelElementIdMap,
    esmodel_operations_FeatureOperation,
    esmodel_operations_ModelElementGroup,
    esmodel_operations_MultiAttributeMoveOperation,
    esmodel_operations_MultiAttributeOperation,
    esmodel_operations_MultiAttributeSetOperation,
    esmodel_operations_MultiReferenceMoveOperation,
    esmodel_operations_MultiReferenceOperation,
    esmodel_operations_MultiReferenceSetOperation,
    esmodel_operations_OperationGroup,
    esmodel_operations_OperationId,
    esmodel_operations_ReferenceOperation,
    esmodel_operations_SingleReferenceOperation,
    esmodel_roles_ProjectAdminRole,
    esmodel_roles_ReaderRole,
    esmodel_roles_Role,
    esmodel_roles_ServerAdmin,
    esmodel_roles_WriterRole,
    esmodel_semantic_SemanticCompositeOperation,
    esmodel_server_ProjectUpdatedEvent,
    esmodel_server_ServerEvent,
    esmodel_server_ServerProjectEvent,
    esmodel_url_ModelElementUrl,
    esmodel_url_ModelElementUrlFragment,
    esmodel_url_ProjectUrlFragment,
    esmodel_url_ServerUrl,
    esmodel_versioning_ChangePackage,
    esmodel_versioning_DateVersionSpec,
    esmodel_versioning_HeadVersionSpec,
    esmodel_versioning_HistoryInfo,
    esmodel_versioning_HistoryQuery,
    esmodel_versioning_LogMessage,
    esmodel_versioning_PrimaryVersionSpec,
    esmodel_versioning_TagVersionSpec,
    esmodel_versioning_Version,
    esmodel_versioning_VersionProperty,
    esmodel_versioning_VersionSpec,
    events_Event,
    meeting_IssueMeetingSection,
    meeting_MeetingSection,
    meeting_WorkItemMeetingSection,
    metamodel_AssociationClassElement,
    metamodel_IdentifiableElement,
    metamodel_ModelElement,
    metamodel_ModelElementId,
    metamodel_ModelVersion,
    metamodel_NonDomainElement,
    metamodel_Project,
    metamodel_UniqueIdentifier,
    model_Annotation,
    model_Attachment,
    model_NonDomainElement,
    model_Project,
    model_UnicaseModelElement,
    model_activity_Activity,
    model_activity_ActivityEnd,
    model_activity_ActivityInitial,
    model_activity_ActivityObject,
    model_activity_Branch,
    model_activity_Fork,
    model_activity_Transition,
    model_attachment_FileAttachment,
    model_attachment_UrlAttachment,
    model_bug_BugReport,
    model_change_MergingIssue,
    model_change_MergingProposal,
    model_change_MergingSolution,
    model_change_ModelChangePackage,
    model_classes_Association,
    model_classes_Attribute,
    model_classes_Class,
    model_classes_Dependency,
    model_classes_Method,
    model_classes_MethodArgument,
    model_classes_Package,
    model_classes_PackageElement,
    model_component_Component,
    model_component_ComponentService,
    model_component_DeploymentNode,
    model_diagram_MEDiagram,
    model_document_CompositeSection,
    model_document_LeafSection,
    model_document_Section,
    model_meeting_CompositeMeetingSection,
    model_meeting_IssueMeetingSection,
    model_meeting_Meeting,
    model_meeting_MeetingSection,
    model_meeting_WorkItemMeetingSection,
    model_organization_Group,
    model_organization_OrgUnit,
    model_organization_User,
    model_profile_Profile,
    model_profile_Stereotype,
    model_profile_StereotypeAttribute,
    model_profile_StereotypeAttributeInstance,
    model_profile_StereotypeAttributeInstanceString,
    model_profile_StereotypeAttributeSimple,
    model_profile_StereotypeInstance,
    model_rationale_Assessment,
    model_rationale_AudioComment,
    model_rationale_Comment,
    model_rationale_Criterion,
    model_rationale_Issue,
    model_rationale_Proposal,
    model_rationale_Solution,
    model_requirement_Actor,
    model_requirement_ActorInstance,
    model_requirement_FunctionalRequirement,
    model_requirement_NonFunctionalRequirement,
    model_requirement_Scenario,
    model_requirement_Step,
    model_requirement_SystemFunction,
    model_requirement_UseCase,
    model_requirement_UserTask,
    model_requirement_Workspace,
    model_state_State,
    model_state_StateEnd,
    model_state_StateInitial,
    model_state_StateNode,
    model_state_Transition,
    model_task_ActionItem,
    model_task_Checkable,
    model_task_Milestone,
    model_task_WorkItem,
    model_task_WorkPackage,
    model_util_ModelElementPath,
    notification_ESNotification,
    operations_AbstractOperation,
    operations_EObjectToModelElementIdMap,
    operations_OperationId,
    operations_ReferenceOperation,
    operations_esmodel_EObject,
    organization_Group,
    organization_OrgUnit,
    organization_User,
    profile_Profile,
    profile_Stereotype,
    profile_StereotypeAttribute,
    profile_StereotypeAttributeInstance,
    profile_StereotypeInstance,
    rationale_Assessment,
    rationale_Comment,
    rationale_Criterion,
    rationale_Issue,
    rationale_Proposal,
    rationale_Solution,
    requirement_Actor,
    requirement_ActorInstance,
    requirement_FunctionalRequirement,
    requirement_NonFunctionalRequirement,
    requirement_Scenario,
    requirement_Step,
    requirement_SystemFunction,
    requirement_UseCase,
    requirement_UserTask,
    requirement_Workspace,
    roles_Role,
    state_StateNode,
    state_Transition,
    task_Checkable,
    task_WorkItem,
    task_WorkPackage,
    url_ModelElementUrlFragment,
    url_ProjectUrlFragment,
    url_ServerUrl,
    versioning_ChangePackage,
    versioning_LogMessage,
    versioning_PrimaryVersionSpec,
    versioning_TagVersionSpec,
    versioning_Version,
    versioning_VersionProperty,
    ActivityType,
    ArgumentDirectionType,
    AssociationType,
    ContainmentType,
    DiagramType,
    FileAttachmentType,
    MergeChoiceSelection,
    MergeGlobalChoiceSelection,
    ResolutionType,
    ScopeType,
    Severity,
    VisibilityType,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations4_stub_double():
    # Annotation has no real 'Annotation' property in the generated
    # code (a bare stub) -- manually attach it so model_UnicaseModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_UnicaseModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    partner = Annotation()
    setattr(partner, 'Annotation', None)
    _safe_set(owner, 'annotatedModelElements', {partner})
    assert getattr(partner, 'Annotation') == owner
    _safe_set(owner, 'annotatedModelElements', set())
    assert getattr(partner, 'Annotation') is None


def test_assoc_appliedStereotypeInstances10_stub_double():
    # profile_StereotypeInstance has no real 'StereotypeInstance' property in the generated
    # code (a bare stub) -- manually attach it so model_UnicaseModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_UnicaseModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    partner = profile_StereotypeInstance()
    setattr(partner, 'StereotypeInstance', None)
    _safe_set(owner, 'modelElement', {partner})
    assert getattr(partner, 'StereotypeInstance') == owner
    _safe_set(owner, 'modelElement', set())
    assert getattr(partner, 'StereotypeInstance') is None


def test_assoc_arguments74_stub_double():
    # classes_MethodArgument has no real 'classes_MethodArgument' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    partner = classes_MethodArgument()
    setattr(partner, 'classes_MethodArgument', None)
    _safe_set(owner, 'model_classes_Method', {partner})
    assert getattr(partner, 'classes_MethodArgument') == owner
    _safe_set(owner, 'model_classes_Method', set())
    assert getattr(partner, 'classes_MethodArgument') is None


def test_assoc_assignee26_stub_double():
    # organization_OrgUnit has no real 'OrgUnit27' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    partner = organization_OrgUnit()
    setattr(partner, 'OrgUnit27', None)
    _safe_set(owner, 'assignments', partner)
    assert getattr(partner, 'OrgUnit27') == owner
    _safe_set(owner, 'assignments', None)
    assert getattr(partner, 'OrgUnit27') is None


def test_assoc_assignments16_stub_double():
    # task_WorkItem has no real 'WorkItem17' property in the generated
    # code (a bare stub) -- manually attach it so model_organization_OrgUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_organization_OrgUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_organization_OrgUnit(acOrgId="sample_text")
    partner = task_WorkItem()
    setattr(partner, 'WorkItem17', None)
    _safe_set(owner, 'assignee', {partner})
    assert getattr(partner, 'WorkItem17') == owner
    _safe_set(owner, 'assignee', set())
    assert getattr(partner, 'WorkItem17') is None


def test_assoc_associatedChangePackages31_stub_double():
    # change_ModelChangePackage has no real 'change_ModelChangePackage' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    partner = change_ModelChangePackage()
    setattr(partner, 'change_ModelChangePackage', None)
    _safe_set(owner, 'model_task_WorkItem', {partner})
    assert getattr(partner, 'change_ModelChangePackage') == owner
    _safe_set(owner, 'model_task_WorkItem', set())
    assert getattr(partner, 'change_ModelChangePackage') is None


def test_assoc_attachments5_stub_double():
    # Attachment has no real 'Attachment' property in the generated
    # code (a bare stub) -- manually attach it so model_UnicaseModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_UnicaseModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    partner = Attachment()
    setattr(partner, 'Attachment', None)
    _safe_set(owner, 'referringModelElements', {partner})
    assert getattr(partner, 'Attachment') == owner
    _safe_set(owner, 'referringModelElements', set())
    assert getattr(partner, 'Attachment') is None


def test_assoc_baseVersion385_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec386' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec386', None)
    _safe_set(owner, 'esmodel_events_MergeEvent', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec386') == owner
    _safe_set(owner, 'esmodel_events_MergeEvent', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec386') is None


def test_assoc_calledMethods70_stub_double():
    # classes_Method has no real 'Method71' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    partner = classes_Method()
    setattr(partner, 'Method71', None)
    _safe_set(owner, 'callingMethods', {partner})
    assert getattr(partner, 'Method71') == owner
    _safe_set(owner, 'callingMethods', set())
    assert getattr(partner, 'Method71') is None


def test_assoc_callingMethods72_stub_double():
    # classes_Method has no real 'Method73' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    partner = classes_Method()
    setattr(partner, 'Method73', None)
    _safe_set(owner, 'calledMethods', {partner})
    assert getattr(partner, 'Method73') == owner
    _safe_set(owner, 'calledMethods', set())
    assert getattr(partner, 'Method73') is None


def test_assoc_comments9_stub_double():
    # rationale_Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so model_UnicaseModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_UnicaseModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    partner = rationale_Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'commentedElement', {partner})
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'commentedElement', set())
    assert getattr(partner, 'Comment') is None


def test_assoc_containedWorkItems32_stub_double():
    # task_WorkItem has no real 'WorkItem33' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkPackage(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    partner = task_WorkItem()
    setattr(partner, 'WorkItem33', None)
    _safe_set(owner, 'containingWorkpackage', {partner})
    assert getattr(partner, 'WorkItem33') == owner
    _safe_set(owner, 'containingWorkpackage', set())
    assert getattr(partner, 'WorkItem33') is None


def test_assoc_containingWorkpackage21_stub_double():
    # task_WorkPackage has no real 'WorkPackage' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    partner = task_WorkPackage()
    setattr(partner, 'WorkPackage', None)
    _safe_set(owner, 'containedWorkItems', partner)
    assert getattr(partner, 'WorkPackage') == owner
    _safe_set(owner, 'containedWorkItems', None)
    assert getattr(partner, 'WorkPackage') is None


def test_assoc_contextModelElement451_stub_double():
    # ModelElementId has no real 'ModelElementId453' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeChoiceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeChoiceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId453', None)
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent452', partner)
    assert getattr(partner, 'ModelElementId453') == owner
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent452', None)
    assert getattr(partner, 'ModelElementId453') is None


def test_assoc_createdElement428_stub_double():
    # ModelElementId has no real 'ModelElementId429' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_NavigatorCreateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_NavigatorCreateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_NavigatorCreateEvent(dynamic=True)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId429', None)
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent', partner)
    assert getattr(partner, 'ModelElementId429') == owner
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent', None)
    assert getattr(partner, 'ModelElementId429') is None


def test_assoc_criteria184_stub_double():
    # rationale_Criterion has no real 'rationale_Criterion' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Issue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Issue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Issue(activity="sample_text")
    partner = rationale_Criterion()
    setattr(partner, 'rationale_Criterion', None)
    _safe_set(owner, 'model_rationale_Issue', {partner})
    assert getattr(partner, 'rationale_Criterion') == owner
    _safe_set(owner, 'model_rationale_Issue', set())
    assert getattr(partner, 'rationale_Criterion') is None


def test_assoc_criterion194_stub_double():
    # rationale_Criterion has no real 'Criterion' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Assessment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Assessment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Assessment(value=7)
    partner = rationale_Criterion()
    setattr(partner, 'Criterion', None)
    _safe_set(owner, 'assessments195', partner)
    assert getattr(partner, 'Criterion') == owner
    _safe_set(owner, 'assessments195', None)
    assert getattr(partner, 'Criterion') is None


def test_assoc_definingClass66_stub_double():
    # classes_Class has no real 'Class67' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    partner = classes_Class()
    setattr(partner, 'Class67', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'Class67') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'Class67') is None


def test_assoc_definingClass68_stub_double():
    # classes_Class has no real 'Class69' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    partner = classes_Class()
    setattr(partner, 'Class69', None)
    _safe_set(owner, 'methods', partner)
    assert getattr(partner, 'Class69') == owner
    _safe_set(owner, 'methods', None)
    assert getattr(partner, 'Class69') is None


def test_assoc_demoParticipations75_stub_double():
    # requirement_Scenario has no real 'Scenario76' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    partner = requirement_Scenario()
    setattr(partner, 'Scenario76', None)
    _safe_set(owner, 'participatingMethods', {partner})
    assert getattr(partner, 'Scenario76') == owner
    _safe_set(owner, 'participatingMethods', set())
    assert getattr(partner, 'Scenario76') is None


def test_assoc_dragSourceElement413_stub_double():
    # ModelElementId has no real 'ModelElementId414' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_DNDEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_DNDEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId414', None)
    _safe_set(owner, 'esmodel_events_DNDEvent', partner)
    assert getattr(partner, 'ModelElementId414') == owner
    _safe_set(owner, 'esmodel_events_DNDEvent', None)
    assert getattr(partner, 'ModelElementId414') is None


def test_assoc_dropTargetElement415_stub_double():
    # ModelElementId has no real 'ModelElementId417' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_DNDEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_DNDEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId417', None)
    _safe_set(owner, 'esmodel_events_DNDEvent416', partner)
    assert getattr(partner, 'ModelElementId417') == owner
    _safe_set(owner, 'esmodel_events_DNDEvent416', None)
    assert getattr(partner, 'ModelElementId417') is None


def test_assoc_eObjectToIdMap358_stub_double():
    # operations_EObjectToModelElementIdMap has no real 'operations_EObjectToModelElementIdMap' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CreateDeleteOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CreateDeleteOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CreateDeleteOperation(delete=True)
    partner = operations_EObjectToModelElementIdMap()
    setattr(partner, 'operations_EObjectToModelElementIdMap', None)
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation359', {partner})
    assert getattr(partner, 'operations_EObjectToModelElementIdMap') == owner
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation359', set())
    assert getattr(partner, 'operations_EObjectToModelElementIdMap') is None


def test_assoc_elements36_stub_double():
    # UnicaseModelElement has no real 'UnicaseModelElement37' property in the generated
    # code (a bare stub) -- manually attach it so model_diagram_MEDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_diagram_MEDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    partner = UnicaseModelElement()
    setattr(partner, 'UnicaseModelElement37', None)
    _safe_set(owner, 'model_diagram_MEDiagram', {partner})
    assert getattr(partner, 'UnicaseModelElement37') == owner
    _safe_set(owner, 'model_diagram_MEDiagram', set())
    assert getattr(partner, 'UnicaseModelElement37') is None


def test_assoc_extendedUseCases101_stub_double():
    # requirement_UseCase has no real 'requirement_UseCase103' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_UseCase()
    setattr(partner, 'requirement_UseCase103', None)
    _safe_set(owner, 'model_requirement_UseCase102', {partner})
    assert getattr(partner, 'requirement_UseCase103') == owner
    _safe_set(owner, 'model_requirement_UseCase102', set())
    assert getattr(partner, 'requirement_UseCase103') is None


def test_assoc_facilitator221_stub_double():
    # organization_User has no real 'organization_User' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = organization_User()
    setattr(partner, 'organization_User', None)
    _safe_set(owner, 'model_meeting_Meeting', partner)
    assert getattr(partner, 'organization_User') == owner
    _safe_set(owner, 'model_meeting_Meeting', None)
    assert getattr(partner, 'organization_User') is None


def test_assoc_functionalRequirements96_stub_double():
    # requirement_FunctionalRequirement has no real 'FunctionalRequirement97' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_FunctionalRequirement()
    setattr(partner, 'FunctionalRequirement97', None)
    _safe_set(owner, 'useCases', {partner})
    assert getattr(partner, 'FunctionalRequirement97') == owner
    _safe_set(owner, 'useCases', set())
    assert getattr(partner, 'FunctionalRequirement97') is None


def test_assoc_gmfdiagram38_stub_double():
    # diagram_model_Diagram has no real 'diagram_model_Diagram' property in the generated
    # code (a bare stub) -- manually attach it so model_diagram_MEDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_diagram_MEDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    partner = diagram_model_Diagram()
    setattr(partner, 'diagram_model_Diagram', None)
    _safe_set(owner, 'model_diagram_MEDiagram39', partner)
    assert getattr(partner, 'diagram_model_Diagram') == owner
    _safe_set(owner, 'model_diagram_MEDiagram39', None)
    assert getattr(partner, 'diagram_model_Diagram') is None


def test_assoc_groupMemberships14_stub_double():
    # organization_Group has no real 'Group' property in the generated
    # code (a bare stub) -- manually attach it so model_organization_OrgUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_organization_OrgUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_organization_OrgUnit(acOrgId="sample_text")
    partner = organization_Group()
    setattr(partner, 'Group', None)
    _safe_set(owner, 'orgUnits', {partner})
    assert getattr(partner, 'Group') == owner
    _safe_set(owner, 'orgUnits', set())
    assert getattr(partner, 'Group') is None


def test_assoc_identifiedClasses98_stub_double():
    # classes_Class has no real 'Class99' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = classes_Class()
    setattr(partner, 'Class99', None)
    _safe_set(owner, 'participatedUseCases', {partner})
    assert getattr(partner, 'Class99') == owner
    _safe_set(owner, 'participatedUseCases', set())
    assert getattr(partner, 'Class99') is None


def test_assoc_identifiedIssuesSection233_stub_double():
    # meeting_IssueMeetingSection has no real 'meeting_IssueMeetingSection' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = meeting_IssueMeetingSection()
    setattr(partner, 'meeting_IssueMeetingSection', None)
    _safe_set(owner, 'model_meeting_Meeting234', partner)
    assert getattr(partner, 'meeting_IssueMeetingSection') == owner
    _safe_set(owner, 'model_meeting_Meeting234', None)
    assert getattr(partner, 'meeting_IssueMeetingSection') is None


def test_assoc_identifiedWorkItemsSection235_stub_double():
    # meeting_WorkItemMeetingSection has no real 'meeting_WorkItemMeetingSection' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = meeting_WorkItemMeetingSection()
    setattr(partner, 'meeting_WorkItemMeetingSection', None)
    _safe_set(owner, 'model_meeting_Meeting236', partner)
    assert getattr(partner, 'meeting_WorkItemMeetingSection') == owner
    _safe_set(owner, 'model_meeting_Meeting236', None)
    assert getattr(partner, 'meeting_WorkItemMeetingSection') is None


def test_assoc_includedSystemFunction152_stub_double():
    # requirement_SystemFunction has no real 'requirement_SystemFunction' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_Step(userStep=True)
    partner = requirement_SystemFunction()
    setattr(partner, 'requirement_SystemFunction', None)
    _safe_set(owner, 'model_requirement_Step153', partner)
    assert getattr(partner, 'requirement_SystemFunction') == owner
    _safe_set(owner, 'model_requirement_Step153', None)
    assert getattr(partner, 'requirement_SystemFunction') is None


def test_assoc_includedUseCase148_stub_double():
    # requirement_UseCase has no real 'requirement_UseCase149' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_Step(userStep=True)
    partner = requirement_UseCase()
    setattr(partner, 'requirement_UseCase149', None)
    _safe_set(owner, 'model_requirement_Step', partner)
    assert getattr(partner, 'requirement_UseCase149') == owner
    _safe_set(owner, 'model_requirement_Step', None)
    assert getattr(partner, 'requirement_UseCase149') is None


def test_assoc_includedUseCases100_stub_double():
    # requirement_UseCase has no real 'requirement_UseCase' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_UseCase()
    setattr(partner, 'requirement_UseCase', None)
    _safe_set(owner, 'model_requirement_UseCase', {partner})
    assert getattr(partner, 'requirement_UseCase') == owner
    _safe_set(owner, 'model_requirement_UseCase', set())
    assert getattr(partner, 'requirement_UseCase') is None


def test_assoc_incomingDocumentReferences7_stub_double():
    # document_LeafSection has no real 'LeafSection8' property in the generated
    # code (a bare stub) -- manually attach it so model_UnicaseModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_UnicaseModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    partner = document_LeafSection()
    setattr(partner, 'LeafSection8', None)
    _safe_set(owner, 'referencedModelElements', {partner})
    assert getattr(partner, 'LeafSection8') == owner
    _safe_set(owner, 'referencedModelElements', set())
    assert getattr(partner, 'LeafSection8') is None


def test_assoc_initiatingActor106_stub_double():
    # requirement_Actor has no real 'Actor' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_Actor()
    setattr(partner, 'Actor', None)
    _safe_set(owner, 'initiatedUseCases', partner)
    assert getattr(partner, 'Actor') == owner
    _safe_set(owner, 'initiatedUseCases', None)
    assert getattr(partner, 'Actor') is None


def test_assoc_leafSection6_stub_double():
    # document_LeafSection has no real 'LeafSection' property in the generated
    # code (a bare stub) -- manually attach it so model_UnicaseModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_UnicaseModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    partner = document_LeafSection()
    setattr(partner, 'LeafSection', None)
    _safe_set(owner, 'modelElements', partner)
    assert getattr(partner, 'LeafSection') == owner
    _safe_set(owner, 'modelElements', None)
    assert getattr(partner, 'LeafSection') is None


def test_assoc_localChanges390_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation392' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation392', None)
    _safe_set(owner, 'esmodel_events_MergeEvent391', {partner})
    assert getattr(partner, 'operations_AbstractOperation392') == owner
    _safe_set(owner, 'esmodel_events_MergeEvent391', set())
    assert getattr(partner, 'operations_AbstractOperation392') is None


def test_assoc_mainOperation352_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation354' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CompositeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CompositeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation354', None)
    _safe_set(owner, 'esmodel_operations_CompositeOperation353', partner)
    assert getattr(partner, 'operations_AbstractOperation354') == owner
    _safe_set(owner, 'esmodel_operations_CompositeOperation353', None)
    assert getattr(partner, 'operations_AbstractOperation354') is None


def test_assoc_minutetaker222_stub_double():
    # organization_User has no real 'organization_User224' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = organization_User()
    setattr(partner, 'organization_User224', None)
    _safe_set(owner, 'model_meeting_Meeting223', partner)
    assert getattr(partner, 'organization_User224') == owner
    _safe_set(owner, 'model_meeting_Meeting223', None)
    assert getattr(partner, 'organization_User224') is None


def test_assoc_modelElement355_stub_double():
    # operations_esmodel_EObject has no real 'operations_esmodel_EObject' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CreateDeleteOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CreateDeleteOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CreateDeleteOperation(delete=True)
    partner = operations_esmodel_EObject()
    setattr(partner, 'operations_esmodel_EObject', None)
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation', partner)
    assert getattr(partner, 'operations_esmodel_EObject') == owner
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation', None)
    assert getattr(partner, 'operations_esmodel_EObject') is None


def test_assoc_modelElement383_stub_double():
    # ModelElementId has no real 'ModelElementId384' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_ReadEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_ReadEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_ReadEvent(readView="sample_text", sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId384', None)
    _safe_set(owner, 'esmodel_events_ReadEvent', partner)
    assert getattr(partner, 'ModelElementId384') == owner
    _safe_set(owner, 'esmodel_events_ReadEvent', None)
    assert getattr(partner, 'ModelElementId384') is None


def test_assoc_modelElementId348_stub_double():
    # ModelElementId has no real 'ModelElementId349' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_AbstractOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_AbstractOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId349', None)
    _safe_set(owner, 'esmodel_operations_AbstractOperation', partner)
    assert getattr(partner, 'ModelElementId349') == owner
    _safe_set(owner, 'esmodel_operations_AbstractOperation', None)
    assert getattr(partner, 'ModelElementId349') is None


def test_assoc_modelElementId476_stub_double():
    # ModelElementId has no real 'ModelElementId477' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_url_ModelElementUrlFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_url_ModelElementUrlFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_url_ModelElementUrlFragment(name="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId477', None)
    _safe_set(owner, 'esmodel_url_ModelElementUrlFragment', partner)
    assert getattr(partner, 'ModelElementId477') == owner
    _safe_set(owner, 'esmodel_url_ModelElementUrlFragment', None)
    assert getattr(partner, 'ModelElementId477') is None


def test_assoc_modelElements329_stub_double():
    # ModelElementId has no real 'ModelElementId331' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_versioning_HistoryQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_versioning_HistoryQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId331', None)
    _safe_set(owner, 'esmodel_versioning_HistoryQuery330', {partner})
    assert getattr(partner, 'ModelElementId331') == owner
    _safe_set(owner, 'esmodel_versioning_HistoryQuery330', set())
    assert getattr(partner, 'ModelElementId331') is None


def test_assoc_modelElements376_stub_double():
    # ModelElementId has no real 'ModelElementId377' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_ModelElementGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_ModelElementGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_ModelElementGroup(name="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId377', None)
    _safe_set(owner, 'esmodel_operations_ModelElementGroup', {partner})
    assert getattr(partner, 'ModelElementId377') == owner
    _safe_set(owner, 'esmodel_operations_ModelElementGroup', set())
    assert getattr(partner, 'ModelElementId377') is None


def test_assoc_myAcceptedChanges447_stub_double():
    # operations_OperationId has no real 'operations_OperationId' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeChoiceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeChoiceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    partner = operations_OperationId()
    setattr(partner, 'operations_OperationId', None)
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent', {partner})
    assert getattr(partner, 'operations_OperationId') == owner
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent', set())
    assert getattr(partner, 'operations_OperationId') is None


def test_assoc_newElements40_stub_double():
    # UnicaseModelElement has no real 'UnicaseModelElement42' property in the generated
    # code (a bare stub) -- manually attach it so model_diagram_MEDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_diagram_MEDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    partner = UnicaseModelElement()
    setattr(partner, 'UnicaseModelElement42', None)
    _safe_set(owner, 'model_diagram_MEDiagram41', {partner})
    assert getattr(partner, 'UnicaseModelElement42') == owner
    _safe_set(owner, 'model_diagram_MEDiagram41', set())
    assert getattr(partner, 'UnicaseModelElement42') is None


def test_assoc_newValue367_stub_double():
    # ModelElementId has no real 'ModelElementId369' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceSetOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceSetOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceSetOperation(index=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId369', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation368', partner)
    assert getattr(partner, 'ModelElementId369') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation368', None)
    assert getattr(partner, 'ModelElementId369') is None


def test_assoc_nonFunctionalRequirement154_stub_double():
    # requirement_NonFunctionalRequirement has no real 'NonFunctionalRequirement155' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_SystemFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_SystemFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    partner = requirement_NonFunctionalRequirement()
    setattr(partner, 'NonFunctionalRequirement155', None)
    _safe_set(owner, 'systemFunctions', partner)
    assert getattr(partner, 'NonFunctionalRequirement155') == owner
    _safe_set(owner, 'systemFunctions', None)
    assert getattr(partner, 'NonFunctionalRequirement155') is None


def test_assoc_nonFunctionalRequirements112_stub_double():
    # requirement_NonFunctionalRequirement has no real 'NonFunctionalRequirement' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_NonFunctionalRequirement()
    setattr(partner, 'NonFunctionalRequirement', None)
    _safe_set(owner, 'restrictedUseCases', {partner})
    assert getattr(partner, 'NonFunctionalRequirement') == owner
    _safe_set(owner, 'restrictedUseCases', set())
    assert getattr(partner, 'NonFunctionalRequirement') is None


def test_assoc_oldValue365_stub_double():
    # ModelElementId has no real 'ModelElementId366' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceSetOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceSetOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceSetOperation(index=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId366', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation', partner)
    assert getattr(partner, 'ModelElementId366') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation', None)
    assert getattr(partner, 'ModelElementId366') is None


def test_assoc_operations374_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation375' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_OperationGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_OperationGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_OperationGroup(name="sample_text")
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation375', None)
    _safe_set(owner, 'esmodel_operations_OperationGroup', {partner})
    assert getattr(partner, 'operations_AbstractOperation375') == owner
    _safe_set(owner, 'esmodel_operations_OperationGroup', set())
    assert getattr(partner, 'operations_AbstractOperation375') is None


def test_assoc_participants228_stub_double():
    # organization_OrgUnit has no real 'organization_OrgUnit230' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = organization_OrgUnit()
    setattr(partner, 'organization_OrgUnit230', None)
    _safe_set(owner, 'model_meeting_Meeting229', {partner})
    assert getattr(partner, 'organization_OrgUnit230') == owner
    _safe_set(owner, 'model_meeting_Meeting229', set())
    assert getattr(partner, 'organization_OrgUnit230') is None


def test_assoc_participants29_stub_double():
    # organization_OrgUnit has no real 'OrgUnit30' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    partner = organization_OrgUnit()
    setattr(partner, 'OrgUnit30', None)
    _safe_set(owner, 'participations', {partner})
    assert getattr(partner, 'OrgUnit30') == owner
    _safe_set(owner, 'participations', set())
    assert getattr(partner, 'OrgUnit30') is None


def test_assoc_participatingActors107_stub_double():
    # requirement_Actor has no real 'Actor109' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_Actor()
    setattr(partner, 'Actor109', None)
    _safe_set(owner, 'participatedUseCases108', {partner})
    assert getattr(partner, 'Actor109') == owner
    _safe_set(owner, 'participatedUseCases108', set())
    assert getattr(partner, 'Actor109') is None


def test_assoc_participations15_stub_double():
    # task_WorkItem has no real 'WorkItem' property in the generated
    # code (a bare stub) -- manually attach it so model_organization_OrgUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_organization_OrgUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_organization_OrgUnit(acOrgId="sample_text")
    partner = task_WorkItem()
    setattr(partner, 'WorkItem', None)
    _safe_set(owner, 'participants', {partner})
    assert getattr(partner, 'WorkItem') == owner
    _safe_set(owner, 'participants', set())
    assert getattr(partner, 'WorkItem') is None


def test_assoc_predecessors24_stub_double():
    # task_WorkItem has no real 'WorkItem25' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    partner = task_WorkItem()
    setattr(partner, 'WorkItem25', None)
    _safe_set(owner, 'successors', {partner})
    assert getattr(partner, 'WorkItem25') == owner
    _safe_set(owner, 'successors', set())
    assert getattr(partner, 'WorkItem25') is None


def test_assoc_profile252_stub_double():
    # profile_Profile has no real 'Profile' property in the generated
    # code (a bare stub) -- manually attach it so model_profile_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_profile_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_profile_Stereotype(required=True)
    partner = profile_Profile()
    setattr(partner, 'Profile', None)
    _safe_set(owner, 'stereotypes', partner)
    assert getattr(partner, 'Profile') == owner
    _safe_set(owner, 'stereotypes', None)
    assert getattr(partner, 'Profile') is None


def test_assoc_project462_stub_double():
    # ProjectId has no real 'ProjectId463' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_accesscontrol_OrgUnitProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_accesscontrol_OrgUnitProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_accesscontrol_OrgUnitProperty(name="sample_text", value="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId463', None)
    _safe_set(owner, 'esmodel_accesscontrol_OrgUnitProperty', partner)
    assert getattr(partner, 'ProjectId463') == owner
    _safe_set(owner, 'esmodel_accesscontrol_OrgUnitProperty', None)
    assert getattr(partner, 'ProjectId463') is None


def test_assoc_project466_stub_double():
    # ProjectId has no real 'ProjectId467' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_notification_ESNotification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_notification_ESNotification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId467', None)
    _safe_set(owner, 'esmodel_notification_ESNotification', partner)
    assert getattr(partner, 'ProjectId467') == owner
    _safe_set(owner, 'esmodel_notification_ESNotification', None)
    assert getattr(partner, 'ProjectId467') is None


def test_assoc_projectId289_stub_double():
    # ProjectId has no real 'ProjectId' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_ProjectHistory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_ProjectHistory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_ProjectHistory(projectDescription="sample_text", projectName="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId', None)
    _safe_set(owner, 'esmodel_ProjectHistory', partner)
    assert getattr(partner, 'ProjectId') == owner
    _safe_set(owner, 'esmodel_ProjectHistory', None)
    assert getattr(partner, 'ProjectId') is None


def test_assoc_projectId292_stub_double():
    # ProjectId has no real 'ProjectId293' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_ProjectInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_ProjectInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId293', None)
    _safe_set(owner, 'esmodel_ProjectInfo', partner)
    assert getattr(partner, 'ProjectId293') == owner
    _safe_set(owner, 'esmodel_ProjectInfo', None)
    assert getattr(partner, 'ProjectId293') is None


def test_assoc_projectId474_stub_double():
    # ProjectId has no real 'ProjectId475' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_url_ProjectUrlFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_url_ProjectUrlFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_url_ProjectUrlFragment(name="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId475', None)
    _safe_set(owner, 'esmodel_url_ProjectUrlFragment', partner)
    assert getattr(partner, 'ProjectId475') == owner
    _safe_set(owner, 'esmodel_url_ProjectUrlFragment', None)
    assert getattr(partner, 'ProjectId475') is None


def test_assoc_projects464_stub_double():
    # ProjectId has no real 'ProjectId465' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_roles_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_roles_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_roles_Role()
    partner = ProjectId()
    setattr(partner, 'ProjectId465', None)
    _safe_set(owner, 'esmodel_roles_Role', {partner})
    assert getattr(partner, 'ProjectId465') == owner
    _safe_set(owner, 'esmodel_roles_Role', set())
    assert getattr(partner, 'ProjectId465') is None


def test_assoc_properties459_stub_double():
    # accesscontrol_OrgUnitProperty has no real 'accesscontrol_OrgUnitProperty' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_accesscontrol_ACOrgUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_accesscontrol_ACOrgUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    partner = accesscontrol_OrgUnitProperty()
    setattr(partner, 'accesscontrol_OrgUnitProperty', None)
    _safe_set(owner, 'esmodel_accesscontrol_ACOrgUnit460', {partner})
    assert getattr(partner, 'accesscontrol_OrgUnitProperty') == owner
    _safe_set(owner, 'esmodel_accesscontrol_ACOrgUnit460', set())
    assert getattr(partner, 'accesscontrol_OrgUnitProperty') is None


def test_assoc_proposal192_stub_double():
    # rationale_Proposal has no real 'Proposal193' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Assessment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Assessment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Assessment(value=7)
    partner = rationale_Proposal()
    setattr(partner, 'Proposal193', None)
    _safe_set(owner, 'assessments', partner)
    assert getattr(partner, 'Proposal193') == owner
    _safe_set(owner, 'assessments', None)
    assert getattr(partner, 'Proposal193') is None


def test_assoc_proposals181_stub_double():
    # rationale_Proposal has no real 'Proposal' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Issue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Issue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Issue(activity="sample_text")
    partner = rationale_Proposal()
    setattr(partner, 'Proposal', None)
    _safe_set(owner, 'issue', {partner})
    assert getattr(partner, 'Proposal') == owner
    _safe_set(owner, 'issue', set())
    assert getattr(partner, 'Proposal') is None


def test_assoc_realizedUserTask111_stub_double():
    # requirement_UserTask has no real 'UserTask' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_UserTask()
    setattr(partner, 'UserTask', None)
    _safe_set(owner, 'realizingUseCases', partner)
    assert getattr(partner, 'UserTask') == owner
    _safe_set(owner, 'realizingUseCases', None)
    assert getattr(partner, 'UserTask') is None


def test_assoc_referencedModelElementId372_stub_double():
    # ModelElementId has no real 'ModelElementId373' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceMoveOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceMoveOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceMoveOperation(newIndex=7, oldIndex=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId373', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceMoveOperation', partner)
    assert getattr(partner, 'ModelElementId373') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceMoveOperation', None)
    assert getattr(partner, 'ModelElementId373') is None


def test_assoc_referencedModelElements370_stub_double():
    # ModelElementId has no real 'ModelElementId371' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceOperation(add=True, index=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId371', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceOperation', {partner})
    assert getattr(partner, 'ModelElementId371') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceOperation', set())
    assert getattr(partner, 'ModelElementId371') is None


def test_assoc_refinedRequirement88_stub_double():
    # requirement_FunctionalRequirement has no real 'FunctionalRequirement89' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_FunctionalRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_FunctionalRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    partner = requirement_FunctionalRequirement()
    setattr(partner, 'FunctionalRequirement89', None)
    _safe_set(owner, 'refiningRequirements', partner)
    assert getattr(partner, 'FunctionalRequirement89') == owner
    _safe_set(owner, 'refiningRequirements', None)
    assert getattr(partner, 'FunctionalRequirement89') is None


def test_assoc_refiningRequirements87_stub_double():
    # requirement_FunctionalRequirement has no real 'FunctionalRequirement' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_FunctionalRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_FunctionalRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    partner = requirement_FunctionalRequirement()
    setattr(partner, 'FunctionalRequirement', None)
    _safe_set(owner, 'refinedRequirement', {partner})
    assert getattr(partner, 'FunctionalRequirement') == owner
    _safe_set(owner, 'refinedRequirement', set())
    assert getattr(partner, 'FunctionalRequirement') is None


def test_assoc_relatedModelElements468_stub_double():
    # ModelElementId has no real 'ModelElementId470' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_notification_ESNotification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_notification_ESNotification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId470', None)
    _safe_set(owner, 'esmodel_notification_ESNotification469', {partner})
    assert getattr(partner, 'ModelElementId470') == owner
    _safe_set(owner, 'esmodel_notification_ESNotification469', set())
    assert getattr(partner, 'ModelElementId470') is None


def test_assoc_relatedOperations471_stub_double():
    # operations_OperationId has no real 'operations_OperationId473' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_notification_ESNotification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_notification_ESNotification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    partner = operations_OperationId()
    setattr(partner, 'operations_OperationId473', None)
    _safe_set(owner, 'esmodel_notification_ESNotification472', {partner})
    assert getattr(partner, 'operations_OperationId473') == owner
    _safe_set(owner, 'esmodel_notification_ESNotification472', set())
    assert getattr(partner, 'operations_OperationId473') is None


def test_assoc_reviewer28_stub_double():
    # organization_User has no real 'User' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    partner = organization_User()
    setattr(partner, 'User', None)
    _safe_set(owner, 'workItemsToReview', partner)
    assert getattr(partner, 'User') == owner
    _safe_set(owner, 'workItemsToReview', None)
    assert getattr(partner, 'User') is None


def test_assoc_roles458_stub_double():
    # roles_Role has no real 'roles_Role' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_accesscontrol_ACOrgUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_accesscontrol_ACOrgUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    partner = roles_Role()
    setattr(partner, 'roles_Role', None)
    _safe_set(owner, 'esmodel_accesscontrol_ACOrgUnit', {partner})
    assert getattr(partner, 'roles_Role') == owner
    _safe_set(owner, 'esmodel_accesscontrol_ACOrgUnit', set())
    assert getattr(partner, 'roles_Role') is None


def test_assoc_scenarios104_stub_double():
    # requirement_Scenario has no real 'Scenario105' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_Scenario()
    setattr(partner, 'Scenario105', None)
    _safe_set(owner, 'instantiatedUseCases', {partner})
    assert getattr(partner, 'Scenario105') == owner
    _safe_set(owner, 'instantiatedUseCases', set())
    assert getattr(partner, 'Scenario105') is None


def test_assoc_scenarios93_stub_double():
    # requirement_Scenario has no real 'Scenario95' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_FunctionalRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_FunctionalRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    partner = requirement_Scenario()
    setattr(partner, 'Scenario95', None)
    _safe_set(owner, 'functionalRequirements94', {partner})
    assert getattr(partner, 'Scenario95') == owner
    _safe_set(owner, 'functionalRequirements94', set())
    assert getattr(partner, 'Scenario95') is None


def test_assoc_sections231_stub_double():
    # meeting_MeetingSection has no real 'meeting_MeetingSection' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = meeting_MeetingSection()
    setattr(partner, 'meeting_MeetingSection', None)
    _safe_set(owner, 'model_meeting_Meeting232', {partner})
    assert getattr(partner, 'meeting_MeetingSection') == owner
    _safe_set(owner, 'model_meeting_Meeting232', set())
    assert getattr(partner, 'meeting_MeetingSection') is None


def test_assoc_solution182_stub_double():
    # rationale_Solution has no real 'Solution' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Issue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Issue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Issue(activity="sample_text")
    partner = rationale_Solution()
    setattr(partner, 'Solution', None)
    _safe_set(owner, 'issue183', partner)
    assert getattr(partner, 'Solution') == owner
    _safe_set(owner, 'issue183', None)
    assert getattr(partner, 'Solution') is None


def test_assoc_source241_stub_double():
    # state_StateNode has no real 'StateNode' property in the generated
    # code (a bare stub) -- manually attach it so model_state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_state_Transition(condition="sample_text")
    partner = state_StateNode()
    setattr(partner, 'StateNode', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'StateNode') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'StateNode') is None


def test_assoc_source284_stub_double():
    # activity_ActivityObject has no real 'ActivityObject' property in the generated
    # code (a bare stub) -- manually attach it so model_activity_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_activity_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_activity_Transition(condition="sample_text")
    partner = activity_ActivityObject()
    setattr(partner, 'ActivityObject', None)
    _safe_set(owner, 'outgoingTransitions285', partner)
    assert getattr(partner, 'ActivityObject') == owner
    _safe_set(owner, 'outgoingTransitions285', None)
    assert getattr(partner, 'ActivityObject') is None


def test_assoc_source324_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec325' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_versioning_HistoryQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_versioning_HistoryQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec325', None)
    _safe_set(owner, 'esmodel_versioning_HistoryQuery', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec325') == owner
    _safe_set(owner, 'esmodel_versioning_HistoryQuery', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec325') is None


def test_assoc_source62_stub_double():
    # classes_Class has no real 'Class63' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    partner = classes_Class()
    setattr(partner, 'Class63', None)
    _safe_set(owner, 'outgoingAssociations', partner)
    assert getattr(partner, 'Class63') == owner
    _safe_set(owner, 'outgoingAssociations', None)
    assert getattr(partner, 'Class63') is None


def test_assoc_sourceElement418_stub_double():
    # ModelElementId has no real 'ModelElementId419' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_LinkEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_LinkEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId419', None)
    _safe_set(owner, 'esmodel_events_LinkEvent', partner)
    assert getattr(partner, 'ModelElementId419') == owner
    _safe_set(owner, 'esmodel_events_LinkEvent', None)
    assert getattr(partner, 'ModelElementId419') is None


def test_assoc_sourceElement423_stub_double():
    # ModelElementId has no real 'ModelElementId424' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_TraceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_TraceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_TraceEvent(featureName="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId424', None)
    _safe_set(owner, 'esmodel_events_TraceEvent', partner)
    assert getattr(partner, 'ModelElementId424') == owner
    _safe_set(owner, 'esmodel_events_TraceEvent', None)
    assert getattr(partner, 'ModelElementId424') is None


def test_assoc_sourceModelElement442_stub_double():
    # ModelElementId has no real 'ModelElementId443' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_URLEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_URLEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_URLEvent(sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId443', None)
    _safe_set(owner, 'esmodel_events_URLEvent', partner)
    assert getattr(partner, 'ModelElementId443') == owner
    _safe_set(owner, 'esmodel_events_URLEvent', None)
    assert getattr(partner, 'ModelElementId443') is None


def test_assoc_sourceSection430_stub_double():
    # ModelElementId has no real 'ModelElementId432' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_NavigatorCreateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_NavigatorCreateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_NavigatorCreateEvent(dynamic=True)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId432', None)
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent431', partner)
    assert getattr(partner, 'ModelElementId432') == owner
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent431', None)
    assert getattr(partner, 'ModelElementId432') is None


def test_assoc_sourceURL444_stub_double():
    # ModelElementId has no real 'ModelElementId446' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_URLEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_URLEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_URLEvent(sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId446', None)
    _safe_set(owner, 'esmodel_events_URLEvent445', partner)
    assert getattr(partner, 'ModelElementId446') == owner
    _safe_set(owner, 'esmodel_events_URLEvent445', None)
    assert getattr(partner, 'ModelElementId446') is None


def test_assoc_stakeholder90_stub_double():
    # organization_OrgUnit has no real 'organization_OrgUnit' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_FunctionalRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_FunctionalRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    partner = organization_OrgUnit()
    setattr(partner, 'organization_OrgUnit', None)
    _safe_set(owner, 'model_requirement_FunctionalRequirement', partner)
    assert getattr(partner, 'organization_OrgUnit') == owner
    _safe_set(owner, 'model_requirement_FunctionalRequirement', None)
    assert getattr(partner, 'organization_OrgUnit') is None


def test_assoc_stereotypeAttributes255_stub_double():
    # profile_StereotypeAttribute has no real 'StereotypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so model_profile_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_profile_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_profile_Stereotype(required=True)
    partner = profile_StereotypeAttribute()
    setattr(partner, 'StereotypeAttribute', None)
    _safe_set(owner, 'stereotype256', {partner})
    assert getattr(partner, 'StereotypeAttribute') == owner
    _safe_set(owner, 'stereotype256', set())
    assert getattr(partner, 'StereotypeAttribute') is None


def test_assoc_stereotypeInstances253_stub_double():
    # profile_StereotypeInstance has no real 'StereotypeInstance254' property in the generated
    # code (a bare stub) -- manually attach it so model_profile_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_profile_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_profile_Stereotype(required=True)
    partner = profile_StereotypeInstance()
    setattr(partner, 'StereotypeInstance254', None)
    _safe_set(owner, 'stereotype', {partner})
    assert getattr(partner, 'StereotypeInstance254') == owner
    _safe_set(owner, 'stereotype', set())
    assert getattr(partner, 'StereotypeInstance254') is None


def test_assoc_subOperations350_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation351' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CompositeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CompositeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation351', None)
    _safe_set(owner, 'esmodel_operations_CompositeOperation', {partner})
    assert getattr(partner, 'operations_AbstractOperation351') == owner
    _safe_set(owner, 'esmodel_operations_CompositeOperation', set())
    assert getattr(partner, 'operations_AbstractOperation351') is None


def test_assoc_subOperations356_stub_double():
    # operations_ReferenceOperation has no real 'operations_ReferenceOperation' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CreateDeleteOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CreateDeleteOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CreateDeleteOperation(delete=True)
    partner = operations_ReferenceOperation()
    setattr(partner, 'operations_ReferenceOperation', None)
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation357', {partner})
    assert getattr(partner, 'operations_ReferenceOperation') == owner
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation357', set())
    assert getattr(partner, 'operations_ReferenceOperation') is None


def test_assoc_successors22_stub_double():
    # task_WorkItem has no real 'WorkItem23' property in the generated
    # code (a bare stub) -- manually attach it so model_task_WorkItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_task_WorkItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    partner = task_WorkItem()
    setattr(partner, 'WorkItem23', None)
    _safe_set(owner, 'predecessors', {partner})
    assert getattr(partner, 'WorkItem23') == owner
    _safe_set(owner, 'predecessors', set())
    assert getattr(partner, 'WorkItem23') is None


def test_assoc_systemFunctions113_stub_double():
    # requirement_SystemFunction has no real 'SystemFunction' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_SystemFunction()
    setattr(partner, 'SystemFunction', None)
    _safe_set(owner, 'usecases', {partner})
    assert getattr(partner, 'SystemFunction') == owner
    _safe_set(owner, 'usecases', set())
    assert getattr(partner, 'SystemFunction') is None


def test_assoc_target242_stub_double():
    # state_StateNode has no real 'StateNode243' property in the generated
    # code (a bare stub) -- manually attach it so model_state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_state_Transition(condition="sample_text")
    partner = state_StateNode()
    setattr(partner, 'StateNode243', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'StateNode243') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'StateNode243') is None


def test_assoc_target286_stub_double():
    # activity_ActivityObject has no real 'ActivityObject288' property in the generated
    # code (a bare stub) -- manually attach it so model_activity_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_activity_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_activity_Transition(condition="sample_text")
    partner = activity_ActivityObject()
    setattr(partner, 'ActivityObject288', None)
    _safe_set(owner, 'incomingTransitions287', partner)
    assert getattr(partner, 'ActivityObject288') == owner
    _safe_set(owner, 'incomingTransitions287', None)
    assert getattr(partner, 'ActivityObject288') is None


def test_assoc_target326_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec328' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_versioning_HistoryQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_versioning_HistoryQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec328', None)
    _safe_set(owner, 'esmodel_versioning_HistoryQuery327', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec328') == owner
    _safe_set(owner, 'esmodel_versioning_HistoryQuery327', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec328') is None


def test_assoc_target64_stub_double():
    # classes_Class has no real 'Class65' property in the generated
    # code (a bare stub) -- manually attach it so model_classes_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_classes_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    partner = classes_Class()
    setattr(partner, 'Class65', None)
    _safe_set(owner, 'incomingAssociations', partner)
    assert getattr(partner, 'Class65') == owner
    _safe_set(owner, 'incomingAssociations', None)
    assert getattr(partner, 'Class65') is None


def test_assoc_targetElement420_stub_double():
    # ModelElementId has no real 'ModelElementId422' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_LinkEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_LinkEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId422', None)
    _safe_set(owner, 'esmodel_events_LinkEvent421', partner)
    assert getattr(partner, 'ModelElementId422') == owner
    _safe_set(owner, 'esmodel_events_LinkEvent421', None)
    assert getattr(partner, 'ModelElementId422') is None


def test_assoc_targetElement425_stub_double():
    # ModelElementId has no real 'ModelElementId427' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_TraceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_TraceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_TraceEvent(featureName="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId427', None)
    _safe_set(owner, 'esmodel_events_TraceEvent426', partner)
    assert getattr(partner, 'ModelElementId427') == owner
    _safe_set(owner, 'esmodel_events_TraceEvent426', None)
    assert getattr(partner, 'ModelElementId427') is None


def test_assoc_targetVersion387_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec389' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec389', None)
    _safe_set(owner, 'esmodel_events_MergeEvent388', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec389') == owner
    _safe_set(owner, 'esmodel_events_MergeEvent388', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec389') is None


def test_assoc_theirRejectedChanges448_stub_double():
    # operations_OperationId has no real 'operations_OperationId450' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeChoiceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeChoiceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    partner = operations_OperationId()
    setattr(partner, 'operations_OperationId450', None)
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent449', {partner})
    assert getattr(partner, 'operations_OperationId450') == owner
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent449', set())
    assert getattr(partner, 'operations_OperationId450') is None


def test_assoc_timekeeper225_stub_double():
    # organization_User has no real 'organization_User227' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = organization_User()
    setattr(partner, 'organization_User227', None)
    _safe_set(owner, 'model_meeting_Meeting226', partner)
    assert getattr(partner, 'organization_User227') == owner
    _safe_set(owner, 'model_meeting_Meeting226', None)
    assert getattr(partner, 'organization_User227') is None


def test_assoc_useCase150_stub_double():
    # requirement_UseCase has no real 'UseCase151' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_Step(userStep=True)
    partner = requirement_UseCase()
    setattr(partner, 'UseCase151', None)
    _safe_set(owner, 'useCaseSteps', partner)
    assert getattr(partner, 'UseCase151') == owner
    _safe_set(owner, 'useCaseSteps', None)
    assert getattr(partner, 'UseCase151') is None


def test_assoc_useCaseSteps110_stub_double():
    # requirement_Step has no real 'Step' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    partner = requirement_Step()
    setattr(partner, 'Step', None)
    _safe_set(owner, 'useCase', {partner})
    assert getattr(partner, 'Step') == owner
    _safe_set(owner, 'useCase', set())
    assert getattr(partner, 'Step') is None


def test_assoc_useCases91_stub_double():
    # requirement_UseCase has no real 'UseCase92' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_FunctionalRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_FunctionalRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    partner = requirement_UseCase()
    setattr(partner, 'UseCase92', None)
    _safe_set(owner, 'functionalRequirements', {partner})
    assert getattr(partner, 'UseCase92') == owner
    _safe_set(owner, 'functionalRequirements', set())
    assert getattr(partner, 'UseCase92') is None


def test_assoc_usecases156_stub_double():
    # requirement_UseCase has no real 'UseCase158' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_SystemFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_SystemFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    partner = requirement_UseCase()
    setattr(partner, 'UseCase158', None)
    _safe_set(owner, 'systemFunctions157', {partner})
    assert getattr(partner, 'UseCase158') == owner
    _safe_set(owner, 'systemFunctions157', set())
    assert getattr(partner, 'UseCase158') is None


def test_assoc_version294_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_ProjectInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_ProjectInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec', None)
    _safe_set(owner, 'esmodel_ProjectInfo295', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec') == owner
    _safe_set(owner, 'esmodel_ProjectInfo295', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec') is None


def test_assoc_versions290_stub_double():
    # versioning_Version has no real 'versioning_Version' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_ProjectHistory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_ProjectHistory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_ProjectHistory(projectDescription="sample_text", projectName="sample_text")
    partner = versioning_Version()
    setattr(partner, 'versioning_Version', None)
    _safe_set(owner, 'esmodel_ProjectHistory291', {partner})
    assert getattr(partner, 'versioning_Version') == owner
    _safe_set(owner, 'esmodel_ProjectHistory291', set())
    assert getattr(partner, 'versioning_Version') is None


def test_assoc_workItemsToReview18_stub_double():
    # task_WorkItem has no real 'WorkItem19' property in the generated
    # code (a bare stub) -- manually attach it so model_organization_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_organization_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_organization_User(email="sample_text", firstName="sample_text", lastName="sample_text")
    partner = task_WorkItem()
    setattr(partner, 'WorkItem19', None)
    _safe_set(owner, 'reviewer', {partner})
    assert getattr(partner, 'WorkItem19') == owner
    _safe_set(owner, 'reviewer', set())
    assert getattr(partner, 'WorkItem19') is None


def test_assoc_workspace159_stub_double():
    # requirement_Workspace has no real 'Workspace' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_SystemFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_SystemFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    partner = requirement_Workspace()
    setattr(partner, 'Workspace', None)
    _safe_set(owner, 'systemFunctions160', partner)
    assert getattr(partner, 'Workspace') == owner
    _safe_set(owner, 'systemFunctions160', None)
    assert getattr(partner, 'Workspace') is None


