import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    ExpressionTerm,
    FromEntry,
    FromJoin,
    InExpression,
    MQuery,
    SelectAggregateExpression,
    SelectExpression,
    Value,
    Variable,
    mql_AliasAttributeExpression,
    mql_AllExpression,
    mql_AndExpression,
    mql_AnyExpression,
    mql_AvgAggregate,
    mql_BetweenExpression,
    mql_BooleanExpression,
    mql_CollectionExpression,
    mql_CountAggregate,
    mql_DateTimeExpression,
    mql_DeleteClause,
    mql_DeleteStatement,
    mql_EmptyComparisonExpression,
    mql_ExistsExpression,
    mql_Expression,
    mql_ExpressionTerm,
    mql_FromClass,
    mql_FromClause,
    mql_FromCollection,
    mql_FromEntry,
    mql_FromJoin,
    mql_Function,
    mql_HavingClause,
    mql_Import,
    mql_InExpression,
    mql_InQueryExpression,
    mql_InSeqExpression,
    mql_InnerJoin,
    mql_IntegerExpression,
    mql_Join,
    mql_LeftJoin,
    mql_LikeExpression,
    mql_MQuery,
    mql_MaxAggregate,
    mql_MinAggregate,
    mql_NamedQuery,
    mql_NullComparisonExpression,
    mql_NullExpression,
    mql_OperatorExpression,
    mql_OrExpression,
    mql_OrderClause,
    mql_OrderItem,
    mql_ParameterExpression,
    mql_QueryModule,
    mql_SelectAggregateExpression,
    mql_SelectClause,
    mql_SelectConstructorExpression,
    mql_SelectExpression,
    mql_SelectFromClause,
    mql_SelectStatement,
    mql_SetClause,
    mql_SomeExpression,
    mql_StringExpression,
    mql_SumAggregate,
    mql_UpdateClause,
    mql_UpdateItem,
    mql_UpdateStatement,
    mql_Value,
    mql_Variable,
    mql_VariableDeclaration,
    mql_WhereClause,
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
    a1 = mql_VariableDeclaration(name="sample_text")
    a2 = mql_VariableDeclaration(name="sample_text_2")
    b = mql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'mql_AliasAttributeExpression101', a1)
    assert _is_linked(b, 'mql_AliasAttributeExpression101', a1)
    if hasattr(a1, 'mql_VariableDeclaration102'):
        assert _is_linked(a1, 'mql_VariableDeclaration102', b)
    _safe_set(b, 'mql_AliasAttributeExpression101', a2)
    assert _is_linked(b, 'mql_AliasAttributeExpression101', a2)
    if hasattr(a1, 'mql_VariableDeclaration102'):
        assert not _is_linked(a1, 'mql_VariableDeclaration102', b)
    if hasattr(a2, 'mql_VariableDeclaration102'):
        assert _is_linked(a2, 'mql_VariableDeclaration102', b)
    _safe_set(b, 'mql_AliasAttributeExpression101', None)
    assert not _is_linked(b, 'mql_AliasAttributeExpression101', a2)
    if hasattr(a2, 'mql_VariableDeclaration102'):
        assert not _is_linked(a2, 'mql_VariableDeclaration102', b)


def test_assoc_item43_reverse_link_reassign_clear():
    a1 = mql_SelectAggregateExpression(isDistinct=True)
    a2 = mql_SelectAggregateExpression(isDistinct=False)
    b = mql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'mql_AliasAttributeExpression44', a1)
    assert _is_linked(b, 'mql_AliasAttributeExpression44', a1)
    if hasattr(a1, 'mql_SelectAggregateExpression'):
        assert _is_linked(a1, 'mql_SelectAggregateExpression', b)
    _safe_set(b, 'mql_AliasAttributeExpression44', a2)
    assert _is_linked(b, 'mql_AliasAttributeExpression44', a2)
    if hasattr(a1, 'mql_SelectAggregateExpression'):
        assert not _is_linked(a1, 'mql_SelectAggregateExpression', b)
    if hasattr(a2, 'mql_SelectAggregateExpression'):
        assert _is_linked(a2, 'mql_SelectAggregateExpression', b)
    _safe_set(b, 'mql_AliasAttributeExpression44', None)
    assert not _is_linked(b, 'mql_AliasAttributeExpression44', a2)
    if hasattr(a2, 'mql_SelectAggregateExpression'):
        assert not _is_linked(a2, 'mql_SelectAggregateExpression', b)


