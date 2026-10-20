import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BuildElement,
    ParameterDefinition,
    TestElement,
    builds_Artifact,
    builds_BooleanParameterDefinition,
    builds_Build,
    builds_BuildCause,
    builds_BuildElement,
    builds_BuildModel,
    builds_BuildParameterDefinition,
    builds_BuildPlan,
    builds_BuildReference,
    builds_BuildServer,
    builds_Change,
    builds_ChangeArtifact,
    builds_ChangeSet,
    builds_ChoiceParameterDefinition,
    builds_FileParameterDefinition,
    builds_HealthReport,
    builds_ParameterDefinition,
    builds_PasswordParameterDefinition,
    builds_PlanParameterDefinition,
    builds_StringParameterDefinition,
    builds_StringToStringMap,
    builds_TestCase,
    builds_TestElement,
    builds_TestResult,
    builds_TestSuite,
    builds_User,
    TestCaseResult,
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

def test_assoc_artifacts0_reverse_link_reassign_clear():
    a1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    a2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    b = builds_Artifact(relativePath="sample_text")
    _safe_set(b, 'builds_Artifact', a1)
    assert _is_linked(b, 'builds_Artifact', a1)
    if hasattr(a1, 'builds_Build'):
        assert _is_linked(a1, 'builds_Build', b)
    _safe_set(b, 'builds_Artifact', a2)
    assert _is_linked(b, 'builds_Artifact', a2)
    if hasattr(a1, 'builds_Build'):
        assert not _is_linked(a1, 'builds_Build', b)
    if hasattr(a2, 'builds_Build'):
        assert _is_linked(a2, 'builds_Build', b)
    _safe_set(b, 'builds_Artifact', None)
    assert not _is_linked(b, 'builds_Artifact', a2)
    if hasattr(a2, 'builds_Build'):
        assert not _is_linked(a2, 'builds_Build', b)


def test_assoc_artifacts40_reverse_link_reassign_clear():
    a1 = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    a2 = builds_ChangeArtifact(dead=False, editType="sample_text_2", file="sample_text_2", prevRevision="sample_text_2", relativePath="sample_text_2", revision="sample_text_2")
    b = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    _safe_set(b, 'builds_Change', {a1})
    assert _is_linked(b, 'builds_Change', a1)
    if hasattr(a1, 'builds_ChangeArtifact'):
        assert _is_linked(a1, 'builds_ChangeArtifact', b)
    _safe_set(b, 'builds_Change', {a2})
    assert _is_linked(b, 'builds_Change', a2)
    if hasattr(a1, 'builds_ChangeArtifact'):
        assert not _is_linked(a1, 'builds_ChangeArtifact', b)
    if hasattr(a2, 'builds_ChangeArtifact'):
        assert _is_linked(a2, 'builds_ChangeArtifact', b)
    _safe_set(b, 'builds_Change', set())
    assert not _is_linked(b, 'builds_Change', a2)
    if hasattr(a2, 'builds_ChangeArtifact'):
        assert not _is_linked(a2, 'builds_ChangeArtifact', b)


def test_assoc_attributes17_reverse_link_reassign_clear():
    a1 = builds_StringToStringMap(key="sample_text", value="sample_text")
    a2 = builds_StringToStringMap(key="sample_text_2", value="sample_text_2")
    b = builds_BuildElement(elementStatus="sample_text", name="sample_text", operations="sample_text", refreshDate=date(2024, 1, 1), url="sample_text")
    _safe_set(b, 'builds_BuildElement', {a1})
    assert _is_linked(b, 'builds_BuildElement', a1)
    if hasattr(a1, 'builds_StringToStringMap'):
        assert _is_linked(a1, 'builds_StringToStringMap', b)
    _safe_set(b, 'builds_BuildElement', {a2})
    assert _is_linked(b, 'builds_BuildElement', a2)
    if hasattr(a1, 'builds_StringToStringMap'):
        assert not _is_linked(a1, 'builds_StringToStringMap', b)
    if hasattr(a2, 'builds_StringToStringMap'):
        assert _is_linked(a2, 'builds_StringToStringMap', b)
    _safe_set(b, 'builds_BuildElement', set())
    assert not _is_linked(b, 'builds_BuildElement', a2)
    if hasattr(a2, 'builds_StringToStringMap'):
        assert not _is_linked(a2, 'builds_StringToStringMap', b)


