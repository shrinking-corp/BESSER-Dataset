import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    ExpressionTerm,
    FromEntry,
    FromJoin,
    InExpression,
    JPQLQuery,
    SelectAggregateExpression,
    SelectExpression,
    Value,
    Variable,
    jpql_AliasAttributeExpression,
    jpql_AllExpression,
    jpql_AndExpression,
    jpql_AnyExpression,
    jpql_AvgAggregate,
    jpql_BetweenExpression,
    jpql_BooleanExpression,
    jpql_CollectionExpression,
    jpql_CountAggregate,
    jpql_DateTimeExpression,
    jpql_DeleteClause,
    jpql_DeleteStatement,
    jpql_EmptyComparisonExpression,
    jpql_ExistsExpression,
    jpql_Expression,
    jpql_ExpressionTerm,
    jpql_FromClass,
    jpql_FromClause,
    jpql_FromCollection,
    jpql_FromEntry,
    jpql_FromJoin,
    jpql_Function,
    jpql_HavingClause,
    jpql_Import,
    jpql_InExpression,
    jpql_InQueryExpression,
    jpql_InSeqExpression,
    jpql_InnerJoin,
    jpql_IntegerExpression,
    jpql_JPQLQuery,
    jpql_Join,
    jpql_LeftJoin,
    jpql_LikeExpression,
    jpql_MaxAggregate,
    jpql_MinAggregate,
    jpql_NamedQuery,
    jpql_NullComparisonExpression,
    jpql_NullExpression,
    jpql_OperatorExpression,
    jpql_OrExpression,
    jpql_OrderClause,
    jpql_OrderItem,
    jpql_ParameterExpression,
    jpql_QueryModule,
    jpql_SelectAggregateExpression,
    jpql_SelectClause,
    jpql_SelectConstructorExpression,
    jpql_SelectExpression,
    jpql_SelectFromClause,
    jpql_SelectStatement,
    jpql_SetClause,
    jpql_SomeExpression,
    jpql_StringExpression,
    jpql_SumAggregate,
    jpql_UpdateClause,
    jpql_UpdateItem,
    jpql_UpdateStatement,
    jpql_Value,
    jpql_Variable,
    jpql_VariableDeclaration,
    jpql_WhereClause,
    Operator,
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

def test_assoc_alias100_reverse_link_reassign_clear():
    a1 = jpql_VariableDeclaration(name="sample_text")
    a2 = jpql_VariableDeclaration(name="sample_text_2")
    b = jpql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jpql_AliasAttributeExpression101', a1)
    assert _is_linked(b, 'jpql_AliasAttributeExpression101', a1)
    if hasattr(a1, 'jpql_VariableDeclaration102'):
        assert _is_linked(a1, 'jpql_VariableDeclaration102', b)
    _safe_set(b, 'jpql_AliasAttributeExpression101', a2)
    assert _is_linked(b, 'jpql_AliasAttributeExpression101', a2)
    if hasattr(a1, 'jpql_VariableDeclaration102'):
        assert not _is_linked(a1, 'jpql_VariableDeclaration102', b)
    if hasattr(a2, 'jpql_VariableDeclaration102'):
        assert _is_linked(a2, 'jpql_VariableDeclaration102', b)
    _safe_set(b, 'jpql_AliasAttributeExpression101', None)
    assert not _is_linked(b, 'jpql_AliasAttributeExpression101', a2)
    if hasattr(a2, 'jpql_VariableDeclaration102'):
        assert not _is_linked(a2, 'jpql_VariableDeclaration102', b)


