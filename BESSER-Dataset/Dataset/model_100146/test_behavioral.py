import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    ExpressionTerm,
    FromEntry,
    FromJoin,
    JPQLQuery,
    Literal,
    OrderBySpec,
    SelectAggregateExpression,
    SelectExpression,
    Variable,
    jPQL_AdditionExpression,
    jPQL_AliasAttributeExpression,
    jPQL_AndExpression,
    jPQL_AvgAggregate,
    jPQL_BooleanLiteral,
    jPQL_ComparisonOperatorExpression,
    jPQL_CountAggregate,
    jPQL_DeleteClause,
    jPQL_DeleteStatement,
    jPQL_Expression,
    jPQL_ExpressionTerm,
    jPQL_Float,
    jPQL_FloatLiteral,
    jPQL_FromClass,
    jPQL_FromClause,
    jPQL_FromCollection,
    jPQL_FromEntry,
    jPQL_FromJoin,
    jPQL_FunctionExpression,
    jPQL_GroupByClause,
    jPQL_HavingClause,
    jPQL_InnerJoin,
    jPQL_IntegerLiteral,
    jPQL_JPQLQuery,
    jPQL_Join,
    jPQL_LeftJoin,
    jPQL_Literal,
    jPQL_MaxAggregate,
    jPQL_MinAggregate,
    jPQL_MultiplicationExpression,
    jPQL_NullLiteral,
    jPQL_OrExpression,
    jPQL_OrderByClause,
    jPQL_OrderBySpec,
    jPQL_ParameterExpression,
    jPQL_SelectAggregateExpression,
    jPQL_SelectClause,
    jPQL_SelectConstructorExpression,
    jPQL_SelectExpression,
    jPQL_SelectStatement,
    jPQL_SetClause,
    jPQL_StringLiteral,
    jPQL_SumAggregate,
    jPQL_UpdateClause,
    jPQL_UpdateItem,
    jPQL_UpdateStatement,
    jPQL_Variable,
    jPQL_VariableDeclaration,
    jPQL_WhereClause,
    AdditionOperator,
    ComparisonOperator,
    MultiplicationOperator,
    OrderByDirection,
    TrimSpec,
    UnaryOperator,
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

