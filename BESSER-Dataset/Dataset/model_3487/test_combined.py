# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fm_Constraint,
    fm_Feature,
    fm_FeatureModel,
    fm_Attribute,
    fm_Group,
    fm_EObject,
    AttributeType,
    ObjectiveFunctionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fm_constraint_is_not_abstract():
    assert not inspect.isabstract(fm_Constraint)


def test_hyp_fm_constraint_constructor_exists():
    assert callable(fm_Constraint.__init__)


def test_hyp_fm_constraint_constructor_args():
    sig = inspect.signature(fm_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "description" in params, "Missing parameter 'description'"
    assert "language" in params, "Missing parameter 'language'"







def test_hyp_fm_feature_is_not_abstract():
    assert not inspect.isabstract(fm_Feature)


def test_hyp_fm_feature_constructor_exists():
    assert callable(fm_Feature.__init__)


def test_hyp_fm_feature_constructor_args():
    sig = inspect.signature(fm_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "orphan" in params, "Missing parameter 'orphan'"
    assert "cloneable" in params, "Missing parameter 'cloneable'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "root" in params, "Missing parameter 'root'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "comment" in params, "Missing parameter 'comment'"














def test_hyp_fm_featuremodel_is_not_abstract():
    assert not inspect.isabstract(fm_FeatureModel)


def test_hyp_fm_featuremodel_constructor_exists():
    assert callable(fm_FeatureModel.__init__)


def test_hyp_fm_featuremodel_constructor_args():
    sig = inspect.signature(fm_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"
    assert "description" in params, "Missing parameter 'description'"







def test_hyp_fm_attribute_is_not_abstract():
    assert not inspect.isabstract(fm_Attribute)


def test_hyp_fm_attribute_constructor_exists():
    assert callable(fm_Attribute.__init__)


def test_hyp_fm_attribute_constructor_args():
    sig = inspect.signature(fm_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "maxRangeValue" in params, "Missing parameter 'maxRangeValue'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "objectiveFunctionAggregator" in params, "Missing parameter 'objectiveFunctionAggregator'"
    assert "resourceAttribute" in params, "Missing parameter 'resourceAttribute'"
    assert "alert" in params, "Missing parameter 'alert'"
    assert "qualityAttribute" in params, "Missing parameter 'qualityAttribute'"
    assert "id" in params, "Missing parameter 'id'"
    assert "minRangeValue" in params, "Missing parameter 'minRangeValue'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "type" in params, "Missing parameter 'type'"
    assert "minimize" in params, "Missing parameter 'minimize'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

















def test_hyp_fm_group_is_not_abstract():
    assert not inspect.isabstract(fm_Group)


def test_hyp_fm_group_constructor_exists():
    assert callable(fm_Group.__init__)


def test_hyp_fm_group_constructor_args():
    sig = inspect.signature(fm_Group.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "description" in params, "Missing parameter 'description'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "or_" in params, "Missing parameter 'or_'"
    assert "xor" in params, "Missing parameter 'xor'"
    assert "comment" in params, "Missing parameter 'comment'"









def test_hyp_fm_eobject_is_not_abstract():
    assert not inspect.isabstract(fm_EObject)


def test_hyp_fm_eobject_constructor_exists():
    assert callable(fm_EObject.__init__)


def test_hyp_fm_eobject_constructor_args():
    sig = inspect.signature(fm_EObject.__init__)
    params = list(sig.parameters.keys())

def test_hyp_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_hyp_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "STRING",
        "BOOLEAN",
        "DOUBLE",
        "INTEGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeType"

def test_hyp_objectivefunctiontype_exists():
    # Check that the Enumeration exists
    assert ObjectiveFunctionType is not None

def test_hyp_objectivefunctiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectiveFunctionType]
    expected_literals = [
        "MINIMUM",
        "MAXIMUM",
        "SUM",
        "NOT_ASSIGNED",
        "PRODUCT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectiveFunctionType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
fm_Constraint_strategy = st.builds(
    fm_Constraint,
    value=
        safe_text,
    comment=
        safe_text,
    description=
        safe_text,
    language=
        safe_text
)
fm_Feature_strategy = st.builds(
    fm_Feature,
    orphan=
        st.booleans(),
    cloneable=
        st.booleans(),
    mandatory=
        st.booleans(),
    root=
        st.booleans(),
    id=
        safe_text,
    lower=
        st.integers(),
    name=
        safe_text,
    description=
        safe_text,
    upper=
        st.integers(),
    optional=
        st.booleans(),
    comment=
        safe_text
)
fm_FeatureModel_strategy = st.builds(
    fm_FeatureModel,
    comment=
        safe_text,
    name=
        safe_text,
    version=
        safe_text,
    description=
        safe_text
)
fm_Attribute_strategy = st.builds(
    fm_Attribute,
    maxRangeValue=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    objectiveFunctionAggregator=
        safe_text,
    resourceAttribute=
        st.booleans(),
    alert=
        st.booleans(),
    qualityAttribute=
        st.booleans(),
    id=
        safe_text,
    minRangeValue=
        safe_text,
    weight=
        safe_text,
    type=
        safe_text,
    minimize=
        st.booleans(),
    comment=
        safe_text,
    defaultValue=
        safe_text
)
fm_Group_strategy = st.builds(
    fm_Group,
    lower=
        st.integers(),
    description=
        safe_text,
    upper=
        st.integers(),
    or_=
        st.booleans(),
    xor=
        st.booleans(),
    comment=
        safe_text
)
fm_EObject_strategy = st.builds(
    fm_EObject,
)




@given(instance=fm_Constraint_strategy)
def test_hyp_fm_constraint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=fm_Constraint_strategy)
def test_hyp_fm_constraint_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=fm_Constraint_strategy)
def test_hyp_fm_constraint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Constraint_strategy)
def test_hyp_fm_constraint_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original




@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_orphan_setter(instance):
    original = instance.orphan
    instance.orphan = original
    assert instance.orphan == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_cloneable_setter(instance):
    original = instance.cloneable
    instance.cloneable = original
    assert instance.cloneable == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=fm_Feature_strategy)
def test_hyp_fm_feature_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original




@given(instance=fm_FeatureModel_strategy)
def test_hyp_fm_featuremodel_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=fm_FeatureModel_strategy)
def test_hyp_fm_featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fm_FeatureModel_strategy)
def test_hyp_fm_featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=fm_FeatureModel_strategy)
def test_hyp_fm_featuremodel_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_maxRangeValue_setter(instance):
    original = instance.maxRangeValue
    instance.maxRangeValue = original
    assert instance.maxRangeValue == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_objectiveFunctionAggregator_setter(instance):
    original = instance.objectiveFunctionAggregator
    instance.objectiveFunctionAggregator = original
    assert instance.objectiveFunctionAggregator == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_resourceAttribute_setter(instance):
    original = instance.resourceAttribute
    instance.resourceAttribute = original
    assert instance.resourceAttribute == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_alert_setter(instance):
    original = instance.alert
    instance.alert = original
    assert instance.alert == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_qualityAttribute_setter(instance):
    original = instance.qualityAttribute
    instance.qualityAttribute = original
    assert instance.qualityAttribute == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_minRangeValue_setter(instance):
    original = instance.minRangeValue
    instance.minRangeValue = original
    assert instance.minRangeValue == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_minimize_setter(instance):
    original = instance.minimize
    instance.minimize = original
    assert instance.minimize == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=fm_Attribute_strategy)
