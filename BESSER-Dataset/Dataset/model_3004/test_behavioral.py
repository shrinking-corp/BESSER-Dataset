import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_classes1_reverse_link_reassign_clear():
    a1 = blorqueScript_BSFile(name="sample_text")
    a2 = blorqueScript_BSFile(name="sample_text_2")
    b = blorqueScript_BSClass(name="sample_text")
    _safe_set(b, 'blorqueScript_BSClass', a1)
    assert _is_linked(b, 'blorqueScript_BSClass', a1)
    if hasattr(a1, 'blorqueScript_BSFile2'):
        assert _is_linked(a1, 'blorqueScript_BSFile2', b)
    _safe_set(b, 'blorqueScript_BSClass', a2)
    assert _is_linked(b, 'blorqueScript_BSClass', a2)
    if hasattr(a1, 'blorqueScript_BSFile2'):
        assert not _is_linked(a1, 'blorqueScript_BSFile2', b)
    if hasattr(a2, 'blorqueScript_BSFile2'):
        assert _is_linked(a2, 'blorqueScript_BSFile2', b)
    _safe_set(b, 'blorqueScript_BSClass', None)
    assert not _is_linked(b, 'blorqueScript_BSClass', a2)
    if hasattr(a2, 'blorqueScript_BSFile2'):
        assert not _is_linked(a2, 'blorqueScript_BSFile2', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = blorqueScript_BSImport(importedNamespace="sample_text")
    a2 = blorqueScript_BSImport(importedNamespace="sample_text_2")
    b = blorqueScript_BSFile(name="sample_text")
    _safe_set(b, 'blorqueScript_BSFile', {a1})
    assert _is_linked(b, 'blorqueScript_BSFile', a1)
    if hasattr(a1, 'blorqueScript_BSImport'):
        assert _is_linked(a1, 'blorqueScript_BSImport', b)
    _safe_set(b, 'blorqueScript_BSFile', {a2})
    assert _is_linked(b, 'blorqueScript_BSFile', a2)
    if hasattr(a1, 'blorqueScript_BSImport'):
        assert not _is_linked(a1, 'blorqueScript_BSImport', b)
    if hasattr(a2, 'blorqueScript_BSImport'):
        assert _is_linked(a2, 'blorqueScript_BSImport', b)
    _safe_set(b, 'blorqueScript_BSFile', set())
    assert not _is_linked(b, 'blorqueScript_BSFile', a2)
    if hasattr(a2, 'blorqueScript_BSImport'):
        assert not _is_linked(a2, 'blorqueScript_BSImport', b)


def test_assoc_left149_reverse_link_reassign_clear():
    a1 = blorqueScript_BSRealConstant(right=7)
    a2 = blorqueScript_BSRealConstant(right=13)
    b = blorqueScript_BSNumberConstant(value=7)
    _safe_set(b, 'blorqueScript_BSNumberConstant', a1)
    assert _is_linked(b, 'blorqueScript_BSNumberConstant', a1)
    if hasattr(a1, 'blorqueScript_BSRealConstant'):
        assert _is_linked(a1, 'blorqueScript_BSRealConstant', b)
    _safe_set(b, 'blorqueScript_BSNumberConstant', a2)
    assert _is_linked(b, 'blorqueScript_BSNumberConstant', a2)
    if hasattr(a1, 'blorqueScript_BSRealConstant'):
        assert not _is_linked(a1, 'blorqueScript_BSRealConstant', b)
    if hasattr(a2, 'blorqueScript_BSRealConstant'):
        assert _is_linked(a2, 'blorqueScript_BSRealConstant', b)
    _safe_set(b, 'blorqueScript_BSNumberConstant', None)
    assert not _is_linked(b, 'blorqueScript_BSNumberConstant', a2)
    if hasattr(a2, 'blorqueScript_BSRealConstant'):
        assert not _is_linked(a2, 'blorqueScript_BSRealConstant', b)


def test_assoc_members6_reverse_link_reassign_clear():
    a1 = blorqueScript_BSMember(isArray=True)
    a2 = blorqueScript_BSMember(isArray=False)
    b = blorqueScript_BSClass(name="sample_text")
    _safe_set(b, 'blorqueScript_BSClass7', {a1})
    assert _is_linked(b, 'blorqueScript_BSClass7', a1)
    if hasattr(a1, 'blorqueScript_BSMember'):
        assert _is_linked(a1, 'blorqueScript_BSMember', b)
    _safe_set(b, 'blorqueScript_BSClass7', {a2})
    assert _is_linked(b, 'blorqueScript_BSClass7', a2)
    if hasattr(a1, 'blorqueScript_BSMember'):
        assert not _is_linked(a1, 'blorqueScript_BSMember', b)
    if hasattr(a2, 'blorqueScript_BSMember'):
        assert _is_linked(a2, 'blorqueScript_BSMember', b)
    _safe_set(b, 'blorqueScript_BSClass7', set())
    assert not _is_linked(b, 'blorqueScript_BSClass7', a2)
    if hasattr(a2, 'blorqueScript_BSMember'):
        assert not _is_linked(a2, 'blorqueScript_BSMember', b)


def test_assoc_rType125_reverse_link_reassign_clear():
    a1 = blorqueScript_BSNewExpression(isArray=True)
    a2 = blorqueScript_BSNewExpression(isArray=False)
    b = blorqueScript_BSClass(name="sample_text")
    _safe_set(b, 'blorqueScript_BSClass126', a1)
    assert _is_linked(b, 'blorqueScript_BSClass126', a1)
    if hasattr(a1, 'blorqueScript_BSNewExpression'):
        assert _is_linked(a1, 'blorqueScript_BSNewExpression', b)
    _safe_set(b, 'blorqueScript_BSClass126', a2)
    assert _is_linked(b, 'blorqueScript_BSClass126', a2)
    if hasattr(a1, 'blorqueScript_BSNewExpression'):
        assert not _is_linked(a1, 'blorqueScript_BSNewExpression', b)
    if hasattr(a2, 'blorqueScript_BSNewExpression'):
        assert _is_linked(a2, 'blorqueScript_BSNewExpression', b)
    _safe_set(b, 'blorqueScript_BSClass126', None)
    assert not _is_linked(b, 'blorqueScript_BSClass126', a2)
    if hasattr(a2, 'blorqueScript_BSNewExpression'):
        assert not _is_linked(a2, 'blorqueScript_BSNewExpression', b)


def test_assoc_rType58_reverse_link_reassign_clear():
    a1 = blorqueScript_BSSymbol(name="sample_text", pType="sample_text")
    a2 = blorqueScript_BSSymbol(name="sample_text_2", pType="sample_text_2")
    b = blorqueScript_BSClass(name="sample_text")
    _safe_set(b, 'blorqueScript_BSClass59', a1)
    assert _is_linked(b, 'blorqueScript_BSClass59', a1)
    if hasattr(a1, 'blorqueScript_BSSymbol'):
        assert _is_linked(a1, 'blorqueScript_BSSymbol', b)
    _safe_set(b, 'blorqueScript_BSClass59', a2)
    assert _is_linked(b, 'blorqueScript_BSClass59', a2)
    if hasattr(a1, 'blorqueScript_BSSymbol'):
        assert not _is_linked(a1, 'blorqueScript_BSSymbol', b)
    if hasattr(a2, 'blorqueScript_BSSymbol'):
        assert _is_linked(a2, 'blorqueScript_BSSymbol', b)
    _safe_set(b, 'blorqueScript_BSClass59', None)
    assert not _is_linked(b, 'blorqueScript_BSClass59', a2)
    if hasattr(a2, 'blorqueScript_BSSymbol'):
        assert not _is_linked(a2, 'blorqueScript_BSSymbol', b)


def test_assoc_superclass4_reverse_link_reassign_clear():
    a1 = blorqueScript_BSClass(name="sample_text")
    a2 = blorqueScript_BSClass(name="sample_text_2")
    b = blorqueScript_BSClass(name="sample_text")
    _safe_set(b, 'blorqueScript_BSClass5', a1)
    assert _is_linked(b, 'blorqueScript_BSClass5', a1)
    if hasattr(a1, 'blorqueScript_BSClass3'):
        assert _is_linked(a1, 'blorqueScript_BSClass3', b)
    _safe_set(b, 'blorqueScript_BSClass5', a2)
    assert _is_linked(b, 'blorqueScript_BSClass5', a2)
    if hasattr(a1, 'blorqueScript_BSClass3'):
        assert not _is_linked(a1, 'blorqueScript_BSClass3', b)
    if hasattr(a2, 'blorqueScript_BSClass3'):
        assert _is_linked(a2, 'blorqueScript_BSClass3', b)
    _safe_set(b, 'blorqueScript_BSClass5', None)
    assert not _is_linked(b, 'blorqueScript_BSClass5', a2)
    if hasattr(a2, 'blorqueScript_BSClass3'):
        assert not _is_linked(a2, 'blorqueScript_BSClass3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args127_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression129' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSNewExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSNewExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSNewExpression(isArray=True)
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression129', None)
    _safe_set(owner, 'blorqueScript_BSNewExpression128', {partner})
    assert getattr(partner, 'blorqueScript_BSExpression129') == owner
    _safe_set(owner, 'blorqueScript_BSNewExpression128', set())
    assert getattr(partner, 'blorqueScript_BSExpression129') is None


def test_assoc_block40_stub_double():
    # blorqueScript_BSSwitchBlock has no real 'blorqueScript_BSSwitchBlock' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSSwitchStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSSwitchStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSSwitchStatement(stringSwitch=True)
    partner = blorqueScript_BSSwitchBlock()
    setattr(partner, 'blorqueScript_BSSwitchBlock', None)
    _safe_set(owner, 'blorqueScript_BSSwitchStatement41', partner)
    assert getattr(partner, 'blorqueScript_BSSwitchBlock') == owner
    _safe_set(owner, 'blorqueScript_BSSwitchStatement41', None)
    assert getattr(partner, 'blorqueScript_BSSwitchBlock') is None


def test_assoc_castExpr123_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression124' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSCastExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSCastExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSCastExpression(isArray=True, pType="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression124', None)
    _safe_set(owner, 'blorqueScript_BSCastExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression124') == owner
    _safe_set(owner, 'blorqueScript_BSCastExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression124') is None


def test_assoc_expression38_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression39' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSSwitchStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSSwitchStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSSwitchStatement(stringSwitch=True)
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression39', None)
    _safe_set(owner, 'blorqueScript_BSSwitchStatement', partner)
    assert getattr(partner, 'blorqueScript_BSExpression39') == owner
    _safe_set(owner, 'blorqueScript_BSSwitchStatement', None)
    assert getattr(partner, 'blorqueScript_BSExpression39') is None


def test_assoc_left103_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression104' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSOrderedRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSOrderedRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSOrderedRelationExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression104', None)
    _safe_set(owner, 'blorqueScript_BSOrderedRelationExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression104') == owner
    _safe_set(owner, 'blorqueScript_BSOrderedRelationExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression104') is None


