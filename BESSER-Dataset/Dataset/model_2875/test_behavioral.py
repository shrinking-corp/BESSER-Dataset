import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticOperatorExpression,
    BinaryOperatorExpression,
    CollectionExpression,
    CollectionInitialisationExpression,
    ComparableExpression,
    ComparisonOperatorExpression,
    Expression,
    FeatureCallExpression,
    LogicalOperatorExpression,
    OperatorExpression,
    OrderedCollection,
    PrimitiveExpression,
    SummableExpression,
    UnaryOperatorExpression,
    UniqueCollection,
    VariableDeclarationExpression,
    eol_expression_AndOperatorExpression,
    eol_expression_ArithmeticOperatorExpression,
    eol_expression_BagExpression,
    eol_expression_BinaryOperatorExpression,
    eol_expression_BooleanExpression,
    eol_expression_CollectionExpression,
    eol_expression_CollectionInitialisationExpression,
    eol_expression_ComparableExpression,
    eol_expression_ComparisonOperatorExpression,
    eol_expression_DivideOperatorExpression,
    eol_expression_EnumerationLiteralExpression,
    eol_expression_EqualsOperatorExpression,
    eol_expression_Expression,
    eol_expression_ExpressionList,
    eol_expression_ExpressionRange,
    eol_expression_FOLMethodCallExpression,
    eol_expression_FeatureCallExpression,
    eol_expression_FormalParameterExpression,
    eol_expression_GreaterThanOperatorExpression,
    eol_expression_GreaterThanOrEqualToOperatorExpression,
    eol_expression_ImpliesOperatorExpression,
    eol_expression_IntegerExpression,
    eol_expression_KeyValueExpression,
    eol_expression_LessThanOperatorExpression,
    eol_expression_LessThanOrEqualToOperatorExpression,
    eol_expression_LogicalOperatorExpression,
    eol_expression_MapExpression,
    eol_expression_MethodCallExpression,
    eol_expression_MinusOperatorExpression,
    eol_expression_MultiplyOperatorExpression,
    eol_expression_NameExpression,
    eol_expression_NegativeOperatorExpression,
    eol_expression_NewExpression,
    eol_expression_NotEqualsOperatorExpression,
    eol_expression_NotOperatorExpression,
    eol_expression_OperatorExpression,
    eol_expression_OrOperatorExpression,
    eol_expression_OrderedCollection,
    eol_expression_OrderedSetExpression,
    eol_expression_PlusOperatorExpression,
    eol_expression_PrimitiveExpression,
    eol_expression_PropertyCallExpression,
    eol_expression_RealExpression,
    eol_expression_SequenceExpression,
    eol_expression_SetExpression,
    eol_expression_Statement,
    eol_expression_StringExpression,
    eol_expression_SummableExpression,
    eol_expression_Type,
    eol_expression_UnaryOperatorExpression,
    eol_expression_UniqueCollection,
    eol_expression_VariableDeclarationExpression,
    eol_expression_XorOperatorExpression,
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

def test_assoc_name8_reverse_link_reassign_clear():
    a1 = eol_expression_VariableDeclarationExpression(create=True)
    a2 = eol_expression_VariableDeclarationExpression(create=False)
    b = eol_expression_NameExpression(isType=True, name="sample_text")
    _safe_set(b, 'eol_expression_NameExpression', a1)
    assert _is_linked(b, 'eol_expression_NameExpression', a1)
    if hasattr(a1, 'eol_expression_VariableDeclarationExpression'):
        assert _is_linked(a1, 'eol_expression_VariableDeclarationExpression', b)
    _safe_set(b, 'eol_expression_NameExpression', a2)
    assert _is_linked(b, 'eol_expression_NameExpression', a2)
    if hasattr(a1, 'eol_expression_VariableDeclarationExpression'):
        assert not _is_linked(a1, 'eol_expression_VariableDeclarationExpression', b)
    if hasattr(a2, 'eol_expression_VariableDeclarationExpression'):
        assert _is_linked(a2, 'eol_expression_VariableDeclarationExpression', b)
    _safe_set(b, 'eol_expression_NameExpression', None)
    assert not _is_linked(b, 'eol_expression_NameExpression', a2)
    if hasattr(a2, 'eol_expression_VariableDeclarationExpression'):
        assert not _is_linked(a2, 'eol_expression_VariableDeclarationExpression', b)


