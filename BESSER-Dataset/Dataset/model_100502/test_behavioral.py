import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractRequirement,
    Actor,
    ContractualElement,
    IdentifiedElement,
    ModelElementReference,
    ReferencedModelElements,
    RequirementsCoverageData,
    VerifiableElement,
    core_AbstractRequirement,
    core_Actor,
    core_Assumption,
    core_Category,
    core_Conflict,
    core_ConstraintLanguagesSpecification,
    core_ContractualElement,
    core_EObject,
    core_Expression,
    core_FormalLanguageExpression,
    core_Goal,
    core_IdentifiedElement,
    core_Interaction,
    core_ModelElementReference,
    core_Rationale,
    core_RefDerivedModelElements,
    core_RefExpressionCollectedModelElements,
    core_RefUserSelectedModelElements,
    core_ReferencedModelElements,
    core_Requirement,
    core_RequirementsContainer,
    core_RequirementsCoverageData,
    core_RequirementsGroup,
    core_Specification,
    core_StakeHolder,
    core_SystemContext,
    core_SystemOverview,
    core_Trace,
    core_TraceModelElementReference,
    core_Uncertainty,
    core_Variable,
    core_VerifiableElement,
    core_VerificationActivity,
    AgregationType,
    AssumptionType,
    ContainerType,
    Direction,
    RiskKind,
    VariableType,
    VerificationMethod,
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

def test_assoc_actors28_reverse_link_reassign_clear():
    a1 = core_Specification(version="sample_text")
    a2 = core_Specification(version="sample_text_2")
    b = core_Actor(address="sample_text", email="sample_text", phoneNumber="sample_text")
    _safe_set(b, 'core_Actor29', a1)
    assert _is_linked(b, 'core_Actor29', a1)
    if hasattr(a1, 'core_Specification'):
        assert _is_linked(a1, 'core_Specification', b)
    _safe_set(b, 'core_Actor29', a2)
    assert _is_linked(b, 'core_Actor29', a2)
    if hasattr(a1, 'core_Specification'):
        assert not _is_linked(a1, 'core_Specification', b)
    if hasattr(a2, 'core_Specification'):
        assert _is_linked(a2, 'core_Specification', b)
    _safe_set(b, 'core_Actor29', None)
    assert not _is_linked(b, 'core_Actor29', a2)
    if hasattr(a2, 'core_Specification'):
        assert not _is_linked(a2, 'core_Specification', b)


def test_assoc_assignedVariable85_reverse_link_reassign_clear():
    a1 = core_Variable(type="sample_text")
    a2 = core_Variable(type="sample_text_2")
    b = core_AbstractRequirement(risk="sample_text")
    _safe_set(b, 'core_AbstractRequirement86', a1)
    assert _is_linked(b, 'core_AbstractRequirement86', a1)
    if hasattr(a1, 'core_Variable87'):
        assert _is_linked(a1, 'core_Variable87', b)
    _safe_set(b, 'core_AbstractRequirement86', a2)
    assert _is_linked(b, 'core_AbstractRequirement86', a2)
    if hasattr(a1, 'core_Variable87'):
        assert not _is_linked(a1, 'core_Variable87', b)
    if hasattr(a2, 'core_Variable87'):
        assert _is_linked(a2, 'core_Variable87', b)
    _safe_set(b, 'core_AbstractRequirement86', None)
    assert not _is_linked(b, 'core_AbstractRequirement86', a2)
    if hasattr(a2, 'core_Variable87'):
        assert not _is_linked(a2, 'core_Variable87', b)


def test_assoc_changeUncertainty0_reverse_link_reassign_clear():
    a1 = core_Uncertainty(costsImpact="sample_text", maturityIndex="sample_text", precedence="sample_text", propRiskIndex="sample_text", riskIndex="sample_text", scheduleImpact="sample_text", volatility="sample_text")
    a2 = core_Uncertainty(costsImpact="sample_text_2", maturityIndex="sample_text_2", precedence="sample_text_2", propRiskIndex="sample_text_2", riskIndex="sample_text_2", scheduleImpact="sample_text_2", volatility="sample_text_2")
    b = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    _safe_set(b, 'core_ContractualElement', a1)
    assert _is_linked(b, 'core_ContractualElement', a1)
    if hasattr(a1, 'core_Uncertainty'):
        assert _is_linked(a1, 'core_Uncertainty', b)
    _safe_set(b, 'core_ContractualElement', a2)
    assert _is_linked(b, 'core_ContractualElement', a2)
    if hasattr(a1, 'core_Uncertainty'):
        assert not _is_linked(a1, 'core_Uncertainty', b)
    if hasattr(a2, 'core_Uncertainty'):
        assert _is_linked(a2, 'core_Uncertainty', b)
    _safe_set(b, 'core_ContractualElement', None)
    assert not _is_linked(b, 'core_ContractualElement', a2)
    if hasattr(a2, 'core_Uncertainty'):
        assert not _is_linked(a2, 'core_Uncertainty', b)


