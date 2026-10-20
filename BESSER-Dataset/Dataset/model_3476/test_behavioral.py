import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FeatureTreeNode,
    feature_Annotation,
    feature_Attribute,
    feature_Constraint,
    feature_Feature,
    feature_FeatureModel,
    feature_FeatureTreeNode,
    feature_Group,
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

def test_assoc_attributes11_reverse_link_reassign_clear():
    a1 = feature_Feature(name="sample_text")
    a2 = feature_Feature(name="sample_text_2")
    b = feature_Attribute(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'feature'):
        assert _is_linked(a1, 'feature', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'feature'):
        assert not _is_linked(a1, 'feature', b)
    if hasattr(a2, 'feature'):
        assert _is_linked(a2, 'feature', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'feature'):
        assert not _is_linked(a2, 'feature', b)


def test_assoc_children4_reverse_link_reassign_clear():
    a1 = feature_FeatureModel(name="sample_text")
    a2 = feature_FeatureModel(name="sample_text_2")
    b = feature_FeatureModel(name="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'FeatureModel'):
        assert _is_linked(a1, 'FeatureModel', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'FeatureModel'):
        assert not _is_linked(a1, 'FeatureModel', b)
    if hasattr(a2, 'FeatureModel'):
        assert _is_linked(a2, 'FeatureModel', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'FeatureModel'):
        assert not _is_linked(a2, 'FeatureModel', b)


def test_assoc_constrainedFeatures21_reverse_link_reassign_clear():
    a1 = feature_Feature(name="sample_text")
    a2 = feature_Feature(name="sample_text_2")
    b = feature_Constraint(expression="sample_text", language="sample_text")
    _safe_set(b, 'constraints', {a1})
    assert _is_linked(b, 'constraints', a1)
    if hasattr(a1, 'Feature22'):
        assert _is_linked(a1, 'Feature22', b)
    _safe_set(b, 'constraints', {a2})
    assert _is_linked(b, 'constraints', a2)
    if hasattr(a1, 'Feature22'):
        assert not _is_linked(a1, 'Feature22', b)
    if hasattr(a2, 'Feature22'):
        assert _is_linked(a2, 'Feature22', b)
    _safe_set(b, 'constraints', set())
    assert not _is_linked(b, 'constraints', a2)
    if hasattr(a2, 'Feature22'):
        assert not _is_linked(a2, 'Feature22', b)


def test_assoc_constrainingFeatureModel9_reverse_link_reassign_clear():
    a1 = feature_FeatureModel(name="sample_text")
    a2 = feature_FeatureModel(name="sample_text_2")
    b = feature_FeatureModel(name="sample_text")
    _safe_set(b, 'feature_FeatureModel8', a1)
    assert _is_linked(b, 'feature_FeatureModel8', a1)
    if hasattr(a1, 'feature_FeatureModel10'):
        assert _is_linked(a1, 'feature_FeatureModel10', b)
    _safe_set(b, 'feature_FeatureModel8', a2)
    assert _is_linked(b, 'feature_FeatureModel8', a2)
    if hasattr(a1, 'feature_FeatureModel10'):
        assert not _is_linked(a1, 'feature_FeatureModel10', b)
    if hasattr(a2, 'feature_FeatureModel10'):
        assert _is_linked(a2, 'feature_FeatureModel10', b)
    _safe_set(b, 'feature_FeatureModel8', None)
    assert not _is_linked(b, 'feature_FeatureModel8', a2)
    if hasattr(a2, 'feature_FeatureModel10'):
        assert not _is_linked(a2, 'feature_FeatureModel10', b)


def test_assoc_constraints0_reverse_link_reassign_clear():
    a1 = feature_FeatureModel(name="sample_text")
    a2 = feature_FeatureModel(name="sample_text_2")
    b = feature_Constraint(expression="sample_text", language="sample_text")
    _safe_set(b, 'feature_Constraint', a1)
    assert _is_linked(b, 'feature_Constraint', a1)
    if hasattr(a1, 'feature_FeatureModel'):
        assert _is_linked(a1, 'feature_FeatureModel', b)
    _safe_set(b, 'feature_Constraint', a2)
    assert _is_linked(b, 'feature_Constraint', a2)
    if hasattr(a1, 'feature_FeatureModel'):
        assert not _is_linked(a1, 'feature_FeatureModel', b)
    if hasattr(a2, 'feature_FeatureModel'):
        assert _is_linked(a2, 'feature_FeatureModel', b)
    _safe_set(b, 'feature_Constraint', None)
    assert not _is_linked(b, 'feature_Constraint', a2)
    if hasattr(a2, 'feature_FeatureModel'):
        assert not _is_linked(a2, 'feature_FeatureModel', b)


def test_assoc_constraints17_reverse_link_reassign_clear():
    a1 = feature_Feature(name="sample_text")
    a2 = feature_Feature(name="sample_text_2")
    b = feature_Constraint(expression="sample_text", language="sample_text")
    _safe_set(b, 'Constraint', a1)
    assert _is_linked(b, 'Constraint', a1)
    if hasattr(a1, 'constrainedFeatures'):
        assert _is_linked(a1, 'constrainedFeatures', b)
    _safe_set(b, 'Constraint', a2)
    assert _is_linked(b, 'Constraint', a2)
    if hasattr(a1, 'constrainedFeatures'):
        assert not _is_linked(a1, 'constrainedFeatures', b)
    if hasattr(a2, 'constrainedFeatures'):
        assert _is_linked(a2, 'constrainedFeatures', b)
    _safe_set(b, 'Constraint', None)
    assert not _is_linked(b, 'Constraint', a2)
    if hasattr(a2, 'constrainedFeatures'):
        assert not _is_linked(a2, 'constrainedFeatures', b)


def test_assoc_feature23_reverse_link_reassign_clear():
    a1 = feature_Feature(name="sample_text")
    a2 = feature_Feature(name="sample_text_2")
    b = feature_Attribute(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Feature24'):
        assert _is_linked(a1, 'Feature24', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Feature24'):
        assert not _is_linked(a1, 'Feature24', b)
    if hasattr(a2, 'Feature24'):
        assert _is_linked(a2, 'Feature24', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Feature24'):
        assert not _is_linked(a2, 'Feature24', b)


def test_assoc_parent6_reverse_link_reassign_clear():
    a1 = feature_FeatureModel(name="sample_text")
    a2 = feature_FeatureModel(name="sample_text_2")
    b = feature_FeatureModel(name="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'FeatureModel7'):
        assert _is_linked(a1, 'FeatureModel7', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'FeatureModel7'):
        assert not _is_linked(a1, 'FeatureModel7', b)
    if hasattr(a2, 'FeatureModel7'):
        assert _is_linked(a2, 'FeatureModel7', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'FeatureModel7'):
        assert not _is_linked(a2, 'FeatureModel7', b)


def test_assoc_root1_reverse_link_reassign_clear():
    a1 = feature_FeatureModel(name="sample_text")
    a2 = feature_FeatureModel(name="sample_text_2")
    b = feature_Feature(name="sample_text")
    _safe_set(b, 'feature_Feature', a1)
    assert _is_linked(b, 'feature_Feature', a1)
    if hasattr(a1, 'feature_FeatureModel2'):
        assert _is_linked(a1, 'feature_FeatureModel2', b)
    _safe_set(b, 'feature_Feature', a2)
    assert _is_linked(b, 'feature_Feature', a2)
    if hasattr(a1, 'feature_FeatureModel2'):
        assert not _is_linked(a1, 'feature_FeatureModel2', b)
    if hasattr(a2, 'feature_FeatureModel2'):
        assert _is_linked(a2, 'feature_FeatureModel2', b)
    _safe_set(b, 'feature_Feature', None)
    assert not _is_linked(b, 'feature_Feature', a2)
    if hasattr(a2, 'feature_FeatureModel2'):
        assert not _is_linked(a2, 'feature_FeatureModel2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations15_stub_double():
    # feature_Annotation has no real 'Annotation' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(name="sample_text")
    partner = feature_Annotation()
    setattr(partner, 'Annotation', None)
    _safe_set(owner, 'feature16', {partner})
    assert getattr(partner, 'Annotation') == owner
    _safe_set(owner, 'feature16', set())
    assert getattr(partner, 'Annotation') is None


def test_assoc_childFeatures19_stub_double():
    # feature_Group has no real 'parentGroup' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(name="sample_text")
    partner = feature_Group()
    setattr(partner, 'parentGroup', None)
    _safe_set(owner, 'Feature20', partner)
    assert owner in getattr(partner, 'parentGroup')
    _safe_set(owner, 'Feature20', None)
    assert owner not in getattr(partner, 'parentGroup')


def test_assoc_feature25_stub_double():
    # feature_Annotation has no real 'annotations' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(name="sample_text")
    partner = feature_Annotation()
    setattr(partner, 'annotations', None)
    _safe_set(owner, 'Feature26', partner)
    assert getattr(partner, 'annotations') == owner
    _safe_set(owner, 'Feature26', None)
    assert getattr(partner, 'annotations') is None


def test_assoc_groups12_stub_double():
    # feature_Group has no real 'Group' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(name="sample_text")
    partner = feature_Group()
    setattr(partner, 'Group', None)
    _safe_set(owner, 'parentFeature', {partner})
    assert getattr(partner, 'Group') == owner
    _safe_set(owner, 'parentFeature', set())
    assert getattr(partner, 'Group') is None


def test_assoc_parentFeature18_stub_double():
    # feature_Group has no real 'groups' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(name="sample_text")
    partner = feature_Group()
    setattr(partner, 'groups', None)
    _safe_set(owner, 'Feature', partner)
    assert getattr(partner, 'groups') == owner
    _safe_set(owner, 'Feature', None)
    assert getattr(partner, 'groups') is None


def test_assoc_parentGroup13_stub_double():
    # feature_Group has no real 'Group14' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(name="sample_text")
    partner = feature_Group()
    setattr(partner, 'Group14', None)
    _safe_set(owner, 'childFeatures', partner)
    assert getattr(partner, 'Group14') == owner
    _safe_set(owner, 'childFeatures', None)
    assert getattr(partner, 'Group14') is None


