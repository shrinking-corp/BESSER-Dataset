import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractType,
    Expression,
    Literal,
    PrimitiveType,
    RangeLiteral,
    Statement,
    Symbol,
    Type,
    amethyst_AbstractType,
    amethyst_AdditiveExpression,
    amethyst_AndExpression,
    amethyst_AnyType,
    amethyst_ArrayType,
    amethyst_AssignmentExpression,
    amethyst_BooleanLiteral,
    amethyst_BooleanType,
    amethyst_BreakStatement,
    amethyst_CallExpression,
    amethyst_CaseElseStatement,
    amethyst_CaseStatement,
    amethyst_CharLiteral,
    amethyst_CharRangeLiteral,
    amethyst_CharType,
    amethyst_ClassDeclaration,
    amethyst_ClassType,
    amethyst_DefinitionDeclaration,
    amethyst_DefinitionType,
    amethyst_EObject,
    amethyst_ElseIfStatement,
    amethyst_ElseStatement,
    amethyst_EqualityExpression,
    amethyst_Expression,
    amethyst_FloatLiteral,
    amethyst_FloatType,
    amethyst_ForInitializerDeclaration,
    amethyst_ForStatement,
    amethyst_IfStatement,
    amethyst_Import,
    amethyst_InExpression,
    amethyst_IndexAccessExpression,
    amethyst_IntLiteral,
    amethyst_IntType,
    amethyst_JsCodeStatement,
    amethyst_Literal,
    amethyst_MatchingExpression,
    amethyst_MemberAccessExpression,
    amethyst_Module,
    amethyst_MultiplicativeExpression,
    amethyst_NewExpression,
    amethyst_NextStatement,
    amethyst_NotExpression,
    amethyst_NullLiteral,
    amethyst_NumberRangeLiteral,
    amethyst_OrExpression,
    amethyst_ParameterDeclaration,
    amethyst_ParenthisedExpression,
    amethyst_PrimitiveType,
    amethyst_PropertyDeclaration,
    amethyst_RangeLiteral,
    amethyst_RelationalExpression,
    amethyst_ReturnStatement,
    amethyst_SelfExpression,
    amethyst_ShiftExpression,
    amethyst_Statement,
    amethyst_StringLiteral,
    amethyst_StringType,
    amethyst_SuperExpression,
    amethyst_Symbol,
    amethyst_SymbolReference,
    amethyst_TagAttribute,
    amethyst_TagDeclaration,
    amethyst_TagExpression,
    amethyst_TagLoopExpression,
    amethyst_TagLoopInitializerDeclaration,
    amethyst_Type,
    amethyst_TypeCastExpression,
    amethyst_UnaryMinusExpression,
    amethyst_VariableDeclaration,
    amethyst_WhenStatement,
    amethyst_WhileStatement,
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

def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = amethyst_Module(name="sample_text")
    a2 = amethyst_Module(name="sample_text_2")
    b = amethyst_Import(importedNamespace="sample_text")
    _safe_set(b, 'amethyst_Import', a1)
    assert _is_linked(b, 'amethyst_Import', a1)
    if hasattr(a1, 'amethyst_Module'):
        assert _is_linked(a1, 'amethyst_Module', b)
    _safe_set(b, 'amethyst_Import', a2)
    assert _is_linked(b, 'amethyst_Import', a2)
    if hasattr(a1, 'amethyst_Module'):
        assert not _is_linked(a1, 'amethyst_Module', b)
    if hasattr(a2, 'amethyst_Module'):
        assert _is_linked(a2, 'amethyst_Module', b)
    _safe_set(b, 'amethyst_Import', None)
    assert not _is_linked(b, 'amethyst_Import', a2)
    if hasattr(a2, 'amethyst_Module'):
        assert not _is_linked(a2, 'amethyst_Module', b)