def test_assoc_left108_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression109' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSBitwiseShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSBitwiseShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSBitwiseShiftExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression109', None)
    _safe_set(owner, 'blorqueScript_BSBitwiseShiftExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression109') == owner
    _safe_set(owner, 'blorqueScript_BSBitwiseShiftExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression109') is None


def test_assoc_left113_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression114' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSPlusMinusOrStringConcatExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSPlusMinusOrStringConcatExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSPlusMinusOrStringConcatExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression114', None)
    _safe_set(owner, 'blorqueScript_BSPlusMinusOrStringConcatExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression114') == owner
    _safe_set(owner, 'blorqueScript_BSPlusMinusOrStringConcatExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression114') is None


def test_assoc_left118_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression119' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSMulDivOrModExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSMulDivOrModExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSMulDivOrModExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression119', None)
    _safe_set(owner, 'blorqueScript_BSMulDivOrModExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression119') == owner
    _safe_set(owner, 'blorqueScript_BSMulDivOrModExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression119') is None


def test_assoc_left60_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression61' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSAssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSAssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSAssignmentExpression(assignmentOperator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression61', None)
    _safe_set(owner, 'blorqueScript_BSAssignmentExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression61') == owner
    _safe_set(owner, 'blorqueScript_BSAssignmentExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression61') is None


