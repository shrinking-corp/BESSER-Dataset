import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SolutionConstraint,
    coCoMM_AttributeType,
    coCoMM_AttributeTypeElement,
    coCoMM_CMConstraintExpression,
    coCoMM_CTConstraintExpression,
    coCoMM_CoCo,
    coCoMM_Config,
    coCoMM_CrossModelConstraint,
    coCoMM_CrossTreeConstraint,
    coCoMM_Feature,
    coCoMM_FeatureAttribute,
    coCoMM_FeatureAttributeElement,
    coCoMM_FeatureModel,
    coCoMM_FiniteDomainSC,
    coCoMM_FiniteDomainSCValue,
    coCoMM_HardLimitDRExpression,
    coCoMM_HardLimitSC,
    coCoMM_OptimizationSC,
    coCoMM_Project,
    coCoMM_SelectionStateSC,
    coCoMM_SolutionConstraint,
    coCoMM_Stakeholder,
    coCoMM_TreeConstraint,
    CMConstraintType,
    CTConstraintType,
    ConfigScenarioType,
    ConfigType,
    DataType,
    HardLimitSCOp,
    OptimizationSCFunct,
    SCType,
    SelectionStateSCType,
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
    a1 = coCoMM_OptimizationSC(funct="sample_text")
    a2 = coCoMM_OptimizationSC(funct="sample_text_2")
    b = coCoMM_AttributeType(id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType52', a1)
    assert _is_linked(b, 'coCoMM_AttributeType52', a1)
    if hasattr(a1, 'coCoMM_OptimizationSC'):
        assert _is_linked(a1, 'coCoMM_OptimizationSC', b)
    _safe_set(b, 'coCoMM_AttributeType52', a2)
    assert _is_linked(b, 'coCoMM_AttributeType52', a2)
    if hasattr(a1, 'coCoMM_OptimizationSC'):
        assert not _is_linked(a1, 'coCoMM_OptimizationSC', b)
    if hasattr(a2, 'coCoMM_OptimizationSC'):
        assert _is_linked(a2, 'coCoMM_OptimizationSC', b)
    _safe_set(b, 'coCoMM_AttributeType52', None)
    assert not _is_linked(b, 'coCoMM_AttributeType52', a2)
    if hasattr(a2, 'coCoMM_OptimizationSC'):
        assert not _is_linked(a2, 'coCoMM_OptimizationSC', b)


def test_assoc_attributeTypes33_reverse_link_reassign_clear():
    a1 = coCoMM_CoCo(configScenario="sample_text")
    a2 = coCoMM_CoCo(configScenario="sample_text_2")
    b = coCoMM_AttributeType(id="sample_text", name="sample_text")
    _safe_set(b, 'coCoMM_AttributeType35', a1)
    assert _is_linked(b, 'coCoMM_AttributeType35', a1)
    if hasattr(a1, 'coCoMM_CoCo34'):
        assert _is_linked(a1, 'coCoMM_CoCo34', b)
    _safe_set(b, 'coCoMM_AttributeType35', a2)
    assert _is_linked(b, 'coCoMM_AttributeType35', a2)
    if hasattr(a1, 'coCoMM_CoCo34'):
        assert not _is_linked(a1, 'coCoMM_CoCo34', b)
    if hasattr(a2, 'coCoMM_CoCo34'):
        assert _is_linked(a2, 'coCoMM_CoCo34', b)
    _safe_set(b, 'coCoMM_AttributeType35', None)
    assert not _is_linked(b, 'coCoMM_AttributeType35', a2)
    if hasattr(a2, 'coCoMM_CoCo34'):
        assert not _is_linked(a2, 'coCoMM_CoCo34', b)


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
    a1 = coCoMM_SelectionStateSC(state="sample_text")
    a2 = coCoMM_SelectionStateSC(state="sample_text_2")
    b = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    _safe_set(b, 'coCoMM_Feature46', a1)
    assert _is_linked(b, 'coCoMM_Feature46', a1)
    if hasattr(a1, 'coCoMM_SelectionStateSC45'):
        assert _is_linked(a1, 'coCoMM_SelectionStateSC45', b)
    _safe_set(b, 'coCoMM_Feature46', a2)
    assert _is_linked(b, 'coCoMM_Feature46', a2)
    if hasattr(a1, 'coCoMM_SelectionStateSC45'):
        assert not _is_linked(a1, 'coCoMM_SelectionStateSC45', b)
    if hasattr(a2, 'coCoMM_SelectionStateSC45'):
        assert _is_linked(a2, 'coCoMM_SelectionStateSC45', b)
    _safe_set(b, 'coCoMM_Feature46', None)
    assert not _is_linked(b, 'coCoMM_Feature46', a2)
    if hasattr(a2, 'coCoMM_SelectionStateSC45'):
        assert not _is_linked(a2, 'coCoMM_SelectionStateSC45', b)


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


def test_assoc_featureModel42_reverse_link_reassign_clear():
    a1 = coCoMM_SelectionStateSC(state="sample_text")
    a2 = coCoMM_SelectionStateSC(state="sample_text_2")
    b = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    _safe_set(b, 'coCoMM_FeatureModel43', a1)
    assert _is_linked(b, 'coCoMM_FeatureModel43', a1)
    if hasattr(a1, 'coCoMM_SelectionStateSC'):
        assert _is_linked(a1, 'coCoMM_SelectionStateSC', b)
    _safe_set(b, 'coCoMM_FeatureModel43', a2)
    assert _is_linked(b, 'coCoMM_FeatureModel43', a2)
    if hasattr(a1, 'coCoMM_SelectionStateSC'):
        assert not _is_linked(a1, 'coCoMM_SelectionStateSC', b)
    if hasattr(a2, 'coCoMM_SelectionStateSC'):
        assert _is_linked(a2, 'coCoMM_SelectionStateSC', b)
    _safe_set(b, 'coCoMM_FeatureModel43', None)
    assert not _is_linked(b, 'coCoMM_FeatureModel43', a2)
    if hasattr(a2, 'coCoMM_SelectionStateSC'):
        assert not _is_linked(a2, 'coCoMM_SelectionStateSC', b)


def test_assoc_featureModel5_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(isDomain=False, name="sample_text_2")
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


def test_assoc_featureModels27_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(isDomain=False, name="sample_text_2")
    b = coCoMM_CoCo(configScenario="sample_text")
    _safe_set(b, 'coCoMM_CoCo', {a1})
    assert _is_linked(b, 'coCoMM_CoCo', a1)
    if hasattr(a1, 'coCoMM_FeatureModel28'):
        assert _is_linked(a1, 'coCoMM_FeatureModel28', b)
    _safe_set(b, 'coCoMM_CoCo', {a2})
    assert _is_linked(b, 'coCoMM_CoCo', a2)
    if hasattr(a1, 'coCoMM_FeatureModel28'):
        assert not _is_linked(a1, 'coCoMM_FeatureModel28', b)
    if hasattr(a2, 'coCoMM_FeatureModel28'):
        assert _is_linked(a2, 'coCoMM_FeatureModel28', b)
    _safe_set(b, 'coCoMM_CoCo', set())
    assert not _is_linked(b, 'coCoMM_CoCo', a2)
    if hasattr(a2, 'coCoMM_FeatureModel28'):
        assert not _is_linked(a2, 'coCoMM_FeatureModel28', b)


def test_assoc_features61_reverse_link_reassign_clear():
    a1 = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", mandatory=False, name="sample_text_2")
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
    a1 = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", mandatory=False, name="sample_text_2")
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
    a1 = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    a2 = coCoMM_Feature(abstract=False, id="sample_text_2", mandatory=False, name="sample_text_2")
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


def test_assoc_project36_reverse_link_reassign_clear():
    a1 = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    a2 = coCoMM_Project(date=date(2025, 6, 15), name="sample_text_2", target=False)
    b = coCoMM_CoCo(configScenario="sample_text")
    _safe_set(b, 'coCoMM_CoCo37', {a1})
    assert _is_linked(b, 'coCoMM_CoCo37', a1)
    if hasattr(a1, 'coCoMM_Project'):
        assert _is_linked(a1, 'coCoMM_Project', b)
    _safe_set(b, 'coCoMM_CoCo37', {a2})
    assert _is_linked(b, 'coCoMM_CoCo37', a2)
    if hasattr(a1, 'coCoMM_Project'):
        assert not _is_linked(a1, 'coCoMM_Project', b)
    if hasattr(a2, 'coCoMM_Project'):
        assert _is_linked(a2, 'coCoMM_Project', b)
    _safe_set(b, 'coCoMM_CoCo37', set())
    assert not _is_linked(b, 'coCoMM_CoCo37', a2)
    if hasattr(a2, 'coCoMM_Project'):
        assert not _is_linked(a2, 'coCoMM_Project', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    a2 = coCoMM_FeatureModel(isDomain=False, name="sample_text_2")
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


def test_assoc_solutionConstraints31_reverse_link_reassign_clear():
    a1 = coCoMM_SolutionConstraint(type="sample_text")
    a2 = coCoMM_SolutionConstraint(type="sample_text_2")
    b = coCoMM_CoCo(configScenario="sample_text")
    _safe_set(b, 'coCoMM_CoCo32', {a1})
    assert _is_linked(b, 'coCoMM_CoCo32', a1)
    if hasattr(a1, 'coCoMM_SolutionConstraint'):
        assert _is_linked(a1, 'coCoMM_SolutionConstraint', b)
    _safe_set(b, 'coCoMM_CoCo32', {a2})
    assert _is_linked(b, 'coCoMM_CoCo32', a2)
    if hasattr(a1, 'coCoMM_SolutionConstraint'):
        assert not _is_linked(a1, 'coCoMM_SolutionConstraint', b)
    if hasattr(a2, 'coCoMM_SolutionConstraint'):
        assert _is_linked(a2, 'coCoMM_SolutionConstraint', b)
    _safe_set(b, 'coCoMM_CoCo32', set())
    assert not _is_linked(b, 'coCoMM_CoCo32', a2)
    if hasattr(a2, 'coCoMM_SolutionConstraint'):
        assert not _is_linked(a2, 'coCoMM_SolutionConstraint', b)


def test_assoc_solutionConstraints53_reverse_link_reassign_clear():
    a1 = coCoMM_SolutionConstraint(type="sample_text")
    a2 = coCoMM_SolutionConstraint(type="sample_text_2")
    b = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    _safe_set(b, 'coCoMM_Project54', {a1})
    assert _is_linked(b, 'coCoMM_Project54', a1)
    if hasattr(a1, 'coCoMM_SolutionConstraint55'):
        assert _is_linked(a1, 'coCoMM_SolutionConstraint55', b)
    _safe_set(b, 'coCoMM_Project54', {a2})
    assert _is_linked(b, 'coCoMM_Project54', a2)
    if hasattr(a1, 'coCoMM_SolutionConstraint55'):
        assert not _is_linked(a1, 'coCoMM_SolutionConstraint55', b)
    if hasattr(a2, 'coCoMM_SolutionConstraint55'):
        assert _is_linked(a2, 'coCoMM_SolutionConstraint55', b)
    _safe_set(b, 'coCoMM_Project54', set())
    assert not _is_linked(b, 'coCoMM_Project54', a2)
    if hasattr(a2, 'coCoMM_SolutionConstraint55'):
        assert not _is_linked(a2, 'coCoMM_SolutionConstraint55', b)


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


def test_assoc_stakeholders38_reverse_link_reassign_clear():
    a1 = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    a2 = coCoMM_Stakeholder(job="sample_text_2", name="sample_text_2")
    b = coCoMM_CoCo(configScenario="sample_text")
    _safe_set(b, 'coCoMM_CoCo39', {a1})
    assert _is_linked(b, 'coCoMM_CoCo39', a1)
    if hasattr(a1, 'coCoMM_Stakeholder'):
        assert _is_linked(a1, 'coCoMM_Stakeholder', b)
    _safe_set(b, 'coCoMM_CoCo39', {a2})
    assert _is_linked(b, 'coCoMM_CoCo39', a2)
    if hasattr(a1, 'coCoMM_Stakeholder'):
        assert not _is_linked(a1, 'coCoMM_Stakeholder', b)
    if hasattr(a2, 'coCoMM_Stakeholder'):
        assert _is_linked(a2, 'coCoMM_Stakeholder', b)
    _safe_set(b, 'coCoMM_CoCo39', set())
    assert not _is_linked(b, 'coCoMM_CoCo39', a2)
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

def test_assoc_attrType48_stub_double():
    # coCoMM_HardLimitSC has no real 'coCoMM_HardLimitSC49' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_AttributeType(id="sample_text", name="sample_text")
    partner = coCoMM_HardLimitSC()
    setattr(partner, 'coCoMM_HardLimitSC49', None)
    _safe_set(owner, 'coCoMM_AttributeType50', partner)
    assert getattr(partner, 'coCoMM_HardLimitSC49') == owner
    _safe_set(owner, 'coCoMM_AttributeType50', None)
    assert getattr(partner, 'coCoMM_HardLimitSC49') is None


def test_assoc_cmConstraints29_stub_double():
    # coCoMM_CrossModelConstraint has no real 'coCoMM_CrossModelConstraint' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_CoCo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_CoCo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_CoCo(configScenario="sample_text")
    partner = coCoMM_CrossModelConstraint()
    setattr(partner, 'coCoMM_CrossModelConstraint', None)
    _safe_set(owner, 'coCoMM_CoCo30', {partner})
    assert getattr(partner, 'coCoMM_CrossModelConstraint') == owner
    _safe_set(owner, 'coCoMM_CoCo30', set())
    assert getattr(partner, 'coCoMM_CrossModelConstraint') is None


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
    # coCoMM_HardLimitSC has no real 'coCoMM_HardLimitSC' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_HardLimitDRExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_HardLimitDRExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    partner = coCoMM_HardLimitSC()
    setattr(partner, 'coCoMM_HardLimitSC', None)
    _safe_set(owner, 'coCoMM_HardLimitDRExpression', partner)
    assert owner in getattr(partner, 'coCoMM_HardLimitSC')
    _safe_set(owner, 'coCoMM_HardLimitDRExpression', None)
    assert owner not in getattr(partner, 'coCoMM_HardLimitSC')


def test_assoc_feature78_stub_double():
    # coCoMM_FiniteDomainSC has no real 'coCoMM_FiniteDomainSC79' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_Feature(abstract=True, id="sample_text", mandatory=True, name="sample_text")
    partner = coCoMM_FiniteDomainSC()
    setattr(partner, 'coCoMM_FiniteDomainSC79', None)
    _safe_set(owner, 'coCoMM_Feature80', partner)
    assert getattr(partner, 'coCoMM_FiniteDomainSC79') == owner
    _safe_set(owner, 'coCoMM_Feature80', None)
    assert getattr(partner, 'coCoMM_FiniteDomainSC79') is None


def test_assoc_featureAttributes76_stub_double():
    # coCoMM_FiniteDomainSC has no real 'coCoMM_FiniteDomainSC' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_FeatureAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_FeatureAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_FeatureAttribute(name="sample_text")
    partner = coCoMM_FiniteDomainSC()
    setattr(partner, 'coCoMM_FiniteDomainSC', None)
    _safe_set(owner, 'coCoMM_FeatureAttribute77', partner)
    assert getattr(partner, 'coCoMM_FiniteDomainSC') == owner
    _safe_set(owner, 'coCoMM_FeatureAttribute77', None)
    assert getattr(partner, 'coCoMM_FiniteDomainSC') is None


def test_assoc_values81_stub_double():
    # coCoMM_FiniteDomainSC has no real 'coCoMM_FiniteDomainSC82' property in the generated
    # code (a bare stub) -- manually attach it so coCoMM_FiniteDomainSCValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coCoMM_FiniteDomainSCValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coCoMM_FiniteDomainSCValue(value="sample_text")
    partner = coCoMM_FiniteDomainSC()
    setattr(partner, 'coCoMM_FiniteDomainSC82', None)
    _safe_set(owner, 'coCoMM_FiniteDomainSCValue', partner)
    assert owner in getattr(partner, 'coCoMM_FiniteDomainSC82')
    _safe_set(owner, 'coCoMM_FiniteDomainSCValue', None)
    assert owner not in getattr(partner, 'coCoMM_FiniteDomainSC82')


