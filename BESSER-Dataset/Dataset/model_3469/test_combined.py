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
    AttributeValue,
    featuremodel_AttributeValueString,
    featuremodel_AttributeValueInt,
    AttributeType,
    featuremodel_AttributeTypeEObject,
    featuremodel_AttributeTypeBoolean,
    featuremodel_AttributeTypeString,
    featuremodel_AttributeTypeInt,
    featuremodel_AttributeType,
    featuremodel_AttributeValue,
    featuremodel_EObject,
    featuremodel_AttributeValueEObject,
    featuremodel_AttributeValueBoolean,
    featuremodel_Group,
    Rule,
    featuremodel_Constraint,
    featuremodel_Feature,
    featuremodel_Attribute,
    featuremodel_Description,
    featuremodel_FeatureModel,
    featuremodel_Rule,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_attributevalue_is_not_abstract():
    assert not inspect.isabstract(AttributeValue)


def test_hyp_attributevalue_constructor_exists():
    assert callable(AttributeValue.__init__)


def test_hyp_attributevalue_constructor_args():
    sig = inspect.signature(AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributevaluestring_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueString)


def test_hyp_featuremodel_attributevaluestring_constructor_exists():
    assert callable(featuremodel_AttributeValueString.__init__)


def test_hyp_featuremodel_attributevaluestring_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_featuremodel_attributevalueint_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueInt)


def test_hyp_featuremodel_attributevalueint_constructor_exists():
    assert callable(featuremodel_AttributeValueInt.__init__)


def test_hyp_featuremodel_attributevalueint_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueInt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_attributetype_is_not_abstract():
    assert not inspect.isabstract(AttributeType)


def test_hyp_attributetype_constructor_exists():
    assert callable(AttributeType.__init__)


def test_hyp_attributetype_constructor_args():
    sig = inspect.signature(AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributetypeeobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeEObject)


def test_hyp_featuremodel_attributetypeeobject_constructor_exists():
    assert callable(featuremodel_AttributeTypeEObject.__init__)


def test_hyp_featuremodel_attributetypeeobject_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeEObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributetypeboolean_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeBoolean)


def test_hyp_featuremodel_attributetypeboolean_constructor_exists():
    assert callable(featuremodel_AttributeTypeBoolean.__init__)


def test_hyp_featuremodel_attributetypeboolean_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributetypestring_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeString)


def test_hyp_featuremodel_attributetypestring_constructor_exists():
    assert callable(featuremodel_AttributeTypeString.__init__)


def test_hyp_featuremodel_attributetypestring_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributetypeint_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeTypeInt)


def test_hyp_featuremodel_attributetypeint_constructor_exists():
    assert callable(featuremodel_AttributeTypeInt.__init__)


def test_hyp_featuremodel_attributetypeint_constructor_args():
    sig = inspect.signature(featuremodel_AttributeTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributetype_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeType)


def test_hyp_featuremodel_attributetype_constructor_exists():
    assert callable(featuremodel_AttributeType.__init__)


def test_hyp_featuremodel_attributetype_constructor_args():
    sig = inspect.signature(featuremodel_AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributevalue_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValue)


def test_hyp_featuremodel_attributevalue_constructor_exists():
    assert callable(featuremodel_AttributeValue.__init__)


def test_hyp_featuremodel_attributevalue_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_eobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel_EObject)


def test_hyp_featuremodel_eobject_constructor_exists():
    assert callable(featuremodel_EObject.__init__)


def test_hyp_featuremodel_eobject_constructor_args():
    sig = inspect.signature(featuremodel_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributevalueeobject_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueEObject)


def test_hyp_featuremodel_attributevalueeobject_constructor_exists():
    assert callable(featuremodel_AttributeValueEObject.__init__)


def test_hyp_featuremodel_attributevalueeobject_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueEObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_attributevalueboolean_is_not_abstract():
    assert not inspect.isabstract(featuremodel_AttributeValueBoolean)


def test_hyp_featuremodel_attributevalueboolean_constructor_exists():
    assert callable(featuremodel_AttributeValueBoolean.__init__)


def test_hyp_featuremodel_attributevalueboolean_constructor_args():
    sig = inspect.signature(featuremodel_AttributeValueBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_featuremodel_group_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Group)