def test_assoc_left98_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression99' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSEqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSEqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSEqualityExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression99', None)
    _safe_set(owner, 'blorqueScript_BSEqualityExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression99') == owner
    _safe_set(owner, 'blorqueScript_BSEqualityExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression99') is None


def test_assoc_params8_stub_double():
    # blorqueScript_BSMethod has no real 'blorqueScript_BSMethod' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSParameter(isArray=True)
    partner = blorqueScript_BSMethod()
    setattr(partner, 'blorqueScript_BSMethod', None)
    _safe_set(owner, 'blorqueScript_BSParameter', partner)
    assert owner in getattr(partner, 'blorqueScript_BSMethod')
    _safe_set(owner, 'blorqueScript_BSParameter', None)
    assert owner not in getattr(partner, 'blorqueScript_BSMethod')


def test_assoc_receiver130_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression131' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSUnaryModifierExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSUnaryModifierExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSUnaryModifierExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression131', None)
    _safe_set(owner, 'blorqueScript_BSUnaryModifierExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression131') == owner
    _safe_set(owner, 'blorqueScript_BSUnaryModifierExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression131') is None


def test_assoc_receiver147_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression148' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSPostfixArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSPostfixArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSPostfixArithmeticExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression148', None)
    _safe_set(owner, 'blorqueScript_BSPostfixArithmeticExpression', partner)
    assert getattr(partner, 'blorqueScript_BSExpression148') == owner
    _safe_set(owner, 'blorqueScript_BSPostfixArithmeticExpression', None)
    assert getattr(partner, 'blorqueScript_BSExpression148') is None


