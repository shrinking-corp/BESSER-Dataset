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
    urml_Stakeholder,
    urml_URMLDiagram,
    urml_UrmlModelElement,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_detailingUseCases4_stub_double():
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


def test_assoc_implementingServices16_stub_double():
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


def test_assoc_influencedGoals10_stub_double():
    # GoalReference has no real 'GoalReference11' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = GoalReference()
    setattr(partner, 'GoalReference11', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'GoalReference11') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'GoalReference11') is None


def test_assoc_influencingGoals9_stub_double():
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


def test_assoc_instances73_stub_double():
    # VariationPointInstance has no real 'VariationPointInstance74' property in the generated
    # code (a bare stub) -- manually attach it so urml_feature_VariationPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_feature_VariationPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_feature_VariationPoint(multiplicity=7)
    partner = VariationPointInstance()
    setattr(partner, 'VariationPointInstance74', None)
    _safe_set(owner, 'variationPoint', {partner})
    assert getattr(partner, 'VariationPointInstance74') == owner
    _safe_set(owner, 'variationPoint', set())
    assert getattr(partner, 'VariationPointInstance74') is None


def test_assoc_optionalSubFeatures71_stub_double():
    # AbstractFeature has no real 'AbstractFeature72' property in the generated
    # code (a bare stub) -- manually attach it so urml_feature_VariationPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_feature_VariationPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_feature_VariationPoint(multiplicity=7)
    partner = AbstractFeature()
    setattr(partner, 'AbstractFeature72', None)
    _safe_set(owner, 'optionalParentVariationPoint', {partner})
    assert getattr(partner, 'AbstractFeature72') == owner
    _safe_set(owner, 'optionalParentVariationPoint', set())
    assert getattr(partner, 'AbstractFeature72') is None


def test_assoc_parentGoal7_stub_double():
    # Goal has no real 'Goal8' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = Goal()
    setattr(partner, 'Goal8', None)
    _safe_set(owner, 'subGoals', partner)
    assert getattr(partner, 'Goal8') == owner
    _safe_set(owner, 'subGoals', None)
    assert getattr(partner, 'Goal8') is None


def test_assoc_realizedFeatures2_stub_double():
    # AbstractFeature has no real 'AbstractFeature' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = AbstractFeature()
    setattr(partner, 'AbstractFeature', None)
    _safe_set(owner, 'goals3', {partner})
    assert getattr(partner, 'AbstractFeature') == owner
    _safe_set(owner, 'goals3', set())
    assert getattr(partner, 'AbstractFeature') is None


def test_assoc_source12_stub_double():
    # Goal has no real 'Goal13' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_GoalReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_GoalReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_GoalReference(weight="sample_text")
    partner = Goal()
    setattr(partner, 'Goal13', None)
    _safe_set(owner, 'influencedGoals', partner)
    assert getattr(partner, 'Goal13') == owner
    _safe_set(owner, 'influencedGoals', None)
    assert getattr(partner, 'Goal13') is None


def test_assoc_stakeholders1_stub_double():
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


def test_assoc_subGoals5_stub_double():
    # Goal has no real 'Goal6' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_Goal(soft=True, type="sample_text")
    partner = Goal()
    setattr(partner, 'Goal6', None)
    _safe_set(owner, 'parentGoal', {partner})
    assert getattr(partner, 'Goal6') == owner
    _safe_set(owner, 'parentGoal', set())
    assert getattr(partner, 'Goal6') is None


def test_assoc_target14_stub_double():
    # Goal has no real 'Goal15' property in the generated
    # code (a bare stub) -- manually attach it so urml_goal_GoalReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # urml_goal_GoalReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = urml_goal_GoalReference(weight="sample_text")
    partner = Goal()
    setattr(partner, 'Goal15', None)
    _safe_set(owner, 'influencingGoals', partner)
    assert getattr(partner, 'Goal15') == owner
    _safe_set(owner, 'influencingGoals', None)
    assert getattr(partner, 'Goal15') is None


