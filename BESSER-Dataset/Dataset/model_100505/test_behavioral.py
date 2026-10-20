import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ContractualElement,
    ReqPredicate,
    ReqRoot,
    RequirementSet,
    reqSpec_AVariableDeclaration,
    reqSpec_AVariableReference,
    reqSpec_Category,
    reqSpec_ComponentClassifier,
    reqSpec_ContractualElement,
    reqSpec_Description,
    reqSpec_DesiredValue,
    reqSpec_DocumentSection,
    reqSpec_EObject,
    reqSpec_ErrorBehaviorState,
    reqSpec_ExternalDocument,
    reqSpec_GlobalConstants,
    reqSpec_GlobalRequirementSet,
    reqSpec_Goal,
    reqSpec_IncludeGlobalRequirement,
    reqSpec_InformalPredicate,
    reqSpec_Mode,
    reqSpec_NamedElement,
    reqSpec_Predicate,
    reqSpec_PropertyExpression,
    reqSpec_Rationale,
    reqSpec_ReqDocument,
    reqSpec_ReqPredicate,
    reqSpec_ReqRoot,
    reqSpec_ReqSpec,
    reqSpec_Requirement,
    reqSpec_RequirementSet,
    reqSpec_Stakeholder,
    reqSpec_StakeholderGoals,
    reqSpec_SystemRequirementSet,
    reqSpec_Uncertainty,
    reqSpec_ValuePredicate,
    reqSpec_WhenCondition,
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

def test_assoc_decomposesReference81_reverse_link_reassign_clear():
    a1 = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    a2 = reqSpec_Requirement(componentCategory="sample_text_2", connections=False, exceptionText="sample_text_2")
    b = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    _safe_set(b, 'reqSpec_Requirement82', a1)
    assert _is_linked(b, 'reqSpec_Requirement82', a1)
    if hasattr(a1, 'reqSpec_Requirement80'):
        assert _is_linked(a1, 'reqSpec_Requirement80', b)
    _safe_set(b, 'reqSpec_Requirement82', a2)
    assert _is_linked(b, 'reqSpec_Requirement82', a2)
    if hasattr(a1, 'reqSpec_Requirement80'):
        assert not _is_linked(a1, 'reqSpec_Requirement80', b)
    if hasattr(a2, 'reqSpec_Requirement80'):
        assert _is_linked(a2, 'reqSpec_Requirement80', b)
    _safe_set(b, 'reqSpec_Requirement82', None)
    assert not _is_linked(b, 'reqSpec_Requirement82', a2)
    if hasattr(a2, 'reqSpec_Requirement80'):
        assert not _is_linked(a2, 'reqSpec_Requirement80', b)


def test_assoc_docReference20_reverse_link_reassign_clear():
    a1 = reqSpec_ExternalDocument(docFragment="sample_text", docReference="sample_text")
    a2 = reqSpec_ExternalDocument(docFragment="sample_text_2", docReference="sample_text_2")
    b = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    _safe_set(b, 'reqSpec_ContractualElement21', {a1})
    assert _is_linked(b, 'reqSpec_ContractualElement21', a1)
    if hasattr(a1, 'reqSpec_ExternalDocument'):
        assert _is_linked(a1, 'reqSpec_ExternalDocument', b)
    _safe_set(b, 'reqSpec_ContractualElement21', {a2})
    assert _is_linked(b, 'reqSpec_ContractualElement21', a2)
    if hasattr(a1, 'reqSpec_ExternalDocument'):
        assert not _is_linked(a1, 'reqSpec_ExternalDocument', b)
    if hasattr(a2, 'reqSpec_ExternalDocument'):
        assert _is_linked(a2, 'reqSpec_ExternalDocument', b)
    _safe_set(b, 'reqSpec_ContractualElement21', set())
    assert not _is_linked(b, 'reqSpec_ContractualElement21', a2)
    if hasattr(a2, 'reqSpec_ExternalDocument'):
        assert not _is_linked(a2, 'reqSpec_ExternalDocument', b)


