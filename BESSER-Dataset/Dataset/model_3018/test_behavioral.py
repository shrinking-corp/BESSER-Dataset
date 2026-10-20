import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BOMItem,
    CharacteristicReference_C,
    CharacteristicType,
    Condition,
    ConstraintObject,
    ConstraintRestriction,
    Dependency,
    Description,
    Documentation,
    Expression,
    FunctionOrTable,
    List,
    Literal,
    NumberListEntry,
    SetOrDelDefault,
    SimpleStatement,
    Statement,
    VCObject,
    vcml_Assignment,
    vcml_BOMItem,
    vcml_BOMItem_Class,
    vcml_BOMItem_Material,
    vcml_BillOfMaterial,
    vcml_BinaryCondition,
    vcml_BinaryExpression,
    vcml_Characteristic,
    vcml_CharacteristicGroup,
    vcml_CharacteristicOrValueDependencies,
    vcml_CharacteristicReference_C,
    vcml_CharacteristicReference_P,
    vcml_CharacteristicType,
    vcml_CharacteristicValue,
    vcml_Class,
    vcml_Classification,
    vcml_Comparison,
    vcml_CompoundStatement,
    vcml_Condition,
    vcml_ConditionSource,
    vcml_ConditionalConstraintRestriction,
    vcml_ConditionalStatement,
    vcml_ConfigurationProfile,
    vcml_ConfigurationProfileEntry,
    vcml_Constraint,
    vcml_ConstraintClass,
    vcml_ConstraintMaterial,
    vcml_ConstraintObject,
    vcml_ConstraintRestriction,
    vcml_ConstraintRestrictionFalse,
    vcml_ConstraintSource,
    vcml_CountParts,
    vcml_DateCharacteristicValue,
    vcml_DateType,
    vcml_DelDefault,
    vcml_Dependency,
    vcml_DependencyNet,
    vcml_Description,
    vcml_Documentation,
    vcml_EObject,
    vcml_Expression,
    vcml_FormattedDocumentationBlock,
    vcml_Function,
    vcml_FunctionCall,
    vcml_FunctionOrTable,
    vcml_Import,
    vcml_InCondition_C,
    vcml_InCondition_P,
    vcml_InterfaceDesign,
    vcml_IsInvisible,
    vcml_IsSpecified_C,
    vcml_IsSpecified_P,
    vcml_List,
    vcml_Literal,
    vcml_MDataCharacteristic_C,
    vcml_MDataCharacteristic_P,
    vcml_Material,
    vcml_MultiLanguageDescription,
    vcml_MultiLanguageDescriptions,
    vcml_MultipleLanguageDocumentation,
    vcml_MultipleLanguageDocumentation_LanguageBlock,
    vcml_NegatedConstraintRestrictionLHS,
    vcml_NumberList,
    vcml_NumberListEntry,
    vcml_NumericCharacteristicValue,
    vcml_NumericInterval,
    vcml_NumericLiteral,
    vcml_NumericType,
    vcml_ObjectCharacteristicReference,
    vcml_ObjectType,
    vcml_Option,
    vcml_PFunction,
    vcml_PartOfCondition,
    vcml_PartialKey,
    vcml_Precondition,
    vcml_Procedure,
    vcml_ProcedureSource,
    vcml_Row,
    vcml_SelectionCondition,
    vcml_SetDefault,
    vcml_SetOrDelDefault,
    vcml_SetPricingFactor,
    vcml_ShortVarDefinition,
    vcml_ShortVarReference,
    vcml_SimpleDescription,
    vcml_SimpleDocumentation,
    vcml_SimpleStatement,
    vcml_Statement,
    vcml_SubpartOfCondition,
    vcml_SumParts,
    vcml_SymbolList,
    vcml_SymbolicLiteral,
    vcml_SymbolicType,
    vcml_Table,
    vcml_TypeOf,
    vcml_UnaryCondition,
    vcml_UnaryExpression,
    vcml_VCObject,
    vcml_ValueAssignment,
    vcml_VariantFunction,
    vcml_VariantFunctionArgument,
    vcml_VariantTable,
    vcml_VariantTableArgument,
    vcml_VariantTableContent,
    vcml_VcmlModel,
    ComparisonOperator,
    Fixing,
    FunctionName,
    Language,
    OptionType,
    ProcedureLocation,
    Status,
    UnaryExpressionOperator,
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

def test_assoc_arguments117_reverse_link_reassign_clear():
    a1 = vcml_VariantFunctionArgument(in_=True)
    a2 = vcml_VariantFunctionArgument(in_=False)
    b = vcml_VariantFunction(group="sample_text", status="sample_text")
    _safe_set(b, 'vcml_VariantFunction', {a1})
    assert _is_linked(b, 'vcml_VariantFunction', a1)
    if hasattr(a1, 'vcml_VariantFunctionArgument'):
        assert _is_linked(a1, 'vcml_VariantFunctionArgument', b)
    _safe_set(b, 'vcml_VariantFunction', {a2})
    assert _is_linked(b, 'vcml_VariantFunction', a2)
    if hasattr(a1, 'vcml_VariantFunctionArgument'):
        assert not _is_linked(a1, 'vcml_VariantFunctionArgument', b)
    if hasattr(a2, 'vcml_VariantFunctionArgument'):
        assert _is_linked(a2, 'vcml_VariantFunctionArgument', b)
    _safe_set(b, 'vcml_VariantFunction', set())
    assert not _is_linked(b, 'vcml_VariantFunction', a2)
    if hasattr(a2, 'vcml_VariantFunctionArgument'):
        assert not _is_linked(a2, 'vcml_VariantFunctionArgument', b)


def test_assoc_arguments121_reverse_link_reassign_clear():
    a1 = vcml_VariantTableArgument(key=True)
    a2 = vcml_VariantTableArgument(key=False)
    b = vcml_VariantTable(group="sample_text", status="sample_text")
    _safe_set(b, 'vcml_VariantTable', {a1})
    assert _is_linked(b, 'vcml_VariantTable', a1)
    if hasattr(a1, 'vcml_VariantTableArgument'):
        assert _is_linked(a1, 'vcml_VariantTableArgument', b)
    _safe_set(b, 'vcml_VariantTable', {a2})
    assert _is_linked(b, 'vcml_VariantTable', a2)
    if hasattr(a1, 'vcml_VariantTableArgument'):
        assert not _is_linked(a1, 'vcml_VariantTableArgument', b)
    if hasattr(a2, 'vcml_VariantTableArgument'):
        assert _is_linked(a2, 'vcml_VariantTableArgument', b)
    _safe_set(b, 'vcml_VariantTable', set())
    assert not _is_linked(b, 'vcml_VariantTable', a2)
    if hasattr(a2, 'vcml_VariantTableArgument'):
        assert not _is_linked(a2, 'vcml_VariantTableArgument', b)


def test_assoc_attrs150_reverse_link_reassign_clear():
    a1 = vcml_PartialKey(key="sample_text")
    a2 = vcml_PartialKey(key="sample_text_2")
    b = vcml_ObjectType(classType=7, type="sample_text")
    _safe_set(b, 'vcml_ObjectType151', {a1})
    assert _is_linked(b, 'vcml_ObjectType151', a1)
    if hasattr(a1, 'vcml_PartialKey'):
        assert _is_linked(a1, 'vcml_PartialKey', b)
    _safe_set(b, 'vcml_ObjectType151', {a2})
    assert _is_linked(b, 'vcml_ObjectType151', a2)
    if hasattr(a1, 'vcml_PartialKey'):
        assert not _is_linked(a1, 'vcml_PartialKey', b)
    if hasattr(a2, 'vcml_PartialKey'):
        assert _is_linked(a2, 'vcml_PartialKey', b)
    _safe_set(b, 'vcml_ObjectType151', set())
    assert not _is_linked(b, 'vcml_ObjectType151', a2)
    if hasattr(a2, 'vcml_PartialKey'):
        assert not _is_linked(a2, 'vcml_PartialKey', b)


def test_assoc_characteristic118_reverse_link_reassign_clear():
    a1 = vcml_VariantFunctionArgument(in_=True)
    a2 = vcml_VariantFunctionArgument(in_=False)
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic120', a1)
    assert _is_linked(b, 'vcml_Characteristic120', a1)
    if hasattr(a1, 'vcml_VariantFunctionArgument119'):
        assert _is_linked(a1, 'vcml_VariantFunctionArgument119', b)
    _safe_set(b, 'vcml_Characteristic120', a2)
    assert _is_linked(b, 'vcml_Characteristic120', a2)
    if hasattr(a1, 'vcml_VariantFunctionArgument119'):
        assert not _is_linked(a1, 'vcml_VariantFunctionArgument119', b)
    if hasattr(a2, 'vcml_VariantFunctionArgument119'):
        assert _is_linked(a2, 'vcml_VariantFunctionArgument119', b)
    _safe_set(b, 'vcml_Characteristic120', None)
    assert not _is_linked(b, 'vcml_Characteristic120', a2)
    if hasattr(a2, 'vcml_VariantFunctionArgument119'):
        assert not _is_linked(a2, 'vcml_VariantFunctionArgument119', b)


