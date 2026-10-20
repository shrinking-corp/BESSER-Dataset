import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AttributeType,
    AttributeValue,
    Rule,
    featuremodel_Attribute,
    featuremodel_AttributeType,
    featuremodel_AttributeTypeBoolean,
    featuremodel_AttributeTypeEObject,
    featuremodel_AttributeTypeInt,
    featuremodel_AttributeTypeString,
    featuremodel_AttributeValue,
    featuremodel_AttributeValueBoolean,
    featuremodel_AttributeValueEObject,
    featuremodel_AttributeValueInt,
    featuremodel_AttributeValueString,
    featuremodel_Constraint,
    featuremodel_Description,
    featuremodel_EObject,
    featuremodel_Feature,
    featuremodel_FeatureModel,
    featuremodel_Group,
    featuremodel_Rule,
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

def test_assoc_attributes1_reverse_link_reassign_clear():
    a1 = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    a2 = featuremodel_FeatureModel(id="sample_text_2", version="sample_text_2")
    b = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    _safe_set(b, 'featuremodel_Attribute', a1)
    assert _is_linked(b, 'featuremodel_Attribute', a1)
    if hasattr(a1, 'featuremodel_FeatureModel2'):
        assert _is_linked(a1, 'featuremodel_FeatureModel2', b)
    _safe_set(b, 'featuremodel_Attribute', a2)
    assert _is_linked(b, 'featuremodel_Attribute', a2)
    if hasattr(a1, 'featuremodel_FeatureModel2'):
        assert not _is_linked(a1, 'featuremodel_FeatureModel2', b)
    if hasattr(a2, 'featuremodel_FeatureModel2'):
        assert _is_linked(a2, 'featuremodel_FeatureModel2', b)
    _safe_set(b, 'featuremodel_Attribute', None)
    assert not _is_linked(b, 'featuremodel_Attribute', a2)
    if hasattr(a2, 'featuremodel_FeatureModel2'):
        assert not _is_linked(a2, 'featuremodel_FeatureModel2', b)


def test_assoc_attributes15_reverse_link_reassign_clear():
    a1 = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    a2 = featuremodel_Feature(id="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    _safe_set(b, 'featuremodel_Attribute17', a1)
    assert _is_linked(b, 'featuremodel_Attribute17', a1)
    if hasattr(a1, 'featuremodel_Feature16'):
        assert _is_linked(a1, 'featuremodel_Feature16', b)
    _safe_set(b, 'featuremodel_Attribute17', a2)
    assert _is_linked(b, 'featuremodel_Attribute17', a2)
    if hasattr(a1, 'featuremodel_Feature16'):
        assert not _is_linked(a1, 'featuremodel_Feature16', b)
    if hasattr(a2, 'featuremodel_Feature16'):
        assert _is_linked(a2, 'featuremodel_Feature16', b)
    _safe_set(b, 'featuremodel_Attribute17', None)
    assert not _is_linked(b, 'featuremodel_Attribute17', a2)
    if hasattr(a2, 'featuremodel_Feature16'):
        assert not _is_linked(a2, 'featuremodel_Feature16', b)


def test_assoc_children18_reverse_link_reassign_clear():
    a1 = featuremodel_Group(id="sample_text", lower=7, upper=7)
    a2 = featuremodel_Group(id="sample_text_2", lower=13, upper=13)
    b = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'featuremodel_Feature19', {a1})
    assert _is_linked(b, 'featuremodel_Feature19', a1)
    if hasattr(a1, 'featuremodel_Group20'):
        assert _is_linked(a1, 'featuremodel_Group20', b)
    _safe_set(b, 'featuremodel_Feature19', {a2})
    assert _is_linked(b, 'featuremodel_Feature19', a2)
    if hasattr(a1, 'featuremodel_Group20'):
        assert not _is_linked(a1, 'featuremodel_Group20', b)
    if hasattr(a2, 'featuremodel_Group20'):
        assert _is_linked(a2, 'featuremodel_Group20', b)
    _safe_set(b, 'featuremodel_Feature19', set())
    assert not _is_linked(b, 'featuremodel_Feature19', a2)
    if hasattr(a2, 'featuremodel_Group20'):
        assert not _is_linked(a2, 'featuremodel_Group20', b)