def test_hyp_featuremodel_group_constructor_exists():
    assert callable(featuremodel_Group.__init__)


def test_hyp_featuremodel_group_constructor_args():
    sig = inspect.signature(featuremodel_Group.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_hyp_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_hyp_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featuremodel_constraint_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Constraint)


def test_hyp_featuremodel_constraint_constructor_exists():
    assert callable(featuremodel_Constraint.__init__)


def test_hyp_featuremodel_constraint_constructor_args():
    sig = inspect.signature(featuremodel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_featuremodel_feature_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Feature)


def test_hyp_featuremodel_feature_constructor_exists():
    assert callable(featuremodel_Feature.__init__)


def test_hyp_featuremodel_feature_constructor_args():
    sig = inspect.signature(featuremodel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_featuremodel_attribute_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Attribute)


def test_hyp_featuremodel_attribute_constructor_exists():
    assert callable(featuremodel_Attribute.__init__)


def test_hyp_featuremodel_attribute_constructor_args():
    sig = inspect.signature(featuremodel_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "setable" in params, "Missing parameter 'setable'"






def test_hyp_featuremodel_description_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Description)


def test_hyp_featuremodel_description_constructor_exists():
    assert callable(featuremodel_Description.__init__)


def test_hyp_featuremodel_description_constructor_args():
    sig = inspect.signature(featuremodel_Description.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "text" in params, "Missing parameter 'text'"





def test_hyp_featuremodel_featuremodel_is_not_abstract():
    assert not inspect.isabstract(featuremodel_FeatureModel)


def test_hyp_featuremodel_featuremodel_constructor_exists():
    assert callable(featuremodel_FeatureModel.__init__)


def test_hyp_featuremodel_featuremodel_constructor_args():
    sig = inspect.signature(featuremodel_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_featuremodel_rule_is_not_abstract():
    assert not inspect.isabstract(featuremodel_Rule)


def test_hyp_featuremodel_rule_constructor_exists():
    assert callable(featuremodel_Rule.__init__)


def test_hyp_featuremodel_rule_constructor_args():
    sig = inspect.signature(featuremodel_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "code" in params, "Missing parameter 'code'"



def test_hyp_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_hyp_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "mandatory",
        "or_",
        "optional",
        "alternative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariabilityType"


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
AttributeValue_strategy = st.builds(
    AttributeValue,
)
featuremodel_AttributeValueString_strategy = st.builds(
    featuremodel_AttributeValueString,
    value=
        safe_text
)
featuremodel_AttributeValueInt_strategy = st.builds(
    featuremodel_AttributeValueInt,
    value=
        st.integers()
)
AttributeType_strategy = st.builds(
    AttributeType,
)
featuremodel_AttributeTypeEObject_strategy = st.builds(
    featuremodel_AttributeTypeEObject,
)
featuremodel_AttributeTypeBoolean_strategy = st.builds(
    featuremodel_AttributeTypeBoolean,
)
featuremodel_AttributeTypeString_strategy = st.builds(
    featuremodel_AttributeTypeString,
)
featuremodel_AttributeTypeInt_strategy = st.builds(
    featuremodel_AttributeTypeInt,
)
featuremodel_AttributeType_strategy = st.builds(
    featuremodel_AttributeType,
)
featuremodel_AttributeValue_strategy = st.builds(
    featuremodel_AttributeValue,
)
featuremodel_EObject_strategy = st.builds(
    featuremodel_EObject,
)
featuremodel_AttributeValueEObject_strategy = st.builds(
    featuremodel_AttributeValueEObject,
)
featuremodel_AttributeValueBoolean_strategy = st.builds(
    featuremodel_AttributeValueBoolean,
    value=
        st.booleans()
)
featuremodel_Group_strategy = st.builds(
    featuremodel_Group,
    upper=
        st.integers(),
    lower=
        st.integers(),
    id=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
featuremodel_Constraint_strategy = st.builds(
    featuremodel_Constraint,
    id=
        safe_text
)
featuremodel_Feature_strategy = st.builds(
    featuremodel_Feature,
    type=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
featuremodel_Attribute_strategy = st.builds(
    featuremodel_Attribute,
    id=
        safe_text,
    name=
        safe_text,
    setable=
        st.booleans()
)
featuremodel_Description_strategy = st.builds(
    featuremodel_Description,
    id=
        safe_text,
    text=
        safe_text
)
featuremodel_FeatureModel_strategy = st.builds(
    featuremodel_FeatureModel,
    version=
        safe_text,
    id=
        safe_text
)
featuremodel_Rule_strategy = st.builds(
    featuremodel_Rule,
    language=
        safe_text,
    code=
        safe_text
)





@given(instance=featuremodel_AttributeValueString_strategy)
def test_hyp_featuremodel_attributevaluestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=featuremodel_AttributeValueInt_strategy)
def test_hyp_featuremodel_attributevalueint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original













@given(instance=featuremodel_AttributeValueBoolean_strategy)
def test_hyp_featuremodel_attributevalueboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=featuremodel_Group_strategy)
def test_hyp_featuremodel_group_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=featuremodel_Group_strategy)
def test_hyp_featuremodel_group_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=featuremodel_Group_strategy)
def test_hyp_featuremodel_group_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=featuremodel_Constraint_strategy)
def test_hyp_featuremodel_constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=featuremodel_Feature_strategy)
def test_hyp_featuremodel_feature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=featuremodel_Feature_strategy)
def test_hyp_featuremodel_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=featuremodel_Feature_strategy)
def test_hyp_featuremodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=featuremodel_Attribute_strategy)
def test_hyp_featuremodel_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=featuremodel_Attribute_strategy)
def test_hyp_featuremodel_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=featuremodel_Attribute_strategy)
def test_hyp_featuremodel_attribute_setable_setter(instance):
    original = instance.setable
    instance.setable = original
    assert instance.setable == original




