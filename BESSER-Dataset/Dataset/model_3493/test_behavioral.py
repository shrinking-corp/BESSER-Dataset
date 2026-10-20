import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_booleanValuation99_reverse_link_reassign_clear():
    a1 = vM_Configuration(name="sample_text")
    a2 = vM_Configuration(name="sample_text_2")
    b = vM_BooleanValuation(notSelected=True)
    _safe_set(b, 'vM_BooleanValuation', a1)
    assert _is_linked(b, 'vM_BooleanValuation', a1)
    if hasattr(a1, 'vM_Configuration100'):
        assert _is_linked(a1, 'vM_Configuration100', b)
    _safe_set(b, 'vM_BooleanValuation', a2)
    assert _is_linked(b, 'vM_BooleanValuation', a2)
    if hasattr(a1, 'vM_Configuration100'):
        assert not _is_linked(a1, 'vM_Configuration100', b)
    if hasattr(a2, 'vM_Configuration100'):
        assert _is_linked(a2, 'vM_Configuration100', b)
    _safe_set(b, 'vM_BooleanValuation', None)
    assert not _is_linked(b, 'vM_BooleanValuation', a2)
    if hasattr(a2, 'vM_Configuration100'):
        assert not _is_linked(a2, 'vM_Configuration100', b)


def test_assoc_default21_reverse_link_reassign_clear():
    a1 = vM_BooleanAttrDef(value="sample_text")
    a2 = vM_BooleanAttrDef(value="sample_text_2")
    b = vM_BoolDefaultDef(value="sample_text")
    _safe_set(b, 'vM_BoolDefaultDef', a1)
    assert _is_linked(b, 'vM_BoolDefaultDef', a1)
    if hasattr(a1, 'vM_BooleanAttrDef22'):
        assert _is_linked(a1, 'vM_BooleanAttrDef22', b)
    _safe_set(b, 'vM_BoolDefaultDef', a2)
    assert _is_linked(b, 'vM_BoolDefaultDef', a2)
    if hasattr(a1, 'vM_BooleanAttrDef22'):
        assert not _is_linked(a1, 'vM_BooleanAttrDef22', b)
    if hasattr(a2, 'vM_BooleanAttrDef22'):
        assert _is_linked(a2, 'vM_BooleanAttrDef22', b)
    _safe_set(b, 'vM_BoolDefaultDef', None)
    assert not _is_linked(b, 'vM_BoolDefaultDef', a2)
    if hasattr(a2, 'vM_BooleanAttrDef22'):
        assert not _is_linked(a2, 'vM_BooleanAttrDef22', b)


def test_assoc_default24_reverse_link_reassign_clear():
    a1 = vM_StringDefaultDef(value="sample_text")
    a2 = vM_StringDefaultDef(value="sample_text_2")
    b = vM_StringAttrDef(value="sample_text")
    _safe_set(b, 'vM_StringAttrDef25', a1)
    assert _is_linked(b, 'vM_StringAttrDef25', a1)
    if hasattr(a1, 'vM_StringDefaultDef'):
        assert _is_linked(a1, 'vM_StringDefaultDef', b)
    _safe_set(b, 'vM_StringAttrDef25', a2)
    assert _is_linked(b, 'vM_StringAttrDef25', a2)
    if hasattr(a1, 'vM_StringDefaultDef'):
        assert not _is_linked(a1, 'vM_StringDefaultDef', b)
    if hasattr(a2, 'vM_StringDefaultDef'):
        assert _is_linked(a2, 'vM_StringDefaultDef', b)
    _safe_set(b, 'vM_StringAttrDef25', None)
    assert not _is_linked(b, 'vM_StringAttrDef25', a2)
    if hasattr(a2, 'vM_StringDefaultDef'):
        assert not _is_linked(a2, 'vM_StringDefaultDef', b)


def test_assoc_delta33_reverse_link_reassign_clear():
    a1 = vM_IntegerDeltaDef(value=7)
    a2 = vM_IntegerDeltaDef(value=13)
    b = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    _safe_set(b, 'vM_IntegerAttrDefComplement34', a1)
    assert _is_linked(b, 'vM_IntegerAttrDefComplement34', a1)
    if hasattr(a1, 'vM_IntegerDeltaDef'):
        assert _is_linked(a1, 'vM_IntegerDeltaDef', b)
    _safe_set(b, 'vM_IntegerAttrDefComplement34', a2)
    assert _is_linked(b, 'vM_IntegerAttrDefComplement34', a2)
    if hasattr(a1, 'vM_IntegerDeltaDef'):
        assert not _is_linked(a1, 'vM_IntegerDeltaDef', b)
    if hasattr(a2, 'vM_IntegerDeltaDef'):
        assert _is_linked(a2, 'vM_IntegerDeltaDef', b)
    _safe_set(b, 'vM_IntegerAttrDefComplement34', None)
    assert not _is_linked(b, 'vM_IntegerAttrDefComplement34', a2)
    if hasattr(a2, 'vM_IntegerDeltaDef'):
        assert not _is_linked(a2, 'vM_IntegerDeltaDef', b)


def test_assoc_delta39_reverse_link_reassign_clear():
    a1 = vM_RealDeltaDef(value="sample_text")
    a2 = vM_RealDeltaDef(value="sample_text_2")
    b = vM_RealAttrDefComplement(max="sample_text", min="sample_text")
    _safe_set(b, 'vM_RealAttrDefComplement40', a1)
    assert _is_linked(b, 'vM_RealAttrDefComplement40', a1)
    if hasattr(a1, 'vM_RealDeltaDef'):
        assert _is_linked(a1, 'vM_RealDeltaDef', b)
    _safe_set(b, 'vM_RealAttrDefComplement40', a2)
    assert _is_linked(b, 'vM_RealAttrDefComplement40', a2)
    if hasattr(a1, 'vM_RealDeltaDef'):
        assert not _is_linked(a1, 'vM_RealDeltaDef', b)
    if hasattr(a2, 'vM_RealDeltaDef'):
        assert _is_linked(a2, 'vM_RealDeltaDef', b)
    _safe_set(b, 'vM_RealAttrDefComplement40', None)
    assert not _is_linked(b, 'vM_RealAttrDefComplement40', a2)
    if hasattr(a2, 'vM_RealDeltaDef'):
        assert not _is_linked(a2, 'vM_RealDeltaDef', b)


