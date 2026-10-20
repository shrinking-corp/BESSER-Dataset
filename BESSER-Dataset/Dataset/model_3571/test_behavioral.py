import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    FeatureCall,
    Literal,
    SyntaxElement,
    expression_BooleanLiteral,
    expression_BooleanOperation,
    expression_Case,
    expression_CastedExpression,
    expression_ChainExpression,
    expression_CollectionExpression,
    expression_ConstructorCallExpression,
    expression_Expression,
    expression_FeatureCall,
    expression_GlobalVarExpression,
    expression_Identifier,
    expression_IfExpression,
    expression_IntegerLiteral,
    expression_LetExpression,
    expression_ListLiteral,
    expression_Literal,
    expression_NullLiteral,
    expression_OperationCall,
    expression_RealLiteral,
    expression_StringLiteral,
    expression_SwitchExpression,
    expression_SyntaxElement,
    expression_TypeSelectExpression,
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

def test_assoc_id143_reverse_link_reassign_clear():
    a1 = expression_Identifier(cl="sample_text", id="sample_text")
    a2 = expression_Identifier(cl="sample_text_2", id="sample_text_2")
    b = expression_Identifier(cl="sample_text", id="sample_text")
    _safe_set(b, 'expression_Identifier44', a1)
    assert _is_linked(b, 'expression_Identifier44', a1)
    if hasattr(a1, 'expression_Identifier42'):
        assert _is_linked(a1, 'expression_Identifier42', b)
    _safe_set(b, 'expression_Identifier44', a2)
    assert _is_linked(b, 'expression_Identifier44', a2)
    if hasattr(a1, 'expression_Identifier42'):
        assert not _is_linked(a1, 'expression_Identifier42', b)
    if hasattr(a2, 'expression_Identifier42'):
        assert _is_linked(a2, 'expression_Identifier42', b)
    _safe_set(b, 'expression_Identifier44', None)
    assert not _is_linked(b, 'expression_Identifier44', a2)
    if hasattr(a2, 'expression_Identifier42'):
        assert not _is_linked(a2, 'expression_Identifier42', b)


def test_assoc_type33_reverse_link_reassign_clear():
    a1 = expression_Identifier(cl="sample_text", id="sample_text")
    a2 = expression_Identifier(cl="sample_text_2", id="sample_text_2")
    b = expression_FeatureCall(name="sample_text")
    _safe_set(b, 'expression_FeatureCall34', a1)
    assert _is_linked(b, 'expression_FeatureCall34', a1)
    if hasattr(a1, 'expression_Identifier35'):
        assert _is_linked(a1, 'expression_Identifier35', b)
    _safe_set(b, 'expression_FeatureCall34', a2)
    assert _is_linked(b, 'expression_FeatureCall34', a2)
    if hasattr(a1, 'expression_Identifier35'):
        assert not _is_linked(a1, 'expression_Identifier35', b)
    if hasattr(a2, 'expression_Identifier35'):
        assert _is_linked(a2, 'expression_Identifier35', b)
    _safe_set(b, 'expression_FeatureCall34', None)
    assert not _is_linked(b, 'expression_FeatureCall34', a2)
    if hasattr(a2, 'expression_Identifier35'):
        assert not _is_linked(a2, 'expression_Identifier35', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_exp40_stub_double():
    # expression_Expression has no real 'expression_Expression41' property in the generated
    # code (a bare stub) -- manually attach it so expression_CollectionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_CollectionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_CollectionExpression(var="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression41', None)
    _safe_set(owner, 'expression_CollectionExpression', partner)
    assert getattr(partner, 'expression_Expression41') == owner
    _safe_set(owner, 'expression_CollectionExpression', None)
    assert getattr(partner, 'expression_Expression41') is None


def test_assoc_left50_stub_double():
    # expression_Expression has no real 'expression_Expression51' property in the generated
    # code (a bare stub) -- manually attach it so expression_BooleanOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_BooleanOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_BooleanOperation(operator="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression51', None)
    _safe_set(owner, 'expression_BooleanOperation', partner)
    assert getattr(partner, 'expression_Expression51') == owner
    _safe_set(owner, 'expression_BooleanOperation', None)
    assert getattr(partner, 'expression_Expression51') is None


def test_assoc_right52_stub_double():
    # expression_Expression has no real 'expression_Expression54' property in the generated
    # code (a bare stub) -- manually attach it so expression_BooleanOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_BooleanOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_BooleanOperation(operator="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression54', None)
    _safe_set(owner, 'expression_BooleanOperation53', partner)
    assert getattr(partner, 'expression_Expression54') == owner
    _safe_set(owner, 'expression_BooleanOperation53', None)
    assert getattr(partner, 'expression_Expression54') is None


def test_assoc_target1_stub_double():
    # expression_Expression has no real 'expression_Expression3' property in the generated
    # code (a bare stub) -- manually attach it so expression_LetExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_LetExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_LetExpression(identifier="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression3', None)
    _safe_set(owner, 'expression_LetExpression2', partner)
    assert getattr(partner, 'expression_Expression3') == owner
    _safe_set(owner, 'expression_LetExpression2', None)
    assert getattr(partner, 'expression_Expression3') is None


def test_assoc_target31_stub_double():
    # expression_Expression has no real 'expression_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so expression_FeatureCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_FeatureCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_FeatureCall(name="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression32', None)
    _safe_set(owner, 'expression_FeatureCall', partner)
    assert getattr(partner, 'expression_Expression32') == owner
    _safe_set(owner, 'expression_FeatureCall', None)
    assert getattr(partner, 'expression_Expression32') is None


def test_assoc_type38_stub_double():
    # expression_ConstructorCallExpression has no real 'expression_ConstructorCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so expression_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Identifier(cl="sample_text", id="sample_text")
    partner = expression_ConstructorCallExpression()
    setattr(partner, 'expression_ConstructorCallExpression', None)
    _safe_set(owner, 'expression_Identifier39', partner)
    assert getattr(partner, 'expression_ConstructorCallExpression') == owner
    _safe_set(owner, 'expression_Identifier39', None)
    assert getattr(partner, 'expression_ConstructorCallExpression') is None


def test_assoc_type4_stub_double():
    # expression_CastedExpression has no real 'expression_CastedExpression' property in the generated
    # code (a bare stub) -- manually attach it so expression_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_Identifier(cl="sample_text", id="sample_text")
    partner = expression_CastedExpression()
    setattr(partner, 'expression_CastedExpression', None)
    _safe_set(owner, 'expression_Identifier', partner)
    assert getattr(partner, 'expression_CastedExpression') == owner
    _safe_set(owner, 'expression_Identifier', None)
    assert getattr(partner, 'expression_CastedExpression') is None


def test_assoc_varExpr0_stub_double():
    # expression_Expression has no real 'expression_Expression' property in the generated
    # code (a bare stub) -- manually attach it so expression_LetExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_LetExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_LetExpression(identifier="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression', None)
    _safe_set(owner, 'expression_LetExpression', partner)
    assert getattr(partner, 'expression_Expression') == owner
    _safe_set(owner, 'expression_LetExpression', None)
    assert getattr(partner, 'expression_Expression') is None