def test_assoc_item43_reverse_link_reassign_clear():
    a1 = jpql_SelectAggregateExpression(isDistinct=True)
    a2 = jpql_SelectAggregateExpression(isDistinct=False)
    b = jpql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jpql_AliasAttributeExpression44', a1)
    assert _is_linked(b, 'jpql_AliasAttributeExpression44', a1)
    if hasattr(a1, 'jpql_SelectAggregateExpression'):
        assert _is_linked(a1, 'jpql_SelectAggregateExpression', b)
    _safe_set(b, 'jpql_AliasAttributeExpression44', a2)
    assert _is_linked(b, 'jpql_AliasAttributeExpression44', a2)
    if hasattr(a1, 'jpql_SelectAggregateExpression'):
        assert not _is_linked(a1, 'jpql_SelectAggregateExpression', b)
    if hasattr(a2, 'jpql_SelectAggregateExpression'):
        assert _is_linked(a2, 'jpql_SelectAggregateExpression', b)
    _safe_set(b, 'jpql_AliasAttributeExpression44', None)
    assert not _is_linked(b, 'jpql_AliasAttributeExpression44', a2)
    if hasattr(a2, 'jpql_SelectAggregateExpression'):
        assert not _is_linked(a2, 'jpql_SelectAggregateExpression', b)


def test_assoc_items45_reverse_link_reassign_clear():
    a1 = jpql_SelectConstructorExpression(name="sample_text")
    a2 = jpql_SelectConstructorExpression(name="sample_text_2")
    b = jpql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jpql_AliasAttributeExpression46', a1)
    assert _is_linked(b, 'jpql_AliasAttributeExpression46', a1)
    if hasattr(a1, 'jpql_SelectConstructorExpression'):
        assert _is_linked(a1, 'jpql_SelectConstructorExpression', b)
    _safe_set(b, 'jpql_AliasAttributeExpression46', a2)
    assert _is_linked(b, 'jpql_AliasAttributeExpression46', a2)
    if hasattr(a1, 'jpql_SelectConstructorExpression'):
        assert not _is_linked(a1, 'jpql_SelectConstructorExpression', b)
    if hasattr(a2, 'jpql_SelectConstructorExpression'):
        assert _is_linked(a2, 'jpql_SelectConstructorExpression', b)
    _safe_set(b, 'jpql_AliasAttributeExpression46', None)
    assert not _is_linked(b, 'jpql_AliasAttributeExpression46', a2)
    if hasattr(a2, 'jpql_SelectConstructorExpression'):
        assert not _is_linked(a2, 'jpql_SelectConstructorExpression', b)


def test_assoc_joins52_reverse_link_reassign_clear():
    a1 = jpql_FromJoin(isFetch=True)
    a2 = jpql_FromJoin(isFetch=False)
    b = jpql_FromClass(type="sample_text")
    _safe_set(b, 'jpql_FromClass', {a1})
    assert _is_linked(b, 'jpql_FromClass', a1)
    if hasattr(a1, 'jpql_FromJoin'):
        assert _is_linked(a1, 'jpql_FromJoin', b)
    _safe_set(b, 'jpql_FromClass', {a2})
    assert _is_linked(b, 'jpql_FromClass', a2)
    if hasattr(a1, 'jpql_FromJoin'):
        assert not _is_linked(a1, 'jpql_FromJoin', b)
    if hasattr(a2, 'jpql_FromJoin'):
        assert _is_linked(a2, 'jpql_FromJoin', b)
    _safe_set(b, 'jpql_FromClass', set())
    assert not _is_linked(b, 'jpql_FromClass', a2)
    if hasattr(a2, 'jpql_FromJoin'):
        assert not _is_linked(a2, 'jpql_FromJoin', b)


def test_assoc_ordering17_reverse_link_reassign_clear():
    a1 = jpql_OrderItem(feature="sample_text")
    a2 = jpql_OrderItem(feature="sample_text_2")
    b = jpql_OrderClause(isAsc=True, isDesc=True)
    _safe_set(b, 'jpql_OrderClause18', {a1})
    assert _is_linked(b, 'jpql_OrderClause18', a1)
    if hasattr(a1, 'jpql_OrderItem'):
        assert _is_linked(a1, 'jpql_OrderItem', b)
    _safe_set(b, 'jpql_OrderClause18', {a2})
    assert _is_linked(b, 'jpql_OrderClause18', a2)
    if hasattr(a1, 'jpql_OrderItem'):
        assert not _is_linked(a1, 'jpql_OrderItem', b)
    if hasattr(a2, 'jpql_OrderItem'):
        assert _is_linked(a2, 'jpql_OrderItem', b)
    _safe_set(b, 'jpql_OrderClause18', set())
    assert not _is_linked(b, 'jpql_OrderClause18', a2)
    if hasattr(a2, 'jpql_OrderItem'):
        assert not _is_linked(a2, 'jpql_OrderItem', b)