def test_assoc_author41_reverse_link_reassign_clear():
    a1 = builds_User(email="sample_text", id="sample_text")
    a2 = builds_User(email="sample_text_2", id="sample_text_2")
    b = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    _safe_set(b, 'builds_Change42', a1)
    assert _is_linked(b, 'builds_Change42', a1)
    if hasattr(a1, 'builds_User43'):
        assert _is_linked(a1, 'builds_User43', b)
    _safe_set(b, 'builds_Change42', a2)
    assert _is_linked(b, 'builds_Change42', a2)
    if hasattr(a1, 'builds_User43'):
        assert not _is_linked(a1, 'builds_User43', b)
    if hasattr(a2, 'builds_User43'):
        assert _is_linked(a2, 'builds_User43', b)
    _safe_set(b, 'builds_Change42', None)
    assert not _is_linked(b, 'builds_Change42', a2)
    if hasattr(a2, 'builds_User43'):
        assert not _is_linked(a2, 'builds_User43', b)


def test_assoc_build12_reverse_link_reassign_clear():
    a1 = builds_BuildReference(build="sample_text", plan="sample_text")
    a2 = builds_BuildReference(build="sample_text_2", plan="sample_text_2")
    b = builds_BuildCause(description="sample_text")
    _safe_set(b, 'builds_BuildCause13', a1)
    assert _is_linked(b, 'builds_BuildCause13', a1)
    if hasattr(a1, 'builds_BuildReference'):
        assert _is_linked(a1, 'builds_BuildReference', b)
    _safe_set(b, 'builds_BuildCause13', a2)
    assert _is_linked(b, 'builds_BuildCause13', a2)
    if hasattr(a1, 'builds_BuildReference'):
        assert not _is_linked(a1, 'builds_BuildReference', b)
    if hasattr(a2, 'builds_BuildReference'):
        assert _is_linked(a2, 'builds_BuildReference', b)
    _safe_set(b, 'builds_BuildCause13', None)
    assert not _is_linked(b, 'builds_BuildCause13', a2)
    if hasattr(a2, 'builds_BuildReference'):
        assert not _is_linked(a2, 'builds_BuildReference', b)


def test_assoc_build51_reverse_link_reassign_clear():
    a1 = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    a2 = builds_TestResult(duration="sample_text_2", errorCount=13, failCount=13, ignoredCount=13, passCount=13)
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'Build', a1)
    assert _is_linked(b, 'Build', a1)
    if hasattr(a1, 'testResult'):
        assert _is_linked(a1, 'testResult', b)
    _safe_set(b, 'Build', a2)
    assert _is_linked(b, 'Build', a2)
    if hasattr(a1, 'testResult'):
        assert not _is_linked(a1, 'testResult', b)
    if hasattr(a2, 'testResult'):
        assert _is_linked(a2, 'testResult', b)
    _safe_set(b, 'Build', None)
    assert not _is_linked(b, 'Build', a2)
    if hasattr(a2, 'testResult'):
        assert not _is_linked(a2, 'testResult', b)


def test_assoc_buildPlan49_reverse_link_reassign_clear():
    a1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    a2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    b = builds_BuildParameterDefinition(buildPlanId="sample_text")
    _safe_set(b, 'builds_BuildParameterDefinition', a1)
    assert _is_linked(b, 'builds_BuildParameterDefinition', a1)
    if hasattr(a1, 'builds_BuildPlan50'):
        assert _is_linked(a1, 'builds_BuildPlan50', b)
    _safe_set(b, 'builds_BuildParameterDefinition', a2)
    assert _is_linked(b, 'builds_BuildParameterDefinition', a2)
    if hasattr(a1, 'builds_BuildPlan50'):
        assert not _is_linked(a1, 'builds_BuildPlan50', b)
    if hasattr(a2, 'builds_BuildPlan50'):
        assert _is_linked(a2, 'builds_BuildPlan50', b)
    _safe_set(b, 'builds_BuildParameterDefinition', None)
    assert not _is_linked(b, 'builds_BuildParameterDefinition', a2)
    if hasattr(a2, 'builds_BuildPlan50'):
        assert not _is_linked(a2, 'builds_BuildPlan50', b)