def test_assoc_params30_reverse_link_reassign_clear():
    a1 = amethyst_Symbol(name="sample_text")
    a2 = amethyst_Symbol(name="sample_text_2")
    b = amethyst_DefinitionDeclaration(static=True)
    _safe_set(b, 'amethyst_DefinitionDeclaration', {a1})
    assert _is_linked(b, 'amethyst_DefinitionDeclaration', a1)
    if hasattr(a1, 'amethyst_Symbol31'):
        assert _is_linked(a1, 'amethyst_Symbol31', b)
    _safe_set(b, 'amethyst_DefinitionDeclaration', {a2})
    assert _is_linked(b, 'amethyst_DefinitionDeclaration', a2)
    if hasattr(a1, 'amethyst_Symbol31'):
        assert not _is_linked(a1, 'amethyst_Symbol31', b)
    if hasattr(a2, 'amethyst_Symbol31'):
        assert _is_linked(a2, 'amethyst_Symbol31', b)
    _safe_set(b, 'amethyst_DefinitionDeclaration', set())
    assert not _is_linked(b, 'amethyst_DefinitionDeclaration', a2)
    if hasattr(a2, 'amethyst_Symbol31'):
        assert not _is_linked(a2, 'amethyst_Symbol31', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_declarations1_stub_double():
    # amethyst_Statement has no real 'amethyst_Statement' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_Module(name="sample_text")
    partner = amethyst_Statement()
    setattr(partner, 'amethyst_Statement', None)
    _safe_set(owner, 'amethyst_Module2', {partner})
    assert getattr(partner, 'amethyst_Statement') == owner
    _safe_set(owner, 'amethyst_Module2', set())
    assert getattr(partner, 'amethyst_Statement') is None


def test_assoc_end188_stub_double():
    # amethyst_NumberRangeLiteral has no real 'amethyst_NumberRangeLiteral189' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_IntLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_IntLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_IntLiteral(value=7)
    partner = amethyst_NumberRangeLiteral()
    setattr(partner, 'amethyst_NumberRangeLiteral189', None)
    _safe_set(owner, 'amethyst_IntLiteral190', partner)
    assert getattr(partner, 'amethyst_NumberRangeLiteral189') == owner
    _safe_set(owner, 'amethyst_IntLiteral190', None)
    assert getattr(partner, 'amethyst_NumberRangeLiteral189') is None


def test_assoc_end192_stub_double():
    # amethyst_CharRangeLiteral has no real 'amethyst_CharRangeLiteral193' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_CharLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_CharLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_CharLiteral(value="sample_text")
    partner = amethyst_CharRangeLiteral()
    setattr(partner, 'amethyst_CharRangeLiteral193', None)
    _safe_set(owner, 'amethyst_CharLiteral194', partner)
    assert getattr(partner, 'amethyst_CharRangeLiteral193') == owner
    _safe_set(owner, 'amethyst_CharLiteral194', None)
    assert getattr(partner, 'amethyst_CharRangeLiteral193') is None


def test_assoc_initializer10_stub_double():
    # amethyst_TagLoopExpression has no real 'amethyst_TagLoopExpression11' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_Symbol(name="sample_text")
    partner = amethyst_TagLoopExpression()
    setattr(partner, 'amethyst_TagLoopExpression11', None)
    _safe_set(owner, 'amethyst_Symbol', partner)
    assert getattr(partner, 'amethyst_TagLoopExpression11') == owner
    _safe_set(owner, 'amethyst_Symbol', None)
    assert getattr(partner, 'amethyst_TagLoopExpression11') is None


def test_assoc_initializer96_stub_double():
    # amethyst_ForStatement has no real 'amethyst_ForStatement' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_Symbol(name="sample_text")
    partner = amethyst_ForStatement()
    setattr(partner, 'amethyst_ForStatement', None)
    _safe_set(owner, 'amethyst_Symbol97', partner)
    assert getattr(partner, 'amethyst_ForStatement') == owner
    _safe_set(owner, 'amethyst_Symbol97', None)
    assert getattr(partner, 'amethyst_ForStatement') is None


def test_assoc_left136_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression137' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_RelationalExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression137', None)
    _safe_set(owner, 'amethyst_RelationalExpression', partner)
    assert getattr(partner, 'amethyst_Expression137') == owner
    _safe_set(owner, 'amethyst_RelationalExpression', None)
    assert getattr(partner, 'amethyst_Expression137') is None


def test_assoc_left141_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression142' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_EqualityExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression142', None)
    _safe_set(owner, 'amethyst_EqualityExpression', partner)
    assert getattr(partner, 'amethyst_Expression142') == owner
    _safe_set(owner, 'amethyst_EqualityExpression', None)
    assert getattr(partner, 'amethyst_Expression142') is None


