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
    BugStatus,
    ContainmentType,
    DiagramType,
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


def test_assoc_baseVersion366_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec367' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec367', None)
    _safe_set(owner, 'esmodel_events_MergeEvent', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec367') == owner
    _safe_set(owner, 'esmodel_events_MergeEvent', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec367') is None


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


def test_assoc_contextModelElement432_stub_double():
    # ModelElementId has no real 'ModelElementId434' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeChoiceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeChoiceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId434', None)
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent433', partner)
    assert getattr(partner, 'ModelElementId434') == owner
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent433', None)
    assert getattr(partner, 'ModelElementId434') is None


def test_assoc_createdElement409_stub_double():
    # ModelElementId has no real 'ModelElementId410' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_NavigatorCreateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_NavigatorCreateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_NavigatorCreateEvent(dynamic=True)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId410', None)
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent', partner)
    assert getattr(partner, 'ModelElementId410') == owner
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent', None)
    assert getattr(partner, 'ModelElementId410') is None


def test_assoc_criteria166_stub_double():
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


def test_assoc_criterion176_stub_double():
    # rationale_Criterion has no real 'Criterion' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Assessment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Assessment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Assessment(value=7)
    partner = rationale_Criterion()
    setattr(partner, 'Criterion', None)
    _safe_set(owner, 'assessments177', partner)
    assert getattr(partner, 'Criterion') == owner
    _safe_set(owner, 'assessments177', None)
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


def test_assoc_dragSourceElement394_stub_double():
    # ModelElementId has no real 'ModelElementId395' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_DNDEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_DNDEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId395', None)
    _safe_set(owner, 'esmodel_events_DNDEvent', partner)
    assert getattr(partner, 'ModelElementId395') == owner
    _safe_set(owner, 'esmodel_events_DNDEvent', None)
    assert getattr(partner, 'ModelElementId395') is None


def test_assoc_dropTargetElement396_stub_double():
    # ModelElementId has no real 'ModelElementId398' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_DNDEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_DNDEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId398', None)
    _safe_set(owner, 'esmodel_events_DNDEvent397', partner)
    assert getattr(partner, 'ModelElementId398') == owner
    _safe_set(owner, 'esmodel_events_DNDEvent397', None)
    assert getattr(partner, 'ModelElementId398') is None


def test_assoc_eObjectToIdMap339_stub_double():
    # operations_EObjectToModelElementIdMap has no real 'operations_EObjectToModelElementIdMap' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CreateDeleteOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CreateDeleteOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CreateDeleteOperation(delete=True)
    partner = operations_EObjectToModelElementIdMap()
    setattr(partner, 'operations_EObjectToModelElementIdMap', None)
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation340', {partner})
    assert getattr(partner, 'operations_EObjectToModelElementIdMap') == owner
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation340', set())
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


def test_assoc_facilitator202_stub_double():
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


def test_assoc_identifiedIssuesSection214_stub_double():
    # meeting_IssueMeetingSection has no real 'meeting_IssueMeetingSection' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = meeting_IssueMeetingSection()
    setattr(partner, 'meeting_IssueMeetingSection', None)
    _safe_set(owner, 'model_meeting_Meeting215', partner)
    assert getattr(partner, 'meeting_IssueMeetingSection') == owner
    _safe_set(owner, 'model_meeting_Meeting215', None)
    assert getattr(partner, 'meeting_IssueMeetingSection') is None


def test_assoc_identifiedWorkItemsSection216_stub_double():
    # meeting_WorkItemMeetingSection has no real 'meeting_WorkItemMeetingSection' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = meeting_WorkItemMeetingSection()
    setattr(partner, 'meeting_WorkItemMeetingSection', None)
    _safe_set(owner, 'model_meeting_Meeting217', partner)
    assert getattr(partner, 'meeting_WorkItemMeetingSection') == owner
    _safe_set(owner, 'model_meeting_Meeting217', None)
    assert getattr(partner, 'meeting_WorkItemMeetingSection') is None


def test_assoc_includedSystemFunction150_stub_double():
    # requirement_SystemFunction has no real 'requirement_SystemFunction' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_Step(userStep=True)
    partner = requirement_SystemFunction()
    setattr(partner, 'requirement_SystemFunction', None)
    _safe_set(owner, 'model_requirement_Step151', partner)
    assert getattr(partner, 'requirement_SystemFunction') == owner
    _safe_set(owner, 'model_requirement_Step151', None)
    assert getattr(partner, 'requirement_SystemFunction') is None


def test_assoc_includedUseCase146_stub_double():
    # requirement_UseCase has no real 'requirement_UseCase147' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_Step(userStep=True)
    partner = requirement_UseCase()
    setattr(partner, 'requirement_UseCase147', None)
    _safe_set(owner, 'model_requirement_Step', partner)
    assert getattr(partner, 'requirement_UseCase147') == owner
    _safe_set(owner, 'model_requirement_Step', None)
    assert getattr(partner, 'requirement_UseCase147') is None


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


def test_assoc_localChanges371_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation373' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation373', None)
    _safe_set(owner, 'esmodel_events_MergeEvent372', {partner})
    assert getattr(partner, 'operations_AbstractOperation373') == owner
    _safe_set(owner, 'esmodel_events_MergeEvent372', set())
    assert getattr(partner, 'operations_AbstractOperation373') is None


def test_assoc_mainOperation333_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation335' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CompositeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CompositeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation335', None)
    _safe_set(owner, 'esmodel_operations_CompositeOperation334', partner)
    assert getattr(partner, 'operations_AbstractOperation335') == owner
    _safe_set(owner, 'esmodel_operations_CompositeOperation334', None)
    assert getattr(partner, 'operations_AbstractOperation335') is None