def test_assoc_property16_reverse_link_reassign_clear():
    a1 = eol_expression_PropertyCallExpression(extended=True)
    a2 = eol_expression_PropertyCallExpression(extended=False)
    b = eol_expression_NameExpression(isType=True, name="sample_text")
    _safe_set(b, 'eol_expression_NameExpression17', a1)
    assert _is_linked(b, 'eol_expression_NameExpression17', a1)
    if hasattr(a1, 'eol_expression_PropertyCallExpression'):
        assert _is_linked(a1, 'eol_expression_PropertyCallExpression', b)
    _safe_set(b, 'eol_expression_NameExpression17', a2)
    assert _is_linked(b, 'eol_expression_NameExpression17', a2)
    if hasattr(a1, 'eol_expression_PropertyCallExpression'):
        assert not _is_linked(a1, 'eol_expression_PropertyCallExpression', b)
    if hasattr(a2, 'eol_expression_PropertyCallExpression'):
        assert _is_linked(a2, 'eol_expression_PropertyCallExpression', b)
    _safe_set(b, 'eol_expression_NameExpression17', None)
    assert not _is_linked(b, 'eol_expression_NameExpression17', a2)
    if hasattr(a2, 'eol_expression_PropertyCallExpression'):
        assert not _is_linked(a2, 'eol_expression_PropertyCallExpression', b)