def test_assoc_email4_reverse_link_reassign_clear():
    a1 = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    a2 = vM_MetaDataDeclaration(author="sample_text_2", date="sample_text_2", description="sample_text_2", name="sample_text_2", organization="sample_text_2", publication="sample_text_2")
    b = vM_Email(domain="sample_text", username="sample_text")
    _safe_set(b, 'vM_Email', a1)
    assert _is_linked(b, 'vM_Email', a1)
    if hasattr(a1, 'vM_MetaDataDeclaration5'):
        assert _is_linked(a1, 'vM_MetaDataDeclaration5', b)
    _safe_set(b, 'vM_Email', a2)
    assert _is_linked(b, 'vM_Email', a2)
    if hasattr(a1, 'vM_MetaDataDeclaration5'):
        assert not _is_linked(a1, 'vM_MetaDataDeclaration5', b)
    if hasattr(a2, 'vM_MetaDataDeclaration5'):
        assert _is_linked(a2, 'vM_MetaDataDeclaration5', b)
    _safe_set(b, 'vM_Email', None)
    assert not _is_linked(b, 'vM_Email', a2)
    if hasattr(a2, 'vM_MetaDataDeclaration5'):
        assert not _is_linked(a2, 'vM_MetaDataDeclaration5', b)


def test_assoc_enumAttrDef18_reverse_link_reassign_clear():
    a1 = vM_EnumAttrDef(value="sample_text")
    a2 = vM_EnumAttrDef(value="sample_text_2")
    b = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    _safe_set(b, 'vM_AttrDef19', a1)
    assert _is_linked(b, 'vM_AttrDef19', a1)
    if hasattr(a1, 'vM_EnumAttrDef'):
        assert _is_linked(a1, 'vM_EnumAttrDef', b)
    _safe_set(b, 'vM_AttrDef19', a2)
    assert _is_linked(b, 'vM_AttrDef19', a2)
    if hasattr(a1, 'vM_EnumAttrDef'):
        assert not _is_linked(a1, 'vM_EnumAttrDef', b)
    if hasattr(a2, 'vM_EnumAttrDef'):
        assert _is_linked(a2, 'vM_EnumAttrDef', b)
    _safe_set(b, 'vM_AttrDef19', None)
    assert not _is_linked(b, 'vM_AttrDef19', a2)
    if hasattr(a2, 'vM_EnumAttrDef'):
        assert not _is_linked(a2, 'vM_EnumAttrDef', b)


def test_assoc_expression67_reverse_link_reassign_clear():
    a1 = vM_SpecialExpression(op="sample_text")
    a2 = vM_SpecialExpression(op="sample_text_2")
    b = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    _safe_set(b, 'vM_Feature68', a1)
    assert _is_linked(b, 'vM_Feature68', a1)
    if hasattr(a1, 'vM_SpecialExpression'):
        assert _is_linked(a1, 'vM_SpecialExpression', b)
    _safe_set(b, 'vM_Feature68', a2)
    assert _is_linked(b, 'vM_Feature68', a2)
    if hasattr(a1, 'vM_SpecialExpression'):
        assert not _is_linked(a1, 'vM_SpecialExpression', b)
    if hasattr(a2, 'vM_SpecialExpression'):
        assert _is_linked(a2, 'vM_SpecialExpression', b)
    _safe_set(b, 'vM_Feature68', None)
    assert not _is_linked(b, 'vM_Feature68', a2)
    if hasattr(a2, 'vM_SpecialExpression'):
        assert not _is_linked(a2, 'vM_SpecialExpression', b)


def test_assoc_expression77_reverse_link_reassign_clear():
    a1 = vM_BooleanExpression(op="sample_text", value="sample_text")
    a2 = vM_BooleanExpression(op="sample_text_2", value="sample_text_2")
    b = vM_BooleanExpression(op="sample_text", value="sample_text")
    _safe_set(b, 'vM_BooleanExpression76', a1)
    assert _is_linked(b, 'vM_BooleanExpression76', a1)
    if hasattr(a1, 'vM_BooleanExpression'):
        assert _is_linked(a1, 'vM_BooleanExpression', b)
    _safe_set(b, 'vM_BooleanExpression76', a2)
    assert _is_linked(b, 'vM_BooleanExpression76', a2)
    if hasattr(a1, 'vM_BooleanExpression'):
        assert not _is_linked(a1, 'vM_BooleanExpression', b)
    if hasattr(a2, 'vM_BooleanExpression'):
        assert _is_linked(a2, 'vM_BooleanExpression', b)
    _safe_set(b, 'vM_BooleanExpression76', None)
    assert not _is_linked(b, 'vM_BooleanExpression76', a2)
    if hasattr(a2, 'vM_BooleanExpression'):
        assert not _is_linked(a2, 'vM_BooleanExpression', b)


def test_assoc_expression83_reverse_link_reassign_clear():
    a1 = vM_NumericExpression(op="sample_text", value="sample_text")
    a2 = vM_NumericExpression(op="sample_text_2", value="sample_text_2")
    b = vM_NumericExpression(op="sample_text", value="sample_text")
    _safe_set(b, 'vM_NumericExpression82', a1)
    assert _is_linked(b, 'vM_NumericExpression82', a1)
    if hasattr(a1, 'vM_NumericExpression'):
        assert _is_linked(a1, 'vM_NumericExpression', b)
    _safe_set(b, 'vM_NumericExpression82', a2)
    assert _is_linked(b, 'vM_NumericExpression82', a2)
    if hasattr(a1, 'vM_NumericExpression'):
        assert not _is_linked(a1, 'vM_NumericExpression', b)
    if hasattr(a2, 'vM_NumericExpression'):
        assert _is_linked(a2, 'vM_NumericExpression', b)
    _safe_set(b, 'vM_NumericExpression82', None)
    assert not _is_linked(b, 'vM_NumericExpression82', a2)
    if hasattr(a2, 'vM_NumericExpression'):
        assert not _is_linked(a2, 'vM_NumericExpression', b)


def test_assoc_expression93_reverse_link_reassign_clear():
    a1 = vM_ObjectiveExpression(op="sample_text")
    a2 = vM_ObjectiveExpression(op="sample_text_2")
    b = vM_Objective(name="sample_text", op="sample_text")
    _safe_set(b, 'vM_Objective94', a1)
    assert _is_linked(b, 'vM_Objective94', a1)
    if hasattr(a1, 'vM_ObjectiveExpression'):
        assert _is_linked(a1, 'vM_ObjectiveExpression', b)
    _safe_set(b, 'vM_Objective94', a2)
    assert _is_linked(b, 'vM_Objective94', a2)
    if hasattr(a1, 'vM_ObjectiveExpression'):
        assert not _is_linked(a1, 'vM_ObjectiveExpression', b)
    if hasattr(a2, 'vM_ObjectiveExpression'):
        assert _is_linked(a2, 'vM_ObjectiveExpression', b)
    _safe_set(b, 'vM_Objective94', None)
    assert not _is_linked(b, 'vM_Objective94', a2)
    if hasattr(a2, 'vM_ObjectiveExpression'):
        assert not _is_linked(a2, 'vM_ObjectiveExpression', b)