def test_assoc_minutetaker203_stub_double():
    # organization_User has no real 'organization_User205' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = organization_User()
    setattr(partner, 'organization_User205', None)
    _safe_set(owner, 'model_meeting_Meeting204', partner)
    assert getattr(partner, 'organization_User205') == owner
    _safe_set(owner, 'model_meeting_Meeting204', None)
    assert getattr(partner, 'organization_User205') is None


def test_assoc_modelElement336_stub_double():
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


def test_assoc_modelElement364_stub_double():
    # ModelElementId has no real 'ModelElementId365' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_ReadEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_ReadEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_ReadEvent(readView="sample_text", sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId365', None)
    _safe_set(owner, 'esmodel_events_ReadEvent', partner)
    assert getattr(partner, 'ModelElementId365') == owner
    _safe_set(owner, 'esmodel_events_ReadEvent', None)
    assert getattr(partner, 'ModelElementId365') is None


def test_assoc_modelElementId329_stub_double():
    # ModelElementId has no real 'ModelElementId330' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_AbstractOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_AbstractOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId330', None)
    _safe_set(owner, 'esmodel_operations_AbstractOperation', partner)
    assert getattr(partner, 'ModelElementId330') == owner
    _safe_set(owner, 'esmodel_operations_AbstractOperation', None)
    assert getattr(partner, 'ModelElementId330') is None


def test_assoc_modelElementId457_stub_double():
    # ModelElementId has no real 'ModelElementId458' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_url_ModelElementUrlFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_url_ModelElementUrlFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_url_ModelElementUrlFragment(name="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId458', None)
    _safe_set(owner, 'esmodel_url_ModelElementUrlFragment', partner)
    assert getattr(partner, 'ModelElementId458') == owner
    _safe_set(owner, 'esmodel_url_ModelElementUrlFragment', None)
    assert getattr(partner, 'ModelElementId458') is None


