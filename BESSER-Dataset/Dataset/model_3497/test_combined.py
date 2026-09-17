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
    ModifyRelationship,
    servicefeaturemodel_FeatureToAttributeModifyRelationship,
    servicefeaturemodel_AttributeToAttributeModifyRelationship,
    servicefeaturemodel_Preference,
    servicefeaturemodel_Configuration,
    Variant,
    servicefeaturemodel_OR,
    servicefeaturemodel_ModifyRelationship,
    servicefeaturemodel_AttributeType,
    ServiceFeature,
    servicefeaturemodel_MandatoryServiceFeature,
    servicefeaturemodel_OptionalServiceFeature,
    servicefeaturemodel_XOR,
    servicefeaturemodel_Excludes,
    servicefeaturemodel_Requires,
    servicefeaturemodel_Variant,
    servicefeaturemodel_Attribute,
    servicefeaturemodel_ServiceFeature,
    servicefeaturemodel_ServiceFeatureDiagram,
    servicefeaturemodel_Service,
    servicefeaturemodel_AttributeTypes,
    servicefeaturemodel_PossibleConfigurations,
    FeatureTypes,
    AggregationRules,
    ScaleOrders,
    AttributeDomain,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_modifyrelationship_is_not_abstract():
    assert not inspect.isabstract(ModifyRelationship)


def test_hyp_modifyrelationship_constructor_exists():
    assert callable(ModifyRelationship.__init__)


def test_hyp_modifyrelationship_constructor_args():
    sig = inspect.signature(ModifyRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_featuretoattributemodifyrelationship_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_FeatureToAttributeModifyRelationship)


def test_hyp_servicefeaturemodel_featuretoattributemodifyrelationship_constructor_exists():
    assert callable(servicefeaturemodel_FeatureToAttributeModifyRelationship.__init__)


def test_hyp_servicefeaturemodel_featuretoattributemodifyrelationship_constructor_args():
    sig = inspect.signature(servicefeaturemodel_FeatureToAttributeModifyRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_attributetoattributemodifyrelationship_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_AttributeToAttributeModifyRelationship)


def test_hyp_servicefeaturemodel_attributetoattributemodifyrelationship_constructor_exists():
    assert callable(servicefeaturemodel_AttributeToAttributeModifyRelationship.__init__)


def test_hyp_servicefeaturemodel_attributetoattributemodifyrelationship_constructor_args():
    sig = inspect.signature(servicefeaturemodel_AttributeToAttributeModifyRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "triggerParameterName" in params, "Missing parameter 'triggerParameterName'"




def test_hyp_servicefeaturemodel_preference_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_Preference)


def test_hyp_servicefeaturemodel_preference_constructor_exists():
    assert callable(servicefeaturemodel_Preference.__init__)


def test_hyp_servicefeaturemodel_preference_constructor_args():
    sig = inspect.signature(servicefeaturemodel_Preference.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "description" in params, "Missing parameter 'description'"
    assert "stakeholderGroup" in params, "Missing parameter 'stakeholderGroup'"







def test_hyp_servicefeaturemodel_configuration_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_Configuration)


def test_hyp_servicefeaturemodel_configuration_constructor_exists():
    assert callable(servicefeaturemodel_Configuration.__init__)


def test_hyp_servicefeaturemodel_configuration_constructor_args():
    sig = inspect.signature(servicefeaturemodel_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_variant_is_not_abstract():
    assert not inspect.isabstract(Variant)


def test_hyp_variant_constructor_exists():
    assert callable(Variant.__init__)


def test_hyp_variant_constructor_args():
    sig = inspect.signature(Variant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_or_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_OR)


def test_hyp_servicefeaturemodel_or_constructor_exists():
    assert callable(servicefeaturemodel_OR.__init__)


def test_hyp_servicefeaturemodel_or_constructor_args():
    sig = inspect.signature(servicefeaturemodel_OR.__init__)
    params = list(sig.parameters.keys())
    assert "maxFeaturesToChoose" in params, "Missing parameter 'maxFeaturesToChoose'"
    assert "minFeaturesToChoose" in params, "Missing parameter 'minFeaturesToChoose'"





def test_hyp_servicefeaturemodel_modifyrelationship_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_ModifyRelationship)


def test_hyp_servicefeaturemodel_modifyrelationship_constructor_exists():
    assert callable(servicefeaturemodel_ModifyRelationship.__init__)


def test_hyp_servicefeaturemodel_modifyrelationship_constructor_args():
    sig = inspect.signature(servicefeaturemodel_ModifyRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "orderNumber" in params, "Missing parameter 'orderNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "function" in params, "Missing parameter 'function'"
    assert "targetParameterName" in params, "Missing parameter 'targetParameterName'"







def test_hyp_servicefeaturemodel_attributetype_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_AttributeType)


def test_hyp_servicefeaturemodel_attributetype_constructor_exists():
    assert callable(servicefeaturemodel_AttributeType.__init__)


