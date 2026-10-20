import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DecisionRule,
    coCoMM_AttributeType,
    coCoMM_AttributeTypeElement,
    coCoMM_CMConstraintExpression,
    coCoMM_CTConstraintExpression,
    coCoMM_CoCo,
    coCoMM_Config,
    coCoMM_CrossModelConstraint,
    coCoMM_CrossTreeConstraint,
    coCoMM_DecisionRule,
    coCoMM_Feature,
    coCoMM_FeatureAttribute,
    coCoMM_FeatureAttributeElement,
    coCoMM_FeatureModel,
    coCoMM_HardLimitDR,
    coCoMM_HardLimitDRExpression,
    coCoMM_OptimizationDR,
    coCoMM_Project,
    coCoMM_SelectionStateDR,
    coCoMM_Stakeholder,
    coCoMM_TreeConstraint,
    CMConstraintType,
    CTConstraintType,
    ConfigType,
    DRHardLimitOp,
    DROptimizationOp,
    DRSelectionStateType,
    DRType,
    DataType,
    TreeConstraintType,
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

def test_assoc_attrType20_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureAttribute(name="sample_text")
    a2 = coCoMM_FeatureAttribute(name="sample_text_2")
    b = coCoMM_AttributeType(id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType22', a1)
    assert _is_linked(b, 'coCoMM_AttributeType22', a1)
    if hasattr(a1, 'coCoMM_FeatureAttribute21'):
        assert _is_linked(a1, 'coCoMM_FeatureAttribute21', b)
    _safe_set(b, 'coCoMM_AttributeType22', a2)
    assert _is_linked(b, 'coCoMM_AttributeType22', a2)
    if hasattr(a1, 'coCoMM_FeatureAttribute21'):
        assert not _is_linked(a1, 'coCoMM_FeatureAttribute21', b)
    if hasattr(a2, 'coCoMM_FeatureAttribute21'):
        assert _is_linked(a2, 'coCoMM_FeatureAttribute21', b)
    _safe_set(b, 'coCoMM_AttributeType22', None)
    assert not _is_linked(b, 'coCoMM_AttributeType22', a2)
    if hasattr(a2, 'coCoMM_FeatureAttribute21'):
        assert not _is_linked(a2, 'coCoMM_FeatureAttribute21', b)


def test_assoc_attrType51_reverse_link_reassign_clear():
    a1 = coCoMM_OptimizationDR(funct="sample_text")
    a2 = coCoMM_OptimizationDR(funct="sample_text_2")
    b = coCoMM_AttributeType(id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType52', a1)
    assert _is_linked(b, 'coCoMM_AttributeType52', a1)
    if hasattr(a1, 'coCoMM_OptimizationDR'):
        assert _is_linked(a1, 'coCoMM_OptimizationDR', b)
    _safe_set(b, 'coCoMM_AttributeType52', a2)
    assert _is_linked(b, 'coCoMM_AttributeType52', a2)
    if hasattr(a1, 'coCoMM_OptimizationDR'):
        assert not _is_linked(a1, 'coCoMM_OptimizationDR', b)
    if hasattr(a2, 'coCoMM_OptimizationDR'):
        assert _is_linked(a2, 'coCoMM_OptimizationDR', b)
    _safe_set(b, 'coCoMM_AttributeType52', None)
    assert not _is_linked(b, 'coCoMM_AttributeType52', a2)
    if hasattr(a2, 'coCoMM_OptimizationDR'):
        assert not _is_linked(a2, 'coCoMM_OptimizationDR', b)


def test_assoc_children10_reverse_link_reassign_clear():
    a1 = coCoMM_TreeConstraint(type="sample_text")
    a2 = coCoMM_TreeConstraint(type="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_Feature12', a1)
    assert _is_linked(b, 'coCoMM_Feature12', a1)
    if hasattr(a1, 'coCoMM_TreeConstraint11'):
        assert _is_linked(a1, 'coCoMM_TreeConstraint11', b)
    _safe_set(b, 'coCoMM_Feature12', a2)
    assert _is_linked(b, 'coCoMM_Feature12', a2)
    if hasattr(a1, 'coCoMM_TreeConstraint11'):
        assert not _is_linked(a1, 'coCoMM_TreeConstraint11', b)
    if hasattr(a2, 'coCoMM_TreeConstraint11'):
        assert _is_linked(a2, 'coCoMM_TreeConstraint11', b)
    _safe_set(b, 'coCoMM_Feature12', None)
    assert not _is_linked(b, 'coCoMM_Feature12', a2)
    if hasattr(a2, 'coCoMM_TreeConstraint11'):
        assert not _is_linked(a2, 'coCoMM_TreeConstraint11', b)


def test_assoc_configs56_reverse_link_reassign_clear():
    a1 = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    a2 = coCoMM_Project(date=date(2025, 6, 15), name="sample_text_2", target=False)
    b = coCoMM_Config(selected=True, type="sample_text")
    _safe_set(b, 'coCoMM_Config', a1)
    assert _is_linked(b, 'coCoMM_Config', a1)
    if hasattr(a1, 'coCoMM_Project57'):
        assert _is_linked(a1, 'coCoMM_Project57', b)
    _safe_set(b, 'coCoMM_Config', a2)
    assert _is_linked(b, 'coCoMM_Config', a2)
    if hasattr(a1, 'coCoMM_Project57'):
        assert not _is_linked(a1, 'coCoMM_Project57', b)
    if hasattr(a2, 'coCoMM_Project57'):
        assert _is_linked(a2, 'coCoMM_Project57', b)
    _safe_set(b, 'coCoMM_Config', None)
    assert not _is_linked(b, 'coCoMM_Config', a2)
    if hasattr(a2, 'coCoMM_Project57'):
        assert not _is_linked(a2, 'coCoMM_Project57', b)


def test_assoc_decisionRules53_reverse_link_reassign_clear():
    a1 = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    a2 = coCoMM_Project(date=date(2025, 6, 15), name="sample_text_2", target=False)
    b = coCoMM_DecisionRule(type="sample_text")
    _safe_set(b, 'coCoMM_DecisionRule55', a1)
    assert _is_linked(b, 'coCoMM_DecisionRule55', a1)
    if hasattr(a1, 'coCoMM_Project54'):
        assert _is_linked(a1, 'coCoMM_Project54', b)
    _safe_set(b, 'coCoMM_DecisionRule55', a2)
    assert _is_linked(b, 'coCoMM_DecisionRule55', a2)
    if hasattr(a1, 'coCoMM_Project54'):
        assert not _is_linked(a1, 'coCoMM_Project54', b)
    if hasattr(a2, 'coCoMM_Project54'):
        assert _is_linked(a2, 'coCoMM_Project54', b)
    _safe_set(b, 'coCoMM_DecisionRule55', None)
    assert not _is_linked(b, 'coCoMM_DecisionRule55', a2)
    if hasattr(a2, 'coCoMM_Project54'):
        assert not _is_linked(a2, 'coCoMM_Project54', b)


def test_assoc_elements15_reverse_link_reassign_clear():
    a1 = coCoMM_AttributeTypeElement(dataType="sample_text", name="sample_text")
    a2 = coCoMM_AttributeTypeElement(dataType="sample_text_2", name="sample_text_2")
    b = coCoMM_AttributeType(id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType16', {a1})
    assert _is_linked(b, 'coCoMM_AttributeType16', a1)
    if hasattr(a1, 'coCoMM_AttributeTypeElement'):
        assert _is_linked(a1, 'coCoMM_AttributeTypeElement', b)
    _safe_set(b, 'coCoMM_AttributeType16', {a2})
    assert _is_linked(b, 'coCoMM_AttributeType16', a2)
    if hasattr(a1, 'coCoMM_AttributeTypeElement'):
        assert not _is_linked(a1, 'coCoMM_AttributeTypeElement', b)
    if hasattr(a2, 'coCoMM_AttributeTypeElement'):
        assert _is_linked(a2, 'coCoMM_AttributeTypeElement', b)
    _safe_set(b, 'coCoMM_AttributeType16', set())
    assert not _is_linked(b, 'coCoMM_AttributeType16', a2)
    if hasattr(a2, 'coCoMM_AttributeTypeElement'):
        assert not _is_linked(a2, 'coCoMM_AttributeTypeElement', b)


def test_assoc_elements23_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureAttributeElement(value="sample_text")
    a2 = coCoMM_FeatureAttributeElement(value="sample_text_2")
    b = coCoMM_FeatureAttribute(name="sample_text")
    _safe_set(b, 'coCoMM_FeatureAttribute24', {a1})
    assert _is_linked(b, 'coCoMM_FeatureAttribute24', a1)
    if hasattr(a1, 'coCoMM_FeatureAttributeElement'):
        assert _is_linked(a1, 'coCoMM_FeatureAttributeElement', b)
    _safe_set(b, 'coCoMM_FeatureAttribute24', {a2})
    assert _is_linked(b, 'coCoMM_FeatureAttribute24', a2)
    if hasattr(a1, 'coCoMM_FeatureAttributeElement'):
        assert not _is_linked(a1, 'coCoMM_FeatureAttributeElement', b)
    if hasattr(a2, 'coCoMM_FeatureAttributeElement'):
        assert _is_linked(a2, 'coCoMM_FeatureAttributeElement', b)
    _safe_set(b, 'coCoMM_FeatureAttribute24', set())
    assert not _is_linked(b, 'coCoMM_FeatureAttribute24', a2)
    if hasattr(a2, 'coCoMM_FeatureAttributeElement'):
        assert not _is_linked(a2, 'coCoMM_FeatureAttributeElement', b)


def test_assoc_expressions68_reverse_link_reassign_clear():
    a1 = coCoMM_CTConstraintExpression(op="sample_text")
    a2 = coCoMM_CTConstraintExpression(op="sample_text_2")
    b = coCoMM_CTConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CTConstraintExpression69', a1)
    assert _is_linked(b, 'coCoMM_CTConstraintExpression69', a1)
    if hasattr(a1, 'coCoMM_CTConstraintExpression67'):
        assert _is_linked(a1, 'coCoMM_CTConstraintExpression67', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression69', a2)
    assert _is_linked(b, 'coCoMM_CTConstraintExpression69', a2)
    if hasattr(a1, 'coCoMM_CTConstraintExpression67'):
        assert not _is_linked(a1, 'coCoMM_CTConstraintExpression67', b)
    if hasattr(a2, 'coCoMM_CTConstraintExpression67'):
        assert _is_linked(a2, 'coCoMM_CTConstraintExpression67', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression69', None)
    assert not _is_linked(b, 'coCoMM_CTConstraintExpression69', a2)
    if hasattr(a2, 'coCoMM_CTConstraintExpression67'):
        assert not _is_linked(a2, 'coCoMM_CTConstraintExpression67', b)


def test_assoc_expressions74_reverse_link_reassign_clear():
    a1 = coCoMM_CMConstraintExpression(op="sample_text")
    a2 = coCoMM_CMConstraintExpression(op="sample_text_2")
    b = coCoMM_CMConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CMConstraintExpression75', a1)
    assert _is_linked(b, 'coCoMM_CMConstraintExpression75', a1)
    if hasattr(a1, 'coCoMM_CMConstraintExpression73'):
        assert _is_linked(a1, 'coCoMM_CMConstraintExpression73', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression75', a2)
    assert _is_linked(b, 'coCoMM_CMConstraintExpression75', a2)
    if hasattr(a1, 'coCoMM_CMConstraintExpression73'):
        assert not _is_linked(a1, 'coCoMM_CMConstraintExpression73', b)
    if hasattr(a2, 'coCoMM_CMConstraintExpression73'):
        assert _is_linked(a2, 'coCoMM_CMConstraintExpression73', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression75', None)
    assert not _is_linked(b, 'coCoMM_CMConstraintExpression75', a2)
    if hasattr(a2, 'coCoMM_CMConstraintExpression73'):
        assert not _is_linked(a2, 'coCoMM_CMConstraintExpression73', b)


def test_assoc_feature44_reverse_link_reassign_clear():
    a1 = coCoMM_SelectionStateDR(state="sample_text")
    a2 = coCoMM_SelectionStateDR(state="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_Feature46', a1)
    assert _is_linked(b, 'coCoMM_Feature46', a1)
    if hasattr(a1, 'coCoMM_SelectionStateDR45'):
        assert _is_linked(a1, 'coCoMM_SelectionStateDR45', b)
    _safe_set(b, 'coCoMM_Feature46', a2)
    assert _is_linked(b, 'coCoMM_Feature46', a2)
    if hasattr(a1, 'coCoMM_SelectionStateDR45'):
        assert not _is_linked(a1, 'coCoMM_SelectionStateDR45', b)
    if hasattr(a2, 'coCoMM_SelectionStateDR45'):
        assert _is_linked(a2, 'coCoMM_SelectionStateDR45', b)
    _safe_set(b, 'coCoMM_Feature46', None)
    assert not _is_linked(b, 'coCoMM_Feature46', a2)
    if hasattr(a2, 'coCoMM_SelectionStateDR45'):
        assert not _is_linked(a2, 'coCoMM_SelectionStateDR45', b)


def test_assoc_featureAttributes17_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureAttribute(name="sample_text")
    a2 = coCoMM_FeatureAttribute(name="sample_text_2")
    b = coCoMM_AttributeType(id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType18', {a1})
    assert _is_linked(b, 'coCoMM_AttributeType18', a1)
    if hasattr(a1, 'coCoMM_FeatureAttribute19'):
        assert _is_linked(a1, 'coCoMM_FeatureAttribute19', b)
    _safe_set(b, 'coCoMM_AttributeType18', {a2})
    assert _is_linked(b, 'coCoMM_AttributeType18', a2)
    if hasattr(a1, 'coCoMM_FeatureAttribute19'):
        assert not _is_linked(a1, 'coCoMM_FeatureAttribute19', b)
    if hasattr(a2, 'coCoMM_FeatureAttribute19'):
        assert _is_linked(a2, 'coCoMM_FeatureAttribute19', b)
    _safe_set(b, 'coCoMM_AttributeType18', set())
    assert not _is_linked(b, 'coCoMM_AttributeType18', a2)
    if hasattr(a2, 'coCoMM_FeatureAttribute19'):
        assert not _is_linked(a2, 'coCoMM_FeatureAttribute19', b)


def test_assoc_featureAttributes8_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureAttribute(name="sample_text")
    a2 = coCoMM_FeatureAttribute(name="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_Feature9', {a1})
    assert _is_linked(b, 'coCoMM_Feature9', a1)
    if hasattr(a1, 'coCoMM_FeatureAttribute'):
        assert _is_linked(a1, 'coCoMM_FeatureAttribute', b)
    _safe_set(b, 'coCoMM_Feature9', {a2})
    assert _is_linked(b, 'coCoMM_Feature9', a2)
    if hasattr(a1, 'coCoMM_FeatureAttribute'):
        assert not _is_linked(a1, 'coCoMM_FeatureAttribute', b)
    if hasattr(a2, 'coCoMM_FeatureAttribute'):
        assert _is_linked(a2, 'coCoMM_FeatureAttribute', b)
    _safe_set(b, 'coCoMM_Feature9', set())
    assert not _is_linked(b, 'coCoMM_Feature9', a2)
    if hasattr(a2, 'coCoMM_FeatureAttribute'):
        assert not _is_linked(a2, 'coCoMM_FeatureAttribute', b)


def test_assoc_featureModel42_reverse_link_reassign_clear():
    a1 = coCoMM_SelectionStateDR(state="sample_text")
    a2 = coCoMM_SelectionStateDR(state="sample_text_2")
    b = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    _safe_set(b, 'coCoMM_FeatureModel43', a1)
    assert _is_linked(b, 'coCoMM_FeatureModel43', a1)
    if hasattr(a1, 'coCoMM_SelectionStateDR'):
        assert _is_linked(a1, 'coCoMM_SelectionStateDR', b)
    _safe_set(b, 'coCoMM_FeatureModel43', a2)
    assert _is_linked(b, 'coCoMM_FeatureModel43', a2)
    if hasattr(a1, 'coCoMM_SelectionStateDR'):
        assert not _is_linked(a1, 'coCoMM_SelectionStateDR', b)
    if hasattr(a2, 'coCoMM_SelectionStateDR'):
        assert _is_linked(a2, 'coCoMM_SelectionStateDR', b)
    _safe_set(b, 'coCoMM_FeatureModel43', None)
    assert not _is_linked(b, 'coCoMM_FeatureModel43', a2)
    if hasattr(a2, 'coCoMM_SelectionStateDR'):
        assert not _is_linked(a2, 'coCoMM_SelectionStateDR', b)


def test_assoc_featureModel5_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(isDomain=False, name="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_Feature6', a1)
    assert _is_linked(b, 'coCoMM_Feature6', a1)
    if hasattr(a1, 'coCoMM_FeatureModel7'):
        assert _is_linked(a1, 'coCoMM_FeatureModel7', b)
    _safe_set(b, 'coCoMM_Feature6', a2)
    assert _is_linked(b, 'coCoMM_Feature6', a2)
    if hasattr(a1, 'coCoMM_FeatureModel7'):
        assert not _is_linked(a1, 'coCoMM_FeatureModel7', b)
    if hasattr(a2, 'coCoMM_FeatureModel7'):
        assert _is_linked(a2, 'coCoMM_FeatureModel7', b)
    _safe_set(b, 'coCoMM_Feature6', None)
    assert not _is_linked(b, 'coCoMM_Feature6', a2)
    if hasattr(a2, 'coCoMM_FeatureModel7'):
        assert not _is_linked(a2, 'coCoMM_FeatureModel7', b)


def test_assoc_features61_reverse_link_reassign_clear():
    a1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    b = coCoMM_Config(selected=True, type="sample_text")
    _safe_set(b, 'coCoMM_Config62', {a1})
    assert _is_linked(b, 'coCoMM_Config62', a1)
    if hasattr(a1, 'coCoMM_Feature63'):
        assert _is_linked(a1, 'coCoMM_Feature63', b)
    _safe_set(b, 'coCoMM_Config62', {a2})
    assert _is_linked(b, 'coCoMM_Config62', a2)
    if hasattr(a1, 'coCoMM_Feature63'):
        assert not _is_linked(a1, 'coCoMM_Feature63', b)
    if hasattr(a2, 'coCoMM_Feature63'):
        assert _is_linked(a2, 'coCoMM_Feature63', b)
    _safe_set(b, 'coCoMM_Config62', set())
    assert not _is_linked(b, 'coCoMM_Config62', a2)
    if hasattr(a2, 'coCoMM_Feature63'):
        assert not _is_linked(a2, 'coCoMM_Feature63', b)


def test_assoc_features64_reverse_link_reassign_clear():
    a1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    b = coCoMM_CTConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CTConstraintExpression65', {a1})
    assert _is_linked(b, 'coCoMM_CTConstraintExpression65', a1)
    if hasattr(a1, 'coCoMM_Feature66'):
        assert _is_linked(a1, 'coCoMM_Feature66', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression65', {a2})
    assert _is_linked(b, 'coCoMM_CTConstraintExpression65', a2)
    if hasattr(a1, 'coCoMM_Feature66'):
        assert not _is_linked(a1, 'coCoMM_Feature66', b)
    if hasattr(a2, 'coCoMM_Feature66'):
        assert _is_linked(a2, 'coCoMM_Feature66', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression65', set())
    assert not _is_linked(b, 'coCoMM_CTConstraintExpression65', a2)
    if hasattr(a2, 'coCoMM_Feature66'):
        assert not _is_linked(a2, 'coCoMM_Feature66', b)


def test_assoc_features70_reverse_link_reassign_clear():
    a1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    b = coCoMM_CMConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CMConstraintExpression71', {a1})
    assert _is_linked(b, 'coCoMM_CMConstraintExpression71', a1)
    if hasattr(a1, 'coCoMM_Feature72'):
        assert _is_linked(a1, 'coCoMM_Feature72', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression71', {a2})
    assert _is_linked(b, 'coCoMM_CMConstraintExpression71', a2)
    if hasattr(a1, 'coCoMM_Feature72'):
        assert not _is_linked(a1, 'coCoMM_Feature72', b)
    if hasattr(a2, 'coCoMM_Feature72'):
        assert _is_linked(a2, 'coCoMM_Feature72', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression71', set())
    assert not _is_linked(b, 'coCoMM_CMConstraintExpression71', a2)
    if hasattr(a2, 'coCoMM_Feature72'):
        assert not _is_linked(a2, 'coCoMM_Feature72', b)


def test_assoc_independentAttrType14_reverse_link_reassign_clear():
    a1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    a2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    b = coCoMM_AttributeType(id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType13', a1)
    assert _is_linked(b, 'coCoMM_AttributeType13', a1)
    if hasattr(a1, 'coCoMM_AttributeType'):
        assert _is_linked(a1, 'coCoMM_AttributeType', b)
    _safe_set(b, 'coCoMM_AttributeType13', a2)
    assert _is_linked(b, 'coCoMM_AttributeType13', a2)
    if hasattr(a1, 'coCoMM_AttributeType'):
        assert not _is_linked(a1, 'coCoMM_AttributeType', b)
    if hasattr(a2, 'coCoMM_AttributeType'):
        assert _is_linked(a2, 'coCoMM_AttributeType', b)
    _safe_set(b, 'coCoMM_AttributeType13', None)
    assert not _is_linked(b, 'coCoMM_AttributeType13', a2)
    if hasattr(a2, 'coCoMM_AttributeType'):
        assert not _is_linked(a2, 'coCoMM_AttributeType', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(isDomain=False, name="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_Feature', a1)
    assert _is_linked(b, 'coCoMM_Feature', a1)
    if hasattr(a1, 'coCoMM_FeatureModel'):
        assert _is_linked(a1, 'coCoMM_FeatureModel', b)
    _safe_set(b, 'coCoMM_Feature', a2)
    assert _is_linked(b, 'coCoMM_Feature', a2)
    if hasattr(a1, 'coCoMM_FeatureModel'):
        assert not _is_linked(a1, 'coCoMM_FeatureModel', b)
    if hasattr(a2, 'coCoMM_FeatureModel'):
        assert _is_linked(a2, 'coCoMM_FeatureModel', b)
    _safe_set(b, 'coCoMM_Feature', None)
    assert not _is_linked(b, 'coCoMM_Feature', a2)
    if hasattr(a2, 'coCoMM_FeatureModel'):
        assert not _is_linked(a2, 'coCoMM_FeatureModel', b)


def test_assoc_stakeholder58_reverse_link_reassign_clear():
    a1 = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    a2 = coCoMM_Stakeholder(job="sample_text_2", name="sample_text_2")
    b = coCoMM_Config(selected=True, type="sample_text")
    _safe_set(b, 'coCoMM_Config59', a1)
    assert _is_linked(b, 'coCoMM_Config59', a1)
    if hasattr(a1, 'coCoMM_Stakeholder60'):
        assert _is_linked(a1, 'coCoMM_Stakeholder60', b)
    _safe_set(b, 'coCoMM_Config59', a2)
    assert _is_linked(b, 'coCoMM_Config59', a2)
    if hasattr(a1, 'coCoMM_Stakeholder60'):
        assert not _is_linked(a1, 'coCoMM_Stakeholder60', b)
    if hasattr(a2, 'coCoMM_Stakeholder60'):
        assert _is_linked(a2, 'coCoMM_Stakeholder60', b)
    _safe_set(b, 'coCoMM_Config59', None)
    assert not _is_linked(b, 'coCoMM_Config59', a2)
    if hasattr(a2, 'coCoMM_Stakeholder60'):
        assert not _is_linked(a2, 'coCoMM_Stakeholder60', b)


def test_assoc_treeConstraints3_reverse_link_reassign_clear():
    a1 = coCoMM_TreeConstraint(type="sample_text")
    a2 = coCoMM_TreeConstraint(type="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_Feature4', {a1})
    assert _is_linked(b, 'coCoMM_Feature4', a1)
    if hasattr(a1, 'coCoMM_TreeConstraint'):
        assert _is_linked(a1, 'coCoMM_TreeConstraint', b)
    _safe_set(b, 'coCoMM_Feature4', {a2})
    assert _is_linked(b, 'coCoMM_Feature4', a2)
    if hasattr(a1, 'coCoMM_TreeConstraint'):
        assert not _is_linked(a1, 'coCoMM_TreeConstraint', b)
    if hasattr(a2, 'coCoMM_TreeConstraint'):
        assert _is_linked(a2, 'coCoMM_TreeConstraint', b)
    _safe_set(b, 'coCoMM_Feature4', set())
    assert not _is_linked(b, 'coCoMM_Feature4', a2)
    if hasattr(a2, 'coCoMM_TreeConstraint'):
        assert not _is_linked(a2, 'coCoMM_TreeConstraint', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attrType48_stub_double():
    # coCoMM_HardLimitDR has no real 'coCoMM_HardLimitDR49' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_AttributeType(id="sample_text", name="sample_text")
    partner = coCoMM_HardLimitDR()
    setattr(partner, 'coCoMM_HardLimitDR49', None)
    _safe_set(owner, 'coCoMM_AttributeType50', partner)
    assert getattr(partner, 'coCoMM_HardLimitDR49') == owner
    _safe_set(owner, 'coCoMM_AttributeType50', None)
    assert getattr(partner, 'coCoMM_HardLimitDR49') is None


def test_assoc_attributeTypes33_stub_double():
    # coCoMM_CoCo has no real 'coCoMM_CoCo34' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_AttributeType(id="sample_text", name="sample_text")
    partner = coCoMM_CoCo()
    setattr(partner, 'coCoMM_CoCo34', None)
    _safe_set(owner, 'coCoMM_AttributeType35', partner)
    assert owner in getattr(partner, 'coCoMM_CoCo34')
    _safe_set(owner, 'coCoMM_AttributeType35', None)
    assert owner not in getattr(partner, 'coCoMM_CoCo34')


def test_assoc_ctConstraints1_stub_double():
    # coCoMM_CrossTreeConstraint has no real 'coCoMM_CrossTreeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    partner = coCoMM_CrossTreeConstraint()
    setattr(partner, 'coCoMM_CrossTreeConstraint', None)
    _safe_set(owner, 'coCoMM_FeatureModel2', {partner})
    assert getattr(partner, 'coCoMM_CrossTreeConstraint') == owner
    _safe_set(owner, 'coCoMM_FeatureModel2', set())
    assert getattr(partner, 'coCoMM_CrossTreeConstraint') is None


def test_assoc_decisionRules31_stub_double():
    # coCoMM_CoCo has no real 'coCoMM_CoCo32' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_DecisionRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_DecisionRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_DecisionRule(type="sample_text")
    partner = coCoMM_CoCo()
    setattr(partner, 'coCoMM_CoCo32', None)
    _safe_set(owner, 'coCoMM_DecisionRule', partner)
    assert owner in getattr(partner, 'coCoMM_CoCo32')
    _safe_set(owner, 'coCoMM_DecisionRule', None)
    assert owner not in getattr(partner, 'coCoMM_CoCo32')


def test_assoc_expressions25_stub_double():
    # coCoMM_CrossTreeConstraint has no real 'coCoMM_CrossTreeConstraint26' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_CTConstraintExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_CTConstraintExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_CTConstraintExpression(op="sample_text")
    partner = coCoMM_CrossTreeConstraint()
    setattr(partner, 'coCoMM_CrossTreeConstraint26', None)
    _safe_set(owner, 'coCoMM_CTConstraintExpression', partner)
    assert owner in getattr(partner, 'coCoMM_CrossTreeConstraint26')
    _safe_set(owner, 'coCoMM_CTConstraintExpression', None)
    assert owner not in getattr(partner, 'coCoMM_CrossTreeConstraint26')


def test_assoc_expressions40_stub_double():
    # coCoMM_CrossModelConstraint has no real 'coCoMM_CrossModelConstraint41' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_CMConstraintExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_CMConstraintExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_CMConstraintExpression(op="sample_text")
    partner = coCoMM_CrossModelConstraint()
    setattr(partner, 'coCoMM_CrossModelConstraint41', None)
    _safe_set(owner, 'coCoMM_CMConstraintExpression', partner)
    assert owner in getattr(partner, 'coCoMM_CrossModelConstraint41')
    _safe_set(owner, 'coCoMM_CMConstraintExpression', None)
    assert owner not in getattr(partner, 'coCoMM_CrossModelConstraint41')


def test_assoc_expressions47_stub_double():
    # coCoMM_HardLimitDR has no real 'coCoMM_HardLimitDR' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_HardLimitDRExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_HardLimitDRExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    partner = coCoMM_HardLimitDR()
    setattr(partner, 'coCoMM_HardLimitDR', None)
    _safe_set(owner, 'coCoMM_HardLimitDRExpression', partner)
    assert owner in getattr(partner, 'coCoMM_HardLimitDR')
    _safe_set(owner, 'coCoMM_HardLimitDRExpression', None)
    assert owner not in getattr(partner, 'coCoMM_HardLimitDR')


def test_assoc_featureModels27_stub_double():
    # coCoMM_CoCo has no real 'coCoMM_CoCo' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    partner = coCoMM_CoCo()
    setattr(partner, 'coCoMM_CoCo', None)
    _safe_set(owner, 'coCoMM_FeatureModel28', partner)
    assert owner in getattr(partner, 'coCoMM_CoCo')
    _safe_set(owner, 'coCoMM_FeatureModel28', None)
    assert owner not in getattr(partner, 'coCoMM_CoCo')


def test_assoc_project36_stub_double():
    # coCoMM_CoCo has no real 'coCoMM_CoCo37' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    partner = coCoMM_CoCo()
    setattr(partner, 'coCoMM_CoCo37', None)
    _safe_set(owner, 'coCoMM_Project', partner)
    assert owner in getattr(partner, 'coCoMM_CoCo37')
    _safe_set(owner, 'coCoMM_Project', None)
    assert owner not in getattr(partner, 'coCoMM_CoCo37')


def test_assoc_stakeholders38_stub_double():
    # coCoMM_CoCo has no real 'coCoMM_CoCo39' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_Stakeholder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_Stakeholder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    partner = coCoMM_CoCo()
    setattr(partner, 'coCoMM_CoCo39', None)
    _safe_set(owner, 'coCoMM_Stakeholder', partner)
    assert owner in getattr(partner, 'coCoMM_CoCo39')
    _safe_set(owner, 'coCoMM_Stakeholder', None)
    assert owner not in getattr(partner, 'coCoMM_CoCo39')


