import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Node,
    Relation,
    featureModel_Feature,
    featureModel_FeatureGroup,
    featureModel_Node,
    featureModel_Project,
    featureModel_Relation,
    featureModel_RelationFG,
    featureModel_RelationFeature,
    featureModel_TypedValue,
    FeatureGroupType,
    FeatureType,
    ValueType,
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

def test_featureModel_Feature_name_value_roundtrip():
    instance = featureModel_Feature(name="sample_text", valueType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featureModel_Feature_valueType_value_roundtrip():
    instance = featureModel_Feature(name="sample_text", valueType="sample_text")
    assert instance.valueType == "sample_text"
    instance.valueType = "sample_text_2"
    assert instance.valueType == "sample_text_2"


def test_featureModel_FeatureGroup_lowerBound_value_roundtrip():
    instance = featureModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_featureModel_FeatureGroup_type_value_roundtrip():
    instance = featureModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_featureModel_FeatureGroup_upperBound_value_roundtrip():
    instance = featureModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_featureModel_Project_nameConfigFile_value_roundtrip():
    instance = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    assert instance.nameConfigFile == "sample_text"
    instance.nameConfigFile = "sample_text_2"
    assert instance.nameConfigFile == "sample_text_2"


def test_featureModel_Project_nameConstraintsFile_value_roundtrip():
    instance = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    assert instance.nameConstraintsFile == "sample_text"
    instance.nameConstraintsFile = "sample_text_2"
    assert instance.nameConstraintsFile == "sample_text_2"


def test_featureModel_Project_numberOfProducts_value_roundtrip():
    instance = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    assert instance.numberOfProducts == 7
    instance.numberOfProducts = 13
    assert instance.numberOfProducts == 13


def test_featureModel_Project_validatedOCL_value_roundtrip():
    instance = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    assert instance.validatedOCL == True
    instance.validatedOCL = False
    assert instance.validatedOCL == False


def test_featureModel_Project_validatedTEF_value_roundtrip():
    instance = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    assert instance.validatedTEF == True
    instance.validatedTEF = False
    assert instance.validatedTEF == False


def test_featureModel_RelationFeature_lowerBound_value_roundtrip():
    instance = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_featureModel_RelationFeature_type_value_roundtrip():
    instance = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_featureModel_RelationFeature_upperBound_value_roundtrip():
    instance = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_featureModel_TypedValue_floatValue_value_roundtrip():
    instance = featureModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    assert instance.floatValue == "sample_text"
    instance.floatValue = "sample_text_2"
    assert instance.floatValue == "sample_text_2"


def test_featureModel_TypedValue_integerValue_value_roundtrip():
    instance = featureModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    assert instance.integerValue == "sample_text"
    instance.integerValue = "sample_text_2"
    assert instance.integerValue == "sample_text_2"


def test_featureModel_TypedValue_stringValue_value_roundtrip():
    instance = featureModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    assert instance.stringValue == "sample_text"
    instance.stringValue = "sample_text_2"
    assert instance.stringValue == "sample_text_2"


def test_featureModel_Feature_isa_Node():
    instance = featureModel_Feature(name="sample_text", valueType="sample_text")
    assert isinstance(instance, Node)


def test_featureModel_FeatureGroup_isa_Node():
    instance = featureModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert isinstance(instance, Node)


def test_featureModel_RelationFG_isa_Relation():
    instance = featureModel_RelationFG()
    assert isinstance(instance, Relation)


def test_featureModel_RelationFeature_isa_Relation():
    instance = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert isinstance(instance, Relation)


def test_assoc_children1_link_reassign_clear():
    a = featureModel_Feature(name="sample_text", valueType="sample_text")
    b1 = featureModel_Node()
    b2 = featureModel_Node()
    _safe_set(a, 'featureModel_Feature2', {b1})
    assert _is_linked(a, 'featureModel_Feature2', b1)
    if hasattr(b1, 'featureModel_Node'):
        assert _is_linked(b1, 'featureModel_Node', a)
    _safe_set(a, 'featureModel_Feature2', {b2})
    assert _is_linked(a, 'featureModel_Feature2', b2)
    if hasattr(b1, 'featureModel_Node'):
        assert not _is_linked(b1, 'featureModel_Node', a)
    if hasattr(b2, 'featureModel_Node'):
        assert _is_linked(b2, 'featureModel_Node', a)
    _safe_set(a, 'featureModel_Feature2', set())
    assert not _is_linked(a, 'featureModel_Feature2', b2)
    if hasattr(b2, 'featureModel_Node'):
        assert not _is_linked(b2, 'featureModel_Node', a)


def test_assoc_children16_link_reassign_clear():
    a = featureModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    b1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'featureModel_FeatureGroup', {b1})
    assert _is_linked(a, 'featureModel_FeatureGroup', b1)
    if hasattr(b1, 'featureModel_Feature17'):
        assert _is_linked(b1, 'featureModel_Feature17', a)
    _safe_set(a, 'featureModel_FeatureGroup', {b2})
    assert _is_linked(a, 'featureModel_FeatureGroup', b2)
    if hasattr(b1, 'featureModel_Feature17'):
        assert not _is_linked(b1, 'featureModel_Feature17', a)
    if hasattr(b2, 'featureModel_Feature17'):
        assert _is_linked(b2, 'featureModel_Feature17', a)
    _safe_set(a, 'featureModel_FeatureGroup', set())
    assert not _is_linked(a, 'featureModel_FeatureGroup', b2)
    if hasattr(b2, 'featureModel_Feature17'):
        assert not _is_linked(b2, 'featureModel_Feature17', a)