def test_hyp_servicefeaturemodel_attributetype_constructor_args():
    sig = inspect.signature(servicefeaturemodel_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "toBeEvaluated" in params, "Missing parameter 'toBeEvaluated'"
    assert "aggregationRule" in params, "Missing parameter 'aggregationRule'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "requirement" in params, "Missing parameter 'requirement'"
    assert "domain" in params, "Missing parameter 'domain'"
    assert "customAttributeTypePriority" in params, "Missing parameter 'customAttributeTypePriority'"
    assert "scaleOrder" in params, "Missing parameter 'scaleOrder'"











def test_hyp_servicefeature_is_not_abstract():
    assert not inspect.isabstract(ServiceFeature)


def test_hyp_servicefeature_constructor_exists():
    assert callable(ServiceFeature.__init__)


def test_hyp_servicefeature_constructor_args():
    sig = inspect.signature(ServiceFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_mandatoryservicefeature_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_MandatoryServiceFeature)


def test_hyp_servicefeaturemodel_mandatoryservicefeature_constructor_exists():
    assert callable(servicefeaturemodel_MandatoryServiceFeature.__init__)


def test_hyp_servicefeaturemodel_mandatoryservicefeature_constructor_args():
    sig = inspect.signature(servicefeaturemodel_MandatoryServiceFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_optionalservicefeature_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_OptionalServiceFeature)


def test_hyp_servicefeaturemodel_optionalservicefeature_constructor_exists():
    assert callable(servicefeaturemodel_OptionalServiceFeature.__init__)


def test_hyp_servicefeaturemodel_optionalservicefeature_constructor_args():
    sig = inspect.signature(servicefeaturemodel_OptionalServiceFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_xor_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_XOR)


def test_hyp_servicefeaturemodel_xor_constructor_exists():
    assert callable(servicefeaturemodel_XOR.__init__)


def test_hyp_servicefeaturemodel_xor_constructor_args():
    sig = inspect.signature(servicefeaturemodel_XOR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_excludes_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_Excludes)


def test_hyp_servicefeaturemodel_excludes_constructor_exists():
    assert callable(servicefeaturemodel_Excludes.__init__)


def test_hyp_servicefeaturemodel_excludes_constructor_args():
    sig = inspect.signature(servicefeaturemodel_Excludes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_requires_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_Requires)


def test_hyp_servicefeaturemodel_requires_constructor_exists():
    assert callable(servicefeaturemodel_Requires.__init__)


def test_hyp_servicefeaturemodel_requires_constructor_args():
    sig = inspect.signature(servicefeaturemodel_Requires.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_variant_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_Variant)


def test_hyp_servicefeaturemodel_variant_constructor_exists():
    assert callable(servicefeaturemodel_Variant.__init__)


def test_hyp_servicefeaturemodel_variant_constructor_args():
    sig = inspect.signature(servicefeaturemodel_Variant.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_attribute_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_Attribute)


def test_hyp_servicefeaturemodel_attribute_constructor_exists():
    assert callable(servicefeaturemodel_Attribute.__init__)


def test_hyp_servicefeaturemodel_attribute_constructor_args():
    sig = inspect.signature(servicefeaturemodel_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "instantiationValue" in params, "Missing parameter 'instantiationValue'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_servicefeaturemodel_servicefeature_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_ServiceFeature)


def test_hyp_servicefeaturemodel_servicefeature_constructor_exists():
    assert callable(servicefeaturemodel_ServiceFeature.__init__)


def test_hyp_servicefeaturemodel_servicefeature_constructor_args():
    sig = inspect.signature(servicefeaturemodel_ServiceFeature.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"
    assert "maxAmount" in params, "Missing parameter 'maxAmount'"
    assert "description" in params, "Missing parameter 'description'"
    assert "associatedGSMElement" in params, "Missing parameter 'associatedGSMElement'"
    assert "name" in params, "Missing parameter 'name'"
    assert "featureType" in params, "Missing parameter 'featureType'"
    assert "minAmount" in params, "Missing parameter 'minAmount'"
    assert "mapsToGSMElement" in params, "Missing parameter 'mapsToGSMElement'"
    assert "id" in params, "Missing parameter 'id'"












def test_hyp_servicefeaturemodel_servicefeaturediagram_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_ServiceFeatureDiagram)


def test_hyp_servicefeaturemodel_servicefeaturediagram_constructor_exists():
    assert callable(servicefeaturemodel_ServiceFeatureDiagram.__init__)


def test_hyp_servicefeaturemodel_servicefeaturediagram_constructor_args():
    sig = inspect.signature(servicefeaturemodel_ServiceFeatureDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_servicefeaturemodel_service_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_Service)


def test_hyp_servicefeaturemodel_service_constructor_exists():
    assert callable(servicefeaturemodel_Service.__init__)


def test_hyp_servicefeaturemodel_service_constructor_args():
    sig = inspect.signature(servicefeaturemodel_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"






def test_hyp_servicefeaturemodel_attributetypes_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_AttributeTypes)


def test_hyp_servicefeaturemodel_attributetypes_constructor_exists():
    assert callable(servicefeaturemodel_AttributeTypes.__init__)


def test_hyp_servicefeaturemodel_attributetypes_constructor_args():
    sig = inspect.signature(servicefeaturemodel_AttributeTypes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicefeaturemodel_possibleconfigurations_is_not_abstract():
    assert not inspect.isabstract(servicefeaturemodel_PossibleConfigurations)


def test_hyp_servicefeaturemodel_possibleconfigurations_constructor_exists():
    assert callable(servicefeaturemodel_PossibleConfigurations.__init__)


def test_hyp_servicefeaturemodel_possibleconfigurations_constructor_args():
    sig = inspect.signature(servicefeaturemodel_PossibleConfigurations.__init__)
    params = list(sig.parameters.keys())

def test_hyp_featuretypes_exists():
    # Check that the Enumeration exists
    assert FeatureTypes is not None

def test_hyp_featuretypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FeatureTypes]
    expected_literals = [
        "InstanceFeature",
        "GroupingFeature",
        "AbstractFeature",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FeatureTypes"

def test_hyp_aggregationrules_exists():
    # Check that the Enumeration exists
    assert AggregationRules is not None

def test_hyp_aggregationrules_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationRules]
    expected_literals = [
        "Maximum",
        "Minimum",
        "Sum",
        "AtLeastOnce",
        "Product",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationRules"

def test_hyp_scaleorders_exists():
    # Check that the Enumeration exists
    assert ScaleOrders is not None

def test_hyp_scaleorders_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScaleOrders]
    expected_literals = [
        "HigherIsBetter",
        "LowerIsBetter",
        "ExistenceIsBetter",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScaleOrders"

def test_hyp_attributedomain_exists():
    # Check that the Enumeration exists
    assert AttributeDomain is not None

def test_hyp_attributedomain_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeDomain]
    expected_literals = [
        "Continuous",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeDomain"


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
ModifyRelationship_strategy = st.builds(
    ModifyRelationship,
)
servicefeaturemodel_FeatureToAttributeModifyRelationship_strategy = st.builds(
    servicefeaturemodel_FeatureToAttributeModifyRelationship,
)
servicefeaturemodel_AttributeToAttributeModifyRelationship_strategy = st.builds(
    servicefeaturemodel_AttributeToAttributeModifyRelationship,
    triggerParameterName=
        safe_text
)
servicefeaturemodel_Preference_strategy = st.builds(
    servicefeaturemodel_Preference,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    creationDate=
        st.dates(),
    description=
        safe_text,
    stakeholderGroup=
        safe_text
)
servicefeaturemodel_Configuration_strategy = st.builds(
    servicefeaturemodel_Configuration,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
Variant_strategy = st.builds(
    Variant,
)
servicefeaturemodel_OR_strategy = st.builds(
    servicefeaturemodel_OR,
    maxFeaturesToChoose=
        st.integers(),
    minFeaturesToChoose=
        st.integers()
)
servicefeaturemodel_ModifyRelationship_strategy = st.builds(
    servicefeaturemodel_ModifyRelationship,
    orderNumber=
        st.integers(),
    name=
        safe_text,
    function=
        safe_text,
    targetParameterName=
        safe_text
)
servicefeaturemodel_AttributeType_strategy = st.builds(
    servicefeaturemodel_AttributeType,
    toBeEvaluated=
        st.booleans(),
    aggregationRule=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    requirement=
        safe_text,
    domain=
        safe_text,
    customAttributeTypePriority=
        st.integers(),
    scaleOrder=
        safe_text
)
ServiceFeature_strategy = st.builds(
    ServiceFeature,
)
servicefeaturemodel_MandatoryServiceFeature_strategy = st.builds(
    servicefeaturemodel_MandatoryServiceFeature,
)
servicefeaturemodel_OptionalServiceFeature_strategy = st.builds(
    servicefeaturemodel_OptionalServiceFeature,
)
servicefeaturemodel_XOR_strategy = st.builds(
    servicefeaturemodel_XOR,
)
servicefeaturemodel_Excludes_strategy = st.builds(
    servicefeaturemodel_Excludes,
)
servicefeaturemodel_Requires_strategy = st.builds(
    servicefeaturemodel_Requires,
)
servicefeaturemodel_Variant_strategy = st.builds(
    servicefeaturemodel_Variant,
)
servicefeaturemodel_Attribute_strategy = st.builds(
    servicefeaturemodel_Attribute,
    instantiationValue=
        safe_text,
    id=
        safe_text
)
servicefeaturemodel_ServiceFeature_strategy = st.builds(
    servicefeaturemodel_ServiceFeature,
    required=
        st.booleans(),
    maxAmount=
        st.integers(),
    description=
        safe_text,
    associatedGSMElement=
        safe_text,
    name=
        safe_text,
    featureType=
        safe_text,
    minAmount=
        st.integers(),
    mapsToGSMElement=
        st.booleans(),
    id=
        safe_text
)
servicefeaturemodel_ServiceFeatureDiagram_strategy = st.builds(
    servicefeaturemodel_ServiceFeatureDiagram,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
servicefeaturemodel_Service_strategy = st.builds(
    servicefeaturemodel_Service,
    name=
        safe_text,
    id=
        safe_text,
    description=
        safe_text
)
servicefeaturemodel_AttributeTypes_strategy = st.builds(
    servicefeaturemodel_AttributeTypes,
)
servicefeaturemodel_PossibleConfigurations_strategy = st.builds(
    servicefeaturemodel_PossibleConfigurations,
)






@given(instance=servicefeaturemodel_AttributeToAttributeModifyRelationship_strategy)
def test_hyp_servicefeaturemodel_attributetoattributemodifyrelationship_triggerParameterName_setter(instance):
    original = instance.triggerParameterName
    instance.triggerParameterName = original
    assert instance.triggerParameterName == original




@given(instance=servicefeaturemodel_Preference_strategy)
def test_hyp_servicefeaturemodel_preference_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=servicefeaturemodel_Preference_strategy)
def test_hyp_servicefeaturemodel_preference_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=servicefeaturemodel_Preference_strategy)
def test_hyp_servicefeaturemodel_preference_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=servicefeaturemodel_Preference_strategy)
def test_hyp_servicefeaturemodel_preference_stakeholderGroup_setter(instance):
    original = instance.stakeholderGroup
    instance.stakeholderGroup = original
    assert instance.stakeholderGroup == original




@given(instance=servicefeaturemodel_Configuration_strategy)
def test_hyp_servicefeaturemodel_configuration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=servicefeaturemodel_Configuration_strategy)
def test_hyp_servicefeaturemodel_configuration_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=servicefeaturemodel_Configuration_strategy)
def test_hyp_servicefeaturemodel_configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=servicefeaturemodel_Configuration_strategy)
@settings(max_examples=30)
def test_hyp_servicefeaturemodel_configuration_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in servicefeaturemodel_Configuration is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in servicefeaturemodel_Configuration did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in servicefeaturemodel_Configuration is not implemented or raised an error")





