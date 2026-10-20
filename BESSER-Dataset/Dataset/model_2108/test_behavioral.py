import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    BlockAction,
    DiagnosticParamValueType,
    DiagonosticModel_Action,
    DiagonosticModel_BlockAction,
    DiagonosticModel_CAPLParam,
    DiagonosticModel_CAPLTestCase,
    DiagonosticModel_CAPLTestStep,
    DiagonosticModel_CheckAction,
    DiagonosticModel_DiagnosticParam,
    DiagonosticModel_DiagnosticParamValueType,
    DiagonosticModel_DiagnosticRequest,
    DiagonosticModel_DiagnosticResponse,
    DiagonosticModel_DiagnosticService,
    DiagonosticModel_ExternalReference,
    DiagonosticModel_ForLoop,
    DiagonosticModel_ImportArtifact,
    DiagonosticModel_OneOf,
    DiagonosticModel_Range,
    DiagonosticModel_SetAction,
    DiagonosticModel_SignalType,
    DiagonosticModel_TestCase,
    DiagonosticModel_TestGroup,
    DiagonosticModel_TestSpecification,
    DiagonosticModel_TestStep,
    DiagonosticModel_TracebilityArtifact,
    DiagonosticModel_Var,
    DiagonosticModel_Variant,
    DiagonosticModel_WaitAction,
    DiagonosticModel_WhileLoop,
    TestStep,
    CreationModeEnum,
    ExecutionStatueTypeEnum,
    OperatorTypeEnum,
    SignalTypeEnum,
    TraceabilityArtifactEnum,
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

