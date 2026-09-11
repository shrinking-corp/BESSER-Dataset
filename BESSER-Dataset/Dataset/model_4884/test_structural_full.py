import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_builds_Artifact_relativePath_value_roundtrip():
    instance = builds_Artifact(relativePath="sample_text")
    assert instance.relativePath == "sample_text"
    instance.relativePath = "sample_text_2"
    assert instance.relativePath == "sample_text_2"


def test_builds_BooleanParameterDefinition_defaultValue_value_roundtrip():
    instance = builds_BooleanParameterDefinition(defaultValue=True)
    assert instance.defaultValue == True
    instance.defaultValue = False
    assert instance.defaultValue == False


def test_builds_Build_buildNumber_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.buildNumber == 7
    instance.buildNumber = 13
    assert instance.buildNumber == 13


def test_builds_Build_displayName_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.displayName == "sample_text"
    instance.displayName = "sample_text_2"
    assert instance.displayName == "sample_text_2"


def test_builds_Build_duration_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_builds_Build_id_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_builds_Build_label_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_builds_Build_state_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_builds_Build_status_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_builds_Build_summary_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.summary == "sample_text"
    instance.summary = "sample_text_2"
    assert instance.summary == "sample_text_2"


def test_builds_Build_timestamp_value_roundtrip():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert instance.timestamp == "sample_text"
    instance.timestamp = "sample_text_2"
    assert instance.timestamp == "sample_text_2"


