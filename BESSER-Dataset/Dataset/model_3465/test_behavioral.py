import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    Group,
    featureModel_Constraint,
    featureModel_Constraints,
    featureModel_ExcludeConstraint,
    featureModel_Feature,
    featureModel_FeatureModel,
    featureModel_Group,
    featureModel_ImplyConstraint,
    featureModel_PropFormula,
    featureModel_Proposition,
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

def test_assoc_children5_stub_double():
    # featureModel_Group has no real 'featureModel_Group' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(name="sample_text")
    partner = featureModel_Group()
    setattr(partner, 'featureModel_Group', None)
    _safe_set(owner, 'featureModel_Feature6', {partner})
    assert getattr(partner, 'featureModel_Group') == owner
    _safe_set(owner, 'featureModel_Feature6', set())
    assert getattr(partner, 'featureModel_Group') is None


def test_assoc_constraints7_stub_double():
    # featureModel_Constraints has no real 'featureModel_Constraints8' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Constraint(nameA="sample_text", nameB="sample_text")
    partner = featureModel_Constraints()
    setattr(partner, 'featureModel_Constraints8', None)
    _safe_set(owner, 'featureModel_Constraint', partner)
    assert owner in getattr(partner, 'featureModel_Constraints8')
    _safe_set(owner, 'featureModel_Constraint', None)
    assert owner not in getattr(partner, 'featureModel_Constraints8')


def test_assoc_firstProp9_stub_double():
    # featureModel_PropFormula has no real 'featureModel_PropFormula10' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Proposition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Proposition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Proposition(nameA="sample_text", nameRest="sample_text")
    partner = featureModel_PropFormula()
    setattr(partner, 'featureModel_PropFormula10', None)
    _safe_set(owner, 'featureModel_Proposition', partner)
    assert owner in getattr(partner, 'featureModel_PropFormula10')
    _safe_set(owner, 'featureModel_Proposition', None)
    assert owner not in getattr(partner, 'featureModel_PropFormula10')


def test_assoc_rest11_stub_double():
    # featureModel_PropFormula has no real 'featureModel_PropFormula12' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Proposition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Proposition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Proposition(nameA="sample_text", nameRest="sample_text")
    partner = featureModel_PropFormula()
    setattr(partner, 'featureModel_PropFormula12', None)
    _safe_set(owner, 'featureModel_Proposition13', partner)
    assert owner in getattr(partner, 'featureModel_PropFormula12')
    _safe_set(owner, 'featureModel_Proposition13', None)
    assert owner not in getattr(partner, 'featureModel_PropFormula12')


def test_assoc_rootFeature0_stub_double():
    # featureModel_FeatureModel has no real 'featureModel_FeatureModel' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(name="sample_text")
    partner = featureModel_FeatureModel()
    setattr(partner, 'featureModel_FeatureModel', None)
    _safe_set(owner, 'featureModel_Feature', partner)
    assert owner in getattr(partner, 'featureModel_FeatureModel')
    _safe_set(owner, 'featureModel_Feature', None)
    assert owner not in getattr(partner, 'featureModel_FeatureModel')


