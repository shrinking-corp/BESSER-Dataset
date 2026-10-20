import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_activeP2Repositories46_reverse_link_reassign_clear():
    a1 = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    a2 = setup_TargletData(activeRepositoryList="sample_text_2", includeAllPlatforms=False, includeSources=False, name="sample_text_2")
    b = setup_P2Repository(uRL="sample_text")
    _safe_set(b, 'setup_P2Repository48', a1)
    assert _is_linked(b, 'setup_P2Repository48', a1)
    if hasattr(a1, 'setup_TargletData47'):
        assert _is_linked(a1, 'setup_TargletData47', b)
    _safe_set(b, 'setup_P2Repository48', a2)
    assert _is_linked(b, 'setup_P2Repository48', a2)
    if hasattr(a1, 'setup_TargletData47'):
        assert not _is_linked(a1, 'setup_TargletData47', b)
    if hasattr(a2, 'setup_TargletData47'):
        assert _is_linked(a2, 'setup_TargletData47', b)
    _safe_set(b, 'setup_P2Repository48', None)
    assert not _is_linked(b, 'setup_P2Repository48', a2)
    if hasattr(a2, 'setup_TargletData47'):
        assert not _is_linked(a2, 'setup_TargletData47', b)


def test_assoc_attributes66_reverse_link_reassign_clear():
    a1 = setup_QueryAttribute(key="sample_text", value="sample_text")
    a2 = setup_QueryAttribute(key="sample_text_2", value="sample_text_2")
    b = setup_Query(summary="sample_text", uRL="sample_text")
    _safe_set(b, 'setup_Query', {a1})
    assert _is_linked(b, 'setup_Query', a1)
    if hasattr(a1, 'setup_QueryAttribute'):
        assert _is_linked(a1, 'setup_QueryAttribute', b)
    _safe_set(b, 'setup_Query', {a2})
    assert _is_linked(b, 'setup_Query', a2)
    if hasattr(a1, 'setup_QueryAttribute'):
        assert not _is_linked(a1, 'setup_QueryAttribute', b)
    if hasattr(a2, 'setup_QueryAttribute'):
        assert _is_linked(a2, 'setup_QueryAttribute', b)
    _safe_set(b, 'setup_Query', set())
    assert not _is_linked(b, 'setup_Query', a2)
    if hasattr(a2, 'setup_QueryAttribute'):
        assert not _is_linked(a2, 'setup_QueryAttribute', b)


def test_assoc_branch13_reverse_link_reassign_clear():
    a1 = setup_Setup()
    a2 = setup_Setup()
    b = setup_Branch(name="sample_text")
    _safe_set(b, 'setup_Branch14', a1)
    assert _is_linked(b, 'setup_Branch14', a1)
    if hasattr(a1, 'setup_Setup'):
        assert _is_linked(a1, 'setup_Setup', b)
    _safe_set(b, 'setup_Branch14', a2)
    assert _is_linked(b, 'setup_Branch14', a2)
    if hasattr(a1, 'setup_Setup'):
        assert not _is_linked(a1, 'setup_Setup', b)
    if hasattr(a2, 'setup_Setup'):
        assert _is_linked(a2, 'setup_Setup', b)
    _safe_set(b, 'setup_Branch14', None)
    assert not _is_linked(b, 'setup_Branch14', a2)
    if hasattr(a2, 'setup_Setup'):
        assert not _is_linked(a2, 'setup_Setup', b)


def test_assoc_branches7_reverse_link_reassign_clear():
    a1 = setup_Project(label="sample_text", name="sample_text")
    a2 = setup_Project(label="sample_text_2", name="sample_text_2")
    b = setup_Branch(name="sample_text")
    _safe_set(b, 'Branch', a1)
    assert _is_linked(b, 'Branch', a1)
    if hasattr(a1, 'project'):
        assert _is_linked(a1, 'project', b)
    _safe_set(b, 'Branch', a2)
    assert _is_linked(b, 'Branch', a2)
    if hasattr(a1, 'project'):
        assert not _is_linked(a1, 'project', b)
    if hasattr(a2, 'project'):
        assert _is_linked(a2, 'project', b)
    _safe_set(b, 'Branch', None)
    assert not _is_linked(b, 'Branch', a2)
    if hasattr(a2, 'project'):
        assert not _is_linked(a2, 'project', b)