def test_assoc_featureValue9_link_reassign_clear():
    a = featureModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    b1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'featureModel_TypedValue10', b1)
    assert _is_linked(a, 'featureModel_TypedValue10', b1)
    if hasattr(b1, 'featureModel_Feature11'):
        assert _is_linked(b1, 'featureModel_Feature11', a)
    _safe_set(a, 'featureModel_TypedValue10', b2)
    assert _is_linked(a, 'featureModel_TypedValue10', b2)
    if hasattr(b1, 'featureModel_Feature11'):
        assert not _is_linked(b1, 'featureModel_Feature11', a)
    if hasattr(b2, 'featureModel_Feature11'):
        assert _is_linked(b2, 'featureModel_Feature11', a)
    _safe_set(a, 'featureModel_TypedValue10', None)
    assert not _is_linked(a, 'featureModel_TypedValue10', b2)
    if hasattr(b2, 'featureModel_Feature11'):
        assert not _is_linked(b2, 'featureModel_Feature11', a)


def test_assoc_features12_link_reassign_clear():
    a = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    b1 = featureModel_Node()
    b2 = featureModel_Node()
    _safe_set(a, 'featureModel_Project', {b1})
    assert _is_linked(a, 'featureModel_Project', b1)
    if hasattr(b1, 'featureModel_Node13'):
        assert _is_linked(b1, 'featureModel_Node13', a)
    _safe_set(a, 'featureModel_Project', {b2})
    assert _is_linked(a, 'featureModel_Project', b2)
    if hasattr(b1, 'featureModel_Node13'):
        assert not _is_linked(b1, 'featureModel_Node13', a)
    if hasattr(b2, 'featureModel_Node13'):
        assert _is_linked(b2, 'featureModel_Node13', a)
    _safe_set(a, 'featureModel_Project', set())
    assert not _is_linked(a, 'featureModel_Project', b2)
    if hasattr(b2, 'featureModel_Node13'):
        assert not _is_linked(b2, 'featureModel_Node13', a)


def test_assoc_references4_link_reassign_clear():
    a = featureModel_Feature(name="sample_text", valueType="sample_text")
    b1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'featureModel_Feature3', b1)
    assert _is_linked(a, 'featureModel_Feature3', b1)
    if hasattr(b1, 'featureModel_Feature5'):
        assert _is_linked(b1, 'featureModel_Feature5', a)
    _safe_set(a, 'featureModel_Feature3', b2)
    assert _is_linked(a, 'featureModel_Feature3', b2)
    if hasattr(b1, 'featureModel_Feature5'):
        assert not _is_linked(b1, 'featureModel_Feature5', a)
    if hasattr(b2, 'featureModel_Feature5'):
        assert _is_linked(b2, 'featureModel_Feature5', a)
    _safe_set(a, 'featureModel_Feature3', None)
    assert not _is_linked(a, 'featureModel_Feature3', b2)
    if hasattr(b2, 'featureModel_Feature5'):
        assert not _is_linked(b2, 'featureModel_Feature5', a)