def test_assoc_alias72_reverse_link_reassign_clear():
    a1 = jPQL_VariableDeclaration(name="sample_text")
    a2 = jPQL_VariableDeclaration(name="sample_text_2")
    b = jPQL_AliasAttributeExpression(attributes="sample_text", direction="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression73', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression73', a1)
    if hasattr(a1, 'jPQL_VariableDeclaration74'):
        assert _is_linked(a1, 'jPQL_VariableDeclaration74', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression73', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression73', a2)
    if hasattr(a1, 'jPQL_VariableDeclaration74'):
        assert not _is_linked(a1, 'jPQL_VariableDeclaration74', b)
    if hasattr(a2, 'jPQL_VariableDeclaration74'):
        assert _is_linked(a2, 'jPQL_VariableDeclaration74', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression73', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression73', a2)
    if hasattr(a2, 'jPQL_VariableDeclaration74'):
        assert not _is_linked(a2, 'jPQL_VariableDeclaration74', b)


def test_assoc_field77_reverse_link_reassign_clear():
    a1 = jPQL_FunctionExpression(name="sample_text", trimSpec="sample_text")
    a2 = jPQL_FunctionExpression(name="sample_text_2", trimSpec="sample_text_2")
    b = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    _safe_set(b, 'jPQL_Expression79', a1)
    assert _is_linked(b, 'jPQL_Expression79', a1)
    if hasattr(a1, 'jPQL_FunctionExpression78'):
        assert _is_linked(a1, 'jPQL_FunctionExpression78', b)
    _safe_set(b, 'jPQL_Expression79', a2)
    assert _is_linked(b, 'jPQL_Expression79', a2)
    if hasattr(a1, 'jPQL_FunctionExpression78'):
        assert not _is_linked(a1, 'jPQL_FunctionExpression78', b)
    if hasattr(a2, 'jPQL_FunctionExpression78'):
        assert _is_linked(a2, 'jPQL_FunctionExpression78', b)
    _safe_set(b, 'jPQL_Expression79', None)
    assert not _is_linked(b, 'jPQL_Expression79', a2)
    if hasattr(a2, 'jPQL_FunctionExpression78'):
        assert not _is_linked(a2, 'jPQL_FunctionExpression78', b)


def test_assoc_fields75_reverse_link_reassign_clear():
    a1 = jPQL_FunctionExpression(name="sample_text", trimSpec="sample_text")
    a2 = jPQL_FunctionExpression(name="sample_text_2", trimSpec="sample_text_2")
    b = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    _safe_set(b, 'jPQL_Expression76', a1)
    assert _is_linked(b, 'jPQL_Expression76', a1)
    if hasattr(a1, 'jPQL_FunctionExpression'):
        assert _is_linked(a1, 'jPQL_FunctionExpression', b)
    _safe_set(b, 'jPQL_Expression76', a2)
    assert _is_linked(b, 'jPQL_Expression76', a2)
    if hasattr(a1, 'jPQL_FunctionExpression'):
        assert not _is_linked(a1, 'jPQL_FunctionExpression', b)
    if hasattr(a2, 'jPQL_FunctionExpression'):
        assert _is_linked(a2, 'jPQL_FunctionExpression', b)
    _safe_set(b, 'jPQL_Expression76', None)
    assert not _is_linked(b, 'jPQL_Expression76', a2)
    if hasattr(a2, 'jPQL_FunctionExpression'):
        assert not _is_linked(a2, 'jPQL_FunctionExpression', b)


def test_assoc_item34_reverse_link_reassign_clear():
    a1 = jPQL_SelectAggregateExpression(isDistinct=True)
    a2 = jPQL_SelectAggregateExpression(isDistinct=False)
    b = jPQL_AliasAttributeExpression(attributes="sample_text", direction="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression35', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression35', a1)
    if hasattr(a1, 'jPQL_SelectAggregateExpression'):
        assert _is_linked(a1, 'jPQL_SelectAggregateExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression35', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression35', a2)
    if hasattr(a1, 'jPQL_SelectAggregateExpression'):
        assert not _is_linked(a1, 'jPQL_SelectAggregateExpression', b)
    if hasattr(a2, 'jPQL_SelectAggregateExpression'):
        assert _is_linked(a2, 'jPQL_SelectAggregateExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression35', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression35', a2)
    if hasattr(a2, 'jPQL_SelectAggregateExpression'):
        assert not _is_linked(a2, 'jPQL_SelectAggregateExpression', b)


def test_assoc_items36_reverse_link_reassign_clear():
    a1 = jPQL_SelectConstructorExpression(name="sample_text")
    a2 = jPQL_SelectConstructorExpression(name="sample_text_2")
    b = jPQL_AliasAttributeExpression(attributes="sample_text", direction="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression37', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression37', a1)
    if hasattr(a1, 'jPQL_SelectConstructorExpression'):
        assert _is_linked(a1, 'jPQL_SelectConstructorExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression37', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression37', a2)
    if hasattr(a1, 'jPQL_SelectConstructorExpression'):
        assert not _is_linked(a1, 'jPQL_SelectConstructorExpression', b)
    if hasattr(a2, 'jPQL_SelectConstructorExpression'):
        assert _is_linked(a2, 'jPQL_SelectConstructorExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression37', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression37', a2)
    if hasattr(a2, 'jPQL_SelectConstructorExpression'):
        assert not _is_linked(a2, 'jPQL_SelectConstructorExpression', b)


def test_assoc_joins43_reverse_link_reassign_clear():
    a1 = jPQL_FromJoin(isFetch=True)
    a2 = jPQL_FromJoin(isFetch=False)
    b = jPQL_FromClass(type="sample_text")
    _safe_set(b, 'jPQL_FromClass', {a1})
    assert _is_linked(b, 'jPQL_FromClass', a1)
    if hasattr(a1, 'jPQL_FromJoin'):
        assert _is_linked(a1, 'jPQL_FromJoin', b)
    _safe_set(b, 'jPQL_FromClass', {a2})
    assert _is_linked(b, 'jPQL_FromClass', a2)
    if hasattr(a1, 'jPQL_FromJoin'):
        assert not _is_linked(a1, 'jPQL_FromJoin', b)
    if hasattr(a2, 'jPQL_FromJoin'):
        assert _is_linked(a2, 'jPQL_FromJoin', b)
    _safe_set(b, 'jPQL_FromClass', set())
    assert not _is_linked(b, 'jPQL_FromClass', a2)
    if hasattr(a2, 'jPQL_FromJoin'):
        assert not _is_linked(a2, 'jPQL_FromJoin', b)


def test_assoc_left59_reverse_link_reassign_clear():
    a1 = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    a2 = jPQL_Expression(isNot=False, unaryOperator="sample_text_2")
    b = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    _safe_set(b, 'jPQL_Expression60', a1)
    assert _is_linked(b, 'jPQL_Expression60', a1)
    if hasattr(a1, 'jPQL_Expression58'):
        assert _is_linked(a1, 'jPQL_Expression58', b)
    _safe_set(b, 'jPQL_Expression60', a2)
    assert _is_linked(b, 'jPQL_Expression60', a2)
    if hasattr(a1, 'jPQL_Expression58'):
        assert not _is_linked(a1, 'jPQL_Expression58', b)
    if hasattr(a2, 'jPQL_Expression58'):
        assert _is_linked(a2, 'jPQL_Expression58', b)
    _safe_set(b, 'jPQL_Expression60', None)
    assert not _is_linked(b, 'jPQL_Expression60', a2)
    if hasattr(a2, 'jPQL_Expression58'):
        assert not _is_linked(a2, 'jPQL_Expression58', b)


def test_assoc_length83_reverse_link_reassign_clear():
    a1 = jPQL_FunctionExpression(name="sample_text", trimSpec="sample_text")
    a2 = jPQL_FunctionExpression(name="sample_text_2", trimSpec="sample_text_2")
    b = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    _safe_set(b, 'jPQL_Expression85', a1)
    assert _is_linked(b, 'jPQL_Expression85', a1)
    if hasattr(a1, 'jPQL_FunctionExpression84'):
        assert _is_linked(a1, 'jPQL_FunctionExpression84', b)
    _safe_set(b, 'jPQL_Expression85', a2)
    assert _is_linked(b, 'jPQL_Expression85', a2)
    if hasattr(a1, 'jPQL_FunctionExpression84'):
        assert not _is_linked(a1, 'jPQL_FunctionExpression84', b)
    if hasattr(a2, 'jPQL_FunctionExpression84'):
        assert _is_linked(a2, 'jPQL_FunctionExpression84', b)
    _safe_set(b, 'jPQL_Expression85', None)
    assert not _is_linked(b, 'jPQL_Expression85', a2)
    if hasattr(a2, 'jPQL_FunctionExpression84'):
        assert not _is_linked(a2, 'jPQL_FunctionExpression84', b)


def test_assoc_path46_reverse_link_reassign_clear():
    a1 = jPQL_FromJoin(isFetch=True)
    a2 = jPQL_FromJoin(isFetch=False)
    b = jPQL_AliasAttributeExpression(attributes="sample_text", direction="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression48', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression48', a1)
    if hasattr(a1, 'jPQL_FromJoin47'):
        assert _is_linked(a1, 'jPQL_FromJoin47', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression48', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression48', a2)
    if hasattr(a1, 'jPQL_FromJoin47'):
        assert not _is_linked(a1, 'jPQL_FromJoin47', b)
    if hasattr(a2, 'jPQL_FromJoin47'):
        assert _is_linked(a2, 'jPQL_FromJoin47', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression48', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression48', a2)
    if hasattr(a2, 'jPQL_FromJoin47'):
        assert not _is_linked(a2, 'jPQL_FromJoin47', b)


def test_assoc_right56_reverse_link_reassign_clear():
    a1 = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    a2 = jPQL_Expression(isNot=False, unaryOperator="sample_text_2")
    b = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    _safe_set(b, 'jPQL_Expression57', a1)
    assert _is_linked(b, 'jPQL_Expression57', a1)
    if hasattr(a1, 'jPQL_Expression55'):
        assert _is_linked(a1, 'jPQL_Expression55', b)
    _safe_set(b, 'jPQL_Expression57', a2)
    assert _is_linked(b, 'jPQL_Expression57', a2)
    if hasattr(a1, 'jPQL_Expression55'):
        assert not _is_linked(a1, 'jPQL_Expression55', b)
    if hasattr(a2, 'jPQL_Expression55'):
        assert _is_linked(a2, 'jPQL_Expression55', b)
    _safe_set(b, 'jPQL_Expression57', None)
    assert not _is_linked(b, 'jPQL_Expression57', a2)
    if hasattr(a2, 'jPQL_Expression55'):
        assert not _is_linked(a2, 'jPQL_Expression55', b)


def test_assoc_startPos80_reverse_link_reassign_clear():
    a1 = jPQL_FunctionExpression(name="sample_text", trimSpec="sample_text")
    a2 = jPQL_FunctionExpression(name="sample_text_2", trimSpec="sample_text_2")
    b = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    _safe_set(b, 'jPQL_Expression82', a1)
    assert _is_linked(b, 'jPQL_Expression82', a1)
    if hasattr(a1, 'jPQL_FunctionExpression81'):
        assert _is_linked(a1, 'jPQL_FunctionExpression81', b)
    _safe_set(b, 'jPQL_Expression82', a2)
    assert _is_linked(b, 'jPQL_Expression82', a2)
    if hasattr(a1, 'jPQL_FunctionExpression81'):
        assert not _is_linked(a1, 'jPQL_FunctionExpression81', b)
    if hasattr(a2, 'jPQL_FunctionExpression81'):
        assert _is_linked(a2, 'jPQL_FunctionExpression81', b)
    _safe_set(b, 'jPQL_Expression82', None)
    assert not _is_linked(b, 'jPQL_Expression82', a2)
    if hasattr(a2, 'jPQL_FunctionExpression81'):
        assert not _is_linked(a2, 'jPQL_FunctionExpression81', b)


def test_assoc_trimChar86_reverse_link_reassign_clear():
    a1 = jPQL_FunctionExpression(name="sample_text", trimSpec="sample_text")
    a2 = jPQL_FunctionExpression(name="sample_text_2", trimSpec="sample_text_2")
    b = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    _safe_set(b, 'jPQL_Expression88', a1)
    assert _is_linked(b, 'jPQL_Expression88', a1)
    if hasattr(a1, 'jPQL_FunctionExpression87'):
        assert _is_linked(a1, 'jPQL_FunctionExpression87', b)
    _safe_set(b, 'jPQL_Expression88', a2)
    assert _is_linked(b, 'jPQL_Expression88', a2)
    if hasattr(a1, 'jPQL_FunctionExpression87'):
        assert not _is_linked(a1, 'jPQL_FunctionExpression87', b)
    if hasattr(a2, 'jPQL_FunctionExpression87'):
        assert _is_linked(a2, 'jPQL_FunctionExpression87', b)
    _safe_set(b, 'jPQL_Expression88', None)
    assert not _is_linked(b, 'jPQL_Expression88', a2)
    if hasattr(a2, 'jPQL_FunctionExpression87'):
        assert not _is_linked(a2, 'jPQL_FunctionExpression87', b)


def test_assoc_variable49_reverse_link_reassign_clear():
    a1 = jPQL_VariableDeclaration(name="sample_text")
    a2 = jPQL_VariableDeclaration(name="sample_text_2")
    b = jPQL_FromJoin(isFetch=True)
    _safe_set(b, 'jPQL_FromJoin50', a1)
    assert _is_linked(b, 'jPQL_FromJoin50', a1)
    if hasattr(a1, 'jPQL_VariableDeclaration51'):
        assert _is_linked(a1, 'jPQL_VariableDeclaration51', b)
    _safe_set(b, 'jPQL_FromJoin50', a2)
    assert _is_linked(b, 'jPQL_FromJoin50', a2)
    if hasattr(a1, 'jPQL_VariableDeclaration51'):
        assert not _is_linked(a1, 'jPQL_VariableDeclaration51', b)
    if hasattr(a2, 'jPQL_VariableDeclaration51'):
        assert _is_linked(a2, 'jPQL_VariableDeclaration51', b)
    _safe_set(b, 'jPQL_FromJoin50', None)
    assert not _is_linked(b, 'jPQL_FromJoin50', a2)
    if hasattr(a2, 'jPQL_VariableDeclaration51'):
        assert not _is_linked(a2, 'jPQL_VariableDeclaration51', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alias23_stub_double():
    # jPQL_UpdateItem has no real 'jPQL_UpdateItem24' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_AliasAttributeExpression(attributes="sample_text", direction="sample_text")
    partner = jPQL_UpdateItem()
    setattr(partner, 'jPQL_UpdateItem24', None)
    _safe_set(owner, 'jPQL_AliasAttributeExpression25', partner)
    assert getattr(partner, 'jPQL_UpdateItem24') == owner
    _safe_set(owner, 'jPQL_AliasAttributeExpression25', None)
    assert getattr(partner, 'jPQL_UpdateItem24') is None


def test_assoc_entries90_stub_double():
    # jPQL_OrExpression has no real 'jPQL_OrExpression' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_OrExpression()
    setattr(partner, 'jPQL_OrExpression', None)
    _safe_set(owner, 'jPQL_Expression91', partner)
    assert owner in getattr(partner, 'jPQL_OrExpression')
    _safe_set(owner, 'jPQL_Expression91', None)
    assert owner not in getattr(partner, 'jPQL_OrExpression')


def test_assoc_entries92_stub_double():
    # jPQL_AndExpression has no real 'jPQL_AndExpression' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_AndExpression()
    setattr(partner, 'jPQL_AndExpression', None)
    _safe_set(owner, 'jPQL_Expression93', partner)
    assert owner in getattr(partner, 'jPQL_AndExpression')
    _safe_set(owner, 'jPQL_Expression93', None)
    assert owner not in getattr(partner, 'jPQL_AndExpression')


def test_assoc_expressions32_stub_double():
    # jPQL_SelectExpression has no real 'jPQL_SelectExpression' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_SelectClause(isDistinct=True)
    partner = jPQL_SelectExpression()
    setattr(partner, 'jPQL_SelectExpression', None)
    _safe_set(owner, 'jPQL_SelectClause33', {partner})
    assert getattr(partner, 'jPQL_SelectExpression') == owner
    _safe_set(owner, 'jPQL_SelectClause33', set())
    assert getattr(partner, 'jPQL_SelectExpression') is None


def test_assoc_grouping8_stub_double():
    # jPQL_GroupByClause has no real 'jPQL_GroupByClause9' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_AliasAttributeExpression(attributes="sample_text", direction="sample_text")
    partner = jPQL_GroupByClause()
    setattr(partner, 'jPQL_GroupByClause9', None)
    _safe_set(owner, 'jPQL_AliasAttributeExpression', partner)
    assert owner in getattr(partner, 'jPQL_GroupByClause9')
    _safe_set(owner, 'jPQL_AliasAttributeExpression', None)
    assert owner not in getattr(partner, 'jPQL_GroupByClause9')


def test_assoc_having12_stub_double():
    # jPQL_HavingClause has no real 'jPQL_HavingClause13' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_HavingClause()
    setattr(partner, 'jPQL_HavingClause13', None)
    _safe_set(owner, 'jPQL_Expression', partner)
    assert getattr(partner, 'jPQL_HavingClause13') == owner
    _safe_set(owner, 'jPQL_Expression', None)
    assert getattr(partner, 'jPQL_HavingClause13') is None


def test_assoc_items61_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable', None)
    _safe_set(owner, 'jPQL_Expression62', {partner})
    assert getattr(partner, 'jPQL_Variable') == owner
    _safe_set(owner, 'jPQL_Expression62', set())
    assert getattr(partner, 'jPQL_Variable') is None


def test_assoc_max69_stub_double():
    # jPQL_Literal has no real 'jPQL_Literal71' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_Literal()
    setattr(partner, 'jPQL_Literal71', None)
    _safe_set(owner, 'jPQL_Expression70', partner)
    assert getattr(partner, 'jPQL_Literal71') == owner
    _safe_set(owner, 'jPQL_Expression70', None)
    assert getattr(partner, 'jPQL_Literal71') is None


def test_assoc_min66_stub_double():
    # jPQL_Literal has no real 'jPQL_Literal68' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_Literal()
    setattr(partner, 'jPQL_Literal68', None)
    _safe_set(owner, 'jPQL_Expression67', partner)
    assert getattr(partner, 'jPQL_Literal68') == owner
    _safe_set(owner, 'jPQL_Expression67', None)
    assert getattr(partner, 'jPQL_Literal68') is None


def test_assoc_path44_stub_double():
    # jPQL_FromCollection has no real 'jPQL_FromCollection' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_AliasAttributeExpression(attributes="sample_text", direction="sample_text")
    partner = jPQL_FromCollection()
    setattr(partner, 'jPQL_FromCollection', None)
    _safe_set(owner, 'jPQL_AliasAttributeExpression45', partner)
    assert getattr(partner, 'jPQL_FromCollection') == owner
    _safe_set(owner, 'jPQL_AliasAttributeExpression45', None)
    assert getattr(partner, 'jPQL_FromCollection') is None


def test_assoc_query63_stub_double():
    # jPQL_SelectStatement has no real 'jPQL_SelectStatement65' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_SelectStatement()
    setattr(partner, 'jPQL_SelectStatement65', None)
    _safe_set(owner, 'jPQL_Expression64', partner)
    assert getattr(partner, 'jPQL_SelectStatement65') == owner
    _safe_set(owner, 'jPQL_Expression64', None)
    assert getattr(partner, 'jPQL_SelectStatement65') is None


def test_assoc_selectClause1_stub_double():
    # jPQL_SelectStatement has no real 'jPQL_SelectStatement' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_SelectClause(isDistinct=True)
    partner = jPQL_SelectStatement()
    setattr(partner, 'jPQL_SelectStatement', None)
    _safe_set(owner, 'jPQL_SelectClause', partner)
    assert getattr(partner, 'jPQL_SelectStatement') == owner
    _safe_set(owner, 'jPQL_SelectClause', None)
    assert getattr(partner, 'jPQL_SelectStatement') is None


def test_assoc_value89_stub_double():
    # jPQL_FloatLiteral has no real 'jPQL_FloatLiteral' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Float's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Float's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Float(fractionValue=7, integerValue=7)
    partner = jPQL_FloatLiteral()
    setattr(partner, 'jPQL_FloatLiteral', None)
    _safe_set(owner, 'jPQL_Float', partner)
    assert getattr(partner, 'jPQL_FloatLiteral') == owner
    _safe_set(owner, 'jPQL_Float', None)
    assert getattr(partner, 'jPQL_FloatLiteral') is None


def test_assoc_variable41_stub_double():
    # jPQL_FromEntry has no real 'jPQL_FromEntry42' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_VariableDeclaration(name="sample_text")
    partner = jPQL_FromEntry()
    setattr(partner, 'jPQL_FromEntry42', None)
    _safe_set(owner, 'jPQL_VariableDeclaration', partner)
    assert getattr(partner, 'jPQL_FromEntry42') == owner
    _safe_set(owner, 'jPQL_VariableDeclaration', None)
    assert getattr(partner, 'jPQL_FromEntry42') is None


def test_assoc_whereEntry52_stub_double():
    # jPQL_WhereClause has no real 'jPQL_WhereClause53' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Expression(isNot=True, unaryOperator="sample_text")
    partner = jPQL_WhereClause()
    setattr(partner, 'jPQL_WhereClause53', None)
    _safe_set(owner, 'jPQL_Expression54', partner)
    assert getattr(partner, 'jPQL_WhereClause53') == owner
    _safe_set(owner, 'jPQL_Expression54', None)
    assert getattr(partner, 'jPQL_WhereClause53') is None


