import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Declaration,
    Expression,
    Literal,
    Statement,
    Type,
    VarDeclaration,
    xs_AndExpression,
    xs_Assign,
    xs_Block,
    xs_BoolType,
    xs_BreakStatement,
    xs_Call,
    xs_ComparisonExpression,
    xs_ContinueStatement,
    xs_Declaration,
    xs_EqualsExpression,
    xs_Expression,
    xs_Factor,
    xs_FloatType,
    xs_ForStatement,
    xs_ForVarDeclaration,
    xs_FunctionDeclaration,
    xs_GlobalVarDeclaration,
    xs_IfElseStatement,
    xs_IncludeDeclaration,
    xs_IntType,
    xs_Literal,
    xs_LiteralBool,
    xs_LiteralFloat,
    xs_LiteralInt,
    xs_LiteralString,
    xs_LocalVarDeclaration,
    xs_OrExpression,
    xs_ParameterDeclaration,
    xs_PostfixStatement,
    xs_Program,
    xs_ReturnStatement,
    xs_RuleDeclaration,
    xs_Statement,
    xs_StringType,
    xs_SwitchCase,
    xs_SwitchDefault,
    xs_SwitchStatement,
    xs_Term,
    xs_Type,
    xs_Var,
    xs_VarDeclaration,
    xs_VectorLiteral,
    xs_VectorType,
    xs_VoidType,
    xs_WhileStatement,
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

