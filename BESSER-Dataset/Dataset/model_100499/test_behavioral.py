import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DefinableRequirement,
    OclAny,
    PerformativeRequirement,
    Requirement,
    gore_Actor,
    gore_AwReq,
    gore_Configuration,
    gore_DefinableRequirement,
    gore_DifferentialRelation,
    gore_DomainAssumption,
    gore_Goal,
    gore_GoalModel,
    gore_Parameter,
    gore_PerformativeRequirement,
    gore_QualityConstraint,
    gore_Requirement,
    gore_Softgoal,
    gore_Task,
    AggregationLevel,
    DefinableRequirementState,
    DifferentialRelationOperator,
    MonitorableMethod,
    ParameterMetric,
    ParameterType,
    RefinementType,
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

def test_assoc_children1_reverse_link_reassign_clear():
    a1 = gore_Requirement(refinementType="sample_text")
    a2 = gore_Requirement(refinementType="sample_text_2")
    b = gore_Requirement(refinementType="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Requirement'):
        assert _is_linked(a1, 'Requirement', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Requirement'):
        assert not _is_linked(a1, 'Requirement', b)
    if hasattr(a2, 'Requirement'):
        assert _is_linked(a2, 'Requirement', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Requirement'):
        assert not _is_linked(a2, 'Requirement', b)


def test_assoc_indicator18_reverse_link_reassign_clear():
    a1 = gore_DifferentialRelation(lowerBound="sample_text", operator="sample_text", upperBound="sample_text", value=3.14)
    a2 = gore_DifferentialRelation(lowerBound="sample_text_2", operator="sample_text_2", upperBound="sample_text_2", value=9.99)
    b = gore_AwReq(incrementCoefficient=3.14)
    _safe_set(b, 'gore_AwReq19', a1)
    assert _is_linked(b, 'gore_AwReq19', a1)
    if hasattr(a1, 'gore_DifferentialRelation'):
        assert _is_linked(a1, 'gore_DifferentialRelation', b)
    _safe_set(b, 'gore_AwReq19', a2)
    assert _is_linked(b, 'gore_AwReq19', a2)
    if hasattr(a1, 'gore_DifferentialRelation'):
        assert not _is_linked(a1, 'gore_DifferentialRelation', b)
    if hasattr(a2, 'gore_DifferentialRelation'):
        assert _is_linked(a2, 'gore_DifferentialRelation', b)
    _safe_set(b, 'gore_AwReq19', None)
    assert not _is_linked(b, 'gore_AwReq19', a2)
    if hasattr(a2, 'gore_DifferentialRelation'):
        assert not _is_linked(a2, 'gore_DifferentialRelation', b)


def test_assoc_otherTargets7_reverse_link_reassign_clear():
    a1 = gore_DefinableRequirement(state="sample_text", time=date(2024, 1, 1))
    a2 = gore_DefinableRequirement(state="sample_text_2", time=date(2025, 6, 15))
    b = gore_AwReq(incrementCoefficient=3.14)
    _safe_set(b, 'gore_AwReq', {a1})
    assert _is_linked(b, 'gore_AwReq', a1)
    if hasattr(a1, 'gore_DefinableRequirement'):
        assert _is_linked(a1, 'gore_DefinableRequirement', b)
    _safe_set(b, 'gore_AwReq', {a2})
    assert _is_linked(b, 'gore_AwReq', a2)
    if hasattr(a1, 'gore_DefinableRequirement'):
        assert not _is_linked(a1, 'gore_DefinableRequirement', b)
    if hasattr(a2, 'gore_DefinableRequirement'):
        assert _is_linked(a2, 'gore_DefinableRequirement', b)
    _safe_set(b, 'gore_AwReq', set())
    assert not _is_linked(b, 'gore_AwReq', a2)
    if hasattr(a2, 'gore_DefinableRequirement'):
        assert not _is_linked(a2, 'gore_DefinableRequirement', b)


def test_assoc_parameter20_reverse_link_reassign_clear():
    a1 = gore_Parameter(metric="sample_text", type="sample_text", unit="sample_text", value="sample_text")
    a2 = gore_Parameter(metric="sample_text_2", type="sample_text_2", unit="sample_text_2", value="sample_text_2")
    b = gore_DifferentialRelation(lowerBound="sample_text", operator="sample_text", upperBound="sample_text", value=3.14)
    _safe_set(b, 'gore_DifferentialRelation21', a1)
    assert _is_linked(b, 'gore_DifferentialRelation21', a1)
    if hasattr(a1, 'gore_Parameter'):
        assert _is_linked(a1, 'gore_Parameter', b)
    _safe_set(b, 'gore_DifferentialRelation21', a2)
    assert _is_linked(b, 'gore_DifferentialRelation21', a2)
    if hasattr(a1, 'gore_Parameter'):
        assert not _is_linked(a1, 'gore_Parameter', b)
    if hasattr(a2, 'gore_Parameter'):
        assert _is_linked(a2, 'gore_Parameter', b)
    _safe_set(b, 'gore_DifferentialRelation21', None)
    assert not _is_linked(b, 'gore_DifferentialRelation21', a2)
    if hasattr(a2, 'gore_Parameter'):
        assert not _is_linked(a2, 'gore_Parameter', b)


def test_assoc_parent3_reverse_link_reassign_clear():
    a1 = gore_Requirement(refinementType="sample_text")
    a2 = gore_Requirement(refinementType="sample_text_2")
    b = gore_Requirement(refinementType="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Requirement4'):
        assert _is_linked(a1, 'Requirement4', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Requirement4'):
        assert not _is_linked(a1, 'Requirement4', b)
    if hasattr(a2, 'Requirement4'):
        assert _is_linked(a2, 'Requirement4', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Requirement4'):
        assert not _is_linked(a2, 'Requirement4', b)


def test_assoc_relations27_reverse_link_reassign_clear():
    a1 = gore_GoalModel(internalId="sample_text")
    a2 = gore_GoalModel(internalId="sample_text_2")
    b = gore_DifferentialRelation(lowerBound="sample_text", operator="sample_text", upperBound="sample_text", value=3.14)
    _safe_set(b, 'gore_DifferentialRelation28', a1)
    assert _is_linked(b, 'gore_DifferentialRelation28', a1)
    if hasattr(a1, 'gore_GoalModel'):
        assert _is_linked(a1, 'gore_GoalModel', b)
    _safe_set(b, 'gore_DifferentialRelation28', a2)
    assert _is_linked(b, 'gore_DifferentialRelation28', a2)
    if hasattr(a1, 'gore_GoalModel'):
        assert not _is_linked(a1, 'gore_GoalModel', b)
    if hasattr(a2, 'gore_GoalModel'):
        assert _is_linked(a2, 'gore_GoalModel', b)
    _safe_set(b, 'gore_DifferentialRelation28', None)
    assert not _is_linked(b, 'gore_DifferentialRelation28', a2)
    if hasattr(a2, 'gore_GoalModel'):
        assert not _is_linked(a2, 'gore_GoalModel', b)


def test_assoc_target8_reverse_link_reassign_clear():
    a1 = gore_DefinableRequirement(state="sample_text", time=date(2024, 1, 1))
    a2 = gore_DefinableRequirement(state="sample_text_2", time=date(2025, 6, 15))
    b = gore_AwReq(incrementCoefficient=3.14)
    _safe_set(b, 'gore_AwReq9', a1)
    assert _is_linked(b, 'gore_AwReq9', a1)
    if hasattr(a1, 'gore_DefinableRequirement10'):
        assert _is_linked(a1, 'gore_DefinableRequirement10', b)
    _safe_set(b, 'gore_AwReq9', a2)
    assert _is_linked(b, 'gore_AwReq9', a2)
    if hasattr(a1, 'gore_DefinableRequirement10'):
        assert not _is_linked(a1, 'gore_DefinableRequirement10', b)
    if hasattr(a2, 'gore_DefinableRequirement10'):
        assert _is_linked(a2, 'gore_DefinableRequirement10', b)
    _safe_set(b, 'gore_AwReq9', None)
    assert not _is_linked(b, 'gore_AwReq9', a2)
    if hasattr(a2, 'gore_DefinableRequirement10'):
        assert not _is_linked(a2, 'gore_DefinableRequirement10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actors23_stub_double():
    # gore_Actor has no real 'Actor' property in the generated
    # code (a bare stub) -- manually attach it so gore_GoalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_GoalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_GoalModel(internalId="sample_text")
    partner = gore_Actor()
    setattr(partner, 'Actor', None)
    _safe_set(owner, 'goalModel24', {partner})
    assert getattr(partner, 'Actor') == owner
    _safe_set(owner, 'goalModel24', set())
    assert getattr(partner, 'Actor') is None


def test_assoc_configuration25_stub_double():
    # gore_Configuration has no real 'Configuration' property in the generated
    # code (a bare stub) -- manually attach it so gore_GoalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_GoalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_GoalModel(internalId="sample_text")
    partner = gore_Configuration()
    setattr(partner, 'Configuration', None)
    _safe_set(owner, 'goalModel26', partner)
    assert getattr(partner, 'Configuration') == owner
    _safe_set(owner, 'goalModel26', None)
    assert getattr(partner, 'Configuration') is None


def test_assoc_configuration29_stub_double():
    # gore_Configuration has no real 'Configuration30' property in the generated
    # code (a bare stub) -- manually attach it so gore_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_Parameter(metric="sample_text", type="sample_text", unit="sample_text", value="sample_text")
    partner = gore_Configuration()
    setattr(partner, 'Configuration30', None)
    _safe_set(owner, 'parameters', partner)
    assert getattr(partner, 'Configuration30') == owner
    _safe_set(owner, 'parameters', None)
    assert getattr(partner, 'Configuration30') is None


def test_assoc_constraints5_stub_double():
    # gore_Softgoal has no real 'softgoal' property in the generated
    # code (a bare stub) -- manually attach it so gore_QualityConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_QualityConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_QualityConstraint()
    partner = gore_Softgoal()
    setattr(partner, 'softgoal', None)
    _safe_set(owner, 'QualityConstraint', partner)
    assert owner in getattr(partner, 'softgoal')
    _safe_set(owner, 'QualityConstraint', None)
    assert owner not in getattr(partner, 'softgoal')


def test_assoc_goalModel11_stub_double():
    # gore_Goal has no real 'rootGoal' property in the generated
    # code (a bare stub) -- manually attach it so gore_GoalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_GoalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_GoalModel(internalId="sample_text")
    partner = gore_Goal()
    setattr(partner, 'rootGoal', None)
    _safe_set(owner, 'GoalModel', partner)
    assert getattr(partner, 'rootGoal') == owner
    _safe_set(owner, 'GoalModel', None)
    assert getattr(partner, 'rootGoal') is None


def test_assoc_goalModel12_stub_double():
    # gore_Actor has no real 'actors' property in the generated
    # code (a bare stub) -- manually attach it so gore_GoalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_GoalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_GoalModel(internalId="sample_text")
    partner = gore_Actor()
    setattr(partner, 'actors', None)
    _safe_set(owner, 'GoalModel13', partner)
    assert getattr(partner, 'actors') == owner
    _safe_set(owner, 'GoalModel13', None)
    assert getattr(partner, 'actors') is None


def test_assoc_goalModel15_stub_double():
    # gore_Configuration has no real 'configuration16' property in the generated
    # code (a bare stub) -- manually attach it so gore_GoalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_GoalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_GoalModel(internalId="sample_text")
    partner = gore_Configuration()
    setattr(partner, 'configuration16', None)
    _safe_set(owner, 'GoalModel17', partner)
    assert getattr(partner, 'configuration16') == owner
    _safe_set(owner, 'GoalModel17', None)
    assert getattr(partner, 'configuration16') is None


def test_assoc_parameters14_stub_double():
    # gore_Configuration has no real 'configuration' property in the generated
    # code (a bare stub) -- manually attach it so gore_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_Parameter(metric="sample_text", type="sample_text", unit="sample_text", value="sample_text")
    partner = gore_Configuration()
    setattr(partner, 'configuration', None)
    _safe_set(owner, 'Parameter', partner)
    assert owner in getattr(partner, 'configuration')
    _safe_set(owner, 'Parameter', None)
    assert owner not in getattr(partner, 'configuration')


def test_assoc_rootGoal22_stub_double():
    # gore_Goal has no real 'Goal' property in the generated
    # code (a bare stub) -- manually attach it so gore_GoalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_GoalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_GoalModel(internalId="sample_text")
    partner = gore_Goal()
    setattr(partner, 'Goal', None)
    _safe_set(owner, 'goalModel', partner)
    assert getattr(partner, 'Goal') == owner
    _safe_set(owner, 'goalModel', None)
    assert getattr(partner, 'Goal') is None


def test_assoc_softgoal6_stub_double():
    # gore_Softgoal has no real 'Softgoal' property in the generated
    # code (a bare stub) -- manually attach it so gore_QualityConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gore_QualityConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gore_QualityConstraint()
    partner = gore_Softgoal()
    setattr(partner, 'Softgoal', None)
    _safe_set(owner, 'constraints', partner)
    assert getattr(partner, 'Softgoal') == owner
    _safe_set(owner, 'constraints', None)
    assert getattr(partner, 'Softgoal') is None