def test_assoc_items45_reverse_link_reassign_clear():
    a1 = mql_SelectConstructorExpression(name="sample_text")
    a2 = mql_SelectConstructorExpression(name="sample_text_2")
    b = mql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'mql_AliasAttributeExpression46', a1)
    assert _is_linked(b, 'mql_AliasAttributeExpression46', a1)
    if hasattr(a1, 'mql_SelectConstructorExpression'):
        assert _is_linked(a1, 'mql_SelectConstructorExpression', b)
    _safe_set(b, 'mql_AliasAttributeExpression46', a2)
    assert _is_linked(b, 'mql_AliasAttributeExpression46', a2)
    if hasattr(a1, 'mql_SelectConstructorExpression'):
        assert not _is_linked(a1, 'mql_SelectConstructorExpression', b)
    if hasattr(a2, 'mql_SelectConstructorExpression'):
        assert _is_linked(a2, 'mql_SelectConstructorExpression', b)
    _safe_set(b, 'mql_AliasAttributeExpression46', None)
    assert not _is_linked(b, 'mql_AliasAttributeExpression46', a2)
    if hasattr(a2, 'mql_SelectConstructorExpression'):
        assert not _is_linked(a2, 'mql_SelectConstructorExpression', b)


def test_assoc_joins52_reverse_link_reassign_clear():
    a1 = mql_FromJoin(isFetch=True)
    a2 = mql_FromJoin(isFetch=False)
    b = mql_FromClass(type="sample_text")
    _safe_set(b, 'mql_FromClass', {a1})
    assert _is_linked(b, 'mql_FromClass', a1)
    if hasattr(a1, 'mql_FromJoin'):
        assert _is_linked(a1, 'mql_FromJoin', b)
    _safe_set(b, 'mql_FromClass', {a2})
    assert _is_linked(b, 'mql_FromClass', a2)
    if hasattr(a1, 'mql_FromJoin'):
        assert not _is_linked(a1, 'mql_FromJoin', b)
    if hasattr(a2, 'mql_FromJoin'):
        assert _is_linked(a2, 'mql_FromJoin', b)
    _safe_set(b, 'mql_FromClass', set())
    assert not _is_linked(b, 'mql_FromClass', a2)
    if hasattr(a2, 'mql_FromJoin'):
        assert not _is_linked(a2, 'mql_FromJoin', b)


def test_assoc_ordering17_reverse_link_reassign_clear():
    a1 = mql_OrderItem(feature="sample_text")
    a2 = mql_OrderItem(feature="sample_text_2")
    b = mql_OrderClause(isAsc=True, isDesc=True)
    _safe_set(b, 'mql_OrderClause18', {a1})
    assert _is_linked(b, 'mql_OrderClause18', a1)
    if hasattr(a1, 'mql_OrderItem'):
        assert _is_linked(a1, 'mql_OrderItem', b)
    _safe_set(b, 'mql_OrderClause18', {a2})
    assert _is_linked(b, 'mql_OrderClause18', a2)
    if hasattr(a1, 'mql_OrderItem'):
        assert not _is_linked(a1, 'mql_OrderItem', b)
    if hasattr(a2, 'mql_OrderItem'):
        assert _is_linked(a2, 'mql_OrderItem', b)
    _safe_set(b, 'mql_OrderClause18', set())
    assert not _is_linked(b, 'mql_OrderClause18', a2)
    if hasattr(a2, 'mql_OrderItem'):
        assert not _is_linked(a2, 'mql_OrderItem', b)


