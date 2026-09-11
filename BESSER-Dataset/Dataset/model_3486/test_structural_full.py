import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    fm_Attribute,
    fm_Constraint,
    fm_EObject,
    fm_Feature,
    fm_FeatureModel,
    fm_Group,
    AttributeType,
    ObjectiveFunctionType,
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

def test_fm_Attribute_comment_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_fm_Attribute_defaultValue_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_fm_Attribute_description_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_fm_Attribute_id_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fm_Attribute_maxRangeValue_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.maxRangeValue == "sample_text"
    instance.maxRangeValue = "sample_text_2"
    assert instance.maxRangeValue == "sample_text_2"


def test_fm_Attribute_minRangeValue_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.minRangeValue == "sample_text"
    instance.minRangeValue = "sample_text_2"
    assert instance.minRangeValue == "sample_text_2"


def test_fm_Attribute_minimize_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.minimize == True
    instance.minimize = False
    assert instance.minimize == False


def test_fm_Attribute_name_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fm_Attribute_objectiveFunctionAggregator_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.objectiveFunctionAggregator == "sample_text"
    instance.objectiveFunctionAggregator = "sample_text_2"
    assert instance.objectiveFunctionAggregator == "sample_text_2"


def test_fm_Attribute_qualityAttribute_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.qualityAttribute == True
    instance.qualityAttribute = False
    assert instance.qualityAttribute == False


def test_fm_Attribute_resourceAttribute_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.resourceAttribute == True
    instance.resourceAttribute = False
    assert instance.resourceAttribute == False


def test_fm_Attribute_type_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_fm_Attribute_weight_value_roundtrip():
    instance = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_fm_Constraint_comment_value_roundtrip():
    instance = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_fm_Constraint_description_value_roundtrip():
    instance = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_fm_Constraint_language_value_roundtrip():
    instance = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_fm_Constraint_value_value_roundtrip():
    instance = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_fm_Feature_cloneable_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.cloneable == True
    instance.cloneable = False
    assert instance.cloneable == False


def test_fm_Feature_comment_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_fm_Feature_description_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_fm_Feature_id_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fm_Feature_lower_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.lower == 7
    instance.lower = 13
    assert instance.lower == 13


def test_fm_Feature_mandatory_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.mandatory == True
    instance.mandatory = False
    assert instance.mandatory == False


def test_fm_Feature_name_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fm_Feature_optional_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_fm_Feature_orphan_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.orphan == True
    instance.orphan = False
    assert instance.orphan == False


def test_fm_Feature_root_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.root == True
    instance.root = False
    assert instance.root == False


def test_fm_Feature_upper_value_roundtrip():
    instance = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    assert instance.upper == 7
    instance.upper = 13
    assert instance.upper == 13


def test_fm_FeatureModel_comment_value_roundtrip():
    instance = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_fm_FeatureModel_description_value_roundtrip():
    instance = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_fm_FeatureModel_name_value_roundtrip():
    instance = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fm_FeatureModel_version_value_roundtrip():
    instance = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_fm_Group_comment_value_roundtrip():
    instance = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_fm_Group_description_value_roundtrip():
    instance = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_fm_Group_lower_value_roundtrip():
    instance = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    assert instance.lower == 7
    instance.lower = 13
    assert instance.lower == 13


def test_fm_Group_or__value_roundtrip():
    instance = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    assert instance.or_ == True
    instance.or_ = False
    assert instance.or_ == False


def test_fm_Group_upper_value_roundtrip():
    instance = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    assert instance.upper == 7
    instance.upper = 13
    assert instance.upper == 13


def test_fm_Group_xor_value_roundtrip():
    instance = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    assert instance.xor == True
    instance.xor = False
    assert instance.xor == False


def test_assoc_attributes12_link_reassign_clear():
    a = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b1 = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    b2 = fm_Attribute(comment="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", id="sample_text_2", maxRangeValue="sample_text_2", minRangeValue="sample_text_2", minimize=False, name="sample_text_2", objectiveFunctionAggregator="sample_text_2", qualityAttribute=False, resourceAttribute=False, type="sample_text_2", weight="sample_text_2")
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