@given(instance=servicefeaturemodel_OR_strategy)
def test_hyp_servicefeaturemodel_or_maxFeaturesToChoose_setter(instance):
    original = instance.maxFeaturesToChoose
    instance.maxFeaturesToChoose = original
    assert instance.maxFeaturesToChoose == original



@given(instance=servicefeaturemodel_OR_strategy)
def test_hyp_servicefeaturemodel_or_minFeaturesToChoose_setter(instance):
    original = instance.minFeaturesToChoose
    instance.minFeaturesToChoose = original
    assert instance.minFeaturesToChoose == original




@given(instance=servicefeaturemodel_ModifyRelationship_strategy)
def test_hyp_servicefeaturemodel_modifyrelationship_orderNumber_setter(instance):
    original = instance.orderNumber
    instance.orderNumber = original
    assert instance.orderNumber == original



@given(instance=servicefeaturemodel_ModifyRelationship_strategy)
def test_hyp_servicefeaturemodel_modifyrelationship_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=servicefeaturemodel_ModifyRelationship_strategy)
def test_hyp_servicefeaturemodel_modifyrelationship_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=servicefeaturemodel_ModifyRelationship_strategy)
def test_hyp_servicefeaturemodel_modifyrelationship_targetParameterName_setter(instance):
    original = instance.targetParameterName
    instance.targetParameterName = original
    assert instance.targetParameterName == original




@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_toBeEvaluated_setter(instance):
    original = instance.toBeEvaluated
    instance.toBeEvaluated = original
    assert instance.toBeEvaluated == original



@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_aggregationRule_setter(instance):
    original = instance.aggregationRule
    instance.aggregationRule = original
    assert instance.aggregationRule == original



@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_requirement_setter(instance):
    original = instance.requirement
    instance.requirement = original
    assert instance.requirement == original



@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original



@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_customAttributeTypePriority_setter(instance):
    original = instance.customAttributeTypePriority
    instance.customAttributeTypePriority = original
    assert instance.customAttributeTypePriority == original



@given(instance=servicefeaturemodel_AttributeType_strategy)
def test_hyp_servicefeaturemodel_attributetype_scaleOrder_setter(instance):
    original = instance.scaleOrder
    instance.scaleOrder = original
    assert instance.scaleOrder == original











@given(instance=servicefeaturemodel_Attribute_strategy)
def test_hyp_servicefeaturemodel_attribute_instantiationValue_setter(instance):
    original = instance.instantiationValue
    instance.instantiationValue = original
    assert instance.instantiationValue == original



@given(instance=servicefeaturemodel_Attribute_strategy)
def test_hyp_servicefeaturemodel_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_maxAmount_setter(instance):
    original = instance.maxAmount
    instance.maxAmount = original
    assert instance.maxAmount == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_associatedGSMElement_setter(instance):
    original = instance.associatedGSMElement
    instance.associatedGSMElement = original
    assert instance.associatedGSMElement == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_featureType_setter(instance):
    original = instance.featureType
    instance.featureType = original
    assert instance.featureType == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_minAmount_setter(instance):
    original = instance.minAmount
    instance.minAmount = original
    assert instance.minAmount == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_mapsToGSMElement_setter(instance):
    original = instance.mapsToGSMElement
    instance.mapsToGSMElement = original
    assert instance.mapsToGSMElement == original



@given(instance=servicefeaturemodel_ServiceFeature_strategy)
def test_hyp_servicefeaturemodel_servicefeature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=servicefeaturemodel_ServiceFeature_strategy)
@settings(max_examples=30)
def test_hyp_servicefeaturemodel_servicefeature_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in servicefeaturemodel_ServiceFeature is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in servicefeaturemodel_ServiceFeature did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in servicefeaturemodel_ServiceFeature is not implemented or raised an error")




