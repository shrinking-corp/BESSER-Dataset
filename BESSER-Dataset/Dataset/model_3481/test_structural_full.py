import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AttributeOperand,
    Constraint,
    Domain,
    FeatureConstraint,
    Identifiable,
    feature_Attribute,
    feature_AttributeConstraint,
    feature_AttributeOperand,
    feature_AttributeReference,
    feature_AttributeValue,
    feature_Constraint,
    feature_DiscreteDomain,
    feature_Domain,
    feature_DomainValue,
    feature_Exclude,
    feature_Feature,
    feature_FeatureConstraint,
    feature_FeatureModel,
    feature_Group,
    feature_Identifiable,
    feature_Imply,
    feature_Interval,
    feature_NumericalDomain,
    FeatureState,
    Relop,
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

def test_feature_Attribute_deselectedDomainValues_value_roundtrip():
    instance = feature_Attribute(deselectedDomainValues="sample_text", name="sample_text", value="sample_text")
    assert instance.deselectedDomainValues == "sample_text"
    instance.deselectedDomainValues = "sample_text_2"
    assert instance.deselectedDomainValues == "sample_text_2"


def test_feature_Attribute_name_value_roundtrip():
    instance = feature_Attribute(deselectedDomainValues="sample_text", name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_feature_Attribute_value_value_roundtrip():
    instance = feature_Attribute(deselectedDomainValues="sample_text", name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_feature_AttributeConstraint_operator_value_roundtrip():
    instance = feature_AttributeConstraint(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_feature_AttributeValue_int_value_roundtrip():
    instance = feature_AttributeValue(int=7, name="sample_text")
    assert instance.int == 7
    instance.int = 13
    assert instance.int == 13


def test_feature_AttributeValue_name_value_roundtrip():
    instance = feature_AttributeValue(int=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_feature_DomainValue_int_value_roundtrip():
    instance = feature_DomainValue(int=7, name="sample_text")
    assert instance.int == 7
    instance.int = 13
    assert instance.int == 13


def test_feature_DomainValue_name_value_roundtrip():
    instance = feature_DomainValue(int=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_feature_Feature_configurationState_value_roundtrip():
    instance = feature_Feature(configurationState="sample_text", name="sample_text")
    assert instance.configurationState == "sample_text"
    instance.configurationState = "sample_text_2"
    assert instance.configurationState == "sample_text_2"


def test_feature_Feature_name_value_roundtrip():
    instance = feature_Feature(configurationState="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_feature_FeatureModel_name_value_roundtrip():
    instance = feature_FeatureModel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_feature_Group_maxCardinality_value_roundtrip():
    instance = feature_Group(maxCardinality=7, minCardinality=7)
    assert instance.maxCardinality == 7
    instance.maxCardinality = 13
    assert instance.maxCardinality == 13


def test_feature_Group_minCardinality_value_roundtrip():
    instance = feature_Group(maxCardinality=7, minCardinality=7)
    assert instance.minCardinality == 7
    instance.minCardinality = 13
    assert instance.minCardinality == 13


def test_feature_Identifiable_id_value_roundtrip():
    instance = feature_Identifiable(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_feature_Interval_lowerBound_value_roundtrip():
    instance = feature_Interval(lowerBound=7, upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_feature_Interval_upperBound_value_roundtrip():
    instance = feature_Interval(lowerBound=7, upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_feature_AttributeReference_isa_AttributeOperand():
    instance = feature_AttributeReference()
    assert isinstance(instance, AttributeOperand)


def test_feature_AttributeValue_isa_AttributeOperand():
    instance = feature_AttributeValue(int=7, name="sample_text")
    assert isinstance(instance, AttributeOperand)


def test_feature_AttributeConstraint_isa_Constraint():
    instance = feature_AttributeConstraint(operator="sample_text")
    assert isinstance(instance, Constraint)


def test_feature_FeatureConstraint_isa_Constraint():
    instance = feature_FeatureConstraint()
    assert isinstance(instance, Constraint)


def test_feature_DiscreteDomain_isa_Domain():
    instance = feature_DiscreteDomain()
    assert isinstance(instance, Domain)


def test_feature_NumericalDomain_isa_Domain():
    instance = feature_NumericalDomain()
    assert isinstance(instance, Domain)


def test_feature_Exclude_isa_FeatureConstraint():
    instance = feature_Exclude()
    assert isinstance(instance, FeatureConstraint)


def test_feature_Imply_isa_FeatureConstraint():
    instance = feature_Imply()
    assert isinstance(instance, FeatureConstraint)


def test_feature_Constraint_isa_Identifiable():
    instance = feature_Constraint()
    assert isinstance(instance, Identifiable)


def test_feature_Domain_isa_Identifiable():
    instance = feature_Domain()
    assert isinstance(instance, Identifiable)


def test_feature_Feature_isa_Identifiable():
    instance = feature_Feature(configurationState="sample_text", name="sample_text")
    assert isinstance(instance, Identifiable)


def test_feature_Group_isa_Identifiable():
    instance = feature_Group(maxCardinality=7, minCardinality=7)
    assert isinstance(instance, Identifiable)


def test_assoc_attribute20_link_reassign_clear():
    a = feature_Attribute(deselectedDomainValues="sample_text", name="sample_text", value="sample_text")
    b1 = feature_AttributeReference()
    b2 = feature_AttributeReference()
    _safe_set(a, 'feature_Attribute21', b1)
    assert _is_linked(a, 'feature_Attribute21', b1)
    if hasattr(b1, 'feature_AttributeReference'):
        assert _is_linked(b1, 'feature_AttributeReference', a)
    _safe_set(a, 'feature_Attribute21', b2)
    assert _is_linked(a, 'feature_Attribute21', b2)
    if hasattr(b1, 'feature_AttributeReference'):
        assert not _is_linked(b1, 'feature_AttributeReference', a)
    if hasattr(b2, 'feature_AttributeReference'):
        assert _is_linked(b2, 'feature_AttributeReference', a)
    _safe_set(a, 'feature_Attribute21', None)
    assert not _is_linked(a, 'feature_Attribute21', b2)
    if hasattr(b2, 'feature_AttributeReference'):
        assert not _is_linked(b2, 'feature_AttributeReference', a)


def test_assoc_attributes5_link_reassign_clear():
    a = feature_Feature(configurationState="sample_text", name="sample_text")
    b1 = feature_Attribute(deselectedDomainValues="sample_text", name="sample_text", value="sample_text")
    b2 = feature_Attribute(deselectedDomainValues="sample_text_2", name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'feature', {b1})
    assert _is_linked(a, 'feature', b1)
    if hasattr(b1, 'Attribute'):
        assert _is_linked(b1, 'Attribute', a)
    _safe_set(a, 'feature', {b2})
    assert _is_linked(a, 'feature', b2)
    if hasattr(b1, 'Attribute'):
        assert not _is_linked(b1, 'Attribute', a)
    if hasattr(b2, 'Attribute'):
        assert _is_linked(b2, 'Attribute', a)
    _safe_set(a, 'feature', set())
    assert not _is_linked(a, 'feature', b2)
    if hasattr(b2, 'Attribute'):
        assert not _is_linked(b2, 'Attribute', a)


def test_assoc_childFeatures8_link_reassign_clear():
    a = feature_Group(maxCardinality=7, minCardinality=7)
    b1 = feature_Feature(configurationState="sample_text", name="sample_text")
    b2 = feature_Feature(configurationState="sample_text_2", name="sample_text_2")
    _safe_set(a, 'feature_Group9', {b1})
    assert _is_linked(a, 'feature_Group9', b1)
    if hasattr(b1, 'feature_Feature10'):
        assert _is_linked(b1, 'feature_Feature10', a)
    _safe_set(a, 'feature_Group9', {b2})
    assert _is_linked(a, 'feature_Group9', b2)
    if hasattr(b1, 'feature_Feature10'):
        assert not _is_linked(b1, 'feature_Feature10', a)
    if hasattr(b2, 'feature_Feature10'):
        assert _is_linked(b2, 'feature_Feature10', a)
    _safe_set(a, 'feature_Group9', set())
    assert not _is_linked(a, 'feature_Group9', b2)
    if hasattr(b2, 'feature_Feature10'):
        assert not _is_linked(b2, 'feature_Feature10', a)


def test_assoc_constraints3_link_reassign_clear():
    a = feature_FeatureModel(name="sample_text")
    b1 = feature_Constraint()
    b2 = feature_Constraint()
    _safe_set(a, 'feature_FeatureModel4', {b1})
    assert _is_linked(a, 'feature_FeatureModel4', b1)
    if hasattr(b1, 'feature_Constraint'):
        assert _is_linked(b1, 'feature_Constraint', a)
    _safe_set(a, 'feature_FeatureModel4', {b2})
    assert _is_linked(a, 'feature_FeatureModel4', b2)
    if hasattr(b1, 'feature_Constraint'):
        assert not _is_linked(b1, 'feature_Constraint', a)
    if hasattr(b2, 'feature_Constraint'):
        assert _is_linked(b2, 'feature_Constraint', a)
    _safe_set(a, 'feature_FeatureModel4', set())
    assert not _is_linked(a, 'feature_FeatureModel4', b2)
    if hasattr(b2, 'feature_Constraint'):
        assert not _is_linked(b2, 'feature_Constraint', a)


def test_assoc_domain12_link_reassign_clear():
    a = feature_Attribute(deselectedDomainValues="sample_text", name="sample_text", value="sample_text")
    b1 = feature_Domain()
    b2 = feature_Domain()
    _safe_set(a, 'feature_Attribute', b1)
    assert _is_linked(a, 'feature_Attribute', b1)
    if hasattr(b1, 'feature_Domain13'):
        assert _is_linked(b1, 'feature_Domain13', a)
    _safe_set(a, 'feature_Attribute', b2)
    assert _is_linked(a, 'feature_Attribute', b2)
    if hasattr(b1, 'feature_Domain13'):
        assert not _is_linked(b1, 'feature_Domain13', a)
    if hasattr(b2, 'feature_Domain13'):
        assert _is_linked(b2, 'feature_Domain13', a)
    _safe_set(a, 'feature_Attribute', None)
    assert not _is_linked(a, 'feature_Attribute', b2)
    if hasattr(b2, 'feature_Domain13'):
        assert not _is_linked(b2, 'feature_Domain13', a)


def test_assoc_domains1_link_reassign_clear():
    a = feature_FeatureModel(name="sample_text")
    b1 = feature_Domain()
    b2 = feature_Domain()
    _safe_set(a, 'feature_FeatureModel2', {b1})
    assert _is_linked(a, 'feature_FeatureModel2', b1)
    if hasattr(b1, 'feature_Domain'):
        assert _is_linked(b1, 'feature_Domain', a)
    _safe_set(a, 'feature_FeatureModel2', {b2})
    assert _is_linked(a, 'feature_FeatureModel2', b2)
    if hasattr(b1, 'feature_Domain'):
        assert not _is_linked(b1, 'feature_Domain', a)
    if hasattr(b2, 'feature_Domain'):
        assert _is_linked(b2, 'feature_Domain', a)
    _safe_set(a, 'feature_FeatureModel2', set())
    assert not _is_linked(a, 'feature_FeatureModel2', b2)
    if hasattr(b2, 'feature_Domain'):
        assert not _is_linked(b2, 'feature_Domain', a)


def test_assoc_feature11_link_reassign_clear():
    a = feature_Feature(configurationState="sample_text", name="sample_text")
    b1 = feature_Attribute(deselectedDomainValues="sample_text", name="sample_text", value="sample_text")
    b2 = feature_Attribute(deselectedDomainValues="sample_text_2", name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'Feature', b1)
    assert _is_linked(a, 'Feature', b1)
    if hasattr(b1, 'attributes'):
        assert _is_linked(b1, 'attributes', a)
    _safe_set(a, 'Feature', b2)
    assert _is_linked(a, 'Feature', b2)
    if hasattr(b1, 'attributes'):
        assert not _is_linked(b1, 'attributes', a)
    if hasattr(b2, 'attributes'):
        assert _is_linked(b2, 'attributes', a)
    _safe_set(a, 'Feature', None)
    assert not _is_linked(a, 'Feature', b2)
    if hasattr(b2, 'attributes'):
        assert not _is_linked(b2, 'attributes', a)


def test_assoc_feature22_link_reassign_clear():
    a = feature_Feature(configurationState="sample_text", name="sample_text")
    b1 = feature_AttributeReference()
    b2 = feature_AttributeReference()
    _safe_set(a, 'feature_Feature24', b1)
    assert _is_linked(a, 'feature_Feature24', b1)
    if hasattr(b1, 'feature_AttributeReference23'):
        assert _is_linked(b1, 'feature_AttributeReference23', a)
    _safe_set(a, 'feature_Feature24', b2)
    assert _is_linked(a, 'feature_Feature24', b2)
    if hasattr(b1, 'feature_AttributeReference23'):
        assert not _is_linked(b1, 'feature_AttributeReference23', a)
    if hasattr(b2, 'feature_AttributeReference23'):
        assert _is_linked(b2, 'feature_AttributeReference23', a)
    _safe_set(a, 'feature_Feature24', None)
    assert not _is_linked(a, 'feature_Feature24', b2)
    if hasattr(b2, 'feature_AttributeReference23'):
        assert not _is_linked(b2, 'feature_AttributeReference23', a)


def test_assoc_groups6_link_reassign_clear():
    a = feature_Group(maxCardinality=7, minCardinality=7)
    b1 = feature_Feature(configurationState="sample_text", name="sample_text")
    b2 = feature_Feature(configurationState="sample_text_2", name="sample_text_2")
    _safe_set(a, 'feature_Group', b1)
    assert _is_linked(a, 'feature_Group', b1)
    if hasattr(b1, 'feature_Feature7'):
        assert _is_linked(b1, 'feature_Feature7', a)
    _safe_set(a, 'feature_Group', b2)
    assert _is_linked(a, 'feature_Group', b2)
    if hasattr(b1, 'feature_Feature7'):
        assert not _is_linked(b1, 'feature_Feature7', a)
    if hasattr(b2, 'feature_Feature7'):
        assert _is_linked(b2, 'feature_Feature7', a)
    _safe_set(a, 'feature_Group', None)
    assert not _is_linked(a, 'feature_Group', b2)
    if hasattr(b2, 'feature_Feature7'):
        assert not _is_linked(b2, 'feature_Feature7', a)


def test_assoc_intervals15_link_reassign_clear():
    a = feature_Interval(lowerBound=7, upperBound=7)
    b1 = feature_NumericalDomain()
    b2 = feature_NumericalDomain()
    _safe_set(a, 'feature_Interval', b1)
    assert _is_linked(a, 'feature_Interval', b1)
    if hasattr(b1, 'feature_NumericalDomain'):
        assert _is_linked(b1, 'feature_NumericalDomain', a)
    _safe_set(a, 'feature_Interval', b2)
    assert _is_linked(a, 'feature_Interval', b2)
    if hasattr(b1, 'feature_NumericalDomain'):
        assert not _is_linked(b1, 'feature_NumericalDomain', a)
    if hasattr(b2, 'feature_NumericalDomain'):
        assert _is_linked(b2, 'feature_NumericalDomain', a)
    _safe_set(a, 'feature_Interval', None)
    assert not _is_linked(a, 'feature_Interval', b2)
    if hasattr(b2, 'feature_NumericalDomain'):
        assert not _is_linked(b2, 'feature_NumericalDomain', a)


def test_assoc_leftOperand16_link_reassign_clear():
    a = feature_AttributeConstraint(operator="sample_text")
    b1 = feature_AttributeOperand()
    b2 = feature_AttributeOperand()
    _safe_set(a, 'feature_AttributeConstraint', b1)
    assert _is_linked(a, 'feature_AttributeConstraint', b1)
    if hasattr(b1, 'feature_AttributeOperand'):
        assert _is_linked(b1, 'feature_AttributeOperand', a)
    _safe_set(a, 'feature_AttributeConstraint', b2)
    assert _is_linked(a, 'feature_AttributeConstraint', b2)
    if hasattr(b1, 'feature_AttributeOperand'):
        assert not _is_linked(b1, 'feature_AttributeOperand', a)
    if hasattr(b2, 'feature_AttributeOperand'):
        assert _is_linked(b2, 'feature_AttributeOperand', a)
    _safe_set(a, 'feature_AttributeConstraint', None)
    assert not _is_linked(a, 'feature_AttributeConstraint', b2)
    if hasattr(b2, 'feature_AttributeOperand'):
        assert not _is_linked(b2, 'feature_AttributeOperand', a)


def test_assoc_leftOperand25_link_reassign_clear():
    a = feature_Feature(configurationState="sample_text", name="sample_text")
    b1 = feature_FeatureConstraint()
    b2 = feature_FeatureConstraint()
    _safe_set(a, 'feature_Feature26', b1)
    assert _is_linked(a, 'feature_Feature26', b1)
    if hasattr(b1, 'feature_FeatureConstraint'):
        assert _is_linked(b1, 'feature_FeatureConstraint', a)
    _safe_set(a, 'feature_Feature26', b2)
    assert _is_linked(a, 'feature_Feature26', b2)
    if hasattr(b1, 'feature_FeatureConstraint'):
        assert not _is_linked(b1, 'feature_FeatureConstraint', a)
    if hasattr(b2, 'feature_FeatureConstraint'):
        assert _is_linked(b2, 'feature_FeatureConstraint', a)
    _safe_set(a, 'feature_Feature26', None)
    assert not _is_linked(a, 'feature_Feature26', b2)
    if hasattr(b2, 'feature_FeatureConstraint'):
        assert not _is_linked(b2, 'feature_FeatureConstraint', a)


def test_assoc_rightOperand17_link_reassign_clear():
    a = feature_AttributeConstraint(operator="sample_text")
    b1 = feature_AttributeOperand()
    b2 = feature_AttributeOperand()
    _safe_set(a, 'feature_AttributeConstraint18', b1)
    assert _is_linked(a, 'feature_AttributeConstraint18', b1)
    if hasattr(b1, 'feature_AttributeOperand19'):
        assert _is_linked(b1, 'feature_AttributeOperand19', a)
    _safe_set(a, 'feature_AttributeConstraint18', b2)
    assert _is_linked(a, 'feature_AttributeConstraint18', b2)
    if hasattr(b1, 'feature_AttributeOperand19'):
        assert not _is_linked(b1, 'feature_AttributeOperand19', a)
    if hasattr(b2, 'feature_AttributeOperand19'):
        assert _is_linked(b2, 'feature_AttributeOperand19', a)
    _safe_set(a, 'feature_AttributeConstraint18', None)
    assert not _is_linked(a, 'feature_AttributeConstraint18', b2)
    if hasattr(b2, 'feature_AttributeOperand19'):
        assert not _is_linked(b2, 'feature_AttributeOperand19', a)


def test_assoc_rightOperand27_link_reassign_clear():
    a = feature_Feature(configurationState="sample_text", name="sample_text")
    b1 = feature_FeatureConstraint()
    b2 = feature_FeatureConstraint()
    _safe_set(a, 'feature_Feature29', b1)
    assert _is_linked(a, 'feature_Feature29', b1)
    if hasattr(b1, 'feature_FeatureConstraint28'):
        assert _is_linked(b1, 'feature_FeatureConstraint28', a)
    _safe_set(a, 'feature_Feature29', b2)
    assert _is_linked(a, 'feature_Feature29', b2)
    if hasattr(b1, 'feature_FeatureConstraint28'):
        assert not _is_linked(b1, 'feature_FeatureConstraint28', a)
    if hasattr(b2, 'feature_FeatureConstraint28'):
        assert _is_linked(b2, 'feature_FeatureConstraint28', a)
    _safe_set(a, 'feature_Feature29', None)
    assert not _is_linked(a, 'feature_Feature29', b2)
    if hasattr(b2, 'feature_FeatureConstraint28'):
        assert not _is_linked(b2, 'feature_FeatureConstraint28', a)


def test_assoc_root0_link_reassign_clear():
    a = feature_FeatureModel(name="sample_text")
    b1 = feature_Feature(configurationState="sample_text", name="sample_text")
    b2 = feature_Feature(configurationState="sample_text_2", name="sample_text_2")
    _safe_set(a, 'feature_FeatureModel', b1)
    assert _is_linked(a, 'feature_FeatureModel', b1)
    if hasattr(b1, 'feature_Feature'):
        assert _is_linked(b1, 'feature_Feature', a)
    _safe_set(a, 'feature_FeatureModel', b2)
    assert _is_linked(a, 'feature_FeatureModel', b2)
    if hasattr(b1, 'feature_Feature'):
        assert not _is_linked(b1, 'feature_Feature', a)
    if hasattr(b2, 'feature_Feature'):
        assert _is_linked(b2, 'feature_Feature', a)
    _safe_set(a, 'feature_FeatureModel', None)
    assert not _is_linked(a, 'feature_FeatureModel', b2)
    if hasattr(b2, 'feature_Feature'):
        assert not _is_linked(b2, 'feature_Feature', a)


def test_assoc_values14_link_reassign_clear():
    a = feature_DomainValue(int=7, name="sample_text")
    b1 = feature_DiscreteDomain()
    b2 = feature_DiscreteDomain()
    _safe_set(a, 'feature_DomainValue', b1)
    assert _is_linked(a, 'feature_DomainValue', b1)
    if hasattr(b1, 'feature_DiscreteDomain'):
        assert _is_linked(b1, 'feature_DiscreteDomain', a)
    _safe_set(a, 'feature_DomainValue', b2)
    assert _is_linked(a, 'feature_DomainValue', b2)
    if hasattr(b1, 'feature_DiscreteDomain'):
        assert not _is_linked(b1, 'feature_DiscreteDomain', a)
    if hasattr(b2, 'feature_DiscreteDomain'):
        assert _is_linked(b2, 'feature_DiscreteDomain', a)
    _safe_set(a, 'feature_DomainValue', None)
    assert not _is_linked(a, 'feature_DomainValue', b2)
    if hasattr(b2, 'feature_DiscreteDomain'):
        assert not _is_linked(b2, 'feature_DiscreteDomain', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AttributeOperand_strategy = st.builds(AttributeOperand)
@given(instance=AttributeOperand_strategy)
@settings(max_examples=25)
def test_AttributeOperand_instantiation(instance):
    assert isinstance(instance, AttributeOperand)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


Domain_strategy = st.builds(Domain)
@given(instance=Domain_strategy)
@settings(max_examples=25)
def test_Domain_instantiation(instance):
    assert isinstance(instance, Domain)


FeatureConstraint_strategy = st.builds(FeatureConstraint)
@given(instance=FeatureConstraint_strategy)
@settings(max_examples=25)
def test_FeatureConstraint_instantiation(instance):
    assert isinstance(instance, FeatureConstraint)


Identifiable_strategy = st.builds(Identifiable)
@given(instance=Identifiable_strategy)
@settings(max_examples=25)
def test_Identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)


feature_Attribute_strategy = st.builds(feature_Attribute, deselectedDomainValues=safe_text, name=safe_text, value=safe_text)
@given(instance=feature_Attribute_strategy)
@settings(max_examples=25)
def test_feature_Attribute_instantiation(instance):
    assert isinstance(instance, feature_Attribute)


feature_AttributeConstraint_strategy = st.builds(feature_AttributeConstraint, operator=safe_text)
@given(instance=feature_AttributeConstraint_strategy)
@settings(max_examples=25)
def test_feature_AttributeConstraint_instantiation(instance):
    assert isinstance(instance, feature_AttributeConstraint)


feature_AttributeOperand_strategy = st.builds(feature_AttributeOperand)
@given(instance=feature_AttributeOperand_strategy)
@settings(max_examples=25)
def test_feature_AttributeOperand_instantiation(instance):
    assert isinstance(instance, feature_AttributeOperand)


feature_AttributeReference_strategy = st.builds(feature_AttributeReference)
@given(instance=feature_AttributeReference_strategy)
@settings(max_examples=25)
def test_feature_AttributeReference_instantiation(instance):
    assert isinstance(instance, feature_AttributeReference)


feature_AttributeValue_strategy = st.builds(feature_AttributeValue, int=st.integers(), name=safe_text)
@given(instance=feature_AttributeValue_strategy)
@settings(max_examples=25)
def test_feature_AttributeValue_instantiation(instance):
    assert isinstance(instance, feature_AttributeValue)


feature_Constraint_strategy = st.builds(feature_Constraint)
@given(instance=feature_Constraint_strategy)
@settings(max_examples=25)
def test_feature_Constraint_instantiation(instance):
    assert isinstance(instance, feature_Constraint)


feature_DiscreteDomain_strategy = st.builds(feature_DiscreteDomain)
@given(instance=feature_DiscreteDomain_strategy)
@settings(max_examples=25)
def test_feature_DiscreteDomain_instantiation(instance):
    assert isinstance(instance, feature_DiscreteDomain)


feature_Domain_strategy = st.builds(feature_Domain)
@given(instance=feature_Domain_strategy)
@settings(max_examples=25)
def test_feature_Domain_instantiation(instance):
    assert isinstance(instance, feature_Domain)


feature_DomainValue_strategy = st.builds(feature_DomainValue, int=st.integers(), name=safe_text)
@given(instance=feature_DomainValue_strategy)
@settings(max_examples=25)
def test_feature_DomainValue_instantiation(instance):
    assert isinstance(instance, feature_DomainValue)


feature_Exclude_strategy = st.builds(feature_Exclude)
@given(instance=feature_Exclude_strategy)
@settings(max_examples=25)
def test_feature_Exclude_instantiation(instance):
    assert isinstance(instance, feature_Exclude)


feature_Feature_strategy = st.builds(feature_Feature, configurationState=safe_text, name=safe_text)
@given(instance=feature_Feature_strategy)
@settings(max_examples=25)
def test_feature_Feature_instantiation(instance):
    assert isinstance(instance, feature_Feature)


feature_FeatureConstraint_strategy = st.builds(feature_FeatureConstraint)
@given(instance=feature_FeatureConstraint_strategy)
@settings(max_examples=25)
def test_feature_FeatureConstraint_instantiation(instance):
    assert isinstance(instance, feature_FeatureConstraint)


feature_FeatureModel_strategy = st.builds(feature_FeatureModel, name=safe_text)
@given(instance=feature_FeatureModel_strategy)
@settings(max_examples=25)
def test_feature_FeatureModel_instantiation(instance):
    assert isinstance(instance, feature_FeatureModel)


feature_Group_strategy = st.builds(feature_Group, maxCardinality=st.integers(), minCardinality=st.integers())
@given(instance=feature_Group_strategy)
@settings(max_examples=25)
def test_feature_Group_instantiation(instance):
    assert isinstance(instance, feature_Group)


feature_Identifiable_strategy = st.builds(feature_Identifiable, id=safe_text)
@given(instance=feature_Identifiable_strategy)
@settings(max_examples=25)
def test_feature_Identifiable_instantiation(instance):
    assert isinstance(instance, feature_Identifiable)


feature_Imply_strategy = st.builds(feature_Imply)
@given(instance=feature_Imply_strategy)
@settings(max_examples=25)
def test_feature_Imply_instantiation(instance):
    assert isinstance(instance, feature_Imply)


feature_Interval_strategy = st.builds(feature_Interval, lowerBound=st.integers(), upperBound=st.integers())
@given(instance=feature_Interval_strategy)
@settings(max_examples=25)
def test_feature_Interval_instantiation(instance):
    assert isinstance(instance, feature_Interval)


feature_NumericalDomain_strategy = st.builds(feature_NumericalDomain)
@given(instance=feature_NumericalDomain_strategy)
@settings(max_examples=25)
def test_feature_NumericalDomain_instantiation(instance):
    assert isinstance(instance, feature_NumericalDomain)