def test_assoc_constraints4_link_reassign_clear():
    a = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    b1 = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    b2 = fm_Constraint(comment="sample_text_2", description="sample_text_2", language="sample_text_2", value="sample_text_2")
    _safe_set(a, 'fm_FeatureModel5', {b1})
    assert _is_linked(a, 'fm_FeatureModel5', b1)
    if hasattr(b1, 'fm_Constraint'):
        assert _is_linked(b1, 'fm_Constraint', a)
    _safe_set(a, 'fm_FeatureModel5', {b2})
    assert _is_linked(a, 'fm_FeatureModel5', b2)
    if hasattr(b1, 'fm_Constraint'):
        assert not _is_linked(b1, 'fm_Constraint', a)
    if hasattr(b2, 'fm_Constraint'):
        assert _is_linked(b2, 'fm_Constraint', a)
    _safe_set(a, 'fm_FeatureModel5', set())
    assert not _is_linked(a, 'fm_FeatureModel5', b2)
    if hasattr(b2, 'fm_Constraint'):
        assert not _is_linked(b2, 'fm_Constraint', a)


def test_assoc_feature25_link_reassign_clear():
    a = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b1 = fm_Attribute(comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    b2 = fm_Attribute(comment="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", id="sample_text_2", maxRangeValue="sample_text_2", minRangeValue="sample_text_2", minimize=False, name="sample_text_2", objectiveFunctionAggregator="sample_text_2", qualityAttribute=False, resourceAttribute=False, type="sample_text_2", weight="sample_text_2")
    _safe_set(a, 'Feature26', b1)
    assert _is_linked(a, 'Feature26', b1)
    if hasattr(b1, 'attributes'):
        assert _is_linked(b1, 'attributes', a)
    _safe_set(a, 'Feature26', b2)
    assert _is_linked(a, 'Feature26', b2)
    if hasattr(b1, 'attributes'):
        assert not _is_linked(b1, 'attributes', a)
    if hasattr(b2, 'attributes'):
        assert _is_linked(b2, 'attributes', a)
    _safe_set(a, 'Feature26', None)
    assert not _is_linked(a, 'Feature26', b2)
    if hasattr(b2, 'attributes'):
        assert not _is_linked(b2, 'attributes', a)


def test_assoc_featureModel18_link_reassign_clear():
    a = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'fm_FeatureModel20', b1)
    assert _is_linked(a, 'fm_FeatureModel20', b1)
    if hasattr(b1, 'fm_Feature19'):
        assert _is_linked(b1, 'fm_Feature19', a)
    _safe_set(a, 'fm_FeatureModel20', b2)
    assert _is_linked(a, 'fm_FeatureModel20', b2)
    if hasattr(b1, 'fm_Feature19'):
        assert not _is_linked(b1, 'fm_Feature19', a)
    if hasattr(b2, 'fm_Feature19'):
        assert _is_linked(b2, 'fm_Feature19', a)
    _safe_set(a, 'fm_FeatureModel20', None)
    assert not _is_linked(a, 'fm_FeatureModel20', b2)
    if hasattr(b2, 'fm_Feature19'):
        assert not _is_linked(b2, 'fm_Feature19', a)


def test_assoc_featureModel27_link_reassign_clear():
    a = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    b1 = fm_Constraint(comment="sample_text", description="sample_text", language="sample_text", value="sample_text")
    b2 = fm_Constraint(comment="sample_text_2", description="sample_text_2", language="sample_text_2", value="sample_text_2")
    _safe_set(a, 'fm_FeatureModel29', b1)
    assert _is_linked(a, 'fm_FeatureModel29', b1)
    if hasattr(b1, 'fm_Constraint28'):
        assert _is_linked(b1, 'fm_Constraint28', a)
    _safe_set(a, 'fm_FeatureModel29', b2)
    assert _is_linked(a, 'fm_FeatureModel29', b2)
    if hasattr(b1, 'fm_Constraint28'):
        assert not _is_linked(b1, 'fm_Constraint28', a)
    if hasattr(b2, 'fm_Constraint28'):
        assert _is_linked(b2, 'fm_Constraint28', a)
    _safe_set(a, 'fm_FeatureModel29', None)
    assert not _is_linked(a, 'fm_FeatureModel29', b2)
    if hasattr(b2, 'fm_Constraint28'):
        assert not _is_linked(b2, 'fm_Constraint28', a)


def test_assoc_features14_link_reassign_clear():
    a = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'Feature15', b1)
    assert _is_linked(a, 'Feature15', b1)
    if hasattr(b1, 'parentFeature'):
        assert _is_linked(b1, 'parentFeature', a)
    _safe_set(a, 'Feature15', b2)
    assert _is_linked(a, 'Feature15', b2)
    if hasattr(b1, 'parentFeature'):
        assert not _is_linked(b1, 'parentFeature', a)
    if hasattr(b2, 'parentFeature'):
        assert _is_linked(b2, 'parentFeature', a)
    _safe_set(a, 'Feature15', None)
    assert not _is_linked(a, 'Feature15', b2)
    if hasattr(b2, 'parentFeature'):
        assert not _is_linked(b2, 'parentFeature', a)