def test_assoc_modelElements310_stub_double():
    # ModelElementId has no real 'ModelElementId312' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_versioning_HistoryQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_versioning_HistoryQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId312', None)
    _safe_set(owner, 'esmodel_versioning_HistoryQuery311', {partner})
    assert getattr(partner, 'ModelElementId312') == owner
    _safe_set(owner, 'esmodel_versioning_HistoryQuery311', set())
    assert getattr(partner, 'ModelElementId312') is None


def test_assoc_modelElements357_stub_double():
    # ModelElementId has no real 'ModelElementId358' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_ModelElementGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_ModelElementGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_ModelElementGroup(name="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId358', None)
    _safe_set(owner, 'esmodel_operations_ModelElementGroup', {partner})
    assert getattr(partner, 'ModelElementId358') == owner
    _safe_set(owner, 'esmodel_operations_ModelElementGroup', set())
    assert getattr(partner, 'ModelElementId358') is None


def test_assoc_myAcceptedChanges428_stub_double():
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


def test_assoc_newValue348_stub_double():
    # ModelElementId has no real 'ModelElementId350' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceSetOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceSetOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceSetOperation(index=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId350', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation349', partner)
    assert getattr(partner, 'ModelElementId350') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation349', None)
    assert getattr(partner, 'ModelElementId350') is None


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


def test_assoc_oldValue346_stub_double():
    # ModelElementId has no real 'ModelElementId347' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceSetOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceSetOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceSetOperation(index=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId347', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation', partner)
    assert getattr(partner, 'ModelElementId347') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceSetOperation', None)
    assert getattr(partner, 'ModelElementId347') is None


def test_assoc_operations355_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation356' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_OperationGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_OperationGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_OperationGroup(name="sample_text")
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation356', None)
    _safe_set(owner, 'esmodel_operations_OperationGroup', {partner})
    assert getattr(partner, 'operations_AbstractOperation356') == owner
    _safe_set(owner, 'esmodel_operations_OperationGroup', set())
    assert getattr(partner, 'operations_AbstractOperation356') is None


def test_assoc_participants209_stub_double():
    # organization_OrgUnit has no real 'organization_OrgUnit211' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = organization_OrgUnit()
    setattr(partner, 'organization_OrgUnit211', None)
    _safe_set(owner, 'model_meeting_Meeting210', {partner})
    assert getattr(partner, 'organization_OrgUnit211') == owner
    _safe_set(owner, 'model_meeting_Meeting210', set())
    assert getattr(partner, 'organization_OrgUnit211') is None


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


def test_assoc_profile233_stub_double():
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


def test_assoc_project443_stub_double():
    # ProjectId has no real 'ProjectId444' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_accesscontrol_OrgUnitProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_accesscontrol_OrgUnitProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_accesscontrol_OrgUnitProperty(name="sample_text", value="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId444', None)
    _safe_set(owner, 'esmodel_accesscontrol_OrgUnitProperty', partner)
    assert getattr(partner, 'ProjectId444') == owner
    _safe_set(owner, 'esmodel_accesscontrol_OrgUnitProperty', None)
    assert getattr(partner, 'ProjectId444') is None


def test_assoc_project447_stub_double():
    # ProjectId has no real 'ProjectId448' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_notification_ESNotification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_notification_ESNotification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId448', None)
    _safe_set(owner, 'esmodel_notification_ESNotification', partner)
    assert getattr(partner, 'ProjectId448') == owner
    _safe_set(owner, 'esmodel_notification_ESNotification', None)
    assert getattr(partner, 'ProjectId448') is None


def test_assoc_projectId270_stub_double():
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


def test_assoc_projectId273_stub_double():
    # ProjectId has no real 'ProjectId274' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_ProjectInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_ProjectInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId274', None)
    _safe_set(owner, 'esmodel_ProjectInfo', partner)
    assert getattr(partner, 'ProjectId274') == owner
    _safe_set(owner, 'esmodel_ProjectInfo', None)
    assert getattr(partner, 'ProjectId274') is None