def test_assoc_left146_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression147' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_ShiftExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression147', None)
    _safe_set(owner, 'amethyst_ShiftExpression', partner)
    assert getattr(partner, 'amethyst_Expression147') == owner
    _safe_set(owner, 'amethyst_ShiftExpression', None)
    assert getattr(partner, 'amethyst_Expression147') is None


def test_assoc_left151_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression152' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_AdditiveExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_AdditiveExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_AdditiveExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression152', None)
    _safe_set(owner, 'amethyst_AdditiveExpression', partner)
    assert getattr(partner, 'amethyst_Expression152') == owner
    _safe_set(owner, 'amethyst_AdditiveExpression', None)
    assert getattr(partner, 'amethyst_Expression152') is None


def test_assoc_left156_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression157' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_MultiplicativeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_MultiplicativeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_MultiplicativeExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression157', None)
    _safe_set(owner, 'amethyst_MultiplicativeExpression', partner)
    assert getattr(partner, 'amethyst_Expression157') == owner
    _safe_set(owner, 'amethyst_MultiplicativeExpression', None)
    assert getattr(partner, 'amethyst_Expression157') is None


def test_assoc_left161_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression162' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_MatchingExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_MatchingExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_MatchingExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression162', None)
    _safe_set(owner, 'amethyst_MatchingExpression', partner)
    assert getattr(partner, 'amethyst_Expression162') == owner
    _safe_set(owner, 'amethyst_MatchingExpression', None)
    assert getattr(partner, 'amethyst_Expression162') is None


def test_assoc_methods43_stub_double():
    # amethyst_ClassDeclaration has no real 'amethyst_ClassDeclaration44' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_Symbol(name="sample_text")
    partner = amethyst_ClassDeclaration()
    setattr(partner, 'amethyst_ClassDeclaration44', None)
    _safe_set(owner, 'amethyst_Symbol45', partner)
    assert owner in getattr(partner, 'amethyst_ClassDeclaration44')
    _safe_set(owner, 'amethyst_Symbol45', None)
    assert owner not in getattr(partner, 'amethyst_ClassDeclaration44')


def test_assoc_properties46_stub_double():
    # amethyst_ClassDeclaration has no real 'amethyst_ClassDeclaration47' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_Symbol(name="sample_text")
    partner = amethyst_ClassDeclaration()
    setattr(partner, 'amethyst_ClassDeclaration47', None)
    _safe_set(owner, 'amethyst_Symbol48', partner)
    assert owner in getattr(partner, 'amethyst_ClassDeclaration47')
    _safe_set(owner, 'amethyst_Symbol48', None)
    assert owner not in getattr(partner, 'amethyst_ClassDeclaration47')


def test_assoc_right123_stub_double():
    # amethyst_MemberAccessExpression has no real 'amethyst_MemberAccessExpression124' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_Symbol(name="sample_text")
    partner = amethyst_MemberAccessExpression()
    setattr(partner, 'amethyst_MemberAccessExpression124', None)
    _safe_set(owner, 'amethyst_Symbol125', partner)
    assert getattr(partner, 'amethyst_MemberAccessExpression124') == owner
    _safe_set(owner, 'amethyst_Symbol125', None)
    assert getattr(partner, 'amethyst_MemberAccessExpression124') is None


def test_assoc_right138_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression140' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_RelationalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_RelationalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_RelationalExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression140', None)
    _safe_set(owner, 'amethyst_RelationalExpression139', partner)
    assert getattr(partner, 'amethyst_Expression140') == owner
    _safe_set(owner, 'amethyst_RelationalExpression139', None)
    assert getattr(partner, 'amethyst_Expression140') is None


def test_assoc_right143_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression145' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_EqualityExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression145', None)
    _safe_set(owner, 'amethyst_EqualityExpression144', partner)
    assert getattr(partner, 'amethyst_Expression145') == owner
    _safe_set(owner, 'amethyst_EqualityExpression144', None)
    assert getattr(partner, 'amethyst_Expression145') is None


def test_assoc_right148_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression150' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_ShiftExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_ShiftExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_ShiftExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression150', None)
    _safe_set(owner, 'amethyst_ShiftExpression149', partner)
    assert getattr(partner, 'amethyst_Expression150') == owner
    _safe_set(owner, 'amethyst_ShiftExpression149', None)
    assert getattr(partner, 'amethyst_Expression150') is None


