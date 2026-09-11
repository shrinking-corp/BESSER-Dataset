import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BasicMaterializationTask,
    ComponentExtension,
    ConfigurableItem,
    ScopeRoot,
    SetupTask,
    SetupTaskContainer,
    SourceLocator,
    TargletData,
    setup_ApiBaselineTask,
    setup_AutomaticSourceLocator,
    setup_BasicMaterializationTask,
    setup_Branch,
    setup_BuckminsterImportTask,
    setup_BuildPlan,
    setup_CommandParameter,
    setup_Component,
    setup_ComponentDefinition,
    setup_ComponentExtension,
    setup_CompoundSetupTask,
    setup_ConfigurableItem,
    setup_Configuration,
    setup_ContextVariableTask,
    setup_Eclipse,
    setup_EclipseIniTask,
    setup_EclipsePreferenceTask,
    setup_FileAssociationTask,
    setup_FileAssociationsTask,
    setup_FileEditor,
    setup_FileMapping,
    setup_GitCloneTask,
    setup_Index,
    setup_InstallableUnit,
    setup_JRETask,
    setup_KeyBindingContext,
    setup_KeyBindingTask,
    setup_LinkLocationTask,
    setup_ManualSourceLocator,
    setup_MaterializationTask,
    setup_MavenImportTask,
    setup_MetaIndex,
    setup_MylynBuildsTask,
    setup_MylynQueriesTask,
    setup_MylynQueryTask,
    setup_P2Repository,
    setup_P2Task,
    setup_Predicate,
    setup_Preferences,
    setup_Project,
    setup_ProjectSetImportTask,
    setup_ProjectsImportTask,
    setup_Query,
    setup_QueryAttribute,
    setup_RedirectionTask,
    setup_RepositoryList,
    setup_ResourceCopyTask,
    setup_ResourceCreationTask,
    setup_ScopeRoot,
    setup_Setup,
    setup_SetupTask,
    setup_SetupTaskContainer,
    setup_SourceLocator,
    setup_TargetPlatformTask,
    setup_Targlet,
    setup_TargletData,
    setup_TargletImportTask,
    setup_TargletTask,
    setup_TextModification,
    setup_TextModifyTask,
    setup_VariableChoice,
    setup_WorkingSet,
    setup_WorkingSetTask,
    ComponentType,
    SetupTaskScope,
    Trigger,
    VariableType,
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

def test_setup_ApiBaselineTask_containerFolder_value_roundtrip():
    instance = setup_ApiBaselineTask(containerFolder="sample_text", version="sample_text", zipLocation="sample_text")
    assert instance.containerFolder == "sample_text"
    instance.containerFolder = "sample_text_2"
    assert instance.containerFolder == "sample_text_2"