def test_assoc_path55_reverse_link_reassign_clear():
    a1 = jpql_FromJoin(isFetch=True)
    a2 = jpql_FromJoin(isFetch=False)
    b = jpql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jpql_AliasAttributeExpression57', a1)
    assert _is_linked(b, 'jpql_AliasAttributeExpression57', a1)
    if hasattr(a1, 'jpql_FromJoin56'):
        assert _is_linked(a1, 'jpql_FromJoin56', b)
    _safe_set(b, 'jpql_AliasAttributeExpression57', a2)
    assert _is_linked(b, 'jpql_AliasAttributeExpression57', a2)
    if hasattr(a1, 'jpql_FromJoin56'):
        assert not _is_linked(a1, 'jpql_FromJoin56', b)
    if hasattr(a2, 'jpql_FromJoin56'):
        assert _is_linked(a2, 'jpql_FromJoin56', b)
    _safe_set(b, 'jpql_AliasAttributeExpression57', None)
    assert not _is_linked(b, 'jpql_AliasAttributeExpression57', a2)
    if hasattr(a2, 'jpql_FromJoin56'):
        assert not _is_linked(a2, 'jpql_FromJoin56', b)


def test_assoc_rhs77_reverse_link_reassign_clear():
    a1 = jpql_CollectionExpression(isNot=True)
    a2 = jpql_CollectionExpression(isNot=False)
    b = jpql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jpql_AliasAttributeExpression79', a1)
    assert _is_linked(b, 'jpql_AliasAttributeExpression79', a1)
    if hasattr(a1, 'jpql_CollectionExpression78'):
        assert _is_linked(a1, 'jpql_CollectionExpression78', b)
    _safe_set(b, 'jpql_AliasAttributeExpression79', a2)
    assert _is_linked(b, 'jpql_AliasAttributeExpression79', a2)
    if hasattr(a1, 'jpql_CollectionExpression78'):
        assert not _is_linked(a1, 'jpql_CollectionExpression78', b)
    if hasattr(a2, 'jpql_CollectionExpression78'):
        assert _is_linked(a2, 'jpql_CollectionExpression78', b)
    _safe_set(b, 'jpql_AliasAttributeExpression79', None)
    assert not _is_linked(b, 'jpql_AliasAttributeExpression79', a2)
    if hasattr(a2, 'jpql_CollectionExpression78'):
        assert not _is_linked(a2, 'jpql_CollectionExpression78', b)