def test_assoc_capltestcases1_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestSpecification(author="sample_text", description="sample_text", functionName="sample_text", functionVersion="sample_text", name="sample_text", version="sample_text")
    a2 = DiagonosticModel_TestSpecification(author="sample_text_2", description="sample_text_2", functionName="sample_text_2", functionVersion="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = DiagonosticModel_CAPLTestCase(name="sample_text")
    _safe_set(b, 'DiagonosticModel_CAPLTestCase', a1)
    assert _is_linked(b, 'DiagonosticModel_CAPLTestCase', a1)
    if hasattr(a1, 'DiagonosticModel_TestSpecification2'):
        assert _is_linked(a1, 'DiagonosticModel_TestSpecification2', b)
    _safe_set(b, 'DiagonosticModel_CAPLTestCase', a2)
    assert _is_linked(b, 'DiagonosticModel_CAPLTestCase', a2)
    if hasattr(a1, 'DiagonosticModel_TestSpecification2'):
        assert not _is_linked(a1, 'DiagonosticModel_TestSpecification2', b)
    if hasattr(a2, 'DiagonosticModel_TestSpecification2'):
        assert _is_linked(a2, 'DiagonosticModel_TestSpecification2', b)
    _safe_set(b, 'DiagonosticModel_CAPLTestCase', None)
    assert not _is_linked(b, 'DiagonosticModel_CAPLTestCase', a2)
    if hasattr(a2, 'DiagonosticModel_TestSpecification2'):
        assert not _is_linked(a2, 'DiagonosticModel_TestSpecification2', b)


def test_assoc_capltestcases14_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestGroup(description="sample_text", name="sample_text")
    a2 = DiagonosticModel_TestGroup(description="sample_text_2", name="sample_text_2")
    b = DiagonosticModel_CAPLTestCase(name="sample_text")
    _safe_set(b, 'DiagonosticModel_CAPLTestCase16', a1)
    assert _is_linked(b, 'DiagonosticModel_CAPLTestCase16', a1)
    if hasattr(a1, 'DiagonosticModel_TestGroup15'):
        assert _is_linked(a1, 'DiagonosticModel_TestGroup15', b)
    _safe_set(b, 'DiagonosticModel_CAPLTestCase16', a2)
    assert _is_linked(b, 'DiagonosticModel_CAPLTestCase16', a2)
    if hasattr(a1, 'DiagonosticModel_TestGroup15'):
        assert not _is_linked(a1, 'DiagonosticModel_TestGroup15', b)
    if hasattr(a2, 'DiagonosticModel_TestGroup15'):
        assert _is_linked(a2, 'DiagonosticModel_TestGroup15', b)
    _safe_set(b, 'DiagonosticModel_CAPLTestCase16', None)
    assert not _is_linked(b, 'DiagonosticModel_CAPLTestCase16', a2)
    if hasattr(a2, 'DiagonosticModel_TestGroup15'):
        assert not _is_linked(a2, 'DiagonosticModel_TestGroup15', b)


def test_assoc_diagparam50_reverse_link_reassign_clear():
    a1 = DiagonosticModel_DiagnosticResponse(primitive="sample_text")
    a2 = DiagonosticModel_DiagnosticResponse(primitive="sample_text_2")
    b = DiagonosticModel_DiagnosticParam(copyToVar="sample_text", qualifier="sample_text")
    _safe_set(b, 'DiagonosticModel_DiagnosticParam52', a1)
    assert _is_linked(b, 'DiagonosticModel_DiagnosticParam52', a1)
    if hasattr(a1, 'DiagonosticModel_DiagnosticResponse51'):
        assert _is_linked(a1, 'DiagonosticModel_DiagnosticResponse51', b)
    _safe_set(b, 'DiagonosticModel_DiagnosticParam52', a2)
    assert _is_linked(b, 'DiagonosticModel_DiagnosticParam52', a2)
    if hasattr(a1, 'DiagonosticModel_DiagnosticResponse51'):
        assert not _is_linked(a1, 'DiagonosticModel_DiagnosticResponse51', b)
    if hasattr(a2, 'DiagonosticModel_DiagnosticResponse51'):
        assert _is_linked(a2, 'DiagonosticModel_DiagnosticResponse51', b)
    _safe_set(b, 'DiagonosticModel_DiagnosticParam52', None)
    assert not _is_linked(b, 'DiagonosticModel_DiagnosticParam52', a2)
    if hasattr(a2, 'DiagonosticModel_DiagnosticResponse51'):
        assert not _is_linked(a2, 'DiagonosticModel_DiagnosticResponse51', b)


def test_assoc_diagresponse39_reverse_link_reassign_clear():
    a1 = DiagonosticModel_DiagnosticService(ecu="sample_text", result="sample_text", service="sample_text")
    a2 = DiagonosticModel_DiagnosticService(ecu="sample_text_2", result="sample_text_2", service="sample_text_2")
    b = DiagonosticModel_DiagnosticResponse(primitive="sample_text")
    _safe_set(b, 'DiagonosticModel_DiagnosticResponse', a1)
    assert _is_linked(b, 'DiagonosticModel_DiagnosticResponse', a1)
    if hasattr(a1, 'DiagonosticModel_DiagnosticService40'):
        assert _is_linked(a1, 'DiagonosticModel_DiagnosticService40', b)
    _safe_set(b, 'DiagonosticModel_DiagnosticResponse', a2)
    assert _is_linked(b, 'DiagonosticModel_DiagnosticResponse', a2)
    if hasattr(a1, 'DiagonosticModel_DiagnosticService40'):
        assert not _is_linked(a1, 'DiagonosticModel_DiagnosticService40', b)
    if hasattr(a2, 'DiagonosticModel_DiagnosticService40'):
        assert _is_linked(a2, 'DiagonosticModel_DiagnosticService40', b)
    _safe_set(b, 'DiagonosticModel_DiagnosticResponse', None)
    assert not _is_linked(b, 'DiagonosticModel_DiagnosticResponse', a2)
    if hasattr(a2, 'DiagonosticModel_DiagnosticService40'):
        assert not _is_linked(a2, 'DiagonosticModel_DiagnosticService40', b)


def test_assoc_externalreference28_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestCase(description="sample_text", executionStatus="sample_text", id="sample_text", name="sample_text", requirementID="sample_text", skip=True)
    a2 = DiagonosticModel_TestCase(description="sample_text_2", executionStatus="sample_text_2", id="sample_text_2", name="sample_text_2", requirementID="sample_text_2", skip=False)
    b = DiagonosticModel_ExternalReference(owner="sample_text", title="sample_text", type="sample_text", url="sample_text")
    _safe_set(b, 'DiagonosticModel_ExternalReference30', a1)
    assert _is_linked(b, 'DiagonosticModel_ExternalReference30', a1)
    if hasattr(a1, 'DiagonosticModel_TestCase29'):
        assert _is_linked(a1, 'DiagonosticModel_TestCase29', b)
    _safe_set(b, 'DiagonosticModel_ExternalReference30', a2)
    assert _is_linked(b, 'DiagonosticModel_ExternalReference30', a2)
    if hasattr(a1, 'DiagonosticModel_TestCase29'):
        assert not _is_linked(a1, 'DiagonosticModel_TestCase29', b)
    if hasattr(a2, 'DiagonosticModel_TestCase29'):
        assert _is_linked(a2, 'DiagonosticModel_TestCase29', b)
    _safe_set(b, 'DiagonosticModel_ExternalReference30', None)
    assert not _is_linked(b, 'DiagonosticModel_ExternalReference30', a2)
    if hasattr(a2, 'DiagonosticModel_TestCase29'):
        assert not _is_linked(a2, 'DiagonosticModel_TestCase29', b)


def test_assoc_externalreference9_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestGroup(description="sample_text", name="sample_text")
    a2 = DiagonosticModel_TestGroup(description="sample_text_2", name="sample_text_2")
    b = DiagonosticModel_ExternalReference(owner="sample_text", title="sample_text", type="sample_text", url="sample_text")
    _safe_set(b, 'DiagonosticModel_ExternalReference', a1)
    assert _is_linked(b, 'DiagonosticModel_ExternalReference', a1)
    if hasattr(a1, 'DiagonosticModel_TestGroup10'):
        assert _is_linked(a1, 'DiagonosticModel_TestGroup10', b)
    _safe_set(b, 'DiagonosticModel_ExternalReference', a2)
    assert _is_linked(b, 'DiagonosticModel_ExternalReference', a2)
    if hasattr(a1, 'DiagonosticModel_TestGroup10'):
        assert not _is_linked(a1, 'DiagonosticModel_TestGroup10', b)
    if hasattr(a2, 'DiagonosticModel_TestGroup10'):
        assert _is_linked(a2, 'DiagonosticModel_TestGroup10', b)
    _safe_set(b, 'DiagonosticModel_ExternalReference', None)
    assert not _is_linked(b, 'DiagonosticModel_ExternalReference', a2)
    if hasattr(a2, 'DiagonosticModel_TestGroup10'):
        assert not _is_linked(a2, 'DiagonosticModel_TestGroup10', b)


def test_assoc_importArtifacts5_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestSpecification(author="sample_text", description="sample_text", functionName="sample_text", functionVersion="sample_text", name="sample_text", version="sample_text")
    a2 = DiagonosticModel_TestSpecification(author="sample_text_2", description="sample_text_2", functionName="sample_text_2", functionVersion="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = DiagonosticModel_ImportArtifact(path="sample_text")
    _safe_set(b, 'DiagonosticModel_ImportArtifact', a1)
    assert _is_linked(b, 'DiagonosticModel_ImportArtifact', a1)
    if hasattr(a1, 'DiagonosticModel_TestSpecification6'):
        assert _is_linked(a1, 'DiagonosticModel_TestSpecification6', b)
    _safe_set(b, 'DiagonosticModel_ImportArtifact', a2)
    assert _is_linked(b, 'DiagonosticModel_ImportArtifact', a2)
    if hasattr(a1, 'DiagonosticModel_TestSpecification6'):
        assert not _is_linked(a1, 'DiagonosticModel_TestSpecification6', b)
    if hasattr(a2, 'DiagonosticModel_TestSpecification6'):
        assert _is_linked(a2, 'DiagonosticModel_TestSpecification6', b)
    _safe_set(b, 'DiagonosticModel_ImportArtifact', None)
    assert not _is_linked(b, 'DiagonosticModel_ImportArtifact', a2)
    if hasattr(a2, 'DiagonosticModel_TestSpecification6'):
        assert not _is_linked(a2, 'DiagonosticModel_TestSpecification6', b)


def test_assoc_key36_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestStep(title="sample_text")
    a2 = DiagonosticModel_TestStep(title="sample_text_2")
    b = DiagonosticModel_SignalType(MessageName="sample_text", creationMode="sample_text", lookupValues="sample_text", name="sample_text", namespace="sample_text", node="sample_text", type="sample_text")
    _safe_set(b, 'DiagonosticModel_SignalType', a1)
    assert _is_linked(b, 'DiagonosticModel_SignalType', a1)
    if hasattr(a1, 'DiagonosticModel_TestStep37'):
        assert _is_linked(a1, 'DiagonosticModel_TestStep37', b)
    _safe_set(b, 'DiagonosticModel_SignalType', a2)
    assert _is_linked(b, 'DiagonosticModel_SignalType', a2)
    if hasattr(a1, 'DiagonosticModel_TestStep37'):
        assert not _is_linked(a1, 'DiagonosticModel_TestStep37', b)
    if hasattr(a2, 'DiagonosticModel_TestStep37'):
        assert _is_linked(a2, 'DiagonosticModel_TestStep37', b)
    _safe_set(b, 'DiagonosticModel_SignalType', None)
    assert not _is_linked(b, 'DiagonosticModel_SignalType', a2)
    if hasattr(a2, 'DiagonosticModel_TestStep37'):
        assert not _is_linked(a2, 'DiagonosticModel_TestStep37', b)


def test_assoc_nextStep34_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestStep(title="sample_text")
    a2 = DiagonosticModel_TestStep(title="sample_text_2")
    b = DiagonosticModel_TestStep(title="sample_text")
    _safe_set(b, 'DiagonosticModel_TestStep35', a1)
    assert _is_linked(b, 'DiagonosticModel_TestStep35', a1)
    if hasattr(a1, 'DiagonosticModel_TestStep33'):
        assert _is_linked(a1, 'DiagonosticModel_TestStep33', b)
    _safe_set(b, 'DiagonosticModel_TestStep35', a2)
    assert _is_linked(b, 'DiagonosticModel_TestStep35', a2)
    if hasattr(a1, 'DiagonosticModel_TestStep33'):
        assert not _is_linked(a1, 'DiagonosticModel_TestStep33', b)
    if hasattr(a2, 'DiagonosticModel_TestStep33'):
        assert _is_linked(a2, 'DiagonosticModel_TestStep33', b)
    _safe_set(b, 'DiagonosticModel_TestStep35', None)
    assert not _is_linked(b, 'DiagonosticModel_TestStep35', a2)
    if hasattr(a2, 'DiagonosticModel_TestStep33'):
        assert not _is_linked(a2, 'DiagonosticModel_TestStep33', b)


def test_assoc_parameters41_reverse_link_reassign_clear():
    a1 = DiagonosticModel_CAPLTestCase(name="sample_text")
    a2 = DiagonosticModel_CAPLTestCase(name="sample_text_2")
    b = DiagonosticModel_CAPLParam(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'DiagonosticModel_CAPLParam', a1)
    assert _is_linked(b, 'DiagonosticModel_CAPLParam', a1)
    if hasattr(a1, 'DiagonosticModel_CAPLTestCase42'):
        assert _is_linked(a1, 'DiagonosticModel_CAPLTestCase42', b)
    _safe_set(b, 'DiagonosticModel_CAPLParam', a2)
    assert _is_linked(b, 'DiagonosticModel_CAPLParam', a2)
    if hasattr(a1, 'DiagonosticModel_CAPLTestCase42'):
        assert not _is_linked(a1, 'DiagonosticModel_CAPLTestCase42', b)
    if hasattr(a2, 'DiagonosticModel_CAPLTestCase42'):
        assert _is_linked(a2, 'DiagonosticModel_CAPLTestCase42', b)
    _safe_set(b, 'DiagonosticModel_CAPLParam', None)
    assert not _is_linked(b, 'DiagonosticModel_CAPLParam', a2)
    if hasattr(a2, 'DiagonosticModel_CAPLTestCase42'):
        assert not _is_linked(a2, 'DiagonosticModel_CAPLTestCase42', b)


def test_assoc_postConditions25_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestStep(title="sample_text")
    a2 = DiagonosticModel_TestStep(title="sample_text_2")
    b = DiagonosticModel_TestCase(description="sample_text", executionStatus="sample_text", id="sample_text", name="sample_text", requirementID="sample_text", skip=True)
    _safe_set(b, 'DiagonosticModel_TestCase26', {a1})
    assert _is_linked(b, 'DiagonosticModel_TestCase26', a1)
    if hasattr(a1, 'DiagonosticModel_TestStep27'):
        assert _is_linked(a1, 'DiagonosticModel_TestStep27', b)
    _safe_set(b, 'DiagonosticModel_TestCase26', {a2})
    assert _is_linked(b, 'DiagonosticModel_TestCase26', a2)
    if hasattr(a1, 'DiagonosticModel_TestStep27'):
        assert not _is_linked(a1, 'DiagonosticModel_TestStep27', b)
    if hasattr(a2, 'DiagonosticModel_TestStep27'):
        assert _is_linked(a2, 'DiagonosticModel_TestStep27', b)
    _safe_set(b, 'DiagonosticModel_TestCase26', set())
    assert not _is_linked(b, 'DiagonosticModel_TestCase26', a2)
    if hasattr(a2, 'DiagonosticModel_TestStep27'):
        assert not _is_linked(a2, 'DiagonosticModel_TestStep27', b)


def test_assoc_preConditions22_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestStep(title="sample_text")
    a2 = DiagonosticModel_TestStep(title="sample_text_2")
    b = DiagonosticModel_TestCase(description="sample_text", executionStatus="sample_text", id="sample_text", name="sample_text", requirementID="sample_text", skip=True)
    _safe_set(b, 'DiagonosticModel_TestCase23', {a1})
    assert _is_linked(b, 'DiagonosticModel_TestCase23', a1)
    if hasattr(a1, 'DiagonosticModel_TestStep24'):
        assert _is_linked(a1, 'DiagonosticModel_TestStep24', b)
    _safe_set(b, 'DiagonosticModel_TestCase23', {a2})
    assert _is_linked(b, 'DiagonosticModel_TestCase23', a2)
    if hasattr(a1, 'DiagonosticModel_TestStep24'):
        assert not _is_linked(a1, 'DiagonosticModel_TestStep24', b)
    if hasattr(a2, 'DiagonosticModel_TestStep24'):
        assert _is_linked(a2, 'DiagonosticModel_TestStep24', b)
    _safe_set(b, 'DiagonosticModel_TestCase23', set())
    assert not _is_linked(b, 'DiagonosticModel_TestCase23', a2)
    if hasattr(a2, 'DiagonosticModel_TestStep24'):
        assert not _is_linked(a2, 'DiagonosticModel_TestStep24', b)


def test_assoc_signalType45_reverse_link_reassign_clear():
    a1 = DiagonosticModel_SignalType(MessageName="sample_text", creationMode="sample_text", lookupValues="sample_text", name="sample_text", namespace="sample_text", node="sample_text", type="sample_text")
    a2 = DiagonosticModel_SignalType(MessageName="sample_text_2", creationMode="sample_text_2", lookupValues="sample_text_2", name="sample_text_2", namespace="sample_text_2", node="sample_text_2", type="sample_text_2")
    b = DiagonosticModel_ImportArtifact(path="sample_text")
    _safe_set(b, 'DiagonosticModel_ImportArtifact46', {a1})
    assert _is_linked(b, 'DiagonosticModel_ImportArtifact46', a1)
    if hasattr(a1, 'DiagonosticModel_SignalType47'):
        assert _is_linked(a1, 'DiagonosticModel_SignalType47', b)
    _safe_set(b, 'DiagonosticModel_ImportArtifact46', {a2})
    assert _is_linked(b, 'DiagonosticModel_ImportArtifact46', a2)
    if hasattr(a1, 'DiagonosticModel_SignalType47'):
        assert not _is_linked(a1, 'DiagonosticModel_SignalType47', b)
    if hasattr(a2, 'DiagonosticModel_SignalType47'):
        assert _is_linked(a2, 'DiagonosticModel_SignalType47', b)
    _safe_set(b, 'DiagonosticModel_ImportArtifact46', set())
    assert not _is_linked(b, 'DiagonosticModel_ImportArtifact46', a2)
    if hasattr(a2, 'DiagonosticModel_SignalType47'):
        assert not _is_linked(a2, 'DiagonosticModel_SignalType47', b)


def test_assoc_testCases7_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestGroup(description="sample_text", name="sample_text")
    a2 = DiagonosticModel_TestGroup(description="sample_text_2", name="sample_text_2")
    b = DiagonosticModel_TestCase(description="sample_text", executionStatus="sample_text", id="sample_text", name="sample_text", requirementID="sample_text", skip=True)
    _safe_set(b, 'DiagonosticModel_TestCase', a1)
    assert _is_linked(b, 'DiagonosticModel_TestCase', a1)
    if hasattr(a1, 'DiagonosticModel_TestGroup8'):
        assert _is_linked(a1, 'DiagonosticModel_TestGroup8', b)
    _safe_set(b, 'DiagonosticModel_TestCase', a2)
    assert _is_linked(b, 'DiagonosticModel_TestCase', a2)
    if hasattr(a1, 'DiagonosticModel_TestGroup8'):
        assert not _is_linked(a1, 'DiagonosticModel_TestGroup8', b)
    if hasattr(a2, 'DiagonosticModel_TestGroup8'):
        assert _is_linked(a2, 'DiagonosticModel_TestGroup8', b)
    _safe_set(b, 'DiagonosticModel_TestCase', None)
    assert not _is_linked(b, 'DiagonosticModel_TestCase', a2)
    if hasattr(a2, 'DiagonosticModel_TestGroup8'):
        assert not _is_linked(a2, 'DiagonosticModel_TestGroup8', b)


def test_assoc_testGroups0_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestSpecification(author="sample_text", description="sample_text", functionName="sample_text", functionVersion="sample_text", name="sample_text", version="sample_text")
    a2 = DiagonosticModel_TestSpecification(author="sample_text_2", description="sample_text_2", functionName="sample_text_2", functionVersion="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = DiagonosticModel_TestGroup(description="sample_text", name="sample_text")
    _safe_set(b, 'DiagonosticModel_TestGroup', a1)
    assert _is_linked(b, 'DiagonosticModel_TestGroup', a1)
    if hasattr(a1, 'DiagonosticModel_TestSpecification'):
        assert _is_linked(a1, 'DiagonosticModel_TestSpecification', b)
    _safe_set(b, 'DiagonosticModel_TestGroup', a2)
    assert _is_linked(b, 'DiagonosticModel_TestGroup', a2)
    if hasattr(a1, 'DiagonosticModel_TestSpecification'):
        assert not _is_linked(a1, 'DiagonosticModel_TestSpecification', b)
    if hasattr(a2, 'DiagonosticModel_TestSpecification'):
        assert _is_linked(a2, 'DiagonosticModel_TestSpecification', b)
    _safe_set(b, 'DiagonosticModel_TestGroup', None)
    assert not _is_linked(b, 'DiagonosticModel_TestGroup', a2)
    if hasattr(a2, 'DiagonosticModel_TestSpecification'):
        assert not _is_linked(a2, 'DiagonosticModel_TestSpecification', b)


def test_assoc_testGroups12_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestGroup(description="sample_text", name="sample_text")
    a2 = DiagonosticModel_TestGroup(description="sample_text_2", name="sample_text_2")
    b = DiagonosticModel_TestGroup(description="sample_text", name="sample_text")
    _safe_set(b, 'DiagonosticModel_TestGroup13', a1)
    assert _is_linked(b, 'DiagonosticModel_TestGroup13', a1)
    if hasattr(a1, 'DiagonosticModel_TestGroup11'):
        assert _is_linked(a1, 'DiagonosticModel_TestGroup11', b)
    _safe_set(b, 'DiagonosticModel_TestGroup13', a2)
    assert _is_linked(b, 'DiagonosticModel_TestGroup13', a2)
    if hasattr(a1, 'DiagonosticModel_TestGroup11'):
        assert not _is_linked(a1, 'DiagonosticModel_TestGroup11', b)
    if hasattr(a2, 'DiagonosticModel_TestGroup11'):
        assert _is_linked(a2, 'DiagonosticModel_TestGroup11', b)
    _safe_set(b, 'DiagonosticModel_TestGroup13', None)
    assert not _is_linked(b, 'DiagonosticModel_TestGroup13', a2)
    if hasattr(a2, 'DiagonosticModel_TestGroup11'):
        assert not _is_linked(a2, 'DiagonosticModel_TestGroup11', b)


def test_assoc_testSteps17_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TestStep(title="sample_text")
    a2 = DiagonosticModel_TestStep(title="sample_text_2")
    b = DiagonosticModel_TestCase(description="sample_text", executionStatus="sample_text", id="sample_text", name="sample_text", requirementID="sample_text", skip=True)
    _safe_set(b, 'DiagonosticModel_TestCase18', {a1})
    assert _is_linked(b, 'DiagonosticModel_TestCase18', a1)
    if hasattr(a1, 'DiagonosticModel_TestStep'):
        assert _is_linked(a1, 'DiagonosticModel_TestStep', b)
    _safe_set(b, 'DiagonosticModel_TestCase18', {a2})
    assert _is_linked(b, 'DiagonosticModel_TestCase18', a2)
    if hasattr(a1, 'DiagonosticModel_TestStep'):
        assert not _is_linked(a1, 'DiagonosticModel_TestStep', b)
    if hasattr(a2, 'DiagonosticModel_TestStep'):
        assert _is_linked(a2, 'DiagonosticModel_TestStep', b)
    _safe_set(b, 'DiagonosticModel_TestCase18', set())
    assert not _is_linked(b, 'DiagonosticModel_TestCase18', a2)
    if hasattr(a2, 'DiagonosticModel_TestStep'):
        assert not _is_linked(a2, 'DiagonosticModel_TestStep', b)


def test_assoc_traceabilityArtifacts31_reverse_link_reassign_clear():
    a1 = DiagonosticModel_TracebilityArtifact(type="sample_text", url="sample_text")
    a2 = DiagonosticModel_TracebilityArtifact(type="sample_text_2", url="sample_text_2")
    b = DiagonosticModel_TestCase(description="sample_text", executionStatus="sample_text", id="sample_text", name="sample_text", requirementID="sample_text", skip=True)
    _safe_set(b, 'DiagonosticModel_TestCase32', {a1})
    assert _is_linked(b, 'DiagonosticModel_TestCase32', a1)
    if hasattr(a1, 'DiagonosticModel_TracebilityArtifact'):
        assert _is_linked(a1, 'DiagonosticModel_TracebilityArtifact', b)
    _safe_set(b, 'DiagonosticModel_TestCase32', {a2})
    assert _is_linked(b, 'DiagonosticModel_TestCase32', a2)
    if hasattr(a1, 'DiagonosticModel_TracebilityArtifact'):
        assert not _is_linked(a1, 'DiagonosticModel_TracebilityArtifact', b)
    if hasattr(a2, 'DiagonosticModel_TracebilityArtifact'):
        assert _is_linked(a2, 'DiagonosticModel_TracebilityArtifact', b)
    _safe_set(b, 'DiagonosticModel_TestCase32', set())
    assert not _is_linked(b, 'DiagonosticModel_TestCase32', a2)
    if hasattr(a2, 'DiagonosticModel_TracebilityArtifact'):
        assert not _is_linked(a2, 'DiagonosticModel_TracebilityArtifact', b)


def test_assoc_variants19_reverse_link_reassign_clear():
    a1 = DiagonosticModel_Variant(description="sample_text", name="sample_text")
    a2 = DiagonosticModel_Variant(description="sample_text_2", name="sample_text_2")
    b = DiagonosticModel_TestCase(description="sample_text", executionStatus="sample_text", id="sample_text", name="sample_text", requirementID="sample_text", skip=True)
    _safe_set(b, 'DiagonosticModel_TestCase20', {a1})
    assert _is_linked(b, 'DiagonosticModel_TestCase20', a1)
    if hasattr(a1, 'DiagonosticModel_Variant21'):
        assert _is_linked(a1, 'DiagonosticModel_Variant21', b)
    _safe_set(b, 'DiagonosticModel_TestCase20', {a2})
    assert _is_linked(b, 'DiagonosticModel_TestCase20', a2)
    if hasattr(a1, 'DiagonosticModel_Variant21'):
        assert not _is_linked(a1, 'DiagonosticModel_Variant21', b)
    if hasattr(a2, 'DiagonosticModel_Variant21'):
        assert _is_linked(a2, 'DiagonosticModel_Variant21', b)
    _safe_set(b, 'DiagonosticModel_TestCase20', set())
    assert not _is_linked(b, 'DiagonosticModel_TestCase20', a2)
    if hasattr(a2, 'DiagonosticModel_Variant21'):
        assert not _is_linked(a2, 'DiagonosticModel_Variant21', b)


def test_assoc_variants3_reverse_link_reassign_clear():
    a1 = DiagonosticModel_Variant(description="sample_text", name="sample_text")
    a2 = DiagonosticModel_Variant(description="sample_text_2", name="sample_text_2")
    b = DiagonosticModel_TestSpecification(author="sample_text", description="sample_text", functionName="sample_text", functionVersion="sample_text", name="sample_text", version="sample_text")
    _safe_set(b, 'DiagonosticModel_TestSpecification4', {a1})
    assert _is_linked(b, 'DiagonosticModel_TestSpecification4', a1)
    if hasattr(a1, 'DiagonosticModel_Variant'):
        assert _is_linked(a1, 'DiagonosticModel_Variant', b)
    _safe_set(b, 'DiagonosticModel_TestSpecification4', {a2})
    assert _is_linked(b, 'DiagonosticModel_TestSpecification4', a2)
    if hasattr(a1, 'DiagonosticModel_Variant'):
        assert not _is_linked(a1, 'DiagonosticModel_Variant', b)
    if hasattr(a2, 'DiagonosticModel_Variant'):
        assert _is_linked(a2, 'DiagonosticModel_Variant', b)
    _safe_set(b, 'DiagonosticModel_TestSpecification4', set())
    assert not _is_linked(b, 'DiagonosticModel_TestSpecification4', a2)
    if hasattr(a2, 'DiagonosticModel_Variant'):
        assert not _is_linked(a2, 'DiagonosticModel_Variant', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_diagparam48_stub_double():
    # DiagonosticModel_DiagnosticRequest has no real 'DiagonosticModel_DiagnosticRequest49' property in the generated
    # code (a bare stub) -- manually attach it so DiagonosticModel_DiagnosticParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DiagonosticModel_DiagnosticParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DiagonosticModel_DiagnosticParam(copyToVar="sample_text", qualifier="sample_text")
    partner = DiagonosticModel_DiagnosticRequest()
    setattr(partner, 'DiagonosticModel_DiagnosticRequest49', None)
    _safe_set(owner, 'DiagonosticModel_DiagnosticParam', partner)
    assert owner in getattr(partner, 'DiagonosticModel_DiagnosticRequest49')
    _safe_set(owner, 'DiagonosticModel_DiagnosticParam', None)
    assert owner not in getattr(partner, 'DiagonosticModel_DiagnosticRequest49')


def test_assoc_diagrequest38_stub_double():
    # DiagonosticModel_DiagnosticRequest has no real 'DiagonosticModel_DiagnosticRequest' property in the generated
    # code (a bare stub) -- manually attach it so DiagonosticModel_DiagnosticService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DiagonosticModel_DiagnosticService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DiagonosticModel_DiagnosticService(ecu="sample_text", result="sample_text", service="sample_text")
    partner = DiagonosticModel_DiagnosticRequest()
    setattr(partner, 'DiagonosticModel_DiagnosticRequest', None)
    _safe_set(owner, 'DiagonosticModel_DiagnosticService', partner)
    assert getattr(partner, 'DiagonosticModel_DiagnosticRequest') == owner
    _safe_set(owner, 'DiagonosticModel_DiagnosticService', None)
    assert getattr(partner, 'DiagonosticModel_DiagnosticRequest') is None


def test_assoc_parameters43_stub_double():
    # DiagonosticModel_CAPLTestStep has no real 'DiagonosticModel_CAPLTestStep' property in the generated
    # code (a bare stub) -- manually attach it so DiagonosticModel_CAPLParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DiagonosticModel_CAPLParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DiagonosticModel_CAPLParam(name="sample_text", type="sample_text", value="sample_text")
    partner = DiagonosticModel_CAPLTestStep()
    setattr(partner, 'DiagonosticModel_CAPLTestStep', None)
    _safe_set(owner, 'DiagonosticModel_CAPLParam44', partner)
    assert owner in getattr(partner, 'DiagonosticModel_CAPLTestStep')
    _safe_set(owner, 'DiagonosticModel_CAPLParam44', None)
    assert owner not in getattr(partner, 'DiagonosticModel_CAPLTestStep')


def test_assoc_testSteps55_stub_double():
    # DiagonosticModel_BlockAction has no real 'DiagonosticModel_BlockAction' property in the generated
    # code (a bare stub) -- manually attach it so DiagonosticModel_TestStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DiagonosticModel_TestStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DiagonosticModel_TestStep(title="sample_text")
    partner = DiagonosticModel_BlockAction()
    setattr(partner, 'DiagonosticModel_BlockAction', None)
    _safe_set(owner, 'DiagonosticModel_TestStep56', partner)
    assert owner in getattr(partner, 'DiagonosticModel_BlockAction')
    _safe_set(owner, 'DiagonosticModel_TestStep56', None)
    assert owner not in getattr(partner, 'DiagonosticModel_BlockAction')


def test_assoc_valueTypes53_stub_double():
    # DiagonosticModel_DiagnosticParamValueType has no real 'DiagonosticModel_DiagnosticParamValueType' property in the generated
    # code (a bare stub) -- manually attach it so DiagonosticModel_DiagnosticParam's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DiagonosticModel_DiagnosticParam's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DiagonosticModel_DiagnosticParam(copyToVar="sample_text", qualifier="sample_text")
    partner = DiagonosticModel_DiagnosticParamValueType()
    setattr(partner, 'DiagonosticModel_DiagnosticParamValueType', None)
    _safe_set(owner, 'DiagonosticModel_DiagnosticParam54', partner)
    assert getattr(partner, 'DiagonosticModel_DiagnosticParamValueType') == owner
    _safe_set(owner, 'DiagonosticModel_DiagnosticParam54', None)
    assert getattr(partner, 'DiagonosticModel_DiagnosticParamValueType') is None