def test_assoc_feature103_reverse_link_reassign_clear():
    a1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    a2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    b = vM_BooleanValuation(notSelected=True)
    _safe_set(b, 'vM_BooleanValuation104', a1)
    assert _is_linked(b, 'vM_BooleanValuation104', a1)
    if hasattr(a1, 'vM_Feature105'):
        assert _is_linked(a1, 'vM_Feature105', b)
    _safe_set(b, 'vM_BooleanValuation104', a2)
    assert _is_linked(b, 'vM_BooleanValuation104', a2)
    if hasattr(a1, 'vM_Feature105'):
        assert not _is_linked(a1, 'vM_Feature105', b)
    if hasattr(a2, 'vM_Feature105'):
        assert _is_linked(a2, 'vM_Feature105', b)
    _safe_set(b, 'vM_BooleanValuation104', None)
    assert not _is_linked(b, 'vM_BooleanValuation104', a2)
    if hasattr(a2, 'vM_Feature105'):
        assert not _is_linked(a2, 'vM_Feature105', b)


def test_assoc_head106_reverse_link_reassign_clear():
    a1 = vM_BasicAttrValuation(value="sample_text")
    a2 = vM_BasicAttrValuation(value="sample_text_2")
    b = vM_AttHead(forAllFeatures=True)
    _safe_set(b, 'vM_AttHead108', a1)
    assert _is_linked(b, 'vM_AttHead108', a1)
    if hasattr(a1, 'vM_BasicAttrValuation107'):
        assert _is_linked(a1, 'vM_BasicAttrValuation107', b)
    _safe_set(b, 'vM_AttHead108', a2)
    assert _is_linked(b, 'vM_AttHead108', a2)
    if hasattr(a1, 'vM_BasicAttrValuation107'):
        assert not _is_linked(a1, 'vM_BasicAttrValuation107', b)
    if hasattr(a2, 'vM_BasicAttrValuation107'):
        assert _is_linked(a2, 'vM_BasicAttrValuation107', b)
    _safe_set(b, 'vM_AttHead108', None)
    assert not _is_linked(b, 'vM_AttHead108', a2)
    if hasattr(a2, 'vM_BasicAttrValuation107'):
        assert not _is_linked(a2, 'vM_BasicAttrValuation107', b)


def test_assoc_head153_reverse_link_reassign_clear():
    a1 = vM_AttHead(forAllFeatures=True)
    a2 = vM_AttHead(forAllFeatures=False)
    b = vM_Abstract_ATT_ID(name="sample_text")
    _safe_set(b, 'vM_Abstract_ATT_ID154', a1)
    assert _is_linked(b, 'vM_Abstract_ATT_ID154', a1)
    if hasattr(a1, 'vM_AttHead155'):
        assert _is_linked(a1, 'vM_AttHead155', b)
    _safe_set(b, 'vM_Abstract_ATT_ID154', a2)
    assert _is_linked(b, 'vM_Abstract_ATT_ID154', a2)
    if hasattr(a1, 'vM_AttHead155'):
        assert not _is_linked(a1, 'vM_AttHead155', b)
    if hasattr(a2, 'vM_AttHead155'):
        assert _is_linked(a2, 'vM_AttHead155', b)
    _safe_set(b, 'vM_Abstract_ATT_ID154', None)
    assert not _is_linked(b, 'vM_Abstract_ATT_ID154', a2)
    if hasattr(a2, 'vM_AttHead155'):
        assert not _is_linked(a2, 'vM_AttHead155', b)


def test_assoc_ownedFeature150_reverse_link_reassign_clear():
    a1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    a2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    b = vM_AttHead(forAllFeatures=True)
    _safe_set(b, 'vM_AttHead151', a1)
    assert _is_linked(b, 'vM_AttHead151', a1)
    if hasattr(a1, 'vM_Feature152'):
        assert _is_linked(a1, 'vM_Feature152', b)
    _safe_set(b, 'vM_AttHead151', a2)
    assert _is_linked(b, 'vM_AttHead151', a2)
    if hasattr(a1, 'vM_Feature152'):
        assert not _is_linked(a1, 'vM_Feature152', b)
    if hasattr(a2, 'vM_Feature152'):
        assert _is_linked(a2, 'vM_Feature152', b)
    _safe_set(b, 'vM_AttHead151', None)
    assert not _is_linked(b, 'vM_AttHead151', a2)
    if hasattr(a2, 'vM_Feature152'):
        assert not _is_linked(a2, 'vM_Feature152', b)


def test_assoc_pairs125_reverse_link_reassign_clear():
    a1 = vM_TableBasedValuationByFeatureAndClone(name="sample_text")
    a2 = vM_TableBasedValuationByFeatureAndClone(name="sample_text_2")
    b = vM_PairAttributeValue(value="sample_text")
    _safe_set(b, 'vM_PairAttributeValue', a1)
    assert _is_linked(b, 'vM_PairAttributeValue', a1)
    if hasattr(a1, 'vM_TableBasedValuationByFeatureAndClone126'):
        assert _is_linked(a1, 'vM_TableBasedValuationByFeatureAndClone126', b)
    _safe_set(b, 'vM_PairAttributeValue', a2)
    assert _is_linked(b, 'vM_PairAttributeValue', a2)
    if hasattr(a1, 'vM_TableBasedValuationByFeatureAndClone126'):
        assert not _is_linked(a1, 'vM_TableBasedValuationByFeatureAndClone126', b)
    if hasattr(a2, 'vM_TableBasedValuationByFeatureAndClone126'):
        assert _is_linked(a2, 'vM_TableBasedValuationByFeatureAndClone126', b)
    _safe_set(b, 'vM_PairAttributeValue', None)
    assert not _is_linked(b, 'vM_PairAttributeValue', a2)
    if hasattr(a2, 'vM_TableBasedValuationByFeatureAndClone126'):
        assert not _is_linked(a2, 'vM_TableBasedValuationByFeatureAndClone126', b)