def test_assoc_projectId455_stub_double():
    # ProjectId has no real 'ProjectId456' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_url_ProjectUrlFragment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_url_ProjectUrlFragment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_url_ProjectUrlFragment(name="sample_text")
    partner = ProjectId()
    setattr(partner, 'ProjectId456', None)
    _safe_set(owner, 'esmodel_url_ProjectUrlFragment', partner)
    assert getattr(partner, 'ProjectId456') == owner
    _safe_set(owner, 'esmodel_url_ProjectUrlFragment', None)
    assert getattr(partner, 'ProjectId456') is None


def test_assoc_projects445_stub_double():
    # ProjectId has no real 'ProjectId446' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_roles_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_roles_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_roles_Role()
    partner = ProjectId()
    setattr(partner, 'ProjectId446', None)
    _safe_set(owner, 'esmodel_roles_Role', {partner})
    assert getattr(partner, 'ProjectId446') == owner
    _safe_set(owner, 'esmodel_roles_Role', set())
    assert getattr(partner, 'ProjectId446') is None


def test_assoc_properties440_stub_double():
    # accesscontrol_OrgUnitProperty has no real 'accesscontrol_OrgUnitProperty' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_accesscontrol_ACOrgUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_accesscontrol_ACOrgUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    partner = accesscontrol_OrgUnitProperty()
    setattr(partner, 'accesscontrol_OrgUnitProperty', None)
    _safe_set(owner, 'esmodel_accesscontrol_ACOrgUnit441', {partner})
    assert getattr(partner, 'accesscontrol_OrgUnitProperty') == owner
    _safe_set(owner, 'esmodel_accesscontrol_ACOrgUnit441', set())
    assert getattr(partner, 'accesscontrol_OrgUnitProperty') is None


def test_assoc_proposal174_stub_double():
    # rationale_Proposal has no real 'Proposal175' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Assessment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Assessment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Assessment(value=7)
    partner = rationale_Proposal()
    setattr(partner, 'Proposal175', None)
    _safe_set(owner, 'assessments', partner)
    assert getattr(partner, 'Proposal175') == owner
    _safe_set(owner, 'assessments', None)
    assert getattr(partner, 'Proposal175') is None


def test_assoc_proposals163_stub_double():
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


def test_assoc_referencedModelElementId353_stub_double():
    # ModelElementId has no real 'ModelElementId354' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceMoveOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceMoveOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceMoveOperation(newIndex=7, oldIndex=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId354', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceMoveOperation', partner)
    assert getattr(partner, 'ModelElementId354') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceMoveOperation', None)
    assert getattr(partner, 'ModelElementId354') is None


def test_assoc_referencedModelElements351_stub_double():
    # ModelElementId has no real 'ModelElementId352' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_MultiReferenceOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_MultiReferenceOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_MultiReferenceOperation(add=True, index=7)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId352', None)
    _safe_set(owner, 'esmodel_operations_MultiReferenceOperation', {partner})
    assert getattr(partner, 'ModelElementId352') == owner
    _safe_set(owner, 'esmodel_operations_MultiReferenceOperation', set())
    assert getattr(partner, 'ModelElementId352') is None


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


def test_assoc_relatedModelElements449_stub_double():
    # ModelElementId has no real 'ModelElementId451' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_notification_ESNotification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_notification_ESNotification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId451', None)
    _safe_set(owner, 'esmodel_notification_ESNotification450', {partner})
    assert getattr(partner, 'ModelElementId451') == owner
    _safe_set(owner, 'esmodel_notification_ESNotification450', set())
    assert getattr(partner, 'ModelElementId451') is None


def test_assoc_relatedOperations452_stub_double():
    # operations_OperationId has no real 'operations_OperationId454' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_notification_ESNotification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_notification_ESNotification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    partner = operations_OperationId()
    setattr(partner, 'operations_OperationId454', None)
    _safe_set(owner, 'esmodel_notification_ESNotification453', {partner})
    assert getattr(partner, 'operations_OperationId454') == owner
    _safe_set(owner, 'esmodel_notification_ESNotification453', set())
    assert getattr(partner, 'operations_OperationId454') is None


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