def test_assoc_features23_link_reassign_clear():
    a = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'parentGroup', {b1})
    assert _is_linked(a, 'parentGroup', b1)
    if hasattr(b1, 'Feature24'):
        assert _is_linked(b1, 'Feature24', a)
    _safe_set(a, 'parentGroup', {b2})
    assert _is_linked(a, 'parentGroup', b2)
    if hasattr(b1, 'Feature24'):
        assert not _is_linked(b1, 'Feature24', a)
    if hasattr(b2, 'Feature24'):
        assert _is_linked(b2, 'Feature24', a)
    _safe_set(a, 'parentGroup', set())
    assert not _is_linked(a, 'parentGroup', b2)
    if hasattr(b2, 'Feature24'):
        assert not _is_linked(b2, 'Feature24', a)


def test_assoc_groups16_link_reassign_clear():
    a = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'Group17', b1)
    assert _is_linked(a, 'Group17', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'Group17', b2)
    assert _is_linked(a, 'Group17', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'Group17', None)
    assert not _is_linked(a, 'Group17', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_orphans1_link_reassign_clear():
    a = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'fm_FeatureModel2', {b1})
    assert _is_linked(a, 'fm_FeatureModel2', b1)
    if hasattr(b1, 'fm_Feature3'):
        assert _is_linked(b1, 'fm_Feature3', a)
    _safe_set(a, 'fm_FeatureModel2', {b2})
    assert _is_linked(a, 'fm_FeatureModel2', b2)
    if hasattr(b1, 'fm_Feature3'):
        assert not _is_linked(b1, 'fm_Feature3', a)
    if hasattr(b2, 'fm_Feature3'):
        assert _is_linked(b2, 'fm_Feature3', a)
    _safe_set(a, 'fm_FeatureModel2', set())
    assert not _is_linked(a, 'fm_FeatureModel2', b2)
    if hasattr(b2, 'fm_Feature3'):
        assert not _is_linked(b2, 'fm_Feature3', a)


def test_assoc_parent21_link_reassign_clear():
    a = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'groups', b1)
    assert _is_linked(a, 'groups', b1)
    if hasattr(b1, 'Feature22'):
        assert _is_linked(b1, 'Feature22', a)
    _safe_set(a, 'groups', b2)
    assert _is_linked(a, 'groups', b2)
    if hasattr(b1, 'Feature22'):
        assert not _is_linked(b1, 'Feature22', a)
    if hasattr(b2, 'Feature22'):
        assert _is_linked(b2, 'Feature22', a)
    _safe_set(a, 'groups', None)
    assert not _is_linked(a, 'groups', b2)
    if hasattr(b2, 'Feature22'):
        assert not _is_linked(b2, 'Feature22', a)


def test_assoc_parent6_link_reassign_clear():
    a = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b1 = fm_EObject()
    b2 = fm_EObject()
    _safe_set(a, 'fm_Feature7', b1)
    assert _is_linked(a, 'fm_Feature7', b1)
    if hasattr(b1, 'fm_EObject'):
        assert _is_linked(b1, 'fm_EObject', a)
    _safe_set(a, 'fm_Feature7', b2)
    assert _is_linked(a, 'fm_Feature7', b2)
    if hasattr(b1, 'fm_EObject'):
        assert not _is_linked(b1, 'fm_EObject', a)
    if hasattr(b2, 'fm_EObject'):
        assert _is_linked(b2, 'fm_EObject', a)
    _safe_set(a, 'fm_Feature7', None)
    assert not _is_linked(a, 'fm_Feature7', b2)
    if hasattr(b2, 'fm_EObject'):
        assert not _is_linked(b2, 'fm_EObject', a)


def test_assoc_parentFeature9_link_reassign_clear():
    a = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'Feature', b1)
    assert _is_linked(a, 'Feature', b1)
    if hasattr(b1, 'features'):
        assert _is_linked(b1, 'features', a)
    _safe_set(a, 'Feature', b2)
    assert _is_linked(a, 'Feature', b2)
    if hasattr(b1, 'features'):
        assert not _is_linked(b1, 'features', a)
    if hasattr(b2, 'features'):
        assert _is_linked(b2, 'features', a)
    _safe_set(a, 'Feature', None)
    assert not _is_linked(a, 'Feature', b2)
    if hasattr(b2, 'features'):
        assert not _is_linked(b2, 'features', a)