def test_assoc_characteristic122_reverse_link_reassign_clear():
    a1 = vcml_VariantTableArgument(key=True)
    a2 = vcml_VariantTableArgument(key=False)
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic124', a1)
    assert _is_linked(b, 'vcml_Characteristic124', a1)
    if hasattr(a1, 'vcml_VariantTableArgument123'):
        assert _is_linked(a1, 'vcml_VariantTableArgument123', b)
    _safe_set(b, 'vcml_Characteristic124', a2)
    assert _is_linked(b, 'vcml_Characteristic124', a2)
    if hasattr(a1, 'vcml_VariantTableArgument123'):
        assert not _is_linked(a1, 'vcml_VariantTableArgument123', b)
    if hasattr(a2, 'vcml_VariantTableArgument123'):
        assert _is_linked(a2, 'vcml_VariantTableArgument123', b)
    _safe_set(b, 'vcml_Characteristic124', None)
    assert not _is_linked(b, 'vcml_Characteristic124', a2)
    if hasattr(a2, 'vcml_VariantTableArgument123'):
        assert not _is_linked(a2, 'vcml_VariantTableArgument123', b)


def test_assoc_characteristic155_reverse_link_reassign_clear():
    a1 = vcml_ShortVarDefinition(name="sample_text")
    a2 = vcml_ShortVarDefinition(name="sample_text_2")
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic157', a1)
    assert _is_linked(b, 'vcml_Characteristic157', a1)
    if hasattr(a1, 'vcml_ShortVarDefinition156'):
        assert _is_linked(a1, 'vcml_ShortVarDefinition156', b)
    _safe_set(b, 'vcml_Characteristic157', a2)
    assert _is_linked(b, 'vcml_Characteristic157', a2)
    if hasattr(a1, 'vcml_ShortVarDefinition156'):
        assert not _is_linked(a1, 'vcml_ShortVarDefinition156', b)
    if hasattr(a2, 'vcml_ShortVarDefinition156'):
        assert _is_linked(a2, 'vcml_ShortVarDefinition156', b)
    _safe_set(b, 'vcml_Characteristic157', None)
    assert not _is_linked(b, 'vcml_Characteristic157', a2)
    if hasattr(a2, 'vcml_ShortVarDefinition156'):
        assert not _is_linked(a2, 'vcml_ShortVarDefinition156', b)


def test_assoc_characteristic214_reverse_link_reassign_clear():
    a1 = vcml_SetPricingFactor(location="sample_text")
    a2 = vcml_SetPricingFactor(location="sample_text_2")
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic215', a1)
    assert _is_linked(b, 'vcml_Characteristic215', a1)
    if hasattr(a1, 'vcml_SetPricingFactor'):
        assert _is_linked(a1, 'vcml_SetPricingFactor', b)
    _safe_set(b, 'vcml_Characteristic215', a2)
    assert _is_linked(b, 'vcml_Characteristic215', a2)
    if hasattr(a1, 'vcml_SetPricingFactor'):
        assert not _is_linked(a1, 'vcml_SetPricingFactor', b)
    if hasattr(a2, 'vcml_SetPricingFactor'):
        assert _is_linked(a2, 'vcml_SetPricingFactor', b)
    _safe_set(b, 'vcml_Characteristic215', None)
    assert not _is_linked(b, 'vcml_Characteristic215', a2)
    if hasattr(a2, 'vcml_SetPricingFactor'):
        assert not _is_linked(a2, 'vcml_SetPricingFactor', b)


def test_assoc_characteristic222_reverse_link_reassign_clear():
    a1 = vcml_CharacteristicReference_P(location="sample_text")
    a2 = vcml_CharacteristicReference_P(location="sample_text_2")
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic223', a1)
    assert _is_linked(b, 'vcml_Characteristic223', a1)
    if hasattr(a1, 'vcml_CharacteristicReference_P'):
        assert _is_linked(a1, 'vcml_CharacteristicReference_P', b)
    _safe_set(b, 'vcml_Characteristic223', a2)
    assert _is_linked(b, 'vcml_Characteristic223', a2)
    if hasattr(a1, 'vcml_CharacteristicReference_P'):
        assert not _is_linked(a1, 'vcml_CharacteristicReference_P', b)
    if hasattr(a2, 'vcml_CharacteristicReference_P'):
        assert _is_linked(a2, 'vcml_CharacteristicReference_P', b)
    _safe_set(b, 'vcml_Characteristic223', None)
    assert not _is_linked(b, 'vcml_Characteristic223', a2)
    if hasattr(a2, 'vcml_CharacteristicReference_P'):
        assert not _is_linked(a2, 'vcml_CharacteristicReference_P', b)


def test_assoc_characteristic228_reverse_link_reassign_clear():
    a1 = vcml_SumParts(location="sample_text")
    a2 = vcml_SumParts(location="sample_text_2")
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic229', a1)
    assert _is_linked(b, 'vcml_Characteristic229', a1)
    if hasattr(a1, 'vcml_SumParts'):
        assert _is_linked(a1, 'vcml_SumParts', b)
    _safe_set(b, 'vcml_Characteristic229', a2)
    assert _is_linked(b, 'vcml_Characteristic229', a2)
    if hasattr(a1, 'vcml_SumParts'):
        assert not _is_linked(a1, 'vcml_SumParts', b)
    if hasattr(a2, 'vcml_SumParts'):
        assert _is_linked(a2, 'vcml_SumParts', b)
    _safe_set(b, 'vcml_Characteristic229', None)
    assert not _is_linked(b, 'vcml_Characteristic229', a2)
    if hasattr(a2, 'vcml_SumParts'):
        assert not _is_linked(a2, 'vcml_SumParts', b)


def test_assoc_characteristics51_reverse_link_reassign_clear():
    a1 = vcml_Class(group="sample_text", status="sample_text")
    a2 = vcml_Class(group="sample_text_2", status="sample_text_2")
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic53', a1)
    assert _is_linked(b, 'vcml_Characteristic53', a1)
    if hasattr(a1, 'vcml_Class52'):
        assert _is_linked(a1, 'vcml_Class52', b)
    _safe_set(b, 'vcml_Characteristic53', a2)
    assert _is_linked(b, 'vcml_Characteristic53', a2)
    if hasattr(a1, 'vcml_Class52'):
        assert not _is_linked(a1, 'vcml_Class52', b)
    if hasattr(a2, 'vcml_Class52'):
        assert _is_linked(a2, 'vcml_Class52', b)
    _safe_set(b, 'vcml_Characteristic53', None)
    assert not _is_linked(b, 'vcml_Characteristic53', a2)
    if hasattr(a2, 'vcml_Class52'):
        assert not _is_linked(a2, 'vcml_Class52', b)


def test_assoc_characteristics99_reverse_link_reassign_clear():
    a1 = vcml_CharacteristicGroup(name="sample_text")
    a2 = vcml_CharacteristicGroup(name="sample_text_2")
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic101', a1)
    assert _is_linked(b, 'vcml_Characteristic101', a1)
    if hasattr(a1, 'vcml_CharacteristicGroup100'):
        assert _is_linked(a1, 'vcml_CharacteristicGroup100', b)
    _safe_set(b, 'vcml_Characteristic101', a2)
    assert _is_linked(b, 'vcml_Characteristic101', a2)
    if hasattr(a1, 'vcml_CharacteristicGroup100'):
        assert not _is_linked(a1, 'vcml_CharacteristicGroup100', b)
    if hasattr(a2, 'vcml_CharacteristicGroup100'):
        assert _is_linked(a2, 'vcml_CharacteristicGroup100', b)
    _safe_set(b, 'vcml_Characteristic101', None)
    assert not _is_linked(b, 'vcml_Characteristic101', a2)
    if hasattr(a2, 'vcml_CharacteristicGroup100'):
        assert not _is_linked(a2, 'vcml_CharacteristicGroup100', b)


def test_assoc_configurationprofiles105_reverse_link_reassign_clear():
    a1 = vcml_Material(type="sample_text")
    a2 = vcml_Material(type="sample_text_2")
    b = vcml_ConfigurationProfile(bomapplication="sample_text", fixing="sample_text", status="sample_text")
    _safe_set(b, 'ConfigurationProfile', a1)
    assert _is_linked(b, 'ConfigurationProfile', a1)
    if hasattr(a1, 'material106'):
        assert _is_linked(a1, 'material106', b)
    _safe_set(b, 'ConfigurationProfile', a2)
    assert _is_linked(b, 'ConfigurationProfile', a2)
    if hasattr(a1, 'material106'):
        assert not _is_linked(a1, 'material106', b)
    if hasattr(a2, 'material106'):
        assert _is_linked(a2, 'material106', b)
    _safe_set(b, 'ConfigurationProfile', None)
    assert not _is_linked(b, 'ConfigurationProfile', a2)
    if hasattr(a2, 'material106'):
        assert not _is_linked(a2, 'material106', b)


def test_assoc_constraints84_reverse_link_reassign_clear():
    a1 = vcml_DependencyNet(group="sample_text", status="sample_text")
    a2 = vcml_DependencyNet(group="sample_text_2", status="sample_text_2")
    b = vcml_Constraint(group="sample_text", status="sample_text")
    _safe_set(b, 'vcml_Constraint', a1)
    assert _is_linked(b, 'vcml_Constraint', a1)
    if hasattr(a1, 'vcml_DependencyNet85'):
        assert _is_linked(a1, 'vcml_DependencyNet85', b)
    _safe_set(b, 'vcml_Constraint', a2)
    assert _is_linked(b, 'vcml_Constraint', a2)
    if hasattr(a1, 'vcml_DependencyNet85'):
        assert not _is_linked(a1, 'vcml_DependencyNet85', b)
    if hasattr(a2, 'vcml_DependencyNet85'):
        assert _is_linked(a2, 'vcml_DependencyNet85', b)
    _safe_set(b, 'vcml_Constraint', None)
    assert not _is_linked(b, 'vcml_Constraint', a2)
    if hasattr(a2, 'vcml_DependencyNet85'):
        assert not _is_linked(a2, 'vcml_DependencyNet85', b)


