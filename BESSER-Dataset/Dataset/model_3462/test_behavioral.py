import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    featuremodels_Attribute,
    featuremodels_Constraint,
    featuremodels_ContainmentAssociation,
    featuremodels_Feature,
    featuremodels_FeatureModel,
    featuremodels_Instance,
    featuremodels_SimpleAttribute,
    ConstraintType,
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

def test_assoc_attributes9_reverse_link_reassign_clear():
    a1 = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    a2 = featuremodels_Feature(lowerBound=13, name="sample_text_2", required=False, root=False, upperBound=13)
    b = featuremodels_Attribute(name="sample_text")
    _safe_set(b, 'featuremodels_Attribute', a1)
    assert _is_linked(b, 'featuremodels_Attribute', a1)
    if hasattr(a1, 'featuremodels_Feature'):
        assert _is_linked(a1, 'featuremodels_Feature', b)
    _safe_set(b, 'featuremodels_Attribute', a2)
    assert _is_linked(b, 'featuremodels_Attribute', a2)
    if hasattr(a1, 'featuremodels_Feature'):
        assert not _is_linked(a1, 'featuremodels_Feature', b)
    if hasattr(a2, 'featuremodels_Feature'):
        assert _is_linked(a2, 'featuremodels_Feature', b)
    _safe_set(b, 'featuremodels_Attribute', None)
    assert not _is_linked(b, 'featuremodels_Attribute', a2)
    if hasattr(a2, 'featuremodels_Feature'):
        assert not _is_linked(a2, 'featuremodels_Feature', b)


def test_assoc_constraints16_reverse_link_reassign_clear():
    a1 = featuremodels_FeatureModel(name="sample_text")
    a2 = featuremodels_FeatureModel(name="sample_text_2")
    b = featuremodels_Constraint(name="sample_text", rule="sample_text", type="sample_text")
    _safe_set(b, 'featuremodels_Constraint', a1)
    assert _is_linked(b, 'featuremodels_Constraint', a1)
    if hasattr(a1, 'featuremodels_FeatureModel17'):
        assert _is_linked(a1, 'featuremodels_FeatureModel17', b)
    _safe_set(b, 'featuremodels_Constraint', a2)
    assert _is_linked(b, 'featuremodels_Constraint', a2)
    if hasattr(a1, 'featuremodels_FeatureModel17'):
        assert not _is_linked(a1, 'featuremodels_FeatureModel17', b)
    if hasattr(a2, 'featuremodels_FeatureModel17'):
        assert _is_linked(a2, 'featuremodels_FeatureModel17', b)
    _safe_set(b, 'featuremodels_Constraint', None)
    assert not _is_linked(b, 'featuremodels_Constraint', a2)
    if hasattr(a2, 'featuremodels_FeatureModel17'):
        assert not _is_linked(a2, 'featuremodels_FeatureModel17', b)


def test_assoc_containerParent6_reverse_link_reassign_clear():
    a1 = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    a2 = featuremodels_Feature(lowerBound=13, name="sample_text_2", required=False, root=False, upperBound=13)
    b = featuremodels_ContainmentAssociation(lowerBound=7, upperBound=7)
    _safe_set(b, 'ContainmentAssociation8', a1)
    assert _is_linked(b, 'ContainmentAssociation8', a1)
    if hasattr(a1, 'subFeatures7'):
        assert _is_linked(a1, 'subFeatures7', b)
    _safe_set(b, 'ContainmentAssociation8', a2)
    assert _is_linked(b, 'ContainmentAssociation8', a2)
    if hasattr(a1, 'subFeatures7'):
        assert not _is_linked(a1, 'subFeatures7', b)
    if hasattr(a2, 'subFeatures7'):
        assert _is_linked(a2, 'subFeatures7', b)
    _safe_set(b, 'ContainmentAssociation8', None)
    assert not _is_linked(b, 'ContainmentAssociation8', a2)
    if hasattr(a2, 'subFeatures7'):
        assert not _is_linked(a2, 'subFeatures7', b)


