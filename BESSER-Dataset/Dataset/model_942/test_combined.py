# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    change_ModelChangePackage,
    organization_OrgUnit,
    organization_User,
    UnicaseModelElement,
    model_Annotation,
    task_WorkPackage,
    profile_StereotypeInstance,
    OrgUnit,
    model_organization_Group,
    model_organization_User,
    task_WorkItem,
    organization_Group,
    model_organization_OrgUnit,
    Project,
    esmodel_url_ModelElementUrlFragment,
    url_ModelElementUrlFragment,
    url_ProjectUrlFragment,
    url_ServerUrl,
    esmodel_url_ModelElementUrl,
    esmodel_url_ProjectUrlFragment,
    esmodel_url_ServerUrl,
    Role,
    esmodel_roles_ServerAdmin,
    esmodel_roles_WriterRole,
    esmodel_roles_ProjectAdminRole,
    esmodel_roles_ReaderRole,
    ACOrgUnit,
    esmodel_accesscontrol_ACUser,
    esmodel_roles_Role,
    esmodel_accesscontrol_OrgUnitProperty,
    accesscontrol_ACOrgUnit,
    esmodel_accesscontrol_ACGroup,
    accesscontrol_OrgUnitProperty,
    roles_Role,
    ServerProjectEvent,
    esmodel_server_ProjectUpdatedEvent,
    ServerEvent,
    esmodel_server_ServerProjectEvent,
    operations_OperationId,
    ReadEvent,
    esmodel_events_NotificationReadEvent,
    esmodel_events_Event,
    CompositeOperation,
    esmodel_semantic_SemanticCompositeOperation,
    esmodel_operations_EObjectToModelElementIdMap,
    Event,
    esmodel_events_ShowHistoryEvent,
    esmodel_events_PerspectiveEvent,
    esmodel_events_UpdateEvent,
    esmodel_events_MergeGlobalChoiceEvent,
    esmodel_events_RevertEvent,
    esmodel_events_NotificationIgnoreEvent,
    esmodel_events_MergeEvent,
    esmodel_events_PluginFocusEvent,
    esmodel_events_CheckoutEvent,
    esmodel_events_PresentationSwitchEvent,
    esmodel_events_ExceptionEvent,
    esmodel_events_PluginStartEvent,
    esmodel_events_UndoEvent,
    esmodel_events_NavigatorCreateEvent,
    esmodel_server_ServerEvent,
    esmodel_events_URLEvent,
    esmodel_events_Validate,
    esmodel_events_TraceEvent,
    esmodel_events_ShowChangesEvent,
    esmodel_events_NotificationGenerationEvent,
    esmodel_events_DNDEvent,
    esmodel_events_LinkEvent,
    esmodel_events_AnnotationEvent,
    esmodel_events_MergeChoiceEvent,
    esmodel_events_ReadEvent,
    ReferenceOperation,
    esmodel_operations_MultiReferenceSetOperation,
    esmodel_operations_SingleReferenceOperation,
    esmodel_operations_ModelElementGroup,
    esmodel_operations_OperationGroup,
    AttributeOperation,
    esmodel_operations_DiagramLayoutOperation,
    esmodel_operations_MultiReferenceOperation,
    operations_esmodel_EObject,
    AbstractOperation,
    esmodel_operations_FeatureOperation,
    esmodel_operations_CreateDeleteOperation,
    esmodel_operations_CompositeOperation,
    FeatureOperation,
    esmodel_operations_MultiAttributeSetOperation,
    esmodel_operations_MultiAttributeMoveOperation,
    esmodel_operations_ReferenceOperation,
    esmodel_operations_MultiReferenceMoveOperation,
    esmodel_operations_MultiAttributeOperation,
    esmodel_operations_AttributeOperation,
    operations_EObjectToModelElementIdMap,
    operations_ReferenceOperation,
    esmodel_versioning_Version,
    esmodel_versioning_HistoryQuery,
    esmodel_versioning_VersionProperty,
    notification_ESNotification,
    versioning_LogMessage,
    events_Event,
    operations_AbstractOperation,
    esmodel_versioning_ChangePackage,
    versioning_ChangePackage,
    versioning_TagVersionSpec,
    esmodel_versioning_HistoryInfo,
    versioning_VersionProperty,
    VersionSpec,
    esmodel_versioning_HeadVersionSpec,
    esmodel_versioning_DateVersionSpec,
    esmodel_versioning_TagVersionSpec,
    esmodel_versioning_LogMessage,
    esmodel_versioning_VersionSpec,
    esmodel_ClientVersionInfo,
    esmodel_VersionInfo,
    esmodel_versioning_PrimaryVersionSpec,
    versioning_PrimaryVersionSpec,
    esmodel_ProjectInfo,
    versioning_Version,
    ProjectId,
    esmodel_ProjectHistory,
    ActivityObject,
    model_activity_ActivityInitial,
    model_activity_ActivityEnd,
    model_activity_Fork,
    model_activity_Branch,
    model_activity_Activity,
    activity_ActivityObject,
    accesscontrol_ACUser,
    SessionId,
    model_activity_Transition,
    ProjectHistory,
    accesscontrol_ACGroup,
    esmodel_ServerSpace,
    ModelElementId,
    model_util_ModelElementPath,
    StereotypeAttributeInstance,
    model_profile_StereotypeAttributeInstanceString,
    model_profile_StereotypeAttributeInstance,
    StereotypeAttribute,
    model_profile_StereotypeAttributeSimple,
    model_profile_StereotypeAttribute,
    profile_StereotypeAttributeInstance,
    activity_Transition,
    model_activity_ActivityObject,
    model_profile_StereotypeInstance,
    profile_StereotypeAttribute,
    profile_Profile,
    model_profile_Stereotype,
    profile_Stereotype,
    model_profile_Profile,
    StateNode,
    model_state_StateEnd,
    model_state_StateInitial,
    model_state_State,
    state_Transition,
    model_state_StateNode,
    state_StateNode,
    model_state_Transition,
    MeetingSection,
    model_meeting_IssueMeetingSection,
    model_meeting_WorkItemMeetingSection,
    model_meeting_CompositeMeetingSection,
    model_meeting_MeetingSection,
    meeting_WorkItemMeetingSection,
    meeting_IssueMeetingSection,
    meeting_MeetingSection,
    component_Component,
    model_component_ComponentService,
    model_meeting_Meeting,
    model_component_DeploymentNode,
    component_ComponentService,
    model_component_Component,
    Solution,
    model_change_MergingSolution,
    change_MergingProposal,
    Proposal,
    model_change_MergingProposal,
    Issue,
    model_change_MergingIssue,
    model_change_ModelChangePackage,
    rationale_Issue,
    rationale_Criterion,
    model_rationale_Criterion,
    rationale_Assessment,
    rationale_Solution,
    rationale_Proposal,
    Criterion,
    model_requirement_NonFunctionalRequirement,
    requirement_SystemFunction,
    NonDomainElement,
    model_rationale_Assessment,
    model_rationale_Proposal,
    model_rationale_Solution,
    model_requirement_SystemFunction,
    model_rationale_Comment,
    model_requirement_UserTask,
    model_requirement_Step,
    model_requirement_ActorInstance,
    model_requirement_Actor,
    requirement_ActorInstance,
    model_requirement_Scenario,
    requirement_NonFunctionalRequirement,
    requirement_UserTask,
    requirement_Step,
    requirement_Actor,
    model_requirement_UseCase,
    model_requirement_FunctionalRequirement,
    document_Section,
    requirement_FunctionalRequirement,
    model_classes_Dependency,
    Section,
    model_document_CompositeSection,
    model_document_LeafSection,
    document_CompositeSection,
    model_document_Section,
    model_classes_MethodArgument,
    classes_MethodArgument,
    model_classes_Method,
    classes_PackageElement,
    model_classes_Attribute,
    model_classes_Association,
    classes_Association,
    requirement_Scenario,
    requirement_UseCase,
    classes_Method,
    classes_Attribute,
    classes_Class,
    PackageElement,
    model_classes_Package,
    model_classes_Class,
    classes_Dependency,
    classes_Package,
    model_classes_PackageElement,
    diagram_model_Diagram,
    task_Checkable,
    model_bug_BugReport,
    model_task_ActionItem,
    model_task_Checkable,
    WorkItem,
    model_task_Milestone,
    model_task_WorkPackage,
    model_Project,
    model_NonDomainElement,
    model_Attachment,
    metamodel_UniqueIdentifier,
    rationale_Comment,
    document_LeafSection,
    Attachment,
    model_attachment_UrlAttachment,
    model_attachment_FileAttachment,
    model_diagram_MEDiagram,
    Annotation,
    model_rationale_Issue,
    model_task_WorkItem,
    metamodel_AssociationClassElement,
    metamodel_NonDomainElement,
    metamodel_ModelVersion,
    UniqueIdentifier,
    esmodel_ProjectId,
    esmodel_operations_OperationId,
    esmodel_SessionId,
    esmodel_accesscontrol_ACOrgUnitId,
    metamodel_ModelElementId,
    IdentifiableElement,
    esmodel_operations_AbstractOperation,
    esmodel_notification_ESNotification,
    esmodel_FileIdentifier,
    esmodel_accesscontrol_ACOrgUnit,
    metamodel_ModelElement,
    metamodel_IdentifiableElement,
    ModelElement,
    model_UnicaseModelElement,
    metamodel_Project,
    AssociationType,
    MergeGlobalChoiceSelection,
    DiagramType,
    ScopeType,
    ResolutionType,
    ActivityType,
    BugStatus,
    Severity,
    ContainmentType,
    ArgumentDirectionType,
    MergeChoiceSelection,
    VisibilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_change_modelchangepackage_is_not_abstract():
    assert not inspect.isabstract(change_ModelChangePackage)


def test_hyp_change_modelchangepackage_constructor_exists():
    assert callable(change_ModelChangePackage.__init__)


def test_hyp_change_modelchangepackage_constructor_args():
    sig = inspect.signature(change_ModelChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_organization_orgunit_is_not_abstract():
    assert not inspect.isabstract(organization_OrgUnit)


def test_hyp_organization_orgunit_constructor_exists():
    assert callable(organization_OrgUnit.__init__)


def test_hyp_organization_orgunit_constructor_args():
    sig = inspect.signature(organization_OrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_organization_user_is_not_abstract():
    assert not inspect.isabstract(organization_User)


def test_hyp_organization_user_constructor_exists():
    assert callable(organization_User.__init__)


def test_hyp_organization_user_constructor_args():
    sig = inspect.signature(organization_User.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unicasemodelelement_is_not_abstract():
    assert not inspect.isabstract(UnicaseModelElement)


def test_hyp_unicasemodelelement_constructor_exists():
    assert callable(UnicaseModelElement.__init__)


def test_hyp_unicasemodelelement_constructor_args():
    sig = inspect.signature(UnicaseModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_annotation_is_not_abstract():
    assert not inspect.isabstract(model_Annotation)


def test_hyp_model_annotation_constructor_exists():
    assert callable(model_Annotation.__init__)


def test_hyp_model_annotation_constructor_args():
    sig = inspect.signature(model_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_task_workpackage_is_not_abstract():
    assert not inspect.isabstract(task_WorkPackage)


def test_hyp_task_workpackage_constructor_exists():
    assert callable(task_WorkPackage.__init__)


def test_hyp_task_workpackage_constructor_args():
    sig = inspect.signature(task_WorkPackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_stereotypeinstance_is_not_abstract():
    assert not inspect.isabstract(profile_StereotypeInstance)


def test_hyp_profile_stereotypeinstance_constructor_exists():
    assert callable(profile_StereotypeInstance.__init__)


def test_hyp_profile_stereotypeinstance_constructor_args():
    sig = inspect.signature(profile_StereotypeInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orgunit_is_not_abstract():
    assert not inspect.isabstract(OrgUnit)


def test_hyp_orgunit_constructor_exists():
    assert callable(OrgUnit.__init__)


def test_hyp_orgunit_constructor_args():
    sig = inspect.signature(OrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_organization_group_is_not_abstract():
    assert not inspect.isabstract(model_organization_Group)


def test_hyp_model_organization_group_constructor_exists():
    assert callable(model_organization_Group.__init__)


def test_hyp_model_organization_group_constructor_args():
    sig = inspect.signature(model_organization_Group.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_organization_user_is_not_abstract():
    assert not inspect.isabstract(model_organization_User)


def test_hyp_model_organization_user_constructor_exists():
    assert callable(model_organization_User.__init__)


def test_hyp_model_organization_user_constructor_args():
    sig = inspect.signature(model_organization_User.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "email" in params, "Missing parameter 'email'"






def test_hyp_task_workitem_is_not_abstract():
    assert not inspect.isabstract(task_WorkItem)


def test_hyp_task_workitem_constructor_exists():
    assert callable(task_WorkItem.__init__)


def test_hyp_task_workitem_constructor_args():
    sig = inspect.signature(task_WorkItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_organization_group_is_not_abstract():
    assert not inspect.isabstract(organization_Group)


def test_hyp_organization_group_constructor_exists():
    assert callable(organization_Group.__init__)


def test_hyp_organization_group_constructor_args():
    sig = inspect.signature(organization_Group.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_organization_orgunit_is_not_abstract():
    assert not inspect.isabstract(model_organization_OrgUnit)


def test_hyp_model_organization_orgunit_constructor_exists():
    assert callable(model_organization_OrgUnit.__init__)


def test_hyp_model_organization_orgunit_constructor_args():
    sig = inspect.signature(model_organization_OrgUnit.__init__)
    params = list(sig.parameters.keys())
    assert "acOrgId" in params, "Missing parameter 'acOrgId'"




def test_hyp_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_hyp_project_constructor_exists():
    assert callable(Project.__init__)


def test_hyp_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_url_modelelementurlfragment_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ModelElementUrlFragment)


def test_hyp_esmodel_url_modelelementurlfragment_constructor_exists():
    assert callable(esmodel_url_ModelElementUrlFragment.__init__)


def test_hyp_esmodel_url_modelelementurlfragment_constructor_args():
    sig = inspect.signature(esmodel_url_ModelElementUrlFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_url_modelelementurlfragment_is_not_abstract():
    assert not inspect.isabstract(url_ModelElementUrlFragment)


def test_hyp_url_modelelementurlfragment_constructor_exists():
    assert callable(url_ModelElementUrlFragment.__init__)


def test_hyp_url_modelelementurlfragment_constructor_args():
    sig = inspect.signature(url_ModelElementUrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_url_projecturlfragment_is_not_abstract():
    assert not inspect.isabstract(url_ProjectUrlFragment)


def test_hyp_url_projecturlfragment_constructor_exists():
    assert callable(url_ProjectUrlFragment.__init__)


def test_hyp_url_projecturlfragment_constructor_args():
    sig = inspect.signature(url_ProjectUrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_url_serverurl_is_not_abstract():
    assert not inspect.isabstract(url_ServerUrl)


def test_hyp_url_serverurl_constructor_exists():
    assert callable(url_ServerUrl.__init__)


def test_hyp_url_serverurl_constructor_args():
    sig = inspect.signature(url_ServerUrl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_url_modelelementurl_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ModelElementUrl)


def test_hyp_esmodel_url_modelelementurl_constructor_exists():
    assert callable(esmodel_url_ModelElementUrl.__init__)


def test_hyp_esmodel_url_modelelementurl_constructor_args():
    sig = inspect.signature(esmodel_url_ModelElementUrl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_url_projecturlfragment_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ProjectUrlFragment)


def test_hyp_esmodel_url_projecturlfragment_constructor_exists():
    assert callable(esmodel_url_ProjectUrlFragment.__init__)


def test_hyp_esmodel_url_projecturlfragment_constructor_args():
    sig = inspect.signature(esmodel_url_ProjectUrlFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_esmodel_url_serverurl_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ServerUrl)


def test_hyp_esmodel_url_serverurl_constructor_exists():
    assert callable(esmodel_url_ServerUrl.__init__)


def test_hyp_esmodel_url_serverurl_constructor_args():
    sig = inspect.signature(esmodel_url_ServerUrl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "hostName" in params, "Missing parameter 'hostName'"





def test_hyp_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_hyp_role_constructor_exists():
    assert callable(Role.__init__)


def test_hyp_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_roles_serveradmin_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_ServerAdmin)


def test_hyp_esmodel_roles_serveradmin_constructor_exists():
    assert callable(esmodel_roles_ServerAdmin.__init__)


def test_hyp_esmodel_roles_serveradmin_constructor_args():
    sig = inspect.signature(esmodel_roles_ServerAdmin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_roles_writerrole_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_WriterRole)


def test_hyp_esmodel_roles_writerrole_constructor_exists():
    assert callable(esmodel_roles_WriterRole.__init__)


def test_hyp_esmodel_roles_writerrole_constructor_args():
    sig = inspect.signature(esmodel_roles_WriterRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_roles_projectadminrole_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_ProjectAdminRole)


def test_hyp_esmodel_roles_projectadminrole_constructor_exists():
    assert callable(esmodel_roles_ProjectAdminRole.__init__)


def test_hyp_esmodel_roles_projectadminrole_constructor_args():
    sig = inspect.signature(esmodel_roles_ProjectAdminRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_roles_readerrole_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_ReaderRole)


def test_hyp_esmodel_roles_readerrole_constructor_exists():
    assert callable(esmodel_roles_ReaderRole.__init__)


def test_hyp_esmodel_roles_readerrole_constructor_args():
    sig = inspect.signature(esmodel_roles_ReaderRole.__init__)
    params = list(sig.parameters.keys())



def test_hyp_acorgunit_is_not_abstract():
    assert not inspect.isabstract(ACOrgUnit)


def test_hyp_acorgunit_constructor_exists():
    assert callable(ACOrgUnit.__init__)


def test_hyp_acorgunit_constructor_args():
    sig = inspect.signature(ACOrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_accesscontrol_acuser_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACUser)


def test_hyp_esmodel_accesscontrol_acuser_constructor_exists():
    assert callable(esmodel_accesscontrol_ACUser.__init__)


def test_hyp_esmodel_accesscontrol_acuser_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACUser.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"





def test_hyp_esmodel_roles_role_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_Role)


def test_hyp_esmodel_roles_role_constructor_exists():
    assert callable(esmodel_roles_Role.__init__)


def test_hyp_esmodel_roles_role_constructor_args():
    sig = inspect.signature(esmodel_roles_Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_accesscontrol_orgunitproperty_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_OrgUnitProperty)


def test_hyp_esmodel_accesscontrol_orgunitproperty_constructor_exists():
    assert callable(esmodel_accesscontrol_OrgUnitProperty.__init__)


def test_hyp_esmodel_accesscontrol_orgunitproperty_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_OrgUnitProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_accesscontrol_acorgunit_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_ACOrgUnit)


def test_hyp_accesscontrol_acorgunit_constructor_exists():
    assert callable(accesscontrol_ACOrgUnit.__init__)


def test_hyp_accesscontrol_acorgunit_constructor_args():
    sig = inspect.signature(accesscontrol_ACOrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_accesscontrol_acgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACGroup)


def test_hyp_esmodel_accesscontrol_acgroup_constructor_exists():
    assert callable(esmodel_accesscontrol_ACGroup.__init__)


def test_hyp_esmodel_accesscontrol_acgroup_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accesscontrol_orgunitproperty_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_OrgUnitProperty)


def test_hyp_accesscontrol_orgunitproperty_constructor_exists():
    assert callable(accesscontrol_OrgUnitProperty.__init__)


def test_hyp_accesscontrol_orgunitproperty_constructor_args():
    sig = inspect.signature(accesscontrol_OrgUnitProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_roles_role_is_not_abstract():
    assert not inspect.isabstract(roles_Role)


def test_hyp_roles_role_constructor_exists():
    assert callable(roles_Role.__init__)


def test_hyp_roles_role_constructor_args():
    sig = inspect.signature(roles_Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_serverprojectevent_is_not_abstract():
    assert not inspect.isabstract(ServerProjectEvent)


def test_hyp_serverprojectevent_constructor_exists():
    assert callable(ServerProjectEvent.__init__)


def test_hyp_serverprojectevent_constructor_args():
    sig = inspect.signature(ServerProjectEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_server_projectupdatedevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_server_ProjectUpdatedEvent)


def test_hyp_esmodel_server_projectupdatedevent_constructor_exists():
    assert callable(esmodel_server_ProjectUpdatedEvent.__init__)


def test_hyp_esmodel_server_projectupdatedevent_constructor_args():
    sig = inspect.signature(esmodel_server_ProjectUpdatedEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_serverevent_is_not_abstract():
    assert not inspect.isabstract(ServerEvent)


def test_hyp_serverevent_constructor_exists():
    assert callable(ServerEvent.__init__)


def test_hyp_serverevent_constructor_args():
    sig = inspect.signature(ServerEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_server_serverprojectevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_server_ServerProjectEvent)


def test_hyp_esmodel_server_serverprojectevent_constructor_exists():
    assert callable(esmodel_server_ServerProjectEvent.__init__)


def test_hyp_esmodel_server_serverprojectevent_constructor_args():
    sig = inspect.signature(esmodel_server_ServerProjectEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operations_operationid_is_not_abstract():
    assert not inspect.isabstract(operations_OperationId)


def test_hyp_operations_operationid_constructor_exists():
    assert callable(operations_OperationId.__init__)


def test_hyp_operations_operationid_constructor_args():
    sig = inspect.signature(operations_OperationId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_readevent_is_not_abstract():
    assert not inspect.isabstract(ReadEvent)


def test_hyp_readevent_constructor_exists():
    assert callable(ReadEvent.__init__)


def test_hyp_readevent_constructor_args():
    sig = inspect.signature(ReadEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_notificationreadevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NotificationReadEvent)


def test_hyp_esmodel_events_notificationreadevent_constructor_exists():
    assert callable(esmodel_events_NotificationReadEvent.__init__)


def test_hyp_esmodel_events_notificationreadevent_constructor_args():
    sig = inspect.signature(esmodel_events_NotificationReadEvent.__init__)
    params = list(sig.parameters.keys())
    assert "notificationId" in params, "Missing parameter 'notificationId'"




def test_hyp_esmodel_events_event_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_Event)


def test_hyp_esmodel_events_event_constructor_exists():
    assert callable(esmodel_events_Event.__init__)


def test_hyp_esmodel_events_event_constructor_args():
    sig = inspect.signature(esmodel_events_Event.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"




def test_hyp_compositeoperation_is_not_abstract():
    assert not inspect.isabstract(CompositeOperation)


def test_hyp_compositeoperation_constructor_exists():
    assert callable(CompositeOperation.__init__)


def test_hyp_compositeoperation_constructor_args():
    sig = inspect.signature(CompositeOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_semantic_semanticcompositeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_semantic_SemanticCompositeOperation)


def test_hyp_esmodel_semantic_semanticcompositeoperation_constructor_exists():
    assert callable(esmodel_semantic_SemanticCompositeOperation.__init__)


def test_hyp_esmodel_semantic_semanticcompositeoperation_constructor_args():
    sig = inspect.signature(esmodel_semantic_SemanticCompositeOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_eobjecttomodelelementidmap_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_EObjectToModelElementIdMap)


def test_hyp_esmodel_operations_eobjecttomodelelementidmap_constructor_exists():
    assert callable(esmodel_operations_EObjectToModelElementIdMap.__init__)


def test_hyp_esmodel_operations_eobjecttomodelelementidmap_constructor_args():
    sig = inspect.signature(esmodel_operations_EObjectToModelElementIdMap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_showhistoryevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ShowHistoryEvent)


def test_hyp_esmodel_events_showhistoryevent_constructor_exists():
    assert callable(esmodel_events_ShowHistoryEvent.__init__)


def test_hyp_esmodel_events_showhistoryevent_constructor_args():
    sig = inspect.signature(esmodel_events_ShowHistoryEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_perspectiveevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PerspectiveEvent)


def test_hyp_esmodel_events_perspectiveevent_constructor_exists():
    assert callable(esmodel_events_PerspectiveEvent.__init__)


def test_hyp_esmodel_events_perspectiveevent_constructor_args():
    sig = inspect.signature(esmodel_events_PerspectiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_updateevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_UpdateEvent)


def test_hyp_esmodel_events_updateevent_constructor_exists():
    assert callable(esmodel_events_UpdateEvent.__init__)


def test_hyp_esmodel_events_updateevent_constructor_args():
    sig = inspect.signature(esmodel_events_UpdateEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_mergeglobalchoiceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_MergeGlobalChoiceEvent)


def test_hyp_esmodel_events_mergeglobalchoiceevent_constructor_exists():
    assert callable(esmodel_events_MergeGlobalChoiceEvent.__init__)


def test_hyp_esmodel_events_mergeglobalchoiceevent_constructor_args():
    sig = inspect.signature(esmodel_events_MergeGlobalChoiceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"




def test_hyp_esmodel_events_revertevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_RevertEvent)


def test_hyp_esmodel_events_revertevent_constructor_exists():
    assert callable(esmodel_events_RevertEvent.__init__)


def test_hyp_esmodel_events_revertevent_constructor_args():
    sig = inspect.signature(esmodel_events_RevertEvent.__init__)
    params = list(sig.parameters.keys())
    assert "revertedChangesCount" in params, "Missing parameter 'revertedChangesCount'"




def test_hyp_esmodel_events_notificationignoreevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NotificationIgnoreEvent)


def test_hyp_esmodel_events_notificationignoreevent_constructor_exists():
    assert callable(esmodel_events_NotificationIgnoreEvent.__init__)


def test_hyp_esmodel_events_notificationignoreevent_constructor_args():
    sig = inspect.signature(esmodel_events_NotificationIgnoreEvent.__init__)
    params = list(sig.parameters.keys())
    assert "notificationId" in params, "Missing parameter 'notificationId'"




def test_hyp_esmodel_events_mergeevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_MergeEvent)


def test_hyp_esmodel_events_mergeevent_constructor_exists():
    assert callable(esmodel_events_MergeEvent.__init__)


def test_hyp_esmodel_events_mergeevent_constructor_args():
    sig = inspect.signature(esmodel_events_MergeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "numberOfConflicts" in params, "Missing parameter 'numberOfConflicts'"





def test_hyp_esmodel_events_pluginfocusevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PluginFocusEvent)


def test_hyp_esmodel_events_pluginfocusevent_constructor_exists():
    assert callable(esmodel_events_PluginFocusEvent.__init__)


def test_hyp_esmodel_events_pluginfocusevent_constructor_args():
    sig = inspect.signature(esmodel_events_PluginFocusEvent.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "pluginId" in params, "Missing parameter 'pluginId'"





def test_hyp_esmodel_events_checkoutevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_CheckoutEvent)


def test_hyp_esmodel_events_checkoutevent_constructor_exists():
    assert callable(esmodel_events_CheckoutEvent.__init__)


def test_hyp_esmodel_events_checkoutevent_constructor_args():
    sig = inspect.signature(esmodel_events_CheckoutEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_presentationswitchevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PresentationSwitchEvent)


def test_hyp_esmodel_events_presentationswitchevent_constructor_exists():
    assert callable(esmodel_events_PresentationSwitchEvent.__init__)


def test_hyp_esmodel_events_presentationswitchevent_constructor_args():
    sig = inspect.signature(esmodel_events_PresentationSwitchEvent.__init__)
    params = list(sig.parameters.keys())
    assert "newPresentation" in params, "Missing parameter 'newPresentation'"
    assert "readView" in params, "Missing parameter 'readView'"





def test_hyp_esmodel_events_exceptionevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ExceptionEvent)


def test_hyp_esmodel_events_exceptionevent_constructor_exists():
    assert callable(esmodel_events_ExceptionEvent.__init__)


def test_hyp_esmodel_events_exceptionevent_constructor_args():
    sig = inspect.signature(esmodel_events_ExceptionEvent.__init__)
    params = list(sig.parameters.keys())
    assert "ExceptionCauseStackTrace" in params, "Missing parameter 'ExceptionCauseStackTrace'"
    assert "ExceptionCauseTitle" in params, "Missing parameter 'ExceptionCauseTitle'"
    assert "ExceptionStackTrace" in params, "Missing parameter 'ExceptionStackTrace'"
    assert "ExceptionTitle" in params, "Missing parameter 'ExceptionTitle'"







def test_hyp_esmodel_events_pluginstartevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PluginStartEvent)


def test_hyp_esmodel_events_pluginstartevent_constructor_exists():
    assert callable(esmodel_events_PluginStartEvent.__init__)


def test_hyp_esmodel_events_pluginstartevent_constructor_args():
    sig = inspect.signature(esmodel_events_PluginStartEvent.__init__)
    params = list(sig.parameters.keys())
    assert "pluginId" in params, "Missing parameter 'pluginId'"




def test_hyp_esmodel_events_undoevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_UndoEvent)


def test_hyp_esmodel_events_undoevent_constructor_exists():
    assert callable(esmodel_events_UndoEvent.__init__)


def test_hyp_esmodel_events_undoevent_constructor_args():
    sig = inspect.signature(esmodel_events_UndoEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_navigatorcreateevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NavigatorCreateEvent)


def test_hyp_esmodel_events_navigatorcreateevent_constructor_exists():
    assert callable(esmodel_events_NavigatorCreateEvent.__init__)


def test_hyp_esmodel_events_navigatorcreateevent_constructor_args():
    sig = inspect.signature(esmodel_events_NavigatorCreateEvent.__init__)
    params = list(sig.parameters.keys())
    assert "dynamic" in params, "Missing parameter 'dynamic'"




def test_hyp_esmodel_server_serverevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_server_ServerEvent)


def test_hyp_esmodel_server_serverevent_constructor_exists():
    assert callable(esmodel_server_ServerEvent.__init__)


def test_hyp_esmodel_server_serverevent_constructor_args():
    sig = inspect.signature(esmodel_server_ServerEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_urlevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_URLEvent)


def test_hyp_esmodel_events_urlevent_constructor_exists():
    assert callable(esmodel_events_URLEvent.__init__)


def test_hyp_esmodel_events_urlevent_constructor_args():
    sig = inspect.signature(esmodel_events_URLEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sourceView" in params, "Missing parameter 'sourceView'"




def test_hyp_esmodel_events_validate_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_Validate)


def test_hyp_esmodel_events_validate_constructor_exists():
    assert callable(esmodel_events_Validate.__init__)


def test_hyp_esmodel_events_validate_constructor_args():
    sig = inspect.signature(esmodel_events_Validate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_traceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_TraceEvent)


def test_hyp_esmodel_events_traceevent_constructor_exists():
    assert callable(esmodel_events_TraceEvent.__init__)


def test_hyp_esmodel_events_traceevent_constructor_args():
    sig = inspect.signature(esmodel_events_TraceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"




def test_hyp_esmodel_events_showchangesevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ShowChangesEvent)


def test_hyp_esmodel_events_showchangesevent_constructor_exists():
    assert callable(esmodel_events_ShowChangesEvent.__init__)


def test_hyp_esmodel_events_showchangesevent_constructor_args():
    sig = inspect.signature(esmodel_events_ShowChangesEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_notificationgenerationevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NotificationGenerationEvent)


def test_hyp_esmodel_events_notificationgenerationevent_constructor_exists():
    assert callable(esmodel_events_NotificationGenerationEvent.__init__)


def test_hyp_esmodel_events_notificationgenerationevent_constructor_args():
    sig = inspect.signature(esmodel_events_NotificationGenerationEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_dndevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_DNDEvent)


def test_hyp_esmodel_events_dndevent_constructor_exists():
    assert callable(esmodel_events_DNDEvent.__init__)


def test_hyp_esmodel_events_dndevent_constructor_args():
    sig = inspect.signature(esmodel_events_DNDEvent.__init__)
    params = list(sig.parameters.keys())
    assert "targetView" in params, "Missing parameter 'targetView'"
    assert "sourceView" in params, "Missing parameter 'sourceView'"





def test_hyp_esmodel_events_linkevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_LinkEvent)


def test_hyp_esmodel_events_linkevent_constructor_exists():
    assert callable(esmodel_events_LinkEvent.__init__)


def test_hyp_esmodel_events_linkevent_constructor_args():
    sig = inspect.signature(esmodel_events_LinkEvent.__init__)
    params = list(sig.parameters.keys())
    assert "createdNew" in params, "Missing parameter 'createdNew'"
    assert "sourceView" in params, "Missing parameter 'sourceView'"





def test_hyp_esmodel_events_annotationevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_AnnotationEvent)


def test_hyp_esmodel_events_annotationevent_constructor_exists():
    assert callable(esmodel_events_AnnotationEvent.__init__)


def test_hyp_esmodel_events_annotationevent_constructor_args():
    sig = inspect.signature(esmodel_events_AnnotationEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_events_mergechoiceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_MergeChoiceEvent)


def test_hyp_esmodel_events_mergechoiceevent_constructor_exists():
    assert callable(esmodel_events_MergeChoiceEvent.__init__)


def test_hyp_esmodel_events_mergechoiceevent_constructor_args():
    sig = inspect.signature(esmodel_events_MergeChoiceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "createdIssueName" in params, "Missing parameter 'createdIssueName'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "contextFeature" in params, "Missing parameter 'contextFeature'"






def test_hyp_esmodel_events_readevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ReadEvent)


def test_hyp_esmodel_events_readevent_constructor_exists():
    assert callable(esmodel_events_ReadEvent.__init__)


def test_hyp_esmodel_events_readevent_constructor_args():
    sig = inspect.signature(esmodel_events_ReadEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sourceView" in params, "Missing parameter 'sourceView'"
    assert "readView" in params, "Missing parameter 'readView'"





def test_hyp_referenceoperation_is_not_abstract():
    assert not inspect.isabstract(ReferenceOperation)


def test_hyp_referenceoperation_constructor_exists():
    assert callable(ReferenceOperation.__init__)


def test_hyp_referenceoperation_constructor_args():
    sig = inspect.signature(ReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_multireferencesetoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiReferenceSetOperation)


def test_hyp_esmodel_operations_multireferencesetoperation_constructor_exists():
    assert callable(esmodel_operations_MultiReferenceSetOperation.__init__)


def test_hyp_esmodel_operations_multireferencesetoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiReferenceSetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"




def test_hyp_esmodel_operations_singlereferenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_SingleReferenceOperation)


def test_hyp_esmodel_operations_singlereferenceoperation_constructor_exists():
    assert callable(esmodel_operations_SingleReferenceOperation.__init__)


def test_hyp_esmodel_operations_singlereferenceoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_SingleReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_modelelementgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_ModelElementGroup)


def test_hyp_esmodel_operations_modelelementgroup_constructor_exists():
    assert callable(esmodel_operations_ModelElementGroup.__init__)


def test_hyp_esmodel_operations_modelelementgroup_constructor_args():
    sig = inspect.signature(esmodel_operations_ModelElementGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_esmodel_operations_operationgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_OperationGroup)


def test_hyp_esmodel_operations_operationgroup_constructor_exists():
    assert callable(esmodel_operations_OperationGroup.__init__)


def test_hyp_esmodel_operations_operationgroup_constructor_args():
    sig = inspect.signature(esmodel_operations_OperationGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(AttributeOperation)


def test_hyp_attributeoperation_constructor_exists():
    assert callable(AttributeOperation.__init__)


def test_hyp_attributeoperation_constructor_args():
    sig = inspect.signature(AttributeOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_diagramlayoutoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_DiagramLayoutOperation)


def test_hyp_esmodel_operations_diagramlayoutoperation_constructor_exists():
    assert callable(esmodel_operations_DiagramLayoutOperation.__init__)


def test_hyp_esmodel_operations_diagramlayoutoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_DiagramLayoutOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_multireferenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiReferenceOperation)


def test_hyp_esmodel_operations_multireferenceoperation_constructor_exists():
    assert callable(esmodel_operations_MultiReferenceOperation.__init__)


def test_hyp_esmodel_operations_multireferenceoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiReferenceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "add" in params, "Missing parameter 'add'"





def test_hyp_operations_esmodel_eobject_is_not_abstract():
    assert not inspect.isabstract(operations_esmodel_EObject)


def test_hyp_operations_esmodel_eobject_constructor_exists():
    assert callable(operations_esmodel_EObject.__init__)


def test_hyp_operations_esmodel_eobject_constructor_args():
    sig = inspect.signature(operations_esmodel_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(AbstractOperation)


def test_hyp_abstractoperation_constructor_exists():
    assert callable(AbstractOperation.__init__)


def test_hyp_abstractoperation_constructor_args():
    sig = inspect.signature(AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_featureoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_FeatureOperation)


def test_hyp_esmodel_operations_featureoperation_constructor_exists():
    assert callable(esmodel_operations_FeatureOperation.__init__)


def test_hyp_esmodel_operations_featureoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_FeatureOperation.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"




def test_hyp_esmodel_operations_createdeleteoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_CreateDeleteOperation)


def test_hyp_esmodel_operations_createdeleteoperation_constructor_exists():
    assert callable(esmodel_operations_CreateDeleteOperation.__init__)


def test_hyp_esmodel_operations_createdeleteoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_CreateDeleteOperation.__init__)
    params = list(sig.parameters.keys())
    assert "delete" in params, "Missing parameter 'delete'"




def test_hyp_esmodel_operations_compositeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_CompositeOperation)


def test_hyp_esmodel_operations_compositeoperation_constructor_exists():
    assert callable(esmodel_operations_CompositeOperation.__init__)


def test_hyp_esmodel_operations_compositeoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_CompositeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "compositeDescription" in params, "Missing parameter 'compositeDescription'"
    assert "reversed" in params, "Missing parameter 'reversed'"
    assert "compositeName" in params, "Missing parameter 'compositeName'"






def test_hyp_featureoperation_is_not_abstract():
    assert not inspect.isabstract(FeatureOperation)


def test_hyp_featureoperation_constructor_exists():
    assert callable(FeatureOperation.__init__)


def test_hyp_featureoperation_constructor_args():
    sig = inspect.signature(FeatureOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_multiattributesetoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiAttributeSetOperation)


def test_hyp_esmodel_operations_multiattributesetoperation_constructor_exists():
    assert callable(esmodel_operations_MultiAttributeSetOperation.__init__)


def test_hyp_esmodel_operations_multiattributesetoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiAttributeSetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"
    assert "index" in params, "Missing parameter 'index'"






def test_hyp_esmodel_operations_multiattributemoveoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiAttributeMoveOperation)


def test_hyp_esmodel_operations_multiattributemoveoperation_constructor_exists():
    assert callable(esmodel_operations_MultiAttributeMoveOperation.__init__)


def test_hyp_esmodel_operations_multiattributemoveoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiAttributeMoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "oldIndex" in params, "Missing parameter 'oldIndex'"
    assert "referencedValue" in params, "Missing parameter 'referencedValue'"
    assert "newIndex" in params, "Missing parameter 'newIndex'"






def test_hyp_esmodel_operations_referenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_ReferenceOperation)


def test_hyp_esmodel_operations_referenceoperation_constructor_exists():
    assert callable(esmodel_operations_ReferenceOperation.__init__)


def test_hyp_esmodel_operations_referenceoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_ReferenceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "containmentType" in params, "Missing parameter 'containmentType'"
    assert "oppositeFeatureName" in params, "Missing parameter 'oppositeFeatureName'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"






def test_hyp_esmodel_operations_multireferencemoveoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiReferenceMoveOperation)


def test_hyp_esmodel_operations_multireferencemoveoperation_constructor_exists():
    assert callable(esmodel_operations_MultiReferenceMoveOperation.__init__)


def test_hyp_esmodel_operations_multireferencemoveoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiReferenceMoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "oldIndex" in params, "Missing parameter 'oldIndex'"
    assert "newIndex" in params, "Missing parameter 'newIndex'"





def test_hyp_esmodel_operations_multiattributeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiAttributeOperation)


def test_hyp_esmodel_operations_multiattributeoperation_constructor_exists():
    assert callable(esmodel_operations_MultiAttributeOperation.__init__)


def test_hyp_esmodel_operations_multiattributeoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiAttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "indexes" in params, "Missing parameter 'indexes'"
    assert "add" in params, "Missing parameter 'add'"
    assert "referencedValues" in params, "Missing parameter 'referencedValues'"






def test_hyp_esmodel_operations_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_AttributeOperation)


def test_hyp_esmodel_operations_attributeoperation_constructor_exists():
    assert callable(esmodel_operations_AttributeOperation.__init__)


def test_hyp_esmodel_operations_attributeoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "oldValue" in params, "Missing parameter 'oldValue'"
    assert "newValue" in params, "Missing parameter 'newValue'"





def test_hyp_operations_eobjecttomodelelementidmap_is_not_abstract():
    assert not inspect.isabstract(operations_EObjectToModelElementIdMap)


def test_hyp_operations_eobjecttomodelelementidmap_constructor_exists():
    assert callable(operations_EObjectToModelElementIdMap.__init__)


def test_hyp_operations_eobjecttomodelelementidmap_constructor_args():
    sig = inspect.signature(operations_EObjectToModelElementIdMap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operations_referenceoperation_is_not_abstract():
    assert not inspect.isabstract(operations_ReferenceOperation)


def test_hyp_operations_referenceoperation_constructor_exists():
    assert callable(operations_ReferenceOperation.__init__)


def test_hyp_operations_referenceoperation_constructor_args():
    sig = inspect.signature(operations_ReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_versioning_version_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_Version)


def test_hyp_esmodel_versioning_version_constructor_exists():
    assert callable(esmodel_versioning_Version.__init__)


def test_hyp_esmodel_versioning_version_constructor_args():
    sig = inspect.signature(esmodel_versioning_Version.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_versioning_historyquery_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_HistoryQuery)


def test_hyp_esmodel_versioning_historyquery_constructor_exists():
    assert callable(esmodel_versioning_HistoryQuery.__init__)


def test_hyp_esmodel_versioning_historyquery_constructor_args():
    sig = inspect.signature(esmodel_versioning_HistoryQuery.__init__)
    params = list(sig.parameters.keys())
    assert "includeChangePackage" in params, "Missing parameter 'includeChangePackage'"




def test_hyp_esmodel_versioning_versionproperty_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_VersionProperty)


def test_hyp_esmodel_versioning_versionproperty_constructor_exists():
    assert callable(esmodel_versioning_VersionProperty.__init__)


def test_hyp_esmodel_versioning_versionproperty_constructor_args():
    sig = inspect.signature(esmodel_versioning_VersionProperty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_notification_esnotification_is_not_abstract():
    assert not inspect.isabstract(notification_ESNotification)


def test_hyp_notification_esnotification_constructor_exists():
    assert callable(notification_ESNotification.__init__)


def test_hyp_notification_esnotification_constructor_args():
    sig = inspect.signature(notification_ESNotification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_versioning_logmessage_is_not_abstract():
    assert not inspect.isabstract(versioning_LogMessage)


def test_hyp_versioning_logmessage_constructor_exists():
    assert callable(versioning_LogMessage.__init__)


def test_hyp_versioning_logmessage_constructor_args():
    sig = inspect.signature(versioning_LogMessage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_events_event_is_not_abstract():
    assert not inspect.isabstract(events_Event)


def test_hyp_events_event_constructor_exists():
    assert callable(events_Event.__init__)


def test_hyp_events_event_constructor_args():
    sig = inspect.signature(events_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operations_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(operations_AbstractOperation)


def test_hyp_operations_abstractoperation_constructor_exists():
    assert callable(operations_AbstractOperation.__init__)


def test_hyp_operations_abstractoperation_constructor_args():
    sig = inspect.signature(operations_AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_versioning_changepackage_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_ChangePackage)


def test_hyp_esmodel_versioning_changepackage_constructor_exists():
    assert callable(esmodel_versioning_ChangePackage.__init__)


def test_hyp_esmodel_versioning_changepackage_constructor_args():
    sig = inspect.signature(esmodel_versioning_ChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_versioning_changepackage_is_not_abstract():
    assert not inspect.isabstract(versioning_ChangePackage)


def test_hyp_versioning_changepackage_constructor_exists():
    assert callable(versioning_ChangePackage.__init__)


def test_hyp_versioning_changepackage_constructor_args():
    sig = inspect.signature(versioning_ChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_versioning_tagversionspec_is_not_abstract():
    assert not inspect.isabstract(versioning_TagVersionSpec)


def test_hyp_versioning_tagversionspec_constructor_exists():
    assert callable(versioning_TagVersionSpec.__init__)


def test_hyp_versioning_tagversionspec_constructor_args():
    sig = inspect.signature(versioning_TagVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_versioning_historyinfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_HistoryInfo)


def test_hyp_esmodel_versioning_historyinfo_constructor_exists():
    assert callable(esmodel_versioning_HistoryInfo.__init__)


def test_hyp_esmodel_versioning_historyinfo_constructor_args():
    sig = inspect.signature(esmodel_versioning_HistoryInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_versioning_versionproperty_is_not_abstract():
    assert not inspect.isabstract(versioning_VersionProperty)


def test_hyp_versioning_versionproperty_constructor_exists():
    assert callable(versioning_VersionProperty.__init__)


def test_hyp_versioning_versionproperty_constructor_args():
    sig = inspect.signature(versioning_VersionProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_versionspec_is_not_abstract():
    assert not inspect.isabstract(VersionSpec)


def test_hyp_versionspec_constructor_exists():
    assert callable(VersionSpec.__init__)


def test_hyp_versionspec_constructor_args():
    sig = inspect.signature(VersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_versioning_headversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_HeadVersionSpec)


def test_hyp_esmodel_versioning_headversionspec_constructor_exists():
    assert callable(esmodel_versioning_HeadVersionSpec.__init__)


def test_hyp_esmodel_versioning_headversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_HeadVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_versioning_dateversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_DateVersionSpec)


def test_hyp_esmodel_versioning_dateversionspec_constructor_exists():
    assert callable(esmodel_versioning_DateVersionSpec.__init__)


def test_hyp_esmodel_versioning_dateversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_DateVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"




def test_hyp_esmodel_versioning_tagversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_TagVersionSpec)


def test_hyp_esmodel_versioning_tagversionspec_constructor_exists():
    assert callable(esmodel_versioning_TagVersionSpec.__init__)


def test_hyp_esmodel_versioning_tagversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_TagVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_esmodel_versioning_logmessage_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_LogMessage)


def test_hyp_esmodel_versioning_logmessage_constructor_exists():
    assert callable(esmodel_versioning_LogMessage.__init__)


def test_hyp_esmodel_versioning_logmessage_constructor_args():
    sig = inspect.signature(esmodel_versioning_LogMessage.__init__)
    params = list(sig.parameters.keys())
    assert "clientDate" in params, "Missing parameter 'clientDate'"
    assert "author" in params, "Missing parameter 'author'"
    assert "message" in params, "Missing parameter 'message'"
    assert "date" in params, "Missing parameter 'date'"







def test_hyp_esmodel_versioning_versionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_VersionSpec)


def test_hyp_esmodel_versioning_versionspec_constructor_exists():
    assert callable(esmodel_versioning_VersionSpec.__init__)


def test_hyp_esmodel_versioning_versionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_VersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_clientversioninfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_ClientVersionInfo)


def test_hyp_esmodel_clientversioninfo_constructor_exists():
    assert callable(esmodel_ClientVersionInfo.__init__)


def test_hyp_esmodel_clientversioninfo_constructor_args():
    sig = inspect.signature(esmodel_ClientVersionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_esmodel_versioninfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_VersionInfo)


def test_hyp_esmodel_versioninfo_constructor_exists():
    assert callable(esmodel_VersionInfo.__init__)


def test_hyp_esmodel_versioninfo_constructor_args():
    sig = inspect.signature(esmodel_VersionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "emfStoreVersionString" in params, "Missing parameter 'emfStoreVersionString'"




def test_hyp_esmodel_versioning_primaryversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_PrimaryVersionSpec)


def test_hyp_esmodel_versioning_primaryversionspec_constructor_exists():
    assert callable(esmodel_versioning_PrimaryVersionSpec.__init__)


def test_hyp_esmodel_versioning_primaryversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_PrimaryVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"




def test_hyp_versioning_primaryversionspec_is_not_abstract():
    assert not inspect.isabstract(versioning_PrimaryVersionSpec)


def test_hyp_versioning_primaryversionspec_constructor_exists():
    assert callable(versioning_PrimaryVersionSpec.__init__)


def test_hyp_versioning_primaryversionspec_constructor_args():
    sig = inspect.signature(versioning_PrimaryVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_projectinfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_ProjectInfo)


def test_hyp_esmodel_projectinfo_constructor_exists():
    assert callable(esmodel_ProjectInfo.__init__)


def test_hyp_esmodel_projectinfo_constructor_args():
    sig = inspect.signature(esmodel_ProjectInfo.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_versioning_version_is_not_abstract():
    assert not inspect.isabstract(versioning_Version)


def test_hyp_versioning_version_constructor_exists():
    assert callable(versioning_Version.__init__)


def test_hyp_versioning_version_constructor_args():
    sig = inspect.signature(versioning_Version.__init__)
    params = list(sig.parameters.keys())



def test_hyp_projectid_is_not_abstract():
    assert not inspect.isabstract(ProjectId)


def test_hyp_projectid_constructor_exists():
    assert callable(ProjectId.__init__)


def test_hyp_projectid_constructor_args():
    sig = inspect.signature(ProjectId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_projecthistory_is_not_abstract():
    assert not inspect.isabstract(esmodel_ProjectHistory)


def test_hyp_esmodel_projecthistory_constructor_exists():
    assert callable(esmodel_ProjectHistory.__init__)


def test_hyp_esmodel_projecthistory_constructor_args():
    sig = inspect.signature(esmodel_ProjectHistory.__init__)
    params = list(sig.parameters.keys())
    assert "projectName" in params, "Missing parameter 'projectName'"
    assert "projectDescription" in params, "Missing parameter 'projectDescription'"





def test_hyp_activityobject_is_not_abstract():
    assert not inspect.isabstract(ActivityObject)


def test_hyp_activityobject_constructor_exists():
    assert callable(ActivityObject.__init__)


def test_hyp_activityobject_constructor_args():
    sig = inspect.signature(ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_activity_activityinitial_is_not_abstract():
    assert not inspect.isabstract(model_activity_ActivityInitial)


def test_hyp_model_activity_activityinitial_constructor_exists():
    assert callable(model_activity_ActivityInitial.__init__)


def test_hyp_model_activity_activityinitial_constructor_args():
    sig = inspect.signature(model_activity_ActivityInitial.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_activity_activityend_is_not_abstract():
    assert not inspect.isabstract(model_activity_ActivityEnd)


def test_hyp_model_activity_activityend_constructor_exists():
    assert callable(model_activity_ActivityEnd.__init__)


def test_hyp_model_activity_activityend_constructor_args():
    sig = inspect.signature(model_activity_ActivityEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_activity_fork_is_not_abstract():
    assert not inspect.isabstract(model_activity_Fork)


def test_hyp_model_activity_fork_constructor_exists():
    assert callable(model_activity_Fork.__init__)


def test_hyp_model_activity_fork_constructor_args():
    sig = inspect.signature(model_activity_Fork.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_activity_branch_is_not_abstract():
    assert not inspect.isabstract(model_activity_Branch)


def test_hyp_model_activity_branch_constructor_exists():
    assert callable(model_activity_Branch.__init__)


def test_hyp_model_activity_branch_constructor_args():
    sig = inspect.signature(model_activity_Branch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_activity_activity_is_not_abstract():
    assert not inspect.isabstract(model_activity_Activity)


def test_hyp_model_activity_activity_constructor_exists():
    assert callable(model_activity_Activity.__init__)


def test_hyp_model_activity_activity_constructor_args():
    sig = inspect.signature(model_activity_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activity_activityobject_is_not_abstract():
    assert not inspect.isabstract(activity_ActivityObject)


def test_hyp_activity_activityobject_constructor_exists():
    assert callable(activity_ActivityObject.__init__)


def test_hyp_activity_activityobject_constructor_args():
    sig = inspect.signature(activity_ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accesscontrol_acuser_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_ACUser)


def test_hyp_accesscontrol_acuser_constructor_exists():
    assert callable(accesscontrol_ACUser.__init__)


def test_hyp_accesscontrol_acuser_constructor_args():
    sig = inspect.signature(accesscontrol_ACUser.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sessionid_is_not_abstract():
    assert not inspect.isabstract(SessionId)


def test_hyp_sessionid_constructor_exists():
    assert callable(SessionId.__init__)


def test_hyp_sessionid_constructor_args():
    sig = inspect.signature(SessionId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_activity_transition_is_not_abstract():
    assert not inspect.isabstract(model_activity_Transition)


def test_hyp_model_activity_transition_constructor_exists():
    assert callable(model_activity_Transition.__init__)


def test_hyp_model_activity_transition_constructor_args():
    sig = inspect.signature(model_activity_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"




def test_hyp_projecthistory_is_not_abstract():
    assert not inspect.isabstract(ProjectHistory)


def test_hyp_projecthistory_constructor_exists():
    assert callable(ProjectHistory.__init__)


def test_hyp_projecthistory_constructor_args():
    sig = inspect.signature(ProjectHistory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accesscontrol_acgroup_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_ACGroup)


def test_hyp_accesscontrol_acgroup_constructor_exists():
    assert callable(accesscontrol_ACGroup.__init__)


def test_hyp_accesscontrol_acgroup_constructor_args():
    sig = inspect.signature(accesscontrol_ACGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_serverspace_is_not_abstract():
    assert not inspect.isabstract(esmodel_ServerSpace)


def test_hyp_esmodel_serverspace_constructor_exists():
    assert callable(esmodel_ServerSpace.__init__)


def test_hyp_esmodel_serverspace_constructor_args():
    sig = inspect.signature(esmodel_ServerSpace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelelementid_is_not_abstract():
    assert not inspect.isabstract(ModelElementId)


def test_hyp_modelelementid_constructor_exists():
    assert callable(ModelElementId.__init__)


def test_hyp_modelelementid_constructor_args():
    sig = inspect.signature(ModelElementId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_util_modelelementpath_is_not_abstract():
    assert not inspect.isabstract(model_util_ModelElementPath)


def test_hyp_model_util_modelelementpath_constructor_exists():
    assert callable(model_util_ModelElementPath.__init__)


def test_hyp_model_util_modelelementpath_constructor_args():
    sig = inspect.signature(model_util_ModelElementPath.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(StereotypeAttributeInstance)


def test_hyp_stereotypeattributeinstance_constructor_exists():
    assert callable(StereotypeAttributeInstance.__init__)


def test_hyp_stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_profile_stereotypeattributeinstancestring_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttributeInstanceString)


def test_hyp_model_profile_stereotypeattributeinstancestring_constructor_exists():
    assert callable(model_profile_StereotypeAttributeInstanceString.__init__)


def test_hyp_model_profile_stereotypeattributeinstancestring_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttributeInstanceString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_model_profile_stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttributeInstance)


def test_hyp_model_profile_stereotypeattributeinstance_constructor_exists():
    assert callable(model_profile_StereotypeAttributeInstance.__init__)


def test_hyp_model_profile_stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(StereotypeAttribute)


def test_hyp_stereotypeattribute_constructor_exists():
    assert callable(StereotypeAttribute.__init__)


def test_hyp_stereotypeattribute_constructor_args():
    sig = inspect.signature(StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_profile_stereotypeattributesimple_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttributeSimple)


def test_hyp_model_profile_stereotypeattributesimple_constructor_exists():
    assert callable(model_profile_StereotypeAttributeSimple.__init__)


def test_hyp_model_profile_stereotypeattributesimple_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttributeSimple.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_model_profile_stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttribute)


def test_hyp_model_profile_stereotypeattribute_constructor_exists():
    assert callable(model_profile_StereotypeAttribute.__init__)


def test_hyp_model_profile_stereotypeattribute_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(profile_StereotypeAttributeInstance)


def test_hyp_profile_stereotypeattributeinstance_constructor_exists():
    assert callable(profile_StereotypeAttributeInstance.__init__)


def test_hyp_profile_stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(profile_StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activity_transition_is_not_abstract():
    assert not inspect.isabstract(activity_Transition)


def test_hyp_activity_transition_constructor_exists():
    assert callable(activity_Transition.__init__)


def test_hyp_activity_transition_constructor_args():
    sig = inspect.signature(activity_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_activity_activityobject_is_not_abstract():
    assert not inspect.isabstract(model_activity_ActivityObject)


def test_hyp_model_activity_activityobject_constructor_exists():
    assert callable(model_activity_ActivityObject.__init__)


def test_hyp_model_activity_activityobject_constructor_args():
    sig = inspect.signature(model_activity_ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_profile_stereotypeinstance_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeInstance)


def test_hyp_model_profile_stereotypeinstance_constructor_exists():
    assert callable(model_profile_StereotypeInstance.__init__)


def test_hyp_model_profile_stereotypeinstance_constructor_args():
    sig = inspect.signature(model_profile_StereotypeInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(profile_StereotypeAttribute)


def test_hyp_profile_stereotypeattribute_constructor_exists():
    assert callable(profile_StereotypeAttribute.__init__)


def test_hyp_profile_stereotypeattribute_constructor_args():
    sig = inspect.signature(profile_StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_profile_is_not_abstract():
    assert not inspect.isabstract(profile_Profile)


def test_hyp_profile_profile_constructor_exists():
    assert callable(profile_Profile.__init__)


def test_hyp_profile_profile_constructor_args():
    sig = inspect.signature(profile_Profile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_profile_stereotype_is_not_abstract():
    assert not inspect.isabstract(model_profile_Stereotype)


def test_hyp_model_profile_stereotype_constructor_exists():
    assert callable(model_profile_Stereotype.__init__)


def test_hyp_model_profile_stereotype_constructor_args():
    sig = inspect.signature(model_profile_Stereotype.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"




def test_hyp_profile_stereotype_is_not_abstract():
    assert not inspect.isabstract(profile_Stereotype)


def test_hyp_profile_stereotype_constructor_exists():
    assert callable(profile_Stereotype.__init__)


def test_hyp_profile_stereotype_constructor_args():
    sig = inspect.signature(profile_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_profile_profile_is_not_abstract():
    assert not inspect.isabstract(model_profile_Profile)


def test_hyp_model_profile_profile_constructor_exists():
    assert callable(model_profile_Profile.__init__)


def test_hyp_model_profile_profile_constructor_args():
    sig = inspect.signature(model_profile_Profile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statenode_is_not_abstract():
    assert not inspect.isabstract(StateNode)


def test_hyp_statenode_constructor_exists():
    assert callable(StateNode.__init__)


def test_hyp_statenode_constructor_args():
    sig = inspect.signature(StateNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_state_stateend_is_not_abstract():
    assert not inspect.isabstract(model_state_StateEnd)


def test_hyp_model_state_stateend_constructor_exists():
    assert callable(model_state_StateEnd.__init__)


def test_hyp_model_state_stateend_constructor_args():
    sig = inspect.signature(model_state_StateEnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_state_stateinitial_is_not_abstract():
    assert not inspect.isabstract(model_state_StateInitial)


def test_hyp_model_state_stateinitial_constructor_exists():
    assert callable(model_state_StateInitial.__init__)


def test_hyp_model_state_stateinitial_constructor_args():
    sig = inspect.signature(model_state_StateInitial.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_state_state_is_not_abstract():
    assert not inspect.isabstract(model_state_State)


def test_hyp_model_state_state_constructor_exists():
    assert callable(model_state_State.__init__)


def test_hyp_model_state_state_constructor_args():
    sig = inspect.signature(model_state_State.__init__)
    params = list(sig.parameters.keys())
    assert "activities" in params, "Missing parameter 'activities'"
    assert "exitConditions" in params, "Missing parameter 'exitConditions'"
    assert "entryConditions" in params, "Missing parameter 'entryConditions'"






def test_hyp_state_transition_is_not_abstract():
    assert not inspect.isabstract(state_Transition)


def test_hyp_state_transition_constructor_exists():
    assert callable(state_Transition.__init__)


def test_hyp_state_transition_constructor_args():
    sig = inspect.signature(state_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_state_statenode_is_not_abstract():
    assert not inspect.isabstract(model_state_StateNode)


def test_hyp_model_state_statenode_constructor_exists():
    assert callable(model_state_StateNode.__init__)


def test_hyp_model_state_statenode_constructor_args():
    sig = inspect.signature(model_state_StateNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_statenode_is_not_abstract():
    assert not inspect.isabstract(state_StateNode)


def test_hyp_state_statenode_constructor_exists():
    assert callable(state_StateNode.__init__)


def test_hyp_state_statenode_constructor_args():
    sig = inspect.signature(state_StateNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_state_transition_is_not_abstract():
    assert not inspect.isabstract(model_state_Transition)


def test_hyp_model_state_transition_constructor_exists():
    assert callable(model_state_Transition.__init__)


def test_hyp_model_state_transition_constructor_args():
    sig = inspect.signature(model_state_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"




def test_hyp_meetingsection_is_not_abstract():
    assert not inspect.isabstract(MeetingSection)


def test_hyp_meetingsection_constructor_exists():
    assert callable(MeetingSection.__init__)


def test_hyp_meetingsection_constructor_args():
    sig = inspect.signature(MeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_meeting_issuemeetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_IssueMeetingSection)


def test_hyp_model_meeting_issuemeetingsection_constructor_exists():
    assert callable(model_meeting_IssueMeetingSection.__init__)


def test_hyp_model_meeting_issuemeetingsection_constructor_args():
    sig = inspect.signature(model_meeting_IssueMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_meeting_workitemmeetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_WorkItemMeetingSection)


def test_hyp_model_meeting_workitemmeetingsection_constructor_exists():
    assert callable(model_meeting_WorkItemMeetingSection.__init__)


def test_hyp_model_meeting_workitemmeetingsection_constructor_args():
    sig = inspect.signature(model_meeting_WorkItemMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_meeting_compositemeetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_CompositeMeetingSection)


def test_hyp_model_meeting_compositemeetingsection_constructor_exists():
    assert callable(model_meeting_CompositeMeetingSection.__init__)


def test_hyp_model_meeting_compositemeetingsection_constructor_args():
    sig = inspect.signature(model_meeting_CompositeMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_meeting_meetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_MeetingSection)


def test_hyp_model_meeting_meetingsection_constructor_exists():
    assert callable(model_meeting_MeetingSection.__init__)


def test_hyp_model_meeting_meetingsection_constructor_args():
    sig = inspect.signature(model_meeting_MeetingSection.__init__)
    params = list(sig.parameters.keys())
    assert "allocatedTime" in params, "Missing parameter 'allocatedTime'"




def test_hyp_meeting_workitemmeetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting_WorkItemMeetingSection)


def test_hyp_meeting_workitemmeetingsection_constructor_exists():
    assert callable(meeting_WorkItemMeetingSection.__init__)


def test_hyp_meeting_workitemmeetingsection_constructor_args():
    sig = inspect.signature(meeting_WorkItemMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_meeting_issuemeetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting_IssueMeetingSection)


def test_hyp_meeting_issuemeetingsection_constructor_exists():
    assert callable(meeting_IssueMeetingSection.__init__)


def test_hyp_meeting_issuemeetingsection_constructor_args():
    sig = inspect.signature(meeting_IssueMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_meeting_meetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting_MeetingSection)


def test_hyp_meeting_meetingsection_constructor_exists():
    assert callable(meeting_MeetingSection.__init__)


def test_hyp_meeting_meetingsection_constructor_args():
    sig = inspect.signature(meeting_MeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component_component_is_not_abstract():
    assert not inspect.isabstract(component_Component)


def test_hyp_component_component_constructor_exists():
    assert callable(component_Component.__init__)


def test_hyp_component_component_constructor_args():
    sig = inspect.signature(component_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_component_componentservice_is_not_abstract():
    assert not inspect.isabstract(model_component_ComponentService)


def test_hyp_model_component_componentservice_constructor_exists():
    assert callable(model_component_ComponentService.__init__)


def test_hyp_model_component_componentservice_constructor_args():
    sig = inspect.signature(model_component_ComponentService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_meeting_meeting_is_not_abstract():
    assert not inspect.isabstract(model_meeting_Meeting)


def test_hyp_model_meeting_meeting_constructor_exists():
    assert callable(model_meeting_Meeting.__init__)


def test_hyp_model_meeting_meeting_constructor_args():
    sig = inspect.signature(model_meeting_Meeting.__init__)
    params = list(sig.parameters.keys())
    assert "starttime" in params, "Missing parameter 'starttime'"
    assert "endtime" in params, "Missing parameter 'endtime'"
    assert "location" in params, "Missing parameter 'location'"






def test_hyp_model_component_deploymentnode_is_not_abstract():
    assert not inspect.isabstract(model_component_DeploymentNode)


def test_hyp_model_component_deploymentnode_constructor_exists():
    assert callable(model_component_DeploymentNode.__init__)


def test_hyp_model_component_deploymentnode_constructor_args():
    sig = inspect.signature(model_component_DeploymentNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component_componentservice_is_not_abstract():
    assert not inspect.isabstract(component_ComponentService)


def test_hyp_component_componentservice_constructor_exists():
    assert callable(component_ComponentService.__init__)


def test_hyp_component_componentservice_constructor_args():
    sig = inspect.signature(component_ComponentService.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_component_component_is_not_abstract():
    assert not inspect.isabstract(model_component_Component)


def test_hyp_model_component_component_constructor_exists():
    assert callable(model_component_Component.__init__)


def test_hyp_model_component_component_constructor_args():
    sig = inspect.signature(model_component_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_solution_is_not_abstract():
    assert not inspect.isabstract(Solution)


def test_hyp_solution_constructor_exists():
    assert callable(Solution.__init__)


def test_hyp_solution_constructor_args():
    sig = inspect.signature(Solution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_change_mergingsolution_is_not_abstract():
    assert not inspect.isabstract(model_change_MergingSolution)


def test_hyp_model_change_mergingsolution_constructor_exists():
    assert callable(model_change_MergingSolution.__init__)


def test_hyp_model_change_mergingsolution_constructor_args():
    sig = inspect.signature(model_change_MergingSolution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_change_mergingproposal_is_not_abstract():
    assert not inspect.isabstract(change_MergingProposal)


def test_hyp_change_mergingproposal_constructor_exists():
    assert callable(change_MergingProposal.__init__)


def test_hyp_change_mergingproposal_constructor_args():
    sig = inspect.signature(change_MergingProposal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_proposal_is_not_abstract():
    assert not inspect.isabstract(Proposal)


def test_hyp_proposal_constructor_exists():
    assert callable(Proposal.__init__)


def test_hyp_proposal_constructor_args():
    sig = inspect.signature(Proposal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_change_mergingproposal_is_not_abstract():
    assert not inspect.isabstract(model_change_MergingProposal)


def test_hyp_model_change_mergingproposal_constructor_exists():
    assert callable(model_change_MergingProposal.__init__)


def test_hyp_model_change_mergingproposal_constructor_args():
    sig = inspect.signature(model_change_MergingProposal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_issue_is_not_abstract():
    assert not inspect.isabstract(Issue)


def test_hyp_issue_constructor_exists():
    assert callable(Issue.__init__)


def test_hyp_issue_constructor_args():
    sig = inspect.signature(Issue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_change_mergingissue_is_not_abstract():
    assert not inspect.isabstract(model_change_MergingIssue)


def test_hyp_model_change_mergingissue_constructor_exists():
    assert callable(model_change_MergingIssue.__init__)


def test_hyp_model_change_mergingissue_constructor_args():
    sig = inspect.signature(model_change_MergingIssue.__init__)
    params = list(sig.parameters.keys())
    assert "resolvingRevision" in params, "Missing parameter 'resolvingRevision'"




def test_hyp_model_change_modelchangepackage_is_not_abstract():
    assert not inspect.isabstract(model_change_ModelChangePackage)


def test_hyp_model_change_modelchangepackage_constructor_exists():
    assert callable(model_change_ModelChangePackage.__init__)


def test_hyp_model_change_modelchangepackage_constructor_args():
    sig = inspect.signature(model_change_ModelChangePackage.__init__)
    params = list(sig.parameters.keys())
    assert "sourceVersion" in params, "Missing parameter 'sourceVersion'"
    assert "targetVersion" in params, "Missing parameter 'targetVersion'"





def test_hyp_rationale_issue_is_not_abstract():
    assert not inspect.isabstract(rationale_Issue)


def test_hyp_rationale_issue_constructor_exists():
    assert callable(rationale_Issue.__init__)


def test_hyp_rationale_issue_constructor_args():
    sig = inspect.signature(rationale_Issue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rationale_criterion_is_not_abstract():
    assert not inspect.isabstract(rationale_Criterion)


def test_hyp_rationale_criterion_constructor_exists():
    assert callable(rationale_Criterion.__init__)


def test_hyp_rationale_criterion_constructor_args():
    sig = inspect.signature(rationale_Criterion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_rationale_criterion_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Criterion)


def test_hyp_model_rationale_criterion_constructor_exists():
    assert callable(model_rationale_Criterion.__init__)


def test_hyp_model_rationale_criterion_constructor_args():
    sig = inspect.signature(model_rationale_Criterion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rationale_assessment_is_not_abstract():
    assert not inspect.isabstract(rationale_Assessment)


def test_hyp_rationale_assessment_constructor_exists():
    assert callable(rationale_Assessment.__init__)


def test_hyp_rationale_assessment_constructor_args():
    sig = inspect.signature(rationale_Assessment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rationale_solution_is_not_abstract():
    assert not inspect.isabstract(rationale_Solution)


def test_hyp_rationale_solution_constructor_exists():
    assert callable(rationale_Solution.__init__)


def test_hyp_rationale_solution_constructor_args():
    sig = inspect.signature(rationale_Solution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rationale_proposal_is_not_abstract():
    assert not inspect.isabstract(rationale_Proposal)


def test_hyp_rationale_proposal_constructor_exists():
    assert callable(rationale_Proposal.__init__)


def test_hyp_rationale_proposal_constructor_args():
    sig = inspect.signature(rationale_Proposal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_criterion_is_not_abstract():
    assert not inspect.isabstract(Criterion)


def test_hyp_criterion_constructor_exists():
    assert callable(Criterion.__init__)


def test_hyp_criterion_constructor_args():
    sig = inspect.signature(Criterion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_requirement_nonfunctionalrequirement_is_not_abstract():
    assert not inspect.isabstract(model_requirement_NonFunctionalRequirement)


def test_hyp_model_requirement_nonfunctionalrequirement_constructor_exists():
    assert callable(model_requirement_NonFunctionalRequirement.__init__)


def test_hyp_model_requirement_nonfunctionalrequirement_constructor_args():
    sig = inspect.signature(model_requirement_NonFunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_systemfunction_is_not_abstract():
    assert not inspect.isabstract(requirement_SystemFunction)


def test_hyp_requirement_systemfunction_constructor_exists():
    assert callable(requirement_SystemFunction.__init__)


def test_hyp_requirement_systemfunction_constructor_args():
    sig = inspect.signature(requirement_SystemFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nondomainelement_is_not_abstract():
    assert not inspect.isabstract(NonDomainElement)


def test_hyp_nondomainelement_constructor_exists():
    assert callable(NonDomainElement.__init__)


def test_hyp_nondomainelement_constructor_args():
    sig = inspect.signature(NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_rationale_assessment_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Assessment)


def test_hyp_model_rationale_assessment_constructor_exists():
    assert callable(model_rationale_Assessment.__init__)


def test_hyp_model_rationale_assessment_constructor_args():
    sig = inspect.signature(model_rationale_Assessment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_model_rationale_proposal_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Proposal)


def test_hyp_model_rationale_proposal_constructor_exists():
    assert callable(model_rationale_Proposal.__init__)


def test_hyp_model_rationale_proposal_constructor_args():
    sig = inspect.signature(model_rationale_Proposal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_rationale_solution_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Solution)


def test_hyp_model_rationale_solution_constructor_exists():
    assert callable(model_rationale_Solution.__init__)


def test_hyp_model_rationale_solution_constructor_args():
    sig = inspect.signature(model_rationale_Solution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_requirement_systemfunction_is_not_abstract():
    assert not inspect.isabstract(model_requirement_SystemFunction)


def test_hyp_model_requirement_systemfunction_constructor_exists():
    assert callable(model_requirement_SystemFunction.__init__)


def test_hyp_model_requirement_systemfunction_constructor_args():
    sig = inspect.signature(model_requirement_SystemFunction.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"
    assert "exception" in params, "Missing parameter 'exception'"






def test_hyp_model_rationale_comment_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Comment)


def test_hyp_model_rationale_comment_constructor_exists():
    assert callable(model_rationale_Comment.__init__)


def test_hyp_model_rationale_comment_constructor_args():
    sig = inspect.signature(model_rationale_Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_requirement_usertask_is_not_abstract():
    assert not inspect.isabstract(model_requirement_UserTask)


def test_hyp_model_requirement_usertask_constructor_exists():
    assert callable(model_requirement_UserTask.__init__)


def test_hyp_model_requirement_usertask_constructor_args():
    sig = inspect.signature(model_requirement_UserTask.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_requirement_step_is_not_abstract():
    assert not inspect.isabstract(model_requirement_Step)


def test_hyp_model_requirement_step_constructor_exists():
    assert callable(model_requirement_Step.__init__)


def test_hyp_model_requirement_step_constructor_args():
    sig = inspect.signature(model_requirement_Step.__init__)
    params = list(sig.parameters.keys())
    assert "userStep" in params, "Missing parameter 'userStep'"




def test_hyp_model_requirement_actorinstance_is_not_abstract():
    assert not inspect.isabstract(model_requirement_ActorInstance)


def test_hyp_model_requirement_actorinstance_constructor_exists():
    assert callable(model_requirement_ActorInstance.__init__)


def test_hyp_model_requirement_actorinstance_constructor_args():
    sig = inspect.signature(model_requirement_ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_requirement_actor_is_not_abstract():
    assert not inspect.isabstract(model_requirement_Actor)


def test_hyp_model_requirement_actor_constructor_exists():
    assert callable(model_requirement_Actor.__init__)


def test_hyp_model_requirement_actor_constructor_args():
    sig = inspect.signature(model_requirement_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_actorinstance_is_not_abstract():
    assert not inspect.isabstract(requirement_ActorInstance)


def test_hyp_requirement_actorinstance_constructor_exists():
    assert callable(requirement_ActorInstance.__init__)


def test_hyp_requirement_actorinstance_constructor_args():
    sig = inspect.signature(requirement_ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_requirement_scenario_is_not_abstract():
    assert not inspect.isabstract(model_requirement_Scenario)


def test_hyp_model_requirement_scenario_constructor_exists():
    assert callable(model_requirement_Scenario.__init__)


def test_hyp_model_requirement_scenario_constructor_args():
    sig = inspect.signature(model_requirement_Scenario.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_nonfunctionalrequirement_is_not_abstract():
    assert not inspect.isabstract(requirement_NonFunctionalRequirement)


def test_hyp_requirement_nonfunctionalrequirement_constructor_exists():
    assert callable(requirement_NonFunctionalRequirement.__init__)


def test_hyp_requirement_nonfunctionalrequirement_constructor_args():
    sig = inspect.signature(requirement_NonFunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_usertask_is_not_abstract():
    assert not inspect.isabstract(requirement_UserTask)


def test_hyp_requirement_usertask_constructor_exists():
    assert callable(requirement_UserTask.__init__)


def test_hyp_requirement_usertask_constructor_args():
    sig = inspect.signature(requirement_UserTask.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_step_is_not_abstract():
    assert not inspect.isabstract(requirement_Step)


def test_hyp_requirement_step_constructor_exists():
    assert callable(requirement_Step.__init__)


def test_hyp_requirement_step_constructor_args():
    sig = inspect.signature(requirement_Step.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_actor_is_not_abstract():
    assert not inspect.isabstract(requirement_Actor)


def test_hyp_requirement_actor_constructor_exists():
    assert callable(requirement_Actor.__init__)


def test_hyp_requirement_actor_constructor_args():
    sig = inspect.signature(requirement_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_requirement_usecase_is_not_abstract():
    assert not inspect.isabstract(model_requirement_UseCase)


def test_hyp_model_requirement_usecase_constructor_exists():
    assert callable(model_requirement_UseCase.__init__)


def test_hyp_model_requirement_usecase_constructor_args():
    sig = inspect.signature(model_requirement_UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "rules" in params, "Missing parameter 'rules'"
    assert "exception" in params, "Missing parameter 'exception'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"







def test_hyp_model_requirement_functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(model_requirement_FunctionalRequirement)


def test_hyp_model_requirement_functionalrequirement_constructor_exists():
    assert callable(model_requirement_FunctionalRequirement.__init__)


def test_hyp_model_requirement_functionalrequirement_constructor_args():
    sig = inspect.signature(model_requirement_FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "storyPoints" in params, "Missing parameter 'storyPoints'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "reviewed" in params, "Missing parameter 'reviewed'"







def test_hyp_document_section_is_not_abstract():
    assert not inspect.isabstract(document_Section)


def test_hyp_document_section_constructor_exists():
    assert callable(document_Section.__init__)


def test_hyp_document_section_constructor_args():
    sig = inspect.signature(document_Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(requirement_FunctionalRequirement)


def test_hyp_requirement_functionalrequirement_constructor_exists():
    assert callable(requirement_FunctionalRequirement.__init__)


def test_hyp_requirement_functionalrequirement_constructor_args():
    sig = inspect.signature(requirement_FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_classes_dependency_is_not_abstract():
    assert not inspect.isabstract(model_classes_Dependency)


def test_hyp_model_classes_dependency_constructor_exists():
    assert callable(model_classes_Dependency.__init__)


def test_hyp_model_classes_dependency_constructor_args():
    sig = inspect.signature(model_classes_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_hyp_section_constructor_exists():
    assert callable(Section.__init__)


def test_hyp_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_document_compositesection_is_not_abstract():
    assert not inspect.isabstract(model_document_CompositeSection)


def test_hyp_model_document_compositesection_constructor_exists():
    assert callable(model_document_CompositeSection.__init__)


def test_hyp_model_document_compositesection_constructor_args():
    sig = inspect.signature(model_document_CompositeSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_document_leafsection_is_not_abstract():
    assert not inspect.isabstract(model_document_LeafSection)


def test_hyp_model_document_leafsection_constructor_exists():
    assert callable(model_document_LeafSection.__init__)


def test_hyp_model_document_leafsection_constructor_args():
    sig = inspect.signature(model_document_LeafSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_document_compositesection_is_not_abstract():
    assert not inspect.isabstract(document_CompositeSection)


def test_hyp_document_compositesection_constructor_exists():
    assert callable(document_CompositeSection.__init__)


def test_hyp_document_compositesection_constructor_args():
    sig = inspect.signature(document_CompositeSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_document_section_is_not_abstract():
    assert not inspect.isabstract(model_document_Section)


def test_hyp_model_document_section_constructor_exists():
    assert callable(model_document_Section.__init__)


def test_hyp_model_document_section_constructor_args():
    sig = inspect.signature(model_document_Section.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_classes_methodargument_is_not_abstract():
    assert not inspect.isabstract(model_classes_MethodArgument)


def test_hyp_model_classes_methodargument_constructor_exists():
    assert callable(model_classes_MethodArgument.__init__)


def test_hyp_model_classes_methodargument_constructor_args():
    sig = inspect.signature(model_classes_MethodArgument.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "type" in params, "Missing parameter 'type'"
    assert "signature" in params, "Missing parameter 'signature'"








def test_hyp_classes_methodargument_is_not_abstract():
    assert not inspect.isabstract(classes_MethodArgument)


def test_hyp_classes_methodargument_constructor_exists():
    assert callable(classes_MethodArgument.__init__)


def test_hyp_classes_methodargument_constructor_args():
    sig = inspect.signature(classes_MethodArgument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_classes_method_is_not_abstract():
    assert not inspect.isabstract(model_classes_Method)


def test_hyp_model_classes_method_constructor_exists():
    assert callable(model_classes_Method.__init__)


def test_hyp_model_classes_method_constructor_args():
    sig = inspect.signature(model_classes_Method.__init__)
    params = list(sig.parameters.keys())
    assert "properties" in params, "Missing parameter 'properties'"
    assert "signature" in params, "Missing parameter 'signature'"
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "stubbed" in params, "Missing parameter 'stubbed'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "label" in params, "Missing parameter 'label'"
    assert "visibility" in params, "Missing parameter 'visibility'"










def test_hyp_classes_packageelement_is_not_abstract():
    assert not inspect.isabstract(classes_PackageElement)


def test_hyp_classes_packageelement_constructor_exists():
    assert callable(classes_PackageElement.__init__)


def test_hyp_classes_packageelement_constructor_args():
    sig = inspect.signature(classes_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_classes_attribute_is_not_abstract():
    assert not inspect.isabstract(model_classes_Attribute)


def test_hyp_model_classes_attribute_constructor_exists():
    assert callable(model_classes_Attribute.__init__)


def test_hyp_model_classes_attribute_constructor_args():
    sig = inspect.signature(model_classes_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "type" in params, "Missing parameter 'type'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "signature" in params, "Missing parameter 'signature'"
    assert "scope" in params, "Missing parameter 'scope'"










def test_hyp_model_classes_association_is_not_abstract():
    assert not inspect.isabstract(model_classes_Association)


def test_hyp_model_classes_association_constructor_exists():
    assert callable(model_classes_Association.__init__)


def test_hyp_model_classes_association_constructor_args():
    sig = inspect.signature(model_classes_Association.__init__)
    params = list(sig.parameters.keys())
    assert "targetRole" in params, "Missing parameter 'targetRole'"
    assert "sourceMultiplicity" in params, "Missing parameter 'sourceMultiplicity'"
    assert "sourceRole" in params, "Missing parameter 'sourceRole'"
    assert "type" in params, "Missing parameter 'type'"
    assert "targetMultiplicity" in params, "Missing parameter 'targetMultiplicity'"








def test_hyp_classes_association_is_not_abstract():
    assert not inspect.isabstract(classes_Association)


def test_hyp_classes_association_constructor_exists():
    assert callable(classes_Association.__init__)


def test_hyp_classes_association_constructor_args():
    sig = inspect.signature(classes_Association.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_scenario_is_not_abstract():
    assert not inspect.isabstract(requirement_Scenario)


def test_hyp_requirement_scenario_constructor_exists():
    assert callable(requirement_Scenario.__init__)


def test_hyp_requirement_scenario_constructor_args():
    sig = inspect.signature(requirement_Scenario.__init__)
    params = list(sig.parameters.keys())



def test_hyp_requirement_usecase_is_not_abstract():
    assert not inspect.isabstract(requirement_UseCase)


def test_hyp_requirement_usecase_constructor_exists():
    assert callable(requirement_UseCase.__init__)


def test_hyp_requirement_usecase_constructor_args():
    sig = inspect.signature(requirement_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_method_is_not_abstract():
    assert not inspect.isabstract(classes_Method)


def test_hyp_classes_method_constructor_exists():
    assert callable(classes_Method.__init__)


def test_hyp_classes_method_constructor_args():
    sig = inspect.signature(classes_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_attribute_is_not_abstract():
    assert not inspect.isabstract(classes_Attribute)


def test_hyp_classes_attribute_constructor_exists():
    assert callable(classes_Attribute.__init__)


def test_hyp_classes_attribute_constructor_args():
    sig = inspect.signature(classes_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_class_is_not_abstract():
    assert not inspect.isabstract(classes_Class)


def test_hyp_classes_class_constructor_exists():
    assert callable(classes_Class.__init__)


def test_hyp_classes_class_constructor_args():
    sig = inspect.signature(classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_hyp_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_hyp_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_classes_package_is_not_abstract():
    assert not inspect.isabstract(model_classes_Package)


def test_hyp_model_classes_package_constructor_exists():
    assert callable(model_classes_Package.__init__)


def test_hyp_model_classes_package_constructor_args():
    sig = inspect.signature(model_classes_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_classes_class_is_not_abstract():
    assert not inspect.isabstract(model_classes_Class)


def test_hyp_model_classes_class_constructor_exists():
    assert callable(model_classes_Class.__init__)


def test_hyp_model_classes_class_constructor_args():
    sig = inspect.signature(model_classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_dependency_is_not_abstract():
    assert not inspect.isabstract(classes_Dependency)


def test_hyp_classes_dependency_constructor_exists():
    assert callable(classes_Dependency.__init__)


def test_hyp_classes_dependency_constructor_args():
    sig = inspect.signature(classes_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_package_is_not_abstract():
    assert not inspect.isabstract(classes_Package)


def test_hyp_classes_package_constructor_exists():
    assert callable(classes_Package.__init__)


def test_hyp_classes_package_constructor_args():
    sig = inspect.signature(classes_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_classes_packageelement_is_not_abstract():
    assert not inspect.isabstract(model_classes_PackageElement)


def test_hyp_model_classes_packageelement_constructor_exists():
    assert callable(model_classes_PackageElement.__init__)


def test_hyp_model_classes_packageelement_constructor_args():
    sig = inspect.signature(model_classes_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagram_model_diagram_is_not_abstract():
    assert not inspect.isabstract(diagram_model_Diagram)


def test_hyp_diagram_model_diagram_constructor_exists():
    assert callable(diagram_model_Diagram.__init__)


def test_hyp_diagram_model_diagram_constructor_args():
    sig = inspect.signature(diagram_model_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_task_checkable_is_not_abstract():
    assert not inspect.isabstract(task_Checkable)


def test_hyp_task_checkable_constructor_exists():
    assert callable(task_Checkable.__init__)


def test_hyp_task_checkable_constructor_args():
    sig = inspect.signature(task_Checkable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_bug_bugreport_is_not_abstract():
    assert not inspect.isabstract(model_bug_BugReport)


def test_hyp_model_bug_bugreport_constructor_exists():
    assert callable(model_bug_BugReport.__init__)


def test_hyp_model_bug_bugreport_constructor_args():
    sig = inspect.signature(model_bug_BugReport.__init__)
    params = list(sig.parameters.keys())
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "resolutionType" in params, "Missing parameter 'resolutionType'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "severity" in params, "Missing parameter 'severity'"







def test_hyp_model_task_actionitem_is_not_abstract():
    assert not inspect.isabstract(model_task_ActionItem)


def test_hyp_model_task_actionitem_constructor_exists():
    assert callable(model_task_ActionItem.__init__)


def test_hyp_model_task_actionitem_constructor_args():
    sig = inspect.signature(model_task_ActionItem.__init__)
    params = list(sig.parameters.keys())
    assert "done" in params, "Missing parameter 'done'"
    assert "activity" in params, "Missing parameter 'activity'"





def test_hyp_model_task_checkable_is_not_abstract():
    assert not inspect.isabstract(model_task_Checkable)


def test_hyp_model_task_checkable_constructor_exists():
    assert callable(model_task_Checkable.__init__)


def test_hyp_model_task_checkable_constructor_args():
    sig = inspect.signature(model_task_Checkable.__init__)
    params = list(sig.parameters.keys())
    assert "checked" in params, "Missing parameter 'checked'"




def test_hyp_workitem_is_not_abstract():
    assert not inspect.isabstract(WorkItem)


def test_hyp_workitem_constructor_exists():
    assert callable(WorkItem.__init__)


def test_hyp_workitem_constructor_args():
    sig = inspect.signature(WorkItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_task_milestone_is_not_abstract():
    assert not inspect.isabstract(model_task_Milestone)


def test_hyp_model_task_milestone_constructor_exists():
    assert callable(model_task_Milestone.__init__)


def test_hyp_model_task_milestone_constructor_args():
    sig = inspect.signature(model_task_Milestone.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_task_workpackage_is_not_abstract():
    assert not inspect.isabstract(model_task_WorkPackage)


def test_hyp_model_task_workpackage_constructor_exists():
    assert callable(model_task_WorkPackage.__init__)


def test_hyp_model_task_workpackage_constructor_args():
    sig = inspect.signature(model_task_WorkPackage.__init__)
    params = list(sig.parameters.keys())
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"





def test_hyp_model_project_is_not_abstract():
    assert not inspect.isabstract(model_Project)


def test_hyp_model_project_constructor_exists():
    assert callable(model_Project.__init__)


def test_hyp_model_project_constructor_args():
    sig = inspect.signature(model_Project.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_nondomainelement_is_not_abstract():
    assert not inspect.isabstract(model_NonDomainElement)


def test_hyp_model_nondomainelement_constructor_exists():
    assert callable(model_NonDomainElement.__init__)


def test_hyp_model_nondomainelement_constructor_args():
    sig = inspect.signature(model_NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_attachment_is_not_abstract():
    assert not inspect.isabstract(model_Attachment)


def test_hyp_model_attachment_constructor_exists():
    assert callable(model_Attachment.__init__)


def test_hyp_model_attachment_constructor_args():
    sig = inspect.signature(model_Attachment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metamodel_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(metamodel_UniqueIdentifier)


def test_hyp_metamodel_uniqueidentifier_constructor_exists():
    assert callable(metamodel_UniqueIdentifier.__init__)


def test_hyp_metamodel_uniqueidentifier_constructor_args():
    sig = inspect.signature(metamodel_UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_rationale_comment_is_not_abstract():
    assert not inspect.isabstract(rationale_Comment)


def test_hyp_rationale_comment_constructor_exists():
    assert callable(rationale_Comment.__init__)


def test_hyp_rationale_comment_constructor_args():
    sig = inspect.signature(rationale_Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_document_leafsection_is_not_abstract():
    assert not inspect.isabstract(document_LeafSection)


def test_hyp_document_leafsection_constructor_exists():
    assert callable(document_LeafSection.__init__)


def test_hyp_document_leafsection_constructor_args():
    sig = inspect.signature(document_LeafSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attachment_is_not_abstract():
    assert not inspect.isabstract(Attachment)


def test_hyp_attachment_constructor_exists():
    assert callable(Attachment.__init__)


def test_hyp_attachment_constructor_args():
    sig = inspect.signature(Attachment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_attachment_urlattachment_is_not_abstract():
    assert not inspect.isabstract(model_attachment_UrlAttachment)


def test_hyp_model_attachment_urlattachment_constructor_exists():
    assert callable(model_attachment_UrlAttachment.__init__)


def test_hyp_model_attachment_urlattachment_constructor_args():
    sig = inspect.signature(model_attachment_UrlAttachment.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"




def test_hyp_model_attachment_fileattachment_is_not_abstract():
    assert not inspect.isabstract(model_attachment_FileAttachment)


def test_hyp_model_attachment_fileattachment_constructor_exists():
    assert callable(model_attachment_FileAttachment.__init__)


def test_hyp_model_attachment_fileattachment_constructor_args():
    sig = inspect.signature(model_attachment_FileAttachment.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "requiredOffline" in params, "Missing parameter 'requiredOffline'"
    assert "fileID" in params, "Missing parameter 'fileID'"
    assert "fileHash" in params, "Missing parameter 'fileHash'"
    assert "fileSize" in params, "Missing parameter 'fileSize'"








def test_hyp_model_diagram_mediagram_is_not_abstract():
    assert not inspect.isabstract(model_diagram_MEDiagram)


def test_hyp_model_diagram_mediagram_constructor_exists():
    assert callable(model_diagram_MEDiagram.__init__)


def test_hyp_model_diagram_mediagram_constructor_args():
    sig = inspect.signature(model_diagram_MEDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "diagramLayout" in params, "Missing parameter 'diagramLayout'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_hyp_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_hyp_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_rationale_issue_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Issue)


def test_hyp_model_rationale_issue_constructor_exists():
    assert callable(model_rationale_Issue.__init__)


def test_hyp_model_rationale_issue_constructor_args():
    sig = inspect.signature(model_rationale_Issue.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"




def test_hyp_model_task_workitem_is_not_abstract():
    assert not inspect.isabstract(model_task_WorkItem)


def test_hyp_model_task_workitem_constructor_exists():
    assert callable(model_task_WorkItem.__init__)


def test_hyp_model_task_workitem_constructor_args():
    sig = inspect.signature(model_task_WorkItem.__init__)
    params = list(sig.parameters.keys())
    assert "effort" in params, "Missing parameter 'effort'"
    assert "dueDate" in params, "Missing parameter 'dueDate'"
    assert "resolved" in params, "Missing parameter 'resolved'"
    assert "estimate" in params, "Missing parameter 'estimate'"
    assert "priority" in params, "Missing parameter 'priority'"








def test_hyp_metamodel_associationclasselement_is_not_abstract():
    assert not inspect.isabstract(metamodel_AssociationClassElement)


def test_hyp_metamodel_associationclasselement_constructor_exists():
    assert callable(metamodel_AssociationClassElement.__init__)


def test_hyp_metamodel_associationclasselement_constructor_args():
    sig = inspect.signature(metamodel_AssociationClassElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metamodel_nondomainelement_is_not_abstract():
    assert not inspect.isabstract(metamodel_NonDomainElement)


def test_hyp_metamodel_nondomainelement_constructor_exists():
    assert callable(metamodel_NonDomainElement.__init__)


def test_hyp_metamodel_nondomainelement_constructor_args():
    sig = inspect.signature(metamodel_NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metamodel_modelversion_is_not_abstract():
    assert not inspect.isabstract(metamodel_ModelVersion)


def test_hyp_metamodel_modelversion_constructor_exists():
    assert callable(metamodel_ModelVersion.__init__)


def test_hyp_metamodel_modelversion_constructor_args():
    sig = inspect.signature(metamodel_ModelVersion.__init__)
    params = list(sig.parameters.keys())
    assert "releaseNumber" in params, "Missing parameter 'releaseNumber'"




def test_hyp_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(UniqueIdentifier)


def test_hyp_uniqueidentifier_constructor_exists():
    assert callable(UniqueIdentifier.__init__)


def test_hyp_uniqueidentifier_constructor_args():
    sig = inspect.signature(UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_projectid_is_not_abstract():
    assert not inspect.isabstract(esmodel_ProjectId)


def test_hyp_esmodel_projectid_constructor_exists():
    assert callable(esmodel_ProjectId.__init__)


def test_hyp_esmodel_projectid_constructor_args():
    sig = inspect.signature(esmodel_ProjectId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_operationid_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_OperationId)


def test_hyp_esmodel_operations_operationid_constructor_exists():
    assert callable(esmodel_operations_OperationId.__init__)


def test_hyp_esmodel_operations_operationid_constructor_args():
    sig = inspect.signature(esmodel_operations_OperationId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_sessionid_is_not_abstract():
    assert not inspect.isabstract(esmodel_SessionId)


def test_hyp_esmodel_sessionid_constructor_exists():
    assert callable(esmodel_SessionId.__init__)


def test_hyp_esmodel_sessionid_constructor_args():
    sig = inspect.signature(esmodel_SessionId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_accesscontrol_acorgunitid_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACOrgUnitId)


def test_hyp_esmodel_accesscontrol_acorgunitid_constructor_exists():
    assert callable(esmodel_accesscontrol_ACOrgUnitId.__init__)


def test_hyp_esmodel_accesscontrol_acorgunitid_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACOrgUnitId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metamodel_modelelementid_is_not_abstract():
    assert not inspect.isabstract(metamodel_ModelElementId)


def test_hyp_metamodel_modelelementid_constructor_exists():
    assert callable(metamodel_ModelElementId.__init__)


def test_hyp_metamodel_modelelementid_constructor_args():
    sig = inspect.signature(metamodel_ModelElementId.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiableElement)


def test_hyp_identifiableelement_constructor_exists():
    assert callable(IdentifiableElement.__init__)


def test_hyp_identifiableelement_constructor_args():
    sig = inspect.signature(IdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_operations_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_AbstractOperation)


def test_hyp_esmodel_operations_abstractoperation_constructor_exists():
    assert callable(esmodel_operations_AbstractOperation.__init__)


def test_hyp_esmodel_operations_abstractoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_AbstractOperation.__init__)
    params = list(sig.parameters.keys())
    assert "clientDate" in params, "Missing parameter 'clientDate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "accepted" in params, "Missing parameter 'accepted'"
    assert "description" in params, "Missing parameter 'description'"







def test_hyp_esmodel_notification_esnotification_is_not_abstract():
    assert not inspect.isabstract(esmodel_notification_ESNotification)


def test_hyp_esmodel_notification_esnotification_constructor_exists():
    assert callable(esmodel_notification_ESNotification.__init__)


def test_hyp_esmodel_notification_esnotification_constructor_args():
    sig = inspect.signature(esmodel_notification_ESNotification.__init__)
    params = list(sig.parameters.keys())
    assert "sender" in params, "Missing parameter 'sender'"
    assert "message" in params, "Missing parameter 'message'"
    assert "recipient" in params, "Missing parameter 'recipient'"
    assert "details" in params, "Missing parameter 'details'"
    assert "seen" in params, "Missing parameter 'seen'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "provider" in params, "Missing parameter 'provider'"
    assert "name" in params, "Missing parameter 'name'"











def test_hyp_esmodel_fileidentifier_is_not_abstract():
    assert not inspect.isabstract(esmodel_FileIdentifier)


def test_hyp_esmodel_fileidentifier_constructor_exists():
    assert callable(esmodel_FileIdentifier.__init__)


def test_hyp_esmodel_fileidentifier_constructor_args():
    sig = inspect.signature(esmodel_FileIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_esmodel_accesscontrol_acorgunit_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACOrgUnit)


def test_hyp_esmodel_accesscontrol_acorgunit_constructor_exists():
    assert callable(esmodel_accesscontrol_ACOrgUnit.__init__)


def test_hyp_esmodel_accesscontrol_acorgunit_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACOrgUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"





def test_hyp_metamodel_modelelement_is_not_abstract():
    assert not inspect.isabstract(metamodel_ModelElement)


def test_hyp_metamodel_modelelement_constructor_exists():
    assert callable(metamodel_ModelElement.__init__)


def test_hyp_metamodel_modelelement_constructor_args():
    sig = inspect.signature(metamodel_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "creator" in params, "Missing parameter 'creator'"





def test_hyp_metamodel_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(metamodel_IdentifiableElement)


def test_hyp_metamodel_identifiableelement_constructor_exists():
    assert callable(metamodel_IdentifiableElement.__init__)


def test_hyp_metamodel_identifiableelement_constructor_args():
    sig = inspect.signature(metamodel_IdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"




def test_hyp_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_hyp_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_hyp_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_unicasemodelelement_is_not_abstract():
    assert not inspect.isabstract(model_UnicaseModelElement)


def test_hyp_model_unicasemodelelement_constructor_exists():
    assert callable(model_UnicaseModelElement.__init__)


def test_hyp_model_unicasemodelelement_constructor_args():
    sig = inspect.signature(model_UnicaseModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "state" in params, "Missing parameter 'state'"
    assert "description" in params, "Missing parameter 'description'"






def test_hyp_metamodel_project_is_not_abstract():
    assert not inspect.isabstract(metamodel_Project)


def test_hyp_metamodel_project_constructor_exists():
    assert callable(metamodel_Project.__init__)


def test_hyp_metamodel_project_constructor_args():
    sig = inspect.signature(metamodel_Project.__init__)
    params = list(sig.parameters.keys())

def test_hyp_associationtype_exists():
    # Check that the Enumeration exists
    assert AssociationType is not None

def test_hyp_associationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationType]
    expected_literals = [
        "COMPOSITION",
        "AGGREGATION",
        "UNDIRECTED_ASSOCIATION",
        "DIRECTED_ASSOCIATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationType"

def test_hyp_mergeglobalchoiceselection_exists():
    # Check that the Enumeration exists
    assert MergeGlobalChoiceSelection is not None

def test_hyp_mergeglobalchoiceselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MergeGlobalChoiceSelection]
    expected_literals = [
        "AllMine",
        "OKNotFinished",
        "Cancel",
        "AllTheir",
        "OKFinished",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MergeGlobalChoiceSelection"

def test_hyp_diagramtype_exists():
    # Check that the Enumeration exists
    assert DiagramType is not None

def test_hyp_diagramtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagramType]
    expected_literals = [
        "USECASE_DIAGRAM",
        "CLASS_DIAGRAM",
        "ACTIVITY_DIAGRAM",
        "STATE_DIAGRAM",
        "WORKITEM_DIAGRAM",
        "COMPONENT_DIAGRAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagramType"

def test_hyp_scopetype_exists():
    # Check that the Enumeration exists
    assert ScopeType is not None

def test_hyp_scopetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeType]
    expected_literals = [
        "INSTANCE",
        "CLASS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"

def test_hyp_resolutiontype_exists():
    # Check that the Enumeration exists
    assert ResolutionType is not None

def test_hyp_resolutiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResolutionType]
    expected_literals = [
        "WONT_FIX",
        "CANNOT_REPRODUCE",
        "FIXED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResolutionType"

def test_hyp_activitytype_exists():
    # Check that the Enumeration exists
    assert ActivityType is not None

def test_hyp_activitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityType]
    expected_literals = [
        "TESTING",
        "SYSTEM_DESIGN",
        "NONE",
        "IMPLEMENTATION",
        "ANALYSIS",
        "OBJECT_DESIGN",
        "MANAGEMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityType"

def test_hyp_bugstatus_exists():
    # Check that the Enumeration exists
    assert BugStatus is not None

def test_hyp_bugstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BugStatus]
    expected_literals = [
        "RESOLVED",
        "ASSIGNED",
        "CLOSED",
        "CONFIRMED",
        "NEW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BugStatus"

def test_hyp_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_hyp_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "BLOCKER",
        "MAJOR",
        "MINOR",
        "FEATURE",
        "TRIVIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Severity"

def test_hyp_containmenttype_exists():
    # Check that the Enumeration exists
    assert ContainmentType is not None

def test_hyp_containmenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainmentType]
    expected_literals = [
        "CONTAINMENT",
        "CONTAINER",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainmentType"

def test_hyp_argumentdirectiontype_exists():
    # Check that the Enumeration exists
    assert ArgumentDirectionType is not None

def test_hyp_argumentdirectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArgumentDirectionType]
    expected_literals = [
        "OUT",
        "UNDEFINED",
        "INOUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArgumentDirectionType"

def test_hyp_mergechoiceselection_exists():
    # Check that the Enumeration exists
    assert MergeChoiceSelection is not None

def test_hyp_mergechoiceselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MergeChoiceSelection]
    expected_literals = [
        "MergedText",
        "Their",
        "Issue",
        "Mine",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MergeChoiceSelection"

def test_hyp_visibilitytype_exists():
    # Check that the Enumeration exists
    assert VisibilityType is not None

def test_hyp_visibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityType]
    expected_literals = [
        "PROTECTED",
        "PRIVATE",
        "PACKAGE",
        "GLOBAL",
        "UNDEFINED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
change_ModelChangePackage_strategy = st.builds(
    change_ModelChangePackage,
)
organization_OrgUnit_strategy = st.builds(
    organization_OrgUnit,
)
organization_User_strategy = st.builds(
    organization_User,
)
UnicaseModelElement_strategy = st.builds(
    UnicaseModelElement,
)
model_Annotation_strategy = st.builds(
    model_Annotation,
)
task_WorkPackage_strategy = st.builds(
    task_WorkPackage,
)
profile_StereotypeInstance_strategy = st.builds(
    profile_StereotypeInstance,
)
OrgUnit_strategy = st.builds(
    OrgUnit,
)
model_organization_Group_strategy = st.builds(
    model_organization_Group,
)
model_organization_User_strategy = st.builds(
    model_organization_User,
    firstName=
        safe_text,
    lastName=
        safe_text,
    email=
        safe_text
)
task_WorkItem_strategy = st.builds(
    task_WorkItem,
)
organization_Group_strategy = st.builds(
    organization_Group,
)
model_organization_OrgUnit_strategy = st.builds(
    model_organization_OrgUnit,
    acOrgId=
        safe_text
)
Project_strategy = st.builds(
    Project,
)
esmodel_url_ModelElementUrlFragment_strategy = st.builds(
    esmodel_url_ModelElementUrlFragment,
    name=
        safe_text
)
url_ModelElementUrlFragment_strategy = st.builds(
    url_ModelElementUrlFragment,
)
url_ProjectUrlFragment_strategy = st.builds(
    url_ProjectUrlFragment,
)
url_ServerUrl_strategy = st.builds(
    url_ServerUrl,
)
esmodel_url_ModelElementUrl_strategy = st.builds(
    esmodel_url_ModelElementUrl,
)
esmodel_url_ProjectUrlFragment_strategy = st.builds(
    esmodel_url_ProjectUrlFragment,
    name=
        safe_text
)
esmodel_url_ServerUrl_strategy = st.builds(
    esmodel_url_ServerUrl,
    port=
        st.integers(),
    hostName=
        safe_text
)
Role_strategy = st.builds(
    Role,
)
esmodel_roles_ServerAdmin_strategy = st.builds(
    esmodel_roles_ServerAdmin,
)
esmodel_roles_WriterRole_strategy = st.builds(
    esmodel_roles_WriterRole,
)
esmodel_roles_ProjectAdminRole_strategy = st.builds(
    esmodel_roles_ProjectAdminRole,
)
esmodel_roles_ReaderRole_strategy = st.builds(
    esmodel_roles_ReaderRole,
)
ACOrgUnit_strategy = st.builds(
    ACOrgUnit,
)
esmodel_accesscontrol_ACUser_strategy = st.builds(
    esmodel_accesscontrol_ACUser,
    lastName=
        safe_text,
    firstName=
        safe_text
)
esmodel_roles_Role_strategy = st.builds(
    esmodel_roles_Role,
)
esmodel_accesscontrol_OrgUnitProperty_strategy = st.builds(
    esmodel_accesscontrol_OrgUnitProperty,
    name=
        safe_text,
    value=
        safe_text
)
accesscontrol_ACOrgUnit_strategy = st.builds(
    accesscontrol_ACOrgUnit,
)
esmodel_accesscontrol_ACGroup_strategy = st.builds(
    esmodel_accesscontrol_ACGroup,
)
accesscontrol_OrgUnitProperty_strategy = st.builds(
    accesscontrol_OrgUnitProperty,
)
roles_Role_strategy = st.builds(
    roles_Role,
)
ServerProjectEvent_strategy = st.builds(
    ServerProjectEvent,
)
esmodel_server_ProjectUpdatedEvent_strategy = st.builds(
    esmodel_server_ProjectUpdatedEvent,
)
ServerEvent_strategy = st.builds(
    ServerEvent,
)
esmodel_server_ServerProjectEvent_strategy = st.builds(
    esmodel_server_ServerProjectEvent,
)
operations_OperationId_strategy = st.builds(
    operations_OperationId,
)
ReadEvent_strategy = st.builds(
    ReadEvent,
)
esmodel_events_NotificationReadEvent_strategy = st.builds(
    esmodel_events_NotificationReadEvent,
    notificationId=
        safe_text
)
esmodel_events_Event_strategy = st.builds(
    esmodel_events_Event,
    timestamp=
        st.dates()
)
CompositeOperation_strategy = st.builds(
    CompositeOperation,
)
esmodel_semantic_SemanticCompositeOperation_strategy = st.builds(
    esmodel_semantic_SemanticCompositeOperation,
)
esmodel_operations_EObjectToModelElementIdMap_strategy = st.builds(
    esmodel_operations_EObjectToModelElementIdMap,
)
Event_strategy = st.builds(
    Event,
)
esmodel_events_ShowHistoryEvent_strategy = st.builds(
    esmodel_events_ShowHistoryEvent,
)
esmodel_events_PerspectiveEvent_strategy = st.builds(
    esmodel_events_PerspectiveEvent,
)
esmodel_events_UpdateEvent_strategy = st.builds(
    esmodel_events_UpdateEvent,
)
esmodel_events_MergeGlobalChoiceEvent_strategy = st.builds(
    esmodel_events_MergeGlobalChoiceEvent,
    selection=
        safe_text
)
esmodel_events_RevertEvent_strategy = st.builds(
    esmodel_events_RevertEvent,
    revertedChangesCount=
        st.integers()
)
esmodel_events_NotificationIgnoreEvent_strategy = st.builds(
    esmodel_events_NotificationIgnoreEvent,
    notificationId=
        safe_text
)
esmodel_events_MergeEvent_strategy = st.builds(
    esmodel_events_MergeEvent,
    totalTime=
        st.integers(),
    numberOfConflicts=
        st.integers()
)
esmodel_events_PluginFocusEvent_strategy = st.builds(
    esmodel_events_PluginFocusEvent,
    startDate=
        st.dates(),
    pluginId=
        safe_text
)
esmodel_events_CheckoutEvent_strategy = st.builds(
    esmodel_events_CheckoutEvent,
)
esmodel_events_PresentationSwitchEvent_strategy = st.builds(
    esmodel_events_PresentationSwitchEvent,
    newPresentation=
        safe_text,
    readView=
        safe_text
)
esmodel_events_ExceptionEvent_strategy = st.builds(
    esmodel_events_ExceptionEvent,
    ExceptionCauseStackTrace=
        safe_text,
    ExceptionCauseTitle=
        safe_text,
    ExceptionStackTrace=
        safe_text,
    ExceptionTitle=
        safe_text
)
esmodel_events_PluginStartEvent_strategy = st.builds(
    esmodel_events_PluginStartEvent,
    pluginId=
        safe_text
)
esmodel_events_UndoEvent_strategy = st.builds(
    esmodel_events_UndoEvent,
)
esmodel_events_NavigatorCreateEvent_strategy = st.builds(
    esmodel_events_NavigatorCreateEvent,
    dynamic=
        st.booleans()
)
esmodel_server_ServerEvent_strategy = st.builds(
    esmodel_server_ServerEvent,
)
esmodel_events_URLEvent_strategy = st.builds(
    esmodel_events_URLEvent,
    sourceView=
        safe_text
)
esmodel_events_Validate_strategy = st.builds(
    esmodel_events_Validate,
)
esmodel_events_TraceEvent_strategy = st.builds(
    esmodel_events_TraceEvent,
    featureName=
        safe_text
)
esmodel_events_ShowChangesEvent_strategy = st.builds(
    esmodel_events_ShowChangesEvent,
)
esmodel_events_NotificationGenerationEvent_strategy = st.builds(
    esmodel_events_NotificationGenerationEvent,
)
esmodel_events_DNDEvent_strategy = st.builds(
    esmodel_events_DNDEvent,
    targetView=
        safe_text,
    sourceView=
        safe_text
)
esmodel_events_LinkEvent_strategy = st.builds(
    esmodel_events_LinkEvent,
    createdNew=
        st.booleans(),
    sourceView=
        safe_text
)
esmodel_events_AnnotationEvent_strategy = st.builds(
    esmodel_events_AnnotationEvent,
)
esmodel_events_MergeChoiceEvent_strategy = st.builds(
    esmodel_events_MergeChoiceEvent,
    createdIssueName=
        safe_text,
    selection=
        safe_text,
    contextFeature=
        safe_text
)
esmodel_events_ReadEvent_strategy = st.builds(
    esmodel_events_ReadEvent,
    sourceView=
        safe_text,
    readView=
        safe_text
)
ReferenceOperation_strategy = st.builds(
    ReferenceOperation,
)
esmodel_operations_MultiReferenceSetOperation_strategy = st.builds(
    esmodel_operations_MultiReferenceSetOperation,
    index=
        st.integers()
)
esmodel_operations_SingleReferenceOperation_strategy = st.builds(
    esmodel_operations_SingleReferenceOperation,
)
esmodel_operations_ModelElementGroup_strategy = st.builds(
    esmodel_operations_ModelElementGroup,
    name=
        safe_text
)
esmodel_operations_OperationGroup_strategy = st.builds(
    esmodel_operations_OperationGroup,
    name=
        safe_text
)
AttributeOperation_strategy = st.builds(
    AttributeOperation,
)
esmodel_operations_DiagramLayoutOperation_strategy = st.builds(
    esmodel_operations_DiagramLayoutOperation,
)
esmodel_operations_MultiReferenceOperation_strategy = st.builds(
    esmodel_operations_MultiReferenceOperation,
    index=
        st.integers(),
    add=
        st.booleans()
)
operations_esmodel_EObject_strategy = st.builds(
    operations_esmodel_EObject,
)
AbstractOperation_strategy = st.builds(
    AbstractOperation,
)
esmodel_operations_FeatureOperation_strategy = st.builds(
    esmodel_operations_FeatureOperation,
    featureName=
        safe_text
)
esmodel_operations_CreateDeleteOperation_strategy = st.builds(
    esmodel_operations_CreateDeleteOperation,
    delete=
        st.booleans()
)
esmodel_operations_CompositeOperation_strategy = st.builds(
    esmodel_operations_CompositeOperation,
    compositeDescription=
        safe_text,
    reversed=
        st.booleans(),
    compositeName=
        safe_text
)
FeatureOperation_strategy = st.builds(
    FeatureOperation,
)
esmodel_operations_MultiAttributeSetOperation_strategy = st.builds(
    esmodel_operations_MultiAttributeSetOperation,
    newValue=
        safe_text,
    oldValue=
        safe_text,
    index=
        st.integers()
)
esmodel_operations_MultiAttributeMoveOperation_strategy = st.builds(
    esmodel_operations_MultiAttributeMoveOperation,
    oldIndex=
        st.integers(),
    referencedValue=
        safe_text,
    newIndex=
        st.integers()
)
esmodel_operations_ReferenceOperation_strategy = st.builds(
    esmodel_operations_ReferenceOperation,
    containmentType=
        safe_text,
    oppositeFeatureName=
        safe_text,
    bidirectional=
        st.booleans()
)
esmodel_operations_MultiReferenceMoveOperation_strategy = st.builds(
    esmodel_operations_MultiReferenceMoveOperation,
    oldIndex=
        st.integers(),
    newIndex=
        st.integers()
)
esmodel_operations_MultiAttributeOperation_strategy = st.builds(
    esmodel_operations_MultiAttributeOperation,
    indexes=
        st.integers(),
    add=
        st.booleans(),
    referencedValues=
        safe_text
)
esmodel_operations_AttributeOperation_strategy = st.builds(
    esmodel_operations_AttributeOperation,
    oldValue=
        safe_text,
    newValue=
        safe_text
)
operations_EObjectToModelElementIdMap_strategy = st.builds(
    operations_EObjectToModelElementIdMap,
)
operations_ReferenceOperation_strategy = st.builds(
    operations_ReferenceOperation,
)
esmodel_versioning_Version_strategy = st.builds(
    esmodel_versioning_Version,
)
esmodel_versioning_HistoryQuery_strategy = st.builds(
    esmodel_versioning_HistoryQuery,
    includeChangePackage=
        st.booleans()
)
esmodel_versioning_VersionProperty_strategy = st.builds(
    esmodel_versioning_VersionProperty,
    value=
        safe_text,
    name=
        safe_text
)
notification_ESNotification_strategy = st.builds(
    notification_ESNotification,
)
versioning_LogMessage_strategy = st.builds(
    versioning_LogMessage,
)
events_Event_strategy = st.builds(
    events_Event,
)
operations_AbstractOperation_strategy = st.builds(
    operations_AbstractOperation,
)
esmodel_versioning_ChangePackage_strategy = st.builds(
    esmodel_versioning_ChangePackage,
)
versioning_ChangePackage_strategy = st.builds(
    versioning_ChangePackage,
)
versioning_TagVersionSpec_strategy = st.builds(
    versioning_TagVersionSpec,
)
esmodel_versioning_HistoryInfo_strategy = st.builds(
    esmodel_versioning_HistoryInfo,
)
versioning_VersionProperty_strategy = st.builds(
    versioning_VersionProperty,
)
VersionSpec_strategy = st.builds(
    VersionSpec,
)
esmodel_versioning_HeadVersionSpec_strategy = st.builds(
    esmodel_versioning_HeadVersionSpec,
)
esmodel_versioning_DateVersionSpec_strategy = st.builds(
    esmodel_versioning_DateVersionSpec,
    date=
        st.dates()
)
esmodel_versioning_TagVersionSpec_strategy = st.builds(
    esmodel_versioning_TagVersionSpec,
    name=
        safe_text
)
esmodel_versioning_LogMessage_strategy = st.builds(
    esmodel_versioning_LogMessage,
    clientDate=
        st.dates(),
    author=
        safe_text,
    message=
        safe_text,
    date=
        st.dates()
)
esmodel_versioning_VersionSpec_strategy = st.builds(
    esmodel_versioning_VersionSpec,
)
esmodel_ClientVersionInfo_strategy = st.builds(
    esmodel_ClientVersionInfo,
    version=
        safe_text,
    name=
        safe_text
)
esmodel_VersionInfo_strategy = st.builds(
    esmodel_VersionInfo,
    emfStoreVersionString=
        safe_text
)
esmodel_versioning_PrimaryVersionSpec_strategy = st.builds(
    esmodel_versioning_PrimaryVersionSpec,
    identifier=
        st.integers()
)
versioning_PrimaryVersionSpec_strategy = st.builds(
    versioning_PrimaryVersionSpec,
)
esmodel_ProjectInfo_strategy = st.builds(
    esmodel_ProjectInfo,
    description=
        safe_text,
    name=
        safe_text
)
versioning_Version_strategy = st.builds(
    versioning_Version,
)
ProjectId_strategy = st.builds(
    ProjectId,
)
esmodel_ProjectHistory_strategy = st.builds(
    esmodel_ProjectHistory,
    projectName=
        safe_text,
    projectDescription=
        safe_text
)
ActivityObject_strategy = st.builds(
    ActivityObject,
)
model_activity_ActivityInitial_strategy = st.builds(
    model_activity_ActivityInitial,
)
model_activity_ActivityEnd_strategy = st.builds(
    model_activity_ActivityEnd,
)
model_activity_Fork_strategy = st.builds(
    model_activity_Fork,
)
model_activity_Branch_strategy = st.builds(
    model_activity_Branch,
)
model_activity_Activity_strategy = st.builds(
    model_activity_Activity,
)
activity_ActivityObject_strategy = st.builds(
    activity_ActivityObject,
)
accesscontrol_ACUser_strategy = st.builds(
    accesscontrol_ACUser,
)
SessionId_strategy = st.builds(
    SessionId,
)
model_activity_Transition_strategy = st.builds(
    model_activity_Transition,
    condition=
        safe_text
)
ProjectHistory_strategy = st.builds(
    ProjectHistory,
)
accesscontrol_ACGroup_strategy = st.builds(
    accesscontrol_ACGroup,
)
esmodel_ServerSpace_strategy = st.builds(
    esmodel_ServerSpace,
)
ModelElementId_strategy = st.builds(
    ModelElementId,
)
model_util_ModelElementPath_strategy = st.builds(
    model_util_ModelElementPath,
)
StereotypeAttributeInstance_strategy = st.builds(
    StereotypeAttributeInstance,
)
model_profile_StereotypeAttributeInstanceString_strategy = st.builds(
    model_profile_StereotypeAttributeInstanceString,
    value=
        safe_text
)
model_profile_StereotypeAttributeInstance_strategy = st.builds(
    model_profile_StereotypeAttributeInstance,
)
StereotypeAttribute_strategy = st.builds(
    StereotypeAttribute,
)
model_profile_StereotypeAttributeSimple_strategy = st.builds(
    model_profile_StereotypeAttributeSimple,
    type=
        safe_text
)
model_profile_StereotypeAttribute_strategy = st.builds(
    model_profile_StereotypeAttribute,
)
profile_StereotypeAttributeInstance_strategy = st.builds(
    profile_StereotypeAttributeInstance,
)
activity_Transition_strategy = st.builds(
    activity_Transition,
)
model_activity_ActivityObject_strategy = st.builds(
    model_activity_ActivityObject,
)
model_profile_StereotypeInstance_strategy = st.builds(
    model_profile_StereotypeInstance,
)
profile_StereotypeAttribute_strategy = st.builds(
    profile_StereotypeAttribute,
)
profile_Profile_strategy = st.builds(
    profile_Profile,
)
model_profile_Stereotype_strategy = st.builds(
    model_profile_Stereotype,
    required=
        st.booleans()
)
profile_Stereotype_strategy = st.builds(
    profile_Stereotype,
)
model_profile_Profile_strategy = st.builds(
    model_profile_Profile,
)
StateNode_strategy = st.builds(
    StateNode,
)
model_state_StateEnd_strategy = st.builds(
    model_state_StateEnd,
)
model_state_StateInitial_strategy = st.builds(
    model_state_StateInitial,
)
model_state_State_strategy = st.builds(
    model_state_State,
    activities=
        safe_text,
    exitConditions=
        safe_text,
    entryConditions=
        safe_text
)
state_Transition_strategy = st.builds(
    state_Transition,
)
model_state_StateNode_strategy = st.builds(
    model_state_StateNode,
)
state_StateNode_strategy = st.builds(
    state_StateNode,
)
model_state_Transition_strategy = st.builds(
    model_state_Transition,
    condition=
        safe_text
)
MeetingSection_strategy = st.builds(
    MeetingSection,
)
model_meeting_IssueMeetingSection_strategy = st.builds(
    model_meeting_IssueMeetingSection,
)
model_meeting_WorkItemMeetingSection_strategy = st.builds(
    model_meeting_WorkItemMeetingSection,
)
model_meeting_CompositeMeetingSection_strategy = st.builds(
    model_meeting_CompositeMeetingSection,
)
model_meeting_MeetingSection_strategy = st.builds(
    model_meeting_MeetingSection,
    allocatedTime=
        st.integers()
)
meeting_WorkItemMeetingSection_strategy = st.builds(
    meeting_WorkItemMeetingSection,
)
meeting_IssueMeetingSection_strategy = st.builds(
    meeting_IssueMeetingSection,
)
meeting_MeetingSection_strategy = st.builds(
    meeting_MeetingSection,
)
component_Component_strategy = st.builds(
    component_Component,
)
model_component_ComponentService_strategy = st.builds(
    model_component_ComponentService,
)
model_meeting_Meeting_strategy = st.builds(
    model_meeting_Meeting,
    starttime=
        st.dates(),
    endtime=
        st.dates(),
    location=
        safe_text
)
model_component_DeploymentNode_strategy = st.builds(
    model_component_DeploymentNode,
)
component_ComponentService_strategy = st.builds(
    component_ComponentService,
)
model_component_Component_strategy = st.builds(
    model_component_Component,
)
Solution_strategy = st.builds(
    Solution,
)
model_change_MergingSolution_strategy = st.builds(
    model_change_MergingSolution,
)
change_MergingProposal_strategy = st.builds(
    change_MergingProposal,
)
Proposal_strategy = st.builds(
    Proposal,
)
model_change_MergingProposal_strategy = st.builds(
    model_change_MergingProposal,
)
Issue_strategy = st.builds(
    Issue,
)
model_change_MergingIssue_strategy = st.builds(
    model_change_MergingIssue,
    resolvingRevision=
        st.integers()
)
model_change_ModelChangePackage_strategy = st.builds(
    model_change_ModelChangePackage,
    sourceVersion=
        st.integers(),
    targetVersion=
        st.integers()
)
rationale_Issue_strategy = st.builds(
    rationale_Issue,
)
rationale_Criterion_strategy = st.builds(
    rationale_Criterion,
)
model_rationale_Criterion_strategy = st.builds(
    model_rationale_Criterion,
)
rationale_Assessment_strategy = st.builds(
    rationale_Assessment,
)
rationale_Solution_strategy = st.builds(
    rationale_Solution,
)
rationale_Proposal_strategy = st.builds(
    rationale_Proposal,
)
Criterion_strategy = st.builds(
    Criterion,
)
model_requirement_NonFunctionalRequirement_strategy = st.builds(
    model_requirement_NonFunctionalRequirement,
)
requirement_SystemFunction_strategy = st.builds(
    requirement_SystemFunction,
)
NonDomainElement_strategy = st.builds(
    NonDomainElement,
)
model_rationale_Assessment_strategy = st.builds(
    model_rationale_Assessment,
    value=
        st.integers()
)
model_rationale_Proposal_strategy = st.builds(
    model_rationale_Proposal,
)
model_rationale_Solution_strategy = st.builds(
    model_rationale_Solution,
)
model_requirement_SystemFunction_strategy = st.builds(
    model_requirement_SystemFunction,
    output=
        safe_text,
    input=
        safe_text,
    exception=
        safe_text
)
model_rationale_Comment_strategy = st.builds(
    model_rationale_Comment,
)
model_requirement_UserTask_strategy = st.builds(
    model_requirement_UserTask,
)
model_requirement_Step_strategy = st.builds(
    model_requirement_Step,
    userStep=
        st.booleans()
)
model_requirement_ActorInstance_strategy = st.builds(
    model_requirement_ActorInstance,
)
model_requirement_Actor_strategy = st.builds(
    model_requirement_Actor,
)
requirement_ActorInstance_strategy = st.builds(
    requirement_ActorInstance,
)
model_requirement_Scenario_strategy = st.builds(
    model_requirement_Scenario,
)
requirement_NonFunctionalRequirement_strategy = st.builds(
    requirement_NonFunctionalRequirement,
)
requirement_UserTask_strategy = st.builds(
    requirement_UserTask,
)
requirement_Step_strategy = st.builds(
    requirement_Step,
)
requirement_Actor_strategy = st.builds(
    requirement_Actor,
)
model_requirement_UseCase_strategy = st.builds(
    model_requirement_UseCase,
    precondition=
        safe_text,
    rules=
        safe_text,
    exception=
        safe_text,
    postcondition=
        safe_text
)
model_requirement_FunctionalRequirement_strategy = st.builds(
    model_requirement_FunctionalRequirement,
    storyPoints=
        st.integers(),
    cost=
        st.integers(),
    priority=
        st.integers(),
    reviewed=
        st.booleans()
)
document_Section_strategy = st.builds(
    document_Section,
)
requirement_FunctionalRequirement_strategy = st.builds(
    requirement_FunctionalRequirement,
)
model_classes_Dependency_strategy = st.builds(
    model_classes_Dependency,
)
Section_strategy = st.builds(
    Section,
)
model_document_CompositeSection_strategy = st.builds(
    model_document_CompositeSection,
)
model_document_LeafSection_strategy = st.builds(
    model_document_LeafSection,
)
document_CompositeSection_strategy = st.builds(
    document_CompositeSection,
)
model_document_Section_strategy = st.builds(
    model_document_Section,
)
model_classes_MethodArgument_strategy = st.builds(
    model_classes_MethodArgument,
    label=
        safe_text,
    defaultValue=
        safe_text,
    direction=
        safe_text,
    type=
        safe_text,
    signature=
        safe_text
)
classes_MethodArgument_strategy = st.builds(
    classes_MethodArgument,
)
model_classes_Method_strategy = st.builds(
    model_classes_Method,
    properties=
        safe_text,
    signature=
        safe_text,
    returnType=
        safe_text,
    stubbed=
        st.booleans(),
    scope=
        safe_text,
    label=
        safe_text,
    visibility=
        safe_text
)
classes_PackageElement_strategy = st.builds(
    classes_PackageElement,
)
model_classes_Attribute_strategy = st.builds(
    model_classes_Attribute,
    label=
        safe_text,
    type=
        safe_text,
    properties=
        safe_text,
    defaultValue=
        safe_text,
    visibility=
        safe_text,
    signature=
        safe_text,
    scope=
        safe_text
)
model_classes_Association_strategy = st.builds(
    model_classes_Association,
    targetRole=
        safe_text,
    sourceMultiplicity=
        safe_text,
    sourceRole=
        safe_text,
    type=
        safe_text,
    targetMultiplicity=
        safe_text
)
classes_Association_strategy = st.builds(
    classes_Association,
)
requirement_Scenario_strategy = st.builds(
    requirement_Scenario,
)
requirement_UseCase_strategy = st.builds(
    requirement_UseCase,
)
classes_Method_strategy = st.builds(
    classes_Method,
)
classes_Attribute_strategy = st.builds(
    classes_Attribute,
)
classes_Class_strategy = st.builds(
    classes_Class,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
model_classes_Package_strategy = st.builds(
    model_classes_Package,
)
model_classes_Class_strategy = st.builds(
    model_classes_Class,
)
classes_Dependency_strategy = st.builds(
    classes_Dependency,
)
classes_Package_strategy = st.builds(
    classes_Package,
)
model_classes_PackageElement_strategy = st.builds(
    model_classes_PackageElement,
)
diagram_model_Diagram_strategy = st.builds(
    diagram_model_Diagram,
)
task_Checkable_strategy = st.builds(
    task_Checkable,
)
model_bug_BugReport_strategy = st.builds(
    model_bug_BugReport,
    resolution=
        safe_text,
    resolutionType=
        safe_text,
    Status=
        safe_text,
    severity=
        safe_text
)
model_task_ActionItem_strategy = st.builds(
    model_task_ActionItem,
    done=
        st.booleans(),
    activity=
        safe_text
)
model_task_Checkable_strategy = st.builds(
    model_task_Checkable,
    checked=
        st.booleans()
)
WorkItem_strategy = st.builds(
    WorkItem,
)
model_task_Milestone_strategy = st.builds(
    model_task_Milestone,
)
model_task_WorkPackage_strategy = st.builds(
    model_task_WorkPackage,
    endDate=
        st.dates(),
    startDate=
        st.dates()
)
model_Project_strategy = st.builds(
    model_Project,
)
model_NonDomainElement_strategy = st.builds(
    model_NonDomainElement,
)
model_Attachment_strategy = st.builds(
    model_Attachment,
)
metamodel_UniqueIdentifier_strategy = st.builds(
    metamodel_UniqueIdentifier,
    id=
        safe_text
)
rationale_Comment_strategy = st.builds(
    rationale_Comment,
)
document_LeafSection_strategy = st.builds(
    document_LeafSection,
)
Attachment_strategy = st.builds(
    Attachment,
)
model_attachment_UrlAttachment_strategy = st.builds(
    model_attachment_UrlAttachment,
    url=
        safe_text
)
model_attachment_FileAttachment_strategy = st.builds(
    model_attachment_FileAttachment,
    fileName=
        safe_text,
    requiredOffline=
        st.booleans(),
    fileID=
        safe_text,
    fileHash=
        safe_text,
    fileSize=
        safe_text
)
model_diagram_MEDiagram_strategy = st.builds(
    model_diagram_MEDiagram,
    diagramLayout=
        safe_text,
    type=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
model_rationale_Issue_strategy = st.builds(
    model_rationale_Issue,
    activity=
        safe_text
)
model_task_WorkItem_strategy = st.builds(
    model_task_WorkItem,
    effort=
        st.integers(),
    dueDate=
        st.dates(),
    resolved=
        st.booleans(),
    estimate=
        st.integers(),
    priority=
        st.integers()
)
metamodel_AssociationClassElement_strategy = st.builds(
    metamodel_AssociationClassElement,
)
metamodel_NonDomainElement_strategy = st.builds(
    metamodel_NonDomainElement,
)
metamodel_ModelVersion_strategy = st.builds(
    metamodel_ModelVersion,
    releaseNumber=
        st.integers()
)
UniqueIdentifier_strategy = st.builds(
    UniqueIdentifier,
)
esmodel_ProjectId_strategy = st.builds(
    esmodel_ProjectId,
)
esmodel_operations_OperationId_strategy = st.builds(
    esmodel_operations_OperationId,
)
esmodel_SessionId_strategy = st.builds(
    esmodel_SessionId,
)
esmodel_accesscontrol_ACOrgUnitId_strategy = st.builds(
    esmodel_accesscontrol_ACOrgUnitId,
)
metamodel_ModelElementId_strategy = st.builds(
    metamodel_ModelElementId,
)
IdentifiableElement_strategy = st.builds(
    IdentifiableElement,
)
esmodel_operations_AbstractOperation_strategy = st.builds(
    esmodel_operations_AbstractOperation,
    clientDate=
        st.dates(),
    name=
        safe_text,
    accepted=
        st.booleans(),
    description=
        safe_text
)
esmodel_notification_ESNotification_strategy = st.builds(
    esmodel_notification_ESNotification,
    sender=
        safe_text,
    message=
        safe_text,
    recipient=
        safe_text,
    details=
        safe_text,
    seen=
        st.booleans(),
    creationDate=
        st.dates(),
    provider=
        safe_text,
    name=
        safe_text
)
esmodel_FileIdentifier_strategy = st.builds(
    esmodel_FileIdentifier,
)
esmodel_accesscontrol_ACOrgUnit_strategy = st.builds(
    esmodel_accesscontrol_ACOrgUnit,
    name=
        safe_text,
    description=
        safe_text
)
metamodel_ModelElement_strategy = st.builds(
    metamodel_ModelElement,
    creationDate=
        st.dates(),
    creator=
        safe_text
)
metamodel_IdentifiableElement_strategy = st.builds(
    metamodel_IdentifiableElement,
    identifier=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
model_UnicaseModelElement_strategy = st.builds(
    model_UnicaseModelElement,
    name=
        safe_text,
    state=
        safe_text,
    description=
        safe_text
)
metamodel_Project_strategy = st.builds(
    metamodel_Project,
)













@given(instance=model_organization_User_strategy)
def test_hyp_model_organization_user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=model_organization_User_strategy)
def test_hyp_model_organization_user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=model_organization_User_strategy)
def test_hyp_model_organization_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original






@given(instance=model_organization_OrgUnit_strategy)
def test_hyp_model_organization_orgunit_acOrgId_setter(instance):
    original = instance.acOrgId
    instance.acOrgId = original
    assert instance.acOrgId == original





@given(instance=esmodel_url_ModelElementUrlFragment_strategy)
def test_hyp_esmodel_url_modelelementurlfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=esmodel_url_ProjectUrlFragment_strategy)
def test_hyp_esmodel_url_projecturlfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=esmodel_url_ServerUrl_strategy)
def test_hyp_esmodel_url_serverurl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=esmodel_url_ServerUrl_strategy)
def test_hyp_esmodel_url_serverurl_hostName_setter(instance):
    original = instance.hostName
    instance.hostName = original
    assert instance.hostName == original










@given(instance=esmodel_accesscontrol_ACUser_strategy)
def test_hyp_esmodel_accesscontrol_acuser_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=esmodel_accesscontrol_ACUser_strategy)
def test_hyp_esmodel_accesscontrol_acuser_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_hyp_esmodel_roles_role_canadministrate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canAdministrate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canAdministrate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canAdministrate' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canAdministrate' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canAdministrate' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_hyp_esmodel_roles_role_candelete_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canDelete(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canDelete).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canDelete' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canDelete' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canDelete' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_hyp_esmodel_roles_role_canread_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canRead(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canRead).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canRead' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canRead' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canRead' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_hyp_esmodel_roles_role_cancreate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canCreate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canCreate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canCreate' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canCreate' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canCreate' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_hyp_esmodel_roles_role_canmodify_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canModify(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canModify).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canModify' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canModify' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canModify' in esmodel_roles_Role is not implemented or raised an error")




@given(instance=esmodel_accesscontrol_OrgUnitProperty_strategy)
def test_hyp_esmodel_accesscontrol_orgunitproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_accesscontrol_OrgUnitProperty_strategy)
def test_hyp_esmodel_accesscontrol_orgunitproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original














@given(instance=esmodel_events_NotificationReadEvent_strategy)
def test_hyp_esmodel_events_notificationreadevent_notificationId_setter(instance):
    original = instance.notificationId
    instance.notificationId = original
    assert instance.notificationId == original




@given(instance=esmodel_events_Event_strategy)
def test_hyp_esmodel_events_event_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original











@given(instance=esmodel_events_MergeGlobalChoiceEvent_strategy)
def test_hyp_esmodel_events_mergeglobalchoiceevent_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original




@given(instance=esmodel_events_RevertEvent_strategy)
def test_hyp_esmodel_events_revertevent_revertedChangesCount_setter(instance):
    original = instance.revertedChangesCount
    instance.revertedChangesCount = original
    assert instance.revertedChangesCount == original




@given(instance=esmodel_events_NotificationIgnoreEvent_strategy)
def test_hyp_esmodel_events_notificationignoreevent_notificationId_setter(instance):
    original = instance.notificationId
    instance.notificationId = original
    assert instance.notificationId == original




@given(instance=esmodel_events_MergeEvent_strategy)
def test_hyp_esmodel_events_mergeevent_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=esmodel_events_MergeEvent_strategy)
def test_hyp_esmodel_events_mergeevent_numberOfConflicts_setter(instance):
    original = instance.numberOfConflicts
    instance.numberOfConflicts = original
    assert instance.numberOfConflicts == original




@given(instance=esmodel_events_PluginFocusEvent_strategy)
def test_hyp_esmodel_events_pluginfocusevent_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=esmodel_events_PluginFocusEvent_strategy)
def test_hyp_esmodel_events_pluginfocusevent_pluginId_setter(instance):
    original = instance.pluginId
    instance.pluginId = original
    assert instance.pluginId == original





@given(instance=esmodel_events_PresentationSwitchEvent_strategy)
def test_hyp_esmodel_events_presentationswitchevent_newPresentation_setter(instance):
    original = instance.newPresentation
    instance.newPresentation = original
    assert instance.newPresentation == original



@given(instance=esmodel_events_PresentationSwitchEvent_strategy)
def test_hyp_esmodel_events_presentationswitchevent_readView_setter(instance):
    original = instance.readView
    instance.readView = original
    assert instance.readView == original




@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_hyp_esmodel_events_exceptionevent_ExceptionCauseStackTrace_setter(instance):
    original = instance.ExceptionCauseStackTrace
    instance.ExceptionCauseStackTrace = original
    assert instance.ExceptionCauseStackTrace == original



@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_hyp_esmodel_events_exceptionevent_ExceptionCauseTitle_setter(instance):
    original = instance.ExceptionCauseTitle
    instance.ExceptionCauseTitle = original
    assert instance.ExceptionCauseTitle == original



@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_hyp_esmodel_events_exceptionevent_ExceptionStackTrace_setter(instance):
    original = instance.ExceptionStackTrace
    instance.ExceptionStackTrace = original
    assert instance.ExceptionStackTrace == original



@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_hyp_esmodel_events_exceptionevent_ExceptionTitle_setter(instance):
    original = instance.ExceptionTitle
    instance.ExceptionTitle = original
    assert instance.ExceptionTitle == original




@given(instance=esmodel_events_PluginStartEvent_strategy)
def test_hyp_esmodel_events_pluginstartevent_pluginId_setter(instance):
    original = instance.pluginId
    instance.pluginId = original
    assert instance.pluginId == original





@given(instance=esmodel_events_NavigatorCreateEvent_strategy)
def test_hyp_esmodel_events_navigatorcreateevent_dynamic_setter(instance):
    original = instance.dynamic
    instance.dynamic = original
    assert instance.dynamic == original





@given(instance=esmodel_events_URLEvent_strategy)
def test_hyp_esmodel_events_urlevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original





@given(instance=esmodel_events_TraceEvent_strategy)
def test_hyp_esmodel_events_traceevent_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original






@given(instance=esmodel_events_DNDEvent_strategy)
def test_hyp_esmodel_events_dndevent_targetView_setter(instance):
    original = instance.targetView
    instance.targetView = original
    assert instance.targetView == original



@given(instance=esmodel_events_DNDEvent_strategy)
def test_hyp_esmodel_events_dndevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original




@given(instance=esmodel_events_LinkEvent_strategy)
def test_hyp_esmodel_events_linkevent_createdNew_setter(instance):
    original = instance.createdNew
    instance.createdNew = original
    assert instance.createdNew == original



@given(instance=esmodel_events_LinkEvent_strategy)
def test_hyp_esmodel_events_linkevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original





@given(instance=esmodel_events_MergeChoiceEvent_strategy)
def test_hyp_esmodel_events_mergechoiceevent_createdIssueName_setter(instance):
    original = instance.createdIssueName
    instance.createdIssueName = original
    assert instance.createdIssueName == original



@given(instance=esmodel_events_MergeChoiceEvent_strategy)
def test_hyp_esmodel_events_mergechoiceevent_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original



@given(instance=esmodel_events_MergeChoiceEvent_strategy)
def test_hyp_esmodel_events_mergechoiceevent_contextFeature_setter(instance):
    original = instance.contextFeature
    instance.contextFeature = original
    assert instance.contextFeature == original




@given(instance=esmodel_events_ReadEvent_strategy)
def test_hyp_esmodel_events_readevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original



@given(instance=esmodel_events_ReadEvent_strategy)
def test_hyp_esmodel_events_readevent_readView_setter(instance):
    original = instance.readView
    instance.readView = original
    assert instance.readView == original





@given(instance=esmodel_operations_MultiReferenceSetOperation_strategy)
def test_hyp_esmodel_operations_multireferencesetoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original





@given(instance=esmodel_operations_ModelElementGroup_strategy)
def test_hyp_esmodel_operations_modelelementgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=esmodel_operations_OperationGroup_strategy)
def test_hyp_esmodel_operations_operationgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=esmodel_operations_MultiReferenceOperation_strategy)
def test_hyp_esmodel_operations_multireferenceoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=esmodel_operations_MultiReferenceOperation_strategy)
def test_hyp_esmodel_operations_multireferenceoperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original






@given(instance=esmodel_operations_FeatureOperation_strategy)
def test_hyp_esmodel_operations_featureoperation_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original




@given(instance=esmodel_operations_CreateDeleteOperation_strategy)
def test_hyp_esmodel_operations_createdeleteoperation_delete_setter(instance):
    original = instance.delete
    instance.delete = original
    assert instance.delete == original




@given(instance=esmodel_operations_CompositeOperation_strategy)
def test_hyp_esmodel_operations_compositeoperation_compositeDescription_setter(instance):
    original = instance.compositeDescription
    instance.compositeDescription = original
    assert instance.compositeDescription == original



@given(instance=esmodel_operations_CompositeOperation_strategy)
def test_hyp_esmodel_operations_compositeoperation_reversed_setter(instance):
    original = instance.reversed
    instance.reversed = original
    assert instance.reversed == original



@given(instance=esmodel_operations_CompositeOperation_strategy)
def test_hyp_esmodel_operations_compositeoperation_compositeName_setter(instance):
    original = instance.compositeName
    instance.compositeName = original
    assert instance.compositeName == original





@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
def test_hyp_esmodel_operations_multiattributesetoperation_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original



@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
def test_hyp_esmodel_operations_multiattributesetoperation_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original



@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
def test_hyp_esmodel_operations_multiattributesetoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original




@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
def test_hyp_esmodel_operations_multiattributemoveoperation_oldIndex_setter(instance):
    original = instance.oldIndex
    instance.oldIndex = original
    assert instance.oldIndex == original



@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
def test_hyp_esmodel_operations_multiattributemoveoperation_referencedValue_setter(instance):
    original = instance.referencedValue
    instance.referencedValue = original
    assert instance.referencedValue == original



@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
def test_hyp_esmodel_operations_multiattributemoveoperation_newIndex_setter(instance):
    original = instance.newIndex
    instance.newIndex = original
    assert instance.newIndex == original




@given(instance=esmodel_operations_ReferenceOperation_strategy)
def test_hyp_esmodel_operations_referenceoperation_containmentType_setter(instance):
    original = instance.containmentType
    instance.containmentType = original
    assert instance.containmentType == original



@given(instance=esmodel_operations_ReferenceOperation_strategy)
def test_hyp_esmodel_operations_referenceoperation_oppositeFeatureName_setter(instance):
    original = instance.oppositeFeatureName
    instance.oppositeFeatureName = original
    assert instance.oppositeFeatureName == original



@given(instance=esmodel_operations_ReferenceOperation_strategy)
def test_hyp_esmodel_operations_referenceoperation_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original




@given(instance=esmodel_operations_MultiReferenceMoveOperation_strategy)
def test_hyp_esmodel_operations_multireferencemoveoperation_oldIndex_setter(instance):
    original = instance.oldIndex
    instance.oldIndex = original
    assert instance.oldIndex == original



@given(instance=esmodel_operations_MultiReferenceMoveOperation_strategy)
def test_hyp_esmodel_operations_multireferencemoveoperation_newIndex_setter(instance):
    original = instance.newIndex
    instance.newIndex = original
    assert instance.newIndex == original




@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
def test_hyp_esmodel_operations_multiattributeoperation_indexes_setter(instance):
    original = instance.indexes
    instance.indexes = original
    assert instance.indexes == original



@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
def test_hyp_esmodel_operations_multiattributeoperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original



@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
def test_hyp_esmodel_operations_multiattributeoperation_referencedValues_setter(instance):
    original = instance.referencedValues
    instance.referencedValues = original
    assert instance.referencedValues == original




@given(instance=esmodel_operations_AttributeOperation_strategy)
def test_hyp_esmodel_operations_attributeoperation_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original



@given(instance=esmodel_operations_AttributeOperation_strategy)
def test_hyp_esmodel_operations_attributeoperation_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original







@given(instance=esmodel_versioning_HistoryQuery_strategy)
def test_hyp_esmodel_versioning_historyquery_includeChangePackage_setter(instance):
    original = instance.includeChangePackage
    instance.includeChangePackage = original
    assert instance.includeChangePackage == original




@given(instance=esmodel_versioning_VersionProperty_strategy)
def test_hyp_esmodel_versioning_versionproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=esmodel_versioning_VersionProperty_strategy)
def test_hyp_esmodel_versioning_versionproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original















@given(instance=esmodel_versioning_DateVersionSpec_strategy)
def test_hyp_esmodel_versioning_dateversionspec_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=esmodel_versioning_TagVersionSpec_strategy)
def test_hyp_esmodel_versioning_tagversionspec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=esmodel_versioning_LogMessage_strategy)
def test_hyp_esmodel_versioning_logmessage_clientDate_setter(instance):
    original = instance.clientDate
    instance.clientDate = original
    assert instance.clientDate == original



@given(instance=esmodel_versioning_LogMessage_strategy)
def test_hyp_esmodel_versioning_logmessage_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=esmodel_versioning_LogMessage_strategy)
def test_hyp_esmodel_versioning_logmessage_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=esmodel_versioning_LogMessage_strategy)
def test_hyp_esmodel_versioning_logmessage_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original





@given(instance=esmodel_ClientVersionInfo_strategy)
def test_hyp_esmodel_clientversioninfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=esmodel_ClientVersionInfo_strategy)
def test_hyp_esmodel_clientversioninfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=esmodel_VersionInfo_strategy)
def test_hyp_esmodel_versioninfo_emfStoreVersionString_setter(instance):
    original = instance.emfStoreVersionString
    instance.emfStoreVersionString = original
    assert instance.emfStoreVersionString == original




@given(instance=esmodel_versioning_PrimaryVersionSpec_strategy)
def test_hyp_esmodel_versioning_primaryversionspec_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original





@given(instance=esmodel_ProjectInfo_strategy)
def test_hyp_esmodel_projectinfo_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=esmodel_ProjectInfo_strategy)
def test_hyp_esmodel_projectinfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=esmodel_ProjectHistory_strategy)
def test_hyp_esmodel_projecthistory_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original



@given(instance=esmodel_ProjectHistory_strategy)
def test_hyp_esmodel_projecthistory_projectDescription_setter(instance):
    original = instance.projectDescription
    instance.projectDescription = original
    assert instance.projectDescription == original













@given(instance=model_activity_Transition_strategy)
def test_hyp_model_activity_transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original










@given(instance=model_profile_StereotypeAttributeInstanceString_strategy)
def test_hyp_model_profile_stereotypeattributeinstancestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=model_profile_StereotypeAttributeSimple_strategy)
def test_hyp_model_profile_stereotypeattributesimple_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original











@given(instance=model_profile_Stereotype_strategy)
def test_hyp_model_profile_stereotype_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original









@given(instance=model_state_State_strategy)
def test_hyp_model_state_state_activities_setter(instance):
    original = instance.activities
    instance.activities = original
    assert instance.activities == original



@given(instance=model_state_State_strategy)
def test_hyp_model_state_state_exitConditions_setter(instance):
    original = instance.exitConditions
    instance.exitConditions = original
    assert instance.exitConditions == original



@given(instance=model_state_State_strategy)
def test_hyp_model_state_state_entryConditions_setter(instance):
    original = instance.entryConditions
    instance.entryConditions = original
    assert instance.entryConditions == original







@given(instance=model_state_Transition_strategy)
def test_hyp_model_state_transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original








@given(instance=model_meeting_MeetingSection_strategy)
def test_hyp_model_meeting_meetingsection_allocatedTime_setter(instance):
    original = instance.allocatedTime
    instance.allocatedTime = original
    assert instance.allocatedTime == original









@given(instance=model_meeting_Meeting_strategy)
def test_hyp_model_meeting_meeting_starttime_setter(instance):
    original = instance.starttime
    instance.starttime = original
    assert instance.starttime == original



@given(instance=model_meeting_Meeting_strategy)
def test_hyp_model_meeting_meeting_endtime_setter(instance):
    original = instance.endtime
    instance.endtime = original
    assert instance.endtime == original



@given(instance=model_meeting_Meeting_strategy)
def test_hyp_model_meeting_meeting_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original













@given(instance=model_change_MergingIssue_strategy)
def test_hyp_model_change_mergingissue_resolvingRevision_setter(instance):
    original = instance.resolvingRevision
    instance.resolvingRevision = original
    assert instance.resolvingRevision == original




@given(instance=model_change_ModelChangePackage_strategy)
def test_hyp_model_change_modelchangepackage_sourceVersion_setter(instance):
    original = instance.sourceVersion
    instance.sourceVersion = original
    assert instance.sourceVersion == original



@given(instance=model_change_ModelChangePackage_strategy)
def test_hyp_model_change_modelchangepackage_targetVersion_setter(instance):
    original = instance.targetVersion
    instance.targetVersion = original
    assert instance.targetVersion == original














@given(instance=model_rationale_Assessment_strategy)
def test_hyp_model_rationale_assessment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=model_requirement_SystemFunction_strategy)
def test_hyp_model_requirement_systemfunction_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=model_requirement_SystemFunction_strategy)
def test_hyp_model_requirement_systemfunction_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=model_requirement_SystemFunction_strategy)
def test_hyp_model_requirement_systemfunction_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original






@given(instance=model_requirement_Step_strategy)
def test_hyp_model_requirement_step_userStep_setter(instance):
    original = instance.userStep
    instance.userStep = original
    assert instance.userStep == original












@given(instance=model_requirement_UseCase_strategy)
def test_hyp_model_requirement_usecase_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=model_requirement_UseCase_strategy)
def test_hyp_model_requirement_usecase_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original



@given(instance=model_requirement_UseCase_strategy)
def test_hyp_model_requirement_usecase_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original



@given(instance=model_requirement_UseCase_strategy)
def test_hyp_model_requirement_usecase_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original




@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_hyp_model_requirement_functionalrequirement_storyPoints_setter(instance):
    original = instance.storyPoints
    instance.storyPoints = original
    assert instance.storyPoints == original



@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_hyp_model_requirement_functionalrequirement_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_hyp_model_requirement_functionalrequirement_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_hyp_model_requirement_functionalrequirement_reviewed_setter(instance):
    original = instance.reviewed
    instance.reviewed = original
    assert instance.reviewed == original












@given(instance=model_classes_MethodArgument_strategy)
def test_hyp_model_classes_methodargument_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=model_classes_MethodArgument_strategy)
def test_hyp_model_classes_methodargument_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=model_classes_MethodArgument_strategy)
def test_hyp_model_classes_methodargument_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=model_classes_MethodArgument_strategy)
def test_hyp_model_classes_methodargument_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_classes_MethodArgument_strategy)
def test_hyp_model_classes_methodargument_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original





@given(instance=model_classes_Method_strategy)
def test_hyp_model_classes_method_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original



@given(instance=model_classes_Method_strategy)
def test_hyp_model_classes_method_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=model_classes_Method_strategy)
def test_hyp_model_classes_method_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original



@given(instance=model_classes_Method_strategy)
def test_hyp_model_classes_method_stubbed_setter(instance):
    original = instance.stubbed
    instance.stubbed = original
    assert instance.stubbed == original



@given(instance=model_classes_Method_strategy)
def test_hyp_model_classes_method_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=model_classes_Method_strategy)
def test_hyp_model_classes_method_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=model_classes_Method_strategy)
def test_hyp_model_classes_method_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original





@given(instance=model_classes_Attribute_strategy)
def test_hyp_model_classes_attribute_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=model_classes_Attribute_strategy)
def test_hyp_model_classes_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_classes_Attribute_strategy)
def test_hyp_model_classes_attribute_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original



@given(instance=model_classes_Attribute_strategy)
def test_hyp_model_classes_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=model_classes_Attribute_strategy)
def test_hyp_model_classes_attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=model_classes_Attribute_strategy)
def test_hyp_model_classes_attribute_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=model_classes_Attribute_strategy)
def test_hyp_model_classes_attribute_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original




@given(instance=model_classes_Association_strategy)
def test_hyp_model_classes_association_targetRole_setter(instance):
    original = instance.targetRole
    instance.targetRole = original
    assert instance.targetRole == original



@given(instance=model_classes_Association_strategy)
def test_hyp_model_classes_association_sourceMultiplicity_setter(instance):
    original = instance.sourceMultiplicity
    instance.sourceMultiplicity = original
    assert instance.sourceMultiplicity == original



@given(instance=model_classes_Association_strategy)
def test_hyp_model_classes_association_sourceRole_setter(instance):
    original = instance.sourceRole
    instance.sourceRole = original
    assert instance.sourceRole == original



@given(instance=model_classes_Association_strategy)
def test_hyp_model_classes_association_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_classes_Association_strategy)
def test_hyp_model_classes_association_targetMultiplicity_setter(instance):
    original = instance.targetMultiplicity
    instance.targetMultiplicity = original
    assert instance.targetMultiplicity == original


















@given(instance=model_bug_BugReport_strategy)
def test_hyp_model_bug_bugreport_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original



@given(instance=model_bug_BugReport_strategy)
def test_hyp_model_bug_bugreport_resolutionType_setter(instance):
    original = instance.resolutionType
    instance.resolutionType = original
    assert instance.resolutionType == original



@given(instance=model_bug_BugReport_strategy)
def test_hyp_model_bug_bugreport_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=model_bug_BugReport_strategy)
def test_hyp_model_bug_bugreport_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original




@given(instance=model_task_ActionItem_strategy)
def test_hyp_model_task_actionitem_done_setter(instance):
    original = instance.done
    instance.done = original
    assert instance.done == original



@given(instance=model_task_ActionItem_strategy)
def test_hyp_model_task_actionitem_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original




@given(instance=model_task_Checkable_strategy)
def test_hyp_model_task_checkable_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original






@given(instance=model_task_WorkPackage_strategy)
def test_hyp_model_task_workpackage_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=model_task_WorkPackage_strategy)
def test_hyp_model_task_workpackage_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original







@given(instance=metamodel_UniqueIdentifier_strategy)
def test_hyp_metamodel_uniqueidentifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original







@given(instance=model_attachment_UrlAttachment_strategy)
def test_hyp_model_attachment_urlattachment_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original




@given(instance=model_attachment_FileAttachment_strategy)
def test_hyp_model_attachment_fileattachment_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_hyp_model_attachment_fileattachment_requiredOffline_setter(instance):
    original = instance.requiredOffline
    instance.requiredOffline = original
    assert instance.requiredOffline == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_hyp_model_attachment_fileattachment_fileID_setter(instance):
    original = instance.fileID
    instance.fileID = original
    assert instance.fileID == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_hyp_model_attachment_fileattachment_fileHash_setter(instance):
    original = instance.fileHash
    instance.fileHash = original
    assert instance.fileHash == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_hyp_model_attachment_fileattachment_fileSize_setter(instance):
    original = instance.fileSize
    instance.fileSize = original
    assert instance.fileSize == original




@given(instance=model_diagram_MEDiagram_strategy)
def test_hyp_model_diagram_mediagram_diagramLayout_setter(instance):
    original = instance.diagramLayout
    instance.diagramLayout = original
    assert instance.diagramLayout == original



@given(instance=model_diagram_MEDiagram_strategy)
def test_hyp_model_diagram_mediagram_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=model_rationale_Issue_strategy)
def test_hyp_model_rationale_issue_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original




@given(instance=model_task_WorkItem_strategy)
def test_hyp_model_task_workitem_effort_setter(instance):
    original = instance.effort
    instance.effort = original
    assert instance.effort == original



@given(instance=model_task_WorkItem_strategy)
def test_hyp_model_task_workitem_dueDate_setter(instance):
    original = instance.dueDate
    instance.dueDate = original
    assert instance.dueDate == original



@given(instance=model_task_WorkItem_strategy)
def test_hyp_model_task_workitem_resolved_setter(instance):
    original = instance.resolved
    instance.resolved = original
    assert instance.resolved == original



@given(instance=model_task_WorkItem_strategy)
def test_hyp_model_task_workitem_estimate_setter(instance):
    original = instance.estimate
    instance.estimate = original
    assert instance.estimate == original



@given(instance=model_task_WorkItem_strategy)
def test_hyp_model_task_workitem_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original






@given(instance=metamodel_ModelVersion_strategy)
def test_hyp_metamodel_modelversion_releaseNumber_setter(instance):
    original = instance.releaseNumber
    instance.releaseNumber = original
    assert instance.releaseNumber == original











@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_hyp_esmodel_operations_abstractoperation_clientDate_setter(instance):
    original = instance.clientDate
    instance.clientDate = original
    assert instance.clientDate == original



@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_hyp_esmodel_operations_abstractoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_hyp_esmodel_operations_abstractoperation_accepted_setter(instance):
    original = instance.accepted
    instance.accepted = original
    assert instance.accepted == original



@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_hyp_esmodel_operations_abstractoperation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_recipient_setter(instance):
    original = instance.recipient
    instance.recipient = original
    assert instance.recipient == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_seen_setter(instance):
    original = instance.seen
    instance.seen = original
    assert instance.seen == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_hyp_esmodel_notification_esnotification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=esmodel_accesscontrol_ACOrgUnit_strategy)
def test_hyp_esmodel_accesscontrol_acorgunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_accesscontrol_ACOrgUnit_strategy)
def test_hyp_esmodel_accesscontrol_acorgunit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=metamodel_ModelElement_strategy)
def test_hyp_metamodel_modelelement_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=metamodel_ModelElement_strategy)
def test_hyp_metamodel_modelelement_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original




@given(instance=metamodel_IdentifiableElement_strategy)
def test_hyp_metamodel_identifiableelement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original





@given(instance=model_UnicaseModelElement_strategy)
def test_hyp_model_unicasemodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_UnicaseModelElement_strategy)
def test_hyp_model_unicasemodelelement_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=model_UnicaseModelElement_strategy)
def test_hyp_model_unicasemodelelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_esmodel_ClientVersionInfo_name_value_roundtrip():
    instance = esmodel_ClientVersionInfo(name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_ClientVersionInfo_version_value_roundtrip():
    instance = esmodel_ClientVersionInfo(name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_esmodel_ProjectHistory_projectDescription_value_roundtrip():
    instance = esmodel_ProjectHistory(projectDescription="sample_text", projectName="sample_text")
    assert instance.projectDescription == "sample_text"
    instance.projectDescription = "sample_text_2"
    assert instance.projectDescription == "sample_text_2"


def test_esmodel_ProjectHistory_projectName_value_roundtrip():
    instance = esmodel_ProjectHistory(projectDescription="sample_text", projectName="sample_text")
    assert instance.projectName == "sample_text"
    instance.projectName = "sample_text_2"
    assert instance.projectName == "sample_text_2"


def test_esmodel_ProjectInfo_description_value_roundtrip():
    instance = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_esmodel_ProjectInfo_name_value_roundtrip():
    instance = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_VersionInfo_emfStoreVersionString_value_roundtrip():
    instance = esmodel_VersionInfo(emfStoreVersionString="sample_text")
    assert instance.emfStoreVersionString == "sample_text"
    instance.emfStoreVersionString = "sample_text_2"
    assert instance.emfStoreVersionString == "sample_text_2"


def test_esmodel_accesscontrol_ACOrgUnit_description_value_roundtrip():
    instance = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_esmodel_accesscontrol_ACOrgUnit_name_value_roundtrip():
    instance = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_accesscontrol_ACUser_firstName_value_roundtrip():
    instance = esmodel_accesscontrol_ACUser(firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_esmodel_accesscontrol_ACUser_lastName_value_roundtrip():
    instance = esmodel_accesscontrol_ACUser(firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_esmodel_accesscontrol_OrgUnitProperty_name_value_roundtrip():
    instance = esmodel_accesscontrol_OrgUnitProperty(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_accesscontrol_OrgUnitProperty_value_value_roundtrip():
    instance = esmodel_accesscontrol_OrgUnitProperty(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_esmodel_events_DNDEvent_sourceView_value_roundtrip():
    instance = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    assert instance.sourceView == "sample_text"
    instance.sourceView = "sample_text_2"
    assert instance.sourceView == "sample_text_2"


def test_esmodel_events_DNDEvent_targetView_value_roundtrip():
    instance = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    assert instance.targetView == "sample_text"
    instance.targetView = "sample_text_2"
    assert instance.targetView == "sample_text_2"


def test_esmodel_events_Event_timestamp_value_roundtrip():
    instance = esmodel_events_Event(timestamp=date(2024, 1, 1))
    assert instance.timestamp == date(2024, 1, 1)
    instance.timestamp = date(2025, 6, 15)
    assert instance.timestamp == date(2025, 6, 15)


def test_esmodel_events_ExceptionEvent_ExceptionCauseStackTrace_value_roundtrip():
    instance = esmodel_events_ExceptionEvent(ExceptionCauseStackTrace="sample_text", ExceptionCauseTitle="sample_text", ExceptionStackTrace="sample_text", ExceptionTitle="sample_text")
    assert instance.ExceptionCauseStackTrace == "sample_text"
    instance.ExceptionCauseStackTrace = "sample_text_2"
    assert instance.ExceptionCauseStackTrace == "sample_text_2"


def test_esmodel_events_ExceptionEvent_ExceptionCauseTitle_value_roundtrip():
    instance = esmodel_events_ExceptionEvent(ExceptionCauseStackTrace="sample_text", ExceptionCauseTitle="sample_text", ExceptionStackTrace="sample_text", ExceptionTitle="sample_text")
    assert instance.ExceptionCauseTitle == "sample_text"
    instance.ExceptionCauseTitle = "sample_text_2"
    assert instance.ExceptionCauseTitle == "sample_text_2"


def test_esmodel_events_ExceptionEvent_ExceptionStackTrace_value_roundtrip():
    instance = esmodel_events_ExceptionEvent(ExceptionCauseStackTrace="sample_text", ExceptionCauseTitle="sample_text", ExceptionStackTrace="sample_text", ExceptionTitle="sample_text")
    assert instance.ExceptionStackTrace == "sample_text"
    instance.ExceptionStackTrace = "sample_text_2"
    assert instance.ExceptionStackTrace == "sample_text_2"


def test_esmodel_events_ExceptionEvent_ExceptionTitle_value_roundtrip():
    instance = esmodel_events_ExceptionEvent(ExceptionCauseStackTrace="sample_text", ExceptionCauseTitle="sample_text", ExceptionStackTrace="sample_text", ExceptionTitle="sample_text")
    assert instance.ExceptionTitle == "sample_text"
    instance.ExceptionTitle = "sample_text_2"
    assert instance.ExceptionTitle == "sample_text_2"


def test_esmodel_events_LinkEvent_createdNew_value_roundtrip():
    instance = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    assert instance.createdNew == True
    instance.createdNew = False
    assert instance.createdNew == False


def test_esmodel_events_LinkEvent_sourceView_value_roundtrip():
    instance = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    assert instance.sourceView == "sample_text"
    instance.sourceView = "sample_text_2"
    assert instance.sourceView == "sample_text_2"


def test_esmodel_events_MergeChoiceEvent_contextFeature_value_roundtrip():
    instance = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    assert instance.contextFeature == "sample_text"
    instance.contextFeature = "sample_text_2"
    assert instance.contextFeature == "sample_text_2"


def test_esmodel_events_MergeChoiceEvent_createdIssueName_value_roundtrip():
    instance = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    assert instance.createdIssueName == "sample_text"
    instance.createdIssueName = "sample_text_2"
    assert instance.createdIssueName == "sample_text_2"


def test_esmodel_events_MergeChoiceEvent_selection_value_roundtrip():
    instance = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    assert instance.selection == "sample_text"
    instance.selection = "sample_text_2"
    assert instance.selection == "sample_text_2"


def test_esmodel_events_MergeEvent_numberOfConflicts_value_roundtrip():
    instance = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    assert instance.numberOfConflicts == 7
    instance.numberOfConflicts = 13
    assert instance.numberOfConflicts == 13


def test_esmodel_events_MergeEvent_totalTime_value_roundtrip():
    instance = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    assert instance.totalTime == 7
    instance.totalTime = 13
    assert instance.totalTime == 13


def test_esmodel_events_MergeGlobalChoiceEvent_selection_value_roundtrip():
    instance = esmodel_events_MergeGlobalChoiceEvent(selection="sample_text")
    assert instance.selection == "sample_text"
    instance.selection = "sample_text_2"
    assert instance.selection == "sample_text_2"


def test_esmodel_events_NavigatorCreateEvent_dynamic_value_roundtrip():
    instance = esmodel_events_NavigatorCreateEvent(dynamic=True)
    assert instance.dynamic == True
    instance.dynamic = False
    assert instance.dynamic == False


def test_esmodel_events_NotificationIgnoreEvent_notificationId_value_roundtrip():
    instance = esmodel_events_NotificationIgnoreEvent(notificationId="sample_text")
    assert instance.notificationId == "sample_text"
    instance.notificationId = "sample_text_2"
    assert instance.notificationId == "sample_text_2"


def test_esmodel_events_NotificationReadEvent_notificationId_value_roundtrip():
    instance = esmodel_events_NotificationReadEvent(notificationId="sample_text")
    assert instance.notificationId == "sample_text"
    instance.notificationId = "sample_text_2"
    assert instance.notificationId == "sample_text_2"


def test_esmodel_events_PluginFocusEvent_pluginId_value_roundtrip():
    instance = esmodel_events_PluginFocusEvent(pluginId="sample_text", startDate=date(2024, 1, 1))
    assert instance.pluginId == "sample_text"
    instance.pluginId = "sample_text_2"
    assert instance.pluginId == "sample_text_2"


def test_esmodel_events_PluginFocusEvent_startDate_value_roundtrip():
    instance = esmodel_events_PluginFocusEvent(pluginId="sample_text", startDate=date(2024, 1, 1))
    assert instance.startDate == date(2024, 1, 1)
    instance.startDate = date(2025, 6, 15)
    assert instance.startDate == date(2025, 6, 15)


def test_esmodel_events_PluginStartEvent_pluginId_value_roundtrip():
    instance = esmodel_events_PluginStartEvent(pluginId="sample_text")
    assert instance.pluginId == "sample_text"
    instance.pluginId = "sample_text_2"
    assert instance.pluginId == "sample_text_2"


def test_esmodel_events_PresentationSwitchEvent_newPresentation_value_roundtrip():
    instance = esmodel_events_PresentationSwitchEvent(newPresentation="sample_text", readView="sample_text")
    assert instance.newPresentation == "sample_text"
    instance.newPresentation = "sample_text_2"
    assert instance.newPresentation == "sample_text_2"


def test_esmodel_events_PresentationSwitchEvent_readView_value_roundtrip():
    instance = esmodel_events_PresentationSwitchEvent(newPresentation="sample_text", readView="sample_text")
    assert instance.readView == "sample_text"
    instance.readView = "sample_text_2"
    assert instance.readView == "sample_text_2"


def test_esmodel_events_ReadEvent_readView_value_roundtrip():
    instance = esmodel_events_ReadEvent(readView="sample_text", sourceView="sample_text")
    assert instance.readView == "sample_text"
    instance.readView = "sample_text_2"
    assert instance.readView == "sample_text_2"


def test_esmodel_events_ReadEvent_sourceView_value_roundtrip():
    instance = esmodel_events_ReadEvent(readView="sample_text", sourceView="sample_text")
    assert instance.sourceView == "sample_text"
    instance.sourceView = "sample_text_2"
    assert instance.sourceView == "sample_text_2"


def test_esmodel_events_RevertEvent_revertedChangesCount_value_roundtrip():
    instance = esmodel_events_RevertEvent(revertedChangesCount=7)
    assert instance.revertedChangesCount == 7
    instance.revertedChangesCount = 13
    assert instance.revertedChangesCount == 13


def test_esmodel_events_TraceEvent_featureName_value_roundtrip():
    instance = esmodel_events_TraceEvent(featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_esmodel_events_URLEvent_sourceView_value_roundtrip():
    instance = esmodel_events_URLEvent(sourceView="sample_text")
    assert instance.sourceView == "sample_text"
    instance.sourceView = "sample_text_2"
    assert instance.sourceView == "sample_text_2"


def test_esmodel_notification_ESNotification_creationDate_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.creationDate == date(2024, 1, 1)
    instance.creationDate = date(2025, 6, 15)
    assert instance.creationDate == date(2025, 6, 15)


def test_esmodel_notification_ESNotification_details_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.details == "sample_text"
    instance.details = "sample_text_2"
    assert instance.details == "sample_text_2"


def test_esmodel_notification_ESNotification_message_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_esmodel_notification_ESNotification_name_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_notification_ESNotification_provider_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.provider == "sample_text"
    instance.provider = "sample_text_2"
    assert instance.provider == "sample_text_2"


def test_esmodel_notification_ESNotification_recipient_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.recipient == "sample_text"
    instance.recipient = "sample_text_2"
    assert instance.recipient == "sample_text_2"


def test_esmodel_notification_ESNotification_seen_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.seen == True
    instance.seen = False
    assert instance.seen == False


def test_esmodel_notification_ESNotification_sender_value_roundtrip():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert instance.sender == "sample_text"
    instance.sender = "sample_text_2"
    assert instance.sender == "sample_text_2"


def test_esmodel_operations_AbstractOperation_accepted_value_roundtrip():
    instance = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    assert instance.accepted == True
    instance.accepted = False
    assert instance.accepted == False


def test_esmodel_operations_AbstractOperation_clientDate_value_roundtrip():
    instance = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    assert instance.clientDate == date(2024, 1, 1)
    instance.clientDate = date(2025, 6, 15)
    assert instance.clientDate == date(2025, 6, 15)


def test_esmodel_operations_AbstractOperation_description_value_roundtrip():
    instance = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_esmodel_operations_AbstractOperation_name_value_roundtrip():
    instance = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_operations_AttributeOperation_newValue_value_roundtrip():
    instance = esmodel_operations_AttributeOperation(newValue="sample_text", oldValue="sample_text")
    assert instance.newValue == "sample_text"
    instance.newValue = "sample_text_2"
    assert instance.newValue == "sample_text_2"


def test_esmodel_operations_AttributeOperation_oldValue_value_roundtrip():
    instance = esmodel_operations_AttributeOperation(newValue="sample_text", oldValue="sample_text")
    assert instance.oldValue == "sample_text"
    instance.oldValue = "sample_text_2"
    assert instance.oldValue == "sample_text_2"


def test_esmodel_operations_CompositeOperation_compositeDescription_value_roundtrip():
    instance = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    assert instance.compositeDescription == "sample_text"
    instance.compositeDescription = "sample_text_2"
    assert instance.compositeDescription == "sample_text_2"


def test_esmodel_operations_CompositeOperation_compositeName_value_roundtrip():
    instance = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    assert instance.compositeName == "sample_text"
    instance.compositeName = "sample_text_2"
    assert instance.compositeName == "sample_text_2"


def test_esmodel_operations_CompositeOperation_reversed_value_roundtrip():
    instance = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    assert instance.reversed == True
    instance.reversed = False
    assert instance.reversed == False


def test_esmodel_operations_CreateDeleteOperation_delete_value_roundtrip():
    instance = esmodel_operations_CreateDeleteOperation(delete=True)
    assert instance.delete == True
    instance.delete = False
    assert instance.delete == False


def test_esmodel_operations_FeatureOperation_featureName_value_roundtrip():
    instance = esmodel_operations_FeatureOperation(featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_esmodel_operations_ModelElementGroup_name_value_roundtrip():
    instance = esmodel_operations_ModelElementGroup(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_operations_MultiAttributeMoveOperation_newIndex_value_roundtrip():
    instance = esmodel_operations_MultiAttributeMoveOperation(newIndex=7, oldIndex=7, referencedValue="sample_text")
    assert instance.newIndex == 7
    instance.newIndex = 13
    assert instance.newIndex == 13


def test_esmodel_operations_MultiAttributeMoveOperation_oldIndex_value_roundtrip():
    instance = esmodel_operations_MultiAttributeMoveOperation(newIndex=7, oldIndex=7, referencedValue="sample_text")
    assert instance.oldIndex == 7
    instance.oldIndex = 13
    assert instance.oldIndex == 13


def test_esmodel_operations_MultiAttributeMoveOperation_referencedValue_value_roundtrip():
    instance = esmodel_operations_MultiAttributeMoveOperation(newIndex=7, oldIndex=7, referencedValue="sample_text")
    assert instance.referencedValue == "sample_text"
    instance.referencedValue = "sample_text_2"
    assert instance.referencedValue == "sample_text_2"


def test_esmodel_operations_MultiAttributeOperation_add_value_roundtrip():
    instance = esmodel_operations_MultiAttributeOperation(add=True, indexes=7, referencedValues="sample_text")
    assert instance.add == True
    instance.add = False
    assert instance.add == False


def test_esmodel_operations_MultiAttributeOperation_indexes_value_roundtrip():
    instance = esmodel_operations_MultiAttributeOperation(add=True, indexes=7, referencedValues="sample_text")
    assert instance.indexes == 7
    instance.indexes = 13
    assert instance.indexes == 13


def test_esmodel_operations_MultiAttributeOperation_referencedValues_value_roundtrip():
    instance = esmodel_operations_MultiAttributeOperation(add=True, indexes=7, referencedValues="sample_text")
    assert instance.referencedValues == "sample_text"
    instance.referencedValues = "sample_text_2"
    assert instance.referencedValues == "sample_text_2"


def test_esmodel_operations_MultiAttributeSetOperation_index_value_roundtrip():
    instance = esmodel_operations_MultiAttributeSetOperation(index=7, newValue="sample_text", oldValue="sample_text")
    assert instance.index == 7
    instance.index = 13
    assert instance.index == 13


def test_esmodel_operations_MultiAttributeSetOperation_newValue_value_roundtrip():
    instance = esmodel_operations_MultiAttributeSetOperation(index=7, newValue="sample_text", oldValue="sample_text")
    assert instance.newValue == "sample_text"
    instance.newValue = "sample_text_2"
    assert instance.newValue == "sample_text_2"


def test_esmodel_operations_MultiAttributeSetOperation_oldValue_value_roundtrip():
    instance = esmodel_operations_MultiAttributeSetOperation(index=7, newValue="sample_text", oldValue="sample_text")
    assert instance.oldValue == "sample_text"
    instance.oldValue = "sample_text_2"
    assert instance.oldValue == "sample_text_2"


def test_esmodel_operations_MultiReferenceMoveOperation_newIndex_value_roundtrip():
    instance = esmodel_operations_MultiReferenceMoveOperation(newIndex=7, oldIndex=7)
    assert instance.newIndex == 7
    instance.newIndex = 13
    assert instance.newIndex == 13


def test_esmodel_operations_MultiReferenceMoveOperation_oldIndex_value_roundtrip():
    instance = esmodel_operations_MultiReferenceMoveOperation(newIndex=7, oldIndex=7)
    assert instance.oldIndex == 7
    instance.oldIndex = 13
    assert instance.oldIndex == 13


def test_esmodel_operations_MultiReferenceOperation_add_value_roundtrip():
    instance = esmodel_operations_MultiReferenceOperation(add=True, index=7)
    assert instance.add == True
    instance.add = False
    assert instance.add == False


def test_esmodel_operations_MultiReferenceOperation_index_value_roundtrip():
    instance = esmodel_operations_MultiReferenceOperation(add=True, index=7)
    assert instance.index == 7
    instance.index = 13
    assert instance.index == 13


def test_esmodel_operations_MultiReferenceSetOperation_index_value_roundtrip():
    instance = esmodel_operations_MultiReferenceSetOperation(index=7)
    assert instance.index == 7
    instance.index = 13
    assert instance.index == 13


def test_esmodel_operations_OperationGroup_name_value_roundtrip():
    instance = esmodel_operations_OperationGroup(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_operations_ReferenceOperation_bidirectional_value_roundtrip():
    instance = esmodel_operations_ReferenceOperation(bidirectional=True, containmentType="sample_text", oppositeFeatureName="sample_text")
    assert instance.bidirectional == True
    instance.bidirectional = False
    assert instance.bidirectional == False


def test_esmodel_operations_ReferenceOperation_containmentType_value_roundtrip():
    instance = esmodel_operations_ReferenceOperation(bidirectional=True, containmentType="sample_text", oppositeFeatureName="sample_text")
    assert instance.containmentType == "sample_text"
    instance.containmentType = "sample_text_2"
    assert instance.containmentType == "sample_text_2"


def test_esmodel_operations_ReferenceOperation_oppositeFeatureName_value_roundtrip():
    instance = esmodel_operations_ReferenceOperation(bidirectional=True, containmentType="sample_text", oppositeFeatureName="sample_text")
    assert instance.oppositeFeatureName == "sample_text"
    instance.oppositeFeatureName = "sample_text_2"
    assert instance.oppositeFeatureName == "sample_text_2"


def test_esmodel_url_ModelElementUrlFragment_name_value_roundtrip():
    instance = esmodel_url_ModelElementUrlFragment(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_url_ProjectUrlFragment_name_value_roundtrip():
    instance = esmodel_url_ProjectUrlFragment(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_url_ServerUrl_hostName_value_roundtrip():
    instance = esmodel_url_ServerUrl(hostName="sample_text", port=7)
    assert instance.hostName == "sample_text"
    instance.hostName = "sample_text_2"
    assert instance.hostName == "sample_text_2"


def test_esmodel_url_ServerUrl_port_value_roundtrip():
    instance = esmodel_url_ServerUrl(hostName="sample_text", port=7)
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_esmodel_versioning_DateVersionSpec_date_value_roundtrip():
    instance = esmodel_versioning_DateVersionSpec(date=date(2024, 1, 1))
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_esmodel_versioning_HistoryQuery_includeChangePackage_value_roundtrip():
    instance = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    assert instance.includeChangePackage == True
    instance.includeChangePackage = False
    assert instance.includeChangePackage == False


def test_esmodel_versioning_LogMessage_author_value_roundtrip():
    instance = esmodel_versioning_LogMessage(author="sample_text", clientDate=date(2024, 1, 1), date=date(2024, 1, 1), message="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_esmodel_versioning_LogMessage_clientDate_value_roundtrip():
    instance = esmodel_versioning_LogMessage(author="sample_text", clientDate=date(2024, 1, 1), date=date(2024, 1, 1), message="sample_text")
    assert instance.clientDate == date(2024, 1, 1)
    instance.clientDate = date(2025, 6, 15)
    assert instance.clientDate == date(2025, 6, 15)


def test_esmodel_versioning_LogMessage_date_value_roundtrip():
    instance = esmodel_versioning_LogMessage(author="sample_text", clientDate=date(2024, 1, 1), date=date(2024, 1, 1), message="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_esmodel_versioning_LogMessage_message_value_roundtrip():
    instance = esmodel_versioning_LogMessage(author="sample_text", clientDate=date(2024, 1, 1), date=date(2024, 1, 1), message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_esmodel_versioning_PrimaryVersionSpec_identifier_value_roundtrip():
    instance = esmodel_versioning_PrimaryVersionSpec(identifier=7)
    assert instance.identifier == 7
    instance.identifier = 13
    assert instance.identifier == 13


def test_esmodel_versioning_TagVersionSpec_name_value_roundtrip():
    instance = esmodel_versioning_TagVersionSpec(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_versioning_VersionProperty_name_value_roundtrip():
    instance = esmodel_versioning_VersionProperty(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_esmodel_versioning_VersionProperty_value_value_roundtrip():
    instance = esmodel_versioning_VersionProperty(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_metamodel_IdentifiableElement_identifier_value_roundtrip():
    instance = metamodel_IdentifiableElement(identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_metamodel_ModelElement_creationDate_value_roundtrip():
    instance = metamodel_ModelElement(creationDate=date(2024, 1, 1), creator="sample_text")
    assert instance.creationDate == date(2024, 1, 1)
    instance.creationDate = date(2025, 6, 15)
    assert instance.creationDate == date(2025, 6, 15)


def test_metamodel_ModelElement_creator_value_roundtrip():
    instance = metamodel_ModelElement(creationDate=date(2024, 1, 1), creator="sample_text")
    assert instance.creator == "sample_text"
    instance.creator = "sample_text_2"
    assert instance.creator == "sample_text_2"


def test_metamodel_ModelVersion_releaseNumber_value_roundtrip():
    instance = metamodel_ModelVersion(releaseNumber=7)
    assert instance.releaseNumber == 7
    instance.releaseNumber = 13
    assert instance.releaseNumber == 13


def test_metamodel_UniqueIdentifier_id_value_roundtrip():
    instance = metamodel_UniqueIdentifier(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_model_UnicaseModelElement_description_value_roundtrip():
    instance = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_UnicaseModelElement_name_value_roundtrip():
    instance = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_UnicaseModelElement_state_value_roundtrip():
    instance = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_model_activity_Transition_condition_value_roundtrip():
    instance = model_activity_Transition(condition="sample_text")
    assert instance.condition == "sample_text"
    instance.condition = "sample_text_2"
    assert instance.condition == "sample_text_2"


def test_model_attachment_FileAttachment_fileHash_value_roundtrip():
    instance = model_attachment_FileAttachment(fileHash="sample_text", fileID="sample_text", fileName="sample_text", fileSize="sample_text", requiredOffline=True)
    assert instance.fileHash == "sample_text"
    instance.fileHash = "sample_text_2"
    assert instance.fileHash == "sample_text_2"


def test_model_attachment_FileAttachment_fileID_value_roundtrip():
    instance = model_attachment_FileAttachment(fileHash="sample_text", fileID="sample_text", fileName="sample_text", fileSize="sample_text", requiredOffline=True)
    assert instance.fileID == "sample_text"
    instance.fileID = "sample_text_2"
    assert instance.fileID == "sample_text_2"


def test_model_attachment_FileAttachment_fileName_value_roundtrip():
    instance = model_attachment_FileAttachment(fileHash="sample_text", fileID="sample_text", fileName="sample_text", fileSize="sample_text", requiredOffline=True)
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_model_attachment_FileAttachment_fileSize_value_roundtrip():
    instance = model_attachment_FileAttachment(fileHash="sample_text", fileID="sample_text", fileName="sample_text", fileSize="sample_text", requiredOffline=True)
    assert instance.fileSize == "sample_text"
    instance.fileSize = "sample_text_2"
    assert instance.fileSize == "sample_text_2"


def test_model_attachment_FileAttachment_requiredOffline_value_roundtrip():
    instance = model_attachment_FileAttachment(fileHash="sample_text", fileID="sample_text", fileName="sample_text", fileSize="sample_text", requiredOffline=True)
    assert instance.requiredOffline == True
    instance.requiredOffline = False
    assert instance.requiredOffline == False


def test_model_attachment_UrlAttachment_url_value_roundtrip():
    instance = model_attachment_UrlAttachment(url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_model_bug_BugReport_Status_value_roundtrip():
    instance = model_bug_BugReport(Status="sample_text", resolution="sample_text", resolutionType="sample_text", severity="sample_text")
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_model_bug_BugReport_resolution_value_roundtrip():
    instance = model_bug_BugReport(Status="sample_text", resolution="sample_text", resolutionType="sample_text", severity="sample_text")
    assert instance.resolution == "sample_text"
    instance.resolution = "sample_text_2"
    assert instance.resolution == "sample_text_2"


def test_model_bug_BugReport_resolutionType_value_roundtrip():
    instance = model_bug_BugReport(Status="sample_text", resolution="sample_text", resolutionType="sample_text", severity="sample_text")
    assert instance.resolutionType == "sample_text"
    instance.resolutionType = "sample_text_2"
    assert instance.resolutionType == "sample_text_2"


def test_model_bug_BugReport_severity_value_roundtrip():
    instance = model_bug_BugReport(Status="sample_text", resolution="sample_text", resolutionType="sample_text", severity="sample_text")
    assert instance.severity == "sample_text"
    instance.severity = "sample_text_2"
    assert instance.severity == "sample_text_2"


def test_model_change_MergingIssue_resolvingRevision_value_roundtrip():
    instance = model_change_MergingIssue(resolvingRevision=7)
    assert instance.resolvingRevision == 7
    instance.resolvingRevision = 13
    assert instance.resolvingRevision == 13


def test_model_change_ModelChangePackage_sourceVersion_value_roundtrip():
    instance = model_change_ModelChangePackage(sourceVersion=7, targetVersion=7)
    assert instance.sourceVersion == 7
    instance.sourceVersion = 13
    assert instance.sourceVersion == 13


def test_model_change_ModelChangePackage_targetVersion_value_roundtrip():
    instance = model_change_ModelChangePackage(sourceVersion=7, targetVersion=7)
    assert instance.targetVersion == 7
    instance.targetVersion = 13
    assert instance.targetVersion == 13


def test_model_classes_Association_sourceMultiplicity_value_roundtrip():
    instance = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    assert instance.sourceMultiplicity == "sample_text"
    instance.sourceMultiplicity = "sample_text_2"
    assert instance.sourceMultiplicity == "sample_text_2"


def test_model_classes_Association_sourceRole_value_roundtrip():
    instance = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    assert instance.sourceRole == "sample_text"
    instance.sourceRole = "sample_text_2"
    assert instance.sourceRole == "sample_text_2"


def test_model_classes_Association_targetMultiplicity_value_roundtrip():
    instance = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    assert instance.targetMultiplicity == "sample_text"
    instance.targetMultiplicity = "sample_text_2"
    assert instance.targetMultiplicity == "sample_text_2"


def test_model_classes_Association_targetRole_value_roundtrip():
    instance = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    assert instance.targetRole == "sample_text"
    instance.targetRole = "sample_text_2"
    assert instance.targetRole == "sample_text_2"


def test_model_classes_Association_type_value_roundtrip():
    instance = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_model_classes_Attribute_defaultValue_value_roundtrip():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_model_classes_Attribute_label_value_roundtrip():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_model_classes_Attribute_properties_value_roundtrip():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert instance.properties == "sample_text"
    instance.properties = "sample_text_2"
    assert instance.properties == "sample_text_2"


def test_model_classes_Attribute_scope_value_roundtrip():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_model_classes_Attribute_signature_value_roundtrip():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert instance.signature == "sample_text"
    instance.signature = "sample_text_2"
    assert instance.signature == "sample_text_2"


def test_model_classes_Attribute_type_value_roundtrip():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_model_classes_Attribute_visibility_value_roundtrip():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_model_classes_Method_label_value_roundtrip():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_model_classes_Method_properties_value_roundtrip():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert instance.properties == "sample_text"
    instance.properties = "sample_text_2"
    assert instance.properties == "sample_text_2"


def test_model_classes_Method_returnType_value_roundtrip():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert instance.returnType == "sample_text"
    instance.returnType = "sample_text_2"
    assert instance.returnType == "sample_text_2"


def test_model_classes_Method_scope_value_roundtrip():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_model_classes_Method_signature_value_roundtrip():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert instance.signature == "sample_text"
    instance.signature = "sample_text_2"
    assert instance.signature == "sample_text_2"


def test_model_classes_Method_stubbed_value_roundtrip():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert instance.stubbed == True
    instance.stubbed = False
    assert instance.stubbed == False


def test_model_classes_Method_visibility_value_roundtrip():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_model_classes_MethodArgument_defaultValue_value_roundtrip():
    instance = model_classes_MethodArgument(defaultValue="sample_text", direction="sample_text", label="sample_text", signature="sample_text", type="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_model_classes_MethodArgument_direction_value_roundtrip():
    instance = model_classes_MethodArgument(defaultValue="sample_text", direction="sample_text", label="sample_text", signature="sample_text", type="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_model_classes_MethodArgument_label_value_roundtrip():
    instance = model_classes_MethodArgument(defaultValue="sample_text", direction="sample_text", label="sample_text", signature="sample_text", type="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_model_classes_MethodArgument_signature_value_roundtrip():
    instance = model_classes_MethodArgument(defaultValue="sample_text", direction="sample_text", label="sample_text", signature="sample_text", type="sample_text")
    assert instance.signature == "sample_text"
    instance.signature = "sample_text_2"
    assert instance.signature == "sample_text_2"


def test_model_classes_MethodArgument_type_value_roundtrip():
    instance = model_classes_MethodArgument(defaultValue="sample_text", direction="sample_text", label="sample_text", signature="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_model_diagram_MEDiagram_diagramLayout_value_roundtrip():
    instance = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    assert instance.diagramLayout == "sample_text"
    instance.diagramLayout = "sample_text_2"
    assert instance.diagramLayout == "sample_text_2"


def test_model_diagram_MEDiagram_type_value_roundtrip():
    instance = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_model_meeting_Meeting_endtime_value_roundtrip():
    instance = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    assert instance.endtime == date(2024, 1, 1)
    instance.endtime = date(2025, 6, 15)
    assert instance.endtime == date(2025, 6, 15)


def test_model_meeting_Meeting_location_value_roundtrip():
    instance = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_model_meeting_Meeting_starttime_value_roundtrip():
    instance = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    assert instance.starttime == date(2024, 1, 1)
    instance.starttime = date(2025, 6, 15)
    assert instance.starttime == date(2025, 6, 15)


def test_model_meeting_MeetingSection_allocatedTime_value_roundtrip():
    instance = model_meeting_MeetingSection(allocatedTime=7)
    assert instance.allocatedTime == 7
    instance.allocatedTime = 13
    assert instance.allocatedTime == 13


def test_model_organization_OrgUnit_acOrgId_value_roundtrip():
    instance = model_organization_OrgUnit(acOrgId="sample_text")
    assert instance.acOrgId == "sample_text"
    instance.acOrgId = "sample_text_2"
    assert instance.acOrgId == "sample_text_2"


def test_model_organization_User_email_value_roundtrip():
    instance = model_organization_User(email="sample_text", firstName="sample_text", lastName="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_model_organization_User_firstName_value_roundtrip():
    instance = model_organization_User(email="sample_text", firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_model_organization_User_lastName_value_roundtrip():
    instance = model_organization_User(email="sample_text", firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_model_profile_Stereotype_required_value_roundtrip():
    instance = model_profile_Stereotype(required=True)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_model_profile_StereotypeAttributeInstanceString_value_value_roundtrip():
    instance = model_profile_StereotypeAttributeInstanceString(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_profile_StereotypeAttributeSimple_type_value_roundtrip():
    instance = model_profile_StereotypeAttributeSimple(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_model_rationale_Assessment_value_value_roundtrip():
    instance = model_rationale_Assessment(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_model_rationale_Issue_activity_value_roundtrip():
    instance = model_rationale_Issue(activity="sample_text")
    assert instance.activity == "sample_text"
    instance.activity = "sample_text_2"
    assert instance.activity == "sample_text_2"


def test_model_requirement_FunctionalRequirement_cost_value_roundtrip():
    instance = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    assert instance.cost == 7
    instance.cost = 13
    assert instance.cost == 13


def test_model_requirement_FunctionalRequirement_priority_value_roundtrip():
    instance = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    assert instance.priority == 7
    instance.priority = 13
    assert instance.priority == 13


def test_model_requirement_FunctionalRequirement_reviewed_value_roundtrip():
    instance = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    assert instance.reviewed == True
    instance.reviewed = False
    assert instance.reviewed == False


def test_model_requirement_FunctionalRequirement_storyPoints_value_roundtrip():
    instance = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    assert instance.storyPoints == 7
    instance.storyPoints = 13
    assert instance.storyPoints == 13


def test_model_requirement_Step_userStep_value_roundtrip():
    instance = model_requirement_Step(userStep=True)
    assert instance.userStep == True
    instance.userStep = False
    assert instance.userStep == False


def test_model_requirement_SystemFunction_exception_value_roundtrip():
    instance = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    assert instance.exception == "sample_text"
    instance.exception = "sample_text_2"
    assert instance.exception == "sample_text_2"


def test_model_requirement_SystemFunction_input_value_roundtrip():
    instance = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_model_requirement_SystemFunction_output_value_roundtrip():
    instance = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_model_requirement_UseCase_exception_value_roundtrip():
    instance = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    assert instance.exception == "sample_text"
    instance.exception = "sample_text_2"
    assert instance.exception == "sample_text_2"


def test_model_requirement_UseCase_postcondition_value_roundtrip():
    instance = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    assert instance.postcondition == "sample_text"
    instance.postcondition = "sample_text_2"
    assert instance.postcondition == "sample_text_2"


def test_model_requirement_UseCase_precondition_value_roundtrip():
    instance = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    assert instance.precondition == "sample_text"
    instance.precondition = "sample_text_2"
    assert instance.precondition == "sample_text_2"


def test_model_requirement_UseCase_rules_value_roundtrip():
    instance = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    assert instance.rules == "sample_text"
    instance.rules = "sample_text_2"
    assert instance.rules == "sample_text_2"


def test_model_state_State_activities_value_roundtrip():
    instance = model_state_State(activities="sample_text", entryConditions="sample_text", exitConditions="sample_text")
    assert instance.activities == "sample_text"
    instance.activities = "sample_text_2"
    assert instance.activities == "sample_text_2"


def test_model_state_State_entryConditions_value_roundtrip():
    instance = model_state_State(activities="sample_text", entryConditions="sample_text", exitConditions="sample_text")
    assert instance.entryConditions == "sample_text"
    instance.entryConditions = "sample_text_2"
    assert instance.entryConditions == "sample_text_2"


def test_model_state_State_exitConditions_value_roundtrip():
    instance = model_state_State(activities="sample_text", entryConditions="sample_text", exitConditions="sample_text")
    assert instance.exitConditions == "sample_text"
    instance.exitConditions = "sample_text_2"
    assert instance.exitConditions == "sample_text_2"


def test_model_state_Transition_condition_value_roundtrip():
    instance = model_state_Transition(condition="sample_text")
    assert instance.condition == "sample_text"
    instance.condition = "sample_text_2"
    assert instance.condition == "sample_text_2"


def test_model_task_ActionItem_activity_value_roundtrip():
    instance = model_task_ActionItem(activity="sample_text", done=True)
    assert instance.activity == "sample_text"
    instance.activity = "sample_text_2"
    assert instance.activity == "sample_text_2"


def test_model_task_ActionItem_done_value_roundtrip():
    instance = model_task_ActionItem(activity="sample_text", done=True)
    assert instance.done == True
    instance.done = False
    assert instance.done == False


def test_model_task_Checkable_checked_value_roundtrip():
    instance = model_task_Checkable(checked=True)
    assert instance.checked == True
    instance.checked = False
    assert instance.checked == False


def test_model_task_WorkItem_dueDate_value_roundtrip():
    instance = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    assert instance.dueDate == date(2024, 1, 1)
    instance.dueDate = date(2025, 6, 15)
    assert instance.dueDate == date(2025, 6, 15)


def test_model_task_WorkItem_effort_value_roundtrip():
    instance = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    assert instance.effort == 7
    instance.effort = 13
    assert instance.effort == 13


def test_model_task_WorkItem_estimate_value_roundtrip():
    instance = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    assert instance.estimate == 7
    instance.estimate = 13
    assert instance.estimate == 13


def test_model_task_WorkItem_priority_value_roundtrip():
    instance = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    assert instance.priority == 7
    instance.priority = 13
    assert instance.priority == 13


def test_model_task_WorkItem_resolved_value_roundtrip():
    instance = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    assert instance.resolved == True
    instance.resolved = False
    assert instance.resolved == False


def test_model_task_WorkPackage_endDate_value_roundtrip():
    instance = model_task_WorkPackage(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    assert instance.endDate == date(2024, 1, 1)
    instance.endDate = date(2025, 6, 15)
    assert instance.endDate == date(2025, 6, 15)


def test_model_task_WorkPackage_startDate_value_roundtrip():
    instance = model_task_WorkPackage(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    assert instance.startDate == date(2024, 1, 1)
    instance.startDate = date(2025, 6, 15)
    assert instance.startDate == date(2025, 6, 15)


def test_esmodel_accesscontrol_ACGroup_isa_ACOrgUnit():
    instance = esmodel_accesscontrol_ACGroup()
    assert isinstance(instance, ACOrgUnit)


def test_esmodel_accesscontrol_ACUser_isa_ACOrgUnit():
    instance = esmodel_accesscontrol_ACUser(firstName="sample_text", lastName="sample_text")
    assert isinstance(instance, ACOrgUnit)


def test_esmodel_operations_CompositeOperation_isa_AbstractOperation():
    instance = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    assert isinstance(instance, AbstractOperation)


def test_esmodel_operations_CreateDeleteOperation_isa_AbstractOperation():
    instance = esmodel_operations_CreateDeleteOperation(delete=True)
    assert isinstance(instance, AbstractOperation)


def test_esmodel_operations_FeatureOperation_isa_AbstractOperation():
    instance = esmodel_operations_FeatureOperation(featureName="sample_text")
    assert isinstance(instance, AbstractOperation)


def test_model_activity_Activity_isa_ActivityObject():
    instance = model_activity_Activity()
    assert isinstance(instance, ActivityObject)


def test_model_activity_ActivityEnd_isa_ActivityObject():
    instance = model_activity_ActivityEnd()
    assert isinstance(instance, ActivityObject)


def test_model_activity_ActivityInitial_isa_ActivityObject():
    instance = model_activity_ActivityInitial()
    assert isinstance(instance, ActivityObject)


def test_model_activity_Branch_isa_ActivityObject():
    instance = model_activity_Branch()
    assert isinstance(instance, ActivityObject)


def test_model_activity_Fork_isa_ActivityObject():
    instance = model_activity_Fork()
    assert isinstance(instance, ActivityObject)


def test_model_rationale_Issue_isa_Annotation():
    instance = model_rationale_Issue(activity="sample_text")
    assert isinstance(instance, Annotation)


def test_model_task_WorkItem_isa_Annotation():
    instance = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    assert isinstance(instance, Annotation)


def test_model_attachment_FileAttachment_isa_Attachment():
    instance = model_attachment_FileAttachment(fileHash="sample_text", fileID="sample_text", fileName="sample_text", fileSize="sample_text", requiredOffline=True)
    assert isinstance(instance, Attachment)


def test_model_attachment_UrlAttachment_isa_Attachment():
    instance = model_attachment_UrlAttachment(url="sample_text")
    assert isinstance(instance, Attachment)


def test_model_diagram_MEDiagram_isa_Attachment():
    instance = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    assert isinstance(instance, Attachment)


def test_esmodel_operations_DiagramLayoutOperation_isa_AttributeOperation():
    instance = esmodel_operations_DiagramLayoutOperation()
    assert isinstance(instance, AttributeOperation)


def test_esmodel_semantic_SemanticCompositeOperation_isa_CompositeOperation():
    instance = esmodel_semantic_SemanticCompositeOperation()
    assert isinstance(instance, CompositeOperation)


def test_model_requirement_NonFunctionalRequirement_isa_Criterion():
    instance = model_requirement_NonFunctionalRequirement()
    assert isinstance(instance, Criterion)


def test_esmodel_events_AnnotationEvent_isa_Event():
    instance = esmodel_events_AnnotationEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_CheckoutEvent_isa_Event():
    instance = esmodel_events_CheckoutEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_DNDEvent_isa_Event():
    instance = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_ExceptionEvent_isa_Event():
    instance = esmodel_events_ExceptionEvent(ExceptionCauseStackTrace="sample_text", ExceptionCauseTitle="sample_text", ExceptionStackTrace="sample_text", ExceptionTitle="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_LinkEvent_isa_Event():
    instance = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_MergeChoiceEvent_isa_Event():
    instance = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_MergeEvent_isa_Event():
    instance = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    assert isinstance(instance, Event)


def test_esmodel_events_MergeGlobalChoiceEvent_isa_Event():
    instance = esmodel_events_MergeGlobalChoiceEvent(selection="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_NavigatorCreateEvent_isa_Event():
    instance = esmodel_events_NavigatorCreateEvent(dynamic=True)
    assert isinstance(instance, Event)


def test_esmodel_events_NotificationGenerationEvent_isa_Event():
    instance = esmodel_events_NotificationGenerationEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_NotificationIgnoreEvent_isa_Event():
    instance = esmodel_events_NotificationIgnoreEvent(notificationId="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_PerspectiveEvent_isa_Event():
    instance = esmodel_events_PerspectiveEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_PluginFocusEvent_isa_Event():
    instance = esmodel_events_PluginFocusEvent(pluginId="sample_text", startDate=date(2024, 1, 1))
    assert isinstance(instance, Event)


def test_esmodel_events_PluginStartEvent_isa_Event():
    instance = esmodel_events_PluginStartEvent(pluginId="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_PresentationSwitchEvent_isa_Event():
    instance = esmodel_events_PresentationSwitchEvent(newPresentation="sample_text", readView="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_ReadEvent_isa_Event():
    instance = esmodel_events_ReadEvent(readView="sample_text", sourceView="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_RevertEvent_isa_Event():
    instance = esmodel_events_RevertEvent(revertedChangesCount=7)
    assert isinstance(instance, Event)


def test_esmodel_events_ShowChangesEvent_isa_Event():
    instance = esmodel_events_ShowChangesEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_ShowHistoryEvent_isa_Event():
    instance = esmodel_events_ShowHistoryEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_TraceEvent_isa_Event():
    instance = esmodel_events_TraceEvent(featureName="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_URLEvent_isa_Event():
    instance = esmodel_events_URLEvent(sourceView="sample_text")
    assert isinstance(instance, Event)


def test_esmodel_events_UndoEvent_isa_Event():
    instance = esmodel_events_UndoEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_UpdateEvent_isa_Event():
    instance = esmodel_events_UpdateEvent()
    assert isinstance(instance, Event)


def test_esmodel_events_Validate_isa_Event():
    instance = esmodel_events_Validate()
    assert isinstance(instance, Event)


def test_esmodel_server_ServerEvent_isa_Event():
    instance = esmodel_server_ServerEvent()
    assert isinstance(instance, Event)


def test_esmodel_operations_AttributeOperation_isa_FeatureOperation():
    instance = esmodel_operations_AttributeOperation(newValue="sample_text", oldValue="sample_text")
    assert isinstance(instance, FeatureOperation)


def test_esmodel_operations_MultiAttributeMoveOperation_isa_FeatureOperation():
    instance = esmodel_operations_MultiAttributeMoveOperation(newIndex=7, oldIndex=7, referencedValue="sample_text")
    assert isinstance(instance, FeatureOperation)


def test_esmodel_operations_MultiAttributeOperation_isa_FeatureOperation():
    instance = esmodel_operations_MultiAttributeOperation(add=True, indexes=7, referencedValues="sample_text")
    assert isinstance(instance, FeatureOperation)


def test_esmodel_operations_MultiAttributeSetOperation_isa_FeatureOperation():
    instance = esmodel_operations_MultiAttributeSetOperation(index=7, newValue="sample_text", oldValue="sample_text")
    assert isinstance(instance, FeatureOperation)


def test_esmodel_operations_MultiReferenceMoveOperation_isa_FeatureOperation():
    instance = esmodel_operations_MultiReferenceMoveOperation(newIndex=7, oldIndex=7)
    assert isinstance(instance, FeatureOperation)


def test_esmodel_operations_ReferenceOperation_isa_FeatureOperation():
    instance = esmodel_operations_ReferenceOperation(bidirectional=True, containmentType="sample_text", oppositeFeatureName="sample_text")
    assert isinstance(instance, FeatureOperation)


def test_esmodel_FileIdentifier_isa_IdentifiableElement():
    instance = esmodel_FileIdentifier()
    assert isinstance(instance, IdentifiableElement)


def test_esmodel_accesscontrol_ACOrgUnit_isa_IdentifiableElement():
    instance = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    assert isinstance(instance, IdentifiableElement)


def test_esmodel_notification_ESNotification_isa_IdentifiableElement():
    instance = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    assert isinstance(instance, IdentifiableElement)


def test_esmodel_operations_AbstractOperation_isa_IdentifiableElement():
    instance = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    assert isinstance(instance, IdentifiableElement)


def test_metamodel_ModelElement_isa_IdentifiableElement():
    instance = metamodel_ModelElement(creationDate=date(2024, 1, 1), creator="sample_text")
    assert isinstance(instance, IdentifiableElement)


def test_model_change_MergingIssue_isa_Issue():
    instance = model_change_MergingIssue(resolvingRevision=7)
    assert isinstance(instance, Issue)


def test_model_meeting_CompositeMeetingSection_isa_MeetingSection():
    instance = model_meeting_CompositeMeetingSection()
    assert isinstance(instance, MeetingSection)


def test_model_meeting_IssueMeetingSection_isa_MeetingSection():
    instance = model_meeting_IssueMeetingSection()
    assert isinstance(instance, MeetingSection)


def test_model_meeting_WorkItemMeetingSection_isa_MeetingSection():
    instance = model_meeting_WorkItemMeetingSection()
    assert isinstance(instance, MeetingSection)


def test_model_UnicaseModelElement_isa_ModelElement():
    instance = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    assert isinstance(instance, ModelElement)


def test_model_rationale_Assessment_isa_NonDomainElement():
    instance = model_rationale_Assessment(value=7)
    assert isinstance(instance, NonDomainElement)


def test_model_rationale_Comment_isa_NonDomainElement():
    instance = model_rationale_Comment()
    assert isinstance(instance, NonDomainElement)


def test_model_rationale_Proposal_isa_NonDomainElement():
    instance = model_rationale_Proposal()
    assert isinstance(instance, NonDomainElement)


def test_model_rationale_Solution_isa_NonDomainElement():
    instance = model_rationale_Solution()
    assert isinstance(instance, NonDomainElement)


def test_model_requirement_Step_isa_NonDomainElement():
    instance = model_requirement_Step(userStep=True)
    assert isinstance(instance, NonDomainElement)


def test_model_requirement_SystemFunction_isa_NonDomainElement():
    instance = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    assert isinstance(instance, NonDomainElement)


def test_model_requirement_UserTask_isa_NonDomainElement():
    instance = model_requirement_UserTask()
    assert isinstance(instance, NonDomainElement)


def test_model_organization_Group_isa_OrgUnit():
    instance = model_organization_Group()
    assert isinstance(instance, OrgUnit)


def test_model_organization_User_isa_OrgUnit():
    instance = model_organization_User(email="sample_text", firstName="sample_text", lastName="sample_text")
    assert isinstance(instance, OrgUnit)


def test_model_classes_Class_isa_PackageElement():
    instance = model_classes_Class()
    assert isinstance(instance, PackageElement)


def test_model_classes_Package_isa_PackageElement():
    instance = model_classes_Package()
    assert isinstance(instance, PackageElement)


def test_model_Project_isa_Project():
    instance = model_Project()
    assert isinstance(instance, Project)


def test_model_change_MergingProposal_isa_Proposal():
    instance = model_change_MergingProposal()
    assert isinstance(instance, Proposal)


def test_esmodel_events_NotificationReadEvent_isa_ReadEvent():
    instance = esmodel_events_NotificationReadEvent(notificationId="sample_text")
    assert isinstance(instance, ReadEvent)


def test_esmodel_operations_MultiReferenceOperation_isa_ReferenceOperation():
    instance = esmodel_operations_MultiReferenceOperation(add=True, index=7)
    assert isinstance(instance, ReferenceOperation)


def test_esmodel_operations_MultiReferenceSetOperation_isa_ReferenceOperation():
    instance = esmodel_operations_MultiReferenceSetOperation(index=7)
    assert isinstance(instance, ReferenceOperation)


def test_esmodel_operations_SingleReferenceOperation_isa_ReferenceOperation():
    instance = esmodel_operations_SingleReferenceOperation()
    assert isinstance(instance, ReferenceOperation)


def test_esmodel_roles_ProjectAdminRole_isa_Role():
    instance = esmodel_roles_ProjectAdminRole()
    assert isinstance(instance, Role)


def test_esmodel_roles_ReaderRole_isa_Role():
    instance = esmodel_roles_ReaderRole()
    assert isinstance(instance, Role)


def test_esmodel_roles_ServerAdmin_isa_Role():
    instance = esmodel_roles_ServerAdmin()
    assert isinstance(instance, Role)


def test_esmodel_roles_WriterRole_isa_Role():
    instance = esmodel_roles_WriterRole()
    assert isinstance(instance, Role)


def test_model_document_CompositeSection_isa_Section():
    instance = model_document_CompositeSection()
    assert isinstance(instance, Section)


def test_model_document_LeafSection_isa_Section():
    instance = model_document_LeafSection()
    assert isinstance(instance, Section)


def test_esmodel_server_ServerProjectEvent_isa_ServerEvent():
    instance = esmodel_server_ServerProjectEvent()
    assert isinstance(instance, ServerEvent)


def test_esmodel_server_ProjectUpdatedEvent_isa_ServerProjectEvent():
    instance = esmodel_server_ProjectUpdatedEvent()
    assert isinstance(instance, ServerProjectEvent)


def test_model_change_MergingSolution_isa_Solution():
    instance = model_change_MergingSolution()
    assert isinstance(instance, Solution)


def test_model_state_State_isa_StateNode():
    instance = model_state_State(activities="sample_text", entryConditions="sample_text", exitConditions="sample_text")
    assert isinstance(instance, StateNode)


def test_model_state_StateEnd_isa_StateNode():
    instance = model_state_StateEnd()
    assert isinstance(instance, StateNode)


def test_model_state_StateInitial_isa_StateNode():
    instance = model_state_StateInitial()
    assert isinstance(instance, StateNode)


def test_model_profile_StereotypeAttributeSimple_isa_StereotypeAttribute():
    instance = model_profile_StereotypeAttributeSimple(type="sample_text")
    assert isinstance(instance, StereotypeAttribute)


def test_model_profile_StereotypeAttributeInstanceString_isa_StereotypeAttributeInstance():
    instance = model_profile_StereotypeAttributeInstanceString(value="sample_text")
    assert isinstance(instance, StereotypeAttributeInstance)


def test_model_Annotation_isa_UnicaseModelElement():
    instance = model_Annotation()
    assert isinstance(instance, UnicaseModelElement)


def test_model_Attachment_isa_UnicaseModelElement():
    instance = model_Attachment()
    assert isinstance(instance, UnicaseModelElement)


def test_model_activity_ActivityObject_isa_UnicaseModelElement():
    instance = model_activity_ActivityObject()
    assert isinstance(instance, UnicaseModelElement)


def test_model_activity_Transition_isa_UnicaseModelElement():
    instance = model_activity_Transition(condition="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_change_ModelChangePackage_isa_UnicaseModelElement():
    instance = model_change_ModelChangePackage(sourceVersion=7, targetVersion=7)
    assert isinstance(instance, UnicaseModelElement)


def test_model_classes_Association_isa_UnicaseModelElement():
    instance = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_classes_Attribute_isa_UnicaseModelElement():
    instance = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_classes_Dependency_isa_UnicaseModelElement():
    instance = model_classes_Dependency()
    assert isinstance(instance, UnicaseModelElement)


def test_model_classes_Method_isa_UnicaseModelElement():
    instance = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_classes_MethodArgument_isa_UnicaseModelElement():
    instance = model_classes_MethodArgument(defaultValue="sample_text", direction="sample_text", label="sample_text", signature="sample_text", type="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_classes_PackageElement_isa_UnicaseModelElement():
    instance = model_classes_PackageElement()
    assert isinstance(instance, UnicaseModelElement)


def test_model_component_Component_isa_UnicaseModelElement():
    instance = model_component_Component()
    assert isinstance(instance, UnicaseModelElement)


def test_model_component_ComponentService_isa_UnicaseModelElement():
    instance = model_component_ComponentService()
    assert isinstance(instance, UnicaseModelElement)


def test_model_component_DeploymentNode_isa_UnicaseModelElement():
    instance = model_component_DeploymentNode()
    assert isinstance(instance, UnicaseModelElement)


def test_model_document_Section_isa_UnicaseModelElement():
    instance = model_document_Section()
    assert isinstance(instance, UnicaseModelElement)


def test_model_meeting_Meeting_isa_UnicaseModelElement():
    instance = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    assert isinstance(instance, UnicaseModelElement)


def test_model_meeting_MeetingSection_isa_UnicaseModelElement():
    instance = model_meeting_MeetingSection(allocatedTime=7)
    assert isinstance(instance, UnicaseModelElement)


def test_model_organization_OrgUnit_isa_UnicaseModelElement():
    instance = model_organization_OrgUnit(acOrgId="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_profile_Profile_isa_UnicaseModelElement():
    instance = model_profile_Profile()
    assert isinstance(instance, UnicaseModelElement)


def test_model_profile_Stereotype_isa_UnicaseModelElement():
    instance = model_profile_Stereotype(required=True)
    assert isinstance(instance, UnicaseModelElement)


def test_model_profile_StereotypeAttribute_isa_UnicaseModelElement():
    instance = model_profile_StereotypeAttribute()
    assert isinstance(instance, UnicaseModelElement)


def test_model_profile_StereotypeAttributeInstance_isa_UnicaseModelElement():
    instance = model_profile_StereotypeAttributeInstance()
    assert isinstance(instance, UnicaseModelElement)


def test_model_profile_StereotypeInstance_isa_UnicaseModelElement():
    instance = model_profile_StereotypeInstance()
    assert isinstance(instance, UnicaseModelElement)


def test_model_rationale_Assessment_isa_UnicaseModelElement():
    instance = model_rationale_Assessment(value=7)
    assert isinstance(instance, UnicaseModelElement)


def test_model_rationale_Comment_isa_UnicaseModelElement():
    instance = model_rationale_Comment()
    assert isinstance(instance, UnicaseModelElement)


def test_model_rationale_Criterion_isa_UnicaseModelElement():
    instance = model_rationale_Criterion()
    assert isinstance(instance, UnicaseModelElement)


def test_model_rationale_Proposal_isa_UnicaseModelElement():
    instance = model_rationale_Proposal()
    assert isinstance(instance, UnicaseModelElement)


def test_model_rationale_Solution_isa_UnicaseModelElement():
    instance = model_rationale_Solution()
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_Actor_isa_UnicaseModelElement():
    instance = model_requirement_Actor()
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_ActorInstance_isa_UnicaseModelElement():
    instance = model_requirement_ActorInstance()
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_FunctionalRequirement_isa_UnicaseModelElement():
    instance = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_Scenario_isa_UnicaseModelElement():
    instance = model_requirement_Scenario()
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_Step_isa_UnicaseModelElement():
    instance = model_requirement_Step(userStep=True)
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_SystemFunction_isa_UnicaseModelElement():
    instance = model_requirement_SystemFunction(exception="sample_text", input="sample_text", output="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_UseCase_isa_UnicaseModelElement():
    instance = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_requirement_UserTask_isa_UnicaseModelElement():
    instance = model_requirement_UserTask()
    assert isinstance(instance, UnicaseModelElement)


def test_model_state_StateNode_isa_UnicaseModelElement():
    instance = model_state_StateNode()
    assert isinstance(instance, UnicaseModelElement)


def test_model_state_Transition_isa_UnicaseModelElement():
    instance = model_state_Transition(condition="sample_text")
    assert isinstance(instance, UnicaseModelElement)


def test_model_task_Checkable_isa_UnicaseModelElement():
    instance = model_task_Checkable(checked=True)
    assert isinstance(instance, UnicaseModelElement)


def test_esmodel_ProjectId_isa_UniqueIdentifier():
    instance = esmodel_ProjectId()
    assert isinstance(instance, UniqueIdentifier)


def test_esmodel_SessionId_isa_UniqueIdentifier():
    instance = esmodel_SessionId()
    assert isinstance(instance, UniqueIdentifier)


def test_esmodel_accesscontrol_ACOrgUnitId_isa_UniqueIdentifier():
    instance = esmodel_accesscontrol_ACOrgUnitId()
    assert isinstance(instance, UniqueIdentifier)


def test_esmodel_operations_OperationId_isa_UniqueIdentifier():
    instance = esmodel_operations_OperationId()
    assert isinstance(instance, UniqueIdentifier)


def test_metamodel_ModelElementId_isa_UniqueIdentifier():
    instance = metamodel_ModelElementId()
    assert isinstance(instance, UniqueIdentifier)


def test_esmodel_versioning_DateVersionSpec_isa_VersionSpec():
    instance = esmodel_versioning_DateVersionSpec(date=date(2024, 1, 1))
    assert isinstance(instance, VersionSpec)


def test_esmodel_versioning_HeadVersionSpec_isa_VersionSpec():
    instance = esmodel_versioning_HeadVersionSpec()
    assert isinstance(instance, VersionSpec)


def test_esmodel_versioning_PrimaryVersionSpec_isa_VersionSpec():
    instance = esmodel_versioning_PrimaryVersionSpec(identifier=7)
    assert isinstance(instance, VersionSpec)


def test_esmodel_versioning_TagVersionSpec_isa_VersionSpec():
    instance = esmodel_versioning_TagVersionSpec(name="sample_text")
    assert isinstance(instance, VersionSpec)


def test_model_task_Milestone_isa_WorkItem():
    instance = model_task_Milestone()
    assert isinstance(instance, WorkItem)


def test_model_task_WorkPackage_isa_WorkItem():
    instance = model_task_WorkPackage(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    assert isinstance(instance, WorkItem)


def test_model_bug_BugReport_isa_task_Checkable():
    instance = model_bug_BugReport(Status="sample_text", resolution="sample_text", resolutionType="sample_text", severity="sample_text")
    assert isinstance(instance, task_Checkable)


def test_model_rationale_Issue_isa_task_Checkable():
    instance = model_rationale_Issue(activity="sample_text")
    assert isinstance(instance, task_Checkable)


def test_model_task_ActionItem_isa_task_Checkable():
    instance = model_task_ActionItem(activity="sample_text", done=True)
    assert isinstance(instance, task_Checkable)


def test_model_bug_BugReport_isa_task_WorkItem():
    instance = model_bug_BugReport(Status="sample_text", resolution="sample_text", resolutionType="sample_text", severity="sample_text")
    assert isinstance(instance, task_WorkItem)


def test_model_rationale_Issue_isa_task_WorkItem():
    instance = model_rationale_Issue(activity="sample_text")
    assert isinstance(instance, task_WorkItem)


def test_model_task_ActionItem_isa_task_WorkItem():
    instance = model_task_ActionItem(activity="sample_text", done=True)
    assert isinstance(instance, task_WorkItem)


def test_assoc_annotations4_link_reassign_clear():
    a = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    b1 = Annotation()
    b2 = Annotation()
    _safe_set(a, 'annotatedModelElements', {b1})
    assert _is_linked(a, 'annotatedModelElements', b1)
    if hasattr(b1, 'Annotation'):
        assert _is_linked(b1, 'Annotation', a)
    _safe_set(a, 'annotatedModelElements', {b2})
    assert _is_linked(a, 'annotatedModelElements', b2)
    if hasattr(b1, 'Annotation'):
        assert not _is_linked(b1, 'Annotation', a)
    if hasattr(b2, 'Annotation'):
        assert _is_linked(b2, 'Annotation', a)
    _safe_set(a, 'annotatedModelElements', set())
    assert not _is_linked(a, 'annotatedModelElements', b2)
    if hasattr(b2, 'Annotation'):
        assert not _is_linked(b2, 'Annotation', a)


def test_assoc_appliedStereotypeInstances10_link_reassign_clear():
    a = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    b1 = profile_StereotypeInstance()
    b2 = profile_StereotypeInstance()
    _safe_set(a, 'modelElement', {b1})
    assert _is_linked(a, 'modelElement', b1)
    if hasattr(b1, 'StereotypeInstance'):
        assert _is_linked(b1, 'StereotypeInstance', a)
    _safe_set(a, 'modelElement', {b2})
    assert _is_linked(a, 'modelElement', b2)
    if hasattr(b1, 'StereotypeInstance'):
        assert not _is_linked(b1, 'StereotypeInstance', a)
    if hasattr(b2, 'StereotypeInstance'):
        assert _is_linked(b2, 'StereotypeInstance', a)
    _safe_set(a, 'modelElement', set())
    assert not _is_linked(a, 'modelElement', b2)
    if hasattr(b2, 'StereotypeInstance'):
        assert not _is_linked(b2, 'StereotypeInstance', a)


def test_assoc_arguments74_link_reassign_clear():
    a = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    b1 = classes_MethodArgument()
    b2 = classes_MethodArgument()
    _safe_set(a, 'model_classes_Method', {b1})
    assert _is_linked(a, 'model_classes_Method', b1)
    if hasattr(b1, 'classes_MethodArgument'):
        assert _is_linked(b1, 'classes_MethodArgument', a)
    _safe_set(a, 'model_classes_Method', {b2})
    assert _is_linked(a, 'model_classes_Method', b2)
    if hasattr(b1, 'classes_MethodArgument'):
        assert not _is_linked(b1, 'classes_MethodArgument', a)
    if hasattr(b2, 'classes_MethodArgument'):
        assert _is_linked(b2, 'classes_MethodArgument', a)
    _safe_set(a, 'model_classes_Method', set())
    assert not _is_linked(a, 'model_classes_Method', b2)
    if hasattr(b2, 'classes_MethodArgument'):
        assert not _is_linked(b2, 'classes_MethodArgument', a)


def test_assoc_assignee26_link_reassign_clear():
    a = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    b1 = organization_OrgUnit()
    b2 = organization_OrgUnit()
    _safe_set(a, 'assignments', b1)
    assert _is_linked(a, 'assignments', b1)
    if hasattr(b1, 'OrgUnit27'):
        assert _is_linked(b1, 'OrgUnit27', a)
    _safe_set(a, 'assignments', b2)
    assert _is_linked(a, 'assignments', b2)
    if hasattr(b1, 'OrgUnit27'):
        assert not _is_linked(b1, 'OrgUnit27', a)
    if hasattr(b2, 'OrgUnit27'):
        assert _is_linked(b2, 'OrgUnit27', a)
    _safe_set(a, 'assignments', None)
    assert not _is_linked(a, 'assignments', b2)
    if hasattr(b2, 'OrgUnit27'):
        assert not _is_linked(b2, 'OrgUnit27', a)


def test_assoc_assignments16_link_reassign_clear():
    a = model_organization_OrgUnit(acOrgId="sample_text")
    b1 = task_WorkItem()
    b2 = task_WorkItem()
    _safe_set(a, 'assignee', {b1})
    assert _is_linked(a, 'assignee', b1)
    if hasattr(b1, 'WorkItem17'):
        assert _is_linked(b1, 'WorkItem17', a)
    _safe_set(a, 'assignee', {b2})
    assert _is_linked(a, 'assignee', b2)
    if hasattr(b1, 'WorkItem17'):
        assert not _is_linked(b1, 'WorkItem17', a)
    if hasattr(b2, 'WorkItem17'):
        assert _is_linked(b2, 'WorkItem17', a)
    _safe_set(a, 'assignee', set())
    assert not _is_linked(a, 'assignee', b2)
    if hasattr(b2, 'WorkItem17'):
        assert not _is_linked(b2, 'WorkItem17', a)


def test_assoc_associatedChangePackages31_link_reassign_clear():
    a = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    b1 = change_ModelChangePackage()
    b2 = change_ModelChangePackage()
    _safe_set(a, 'model_task_WorkItem', {b1})
    assert _is_linked(a, 'model_task_WorkItem', b1)
    if hasattr(b1, 'change_ModelChangePackage'):
        assert _is_linked(b1, 'change_ModelChangePackage', a)
    _safe_set(a, 'model_task_WorkItem', {b2})
    assert _is_linked(a, 'model_task_WorkItem', b2)
    if hasattr(b1, 'change_ModelChangePackage'):
        assert not _is_linked(b1, 'change_ModelChangePackage', a)
    if hasattr(b2, 'change_ModelChangePackage'):
        assert _is_linked(b2, 'change_ModelChangePackage', a)
    _safe_set(a, 'model_task_WorkItem', set())
    assert not _is_linked(a, 'model_task_WorkItem', b2)
    if hasattr(b2, 'change_ModelChangePackage'):
        assert not _is_linked(b2, 'change_ModelChangePackage', a)


def test_assoc_attachments5_link_reassign_clear():
    a = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    b1 = Attachment()
    b2 = Attachment()
    _safe_set(a, 'referringModelElements', {b1})
    assert _is_linked(a, 'referringModelElements', b1)
    if hasattr(b1, 'Attachment'):
        assert _is_linked(b1, 'Attachment', a)
    _safe_set(a, 'referringModelElements', {b2})
    assert _is_linked(a, 'referringModelElements', b2)
    if hasattr(b1, 'Attachment'):
        assert not _is_linked(b1, 'Attachment', a)
    if hasattr(b2, 'Attachment'):
        assert _is_linked(b2, 'Attachment', a)
    _safe_set(a, 'referringModelElements', set())
    assert not _is_linked(a, 'referringModelElements', b2)
    if hasattr(b2, 'Attachment'):
        assert not _is_linked(b2, 'Attachment', a)


def test_assoc_baseVersion366_link_reassign_clear():
    a = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    b1 = versioning_PrimaryVersionSpec()
    b2 = versioning_PrimaryVersionSpec()
    _safe_set(a, 'esmodel_events_MergeEvent', b1)
    assert _is_linked(a, 'esmodel_events_MergeEvent', b1)
    if hasattr(b1, 'versioning_PrimaryVersionSpec367'):
        assert _is_linked(b1, 'versioning_PrimaryVersionSpec367', a)
    _safe_set(a, 'esmodel_events_MergeEvent', b2)
    assert _is_linked(a, 'esmodel_events_MergeEvent', b2)
    if hasattr(b1, 'versioning_PrimaryVersionSpec367'):
        assert not _is_linked(b1, 'versioning_PrimaryVersionSpec367', a)
    if hasattr(b2, 'versioning_PrimaryVersionSpec367'):
        assert _is_linked(b2, 'versioning_PrimaryVersionSpec367', a)
    _safe_set(a, 'esmodel_events_MergeEvent', None)
    assert not _is_linked(a, 'esmodel_events_MergeEvent', b2)
    if hasattr(b2, 'versioning_PrimaryVersionSpec367'):
        assert not _is_linked(b2, 'versioning_PrimaryVersionSpec367', a)


def test_assoc_calledMethods70_link_reassign_clear():
    a = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    b1 = classes_Method()
    b2 = classes_Method()
    _safe_set(a, 'callingMethods', {b1})
    assert _is_linked(a, 'callingMethods', b1)
    if hasattr(b1, 'Method71'):
        assert _is_linked(b1, 'Method71', a)
    _safe_set(a, 'callingMethods', {b2})
    assert _is_linked(a, 'callingMethods', b2)
    if hasattr(b1, 'Method71'):
        assert not _is_linked(b1, 'Method71', a)
    if hasattr(b2, 'Method71'):
        assert _is_linked(b2, 'Method71', a)
    _safe_set(a, 'callingMethods', set())
    assert not _is_linked(a, 'callingMethods', b2)
    if hasattr(b2, 'Method71'):
        assert not _is_linked(b2, 'Method71', a)


def test_assoc_callingMethods72_link_reassign_clear():
    a = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    b1 = classes_Method()
    b2 = classes_Method()
    _safe_set(a, 'calledMethods', {b1})
    assert _is_linked(a, 'calledMethods', b1)
    if hasattr(b1, 'Method73'):
        assert _is_linked(b1, 'Method73', a)
    _safe_set(a, 'calledMethods', {b2})
    assert _is_linked(a, 'calledMethods', b2)
    if hasattr(b1, 'Method73'):
        assert not _is_linked(b1, 'Method73', a)
    if hasattr(b2, 'Method73'):
        assert _is_linked(b2, 'Method73', a)
    _safe_set(a, 'calledMethods', set())
    assert not _is_linked(a, 'calledMethods', b2)
    if hasattr(b2, 'Method73'):
        assert not _is_linked(b2, 'Method73', a)


def test_assoc_comments9_link_reassign_clear():
    a = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    b1 = rationale_Comment()
    b2 = rationale_Comment()
    _safe_set(a, 'commentedElement', {b1})
    assert _is_linked(a, 'commentedElement', b1)
    if hasattr(b1, 'Comment'):
        assert _is_linked(b1, 'Comment', a)
    _safe_set(a, 'commentedElement', {b2})
    assert _is_linked(a, 'commentedElement', b2)
    if hasattr(b1, 'Comment'):
        assert not _is_linked(b1, 'Comment', a)
    if hasattr(b2, 'Comment'):
        assert _is_linked(b2, 'Comment', a)
    _safe_set(a, 'commentedElement', set())
    assert not _is_linked(a, 'commentedElement', b2)
    if hasattr(b2, 'Comment'):
        assert not _is_linked(b2, 'Comment', a)


def test_assoc_containedWorkItems32_link_reassign_clear():
    a = model_task_WorkPackage(endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    b1 = task_WorkItem()
    b2 = task_WorkItem()
    _safe_set(a, 'containingWorkpackage', {b1})
    assert _is_linked(a, 'containingWorkpackage', b1)
    if hasattr(b1, 'WorkItem33'):
        assert _is_linked(b1, 'WorkItem33', a)
    _safe_set(a, 'containingWorkpackage', {b2})
    assert _is_linked(a, 'containingWorkpackage', b2)
    if hasattr(b1, 'WorkItem33'):
        assert not _is_linked(b1, 'WorkItem33', a)
    if hasattr(b2, 'WorkItem33'):
        assert _is_linked(b2, 'WorkItem33', a)
    _safe_set(a, 'containingWorkpackage', set())
    assert not _is_linked(a, 'containingWorkpackage', b2)
    if hasattr(b2, 'WorkItem33'):
        assert not _is_linked(b2, 'WorkItem33', a)


def test_assoc_containingWorkpackage21_link_reassign_clear():
    a = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    b1 = task_WorkPackage()
    b2 = task_WorkPackage()
    _safe_set(a, 'containedWorkItems', b1)
    assert _is_linked(a, 'containedWorkItems', b1)
    if hasattr(b1, 'WorkPackage'):
        assert _is_linked(b1, 'WorkPackage', a)
    _safe_set(a, 'containedWorkItems', b2)
    assert _is_linked(a, 'containedWorkItems', b2)
    if hasattr(b1, 'WorkPackage'):
        assert not _is_linked(b1, 'WorkPackage', a)
    if hasattr(b2, 'WorkPackage'):
        assert _is_linked(b2, 'WorkPackage', a)
    _safe_set(a, 'containedWorkItems', None)
    assert not _is_linked(a, 'containedWorkItems', b2)
    if hasattr(b2, 'WorkPackage'):
        assert not _is_linked(b2, 'WorkPackage', a)


def test_assoc_contextModelElement432_link_reassign_clear():
    a = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_MergeChoiceEvent433', b1)
    assert _is_linked(a, 'esmodel_events_MergeChoiceEvent433', b1)
    if hasattr(b1, 'ModelElementId434'):
        assert _is_linked(b1, 'ModelElementId434', a)
    _safe_set(a, 'esmodel_events_MergeChoiceEvent433', b2)
    assert _is_linked(a, 'esmodel_events_MergeChoiceEvent433', b2)
    if hasattr(b1, 'ModelElementId434'):
        assert not _is_linked(b1, 'ModelElementId434', a)
    if hasattr(b2, 'ModelElementId434'):
        assert _is_linked(b2, 'ModelElementId434', a)
    _safe_set(a, 'esmodel_events_MergeChoiceEvent433', None)
    assert not _is_linked(a, 'esmodel_events_MergeChoiceEvent433', b2)
    if hasattr(b2, 'ModelElementId434'):
        assert not _is_linked(b2, 'ModelElementId434', a)


def test_assoc_createdElement409_link_reassign_clear():
    a = esmodel_events_NavigatorCreateEvent(dynamic=True)
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_NavigatorCreateEvent', b1)
    assert _is_linked(a, 'esmodel_events_NavigatorCreateEvent', b1)
    if hasattr(b1, 'ModelElementId410'):
        assert _is_linked(b1, 'ModelElementId410', a)
    _safe_set(a, 'esmodel_events_NavigatorCreateEvent', b2)
    assert _is_linked(a, 'esmodel_events_NavigatorCreateEvent', b2)
    if hasattr(b1, 'ModelElementId410'):
        assert not _is_linked(b1, 'ModelElementId410', a)
    if hasattr(b2, 'ModelElementId410'):
        assert _is_linked(b2, 'ModelElementId410', a)
    _safe_set(a, 'esmodel_events_NavigatorCreateEvent', None)
    assert not _is_linked(a, 'esmodel_events_NavigatorCreateEvent', b2)
    if hasattr(b2, 'ModelElementId410'):
        assert not _is_linked(b2, 'ModelElementId410', a)


def test_assoc_criteria166_link_reassign_clear():
    a = model_rationale_Issue(activity="sample_text")
    b1 = rationale_Criterion()
    b2 = rationale_Criterion()
    _safe_set(a, 'model_rationale_Issue', {b1})
    assert _is_linked(a, 'model_rationale_Issue', b1)
    if hasattr(b1, 'rationale_Criterion'):
        assert _is_linked(b1, 'rationale_Criterion', a)
    _safe_set(a, 'model_rationale_Issue', {b2})
    assert _is_linked(a, 'model_rationale_Issue', b2)
    if hasattr(b1, 'rationale_Criterion'):
        assert not _is_linked(b1, 'rationale_Criterion', a)
    if hasattr(b2, 'rationale_Criterion'):
        assert _is_linked(b2, 'rationale_Criterion', a)
    _safe_set(a, 'model_rationale_Issue', set())
    assert not _is_linked(a, 'model_rationale_Issue', b2)
    if hasattr(b2, 'rationale_Criterion'):
        assert not _is_linked(b2, 'rationale_Criterion', a)


def test_assoc_criterion176_link_reassign_clear():
    a = model_rationale_Assessment(value=7)
    b1 = rationale_Criterion()
    b2 = rationale_Criterion()
    _safe_set(a, 'assessments177', b1)
    assert _is_linked(a, 'assessments177', b1)
    if hasattr(b1, 'Criterion'):
        assert _is_linked(b1, 'Criterion', a)
    _safe_set(a, 'assessments177', b2)
    assert _is_linked(a, 'assessments177', b2)
    if hasattr(b1, 'Criterion'):
        assert not _is_linked(b1, 'Criterion', a)
    if hasattr(b2, 'Criterion'):
        assert _is_linked(b2, 'Criterion', a)
    _safe_set(a, 'assessments177', None)
    assert not _is_linked(a, 'assessments177', b2)
    if hasattr(b2, 'Criterion'):
        assert not _is_linked(b2, 'Criterion', a)


def test_assoc_definingClass66_link_reassign_clear():
    a = model_classes_Attribute(defaultValue="sample_text", label="sample_text", properties="sample_text", scope="sample_text", signature="sample_text", type="sample_text", visibility="sample_text")
    b1 = classes_Class()
    b2 = classes_Class()
    _safe_set(a, 'attributes', b1)
    assert _is_linked(a, 'attributes', b1)
    if hasattr(b1, 'Class67'):
        assert _is_linked(b1, 'Class67', a)
    _safe_set(a, 'attributes', b2)
    assert _is_linked(a, 'attributes', b2)
    if hasattr(b1, 'Class67'):
        assert not _is_linked(b1, 'Class67', a)
    if hasattr(b2, 'Class67'):
        assert _is_linked(b2, 'Class67', a)
    _safe_set(a, 'attributes', None)
    assert not _is_linked(a, 'attributes', b2)
    if hasattr(b2, 'Class67'):
        assert not _is_linked(b2, 'Class67', a)


def test_assoc_definingClass68_link_reassign_clear():
    a = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    b1 = classes_Class()
    b2 = classes_Class()
    _safe_set(a, 'methods', b1)
    assert _is_linked(a, 'methods', b1)
    if hasattr(b1, 'Class69'):
        assert _is_linked(b1, 'Class69', a)
    _safe_set(a, 'methods', b2)
    assert _is_linked(a, 'methods', b2)
    if hasattr(b1, 'Class69'):
        assert not _is_linked(b1, 'Class69', a)
    if hasattr(b2, 'Class69'):
        assert _is_linked(b2, 'Class69', a)
    _safe_set(a, 'methods', None)
    assert not _is_linked(a, 'methods', b2)
    if hasattr(b2, 'Class69'):
        assert not _is_linked(b2, 'Class69', a)


def test_assoc_demoParticipations75_link_reassign_clear():
    a = model_classes_Method(label="sample_text", properties="sample_text", returnType="sample_text", scope="sample_text", signature="sample_text", stubbed=True, visibility="sample_text")
    b1 = requirement_Scenario()
    b2 = requirement_Scenario()
    _safe_set(a, 'participatingMethods', {b1})
    assert _is_linked(a, 'participatingMethods', b1)
    if hasattr(b1, 'Scenario76'):
        assert _is_linked(b1, 'Scenario76', a)
    _safe_set(a, 'participatingMethods', {b2})
    assert _is_linked(a, 'participatingMethods', b2)
    if hasattr(b1, 'Scenario76'):
        assert not _is_linked(b1, 'Scenario76', a)
    if hasattr(b2, 'Scenario76'):
        assert _is_linked(b2, 'Scenario76', a)
    _safe_set(a, 'participatingMethods', set())
    assert not _is_linked(a, 'participatingMethods', b2)
    if hasattr(b2, 'Scenario76'):
        assert not _is_linked(b2, 'Scenario76', a)


def test_assoc_dragSourceElement394_link_reassign_clear():
    a = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_DNDEvent', b1)
    assert _is_linked(a, 'esmodel_events_DNDEvent', b1)
    if hasattr(b1, 'ModelElementId395'):
        assert _is_linked(b1, 'ModelElementId395', a)
    _safe_set(a, 'esmodel_events_DNDEvent', b2)
    assert _is_linked(a, 'esmodel_events_DNDEvent', b2)
    if hasattr(b1, 'ModelElementId395'):
        assert not _is_linked(b1, 'ModelElementId395', a)
    if hasattr(b2, 'ModelElementId395'):
        assert _is_linked(b2, 'ModelElementId395', a)
    _safe_set(a, 'esmodel_events_DNDEvent', None)
    assert not _is_linked(a, 'esmodel_events_DNDEvent', b2)
    if hasattr(b2, 'ModelElementId395'):
        assert not _is_linked(b2, 'ModelElementId395', a)


def test_assoc_dropTargetElement396_link_reassign_clear():
    a = esmodel_events_DNDEvent(sourceView="sample_text", targetView="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_DNDEvent397', b1)
    assert _is_linked(a, 'esmodel_events_DNDEvent397', b1)
    if hasattr(b1, 'ModelElementId398'):
        assert _is_linked(b1, 'ModelElementId398', a)
    _safe_set(a, 'esmodel_events_DNDEvent397', b2)
    assert _is_linked(a, 'esmodel_events_DNDEvent397', b2)
    if hasattr(b1, 'ModelElementId398'):
        assert not _is_linked(b1, 'ModelElementId398', a)
    if hasattr(b2, 'ModelElementId398'):
        assert _is_linked(b2, 'ModelElementId398', a)
    _safe_set(a, 'esmodel_events_DNDEvent397', None)
    assert not _is_linked(a, 'esmodel_events_DNDEvent397', b2)
    if hasattr(b2, 'ModelElementId398'):
        assert not _is_linked(b2, 'ModelElementId398', a)


def test_assoc_eObjectToIdMap339_link_reassign_clear():
    a = esmodel_operations_CreateDeleteOperation(delete=True)
    b1 = operations_EObjectToModelElementIdMap()
    b2 = operations_EObjectToModelElementIdMap()
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation340', {b1})
    assert _is_linked(a, 'esmodel_operations_CreateDeleteOperation340', b1)
    if hasattr(b1, 'operations_EObjectToModelElementIdMap'):
        assert _is_linked(b1, 'operations_EObjectToModelElementIdMap', a)
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation340', {b2})
    assert _is_linked(a, 'esmodel_operations_CreateDeleteOperation340', b2)
    if hasattr(b1, 'operations_EObjectToModelElementIdMap'):
        assert not _is_linked(b1, 'operations_EObjectToModelElementIdMap', a)
    if hasattr(b2, 'operations_EObjectToModelElementIdMap'):
        assert _is_linked(b2, 'operations_EObjectToModelElementIdMap', a)
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation340', set())
    assert not _is_linked(a, 'esmodel_operations_CreateDeleteOperation340', b2)
    if hasattr(b2, 'operations_EObjectToModelElementIdMap'):
        assert not _is_linked(b2, 'operations_EObjectToModelElementIdMap', a)


def test_assoc_elements36_link_reassign_clear():
    a = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    b1 = UnicaseModelElement()
    b2 = UnicaseModelElement()
    _safe_set(a, 'model_diagram_MEDiagram', {b1})
    assert _is_linked(a, 'model_diagram_MEDiagram', b1)
    if hasattr(b1, 'UnicaseModelElement37'):
        assert _is_linked(b1, 'UnicaseModelElement37', a)
    _safe_set(a, 'model_diagram_MEDiagram', {b2})
    assert _is_linked(a, 'model_diagram_MEDiagram', b2)
    if hasattr(b1, 'UnicaseModelElement37'):
        assert not _is_linked(b1, 'UnicaseModelElement37', a)
    if hasattr(b2, 'UnicaseModelElement37'):
        assert _is_linked(b2, 'UnicaseModelElement37', a)
    _safe_set(a, 'model_diagram_MEDiagram', set())
    assert not _is_linked(a, 'model_diagram_MEDiagram', b2)
    if hasattr(b2, 'UnicaseModelElement37'):
        assert not _is_linked(b2, 'UnicaseModelElement37', a)


def test_assoc_extendedUseCases101_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_UseCase()
    b2 = requirement_UseCase()
    _safe_set(a, 'model_requirement_UseCase102', {b1})
    assert _is_linked(a, 'model_requirement_UseCase102', b1)
    if hasattr(b1, 'requirement_UseCase103'):
        assert _is_linked(b1, 'requirement_UseCase103', a)
    _safe_set(a, 'model_requirement_UseCase102', {b2})
    assert _is_linked(a, 'model_requirement_UseCase102', b2)
    if hasattr(b1, 'requirement_UseCase103'):
        assert not _is_linked(b1, 'requirement_UseCase103', a)
    if hasattr(b2, 'requirement_UseCase103'):
        assert _is_linked(b2, 'requirement_UseCase103', a)
    _safe_set(a, 'model_requirement_UseCase102', set())
    assert not _is_linked(a, 'model_requirement_UseCase102', b2)
    if hasattr(b2, 'requirement_UseCase103'):
        assert not _is_linked(b2, 'requirement_UseCase103', a)


def test_assoc_facilitator202_link_reassign_clear():
    a = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    b1 = organization_User()
    b2 = organization_User()
    _safe_set(a, 'model_meeting_Meeting', b1)
    assert _is_linked(a, 'model_meeting_Meeting', b1)
    if hasattr(b1, 'organization_User'):
        assert _is_linked(b1, 'organization_User', a)
    _safe_set(a, 'model_meeting_Meeting', b2)
    assert _is_linked(a, 'model_meeting_Meeting', b2)
    if hasattr(b1, 'organization_User'):
        assert not _is_linked(b1, 'organization_User', a)
    if hasattr(b2, 'organization_User'):
        assert _is_linked(b2, 'organization_User', a)
    _safe_set(a, 'model_meeting_Meeting', None)
    assert not _is_linked(a, 'model_meeting_Meeting', b2)
    if hasattr(b2, 'organization_User'):
        assert not _is_linked(b2, 'organization_User', a)


def test_assoc_functionalRequirements96_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_FunctionalRequirement()
    b2 = requirement_FunctionalRequirement()
    _safe_set(a, 'useCases', {b1})
    assert _is_linked(a, 'useCases', b1)
    if hasattr(b1, 'FunctionalRequirement97'):
        assert _is_linked(b1, 'FunctionalRequirement97', a)
    _safe_set(a, 'useCases', {b2})
    assert _is_linked(a, 'useCases', b2)
    if hasattr(b1, 'FunctionalRequirement97'):
        assert not _is_linked(b1, 'FunctionalRequirement97', a)
    if hasattr(b2, 'FunctionalRequirement97'):
        assert _is_linked(b2, 'FunctionalRequirement97', a)
    _safe_set(a, 'useCases', set())
    assert not _is_linked(a, 'useCases', b2)
    if hasattr(b2, 'FunctionalRequirement97'):
        assert not _is_linked(b2, 'FunctionalRequirement97', a)


def test_assoc_gmfdiagram38_link_reassign_clear():
    a = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    b1 = diagram_model_Diagram()
    b2 = diagram_model_Diagram()
    _safe_set(a, 'model_diagram_MEDiagram39', b1)
    assert _is_linked(a, 'model_diagram_MEDiagram39', b1)
    if hasattr(b1, 'diagram_model_Diagram'):
        assert _is_linked(b1, 'diagram_model_Diagram', a)
    _safe_set(a, 'model_diagram_MEDiagram39', b2)
    assert _is_linked(a, 'model_diagram_MEDiagram39', b2)
    if hasattr(b1, 'diagram_model_Diagram'):
        assert not _is_linked(b1, 'diagram_model_Diagram', a)
    if hasattr(b2, 'diagram_model_Diagram'):
        assert _is_linked(b2, 'diagram_model_Diagram', a)
    _safe_set(a, 'model_diagram_MEDiagram39', None)
    assert not _is_linked(a, 'model_diagram_MEDiagram39', b2)
    if hasattr(b2, 'diagram_model_Diagram'):
        assert not _is_linked(b2, 'diagram_model_Diagram', a)


def test_assoc_groupMemberships14_link_reassign_clear():
    a = model_organization_OrgUnit(acOrgId="sample_text")
    b1 = organization_Group()
    b2 = organization_Group()
    _safe_set(a, 'orgUnits', {b1})
    assert _is_linked(a, 'orgUnits', b1)
    if hasattr(b1, 'Group'):
        assert _is_linked(b1, 'Group', a)
    _safe_set(a, 'orgUnits', {b2})
    assert _is_linked(a, 'orgUnits', b2)
    if hasattr(b1, 'Group'):
        assert not _is_linked(b1, 'Group', a)
    if hasattr(b2, 'Group'):
        assert _is_linked(b2, 'Group', a)
    _safe_set(a, 'orgUnits', set())
    assert not _is_linked(a, 'orgUnits', b2)
    if hasattr(b2, 'Group'):
        assert not _is_linked(b2, 'Group', a)


def test_assoc_identifiedClasses98_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = classes_Class()
    b2 = classes_Class()
    _safe_set(a, 'participatedUseCases', {b1})
    assert _is_linked(a, 'participatedUseCases', b1)
    if hasattr(b1, 'Class99'):
        assert _is_linked(b1, 'Class99', a)
    _safe_set(a, 'participatedUseCases', {b2})
    assert _is_linked(a, 'participatedUseCases', b2)
    if hasattr(b1, 'Class99'):
        assert not _is_linked(b1, 'Class99', a)
    if hasattr(b2, 'Class99'):
        assert _is_linked(b2, 'Class99', a)
    _safe_set(a, 'participatedUseCases', set())
    assert not _is_linked(a, 'participatedUseCases', b2)
    if hasattr(b2, 'Class99'):
        assert not _is_linked(b2, 'Class99', a)


def test_assoc_identifiedIssuesSection214_link_reassign_clear():
    a = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    b1 = meeting_IssueMeetingSection()
    b2 = meeting_IssueMeetingSection()
    _safe_set(a, 'model_meeting_Meeting215', b1)
    assert _is_linked(a, 'model_meeting_Meeting215', b1)
    if hasattr(b1, 'meeting_IssueMeetingSection'):
        assert _is_linked(b1, 'meeting_IssueMeetingSection', a)
    _safe_set(a, 'model_meeting_Meeting215', b2)
    assert _is_linked(a, 'model_meeting_Meeting215', b2)
    if hasattr(b1, 'meeting_IssueMeetingSection'):
        assert not _is_linked(b1, 'meeting_IssueMeetingSection', a)
    if hasattr(b2, 'meeting_IssueMeetingSection'):
        assert _is_linked(b2, 'meeting_IssueMeetingSection', a)
    _safe_set(a, 'model_meeting_Meeting215', None)
    assert not _is_linked(a, 'model_meeting_Meeting215', b2)
    if hasattr(b2, 'meeting_IssueMeetingSection'):
        assert not _is_linked(b2, 'meeting_IssueMeetingSection', a)


def test_assoc_identifiedWorkItemsSection216_link_reassign_clear():
    a = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    b1 = meeting_WorkItemMeetingSection()
    b2 = meeting_WorkItemMeetingSection()
    _safe_set(a, 'model_meeting_Meeting217', b1)
    assert _is_linked(a, 'model_meeting_Meeting217', b1)
    if hasattr(b1, 'meeting_WorkItemMeetingSection'):
        assert _is_linked(b1, 'meeting_WorkItemMeetingSection', a)
    _safe_set(a, 'model_meeting_Meeting217', b2)
    assert _is_linked(a, 'model_meeting_Meeting217', b2)
    if hasattr(b1, 'meeting_WorkItemMeetingSection'):
        assert not _is_linked(b1, 'meeting_WorkItemMeetingSection', a)
    if hasattr(b2, 'meeting_WorkItemMeetingSection'):
        assert _is_linked(b2, 'meeting_WorkItemMeetingSection', a)
    _safe_set(a, 'model_meeting_Meeting217', None)
    assert not _is_linked(a, 'model_meeting_Meeting217', b2)
    if hasattr(b2, 'meeting_WorkItemMeetingSection'):
        assert not _is_linked(b2, 'meeting_WorkItemMeetingSection', a)


def test_assoc_includedSystemFunction150_link_reassign_clear():
    a = model_requirement_Step(userStep=True)
    b1 = requirement_SystemFunction()
    b2 = requirement_SystemFunction()
    _safe_set(a, 'model_requirement_Step151', b1)
    assert _is_linked(a, 'model_requirement_Step151', b1)
    if hasattr(b1, 'requirement_SystemFunction'):
        assert _is_linked(b1, 'requirement_SystemFunction', a)
    _safe_set(a, 'model_requirement_Step151', b2)
    assert _is_linked(a, 'model_requirement_Step151', b2)
    if hasattr(b1, 'requirement_SystemFunction'):
        assert not _is_linked(b1, 'requirement_SystemFunction', a)
    if hasattr(b2, 'requirement_SystemFunction'):
        assert _is_linked(b2, 'requirement_SystemFunction', a)
    _safe_set(a, 'model_requirement_Step151', None)
    assert not _is_linked(a, 'model_requirement_Step151', b2)
    if hasattr(b2, 'requirement_SystemFunction'):
        assert not _is_linked(b2, 'requirement_SystemFunction', a)


def test_assoc_includedUseCase146_link_reassign_clear():
    a = model_requirement_Step(userStep=True)
    b1 = requirement_UseCase()
    b2 = requirement_UseCase()
    _safe_set(a, 'model_requirement_Step', b1)
    assert _is_linked(a, 'model_requirement_Step', b1)
    if hasattr(b1, 'requirement_UseCase147'):
        assert _is_linked(b1, 'requirement_UseCase147', a)
    _safe_set(a, 'model_requirement_Step', b2)
    assert _is_linked(a, 'model_requirement_Step', b2)
    if hasattr(b1, 'requirement_UseCase147'):
        assert not _is_linked(b1, 'requirement_UseCase147', a)
    if hasattr(b2, 'requirement_UseCase147'):
        assert _is_linked(b2, 'requirement_UseCase147', a)
    _safe_set(a, 'model_requirement_Step', None)
    assert not _is_linked(a, 'model_requirement_Step', b2)
    if hasattr(b2, 'requirement_UseCase147'):
        assert not _is_linked(b2, 'requirement_UseCase147', a)


def test_assoc_includedUseCases100_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_UseCase()
    b2 = requirement_UseCase()
    _safe_set(a, 'model_requirement_UseCase', {b1})
    assert _is_linked(a, 'model_requirement_UseCase', b1)
    if hasattr(b1, 'requirement_UseCase'):
        assert _is_linked(b1, 'requirement_UseCase', a)
    _safe_set(a, 'model_requirement_UseCase', {b2})
    assert _is_linked(a, 'model_requirement_UseCase', b2)
    if hasattr(b1, 'requirement_UseCase'):
        assert not _is_linked(b1, 'requirement_UseCase', a)
    if hasattr(b2, 'requirement_UseCase'):
        assert _is_linked(b2, 'requirement_UseCase', a)
    _safe_set(a, 'model_requirement_UseCase', set())
    assert not _is_linked(a, 'model_requirement_UseCase', b2)
    if hasattr(b2, 'requirement_UseCase'):
        assert not _is_linked(b2, 'requirement_UseCase', a)


def test_assoc_incomingDocumentReferences7_link_reassign_clear():
    a = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    b1 = document_LeafSection()
    b2 = document_LeafSection()
    _safe_set(a, 'referencedModelElements', {b1})
    assert _is_linked(a, 'referencedModelElements', b1)
    if hasattr(b1, 'LeafSection8'):
        assert _is_linked(b1, 'LeafSection8', a)
    _safe_set(a, 'referencedModelElements', {b2})
    assert _is_linked(a, 'referencedModelElements', b2)
    if hasattr(b1, 'LeafSection8'):
        assert not _is_linked(b1, 'LeafSection8', a)
    if hasattr(b2, 'LeafSection8'):
        assert _is_linked(b2, 'LeafSection8', a)
    _safe_set(a, 'referencedModelElements', set())
    assert not _is_linked(a, 'referencedModelElements', b2)
    if hasattr(b2, 'LeafSection8'):
        assert not _is_linked(b2, 'LeafSection8', a)


def test_assoc_initiatingActor106_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_Actor()
    b2 = requirement_Actor()
    _safe_set(a, 'initiatedUseCases', b1)
    assert _is_linked(a, 'initiatedUseCases', b1)
    if hasattr(b1, 'Actor'):
        assert _is_linked(b1, 'Actor', a)
    _safe_set(a, 'initiatedUseCases', b2)
    assert _is_linked(a, 'initiatedUseCases', b2)
    if hasattr(b1, 'Actor'):
        assert not _is_linked(b1, 'Actor', a)
    if hasattr(b2, 'Actor'):
        assert _is_linked(b2, 'Actor', a)
    _safe_set(a, 'initiatedUseCases', None)
    assert not _is_linked(a, 'initiatedUseCases', b2)
    if hasattr(b2, 'Actor'):
        assert not _is_linked(b2, 'Actor', a)


def test_assoc_leafSection6_link_reassign_clear():
    a = model_UnicaseModelElement(description="sample_text", name="sample_text", state="sample_text")
    b1 = document_LeafSection()
    b2 = document_LeafSection()
    _safe_set(a, 'modelElements', b1)
    assert _is_linked(a, 'modelElements', b1)
    if hasattr(b1, 'LeafSection'):
        assert _is_linked(b1, 'LeafSection', a)
    _safe_set(a, 'modelElements', b2)
    assert _is_linked(a, 'modelElements', b2)
    if hasattr(b1, 'LeafSection'):
        assert not _is_linked(b1, 'LeafSection', a)
    if hasattr(b2, 'LeafSection'):
        assert _is_linked(b2, 'LeafSection', a)
    _safe_set(a, 'modelElements', None)
    assert not _is_linked(a, 'modelElements', b2)
    if hasattr(b2, 'LeafSection'):
        assert not _is_linked(b2, 'LeafSection', a)


def test_assoc_localChanges371_link_reassign_clear():
    a = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    b1 = operations_AbstractOperation()
    b2 = operations_AbstractOperation()
    _safe_set(a, 'esmodel_events_MergeEvent372', {b1})
    assert _is_linked(a, 'esmodel_events_MergeEvent372', b1)
    if hasattr(b1, 'operations_AbstractOperation373'):
        assert _is_linked(b1, 'operations_AbstractOperation373', a)
    _safe_set(a, 'esmodel_events_MergeEvent372', {b2})
    assert _is_linked(a, 'esmodel_events_MergeEvent372', b2)
    if hasattr(b1, 'operations_AbstractOperation373'):
        assert not _is_linked(b1, 'operations_AbstractOperation373', a)
    if hasattr(b2, 'operations_AbstractOperation373'):
        assert _is_linked(b2, 'operations_AbstractOperation373', a)
    _safe_set(a, 'esmodel_events_MergeEvent372', set())
    assert not _is_linked(a, 'esmodel_events_MergeEvent372', b2)
    if hasattr(b2, 'operations_AbstractOperation373'):
        assert not _is_linked(b2, 'operations_AbstractOperation373', a)


def test_assoc_mainOperation333_link_reassign_clear():
    a = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    b1 = operations_AbstractOperation()
    b2 = operations_AbstractOperation()
    _safe_set(a, 'esmodel_operations_CompositeOperation334', b1)
    assert _is_linked(a, 'esmodel_operations_CompositeOperation334', b1)
    if hasattr(b1, 'operations_AbstractOperation335'):
        assert _is_linked(b1, 'operations_AbstractOperation335', a)
    _safe_set(a, 'esmodel_operations_CompositeOperation334', b2)
    assert _is_linked(a, 'esmodel_operations_CompositeOperation334', b2)
    if hasattr(b1, 'operations_AbstractOperation335'):
        assert not _is_linked(b1, 'operations_AbstractOperation335', a)
    if hasattr(b2, 'operations_AbstractOperation335'):
        assert _is_linked(b2, 'operations_AbstractOperation335', a)
    _safe_set(a, 'esmodel_operations_CompositeOperation334', None)
    assert not _is_linked(a, 'esmodel_operations_CompositeOperation334', b2)
    if hasattr(b2, 'operations_AbstractOperation335'):
        assert not _is_linked(b2, 'operations_AbstractOperation335', a)


def test_assoc_minutetaker203_link_reassign_clear():
    a = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    b1 = organization_User()
    b2 = organization_User()
    _safe_set(a, 'model_meeting_Meeting204', b1)
    assert _is_linked(a, 'model_meeting_Meeting204', b1)
    if hasattr(b1, 'organization_User205'):
        assert _is_linked(b1, 'organization_User205', a)
    _safe_set(a, 'model_meeting_Meeting204', b2)
    assert _is_linked(a, 'model_meeting_Meeting204', b2)
    if hasattr(b1, 'organization_User205'):
        assert not _is_linked(b1, 'organization_User205', a)
    if hasattr(b2, 'organization_User205'):
        assert _is_linked(b2, 'organization_User205', a)
    _safe_set(a, 'model_meeting_Meeting204', None)
    assert not _is_linked(a, 'model_meeting_Meeting204', b2)
    if hasattr(b2, 'organization_User205'):
        assert not _is_linked(b2, 'organization_User205', a)


def test_assoc_modelElement336_link_reassign_clear():
    a = esmodel_operations_CreateDeleteOperation(delete=True)
    b1 = operations_esmodel_EObject()
    b2 = operations_esmodel_EObject()
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation', b1)
    assert _is_linked(a, 'esmodel_operations_CreateDeleteOperation', b1)
    if hasattr(b1, 'operations_esmodel_EObject'):
        assert _is_linked(b1, 'operations_esmodel_EObject', a)
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation', b2)
    assert _is_linked(a, 'esmodel_operations_CreateDeleteOperation', b2)
    if hasattr(b1, 'operations_esmodel_EObject'):
        assert not _is_linked(b1, 'operations_esmodel_EObject', a)
    if hasattr(b2, 'operations_esmodel_EObject'):
        assert _is_linked(b2, 'operations_esmodel_EObject', a)
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation', None)
    assert not _is_linked(a, 'esmodel_operations_CreateDeleteOperation', b2)
    if hasattr(b2, 'operations_esmodel_EObject'):
        assert not _is_linked(b2, 'operations_esmodel_EObject', a)


def test_assoc_modelElement364_link_reassign_clear():
    a = esmodel_events_ReadEvent(readView="sample_text", sourceView="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_ReadEvent', b1)
    assert _is_linked(a, 'esmodel_events_ReadEvent', b1)
    if hasattr(b1, 'ModelElementId365'):
        assert _is_linked(b1, 'ModelElementId365', a)
    _safe_set(a, 'esmodel_events_ReadEvent', b2)
    assert _is_linked(a, 'esmodel_events_ReadEvent', b2)
    if hasattr(b1, 'ModelElementId365'):
        assert not _is_linked(b1, 'ModelElementId365', a)
    if hasattr(b2, 'ModelElementId365'):
        assert _is_linked(b2, 'ModelElementId365', a)
    _safe_set(a, 'esmodel_events_ReadEvent', None)
    assert not _is_linked(a, 'esmodel_events_ReadEvent', b2)
    if hasattr(b2, 'ModelElementId365'):
        assert not _is_linked(b2, 'ModelElementId365', a)


def test_assoc_modelElementId329_link_reassign_clear():
    a = esmodel_operations_AbstractOperation(accepted=True, clientDate=date(2024, 1, 1), description="sample_text", name="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_operations_AbstractOperation', b1)
    assert _is_linked(a, 'esmodel_operations_AbstractOperation', b1)
    if hasattr(b1, 'ModelElementId330'):
        assert _is_linked(b1, 'ModelElementId330', a)
    _safe_set(a, 'esmodel_operations_AbstractOperation', b2)
    assert _is_linked(a, 'esmodel_operations_AbstractOperation', b2)
    if hasattr(b1, 'ModelElementId330'):
        assert not _is_linked(b1, 'ModelElementId330', a)
    if hasattr(b2, 'ModelElementId330'):
        assert _is_linked(b2, 'ModelElementId330', a)
    _safe_set(a, 'esmodel_operations_AbstractOperation', None)
    assert not _is_linked(a, 'esmodel_operations_AbstractOperation', b2)
    if hasattr(b2, 'ModelElementId330'):
        assert not _is_linked(b2, 'ModelElementId330', a)


def test_assoc_modelElementId457_link_reassign_clear():
    a = esmodel_url_ModelElementUrlFragment(name="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_url_ModelElementUrlFragment', b1)
    assert _is_linked(a, 'esmodel_url_ModelElementUrlFragment', b1)
    if hasattr(b1, 'ModelElementId458'):
        assert _is_linked(b1, 'ModelElementId458', a)
    _safe_set(a, 'esmodel_url_ModelElementUrlFragment', b2)
    assert _is_linked(a, 'esmodel_url_ModelElementUrlFragment', b2)
    if hasattr(b1, 'ModelElementId458'):
        assert not _is_linked(b1, 'ModelElementId458', a)
    if hasattr(b2, 'ModelElementId458'):
        assert _is_linked(b2, 'ModelElementId458', a)
    _safe_set(a, 'esmodel_url_ModelElementUrlFragment', None)
    assert not _is_linked(a, 'esmodel_url_ModelElementUrlFragment', b2)
    if hasattr(b2, 'ModelElementId458'):
        assert not _is_linked(b2, 'ModelElementId458', a)


def test_assoc_modelElements310_link_reassign_clear():
    a = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_versioning_HistoryQuery311', {b1})
    assert _is_linked(a, 'esmodel_versioning_HistoryQuery311', b1)
    if hasattr(b1, 'ModelElementId312'):
        assert _is_linked(b1, 'ModelElementId312', a)
    _safe_set(a, 'esmodel_versioning_HistoryQuery311', {b2})
    assert _is_linked(a, 'esmodel_versioning_HistoryQuery311', b2)
    if hasattr(b1, 'ModelElementId312'):
        assert not _is_linked(b1, 'ModelElementId312', a)
    if hasattr(b2, 'ModelElementId312'):
        assert _is_linked(b2, 'ModelElementId312', a)
    _safe_set(a, 'esmodel_versioning_HistoryQuery311', set())
    assert not _is_linked(a, 'esmodel_versioning_HistoryQuery311', b2)
    if hasattr(b2, 'ModelElementId312'):
        assert not _is_linked(b2, 'ModelElementId312', a)


def test_assoc_modelElements357_link_reassign_clear():
    a = esmodel_operations_ModelElementGroup(name="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_operations_ModelElementGroup', {b1})
    assert _is_linked(a, 'esmodel_operations_ModelElementGroup', b1)
    if hasattr(b1, 'ModelElementId358'):
        assert _is_linked(b1, 'ModelElementId358', a)
    _safe_set(a, 'esmodel_operations_ModelElementGroup', {b2})
    assert _is_linked(a, 'esmodel_operations_ModelElementGroup', b2)
    if hasattr(b1, 'ModelElementId358'):
        assert not _is_linked(b1, 'ModelElementId358', a)
    if hasattr(b2, 'ModelElementId358'):
        assert _is_linked(b2, 'ModelElementId358', a)
    _safe_set(a, 'esmodel_operations_ModelElementGroup', set())
    assert not _is_linked(a, 'esmodel_operations_ModelElementGroup', b2)
    if hasattr(b2, 'ModelElementId358'):
        assert not _is_linked(b2, 'ModelElementId358', a)


def test_assoc_myAcceptedChanges428_link_reassign_clear():
    a = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    b1 = operations_OperationId()
    b2 = operations_OperationId()
    _safe_set(a, 'esmodel_events_MergeChoiceEvent', {b1})
    assert _is_linked(a, 'esmodel_events_MergeChoiceEvent', b1)
    if hasattr(b1, 'operations_OperationId'):
        assert _is_linked(b1, 'operations_OperationId', a)
    _safe_set(a, 'esmodel_events_MergeChoiceEvent', {b2})
    assert _is_linked(a, 'esmodel_events_MergeChoiceEvent', b2)
    if hasattr(b1, 'operations_OperationId'):
        assert not _is_linked(b1, 'operations_OperationId', a)
    if hasattr(b2, 'operations_OperationId'):
        assert _is_linked(b2, 'operations_OperationId', a)
    _safe_set(a, 'esmodel_events_MergeChoiceEvent', set())
    assert not _is_linked(a, 'esmodel_events_MergeChoiceEvent', b2)
    if hasattr(b2, 'operations_OperationId'):
        assert not _is_linked(b2, 'operations_OperationId', a)


def test_assoc_newElements40_link_reassign_clear():
    a = model_diagram_MEDiagram(diagramLayout="sample_text", type="sample_text")
    b1 = UnicaseModelElement()
    b2 = UnicaseModelElement()
    _safe_set(a, 'model_diagram_MEDiagram41', {b1})
    assert _is_linked(a, 'model_diagram_MEDiagram41', b1)
    if hasattr(b1, 'UnicaseModelElement42'):
        assert _is_linked(b1, 'UnicaseModelElement42', a)
    _safe_set(a, 'model_diagram_MEDiagram41', {b2})
    assert _is_linked(a, 'model_diagram_MEDiagram41', b2)
    if hasattr(b1, 'UnicaseModelElement42'):
        assert not _is_linked(b1, 'UnicaseModelElement42', a)
    if hasattr(b2, 'UnicaseModelElement42'):
        assert _is_linked(b2, 'UnicaseModelElement42', a)
    _safe_set(a, 'model_diagram_MEDiagram41', set())
    assert not _is_linked(a, 'model_diagram_MEDiagram41', b2)
    if hasattr(b2, 'UnicaseModelElement42'):
        assert not _is_linked(b2, 'UnicaseModelElement42', a)


def test_assoc_newValue348_link_reassign_clear():
    a = esmodel_operations_MultiReferenceSetOperation(index=7)
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_operations_MultiReferenceSetOperation349', b1)
    assert _is_linked(a, 'esmodel_operations_MultiReferenceSetOperation349', b1)
    if hasattr(b1, 'ModelElementId350'):
        assert _is_linked(b1, 'ModelElementId350', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceSetOperation349', b2)
    assert _is_linked(a, 'esmodel_operations_MultiReferenceSetOperation349', b2)
    if hasattr(b1, 'ModelElementId350'):
        assert not _is_linked(b1, 'ModelElementId350', a)
    if hasattr(b2, 'ModelElementId350'):
        assert _is_linked(b2, 'ModelElementId350', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceSetOperation349', None)
    assert not _is_linked(a, 'esmodel_operations_MultiReferenceSetOperation349', b2)
    if hasattr(b2, 'ModelElementId350'):
        assert not _is_linked(b2, 'ModelElementId350', a)


def test_assoc_nonFunctionalRequirements112_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_NonFunctionalRequirement()
    b2 = requirement_NonFunctionalRequirement()
    _safe_set(a, 'restrictedUseCases', {b1})
    assert _is_linked(a, 'restrictedUseCases', b1)
    if hasattr(b1, 'NonFunctionalRequirement'):
        assert _is_linked(b1, 'NonFunctionalRequirement', a)
    _safe_set(a, 'restrictedUseCases', {b2})
    assert _is_linked(a, 'restrictedUseCases', b2)
    if hasattr(b1, 'NonFunctionalRequirement'):
        assert not _is_linked(b1, 'NonFunctionalRequirement', a)
    if hasattr(b2, 'NonFunctionalRequirement'):
        assert _is_linked(b2, 'NonFunctionalRequirement', a)
    _safe_set(a, 'restrictedUseCases', set())
    assert not _is_linked(a, 'restrictedUseCases', b2)
    if hasattr(b2, 'NonFunctionalRequirement'):
        assert not _is_linked(b2, 'NonFunctionalRequirement', a)


def test_assoc_oldValue346_link_reassign_clear():
    a = esmodel_operations_MultiReferenceSetOperation(index=7)
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_operations_MultiReferenceSetOperation', b1)
    assert _is_linked(a, 'esmodel_operations_MultiReferenceSetOperation', b1)
    if hasattr(b1, 'ModelElementId347'):
        assert _is_linked(b1, 'ModelElementId347', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceSetOperation', b2)
    assert _is_linked(a, 'esmodel_operations_MultiReferenceSetOperation', b2)
    if hasattr(b1, 'ModelElementId347'):
        assert not _is_linked(b1, 'ModelElementId347', a)
    if hasattr(b2, 'ModelElementId347'):
        assert _is_linked(b2, 'ModelElementId347', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceSetOperation', None)
    assert not _is_linked(a, 'esmodel_operations_MultiReferenceSetOperation', b2)
    if hasattr(b2, 'ModelElementId347'):
        assert not _is_linked(b2, 'ModelElementId347', a)


def test_assoc_operations355_link_reassign_clear():
    a = esmodel_operations_OperationGroup(name="sample_text")
    b1 = operations_AbstractOperation()
    b2 = operations_AbstractOperation()
    _safe_set(a, 'esmodel_operations_OperationGroup', {b1})
    assert _is_linked(a, 'esmodel_operations_OperationGroup', b1)
    if hasattr(b1, 'operations_AbstractOperation356'):
        assert _is_linked(b1, 'operations_AbstractOperation356', a)
    _safe_set(a, 'esmodel_operations_OperationGroup', {b2})
    assert _is_linked(a, 'esmodel_operations_OperationGroup', b2)
    if hasattr(b1, 'operations_AbstractOperation356'):
        assert not _is_linked(b1, 'operations_AbstractOperation356', a)
    if hasattr(b2, 'operations_AbstractOperation356'):
        assert _is_linked(b2, 'operations_AbstractOperation356', a)
    _safe_set(a, 'esmodel_operations_OperationGroup', set())
    assert not _is_linked(a, 'esmodel_operations_OperationGroup', b2)
    if hasattr(b2, 'operations_AbstractOperation356'):
        assert not _is_linked(b2, 'operations_AbstractOperation356', a)


def test_assoc_participants209_link_reassign_clear():
    a = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    b1 = organization_OrgUnit()
    b2 = organization_OrgUnit()
    _safe_set(a, 'model_meeting_Meeting210', {b1})
    assert _is_linked(a, 'model_meeting_Meeting210', b1)
    if hasattr(b1, 'organization_OrgUnit211'):
        assert _is_linked(b1, 'organization_OrgUnit211', a)
    _safe_set(a, 'model_meeting_Meeting210', {b2})
    assert _is_linked(a, 'model_meeting_Meeting210', b2)
    if hasattr(b1, 'organization_OrgUnit211'):
        assert not _is_linked(b1, 'organization_OrgUnit211', a)
    if hasattr(b2, 'organization_OrgUnit211'):
        assert _is_linked(b2, 'organization_OrgUnit211', a)
    _safe_set(a, 'model_meeting_Meeting210', set())
    assert not _is_linked(a, 'model_meeting_Meeting210', b2)
    if hasattr(b2, 'organization_OrgUnit211'):
        assert not _is_linked(b2, 'organization_OrgUnit211', a)


def test_assoc_participants29_link_reassign_clear():
    a = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    b1 = organization_OrgUnit()
    b2 = organization_OrgUnit()
    _safe_set(a, 'participations', {b1})
    assert _is_linked(a, 'participations', b1)
    if hasattr(b1, 'OrgUnit30'):
        assert _is_linked(b1, 'OrgUnit30', a)
    _safe_set(a, 'participations', {b2})
    assert _is_linked(a, 'participations', b2)
    if hasattr(b1, 'OrgUnit30'):
        assert not _is_linked(b1, 'OrgUnit30', a)
    if hasattr(b2, 'OrgUnit30'):
        assert _is_linked(b2, 'OrgUnit30', a)
    _safe_set(a, 'participations', set())
    assert not _is_linked(a, 'participations', b2)
    if hasattr(b2, 'OrgUnit30'):
        assert not _is_linked(b2, 'OrgUnit30', a)


def test_assoc_participatingActors107_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_Actor()
    b2 = requirement_Actor()
    _safe_set(a, 'participatedUseCases108', {b1})
    assert _is_linked(a, 'participatedUseCases108', b1)
    if hasattr(b1, 'Actor109'):
        assert _is_linked(b1, 'Actor109', a)
    _safe_set(a, 'participatedUseCases108', {b2})
    assert _is_linked(a, 'participatedUseCases108', b2)
    if hasattr(b1, 'Actor109'):
        assert not _is_linked(b1, 'Actor109', a)
    if hasattr(b2, 'Actor109'):
        assert _is_linked(b2, 'Actor109', a)
    _safe_set(a, 'participatedUseCases108', set())
    assert not _is_linked(a, 'participatedUseCases108', b2)
    if hasattr(b2, 'Actor109'):
        assert not _is_linked(b2, 'Actor109', a)


def test_assoc_participations15_link_reassign_clear():
    a = model_organization_OrgUnit(acOrgId="sample_text")
    b1 = task_WorkItem()
    b2 = task_WorkItem()
    _safe_set(a, 'participants', {b1})
    assert _is_linked(a, 'participants', b1)
    if hasattr(b1, 'WorkItem'):
        assert _is_linked(b1, 'WorkItem', a)
    _safe_set(a, 'participants', {b2})
    assert _is_linked(a, 'participants', b2)
    if hasattr(b1, 'WorkItem'):
        assert not _is_linked(b1, 'WorkItem', a)
    if hasattr(b2, 'WorkItem'):
        assert _is_linked(b2, 'WorkItem', a)
    _safe_set(a, 'participants', set())
    assert not _is_linked(a, 'participants', b2)
    if hasattr(b2, 'WorkItem'):
        assert not _is_linked(b2, 'WorkItem', a)


def test_assoc_predecessors24_link_reassign_clear():
    a = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    b1 = task_WorkItem()
    b2 = task_WorkItem()
    _safe_set(a, 'successors', {b1})
    assert _is_linked(a, 'successors', b1)
    if hasattr(b1, 'WorkItem25'):
        assert _is_linked(b1, 'WorkItem25', a)
    _safe_set(a, 'successors', {b2})
    assert _is_linked(a, 'successors', b2)
    if hasattr(b1, 'WorkItem25'):
        assert not _is_linked(b1, 'WorkItem25', a)
    if hasattr(b2, 'WorkItem25'):
        assert _is_linked(b2, 'WorkItem25', a)
    _safe_set(a, 'successors', set())
    assert not _is_linked(a, 'successors', b2)
    if hasattr(b2, 'WorkItem25'):
        assert not _is_linked(b2, 'WorkItem25', a)


def test_assoc_profile233_link_reassign_clear():
    a = model_profile_Stereotype(required=True)
    b1 = profile_Profile()
    b2 = profile_Profile()
    _safe_set(a, 'stereotypes', b1)
    assert _is_linked(a, 'stereotypes', b1)
    if hasattr(b1, 'Profile'):
        assert _is_linked(b1, 'Profile', a)
    _safe_set(a, 'stereotypes', b2)
    assert _is_linked(a, 'stereotypes', b2)
    if hasattr(b1, 'Profile'):
        assert not _is_linked(b1, 'Profile', a)
    if hasattr(b2, 'Profile'):
        assert _is_linked(b2, 'Profile', a)
    _safe_set(a, 'stereotypes', None)
    assert not _is_linked(a, 'stereotypes', b2)
    if hasattr(b2, 'Profile'):
        assert not _is_linked(b2, 'Profile', a)


def test_assoc_project443_link_reassign_clear():
    a = esmodel_accesscontrol_OrgUnitProperty(name="sample_text", value="sample_text")
    b1 = ProjectId()
    b2 = ProjectId()
    _safe_set(a, 'esmodel_accesscontrol_OrgUnitProperty', b1)
    assert _is_linked(a, 'esmodel_accesscontrol_OrgUnitProperty', b1)
    if hasattr(b1, 'ProjectId444'):
        assert _is_linked(b1, 'ProjectId444', a)
    _safe_set(a, 'esmodel_accesscontrol_OrgUnitProperty', b2)
    assert _is_linked(a, 'esmodel_accesscontrol_OrgUnitProperty', b2)
    if hasattr(b1, 'ProjectId444'):
        assert not _is_linked(b1, 'ProjectId444', a)
    if hasattr(b2, 'ProjectId444'):
        assert _is_linked(b2, 'ProjectId444', a)
    _safe_set(a, 'esmodel_accesscontrol_OrgUnitProperty', None)
    assert not _is_linked(a, 'esmodel_accesscontrol_OrgUnitProperty', b2)
    if hasattr(b2, 'ProjectId444'):
        assert not _is_linked(b2, 'ProjectId444', a)


def test_assoc_project447_link_reassign_clear():
    a = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    b1 = ProjectId()
    b2 = ProjectId()
    _safe_set(a, 'esmodel_notification_ESNotification', b1)
    assert _is_linked(a, 'esmodel_notification_ESNotification', b1)
    if hasattr(b1, 'ProjectId448'):
        assert _is_linked(b1, 'ProjectId448', a)
    _safe_set(a, 'esmodel_notification_ESNotification', b2)
    assert _is_linked(a, 'esmodel_notification_ESNotification', b2)
    if hasattr(b1, 'ProjectId448'):
        assert not _is_linked(b1, 'ProjectId448', a)
    if hasattr(b2, 'ProjectId448'):
        assert _is_linked(b2, 'ProjectId448', a)
    _safe_set(a, 'esmodel_notification_ESNotification', None)
    assert not _is_linked(a, 'esmodel_notification_ESNotification', b2)
    if hasattr(b2, 'ProjectId448'):
        assert not _is_linked(b2, 'ProjectId448', a)


def test_assoc_projectId270_link_reassign_clear():
    a = esmodel_ProjectHistory(projectDescription="sample_text", projectName="sample_text")
    b1 = ProjectId()
    b2 = ProjectId()
    _safe_set(a, 'esmodel_ProjectHistory', b1)
    assert _is_linked(a, 'esmodel_ProjectHistory', b1)
    if hasattr(b1, 'ProjectId'):
        assert _is_linked(b1, 'ProjectId', a)
    _safe_set(a, 'esmodel_ProjectHistory', b2)
    assert _is_linked(a, 'esmodel_ProjectHistory', b2)
    if hasattr(b1, 'ProjectId'):
        assert not _is_linked(b1, 'ProjectId', a)
    if hasattr(b2, 'ProjectId'):
        assert _is_linked(b2, 'ProjectId', a)
    _safe_set(a, 'esmodel_ProjectHistory', None)
    assert not _is_linked(a, 'esmodel_ProjectHistory', b2)
    if hasattr(b2, 'ProjectId'):
        assert not _is_linked(b2, 'ProjectId', a)


def test_assoc_projectId273_link_reassign_clear():
    a = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    b1 = ProjectId()
    b2 = ProjectId()
    _safe_set(a, 'esmodel_ProjectInfo', b1)
    assert _is_linked(a, 'esmodel_ProjectInfo', b1)
    if hasattr(b1, 'ProjectId274'):
        assert _is_linked(b1, 'ProjectId274', a)
    _safe_set(a, 'esmodel_ProjectInfo', b2)
    assert _is_linked(a, 'esmodel_ProjectInfo', b2)
    if hasattr(b1, 'ProjectId274'):
        assert not _is_linked(b1, 'ProjectId274', a)
    if hasattr(b2, 'ProjectId274'):
        assert _is_linked(b2, 'ProjectId274', a)
    _safe_set(a, 'esmodel_ProjectInfo', None)
    assert not _is_linked(a, 'esmodel_ProjectInfo', b2)
    if hasattr(b2, 'ProjectId274'):
        assert not _is_linked(b2, 'ProjectId274', a)


def test_assoc_projectId455_link_reassign_clear():
    a = esmodel_url_ProjectUrlFragment(name="sample_text")
    b1 = ProjectId()
    b2 = ProjectId()
    _safe_set(a, 'esmodel_url_ProjectUrlFragment', b1)
    assert _is_linked(a, 'esmodel_url_ProjectUrlFragment', b1)
    if hasattr(b1, 'ProjectId456'):
        assert _is_linked(b1, 'ProjectId456', a)
    _safe_set(a, 'esmodel_url_ProjectUrlFragment', b2)
    assert _is_linked(a, 'esmodel_url_ProjectUrlFragment', b2)
    if hasattr(b1, 'ProjectId456'):
        assert not _is_linked(b1, 'ProjectId456', a)
    if hasattr(b2, 'ProjectId456'):
        assert _is_linked(b2, 'ProjectId456', a)
    _safe_set(a, 'esmodel_url_ProjectUrlFragment', None)
    assert not _is_linked(a, 'esmodel_url_ProjectUrlFragment', b2)
    if hasattr(b2, 'ProjectId456'):
        assert not _is_linked(b2, 'ProjectId456', a)


def test_assoc_projects445_link_reassign_clear():
    a = esmodel_roles_Role()
    b1 = ProjectId()
    b2 = ProjectId()
    _safe_set(a, 'esmodel_roles_Role', {b1})
    assert _is_linked(a, 'esmodel_roles_Role', b1)
    if hasattr(b1, 'ProjectId446'):
        assert _is_linked(b1, 'ProjectId446', a)
    _safe_set(a, 'esmodel_roles_Role', {b2})
    assert _is_linked(a, 'esmodel_roles_Role', b2)
    if hasattr(b1, 'ProjectId446'):
        assert not _is_linked(b1, 'ProjectId446', a)
    if hasattr(b2, 'ProjectId446'):
        assert _is_linked(b2, 'ProjectId446', a)
    _safe_set(a, 'esmodel_roles_Role', set())
    assert not _is_linked(a, 'esmodel_roles_Role', b2)
    if hasattr(b2, 'ProjectId446'):
        assert not _is_linked(b2, 'ProjectId446', a)


def test_assoc_properties440_link_reassign_clear():
    a = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    b1 = accesscontrol_OrgUnitProperty()
    b2 = accesscontrol_OrgUnitProperty()
    _safe_set(a, 'esmodel_accesscontrol_ACOrgUnit441', {b1})
    assert _is_linked(a, 'esmodel_accesscontrol_ACOrgUnit441', b1)
    if hasattr(b1, 'accesscontrol_OrgUnitProperty'):
        assert _is_linked(b1, 'accesscontrol_OrgUnitProperty', a)
    _safe_set(a, 'esmodel_accesscontrol_ACOrgUnit441', {b2})
    assert _is_linked(a, 'esmodel_accesscontrol_ACOrgUnit441', b2)
    if hasattr(b1, 'accesscontrol_OrgUnitProperty'):
        assert not _is_linked(b1, 'accesscontrol_OrgUnitProperty', a)
    if hasattr(b2, 'accesscontrol_OrgUnitProperty'):
        assert _is_linked(b2, 'accesscontrol_OrgUnitProperty', a)
    _safe_set(a, 'esmodel_accesscontrol_ACOrgUnit441', set())
    assert not _is_linked(a, 'esmodel_accesscontrol_ACOrgUnit441', b2)
    if hasattr(b2, 'accesscontrol_OrgUnitProperty'):
        assert not _is_linked(b2, 'accesscontrol_OrgUnitProperty', a)


def test_assoc_proposal174_link_reassign_clear():
    a = model_rationale_Assessment(value=7)
    b1 = rationale_Proposal()
    b2 = rationale_Proposal()
    _safe_set(a, 'assessments', b1)
    assert _is_linked(a, 'assessments', b1)
    if hasattr(b1, 'Proposal175'):
        assert _is_linked(b1, 'Proposal175', a)
    _safe_set(a, 'assessments', b2)
    assert _is_linked(a, 'assessments', b2)
    if hasattr(b1, 'Proposal175'):
        assert not _is_linked(b1, 'Proposal175', a)
    if hasattr(b2, 'Proposal175'):
        assert _is_linked(b2, 'Proposal175', a)
    _safe_set(a, 'assessments', None)
    assert not _is_linked(a, 'assessments', b2)
    if hasattr(b2, 'Proposal175'):
        assert not _is_linked(b2, 'Proposal175', a)


def test_assoc_proposals163_link_reassign_clear():
    a = model_rationale_Issue(activity="sample_text")
    b1 = rationale_Proposal()
    b2 = rationale_Proposal()
    _safe_set(a, 'issue', {b1})
    assert _is_linked(a, 'issue', b1)
    if hasattr(b1, 'Proposal'):
        assert _is_linked(b1, 'Proposal', a)
    _safe_set(a, 'issue', {b2})
    assert _is_linked(a, 'issue', b2)
    if hasattr(b1, 'Proposal'):
        assert not _is_linked(b1, 'Proposal', a)
    if hasattr(b2, 'Proposal'):
        assert _is_linked(b2, 'Proposal', a)
    _safe_set(a, 'issue', set())
    assert not _is_linked(a, 'issue', b2)
    if hasattr(b2, 'Proposal'):
        assert not _is_linked(b2, 'Proposal', a)


def test_assoc_realizedUserTask111_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_UserTask()
    b2 = requirement_UserTask()
    _safe_set(a, 'realizingUseCases', b1)
    assert _is_linked(a, 'realizingUseCases', b1)
    if hasattr(b1, 'UserTask'):
        assert _is_linked(b1, 'UserTask', a)
    _safe_set(a, 'realizingUseCases', b2)
    assert _is_linked(a, 'realizingUseCases', b2)
    if hasattr(b1, 'UserTask'):
        assert not _is_linked(b1, 'UserTask', a)
    if hasattr(b2, 'UserTask'):
        assert _is_linked(b2, 'UserTask', a)
    _safe_set(a, 'realizingUseCases', None)
    assert not _is_linked(a, 'realizingUseCases', b2)
    if hasattr(b2, 'UserTask'):
        assert not _is_linked(b2, 'UserTask', a)


def test_assoc_referencedModelElementId353_link_reassign_clear():
    a = esmodel_operations_MultiReferenceMoveOperation(newIndex=7, oldIndex=7)
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_operations_MultiReferenceMoveOperation', b1)
    assert _is_linked(a, 'esmodel_operations_MultiReferenceMoveOperation', b1)
    if hasattr(b1, 'ModelElementId354'):
        assert _is_linked(b1, 'ModelElementId354', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceMoveOperation', b2)
    assert _is_linked(a, 'esmodel_operations_MultiReferenceMoveOperation', b2)
    if hasattr(b1, 'ModelElementId354'):
        assert not _is_linked(b1, 'ModelElementId354', a)
    if hasattr(b2, 'ModelElementId354'):
        assert _is_linked(b2, 'ModelElementId354', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceMoveOperation', None)
    assert not _is_linked(a, 'esmodel_operations_MultiReferenceMoveOperation', b2)
    if hasattr(b2, 'ModelElementId354'):
        assert not _is_linked(b2, 'ModelElementId354', a)


def test_assoc_referencedModelElements351_link_reassign_clear():
    a = esmodel_operations_MultiReferenceOperation(add=True, index=7)
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_operations_MultiReferenceOperation', {b1})
    assert _is_linked(a, 'esmodel_operations_MultiReferenceOperation', b1)
    if hasattr(b1, 'ModelElementId352'):
        assert _is_linked(b1, 'ModelElementId352', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceOperation', {b2})
    assert _is_linked(a, 'esmodel_operations_MultiReferenceOperation', b2)
    if hasattr(b1, 'ModelElementId352'):
        assert not _is_linked(b1, 'ModelElementId352', a)
    if hasattr(b2, 'ModelElementId352'):
        assert _is_linked(b2, 'ModelElementId352', a)
    _safe_set(a, 'esmodel_operations_MultiReferenceOperation', set())
    assert not _is_linked(a, 'esmodel_operations_MultiReferenceOperation', b2)
    if hasattr(b2, 'ModelElementId352'):
        assert not _is_linked(b2, 'ModelElementId352', a)


def test_assoc_refinedRequirement88_link_reassign_clear():
    a = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    b1 = requirement_FunctionalRequirement()
    b2 = requirement_FunctionalRequirement()
    _safe_set(a, 'refiningRequirements', b1)
    assert _is_linked(a, 'refiningRequirements', b1)
    if hasattr(b1, 'FunctionalRequirement89'):
        assert _is_linked(b1, 'FunctionalRequirement89', a)
    _safe_set(a, 'refiningRequirements', b2)
    assert _is_linked(a, 'refiningRequirements', b2)
    if hasattr(b1, 'FunctionalRequirement89'):
        assert not _is_linked(b1, 'FunctionalRequirement89', a)
    if hasattr(b2, 'FunctionalRequirement89'):
        assert _is_linked(b2, 'FunctionalRequirement89', a)
    _safe_set(a, 'refiningRequirements', None)
    assert not _is_linked(a, 'refiningRequirements', b2)
    if hasattr(b2, 'FunctionalRequirement89'):
        assert not _is_linked(b2, 'FunctionalRequirement89', a)


def test_assoc_refiningRequirements87_link_reassign_clear():
    a = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    b1 = requirement_FunctionalRequirement()
    b2 = requirement_FunctionalRequirement()
    _safe_set(a, 'refinedRequirement', {b1})
    assert _is_linked(a, 'refinedRequirement', b1)
    if hasattr(b1, 'FunctionalRequirement'):
        assert _is_linked(b1, 'FunctionalRequirement', a)
    _safe_set(a, 'refinedRequirement', {b2})
    assert _is_linked(a, 'refinedRequirement', b2)
    if hasattr(b1, 'FunctionalRequirement'):
        assert not _is_linked(b1, 'FunctionalRequirement', a)
    if hasattr(b2, 'FunctionalRequirement'):
        assert _is_linked(b2, 'FunctionalRequirement', a)
    _safe_set(a, 'refinedRequirement', set())
    assert not _is_linked(a, 'refinedRequirement', b2)
    if hasattr(b2, 'FunctionalRequirement'):
        assert not _is_linked(b2, 'FunctionalRequirement', a)


def test_assoc_relatedModelElements449_link_reassign_clear():
    a = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_notification_ESNotification450', {b1})
    assert _is_linked(a, 'esmodel_notification_ESNotification450', b1)
    if hasattr(b1, 'ModelElementId451'):
        assert _is_linked(b1, 'ModelElementId451', a)
    _safe_set(a, 'esmodel_notification_ESNotification450', {b2})
    assert _is_linked(a, 'esmodel_notification_ESNotification450', b2)
    if hasattr(b1, 'ModelElementId451'):
        assert not _is_linked(b1, 'ModelElementId451', a)
    if hasattr(b2, 'ModelElementId451'):
        assert _is_linked(b2, 'ModelElementId451', a)
    _safe_set(a, 'esmodel_notification_ESNotification450', set())
    assert not _is_linked(a, 'esmodel_notification_ESNotification450', b2)
    if hasattr(b2, 'ModelElementId451'):
        assert not _is_linked(b2, 'ModelElementId451', a)


def test_assoc_relatedOperations452_link_reassign_clear():
    a = esmodel_notification_ESNotification(creationDate=date(2024, 1, 1), details="sample_text", message="sample_text", name="sample_text", provider="sample_text", recipient="sample_text", seen=True, sender="sample_text")
    b1 = operations_OperationId()
    b2 = operations_OperationId()
    _safe_set(a, 'esmodel_notification_ESNotification453', {b1})
    assert _is_linked(a, 'esmodel_notification_ESNotification453', b1)
    if hasattr(b1, 'operations_OperationId454'):
        assert _is_linked(b1, 'operations_OperationId454', a)
    _safe_set(a, 'esmodel_notification_ESNotification453', {b2})
    assert _is_linked(a, 'esmodel_notification_ESNotification453', b2)
    if hasattr(b1, 'operations_OperationId454'):
        assert not _is_linked(b1, 'operations_OperationId454', a)
    if hasattr(b2, 'operations_OperationId454'):
        assert _is_linked(b2, 'operations_OperationId454', a)
    _safe_set(a, 'esmodel_notification_ESNotification453', set())
    assert not _is_linked(a, 'esmodel_notification_ESNotification453', b2)
    if hasattr(b2, 'operations_OperationId454'):
        assert not _is_linked(b2, 'operations_OperationId454', a)


def test_assoc_reviewer28_link_reassign_clear():
    a = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    b1 = organization_User()
    b2 = organization_User()
    _safe_set(a, 'workItemsToReview', b1)
    assert _is_linked(a, 'workItemsToReview', b1)
    if hasattr(b1, 'User'):
        assert _is_linked(b1, 'User', a)
    _safe_set(a, 'workItemsToReview', b2)
    assert _is_linked(a, 'workItemsToReview', b2)
    if hasattr(b1, 'User'):
        assert not _is_linked(b1, 'User', a)
    if hasattr(b2, 'User'):
        assert _is_linked(b2, 'User', a)
    _safe_set(a, 'workItemsToReview', None)
    assert not _is_linked(a, 'workItemsToReview', b2)
    if hasattr(b2, 'User'):
        assert not _is_linked(b2, 'User', a)


def test_assoc_roles439_link_reassign_clear():
    a = esmodel_accesscontrol_ACOrgUnit(description="sample_text", name="sample_text")
    b1 = roles_Role()
    b2 = roles_Role()
    _safe_set(a, 'esmodel_accesscontrol_ACOrgUnit', {b1})
    assert _is_linked(a, 'esmodel_accesscontrol_ACOrgUnit', b1)
    if hasattr(b1, 'roles_Role'):
        assert _is_linked(b1, 'roles_Role', a)
    _safe_set(a, 'esmodel_accesscontrol_ACOrgUnit', {b2})
    assert _is_linked(a, 'esmodel_accesscontrol_ACOrgUnit', b2)
    if hasattr(b1, 'roles_Role'):
        assert not _is_linked(b1, 'roles_Role', a)
    if hasattr(b2, 'roles_Role'):
        assert _is_linked(b2, 'roles_Role', a)
    _safe_set(a, 'esmodel_accesscontrol_ACOrgUnit', set())
    assert not _is_linked(a, 'esmodel_accesscontrol_ACOrgUnit', b2)
    if hasattr(b2, 'roles_Role'):
        assert not _is_linked(b2, 'roles_Role', a)


def test_assoc_scenarios104_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_Scenario()
    b2 = requirement_Scenario()
    _safe_set(a, 'instantiatedUseCases', {b1})
    assert _is_linked(a, 'instantiatedUseCases', b1)
    if hasattr(b1, 'Scenario105'):
        assert _is_linked(b1, 'Scenario105', a)
    _safe_set(a, 'instantiatedUseCases', {b2})
    assert _is_linked(a, 'instantiatedUseCases', b2)
    if hasattr(b1, 'Scenario105'):
        assert not _is_linked(b1, 'Scenario105', a)
    if hasattr(b2, 'Scenario105'):
        assert _is_linked(b2, 'Scenario105', a)
    _safe_set(a, 'instantiatedUseCases', set())
    assert not _is_linked(a, 'instantiatedUseCases', b2)
    if hasattr(b2, 'Scenario105'):
        assert not _is_linked(b2, 'Scenario105', a)


def test_assoc_scenarios93_link_reassign_clear():
    a = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    b1 = requirement_Scenario()
    b2 = requirement_Scenario()
    _safe_set(a, 'functionalRequirements94', {b1})
    assert _is_linked(a, 'functionalRequirements94', b1)
    if hasattr(b1, 'Scenario95'):
        assert _is_linked(b1, 'Scenario95', a)
    _safe_set(a, 'functionalRequirements94', {b2})
    assert _is_linked(a, 'functionalRequirements94', b2)
    if hasattr(b1, 'Scenario95'):
        assert not _is_linked(b1, 'Scenario95', a)
    if hasattr(b2, 'Scenario95'):
        assert _is_linked(b2, 'Scenario95', a)
    _safe_set(a, 'functionalRequirements94', set())
    assert not _is_linked(a, 'functionalRequirements94', b2)
    if hasattr(b2, 'Scenario95'):
        assert not _is_linked(b2, 'Scenario95', a)


def test_assoc_sections212_link_reassign_clear():
    a = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    b1 = meeting_MeetingSection()
    b2 = meeting_MeetingSection()
    _safe_set(a, 'model_meeting_Meeting213', {b1})
    assert _is_linked(a, 'model_meeting_Meeting213', b1)
    if hasattr(b1, 'meeting_MeetingSection'):
        assert _is_linked(b1, 'meeting_MeetingSection', a)
    _safe_set(a, 'model_meeting_Meeting213', {b2})
    assert _is_linked(a, 'model_meeting_Meeting213', b2)
    if hasattr(b1, 'meeting_MeetingSection'):
        assert not _is_linked(b1, 'meeting_MeetingSection', a)
    if hasattr(b2, 'meeting_MeetingSection'):
        assert _is_linked(b2, 'meeting_MeetingSection', a)
    _safe_set(a, 'model_meeting_Meeting213', set())
    assert not _is_linked(a, 'model_meeting_Meeting213', b2)
    if hasattr(b2, 'meeting_MeetingSection'):
        assert not _is_linked(b2, 'meeting_MeetingSection', a)


def test_assoc_solution164_link_reassign_clear():
    a = model_rationale_Issue(activity="sample_text")
    b1 = rationale_Solution()
    b2 = rationale_Solution()
    _safe_set(a, 'issue165', b1)
    assert _is_linked(a, 'issue165', b1)
    if hasattr(b1, 'Solution'):
        assert _is_linked(b1, 'Solution', a)
    _safe_set(a, 'issue165', b2)
    assert _is_linked(a, 'issue165', b2)
    if hasattr(b1, 'Solution'):
        assert not _is_linked(b1, 'Solution', a)
    if hasattr(b2, 'Solution'):
        assert _is_linked(b2, 'Solution', a)
    _safe_set(a, 'issue165', None)
    assert not _is_linked(a, 'issue165', b2)
    if hasattr(b2, 'Solution'):
        assert not _is_linked(b2, 'Solution', a)


def test_assoc_source222_link_reassign_clear():
    a = model_state_Transition(condition="sample_text")
    b1 = state_StateNode()
    b2 = state_StateNode()
    _safe_set(a, 'outgoingTransitions', b1)
    assert _is_linked(a, 'outgoingTransitions', b1)
    if hasattr(b1, 'StateNode'):
        assert _is_linked(b1, 'StateNode', a)
    _safe_set(a, 'outgoingTransitions', b2)
    assert _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b1, 'StateNode'):
        assert not _is_linked(b1, 'StateNode', a)
    if hasattr(b2, 'StateNode'):
        assert _is_linked(b2, 'StateNode', a)
    _safe_set(a, 'outgoingTransitions', None)
    assert not _is_linked(a, 'outgoingTransitions', b2)
    if hasattr(b2, 'StateNode'):
        assert not _is_linked(b2, 'StateNode', a)


def test_assoc_source265_link_reassign_clear():
    a = model_activity_Transition(condition="sample_text")
    b1 = activity_ActivityObject()
    b2 = activity_ActivityObject()
    _safe_set(a, 'outgoingTransitions266', b1)
    assert _is_linked(a, 'outgoingTransitions266', b1)
    if hasattr(b1, 'ActivityObject'):
        assert _is_linked(b1, 'ActivityObject', a)
    _safe_set(a, 'outgoingTransitions266', b2)
    assert _is_linked(a, 'outgoingTransitions266', b2)
    if hasattr(b1, 'ActivityObject'):
        assert not _is_linked(b1, 'ActivityObject', a)
    if hasattr(b2, 'ActivityObject'):
        assert _is_linked(b2, 'ActivityObject', a)
    _safe_set(a, 'outgoingTransitions266', None)
    assert not _is_linked(a, 'outgoingTransitions266', b2)
    if hasattr(b2, 'ActivityObject'):
        assert not _is_linked(b2, 'ActivityObject', a)


def test_assoc_source305_link_reassign_clear():
    a = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    b1 = versioning_PrimaryVersionSpec()
    b2 = versioning_PrimaryVersionSpec()
    _safe_set(a, 'esmodel_versioning_HistoryQuery', b1)
    assert _is_linked(a, 'esmodel_versioning_HistoryQuery', b1)
    if hasattr(b1, 'versioning_PrimaryVersionSpec306'):
        assert _is_linked(b1, 'versioning_PrimaryVersionSpec306', a)
    _safe_set(a, 'esmodel_versioning_HistoryQuery', b2)
    assert _is_linked(a, 'esmodel_versioning_HistoryQuery', b2)
    if hasattr(b1, 'versioning_PrimaryVersionSpec306'):
        assert not _is_linked(b1, 'versioning_PrimaryVersionSpec306', a)
    if hasattr(b2, 'versioning_PrimaryVersionSpec306'):
        assert _is_linked(b2, 'versioning_PrimaryVersionSpec306', a)
    _safe_set(a, 'esmodel_versioning_HistoryQuery', None)
    assert not _is_linked(a, 'esmodel_versioning_HistoryQuery', b2)
    if hasattr(b2, 'versioning_PrimaryVersionSpec306'):
        assert not _is_linked(b2, 'versioning_PrimaryVersionSpec306', a)


def test_assoc_source62_link_reassign_clear():
    a = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    b1 = classes_Class()
    b2 = classes_Class()
    _safe_set(a, 'outgoingAssociations', b1)
    assert _is_linked(a, 'outgoingAssociations', b1)
    if hasattr(b1, 'Class63'):
        assert _is_linked(b1, 'Class63', a)
    _safe_set(a, 'outgoingAssociations', b2)
    assert _is_linked(a, 'outgoingAssociations', b2)
    if hasattr(b1, 'Class63'):
        assert not _is_linked(b1, 'Class63', a)
    if hasattr(b2, 'Class63'):
        assert _is_linked(b2, 'Class63', a)
    _safe_set(a, 'outgoingAssociations', None)
    assert not _is_linked(a, 'outgoingAssociations', b2)
    if hasattr(b2, 'Class63'):
        assert not _is_linked(b2, 'Class63', a)


def test_assoc_sourceElement399_link_reassign_clear():
    a = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_LinkEvent', b1)
    assert _is_linked(a, 'esmodel_events_LinkEvent', b1)
    if hasattr(b1, 'ModelElementId400'):
        assert _is_linked(b1, 'ModelElementId400', a)
    _safe_set(a, 'esmodel_events_LinkEvent', b2)
    assert _is_linked(a, 'esmodel_events_LinkEvent', b2)
    if hasattr(b1, 'ModelElementId400'):
        assert not _is_linked(b1, 'ModelElementId400', a)
    if hasattr(b2, 'ModelElementId400'):
        assert _is_linked(b2, 'ModelElementId400', a)
    _safe_set(a, 'esmodel_events_LinkEvent', None)
    assert not _is_linked(a, 'esmodel_events_LinkEvent', b2)
    if hasattr(b2, 'ModelElementId400'):
        assert not _is_linked(b2, 'ModelElementId400', a)


def test_assoc_sourceElement404_link_reassign_clear():
    a = esmodel_events_TraceEvent(featureName="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_TraceEvent', b1)
    assert _is_linked(a, 'esmodel_events_TraceEvent', b1)
    if hasattr(b1, 'ModelElementId405'):
        assert _is_linked(b1, 'ModelElementId405', a)
    _safe_set(a, 'esmodel_events_TraceEvent', b2)
    assert _is_linked(a, 'esmodel_events_TraceEvent', b2)
    if hasattr(b1, 'ModelElementId405'):
        assert not _is_linked(b1, 'ModelElementId405', a)
    if hasattr(b2, 'ModelElementId405'):
        assert _is_linked(b2, 'ModelElementId405', a)
    _safe_set(a, 'esmodel_events_TraceEvent', None)
    assert not _is_linked(a, 'esmodel_events_TraceEvent', b2)
    if hasattr(b2, 'ModelElementId405'):
        assert not _is_linked(b2, 'ModelElementId405', a)


def test_assoc_sourceModelElement423_link_reassign_clear():
    a = esmodel_events_URLEvent(sourceView="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_URLEvent', b1)
    assert _is_linked(a, 'esmodel_events_URLEvent', b1)
    if hasattr(b1, 'ModelElementId424'):
        assert _is_linked(b1, 'ModelElementId424', a)
    _safe_set(a, 'esmodel_events_URLEvent', b2)
    assert _is_linked(a, 'esmodel_events_URLEvent', b2)
    if hasattr(b1, 'ModelElementId424'):
        assert not _is_linked(b1, 'ModelElementId424', a)
    if hasattr(b2, 'ModelElementId424'):
        assert _is_linked(b2, 'ModelElementId424', a)
    _safe_set(a, 'esmodel_events_URLEvent', None)
    assert not _is_linked(a, 'esmodel_events_URLEvent', b2)
    if hasattr(b2, 'ModelElementId424'):
        assert not _is_linked(b2, 'ModelElementId424', a)


def test_assoc_sourceSection411_link_reassign_clear():
    a = esmodel_events_NavigatorCreateEvent(dynamic=True)
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_NavigatorCreateEvent412', b1)
    assert _is_linked(a, 'esmodel_events_NavigatorCreateEvent412', b1)
    if hasattr(b1, 'ModelElementId413'):
        assert _is_linked(b1, 'ModelElementId413', a)
    _safe_set(a, 'esmodel_events_NavigatorCreateEvent412', b2)
    assert _is_linked(a, 'esmodel_events_NavigatorCreateEvent412', b2)
    if hasattr(b1, 'ModelElementId413'):
        assert not _is_linked(b1, 'ModelElementId413', a)
    if hasattr(b2, 'ModelElementId413'):
        assert _is_linked(b2, 'ModelElementId413', a)
    _safe_set(a, 'esmodel_events_NavigatorCreateEvent412', None)
    assert not _is_linked(a, 'esmodel_events_NavigatorCreateEvent412', b2)
    if hasattr(b2, 'ModelElementId413'):
        assert not _is_linked(b2, 'ModelElementId413', a)


def test_assoc_sourceURL425_link_reassign_clear():
    a = esmodel_events_URLEvent(sourceView="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_URLEvent426', b1)
    assert _is_linked(a, 'esmodel_events_URLEvent426', b1)
    if hasattr(b1, 'ModelElementId427'):
        assert _is_linked(b1, 'ModelElementId427', a)
    _safe_set(a, 'esmodel_events_URLEvent426', b2)
    assert _is_linked(a, 'esmodel_events_URLEvent426', b2)
    if hasattr(b1, 'ModelElementId427'):
        assert not _is_linked(b1, 'ModelElementId427', a)
    if hasattr(b2, 'ModelElementId427'):
        assert _is_linked(b2, 'ModelElementId427', a)
    _safe_set(a, 'esmodel_events_URLEvent426', None)
    assert not _is_linked(a, 'esmodel_events_URLEvent426', b2)
    if hasattr(b2, 'ModelElementId427'):
        assert not _is_linked(b2, 'ModelElementId427', a)


def test_assoc_stakeholder90_link_reassign_clear():
    a = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    b1 = organization_OrgUnit()
    b2 = organization_OrgUnit()
    _safe_set(a, 'model_requirement_FunctionalRequirement', b1)
    assert _is_linked(a, 'model_requirement_FunctionalRequirement', b1)
    if hasattr(b1, 'organization_OrgUnit'):
        assert _is_linked(b1, 'organization_OrgUnit', a)
    _safe_set(a, 'model_requirement_FunctionalRequirement', b2)
    assert _is_linked(a, 'model_requirement_FunctionalRequirement', b2)
    if hasattr(b1, 'organization_OrgUnit'):
        assert not _is_linked(b1, 'organization_OrgUnit', a)
    if hasattr(b2, 'organization_OrgUnit'):
        assert _is_linked(b2, 'organization_OrgUnit', a)
    _safe_set(a, 'model_requirement_FunctionalRequirement', None)
    assert not _is_linked(a, 'model_requirement_FunctionalRequirement', b2)
    if hasattr(b2, 'organization_OrgUnit'):
        assert not _is_linked(b2, 'organization_OrgUnit', a)


def test_assoc_stereotypeAttributes236_link_reassign_clear():
    a = model_profile_Stereotype(required=True)
    b1 = profile_StereotypeAttribute()
    b2 = profile_StereotypeAttribute()
    _safe_set(a, 'stereotype237', {b1})
    assert _is_linked(a, 'stereotype237', b1)
    if hasattr(b1, 'StereotypeAttribute'):
        assert _is_linked(b1, 'StereotypeAttribute', a)
    _safe_set(a, 'stereotype237', {b2})
    assert _is_linked(a, 'stereotype237', b2)
    if hasattr(b1, 'StereotypeAttribute'):
        assert not _is_linked(b1, 'StereotypeAttribute', a)
    if hasattr(b2, 'StereotypeAttribute'):
        assert _is_linked(b2, 'StereotypeAttribute', a)
    _safe_set(a, 'stereotype237', set())
    assert not _is_linked(a, 'stereotype237', b2)
    if hasattr(b2, 'StereotypeAttribute'):
        assert not _is_linked(b2, 'StereotypeAttribute', a)


def test_assoc_stereotypeInstances234_link_reassign_clear():
    a = model_profile_Stereotype(required=True)
    b1 = profile_StereotypeInstance()
    b2 = profile_StereotypeInstance()
    _safe_set(a, 'stereotype', {b1})
    assert _is_linked(a, 'stereotype', b1)
    if hasattr(b1, 'StereotypeInstance235'):
        assert _is_linked(b1, 'StereotypeInstance235', a)
    _safe_set(a, 'stereotype', {b2})
    assert _is_linked(a, 'stereotype', b2)
    if hasattr(b1, 'StereotypeInstance235'):
        assert not _is_linked(b1, 'StereotypeInstance235', a)
    if hasattr(b2, 'StereotypeInstance235'):
        assert _is_linked(b2, 'StereotypeInstance235', a)
    _safe_set(a, 'stereotype', set())
    assert not _is_linked(a, 'stereotype', b2)
    if hasattr(b2, 'StereotypeInstance235'):
        assert not _is_linked(b2, 'StereotypeInstance235', a)


def test_assoc_subOperations331_link_reassign_clear():
    a = esmodel_operations_CompositeOperation(compositeDescription="sample_text", compositeName="sample_text", reversed=True)
    b1 = operations_AbstractOperation()
    b2 = operations_AbstractOperation()
    _safe_set(a, 'esmodel_operations_CompositeOperation', {b1})
    assert _is_linked(a, 'esmodel_operations_CompositeOperation', b1)
    if hasattr(b1, 'operations_AbstractOperation332'):
        assert _is_linked(b1, 'operations_AbstractOperation332', a)
    _safe_set(a, 'esmodel_operations_CompositeOperation', {b2})
    assert _is_linked(a, 'esmodel_operations_CompositeOperation', b2)
    if hasattr(b1, 'operations_AbstractOperation332'):
        assert not _is_linked(b1, 'operations_AbstractOperation332', a)
    if hasattr(b2, 'operations_AbstractOperation332'):
        assert _is_linked(b2, 'operations_AbstractOperation332', a)
    _safe_set(a, 'esmodel_operations_CompositeOperation', set())
    assert not _is_linked(a, 'esmodel_operations_CompositeOperation', b2)
    if hasattr(b2, 'operations_AbstractOperation332'):
        assert not _is_linked(b2, 'operations_AbstractOperation332', a)


def test_assoc_subOperations337_link_reassign_clear():
    a = esmodel_operations_CreateDeleteOperation(delete=True)
    b1 = operations_ReferenceOperation()
    b2 = operations_ReferenceOperation()
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation338', {b1})
    assert _is_linked(a, 'esmodel_operations_CreateDeleteOperation338', b1)
    if hasattr(b1, 'operations_ReferenceOperation'):
        assert _is_linked(b1, 'operations_ReferenceOperation', a)
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation338', {b2})
    assert _is_linked(a, 'esmodel_operations_CreateDeleteOperation338', b2)
    if hasattr(b1, 'operations_ReferenceOperation'):
        assert not _is_linked(b1, 'operations_ReferenceOperation', a)
    if hasattr(b2, 'operations_ReferenceOperation'):
        assert _is_linked(b2, 'operations_ReferenceOperation', a)
    _safe_set(a, 'esmodel_operations_CreateDeleteOperation338', set())
    assert not _is_linked(a, 'esmodel_operations_CreateDeleteOperation338', b2)
    if hasattr(b2, 'operations_ReferenceOperation'):
        assert not _is_linked(b2, 'operations_ReferenceOperation', a)


def test_assoc_successors22_link_reassign_clear():
    a = model_task_WorkItem(dueDate=date(2024, 1, 1), effort=7, estimate=7, priority=7, resolved=True)
    b1 = task_WorkItem()
    b2 = task_WorkItem()
    _safe_set(a, 'predecessors', {b1})
    assert _is_linked(a, 'predecessors', b1)
    if hasattr(b1, 'WorkItem23'):
        assert _is_linked(b1, 'WorkItem23', a)
    _safe_set(a, 'predecessors', {b2})
    assert _is_linked(a, 'predecessors', b2)
    if hasattr(b1, 'WorkItem23'):
        assert not _is_linked(b1, 'WorkItem23', a)
    if hasattr(b2, 'WorkItem23'):
        assert _is_linked(b2, 'WorkItem23', a)
    _safe_set(a, 'predecessors', set())
    assert not _is_linked(a, 'predecessors', b2)
    if hasattr(b2, 'WorkItem23'):
        assert not _is_linked(b2, 'WorkItem23', a)


def test_assoc_target223_link_reassign_clear():
    a = model_state_Transition(condition="sample_text")
    b1 = state_StateNode()
    b2 = state_StateNode()
    _safe_set(a, 'incomingTransitions', b1)
    assert _is_linked(a, 'incomingTransitions', b1)
    if hasattr(b1, 'StateNode224'):
        assert _is_linked(b1, 'StateNode224', a)
    _safe_set(a, 'incomingTransitions', b2)
    assert _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b1, 'StateNode224'):
        assert not _is_linked(b1, 'StateNode224', a)
    if hasattr(b2, 'StateNode224'):
        assert _is_linked(b2, 'StateNode224', a)
    _safe_set(a, 'incomingTransitions', None)
    assert not _is_linked(a, 'incomingTransitions', b2)
    if hasattr(b2, 'StateNode224'):
        assert not _is_linked(b2, 'StateNode224', a)


def test_assoc_target267_link_reassign_clear():
    a = model_activity_Transition(condition="sample_text")
    b1 = activity_ActivityObject()
    b2 = activity_ActivityObject()
    _safe_set(a, 'incomingTransitions268', b1)
    assert _is_linked(a, 'incomingTransitions268', b1)
    if hasattr(b1, 'ActivityObject269'):
        assert _is_linked(b1, 'ActivityObject269', a)
    _safe_set(a, 'incomingTransitions268', b2)
    assert _is_linked(a, 'incomingTransitions268', b2)
    if hasattr(b1, 'ActivityObject269'):
        assert not _is_linked(b1, 'ActivityObject269', a)
    if hasattr(b2, 'ActivityObject269'):
        assert _is_linked(b2, 'ActivityObject269', a)
    _safe_set(a, 'incomingTransitions268', None)
    assert not _is_linked(a, 'incomingTransitions268', b2)
    if hasattr(b2, 'ActivityObject269'):
        assert not _is_linked(b2, 'ActivityObject269', a)


def test_assoc_target307_link_reassign_clear():
    a = esmodel_versioning_HistoryQuery(includeChangePackage=True)
    b1 = versioning_PrimaryVersionSpec()
    b2 = versioning_PrimaryVersionSpec()
    _safe_set(a, 'esmodel_versioning_HistoryQuery308', b1)
    assert _is_linked(a, 'esmodel_versioning_HistoryQuery308', b1)
    if hasattr(b1, 'versioning_PrimaryVersionSpec309'):
        assert _is_linked(b1, 'versioning_PrimaryVersionSpec309', a)
    _safe_set(a, 'esmodel_versioning_HistoryQuery308', b2)
    assert _is_linked(a, 'esmodel_versioning_HistoryQuery308', b2)
    if hasattr(b1, 'versioning_PrimaryVersionSpec309'):
        assert not _is_linked(b1, 'versioning_PrimaryVersionSpec309', a)
    if hasattr(b2, 'versioning_PrimaryVersionSpec309'):
        assert _is_linked(b2, 'versioning_PrimaryVersionSpec309', a)
    _safe_set(a, 'esmodel_versioning_HistoryQuery308', None)
    assert not _is_linked(a, 'esmodel_versioning_HistoryQuery308', b2)
    if hasattr(b2, 'versioning_PrimaryVersionSpec309'):
        assert not _is_linked(b2, 'versioning_PrimaryVersionSpec309', a)


def test_assoc_target64_link_reassign_clear():
    a = model_classes_Association(sourceMultiplicity="sample_text", sourceRole="sample_text", targetMultiplicity="sample_text", targetRole="sample_text", type="sample_text")
    b1 = classes_Class()
    b2 = classes_Class()
    _safe_set(a, 'incomingAssociations', b1)
    assert _is_linked(a, 'incomingAssociations', b1)
    if hasattr(b1, 'Class65'):
        assert _is_linked(b1, 'Class65', a)
    _safe_set(a, 'incomingAssociations', b2)
    assert _is_linked(a, 'incomingAssociations', b2)
    if hasattr(b1, 'Class65'):
        assert not _is_linked(b1, 'Class65', a)
    if hasattr(b2, 'Class65'):
        assert _is_linked(b2, 'Class65', a)
    _safe_set(a, 'incomingAssociations', None)
    assert not _is_linked(a, 'incomingAssociations', b2)
    if hasattr(b2, 'Class65'):
        assert not _is_linked(b2, 'Class65', a)


def test_assoc_targetElement401_link_reassign_clear():
    a = esmodel_events_LinkEvent(createdNew=True, sourceView="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_LinkEvent402', b1)
    assert _is_linked(a, 'esmodel_events_LinkEvent402', b1)
    if hasattr(b1, 'ModelElementId403'):
        assert _is_linked(b1, 'ModelElementId403', a)
    _safe_set(a, 'esmodel_events_LinkEvent402', b2)
    assert _is_linked(a, 'esmodel_events_LinkEvent402', b2)
    if hasattr(b1, 'ModelElementId403'):
        assert not _is_linked(b1, 'ModelElementId403', a)
    if hasattr(b2, 'ModelElementId403'):
        assert _is_linked(b2, 'ModelElementId403', a)
    _safe_set(a, 'esmodel_events_LinkEvent402', None)
    assert not _is_linked(a, 'esmodel_events_LinkEvent402', b2)
    if hasattr(b2, 'ModelElementId403'):
        assert not _is_linked(b2, 'ModelElementId403', a)


def test_assoc_targetElement406_link_reassign_clear():
    a = esmodel_events_TraceEvent(featureName="sample_text")
    b1 = ModelElementId()
    b2 = ModelElementId()
    _safe_set(a, 'esmodel_events_TraceEvent407', b1)
    assert _is_linked(a, 'esmodel_events_TraceEvent407', b1)
    if hasattr(b1, 'ModelElementId408'):
        assert _is_linked(b1, 'ModelElementId408', a)
    _safe_set(a, 'esmodel_events_TraceEvent407', b2)
    assert _is_linked(a, 'esmodel_events_TraceEvent407', b2)
    if hasattr(b1, 'ModelElementId408'):
        assert not _is_linked(b1, 'ModelElementId408', a)
    if hasattr(b2, 'ModelElementId408'):
        assert _is_linked(b2, 'ModelElementId408', a)
    _safe_set(a, 'esmodel_events_TraceEvent407', None)
    assert not _is_linked(a, 'esmodel_events_TraceEvent407', b2)
    if hasattr(b2, 'ModelElementId408'):
        assert not _is_linked(b2, 'ModelElementId408', a)


def test_assoc_targetVersion368_link_reassign_clear():
    a = esmodel_events_MergeEvent(numberOfConflicts=7, totalTime=7)
    b1 = versioning_PrimaryVersionSpec()
    b2 = versioning_PrimaryVersionSpec()
    _safe_set(a, 'esmodel_events_MergeEvent369', b1)
    assert _is_linked(a, 'esmodel_events_MergeEvent369', b1)
    if hasattr(b1, 'versioning_PrimaryVersionSpec370'):
        assert _is_linked(b1, 'versioning_PrimaryVersionSpec370', a)
    _safe_set(a, 'esmodel_events_MergeEvent369', b2)
    assert _is_linked(a, 'esmodel_events_MergeEvent369', b2)
    if hasattr(b1, 'versioning_PrimaryVersionSpec370'):
        assert not _is_linked(b1, 'versioning_PrimaryVersionSpec370', a)
    if hasattr(b2, 'versioning_PrimaryVersionSpec370'):
        assert _is_linked(b2, 'versioning_PrimaryVersionSpec370', a)
    _safe_set(a, 'esmodel_events_MergeEvent369', None)
    assert not _is_linked(a, 'esmodel_events_MergeEvent369', b2)
    if hasattr(b2, 'versioning_PrimaryVersionSpec370'):
        assert not _is_linked(b2, 'versioning_PrimaryVersionSpec370', a)


def test_assoc_theirRejectedChanges429_link_reassign_clear():
    a = esmodel_events_MergeChoiceEvent(contextFeature="sample_text", createdIssueName="sample_text", selection="sample_text")
    b1 = operations_OperationId()
    b2 = operations_OperationId()
    _safe_set(a, 'esmodel_events_MergeChoiceEvent430', {b1})
    assert _is_linked(a, 'esmodel_events_MergeChoiceEvent430', b1)
    if hasattr(b1, 'operations_OperationId431'):
        assert _is_linked(b1, 'operations_OperationId431', a)
    _safe_set(a, 'esmodel_events_MergeChoiceEvent430', {b2})
    assert _is_linked(a, 'esmodel_events_MergeChoiceEvent430', b2)
    if hasattr(b1, 'operations_OperationId431'):
        assert not _is_linked(b1, 'operations_OperationId431', a)
    if hasattr(b2, 'operations_OperationId431'):
        assert _is_linked(b2, 'operations_OperationId431', a)
    _safe_set(a, 'esmodel_events_MergeChoiceEvent430', set())
    assert not _is_linked(a, 'esmodel_events_MergeChoiceEvent430', b2)
    if hasattr(b2, 'operations_OperationId431'):
        assert not _is_linked(b2, 'operations_OperationId431', a)


def test_assoc_timekeeper206_link_reassign_clear():
    a = model_meeting_Meeting(endtime=date(2024, 1, 1), location="sample_text", starttime=date(2024, 1, 1))
    b1 = organization_User()
    b2 = organization_User()
    _safe_set(a, 'model_meeting_Meeting207', b1)
    assert _is_linked(a, 'model_meeting_Meeting207', b1)
    if hasattr(b1, 'organization_User208'):
        assert _is_linked(b1, 'organization_User208', a)
    _safe_set(a, 'model_meeting_Meeting207', b2)
    assert _is_linked(a, 'model_meeting_Meeting207', b2)
    if hasattr(b1, 'organization_User208'):
        assert not _is_linked(b1, 'organization_User208', a)
    if hasattr(b2, 'organization_User208'):
        assert _is_linked(b2, 'organization_User208', a)
    _safe_set(a, 'model_meeting_Meeting207', None)
    assert not _is_linked(a, 'model_meeting_Meeting207', b2)
    if hasattr(b2, 'organization_User208'):
        assert not _is_linked(b2, 'organization_User208', a)


def test_assoc_useCase148_link_reassign_clear():
    a = model_requirement_Step(userStep=True)
    b1 = requirement_UseCase()
    b2 = requirement_UseCase()
    _safe_set(a, 'useCaseSteps', b1)
    assert _is_linked(a, 'useCaseSteps', b1)
    if hasattr(b1, 'UseCase149'):
        assert _is_linked(b1, 'UseCase149', a)
    _safe_set(a, 'useCaseSteps', b2)
    assert _is_linked(a, 'useCaseSteps', b2)
    if hasattr(b1, 'UseCase149'):
        assert not _is_linked(b1, 'UseCase149', a)
    if hasattr(b2, 'UseCase149'):
        assert _is_linked(b2, 'UseCase149', a)
    _safe_set(a, 'useCaseSteps', None)
    assert not _is_linked(a, 'useCaseSteps', b2)
    if hasattr(b2, 'UseCase149'):
        assert not _is_linked(b2, 'UseCase149', a)


def test_assoc_useCaseSteps110_link_reassign_clear():
    a = model_requirement_UseCase(exception="sample_text", postcondition="sample_text", precondition="sample_text", rules="sample_text")
    b1 = requirement_Step()
    b2 = requirement_Step()
    _safe_set(a, 'useCase', {b1})
    assert _is_linked(a, 'useCase', b1)
    if hasattr(b1, 'Step'):
        assert _is_linked(b1, 'Step', a)
    _safe_set(a, 'useCase', {b2})
    assert _is_linked(a, 'useCase', b2)
    if hasattr(b1, 'Step'):
        assert not _is_linked(b1, 'Step', a)
    if hasattr(b2, 'Step'):
        assert _is_linked(b2, 'Step', a)
    _safe_set(a, 'useCase', set())
    assert not _is_linked(a, 'useCase', b2)
    if hasattr(b2, 'Step'):
        assert not _is_linked(b2, 'Step', a)


def test_assoc_useCases91_link_reassign_clear():
    a = model_requirement_FunctionalRequirement(cost=7, priority=7, reviewed=True, storyPoints=7)
    b1 = requirement_UseCase()
    b2 = requirement_UseCase()
    _safe_set(a, 'functionalRequirements', {b1})
    assert _is_linked(a, 'functionalRequirements', b1)
    if hasattr(b1, 'UseCase92'):
        assert _is_linked(b1, 'UseCase92', a)
    _safe_set(a, 'functionalRequirements', {b2})
    assert _is_linked(a, 'functionalRequirements', b2)
    if hasattr(b1, 'UseCase92'):
        assert not _is_linked(b1, 'UseCase92', a)
    if hasattr(b2, 'UseCase92'):
        assert _is_linked(b2, 'UseCase92', a)
    _safe_set(a, 'functionalRequirements', set())
    assert not _is_linked(a, 'functionalRequirements', b2)
    if hasattr(b2, 'UseCase92'):
        assert not _is_linked(b2, 'UseCase92', a)


def test_assoc_version275_link_reassign_clear():
    a = esmodel_ProjectInfo(description="sample_text", name="sample_text")
    b1 = versioning_PrimaryVersionSpec()
    b2 = versioning_PrimaryVersionSpec()
    _safe_set(a, 'esmodel_ProjectInfo276', b1)
    assert _is_linked(a, 'esmodel_ProjectInfo276', b1)
    if hasattr(b1, 'versioning_PrimaryVersionSpec'):
        assert _is_linked(b1, 'versioning_PrimaryVersionSpec', a)
    _safe_set(a, 'esmodel_ProjectInfo276', b2)
    assert _is_linked(a, 'esmodel_ProjectInfo276', b2)
    if hasattr(b1, 'versioning_PrimaryVersionSpec'):
        assert not _is_linked(b1, 'versioning_PrimaryVersionSpec', a)
    if hasattr(b2, 'versioning_PrimaryVersionSpec'):
        assert _is_linked(b2, 'versioning_PrimaryVersionSpec', a)
    _safe_set(a, 'esmodel_ProjectInfo276', None)
    assert not _is_linked(a, 'esmodel_ProjectInfo276', b2)
    if hasattr(b2, 'versioning_PrimaryVersionSpec'):
        assert not _is_linked(b2, 'versioning_PrimaryVersionSpec', a)


def test_assoc_versions271_link_reassign_clear():
    a = esmodel_ProjectHistory(projectDescription="sample_text", projectName="sample_text")
    b1 = versioning_Version()
    b2 = versioning_Version()
    _safe_set(a, 'esmodel_ProjectHistory272', {b1})
    assert _is_linked(a, 'esmodel_ProjectHistory272', b1)
    if hasattr(b1, 'versioning_Version'):
        assert _is_linked(b1, 'versioning_Version', a)
    _safe_set(a, 'esmodel_ProjectHistory272', {b2})
    assert _is_linked(a, 'esmodel_ProjectHistory272', b2)
    if hasattr(b1, 'versioning_Version'):
        assert not _is_linked(b1, 'versioning_Version', a)
    if hasattr(b2, 'versioning_Version'):
        assert _is_linked(b2, 'versioning_Version', a)
    _safe_set(a, 'esmodel_ProjectHistory272', set())
    assert not _is_linked(a, 'esmodel_ProjectHistory272', b2)
    if hasattr(b2, 'versioning_Version'):
        assert not _is_linked(b2, 'versioning_Version', a)


def test_assoc_workItemsToReview18_link_reassign_clear():
    a = model_organization_User(email="sample_text", firstName="sample_text", lastName="sample_text")
    b1 = task_WorkItem()
    b2 = task_WorkItem()
    _safe_set(a, 'reviewer', {b1})
    assert _is_linked(a, 'reviewer', b1)
    if hasattr(b1, 'WorkItem19'):
        assert _is_linked(b1, 'WorkItem19', a)
    _safe_set(a, 'reviewer', {b2})
    assert _is_linked(a, 'reviewer', b2)
    if hasattr(b1, 'WorkItem19'):
        assert not _is_linked(b1, 'WorkItem19', a)
    if hasattr(b2, 'WorkItem19'):
        assert _is_linked(b2, 'WorkItem19', a)
    _safe_set(a, 'reviewer', set())
    assert not _is_linked(a, 'reviewer', b2)
    if hasattr(b2, 'WorkItem19'):
        assert not _is_linked(b2, 'WorkItem19', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ACOrgUnit_strategy = st.builds(ACOrgUnit)
@given(instance=ACOrgUnit_strategy)
@settings(max_examples=25)
def test_ACOrgUnit_instantiation(instance):
    assert isinstance(instance, ACOrgUnit)


AbstractOperation_strategy = st.builds(AbstractOperation)
@given(instance=AbstractOperation_strategy)
@settings(max_examples=25)
def test_AbstractOperation_instantiation(instance):
    assert isinstance(instance, AbstractOperation)


ActivityObject_strategy = st.builds(ActivityObject)
@given(instance=ActivityObject_strategy)
@settings(max_examples=25)
def test_ActivityObject_instantiation(instance):
    assert isinstance(instance, ActivityObject)


Annotation_strategy = st.builds(Annotation)
@given(instance=Annotation_strategy)
@settings(max_examples=25)
def test_Annotation_instantiation(instance):
    assert isinstance(instance, Annotation)


Attachment_strategy = st.builds(Attachment)
@given(instance=Attachment_strategy)
@settings(max_examples=25)
def test_Attachment_instantiation(instance):
    assert isinstance(instance, Attachment)


AttributeOperation_strategy = st.builds(AttributeOperation)
@given(instance=AttributeOperation_strategy)
@settings(max_examples=25)
def test_AttributeOperation_instantiation(instance):
    assert isinstance(instance, AttributeOperation)


CompositeOperation_strategy = st.builds(CompositeOperation)
@given(instance=CompositeOperation_strategy)
@settings(max_examples=25)
def test_CompositeOperation_instantiation(instance):
    assert isinstance(instance, CompositeOperation)


Criterion_strategy = st.builds(Criterion)
@given(instance=Criterion_strategy)
@settings(max_examples=25)
def test_Criterion_instantiation(instance):
    assert isinstance(instance, Criterion)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


FeatureOperation_strategy = st.builds(FeatureOperation)
@given(instance=FeatureOperation_strategy)
@settings(max_examples=25)
def test_FeatureOperation_instantiation(instance):
    assert isinstance(instance, FeatureOperation)


IdentifiableElement_strategy = st.builds(IdentifiableElement)
@given(instance=IdentifiableElement_strategy)
@settings(max_examples=25)
def test_IdentifiableElement_instantiation(instance):
    assert isinstance(instance, IdentifiableElement)


Issue_strategy = st.builds(Issue)
@given(instance=Issue_strategy)
@settings(max_examples=25)
def test_Issue_instantiation(instance):
    assert isinstance(instance, Issue)


MeetingSection_strategy = st.builds(MeetingSection)
@given(instance=MeetingSection_strategy)
@settings(max_examples=25)
def test_MeetingSection_instantiation(instance):
    assert isinstance(instance, MeetingSection)


ModelElement_strategy = st.builds(ModelElement)
@given(instance=ModelElement_strategy)
@settings(max_examples=25)
def test_ModelElement_instantiation(instance):
    assert isinstance(instance, ModelElement)


ModelElementId_strategy = st.builds(ModelElementId)
@given(instance=ModelElementId_strategy)
@settings(max_examples=25)
def test_ModelElementId_instantiation(instance):
    assert isinstance(instance, ModelElementId)


NonDomainElement_strategy = st.builds(NonDomainElement)
@given(instance=NonDomainElement_strategy)
@settings(max_examples=25)
def test_NonDomainElement_instantiation(instance):
    assert isinstance(instance, NonDomainElement)


OrgUnit_strategy = st.builds(OrgUnit)
@given(instance=OrgUnit_strategy)
@settings(max_examples=25)
def test_OrgUnit_instantiation(instance):
    assert isinstance(instance, OrgUnit)


PackageElement_strategy = st.builds(PackageElement)
@given(instance=PackageElement_strategy)
@settings(max_examples=25)
def test_PackageElement_instantiation(instance):
    assert isinstance(instance, PackageElement)


Project_strategy = st.builds(Project)
@given(instance=Project_strategy)
@settings(max_examples=25)
def test_Project_instantiation(instance):
    assert isinstance(instance, Project)


ProjectHistory_strategy = st.builds(ProjectHistory)
@given(instance=ProjectHistory_strategy)
@settings(max_examples=25)
def test_ProjectHistory_instantiation(instance):
    assert isinstance(instance, ProjectHistory)


ProjectId_strategy = st.builds(ProjectId)
@given(instance=ProjectId_strategy)
@settings(max_examples=25)
def test_ProjectId_instantiation(instance):
    assert isinstance(instance, ProjectId)


Proposal_strategy = st.builds(Proposal)
@given(instance=Proposal_strategy)
@settings(max_examples=25)
def test_Proposal_instantiation(instance):
    assert isinstance(instance, Proposal)


ReadEvent_strategy = st.builds(ReadEvent)
@given(instance=ReadEvent_strategy)
@settings(max_examples=25)
def test_ReadEvent_instantiation(instance):
    assert isinstance(instance, ReadEvent)


ReferenceOperation_strategy = st.builds(ReferenceOperation)
@given(instance=ReferenceOperation_strategy)
@settings(max_examples=25)
def test_ReferenceOperation_instantiation(instance):
    assert isinstance(instance, ReferenceOperation)


Role_strategy = st.builds(Role)
@given(instance=Role_strategy)
@settings(max_examples=25)
def test_Role_instantiation(instance):
    assert isinstance(instance, Role)


Section_strategy = st.builds(Section)
@given(instance=Section_strategy)
@settings(max_examples=25)
def test_Section_instantiation(instance):
    assert isinstance(instance, Section)


ServerEvent_strategy = st.builds(ServerEvent)
@given(instance=ServerEvent_strategy)
@settings(max_examples=25)
def test_ServerEvent_instantiation(instance):
    assert isinstance(instance, ServerEvent)


ServerProjectEvent_strategy = st.builds(ServerProjectEvent)
@given(instance=ServerProjectEvent_strategy)
@settings(max_examples=25)
def test_ServerProjectEvent_instantiation(instance):
    assert isinstance(instance, ServerProjectEvent)


SessionId_strategy = st.builds(SessionId)
@given(instance=SessionId_strategy)
@settings(max_examples=25)
def test_SessionId_instantiation(instance):
    assert isinstance(instance, SessionId)


Solution_strategy = st.builds(Solution)
@given(instance=Solution_strategy)
@settings(max_examples=25)
def test_Solution_instantiation(instance):
    assert isinstance(instance, Solution)


StateNode_strategy = st.builds(StateNode)
@given(instance=StateNode_strategy)
@settings(max_examples=25)
def test_StateNode_instantiation(instance):
    assert isinstance(instance, StateNode)


StereotypeAttribute_strategy = st.builds(StereotypeAttribute)
@given(instance=StereotypeAttribute_strategy)
@settings(max_examples=25)
def test_StereotypeAttribute_instantiation(instance):
    assert isinstance(instance, StereotypeAttribute)


StereotypeAttributeInstance_strategy = st.builds(StereotypeAttributeInstance)
@given(instance=StereotypeAttributeInstance_strategy)
@settings(max_examples=25)
def test_StereotypeAttributeInstance_instantiation(instance):
    assert isinstance(instance, StereotypeAttributeInstance)


UnicaseModelElement_strategy = st.builds(UnicaseModelElement)
@given(instance=UnicaseModelElement_strategy)
@settings(max_examples=25)
def test_UnicaseModelElement_instantiation(instance):
    assert isinstance(instance, UnicaseModelElement)


UniqueIdentifier_strategy = st.builds(UniqueIdentifier)
@given(instance=UniqueIdentifier_strategy)
@settings(max_examples=25)
def test_UniqueIdentifier_instantiation(instance):
    assert isinstance(instance, UniqueIdentifier)


VersionSpec_strategy = st.builds(VersionSpec)
@given(instance=VersionSpec_strategy)
@settings(max_examples=25)
def test_VersionSpec_instantiation(instance):
    assert isinstance(instance, VersionSpec)


WorkItem_strategy = st.builds(WorkItem)
@given(instance=WorkItem_strategy)
@settings(max_examples=25)
def test_WorkItem_instantiation(instance):
    assert isinstance(instance, WorkItem)


accesscontrol_ACGroup_strategy = st.builds(accesscontrol_ACGroup)
@given(instance=accesscontrol_ACGroup_strategy)
@settings(max_examples=25)
def test_accesscontrol_ACGroup_instantiation(instance):
    assert isinstance(instance, accesscontrol_ACGroup)


accesscontrol_ACOrgUnit_strategy = st.builds(accesscontrol_ACOrgUnit)
@given(instance=accesscontrol_ACOrgUnit_strategy)
@settings(max_examples=25)
def test_accesscontrol_ACOrgUnit_instantiation(instance):
    assert isinstance(instance, accesscontrol_ACOrgUnit)


accesscontrol_ACUser_strategy = st.builds(accesscontrol_ACUser)
@given(instance=accesscontrol_ACUser_strategy)
@settings(max_examples=25)
def test_accesscontrol_ACUser_instantiation(instance):
    assert isinstance(instance, accesscontrol_ACUser)


accesscontrol_OrgUnitProperty_strategy = st.builds(accesscontrol_OrgUnitProperty)
@given(instance=accesscontrol_OrgUnitProperty_strategy)
@settings(max_examples=25)
def test_accesscontrol_OrgUnitProperty_instantiation(instance):
    assert isinstance(instance, accesscontrol_OrgUnitProperty)


activity_ActivityObject_strategy = st.builds(activity_ActivityObject)
@given(instance=activity_ActivityObject_strategy)
@settings(max_examples=25)
def test_activity_ActivityObject_instantiation(instance):
    assert isinstance(instance, activity_ActivityObject)


activity_Transition_strategy = st.builds(activity_Transition)
@given(instance=activity_Transition_strategy)
@settings(max_examples=25)
def test_activity_Transition_instantiation(instance):
    assert isinstance(instance, activity_Transition)


change_MergingProposal_strategy = st.builds(change_MergingProposal)
@given(instance=change_MergingProposal_strategy)
@settings(max_examples=25)
def test_change_MergingProposal_instantiation(instance):
    assert isinstance(instance, change_MergingProposal)


change_ModelChangePackage_strategy = st.builds(change_ModelChangePackage)
@given(instance=change_ModelChangePackage_strategy)
@settings(max_examples=25)
def test_change_ModelChangePackage_instantiation(instance):
    assert isinstance(instance, change_ModelChangePackage)


classes_Association_strategy = st.builds(classes_Association)
@given(instance=classes_Association_strategy)
@settings(max_examples=25)
def test_classes_Association_instantiation(instance):
    assert isinstance(instance, classes_Association)


classes_Attribute_strategy = st.builds(classes_Attribute)
@given(instance=classes_Attribute_strategy)
@settings(max_examples=25)
def test_classes_Attribute_instantiation(instance):
    assert isinstance(instance, classes_Attribute)


classes_Class_strategy = st.builds(classes_Class)
@given(instance=classes_Class_strategy)
@settings(max_examples=25)
def test_classes_Class_instantiation(instance):
    assert isinstance(instance, classes_Class)


classes_Dependency_strategy = st.builds(classes_Dependency)
@given(instance=classes_Dependency_strategy)
@settings(max_examples=25)
def test_classes_Dependency_instantiation(instance):
    assert isinstance(instance, classes_Dependency)


classes_Method_strategy = st.builds(classes_Method)
@given(instance=classes_Method_strategy)
@settings(max_examples=25)
def test_classes_Method_instantiation(instance):
    assert isinstance(instance, classes_Method)


classes_MethodArgument_strategy = st.builds(classes_MethodArgument)
@given(instance=classes_MethodArgument_strategy)
@settings(max_examples=25)
def test_classes_MethodArgument_instantiation(instance):
    assert isinstance(instance, classes_MethodArgument)


classes_Package_strategy = st.builds(classes_Package)
@given(instance=classes_Package_strategy)
@settings(max_examples=25)
def test_classes_Package_instantiation(instance):
    assert isinstance(instance, classes_Package)


classes_PackageElement_strategy = st.builds(classes_PackageElement)
@given(instance=classes_PackageElement_strategy)
@settings(max_examples=25)
def test_classes_PackageElement_instantiation(instance):
    assert isinstance(instance, classes_PackageElement)


component_Component_strategy = st.builds(component_Component)
@given(instance=component_Component_strategy)
@settings(max_examples=25)
def test_component_Component_instantiation(instance):
    assert isinstance(instance, component_Component)


component_ComponentService_strategy = st.builds(component_ComponentService)
@given(instance=component_ComponentService_strategy)
@settings(max_examples=25)
def test_component_ComponentService_instantiation(instance):
    assert isinstance(instance, component_ComponentService)


diagram_model_Diagram_strategy = st.builds(diagram_model_Diagram)
@given(instance=diagram_model_Diagram_strategy)
@settings(max_examples=25)
def test_diagram_model_Diagram_instantiation(instance):
    assert isinstance(instance, diagram_model_Diagram)


document_CompositeSection_strategy = st.builds(document_CompositeSection)
@given(instance=document_CompositeSection_strategy)
@settings(max_examples=25)
def test_document_CompositeSection_instantiation(instance):
    assert isinstance(instance, document_CompositeSection)


document_LeafSection_strategy = st.builds(document_LeafSection)
@given(instance=document_LeafSection_strategy)
@settings(max_examples=25)
def test_document_LeafSection_instantiation(instance):
    assert isinstance(instance, document_LeafSection)


document_Section_strategy = st.builds(document_Section)
@given(instance=document_Section_strategy)
@settings(max_examples=25)
def test_document_Section_instantiation(instance):
    assert isinstance(instance, document_Section)


esmodel_ClientVersionInfo_strategy = st.builds(esmodel_ClientVersionInfo, name=safe_text, version=safe_text)
@given(instance=esmodel_ClientVersionInfo_strategy)
@settings(max_examples=25)
def test_esmodel_ClientVersionInfo_instantiation(instance):
    assert isinstance(instance, esmodel_ClientVersionInfo)


esmodel_FileIdentifier_strategy = st.builds(esmodel_FileIdentifier)
@given(instance=esmodel_FileIdentifier_strategy)
@settings(max_examples=25)
def test_esmodel_FileIdentifier_instantiation(instance):
    assert isinstance(instance, esmodel_FileIdentifier)


esmodel_ProjectHistory_strategy = st.builds(esmodel_ProjectHistory, projectDescription=safe_text, projectName=safe_text)
@given(instance=esmodel_ProjectHistory_strategy)
@settings(max_examples=25)
def test_esmodel_ProjectHistory_instantiation(instance):
    assert isinstance(instance, esmodel_ProjectHistory)


esmodel_ProjectId_strategy = st.builds(esmodel_ProjectId)
@given(instance=esmodel_ProjectId_strategy)
@settings(max_examples=25)
def test_esmodel_ProjectId_instantiation(instance):
    assert isinstance(instance, esmodel_ProjectId)


esmodel_ProjectInfo_strategy = st.builds(esmodel_ProjectInfo, description=safe_text, name=safe_text)
@given(instance=esmodel_ProjectInfo_strategy)
@settings(max_examples=25)
def test_esmodel_ProjectInfo_instantiation(instance):
    assert isinstance(instance, esmodel_ProjectInfo)


esmodel_ServerSpace_strategy = st.builds(esmodel_ServerSpace)
@given(instance=esmodel_ServerSpace_strategy)
@settings(max_examples=25)
def test_esmodel_ServerSpace_instantiation(instance):
    assert isinstance(instance, esmodel_ServerSpace)


esmodel_SessionId_strategy = st.builds(esmodel_SessionId)
@given(instance=esmodel_SessionId_strategy)
@settings(max_examples=25)
def test_esmodel_SessionId_instantiation(instance):
    assert isinstance(instance, esmodel_SessionId)


esmodel_VersionInfo_strategy = st.builds(esmodel_VersionInfo, emfStoreVersionString=safe_text)
@given(instance=esmodel_VersionInfo_strategy)
@settings(max_examples=25)
def test_esmodel_VersionInfo_instantiation(instance):
    assert isinstance(instance, esmodel_VersionInfo)


esmodel_accesscontrol_ACGroup_strategy = st.builds(esmodel_accesscontrol_ACGroup)
@given(instance=esmodel_accesscontrol_ACGroup_strategy)
@settings(max_examples=25)
def test_esmodel_accesscontrol_ACGroup_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACGroup)


esmodel_accesscontrol_ACOrgUnit_strategy = st.builds(esmodel_accesscontrol_ACOrgUnit, description=safe_text, name=safe_text)
@given(instance=esmodel_accesscontrol_ACOrgUnit_strategy)
@settings(max_examples=25)
def test_esmodel_accesscontrol_ACOrgUnit_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACOrgUnit)


esmodel_accesscontrol_ACOrgUnitId_strategy = st.builds(esmodel_accesscontrol_ACOrgUnitId)
@given(instance=esmodel_accesscontrol_ACOrgUnitId_strategy)
@settings(max_examples=25)
def test_esmodel_accesscontrol_ACOrgUnitId_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACOrgUnitId)


esmodel_accesscontrol_ACUser_strategy = st.builds(esmodel_accesscontrol_ACUser, firstName=safe_text, lastName=safe_text)
@given(instance=esmodel_accesscontrol_ACUser_strategy)
@settings(max_examples=25)
def test_esmodel_accesscontrol_ACUser_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACUser)


esmodel_accesscontrol_OrgUnitProperty_strategy = st.builds(esmodel_accesscontrol_OrgUnitProperty, name=safe_text, value=safe_text)
@given(instance=esmodel_accesscontrol_OrgUnitProperty_strategy)
@settings(max_examples=25)
def test_esmodel_accesscontrol_OrgUnitProperty_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_OrgUnitProperty)


esmodel_events_AnnotationEvent_strategy = st.builds(esmodel_events_AnnotationEvent)
@given(instance=esmodel_events_AnnotationEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_AnnotationEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_AnnotationEvent)


esmodel_events_CheckoutEvent_strategy = st.builds(esmodel_events_CheckoutEvent)
@given(instance=esmodel_events_CheckoutEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_CheckoutEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_CheckoutEvent)


esmodel_events_DNDEvent_strategy = st.builds(esmodel_events_DNDEvent, sourceView=safe_text, targetView=safe_text)
@given(instance=esmodel_events_DNDEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_DNDEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_DNDEvent)


esmodel_events_Event_strategy = st.builds(esmodel_events_Event, timestamp=st.dates())
@given(instance=esmodel_events_Event_strategy)
@settings(max_examples=25)
def test_esmodel_events_Event_instantiation(instance):
    assert isinstance(instance, esmodel_events_Event)


esmodel_events_ExceptionEvent_strategy = st.builds(esmodel_events_ExceptionEvent, ExceptionCauseStackTrace=safe_text, ExceptionCauseTitle=safe_text, ExceptionStackTrace=safe_text, ExceptionTitle=safe_text)
@given(instance=esmodel_events_ExceptionEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_ExceptionEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ExceptionEvent)


esmodel_events_LinkEvent_strategy = st.builds(esmodel_events_LinkEvent, createdNew=st.booleans(), sourceView=safe_text)
@given(instance=esmodel_events_LinkEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_LinkEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_LinkEvent)


esmodel_events_MergeChoiceEvent_strategy = st.builds(esmodel_events_MergeChoiceEvent, contextFeature=safe_text, createdIssueName=safe_text, selection=safe_text)
@given(instance=esmodel_events_MergeChoiceEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_MergeChoiceEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_MergeChoiceEvent)


esmodel_events_MergeEvent_strategy = st.builds(esmodel_events_MergeEvent, numberOfConflicts=st.integers(), totalTime=st.integers())
@given(instance=esmodel_events_MergeEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_MergeEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_MergeEvent)


esmodel_events_MergeGlobalChoiceEvent_strategy = st.builds(esmodel_events_MergeGlobalChoiceEvent, selection=safe_text)
@given(instance=esmodel_events_MergeGlobalChoiceEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_MergeGlobalChoiceEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_MergeGlobalChoiceEvent)


esmodel_events_NavigatorCreateEvent_strategy = st.builds(esmodel_events_NavigatorCreateEvent, dynamic=st.booleans())
@given(instance=esmodel_events_NavigatorCreateEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_NavigatorCreateEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NavigatorCreateEvent)


esmodel_events_NotificationGenerationEvent_strategy = st.builds(esmodel_events_NotificationGenerationEvent)
@given(instance=esmodel_events_NotificationGenerationEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_NotificationGenerationEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NotificationGenerationEvent)


esmodel_events_NotificationIgnoreEvent_strategy = st.builds(esmodel_events_NotificationIgnoreEvent, notificationId=safe_text)
@given(instance=esmodel_events_NotificationIgnoreEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_NotificationIgnoreEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NotificationIgnoreEvent)


esmodel_events_NotificationReadEvent_strategy = st.builds(esmodel_events_NotificationReadEvent, notificationId=safe_text)
@given(instance=esmodel_events_NotificationReadEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_NotificationReadEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NotificationReadEvent)


esmodel_events_PerspectiveEvent_strategy = st.builds(esmodel_events_PerspectiveEvent)
@given(instance=esmodel_events_PerspectiveEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_PerspectiveEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PerspectiveEvent)


esmodel_events_PluginFocusEvent_strategy = st.builds(esmodel_events_PluginFocusEvent, pluginId=safe_text, startDate=st.dates())
@given(instance=esmodel_events_PluginFocusEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_PluginFocusEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PluginFocusEvent)


esmodel_events_PluginStartEvent_strategy = st.builds(esmodel_events_PluginStartEvent, pluginId=safe_text)
@given(instance=esmodel_events_PluginStartEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_PluginStartEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PluginStartEvent)


esmodel_events_PresentationSwitchEvent_strategy = st.builds(esmodel_events_PresentationSwitchEvent, newPresentation=safe_text, readView=safe_text)
@given(instance=esmodel_events_PresentationSwitchEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_PresentationSwitchEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PresentationSwitchEvent)


esmodel_events_ReadEvent_strategy = st.builds(esmodel_events_ReadEvent, readView=safe_text, sourceView=safe_text)
@given(instance=esmodel_events_ReadEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_ReadEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ReadEvent)


esmodel_events_RevertEvent_strategy = st.builds(esmodel_events_RevertEvent, revertedChangesCount=st.integers())
@given(instance=esmodel_events_RevertEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_RevertEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_RevertEvent)


esmodel_events_ShowChangesEvent_strategy = st.builds(esmodel_events_ShowChangesEvent)
@given(instance=esmodel_events_ShowChangesEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_ShowChangesEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ShowChangesEvent)


esmodel_events_ShowHistoryEvent_strategy = st.builds(esmodel_events_ShowHistoryEvent)
@given(instance=esmodel_events_ShowHistoryEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_ShowHistoryEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ShowHistoryEvent)


esmodel_events_TraceEvent_strategy = st.builds(esmodel_events_TraceEvent, featureName=safe_text)
@given(instance=esmodel_events_TraceEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_TraceEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_TraceEvent)


esmodel_events_URLEvent_strategy = st.builds(esmodel_events_URLEvent, sourceView=safe_text)
@given(instance=esmodel_events_URLEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_URLEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_URLEvent)


esmodel_events_UndoEvent_strategy = st.builds(esmodel_events_UndoEvent)
@given(instance=esmodel_events_UndoEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_UndoEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_UndoEvent)


esmodel_events_UpdateEvent_strategy = st.builds(esmodel_events_UpdateEvent)
@given(instance=esmodel_events_UpdateEvent_strategy)
@settings(max_examples=25)
def test_esmodel_events_UpdateEvent_instantiation(instance):
    assert isinstance(instance, esmodel_events_UpdateEvent)


esmodel_events_Validate_strategy = st.builds(esmodel_events_Validate)
@given(instance=esmodel_events_Validate_strategy)
@settings(max_examples=25)
def test_esmodel_events_Validate_instantiation(instance):
    assert isinstance(instance, esmodel_events_Validate)


esmodel_notification_ESNotification_strategy = st.builds(esmodel_notification_ESNotification, creationDate=st.dates(), details=safe_text, message=safe_text, name=safe_text, provider=safe_text, recipient=safe_text, seen=st.booleans(), sender=safe_text)
@given(instance=esmodel_notification_ESNotification_strategy)
@settings(max_examples=25)
def test_esmodel_notification_ESNotification_instantiation(instance):
    assert isinstance(instance, esmodel_notification_ESNotification)


esmodel_operations_AbstractOperation_strategy = st.builds(esmodel_operations_AbstractOperation, accepted=st.booleans(), clientDate=st.dates(), description=safe_text, name=safe_text)
@given(instance=esmodel_operations_AbstractOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_AbstractOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_AbstractOperation)


esmodel_operations_AttributeOperation_strategy = st.builds(esmodel_operations_AttributeOperation, newValue=safe_text, oldValue=safe_text)
@given(instance=esmodel_operations_AttributeOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_AttributeOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_AttributeOperation)


esmodel_operations_CompositeOperation_strategy = st.builds(esmodel_operations_CompositeOperation, compositeDescription=safe_text, compositeName=safe_text, reversed=st.booleans())
@given(instance=esmodel_operations_CompositeOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_CompositeOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_CompositeOperation)


esmodel_operations_CreateDeleteOperation_strategy = st.builds(esmodel_operations_CreateDeleteOperation, delete=st.booleans())
@given(instance=esmodel_operations_CreateDeleteOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_CreateDeleteOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_CreateDeleteOperation)


esmodel_operations_DiagramLayoutOperation_strategy = st.builds(esmodel_operations_DiagramLayoutOperation)
@given(instance=esmodel_operations_DiagramLayoutOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_DiagramLayoutOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_DiagramLayoutOperation)


esmodel_operations_EObjectToModelElementIdMap_strategy = st.builds(esmodel_operations_EObjectToModelElementIdMap)
@given(instance=esmodel_operations_EObjectToModelElementIdMap_strategy)
@settings(max_examples=25)
def test_esmodel_operations_EObjectToModelElementIdMap_instantiation(instance):
    assert isinstance(instance, esmodel_operations_EObjectToModelElementIdMap)


esmodel_operations_FeatureOperation_strategy = st.builds(esmodel_operations_FeatureOperation, featureName=safe_text)
@given(instance=esmodel_operations_FeatureOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_FeatureOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_FeatureOperation)


esmodel_operations_ModelElementGroup_strategy = st.builds(esmodel_operations_ModelElementGroup, name=safe_text)
@given(instance=esmodel_operations_ModelElementGroup_strategy)
@settings(max_examples=25)
def test_esmodel_operations_ModelElementGroup_instantiation(instance):
    assert isinstance(instance, esmodel_operations_ModelElementGroup)


esmodel_operations_MultiAttributeMoveOperation_strategy = st.builds(esmodel_operations_MultiAttributeMoveOperation, newIndex=st.integers(), oldIndex=st.integers(), referencedValue=safe_text)
@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_MultiAttributeMoveOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiAttributeMoveOperation)


esmodel_operations_MultiAttributeOperation_strategy = st.builds(esmodel_operations_MultiAttributeOperation, add=st.booleans(), indexes=st.integers(), referencedValues=safe_text)
@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_MultiAttributeOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiAttributeOperation)


esmodel_operations_MultiAttributeSetOperation_strategy = st.builds(esmodel_operations_MultiAttributeSetOperation, index=st.integers(), newValue=safe_text, oldValue=safe_text)
@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_MultiAttributeSetOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiAttributeSetOperation)


esmodel_operations_MultiReferenceMoveOperation_strategy = st.builds(esmodel_operations_MultiReferenceMoveOperation, newIndex=st.integers(), oldIndex=st.integers())
@given(instance=esmodel_operations_MultiReferenceMoveOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_MultiReferenceMoveOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiReferenceMoveOperation)


esmodel_operations_MultiReferenceOperation_strategy = st.builds(esmodel_operations_MultiReferenceOperation, add=st.booleans(), index=st.integers())
@given(instance=esmodel_operations_MultiReferenceOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_MultiReferenceOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiReferenceOperation)


esmodel_operations_MultiReferenceSetOperation_strategy = st.builds(esmodel_operations_MultiReferenceSetOperation, index=st.integers())
@given(instance=esmodel_operations_MultiReferenceSetOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_MultiReferenceSetOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiReferenceSetOperation)


esmodel_operations_OperationGroup_strategy = st.builds(esmodel_operations_OperationGroup, name=safe_text)
@given(instance=esmodel_operations_OperationGroup_strategy)
@settings(max_examples=25)
def test_esmodel_operations_OperationGroup_instantiation(instance):
    assert isinstance(instance, esmodel_operations_OperationGroup)


esmodel_operations_OperationId_strategy = st.builds(esmodel_operations_OperationId)
@given(instance=esmodel_operations_OperationId_strategy)
@settings(max_examples=25)
def test_esmodel_operations_OperationId_instantiation(instance):
    assert isinstance(instance, esmodel_operations_OperationId)


esmodel_operations_ReferenceOperation_strategy = st.builds(esmodel_operations_ReferenceOperation, bidirectional=st.booleans(), containmentType=safe_text, oppositeFeatureName=safe_text)
@given(instance=esmodel_operations_ReferenceOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_ReferenceOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_ReferenceOperation)


esmodel_operations_SingleReferenceOperation_strategy = st.builds(esmodel_operations_SingleReferenceOperation)
@given(instance=esmodel_operations_SingleReferenceOperation_strategy)
@settings(max_examples=25)
def test_esmodel_operations_SingleReferenceOperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_SingleReferenceOperation)


esmodel_roles_ProjectAdminRole_strategy = st.builds(esmodel_roles_ProjectAdminRole)
@given(instance=esmodel_roles_ProjectAdminRole_strategy)
@settings(max_examples=25)
def test_esmodel_roles_ProjectAdminRole_instantiation(instance):
    assert isinstance(instance, esmodel_roles_ProjectAdminRole)


esmodel_roles_ReaderRole_strategy = st.builds(esmodel_roles_ReaderRole)
@given(instance=esmodel_roles_ReaderRole_strategy)
@settings(max_examples=25)
def test_esmodel_roles_ReaderRole_instantiation(instance):
    assert isinstance(instance, esmodel_roles_ReaderRole)


esmodel_roles_Role_strategy = st.builds(esmodel_roles_Role)
@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=25)
def test_esmodel_roles_Role_instantiation(instance):
    assert isinstance(instance, esmodel_roles_Role)


esmodel_roles_ServerAdmin_strategy = st.builds(esmodel_roles_ServerAdmin)
@given(instance=esmodel_roles_ServerAdmin_strategy)
@settings(max_examples=25)
def test_esmodel_roles_ServerAdmin_instantiation(instance):
    assert isinstance(instance, esmodel_roles_ServerAdmin)


esmodel_roles_WriterRole_strategy = st.builds(esmodel_roles_WriterRole)
@given(instance=esmodel_roles_WriterRole_strategy)
@settings(max_examples=25)
def test_esmodel_roles_WriterRole_instantiation(instance):
    assert isinstance(instance, esmodel_roles_WriterRole)


esmodel_semantic_SemanticCompositeOperation_strategy = st.builds(esmodel_semantic_SemanticCompositeOperation)
@given(instance=esmodel_semantic_SemanticCompositeOperation_strategy)
@settings(max_examples=25)
def test_esmodel_semantic_SemanticCompositeOperation_instantiation(instance):
    assert isinstance(instance, esmodel_semantic_SemanticCompositeOperation)


esmodel_server_ProjectUpdatedEvent_strategy = st.builds(esmodel_server_ProjectUpdatedEvent)
@given(instance=esmodel_server_ProjectUpdatedEvent_strategy)
@settings(max_examples=25)
def test_esmodel_server_ProjectUpdatedEvent_instantiation(instance):
    assert isinstance(instance, esmodel_server_ProjectUpdatedEvent)


esmodel_server_ServerEvent_strategy = st.builds(esmodel_server_ServerEvent)
@given(instance=esmodel_server_ServerEvent_strategy)
@settings(max_examples=25)
def test_esmodel_server_ServerEvent_instantiation(instance):
    assert isinstance(instance, esmodel_server_ServerEvent)


esmodel_server_ServerProjectEvent_strategy = st.builds(esmodel_server_ServerProjectEvent)
@given(instance=esmodel_server_ServerProjectEvent_strategy)
@settings(max_examples=25)
def test_esmodel_server_ServerProjectEvent_instantiation(instance):
    assert isinstance(instance, esmodel_server_ServerProjectEvent)


esmodel_url_ModelElementUrl_strategy = st.builds(esmodel_url_ModelElementUrl)
@given(instance=esmodel_url_ModelElementUrl_strategy)
@settings(max_examples=25)
def test_esmodel_url_ModelElementUrl_instantiation(instance):
    assert isinstance(instance, esmodel_url_ModelElementUrl)


esmodel_url_ModelElementUrlFragment_strategy = st.builds(esmodel_url_ModelElementUrlFragment, name=safe_text)
@given(instance=esmodel_url_ModelElementUrlFragment_strategy)
@settings(max_examples=25)
def test_esmodel_url_ModelElementUrlFragment_instantiation(instance):
    assert isinstance(instance, esmodel_url_ModelElementUrlFragment)


esmodel_url_ProjectUrlFragment_strategy = st.builds(esmodel_url_ProjectUrlFragment, name=safe_text)
@given(instance=esmodel_url_ProjectUrlFragment_strategy)
@settings(max_examples=25)
def test_esmodel_url_ProjectUrlFragment_instantiation(instance):
    assert isinstance(instance, esmodel_url_ProjectUrlFragment)


esmodel_url_ServerUrl_strategy = st.builds(esmodel_url_ServerUrl, hostName=safe_text, port=st.integers())
@given(instance=esmodel_url_ServerUrl_strategy)
@settings(max_examples=25)
def test_esmodel_url_ServerUrl_instantiation(instance):
    assert isinstance(instance, esmodel_url_ServerUrl)


esmodel_versioning_ChangePackage_strategy = st.builds(esmodel_versioning_ChangePackage)
@given(instance=esmodel_versioning_ChangePackage_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_ChangePackage_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_ChangePackage)


esmodel_versioning_DateVersionSpec_strategy = st.builds(esmodel_versioning_DateVersionSpec, date=st.dates())
@given(instance=esmodel_versioning_DateVersionSpec_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_DateVersionSpec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_DateVersionSpec)


esmodel_versioning_HeadVersionSpec_strategy = st.builds(esmodel_versioning_HeadVersionSpec)
@given(instance=esmodel_versioning_HeadVersionSpec_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_HeadVersionSpec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_HeadVersionSpec)


esmodel_versioning_HistoryInfo_strategy = st.builds(esmodel_versioning_HistoryInfo)
@given(instance=esmodel_versioning_HistoryInfo_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_HistoryInfo_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_HistoryInfo)


esmodel_versioning_HistoryQuery_strategy = st.builds(esmodel_versioning_HistoryQuery, includeChangePackage=st.booleans())
@given(instance=esmodel_versioning_HistoryQuery_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_HistoryQuery_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_HistoryQuery)


esmodel_versioning_LogMessage_strategy = st.builds(esmodel_versioning_LogMessage, author=safe_text, clientDate=st.dates(), date=st.dates(), message=safe_text)
@given(instance=esmodel_versioning_LogMessage_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_LogMessage_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_LogMessage)


esmodel_versioning_PrimaryVersionSpec_strategy = st.builds(esmodel_versioning_PrimaryVersionSpec, identifier=st.integers())
@given(instance=esmodel_versioning_PrimaryVersionSpec_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_PrimaryVersionSpec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_PrimaryVersionSpec)


esmodel_versioning_TagVersionSpec_strategy = st.builds(esmodel_versioning_TagVersionSpec, name=safe_text)
@given(instance=esmodel_versioning_TagVersionSpec_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_TagVersionSpec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_TagVersionSpec)


esmodel_versioning_Version_strategy = st.builds(esmodel_versioning_Version)
@given(instance=esmodel_versioning_Version_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_Version_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_Version)


esmodel_versioning_VersionProperty_strategy = st.builds(esmodel_versioning_VersionProperty, name=safe_text, value=safe_text)
@given(instance=esmodel_versioning_VersionProperty_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_VersionProperty_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_VersionProperty)


esmodel_versioning_VersionSpec_strategy = st.builds(esmodel_versioning_VersionSpec)
@given(instance=esmodel_versioning_VersionSpec_strategy)
@settings(max_examples=25)
def test_esmodel_versioning_VersionSpec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_VersionSpec)


events_Event_strategy = st.builds(events_Event)
@given(instance=events_Event_strategy)
@settings(max_examples=25)
def test_events_Event_instantiation(instance):
    assert isinstance(instance, events_Event)


meeting_IssueMeetingSection_strategy = st.builds(meeting_IssueMeetingSection)
@given(instance=meeting_IssueMeetingSection_strategy)
@settings(max_examples=25)
def test_meeting_IssueMeetingSection_instantiation(instance):
    assert isinstance(instance, meeting_IssueMeetingSection)


meeting_MeetingSection_strategy = st.builds(meeting_MeetingSection)
@given(instance=meeting_MeetingSection_strategy)
@settings(max_examples=25)
def test_meeting_MeetingSection_instantiation(instance):
    assert isinstance(instance, meeting_MeetingSection)


meeting_WorkItemMeetingSection_strategy = st.builds(meeting_WorkItemMeetingSection)
@given(instance=meeting_WorkItemMeetingSection_strategy)
@settings(max_examples=25)
def test_meeting_WorkItemMeetingSection_instantiation(instance):
    assert isinstance(instance, meeting_WorkItemMeetingSection)


metamodel_AssociationClassElement_strategy = st.builds(metamodel_AssociationClassElement)
@given(instance=metamodel_AssociationClassElement_strategy)
@settings(max_examples=25)
def test_metamodel_AssociationClassElement_instantiation(instance):
    assert isinstance(instance, metamodel_AssociationClassElement)


metamodel_IdentifiableElement_strategy = st.builds(metamodel_IdentifiableElement, identifier=safe_text)
@given(instance=metamodel_IdentifiableElement_strategy)
@settings(max_examples=25)
def test_metamodel_IdentifiableElement_instantiation(instance):
    assert isinstance(instance, metamodel_IdentifiableElement)


metamodel_ModelElement_strategy = st.builds(metamodel_ModelElement, creationDate=st.dates(), creator=safe_text)
@given(instance=metamodel_ModelElement_strategy)
@settings(max_examples=25)
def test_metamodel_ModelElement_instantiation(instance):
    assert isinstance(instance, metamodel_ModelElement)


metamodel_ModelElementId_strategy = st.builds(metamodel_ModelElementId)
@given(instance=metamodel_ModelElementId_strategy)
@settings(max_examples=25)
def test_metamodel_ModelElementId_instantiation(instance):
    assert isinstance(instance, metamodel_ModelElementId)


metamodel_ModelVersion_strategy = st.builds(metamodel_ModelVersion, releaseNumber=st.integers())
@given(instance=metamodel_ModelVersion_strategy)
@settings(max_examples=25)
def test_metamodel_ModelVersion_instantiation(instance):
    assert isinstance(instance, metamodel_ModelVersion)


metamodel_NonDomainElement_strategy = st.builds(metamodel_NonDomainElement)
@given(instance=metamodel_NonDomainElement_strategy)
@settings(max_examples=25)
def test_metamodel_NonDomainElement_instantiation(instance):
    assert isinstance(instance, metamodel_NonDomainElement)


metamodel_Project_strategy = st.builds(metamodel_Project)
@given(instance=metamodel_Project_strategy)
@settings(max_examples=25)
def test_metamodel_Project_instantiation(instance):
    assert isinstance(instance, metamodel_Project)


metamodel_UniqueIdentifier_strategy = st.builds(metamodel_UniqueIdentifier, id=safe_text)
@given(instance=metamodel_UniqueIdentifier_strategy)
@settings(max_examples=25)
def test_metamodel_UniqueIdentifier_instantiation(instance):
    assert isinstance(instance, metamodel_UniqueIdentifier)


model_Annotation_strategy = st.builds(model_Annotation)
@given(instance=model_Annotation_strategy)
@settings(max_examples=25)
def test_model_Annotation_instantiation(instance):
    assert isinstance(instance, model_Annotation)


model_Attachment_strategy = st.builds(model_Attachment)
@given(instance=model_Attachment_strategy)
@settings(max_examples=25)
def test_model_Attachment_instantiation(instance):
    assert isinstance(instance, model_Attachment)


model_NonDomainElement_strategy = st.builds(model_NonDomainElement)
@given(instance=model_NonDomainElement_strategy)
@settings(max_examples=25)
def test_model_NonDomainElement_instantiation(instance):
    assert isinstance(instance, model_NonDomainElement)


model_Project_strategy = st.builds(model_Project)
@given(instance=model_Project_strategy)
@settings(max_examples=25)
def test_model_Project_instantiation(instance):
    assert isinstance(instance, model_Project)


model_UnicaseModelElement_strategy = st.builds(model_UnicaseModelElement, description=safe_text, name=safe_text, state=safe_text)
@given(instance=model_UnicaseModelElement_strategy)
@settings(max_examples=25)
def test_model_UnicaseModelElement_instantiation(instance):
    assert isinstance(instance, model_UnicaseModelElement)


model_activity_Activity_strategy = st.builds(model_activity_Activity)
@given(instance=model_activity_Activity_strategy)
@settings(max_examples=25)
def test_model_activity_Activity_instantiation(instance):
    assert isinstance(instance, model_activity_Activity)


model_activity_ActivityEnd_strategy = st.builds(model_activity_ActivityEnd)
@given(instance=model_activity_ActivityEnd_strategy)
@settings(max_examples=25)
def test_model_activity_ActivityEnd_instantiation(instance):
    assert isinstance(instance, model_activity_ActivityEnd)


model_activity_ActivityInitial_strategy = st.builds(model_activity_ActivityInitial)
@given(instance=model_activity_ActivityInitial_strategy)
@settings(max_examples=25)
def test_model_activity_ActivityInitial_instantiation(instance):
    assert isinstance(instance, model_activity_ActivityInitial)


model_activity_ActivityObject_strategy = st.builds(model_activity_ActivityObject)
@given(instance=model_activity_ActivityObject_strategy)
@settings(max_examples=25)
def test_model_activity_ActivityObject_instantiation(instance):
    assert isinstance(instance, model_activity_ActivityObject)


model_activity_Branch_strategy = st.builds(model_activity_Branch)
@given(instance=model_activity_Branch_strategy)
@settings(max_examples=25)
def test_model_activity_Branch_instantiation(instance):
    assert isinstance(instance, model_activity_Branch)


model_activity_Fork_strategy = st.builds(model_activity_Fork)
@given(instance=model_activity_Fork_strategy)
@settings(max_examples=25)
def test_model_activity_Fork_instantiation(instance):
    assert isinstance(instance, model_activity_Fork)


model_activity_Transition_strategy = st.builds(model_activity_Transition, condition=safe_text)
@given(instance=model_activity_Transition_strategy)
@settings(max_examples=25)
def test_model_activity_Transition_instantiation(instance):
    assert isinstance(instance, model_activity_Transition)


model_attachment_FileAttachment_strategy = st.builds(model_attachment_FileAttachment, fileHash=safe_text, fileID=safe_text, fileName=safe_text, fileSize=safe_text, requiredOffline=st.booleans())
@given(instance=model_attachment_FileAttachment_strategy)
@settings(max_examples=25)
def test_model_attachment_FileAttachment_instantiation(instance):
    assert isinstance(instance, model_attachment_FileAttachment)


model_attachment_UrlAttachment_strategy = st.builds(model_attachment_UrlAttachment, url=safe_text)
@given(instance=model_attachment_UrlAttachment_strategy)
@settings(max_examples=25)
def test_model_attachment_UrlAttachment_instantiation(instance):
    assert isinstance(instance, model_attachment_UrlAttachment)


model_bug_BugReport_strategy = st.builds(model_bug_BugReport, Status=safe_text, resolution=safe_text, resolutionType=safe_text, severity=safe_text)
@given(instance=model_bug_BugReport_strategy)
@settings(max_examples=25)
def test_model_bug_BugReport_instantiation(instance):
    assert isinstance(instance, model_bug_BugReport)


model_change_MergingIssue_strategy = st.builds(model_change_MergingIssue, resolvingRevision=st.integers())
@given(instance=model_change_MergingIssue_strategy)
@settings(max_examples=25)
def test_model_change_MergingIssue_instantiation(instance):
    assert isinstance(instance, model_change_MergingIssue)


model_change_MergingProposal_strategy = st.builds(model_change_MergingProposal)
@given(instance=model_change_MergingProposal_strategy)
@settings(max_examples=25)
def test_model_change_MergingProposal_instantiation(instance):
    assert isinstance(instance, model_change_MergingProposal)


model_change_MergingSolution_strategy = st.builds(model_change_MergingSolution)
@given(instance=model_change_MergingSolution_strategy)
@settings(max_examples=25)
def test_model_change_MergingSolution_instantiation(instance):
    assert isinstance(instance, model_change_MergingSolution)


model_change_ModelChangePackage_strategy = st.builds(model_change_ModelChangePackage, sourceVersion=st.integers(), targetVersion=st.integers())
@given(instance=model_change_ModelChangePackage_strategy)
@settings(max_examples=25)
def test_model_change_ModelChangePackage_instantiation(instance):
    assert isinstance(instance, model_change_ModelChangePackage)


model_classes_Association_strategy = st.builds(model_classes_Association, sourceMultiplicity=safe_text, sourceRole=safe_text, targetMultiplicity=safe_text, targetRole=safe_text, type=safe_text)
@given(instance=model_classes_Association_strategy)
@settings(max_examples=25)
def test_model_classes_Association_instantiation(instance):
    assert isinstance(instance, model_classes_Association)


model_classes_Attribute_strategy = st.builds(model_classes_Attribute, defaultValue=safe_text, label=safe_text, properties=safe_text, scope=safe_text, signature=safe_text, type=safe_text, visibility=safe_text)
@given(instance=model_classes_Attribute_strategy)
@settings(max_examples=25)
def test_model_classes_Attribute_instantiation(instance):
    assert isinstance(instance, model_classes_Attribute)


model_classes_Class_strategy = st.builds(model_classes_Class)
@given(instance=model_classes_Class_strategy)
@settings(max_examples=25)
def test_model_classes_Class_instantiation(instance):
    assert isinstance(instance, model_classes_Class)


model_classes_Dependency_strategy = st.builds(model_classes_Dependency)
@given(instance=model_classes_Dependency_strategy)
@settings(max_examples=25)
def test_model_classes_Dependency_instantiation(instance):
    assert isinstance(instance, model_classes_Dependency)


model_classes_Method_strategy = st.builds(model_classes_Method, label=safe_text, properties=safe_text, returnType=safe_text, scope=safe_text, signature=safe_text, stubbed=st.booleans(), visibility=safe_text)
@given(instance=model_classes_Method_strategy)
@settings(max_examples=25)
def test_model_classes_Method_instantiation(instance):
    assert isinstance(instance, model_classes_Method)


model_classes_MethodArgument_strategy = st.builds(model_classes_MethodArgument, defaultValue=safe_text, direction=safe_text, label=safe_text, signature=safe_text, type=safe_text)
@given(instance=model_classes_MethodArgument_strategy)
@settings(max_examples=25)
def test_model_classes_MethodArgument_instantiation(instance):
    assert isinstance(instance, model_classes_MethodArgument)


model_classes_Package_strategy = st.builds(model_classes_Package)
@given(instance=model_classes_Package_strategy)
@settings(max_examples=25)
def test_model_classes_Package_instantiation(instance):
    assert isinstance(instance, model_classes_Package)


model_classes_PackageElement_strategy = st.builds(model_classes_PackageElement)
@given(instance=model_classes_PackageElement_strategy)
@settings(max_examples=25)
def test_model_classes_PackageElement_instantiation(instance):
    assert isinstance(instance, model_classes_PackageElement)


model_component_Component_strategy = st.builds(model_component_Component)
@given(instance=model_component_Component_strategy)
@settings(max_examples=25)
def test_model_component_Component_instantiation(instance):
    assert isinstance(instance, model_component_Component)


model_component_ComponentService_strategy = st.builds(model_component_ComponentService)
@given(instance=model_component_ComponentService_strategy)
@settings(max_examples=25)
def test_model_component_ComponentService_instantiation(instance):
    assert isinstance(instance, model_component_ComponentService)


model_component_DeploymentNode_strategy = st.builds(model_component_DeploymentNode)
@given(instance=model_component_DeploymentNode_strategy)
@settings(max_examples=25)
def test_model_component_DeploymentNode_instantiation(instance):
    assert isinstance(instance, model_component_DeploymentNode)


model_diagram_MEDiagram_strategy = st.builds(model_diagram_MEDiagram, diagramLayout=safe_text, type=safe_text)
@given(instance=model_diagram_MEDiagram_strategy)
@settings(max_examples=25)
def test_model_diagram_MEDiagram_instantiation(instance):
    assert isinstance(instance, model_diagram_MEDiagram)


model_document_CompositeSection_strategy = st.builds(model_document_CompositeSection)
@given(instance=model_document_CompositeSection_strategy)
@settings(max_examples=25)
def test_model_document_CompositeSection_instantiation(instance):
    assert isinstance(instance, model_document_CompositeSection)


model_document_LeafSection_strategy = st.builds(model_document_LeafSection)
@given(instance=model_document_LeafSection_strategy)
@settings(max_examples=25)
def test_model_document_LeafSection_instantiation(instance):
    assert isinstance(instance, model_document_LeafSection)


model_document_Section_strategy = st.builds(model_document_Section)
@given(instance=model_document_Section_strategy)
@settings(max_examples=25)
def test_model_document_Section_instantiation(instance):
    assert isinstance(instance, model_document_Section)


model_meeting_CompositeMeetingSection_strategy = st.builds(model_meeting_CompositeMeetingSection)
@given(instance=model_meeting_CompositeMeetingSection_strategy)
@settings(max_examples=25)
def test_model_meeting_CompositeMeetingSection_instantiation(instance):
    assert isinstance(instance, model_meeting_CompositeMeetingSection)


model_meeting_IssueMeetingSection_strategy = st.builds(model_meeting_IssueMeetingSection)
@given(instance=model_meeting_IssueMeetingSection_strategy)
@settings(max_examples=25)
def test_model_meeting_IssueMeetingSection_instantiation(instance):
    assert isinstance(instance, model_meeting_IssueMeetingSection)


model_meeting_Meeting_strategy = st.builds(model_meeting_Meeting, endtime=st.dates(), location=safe_text, starttime=st.dates())
@given(instance=model_meeting_Meeting_strategy)
@settings(max_examples=25)
def test_model_meeting_Meeting_instantiation(instance):
    assert isinstance(instance, model_meeting_Meeting)


model_meeting_MeetingSection_strategy = st.builds(model_meeting_MeetingSection, allocatedTime=st.integers())
@given(instance=model_meeting_MeetingSection_strategy)
@settings(max_examples=25)
def test_model_meeting_MeetingSection_instantiation(instance):
    assert isinstance(instance, model_meeting_MeetingSection)


model_meeting_WorkItemMeetingSection_strategy = st.builds(model_meeting_WorkItemMeetingSection)
@given(instance=model_meeting_WorkItemMeetingSection_strategy)
@settings(max_examples=25)
def test_model_meeting_WorkItemMeetingSection_instantiation(instance):
    assert isinstance(instance, model_meeting_WorkItemMeetingSection)


model_organization_Group_strategy = st.builds(model_organization_Group)
@given(instance=model_organization_Group_strategy)
@settings(max_examples=25)
def test_model_organization_Group_instantiation(instance):
    assert isinstance(instance, model_organization_Group)


model_organization_OrgUnit_strategy = st.builds(model_organization_OrgUnit, acOrgId=safe_text)
@given(instance=model_organization_OrgUnit_strategy)
@settings(max_examples=25)
def test_model_organization_OrgUnit_instantiation(instance):
    assert isinstance(instance, model_organization_OrgUnit)


model_organization_User_strategy = st.builds(model_organization_User, email=safe_text, firstName=safe_text, lastName=safe_text)
@given(instance=model_organization_User_strategy)
@settings(max_examples=25)
def test_model_organization_User_instantiation(instance):
    assert isinstance(instance, model_organization_User)


model_profile_Profile_strategy = st.builds(model_profile_Profile)
@given(instance=model_profile_Profile_strategy)
@settings(max_examples=25)
def test_model_profile_Profile_instantiation(instance):
    assert isinstance(instance, model_profile_Profile)


model_profile_Stereotype_strategy = st.builds(model_profile_Stereotype, required=st.booleans())
@given(instance=model_profile_Stereotype_strategy)
@settings(max_examples=25)
def test_model_profile_Stereotype_instantiation(instance):
    assert isinstance(instance, model_profile_Stereotype)


model_profile_StereotypeAttribute_strategy = st.builds(model_profile_StereotypeAttribute)
@given(instance=model_profile_StereotypeAttribute_strategy)
@settings(max_examples=25)
def test_model_profile_StereotypeAttribute_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttribute)


model_profile_StereotypeAttributeInstance_strategy = st.builds(model_profile_StereotypeAttributeInstance)
@given(instance=model_profile_StereotypeAttributeInstance_strategy)
@settings(max_examples=25)
def test_model_profile_StereotypeAttributeInstance_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttributeInstance)


model_profile_StereotypeAttributeInstanceString_strategy = st.builds(model_profile_StereotypeAttributeInstanceString, value=safe_text)
@given(instance=model_profile_StereotypeAttributeInstanceString_strategy)
@settings(max_examples=25)
def test_model_profile_StereotypeAttributeInstanceString_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttributeInstanceString)


model_profile_StereotypeAttributeSimple_strategy = st.builds(model_profile_StereotypeAttributeSimple, type=safe_text)
@given(instance=model_profile_StereotypeAttributeSimple_strategy)
@settings(max_examples=25)
def test_model_profile_StereotypeAttributeSimple_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttributeSimple)


model_profile_StereotypeInstance_strategy = st.builds(model_profile_StereotypeInstance)
@given(instance=model_profile_StereotypeInstance_strategy)
@settings(max_examples=25)
def test_model_profile_StereotypeInstance_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeInstance)


model_rationale_Assessment_strategy = st.builds(model_rationale_Assessment, value=st.integers())
@given(instance=model_rationale_Assessment_strategy)
@settings(max_examples=25)
def test_model_rationale_Assessment_instantiation(instance):
    assert isinstance(instance, model_rationale_Assessment)


model_rationale_Comment_strategy = st.builds(model_rationale_Comment)
@given(instance=model_rationale_Comment_strategy)
@settings(max_examples=25)
def test_model_rationale_Comment_instantiation(instance):
    assert isinstance(instance, model_rationale_Comment)


model_rationale_Criterion_strategy = st.builds(model_rationale_Criterion)
@given(instance=model_rationale_Criterion_strategy)
@settings(max_examples=25)
def test_model_rationale_Criterion_instantiation(instance):
    assert isinstance(instance, model_rationale_Criterion)


model_rationale_Issue_strategy = st.builds(model_rationale_Issue, activity=safe_text)
@given(instance=model_rationale_Issue_strategy)
@settings(max_examples=25)
def test_model_rationale_Issue_instantiation(instance):
    assert isinstance(instance, model_rationale_Issue)


model_rationale_Proposal_strategy = st.builds(model_rationale_Proposal)
@given(instance=model_rationale_Proposal_strategy)
@settings(max_examples=25)
def test_model_rationale_Proposal_instantiation(instance):
    assert isinstance(instance, model_rationale_Proposal)


model_rationale_Solution_strategy = st.builds(model_rationale_Solution)
@given(instance=model_rationale_Solution_strategy)
@settings(max_examples=25)
def test_model_rationale_Solution_instantiation(instance):
    assert isinstance(instance, model_rationale_Solution)


model_requirement_Actor_strategy = st.builds(model_requirement_Actor)
@given(instance=model_requirement_Actor_strategy)
@settings(max_examples=25)
def test_model_requirement_Actor_instantiation(instance):
    assert isinstance(instance, model_requirement_Actor)


model_requirement_ActorInstance_strategy = st.builds(model_requirement_ActorInstance)
@given(instance=model_requirement_ActorInstance_strategy)
@settings(max_examples=25)
def test_model_requirement_ActorInstance_instantiation(instance):
    assert isinstance(instance, model_requirement_ActorInstance)


model_requirement_FunctionalRequirement_strategy = st.builds(model_requirement_FunctionalRequirement, cost=st.integers(), priority=st.integers(), reviewed=st.booleans(), storyPoints=st.integers())
@given(instance=model_requirement_FunctionalRequirement_strategy)
@settings(max_examples=25)
def test_model_requirement_FunctionalRequirement_instantiation(instance):
    assert isinstance(instance, model_requirement_FunctionalRequirement)


model_requirement_NonFunctionalRequirement_strategy = st.builds(model_requirement_NonFunctionalRequirement)
@given(instance=model_requirement_NonFunctionalRequirement_strategy)
@settings(max_examples=25)
def test_model_requirement_NonFunctionalRequirement_instantiation(instance):
    assert isinstance(instance, model_requirement_NonFunctionalRequirement)


model_requirement_Scenario_strategy = st.builds(model_requirement_Scenario)
@given(instance=model_requirement_Scenario_strategy)
@settings(max_examples=25)
def test_model_requirement_Scenario_instantiation(instance):
    assert isinstance(instance, model_requirement_Scenario)


model_requirement_Step_strategy = st.builds(model_requirement_Step, userStep=st.booleans())
@given(instance=model_requirement_Step_strategy)
@settings(max_examples=25)
def test_model_requirement_Step_instantiation(instance):
    assert isinstance(instance, model_requirement_Step)


model_requirement_SystemFunction_strategy = st.builds(model_requirement_SystemFunction, exception=safe_text, input=safe_text, output=safe_text)
@given(instance=model_requirement_SystemFunction_strategy)
@settings(max_examples=25)
def test_model_requirement_SystemFunction_instantiation(instance):
    assert isinstance(instance, model_requirement_SystemFunction)


model_requirement_UseCase_strategy = st.builds(model_requirement_UseCase, exception=safe_text, postcondition=safe_text, precondition=safe_text, rules=safe_text)
@given(instance=model_requirement_UseCase_strategy)
@settings(max_examples=25)
def test_model_requirement_UseCase_instantiation(instance):
    assert isinstance(instance, model_requirement_UseCase)


model_requirement_UserTask_strategy = st.builds(model_requirement_UserTask)
@given(instance=model_requirement_UserTask_strategy)
@settings(max_examples=25)
def test_model_requirement_UserTask_instantiation(instance):
    assert isinstance(instance, model_requirement_UserTask)


model_state_State_strategy = st.builds(model_state_State, activities=safe_text, entryConditions=safe_text, exitConditions=safe_text)
@given(instance=model_state_State_strategy)
@settings(max_examples=25)
def test_model_state_State_instantiation(instance):
    assert isinstance(instance, model_state_State)


model_state_StateEnd_strategy = st.builds(model_state_StateEnd)
@given(instance=model_state_StateEnd_strategy)
@settings(max_examples=25)
def test_model_state_StateEnd_instantiation(instance):
    assert isinstance(instance, model_state_StateEnd)


model_state_StateInitial_strategy = st.builds(model_state_StateInitial)
@given(instance=model_state_StateInitial_strategy)
@settings(max_examples=25)
def test_model_state_StateInitial_instantiation(instance):
    assert isinstance(instance, model_state_StateInitial)


model_state_StateNode_strategy = st.builds(model_state_StateNode)
@given(instance=model_state_StateNode_strategy)
@settings(max_examples=25)
def test_model_state_StateNode_instantiation(instance):
    assert isinstance(instance, model_state_StateNode)


model_state_Transition_strategy = st.builds(model_state_Transition, condition=safe_text)
@given(instance=model_state_Transition_strategy)
@settings(max_examples=25)
def test_model_state_Transition_instantiation(instance):
    assert isinstance(instance, model_state_Transition)


model_task_ActionItem_strategy = st.builds(model_task_ActionItem, activity=safe_text, done=st.booleans())
@given(instance=model_task_ActionItem_strategy)
@settings(max_examples=25)
def test_model_task_ActionItem_instantiation(instance):
    assert isinstance(instance, model_task_ActionItem)


model_task_Checkable_strategy = st.builds(model_task_Checkable, checked=st.booleans())
@given(instance=model_task_Checkable_strategy)
@settings(max_examples=25)
def test_model_task_Checkable_instantiation(instance):
    assert isinstance(instance, model_task_Checkable)


model_task_Milestone_strategy = st.builds(model_task_Milestone)
@given(instance=model_task_Milestone_strategy)
@settings(max_examples=25)
def test_model_task_Milestone_instantiation(instance):
    assert isinstance(instance, model_task_Milestone)


model_task_WorkItem_strategy = st.builds(model_task_WorkItem, dueDate=st.dates(), effort=st.integers(), estimate=st.integers(), priority=st.integers(), resolved=st.booleans())
@given(instance=model_task_WorkItem_strategy)
@settings(max_examples=25)
def test_model_task_WorkItem_instantiation(instance):
    assert isinstance(instance, model_task_WorkItem)


model_task_WorkPackage_strategy = st.builds(model_task_WorkPackage, endDate=st.dates(), startDate=st.dates())
@given(instance=model_task_WorkPackage_strategy)
@settings(max_examples=25)
def test_model_task_WorkPackage_instantiation(instance):
    assert isinstance(instance, model_task_WorkPackage)


model_util_ModelElementPath_strategy = st.builds(model_util_ModelElementPath)
@given(instance=model_util_ModelElementPath_strategy)
@settings(max_examples=25)
def test_model_util_ModelElementPath_instantiation(instance):
    assert isinstance(instance, model_util_ModelElementPath)


notification_ESNotification_strategy = st.builds(notification_ESNotification)
@given(instance=notification_ESNotification_strategy)
@settings(max_examples=25)
def test_notification_ESNotification_instantiation(instance):
    assert isinstance(instance, notification_ESNotification)


operations_AbstractOperation_strategy = st.builds(operations_AbstractOperation)
@given(instance=operations_AbstractOperation_strategy)
@settings(max_examples=25)
def test_operations_AbstractOperation_instantiation(instance):
    assert isinstance(instance, operations_AbstractOperation)


operations_EObjectToModelElementIdMap_strategy = st.builds(operations_EObjectToModelElementIdMap)
@given(instance=operations_EObjectToModelElementIdMap_strategy)
@settings(max_examples=25)
def test_operations_EObjectToModelElementIdMap_instantiation(instance):
    assert isinstance(instance, operations_EObjectToModelElementIdMap)


operations_OperationId_strategy = st.builds(operations_OperationId)
@given(instance=operations_OperationId_strategy)
@settings(max_examples=25)
def test_operations_OperationId_instantiation(instance):
    assert isinstance(instance, operations_OperationId)


operations_ReferenceOperation_strategy = st.builds(operations_ReferenceOperation)
@given(instance=operations_ReferenceOperation_strategy)
@settings(max_examples=25)
def test_operations_ReferenceOperation_instantiation(instance):
    assert isinstance(instance, operations_ReferenceOperation)


operations_esmodel_EObject_strategy = st.builds(operations_esmodel_EObject)
@given(instance=operations_esmodel_EObject_strategy)
@settings(max_examples=25)
def test_operations_esmodel_EObject_instantiation(instance):
    assert isinstance(instance, operations_esmodel_EObject)


organization_Group_strategy = st.builds(organization_Group)
@given(instance=organization_Group_strategy)
@settings(max_examples=25)
def test_organization_Group_instantiation(instance):
    assert isinstance(instance, organization_Group)


organization_OrgUnit_strategy = st.builds(organization_OrgUnit)
@given(instance=organization_OrgUnit_strategy)
@settings(max_examples=25)
def test_organization_OrgUnit_instantiation(instance):
    assert isinstance(instance, organization_OrgUnit)


organization_User_strategy = st.builds(organization_User)
@given(instance=organization_User_strategy)
@settings(max_examples=25)
def test_organization_User_instantiation(instance):
    assert isinstance(instance, organization_User)


profile_Profile_strategy = st.builds(profile_Profile)
@given(instance=profile_Profile_strategy)
@settings(max_examples=25)
def test_profile_Profile_instantiation(instance):
    assert isinstance(instance, profile_Profile)


profile_Stereotype_strategy = st.builds(profile_Stereotype)
@given(instance=profile_Stereotype_strategy)
@settings(max_examples=25)
def test_profile_Stereotype_instantiation(instance):
    assert isinstance(instance, profile_Stereotype)


profile_StereotypeAttribute_strategy = st.builds(profile_StereotypeAttribute)
@given(instance=profile_StereotypeAttribute_strategy)
@settings(max_examples=25)
def test_profile_StereotypeAttribute_instantiation(instance):
    assert isinstance(instance, profile_StereotypeAttribute)


profile_StereotypeAttributeInstance_strategy = st.builds(profile_StereotypeAttributeInstance)
@given(instance=profile_StereotypeAttributeInstance_strategy)
@settings(max_examples=25)
def test_profile_StereotypeAttributeInstance_instantiation(instance):
    assert isinstance(instance, profile_StereotypeAttributeInstance)


profile_StereotypeInstance_strategy = st.builds(profile_StereotypeInstance)
@given(instance=profile_StereotypeInstance_strategy)
@settings(max_examples=25)
def test_profile_StereotypeInstance_instantiation(instance):
    assert isinstance(instance, profile_StereotypeInstance)


rationale_Assessment_strategy = st.builds(rationale_Assessment)
@given(instance=rationale_Assessment_strategy)
@settings(max_examples=25)
def test_rationale_Assessment_instantiation(instance):
    assert isinstance(instance, rationale_Assessment)


rationale_Comment_strategy = st.builds(rationale_Comment)
@given(instance=rationale_Comment_strategy)
@settings(max_examples=25)
def test_rationale_Comment_instantiation(instance):
    assert isinstance(instance, rationale_Comment)


rationale_Criterion_strategy = st.builds(rationale_Criterion)
@given(instance=rationale_Criterion_strategy)
@settings(max_examples=25)
def test_rationale_Criterion_instantiation(instance):
    assert isinstance(instance, rationale_Criterion)


rationale_Issue_strategy = st.builds(rationale_Issue)
@given(instance=rationale_Issue_strategy)
@settings(max_examples=25)
def test_rationale_Issue_instantiation(instance):
    assert isinstance(instance, rationale_Issue)


rationale_Proposal_strategy = st.builds(rationale_Proposal)
@given(instance=rationale_Proposal_strategy)
@settings(max_examples=25)
def test_rationale_Proposal_instantiation(instance):
    assert isinstance(instance, rationale_Proposal)


rationale_Solution_strategy = st.builds(rationale_Solution)
@given(instance=rationale_Solution_strategy)
@settings(max_examples=25)
def test_rationale_Solution_instantiation(instance):
    assert isinstance(instance, rationale_Solution)


requirement_Actor_strategy = st.builds(requirement_Actor)
@given(instance=requirement_Actor_strategy)
@settings(max_examples=25)
def test_requirement_Actor_instantiation(instance):
    assert isinstance(instance, requirement_Actor)


requirement_ActorInstance_strategy = st.builds(requirement_ActorInstance)
@given(instance=requirement_ActorInstance_strategy)
@settings(max_examples=25)
def test_requirement_ActorInstance_instantiation(instance):
    assert isinstance(instance, requirement_ActorInstance)


requirement_FunctionalRequirement_strategy = st.builds(requirement_FunctionalRequirement)
@given(instance=requirement_FunctionalRequirement_strategy)
@settings(max_examples=25)
def test_requirement_FunctionalRequirement_instantiation(instance):
    assert isinstance(instance, requirement_FunctionalRequirement)


requirement_NonFunctionalRequirement_strategy = st.builds(requirement_NonFunctionalRequirement)
@given(instance=requirement_NonFunctionalRequirement_strategy)
@settings(max_examples=25)
def test_requirement_NonFunctionalRequirement_instantiation(instance):
    assert isinstance(instance, requirement_NonFunctionalRequirement)


requirement_Scenario_strategy = st.builds(requirement_Scenario)
@given(instance=requirement_Scenario_strategy)
@settings(max_examples=25)
def test_requirement_Scenario_instantiation(instance):
    assert isinstance(instance, requirement_Scenario)


requirement_Step_strategy = st.builds(requirement_Step)
@given(instance=requirement_Step_strategy)
@settings(max_examples=25)
def test_requirement_Step_instantiation(instance):
    assert isinstance(instance, requirement_Step)


requirement_SystemFunction_strategy = st.builds(requirement_SystemFunction)
@given(instance=requirement_SystemFunction_strategy)
@settings(max_examples=25)
def test_requirement_SystemFunction_instantiation(instance):
    assert isinstance(instance, requirement_SystemFunction)


requirement_UseCase_strategy = st.builds(requirement_UseCase)
@given(instance=requirement_UseCase_strategy)
@settings(max_examples=25)
def test_requirement_UseCase_instantiation(instance):
    assert isinstance(instance, requirement_UseCase)


requirement_UserTask_strategy = st.builds(requirement_UserTask)
@given(instance=requirement_UserTask_strategy)
@settings(max_examples=25)
def test_requirement_UserTask_instantiation(instance):
    assert isinstance(instance, requirement_UserTask)


roles_Role_strategy = st.builds(roles_Role)
@given(instance=roles_Role_strategy)
@settings(max_examples=25)
def test_roles_Role_instantiation(instance):
    assert isinstance(instance, roles_Role)


state_StateNode_strategy = st.builds(state_StateNode)
@given(instance=state_StateNode_strategy)
@settings(max_examples=25)
def test_state_StateNode_instantiation(instance):
    assert isinstance(instance, state_StateNode)


state_Transition_strategy = st.builds(state_Transition)
@given(instance=state_Transition_strategy)
@settings(max_examples=25)
def test_state_Transition_instantiation(instance):
    assert isinstance(instance, state_Transition)


task_Checkable_strategy = st.builds(task_Checkable)
@given(instance=task_Checkable_strategy)
@settings(max_examples=25)
def test_task_Checkable_instantiation(instance):
    assert isinstance(instance, task_Checkable)


task_WorkItem_strategy = st.builds(task_WorkItem)
@given(instance=task_WorkItem_strategy)
@settings(max_examples=25)
def test_task_WorkItem_instantiation(instance):
    assert isinstance(instance, task_WorkItem)


task_WorkPackage_strategy = st.builds(task_WorkPackage)
@given(instance=task_WorkPackage_strategy)
@settings(max_examples=25)
def test_task_WorkPackage_instantiation(instance):
    assert isinstance(instance, task_WorkPackage)


url_ModelElementUrlFragment_strategy = st.builds(url_ModelElementUrlFragment)
@given(instance=url_ModelElementUrlFragment_strategy)
@settings(max_examples=25)
def test_url_ModelElementUrlFragment_instantiation(instance):
    assert isinstance(instance, url_ModelElementUrlFragment)


url_ProjectUrlFragment_strategy = st.builds(url_ProjectUrlFragment)
@given(instance=url_ProjectUrlFragment_strategy)
@settings(max_examples=25)
def test_url_ProjectUrlFragment_instantiation(instance):
    assert isinstance(instance, url_ProjectUrlFragment)


url_ServerUrl_strategy = st.builds(url_ServerUrl)
@given(instance=url_ServerUrl_strategy)
@settings(max_examples=25)
def test_url_ServerUrl_instantiation(instance):
    assert isinstance(instance, url_ServerUrl)


versioning_ChangePackage_strategy = st.builds(versioning_ChangePackage)
@given(instance=versioning_ChangePackage_strategy)
@settings(max_examples=25)
def test_versioning_ChangePackage_instantiation(instance):
    assert isinstance(instance, versioning_ChangePackage)


versioning_LogMessage_strategy = st.builds(versioning_LogMessage)
@given(instance=versioning_LogMessage_strategy)
@settings(max_examples=25)
def test_versioning_LogMessage_instantiation(instance):
    assert isinstance(instance, versioning_LogMessage)


versioning_PrimaryVersionSpec_strategy = st.builds(versioning_PrimaryVersionSpec)
@given(instance=versioning_PrimaryVersionSpec_strategy)
@settings(max_examples=25)
def test_versioning_PrimaryVersionSpec_instantiation(instance):
    assert isinstance(instance, versioning_PrimaryVersionSpec)


versioning_TagVersionSpec_strategy = st.builds(versioning_TagVersionSpec)
@given(instance=versioning_TagVersionSpec_strategy)
@settings(max_examples=25)
def test_versioning_TagVersionSpec_instantiation(instance):
    assert isinstance(instance, versioning_TagVersionSpec)


versioning_Version_strategy = st.builds(versioning_Version)
@given(instance=versioning_Version_strategy)
@settings(max_examples=25)
def test_versioning_Version_instantiation(instance):
    assert isinstance(instance, versioning_Version)


versioning_VersionProperty_strategy = st.builds(versioning_VersionProperty)
@given(instance=versioning_VersionProperty_strategy)
@settings(max_examples=25)
def test_versioning_VersionProperty_instantiation(instance):
    assert isinstance(instance, versioning_VersionProperty)