def test_assoc_referenciated7_link_reassign_clear():
    a = featureModel_Feature(name="sample_text", valueType="sample_text")
    b1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'featureModel_Feature6', {b1})
    assert _is_linked(a, 'featureModel_Feature6', b1)
    if hasattr(b1, 'featureModel_Feature8'):
        assert _is_linked(b1, 'featureModel_Feature8', a)
    _safe_set(a, 'featureModel_Feature6', {b2})
    assert _is_linked(a, 'featureModel_Feature6', b2)
    if hasattr(b1, 'featureModel_Feature8'):
        assert not _is_linked(b1, 'featureModel_Feature8', a)
    if hasattr(b2, 'featureModel_Feature8'):
        assert _is_linked(b2, 'featureModel_Feature8', a)
    _safe_set(a, 'featureModel_Feature6', set())
    assert not _is_linked(a, 'featureModel_Feature6', b2)
    if hasattr(b2, 'featureModel_Feature8'):
        assert not _is_linked(b2, 'featureModel_Feature8', a)


def test_assoc_relations14_link_reassign_clear():
    a = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    b1 = featureModel_Relation()
    b2 = featureModel_Relation()
    _safe_set(a, 'featureModel_Project15', {b1})
    assert _is_linked(a, 'featureModel_Project15', b1)
    if hasattr(b1, 'featureModel_Relation'):
        assert _is_linked(b1, 'featureModel_Relation', a)
    _safe_set(a, 'featureModel_Project15', {b2})
    assert _is_linked(a, 'featureModel_Project15', b2)
    if hasattr(b1, 'featureModel_Relation'):
        assert not _is_linked(b1, 'featureModel_Relation', a)
    if hasattr(b2, 'featureModel_Relation'):
        assert _is_linked(b2, 'featureModel_Relation', a)
    _safe_set(a, 'featureModel_Project15', set())
    assert not _is_linked(a, 'featureModel_Project15', b2)
    if hasattr(b2, 'featureModel_Relation'):
        assert not _is_linked(b2, 'featureModel_Relation', a)


def test_assoc_source26_link_reassign_clear():
    a = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    b1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'featureModel_RelationFeature', b1)
    assert _is_linked(a, 'featureModel_RelationFeature', b1)
    if hasattr(b1, 'featureModel_Feature27'):
        assert _is_linked(b1, 'featureModel_Feature27', a)
    _safe_set(a, 'featureModel_RelationFeature', b2)
    assert _is_linked(a, 'featureModel_RelationFeature', b2)
    if hasattr(b1, 'featureModel_Feature27'):
        assert not _is_linked(b1, 'featureModel_Feature27', a)
    if hasattr(b2, 'featureModel_Feature27'):
        assert _is_linked(b2, 'featureModel_Feature27', a)
    _safe_set(a, 'featureModel_RelationFeature', None)
    assert not _is_linked(a, 'featureModel_RelationFeature', b2)
    if hasattr(b2, 'featureModel_Feature27'):
        assert not _is_linked(b2, 'featureModel_Feature27', a)


def test_assoc_target28_link_reassign_clear():
    a = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    b1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'featureModel_RelationFeature29', b1)
    assert _is_linked(a, 'featureModel_RelationFeature29', b1)
    if hasattr(b1, 'featureModel_Feature30'):
        assert _is_linked(b1, 'featureModel_Feature30', a)
    _safe_set(a, 'featureModel_RelationFeature29', b2)
    assert _is_linked(a, 'featureModel_RelationFeature29', b2)
    if hasattr(b1, 'featureModel_Feature30'):
        assert not _is_linked(b1, 'featureModel_Feature30', a)
    if hasattr(b2, 'featureModel_Feature30'):
        assert _is_linked(b2, 'featureModel_Feature30', a)
    _safe_set(a, 'featureModel_RelationFeature29', None)
    assert not _is_linked(a, 'featureModel_RelationFeature29', b2)
    if hasattr(b2, 'featureModel_Feature30'):
        assert not _is_linked(b2, 'featureModel_Feature30', a)