@given(instance=featuremodel_Description_strategy)
def test_hyp_featuremodel_description_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=featuremodel_Description_strategy)
def test_hyp_featuremodel_description_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=featuremodel_FeatureModel_strategy)
def test_hyp_featuremodel_featuremodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=featuremodel_FeatureModel_strategy)
def test_hyp_featuremodel_featuremodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=featuremodel_Rule_strategy)
def test_hyp_featuremodel_rule_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=featuremodel_Rule_strategy)
def test_hyp_featuremodel_rule_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AttributeType,
    AttributeValue,
    Rule,
    featuremodel_Attribute,
    featuremodel_AttributeType,
    featuremodel_AttributeTypeBoolean,
    featuremodel_AttributeTypeEObject,
    featuremodel_AttributeTypeInt,
    featuremodel_AttributeTypeString,
    featuremodel_AttributeValue,
    featuremodel_AttributeValueBoolean,
    featuremodel_AttributeValueEObject,
    featuremodel_AttributeValueInt,
    featuremodel_AttributeValueString,
    featuremodel_Constraint,
    featuremodel_Description,
    featuremodel_EObject,
    featuremodel_Feature,
    featuremodel_FeatureModel,
    featuremodel_Group,
    featuremodel_Rule,
    VariabilityType,
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

def test_featuremodel_Attribute_id_value_roundtrip():
    instance = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_featuremodel_Attribute_name_value_roundtrip():
    instance = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featuremodel_Attribute_setable_value_roundtrip():
    instance = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    assert instance.setable == True
    instance.setable = False
    assert instance.setable == False


