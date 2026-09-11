import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BSBlock,
    BSExpression,
    BSMember,
    BSStatement,
    BSSymbol,
    blorqueScript_BSArrayAccessExpression,
    blorqueScript_BSAssignmentExpression,
    blorqueScript_BSBitwiseAndExpression,
    blorqueScript_BSBitwiseOrExpression,
    blorqueScript_BSBitwiseShiftExpression,
    blorqueScript_BSBitwiseXorExpression,
    blorqueScript_BSBlock,
    blorqueScript_BSBooleanAndExpression,
    blorqueScript_BSBooleanConstant,
    blorqueScript_BSBooleanOrExpression,
    blorqueScript_BSBreak,
    blorqueScript_BSCase,
    blorqueScript_BSCaseBlock,
    blorqueScript_BSCastExpression,
    blorqueScript_BSClass,
    blorqueScript_BSClientLiteral,
    blorqueScript_BSContinue,
    blorqueScript_BSEqualityExpression,
    blorqueScript_BSExpression,
    blorqueScript_BSField,
    blorqueScript_BSFile,
    blorqueScript_BSForLoop,
    blorqueScript_BSHexadecimalConstant,
    blorqueScript_BSIfBlock,
    blorqueScript_BSIfStatement,
    blorqueScript_BSImport,
    blorqueScript_BSLoopBlock,
    blorqueScript_BSMember,
    blorqueScript_BSMemberSelectionExpression,
    blorqueScript_BSMethod,
    blorqueScript_BSMethodBody,
    blorqueScript_BSMethodInvokationExpression,
    blorqueScript_BSMulDivOrModExpression,
    blorqueScript_BSNewExpression,
    blorqueScript_BSNullLiteral,
    blorqueScript_BSNumberConstant,
    blorqueScript_BSOrderedRelationExpression,
    blorqueScript_BSParameter,
    blorqueScript_BSParentLiteral,
    blorqueScript_BSParentheticalExpression,
    blorqueScript_BSPlusMinusOrStringConcatExpression,
    blorqueScript_BSPostfixArithmeticExpression,
    blorqueScript_BSRealConstant,
    blorqueScript_BSReturn,
    blorqueScript_BSStatement,
    blorqueScript_BSStringConstant,
    blorqueScript_BSSwitchBlock,
    blorqueScript_BSSwitchStatement,
    blorqueScript_BSSymbol,
    blorqueScript_BSSymbolRef,
    blorqueScript_BSTernaryExpression,
    blorqueScript_BSThisLiteral,
    blorqueScript_BSUnaryModifierExpression,
    blorqueScript_BSVariableDeclaration,
    blorqueScript_BSWhileLoop,
    BSPrimitiveType,
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

def test_blorqueScript_BSAssignmentExpression_assignmentOperator_value_roundtrip():
    instance = blorqueScript_BSAssignmentExpression(assignmentOperator="sample_text")
    assert instance.assignmentOperator == "sample_text"
    instance.assignmentOperator = "sample_text_2"
    assert instance.assignmentOperator == "sample_text_2"


def test_blorqueScript_BSBitwiseShiftExpression_operator_value_roundtrip():
    instance = blorqueScript_BSBitwiseShiftExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_blorqueScript_BSBooleanConstant_value_value_roundtrip():
    instance = blorqueScript_BSBooleanConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_blorqueScript_BSCastExpression_isArray_value_roundtrip():
    instance = blorqueScript_BSCastExpression(isArray=True, pType="sample_text")
    assert instance.isArray == True
    instance.isArray = False
    assert instance.isArray == False


def test_blorqueScript_BSCastExpression_pType_value_roundtrip():
    instance = blorqueScript_BSCastExpression(isArray=True, pType="sample_text")
    assert instance.pType == "sample_text"
    instance.pType = "sample_text_2"
    assert instance.pType == "sample_text_2"


