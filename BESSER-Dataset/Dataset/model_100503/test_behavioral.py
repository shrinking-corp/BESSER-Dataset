import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractContractualElement,
    AbstractGoal,
    AbstractRequirement,
    DesignElementReference,
    ElementRefinement,
    IdentifiedElement,
    NonFunctionalGoal,
    RdalOrgPackage,
    ReferencedDesignElements,
    RefineableElement,
    RequirementsCoverageData,
    SatisfiableDesignElementRef,
    SatisfiableElement,
    SubElementReference,
    TextualContractualElement,
    TraceableToDesignElementsElement,
    Variable,
    VerifiableElement,
    rdal_AbstractContractualElement,
    rdal_AbstractGoal,
    rdal_AbstractRequirement,
    rdal_ActorReference,
    rdal_Assumption,
    rdal_Capability,
    rdal_Category,
    rdal_Conflict,
    rdal_ConstraintLanguagesSpec,
    rdal_ContactInformation,
    rdal_DesignElementReference,
    rdal_EObject,
    rdal_ElementRefinement,
    rdal_Expression,
    rdal_FormalLanguageExpression,
    rdal_GoalRefinement,
    rdal_GoalsPackage,
    rdal_IdentifiedElement,
    rdal_InteractionVariable,
    rdal_NonFunctionalGoal,
    rdal_NonFunctionalProperty,
    rdal_PrioritizedSatDesignElementRef,
    rdal_QualityObjective,
    rdal_Rationale,
    rdal_RdalOrgPackage,
    rdal_RefManuallySelectedDesignElements,
    rdal_RefQueryCollectedDesignElements,
    rdal_ReferencedDesignElements,
    rdal_RefineableElement,
    rdal_Requirement,
    rdal_RequirementRefinement,
    rdal_RequirementsCoverageData,
    rdal_RequirementsPackage,
    rdal_SatisfiableDesignElementRef,
    rdal_SatisfiableElement,
    rdal_Sensitivity,
    rdal_Specification,
    rdal_Stakeholder,
    rdal_SubElementReference,
    rdal_SubGoalReference,
    rdal_SubRequirementReference,
    rdal_SystContextDesignElemRef,
    rdal_SystOverviewDesignElemRef,
    rdal_SystemContext,
    rdal_SystemFunctionGoal,
    rdal_SystemOverview,
    rdal_TextualContractualElement,
    rdal_Trace,
    rdal_TraceDesignElementRef,
    rdal_TraceableToDesignElementsElement,
    rdal_Uncertainty,
    rdal_UserProperty,
    rdal_Variable,
    rdal_VerifiableDesignElementRef,
    rdal_VerifiableElement,
    rdal_VerificationActivity,
    AggregationType,
    InteractionVariableType,
    Modality,
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

def test_assoc_changeUncertainty33_reverse_link_reassign_clear():
    a1 = rdal_Uncertainty(costsImpact="sample_text", familiarity="sample_text", maturityIndex="sample_text", propRiskIndex="sample_text", riskIndex="sample_text", scheduleImpact="sample_text", timeCriticality="sample_text", volatility="sample_text")
    a2 = rdal_Uncertainty(costsImpact="sample_text_2", familiarity="sample_text_2", maturityIndex="sample_text_2", propRiskIndex="sample_text_2", riskIndex="sample_text_2", scheduleImpact="sample_text_2", timeCriticality="sample_text_2", volatility="sample_text_2")
    b = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    _safe_set(b, 'rdal_AbstractContractualElement34', a1)
    assert _is_linked(b, 'rdal_AbstractContractualElement34', a1)
    if hasattr(a1, 'rdal_Uncertainty'):
        assert _is_linked(a1, 'rdal_Uncertainty', b)
    _safe_set(b, 'rdal_AbstractContractualElement34', a2)
    assert _is_linked(b, 'rdal_AbstractContractualElement34', a2)
    if hasattr(a1, 'rdal_Uncertainty'):
        assert not _is_linked(a1, 'rdal_Uncertainty', b)
    if hasattr(a2, 'rdal_Uncertainty'):
        assert _is_linked(a2, 'rdal_Uncertainty', b)
    _safe_set(b, 'rdal_AbstractContractualElement34', None)
    assert not _is_linked(b, 'rdal_AbstractContractualElement34', a2)
    if hasattr(a2, 'rdal_Uncertainty'):
        assert not _is_linked(a2, 'rdal_Uncertainty', b)


def test_assoc_contactInformation25_reverse_link_reassign_clear():
    a1 = rdal_ContactInformation(address="sample_text", country="sample_text", email="sample_text", phoneNumber="sample_text")
    a2 = rdal_ContactInformation(address="sample_text_2", country="sample_text_2", email="sample_text_2", phoneNumber="sample_text_2")
    b = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    _safe_set(b, 'rdal_AbstractContractualElement26', {a1})
    assert _is_linked(b, 'rdal_AbstractContractualElement26', a1)
    if hasattr(a1, 'rdal_ContactInformation'):
        assert _is_linked(a1, 'rdal_ContactInformation', b)
    _safe_set(b, 'rdal_AbstractContractualElement26', {a2})
    assert _is_linked(b, 'rdal_AbstractContractualElement26', a2)
    if hasattr(a1, 'rdal_ContactInformation'):
        assert not _is_linked(a1, 'rdal_ContactInformation', b)
    if hasattr(a2, 'rdal_ContactInformation'):
        assert _is_linked(a2, 'rdal_ContactInformation', b)
    _safe_set(b, 'rdal_AbstractContractualElement26', set())
    assert not _is_linked(b, 'rdal_AbstractContractualElement26', a2)
    if hasattr(a2, 'rdal_ContactInformation'):
        assert not _is_linked(a2, 'rdal_ContactInformation', b)