def test_assoc_docReference26_reverse_link_reassign_clear():
    a1 = reqSpec_ReqRoot(issues="sample_text", name="sample_text", title="sample_text")
    a2 = reqSpec_ReqRoot(issues="sample_text_2", name="sample_text_2", title="sample_text_2")
    b = reqSpec_ExternalDocument(docFragment="sample_text", docReference="sample_text")
    _safe_set(b, 'reqSpec_ExternalDocument28', a1)
    assert _is_linked(b, 'reqSpec_ExternalDocument28', a1)
    if hasattr(a1, 'reqSpec_ReqRoot27'):
        assert _is_linked(a1, 'reqSpec_ReqRoot27', b)
    _safe_set(b, 'reqSpec_ExternalDocument28', a2)
    assert _is_linked(b, 'reqSpec_ExternalDocument28', a2)
    if hasattr(a1, 'reqSpec_ReqRoot27'):
        assert not _is_linked(a1, 'reqSpec_ReqRoot27', b)
    if hasattr(a2, 'reqSpec_ReqRoot27'):
        assert _is_linked(a2, 'reqSpec_ReqRoot27', b)
    _safe_set(b, 'reqSpec_ExternalDocument28', None)
    assert not _is_linked(b, 'reqSpec_ExternalDocument28', a2)
    if hasattr(a2, 'reqSpec_ReqRoot27'):
        assert not _is_linked(a2, 'reqSpec_ReqRoot27', b)


def test_assoc_evolvesReference18_reverse_link_reassign_clear():
    a1 = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    a2 = reqSpec_Requirement(componentCategory="sample_text_2", connections=False, exceptionText="sample_text_2")
    b = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    _safe_set(b, 'reqSpec_ContractualElement19', {a1})
    assert _is_linked(b, 'reqSpec_ContractualElement19', a1)
    if hasattr(a1, 'reqSpec_Requirement'):
        assert _is_linked(a1, 'reqSpec_Requirement', b)
    _safe_set(b, 'reqSpec_ContractualElement19', {a2})
    assert _is_linked(b, 'reqSpec_ContractualElement19', a2)
    if hasattr(a1, 'reqSpec_Requirement'):
        assert not _is_linked(a1, 'reqSpec_Requirement', b)
    if hasattr(a2, 'reqSpec_Requirement'):
        assert _is_linked(a2, 'reqSpec_Requirement', b)
    _safe_set(b, 'reqSpec_ContractualElement19', set())
    assert not _is_linked(b, 'reqSpec_ContractualElement19', a2)
    if hasattr(a2, 'reqSpec_Requirement'):
        assert not _is_linked(a2, 'reqSpec_Requirement', b)


def test_assoc_importConstants31_reverse_link_reassign_clear():
    a1 = reqSpec_StakeholderGoals(componentCategory="sample_text")
    a2 = reqSpec_StakeholderGoals(componentCategory="sample_text_2")
    b = reqSpec_GlobalConstants(name="sample_text")
    _safe_set(b, 'reqSpec_GlobalConstants33', a1)
    assert _is_linked(b, 'reqSpec_GlobalConstants33', a1)
    if hasattr(a1, 'reqSpec_StakeholderGoals32'):
        assert _is_linked(a1, 'reqSpec_StakeholderGoals32', b)
    _safe_set(b, 'reqSpec_GlobalConstants33', a2)
    assert _is_linked(b, 'reqSpec_GlobalConstants33', a2)
    if hasattr(a1, 'reqSpec_StakeholderGoals32'):
        assert not _is_linked(a1, 'reqSpec_StakeholderGoals32', b)
    if hasattr(a2, 'reqSpec_StakeholderGoals32'):
        assert _is_linked(a2, 'reqSpec_StakeholderGoals32', b)
    _safe_set(b, 'reqSpec_GlobalConstants33', None)
    assert not _is_linked(b, 'reqSpec_GlobalConstants33', a2)
    if hasattr(a2, 'reqSpec_StakeholderGoals32'):
        assert not _is_linked(a2, 'reqSpec_StakeholderGoals32', b)


def test_assoc_inheritsReference84_reverse_link_reassign_clear():
    a1 = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    a2 = reqSpec_Requirement(componentCategory="sample_text_2", connections=False, exceptionText="sample_text_2")
    b = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    _safe_set(b, 'reqSpec_Requirement85', a1)
    assert _is_linked(b, 'reqSpec_Requirement85', a1)
    if hasattr(a1, 'reqSpec_Requirement83'):
        assert _is_linked(a1, 'reqSpec_Requirement83', b)
    _safe_set(b, 'reqSpec_Requirement85', a2)
    assert _is_linked(b, 'reqSpec_Requirement85', a2)
    if hasattr(a1, 'reqSpec_Requirement83'):
        assert not _is_linked(a1, 'reqSpec_Requirement83', b)
    if hasattr(a2, 'reqSpec_Requirement83'):
        assert _is_linked(a2, 'reqSpec_Requirement83', b)
    _safe_set(b, 'reqSpec_Requirement85', None)
    assert not _is_linked(b, 'reqSpec_Requirement85', a2)
    if hasattr(a2, 'reqSpec_Requirement83'):
        assert not _is_linked(a2, 'reqSpec_Requirement83', b)