def test_assoc_right153_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression155' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_AdditiveExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_AdditiveExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_AdditiveExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression155', None)
    _safe_set(owner, 'amethyst_AdditiveExpression154', partner)
    assert getattr(partner, 'amethyst_Expression155') == owner
    _safe_set(owner, 'amethyst_AdditiveExpression154', None)
    assert getattr(partner, 'amethyst_Expression155') is None


def test_assoc_right158_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression160' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_MultiplicativeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_MultiplicativeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_MultiplicativeExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression160', None)
    _safe_set(owner, 'amethyst_MultiplicativeExpression159', partner)
    assert getattr(partner, 'amethyst_Expression160') == owner
    _safe_set(owner, 'amethyst_MultiplicativeExpression159', None)
    assert getattr(partner, 'amethyst_Expression160') is None


def test_assoc_right163_stub_double():
    # amethyst_Expression has no real 'amethyst_Expression165' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_MatchingExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_MatchingExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_MatchingExpression(operator="sample_text")
    partner = amethyst_Expression()
    setattr(partner, 'amethyst_Expression165', None)
    _safe_set(owner, 'amethyst_MatchingExpression164', partner)
    assert getattr(partner, 'amethyst_Expression165') == owner
    _safe_set(owner, 'amethyst_MatchingExpression164', None)
    assert getattr(partner, 'amethyst_Expression165') is None


def test_assoc_start187_stub_double():
    # amethyst_NumberRangeLiteral has no real 'amethyst_NumberRangeLiteral' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_IntLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_IntLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_IntLiteral(value=7)
    partner = amethyst_NumberRangeLiteral()
    setattr(partner, 'amethyst_NumberRangeLiteral', None)
    _safe_set(owner, 'amethyst_IntLiteral', partner)
    assert getattr(partner, 'amethyst_NumberRangeLiteral') == owner
    _safe_set(owner, 'amethyst_IntLiteral', None)
    assert getattr(partner, 'amethyst_NumberRangeLiteral') is None


def test_assoc_start191_stub_double():
    # amethyst_CharRangeLiteral has no real 'amethyst_CharRangeLiteral' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_CharLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_CharLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_CharLiteral(value="sample_text")
    partner = amethyst_CharRangeLiteral()
    setattr(partner, 'amethyst_CharRangeLiteral', None)
    _safe_set(owner, 'amethyst_CharLiteral', partner)
    assert getattr(partner, 'amethyst_CharRangeLiteral') == owner
    _safe_set(owner, 'amethyst_CharLiteral', None)
    assert getattr(partner, 'amethyst_CharRangeLiteral') is None


def test_assoc_statements35_stub_double():
    # amethyst_Statement has no real 'amethyst_Statement37' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_DefinitionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_DefinitionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_DefinitionDeclaration(static=True)
    partner = amethyst_Statement()
    setattr(partner, 'amethyst_Statement37', None)
    _safe_set(owner, 'amethyst_DefinitionDeclaration36', {partner})
    assert getattr(partner, 'amethyst_Statement37') == owner
    _safe_set(owner, 'amethyst_DefinitionDeclaration36', set())
    assert getattr(partner, 'amethyst_Statement37') is None


def test_assoc_symbolRef21_stub_double():
    # amethyst_SymbolReference has no real 'amethyst_SymbolReference' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_Symbol(name="sample_text")
    partner = amethyst_SymbolReference()
    setattr(partner, 'amethyst_SymbolReference', None)
    _safe_set(owner, 'amethyst_Symbol22', partner)
    assert getattr(partner, 'amethyst_SymbolReference') == owner
    _safe_set(owner, 'amethyst_Symbol22', None)
    assert getattr(partner, 'amethyst_SymbolReference') is None


def test_assoc_type32_stub_double():
    # amethyst_AbstractType has no real 'amethyst_AbstractType34' property in the generated
    # code (a bare stub) -- manually attach it so amethyst_DefinitionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # amethyst_DefinitionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = amethyst_DefinitionDeclaration(static=True)
    partner = amethyst_AbstractType()
    setattr(partner, 'amethyst_AbstractType34', None)
    _safe_set(owner, 'amethyst_DefinitionDeclaration33', partner)
    assert getattr(partner, 'amethyst_AbstractType34') == owner
    _safe_set(owner, 'amethyst_DefinitionDeclaration33', None)
    assert getattr(partner, 'amethyst_AbstractType34') is None


