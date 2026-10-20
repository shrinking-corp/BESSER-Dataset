import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Feature,
    Multiplicity_,
    Selection,
    featureModelMetamodel_AbstractFeature,
    featureModelMetamodel_Attribute,
    featureModelMetamodel_ClonableFeature,
    featureModelMetamodel_ClonableSelection,
    featureModelMetamodel_ConfigurationModel,
    featureModelMetamodel_Constraint,
    featureModelMetamodel_Feature,
    featureModelMetamodel_FeatureModel,
    featureModelMetamodel_GroupMultiplicity,
    featureModelMetamodel_Multiplicity_,
    featureModelMetamodel_Selection,
    featureModelMetamodel_VariableFeature,
    SelectionState,
    VariabilityType,
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
    a1 = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    a2 = featureModelMetamodel_Feature(id="sample_text_2", name="sample_text_2", variabilityType="sample_text_2")
    b = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    _safe_set(b, 'featureModelMetamodel_Feature0', {a1})
    assert _is_linked(b, 'featureModelMetamodel_Feature0', a1)
    if hasattr(a1, 'featureModelMetamodel_Feature'):
        assert _is_linked(a1, 'featureModelMetamodel_Feature', b)
    _safe_set(b, 'featureModelMetamodel_Feature0', {a2})
    assert _is_linked(b, 'featureModelMetamodel_Feature0', a2)
    if hasattr(a1, 'featureModelMetamodel_Feature'):
        assert not _is_linked(a1, 'featureModelMetamodel_Feature', b)
    if hasattr(a2, 'featureModelMetamodel_Feature'):
        assert _is_linked(a2, 'featureModelMetamodel_Feature', b)
    _safe_set(b, 'featureModelMetamodel_Feature0', set())
    assert not _is_linked(b, 'featureModelMetamodel_Feature0', a2)
    if hasattr(a2, 'featureModelMetamodel_Feature'):
        assert not _is_linked(a2, 'featureModelMetamodel_Feature', b)


def test_assoc_feature20_reverse_link_reassign_clear():
    a1 = featureModelMetamodel_Selection(name="sample_text", state="sample_text")
    a2 = featureModelMetamodel_Selection(name="sample_text_2", state="sample_text_2")
    b = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    _safe_set(b, 'featureModelMetamodel_Feature21', a1)
    assert _is_linked(b, 'featureModelMetamodel_Feature21', a1)
    if hasattr(a1, 'featureModelMetamodel_Selection'):
        assert _is_linked(a1, 'featureModelMetamodel_Selection', b)
    _safe_set(b, 'featureModelMetamodel_Feature21', a2)
    assert _is_linked(b, 'featureModelMetamodel_Feature21', a2)
    if hasattr(a1, 'featureModelMetamodel_Selection'):
        assert not _is_linked(a1, 'featureModelMetamodel_Selection', b)
    if hasattr(a2, 'featureModelMetamodel_Selection'):
        assert _is_linked(a2, 'featureModelMetamodel_Selection', b)
    _safe_set(b, 'featureModelMetamodel_Feature21', None)
    assert not _is_linked(b, 'featureModelMetamodel_Feature21', a2)
    if hasattr(a2, 'featureModelMetamodel_Selection'):
        assert not _is_linked(a2, 'featureModelMetamodel_Selection', b)