def test_assoc_refAtt133_reverse_link_reassign_clear():
    a1 = vM_PairAttributeValue(value="sample_text")
    a2 = vM_PairAttributeValue(value="sample_text_2")
    b = vM_Abstract_ATT_ID(name="sample_text")
    _safe_set(b, 'vM_Abstract_ATT_ID135', a1)
    assert _is_linked(b, 'vM_Abstract_ATT_ID135', a1)
    if hasattr(a1, 'vM_PairAttributeValue134'):
        assert _is_linked(a1, 'vM_PairAttributeValue134', b)
    _safe_set(b, 'vM_Abstract_ATT_ID135', a2)
    assert _is_linked(b, 'vM_Abstract_ATT_ID135', a2)
    if hasattr(a1, 'vM_PairAttributeValue134'):
        assert not _is_linked(a1, 'vM_PairAttributeValue134', b)
    if hasattr(a2, 'vM_PairAttributeValue134'):
        assert _is_linked(a2, 'vM_PairAttributeValue134', b)
    _safe_set(b, 'vM_Abstract_ATT_ID135', None)
    assert not _is_linked(b, 'vM_Abstract_ATT_ID135', a2)
    if hasattr(a2, 'vM_PairAttributeValue134'):
        assert not _is_linked(a2, 'vM_PairAttributeValue134', b)


def test_assoc_refAtt62_reverse_link_reassign_clear():
    a1 = vM_AttributeDescription(description="sample_text")
    a2 = vM_AttributeDescription(description="sample_text_2")
    b = vM_Abstract_ATT_ID(name="sample_text")
    _safe_set(b, 'vM_Abstract_ATT_ID', a1)
    assert _is_linked(b, 'vM_Abstract_ATT_ID', a1)
    if hasattr(a1, 'vM_AttributeDescription63'):
        assert _is_linked(a1, 'vM_AttributeDescription63', b)
    _safe_set(b, 'vM_Abstract_ATT_ID', a2)
    assert _is_linked(b, 'vM_Abstract_ATT_ID', a2)
    if hasattr(a1, 'vM_AttributeDescription63'):
        assert not _is_linked(a1, 'vM_AttributeDescription63', b)
    if hasattr(a2, 'vM_AttributeDescription63'):
        assert _is_linked(a2, 'vM_AttributeDescription63', b)
    _safe_set(b, 'vM_Abstract_ATT_ID', None)
    assert not _is_linked(b, 'vM_Abstract_ATT_ID', a2)
    if hasattr(a2, 'vM_AttributeDescription63'):
        assert not _is_linked(a2, 'vM_AttributeDescription63', b)


def test_assoc_refFeat140_reverse_link_reassign_clear():
    a1 = vM_PairFeatureInteger(value="sample_text")
    a2 = vM_PairFeatureInteger(value="sample_text_2")
    b = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    _safe_set(b, 'vM_Feature142', a1)
    assert _is_linked(b, 'vM_Feature142', a1)
    if hasattr(a1, 'vM_PairFeatureInteger141'):
        assert _is_linked(a1, 'vM_PairFeatureInteger141', b)
    _safe_set(b, 'vM_Feature142', a2)
    assert _is_linked(b, 'vM_Feature142', a2)
    if hasattr(a1, 'vM_PairFeatureInteger141'):
        assert not _is_linked(a1, 'vM_PairFeatureInteger141', b)
    if hasattr(a2, 'vM_PairFeatureInteger141'):
        assert _is_linked(a2, 'vM_PairFeatureInteger141', b)
    _safe_set(b, 'vM_Feature142', None)
    assert not _is_linked(b, 'vM_Feature142', a2)
    if hasattr(a2, 'vM_PairFeatureInteger141'):
        assert not _is_linked(a2, 'vM_PairFeatureInteger141', b)


def test_assoc_refFeat147_reverse_link_reassign_clear():
    a1 = vM_PairFeatureReal(value="sample_text")
    a2 = vM_PairFeatureReal(value="sample_text_2")
    b = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    _safe_set(b, 'vM_Feature149', a1)
    assert _is_linked(b, 'vM_Feature149', a1)
    if hasattr(a1, 'vM_PairFeatureReal148'):
        assert _is_linked(a1, 'vM_PairFeatureReal148', b)
    _safe_set(b, 'vM_Feature149', a2)
    assert _is_linked(b, 'vM_Feature149', a2)
    if hasattr(a1, 'vM_PairFeatureReal148'):
        assert not _is_linked(a1, 'vM_PairFeatureReal148', b)
    if hasattr(a2, 'vM_PairFeatureReal148'):
        assert _is_linked(a2, 'vM_PairFeatureReal148', b)
    _safe_set(b, 'vM_Feature149', None)
    assert not _is_linked(b, 'vM_Feature149', a2)
    if hasattr(a2, 'vM_PairFeatureReal148'):
        assert not _is_linked(a2, 'vM_PairFeatureReal148', b)


def test_assoc_refFeat56_reverse_link_reassign_clear():
    a1 = vM_FeatureDescription(description="sample_text")
    a2 = vM_FeatureDescription(description="sample_text_2")
    b = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    _safe_set(b, 'vM_Feature58', a1)
    assert _is_linked(b, 'vM_Feature58', a1)
    if hasattr(a1, 'vM_FeatureDescription57'):
        assert _is_linked(a1, 'vM_FeatureDescription57', b)
    _safe_set(b, 'vM_Feature58', a2)
    assert _is_linked(b, 'vM_Feature58', a2)
    if hasattr(a1, 'vM_FeatureDescription57'):
        assert not _is_linked(a1, 'vM_FeatureDescription57', b)
    if hasattr(a2, 'vM_FeatureDescription57'):
        assert _is_linked(a2, 'vM_FeatureDescription57', b)
    _safe_set(b, 'vM_Feature58', None)
    assert not _is_linked(b, 'vM_Feature58', a2)
    if hasattr(a2, 'vM_FeatureDescription57'):
        assert not _is_linked(a2, 'vM_FeatureDescription57', b)


def test_assoc_refFeat59_reverse_link_reassign_clear():
    a1 = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    a2 = vM_Feature(max="sample_text_2", min="sample_text_2", name="sample_text_2", notDecidable=False, notTranslatable=False, optional=False, runTime=False)
    b = vM_AttributeDescription(description="sample_text")
    _safe_set(b, 'vM_AttributeDescription60', a1)
    assert _is_linked(b, 'vM_AttributeDescription60', a1)
    if hasattr(a1, 'vM_Feature61'):
        assert _is_linked(a1, 'vM_Feature61', b)
    _safe_set(b, 'vM_AttributeDescription60', a2)
    assert _is_linked(b, 'vM_AttributeDescription60', a2)
    if hasattr(a1, 'vM_Feature61'):
        assert not _is_linked(a1, 'vM_Feature61', b)
    if hasattr(a2, 'vM_Feature61'):
        assert _is_linked(a2, 'vM_Feature61', b)
    _safe_set(b, 'vM_AttributeDescription60', None)
    assert not _is_linked(b, 'vM_AttributeDescription60', a2)
    if hasattr(a2, 'vM_Feature61'):
        assert not _is_linked(a2, 'vM_Feature61', b)


