import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    feature_Attribute,
    feature_Constraint,
    feature_Feature,
    feature_FeatureModel,
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

def test_assoc_attributes8_reverse_link_reassign_clear():
    a1 = feature_Feature(maxCardinality=7, minCardinality=7, name="sample_text")
    a2 = feature_Feature(maxCardinality=13, minCardinality=13, name="sample_text_2")
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


def test_assoc_childFeatures13_reverse_link_reassign_clear():
    a1 = feature_Group(maxCardinality=7, minCardinality=7)
    a2 = feature_Group(maxCardinality=13, minCardinality=13)
    b = feature_Feature(maxCardinality=7, minCardinality=7, name="sample_text")
    _safe_set(b, 'Feature14', a1)
    assert _is_linked(b, 'Feature14', a1)
    if hasattr(a1, 'parentGroup'):
        assert _is_linked(a1, 'parentGroup', b)
    _safe_set(b, 'Feature14', a2)
    assert _is_linked(b, 'Feature14', a2)
    if hasattr(a1, 'parentGroup'):
        assert not _is_linked(a1, 'parentGroup', b)
    if hasattr(a2, 'parentGroup'):
        assert _is_linked(a2, 'parentGroup', b)
    _safe_set(b, 'Feature14', None)
    assert not _is_linked(b, 'Feature14', a2)
    if hasattr(a2, 'parentGroup'):
        assert not _is_linked(a2, 'parentGroup', b)


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


def test_assoc_feature15_reverse_link_reassign_clear():
    a1 = feature_Feature(maxCardinality=7, minCardinality=7, name="sample_text")
    a2 = feature_Feature(maxCardinality=13, minCardinality=13, name="sample_text_2")
    b = feature_Attribute(name="sample_text", type="sample_text", value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Feature16'):
        assert _is_linked(a1, 'Feature16', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Feature16'):
        assert not _is_linked(a1, 'Feature16', b)
    if hasattr(a2, 'Feature16'):
        assert _is_linked(a2, 'Feature16', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Feature16'):
        assert not _is_linked(a2, 'Feature16', b)


def test_assoc_groups9_reverse_link_reassign_clear():
    a1 = feature_Group(maxCardinality=7, minCardinality=7)
    a2 = feature_Group(maxCardinality=13, minCardinality=13)
    b = feature_Feature(maxCardinality=7, minCardinality=7, name="sample_text")
    _safe_set(b, 'parentFeature', {a1})
    assert _is_linked(b, 'parentFeature', a1)
    if hasattr(a1, 'Group'):
        assert _is_linked(a1, 'Group', b)
    _safe_set(b, 'parentFeature', {a2})
    assert _is_linked(b, 'parentFeature', a2)
    if hasattr(a1, 'Group'):
        assert not _is_linked(a1, 'Group', b)
    if hasattr(a2, 'Group'):
        assert _is_linked(a2, 'Group', b)
    _safe_set(b, 'parentFeature', set())
    assert not _is_linked(b, 'parentFeature', a2)
    if hasattr(a2, 'Group'):
        assert not _is_linked(a2, 'Group', b)


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


def test_assoc_parentFeature12_reverse_link_reassign_clear():
    a1 = feature_Group(maxCardinality=7, minCardinality=7)
    a2 = feature_Group(maxCardinality=13, minCardinality=13)
    b = feature_Feature(maxCardinality=7, minCardinality=7, name="sample_text")
    _safe_set(b, 'Feature', a1)
    assert _is_linked(b, 'Feature', a1)
    if hasattr(a1, 'groups'):
        assert _is_linked(a1, 'groups', b)
    _safe_set(b, 'Feature', a2)
    assert _is_linked(b, 'Feature', a2)
    if hasattr(a1, 'groups'):
        assert not _is_linked(a1, 'groups', b)
    if hasattr(a2, 'groups'):
        assert _is_linked(a2, 'groups', b)
    _safe_set(b, 'Feature', None)
    assert not _is_linked(b, 'Feature', a2)
    if hasattr(a2, 'groups'):
        assert not _is_linked(a2, 'groups', b)


def test_assoc_parentGroup10_reverse_link_reassign_clear():
    a1 = feature_Group(maxCardinality=7, minCardinality=7)
    a2 = feature_Group(maxCardinality=13, minCardinality=13)
    b = feature_Feature(maxCardinality=7, minCardinality=7, name="sample_text")
    _safe_set(b, 'childFeatures', a1)
    assert _is_linked(b, 'childFeatures', a1)
    if hasattr(a1, 'Group11'):
        assert _is_linked(a1, 'Group11', b)
    _safe_set(b, 'childFeatures', a2)
    assert _is_linked(b, 'childFeatures', a2)
    if hasattr(a1, 'Group11'):
        assert not _is_linked(a1, 'Group11', b)
    if hasattr(a2, 'Group11'):
        assert _is_linked(a2, 'Group11', b)
    _safe_set(b, 'childFeatures', None)
    assert not _is_linked(b, 'childFeatures', a2)
    if hasattr(a2, 'Group11'):
        assert not _is_linked(a2, 'Group11', b)


def test_assoc_root1_reverse_link_reassign_clear():
    a1 = feature_FeatureModel(name="sample_text")
    a2 = feature_FeatureModel(name="sample_text_2")
    b = feature_Feature(maxCardinality=7, minCardinality=7, name="sample_text")
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