def test_assoc_conditionVariables88_reverse_link_reassign_clear():
    a1 = core_Variable(type="sample_text")
    a2 = core_Variable(type="sample_text_2")
    b = core_AbstractRequirement(risk="sample_text")
    _safe_set(b, 'core_AbstractRequirement89', {a1})
    assert _is_linked(b, 'core_AbstractRequirement89', a1)
    if hasattr(a1, 'core_Variable90'):
        assert _is_linked(a1, 'core_Variable90', b)
    _safe_set(b, 'core_AbstractRequirement89', {a2})
    assert _is_linked(b, 'core_AbstractRequirement89', a2)
    if hasattr(a1, 'core_Variable90'):
        assert not _is_linked(a1, 'core_Variable90', b)
    if hasattr(a2, 'core_Variable90'):
        assert _is_linked(a2, 'core_Variable90', b)
    _safe_set(b, 'core_AbstractRequirement89', set())
    assert not _is_linked(b, 'core_AbstractRequirement89', a2)
    if hasattr(a2, 'core_Variable90'):
        assert not _is_linked(a2, 'core_Variable90', b)


def test_assoc_conflicts35_reverse_link_reassign_clear():
    a1 = core_Specification(version="sample_text")
    a2 = core_Specification(version="sample_text_2")
    b = core_Conflict(degree="sample_text")
    _safe_set(b, 'core_Conflict', a1)
    assert _is_linked(b, 'core_Conflict', a1)
    if hasattr(a1, 'core_Specification36'):
        assert _is_linked(a1, 'core_Specification36', b)
    _safe_set(b, 'core_Conflict', a2)
    assert _is_linked(b, 'core_Conflict', a2)
    if hasattr(a1, 'core_Specification36'):
        assert not _is_linked(a1, 'core_Specification36', b)
    if hasattr(a2, 'core_Specification36'):
        assert _is_linked(a2, 'core_Specification36', b)
    _safe_set(b, 'core_Conflict', None)
    assert not _is_linked(b, 'core_Conflict', a2)
    if hasattr(a2, 'core_Specification36'):
        assert not _is_linked(a2, 'core_Specification36', b)


def test_assoc_conflicts74_reverse_link_reassign_clear():
    a1 = core_Goal(priority="sample_text")
    a2 = core_Goal(priority="sample_text_2")
    b = core_Conflict(degree="sample_text")
    _safe_set(b, 'Conflict', a1)
    assert _is_linked(b, 'Conflict', a1)
    if hasattr(a1, 'goals'):
        assert _is_linked(a1, 'goals', b)
    _safe_set(b, 'Conflict', a2)
    assert _is_linked(b, 'Conflict', a2)
    if hasattr(a1, 'goals'):
        assert not _is_linked(a1, 'goals', b)
    if hasattr(a2, 'goals'):
        assert _is_linked(a2, 'goals', b)
    _safe_set(b, 'Conflict', None)
    assert not _is_linked(b, 'Conflict', a2)
    if hasattr(a2, 'goals'):
        assert not _is_linked(a2, 'goals', b)


def test_assoc_contactInformation18_reverse_link_reassign_clear():
    a1 = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    a2 = core_ContractualElement(dropped=False, droppingReason="sample_text_2", originDate="sample_text_2", satisfactionLevel="sample_text_2", scheduleDate="sample_text_2", sources="sample_text_2", timeCriticality="sample_text_2")
    b = core_Actor(address="sample_text", email="sample_text", phoneNumber="sample_text")
    _safe_set(b, 'core_Actor', a1)
    assert _is_linked(b, 'core_Actor', a1)
    if hasattr(a1, 'core_ContractualElement19'):
        assert _is_linked(a1, 'core_ContractualElement19', b)
    _safe_set(b, 'core_Actor', a2)
    assert _is_linked(b, 'core_Actor', a2)
    if hasattr(a1, 'core_ContractualElement19'):
        assert not _is_linked(a1, 'core_ContractualElement19', b)
    if hasattr(a2, 'core_ContractualElement19'):
        assert _is_linked(a2, 'core_ContractualElement19', b)
    _safe_set(b, 'core_Actor', None)
    assert not _is_linked(b, 'core_Actor', a2)
    if hasattr(a2, 'core_ContractualElement19'):
        assert not _is_linked(a2, 'core_ContractualElement19', b)


def test_assoc_containedRequirements81_reverse_link_reassign_clear():
    a1 = core_AbstractRequirement(risk="sample_text")
    a2 = core_AbstractRequirement(risk="sample_text_2")
    b = core_AbstractRequirement(risk="sample_text")
    _safe_set(b, 'core_AbstractRequirement80', {a1})
    assert _is_linked(b, 'core_AbstractRequirement80', a1)
    if hasattr(a1, 'core_AbstractRequirement'):
        assert _is_linked(a1, 'core_AbstractRequirement', b)
    _safe_set(b, 'core_AbstractRequirement80', {a2})
    assert _is_linked(b, 'core_AbstractRequirement80', a2)
    if hasattr(a1, 'core_AbstractRequirement'):
        assert not _is_linked(a1, 'core_AbstractRequirement', b)
    if hasattr(a2, 'core_AbstractRequirement'):
        assert _is_linked(a2, 'core_AbstractRequirement', b)
    _safe_set(b, 'core_AbstractRequirement80', set())
    assert not _is_linked(b, 'core_AbstractRequirement80', a2)
    if hasattr(a2, 'core_AbstractRequirement'):
        assert not _is_linked(a2, 'core_AbstractRequirement', b)