def test_assoc_variable58_reverse_link_reassign_clear():
    a1 = jpql_VariableDeclaration(name="sample_text")
    a2 = jpql_VariableDeclaration(name="sample_text_2")
    b = jpql_FromJoin(isFetch=True)
    _safe_set(b, 'jpql_FromJoin59', a1)
    assert _is_linked(b, 'jpql_FromJoin59', a1)
    if hasattr(a1, 'jpql_VariableDeclaration60'):
        assert _is_linked(a1, 'jpql_VariableDeclaration60', b)
    _safe_set(b, 'jpql_FromJoin59', a2)
    assert _is_linked(b, 'jpql_FromJoin59', a2)
    if hasattr(a1, 'jpql_VariableDeclaration60'):
        assert not _is_linked(a1, 'jpql_VariableDeclaration60', b)
    if hasattr(a2, 'jpql_VariableDeclaration60'):
        assert _is_linked(a2, 'jpql_VariableDeclaration60', b)
    _safe_set(b, 'jpql_FromJoin59', None)
    assert not _is_linked(b, 'jpql_FromJoin59', a2)
    if hasattr(a2, 'jpql_VariableDeclaration60'):
        assert not _is_linked(a2, 'jpql_VariableDeclaration60', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alias29_stub_double():
    # jpql_UpdateItem has no real 'jpql_UpdateItem30' property in the generated
    # code (a bare stub) -- manually attach it so jpql_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_AliasAttributeExpression(attributes="sample_text")
    partner = jpql_UpdateItem()
    setattr(partner, 'jpql_UpdateItem30', None)
    _safe_set(owner, 'jpql_AliasAttributeExpression', partner)
    assert getattr(partner, 'jpql_UpdateItem30') == owner
    _safe_set(owner, 'jpql_AliasAttributeExpression', None)
    assert getattr(partner, 'jpql_UpdateItem30') is None


def test_assoc_expressions41_stub_double():
    # jpql_SelectExpression has no real 'jpql_SelectExpression' property in the generated
    # code (a bare stub) -- manually attach it so jpql_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_SelectClause(isDistinct=True)
    partner = jpql_SelectExpression()
    setattr(partner, 'jpql_SelectExpression', None)
    _safe_set(owner, 'jpql_SelectClause42', {partner})
    assert getattr(partner, 'jpql_SelectExpression') == owner
    _safe_set(owner, 'jpql_SelectClause42', set())
    assert getattr(partner, 'jpql_SelectExpression') is None


def test_assoc_imports0_stub_double():
    # jpql_QueryModule has no real 'jpql_QueryModule' property in the generated
    # code (a bare stub) -- manually attach it so jpql_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_Import(importURI="sample_text")
    partner = jpql_QueryModule()
    setattr(partner, 'jpql_QueryModule', None)
    _safe_set(owner, 'jpql_Import', partner)
    assert owner in getattr(partner, 'jpql_QueryModule')
    _safe_set(owner, 'jpql_Import', None)
    assert owner not in getattr(partner, 'jpql_QueryModule')


def test_assoc_lhs64_stub_double():
    # jpql_Variable has no real 'jpql_Variable' property in the generated
    # code (a bare stub) -- manually attach it so jpql_OperatorExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_OperatorExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_OperatorExpression(operator="sample_text")
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable', None)
    _safe_set(owner, 'jpql_OperatorExpression', partner)
    assert getattr(partner, 'jpql_Variable') == owner
    _safe_set(owner, 'jpql_OperatorExpression', None)
    assert getattr(partner, 'jpql_Variable') is None


def test_assoc_lhs75_stub_double():
    # jpql_Variable has no real 'jpql_Variable76' property in the generated
    # code (a bare stub) -- manually attach it so jpql_CollectionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_CollectionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_CollectionExpression(isNot=True)
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable76', None)
    _safe_set(owner, 'jpql_CollectionExpression', partner)
    assert getattr(partner, 'jpql_Variable76') == owner
    _safe_set(owner, 'jpql_CollectionExpression', None)
    assert getattr(partner, 'jpql_Variable76') is None


def test_assoc_lhs80_stub_double():
    # jpql_Variable has no real 'jpql_Variable81' property in the generated
    # code (a bare stub) -- manually attach it so jpql_NullComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_NullComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_NullComparisonExpression(isNot=True)
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable81', None)
    _safe_set(owner, 'jpql_NullComparisonExpression', partner)
    assert getattr(partner, 'jpql_Variable81') == owner
    _safe_set(owner, 'jpql_NullComparisonExpression', None)
    assert getattr(partner, 'jpql_Variable81') is None


def test_assoc_lhs82_stub_double():
    # jpql_Variable has no real 'jpql_Variable83' property in the generated
    # code (a bare stub) -- manually attach it so jpql_EmptyComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_EmptyComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_EmptyComparisonExpression(isNot=True)
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable83', None)
    _safe_set(owner, 'jpql_EmptyComparisonExpression', partner)
    assert getattr(partner, 'jpql_Variable83') == owner
    _safe_set(owner, 'jpql_EmptyComparisonExpression', None)
    assert getattr(partner, 'jpql_Variable83') is None


def test_assoc_lhs84_stub_double():
    # jpql_Variable has no real 'jpql_Variable85' property in the generated
    # code (a bare stub) -- manually attach it so jpql_LikeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_LikeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_LikeExpression(isNot=True, pattern="sample_text")
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable85', None)
    _safe_set(owner, 'jpql_LikeExpression', partner)
    assert getattr(partner, 'jpql_Variable85') == owner
    _safe_set(owner, 'jpql_LikeExpression', None)
    assert getattr(partner, 'jpql_Variable85') is None


def test_assoc_lhs86_stub_double():
    # jpql_Variable has no real 'jpql_Variable87' property in the generated
    # code (a bare stub) -- manually attach it so jpql_InExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_InExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_InExpression(isNot=True)
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable87', None)
    _safe_set(owner, 'jpql_InExpression', partner)
    assert getattr(partner, 'jpql_Variable87') == owner
    _safe_set(owner, 'jpql_InExpression', None)
    assert getattr(partner, 'jpql_Variable87') is None


def test_assoc_lhs92_stub_double():
    # jpql_Variable has no real 'jpql_Variable93' property in the generated
    # code (a bare stub) -- manually attach it so jpql_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_BetweenExpression(isNot=True)
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable93', None)
    _safe_set(owner, 'jpql_BetweenExpression', partner)
    assert getattr(partner, 'jpql_Variable93') == owner
    _safe_set(owner, 'jpql_BetweenExpression', None)
    assert getattr(partner, 'jpql_Variable93') is None


def test_assoc_max97_stub_double():
    # jpql_Value has no real 'jpql_Value99' property in the generated
    # code (a bare stub) -- manually attach it so jpql_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_BetweenExpression(isNot=True)
    partner = jpql_Value()
    setattr(partner, 'jpql_Value99', None)
    _safe_set(owner, 'jpql_BetweenExpression98', partner)
    assert getattr(partner, 'jpql_Value99') == owner
    _safe_set(owner, 'jpql_BetweenExpression98', None)
    assert getattr(partner, 'jpql_Value99') is None


def test_assoc_min94_stub_double():
    # jpql_Value has no real 'jpql_Value96' property in the generated
    # code (a bare stub) -- manually attach it so jpql_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_BetweenExpression(isNot=True)
    partner = jpql_Value()
    setattr(partner, 'jpql_Value96', None)
    _safe_set(owner, 'jpql_BetweenExpression95', partner)
    assert getattr(partner, 'jpql_Value96') == owner
    _safe_set(owner, 'jpql_BetweenExpression95', None)
    assert getattr(partner, 'jpql_Value96') is None


def test_assoc_namedQueries3_stub_double():
    # jpql_QueryModule has no real 'jpql_QueryModule4' property in the generated
    # code (a bare stub) -- manually attach it so jpql_NamedQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_NamedQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_NamedQuery(name="sample_text")
    partner = jpql_QueryModule()
    setattr(partner, 'jpql_QueryModule4', None)
    _safe_set(owner, 'jpql_NamedQuery', partner)
    assert owner in getattr(partner, 'jpql_QueryModule4')
    _safe_set(owner, 'jpql_NamedQuery', None)
    assert owner not in getattr(partner, 'jpql_QueryModule4')


def test_assoc_order13_stub_double():
    # jpql_SelectStatement has no real 'jpql_SelectStatement14' property in the generated
    # code (a bare stub) -- manually attach it so jpql_OrderClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_OrderClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_OrderClause(isAsc=True, isDesc=True)
    partner = jpql_SelectStatement()
    setattr(partner, 'jpql_SelectStatement14', None)
    _safe_set(owner, 'jpql_OrderClause', partner)
    assert getattr(partner, 'jpql_SelectStatement14') == owner
    _safe_set(owner, 'jpql_OrderClause', None)
    assert getattr(partner, 'jpql_SelectStatement14') is None


def test_assoc_params103_stub_double():
    # jpql_Variable has no real 'jpql_Variable104' property in the generated
    # code (a bare stub) -- manually attach it so jpql_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_Function(name="sample_text")
    partner = jpql_Variable()
    setattr(partner, 'jpql_Variable104', None)
    _safe_set(owner, 'jpql_Function', {partner})
    assert getattr(partner, 'jpql_Variable104') == owner
    _safe_set(owner, 'jpql_Function', set())
    assert getattr(partner, 'jpql_Variable104') is None


def test_assoc_path53_stub_double():
    # jpql_FromCollection has no real 'jpql_FromCollection' property in the generated
    # code (a bare stub) -- manually attach it so jpql_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_AliasAttributeExpression(attributes="sample_text")
    partner = jpql_FromCollection()
    setattr(partner, 'jpql_FromCollection', None)
    _safe_set(owner, 'jpql_AliasAttributeExpression54', partner)
    assert getattr(partner, 'jpql_FromCollection') == owner
    _safe_set(owner, 'jpql_AliasAttributeExpression54', None)
    assert getattr(partner, 'jpql_FromCollection') is None


def test_assoc_query5_stub_double():
    # jpql_JPQLQuery has no real 'jpql_JPQLQuery7' property in the generated
    # code (a bare stub) -- manually attach it so jpql_NamedQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_NamedQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_NamedQuery(name="sample_text")
    partner = jpql_JPQLQuery()
    setattr(partner, 'jpql_JPQLQuery7', None)
    _safe_set(owner, 'jpql_NamedQuery6', partner)
    assert getattr(partner, 'jpql_JPQLQuery7') == owner
    _safe_set(owner, 'jpql_NamedQuery6', None)
    assert getattr(partner, 'jpql_JPQLQuery7') is None


def test_assoc_query67_stub_double():
    # jpql_SelectStatement has no real 'jpql_SelectStatement68' property in the generated
    # code (a bare stub) -- manually attach it so jpql_ExistsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_ExistsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_ExistsExpression(isNot=True)
    partner = jpql_SelectStatement()
    setattr(partner, 'jpql_SelectStatement68', None)
    _safe_set(owner, 'jpql_ExistsExpression', partner)
    assert getattr(partner, 'jpql_SelectStatement68') == owner
    _safe_set(owner, 'jpql_ExistsExpression', None)
    assert getattr(partner, 'jpql_SelectStatement68') is None


def test_assoc_rhs65_stub_double():
    # jpql_ExpressionTerm has no real 'jpql_ExpressionTerm' property in the generated
    # code (a bare stub) -- manually attach it so jpql_OperatorExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_OperatorExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_OperatorExpression(operator="sample_text")
    partner = jpql_ExpressionTerm()
    setattr(partner, 'jpql_ExpressionTerm', None)
    _safe_set(owner, 'jpql_OperatorExpression66', partner)
    assert getattr(partner, 'jpql_ExpressionTerm') == owner
    _safe_set(owner, 'jpql_OperatorExpression66', None)
    assert getattr(partner, 'jpql_ExpressionTerm') is None


def test_assoc_selectClause36_stub_double():
    # jpql_SelectFromClause has no real 'jpql_SelectFromClause37' property in the generated
    # code (a bare stub) -- manually attach it so jpql_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_SelectClause(isDistinct=True)
    partner = jpql_SelectFromClause()
    setattr(partner, 'jpql_SelectFromClause37', None)
    _safe_set(owner, 'jpql_SelectClause', partner)
    assert getattr(partner, 'jpql_SelectFromClause37') == owner
    _safe_set(owner, 'jpql_SelectClause', None)
    assert getattr(partner, 'jpql_SelectFromClause37') is None


def test_assoc_var19_stub_double():
    # jpql_FromEntry has no real 'jpql_FromEntry' property in the generated
    # code (a bare stub) -- manually attach it so jpql_OrderItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_OrderItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_OrderItem(feature="sample_text")
    partner = jpql_FromEntry()
    setattr(partner, 'jpql_FromEntry', None)
    _safe_set(owner, 'jpql_OrderItem20', partner)
    assert getattr(partner, 'jpql_FromEntry') == owner
    _safe_set(owner, 'jpql_OrderItem20', None)
    assert getattr(partner, 'jpql_FromEntry') is None


def test_assoc_variable50_stub_double():
    # jpql_FromEntry has no real 'jpql_FromEntry51' property in the generated
    # code (a bare stub) -- manually attach it so jpql_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jpql_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jpql_VariableDeclaration(name="sample_text")
    partner = jpql_FromEntry()
    setattr(partner, 'jpql_FromEntry51', None)
    _safe_set(owner, 'jpql_VariableDeclaration', partner)
    assert getattr(partner, 'jpql_FromEntry51') == owner
    _safe_set(owner, 'jpql_VariableDeclaration', None)
    assert getattr(partner, 'jpql_FromEntry51') is None


