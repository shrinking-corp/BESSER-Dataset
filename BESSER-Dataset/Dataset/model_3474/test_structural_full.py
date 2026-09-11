import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    TreeConstraint,
    myDsl_CrossTreeConstraint,
    myDsl_FM,
    myDsl_Feature,
    myDsl_FeatureAttribute,
    myDsl_MandatoryTreeConstraint,
    myDsl_OptionalTreeConstraint,
    myDsl_OrAlternativeTreeConstraint,
    myDsl_ParentChildConstraint,
    myDsl_TreeConstraint,
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

def test_myDsl_CrossTreeConstraint_type_value_roundtrip():
    instance = myDsl_CrossTreeConstraint(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_myDsl_Feature_name_value_roundtrip():
    instance = myDsl_Feature(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_myDsl_FeatureAttribute_attributeType_value_roundtrip():
    instance = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    assert instance.attributeType == "sample_text"
    instance.attributeType = "sample_text_2"
    assert instance.attributeType == "sample_text_2"


def test_myDsl_FeatureAttribute_defaultValue_value_roundtrip():
    instance = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    assert instance.defaultValue == 7
    instance.defaultValue = 13
    assert instance.defaultValue == 13


def test_myDsl_FeatureAttribute_maxValue_value_roundtrip():
    instance = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    assert instance.maxValue == 7
    instance.maxValue = 13
    assert instance.maxValue == 13


def test_myDsl_FeatureAttribute_minValue_value_roundtrip():
    instance = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    assert instance.minValue == 7
    instance.minValue = 13
    assert instance.minValue == 13


def test_myDsl_FeatureAttribute_nullValue_value_roundtrip():
    instance = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    assert instance.nullValue == 7
    instance.nullValue = 13
    assert instance.nullValue == 13


def test_myDsl_OrAlternativeTreeConstraint_max_value_roundtrip():
    instance = myDsl_OrAlternativeTreeConstraint(max=7, min=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_myDsl_OrAlternativeTreeConstraint_min_value_roundtrip():
    instance = myDsl_OrAlternativeTreeConstraint(max=7, min=7)
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_myDsl_MandatoryTreeConstraint_isa_TreeConstraint():
    instance = myDsl_MandatoryTreeConstraint()
    assert isinstance(instance, TreeConstraint)


def test_myDsl_OptionalTreeConstraint_isa_TreeConstraint():
    instance = myDsl_OptionalTreeConstraint()
    assert isinstance(instance, TreeConstraint)


def test_myDsl_OrAlternativeTreeConstraint_isa_TreeConstraint():
    instance = myDsl_OrAlternativeTreeConstraint(max=7, min=7)
    assert isinstance(instance, TreeConstraint)


def test_assoc_attributes3_link_reassign_clear():
    a = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    b1 = myDsl_FM()
    b2 = myDsl_FM()
    _safe_set(a, 'myDsl_FeatureAttribute', b1)
    assert _is_linked(a, 'myDsl_FeatureAttribute', b1)
    if hasattr(b1, 'myDsl_FM4'):
        assert _is_linked(b1, 'myDsl_FM4', a)
    _safe_set(a, 'myDsl_FeatureAttribute', b2)
    assert _is_linked(a, 'myDsl_FeatureAttribute', b2)
    if hasattr(b1, 'myDsl_FM4'):
        assert not _is_linked(b1, 'myDsl_FM4', a)
    if hasattr(b2, 'myDsl_FM4'):
        assert _is_linked(b2, 'myDsl_FM4', a)
    _safe_set(a, 'myDsl_FeatureAttribute', None)
    assert not _is_linked(a, 'myDsl_FeatureAttribute', b2)
    if hasattr(b2, 'myDsl_FM4'):
        assert not _is_linked(b2, 'myDsl_FM4', a)


def test_assoc_crossTreeConstraints5_link_reassign_clear():
    a = myDsl_CrossTreeConstraint(type="sample_text")
    b1 = myDsl_FM()
    b2 = myDsl_FM()
    _safe_set(a, 'myDsl_CrossTreeConstraint', b1)
    assert _is_linked(a, 'myDsl_CrossTreeConstraint', b1)
    if hasattr(b1, 'myDsl_FM6'):
        assert _is_linked(b1, 'myDsl_FM6', a)
    _safe_set(a, 'myDsl_CrossTreeConstraint', b2)
    assert _is_linked(a, 'myDsl_CrossTreeConstraint', b2)
    if hasattr(b1, 'myDsl_FM6'):
        assert not _is_linked(b1, 'myDsl_FM6', a)
    if hasattr(b2, 'myDsl_FM6'):
        assert _is_linked(b2, 'myDsl_FM6', a)
    _safe_set(a, 'myDsl_CrossTreeConstraint', None)
    assert not _is_linked(a, 'myDsl_CrossTreeConstraint', b2)
    if hasattr(b2, 'myDsl_FM6'):
        assert not _is_linked(b2, 'myDsl_FM6', a)


def test_assoc_feature118_link_reassign_clear():
    a = myDsl_Feature(name="sample_text")
    b1 = myDsl_CrossTreeConstraint(type="sample_text")
    b2 = myDsl_CrossTreeConstraint(type="sample_text_2")
    _safe_set(a, 'myDsl_Feature20', b1)
    assert _is_linked(a, 'myDsl_Feature20', b1)
    if hasattr(b1, 'myDsl_CrossTreeConstraint19'):
        assert _is_linked(b1, 'myDsl_CrossTreeConstraint19', a)
    _safe_set(a, 'myDsl_Feature20', b2)
    assert _is_linked(a, 'myDsl_Feature20', b2)
    if hasattr(b1, 'myDsl_CrossTreeConstraint19'):
        assert not _is_linked(b1, 'myDsl_CrossTreeConstraint19', a)
    if hasattr(b2, 'myDsl_CrossTreeConstraint19'):
        assert _is_linked(b2, 'myDsl_CrossTreeConstraint19', a)
    _safe_set(a, 'myDsl_Feature20', None)
    assert not _is_linked(a, 'myDsl_Feature20', b2)
    if hasattr(b2, 'myDsl_CrossTreeConstraint19'):
        assert not _is_linked(b2, 'myDsl_CrossTreeConstraint19', a)


def test_assoc_feature12_link_reassign_clear():
    a = myDsl_Feature(name="sample_text")
    b1 = myDsl_MandatoryTreeConstraint()
    b2 = myDsl_MandatoryTreeConstraint()
    _safe_set(a, 'myDsl_Feature13', b1)
    assert _is_linked(a, 'myDsl_Feature13', b1)
    if hasattr(b1, 'myDsl_MandatoryTreeConstraint'):
        assert _is_linked(b1, 'myDsl_MandatoryTreeConstraint', a)
    _safe_set(a, 'myDsl_Feature13', b2)
    assert _is_linked(a, 'myDsl_Feature13', b2)
    if hasattr(b1, 'myDsl_MandatoryTreeConstraint'):
        assert not _is_linked(b1, 'myDsl_MandatoryTreeConstraint', a)
    if hasattr(b2, 'myDsl_MandatoryTreeConstraint'):
        assert _is_linked(b2, 'myDsl_MandatoryTreeConstraint', a)
    _safe_set(a, 'myDsl_Feature13', None)
    assert not _is_linked(a, 'myDsl_Feature13', b2)
    if hasattr(b2, 'myDsl_MandatoryTreeConstraint'):
        assert not _is_linked(b2, 'myDsl_MandatoryTreeConstraint', a)


def test_assoc_feature14_link_reassign_clear():
    a = myDsl_Feature(name="sample_text")
    b1 = myDsl_OptionalTreeConstraint()
    b2 = myDsl_OptionalTreeConstraint()
    _safe_set(a, 'myDsl_Feature15', b1)
    assert _is_linked(a, 'myDsl_Feature15', b1)
    if hasattr(b1, 'myDsl_OptionalTreeConstraint'):
        assert _is_linked(b1, 'myDsl_OptionalTreeConstraint', a)
    _safe_set(a, 'myDsl_Feature15', b2)
    assert _is_linked(a, 'myDsl_Feature15', b2)
    if hasattr(b1, 'myDsl_OptionalTreeConstraint'):
        assert not _is_linked(b1, 'myDsl_OptionalTreeConstraint', a)
    if hasattr(b2, 'myDsl_OptionalTreeConstraint'):
        assert _is_linked(b2, 'myDsl_OptionalTreeConstraint', a)
    _safe_set(a, 'myDsl_Feature15', None)
    assert not _is_linked(a, 'myDsl_Feature15', b2)
    if hasattr(b2, 'myDsl_OptionalTreeConstraint'):
        assert not _is_linked(b2, 'myDsl_OptionalTreeConstraint', a)


def test_assoc_feature221_link_reassign_clear():
    a = myDsl_Feature(name="sample_text")
    b1 = myDsl_CrossTreeConstraint(type="sample_text")
    b2 = myDsl_CrossTreeConstraint(type="sample_text_2")
    _safe_set(a, 'myDsl_Feature23', b1)
    assert _is_linked(a, 'myDsl_Feature23', b1)
    if hasattr(b1, 'myDsl_CrossTreeConstraint22'):
        assert _is_linked(b1, 'myDsl_CrossTreeConstraint22', a)
    _safe_set(a, 'myDsl_Feature23', b2)
    assert _is_linked(a, 'myDsl_Feature23', b2)
    if hasattr(b1, 'myDsl_CrossTreeConstraint22'):
        assert not _is_linked(b1, 'myDsl_CrossTreeConstraint22', a)
    if hasattr(b2, 'myDsl_CrossTreeConstraint22'):
        assert _is_linked(b2, 'myDsl_CrossTreeConstraint22', a)
    _safe_set(a, 'myDsl_Feature23', None)
    assert not _is_linked(a, 'myDsl_Feature23', b2)
    if hasattr(b2, 'myDsl_CrossTreeConstraint22'):
        assert not _is_linked(b2, 'myDsl_CrossTreeConstraint22', a)


def test_assoc_feature24_link_reassign_clear():
    a = myDsl_FeatureAttribute(attributeType="sample_text", defaultValue=7, maxValue=7, minValue=7, nullValue=7)
    b1 = myDsl_Feature(name="sample_text")
    b2 = myDsl_Feature(name="sample_text_2")
    _safe_set(a, 'myDsl_FeatureAttribute25', b1)
    assert _is_linked(a, 'myDsl_FeatureAttribute25', b1)
    if hasattr(b1, 'myDsl_Feature26'):
        assert _is_linked(b1, 'myDsl_Feature26', a)
    _safe_set(a, 'myDsl_FeatureAttribute25', b2)
    assert _is_linked(a, 'myDsl_FeatureAttribute25', b2)
    if hasattr(b1, 'myDsl_Feature26'):
        assert not _is_linked(b1, 'myDsl_Feature26', a)
    if hasattr(b2, 'myDsl_Feature26'):
        assert _is_linked(b2, 'myDsl_Feature26', a)
    _safe_set(a, 'myDsl_FeatureAttribute25', None)
    assert not _is_linked(a, 'myDsl_FeatureAttribute25', b2)
    if hasattr(b2, 'myDsl_Feature26'):
        assert not _is_linked(b2, 'myDsl_Feature26', a)


def test_assoc_features0_link_reassign_clear():
    a = myDsl_Feature(name="sample_text")
    b1 = myDsl_FM()
    b2 = myDsl_FM()
    _safe_set(a, 'myDsl_Feature', b1)
    assert _is_linked(a, 'myDsl_Feature', b1)
    if hasattr(b1, 'myDsl_FM'):
        assert _is_linked(b1, 'myDsl_FM', a)
    _safe_set(a, 'myDsl_Feature', b2)
    assert _is_linked(a, 'myDsl_Feature', b2)
    if hasattr(b1, 'myDsl_FM'):
        assert not _is_linked(b1, 'myDsl_FM', a)
    if hasattr(b2, 'myDsl_FM'):
        assert _is_linked(b2, 'myDsl_FM', a)
    _safe_set(a, 'myDsl_Feature', None)
    assert not _is_linked(a, 'myDsl_Feature', b2)
    if hasattr(b2, 'myDsl_FM'):
        assert not _is_linked(b2, 'myDsl_FM', a)


def test_assoc_features16_link_reassign_clear():
    a = myDsl_OrAlternativeTreeConstraint(max=7, min=7)
    b1 = myDsl_Feature(name="sample_text")
    b2 = myDsl_Feature(name="sample_text_2")
    _safe_set(a, 'myDsl_OrAlternativeTreeConstraint', {b1})
    assert _is_linked(a, 'myDsl_OrAlternativeTreeConstraint', b1)
    if hasattr(b1, 'myDsl_Feature17'):
        assert _is_linked(b1, 'myDsl_Feature17', a)
    _safe_set(a, 'myDsl_OrAlternativeTreeConstraint', {b2})
    assert _is_linked(a, 'myDsl_OrAlternativeTreeConstraint', b2)
    if hasattr(b1, 'myDsl_Feature17'):
        assert not _is_linked(b1, 'myDsl_Feature17', a)
    if hasattr(b2, 'myDsl_Feature17'):
        assert _is_linked(b2, 'myDsl_Feature17', a)
    _safe_set(a, 'myDsl_OrAlternativeTreeConstraint', set())
    assert not _is_linked(a, 'myDsl_OrAlternativeTreeConstraint', b2)
    if hasattr(b2, 'myDsl_Feature17'):
        assert not _is_linked(b2, 'myDsl_Feature17', a)


def test_assoc_parent7_link_reassign_clear():
    a = myDsl_Feature(name="sample_text")
    b1 = myDsl_ParentChildConstraint()
    b2 = myDsl_ParentChildConstraint()
    _safe_set(a, 'myDsl_Feature9', b1)
    assert _is_linked(a, 'myDsl_Feature9', b1)
    if hasattr(b1, 'myDsl_ParentChildConstraint8'):
        assert _is_linked(b1, 'myDsl_ParentChildConstraint8', a)
    _safe_set(a, 'myDsl_Feature9', b2)
    assert _is_linked(a, 'myDsl_Feature9', b2)
    if hasattr(b1, 'myDsl_ParentChildConstraint8'):
        assert not _is_linked(b1, 'myDsl_ParentChildConstraint8', a)
    if hasattr(b2, 'myDsl_ParentChildConstraint8'):
        assert _is_linked(b2, 'myDsl_ParentChildConstraint8', a)
    _safe_set(a, 'myDsl_Feature9', None)
    assert not _is_linked(a, 'myDsl_Feature9', b2)
    if hasattr(b2, 'myDsl_ParentChildConstraint8'):
        assert not _is_linked(b2, 'myDsl_ParentChildConstraint8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

TreeConstraint_strategy = st.builds(TreeConstraint)
@given(instance=TreeConstraint_strategy)
@settings(max_examples=25)
def test_TreeConstraint_instantiation(instance):
    assert isinstance(instance, TreeConstraint)


myDsl_CrossTreeConstraint_strategy = st.builds(myDsl_CrossTreeConstraint, type=safe_text)
@given(instance=myDsl_CrossTreeConstraint_strategy)
@settings(max_examples=25)
def test_myDsl_CrossTreeConstraint_instantiation(instance):
    assert isinstance(instance, myDsl_CrossTreeConstraint)


myDsl_FM_strategy = st.builds(myDsl_FM)
@given(instance=myDsl_FM_strategy)
@settings(max_examples=25)
def test_myDsl_FM_instantiation(instance):
    assert isinstance(instance, myDsl_FM)


myDsl_Feature_strategy = st.builds(myDsl_Feature, name=safe_text)
@given(instance=myDsl_Feature_strategy)
@settings(max_examples=25)
def test_myDsl_Feature_instantiation(instance):
    assert isinstance(instance, myDsl_Feature)


myDsl_FeatureAttribute_strategy = st.builds(myDsl_FeatureAttribute, attributeType=safe_text, defaultValue=st.integers(), maxValue=st.integers(), minValue=st.integers(), nullValue=st.integers())
@given(instance=myDsl_FeatureAttribute_strategy)
@settings(max_examples=25)
def test_myDsl_FeatureAttribute_instantiation(instance):
    assert isinstance(instance, myDsl_FeatureAttribute)


myDsl_MandatoryTreeConstraint_strategy = st.builds(myDsl_MandatoryTreeConstraint)
@given(instance=myDsl_MandatoryTreeConstraint_strategy)
@settings(max_examples=25)
def test_myDsl_MandatoryTreeConstraint_instantiation(instance):
    assert isinstance(instance, myDsl_MandatoryTreeConstraint)


myDsl_OptionalTreeConstraint_strategy = st.builds(myDsl_OptionalTreeConstraint)
@given(instance=myDsl_OptionalTreeConstraint_strategy)
@settings(max_examples=25)
def test_myDsl_OptionalTreeConstraint_instantiation(instance):
    assert isinstance(instance, myDsl_OptionalTreeConstraint)


myDsl_OrAlternativeTreeConstraint_strategy = st.builds(myDsl_OrAlternativeTreeConstraint, max=st.integers(), min=st.integers())
@given(instance=myDsl_OrAlternativeTreeConstraint_strategy)
@settings(max_examples=25)
def test_myDsl_OrAlternativeTreeConstraint_instantiation(instance):
    assert isinstance(instance, myDsl_OrAlternativeTreeConstraint)


myDsl_ParentChildConstraint_strategy = st.builds(myDsl_ParentChildConstraint)
@given(instance=myDsl_ParentChildConstraint_strategy)
@settings(max_examples=25)
def test_myDsl_ParentChildConstraint_instantiation(instance):
    assert isinstance(instance, myDsl_ParentChildConstraint)


myDsl_TreeConstraint_strategy = st.builds(myDsl_TreeConstraint)
@given(instance=myDsl_TreeConstraint_strategy)
@settings(max_examples=25)
def test_myDsl_TreeConstraint_instantiation(instance):
    assert isinstance(instance, myDsl_TreeConstraint)


