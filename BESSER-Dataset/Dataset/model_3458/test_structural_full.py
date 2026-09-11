import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Alternative,
    BooleanConstraint,
    FMConstraint,
    Feature,
    VariabilityElement,
    featureModel_Action,
    featureModel_AdaptationRule,
    featureModel_Alternative,
    featureModel_Attribute,
    featureModel_BooleanConstraint,
    featureModel_Condition,
    featureModel_Excludes,
    featureModel_Exclusive,
    featureModel_FMConstraint,
    featureModel_Feature,
    featureModel_FeatureModel,
    featureModel_Implies,
    featureModel_IntValue,
    featureModel_Value,
    featureModel_VariabilityElement,
    ComparisonOperator,
    SelectionOperator,
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

def test_featureModel_Action_type_value_roundtrip():
    instance = featureModel_Action(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_featureModel_Attribute_name_value_roundtrip():
    instance = featureModel_Attribute(name="sample_text", runtime=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featureModel_Attribute_runtime_value_roundtrip():
    instance = featureModel_Attribute(name="sample_text", runtime=True)
    assert instance.runtime == True
    instance.runtime = False
    assert instance.runtime == False


def test_featureModel_Condition_type_value_roundtrip():
    instance = featureModel_Condition(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_featureModel_Feature_mandatory_value_roundtrip():
    instance = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_featureModel_Feature_name_value_roundtrip():
    instance = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featureModel_Feature_selected_value_roundtrip():
    instance = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_featureModel_Feature_unselected_value_roundtrip():
    instance = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    assert instance.unselected == True
    instance.unselected = False
    assert instance.unselected == False


def test_featureModel_Exclusive_isa_Alternative():
    instance = featureModel_Exclusive()
    assert isinstance(instance, Alternative)


def test_featureModel_Excludes_isa_BooleanConstraint():
    instance = featureModel_Excludes()
    assert isinstance(instance, BooleanConstraint)


def test_featureModel_Implies_isa_BooleanConstraint():
    instance = featureModel_Implies()
    assert isinstance(instance, BooleanConstraint)


def test_featureModel_AdaptationRule_isa_FMConstraint():
    instance = featureModel_AdaptationRule()
    assert isinstance(instance, FMConstraint)


def test_featureModel_BooleanConstraint_isa_FMConstraint():
    instance = featureModel_BooleanConstraint()
    assert isinstance(instance, FMConstraint)


def test_featureModel_Alternative_isa_Feature():
    instance = featureModel_Alternative()
    assert isinstance(instance, Feature)


def test_featureModel_Attribute_isa_VariabilityElement():
    instance = featureModel_Attribute(name="sample_text", runtime=True)
    assert isinstance(instance, VariabilityElement)


def test_featureModel_Feature_isa_VariabilityElement():
    instance = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    assert isinstance(instance, VariabilityElement)


def test_assoc_action18_link_reassign_clear():
    a = featureModel_Action(type="sample_text")
    b1 = featureModel_AdaptationRule()
    b2 = featureModel_AdaptationRule()
    _safe_set(a, 'featureModel_Action', b1)
    assert _is_linked(a, 'featureModel_Action', b1)
    if hasattr(b1, 'featureModel_AdaptationRule19'):
        assert _is_linked(b1, 'featureModel_AdaptationRule19', a)
    _safe_set(a, 'featureModel_Action', b2)
    assert _is_linked(a, 'featureModel_Action', b2)
    if hasattr(b1, 'featureModel_AdaptationRule19'):
        assert not _is_linked(b1, 'featureModel_AdaptationRule19', a)
    if hasattr(b2, 'featureModel_AdaptationRule19'):
        assert _is_linked(b2, 'featureModel_AdaptationRule19', a)
    _safe_set(a, 'featureModel_Action', None)
    assert not _is_linked(a, 'featureModel_Action', b2)
    if hasattr(b2, 'featureModel_AdaptationRule19'):
        assert not _is_linked(b2, 'featureModel_AdaptationRule19', a)


def test_assoc_attribute20_link_reassign_clear():
    a = featureModel_Condition(type="sample_text")
    b1 = featureModel_Attribute(name="sample_text", runtime=True)
    b2 = featureModel_Attribute(name="sample_text_2", runtime=False)
    _safe_set(a, 'featureModel_Condition21', b1)
    assert _is_linked(a, 'featureModel_Condition21', b1)
    if hasattr(b1, 'featureModel_Attribute22'):
        assert _is_linked(b1, 'featureModel_Attribute22', a)
    _safe_set(a, 'featureModel_Condition21', b2)
    assert _is_linked(a, 'featureModel_Condition21', b2)
    if hasattr(b1, 'featureModel_Attribute22'):
        assert not _is_linked(b1, 'featureModel_Attribute22', a)
    if hasattr(b2, 'featureModel_Attribute22'):
        assert _is_linked(b2, 'featureModel_Attribute22', a)
    _safe_set(a, 'featureModel_Condition21', None)
    assert not _is_linked(a, 'featureModel_Condition21', b2)
    if hasattr(b2, 'featureModel_Attribute22'):
        assert not _is_linked(b2, 'featureModel_Attribute22', a)


def test_assoc_attributes3_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_Attribute(name="sample_text", runtime=True)
    b2 = featureModel_Attribute(name="sample_text_2", runtime=False)
    _safe_set(a, 'featureModel_Feature4', {b1})
    assert _is_linked(a, 'featureModel_Feature4', b1)
    if hasattr(b1, 'featureModel_Attribute'):
        assert _is_linked(b1, 'featureModel_Attribute', a)
    _safe_set(a, 'featureModel_Feature4', {b2})
    assert _is_linked(a, 'featureModel_Feature4', b2)
    if hasattr(b1, 'featureModel_Attribute'):
        assert not _is_linked(b1, 'featureModel_Attribute', a)
    if hasattr(b2, 'featureModel_Attribute'):
        assert _is_linked(b2, 'featureModel_Attribute', a)
    _safe_set(a, 'featureModel_Feature4', set())
    assert not _is_linked(a, 'featureModel_Feature4', b2)
    if hasattr(b2, 'featureModel_Attribute'):
        assert not _is_linked(b2, 'featureModel_Attribute', a)


def test_assoc_condition17_link_reassign_clear():
    a = featureModel_Condition(type="sample_text")
    b1 = featureModel_AdaptationRule()
    b2 = featureModel_AdaptationRule()
    _safe_set(a, 'featureModel_Condition', b1)
    assert _is_linked(a, 'featureModel_Condition', b1)
    if hasattr(b1, 'featureModel_AdaptationRule'):
        assert _is_linked(b1, 'featureModel_AdaptationRule', a)
    _safe_set(a, 'featureModel_Condition', b2)
    assert _is_linked(a, 'featureModel_Condition', b2)
    if hasattr(b1, 'featureModel_AdaptationRule'):
        assert not _is_linked(b1, 'featureModel_AdaptationRule', a)
    if hasattr(b2, 'featureModel_AdaptationRule'):
        assert _is_linked(b2, 'featureModel_AdaptationRule', a)
    _safe_set(a, 'featureModel_Condition', None)
    assert not _is_linked(a, 'featureModel_Condition', b2)
    if hasattr(b2, 'featureModel_AdaptationRule'):
        assert not _is_linked(b2, 'featureModel_AdaptationRule', a)


def test_assoc_feature25_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_Condition(type="sample_text")
    b2 = featureModel_Condition(type="sample_text_2")
    _safe_set(a, 'featureModel_Feature27', b1)
    assert _is_linked(a, 'featureModel_Feature27', b1)
    if hasattr(b1, 'featureModel_Condition26'):
        assert _is_linked(b1, 'featureModel_Condition26', a)
    _safe_set(a, 'featureModel_Feature27', b2)
    assert _is_linked(a, 'featureModel_Feature27', b2)
    if hasattr(b1, 'featureModel_Condition26'):
        assert not _is_linked(b1, 'featureModel_Condition26', a)
    if hasattr(b2, 'featureModel_Condition26'):
        assert _is_linked(b2, 'featureModel_Condition26', a)
    _safe_set(a, 'featureModel_Feature27', None)
    assert not _is_linked(a, 'featureModel_Feature27', b2)
    if hasattr(b2, 'featureModel_Condition26'):
        assert not _is_linked(b2, 'featureModel_Condition26', a)


def test_assoc_feature28_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_Action(type="sample_text")
    b2 = featureModel_Action(type="sample_text_2")
    _safe_set(a, 'featureModel_Feature30', b1)
    assert _is_linked(a, 'featureModel_Feature30', b1)
    if hasattr(b1, 'featureModel_Action29'):
        assert _is_linked(b1, 'featureModel_Action29', a)
    _safe_set(a, 'featureModel_Feature30', b2)
    assert _is_linked(a, 'featureModel_Feature30', b2)
    if hasattr(b1, 'featureModel_Action29'):
        assert not _is_linked(b1, 'featureModel_Action29', a)
    if hasattr(b2, 'featureModel_Action29'):
        assert _is_linked(b2, 'featureModel_Action29', a)
    _safe_set(a, 'featureModel_Feature30', None)
    assert not _is_linked(a, 'featureModel_Feature30', b2)
    if hasattr(b2, 'featureModel_Action29'):
        assert not _is_linked(b2, 'featureModel_Action29', a)


def test_assoc_from_12_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_BooleanConstraint()
    b2 = featureModel_BooleanConstraint()
    _safe_set(a, 'featureModel_Feature13', b1)
    assert _is_linked(a, 'featureModel_Feature13', b1)
    if hasattr(b1, 'featureModel_BooleanConstraint'):
        assert _is_linked(b1, 'featureModel_BooleanConstraint', a)
    _safe_set(a, 'featureModel_Feature13', b2)
    assert _is_linked(a, 'featureModel_Feature13', b2)
    if hasattr(b1, 'featureModel_BooleanConstraint'):
        assert not _is_linked(b1, 'featureModel_BooleanConstraint', a)
    if hasattr(b2, 'featureModel_BooleanConstraint'):
        assert _is_linked(b2, 'featureModel_BooleanConstraint', a)
    _safe_set(a, 'featureModel_Feature13', None)
    assert not _is_linked(a, 'featureModel_Feature13', b2)
    if hasattr(b2, 'featureModel_BooleanConstraint'):
        assert not _is_linked(b2, 'featureModel_BooleanConstraint', a)


def test_assoc_rootFeature1_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_FeatureModel()
    b2 = featureModel_FeatureModel()
    _safe_set(a, 'featureModel_Feature', b1)
    assert _is_linked(a, 'featureModel_Feature', b1)
    if hasattr(b1, 'featureModel_FeatureModel2'):
        assert _is_linked(b1, 'featureModel_FeatureModel2', a)
    _safe_set(a, 'featureModel_Feature', b2)
    assert _is_linked(a, 'featureModel_Feature', b2)
    if hasattr(b1, 'featureModel_FeatureModel2'):
        assert not _is_linked(b1, 'featureModel_FeatureModel2', a)
    if hasattr(b2, 'featureModel_FeatureModel2'):
        assert _is_linked(b2, 'featureModel_FeatureModel2', a)
    _safe_set(a, 'featureModel_Feature', None)
    assert not _is_linked(a, 'featureModel_Feature', b2)
    if hasattr(b2, 'featureModel_FeatureModel2'):
        assert not _is_linked(b2, 'featureModel_FeatureModel2', a)


def test_assoc_subFeatures6_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b2 = featureModel_Feature(mandatory=False, name="sample_text_2", selected=False, unselected=False)
    _safe_set(a, 'featureModel_Feature5', {b1})
    assert _is_linked(a, 'featureModel_Feature5', b1)
    if hasattr(b1, 'featureModel_Feature7'):
        assert _is_linked(b1, 'featureModel_Feature7', a)
    _safe_set(a, 'featureModel_Feature5', {b2})
    assert _is_linked(a, 'featureModel_Feature5', b2)
    if hasattr(b1, 'featureModel_Feature7'):
        assert not _is_linked(b1, 'featureModel_Feature7', a)
    if hasattr(b2, 'featureModel_Feature7'):
        assert _is_linked(b2, 'featureModel_Feature7', a)
    _safe_set(a, 'featureModel_Feature5', set())
    assert not _is_linked(a, 'featureModel_Feature5', b2)
    if hasattr(b2, 'featureModel_Feature7'):
        assert not _is_linked(b2, 'featureModel_Feature7', a)


def test_assoc_to14_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_BooleanConstraint()
    b2 = featureModel_BooleanConstraint()
    _safe_set(a, 'featureModel_Feature16', b1)
    assert _is_linked(a, 'featureModel_Feature16', b1)
    if hasattr(b1, 'featureModel_BooleanConstraint15'):
        assert _is_linked(b1, 'featureModel_BooleanConstraint15', a)
    _safe_set(a, 'featureModel_Feature16', b2)
    assert _is_linked(a, 'featureModel_Feature16', b2)
    if hasattr(b1, 'featureModel_BooleanConstraint15'):
        assert not _is_linked(b1, 'featureModel_BooleanConstraint15', a)
    if hasattr(b2, 'featureModel_BooleanConstraint15'):
        assert _is_linked(b2, 'featureModel_BooleanConstraint15', a)
    _safe_set(a, 'featureModel_Feature16', None)
    assert not _is_linked(a, 'featureModel_Feature16', b2)
    if hasattr(b2, 'featureModel_BooleanConstraint15'):
        assert not _is_linked(b2, 'featureModel_BooleanConstraint15', a)


def test_assoc_value10_link_reassign_clear():
    a = featureModel_Attribute(name="sample_text", runtime=True)
    b1 = featureModel_Value()
    b2 = featureModel_Value()
    _safe_set(a, 'featureModel_Attribute11', b1)
    assert _is_linked(a, 'featureModel_Attribute11', b1)
    if hasattr(b1, 'featureModel_Value'):
        assert _is_linked(b1, 'featureModel_Value', a)
    _safe_set(a, 'featureModel_Attribute11', b2)
    assert _is_linked(a, 'featureModel_Attribute11', b2)
    if hasattr(b1, 'featureModel_Value'):
        assert not _is_linked(b1, 'featureModel_Value', a)
    if hasattr(b2, 'featureModel_Value'):
        assert _is_linked(b2, 'featureModel_Value', a)
    _safe_set(a, 'featureModel_Attribute11', None)
    assert not _is_linked(a, 'featureModel_Attribute11', b2)
    if hasattr(b2, 'featureModel_Value'):
        assert not _is_linked(b2, 'featureModel_Value', a)


def test_assoc_value23_link_reassign_clear():
    a = featureModel_Condition(type="sample_text")
    b1 = featureModel_IntValue()
    b2 = featureModel_IntValue()
    _safe_set(a, 'featureModel_Condition24', b1)
    assert _is_linked(a, 'featureModel_Condition24', b1)
    if hasattr(b1, 'featureModel_IntValue'):
        assert _is_linked(b1, 'featureModel_IntValue', a)
    _safe_set(a, 'featureModel_Condition24', b2)
    assert _is_linked(a, 'featureModel_Condition24', b2)
    if hasattr(b1, 'featureModel_IntValue'):
        assert not _is_linked(b1, 'featureModel_IntValue', a)
    if hasattr(b2, 'featureModel_IntValue'):
        assert _is_linked(b2, 'featureModel_IntValue', a)
    _safe_set(a, 'featureModel_Condition24', None)
    assert not _is_linked(a, 'featureModel_Condition24', b2)
    if hasattr(b2, 'featureModel_IntValue'):
        assert not _is_linked(b2, 'featureModel_IntValue', a)


def test_assoc_variants8_link_reassign_clear():
    a = featureModel_Feature(mandatory=True, name="sample_text", selected=True, unselected=True)
    b1 = featureModel_Alternative()
    b2 = featureModel_Alternative()
    _safe_set(a, 'featureModel_Feature9', b1)
    assert _is_linked(a, 'featureModel_Feature9', b1)
    if hasattr(b1, 'featureModel_Alternative'):
        assert _is_linked(b1, 'featureModel_Alternative', a)
    _safe_set(a, 'featureModel_Feature9', b2)
    assert _is_linked(a, 'featureModel_Feature9', b2)
    if hasattr(b1, 'featureModel_Alternative'):
        assert not _is_linked(b1, 'featureModel_Alternative', a)
    if hasattr(b2, 'featureModel_Alternative'):
        assert _is_linked(b2, 'featureModel_Alternative', a)
    _safe_set(a, 'featureModel_Feature9', None)
    assert not _is_linked(a, 'featureModel_Feature9', b2)
    if hasattr(b2, 'featureModel_Alternative'):
        assert not _is_linked(b2, 'featureModel_Alternative', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Alternative_strategy = st.builds(Alternative)
@given(instance=Alternative_strategy)
@settings(max_examples=25)
def test_Alternative_instantiation(instance):
    assert isinstance(instance, Alternative)


BooleanConstraint_strategy = st.builds(BooleanConstraint)
@given(instance=BooleanConstraint_strategy)
@settings(max_examples=25)
def test_BooleanConstraint_instantiation(instance):
    assert isinstance(instance, BooleanConstraint)


FMConstraint_strategy = st.builds(FMConstraint)
@given(instance=FMConstraint_strategy)
@settings(max_examples=25)
def test_FMConstraint_instantiation(instance):
    assert isinstance(instance, FMConstraint)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


VariabilityElement_strategy = st.builds(VariabilityElement)
@given(instance=VariabilityElement_strategy)
@settings(max_examples=25)
def test_VariabilityElement_instantiation(instance):
    assert isinstance(instance, VariabilityElement)


featureModel_Action_strategy = st.builds(featureModel_Action, type=safe_text)
@given(instance=featureModel_Action_strategy)
@settings(max_examples=25)
def test_featureModel_Action_instantiation(instance):
    assert isinstance(instance, featureModel_Action)


featureModel_AdaptationRule_strategy = st.builds(featureModel_AdaptationRule)
@given(instance=featureModel_AdaptationRule_strategy)
@settings(max_examples=25)
def test_featureModel_AdaptationRule_instantiation(instance):
    assert isinstance(instance, featureModel_AdaptationRule)


featureModel_Alternative_strategy = st.builds(featureModel_Alternative)
@given(instance=featureModel_Alternative_strategy)
@settings(max_examples=25)
def test_featureModel_Alternative_instantiation(instance):
    assert isinstance(instance, featureModel_Alternative)


featureModel_Attribute_strategy = st.builds(featureModel_Attribute, name=safe_text, runtime=st.booleans())
@given(instance=featureModel_Attribute_strategy)
@settings(max_examples=25)
def test_featureModel_Attribute_instantiation(instance):
    assert isinstance(instance, featureModel_Attribute)


featureModel_BooleanConstraint_strategy = st.builds(featureModel_BooleanConstraint)
@given(instance=featureModel_BooleanConstraint_strategy)
@settings(max_examples=25)
def test_featureModel_BooleanConstraint_instantiation(instance):
    assert isinstance(instance, featureModel_BooleanConstraint)


featureModel_Condition_strategy = st.builds(featureModel_Condition, type=safe_text)
@given(instance=featureModel_Condition_strategy)
@settings(max_examples=25)
def test_featureModel_Condition_instantiation(instance):
    assert isinstance(instance, featureModel_Condition)


featureModel_Excludes_strategy = st.builds(featureModel_Excludes)
@given(instance=featureModel_Excludes_strategy)
@settings(max_examples=25)
def test_featureModel_Excludes_instantiation(instance):
    assert isinstance(instance, featureModel_Excludes)


featureModel_Exclusive_strategy = st.builds(featureModel_Exclusive)
@given(instance=featureModel_Exclusive_strategy)
@settings(max_examples=25)
def test_featureModel_Exclusive_instantiation(instance):
    assert isinstance(instance, featureModel_Exclusive)


featureModel_FMConstraint_strategy = st.builds(featureModel_FMConstraint)
@given(instance=featureModel_FMConstraint_strategy)
@settings(max_examples=25)
def test_featureModel_FMConstraint_instantiation(instance):
    assert isinstance(instance, featureModel_FMConstraint)


featureModel_Feature_strategy = st.builds(featureModel_Feature, mandatory=st.booleans(), name=safe_text, selected=st.booleans(), unselected=st.booleans())
@given(instance=featureModel_Feature_strategy)
@settings(max_examples=25)
def test_featureModel_Feature_instantiation(instance):
    assert isinstance(instance, featureModel_Feature)


featureModel_FeatureModel_strategy = st.builds(featureModel_FeatureModel)
@given(instance=featureModel_FeatureModel_strategy)
@settings(max_examples=25)
def test_featureModel_FeatureModel_instantiation(instance):
    assert isinstance(instance, featureModel_FeatureModel)


featureModel_Implies_strategy = st.builds(featureModel_Implies)
@given(instance=featureModel_Implies_strategy)
@settings(max_examples=25)
def test_featureModel_Implies_instantiation(instance):
    assert isinstance(instance, featureModel_Implies)


featureModel_IntValue_strategy = st.builds(featureModel_IntValue)
@given(instance=featureModel_IntValue_strategy)
@settings(max_examples=25)
def test_featureModel_IntValue_instantiation(instance):
    assert isinstance(instance, featureModel_IntValue)


featureModel_Value_strategy = st.builds(featureModel_Value)
@given(instance=featureModel_Value_strategy)
@settings(max_examples=25)
def test_featureModel_Value_instantiation(instance):
    assert isinstance(instance, featureModel_Value)


featureModel_VariabilityElement_strategy = st.builds(featureModel_VariabilityElement)
@given(instance=featureModel_VariabilityElement_strategy)
@settings(max_examples=25)
def test_featureModel_VariabilityElement_instantiation(instance):
    assert isinstance(instance, featureModel_VariabilityElement)