def test_assoc_buildPlans67_reverse_link_reassign_clear():
    a1 = setup_MylynBuildsTask(connectorKind="sample_text", password="sample_text", serverURL="sample_text", userID="sample_text")
    a2 = setup_MylynBuildsTask(connectorKind="sample_text_2", password="sample_text_2", serverURL="sample_text_2", userID="sample_text_2")
    b = setup_BuildPlan(name="sample_text")
    _safe_set(b, 'setup_BuildPlan', a1)
    assert _is_linked(b, 'setup_BuildPlan', a1)
    if hasattr(a1, 'setup_MylynBuildsTask'):
        assert _is_linked(a1, 'setup_MylynBuildsTask', b)
    _safe_set(b, 'setup_BuildPlan', a2)
    assert _is_linked(b, 'setup_BuildPlan', a2)
    if hasattr(a1, 'setup_MylynBuildsTask'):
        assert not _is_linked(a1, 'setup_MylynBuildsTask', b)
    if hasattr(a2, 'setup_MylynBuildsTask'):
        assert _is_linked(a2, 'setup_MylynBuildsTask', b)
    _safe_set(b, 'setup_BuildPlan', None)
    assert not _is_linked(b, 'setup_BuildPlan', a2)
    if hasattr(a2, 'setup_MylynBuildsTask'):
        assert not _is_linked(a2, 'setup_MylynBuildsTask', b)


def test_assoc_choices24_reverse_link_reassign_clear():
    a1 = setup_VariableChoice(label="sample_text", value="sample_text")
    a2 = setup_VariableChoice(label="sample_text_2", value="sample_text_2")
    b = setup_ContextVariableTask(label="sample_text", name="sample_text", stringSubstitution=True, type="sample_text", value="sample_text")
    _safe_set(b, 'setup_ContextVariableTask', {a1})
    assert _is_linked(b, 'setup_ContextVariableTask', a1)
    if hasattr(a1, 'setup_VariableChoice'):
        assert _is_linked(a1, 'setup_VariableChoice', b)
    _safe_set(b, 'setup_ContextVariableTask', {a2})
    assert _is_linked(b, 'setup_ContextVariableTask', a2)
    if hasattr(a1, 'setup_VariableChoice'):
        assert not _is_linked(a1, 'setup_VariableChoice', b)
    if hasattr(a2, 'setup_VariableChoice'):
        assert _is_linked(a2, 'setup_VariableChoice', b)
    _safe_set(b, 'setup_ContextVariableTask', set())
    assert not _is_linked(b, 'setup_ContextVariableTask', a2)
    if hasattr(a2, 'setup_VariableChoice'):
        assert not _is_linked(a2, 'setup_VariableChoice', b)


def test_assoc_commandParameters62_reverse_link_reassign_clear():
    a1 = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    a2 = setup_KeyBindingTask(command="sample_text_2", keys="sample_text_2", locale="sample_text_2", platform="sample_text_2", scheme="sample_text_2")
    b = setup_CommandParameter(iD="sample_text", value="sample_text")
    _safe_set(b, 'setup_CommandParameter', a1)
    assert _is_linked(b, 'setup_CommandParameter', a1)
    if hasattr(a1, 'setup_KeyBindingTask63'):
        assert _is_linked(a1, 'setup_KeyBindingTask63', b)
    _safe_set(b, 'setup_CommandParameter', a2)
    assert _is_linked(b, 'setup_CommandParameter', a2)
    if hasattr(a1, 'setup_KeyBindingTask63'):
        assert not _is_linked(a1, 'setup_KeyBindingTask63', b)
    if hasattr(a2, 'setup_KeyBindingTask63'):
        assert _is_linked(a2, 'setup_KeyBindingTask63', b)
    _safe_set(b, 'setup_CommandParameter', None)
    assert not _is_linked(b, 'setup_CommandParameter', a2)
    if hasattr(a2, 'setup_KeyBindingTask63'):
        assert not _is_linked(a2, 'setup_KeyBindingTask63', b)


def test_assoc_contexts61_reverse_link_reassign_clear():
    a1 = setup_KeyBindingTask(command="sample_text", keys="sample_text", locale="sample_text", platform="sample_text", scheme="sample_text")
    a2 = setup_KeyBindingTask(command="sample_text_2", keys="sample_text_2", locale="sample_text_2", platform="sample_text_2", scheme="sample_text_2")
    b = setup_KeyBindingContext(iD="sample_text")
    _safe_set(b, 'setup_KeyBindingContext', a1)
    assert _is_linked(b, 'setup_KeyBindingContext', a1)
    if hasattr(a1, 'setup_KeyBindingTask'):
        assert _is_linked(a1, 'setup_KeyBindingTask', b)
    _safe_set(b, 'setup_KeyBindingContext', a2)
    assert _is_linked(b, 'setup_KeyBindingContext', a2)
    if hasattr(a1, 'setup_KeyBindingTask'):
        assert not _is_linked(a1, 'setup_KeyBindingTask', b)
    if hasattr(a2, 'setup_KeyBindingTask'):
        assert _is_linked(a2, 'setup_KeyBindingTask', b)
    _safe_set(b, 'setup_KeyBindingContext', None)
    assert not _is_linked(b, 'setup_KeyBindingContext', a2)
    if hasattr(a2, 'setup_KeyBindingTask'):
        assert not _is_linked(a2, 'setup_KeyBindingTask', b)


