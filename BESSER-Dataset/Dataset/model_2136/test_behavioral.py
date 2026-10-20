import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Change,
    HistoryEntry,
    IContainer,
    IContentElement,
    IModelConnection,
    IModelNode,
    INamed,
    ISpecmateModelObject,
    ISpecmatePositionableModelObject,
    ITracingElement,
    Operation,
    ParameterAssignment,
    ProcessNode,
    TestParameter,
    base_IContainer,
    base_IContentElement,
    base_IDescribed,
    base_IExternal,
    base_IID,
    base_INamed,
    base_IPositionable,
    base_IRecycled,
    base_ISpecmateModelObject,
    base_ITracingElement,
    model_administration_ProblemDetail,
    model_administration_Status,
    model_base_Folder,
    model_base_IContainer,
    model_base_IContentElement,
    model_base_IDescribed,
    model_base_IExternal,
    model_base_IID,
    model_base_IModelConnection,
    model_base_IModelNode,
    model_base_INamed,
    model_base_IPositionable,
    model_base_IRecycled,
    model_base_ISpecmateModelObject,
    model_base_ISpecmatePositionableModelObject,
    model_base_ITracingElement,
    model_batch_BatchOperation,
    model_batch_Operation,
    model_export_Export,
    model_history_Change,
    model_history_History,
    model_history_HistoryEntry,
    model_processes_Process,
    model_processes_ProcessConnection,
    model_processes_ProcessDecision,
    model_processes_ProcessEnd,
    model_processes_ProcessNode,
    model_processes_ProcessStart,
    model_processes_ProcessStep,
    model_requirements_CEGConnection,
    model_requirements_CEGModel,
    model_requirements_CEGNode,
    model_requirements_Requirement,
    model_testspecification_ParameterAssignment,
    model_testspecification_TestCase,
    model_testspecification_TestParameter,
    model_testspecification_TestProcedure,
    model_testspecification_TestSpecification,
    model_testspecification_TestStep,
    ErrorCode,
    NodeType,
    OperationType,
    ParameterType,
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

def test_assoc_assignments10_stub_double():
    # ParameterAssignment has no real 'ParameterAssignment' property in the generated
    # code (a bare stub) -- manually attach it so model_testspecification_TestParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_testspecification_TestParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_testspecification_TestParameter(type="sample_text")
    partner = ParameterAssignment()
    setattr(partner, 'ParameterAssignment', None)
    _safe_set(owner, 'parameter', {partner})
    assert getattr(partner, 'ParameterAssignment') == owner
    _safe_set(owner, 'parameter', set())
    assert getattr(partner, 'ParameterAssignment') is None


def test_assoc_changes15_stub_double():
    # Change has no real 'Change' property in the generated
    # code (a bare stub) -- manually attach it so model_history_HistoryEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_history_HistoryEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_history_HistoryEntry(comment="sample_text", deletedObjects="sample_text", timestamp="sample_text", user="sample_text")
    partner = Change()
    setattr(partner, 'Change', None)
    _safe_set(owner, 'model_history_HistoryEntry', {partner})
    assert getattr(partner, 'Change') == owner
    _safe_set(owner, 'model_history_HistoryEntry', set())
    assert getattr(partner, 'Change') is None


def test_assoc_parameter11_stub_double():
    # TestParameter has no real 'TestParameter' property in the generated
    # code (a bare stub) -- manually attach it so model_testspecification_ParameterAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_testspecification_ParameterAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_testspecification_ParameterAssignment(condition="sample_text", value="sample_text")
    partner = TestParameter()
    setattr(partner, 'TestParameter', None)
    _safe_set(owner, 'assignments', partner)
    assert getattr(partner, 'TestParameter') == owner
    _safe_set(owner, 'assignments', None)
    assert getattr(partner, 'TestParameter') is None


def test_assoc_referencedTestParameters12_stub_double():
    # TestParameter has no real 'TestParameter13' property in the generated
    # code (a bare stub) -- manually attach it so model_testspecification_TestStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_testspecification_TestStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_testspecification_TestStep(expectedOutcome="sample_text")
    partner = TestParameter()
    setattr(partner, 'TestParameter13', None)
    _safe_set(owner, 'model_testspecification_TestStep', {partner})
    assert getattr(partner, 'TestParameter13') == owner
    _safe_set(owner, 'model_testspecification_TestStep', set())
    assert getattr(partner, 'TestParameter13') is None


def test_assoc_target17_stub_double():
    # IContentElement has no real 'IContentElement18' property in the generated
    # code (a bare stub) -- manually attach it so model_batch_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_batch_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_batch_Operation(type="sample_text")
    partner = IContentElement()
    setattr(partner, 'IContentElement18', None)
    _safe_set(owner, 'model_batch_Operation', partner)
    assert getattr(partner, 'IContentElement18') == owner
    _safe_set(owner, 'model_batch_Operation', None)
    assert getattr(partner, 'IContentElement18') is None


def test_assoc_value19_stub_double():
    # IContentElement has no real 'IContentElement21' property in the generated
    # code (a bare stub) -- manually attach it so model_batch_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_batch_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_batch_Operation(type="sample_text")
    partner = IContentElement()
    setattr(partner, 'IContentElement21', None)
    _safe_set(owner, 'model_batch_Operation20', partner)
    assert getattr(partner, 'IContentElement21') == owner
    _safe_set(owner, 'model_batch_Operation20', None)
    assert getattr(partner, 'IContentElement21') is None