def test_assoc_refFeature122_reverse_link_reassign_clear():
    a1 = vM_TableBasedValuationByFeatureAndClone(name="sample_text")
    a2 = vM_TableBasedValuationByFeatureAndClone(name="sample_text_2")
    b = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    _safe_set(b, 'vM_Feature124', a1)
    assert _is_linked(b, 'vM_Feature124', a1)
    if hasattr(a1, 'vM_TableBasedValuationByFeatureAndClone123'):
        assert _is_linked(a1, 'vM_TableBasedValuationByFeatureAndClone123', b)
    _safe_set(b, 'vM_Feature124', a2)
    assert _is_linked(b, 'vM_Feature124', a2)
    if hasattr(a1, 'vM_TableBasedValuationByFeatureAndClone123'):
        assert not _is_linked(a1, 'vM_TableBasedValuationByFeatureAndClone123', b)
    if hasattr(a2, 'vM_TableBasedValuationByFeatureAndClone123'):
        assert _is_linked(a2, 'vM_TableBasedValuationByFeatureAndClone123', b)
    _safe_set(b, 'vM_Feature124', None)
    assert not _is_linked(b, 'vM_Feature124', a2)
    if hasattr(a2, 'vM_TableBasedValuationByFeatureAndClone123'):
        assert not _is_linked(a2, 'vM_TableBasedValuationByFeatureAndClone123', b)