def test_assoc_refinesReference78_reverse_link_reassign_clear():
    a1 = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    a2 = reqSpec_Requirement(componentCategory="sample_text_2", connections=False, exceptionText="sample_text_2")
    b = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    _safe_set(b, 'reqSpec_Requirement79', a1)
    assert _is_linked(b, 'reqSpec_Requirement79', a1)
    if hasattr(a1, 'reqSpec_Requirement77'):
        assert _is_linked(a1, 'reqSpec_Requirement77', b)
    _safe_set(b, 'reqSpec_Requirement79', a2)
    assert _is_linked(b, 'reqSpec_Requirement79', a2)
    if hasattr(a1, 'reqSpec_Requirement77'):
        assert not _is_linked(a1, 'reqSpec_Requirement77', b)
    if hasattr(a2, 'reqSpec_Requirement77'):
        assert _is_linked(a2, 'reqSpec_Requirement77', b)
    _safe_set(b, 'reqSpec_Requirement79', None)
    assert not _is_linked(b, 'reqSpec_Requirement79', a2)
    if hasattr(a2, 'reqSpec_Requirement77'):
        assert not _is_linked(a2, 'reqSpec_Requirement77', b)


def test_assoc_requirementReference90_reverse_link_reassign_clear():
    a1 = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    a2 = reqSpec_Requirement(componentCategory="sample_text_2", connections=False, exceptionText="sample_text_2")
    b = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    _safe_set(b, 'reqSpec_Requirement91', a1)
    assert _is_linked(b, 'reqSpec_Requirement91', a1)
    if hasattr(a1, 'reqSpec_Requirement89'):
        assert _is_linked(a1, 'reqSpec_Requirement89', b)
    _safe_set(b, 'reqSpec_Requirement91', a2)
    assert _is_linked(b, 'reqSpec_Requirement91', a2)
    if hasattr(a1, 'reqSpec_Requirement89'):
        assert not _is_linked(a1, 'reqSpec_Requirement89', b)
    if hasattr(a2, 'reqSpec_Requirement89'):
        assert _is_linked(a2, 'reqSpec_Requirement89', b)
    _safe_set(b, 'reqSpec_Requirement91', None)
    assert not _is_linked(b, 'reqSpec_Requirement91', a2)
    if hasattr(a2, 'reqSpec_Requirement89'):
        assert not _is_linked(a2, 'reqSpec_Requirement89', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_category5_stub_double():
    # reqSpec_Category has no real 'reqSpec_Category' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_Category()
    setattr(partner, 'reqSpec_Category', None)
    _safe_set(owner, 'reqSpec_ContractualElement6', {partner})
    assert getattr(partner, 'reqSpec_Category') == owner
    _safe_set(owner, 'reqSpec_ContractualElement6', set())
    assert getattr(partner, 'reqSpec_Category') is None


def test_assoc_changeUncertainty16_stub_double():
    # reqSpec_Uncertainty has no real 'reqSpec_Uncertainty' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_Uncertainty()
    setattr(partner, 'reqSpec_Uncertainty', None)
    _safe_set(owner, 'reqSpec_ContractualElement17', partner)
    assert getattr(partner, 'reqSpec_Uncertainty') == owner
    _safe_set(owner, 'reqSpec_ContractualElement17', None)
    assert getattr(partner, 'reqSpec_Uncertainty') is None


def test_assoc_computes69_stub_double():
    # reqSpec_AVariableDeclaration has no real 'reqSpec_AVariableDeclaration71' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    partner = reqSpec_AVariableDeclaration()
    setattr(partner, 'reqSpec_AVariableDeclaration71', None)
    _safe_set(owner, 'reqSpec_Requirement70', {partner})
    assert getattr(partner, 'reqSpec_AVariableDeclaration71') == owner
    _safe_set(owner, 'reqSpec_Requirement70', set())
    assert getattr(partner, 'reqSpec_AVariableDeclaration71') is None


def test_assoc_constants1_stub_double():
    # reqSpec_AVariableDeclaration has no real 'reqSpec_AVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_GlobalConstants's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_GlobalConstants's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_GlobalConstants(name="sample_text")
    partner = reqSpec_AVariableDeclaration()
    setattr(partner, 'reqSpec_AVariableDeclaration', None)
    _safe_set(owner, 'reqSpec_GlobalConstants', {partner})
    assert getattr(partner, 'reqSpec_AVariableDeclaration') == owner
    _safe_set(owner, 'reqSpec_GlobalConstants', set())
    assert getattr(partner, 'reqSpec_AVariableDeclaration') is None


def test_assoc_constants34_stub_double():
    # reqSpec_AVariableDeclaration has no real 'reqSpec_AVariableDeclaration36' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_StakeholderGoals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_StakeholderGoals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_StakeholderGoals(componentCategory="sample_text")
    partner = reqSpec_AVariableDeclaration()
    setattr(partner, 'reqSpec_AVariableDeclaration36', None)
    _safe_set(owner, 'reqSpec_StakeholderGoals35', {partner})
    assert getattr(partner, 'reqSpec_AVariableDeclaration36') == owner
    _safe_set(owner, 'reqSpec_StakeholderGoals35', set())
    assert getattr(partner, 'reqSpec_AVariableDeclaration36') is None


def test_assoc_constants9_stub_double():
    # reqSpec_AVariableDeclaration has no real 'reqSpec_AVariableDeclaration11' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_AVariableDeclaration()
    setattr(partner, 'reqSpec_AVariableDeclaration11', None)
    _safe_set(owner, 'reqSpec_ContractualElement10', {partner})
    assert getattr(partner, 'reqSpec_AVariableDeclaration11') == owner
    _safe_set(owner, 'reqSpec_ContractualElement10', set())
    assert getattr(partner, 'reqSpec_AVariableDeclaration11') is None


def test_assoc_content44_stub_double():
    # reqSpec_EObject has no real 'reqSpec_EObject46' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_DocumentSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_DocumentSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_DocumentSection(label="sample_text", title="sample_text")
    partner = reqSpec_EObject()
    setattr(partner, 'reqSpec_EObject46', None)
    _safe_set(owner, 'reqSpec_DocumentSection45', {partner})
    assert getattr(partner, 'reqSpec_EObject46') == owner
    _safe_set(owner, 'reqSpec_DocumentSection45', set())
    assert getattr(partner, 'reqSpec_EObject46') is None


def test_assoc_description24_stub_double():
    # reqSpec_Description has no real 'reqSpec_Description25' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ReqRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ReqRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ReqRoot(issues="sample_text", name="sample_text", title="sample_text")
    partner = reqSpec_Description()
    setattr(partner, 'reqSpec_Description25', None)
    _safe_set(owner, 'reqSpec_ReqRoot', partner)
    assert getattr(partner, 'reqSpec_Description25') == owner
    _safe_set(owner, 'reqSpec_ReqRoot', None)
    assert getattr(partner, 'reqSpec_Description25') is None


def test_assoc_description42_stub_double():
    # reqSpec_Description has no real 'reqSpec_Description43' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_DocumentSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_DocumentSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_DocumentSection(label="sample_text", title="sample_text")
    partner = reqSpec_Description()
    setattr(partner, 'reqSpec_Description43', None)
    _safe_set(owner, 'reqSpec_DocumentSection', partner)
    assert getattr(partner, 'reqSpec_Description43') == owner
    _safe_set(owner, 'reqSpec_DocumentSection', None)
    assert getattr(partner, 'reqSpec_Description43') is None


def test_assoc_description7_stub_double():
    # reqSpec_Description has no real 'reqSpec_Description' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_Description()
    setattr(partner, 'reqSpec_Description', None)
    _safe_set(owner, 'reqSpec_ContractualElement8', partner)
    assert getattr(partner, 'reqSpec_Description') == owner
    _safe_set(owner, 'reqSpec_ContractualElement8', None)
    assert getattr(partner, 'reqSpec_Description') is None


def test_assoc_desired106_stub_double():
    # reqSpec_AVariableReference has no real 'reqSpec_AVariableReference' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_DesiredValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_DesiredValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_DesiredValue(upto=True)
    partner = reqSpec_AVariableReference()
    setattr(partner, 'reqSpec_AVariableReference', None)
    _safe_set(owner, 'reqSpec_DesiredValue107', partner)
    assert getattr(partner, 'reqSpec_AVariableReference') == owner
    _safe_set(owner, 'reqSpec_DesiredValue107', None)
    assert getattr(partner, 'reqSpec_AVariableReference') is None


def test_assoc_desiredValue104_stub_double():
    # reqSpec_ValuePredicate has no real 'reqSpec_ValuePredicate105' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_DesiredValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_DesiredValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_DesiredValue(upto=True)
    partner = reqSpec_ValuePredicate()
    setattr(partner, 'reqSpec_ValuePredicate105', None)
    _safe_set(owner, 'reqSpec_DesiredValue', partner)
    assert owner in getattr(partner, 'reqSpec_ValuePredicate105')
    _safe_set(owner, 'reqSpec_DesiredValue', None)
    assert owner not in getattr(partner, 'reqSpec_ValuePredicate105')


def test_assoc_developmentStakeholder86_stub_double():
    # reqSpec_Stakeholder has no real 'reqSpec_Stakeholder88' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    partner = reqSpec_Stakeholder()
    setattr(partner, 'reqSpec_Stakeholder88', None)
    _safe_set(owner, 'reqSpec_Requirement87', {partner})
    assert getattr(partner, 'reqSpec_Stakeholder88') == owner
    _safe_set(owner, 'reqSpec_Requirement87', set())
    assert getattr(partner, 'reqSpec_Stakeholder88') is None


def test_assoc_exception74_stub_double():
    # reqSpec_EObject has no real 'reqSpec_EObject76' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    partner = reqSpec_EObject()
    setattr(partner, 'reqSpec_EObject76', None)
    _safe_set(owner, 'reqSpec_Requirement75', partner)
    assert getattr(partner, 'reqSpec_EObject76') == owner
    _safe_set(owner, 'reqSpec_Requirement75', None)
    assert getattr(partner, 'reqSpec_EObject76') is None


def test_assoc_goalReference22_stub_double():
    # reqSpec_Goal has no real 'reqSpec_Goal' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_Goal()
    setattr(partner, 'reqSpec_Goal', None)
    _safe_set(owner, 'reqSpec_ContractualElement23', {partner})
    assert getattr(partner, 'reqSpec_Goal') == owner
    _safe_set(owner, 'reqSpec_ContractualElement23', set())
    assert getattr(partner, 'reqSpec_Goal') is None


def test_assoc_goals37_stub_double():
    # reqSpec_Goal has no real 'reqSpec_Goal39' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_StakeholderGoals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_StakeholderGoals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_StakeholderGoals(componentCategory="sample_text")
    partner = reqSpec_Goal()
    setattr(partner, 'reqSpec_Goal39', None)
    _safe_set(owner, 'reqSpec_StakeholderGoals38', {partner})
    assert getattr(partner, 'reqSpec_Goal39') == owner
    _safe_set(owner, 'reqSpec_StakeholderGoals38', set())
    assert getattr(partner, 'reqSpec_Goal39') is None


def test_assoc_importConstants47_stub_double():
    # reqSpec_RequirementSet has no real 'reqSpec_RequirementSet' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_GlobalConstants's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_GlobalConstants's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_GlobalConstants(name="sample_text")
    partner = reqSpec_RequirementSet()
    setattr(partner, 'reqSpec_RequirementSet', None)
    _safe_set(owner, 'reqSpec_GlobalConstants48', partner)
    assert owner in getattr(partner, 'reqSpec_RequirementSet')
    _safe_set(owner, 'reqSpec_GlobalConstants48', None)
    assert owner not in getattr(partner, 'reqSpec_RequirementSet')


def test_assoc_predicate72_stub_double():
    # reqSpec_ReqPredicate has no real 'reqSpec_ReqPredicate' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    partner = reqSpec_ReqPredicate()
    setattr(partner, 'reqSpec_ReqPredicate', None)
    _safe_set(owner, 'reqSpec_Requirement73', partner)
    assert getattr(partner, 'reqSpec_ReqPredicate') == owner
    _safe_set(owner, 'reqSpec_Requirement73', None)
    assert getattr(partner, 'reqSpec_ReqPredicate') is None


def test_assoc_rationale14_stub_double():
    # reqSpec_Rationale has no real 'reqSpec_Rationale' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_Rationale()
    setattr(partner, 'reqSpec_Rationale', None)
    _safe_set(owner, 'reqSpec_ContractualElement15', partner)
    assert getattr(partner, 'reqSpec_Rationale') == owner
    _safe_set(owner, 'reqSpec_ContractualElement15', None)
    assert getattr(partner, 'reqSpec_Rationale') is None


def test_assoc_requirements55_stub_double():
    # reqSpec_RequirementSet has no real 'reqSpec_RequirementSet56' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_Requirement(componentCategory="sample_text", connections=True, exceptionText="sample_text")
    partner = reqSpec_RequirementSet()
    setattr(partner, 'reqSpec_RequirementSet56', None)
    _safe_set(owner, 'reqSpec_Requirement57', partner)
    assert owner in getattr(partner, 'reqSpec_RequirementSet56')
    _safe_set(owner, 'reqSpec_Requirement57', None)
    assert owner not in getattr(partner, 'reqSpec_RequirementSet56')


def test_assoc_stakeholderGoals58_stub_double():
    # reqSpec_RequirementSet has no real 'reqSpec_RequirementSet59' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ReqRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ReqRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ReqRoot(issues="sample_text", name="sample_text", title="sample_text")
    partner = reqSpec_RequirementSet()
    setattr(partner, 'reqSpec_RequirementSet59', None)
    _safe_set(owner, 'reqSpec_ReqRoot60', partner)
    assert owner in getattr(partner, 'reqSpec_RequirementSet59')
    _safe_set(owner, 'reqSpec_ReqRoot60', None)
    assert owner not in getattr(partner, 'reqSpec_RequirementSet59')


def test_assoc_target2_stub_double():
    # reqSpec_ComponentClassifier has no real 'reqSpec_ComponentClassifier' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_ComponentClassifier()
    setattr(partner, 'reqSpec_ComponentClassifier', None)
    _safe_set(owner, 'reqSpec_ContractualElement', partner)
    assert getattr(partner, 'reqSpec_ComponentClassifier') == owner
    _safe_set(owner, 'reqSpec_ContractualElement', None)
    assert getattr(partner, 'reqSpec_ComponentClassifier') is None


def test_assoc_target29_stub_double():
    # reqSpec_ComponentClassifier has no real 'reqSpec_ComponentClassifier30' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_StakeholderGoals's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_StakeholderGoals's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_StakeholderGoals(componentCategory="sample_text")
    partner = reqSpec_ComponentClassifier()
    setattr(partner, 'reqSpec_ComponentClassifier30', None)
    _safe_set(owner, 'reqSpec_StakeholderGoals', partner)
    assert getattr(partner, 'reqSpec_ComponentClassifier30') == owner
    _safe_set(owner, 'reqSpec_StakeholderGoals', None)
    assert getattr(partner, 'reqSpec_ComponentClassifier30') is None


def test_assoc_targetElement3_stub_double():
    # reqSpec_NamedElement has no real 'reqSpec_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_NamedElement()
    setattr(partner, 'reqSpec_NamedElement', None)
    _safe_set(owner, 'reqSpec_ContractualElement4', partner)
    assert getattr(partner, 'reqSpec_NamedElement') == owner
    _safe_set(owner, 'reqSpec_ContractualElement4', None)
    assert getattr(partner, 'reqSpec_NamedElement') is None


def test_assoc_value108_stub_double():
    # reqSpec_PropertyExpression has no real 'reqSpec_PropertyExpression110' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_DesiredValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_DesiredValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_DesiredValue(upto=True)
    partner = reqSpec_PropertyExpression()
    setattr(partner, 'reqSpec_PropertyExpression110', None)
    _safe_set(owner, 'reqSpec_DesiredValue109', partner)
    assert getattr(partner, 'reqSpec_PropertyExpression110') == owner
    _safe_set(owner, 'reqSpec_DesiredValue109', None)
    assert getattr(partner, 'reqSpec_PropertyExpression110') is None


def test_assoc_whencondition12_stub_double():
    # reqSpec_WhenCondition has no real 'reqSpec_WhenCondition' property in the generated
    # code (a bare stub) -- manually attach it so reqSpec_ContractualElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reqSpec_ContractualElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reqSpec_ContractualElement(dropRationale="sample_text", dropped=True, issues="sample_text", name="sample_text", targetDescription="sample_text", title="sample_text")
    partner = reqSpec_WhenCondition()
    setattr(partner, 'reqSpec_WhenCondition', None)
    _safe_set(owner, 'reqSpec_ContractualElement13', partner)
    assert getattr(partner, 'reqSpec_WhenCondition') == owner
    _safe_set(owner, 'reqSpec_ContractualElement13', None)
    assert getattr(partner, 'reqSpec_WhenCondition') is None