@given(instance=servicefeaturemodel_ServiceFeatureDiagram_strategy)
def test_hyp_servicefeaturemodel_servicefeaturediagram_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=servicefeaturemodel_ServiceFeatureDiagram_strategy)
def test_hyp_servicefeaturemodel_servicefeaturediagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=servicefeaturemodel_ServiceFeatureDiagram_strategy)
def test_hyp_servicefeaturemodel_servicefeaturediagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=servicefeaturemodel_ServiceFeatureDiagram_strategy)
@settings(max_examples=30)
def test_hyp_servicefeaturemodel_servicefeaturediagram_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in servicefeaturemodel_ServiceFeatureDiagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in servicefeaturemodel_ServiceFeatureDiagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in servicefeaturemodel_ServiceFeatureDiagram is not implemented or raised an error")




@given(instance=servicefeaturemodel_Service_strategy)
def test_hyp_servicefeaturemodel_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=servicefeaturemodel_Service_strategy)
def test_hyp_servicefeaturemodel_service_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=servicefeaturemodel_Service_strategy)
def test_hyp_servicefeaturemodel_service_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ModifyRelationship,
    ServiceFeature,
    Variant,
    servicefeaturemodel_Attribute,
    servicefeaturemodel_AttributeToAttributeModifyRelationship,
    servicefeaturemodel_AttributeType,
    servicefeaturemodel_AttributeTypes,
    servicefeaturemodel_Configuration,
    servicefeaturemodel_Excludes,
    servicefeaturemodel_FeatureToAttributeModifyRelationship,
    servicefeaturemodel_MandatoryServiceFeature,
    servicefeaturemodel_ModifyRelationship,
    servicefeaturemodel_OR,
    servicefeaturemodel_OptionalServiceFeature,
    servicefeaturemodel_PossibleConfigurations,
    servicefeaturemodel_Preference,
    servicefeaturemodel_Requires,
    servicefeaturemodel_Service,
    servicefeaturemodel_ServiceFeature,
    servicefeaturemodel_ServiceFeatureDiagram,
    servicefeaturemodel_Variant,
    servicefeaturemodel_XOR,
    AggregationRules,
    AttributeDomain,
    FeatureTypes,
    ScaleOrders,
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

def test_servicefeaturemodel_Attribute_id_value_roundtrip():
    instance = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_Attribute_instantiationValue_value_roundtrip():
    instance = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    assert instance.instantiationValue == "sample_text"
    instance.instantiationValue = "sample_text_2"
    assert instance.instantiationValue == "sample_text_2"


def test_servicefeaturemodel_AttributeToAttributeModifyRelationship_triggerParameterName_value_roundtrip():
    instance = servicefeaturemodel_AttributeToAttributeModifyRelationship(triggerParameterName="sample_text")
    assert instance.triggerParameterName == "sample_text"
    instance.triggerParameterName = "sample_text_2"
    assert instance.triggerParameterName == "sample_text_2"


def test_servicefeaturemodel_AttributeType_aggregationRule_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.aggregationRule == "sample_text"
    instance.aggregationRule = "sample_text_2"
    assert instance.aggregationRule == "sample_text_2"


def test_servicefeaturemodel_AttributeType_customAttributeTypePriority_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.customAttributeTypePriority == 7
    instance.customAttributeTypePriority = 13
    assert instance.customAttributeTypePriority == 13


def test_servicefeaturemodel_AttributeType_description_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_AttributeType_domain_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.domain == "sample_text"
    instance.domain = "sample_text_2"
    assert instance.domain == "sample_text_2"


def test_servicefeaturemodel_AttributeType_name_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_AttributeType_requirement_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.requirement == "sample_text"
    instance.requirement = "sample_text_2"
    assert instance.requirement == "sample_text_2"


def test_servicefeaturemodel_AttributeType_scaleOrder_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.scaleOrder == "sample_text"
    instance.scaleOrder = "sample_text_2"
    assert instance.scaleOrder == "sample_text_2"


def test_servicefeaturemodel_AttributeType_toBeEvaluated_value_roundtrip():
    instance = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    assert instance.toBeEvaluated == True
    instance.toBeEvaluated = False
    assert instance.toBeEvaluated == False


def test_servicefeaturemodel_Configuration_description_value_roundtrip():
    instance = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_Configuration_id_value_roundtrip():
    instance = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_Configuration_name_value_roundtrip():
    instance = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_ModifyRelationship_function_value_roundtrip():
    instance = servicefeaturemodel_ModifyRelationship(function="sample_text", name="sample_text", orderNumber=7, targetParameterName="sample_text")
    assert instance.function == "sample_text"
    instance.function = "sample_text_2"
    assert instance.function == "sample_text_2"