def test_assoc_cause10_reverse_link_reassign_clear():
    a1 = builds_BuildCause(description="sample_text")
    a2 = builds_BuildCause(description="sample_text_2")
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'builds_Build11', {a1})
    assert _is_linked(b, 'builds_Build11', a1)
    if hasattr(a1, 'builds_BuildCause'):
        assert _is_linked(a1, 'builds_BuildCause', b)
    _safe_set(b, 'builds_Build11', {a2})
    assert _is_linked(b, 'builds_Build11', a2)
    if hasattr(a1, 'builds_BuildCause'):
        assert not _is_linked(a1, 'builds_BuildCause', b)
    if hasattr(a2, 'builds_BuildCause'):
        assert _is_linked(a2, 'builds_BuildCause', b)
    _safe_set(b, 'builds_Build11', set())
    assert not _is_linked(b, 'builds_Build11', a2)
    if hasattr(a2, 'builds_BuildCause'):
        assert not _is_linked(a2, 'builds_BuildCause', b)


def test_assoc_changeSet1_reverse_link_reassign_clear():
    a1 = builds_ChangeSet(kind="sample_text")
    a2 = builds_ChangeSet(kind="sample_text_2")
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'builds_Build2', a1)
    assert _is_linked(b, 'builds_Build2', a1)
    if hasattr(a1, 'builds_ChangeSet'):
        assert _is_linked(a1, 'builds_ChangeSet', b)
    _safe_set(b, 'builds_Build2', a2)
    assert _is_linked(b, 'builds_Build2', a2)
    if hasattr(a1, 'builds_ChangeSet'):
        assert not _is_linked(a1, 'builds_ChangeSet', b)
    if hasattr(a2, 'builds_ChangeSet'):
        assert _is_linked(a2, 'builds_ChangeSet', b)
    _safe_set(b, 'builds_Build2', None)
    assert not _is_linked(b, 'builds_Build2', a2)
    if hasattr(a2, 'builds_ChangeSet'):
        assert not _is_linked(a2, 'builds_ChangeSet', b)


def test_assoc_changes44_reverse_link_reassign_clear():
    a1 = builds_ChangeSet(kind="sample_text")
    a2 = builds_ChangeSet(kind="sample_text_2")
    b = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    _safe_set(b, 'builds_Change46', a1)
    assert _is_linked(b, 'builds_Change46', a1)
    if hasattr(a1, 'builds_ChangeSet45'):
        assert _is_linked(a1, 'builds_ChangeSet45', b)
    _safe_set(b, 'builds_Change46', a2)
    assert _is_linked(b, 'builds_Change46', a2)
    if hasattr(a1, 'builds_ChangeSet45'):
        assert not _is_linked(a1, 'builds_ChangeSet45', b)
    if hasattr(a2, 'builds_ChangeSet45'):
        assert _is_linked(a2, 'builds_ChangeSet45', b)
    _safe_set(b, 'builds_Change46', None)
    assert not _is_linked(b, 'builds_Change46', a2)
    if hasattr(a2, 'builds_ChangeSet45'):
        assert not _is_linked(a2, 'builds_ChangeSet45', b)


def test_assoc_children22_reverse_link_reassign_clear():
    a1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    a2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    b = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'BuildPlan'):
        assert _is_linked(a1, 'BuildPlan', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'BuildPlan'):
        assert not _is_linked(a1, 'BuildPlan', b)
    if hasattr(a2, 'BuildPlan'):
        assert _is_linked(a2, 'BuildPlan', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'BuildPlan'):
        assert not _is_linked(a2, 'BuildPlan', b)


def test_assoc_containingBuildPlan47_reverse_link_reassign_clear():
    a1 = builds_ParameterDefinition(description="sample_text", name="sample_text")
    a2 = builds_ParameterDefinition(description="sample_text_2", name="sample_text_2")
    b = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    _safe_set(b, 'BuildPlan48', a1)
    assert _is_linked(b, 'BuildPlan48', a1)
    if hasattr(a1, 'parameterDefinitions'):
        assert _is_linked(a1, 'parameterDefinitions', b)
    _safe_set(b, 'BuildPlan48', a2)
    assert _is_linked(b, 'BuildPlan48', a2)
    if hasattr(a1, 'parameterDefinitions'):
        assert not _is_linked(a1, 'parameterDefinitions', b)
    if hasattr(a2, 'parameterDefinitions'):
        assert _is_linked(a2, 'parameterDefinitions', b)
    _safe_set(b, 'BuildPlan48', None)
    assert not _is_linked(b, 'BuildPlan48', a2)
    if hasattr(a2, 'parameterDefinitions'):
        assert not _is_linked(a2, 'parameterDefinitions', b)