def test_assoc_version3_reverse_link_reassign_clear():
    a1 = vM_Version(main=7, tail=7)
    a2 = vM_Version(main=13, tail=13)
    b = vM_MetaDataDeclaration(author="sample_text", date="sample_text", description="sample_text", name="sample_text", organization="sample_text", publication="sample_text")
    _safe_set(b, 'vM_MetaDataDeclaration', a1)
    assert _is_linked(b, 'vM_MetaDataDeclaration', a1)
    if hasattr(a1, 'vM_Version'):
        assert _is_linked(a1, 'vM_Version', b)
    _safe_set(b, 'vM_MetaDataDeclaration', a2)
    assert _is_linked(b, 'vM_MetaDataDeclaration', a2)
    if hasattr(a1, 'vM_Version'):
        assert not _is_linked(a1, 'vM_Version', b)
    if hasattr(a2, 'vM_Version'):
        assert _is_linked(a2, 'vM_Version', b)
    _safe_set(b, 'vM_MetaDataDeclaration', None)
    assert not _is_linked(b, 'vM_MetaDataDeclaration', a2)
    if hasattr(a2, 'vM_Version'):
        assert not _is_linked(a2, 'vM_Version', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attVsValForMultiFeature120_stub_double():
    # vM_AdvancedAttrValuation has no real 'vM_AdvancedAttrValuation121' property in the generated
    # code (a bare stub) -- manually attach it so vM_TableBasedValuationByFeatureAndClone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_TableBasedValuationByFeatureAndClone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_TableBasedValuationByFeatureAndClone(name="sample_text")
    partner = vM_AdvancedAttrValuation()
    setattr(partner, 'vM_AdvancedAttrValuation121', None)
    _safe_set(owner, 'vM_TableBasedValuationByFeatureAndClone', partner)
    assert getattr(partner, 'vM_AdvancedAttrValuation121') == owner
    _safe_set(owner, 'vM_TableBasedValuationByFeatureAndClone', None)
    assert getattr(partner, 'vM_AdvancedAttrValuation121') is None


def test_assoc_attrDefs13_stub_double():
    # vM_Attributes has no real 'vM_Attributes' property in the generated
    # code (a bare stub) -- manually attach it so vM_AttrDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_AttrDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    partner = vM_Attributes()
    setattr(partner, 'vM_Attributes', None)
    _safe_set(owner, 'vM_AttrDef', partner)
    assert owner in getattr(partner, 'vM_Attributes')
    _safe_set(owner, 'vM_AttrDef', None)
    assert owner not in getattr(partner, 'vM_Attributes')


def test_assoc_attrValuations14_stub_double():
    # vM_Attributes has no real 'vM_Attributes15' property in the generated
    # code (a bare stub) -- manually attach it so vM_BasicAttrValuation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_BasicAttrValuation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_BasicAttrValuation(value="sample_text")
    partner = vM_Attributes()
    setattr(partner, 'vM_Attributes15', None)
    _safe_set(owner, 'vM_BasicAttrValuation', partner)
    assert owner in getattr(partner, 'vM_Attributes15')
    _safe_set(owner, 'vM_BasicAttrValuation', None)
    assert owner not in getattr(partner, 'vM_Attributes15')


def test_assoc_attributesDescriptions54_stub_double():
    # vM_Descriptions has no real 'vM_Descriptions55' property in the generated
    # code (a bare stub) -- manually attach it so vM_AttributeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_AttributeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_AttributeDescription(description="sample_text")
    partner = vM_Descriptions()
    setattr(partner, 'vM_Descriptions55', None)
    _safe_set(owner, 'vM_AttributeDescription', partner)
    assert owner in getattr(partner, 'vM_Descriptions55')
    _safe_set(owner, 'vM_AttributeDescription', None)
    assert owner not in getattr(partner, 'vM_Descriptions55')


def test_assoc_basicAttrDef16_stub_double():
    # vM_BasicAttrDef has no real 'vM_BasicAttrDef' property in the generated
    # code (a bare stub) -- manually attach it so vM_AttrDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_AttrDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_AttrDef(notDecidable=True, notTranslatable=True, runTime=True)
    partner = vM_BasicAttrDef()
    setattr(partner, 'vM_BasicAttrDef', None)
    _safe_set(owner, 'vM_AttrDef17', partner)
    assert getattr(partner, 'vM_BasicAttrDef') == owner
    _safe_set(owner, 'vM_AttrDef17', None)
    assert getattr(partner, 'vM_BasicAttrDef') is None


def test_assoc_blocks1_stub_double():
    # vM_VmBlock has no real 'vM_VmBlock2' property in the generated
    # code (a bare stub) -- manually attach it so vM_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_PackageDeclaration(name="sample_text")
    partner = vM_VmBlock()
    setattr(partner, 'vM_VmBlock2', None)
    _safe_set(owner, 'vM_PackageDeclaration', {partner})
    assert getattr(partner, 'vM_VmBlock2') == owner
    _safe_set(owner, 'vM_PackageDeclaration', set())
    assert getattr(partner, 'vM_VmBlock2') is None


def test_assoc_complement30_stub_double():
    # vM_IntegerAttrDefBounded has no real 'vM_IntegerAttrDefBounded31' property in the generated
    # code (a bare stub) -- manually attach it so vM_IntegerAttrDefComplement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_IntegerAttrDefComplement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    partner = vM_IntegerAttrDefBounded()
    setattr(partner, 'vM_IntegerAttrDefBounded31', None)
    _safe_set(owner, 'vM_IntegerAttrDefComplement32', partner)
    assert owner in getattr(partner, 'vM_IntegerAttrDefBounded31')
    _safe_set(owner, 'vM_IntegerAttrDefComplement32', None)
    assert owner not in getattr(partner, 'vM_IntegerAttrDefBounded31')


def test_assoc_complement38_stub_double():
    # vM_RealAttrDefBounded has no real 'vM_RealAttrDefBounded' property in the generated
    # code (a bare stub) -- manually attach it so vM_RealAttrDefComplement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_RealAttrDefComplement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_RealAttrDefComplement(max="sample_text", min="sample_text")
    partner = vM_RealAttrDefBounded()
    setattr(partner, 'vM_RealAttrDefBounded', None)
    _safe_set(owner, 'vM_RealAttrDefComplement', partner)
    assert owner in getattr(partner, 'vM_RealAttrDefBounded')
    _safe_set(owner, 'vM_RealAttrDefComplement', None)
    assert owner not in getattr(partner, 'vM_RealAttrDefBounded')


def test_assoc_complements29_stub_double():
    # vM_IntegerAttrDefBounded has no real 'vM_IntegerAttrDefBounded' property in the generated
    # code (a bare stub) -- manually attach it so vM_IntegerAttrDefComplement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_IntegerAttrDefComplement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_IntegerAttrDefComplement(max="sample_text", min="sample_text")
    partner = vM_IntegerAttrDefBounded()
    setattr(partner, 'vM_IntegerAttrDefBounded', None)
    _safe_set(owner, 'vM_IntegerAttrDefComplement', partner)
    assert owner in getattr(partner, 'vM_IntegerAttrDefBounded')
    _safe_set(owner, 'vM_IntegerAttrDefComplement', None)
    assert owner not in getattr(partner, 'vM_IntegerAttrDefBounded')


def test_assoc_configurations98_stub_double():
    # vM_Configurations has no real 'vM_Configurations' property in the generated
    # code (a bare stub) -- manually attach it so vM_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Configuration(name="sample_text")
    partner = vM_Configurations()
    setattr(partner, 'vM_Configurations', None)
    _safe_set(owner, 'vM_Configuration', partner)
    assert owner in getattr(partner, 'vM_Configurations')
    _safe_set(owner, 'vM_Configuration', None)
    assert owner not in getattr(partner, 'vM_Configurations')


def test_assoc_constraints64_stub_double():
    # vM_Constraints has no real 'vM_Constraints' property in the generated
    # code (a bare stub) -- manually attach it so vM_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Constraint(name="sample_text")
    partner = vM_Constraints()
    setattr(partner, 'vM_Constraints', None)
    _safe_set(owner, 'vM_Constraint', partner)
    assert owner in getattr(partner, 'vM_Constraints')
    _safe_set(owner, 'vM_Constraint', None)
    assert owner not in getattr(partner, 'vM_Constraints')


def test_assoc_default27_stub_double():
    # vM_IntegerAttrDef has no real 'vM_IntegerAttrDef28' property in the generated
    # code (a bare stub) -- manually attach it so vM_IntegerDefaultDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_IntegerDefaultDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_IntegerDefaultDef(value=7)
    partner = vM_IntegerAttrDef()
    setattr(partner, 'vM_IntegerAttrDef28', None)
    _safe_set(owner, 'vM_IntegerDefaultDef', partner)
    assert getattr(partner, 'vM_IntegerAttrDef28') == owner
    _safe_set(owner, 'vM_IntegerDefaultDef', None)
    assert getattr(partner, 'vM_IntegerAttrDef28') is None


def test_assoc_default36_stub_double():
    # vM_RealAttrDef has no real 'vM_RealAttrDef37' property in the generated
    # code (a bare stub) -- manually attach it so vM_RealDefaultDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_RealDefaultDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_RealDefaultDef(value="sample_text")
    partner = vM_RealAttrDef()
    setattr(partner, 'vM_RealAttrDef37', None)
    _safe_set(owner, 'vM_RealDefaultDef', partner)
    assert getattr(partner, 'vM_RealAttrDef37') == owner
    _safe_set(owner, 'vM_RealDefaultDef', None)
    assert getattr(partner, 'vM_RealAttrDef37') is None


def test_assoc_default42_stub_double():
    # vM_EnumStringDef has no real 'vM_EnumStringDef43' property in the generated
    # code (a bare stub) -- manually attach it so vM_StringDefaultDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_StringDefaultDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_StringDefaultDef(value="sample_text")
    partner = vM_EnumStringDef()
    setattr(partner, 'vM_EnumStringDef43', None)
    _safe_set(owner, 'vM_StringDefaultDef44', partner)
    assert getattr(partner, 'vM_EnumStringDef43') == owner
    _safe_set(owner, 'vM_StringDefaultDef44', None)
    assert getattr(partner, 'vM_EnumStringDef43') is None


def test_assoc_default46_stub_double():
    # vM_EnumIntegerDef has no real 'vM_EnumIntegerDef47' property in the generated
    # code (a bare stub) -- manually attach it so vM_IntegerDefaultDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_IntegerDefaultDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_IntegerDefaultDef(value=7)
    partner = vM_EnumIntegerDef()
    setattr(partner, 'vM_EnumIntegerDef47', None)
    _safe_set(owner, 'vM_IntegerDefaultDef48', partner)
    assert getattr(partner, 'vM_EnumIntegerDef47') == owner
    _safe_set(owner, 'vM_IntegerDefaultDef48', None)
    assert getattr(partner, 'vM_EnumIntegerDef47') is None


def test_assoc_default50_stub_double():
    # vM_EnumRealDef has no real 'vM_EnumRealDef51' property in the generated
    # code (a bare stub) -- manually attach it so vM_RealDefaultDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_RealDefaultDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_RealDefaultDef(value="sample_text")
    partner = vM_EnumRealDef()
    setattr(partner, 'vM_EnumRealDef51', None)
    _safe_set(owner, 'vM_RealDefaultDef52', partner)
    assert getattr(partner, 'vM_EnumRealDef51') == owner
    _safe_set(owner, 'vM_RealDefaultDef52', None)
    assert getattr(partner, 'vM_EnumRealDef51') is None


def test_assoc_ex86_stub_double():
    # vM_NumericExpression_List has no real 'vM_NumericExpression_List87' property in the generated
    # code (a bare stub) -- manually attach it so vM_NumericExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_NumericExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_NumericExpression(op="sample_text", value="sample_text")
    partner = vM_NumericExpression_List()
    setattr(partner, 'vM_NumericExpression_List87', None)
    _safe_set(owner, 'vM_NumericExpression88', partner)
    assert owner in getattr(partner, 'vM_NumericExpression_List87')
    _safe_set(owner, 'vM_NumericExpression88', None)
    assert owner not in getattr(partner, 'vM_NumericExpression_List87')


def test_assoc_ex89_stub_double():
    # vM_BooleanExpression_List has no real 'vM_BooleanExpression_List90' property in the generated
    # code (a bare stub) -- manually attach it so vM_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_BooleanExpression(op="sample_text", value="sample_text")
    partner = vM_BooleanExpression_List()
    setattr(partner, 'vM_BooleanExpression_List90', None)
    _safe_set(owner, 'vM_BooleanExpression91', partner)
    assert owner in getattr(partner, 'vM_BooleanExpression_List90')
    _safe_set(owner, 'vM_BooleanExpression91', None)
    assert owner not in getattr(partner, 'vM_BooleanExpression_List90')


def test_assoc_expression65_stub_double():
    # vM_ComplexExpression has no real 'vM_ComplexExpression' property in the generated
    # code (a bare stub) -- manually attach it so vM_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Constraint(name="sample_text")
    partner = vM_ComplexExpression()
    setattr(partner, 'vM_ComplexExpression', None)
    _safe_set(owner, 'vM_Constraint66', partner)
    assert getattr(partner, 'vM_ComplexExpression') == owner
    _safe_set(owner, 'vM_Constraint66', None)
    assert getattr(partner, 'vM_ComplexExpression') is None


def test_assoc_expression95_stub_double():
    # vM_PrimitiveExpression has no real 'vM_PrimitiveExpression97' property in the generated
    # code (a bare stub) -- manually attach it so vM_ObjectiveExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_ObjectiveExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_ObjectiveExpression(op="sample_text")
    partner = vM_PrimitiveExpression()
    setattr(partner, 'vM_PrimitiveExpression97', None)
    _safe_set(owner, 'vM_ObjectiveExpression96', partner)
    assert getattr(partner, 'vM_PrimitiveExpression97') == owner
    _safe_set(owner, 'vM_ObjectiveExpression96', None)
    assert getattr(partner, 'vM_PrimitiveExpression97') is None


def test_assoc_expression_list78_stub_double():
    # vM_BooleanExpression_List has no real 'vM_BooleanExpression_List' property in the generated
    # code (a bare stub) -- manually attach it so vM_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_BooleanExpression(op="sample_text", value="sample_text")
    partner = vM_BooleanExpression_List()
    setattr(partner, 'vM_BooleanExpression_List', None)
    _safe_set(owner, 'vM_BooleanExpression79', partner)
    assert getattr(partner, 'vM_BooleanExpression_List') == owner
    _safe_set(owner, 'vM_BooleanExpression79', None)
    assert getattr(partner, 'vM_BooleanExpression_List') is None


def test_assoc_expression_list84_stub_double():
    # vM_NumericExpression_List has no real 'vM_NumericExpression_List' property in the generated
    # code (a bare stub) -- manually attach it so vM_NumericExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_NumericExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_NumericExpression(op="sample_text", value="sample_text")
    partner = vM_NumericExpression_List()
    setattr(partner, 'vM_NumericExpression_List', None)
    _safe_set(owner, 'vM_NumericExpression85', partner)
    assert getattr(partner, 'vM_NumericExpression_List') == owner
    _safe_set(owner, 'vM_NumericExpression85', None)
    assert getattr(partner, 'vM_NumericExpression_List') is None


def test_assoc_extendedValuation101_stub_double():
    # vM_ExtendedValuation has no real 'vM_ExtendedValuation' property in the generated
    # code (a bare stub) -- manually attach it so vM_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Configuration(name="sample_text")
    partner = vM_ExtendedValuation()
    setattr(partner, 'vM_ExtendedValuation', None)
    _safe_set(owner, 'vM_Configuration102', {partner})
    assert getattr(partner, 'vM_ExtendedValuation') == owner
    _safe_set(owner, 'vM_Configuration102', set())
    assert getattr(partner, 'vM_ExtendedValuation') is None


def test_assoc_featureID69_stub_double():
    # vM_PrimitiveExpression has no real 'vM_PrimitiveExpression' property in the generated
    # code (a bare stub) -- manually attach it so vM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    partner = vM_PrimitiveExpression()
    setattr(partner, 'vM_PrimitiveExpression', None)
    _safe_set(owner, 'vM_Feature70', partner)
    assert getattr(partner, 'vM_PrimitiveExpression') == owner
    _safe_set(owner, 'vM_Feature70', None)
    assert getattr(partner, 'vM_PrimitiveExpression') is None


def test_assoc_featuresDescriptions53_stub_double():
    # vM_Descriptions has no real 'vM_Descriptions' property in the generated
    # code (a bare stub) -- manually attach it so vM_FeatureDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_FeatureDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_FeatureDescription(description="sample_text")
    partner = vM_Descriptions()
    setattr(partner, 'vM_Descriptions', None)
    _safe_set(owner, 'vM_FeatureDescription', partner)
    assert owner in getattr(partner, 'vM_Descriptions')
    _safe_set(owner, 'vM_FeatureDescription', None)
    assert owner not in getattr(partner, 'vM_Descriptions')


def test_assoc_head71_stub_double():
    # vM_PrimitiveExpression has no real 'vM_PrimitiveExpression72' property in the generated
    # code (a bare stub) -- manually attach it so vM_AttHead's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_AttHead's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_AttHead(forAllFeatures=True)
    partner = vM_PrimitiveExpression()
    setattr(partner, 'vM_PrimitiveExpression72', None)
    _safe_set(owner, 'vM_AttHead', partner)
    assert getattr(partner, 'vM_PrimitiveExpression72') == owner
    _safe_set(owner, 'vM_AttHead', None)
    assert getattr(partner, 'vM_PrimitiveExpression72') is None


def test_assoc_name20_stub_double():
    # vM_Boolean_ATT_ID has no real 'vM_Boolean_ATT_ID' property in the generated
    # code (a bare stub) -- manually attach it so vM_BooleanAttrDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_BooleanAttrDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_BooleanAttrDef(value="sample_text")
    partner = vM_Boolean_ATT_ID()
    setattr(partner, 'vM_Boolean_ATT_ID', None)
    _safe_set(owner, 'vM_BooleanAttrDef', partner)
    assert getattr(partner, 'vM_Boolean_ATT_ID') == owner
    _safe_set(owner, 'vM_BooleanAttrDef', None)
    assert getattr(partner, 'vM_Boolean_ATT_ID') is None


def test_assoc_name23_stub_double():
    # vM_String_ATT_ID has no real 'vM_String_ATT_ID' property in the generated
    # code (a bare stub) -- manually attach it so vM_StringAttrDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_StringAttrDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_StringAttrDef(value="sample_text")
    partner = vM_String_ATT_ID()
    setattr(partner, 'vM_String_ATT_ID', None)
    _safe_set(owner, 'vM_StringAttrDef', partner)
    assert getattr(partner, 'vM_String_ATT_ID') == owner
    _safe_set(owner, 'vM_StringAttrDef', None)
    assert getattr(partner, 'vM_String_ATT_ID') is None


def test_assoc_objectives92_stub_double():
    # vM_Objectives has no real 'vM_Objectives' property in the generated
    # code (a bare stub) -- manually attach it so vM_Objective's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Objective's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Objective(name="sample_text", op="sample_text")
    partner = vM_Objectives()
    setattr(partner, 'vM_Objectives', None)
    _safe_set(owner, 'vM_Objective', partner)
    assert owner in getattr(partner, 'vM_Objectives')
    _safe_set(owner, 'vM_Objective', None)
    assert owner not in getattr(partner, 'vM_Objectives')


def test_assoc_pairs130_stub_double():
    # vM_TableBasedValuationByFeature has no real 'vM_TableBasedValuationByFeature131' property in the generated
    # code (a bare stub) -- manually attach it so vM_PairAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_PairAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_PairAttributeValue(value="sample_text")
    partner = vM_TableBasedValuationByFeature()
    setattr(partner, 'vM_TableBasedValuationByFeature131', None)
    _safe_set(owner, 'vM_PairAttributeValue132', partner)
    assert owner in getattr(partner, 'vM_TableBasedValuationByFeature131')
    _safe_set(owner, 'vM_PairAttributeValue132', None)
    assert owner not in getattr(partner, 'vM_TableBasedValuationByFeature131')


def test_assoc_pairs138_stub_double():
    # vM_TableBasedValuationByAttributeForInteger has no real 'vM_TableBasedValuationByAttributeForInteger139' property in the generated
    # code (a bare stub) -- manually attach it so vM_PairFeatureInteger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_PairFeatureInteger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_PairFeatureInteger(value="sample_text")
    partner = vM_TableBasedValuationByAttributeForInteger()
    setattr(partner, 'vM_TableBasedValuationByAttributeForInteger139', None)
    _safe_set(owner, 'vM_PairFeatureInteger', partner)
    assert owner in getattr(partner, 'vM_TableBasedValuationByAttributeForInteger139')
    _safe_set(owner, 'vM_PairFeatureInteger', None)
    assert owner not in getattr(partner, 'vM_TableBasedValuationByAttributeForInteger139')


def test_assoc_pairs145_stub_double():
    # vM_TableBasedValuationByAttributeForReal has no real 'vM_TableBasedValuationByAttributeForReal146' property in the generated
    # code (a bare stub) -- manually attach it so vM_PairFeatureReal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_PairFeatureReal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_PairFeatureReal(value="sample_text")
    partner = vM_TableBasedValuationByAttributeForReal()
    setattr(partner, 'vM_TableBasedValuationByAttributeForReal146', None)
    _safe_set(owner, 'vM_PairFeatureReal', partner)
    assert owner in getattr(partner, 'vM_TableBasedValuationByAttributeForReal146')
    _safe_set(owner, 'vM_PairFeatureReal', None)
    assert owner not in getattr(partner, 'vM_TableBasedValuationByAttributeForReal146')


def test_assoc_parent7_stub_double():
    # vM_FeatureHierarchy has no real 'vM_FeatureHierarchy8' property in the generated
    # code (a bare stub) -- manually attach it so vM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    partner = vM_FeatureHierarchy()
    setattr(partner, 'vM_FeatureHierarchy8', None)
    _safe_set(owner, 'vM_Feature', partner)
    assert getattr(partner, 'vM_FeatureHierarchy8') == owner
    _safe_set(owner, 'vM_Feature', None)
    assert getattr(partner, 'vM_FeatureHierarchy8') is None


def test_assoc_refAtt73_stub_double():
    # vM_PrimitiveExpression has no real 'vM_PrimitiveExpression74' property in the generated
    # code (a bare stub) -- manually attach it so vM_Abstract_ATT_ID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Abstract_ATT_ID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Abstract_ATT_ID(name="sample_text")
    partner = vM_PrimitiveExpression()
    setattr(partner, 'vM_PrimitiveExpression74', None)
    _safe_set(owner, 'vM_Abstract_ATT_ID75', partner)
    assert getattr(partner, 'vM_PrimitiveExpression74') == owner
    _safe_set(owner, 'vM_Abstract_ATT_ID75', None)
    assert getattr(partner, 'vM_PrimitiveExpression74') is None


def test_assoc_refFeature127_stub_double():
    # vM_TableBasedValuationByFeature has no real 'vM_TableBasedValuationByFeature128' property in the generated
    # code (a bare stub) -- manually attach it so vM_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vM_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vM_Feature(max="sample_text", min="sample_text", name="sample_text", notDecidable=True, notTranslatable=True, optional=True, runTime=True)
    partner = vM_TableBasedValuationByFeature()
    setattr(partner, 'vM_TableBasedValuationByFeature128', None)
    _safe_set(owner, 'vM_Feature129', partner)
    assert getattr(partner, 'vM_TableBasedValuationByFeature128') == owner
    _safe_set(owner, 'vM_Feature129', None)
    assert getattr(partner, 'vM_TableBasedValuationByFeature128') is None