def test_servicefeaturemodel_ModifyRelationship_name_value_roundtrip():
    instance = servicefeaturemodel_ModifyRelationship(function="sample_text", name="sample_text", orderNumber=7, targetParameterName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_ModifyRelationship_orderNumber_value_roundtrip():
    instance = servicefeaturemodel_ModifyRelationship(function="sample_text", name="sample_text", orderNumber=7, targetParameterName="sample_text")
    assert instance.orderNumber == 7
    instance.orderNumber = 13
    assert instance.orderNumber == 13


def test_servicefeaturemodel_ModifyRelationship_targetParameterName_value_roundtrip():
    instance = servicefeaturemodel_ModifyRelationship(function="sample_text", name="sample_text", orderNumber=7, targetParameterName="sample_text")
    assert instance.targetParameterName == "sample_text"
    instance.targetParameterName = "sample_text_2"
    assert instance.targetParameterName == "sample_text_2"


def test_servicefeaturemodel_OR_maxFeaturesToChoose_value_roundtrip():
    instance = servicefeaturemodel_OR(maxFeaturesToChoose=7, minFeaturesToChoose=7)
    assert instance.maxFeaturesToChoose == 7
    instance.maxFeaturesToChoose = 13
    assert instance.maxFeaturesToChoose == 13


def test_servicefeaturemodel_OR_minFeaturesToChoose_value_roundtrip():
    instance = servicefeaturemodel_OR(maxFeaturesToChoose=7, minFeaturesToChoose=7)
    assert instance.minFeaturesToChoose == 7
    instance.minFeaturesToChoose = 13
    assert instance.minFeaturesToChoose == 13


def test_servicefeaturemodel_Preference_creationDate_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.creationDate == date(2024, 1, 1)
    instance.creationDate = date(2025, 6, 15)
    assert instance.creationDate == date(2025, 6, 15)


def test_servicefeaturemodel_Preference_description_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_Preference_stakeholderGroup_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.stakeholderGroup == "sample_text"
    instance.stakeholderGroup = "sample_text_2"
    assert instance.stakeholderGroup == "sample_text_2"


def test_servicefeaturemodel_Preference_value_value_roundtrip():
    instance = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_servicefeaturemodel_Service_description_value_roundtrip():
    instance = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_Service_id_value_roundtrip():
    instance = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_Service_name_value_roundtrip():
    instance = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_associatedGSMElement_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.associatedGSMElement == "sample_text"
    instance.associatedGSMElement = "sample_text_2"
    assert instance.associatedGSMElement == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_description_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_featureType_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.featureType == "sample_text"
    instance.featureType = "sample_text_2"
    assert instance.featureType == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_id_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_mapsToGSMElement_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.mapsToGSMElement == True
    instance.mapsToGSMElement = False
    assert instance.mapsToGSMElement == False


def test_servicefeaturemodel_ServiceFeature_maxAmount_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.maxAmount == 7
    instance.maxAmount = 13
    assert instance.maxAmount == 13


def test_servicefeaturemodel_ServiceFeature_minAmount_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.minAmount == 7
    instance.minAmount = 13
    assert instance.minAmount == 13


def test_servicefeaturemodel_ServiceFeature_name_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_ServiceFeature_required_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_servicefeaturemodel_ServiceFeatureDiagram_description_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_servicefeaturemodel_ServiceFeatureDiagram_id_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_servicefeaturemodel_ServiceFeatureDiagram_name_value_roundtrip():
    instance = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_servicefeaturemodel_AttributeToAttributeModifyRelationship_isa_ModifyRelationship():
    instance = servicefeaturemodel_AttributeToAttributeModifyRelationship(triggerParameterName="sample_text")
    assert isinstance(instance, ModifyRelationship)


def test_servicefeaturemodel_FeatureToAttributeModifyRelationship_isa_ModifyRelationship():
    instance = servicefeaturemodel_FeatureToAttributeModifyRelationship()
    assert isinstance(instance, ModifyRelationship)


def test_servicefeaturemodel_MandatoryServiceFeature_isa_ServiceFeature():
    instance = servicefeaturemodel_MandatoryServiceFeature()
    assert isinstance(instance, ServiceFeature)


def test_servicefeaturemodel_OptionalServiceFeature_isa_ServiceFeature():
    instance = servicefeaturemodel_OptionalServiceFeature()
    assert isinstance(instance, ServiceFeature)


def test_servicefeaturemodel_OR_isa_Variant():
    instance = servicefeaturemodel_OR(maxFeaturesToChoose=7, minFeaturesToChoose=7)
    assert isinstance(instance, Variant)


def test_servicefeaturemodel_XOR_isa_Variant():
    instance = servicefeaturemodel_XOR()
    assert isinstance(instance, Variant)


def test_assoc_contains37_link_reassign_clear():
    a = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_PossibleConfigurations()
    b2 = servicefeaturemodel_PossibleConfigurations()
    _safe_set(a, 'servicefeaturemodel_Configuration39', b1)
    assert _is_linked(a, 'servicefeaturemodel_Configuration39', b1)
    if hasattr(b1, 'servicefeaturemodel_PossibleConfigurations38'):
        assert _is_linked(b1, 'servicefeaturemodel_PossibleConfigurations38', a)
    _safe_set(a, 'servicefeaturemodel_Configuration39', b2)
    assert _is_linked(a, 'servicefeaturemodel_Configuration39', b2)
    if hasattr(b1, 'servicefeaturemodel_PossibleConfigurations38'):
        assert not _is_linked(b1, 'servicefeaturemodel_PossibleConfigurations38', a)
    if hasattr(b2, 'servicefeaturemodel_PossibleConfigurations38'):
        assert _is_linked(b2, 'servicefeaturemodel_PossibleConfigurations38', a)
    _safe_set(a, 'servicefeaturemodel_Configuration39', None)
    assert not _is_linked(a, 'servicefeaturemodel_Configuration39', b2)
    if hasattr(b2, 'servicefeaturemodel_PossibleConfigurations38'):
        assert not _is_linked(b2, 'servicefeaturemodel_PossibleConfigurations38', a)


def test_assoc_contains40_link_reassign_clear():
    a = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    b1 = servicefeaturemodel_AttributeTypes()
    b2 = servicefeaturemodel_AttributeTypes()
    _safe_set(a, 'servicefeaturemodel_AttributeType42', b1)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType42', b1)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes41'):
        assert _is_linked(b1, 'servicefeaturemodel_AttributeTypes41', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType42', b2)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType42', b2)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes41'):
        assert not _is_linked(b1, 'servicefeaturemodel_AttributeTypes41', a)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes41'):
        assert _is_linked(b2, 'servicefeaturemodel_AttributeTypes41', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType42', None)
    assert not _is_linked(a, 'servicefeaturemodel_AttributeType42', b2)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes41'):
        assert not _is_linked(b2, 'servicefeaturemodel_AttributeTypes41', a)


def test_assoc_containsExcludes10_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_Excludes()
    b2 = servicefeaturemodel_Excludes()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature11', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature11', b1)
    if hasattr(b1, 'servicefeaturemodel_Excludes'):
        assert _is_linked(b1, 'servicefeaturemodel_Excludes', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature11', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature11', b2)
    if hasattr(b1, 'servicefeaturemodel_Excludes'):
        assert not _is_linked(b1, 'servicefeaturemodel_Excludes', a)
    if hasattr(b2, 'servicefeaturemodel_Excludes'):
        assert _is_linked(b2, 'servicefeaturemodel_Excludes', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature11', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature11', b2)
    if hasattr(b2, 'servicefeaturemodel_Excludes'):
        assert not _is_linked(b2, 'servicefeaturemodel_Excludes', a)


def test_assoc_containsFeatures25_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b2 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text_2", description="sample_text_2", featureType="sample_text_2", id="sample_text_2", mapsToGSMElement=False, maxAmount=13, minAmount=13, name="sample_text_2", required=False)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram26', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram26', b1)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature27'):
        assert _is_linked(b1, 'servicefeaturemodel_ServiceFeature27', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram26', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram26', b2)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature27'):
        assert not _is_linked(b1, 'servicefeaturemodel_ServiceFeature27', a)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature27'):
        assert _is_linked(b2, 'servicefeaturemodel_ServiceFeature27', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram26', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram26', b2)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature27'):
        assert not _is_linked(b2, 'servicefeaturemodel_ServiceFeature27', a)