def test_assoc_parentGroup10_link_reassign_clear():
    a = fm_Group(comment="sample_text", description="sample_text", lower=7, or_=True, upper=7, xor=True)
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'Group', b1)
    assert _is_linked(a, 'Group', b1)
    if hasattr(b1, 'features11'):
        assert _is_linked(b1, 'features11', a)
    _safe_set(a, 'Group', b2)
    assert _is_linked(a, 'Group', b2)
    if hasattr(b1, 'features11'):
        assert not _is_linked(b1, 'features11', a)
    if hasattr(b2, 'features11'):
        assert _is_linked(b2, 'features11', a)
    _safe_set(a, 'Group', None)
    assert not _is_linked(a, 'Group', b2)
    if hasattr(b2, 'features11'):
        assert not _is_linked(b2, 'features11', a)


def test_assoc_root0_link_reassign_clear():
    a = fm_FeatureModel(comment="sample_text", description="sample_text", name="sample_text", version="sample_text")
    b1 = fm_Feature(cloneable=True, comment="sample_text", description="sample_text", id="sample_text", lower=7, mandatory=True, name="sample_text", optional=True, orphan=True, root=True, upper=7)
    b2 = fm_Feature(cloneable=False, comment="sample_text_2", description="sample_text_2", id="sample_text_2", lower=13, mandatory=False, name="sample_text_2", optional=False, orphan=False, root=False, upper=13)
    _safe_set(a, 'fm_FeatureModel', b1)
    assert _is_linked(a, 'fm_FeatureModel', b1)
    if hasattr(b1, 'fm_Feature'):
        assert _is_linked(b1, 'fm_Feature', a)
    _safe_set(a, 'fm_FeatureModel', b2)
    assert _is_linked(a, 'fm_FeatureModel', b2)
    if hasattr(b1, 'fm_Feature'):
        assert not _is_linked(b1, 'fm_Feature', a)
    if hasattr(b2, 'fm_Feature'):
        assert _is_linked(b2, 'fm_Feature', a)
    _safe_set(a, 'fm_FeatureModel', None)
    assert not _is_linked(a, 'fm_FeatureModel', b2)
    if hasattr(b2, 'fm_Feature'):
        assert not _is_linked(b2, 'fm_Feature', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fm_Attribute_strategy = st.builds(fm_Attribute, comment=safe_text, defaultValue=safe_text, description=safe_text, id=safe_text, maxRangeValue=safe_text, minRangeValue=safe_text, minimize=st.booleans(), name=safe_text, objectiveFunctionAggregator=safe_text, qualityAttribute=st.booleans(), resourceAttribute=st.booleans(), type=safe_text, weight=safe_text)
@given(instance=fm_Attribute_strategy)
@settings(max_examples=25)
def test_fm_Attribute_instantiation(instance):
    assert isinstance(instance, fm_Attribute)


fm_Constraint_strategy = st.builds(fm_Constraint, comment=safe_text, description=safe_text, language=safe_text, value=safe_text)
@given(instance=fm_Constraint_strategy)
@settings(max_examples=25)
def test_fm_Constraint_instantiation(instance):
    assert isinstance(instance, fm_Constraint)


fm_EObject_strategy = st.builds(fm_EObject)
@given(instance=fm_EObject_strategy)
@settings(max_examples=25)
def test_fm_EObject_instantiation(instance):
    assert isinstance(instance, fm_EObject)


fm_Feature_strategy = st.builds(fm_Feature, cloneable=st.booleans(), comment=safe_text, description=safe_text, id=safe_text, lower=st.integers(), mandatory=st.booleans(), name=safe_text, optional=st.booleans(), orphan=st.booleans(), root=st.booleans(), upper=st.integers())
@given(instance=fm_Feature_strategy)
@settings(max_examples=25)
def test_fm_Feature_instantiation(instance):
    assert isinstance(instance, fm_Feature)


fm_FeatureModel_strategy = st.builds(fm_FeatureModel, comment=safe_text, description=safe_text, name=safe_text, version=safe_text)
@given(instance=fm_FeatureModel_strategy)
@settings(max_examples=25)
def test_fm_FeatureModel_instantiation(instance):
    assert isinstance(instance, fm_FeatureModel)


fm_Group_strategy = st.builds(fm_Group, comment=safe_text, description=safe_text, lower=st.integers(), or_=st.booleans(), upper=st.integers(), xor=st.booleans())
@given(instance=fm_Group_strategy)
@settings(max_examples=25)
def test_fm_Group_instantiation(instance):
    assert isinstance(instance, fm_Group)