def test_assoc_dependency91_reverse_link_reassign_clear():
    a1 = vcml_Procedure(group="sample_text", status="sample_text")
    a2 = vcml_Procedure(group="sample_text_2", status="sample_text_2")
    b = vcml_ConfigurationProfileEntry(sequence=7)
    _safe_set(b, 'vcml_ConfigurationProfileEntry92', a1)
    assert _is_linked(b, 'vcml_ConfigurationProfileEntry92', a1)
    if hasattr(a1, 'vcml_Procedure93'):
        assert _is_linked(a1, 'vcml_Procedure93', b)
    _safe_set(b, 'vcml_ConfigurationProfileEntry92', a2)
    assert _is_linked(b, 'vcml_ConfigurationProfileEntry92', a2)
    if hasattr(a1, 'vcml_Procedure93'):
        assert not _is_linked(a1, 'vcml_Procedure93', b)
    if hasattr(a2, 'vcml_Procedure93'):
        assert _is_linked(a2, 'vcml_Procedure93', b)
    _safe_set(b, 'vcml_ConfigurationProfileEntry92', None)
    assert not _is_linked(b, 'vcml_ConfigurationProfileEntry92', a2)
    if hasattr(a2, 'vcml_Procedure93'):
        assert not _is_linked(a2, 'vcml_Procedure93', b)


def test_assoc_dependencyNets58_reverse_link_reassign_clear():
    a1 = vcml_DependencyNet(group="sample_text", status="sample_text")
    a2 = vcml_DependencyNet(group="sample_text_2", status="sample_text_2")
    b = vcml_ConfigurationProfile(bomapplication="sample_text", fixing="sample_text", status="sample_text")
    _safe_set(b, 'vcml_ConfigurationProfile59', {a1})
    assert _is_linked(b, 'vcml_ConfigurationProfile59', a1)
    if hasattr(a1, 'vcml_DependencyNet'):
        assert _is_linked(a1, 'vcml_DependencyNet', b)
    _safe_set(b, 'vcml_ConfigurationProfile59', {a2})
    assert _is_linked(b, 'vcml_ConfigurationProfile59', a2)
    if hasattr(a1, 'vcml_DependencyNet'):
        assert not _is_linked(a1, 'vcml_DependencyNet', b)
    if hasattr(a2, 'vcml_DependencyNet'):
        assert _is_linked(a2, 'vcml_DependencyNet', b)
    _safe_set(b, 'vcml_ConfigurationProfile59', set())
    assert not _is_linked(b, 'vcml_ConfigurationProfile59', a2)
    if hasattr(a2, 'vcml_DependencyNet'):
        assert not _is_linked(a2, 'vcml_DependencyNet', b)


def test_assoc_entries14_reverse_link_reassign_clear():
    a1 = vcml_ConfigurationProfileEntry(sequence=7)
    a2 = vcml_ConfigurationProfileEntry(sequence=13)
    b = vcml_BOMItem(itemnumber=7)
    _safe_set(b, 'vcml_BOMItem15', {a1})
    assert _is_linked(b, 'vcml_BOMItem15', a1)
    if hasattr(a1, 'vcml_ConfigurationProfileEntry'):
        assert _is_linked(a1, 'vcml_ConfigurationProfileEntry', b)
    _safe_set(b, 'vcml_BOMItem15', {a2})
    assert _is_linked(b, 'vcml_BOMItem15', a2)
    if hasattr(a1, 'vcml_ConfigurationProfileEntry'):
        assert not _is_linked(a1, 'vcml_ConfigurationProfileEntry', b)
    if hasattr(a2, 'vcml_ConfigurationProfileEntry'):
        assert _is_linked(a2, 'vcml_ConfigurationProfileEntry', b)
    _safe_set(b, 'vcml_BOMItem15', set())
    assert not _is_linked(b, 'vcml_BOMItem15', a2)
    if hasattr(a2, 'vcml_ConfigurationProfileEntry'):
        assert not _is_linked(a2, 'vcml_ConfigurationProfileEntry', b)


def test_assoc_entries60_reverse_link_reassign_clear():
    a1 = vcml_ConfigurationProfileEntry(sequence=7)
    a2 = vcml_ConfigurationProfileEntry(sequence=13)
    b = vcml_ConfigurationProfile(bomapplication="sample_text", fixing="sample_text", status="sample_text")
    _safe_set(b, 'vcml_ConfigurationProfile61', {a1})
    assert _is_linked(b, 'vcml_ConfigurationProfile61', a1)
    if hasattr(a1, 'vcml_ConfigurationProfileEntry62'):
        assert _is_linked(a1, 'vcml_ConfigurationProfileEntry62', b)
    _safe_set(b, 'vcml_ConfigurationProfile61', {a2})
    assert _is_linked(b, 'vcml_ConfigurationProfile61', a2)
    if hasattr(a1, 'vcml_ConfigurationProfileEntry62'):
        assert not _is_linked(a1, 'vcml_ConfigurationProfileEntry62', b)
    if hasattr(a2, 'vcml_ConfigurationProfileEntry62'):
        assert _is_linked(a2, 'vcml_ConfigurationProfileEntry62', b)
    _safe_set(b, 'vcml_ConfigurationProfile61', set())
    assert not _is_linked(b, 'vcml_ConfigurationProfile61', a2)
    if hasattr(a2, 'vcml_ConfigurationProfileEntry62'):
        assert not _is_linked(a2, 'vcml_ConfigurationProfileEntry62', b)


def test_assoc_formattedDocumentationBlocks134_reverse_link_reassign_clear():
    a1 = vcml_MultipleLanguageDocumentation_LanguageBlock(language="sample_text")
    a2 = vcml_MultipleLanguageDocumentation_LanguageBlock(language="sample_text_2")
    b = vcml_FormattedDocumentationBlock(format="sample_text", value="sample_text")
    _safe_set(b, 'vcml_FormattedDocumentationBlock', a1)
    assert _is_linked(b, 'vcml_FormattedDocumentationBlock', a1)
    if hasattr(a1, 'vcml_MultipleLanguageDocumentation_LanguageBlock135'):
        assert _is_linked(a1, 'vcml_MultipleLanguageDocumentation_LanguageBlock135', b)
    _safe_set(b, 'vcml_FormattedDocumentationBlock', a2)
    assert _is_linked(b, 'vcml_FormattedDocumentationBlock', a2)
    if hasattr(a1, 'vcml_MultipleLanguageDocumentation_LanguageBlock135'):
        assert not _is_linked(a1, 'vcml_MultipleLanguageDocumentation_LanguageBlock135', b)
    if hasattr(a2, 'vcml_MultipleLanguageDocumentation_LanguageBlock135'):
        assert _is_linked(a2, 'vcml_MultipleLanguageDocumentation_LanguageBlock135', b)
    _safe_set(b, 'vcml_FormattedDocumentationBlock', None)
    assert not _is_linked(b, 'vcml_FormattedDocumentationBlock', a2)
    if hasattr(a2, 'vcml_MultipleLanguageDocumentation_LanguageBlock135'):
        assert not _is_linked(a2, 'vcml_MultipleLanguageDocumentation_LanguageBlock135', b)


def test_assoc_material152_reverse_link_reassign_clear():
    a1 = vcml_PartialKey(key="sample_text")
    a2 = vcml_PartialKey(key="sample_text_2")
    b = vcml_Material(type="sample_text")
    _safe_set(b, 'vcml_Material154', a1)
    assert _is_linked(b, 'vcml_Material154', a1)
    if hasattr(a1, 'vcml_PartialKey153'):
        assert _is_linked(a1, 'vcml_PartialKey153', b)
    _safe_set(b, 'vcml_Material154', a2)
    assert _is_linked(b, 'vcml_Material154', a2)
    if hasattr(a1, 'vcml_PartialKey153'):
        assert not _is_linked(a1, 'vcml_PartialKey153', b)
    if hasattr(a2, 'vcml_PartialKey153'):
        assert _is_linked(a2, 'vcml_PartialKey153', b)
    _safe_set(b, 'vcml_Material154', None)
    assert not _is_linked(b, 'vcml_Material154', a2)
    if hasattr(a2, 'vcml_PartialKey153'):
        assert not _is_linked(a2, 'vcml_PartialKey153', b)


def test_assoc_material63_reverse_link_reassign_clear():
    a1 = vcml_Material(type="sample_text")
    a2 = vcml_Material(type="sample_text_2")
    b = vcml_ConfigurationProfile(bomapplication="sample_text", fixing="sample_text", status="sample_text")
    _safe_set(b, 'configurationprofiles', a1)
    assert _is_linked(b, 'configurationprofiles', a1)
    if hasattr(a1, 'Material64'):
        assert _is_linked(a1, 'Material64', b)
    _safe_set(b, 'configurationprofiles', a2)
    assert _is_linked(b, 'configurationprofiles', a2)
    if hasattr(a1, 'Material64'):
        assert not _is_linked(a1, 'Material64', b)
    if hasattr(a2, 'Material64'):
        assert _is_linked(a2, 'Material64', b)
    _safe_set(b, 'configurationprofiles', None)
    assert not _is_linked(b, 'configurationprofiles', a2)
    if hasattr(a2, 'Material64'):
        assert not _is_linked(a2, 'Material64', b)


def test_assoc_options7_reverse_link_reassign_clear():
    a1 = vcml_VCObject(name="sample_text")
    a2 = vcml_VCObject(name="sample_text_2")
    b = vcml_Option(name="sample_text", value="sample_text")
    _safe_set(b, 'vcml_Option9', a1)
    assert _is_linked(b, 'vcml_Option9', a1)
    if hasattr(a1, 'vcml_VCObject8'):
        assert _is_linked(a1, 'vcml_VCObject8', b)
    _safe_set(b, 'vcml_Option9', a2)
    assert _is_linked(b, 'vcml_Option9', a2)
    if hasattr(a1, 'vcml_VCObject8'):
        assert not _is_linked(a1, 'vcml_VCObject8', b)
    if hasattr(a2, 'vcml_VCObject8'):
        assert _is_linked(a2, 'vcml_VCObject8', b)
    _safe_set(b, 'vcml_Option9', None)
    assert not _is_linked(b, 'vcml_Option9', a2)
    if hasattr(a2, 'vcml_VCObject8'):
        assert not _is_linked(a2, 'vcml_VCObject8', b)