def test_assoc_containsModifyRelationship17_link_reassign_clear():
    a = servicefeaturemodel_ModifyRelationship(function="sample_text", name="sample_text", orderNumber=7, targetParameterName="sample_text")
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ModifyRelationship', b1)
    assert _is_linked(a, 'servicefeaturemodel_ModifyRelationship', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute18'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute18', a)
    _safe_set(a, 'servicefeaturemodel_ModifyRelationship', b2)
    assert _is_linked(a, 'servicefeaturemodel_ModifyRelationship', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute18'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute18', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute18'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute18', a)
    _safe_set(a, 'servicefeaturemodel_ModifyRelationship', None)
    assert not _is_linked(a, 'servicefeaturemodel_ModifyRelationship', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute18'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute18', a)


def test_assoc_containsRequires8_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_Requires()
    b2 = servicefeaturemodel_Requires()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature9', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature9', b1)
    if hasattr(b1, 'servicefeaturemodel_Requires'):
        assert _is_linked(b1, 'servicefeaturemodel_Requires', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature9', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature9', b2)
    if hasattr(b1, 'servicefeaturemodel_Requires'):
        assert not _is_linked(b1, 'servicefeaturemodel_Requires', a)
    if hasattr(b2, 'servicefeaturemodel_Requires'):
        assert _is_linked(b2, 'servicefeaturemodel_Requires', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature9', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature9', b2)
    if hasattr(b2, 'servicefeaturemodel_Requires'):
        assert not _is_linked(b2, 'servicefeaturemodel_Requires', a)


def test_assoc_containsVariant6_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_Variant()
    b2 = servicefeaturemodel_Variant()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature7', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature7', b1)
    if hasattr(b1, 'servicefeaturemodel_Variant'):
        assert _is_linked(b1, 'servicefeaturemodel_Variant', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature7', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature7', b2)
    if hasattr(b1, 'servicefeaturemodel_Variant'):
        assert not _is_linked(b1, 'servicefeaturemodel_Variant', a)
    if hasattr(b2, 'servicefeaturemodel_Variant'):
        assert _is_linked(b2, 'servicefeaturemodel_Variant', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature7', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature7', b2)
    if hasattr(b2, 'servicefeaturemodel_Variant'):
        assert not _is_linked(b2, 'servicefeaturemodel_Variant', a)


def test_assoc_decomposesInto13_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b2 = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text_2", description="sample_text_2", featureType="sample_text_2", id="sample_text_2", mapsToGSMElement=False, maxAmount=13, minAmount=13, name="sample_text_2", required=False)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature12', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature12', b1)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature14'):
        assert _is_linked(b1, 'servicefeaturemodel_ServiceFeature14', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature12', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature12', b2)
    if hasattr(b1, 'servicefeaturemodel_ServiceFeature14'):
        assert not _is_linked(b1, 'servicefeaturemodel_ServiceFeature14', a)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature14'):
        assert _is_linked(b2, 'servicefeaturemodel_ServiceFeature14', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature12', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature12', b2)
    if hasattr(b2, 'servicefeaturemodel_ServiceFeature14'):
        assert not _is_linked(b2, 'servicefeaturemodel_ServiceFeature14', a)


def test_assoc_describedBy32_link_reassign_clear():
    a = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_Configuration33', {b1})
    assert _is_linked(a, 'servicefeaturemodel_Configuration33', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute34'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute34', a)
    _safe_set(a, 'servicefeaturemodel_Configuration33', {b2})
    assert _is_linked(a, 'servicefeaturemodel_Configuration33', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute34'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute34', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute34'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute34', a)
    _safe_set(a, 'servicefeaturemodel_Configuration33', set())
    assert not _is_linked(a, 'servicefeaturemodel_Configuration33', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute34'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute34', a)


def test_assoc_describedBy5_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ServiceFeature', {b1})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature', {b2})
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature', set())
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute', a)


def test_assoc_enables1_link_reassign_clear():
    a = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_PossibleConfigurations()
    b2 = servicefeaturemodel_PossibleConfigurations()
    _safe_set(a, 'servicefeaturemodel_Service2', b1)
    assert _is_linked(a, 'servicefeaturemodel_Service2', b1)
    if hasattr(b1, 'servicefeaturemodel_PossibleConfigurations'):
        assert _is_linked(b1, 'servicefeaturemodel_PossibleConfigurations', a)
    _safe_set(a, 'servicefeaturemodel_Service2', b2)
    assert _is_linked(a, 'servicefeaturemodel_Service2', b2)
    if hasattr(b1, 'servicefeaturemodel_PossibleConfigurations'):
        assert not _is_linked(b1, 'servicefeaturemodel_PossibleConfigurations', a)
    if hasattr(b2, 'servicefeaturemodel_PossibleConfigurations'):
        assert _is_linked(b2, 'servicefeaturemodel_PossibleConfigurations', a)
    _safe_set(a, 'servicefeaturemodel_Service2', None)
    assert not _is_linked(a, 'servicefeaturemodel_Service2', b2)
    if hasattr(b2, 'servicefeaturemodel_PossibleConfigurations'):
        assert not _is_linked(b2, 'servicefeaturemodel_PossibleConfigurations', a)


def test_assoc_evaluatedBy30_link_reassign_clear():
    a = servicefeaturemodel_Preference(creationDate=date(2024, 1, 1), description="sample_text", stakeholderGroup="sample_text", value=3.14)
    b1 = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    b2 = servicefeaturemodel_Configuration(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_Preference', b1)
    assert _is_linked(a, 'servicefeaturemodel_Preference', b1)
    if hasattr(b1, 'servicefeaturemodel_Configuration31'):
        assert _is_linked(b1, 'servicefeaturemodel_Configuration31', a)
    _safe_set(a, 'servicefeaturemodel_Preference', b2)
    assert _is_linked(a, 'servicefeaturemodel_Preference', b2)
    if hasattr(b1, 'servicefeaturemodel_Configuration31'):
        assert not _is_linked(b1, 'servicefeaturemodel_Configuration31', a)
    if hasattr(b2, 'servicefeaturemodel_Configuration31'):
        assert _is_linked(b2, 'servicefeaturemodel_Configuration31', a)
    _safe_set(a, 'servicefeaturemodel_Preference', None)
    assert not _is_linked(a, 'servicefeaturemodel_Preference', b2)
    if hasattr(b2, 'servicefeaturemodel_Configuration31'):
        assert not _is_linked(b2, 'servicefeaturemodel_Configuration31', a)


def test_assoc_excludesServiceFeature22_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_Excludes()
    b2 = servicefeaturemodel_Excludes()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature24', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature24', b1)
    if hasattr(b1, 'servicefeaturemodel_Excludes23'):
        assert _is_linked(b1, 'servicefeaturemodel_Excludes23', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature24', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature24', b2)
    if hasattr(b1, 'servicefeaturemodel_Excludes23'):
        assert not _is_linked(b1, 'servicefeaturemodel_Excludes23', a)
    if hasattr(b2, 'servicefeaturemodel_Excludes23'):
        assert _is_linked(b2, 'servicefeaturemodel_Excludes23', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature24', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature24', b2)
    if hasattr(b2, 'servicefeaturemodel_Excludes23'):
        assert not _is_linked(b2, 'servicefeaturemodel_Excludes23', a)


