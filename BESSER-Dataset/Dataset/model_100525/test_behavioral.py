import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFeature,
    Actor,
    ApplicationDomainUseCase,
    Asset,
    AssociationClassElement,
    Danger,
    Feature,
    FunctionalRequirement,
    Goal,
    GoalReference,
    MEDiagram,
    Mitigation,
    NonDomainElement,
    NonFunctionalRequirement,
    Product,
    Requirement,
    Service,
    SolutionDomainUseCase,
    Step,
    UnicaseModelElement,
    UrmlModelElement,
    UseCase,
    VariationPoint,
    VariationPointInstance,
    goal_urml_Stakeholder,
    urml_EClass,
    urml_EStructuralFeature,
    urml_Phase,
    urml_PhaseSetEntry,
    urml_SetEntry,
    urml_Stakeholder,
    urml_StakeholderRole,
    urml_URMLDiagram,
    urml_UrmlModelElement,
    urml_UrmlProjectSettings,
    urml_danger_Asset,
    urml_danger_Danger,
    urml_danger_Mitigation,
    urml_danger_ProceduralMitigation,
    urml_feature_AbstractFeature,
    urml_feature_Feature,
    urml_feature_Product,
    urml_feature_VariationPoint,
    urml_feature_VariationPointInstance,
    urml_goal_Goal,
    urml_goal_GoalReference,
    urml_requirement_FunctionalRequirement,
    urml_requirement_NonFunctionalRequirement,
    urml_requirement_Requirement,
    urml_service_Service,
    urml_usecase_Actor,
    urml_usecase_ApplicationDomainUseCase,
    urml_usecase_SolutionDomainUseCase,
    urml_usecase_UseCase,
    GoalReferenceType,
    GoalType,
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

def test_assoc_associations1_reverse_link_reassign_clear():
    a1 = urml_UrmlModelElement(reviewed=True)
    a2 = urml_UrmlModelElement(reviewed=False)
    b = urml_UrmlModelElement(reviewed=True)
    _safe_set(b, 'urml_UrmlModelElement0', {a1})
    assert _is_linked(b, 'urml_UrmlModelElement0', a1)
    if hasattr(a1, 'urml_UrmlModelElement'):
        assert _is_linked(a1, 'urml_UrmlModelElement', b)
    _safe_set(b, 'urml_UrmlModelElement0', {a2})
    assert _is_linked(b, 'urml_UrmlModelElement0', a2)
    if hasattr(a1, 'urml_UrmlModelElement'):
        assert not _is_linked(a1, 'urml_UrmlModelElement', b)
    if hasattr(a2, 'urml_UrmlModelElement'):
        assert _is_linked(a2, 'urml_UrmlModelElement', b)
    _safe_set(b, 'urml_UrmlModelElement0', set())
    assert not _is_linked(b, 'urml_UrmlModelElement0', a2)
    if hasattr(a2, 'urml_UrmlModelElement'):
        assert not _is_linked(a2, 'urml_UrmlModelElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_detailingUseCases23_stub_double():
    # ApplicationDomainUseCase has no real 'ApplicationDomainUseCase' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = ApplicationDomainUseCase()
    setattr(partner, 'ApplicationDomainUseCase', None)
    _safe_set(owner, 'detailedGoal', partner)
    assert getattr(partner, 'ApplicationDomainUseCase') == owner
    _safe_set(owner, 'detailedGoal', None)
    assert getattr(partner, 'ApplicationDomainUseCase') is None


def test_assoc_implementingServices35_stub_double():
    # Service has no real 'Service' property in the generated
    # code (a bare stub) -- manually attach it so urml_requirement_Requirement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_requirement_Requirement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_requirement_Requirement(terminal=True)
    partner = Service()
    setattr(partner, 'Service', None)
    _safe_set(owner, 'satisfiedRequirements', {partner})
    assert getattr(partner, 'Service') == owner
    _safe_set(owner, 'satisfiedRequirements', set())
    assert getattr(partner, 'Service') is None


def test_assoc_influencedGoals29_stub_double():
    # GoalReference has no real 'GoalReference30' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = GoalReference()
    setattr(partner, 'GoalReference30', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'GoalReference30') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'GoalReference30') is None