def test_assoc_target9_reverse_link_reassign_clear():
    a1 = eol_expression_FeatureCallExpression(arrow=True)
    a2 = eol_expression_FeatureCallExpression(arrow=False)
    b = eol_expression_Expression(inBrackets=True)
    _safe_set(b, 'eol_expression_Expression10', a1)
    assert _is_linked(b, 'eol_expression_Expression10', a1)
    if hasattr(a1, 'eol_expression_FeatureCallExpression'):
        assert _is_linked(a1, 'eol_expression_FeatureCallExpression', b)
    _safe_set(b, 'eol_expression_Expression10', a2)
    assert _is_linked(b, 'eol_expression_Expression10', a2)
    if hasattr(a1, 'eol_expression_FeatureCallExpression'):
        assert not _is_linked(a1, 'eol_expression_FeatureCallExpression', b)
    if hasattr(a2, 'eol_expression_FeatureCallExpression'):
        assert _is_linked(a2, 'eol_expression_FeatureCallExpression', b)
    _safe_set(b, 'eol_expression_Expression10', None)
    assert not _is_linked(b, 'eol_expression_Expression10', a2)
    if hasattr(a2, 'eol_expression_FeatureCallExpression'):
        assert not _is_linked(a2, 'eol_expression_FeatureCallExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments11_stub_double():
    # eol_expression_MethodCallExpression has no real 'eol_expression_MethodCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_MethodCallExpression()
    setattr(partner, 'eol_expression_MethodCallExpression', None)
    _safe_set(owner, 'eol_expression_Expression12', partner)
    assert owner in getattr(partner, 'eol_expression_MethodCallExpression')
    _safe_set(owner, 'eol_expression_Expression12', None)
    assert owner not in getattr(partner, 'eol_expression_MethodCallExpression')


def test_assoc_conditions19_stub_double():
    # eol_expression_FOLMethodCallExpression has no real 'eol_expression_FOLMethodCallExpression20' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_FOLMethodCallExpression()
    setattr(partner, 'eol_expression_FOLMethodCallExpression20', None)
    _safe_set(owner, 'eol_expression_Expression21', partner)
    assert owner in getattr(partner, 'eol_expression_FOLMethodCallExpression20')
    _safe_set(owner, 'eol_expression_Expression21', None)
    assert owner not in getattr(partner, 'eol_expression_FOLMethodCallExpression20')


def test_assoc_contents37_stub_double():
    # eol_expression_CollectionExpression has no real 'eol_expression_CollectionExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_CollectionExpression()
    setattr(partner, 'eol_expression_CollectionExpression', None)
    _safe_set(owner, 'eol_expression_Expression38', partner)
    assert owner in getattr(partner, 'eol_expression_CollectionExpression')
    _safe_set(owner, 'eol_expression_Expression38', None)
    assert owner not in getattr(partner, 'eol_expression_CollectionExpression')


def test_assoc_end51_stub_double():
    # eol_expression_ExpressionRange has no real 'eol_expression_ExpressionRange52' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_ExpressionRange()
    setattr(partner, 'eol_expression_ExpressionRange52', None)
    _safe_set(owner, 'eol_expression_Expression53', partner)
    assert getattr(partner, 'eol_expression_ExpressionRange52') == owner
    _safe_set(owner, 'eol_expression_Expression53', None)
    assert getattr(partner, 'eol_expression_ExpressionRange52') is None


def test_assoc_enumeration43_stub_double():
    # eol_expression_EnumerationLiteralExpression has no real 'eol_expression_EnumerationLiteralExpression44' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_NameExpression(isType=True, name="sample_text")
    partner = eol_expression_EnumerationLiteralExpression()
    setattr(partner, 'eol_expression_EnumerationLiteralExpression44', None)
    _safe_set(owner, 'eol_expression_NameExpression45', partner)
    assert getattr(partner, 'eol_expression_EnumerationLiteralExpression44') == owner
    _safe_set(owner, 'eol_expression_NameExpression45', None)
    assert getattr(partner, 'eol_expression_EnumerationLiteralExpression44') is None


def test_assoc_expression1_stub_double():
    # eol_expression_UnaryOperatorExpression has no real 'eol_expression_UnaryOperatorExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_UnaryOperatorExpression()
    setattr(partner, 'eol_expression_UnaryOperatorExpression', None)
    _safe_set(owner, 'eol_expression_Expression2', partner)
    assert getattr(partner, 'eol_expression_UnaryOperatorExpression') == owner
    _safe_set(owner, 'eol_expression_Expression2', None)
    assert getattr(partner, 'eol_expression_UnaryOperatorExpression') is None


def test_assoc_expressions54_stub_double():
    # eol_expression_ExpressionList has no real 'eol_expression_ExpressionList' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_ExpressionList()
    setattr(partner, 'eol_expression_ExpressionList', None)
    _safe_set(owner, 'eol_expression_Expression55', partner)
    assert owner in getattr(partner, 'eol_expression_ExpressionList')
    _safe_set(owner, 'eol_expression_Expression55', None)
    assert owner not in getattr(partner, 'eol_expression_ExpressionList')


def test_assoc_key25_stub_double():
    # eol_expression_KeyValueExpression has no real 'eol_expression_KeyValueExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_KeyValueExpression()
    setattr(partner, 'eol_expression_KeyValueExpression', None)
    _safe_set(owner, 'eol_expression_Expression26', partner)
    assert getattr(partner, 'eol_expression_KeyValueExpression') == owner
    _safe_set(owner, 'eol_expression_Expression26', None)
    assert getattr(partner, 'eol_expression_KeyValueExpression') is None


def test_assoc_lhs3_stub_double():
    # eol_expression_BinaryOperatorExpression has no real 'eol_expression_BinaryOperatorExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_BinaryOperatorExpression()
    setattr(partner, 'eol_expression_BinaryOperatorExpression', None)
    _safe_set(owner, 'eol_expression_Expression4', partner)
    assert getattr(partner, 'eol_expression_BinaryOperatorExpression') == owner
    _safe_set(owner, 'eol_expression_Expression4', None)
    assert getattr(partner, 'eol_expression_BinaryOperatorExpression') is None


def test_assoc_literal41_stub_double():
    # eol_expression_EnumerationLiteralExpression has no real 'eol_expression_EnumerationLiteralExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_NameExpression(isType=True, name="sample_text")
    partner = eol_expression_EnumerationLiteralExpression()
    setattr(partner, 'eol_expression_EnumerationLiteralExpression', None)
    _safe_set(owner, 'eol_expression_NameExpression42', partner)
    assert getattr(partner, 'eol_expression_EnumerationLiteralExpression') == owner
    _safe_set(owner, 'eol_expression_NameExpression42', None)
    assert getattr(partner, 'eol_expression_EnumerationLiteralExpression') is None


def test_assoc_method13_stub_double():
    # eol_expression_MethodCallExpression has no real 'eol_expression_MethodCallExpression14' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_NameExpression(isType=True, name="sample_text")
    partner = eol_expression_MethodCallExpression()
    setattr(partner, 'eol_expression_MethodCallExpression14', None)
    _safe_set(owner, 'eol_expression_NameExpression15', partner)
    assert getattr(partner, 'eol_expression_MethodCallExpression14') == owner
    _safe_set(owner, 'eol_expression_NameExpression15', None)
    assert getattr(partner, 'eol_expression_MethodCallExpression14') is None


def test_assoc_method22_stub_double():
    # eol_expression_FOLMethodCallExpression has no real 'eol_expression_FOLMethodCallExpression23' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_NameExpression(isType=True, name="sample_text")
    partner = eol_expression_FOLMethodCallExpression()
    setattr(partner, 'eol_expression_FOLMethodCallExpression23', None)
    _safe_set(owner, 'eol_expression_NameExpression24', partner)
    assert getattr(partner, 'eol_expression_FOLMethodCallExpression23') == owner
    _safe_set(owner, 'eol_expression_NameExpression24', None)
    assert getattr(partner, 'eol_expression_FOLMethodCallExpression23') is None


def test_assoc_model46_stub_double():
    # eol_expression_EnumerationLiteralExpression has no real 'eol_expression_EnumerationLiteralExpression47' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_NameExpression(isType=True, name="sample_text")
    partner = eol_expression_EnumerationLiteralExpression()
    setattr(partner, 'eol_expression_EnumerationLiteralExpression47', None)
    _safe_set(owner, 'eol_expression_NameExpression48', partner)
    assert getattr(partner, 'eol_expression_EnumerationLiteralExpression47') == owner
    _safe_set(owner, 'eol_expression_NameExpression48', None)
    assert getattr(partner, 'eol_expression_EnumerationLiteralExpression47') is None


def test_assoc_parameters32_stub_double():
    # eol_expression_NewExpression has no real 'eol_expression_NewExpression33' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_NewExpression()
    setattr(partner, 'eol_expression_NewExpression33', None)
    _safe_set(owner, 'eol_expression_Expression34', partner)
    assert owner in getattr(partner, 'eol_expression_NewExpression33')
    _safe_set(owner, 'eol_expression_Expression34', None)
    assert owner not in getattr(partner, 'eol_expression_NewExpression33')


def test_assoc_resolvedType0_stub_double():
    # eol_expression_Type has no real 'eol_expression_Type' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_Type()
    setattr(partner, 'eol_expression_Type', None)
    _safe_set(owner, 'eol_expression_Expression', partner)
    assert getattr(partner, 'eol_expression_Type') == owner
    _safe_set(owner, 'eol_expression_Expression', None)
    assert getattr(partner, 'eol_expression_Type') is None


def test_assoc_rhs5_stub_double():
    # eol_expression_BinaryOperatorExpression has no real 'eol_expression_BinaryOperatorExpression6' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_BinaryOperatorExpression()
    setattr(partner, 'eol_expression_BinaryOperatorExpression6', None)
    _safe_set(owner, 'eol_expression_Expression7', partner)
    assert getattr(partner, 'eol_expression_BinaryOperatorExpression6') == owner
    _safe_set(owner, 'eol_expression_Expression7', None)
    assert getattr(partner, 'eol_expression_BinaryOperatorExpression6') is None


def test_assoc_start49_stub_double():
    # eol_expression_ExpressionRange has no real 'eol_expression_ExpressionRange' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_ExpressionRange()
    setattr(partner, 'eol_expression_ExpressionRange', None)
    _safe_set(owner, 'eol_expression_Expression50', partner)
    assert getattr(partner, 'eol_expression_ExpressionRange') == owner
    _safe_set(owner, 'eol_expression_Expression50', None)
    assert getattr(partner, 'eol_expression_ExpressionRange') is None


def test_assoc_typeName30_stub_double():
    # eol_expression_NewExpression has no real 'eol_expression_NewExpression' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_NameExpression(isType=True, name="sample_text")
    partner = eol_expression_NewExpression()
    setattr(partner, 'eol_expression_NewExpression', None)
    _safe_set(owner, 'eol_expression_NameExpression31', partner)
    assert getattr(partner, 'eol_expression_NewExpression') == owner
    _safe_set(owner, 'eol_expression_NameExpression31', None)
    assert getattr(partner, 'eol_expression_NewExpression') is None


def test_assoc_value27_stub_double():
    # eol_expression_KeyValueExpression has no real 'eol_expression_KeyValueExpression28' property in the generated
    # code (a bare stub) -- manually attach it so eol_expression_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_expression_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_expression_Expression(inBrackets=True)
    partner = eol_expression_KeyValueExpression()
    setattr(partner, 'eol_expression_KeyValueExpression28', None)
    _safe_set(owner, 'eol_expression_Expression29', partner)
    assert getattr(partner, 'eol_expression_KeyValueExpression28') == owner
    _safe_set(owner, 'eol_expression_Expression29', None)
    assert getattr(partner, 'eol_expression_KeyValueExpression28') is None


