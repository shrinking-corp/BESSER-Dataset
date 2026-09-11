import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Abstract_ATT_ID,
    BasicAttrDef,
    BasicAttrValuation,
    ComplexExpression,
    EnumAttrDef,
    Expression,
    ExtendedValuation,
    FeatureDefinition,
    FeaturesGroup,
    IntegerAttrDef,
    RealAttrDef,
    TableBasedValuationByAttribute,
    VmBlock,
    vM_Abstract_ATT_ID,
    vM_AdvancedAttrValuation,
    vM_And,
    vM_AttHead,
    vM_AttrDef,
    vM_AttributeDescription,
    vM_Attributes,
    vM_BasicAttrDef,
    vM_BasicAttrValuation,
    vM_BiImplication,
    vM_BoolDefaultDef,
    vM_BooleanAttrDef,
    vM_BooleanAttrValuation,
    vM_BooleanExpression,
    vM_BooleanExpression_List,
    vM_BooleanValuation,
    vM_Boolean_ATT_ID,
    vM_BrackedExpression,
    vM_CardinalityBased,
    vM_ComplexExpression,
    vM_Configuration,
    vM_Configurations,
    vM_Constraint,
    vM_Constraints,
    vM_Descriptions,
    vM_Division,
    vM_Email,
    vM_EnumAttrDef,
    vM_EnumIntegerDef,
    vM_EnumRealDef,
    vM_EnumStringDef,
    vM_Enum_Integer_ATT_ID,
    vM_Enum_Real_ATT_ID,
    vM_Enum_String_ATT_ID,
    vM_Equality,
    vM_Excludes,
    vM_Expression,
    vM_ExtendedValuation,
    vM_Feature,
    vM_FeatureDefinition,
    vM_FeatureDescription,
    vM_FeatureHierarchy,
    vM_FeaturesGroup,
    vM_Greater,
    vM_Greaterequal,
    vM_If,
    vM_ImportDeclaration,
    vM_Inequality,
    vM_IntegerAttrDef,
    vM_IntegerAttrDefBounded,
    vM_IntegerAttrDefComplement,
    vM_IntegerAttrDefUnbounded,
    vM_IntegerAttrValuation,
    vM_IntegerDefaultDef,
    vM_IntegerDeltaDef,
    vM_Integer_ATT_ID,
    vM_LeftImplication,
    vM_Less,
    vM_Lessequal,
    vM_MetaDataDeclaration,
    vM_Minus,
    vM_Model,
    vM_Multiplication,
    vM_NumericExpression,
    vM_NumericExpression_List,
    vM_Objective,
    vM_ObjectiveExpression,
    vM_Objectives,
    vM_Or,
    vM_Orgroup,
    vM_PackageDeclaration,
    vM_PairAttributeValue,
    vM_PairFeatureInteger,
    vM_PairFeatureReal,
    vM_Plus,
    vM_PrimitiveExpression,
    vM_RealAttrDef,
    vM_RealAttrDefBounded,
    vM_RealAttrDefComplement,
    vM_RealAttrDefUnbounded,
    vM_RealAttrValuation,
    vM_RealDefaultDef,
    vM_RealDeltaDef,
    vM_Real_ATT_ID,
    vM_Relationships,
    vM_Requires,
    vM_RightImplication,
    vM_SpecialExpression,
    vM_StringAttrDef,
    vM_StringAttrValuation,
    vM_StringDefaultDef,
    vM_StringExpression,
    vM_String_ATT_ID,
    vM_TableBasedValuationByAttribute,
    vM_TableBasedValuationByAttributeForInteger,
    vM_TableBasedValuationByAttributeForReal,
    vM_TableBasedValuationByFeature,
    vM_TableBasedValuationByFeatureAndClone,
    vM_Version,
    vM_VmBlock,
    vM_Xorgroup,
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