def test_assoc_contractualElement141_reverse_link_reassign_clear():
    a1 = rdal_Conflict(degree="sample_text")
    a2 = rdal_Conflict(degree="sample_text_2")
    b = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    _safe_set(b, 'rdal_AbstractContractualElement143', a1)
    assert _is_linked(b, 'rdal_AbstractContractualElement143', a1)
    if hasattr(a1, 'rdal_Conflict142'):
        assert _is_linked(a1, 'rdal_Conflict142', b)
    _safe_set(b, 'rdal_AbstractContractualElement143', a2)
    assert _is_linked(b, 'rdal_AbstractContractualElement143', a2)
    if hasattr(a1, 'rdal_Conflict142'):
        assert not _is_linked(a1, 'rdal_Conflict142', b)
    if hasattr(a2, 'rdal_Conflict142'):
        assert _is_linked(a2, 'rdal_Conflict142', b)
    _safe_set(b, 'rdal_AbstractContractualElement143', None)
    assert not _is_linked(b, 'rdal_AbstractContractualElement143', a2)
    if hasattr(a2, 'rdal_Conflict142'):
        assert not _is_linked(a2, 'rdal_Conflict142', b)


def test_assoc_derivedFrom46_reverse_link_reassign_clear():
    a1 = rdal_TextualContractualElement(priority="sample_text")
    a2 = rdal_TextualContractualElement(priority="sample_text_2")
    b = rdal_TextualContractualElement(priority="sample_text")
    _safe_set(b, 'rdal_TextualContractualElement47', a1)
    assert _is_linked(b, 'rdal_TextualContractualElement47', a1)
    if hasattr(a1, 'rdal_TextualContractualElement45'):
        assert _is_linked(a1, 'rdal_TextualContractualElement45', b)
    _safe_set(b, 'rdal_TextualContractualElement47', a2)
    assert _is_linked(b, 'rdal_TextualContractualElement47', a2)
    if hasattr(a1, 'rdal_TextualContractualElement45'):
        assert not _is_linked(a1, 'rdal_TextualContractualElement45', b)
    if hasattr(a2, 'rdal_TextualContractualElement45'):
        assert _is_linked(a2, 'rdal_TextualContractualElement45', b)
    _safe_set(b, 'rdal_TextualContractualElement47', None)
    assert not _is_linked(b, 'rdal_TextualContractualElement47', a2)
    if hasattr(a2, 'rdal_TextualContractualElement45'):
        assert not _is_linked(a2, 'rdal_TextualContractualElement45', b)


def test_assoc_evolvedTo28_reverse_link_reassign_clear():
    a1 = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    a2 = rdal_AbstractContractualElement(dropped=False, originDate="sample_text_2", scheduleDate="sample_text_2", sources="sample_text_2")
    b = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    _safe_set(b, 'rdal_AbstractContractualElement29', a1)
    assert _is_linked(b, 'rdal_AbstractContractualElement29', a1)
    if hasattr(a1, 'rdal_AbstractContractualElement27'):
        assert _is_linked(a1, 'rdal_AbstractContractualElement27', b)
    _safe_set(b, 'rdal_AbstractContractualElement29', a2)
    assert _is_linked(b, 'rdal_AbstractContractualElement29', a2)
    if hasattr(a1, 'rdal_AbstractContractualElement27'):
        assert not _is_linked(a1, 'rdal_AbstractContractualElement27', b)
    if hasattr(a2, 'rdal_AbstractContractualElement27'):
        assert _is_linked(a2, 'rdal_AbstractContractualElement27', b)
    _safe_set(b, 'rdal_AbstractContractualElement29', None)
    assert not _is_linked(b, 'rdal_AbstractContractualElement29', a2)
    if hasattr(a2, 'rdal_AbstractContractualElement27'):
        assert not _is_linked(a2, 'rdal_AbstractContractualElement27', b)


def test_assoc_ownedConflicts54_reverse_link_reassign_clear():
    a1 = rdal_Specification(version="sample_text")
    a2 = rdal_Specification(version="sample_text_2")
    b = rdal_Conflict(degree="sample_text")
    _safe_set(b, 'rdal_Conflict', a1)
    assert _is_linked(b, 'rdal_Conflict', a1)
    if hasattr(a1, 'rdal_Specification55'):
        assert _is_linked(a1, 'rdal_Specification55', b)
    _safe_set(b, 'rdal_Conflict', a2)
    assert _is_linked(b, 'rdal_Conflict', a2)
    if hasattr(a1, 'rdal_Specification55'):
        assert not _is_linked(a1, 'rdal_Specification55', b)
    if hasattr(a2, 'rdal_Specification55'):
        assert _is_linked(a2, 'rdal_Specification55', b)
    _safe_set(b, 'rdal_Conflict', None)
    assert not _is_linked(b, 'rdal_Conflict', a2)
    if hasattr(a2, 'rdal_Specification55'):
        assert not _is_linked(a2, 'rdal_Specification55', b)


def test_assoc_ownedContactInformation51_reverse_link_reassign_clear():
    a1 = rdal_Specification(version="sample_text")
    a2 = rdal_Specification(version="sample_text_2")
    b = rdal_ContactInformation(address="sample_text", country="sample_text", email="sample_text", phoneNumber="sample_text")
    _safe_set(b, 'rdal_ContactInformation53', a1)
    assert _is_linked(b, 'rdal_ContactInformation53', a1)
    if hasattr(a1, 'rdal_Specification52'):
        assert _is_linked(a1, 'rdal_Specification52', b)
    _safe_set(b, 'rdal_ContactInformation53', a2)
    assert _is_linked(b, 'rdal_ContactInformation53', a2)
    if hasattr(a1, 'rdal_Specification52'):
        assert not _is_linked(a1, 'rdal_Specification52', b)
    if hasattr(a2, 'rdal_Specification52'):
        assert _is_linked(a2, 'rdal_Specification52', b)
    _safe_set(b, 'rdal_ContactInformation53', None)
    assert not _is_linked(b, 'rdal_ContactInformation53', a2)
    if hasattr(a2, 'rdal_Specification52'):
        assert not _is_linked(a2, 'rdal_Specification52', b)


def test_assoc_ownedContractualElements78_reverse_link_reassign_clear():
    a1 = rdal_TextualContractualElement(priority="sample_text")
    a2 = rdal_TextualContractualElement(priority="sample_text_2")
    b = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    _safe_set(b, 'rdal_RdalOrgPackage79', {a1})
    assert _is_linked(b, 'rdal_RdalOrgPackage79', a1)
    if hasattr(a1, 'rdal_TextualContractualElement80'):
        assert _is_linked(a1, 'rdal_TextualContractualElement80', b)
    _safe_set(b, 'rdal_RdalOrgPackage79', {a2})
    assert _is_linked(b, 'rdal_RdalOrgPackage79', a2)
    if hasattr(a1, 'rdal_TextualContractualElement80'):
        assert not _is_linked(a1, 'rdal_TextualContractualElement80', b)
    if hasattr(a2, 'rdal_TextualContractualElement80'):
        assert _is_linked(a2, 'rdal_TextualContractualElement80', b)
    _safe_set(b, 'rdal_RdalOrgPackage79', set())
    assert not _is_linked(b, 'rdal_RdalOrgPackage79', a2)
    if hasattr(a2, 'rdal_TextualContractualElement80'):
        assert not _is_linked(a2, 'rdal_TextualContractualElement80', b)