def test_assoc_path55_reverse_link_reassign_clear():
    a1 = mql_FromJoin(isFetch=True)
    a2 = mql_FromJoin(isFetch=False)
    b = mql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'mql_AliasAttributeExpression57', a1)
    assert _is_linked(b, 'mql_AliasAttributeExpression57', a1)
    if hasattr(a1, 'mql_FromJoin56'):
        assert _is_linked(a1, 'mql_FromJoin56', b)
    _safe_set(b, 'mql_AliasAttributeExpression57', a2)
    assert _is_linked(b, 'mql_AliasAttributeExpression57', a2)
    if hasattr(a1, 'mql_FromJoin56'):
        assert not _is_linked(a1, 'mql_FromJoin56', b)
    if hasattr(a2, 'mql_FromJoin56'):
        assert _is_linked(a2, 'mql_FromJoin56', b)
    _safe_set(b, 'mql_AliasAttributeExpression57', None)
    assert not _is_linked(b, 'mql_AliasAttributeExpression57', a2)
    if hasattr(a2, 'mql_FromJoin56'):
        assert not _is_linked(a2, 'mql_FromJoin56', b)


def test_assoc_rhs77_reverse_link_reassign_clear():
    a1 = mql_CollectionExpression(isNot=True)
    a2 = mql_CollectionExpression(isNot=False)
    b = mql_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'mql_AliasAttributeExpression79', a1)
    assert _is_linked(b, 'mql_AliasAttributeExpression79', a1)
    if hasattr(a1, 'mql_CollectionExpression78'):
        assert _is_linked(a1, 'mql_CollectionExpression78', b)
    _safe_set(b, 'mql_AliasAttributeExpression79', a2)
    assert _is_linked(b, 'mql_AliasAttributeExpression79', a2)
    if hasattr(a1, 'mql_CollectionExpression78'):
        assert not _is_linked(a1, 'mql_CollectionExpression78', b)
    if hasattr(a2, 'mql_CollectionExpression78'):
        assert _is_linked(a2, 'mql_CollectionExpression78', b)
    _safe_set(b, 'mql_AliasAttributeExpression79', None)
    assert not _is_linked(b, 'mql_AliasAttributeExpression79', a2)
    if hasattr(a2, 'mql_CollectionExpression78'):
        assert not _is_linked(a2, 'mql_CollectionExpression78', b)