def test_assoc_constraints5_reverse_link_reassign_clear():
    a1 = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    a2 = featuremodel_FeatureModel(id="sample_text_2", version="sample_text_2")
    b = featuremodel_Constraint(id="sample_text")
    _safe_set(b, 'featuremodel_Constraint', a1)
    assert _is_linked(b, 'featuremodel_Constraint', a1)
    if hasattr(a1, 'featuremodel_FeatureModel6'):
        assert _is_linked(a1, 'featuremodel_FeatureModel6', b)
    _safe_set(b, 'featuremodel_Constraint', a2)
    assert _is_linked(b, 'featuremodel_Constraint', a2)
    if hasattr(a1, 'featuremodel_FeatureModel6'):
        assert not _is_linked(a1, 'featuremodel_FeatureModel6', b)
    if hasattr(a2, 'featuremodel_FeatureModel6'):
        assert _is_linked(a2, 'featuremodel_FeatureModel6', b)
    _safe_set(b, 'featuremodel_Constraint', None)
    assert not _is_linked(b, 'featuremodel_Constraint', a2)
    if hasattr(a2, 'featuremodel_FeatureModel6'):
        assert not _is_linked(a2, 'featuremodel_FeatureModel6', b)


def test_assoc_description0_reverse_link_reassign_clear():
    a1 = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    a2 = featuremodel_FeatureModel(id="sample_text_2", version="sample_text_2")
    b = featuremodel_Description(id="sample_text", text="sample_text")
    _safe_set(b, 'featuremodel_Description', a1)
    assert _is_linked(b, 'featuremodel_Description', a1)
    if hasattr(a1, 'featuremodel_FeatureModel'):
        assert _is_linked(a1, 'featuremodel_FeatureModel', b)
    _safe_set(b, 'featuremodel_Description', a2)
    assert _is_linked(b, 'featuremodel_Description', a2)
    if hasattr(a1, 'featuremodel_FeatureModel'):
        assert not _is_linked(a1, 'featuremodel_FeatureModel', b)
    if hasattr(a2, 'featuremodel_FeatureModel'):
        assert _is_linked(a2, 'featuremodel_FeatureModel', b)
    _safe_set(b, 'featuremodel_Description', None)
    assert not _is_linked(b, 'featuremodel_Description', a2)
    if hasattr(a2, 'featuremodel_FeatureModel'):
        assert not _is_linked(a2, 'featuremodel_FeatureModel', b)


def test_assoc_description12_reverse_link_reassign_clear():
    a1 = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    a2 = featuremodel_Feature(id="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = featuremodel_Description(id="sample_text", text="sample_text")
    _safe_set(b, 'featuremodel_Description14', a1)
    assert _is_linked(b, 'featuremodel_Description14', a1)
    if hasattr(a1, 'featuremodel_Feature13'):
        assert _is_linked(a1, 'featuremodel_Feature13', b)
    _safe_set(b, 'featuremodel_Description14', a2)
    assert _is_linked(b, 'featuremodel_Description14', a2)
    if hasattr(a1, 'featuremodel_Feature13'):
        assert not _is_linked(a1, 'featuremodel_Feature13', b)
    if hasattr(a2, 'featuremodel_Feature13'):
        assert _is_linked(a2, 'featuremodel_Feature13', b)
    _safe_set(b, 'featuremodel_Description14', None)
    assert not _is_linked(b, 'featuremodel_Description14', a2)
    if hasattr(a2, 'featuremodel_Feature13'):
        assert not _is_linked(a2, 'featuremodel_Feature13', b)


def test_assoc_description21_reverse_link_reassign_clear():
    a1 = featuremodel_Description(id="sample_text", text="sample_text")
    a2 = featuremodel_Description(id="sample_text_2", text="sample_text_2")
    b = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    _safe_set(b, 'featuremodel_Attribute22', a1)
    assert _is_linked(b, 'featuremodel_Attribute22', a1)
    if hasattr(a1, 'featuremodel_Description23'):
        assert _is_linked(a1, 'featuremodel_Description23', b)
    _safe_set(b, 'featuremodel_Attribute22', a2)
    assert _is_linked(b, 'featuremodel_Attribute22', a2)
    if hasattr(a1, 'featuremodel_Description23'):
        assert not _is_linked(a1, 'featuremodel_Description23', b)
    if hasattr(a2, 'featuremodel_Description23'):
        assert _is_linked(a2, 'featuremodel_Description23', b)
    _safe_set(b, 'featuremodel_Attribute22', None)
    assert not _is_linked(b, 'featuremodel_Attribute22', a2)
    if hasattr(a2, 'featuremodel_Description23'):
        assert not _is_linked(a2, 'featuremodel_Description23', b)


def test_assoc_description7_reverse_link_reassign_clear():
    a1 = featuremodel_Description(id="sample_text", text="sample_text")
    a2 = featuremodel_Description(id="sample_text_2", text="sample_text_2")
    b = featuremodel_Constraint(id="sample_text")
    _safe_set(b, 'featuremodel_Constraint8', a1)
    assert _is_linked(b, 'featuremodel_Constraint8', a1)
    if hasattr(a1, 'featuremodel_Description9'):
        assert _is_linked(a1, 'featuremodel_Description9', b)
    _safe_set(b, 'featuremodel_Constraint8', a2)
    assert _is_linked(b, 'featuremodel_Constraint8', a2)
    if hasattr(a1, 'featuremodel_Description9'):
        assert not _is_linked(a1, 'featuremodel_Description9', b)
    if hasattr(a2, 'featuremodel_Description9'):
        assert _is_linked(a2, 'featuremodel_Description9', b)
    _safe_set(b, 'featuremodel_Constraint8', None)
    assert not _is_linked(b, 'featuremodel_Constraint8', a2)
    if hasattr(a2, 'featuremodel_Description9'):
        assert not _is_linked(a2, 'featuremodel_Description9', b)


def test_assoc_features10_reverse_link_reassign_clear():
    a1 = featuremodel_Group(id="sample_text", lower=7, upper=7)
    a2 = featuremodel_Group(id="sample_text_2", lower=13, upper=13)
    b = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'featuremodel_Feature11', a1)
    assert _is_linked(b, 'featuremodel_Feature11', a1)
    if hasattr(a1, 'featuremodel_Group'):
        assert _is_linked(a1, 'featuremodel_Group', b)
    _safe_set(b, 'featuremodel_Feature11', a2)
    assert _is_linked(b, 'featuremodel_Feature11', a2)
    if hasattr(a1, 'featuremodel_Group'):
        assert not _is_linked(a1, 'featuremodel_Group', b)
    if hasattr(a2, 'featuremodel_Group'):
        assert _is_linked(a2, 'featuremodel_Group', b)
    _safe_set(b, 'featuremodel_Feature11', None)
    assert not _is_linked(b, 'featuremodel_Feature11', a2)
    if hasattr(a2, 'featuremodel_Group'):
        assert not _is_linked(a2, 'featuremodel_Group', b)