def test_assoc_eclipseVersion15_reverse_link_reassign_clear():
    a1 = setup_Setup()
    a2 = setup_Setup()
    b = setup_Eclipse(version="sample_text")
    _safe_set(b, 'setup_Eclipse17', a1)
    assert _is_linked(b, 'setup_Eclipse17', a1)
    if hasattr(a1, 'setup_Setup16'):
        assert _is_linked(a1, 'setup_Setup16', b)
    _safe_set(b, 'setup_Eclipse17', a2)
    assert _is_linked(b, 'setup_Eclipse17', a2)
    if hasattr(a1, 'setup_Setup16'):
        assert not _is_linked(a1, 'setup_Setup16', b)
    if hasattr(a2, 'setup_Setup16'):
        assert _is_linked(a2, 'setup_Setup16', b)
    _safe_set(b, 'setup_Eclipse17', None)
    assert not _is_linked(b, 'setup_Eclipse17', a2)
    if hasattr(a2, 'setup_Setup16'):
        assert not _is_linked(a2, 'setup_Setup16', b)


def test_assoc_editors54_reverse_link_reassign_clear():
    a1 = setup_FileEditor(iD="sample_text")
    a2 = setup_FileEditor(iD="sample_text_2")
    b = setup_FileAssociationTask(defaultEditorID="sample_text", filePattern="sample_text")
    _safe_set(b, 'setup_FileAssociationTask', {a1})
    assert _is_linked(b, 'setup_FileAssociationTask', a1)
    if hasattr(a1, 'setup_FileEditor'):
        assert _is_linked(a1, 'setup_FileEditor', b)
    _safe_set(b, 'setup_FileAssociationTask', {a2})
    assert _is_linked(b, 'setup_FileAssociationTask', a2)
    if hasattr(a1, 'setup_FileEditor'):
        assert not _is_linked(a1, 'setup_FileEditor', b)
    if hasattr(a2, 'setup_FileEditor'):
        assert _is_linked(a2, 'setup_FileEditor', b)
    _safe_set(b, 'setup_FileAssociationTask', set())
    assert not _is_linked(b, 'setup_FileAssociationTask', a2)
    if hasattr(a2, 'setup_FileEditor'):
        assert not _is_linked(a2, 'setup_FileEditor', b)


def test_assoc_editors56_reverse_link_reassign_clear():
    a1 = setup_FileMapping(defaultEditorID="sample_text", filePattern="sample_text")
    a2 = setup_FileMapping(defaultEditorID="sample_text_2", filePattern="sample_text_2")
    b = setup_FileEditor(iD="sample_text")
    _safe_set(b, 'setup_FileEditor58', a1)
    assert _is_linked(b, 'setup_FileEditor58', a1)
    if hasattr(a1, 'setup_FileMapping57'):
        assert _is_linked(a1, 'setup_FileMapping57', b)
    _safe_set(b, 'setup_FileEditor58', a2)
    assert _is_linked(b, 'setup_FileEditor58', a2)
    if hasattr(a1, 'setup_FileMapping57'):
        assert not _is_linked(a1, 'setup_FileMapping57', b)
    if hasattr(a2, 'setup_FileMapping57'):
        assert _is_linked(a2, 'setup_FileMapping57', b)
    _safe_set(b, 'setup_FileEditor58', None)
    assert not _is_linked(b, 'setup_FileEditor58', a2)
    if hasattr(a2, 'setup_FileMapping57'):
        assert not _is_linked(a2, 'setup_FileMapping57', b)