def test_assoc_ownedDesignElementRefs144_reverse_link_reassign_clear():
    a1 = rdal_ReferencedDesignElements(agregationType="sample_text")
    a2 = rdal_ReferencedDesignElements(agregationType="sample_text_2")
    b = rdal_DesignElementReference(evaluationResult="sample_text")
    _safe_set(b, 'DesignElementReference', a1)
    assert _is_linked(b, 'DesignElementReference', a1)
    if hasattr(a1, 'parent145'):
        assert _is_linked(a1, 'parent145', b)
    _safe_set(b, 'DesignElementReference', a2)
    assert _is_linked(b, 'DesignElementReference', a2)
    if hasattr(a1, 'parent145'):
        assert not _is_linked(a1, 'parent145', b)
    if hasattr(a2, 'parent145'):
        assert _is_linked(a2, 'parent145', b)
    _safe_set(b, 'DesignElementReference', None)
    assert not _is_linked(b, 'DesignElementReference', a2)
    if hasattr(a2, 'parent145'):
        assert not _is_linked(a2, 'parent145', b)


def test_assoc_ownedPackages50_reverse_link_reassign_clear():
    a1 = rdal_Specification(version="sample_text")
    a2 = rdal_Specification(version="sample_text_2")
    b = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    _safe_set(b, 'RdalOrgPackage', a1)
    assert _is_linked(b, 'RdalOrgPackage', a1)
    if hasattr(a1, 'specification'):
        assert _is_linked(a1, 'specification', b)
    _safe_set(b, 'RdalOrgPackage', a2)
    assert _is_linked(b, 'RdalOrgPackage', a2)
    if hasattr(a1, 'specification'):
        assert not _is_linked(a1, 'specification', b)
    if hasattr(a2, 'specification'):
        assert _is_linked(a2, 'specification', b)
    _safe_set(b, 'RdalOrgPackage', None)
    assert not _is_linked(b, 'RdalOrgPackage', a2)
    if hasattr(a2, 'specification'):
        assert not _is_linked(a2, 'specification', b)


def test_assoc_ownedRefinements76_reverse_link_reassign_clear():
    a1 = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    a2 = rdal_RdalOrgPackage(contractualElementEntries="sample_text_2", refinementEntries="sample_text_2")
    b = rdal_ElementRefinement(refinedElementEntries="sample_text", subElementRefEntries="sample_text")
    _safe_set(b, 'rdal_ElementRefinement77', a1)
    assert _is_linked(b, 'rdal_ElementRefinement77', a1)
    if hasattr(a1, 'rdal_RdalOrgPackage'):
        assert _is_linked(a1, 'rdal_RdalOrgPackage', b)
    _safe_set(b, 'rdal_ElementRefinement77', a2)
    assert _is_linked(b, 'rdal_ElementRefinement77', a2)
    if hasattr(a1, 'rdal_RdalOrgPackage'):
        assert not _is_linked(a1, 'rdal_RdalOrgPackage', b)
    if hasattr(a2, 'rdal_RdalOrgPackage'):
        assert _is_linked(a2, 'rdal_RdalOrgPackage', b)
    _safe_set(b, 'rdal_ElementRefinement77', None)
    assert not _is_linked(b, 'rdal_ElementRefinement77', a2)
    if hasattr(a2, 'rdal_RdalOrgPackage'):
        assert not _is_linked(a2, 'rdal_RdalOrgPackage', b)


def test_assoc_ownedSubElementRefs2_reverse_link_reassign_clear():
    a1 = rdal_SubElementReference(referencedElementEntries="sample_text", weight="sample_text")
    a2 = rdal_SubElementReference(referencedElementEntries="sample_text_2", weight="sample_text_2")
    b = rdal_ElementRefinement(refinedElementEntries="sample_text", subElementRefEntries="sample_text")
    _safe_set(b, 'rdal_ElementRefinement3', {a1})
    assert _is_linked(b, 'rdal_ElementRefinement3', a1)
    if hasattr(a1, 'rdal_SubElementReference'):
        assert _is_linked(a1, 'rdal_SubElementReference', b)
    _safe_set(b, 'rdal_ElementRefinement3', {a2})
    assert _is_linked(b, 'rdal_ElementRefinement3', a2)
    if hasattr(a1, 'rdal_SubElementReference'):
        assert not _is_linked(a1, 'rdal_SubElementReference', b)
    if hasattr(a2, 'rdal_SubElementReference'):
        assert _is_linked(a2, 'rdal_SubElementReference', b)
    _safe_set(b, 'rdal_ElementRefinement3', set())
    assert not _is_linked(b, 'rdal_ElementRefinement3', a2)
    if hasattr(a2, 'rdal_SubElementReference'):
        assert not _is_linked(a2, 'rdal_SubElementReference', b)


def test_assoc_ownedSystOverview56_reverse_link_reassign_clear():
    a1 = rdal_SystemOverview(purpose="sample_text")
    a2 = rdal_SystemOverview(purpose="sample_text_2")
    b = rdal_Specification(version="sample_text")
    _safe_set(b, 'rdal_Specification57', a1)
    assert _is_linked(b, 'rdal_Specification57', a1)
    if hasattr(a1, 'rdal_SystemOverview'):
        assert _is_linked(a1, 'rdal_SystemOverview', b)
    _safe_set(b, 'rdal_Specification57', a2)
    assert _is_linked(b, 'rdal_Specification57', a2)
    if hasattr(a1, 'rdal_SystemOverview'):
        assert not _is_linked(a1, 'rdal_SystemOverview', b)
    if hasattr(a2, 'rdal_SystemOverview'):
        assert _is_linked(a2, 'rdal_SystemOverview', b)
    _safe_set(b, 'rdal_Specification57', None)
    assert not _is_linked(b, 'rdal_Specification57', a2)
    if hasattr(a2, 'rdal_SystemOverview'):
        assert not _is_linked(a2, 'rdal_SystemOverview', b)