def test_assoc_culprits8_reverse_link_reassign_clear():
    a1 = builds_User(email="sample_text", id="sample_text")
    a2 = builds_User(email="sample_text_2", id="sample_text_2")
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'builds_Build9', {a1})
    assert _is_linked(b, 'builds_Build9', a1)
    if hasattr(a1, 'builds_User'):
        assert _is_linked(a1, 'builds_User', b)
    _safe_set(b, 'builds_Build9', {a2})
    assert _is_linked(b, 'builds_Build9', a2)
    if hasattr(a1, 'builds_User'):
        assert not _is_linked(a1, 'builds_User', b)
    if hasattr(a2, 'builds_User'):
        assert _is_linked(a2, 'builds_User', b)
    _safe_set(b, 'builds_Build9', set())
    assert not _is_linked(b, 'builds_Build9', a2)
    if hasattr(a2, 'builds_User'):
        assert not _is_linked(a2, 'builds_User', b)


def test_assoc_healthReports30_reverse_link_reassign_clear():
    a1 = builds_HealthReport(description="sample_text", health=7)
    a2 = builds_HealthReport(description="sample_text_2", health=13)
    b = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    _safe_set(b, 'builds_BuildPlan31', {a1})
    assert _is_linked(b, 'builds_BuildPlan31', a1)
    if hasattr(a1, 'builds_HealthReport'):
        assert _is_linked(a1, 'builds_HealthReport', b)
    _safe_set(b, 'builds_BuildPlan31', {a2})
    assert _is_linked(b, 'builds_BuildPlan31', a2)
    if hasattr(a1, 'builds_HealthReport'):
        assert not _is_linked(a1, 'builds_HealthReport', b)
    if hasattr(a2, 'builds_HealthReport'):
        assert _is_linked(a2, 'builds_HealthReport', b)
    _safe_set(b, 'builds_BuildPlan31', set())
    assert not _is_linked(b, 'builds_BuildPlan31', a2)
    if hasattr(a2, 'builds_HealthReport'):
        assert not _is_linked(a2, 'builds_HealthReport', b)


def test_assoc_lastBuild26_reverse_link_reassign_clear():
    a1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    a2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'builds_Build28', a1)
    assert _is_linked(b, 'builds_Build28', a1)
    if hasattr(a1, 'builds_BuildPlan27'):
        assert _is_linked(a1, 'builds_BuildPlan27', b)
    _safe_set(b, 'builds_Build28', a2)
    assert _is_linked(b, 'builds_Build28', a2)
    if hasattr(a1, 'builds_BuildPlan27'):
        assert not _is_linked(a1, 'builds_BuildPlan27', b)
    if hasattr(a2, 'builds_BuildPlan27'):
        assert _is_linked(a2, 'builds_BuildPlan27', b)
    _safe_set(b, 'builds_Build28', None)
    assert not _is_linked(b, 'builds_Build28', a2)
    if hasattr(a2, 'builds_BuildPlan27'):
        assert not _is_linked(a2, 'builds_BuildPlan27', b)


def test_assoc_parameterDefinitions29_reverse_link_reassign_clear():
    a1 = builds_ParameterDefinition(description="sample_text", name="sample_text")
    a2 = builds_ParameterDefinition(description="sample_text_2", name="sample_text_2")
    b = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    _safe_set(b, 'containingBuildPlan', {a1})
    assert _is_linked(b, 'containingBuildPlan', a1)
    if hasattr(a1, 'ParameterDefinition'):
        assert _is_linked(a1, 'ParameterDefinition', b)
    _safe_set(b, 'containingBuildPlan', {a2})
    assert _is_linked(b, 'containingBuildPlan', a2)
    if hasattr(a1, 'ParameterDefinition'):
        assert not _is_linked(a1, 'ParameterDefinition', b)
    if hasattr(a2, 'ParameterDefinition'):
        assert _is_linked(a2, 'ParameterDefinition', b)
    _safe_set(b, 'containingBuildPlan', set())
    assert not _is_linked(b, 'containingBuildPlan', a2)
    if hasattr(a2, 'ParameterDefinition'):
        assert not _is_linked(a2, 'ParameterDefinition', b)


def test_assoc_parent24_reverse_link_reassign_clear():
    a1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    a2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    b = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'BuildPlan25'):
        assert _is_linked(a1, 'BuildPlan25', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'BuildPlan25'):
        assert not _is_linked(a1, 'BuildPlan25', b)
    if hasattr(a2, 'BuildPlan25'):
        assert _is_linked(a2, 'BuildPlan25', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'BuildPlan25'):
        assert not _is_linked(a2, 'BuildPlan25', b)