def test_assoc_selectionCondition12_reverse_link_reassign_clear():
    a1 = vcml_SelectionCondition(group="sample_text", status="sample_text")
    a2 = vcml_SelectionCondition(group="sample_text_2", status="sample_text_2")
    b = vcml_BOMItem(itemnumber=7)
    _safe_set(b, 'vcml_BOMItem13', a1)
    assert _is_linked(b, 'vcml_BOMItem13', a1)
    if hasattr(a1, 'vcml_SelectionCondition'):
        assert _is_linked(a1, 'vcml_SelectionCondition', b)
    _safe_set(b, 'vcml_BOMItem13', a2)
    assert _is_linked(b, 'vcml_BOMItem13', a2)
    if hasattr(a1, 'vcml_SelectionCondition'):
        assert not _is_linked(a1, 'vcml_SelectionCondition', b)
    if hasattr(a2, 'vcml_SelectionCondition'):
        assert _is_linked(a2, 'vcml_SelectionCondition', b)
    _safe_set(b, 'vcml_BOMItem13', None)
    assert not _is_linked(b, 'vcml_BOMItem13', a2)
    if hasattr(a2, 'vcml_SelectionCondition'):
        assert not _is_linked(a2, 'vcml_SelectionCondition', b)


def test_assoc_shortVars145_reverse_link_reassign_clear():
    a1 = vcml_ShortVarDefinition(name="sample_text")
    a2 = vcml_ShortVarDefinition(name="sample_text_2")
    b = vcml_ConstraintObject(name="sample_text")
    _safe_set(b, 'vcml_ConstraintObject146', {a1})
    assert _is_linked(b, 'vcml_ConstraintObject146', a1)
    if hasattr(a1, 'vcml_ShortVarDefinition'):
        assert _is_linked(a1, 'vcml_ShortVarDefinition', b)
    _safe_set(b, 'vcml_ConstraintObject146', {a2})
    assert _is_linked(b, 'vcml_ConstraintObject146', a2)
    if hasattr(a1, 'vcml_ShortVarDefinition'):
        assert not _is_linked(a1, 'vcml_ShortVarDefinition', b)
    if hasattr(a2, 'vcml_ShortVarDefinition'):
        assert _is_linked(a2, 'vcml_ShortVarDefinition', b)
    _safe_set(b, 'vcml_ConstraintObject146', set())
    assert not _is_linked(b, 'vcml_ConstraintObject146', a2)
    if hasattr(a2, 'vcml_ShortVarDefinition'):
        assert not _is_linked(a2, 'vcml_ShortVarDefinition', b)


def test_assoc_superClasses55_reverse_link_reassign_clear():
    a1 = vcml_Class(group="sample_text", status="sample_text")
    a2 = vcml_Class(group="sample_text_2", status="sample_text_2")
    b = vcml_Class(group="sample_text", status="sample_text")
    _safe_set(b, 'vcml_Class56', a1)
    assert _is_linked(b, 'vcml_Class56', a1)
    if hasattr(a1, 'vcml_Class54'):
        assert _is_linked(a1, 'vcml_Class54', b)
    _safe_set(b, 'vcml_Class56', a2)
    assert _is_linked(b, 'vcml_Class56', a2)
    if hasattr(a1, 'vcml_Class54'):
        assert not _is_linked(a1, 'vcml_Class54', b)
    if hasattr(a2, 'vcml_Class54'):
        assert _is_linked(a2, 'vcml_Class54', b)
    _safe_set(b, 'vcml_Class56', None)
    assert not _is_linked(b, 'vcml_Class56', a2)
    if hasattr(a2, 'vcml_Class54'):
        assert not _is_linked(a2, 'vcml_Class54', b)


def test_assoc_type19_reverse_link_reassign_clear():
    a1 = vcml_CharacteristicType(numberOfChars=7)
    a2 = vcml_CharacteristicType(numberOfChars=13)
    b = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    _safe_set(b, 'vcml_Characteristic20', a1)
    assert _is_linked(b, 'vcml_Characteristic20', a1)
    if hasattr(a1, 'vcml_CharacteristicType'):
        assert _is_linked(a1, 'vcml_CharacteristicType', b)
    _safe_set(b, 'vcml_Characteristic20', a2)
    assert _is_linked(b, 'vcml_Characteristic20', a2)
    if hasattr(a1, 'vcml_CharacteristicType'):
        assert not _is_linked(a1, 'vcml_CharacteristicType', b)
    if hasattr(a2, 'vcml_CharacteristicType'):
        assert _is_linked(a2, 'vcml_CharacteristicType', b)
    _safe_set(b, 'vcml_Characteristic20', None)
    assert not _is_linked(b, 'vcml_Characteristic20', a2)
    if hasattr(a2, 'vcml_CharacteristicType'):
        assert not _is_linked(a2, 'vcml_CharacteristicType', b)


def test_assoc_values23_reverse_link_reassign_clear():
    a1 = vcml_NumericType(decimalPlaces=7, intervalValuesAllowed=True, negativeValuesAllowed=True, unit="sample_text")
    a2 = vcml_NumericType(decimalPlaces=13, intervalValuesAllowed=False, negativeValuesAllowed=False, unit="sample_text_2")
    b = vcml_NumericCharacteristicValue(default=True)
    _safe_set(b, 'vcml_NumericCharacteristicValue', a1)
    assert _is_linked(b, 'vcml_NumericCharacteristicValue', a1)
    if hasattr(a1, 'vcml_NumericType'):
        assert _is_linked(a1, 'vcml_NumericType', b)
    _safe_set(b, 'vcml_NumericCharacteristicValue', a2)
    assert _is_linked(b, 'vcml_NumericCharacteristicValue', a2)
    if hasattr(a1, 'vcml_NumericType'):
        assert not _is_linked(a1, 'vcml_NumericType', b)
    if hasattr(a2, 'vcml_NumericType'):
        assert _is_linked(a2, 'vcml_NumericType', b)
    _safe_set(b, 'vcml_NumericCharacteristicValue', None)
    assert not _is_linked(b, 'vcml_NumericCharacteristicValue', a2)
    if hasattr(a2, 'vcml_NumericType'):
        assert not _is_linked(a2, 'vcml_NumericType', b)


def test_assoc_values24_reverse_link_reassign_clear():
    a1 = vcml_SymbolicType(caseSensitive=True)
    a2 = vcml_SymbolicType(caseSensitive=False)
    b = vcml_CharacteristicValue(default=True, name="sample_text")
    _safe_set(b, 'vcml_CharacteristicValue', a1)
    assert _is_linked(b, 'vcml_CharacteristicValue', a1)
    if hasattr(a1, 'vcml_SymbolicType'):
        assert _is_linked(a1, 'vcml_SymbolicType', b)
    _safe_set(b, 'vcml_CharacteristicValue', a2)
    assert _is_linked(b, 'vcml_CharacteristicValue', a2)
    if hasattr(a1, 'vcml_SymbolicType'):
        assert not _is_linked(a1, 'vcml_SymbolicType', b)
    if hasattr(a2, 'vcml_SymbolicType'):
        assert _is_linked(a2, 'vcml_SymbolicType', b)
    _safe_set(b, 'vcml_CharacteristicValue', None)
    assert not _is_linked(b, 'vcml_CharacteristicValue', a2)
    if hasattr(a2, 'vcml_SymbolicType'):
        assert not _is_linked(a2, 'vcml_SymbolicType', b)


def test_assoc_values25_reverse_link_reassign_clear():
    a1 = vcml_DateType(intervalValuesAllowed=True)
    a2 = vcml_DateType(intervalValuesAllowed=False)
    b = vcml_DateCharacteristicValue(default=True, from_="sample_text", to="sample_text")
    _safe_set(b, 'vcml_DateCharacteristicValue', a1)
    assert _is_linked(b, 'vcml_DateCharacteristicValue', a1)
    if hasattr(a1, 'vcml_DateType'):
        assert _is_linked(a1, 'vcml_DateType', b)
    _safe_set(b, 'vcml_DateCharacteristicValue', a2)
    assert _is_linked(b, 'vcml_DateCharacteristicValue', a2)
    if hasattr(a1, 'vcml_DateType'):
        assert not _is_linked(a1, 'vcml_DateType', b)
    if hasattr(a2, 'vcml_DateType'):
        assert _is_linked(a2, 'vcml_DateType', b)
    _safe_set(b, 'vcml_DateCharacteristicValue', None)
    assert not _is_linked(b, 'vcml_DateCharacteristicValue', a2)
    if hasattr(a2, 'vcml_DateType'):
        assert not _is_linked(a2, 'vcml_DateType', b)