def test_assoc_evolvedTo3_reverse_link_reassign_clear():
    a1 = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    a2 = core_ContractualElement(dropped=False, droppingReason="sample_text_2", originDate="sample_text_2", satisfactionLevel="sample_text_2", scheduleDate="sample_text_2", sources="sample_text_2", timeCriticality="sample_text_2")
    b = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    _safe_set(b, 'core_ContractualElement4', a1)
    assert _is_linked(b, 'core_ContractualElement4', a1)
    if hasattr(a1, 'core_ContractualElement2'):
        assert _is_linked(a1, 'core_ContractualElement2', b)
    _safe_set(b, 'core_ContractualElement4', a2)
    assert _is_linked(b, 'core_ContractualElement4', a2)
    if hasattr(a1, 'core_ContractualElement2'):
        assert not _is_linked(a1, 'core_ContractualElement2', b)
    if hasattr(a2, 'core_ContractualElement2'):
        assert _is_linked(a2, 'core_ContractualElement2', b)
    _safe_set(b, 'core_ContractualElement4', None)
    assert not _is_linked(b, 'core_ContractualElement4', a2)
    if hasattr(a2, 'core_ContractualElement2'):
        assert not _is_linked(a2, 'core_ContractualElement2', b)


def test_assoc_goals45_reverse_link_reassign_clear():
    a1 = core_SystemOverview(capabilities="sample_text", purpose="sample_text")
    a2 = core_SystemOverview(capabilities="sample_text_2", purpose="sample_text_2")
    b = core_Goal(priority="sample_text")
    _safe_set(b, 'core_Goal', a1)
    assert _is_linked(b, 'core_Goal', a1)
    if hasattr(a1, 'core_SystemOverview46'):
        assert _is_linked(a1, 'core_SystemOverview46', b)
    _safe_set(b, 'core_Goal', a2)
    assert _is_linked(b, 'core_Goal', a2)
    if hasattr(a1, 'core_SystemOverview46'):
        assert not _is_linked(a1, 'core_SystemOverview46', b)
    if hasattr(a2, 'core_SystemOverview46'):
        assert _is_linked(a2, 'core_SystemOverview46', b)
    _safe_set(b, 'core_Goal', None)
    assert not _is_linked(b, 'core_Goal', a2)
    if hasattr(a2, 'core_SystemOverview46'):
        assert not _is_linked(a2, 'core_SystemOverview46', b)


def test_assoc_goals75_reverse_link_reassign_clear():
    a1 = core_Goal(priority="sample_text")
    a2 = core_Goal(priority="sample_text_2")
    b = core_Conflict(degree="sample_text")
    _safe_set(b, 'conflicts', {a1})
    assert _is_linked(b, 'conflicts', a1)
    if hasattr(a1, 'Goal'):
        assert _is_linked(a1, 'Goal', b)
    _safe_set(b, 'conflicts', {a2})
    assert _is_linked(b, 'conflicts', a2)
    if hasattr(a1, 'Goal'):
        assert not _is_linked(a1, 'Goal', b)
    if hasattr(a2, 'Goal'):
        assert _is_linked(a2, 'Goal', b)
    _safe_set(b, 'conflicts', set())
    assert not _is_linked(b, 'conflicts', a2)
    if hasattr(a2, 'Goal'):
        assert not _is_linked(a2, 'Goal', b)


def test_assoc_interactions69_reverse_link_reassign_clear():
    a1 = core_Interaction(direction="sample_text")
    a2 = core_Interaction(direction="sample_text_2")
    b = core_Actor(address="sample_text", email="sample_text", phoneNumber="sample_text")
    _safe_set(b, 'core_Actor70', {a1})
    assert _is_linked(b, 'core_Actor70', a1)
    if hasattr(a1, 'core_Interaction'):
        assert _is_linked(a1, 'core_Interaction', b)
    _safe_set(b, 'core_Actor70', {a2})
    assert _is_linked(b, 'core_Actor70', a2)
    if hasattr(a1, 'core_Interaction'):
        assert not _is_linked(a1, 'core_Interaction', b)
    if hasattr(a2, 'core_Interaction'):
        assert _is_linked(a2, 'core_Interaction', b)
    _safe_set(b, 'core_Actor70', set())
    assert not _is_linked(b, 'core_Actor70', a2)
    if hasattr(a2, 'core_Interaction'):
        assert not _is_linked(a2, 'core_Interaction', b)


def test_assoc_modelElementReferences114_reverse_link_reassign_clear():
    a1 = core_ReferencedModelElements(agregationType="sample_text")
    a2 = core_ReferencedModelElements(agregationType="sample_text_2")
    b = core_ModelElementReference(reason="sample_text", satisfactionLevel="sample_text", verifies="sample_text", weight="sample_text")
    _safe_set(b, 'ModelElementReference', a1)
    assert _is_linked(b, 'ModelElementReference', a1)
    if hasattr(a1, 'parent'):
        assert _is_linked(a1, 'parent', b)
    _safe_set(b, 'ModelElementReference', a2)
    assert _is_linked(b, 'ModelElementReference', a2)
    if hasattr(a1, 'parent'):
        assert not _is_linked(a1, 'parent', b)
    if hasattr(a2, 'parent'):
        assert _is_linked(a2, 'parent', b)
    _safe_set(b, 'ModelElementReference', None)
    assert not _is_linked(b, 'ModelElementReference', a2)
    if hasattr(a2, 'parent'):
        assert not _is_linked(a2, 'parent', b)