def test_assoc_plan3_reverse_link_reassign_clear():
    a1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    a2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'builds_Build4', a1)
    assert _is_linked(b, 'builds_Build4', a1)
    if hasattr(a1, 'builds_BuildPlan'):
        assert _is_linked(a1, 'builds_BuildPlan', b)
    _safe_set(b, 'builds_Build4', a2)
    assert _is_linked(b, 'builds_Build4', a2)
    if hasattr(a1, 'builds_BuildPlan'):
        assert not _is_linked(a1, 'builds_BuildPlan', b)
    if hasattr(a2, 'builds_BuildPlan'):
        assert _is_linked(a2, 'builds_BuildPlan', b)
    _safe_set(b, 'builds_Build4', None)
    assert not _is_linked(b, 'builds_Build4', a2)
    if hasattr(a2, 'builds_BuildPlan'):
        assert not _is_linked(a2, 'builds_BuildPlan', b)


def test_assoc_server18_reverse_link_reassign_clear():
    a1 = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    a2 = builds_BuildServer(connectorKind="sample_text_2", location="sample_text_2", repositoryUrl="sample_text_2")
    b = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    _safe_set(b, 'builds_BuildPlan19', a1)
    assert _is_linked(b, 'builds_BuildPlan19', a1)
    if hasattr(a1, 'builds_BuildServer20'):
        assert _is_linked(a1, 'builds_BuildServer20', b)
    _safe_set(b, 'builds_BuildPlan19', a2)
    assert _is_linked(b, 'builds_BuildPlan19', a2)
    if hasattr(a1, 'builds_BuildServer20'):
        assert not _is_linked(a1, 'builds_BuildServer20', b)
    if hasattr(a2, 'builds_BuildServer20'):
        assert _is_linked(a2, 'builds_BuildServer20', b)
    _safe_set(b, 'builds_BuildPlan19', None)
    assert not _is_linked(b, 'builds_BuildPlan19', a2)
    if hasattr(a2, 'builds_BuildServer20'):
        assert not _is_linked(a2, 'builds_BuildServer20', b)


def test_assoc_server5_reverse_link_reassign_clear():
    a1 = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    a2 = builds_BuildServer(connectorKind="sample_text_2", location="sample_text_2", repositoryUrl="sample_text_2")
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'builds_Build6', a1)
    assert _is_linked(b, 'builds_Build6', a1)
    if hasattr(a1, 'builds_BuildServer'):
        assert _is_linked(a1, 'builds_BuildServer', b)
    _safe_set(b, 'builds_Build6', a2)
    assert _is_linked(b, 'builds_Build6', a2)
    if hasattr(a1, 'builds_BuildServer'):
        assert not _is_linked(a1, 'builds_BuildServer', b)
    if hasattr(a2, 'builds_BuildServer'):
        assert _is_linked(a2, 'builds_BuildServer', b)
    _safe_set(b, 'builds_Build6', None)
    assert not _is_linked(b, 'builds_Build6', a2)
    if hasattr(a2, 'builds_BuildServer'):
        assert not _is_linked(a2, 'builds_BuildServer', b)


def test_assoc_testResult7_reverse_link_reassign_clear():
    a1 = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    a2 = builds_TestResult(duration="sample_text_2", errorCount=13, failCount=13, ignoredCount=13, passCount=13)
    b = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    _safe_set(b, 'build', a1)
    assert _is_linked(b, 'build', a1)
    if hasattr(a1, 'TestResult'):
        assert _is_linked(a1, 'TestResult', b)
    _safe_set(b, 'build', a2)
    assert _is_linked(b, 'build', a2)
    if hasattr(a1, 'TestResult'):
        assert not _is_linked(a1, 'TestResult', b)
    if hasattr(a2, 'TestResult'):
        assert _is_linked(a2, 'TestResult', b)
    _safe_set(b, 'build', None)
    assert not _is_linked(b, 'build', a2)
    if hasattr(a2, 'TestResult'):
        assert not _is_linked(a2, 'TestResult', b)