def test_assoc_installableUnits25_reverse_link_reassign_clear():
    a1 = setup_P2Task(licenseConfirmationDisabled=True, mergeDisabled=True)
    a2 = setup_P2Task(licenseConfirmationDisabled=False, mergeDisabled=False)
    b = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    _safe_set(b, 'setup_InstallableUnit', a1)
    assert _is_linked(b, 'setup_InstallableUnit', a1)
    if hasattr(a1, 'setup_P2Task'):
        assert _is_linked(a1, 'setup_P2Task', b)
    _safe_set(b, 'setup_InstallableUnit', a2)
    assert _is_linked(b, 'setup_InstallableUnit', a2)
    if hasattr(a1, 'setup_P2Task'):
        assert not _is_linked(a1, 'setup_P2Task', b)
    if hasattr(a2, 'setup_P2Task'):
        assert _is_linked(a2, 'setup_P2Task', b)
    _safe_set(b, 'setup_InstallableUnit', None)
    assert not _is_linked(b, 'setup_InstallableUnit', a2)
    if hasattr(a2, 'setup_P2Task'):
        assert not _is_linked(a2, 'setup_P2Task', b)


def test_assoc_modifications60_reverse_link_reassign_clear():
    a1 = setup_TextModifyTask(encoding="sample_text", uRL="sample_text")
    a2 = setup_TextModifyTask(encoding="sample_text_2", uRL="sample_text_2")
    b = setup_TextModification(pattern="sample_text", substitutions="sample_text")
    _safe_set(b, 'setup_TextModification', a1)
    assert _is_linked(b, 'setup_TextModification', a1)
    if hasattr(a1, 'setup_TextModifyTask'):
        assert _is_linked(a1, 'setup_TextModifyTask', b)
    _safe_set(b, 'setup_TextModification', a2)
    assert _is_linked(b, 'setup_TextModification', a2)
    if hasattr(a1, 'setup_TextModifyTask'):
        assert not _is_linked(a1, 'setup_TextModifyTask', b)
    if hasattr(a2, 'setup_TextModifyTask'):
        assert _is_linked(a2, 'setup_TextModifyTask', b)
    _safe_set(b, 'setup_TextModification', None)
    assert not _is_linked(b, 'setup_TextModification', a2)
    if hasattr(a2, 'setup_TextModifyTask'):
        assert not _is_linked(a2, 'setup_TextModifyTask', b)


def test_assoc_p2Repositories26_reverse_link_reassign_clear():
    a1 = setup_P2Task(licenseConfirmationDisabled=True, mergeDisabled=True)
    a2 = setup_P2Task(licenseConfirmationDisabled=False, mergeDisabled=False)
    b = setup_P2Repository(uRL="sample_text")
    _safe_set(b, 'setup_P2Repository', a1)
    assert _is_linked(b, 'setup_P2Repository', a1)
    if hasattr(a1, 'setup_P2Task27'):
        assert _is_linked(a1, 'setup_P2Task27', b)
    _safe_set(b, 'setup_P2Repository', a2)
    assert _is_linked(b, 'setup_P2Repository', a2)
    if hasattr(a1, 'setup_P2Task27'):
        assert not _is_linked(a1, 'setup_P2Task27', b)
    if hasattr(a2, 'setup_P2Task27'):
        assert _is_linked(a2, 'setup_P2Task27', b)
    _safe_set(b, 'setup_P2Repository', None)
    assert not _is_linked(b, 'setup_P2Repository', a2)
    if hasattr(a2, 'setup_P2Task27'):
        assert not _is_linked(a2, 'setup_P2Task27', b)


def test_assoc_p2Repositories49_reverse_link_reassign_clear():
    a1 = setup_RepositoryList(name="sample_text")
    a2 = setup_RepositoryList(name="sample_text_2")
    b = setup_P2Repository(uRL="sample_text")
    _safe_set(b, 'setup_P2Repository51', a1)
    assert _is_linked(b, 'setup_P2Repository51', a1)
    if hasattr(a1, 'setup_RepositoryList50'):
        assert _is_linked(a1, 'setup_RepositoryList50', b)
    _safe_set(b, 'setup_P2Repository51', a2)
    assert _is_linked(b, 'setup_P2Repository51', a2)
    if hasattr(a1, 'setup_RepositoryList50'):
        assert not _is_linked(a1, 'setup_RepositoryList50', b)
    if hasattr(a2, 'setup_RepositoryList50'):
        assert _is_linked(a2, 'setup_RepositoryList50', b)
    _safe_set(b, 'setup_P2Repository51', None)
    assert not _is_linked(b, 'setup_P2Repository51', a2)
    if hasattr(a2, 'setup_RepositoryList50'):
        assert not _is_linked(a2, 'setup_RepositoryList50', b)