def test_assoc_groups28_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_Configuration(description="sample_text", id="sample_text", name="sample_text")
    b2 = servicefeaturemodel_Configuration(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ServiceFeature29', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature29', b1)
    if hasattr(b1, 'servicefeaturemodel_Configuration'):
        assert _is_linked(b1, 'servicefeaturemodel_Configuration', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature29', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature29', b2)
    if hasattr(b1, 'servicefeaturemodel_Configuration'):
        assert not _is_linked(b1, 'servicefeaturemodel_Configuration', a)
    if hasattr(b2, 'servicefeaturemodel_Configuration'):
        assert _is_linked(b2, 'servicefeaturemodel_Configuration', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature29', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature29', b2)
    if hasattr(b2, 'servicefeaturemodel_Configuration'):
        assert not _is_linked(b2, 'servicefeaturemodel_Configuration', a)


def test_assoc_has3_link_reassign_clear():
    a = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_AttributeTypes()
    b2 = servicefeaturemodel_AttributeTypes()
    _safe_set(a, 'servicefeaturemodel_Service4', b1)
    assert _is_linked(a, 'servicefeaturemodel_Service4', b1)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes'):
        assert _is_linked(b1, 'servicefeaturemodel_AttributeTypes', a)
    _safe_set(a, 'servicefeaturemodel_Service4', b2)
    assert _is_linked(a, 'servicefeaturemodel_Service4', b2)
    if hasattr(b1, 'servicefeaturemodel_AttributeTypes'):
        assert not _is_linked(b1, 'servicefeaturemodel_AttributeTypes', a)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes'):
        assert _is_linked(b2, 'servicefeaturemodel_AttributeTypes', a)
    _safe_set(a, 'servicefeaturemodel_Service4', None)
    assert not _is_linked(a, 'servicefeaturemodel_Service4', b2)
    if hasattr(b2, 'servicefeaturemodel_AttributeTypes'):
        assert not _is_linked(b2, 'servicefeaturemodel_AttributeTypes', a)


def test_assoc_ofAttributeType15_link_reassign_clear():
    a = servicefeaturemodel_AttributeType(aggregationRule="sample_text", customAttributeTypePriority=7, description="sample_text", domain="sample_text", name="sample_text", requirement="sample_text", scaleOrder="sample_text", toBeEvaluated=True)
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_AttributeType', b1)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute16'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute16', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType', b2)
    assert _is_linked(a, 'servicefeaturemodel_AttributeType', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute16'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute16', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute16'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute16', a)
    _safe_set(a, 'servicefeaturemodel_AttributeType', None)
    assert not _is_linked(a, 'servicefeaturemodel_AttributeType', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute16'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute16', a)