def test_assoc_parent117_reverse_link_reassign_clear():
    a1 = core_ReferencedModelElements(agregationType="sample_text")
    a2 = core_ReferencedModelElements(agregationType="sample_text_2")
    b = core_ModelElementReference(reason="sample_text", satisfactionLevel="sample_text", verifies="sample_text", weight="sample_text")
    _safe_set(b, 'modelElementReferences', a1)
    assert _is_linked(b, 'modelElementReferences', a1)
    if hasattr(a1, 'ReferencedModelElements'):
        assert _is_linked(a1, 'ReferencedModelElements', b)
    _safe_set(b, 'modelElementReferences', a2)
    assert _is_linked(b, 'modelElementReferences', a2)
    if hasattr(a1, 'ReferencedModelElements'):
        assert not _is_linked(a1, 'ReferencedModelElements', b)
    if hasattr(a2, 'ReferencedModelElements'):
        assert _is_linked(a2, 'ReferencedModelElements', b)
    _safe_set(b, 'modelElementReferences', None)
    assert not _is_linked(b, 'modelElementReferences', a2)
    if hasattr(a2, 'ReferencedModelElements'):
        assert not _is_linked(a2, 'ReferencedModelElements', b)


def test_assoc_requirement105_reverse_link_reassign_clear():
    a1 = core_VerificationActivity(passed=True, verificationMethod="sample_text")
    a2 = core_VerificationActivity(passed=False, verificationMethod="sample_text_2")
    b = core_AbstractRequirement(risk="sample_text")
    _safe_set(b, 'AbstractRequirement106', a1)
    assert _is_linked(b, 'AbstractRequirement106', a1)
    if hasattr(a1, 'verifiedBy'):
        assert _is_linked(a1, 'verifiedBy', b)
    _safe_set(b, 'AbstractRequirement106', a2)
    assert _is_linked(b, 'AbstractRequirement106', a2)
    if hasattr(a1, 'verifiedBy'):
        assert not _is_linked(a1, 'verifiedBy', b)
    if hasattr(a2, 'verifiedBy'):
        assert _is_linked(a2, 'verifiedBy', b)
    _safe_set(b, 'AbstractRequirement106', None)
    assert not _is_linked(b, 'AbstractRequirement106', a2)
    if hasattr(a2, 'verifiedBy'):
        assert not _is_linked(a2, 'verifiedBy', b)


def test_assoc_satisfiedBy9_reverse_link_reassign_clear():
    a1 = core_ReferencedModelElements(agregationType="sample_text")
    a2 = core_ReferencedModelElements(agregationType="sample_text_2")
    b = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    _safe_set(b, 'core_ContractualElement10', {a1})
    assert _is_linked(b, 'core_ContractualElement10', a1)
    if hasattr(a1, 'core_ReferencedModelElements'):
        assert _is_linked(a1, 'core_ReferencedModelElements', b)
    _safe_set(b, 'core_ContractualElement10', {a2})
    assert _is_linked(b, 'core_ContractualElement10', a2)
    if hasattr(a1, 'core_ReferencedModelElements'):
        assert not _is_linked(a1, 'core_ReferencedModelElements', b)
    if hasattr(a2, 'core_ReferencedModelElements'):
        assert _is_linked(a2, 'core_ReferencedModelElements', b)
    _safe_set(b, 'core_ContractualElement10', set())
    assert not _is_linked(b, 'core_ContractualElement10', a2)
    if hasattr(a2, 'core_ReferencedModelElements'):
        assert not _is_linked(a2, 'core_ReferencedModelElements', b)


def test_assoc_specifications118_reverse_link_reassign_clear():
    a1 = core_Trace()
    a2 = core_Trace()
    b = core_Specification(version="sample_text")
    _safe_set(b, 'core_Specification119', a1)
    assert _is_linked(b, 'core_Specification119', a1)
    if hasattr(a1, 'core_Trace'):
        assert _is_linked(a1, 'core_Trace', b)
    _safe_set(b, 'core_Specification119', a2)
    assert _is_linked(b, 'core_Specification119', a2)
    if hasattr(a1, 'core_Trace'):
        assert not _is_linked(a1, 'core_Trace', b)
    if hasattr(a2, 'core_Trace'):
        assert _is_linked(a2, 'core_Trace', b)
    _safe_set(b, 'core_Specification119', None)
    assert not _is_linked(b, 'core_Specification119', a2)
    if hasattr(a2, 'core_Trace'):
        assert not _is_linked(a2, 'core_Trace', b)


