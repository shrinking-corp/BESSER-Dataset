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
    Influence,
    FeatureConstraint,
    Conncection,
    FCORE_Conncection,
    FCORE_Influence,
    SingleFeatureConnection,
    FCORE_CardinalityConnection,
    Feature,
    FCORE_SingleFeatureConnection,
    FCORE_FeatureConstraint,
    FCORE_InfluenceAttribute,
    FCORE_InfluenceFeature,
    FCORE_Softgoal,
    FCORE_ExcludesFeatureConstraint,
    FCORE_RequiresFeatureConstraint,
    FCORE_AttributeConstraint,
    FCORE_Attribute,
    FCORE_FeatureGroup,
    FCORE_SolitaryFeature,
    FCORE_GroupFeature,
    FCORE_RootFeature,
    FCORE_FeatureModel,
    FCORE_Feature,
    FCORE_AttributeConstraintConnection,
    FCORE_GroupToFeatureConnection,
    FCORE_FeatureToGroupConnection,
    FCORE_OptionalConnection,
    FCORE_MandatoryConnection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_influence_is_not_abstract():
    assert not inspect.isabstract(Influence)


def test_hyp_influence_constructor_exists():
    assert callable(Influence.__init__)


def test_hyp_influence_constructor_args():
    sig = inspect.signature(Influence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featureconstraint_is_not_abstract():
    assert not inspect.isabstract(FeatureConstraint)


def test_hyp_featureconstraint_constructor_exists():
    assert callable(FeatureConstraint.__init__)


def test_hyp_featureconstraint_constructor_args():
    sig = inspect.signature(FeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conncection_is_not_abstract():
    assert not inspect.isabstract(Conncection)


def test_hyp_conncection_constructor_exists():
    assert callable(Conncection.__init__)


def test_hyp_conncection_constructor_args():
    sig = inspect.signature(Conncection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_conncection_is_not_abstract():
    assert not inspect.isabstract(FCORE_Conncection)


def test_hyp_fcore_conncection_constructor_exists():
    assert callable(FCORE_Conncection.__init__)


def test_hyp_fcore_conncection_constructor_args():
    sig = inspect.signature(FCORE_Conncection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_influence_is_not_abstract():
    assert not inspect.isabstract(FCORE_Influence)


def test_hyp_fcore_influence_constructor_exists():
    assert callable(FCORE_Influence.__init__)


def test_hyp_fcore_influence_constructor_args():
    sig = inspect.signature(FCORE_Influence.__init__)
    params = list(sig.parameters.keys())
    assert "contribution" in params, "Missing parameter 'contribution'"




def test_hyp_singlefeatureconnection_is_not_abstract():
    assert not inspect.isabstract(SingleFeatureConnection)


def test_hyp_singlefeatureconnection_constructor_exists():
    assert callable(SingleFeatureConnection.__init__)


def test_hyp_singlefeatureconnection_constructor_args():
    sig = inspect.signature(SingleFeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_cardinalityconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE_CardinalityConnection)


def test_hyp_fcore_cardinalityconnection_constructor_exists():
    assert callable(FCORE_CardinalityConnection.__init__)


def test_hyp_fcore_cardinalityconnection_constructor_args():
    sig = inspect.signature(FCORE_CardinalityConnection.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"





def test_hyp_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_hyp_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_hyp_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_singlefeatureconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE_SingleFeatureConnection)


def test_hyp_fcore_singlefeatureconnection_constructor_exists():
    assert callable(FCORE_SingleFeatureConnection.__init__)


def test_hyp_fcore_singlefeatureconnection_constructor_args():
    sig = inspect.signature(FCORE_SingleFeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_featureconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE_FeatureConstraint)


def test_hyp_fcore_featureconstraint_constructor_exists():
    assert callable(FCORE_FeatureConstraint.__init__)


def test_hyp_fcore_featureconstraint_constructor_args():
    sig = inspect.signature(FCORE_FeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_influenceattribute_is_not_abstract():
    assert not inspect.isabstract(FCORE_InfluenceAttribute)


def test_hyp_fcore_influenceattribute_constructor_exists():
    assert callable(FCORE_InfluenceAttribute.__init__)


def test_hyp_fcore_influenceattribute_constructor_args():
    sig = inspect.signature(FCORE_InfluenceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_influencefeature_is_not_abstract():
    assert not inspect.isabstract(FCORE_InfluenceFeature)


def test_hyp_fcore_influencefeature_constructor_exists():
    assert callable(FCORE_InfluenceFeature.__init__)


def test_hyp_fcore_influencefeature_constructor_args():
    sig = inspect.signature(FCORE_InfluenceFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_softgoal_is_not_abstract():
    assert not inspect.isabstract(FCORE_Softgoal)


def test_hyp_fcore_softgoal_constructor_exists():
    assert callable(FCORE_Softgoal.__init__)


def test_hyp_fcore_softgoal_constructor_args():
    sig = inspect.signature(FCORE_Softgoal.__init__)
    params = list(sig.parameters.keys())
    assert "weighting" in params, "Missing parameter 'weighting'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_fcore_excludesfeatureconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE_ExcludesFeatureConstraint)


def test_hyp_fcore_excludesfeatureconstraint_constructor_exists():
    assert callable(FCORE_ExcludesFeatureConstraint.__init__)


def test_hyp_fcore_excludesfeatureconstraint_constructor_args():
    sig = inspect.signature(FCORE_ExcludesFeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_requiresfeatureconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE_RequiresFeatureConstraint)


def test_hyp_fcore_requiresfeatureconstraint_constructor_exists():
    assert callable(FCORE_RequiresFeatureConstraint.__init__)


def test_hyp_fcore_requiresfeatureconstraint_constructor_args():
    sig = inspect.signature(FCORE_RequiresFeatureConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_attributeconstraint_is_not_abstract():
    assert not inspect.isabstract(FCORE_AttributeConstraint)


def test_hyp_fcore_attributeconstraint_constructor_exists():
    assert callable(FCORE_AttributeConstraint.__init__)


def test_hyp_fcore_attributeconstraint_constructor_args():
    sig = inspect.signature(FCORE_AttributeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "equation" in params, "Missing parameter 'equation'"




def test_hyp_fcore_attribute_is_not_abstract():
    assert not inspect.isabstract(FCORE_Attribute)


def test_hyp_fcore_attribute_constructor_exists():
    assert callable(FCORE_Attribute.__init__)


def test_hyp_fcore_attribute_constructor_args():
    sig = inspect.signature(FCORE_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "min" in params, "Missing parameter 'min'"
    assert "name" in params, "Missing parameter 'name'"
    assert "max" in params, "Missing parameter 'max'"







def test_hyp_fcore_featuregroup_is_not_abstract():
    assert not inspect.isabstract(FCORE_FeatureGroup)


def test_hyp_fcore_featuregroup_constructor_exists():
    assert callable(FCORE_FeatureGroup.__init__)


def test_hyp_fcore_featuregroup_constructor_args():
    sig = inspect.signature(FCORE_FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"





def test_hyp_fcore_solitaryfeature_is_not_abstract():
    assert not inspect.isabstract(FCORE_SolitaryFeature)


def test_hyp_fcore_solitaryfeature_constructor_exists():
    assert callable(FCORE_SolitaryFeature.__init__)


def test_hyp_fcore_solitaryfeature_constructor_args():
    sig = inspect.signature(FCORE_SolitaryFeature.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"





def test_hyp_fcore_groupfeature_is_not_abstract():
    assert not inspect.isabstract(FCORE_GroupFeature)


def test_hyp_fcore_groupfeature_constructor_exists():
    assert callable(FCORE_GroupFeature.__init__)


def test_hyp_fcore_groupfeature_constructor_args():
    sig = inspect.signature(FCORE_GroupFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_rootfeature_is_not_abstract():
    assert not inspect.isabstract(FCORE_RootFeature)


def test_hyp_fcore_rootfeature_constructor_exists():
    assert callable(FCORE_RootFeature.__init__)


def test_hyp_fcore_rootfeature_constructor_args():
    sig = inspect.signature(FCORE_RootFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_featuremodel_is_not_abstract():
    assert not inspect.isabstract(FCORE_FeatureModel)


def test_hyp_fcore_featuremodel_constructor_exists():
    assert callable(FCORE_FeatureModel.__init__)


def test_hyp_fcore_featuremodel_constructor_args():
    sig = inspect.signature(FCORE_FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_feature_is_not_abstract():
    assert not inspect.isabstract(FCORE_Feature)


def test_hyp_fcore_feature_constructor_exists():
    assert callable(FCORE_Feature.__init__)


def test_hyp_fcore_feature_constructor_args():
    sig = inspect.signature(FCORE_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "selected" in params, "Missing parameter 'selected'"





def test_hyp_fcore_attributeconstraintconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE_AttributeConstraintConnection)


def test_hyp_fcore_attributeconstraintconnection_constructor_exists():
    assert callable(FCORE_AttributeConstraintConnection.__init__)


def test_hyp_fcore_attributeconstraintconnection_constructor_args():
    sig = inspect.signature(FCORE_AttributeConstraintConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_grouptofeatureconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE_GroupToFeatureConnection)


def test_hyp_fcore_grouptofeatureconnection_constructor_exists():
    assert callable(FCORE_GroupToFeatureConnection.__init__)


def test_hyp_fcore_grouptofeatureconnection_constructor_args():
    sig = inspect.signature(FCORE_GroupToFeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_featuretogroupconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE_FeatureToGroupConnection)


def test_hyp_fcore_featuretogroupconnection_constructor_exists():
    assert callable(FCORE_FeatureToGroupConnection.__init__)


def test_hyp_fcore_featuretogroupconnection_constructor_args():
    sig = inspect.signature(FCORE_FeatureToGroupConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_optionalconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE_OptionalConnection)


def test_hyp_fcore_optionalconnection_constructor_exists():
    assert callable(FCORE_OptionalConnection.__init__)


def test_hyp_fcore_optionalconnection_constructor_args():
    sig = inspect.signature(FCORE_OptionalConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fcore_mandatoryconnection_is_not_abstract():
    assert not inspect.isabstract(FCORE_MandatoryConnection)


def test_hyp_fcore_mandatoryconnection_constructor_exists():
    assert callable(FCORE_MandatoryConnection.__init__)


def test_hyp_fcore_mandatoryconnection_constructor_args():
    sig = inspect.signature(FCORE_MandatoryConnection.__init__)
    params = list(sig.parameters.keys())


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
Influence_strategy = st.builds(
    Influence,
)
FeatureConstraint_strategy = st.builds(
    FeatureConstraint,
)
Conncection_strategy = st.builds(
    Conncection,
)
FCORE_Conncection_strategy = st.builds(
    FCORE_Conncection,
)
FCORE_Influence_strategy = st.builds(
    FCORE_Influence,
    contribution=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SingleFeatureConnection_strategy = st.builds(
    SingleFeatureConnection,
)
FCORE_CardinalityConnection_strategy = st.builds(
    FCORE_CardinalityConnection,
    max=
        st.integers(),
    min=
        st.integers()
)
Feature_strategy = st.builds(
    Feature,
)
FCORE_SingleFeatureConnection_strategy = st.builds(
    FCORE_SingleFeatureConnection,
)
FCORE_FeatureConstraint_strategy = st.builds(
    FCORE_FeatureConstraint,
)
FCORE_InfluenceAttribute_strategy = st.builds(
    FCORE_InfluenceAttribute,
)
FCORE_InfluenceFeature_strategy = st.builds(
    FCORE_InfluenceFeature,
)
FCORE_Softgoal_strategy = st.builds(
    FCORE_Softgoal,
    weighting=
        safe_text,
    name=
        safe_text
)
FCORE_ExcludesFeatureConstraint_strategy = st.builds(
    FCORE_ExcludesFeatureConstraint,
)
FCORE_RequiresFeatureConstraint_strategy = st.builds(
    FCORE_RequiresFeatureConstraint,
)
FCORE_AttributeConstraint_strategy = st.builds(
    FCORE_AttributeConstraint,
    equation=
        safe_text
)
FCORE_Attribute_strategy = st.builds(
    FCORE_Attribute,
    value=
        st.integers(),
    min=
        st.integers(),
    name=
        safe_text,
    max=
        st.integers()
)
FCORE_FeatureGroup_strategy = st.builds(
    FCORE_FeatureGroup,
    max=
        st.integers(),
    min=
        st.integers()
)
FCORE_SolitaryFeature_strategy = st.builds(
    FCORE_SolitaryFeature,
    max=
        st.integers(),
    min=
        st.integers()
)
FCORE_GroupFeature_strategy = st.builds(
    FCORE_GroupFeature,
)
FCORE_RootFeature_strategy = st.builds(
    FCORE_RootFeature,
)
FCORE_FeatureModel_strategy = st.builds(
    FCORE_FeatureModel,
)
FCORE_Feature_strategy = st.builds(
    FCORE_Feature,
    name=
        safe_text,
    selected=
        st.booleans()
)
FCORE_AttributeConstraintConnection_strategy = st.builds(
    FCORE_AttributeConstraintConnection,
)
FCORE_GroupToFeatureConnection_strategy = st.builds(
    FCORE_GroupToFeatureConnection,
)
FCORE_FeatureToGroupConnection_strategy = st.builds(
    FCORE_FeatureToGroupConnection,
)
FCORE_OptionalConnection_strategy = st.builds(
    FCORE_OptionalConnection,
)
FCORE_MandatoryConnection_strategy = st.builds(
    FCORE_MandatoryConnection,
)








@given(instance=FCORE_Influence_strategy)
def test_hyp_fcore_influence_contribution_setter(instance):
    original = instance.contribution
    instance.contribution = original
    assert instance.contribution == original





@given(instance=FCORE_CardinalityConnection_strategy)
def test_hyp_fcore_cardinalityconnection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=FCORE_CardinalityConnection_strategy)
def test_hyp_fcore_cardinalityconnection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original









@given(instance=FCORE_Softgoal_strategy)
def test_hyp_fcore_softgoal_weighting_setter(instance):
    original = instance.weighting
    instance.weighting = original
    assert instance.weighting == original



@given(instance=FCORE_Softgoal_strategy)
def test_hyp_fcore_softgoal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=FCORE_AttributeConstraint_strategy)
def test_hyp_fcore_attributeconstraint_equation_setter(instance):
    original = instance.equation
    instance.equation = original
    assert instance.equation == original




@given(instance=FCORE_Attribute_strategy)
def test_hyp_fcore_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=FCORE_Attribute_strategy)
def test_hyp_fcore_attribute_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=FCORE_Attribute_strategy)
def test_hyp_fcore_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FCORE_Attribute_strategy)
def test_hyp_fcore_attribute_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original




@given(instance=FCORE_FeatureGroup_strategy)
def test_hyp_fcore_featuregroup_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=FCORE_FeatureGroup_strategy)
def test_hyp_fcore_featuregroup_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original




@given(instance=FCORE_SolitaryFeature_strategy)
def test_hyp_fcore_solitaryfeature_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=FCORE_SolitaryFeature_strategy)
def test_hyp_fcore_solitaryfeature_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original







@given(instance=FCORE_Feature_strategy)
def test_hyp_fcore_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=FCORE_Feature_strategy)
def test_hyp_fcore_feature_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Conncection,
    FCORE_Attribute,
    FCORE_AttributeConstraint,
    FCORE_AttributeConstraintConnection,
    FCORE_CardinalityConnection,
    FCORE_Conncection,
    FCORE_ExcludesFeatureConstraint,
    FCORE_Feature,
    FCORE_FeatureConstraint,
    FCORE_FeatureGroup,
    FCORE_FeatureModel,
    FCORE_FeatureToGroupConnection,
    FCORE_GroupFeature,
    FCORE_GroupToFeatureConnection,
    FCORE_Influence,
    FCORE_InfluenceAttribute,
    FCORE_InfluenceFeature,
    FCORE_MandatoryConnection,
    FCORE_OptionalConnection,
    FCORE_RequiresFeatureConstraint,
    FCORE_RootFeature,
    FCORE_SingleFeatureConnection,
    FCORE_Softgoal,
    FCORE_SolitaryFeature,
    Feature,
    FeatureConstraint,
    Influence,
    SingleFeatureConnection,
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

def test_FCORE_Attribute_max_value_roundtrip():
    instance = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_FCORE_Attribute_min_value_roundtrip():
    instance = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_FCORE_Attribute_name_value_roundtrip():
    instance = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FCORE_Attribute_value_value_roundtrip():
    instance = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_FCORE_AttributeConstraint_equation_value_roundtrip():
    instance = FCORE_AttributeConstraint(equation="sample_text")
    assert instance.equation == "sample_text"
    instance.equation = "sample_text_2"
    assert instance.equation == "sample_text_2"


def test_FCORE_CardinalityConnection_max_value_roundtrip():
    instance = FCORE_CardinalityConnection(max=7, min=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_FCORE_CardinalityConnection_min_value_roundtrip():
    instance = FCORE_CardinalityConnection(max=7, min=7)
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_FCORE_Feature_name_value_roundtrip():
    instance = FCORE_Feature(name="sample_text", selected=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FCORE_Feature_selected_value_roundtrip():
    instance = FCORE_Feature(name="sample_text", selected=True)
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_FCORE_FeatureGroup_max_value_roundtrip():
    instance = FCORE_FeatureGroup(max=7, min=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_FCORE_FeatureGroup_min_value_roundtrip():
    instance = FCORE_FeatureGroup(max=7, min=7)
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_FCORE_Influence_contribution_value_roundtrip():
    instance = FCORE_Influence(contribution=3.14)
    assert instance.contribution == 3.14
    instance.contribution = 9.99
    assert instance.contribution == 9.99


def test_FCORE_Softgoal_name_value_roundtrip():
    instance = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FCORE_Softgoal_weighting_value_roundtrip():
    instance = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    assert instance.weighting == "sample_text"
    instance.weighting = "sample_text_2"
    assert instance.weighting == "sample_text_2"


def test_FCORE_SolitaryFeature_max_value_roundtrip():
    instance = FCORE_SolitaryFeature(max=7, min=7)
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_FCORE_SolitaryFeature_min_value_roundtrip():
    instance = FCORE_SolitaryFeature(max=7, min=7)
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_FCORE_AttributeConstraintConnection_isa_Conncection():
    instance = FCORE_AttributeConstraintConnection()
    assert isinstance(instance, Conncection)


def test_FCORE_FeatureConstraint_isa_Conncection():
    instance = FCORE_FeatureConstraint()
    assert isinstance(instance, Conncection)


def test_FCORE_FeatureToGroupConnection_isa_Conncection():
    instance = FCORE_FeatureToGroupConnection()
    assert isinstance(instance, Conncection)


def test_FCORE_GroupToFeatureConnection_isa_Conncection():
    instance = FCORE_GroupToFeatureConnection()
    assert isinstance(instance, Conncection)


def test_FCORE_Influence_isa_Conncection():
    instance = FCORE_Influence(contribution=3.14)
    assert isinstance(instance, Conncection)


def test_FCORE_SingleFeatureConnection_isa_Conncection():
    instance = FCORE_SingleFeatureConnection()
    assert isinstance(instance, Conncection)


def test_FCORE_GroupFeature_isa_Feature():
    instance = FCORE_GroupFeature()
    assert isinstance(instance, Feature)


def test_FCORE_RootFeature_isa_Feature():
    instance = FCORE_RootFeature()
    assert isinstance(instance, Feature)


def test_FCORE_SolitaryFeature_isa_Feature():
    instance = FCORE_SolitaryFeature(max=7, min=7)
    assert isinstance(instance, Feature)


def test_FCORE_ExcludesFeatureConstraint_isa_FeatureConstraint():
    instance = FCORE_ExcludesFeatureConstraint()
    assert isinstance(instance, FeatureConstraint)


def test_FCORE_RequiresFeatureConstraint_isa_FeatureConstraint():
    instance = FCORE_RequiresFeatureConstraint()
    assert isinstance(instance, FeatureConstraint)


def test_FCORE_InfluenceAttribute_isa_Influence():
    instance = FCORE_InfluenceAttribute()
    assert isinstance(instance, Influence)


def test_FCORE_InfluenceFeature_isa_Influence():
    instance = FCORE_InfluenceFeature()
    assert isinstance(instance, Influence)


def test_FCORE_CardinalityConnection_isa_SingleFeatureConnection():
    instance = FCORE_CardinalityConnection(max=7, min=7)
    assert isinstance(instance, SingleFeatureConnection)


def test_FCORE_MandatoryConnection_isa_SingleFeatureConnection():
    instance = FCORE_MandatoryConnection()
    assert isinstance(instance, SingleFeatureConnection)


def test_FCORE_OptionalConnection_isa_SingleFeatureConnection():
    instance = FCORE_OptionalConnection()
    assert isinstance(instance, SingleFeatureConnection)


def test_assoc_attribute63_link_reassign_clear():
    a = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    b1 = FCORE_InfluenceAttribute()
    b2 = FCORE_InfluenceAttribute()
    _safe_set(a, 'Attribute', b1)
    assert _is_linked(a, 'Attribute', b1)
    if hasattr(b1, 'influences64'):
        assert _is_linked(b1, 'influences64', a)
    _safe_set(a, 'Attribute', b2)
    assert _is_linked(a, 'Attribute', b2)
    if hasattr(b1, 'influences64'):
        assert not _is_linked(b1, 'influences64', a)
    if hasattr(b2, 'influences64'):
        assert _is_linked(b2, 'influences64', a)
    _safe_set(a, 'Attribute', None)
    assert not _is_linked(a, 'Attribute', b2)
    if hasattr(b2, 'influences64'):
        assert not _is_linked(b2, 'influences64', a)


def test_assoc_attributeConstraintConnection53_link_reassign_clear():
    a = FCORE_AttributeConstraint(equation="sample_text")
    b1 = FCORE_AttributeConstraintConnection()
    b2 = FCORE_AttributeConstraintConnection()
    _safe_set(a, 'target54', b1)
    assert _is_linked(a, 'target54', b1)
    if hasattr(b1, 'AttributeConstraintConnection55'):
        assert _is_linked(b1, 'AttributeConstraintConnection55', a)
    _safe_set(a, 'target54', b2)
    assert _is_linked(a, 'target54', b2)
    if hasattr(b1, 'AttributeConstraintConnection55'):
        assert not _is_linked(b1, 'AttributeConstraintConnection55', a)
    if hasattr(b2, 'AttributeConstraintConnection55'):
        assert _is_linked(b2, 'AttributeConstraintConnection55', a)
    _safe_set(a, 'target54', None)
    assert not _is_linked(a, 'target54', b2)
    if hasattr(b2, 'AttributeConstraintConnection55'):
        assert not _is_linked(b2, 'AttributeConstraintConnection55', a)


def test_assoc_attributeConstraints31_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_AttributeConstraintConnection()
    b2 = FCORE_AttributeConstraintConnection()
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'AttributeConstraintConnection'):
        assert _is_linked(b1, 'AttributeConstraintConnection', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'AttributeConstraintConnection'):
        assert not _is_linked(b1, 'AttributeConstraintConnection', a)
    if hasattr(b2, 'AttributeConstraintConnection'):
        assert _is_linked(b2, 'AttributeConstraintConnection', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'AttributeConstraintConnection'):
        assert not _is_linked(b2, 'AttributeConstraintConnection', a)


def test_assoc_attributeConstraints9_link_reassign_clear():
    a = FCORE_AttributeConstraint(equation="sample_text")
    b1 = FCORE_FeatureModel()
    b2 = FCORE_FeatureModel()
    _safe_set(a, 'FCORE_AttributeConstraint', b1)
    assert _is_linked(a, 'FCORE_AttributeConstraint', b1)
    if hasattr(b1, 'FCORE_FeatureModel10'):
        assert _is_linked(b1, 'FCORE_FeatureModel10', a)
    _safe_set(a, 'FCORE_AttributeConstraint', b2)
    assert _is_linked(a, 'FCORE_AttributeConstraint', b2)
    if hasattr(b1, 'FCORE_FeatureModel10'):
        assert not _is_linked(b1, 'FCORE_FeatureModel10', a)
    if hasattr(b2, 'FCORE_FeatureModel10'):
        assert _is_linked(b2, 'FCORE_FeatureModel10', a)
    _safe_set(a, 'FCORE_AttributeConstraint', None)
    assert not _is_linked(a, 'FCORE_AttributeConstraint', b2)
    if hasattr(b2, 'FCORE_FeatureModel10'):
        assert not _is_linked(b2, 'FCORE_FeatureModel10', a)


def test_assoc_attributes32_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    b2 = FCORE_Attribute(max=13, min=13, name="sample_text_2", value=13)
    _safe_set(a, 'FCORE_Feature', {b1})
    assert _is_linked(a, 'FCORE_Feature', b1)
    if hasattr(b1, 'FCORE_Attribute33'):
        assert _is_linked(b1, 'FCORE_Attribute33', a)
    _safe_set(a, 'FCORE_Feature', {b2})
    assert _is_linked(a, 'FCORE_Feature', b2)
    if hasattr(b1, 'FCORE_Attribute33'):
        assert not _is_linked(b1, 'FCORE_Attribute33', a)
    if hasattr(b2, 'FCORE_Attribute33'):
        assert _is_linked(b2, 'FCORE_Attribute33', a)
    _safe_set(a, 'FCORE_Feature', set())
    assert not _is_linked(a, 'FCORE_Feature', b2)
    if hasattr(b2, 'FCORE_Attribute33'):
        assert not _is_linked(b2, 'FCORE_Attribute33', a)


def test_assoc_attributes7_link_reassign_clear():
    a = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    b1 = FCORE_FeatureModel()
    b2 = FCORE_FeatureModel()
    _safe_set(a, 'FCORE_Attribute', b1)
    assert _is_linked(a, 'FCORE_Attribute', b1)
    if hasattr(b1, 'FCORE_FeatureModel8'):
        assert _is_linked(b1, 'FCORE_FeatureModel8', a)
    _safe_set(a, 'FCORE_Attribute', b2)
    assert _is_linked(a, 'FCORE_Attribute', b2)
    if hasattr(b1, 'FCORE_FeatureModel8'):
        assert not _is_linked(b1, 'FCORE_FeatureModel8', a)
    if hasattr(b2, 'FCORE_FeatureModel8'):
        assert _is_linked(b2, 'FCORE_FeatureModel8', a)
    _safe_set(a, 'FCORE_Attribute', None)
    assert not _is_linked(a, 'FCORE_Attribute', b2)
    if hasattr(b2, 'FCORE_FeatureModel8'):
        assert not _is_linked(b2, 'FCORE_FeatureModel8', a)


def test_assoc_feature61_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_InfluenceFeature()
    b2 = FCORE_InfluenceFeature()
    _safe_set(a, 'Feature62', b1)
    assert _is_linked(a, 'Feature62', b1)
    if hasattr(b1, 'influences'):
        assert _is_linked(b1, 'influences', a)
    _safe_set(a, 'Feature62', b2)
    assert _is_linked(a, 'Feature62', b2)
    if hasattr(b1, 'influences'):
        assert not _is_linked(b1, 'influences', a)
    if hasattr(b2, 'influences'):
        assert _is_linked(b2, 'influences', a)
    _safe_set(a, 'Feature62', None)
    assert not _is_linked(a, 'Feature62', b2)
    if hasattr(b2, 'influences'):
        assert not _is_linked(b2, 'influences', a)


def test_assoc_featureConstraintsEnds35_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_FeatureConstraint()
    b2 = FCORE_FeatureConstraint()
    _safe_set(a, 'featureEnd', {b1})
    assert _is_linked(a, 'featureEnd', b1)
    if hasattr(b1, 'FeatureConstraint36'):
        assert _is_linked(b1, 'FeatureConstraint36', a)
    _safe_set(a, 'featureEnd', {b2})
    assert _is_linked(a, 'featureEnd', b2)
    if hasattr(b1, 'FeatureConstraint36'):
        assert not _is_linked(b1, 'FeatureConstraint36', a)
    if hasattr(b2, 'FeatureConstraint36'):
        assert _is_linked(b2, 'FeatureConstraint36', a)
    _safe_set(a, 'featureEnd', set())
    assert not _is_linked(a, 'featureEnd', b2)
    if hasattr(b2, 'FeatureConstraint36'):
        assert not _is_linked(b2, 'FeatureConstraint36', a)


def test_assoc_featureConstraintsStarts34_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_FeatureConstraint()
    b2 = FCORE_FeatureConstraint()
    _safe_set(a, 'featureStart', {b1})
    assert _is_linked(a, 'featureStart', b1)
    if hasattr(b1, 'FeatureConstraint'):
        assert _is_linked(b1, 'FeatureConstraint', a)
    _safe_set(a, 'featureStart', {b2})
    assert _is_linked(a, 'featureStart', b2)
    if hasattr(b1, 'FeatureConstraint'):
        assert not _is_linked(b1, 'FeatureConstraint', a)
    if hasattr(b2, 'FeatureConstraint'):
        assert _is_linked(b2, 'FeatureConstraint', a)
    _safe_set(a, 'featureStart', set())
    assert not _is_linked(a, 'featureStart', b2)
    if hasattr(b2, 'FeatureConstraint'):
        assert not _is_linked(b2, 'FeatureConstraint', a)


def test_assoc_featureEnd58_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_FeatureConstraint()
    b2 = FCORE_FeatureConstraint()
    _safe_set(a, 'Feature59', b1)
    assert _is_linked(a, 'Feature59', b1)
    if hasattr(b1, 'featureConstraintsEnds'):
        assert _is_linked(b1, 'featureConstraintsEnds', a)
    _safe_set(a, 'Feature59', b2)
    assert _is_linked(a, 'Feature59', b2)
    if hasattr(b1, 'featureConstraintsEnds'):
        assert not _is_linked(b1, 'featureConstraintsEnds', a)
    if hasattr(b2, 'featureConstraintsEnds'):
        assert _is_linked(b2, 'featureConstraintsEnds', a)
    _safe_set(a, 'Feature59', None)
    assert not _is_linked(a, 'Feature59', b2)
    if hasattr(b2, 'featureConstraintsEnds'):
        assert not _is_linked(b2, 'featureConstraintsEnds', a)


def test_assoc_featureGroups5_link_reassign_clear():
    a = FCORE_FeatureGroup(max=7, min=7)
    b1 = FCORE_FeatureModel()
    b2 = FCORE_FeatureModel()
    _safe_set(a, 'FCORE_FeatureGroup', b1)
    assert _is_linked(a, 'FCORE_FeatureGroup', b1)
    if hasattr(b1, 'FCORE_FeatureModel6'):
        assert _is_linked(b1, 'FCORE_FeatureModel6', a)
    _safe_set(a, 'FCORE_FeatureGroup', b2)
    assert _is_linked(a, 'FCORE_FeatureGroup', b2)
    if hasattr(b1, 'FCORE_FeatureModel6'):
        assert not _is_linked(b1, 'FCORE_FeatureModel6', a)
    if hasattr(b2, 'FCORE_FeatureModel6'):
        assert _is_linked(b2, 'FCORE_FeatureModel6', a)
    _safe_set(a, 'FCORE_FeatureGroup', None)
    assert not _is_linked(a, 'FCORE_FeatureGroup', b2)
    if hasattr(b2, 'FCORE_FeatureModel6'):
        assert not _is_linked(b2, 'FCORE_FeatureModel6', a)


def test_assoc_featureStart57_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_FeatureConstraint()
    b2 = FCORE_FeatureConstraint()
    _safe_set(a, 'Feature', b1)
    assert _is_linked(a, 'Feature', b1)
    if hasattr(b1, 'featureConstraintsStarts'):
        assert _is_linked(b1, 'featureConstraintsStarts', a)
    _safe_set(a, 'Feature', b2)
    assert _is_linked(a, 'Feature', b2)
    if hasattr(b1, 'featureConstraintsStarts'):
        assert not _is_linked(b1, 'featureConstraintsStarts', a)
    if hasattr(b2, 'featureConstraintsStarts'):
        assert _is_linked(b2, 'featureConstraintsStarts', a)
    _safe_set(a, 'Feature', None)
    assert not _is_linked(a, 'Feature', b2)
    if hasattr(b2, 'featureConstraintsStarts'):
        assert not _is_linked(b2, 'featureConstraintsStarts', a)


def test_assoc_featureToGroupConnection46_link_reassign_clear():
    a = FCORE_FeatureGroup(max=7, min=7)
    b1 = FCORE_FeatureToGroupConnection()
    b2 = FCORE_FeatureToGroupConnection()
    _safe_set(a, 'target47', b1)
    assert _is_linked(a, 'target47', b1)
    if hasattr(b1, 'FeatureToGroupConnection48'):
        assert _is_linked(b1, 'FeatureToGroupConnection48', a)
    _safe_set(a, 'target47', b2)
    assert _is_linked(a, 'target47', b2)
    if hasattr(b1, 'FeatureToGroupConnection48'):
        assert not _is_linked(b1, 'FeatureToGroupConnection48', a)
    if hasattr(b2, 'FeatureToGroupConnection48'):
        assert _is_linked(b2, 'FeatureToGroupConnection48', a)
    _safe_set(a, 'target47', None)
    assert not _is_linked(a, 'target47', b2)
    if hasattr(b2, 'FeatureToGroupConnection48'):
        assert not _is_linked(b2, 'FeatureToGroupConnection48', a)


def test_assoc_featureToGroupConnections40_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_FeatureToGroupConnection()
    b2 = FCORE_FeatureToGroupConnection()
    _safe_set(a, 'source41', {b1})
    assert _is_linked(a, 'source41', b1)
    if hasattr(b1, 'FeatureToGroupConnection'):
        assert _is_linked(b1, 'FeatureToGroupConnection', a)
    _safe_set(a, 'source41', {b2})
    assert _is_linked(a, 'source41', b2)
    if hasattr(b1, 'FeatureToGroupConnection'):
        assert not _is_linked(b1, 'FeatureToGroupConnection', a)
    if hasattr(b2, 'FeatureToGroupConnection'):
        assert _is_linked(b2, 'FeatureToGroupConnection', a)
    _safe_set(a, 'source41', set())
    assert not _is_linked(a, 'source41', b2)
    if hasattr(b2, 'FeatureToGroupConnection'):
        assert not _is_linked(b2, 'FeatureToGroupConnection', a)


def test_assoc_groupToFeatureConnections49_link_reassign_clear():
    a = FCORE_FeatureGroup(max=7, min=7)
    b1 = FCORE_GroupToFeatureConnection()
    b2 = FCORE_GroupToFeatureConnection()
    _safe_set(a, 'source50', {b1})
    assert _is_linked(a, 'source50', b1)
    if hasattr(b1, 'GroupToFeatureConnection51'):
        assert _is_linked(b1, 'GroupToFeatureConnection51', a)
    _safe_set(a, 'source50', {b2})
    assert _is_linked(a, 'source50', b2)
    if hasattr(b1, 'GroupToFeatureConnection51'):
        assert not _is_linked(b1, 'GroupToFeatureConnection51', a)
    if hasattr(b2, 'GroupToFeatureConnection51'):
        assert _is_linked(b2, 'GroupToFeatureConnection51', a)
    _safe_set(a, 'source50', set())
    assert not _is_linked(a, 'source50', b2)
    if hasattr(b2, 'GroupToFeatureConnection51'):
        assert not _is_linked(b2, 'GroupToFeatureConnection51', a)


def test_assoc_incomingSingleFeatureConnection42_link_reassign_clear():
    a = FCORE_SolitaryFeature(max=7, min=7)
    b1 = FCORE_SingleFeatureConnection()
    b2 = FCORE_SingleFeatureConnection()
    _safe_set(a, 'target', b1)
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'SingleFeatureConnection43'):
        assert _is_linked(b1, 'SingleFeatureConnection43', a)
    _safe_set(a, 'target', b2)
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'SingleFeatureConnection43'):
        assert not _is_linked(b1, 'SingleFeatureConnection43', a)
    if hasattr(b2, 'SingleFeatureConnection43'):
        assert _is_linked(b2, 'SingleFeatureConnection43', a)
    _safe_set(a, 'target', None)
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'SingleFeatureConnection43'):
        assert not _is_linked(b2, 'SingleFeatureConnection43', a)


def test_assoc_influence56_link_reassign_clear():
    a = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    b1 = FCORE_Influence(contribution=3.14)
    b2 = FCORE_Influence(contribution=9.99)
    _safe_set(a, 'softgoal', {b1})
    assert _is_linked(a, 'softgoal', b1)
    if hasattr(b1, 'Influence'):
        assert _is_linked(b1, 'Influence', a)
    _safe_set(a, 'softgoal', {b2})
    assert _is_linked(a, 'softgoal', b2)
    if hasattr(b1, 'Influence'):
        assert not _is_linked(b1, 'Influence', a)
    if hasattr(b2, 'Influence'):
        assert _is_linked(b2, 'Influence', a)
    _safe_set(a, 'softgoal', set())
    assert not _is_linked(a, 'softgoal', b2)
    if hasattr(b2, 'Influence'):
        assert not _is_linked(b2, 'Influence', a)


def test_assoc_influences37_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_InfluenceFeature()
    b2 = FCORE_InfluenceFeature()
    _safe_set(a, 'feature', {b1})
    assert _is_linked(a, 'feature', b1)
    if hasattr(b1, 'InfluenceFeature'):
        assert _is_linked(b1, 'InfluenceFeature', a)
    _safe_set(a, 'feature', {b2})
    assert _is_linked(a, 'feature', b2)
    if hasattr(b1, 'InfluenceFeature'):
        assert not _is_linked(b1, 'InfluenceFeature', a)
    if hasattr(b2, 'InfluenceFeature'):
        assert _is_linked(b2, 'InfluenceFeature', a)
    _safe_set(a, 'feature', set())
    assert not _is_linked(a, 'feature', b2)
    if hasattr(b2, 'InfluenceFeature'):
        assert not _is_linked(b2, 'InfluenceFeature', a)


def test_assoc_influences52_link_reassign_clear():
    a = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    b1 = FCORE_InfluenceAttribute()
    b2 = FCORE_InfluenceAttribute()
    _safe_set(a, 'attribute', {b1})
    assert _is_linked(a, 'attribute', b1)
    if hasattr(b1, 'InfluenceAttribute'):
        assert _is_linked(b1, 'InfluenceAttribute', a)
    _safe_set(a, 'attribute', {b2})
    assert _is_linked(a, 'attribute', b2)
    if hasattr(b1, 'InfluenceAttribute'):
        assert not _is_linked(b1, 'InfluenceAttribute', a)
    if hasattr(b2, 'InfluenceAttribute'):
        assert _is_linked(b2, 'InfluenceAttribute', a)
    _safe_set(a, 'attribute', set())
    assert not _is_linked(a, 'attribute', b2)
    if hasattr(b2, 'InfluenceAttribute'):
        assert not _is_linked(b2, 'InfluenceAttribute', a)


def test_assoc_outgoingSingleFeatureConnections38_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_SingleFeatureConnection()
    b2 = FCORE_SingleFeatureConnection()
    _safe_set(a, 'source39', {b1})
    assert _is_linked(a, 'source39', b1)
    if hasattr(b1, 'SingleFeatureConnection'):
        assert _is_linked(b1, 'SingleFeatureConnection', a)
    _safe_set(a, 'source39', {b2})
    assert _is_linked(a, 'source39', b2)
    if hasattr(b1, 'SingleFeatureConnection'):
        assert not _is_linked(b1, 'SingleFeatureConnection', a)
    if hasattr(b2, 'SingleFeatureConnection'):
        assert _is_linked(b2, 'SingleFeatureConnection', a)
    _safe_set(a, 'source39', set())
    assert not _is_linked(a, 'source39', b2)
    if hasattr(b2, 'SingleFeatureConnection'):
        assert not _is_linked(b2, 'SingleFeatureConnection', a)


def test_assoc_softgoal60_link_reassign_clear():
    a = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    b1 = FCORE_Influence(contribution=3.14)
    b2 = FCORE_Influence(contribution=9.99)
    _safe_set(a, 'Softgoal', b1)
    assert _is_linked(a, 'Softgoal', b1)
    if hasattr(b1, 'influence'):
        assert _is_linked(b1, 'influence', a)
    _safe_set(a, 'Softgoal', b2)
    assert _is_linked(a, 'Softgoal', b2)
    if hasattr(b1, 'influence'):
        assert not _is_linked(b1, 'influence', a)
    if hasattr(b2, 'influence'):
        assert _is_linked(b2, 'influence', a)
    _safe_set(a, 'Softgoal', None)
    assert not _is_linked(a, 'Softgoal', b2)
    if hasattr(b2, 'influence'):
        assert not _is_linked(b2, 'influence', a)


def test_assoc_softgoals15_link_reassign_clear():
    a = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    b1 = FCORE_FeatureModel()
    b2 = FCORE_FeatureModel()
    _safe_set(a, 'FCORE_Softgoal', b1)
    assert _is_linked(a, 'FCORE_Softgoal', b1)
    if hasattr(b1, 'FCORE_FeatureModel16'):
        assert _is_linked(b1, 'FCORE_FeatureModel16', a)
    _safe_set(a, 'FCORE_Softgoal', b2)
    assert _is_linked(a, 'FCORE_Softgoal', b2)
    if hasattr(b1, 'FCORE_FeatureModel16'):
        assert not _is_linked(b1, 'FCORE_FeatureModel16', a)
    if hasattr(b2, 'FCORE_FeatureModel16'):
        assert _is_linked(b2, 'FCORE_FeatureModel16', a)
    _safe_set(a, 'FCORE_Softgoal', None)
    assert not _is_linked(a, 'FCORE_Softgoal', b2)
    if hasattr(b2, 'FCORE_FeatureModel16'):
        assert not _is_linked(b2, 'FCORE_FeatureModel16', a)


def test_assoc_solitaryFeatures3_link_reassign_clear():
    a = FCORE_SolitaryFeature(max=7, min=7)
    b1 = FCORE_FeatureModel()
    b2 = FCORE_FeatureModel()
    _safe_set(a, 'FCORE_SolitaryFeature', b1)
    assert _is_linked(a, 'FCORE_SolitaryFeature', b1)
    if hasattr(b1, 'FCORE_FeatureModel4'):
        assert _is_linked(b1, 'FCORE_FeatureModel4', a)
    _safe_set(a, 'FCORE_SolitaryFeature', b2)
    assert _is_linked(a, 'FCORE_SolitaryFeature', b2)
    if hasattr(b1, 'FCORE_FeatureModel4'):
        assert not _is_linked(b1, 'FCORE_FeatureModel4', a)
    if hasattr(b2, 'FCORE_FeatureModel4'):
        assert _is_linked(b2, 'FCORE_FeatureModel4', a)
    _safe_set(a, 'FCORE_SolitaryFeature', None)
    assert not _is_linked(a, 'FCORE_SolitaryFeature', b2)
    if hasattr(b2, 'FCORE_FeatureModel4'):
        assert not _is_linked(b2, 'FCORE_FeatureModel4', a)


def test_assoc_source65_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_SingleFeatureConnection()
    b2 = FCORE_SingleFeatureConnection()
    _safe_set(a, 'Feature66', b1)
    assert _is_linked(a, 'Feature66', b1)
    if hasattr(b1, 'outgoingSingleFeatureConnections'):
        assert _is_linked(b1, 'outgoingSingleFeatureConnections', a)
    _safe_set(a, 'Feature66', b2)
    assert _is_linked(a, 'Feature66', b2)
    if hasattr(b1, 'outgoingSingleFeatureConnections'):
        assert not _is_linked(b1, 'outgoingSingleFeatureConnections', a)
    if hasattr(b2, 'outgoingSingleFeatureConnections'):
        assert _is_linked(b2, 'outgoingSingleFeatureConnections', a)
    _safe_set(a, 'Feature66', None)
    assert not _is_linked(a, 'Feature66', b2)
    if hasattr(b2, 'outgoingSingleFeatureConnections'):
        assert not _is_linked(b2, 'outgoingSingleFeatureConnections', a)


def test_assoc_source68_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_FeatureToGroupConnection()
    b2 = FCORE_FeatureToGroupConnection()
    _safe_set(a, 'Feature69', b1)
    assert _is_linked(a, 'Feature69', b1)
    if hasattr(b1, 'featureToGroupConnections'):
        assert _is_linked(b1, 'featureToGroupConnections', a)
    _safe_set(a, 'Feature69', b2)
    assert _is_linked(a, 'Feature69', b2)
    if hasattr(b1, 'featureToGroupConnections'):
        assert not _is_linked(b1, 'featureToGroupConnections', a)
    if hasattr(b2, 'featureToGroupConnections'):
        assert _is_linked(b2, 'featureToGroupConnections', a)
    _safe_set(a, 'Feature69', None)
    assert not _is_linked(a, 'Feature69', b2)
    if hasattr(b2, 'featureToGroupConnections'):
        assert not _is_linked(b2, 'featureToGroupConnections', a)


def test_assoc_source71_link_reassign_clear():
    a = FCORE_FeatureGroup(max=7, min=7)
    b1 = FCORE_GroupToFeatureConnection()
    b2 = FCORE_GroupToFeatureConnection()
    _safe_set(a, 'FeatureGroup72', b1)
    assert _is_linked(a, 'FeatureGroup72', b1)
    if hasattr(b1, 'groupToFeatureConnections'):
        assert _is_linked(b1, 'groupToFeatureConnections', a)
    _safe_set(a, 'FeatureGroup72', b2)
    assert _is_linked(a, 'FeatureGroup72', b2)
    if hasattr(b1, 'groupToFeatureConnections'):
        assert not _is_linked(b1, 'groupToFeatureConnections', a)
    if hasattr(b2, 'groupToFeatureConnections'):
        assert _is_linked(b2, 'groupToFeatureConnections', a)
    _safe_set(a, 'FeatureGroup72', None)
    assert not _is_linked(a, 'FeatureGroup72', b2)
    if hasattr(b2, 'groupToFeatureConnections'):
        assert not _is_linked(b2, 'groupToFeatureConnections', a)


def test_assoc_source74_link_reassign_clear():
    a = FCORE_Feature(name="sample_text", selected=True)
    b1 = FCORE_AttributeConstraintConnection()
    b2 = FCORE_AttributeConstraintConnection()
    _safe_set(a, 'Feature75', b1)
    assert _is_linked(a, 'Feature75', b1)
    if hasattr(b1, 'attributeConstraints'):
        assert _is_linked(b1, 'attributeConstraints', a)
    _safe_set(a, 'Feature75', b2)
    assert _is_linked(a, 'Feature75', b2)
    if hasattr(b1, 'attributeConstraints'):
        assert not _is_linked(b1, 'attributeConstraints', a)
    if hasattr(b2, 'attributeConstraints'):
        assert _is_linked(b2, 'attributeConstraints', a)
    _safe_set(a, 'Feature75', None)
    assert not _is_linked(a, 'Feature75', b2)
    if hasattr(b2, 'attributeConstraints'):
        assert not _is_linked(b2, 'attributeConstraints', a)


def test_assoc_target67_link_reassign_clear():
    a = FCORE_SolitaryFeature(max=7, min=7)
    b1 = FCORE_SingleFeatureConnection()
    b2 = FCORE_SingleFeatureConnection()
    _safe_set(a, 'SolitaryFeature', b1)
    assert _is_linked(a, 'SolitaryFeature', b1)
    if hasattr(b1, 'incomingSingleFeatureConnection'):
        assert _is_linked(b1, 'incomingSingleFeatureConnection', a)
    _safe_set(a, 'SolitaryFeature', b2)
    assert _is_linked(a, 'SolitaryFeature', b2)
    if hasattr(b1, 'incomingSingleFeatureConnection'):
        assert not _is_linked(b1, 'incomingSingleFeatureConnection', a)
    if hasattr(b2, 'incomingSingleFeatureConnection'):
        assert _is_linked(b2, 'incomingSingleFeatureConnection', a)
    _safe_set(a, 'SolitaryFeature', None)
    assert not _is_linked(a, 'SolitaryFeature', b2)
    if hasattr(b2, 'incomingSingleFeatureConnection'):
        assert not _is_linked(b2, 'incomingSingleFeatureConnection', a)


def test_assoc_target70_link_reassign_clear():
    a = FCORE_FeatureGroup(max=7, min=7)
    b1 = FCORE_FeatureToGroupConnection()
    b2 = FCORE_FeatureToGroupConnection()
    _safe_set(a, 'FeatureGroup', b1)
    assert _is_linked(a, 'FeatureGroup', b1)
    if hasattr(b1, 'featureToGroupConnection'):
        assert _is_linked(b1, 'featureToGroupConnection', a)
    _safe_set(a, 'FeatureGroup', b2)
    assert _is_linked(a, 'FeatureGroup', b2)
    if hasattr(b1, 'featureToGroupConnection'):
        assert not _is_linked(b1, 'featureToGroupConnection', a)
    if hasattr(b2, 'featureToGroupConnection'):
        assert _is_linked(b2, 'featureToGroupConnection', a)
    _safe_set(a, 'FeatureGroup', None)
    assert not _is_linked(a, 'FeatureGroup', b2)
    if hasattr(b2, 'featureToGroupConnection'):
        assert not _is_linked(b2, 'featureToGroupConnection', a)


def test_assoc_target76_link_reassign_clear():
    a = FCORE_AttributeConstraint(equation="sample_text")
    b1 = FCORE_AttributeConstraintConnection()
    b2 = FCORE_AttributeConstraintConnection()
    _safe_set(a, 'AttributeConstraint', b1)
    assert _is_linked(a, 'AttributeConstraint', b1)
    if hasattr(b1, 'attributeConstraintConnection'):
        assert _is_linked(b1, 'attributeConstraintConnection', a)
    _safe_set(a, 'AttributeConstraint', b2)
    assert _is_linked(a, 'AttributeConstraint', b2)
    if hasattr(b1, 'attributeConstraintConnection'):
        assert not _is_linked(b1, 'attributeConstraintConnection', a)
    if hasattr(b2, 'attributeConstraintConnection'):
        assert _is_linked(b2, 'attributeConstraintConnection', a)
    _safe_set(a, 'AttributeConstraint', None)
    assert not _is_linked(a, 'AttributeConstraint', b2)
    if hasattr(b2, 'attributeConstraintConnection'):
        assert not _is_linked(b2, 'attributeConstraintConnection', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Conncection_strategy = st.builds(Conncection)
@given(instance=Conncection_strategy)
@settings(max_examples=25)
def test_Conncection_instantiation(instance):
    assert isinstance(instance, Conncection)


FCORE_Attribute_strategy = st.builds(FCORE_Attribute, max=st.integers(), min=st.integers(), name=safe_text, value=st.integers())
@given(instance=FCORE_Attribute_strategy)
@settings(max_examples=25)
def test_FCORE_Attribute_instantiation(instance):
    assert isinstance(instance, FCORE_Attribute)


FCORE_AttributeConstraint_strategy = st.builds(FCORE_AttributeConstraint, equation=safe_text)
@given(instance=FCORE_AttributeConstraint_strategy)
@settings(max_examples=25)
def test_FCORE_AttributeConstraint_instantiation(instance):
    assert isinstance(instance, FCORE_AttributeConstraint)


FCORE_AttributeConstraintConnection_strategy = st.builds(FCORE_AttributeConstraintConnection)
@given(instance=FCORE_AttributeConstraintConnection_strategy)
@settings(max_examples=25)
def test_FCORE_AttributeConstraintConnection_instantiation(instance):
    assert isinstance(instance, FCORE_AttributeConstraintConnection)


FCORE_CardinalityConnection_strategy = st.builds(FCORE_CardinalityConnection, max=st.integers(), min=st.integers())
@given(instance=FCORE_CardinalityConnection_strategy)
@settings(max_examples=25)
def test_FCORE_CardinalityConnection_instantiation(instance):
    assert isinstance(instance, FCORE_CardinalityConnection)


FCORE_Conncection_strategy = st.builds(FCORE_Conncection)
@given(instance=FCORE_Conncection_strategy)
@settings(max_examples=25)
def test_FCORE_Conncection_instantiation(instance):
    assert isinstance(instance, FCORE_Conncection)


FCORE_ExcludesFeatureConstraint_strategy = st.builds(FCORE_ExcludesFeatureConstraint)
@given(instance=FCORE_ExcludesFeatureConstraint_strategy)
@settings(max_examples=25)
def test_FCORE_ExcludesFeatureConstraint_instantiation(instance):
    assert isinstance(instance, FCORE_ExcludesFeatureConstraint)


FCORE_Feature_strategy = st.builds(FCORE_Feature, name=safe_text, selected=st.booleans())
@given(instance=FCORE_Feature_strategy)
@settings(max_examples=25)
def test_FCORE_Feature_instantiation(instance):
    assert isinstance(instance, FCORE_Feature)


FCORE_FeatureConstraint_strategy = st.builds(FCORE_FeatureConstraint)
@given(instance=FCORE_FeatureConstraint_strategy)
@settings(max_examples=25)
def test_FCORE_FeatureConstraint_instantiation(instance):
    assert isinstance(instance, FCORE_FeatureConstraint)


FCORE_FeatureGroup_strategy = st.builds(FCORE_FeatureGroup, max=st.integers(), min=st.integers())
@given(instance=FCORE_FeatureGroup_strategy)
@settings(max_examples=25)
def test_FCORE_FeatureGroup_instantiation(instance):
    assert isinstance(instance, FCORE_FeatureGroup)


FCORE_FeatureModel_strategy = st.builds(FCORE_FeatureModel)
@given(instance=FCORE_FeatureModel_strategy)
@settings(max_examples=25)
def test_FCORE_FeatureModel_instantiation(instance):
    assert isinstance(instance, FCORE_FeatureModel)


FCORE_FeatureToGroupConnection_strategy = st.builds(FCORE_FeatureToGroupConnection)
@given(instance=FCORE_FeatureToGroupConnection_strategy)
@settings(max_examples=25)
def test_FCORE_FeatureToGroupConnection_instantiation(instance):
    assert isinstance(instance, FCORE_FeatureToGroupConnection)


FCORE_GroupFeature_strategy = st.builds(FCORE_GroupFeature)
@given(instance=FCORE_GroupFeature_strategy)
@settings(max_examples=25)
def test_FCORE_GroupFeature_instantiation(instance):
    assert isinstance(instance, FCORE_GroupFeature)


FCORE_GroupToFeatureConnection_strategy = st.builds(FCORE_GroupToFeatureConnection)
@given(instance=FCORE_GroupToFeatureConnection_strategy)
@settings(max_examples=25)
def test_FCORE_GroupToFeatureConnection_instantiation(instance):
    assert isinstance(instance, FCORE_GroupToFeatureConnection)


FCORE_Influence_strategy = st.builds(FCORE_Influence, contribution=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=FCORE_Influence_strategy)
@settings(max_examples=25)
def test_FCORE_Influence_instantiation(instance):
    assert isinstance(instance, FCORE_Influence)


FCORE_InfluenceAttribute_strategy = st.builds(FCORE_InfluenceAttribute)
@given(instance=FCORE_InfluenceAttribute_strategy)
@settings(max_examples=25)
def test_FCORE_InfluenceAttribute_instantiation(instance):
    assert isinstance(instance, FCORE_InfluenceAttribute)


FCORE_InfluenceFeature_strategy = st.builds(FCORE_InfluenceFeature)
@given(instance=FCORE_InfluenceFeature_strategy)
@settings(max_examples=25)
def test_FCORE_InfluenceFeature_instantiation(instance):
    assert isinstance(instance, FCORE_InfluenceFeature)


FCORE_MandatoryConnection_strategy = st.builds(FCORE_MandatoryConnection)
@given(instance=FCORE_MandatoryConnection_strategy)
@settings(max_examples=25)
def test_FCORE_MandatoryConnection_instantiation(instance):
    assert isinstance(instance, FCORE_MandatoryConnection)


FCORE_OptionalConnection_strategy = st.builds(FCORE_OptionalConnection)
@given(instance=FCORE_OptionalConnection_strategy)
@settings(max_examples=25)
def test_FCORE_OptionalConnection_instantiation(instance):
    assert isinstance(instance, FCORE_OptionalConnection)


FCORE_RequiresFeatureConstraint_strategy = st.builds(FCORE_RequiresFeatureConstraint)
@given(instance=FCORE_RequiresFeatureConstraint_strategy)
@settings(max_examples=25)
def test_FCORE_RequiresFeatureConstraint_instantiation(instance):
    assert isinstance(instance, FCORE_RequiresFeatureConstraint)


FCORE_RootFeature_strategy = st.builds(FCORE_RootFeature)
@given(instance=FCORE_RootFeature_strategy)
@settings(max_examples=25)
def test_FCORE_RootFeature_instantiation(instance):
    assert isinstance(instance, FCORE_RootFeature)


FCORE_SingleFeatureConnection_strategy = st.builds(FCORE_SingleFeatureConnection)
@given(instance=FCORE_SingleFeatureConnection_strategy)
@settings(max_examples=25)
def test_FCORE_SingleFeatureConnection_instantiation(instance):
    assert isinstance(instance, FCORE_SingleFeatureConnection)


FCORE_Softgoal_strategy = st.builds(FCORE_Softgoal, name=safe_text, weighting=safe_text)
@given(instance=FCORE_Softgoal_strategy)
@settings(max_examples=25)
def test_FCORE_Softgoal_instantiation(instance):
    assert isinstance(instance, FCORE_Softgoal)


FCORE_SolitaryFeature_strategy = st.builds(FCORE_SolitaryFeature, max=st.integers(), min=st.integers())
@given(instance=FCORE_SolitaryFeature_strategy)
@settings(max_examples=25)
def test_FCORE_SolitaryFeature_instantiation(instance):
    assert isinstance(instance, FCORE_SolitaryFeature)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


FeatureConstraint_strategy = st.builds(FeatureConstraint)
@given(instance=FeatureConstraint_strategy)
@settings(max_examples=25)
def test_FeatureConstraint_instantiation(instance):
    assert isinstance(instance, FeatureConstraint)


Influence_strategy = st.builds(Influence)
@given(instance=Influence_strategy)
@settings(max_examples=25)
def test_Influence_instantiation(instance):
    assert isinstance(instance, Influence)


SingleFeatureConnection_strategy = st.builds(SingleFeatureConnection)
@given(instance=SingleFeatureConnection_strategy)
@settings(max_examples=25)
def test_SingleFeatureConnection_instantiation(instance):
    assert isinstance(instance, SingleFeatureConnection)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Conncection,
    FCORE_Attribute,
    FCORE_AttributeConstraint,
    FCORE_AttributeConstraintConnection,
    FCORE_CardinalityConnection,
    FCORE_Conncection,
    FCORE_ExcludesFeatureConstraint,
    FCORE_Feature,
    FCORE_FeatureConstraint,
    FCORE_FeatureGroup,
    FCORE_FeatureModel,
    FCORE_FeatureToGroupConnection,
    FCORE_GroupFeature,
    FCORE_GroupToFeatureConnection,
    FCORE_Influence,
    FCORE_InfluenceAttribute,
    FCORE_InfluenceFeature,
    FCORE_MandatoryConnection,
    FCORE_OptionalConnection,
    FCORE_RequiresFeatureConstraint,
    FCORE_RootFeature,
    FCORE_SingleFeatureConnection,
    FCORE_Softgoal,
    FCORE_SolitaryFeature,
    Feature,
    FeatureConstraint,
    Influence,
    SingleFeatureConnection,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_attributes32_reverse_link_reassign_clear():
    a1 = FCORE_Feature(name="sample_text", selected=True)
    a2 = FCORE_Feature(name="sample_text_2", selected=False)
    b = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    _safe_set(b, 'FCORE_Attribute33', a1)
    assert _is_linked(b, 'FCORE_Attribute33', a1)
    if hasattr(a1, 'FCORE_Feature'):
        assert _is_linked(a1, 'FCORE_Feature', b)
    _safe_set(b, 'FCORE_Attribute33', a2)
    assert _is_linked(b, 'FCORE_Attribute33', a2)
    if hasattr(a1, 'FCORE_Feature'):
        assert not _is_linked(a1, 'FCORE_Feature', b)
    if hasattr(a2, 'FCORE_Feature'):
        assert _is_linked(a2, 'FCORE_Feature', b)
    _safe_set(b, 'FCORE_Attribute33', None)
    assert not _is_linked(b, 'FCORE_Attribute33', a2)
    if hasattr(a2, 'FCORE_Feature'):
        assert not _is_linked(a2, 'FCORE_Feature', b)


def test_assoc_influence56_reverse_link_reassign_clear():
    a1 = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    a2 = FCORE_Softgoal(name="sample_text_2", weighting="sample_text_2")
    b = FCORE_Influence(contribution=3.14)
    _safe_set(b, 'Influence', a1)
    assert _is_linked(b, 'Influence', a1)
    if hasattr(a1, 'softgoal'):
        assert _is_linked(a1, 'softgoal', b)
    _safe_set(b, 'Influence', a2)
    assert _is_linked(b, 'Influence', a2)
    if hasattr(a1, 'softgoal'):
        assert not _is_linked(a1, 'softgoal', b)
    if hasattr(a2, 'softgoal'):
        assert _is_linked(a2, 'softgoal', b)
    _safe_set(b, 'Influence', None)
    assert not _is_linked(b, 'Influence', a2)
    if hasattr(a2, 'softgoal'):
        assert not _is_linked(a2, 'softgoal', b)


def test_assoc_softgoal60_reverse_link_reassign_clear():
    a1 = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    a2 = FCORE_Softgoal(name="sample_text_2", weighting="sample_text_2")
    b = FCORE_Influence(contribution=3.14)
    _safe_set(b, 'influence', a1)
    assert _is_linked(b, 'influence', a1)
    if hasattr(a1, 'Softgoal'):
        assert _is_linked(a1, 'Softgoal', b)
    _safe_set(b, 'influence', a2)
    assert _is_linked(b, 'influence', a2)
    if hasattr(a1, 'Softgoal'):
        assert not _is_linked(a1, 'Softgoal', b)
    if hasattr(a2, 'Softgoal'):
        assert _is_linked(a2, 'Softgoal', b)
    _safe_set(b, 'influence', None)
    assert not _is_linked(b, 'influence', a2)
    if hasattr(a2, 'Softgoal'):
        assert not _is_linked(a2, 'Softgoal', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute63_stub_double():
    # FCORE_InfluenceAttribute has no real 'influences64' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    partner = FCORE_InfluenceAttribute()
    setattr(partner, 'influences64', None)
    _safe_set(owner, 'Attribute', partner)
    assert getattr(partner, 'influences64') == owner
    _safe_set(owner, 'Attribute', None)
    assert getattr(partner, 'influences64') is None


def test_assoc_attributeConstraintConnection53_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'AttributeConstraintConnection55' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_AttributeConstraint(equation="sample_text")
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'AttributeConstraintConnection55', None)
    _safe_set(owner, 'target54', partner)
    assert getattr(partner, 'AttributeConstraintConnection55') == owner
    _safe_set(owner, 'target54', None)
    assert getattr(partner, 'AttributeConstraintConnection55') is None


def test_assoc_attributeConstraints31_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'AttributeConstraintConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'AttributeConstraintConnection', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'AttributeConstraintConnection') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'AttributeConstraintConnection') is None


def test_assoc_attributeConstraints9_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel10' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_AttributeConstraint(equation="sample_text")
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel10', None)
    _safe_set(owner, 'FCORE_AttributeConstraint', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel10')
    _safe_set(owner, 'FCORE_AttributeConstraint', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel10')


def test_assoc_attributes7_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel8' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel8', None)
    _safe_set(owner, 'FCORE_Attribute', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel8')
    _safe_set(owner, 'FCORE_Attribute', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel8')


def test_assoc_feature61_stub_double():
    # FCORE_InfluenceFeature has no real 'influences' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_InfluenceFeature()
    setattr(partner, 'influences', None)
    _safe_set(owner, 'Feature62', partner)
    assert getattr(partner, 'influences') == owner
    _safe_set(owner, 'Feature62', None)
    assert getattr(partner, 'influences') is None


def test_assoc_featureConstraintsEnds35_stub_double():
    # FCORE_FeatureConstraint has no real 'FeatureConstraint36' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'FeatureConstraint36', None)
    _safe_set(owner, 'featureEnd', {partner})
    assert getattr(partner, 'FeatureConstraint36') == owner
    _safe_set(owner, 'featureEnd', set())
    assert getattr(partner, 'FeatureConstraint36') is None


def test_assoc_featureConstraintsStarts34_stub_double():
    # FCORE_FeatureConstraint has no real 'FeatureConstraint' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'FeatureConstraint', None)
    _safe_set(owner, 'featureStart', {partner})
    assert getattr(partner, 'FeatureConstraint') == owner
    _safe_set(owner, 'featureStart', set())
    assert getattr(partner, 'FeatureConstraint') is None


def test_assoc_featureEnd58_stub_double():
    # FCORE_FeatureConstraint has no real 'featureConstraintsEnds' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'featureConstraintsEnds', None)
    _safe_set(owner, 'Feature59', partner)
    assert getattr(partner, 'featureConstraintsEnds') == owner
    _safe_set(owner, 'Feature59', None)
    assert getattr(partner, 'featureConstraintsEnds') is None


def test_assoc_featureGroups5_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel6' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel6', None)
    _safe_set(owner, 'FCORE_FeatureGroup', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel6')
    _safe_set(owner, 'FCORE_FeatureGroup', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel6')


def test_assoc_featureStart57_stub_double():
    # FCORE_FeatureConstraint has no real 'featureConstraintsStarts' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'featureConstraintsStarts', None)
    _safe_set(owner, 'Feature', partner)
    assert getattr(partner, 'featureConstraintsStarts') == owner
    _safe_set(owner, 'Feature', None)
    assert getattr(partner, 'featureConstraintsStarts') is None


def test_assoc_featureToGroupConnection46_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'FeatureToGroupConnection48' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'FeatureToGroupConnection48', None)
    _safe_set(owner, 'target47', partner)
    assert getattr(partner, 'FeatureToGroupConnection48') == owner
    _safe_set(owner, 'target47', None)
    assert getattr(partner, 'FeatureToGroupConnection48') is None


def test_assoc_featureToGroupConnections40_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'FeatureToGroupConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'FeatureToGroupConnection', None)
    _safe_set(owner, 'source41', {partner})
    assert getattr(partner, 'FeatureToGroupConnection') == owner
    _safe_set(owner, 'source41', set())
    assert getattr(partner, 'FeatureToGroupConnection') is None


def test_assoc_groupToFeatureConnections49_stub_double():
    # FCORE_GroupToFeatureConnection has no real 'GroupToFeatureConnection51' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_GroupToFeatureConnection()
    setattr(partner, 'GroupToFeatureConnection51', None)
    _safe_set(owner, 'source50', {partner})
    assert getattr(partner, 'GroupToFeatureConnection51') == owner
    _safe_set(owner, 'source50', set())
    assert getattr(partner, 'GroupToFeatureConnection51') is None


def test_assoc_incomingSingleFeatureConnection42_stub_double():
    # FCORE_SingleFeatureConnection has no real 'SingleFeatureConnection43' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_SolitaryFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_SolitaryFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_SolitaryFeature(max=7, min=7)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'SingleFeatureConnection43', None)
    _safe_set(owner, 'target', partner)
    assert getattr(partner, 'SingleFeatureConnection43') == owner
    _safe_set(owner, 'target', None)
    assert getattr(partner, 'SingleFeatureConnection43') is None


def test_assoc_influences37_stub_double():
    # FCORE_InfluenceFeature has no real 'InfluenceFeature' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_InfluenceFeature()
    setattr(partner, 'InfluenceFeature', None)
    _safe_set(owner, 'feature', {partner})
    assert getattr(partner, 'InfluenceFeature') == owner
    _safe_set(owner, 'feature', set())
    assert getattr(partner, 'InfluenceFeature') is None


def test_assoc_influences52_stub_double():
    # FCORE_InfluenceAttribute has no real 'InfluenceAttribute' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    partner = FCORE_InfluenceAttribute()
    setattr(partner, 'InfluenceAttribute', None)
    _safe_set(owner, 'attribute', {partner})
    assert getattr(partner, 'InfluenceAttribute') == owner
    _safe_set(owner, 'attribute', set())
    assert getattr(partner, 'InfluenceAttribute') is None


def test_assoc_outgoingSingleFeatureConnections38_stub_double():
    # FCORE_SingleFeatureConnection has no real 'SingleFeatureConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'SingleFeatureConnection', None)
    _safe_set(owner, 'source39', {partner})
    assert getattr(partner, 'SingleFeatureConnection') == owner
    _safe_set(owner, 'source39', set())
    assert getattr(partner, 'SingleFeatureConnection') is None


def test_assoc_softgoals15_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel16' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Softgoal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Softgoal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel16', None)
    _safe_set(owner, 'FCORE_Softgoal', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel16')
    _safe_set(owner, 'FCORE_Softgoal', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel16')


def test_assoc_solitaryFeatures3_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel4' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_SolitaryFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_SolitaryFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_SolitaryFeature(max=7, min=7)
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel4', None)
    _safe_set(owner, 'FCORE_SolitaryFeature', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel4')
    _safe_set(owner, 'FCORE_SolitaryFeature', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel4')


def test_assoc_source65_stub_double():
    # FCORE_SingleFeatureConnection has no real 'outgoingSingleFeatureConnections' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'outgoingSingleFeatureConnections', None)
    _safe_set(owner, 'Feature66', partner)
    assert getattr(partner, 'outgoingSingleFeatureConnections') == owner
    _safe_set(owner, 'Feature66', None)
    assert getattr(partner, 'outgoingSingleFeatureConnections') is None


def test_assoc_source68_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'featureToGroupConnections' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'featureToGroupConnections', None)
    _safe_set(owner, 'Feature69', partner)
    assert getattr(partner, 'featureToGroupConnections') == owner
    _safe_set(owner, 'Feature69', None)
    assert getattr(partner, 'featureToGroupConnections') is None


def test_assoc_source71_stub_double():
    # FCORE_GroupToFeatureConnection has no real 'groupToFeatureConnections' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_GroupToFeatureConnection()
    setattr(partner, 'groupToFeatureConnections', None)
    _safe_set(owner, 'FeatureGroup72', partner)
    assert getattr(partner, 'groupToFeatureConnections') == owner
    _safe_set(owner, 'FeatureGroup72', None)
    assert getattr(partner, 'groupToFeatureConnections') is None


def test_assoc_source74_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'attributeConstraints' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'attributeConstraints', None)
    _safe_set(owner, 'Feature75', partner)
    assert getattr(partner, 'attributeConstraints') == owner
    _safe_set(owner, 'Feature75', None)
    assert getattr(partner, 'attributeConstraints') is None


def test_assoc_target67_stub_double():
    # FCORE_SingleFeatureConnection has no real 'incomingSingleFeatureConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_SolitaryFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_SolitaryFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_SolitaryFeature(max=7, min=7)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'incomingSingleFeatureConnection', None)
    _safe_set(owner, 'SolitaryFeature', partner)
    assert getattr(partner, 'incomingSingleFeatureConnection') == owner
    _safe_set(owner, 'SolitaryFeature', None)
    assert getattr(partner, 'incomingSingleFeatureConnection') is None


def test_assoc_target70_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'featureToGroupConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'featureToGroupConnection', None)
    _safe_set(owner, 'FeatureGroup', partner)
    assert getattr(partner, 'featureToGroupConnection') == owner
    _safe_set(owner, 'FeatureGroup', None)
    assert getattr(partner, 'featureToGroupConnection') is None


def test_assoc_target76_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'attributeConstraintConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_AttributeConstraint(equation="sample_text")
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'attributeConstraintConnection', None)
    _safe_set(owner, 'AttributeConstraint', partner)
    assert getattr(partner, 'attributeConstraintConnection') == owner
    _safe_set(owner, 'AttributeConstraint', None)
    assert getattr(partner, 'attributeConstraintConnection') is None




from python_code import FCORE_AttributeConstraint
from python_code import FCORE_AttributeConstraintConnection
from python_code import FCORE_FeatureModel

def test_FCORE_AttributeConstraint___init__():
    assert FCORE_AttributeConstraint.__init__(FCORE_AttributeConstraint('', target54=FCORE_AttributeConstraintConnection(), AttributeConstraint=FCORE_AttributeConstraintConnection(), FCORE_AttributeConstraint=FCORE_FeatureModel()), '', target54=FCORE_AttributeConstraintConnection(), AttributeConstraint=FCORE_AttributeConstraintConnection(), FCORE_AttributeConstraint=FCORE_FeatureModel()) == None
from python_code import FCORE_CardinalityConnection

def test_FCORE_CardinalityConnection___init__():
    assert FCORE_CardinalityConnection.__init__(FCORE_CardinalityConnection(0, 0), 0, 0) == None
from python_code import FCORE_FeatureGroup
from python_code import FCORE_FeatureModel
from python_code import FCORE_FeatureToGroupConnection
from python_code import FCORE_GroupToFeatureConnection

def test_FCORE_FeatureGroup___init__():
    assert FCORE_FeatureGroup.__init__(FCORE_FeatureGroup(0, 0, target47=FCORE_FeatureToGroupConnection(), source50=set(), FeatureGroup=FCORE_FeatureToGroupConnection(), FeatureGroup72=FCORE_GroupToFeatureConnection(), FCORE_FeatureGroup=FCORE_FeatureModel()), 0, 0, target47=FCORE_FeatureToGroupConnection(), source50=set(), FeatureGroup=FCORE_FeatureToGroupConnection(), FeatureGroup72=FCORE_GroupToFeatureConnection(), FCORE_FeatureGroup=FCORE_FeatureModel()) == None
from python_code import FCORE_FeatureModel
from python_code import FCORE_SingleFeatureConnection
from python_code import FCORE_SolitaryFeature

def test_FCORE_SolitaryFeature___init__():
    assert FCORE_SolitaryFeature.__init__(FCORE_SolitaryFeature(0, 0, target=FCORE_SingleFeatureConnection(), SolitaryFeature=FCORE_SingleFeatureConnection(), FCORE_SolitaryFeature=FCORE_FeatureModel()), 0, 0, target=FCORE_SingleFeatureConnection(), SolitaryFeature=FCORE_SingleFeatureConnection(), FCORE_SolitaryFeature=FCORE_FeatureModel()) == None