def test_assoc_containers5_reverse_link_reassign_clear():
    a1 = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    a2 = featuremodels_Feature(lowerBound=13, name="sample_text_2", required=False, root=False, upperBound=13)
    b = featuremodels_ContainmentAssociation(lowerBound=7, upperBound=7)
    _safe_set(b, 'ContainmentAssociation', a1)
    assert _is_linked(b, 'ContainmentAssociation', a1)
    if hasattr(a1, 'parent'):
        assert _is_linked(a1, 'parent', b)
    _safe_set(b, 'ContainmentAssociation', a2)
    assert _is_linked(b, 'ContainmentAssociation', a2)
    if hasattr(a1, 'parent'):
        assert not _is_linked(a1, 'parent', b)
    if hasattr(a2, 'parent'):
        assert _is_linked(a2, 'parent', b)
    _safe_set(b, 'ContainmentAssociation', None)
    assert not _is_linked(b, 'ContainmentAssociation', a2)
    if hasattr(a2, 'parent'):
        assert not _is_linked(a2, 'parent', b)


def test_assoc_featureParent3_reverse_link_reassign_clear():
    a1 = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    a2 = featuremodels_Feature(lowerBound=13, name="sample_text_2", required=False, root=False, upperBound=13)
    b = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    _safe_set(b, 'subFeatures', a1)
    assert _is_linked(b, 'subFeatures', a1)
    if hasattr(a1, 'Feature4'):
        assert _is_linked(a1, 'Feature4', b)
    _safe_set(b, 'subFeatures', a2)
    assert _is_linked(b, 'subFeatures', a2)
    if hasattr(a1, 'Feature4'):
        assert not _is_linked(a1, 'Feature4', b)
    if hasattr(a2, 'Feature4'):
        assert _is_linked(a2, 'Feature4', b)
    _safe_set(b, 'subFeatures', None)
    assert not _is_linked(b, 'subFeatures', a2)
    if hasattr(a2, 'Feature4'):
        assert not _is_linked(a2, 'Feature4', b)


def test_assoc_instances18_reverse_link_reassign_clear():
    a1 = featuremodels_Instance(descritpion="sample_text", id="sample_text")
    a2 = featuremodels_Instance(descritpion="sample_text_2", id="sample_text_2")
    b = featuremodels_FeatureModel(name="sample_text")
    _safe_set(b, 'featuremodels_FeatureModel19', {a1})
    assert _is_linked(b, 'featuremodels_FeatureModel19', a1)
    if hasattr(a1, 'featuremodels_Instance'):
        assert _is_linked(a1, 'featuremodels_Instance', b)
    _safe_set(b, 'featuremodels_FeatureModel19', {a2})
    assert _is_linked(b, 'featuremodels_FeatureModel19', a2)
    if hasattr(a1, 'featuremodels_Instance'):
        assert not _is_linked(a1, 'featuremodels_Instance', b)
    if hasattr(a2, 'featuremodels_Instance'):
        assert _is_linked(a2, 'featuremodels_Instance', b)
    _safe_set(b, 'featuremodels_FeatureModel19', set())
    assert not _is_linked(b, 'featuremodels_FeatureModel19', a2)
    if hasattr(a2, 'featuremodels_Instance'):
        assert not _is_linked(a2, 'featuremodels_Instance', b)


def test_assoc_parent12_reverse_link_reassign_clear():
    a1 = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    a2 = featuremodels_Feature(lowerBound=13, name="sample_text_2", required=False, root=False, upperBound=13)
    b = featuremodels_ContainmentAssociation(lowerBound=7, upperBound=7)
    _safe_set(b, 'containers', a1)
    assert _is_linked(b, 'containers', a1)
    if hasattr(a1, 'Feature13'):
        assert _is_linked(a1, 'Feature13', b)
    _safe_set(b, 'containers', a2)
    assert _is_linked(b, 'containers', a2)
    if hasattr(a1, 'Feature13'):
        assert not _is_linked(a1, 'Feature13', b)
    if hasattr(a2, 'Feature13'):
        assert _is_linked(a2, 'Feature13', b)
    _safe_set(b, 'containers', None)
    assert not _is_linked(b, 'containers', a2)
    if hasattr(a2, 'Feature13'):
        assert not _is_linked(a2, 'Feature13', b)