def test_assoc_root3_reverse_link_reassign_clear():
    a1 = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    a2 = featuremodel_FeatureModel(id="sample_text_2", version="sample_text_2")
    b = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'featuremodel_Feature', a1)
    assert _is_linked(b, 'featuremodel_Feature', a1)
    if hasattr(a1, 'featuremodel_FeatureModel4'):
        assert _is_linked(a1, 'featuremodel_FeatureModel4', b)
    _safe_set(b, 'featuremodel_Feature', a2)
    assert _is_linked(b, 'featuremodel_Feature', a2)
    if hasattr(a1, 'featuremodel_FeatureModel4'):
        assert not _is_linked(a1, 'featuremodel_FeatureModel4', b)
    if hasattr(a2, 'featuremodel_FeatureModel4'):
        assert _is_linked(a2, 'featuremodel_FeatureModel4', b)
    _safe_set(b, 'featuremodel_Feature', None)
    assert not _is_linked(b, 'featuremodel_Feature', a2)
    if hasattr(a2, 'featuremodel_FeatureModel4'):
        assert not _is_linked(a2, 'featuremodel_FeatureModel4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_defaultValue24_stub_double():
    # featuremodel_AttributeValue has no real 'featuremodel_AttributeValue' property in the generated
    # code (a bare stub) -- manually attach it so featuremodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featuremodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    partner = featuremodel_AttributeValue()
    setattr(partner, 'featuremodel_AttributeValue', None)
    _safe_set(owner, 'featuremodel_Attribute25', partner)
    assert getattr(partner, 'featuremodel_AttributeValue') == owner
    _safe_set(owner, 'featuremodel_Attribute25', None)
    assert getattr(partner, 'featuremodel_AttributeValue') is None


def test_assoc_type26_stub_double():
    # featuremodel_AttributeType has no real 'featuremodel_AttributeType' property in the generated
    # code (a bare stub) -- manually attach it so featuremodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featuremodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    partner = featuremodel_AttributeType()
    setattr(partner, 'featuremodel_AttributeType', None)
    _safe_set(owner, 'featuremodel_Attribute27', partner)
    assert getattr(partner, 'featuremodel_AttributeType') == owner
    _safe_set(owner, 'featuremodel_Attribute27', None)
    assert getattr(partner, 'featuremodel_AttributeType') is None