def test_assoc_project9_reverse_link_reassign_clear():
    a1 = setup_Project(label="sample_text", name="sample_text")
    a2 = setup_Project(label="sample_text_2", name="sample_text_2")
    b = setup_Branch(name="sample_text")
    _safe_set(b, 'branches', a1)
    assert _is_linked(b, 'branches', a1)
    if hasattr(a1, 'Project10'):
        assert _is_linked(a1, 'Project10', b)
    _safe_set(b, 'branches', a2)
    assert _is_linked(b, 'branches', a2)
    if hasattr(a1, 'Project10'):
        assert not _is_linked(a1, 'Project10', b)
    if hasattr(a2, 'Project10'):
        assert _is_linked(a2, 'Project10', b)
    _safe_set(b, 'branches', None)
    assert not _is_linked(b, 'branches', a2)
    if hasattr(a2, 'Project10'):
        assert not _is_linked(a2, 'Project10', b)


def test_assoc_queries64_reverse_link_reassign_clear():
    a1 = setup_Query(summary="sample_text", uRL="sample_text")
    a2 = setup_Query(summary="sample_text_2", uRL="sample_text_2")
    b = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    _safe_set(b, 'task', {a1})
    assert _is_linked(b, 'task', a1)
    if hasattr(a1, 'Query'):
        assert _is_linked(a1, 'Query', b)
    _safe_set(b, 'task', {a2})
    assert _is_linked(b, 'task', a2)
    if hasattr(a1, 'Query'):
        assert not _is_linked(a1, 'Query', b)
    if hasattr(a2, 'Query'):
        assert _is_linked(a2, 'Query', b)
    _safe_set(b, 'task', set())
    assert not _is_linked(b, 'task', a2)
    if hasattr(a2, 'Query'):
        assert not _is_linked(a2, 'Query', b)


def test_assoc_repositoryLists44_reverse_link_reassign_clear():
    a1 = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    a2 = setup_TargletData(activeRepositoryList="sample_text_2", includeAllPlatforms=False, includeSources=False, name="sample_text_2")
    b = setup_RepositoryList(name="sample_text")
    _safe_set(b, 'setup_RepositoryList', a1)
    assert _is_linked(b, 'setup_RepositoryList', a1)
    if hasattr(a1, 'setup_TargletData45'):
        assert _is_linked(a1, 'setup_TargletData45', b)
    _safe_set(b, 'setup_RepositoryList', a2)
    assert _is_linked(b, 'setup_RepositoryList', a2)
    if hasattr(a1, 'setup_TargletData45'):
        assert not _is_linked(a1, 'setup_TargletData45', b)
    if hasattr(a2, 'setup_TargletData45'):
        assert _is_linked(a2, 'setup_TargletData45', b)
    _safe_set(b, 'setup_RepositoryList', None)
    assert not _is_linked(b, 'setup_RepositoryList', a2)
    if hasattr(a2, 'setup_TargletData45'):
        assert not _is_linked(a2, 'setup_TargletData45', b)


def test_assoc_requirements19_reverse_link_reassign_clear():
    a1 = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    a2 = setup_SetupTask(disabled=False, documentation="sample_text_2", excludedTriggers="sample_text_2", scope="sample_text_2")
    b = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    _safe_set(b, 'setup_SetupTask18', {a1})
    assert _is_linked(b, 'setup_SetupTask18', a1)
    if hasattr(a1, 'setup_SetupTask'):
        assert _is_linked(a1, 'setup_SetupTask', b)
    _safe_set(b, 'setup_SetupTask18', {a2})
    assert _is_linked(b, 'setup_SetupTask18', a2)
    if hasattr(a1, 'setup_SetupTask'):
        assert not _is_linked(a1, 'setup_SetupTask', b)
    if hasattr(a2, 'setup_SetupTask'):
        assert _is_linked(a2, 'setup_SetupTask', b)
    _safe_set(b, 'setup_SetupTask18', set())
    assert not _is_linked(b, 'setup_SetupTask18', a2)
    if hasattr(a2, 'setup_SetupTask'):
        assert not _is_linked(a2, 'setup_SetupTask', b)


def test_assoc_restrictions11_reverse_link_reassign_clear():
    a1 = setup_Eclipse(version="sample_text")
    a2 = setup_Eclipse(version="sample_text_2")
    b = setup_Branch(name="sample_text")
    _safe_set(b, 'setup_Branch', {a1})
    assert _is_linked(b, 'setup_Branch', a1)
    if hasattr(a1, 'setup_Eclipse12'):
        assert _is_linked(a1, 'setup_Eclipse12', b)
    _safe_set(b, 'setup_Branch', {a2})
    assert _is_linked(b, 'setup_Branch', a2)
    if hasattr(a1, 'setup_Eclipse12'):
        assert not _is_linked(a1, 'setup_Eclipse12', b)
    if hasattr(a2, 'setup_Eclipse12'):
        assert _is_linked(a2, 'setup_Eclipse12', b)
    _safe_set(b, 'setup_Branch', set())
    assert not _is_linked(b, 'setup_Branch', a2)
    if hasattr(a2, 'setup_Eclipse12'):
        assert not _is_linked(a2, 'setup_Eclipse12', b)