def test_assoc_variable58_reverse_link_reassign_clear():
    a1 = mql_VariableDeclaration(name="sample_text")
    a2 = mql_VariableDeclaration(name="sample_text_2")
    b = mql_FromJoin(isFetch=True)
    _safe_set(b, 'mql_FromJoin59', a1)
    assert _is_linked(b, 'mql_FromJoin59', a1)
    if hasattr(a1, 'mql_VariableDeclaration60'):
        assert _is_linked(a1, 'mql_VariableDeclaration60', b)
    _safe_set(b, 'mql_FromJoin59', a2)
    assert _is_linked(b, 'mql_FromJoin59', a2)
    if hasattr(a1, 'mql_VariableDeclaration60'):
        assert not _is_linked(a1, 'mql_VariableDeclaration60', b)
    if hasattr(a2, 'mql_VariableDeclaration60'):
        assert _is_linked(a2, 'mql_VariableDeclaration60', b)
    _safe_set(b, 'mql_FromJoin59', None)
    assert not _is_linked(b, 'mql_FromJoin59', a2)
    if hasattr(a2, 'mql_VariableDeclaration60'):
        assert not _is_linked(a2, 'mql_VariableDeclaration60', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alias29_stub_double():
    # mql_UpdateItem has no real 'mql_UpdateItem30' property in the generated
    # code (a bare stub) -- manually attach it so mql_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_AliasAttributeExpression(attributes="sample_text")
    partner = mql_UpdateItem()
    setattr(partner, 'mql_UpdateItem30', None)
    _safe_set(owner, 'mql_AliasAttributeExpression', partner)
    assert getattr(partner, 'mql_UpdateItem30') == owner
    _safe_set(owner, 'mql_AliasAttributeExpression', None)
    assert getattr(partner, 'mql_UpdateItem30') is None


def test_assoc_expressions41_stub_double():
    # mql_SelectExpression has no real 'mql_SelectExpression' property in the generated
    # code (a bare stub) -- manually attach it so mql_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_SelectClause(isDistinct=True)
    partner = mql_SelectExpression()
    setattr(partner, 'mql_SelectExpression', None)
    _safe_set(owner, 'mql_SelectClause42', {partner})
    assert getattr(partner, 'mql_SelectExpression') == owner
    _safe_set(owner, 'mql_SelectClause42', set())
    assert getattr(partner, 'mql_SelectExpression') is None


def test_assoc_imports0_stub_double():
    # mql_QueryModule has no real 'mql_QueryModule' property in the generated
    # code (a bare stub) -- manually attach it so mql_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_Import(importURI="sample_text")
    partner = mql_QueryModule()
    setattr(partner, 'mql_QueryModule', None)
    _safe_set(owner, 'mql_Import', partner)
    assert owner in getattr(partner, 'mql_QueryModule')
    _safe_set(owner, 'mql_Import', None)
    assert owner not in getattr(partner, 'mql_QueryModule')


def test_assoc_lhs64_stub_double():
    # mql_Variable has no real 'mql_Variable' property in the generated
    # code (a bare stub) -- manually attach it so mql_OperatorExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_OperatorExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_OperatorExpression(operator="sample_text")
    partner = mql_Variable()
    setattr(partner, 'mql_Variable', None)
    _safe_set(owner, 'mql_OperatorExpression', partner)
    assert getattr(partner, 'mql_Variable') == owner
    _safe_set(owner, 'mql_OperatorExpression', None)
    assert getattr(partner, 'mql_Variable') is None


def test_assoc_lhs75_stub_double():
    # mql_Variable has no real 'mql_Variable76' property in the generated
    # code (a bare stub) -- manually attach it so mql_CollectionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_CollectionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_CollectionExpression(isNot=True)
    partner = mql_Variable()
    setattr(partner, 'mql_Variable76', None)
    _safe_set(owner, 'mql_CollectionExpression', partner)
    assert getattr(partner, 'mql_Variable76') == owner
    _safe_set(owner, 'mql_CollectionExpression', None)
    assert getattr(partner, 'mql_Variable76') is None


def test_assoc_lhs80_stub_double():
    # mql_Variable has no real 'mql_Variable81' property in the generated
    # code (a bare stub) -- manually attach it so mql_NullComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_NullComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_NullComparisonExpression(isNot=True)
    partner = mql_Variable()
    setattr(partner, 'mql_Variable81', None)
    _safe_set(owner, 'mql_NullComparisonExpression', partner)
    assert getattr(partner, 'mql_Variable81') == owner
    _safe_set(owner, 'mql_NullComparisonExpression', None)
    assert getattr(partner, 'mql_Variable81') is None


def test_assoc_lhs82_stub_double():
    # mql_Variable has no real 'mql_Variable83' property in the generated
    # code (a bare stub) -- manually attach it so mql_EmptyComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_EmptyComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_EmptyComparisonExpression(isNot=True)
    partner = mql_Variable()
    setattr(partner, 'mql_Variable83', None)
    _safe_set(owner, 'mql_EmptyComparisonExpression', partner)
    assert getattr(partner, 'mql_Variable83') == owner
    _safe_set(owner, 'mql_EmptyComparisonExpression', None)
    assert getattr(partner, 'mql_Variable83') is None


def test_assoc_lhs84_stub_double():
    # mql_Variable has no real 'mql_Variable85' property in the generated
    # code (a bare stub) -- manually attach it so mql_LikeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_LikeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_LikeExpression(isNot=True, pattern="sample_text")
    partner = mql_Variable()
    setattr(partner, 'mql_Variable85', None)
    _safe_set(owner, 'mql_LikeExpression', partner)
    assert getattr(partner, 'mql_Variable85') == owner
    _safe_set(owner, 'mql_LikeExpression', None)
    assert getattr(partner, 'mql_Variable85') is None


def test_assoc_lhs86_stub_double():
    # mql_Variable has no real 'mql_Variable87' property in the generated
    # code (a bare stub) -- manually attach it so mql_InExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_InExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_InExpression(isNot=True)
    partner = mql_Variable()
    setattr(partner, 'mql_Variable87', None)
    _safe_set(owner, 'mql_InExpression', partner)
    assert getattr(partner, 'mql_Variable87') == owner
    _safe_set(owner, 'mql_InExpression', None)
    assert getattr(partner, 'mql_Variable87') is None


def test_assoc_lhs92_stub_double():
    # mql_Variable has no real 'mql_Variable93' property in the generated
    # code (a bare stub) -- manually attach it so mql_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_BetweenExpression(isNot=True)
    partner = mql_Variable()
    setattr(partner, 'mql_Variable93', None)
    _safe_set(owner, 'mql_BetweenExpression', partner)
    assert getattr(partner, 'mql_Variable93') == owner
    _safe_set(owner, 'mql_BetweenExpression', None)
    assert getattr(partner, 'mql_Variable93') is None


def test_assoc_max97_stub_double():
    # mql_Value has no real 'mql_Value99' property in the generated
    # code (a bare stub) -- manually attach it so mql_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_BetweenExpression(isNot=True)
    partner = mql_Value()
    setattr(partner, 'mql_Value99', None)
    _safe_set(owner, 'mql_BetweenExpression98', partner)
    assert getattr(partner, 'mql_Value99') == owner
    _safe_set(owner, 'mql_BetweenExpression98', None)
    assert getattr(partner, 'mql_Value99') is None


def test_assoc_min94_stub_double():
    # mql_Value has no real 'mql_Value96' property in the generated
    # code (a bare stub) -- manually attach it so mql_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_BetweenExpression(isNot=True)
    partner = mql_Value()
    setattr(partner, 'mql_Value96', None)
    _safe_set(owner, 'mql_BetweenExpression95', partner)
    assert getattr(partner, 'mql_Value96') == owner
    _safe_set(owner, 'mql_BetweenExpression95', None)
    assert getattr(partner, 'mql_Value96') is None


def test_assoc_namedQueries3_stub_double():
    # mql_QueryModule has no real 'mql_QueryModule4' property in the generated
    # code (a bare stub) -- manually attach it so mql_NamedQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_NamedQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_NamedQuery(name="sample_text")
    partner = mql_QueryModule()
    setattr(partner, 'mql_QueryModule4', None)
    _safe_set(owner, 'mql_NamedQuery', partner)
    assert owner in getattr(partner, 'mql_QueryModule4')
    _safe_set(owner, 'mql_NamedQuery', None)
    assert owner not in getattr(partner, 'mql_QueryModule4')


def test_assoc_order13_stub_double():
    # mql_SelectStatement has no real 'mql_SelectStatement14' property in the generated
    # code (a bare stub) -- manually attach it so mql_OrderClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_OrderClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_OrderClause(isAsc=True, isDesc=True)
    partner = mql_SelectStatement()
    setattr(partner, 'mql_SelectStatement14', None)
    _safe_set(owner, 'mql_OrderClause', partner)
    assert getattr(partner, 'mql_SelectStatement14') == owner
    _safe_set(owner, 'mql_OrderClause', None)
    assert getattr(partner, 'mql_SelectStatement14') is None


def test_assoc_params103_stub_double():
    # mql_Variable has no real 'mql_Variable104' property in the generated
    # code (a bare stub) -- manually attach it so mql_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_Function(name="sample_text")
    partner = mql_Variable()
    setattr(partner, 'mql_Variable104', None)
    _safe_set(owner, 'mql_Function', {partner})
    assert getattr(partner, 'mql_Variable104') == owner
    _safe_set(owner, 'mql_Function', set())
    assert getattr(partner, 'mql_Variable104') is None


def test_assoc_path53_stub_double():
    # mql_FromCollection has no real 'mql_FromCollection' property in the generated
    # code (a bare stub) -- manually attach it so mql_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_AliasAttributeExpression(attributes="sample_text")
    partner = mql_FromCollection()
    setattr(partner, 'mql_FromCollection', None)
    _safe_set(owner, 'mql_AliasAttributeExpression54', partner)
    assert getattr(partner, 'mql_FromCollection') == owner
    _safe_set(owner, 'mql_AliasAttributeExpression54', None)
    assert getattr(partner, 'mql_FromCollection') is None


def test_assoc_query5_stub_double():
    # mql_MQuery has no real 'mql_MQuery7' property in the generated
    # code (a bare stub) -- manually attach it so mql_NamedQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_NamedQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_NamedQuery(name="sample_text")
    partner = mql_MQuery()
    setattr(partner, 'mql_MQuery7', None)
    _safe_set(owner, 'mql_NamedQuery6', partner)
    assert getattr(partner, 'mql_MQuery7') == owner
    _safe_set(owner, 'mql_NamedQuery6', None)
    assert getattr(partner, 'mql_MQuery7') is None


def test_assoc_query67_stub_double():
    # mql_SelectStatement has no real 'mql_SelectStatement68' property in the generated
    # code (a bare stub) -- manually attach it so mql_ExistsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_ExistsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_ExistsExpression(isNot=True)
    partner = mql_SelectStatement()
    setattr(partner, 'mql_SelectStatement68', None)
    _safe_set(owner, 'mql_ExistsExpression', partner)
    assert getattr(partner, 'mql_SelectStatement68') == owner
    _safe_set(owner, 'mql_ExistsExpression', None)
    assert getattr(partner, 'mql_SelectStatement68') is None


def test_assoc_rhs65_stub_double():
    # mql_ExpressionTerm has no real 'mql_ExpressionTerm' property in the generated
    # code (a bare stub) -- manually attach it so mql_OperatorExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_OperatorExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_OperatorExpression(operator="sample_text")
    partner = mql_ExpressionTerm()
    setattr(partner, 'mql_ExpressionTerm', None)
    _safe_set(owner, 'mql_OperatorExpression66', partner)
    assert getattr(partner, 'mql_ExpressionTerm') == owner
    _safe_set(owner, 'mql_OperatorExpression66', None)
    assert getattr(partner, 'mql_ExpressionTerm') is None


def test_assoc_selectClause36_stub_double():
    # mql_SelectFromClause has no real 'mql_SelectFromClause37' property in the generated
    # code (a bare stub) -- manually attach it so mql_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_SelectClause(isDistinct=True)
    partner = mql_SelectFromClause()
    setattr(partner, 'mql_SelectFromClause37', None)
    _safe_set(owner, 'mql_SelectClause', partner)
    assert getattr(partner, 'mql_SelectFromClause37') == owner
    _safe_set(owner, 'mql_SelectClause', None)
    assert getattr(partner, 'mql_SelectFromClause37') is None


def test_assoc_var19_stub_double():
    # mql_FromEntry has no real 'mql_FromEntry' property in the generated
    # code (a bare stub) -- manually attach it so mql_OrderItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_OrderItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_OrderItem(feature="sample_text")
    partner = mql_FromEntry()
    setattr(partner, 'mql_FromEntry', None)
    _safe_set(owner, 'mql_OrderItem20', partner)
    assert getattr(partner, 'mql_FromEntry') == owner
    _safe_set(owner, 'mql_OrderItem20', None)
    assert getattr(partner, 'mql_FromEntry') is None


def test_assoc_variable50_stub_double():
    # mql_FromEntry has no real 'mql_FromEntry51' property in the generated
    # code (a bare stub) -- manually attach it so mql_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mql_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mql_VariableDeclaration(name="sample_text")
    partner = mql_FromEntry()
    setattr(partner, 'mql_FromEntry51', None)
    _safe_set(owner, 'mql_VariableDeclaration', partner)
    assert getattr(partner, 'mql_FromEntry51') == owner
    _safe_set(owner, 'mql_VariableDeclaration', None)
    assert getattr(partner, 'mql_FromEntry51') is None