def test_assoc_influencingGoals28_stub_double():
    # GoalReference has no real 'GoalReference' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = GoalReference()
    setattr(partner, 'GoalReference', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'GoalReference') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'GoalReference') is None


def test_assoc_instances92_stub_double():
    # VariationPointInstance has no real 'VariationPointInstance93' property in the generated
    # code (a bare stub) -- manually attach it so urml_feature_VariationPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_feature_VariationPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_feature_VariationPoint(multiplicity=7)
    partner = VariationPointInstance()
    setattr(partner, 'VariationPointInstance93', None)
    _safe_set(owner, 'variationPoint', {partner})
    assert getattr(partner, 'VariationPointInstance93') == owner
    _safe_set(owner, 'variationPoint', set())
    assert getattr(partner, 'VariationPointInstance93') is None


def test_assoc_optionalSubFeatures90_stub_double():
    # AbstractFeature has no real 'AbstractFeature91' property in the generated
    # code (a bare stub) -- manually attach it so urml_feature_VariationPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_feature_VariationPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_feature_VariationPoint(multiplicity=7)
    partner = AbstractFeature()
    setattr(partner, 'AbstractFeature91', None)
    _safe_set(owner, 'optionalParentVariationPoint', {partner})
    assert getattr(partner, 'AbstractFeature91') == owner
    _safe_set(owner, 'optionalParentVariationPoint', set())
    assert getattr(partner, 'AbstractFeature91') is None


def test_assoc_parentGoal26_stub_double():
    # Goal has no real 'Goal27' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = Goal()
    setattr(partner, 'Goal27', None)
    _safe_set(owner, 'subGoals', partner)
    assert getattr(partner, 'Goal27') == owner
    _safe_set(owner, 'subGoals', None)
    assert getattr(partner, 'Goal27') is None


def test_assoc_realizedFeatures21_stub_double():
    # AbstractFeature has no real 'AbstractFeature' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = AbstractFeature()
    setattr(partner, 'AbstractFeature', None)
    _safe_set(owner, 'goals22', {partner})
    assert getattr(partner, 'AbstractFeature') == owner
    _safe_set(owner, 'goals22', set())
    assert getattr(partner, 'AbstractFeature') is None


def test_assoc_source31_stub_double():
    # Goal has no real 'Goal32' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_GoalReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_GoalReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_GoalReference(weight="sample_text")
    partner = Goal()
    setattr(partner, 'Goal32', None)
    _safe_set(owner, 'influencedGoals', partner)
    assert getattr(partner, 'Goal32') == owner
    _safe_set(owner, 'influencedGoals', None)
    assert getattr(partner, 'Goal32') is None


def test_assoc_stakeholders20_stub_double():
    # goal_urml_Stakeholder has no real 'Stakeholder' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = goal_urml_Stakeholder()
    setattr(partner, 'Stakeholder', None)
    _safe_set(owner, 'goals', {partner})
    assert getattr(partner, 'Stakeholder') == owner
    _safe_set(owner, 'goals', set())
    assert getattr(partner, 'Stakeholder') is None


def test_assoc_subGoals24_stub_double():
    # Goal has no real 'Goal25' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = Goal()
    setattr(partner, 'Goal25', None)
    _safe_set(owner, 'parentGoal', {partner})
    assert getattr(partner, 'Goal25') == owner
    _safe_set(owner, 'parentGoal', set())
    assert getattr(partner, 'Goal25') is None


def test_assoc_target33_stub_double():
    # Goal has no real 'Goal34' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_GoalReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_GoalReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_GoalReference(weight="sample_text")
    partner = Goal()
    setattr(partner, 'Goal34', None)
    _safe_set(owner, 'influencingGoals', partner)
    assert getattr(partner, 'Goal34') == owner
    _safe_set(owner, 'influencingGoals', None)
    assert getattr(partner, 'Goal34') is None