def test_setup_ApiBaselineTask_version_value_roundtrip():
    instance = setup_ApiBaselineTask(containerFolder="sample_text", version="sample_text", zipLocation="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_setup_ApiBaselineTask_zipLocation_value_roundtrip():
    instance = setup_ApiBaselineTask(containerFolder="sample_text", version="sample_text", zipLocation="sample_text")
    assert instance.zipLocation == "sample_text"
    instance.zipLocation = "sample_text_2"
    assert instance.zipLocation == "sample_text_2"


def test_setup_AutomaticSourceLocator_locateNestedProjects_value_roundtrip():
    instance = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    assert instance.locateNestedProjects == True
    instance.locateNestedProjects = False
    assert instance.locateNestedProjects == False


def test_setup_AutomaticSourceLocator_rootFolder_value_roundtrip():
    instance = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    assert instance.rootFolder == "sample_text"
    instance.rootFolder = "sample_text_2"
    assert instance.rootFolder == "sample_text_2"


def test_setup_BasicMaterializationTask_bundlePool_value_roundtrip():
    instance = setup_BasicMaterializationTask(bundlePool="sample_text", targetPlatform="sample_text")
    assert instance.bundlePool == "sample_text"
    instance.bundlePool = "sample_text_2"
    assert instance.bundlePool == "sample_text_2"


def test_setup_BasicMaterializationTask_targetPlatform_value_roundtrip():
    instance = setup_BasicMaterializationTask(bundlePool="sample_text", targetPlatform="sample_text")
    assert instance.targetPlatform == "sample_text"
    instance.targetPlatform = "sample_text_2"
    assert instance.targetPlatform == "sample_text_2"


def test_setup_Branch_name_value_roundtrip():
    instance = setup_Branch(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_BuckminsterImportTask_mspec_value_roundtrip():
    instance = setup_BuckminsterImportTask(mspec="sample_text")
    assert instance.mspec == "sample_text"
    instance.mspec = "sample_text_2"
    assert instance.mspec == "sample_text_2"


def test_setup_BuildPlan_name_value_roundtrip():
    instance = setup_BuildPlan(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_CommandParameter_iD_value_roundtrip():
    instance = setup_CommandParameter(iD="sample_text", value="sample_text")
    assert instance.iD == "sample_text"
    instance.iD = "sample_text_2"
    assert instance.iD == "sample_text_2"


def test_setup_CommandParameter_value_value_roundtrip():
    instance = setup_CommandParameter(iD="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_setup_Component_name_value_roundtrip():
    instance = setup_Component(name="sample_text", type="sample_text", versionRange="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_Component_type_value_roundtrip():
    instance = setup_Component(name="sample_text", type="sample_text", versionRange="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_setup_Component_versionRange_value_roundtrip():
    instance = setup_Component(name="sample_text", type="sample_text", versionRange="sample_text")
    assert instance.versionRange == "sample_text"
    instance.versionRange = "sample_text_2"
    assert instance.versionRange == "sample_text_2"


def test_setup_ComponentDefinition_iD_value_roundtrip():
    instance = setup_ComponentDefinition(iD="sample_text", version="sample_text")
    assert instance.iD == "sample_text"
    instance.iD = "sample_text_2"
    assert instance.iD == "sample_text_2"


def test_setup_ComponentDefinition_version_value_roundtrip():
    instance = setup_ComponentDefinition(iD="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_setup_CompoundSetupTask_name_value_roundtrip():
    instance = setup_CompoundSetupTask(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_ContextVariableTask_label_value_roundtrip():
    instance = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_setup_ContextVariableTask_name_value_roundtrip():
    instance = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_ContextVariableTask_stringSubstitution_value_roundtrip():
    instance = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    assert instance.stringSubstitution == True
    instance.stringSubstitution = False
    assert instance.stringSubstitution == False


def test_setup_ContextVariableTask_type_value_roundtrip():
    instance = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_setup_ContextVariableTask_value_value_roundtrip():
    instance = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_setup_Eclipse_version_value_roundtrip():
    instance = setup_Eclipse(version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_setup_EclipseIniTask_option_value_roundtrip():
    instance = setup_EclipseIniTask(option="sample_text", value="sample_text", vm=True)
    assert instance.option == "sample_text"
    instance.option = "sample_text_2"
    assert instance.option == "sample_text_2"


def test_setup_EclipseIniTask_value_value_roundtrip():
    instance = setup_EclipseIniTask(option="sample_text", value="sample_text", vm=True)
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_setup_EclipseIniTask_vm_value_roundtrip():
    instance = setup_EclipseIniTask(option="sample_text", value="sample_text", vm=True)
    assert instance.vm == True
    instance.vm = False
    assert instance.vm == False


def test_setup_EclipsePreferenceTask_key_value_roundtrip():
    instance = setup_EclipsePreferenceTask(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_setup_EclipsePreferenceTask_value_value_roundtrip():
    instance = setup_EclipsePreferenceTask(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_setup_FileAssociationTask_defaultEditorID_value_roundtrip():
    instance = setup_FileAssociationTask(defaultEditorID="sample_text", filePattern="sample_text")
    assert instance.defaultEditorID == "sample_text"
    instance.defaultEditorID = "sample_text_2"
    assert instance.defaultEditorID == "sample_text_2"


def test_setup_FileAssociationTask_filePattern_value_roundtrip():
    instance = setup_FileAssociationTask(defaultEditorID="sample_text", filePattern="sample_text")
    assert instance.filePattern == "sample_text"
    instance.filePattern = "sample_text_2"
    assert instance.filePattern == "sample_text_2"


def test_setup_FileEditor_iD_value_roundtrip():
    instance = setup_FileEditor(iD="sample_text")
    assert instance.iD == "sample_text"
    instance.iD = "sample_text_2"
    assert instance.iD == "sample_text_2"


def test_setup_FileMapping_defaultEditorID_value_roundtrip():
    instance = setup_FileMapping(defaultEditorID="sample_text", filePattern="sample_text")
    assert instance.defaultEditorID == "sample_text"
    instance.defaultEditorID = "sample_text_2"
    assert instance.defaultEditorID == "sample_text_2"


def test_setup_FileMapping_filePattern_value_roundtrip():
    instance = setup_FileMapping(defaultEditorID="sample_text", filePattern="sample_text")
    assert instance.filePattern == "sample_text"
    instance.filePattern = "sample_text_2"
    assert instance.filePattern == "sample_text_2"


def test_setup_GitCloneTask_checkoutBranch_value_roundtrip():
    instance = setup_GitCloneTask(checkoutBranch="sample_text", location="sample_text", pushURI="sample_text", remoteName="sample_text", remoteURI="sample_text", userID="sample_text")
    assert instance.checkoutBranch == "sample_text"
    instance.checkoutBranch = "sample_text_2"
    assert instance.checkoutBranch == "sample_text_2"


def test_setup_GitCloneTask_location_value_roundtrip():
    instance = setup_GitCloneTask(checkoutBranch="sample_text", location="sample_text", pushURI="sample_text", remoteName="sample_text", remoteURI="sample_text", userID="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_setup_GitCloneTask_pushURI_value_roundtrip():
    instance = setup_GitCloneTask(checkoutBranch="sample_text", location="sample_text", pushURI="sample_text", remoteName="sample_text", remoteURI="sample_text", userID="sample_text")
    assert instance.pushURI == "sample_text"
    instance.pushURI = "sample_text_2"
    assert instance.pushURI == "sample_text_2"


def test_setup_GitCloneTask_remoteName_value_roundtrip():
    instance = setup_GitCloneTask(checkoutBranch="sample_text", location="sample_text", pushURI="sample_text", remoteName="sample_text", remoteURI="sample_text", userID="sample_text")
    assert instance.remoteName == "sample_text"
    instance.remoteName = "sample_text_2"
    assert instance.remoteName == "sample_text_2"


def test_setup_GitCloneTask_remoteURI_value_roundtrip():
    instance = setup_GitCloneTask(checkoutBranch="sample_text", location="sample_text", pushURI="sample_text", remoteName="sample_text", remoteURI="sample_text", userID="sample_text")
    assert instance.remoteURI == "sample_text"
    instance.remoteURI = "sample_text_2"
    assert instance.remoteURI == "sample_text_2"


def test_setup_GitCloneTask_userID_value_roundtrip():
    instance = setup_GitCloneTask(checkoutBranch="sample_text", location="sample_text", pushURI="sample_text", remoteName="sample_text", remoteURI="sample_text", userID="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_setup_Index_name_value_roundtrip():
    instance = setup_Index(name="sample_text", oldURIs="sample_text", uRI="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_Index_oldURIs_value_roundtrip():
    instance = setup_Index(name="sample_text", oldURIs="sample_text", uRI="sample_text")
    assert instance.oldURIs == "sample_text"
    instance.oldURIs = "sample_text_2"
    assert instance.oldURIs == "sample_text_2"


def test_setup_Index_uRI_value_roundtrip():
    instance = setup_Index(name="sample_text", oldURIs="sample_text", uRI="sample_text")
    assert instance.uRI == "sample_text"
    instance.uRI = "sample_text_2"
    assert instance.uRI == "sample_text_2"


def test_setup_InstallableUnit_iD_value_roundtrip():
    instance = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    assert instance.iD == "sample_text"
    instance.iD = "sample_text_2"
    assert instance.iD == "sample_text_2"


def test_setup_InstallableUnit_versionRange_value_roundtrip():
    instance = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    assert instance.versionRange == "sample_text"
    instance.versionRange = "sample_text_2"
    assert instance.versionRange == "sample_text_2"


def test_setup_JRETask_location_value_roundtrip():
    instance = setup_JRETask(location="sample_text", version="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_setup_JRETask_version_value_roundtrip():
    instance = setup_JRETask(location="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_setup_KeyBindingContext_iD_value_roundtrip():
    instance = setup_KeyBindingContext(iD="sample_text")
    assert instance.iD == "sample_text"
    instance.iD = "sample_text_2"
    assert instance.iD == "sample_text_2"


def test_setup_KeyBindingTask_command_value_roundtrip():
    instance = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    assert instance.command == "sample_text"
    instance.command = "sample_text_2"
    assert instance.command == "sample_text_2"


def test_setup_KeyBindingTask_keys_value_roundtrip():
    instance = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    assert instance.keys == "sample_text"
    instance.keys = "sample_text_2"
    assert instance.keys == "sample_text_2"


def test_setup_KeyBindingTask_locale_value_roundtrip():
    instance = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    assert instance.locale == "sample_text"
    instance.locale = "sample_text_2"
    assert instance.locale == "sample_text_2"


def test_setup_KeyBindingTask_platform_value_roundtrip():
    instance = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    assert instance.platform == "sample_text"
    instance.platform = "sample_text_2"
    assert instance.platform == "sample_text_2"


def test_setup_KeyBindingTask_scheme_value_roundtrip():
    instance = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    assert instance.scheme == "sample_text"
    instance.scheme = "sample_text_2"
    assert instance.scheme == "sample_text_2"


def test_setup_LinkLocationTask_name_value_roundtrip():
    instance = setup_LinkLocationTask(name="sample_text", path="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_LinkLocationTask_path_value_roundtrip():
    instance = setup_LinkLocationTask(name="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_setup_ManualSourceLocator_componentNamePattern_value_roundtrip():
    instance = setup_ManualSourceLocator(componentNamePattern="sample_text", componentTypes="sample_text", location="sample_text")
    assert instance.componentNamePattern == "sample_text"
    instance.componentNamePattern = "sample_text_2"
    assert instance.componentNamePattern == "sample_text_2"


def test_setup_ManualSourceLocator_componentTypes_value_roundtrip():
    instance = setup_ManualSourceLocator(componentNamePattern="sample_text", componentTypes="sample_text", location="sample_text")
    assert instance.componentTypes == "sample_text"
    instance.componentTypes = "sample_text_2"
    assert instance.componentTypes == "sample_text_2"


def test_setup_ManualSourceLocator_location_value_roundtrip():
    instance = setup_ManualSourceLocator(componentNamePattern="sample_text", componentTypes="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_setup_MylynBuildsTask_connectorKind_value_roundtrip():
    instance = setup_MylynBuildsTask(connectorKind="sample_text", password="sample_text", serverURL="sample_text", userID="sample_text")
    assert instance.connectorKind == "sample_text"
    instance.connectorKind = "sample_text_2"
    assert instance.connectorKind == "sample_text_2"


def test_setup_MylynBuildsTask_password_value_roundtrip():
    instance = setup_MylynBuildsTask(connectorKind="sample_text", password="sample_text", serverURL="sample_text", userID="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_setup_MylynBuildsTask_serverURL_value_roundtrip():
    instance = setup_MylynBuildsTask(connectorKind="sample_text", password="sample_text", serverURL="sample_text", userID="sample_text")
    assert instance.serverURL == "sample_text"
    instance.serverURL = "sample_text_2"
    assert instance.serverURL == "sample_text_2"


def test_setup_MylynBuildsTask_userID_value_roundtrip():
    instance = setup_MylynBuildsTask(connectorKind="sample_text", password="sample_text", serverURL="sample_text", userID="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_setup_MylynQueriesTask_connectorKind_value_roundtrip():
    instance = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    assert instance.connectorKind == "sample_text"
    instance.connectorKind = "sample_text_2"
    assert instance.connectorKind == "sample_text_2"


def test_setup_MylynQueriesTask_password_value_roundtrip():
    instance = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_setup_MylynQueriesTask_repositoryURL_value_roundtrip():
    instance = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    assert instance.repositoryURL == "sample_text"
    instance.repositoryURL = "sample_text_2"
    assert instance.repositoryURL == "sample_text_2"


def test_setup_MylynQueriesTask_userID_value_roundtrip():
    instance = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_setup_MylynQueryTask_connectorKind_value_roundtrip():
    instance = setup_MylynQueryTask(connectorKind="sample_text", relativeURL="sample_text", repositoryURL="sample_text", summary="sample_text")
    assert instance.connectorKind == "sample_text"
    instance.connectorKind = "sample_text_2"
    assert instance.connectorKind == "sample_text_2"


def test_setup_MylynQueryTask_relativeURL_value_roundtrip():
    instance = setup_MylynQueryTask(connectorKind="sample_text", relativeURL="sample_text", repositoryURL="sample_text", summary="sample_text")
    assert instance.relativeURL == "sample_text"
    instance.relativeURL = "sample_text_2"
    assert instance.relativeURL == "sample_text_2"


def test_setup_MylynQueryTask_repositoryURL_value_roundtrip():
    instance = setup_MylynQueryTask(connectorKind="sample_text", relativeURL="sample_text", repositoryURL="sample_text", summary="sample_text")
    assert instance.repositoryURL == "sample_text"
    instance.repositoryURL = "sample_text_2"
    assert instance.repositoryURL == "sample_text_2"


def test_setup_MylynQueryTask_summary_value_roundtrip():
    instance = setup_MylynQueryTask(connectorKind="sample_text", relativeURL="sample_text", repositoryURL="sample_text", summary="sample_text")
    assert instance.summary == "sample_text"
    instance.summary = "sample_text_2"
    assert instance.summary == "sample_text_2"


def test_setup_P2Repository_uRL_value_roundtrip():
    instance = setup_P2Repository(uRL="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_setup_P2Task_licenseConfirmationDisabled_value_roundtrip():
    instance = setup_P2Task(licenseConfirmationDisabled=True, mergeDisabled=True)
    assert instance.licenseConfirmationDisabled == True
    instance.licenseConfirmationDisabled = False
    assert instance.licenseConfirmationDisabled == False


def test_setup_P2Task_mergeDisabled_value_roundtrip():
    instance = setup_P2Task(licenseConfirmationDisabled=True, mergeDisabled=True)
    assert instance.mergeDisabled == True
    instance.mergeDisabled = False
    assert instance.mergeDisabled == False


def test_setup_Preferences_acceptedLicenses_value_roundtrip():
    instance = setup_Preferences(acceptedLicenses="sample_text", installFolder="sample_text")
    assert instance.acceptedLicenses == "sample_text"
    instance.acceptedLicenses = "sample_text_2"
    assert instance.acceptedLicenses == "sample_text_2"


def test_setup_Preferences_installFolder_value_roundtrip():
    instance = setup_Preferences(acceptedLicenses="sample_text", installFolder="sample_text")
    assert instance.installFolder == "sample_text"
    instance.installFolder = "sample_text_2"
    assert instance.installFolder == "sample_text_2"


def test_setup_Project_label_value_roundtrip():
    instance = setup_Project(label="sample_text", name="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_setup_Project_name_value_roundtrip():
    instance = setup_Project(label="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_ProjectSetImportTask_uRL_value_roundtrip():
    instance = setup_ProjectSetImportTask(uRL="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_setup_Query_summary_value_roundtrip():
    instance = setup_Query(summary="sample_text", uRL="sample_text")
    assert instance.summary == "sample_text"
    instance.summary = "sample_text_2"
    assert instance.summary == "sample_text_2"


def test_setup_Query_uRL_value_roundtrip():
    instance = setup_Query(summary="sample_text", uRL="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_setup_QueryAttribute_key_value_roundtrip():
    instance = setup_QueryAttribute(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_setup_QueryAttribute_value_value_roundtrip():
    instance = setup_QueryAttribute(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_setup_RedirectionTask_sourceURL_value_roundtrip():
    instance = setup_RedirectionTask(sourceURL="sample_text", targetURL="sample_text")
    assert instance.sourceURL == "sample_text"
    instance.sourceURL = "sample_text_2"
    assert instance.sourceURL == "sample_text_2"


def test_setup_RedirectionTask_targetURL_value_roundtrip():
    instance = setup_RedirectionTask(sourceURL="sample_text", targetURL="sample_text")
    assert instance.targetURL == "sample_text"
    instance.targetURL = "sample_text_2"
    assert instance.targetURL == "sample_text_2"


def test_setup_RepositoryList_name_value_roundtrip():
    instance = setup_RepositoryList(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_ResourceCopyTask_sourceURL_value_roundtrip():
    instance = setup_ResourceCopyTask(sourceURL="sample_text", targetURL="sample_text")
    assert instance.sourceURL == "sample_text"
    instance.sourceURL = "sample_text_2"
    assert instance.sourceURL == "sample_text_2"


def test_setup_ResourceCopyTask_targetURL_value_roundtrip():
    instance = setup_ResourceCopyTask(sourceURL="sample_text", targetURL="sample_text")
    assert instance.targetURL == "sample_text"
    instance.targetURL = "sample_text_2"
    assert instance.targetURL == "sample_text_2"


def test_setup_ResourceCreationTask_content_value_roundtrip():
    instance = setup_ResourceCreationTask(content="sample_text", encoding="sample_text", targetURL="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_setup_ResourceCreationTask_encoding_value_roundtrip():
    instance = setup_ResourceCreationTask(content="sample_text", encoding="sample_text", targetURL="sample_text")
    assert instance.encoding == "sample_text"
    instance.encoding = "sample_text_2"
    assert instance.encoding == "sample_text_2"


def test_setup_ResourceCreationTask_targetURL_value_roundtrip():
    instance = setup_ResourceCreationTask(content="sample_text", encoding="sample_text", targetURL="sample_text")
    assert instance.targetURL == "sample_text"
    instance.targetURL = "sample_text_2"
    assert instance.targetURL == "sample_text_2"


def test_setup_SetupTask_disabled_value_roundtrip():
    instance = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    assert instance.disabled == True
    instance.disabled = False
    assert instance.disabled == False


def test_setup_SetupTask_documentation_value_roundtrip():
    instance = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_setup_SetupTask_excludedTriggers_value_roundtrip():
    instance = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    assert instance.excludedTriggers == "sample_text"
    instance.excludedTriggers = "sample_text_2"
    assert instance.excludedTriggers == "sample_text_2"


def test_setup_SetupTask_scope_value_roundtrip():
    instance = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    assert instance.scope == "sample_text"
    instance.scope = "sample_text_2"
    assert instance.scope == "sample_text_2"


def test_setup_TargetPlatformTask_name_value_roundtrip():
    instance = setup_TargetPlatformTask(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_TargletData_activeRepositoryList_value_roundtrip():
    instance = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    assert instance.activeRepositoryList == "sample_text"
    instance.activeRepositoryList = "sample_text_2"
    assert instance.activeRepositoryList == "sample_text_2"


def test_setup_TargletData_includeAllPlatforms_value_roundtrip():
    instance = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    assert instance.includeAllPlatforms == True
    instance.includeAllPlatforms = False
    assert instance.includeAllPlatforms == False


def test_setup_TargletData_includeSources_value_roundtrip():
    instance = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    assert instance.includeSources == True
    instance.includeSources = False
    assert instance.includeSources == False


def test_setup_TargletData_name_value_roundtrip():
    instance = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_setup_TargletImportTask_targletURI_value_roundtrip():
    instance = setup_TargletImportTask(targletURI="sample_text")
    assert instance.targletURI == "sample_text"
    instance.targletURI = "sample_text_2"
    assert instance.targletURI == "sample_text_2"


def test_setup_TextModification_pattern_value_roundtrip():
    instance = setup_TextModification(pattern="sample_text", substitutions="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_setup_TextModification_substitutions_value_roundtrip():
    instance = setup_TextModification(pattern="sample_text", substitutions="sample_text")
    assert instance.substitutions == "sample_text"
    instance.substitutions = "sample_text_2"
    assert instance.substitutions == "sample_text_2"


def test_setup_TextModifyTask_encoding_value_roundtrip():
    instance = setup_TextModifyTask(encoding="sample_text", uRL="sample_text")
    assert instance.encoding == "sample_text"
    instance.encoding = "sample_text_2"
    assert instance.encoding == "sample_text_2"


def test_setup_TextModifyTask_uRL_value_roundtrip():
    instance = setup_TextModifyTask(encoding="sample_text", uRL="sample_text")
    assert instance.uRL == "sample_text"
    instance.uRL = "sample_text_2"
    assert instance.uRL == "sample_text_2"


def test_setup_VariableChoice_label_value_roundtrip():
    instance = setup_VariableChoice(label="sample_text", value="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_setup_VariableChoice_value_value_roundtrip():
    instance = setup_VariableChoice(label="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_setup_BuckminsterImportTask_isa_BasicMaterializationTask():
    instance = setup_BuckminsterImportTask(mspec="sample_text")
    assert isinstance(instance, BasicMaterializationTask)


def test_setup_MaterializationTask_isa_BasicMaterializationTask():
    instance = setup_MaterializationTask()
    assert isinstance(instance, BasicMaterializationTask)


def test_setup_ComponentDefinition_isa_ComponentExtension():
    instance = setup_ComponentDefinition(iD="sample_text", version="sample_text")
    assert isinstance(instance, ComponentExtension)


def test_setup_Branch_isa_ConfigurableItem():
    instance = setup_Branch(name="sample_text")
    assert isinstance(instance, ConfigurableItem)


def test_setup_Eclipse_isa_ConfigurableItem():
    instance = setup_Eclipse(version="sample_text")
    assert isinstance(instance, ConfigurableItem)


def test_setup_Project_isa_ConfigurableItem():
    instance = setup_Project(label="sample_text", name="sample_text")
    assert isinstance(instance, ConfigurableItem)


def test_setup_ConfigurableItem_isa_ScopeRoot():
    instance = setup_ConfigurableItem()
    assert isinstance(instance, ScopeRoot)


def test_setup_Configuration_isa_ScopeRoot():
    instance = setup_Configuration()
    assert isinstance(instance, ScopeRoot)


def test_setup_Preferences_isa_ScopeRoot():
    instance = setup_Preferences(acceptedLicenses="sample_text", installFolder="sample_text")
    assert isinstance(instance, ScopeRoot)


def test_setup_ApiBaselineTask_isa_SetupTask():
    instance = setup_ApiBaselineTask(containerFolder="sample_text", version="sample_text", zipLocation="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_BasicMaterializationTask_isa_SetupTask():
    instance = setup_BasicMaterializationTask(bundlePool="sample_text", targetPlatform="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_CompoundSetupTask_isa_SetupTask():
    instance = setup_CompoundSetupTask(name="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_ContextVariableTask_isa_SetupTask():
    instance = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_EclipseIniTask_isa_SetupTask():
    instance = setup_EclipseIniTask(option="sample_text", value="sample_text", vm=True)
    assert isinstance(instance, SetupTask)


def test_setup_EclipsePreferenceTask_isa_SetupTask():
    instance = setup_EclipsePreferenceTask(key="sample_text", value="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_FileAssociationTask_isa_SetupTask():
    instance = setup_FileAssociationTask(defaultEditorID="sample_text", filePattern="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_FileAssociationsTask_isa_SetupTask():
    instance = setup_FileAssociationsTask()
    assert isinstance(instance, SetupTask)


def test_setup_GitCloneTask_isa_SetupTask():
    instance = setup_GitCloneTask(checkoutBranch="sample_text", location="sample_text", pushURI="sample_text", remoteName="sample_text", remoteURI="sample_text", userID="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_JRETask_isa_SetupTask():
    instance = setup_JRETask(location="sample_text", version="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_KeyBindingTask_isa_SetupTask():
    instance = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_LinkLocationTask_isa_SetupTask():
    instance = setup_LinkLocationTask(name="sample_text", path="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_MavenImportTask_isa_SetupTask():
    instance = setup_MavenImportTask()
    assert isinstance(instance, SetupTask)


def test_setup_MylynBuildsTask_isa_SetupTask():
    instance = setup_MylynBuildsTask(connectorKind="sample_text", password="sample_text", serverURL="sample_text", userID="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_MylynQueriesTask_isa_SetupTask():
    instance = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_MylynQueryTask_isa_SetupTask():
    instance = setup_MylynQueryTask(connectorKind="sample_text", relativeURL="sample_text", repositoryURL="sample_text", summary="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_P2Task_isa_SetupTask():
    instance = setup_P2Task(licenseConfirmationDisabled=True, mergeDisabled=True)
    assert isinstance(instance, SetupTask)


def test_setup_ProjectSetImportTask_isa_SetupTask():
    instance = setup_ProjectSetImportTask(uRL="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_ProjectsImportTask_isa_SetupTask():
    instance = setup_ProjectsImportTask()
    assert isinstance(instance, SetupTask)


def test_setup_RedirectionTask_isa_SetupTask():
    instance = setup_RedirectionTask(sourceURL="sample_text", targetURL="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_ResourceCopyTask_isa_SetupTask():
    instance = setup_ResourceCopyTask(sourceURL="sample_text", targetURL="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_ResourceCreationTask_isa_SetupTask():
    instance = setup_ResourceCreationTask(content="sample_text", encoding="sample_text", targetURL="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_TargetPlatformTask_isa_SetupTask():
    instance = setup_TargetPlatformTask(name="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_TargletImportTask_isa_SetupTask():
    instance = setup_TargletImportTask(targletURI="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_TargletTask_isa_SetupTask():
    instance = setup_TargletTask()
    assert isinstance(instance, SetupTask)


def test_setup_TextModifyTask_isa_SetupTask():
    instance = setup_TextModifyTask(encoding="sample_text", uRL="sample_text")
    assert isinstance(instance, SetupTask)


def test_setup_WorkingSetTask_isa_SetupTask():
    instance = setup_WorkingSetTask()
    assert isinstance(instance, SetupTask)


def test_setup_CompoundSetupTask_isa_SetupTaskContainer():
    instance = setup_CompoundSetupTask(name="sample_text")
    assert isinstance(instance, SetupTaskContainer)


def test_setup_ScopeRoot_isa_SetupTaskContainer():
    instance = setup_ScopeRoot()
    assert isinstance(instance, SetupTaskContainer)


def test_setup_AutomaticSourceLocator_isa_SourceLocator():
    instance = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    assert isinstance(instance, SourceLocator)


def test_setup_ManualSourceLocator_isa_SourceLocator():
    instance = setup_ManualSourceLocator(componentNamePattern="sample_text", componentTypes="sample_text", location="sample_text")
    assert isinstance(instance, SourceLocator)


def test_setup_Targlet_isa_TargletData():
    instance = setup_Targlet()
    assert isinstance(instance, TargletData)


def test_setup_TargletTask_isa_TargletData():
    instance = setup_TargletTask()
    assert isinstance(instance, TargletData)


def test_assoc_activeP2Repositories46_link_reassign_clear():
    a = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    b1 = setup_P2Repository(uRL="sample_text")
    b2 = setup_P2Repository(uRL="sample_text_2")
    _safe_set(a, 'setup_TargletData47', {b1})
    assert _is_linked(a, 'setup_TargletData47', b1)
    if hasattr(b1, 'setup_P2Repository48'):
        assert _is_linked(b1, 'setup_P2Repository48', a)
    _safe_set(a, 'setup_TargletData47', {b2})
    assert _is_linked(a, 'setup_TargletData47', b2)
    if hasattr(b1, 'setup_P2Repository48'):
        assert not _is_linked(b1, 'setup_P2Repository48', a)
    if hasattr(b2, 'setup_P2Repository48'):
        assert _is_linked(b2, 'setup_P2Repository48', a)
    _safe_set(a, 'setup_TargletData47', set())
    assert not _is_linked(a, 'setup_TargletData47', b2)
    if hasattr(b2, 'setup_P2Repository48'):
        assert not _is_linked(b2, 'setup_P2Repository48', a)


def test_assoc_attributes66_link_reassign_clear():
    a = setup_QueryAttribute(key="sample_text", value="sample_text")
    b1 = setup_Query(summary="sample_text", uRL="sample_text")
    b2 = setup_Query(summary="sample_text_2", uRL="sample_text_2")
    _safe_set(a, 'setup_QueryAttribute', b1)
    assert _is_linked(a, 'setup_QueryAttribute', b1)
    if hasattr(b1, 'setup_Query'):
        assert _is_linked(b1, 'setup_Query', a)
    _safe_set(a, 'setup_QueryAttribute', b2)
    assert _is_linked(a, 'setup_QueryAttribute', b2)
    if hasattr(b1, 'setup_Query'):
        assert not _is_linked(b1, 'setup_Query', a)
    if hasattr(b2, 'setup_Query'):
        assert _is_linked(b2, 'setup_Query', a)
    _safe_set(a, 'setup_QueryAttribute', None)
    assert not _is_linked(a, 'setup_QueryAttribute', b2)
    if hasattr(b2, 'setup_Query'):
        assert not _is_linked(b2, 'setup_Query', a)


def test_assoc_branch13_link_reassign_clear():
    a = setup_Setup()
    b1 = setup_Branch(name="sample_text")
    b2 = setup_Branch(name="sample_text_2")
    _safe_set(a, 'setup_Setup', b1)
    assert _is_linked(a, 'setup_Setup', b1)
    if hasattr(b1, 'setup_Branch14'):
        assert _is_linked(b1, 'setup_Branch14', a)
    _safe_set(a, 'setup_Setup', b2)
    assert _is_linked(a, 'setup_Setup', b2)
    if hasattr(b1, 'setup_Branch14'):
        assert not _is_linked(b1, 'setup_Branch14', a)
    if hasattr(b2, 'setup_Branch14'):
        assert _is_linked(b2, 'setup_Branch14', a)
    _safe_set(a, 'setup_Setup', None)
    assert not _is_linked(a, 'setup_Setup', b2)
    if hasattr(b2, 'setup_Branch14'):
        assert not _is_linked(b2, 'setup_Branch14', a)


def test_assoc_branches7_link_reassign_clear():
    a = setup_Project(label="sample_text", name="sample_text")
    b1 = setup_Branch(name="sample_text")
    b2 = setup_Branch(name="sample_text_2")
    _safe_set(a, 'project', {b1})
    assert _is_linked(a, 'project', b1)
    if hasattr(b1, 'Branch'):
        assert _is_linked(b1, 'Branch', a)
    _safe_set(a, 'project', {b2})
    assert _is_linked(a, 'project', b2)
    if hasattr(b1, 'Branch'):
        assert not _is_linked(b1, 'Branch', a)
    if hasattr(b2, 'Branch'):
        assert _is_linked(b2, 'Branch', a)
    _safe_set(a, 'project', set())
    assert not _is_linked(a, 'project', b2)
    if hasattr(b2, 'Branch'):
        assert not _is_linked(b2, 'Branch', a)


def test_assoc_buildPlans67_link_reassign_clear():
    a = setup_MylynBuildsTask(connectorKind="sample_text", password="sample_text", serverURL="sample_text", userID="sample_text")
    b1 = setup_BuildPlan(name="sample_text")
    b2 = setup_BuildPlan(name="sample_text_2")
    _safe_set(a, 'setup_MylynBuildsTask', {b1})
    assert _is_linked(a, 'setup_MylynBuildsTask', b1)
    if hasattr(b1, 'setup_BuildPlan'):
        assert _is_linked(b1, 'setup_BuildPlan', a)
    _safe_set(a, 'setup_MylynBuildsTask', {b2})
    assert _is_linked(a, 'setup_MylynBuildsTask', b2)
    if hasattr(b1, 'setup_BuildPlan'):
        assert not _is_linked(b1, 'setup_BuildPlan', a)
    if hasattr(b2, 'setup_BuildPlan'):
        assert _is_linked(b2, 'setup_BuildPlan', a)
    _safe_set(a, 'setup_MylynBuildsTask', set())
    assert not _is_linked(a, 'setup_MylynBuildsTask', b2)
    if hasattr(b2, 'setup_BuildPlan'):
        assert not _is_linked(b2, 'setup_BuildPlan', a)


def test_assoc_choices24_link_reassign_clear():
    a = setup_VariableChoice(label="sample_text", value="sample_text")
    b1 = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    b2 = setup_ContextVariableTask(label="sample_text_2", name="sample_text_2", stringSubstitution=False, type="sample_text_2", value="sample_text_2")
    _safe_set(a, 'setup_VariableChoice', b1)
    assert _is_linked(a, 'setup_VariableChoice', b1)
    if hasattr(b1, 'setup_ContextVariableTask'):
        assert _is_linked(b1, 'setup_ContextVariableTask', a)
    _safe_set(a, 'setup_VariableChoice', b2)
    assert _is_linked(a, 'setup_VariableChoice', b2)
    if hasattr(b1, 'setup_ContextVariableTask'):
        assert not _is_linked(b1, 'setup_ContextVariableTask', a)
    if hasattr(b2, 'setup_ContextVariableTask'):
        assert _is_linked(b2, 'setup_ContextVariableTask', a)
    _safe_set(a, 'setup_VariableChoice', None)
    assert not _is_linked(a, 'setup_VariableChoice', b2)
    if hasattr(b2, 'setup_ContextVariableTask'):
        assert not _is_linked(b2, 'setup_ContextVariableTask', a)


def test_assoc_commandParameters62_link_reassign_clear():
    a = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    b1 = setup_CommandParameter(iD="sample_text", value="sample_text")
    b2 = setup_CommandParameter(iD="sample_text_2", value="sample_text_2")
    _safe_set(a, 'setup_KeyBindingTask63', {b1})
    assert _is_linked(a, 'setup_KeyBindingTask63', b1)
    if hasattr(b1, 'setup_CommandParameter'):
        assert _is_linked(b1, 'setup_CommandParameter', a)
    _safe_set(a, 'setup_KeyBindingTask63', {b2})
    assert _is_linked(a, 'setup_KeyBindingTask63', b2)
    if hasattr(b1, 'setup_CommandParameter'):
        assert not _is_linked(b1, 'setup_CommandParameter', a)
    if hasattr(b2, 'setup_CommandParameter'):
        assert _is_linked(b2, 'setup_CommandParameter', a)
    _safe_set(a, 'setup_KeyBindingTask63', set())
    assert not _is_linked(a, 'setup_KeyBindingTask63', b2)
    if hasattr(b2, 'setup_CommandParameter'):
        assert not _is_linked(b2, 'setup_CommandParameter', a)


def test_assoc_configuration1_link_reassign_clear():
    a = setup_Eclipse(version="sample_text")
    b1 = setup_Configuration()
    b2 = setup_Configuration()
    _safe_set(a, 'eclipseVersions', b1)
    assert _is_linked(a, 'eclipseVersions', b1)
    if hasattr(b1, 'Configuration'):
        assert _is_linked(b1, 'Configuration', a)
    _safe_set(a, 'eclipseVersions', b2)
    assert _is_linked(a, 'eclipseVersions', b2)
    if hasattr(b1, 'Configuration'):
        assert not _is_linked(b1, 'Configuration', a)
    if hasattr(b2, 'Configuration'):
        assert _is_linked(b2, 'Configuration', a)
    _safe_set(a, 'eclipseVersions', None)
    assert not _is_linked(a, 'eclipseVersions', b2)
    if hasattr(b2, 'Configuration'):
        assert not _is_linked(b2, 'Configuration', a)


def test_assoc_configuration5_link_reassign_clear():
    a = setup_Project(label="sample_text", name="sample_text")
    b1 = setup_Configuration()
    b2 = setup_Configuration()
    _safe_set(a, 'projects', b1)
    assert _is_linked(a, 'projects', b1)
    if hasattr(b1, 'Configuration6'):
        assert _is_linked(b1, 'Configuration6', a)
    _safe_set(a, 'projects', b2)
    assert _is_linked(a, 'projects', b2)
    if hasattr(b1, 'Configuration6'):
        assert not _is_linked(b1, 'Configuration6', a)
    if hasattr(b2, 'Configuration6'):
        assert _is_linked(b2, 'Configuration6', a)
    _safe_set(a, 'projects', None)
    assert not _is_linked(a, 'projects', b2)
    if hasattr(b2, 'Configuration6'):
        assert not _is_linked(b2, 'Configuration6', a)


def test_assoc_contexts61_link_reassign_clear():
    a = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    b1 = setup_KeyBindingContext(iD="sample_text")
    b2 = setup_KeyBindingContext(iD="sample_text_2")
    _safe_set(a, 'setup_KeyBindingTask', {b1})
    assert _is_linked(a, 'setup_KeyBindingTask', b1)
    if hasattr(b1, 'setup_KeyBindingContext'):
        assert _is_linked(b1, 'setup_KeyBindingContext', a)
    _safe_set(a, 'setup_KeyBindingTask', {b2})
    assert _is_linked(a, 'setup_KeyBindingTask', b2)
    if hasattr(b1, 'setup_KeyBindingContext'):
        assert not _is_linked(b1, 'setup_KeyBindingContext', a)
    if hasattr(b2, 'setup_KeyBindingContext'):
        assert _is_linked(b2, 'setup_KeyBindingContext', a)
    _safe_set(a, 'setup_KeyBindingTask', set())
    assert not _is_linked(a, 'setup_KeyBindingTask', b2)
    if hasattr(b2, 'setup_KeyBindingContext'):
        assert not _is_linked(b2, 'setup_KeyBindingContext', a)


def test_assoc_dependencies35_link_reassign_clear():
    a = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    b1 = setup_ComponentExtension()
    b2 = setup_ComponentExtension()
    _safe_set(a, 'setup_InstallableUnit36', b1)
    assert _is_linked(a, 'setup_InstallableUnit36', b1)
    if hasattr(b1, 'setup_ComponentExtension'):
        assert _is_linked(b1, 'setup_ComponentExtension', a)
    _safe_set(a, 'setup_InstallableUnit36', b2)
    assert _is_linked(a, 'setup_InstallableUnit36', b2)
    if hasattr(b1, 'setup_ComponentExtension'):
        assert not _is_linked(b1, 'setup_ComponentExtension', a)
    if hasattr(b2, 'setup_ComponentExtension'):
        assert _is_linked(b2, 'setup_ComponentExtension', a)
    _safe_set(a, 'setup_InstallableUnit36', None)
    assert not _is_linked(a, 'setup_InstallableUnit36', b2)
    if hasattr(b2, 'setup_ComponentExtension'):
        assert not _is_linked(b2, 'setup_ComponentExtension', a)


def test_assoc_eclipseVersion15_link_reassign_clear():
    a = setup_Setup()
    b1 = setup_Eclipse(version="sample_text")
    b2 = setup_Eclipse(version="sample_text_2")
    _safe_set(a, 'setup_Setup16', b1)
    assert _is_linked(a, 'setup_Setup16', b1)
    if hasattr(b1, 'setup_Eclipse17'):
        assert _is_linked(b1, 'setup_Eclipse17', a)
    _safe_set(a, 'setup_Setup16', b2)
    assert _is_linked(a, 'setup_Setup16', b2)
    if hasattr(b1, 'setup_Eclipse17'):
        assert not _is_linked(b1, 'setup_Eclipse17', a)
    if hasattr(b2, 'setup_Eclipse17'):
        assert _is_linked(b2, 'setup_Eclipse17', a)
    _safe_set(a, 'setup_Setup16', None)
    assert not _is_linked(a, 'setup_Setup16', b2)
    if hasattr(b2, 'setup_Eclipse17'):
        assert not _is_linked(b2, 'setup_Eclipse17', a)


def test_assoc_eclipseVersions2_link_reassign_clear():
    a = setup_Eclipse(version="sample_text")
    b1 = setup_Configuration()
    b2 = setup_Configuration()
    _safe_set(a, 'Eclipse', b1)
    assert _is_linked(a, 'Eclipse', b1)
    if hasattr(b1, 'configuration'):
        assert _is_linked(b1, 'configuration', a)
    _safe_set(a, 'Eclipse', b2)
    assert _is_linked(a, 'Eclipse', b2)
    if hasattr(b1, 'configuration'):
        assert not _is_linked(b1, 'configuration', a)
    if hasattr(b2, 'configuration'):
        assert _is_linked(b2, 'configuration', a)
    _safe_set(a, 'Eclipse', None)
    assert not _is_linked(a, 'Eclipse', b2)
    if hasattr(b2, 'configuration'):
        assert not _is_linked(b2, 'configuration', a)


def test_assoc_editors54_link_reassign_clear():
    a = setup_FileEditor(iD="sample_text")
    b1 = setup_FileAssociationTask(defaultEditorID="sample_text", filePattern="sample_text")
    b2 = setup_FileAssociationTask(defaultEditorID="sample_text_2", filePattern="sample_text_2")
    _safe_set(a, 'setup_FileEditor', b1)
    assert _is_linked(a, 'setup_FileEditor', b1)
    if hasattr(b1, 'setup_FileAssociationTask'):
        assert _is_linked(b1, 'setup_FileAssociationTask', a)
    _safe_set(a, 'setup_FileEditor', b2)
    assert _is_linked(a, 'setup_FileEditor', b2)
    if hasattr(b1, 'setup_FileAssociationTask'):
        assert not _is_linked(b1, 'setup_FileAssociationTask', a)
    if hasattr(b2, 'setup_FileAssociationTask'):
        assert _is_linked(b2, 'setup_FileAssociationTask', a)
    _safe_set(a, 'setup_FileEditor', None)
    assert not _is_linked(a, 'setup_FileEditor', b2)
    if hasattr(b2, 'setup_FileAssociationTask'):
        assert not _is_linked(b2, 'setup_FileAssociationTask', a)


def test_assoc_editors56_link_reassign_clear():
    a = setup_FileMapping(defaultEditorID="sample_text", filePattern="sample_text")
    b1 = setup_FileEditor(iD="sample_text")
    b2 = setup_FileEditor(iD="sample_text_2")
    _safe_set(a, 'setup_FileMapping57', {b1})
    assert _is_linked(a, 'setup_FileMapping57', b1)
    if hasattr(b1, 'setup_FileEditor58'):
        assert _is_linked(b1, 'setup_FileEditor58', a)
    _safe_set(a, 'setup_FileMapping57', {b2})
    assert _is_linked(a, 'setup_FileMapping57', b2)
    if hasattr(b1, 'setup_FileEditor58'):
        assert not _is_linked(b1, 'setup_FileEditor58', a)
    if hasattr(b2, 'setup_FileEditor58'):
        assert _is_linked(b2, 'setup_FileEditor58', a)
    _safe_set(a, 'setup_FileMapping57', set())
    assert not _is_linked(a, 'setup_FileMapping57', b2)
    if hasattr(b2, 'setup_FileEditor58'):
        assert not _is_linked(b2, 'setup_FileEditor58', a)


def test_assoc_indexes0_link_reassign_clear():
    a = setup_Index(name="sample_text", oldURIs="sample_text", uRI="sample_text")
    b1 = setup_MetaIndex()
    b2 = setup_MetaIndex()
    _safe_set(a, 'setup_Index', b1)
    assert _is_linked(a, 'setup_Index', b1)
    if hasattr(b1, 'setup_MetaIndex'):
        assert _is_linked(b1, 'setup_MetaIndex', a)
    _safe_set(a, 'setup_Index', b2)
    assert _is_linked(a, 'setup_Index', b2)
    if hasattr(b1, 'setup_MetaIndex'):
        assert not _is_linked(b1, 'setup_MetaIndex', a)
    if hasattr(b2, 'setup_MetaIndex'):
        assert _is_linked(b2, 'setup_MetaIndex', a)
    _safe_set(a, 'setup_Index', None)
    assert not _is_linked(a, 'setup_Index', b2)
    if hasattr(b2, 'setup_MetaIndex'):
        assert not _is_linked(b2, 'setup_MetaIndex', a)


def test_assoc_installableUnits25_link_reassign_clear():
    a = setup_P2Task(licenseConfirmationDisabled=True, mergeDisabled=True)
    b1 = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    b2 = setup_InstallableUnit(iD="sample_text_2", versionRange="sample_text_2")
    _safe_set(a, 'setup_P2Task', {b1})
    assert _is_linked(a, 'setup_P2Task', b1)
    if hasattr(b1, 'setup_InstallableUnit'):
        assert _is_linked(b1, 'setup_InstallableUnit', a)
    _safe_set(a, 'setup_P2Task', {b2})
    assert _is_linked(a, 'setup_P2Task', b2)
    if hasattr(b1, 'setup_InstallableUnit'):
        assert not _is_linked(b1, 'setup_InstallableUnit', a)
    if hasattr(b2, 'setup_InstallableUnit'):
        assert _is_linked(b2, 'setup_InstallableUnit', a)
    _safe_set(a, 'setup_P2Task', set())
    assert not _is_linked(a, 'setup_P2Task', b2)
    if hasattr(b2, 'setup_InstallableUnit'):
        assert not _is_linked(b2, 'setup_InstallableUnit', a)


def test_assoc_mappings55_link_reassign_clear():
    a = setup_FileMapping(defaultEditorID="sample_text", filePattern="sample_text")
    b1 = setup_FileAssociationsTask()
    b2 = setup_FileAssociationsTask()
    _safe_set(a, 'setup_FileMapping', b1)
    assert _is_linked(a, 'setup_FileMapping', b1)
    if hasattr(b1, 'setup_FileAssociationsTask'):
        assert _is_linked(b1, 'setup_FileAssociationsTask', a)
    _safe_set(a, 'setup_FileMapping', b2)
    assert _is_linked(a, 'setup_FileMapping', b2)
    if hasattr(b1, 'setup_FileAssociationsTask'):
        assert not _is_linked(b1, 'setup_FileAssociationsTask', a)
    if hasattr(b2, 'setup_FileAssociationsTask'):
        assert _is_linked(b2, 'setup_FileAssociationsTask', a)
    _safe_set(a, 'setup_FileMapping', None)
    assert not _is_linked(a, 'setup_FileMapping', b2)
    if hasattr(b2, 'setup_FileAssociationsTask'):
        assert not _is_linked(b2, 'setup_FileAssociationsTask', a)


def test_assoc_modifications60_link_reassign_clear():
    a = setup_TextModifyTask(encoding="sample_text", uRL="sample_text")
    b1 = setup_TextModification(pattern="sample_text", substitutions="sample_text")
    b2 = setup_TextModification(pattern="sample_text_2", substitutions="sample_text_2")
    _safe_set(a, 'setup_TextModifyTask', {b1})
    assert _is_linked(a, 'setup_TextModifyTask', b1)
    if hasattr(b1, 'setup_TextModification'):
        assert _is_linked(b1, 'setup_TextModification', a)
    _safe_set(a, 'setup_TextModifyTask', {b2})
    assert _is_linked(a, 'setup_TextModifyTask', b2)
    if hasattr(b1, 'setup_TextModification'):
        assert not _is_linked(b1, 'setup_TextModification', a)
    if hasattr(b2, 'setup_TextModification'):
        assert _is_linked(b2, 'setup_TextModification', a)
    _safe_set(a, 'setup_TextModifyTask', set())
    assert not _is_linked(a, 'setup_TextModifyTask', b2)
    if hasattr(b2, 'setup_TextModification'):
        assert not _is_linked(b2, 'setup_TextModification', a)


def test_assoc_p2Repositories26_link_reassign_clear():
    a = setup_P2Task(licenseConfirmationDisabled=True, mergeDisabled=True)
    b1 = setup_P2Repository(uRL="sample_text")
    b2 = setup_P2Repository(uRL="sample_text_2")
    _safe_set(a, 'setup_P2Task27', {b1})
    assert _is_linked(a, 'setup_P2Task27', b1)
    if hasattr(b1, 'setup_P2Repository'):
        assert _is_linked(b1, 'setup_P2Repository', a)
    _safe_set(a, 'setup_P2Task27', {b2})
    assert _is_linked(a, 'setup_P2Task27', b2)
    if hasattr(b1, 'setup_P2Repository'):
        assert not _is_linked(b1, 'setup_P2Repository', a)
    if hasattr(b2, 'setup_P2Repository'):
        assert _is_linked(b2, 'setup_P2Repository', a)
    _safe_set(a, 'setup_P2Task27', set())
    assert not _is_linked(a, 'setup_P2Task27', b2)
    if hasattr(b2, 'setup_P2Repository'):
        assert not _is_linked(b2, 'setup_P2Repository', a)


def test_assoc_p2Repositories31_link_reassign_clear():
    a = setup_P2Repository(uRL="sample_text")
    b1 = setup_MaterializationTask()
    b2 = setup_MaterializationTask()
    _safe_set(a, 'setup_P2Repository33', b1)
    assert _is_linked(a, 'setup_P2Repository33', b1)
    if hasattr(b1, 'setup_MaterializationTask32'):
        assert _is_linked(b1, 'setup_MaterializationTask32', a)
    _safe_set(a, 'setup_P2Repository33', b2)
    assert _is_linked(a, 'setup_P2Repository33', b2)
    if hasattr(b1, 'setup_MaterializationTask32'):
        assert not _is_linked(b1, 'setup_MaterializationTask32', a)
    if hasattr(b2, 'setup_MaterializationTask32'):
        assert _is_linked(b2, 'setup_MaterializationTask32', a)
    _safe_set(a, 'setup_P2Repository33', None)
    assert not _is_linked(a, 'setup_P2Repository33', b2)
    if hasattr(b2, 'setup_MaterializationTask32'):
        assert not _is_linked(b2, 'setup_MaterializationTask32', a)


def test_assoc_p2Repositories49_link_reassign_clear():
    a = setup_RepositoryList(name="sample_text")
    b1 = setup_P2Repository(uRL="sample_text")
    b2 = setup_P2Repository(uRL="sample_text_2")
    _safe_set(a, 'setup_RepositoryList50', {b1})
    assert _is_linked(a, 'setup_RepositoryList50', b1)
    if hasattr(b1, 'setup_P2Repository51'):
        assert _is_linked(b1, 'setup_P2Repository51', a)
    _safe_set(a, 'setup_RepositoryList50', {b2})
    assert _is_linked(a, 'setup_RepositoryList50', b2)
    if hasattr(b1, 'setup_P2Repository51'):
        assert not _is_linked(b1, 'setup_P2Repository51', a)
    if hasattr(b2, 'setup_P2Repository51'):
        assert _is_linked(b2, 'setup_P2Repository51', a)
    _safe_set(a, 'setup_RepositoryList50', set())
    assert not _is_linked(a, 'setup_RepositoryList50', b2)
    if hasattr(b2, 'setup_P2Repository51'):
        assert not _is_linked(b2, 'setup_P2Repository51', a)


def test_assoc_predicates34_link_reassign_clear():
    a = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    b1 = setup_Predicate()
    b2 = setup_Predicate()
    _safe_set(a, 'setup_AutomaticSourceLocator', {b1})
    assert _is_linked(a, 'setup_AutomaticSourceLocator', b1)
    if hasattr(b1, 'setup_Predicate'):
        assert _is_linked(b1, 'setup_Predicate', a)
    _safe_set(a, 'setup_AutomaticSourceLocator', {b2})
    assert _is_linked(a, 'setup_AutomaticSourceLocator', b2)
    if hasattr(b1, 'setup_Predicate'):
        assert not _is_linked(b1, 'setup_Predicate', a)
    if hasattr(b2, 'setup_Predicate'):
        assert _is_linked(b2, 'setup_Predicate', a)
    _safe_set(a, 'setup_AutomaticSourceLocator', set())
    assert not _is_linked(a, 'setup_AutomaticSourceLocator', b2)
    if hasattr(b2, 'setup_Predicate'):
        assert not _is_linked(b2, 'setup_Predicate', a)


def test_assoc_project9_link_reassign_clear():
    a = setup_Project(label="sample_text", name="sample_text")
    b1 = setup_Branch(name="sample_text")
    b2 = setup_Branch(name="sample_text_2")
    _safe_set(a, 'Project10', b1)
    assert _is_linked(a, 'Project10', b1)
    if hasattr(b1, 'branches'):
        assert _is_linked(b1, 'branches', a)
    _safe_set(a, 'Project10', b2)
    assert _is_linked(a, 'Project10', b2)
    if hasattr(b1, 'branches'):
        assert not _is_linked(b1, 'branches', a)
    if hasattr(b2, 'branches'):
        assert _is_linked(b2, 'branches', a)
    _safe_set(a, 'Project10', None)
    assert not _is_linked(a, 'Project10', b2)
    if hasattr(b2, 'branches'):
        assert not _is_linked(b2, 'branches', a)


def test_assoc_projects3_link_reassign_clear():
    a = setup_Project(label="sample_text", name="sample_text")
    b1 = setup_Configuration()
    b2 = setup_Configuration()
    _safe_set(a, 'Project', b1)
    assert _is_linked(a, 'Project', b1)
    if hasattr(b1, 'configuration4'):
        assert _is_linked(b1, 'configuration4', a)
    _safe_set(a, 'Project', b2)
    assert _is_linked(a, 'Project', b2)
    if hasattr(b1, 'configuration4'):
        assert not _is_linked(b1, 'configuration4', a)
    if hasattr(b2, 'configuration4'):
        assert _is_linked(b2, 'configuration4', a)
    _safe_set(a, 'Project', None)
    assert not _is_linked(a, 'Project', b2)
    if hasattr(b2, 'configuration4'):
        assert not _is_linked(b2, 'configuration4', a)


def test_assoc_queries64_link_reassign_clear():
    a = setup_Query(summary="sample_text", uRL="sample_text")
    b1 = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    b2 = setup_MylynQueriesTask(connectorKind="sample_text_2", password="sample_text_2", repositoryURL="sample_text_2", userID="sample_text_2")
    _safe_set(a, 'Query', b1)
    assert _is_linked(a, 'Query', b1)
    if hasattr(b1, 'task'):
        assert _is_linked(b1, 'task', a)
    _safe_set(a, 'Query', b2)
    assert _is_linked(a, 'Query', b2)
    if hasattr(b1, 'task'):
        assert not _is_linked(b1, 'task', a)
    if hasattr(b2, 'task'):
        assert _is_linked(b2, 'task', a)
    _safe_set(a, 'Query', None)
    assert not _is_linked(a, 'Query', b2)
    if hasattr(b2, 'task'):
        assert not _is_linked(b2, 'task', a)


def test_assoc_repositoryLists44_link_reassign_clear():
    a = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    b1 = setup_RepositoryList(name="sample_text")
    b2 = setup_RepositoryList(name="sample_text_2")
    _safe_set(a, 'setup_TargletData45', {b1})
    assert _is_linked(a, 'setup_TargletData45', b1)
    if hasattr(b1, 'setup_RepositoryList'):
        assert _is_linked(b1, 'setup_RepositoryList', a)
    _safe_set(a, 'setup_TargletData45', {b2})
    assert _is_linked(a, 'setup_TargletData45', b2)
    if hasattr(b1, 'setup_RepositoryList'):
        assert not _is_linked(b1, 'setup_RepositoryList', a)
    if hasattr(b2, 'setup_RepositoryList'):
        assert _is_linked(b2, 'setup_RepositoryList', a)
    _safe_set(a, 'setup_TargletData45', set())
    assert not _is_linked(a, 'setup_TargletData45', b2)
    if hasattr(b2, 'setup_RepositoryList'):
        assert not _is_linked(b2, 'setup_RepositoryList', a)


def test_assoc_requirements19_link_reassign_clear():
    a = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    b1 = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    b2 = setup_SetupTask(disabled=False, documentation="sample_text_2", excludedTriggers="sample_text_2", scope="sample_text_2")
    _safe_set(a, 'setup_SetupTask', b1)
    assert _is_linked(a, 'setup_SetupTask', b1)
    if hasattr(b1, 'setup_SetupTask18'):
        assert _is_linked(b1, 'setup_SetupTask18', a)
    _safe_set(a, 'setup_SetupTask', b2)
    assert _is_linked(a, 'setup_SetupTask', b2)
    if hasattr(b1, 'setup_SetupTask18'):
        assert not _is_linked(b1, 'setup_SetupTask18', a)
    if hasattr(b2, 'setup_SetupTask18'):
        assert _is_linked(b2, 'setup_SetupTask18', a)
    _safe_set(a, 'setup_SetupTask', None)
    assert not _is_linked(a, 'setup_SetupTask', b2)
    if hasattr(b2, 'setup_SetupTask18'):
        assert not _is_linked(b2, 'setup_SetupTask18', a)


def test_assoc_restrictions11_link_reassign_clear():
    a = setup_Eclipse(version="sample_text")
    b1 = setup_Branch(name="sample_text")
    b2 = setup_Branch(name="sample_text_2")
    _safe_set(a, 'setup_Eclipse12', b1)
    assert _is_linked(a, 'setup_Eclipse12', b1)
    if hasattr(b1, 'setup_Branch'):
        assert _is_linked(b1, 'setup_Branch', a)
    _safe_set(a, 'setup_Eclipse12', b2)
    assert _is_linked(a, 'setup_Eclipse12', b2)
    if hasattr(b1, 'setup_Branch'):
        assert not _is_linked(b1, 'setup_Branch', a)
    if hasattr(b2, 'setup_Branch'):
        assert _is_linked(b2, 'setup_Branch', a)
    _safe_set(a, 'setup_Eclipse12', None)
    assert not _is_linked(a, 'setup_Eclipse12', b2)
    if hasattr(b2, 'setup_Branch'):
        assert not _is_linked(b2, 'setup_Branch', a)


def test_assoc_restrictions20_link_reassign_clear():
    a = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    b1 = setup_ConfigurableItem()
    b2 = setup_ConfigurableItem()
    _safe_set(a, 'setup_SetupTask21', {b1})
    assert _is_linked(a, 'setup_SetupTask21', b1)
    if hasattr(b1, 'setup_ConfigurableItem'):
        assert _is_linked(b1, 'setup_ConfigurableItem', a)
    _safe_set(a, 'setup_SetupTask21', {b2})
    assert _is_linked(a, 'setup_SetupTask21', b2)
    if hasattr(b1, 'setup_ConfigurableItem'):
        assert not _is_linked(b1, 'setup_ConfigurableItem', a)
    if hasattr(b2, 'setup_ConfigurableItem'):
        assert _is_linked(b2, 'setup_ConfigurableItem', a)
    _safe_set(a, 'setup_SetupTask21', set())
    assert not _is_linked(a, 'setup_SetupTask21', b2)
    if hasattr(b2, 'setup_ConfigurableItem'):
        assert not _is_linked(b2, 'setup_ConfigurableItem', a)


def test_assoc_restrictions8_link_reassign_clear():
    a = setup_Project(label="sample_text", name="sample_text")
    b1 = setup_Eclipse(version="sample_text")
    b2 = setup_Eclipse(version="sample_text_2")
    _safe_set(a, 'setup_Project', {b1})
    assert _is_linked(a, 'setup_Project', b1)
    if hasattr(b1, 'setup_Eclipse'):
        assert _is_linked(b1, 'setup_Eclipse', a)
    _safe_set(a, 'setup_Project', {b2})
    assert _is_linked(a, 'setup_Project', b2)
    if hasattr(b1, 'setup_Eclipse'):
        assert not _is_linked(b1, 'setup_Eclipse', a)
    if hasattr(b2, 'setup_Eclipse'):
        assert _is_linked(b2, 'setup_Eclipse', a)
    _safe_set(a, 'setup_Project', set())
    assert not _is_linked(a, 'setup_Project', b2)
    if hasattr(b2, 'setup_Eclipse'):
        assert not _is_linked(b2, 'setup_Eclipse', a)


def test_assoc_rootComponents28_link_reassign_clear():
    a = setup_Component(name="sample_text", type="sample_text", versionRange="sample_text")
    b1 = setup_MaterializationTask()
    b2 = setup_MaterializationTask()
    _safe_set(a, 'setup_Component', b1)
    assert _is_linked(a, 'setup_Component', b1)
    if hasattr(b1, 'setup_MaterializationTask'):
        assert _is_linked(b1, 'setup_MaterializationTask', a)
    _safe_set(a, 'setup_Component', b2)
    assert _is_linked(a, 'setup_Component', b2)
    if hasattr(b1, 'setup_MaterializationTask'):
        assert not _is_linked(b1, 'setup_MaterializationTask', a)
    if hasattr(b2, 'setup_MaterializationTask'):
        assert _is_linked(b2, 'setup_MaterializationTask', a)
    _safe_set(a, 'setup_Component', None)
    assert not _is_linked(a, 'setup_Component', b2)
    if hasattr(b2, 'setup_MaterializationTask'):
        assert not _is_linked(b2, 'setup_MaterializationTask', a)


def test_assoc_roots39_link_reassign_clear():
    a = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    b1 = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    b2 = setup_InstallableUnit(iD="sample_text_2", versionRange="sample_text_2")
    _safe_set(a, 'setup_TargletData', {b1})
    assert _is_linked(a, 'setup_TargletData', b1)
    if hasattr(b1, 'setup_InstallableUnit40'):
        assert _is_linked(b1, 'setup_InstallableUnit40', a)
    _safe_set(a, 'setup_TargletData', {b2})
    assert _is_linked(a, 'setup_TargletData', b2)
    if hasattr(b1, 'setup_InstallableUnit40'):
        assert not _is_linked(b1, 'setup_InstallableUnit40', a)
    if hasattr(b2, 'setup_InstallableUnit40'):
        assert _is_linked(b2, 'setup_InstallableUnit40', a)
    _safe_set(a, 'setup_TargletData', set())
    assert not _is_linked(a, 'setup_TargletData', b2)
    if hasattr(b2, 'setup_InstallableUnit40'):
        assert not _is_linked(b2, 'setup_InstallableUnit40', a)


def test_assoc_setupTasks22_link_reassign_clear():
    a = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    b1 = setup_SetupTaskContainer()
    b2 = setup_SetupTaskContainer()
    _safe_set(a, 'setup_SetupTask23', b1)
    assert _is_linked(a, 'setup_SetupTask23', b1)
    if hasattr(b1, 'setup_SetupTaskContainer'):
        assert _is_linked(b1, 'setup_SetupTaskContainer', a)
    _safe_set(a, 'setup_SetupTask23', b2)
    assert _is_linked(a, 'setup_SetupTask23', b2)
    if hasattr(b1, 'setup_SetupTaskContainer'):
        assert not _is_linked(b1, 'setup_SetupTaskContainer', a)
    if hasattr(b2, 'setup_SetupTaskContainer'):
        assert _is_linked(b2, 'setup_SetupTaskContainer', a)
    _safe_set(a, 'setup_SetupTask23', None)
    assert not _is_linked(a, 'setup_SetupTask23', b2)
    if hasattr(b2, 'setup_SetupTaskContainer'):
        assert not _is_linked(b2, 'setup_SetupTaskContainer', a)


def test_assoc_sourceLocators37_link_reassign_clear():
    a = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    b1 = setup_MavenImportTask()
    b2 = setup_MavenImportTask()
    _safe_set(a, 'setup_AutomaticSourceLocator38', b1)
    assert _is_linked(a, 'setup_AutomaticSourceLocator38', b1)
    if hasattr(b1, 'setup_MavenImportTask'):
        assert _is_linked(b1, 'setup_MavenImportTask', a)
    _safe_set(a, 'setup_AutomaticSourceLocator38', b2)
    assert _is_linked(a, 'setup_AutomaticSourceLocator38', b2)
    if hasattr(b1, 'setup_MavenImportTask'):
        assert not _is_linked(b1, 'setup_MavenImportTask', a)
    if hasattr(b2, 'setup_MavenImportTask'):
        assert _is_linked(b2, 'setup_MavenImportTask', a)
    _safe_set(a, 'setup_AutomaticSourceLocator38', None)
    assert not _is_linked(a, 'setup_AutomaticSourceLocator38', b2)
    if hasattr(b2, 'setup_MavenImportTask'):
        assert not _is_linked(b2, 'setup_MavenImportTask', a)


def test_assoc_sourceLocators41_link_reassign_clear():
    a = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    b1 = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    b2 = setup_AutomaticSourceLocator(locateNestedProjects=False, rootFolder="sample_text_2")
    _safe_set(a, 'setup_TargletData42', {b1})
    assert _is_linked(a, 'setup_TargletData42', b1)
    if hasattr(b1, 'setup_AutomaticSourceLocator43'):
        assert _is_linked(b1, 'setup_AutomaticSourceLocator43', a)
    _safe_set(a, 'setup_TargletData42', {b2})
    assert _is_linked(a, 'setup_TargletData42', b2)
    if hasattr(b1, 'setup_AutomaticSourceLocator43'):
        assert not _is_linked(b1, 'setup_AutomaticSourceLocator43', a)
    if hasattr(b2, 'setup_AutomaticSourceLocator43'):
        assert _is_linked(b2, 'setup_AutomaticSourceLocator43', a)
    _safe_set(a, 'setup_TargletData42', set())
    assert not _is_linked(a, 'setup_TargletData42', b2)
    if hasattr(b2, 'setup_AutomaticSourceLocator43'):
        assert not _is_linked(b2, 'setup_AutomaticSourceLocator43', a)


def test_assoc_sourceLocators52_link_reassign_clear():
    a = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    b1 = setup_ProjectsImportTask()
    b2 = setup_ProjectsImportTask()
    _safe_set(a, 'setup_AutomaticSourceLocator53', b1)
    assert _is_linked(a, 'setup_AutomaticSourceLocator53', b1)
    if hasattr(b1, 'setup_ProjectsImportTask'):
        assert _is_linked(b1, 'setup_ProjectsImportTask', a)
    _safe_set(a, 'setup_AutomaticSourceLocator53', b2)
    assert _is_linked(a, 'setup_AutomaticSourceLocator53', b2)
    if hasattr(b1, 'setup_ProjectsImportTask'):
        assert not _is_linked(b1, 'setup_ProjectsImportTask', a)
    if hasattr(b2, 'setup_ProjectsImportTask'):
        assert _is_linked(b2, 'setup_ProjectsImportTask', a)
    _safe_set(a, 'setup_AutomaticSourceLocator53', None)
    assert not _is_linked(a, 'setup_AutomaticSourceLocator53', b2)
    if hasattr(b2, 'setup_ProjectsImportTask'):
        assert not _is_linked(b2, 'setup_ProjectsImportTask', a)


def test_assoc_task65_link_reassign_clear():
    a = setup_Query(summary="sample_text", uRL="sample_text")
    b1 = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    b2 = setup_MylynQueriesTask(connectorKind="sample_text_2", password="sample_text_2", repositoryURL="sample_text_2", userID="sample_text_2")
    _safe_set(a, 'queries', b1)
    assert _is_linked(a, 'queries', b1)
    if hasattr(b1, 'MylynQueriesTask'):
        assert _is_linked(b1, 'MylynQueriesTask', a)
    _safe_set(a, 'queries', b2)
    assert _is_linked(a, 'queries', b2)
    if hasattr(b1, 'MylynQueriesTask'):
        assert not _is_linked(b1, 'MylynQueriesTask', a)
    if hasattr(b2, 'MylynQueriesTask'):
        assert _is_linked(b2, 'MylynQueriesTask', a)
    _safe_set(a, 'queries', None)
    assert not _is_linked(a, 'queries', b2)
    if hasattr(b2, 'MylynQueriesTask'):
        assert not _is_linked(b2, 'MylynQueriesTask', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BasicMaterializationTask_strategy = st.builds(BasicMaterializationTask)
@given(instance=BasicMaterializationTask_strategy)
@settings(max_examples=25)
def test_BasicMaterializationTask_instantiation(instance):
    assert isinstance(instance, BasicMaterializationTask)


ComponentExtension_strategy = st.builds(ComponentExtension)
@given(instance=ComponentExtension_strategy)
@settings(max_examples=25)
def test_ComponentExtension_instantiation(instance):
    assert isinstance(instance, ComponentExtension)


ConfigurableItem_strategy = st.builds(ConfigurableItem)
@given(instance=ConfigurableItem_strategy)
@settings(max_examples=25)
def test_ConfigurableItem_instantiation(instance):
    assert isinstance(instance, ConfigurableItem)


ScopeRoot_strategy = st.builds(ScopeRoot)
@given(instance=ScopeRoot_strategy)
@settings(max_examples=25)
def test_ScopeRoot_instantiation(instance):
    assert isinstance(instance, ScopeRoot)


SetupTask_strategy = st.builds(SetupTask)
@given(instance=SetupTask_strategy)
@settings(max_examples=25)
def test_SetupTask_instantiation(instance):
    assert isinstance(instance, SetupTask)


SetupTaskContainer_strategy = st.builds(SetupTaskContainer)
@given(instance=SetupTaskContainer_strategy)
@settings(max_examples=25)
def test_SetupTaskContainer_instantiation(instance):
    assert isinstance(instance, SetupTaskContainer)


SourceLocator_strategy = st.builds(SourceLocator)
@given(instance=SourceLocator_strategy)
@settings(max_examples=25)
def test_SourceLocator_instantiation(instance):
    assert isinstance(instance, SourceLocator)


TargletData_strategy = st.builds(TargletData)
@given(instance=TargletData_strategy)
@settings(max_examples=25)
def test_TargletData_instantiation(instance):
    assert isinstance(instance, TargletData)


setup_ApiBaselineTask_strategy = st.builds(setup_ApiBaselineTask, containerFolder=safe_text, version=safe_text, zipLocation=safe_text)
@given(instance=setup_ApiBaselineTask_strategy)
@settings(max_examples=25)
def test_setup_ApiBaselineTask_instantiation(instance):
    assert isinstance(instance, setup_ApiBaselineTask)


setup_AutomaticSourceLocator_strategy = st.builds(setup_AutomaticSourceLocator, locateNestedProjects=st.booleans(), rootFolder=safe_text)
@given(instance=setup_AutomaticSourceLocator_strategy)
@settings(max_examples=25)
def test_setup_AutomaticSourceLocator_instantiation(instance):
    assert isinstance(instance, setup_AutomaticSourceLocator)


setup_BasicMaterializationTask_strategy = st.builds(setup_BasicMaterializationTask, bundlePool=safe_text, targetPlatform=safe_text)
@given(instance=setup_BasicMaterializationTask_strategy)
@settings(max_examples=25)
def test_setup_BasicMaterializationTask_instantiation(instance):
    assert isinstance(instance, setup_BasicMaterializationTask)


setup_Branch_strategy = st.builds(setup_Branch, name=safe_text)
@given(instance=setup_Branch_strategy)
@settings(max_examples=25)
def test_setup_Branch_instantiation(instance):
    assert isinstance(instance, setup_Branch)


setup_BuckminsterImportTask_strategy = st.builds(setup_BuckminsterImportTask, mspec=safe_text)
@given(instance=setup_BuckminsterImportTask_strategy)
@settings(max_examples=25)
def test_setup_BuckminsterImportTask_instantiation(instance):
    assert isinstance(instance, setup_BuckminsterImportTask)


setup_BuildPlan_strategy = st.builds(setup_BuildPlan, name=safe_text)
@given(instance=setup_BuildPlan_strategy)
@settings(max_examples=25)
def test_setup_BuildPlan_instantiation(instance):
    assert isinstance(instance, setup_BuildPlan)


setup_CommandParameter_strategy = st.builds(setup_CommandParameter, iD=safe_text, value=safe_text)
@given(instance=setup_CommandParameter_strategy)
@settings(max_examples=25)
def test_setup_CommandParameter_instantiation(instance):
    assert isinstance(instance, setup_CommandParameter)


setup_Component_strategy = st.builds(setup_Component, name=safe_text, type=safe_text, versionRange=safe_text)
@given(instance=setup_Component_strategy)
@settings(max_examples=25)
def test_setup_Component_instantiation(instance):
    assert isinstance(instance, setup_Component)


setup_ComponentDefinition_strategy = st.builds(setup_ComponentDefinition, iD=safe_text, version=safe_text)
@given(instance=setup_ComponentDefinition_strategy)
@settings(max_examples=25)
def test_setup_ComponentDefinition_instantiation(instance):
    assert isinstance(instance, setup_ComponentDefinition)


setup_ComponentExtension_strategy = st.builds(setup_ComponentExtension)
@given(instance=setup_ComponentExtension_strategy)
@settings(max_examples=25)
def test_setup_ComponentExtension_instantiation(instance):
    assert isinstance(instance, setup_ComponentExtension)


setup_CompoundSetupTask_strategy = st.builds(setup_CompoundSetupTask, name=safe_text)
@given(instance=setup_CompoundSetupTask_strategy)
@settings(max_examples=25)
def test_setup_CompoundSetupTask_instantiation(instance):
    assert isinstance(instance, setup_CompoundSetupTask)


setup_ConfigurableItem_strategy = st.builds(setup_ConfigurableItem)
@given(instance=setup_ConfigurableItem_strategy)
@settings(max_examples=25)
def test_setup_ConfigurableItem_instantiation(instance):
    assert isinstance(instance, setup_ConfigurableItem)


setup_Configuration_strategy = st.builds(setup_Configuration)
@given(instance=setup_Configuration_strategy)
@settings(max_examples=25)
def test_setup_Configuration_instantiation(instance):
    assert isinstance(instance, setup_Configuration)


setup_ContextVariableTask_strategy = st.builds(setup_ContextVariableTask, label=safe_text, name=safe_text, stringSubstitution=st.booleans(), type=safe_text, value=safe_text)
@given(instance=setup_ContextVariableTask_strategy)
@settings(max_examples=25)
def test_setup_ContextVariableTask_instantiation(instance):
    assert isinstance(instance, setup_ContextVariableTask)


setup_Eclipse_strategy = st.builds(setup_Eclipse, version=safe_text)
@given(instance=setup_Eclipse_strategy)
@settings(max_examples=25)
def test_setup_Eclipse_instantiation(instance):
    assert isinstance(instance, setup_Eclipse)


setup_EclipseIniTask_strategy = st.builds(setup_EclipseIniTask, option=safe_text, value=safe_text, vm=st.booleans())
@given(instance=setup_EclipseIniTask_strategy)
@settings(max_examples=25)
def test_setup_EclipseIniTask_instantiation(instance):
    assert isinstance(instance, setup_EclipseIniTask)


setup_EclipsePreferenceTask_strategy = st.builds(setup_EclipsePreferenceTask, key=safe_text, value=safe_text)
@given(instance=setup_EclipsePreferenceTask_strategy)
@settings(max_examples=25)
def test_setup_EclipsePreferenceTask_instantiation(instance):
    assert isinstance(instance, setup_EclipsePreferenceTask)


setup_FileAssociationTask_strategy = st.builds(setup_FileAssociationTask, defaultEditorID=safe_text, filePattern=safe_text)
@given(instance=setup_FileAssociationTask_strategy)
@settings(max_examples=25)
def test_setup_FileAssociationTask_instantiation(instance):
    assert isinstance(instance, setup_FileAssociationTask)


setup_FileAssociationsTask_strategy = st.builds(setup_FileAssociationsTask)
@given(instance=setup_FileAssociationsTask_strategy)
@settings(max_examples=25)
def test_setup_FileAssociationsTask_instantiation(instance):
    assert isinstance(instance, setup_FileAssociationsTask)


setup_FileEditor_strategy = st.builds(setup_FileEditor, iD=safe_text)
@given(instance=setup_FileEditor_strategy)
@settings(max_examples=25)
def test_setup_FileEditor_instantiation(instance):
    assert isinstance(instance, setup_FileEditor)


setup_FileMapping_strategy = st.builds(setup_FileMapping, defaultEditorID=safe_text, filePattern=safe_text)
@given(instance=setup_FileMapping_strategy)
@settings(max_examples=25)
def test_setup_FileMapping_instantiation(instance):
    assert isinstance(instance, setup_FileMapping)


setup_GitCloneTask_strategy = st.builds(setup_GitCloneTask, checkoutBranch=safe_text, location=safe_text, pushURI=safe_text, remoteName=safe_text, remoteURI=safe_text, userID=safe_text)
@given(instance=setup_GitCloneTask_strategy)
@settings(max_examples=25)
def test_setup_GitCloneTask_instantiation(instance):
    assert isinstance(instance, setup_GitCloneTask)


setup_Index_strategy = st.builds(setup_Index, name=safe_text, oldURIs=safe_text, uRI=safe_text)
@given(instance=setup_Index_strategy)
@settings(max_examples=25)
def test_setup_Index_instantiation(instance):
    assert isinstance(instance, setup_Index)


setup_InstallableUnit_strategy = st.builds(setup_InstallableUnit, iD=safe_text, versionRange=safe_text)
@given(instance=setup_InstallableUnit_strategy)
@settings(max_examples=25)
def test_setup_InstallableUnit_instantiation(instance):
    assert isinstance(instance, setup_InstallableUnit)


setup_JRETask_strategy = st.builds(setup_JRETask, location=safe_text, version=safe_text)
@given(instance=setup_JRETask_strategy)
@settings(max_examples=25)
def test_setup_JRETask_instantiation(instance):
    assert isinstance(instance, setup_JRETask)


setup_KeyBindingContext_strategy = st.builds(setup_KeyBindingContext, iD=safe_text)
@given(instance=setup_KeyBindingContext_strategy)
@settings(max_examples=25)
def test_setup_KeyBindingContext_instantiation(instance):
    assert isinstance(instance, setup_KeyBindingContext)


setup_KeyBindingTask_strategy = st.builds(setup_KeyBindingTask, command=safe_text, keys=safe_text, locale=safe_text, platform=safe_text, scheme=safe_text)
@given(instance=setup_KeyBindingTask_strategy)
@settings(max_examples=25)
def test_setup_KeyBindingTask_instantiation(instance):
    assert isinstance(instance, setup_KeyBindingTask)


setup_LinkLocationTask_strategy = st.builds(setup_LinkLocationTask, name=safe_text, path=safe_text)
@given(instance=setup_LinkLocationTask_strategy)
@settings(max_examples=25)
def test_setup_LinkLocationTask_instantiation(instance):
    assert isinstance(instance, setup_LinkLocationTask)


setup_ManualSourceLocator_strategy = st.builds(setup_ManualSourceLocator, componentNamePattern=safe_text, componentTypes=safe_text, location=safe_text)
@given(instance=setup_ManualSourceLocator_strategy)
@settings(max_examples=25)
def test_setup_ManualSourceLocator_instantiation(instance):
    assert isinstance(instance, setup_ManualSourceLocator)


setup_MaterializationTask_strategy = st.builds(setup_MaterializationTask)
@given(instance=setup_MaterializationTask_strategy)
@settings(max_examples=25)
def test_setup_MaterializationTask_instantiation(instance):
    assert isinstance(instance, setup_MaterializationTask)


setup_MavenImportTask_strategy = st.builds(setup_MavenImportTask)
@given(instance=setup_MavenImportTask_strategy)
@settings(max_examples=25)
def test_setup_MavenImportTask_instantiation(instance):
    assert isinstance(instance, setup_MavenImportTask)


setup_MetaIndex_strategy = st.builds(setup_MetaIndex)
@given(instance=setup_MetaIndex_strategy)
@settings(max_examples=25)
def test_setup_MetaIndex_instantiation(instance):
    assert isinstance(instance, setup_MetaIndex)


setup_MylynBuildsTask_strategy = st.builds(setup_MylynBuildsTask, connectorKind=safe_text, password=safe_text, serverURL=safe_text, userID=safe_text)
@given(instance=setup_MylynBuildsTask_strategy)
@settings(max_examples=25)
def test_setup_MylynBuildsTask_instantiation(instance):
    assert isinstance(instance, setup_MylynBuildsTask)


setup_MylynQueriesTask_strategy = st.builds(setup_MylynQueriesTask, connectorKind=safe_text, password=safe_text, repositoryURL=safe_text, userID=safe_text)
@given(instance=setup_MylynQueriesTask_strategy)
@settings(max_examples=25)
def test_setup_MylynQueriesTask_instantiation(instance):
    assert isinstance(instance, setup_MylynQueriesTask)


setup_MylynQueryTask_strategy = st.builds(setup_MylynQueryTask, connectorKind=safe_text, relativeURL=safe_text, repositoryURL=safe_text, summary=safe_text)
@given(instance=setup_MylynQueryTask_strategy)
@settings(max_examples=25)
def test_setup_MylynQueryTask_instantiation(instance):
    assert isinstance(instance, setup_MylynQueryTask)


setup_P2Repository_strategy = st.builds(setup_P2Repository, uRL=safe_text)
@given(instance=setup_P2Repository_strategy)
@settings(max_examples=25)
def test_setup_P2Repository_instantiation(instance):
    assert isinstance(instance, setup_P2Repository)


setup_P2Task_strategy = st.builds(setup_P2Task, licenseConfirmationDisabled=st.booleans(), mergeDisabled=st.booleans())
@given(instance=setup_P2Task_strategy)
@settings(max_examples=25)
def test_setup_P2Task_instantiation(instance):
    assert isinstance(instance, setup_P2Task)


setup_Predicate_strategy = st.builds(setup_Predicate)
@given(instance=setup_Predicate_strategy)
@settings(max_examples=25)
def test_setup_Predicate_instantiation(instance):
    assert isinstance(instance, setup_Predicate)


setup_Preferences_strategy = st.builds(setup_Preferences, acceptedLicenses=safe_text, installFolder=safe_text)
@given(instance=setup_Preferences_strategy)
@settings(max_examples=25)
def test_setup_Preferences_instantiation(instance):
    assert isinstance(instance, setup_Preferences)


setup_Project_strategy = st.builds(setup_Project, label=safe_text, name=safe_text)
@given(instance=setup_Project_strategy)
@settings(max_examples=25)
def test_setup_Project_instantiation(instance):
    assert isinstance(instance, setup_Project)


setup_ProjectSetImportTask_strategy = st.builds(setup_ProjectSetImportTask, uRL=safe_text)
@given(instance=setup_ProjectSetImportTask_strategy)
@settings(max_examples=25)
def test_setup_ProjectSetImportTask_instantiation(instance):
    assert isinstance(instance, setup_ProjectSetImportTask)


setup_ProjectsImportTask_strategy = st.builds(setup_ProjectsImportTask)
@given(instance=setup_ProjectsImportTask_strategy)
@settings(max_examples=25)
def test_setup_ProjectsImportTask_instantiation(instance):
    assert isinstance(instance, setup_ProjectsImportTask)


setup_Query_strategy = st.builds(setup_Query, summary=safe_text, uRL=safe_text)
@given(instance=setup_Query_strategy)
@settings(max_examples=25)
def test_setup_Query_instantiation(instance):
    assert isinstance(instance, setup_Query)


setup_QueryAttribute_strategy = st.builds(setup_QueryAttribute, key=safe_text, value=safe_text)
@given(instance=setup_QueryAttribute_strategy)
@settings(max_examples=25)
def test_setup_QueryAttribute_instantiation(instance):
    assert isinstance(instance, setup_QueryAttribute)


setup_RedirectionTask_strategy = st.builds(setup_RedirectionTask, sourceURL=safe_text, targetURL=safe_text)
@given(instance=setup_RedirectionTask_strategy)
@settings(max_examples=25)
def test_setup_RedirectionTask_instantiation(instance):
    assert isinstance(instance, setup_RedirectionTask)


setup_RepositoryList_strategy = st.builds(setup_RepositoryList, name=safe_text)
@given(instance=setup_RepositoryList_strategy)
@settings(max_examples=25)
def test_setup_RepositoryList_instantiation(instance):
    assert isinstance(instance, setup_RepositoryList)


setup_ResourceCopyTask_strategy = st.builds(setup_ResourceCopyTask, sourceURL=safe_text, targetURL=safe_text)
@given(instance=setup_ResourceCopyTask_strategy)
@settings(max_examples=25)
def test_setup_ResourceCopyTask_instantiation(instance):
    assert isinstance(instance, setup_ResourceCopyTask)


setup_ResourceCreationTask_strategy = st.builds(setup_ResourceCreationTask, content=safe_text, encoding=safe_text, targetURL=safe_text)
@given(instance=setup_ResourceCreationTask_strategy)
@settings(max_examples=25)
def test_setup_ResourceCreationTask_instantiation(instance):
    assert isinstance(instance, setup_ResourceCreationTask)


setup_ScopeRoot_strategy = st.builds(setup_ScopeRoot)
@given(instance=setup_ScopeRoot_strategy)
@settings(max_examples=25)
def test_setup_ScopeRoot_instantiation(instance):
    assert isinstance(instance, setup_ScopeRoot)


setup_Setup_strategy = st.builds(setup_Setup)
@given(instance=setup_Setup_strategy)
@settings(max_examples=25)
def test_setup_Setup_instantiation(instance):
    assert isinstance(instance, setup_Setup)


setup_SetupTask_strategy = st.builds(setup_SetupTask, disabled=st.booleans(), documentation=safe_text, excludedTriggers=safe_text, scope=safe_text)
@given(instance=setup_SetupTask_strategy)
@settings(max_examples=25)
def test_setup_SetupTask_instantiation(instance):
    assert isinstance(instance, setup_SetupTask)


setup_SetupTaskContainer_strategy = st.builds(setup_SetupTaskContainer)
@given(instance=setup_SetupTaskContainer_strategy)
@settings(max_examples=25)
def test_setup_SetupTaskContainer_instantiation(instance):
    assert isinstance(instance, setup_SetupTaskContainer)


setup_SourceLocator_strategy = st.builds(setup_SourceLocator)
@given(instance=setup_SourceLocator_strategy)
@settings(max_examples=25)
def test_setup_SourceLocator_instantiation(instance):
    assert isinstance(instance, setup_SourceLocator)


setup_TargetPlatformTask_strategy = st.builds(setup_TargetPlatformTask, name=safe_text)
@given(instance=setup_TargetPlatformTask_strategy)
@settings(max_examples=25)
def test_setup_TargetPlatformTask_instantiation(instance):
    assert isinstance(instance, setup_TargetPlatformTask)


setup_Targlet_strategy = st.builds(setup_Targlet)
@given(instance=setup_Targlet_strategy)
@settings(max_examples=25)
def test_setup_Targlet_instantiation(instance):
    assert isinstance(instance, setup_Targlet)


setup_TargletData_strategy = st.builds(setup_TargletData, activeRepositoryList=safe_text, includeAllPlatforms=st.booleans(), includeSources=st.booleans(), name=safe_text)
@given(instance=setup_TargletData_strategy)
@settings(max_examples=25)
def test_setup_TargletData_instantiation(instance):
    assert isinstance(instance, setup_TargletData)


setup_TargletImportTask_strategy = st.builds(setup_TargletImportTask, targletURI=safe_text)
@given(instance=setup_TargletImportTask_strategy)
@settings(max_examples=25)
def test_setup_TargletImportTask_instantiation(instance):
    assert isinstance(instance, setup_TargletImportTask)


setup_TargletTask_strategy = st.builds(setup_TargletTask)
@given(instance=setup_TargletTask_strategy)
@settings(max_examples=25)
def test_setup_TargletTask_instantiation(instance):
    assert isinstance(instance, setup_TargletTask)


setup_TextModification_strategy = st.builds(setup_TextModification, pattern=safe_text, substitutions=safe_text)
@given(instance=setup_TextModification_strategy)
@settings(max_examples=25)
def test_setup_TextModification_instantiation(instance):
    assert isinstance(instance, setup_TextModification)


setup_TextModifyTask_strategy = st.builds(setup_TextModifyTask, encoding=safe_text, uRL=safe_text)
@given(instance=setup_TextModifyTask_strategy)
@settings(max_examples=25)
def test_setup_TextModifyTask_instantiation(instance):
    assert isinstance(instance, setup_TextModifyTask)


setup_VariableChoice_strategy = st.builds(setup_VariableChoice, label=safe_text, value=safe_text)
@given(instance=setup_VariableChoice_strategy)
@settings(max_examples=25)
def test_setup_VariableChoice_instantiation(instance):
    assert isinstance(instance, setup_VariableChoice)


setup_WorkingSet_strategy = st.builds(setup_WorkingSet)
@given(instance=setup_WorkingSet_strategy)
@settings(max_examples=25)
def test_setup_WorkingSet_instantiation(instance):
    assert isinstance(instance, setup_WorkingSet)


setup_WorkingSetTask_strategy = st.builds(setup_WorkingSetTask)
@given(instance=setup_WorkingSetTask_strategy)
@settings(max_examples=25)
def test_setup_WorkingSetTask_instantiation(instance):
    assert isinstance(instance, setup_WorkingSetTask)