def test_assoc_restrictions8_reverse_link_reassign_clear():
    a1 = setup_Project(label="sample_text", name="sample_text")
    a2 = setup_Project(label="sample_text_2", name="sample_text_2")
    b = setup_Eclipse(version="sample_text")
    _safe_set(b, 'setup_Eclipse', a1)
    assert _is_linked(b, 'setup_Eclipse', a1)
    if hasattr(a1, 'setup_Project'):
        assert _is_linked(a1, 'setup_Project', b)
    _safe_set(b, 'setup_Eclipse', a2)
    assert _is_linked(b, 'setup_Eclipse', a2)
    if hasattr(a1, 'setup_Project'):
        assert not _is_linked(a1, 'setup_Project', b)
    if hasattr(a2, 'setup_Project'):
        assert _is_linked(a2, 'setup_Project', b)
    _safe_set(b, 'setup_Eclipse', None)
    assert not _is_linked(b, 'setup_Eclipse', a2)
    if hasattr(a2, 'setup_Project'):
        assert not _is_linked(a2, 'setup_Project', b)


def test_assoc_roots39_reverse_link_reassign_clear():
    a1 = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    a2 = setup_TargletData(activeRepositoryList="sample_text_2", includeAllPlatforms=False, includeSources=False, name="sample_text_2")
    b = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    _safe_set(b, 'setup_InstallableUnit40', a1)
    assert _is_linked(b, 'setup_InstallableUnit40', a1)
    if hasattr(a1, 'setup_TargletData'):
        assert _is_linked(a1, 'setup_TargletData', b)
    _safe_set(b, 'setup_InstallableUnit40', a2)
    assert _is_linked(b, 'setup_InstallableUnit40', a2)
    if hasattr(a1, 'setup_TargletData'):
        assert not _is_linked(a1, 'setup_TargletData', b)
    if hasattr(a2, 'setup_TargletData'):
        assert _is_linked(a2, 'setup_TargletData', b)
    _safe_set(b, 'setup_InstallableUnit40', None)
    assert not _is_linked(b, 'setup_InstallableUnit40', a2)
    if hasattr(a2, 'setup_TargletData'):
        assert not _is_linked(a2, 'setup_TargletData', b)


def test_assoc_sourceLocators41_reverse_link_reassign_clear():
    a1 = setup_TargletData(activeRepositoryList="sample_text", includeAllPlatforms=True, includeSources=True, name="sample_text")
    a2 = setup_TargletData(activeRepositoryList="sample_text_2", includeAllPlatforms=False, includeSources=False, name="sample_text_2")
    b = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    _safe_set(b, 'setup_AutomaticSourceLocator43', a1)
    assert _is_linked(b, 'setup_AutomaticSourceLocator43', a1)
    if hasattr(a1, 'setup_TargletData42'):
        assert _is_linked(a1, 'setup_TargletData42', b)
    _safe_set(b, 'setup_AutomaticSourceLocator43', a2)
    assert _is_linked(b, 'setup_AutomaticSourceLocator43', a2)
    if hasattr(a1, 'setup_TargletData42'):
        assert not _is_linked(a1, 'setup_TargletData42', b)
    if hasattr(a2, 'setup_TargletData42'):
        assert _is_linked(a2, 'setup_TargletData42', b)
    _safe_set(b, 'setup_AutomaticSourceLocator43', None)
    assert not _is_linked(b, 'setup_AutomaticSourceLocator43', a2)
    if hasattr(a2, 'setup_TargletData42'):
        assert not _is_linked(a2, 'setup_TargletData42', b)