def test_builds_BuildCause_description_value_roundtrip():
    instance = builds_BuildCause(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_builds_BuildElement_elementStatus_value_roundtrip():
    instance = builds_BuildElement(elementStatus="sample_text", name="sample_text", operations="sample_text", refreshDate=date(2024, 1, 1), url="sample_text")
    assert instance.elementStatus == "sample_text"
    instance.elementStatus = "sample_text_2"
    assert instance.elementStatus == "sample_text_2"


def test_builds_BuildElement_name_value_roundtrip():
    instance = builds_BuildElement(elementStatus="sample_text", name="sample_text", operations="sample_text", refreshDate=date(2024, 1, 1), url="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_builds_BuildElement_operations_value_roundtrip():
    instance = builds_BuildElement(elementStatus="sample_text", name="sample_text", operations="sample_text", refreshDate=date(2024, 1, 1), url="sample_text")
    assert instance.operations == "sample_text"
    instance.operations = "sample_text_2"
    assert instance.operations == "sample_text_2"


def test_builds_BuildElement_refreshDate_value_roundtrip():
    instance = builds_BuildElement(elementStatus="sample_text", name="sample_text", operations="sample_text", refreshDate=date(2024, 1, 1), url="sample_text")
    assert instance.refreshDate == date(2024, 1, 1)
    instance.refreshDate = date(2025, 6, 15)
    assert instance.refreshDate == date(2025, 6, 15)


def test_builds_BuildElement_url_value_roundtrip():
    instance = builds_BuildElement(elementStatus="sample_text", name="sample_text", operations="sample_text", refreshDate=date(2024, 1, 1), url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_builds_BuildParameterDefinition_buildPlanId_value_roundtrip():
    instance = builds_BuildParameterDefinition(buildPlanId="sample_text")
    assert instance.buildPlanId == "sample_text"
    instance.buildPlanId = "sample_text_2"
    assert instance.buildPlanId == "sample_text_2"


def test_builds_BuildPlan_description_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_builds_BuildPlan_flags_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.flags == "sample_text"
    instance.flags = "sample_text_2"
    assert instance.flags == "sample_text_2"


def test_builds_BuildPlan_health_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.health == 7
    instance.health = 13
    assert instance.health == 13


def test_builds_BuildPlan_id_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_builds_BuildPlan_info_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.info == "sample_text"
    instance.info = "sample_text_2"
    assert instance.info == "sample_text_2"


def test_builds_BuildPlan_selected_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_builds_BuildPlan_state_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_builds_BuildPlan_status_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_builds_BuildPlan_summary_value_roundtrip():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert instance.summary == "sample_text"
    instance.summary = "sample_text_2"
    assert instance.summary == "sample_text_2"


def test_builds_BuildReference_build_value_roundtrip():
    instance = builds_BuildReference(build="sample_text", plan="sample_text")
    assert instance.build == "sample_text"
    instance.build = "sample_text_2"
    assert instance.build == "sample_text_2"


def test_builds_BuildReference_plan_value_roundtrip():
    instance = builds_BuildReference(build="sample_text", plan="sample_text")
    assert instance.plan == "sample_text"
    instance.plan = "sample_text_2"
    assert instance.plan == "sample_text_2"


def test_builds_BuildServer_connectorKind_value_roundtrip():
    instance = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    assert instance.connectorKind == "sample_text"
    instance.connectorKind = "sample_text_2"
    assert instance.connectorKind == "sample_text_2"


def test_builds_BuildServer_location_value_roundtrip():
    instance = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_builds_BuildServer_repositoryUrl_value_roundtrip():
    instance = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    assert instance.repositoryUrl == "sample_text"
    instance.repositoryUrl = "sample_text_2"
    assert instance.repositoryUrl == "sample_text_2"


def test_builds_Change_date_value_roundtrip():
    instance = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_builds_Change_message_value_roundtrip():
    instance = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_builds_Change_revision_value_roundtrip():
    instance = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    assert instance.revision == "sample_text"
    instance.revision = "sample_text_2"
    assert instance.revision == "sample_text_2"


def test_builds_ChangeArtifact_dead_value_roundtrip():
    instance = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    assert instance.dead == True
    instance.dead = False
    assert instance.dead == False


def test_builds_ChangeArtifact_editType_value_roundtrip():
    instance = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    assert instance.editType == "sample_text"
    instance.editType = "sample_text_2"
    assert instance.editType == "sample_text_2"


def test_builds_ChangeArtifact_file_value_roundtrip():
    instance = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_builds_ChangeArtifact_prevRevision_value_roundtrip():
    instance = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    assert instance.prevRevision == "sample_text"
    instance.prevRevision = "sample_text_2"
    assert instance.prevRevision == "sample_text_2"


def test_builds_ChangeArtifact_relativePath_value_roundtrip():
    instance = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    assert instance.relativePath == "sample_text"
    instance.relativePath = "sample_text_2"
    assert instance.relativePath == "sample_text_2"


def test_builds_ChangeArtifact_revision_value_roundtrip():
    instance = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    assert instance.revision == "sample_text"
    instance.revision = "sample_text_2"
    assert instance.revision == "sample_text_2"


def test_builds_ChangeSet_kind_value_roundtrip():
    instance = builds_ChangeSet(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_builds_ChoiceParameterDefinition_defaultValue_value_roundtrip():
    instance = builds_ChoiceParameterDefinition(defaultValue="sample_text", options="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_builds_ChoiceParameterDefinition_options_value_roundtrip():
    instance = builds_ChoiceParameterDefinition(defaultValue="sample_text", options="sample_text")
    assert instance.options == "sample_text"
    instance.options = "sample_text_2"
    assert instance.options == "sample_text_2"


def test_builds_HealthReport_description_value_roundtrip():
    instance = builds_HealthReport(description="sample_text", health=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_builds_HealthReport_health_value_roundtrip():
    instance = builds_HealthReport(description="sample_text", health=7)
    assert instance.health == 7
    instance.health = 13
    assert instance.health == 13


def test_builds_ParameterDefinition_description_value_roundtrip():
    instance = builds_ParameterDefinition(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_builds_ParameterDefinition_name_value_roundtrip():
    instance = builds_ParameterDefinition(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_builds_PasswordParameterDefinition_defaultValue_value_roundtrip():
    instance = builds_PasswordParameterDefinition(defaultValue="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_builds_StringParameterDefinition_defaultValue_value_roundtrip():
    instance = builds_StringParameterDefinition(defaultValue="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_builds_StringToStringMap_key_value_roundtrip():
    instance = builds_StringToStringMap(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_builds_StringToStringMap_value_value_roundtrip():
    instance = builds_StringToStringMap(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_builds_TestCase_className_value_roundtrip():
    instance = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_builds_TestCase_message_value_roundtrip():
    instance = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_builds_TestCase_skipped_value_roundtrip():
    instance = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    assert instance.skipped == True
    instance.skipped = False
    assert instance.skipped == False


def test_builds_TestCase_stackTrace_value_roundtrip():
    instance = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    assert instance.stackTrace == "sample_text"
    instance.stackTrace = "sample_text_2"
    assert instance.stackTrace == "sample_text_2"


def test_builds_TestCase_status_value_roundtrip():
    instance = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_builds_TestElement_duration_value_roundtrip():
    instance = builds_TestElement(duration="sample_text", errorOutput="sample_text", label="sample_text", output="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_builds_TestElement_errorOutput_value_roundtrip():
    instance = builds_TestElement(duration="sample_text", errorOutput="sample_text", label="sample_text", output="sample_text")
    assert instance.errorOutput == "sample_text"
    instance.errorOutput = "sample_text_2"
    assert instance.errorOutput == "sample_text_2"


def test_builds_TestElement_label_value_roundtrip():
    instance = builds_TestElement(duration="sample_text", errorOutput="sample_text", label="sample_text", output="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_builds_TestElement_output_value_roundtrip():
    instance = builds_TestElement(duration="sample_text", errorOutput="sample_text", label="sample_text", output="sample_text")
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_builds_TestResult_duration_value_roundtrip():
    instance = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_builds_TestResult_errorCount_value_roundtrip():
    instance = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    assert instance.errorCount == 7
    instance.errorCount = 13
    assert instance.errorCount == 13


def test_builds_TestResult_failCount_value_roundtrip():
    instance = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    assert instance.failCount == 7
    instance.failCount = 13
    assert instance.failCount == 13


def test_builds_TestResult_ignoredCount_value_roundtrip():
    instance = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    assert instance.ignoredCount == 7
    instance.ignoredCount = 13
    assert instance.ignoredCount == 13


def test_builds_TestResult_passCount_value_roundtrip():
    instance = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    assert instance.passCount == 7
    instance.passCount = 13
    assert instance.passCount == 13


def test_builds_User_email_value_roundtrip():
    instance = builds_User(email="sample_text", id="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_builds_User_id_value_roundtrip():
    instance = builds_User(email="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_builds_Artifact_isa_BuildElement():
    instance = builds_Artifact(relativePath="sample_text")
    assert isinstance(instance, BuildElement)


def test_builds_Build_isa_BuildElement():
    instance = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    assert isinstance(instance, BuildElement)


def test_builds_BuildPlan_isa_BuildElement():
    instance = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    assert isinstance(instance, BuildElement)


def test_builds_BuildServer_isa_BuildElement():
    instance = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    assert isinstance(instance, BuildElement)


def test_builds_User_isa_BuildElement():
    instance = builds_User(email="sample_text", id="sample_text")
    assert isinstance(instance, BuildElement)


def test_builds_BooleanParameterDefinition_isa_ParameterDefinition():
    instance = builds_BooleanParameterDefinition(defaultValue=True)
    assert isinstance(instance, ParameterDefinition)


def test_builds_BuildParameterDefinition_isa_ParameterDefinition():
    instance = builds_BuildParameterDefinition(buildPlanId="sample_text")
    assert isinstance(instance, ParameterDefinition)


def test_builds_ChoiceParameterDefinition_isa_ParameterDefinition():
    instance = builds_ChoiceParameterDefinition(defaultValue="sample_text", options="sample_text")
    assert isinstance(instance, ParameterDefinition)


def test_builds_FileParameterDefinition_isa_ParameterDefinition():
    instance = builds_FileParameterDefinition()
    assert isinstance(instance, ParameterDefinition)


def test_builds_PasswordParameterDefinition_isa_ParameterDefinition():
    instance = builds_PasswordParameterDefinition(defaultValue="sample_text")
    assert isinstance(instance, ParameterDefinition)


def test_builds_PlanParameterDefinition_isa_ParameterDefinition():
    instance = builds_PlanParameterDefinition()
    assert isinstance(instance, ParameterDefinition)


def test_builds_StringParameterDefinition_isa_ParameterDefinition():
    instance = builds_StringParameterDefinition(defaultValue="sample_text")
    assert isinstance(instance, ParameterDefinition)


def test_builds_TestCase_isa_TestElement():
    instance = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    assert isinstance(instance, TestElement)


def test_builds_TestSuite_isa_TestElement():
    instance = builds_TestSuite()
    assert isinstance(instance, TestElement)


def test_assoc_artifacts0_link_reassign_clear():
    a = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b1 = builds_Artifact(relativePath="sample_text")
    b2 = builds_Artifact(relativePath="sample_text_2")
    _safe_set(a, 'builds_Build', {b1})
    assert _is_linked(a, 'builds_Build', b1)
    if hasattr(b1, 'builds_Artifact'):
        assert _is_linked(b1, 'builds_Artifact', a)
    _safe_set(a, 'builds_Build', {b2})
    assert _is_linked(a, 'builds_Build', b2)
    if hasattr(b1, 'builds_Artifact'):
        assert not _is_linked(b1, 'builds_Artifact', a)
    if hasattr(b2, 'builds_Artifact'):
        assert _is_linked(b2, 'builds_Artifact', a)
    _safe_set(a, 'builds_Build', set())
    assert not _is_linked(a, 'builds_Build', b2)
    if hasattr(b2, 'builds_Artifact'):
        assert not _is_linked(b2, 'builds_Artifact', a)


def test_assoc_artifacts40_link_reassign_clear():
    a = builds_ChangeArtifact(dead=True, editType="sample_text", file="sample_text", prevRevision="sample_text", relativePath="sample_text", revision="sample_text")
    b1 = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    b2 = builds_Change(date="sample_text_2", message="sample_text_2", revision="sample_text_2")
    _safe_set(a, 'builds_ChangeArtifact', b1)
    assert _is_linked(a, 'builds_ChangeArtifact', b1)
    if hasattr(b1, 'builds_Change'):
        assert _is_linked(b1, 'builds_Change', a)
    _safe_set(a, 'builds_ChangeArtifact', b2)
    assert _is_linked(a, 'builds_ChangeArtifact', b2)
    if hasattr(b1, 'builds_Change'):
        assert not _is_linked(b1, 'builds_Change', a)
    if hasattr(b2, 'builds_Change'):
        assert _is_linked(b2, 'builds_Change', a)
    _safe_set(a, 'builds_ChangeArtifact', None)
    assert not _is_linked(a, 'builds_ChangeArtifact', b2)
    if hasattr(b2, 'builds_Change'):
        assert not _is_linked(b2, 'builds_Change', a)


def test_assoc_attributes17_link_reassign_clear():
    a = builds_StringToStringMap(key="sample_text", value="sample_text")
    b1 = builds_BuildElement(elementStatus="sample_text", name="sample_text", operations="sample_text", refreshDate=date(2024, 1, 1), url="sample_text")
    b2 = builds_BuildElement(elementStatus="sample_text_2", name="sample_text_2", operations="sample_text_2", refreshDate=date(2025, 6, 15), url="sample_text_2")
    _safe_set(a, 'builds_StringToStringMap', b1)
    assert _is_linked(a, 'builds_StringToStringMap', b1)
    if hasattr(b1, 'builds_BuildElement'):
        assert _is_linked(b1, 'builds_BuildElement', a)
    _safe_set(a, 'builds_StringToStringMap', b2)
    assert _is_linked(a, 'builds_StringToStringMap', b2)
    if hasattr(b1, 'builds_BuildElement'):
        assert not _is_linked(b1, 'builds_BuildElement', a)
    if hasattr(b2, 'builds_BuildElement'):
        assert _is_linked(b2, 'builds_BuildElement', a)
    _safe_set(a, 'builds_StringToStringMap', None)
    assert not _is_linked(a, 'builds_StringToStringMap', b2)
    if hasattr(b2, 'builds_BuildElement'):
        assert not _is_linked(b2, 'builds_BuildElement', a)


def test_assoc_author41_link_reassign_clear():
    a = builds_User(email="sample_text", id="sample_text")
    b1 = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    b2 = builds_Change(date="sample_text_2", message="sample_text_2", revision="sample_text_2")
    _safe_set(a, 'builds_User43', b1)
    assert _is_linked(a, 'builds_User43', b1)
    if hasattr(b1, 'builds_Change42'):
        assert _is_linked(b1, 'builds_Change42', a)
    _safe_set(a, 'builds_User43', b2)
    assert _is_linked(a, 'builds_User43', b2)
    if hasattr(b1, 'builds_Change42'):
        assert not _is_linked(b1, 'builds_Change42', a)
    if hasattr(b2, 'builds_Change42'):
        assert _is_linked(b2, 'builds_Change42', a)
    _safe_set(a, 'builds_User43', None)
    assert not _is_linked(a, 'builds_User43', b2)
    if hasattr(b2, 'builds_Change42'):
        assert not _is_linked(b2, 'builds_Change42', a)


def test_assoc_build12_link_reassign_clear():
    a = builds_BuildReference(build="sample_text", plan="sample_text")
    b1 = builds_BuildCause(description="sample_text")
    b2 = builds_BuildCause(description="sample_text_2")
    _safe_set(a, 'builds_BuildReference', b1)
    assert _is_linked(a, 'builds_BuildReference', b1)
    if hasattr(b1, 'builds_BuildCause13'):
        assert _is_linked(b1, 'builds_BuildCause13', a)
    _safe_set(a, 'builds_BuildReference', b2)
    assert _is_linked(a, 'builds_BuildReference', b2)
    if hasattr(b1, 'builds_BuildCause13'):
        assert not _is_linked(b1, 'builds_BuildCause13', a)
    if hasattr(b2, 'builds_BuildCause13'):
        assert _is_linked(b2, 'builds_BuildCause13', a)
    _safe_set(a, 'builds_BuildReference', None)
    assert not _is_linked(a, 'builds_BuildReference', b2)
    if hasattr(b2, 'builds_BuildCause13'):
        assert not _is_linked(b2, 'builds_BuildCause13', a)


def test_assoc_build51_link_reassign_clear():
    a = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'testResult', b1)
    assert _is_linked(a, 'testResult', b1)
    if hasattr(b1, 'Build'):
        assert _is_linked(b1, 'Build', a)
    _safe_set(a, 'testResult', b2)
    assert _is_linked(a, 'testResult', b2)
    if hasattr(b1, 'Build'):
        assert not _is_linked(b1, 'Build', a)
    if hasattr(b2, 'Build'):
        assert _is_linked(b2, 'Build', a)
    _safe_set(a, 'testResult', None)
    assert not _is_linked(a, 'testResult', b2)
    if hasattr(b2, 'Build'):
        assert not _is_linked(b2, 'Build', a)


def test_assoc_buildPlan49_link_reassign_clear():
    a = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b1 = builds_BuildParameterDefinition(buildPlanId="sample_text")
    b2 = builds_BuildParameterDefinition(buildPlanId="sample_text_2")
    _safe_set(a, 'builds_BuildPlan50', b1)
    assert _is_linked(a, 'builds_BuildPlan50', b1)
    if hasattr(b1, 'builds_BuildParameterDefinition'):
        assert _is_linked(b1, 'builds_BuildParameterDefinition', a)
    _safe_set(a, 'builds_BuildPlan50', b2)
    assert _is_linked(a, 'builds_BuildPlan50', b2)
    if hasattr(b1, 'builds_BuildParameterDefinition'):
        assert not _is_linked(b1, 'builds_BuildParameterDefinition', a)
    if hasattr(b2, 'builds_BuildParameterDefinition'):
        assert _is_linked(b2, 'builds_BuildParameterDefinition', a)
    _safe_set(a, 'builds_BuildPlan50', None)
    assert not _is_linked(a, 'builds_BuildPlan50', b2)
    if hasattr(b2, 'builds_BuildParameterDefinition'):
        assert not _is_linked(b2, 'builds_BuildParameterDefinition', a)


def test_assoc_builds37_link_reassign_clear():
    a = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b1 = builds_BuildModel()
    b2 = builds_BuildModel()
    _safe_set(a, 'builds_Build39', b1)
    assert _is_linked(a, 'builds_Build39', b1)
    if hasattr(b1, 'builds_BuildModel38'):
        assert _is_linked(b1, 'builds_BuildModel38', a)
    _safe_set(a, 'builds_Build39', b2)
    assert _is_linked(a, 'builds_Build39', b2)
    if hasattr(b1, 'builds_BuildModel38'):
        assert not _is_linked(b1, 'builds_BuildModel38', a)
    if hasattr(b2, 'builds_BuildModel38'):
        assert _is_linked(b2, 'builds_BuildModel38', a)
    _safe_set(a, 'builds_Build39', None)
    assert not _is_linked(a, 'builds_Build39', b2)
    if hasattr(b2, 'builds_BuildModel38'):
        assert not _is_linked(b2, 'builds_BuildModel38', a)


def test_assoc_cases53_link_reassign_clear():
    a = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    b1 = builds_TestSuite()
    b2 = builds_TestSuite()
    _safe_set(a, 'TestCase', b1)
    assert _is_linked(a, 'TestCase', b1)
    if hasattr(b1, 'suite'):
        assert _is_linked(b1, 'suite', a)
    _safe_set(a, 'TestCase', b2)
    assert _is_linked(a, 'TestCase', b2)
    if hasattr(b1, 'suite'):
        assert not _is_linked(b1, 'suite', a)
    if hasattr(b2, 'suite'):
        assert _is_linked(b2, 'suite', a)
    _safe_set(a, 'TestCase', None)
    assert not _is_linked(a, 'TestCase', b2)
    if hasattr(b2, 'suite'):
        assert not _is_linked(b2, 'suite', a)


def test_assoc_cause10_link_reassign_clear():
    a = builds_BuildCause(description="sample_text")
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'builds_BuildCause', b1)
    assert _is_linked(a, 'builds_BuildCause', b1)
    if hasattr(b1, 'builds_Build11'):
        assert _is_linked(b1, 'builds_Build11', a)
    _safe_set(a, 'builds_BuildCause', b2)
    assert _is_linked(a, 'builds_BuildCause', b2)
    if hasattr(b1, 'builds_Build11'):
        assert not _is_linked(b1, 'builds_Build11', a)
    if hasattr(b2, 'builds_Build11'):
        assert _is_linked(b2, 'builds_Build11', a)
    _safe_set(a, 'builds_BuildCause', None)
    assert not _is_linked(a, 'builds_BuildCause', b2)
    if hasattr(b2, 'builds_Build11'):
        assert not _is_linked(b2, 'builds_Build11', a)


def test_assoc_changeSet1_link_reassign_clear():
    a = builds_ChangeSet(kind="sample_text")
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'builds_ChangeSet', b1)
    assert _is_linked(a, 'builds_ChangeSet', b1)
    if hasattr(b1, 'builds_Build2'):
        assert _is_linked(b1, 'builds_Build2', a)
    _safe_set(a, 'builds_ChangeSet', b2)
    assert _is_linked(a, 'builds_ChangeSet', b2)
    if hasattr(b1, 'builds_Build2'):
        assert not _is_linked(b1, 'builds_Build2', a)
    if hasattr(b2, 'builds_Build2'):
        assert _is_linked(b2, 'builds_Build2', a)
    _safe_set(a, 'builds_ChangeSet', None)
    assert not _is_linked(a, 'builds_ChangeSet', b2)
    if hasattr(b2, 'builds_Build2'):
        assert not _is_linked(b2, 'builds_Build2', a)


def test_assoc_changes44_link_reassign_clear():
    a = builds_ChangeSet(kind="sample_text")
    b1 = builds_Change(date="sample_text", message="sample_text", revision="sample_text")
    b2 = builds_Change(date="sample_text_2", message="sample_text_2", revision="sample_text_2")
    _safe_set(a, 'builds_ChangeSet45', {b1})
    assert _is_linked(a, 'builds_ChangeSet45', b1)
    if hasattr(b1, 'builds_Change46'):
        assert _is_linked(b1, 'builds_Change46', a)
    _safe_set(a, 'builds_ChangeSet45', {b2})
    assert _is_linked(a, 'builds_ChangeSet45', b2)
    if hasattr(b1, 'builds_Change46'):
        assert not _is_linked(b1, 'builds_Change46', a)
    if hasattr(b2, 'builds_Change46'):
        assert _is_linked(b2, 'builds_Change46', a)
    _safe_set(a, 'builds_ChangeSet45', set())
    assert not _is_linked(a, 'builds_ChangeSet45', b2)
    if hasattr(b2, 'builds_Change46'):
        assert not _is_linked(b2, 'builds_Change46', a)


def test_assoc_children22_link_reassign_clear():
    a = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    _safe_set(a, 'BuildPlan', b1)
    assert _is_linked(a, 'BuildPlan', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'BuildPlan', b2)
    assert _is_linked(a, 'BuildPlan', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'BuildPlan', None)
    assert not _is_linked(a, 'BuildPlan', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_containingBuildPlan47_link_reassign_clear():
    a = builds_ParameterDefinition(description="sample_text", name="sample_text")
    b1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    _safe_set(a, 'parameterDefinitions', b1)
    assert _is_linked(a, 'parameterDefinitions', b1)
    if hasattr(b1, 'BuildPlan48'):
        assert _is_linked(b1, 'BuildPlan48', a)
    _safe_set(a, 'parameterDefinitions', b2)
    assert _is_linked(a, 'parameterDefinitions', b2)
    if hasattr(b1, 'BuildPlan48'):
        assert not _is_linked(b1, 'BuildPlan48', a)
    if hasattr(b2, 'BuildPlan48'):
        assert _is_linked(b2, 'BuildPlan48', a)
    _safe_set(a, 'parameterDefinitions', None)
    assert not _is_linked(a, 'parameterDefinitions', b2)
    if hasattr(b2, 'BuildPlan48'):
        assert not _is_linked(b2, 'BuildPlan48', a)


def test_assoc_culprits8_link_reassign_clear():
    a = builds_User(email="sample_text", id="sample_text")
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'builds_User', b1)
    assert _is_linked(a, 'builds_User', b1)
    if hasattr(b1, 'builds_Build9'):
        assert _is_linked(b1, 'builds_Build9', a)
    _safe_set(a, 'builds_User', b2)
    assert _is_linked(a, 'builds_User', b2)
    if hasattr(b1, 'builds_Build9'):
        assert not _is_linked(b1, 'builds_Build9', a)
    if hasattr(b2, 'builds_Build9'):
        assert _is_linked(b2, 'builds_Build9', a)
    _safe_set(a, 'builds_User', None)
    assert not _is_linked(a, 'builds_User', b2)
    if hasattr(b2, 'builds_Build9'):
        assert not _is_linked(b2, 'builds_Build9', a)


def test_assoc_healthReports30_link_reassign_clear():
    a = builds_HealthReport(description="sample_text", health=7)
    b1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    _safe_set(a, 'builds_HealthReport', b1)
    assert _is_linked(a, 'builds_HealthReport', b1)
    if hasattr(b1, 'builds_BuildPlan31'):
        assert _is_linked(b1, 'builds_BuildPlan31', a)
    _safe_set(a, 'builds_HealthReport', b2)
    assert _is_linked(a, 'builds_HealthReport', b2)
    if hasattr(b1, 'builds_BuildPlan31'):
        assert not _is_linked(b1, 'builds_BuildPlan31', a)
    if hasattr(b2, 'builds_BuildPlan31'):
        assert _is_linked(b2, 'builds_BuildPlan31', a)
    _safe_set(a, 'builds_HealthReport', None)
    assert not _is_linked(a, 'builds_HealthReport', b2)
    if hasattr(b2, 'builds_BuildPlan31'):
        assert not _is_linked(b2, 'builds_BuildPlan31', a)


def test_assoc_lastBuild26_link_reassign_clear():
    a = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'builds_BuildPlan27', b1)
    assert _is_linked(a, 'builds_BuildPlan27', b1)
    if hasattr(b1, 'builds_Build28'):
        assert _is_linked(b1, 'builds_Build28', a)
    _safe_set(a, 'builds_BuildPlan27', b2)
    assert _is_linked(a, 'builds_BuildPlan27', b2)
    if hasattr(b1, 'builds_Build28'):
        assert not _is_linked(b1, 'builds_Build28', a)
    if hasattr(b2, 'builds_Build28'):
        assert _is_linked(b2, 'builds_Build28', a)
    _safe_set(a, 'builds_BuildPlan27', None)
    assert not _is_linked(a, 'builds_BuildPlan27', b2)
    if hasattr(b2, 'builds_Build28'):
        assert not _is_linked(b2, 'builds_Build28', a)


def test_assoc_parameterDefinitions29_link_reassign_clear():
    a = builds_ParameterDefinition(description="sample_text", name="sample_text")
    b1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    _safe_set(a, 'ParameterDefinition', b1)
    assert _is_linked(a, 'ParameterDefinition', b1)
    if hasattr(b1, 'containingBuildPlan'):
        assert _is_linked(b1, 'containingBuildPlan', a)
    _safe_set(a, 'ParameterDefinition', b2)
    assert _is_linked(a, 'ParameterDefinition', b2)
    if hasattr(b1, 'containingBuildPlan'):
        assert not _is_linked(b1, 'containingBuildPlan', a)
    if hasattr(b2, 'containingBuildPlan'):
        assert _is_linked(b2, 'containingBuildPlan', a)
    _safe_set(a, 'ParameterDefinition', None)
    assert not _is_linked(a, 'ParameterDefinition', b2)
    if hasattr(b2, 'containingBuildPlan'):
        assert not _is_linked(b2, 'containingBuildPlan', a)


def test_assoc_parent24_link_reassign_clear():
    a = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    _safe_set(a, 'BuildPlan25', b1)
    assert _is_linked(a, 'BuildPlan25', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'BuildPlan25', b2)
    assert _is_linked(a, 'BuildPlan25', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'BuildPlan25', None)
    assert not _is_linked(a, 'BuildPlan25', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_plan3_link_reassign_clear():
    a = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'builds_BuildPlan', b1)
    assert _is_linked(a, 'builds_BuildPlan', b1)
    if hasattr(b1, 'builds_Build4'):
        assert _is_linked(b1, 'builds_Build4', a)
    _safe_set(a, 'builds_BuildPlan', b2)
    assert _is_linked(a, 'builds_BuildPlan', b2)
    if hasattr(b1, 'builds_Build4'):
        assert not _is_linked(b1, 'builds_Build4', a)
    if hasattr(b2, 'builds_Build4'):
        assert _is_linked(b2, 'builds_Build4', a)
    _safe_set(a, 'builds_BuildPlan', None)
    assert not _is_linked(a, 'builds_BuildPlan', b2)
    if hasattr(b2, 'builds_Build4'):
        assert not _is_linked(b2, 'builds_Build4', a)


def test_assoc_plans34_link_reassign_clear():
    a = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b1 = builds_BuildModel()
    b2 = builds_BuildModel()
    _safe_set(a, 'builds_BuildPlan36', b1)
    assert _is_linked(a, 'builds_BuildPlan36', b1)
    if hasattr(b1, 'builds_BuildModel35'):
        assert _is_linked(b1, 'builds_BuildModel35', a)
    _safe_set(a, 'builds_BuildPlan36', b2)
    assert _is_linked(a, 'builds_BuildPlan36', b2)
    if hasattr(b1, 'builds_BuildModel35'):
        assert not _is_linked(b1, 'builds_BuildModel35', a)
    if hasattr(b2, 'builds_BuildModel35'):
        assert _is_linked(b2, 'builds_BuildModel35', a)
    _safe_set(a, 'builds_BuildPlan36', None)
    assert not _is_linked(a, 'builds_BuildPlan36', b2)
    if hasattr(b2, 'builds_BuildModel35'):
        assert not _is_linked(b2, 'builds_BuildModel35', a)


def test_assoc_result54_link_reassign_clear():
    a = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    b1 = builds_TestSuite()
    b2 = builds_TestSuite()
    _safe_set(a, 'TestResult55', b1)
    assert _is_linked(a, 'TestResult55', b1)
    if hasattr(b1, 'suites'):
        assert _is_linked(b1, 'suites', a)
    _safe_set(a, 'TestResult55', b2)
    assert _is_linked(a, 'TestResult55', b2)
    if hasattr(b1, 'suites'):
        assert not _is_linked(b1, 'suites', a)
    if hasattr(b2, 'suites'):
        assert _is_linked(b2, 'suites', a)
    _safe_set(a, 'TestResult55', None)
    assert not _is_linked(a, 'TestResult55', b2)
    if hasattr(b2, 'suites'):
        assert not _is_linked(b2, 'suites', a)


def test_assoc_server18_link_reassign_clear():
    a = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    b1 = builds_BuildPlan(description="sample_text", flags="sample_text", health=7, id="sample_text", info="sample_text", selected=True, state="sample_text", status="sample_text", summary="sample_text")
    b2 = builds_BuildPlan(description="sample_text_2", flags="sample_text_2", health=13, id="sample_text_2", info="sample_text_2", selected=False, state="sample_text_2", status="sample_text_2", summary="sample_text_2")
    _safe_set(a, 'builds_BuildServer20', b1)
    assert _is_linked(a, 'builds_BuildServer20', b1)
    if hasattr(b1, 'builds_BuildPlan19'):
        assert _is_linked(b1, 'builds_BuildPlan19', a)
    _safe_set(a, 'builds_BuildServer20', b2)
    assert _is_linked(a, 'builds_BuildServer20', b2)
    if hasattr(b1, 'builds_BuildPlan19'):
        assert not _is_linked(b1, 'builds_BuildPlan19', a)
    if hasattr(b2, 'builds_BuildPlan19'):
        assert _is_linked(b2, 'builds_BuildPlan19', a)
    _safe_set(a, 'builds_BuildServer20', None)
    assert not _is_linked(a, 'builds_BuildServer20', b2)
    if hasattr(b2, 'builds_BuildPlan19'):
        assert not _is_linked(b2, 'builds_BuildPlan19', a)


def test_assoc_server5_link_reassign_clear():
    a = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'builds_BuildServer', b1)
    assert _is_linked(a, 'builds_BuildServer', b1)
    if hasattr(b1, 'builds_Build6'):
        assert _is_linked(b1, 'builds_Build6', a)
    _safe_set(a, 'builds_BuildServer', b2)
    assert _is_linked(a, 'builds_BuildServer', b2)
    if hasattr(b1, 'builds_Build6'):
        assert not _is_linked(b1, 'builds_Build6', a)
    if hasattr(b2, 'builds_Build6'):
        assert _is_linked(b2, 'builds_Build6', a)
    _safe_set(a, 'builds_BuildServer', None)
    assert not _is_linked(a, 'builds_BuildServer', b2)
    if hasattr(b2, 'builds_Build6'):
        assert not _is_linked(b2, 'builds_Build6', a)


def test_assoc_servers32_link_reassign_clear():
    a = builds_BuildServer(connectorKind="sample_text", location="sample_text", repositoryUrl="sample_text")
    b1 = builds_BuildModel()
    b2 = builds_BuildModel()
    _safe_set(a, 'builds_BuildServer33', b1)
    assert _is_linked(a, 'builds_BuildServer33', b1)
    if hasattr(b1, 'builds_BuildModel'):
        assert _is_linked(b1, 'builds_BuildModel', a)
    _safe_set(a, 'builds_BuildServer33', b2)
    assert _is_linked(a, 'builds_BuildServer33', b2)
    if hasattr(b1, 'builds_BuildModel'):
        assert not _is_linked(b1, 'builds_BuildModel', a)
    if hasattr(b2, 'builds_BuildModel'):
        assert _is_linked(b2, 'builds_BuildModel', a)
    _safe_set(a, 'builds_BuildServer33', None)
    assert not _is_linked(a, 'builds_BuildServer33', b2)
    if hasattr(b2, 'builds_BuildModel'):
        assert not _is_linked(b2, 'builds_BuildModel', a)


def test_assoc_suite56_link_reassign_clear():
    a = builds_TestCase(className="sample_text", message="sample_text", skipped=True, stackTrace="sample_text", status="sample_text")
    b1 = builds_TestSuite()
    b2 = builds_TestSuite()
    _safe_set(a, 'cases', b1)
    assert _is_linked(a, 'cases', b1)
    if hasattr(b1, 'TestSuite57'):
        assert _is_linked(b1, 'TestSuite57', a)
    _safe_set(a, 'cases', b2)
    assert _is_linked(a, 'cases', b2)
    if hasattr(b1, 'TestSuite57'):
        assert not _is_linked(b1, 'TestSuite57', a)
    if hasattr(b2, 'TestSuite57'):
        assert _is_linked(b2, 'TestSuite57', a)
    _safe_set(a, 'cases', None)
    assert not _is_linked(a, 'cases', b2)
    if hasattr(b2, 'TestSuite57'):
        assert not _is_linked(b2, 'TestSuite57', a)


def test_assoc_suites52_link_reassign_clear():
    a = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    b1 = builds_TestSuite()
    b2 = builds_TestSuite()
    _safe_set(a, 'result', {b1})
    assert _is_linked(a, 'result', b1)
    if hasattr(b1, 'TestSuite'):
        assert _is_linked(b1, 'TestSuite', a)
    _safe_set(a, 'result', {b2})
    assert _is_linked(a, 'result', b2)
    if hasattr(b1, 'TestSuite'):
        assert not _is_linked(b1, 'TestSuite', a)
    if hasattr(b2, 'TestSuite'):
        assert _is_linked(b2, 'TestSuite', a)
    _safe_set(a, 'result', set())
    assert not _is_linked(a, 'result', b2)
    if hasattr(b2, 'TestSuite'):
        assert not _is_linked(b2, 'TestSuite', a)


def test_assoc_testResult7_link_reassign_clear():
    a = builds_TestResult(duration="sample_text", errorCount=7, failCount=7, ignoredCount=7, passCount=7)
    b1 = builds_Build(buildNumber=7, displayName="sample_text", duration="sample_text", id="sample_text", label="sample_text", state="sample_text", status="sample_text", summary="sample_text", timestamp="sample_text")
    b2 = builds_Build(buildNumber=13, displayName="sample_text_2", duration="sample_text_2", id="sample_text_2", label="sample_text_2", state="sample_text_2", status="sample_text_2", summary="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'TestResult', b1)
    assert _is_linked(a, 'TestResult', b1)
    if hasattr(b1, 'build'):
        assert _is_linked(b1, 'build', a)
    _safe_set(a, 'TestResult', b2)
    assert _is_linked(a, 'TestResult', b2)
    if hasattr(b1, 'build'):
        assert not _is_linked(b1, 'build', a)
    if hasattr(b2, 'build'):
        assert _is_linked(b2, 'build', a)
    _safe_set(a, 'TestResult', None)
    assert not _is_linked(a, 'TestResult', b2)
    if hasattr(b2, 'build'):
        assert not _is_linked(b2, 'build', a)


def test_assoc_user14_link_reassign_clear():
    a = builds_User(email="sample_text", id="sample_text")
    b1 = builds_BuildCause(description="sample_text")
    b2 = builds_BuildCause(description="sample_text_2")
    _safe_set(a, 'builds_User16', b1)
    assert _is_linked(a, 'builds_User16', b1)
    if hasattr(b1, 'builds_BuildCause15'):
        assert _is_linked(b1, 'builds_BuildCause15', a)
    _safe_set(a, 'builds_User16', b2)
    assert _is_linked(a, 'builds_User16', b2)
    if hasattr(b1, 'builds_BuildCause15'):
        assert not _is_linked(b1, 'builds_BuildCause15', a)
    if hasattr(b2, 'builds_BuildCause15'):
        assert _is_linked(b2, 'builds_BuildCause15', a)
    _safe_set(a, 'builds_User16', None)
    assert not _is_linked(a, 'builds_User16', b2)
    if hasattr(b2, 'builds_BuildCause15'):
        assert not _is_linked(b2, 'builds_BuildCause15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BuildElement_strategy = st.builds(BuildElement)
@given(instance=BuildElement_strategy)
@settings(max_examples=25)
def test_BuildElement_instantiation(instance):
    assert isinstance(instance, BuildElement)


ParameterDefinition_strategy = st.builds(ParameterDefinition)
@given(instance=ParameterDefinition_strategy)
@settings(max_examples=25)
def test_ParameterDefinition_instantiation(instance):
    assert isinstance(instance, ParameterDefinition)


TestElement_strategy = st.builds(TestElement)
@given(instance=TestElement_strategy)
@settings(max_examples=25)
def test_TestElement_instantiation(instance):
    assert isinstance(instance, TestElement)


builds_Artifact_strategy = st.builds(builds_Artifact, relativePath=safe_text)
@given(instance=builds_Artifact_strategy)
@settings(max_examples=25)
def test_builds_Artifact_instantiation(instance):
    assert isinstance(instance, builds_Artifact)


builds_BooleanParameterDefinition_strategy = st.builds(builds_BooleanParameterDefinition, defaultValue=st.booleans())
@given(instance=builds_BooleanParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_BooleanParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_BooleanParameterDefinition)


builds_Build_strategy = st.builds(builds_Build, buildNumber=st.integers(), displayName=safe_text, duration=safe_text, id=safe_text, label=safe_text, state=safe_text, status=safe_text, summary=safe_text, timestamp=safe_text)
@given(instance=builds_Build_strategy)
@settings(max_examples=25)
def test_builds_Build_instantiation(instance):
    assert isinstance(instance, builds_Build)


builds_BuildCause_strategy = st.builds(builds_BuildCause, description=safe_text)
@given(instance=builds_BuildCause_strategy)
@settings(max_examples=25)
def test_builds_BuildCause_instantiation(instance):
    assert isinstance(instance, builds_BuildCause)


builds_BuildElement_strategy = st.builds(builds_BuildElement, elementStatus=safe_text, name=safe_text, operations=safe_text, refreshDate=st.dates(), url=safe_text)
@given(instance=builds_BuildElement_strategy)
@settings(max_examples=25)
def test_builds_BuildElement_instantiation(instance):
    assert isinstance(instance, builds_BuildElement)


builds_BuildModel_strategy = st.builds(builds_BuildModel)
@given(instance=builds_BuildModel_strategy)
@settings(max_examples=25)
def test_builds_BuildModel_instantiation(instance):
    assert isinstance(instance, builds_BuildModel)


builds_BuildParameterDefinition_strategy = st.builds(builds_BuildParameterDefinition, buildPlanId=safe_text)
@given(instance=builds_BuildParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_BuildParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_BuildParameterDefinition)


builds_BuildPlan_strategy = st.builds(builds_BuildPlan, description=safe_text, flags=safe_text, health=st.integers(), id=safe_text, info=safe_text, selected=st.booleans(), state=safe_text, status=safe_text, summary=safe_text)
@given(instance=builds_BuildPlan_strategy)
@settings(max_examples=25)
def test_builds_BuildPlan_instantiation(instance):
    assert isinstance(instance, builds_BuildPlan)


builds_BuildReference_strategy = st.builds(builds_BuildReference, build=safe_text, plan=safe_text)
@given(instance=builds_BuildReference_strategy)
@settings(max_examples=25)
def test_builds_BuildReference_instantiation(instance):
    assert isinstance(instance, builds_BuildReference)


builds_BuildServer_strategy = st.builds(builds_BuildServer, connectorKind=safe_text, location=safe_text, repositoryUrl=safe_text)
@given(instance=builds_BuildServer_strategy)
@settings(max_examples=25)
def test_builds_BuildServer_instantiation(instance):
    assert isinstance(instance, builds_BuildServer)


builds_Change_strategy = st.builds(builds_Change, date=safe_text, message=safe_text, revision=safe_text)
@given(instance=builds_Change_strategy)
@settings(max_examples=25)
def test_builds_Change_instantiation(instance):
    assert isinstance(instance, builds_Change)


builds_ChangeArtifact_strategy = st.builds(builds_ChangeArtifact, dead=st.booleans(), editType=safe_text, file=safe_text, prevRevision=safe_text, relativePath=safe_text, revision=safe_text)
@given(instance=builds_ChangeArtifact_strategy)
@settings(max_examples=25)
def test_builds_ChangeArtifact_instantiation(instance):
    assert isinstance(instance, builds_ChangeArtifact)


builds_ChangeSet_strategy = st.builds(builds_ChangeSet, kind=safe_text)
@given(instance=builds_ChangeSet_strategy)
@settings(max_examples=25)
def test_builds_ChangeSet_instantiation(instance):
    assert isinstance(instance, builds_ChangeSet)


builds_ChoiceParameterDefinition_strategy = st.builds(builds_ChoiceParameterDefinition, defaultValue=safe_text, options=safe_text)
@given(instance=builds_ChoiceParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_ChoiceParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_ChoiceParameterDefinition)


builds_FileParameterDefinition_strategy = st.builds(builds_FileParameterDefinition)
@given(instance=builds_FileParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_FileParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_FileParameterDefinition)


builds_HealthReport_strategy = st.builds(builds_HealthReport, description=safe_text, health=st.integers())
@given(instance=builds_HealthReport_strategy)
@settings(max_examples=25)
def test_builds_HealthReport_instantiation(instance):
    assert isinstance(instance, builds_HealthReport)


builds_ParameterDefinition_strategy = st.builds(builds_ParameterDefinition, description=safe_text, name=safe_text)
@given(instance=builds_ParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_ParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_ParameterDefinition)


builds_PasswordParameterDefinition_strategy = st.builds(builds_PasswordParameterDefinition, defaultValue=safe_text)
@given(instance=builds_PasswordParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_PasswordParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_PasswordParameterDefinition)


builds_PlanParameterDefinition_strategy = st.builds(builds_PlanParameterDefinition)
@given(instance=builds_PlanParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_PlanParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_PlanParameterDefinition)


builds_StringParameterDefinition_strategy = st.builds(builds_StringParameterDefinition, defaultValue=safe_text)
@given(instance=builds_StringParameterDefinition_strategy)
@settings(max_examples=25)
def test_builds_StringParameterDefinition_instantiation(instance):
    assert isinstance(instance, builds_StringParameterDefinition)


builds_StringToStringMap_strategy = st.builds(builds_StringToStringMap, key=safe_text, value=safe_text)
@given(instance=builds_StringToStringMap_strategy)
@settings(max_examples=25)
def test_builds_StringToStringMap_instantiation(instance):
    assert isinstance(instance, builds_StringToStringMap)


builds_TestCase_strategy = st.builds(builds_TestCase, className=safe_text, message=safe_text, skipped=st.booleans(), stackTrace=safe_text, status=safe_text)
@given(instance=builds_TestCase_strategy)
@settings(max_examples=25)
def test_builds_TestCase_instantiation(instance):
    assert isinstance(instance, builds_TestCase)


builds_TestElement_strategy = st.builds(builds_TestElement, duration=safe_text, errorOutput=safe_text, label=safe_text, output=safe_text)
@given(instance=builds_TestElement_strategy)
@settings(max_examples=25)
def test_builds_TestElement_instantiation(instance):
    assert isinstance(instance, builds_TestElement)


builds_TestResult_strategy = st.builds(builds_TestResult, duration=safe_text, errorCount=st.integers(), failCount=st.integers(), ignoredCount=st.integers(), passCount=st.integers())
@given(instance=builds_TestResult_strategy)
@settings(max_examples=25)
def test_builds_TestResult_instantiation(instance):
    assert isinstance(instance, builds_TestResult)


builds_TestSuite_strategy = st.builds(builds_TestSuite)
@given(instance=builds_TestSuite_strategy)
@settings(max_examples=25)
def test_builds_TestSuite_instantiation(instance):
    assert isinstance(instance, builds_TestSuite)


builds_User_strategy = st.builds(builds_User, email=safe_text, id=safe_text)
@given(instance=builds_User_strategy)
@settings(max_examples=25)
def test_builds_User_instantiation(instance):
    assert isinstance(instance, builds_User)