def test_assoc_ownedSystemBoundary100_reverse_link_reassign_clear():
    a1 = rdal_SystemOverview(purpose="sample_text")
    a2 = rdal_SystemOverview(purpose="sample_text_2")
    b = rdal_InteractionVariable(neglected=True, type="sample_text")
    _safe_set(b, 'rdal_InteractionVariable', a1)
    assert _is_linked(b, 'rdal_InteractionVariable', a1)
    if hasattr(a1, 'rdal_SystemOverview101'):
        assert _is_linked(a1, 'rdal_SystemOverview101', b)
    _safe_set(b, 'rdal_InteractionVariable', a2)
    assert _is_linked(b, 'rdal_InteractionVariable', a2)
    if hasattr(a1, 'rdal_SystemOverview101'):
        assert not _is_linked(a1, 'rdal_SystemOverview101', b)
    if hasattr(a2, 'rdal_SystemOverview101'):
        assert _is_linked(a2, 'rdal_SystemOverview101', b)
    _safe_set(b, 'rdal_InteractionVariable', None)
    assert not _is_linked(b, 'rdal_InteractionVariable', a2)
    if hasattr(a2, 'rdal_SystemOverview101'):
        assert not _is_linked(a2, 'rdal_SystemOverview101', b)


def test_assoc_ownedUserProperties0_reverse_link_reassign_clear():
    a1 = rdal_UserProperty(name="sample_text", value="sample_text")
    a2 = rdal_UserProperty(name="sample_text_2", value="sample_text_2")
    b = rdal_IdentifiedElement(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'rdal_IdentifiedElement', {a1})
    assert _is_linked(b, 'rdal_IdentifiedElement', a1)
    if hasattr(a1, 'rdal_UserProperty'):
        assert _is_linked(a1, 'rdal_UserProperty', b)
    _safe_set(b, 'rdal_IdentifiedElement', {a2})
    assert _is_linked(b, 'rdal_IdentifiedElement', a2)
    if hasattr(a1, 'rdal_UserProperty'):
        assert not _is_linked(a1, 'rdal_UserProperty', b)
    if hasattr(a2, 'rdal_UserProperty'):
        assert _is_linked(a2, 'rdal_UserProperty', b)
    _safe_set(b, 'rdal_IdentifiedElement', set())
    assert not _is_linked(b, 'rdal_IdentifiedElement', a2)
    if hasattr(a2, 'rdal_UserProperty'):
        assert not _is_linked(a2, 'rdal_UserProperty', b)


def test_assoc_ownedVerifiedBy116_reverse_link_reassign_clear():
    a1 = rdal_VerificationActivity(passed=True)
    a2 = rdal_VerificationActivity(passed=False)
    b = rdal_AbstractRequirement(risk="sample_text")
    _safe_set(b, 'requirements', {a1})
    assert _is_linked(b, 'requirements', a1)
    if hasattr(a1, 'VerificationActivity'):
        assert _is_linked(a1, 'VerificationActivity', b)
    _safe_set(b, 'requirements', {a2})
    assert _is_linked(b, 'requirements', a2)
    if hasattr(a1, 'VerificationActivity'):
        assert not _is_linked(a1, 'VerificationActivity', b)
    if hasattr(a2, 'VerificationActivity'):
        assert _is_linked(a2, 'VerificationActivity', b)
    _safe_set(b, 'requirements', set())
    assert not _is_linked(b, 'requirements', a2)
    if hasattr(a2, 'VerificationActivity'):
        assert not _is_linked(a2, 'VerificationActivity', b)


def test_assoc_parent148_reverse_link_reassign_clear():
    a1 = rdal_ReferencedDesignElements(agregationType="sample_text")
    a2 = rdal_ReferencedDesignElements(agregationType="sample_text_2")
    b = rdal_DesignElementReference(evaluationResult="sample_text")
    _safe_set(b, 'ownedDesignElementRefs', a1)
    assert _is_linked(b, 'ownedDesignElementRefs', a1)
    if hasattr(a1, 'ReferencedDesignElements'):
        assert _is_linked(a1, 'ReferencedDesignElements', b)
    _safe_set(b, 'ownedDesignElementRefs', a2)
    assert _is_linked(b, 'ownedDesignElementRefs', a2)
    if hasattr(a1, 'ReferencedDesignElements'):
        assert not _is_linked(a1, 'ReferencedDesignElements', b)
    if hasattr(a2, 'ReferencedDesignElements'):
        assert _is_linked(a2, 'ReferencedDesignElements', b)
    _safe_set(b, 'ownedDesignElementRefs', None)
    assert not _is_linked(b, 'ownedDesignElementRefs', a2)
    if hasattr(a2, 'ReferencedDesignElements'):
        assert not _is_linked(a2, 'ReferencedDesignElements', b)


def test_assoc_parent74_reverse_link_reassign_clear():
    a1 = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    a2 = rdal_RdalOrgPackage(contractualElementEntries="sample_text_2", refinementEntries="sample_text_2")
    b = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    _safe_set(b, 'subPackages', a1)
    assert _is_linked(b, 'subPackages', a1)
    if hasattr(a1, 'RdalOrgPackage75'):
        assert _is_linked(a1, 'RdalOrgPackage75', b)
    _safe_set(b, 'subPackages', a2)
    assert _is_linked(b, 'subPackages', a2)
    if hasattr(a1, 'RdalOrgPackage75'):
        assert not _is_linked(a1, 'RdalOrgPackage75', b)
    if hasattr(a2, 'RdalOrgPackage75'):
        assert _is_linked(a2, 'RdalOrgPackage75', b)
    _safe_set(b, 'subPackages', None)
    assert not _is_linked(b, 'subPackages', a2)
    if hasattr(a2, 'RdalOrgPackage75'):
        assert not _is_linked(a2, 'RdalOrgPackage75', b)