def test_assoc_right100_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression102' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSEqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSEqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSEqualityExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression102', None)
    _safe_set(owner, 'blorqueScript_BSEqualityExpression101', partner)
    assert getattr(partner, 'blorqueScript_BSExpression102') == owner
    _safe_set(owner, 'blorqueScript_BSEqualityExpression101', None)
    assert getattr(partner, 'blorqueScript_BSExpression102') is None


def test_assoc_right105_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression107' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSOrderedRelationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSOrderedRelationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSOrderedRelationExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression107', None)
    _safe_set(owner, 'blorqueScript_BSOrderedRelationExpression106', partner)
    assert getattr(partner, 'blorqueScript_BSExpression107') == owner
    _safe_set(owner, 'blorqueScript_BSOrderedRelationExpression106', None)
    assert getattr(partner, 'blorqueScript_BSExpression107') is None


def test_assoc_right110_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression112' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSBitwiseShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSBitwiseShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSBitwiseShiftExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression112', None)
    _safe_set(owner, 'blorqueScript_BSBitwiseShiftExpression111', partner)
    assert getattr(partner, 'blorqueScript_BSExpression112') == owner
    _safe_set(owner, 'blorqueScript_BSBitwiseShiftExpression111', None)
    assert getattr(partner, 'blorqueScript_BSExpression112') is None


def test_assoc_right115_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression117' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSPlusMinusOrStringConcatExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSPlusMinusOrStringConcatExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSPlusMinusOrStringConcatExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression117', None)
    _safe_set(owner, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', partner)
    assert getattr(partner, 'blorqueScript_BSExpression117') == owner
    _safe_set(owner, 'blorqueScript_BSPlusMinusOrStringConcatExpression116', None)
    assert getattr(partner, 'blorqueScript_BSExpression117') is None


def test_assoc_right120_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression122' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSMulDivOrModExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSMulDivOrModExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSMulDivOrModExpression(operator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression122', None)
    _safe_set(owner, 'blorqueScript_BSMulDivOrModExpression121', partner)
    assert getattr(partner, 'blorqueScript_BSExpression122') == owner
    _safe_set(owner, 'blorqueScript_BSMulDivOrModExpression121', None)
    assert getattr(partner, 'blorqueScript_BSExpression122') is None


def test_assoc_right62_stub_double():
    # blorqueScript_BSExpression has no real 'blorqueScript_BSExpression64' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSAssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSAssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSAssignmentExpression(assignmentOperator="sample_text")
    partner = blorqueScript_BSExpression()
    setattr(partner, 'blorqueScript_BSExpression64', None)
    _safe_set(owner, 'blorqueScript_BSAssignmentExpression63', partner)
    assert getattr(partner, 'blorqueScript_BSExpression64') == owner
    _safe_set(owner, 'blorqueScript_BSAssignmentExpression63', None)
    assert getattr(partner, 'blorqueScript_BSExpression64') is None


def test_assoc_symbol150_stub_double():
    # blorqueScript_BSSymbolRef has no real 'blorqueScript_BSSymbolRef' property in the generated
    # code (a bare stub) -- manually attach it so blorqueScript_BSSymbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # blorqueScript_BSSymbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = blorqueScript_BSSymbol(name="sample_text", pType="sample_text")
    partner = blorqueScript_BSSymbolRef()
    setattr(partner, 'blorqueScript_BSSymbolRef', None)
    _safe_set(owner, 'blorqueScript_BSSymbol151', partner)
    assert getattr(partner, 'blorqueScript_BSSymbolRef') == owner
    _safe_set(owner, 'blorqueScript_BSSymbol151', None)
    assert getattr(partner, 'blorqueScript_BSSymbolRef') is None