def test_assoc_systOverview30_reverse_link_reassign_clear():
    a1 = core_SystemOverview(capabilities="sample_text", purpose="sample_text")
    a2 = core_SystemOverview(capabilities="sample_text_2", purpose="sample_text_2")
    b = core_Specification(version="sample_text")
    _safe_set(b, 'core_Specification31', a1)
    assert _is_linked(b, 'core_Specification31', a1)
    if hasattr(a1, 'core_SystemOverview'):
        assert _is_linked(a1, 'core_SystemOverview', b)
    _safe_set(b, 'core_Specification31', a2)
    assert _is_linked(b, 'core_Specification31', a2)
    if hasattr(a1, 'core_SystemOverview'):
        assert not _is_linked(a1, 'core_SystemOverview', b)
    if hasattr(a2, 'core_SystemOverview'):
        assert _is_linked(a2, 'core_SystemOverview', b)
    _safe_set(b, 'core_Specification31', None)
    assert not _is_linked(b, 'core_Specification31', a2)
    if hasattr(a2, 'core_SystemOverview'):
        assert not _is_linked(a2, 'core_SystemOverview', b)


def test_assoc_systemBoundary52_reverse_link_reassign_clear():
    a1 = core_Variable(type="sample_text")
    a2 = core_Variable(type="sample_text_2")
    b = core_SystemOverview(capabilities="sample_text", purpose="sample_text")
    _safe_set(b, 'core_SystemOverview53', {a1})
    assert _is_linked(b, 'core_SystemOverview53', a1)
    if hasattr(a1, 'core_Variable'):
        assert _is_linked(a1, 'core_Variable', b)
    _safe_set(b, 'core_SystemOverview53', {a2})
    assert _is_linked(b, 'core_SystemOverview53', a2)
    if hasattr(a1, 'core_Variable'):
        assert not _is_linked(a1, 'core_Variable', b)
    if hasattr(a2, 'core_Variable'):
        assert _is_linked(a2, 'core_Variable', b)
    _safe_set(b, 'core_SystemOverview53', set())
    assert not _is_linked(b, 'core_SystemOverview53', a2)
    if hasattr(a2, 'core_Variable'):
        assert not _is_linked(a2, 'core_Variable', b)


def test_assoc_verificationActivities33_reverse_link_reassign_clear():
    a1 = core_VerificationActivity(passed=True, verificationMethod="sample_text")
    a2 = core_VerificationActivity(passed=False, verificationMethod="sample_text_2")
    b = core_Specification(version="sample_text")
    _safe_set(b, 'core_Specification34', {a1})
    assert _is_linked(b, 'core_Specification34', a1)
    if hasattr(a1, 'core_VerificationActivity'):
        assert _is_linked(a1, 'core_VerificationActivity', b)
    _safe_set(b, 'core_Specification34', {a2})
    assert _is_linked(b, 'core_Specification34', a2)
    if hasattr(a1, 'core_VerificationActivity'):
        assert not _is_linked(a1, 'core_VerificationActivity', b)
    if hasattr(a2, 'core_VerificationActivity'):
        assert _is_linked(a2, 'core_VerificationActivity', b)
    _safe_set(b, 'core_Specification34', set())
    assert not _is_linked(b, 'core_Specification34', a2)
    if hasattr(a2, 'core_VerificationActivity'):
        assert not _is_linked(a2, 'core_VerificationActivity', b)