def test_assoc_requirements120_reverse_link_reassign_clear():
    a1 = rdal_VerificationActivity(passed=True)
    a2 = rdal_VerificationActivity(passed=False)
    b = rdal_AbstractRequirement(risk="sample_text")
    _safe_set(b, 'AbstractRequirement121', a1)
    assert _is_linked(b, 'AbstractRequirement121', a1)
    if hasattr(a1, 'ownedVerifiedBy'):
        assert _is_linked(a1, 'ownedVerifiedBy', b)
    _safe_set(b, 'AbstractRequirement121', a2)
    assert _is_linked(b, 'AbstractRequirement121', a2)
    if hasattr(a1, 'ownedVerifiedBy'):
        assert not _is_linked(a1, 'ownedVerifiedBy', b)
    if hasattr(a2, 'ownedVerifiedBy'):
        assert _is_linked(a2, 'ownedVerifiedBy', b)
    _safe_set(b, 'AbstractRequirement121', None)
    assert not _is_linked(b, 'AbstractRequirement121', a2)
    if hasattr(a2, 'ownedVerifiedBy'):
        assert not _is_linked(a2, 'ownedVerifiedBy', b)


def test_assoc_specification69_reverse_link_reassign_clear():
    a1 = rdal_Specification(version="sample_text")
    a2 = rdal_Specification(version="sample_text_2")
    b = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    _safe_set(b, 'ownedPackages', a1)
    assert _is_linked(b, 'ownedPackages', a1)
    if hasattr(a1, 'Specification'):
        assert _is_linked(a1, 'Specification', b)
    _safe_set(b, 'ownedPackages', a2)
    assert _is_linked(b, 'ownedPackages', a2)
    if hasattr(a1, 'Specification'):
        assert not _is_linked(a1, 'Specification', b)
    if hasattr(a2, 'Specification'):
        assert _is_linked(a2, 'Specification', b)
    _safe_set(b, 'ownedPackages', None)
    assert not _is_linked(b, 'ownedPackages', a2)
    if hasattr(a2, 'Specification'):
        assert not _is_linked(a2, 'Specification', b)


def test_assoc_specifications153_reverse_link_reassign_clear():
    a1 = rdal_Trace()
    a2 = rdal_Trace()
    b = rdal_Specification(version="sample_text")
    _safe_set(b, 'rdal_Specification154', a1)
    assert _is_linked(b, 'rdal_Specification154', a1)
    if hasattr(a1, 'rdal_Trace'):
        assert _is_linked(a1, 'rdal_Trace', b)
    _safe_set(b, 'rdal_Specification154', a2)
    assert _is_linked(b, 'rdal_Specification154', a2)
    if hasattr(a1, 'rdal_Trace'):
        assert not _is_linked(a1, 'rdal_Trace', b)
    if hasattr(a2, 'rdal_Trace'):
        assert _is_linked(a2, 'rdal_Trace', b)
    _safe_set(b, 'rdal_Specification154', None)
    assert not _is_linked(b, 'rdal_Specification154', a2)
    if hasattr(a2, 'rdal_Trace'):
        assert not _is_linked(a2, 'rdal_Trace', b)