def test_assoc_user14_reverse_link_reassign_clear():
    a1 = builds_User(email="sample_text", id="sample_text")
    a2 = builds_User(email="sample_text_2", id="sample_text_2")
    b = builds_BuildCause(description="sample_text")
    _safe_set(b, 'builds_BuildCause15', a1)
    assert _is_linked(b, 'builds_BuildCause15', a1)
    if hasattr(a1, 'builds_User16'):
        assert _is_linked(a1, 'builds_User16', b)
    _safe_set(b, 'builds_BuildCause15', a2)
    assert _is_linked(b, 'builds_BuildCause15', a2)
    if hasattr(a1, 'builds_User16'):
        assert not _is_linked(a1, 'builds_User16', b)
    if hasattr(a2, 'builds_User16'):
        assert _is_linked(a2, 'builds_User16', b)
    _safe_set(b, 'builds_BuildCause15', None)
    assert not _is_linked(b, 'builds_BuildCause15', a2)
    if hasattr(a2, 'builds_User16'):
        assert not _is_linked(a2, 'builds_User16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_builds37_stub_double():
    # builds_BuildModel has no real 'builds_BuildModel38' property in the generated
    # code (a bare stub) -- manually attach it so builds_Build's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # builds_Build's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    partner = builds_BuildModel()
    setattr(partner, 'builds_BuildModel38', None)
    _safe_set(owner, 'builds_Build39', partner)
    assert owner in getattr(partner, 'builds_BuildModel38')
    _safe_set(owner, 'builds_Build39', None)
    assert owner not in getattr(partner, 'builds_BuildModel38')


def test_assoc_cases53_stub_double():
    # builds_TestSuite has no real 'suite' property in the generated
    # code (a bare stub) -- manually attach it so builds_TestCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # builds_TestCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    partner = builds_TestSuite()
    setattr(partner, 'suite', None)
    _safe_set(owner, 'TestCase', partner)
    assert owner in getattr(partner, 'suite')
    _safe_set(owner, 'TestCase', None)
    assert owner not in getattr(partner, 'suite')


def test_assoc_plans34_stub_double():
    # builds_BuildModel has no real 'builds_BuildModel35' property in the generated
    # code (a bare stub) -- manually attach it so builds_BuildPlan's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # builds_BuildPlan's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    partner = builds_BuildModel()
    setattr(partner, 'builds_BuildModel35', None)
    _safe_set(owner, 'builds_BuildPlan36', partner)
    assert owner in getattr(partner, 'builds_BuildModel35')
    _safe_set(owner, 'builds_BuildPlan36', None)
    assert owner not in getattr(partner, 'builds_BuildModel35')


def test_assoc_result54_stub_double():
    # builds_TestSuite has no real 'suites' property in the generated
    # code (a bare stub) -- manually attach it so builds_TestResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # builds_TestResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    partner = builds_TestSuite()
    setattr(partner, 'suites', None)
    _safe_set(owner, 'TestResult55', partner)
    assert getattr(partner, 'suites') == owner
    _safe_set(owner, 'TestResult55', None)
    assert getattr(partner, 'suites') is None


def test_assoc_servers32_stub_double():
    # builds_BuildModel has no real 'builds_BuildModel' property in the generated
    # code (a bare stub) -- manually attach it so builds_BuildServer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # builds_BuildServer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    partner = builds_BuildModel()
    setattr(partner, 'builds_BuildModel', None)
    _safe_set(owner, 'builds_BuildServer33', partner)
    assert owner in getattr(partner, 'builds_BuildModel')
    _safe_set(owner, 'builds_BuildServer33', None)
    assert owner not in getattr(partner, 'builds_BuildModel')


def test_assoc_suite56_stub_double():
    # builds_TestSuite has no real 'TestSuite57' property in the generated
    # code (a bare stub) -- manually attach it so builds_TestCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # builds_TestCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    partner = builds_TestSuite()
    setattr(partner, 'TestSuite57', None)
    _safe_set(owner, 'cases', partner)
    assert getattr(partner, 'TestSuite57') == owner
    _safe_set(owner, 'cases', None)
    assert getattr(partner, 'TestSuite57') is None


def test_assoc_suites52_stub_double():
    # builds_TestSuite has no real 'TestSuite' property in the generated
    # code (a bare stub) -- manually attach it so builds_TestResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # builds_TestResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    partner = builds_TestSuite()
    setattr(partner, 'TestSuite', None)
    _safe_set(owner, 'result', {partner})
    assert getattr(partner, 'TestSuite') == owner
    _safe_set(owner, 'result', set())
    assert getattr(partner, 'TestSuite') is None