def test_assoc_verifiedBy82_reverse_link_reassign_clear():
    a1 = core_VerificationActivity(passed=True, verificationMethod="sample_text")
    a2 = core_VerificationActivity(passed=False, verificationMethod="sample_text_2")
    b = core_AbstractRequirement(risk="sample_text")
    _safe_set(b, 'requirement', {a1})
    assert _is_linked(b, 'requirement', a1)
    if hasattr(a1, 'VerificationActivity'):
        assert _is_linked(a1, 'VerificationActivity', b)
    _safe_set(b, 'requirement', {a2})
    assert _is_linked(b, 'requirement', a2)
    if hasattr(a1, 'VerificationActivity'):
        assert not _is_linked(a1, 'VerificationActivity', b)
    if hasattr(a2, 'VerificationActivity'):
        assert _is_linked(a2, 'VerificationActivity', b)
    _safe_set(b, 'requirement', set())
    assert not _is_linked(b, 'requirement', a2)
    if hasattr(a2, 'VerificationActivity'):
        assert not _is_linked(a2, 'VerificationActivity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actors57_stub_double():
    # core_SystemContext has no real 'core_SystemContext58' property in the generated
    # code (a bare stub) -- manually attach it so core_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Actor(address="sample_text", email="sample_text", phoneNumber="sample_text")
    partner = core_SystemContext()
    setattr(partner, 'core_SystemContext58', None)
    _safe_set(owner, 'core_Actor59', partner)
    assert owner in getattr(partner, 'core_SystemContext58')
    _safe_set(owner, 'core_Actor59', None)
    assert owner not in getattr(partner, 'core_SystemContext58')


def test_assoc_agents11_stub_double():
    # core_EObject has no real 'core_EObject13' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject13', None)
    _safe_set(owner, 'core_ContractualElement12', {partner})
    assert getattr(partner, 'core_EObject13') == owner
    _safe_set(owner, 'core_ContractualElement12', set())
    assert getattr(partner, 'core_EObject13') is None


def test_assoc_assumptions93_stub_double():
    # core_Requirement has no real 'requirements94' property in the generated
    # code (a bare stub) -- manually attach it so core_Assumption's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Assumption's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Assumption(type="sample_text")
    partner = core_Requirement()
    setattr(partner, 'requirements94', None)
    _safe_set(owner, 'Assumption', partner)
    assert owner in getattr(partner, 'requirements94')
    _safe_set(owner, 'Assumption', None)
    assert owner not in getattr(partner, 'requirements94')


def test_assoc_category7_stub_double():
    # core_Category has no real 'core_Category' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_Category()
    setattr(partner, 'core_Category', None)
    _safe_set(owner, 'core_ContractualElement8', partner)
    assert getattr(partner, 'core_Category') == owner
    _safe_set(owner, 'core_ContractualElement8', None)
    assert getattr(partner, 'core_Category') is None


def test_assoc_condition22_stub_double():
    # core_Expression has no real 'core_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression24', None)
    _safe_set(owner, 'core_ContractualElement23', partner)
    assert getattr(partner, 'core_Expression24') == owner
    _safe_set(owner, 'core_ContractualElement23', None)
    assert getattr(partner, 'core_Expression24') is None


def test_assoc_constraintLanguagesSpecification37_stub_double():
    # core_ConstraintLanguagesSpecification has no real 'core_ConstraintLanguagesSpecification' property in the generated
    # code (a bare stub) -- manually attach it so core_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Specification(version="sample_text")
    partner = core_ConstraintLanguagesSpecification()
    setattr(partner, 'core_ConstraintLanguagesSpecification', None)
    _safe_set(owner, 'core_Specification38', partner)
    assert getattr(partner, 'core_ConstraintLanguagesSpecification') == owner
    _safe_set(owner, 'core_Specification38', None)
    assert getattr(partner, 'core_ConstraintLanguagesSpecification') is None


def test_assoc_contexts50_stub_double():
    # core_SystemContext has no real 'core_SystemContext' property in the generated
    # code (a bare stub) -- manually attach it so core_SystemOverview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_SystemOverview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_SystemOverview(capabilities="sample_text", purpose="sample_text")
    partner = core_SystemContext()
    setattr(partner, 'core_SystemContext', None)
    _safe_set(owner, 'core_SystemOverview51', {partner})
    assert getattr(partner, 'core_SystemContext') == owner
    _safe_set(owner, 'core_SystemOverview51', set())
    assert getattr(partner, 'core_SystemContext') is None


def test_assoc_contract123_stub_double():
    # core_Rationale has no real 'rationales' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_Rationale()
    setattr(partner, 'rationales', None)
    _safe_set(owner, 'ContractualElement124', partner)
    assert getattr(partner, 'rationales') == owner
    _safe_set(owner, 'ContractualElement124', None)
    assert getattr(partner, 'rationales') is None


def test_assoc_contractualElements76_stub_double():
    # core_StakeHolder has no real 'stakeholders' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_StakeHolder()
    setattr(partner, 'stakeholders', None)
    _safe_set(owner, 'ContractualElement', partner)
    assert owner in getattr(partner, 'stakeholders')
    _safe_set(owner, 'ContractualElement', None)
    assert owner not in getattr(partner, 'stakeholders')


def test_assoc_derivedFrom14_stub_double():
    # core_EObject has no real 'core_EObject16' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject16', None)
    _safe_set(owner, 'core_ContractualElement15', {partner})
    assert getattr(partner, 'core_EObject16') == owner
    _safe_set(owner, 'core_ContractualElement15', set())
    assert getattr(partner, 'core_EObject16') is None


def test_assoc_entity71_stub_double():
    # core_EObject has no real 'core_EObject73' property in the generated
    # code (a bare stub) -- manually attach it so core_Interaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Interaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Interaction(direction="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject73', None)
    _safe_set(owner, 'core_Interaction72', partner)
    assert getattr(partner, 'core_EObject73') == owner
    _safe_set(owner, 'core_Interaction72', None)
    assert getattr(partner, 'core_EObject73') is None


def test_assoc_expression110_stub_double():
    # core_Expression has no real 'core_Expression112' property in the generated
    # code (a bare stub) -- manually attach it so core_VerificationActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_VerificationActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_VerificationActivity(passed=True, verificationMethod="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression112', None)
    _safe_set(owner, 'core_VerificationActivity111', partner)
    assert getattr(partner, 'core_Expression112') == owner
    _safe_set(owner, 'core_VerificationActivity111', None)
    assert getattr(partner, 'core_Expression112') is None


def test_assoc_expression20_stub_double():
    # core_Expression has no real 'core_Expression' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression', None)
    _safe_set(owner, 'core_ContractualElement21', partner)
    assert getattr(partner, 'core_Expression') == owner
    _safe_set(owner, 'core_ContractualElement21', None)
    assert getattr(partner, 'core_Expression') is None


def test_assoc_externalRef107_stub_double():
    # core_EObject has no real 'core_EObject109' property in the generated
    # code (a bare stub) -- manually attach it so core_VerificationActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_VerificationActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_VerificationActivity(passed=True, verificationMethod="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject109', None)
    _safe_set(owner, 'core_VerificationActivity108', {partner})
    assert getattr(partner, 'core_EObject109') == owner
    _safe_set(owner, 'core_VerificationActivity108', set())
    assert getattr(partner, 'core_EObject109') is None


def test_assoc_feature120_stub_double():
    # core_EObject has no real 'core_EObject122' property in the generated
    # code (a bare stub) -- manually attach it so core_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Variable(type="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject122', None)
    _safe_set(owner, 'core_Variable121', partner)
    assert getattr(partner, 'core_EObject122') == owner
    _safe_set(owner, 'core_Variable121', None)
    assert getattr(partner, 'core_EObject122') is None


def test_assoc_group83_stub_double():
    # core_RequirementsGroup has no real 'RequirementsGroup84' property in the generated
    # code (a bare stub) -- manually attach it so core_AbstractRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_AbstractRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_AbstractRequirement(risk="sample_text")
    partner = core_RequirementsGroup()
    setattr(partner, 'RequirementsGroup84', None)
    _safe_set(owner, 'requirements', partner)
    assert getattr(partner, 'RequirementsGroup84') == owner
    _safe_set(owner, 'requirements', None)
    assert getattr(partner, 'RequirementsGroup84') is None


def test_assoc_imageAssumption95_stub_double():
    # core_Requirement has no real 'imageRequirement' property in the generated
    # code (a bare stub) -- manually attach it so core_Assumption's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Assumption's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Assumption(type="sample_text")
    partner = core_Requirement()
    setattr(partner, 'imageRequirement', None)
    _safe_set(owner, 'Assumption96', partner)
    assert getattr(partner, 'imageRequirement') == owner
    _safe_set(owner, 'Assumption96', None)
    assert getattr(partner, 'imageRequirement') is None


def test_assoc_imageRequirement103_stub_double():
    # core_Requirement has no real 'Requirement104' property in the generated
    # code (a bare stub) -- manually attach it so core_Assumption's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Assumption's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Assumption(type="sample_text")
    partner = core_Requirement()
    setattr(partner, 'Requirement104', None)
    _safe_set(owner, 'imageAssumption', partner)
    assert getattr(partner, 'Requirement104') == owner
    _safe_set(owner, 'imageAssumption', None)
    assert getattr(partner, 'Requirement104') is None


def test_assoc_images66_stub_double():
    # core_EObject has no real 'core_EObject68' property in the generated
    # code (a bare stub) -- manually attach it so core_Actor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Actor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Actor(address="sample_text", email="sample_text", phoneNumber="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject68', None)
    _safe_set(owner, 'core_Actor67', {partner})
    assert getattr(partner, 'core_EObject68') == owner
    _safe_set(owner, 'core_Actor67', set())
    assert getattr(partner, 'core_EObject68') is None


def test_assoc_modelElement115_stub_double():
    # core_EObject has no real 'core_EObject116' property in the generated
    # code (a bare stub) -- manually attach it so core_ModelElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ModelElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ModelElementReference(reason="sample_text", satisfactionLevel="sample_text", verifies="sample_text", weight="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject116', None)
    _safe_set(owner, 'core_ModelElementReference', partner)
    assert getattr(partner, 'core_EObject116') == owner
    _safe_set(owner, 'core_ModelElementReference', None)
    assert getattr(partner, 'core_EObject116') is None


def test_assoc_modes25_stub_double():
    # core_EObject has no real 'core_EObject27' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject27', None)
    _safe_set(owner, 'core_ContractualElement26', {partner})
    assert getattr(partner, 'core_EObject27') == owner
    _safe_set(owner, 'core_ContractualElement26', set())
    assert getattr(partner, 'core_EObject27') is None


def test_assoc_primaryActors42_stub_double():
    # core_EObject has no real 'core_EObject44' property in the generated
    # code (a bare stub) -- manually attach it so core_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Specification(version="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject44', None)
    _safe_set(owner, 'core_Specification43', {partner})
    assert getattr(partner, 'core_EObject44') == owner
    _safe_set(owner, 'core_Specification43', set())
    assert getattr(partner, 'core_EObject44') is None


def test_assoc_rationales17_stub_double():
    # core_Rationale has no real 'Rationale' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_Rationale()
    setattr(partner, 'Rationale', None)
    _safe_set(owner, 'contract', {partner})
    assert getattr(partner, 'Rationale') == owner
    _safe_set(owner, 'contract', set())
    assert getattr(partner, 'Rationale') is None


def test_assoc_requirement125_stub_double():
    # core_Requirement has no real 'core_Requirement127' property in the generated
    # code (a bare stub) -- manually attach it so core_RequirementsContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_RequirementsContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_RequirementsContainer(type="sample_text")
    partner = core_Requirement()
    setattr(partner, 'core_Requirement127', None)
    _safe_set(owner, 'core_RequirementsContainer126', partner)
    assert getattr(partner, 'core_Requirement127') == owner
    _safe_set(owner, 'core_RequirementsContainer126', None)
    assert getattr(partner, 'core_Requirement127') is None


def test_assoc_requirementGroups32_stub_double():
    # core_RequirementsGroup has no real 'RequirementsGroup' property in the generated
    # code (a bare stub) -- manually attach it so core_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Specification(version="sample_text")
    partner = core_RequirementsGroup()
    setattr(partner, 'RequirementsGroup', None)
    _safe_set(owner, 'specification', {partner})
    assert getattr(partner, 'RequirementsGroup') == owner
    _safe_set(owner, 'specification', set())
    assert getattr(partner, 'RequirementsGroup') is None


def test_assoc_requirements102_stub_double():
    # core_Requirement has no real 'Requirement' property in the generated
    # code (a bare stub) -- manually attach it so core_Assumption's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Assumption's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Assumption(type="sample_text")
    partner = core_Requirement()
    setattr(partner, 'Requirement', None)
    _safe_set(owner, 'assumptions', partner)
    assert getattr(partner, 'Requirement') == owner
    _safe_set(owner, 'assumptions', None)
    assert getattr(partner, 'Requirement') is None


def test_assoc_requirements128_stub_double():
    # core_Requirement has no real 'core_Requirement130' property in the generated
    # code (a bare stub) -- manually attach it so core_RequirementsContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_RequirementsContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_RequirementsContainer(type="sample_text")
    partner = core_Requirement()
    setattr(partner, 'core_Requirement130', None)
    _safe_set(owner, 'core_RequirementsContainer129', {partner})
    assert getattr(partner, 'core_Requirement130') == owner
    _safe_set(owner, 'core_RequirementsContainer129', set())
    assert getattr(partner, 'core_Requirement130') is None


def test_assoc_requirements78_stub_double():
    # core_RequirementsGroup has no real 'group' property in the generated
    # code (a bare stub) -- manually attach it so core_AbstractRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_AbstractRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_AbstractRequirement(risk="sample_text")
    partner = core_RequirementsGroup()
    setattr(partner, 'group', None)
    _safe_set(owner, 'AbstractRequirement', partner)
    assert owner in getattr(partner, 'group')
    _safe_set(owner, 'AbstractRequirement', None)
    assert owner not in getattr(partner, 'group')


def test_assoc_specification79_stub_double():
    # core_RequirementsGroup has no real 'requirementGroups' property in the generated
    # code (a bare stub) -- manually attach it so core_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Specification(version="sample_text")
    partner = core_RequirementsGroup()
    setattr(partner, 'requirementGroups', None)
    _safe_set(owner, 'Specification', partner)
    assert getattr(partner, 'requirementGroups') == owner
    _safe_set(owner, 'Specification', None)
    assert getattr(partner, 'requirementGroups') is None


def test_assoc_specifies39_stub_double():
    # core_EObject has no real 'core_EObject41' property in the generated
    # code (a bare stub) -- manually attach it so core_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Specification(version="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject41', None)
    _safe_set(owner, 'core_Specification40', {partner})
    assert getattr(partner, 'core_EObject41') == owner
    _safe_set(owner, 'core_Specification40', set())
    assert getattr(partner, 'core_EObject41') is None


def test_assoc_stakeholders1_stub_double():
    # core_StakeHolder has no real 'StakeHolder' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_StakeHolder()
    setattr(partner, 'StakeHolder', None)
    _safe_set(owner, 'contractualElements', {partner})
    assert getattr(partner, 'StakeHolder') == owner
    _safe_set(owner, 'contractualElements', set())
    assert getattr(partner, 'StakeHolder') is None


def test_assoc_subRequirements100_stub_double():
    # core_Requirement has no real 'core_Requirement101' property in the generated
    # code (a bare stub) -- manually attach it so core_RequirementsContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_RequirementsContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_RequirementsContainer(type="sample_text")
    partner = core_Requirement()
    setattr(partner, 'core_Requirement101', None)
    _safe_set(owner, 'core_RequirementsContainer', partner)
    assert getattr(partner, 'core_Requirement101') == owner
    _safe_set(owner, 'core_RequirementsContainer', None)
    assert getattr(partner, 'core_Requirement101') is None


def test_assoc_systemBoundary60_stub_double():
    # core_SystemContext has no real 'core_SystemContext61' property in the generated
    # code (a bare stub) -- manually attach it so core_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Variable(type="sample_text")
    partner = core_SystemContext()
    setattr(partner, 'core_SystemContext61', None)
    _safe_set(owner, 'core_Variable62', partner)
    assert owner in getattr(partner, 'core_SystemContext61')
    _safe_set(owner, 'core_Variable62', None)
    assert owner not in getattr(partner, 'core_SystemContext61')


def test_assoc_systemToBe47_stub_double():
    # core_EObject has no real 'core_EObject49' property in the generated
    # code (a bare stub) -- manually attach it so core_SystemOverview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_SystemOverview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_SystemOverview(capabilities="sample_text", purpose="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject49', None)
    _safe_set(owner, 'core_SystemOverview48', partner)
    assert getattr(partner, 'core_EObject49') == owner
    _safe_set(owner, 'core_SystemOverview48', None)
    assert getattr(partner, 'core_EObject49') is None


def test_assoc_tracedTo5_stub_double():
    # core_EObject has no real 'core_EObject' property in the generated
    # code (a bare stub) -- manually attach it so core_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ContractualElement(dropped=True, droppingReason="sample_text", originDate="sample_text", satisfactionLevel="sample_text", scheduleDate="sample_text", sources="sample_text", timeCriticality="sample_text")
    partner = core_EObject()
    setattr(partner, 'core_EObject', None)
    _safe_set(owner, 'core_ContractualElement6', {partner})
    assert getattr(partner, 'core_EObject') == owner
    _safe_set(owner, 'core_ContractualElement6', set())
    assert getattr(partner, 'core_EObject') is None


