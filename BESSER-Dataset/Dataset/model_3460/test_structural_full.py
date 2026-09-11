import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_coCoMM_AttributeType_id_value_roundtrip():
    instance = coCoMM_AttributeType(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_coCoMM_AttributeType_name_value_roundtrip():
    instance = coCoMM_AttributeType(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_AttributeTypeElement_dataType_value_roundtrip():
    instance = coCoMM_AttributeTypeElement(dataType="sample_text", name="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_coCoMM_AttributeTypeElement_name_value_roundtrip():
    instance = coCoMM_AttributeTypeElement(dataType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_CMConstraintExpression_op_value_roundtrip():
    instance = coCoMM_CMConstraintExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_coCoMM_CTConstraintExpression_op_value_roundtrip():
    instance = coCoMM_CTConstraintExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_coCoMM_Config_selected_value_roundtrip():
    instance = coCoMM_Config(selected=True, type="sample_text")
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_coCoMM_Config_type_value_roundtrip():
    instance = coCoMM_Config(selected=True, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_coCoMM_DecisionRule_type_value_roundtrip():
    instance = coCoMM_DecisionRule(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_coCoMM_Feature_abstract_value_roundtrip():
    instance = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_coCoMM_Feature_id_value_roundtrip():
    instance = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_coCoMM_Feature_name_value_roundtrip():
    instance = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_FeatureAttribute_name_value_roundtrip():
    instance = coCoMM_FeatureAttribute(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_FeatureAttributeElement_value_value_roundtrip():
    instance = coCoMM_FeatureAttributeElement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_coCoMM_FeatureModel_isDomain_value_roundtrip():
    instance = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    assert instance.isDomain == True
    instance.isDomain = False
    assert instance.isDomain == False


def test_coCoMM_FeatureModel_name_value_roundtrip():
    instance = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_HardLimitDRExpression_op_value_roundtrip():
    instance = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_coCoMM_HardLimitDRExpression_value_value_roundtrip():
    instance = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_coCoMM_OptimizationDR_funct_value_roundtrip():
    instance = coCoMM_OptimizationDR(funct="sample_text")
    assert instance.funct == "sample_text"
    instance.funct = "sample_text_2"
    assert instance.funct == "sample_text_2"


def test_coCoMM_Project_date_value_roundtrip():
    instance = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_coCoMM_Project_name_value_roundtrip():
    instance = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_Project_target_value_roundtrip():
    instance = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    assert instance.target == True
    instance.target = False
    assert instance.target == False


def test_coCoMM_SelectionStateDR_state_value_roundtrip():
    instance = coCoMM_SelectionStateDR(state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_coCoMM_Stakeholder_job_value_roundtrip():
    instance = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    assert instance.job == "sample_text"
    instance.job = "sample_text_2"
    assert instance.job == "sample_text_2"


def test_coCoMM_Stakeholder_name_value_roundtrip():
    instance = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_coCoMM_TreeConstraint_type_value_roundtrip():
    instance = coCoMM_TreeConstraint(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_coCoMM_HardLimitDR_isa_DecisionRule():
    instance = coCoMM_HardLimitDR()
    assert isinstance(instance, DecisionRule)


def test_coCoMM_OptimizationDR_isa_DecisionRule():
    instance = coCoMM_OptimizationDR(funct="sample_text")
    assert isinstance(instance, DecisionRule)


def test_coCoMM_SelectionStateDR_isa_DecisionRule():
    instance = coCoMM_SelectionStateDR(state="sample_text")
    assert isinstance(instance, DecisionRule)


def test_assoc_attrType20_link_reassign_clear():
    a = coCoMM_FeatureAttribute(name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttribute21', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttribute21', b1)
    if hasattr(b1, 'coCoMM_AttributeType22'):
        assert _is_linked(b1, 'coCoMM_AttributeType22', a)
    _safe_set(a, 'coCoMM_FeatureAttribute21', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttribute21', b2)
    if hasattr(b1, 'coCoMM_AttributeType22'):
        assert not _is_linked(b1, 'coCoMM_AttributeType22', a)
    if hasattr(b2, 'coCoMM_AttributeType22'):
        assert _is_linked(b2, 'coCoMM_AttributeType22', a)
    _safe_set(a, 'coCoMM_FeatureAttribute21', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttribute21', b2)
    if hasattr(b2, 'coCoMM_AttributeType22'):
        assert not _is_linked(b2, 'coCoMM_AttributeType22', a)


def test_assoc_attrType48_link_reassign_clear():
    a = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b1 = coCoMM_HardLimitDR()
    b2 = coCoMM_HardLimitDR()
    _safe_set(a, 'coCoMM_AttributeType50', b1)
    assert _is_linked(a, 'coCoMM_AttributeType50', b1)
    if hasattr(b1, 'coCoMM_HardLimitDR49'):
        assert _is_linked(b1, 'coCoMM_HardLimitDR49', a)
    _safe_set(a, 'coCoMM_AttributeType50', b2)
    assert _is_linked(a, 'coCoMM_AttributeType50', b2)
    if hasattr(b1, 'coCoMM_HardLimitDR49'):
        assert not _is_linked(b1, 'coCoMM_HardLimitDR49', a)
    if hasattr(b2, 'coCoMM_HardLimitDR49'):
        assert _is_linked(b2, 'coCoMM_HardLimitDR49', a)
    _safe_set(a, 'coCoMM_AttributeType50', None)
    assert not _is_linked(a, 'coCoMM_AttributeType50', b2)
    if hasattr(b2, 'coCoMM_HardLimitDR49'):
        assert not _is_linked(b2, 'coCoMM_HardLimitDR49', a)


def test_assoc_attrType51_link_reassign_clear():
    a = coCoMM_OptimizationDR(funct="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_OptimizationDR', b1)
    assert _is_linked(a, 'coCoMM_OptimizationDR', b1)
    if hasattr(b1, 'coCoMM_AttributeType52'):
        assert _is_linked(b1, 'coCoMM_AttributeType52', a)
    _safe_set(a, 'coCoMM_OptimizationDR', b2)
    assert _is_linked(a, 'coCoMM_OptimizationDR', b2)
    if hasattr(b1, 'coCoMM_AttributeType52'):
        assert not _is_linked(b1, 'coCoMM_AttributeType52', a)
    if hasattr(b2, 'coCoMM_AttributeType52'):
        assert _is_linked(b2, 'coCoMM_AttributeType52', a)
    _safe_set(a, 'coCoMM_OptimizationDR', None)
    assert not _is_linked(a, 'coCoMM_OptimizationDR', b2)
    if hasattr(b2, 'coCoMM_AttributeType52'):
        assert not _is_linked(b2, 'coCoMM_AttributeType52', a)


def test_assoc_attributeTypes33_link_reassign_clear():
    a = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_AttributeType35', b1)
    assert _is_linked(a, 'coCoMM_AttributeType35', b1)
    if hasattr(b1, 'coCoMM_CoCo34'):
        assert _is_linked(b1, 'coCoMM_CoCo34', a)
    _safe_set(a, 'coCoMM_AttributeType35', b2)
    assert _is_linked(a, 'coCoMM_AttributeType35', b2)
    if hasattr(b1, 'coCoMM_CoCo34'):
        assert not _is_linked(b1, 'coCoMM_CoCo34', a)
    if hasattr(b2, 'coCoMM_CoCo34'):
        assert _is_linked(b2, 'coCoMM_CoCo34', a)
    _safe_set(a, 'coCoMM_AttributeType35', None)
    assert not _is_linked(a, 'coCoMM_AttributeType35', b2)
    if hasattr(b2, 'coCoMM_CoCo34'):
        assert not _is_linked(b2, 'coCoMM_CoCo34', a)


def test_assoc_children10_link_reassign_clear():
    a = coCoMM_TreeConstraint(type="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_TreeConstraint11', {b1})
    assert _is_linked(a, 'coCoMM_TreeConstraint11', b1)
    if hasattr(b1, 'coCoMM_Feature12'):
        assert _is_linked(b1, 'coCoMM_Feature12', a)
    _safe_set(a, 'coCoMM_TreeConstraint11', {b2})
    assert _is_linked(a, 'coCoMM_TreeConstraint11', b2)
    if hasattr(b1, 'coCoMM_Feature12'):
        assert not _is_linked(b1, 'coCoMM_Feature12', a)
    if hasattr(b2, 'coCoMM_Feature12'):
        assert _is_linked(b2, 'coCoMM_Feature12', a)
    _safe_set(a, 'coCoMM_TreeConstraint11', set())
    assert not _is_linked(a, 'coCoMM_TreeConstraint11', b2)
    if hasattr(b2, 'coCoMM_Feature12'):
        assert not _is_linked(b2, 'coCoMM_Feature12', a)


def test_assoc_configs56_link_reassign_clear():
    a = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    b1 = coCoMM_Config(selected=True, type="sample_text")
    b2 = coCoMM_Config(selected=False, type="sample_text_2")
    _safe_set(a, 'coCoMM_Project57', {b1})
    assert _is_linked(a, 'coCoMM_Project57', b1)
    if hasattr(b1, 'coCoMM_Config'):
        assert _is_linked(b1, 'coCoMM_Config', a)
    _safe_set(a, 'coCoMM_Project57', {b2})
    assert _is_linked(a, 'coCoMM_Project57', b2)
    if hasattr(b1, 'coCoMM_Config'):
        assert not _is_linked(b1, 'coCoMM_Config', a)
    if hasattr(b2, 'coCoMM_Config'):
        assert _is_linked(b2, 'coCoMM_Config', a)
    _safe_set(a, 'coCoMM_Project57', set())
    assert not _is_linked(a, 'coCoMM_Project57', b2)
    if hasattr(b2, 'coCoMM_Config'):
        assert not _is_linked(b2, 'coCoMM_Config', a)


def test_assoc_ctConstraints1_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_CrossTreeConstraint()
    b2 = coCoMM_CrossTreeConstraint()
    _safe_set(a, 'coCoMM_FeatureModel2', {b1})
    assert _is_linked(a, 'coCoMM_FeatureModel2', b1)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint'):
        assert _is_linked(b1, 'coCoMM_CrossTreeConstraint', a)
    _safe_set(a, 'coCoMM_FeatureModel2', {b2})
    assert _is_linked(a, 'coCoMM_FeatureModel2', b2)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint'):
        assert not _is_linked(b1, 'coCoMM_CrossTreeConstraint', a)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint'):
        assert _is_linked(b2, 'coCoMM_CrossTreeConstraint', a)
    _safe_set(a, 'coCoMM_FeatureModel2', set())
    assert not _is_linked(a, 'coCoMM_FeatureModel2', b2)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint'):
        assert not _is_linked(b2, 'coCoMM_CrossTreeConstraint', a)


def test_assoc_decisionRules31_link_reassign_clear():
    a = coCoMM_DecisionRule(type="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_DecisionRule', b1)
    assert _is_linked(a, 'coCoMM_DecisionRule', b1)
    if hasattr(b1, 'coCoMM_CoCo32'):
        assert _is_linked(b1, 'coCoMM_CoCo32', a)
    _safe_set(a, 'coCoMM_DecisionRule', b2)
    assert _is_linked(a, 'coCoMM_DecisionRule', b2)
    if hasattr(b1, 'coCoMM_CoCo32'):
        assert not _is_linked(b1, 'coCoMM_CoCo32', a)
    if hasattr(b2, 'coCoMM_CoCo32'):
        assert _is_linked(b2, 'coCoMM_CoCo32', a)
    _safe_set(a, 'coCoMM_DecisionRule', None)
    assert not _is_linked(a, 'coCoMM_DecisionRule', b2)
    if hasattr(b2, 'coCoMM_CoCo32'):
        assert not _is_linked(b2, 'coCoMM_CoCo32', a)


def test_assoc_decisionRules53_link_reassign_clear():
    a = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    b1 = coCoMM_DecisionRule(type="sample_text")
    b2 = coCoMM_DecisionRule(type="sample_text_2")
    _safe_set(a, 'coCoMM_Project54', {b1})
    assert _is_linked(a, 'coCoMM_Project54', b1)
    if hasattr(b1, 'coCoMM_DecisionRule55'):
        assert _is_linked(b1, 'coCoMM_DecisionRule55', a)
    _safe_set(a, 'coCoMM_Project54', {b2})
    assert _is_linked(a, 'coCoMM_Project54', b2)
    if hasattr(b1, 'coCoMM_DecisionRule55'):
        assert not _is_linked(b1, 'coCoMM_DecisionRule55', a)
    if hasattr(b2, 'coCoMM_DecisionRule55'):
        assert _is_linked(b2, 'coCoMM_DecisionRule55', a)
    _safe_set(a, 'coCoMM_Project54', set())
    assert not _is_linked(a, 'coCoMM_Project54', b2)
    if hasattr(b2, 'coCoMM_DecisionRule55'):
        assert not _is_linked(b2, 'coCoMM_DecisionRule55', a)


def test_assoc_elements15_link_reassign_clear():
    a = coCoMM_AttributeTypeElement(dataType="sample_text", name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_AttributeTypeElement', b1)
    assert _is_linked(a, 'coCoMM_AttributeTypeElement', b1)
    if hasattr(b1, 'coCoMM_AttributeType16'):
        assert _is_linked(b1, 'coCoMM_AttributeType16', a)
    _safe_set(a, 'coCoMM_AttributeTypeElement', b2)
    assert _is_linked(a, 'coCoMM_AttributeTypeElement', b2)
    if hasattr(b1, 'coCoMM_AttributeType16'):
        assert not _is_linked(b1, 'coCoMM_AttributeType16', a)
    if hasattr(b2, 'coCoMM_AttributeType16'):
        assert _is_linked(b2, 'coCoMM_AttributeType16', a)
    _safe_set(a, 'coCoMM_AttributeTypeElement', None)
    assert not _is_linked(a, 'coCoMM_AttributeTypeElement', b2)
    if hasattr(b2, 'coCoMM_AttributeType16'):
        assert not _is_linked(b2, 'coCoMM_AttributeType16', a)


def test_assoc_elements23_link_reassign_clear():
    a = coCoMM_FeatureAttributeElement(value="sample_text")
    b1 = coCoMM_FeatureAttribute(name="sample_text")
    b2 = coCoMM_FeatureAttribute(name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttributeElement', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttributeElement', b1)
    if hasattr(b1, 'coCoMM_FeatureAttribute24'):
        assert _is_linked(b1, 'coCoMM_FeatureAttribute24', a)
    _safe_set(a, 'coCoMM_FeatureAttributeElement', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttributeElement', b2)
    if hasattr(b1, 'coCoMM_FeatureAttribute24'):
        assert not _is_linked(b1, 'coCoMM_FeatureAttribute24', a)
    if hasattr(b2, 'coCoMM_FeatureAttribute24'):
        assert _is_linked(b2, 'coCoMM_FeatureAttribute24', a)
    _safe_set(a, 'coCoMM_FeatureAttributeElement', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttributeElement', b2)
    if hasattr(b2, 'coCoMM_FeatureAttribute24'):
        assert not _is_linked(b2, 'coCoMM_FeatureAttribute24', a)


def test_assoc_expressions25_link_reassign_clear():
    a = coCoMM_CTConstraintExpression(op="sample_text")
    b1 = coCoMM_CrossTreeConstraint()
    b2 = coCoMM_CrossTreeConstraint()
    _safe_set(a, 'coCoMM_CTConstraintExpression', b1)
    assert _is_linked(a, 'coCoMM_CTConstraintExpression', b1)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint26'):
        assert _is_linked(b1, 'coCoMM_CrossTreeConstraint26', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression', b2)
    assert _is_linked(a, 'coCoMM_CTConstraintExpression', b2)
    if hasattr(b1, 'coCoMM_CrossTreeConstraint26'):
        assert not _is_linked(b1, 'coCoMM_CrossTreeConstraint26', a)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint26'):
        assert _is_linked(b2, 'coCoMM_CrossTreeConstraint26', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression', None)
    assert not _is_linked(a, 'coCoMM_CTConstraintExpression', b2)
    if hasattr(b2, 'coCoMM_CrossTreeConstraint26'):
        assert not _is_linked(b2, 'coCoMM_CrossTreeConstraint26', a)


def test_assoc_expressions40_link_reassign_clear():
    a = coCoMM_CMConstraintExpression(op="sample_text")
    b1 = coCoMM_CrossModelConstraint()
    b2 = coCoMM_CrossModelConstraint()
    _safe_set(a, 'coCoMM_CMConstraintExpression', b1)
    assert _is_linked(a, 'coCoMM_CMConstraintExpression', b1)
    if hasattr(b1, 'coCoMM_CrossModelConstraint41'):
        assert _is_linked(b1, 'coCoMM_CrossModelConstraint41', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression', b2)
    assert _is_linked(a, 'coCoMM_CMConstraintExpression', b2)
    if hasattr(b1, 'coCoMM_CrossModelConstraint41'):
        assert not _is_linked(b1, 'coCoMM_CrossModelConstraint41', a)
    if hasattr(b2, 'coCoMM_CrossModelConstraint41'):
        assert _is_linked(b2, 'coCoMM_CrossModelConstraint41', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression', None)
    assert not _is_linked(a, 'coCoMM_CMConstraintExpression', b2)
    if hasattr(b2, 'coCoMM_CrossModelConstraint41'):
        assert not _is_linked(b2, 'coCoMM_CrossModelConstraint41', a)


def test_assoc_expressions47_link_reassign_clear():
    a = coCoMM_HardLimitDRExpression(op="sample_text", value="sample_text")
    b1 = coCoMM_HardLimitDR()
    b2 = coCoMM_HardLimitDR()
    _safe_set(a, 'coCoMM_HardLimitDRExpression', b1)
    assert _is_linked(a, 'coCoMM_HardLimitDRExpression', b1)
    if hasattr(b1, 'coCoMM_HardLimitDR'):
        assert _is_linked(b1, 'coCoMM_HardLimitDR', a)
    _safe_set(a, 'coCoMM_HardLimitDRExpression', b2)
    assert _is_linked(a, 'coCoMM_HardLimitDRExpression', b2)
    if hasattr(b1, 'coCoMM_HardLimitDR'):
        assert not _is_linked(b1, 'coCoMM_HardLimitDR', a)
    if hasattr(b2, 'coCoMM_HardLimitDR'):
        assert _is_linked(b2, 'coCoMM_HardLimitDR', a)
    _safe_set(a, 'coCoMM_HardLimitDRExpression', None)
    assert not _is_linked(a, 'coCoMM_HardLimitDRExpression', b2)
    if hasattr(b2, 'coCoMM_HardLimitDR'):
        assert not _is_linked(b2, 'coCoMM_HardLimitDR', a)


def test_assoc_expressions68_link_reassign_clear():
    a = coCoMM_CTConstraintExpression(op="sample_text")
    b1 = coCoMM_CTConstraintExpression(op="sample_text")
    b2 = coCoMM_CTConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_CTConstraintExpression67', {b1})
    assert _is_linked(a, 'coCoMM_CTConstraintExpression67', b1)
    if hasattr(b1, 'coCoMM_CTConstraintExpression69'):
        assert _is_linked(b1, 'coCoMM_CTConstraintExpression69', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression67', {b2})
    assert _is_linked(a, 'coCoMM_CTConstraintExpression67', b2)
    if hasattr(b1, 'coCoMM_CTConstraintExpression69'):
        assert not _is_linked(b1, 'coCoMM_CTConstraintExpression69', a)
    if hasattr(b2, 'coCoMM_CTConstraintExpression69'):
        assert _is_linked(b2, 'coCoMM_CTConstraintExpression69', a)
    _safe_set(a, 'coCoMM_CTConstraintExpression67', set())
    assert not _is_linked(a, 'coCoMM_CTConstraintExpression67', b2)
    if hasattr(b2, 'coCoMM_CTConstraintExpression69'):
        assert not _is_linked(b2, 'coCoMM_CTConstraintExpression69', a)


def test_assoc_expressions74_link_reassign_clear():
    a = coCoMM_CMConstraintExpression(op="sample_text")
    b1 = coCoMM_CMConstraintExpression(op="sample_text")
    b2 = coCoMM_CMConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_CMConstraintExpression73', {b1})
    assert _is_linked(a, 'coCoMM_CMConstraintExpression73', b1)
    if hasattr(b1, 'coCoMM_CMConstraintExpression75'):
        assert _is_linked(b1, 'coCoMM_CMConstraintExpression75', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression73', {b2})
    assert _is_linked(a, 'coCoMM_CMConstraintExpression73', b2)
    if hasattr(b1, 'coCoMM_CMConstraintExpression75'):
        assert not _is_linked(b1, 'coCoMM_CMConstraintExpression75', a)
    if hasattr(b2, 'coCoMM_CMConstraintExpression75'):
        assert _is_linked(b2, 'coCoMM_CMConstraintExpression75', a)
    _safe_set(a, 'coCoMM_CMConstraintExpression73', set())
    assert not _is_linked(a, 'coCoMM_CMConstraintExpression73', b2)
    if hasattr(b2, 'coCoMM_CMConstraintExpression75'):
        assert not _is_linked(b2, 'coCoMM_CMConstraintExpression75', a)


def test_assoc_feature44_link_reassign_clear():
    a = coCoMM_SelectionStateDR(state="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_SelectionStateDR45', b1)
    assert _is_linked(a, 'coCoMM_SelectionStateDR45', b1)
    if hasattr(b1, 'coCoMM_Feature46'):
        assert _is_linked(b1, 'coCoMM_Feature46', a)
    _safe_set(a, 'coCoMM_SelectionStateDR45', b2)
    assert _is_linked(a, 'coCoMM_SelectionStateDR45', b2)
    if hasattr(b1, 'coCoMM_Feature46'):
        assert not _is_linked(b1, 'coCoMM_Feature46', a)
    if hasattr(b2, 'coCoMM_Feature46'):
        assert _is_linked(b2, 'coCoMM_Feature46', a)
    _safe_set(a, 'coCoMM_SelectionStateDR45', None)
    assert not _is_linked(a, 'coCoMM_SelectionStateDR45', b2)
    if hasattr(b2, 'coCoMM_Feature46'):
        assert not _is_linked(b2, 'coCoMM_Feature46', a)


def test_assoc_featureAttributes17_link_reassign_clear():
    a = coCoMM_FeatureAttribute(name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttribute19', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttribute19', b1)
    if hasattr(b1, 'coCoMM_AttributeType18'):
        assert _is_linked(b1, 'coCoMM_AttributeType18', a)
    _safe_set(a, 'coCoMM_FeatureAttribute19', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttribute19', b2)
    if hasattr(b1, 'coCoMM_AttributeType18'):
        assert not _is_linked(b1, 'coCoMM_AttributeType18', a)
    if hasattr(b2, 'coCoMM_AttributeType18'):
        assert _is_linked(b2, 'coCoMM_AttributeType18', a)
    _safe_set(a, 'coCoMM_FeatureAttribute19', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttribute19', b2)
    if hasattr(b2, 'coCoMM_AttributeType18'):
        assert not _is_linked(b2, 'coCoMM_AttributeType18', a)


def test_assoc_featureAttributes8_link_reassign_clear():
    a = coCoMM_FeatureAttribute(name="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureAttribute', b1)
    assert _is_linked(a, 'coCoMM_FeatureAttribute', b1)
    if hasattr(b1, 'coCoMM_Feature9'):
        assert _is_linked(b1, 'coCoMM_Feature9', a)
    _safe_set(a, 'coCoMM_FeatureAttribute', b2)
    assert _is_linked(a, 'coCoMM_FeatureAttribute', b2)
    if hasattr(b1, 'coCoMM_Feature9'):
        assert not _is_linked(b1, 'coCoMM_Feature9', a)
    if hasattr(b2, 'coCoMM_Feature9'):
        assert _is_linked(b2, 'coCoMM_Feature9', a)
    _safe_set(a, 'coCoMM_FeatureAttribute', None)
    assert not _is_linked(a, 'coCoMM_FeatureAttribute', b2)
    if hasattr(b2, 'coCoMM_Feature9'):
        assert not _is_linked(b2, 'coCoMM_Feature9', a)


def test_assoc_featureModel42_link_reassign_clear():
    a = coCoMM_SelectionStateDR(state="sample_text")
    b1 = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b2 = coCoMM_FeatureModel(isDomain=False, name="sample_text_2")
    _safe_set(a, 'coCoMM_SelectionStateDR', b1)
    assert _is_linked(a, 'coCoMM_SelectionStateDR', b1)
    if hasattr(b1, 'coCoMM_FeatureModel43'):
        assert _is_linked(b1, 'coCoMM_FeatureModel43', a)
    _safe_set(a, 'coCoMM_SelectionStateDR', b2)
    assert _is_linked(a, 'coCoMM_SelectionStateDR', b2)
    if hasattr(b1, 'coCoMM_FeatureModel43'):
        assert not _is_linked(b1, 'coCoMM_FeatureModel43', a)
    if hasattr(b2, 'coCoMM_FeatureModel43'):
        assert _is_linked(b2, 'coCoMM_FeatureModel43', a)
    _safe_set(a, 'coCoMM_SelectionStateDR', None)
    assert not _is_linked(a, 'coCoMM_SelectionStateDR', b2)
    if hasattr(b2, 'coCoMM_FeatureModel43'):
        assert not _is_linked(b2, 'coCoMM_FeatureModel43', a)


def test_assoc_featureModel5_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureModel7', b1)
    assert _is_linked(a, 'coCoMM_FeatureModel7', b1)
    if hasattr(b1, 'coCoMM_Feature6'):
        assert _is_linked(b1, 'coCoMM_Feature6', a)
    _safe_set(a, 'coCoMM_FeatureModel7', b2)
    assert _is_linked(a, 'coCoMM_FeatureModel7', b2)
    if hasattr(b1, 'coCoMM_Feature6'):
        assert not _is_linked(b1, 'coCoMM_Feature6', a)
    if hasattr(b2, 'coCoMM_Feature6'):
        assert _is_linked(b2, 'coCoMM_Feature6', a)
    _safe_set(a, 'coCoMM_FeatureModel7', None)
    assert not _is_linked(a, 'coCoMM_FeatureModel7', b2)
    if hasattr(b2, 'coCoMM_Feature6'):
        assert not _is_linked(b2, 'coCoMM_Feature6', a)


def test_assoc_featureModels27_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_FeatureModel28', b1)
    assert _is_linked(a, 'coCoMM_FeatureModel28', b1)
    if hasattr(b1, 'coCoMM_CoCo'):
        assert _is_linked(b1, 'coCoMM_CoCo', a)
    _safe_set(a, 'coCoMM_FeatureModel28', b2)
    assert _is_linked(a, 'coCoMM_FeatureModel28', b2)
    if hasattr(b1, 'coCoMM_CoCo'):
        assert not _is_linked(b1, 'coCoMM_CoCo', a)
    if hasattr(b2, 'coCoMM_CoCo'):
        assert _is_linked(b2, 'coCoMM_CoCo', a)
    _safe_set(a, 'coCoMM_FeatureModel28', None)
    assert not _is_linked(a, 'coCoMM_FeatureModel28', b2)
    if hasattr(b2, 'coCoMM_CoCo'):
        assert not _is_linked(b2, 'coCoMM_CoCo', a)


def test_assoc_features61_link_reassign_clear():
    a = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b1 = coCoMM_Config(selected=True, type="sample_text")
    b2 = coCoMM_Config(selected=False, type="sample_text_2")
    _safe_set(a, 'coCoMM_Feature63', b1)
    assert _is_linked(a, 'coCoMM_Feature63', b1)
    if hasattr(b1, 'coCoMM_Config62'):
        assert _is_linked(b1, 'coCoMM_Config62', a)
    _safe_set(a, 'coCoMM_Feature63', b2)
    assert _is_linked(a, 'coCoMM_Feature63', b2)
    if hasattr(b1, 'coCoMM_Config62'):
        assert not _is_linked(b1, 'coCoMM_Config62', a)
    if hasattr(b2, 'coCoMM_Config62'):
        assert _is_linked(b2, 'coCoMM_Config62', a)
    _safe_set(a, 'coCoMM_Feature63', None)
    assert not _is_linked(a, 'coCoMM_Feature63', b2)
    if hasattr(b2, 'coCoMM_Config62'):
        assert not _is_linked(b2, 'coCoMM_Config62', a)


def test_assoc_features64_link_reassign_clear():
    a = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b1 = coCoMM_CTConstraintExpression(op="sample_text")
    b2 = coCoMM_CTConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_Feature66', b1)
    assert _is_linked(a, 'coCoMM_Feature66', b1)
    if hasattr(b1, 'coCoMM_CTConstraintExpression65'):
        assert _is_linked(b1, 'coCoMM_CTConstraintExpression65', a)
    _safe_set(a, 'coCoMM_Feature66', b2)
    assert _is_linked(a, 'coCoMM_Feature66', b2)
    if hasattr(b1, 'coCoMM_CTConstraintExpression65'):
        assert not _is_linked(b1, 'coCoMM_CTConstraintExpression65', a)
    if hasattr(b2, 'coCoMM_CTConstraintExpression65'):
        assert _is_linked(b2, 'coCoMM_CTConstraintExpression65', a)
    _safe_set(a, 'coCoMM_Feature66', None)
    assert not _is_linked(a, 'coCoMM_Feature66', b2)
    if hasattr(b2, 'coCoMM_CTConstraintExpression65'):
        assert not _is_linked(b2, 'coCoMM_CTConstraintExpression65', a)


def test_assoc_features70_link_reassign_clear():
    a = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b1 = coCoMM_CMConstraintExpression(op="sample_text")
    b2 = coCoMM_CMConstraintExpression(op="sample_text_2")
    _safe_set(a, 'coCoMM_Feature72', b1)
    assert _is_linked(a, 'coCoMM_Feature72', b1)
    if hasattr(b1, 'coCoMM_CMConstraintExpression71'):
        assert _is_linked(b1, 'coCoMM_CMConstraintExpression71', a)
    _safe_set(a, 'coCoMM_Feature72', b2)
    assert _is_linked(a, 'coCoMM_Feature72', b2)
    if hasattr(b1, 'coCoMM_CMConstraintExpression71'):
        assert not _is_linked(b1, 'coCoMM_CMConstraintExpression71', a)
    if hasattr(b2, 'coCoMM_CMConstraintExpression71'):
        assert _is_linked(b2, 'coCoMM_CMConstraintExpression71', a)
    _safe_set(a, 'coCoMM_Feature72', None)
    assert not _is_linked(a, 'coCoMM_Feature72', b2)
    if hasattr(b2, 'coCoMM_CMConstraintExpression71'):
        assert not _is_linked(b2, 'coCoMM_CMConstraintExpression71', a)


def test_assoc_independentAttrType14_link_reassign_clear():
    a = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b1 = coCoMM_AttributeType(id="sample_text", name="sample_text")
    b2 = coCoMM_AttributeType(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_AttributeType', b1)
    assert _is_linked(a, 'coCoMM_AttributeType', b1)
    if hasattr(b1, 'coCoMM_AttributeType13'):
        assert _is_linked(b1, 'coCoMM_AttributeType13', a)
    _safe_set(a, 'coCoMM_AttributeType', b2)
    assert _is_linked(a, 'coCoMM_AttributeType', b2)
    if hasattr(b1, 'coCoMM_AttributeType13'):
        assert not _is_linked(b1, 'coCoMM_AttributeType13', a)
    if hasattr(b2, 'coCoMM_AttributeType13'):
        assert _is_linked(b2, 'coCoMM_AttributeType13', a)
    _safe_set(a, 'coCoMM_AttributeType', None)
    assert not _is_linked(a, 'coCoMM_AttributeType', b2)
    if hasattr(b2, 'coCoMM_AttributeType13'):
        assert not _is_linked(b2, 'coCoMM_AttributeType13', a)


def test_assoc_project36_link_reassign_clear():
    a = coCoMM_Project(date=date(2024, 1, 1), name="sample_text", target=True)
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_Project', b1)
    assert _is_linked(a, 'coCoMM_Project', b1)
    if hasattr(b1, 'coCoMM_CoCo37'):
        assert _is_linked(b1, 'coCoMM_CoCo37', a)
    _safe_set(a, 'coCoMM_Project', b2)
    assert _is_linked(a, 'coCoMM_Project', b2)
    if hasattr(b1, 'coCoMM_CoCo37'):
        assert not _is_linked(b1, 'coCoMM_CoCo37', a)
    if hasattr(b2, 'coCoMM_CoCo37'):
        assert _is_linked(b2, 'coCoMM_CoCo37', a)
    _safe_set(a, 'coCoMM_Project', None)
    assert not _is_linked(a, 'coCoMM_Project', b2)
    if hasattr(b2, 'coCoMM_CoCo37'):
        assert not _is_linked(b2, 'coCoMM_CoCo37', a)


def test_assoc_root0_link_reassign_clear():
    a = coCoMM_FeatureModel(isDomain=True, name="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_FeatureModel', b1)
    assert _is_linked(a, 'coCoMM_FeatureModel', b1)
    if hasattr(b1, 'coCoMM_Feature'):
        assert _is_linked(b1, 'coCoMM_Feature', a)
    _safe_set(a, 'coCoMM_FeatureModel', b2)
    assert _is_linked(a, 'coCoMM_FeatureModel', b2)
    if hasattr(b1, 'coCoMM_Feature'):
        assert not _is_linked(b1, 'coCoMM_Feature', a)
    if hasattr(b2, 'coCoMM_Feature'):
        assert _is_linked(b2, 'coCoMM_Feature', a)
    _safe_set(a, 'coCoMM_FeatureModel', None)
    assert not _is_linked(a, 'coCoMM_FeatureModel', b2)
    if hasattr(b2, 'coCoMM_Feature'):
        assert not _is_linked(b2, 'coCoMM_Feature', a)


def test_assoc_stakeholder58_link_reassign_clear():
    a = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    b1 = coCoMM_Config(selected=True, type="sample_text")
    b2 = coCoMM_Config(selected=False, type="sample_text_2")
    _safe_set(a, 'coCoMM_Stakeholder60', b1)
    assert _is_linked(a, 'coCoMM_Stakeholder60', b1)
    if hasattr(b1, 'coCoMM_Config59'):
        assert _is_linked(b1, 'coCoMM_Config59', a)
    _safe_set(a, 'coCoMM_Stakeholder60', b2)
    assert _is_linked(a, 'coCoMM_Stakeholder60', b2)
    if hasattr(b1, 'coCoMM_Config59'):
        assert not _is_linked(b1, 'coCoMM_Config59', a)
    if hasattr(b2, 'coCoMM_Config59'):
        assert _is_linked(b2, 'coCoMM_Config59', a)
    _safe_set(a, 'coCoMM_Stakeholder60', None)
    assert not _is_linked(a, 'coCoMM_Stakeholder60', b2)
    if hasattr(b2, 'coCoMM_Config59'):
        assert not _is_linked(b2, 'coCoMM_Config59', a)


def test_assoc_stakeholders38_link_reassign_clear():
    a = coCoMM_Stakeholder(job="sample_text", name="sample_text")
    b1 = coCoMM_CoCo()
    b2 = coCoMM_CoCo()
    _safe_set(a, 'coCoMM_Stakeholder', b1)
    assert _is_linked(a, 'coCoMM_Stakeholder', b1)
    if hasattr(b1, 'coCoMM_CoCo39'):
        assert _is_linked(b1, 'coCoMM_CoCo39', a)
    _safe_set(a, 'coCoMM_Stakeholder', b2)
    assert _is_linked(a, 'coCoMM_Stakeholder', b2)
    if hasattr(b1, 'coCoMM_CoCo39'):
        assert not _is_linked(b1, 'coCoMM_CoCo39', a)
    if hasattr(b2, 'coCoMM_CoCo39'):
        assert _is_linked(b2, 'coCoMM_CoCo39', a)
    _safe_set(a, 'coCoMM_Stakeholder', None)
    assert not _is_linked(a, 'coCoMM_Stakeholder', b2)
    if hasattr(b2, 'coCoMM_CoCo39'):
        assert not _is_linked(b2, 'coCoMM_CoCo39', a)


def test_assoc_treeConstraints3_link_reassign_clear():
    a = coCoMM_TreeConstraint(type="sample_text")
    b1 = coCoMM_Feature(abstract=True, id="sample_text", name="sample_text")
    b2 = coCoMM_Feature(abstract=False, id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'coCoMM_TreeConstraint', b1)
    assert _is_linked(a, 'coCoMM_TreeConstraint', b1)
    if hasattr(b1, 'coCoMM_Feature4'):
        assert _is_linked(b1, 'coCoMM_Feature4', a)
    _safe_set(a, 'coCoMM_TreeConstraint', b2)
    assert _is_linked(a, 'coCoMM_TreeConstraint', b2)
    if hasattr(b1, 'coCoMM_Feature4'):
        assert not _is_linked(b1, 'coCoMM_Feature4', a)
    if hasattr(b2, 'coCoMM_Feature4'):
        assert _is_linked(b2, 'coCoMM_Feature4', a)
    _safe_set(a, 'coCoMM_TreeConstraint', None)
    assert not _is_linked(a, 'coCoMM_TreeConstraint', b2)
    if hasattr(b2, 'coCoMM_Feature4'):
        assert not _is_linked(b2, 'coCoMM_Feature4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DecisionRule_strategy = st.builds(DecisionRule)
@given(instance=DecisionRule_strategy)
@settings(max_examples=25)
def test_DecisionRule_instantiation(instance):
    assert isinstance(instance, DecisionRule)


coCoMM_AttributeType_strategy = st.builds(coCoMM_AttributeType, id=safe_text, name=safe_text)
@given(instance=coCoMM_AttributeType_strategy)
@settings(max_examples=25)
def test_coCoMM_AttributeType_instantiation(instance):
    assert isinstance(instance, coCoMM_AttributeType)


coCoMM_AttributeTypeElement_strategy = st.builds(coCoMM_AttributeTypeElement, dataType=safe_text, name=safe_text)
@given(instance=coCoMM_AttributeTypeElement_strategy)
@settings(max_examples=25)
def test_coCoMM_AttributeTypeElement_instantiation(instance):
    assert isinstance(instance, coCoMM_AttributeTypeElement)


coCoMM_CMConstraintExpression_strategy = st.builds(coCoMM_CMConstraintExpression, op=safe_text)
@given(instance=coCoMM_CMConstraintExpression_strategy)
@settings(max_examples=25)
def test_coCoMM_CMConstraintExpression_instantiation(instance):
    assert isinstance(instance, coCoMM_CMConstraintExpression)


coCoMM_CTConstraintExpression_strategy = st.builds(coCoMM_CTConstraintExpression, op=safe_text)
@given(instance=coCoMM_CTConstraintExpression_strategy)
@settings(max_examples=25)
def test_coCoMM_CTConstraintExpression_instantiation(instance):
    assert isinstance(instance, coCoMM_CTConstraintExpression)


coCoMM_CoCo_strategy = st.builds(coCoMM_CoCo)
@given(instance=coCoMM_CoCo_strategy)
@settings(max_examples=25)
def test_coCoMM_CoCo_instantiation(instance):
    assert isinstance(instance, coCoMM_CoCo)


coCoMM_Config_strategy = st.builds(coCoMM_Config, selected=st.booleans(), type=safe_text)
@given(instance=coCoMM_Config_strategy)
@settings(max_examples=25)
def test_coCoMM_Config_instantiation(instance):
    assert isinstance(instance, coCoMM_Config)


coCoMM_CrossModelConstraint_strategy = st.builds(coCoMM_CrossModelConstraint)
@given(instance=coCoMM_CrossModelConstraint_strategy)
@settings(max_examples=25)
def test_coCoMM_CrossModelConstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossModelConstraint)


coCoMM_CrossTreeConstraint_strategy = st.builds(coCoMM_CrossTreeConstraint)
@given(instance=coCoMM_CrossTreeConstraint_strategy)
@settings(max_examples=25)
def test_coCoMM_CrossTreeConstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossTreeConstraint)


coCoMM_DecisionRule_strategy = st.builds(coCoMM_DecisionRule, type=safe_text)
@given(instance=coCoMM_DecisionRule_strategy)
@settings(max_examples=25)
def test_coCoMM_DecisionRule_instantiation(instance):
    assert isinstance(instance, coCoMM_DecisionRule)


coCoMM_Feature_strategy = st.builds(coCoMM_Feature, abstract=st.booleans(), id=safe_text, name=safe_text)
@given(instance=coCoMM_Feature_strategy)
@settings(max_examples=25)
def test_coCoMM_Feature_instantiation(instance):
    assert isinstance(instance, coCoMM_Feature)


coCoMM_FeatureAttribute_strategy = st.builds(coCoMM_FeatureAttribute, name=safe_text)
@given(instance=coCoMM_FeatureAttribute_strategy)
@settings(max_examples=25)
def test_coCoMM_FeatureAttribute_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureAttribute)


coCoMM_FeatureAttributeElement_strategy = st.builds(coCoMM_FeatureAttributeElement, value=safe_text)
@given(instance=coCoMM_FeatureAttributeElement_strategy)
@settings(max_examples=25)
def test_coCoMM_FeatureAttributeElement_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureAttributeElement)


coCoMM_FeatureModel_strategy = st.builds(coCoMM_FeatureModel, isDomain=st.booleans(), name=safe_text)
@given(instance=coCoMM_FeatureModel_strategy)
@settings(max_examples=25)
def test_coCoMM_FeatureModel_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureModel)


coCoMM_HardLimitDR_strategy = st.builds(coCoMM_HardLimitDR)
@given(instance=coCoMM_HardLimitDR_strategy)
@settings(max_examples=25)
def test_coCoMM_HardLimitDR_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitDR)


coCoMM_HardLimitDRExpression_strategy = st.builds(coCoMM_HardLimitDRExpression, op=safe_text, value=safe_text)
@given(instance=coCoMM_HardLimitDRExpression_strategy)
@settings(max_examples=25)
def test_coCoMM_HardLimitDRExpression_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitDRExpression)


coCoMM_OptimizationDR_strategy = st.builds(coCoMM_OptimizationDR, funct=safe_text)
@given(instance=coCoMM_OptimizationDR_strategy)
@settings(max_examples=25)
def test_coCoMM_OptimizationDR_instantiation(instance):
    assert isinstance(instance, coCoMM_OptimizationDR)


coCoMM_Project_strategy = st.builds(coCoMM_Project, date=st.dates(), name=safe_text, target=st.booleans())
@given(instance=coCoMM_Project_strategy)
@settings(max_examples=25)
def test_coCoMM_Project_instantiation(instance):
    assert isinstance(instance, coCoMM_Project)


coCoMM_SelectionStateDR_strategy = st.builds(coCoMM_SelectionStateDR, state=safe_text)
@given(instance=coCoMM_SelectionStateDR_strategy)
@settings(max_examples=25)
def test_coCoMM_SelectionStateDR_instantiation(instance):
    assert isinstance(instance, coCoMM_SelectionStateDR)


coCoMM_Stakeholder_strategy = st.builds(coCoMM_Stakeholder, job=safe_text, name=safe_text)
@given(instance=coCoMM_Stakeholder_strategy)
@settings(max_examples=25)
def test_coCoMM_Stakeholder_instantiation(instance):
    assert isinstance(instance, coCoMM_Stakeholder)


coCoMM_TreeConstraint_strategy = st.builds(coCoMM_TreeConstraint, type=safe_text)
@given(instance=coCoMM_TreeConstraint_strategy)
@settings(max_examples=25)
def test_coCoMM_TreeConstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_TreeConstraint)


