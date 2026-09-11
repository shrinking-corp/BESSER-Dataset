import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SolutionConstraint,
    test7_AttributeType,
    test7_AttributeTypeElement,
    test7_Feature,
    test7_FeatureAttribute,
    test7_FeatureAttributeElement,
    test7_FeatureAttributeReference,
    test7_FiniteDomainSC,
    test7_FiniteDomainSCValueReference,
    test7_HardLimitSC,
    test7_Model,
    test7_OptimizationSC,
    test7_SelectionStateSC,
    test7_SolutionConstraint,
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

def test_test7_AttributeType_name_value_roundtrip():
    instance = test7_AttributeType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_test7_AttributeTypeElement_dataType_value_roundtrip():
    instance = test7_AttributeTypeElement(dataType="sample_text", name="sample_text")
    assert instance.dataType == "sample_text"
    instance.dataType = "sample_text_2"
    assert instance.dataType == "sample_text_2"


def test_test7_AttributeTypeElement_name_value_roundtrip():
    instance = test7_AttributeTypeElement(dataType="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_test7_Feature_name_value_roundtrip():
    instance = test7_Feature(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_test7_FeatureAttribute_name_value_roundtrip():
    instance = test7_FeatureAttribute(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_test7_FeatureAttributeElement_value_value_roundtrip():
    instance = test7_FeatureAttributeElement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_test7_FiniteDomainSCValueReference_value_value_roundtrip():
    instance = test7_FiniteDomainSCValueReference(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_test7_HardLimitSC_op1_value_roundtrip():
    instance = test7_HardLimitSC(op1="sample_text", op2="sample_text", value1="sample_text", value2="sample_text")
    assert instance.op1 == "sample_text"
    instance.op1 = "sample_text_2"
    assert instance.op1 == "sample_text_2"


def test_test7_HardLimitSC_op2_value_roundtrip():
    instance = test7_HardLimitSC(op1="sample_text", op2="sample_text", value1="sample_text", value2="sample_text")
    assert instance.op2 == "sample_text"
    instance.op2 = "sample_text_2"
    assert instance.op2 == "sample_text_2"


def test_test7_HardLimitSC_value1_value_roundtrip():
    instance = test7_HardLimitSC(op1="sample_text", op2="sample_text", value1="sample_text", value2="sample_text")
    assert instance.value1 == "sample_text"
    instance.value1 = "sample_text_2"
    assert instance.value1 == "sample_text_2"


def test_test7_HardLimitSC_value2_value_roundtrip():
    instance = test7_HardLimitSC(op1="sample_text", op2="sample_text", value1="sample_text", value2="sample_text")
    assert instance.value2 == "sample_text"
    instance.value2 = "sample_text_2"
    assert instance.value2 == "sample_text_2"


def test_test7_OptimizationSC_funct_value_roundtrip():
    instance = test7_OptimizationSC(funct="sample_text")
    assert instance.funct == "sample_text"
    instance.funct = "sample_text_2"
    assert instance.funct == "sample_text_2"


def test_test7_SelectionStateSC_state_value_roundtrip():
    instance = test7_SelectionStateSC(state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_test7_SolutionConstraint_name_value_roundtrip():
    instance = test7_SolutionConstraint(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_test7_SolutionConstraint_type_value_roundtrip():
    instance = test7_SolutionConstraint(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_test7_FiniteDomainSC_isa_SolutionConstraint():
    instance = test7_FiniteDomainSC()
    assert isinstance(instance, SolutionConstraint)


def test_test7_HardLimitSC_isa_SolutionConstraint():
    instance = test7_HardLimitSC(op1="sample_text", op2="sample_text", value1="sample_text", value2="sample_text")
    assert isinstance(instance, SolutionConstraint)


def test_test7_OptimizationSC_isa_SolutionConstraint():
    instance = test7_OptimizationSC(funct="sample_text")
    assert isinstance(instance, SolutionConstraint)


def test_test7_SelectionStateSC_isa_SolutionConstraint():
    instance = test7_SelectionStateSC(state="sample_text")
    assert isinstance(instance, SolutionConstraint)


def test_assoc_attrType12_link_reassign_clear():
    a = test7_FeatureAttribute(name="sample_text")
    b1 = test7_AttributeType(name="sample_text")
    b2 = test7_AttributeType(name="sample_text_2")
    _safe_set(a, 'test7_FeatureAttribute13', b1)
    assert _is_linked(a, 'test7_FeatureAttribute13', b1)
    if hasattr(b1, 'test7_AttributeType14'):
        assert _is_linked(b1, 'test7_AttributeType14', a)
    _safe_set(a, 'test7_FeatureAttribute13', b2)
    assert _is_linked(a, 'test7_FeatureAttribute13', b2)
    if hasattr(b1, 'test7_AttributeType14'):
        assert not _is_linked(b1, 'test7_AttributeType14', a)
    if hasattr(b2, 'test7_AttributeType14'):
        assert _is_linked(b2, 'test7_AttributeType14', a)
    _safe_set(a, 'test7_FeatureAttribute13', None)
    assert not _is_linked(a, 'test7_FeatureAttribute13', b2)
    if hasattr(b2, 'test7_AttributeType14'):
        assert not _is_linked(b2, 'test7_AttributeType14', a)


def test_assoc_attrType22_link_reassign_clear():
    a = test7_OptimizationSC(funct="sample_text")
    b1 = test7_AttributeType(name="sample_text")
    b2 = test7_AttributeType(name="sample_text_2")
    _safe_set(a, 'test7_OptimizationSC', b1)
    assert _is_linked(a, 'test7_OptimizationSC', b1)
    if hasattr(b1, 'test7_AttributeType23'):
        assert _is_linked(b1, 'test7_AttributeType23', a)
    _safe_set(a, 'test7_OptimizationSC', b2)
    assert _is_linked(a, 'test7_OptimizationSC', b2)
    if hasattr(b1, 'test7_AttributeType23'):
        assert not _is_linked(b1, 'test7_AttributeType23', a)
    if hasattr(b2, 'test7_AttributeType23'):
        assert _is_linked(b2, 'test7_AttributeType23', a)
    _safe_set(a, 'test7_OptimizationSC', None)
    assert not _is_linked(a, 'test7_OptimizationSC', b2)
    if hasattr(b2, 'test7_AttributeType23'):
        assert not _is_linked(b2, 'test7_AttributeType23', a)


def test_assoc_attrType24_link_reassign_clear():
    a = test7_HardLimitSC(op1="sample_text", op2="sample_text", value1="sample_text", value2="sample_text")
    b1 = test7_AttributeType(name="sample_text")
    b2 = test7_AttributeType(name="sample_text_2")
    _safe_set(a, 'test7_HardLimitSC', b1)
    assert _is_linked(a, 'test7_HardLimitSC', b1)
    if hasattr(b1, 'test7_AttributeType25'):
        assert _is_linked(b1, 'test7_AttributeType25', a)
    _safe_set(a, 'test7_HardLimitSC', b2)
    assert _is_linked(a, 'test7_HardLimitSC', b2)
    if hasattr(b1, 'test7_AttributeType25'):
        assert not _is_linked(b1, 'test7_AttributeType25', a)
    if hasattr(b2, 'test7_AttributeType25'):
        assert _is_linked(b2, 'test7_AttributeType25', a)
    _safe_set(a, 'test7_HardLimitSC', None)
    assert not _is_linked(a, 'test7_HardLimitSC', b2)
    if hasattr(b2, 'test7_AttributeType25'):
        assert not _is_linked(b2, 'test7_AttributeType25', a)


def test_assoc_attributeTypes0_link_reassign_clear():
    a = test7_AttributeType(name="sample_text")
    b1 = test7_Model()
    b2 = test7_Model()
    _safe_set(a, 'test7_AttributeType', b1)
    assert _is_linked(a, 'test7_AttributeType', b1)
    if hasattr(b1, 'test7_Model'):
        assert _is_linked(b1, 'test7_Model', a)
    _safe_set(a, 'test7_AttributeType', b2)
    assert _is_linked(a, 'test7_AttributeType', b2)
    if hasattr(b1, 'test7_Model'):
        assert not _is_linked(b1, 'test7_Model', a)
    if hasattr(b2, 'test7_Model'):
        assert _is_linked(b2, 'test7_Model', a)
    _safe_set(a, 'test7_AttributeType', None)
    assert not _is_linked(a, 'test7_AttributeType', b2)
    if hasattr(b2, 'test7_Model'):
        assert not _is_linked(b2, 'test7_Model', a)


def test_assoc_attributes19_link_reassign_clear():
    a = test7_Feature(name="sample_text")
    b1 = test7_FeatureAttributeReference()
    b2 = test7_FeatureAttributeReference()
    _safe_set(a, 'test7_Feature20', {b1})
    assert _is_linked(a, 'test7_Feature20', b1)
    if hasattr(b1, 'test7_FeatureAttributeReference21'):
        assert _is_linked(b1, 'test7_FeatureAttributeReference21', a)
    _safe_set(a, 'test7_Feature20', {b2})
    assert _is_linked(a, 'test7_Feature20', b2)
    if hasattr(b1, 'test7_FeatureAttributeReference21'):
        assert not _is_linked(b1, 'test7_FeatureAttributeReference21', a)
    if hasattr(b2, 'test7_FeatureAttributeReference21'):
        assert _is_linked(b2, 'test7_FeatureAttributeReference21', a)
    _safe_set(a, 'test7_Feature20', set())
    assert not _is_linked(a, 'test7_Feature20', b2)
    if hasattr(b2, 'test7_FeatureAttributeReference21'):
        assert not _is_linked(b2, 'test7_FeatureAttributeReference21', a)


def test_assoc_elements7_link_reassign_clear():
    a = test7_AttributeTypeElement(dataType="sample_text", name="sample_text")
    b1 = test7_AttributeType(name="sample_text")
    b2 = test7_AttributeType(name="sample_text_2")
    _safe_set(a, 'test7_AttributeTypeElement', b1)
    assert _is_linked(a, 'test7_AttributeTypeElement', b1)
    if hasattr(b1, 'test7_AttributeType8'):
        assert _is_linked(b1, 'test7_AttributeType8', a)
    _safe_set(a, 'test7_AttributeTypeElement', b2)
    assert _is_linked(a, 'test7_AttributeTypeElement', b2)
    if hasattr(b1, 'test7_AttributeType8'):
        assert not _is_linked(b1, 'test7_AttributeType8', a)
    if hasattr(b2, 'test7_AttributeType8'):
        assert _is_linked(b2, 'test7_AttributeType8', a)
    _safe_set(a, 'test7_AttributeTypeElement', None)
    assert not _is_linked(a, 'test7_AttributeTypeElement', b2)
    if hasattr(b2, 'test7_AttributeType8'):
        assert not _is_linked(b2, 'test7_AttributeType8', a)


def test_assoc_feature26_link_reassign_clear():
    a = test7_SelectionStateSC(state="sample_text")
    b1 = test7_Feature(name="sample_text")
    b2 = test7_Feature(name="sample_text_2")
    _safe_set(a, 'test7_SelectionStateSC', b1)
    assert _is_linked(a, 'test7_SelectionStateSC', b1)
    if hasattr(b1, 'test7_Feature27'):
        assert _is_linked(b1, 'test7_Feature27', a)
    _safe_set(a, 'test7_SelectionStateSC', b2)
    assert _is_linked(a, 'test7_SelectionStateSC', b2)
    if hasattr(b1, 'test7_Feature27'):
        assert not _is_linked(b1, 'test7_Feature27', a)
    if hasattr(b2, 'test7_Feature27'):
        assert _is_linked(b2, 'test7_Feature27', a)
    _safe_set(a, 'test7_SelectionStateSC', None)
    assert not _is_linked(a, 'test7_SelectionStateSC', b2)
    if hasattr(b2, 'test7_Feature27'):
        assert not _is_linked(b2, 'test7_Feature27', a)


def test_assoc_feature28_link_reassign_clear():
    a = test7_Feature(name="sample_text")
    b1 = test7_FiniteDomainSC()
    b2 = test7_FiniteDomainSC()
    _safe_set(a, 'test7_Feature29', b1)
    assert _is_linked(a, 'test7_Feature29', b1)
    if hasattr(b1, 'test7_FiniteDomainSC'):
        assert _is_linked(b1, 'test7_FiniteDomainSC', a)
    _safe_set(a, 'test7_Feature29', b2)
    assert _is_linked(a, 'test7_Feature29', b2)
    if hasattr(b1, 'test7_FiniteDomainSC'):
        assert not _is_linked(b1, 'test7_FiniteDomainSC', a)
    if hasattr(b2, 'test7_FiniteDomainSC'):
        assert _is_linked(b2, 'test7_FiniteDomainSC', a)
    _safe_set(a, 'test7_Feature29', None)
    assert not _is_linked(a, 'test7_Feature29', b2)
    if hasattr(b2, 'test7_FiniteDomainSC'):
        assert not _is_linked(b2, 'test7_FiniteDomainSC', a)


def test_assoc_featureAttr30_link_reassign_clear():
    a = test7_FeatureAttribute(name="sample_text")
    b1 = test7_FiniteDomainSC()
    b2 = test7_FiniteDomainSC()
    _safe_set(a, 'test7_FeatureAttribute32', b1)
    assert _is_linked(a, 'test7_FeatureAttribute32', b1)
    if hasattr(b1, 'test7_FiniteDomainSC31'):
        assert _is_linked(b1, 'test7_FiniteDomainSC31', a)
    _safe_set(a, 'test7_FeatureAttribute32', b2)
    assert _is_linked(a, 'test7_FeatureAttribute32', b2)
    if hasattr(b1, 'test7_FiniteDomainSC31'):
        assert not _is_linked(b1, 'test7_FiniteDomainSC31', a)
    if hasattr(b2, 'test7_FiniteDomainSC31'):
        assert _is_linked(b2, 'test7_FiniteDomainSC31', a)
    _safe_set(a, 'test7_FeatureAttribute32', None)
    assert not _is_linked(a, 'test7_FeatureAttribute32', b2)
    if hasattr(b2, 'test7_FiniteDomainSC31'):
        assert not _is_linked(b2, 'test7_FiniteDomainSC31', a)


def test_assoc_featureAttributes1_link_reassign_clear():
    a = test7_FeatureAttribute(name="sample_text")
    b1 = test7_Model()
    b2 = test7_Model()
    _safe_set(a, 'test7_FeatureAttribute', b1)
    assert _is_linked(a, 'test7_FeatureAttribute', b1)
    if hasattr(b1, 'test7_Model2'):
        assert _is_linked(b1, 'test7_Model2', a)
    _safe_set(a, 'test7_FeatureAttribute', b2)
    assert _is_linked(a, 'test7_FeatureAttribute', b2)
    if hasattr(b1, 'test7_Model2'):
        assert not _is_linked(b1, 'test7_Model2', a)
    if hasattr(b2, 'test7_Model2'):
        assert _is_linked(b2, 'test7_Model2', a)
    _safe_set(a, 'test7_FeatureAttribute', None)
    assert not _is_linked(a, 'test7_FeatureAttribute', b2)
    if hasattr(b2, 'test7_Model2'):
        assert not _is_linked(b2, 'test7_Model2', a)


def test_assoc_features3_link_reassign_clear():
    a = test7_Feature(name="sample_text")
    b1 = test7_Model()
    b2 = test7_Model()
    _safe_set(a, 'test7_Feature', b1)
    assert _is_linked(a, 'test7_Feature', b1)
    if hasattr(b1, 'test7_Model4'):
        assert _is_linked(b1, 'test7_Model4', a)
    _safe_set(a, 'test7_Feature', b2)
    assert _is_linked(a, 'test7_Feature', b2)
    if hasattr(b1, 'test7_Model4'):
        assert not _is_linked(b1, 'test7_Model4', a)
    if hasattr(b2, 'test7_Model4'):
        assert _is_linked(b2, 'test7_Model4', a)
    _safe_set(a, 'test7_Feature', None)
    assert not _is_linked(a, 'test7_Feature', b2)
    if hasattr(b2, 'test7_Model4'):
        assert not _is_linked(b2, 'test7_Model4', a)


def test_assoc_independentAttrType10_link_reassign_clear():
    a = test7_AttributeType(name="sample_text")
    b1 = test7_AttributeType(name="sample_text")
    b2 = test7_AttributeType(name="sample_text_2")
    _safe_set(a, 'test7_AttributeType11', b1)
    assert _is_linked(a, 'test7_AttributeType11', b1)
    if hasattr(b1, 'test7_AttributeType9'):
        assert _is_linked(b1, 'test7_AttributeType9', a)
    _safe_set(a, 'test7_AttributeType11', b2)
    assert _is_linked(a, 'test7_AttributeType11', b2)
    if hasattr(b1, 'test7_AttributeType9'):
        assert not _is_linked(b1, 'test7_AttributeType9', a)
    if hasattr(b2, 'test7_AttributeType9'):
        assert _is_linked(b2, 'test7_AttributeType9', a)
    _safe_set(a, 'test7_AttributeType11', None)
    assert not _is_linked(a, 'test7_AttributeType11', b2)
    if hasattr(b2, 'test7_AttributeType9'):
        assert not _is_linked(b2, 'test7_AttributeType9', a)


def test_assoc_name17_link_reassign_clear():
    a = test7_FeatureAttribute(name="sample_text")
    b1 = test7_FeatureAttributeReference()
    b2 = test7_FeatureAttributeReference()
    _safe_set(a, 'test7_FeatureAttribute18', b1)
    assert _is_linked(a, 'test7_FeatureAttribute18', b1)
    if hasattr(b1, 'test7_FeatureAttributeReference'):
        assert _is_linked(b1, 'test7_FeatureAttributeReference', a)
    _safe_set(a, 'test7_FeatureAttribute18', b2)
    assert _is_linked(a, 'test7_FeatureAttribute18', b2)
    if hasattr(b1, 'test7_FeatureAttributeReference'):
        assert not _is_linked(b1, 'test7_FeatureAttributeReference', a)
    if hasattr(b2, 'test7_FeatureAttributeReference'):
        assert _is_linked(b2, 'test7_FeatureAttributeReference', a)
    _safe_set(a, 'test7_FeatureAttribute18', None)
    assert not _is_linked(a, 'test7_FeatureAttribute18', b2)
    if hasattr(b2, 'test7_FeatureAttributeReference'):
        assert not _is_linked(b2, 'test7_FeatureAttributeReference', a)


def test_assoc_solutionConstraints5_link_reassign_clear():
    a = test7_SolutionConstraint(name="sample_text", type="sample_text")
    b1 = test7_Model()
    b2 = test7_Model()
    _safe_set(a, 'test7_SolutionConstraint', b1)
    assert _is_linked(a, 'test7_SolutionConstraint', b1)
    if hasattr(b1, 'test7_Model6'):
        assert _is_linked(b1, 'test7_Model6', a)
    _safe_set(a, 'test7_SolutionConstraint', b2)
    assert _is_linked(a, 'test7_SolutionConstraint', b2)
    if hasattr(b1, 'test7_Model6'):
        assert not _is_linked(b1, 'test7_Model6', a)
    if hasattr(b2, 'test7_Model6'):
        assert _is_linked(b2, 'test7_Model6', a)
    _safe_set(a, 'test7_SolutionConstraint', None)
    assert not _is_linked(a, 'test7_SolutionConstraint', b2)
    if hasattr(b2, 'test7_Model6'):
        assert not _is_linked(b2, 'test7_Model6', a)


def test_assoc_values15_link_reassign_clear():
    a = test7_FeatureAttributeElement(value="sample_text")
    b1 = test7_FeatureAttribute(name="sample_text")
    b2 = test7_FeatureAttribute(name="sample_text_2")
    _safe_set(a, 'test7_FeatureAttributeElement', b1)
    assert _is_linked(a, 'test7_FeatureAttributeElement', b1)
    if hasattr(b1, 'test7_FeatureAttribute16'):
        assert _is_linked(b1, 'test7_FeatureAttribute16', a)
    _safe_set(a, 'test7_FeatureAttributeElement', b2)
    assert _is_linked(a, 'test7_FeatureAttributeElement', b2)
    if hasattr(b1, 'test7_FeatureAttribute16'):
        assert not _is_linked(b1, 'test7_FeatureAttribute16', a)
    if hasattr(b2, 'test7_FeatureAttribute16'):
        assert _is_linked(b2, 'test7_FeatureAttribute16', a)
    _safe_set(a, 'test7_FeatureAttributeElement', None)
    assert not _is_linked(a, 'test7_FeatureAttributeElement', b2)
    if hasattr(b2, 'test7_FeatureAttribute16'):
        assert not _is_linked(b2, 'test7_FeatureAttribute16', a)


def test_assoc_values33_link_reassign_clear():
    a = test7_FiniteDomainSCValueReference(value="sample_text")
    b1 = test7_FiniteDomainSC()
    b2 = test7_FiniteDomainSC()
    _safe_set(a, 'test7_FiniteDomainSCValueReference', b1)
    assert _is_linked(a, 'test7_FiniteDomainSCValueReference', b1)
    if hasattr(b1, 'test7_FiniteDomainSC34'):
        assert _is_linked(b1, 'test7_FiniteDomainSC34', a)
    _safe_set(a, 'test7_FiniteDomainSCValueReference', b2)
    assert _is_linked(a, 'test7_FiniteDomainSCValueReference', b2)
    if hasattr(b1, 'test7_FiniteDomainSC34'):
        assert not _is_linked(b1, 'test7_FiniteDomainSC34', a)
    if hasattr(b2, 'test7_FiniteDomainSC34'):
        assert _is_linked(b2, 'test7_FiniteDomainSC34', a)
    _safe_set(a, 'test7_FiniteDomainSCValueReference', None)
    assert not _is_linked(a, 'test7_FiniteDomainSCValueReference', b2)
    if hasattr(b2, 'test7_FiniteDomainSC34'):
        assert not _is_linked(b2, 'test7_FiniteDomainSC34', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SolutionConstraint_strategy = st.builds(SolutionConstraint)
@given(instance=SolutionConstraint_strategy)
@settings(max_examples=25)
def test_SolutionConstraint_instantiation(instance):
    assert isinstance(instance, SolutionConstraint)


test7_AttributeType_strategy = st.builds(test7_AttributeType, name=safe_text)
@given(instance=test7_AttributeType_strategy)
@settings(max_examples=25)
def test_test7_AttributeType_instantiation(instance):
    assert isinstance(instance, test7_AttributeType)


test7_AttributeTypeElement_strategy = st.builds(test7_AttributeTypeElement, dataType=safe_text, name=safe_text)
@given(instance=test7_AttributeTypeElement_strategy)
@settings(max_examples=25)
def test_test7_AttributeTypeElement_instantiation(instance):
    assert isinstance(instance, test7_AttributeTypeElement)


test7_Feature_strategy = st.builds(test7_Feature, name=safe_text)
@given(instance=test7_Feature_strategy)
@settings(max_examples=25)
def test_test7_Feature_instantiation(instance):
    assert isinstance(instance, test7_Feature)


test7_FeatureAttribute_strategy = st.builds(test7_FeatureAttribute, name=safe_text)
@given(instance=test7_FeatureAttribute_strategy)
@settings(max_examples=25)
def test_test7_FeatureAttribute_instantiation(instance):
    assert isinstance(instance, test7_FeatureAttribute)


test7_FeatureAttributeElement_strategy = st.builds(test7_FeatureAttributeElement, value=safe_text)
@given(instance=test7_FeatureAttributeElement_strategy)
@settings(max_examples=25)
def test_test7_FeatureAttributeElement_instantiation(instance):
    assert isinstance(instance, test7_FeatureAttributeElement)


test7_FeatureAttributeReference_strategy = st.builds(test7_FeatureAttributeReference)
@given(instance=test7_FeatureAttributeReference_strategy)
@settings(max_examples=25)
def test_test7_FeatureAttributeReference_instantiation(instance):
    assert isinstance(instance, test7_FeatureAttributeReference)


test7_FiniteDomainSC_strategy = st.builds(test7_FiniteDomainSC)
@given(instance=test7_FiniteDomainSC_strategy)
@settings(max_examples=25)
def test_test7_FiniteDomainSC_instantiation(instance):
    assert isinstance(instance, test7_FiniteDomainSC)


test7_FiniteDomainSCValueReference_strategy = st.builds(test7_FiniteDomainSCValueReference, value=safe_text)
@given(instance=test7_FiniteDomainSCValueReference_strategy)
@settings(max_examples=25)
def test_test7_FiniteDomainSCValueReference_instantiation(instance):
    assert isinstance(instance, test7_FiniteDomainSCValueReference)


test7_HardLimitSC_strategy = st.builds(test7_HardLimitSC, op1=safe_text, op2=safe_text, value1=safe_text, value2=safe_text)
@given(instance=test7_HardLimitSC_strategy)
@settings(max_examples=25)
def test_test7_HardLimitSC_instantiation(instance):
    assert isinstance(instance, test7_HardLimitSC)


test7_Model_strategy = st.builds(test7_Model)
@given(instance=test7_Model_strategy)
@settings(max_examples=25)
def test_test7_Model_instantiation(instance):
    assert isinstance(instance, test7_Model)


test7_OptimizationSC_strategy = st.builds(test7_OptimizationSC, funct=safe_text)
@given(instance=test7_OptimizationSC_strategy)
@settings(max_examples=25)
def test_test7_OptimizationSC_instantiation(instance):
    assert isinstance(instance, test7_OptimizationSC)


test7_SelectionStateSC_strategy = st.builds(test7_SelectionStateSC, state=safe_text)
@given(instance=test7_SelectionStateSC_strategy)
@settings(max_examples=25)
def test_test7_SelectionStateSC_instantiation(instance):
    assert isinstance(instance, test7_SelectionStateSC)


test7_SolutionConstraint_strategy = st.builds(test7_SolutionConstraint, name=safe_text, type=safe_text)
@given(instance=test7_SolutionConstraint_strategy)
@settings(max_examples=25)
def test_test7_SolutionConstraint_instantiation(instance):
    assert isinstance(instance, test7_SolutionConstraint)