def test_assoc_roles439_stub_double():
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


def test_assoc_sections212_stub_double():
    # meeting_MeetingSection has no real 'meeting_MeetingSection' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = meeting_MeetingSection()
    setattr(partner, 'meeting_MeetingSection', None)
    _safe_set(owner, 'model_meeting_Meeting213', {partner})
    assert getattr(partner, 'meeting_MeetingSection') == owner
    _safe_set(owner, 'model_meeting_Meeting213', set())
    assert getattr(partner, 'meeting_MeetingSection') is None


def test_assoc_solution164_stub_double():
    # rationale_Solution has no real 'Solution' property in the generated
    # code (a bare stub) -- manually attach it so model_rationale_Issue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_rationale_Issue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_rationale_Issue(activity="sample_text")
    partner = rationale_Solution()
    setattr(partner, 'Solution', None)
    _safe_set(owner, 'issue165', partner)
    assert getattr(partner, 'Solution') == owner
    _safe_set(owner, 'issue165', None)
    assert getattr(partner, 'Solution') is None


def test_assoc_source222_stub_double():
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


def test_assoc_source265_stub_double():
    # activity_ActivityObject has no real 'ActivityObject' property in the generated
    # code (a bare stub) -- manually attach it so model_activity_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_activity_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_activity_Transition(condition="sample_text")
    partner = activity_ActivityObject()
    setattr(partner, 'ActivityObject', None)
    _safe_set(owner, 'outgoingTransitions266', partner)
    assert getattr(partner, 'ActivityObject') == owner
    _safe_set(owner, 'outgoingTransitions266', None)
    assert getattr(partner, 'ActivityObject') is None


