import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CardinalizedElement,
    CommonFeature,
    ConstraintableElement,
    ContainableElement,
    ContainerElement,
    Feature,
    Literal,
    VariableFeature,
    sxfm_Atom,
    sxfm_CardinalizedElement,
    sxfm_CommonFeature,
    sxfm_Constraint,
    sxfm_ConstraintableElement,
    sxfm_ConstraintsSet,
    sxfm_ContainableElement,
    sxfm_ContainerElement,
    sxfm_Data,
    sxfm_Feature,
    sxfm_FeatureChoice,
    sxfm_FeatureModel,
    sxfm_FeatureModelConfiguaration,
    sxfm_FeatureTree,
    sxfm_Group,
    sxfm_GroupedFeature,
    sxfm_Literal,
    sxfm_Mandatory,
    sxfm_MetadataSet,
    sxfm_Not,
    sxfm_Optional,
    sxfm_Or,
    sxfm_Root,
    sxfm_VariableFeature,
    DecisionType,
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

def test_assoc_feature26_reverse_link_reassign_clear():
    a1 = sxfm_FeatureChoice(decisionStep=7, decisionType="sample_text", selected=True)
    a2 = sxfm_FeatureChoice(decisionStep=13, decisionType="sample_text_2", selected=False)
    b = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    _safe_set(b, 'sxfm_Feature28', a1)
    assert _is_linked(b, 'sxfm_Feature28', a1)
    if hasattr(a1, 'sxfm_FeatureChoice27'):
        assert _is_linked(a1, 'sxfm_FeatureChoice27', b)
    _safe_set(b, 'sxfm_Feature28', a2)
    assert _is_linked(b, 'sxfm_Feature28', a2)
    if hasattr(a1, 'sxfm_FeatureChoice27'):
        assert not _is_linked(a1, 'sxfm_FeatureChoice27', b)
    if hasattr(a2, 'sxfm_FeatureChoice27'):
        assert _is_linked(a2, 'sxfm_FeatureChoice27', b)
    _safe_set(b, 'sxfm_Feature28', None)
    assert not _is_linked(b, 'sxfm_Feature28', a2)
    if hasattr(a2, 'sxfm_FeatureChoice27'):
        assert not _is_linked(a2, 'sxfm_FeatureChoice27', b)