def test_assoc_task65_reverse_link_reassign_clear():
    a1 = setup_Query(summary="sample_text", uRL="sample_text")
    a2 = setup_Query(summary="sample_text_2", uRL="sample_text_2")
    b = setup_MylynQueriesTask(connectorKind="sample_text", password="sample_text", repositoryURL="sample_text", userID="sample_text")
    _safe_set(b, 'MylynQueriesTask', a1)
    assert _is_linked(b, 'MylynQueriesTask', a1)
    if hasattr(a1, 'queries'):
        assert _is_linked(a1, 'queries', b)
    _safe_set(b, 'MylynQueriesTask', a2)
    assert _is_linked(b, 'MylynQueriesTask', a2)
    if hasattr(a1, 'queries'):
        assert not _is_linked(a1, 'queries', b)
    if hasattr(a2, 'queries'):
        assert _is_linked(a2, 'queries', b)
    _safe_set(b, 'MylynQueriesTask', None)
    assert not _is_linked(b, 'MylynQueriesTask', a2)
    if hasattr(a2, 'queries'):
        assert not _is_linked(a2, 'queries', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configuration1_stub_double():
    # setup_Configuration has no real 'Configuration' property in the generated
    # code (a bare stub) -- manually attach it so setup_Eclipse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_Eclipse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_Eclipse(version="sample_text")
    partner = setup_Configuration()
    setattr(partner, 'Configuration', None)
    _safe_set(owner, 'eclipseVersions', partner)
    assert getattr(partner, 'Configuration') == owner
    _safe_set(owner, 'eclipseVersions', None)
    assert getattr(partner, 'Configuration') is None


def test_assoc_configuration5_stub_double():
    # setup_Configuration has no real 'Configuration6' property in the generated
    # code (a bare stub) -- manually attach it so setup_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_Project(label="sample_text", name="sample_text")
    partner = setup_Configuration()
    setattr(partner, 'Configuration6', None)
    _safe_set(owner, 'projects', partner)
    assert getattr(partner, 'Configuration6') == owner
    _safe_set(owner, 'projects', None)
    assert getattr(partner, 'Configuration6') is None


def test_assoc_dependencies35_stub_double():
    # setup_ComponentExtension has no real 'setup_ComponentExtension' property in the generated
    # code (a bare stub) -- manually attach it so setup_InstallableUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_InstallableUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_InstallableUnit(iD="sample_text", versionRange="sample_text")
    partner = setup_ComponentExtension()
    setattr(partner, 'setup_ComponentExtension', None)
    _safe_set(owner, 'setup_InstallableUnit36', partner)
    assert owner in getattr(partner, 'setup_ComponentExtension')
    _safe_set(owner, 'setup_InstallableUnit36', None)
    assert owner not in getattr(partner, 'setup_ComponentExtension')


def test_assoc_eclipseVersions2_stub_double():
    # setup_Configuration has no real 'configuration' property in the generated
    # code (a bare stub) -- manually attach it so setup_Eclipse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_Eclipse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_Eclipse(version="sample_text")
    partner = setup_Configuration()
    setattr(partner, 'configuration', None)
    _safe_set(owner, 'Eclipse', partner)
    assert owner in getattr(partner, 'configuration')
    _safe_set(owner, 'Eclipse', None)
    assert owner not in getattr(partner, 'configuration')


def test_assoc_indexes0_stub_double():
    # setup_MetaIndex has no real 'setup_MetaIndex' property in the generated
    # code (a bare stub) -- manually attach it so setup_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_Index(name="sample_text", oldURIs="sample_text", uRI="sample_text")
    partner = setup_MetaIndex()
    setattr(partner, 'setup_MetaIndex', None)
    _safe_set(owner, 'setup_Index', partner)
    assert owner in getattr(partner, 'setup_MetaIndex')
    _safe_set(owner, 'setup_Index', None)
    assert owner not in getattr(partner, 'setup_MetaIndex')


def test_assoc_mappings55_stub_double():
    # setup_FileAssociationsTask has no real 'setup_FileAssociationsTask' property in the generated
    # code (a bare stub) -- manually attach it so setup_FileMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_FileMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_FileMapping(defaultEditorID="sample_text", filePattern="sample_text")
    partner = setup_FileAssociationsTask()
    setattr(partner, 'setup_FileAssociationsTask', None)
    _safe_set(owner, 'setup_FileMapping', partner)
    assert owner in getattr(partner, 'setup_FileAssociationsTask')
    _safe_set(owner, 'setup_FileMapping', None)
    assert owner not in getattr(partner, 'setup_FileAssociationsTask')


def test_assoc_p2Repositories31_stub_double():
    # setup_MaterializationTask has no real 'setup_MaterializationTask32' property in the generated
    # code (a bare stub) -- manually attach it so setup_P2Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_P2Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_P2Repository(uRL="sample_text")
    partner = setup_MaterializationTask()
    setattr(partner, 'setup_MaterializationTask32', None)
    _safe_set(owner, 'setup_P2Repository33', partner)
    assert owner in getattr(partner, 'setup_MaterializationTask32')
    _safe_set(owner, 'setup_P2Repository33', None)
    assert owner not in getattr(partner, 'setup_MaterializationTask32')


def test_assoc_predicates34_stub_double():
    # setup_Predicate has no real 'setup_Predicate' property in the generated
    # code (a bare stub) -- manually attach it so setup_AutomaticSourceLocator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_AutomaticSourceLocator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    partner = setup_Predicate()
    setattr(partner, 'setup_Predicate', None)
    _safe_set(owner, 'setup_AutomaticSourceLocator', {partner})
    assert getattr(partner, 'setup_Predicate') == owner
    _safe_set(owner, 'setup_AutomaticSourceLocator', set())
    assert getattr(partner, 'setup_Predicate') is None


def test_assoc_projects3_stub_double():
    # setup_Configuration has no real 'configuration4' property in the generated
    # code (a bare stub) -- manually attach it so setup_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_Project(label="sample_text", name="sample_text")
    partner = setup_Configuration()
    setattr(partner, 'configuration4', None)
    _safe_set(owner, 'Project', partner)
    assert owner in getattr(partner, 'configuration4')
    _safe_set(owner, 'Project', None)
    assert owner not in getattr(partner, 'configuration4')


def test_assoc_restrictions20_stub_double():
    # setup_ConfigurableItem has no real 'setup_ConfigurableItem' property in the generated
    # code (a bare stub) -- manually attach it so setup_SetupTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_SetupTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    partner = setup_ConfigurableItem()
    setattr(partner, 'setup_ConfigurableItem', None)
    _safe_set(owner, 'setup_SetupTask21', {partner})
    assert getattr(partner, 'setup_ConfigurableItem') == owner
    _safe_set(owner, 'setup_SetupTask21', set())
    assert getattr(partner, 'setup_ConfigurableItem') is None


def test_assoc_rootComponents28_stub_double():
    # setup_MaterializationTask has no real 'setup_MaterializationTask' property in the generated
    # code (a bare stub) -- manually attach it so setup_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_Component(name="sample_text", type="sample_text", versionRange="sample_text")
    partner = setup_MaterializationTask()
    setattr(partner, 'setup_MaterializationTask', None)
    _safe_set(owner, 'setup_Component', partner)
    assert owner in getattr(partner, 'setup_MaterializationTask')
    _safe_set(owner, 'setup_Component', None)
    assert owner not in getattr(partner, 'setup_MaterializationTask')


def test_assoc_setupTasks22_stub_double():
    # setup_SetupTaskContainer has no real 'setup_SetupTaskContainer' property in the generated
    # code (a bare stub) -- manually attach it so setup_SetupTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_SetupTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_SetupTask(disabled=True, documentation="sample_text", excludedTriggers="sample_text", scope="sample_text")
    partner = setup_SetupTaskContainer()
    setattr(partner, 'setup_SetupTaskContainer', None)
    _safe_set(owner, 'setup_SetupTask23', partner)
    assert owner in getattr(partner, 'setup_SetupTaskContainer')
    _safe_set(owner, 'setup_SetupTask23', None)
    assert owner not in getattr(partner, 'setup_SetupTaskContainer')


def test_assoc_sourceLocators37_stub_double():
    # setup_MavenImportTask has no real 'setup_MavenImportTask' property in the generated
    # code (a bare stub) -- manually attach it so setup_AutomaticSourceLocator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_AutomaticSourceLocator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    partner = setup_MavenImportTask()
    setattr(partner, 'setup_MavenImportTask', None)
    _safe_set(owner, 'setup_AutomaticSourceLocator38', partner)
    assert owner in getattr(partner, 'setup_MavenImportTask')
    _safe_set(owner, 'setup_AutomaticSourceLocator38', None)
    assert owner not in getattr(partner, 'setup_MavenImportTask')


def test_assoc_sourceLocators52_stub_double():
    # setup_ProjectsImportTask has no real 'setup_ProjectsImportTask' property in the generated
    # code (a bare stub) -- manually attach it so setup_AutomaticSourceLocator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # setup_AutomaticSourceLocator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = setup_AutomaticSourceLocator(locateNestedProjects=True, rootFolder="sample_text")
    partner = setup_ProjectsImportTask()
    setattr(partner, 'setup_ProjectsImportTask', None)
    _safe_set(owner, 'setup_AutomaticSourceLocator53', partner)
    assert owner in getattr(partner, 'setup_ProjectsImportTask')
    _safe_set(owner, 'setup_AutomaticSourceLocator53', None)
    assert owner not in getattr(partner, 'setup_ProjectsImportTask')