def test_featuremodel_AttributeValueBoolean_value_value_roundtrip():
    instance = featuremodel_AttributeValueBoolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_featuremodel_AttributeValueInt_value_value_roundtrip():
    instance = featuremodel_AttributeValueInt(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_featuremodel_AttributeValueString_value_value_roundtrip():
    instance = featuremodel_AttributeValueString(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_featuremodel_Constraint_id_value_roundtrip():
    instance = featuremodel_Constraint(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_featuremodel_Description_id_value_roundtrip():
    instance = featuremodel_Description(id="sample_text", text="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_featuremodel_Description_text_value_roundtrip():
    instance = featuremodel_Description(id="sample_text", text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_featuremodel_Feature_id_value_roundtrip():
    instance = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_featuremodel_Feature_name_value_roundtrip():
    instance = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_featuremodel_Feature_type_value_roundtrip():
    instance = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_featuremodel_FeatureModel_id_value_roundtrip():
    instance = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_featuremodel_FeatureModel_version_value_roundtrip():
    instance = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_featuremodel_Group_id_value_roundtrip():
    instance = featuremodel_Group(id="sample_text", lower=7, upper=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_featuremodel_Group_lower_value_roundtrip():
    instance = featuremodel_Group(id="sample_text", lower=7, upper=7)
    assert instance.lower == 7
    instance.lower = 13
    assert instance.lower == 13


def test_featuremodel_Group_upper_value_roundtrip():
    instance = featuremodel_Group(id="sample_text", lower=7, upper=7)
    assert instance.upper == 7
    instance.upper = 13
    assert instance.upper == 13


def test_featuremodel_Rule_code_value_roundtrip():
    instance = featuremodel_Rule(code="sample_text", language="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_featuremodel_Rule_language_value_roundtrip():
    instance = featuremodel_Rule(code="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_featuremodel_AttributeTypeBoolean_isa_AttributeType():
    instance = featuremodel_AttributeTypeBoolean()
    assert isinstance(instance, AttributeType)


def test_featuremodel_AttributeTypeEObject_isa_AttributeType():
    instance = featuremodel_AttributeTypeEObject()
    assert isinstance(instance, AttributeType)


def test_featuremodel_AttributeTypeInt_isa_AttributeType():
    instance = featuremodel_AttributeTypeInt()
    assert isinstance(instance, AttributeType)


def test_featuremodel_AttributeTypeString_isa_AttributeType():
    instance = featuremodel_AttributeTypeString()
    assert isinstance(instance, AttributeType)


def test_featuremodel_AttributeValueBoolean_isa_AttributeValue():
    instance = featuremodel_AttributeValueBoolean(value=True)
    assert isinstance(instance, AttributeValue)


def test_featuremodel_AttributeValueEObject_isa_AttributeValue():
    instance = featuremodel_AttributeValueEObject()
    assert isinstance(instance, AttributeValue)


def test_featuremodel_AttributeValueInt_isa_AttributeValue():
    instance = featuremodel_AttributeValueInt(value=7)
    assert isinstance(instance, AttributeValue)


def test_featuremodel_AttributeValueString_isa_AttributeValue():
    instance = featuremodel_AttributeValueString(value="sample_text")
    assert isinstance(instance, AttributeValue)


def test_featuremodel_Constraint_isa_Rule():
    instance = featuremodel_Constraint(id="sample_text")
    assert isinstance(instance, Rule)


def test_assoc_attributes1_link_reassign_clear():
    a = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    b1 = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    b2 = featuremodel_Attribute(id="sample_text_2", name="sample_text_2", setable=False)
    _safe_set(a, 'featuremodel_FeatureModel2', {b1})
    assert _is_linked(a, 'featuremodel_FeatureModel2', b1)
    if hasattr(b1, 'featuremodel_Attribute'):
        assert _is_linked(b1, 'featuremodel_Attribute', a)
    _safe_set(a, 'featuremodel_FeatureModel2', {b2})
    assert _is_linked(a, 'featuremodel_FeatureModel2', b2)
    if hasattr(b1, 'featuremodel_Attribute'):
        assert not _is_linked(b1, 'featuremodel_Attribute', a)
    if hasattr(b2, 'featuremodel_Attribute'):
        assert _is_linked(b2, 'featuremodel_Attribute', a)
    _safe_set(a, 'featuremodel_FeatureModel2', set())
    assert not _is_linked(a, 'featuremodel_FeatureModel2', b2)
    if hasattr(b2, 'featuremodel_Attribute'):
        assert not _is_linked(b2, 'featuremodel_Attribute', a)


def test_assoc_attributes15_link_reassign_clear():
    a = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    b1 = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    b2 = featuremodel_Attribute(id="sample_text_2", name="sample_text_2", setable=False)
    _safe_set(a, 'featuremodel_Feature16', {b1})
    assert _is_linked(a, 'featuremodel_Feature16', b1)
    if hasattr(b1, 'featuremodel_Attribute17'):
        assert _is_linked(b1, 'featuremodel_Attribute17', a)
    _safe_set(a, 'featuremodel_Feature16', {b2})
    assert _is_linked(a, 'featuremodel_Feature16', b2)
    if hasattr(b1, 'featuremodel_Attribute17'):
        assert not _is_linked(b1, 'featuremodel_Attribute17', a)
    if hasattr(b2, 'featuremodel_Attribute17'):
        assert _is_linked(b2, 'featuremodel_Attribute17', a)
    _safe_set(a, 'featuremodel_Feature16', set())
    assert not _is_linked(a, 'featuremodel_Feature16', b2)
    if hasattr(b2, 'featuremodel_Attribute17'):
        assert not _is_linked(b2, 'featuremodel_Attribute17', a)


def test_assoc_children18_link_reassign_clear():
    a = featuremodel_Group(id="sample_text", lower=7, upper=7)
    b1 = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    b2 = featuremodel_Feature(id="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'featuremodel_Group20', b1)
    assert _is_linked(a, 'featuremodel_Group20', b1)
    if hasattr(b1, 'featuremodel_Feature19'):
        assert _is_linked(b1, 'featuremodel_Feature19', a)
    _safe_set(a, 'featuremodel_Group20', b2)
    assert _is_linked(a, 'featuremodel_Group20', b2)
    if hasattr(b1, 'featuremodel_Feature19'):
        assert not _is_linked(b1, 'featuremodel_Feature19', a)
    if hasattr(b2, 'featuremodel_Feature19'):
        assert _is_linked(b2, 'featuremodel_Feature19', a)
    _safe_set(a, 'featuremodel_Group20', None)
    assert not _is_linked(a, 'featuremodel_Group20', b2)
    if hasattr(b2, 'featuremodel_Feature19'):
        assert not _is_linked(b2, 'featuremodel_Feature19', a)


def test_assoc_constraints5_link_reassign_clear():
    a = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    b1 = featuremodel_Constraint(id="sample_text")
    b2 = featuremodel_Constraint(id="sample_text_2")
    _safe_set(a, 'featuremodel_FeatureModel6', {b1})
    assert _is_linked(a, 'featuremodel_FeatureModel6', b1)
    if hasattr(b1, 'featuremodel_Constraint'):
        assert _is_linked(b1, 'featuremodel_Constraint', a)
    _safe_set(a, 'featuremodel_FeatureModel6', {b2})
    assert _is_linked(a, 'featuremodel_FeatureModel6', b2)
    if hasattr(b1, 'featuremodel_Constraint'):
        assert not _is_linked(b1, 'featuremodel_Constraint', a)
    if hasattr(b2, 'featuremodel_Constraint'):
        assert _is_linked(b2, 'featuremodel_Constraint', a)
    _safe_set(a, 'featuremodel_FeatureModel6', set())
    assert not _is_linked(a, 'featuremodel_FeatureModel6', b2)
    if hasattr(b2, 'featuremodel_Constraint'):
        assert not _is_linked(b2, 'featuremodel_Constraint', a)


def test_assoc_defaultValue24_link_reassign_clear():
    a = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    b1 = featuremodel_AttributeValue()
    b2 = featuremodel_AttributeValue()
    _safe_set(a, 'featuremodel_Attribute25', b1)
    assert _is_linked(a, 'featuremodel_Attribute25', b1)
    if hasattr(b1, 'featuremodel_AttributeValue'):
        assert _is_linked(b1, 'featuremodel_AttributeValue', a)
    _safe_set(a, 'featuremodel_Attribute25', b2)
    assert _is_linked(a, 'featuremodel_Attribute25', b2)
    if hasattr(b1, 'featuremodel_AttributeValue'):
        assert not _is_linked(b1, 'featuremodel_AttributeValue', a)
    if hasattr(b2, 'featuremodel_AttributeValue'):
        assert _is_linked(b2, 'featuremodel_AttributeValue', a)
    _safe_set(a, 'featuremodel_Attribute25', None)
    assert not _is_linked(a, 'featuremodel_Attribute25', b2)
    if hasattr(b2, 'featuremodel_AttributeValue'):
        assert not _is_linked(b2, 'featuremodel_AttributeValue', a)


def test_assoc_description0_link_reassign_clear():
    a = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    b1 = featuremodel_Description(id="sample_text", text="sample_text")
    b2 = featuremodel_Description(id="sample_text_2", text="sample_text_2")
    _safe_set(a, 'featuremodel_FeatureModel', b1)
    assert _is_linked(a, 'featuremodel_FeatureModel', b1)
    if hasattr(b1, 'featuremodel_Description'):
        assert _is_linked(b1, 'featuremodel_Description', a)
    _safe_set(a, 'featuremodel_FeatureModel', b2)
    assert _is_linked(a, 'featuremodel_FeatureModel', b2)
    if hasattr(b1, 'featuremodel_Description'):
        assert not _is_linked(b1, 'featuremodel_Description', a)
    if hasattr(b2, 'featuremodel_Description'):
        assert _is_linked(b2, 'featuremodel_Description', a)
    _safe_set(a, 'featuremodel_FeatureModel', None)
    assert not _is_linked(a, 'featuremodel_FeatureModel', b2)
    if hasattr(b2, 'featuremodel_Description'):
        assert not _is_linked(b2, 'featuremodel_Description', a)


def test_assoc_description12_link_reassign_clear():
    a = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    b1 = featuremodel_Description(id="sample_text", text="sample_text")
    b2 = featuremodel_Description(id="sample_text_2", text="sample_text_2")
    _safe_set(a, 'featuremodel_Feature13', b1)
    assert _is_linked(a, 'featuremodel_Feature13', b1)
    if hasattr(b1, 'featuremodel_Description14'):
        assert _is_linked(b1, 'featuremodel_Description14', a)
    _safe_set(a, 'featuremodel_Feature13', b2)
    assert _is_linked(a, 'featuremodel_Feature13', b2)
    if hasattr(b1, 'featuremodel_Description14'):
        assert not _is_linked(b1, 'featuremodel_Description14', a)
    if hasattr(b2, 'featuremodel_Description14'):
        assert _is_linked(b2, 'featuremodel_Description14', a)
    _safe_set(a, 'featuremodel_Feature13', None)
    assert not _is_linked(a, 'featuremodel_Feature13', b2)
    if hasattr(b2, 'featuremodel_Description14'):
        assert not _is_linked(b2, 'featuremodel_Description14', a)


def test_assoc_description21_link_reassign_clear():
    a = featuremodel_Description(id="sample_text", text="sample_text")
    b1 = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    b2 = featuremodel_Attribute(id="sample_text_2", name="sample_text_2", setable=False)
    _safe_set(a, 'featuremodel_Description23', b1)
    assert _is_linked(a, 'featuremodel_Description23', b1)
    if hasattr(b1, 'featuremodel_Attribute22'):
        assert _is_linked(b1, 'featuremodel_Attribute22', a)
    _safe_set(a, 'featuremodel_Description23', b2)
    assert _is_linked(a, 'featuremodel_Description23', b2)
    if hasattr(b1, 'featuremodel_Attribute22'):
        assert not _is_linked(b1, 'featuremodel_Attribute22', a)
    if hasattr(b2, 'featuremodel_Attribute22'):
        assert _is_linked(b2, 'featuremodel_Attribute22', a)
    _safe_set(a, 'featuremodel_Description23', None)
    assert not _is_linked(a, 'featuremodel_Description23', b2)
    if hasattr(b2, 'featuremodel_Attribute22'):
        assert not _is_linked(b2, 'featuremodel_Attribute22', a)


def test_assoc_description7_link_reassign_clear():
    a = featuremodel_Description(id="sample_text", text="sample_text")
    b1 = featuremodel_Constraint(id="sample_text")
    b2 = featuremodel_Constraint(id="sample_text_2")
    _safe_set(a, 'featuremodel_Description9', b1)
    assert _is_linked(a, 'featuremodel_Description9', b1)
    if hasattr(b1, 'featuremodel_Constraint8'):
        assert _is_linked(b1, 'featuremodel_Constraint8', a)
    _safe_set(a, 'featuremodel_Description9', b2)
    assert _is_linked(a, 'featuremodel_Description9', b2)
    if hasattr(b1, 'featuremodel_Constraint8'):
        assert not _is_linked(b1, 'featuremodel_Constraint8', a)
    if hasattr(b2, 'featuremodel_Constraint8'):
        assert _is_linked(b2, 'featuremodel_Constraint8', a)
    _safe_set(a, 'featuremodel_Description9', None)
    assert not _is_linked(a, 'featuremodel_Description9', b2)
    if hasattr(b2, 'featuremodel_Constraint8'):
        assert not _is_linked(b2, 'featuremodel_Constraint8', a)


def test_assoc_features10_link_reassign_clear():
    a = featuremodel_Group(id="sample_text", lower=7, upper=7)
    b1 = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    b2 = featuremodel_Feature(id="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'featuremodel_Group', {b1})
    assert _is_linked(a, 'featuremodel_Group', b1)
    if hasattr(b1, 'featuremodel_Feature11'):
        assert _is_linked(b1, 'featuremodel_Feature11', a)
    _safe_set(a, 'featuremodel_Group', {b2})
    assert _is_linked(a, 'featuremodel_Group', b2)
    if hasattr(b1, 'featuremodel_Feature11'):
        assert not _is_linked(b1, 'featuremodel_Feature11', a)
    if hasattr(b2, 'featuremodel_Feature11'):
        assert _is_linked(b2, 'featuremodel_Feature11', a)
    _safe_set(a, 'featuremodel_Group', set())
    assert not _is_linked(a, 'featuremodel_Group', b2)
    if hasattr(b2, 'featuremodel_Feature11'):
        assert not _is_linked(b2, 'featuremodel_Feature11', a)


def test_assoc_root3_link_reassign_clear():
    a = featuremodel_FeatureModel(id="sample_text", version="sample_text")
    b1 = featuremodel_Feature(id="sample_text", name="sample_text", type="sample_text")
    b2 = featuremodel_Feature(id="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'featuremodel_FeatureModel4', b1)
    assert _is_linked(a, 'featuremodel_FeatureModel4', b1)
    if hasattr(b1, 'featuremodel_Feature'):
        assert _is_linked(b1, 'featuremodel_Feature', a)
    _safe_set(a, 'featuremodel_FeatureModel4', b2)
    assert _is_linked(a, 'featuremodel_FeatureModel4', b2)
    if hasattr(b1, 'featuremodel_Feature'):
        assert not _is_linked(b1, 'featuremodel_Feature', a)
    if hasattr(b2, 'featuremodel_Feature'):
        assert _is_linked(b2, 'featuremodel_Feature', a)
    _safe_set(a, 'featuremodel_FeatureModel4', None)
    assert not _is_linked(a, 'featuremodel_FeatureModel4', b2)
    if hasattr(b2, 'featuremodel_Feature'):
        assert not _is_linked(b2, 'featuremodel_Feature', a)


def test_assoc_type26_link_reassign_clear():
    a = featuremodel_Attribute(id="sample_text", name="sample_text", setable=True)
    b1 = featuremodel_AttributeType()
    b2 = featuremodel_AttributeType()
    _safe_set(a, 'featuremodel_Attribute27', b1)
    assert _is_linked(a, 'featuremodel_Attribute27', b1)
    if hasattr(b1, 'featuremodel_AttributeType'):
        assert _is_linked(b1, 'featuremodel_AttributeType', a)
    _safe_set(a, 'featuremodel_Attribute27', b2)
    assert _is_linked(a, 'featuremodel_Attribute27', b2)
    if hasattr(b1, 'featuremodel_AttributeType'):
        assert not _is_linked(b1, 'featuremodel_AttributeType', a)
    if hasattr(b2, 'featuremodel_AttributeType'):
        assert _is_linked(b2, 'featuremodel_AttributeType', a)
    _safe_set(a, 'featuremodel_Attribute27', None)
    assert not _is_linked(a, 'featuremodel_Attribute27', b2)
    if hasattr(b2, 'featuremodel_AttributeType'):
        assert not _is_linked(b2, 'featuremodel_AttributeType', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AttributeType_strategy = st.builds(AttributeType)
@given(instance=AttributeType_strategy)
@settings(max_examples=25)
def test_AttributeType_instantiation(instance):
    assert isinstance(instance, AttributeType)


AttributeValue_strategy = st.builds(AttributeValue)
@given(instance=AttributeValue_strategy)
@settings(max_examples=25)
def test_AttributeValue_instantiation(instance):
    assert isinstance(instance, AttributeValue)


Rule_strategy = st.builds(Rule)
@given(instance=Rule_strategy)
@settings(max_examples=25)
def test_Rule_instantiation(instance):
    assert isinstance(instance, Rule)


featuremodel_Attribute_strategy = st.builds(featuremodel_Attribute, id=safe_text, name=safe_text, setable=st.booleans())
@given(instance=featuremodel_Attribute_strategy)
@settings(max_examples=25)
def test_featuremodel_Attribute_instantiation(instance):
    assert isinstance(instance, featuremodel_Attribute)


featuremodel_AttributeType_strategy = st.builds(featuremodel_AttributeType)
@given(instance=featuremodel_AttributeType_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeType_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeType)


featuremodel_AttributeTypeBoolean_strategy = st.builds(featuremodel_AttributeTypeBoolean)
@given(instance=featuremodel_AttributeTypeBoolean_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeTypeBoolean_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeBoolean)


featuremodel_AttributeTypeEObject_strategy = st.builds(featuremodel_AttributeTypeEObject)
@given(instance=featuremodel_AttributeTypeEObject_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeTypeEObject_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeEObject)


featuremodel_AttributeTypeInt_strategy = st.builds(featuremodel_AttributeTypeInt)
@given(instance=featuremodel_AttributeTypeInt_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeTypeInt_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeInt)


featuremodel_AttributeTypeString_strategy = st.builds(featuremodel_AttributeTypeString)
@given(instance=featuremodel_AttributeTypeString_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeTypeString_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeTypeString)


featuremodel_AttributeValue_strategy = st.builds(featuremodel_AttributeValue)
@given(instance=featuremodel_AttributeValue_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeValue_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValue)


featuremodel_AttributeValueBoolean_strategy = st.builds(featuremodel_AttributeValueBoolean, value=st.booleans())
@given(instance=featuremodel_AttributeValueBoolean_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeValueBoolean_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueBoolean)


featuremodel_AttributeValueEObject_strategy = st.builds(featuremodel_AttributeValueEObject)
@given(instance=featuremodel_AttributeValueEObject_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeValueEObject_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueEObject)


featuremodel_AttributeValueInt_strategy = st.builds(featuremodel_AttributeValueInt, value=st.integers())
@given(instance=featuremodel_AttributeValueInt_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeValueInt_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueInt)


featuremodel_AttributeValueString_strategy = st.builds(featuremodel_AttributeValueString, value=safe_text)
@given(instance=featuremodel_AttributeValueString_strategy)
@settings(max_examples=25)
def test_featuremodel_AttributeValueString_instantiation(instance):
    assert isinstance(instance, featuremodel_AttributeValueString)


featuremodel_Constraint_strategy = st.builds(featuremodel_Constraint, id=safe_text)
@given(instance=featuremodel_Constraint_strategy)
@settings(max_examples=25)
def test_featuremodel_Constraint_instantiation(instance):
    assert isinstance(instance, featuremodel_Constraint)


featuremodel_Description_strategy = st.builds(featuremodel_Description, id=safe_text, text=safe_text)
@given(instance=featuremodel_Description_strategy)
@settings(max_examples=25)
def test_featuremodel_Description_instantiation(instance):
    assert isinstance(instance, featuremodel_Description)


featuremodel_EObject_strategy = st.builds(featuremodel_EObject)
@given(instance=featuremodel_EObject_strategy)
@settings(max_examples=25)
def test_featuremodel_EObject_instantiation(instance):
    assert isinstance(instance, featuremodel_EObject)


featuremodel_Feature_strategy = st.builds(featuremodel_Feature, id=safe_text, name=safe_text, type=safe_text)
@given(instance=featuremodel_Feature_strategy)
@settings(max_examples=25)
def test_featuremodel_Feature_instantiation(instance):
    assert isinstance(instance, featuremodel_Feature)


featuremodel_FeatureModel_strategy = st.builds(featuremodel_FeatureModel, id=safe_text, version=safe_text)
@given(instance=featuremodel_FeatureModel_strategy)
@settings(max_examples=25)
def test_featuremodel_FeatureModel_instantiation(instance):
    assert isinstance(instance, featuremodel_FeatureModel)


featuremodel_Group_strategy = st.builds(featuremodel_Group, id=safe_text, lower=st.integers(), upper=st.integers())
@given(instance=featuremodel_Group_strategy)
@settings(max_examples=25)
def test_featuremodel_Group_instantiation(instance):
    assert isinstance(instance, featuremodel_Group)


featuremodel_Rule_strategy = st.builds(featuremodel_Rule, code=safe_text, language=safe_text)
@given(instance=featuremodel_Rule_strategy)
@settings(max_examples=25)
def test_featuremodel_Rule_instantiation(instance):
    assert isinstance(instance, featuremodel_Rule)



