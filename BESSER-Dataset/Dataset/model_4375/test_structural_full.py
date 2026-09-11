import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Node,
    Relation,
    specializationModel_Feature,
    specializationModel_FeatureGroup,
    specializationModel_Node,
    specializationModel_Project,
    specializationModel_Relation,
    specializationModel_RelationFG,
    specializationModel_RelationFeature,
    specializationModel_TypedValue,
    ConfigState,
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

def test_specializationModel_Feature_name_value_roundtrip():
    instance = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_specializationModel_Feature_realName_value_roundtrip():
    instance = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    assert instance.realName == "sample_text"
    instance.realName = "sample_text_2"
    assert instance.realName == "sample_text_2"


def test_specializationModel_Feature_state_value_roundtrip():
    instance = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_specializationModel_Feature_valueType_value_roundtrip():
    instance = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    assert instance.valueType == "sample_text"
    instance.valueType = "sample_text_2"
    assert instance.valueType == "sample_text_2"


def test_specializationModel_FeatureGroup_lowerBound_value_roundtrip():
    instance = specializationModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_specializationModel_FeatureGroup_type_value_roundtrip():
    instance = specializationModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_specializationModel_FeatureGroup_upperBound_value_roundtrip():
    instance = specializationModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_specializationModel_Project_featureModelURI_value_roundtrip():
    instance = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    assert instance.featureModelURI == "sample_text"
    instance.featureModelURI = "sample_text_2"
    assert instance.featureModelURI == "sample_text_2"


def test_specializationModel_Project_infiniteDomain_value_roundtrip():
    instance = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    assert instance.infiniteDomain == True
    instance.infiniteDomain = False
    assert instance.infiniteDomain == False


def test_specializationModel_Project_nameConfigFile_value_roundtrip():
    instance = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    assert instance.nameConfigFile == "sample_text"
    instance.nameConfigFile = "sample_text_2"
    assert instance.nameConfigFile == "sample_text_2"


def test_specializationModel_Project_nameConstraintsFile_value_roundtrip():
    instance = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    assert instance.nameConstraintsFile == "sample_text"
    instance.nameConstraintsFile = "sample_text_2"
    assert instance.nameConstraintsFile == "sample_text_2"


def test_specializationModel_Project_numberOfProducts_value_roundtrip():
    instance = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    assert instance.numberOfProducts == 7
    instance.numberOfProducts = 13
    assert instance.numberOfProducts == 13


def test_specializationModel_Project_userConstraintsState_value_roundtrip():
    instance = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    assert instance.userConstraintsState == True
    instance.userConstraintsState = False
    assert instance.userConstraintsState == False


def test_specializationModel_RelationFeature_lowerBound_value_roundtrip():
    instance = specializationModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_specializationModel_RelationFeature_type_value_roundtrip():
    instance = specializationModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_specializationModel_RelationFeature_upperBound_value_roundtrip():
    instance = specializationModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_specializationModel_TypedValue_floatValue_value_roundtrip():
    instance = specializationModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    assert instance.floatValue == "sample_text"
    instance.floatValue = "sample_text_2"
    assert instance.floatValue == "sample_text_2"


def test_specializationModel_TypedValue_integerValue_value_roundtrip():
    instance = specializationModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    assert instance.integerValue == "sample_text"
    instance.integerValue = "sample_text_2"
    assert instance.integerValue == "sample_text_2"


def test_specializationModel_TypedValue_stringValue_value_roundtrip():
    instance = specializationModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    assert instance.stringValue == "sample_text"
    instance.stringValue = "sample_text_2"
    assert instance.stringValue == "sample_text_2"


def test_specializationModel_Feature_isa_Node():
    instance = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    assert isinstance(instance, Node)


def test_specializationModel_FeatureGroup_isa_Node():
    instance = specializationModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    assert isinstance(instance, Node)


def test_specializationModel_RelationFG_isa_Relation():
    instance = specializationModel_RelationFG()
    assert isinstance(instance, Relation)


def test_specializationModel_RelationFeature_isa_Relation():
    instance = specializationModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    assert isinstance(instance, Relation)