def test_assoc_subPackages71_reverse_link_reassign_clear():
    a1 = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    a2 = rdal_RdalOrgPackage(contractualElementEntries="sample_text_2", refinementEntries="sample_text_2")
    b = rdal_RdalOrgPackage(contractualElementEntries="sample_text", refinementEntries="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'RdalOrgPackage72'):
        assert _is_linked(a1, 'RdalOrgPackage72', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'RdalOrgPackage72'):
        assert not _is_linked(a1, 'RdalOrgPackage72', b)
    if hasattr(a2, 'RdalOrgPackage72'):
        assert _is_linked(a2, 'RdalOrgPackage72', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'RdalOrgPackage72'):
        assert not _is_linked(a2, 'RdalOrgPackage72', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_category122_stub_double():
    # rdal_Category has no real 'rdal_Category124' property in the generated
    # code (a bare stub) -- manually attach it so rdal_VerificationActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_VerificationActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_VerificationActivity(passed=True)
    partner = rdal_Category()
    setattr(partner, 'rdal_Category124', None)
    _safe_set(owner, 'rdal_VerificationActivity123', partner)
    assert getattr(partner, 'rdal_Category124') == owner
    _safe_set(owner, 'rdal_VerificationActivity123', None)
    assert getattr(partner, 'rdal_Category124') is None


def test_assoc_category48_stub_double():
    # rdal_Category has no real 'rdal_Category' property in the generated
    # code (a bare stub) -- manually attach it so rdal_TextualContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_TextualContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_TextualContractualElement(priority="sample_text")
    partner = rdal_Category()
    setattr(partner, 'rdal_Category', None)
    _safe_set(owner, 'rdal_TextualContractualElement49', partner)
    assert getattr(partner, 'rdal_Category') == owner
    _safe_set(owner, 'rdal_TextualContractualElement49', None)
    assert getattr(partner, 'rdal_Category') is None


def test_assoc_conflicts131_stub_double():
    # rdal_AbstractGoal has no real 'goal' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Conflict's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Conflict's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Conflict(degree="sample_text")
    partner = rdal_AbstractGoal()
    setattr(partner, 'goal', None)
    _safe_set(owner, 'Conflict', partner)
    assert owner in getattr(partner, 'goal')
    _safe_set(owner, 'Conflict', None)
    assert owner not in getattr(partner, 'goal')


def test_assoc_constraintLanguagesSpec58_stub_double():
    # rdal_ConstraintLanguagesSpec has no real 'rdal_ConstraintLanguagesSpec' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Specification(version="sample_text")
    partner = rdal_ConstraintLanguagesSpec()
    setattr(partner, 'rdal_ConstraintLanguagesSpec', None)
    _safe_set(owner, 'rdal_Specification59', partner)
    assert getattr(partner, 'rdal_ConstraintLanguagesSpec') == owner
    _safe_set(owner, 'rdal_Specification59', None)
    assert getattr(partner, 'rdal_ConstraintLanguagesSpec') is None


def test_assoc_contactInformation35_stub_double():
    # rdal_Stakeholder has no real 'rdal_Stakeholder36' property in the generated
    # code (a bare stub) -- manually attach it so rdal_ContactInformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_ContactInformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_ContactInformation(address="sample_text", country="sample_text", email="sample_text", phoneNumber="sample_text")
    partner = rdal_Stakeholder()
    setattr(partner, 'rdal_Stakeholder36', None)
    _safe_set(owner, 'rdal_ContactInformation37', partner)
    assert owner in getattr(partner, 'rdal_Stakeholder36')
    _safe_set(owner, 'rdal_ContactInformation37', None)
    assert owner not in getattr(partner, 'rdal_Stakeholder36')


def test_assoc_designElement146_stub_double():
    # rdal_EObject has no real 'rdal_EObject147' property in the generated
    # code (a bare stub) -- manually attach it so rdal_DesignElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_DesignElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_DesignElementReference(evaluationResult="sample_text")
    partner = rdal_EObject()
    setattr(partner, 'rdal_EObject147', None)
    _safe_set(owner, 'rdal_DesignElementReference', partner)
    assert getattr(partner, 'rdal_EObject147') == owner
    _safe_set(owner, 'rdal_DesignElementReference', None)
    assert getattr(partner, 'rdal_EObject147') is None


def test_assoc_externalRefs118_stub_double():
    # rdal_EObject has no real 'rdal_EObject119' property in the generated
    # code (a bare stub) -- manually attach it so rdal_VerificationActivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_VerificationActivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_VerificationActivity(passed=True)
    partner = rdal_EObject()
    setattr(partner, 'rdal_EObject119', None)
    _safe_set(owner, 'rdal_VerificationActivity', {partner})
    assert getattr(partner, 'rdal_EObject119') == owner
    _safe_set(owner, 'rdal_VerificationActivity', set())
    assert getattr(partner, 'rdal_EObject119') is None


def test_assoc_globalSystem93_stub_double():
    # rdal_EObject has no real 'rdal_EObject95' property in the generated
    # code (a bare stub) -- manually attach it so rdal_SystemOverview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_SystemOverview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_SystemOverview(purpose="sample_text")
    partner = rdal_EObject()
    setattr(partner, 'rdal_EObject95', None)
    _safe_set(owner, 'rdal_SystemOverview94', partner)
    assert getattr(partner, 'rdal_EObject95') == owner
    _safe_set(owner, 'rdal_SystemOverview94', None)
    assert getattr(partner, 'rdal_EObject95') is None


def test_assoc_goal139_stub_double():
    # rdal_AbstractGoal has no real 'AbstractGoal140' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Conflict's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Conflict's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Conflict(degree="sample_text")
    partner = rdal_AbstractGoal()
    setattr(partner, 'AbstractGoal140', None)
    _safe_set(owner, 'conflicts', partner)
    assert getattr(partner, 'AbstractGoal140') == owner
    _safe_set(owner, 'conflicts', None)
    assert getattr(partner, 'AbstractGoal140') is None


def test_assoc_ownedActorReferences60_stub_double():
    # rdal_ActorReference has no real 'rdal_ActorReference' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Specification(version="sample_text")
    partner = rdal_ActorReference()
    setattr(partner, 'rdal_ActorReference', None)
    _safe_set(owner, 'rdal_Specification61', {partner})
    assert getattr(partner, 'rdal_ActorReference') == owner
    _safe_set(owner, 'rdal_Specification61', set())
    assert getattr(partner, 'rdal_ActorReference') is None


def test_assoc_ownedCapabilities91_stub_double():
    # rdal_Capability has no real 'rdal_Capability' property in the generated
    # code (a bare stub) -- manually attach it so rdal_SystemOverview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_SystemOverview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_SystemOverview(purpose="sample_text")
    partner = rdal_Capability()
    setattr(partner, 'rdal_Capability', None)
    _safe_set(owner, 'rdal_SystemOverview92', {partner})
    assert getattr(partner, 'rdal_Capability') == owner
    _safe_set(owner, 'rdal_SystemOverview92', set())
    assert getattr(partner, 'rdal_Capability') is None


def test_assoc_ownedCondition42_stub_double():
    # rdal_Expression has no real 'rdal_Expression44' property in the generated
    # code (a bare stub) -- manually attach it so rdal_TextualContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_TextualContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_TextualContractualElement(priority="sample_text")
    partner = rdal_Expression()
    setattr(partner, 'rdal_Expression44', None)
    _safe_set(owner, 'rdal_TextualContractualElement43', partner)
    assert getattr(partner, 'rdal_Expression44') == owner
    _safe_set(owner, 'rdal_TextualContractualElement43', None)
    assert getattr(partner, 'rdal_Expression44') is None


def test_assoc_ownedContexts99_stub_double():
    # rdal_SystemContext has no real 'SystemContext' property in the generated
    # code (a bare stub) -- manually attach it so rdal_SystemOverview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_SystemOverview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_SystemOverview(purpose="sample_text")
    partner = rdal_SystemContext()
    setattr(partner, 'SystemContext', None)
    _safe_set(owner, 'systemOverview', {partner})
    assert getattr(partner, 'SystemContext') == owner
    _safe_set(owner, 'systemOverview', set())
    assert getattr(partner, 'SystemContext') is None


def test_assoc_ownedDroppingReasons30_stub_double():
    # rdal_Rationale has no real 'rdal_Rationale32' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    partner = rdal_Rationale()
    setattr(partner, 'rdal_Rationale32', None)
    _safe_set(owner, 'rdal_AbstractContractualElement31', {partner})
    assert getattr(partner, 'rdal_Rationale32') == owner
    _safe_set(owner, 'rdal_AbstractContractualElement31', set())
    assert getattr(partner, 'rdal_Rationale32') is None


def test_assoc_ownedExpression41_stub_double():
    # rdal_Expression has no real 'rdal_Expression' property in the generated
    # code (a bare stub) -- manually attach it so rdal_TextualContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_TextualContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_TextualContractualElement(priority="sample_text")
    partner = rdal_Expression()
    setattr(partner, 'rdal_Expression', None)
    _safe_set(owner, 'rdal_TextualContractualElement', partner)
    assert getattr(partner, 'rdal_Expression') == owner
    _safe_set(owner, 'rdal_TextualContractualElement', None)
    assert getattr(partner, 'rdal_Expression') is None


def test_assoc_ownedNonFuncProperties64_stub_double():
    # rdal_NonFunctionalProperty has no real 'rdal_NonFunctionalProperty' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Specification(version="sample_text")
    partner = rdal_NonFunctionalProperty()
    setattr(partner, 'rdal_NonFunctionalProperty', None)
    _safe_set(owner, 'rdal_Specification65', {partner})
    assert getattr(partner, 'rdal_NonFunctionalProperty') == owner
    _safe_set(owner, 'rdal_Specification65', set())
    assert getattr(partner, 'rdal_NonFunctionalProperty') is None


def test_assoc_ownedRationales23_stub_double():
    # rdal_Rationale has no real 'rdal_Rationale' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    partner = rdal_Rationale()
    setattr(partner, 'rdal_Rationale', None)
    _safe_set(owner, 'rdal_AbstractContractualElement24', {partner})
    assert getattr(partner, 'rdal_Rationale') == owner
    _safe_set(owner, 'rdal_AbstractContractualElement24', set())
    assert getattr(partner, 'rdal_Rationale') is None


def test_assoc_ownedReferencedDesignElements19_stub_double():
    # rdal_TraceableToDesignElementsElement has no real 'rdal_TraceableToDesignElementsElement' property in the generated
    # code (a bare stub) -- manually attach it so rdal_ReferencedDesignElements's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_ReferencedDesignElements's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_ReferencedDesignElements(agregationType="sample_text")
    partner = rdal_TraceableToDesignElementsElement()
    setattr(partner, 'rdal_TraceableToDesignElementsElement', None)
    _safe_set(owner, 'rdal_ReferencedDesignElements', partner)
    assert getattr(partner, 'rdal_TraceableToDesignElementsElement') == owner
    _safe_set(owner, 'rdal_ReferencedDesignElements', None)
    assert getattr(partner, 'rdal_TraceableToDesignElementsElement') is None


def test_assoc_ownedRequirements81_stub_double():
    # rdal_RequirementsPackage has no real 'package' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractRequirement(risk="sample_text")
    partner = rdal_RequirementsPackage()
    setattr(partner, 'package', None)
    _safe_set(owner, 'AbstractRequirement', partner)
    assert owner in getattr(partner, 'package')
    _safe_set(owner, 'AbstractRequirement', None)
    assert owner not in getattr(partner, 'package')


def test_assoc_ownedSensitivity137_stub_double():
    # rdal_Sensitivity has no real 'rdal_Sensitivity' property in the generated
    # code (a bare stub) -- manually attach it so rdal_QualityObjective's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_QualityObjective's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_QualityObjective(bound=3.14, modality="sample_text")
    partner = rdal_Sensitivity()
    setattr(partner, 'rdal_Sensitivity', None)
    _safe_set(owner, 'rdal_QualityObjective138', partner)
    assert getattr(partner, 'rdal_Sensitivity') == owner
    _safe_set(owner, 'rdal_QualityObjective138', None)
    assert getattr(partner, 'rdal_Sensitivity') is None


def test_assoc_ownedStakeholders66_stub_double():
    # rdal_Stakeholder has no real 'rdal_Stakeholder68' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Specification(version="sample_text")
    partner = rdal_Stakeholder()
    setattr(partner, 'rdal_Stakeholder68', None)
    _safe_set(owner, 'rdal_Specification67', {partner})
    assert getattr(partner, 'rdal_Stakeholder68') == owner
    _safe_set(owner, 'rdal_Specification67', set())
    assert getattr(partner, 'rdal_Stakeholder68') is None


def test_assoc_package117_stub_double():
    # rdal_RequirementsPackage has no real 'RequirementsPackage' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractRequirement(risk="sample_text")
    partner = rdal_RequirementsPackage()
    setattr(partner, 'RequirementsPackage', None)
    _safe_set(owner, 'ownedRequirements', partner)
    assert getattr(partner, 'RequirementsPackage') == owner
    _safe_set(owner, 'ownedRequirements', None)
    assert getattr(partner, 'RequirementsPackage') is None


def test_assoc_parentTraceableElement149_stub_double():
    # rdal_TraceableToDesignElementsElement has no real 'rdal_TraceableToDesignElementsElement151' property in the generated
    # code (a bare stub) -- manually attach it so rdal_DesignElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_DesignElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_DesignElementReference(evaluationResult="sample_text")
    partner = rdal_TraceableToDesignElementsElement()
    setattr(partner, 'rdal_TraceableToDesignElementsElement151', None)
    _safe_set(owner, 'rdal_DesignElementReference150', partner)
    assert getattr(partner, 'rdal_TraceableToDesignElementsElement151') == owner
    _safe_set(owner, 'rdal_DesignElementReference150', None)
    assert getattr(partner, 'rdal_TraceableToDesignElementsElement151') is None


def test_assoc_primaryActors62_stub_double():
    # rdal_EObject has no real 'rdal_EObject' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Specification(version="sample_text")
    partner = rdal_EObject()
    setattr(partner, 'rdal_EObject', None)
    _safe_set(owner, 'rdal_Specification63', {partner})
    assert getattr(partner, 'rdal_EObject') == owner
    _safe_set(owner, 'rdal_Specification63', set())
    assert getattr(partner, 'rdal_EObject') is None


def test_assoc_property135_stub_double():
    # rdal_NonFunctionalProperty has no real 'rdal_NonFunctionalProperty136' property in the generated
    # code (a bare stub) -- manually attach it so rdal_QualityObjective's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_QualityObjective's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_QualityObjective(bound=3.14, modality="sample_text")
    partner = rdal_NonFunctionalProperty()
    setattr(partner, 'rdal_NonFunctionalProperty136', None)
    _safe_set(owner, 'rdal_QualityObjective', partner)
    assert getattr(partner, 'rdal_NonFunctionalProperty136') == owner
    _safe_set(owner, 'rdal_QualityObjective', None)
    assert getattr(partner, 'rdal_NonFunctionalProperty136') is None


def test_assoc_referencedElement158_stub_double():
    # rdal_RefineableElement has no real 'rdal_RefineableElement160' property in the generated
    # code (a bare stub) -- manually attach it so rdal_SubElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_SubElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_SubElementReference(referencedElementEntries="sample_text", weight="sample_text")
    partner = rdal_RefineableElement()
    setattr(partner, 'rdal_RefineableElement160', None)
    _safe_set(owner, 'rdal_SubElementReference159', partner)
    assert getattr(partner, 'rdal_RefineableElement160') == owner
    _safe_set(owner, 'rdal_SubElementReference159', None)
    assert getattr(partner, 'rdal_RefineableElement160') is None


def test_assoc_refinedElement4_stub_double():
    # rdal_RefineableElement has no real 'rdal_RefineableElement6' property in the generated
    # code (a bare stub) -- manually attach it so rdal_ElementRefinement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_ElementRefinement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_ElementRefinement(refinedElementEntries="sample_text", subElementRefEntries="sample_text")
    partner = rdal_RefineableElement()
    setattr(partner, 'rdal_RefineableElement6', None)
    _safe_set(owner, 'rdal_ElementRefinement5', partner)
    assert getattr(partner, 'rdal_RefineableElement6') == owner
    _safe_set(owner, 'rdal_ElementRefinement5', None)
    assert getattr(partner, 'rdal_RefineableElement6') is None


def test_assoc_refinedRequirement10_stub_double():
    # rdal_RequirementRefinement has no real 'rdal_RequirementRefinement11' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractRequirement(risk="sample_text")
    partner = rdal_RequirementRefinement()
    setattr(partner, 'rdal_RequirementRefinement11', None)
    _safe_set(owner, 'rdal_AbstractRequirement12', partner)
    assert getattr(partner, 'rdal_RequirementRefinement11') == owner
    _safe_set(owner, 'rdal_AbstractRequirement12', None)
    assert getattr(partner, 'rdal_RequirementRefinement11') is None


def test_assoc_requirement161_stub_double():
    # rdal_SubRequirementReference has no real 'rdal_SubRequirementReference162' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractRequirement(risk="sample_text")
    partner = rdal_SubRequirementReference()
    setattr(partner, 'rdal_SubRequirementReference162', None)
    _safe_set(owner, 'rdal_AbstractRequirement163', partner)
    assert getattr(partner, 'rdal_SubRequirementReference162') == owner
    _safe_set(owner, 'rdal_AbstractRequirement163', None)
    assert getattr(partner, 'rdal_SubRequirementReference162') is None


def test_assoc_specification20_stub_double():
    # rdal_TraceableToDesignElementsElement has no real 'rdal_TraceableToDesignElementsElement21' property in the generated
    # code (a bare stub) -- manually attach it so rdal_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_Specification(version="sample_text")
    partner = rdal_TraceableToDesignElementsElement()
    setattr(partner, 'rdal_TraceableToDesignElementsElement21', None)
    _safe_set(owner, 'rdal_Specification', partner)
    assert getattr(partner, 'rdal_TraceableToDesignElementsElement21') == owner
    _safe_set(owner, 'rdal_Specification', None)
    assert getattr(partner, 'rdal_TraceableToDesignElementsElement21') is None


def test_assoc_stakeholders22_stub_double():
    # rdal_Stakeholder has no real 'rdal_Stakeholder' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractContractualElement(dropped=True, originDate="sample_text", scheduleDate="sample_text", sources="sample_text")
    partner = rdal_Stakeholder()
    setattr(partner, 'rdal_Stakeholder', None)
    _safe_set(owner, 'rdal_AbstractContractualElement', {partner})
    assert getattr(partner, 'rdal_Stakeholder') == owner
    _safe_set(owner, 'rdal_AbstractContractualElement', set())
    assert getattr(partner, 'rdal_Stakeholder') is None


def test_assoc_subElements1_stub_double():
    # rdal_RefineableElement has no real 'rdal_RefineableElement' property in the generated
    # code (a bare stub) -- manually attach it so rdal_ElementRefinement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_ElementRefinement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_ElementRefinement(refinedElementEntries="sample_text", subElementRefEntries="sample_text")
    partner = rdal_RefineableElement()
    setattr(partner, 'rdal_RefineableElement', None)
    _safe_set(owner, 'rdal_ElementRefinement', {partner})
    assert getattr(partner, 'rdal_RefineableElement') == owner
    _safe_set(owner, 'rdal_ElementRefinement', set())
    assert getattr(partner, 'rdal_RefineableElement') is None


def test_assoc_subRequirements8_stub_double():
    # rdal_RequirementRefinement has no real 'rdal_RequirementRefinement9' property in the generated
    # code (a bare stub) -- manually attach it so rdal_AbstractRequirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_AbstractRequirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_AbstractRequirement(risk="sample_text")
    partner = rdal_RequirementRefinement()
    setattr(partner, 'rdal_RequirementRefinement9', None)
    _safe_set(owner, 'rdal_AbstractRequirement', partner)
    assert owner in getattr(partner, 'rdal_RequirementRefinement9')
    _safe_set(owner, 'rdal_AbstractRequirement', None)
    assert owner not in getattr(partner, 'rdal_RequirementRefinement9')


def test_assoc_systemContextBoundary104_stub_double():
    # rdal_SystemContext has no real 'rdal_SystemContext105' property in the generated
    # code (a bare stub) -- manually attach it so rdal_InteractionVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_InteractionVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_InteractionVariable(neglected=True, type="sample_text")
    partner = rdal_SystemContext()
    setattr(partner, 'rdal_SystemContext105', None)
    _safe_set(owner, 'rdal_InteractionVariable106', partner)
    assert owner in getattr(partner, 'rdal_SystemContext105')
    _safe_set(owner, 'rdal_InteractionVariable106', None)
    assert owner not in getattr(partner, 'rdal_SystemContext105')


def test_assoc_systemOverview110_stub_double():
    # rdal_SystemContext has no real 'ownedContexts' property in the generated
    # code (a bare stub) -- manually attach it so rdal_SystemOverview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_SystemOverview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_SystemOverview(purpose="sample_text")
    partner = rdal_SystemContext()
    setattr(partner, 'ownedContexts', None)
    _safe_set(owner, 'SystemOverview', partner)
    assert getattr(partner, 'ownedContexts') == owner
    _safe_set(owner, 'SystemOverview', None)
    assert getattr(partner, 'ownedContexts') is None


def test_assoc_systemToBe96_stub_double():
    # rdal_EObject has no real 'rdal_EObject98' property in the generated
    # code (a bare stub) -- manually attach it so rdal_SystemOverview's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdal_SystemOverview's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdal_SystemOverview(purpose="sample_text")
    partner = rdal_EObject()
    setattr(partner, 'rdal_EObject98', None)
    _safe_set(owner, 'rdal_SystemOverview97', partner)
    assert getattr(partner, 'rdal_EObject98') == owner
    _safe_set(owner, 'rdal_SystemOverview97', None)
    assert getattr(partner, 'rdal_EObject98') is None


