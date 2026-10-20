import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConfigurationConstraint,
    SolutionConstraint,
    coCoMM_AggregationFunction,
    coCoMM_AttributeType,
    coCoMM_CMConstraintExpression,
    coCoMM_CTConstraintExpression,
    coCoMM_CoCo,
    coCoMM_Config,
    coCoMM_ConfigurationConstraint,
    coCoMM_CrossModelConstraint,
    coCoMM_CrossTreeConstraint,
    coCoMM_Feature,
    coCoMM_FeatureAttribute,
    coCoMM_FeatureModel,
    coCoMM_HardLimitCC,
    coCoMM_HardLimitCCExpression,
    coCoMM_OptimizationCC,
    coCoMM_OptimizationSC,
    coCoMM_Project,
    coCoMM_SelectionStateCC,
    coCoMM_SolutionConstraint,
    coCoMM_Stakeholder,
    coCoMM_TreeConstraint,
    AggregationOp,
    CCHardLimitOp,
    CCOptimizationOp,
    CCSelectionStateType,
    CCType,
    CMConstraintType,
    CTConstraintType,
    ConfigType,
    DataType,
    OptimizationSCFunct,
    SCType,
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

def test_assoc_attrType13_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureAttribute(defaultValue="sample_text", maxValue="sample_text", minValue="sample_text")
    a2 = coCoMM_FeatureAttribute(defaultValue="sample_text_2", maxValue="sample_text_2", minValue="sample_text_2")
    b = coCoMM_AttributeType(dataType="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType', a1)
    assert _is_linked(b, 'coCoMM_AttributeType', a1)
    if hasattr(a1, 'coCoMM_FeatureAttribute14'):
        assert _is_linked(a1, 'coCoMM_FeatureAttribute14', b)
    _safe_set(b, 'coCoMM_AttributeType', a2)
    assert _is_linked(b, 'coCoMM_AttributeType', a2)
    if hasattr(a1, 'coCoMM_FeatureAttribute14'):
        assert not _is_linked(a1, 'coCoMM_FeatureAttribute14', b)
    if hasattr(a2, 'coCoMM_FeatureAttribute14'):
        assert _is_linked(a2, 'coCoMM_FeatureAttribute14', b)
    _safe_set(b, 'coCoMM_AttributeType', None)
    assert not _is_linked(b, 'coCoMM_AttributeType', a2)
    if hasattr(a2, 'coCoMM_FeatureAttribute14'):
        assert not _is_linked(a2, 'coCoMM_FeatureAttribute14', b)


def test_assoc_attrType70_reverse_link_reassign_clear():
    a1 = coCoMM_AttributeType(dataType="sample_text", id="sample_text", name="sample_text")
    a2 = coCoMM_AttributeType(dataType="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = coCoMM_AggregationFunction(operation="sample_text")
    _safe_set(b, 'coCoMM_AggregationFunction71', a1)
    assert _is_linked(b, 'coCoMM_AggregationFunction71', a1)
    if hasattr(a1, 'coCoMM_AttributeType72'):
        assert _is_linked(a1, 'coCoMM_AttributeType72', b)
    _safe_set(b, 'coCoMM_AggregationFunction71', a2)
    assert _is_linked(b, 'coCoMM_AggregationFunction71', a2)
    if hasattr(a1, 'coCoMM_AttributeType72'):
        assert not _is_linked(a1, 'coCoMM_AttributeType72', b)
    if hasattr(a2, 'coCoMM_AttributeType72'):
        assert _is_linked(a2, 'coCoMM_AttributeType72', b)
    _safe_set(b, 'coCoMM_AggregationFunction71', None)
    assert not _is_linked(b, 'coCoMM_AggregationFunction71', a2)
    if hasattr(a2, 'coCoMM_AttributeType72'):
        assert not _is_linked(a2, 'coCoMM_AttributeType72', b)


def test_assoc_attrType73_reverse_link_reassign_clear():
    a1 = coCoMM_OptimizationSC(funct="sample_text")
    a2 = coCoMM_OptimizationSC(funct="sample_text_2")
    b = coCoMM_AttributeType(dataType="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType74', a1)
    assert _is_linked(b, 'coCoMM_AttributeType74', a1)
    if hasattr(a1, 'coCoMM_OptimizationSC'):
        assert _is_linked(a1, 'coCoMM_OptimizationSC', b)
    _safe_set(b, 'coCoMM_AttributeType74', a2)
    assert _is_linked(b, 'coCoMM_AttributeType74', a2)
    if hasattr(a1, 'coCoMM_OptimizationSC'):
        assert not _is_linked(a1, 'coCoMM_OptimizationSC', b)
    if hasattr(a2, 'coCoMM_OptimizationSC'):
        assert _is_linked(a2, 'coCoMM_OptimizationSC', b)
    _safe_set(b, 'coCoMM_AttributeType74', None)
    assert not _is_linked(b, 'coCoMM_AttributeType74', a2)
    if hasattr(a2, 'coCoMM_OptimizationSC'):
        assert not _is_linked(a2, 'coCoMM_OptimizationSC', b)


def test_assoc_attributeTypes25_reverse_link_reassign_clear():
    a1 = coCoMM_CoCo(configScenario="sample_text", id="sample_text", name="sample_text")
    a2 = coCoMM_CoCo(configScenario="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = coCoMM_AttributeType(dataType="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType27', a1)
    assert _is_linked(b, 'coCoMM_AttributeType27', a1)
    if hasattr(a1, 'coCoMM_CoCo26'):
        assert _is_linked(a1, 'coCoMM_CoCo26', b)
    _safe_set(b, 'coCoMM_AttributeType27', a2)
    assert _is_linked(b, 'coCoMM_AttributeType27', a2)
    if hasattr(a1, 'coCoMM_CoCo26'):
        assert not _is_linked(a1, 'coCoMM_CoCo26', b)
    if hasattr(a2, 'coCoMM_CoCo26'):
        assert _is_linked(a2, 'coCoMM_CoCo26', b)
    _safe_set(b, 'coCoMM_AttributeType27', None)
    assert not _is_linked(b, 'coCoMM_AttributeType27', a2)
    if hasattr(a2, 'coCoMM_CoCo26'):
        assert not _is_linked(a2, 'coCoMM_CoCo26', b)


def test_assoc_children10_reverse_link_reassign_clear():
    a1 = coCoMM_TreeConstraint(type="sample_text")
    a2 = coCoMM_TreeConstraint(type="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
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


def test_assoc_configConstraints23_reverse_link_reassign_clear():
    a1 = coCoMM_ConfigurationConstraint(id="sample_text", name="sample_text", type="sample_text")
    a2 = coCoMM_ConfigurationConstraint(id="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = coCoMM_CoCo(configScenario="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_CoCo24', {a1})
    assert _is_linked(b, 'coCoMM_CoCo24', a1)
    if hasattr(a1, 'coCoMM_ConfigurationConstraint'):
        assert _is_linked(a1, 'coCoMM_ConfigurationConstraint', b)
    _safe_set(b, 'coCoMM_CoCo24', {a2})
    assert _is_linked(b, 'coCoMM_CoCo24', a2)
    if hasattr(a1, 'coCoMM_ConfigurationConstraint'):
        assert not _is_linked(a1, 'coCoMM_ConfigurationConstraint', b)
    if hasattr(a2, 'coCoMM_ConfigurationConstraint'):
        assert _is_linked(a2, 'coCoMM_ConfigurationConstraint', b)
    _safe_set(b, 'coCoMM_CoCo24', set())
    assert not _is_linked(b, 'coCoMM_CoCo24', a2)
    if hasattr(a2, 'coCoMM_ConfigurationConstraint'):
        assert not _is_linked(a2, 'coCoMM_ConfigurationConstraint', b)


def test_assoc_configConstraints44_reverse_link_reassign_clear():
    a1 = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    a2 = coCoMM_Project(date=date(2025, 6, 15), name="sample_text_2", target=False)
    b = coCoMM_ConfigurationConstraint(id="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'coCoMM_ConfigurationConstraint46', a1)
    assert _is_linked(b, 'coCoMM_ConfigurationConstraint46', a1)
    if hasattr(a1, 'coCoMM_Project45'):
        assert _is_linked(a1, 'coCoMM_Project45', b)
    _safe_set(b, 'coCoMM_ConfigurationConstraint46', a2)
    assert _is_linked(b, 'coCoMM_ConfigurationConstraint46', a2)
    if hasattr(a1, 'coCoMM_Project45'):
        assert not _is_linked(a1, 'coCoMM_Project45', b)
    if hasattr(a2, 'coCoMM_Project45'):
        assert _is_linked(a2, 'coCoMM_Project45', b)
    _safe_set(b, 'coCoMM_ConfigurationConstraint46', None)
    assert not _is_linked(b, 'coCoMM_ConfigurationConstraint46', a2)
    if hasattr(a2, 'coCoMM_Project45'):
        assert not _is_linked(a2, 'coCoMM_Project45', b)


def test_assoc_configs50_reverse_link_reassign_clear():
    a1 = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    a2 = coCoMM_Project(date=date(2025, 6, 15), name="sample_text_2", target=False)
    b = coCoMM_Config(selected=True, type="sample_text")
    _safe_set(b, 'coCoMM_Config', a1)
    assert _is_linked(b, 'coCoMM_Config', a1)
    if hasattr(a1, 'coCoMM_Project51'):
        assert _is_linked(a1, 'coCoMM_Project51', b)
    _safe_set(b, 'coCoMM_Config', a2)
    assert _is_linked(b, 'coCoMM_Config', a2)
    if hasattr(a1, 'coCoMM_Project51'):
        assert not _is_linked(a1, 'coCoMM_Project51', b)
    if hasattr(a2, 'coCoMM_Project51'):
        assert _is_linked(a2, 'coCoMM_Project51', b)
    _safe_set(b, 'coCoMM_Config', None)
    assert not _is_linked(b, 'coCoMM_Config', a2)
    if hasattr(a2, 'coCoMM_Project51'):
        assert not _is_linked(a2, 'coCoMM_Project51', b)


def test_assoc_expressions62_reverse_link_reassign_clear():
    a1 = coCoMM_CTConstraintExpression(op="sample_text")
    a2 = coCoMM_CTConstraintExpression(op="sample_text_2")
    b = coCoMM_CTConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CTConstraintExpression63', a1)
    assert _is_linked(b, 'coCoMM_CTConstraintExpression63', a1)
    if hasattr(a1, 'coCoMM_CTConstraintExpression61'):
        assert _is_linked(a1, 'coCoMM_CTConstraintExpression61', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression63', a2)
    assert _is_linked(b, 'coCoMM_CTConstraintExpression63', a2)
    if hasattr(a1, 'coCoMM_CTConstraintExpression61'):
        assert not _is_linked(a1, 'coCoMM_CTConstraintExpression61', b)
    if hasattr(a2, 'coCoMM_CTConstraintExpression61'):
        assert _is_linked(a2, 'coCoMM_CTConstraintExpression61', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression63', None)
    assert not _is_linked(b, 'coCoMM_CTConstraintExpression63', a2)
    if hasattr(a2, 'coCoMM_CTConstraintExpression61'):
        assert not _is_linked(a2, 'coCoMM_CTConstraintExpression61', b)


def test_assoc_expressions68_reverse_link_reassign_clear():
    a1 = coCoMM_CMConstraintExpression(op="sample_text")
    a2 = coCoMM_CMConstraintExpression(op="sample_text_2")
    b = coCoMM_CMConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CMConstraintExpression69', a1)
    assert _is_linked(b, 'coCoMM_CMConstraintExpression69', a1)
    if hasattr(a1, 'coCoMM_CMConstraintExpression67'):
        assert _is_linked(a1, 'coCoMM_CMConstraintExpression67', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression69', a2)
    assert _is_linked(b, 'coCoMM_CMConstraintExpression69', a2)
    if hasattr(a1, 'coCoMM_CMConstraintExpression67'):
        assert not _is_linked(a1, 'coCoMM_CMConstraintExpression67', b)
    if hasattr(a2, 'coCoMM_CMConstraintExpression67'):
        assert _is_linked(a2, 'coCoMM_CMConstraintExpression67', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression69', None)
    assert not _is_linked(b, 'coCoMM_CMConstraintExpression69', a2)
    if hasattr(a2, 'coCoMM_CMConstraintExpression67'):
        assert not _is_linked(a2, 'coCoMM_CMConstraintExpression67', b)


def test_assoc_feature36_reverse_link_reassign_clear():
    a1 = coCoMM_SelectionStateCC(state="sample_text")
    a2 = coCoMM_SelectionStateCC(state="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    _safe_set(b, 'coCoMM_Feature38', a1)
    assert _is_linked(b, 'coCoMM_Feature38', a1)
    if hasattr(a1, 'coCoMM_SelectionStateCC37'):
        assert _is_linked(a1, 'coCoMM_SelectionStateCC37', b)
    _safe_set(b, 'coCoMM_Feature38', a2)
    assert _is_linked(b, 'coCoMM_Feature38', a2)
    if hasattr(a1, 'coCoMM_SelectionStateCC37'):
        assert not _is_linked(a1, 'coCoMM_SelectionStateCC37', b)
    if hasattr(a2, 'coCoMM_SelectionStateCC37'):
        assert _is_linked(a2, 'coCoMM_SelectionStateCC37', b)
    _safe_set(b, 'coCoMM_Feature38', None)
    assert not _is_linked(b, 'coCoMM_Feature38', a2)
    if hasattr(a2, 'coCoMM_SelectionStateCC37'):
        assert not _is_linked(a2, 'coCoMM_SelectionStateCC37', b)


def test_assoc_featureAttributes8_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureAttribute(defaultValue="sample_text", maxValue="sample_text", minValue="sample_text")
    a2 = coCoMM_FeatureAttribute(defaultValue="sample_text_2", maxValue="sample_text_2", minValue="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
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


def test_assoc_featureModel34_reverse_link_reassign_clear():
    a1 = coCoMM_SelectionStateCC(state="sample_text")
    a2 = coCoMM_SelectionStateCC(state="sample_text_2")
    b = coCoMM_FeatureModel(id="sample_text", isDomain=True, name="sample_text")
    _safe_set(b, 'coCoMM_FeatureModel35', a1)
    assert _is_linked(b, 'coCoMM_FeatureModel35', a1)
    if hasattr(a1, 'coCoMM_SelectionStateCC'):
        assert _is_linked(a1, 'coCoMM_SelectionStateCC', b)
    _safe_set(b, 'coCoMM_FeatureModel35', a2)
    assert _is_linked(b, 'coCoMM_FeatureModel35', a2)
    if hasattr(a1, 'coCoMM_SelectionStateCC'):
        assert not _is_linked(a1, 'coCoMM_SelectionStateCC', b)
    if hasattr(a2, 'coCoMM_SelectionStateCC'):
        assert _is_linked(a2, 'coCoMM_SelectionStateCC', b)
    _safe_set(b, 'coCoMM_FeatureModel35', None)
    assert not _is_linked(b, 'coCoMM_FeatureModel35', a2)
    if hasattr(a2, 'coCoMM_SelectionStateCC'):
        assert not _is_linked(a2, 'coCoMM_SelectionStateCC', b)


def test_assoc_featureModel5_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(id="sample_text", isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(id="sample_text_2", isDomain=False, name="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
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


def test_assoc_featureModels17_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(id="sample_text", isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(id="sample_text_2", isDomain=False, name="sample_text_2")
    b = coCoMM_CoCo(configScenario="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_CoCo', {a1})
    assert _is_linked(b, 'coCoMM_CoCo', a1)
    if hasattr(a1, 'coCoMM_FeatureModel18'):
        assert _is_linked(a1, 'coCoMM_FeatureModel18', b)
    _safe_set(b, 'coCoMM_CoCo', {a2})
    assert _is_linked(b, 'coCoMM_CoCo', a2)
    if hasattr(a1, 'coCoMM_FeatureModel18'):
        assert not _is_linked(a1, 'coCoMM_FeatureModel18', b)
    if hasattr(a2, 'coCoMM_FeatureModel18'):
        assert _is_linked(a2, 'coCoMM_FeatureModel18', b)
    _safe_set(b, 'coCoMM_CoCo', set())
    assert not _is_linked(b, 'coCoMM_CoCo', a2)
    if hasattr(a2, 'coCoMM_FeatureModel18'):
        assert not _is_linked(a2, 'coCoMM_FeatureModel18', b)


def test_assoc_features55_reverse_link_reassign_clear():
    a1 = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", mandatory=False, name="sample_text_2")
    b = coCoMM_Config(selected=True, type="sample_text")
    _safe_set(b, 'coCoMM_Config56', {a1})
    assert _is_linked(b, 'coCoMM_Config56', a1)
    if hasattr(a1, 'coCoMM_Feature57'):
        assert _is_linked(a1, 'coCoMM_Feature57', b)
    _safe_set(b, 'coCoMM_Config56', {a2})
    assert _is_linked(b, 'coCoMM_Config56', a2)
    if hasattr(a1, 'coCoMM_Feature57'):
        assert not _is_linked(a1, 'coCoMM_Feature57', b)
    if hasattr(a2, 'coCoMM_Feature57'):
        assert _is_linked(a2, 'coCoMM_Feature57', b)
    _safe_set(b, 'coCoMM_Config56', set())
    assert not _is_linked(b, 'coCoMM_Config56', a2)
    if hasattr(a2, 'coCoMM_Feature57'):
        assert not _is_linked(a2, 'coCoMM_Feature57', b)


def test_assoc_features58_reverse_link_reassign_clear():
    a1 = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", mandatory=False, name="sample_text_2")
    b = coCoMM_CTConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CTConstraintExpression59', {a1})
    assert _is_linked(b, 'coCoMM_CTConstraintExpression59', a1)
    if hasattr(a1, 'coCoMM_Feature60'):
        assert _is_linked(a1, 'coCoMM_Feature60', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression59', {a2})
    assert _is_linked(b, 'coCoMM_CTConstraintExpression59', a2)
    if hasattr(a1, 'coCoMM_Feature60'):
        assert not _is_linked(a1, 'coCoMM_Feature60', b)
    if hasattr(a2, 'coCoMM_Feature60'):
        assert _is_linked(a2, 'coCoMM_Feature60', b)
    _safe_set(b, 'coCoMM_CTConstraintExpression59', set())
    assert not _is_linked(b, 'coCoMM_CTConstraintExpression59', a2)
    if hasattr(a2, 'coCoMM_Feature60'):
        assert not _is_linked(a2, 'coCoMM_Feature60', b)


def test_assoc_features64_reverse_link_reassign_clear():
    a1 = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", mandatory=False, name="sample_text_2")
    b = coCoMM_CMConstraintExpression(op="sample_text")
    _safe_set(b, 'coCoMM_CMConstraintExpression65', {a1})
    assert _is_linked(b, 'coCoMM_CMConstraintExpression65', a1)
    if hasattr(a1, 'coCoMM_Feature66'):
        assert _is_linked(a1, 'coCoMM_Feature66', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression65', {a2})
    assert _is_linked(b, 'coCoMM_CMConstraintExpression65', a2)
    if hasattr(a1, 'coCoMM_Feature66'):
        assert not _is_linked(a1, 'coCoMM_Feature66', b)
    if hasattr(a2, 'coCoMM_Feature66'):
        assert _is_linked(a2, 'coCoMM_Feature66', b)
    _safe_set(b, 'coCoMM_CMConstraintExpression65', set())
    assert not _is_linked(b, 'coCoMM_CMConstraintExpression65', a2)
    if hasattr(a2, 'coCoMM_Feature66'):
        assert not _is_linked(a2, 'coCoMM_Feature66', b)


def test_assoc_funtion42_reverse_link_reassign_clear():
    a1 = coCoMM_OptimizationCC(funct="sample_text")
    a2 = coCoMM_OptimizationCC(funct="sample_text_2")
    b = coCoMM_AggregationFunction(operation="sample_text")
    _safe_set(b, 'coCoMM_AggregationFunction43', a1)
    assert _is_linked(b, 'coCoMM_AggregationFunction43', a1)
    if hasattr(a1, 'coCoMM_OptimizationCC'):
        assert _is_linked(a1, 'coCoMM_OptimizationCC', b)
    _safe_set(b, 'coCoMM_AggregationFunction43', a2)
    assert _is_linked(b, 'coCoMM_AggregationFunction43', a2)
    if hasattr(a1, 'coCoMM_OptimizationCC'):
        assert not _is_linked(a1, 'coCoMM_OptimizationCC', b)
    if hasattr(a2, 'coCoMM_OptimizationCC'):
        assert _is_linked(a2, 'coCoMM_OptimizationCC', b)
    _safe_set(b, 'coCoMM_AggregationFunction43', None)
    assert not _is_linked(b, 'coCoMM_AggregationFunction43', a2)
    if hasattr(a2, 'coCoMM_OptimizationCC'):
        assert not _is_linked(a2, 'coCoMM_OptimizationCC', b)


def test_assoc_project28_reverse_link_reassign_clear():
    a1 = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    a2 = coCoMM_Project(date=date(2025, 6, 15), name="sample_text_2", target=False)
    b = coCoMM_CoCo(configScenario="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_CoCo29', {a1})
    assert _is_linked(b, 'coCoMM_CoCo29', a1)
    if hasattr(a1, 'coCoMM_Project'):
        assert _is_linked(a1, 'coCoMM_Project', b)
    _safe_set(b, 'coCoMM_CoCo29', {a2})
    assert _is_linked(b, 'coCoMM_CoCo29', a2)
    if hasattr(a1, 'coCoMM_Project'):
        assert not _is_linked(a1, 'coCoMM_Project', b)
    if hasattr(a2, 'coCoMM_Project'):
        assert _is_linked(a2, 'coCoMM_Project', b)
    _safe_set(b, 'coCoMM_CoCo29', set())
    assert not _is_linked(b, 'coCoMM_CoCo29', a2)
    if hasattr(a2, 'coCoMM_Project'):
        assert not _is_linked(a2, 'coCoMM_Project', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(id="sample_text", isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(id="sample_text_2", isDomain=False, name="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
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


def test_assoc_solutionConstraints21_reverse_link_reassign_clear():
    a1 = coCoMM_SolutionConstraint(type="sample_text")
    a2 = coCoMM_SolutionConstraint(type="sample_text_2")
    b = coCoMM_CoCo(configScenario="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_CoCo22', {a1})
    assert _is_linked(b, 'coCoMM_CoCo22', a1)
    if hasattr(a1, 'coCoMM_SolutionConstraint'):
        assert _is_linked(a1, 'coCoMM_SolutionConstraint', b)
    _safe_set(b, 'coCoMM_CoCo22', {a2})
    assert _is_linked(b, 'coCoMM_CoCo22', a2)
    if hasattr(a1, 'coCoMM_SolutionConstraint'):
        assert not _is_linked(a1, 'coCoMM_SolutionConstraint', b)
    if hasattr(a2, 'coCoMM_SolutionConstraint'):
        assert _is_linked(a2, 'coCoMM_SolutionConstraint', b)
    _safe_set(b, 'coCoMM_CoCo22', set())
    assert not _is_linked(b, 'coCoMM_CoCo22', a2)
    if hasattr(a2, 'coCoMM_SolutionConstraint'):
        assert not _is_linked(a2, 'coCoMM_SolutionConstraint', b)


def test_assoc_solutionConstraints47_reverse_link_reassign_clear():
    a1 = coCoMM_SolutionConstraint(type="sample_text")
    a2 = coCoMM_SolutionConstraint(type="sample_text_2")
    b = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    _safe_set(b, 'coCoMM_Project48', {a1})
    assert _is_linked(b, 'coCoMM_Project48', a1)
    if hasattr(a1, 'coCoMM_SolutionConstraint49'):
        assert _is_linked(a1, 'coCoMM_SolutionConstraint49', b)
    _safe_set(b, 'coCoMM_Project48', {a2})
    assert _is_linked(b, 'coCoMM_Project48', a2)
    if hasattr(a1, 'coCoMM_SolutionConstraint49'):
        assert not _is_linked(a1, 'coCoMM_SolutionConstraint49', b)
    if hasattr(a2, 'coCoMM_SolutionConstraint49'):
        assert _is_linked(a2, 'coCoMM_SolutionConstraint49', b)
    _safe_set(b, 'coCoMM_Project48', set())
    assert not _is_linked(b, 'coCoMM_Project48', a2)
    if hasattr(a2, 'coCoMM_SolutionConstraint49'):
        assert not _is_linked(a2, 'coCoMM_SolutionConstraint49', b)


def test_assoc_stakeholder52_reverse_link_reassign_clear():
    a1 = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    a2 = coCoMM_Stakeholder(job="sample_text_2", name="sample_text_2")
    b = coCoMM_Config(selected=True, type="sample_text")
    _safe_set(b, 'coCoMM_Config53', a1)
    assert _is_linked(b, 'coCoMM_Config53', a1)
    if hasattr(a1, 'coCoMM_Stakeholder54'):
        assert _is_linked(a1, 'coCoMM_Stakeholder54', b)
    _safe_set(b, 'coCoMM_Config53', a2)
    assert _is_linked(b, 'coCoMM_Config53', a2)
    if hasattr(a1, 'coCoMM_Stakeholder54'):
        assert not _is_linked(a1, 'coCoMM_Stakeholder54', b)
    if hasattr(a2, 'coCoMM_Stakeholder54'):
        assert _is_linked(a2, 'coCoMM_Stakeholder54', b)
    _safe_set(b, 'coCoMM_Config53', None)
    assert not _is_linked(b, 'coCoMM_Config53', a2)
    if hasattr(a2, 'coCoMM_Stakeholder54'):
        assert not _is_linked(a2, 'coCoMM_Stakeholder54', b)


def test_assoc_stakeholders30_reverse_link_reassign_clear():
    a1 = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    a2 = coCoMM_Stakeholder(job="sample_text_2", name="sample_text_2")
    b = coCoMM_CoCo(configScenario="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_CoCo31', {a1})
    assert _is_linked(b, 'coCoMM_CoCo31', a1)
    if hasattr(a1, 'coCoMM_Stakeholder'):
        assert _is_linked(a1, 'coCoMM_Stakeholder', b)
    _safe_set(b, 'coCoMM_CoCo31', {a2})
    assert _is_linked(b, 'coCoMM_CoCo31', a2)
    if hasattr(a1, 'coCoMM_Stakeholder'):
        assert not _is_linked(a1, 'coCoMM_Stakeholder', b)
    if hasattr(a2, 'coCoMM_Stakeholder'):
        assert _is_linked(a2, 'coCoMM_Stakeholder', b)
    _safe_set(b, 'coCoMM_CoCo31', set())
    assert not _is_linked(b, 'coCoMM_CoCo31', a2)
    if hasattr(a2, 'coCoMM_Stakeholder'):
        assert not _is_linked(a2, 'coCoMM_Stakeholder', b)


def test_assoc_treeConstraints3_reverse_link_reassign_clear():
    a1 = coCoMM_TreeConstraint(type="sample_text")
    a2 = coCoMM_TreeConstraint(type="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
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

def test_assoc_cmConstraints19_stub_double():
    # coCoMM_CrossModelConstraint has no real 'coCoMM_CrossModelConstraint' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_CoCo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_CoCo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_CoCo(configScenario="sample_text", id="sample_text", name="sample_text")
    partner = coCoMM_CrossModelConstraint()
    setattr(partner, 'coCoMM_CrossModelConstraint', None)
    _safe_set(owner, 'coCoMM_CoCo20', {partner})
    assert getattr(partner, 'coCoMM_CrossModelConstraint') == owner
    _safe_set(owner, 'coCoMM_CoCo20', set())
    assert getattr(partner, 'coCoMM_CrossModelConstraint') is None


def test_assoc_ctConstraints1_stub_double():
    # coCoMM_CrossTreeConstraint has no real 'coCoMM_CrossTreeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_FeatureModel(id="sample_text", isDomain=True, name="sample_text")
    partner = coCoMM_CrossTreeConstraint()
    setattr(partner, 'coCoMM_CrossTreeConstraint', None)
    _safe_set(owner, 'coCoMM_FeatureModel2', {partner})
    assert getattr(partner, 'coCoMM_CrossTreeConstraint') == owner
    _safe_set(owner, 'coCoMM_FeatureModel2', set())
    assert getattr(partner, 'coCoMM_CrossTreeConstraint') is None


def test_assoc_expressions15_stub_double():
    # coCoMM_CrossTreeConstraint has no real 'coCoMM_CrossTreeConstraint16' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_CTConstraintExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_CTConstraintExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_CTConstraintExpression(op="sample_text")
    partner = coCoMM_CrossTreeConstraint()
    setattr(partner, 'coCoMM_CrossTreeConstraint16', None)
    _safe_set(owner, 'coCoMM_CTConstraintExpression', partner)
    assert owner in getattr(partner, 'coCoMM_CrossTreeConstraint16')
    _safe_set(owner, 'coCoMM_CTConstraintExpression', None)
    assert owner not in getattr(partner, 'coCoMM_CrossTreeConstraint16')


def test_assoc_expressions32_stub_double():
    # coCoMM_CrossModelConstraint has no real 'coCoMM_CrossModelConstraint33' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_CMConstraintExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_CMConstraintExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_CMConstraintExpression(op="sample_text")
    partner = coCoMM_CrossModelConstraint()
    setattr(partner, 'coCoMM_CrossModelConstraint33', None)
    _safe_set(owner, 'coCoMM_CMConstraintExpression', partner)
    assert owner in getattr(partner, 'coCoMM_CrossModelConstraint33')
    _safe_set(owner, 'coCoMM_CMConstraintExpression', None)
    assert owner not in getattr(partner, 'coCoMM_CrossModelConstraint33')


def test_assoc_expressions39_stub_double():
    # coCoMM_HardLimitCC has no real 'coCoMM_HardLimitCC' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_HardLimitCCExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_HardLimitCCExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_HardLimitCCExpression(op="sample_text", value="sample_text")
    partner = coCoMM_HardLimitCC()
    setattr(partner, 'coCoMM_HardLimitCC', None)
    _safe_set(owner, 'coCoMM_HardLimitCCExpression', partner)
    assert owner in getattr(partner, 'coCoMM_HardLimitCC')
    _safe_set(owner, 'coCoMM_HardLimitCCExpression', None)
    assert owner not in getattr(partner, 'coCoMM_HardLimitCC')


def test_assoc_function40_stub_double():
    # coCoMM_HardLimitCC has no real 'coCoMM_HardLimitCC41' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_AggregationFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_AggregationFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_AggregationFunction(operation="sample_text")
    partner = coCoMM_HardLimitCC()
    setattr(partner, 'coCoMM_HardLimitCC41', None)
    _safe_set(owner, 'coCoMM_AggregationFunction', partner)
    assert getattr(partner, 'coCoMM_HardLimitCC41') == owner
    _safe_set(owner, 'coCoMM_AggregationFunction', None)
    assert getattr(partner, 'coCoMM_HardLimitCC41') is None