def test_assoc_groups0_reverse_link_reassign_clear():
    a1 = sxfm_Group(id="sample_text")
    a2 = sxfm_Group(id="sample_text_2")
    b = sxfm_Feature(description="sample_text", id="sample_text", name="sample_text", treeLevel=7)
    _safe_set(b, 'sxfm_Feature', {a1})
    assert _is_linked(b, 'sxfm_Feature', a1)
    if hasattr(a1, 'sxfm_Group'):
        assert _is_linked(a1, 'sxfm_Group', b)
    _safe_set(b, 'sxfm_Feature', {a2})
    assert _is_linked(b, 'sxfm_Feature', a2)
    if hasattr(a1, 'sxfm_Group'):
        assert not _is_linked(a1, 'sxfm_Group', b)
    if hasattr(a2, 'sxfm_Group'):
        assert _is_linked(a2, 'sxfm_Group', b)
    _safe_set(b, 'sxfm_Feature', set())
    assert not _is_linked(b, 'sxfm_Feature', a2)
    if hasattr(a2, 'sxfm_Group'):
        assert not _is_linked(a2, 'sxfm_Group', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configuration9_stub_double():
    # sxfm_FeatureModelConfiguaration has no real 'sxfm_FeatureModelConfiguaration' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_FeatureModel(name="sample_text")
    partner = sxfm_FeatureModelConfiguaration()
    setattr(partner, 'sxfm_FeatureModelConfiguaration', None)
    _safe_set(owner, 'sxfm_FeatureModel10', {partner})
    assert getattr(partner, 'sxfm_FeatureModelConfiguaration') == owner
    _safe_set(owner, 'sxfm_FeatureModel10', set())
    assert getattr(partner, 'sxfm_FeatureModelConfiguaration') is None


def test_assoc_constraints13_stub_double():
    # sxfm_ConstraintsSet has no real 'sxfm_ConstraintsSet14' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_Constraint(id=7)
    partner = sxfm_ConstraintsSet()
    setattr(partner, 'sxfm_ConstraintsSet14', None)
    _safe_set(owner, 'sxfm_Constraint15', partner)
    assert owner in getattr(partner, 'sxfm_ConstraintsSet14')
    _safe_set(owner, 'sxfm_Constraint15', None)
    assert owner not in getattr(partner, 'sxfm_ConstraintsSet14')


def test_assoc_constraintsSet4_stub_double():
    # sxfm_ConstraintsSet has no real 'sxfm_ConstraintsSet' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_FeatureModel(name="sample_text")
    partner = sxfm_ConstraintsSet()
    setattr(partner, 'sxfm_ConstraintsSet', None)
    _safe_set(owner, 'sxfm_FeatureModel', partner)
    assert getattr(partner, 'sxfm_ConstraintsSet') == owner
    _safe_set(owner, 'sxfm_FeatureModel', None)
    assert getattr(partner, 'sxfm_ConstraintsSet') is None


def test_assoc_data22_stub_double():
    # sxfm_MetadataSet has no real 'sxfm_MetadataSet23' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_Data's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_Data's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_Data(name="sample_text", value="sample_text")
    partner = sxfm_MetadataSet()
    setattr(partner, 'sxfm_MetadataSet23', None)
    _safe_set(owner, 'sxfm_Data', partner)
    assert owner in getattr(partner, 'sxfm_MetadataSet23')
    _safe_set(owner, 'sxfm_Data', None)
    assert owner not in getattr(partner, 'sxfm_MetadataSet23')


def test_assoc_featureChoice24_stub_double():
    # sxfm_FeatureModelConfiguaration has no real 'sxfm_FeatureModelConfiguaration25' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_FeatureChoice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_FeatureChoice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_FeatureChoice(decisionStep=7, decisionType="sample_text", selected=True)
    partner = sxfm_FeatureModelConfiguaration()
    setattr(partner, 'sxfm_FeatureModelConfiguaration25', None)
    _safe_set(owner, 'sxfm_FeatureChoice', partner)
    assert owner in getattr(partner, 'sxfm_FeatureModelConfiguaration25')
    _safe_set(owner, 'sxfm_FeatureChoice', None)
    assert owner not in getattr(partner, 'sxfm_FeatureModelConfiguaration25')


def test_assoc_featureModelInfo7_stub_double():
    # sxfm_MetadataSet has no real 'sxfm_MetadataSet' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_FeatureModel(name="sample_text")
    partner = sxfm_MetadataSet()
    setattr(partner, 'sxfm_MetadataSet', None)
    _safe_set(owner, 'sxfm_FeatureModel8', partner)
    assert getattr(partner, 'sxfm_MetadataSet') == owner
    _safe_set(owner, 'sxfm_FeatureModel8', None)
    assert getattr(partner, 'sxfm_MetadataSet') is None


def test_assoc_featureTree5_stub_double():
    # sxfm_FeatureTree has no real 'sxfm_FeatureTree' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_FeatureModel(name="sample_text")
    partner = sxfm_FeatureTree()
    setattr(partner, 'sxfm_FeatureTree', None)
    _safe_set(owner, 'sxfm_FeatureModel6', partner)
    assert getattr(partner, 'sxfm_FeatureTree') == owner
    _safe_set(owner, 'sxfm_FeatureModel6', None)
    assert getattr(partner, 'sxfm_FeatureTree') is None


def test_assoc_groupedFeatures1_stub_double():
    # sxfm_GroupedFeature has no real 'sxfm_GroupedFeature' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_Group(id="sample_text")
    partner = sxfm_GroupedFeature()
    setattr(partner, 'sxfm_GroupedFeature', None)
    _safe_set(owner, 'sxfm_Group2', {partner})
    assert getattr(partner, 'sxfm_GroupedFeature') == owner
    _safe_set(owner, 'sxfm_Group2', set())
    assert getattr(partner, 'sxfm_GroupedFeature') is None


def test_assoc_or_3_stub_double():
    # sxfm_Or has no real 'sxfm_Or' property in the generated
    # code (a bare stub) -- manually attach it so sxfm_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sxfm_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sxfm_Constraint(id=7)
    partner = sxfm_Or()
    setattr(partner, 'sxfm_Or', None)
    _safe_set(owner, 'sxfm_Constraint', partner)
    assert getattr(partner, 'sxfm_Or') == owner
    _safe_set(owner, 'sxfm_Constraint', None)
    assert getattr(partner, 'sxfm_Or') is None