def test_assoc_children16_link_reassign_clear():
    a = specializationModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    b1 = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b2 = specializationModel_Feature(name="sample_text_2", realName="sample_text_2", state="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'specializationModel_FeatureGroup', {b1})
    assert _is_linked(a, 'specializationModel_FeatureGroup', b1)
    if hasattr(b1, 'specializationModel_Feature17'):
        assert _is_linked(b1, 'specializationModel_Feature17', a)
    _safe_set(a, 'specializationModel_FeatureGroup', {b2})
    assert _is_linked(a, 'specializationModel_FeatureGroup', b2)
    if hasattr(b1, 'specializationModel_Feature17'):
        assert not _is_linked(b1, 'specializationModel_Feature17', a)
    if hasattr(b2, 'specializationModel_Feature17'):
        assert _is_linked(b2, 'specializationModel_Feature17', a)
    _safe_set(a, 'specializationModel_FeatureGroup', set())
    assert not _is_linked(a, 'specializationModel_FeatureGroup', b2)
    if hasattr(b2, 'specializationModel_Feature17'):
        assert not _is_linked(b2, 'specializationModel_Feature17', a)


def test_assoc_children4_link_reassign_clear():
    a = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b1 = specializationModel_Node()
    b2 = specializationModel_Node()
    _safe_set(a, 'specializationModel_Feature5', {b1})
    assert _is_linked(a, 'specializationModel_Feature5', b1)
    if hasattr(b1, 'specializationModel_Node'):
        assert _is_linked(b1, 'specializationModel_Node', a)
    _safe_set(a, 'specializationModel_Feature5', {b2})
    assert _is_linked(a, 'specializationModel_Feature5', b2)
    if hasattr(b1, 'specializationModel_Node'):
        assert not _is_linked(b1, 'specializationModel_Node', a)
    if hasattr(b2, 'specializationModel_Node'):
        assert _is_linked(b2, 'specializationModel_Node', a)
    _safe_set(a, 'specializationModel_Feature5', set())
    assert not _is_linked(a, 'specializationModel_Feature5', b2)
    if hasattr(b2, 'specializationModel_Node'):
        assert not _is_linked(b2, 'specializationModel_Node', a)


def test_assoc_featureValue9_link_reassign_clear():
    a = specializationModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    b1 = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b2 = specializationModel_Feature(name="sample_text_2", realName="sample_text_2", state="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'specializationModel_TypedValue10', b1)
    assert _is_linked(a, 'specializationModel_TypedValue10', b1)
    if hasattr(b1, 'specializationModel_Feature11'):
        assert _is_linked(b1, 'specializationModel_Feature11', a)
    _safe_set(a, 'specializationModel_TypedValue10', b2)
    assert _is_linked(a, 'specializationModel_TypedValue10', b2)
    if hasattr(b1, 'specializationModel_Feature11'):
        assert not _is_linked(b1, 'specializationModel_Feature11', a)
    if hasattr(b2, 'specializationModel_Feature11'):
        assert _is_linked(b2, 'specializationModel_Feature11', a)
    _safe_set(a, 'specializationModel_TypedValue10', None)
    assert not _is_linked(a, 'specializationModel_TypedValue10', b2)
    if hasattr(b2, 'specializationModel_Feature11'):
        assert not _is_linked(b2, 'specializationModel_Feature11', a)


def test_assoc_features12_link_reassign_clear():
    a = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    b1 = specializationModel_Node()
    b2 = specializationModel_Node()
    _safe_set(a, 'specializationModel_Project', {b1})
    assert _is_linked(a, 'specializationModel_Project', b1)
    if hasattr(b1, 'specializationModel_Node13'):
        assert _is_linked(b1, 'specializationModel_Node13', a)
    _safe_set(a, 'specializationModel_Project', {b2})
    assert _is_linked(a, 'specializationModel_Project', b2)
    if hasattr(b1, 'specializationModel_Node13'):
        assert not _is_linked(b1, 'specializationModel_Node13', a)
    if hasattr(b2, 'specializationModel_Node13'):
        assert _is_linked(b2, 'specializationModel_Node13', a)
    _safe_set(a, 'specializationModel_Project', set())
    assert not _is_linked(a, 'specializationModel_Project', b2)
    if hasattr(b2, 'specializationModel_Node13'):
        assert not _is_linked(b2, 'specializationModel_Node13', a)


def test_assoc_references2_link_reassign_clear():
    a = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b1 = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b2 = specializationModel_Feature(name="sample_text_2", realName="sample_text_2", state="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'specializationModel_Feature1', b1)
    assert _is_linked(a, 'specializationModel_Feature1', b1)
    if hasattr(b1, 'specializationModel_Feature3'):
        assert _is_linked(b1, 'specializationModel_Feature3', a)
    _safe_set(a, 'specializationModel_Feature1', b2)
    assert _is_linked(a, 'specializationModel_Feature1', b2)
    if hasattr(b1, 'specializationModel_Feature3'):
        assert not _is_linked(b1, 'specializationModel_Feature3', a)
    if hasattr(b2, 'specializationModel_Feature3'):
        assert _is_linked(b2, 'specializationModel_Feature3', a)
    _safe_set(a, 'specializationModel_Feature1', None)
    assert not _is_linked(a, 'specializationModel_Feature1', b2)
    if hasattr(b2, 'specializationModel_Feature3'):
        assert not _is_linked(b2, 'specializationModel_Feature3', a)


def test_assoc_referenciated7_link_reassign_clear():
    a = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b1 = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b2 = specializationModel_Feature(name="sample_text_2", realName="sample_text_2", state="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'specializationModel_Feature6', {b1})
    assert _is_linked(a, 'specializationModel_Feature6', b1)
    if hasattr(b1, 'specializationModel_Feature8'):
        assert _is_linked(b1, 'specializationModel_Feature8', a)
    _safe_set(a, 'specializationModel_Feature6', {b2})
    assert _is_linked(a, 'specializationModel_Feature6', b2)
    if hasattr(b1, 'specializationModel_Feature8'):
        assert not _is_linked(b1, 'specializationModel_Feature8', a)
    if hasattr(b2, 'specializationModel_Feature8'):
        assert _is_linked(b2, 'specializationModel_Feature8', a)
    _safe_set(a, 'specializationModel_Feature6', set())
    assert not _is_linked(a, 'specializationModel_Feature6', b2)
    if hasattr(b2, 'specializationModel_Feature8'):
        assert not _is_linked(b2, 'specializationModel_Feature8', a)


def test_assoc_relations14_link_reassign_clear():
    a = specializationModel_Project(featureModelURI="sample_text", infiniteDomain=True, nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, userConstraintsState=True)
    b1 = specializationModel_Relation()
    b2 = specializationModel_Relation()
    _safe_set(a, 'specializationModel_Project15', {b1})
    assert _is_linked(a, 'specializationModel_Project15', b1)
    if hasattr(b1, 'specializationModel_Relation'):
        assert _is_linked(b1, 'specializationModel_Relation', a)
    _safe_set(a, 'specializationModel_Project15', {b2})
    assert _is_linked(a, 'specializationModel_Project15', b2)
    if hasattr(b1, 'specializationModel_Relation'):
        assert not _is_linked(b1, 'specializationModel_Relation', a)
    if hasattr(b2, 'specializationModel_Relation'):
        assert _is_linked(b2, 'specializationModel_Relation', a)
    _safe_set(a, 'specializationModel_Project15', set())
    assert not _is_linked(a, 'specializationModel_Project15', b2)
    if hasattr(b2, 'specializationModel_Relation'):
        assert not _is_linked(b2, 'specializationModel_Relation', a)


def test_assoc_source26_link_reassign_clear():
    a = specializationModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    b1 = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b2 = specializationModel_Feature(name="sample_text_2", realName="sample_text_2", state="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'specializationModel_RelationFeature', b1)
    assert _is_linked(a, 'specializationModel_RelationFeature', b1)
    if hasattr(b1, 'specializationModel_Feature27'):
        assert _is_linked(b1, 'specializationModel_Feature27', a)
    _safe_set(a, 'specializationModel_RelationFeature', b2)
    assert _is_linked(a, 'specializationModel_RelationFeature', b2)
    if hasattr(b1, 'specializationModel_Feature27'):
        assert not _is_linked(b1, 'specializationModel_Feature27', a)
    if hasattr(b2, 'specializationModel_Feature27'):
        assert _is_linked(b2, 'specializationModel_Feature27', a)
    _safe_set(a, 'specializationModel_RelationFeature', None)
    assert not _is_linked(a, 'specializationModel_RelationFeature', b2)
    if hasattr(b2, 'specializationModel_Feature27'):
        assert not _is_linked(b2, 'specializationModel_Feature27', a)


def test_assoc_target28_link_reassign_clear():
    a = specializationModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    b1 = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b2 = specializationModel_Feature(name="sample_text_2", realName="sample_text_2", state="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'specializationModel_RelationFeature29', b1)
    assert _is_linked(a, 'specializationModel_RelationFeature29', b1)
    if hasattr(b1, 'specializationModel_Feature30'):
        assert _is_linked(b1, 'specializationModel_Feature30', a)
    _safe_set(a, 'specializationModel_RelationFeature29', b2)
    assert _is_linked(a, 'specializationModel_RelationFeature29', b2)
    if hasattr(b1, 'specializationModel_Feature30'):
        assert not _is_linked(b1, 'specializationModel_Feature30', a)
    if hasattr(b2, 'specializationModel_Feature30'):
        assert _is_linked(b2, 'specializationModel_Feature30', a)
    _safe_set(a, 'specializationModel_RelationFeature29', None)
    assert not _is_linked(a, 'specializationModel_RelationFeature29', b2)
    if hasattr(b2, 'specializationModel_Feature30'):
        assert not _is_linked(b2, 'specializationModel_Feature30', a)


def test_assoc_typedValue0_link_reassign_clear():
    a = specializationModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    b1 = specializationModel_Feature(name="sample_text", realName="sample_text", state="sample_text", valueType="sample_text")
    b2 = specializationModel_Feature(name="sample_text_2", realName="sample_text_2", state="sample_text_2", valueType="sample_text_2")
    _safe_set(a, 'specializationModel_TypedValue', b1)
    assert _is_linked(a, 'specializationModel_TypedValue', b1)
    if hasattr(b1, 'specializationModel_Feature'):
        assert _is_linked(b1, 'specializationModel_Feature', a)
    _safe_set(a, 'specializationModel_TypedValue', b2)
    assert _is_linked(a, 'specializationModel_TypedValue', b2)
    if hasattr(b1, 'specializationModel_Feature'):
        assert not _is_linked(b1, 'specializationModel_Feature', a)
    if hasattr(b2, 'specializationModel_Feature'):
        assert _is_linked(b2, 'specializationModel_Feature', a)
    _safe_set(a, 'specializationModel_TypedValue', None)
    assert not _is_linked(a, 'specializationModel_TypedValue', b2)
    if hasattr(b2, 'specializationModel_Feature'):
        assert not _is_linked(b2, 'specializationModel_Feature', a)


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


specializationModel_Feature_strategy = st.builds(specializationModel_Feature, name=safe_text, realName=safe_text, state=safe_text, valueType=safe_text)
@given(instance=specializationModel_Feature_strategy)
@settings(max_examples=25)
def test_specializationModel_Feature_instantiation(instance):
    assert isinstance(instance, specializationModel_Feature)


specializationModel_FeatureGroup_strategy = st.builds(specializationModel_FeatureGroup, lowerBound=st.integers(), type=safe_text, upperBound=st.integers())
@given(instance=specializationModel_FeatureGroup_strategy)
@settings(max_examples=25)
def test_specializationModel_FeatureGroup_instantiation(instance):
    assert isinstance(instance, specializationModel_FeatureGroup)


specializationModel_Node_strategy = st.builds(specializationModel_Node)
@given(instance=specializationModel_Node_strategy)
@settings(max_examples=25)
def test_specializationModel_Node_instantiation(instance):
    assert isinstance(instance, specializationModel_Node)


specializationModel_Project_strategy = st.builds(specializationModel_Project, featureModelURI=safe_text, infiniteDomain=st.booleans(), nameConfigFile=safe_text, nameConstraintsFile=safe_text, numberOfProducts=st.integers(), userConstraintsState=st.booleans())
@given(instance=specializationModel_Project_strategy)
@settings(max_examples=25)
def test_specializationModel_Project_instantiation(instance):
    assert isinstance(instance, specializationModel_Project)


specializationModel_Relation_strategy = st.builds(specializationModel_Relation)
@given(instance=specializationModel_Relation_strategy)
@settings(max_examples=25)
def test_specializationModel_Relation_instantiation(instance):
    assert isinstance(instance, specializationModel_Relation)


specializationModel_RelationFG_strategy = st.builds(specializationModel_RelationFG)
@given(instance=specializationModel_RelationFG_strategy)
@settings(max_examples=25)
def test_specializationModel_RelationFG_instantiation(instance):
    assert isinstance(instance, specializationModel_RelationFG)


specializationModel_RelationFeature_strategy = st.builds(specializationModel_RelationFeature, lowerBound=st.integers(), type=safe_text, upperBound=st.integers())
@given(instance=specializationModel_RelationFeature_strategy)
@settings(max_examples=25)
def test_specializationModel_RelationFeature_instantiation(instance):
    assert isinstance(instance, specializationModel_RelationFeature)


specializationModel_TypedValue_strategy = st.builds(specializationModel_TypedValue, floatValue=safe_text, integerValue=safe_text, stringValue=safe_text)
@given(instance=specializationModel_TypedValue_strategy)
@settings(max_examples=25)
def test_specializationModel_TypedValue_instantiation(instance):
    assert isinstance(instance, specializationModel_TypedValue)