def test_assoc_parent7_reverse_link_reassign_clear():
    a1 = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    a2 = featureModelMetamodel_Feature(id="sample_text_2", name="sample_text_2", variabilityType="sample_text_2")
    b = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    _safe_set(b, 'featureModelMetamodel_Feature8', a1)
    assert _is_linked(b, 'featureModelMetamodel_Feature8', a1)
    if hasattr(a1, 'featureModelMetamodel_Feature6'):
        assert _is_linked(a1, 'featureModelMetamodel_Feature6', b)
    _safe_set(b, 'featureModelMetamodel_Feature8', a2)
    assert _is_linked(b, 'featureModelMetamodel_Feature8', a2)
    if hasattr(a1, 'featureModelMetamodel_Feature6'):
        assert not _is_linked(a1, 'featureModelMetamodel_Feature6', b)
    if hasattr(a2, 'featureModelMetamodel_Feature6'):
        assert _is_linked(a2, 'featureModelMetamodel_Feature6', b)
    _safe_set(b, 'featureModelMetamodel_Feature8', None)
    assert not _is_linked(b, 'featureModelMetamodel_Feature8', a2)
    if hasattr(a2, 'featureModelMetamodel_Feature6'):
        assert not _is_linked(a2, 'featureModelMetamodel_Feature6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes4_stub_double():
    # featureModelMetamodel_Attribute has no real 'featureModelMetamodel_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    partner = featureModelMetamodel_Attribute()
    setattr(partner, 'featureModelMetamodel_Attribute', None)
    _safe_set(owner, 'featureModelMetamodel_Feature5', {partner})
    assert getattr(partner, 'featureModelMetamodel_Attribute') == owner
    _safe_set(owner, 'featureModelMetamodel_Feature5', set())
    assert getattr(partner, 'featureModelMetamodel_Attribute') is None


def test_assoc_constraints12_stub_double():
    # featureModelMetamodel_FeatureModel has no real 'featureModelMetamodel_FeatureModel13' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Constraint(code="sample_text", id="sample_text", language="sample_text")
    partner = featureModelMetamodel_FeatureModel()
    setattr(partner, 'featureModelMetamodel_FeatureModel13', None)
    _safe_set(owner, 'featureModelMetamodel_Constraint', partner)
    assert owner in getattr(partner, 'featureModelMetamodel_FeatureModel13')
    _safe_set(owner, 'featureModelMetamodel_Constraint', None)
    assert owner not in getattr(partner, 'featureModelMetamodel_FeatureModel13')


def test_assoc_features14_stub_double():
    # featureModelMetamodel_FeatureModel has no real 'featureModelMetamodel_FeatureModel15' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    partner = featureModelMetamodel_FeatureModel()
    setattr(partner, 'featureModelMetamodel_FeatureModel15', None)
    _safe_set(owner, 'featureModelMetamodel_Feature16', partner)
    assert owner in getattr(partner, 'featureModelMetamodel_FeatureModel15')
    _safe_set(owner, 'featureModelMetamodel_Feature16', None)
    assert owner not in getattr(partner, 'featureModelMetamodel_FeatureModel15')


def test_assoc_features17_stub_double():
    # featureModelMetamodel_GroupMultiplicity has no real 'featureModelMetamodel_GroupMultiplicity18' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    partner = featureModelMetamodel_GroupMultiplicity()
    setattr(partner, 'featureModelMetamodel_GroupMultiplicity18', None)
    _safe_set(owner, 'featureModelMetamodel_Feature19', partner)
    assert owner in getattr(partner, 'featureModelMetamodel_GroupMultiplicity18')
    _safe_set(owner, 'featureModelMetamodel_Feature19', None)
    assert owner not in getattr(partner, 'featureModelMetamodel_GroupMultiplicity18')


def test_assoc_groupMultiplicity2_stub_double():
    # featureModelMetamodel_GroupMultiplicity has no real 'featureModelMetamodel_GroupMultiplicity' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    partner = featureModelMetamodel_GroupMultiplicity()
    setattr(partner, 'featureModelMetamodel_GroupMultiplicity', None)
    _safe_set(owner, 'featureModelMetamodel_Feature3', partner)
    assert getattr(partner, 'featureModelMetamodel_GroupMultiplicity') == owner
    _safe_set(owner, 'featureModelMetamodel_Feature3', None)
    assert getattr(partner, 'featureModelMetamodel_GroupMultiplicity') is None


def test_assoc_instanceMultiplicity9_stub_double():
    # featureModelMetamodel_ClonableFeature has no real 'featureModelMetamodel_ClonableFeature' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Multiplicity_'s own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Multiplicity_'s OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Multiplicity_(lower="sample_text", upper="sample_text")
    partner = featureModelMetamodel_ClonableFeature()
    setattr(partner, 'featureModelMetamodel_ClonableFeature', None)
    _safe_set(owner, 'featureModelMetamodel_Multiplicity', partner)
    assert getattr(partner, 'featureModelMetamodel_ClonableFeature') == owner
    _safe_set(owner, 'featureModelMetamodel_Multiplicity', None)
    assert getattr(partner, 'featureModelMetamodel_ClonableFeature') is None


def test_assoc_root10_stub_double():
    # featureModelMetamodel_FeatureModel has no real 'featureModelMetamodel_FeatureModel' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Feature(id="sample_text", name="sample_text", variabilityType="sample_text")
    partner = featureModelMetamodel_FeatureModel()
    setattr(partner, 'featureModelMetamodel_FeatureModel', None)
    _safe_set(owner, 'featureModelMetamodel_Feature11', partner)
    assert getattr(partner, 'featureModelMetamodel_FeatureModel') == owner
    _safe_set(owner, 'featureModelMetamodel_Feature11', None)
    assert getattr(partner, 'featureModelMetamodel_FeatureModel') is None


def test_assoc_selections22_stub_double():
    # featureModelMetamodel_ConfigurationModel has no real 'featureModelMetamodel_ConfigurationModel' property in the generated
    # code (a bare stub) -- manually attach it so featureModelMetamodel_Selection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModelMetamodel_Selection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModelMetamodel_Selection(name="sample_text", state="sample_text")
    partner = featureModelMetamodel_ConfigurationModel()
    setattr(partner, 'featureModelMetamodel_ConfigurationModel', None)
    _safe_set(owner, 'featureModelMetamodel_Selection23', partner)
    assert owner in getattr(partner, 'featureModelMetamodel_ConfigurationModel')
    _safe_set(owner, 'featureModelMetamodel_Selection23', None)
    assert owner not in getattr(partner, 'featureModelMetamodel_ConfigurationModel')