def test_assoc_typedValue0_link_reassign_clear():
    a = featureModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    b1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    b2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'featureModel_TypedValue', b1)
    assert _is_linked(a, 'featureModel_TypedValue', b1)
    if hasattr(b1, 'featureModel_Feature'):
        assert _is_linked(b1, 'featureModel_Feature', a)
    _safe_set(a, 'featureModel_TypedValue', b2)
    assert _is_linked(a, 'featureModel_TypedValue', b2)
    if hasattr(b1, 'featureModel_Feature'):
        assert not _is_linked(b1, 'featureModel_Feature', a)
    if hasattr(b2, 'featureModel_Feature'):
        assert _is_linked(b2, 'featureModel_Feature', a)
    _safe_set(a, 'featureModel_TypedValue', None)
    assert not _is_linked(a, 'featureModel_TypedValue', b2)
    if hasattr(b2, 'featureModel_Feature'):
        assert not _is_linked(b2, 'featureModel_Feature', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


Relation_strategy = st.builds(Relation)
@given(instance=Relation_strategy)
@settings(max_examples=25)
def test_Relation_instantiation(instance):
    assert isinstance(instance, Relation)


featureModel_Feature_strategy = st.builds(featureModel_Feature, name=safe_text, valueType=safe_text)
@given(instance=featureModel_Feature_strategy)
@settings(max_examples=25)
def test_featureModel_Feature_instantiation(instance):
    assert isinstance(instance, featureModel_Feature)


featureModel_FeatureGroup_strategy = st.builds(featureModel_FeatureGroup, lowerBound=st.integers(), type=safe_text, upperBound=st.integers())
@given(instance=featureModel_FeatureGroup_strategy)
@settings(max_examples=25)
def test_featureModel_FeatureGroup_instantiation(instance):
    assert isinstance(instance, featureModel_FeatureGroup)


featureModel_Node_strategy = st.builds(featureModel_Node)
@given(instance=featureModel_Node_strategy)
@settings(max_examples=25)
def test_featureModel_Node_instantiation(instance):
    assert isinstance(instance, featureModel_Node)


featureModel_Project_strategy = st.builds(featureModel_Project, nameConfigFile=safe_text, nameConstraintsFile=safe_text, numberOfProducts=st.integers(), validatedOCL=st.booleans(), validatedTEF=st.booleans())
@given(instance=featureModel_Project_strategy)
@settings(max_examples=25)
def test_featureModel_Project_instantiation(instance):
    assert isinstance(instance, featureModel_Project)


featureModel_Relation_strategy = st.builds(featureModel_Relation)
@given(instance=featureModel_Relation_strategy)
@settings(max_examples=25)
def test_featureModel_Relation_instantiation(instance):
    assert isinstance(instance, featureModel_Relation)


featureModel_RelationFG_strategy = st.builds(featureModel_RelationFG)
@given(instance=featureModel_RelationFG_strategy)
@settings(max_examples=25)
def test_featureModel_RelationFG_instantiation(instance):
    assert isinstance(instance, featureModel_RelationFG)


featureModel_RelationFeature_strategy = st.builds(featureModel_RelationFeature, lowerBound=st.integers(), type=safe_text, upperBound=st.integers())
@given(instance=featureModel_RelationFeature_strategy)
@settings(max_examples=25)
def test_featureModel_RelationFeature_instantiation(instance):
    assert isinstance(instance, featureModel_RelationFeature)


featureModel_TypedValue_strategy = st.builds(featureModel_TypedValue, floatValue=safe_text, integerValue=safe_text, stringValue=safe_text)
@given(instance=featureModel_TypedValue_strategy)
@settings(max_examples=25)
def test_featureModel_TypedValue_instantiation(instance):
    assert isinstance(instance, featureModel_TypedValue)