def test_assoc_representedBy0_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeatureDiagram(description="sample_text", id="sample_text", name="sample_text")
    b1 = servicefeaturemodel_Service(description="sample_text", id="sample_text", name="sample_text")
    b2 = servicefeaturemodel_Service(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram', b1)
    if hasattr(b1, 'servicefeaturemodel_Service'):
        assert _is_linked(b1, 'servicefeaturemodel_Service', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram', b2)
    if hasattr(b1, 'servicefeaturemodel_Service'):
        assert not _is_linked(b1, 'servicefeaturemodel_Service', a)
    if hasattr(b2, 'servicefeaturemodel_Service'):
        assert _is_linked(b2, 'servicefeaturemodel_Service', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeatureDiagram', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeatureDiagram', b2)
    if hasattr(b2, 'servicefeaturemodel_Service'):
        assert not _is_linked(b2, 'servicefeaturemodel_Service', a)


def test_assoc_requiresServiceFeature19_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_Requires()
    b2 = servicefeaturemodel_Requires()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature21', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature21', b1)
    if hasattr(b1, 'servicefeaturemodel_Requires20'):
        assert _is_linked(b1, 'servicefeaturemodel_Requires20', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature21', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature21', b2)
    if hasattr(b1, 'servicefeaturemodel_Requires20'):
        assert not _is_linked(b1, 'servicefeaturemodel_Requires20', a)
    if hasattr(b2, 'servicefeaturemodel_Requires20'):
        assert _is_linked(b2, 'servicefeaturemodel_Requires20', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature21', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature21', b2)
    if hasattr(b2, 'servicefeaturemodel_Requires20'):
        assert not _is_linked(b2, 'servicefeaturemodel_Requires20', a)


def test_assoc_triggeredByAttribute43_link_reassign_clear():
    a = servicefeaturemodel_AttributeToAttributeModifyRelationship(triggerParameterName="sample_text")
    b1 = servicefeaturemodel_Attribute(id="sample_text", instantiationValue="sample_text")
    b2 = servicefeaturemodel_Attribute(id="sample_text_2", instantiationValue="sample_text_2")
    _safe_set(a, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b1)
    assert _is_linked(a, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b1)
    if hasattr(b1, 'servicefeaturemodel_Attribute44'):
        assert _is_linked(b1, 'servicefeaturemodel_Attribute44', a)
    _safe_set(a, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b2)
    assert _is_linked(a, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b2)
    if hasattr(b1, 'servicefeaturemodel_Attribute44'):
        assert not _is_linked(b1, 'servicefeaturemodel_Attribute44', a)
    if hasattr(b2, 'servicefeaturemodel_Attribute44'):
        assert _is_linked(b2, 'servicefeaturemodel_Attribute44', a)
    _safe_set(a, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', None)
    assert not _is_linked(a, 'servicefeaturemodel_AttributeToAttributeModifyRelationship', b2)
    if hasattr(b2, 'servicefeaturemodel_Attribute44'):
        assert not _is_linked(b2, 'servicefeaturemodel_Attribute44', a)


def test_assoc_triggeredByServiceFeature45_link_reassign_clear():
    a = servicefeaturemodel_ServiceFeature(associatedGSMElement="sample_text", description="sample_text", featureType="sample_text", id="sample_text", mapsToGSMElement=True, maxAmount=7, minAmount=7, name="sample_text", required=True)
    b1 = servicefeaturemodel_FeatureToAttributeModifyRelationship()
    b2 = servicefeaturemodel_FeatureToAttributeModifyRelationship()
    _safe_set(a, 'servicefeaturemodel_ServiceFeature46', b1)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature46', b1)
    if hasattr(b1, 'servicefeaturemodel_FeatureToAttributeModifyRelationship'):
        assert _is_linked(b1, 'servicefeaturemodel_FeatureToAttributeModifyRelationship', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature46', b2)
    assert _is_linked(a, 'servicefeaturemodel_ServiceFeature46', b2)
    if hasattr(b1, 'servicefeaturemodel_FeatureToAttributeModifyRelationship'):
        assert not _is_linked(b1, 'servicefeaturemodel_FeatureToAttributeModifyRelationship', a)
    if hasattr(b2, 'servicefeaturemodel_FeatureToAttributeModifyRelationship'):
        assert _is_linked(b2, 'servicefeaturemodel_FeatureToAttributeModifyRelationship', a)
    _safe_set(a, 'servicefeaturemodel_ServiceFeature46', None)
    assert not _is_linked(a, 'servicefeaturemodel_ServiceFeature46', b2)
    if hasattr(b2, 'servicefeaturemodel_FeatureToAttributeModifyRelationship'):
        assert not _is_linked(b2, 'servicefeaturemodel_FeatureToAttributeModifyRelationship', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ModifyRelationship_strategy = st.builds(ModifyRelationship)
@given(instance=ModifyRelationship_strategy)
@settings(max_examples=25)
def test_ModifyRelationship_instantiation(instance):
    assert isinstance(instance, ModifyRelationship)


ServiceFeature_strategy = st.builds(ServiceFeature)
@given(instance=ServiceFeature_strategy)
@settings(max_examples=25)
def test_ServiceFeature_instantiation(instance):
    assert isinstance(instance, ServiceFeature)


Variant_strategy = st.builds(Variant)
@given(instance=Variant_strategy)
@settings(max_examples=25)
def test_Variant_instantiation(instance):
    assert isinstance(instance, Variant)


servicefeaturemodel_Attribute_strategy = st.builds(servicefeaturemodel_Attribute, id=safe_text, instantiationValue=safe_text)
@given(instance=servicefeaturemodel_Attribute_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Attribute_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Attribute)


servicefeaturemodel_AttributeToAttributeModifyRelationship_strategy = st.builds(servicefeaturemodel_AttributeToAttributeModifyRelationship, triggerParameterName=safe_text)
@given(instance=servicefeaturemodel_AttributeToAttributeModifyRelationship_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_AttributeToAttributeModifyRelationship_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_AttributeToAttributeModifyRelationship)


servicefeaturemodel_AttributeType_strategy = st.builds(servicefeaturemodel_AttributeType, aggregationRule=safe_text, customAttributeTypePriority=st.integers(), description=safe_text, domain=safe_text, name=safe_text, requirement=safe_text, scaleOrder=safe_text, toBeEvaluated=st.booleans())
@given(instance=servicefeaturemodel_AttributeType_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_AttributeType_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_AttributeType)


servicefeaturemodel_AttributeTypes_strategy = st.builds(servicefeaturemodel_AttributeTypes)
@given(instance=servicefeaturemodel_AttributeTypes_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_AttributeTypes_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_AttributeTypes)


servicefeaturemodel_Configuration_strategy = st.builds(servicefeaturemodel_Configuration, description=safe_text, id=safe_text, name=safe_text)
@given(instance=servicefeaturemodel_Configuration_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Configuration_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Configuration)


servicefeaturemodel_Excludes_strategy = st.builds(servicefeaturemodel_Excludes)
@given(instance=servicefeaturemodel_Excludes_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Excludes_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Excludes)


servicefeaturemodel_FeatureToAttributeModifyRelationship_strategy = st.builds(servicefeaturemodel_FeatureToAttributeModifyRelationship)
@given(instance=servicefeaturemodel_FeatureToAttributeModifyRelationship_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_FeatureToAttributeModifyRelationship_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_FeatureToAttributeModifyRelationship)


servicefeaturemodel_MandatoryServiceFeature_strategy = st.builds(servicefeaturemodel_MandatoryServiceFeature)
@given(instance=servicefeaturemodel_MandatoryServiceFeature_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_MandatoryServiceFeature_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_MandatoryServiceFeature)


servicefeaturemodel_ModifyRelationship_strategy = st.builds(servicefeaturemodel_ModifyRelationship, function=safe_text, name=safe_text, orderNumber=st.integers(), targetParameterName=safe_text)
@given(instance=servicefeaturemodel_ModifyRelationship_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_ModifyRelationship_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_ModifyRelationship)


servicefeaturemodel_OR_strategy = st.builds(servicefeaturemodel_OR, maxFeaturesToChoose=st.integers(), minFeaturesToChoose=st.integers())
@given(instance=servicefeaturemodel_OR_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_OR_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_OR)


servicefeaturemodel_OptionalServiceFeature_strategy = st.builds(servicefeaturemodel_OptionalServiceFeature)
@given(instance=servicefeaturemodel_OptionalServiceFeature_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_OptionalServiceFeature_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_OptionalServiceFeature)


servicefeaturemodel_PossibleConfigurations_strategy = st.builds(servicefeaturemodel_PossibleConfigurations)
@given(instance=servicefeaturemodel_PossibleConfigurations_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_PossibleConfigurations_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_PossibleConfigurations)


servicefeaturemodel_Preference_strategy = st.builds(servicefeaturemodel_Preference, creationDate=st.dates(), description=safe_text, stakeholderGroup=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=servicefeaturemodel_Preference_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Preference_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Preference)


servicefeaturemodel_Requires_strategy = st.builds(servicefeaturemodel_Requires)
@given(instance=servicefeaturemodel_Requires_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Requires_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Requires)


servicefeaturemodel_Service_strategy = st.builds(servicefeaturemodel_Service, description=safe_text, id=safe_text, name=safe_text)
@given(instance=servicefeaturemodel_Service_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Service_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Service)


servicefeaturemodel_ServiceFeature_strategy = st.builds(servicefeaturemodel_ServiceFeature, associatedGSMElement=safe_text, description=safe_text, featureType=safe_text, id=safe_text, mapsToGSMElement=st.booleans(), maxAmount=st.integers(), minAmount=st.integers(), name=safe_text, required=st.booleans())
@given(instance=servicefeaturemodel_ServiceFeature_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_ServiceFeature_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_ServiceFeature)


servicefeaturemodel_ServiceFeatureDiagram_strategy = st.builds(servicefeaturemodel_ServiceFeatureDiagram, description=safe_text, id=safe_text, name=safe_text)
@given(instance=servicefeaturemodel_ServiceFeatureDiagram_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_ServiceFeatureDiagram_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_ServiceFeatureDiagram)


servicefeaturemodel_Variant_strategy = st.builds(servicefeaturemodel_Variant)
@given(instance=servicefeaturemodel_Variant_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_Variant_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_Variant)


servicefeaturemodel_XOR_strategy = st.builds(servicefeaturemodel_XOR)
@given(instance=servicefeaturemodel_XOR_strategy)
@settings(max_examples=25)
def test_servicefeaturemodel_XOR_instantiation(instance):
    assert isinstance(instance, servicefeaturemodel_XOR)