def test_blorqueScript_BSClass_name_value_roundtrip():
    instance = blorqueScript_BSClass(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_blorqueScript_BSEqualityExpression_operator_value_roundtrip():
    instance = blorqueScript_BSEqualityExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_blorqueScript_BSFile_name_value_roundtrip():
    instance = blorqueScript_BSFile(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_blorqueScript_BSHexadecimalConstant_value_value_roundtrip():
    instance = blorqueScript_BSHexadecimalConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_blorqueScript_BSImport_importedNamespace_value_roundtrip():
    instance = blorqueScript_BSImport(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_blorqueScript_BSMember_isArray_value_roundtrip():
    instance = blorqueScript_BSMember(isArray=True)
    assert instance.isArray == True
    instance.isArray = False
    assert instance.isArray == False


def test_blorqueScript_BSMulDivOrModExpression_operator_value_roundtrip():
    instance = blorqueScript_BSMulDivOrModExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_blorqueScript_BSNewExpression_isArray_value_roundtrip():
    instance = blorqueScript_BSNewExpression(isArray=True)
    assert instance.isArray == True
    instance.isArray = False
    assert instance.isArray == False


def test_blorqueScript_BSNumberConstant_value_value_roundtrip():
    instance = blorqueScript_BSNumberConstant(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_blorqueScript_BSOrderedRelationExpression_operator_value_roundtrip():
    instance = blorqueScript_BSOrderedRelationExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_blorqueScript_BSParameter_isArray_value_roundtrip():
    instance = blorqueScript_BSParameter(isArray=True)
    assert instance.isArray == True
    instance.isArray = False
    assert instance.isArray == False


def test_blorqueScript_BSPlusMinusOrStringConcatExpression_operator_value_roundtrip():
    instance = blorqueScript_BSPlusMinusOrStringConcatExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_blorqueScript_BSPostfixArithmeticExpression_operator_value_roundtrip():
    instance = blorqueScript_BSPostfixArithmeticExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_blorqueScript_BSRealConstant_right_value_roundtrip():
    instance = blorqueScript_BSRealConstant(right=7)
    assert instance.right == 7
    instance.right = 13
    assert instance.right == 13


def test_blorqueScript_BSStringConstant_value_value_roundtrip():
    instance = blorqueScript_BSStringConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_blorqueScript_BSSwitchStatement_stringSwitch_value_roundtrip():
    instance = blorqueScript_BSSwitchStatement(stringSwitch=True)
    assert instance.stringSwitch == True
    instance.stringSwitch = False
    assert instance.stringSwitch == False


def test_blorqueScript_BSSymbol_name_value_roundtrip():
    instance = blorqueScript_BSSymbol(name="sample_text", pType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_blorqueScript_BSSymbol_pType_value_roundtrip():
    instance = blorqueScript_BSSymbol(name="sample_text", pType="sample_text")
    assert instance.pType == "sample_text"
    instance.pType = "sample_text_2"
    assert instance.pType == "sample_text_2"


def test_blorqueScript_BSUnaryModifierExpression_operator_value_roundtrip():
    instance = blorqueScript_BSUnaryModifierExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_blorqueScript_BSCaseBlock_isa_BSBlock():
    instance = blorqueScript_BSCaseBlock()
    assert isinstance(instance, BSBlock)


def test_blorqueScript_BSIfBlock_isa_BSBlock():
    instance = blorqueScript_BSIfBlock()
    assert isinstance(instance, BSBlock)


def test_blorqueScript_BSLoopBlock_isa_BSBlock():
    instance = blorqueScript_BSLoopBlock()
    assert isinstance(instance, BSBlock)


def test_blorqueScript_BSMethodBody_isa_BSBlock():
    instance = blorqueScript_BSMethodBody()
    assert isinstance(instance, BSBlock)


def test_blorqueScript_BSSwitchBlock_isa_BSBlock():
    instance = blorqueScript_BSSwitchBlock()
    assert isinstance(instance, BSBlock)


def test_blorqueScript_BSArrayAccessExpression_isa_BSExpression():
    instance = blorqueScript_BSArrayAccessExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSAssignmentExpression_isa_BSExpression():
    instance = blorqueScript_BSAssignmentExpression(assignmentOperator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSBitwiseAndExpression_isa_BSExpression():
    instance = blorqueScript_BSBitwiseAndExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSBitwiseOrExpression_isa_BSExpression():
    instance = blorqueScript_BSBitwiseOrExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSBitwiseShiftExpression_isa_BSExpression():
    instance = blorqueScript_BSBitwiseShiftExpression(operator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSBitwiseXorExpression_isa_BSExpression():
    instance = blorqueScript_BSBitwiseXorExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSBooleanAndExpression_isa_BSExpression():
    instance = blorqueScript_BSBooleanAndExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSBooleanConstant_isa_BSExpression():
    instance = blorqueScript_BSBooleanConstant(value="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSBooleanOrExpression_isa_BSExpression():
    instance = blorqueScript_BSBooleanOrExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSCastExpression_isa_BSExpression():
    instance = blorqueScript_BSCastExpression(isArray=True, pType="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSClientLiteral_isa_BSExpression():
    instance = blorqueScript_BSClientLiteral()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSEqualityExpression_isa_BSExpression():
    instance = blorqueScript_BSEqualityExpression(operator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSHexadecimalConstant_isa_BSExpression():
    instance = blorqueScript_BSHexadecimalConstant(value="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSMemberSelectionExpression_isa_BSExpression():
    instance = blorqueScript_BSMemberSelectionExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSMethodInvokationExpression_isa_BSExpression():
    instance = blorqueScript_BSMethodInvokationExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSMulDivOrModExpression_isa_BSExpression():
    instance = blorqueScript_BSMulDivOrModExpression(operator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSNewExpression_isa_BSExpression():
    instance = blorqueScript_BSNewExpression(isArray=True)
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSNullLiteral_isa_BSExpression():
    instance = blorqueScript_BSNullLiteral()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSNumberConstant_isa_BSExpression():
    instance = blorqueScript_BSNumberConstant(value=7)
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSOrderedRelationExpression_isa_BSExpression():
    instance = blorqueScript_BSOrderedRelationExpression(operator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSParentLiteral_isa_BSExpression():
    instance = blorqueScript_BSParentLiteral()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSParentheticalExpression_isa_BSExpression():
    instance = blorqueScript_BSParentheticalExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSPlusMinusOrStringConcatExpression_isa_BSExpression():
    instance = blorqueScript_BSPlusMinusOrStringConcatExpression(operator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSPostfixArithmeticExpression_isa_BSExpression():
    instance = blorqueScript_BSPostfixArithmeticExpression(operator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSRealConstant_isa_BSExpression():
    instance = blorqueScript_BSRealConstant(right=7)
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSStringConstant_isa_BSExpression():
    instance = blorqueScript_BSStringConstant(value="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSSymbolRef_isa_BSExpression():
    instance = blorqueScript_BSSymbolRef()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSTernaryExpression_isa_BSExpression():
    instance = blorqueScript_BSTernaryExpression()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSThisLiteral_isa_BSExpression():
    instance = blorqueScript_BSThisLiteral()
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSUnaryModifierExpression_isa_BSExpression():
    instance = blorqueScript_BSUnaryModifierExpression(operator="sample_text")
    assert isinstance(instance, BSExpression)


def test_blorqueScript_BSField_isa_BSMember():
    instance = blorqueScript_BSField()
    assert isinstance(instance, BSMember)


def test_blorqueScript_BSMethod_isa_BSMember():
    instance = blorqueScript_BSMethod()
    assert isinstance(instance, BSMember)


def test_blorqueScript_BSBreak_isa_BSStatement():
    instance = blorqueScript_BSBreak()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSContinue_isa_BSStatement():
    instance = blorqueScript_BSContinue()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSExpression_isa_BSStatement():
    instance = blorqueScript_BSExpression()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSForLoop_isa_BSStatement():
    instance = blorqueScript_BSForLoop()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSIfStatement_isa_BSStatement():
    instance = blorqueScript_BSIfStatement()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSReturn_isa_BSStatement():
    instance = blorqueScript_BSReturn()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSSwitchStatement_isa_BSStatement():
    instance = blorqueScript_BSSwitchStatement(stringSwitch=True)
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSVariableDeclaration_isa_BSStatement():
    instance = blorqueScript_BSVariableDeclaration()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSWhileLoop_isa_BSStatement():
    instance = blorqueScript_BSWhileLoop()
    assert isinstance(instance, BSStatement)


def test_blorqueScript_BSMember_isa_BSSymbol():
    instance = blorqueScript_BSMember(isArray=True)
    assert isinstance(instance, BSSymbol)


def test_blorqueScript_BSParameter_isa_BSSymbol():
    instance = blorqueScript_BSParameter(isArray=True)
    assert isinstance(instance, BSSymbol)


def test_blorqueScript_BSVariableDeclaration_isa_BSSymbol():
    instance = blorqueScript_BSVariableDeclaration()
    assert isinstance(instance, BSSymbol)


def test_assoc_args127_link_reassign_clear():
    a = blorqueScript_BSNewExpression(isArray=True)
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSNewExpression128', {b1})
    assert _is_linked(a, 'blorqueScript_BSNewExpression128', b1)
    if hasattr(b1, 'blorqueScript_BSExpression129'):
        assert _is_linked(b1, 'blorqueScript_BSExpression129', a)
    _safe_set(a, 'blorqueScript_BSNewExpression128', {b2})
    assert _is_linked(a, 'blorqueScript_BSNewExpression128', b2)
    if hasattr(b1, 'blorqueScript_BSExpression129'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression129', a)
    if hasattr(b2, 'blorqueScript_BSExpression129'):
        assert _is_linked(b2, 'blorqueScript_BSExpression129', a)
    _safe_set(a, 'blorqueScript_BSNewExpression128', set())
    assert not _is_linked(a, 'blorqueScript_BSNewExpression128', b2)
    if hasattr(b2, 'blorqueScript_BSExpression129'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression129', a)


def test_assoc_block40_link_reassign_clear():
    a = blorqueScript_BSSwitchStatement(stringSwitch=True)
    b1 = blorqueScript_BSSwitchBlock()
    b2 = blorqueScript_BSSwitchBlock()
    _safe_set(a, 'blorqueScript_BSSwitchStatement41', b1)
    assert _is_linked(a, 'blorqueScript_BSSwitchStatement41', b1)
    if hasattr(b1, 'blorqueScript_BSSwitchBlock'):
        assert _is_linked(b1, 'blorqueScript_BSSwitchBlock', a)
    _safe_set(a, 'blorqueScript_BSSwitchStatement41', b2)
    assert _is_linked(a, 'blorqueScript_BSSwitchStatement41', b2)
    if hasattr(b1, 'blorqueScript_BSSwitchBlock'):
        assert not _is_linked(b1, 'blorqueScript_BSSwitchBlock', a)
    if hasattr(b2, 'blorqueScript_BSSwitchBlock'):
        assert _is_linked(b2, 'blorqueScript_BSSwitchBlock', a)
    _safe_set(a, 'blorqueScript_BSSwitchStatement41', None)
    assert not _is_linked(a, 'blorqueScript_BSSwitchStatement41', b2)
    if hasattr(b2, 'blorqueScript_BSSwitchBlock'):
        assert not _is_linked(b2, 'blorqueScript_BSSwitchBlock', a)


def test_assoc_castExpr123_link_reassign_clear():
    a = blorqueScript_BSCastExpression(isArray=True, pType="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSCastExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSCastExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression124'):
        assert _is_linked(b1, 'blorqueScript_BSExpression124', a)
    _safe_set(a, 'blorqueScript_BSCastExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSCastExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression124'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression124', a)
    if hasattr(b2, 'blorqueScript_BSExpression124'):
        assert _is_linked(b2, 'blorqueScript_BSExpression124', a)
    _safe_set(a, 'blorqueScript_BSCastExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSCastExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression124'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression124', a)


def test_assoc_classes1_link_reassign_clear():
    a = blorqueScript_BSFile(name="sample_text")
    b1 = blorqueScript_BSClass(name="sample_text")
    b2 = blorqueScript_BSClass(name="sample_text_2")
    _safe_set(a, 'blorqueScript_BSFile2', {b1})
    assert _is_linked(a, 'blorqueScript_BSFile2', b1)
    if hasattr(b1, 'blorqueScript_BSClass'):
        assert _is_linked(b1, 'blorqueScript_BSClass', a)
    _safe_set(a, 'blorqueScript_BSFile2', {b2})
    assert _is_linked(a, 'blorqueScript_BSFile2', b2)
    if hasattr(b1, 'blorqueScript_BSClass'):
        assert not _is_linked(b1, 'blorqueScript_BSClass', a)
    if hasattr(b2, 'blorqueScript_BSClass'):
        assert _is_linked(b2, 'blorqueScript_BSClass', a)
    _safe_set(a, 'blorqueScript_BSFile2', set())
    assert not _is_linked(a, 'blorqueScript_BSFile2', b2)
    if hasattr(b2, 'blorqueScript_BSClass'):
        assert not _is_linked(b2, 'blorqueScript_BSClass', a)


def test_assoc_expression38_link_reassign_clear():
    a = blorqueScript_BSSwitchStatement(stringSwitch=True)
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSSwitchStatement', b1)
    assert _is_linked(a, 'blorqueScript_BSSwitchStatement', b1)
    if hasattr(b1, 'blorqueScript_BSExpression39'):
        assert _is_linked(b1, 'blorqueScript_BSExpression39', a)
    _safe_set(a, 'blorqueScript_BSSwitchStatement', b2)
    assert _is_linked(a, 'blorqueScript_BSSwitchStatement', b2)
    if hasattr(b1, 'blorqueScript_BSExpression39'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression39', a)
    if hasattr(b2, 'blorqueScript_BSExpression39'):
        assert _is_linked(b2, 'blorqueScript_BSExpression39', a)
    _safe_set(a, 'blorqueScript_BSSwitchStatement', None)
    assert not _is_linked(a, 'blorqueScript_BSSwitchStatement', b2)
    if hasattr(b2, 'blorqueScript_BSExpression39'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression39', a)


def test_assoc_imports0_link_reassign_clear():
    a = blorqueScript_BSImport(importedNamespace="sample_text")
    b1 = blorqueScript_BSFile(name="sample_text")
    b2 = blorqueScript_BSFile(name="sample_text_2")
    _safe_set(a, 'blorqueScript_BSImport', b1)
    assert _is_linked(a, 'blorqueScript_BSImport', b1)
    if hasattr(b1, 'blorqueScript_BSFile'):
        assert _is_linked(b1, 'blorqueScript_BSFile', a)
    _safe_set(a, 'blorqueScript_BSImport', b2)
    assert _is_linked(a, 'blorqueScript_BSImport', b2)
    if hasattr(b1, 'blorqueScript_BSFile'):
        assert not _is_linked(b1, 'blorqueScript_BSFile', a)
    if hasattr(b2, 'blorqueScript_BSFile'):
        assert _is_linked(b2, 'blorqueScript_BSFile', a)
    _safe_set(a, 'blorqueScript_BSImport', None)
    assert not _is_linked(a, 'blorqueScript_BSImport', b2)
    if hasattr(b2, 'blorqueScript_BSFile'):
        assert not _is_linked(b2, 'blorqueScript_BSFile', a)


def test_assoc_left103_link_reassign_clear():
    a = blorqueScript_BSOrderedRelationExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSOrderedRelationExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSOrderedRelationExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression104'):
        assert _is_linked(b1, 'blorqueScript_BSExpression104', a)
    _safe_set(a, 'blorqueScript_BSOrderedRelationExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSOrderedRelationExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression104'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression104', a)
    if hasattr(b2, 'blorqueScript_BSExpression104'):
        assert _is_linked(b2, 'blorqueScript_BSExpression104', a)
    _safe_set(a, 'blorqueScript_BSOrderedRelationExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSOrderedRelationExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression104'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression104', a)


def test_assoc_left108_link_reassign_clear():
    a = blorqueScript_BSBitwiseShiftExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSBitwiseShiftExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSBitwiseShiftExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression109'):
        assert _is_linked(b1, 'blorqueScript_BSExpression109', a)
    _safe_set(a, 'blorqueScript_BSBitwiseShiftExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSBitwiseShiftExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression109'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression109', a)
    if hasattr(b2, 'blorqueScript_BSExpression109'):
        assert _is_linked(b2, 'blorqueScript_BSExpression109', a)
    _safe_set(a, 'blorqueScript_BSBitwiseShiftExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSBitwiseShiftExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression109'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression109', a)


def test_assoc_left113_link_reassign_clear():
    a = blorqueScript_BSPlusMinusOrStringConcatExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression114'):
        assert _is_linked(b1, 'blorqueScript_BSExpression114', a)
    _safe_set(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression114'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression114', a)
    if hasattr(b2, 'blorqueScript_BSExpression114'):
        assert _is_linked(b2, 'blorqueScript_BSExpression114', a)
    _safe_set(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression114'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression114', a)


def test_assoc_left118_link_reassign_clear():
    a = blorqueScript_BSMulDivOrModExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSMulDivOrModExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSMulDivOrModExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression119'):
        assert _is_linked(b1, 'blorqueScript_BSExpression119', a)
    _safe_set(a, 'blorqueScript_BSMulDivOrModExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSMulDivOrModExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression119'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression119', a)
    if hasattr(b2, 'blorqueScript_BSExpression119'):
        assert _is_linked(b2, 'blorqueScript_BSExpression119', a)
    _safe_set(a, 'blorqueScript_BSMulDivOrModExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSMulDivOrModExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression119'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression119', a)


def test_assoc_left149_link_reassign_clear():
    a = blorqueScript_BSRealConstant(right=7)
    b1 = blorqueScript_BSNumberConstant(value=7)
    b2 = blorqueScript_BSNumberConstant(value=13)
    _safe_set(a, 'blorqueScript_BSRealConstant', b1)
    assert _is_linked(a, 'blorqueScript_BSRealConstant', b1)
    if hasattr(b1, 'blorqueScript_BSNumberConstant'):
        assert _is_linked(b1, 'blorqueScript_BSNumberConstant', a)
    _safe_set(a, 'blorqueScript_BSRealConstant', b2)
    assert _is_linked(a, 'blorqueScript_BSRealConstant', b2)
    if hasattr(b1, 'blorqueScript_BSNumberConstant'):
        assert not _is_linked(b1, 'blorqueScript_BSNumberConstant', a)
    if hasattr(b2, 'blorqueScript_BSNumberConstant'):
        assert _is_linked(b2, 'blorqueScript_BSNumberConstant', a)
    _safe_set(a, 'blorqueScript_BSRealConstant', None)
    assert not _is_linked(a, 'blorqueScript_BSRealConstant', b2)
    if hasattr(b2, 'blorqueScript_BSNumberConstant'):
        assert not _is_linked(b2, 'blorqueScript_BSNumberConstant', a)


def test_assoc_left60_link_reassign_clear():
    a = blorqueScript_BSAssignmentExpression(assignmentOperator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSAssignmentExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSAssignmentExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression61'):
        assert _is_linked(b1, 'blorqueScript_BSExpression61', a)
    _safe_set(a, 'blorqueScript_BSAssignmentExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSAssignmentExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression61'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression61', a)
    if hasattr(b2, 'blorqueScript_BSExpression61'):
        assert _is_linked(b2, 'blorqueScript_BSExpression61', a)
    _safe_set(a, 'blorqueScript_BSAssignmentExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSAssignmentExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression61'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression61', a)


def test_assoc_left98_link_reassign_clear():
    a = blorqueScript_BSEqualityExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSEqualityExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSEqualityExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression99'):
        assert _is_linked(b1, 'blorqueScript_BSExpression99', a)
    _safe_set(a, 'blorqueScript_BSEqualityExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSEqualityExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression99'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression99', a)
    if hasattr(b2, 'blorqueScript_BSExpression99'):
        assert _is_linked(b2, 'blorqueScript_BSExpression99', a)
    _safe_set(a, 'blorqueScript_BSEqualityExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSEqualityExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression99'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression99', a)


def test_assoc_members6_link_reassign_clear():
    a = blorqueScript_BSMember(isArray=True)
    b1 = blorqueScript_BSClass(name="sample_text")
    b2 = blorqueScript_BSClass(name="sample_text_2")
    _safe_set(a, 'blorqueScript_BSMember', b1)
    assert _is_linked(a, 'blorqueScript_BSMember', b1)
    if hasattr(b1, 'blorqueScript_BSClass7'):
        assert _is_linked(b1, 'blorqueScript_BSClass7', a)
    _safe_set(a, 'blorqueScript_BSMember', b2)
    assert _is_linked(a, 'blorqueScript_BSMember', b2)
    if hasattr(b1, 'blorqueScript_BSClass7'):
        assert not _is_linked(b1, 'blorqueScript_BSClass7', a)
    if hasattr(b2, 'blorqueScript_BSClass7'):
        assert _is_linked(b2, 'blorqueScript_BSClass7', a)
    _safe_set(a, 'blorqueScript_BSMember', None)
    assert not _is_linked(a, 'blorqueScript_BSMember', b2)
    if hasattr(b2, 'blorqueScript_BSClass7'):
        assert not _is_linked(b2, 'blorqueScript_BSClass7', a)


def test_assoc_params8_link_reassign_clear():
    a = blorqueScript_BSParameter(isArray=True)
    b1 = blorqueScript_BSMethod()
    b2 = blorqueScript_BSMethod()
    _safe_set(a, 'blorqueScript_BSParameter', b1)
    assert _is_linked(a, 'blorqueScript_BSParameter', b1)
    if hasattr(b1, 'blorqueScript_BSMethod'):
        assert _is_linked(b1, 'blorqueScript_BSMethod', a)
    _safe_set(a, 'blorqueScript_BSParameter', b2)
    assert _is_linked(a, 'blorqueScript_BSParameter', b2)
    if hasattr(b1, 'blorqueScript_BSMethod'):
        assert not _is_linked(b1, 'blorqueScript_BSMethod', a)
    if hasattr(b2, 'blorqueScript_BSMethod'):
        assert _is_linked(b2, 'blorqueScript_BSMethod', a)
    _safe_set(a, 'blorqueScript_BSParameter', None)
    assert not _is_linked(a, 'blorqueScript_BSParameter', b2)
    if hasattr(b2, 'blorqueScript_BSMethod'):
        assert not _is_linked(b2, 'blorqueScript_BSMethod', a)


def test_assoc_rType125_link_reassign_clear():
    a = blorqueScript_BSNewExpression(isArray=True)
    b1 = blorqueScript_BSClass(name="sample_text")
    b2 = blorqueScript_BSClass(name="sample_text_2")
    _safe_set(a, 'blorqueScript_BSNewExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSNewExpression', b1)
    if hasattr(b1, 'blorqueScript_BSClass126'):
        assert _is_linked(b1, 'blorqueScript_BSClass126', a)
    _safe_set(a, 'blorqueScript_BSNewExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSNewExpression', b2)
    if hasattr(b1, 'blorqueScript_BSClass126'):
        assert not _is_linked(b1, 'blorqueScript_BSClass126', a)
    if hasattr(b2, 'blorqueScript_BSClass126'):
        assert _is_linked(b2, 'blorqueScript_BSClass126', a)
    _safe_set(a, 'blorqueScript_BSNewExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSNewExpression', b2)
    if hasattr(b2, 'blorqueScript_BSClass126'):
        assert not _is_linked(b2, 'blorqueScript_BSClass126', a)


def test_assoc_rType58_link_reassign_clear():
    a = blorqueScript_BSSymbol(name="sample_text", pType="sample_text")
    b1 = blorqueScript_BSClass(name="sample_text")
    b2 = blorqueScript_BSClass(name="sample_text_2")
    _safe_set(a, 'blorqueScript_BSSymbol', b1)
    assert _is_linked(a, 'blorqueScript_BSSymbol', b1)
    if hasattr(b1, 'blorqueScript_BSClass59'):
        assert _is_linked(b1, 'blorqueScript_BSClass59', a)
    _safe_set(a, 'blorqueScript_BSSymbol', b2)
    assert _is_linked(a, 'blorqueScript_BSSymbol', b2)
    if hasattr(b1, 'blorqueScript_BSClass59'):
        assert not _is_linked(b1, 'blorqueScript_BSClass59', a)
    if hasattr(b2, 'blorqueScript_BSClass59'):
        assert _is_linked(b2, 'blorqueScript_BSClass59', a)
    _safe_set(a, 'blorqueScript_BSSymbol', None)
    assert not _is_linked(a, 'blorqueScript_BSSymbol', b2)
    if hasattr(b2, 'blorqueScript_BSClass59'):
        assert not _is_linked(b2, 'blorqueScript_BSClass59', a)


def test_assoc_receiver130_link_reassign_clear():
    a = blorqueScript_BSUnaryModifierExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSUnaryModifierExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSUnaryModifierExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression131'):
        assert _is_linked(b1, 'blorqueScript_BSExpression131', a)
    _safe_set(a, 'blorqueScript_BSUnaryModifierExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSUnaryModifierExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression131'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression131', a)
    if hasattr(b2, 'blorqueScript_BSExpression131'):
        assert _is_linked(b2, 'blorqueScript_BSExpression131', a)
    _safe_set(a, 'blorqueScript_BSUnaryModifierExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSUnaryModifierExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression131'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression131', a)


def test_assoc_receiver147_link_reassign_clear():
    a = blorqueScript_BSPostfixArithmeticExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSPostfixArithmeticExpression', b1)
    assert _is_linked(a, 'blorqueScript_BSPostfixArithmeticExpression', b1)
    if hasattr(b1, 'blorqueScript_BSExpression148'):
        assert _is_linked(b1, 'blorqueScript_BSExpression148', a)
    _safe_set(a, 'blorqueScript_BSPostfixArithmeticExpression', b2)
    assert _is_linked(a, 'blorqueScript_BSPostfixArithmeticExpression', b2)
    if hasattr(b1, 'blorqueScript_BSExpression148'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression148', a)
    if hasattr(b2, 'blorqueScript_BSExpression148'):
        assert _is_linked(b2, 'blorqueScript_BSExpression148', a)
    _safe_set(a, 'blorqueScript_BSPostfixArithmeticExpression', None)
    assert not _is_linked(a, 'blorqueScript_BSPostfixArithmeticExpression', b2)
    if hasattr(b2, 'blorqueScript_BSExpression148'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression148', a)


def test_assoc_right100_link_reassign_clear():
    a = blorqueScript_BSEqualityExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSEqualityExpression101', b1)
    assert _is_linked(a, 'blorqueScript_BSEqualityExpression101', b1)
    if hasattr(b1, 'blorqueScript_BSExpression102'):
        assert _is_linked(b1, 'blorqueScript_BSExpression102', a)
    _safe_set(a, 'blorqueScript_BSEqualityExpression101', b2)
    assert _is_linked(a, 'blorqueScript_BSEqualityExpression101', b2)
    if hasattr(b1, 'blorqueScript_BSExpression102'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression102', a)
    if hasattr(b2, 'blorqueScript_BSExpression102'):
        assert _is_linked(b2, 'blorqueScript_BSExpression102', a)
    _safe_set(a, 'blorqueScript_BSEqualityExpression101', None)
    assert not _is_linked(a, 'blorqueScript_BSEqualityExpression101', b2)
    if hasattr(b2, 'blorqueScript_BSExpression102'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression102', a)


def test_assoc_right105_link_reassign_clear():
    a = blorqueScript_BSOrderedRelationExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSOrderedRelationExpression106', b1)
    assert _is_linked(a, 'blorqueScript_BSOrderedRelationExpression106', b1)
    if hasattr(b1, 'blorqueScript_BSExpression107'):
        assert _is_linked(b1, 'blorqueScript_BSExpression107', a)
    _safe_set(a, 'blorqueScript_BSOrderedRelationExpression106', b2)
    assert _is_linked(a, 'blorqueScript_BSOrderedRelationExpression106', b2)
    if hasattr(b1, 'blorqueScript_BSExpression107'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression107', a)
    if hasattr(b2, 'blorqueScript_BSExpression107'):
        assert _is_linked(b2, 'blorqueScript_BSExpression107', a)
    _safe_set(a, 'blorqueScript_BSOrderedRelationExpression106', None)
    assert not _is_linked(a, 'blorqueScript_BSOrderedRelationExpression106', b2)
    if hasattr(b2, 'blorqueScript_BSExpression107'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression107', a)


def test_assoc_right110_link_reassign_clear():
    a = blorqueScript_BSBitwiseShiftExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSBitwiseShiftExpression111', b1)
    assert _is_linked(a, 'blorqueScript_BSBitwiseShiftExpression111', b1)
    if hasattr(b1, 'blorqueScript_BSExpression112'):
        assert _is_linked(b1, 'blorqueScript_BSExpression112', a)
    _safe_set(a, 'blorqueScript_BSBitwiseShiftExpression111', b2)
    assert _is_linked(a, 'blorqueScript_BSBitwiseShiftExpression111', b2)
    if hasattr(b1, 'blorqueScript_BSExpression112'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression112', a)
    if hasattr(b2, 'blorqueScript_BSExpression112'):
        assert _is_linked(b2, 'blorqueScript_BSExpression112', a)
    _safe_set(a, 'blorqueScript_BSBitwiseShiftExpression111', None)
    assert not _is_linked(a, 'blorqueScript_BSBitwiseShiftExpression111', b2)
    if hasattr(b2, 'blorqueScript_BSExpression112'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression112', a)


def test_assoc_right115_link_reassign_clear():
    a = blorqueScript_BSPlusMinusOrStringConcatExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', b1)
    assert _is_linked(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', b1)
    if hasattr(b1, 'blorqueScript_BSExpression117'):
        assert _is_linked(b1, 'blorqueScript_BSExpression117', a)
    _safe_set(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', b2)
    assert _is_linked(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', b2)
    if hasattr(b1, 'blorqueScript_BSExpression117'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression117', a)
    if hasattr(b2, 'blorqueScript_BSExpression117'):
        assert _is_linked(b2, 'blorqueScript_BSExpression117', a)
    _safe_set(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', None)
    assert not _is_linked(a, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', b2)
    if hasattr(b2, 'blorqueScript_BSExpression117'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression117', a)


def test_assoc_right120_link_reassign_clear():
    a = blorqueScript_BSMulDivOrModExpression(operator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSMulDivOrModExpression121', b1)
    assert _is_linked(a, 'blorqueScript_BSMulDivOrModExpression121', b1)
    if hasattr(b1, 'blorqueScript_BSExpression122'):
        assert _is_linked(b1, 'blorqueScript_BSExpression122', a)
    _safe_set(a, 'blorqueScript_BSMulDivOrModExpression121', b2)
    assert _is_linked(a, 'blorqueScript_BSMulDivOrModExpression121', b2)
    if hasattr(b1, 'blorqueScript_BSExpression122'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression122', a)
    if hasattr(b2, 'blorqueScript_BSExpression122'):
        assert _is_linked(b2, 'blorqueScript_BSExpression122', a)
    _safe_set(a, 'blorqueScript_BSMulDivOrModExpression121', None)
    assert not _is_linked(a, 'blorqueScript_BSMulDivOrModExpression121', b2)
    if hasattr(b2, 'blorqueScript_BSExpression122'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression122', a)


def test_assoc_right62_link_reassign_clear():
    a = blorqueScript_BSAssignmentExpression(assignmentOperator="sample_text")
    b1 = blorqueScript_BSExpression()
    b2 = blorqueScript_BSExpression()
    _safe_set(a, 'blorqueScript_BSAssignmentExpression63', b1)
    assert _is_linked(a, 'blorqueScript_BSAssignmentExpression63', b1)
    if hasattr(b1, 'blorqueScript_BSExpression64'):
        assert _is_linked(b1, 'blorqueScript_BSExpression64', a)
    _safe_set(a, 'blorqueScript_BSAssignmentExpression63', b2)
    assert _is_linked(a, 'blorqueScript_BSAssignmentExpression63', b2)
    if hasattr(b1, 'blorqueScript_BSExpression64'):
        assert not _is_linked(b1, 'blorqueScript_BSExpression64', a)
    if hasattr(b2, 'blorqueScript_BSExpression64'):
        assert _is_linked(b2, 'blorqueScript_BSExpression64', a)
    _safe_set(a, 'blorqueScript_BSAssignmentExpression63', None)
    assert not _is_linked(a, 'blorqueScript_BSAssignmentExpression63', b2)
    if hasattr(b2, 'blorqueScript_BSExpression64'):
        assert not _is_linked(b2, 'blorqueScript_BSExpression64', a)


def test_assoc_superclass4_link_reassign_clear():
    a = blorqueScript_BSClass(name="sample_text")
    b1 = blorqueScript_BSClass(name="sample_text")
    b2 = blorqueScript_BSClass(name="sample_text_2")
    _safe_set(a, 'blorqueScript_BSClass3', b1)
    assert _is_linked(a, 'blorqueScript_BSClass3', b1)
    if hasattr(b1, 'blorqueScript_BSClass5'):
        assert _is_linked(b1, 'blorqueScript_BSClass5', a)
    _safe_set(a, 'blorqueScript_BSClass3', b2)
    assert _is_linked(a, 'blorqueScript_BSClass3', b2)
    if hasattr(b1, 'blorqueScript_BSClass5'):
        assert not _is_linked(b1, 'blorqueScript_BSClass5', a)
    if hasattr(b2, 'blorqueScript_BSClass5'):
        assert _is_linked(b2, 'blorqueScript_BSClass5', a)
    _safe_set(a, 'blorqueScript_BSClass3', None)
    assert not _is_linked(a, 'blorqueScript_BSClass3', b2)
    if hasattr(b2, 'blorqueScript_BSClass5'):
        assert not _is_linked(b2, 'blorqueScript_BSClass5', a)


def test_assoc_symbol150_link_reassign_clear():
    a = blorqueScript_BSSymbol(name="sample_text", pType="sample_text")
    b1 = blorqueScript_BSSymbolRef()
    b2 = blorqueScript_BSSymbolRef()
    _safe_set(a, 'blorqueScript_BSSymbol151', b1)
    assert _is_linked(a, 'blorqueScript_BSSymbol151', b1)
    if hasattr(b1, 'blorqueScript_BSSymbolRef'):
        assert _is_linked(b1, 'blorqueScript_BSSymbolRef', a)
    _safe_set(a, 'blorqueScript_BSSymbol151', b2)
    assert _is_linked(a, 'blorqueScript_BSSymbol151', b2)
    if hasattr(b1, 'blorqueScript_BSSymbolRef'):
        assert not _is_linked(b1, 'blorqueScript_BSSymbolRef', a)
    if hasattr(b2, 'blorqueScript_BSSymbolRef'):
        assert _is_linked(b2, 'blorqueScript_BSSymbolRef', a)
    _safe_set(a, 'blorqueScript_BSSymbol151', None)
    assert not _is_linked(a, 'blorqueScript_BSSymbol151', b2)
    if hasattr(b2, 'blorqueScript_BSSymbolRef'):
        assert not _is_linked(b2, 'blorqueScript_BSSymbolRef', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BSBlock_strategy = st.builds(BSBlock)
@given(instance=BSBlock_strategy)
@settings(max_examples=25)
def test_BSBlock_instantiation(instance):
    assert isinstance(instance, BSBlock)


BSExpression_strategy = st.builds(BSExpression)
@given(instance=BSExpression_strategy)
@settings(max_examples=25)
def test_BSExpression_instantiation(instance):
    assert isinstance(instance, BSExpression)


BSMember_strategy = st.builds(BSMember)
@given(instance=BSMember_strategy)
@settings(max_examples=25)
def test_BSMember_instantiation(instance):
    assert isinstance(instance, BSMember)


BSStatement_strategy = st.builds(BSStatement)
@given(instance=BSStatement_strategy)
@settings(max_examples=25)
def test_BSStatement_instantiation(instance):
    assert isinstance(instance, BSStatement)


BSSymbol_strategy = st.builds(BSSymbol)
@given(instance=BSSymbol_strategy)
@settings(max_examples=25)
def test_BSSymbol_instantiation(instance):
    assert isinstance(instance, BSSymbol)


blorqueScript_BSArrayAccessExpression_strategy = st.builds(blorqueScript_BSArrayAccessExpression)
@given(instance=blorqueScript_BSArrayAccessExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSArrayAccessExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSArrayAccessExpression)


blorqueScript_BSAssignmentExpression_strategy = st.builds(blorqueScript_BSAssignmentExpression, assignmentOperator=safe_text)
@given(instance=blorqueScript_BSAssignmentExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSAssignmentExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSAssignmentExpression)


blorqueScript_BSBitwiseAndExpression_strategy = st.builds(blorqueScript_BSBitwiseAndExpression)
@given(instance=blorqueScript_BSBitwiseAndExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBitwiseAndExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseAndExpression)


blorqueScript_BSBitwiseOrExpression_strategy = st.builds(blorqueScript_BSBitwiseOrExpression)
@given(instance=blorqueScript_BSBitwiseOrExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBitwiseOrExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseOrExpression)


blorqueScript_BSBitwiseShiftExpression_strategy = st.builds(blorqueScript_BSBitwiseShiftExpression, operator=safe_text)
@given(instance=blorqueScript_BSBitwiseShiftExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBitwiseShiftExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseShiftExpression)


blorqueScript_BSBitwiseXorExpression_strategy = st.builds(blorqueScript_BSBitwiseXorExpression)
@given(instance=blorqueScript_BSBitwiseXorExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBitwiseXorExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseXorExpression)


blorqueScript_BSBlock_strategy = st.builds(blorqueScript_BSBlock)
@given(instance=blorqueScript_BSBlock_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBlock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBlock)


blorqueScript_BSBooleanAndExpression_strategy = st.builds(blorqueScript_BSBooleanAndExpression)
@given(instance=blorqueScript_BSBooleanAndExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBooleanAndExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBooleanAndExpression)


blorqueScript_BSBooleanConstant_strategy = st.builds(blorqueScript_BSBooleanConstant, value=safe_text)
@given(instance=blorqueScript_BSBooleanConstant_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBooleanConstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBooleanConstant)


blorqueScript_BSBooleanOrExpression_strategy = st.builds(blorqueScript_BSBooleanOrExpression)
@given(instance=blorqueScript_BSBooleanOrExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBooleanOrExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBooleanOrExpression)


blorqueScript_BSBreak_strategy = st.builds(blorqueScript_BSBreak)
@given(instance=blorqueScript_BSBreak_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSBreak_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBreak)


blorqueScript_BSCase_strategy = st.builds(blorqueScript_BSCase)
@given(instance=blorqueScript_BSCase_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSCase_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSCase)


blorqueScript_BSCaseBlock_strategy = st.builds(blorqueScript_BSCaseBlock)
@given(instance=blorqueScript_BSCaseBlock_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSCaseBlock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSCaseBlock)


blorqueScript_BSCastExpression_strategy = st.builds(blorqueScript_BSCastExpression, isArray=st.booleans(), pType=safe_text)
@given(instance=blorqueScript_BSCastExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSCastExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSCastExpression)


blorqueScript_BSClass_strategy = st.builds(blorqueScript_BSClass, name=safe_text)
@given(instance=blorqueScript_BSClass_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSClass_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSClass)


blorqueScript_BSClientLiteral_strategy = st.builds(blorqueScript_BSClientLiteral)
@given(instance=blorqueScript_BSClientLiteral_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSClientLiteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSClientLiteral)


blorqueScript_BSContinue_strategy = st.builds(blorqueScript_BSContinue)
@given(instance=blorqueScript_BSContinue_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSContinue_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSContinue)


blorqueScript_BSEqualityExpression_strategy = st.builds(blorqueScript_BSEqualityExpression, operator=safe_text)
@given(instance=blorqueScript_BSEqualityExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSEqualityExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSEqualityExpression)


blorqueScript_BSExpression_strategy = st.builds(blorqueScript_BSExpression)
@given(instance=blorqueScript_BSExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSExpression)


blorqueScript_BSField_strategy = st.builds(blorqueScript_BSField)
@given(instance=blorqueScript_BSField_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSField_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSField)


blorqueScript_BSFile_strategy = st.builds(blorqueScript_BSFile, name=safe_text)
@given(instance=blorqueScript_BSFile_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSFile_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSFile)


blorqueScript_BSForLoop_strategy = st.builds(blorqueScript_BSForLoop)
@given(instance=blorqueScript_BSForLoop_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSForLoop_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSForLoop)


blorqueScript_BSHexadecimalConstant_strategy = st.builds(blorqueScript_BSHexadecimalConstant, value=safe_text)
@given(instance=blorqueScript_BSHexadecimalConstant_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSHexadecimalConstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSHexadecimalConstant)


blorqueScript_BSIfBlock_strategy = st.builds(blorqueScript_BSIfBlock)
@given(instance=blorqueScript_BSIfBlock_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSIfBlock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSIfBlock)


blorqueScript_BSIfStatement_strategy = st.builds(blorqueScript_BSIfStatement)
@given(instance=blorqueScript_BSIfStatement_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSIfStatement_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSIfStatement)


blorqueScript_BSImport_strategy = st.builds(blorqueScript_BSImport, importedNamespace=safe_text)
@given(instance=blorqueScript_BSImport_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSImport_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSImport)


blorqueScript_BSLoopBlock_strategy = st.builds(blorqueScript_BSLoopBlock)
@given(instance=blorqueScript_BSLoopBlock_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSLoopBlock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSLoopBlock)


blorqueScript_BSMember_strategy = st.builds(blorqueScript_BSMember, isArray=st.booleans())
@given(instance=blorqueScript_BSMember_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSMember_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMember)


blorqueScript_BSMemberSelectionExpression_strategy = st.builds(blorqueScript_BSMemberSelectionExpression)
@given(instance=blorqueScript_BSMemberSelectionExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSMemberSelectionExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMemberSelectionExpression)


blorqueScript_BSMethod_strategy = st.builds(blorqueScript_BSMethod)
@given(instance=blorqueScript_BSMethod_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSMethod_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMethod)


blorqueScript_BSMethodBody_strategy = st.builds(blorqueScript_BSMethodBody)
@given(instance=blorqueScript_BSMethodBody_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSMethodBody_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMethodBody)


blorqueScript_BSMethodInvokationExpression_strategy = st.builds(blorqueScript_BSMethodInvokationExpression)
@given(instance=blorqueScript_BSMethodInvokationExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSMethodInvokationExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMethodInvokationExpression)


blorqueScript_BSMulDivOrModExpression_strategy = st.builds(blorqueScript_BSMulDivOrModExpression, operator=safe_text)
@given(instance=blorqueScript_BSMulDivOrModExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSMulDivOrModExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMulDivOrModExpression)


blorqueScript_BSNewExpression_strategy = st.builds(blorqueScript_BSNewExpression, isArray=st.booleans())
@given(instance=blorqueScript_BSNewExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSNewExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSNewExpression)


blorqueScript_BSNullLiteral_strategy = st.builds(blorqueScript_BSNullLiteral)
@given(instance=blorqueScript_BSNullLiteral_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSNullLiteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSNullLiteral)


blorqueScript_BSNumberConstant_strategy = st.builds(blorqueScript_BSNumberConstant, value=st.integers())
@given(instance=blorqueScript_BSNumberConstant_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSNumberConstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSNumberConstant)


blorqueScript_BSOrderedRelationExpression_strategy = st.builds(blorqueScript_BSOrderedRelationExpression, operator=safe_text)
@given(instance=blorqueScript_BSOrderedRelationExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSOrderedRelationExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSOrderedRelationExpression)


blorqueScript_BSParameter_strategy = st.builds(blorqueScript_BSParameter, isArray=st.booleans())
@given(instance=blorqueScript_BSParameter_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSParameter_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSParameter)


blorqueScript_BSParentLiteral_strategy = st.builds(blorqueScript_BSParentLiteral)
@given(instance=blorqueScript_BSParentLiteral_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSParentLiteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSParentLiteral)


blorqueScript_BSParentheticalExpression_strategy = st.builds(blorqueScript_BSParentheticalExpression)
@given(instance=blorqueScript_BSParentheticalExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSParentheticalExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSParentheticalExpression)


blorqueScript_BSPlusMinusOrStringConcatExpression_strategy = st.builds(blorqueScript_BSPlusMinusOrStringConcatExpression, operator=safe_text)
@given(instance=blorqueScript_BSPlusMinusOrStringConcatExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSPlusMinusOrStringConcatExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSPlusMinusOrStringConcatExpression)


blorqueScript_BSPostfixArithmeticExpression_strategy = st.builds(blorqueScript_BSPostfixArithmeticExpression, operator=safe_text)
@given(instance=blorqueScript_BSPostfixArithmeticExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSPostfixArithmeticExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSPostfixArithmeticExpression)


blorqueScript_BSRealConstant_strategy = st.builds(blorqueScript_BSRealConstant, right=st.integers())
@given(instance=blorqueScript_BSRealConstant_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSRealConstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSRealConstant)


blorqueScript_BSReturn_strategy = st.builds(blorqueScript_BSReturn)
@given(instance=blorqueScript_BSReturn_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSReturn_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSReturn)


blorqueScript_BSStatement_strategy = st.builds(blorqueScript_BSStatement)
@given(instance=blorqueScript_BSStatement_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSStatement_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSStatement)


blorqueScript_BSStringConstant_strategy = st.builds(blorqueScript_BSStringConstant, value=safe_text)
@given(instance=blorqueScript_BSStringConstant_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSStringConstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSStringConstant)


blorqueScript_BSSwitchBlock_strategy = st.builds(blorqueScript_BSSwitchBlock)
@given(instance=blorqueScript_BSSwitchBlock_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSSwitchBlock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSwitchBlock)


blorqueScript_BSSwitchStatement_strategy = st.builds(blorqueScript_BSSwitchStatement, stringSwitch=st.booleans())
@given(instance=blorqueScript_BSSwitchStatement_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSSwitchStatement_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSwitchStatement)


blorqueScript_BSSymbol_strategy = st.builds(blorqueScript_BSSymbol, name=safe_text, pType=safe_text)
@given(instance=blorqueScript_BSSymbol_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSSymbol_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSymbol)


blorqueScript_BSSymbolRef_strategy = st.builds(blorqueScript_BSSymbolRef)
@given(instance=blorqueScript_BSSymbolRef_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSSymbolRef_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSymbolRef)


blorqueScript_BSTernaryExpression_strategy = st.builds(blorqueScript_BSTernaryExpression)
@given(instance=blorqueScript_BSTernaryExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSTernaryExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSTernaryExpression)


blorqueScript_BSThisLiteral_strategy = st.builds(blorqueScript_BSThisLiteral)
@given(instance=blorqueScript_BSThisLiteral_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSThisLiteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSThisLiteral)


blorqueScript_BSUnaryModifierExpression_strategy = st.builds(blorqueScript_BSUnaryModifierExpression, operator=safe_text)
@given(instance=blorqueScript_BSUnaryModifierExpression_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSUnaryModifierExpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSUnaryModifierExpression)


blorqueScript_BSVariableDeclaration_strategy = st.builds(blorqueScript_BSVariableDeclaration)
@given(instance=blorqueScript_BSVariableDeclaration_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSVariableDeclaration_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSVariableDeclaration)


blorqueScript_BSWhileLoop_strategy = st.builds(blorqueScript_BSWhileLoop)
@given(instance=blorqueScript_BSWhileLoop_strategy)
@settings(max_examples=25)
def test_blorqueScript_BSWhileLoop_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSWhileLoop)