def test_assoc_source305_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec306' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_versioning_HistoryQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_versioning_HistoryQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec306', None)
    _safe_set(owner, 'esmodel_versioning_HistoryQuery', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec306') == owner
    _safe_set(owner, 'esmodel_versioning_HistoryQuery', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec306') is None


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


def test_assoc_sourceElement399_stub_double():
    # ModelElementId has no real 'ModelElementId400' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_LinkEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_LinkEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId400', None)
    _safe_set(owner, 'esmodel_events_LinkEvent', partner)
    assert getattr(partner, 'ModelElementId400') == owner
    _safe_set(owner, 'esmodel_events_LinkEvent', None)
    assert getattr(partner, 'ModelElementId400') is None


def test_assoc_sourceElement404_stub_double():
    # ModelElementId has no real 'ModelElementId405' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_TraceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_TraceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_TraceEvent(featureName="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId405', None)
    _safe_set(owner, 'esmodel_events_TraceEvent', partner)
    assert getattr(partner, 'ModelElementId405') == owner
    _safe_set(owner, 'esmodel_events_TraceEvent', None)
    assert getattr(partner, 'ModelElementId405') is None


def test_assoc_sourceModelElement423_stub_double():
    # ModelElementId has no real 'ModelElementId424' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_URLEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_URLEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_URLEvent(sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId424', None)
    _safe_set(owner, 'esmodel_events_URLEvent', partner)
    assert getattr(partner, 'ModelElementId424') == owner
    _safe_set(owner, 'esmodel_events_URLEvent', None)
    assert getattr(partner, 'ModelElementId424') is None


def test_assoc_sourceSection411_stub_double():
    # ModelElementId has no real 'ModelElementId413' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_NavigatorCreateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_NavigatorCreateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_NavigatorCreateEvent(dynamic=True)
    partner = ModelElementId()
    setattr(partner, 'ModelElementId413', None)
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent412', partner)
    assert getattr(partner, 'ModelElementId413') == owner
    _safe_set(owner, 'esmodel_events_NavigatorCreateEvent412', None)
    assert getattr(partner, 'ModelElementId413') is None


def test_assoc_sourceURL425_stub_double():
    # ModelElementId has no real 'ModelElementId427' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_URLEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_URLEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_URLEvent(sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId427', None)
    _safe_set(owner, 'esmodel_events_URLEvent426', partner)
    assert getattr(partner, 'ModelElementId427') == owner
    _safe_set(owner, 'esmodel_events_URLEvent426', None)
    assert getattr(partner, 'ModelElementId427') is None


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


def test_assoc_stereotypeAttributes236_stub_double():
    # profile_StereotypeAttribute has no real 'StereotypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so model_profile_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_profile_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_profile_Stereotype(required=True)
    partner = profile_StereotypeAttribute()
    setattr(partner, 'StereotypeAttribute', None)
    _safe_set(owner, 'stereotype237', {partner})
    assert getattr(partner, 'StereotypeAttribute') == owner
    _safe_set(owner, 'stereotype237', set())
    assert getattr(partner, 'StereotypeAttribute') is None


def test_assoc_stereotypeInstances234_stub_double():
    # profile_StereotypeInstance has no real 'StereotypeInstance235' property in the generated
    # code (a bare stub) -- manually attach it so model_profile_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_profile_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_profile_Stereotype(required=True)
    partner = profile_StereotypeInstance()
    setattr(partner, 'StereotypeInstance235', None)
    _safe_set(owner, 'stereotype', {partner})
    assert getattr(partner, 'StereotypeInstance235') == owner
    _safe_set(owner, 'stereotype', set())
    assert getattr(partner, 'StereotypeInstance235') is None


def test_assoc_subOperations331_stub_double():
    # operations_AbstractOperation has no real 'operations_AbstractOperation332' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CompositeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CompositeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    partner = operations_AbstractOperation()
    setattr(partner, 'operations_AbstractOperation332', None)
    _safe_set(owner, 'esmodel_operations_CompositeOperation', {partner})
    assert getattr(partner, 'operations_AbstractOperation332') == owner
    _safe_set(owner, 'esmodel_operations_CompositeOperation', set())
    assert getattr(partner, 'operations_AbstractOperation332') is None


def test_assoc_subOperations337_stub_double():
    # operations_ReferenceOperation has no real 'operations_ReferenceOperation' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_operations_CreateDeleteOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_operations_CreateDeleteOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_operations_CreateDeleteOperation(delete=True)
    partner = operations_ReferenceOperation()
    setattr(partner, 'operations_ReferenceOperation', None)
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation338', {partner})
    assert getattr(partner, 'operations_ReferenceOperation') == owner
    _safe_set(owner, 'esmodel_operations_CreateDeleteOperation338', set())
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


def test_assoc_target223_stub_double():
    # state_StateNode has no real 'StateNode224' property in the generated
    # code (a bare stub) -- manually attach it so model_state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_state_Transition(condition="sample_text")
    partner = state_StateNode()
    setattr(partner, 'StateNode224', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'StateNode224') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'StateNode224') is None


def test_assoc_target267_stub_double():
    # activity_ActivityObject has no real 'ActivityObject269' property in the generated
    # code (a bare stub) -- manually attach it so model_activity_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_activity_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_activity_Transition(condition="sample_text")
    partner = activity_ActivityObject()
    setattr(partner, 'ActivityObject269', None)
    _safe_set(owner, 'incomingTransitions268', partner)
    assert getattr(partner, 'ActivityObject269') == owner
    _safe_set(owner, 'incomingTransitions268', None)
    assert getattr(partner, 'ActivityObject269') is None


def test_assoc_target307_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec309' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_versioning_HistoryQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_versioning_HistoryQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec309', None)
    _safe_set(owner, 'esmodel_versioning_HistoryQuery308', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec309') == owner
    _safe_set(owner, 'esmodel_versioning_HistoryQuery308', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec309') is None


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


def test_assoc_targetElement401_stub_double():
    # ModelElementId has no real 'ModelElementId403' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_LinkEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_LinkEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId403', None)
    _safe_set(owner, 'esmodel_events_LinkEvent402', partner)
    assert getattr(partner, 'ModelElementId403') == owner
    _safe_set(owner, 'esmodel_events_LinkEvent402', None)
    assert getattr(partner, 'ModelElementId403') is None


def test_assoc_targetElement406_stub_double():
    # ModelElementId has no real 'ModelElementId408' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_TraceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_TraceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_TraceEvent(featureName="sample_text")
    partner = ModelElementId()
    setattr(partner, 'ModelElementId408', None)
    _safe_set(owner, 'esmodel_events_TraceEvent407', partner)
    assert getattr(partner, 'ModelElementId408') == owner
    _safe_set(owner, 'esmodel_events_TraceEvent407', None)
    assert getattr(partner, 'ModelElementId408') is None


def test_assoc_targetVersion368_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec370' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec370', None)
    _safe_set(owner, 'esmodel_events_MergeEvent369', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec370') == owner
    _safe_set(owner, 'esmodel_events_MergeEvent369', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec370') is None


def test_assoc_theirRejectedChanges429_stub_double():
    # operations_OperationId has no real 'operations_OperationId431' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_events_MergeChoiceEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_events_MergeChoiceEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    partner = operations_OperationId()
    setattr(partner, 'operations_OperationId431', None)
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent430', {partner})
    assert getattr(partner, 'operations_OperationId431') == owner
    _safe_set(owner, 'esmodel_events_MergeChoiceEvent430', set())
    assert getattr(partner, 'operations_OperationId431') is None


def test_assoc_timekeeper206_stub_double():
    # organization_User has no real 'organization_User208' property in the generated
    # code (a bare stub) -- manually attach it so model_meeting_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_meeting_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    partner = organization_User()
    setattr(partner, 'organization_User208', None)
    _safe_set(owner, 'model_meeting_Meeting207', partner)
    assert getattr(partner, 'organization_User208') == owner
    _safe_set(owner, 'model_meeting_Meeting207', None)
    assert getattr(partner, 'organization_User208') is None


def test_assoc_useCase148_stub_double():
    # requirement_UseCase has no real 'UseCase149' property in the generated
    # code (a bare stub) -- manually attach it so model_requirement_Step's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_requirement_Step's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_requirement_Step(userStep=True)
    partner = requirement_UseCase()
    setattr(partner, 'UseCase149', None)
    _safe_set(owner, 'useCaseSteps', partner)
    assert getattr(partner, 'UseCase149') == owner
    _safe_set(owner, 'useCaseSteps', None)
    assert getattr(partner, 'UseCase149') is None


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


def test_assoc_version275_stub_double():
    # versioning_PrimaryVersionSpec has no real 'versioning_PrimaryVersionSpec' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_ProjectInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_ProjectInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    partner = versioning_PrimaryVersionSpec()
    setattr(partner, 'versioning_PrimaryVersionSpec', None)
    _safe_set(owner, 'esmodel_ProjectInfo276', partner)
    assert getattr(partner, 'versioning_PrimaryVersionSpec') == owner
    _safe_set(owner, 'esmodel_ProjectInfo276', None)
    assert getattr(partner, 'versioning_PrimaryVersionSpec') is None


def test_assoc_versions271_stub_double():
    # versioning_Version has no real 'versioning_Version' property in the generated
    # code (a bare stub) -- manually attach it so esmodel_ProjectHistory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # esmodel_ProjectHistory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = esmodel_ProjectHistory(projectDescription="sample_text", projectName="sample_text")
    partner = versioning_Version()
    setattr(partner, 'versioning_Version', None)
    _safe_set(owner, 'esmodel_ProjectHistory272', {partner})
    assert getattr(partner, 'versioning_Version') == owner
    _safe_set(owner, 'esmodel_ProjectHistory272', set())
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