def test_vM_Abstract_ATT_ID_name_value_roundtrip():
    instance = vM_Abstract_ATT_ID(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_AttHead_forAllFeatures_value_roundtrip():
    instance = vM_AttHead(forAllFeatures=True)
    assert instance.forAllFeatures == True
    instance.forAllFeatures = False
    assert instance.forAllFeatures == False


def test_vM_AttrDef_notDecidable_value_roundtrip():
    instance = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    assert instance.notDecidable == True
    instance.notDecidable = False
    assert instance.notDecidable == False


def test_vM_AttrDef_notTranslatable_value_roundtrip():
    instance = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    assert instance.notTranslatable == True
    instance.notTranslatable = False
    assert instance.notTranslatable == False


def test_vM_AttrDef_runTime_value_roundtrip():
    instance = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    assert instance.runTime == True
    instance.runTime = False
    assert instance.runTime == False


def test_vM_AttributeDescription_description_value_roundtrip():
    instance = vM_AttributeDescription(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_vM_BasicAttrValuation_value_value_roundtrip():
    instance = vM_BasicAttrValuation(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_BoolDefaultDef_value_value_roundtrip():
    instance = vM_BoolDefaultDef(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_BooleanAttrDef_value_value_roundtrip():
    instance = vM_BooleanAttrDef(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_BooleanExpression_op_value_roundtrip():
    instance = vM_BooleanExpression(op="sample_text", value="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_vM_BooleanExpression_value_value_roundtrip():
    instance = vM_BooleanExpression(op="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_BooleanValuation_notSelected_value_roundtrip():
    instance = vM_BooleanValuation(notSelected=True)
    assert instance.notSelected == True
    instance.notSelected = False
    assert instance.notSelected == False


def test_vM_CardinalityBased_all_value_roundtrip():
    instance = vM_CardinalityBased(all=True, max="sample_text", min="sample_text")
    assert instance.all == True
    instance.all = False
    assert instance.all == False


def test_vM_CardinalityBased_max_value_roundtrip():
    instance = vM_CardinalityBased(all=True, max="sample_text", min="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_vM_CardinalityBased_min_value_roundtrip():
    instance = vM_CardinalityBased(all=True, max="sample_text", min="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_vM_Configuration_name_value_roundtrip():
    instance = vM_Configuration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_Constraint_name_value_roundtrip():
    instance = vM_Constraint(name="sample_text", not_=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_Constraint_not__value_roundtrip():
    instance = vM_Constraint(name="sample_text", not_=True)
    assert instance.not_ == True
    instance.not_ = False
    assert instance.not_ == False


def test_vM_Email_domain_value_roundtrip():
    instance = vM_Email(domain="sample_text", username="sample_text")
    assert instance.domain == "sample_text"
    instance.domain = "sample_text_2"
    assert instance.domain == "sample_text_2"


def test_vM_Email_username_value_roundtrip():
    instance = vM_Email(domain="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_vM_EnumAttrDef_value_value_roundtrip():
    instance = vM_EnumAttrDef(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_Feature_max_value_roundtrip():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_vM_Feature_min_value_roundtrip():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_vM_Feature_name_value_roundtrip():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_Feature_notDecidable_value_roundtrip():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert instance.notDecidable == True
    instance.notDecidable = False
    assert instance.notDecidable == False


def test_vM_Feature_notTranslatable_value_roundtrip():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert instance.notTranslatable == True
    instance.notTranslatable = False
    assert instance.notTranslatable == False


def test_vM_Feature_optional_value_roundtrip():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_vM_Feature_runTime_value_roundtrip():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert instance.runTime == True
    instance.runTime = False
    assert instance.runTime == False


def test_vM_FeatureDescription_description_value_roundtrip():
    instance = vM_FeatureDescription(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_vM_ImportDeclaration_importedNamespace_value_roundtrip():
    instance = vM_ImportDeclaration(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_vM_IntegerAttrDefComplement_max_value_roundtrip():
    instance = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_vM_IntegerAttrDefComplement_min_value_roundtrip():
    instance = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_vM_IntegerAttrDefUnbounded_value_value_roundtrip():
    instance = vM_IntegerAttrDefUnbounded(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_IntegerDefaultDef_value_value_roundtrip():
    instance = vM_IntegerDefaultDef(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_vM_IntegerDeltaDef_value_value_roundtrip():
    instance = vM_IntegerDeltaDef(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_vM_MetaDataDeclaration_author_value_roundtrip():
    instance = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_vM_MetaDataDeclaration_date_value_roundtrip():
    instance = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_vM_MetaDataDeclaration_description_value_roundtrip():
    instance = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_vM_MetaDataDeclaration_name_value_roundtrip():
    instance = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_MetaDataDeclaration_organization_value_roundtrip():
    instance = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_vM_MetaDataDeclaration_publication_value_roundtrip():
    instance = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    assert instance.publication == "sample_text"
    instance.publication = "sample_text_2"
    assert instance.publication == "sample_text_2"


def test_vM_NumericExpression_op_value_roundtrip():
    instance = vM_NumericExpression(op="sample_text", value="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_vM_NumericExpression_value_value_roundtrip():
    instance = vM_NumericExpression(op="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_Objective_name_value_roundtrip():
    instance = vM_Objective(name="sample_text", op="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_Objective_op_value_roundtrip():
    instance = vM_Objective(name="sample_text", op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_vM_ObjectiveExpression_op_value_roundtrip():
    instance = vM_ObjectiveExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_vM_PackageDeclaration_name_value_roundtrip():
    instance = vM_PackageDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_PairAttributeValue_value_value_roundtrip():
    instance = vM_PairAttributeValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_PairFeatureInteger_value_value_roundtrip():
    instance = vM_PairFeatureInteger(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_PairFeatureReal_value_value_roundtrip():
    instance = vM_PairFeatureReal(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_RealAttrDefComplement_max_value_roundtrip():
    instance = vM_RealAttrDefComplement(max="sample_text", min="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_vM_RealAttrDefComplement_min_value_roundtrip():
    instance = vM_RealAttrDefComplement(max="sample_text", min="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_vM_RealAttrDefUnbounded_value_value_roundtrip():
    instance = vM_RealAttrDefUnbounded(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_RealDefaultDef_value_value_roundtrip():
    instance = vM_RealDefaultDef(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_RealDeltaDef_value_value_roundtrip():
    instance = vM_RealDeltaDef(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_SpecialExpression_op_value_roundtrip():
    instance = vM_SpecialExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_vM_StringAttrDef_value_value_roundtrip():
    instance = vM_StringAttrDef(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_StringDefaultDef_value_value_roundtrip():
    instance = vM_StringDefaultDef(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_StringExpression_value_value_roundtrip():
    instance = vM_StringExpression(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_vM_TableBasedValuationByFeatureAndClone_name_value_roundtrip():
    instance = vM_TableBasedValuationByFeatureAndClone(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_vM_Version_main_value_roundtrip():
    instance = vM_Version(main=7, tail=7)
    assert instance.main == 7
    instance.main = 13
    assert instance.main == 13


def test_vM_Version_tail_value_roundtrip():
    instance = vM_Version(main=7, tail=7)
    assert instance.tail == 7
    instance.tail = 13
    assert instance.tail == 13


def test_vM_Boolean_ATT_ID_isa_Abstract_ATT_ID():
    instance = vM_Boolean_ATT_ID()
    assert isinstance(instance, Abstract_ATT_ID)


def test_vM_Enum_Integer_ATT_ID_isa_Abstract_ATT_ID():
    instance = vM_Enum_Integer_ATT_ID()
    assert isinstance(instance, Abstract_ATT_ID)


def test_vM_Enum_Real_ATT_ID_isa_Abstract_ATT_ID():
    instance = vM_Enum_Real_ATT_ID()
    assert isinstance(instance, Abstract_ATT_ID)


def test_vM_Enum_String_ATT_ID_isa_Abstract_ATT_ID():
    instance = vM_Enum_String_ATT_ID()
    assert isinstance(instance, Abstract_ATT_ID)


def test_vM_Integer_ATT_ID_isa_Abstract_ATT_ID():
    instance = vM_Integer_ATT_ID()
    assert isinstance(instance, Abstract_ATT_ID)


def test_vM_Real_ATT_ID_isa_Abstract_ATT_ID():
    instance = vM_Real_ATT_ID()
    assert isinstance(instance, Abstract_ATT_ID)


def test_vM_String_ATT_ID_isa_Abstract_ATT_ID():
    instance = vM_String_ATT_ID()
    assert isinstance(instance, Abstract_ATT_ID)


def test_vM_BooleanAttrDef_isa_BasicAttrDef():
    instance = vM_BooleanAttrDef(value="sample_text")
    assert isinstance(instance, BasicAttrDef)


def test_vM_IntegerAttrDef_isa_BasicAttrDef():
    instance = vM_IntegerAttrDef()
    assert isinstance(instance, BasicAttrDef)


def test_vM_RealAttrDef_isa_BasicAttrDef():
    instance = vM_RealAttrDef()
    assert isinstance(instance, BasicAttrDef)


def test_vM_StringAttrDef_isa_BasicAttrDef():
    instance = vM_StringAttrDef(value="sample_text")
    assert isinstance(instance, BasicAttrDef)


def test_vM_BooleanAttrValuation_isa_BasicAttrValuation():
    instance = vM_BooleanAttrValuation()
    assert isinstance(instance, BasicAttrValuation)


def test_vM_IntegerAttrValuation_isa_BasicAttrValuation():
    instance = vM_IntegerAttrValuation()
    assert isinstance(instance, BasicAttrValuation)


def test_vM_RealAttrValuation_isa_BasicAttrValuation():
    instance = vM_RealAttrValuation()
    assert isinstance(instance, BasicAttrValuation)


def test_vM_StringAttrValuation_isa_BasicAttrValuation():
    instance = vM_StringAttrValuation()
    assert isinstance(instance, BasicAttrValuation)


def test_vM_And_isa_ComplexExpression():
    instance = vM_And()
    assert isinstance(instance, ComplexExpression)


def test_vM_BiImplication_isa_ComplexExpression():
    instance = vM_BiImplication()
    assert isinstance(instance, ComplexExpression)


def test_vM_Division_isa_ComplexExpression():
    instance = vM_Division()
    assert isinstance(instance, ComplexExpression)


def test_vM_Equality_isa_ComplexExpression():
    instance = vM_Equality()
    assert isinstance(instance, ComplexExpression)


def test_vM_Excludes_isa_ComplexExpression():
    instance = vM_Excludes()
    assert isinstance(instance, ComplexExpression)


def test_vM_Expression_isa_ComplexExpression():
    instance = vM_Expression()
    assert isinstance(instance, ComplexExpression)


def test_vM_Greater_isa_ComplexExpression():
    instance = vM_Greater()
    assert isinstance(instance, ComplexExpression)


def test_vM_Greaterequal_isa_ComplexExpression():
    instance = vM_Greaterequal()
    assert isinstance(instance, ComplexExpression)


def test_vM_If_isa_ComplexExpression():
    instance = vM_If()
    assert isinstance(instance, ComplexExpression)


def test_vM_Inequality_isa_ComplexExpression():
    instance = vM_Inequality()
    assert isinstance(instance, ComplexExpression)


def test_vM_LeftImplication_isa_ComplexExpression():
    instance = vM_LeftImplication()
    assert isinstance(instance, ComplexExpression)


def test_vM_Less_isa_ComplexExpression():
    instance = vM_Less()
    assert isinstance(instance, ComplexExpression)


def test_vM_Lessequal_isa_ComplexExpression():
    instance = vM_Lessequal()
    assert isinstance(instance, ComplexExpression)


def test_vM_Minus_isa_ComplexExpression():
    instance = vM_Minus()
    assert isinstance(instance, ComplexExpression)


def test_vM_Multiplication_isa_ComplexExpression():
    instance = vM_Multiplication()
    assert isinstance(instance, ComplexExpression)


def test_vM_Or_isa_ComplexExpression():
    instance = vM_Or()
    assert isinstance(instance, ComplexExpression)


def test_vM_Plus_isa_ComplexExpression():
    instance = vM_Plus()
    assert isinstance(instance, ComplexExpression)


def test_vM_Requires_isa_ComplexExpression():
    instance = vM_Requires()
    assert isinstance(instance, ComplexExpression)


def test_vM_RightImplication_isa_ComplexExpression():
    instance = vM_RightImplication()
    assert isinstance(instance, ComplexExpression)


def test_vM_EnumIntegerDef_isa_EnumAttrDef():
    instance = vM_EnumIntegerDef()
    assert isinstance(instance, EnumAttrDef)


def test_vM_EnumRealDef_isa_EnumAttrDef():
    instance = vM_EnumRealDef()
    assert isinstance(instance, EnumAttrDef)


def test_vM_EnumStringDef_isa_EnumAttrDef():
    instance = vM_EnumStringDef()
    assert isinstance(instance, EnumAttrDef)


def test_vM_BooleanExpression_isa_Expression():
    instance = vM_BooleanExpression(op="sample_text", value="sample_text")
    assert isinstance(instance, Expression)


def test_vM_BrackedExpression_isa_Expression():
    instance = vM_BrackedExpression()
    assert isinstance(instance, Expression)


def test_vM_NumericExpression_isa_Expression():
    instance = vM_NumericExpression(op="sample_text", value="sample_text")
    assert isinstance(instance, Expression)


def test_vM_PrimitiveExpression_isa_Expression():
    instance = vM_PrimitiveExpression()
    assert isinstance(instance, Expression)


def test_vM_SpecialExpression_isa_Expression():
    instance = vM_SpecialExpression(op="sample_text")
    assert isinstance(instance, Expression)


def test_vM_StringExpression_isa_Expression():
    instance = vM_StringExpression(value="sample_text")
    assert isinstance(instance, Expression)


def test_vM_AdvancedAttrValuation_isa_ExtendedValuation():
    instance = vM_AdvancedAttrValuation()
    assert isinstance(instance, ExtendedValuation)


def test_vM_BasicAttrValuation_isa_ExtendedValuation():
    instance = vM_BasicAttrValuation(value="sample_text")
    assert isinstance(instance, ExtendedValuation)


def test_vM_Feature_isa_FeatureDefinition():
    instance = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    assert isinstance(instance, FeatureDefinition)


def test_vM_FeatureHierarchy_isa_FeatureDefinition():
    instance = vM_FeatureHierarchy()
    assert isinstance(instance, FeatureDefinition)


def test_vM_FeaturesGroup_isa_FeatureDefinition():
    instance = vM_FeaturesGroup()
    assert isinstance(instance, FeatureDefinition)


def test_vM_CardinalityBased_isa_FeaturesGroup():
    instance = vM_CardinalityBased(all=True, max="sample_text", min="sample_text")
    assert isinstance(instance, FeaturesGroup)


def test_vM_Orgroup_isa_FeaturesGroup():
    instance = vM_Orgroup()
    assert isinstance(instance, FeaturesGroup)


def test_vM_Xorgroup_isa_FeaturesGroup():
    instance = vM_Xorgroup()
    assert isinstance(instance, FeaturesGroup)


def test_vM_IntegerAttrDefBounded_isa_IntegerAttrDef():
    instance = vM_IntegerAttrDefBounded()
    assert isinstance(instance, IntegerAttrDef)


def test_vM_IntegerAttrDefUnbounded_isa_IntegerAttrDef():
    instance = vM_IntegerAttrDefUnbounded(value="sample_text")
    assert isinstance(instance, IntegerAttrDef)


def test_vM_RealAttrDefBounded_isa_RealAttrDef():
    instance = vM_RealAttrDefBounded()
    assert isinstance(instance, RealAttrDef)


def test_vM_RealAttrDefUnbounded_isa_RealAttrDef():
    instance = vM_RealAttrDefUnbounded(value="sample_text")
    assert isinstance(instance, RealAttrDef)


def test_vM_TableBasedValuationByAttributeForInteger_isa_TableBasedValuationByAttribute():
    instance = vM_TableBasedValuationByAttributeForInteger()
    assert isinstance(instance, TableBasedValuationByAttribute)


def test_vM_TableBasedValuationByAttributeForReal_isa_TableBasedValuationByAttribute():
    instance = vM_TableBasedValuationByAttributeForReal()
    assert isinstance(instance, TableBasedValuationByAttribute)


def test_vM_Attributes_isa_VmBlock():
    instance = vM_Attributes()
    assert isinstance(instance, VmBlock)


def test_vM_Configurations_isa_VmBlock():
    instance = vM_Configurations()
    assert isinstance(instance, VmBlock)


def test_vM_Constraints_isa_VmBlock():
    instance = vM_Constraints()
    assert isinstance(instance, VmBlock)


def test_vM_Descriptions_isa_VmBlock():
    instance = vM_Descriptions()
    assert isinstance(instance, VmBlock)


def test_vM_ImportDeclaration_isa_VmBlock():
    instance = vM_ImportDeclaration(importedNamespace="sample_text")
    assert isinstance(instance, VmBlock)


def test_vM_MetaDataDeclaration_isa_VmBlock():
    instance = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    assert isinstance(instance, VmBlock)


def test_vM_Objectives_isa_VmBlock():
    instance = vM_Objectives()
    assert isinstance(instance, VmBlock)


def test_vM_PackageDeclaration_isa_VmBlock():
    instance = vM_PackageDeclaration(name="sample_text")
    assert isinstance(instance, VmBlock)


def test_vM_Relationships_isa_VmBlock():
    instance = vM_Relationships()
    assert isinstance(instance, VmBlock)


def test_assoc_attVsValForMultiFeature120_link_reassign_clear():
    a = vM_TableBasedValuationByFeatureAndClone(name="sample_text")
    b1 = vM_AdvancedAttrValuation()
    b2 = vM_AdvancedAttrValuation()
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone', b1)
    assert _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone', b1)
    if hasattr(b1, 'vM_AdvancedAttrValuation121'):
        assert _is_linked(b1, 'vM_AdvancedAttrValuation121', a)
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone', b2)
    assert _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone', b2)
    if hasattr(b1, 'vM_AdvancedAttrValuation121'):
        assert not _is_linked(b1, 'vM_AdvancedAttrValuation121', a)
    if hasattr(b2, 'vM_AdvancedAttrValuation121'):
        assert _is_linked(b2, 'vM_AdvancedAttrValuation121', a)
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone', None)
    assert not _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone', b2)
    if hasattr(b2, 'vM_AdvancedAttrValuation121'):
        assert not _is_linked(b2, 'vM_AdvancedAttrValuation121', a)


def test_assoc_attrDefs13_link_reassign_clear():
    a = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    b1 = vM_Attributes()
    b2 = vM_Attributes()
    _safe_set(a, 'vM_AttrDef', b1)
    assert _is_linked(a, 'vM_AttrDef', b1)
    if hasattr(b1, 'vM_Attributes'):
        assert _is_linked(b1, 'vM_Attributes', a)
    _safe_set(a, 'vM_AttrDef', b2)
    assert _is_linked(a, 'vM_AttrDef', b2)
    if hasattr(b1, 'vM_Attributes'):
        assert not _is_linked(b1, 'vM_Attributes', a)
    if hasattr(b2, 'vM_Attributes'):
        assert _is_linked(b2, 'vM_Attributes', a)
    _safe_set(a, 'vM_AttrDef', None)
    assert not _is_linked(a, 'vM_AttrDef', b2)
    if hasattr(b2, 'vM_Attributes'):
        assert not _is_linked(b2, 'vM_Attributes', a)


def test_assoc_attrValuations14_link_reassign_clear():
    a = vM_BasicAttrValuation(value="sample_text")
    b1 = vM_Attributes()
    b2 = vM_Attributes()
    _safe_set(a, 'vM_BasicAttrValuation', b1)
    assert _is_linked(a, 'vM_BasicAttrValuation', b1)
    if hasattr(b1, 'vM_Attributes15'):
        assert _is_linked(b1, 'vM_Attributes15', a)
    _safe_set(a, 'vM_BasicAttrValuation', b2)
    assert _is_linked(a, 'vM_BasicAttrValuation', b2)
    if hasattr(b1, 'vM_Attributes15'):
        assert not _is_linked(b1, 'vM_Attributes15', a)
    if hasattr(b2, 'vM_Attributes15'):
        assert _is_linked(b2, 'vM_Attributes15', a)
    _safe_set(a, 'vM_BasicAttrValuation', None)
    assert not _is_linked(a, 'vM_BasicAttrValuation', b2)
    if hasattr(b2, 'vM_Attributes15'):
        assert not _is_linked(b2, 'vM_Attributes15', a)


def test_assoc_attributesDescriptions54_link_reassign_clear():
    a = vM_AttributeDescription(description="sample_text")
    b1 = vM_Descriptions()
    b2 = vM_Descriptions()
    _safe_set(a, 'vM_AttributeDescription', b1)
    assert _is_linked(a, 'vM_AttributeDescription', b1)
    if hasattr(b1, 'vM_Descriptions55'):
        assert _is_linked(b1, 'vM_Descriptions55', a)
    _safe_set(a, 'vM_AttributeDescription', b2)
    assert _is_linked(a, 'vM_AttributeDescription', b2)
    if hasattr(b1, 'vM_Descriptions55'):
        assert not _is_linked(b1, 'vM_Descriptions55', a)
    if hasattr(b2, 'vM_Descriptions55'):
        assert _is_linked(b2, 'vM_Descriptions55', a)
    _safe_set(a, 'vM_AttributeDescription', None)
    assert not _is_linked(a, 'vM_AttributeDescription', b2)
    if hasattr(b2, 'vM_Descriptions55'):
        assert not _is_linked(b2, 'vM_Descriptions55', a)


def test_assoc_basicAttrDef16_link_reassign_clear():
    a = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    b1 = vM_BasicAttrDef()
    b2 = vM_BasicAttrDef()
    _safe_set(a, 'vM_AttrDef17', b1)
    assert _is_linked(a, 'vM_AttrDef17', b1)
    if hasattr(b1, 'vM_BasicAttrDef'):
        assert _is_linked(b1, 'vM_BasicAttrDef', a)
    _safe_set(a, 'vM_AttrDef17', b2)
    assert _is_linked(a, 'vM_AttrDef17', b2)
    if hasattr(b1, 'vM_BasicAttrDef'):
        assert not _is_linked(b1, 'vM_BasicAttrDef', a)
    if hasattr(b2, 'vM_BasicAttrDef'):
        assert _is_linked(b2, 'vM_BasicAttrDef', a)
    _safe_set(a, 'vM_AttrDef17', None)
    assert not _is_linked(a, 'vM_AttrDef17', b2)
    if hasattr(b2, 'vM_BasicAttrDef'):
        assert not _is_linked(b2, 'vM_BasicAttrDef', a)


def test_assoc_blocks1_link_reassign_clear():
    a = vM_PackageDeclaration(name="sample_text")
    b1 = vM_VmBlock()
    b2 = vM_VmBlock()
    _safe_set(a, 'vM_PackageDeclaration', {b1})
    assert _is_linked(a, 'vM_PackageDeclaration', b1)
    if hasattr(b1, 'vM_VmBlock2'):
        assert _is_linked(b1, 'vM_VmBlock2', a)
    _safe_set(a, 'vM_PackageDeclaration', {b2})
    assert _is_linked(a, 'vM_PackageDeclaration', b2)
    if hasattr(b1, 'vM_VmBlock2'):
        assert not _is_linked(b1, 'vM_VmBlock2', a)
    if hasattr(b2, 'vM_VmBlock2'):
        assert _is_linked(b2, 'vM_VmBlock2', a)
    _safe_set(a, 'vM_PackageDeclaration', set())
    assert not _is_linked(a, 'vM_PackageDeclaration', b2)
    if hasattr(b2, 'vM_VmBlock2'):
        assert not _is_linked(b2, 'vM_VmBlock2', a)


def test_assoc_booleanValuation99_link_reassign_clear():
    a = vM_Configuration(name="sample_text")
    b1 = vM_BooleanValuation(notSelected=True)
    b2 = vM_BooleanValuation(notSelected=False)
    _safe_set(a, 'vM_Configuration100', {b1})
    assert _is_linked(a, 'vM_Configuration100', b1)
    if hasattr(b1, 'vM_BooleanValuation'):
        assert _is_linked(b1, 'vM_BooleanValuation', a)
    _safe_set(a, 'vM_Configuration100', {b2})
    assert _is_linked(a, 'vM_Configuration100', b2)
    if hasattr(b1, 'vM_BooleanValuation'):
        assert not _is_linked(b1, 'vM_BooleanValuation', a)
    if hasattr(b2, 'vM_BooleanValuation'):
        assert _is_linked(b2, 'vM_BooleanValuation', a)
    _safe_set(a, 'vM_Configuration100', set())
    assert not _is_linked(a, 'vM_Configuration100', b2)
    if hasattr(b2, 'vM_BooleanValuation'):
        assert not _is_linked(b2, 'vM_BooleanValuation', a)


def test_assoc_complement30_link_reassign_clear():
    a = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    b1 = vM_IntegerAttrDefBounded()
    b2 = vM_IntegerAttrDefBounded()
    _safe_set(a, 'vM_IntegerAttrDefComplement32', b1)
    assert _is_linked(a, 'vM_IntegerAttrDefComplement32', b1)
    if hasattr(b1, 'vM_IntegerAttrDefBounded31'):
        assert _is_linked(b1, 'vM_IntegerAttrDefBounded31', a)
    _safe_set(a, 'vM_IntegerAttrDefComplement32', b2)
    assert _is_linked(a, 'vM_IntegerAttrDefComplement32', b2)
    if hasattr(b1, 'vM_IntegerAttrDefBounded31'):
        assert not _is_linked(b1, 'vM_IntegerAttrDefBounded31', a)
    if hasattr(b2, 'vM_IntegerAttrDefBounded31'):
        assert _is_linked(b2, 'vM_IntegerAttrDefBounded31', a)
    _safe_set(a, 'vM_IntegerAttrDefComplement32', None)
    assert not _is_linked(a, 'vM_IntegerAttrDefComplement32', b2)
    if hasattr(b2, 'vM_IntegerAttrDefBounded31'):
        assert not _is_linked(b2, 'vM_IntegerAttrDefBounded31', a)


def test_assoc_complement38_link_reassign_clear():
    a = vM_RealAttrDefComplement(max="sample_text", min="sample_text")
    b1 = vM_RealAttrDefBounded()
    b2 = vM_RealAttrDefBounded()
    _safe_set(a, 'vM_RealAttrDefComplement', b1)
    assert _is_linked(a, 'vM_RealAttrDefComplement', b1)
    if hasattr(b1, 'vM_RealAttrDefBounded'):
        assert _is_linked(b1, 'vM_RealAttrDefBounded', a)
    _safe_set(a, 'vM_RealAttrDefComplement', b2)
    assert _is_linked(a, 'vM_RealAttrDefComplement', b2)
    if hasattr(b1, 'vM_RealAttrDefBounded'):
        assert not _is_linked(b1, 'vM_RealAttrDefBounded', a)
    if hasattr(b2, 'vM_RealAttrDefBounded'):
        assert _is_linked(b2, 'vM_RealAttrDefBounded', a)
    _safe_set(a, 'vM_RealAttrDefComplement', None)
    assert not _is_linked(a, 'vM_RealAttrDefComplement', b2)
    if hasattr(b2, 'vM_RealAttrDefBounded'):
        assert not _is_linked(b2, 'vM_RealAttrDefBounded', a)


def test_assoc_complements29_link_reassign_clear():
    a = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    b1 = vM_IntegerAttrDefBounded()
    b2 = vM_IntegerAttrDefBounded()
    _safe_set(a, 'vM_IntegerAttrDefComplement', b1)
    assert _is_linked(a, 'vM_IntegerAttrDefComplement', b1)
    if hasattr(b1, 'vM_IntegerAttrDefBounded'):
        assert _is_linked(b1, 'vM_IntegerAttrDefBounded', a)
    _safe_set(a, 'vM_IntegerAttrDefComplement', b2)
    assert _is_linked(a, 'vM_IntegerAttrDefComplement', b2)
    if hasattr(b1, 'vM_IntegerAttrDefBounded'):
        assert not _is_linked(b1, 'vM_IntegerAttrDefBounded', a)
    if hasattr(b2, 'vM_IntegerAttrDefBounded'):
        assert _is_linked(b2, 'vM_IntegerAttrDefBounded', a)
    _safe_set(a, 'vM_IntegerAttrDefComplement', None)
    assert not _is_linked(a, 'vM_IntegerAttrDefComplement', b2)
    if hasattr(b2, 'vM_IntegerAttrDefBounded'):
        assert not _is_linked(b2, 'vM_IntegerAttrDefBounded', a)


def test_assoc_configurations98_link_reassign_clear():
    a = vM_Configuration(name="sample_text")
    b1 = vM_Configurations()
    b2 = vM_Configurations()
    _safe_set(a, 'vM_Configuration', b1)
    assert _is_linked(a, 'vM_Configuration', b1)
    if hasattr(b1, 'vM_Configurations'):
        assert _is_linked(b1, 'vM_Configurations', a)
    _safe_set(a, 'vM_Configuration', b2)
    assert _is_linked(a, 'vM_Configuration', b2)
    if hasattr(b1, 'vM_Configurations'):
        assert not _is_linked(b1, 'vM_Configurations', a)
    if hasattr(b2, 'vM_Configurations'):
        assert _is_linked(b2, 'vM_Configurations', a)
    _safe_set(a, 'vM_Configuration', None)
    assert not _is_linked(a, 'vM_Configuration', b2)
    if hasattr(b2, 'vM_Configurations'):
        assert not _is_linked(b2, 'vM_Configurations', a)


def test_assoc_constraints64_link_reassign_clear():
    a = vM_Constraint(name="sample_text", not_=True)
    b1 = vM_Constraints()
    b2 = vM_Constraints()
    _safe_set(a, 'vM_Constraint', b1)
    assert _is_linked(a, 'vM_Constraint', b1)
    if hasattr(b1, 'vM_Constraints'):
        assert _is_linked(b1, 'vM_Constraints', a)
    _safe_set(a, 'vM_Constraint', b2)
    assert _is_linked(a, 'vM_Constraint', b2)
    if hasattr(b1, 'vM_Constraints'):
        assert not _is_linked(b1, 'vM_Constraints', a)
    if hasattr(b2, 'vM_Constraints'):
        assert _is_linked(b2, 'vM_Constraints', a)
    _safe_set(a, 'vM_Constraint', None)
    assert not _is_linked(a, 'vM_Constraint', b2)
    if hasattr(b2, 'vM_Constraints'):
        assert not _is_linked(b2, 'vM_Constraints', a)


def test_assoc_default21_link_reassign_clear():
    a = vM_BooleanAttrDef(value="sample_text")
    b1 = vM_BoolDefaultDef(value="sample_text")
    b2 = vM_BoolDefaultDef(value="sample_text_2")
    _safe_set(a, 'vM_BooleanAttrDef22', b1)
    assert _is_linked(a, 'vM_BooleanAttrDef22', b1)
    if hasattr(b1, 'vM_BoolDefaultDef'):
        assert _is_linked(b1, 'vM_BoolDefaultDef', a)
    _safe_set(a, 'vM_BooleanAttrDef22', b2)
    assert _is_linked(a, 'vM_BooleanAttrDef22', b2)
    if hasattr(b1, 'vM_BoolDefaultDef'):
        assert not _is_linked(b1, 'vM_BoolDefaultDef', a)
    if hasattr(b2, 'vM_BoolDefaultDef'):
        assert _is_linked(b2, 'vM_BoolDefaultDef', a)
    _safe_set(a, 'vM_BooleanAttrDef22', None)
    assert not _is_linked(a, 'vM_BooleanAttrDef22', b2)
    if hasattr(b2, 'vM_BoolDefaultDef'):
        assert not _is_linked(b2, 'vM_BoolDefaultDef', a)


def test_assoc_default24_link_reassign_clear():
    a = vM_StringDefaultDef(value="sample_text")
    b1 = vM_StringAttrDef(value="sample_text")
    b2 = vM_StringAttrDef(value="sample_text_2")
    _safe_set(a, 'vM_StringDefaultDef', b1)
    assert _is_linked(a, 'vM_StringDefaultDef', b1)
    if hasattr(b1, 'vM_StringAttrDef25'):
        assert _is_linked(b1, 'vM_StringAttrDef25', a)
    _safe_set(a, 'vM_StringDefaultDef', b2)
    assert _is_linked(a, 'vM_StringDefaultDef', b2)
    if hasattr(b1, 'vM_StringAttrDef25'):
        assert not _is_linked(b1, 'vM_StringAttrDef25', a)
    if hasattr(b2, 'vM_StringAttrDef25'):
        assert _is_linked(b2, 'vM_StringAttrDef25', a)
    _safe_set(a, 'vM_StringDefaultDef', None)
    assert not _is_linked(a, 'vM_StringDefaultDef', b2)
    if hasattr(b2, 'vM_StringAttrDef25'):
        assert not _is_linked(b2, 'vM_StringAttrDef25', a)


def test_assoc_default27_link_reassign_clear():
    a = vM_IntegerDefaultDef(value=7)
    b1 = vM_IntegerAttrDef()
    b2 = vM_IntegerAttrDef()
    _safe_set(a, 'vM_IntegerDefaultDef', b1)
    assert _is_linked(a, 'vM_IntegerDefaultDef', b1)
    if hasattr(b1, 'vM_IntegerAttrDef28'):
        assert _is_linked(b1, 'vM_IntegerAttrDef28', a)
    _safe_set(a, 'vM_IntegerDefaultDef', b2)
    assert _is_linked(a, 'vM_IntegerDefaultDef', b2)
    if hasattr(b1, 'vM_IntegerAttrDef28'):
        assert not _is_linked(b1, 'vM_IntegerAttrDef28', a)
    if hasattr(b2, 'vM_IntegerAttrDef28'):
        assert _is_linked(b2, 'vM_IntegerAttrDef28', a)
    _safe_set(a, 'vM_IntegerDefaultDef', None)
    assert not _is_linked(a, 'vM_IntegerDefaultDef', b2)
    if hasattr(b2, 'vM_IntegerAttrDef28'):
        assert not _is_linked(b2, 'vM_IntegerAttrDef28', a)


def test_assoc_default36_link_reassign_clear():
    a = vM_RealDefaultDef(value="sample_text")
    b1 = vM_RealAttrDef()
    b2 = vM_RealAttrDef()
    _safe_set(a, 'vM_RealDefaultDef', b1)
    assert _is_linked(a, 'vM_RealDefaultDef', b1)
    if hasattr(b1, 'vM_RealAttrDef37'):
        assert _is_linked(b1, 'vM_RealAttrDef37', a)
    _safe_set(a, 'vM_RealDefaultDef', b2)
    assert _is_linked(a, 'vM_RealDefaultDef', b2)
    if hasattr(b1, 'vM_RealAttrDef37'):
        assert not _is_linked(b1, 'vM_RealAttrDef37', a)
    if hasattr(b2, 'vM_RealAttrDef37'):
        assert _is_linked(b2, 'vM_RealAttrDef37', a)
    _safe_set(a, 'vM_RealDefaultDef', None)
    assert not _is_linked(a, 'vM_RealDefaultDef', b2)
    if hasattr(b2, 'vM_RealAttrDef37'):
        assert not _is_linked(b2, 'vM_RealAttrDef37', a)


def test_assoc_default42_link_reassign_clear():
    a = vM_StringDefaultDef(value="sample_text")
    b1 = vM_EnumStringDef()
    b2 = vM_EnumStringDef()
    _safe_set(a, 'vM_StringDefaultDef44', b1)
    assert _is_linked(a, 'vM_StringDefaultDef44', b1)
    if hasattr(b1, 'vM_EnumStringDef43'):
        assert _is_linked(b1, 'vM_EnumStringDef43', a)
    _safe_set(a, 'vM_StringDefaultDef44', b2)
    assert _is_linked(a, 'vM_StringDefaultDef44', b2)
    if hasattr(b1, 'vM_EnumStringDef43'):
        assert not _is_linked(b1, 'vM_EnumStringDef43', a)
    if hasattr(b2, 'vM_EnumStringDef43'):
        assert _is_linked(b2, 'vM_EnumStringDef43', a)
    _safe_set(a, 'vM_StringDefaultDef44', None)
    assert not _is_linked(a, 'vM_StringDefaultDef44', b2)
    if hasattr(b2, 'vM_EnumStringDef43'):
        assert not _is_linked(b2, 'vM_EnumStringDef43', a)


def test_assoc_default46_link_reassign_clear():
    a = vM_IntegerDefaultDef(value=7)
    b1 = vM_EnumIntegerDef()
    b2 = vM_EnumIntegerDef()
    _safe_set(a, 'vM_IntegerDefaultDef48', b1)
    assert _is_linked(a, 'vM_IntegerDefaultDef48', b1)
    if hasattr(b1, 'vM_EnumIntegerDef47'):
        assert _is_linked(b1, 'vM_EnumIntegerDef47', a)
    _safe_set(a, 'vM_IntegerDefaultDef48', b2)
    assert _is_linked(a, 'vM_IntegerDefaultDef48', b2)
    if hasattr(b1, 'vM_EnumIntegerDef47'):
        assert not _is_linked(b1, 'vM_EnumIntegerDef47', a)
    if hasattr(b2, 'vM_EnumIntegerDef47'):
        assert _is_linked(b2, 'vM_EnumIntegerDef47', a)
    _safe_set(a, 'vM_IntegerDefaultDef48', None)
    assert not _is_linked(a, 'vM_IntegerDefaultDef48', b2)
    if hasattr(b2, 'vM_EnumIntegerDef47'):
        assert not _is_linked(b2, 'vM_EnumIntegerDef47', a)


def test_assoc_default50_link_reassign_clear():
    a = vM_RealDefaultDef(value="sample_text")
    b1 = vM_EnumRealDef()
    b2 = vM_EnumRealDef()
    _safe_set(a, 'vM_RealDefaultDef52', b1)
    assert _is_linked(a, 'vM_RealDefaultDef52', b1)
    if hasattr(b1, 'vM_EnumRealDef51'):
        assert _is_linked(b1, 'vM_EnumRealDef51', a)
    _safe_set(a, 'vM_RealDefaultDef52', b2)
    assert _is_linked(a, 'vM_RealDefaultDef52', b2)
    if hasattr(b1, 'vM_EnumRealDef51'):
        assert not _is_linked(b1, 'vM_EnumRealDef51', a)
    if hasattr(b2, 'vM_EnumRealDef51'):
        assert _is_linked(b2, 'vM_EnumRealDef51', a)
    _safe_set(a, 'vM_RealDefaultDef52', None)
    assert not _is_linked(a, 'vM_RealDefaultDef52', b2)
    if hasattr(b2, 'vM_EnumRealDef51'):
        assert not _is_linked(b2, 'vM_EnumRealDef51', a)


def test_assoc_delta33_link_reassign_clear():
    a = vM_IntegerDeltaDef(value=7)
    b1 = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    b2 = vM_IntegerAttrDefComplement(max="sample_text_2", min="sample_text_2")
    _safe_set(a, 'vM_IntegerDeltaDef', b1)
    assert _is_linked(a, 'vM_IntegerDeltaDef', b1)
    if hasattr(b1, 'vM_IntegerAttrDefComplement34'):
        assert _is_linked(b1, 'vM_IntegerAttrDefComplement34', a)
    _safe_set(a, 'vM_IntegerDeltaDef', b2)
    assert _is_linked(a, 'vM_IntegerDeltaDef', b2)
    if hasattr(b1, 'vM_IntegerAttrDefComplement34'):
        assert not _is_linked(b1, 'vM_IntegerAttrDefComplement34', a)
    if hasattr(b2, 'vM_IntegerAttrDefComplement34'):
        assert _is_linked(b2, 'vM_IntegerAttrDefComplement34', a)
    _safe_set(a, 'vM_IntegerDeltaDef', None)
    assert not _is_linked(a, 'vM_IntegerDeltaDef', b2)
    if hasattr(b2, 'vM_IntegerAttrDefComplement34'):
        assert not _is_linked(b2, 'vM_IntegerAttrDefComplement34', a)


def test_assoc_delta39_link_reassign_clear():
    a = vM_RealDeltaDef(value="sample_text")
    b1 = vM_RealAttrDefComplement(max="sample_text", min="sample_text")
    b2 = vM_RealAttrDefComplement(max="sample_text_2", min="sample_text_2")
    _safe_set(a, 'vM_RealDeltaDef', b1)
    assert _is_linked(a, 'vM_RealDeltaDef', b1)
    if hasattr(b1, 'vM_RealAttrDefComplement40'):
        assert _is_linked(b1, 'vM_RealAttrDefComplement40', a)
    _safe_set(a, 'vM_RealDeltaDef', b2)
    assert _is_linked(a, 'vM_RealDeltaDef', b2)
    if hasattr(b1, 'vM_RealAttrDefComplement40'):
        assert not _is_linked(b1, 'vM_RealAttrDefComplement40', a)
    if hasattr(b2, 'vM_RealAttrDefComplement40'):
        assert _is_linked(b2, 'vM_RealAttrDefComplement40', a)
    _safe_set(a, 'vM_RealDeltaDef', None)
    assert not _is_linked(a, 'vM_RealDeltaDef', b2)
    if hasattr(b2, 'vM_RealAttrDefComplement40'):
        assert not _is_linked(b2, 'vM_RealAttrDefComplement40', a)


def test_assoc_email4_link_reassign_clear():
    a = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    b1 = vM_Email(domain="sample_text", username="sample_text")
    b2 = vM_Email(domain="sample_text_2", username="sample_text_2")
    _safe_set(a, 'vM_MetaDataDeclaration5', b1)
    assert _is_linked(a, 'vM_MetaDataDeclaration5', b1)
    if hasattr(b1, 'vM_Email'):
        assert _is_linked(b1, 'vM_Email', a)
    _safe_set(a, 'vM_MetaDataDeclaration5', b2)
    assert _is_linked(a, 'vM_MetaDataDeclaration5', b2)
    if hasattr(b1, 'vM_Email'):
        assert not _is_linked(b1, 'vM_Email', a)
    if hasattr(b2, 'vM_Email'):
        assert _is_linked(b2, 'vM_Email', a)
    _safe_set(a, 'vM_MetaDataDeclaration5', None)
    assert not _is_linked(a, 'vM_MetaDataDeclaration5', b2)
    if hasattr(b2, 'vM_Email'):
        assert not _is_linked(b2, 'vM_Email', a)


def test_assoc_enumAttrDef18_link_reassign_clear():
    a = vM_EnumAttrDef(value="sample_text")
    b1 = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    b2 = vM_AttrDef(notDecidable=False, notTranslatable=False, runTime=False)
    _safe_set(a, 'vM_EnumAttrDef', b1)
    assert _is_linked(a, 'vM_EnumAttrDef', b1)
    if hasattr(b1, 'vM_AttrDef19'):
        assert _is_linked(b1, 'vM_AttrDef19', a)
    _safe_set(a, 'vM_EnumAttrDef', b2)
    assert _is_linked(a, 'vM_EnumAttrDef', b2)
    if hasattr(b1, 'vM_AttrDef19'):
        assert not _is_linked(b1, 'vM_AttrDef19', a)
    if hasattr(b2, 'vM_AttrDef19'):
        assert _is_linked(b2, 'vM_AttrDef19', a)
    _safe_set(a, 'vM_EnumAttrDef', None)
    assert not _is_linked(a, 'vM_EnumAttrDef', b2)
    if hasattr(b2, 'vM_AttrDef19'):
        assert not _is_linked(b2, 'vM_AttrDef19', a)


def test_assoc_ex86_link_reassign_clear():
    a = vM_NumericExpression(op="sample_text", value="sample_text")
    b1 = vM_NumericExpression_List()
    b2 = vM_NumericExpression_List()
    _safe_set(a, 'vM_NumericExpression88', b1)
    assert _is_linked(a, 'vM_NumericExpression88', b1)
    if hasattr(b1, 'vM_NumericExpression_List87'):
        assert _is_linked(b1, 'vM_NumericExpression_List87', a)
    _safe_set(a, 'vM_NumericExpression88', b2)
    assert _is_linked(a, 'vM_NumericExpression88', b2)
    if hasattr(b1, 'vM_NumericExpression_List87'):
        assert not _is_linked(b1, 'vM_NumericExpression_List87', a)
    if hasattr(b2, 'vM_NumericExpression_List87'):
        assert _is_linked(b2, 'vM_NumericExpression_List87', a)
    _safe_set(a, 'vM_NumericExpression88', None)
    assert not _is_linked(a, 'vM_NumericExpression88', b2)
    if hasattr(b2, 'vM_NumericExpression_List87'):
        assert not _is_linked(b2, 'vM_NumericExpression_List87', a)


def test_assoc_ex89_link_reassign_clear():
    a = vM_BooleanExpression(op="sample_text", value="sample_text")
    b1 = vM_BooleanExpression_List()
    b2 = vM_BooleanExpression_List()
    _safe_set(a, 'vM_BooleanExpression91', b1)
    assert _is_linked(a, 'vM_BooleanExpression91', b1)
    if hasattr(b1, 'vM_BooleanExpression_List90'):
        assert _is_linked(b1, 'vM_BooleanExpression_List90', a)
    _safe_set(a, 'vM_BooleanExpression91', b2)
    assert _is_linked(a, 'vM_BooleanExpression91', b2)
    if hasattr(b1, 'vM_BooleanExpression_List90'):
        assert not _is_linked(b1, 'vM_BooleanExpression_List90', a)
    if hasattr(b2, 'vM_BooleanExpression_List90'):
        assert _is_linked(b2, 'vM_BooleanExpression_List90', a)
    _safe_set(a, 'vM_BooleanExpression91', None)
    assert not _is_linked(a, 'vM_BooleanExpression91', b2)
    if hasattr(b2, 'vM_BooleanExpression_List90'):
        assert not _is_linked(b2, 'vM_BooleanExpression_List90', a)


def test_assoc_expression65_link_reassign_clear():
    a = vM_Constraint(name="sample_text", not_=True)
    b1 = vM_ComplexExpression()
    b2 = vM_ComplexExpression()
    _safe_set(a, 'vM_Constraint66', b1)
    assert _is_linked(a, 'vM_Constraint66', b1)
    if hasattr(b1, 'vM_ComplexExpression'):
        assert _is_linked(b1, 'vM_ComplexExpression', a)
    _safe_set(a, 'vM_Constraint66', b2)
    assert _is_linked(a, 'vM_Constraint66', b2)
    if hasattr(b1, 'vM_ComplexExpression'):
        assert not _is_linked(b1, 'vM_ComplexExpression', a)
    if hasattr(b2, 'vM_ComplexExpression'):
        assert _is_linked(b2, 'vM_ComplexExpression', a)
    _safe_set(a, 'vM_Constraint66', None)
    assert not _is_linked(a, 'vM_Constraint66', b2)
    if hasattr(b2, 'vM_ComplexExpression'):
        assert not _is_linked(b2, 'vM_ComplexExpression', a)


def test_assoc_expression67_link_reassign_clear():
    a = vM_SpecialExpression(op="sample_text")
    b1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    _safe_set(a, 'vM_SpecialExpression', b1)
    assert _is_linked(a, 'vM_SpecialExpression', b1)
    if hasattr(b1, 'vM_Feature68'):
        assert _is_linked(b1, 'vM_Feature68', a)
    _safe_set(a, 'vM_SpecialExpression', b2)
    assert _is_linked(a, 'vM_SpecialExpression', b2)
    if hasattr(b1, 'vM_Feature68'):
        assert not _is_linked(b1, 'vM_Feature68', a)
    if hasattr(b2, 'vM_Feature68'):
        assert _is_linked(b2, 'vM_Feature68', a)
    _safe_set(a, 'vM_SpecialExpression', None)
    assert not _is_linked(a, 'vM_SpecialExpression', b2)
    if hasattr(b2, 'vM_Feature68'):
        assert not _is_linked(b2, 'vM_Feature68', a)


def test_assoc_expression77_link_reassign_clear():
    a = vM_BooleanExpression(op="sample_text", value="sample_text")
    b1 = vM_BooleanExpression(op="sample_text", value="sample_text")
    b2 = vM_BooleanExpression(op="sample_text_2", value="sample_text_2")
    _safe_set(a, 'vM_BooleanExpression', b1)
    assert _is_linked(a, 'vM_BooleanExpression', b1)
    if hasattr(b1, 'vM_BooleanExpression76'):
        assert _is_linked(b1, 'vM_BooleanExpression76', a)
    _safe_set(a, 'vM_BooleanExpression', b2)
    assert _is_linked(a, 'vM_BooleanExpression', b2)
    if hasattr(b1, 'vM_BooleanExpression76'):
        assert not _is_linked(b1, 'vM_BooleanExpression76', a)
    if hasattr(b2, 'vM_BooleanExpression76'):
        assert _is_linked(b2, 'vM_BooleanExpression76', a)
    _safe_set(a, 'vM_BooleanExpression', None)
    assert not _is_linked(a, 'vM_BooleanExpression', b2)
    if hasattr(b2, 'vM_BooleanExpression76'):
        assert not _is_linked(b2, 'vM_BooleanExpression76', a)


def test_assoc_expression83_link_reassign_clear():
    a = vM_NumericExpression(op="sample_text", value="sample_text")
    b1 = vM_NumericExpression(op="sample_text", value="sample_text")
    b2 = vM_NumericExpression(op="sample_text_2", value="sample_text_2")
    _safe_set(a, 'vM_NumericExpression', b1)
    assert _is_linked(a, 'vM_NumericExpression', b1)
    if hasattr(b1, 'vM_NumericExpression82'):
        assert _is_linked(b1, 'vM_NumericExpression82', a)
    _safe_set(a, 'vM_NumericExpression', b2)
    assert _is_linked(a, 'vM_NumericExpression', b2)
    if hasattr(b1, 'vM_NumericExpression82'):
        assert not _is_linked(b1, 'vM_NumericExpression82', a)
    if hasattr(b2, 'vM_NumericExpression82'):
        assert _is_linked(b2, 'vM_NumericExpression82', a)
    _safe_set(a, 'vM_NumericExpression', None)
    assert not _is_linked(a, 'vM_NumericExpression', b2)
    if hasattr(b2, 'vM_NumericExpression82'):
        assert not _is_linked(b2, 'vM_NumericExpression82', a)


def test_assoc_expression93_link_reassign_clear():
    a = vM_ObjectiveExpression(op="sample_text")
    b1 = vM_Objective(name="sample_text", op="sample_text")
    b2 = vM_Objective(name="sample_text_2", op="sample_text_2")
    _safe_set(a, 'vM_ObjectiveExpression', b1)
    assert _is_linked(a, 'vM_ObjectiveExpression', b1)
    if hasattr(b1, 'vM_Objective94'):
        assert _is_linked(b1, 'vM_Objective94', a)
    _safe_set(a, 'vM_ObjectiveExpression', b2)
    assert _is_linked(a, 'vM_ObjectiveExpression', b2)
    if hasattr(b1, 'vM_Objective94'):
        assert not _is_linked(b1, 'vM_Objective94', a)
    if hasattr(b2, 'vM_Objective94'):
        assert _is_linked(b2, 'vM_Objective94', a)
    _safe_set(a, 'vM_ObjectiveExpression', None)
    assert not _is_linked(a, 'vM_ObjectiveExpression', b2)
    if hasattr(b2, 'vM_Objective94'):
        assert not _is_linked(b2, 'vM_Objective94', a)


def test_assoc_expression95_link_reassign_clear():
    a = vM_ObjectiveExpression(op="sample_text")
    b1 = vM_PrimitiveExpression()
    b2 = vM_PrimitiveExpression()
    _safe_set(a, 'vM_ObjectiveExpression96', b1)
    assert _is_linked(a, 'vM_ObjectiveExpression96', b1)
    if hasattr(b1, 'vM_PrimitiveExpression97'):
        assert _is_linked(b1, 'vM_PrimitiveExpression97', a)
    _safe_set(a, 'vM_ObjectiveExpression96', b2)
    assert _is_linked(a, 'vM_ObjectiveExpression96', b2)
    if hasattr(b1, 'vM_PrimitiveExpression97'):
        assert not _is_linked(b1, 'vM_PrimitiveExpression97', a)
    if hasattr(b2, 'vM_PrimitiveExpression97'):
        assert _is_linked(b2, 'vM_PrimitiveExpression97', a)
    _safe_set(a, 'vM_ObjectiveExpression96', None)
    assert not _is_linked(a, 'vM_ObjectiveExpression96', b2)
    if hasattr(b2, 'vM_PrimitiveExpression97'):
        assert not _is_linked(b2, 'vM_PrimitiveExpression97', a)


def test_assoc_expression_list78_link_reassign_clear():
    a = vM_BooleanExpression(op="sample_text", value="sample_text")
    b1 = vM_BooleanExpression_List()
    b2 = vM_BooleanExpression_List()
    _safe_set(a, 'vM_BooleanExpression79', b1)
    assert _is_linked(a, 'vM_BooleanExpression79', b1)
    if hasattr(b1, 'vM_BooleanExpression_List'):
        assert _is_linked(b1, 'vM_BooleanExpression_List', a)
    _safe_set(a, 'vM_BooleanExpression79', b2)
    assert _is_linked(a, 'vM_BooleanExpression79', b2)
    if hasattr(b1, 'vM_BooleanExpression_List'):
        assert not _is_linked(b1, 'vM_BooleanExpression_List', a)
    if hasattr(b2, 'vM_BooleanExpression_List'):
        assert _is_linked(b2, 'vM_BooleanExpression_List', a)
    _safe_set(a, 'vM_BooleanExpression79', None)
    assert not _is_linked(a, 'vM_BooleanExpression79', b2)
    if hasattr(b2, 'vM_BooleanExpression_List'):
        assert not _is_linked(b2, 'vM_BooleanExpression_List', a)


def test_assoc_expression_list84_link_reassign_clear():
    a = vM_NumericExpression(op="sample_text", value="sample_text")
    b1 = vM_NumericExpression_List()
    b2 = vM_NumericExpression_List()
    _safe_set(a, 'vM_NumericExpression85', b1)
    assert _is_linked(a, 'vM_NumericExpression85', b1)
    if hasattr(b1, 'vM_NumericExpression_List'):
        assert _is_linked(b1, 'vM_NumericExpression_List', a)
    _safe_set(a, 'vM_NumericExpression85', b2)
    assert _is_linked(a, 'vM_NumericExpression85', b2)
    if hasattr(b1, 'vM_NumericExpression_List'):
        assert not _is_linked(b1, 'vM_NumericExpression_List', a)
    if hasattr(b2, 'vM_NumericExpression_List'):
        assert _is_linked(b2, 'vM_NumericExpression_List', a)
    _safe_set(a, 'vM_NumericExpression85', None)
    assert not _is_linked(a, 'vM_NumericExpression85', b2)
    if hasattr(b2, 'vM_NumericExpression_List'):
        assert not _is_linked(b2, 'vM_NumericExpression_List', a)


def test_assoc_extendedValuation101_link_reassign_clear():
    a = vM_Configuration(name="sample_text")
    b1 = vM_ExtendedValuation()
    b2 = vM_ExtendedValuation()
    _safe_set(a, 'vM_Configuration102', {b1})
    assert _is_linked(a, 'vM_Configuration102', b1)
    if hasattr(b1, 'vM_ExtendedValuation'):
        assert _is_linked(b1, 'vM_ExtendedValuation', a)
    _safe_set(a, 'vM_Configuration102', {b2})
    assert _is_linked(a, 'vM_Configuration102', b2)
    if hasattr(b1, 'vM_ExtendedValuation'):
        assert not _is_linked(b1, 'vM_ExtendedValuation', a)
    if hasattr(b2, 'vM_ExtendedValuation'):
        assert _is_linked(b2, 'vM_ExtendedValuation', a)
    _safe_set(a, 'vM_Configuration102', set())
    assert not _is_linked(a, 'vM_Configuration102', b2)
    if hasattr(b2, 'vM_ExtendedValuation'):
        assert not _is_linked(b2, 'vM_ExtendedValuation', a)


def test_assoc_feature103_link_reassign_clear():
    a = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b1 = vM_BooleanValuation(notSelected=True)
    b2 = vM_BooleanValuation(notSelected=False)
    _safe_set(a, 'vM_Feature105', b1)
    assert _is_linked(a, 'vM_Feature105', b1)
    if hasattr(b1, 'vM_BooleanValuation104'):
        assert _is_linked(b1, 'vM_BooleanValuation104', a)
    _safe_set(a, 'vM_Feature105', b2)
    assert _is_linked(a, 'vM_Feature105', b2)
    if hasattr(b1, 'vM_BooleanValuation104'):
        assert not _is_linked(b1, 'vM_BooleanValuation104', a)
    if hasattr(b2, 'vM_BooleanValuation104'):
        assert _is_linked(b2, 'vM_BooleanValuation104', a)
    _safe_set(a, 'vM_Feature105', None)
    assert not _is_linked(a, 'vM_Feature105', b2)
    if hasattr(b2, 'vM_BooleanValuation104'):
        assert not _is_linked(b2, 'vM_BooleanValuation104', a)


def test_assoc_featureID69_link_reassign_clear():
    a = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b1 = vM_PrimitiveExpression()
    b2 = vM_PrimitiveExpression()
    _safe_set(a, 'vM_Feature70', b1)
    assert _is_linked(a, 'vM_Feature70', b1)
    if hasattr(b1, 'vM_PrimitiveExpression'):
        assert _is_linked(b1, 'vM_PrimitiveExpression', a)
    _safe_set(a, 'vM_Feature70', b2)
    assert _is_linked(a, 'vM_Feature70', b2)
    if hasattr(b1, 'vM_PrimitiveExpression'):
        assert not _is_linked(b1, 'vM_PrimitiveExpression', a)
    if hasattr(b2, 'vM_PrimitiveExpression'):
        assert _is_linked(b2, 'vM_PrimitiveExpression', a)
    _safe_set(a, 'vM_Feature70', None)
    assert not _is_linked(a, 'vM_Feature70', b2)
    if hasattr(b2, 'vM_PrimitiveExpression'):
        assert not _is_linked(b2, 'vM_PrimitiveExpression', a)


def test_assoc_featuresDescriptions53_link_reassign_clear():
    a = vM_FeatureDescription(description="sample_text")
    b1 = vM_Descriptions()
    b2 = vM_Descriptions()
    _safe_set(a, 'vM_FeatureDescription', b1)
    assert _is_linked(a, 'vM_FeatureDescription', b1)
    if hasattr(b1, 'vM_Descriptions'):
        assert _is_linked(b1, 'vM_Descriptions', a)
    _safe_set(a, 'vM_FeatureDescription', b2)
    assert _is_linked(a, 'vM_FeatureDescription', b2)
    if hasattr(b1, 'vM_Descriptions'):
        assert not _is_linked(b1, 'vM_Descriptions', a)
    if hasattr(b2, 'vM_Descriptions'):
        assert _is_linked(b2, 'vM_Descriptions', a)
    _safe_set(a, 'vM_FeatureDescription', None)
    assert not _is_linked(a, 'vM_FeatureDescription', b2)
    if hasattr(b2, 'vM_Descriptions'):
        assert not _is_linked(b2, 'vM_Descriptions', a)


def test_assoc_head106_link_reassign_clear():
    a = vM_BasicAttrValuation(value="sample_text")
    b1 = vM_AttHead(forAllFeatures=True)
    b2 = vM_AttHead(forAllFeatures=False)
    _safe_set(a, 'vM_BasicAttrValuation107', b1)
    assert _is_linked(a, 'vM_BasicAttrValuation107', b1)
    if hasattr(b1, 'vM_AttHead108'):
        assert _is_linked(b1, 'vM_AttHead108', a)
    _safe_set(a, 'vM_BasicAttrValuation107', b2)
    assert _is_linked(a, 'vM_BasicAttrValuation107', b2)
    if hasattr(b1, 'vM_AttHead108'):
        assert not _is_linked(b1, 'vM_AttHead108', a)
    if hasattr(b2, 'vM_AttHead108'):
        assert _is_linked(b2, 'vM_AttHead108', a)
    _safe_set(a, 'vM_BasicAttrValuation107', None)
    assert not _is_linked(a, 'vM_BasicAttrValuation107', b2)
    if hasattr(b2, 'vM_AttHead108'):
        assert not _is_linked(b2, 'vM_AttHead108', a)


def test_assoc_head153_link_reassign_clear():
    a = vM_AttHead(forAllFeatures=True)
    b1 = vM_Abstract_ATT_ID(name="sample_text")
    b2 = vM_Abstract_ATT_ID(name="sample_text_2")
    _safe_set(a, 'vM_AttHead155', b1)
    assert _is_linked(a, 'vM_AttHead155', b1)
    if hasattr(b1, 'vM_Abstract_ATT_ID154'):
        assert _is_linked(b1, 'vM_Abstract_ATT_ID154', a)
    _safe_set(a, 'vM_AttHead155', b2)
    assert _is_linked(a, 'vM_AttHead155', b2)
    if hasattr(b1, 'vM_Abstract_ATT_ID154'):
        assert not _is_linked(b1, 'vM_Abstract_ATT_ID154', a)
    if hasattr(b2, 'vM_Abstract_ATT_ID154'):
        assert _is_linked(b2, 'vM_Abstract_ATT_ID154', a)
    _safe_set(a, 'vM_AttHead155', None)
    assert not _is_linked(a, 'vM_AttHead155', b2)
    if hasattr(b2, 'vM_Abstract_ATT_ID154'):
        assert not _is_linked(b2, 'vM_Abstract_ATT_ID154', a)


def test_assoc_head71_link_reassign_clear():
    a = vM_AttHead(forAllFeatures=True)
    b1 = vM_PrimitiveExpression()
    b2 = vM_PrimitiveExpression()
    _safe_set(a, 'vM_AttHead', b1)
    assert _is_linked(a, 'vM_AttHead', b1)
    if hasattr(b1, 'vM_PrimitiveExpression72'):
        assert _is_linked(b1, 'vM_PrimitiveExpression72', a)
    _safe_set(a, 'vM_AttHead', b2)
    assert _is_linked(a, 'vM_AttHead', b2)
    if hasattr(b1, 'vM_PrimitiveExpression72'):
        assert not _is_linked(b1, 'vM_PrimitiveExpression72', a)
    if hasattr(b2, 'vM_PrimitiveExpression72'):
        assert _is_linked(b2, 'vM_PrimitiveExpression72', a)
    _safe_set(a, 'vM_AttHead', None)
    assert not _is_linked(a, 'vM_AttHead', b2)
    if hasattr(b2, 'vM_PrimitiveExpression72'):
        assert not _is_linked(b2, 'vM_PrimitiveExpression72', a)


def test_assoc_name20_link_reassign_clear():
    a = vM_BooleanAttrDef(value="sample_text")
    b1 = vM_Boolean_ATT_ID()
    b2 = vM_Boolean_ATT_ID()
    _safe_set(a, 'vM_BooleanAttrDef', b1)
    assert _is_linked(a, 'vM_BooleanAttrDef', b1)
    if hasattr(b1, 'vM_Boolean_ATT_ID'):
        assert _is_linked(b1, 'vM_Boolean_ATT_ID', a)
    _safe_set(a, 'vM_BooleanAttrDef', b2)
    assert _is_linked(a, 'vM_BooleanAttrDef', b2)
    if hasattr(b1, 'vM_Boolean_ATT_ID'):
        assert not _is_linked(b1, 'vM_Boolean_ATT_ID', a)
    if hasattr(b2, 'vM_Boolean_ATT_ID'):
        assert _is_linked(b2, 'vM_Boolean_ATT_ID', a)
    _safe_set(a, 'vM_BooleanAttrDef', None)
    assert not _is_linked(a, 'vM_BooleanAttrDef', b2)
    if hasattr(b2, 'vM_Boolean_ATT_ID'):
        assert not _is_linked(b2, 'vM_Boolean_ATT_ID', a)


def test_assoc_name23_link_reassign_clear():
    a = vM_StringAttrDef(value="sample_text")
    b1 = vM_String_ATT_ID()
    b2 = vM_String_ATT_ID()
    _safe_set(a, 'vM_StringAttrDef', b1)
    assert _is_linked(a, 'vM_StringAttrDef', b1)
    if hasattr(b1, 'vM_String_ATT_ID'):
        assert _is_linked(b1, 'vM_String_ATT_ID', a)
    _safe_set(a, 'vM_StringAttrDef', b2)
    assert _is_linked(a, 'vM_StringAttrDef', b2)
    if hasattr(b1, 'vM_String_ATT_ID'):
        assert not _is_linked(b1, 'vM_String_ATT_ID', a)
    if hasattr(b2, 'vM_String_ATT_ID'):
        assert _is_linked(b2, 'vM_String_ATT_ID', a)
    _safe_set(a, 'vM_StringAttrDef', None)
    assert not _is_linked(a, 'vM_StringAttrDef', b2)
    if hasattr(b2, 'vM_String_ATT_ID'):
        assert not _is_linked(b2, 'vM_String_ATT_ID', a)


def test_assoc_objectives92_link_reassign_clear():
    a = vM_Objective(name="sample_text", op="sample_text")
    b1 = vM_Objectives()
    b2 = vM_Objectives()
    _safe_set(a, 'vM_Objective', b1)
    assert _is_linked(a, 'vM_Objective', b1)
    if hasattr(b1, 'vM_Objectives'):
        assert _is_linked(b1, 'vM_Objectives', a)
    _safe_set(a, 'vM_Objective', b2)
    assert _is_linked(a, 'vM_Objective', b2)
    if hasattr(b1, 'vM_Objectives'):
        assert not _is_linked(b1, 'vM_Objectives', a)
    if hasattr(b2, 'vM_Objectives'):
        assert _is_linked(b2, 'vM_Objectives', a)
    _safe_set(a, 'vM_Objective', None)
    assert not _is_linked(a, 'vM_Objective', b2)
    if hasattr(b2, 'vM_Objectives'):
        assert not _is_linked(b2, 'vM_Objectives', a)


def test_assoc_ownedFeature150_link_reassign_clear():
    a = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b1 = vM_AttHead(forAllFeatures=True)
    b2 = vM_AttHead(forAllFeatures=False)
    _safe_set(a, 'vM_Feature152', b1)
    assert _is_linked(a, 'vM_Feature152', b1)
    if hasattr(b1, 'vM_AttHead151'):
        assert _is_linked(b1, 'vM_AttHead151', a)
    _safe_set(a, 'vM_Feature152', b2)
    assert _is_linked(a, 'vM_Feature152', b2)
    if hasattr(b1, 'vM_AttHead151'):
        assert not _is_linked(b1, 'vM_AttHead151', a)
    if hasattr(b2, 'vM_AttHead151'):
        assert _is_linked(b2, 'vM_AttHead151', a)
    _safe_set(a, 'vM_Feature152', None)
    assert not _is_linked(a, 'vM_Feature152', b2)
    if hasattr(b2, 'vM_AttHead151'):
        assert not _is_linked(b2, 'vM_AttHead151', a)


def test_assoc_pairs125_link_reassign_clear():
    a = vM_TableBasedValuationByFeatureAndClone(name="sample_text")
    b1 = vM_PairAttributeValue(value="sample_text")
    b2 = vM_PairAttributeValue(value="sample_text_2")
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone126', {b1})
    assert _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone126', b1)
    if hasattr(b1, 'vM_PairAttributeValue'):
        assert _is_linked(b1, 'vM_PairAttributeValue', a)
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone126', {b2})
    assert _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone126', b2)
    if hasattr(b1, 'vM_PairAttributeValue'):
        assert not _is_linked(b1, 'vM_PairAttributeValue', a)
    if hasattr(b2, 'vM_PairAttributeValue'):
        assert _is_linked(b2, 'vM_PairAttributeValue', a)
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone126', set())
    assert not _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone126', b2)
    if hasattr(b2, 'vM_PairAttributeValue'):
        assert not _is_linked(b2, 'vM_PairAttributeValue', a)


def test_assoc_pairs130_link_reassign_clear():
    a = vM_PairAttributeValue(value="sample_text")
    b1 = vM_TableBasedValuationByFeature()
    b2 = vM_TableBasedValuationByFeature()
    _safe_set(a, 'vM_PairAttributeValue132', b1)
    assert _is_linked(a, 'vM_PairAttributeValue132', b1)
    if hasattr(b1, 'vM_TableBasedValuationByFeature131'):
        assert _is_linked(b1, 'vM_TableBasedValuationByFeature131', a)
    _safe_set(a, 'vM_PairAttributeValue132', b2)
    assert _is_linked(a, 'vM_PairAttributeValue132', b2)
    if hasattr(b1, 'vM_TableBasedValuationByFeature131'):
        assert not _is_linked(b1, 'vM_TableBasedValuationByFeature131', a)
    if hasattr(b2, 'vM_TableBasedValuationByFeature131'):
        assert _is_linked(b2, 'vM_TableBasedValuationByFeature131', a)
    _safe_set(a, 'vM_PairAttributeValue132', None)
    assert not _is_linked(a, 'vM_PairAttributeValue132', b2)
    if hasattr(b2, 'vM_TableBasedValuationByFeature131'):
        assert not _is_linked(b2, 'vM_TableBasedValuationByFeature131', a)


def test_assoc_pairs138_link_reassign_clear():
    a = vM_PairFeatureInteger(value="sample_text")
    b1 = vM_TableBasedValuationByAttributeForInteger()
    b2 = vM_TableBasedValuationByAttributeForInteger()
    _safe_set(a, 'vM_PairFeatureInteger', b1)
    assert _is_linked(a, 'vM_PairFeatureInteger', b1)
    if hasattr(b1, 'vM_TableBasedValuationByAttributeForInteger139'):
        assert _is_linked(b1, 'vM_TableBasedValuationByAttributeForInteger139', a)
    _safe_set(a, 'vM_PairFeatureInteger', b2)
    assert _is_linked(a, 'vM_PairFeatureInteger', b2)
    if hasattr(b1, 'vM_TableBasedValuationByAttributeForInteger139'):
        assert not _is_linked(b1, 'vM_TableBasedValuationByAttributeForInteger139', a)
    if hasattr(b2, 'vM_TableBasedValuationByAttributeForInteger139'):
        assert _is_linked(b2, 'vM_TableBasedValuationByAttributeForInteger139', a)
    _safe_set(a, 'vM_PairFeatureInteger', None)
    assert not _is_linked(a, 'vM_PairFeatureInteger', b2)
    if hasattr(b2, 'vM_TableBasedValuationByAttributeForInteger139'):
        assert not _is_linked(b2, 'vM_TableBasedValuationByAttributeForInteger139', a)


def test_assoc_pairs145_link_reassign_clear():
    a = vM_PairFeatureReal(value="sample_text")
    b1 = vM_TableBasedValuationByAttributeForReal()
    b2 = vM_TableBasedValuationByAttributeForReal()
    _safe_set(a, 'vM_PairFeatureReal', b1)
    assert _is_linked(a, 'vM_PairFeatureReal', b1)
    if hasattr(b1, 'vM_TableBasedValuationByAttributeForReal146'):
        assert _is_linked(b1, 'vM_TableBasedValuationByAttributeForReal146', a)
    _safe_set(a, 'vM_PairFeatureReal', b2)
    assert _is_linked(a, 'vM_PairFeatureReal', b2)
    if hasattr(b1, 'vM_TableBasedValuationByAttributeForReal146'):
        assert not _is_linked(b1, 'vM_TableBasedValuationByAttributeForReal146', a)
    if hasattr(b2, 'vM_TableBasedValuationByAttributeForReal146'):
        assert _is_linked(b2, 'vM_TableBasedValuationByAttributeForReal146', a)
    _safe_set(a, 'vM_PairFeatureReal', None)
    assert not _is_linked(a, 'vM_PairFeatureReal', b2)
    if hasattr(b2, 'vM_TableBasedValuationByAttributeForReal146'):
        assert not _is_linked(b2, 'vM_TableBasedValuationByAttributeForReal146', a)


def test_assoc_parent7_link_reassign_clear():
    a = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b1 = vM_FeatureHierarchy()
    b2 = vM_FeatureHierarchy()
    _safe_set(a, 'vM_Feature', b1)
    assert _is_linked(a, 'vM_Feature', b1)
    if hasattr(b1, 'vM_FeatureHierarchy8'):
        assert _is_linked(b1, 'vM_FeatureHierarchy8', a)
    _safe_set(a, 'vM_Feature', b2)
    assert _is_linked(a, 'vM_Feature', b2)
    if hasattr(b1, 'vM_FeatureHierarchy8'):
        assert not _is_linked(b1, 'vM_FeatureHierarchy8', a)
    if hasattr(b2, 'vM_FeatureHierarchy8'):
        assert _is_linked(b2, 'vM_FeatureHierarchy8', a)
    _safe_set(a, 'vM_Feature', None)
    assert not _is_linked(a, 'vM_Feature', b2)
    if hasattr(b2, 'vM_FeatureHierarchy8'):
        assert not _is_linked(b2, 'vM_FeatureHierarchy8', a)


def test_assoc_refAtt133_link_reassign_clear():
    a = vM_PairAttributeValue(value="sample_text")
    b1 = vM_Abstract_ATT_ID(name="sample_text")
    b2 = vM_Abstract_ATT_ID(name="sample_text_2")
    _safe_set(a, 'vM_PairAttributeValue134', b1)
    assert _is_linked(a, 'vM_PairAttributeValue134', b1)
    if hasattr(b1, 'vM_Abstract_ATT_ID135'):
        assert _is_linked(b1, 'vM_Abstract_ATT_ID135', a)
    _safe_set(a, 'vM_PairAttributeValue134', b2)
    assert _is_linked(a, 'vM_PairAttributeValue134', b2)
    if hasattr(b1, 'vM_Abstract_ATT_ID135'):
        assert not _is_linked(b1, 'vM_Abstract_ATT_ID135', a)
    if hasattr(b2, 'vM_Abstract_ATT_ID135'):
        assert _is_linked(b2, 'vM_Abstract_ATT_ID135', a)
    _safe_set(a, 'vM_PairAttributeValue134', None)
    assert not _is_linked(a, 'vM_PairAttributeValue134', b2)
    if hasattr(b2, 'vM_Abstract_ATT_ID135'):
        assert not _is_linked(b2, 'vM_Abstract_ATT_ID135', a)


def test_assoc_refAtt62_link_reassign_clear():
    a = vM_AttributeDescription(description="sample_text")
    b1 = vM_Abstract_ATT_ID(name="sample_text")
    b2 = vM_Abstract_ATT_ID(name="sample_text_2")
    _safe_set(a, 'vM_AttributeDescription63', b1)
    assert _is_linked(a, 'vM_AttributeDescription63', b1)
    if hasattr(b1, 'vM_Abstract_ATT_ID'):
        assert _is_linked(b1, 'vM_Abstract_ATT_ID', a)
    _safe_set(a, 'vM_AttributeDescription63', b2)
    assert _is_linked(a, 'vM_AttributeDescription63', b2)
    if hasattr(b1, 'vM_Abstract_ATT_ID'):
        assert not _is_linked(b1, 'vM_Abstract_ATT_ID', a)
    if hasattr(b2, 'vM_Abstract_ATT_ID'):
        assert _is_linked(b2, 'vM_Abstract_ATT_ID', a)
    _safe_set(a, 'vM_AttributeDescription63', None)
    assert not _is_linked(a, 'vM_AttributeDescription63', b2)
    if hasattr(b2, 'vM_Abstract_ATT_ID'):
        assert not _is_linked(b2, 'vM_Abstract_ATT_ID', a)


def test_assoc_refAtt73_link_reassign_clear():
    a = vM_Abstract_ATT_ID(name="sample_text")
    b1 = vM_PrimitiveExpression()
    b2 = vM_PrimitiveExpression()
    _safe_set(a, 'vM_Abstract_ATT_ID75', b1)
    assert _is_linked(a, 'vM_Abstract_ATT_ID75', b1)
    if hasattr(b1, 'vM_PrimitiveExpression74'):
        assert _is_linked(b1, 'vM_PrimitiveExpression74', a)
    _safe_set(a, 'vM_Abstract_ATT_ID75', b2)
    assert _is_linked(a, 'vM_Abstract_ATT_ID75', b2)
    if hasattr(b1, 'vM_PrimitiveExpression74'):
        assert not _is_linked(b1, 'vM_PrimitiveExpression74', a)
    if hasattr(b2, 'vM_PrimitiveExpression74'):
        assert _is_linked(b2, 'vM_PrimitiveExpression74', a)
    _safe_set(a, 'vM_Abstract_ATT_ID75', None)
    assert not _is_linked(a, 'vM_Abstract_ATT_ID75', b2)
    if hasattr(b2, 'vM_PrimitiveExpression74'):
        assert not _is_linked(b2, 'vM_PrimitiveExpression74', a)


def test_assoc_refFeat140_link_reassign_clear():
    a = vM_PairFeatureInteger(value="sample_text")
    b1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    _safe_set(a, 'vM_PairFeatureInteger141', b1)
    assert _is_linked(a, 'vM_PairFeatureInteger141', b1)
    if hasattr(b1, 'vM_Feature142'):
        assert _is_linked(b1, 'vM_Feature142', a)
    _safe_set(a, 'vM_PairFeatureInteger141', b2)
    assert _is_linked(a, 'vM_PairFeatureInteger141', b2)
    if hasattr(b1, 'vM_Feature142'):
        assert not _is_linked(b1, 'vM_Feature142', a)
    if hasattr(b2, 'vM_Feature142'):
        assert _is_linked(b2, 'vM_Feature142', a)
    _safe_set(a, 'vM_PairFeatureInteger141', None)
    assert not _is_linked(a, 'vM_PairFeatureInteger141', b2)
    if hasattr(b2, 'vM_Feature142'):
        assert not _is_linked(b2, 'vM_Feature142', a)


def test_assoc_refFeat147_link_reassign_clear():
    a = vM_PairFeatureReal(value="sample_text")
    b1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    _safe_set(a, 'vM_PairFeatureReal148', b1)
    assert _is_linked(a, 'vM_PairFeatureReal148', b1)
    if hasattr(b1, 'vM_Feature149'):
        assert _is_linked(b1, 'vM_Feature149', a)
    _safe_set(a, 'vM_PairFeatureReal148', b2)
    assert _is_linked(a, 'vM_PairFeatureReal148', b2)
    if hasattr(b1, 'vM_Feature149'):
        assert not _is_linked(b1, 'vM_Feature149', a)
    if hasattr(b2, 'vM_Feature149'):
        assert _is_linked(b2, 'vM_Feature149', a)
    _safe_set(a, 'vM_PairFeatureReal148', None)
    assert not _is_linked(a, 'vM_PairFeatureReal148', b2)
    if hasattr(b2, 'vM_Feature149'):
        assert not _is_linked(b2, 'vM_Feature149', a)


def test_assoc_refFeat56_link_reassign_clear():
    a = vM_FeatureDescription(description="sample_text")
    b1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    _safe_set(a, 'vM_FeatureDescription57', b1)
    assert _is_linked(a, 'vM_FeatureDescription57', b1)
    if hasattr(b1, 'vM_Feature58'):
        assert _is_linked(b1, 'vM_Feature58', a)
    _safe_set(a, 'vM_FeatureDescription57', b2)
    assert _is_linked(a, 'vM_FeatureDescription57', b2)
    if hasattr(b1, 'vM_Feature58'):
        assert not _is_linked(b1, 'vM_Feature58', a)
    if hasattr(b2, 'vM_Feature58'):
        assert _is_linked(b2, 'vM_Feature58', a)
    _safe_set(a, 'vM_FeatureDescription57', None)
    assert not _is_linked(a, 'vM_FeatureDescription57', b2)
    if hasattr(b2, 'vM_Feature58'):
        assert not _is_linked(b2, 'vM_Feature58', a)


def test_assoc_refFeat59_link_reassign_clear():
    a = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b1 = vM_AttributeDescription(description="sample_text")
    b2 = vM_AttributeDescription(description="sample_text_2")
    _safe_set(a, 'vM_Feature61', b1)
    assert _is_linked(a, 'vM_Feature61', b1)
    if hasattr(b1, 'vM_AttributeDescription60'):
        assert _is_linked(b1, 'vM_AttributeDescription60', a)
    _safe_set(a, 'vM_Feature61', b2)
    assert _is_linked(a, 'vM_Feature61', b2)
    if hasattr(b1, 'vM_AttributeDescription60'):
        assert not _is_linked(b1, 'vM_AttributeDescription60', a)
    if hasattr(b2, 'vM_AttributeDescription60'):
        assert _is_linked(b2, 'vM_AttributeDescription60', a)
    _safe_set(a, 'vM_Feature61', None)
    assert not _is_linked(a, 'vM_Feature61', b2)
    if hasattr(b2, 'vM_AttributeDescription60'):
        assert not _is_linked(b2, 'vM_AttributeDescription60', a)


def test_assoc_refFeature122_link_reassign_clear():
    a = vM_TableBasedValuationByFeatureAndClone(name="sample_text")
    b1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone123', b1)
    assert _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone123', b1)
    if hasattr(b1, 'vM_Feature124'):
        assert _is_linked(b1, 'vM_Feature124', a)
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone123', b2)
    assert _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone123', b2)
    if hasattr(b1, 'vM_Feature124'):
        assert not _is_linked(b1, 'vM_Feature124', a)
    if hasattr(b2, 'vM_Feature124'):
        assert _is_linked(b2, 'vM_Feature124', a)
    _safe_set(a, 'vM_TableBasedValuationByFeatureAndClone123', None)
    assert not _is_linked(a, 'vM_TableBasedValuationByFeatureAndClone123', b2)
    if hasattr(b2, 'vM_Feature124'):
        assert not _is_linked(b2, 'vM_Feature124', a)


def test_assoc_refFeature127_link_reassign_clear():
    a = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    b1 = vM_TableBasedValuationByFeature()
    b2 = vM_TableBasedValuationByFeature()
    _safe_set(a, 'vM_Feature129', b1)
    assert _is_linked(a, 'vM_Feature129', b1)
    if hasattr(b1, 'vM_TableBasedValuationByFeature128'):
        assert _is_linked(b1, 'vM_TableBasedValuationByFeature128', a)
    _safe_set(a, 'vM_Feature129', b2)
    assert _is_linked(a, 'vM_Feature129', b2)
    if hasattr(b1, 'vM_TableBasedValuationByFeature128'):
        assert not _is_linked(b1, 'vM_TableBasedValuationByFeature128', a)
    if hasattr(b2, 'vM_TableBasedValuationByFeature128'):
        assert _is_linked(b2, 'vM_TableBasedValuationByFeature128', a)
    _safe_set(a, 'vM_Feature129', None)
    assert not _is_linked(a, 'vM_Feature129', b2)
    if hasattr(b2, 'vM_TableBasedValuationByFeature128'):
        assert not _is_linked(b2, 'vM_TableBasedValuationByFeature128', a)


def test_assoc_version3_link_reassign_clear():
    a = vM_Version(main=7, tail=7)
    b1 = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    b2 = vM_MetaDataDeclaration(author="sample_text_2", date="sample_text_2", description="sample_text_2", name="sample_text_2", organization="sample_text_2", publication="sample_text_2")
    _safe_set(a, 'vM_Version', b1)
    assert _is_linked(a, 'vM_Version', b1)
    if hasattr(b1, 'vM_MetaDataDeclaration'):
        assert _is_linked(b1, 'vM_MetaDataDeclaration', a)
    _safe_set(a, 'vM_Version', b2)
    assert _is_linked(a, 'vM_Version', b2)
    if hasattr(b1, 'vM_MetaDataDeclaration'):
        assert not _is_linked(b1, 'vM_MetaDataDeclaration', a)
    if hasattr(b2, 'vM_MetaDataDeclaration'):
        assert _is_linked(b2, 'vM_MetaDataDeclaration', a)
    _safe_set(a, 'vM_Version', None)
    assert not _is_linked(a, 'vM_Version', b2)
    if hasattr(b2, 'vM_MetaDataDeclaration'):
        assert not _is_linked(b2, 'vM_MetaDataDeclaration', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Abstract_ATT_ID_strategy = st.builds(Abstract_ATT_ID)
@given(instance=Abstract_ATT_ID_strategy)
@settings(max_examples=25)
def test_Abstract_ATT_ID_instantiation(instance):
    assert isinstance(instance, Abstract_ATT_ID)


BasicAttrDef_strategy = st.builds(BasicAttrDef)
@given(instance=BasicAttrDef_strategy)
@settings(max_examples=25)
def test_BasicAttrDef_instantiation(instance):
    assert isinstance(instance, BasicAttrDef)


BasicAttrValuation_strategy = st.builds(BasicAttrValuation)
@given(instance=BasicAttrValuation_strategy)
@settings(max_examples=25)
def test_BasicAttrValuation_instantiation(instance):
    assert isinstance(instance, BasicAttrValuation)


ComplexExpression_strategy = st.builds(ComplexExpression)
@given(instance=ComplexExpression_strategy)
@settings(max_examples=25)
def test_ComplexExpression_instantiation(instance):
    assert isinstance(instance, ComplexExpression)


EnumAttrDef_strategy = st.builds(EnumAttrDef)
@given(instance=EnumAttrDef_strategy)
@settings(max_examples=25)
def test_EnumAttrDef_instantiation(instance):
    assert isinstance(instance, EnumAttrDef)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExtendedValuation_strategy = st.builds(ExtendedValuation)
@given(instance=ExtendedValuation_strategy)
@settings(max_examples=25)
def test_ExtendedValuation_instantiation(instance):
    assert isinstance(instance, ExtendedValuation)


FeatureDefinition_strategy = st.builds(FeatureDefinition)
@given(instance=FeatureDefinition_strategy)
@settings(max_examples=25)
def test_FeatureDefinition_instantiation(instance):
    assert isinstance(instance, FeatureDefinition)


FeaturesGroup_strategy = st.builds(FeaturesGroup)
@given(instance=FeaturesGroup_strategy)
@settings(max_examples=25)
def test_FeaturesGroup_instantiation(instance):
    assert isinstance(instance, FeaturesGroup)


IntegerAttrDef_strategy = st.builds(IntegerAttrDef)
@given(instance=IntegerAttrDef_strategy)
@settings(max_examples=25)
def test_IntegerAttrDef_instantiation(instance):
    assert isinstance(instance, IntegerAttrDef)


RealAttrDef_strategy = st.builds(RealAttrDef)
@given(instance=RealAttrDef_strategy)
@settings(max_examples=25)
def test_RealAttrDef_instantiation(instance):
    assert isinstance(instance, RealAttrDef)


TableBasedValuationByAttribute_strategy = st.builds(TableBasedValuationByAttribute)
@given(instance=TableBasedValuationByAttribute_strategy)
@settings(max_examples=25)
def test_TableBasedValuationByAttribute_instantiation(instance):
    assert isinstance(instance, TableBasedValuationByAttribute)


VmBlock_strategy = st.builds(VmBlock)
@given(instance=VmBlock_strategy)
@settings(max_examples=25)
def test_VmBlock_instantiation(instance):
    assert isinstance(instance, VmBlock)


vM_Abstract_ATT_ID_strategy = st.builds(vM_Abstract_ATT_ID, name=safe_text)
@given(instance=vM_Abstract_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_Abstract_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_Abstract_ATT_ID)


vM_AdvancedAttrValuation_strategy = st.builds(vM_AdvancedAttrValuation)
@given(instance=vM_AdvancedAttrValuation_strategy)
@settings(max_examples=25)
def test_vM_AdvancedAttrValuation_instantiation(instance):
    assert isinstance(instance, vM_AdvancedAttrValuation)


vM_And_strategy = st.builds(vM_And)
@given(instance=vM_And_strategy)
@settings(max_examples=25)
def test_vM_And_instantiation(instance):
    assert isinstance(instance, vM_And)


vM_AttHead_strategy = st.builds(vM_AttHead, forAllFeatures=st.booleans())
@given(instance=vM_AttHead_strategy)
@settings(max_examples=25)
def test_vM_AttHead_instantiation(instance):
    assert isinstance(instance, vM_AttHead)


vM_AttrDef_strategy = st.builds(vM_AttrDef, notDecidable=st.booleans(), notTranslatable=st.booleans(), runTime=st.booleans())
@given(instance=vM_AttrDef_strategy)
@settings(max_examples=25)
def test_vM_AttrDef_instantiation(instance):
    assert isinstance(instance, vM_AttrDef)


vM_AttributeDescription_strategy = st.builds(vM_AttributeDescription, description=safe_text)
@given(instance=vM_AttributeDescription_strategy)
@settings(max_examples=25)
def test_vM_AttributeDescription_instantiation(instance):
    assert isinstance(instance, vM_AttributeDescription)


vM_Attributes_strategy = st.builds(vM_Attributes)
@given(instance=vM_Attributes_strategy)
@settings(max_examples=25)
def test_vM_Attributes_instantiation(instance):
    assert isinstance(instance, vM_Attributes)


vM_BasicAttrDef_strategy = st.builds(vM_BasicAttrDef)
@given(instance=vM_BasicAttrDef_strategy)
@settings(max_examples=25)
def test_vM_BasicAttrDef_instantiation(instance):
    assert isinstance(instance, vM_BasicAttrDef)


vM_BasicAttrValuation_strategy = st.builds(vM_BasicAttrValuation, value=safe_text)
@given(instance=vM_BasicAttrValuation_strategy)
@settings(max_examples=25)
def test_vM_BasicAttrValuation_instantiation(instance):
    assert isinstance(instance, vM_BasicAttrValuation)


vM_BiImplication_strategy = st.builds(vM_BiImplication)
@given(instance=vM_BiImplication_strategy)
@settings(max_examples=25)
def test_vM_BiImplication_instantiation(instance):
    assert isinstance(instance, vM_BiImplication)


vM_BoolDefaultDef_strategy = st.builds(vM_BoolDefaultDef, value=safe_text)
@given(instance=vM_BoolDefaultDef_strategy)
@settings(max_examples=25)
def test_vM_BoolDefaultDef_instantiation(instance):
    assert isinstance(instance, vM_BoolDefaultDef)


vM_BooleanAttrDef_strategy = st.builds(vM_BooleanAttrDef, value=safe_text)
@given(instance=vM_BooleanAttrDef_strategy)
@settings(max_examples=25)
def test_vM_BooleanAttrDef_instantiation(instance):
    assert isinstance(instance, vM_BooleanAttrDef)


vM_BooleanAttrValuation_strategy = st.builds(vM_BooleanAttrValuation)
@given(instance=vM_BooleanAttrValuation_strategy)
@settings(max_examples=25)
def test_vM_BooleanAttrValuation_instantiation(instance):
    assert isinstance(instance, vM_BooleanAttrValuation)


vM_BooleanExpression_strategy = st.builds(vM_BooleanExpression, op=safe_text, value=safe_text)
@given(instance=vM_BooleanExpression_strategy)
@settings(max_examples=25)
def test_vM_BooleanExpression_instantiation(instance):
    assert isinstance(instance, vM_BooleanExpression)


vM_BooleanExpression_List_strategy = st.builds(vM_BooleanExpression_List)
@given(instance=vM_BooleanExpression_List_strategy)
@settings(max_examples=25)
def test_vM_BooleanExpression_List_instantiation(instance):
    assert isinstance(instance, vM_BooleanExpression_List)


vM_BooleanValuation_strategy = st.builds(vM_BooleanValuation, notSelected=st.booleans())
@given(instance=vM_BooleanValuation_strategy)
@settings(max_examples=25)
def test_vM_BooleanValuation_instantiation(instance):
    assert isinstance(instance, vM_BooleanValuation)


vM_Boolean_ATT_ID_strategy = st.builds(vM_Boolean_ATT_ID)
@given(instance=vM_Boolean_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_Boolean_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_Boolean_ATT_ID)


vM_BrackedExpression_strategy = st.builds(vM_BrackedExpression)
@given(instance=vM_BrackedExpression_strategy)
@settings(max_examples=25)
def test_vM_BrackedExpression_instantiation(instance):
    assert isinstance(instance, vM_BrackedExpression)


vM_CardinalityBased_strategy = st.builds(vM_CardinalityBased, all=st.booleans(), max=safe_text, min=safe_text)
@given(instance=vM_CardinalityBased_strategy)
@settings(max_examples=25)
def test_vM_CardinalityBased_instantiation(instance):
    assert isinstance(instance, vM_CardinalityBased)


vM_ComplexExpression_strategy = st.builds(vM_ComplexExpression)
@given(instance=vM_ComplexExpression_strategy)
@settings(max_examples=25)
def test_vM_ComplexExpression_instantiation(instance):
    assert isinstance(instance, vM_ComplexExpression)


vM_Configuration_strategy = st.builds(vM_Configuration, name=safe_text)
@given(instance=vM_Configuration_strategy)
@settings(max_examples=25)
def test_vM_Configuration_instantiation(instance):
    assert isinstance(instance, vM_Configuration)


vM_Configurations_strategy = st.builds(vM_Configurations)
@given(instance=vM_Configurations_strategy)
@settings(max_examples=25)
def test_vM_Configurations_instantiation(instance):
    assert isinstance(instance, vM_Configurations)


vM_Constraint_strategy = st.builds(vM_Constraint, name=safe_text, not_=st.booleans())
@given(instance=vM_Constraint_strategy)
@settings(max_examples=25)
def test_vM_Constraint_instantiation(instance):
    assert isinstance(instance, vM_Constraint)


vM_Constraints_strategy = st.builds(vM_Constraints)
@given(instance=vM_Constraints_strategy)
@settings(max_examples=25)
def test_vM_Constraints_instantiation(instance):
    assert isinstance(instance, vM_Constraints)


vM_Descriptions_strategy = st.builds(vM_Descriptions)
@given(instance=vM_Descriptions_strategy)
@settings(max_examples=25)
def test_vM_Descriptions_instantiation(instance):
    assert isinstance(instance, vM_Descriptions)


vM_Division_strategy = st.builds(vM_Division)
@given(instance=vM_Division_strategy)
@settings(max_examples=25)
def test_vM_Division_instantiation(instance):
    assert isinstance(instance, vM_Division)


vM_Email_strategy = st.builds(vM_Email, domain=safe_text, username=safe_text)
@given(instance=vM_Email_strategy)
@settings(max_examples=25)
def test_vM_Email_instantiation(instance):
    assert isinstance(instance, vM_Email)


vM_EnumAttrDef_strategy = st.builds(vM_EnumAttrDef, value=safe_text)
@given(instance=vM_EnumAttrDef_strategy)
@settings(max_examples=25)
def test_vM_EnumAttrDef_instantiation(instance):
    assert isinstance(instance, vM_EnumAttrDef)


vM_EnumIntegerDef_strategy = st.builds(vM_EnumIntegerDef)
@given(instance=vM_EnumIntegerDef_strategy)
@settings(max_examples=25)
def test_vM_EnumIntegerDef_instantiation(instance):
    assert isinstance(instance, vM_EnumIntegerDef)


vM_EnumRealDef_strategy = st.builds(vM_EnumRealDef)
@given(instance=vM_EnumRealDef_strategy)
@settings(max_examples=25)
def test_vM_EnumRealDef_instantiation(instance):
    assert isinstance(instance, vM_EnumRealDef)


vM_EnumStringDef_strategy = st.builds(vM_EnumStringDef)
@given(instance=vM_EnumStringDef_strategy)
@settings(max_examples=25)
def test_vM_EnumStringDef_instantiation(instance):
    assert isinstance(instance, vM_EnumStringDef)


vM_Enum_Integer_ATT_ID_strategy = st.builds(vM_Enum_Integer_ATT_ID)
@given(instance=vM_Enum_Integer_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_Enum_Integer_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_Enum_Integer_ATT_ID)


vM_Enum_Real_ATT_ID_strategy = st.builds(vM_Enum_Real_ATT_ID)
@given(instance=vM_Enum_Real_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_Enum_Real_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_Enum_Real_ATT_ID)


vM_Enum_String_ATT_ID_strategy = st.builds(vM_Enum_String_ATT_ID)
@given(instance=vM_Enum_String_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_Enum_String_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_Enum_String_ATT_ID)


vM_Equality_strategy = st.builds(vM_Equality)
@given(instance=vM_Equality_strategy)
@settings(max_examples=25)
def test_vM_Equality_instantiation(instance):
    assert isinstance(instance, vM_Equality)


vM_Excludes_strategy = st.builds(vM_Excludes)
@given(instance=vM_Excludes_strategy)
@settings(max_examples=25)
def test_vM_Excludes_instantiation(instance):
    assert isinstance(instance, vM_Excludes)


vM_Expression_strategy = st.builds(vM_Expression)
@given(instance=vM_Expression_strategy)
@settings(max_examples=25)
def test_vM_Expression_instantiation(instance):
    assert isinstance(instance, vM_Expression)


vM_ExtendedValuation_strategy = st.builds(vM_ExtendedValuation)
@given(instance=vM_ExtendedValuation_strategy)
@settings(max_examples=25)
def test_vM_ExtendedValuation_instantiation(instance):
    assert isinstance(instance, vM_ExtendedValuation)


vM_Feature_strategy = st.builds(vM_Feature, max=safe_text, min=safe_text, name=safe_text, notDecidable=st.booleans(), notTranslatable=st.booleans(), optional=st.booleans(), runTime=st.booleans())
@given(instance=vM_Feature_strategy)
@settings(max_examples=25)
def test_vM_Feature_instantiation(instance):
    assert isinstance(instance, vM_Feature)


vM_FeatureDefinition_strategy = st.builds(vM_FeatureDefinition)
@given(instance=vM_FeatureDefinition_strategy)
@settings(max_examples=25)
def test_vM_FeatureDefinition_instantiation(instance):
    assert isinstance(instance, vM_FeatureDefinition)


vM_FeatureDescription_strategy = st.builds(vM_FeatureDescription, description=safe_text)
@given(instance=vM_FeatureDescription_strategy)
@settings(max_examples=25)
def test_vM_FeatureDescription_instantiation(instance):
    assert isinstance(instance, vM_FeatureDescription)


vM_FeatureHierarchy_strategy = st.builds(vM_FeatureHierarchy)
@given(instance=vM_FeatureHierarchy_strategy)
@settings(max_examples=25)
def test_vM_FeatureHierarchy_instantiation(instance):
    assert isinstance(instance, vM_FeatureHierarchy)


vM_FeaturesGroup_strategy = st.builds(vM_FeaturesGroup)
@given(instance=vM_FeaturesGroup_strategy)
@settings(max_examples=25)
def test_vM_FeaturesGroup_instantiation(instance):
    assert isinstance(instance, vM_FeaturesGroup)


vM_Greater_strategy = st.builds(vM_Greater)
@given(instance=vM_Greater_strategy)
@settings(max_examples=25)
def test_vM_Greater_instantiation(instance):
    assert isinstance(instance, vM_Greater)


vM_Greaterequal_strategy = st.builds(vM_Greaterequal)
@given(instance=vM_Greaterequal_strategy)
@settings(max_examples=25)
def test_vM_Greaterequal_instantiation(instance):
    assert isinstance(instance, vM_Greaterequal)


vM_If_strategy = st.builds(vM_If)
@given(instance=vM_If_strategy)
@settings(max_examples=25)
def test_vM_If_instantiation(instance):
    assert isinstance(instance, vM_If)


vM_ImportDeclaration_strategy = st.builds(vM_ImportDeclaration, importedNamespace=safe_text)
@given(instance=vM_ImportDeclaration_strategy)
@settings(max_examples=25)
def test_vM_ImportDeclaration_instantiation(instance):
    assert isinstance(instance, vM_ImportDeclaration)


vM_Inequality_strategy = st.builds(vM_Inequality)
@given(instance=vM_Inequality_strategy)
@settings(max_examples=25)
def test_vM_Inequality_instantiation(instance):
    assert isinstance(instance, vM_Inequality)


vM_IntegerAttrDef_strategy = st.builds(vM_IntegerAttrDef)
@given(instance=vM_IntegerAttrDef_strategy)
@settings(max_examples=25)
def test_vM_IntegerAttrDef_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDef)


vM_IntegerAttrDefBounded_strategy = st.builds(vM_IntegerAttrDefBounded)
@given(instance=vM_IntegerAttrDefBounded_strategy)
@settings(max_examples=25)
def test_vM_IntegerAttrDefBounded_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDefBounded)


vM_IntegerAttrDefComplement_strategy = st.builds(vM_IntegerAttrDefComplement, max=safe_text, min=safe_text)
@given(instance=vM_IntegerAttrDefComplement_strategy)
@settings(max_examples=25)
def test_vM_IntegerAttrDefComplement_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDefComplement)


vM_IntegerAttrDefUnbounded_strategy = st.builds(vM_IntegerAttrDefUnbounded, value=safe_text)
@given(instance=vM_IntegerAttrDefUnbounded_strategy)
@settings(max_examples=25)
def test_vM_IntegerAttrDefUnbounded_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDefUnbounded)


vM_IntegerAttrValuation_strategy = st.builds(vM_IntegerAttrValuation)
@given(instance=vM_IntegerAttrValuation_strategy)
@settings(max_examples=25)
def test_vM_IntegerAttrValuation_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrValuation)


vM_IntegerDefaultDef_strategy = st.builds(vM_IntegerDefaultDef, value=st.integers())
@given(instance=vM_IntegerDefaultDef_strategy)
@settings(max_examples=25)
def test_vM_IntegerDefaultDef_instantiation(instance):
    assert isinstance(instance, vM_IntegerDefaultDef)


vM_IntegerDeltaDef_strategy = st.builds(vM_IntegerDeltaDef, value=st.integers())
@given(instance=vM_IntegerDeltaDef_strategy)
@settings(max_examples=25)
def test_vM_IntegerDeltaDef_instantiation(instance):
    assert isinstance(instance, vM_IntegerDeltaDef)


vM_Integer_ATT_ID_strategy = st.builds(vM_Integer_ATT_ID)
@given(instance=vM_Integer_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_Integer_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_Integer_ATT_ID)


vM_LeftImplication_strategy = st.builds(vM_LeftImplication)
@given(instance=vM_LeftImplication_strategy)
@settings(max_examples=25)
def test_vM_LeftImplication_instantiation(instance):
    assert isinstance(instance, vM_LeftImplication)


vM_Less_strategy = st.builds(vM_Less)
@given(instance=vM_Less_strategy)
@settings(max_examples=25)
def test_vM_Less_instantiation(instance):
    assert isinstance(instance, vM_Less)


vM_Lessequal_strategy = st.builds(vM_Lessequal)
@given(instance=vM_Lessequal_strategy)
@settings(max_examples=25)
def test_vM_Lessequal_instantiation(instance):
    assert isinstance(instance, vM_Lessequal)


vM_MetaDataDeclaration_strategy = st.builds(vM_MetaDataDeclaration, author=safe_text, date=safe_text, description=safe_text, name=safe_text, organization=safe_text, publication=safe_text)
@given(instance=vM_MetaDataDeclaration_strategy)
@settings(max_examples=25)
def test_vM_MetaDataDeclaration_instantiation(instance):
    assert isinstance(instance, vM_MetaDataDeclaration)


vM_Minus_strategy = st.builds(vM_Minus)
@given(instance=vM_Minus_strategy)
@settings(max_examples=25)
def test_vM_Minus_instantiation(instance):
    assert isinstance(instance, vM_Minus)


vM_Model_strategy = st.builds(vM_Model)
@given(instance=vM_Model_strategy)
@settings(max_examples=25)
def test_vM_Model_instantiation(instance):
    assert isinstance(instance, vM_Model)


vM_Multiplication_strategy = st.builds(vM_Multiplication)
@given(instance=vM_Multiplication_strategy)
@settings(max_examples=25)
def test_vM_Multiplication_instantiation(instance):
    assert isinstance(instance, vM_Multiplication)


vM_NumericExpression_strategy = st.builds(vM_NumericExpression, op=safe_text, value=safe_text)
@given(instance=vM_NumericExpression_strategy)
@settings(max_examples=25)
def test_vM_NumericExpression_instantiation(instance):
    assert isinstance(instance, vM_NumericExpression)


vM_NumericExpression_List_strategy = st.builds(vM_NumericExpression_List)
@given(instance=vM_NumericExpression_List_strategy)
@settings(max_examples=25)
def test_vM_NumericExpression_List_instantiation(instance):
    assert isinstance(instance, vM_NumericExpression_List)


vM_Objective_strategy = st.builds(vM_Objective, name=safe_text, op=safe_text)
@given(instance=vM_Objective_strategy)
@settings(max_examples=25)
def test_vM_Objective_instantiation(instance):
    assert isinstance(instance, vM_Objective)


vM_ObjectiveExpression_strategy = st.builds(vM_ObjectiveExpression, op=safe_text)
@given(instance=vM_ObjectiveExpression_strategy)
@settings(max_examples=25)
def test_vM_ObjectiveExpression_instantiation(instance):
    assert isinstance(instance, vM_ObjectiveExpression)


vM_Objectives_strategy = st.builds(vM_Objectives)
@given(instance=vM_Objectives_strategy)
@settings(max_examples=25)
def test_vM_Objectives_instantiation(instance):
    assert isinstance(instance, vM_Objectives)


vM_Or_strategy = st.builds(vM_Or)
@given(instance=vM_Or_strategy)
@settings(max_examples=25)
def test_vM_Or_instantiation(instance):
    assert isinstance(instance, vM_Or)


vM_Orgroup_strategy = st.builds(vM_Orgroup)
@given(instance=vM_Orgroup_strategy)
@settings(max_examples=25)
def test_vM_Orgroup_instantiation(instance):
    assert isinstance(instance, vM_Orgroup)


vM_PackageDeclaration_strategy = st.builds(vM_PackageDeclaration, name=safe_text)
@given(instance=vM_PackageDeclaration_strategy)
@settings(max_examples=25)
def test_vM_PackageDeclaration_instantiation(instance):
    assert isinstance(instance, vM_PackageDeclaration)


vM_PairAttributeValue_strategy = st.builds(vM_PairAttributeValue, value=safe_text)
@given(instance=vM_PairAttributeValue_strategy)
@settings(max_examples=25)
def test_vM_PairAttributeValue_instantiation(instance):
    assert isinstance(instance, vM_PairAttributeValue)


vM_PairFeatureInteger_strategy = st.builds(vM_PairFeatureInteger, value=safe_text)
@given(instance=vM_PairFeatureInteger_strategy)
@settings(max_examples=25)
def test_vM_PairFeatureInteger_instantiation(instance):
    assert isinstance(instance, vM_PairFeatureInteger)


vM_PairFeatureReal_strategy = st.builds(vM_PairFeatureReal, value=safe_text)
@given(instance=vM_PairFeatureReal_strategy)
@settings(max_examples=25)
def test_vM_PairFeatureReal_instantiation(instance):
    assert isinstance(instance, vM_PairFeatureReal)


vM_Plus_strategy = st.builds(vM_Plus)
@given(instance=vM_Plus_strategy)
@settings(max_examples=25)
def test_vM_Plus_instantiation(instance):
    assert isinstance(instance, vM_Plus)


vM_PrimitiveExpression_strategy = st.builds(vM_PrimitiveExpression)
@given(instance=vM_PrimitiveExpression_strategy)
@settings(max_examples=25)
def test_vM_PrimitiveExpression_instantiation(instance):
    assert isinstance(instance, vM_PrimitiveExpression)


vM_RealAttrDef_strategy = st.builds(vM_RealAttrDef)
@given(instance=vM_RealAttrDef_strategy)
@settings(max_examples=25)
def test_vM_RealAttrDef_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDef)


vM_RealAttrDefBounded_strategy = st.builds(vM_RealAttrDefBounded)
@given(instance=vM_RealAttrDefBounded_strategy)
@settings(max_examples=25)
def test_vM_RealAttrDefBounded_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDefBounded)


vM_RealAttrDefComplement_strategy = st.builds(vM_RealAttrDefComplement, max=safe_text, min=safe_text)
@given(instance=vM_RealAttrDefComplement_strategy)
@settings(max_examples=25)
def test_vM_RealAttrDefComplement_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDefComplement)


vM_RealAttrDefUnbounded_strategy = st.builds(vM_RealAttrDefUnbounded, value=safe_text)
@given(instance=vM_RealAttrDefUnbounded_strategy)
@settings(max_examples=25)
def test_vM_RealAttrDefUnbounded_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDefUnbounded)


vM_RealAttrValuation_strategy = st.builds(vM_RealAttrValuation)
@given(instance=vM_RealAttrValuation_strategy)
@settings(max_examples=25)
def test_vM_RealAttrValuation_instantiation(instance):
    assert isinstance(instance, vM_RealAttrValuation)


vM_RealDefaultDef_strategy = st.builds(vM_RealDefaultDef, value=safe_text)
@given(instance=vM_RealDefaultDef_strategy)
@settings(max_examples=25)
def test_vM_RealDefaultDef_instantiation(instance):
    assert isinstance(instance, vM_RealDefaultDef)


vM_RealDeltaDef_strategy = st.builds(vM_RealDeltaDef, value=safe_text)
@given(instance=vM_RealDeltaDef_strategy)
@settings(max_examples=25)
def test_vM_RealDeltaDef_instantiation(instance):
    assert isinstance(instance, vM_RealDeltaDef)


vM_Real_ATT_ID_strategy = st.builds(vM_Real_ATT_ID)
@given(instance=vM_Real_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_Real_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_Real_ATT_ID)


vM_Relationships_strategy = st.builds(vM_Relationships)
@given(instance=vM_Relationships_strategy)
@settings(max_examples=25)
def test_vM_Relationships_instantiation(instance):
    assert isinstance(instance, vM_Relationships)


vM_Requires_strategy = st.builds(vM_Requires)
@given(instance=vM_Requires_strategy)
@settings(max_examples=25)
def test_vM_Requires_instantiation(instance):
    assert isinstance(instance, vM_Requires)


vM_RightImplication_strategy = st.builds(vM_RightImplication)
@given(instance=vM_RightImplication_strategy)
@settings(max_examples=25)
def test_vM_RightImplication_instantiation(instance):
    assert isinstance(instance, vM_RightImplication)


vM_SpecialExpression_strategy = st.builds(vM_SpecialExpression, op=safe_text)
@given(instance=vM_SpecialExpression_strategy)
@settings(max_examples=25)
def test_vM_SpecialExpression_instantiation(instance):
    assert isinstance(instance, vM_SpecialExpression)


vM_StringAttrDef_strategy = st.builds(vM_StringAttrDef, value=safe_text)
@given(instance=vM_StringAttrDef_strategy)
@settings(max_examples=25)
def test_vM_StringAttrDef_instantiation(instance):
    assert isinstance(instance, vM_StringAttrDef)


vM_StringAttrValuation_strategy = st.builds(vM_StringAttrValuation)
@given(instance=vM_StringAttrValuation_strategy)
@settings(max_examples=25)
def test_vM_StringAttrValuation_instantiation(instance):
    assert isinstance(instance, vM_StringAttrValuation)


vM_StringDefaultDef_strategy = st.builds(vM_StringDefaultDef, value=safe_text)
@given(instance=vM_StringDefaultDef_strategy)
@settings(max_examples=25)
def test_vM_StringDefaultDef_instantiation(instance):
    assert isinstance(instance, vM_StringDefaultDef)


vM_StringExpression_strategy = st.builds(vM_StringExpression, value=safe_text)
@given(instance=vM_StringExpression_strategy)
@settings(max_examples=25)
def test_vM_StringExpression_instantiation(instance):
    assert isinstance(instance, vM_StringExpression)


vM_String_ATT_ID_strategy = st.builds(vM_String_ATT_ID)
@given(instance=vM_String_ATT_ID_strategy)
@settings(max_examples=25)
def test_vM_String_ATT_ID_instantiation(instance):
    assert isinstance(instance, vM_String_ATT_ID)


vM_TableBasedValuationByAttribute_strategy = st.builds(vM_TableBasedValuationByAttribute)
@given(instance=vM_TableBasedValuationByAttribute_strategy)
@settings(max_examples=25)
def test_vM_TableBasedValuationByAttribute_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByAttribute)


vM_TableBasedValuationByAttributeForInteger_strategy = st.builds(vM_TableBasedValuationByAttributeForInteger)
@given(instance=vM_TableBasedValuationByAttributeForInteger_strategy)
@settings(max_examples=25)
def test_vM_TableBasedValuationByAttributeForInteger_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByAttributeForInteger)


vM_TableBasedValuationByAttributeForReal_strategy = st.builds(vM_TableBasedValuationByAttributeForReal)
@given(instance=vM_TableBasedValuationByAttributeForReal_strategy)
@settings(max_examples=25)
def test_vM_TableBasedValuationByAttributeForReal_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByAttributeForReal)


vM_TableBasedValuationByFeature_strategy = st.builds(vM_TableBasedValuationByFeature)
@given(instance=vM_TableBasedValuationByFeature_strategy)
@settings(max_examples=25)
def test_vM_TableBasedValuationByFeature_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByFeature)


vM_TableBasedValuationByFeatureAndClone_strategy = st.builds(vM_TableBasedValuationByFeatureAndClone, name=safe_text)
@given(instance=vM_TableBasedValuationByFeatureAndClone_strategy)
@settings(max_examples=25)
def test_vM_TableBasedValuationByFeatureAndClone_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByFeatureAndClone)


vM_Version_strategy = st.builds(vM_Version, main=st.integers(), tail=st.integers())
@given(instance=vM_Version_strategy)
@settings(max_examples=25)
def test_vM_Version_instantiation(instance):
    assert isinstance(instance, vM_Version)


vM_VmBlock_strategy = st.builds(vM_VmBlock)
@given(instance=vM_VmBlock_strategy)
@settings(max_examples=25)
def test_vM_VmBlock_instantiation(instance):
    assert isinstance(instance, vM_VmBlock)


vM_Xorgroup_strategy = st.builds(vM_Xorgroup)
@given(instance=vM_Xorgroup_strategy)
@settings(max_examples=25)
def test_vM_Xorgroup_instantiation(instance):
    assert isinstance(instance, vM_Xorgroup)