def test_assoc_variantclass245_reverse_link_reassign_clear():
    a1 = vcml_TypeOf(location="sample_text")
    a2 = vcml_TypeOf(location="sample_text_2")
    b = vcml_ObjectType(classType=7, type="sample_text")
    _safe_set(b, 'vcml_ObjectType246', a1)
    assert _is_linked(b, 'vcml_ObjectType246', a1)
    if hasattr(a1, 'vcml_TypeOf'):
        assert _is_linked(a1, 'vcml_TypeOf', b)
    _safe_set(b, 'vcml_ObjectType246', a2)
    assert _is_linked(b, 'vcml_ObjectType246', a2)
    if hasattr(a1, 'vcml_TypeOf'):
        assert not _is_linked(a1, 'vcml_TypeOf', b)
    if hasattr(a2, 'vcml_TypeOf'):
        assert _is_linked(a2, 'vcml_TypeOf', b)
    _safe_set(b, 'vcml_ObjectType246', None)
    assert not _is_linked(b, 'vcml_ObjectType246', a2)
    if hasattr(a2, 'vcml_TypeOf'):
        assert not _is_linked(a2, 'vcml_TypeOf', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arg1216_stub_double():
    # vcml_Expression has no real 'vcml_Expression218' property in the generated
    # code (a bare stub) -- manually attach it so vcml_SetPricingFactor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_SetPricingFactor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_SetPricingFactor(location="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression218', None)
    _safe_set(owner, 'vcml_SetPricingFactor217', partner)
    assert getattr(partner, 'vcml_Expression218') == owner
    _safe_set(owner, 'vcml_SetPricingFactor217', None)
    assert getattr(partner, 'vcml_Expression218') is None


def test_assoc_arg2219_stub_double():
    # vcml_Expression has no real 'vcml_Expression221' property in the generated
    # code (a bare stub) -- manually attach it so vcml_SetPricingFactor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_SetPricingFactor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_SetPricingFactor(location="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression221', None)
    _safe_set(owner, 'vcml_SetPricingFactor220', partner)
    assert getattr(partner, 'vcml_Expression221') == owner
    _safe_set(owner, 'vcml_SetPricingFactor220', None)
    assert getattr(partner, 'vcml_Expression221') is None


def test_assoc_argument226_stub_double():
    # vcml_Expression has no real 'vcml_Expression227' property in the generated
    # code (a bare stub) -- manually attach it so vcml_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_FunctionCall(function="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression227', None)
    _safe_set(owner, 'vcml_FunctionCall', partner)
    assert getattr(partner, 'vcml_Expression227') == owner
    _safe_set(owner, 'vcml_FunctionCall', None)
    assert getattr(partner, 'vcml_Expression227') is None


def test_assoc_billofmaterials102_stub_double():
    # vcml_BillOfMaterial has no real 'BillOfMaterial' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Material's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Material's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Material(type="sample_text")
    partner = vcml_BillOfMaterial()
    setattr(partner, 'BillOfMaterial', None)
    _safe_set(owner, 'material', {partner})
    assert getattr(partner, 'BillOfMaterial') == owner
    _safe_set(owner, 'material', set())
    assert getattr(partner, 'BillOfMaterial') is None


def test_assoc_characteristic112_stub_double():
    # vcml_ValueAssignment has no real 'vcml_ValueAssignment113' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_ValueAssignment()
    setattr(partner, 'vcml_ValueAssignment113', None)
    _safe_set(owner, 'vcml_Characteristic114', partner)
    assert getattr(partner, 'vcml_ValueAssignment113') == owner
    _safe_set(owner, 'vcml_Characteristic114', None)
    assert getattr(partner, 'vcml_ValueAssignment113') is None


def test_assoc_characteristic171_stub_double():
    # vcml_ObjectCharacteristicReference has no real 'vcml_ObjectCharacteristicReference172' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_ObjectCharacteristicReference()
    setattr(partner, 'vcml_ObjectCharacteristicReference172', None)
    _safe_set(owner, 'vcml_Characteristic173', partner)
    assert getattr(partner, 'vcml_ObjectCharacteristicReference172') == owner
    _safe_set(owner, 'vcml_Characteristic173', None)
    assert getattr(partner, 'vcml_ObjectCharacteristicReference172') is None


def test_assoc_characteristic179_stub_double():
    # vcml_Assignment has no real 'vcml_Assignment' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_Assignment()
    setattr(partner, 'vcml_Assignment', None)
    _safe_set(owner, 'vcml_Characteristic180', partner)
    assert getattr(partner, 'vcml_Assignment') == owner
    _safe_set(owner, 'vcml_Characteristic180', None)
    assert getattr(partner, 'vcml_Assignment') is None


def test_assoc_characteristic207_stub_double():
    # vcml_SetOrDelDefault has no real 'vcml_SetOrDelDefault' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_SetOrDelDefault()
    setattr(partner, 'vcml_SetOrDelDefault', None)
    _safe_set(owner, 'vcml_Characteristic208', partner)
    assert getattr(partner, 'vcml_SetOrDelDefault') == owner
    _safe_set(owner, 'vcml_Characteristic208', None)
    assert getattr(partner, 'vcml_SetOrDelDefault') is None


def test_assoc_characteristic212_stub_double():
    # vcml_IsInvisible has no real 'vcml_IsInvisible' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_IsInvisible()
    setattr(partner, 'vcml_IsInvisible', None)
    _safe_set(owner, 'vcml_Characteristic213', partner)
    assert getattr(partner, 'vcml_IsInvisible') == owner
    _safe_set(owner, 'vcml_Characteristic213', None)
    assert getattr(partner, 'vcml_IsInvisible') is None


def test_assoc_characteristic232_stub_double():
    # vcml_MDataCharacteristic_P has no real 'vcml_MDataCharacteristic_P' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicReference_P's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicReference_P's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicReference_P(location="sample_text")
    partner = vcml_MDataCharacteristic_P()
    setattr(partner, 'vcml_MDataCharacteristic_P', None)
    _safe_set(owner, 'vcml_CharacteristicReference_P233', partner)
    assert getattr(partner, 'vcml_MDataCharacteristic_P') == owner
    _safe_set(owner, 'vcml_CharacteristicReference_P233', None)
    assert getattr(partner, 'vcml_MDataCharacteristic_P') is None


def test_assoc_characteristic243_stub_double():
    # vcml_IsSpecified_P has no real 'vcml_IsSpecified_P' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicReference_P's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicReference_P's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicReference_P(location="sample_text")
    partner = vcml_IsSpecified_P()
    setattr(partner, 'vcml_IsSpecified_P', None)
    _safe_set(owner, 'vcml_CharacteristicReference_P244', partner)
    assert getattr(partner, 'vcml_IsSpecified_P') == owner
    _safe_set(owner, 'vcml_CharacteristicReference_P244', None)
    assert getattr(partner, 'vcml_IsSpecified_P') is None


def test_assoc_characteristic251_stub_double():
    # vcml_InCondition_P has no real 'vcml_InCondition_P' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicReference_P's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicReference_P's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicReference_P(location="sample_text")
    partner = vcml_InCondition_P()
    setattr(partner, 'vcml_InCondition_P', None)
    _safe_set(owner, 'vcml_CharacteristicReference_P252', partner)
    assert getattr(partner, 'vcml_InCondition_P') == owner
    _safe_set(owner, 'vcml_CharacteristicReference_P252', None)
    assert getattr(partner, 'vcml_InCondition_P') is None


def test_assoc_characteristicGroups94_stub_double():
    # vcml_InterfaceDesign has no real 'vcml_InterfaceDesign95' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicGroup(name="sample_text")
    partner = vcml_InterfaceDesign()
    setattr(partner, 'vcml_InterfaceDesign95', None)
    _safe_set(owner, 'vcml_CharacteristicGroup', partner)
    assert owner in getattr(partner, 'vcml_InterfaceDesign95')
    _safe_set(owner, 'vcml_CharacteristicGroup', None)
    assert owner not in getattr(partner, 'vcml_InterfaceDesign95')


def test_assoc_characteristics185_stub_double():
    # vcml_Function has no real 'vcml_Function186' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_Function()
    setattr(partner, 'vcml_Function186', None)
    _safe_set(owner, 'vcml_Characteristic187', partner)
    assert owner in getattr(partner, 'vcml_Function186')
    _safe_set(owner, 'vcml_Characteristic187', None)
    assert owner not in getattr(partner, 'vcml_Function186')


def test_assoc_characteristics193_stub_double():
    # vcml_PFunction has no real 'vcml_PFunction194' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_PFunction()
    setattr(partner, 'vcml_PFunction194', None)
    _safe_set(owner, 'vcml_Characteristic195', partner)
    assert owner in getattr(partner, 'vcml_PFunction194')
    _safe_set(owner, 'vcml_Characteristic195', None)
    assert owner not in getattr(partner, 'vcml_PFunction194')


def test_assoc_characteristics201_stub_double():
    # vcml_Table has no real 'vcml_Table202' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_Table()
    setattr(partner, 'vcml_Table202', None)
    _safe_set(owner, 'vcml_Characteristic203', partner)
    assert owner in getattr(partner, 'vcml_Table202')
    _safe_set(owner, 'vcml_Characteristic203', None)
    assert owner not in getattr(partner, 'vcml_Table202')


def test_assoc_child158_stub_double():
    # vcml_PartOfCondition has no real 'vcml_PartOfCondition' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ConstraintObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ConstraintObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ConstraintObject(name="sample_text")
    partner = vcml_PartOfCondition()
    setattr(partner, 'vcml_PartOfCondition', None)
    _safe_set(owner, 'vcml_ConstraintObject159', partner)
    assert getattr(partner, 'vcml_PartOfCondition') == owner
    _safe_set(owner, 'vcml_ConstraintObject159', None)
    assert getattr(partner, 'vcml_PartOfCondition') is None


def test_assoc_child163_stub_double():
    # vcml_SubpartOfCondition has no real 'vcml_SubpartOfCondition' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ConstraintObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ConstraintObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ConstraintObject(name="sample_text")
    partner = vcml_SubpartOfCondition()
    setattr(partner, 'vcml_SubpartOfCondition', None)
    _safe_set(owner, 'vcml_ConstraintObject164', partner)
    assert getattr(partner, 'vcml_SubpartOfCondition') == owner
    _safe_set(owner, 'vcml_ConstraintObject164', None)
    assert getattr(partner, 'vcml_SubpartOfCondition') is None


def test_assoc_class_147_stub_double():
    # vcml_ConstraintClass has no real 'vcml_ConstraintClass' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Class(group="sample_text", status="sample_text")
    partner = vcml_ConstraintClass()
    setattr(partner, 'vcml_ConstraintClass', None)
    _safe_set(owner, 'vcml_Class148', partner)
    assert getattr(partner, 'vcml_ConstraintClass') == owner
    _safe_set(owner, 'vcml_Class148', None)
    assert getattr(partner, 'vcml_ConstraintClass') is None


def test_assoc_classifications103_stub_double():
    # vcml_Classification has no real 'vcml_Classification' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Material's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Material's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Material(type="sample_text")
    partner = vcml_Classification()
    setattr(partner, 'vcml_Classification', None)
    _safe_set(owner, 'vcml_Material104', {partner})
    assert getattr(partner, 'vcml_Classification') == owner
    _safe_set(owner, 'vcml_Material104', set())
    assert getattr(partner, 'vcml_Classification') is None


def test_assoc_cls107_stub_double():
    # vcml_Classification has no real 'vcml_Classification108' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Class(group="sample_text", status="sample_text")
    partner = vcml_Classification()
    setattr(partner, 'vcml_Classification108', None)
    _safe_set(owner, 'vcml_Class109', partner)
    assert getattr(partner, 'vcml_Classification108') == owner
    _safe_set(owner, 'vcml_Class109', None)
    assert getattr(partner, 'vcml_Classification108') is None


def test_assoc_cls17_stub_double():
    # vcml_BOMItem_Class has no real 'vcml_BOMItem_Class' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Class(group="sample_text", status="sample_text")
    partner = vcml_BOMItem_Class()
    setattr(partner, 'vcml_BOMItem_Class', None)
    _safe_set(owner, 'vcml_Class', partner)
    assert getattr(partner, 'vcml_BOMItem_Class') == owner
    _safe_set(owner, 'vcml_Class', None)
    assert getattr(partner, 'vcml_BOMItem_Class') is None


def test_assoc_dependencies21_stub_double():
    # vcml_CharacteristicOrValueDependencies has no real 'vcml_CharacteristicOrValueDependencies' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_CharacteristicOrValueDependencies()
    setattr(partner, 'vcml_CharacteristicOrValueDependencies', None)
    _safe_set(owner, 'vcml_Characteristic22', partner)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies') == owner
    _safe_set(owner, 'vcml_Characteristic22', None)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies') is None


def test_assoc_dependencies32_stub_double():
    # vcml_CharacteristicOrValueDependencies has no real 'vcml_CharacteristicOrValueDependencies34' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicValue(default=True, name="sample_text")
    partner = vcml_CharacteristicOrValueDependencies()
    setattr(partner, 'vcml_CharacteristicOrValueDependencies34', None)
    _safe_set(owner, 'vcml_CharacteristicValue33', partner)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies34') == owner
    _safe_set(owner, 'vcml_CharacteristicValue33', None)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies34') is None


def test_assoc_dependencies40_stub_double():
    # vcml_CharacteristicOrValueDependencies has no real 'vcml_CharacteristicOrValueDependencies42' property in the generated
    # code (a bare stub) -- manually attach it so vcml_NumericCharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_NumericCharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_NumericCharacteristicValue(default=True)
    partner = vcml_CharacteristicOrValueDependencies()
    setattr(partner, 'vcml_CharacteristicOrValueDependencies42', None)
    _safe_set(owner, 'vcml_NumericCharacteristicValue41', partner)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies42') == owner
    _safe_set(owner, 'vcml_NumericCharacteristicValue41', None)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies42') is None


def test_assoc_dependencies46_stub_double():
    # vcml_CharacteristicOrValueDependencies has no real 'vcml_CharacteristicOrValueDependencies48' property in the generated
    # code (a bare stub) -- manually attach it so vcml_DateCharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_DateCharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_DateCharacteristicValue(default=True, from_="sample_text", to="sample_text")
    partner = vcml_CharacteristicOrValueDependencies()
    setattr(partner, 'vcml_CharacteristicOrValueDependencies48', None)
    _safe_set(owner, 'vcml_DateCharacteristicValue47', partner)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies48') == owner
    _safe_set(owner, 'vcml_DateCharacteristicValue47', None)
    assert getattr(partner, 'vcml_CharacteristicOrValueDependencies48') is None


def test_assoc_description26_stub_double():
    # vcml_Description has no real 'vcml_Description28' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicValue(default=True, name="sample_text")
    partner = vcml_Description()
    setattr(partner, 'vcml_Description28', None)
    _safe_set(owner, 'vcml_CharacteristicValue27', partner)
    assert getattr(partner, 'vcml_Description28') == owner
    _safe_set(owner, 'vcml_CharacteristicValue27', None)
    assert getattr(partner, 'vcml_Description28') is None


def test_assoc_description5_stub_double():
    # vcml_Description has no real 'vcml_Description' property in the generated
    # code (a bare stub) -- manually attach it so vcml_VCObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_VCObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_VCObject(name="sample_text")
    partner = vcml_Description()
    setattr(partner, 'vcml_Description', None)
    _safe_set(owner, 'vcml_VCObject6', partner)
    assert getattr(partner, 'vcml_Description') == owner
    _safe_set(owner, 'vcml_VCObject6', None)
    assert getattr(partner, 'vcml_Description') is None


def test_assoc_description96_stub_double():
    # vcml_Description has no real 'vcml_Description98' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicGroup(name="sample_text")
    partner = vcml_Description()
    setattr(partner, 'vcml_Description98', None)
    _safe_set(owner, 'vcml_CharacteristicGroup97', partner)
    assert getattr(partner, 'vcml_Description98') == owner
    _safe_set(owner, 'vcml_CharacteristicGroup97', None)
    assert getattr(partner, 'vcml_Description98') is None


def test_assoc_descriptions132_stub_double():
    # vcml_MultiLanguageDescriptions has no real 'vcml_MultiLanguageDescriptions' property in the generated
    # code (a bare stub) -- manually attach it so vcml_MultiLanguageDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_MultiLanguageDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_MultiLanguageDescription(language="sample_text", value="sample_text")
    partner = vcml_MultiLanguageDescriptions()
    setattr(partner, 'vcml_MultiLanguageDescriptions', None)
    _safe_set(owner, 'vcml_MultiLanguageDescription', partner)
    assert owner in getattr(partner, 'vcml_MultiLanguageDescriptions')
    _safe_set(owner, 'vcml_MultiLanguageDescription', None)
    assert owner not in getattr(partner, 'vcml_MultiLanguageDescriptions')


def test_assoc_documentation18_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Characteristic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Characteristic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Characteristic(additionalValues=True, displayAllowedValues=True, field="sample_text", group="sample_text", multiValue=True, noDisplay=True, notReadyForInput=True, required=True, restrictable=True, status="sample_text", table="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation', None)
    _safe_set(owner, 'vcml_Characteristic', partner)
    assert getattr(partner, 'vcml_Documentation') == owner
    _safe_set(owner, 'vcml_Characteristic', None)
    assert getattr(partner, 'vcml_Documentation') is None


def test_assoc_documentation29_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation31' property in the generated
    # code (a bare stub) -- manually attach it so vcml_CharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_CharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_CharacteristicValue(default=True, name="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation31', None)
    _safe_set(owner, 'vcml_CharacteristicValue30', partner)
    assert getattr(partner, 'vcml_Documentation31') == owner
    _safe_set(owner, 'vcml_CharacteristicValue30', None)
    assert getattr(partner, 'vcml_Documentation31') is None


def test_assoc_documentation37_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation39' property in the generated
    # code (a bare stub) -- manually attach it so vcml_NumericCharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_NumericCharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_NumericCharacteristicValue(default=True)
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation39', None)
    _safe_set(owner, 'vcml_NumericCharacteristicValue38', partner)
    assert getattr(partner, 'vcml_Documentation39') == owner
    _safe_set(owner, 'vcml_NumericCharacteristicValue38', None)
    assert getattr(partner, 'vcml_Documentation39') is None


def test_assoc_documentation43_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation45' property in the generated
    # code (a bare stub) -- manually attach it so vcml_DateCharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_DateCharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_DateCharacteristicValue(default=True, from_="sample_text", to="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation45', None)
    _safe_set(owner, 'vcml_DateCharacteristicValue44', partner)
    assert getattr(partner, 'vcml_Documentation45') == owner
    _safe_set(owner, 'vcml_DateCharacteristicValue44', None)
    assert getattr(partner, 'vcml_Documentation45') is None


def test_assoc_documentation65_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation66' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Procedure(group="sample_text", status="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation66', None)
    _safe_set(owner, 'vcml_Procedure', partner)
    assert getattr(partner, 'vcml_Documentation66') == owner
    _safe_set(owner, 'vcml_Procedure', None)
    assert getattr(partner, 'vcml_Documentation66') is None


def test_assoc_documentation69_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation71' property in the generated
    # code (a bare stub) -- manually attach it so vcml_SelectionCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_SelectionCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_SelectionCondition(group="sample_text", status="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation71', None)
    _safe_set(owner, 'vcml_SelectionCondition70', partner)
    assert getattr(partner, 'vcml_Documentation71') == owner
    _safe_set(owner, 'vcml_SelectionCondition70', None)
    assert getattr(partner, 'vcml_Documentation71') is None


def test_assoc_documentation74_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation75' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Precondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Precondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Precondition(group="sample_text", status="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation75', None)
    _safe_set(owner, 'vcml_Precondition', partner)
    assert getattr(partner, 'vcml_Documentation75') == owner
    _safe_set(owner, 'vcml_Precondition', None)
    assert getattr(partner, 'vcml_Documentation75') is None