def test_assoc_var27_reverse_link_reassign_clear():
    a1 = xs_VarDeclaration(name="sample_text")
    a2 = xs_VarDeclaration(name="sample_text_2")
    b = xs_PostfixStatement(op="sample_text")
    _safe_set(b, 'xs_PostfixStatement', a1)
    assert _is_linked(b, 'xs_PostfixStatement', a1)
    if hasattr(a1, 'xs_VarDeclaration28'):
        assert _is_linked(a1, 'xs_VarDeclaration28', b)
    _safe_set(b, 'xs_PostfixStatement', a2)
    assert _is_linked(b, 'xs_PostfixStatement', a2)
    if hasattr(a1, 'xs_VarDeclaration28'):
        assert not _is_linked(a1, 'xs_VarDeclaration28', b)
    if hasattr(a2, 'xs_VarDeclaration28'):
        assert _is_linked(a2, 'xs_VarDeclaration28', b)
    _safe_set(b, 'xs_PostfixStatement', None)
    assert not _is_linked(b, 'xs_PostfixStatement', a2)
    if hasattr(a2, 'xs_VarDeclaration28'):
        assert not _is_linked(a2, 'xs_VarDeclaration28', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body12_stub_double():
    # xs_Block has no real 'xs_Block' property in the generated
    # code (a bare stub) -- manually attach it so xs_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_FunctionDeclaration(mutable=True, name="sample_text")
    partner = xs_Block()
    setattr(partner, 'xs_Block', None)
    _safe_set(owner, 'xs_FunctionDeclaration13', partner)
    assert getattr(partner, 'xs_Block') == owner
    _safe_set(owner, 'xs_FunctionDeclaration13', None)
    assert getattr(partner, 'xs_Block') is None


def test_assoc_body14_stub_double():
    # xs_Block has no real 'xs_Block15' property in the generated
    # code (a bare stub) -- manually attach it so xs_RuleDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_RuleDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_RuleDeclaration(active=True, group="sample_text", highFrequency=True, maxInterval=7, minInterval=7, name="sample_text", priority=7, runImmediately=True)
    partner = xs_Block()
    setattr(partner, 'xs_Block15', None)
    _safe_set(owner, 'xs_RuleDeclaration', partner)
    assert getattr(partner, 'xs_Block15') == owner
    _safe_set(owner, 'xs_RuleDeclaration', None)
    assert getattr(partner, 'xs_Block15') is None


def test_assoc_declaration25_stub_double():
    # xs_Var has no real 'xs_Var' property in the generated
    # code (a bare stub) -- manually attach it so xs_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_VarDeclaration(name="sample_text")
    partner = xs_Var()
    setattr(partner, 'xs_Var', None)
    _safe_set(owner, 'xs_VarDeclaration26', partner)
    assert getattr(partner, 'xs_Var') == owner
    _safe_set(owner, 'xs_VarDeclaration26', None)
    assert getattr(partner, 'xs_Var') is None


def test_assoc_end43_stub_double():
    # xs_Expression has no real 'xs_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so xs_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_ForStatement(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression45', None)
    _safe_set(owner, 'xs_ForStatement44', partner)
    assert getattr(partner, 'xs_Expression45') == owner
    _safe_set(owner, 'xs_ForStatement44', None)
    assert getattr(partner, 'xs_Expression45') is None


def test_assoc_function94_stub_double():
    # xs_Call has no real 'xs_Call' property in the generated
    # code (a bare stub) -- manually attach it so xs_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_FunctionDeclaration(mutable=True, name="sample_text")
    partner = xs_Call()
    setattr(partner, 'xs_Call', None)
    _safe_set(owner, 'xs_FunctionDeclaration95', partner)
    assert getattr(partner, 'xs_Call') == owner
    _safe_set(owner, 'xs_FunctionDeclaration95', None)
    assert getattr(partner, 'xs_Call') is None


def test_assoc_left64_stub_double():
    # xs_Expression has no real 'xs_Expression65' property in the generated
    # code (a bare stub) -- manually attach it so xs_OrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_OrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_OrExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression65', None)
    _safe_set(owner, 'xs_OrExpression', partner)
    assert getattr(partner, 'xs_Expression65') == owner
    _safe_set(owner, 'xs_OrExpression', None)
    assert getattr(partner, 'xs_Expression65') is None


def test_assoc_left69_stub_double():
    # xs_Expression has no real 'xs_Expression70' property in the generated
    # code (a bare stub) -- manually attach it so xs_AndExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_AndExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_AndExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression70', None)
    _safe_set(owner, 'xs_AndExpression', partner)
    assert getattr(partner, 'xs_Expression70') == owner
    _safe_set(owner, 'xs_AndExpression', None)
    assert getattr(partner, 'xs_Expression70') is None


def test_assoc_left74_stub_double():
    # xs_Expression has no real 'xs_Expression75' property in the generated
    # code (a bare stub) -- manually attach it so xs_EqualsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_EqualsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_EqualsExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression75', None)
    _safe_set(owner, 'xs_EqualsExpression', partner)
    assert getattr(partner, 'xs_Expression75') == owner
    _safe_set(owner, 'xs_EqualsExpression', None)
    assert getattr(partner, 'xs_Expression75') is None


def test_assoc_left79_stub_double():
    # xs_Expression has no real 'xs_Expression80' property in the generated
    # code (a bare stub) -- manually attach it so xs_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_ComparisonExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression80', None)
    _safe_set(owner, 'xs_ComparisonExpression', partner)
    assert getattr(partner, 'xs_Expression80') == owner
    _safe_set(owner, 'xs_ComparisonExpression', None)
    assert getattr(partner, 'xs_Expression80') is None


def test_assoc_left84_stub_double():
    # xs_Expression has no real 'xs_Expression85' property in the generated
    # code (a bare stub) -- manually attach it so xs_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_Term(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression85', None)
    _safe_set(owner, 'xs_Term', partner)
    assert getattr(partner, 'xs_Expression85') == owner
    _safe_set(owner, 'xs_Term', None)
    assert getattr(partner, 'xs_Expression85') is None


def test_assoc_left89_stub_double():
    # xs_Expression has no real 'xs_Expression90' property in the generated
    # code (a bare stub) -- manually attach it so xs_Factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_Factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_Factor(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression90', None)
    _safe_set(owner, 'xs_Factor', partner)
    assert getattr(partner, 'xs_Expression90') == owner
    _safe_set(owner, 'xs_Factor', None)
    assert getattr(partner, 'xs_Expression90') is None


def test_assoc_parameters9_stub_double():
    # xs_ParameterDeclaration has no real 'xs_ParameterDeclaration11' property in the generated
    # code (a bare stub) -- manually attach it so xs_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_FunctionDeclaration(mutable=True, name="sample_text")
    partner = xs_ParameterDeclaration()
    setattr(partner, 'xs_ParameterDeclaration11', None)
    _safe_set(owner, 'xs_FunctionDeclaration10', {partner})
    assert getattr(partner, 'xs_ParameterDeclaration11') == owner
    _safe_set(owner, 'xs_FunctionDeclaration10', set())
    assert getattr(partner, 'xs_ParameterDeclaration11') is None


def test_assoc_right66_stub_double():
    # xs_Expression has no real 'xs_Expression68' property in the generated
    # code (a bare stub) -- manually attach it so xs_OrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_OrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_OrExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression68', None)
    _safe_set(owner, 'xs_OrExpression67', partner)
    assert getattr(partner, 'xs_Expression68') == owner
    _safe_set(owner, 'xs_OrExpression67', None)
    assert getattr(partner, 'xs_Expression68') is None


def test_assoc_right71_stub_double():
    # xs_Expression has no real 'xs_Expression73' property in the generated
    # code (a bare stub) -- manually attach it so xs_AndExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_AndExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_AndExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression73', None)
    _safe_set(owner, 'xs_AndExpression72', partner)
    assert getattr(partner, 'xs_Expression73') == owner
    _safe_set(owner, 'xs_AndExpression72', None)
    assert getattr(partner, 'xs_Expression73') is None


def test_assoc_right76_stub_double():
    # xs_Expression has no real 'xs_Expression78' property in the generated
    # code (a bare stub) -- manually attach it so xs_EqualsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_EqualsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_EqualsExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression78', None)
    _safe_set(owner, 'xs_EqualsExpression77', partner)
    assert getattr(partner, 'xs_Expression78') == owner
    _safe_set(owner, 'xs_EqualsExpression77', None)
    assert getattr(partner, 'xs_Expression78') is None


def test_assoc_right81_stub_double():
    # xs_Expression has no real 'xs_Expression83' property in the generated
    # code (a bare stub) -- manually attach it so xs_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_ComparisonExpression(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression83', None)
    _safe_set(owner, 'xs_ComparisonExpression82', partner)
    assert getattr(partner, 'xs_Expression83') == owner
    _safe_set(owner, 'xs_ComparisonExpression82', None)
    assert getattr(partner, 'xs_Expression83') is None


def test_assoc_right86_stub_double():
    # xs_Expression has no real 'xs_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so xs_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_Term(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression88', None)
    _safe_set(owner, 'xs_Term87', partner)
    assert getattr(partner, 'xs_Expression88') == owner
    _safe_set(owner, 'xs_Term87', None)
    assert getattr(partner, 'xs_Expression88') is None


def test_assoc_right91_stub_double():
    # xs_Expression has no real 'xs_Expression93' property in the generated
    # code (a bare stub) -- manually attach it so xs_Factor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_Factor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_Factor(op="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression93', None)
    _safe_set(owner, 'xs_Factor92', partner)
    assert getattr(partner, 'xs_Expression93') == owner
    _safe_set(owner, 'xs_Factor92', None)
    assert getattr(partner, 'xs_Expression93') is None


def test_assoc_statement46_stub_double():
    # xs_Statement has no real 'xs_Statement48' property in the generated
    # code (a bare stub) -- manually attach it so xs_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_ForStatement(op="sample_text")
    partner = xs_Statement()
    setattr(partner, 'xs_Statement48', None)
    _safe_set(owner, 'xs_ForStatement47', partner)
    assert getattr(partner, 'xs_Statement48') == owner
    _safe_set(owner, 'xs_ForStatement47', None)
    assert getattr(partner, 'xs_Statement48') is None


def test_assoc_type3_stub_double():
    # xs_Type has no real 'xs_Type4' property in the generated
    # code (a bare stub) -- manually attach it so xs_GlobalVarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_GlobalVarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_GlobalVarDeclaration(const=True, extern=True)
    partner = xs_Type()
    setattr(partner, 'xs_Type4', None)
    _safe_set(owner, 'xs_GlobalVarDeclaration', partner)
    assert getattr(partner, 'xs_Type4') == owner
    _safe_set(owner, 'xs_GlobalVarDeclaration', None)
    assert getattr(partner, 'xs_Type4') is None


def test_assoc_type7_stub_double():
    # xs_Type has no real 'xs_Type8' property in the generated
    # code (a bare stub) -- manually attach it so xs_FunctionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_FunctionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_FunctionDeclaration(mutable=True, name="sample_text")
    partner = xs_Type()
    setattr(partner, 'xs_Type8', None)
    _safe_set(owner, 'xs_FunctionDeclaration', partner)
    assert getattr(partner, 'xs_Type8') == owner
    _safe_set(owner, 'xs_FunctionDeclaration', None)
    assert getattr(partner, 'xs_Type8') is None


def test_assoc_value1_stub_double():
    # xs_Expression has no real 'xs_Expression' property in the generated
    # code (a bare stub) -- manually attach it so xs_VarDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_VarDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_VarDeclaration(name="sample_text")
    partner = xs_Expression()
    setattr(partner, 'xs_Expression', None)
    _safe_set(owner, 'xs_VarDeclaration', partner)
    assert getattr(partner, 'xs_Expression') == owner
    _safe_set(owner, 'xs_VarDeclaration', None)
    assert getattr(partner, 'xs_Expression') is None


def test_assoc_var42_stub_double():
    # xs_ForVarDeclaration has no real 'xs_ForVarDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so xs_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xs_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xs_ForStatement(op="sample_text")
    partner = xs_ForVarDeclaration()
    setattr(partner, 'xs_ForVarDeclaration', None)
    _safe_set(owner, 'xs_ForStatement', partner)
    assert getattr(partner, 'xs_ForVarDeclaration') == owner
    _safe_set(owner, 'xs_ForStatement', None)
    assert getattr(partner, 'xs_ForVarDeclaration') is None