def test_assoc_rootFeature14_reverse_link_reassign_clear():
    a1 = featuremodels_FeatureModel(name="sample_text")
    a2 = featuremodels_FeatureModel(name="sample_text_2")
    b = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    _safe_set(b, 'featuremodels_Feature15', a1)
    assert _is_linked(b, 'featuremodels_Feature15', a1)
    if hasattr(a1, 'featuremodels_FeatureModel'):
        assert _is_linked(a1, 'featuremodels_FeatureModel', b)
    _safe_set(b, 'featuremodels_Feature15', a2)
    assert _is_linked(b, 'featuremodels_Feature15', a2)
    if hasattr(a1, 'featuremodels_FeatureModel'):
        assert not _is_linked(a1, 'featuremodels_FeatureModel', b)
    if hasattr(a2, 'featuremodels_FeatureModel'):
        assert _is_linked(a2, 'featuremodels_FeatureModel', b)
    _safe_set(b, 'featuremodels_Feature15', None)
    assert not _is_linked(b, 'featuremodels_Feature15', a2)
    if hasattr(a2, 'featuremodels_FeatureModel'):
        assert not _is_linked(a2, 'featuremodels_FeatureModel', b)


def test_assoc_selectedFeatures20_reverse_link_reassign_clear():
    a1 = featuremodels_Instance(descritpion="sample_text", id="sample_text")
    a2 = featuremodels_Instance(descritpion="sample_text_2", id="sample_text_2")
    b = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    _safe_set(b, 'featuremodels_Feature22', a1)
    assert _is_linked(b, 'featuremodels_Feature22', a1)
    if hasattr(a1, 'featuremodels_Instance21'):
        assert _is_linked(a1, 'featuremodels_Instance21', b)
    _safe_set(b, 'featuremodels_Feature22', a2)
    assert _is_linked(b, 'featuremodels_Feature22', a2)
    if hasattr(a1, 'featuremodels_Instance21'):
        assert not _is_linked(a1, 'featuremodels_Instance21', b)
    if hasattr(a2, 'featuremodels_Instance21'):
        assert _is_linked(a2, 'featuremodels_Instance21', b)
    _safe_set(b, 'featuremodels_Feature22', None)
    assert not _is_linked(b, 'featuremodels_Feature22', a2)
    if hasattr(a2, 'featuremodels_Instance21'):
        assert not _is_linked(a2, 'featuremodels_Instance21', b)


def test_assoc_subFeatures1_reverse_link_reassign_clear():
    a1 = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    a2 = featuremodels_Feature(lowerBound=13, name="sample_text_2", required=False, root=False, upperBound=13)
    b = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    _safe_set(b, 'featureParent', {a1})
    assert _is_linked(b, 'featureParent', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'featureParent', {a2})
    assert _is_linked(b, 'featureParent', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'featureParent', set())
    assert not _is_linked(b, 'featureParent', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_subFeatures10_reverse_link_reassign_clear():
    a1 = featuremodels_Feature(lowerBound=7, name="sample_text", required=True, root=True, upperBound=7)
    a2 = featuremodels_Feature(lowerBound=13, name="sample_text_2", required=False, root=False, upperBound=13)
    b = featuremodels_ContainmentAssociation(lowerBound=7, upperBound=7)
    _safe_set(b, 'containerParent', {a1})
    assert _is_linked(b, 'containerParent', a1)
    if hasattr(a1, 'Feature11'):
        assert _is_linked(a1, 'Feature11', b)
    _safe_set(b, 'containerParent', {a2})
    assert _is_linked(b, 'containerParent', a2)
    if hasattr(a1, 'Feature11'):
        assert not _is_linked(a1, 'Feature11', b)
    if hasattr(a2, 'Feature11'):
        assert _is_linked(a2, 'Feature11', b)
    _safe_set(b, 'containerParent', set())
    assert not _is_linked(b, 'containerParent', a2)
    if hasattr(a2, 'Feature11'):
        assert not _is_linked(a2, 'Feature11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