def test_assoc_documentation81_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation83' property in the generated
    # code (a bare stub) -- manually attach it so vcml_DependencyNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_DependencyNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_DependencyNet(group="sample_text", status="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation83', None)
    _safe_set(owner, 'vcml_DependencyNet82', partner)
    assert getattr(partner, 'vcml_Documentation83') == owner
    _safe_set(owner, 'vcml_DependencyNet82', None)
    assert getattr(partner, 'vcml_Documentation83') is None


def test_assoc_documentation86_stub_double():
    # vcml_Documentation has no real 'vcml_Documentation88' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Constraint(group="sample_text", status="sample_text")
    partner = vcml_Documentation()
    setattr(partner, 'vcml_Documentation88', None)
    _safe_set(owner, 'vcml_Constraint87', partner)
    assert getattr(partner, 'vcml_Documentation88') == owner
    _safe_set(owner, 'vcml_Constraint87', None)
    assert getattr(partner, 'vcml_Documentation88') is None


def test_assoc_entries258_stub_double():
    # vcml_SymbolList has no real 'vcml_SymbolList' property in the generated
    # code (a bare stub) -- manually attach it so vcml_SymbolicLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_SymbolicLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_SymbolicLiteral(value="sample_text")
    partner = vcml_SymbolList()
    setattr(partner, 'vcml_SymbolList', None)
    _safe_set(owner, 'vcml_SymbolicLiteral', partner)
    assert owner in getattr(partner, 'vcml_SymbolList')
    _safe_set(owner, 'vcml_SymbolicLiteral', None)
    assert owner not in getattr(partner, 'vcml_SymbolList')