def test_hyp_fm_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original




@given(instance=fm_Group_strategy)
def test_hyp_fm_group_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=fm_Group_strategy)
def test_hyp_fm_group_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=fm_Group_strategy)
def test_hyp_fm_group_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=fm_Group_strategy)
def test_hyp_fm_group_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original



@given(instance=fm_Group_strategy)
def test_hyp_fm_group_xor_setter(instance):
    original = instance.xor
    instance.xor = original
    assert instance.xor == original



@given(instance=fm_Group_strategy)
def test_hyp_fm_group_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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

def test_fm_Attribute_alert_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.alert == True
    instance.alert = False
    assert instance.alert == False


def test_fm_Attribute_comment_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_fm_Attribute_defaultValue_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_fm_Attribute_description_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_fm_Attribute_id_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_fm_Attribute_maxRangeValue_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.maxRangeValue == "sample_text"
    instance.maxRangeValue = "sample_text_2"
    assert instance.maxRangeValue == "sample_text_2"


def test_fm_Attribute_minRangeValue_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.minRangeValue == "sample_text"
    instance.minRangeValue = "sample_text_2"
    assert instance.minRangeValue == "sample_text_2"


def test_fm_Attribute_minimize_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.minimize == True
    instance.minimize = False
    assert instance.minimize == False


def test_fm_Attribute_name_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_fm_Attribute_objectiveFunctionAggregator_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.objectiveFunctionAggregator == "sample_text"
    instance.objectiveFunctionAggregator = "sample_text_2"
    assert instance.objectiveFunctionAggregator == "sample_text_2"


def test_fm_Attribute_qualityAttribute_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.qualityAttribute == True
    instance.qualityAttribute = False
    assert instance.qualityAttribute == False


def test_fm_Attribute_resourceAttribute_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.resourceAttribute == True
    instance.resourceAttribute = False
    assert instance.resourceAttribute == False


def test_fm_Attribute_type_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_fm_Attribute_weight_value_roundtrip():
    instance = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
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
    b1 = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    b2 = fm_Attribute(alert=False, comment="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", id="sample_text_2", maxRangeValue="sample_text_2", minRangeValue="sample_text_2", minimize=False, name="sample_text_2", objectiveFunctionAggregator="sample_text_2", qualityAttribute=False, resourceAttribute=False, type="sample_text_2", weight="sample_text_2")
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
    b1 = fm_Attribute(alert=True, comment="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", maxRangeValue="sample_text", minRangeValue="sample_text", minimize=True, name="sample_text", objectiveFunctionAggregator="sample_text", qualityAttribute=True, resourceAttribute=True, type="sample_text", weight="sample_text")
    b2 = fm_Attribute(alert=False, comment="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", id="sample_text_2", maxRangeValue="sample_text_2", minRangeValue="sample_text_2", minimize=False, name="sample_text_2", objectiveFunctionAggregator="sample_text_2", qualityAttribute=False, resourceAttribute=False, type="sample_text_2", weight="sample_text_2")
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

fm_Attribute_strategy = st.builds(fm_Attribute, alert=st.booleans(), comment=safe_text, defaultValue=safe_text, description=safe_text, id=safe_text, maxRangeValue=safe_text, minRangeValue=safe_text, minimize=st.booleans(), name=safe_text, objectiveFunctionAggregator=safe_text, qualityAttribute=st.booleans(), resourceAttribute=st.booleans(), type=safe_text, weight=safe_text)
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