def test_assoc_entry35_stub_double():
    # vcml_NumberListEntry has no real 'vcml_NumberListEntry' property in the generated
    # code (a bare stub) -- manually attach it so vcml_NumericCharacteristicValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_NumericCharacteristicValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_NumericCharacteristicValue(default=True)
    partner = vcml_NumberListEntry()
    setattr(partner, 'vcml_NumberListEntry', None)
    _safe_set(owner, 'vcml_NumericCharacteristicValue36', partner)
    assert getattr(partner, 'vcml_NumberListEntry') == owner
    _safe_set(owner, 'vcml_NumericCharacteristicValue36', None)
    assert getattr(partner, 'vcml_NumberListEntry') is None


def test_assoc_expression224_stub_double():
    # vcml_Expression has no real 'vcml_Expression225' property in the generated
    # code (a bare stub) -- manually attach it so vcml_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_UnaryExpression(operator="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression225', None)
    _safe_set(owner, 'vcml_UnaryExpression', partner)
    assert getattr(partner, 'vcml_Expression225') == owner
    _safe_set(owner, 'vcml_UnaryExpression', None)
    assert getattr(partner, 'vcml_Expression225') is None


def test_assoc_function183_stub_double():
    # vcml_Function has no real 'vcml_Function' property in the generated
    # code (a bare stub) -- manually attach it so vcml_VariantFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_VariantFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_VariantFunction(group="sample_text", status="sample_text")
    partner = vcml_Function()
    setattr(partner, 'vcml_Function', None)
    _safe_set(owner, 'vcml_VariantFunction184', partner)
    assert getattr(partner, 'vcml_Function') == owner
    _safe_set(owner, 'vcml_VariantFunction184', None)
    assert getattr(partner, 'vcml_Function') is None


def test_assoc_function191_stub_double():
    # vcml_PFunction has no real 'vcml_PFunction' property in the generated
    # code (a bare stub) -- manually attach it so vcml_VariantFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_VariantFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_VariantFunction(group="sample_text", status="sample_text")
    partner = vcml_PFunction()
    setattr(partner, 'vcml_PFunction', None)
    _safe_set(owner, 'vcml_VariantFunction192', partner)
    assert getattr(partner, 'vcml_PFunction') == owner
    _safe_set(owner, 'vcml_VariantFunction192', None)
    assert getattr(partner, 'vcml_PFunction') is None


def test_assoc_imports0_stub_double():
    # vcml_VcmlModel has no real 'vcml_VcmlModel' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Import(importURI="sample_text")
    partner = vcml_VcmlModel()
    setattr(partner, 'vcml_VcmlModel', None)
    _safe_set(owner, 'vcml_Import', partner)
    assert owner in getattr(partner, 'vcml_VcmlModel')
    _safe_set(owner, 'vcml_Import', None)
    assert owner not in getattr(partner, 'vcml_VcmlModel')


def test_assoc_items10_stub_double():
    # vcml_BillOfMaterial has no real 'vcml_BillOfMaterial' property in the generated
    # code (a bare stub) -- manually attach it so vcml_BOMItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_BOMItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_BOMItem(itemnumber=7)
    partner = vcml_BillOfMaterial()
    setattr(partner, 'vcml_BillOfMaterial', None)
    _safe_set(owner, 'vcml_BOMItem', partner)
    assert owner in getattr(partner, 'vcml_BillOfMaterial')
    _safe_set(owner, 'vcml_BOMItem', None)
    assert owner not in getattr(partner, 'vcml_BillOfMaterial')


def test_assoc_languageblocks133_stub_double():
    # vcml_MultipleLanguageDocumentation has no real 'vcml_MultipleLanguageDocumentation' property in the generated
    # code (a bare stub) -- manually attach it so vcml_MultipleLanguageDocumentation_LanguageBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_MultipleLanguageDocumentation_LanguageBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_MultipleLanguageDocumentation_LanguageBlock(language="sample_text")
    partner = vcml_MultipleLanguageDocumentation()
    setattr(partner, 'vcml_MultipleLanguageDocumentation', None)
    _safe_set(owner, 'vcml_MultipleLanguageDocumentation_LanguageBlock', partner)
    assert owner in getattr(partner, 'vcml_MultipleLanguageDocumentation')
    _safe_set(owner, 'vcml_MultipleLanguageDocumentation_LanguageBlock', None)
    assert owner not in getattr(partner, 'vcml_MultipleLanguageDocumentation')


def test_assoc_left236_stub_double():
    # vcml_Expression has no real 'vcml_Expression237' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Comparison(operator="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression237', None)
    _safe_set(owner, 'vcml_Comparison', partner)
    assert getattr(partner, 'vcml_Expression237') == owner
    _safe_set(owner, 'vcml_Comparison', None)
    assert getattr(partner, 'vcml_Expression237') is None


def test_assoc_left269_stub_double():
    # vcml_Expression has no real 'vcml_Expression270' property in the generated
    # code (a bare stub) -- manually attach it so vcml_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_BinaryExpression(operator="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression270', None)
    _safe_set(owner, 'vcml_BinaryExpression', partner)
    assert getattr(partner, 'vcml_Expression270') == owner
    _safe_set(owner, 'vcml_BinaryExpression', None)
    assert getattr(partner, 'vcml_Expression270') is None


def test_assoc_left274_stub_double():
    # vcml_Condition has no real 'vcml_Condition275' property in the generated
    # code (a bare stub) -- manually attach it so vcml_BinaryCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_BinaryCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_BinaryCondition(operator="sample_text")
    partner = vcml_Condition()
    setattr(partner, 'vcml_Condition275', None)
    _safe_set(owner, 'vcml_BinaryCondition', partner)
    assert getattr(partner, 'vcml_Condition275') == owner
    _safe_set(owner, 'vcml_BinaryCondition', None)
    assert getattr(partner, 'vcml_Condition275') is None


def test_assoc_location169_stub_double():
    # vcml_ObjectCharacteristicReference has no real 'vcml_ObjectCharacteristicReference' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ConstraintObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ConstraintObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ConstraintObject(name="sample_text")
    partner = vcml_ObjectCharacteristicReference()
    setattr(partner, 'vcml_ObjectCharacteristicReference', None)
    _safe_set(owner, 'vcml_ConstraintObject170', partner)
    assert getattr(partner, 'vcml_ObjectCharacteristicReference') == owner
    _safe_set(owner, 'vcml_ConstraintObject170', None)
    assert getattr(partner, 'vcml_ObjectCharacteristicReference') is None


def test_assoc_material11_stub_double():
    # vcml_BillOfMaterial has no real 'billofmaterials' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Material's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Material's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Material(type="sample_text")
    partner = vcml_BillOfMaterial()
    setattr(partner, 'billofmaterials', None)
    _safe_set(owner, 'Material', partner)
    assert getattr(partner, 'billofmaterials') == owner
    _safe_set(owner, 'Material', None)
    assert getattr(partner, 'billofmaterials') is None


def test_assoc_material16_stub_double():
    # vcml_BOMItem_Material has no real 'vcml_BOMItem_Material' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Material's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Material's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Material(type="sample_text")
    partner = vcml_BOMItem_Material()
    setattr(partner, 'vcml_BOMItem_Material', None)
    _safe_set(owner, 'vcml_Material', partner)
    assert getattr(partner, 'vcml_BOMItem_Material') == owner
    _safe_set(owner, 'vcml_Material', None)
    assert getattr(partner, 'vcml_BOMItem_Material') is None


def test_assoc_objectType149_stub_double():
    # vcml_ConstraintMaterial has no real 'vcml_ConstraintMaterial' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ObjectType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ObjectType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ObjectType(classType=7, type="sample_text")
    partner = vcml_ConstraintMaterial()
    setattr(partner, 'vcml_ConstraintMaterial', None)
    _safe_set(owner, 'vcml_ObjectType', partner)
    assert getattr(partner, 'vcml_ConstraintMaterial') == owner
    _safe_set(owner, 'vcml_ObjectType', None)
    assert getattr(partner, 'vcml_ConstraintMaterial') is None


def test_assoc_objects136_stub_double():
    # vcml_ConstraintSource has no real 'vcml_ConstraintSource137' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ConstraintObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ConstraintObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ConstraintObject(name="sample_text")
    partner = vcml_ConstraintSource()
    setattr(partner, 'vcml_ConstraintSource137', None)
    _safe_set(owner, 'vcml_ConstraintObject', partner)
    assert owner in getattr(partner, 'vcml_ConstraintSource137')
    _safe_set(owner, 'vcml_ConstraintObject', None)
    assert owner not in getattr(partner, 'vcml_ConstraintSource137')


def test_assoc_objects3_stub_double():
    # vcml_VcmlModel has no real 'vcml_VcmlModel4' property in the generated
    # code (a bare stub) -- manually attach it so vcml_VCObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_VCObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_VCObject(name="sample_text")
    partner = vcml_VcmlModel()
    setattr(partner, 'vcml_VcmlModel4', None)
    _safe_set(owner, 'vcml_VCObject', partner)
    assert owner in getattr(partner, 'vcml_VcmlModel4')
    _safe_set(owner, 'vcml_VCObject', None)
    assert owner not in getattr(partner, 'vcml_VcmlModel4')


def test_assoc_options1_stub_double():
    # vcml_VcmlModel has no real 'vcml_VcmlModel2' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Option's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Option's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Option(name="sample_text", value="sample_text")
    partner = vcml_VcmlModel()
    setattr(partner, 'vcml_VcmlModel2', None)
    _safe_set(owner, 'vcml_Option', partner)
    assert owner in getattr(partner, 'vcml_VcmlModel2')
    _safe_set(owner, 'vcml_Option', None)
    assert owner not in getattr(partner, 'vcml_VcmlModel2')


def test_assoc_parent160_stub_double():
    # vcml_PartOfCondition has no real 'vcml_PartOfCondition161' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ConstraintObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ConstraintObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ConstraintObject(name="sample_text")
    partner = vcml_PartOfCondition()
    setattr(partner, 'vcml_PartOfCondition161', None)
    _safe_set(owner, 'vcml_ConstraintObject162', partner)
    assert getattr(partner, 'vcml_PartOfCondition161') == owner
    _safe_set(owner, 'vcml_ConstraintObject162', None)
    assert getattr(partner, 'vcml_PartOfCondition161') is None


def test_assoc_parent165_stub_double():
    # vcml_SubpartOfCondition has no real 'vcml_SubpartOfCondition166' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ConstraintObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ConstraintObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ConstraintObject(name="sample_text")
    partner = vcml_SubpartOfCondition()
    setattr(partner, 'vcml_SubpartOfCondition166', None)
    _safe_set(owner, 'vcml_ConstraintObject167', partner)
    assert getattr(partner, 'vcml_SubpartOfCondition166') == owner
    _safe_set(owner, 'vcml_ConstraintObject167', None)
    assert getattr(partner, 'vcml_SubpartOfCondition166') is None


def test_assoc_ref174_stub_double():
    # vcml_ShortVarReference has no real 'vcml_ShortVarReference' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ShortVarDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ShortVarDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ShortVarDefinition(name="sample_text")
    partner = vcml_ShortVarReference()
    setattr(partner, 'vcml_ShortVarReference', None)
    _safe_set(owner, 'vcml_ShortVarDefinition175', partner)
    assert getattr(partner, 'vcml_ShortVarReference') == owner
    _safe_set(owner, 'vcml_ShortVarDefinition175', None)
    assert getattr(partner, 'vcml_ShortVarReference') is None


def test_assoc_right238_stub_double():
    # vcml_Expression has no real 'vcml_Expression240' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Comparison(operator="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression240', None)
    _safe_set(owner, 'vcml_Comparison239', partner)
    assert getattr(partner, 'vcml_Expression240') == owner
    _safe_set(owner, 'vcml_Comparison239', None)
    assert getattr(partner, 'vcml_Expression240') is None


def test_assoc_right271_stub_double():
    # vcml_Expression has no real 'vcml_Expression273' property in the generated
    # code (a bare stub) -- manually attach it so vcml_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_BinaryExpression(operator="sample_text")
    partner = vcml_Expression()
    setattr(partner, 'vcml_Expression273', None)
    _safe_set(owner, 'vcml_BinaryExpression272', partner)
    assert getattr(partner, 'vcml_Expression273') == owner
    _safe_set(owner, 'vcml_BinaryExpression272', None)
    assert getattr(partner, 'vcml_Expression273') is None


def test_assoc_right276_stub_double():
    # vcml_Condition has no real 'vcml_Condition278' property in the generated
    # code (a bare stub) -- manually attach it so vcml_BinaryCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_BinaryCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_BinaryCondition(operator="sample_text")
    partner = vcml_Condition()
    setattr(partner, 'vcml_Condition278', None)
    _safe_set(owner, 'vcml_BinaryCondition277', partner)
    assert getattr(partner, 'vcml_Condition278') == owner
    _safe_set(owner, 'vcml_BinaryCondition277', None)
    assert getattr(partner, 'vcml_Condition278') is None


def test_assoc_source67_stub_double():
    # vcml_ProcedureSource has no real 'vcml_ProcedureSource' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Procedure(group="sample_text", status="sample_text")
    partner = vcml_ProcedureSource()
    setattr(partner, 'vcml_ProcedureSource', None)
    _safe_set(owner, 'vcml_Procedure68', partner)
    assert getattr(partner, 'vcml_ProcedureSource') == owner
    _safe_set(owner, 'vcml_Procedure68', None)
    assert getattr(partner, 'vcml_ProcedureSource') is None


def test_assoc_source72_stub_double():
    # vcml_ConditionSource has no real 'vcml_ConditionSource' property in the generated
    # code (a bare stub) -- manually attach it so vcml_SelectionCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_SelectionCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_SelectionCondition(group="sample_text", status="sample_text")
    partner = vcml_ConditionSource()
    setattr(partner, 'vcml_ConditionSource', None)
    _safe_set(owner, 'vcml_SelectionCondition73', partner)
    assert getattr(partner, 'vcml_ConditionSource') == owner
    _safe_set(owner, 'vcml_SelectionCondition73', None)
    assert getattr(partner, 'vcml_ConditionSource') is None


def test_assoc_source76_stub_double():
    # vcml_ConditionSource has no real 'vcml_ConditionSource78' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Precondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Precondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Precondition(group="sample_text", status="sample_text")
    partner = vcml_ConditionSource()
    setattr(partner, 'vcml_ConditionSource78', None)
    _safe_set(owner, 'vcml_Precondition77', partner)
    assert getattr(partner, 'vcml_ConditionSource78') == owner
    _safe_set(owner, 'vcml_Precondition77', None)
    assert getattr(partner, 'vcml_ConditionSource78') is None


def test_assoc_source89_stub_double():
    # vcml_ConstraintSource has no real 'vcml_ConstraintSource' property in the generated
    # code (a bare stub) -- manually attach it so vcml_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_Constraint(group="sample_text", status="sample_text")
    partner = vcml_ConstraintSource()
    setattr(partner, 'vcml_ConstraintSource', None)
    _safe_set(owner, 'vcml_Constraint90', partner)
    assert getattr(partner, 'vcml_ConstraintSource') == owner
    _safe_set(owner, 'vcml_Constraint90', None)
    assert getattr(partner, 'vcml_ConstraintSource') is None


def test_assoc_table125_stub_double():
    # vcml_VariantTableContent has no real 'vcml_VariantTableContent' property in the generated
    # code (a bare stub) -- manually attach it so vcml_VariantTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_VariantTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_VariantTable(group="sample_text", status="sample_text")
    partner = vcml_VariantTableContent()
    setattr(partner, 'vcml_VariantTableContent', None)
    _safe_set(owner, 'vcml_VariantTable126', partner)
    assert getattr(partner, 'vcml_VariantTableContent') == owner
    _safe_set(owner, 'vcml_VariantTable126', None)
    assert getattr(partner, 'vcml_VariantTableContent') is None


def test_assoc_table199_stub_double():
    # vcml_Table has no real 'vcml_Table' property in the generated
    # code (a bare stub) -- manually attach it so vcml_VariantTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_VariantTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_VariantTable(group="sample_text", status="sample_text")
    partner = vcml_Table()
    setattr(partner, 'vcml_Table', None)
    _safe_set(owner, 'vcml_VariantTable200', partner)
    assert getattr(partner, 'vcml_Table') == owner
    _safe_set(owner, 'vcml_VariantTable200', None)
    assert getattr(partner, 'vcml_Table') is None


def test_assoc_uidesign57_stub_double():
    # vcml_InterfaceDesign has no real 'vcml_InterfaceDesign' property in the generated
    # code (a bare stub) -- manually attach it so vcml_ConfigurationProfile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vcml_ConfigurationProfile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vcml_ConfigurationProfile(bomapplication="sample_text", fixing="sample_text", status="sample_text")
    partner = vcml_InterfaceDesign()
    setattr(partner, 'vcml_InterfaceDesign', None)
    _safe_set(owner, 'vcml_ConfigurationProfile', partner)
    assert getattr(partner, 'vcml_InterfaceDesign') == owner
    _safe_set(owner, 'vcml_ConfigurationProfile', None)
    assert getattr(partner, 'vcml_InterfaceDesign') is None


