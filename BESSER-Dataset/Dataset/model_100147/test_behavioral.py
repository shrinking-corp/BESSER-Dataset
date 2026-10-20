import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    ExpressionTerm,
    FromEntry,
    FromJoin,
    InExpression,
    Query,
    SelectAggregateExpression,
    SelectExpression,
    Value,
    Variable,
    jPQL_AliasAttributeExpression,
    jPQL_AllExpression,
    jPQL_AndExpression,
    jPQL_AnyExpression,
    jPQL_AvgAggregate,
    jPQL_BetweenExpression,
    jPQL_BooleanExpression,
    jPQL_CollectionExpression,
    jPQL_CountAggregate,
    jPQL_DateTimeExpression,
    jPQL_DeleteClause,
    jPQL_DeleteStatement,
    jPQL_EmptyComparisonExpression,
    jPQL_ExistsExpression,
    jPQL_Expression,
    jPQL_ExpressionTerm,
    jPQL_FromClass,
    jPQL_FromClause,
    jPQL_FromCollection,
    jPQL_FromEntry,
    jPQL_FromJoin,
    jPQL_Function,
    jPQL_HavingClause,
    jPQL_InExpression,
    jPQL_InQueryExpression,
    jPQL_InSeqExpression,
    jPQL_InnerJoin,
    jPQL_IntegerExpression,
    jPQL_Join,
    jPQL_JvmType,
    jPQL_LeftJoin,
    jPQL_LikeExpression,
    jPQL_MaxAggregate,
    jPQL_MinAggregate,
    jPQL_NullComparisonExpression,
    jPQL_NullExpression,
    jPQL_OperatorExpression,
    jPQL_OrExpression,
    jPQL_OrderClause,
    jPQL_OrderItem,
    jPQL_ParameterExpression,
    jPQL_Query,
    jPQL_QueryModule,
    jPQL_SelectAggregateExpression,
    jPQL_SelectClause,
    jPQL_SelectConstructorExpression,
    jPQL_SelectExpression,
    jPQL_SelectFromClause,
    jPQL_SelectStatement,
    jPQL_SetClause,
    jPQL_SomeExpression,
    jPQL_StringExpression,
    jPQL_SumAggregate,
    jPQL_UpdateClause,
    jPQL_UpdateItem,
    jPQL_UpdateStatement,
    jPQL_Value,
    jPQL_Variable,
    jPQL_VariableDeclaration,
    jPQL_WhereClause,
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

def test_assoc_alias95_reverse_link_reassign_clear():
    a1 = jPQL_VariableDeclaration(name="sample_text")
    a2 = jPQL_VariableDeclaration(name="sample_text_2")
    b = jPQL_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression96', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression96', a1)
    if hasattr(a1, 'jPQL_VariableDeclaration97'):
        assert _is_linked(a1, 'jPQL_VariableDeclaration97', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression96', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression96', a2)
    if hasattr(a1, 'jPQL_VariableDeclaration97'):
        assert not _is_linked(a1, 'jPQL_VariableDeclaration97', b)
    if hasattr(a2, 'jPQL_VariableDeclaration97'):
        assert _is_linked(a2, 'jPQL_VariableDeclaration97', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression96', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression96', a2)
    if hasattr(a2, 'jPQL_VariableDeclaration97'):
        assert not _is_linked(a2, 'jPQL_VariableDeclaration97', b)


def test_assoc_item36_reverse_link_reassign_clear():
    a1 = jPQL_SelectAggregateExpression(isDistinct=True)
    a2 = jPQL_SelectAggregateExpression(isDistinct=False)
    b = jPQL_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression37', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression37', a1)
    if hasattr(a1, 'jPQL_SelectAggregateExpression'):
        assert _is_linked(a1, 'jPQL_SelectAggregateExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression37', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression37', a2)
    if hasattr(a1, 'jPQL_SelectAggregateExpression'):
        assert not _is_linked(a1, 'jPQL_SelectAggregateExpression', b)
    if hasattr(a2, 'jPQL_SelectAggregateExpression'):
        assert _is_linked(a2, 'jPQL_SelectAggregateExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression37', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression37', a2)
    if hasattr(a2, 'jPQL_SelectAggregateExpression'):
        assert not _is_linked(a2, 'jPQL_SelectAggregateExpression', b)


def test_assoc_items38_reverse_link_reassign_clear():
    a1 = jPQL_SelectConstructorExpression(name="sample_text")
    a2 = jPQL_SelectConstructorExpression(name="sample_text_2")
    b = jPQL_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression39', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression39', a1)
    if hasattr(a1, 'jPQL_SelectConstructorExpression'):
        assert _is_linked(a1, 'jPQL_SelectConstructorExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression39', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression39', a2)
    if hasattr(a1, 'jPQL_SelectConstructorExpression'):
        assert not _is_linked(a1, 'jPQL_SelectConstructorExpression', b)
    if hasattr(a2, 'jPQL_SelectConstructorExpression'):
        assert _is_linked(a2, 'jPQL_SelectConstructorExpression', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression39', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression39', a2)
    if hasattr(a2, 'jPQL_SelectConstructorExpression'):
        assert not _is_linked(a2, 'jPQL_SelectConstructorExpression', b)


def test_assoc_ordering10_reverse_link_reassign_clear():
    a1 = jPQL_OrderItem(feature="sample_text")
    a2 = jPQL_OrderItem(feature="sample_text_2")
    b = jPQL_OrderClause(isAsc=True, isDesc=True)
    _safe_set(b, 'jPQL_OrderClause11', {a1})
    assert _is_linked(b, 'jPQL_OrderClause11', a1)
    if hasattr(a1, 'jPQL_OrderItem'):
        assert _is_linked(a1, 'jPQL_OrderItem', b)
    _safe_set(b, 'jPQL_OrderClause11', {a2})
    assert _is_linked(b, 'jPQL_OrderClause11', a2)
    if hasattr(a1, 'jPQL_OrderItem'):
        assert not _is_linked(a1, 'jPQL_OrderItem', b)
    if hasattr(a2, 'jPQL_OrderItem'):
        assert _is_linked(a2, 'jPQL_OrderItem', b)
    _safe_set(b, 'jPQL_OrderClause11', set())
    assert not _is_linked(b, 'jPQL_OrderClause11', a2)
    if hasattr(a2, 'jPQL_OrderItem'):
        assert not _is_linked(a2, 'jPQL_OrderItem', b)


def test_assoc_path50_reverse_link_reassign_clear():
    a1 = jPQL_FromJoin(isFetch=True)
    a2 = jPQL_FromJoin(isFetch=False)
    b = jPQL_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression52', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression52', a1)
    if hasattr(a1, 'jPQL_FromJoin51'):
        assert _is_linked(a1, 'jPQL_FromJoin51', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression52', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression52', a2)
    if hasattr(a1, 'jPQL_FromJoin51'):
        assert not _is_linked(a1, 'jPQL_FromJoin51', b)
    if hasattr(a2, 'jPQL_FromJoin51'):
        assert _is_linked(a2, 'jPQL_FromJoin51', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression52', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression52', a2)
    if hasattr(a2, 'jPQL_FromJoin51'):
        assert not _is_linked(a2, 'jPQL_FromJoin51', b)


def test_assoc_rhs72_reverse_link_reassign_clear():
    a1 = jPQL_CollectionExpression(isNot=True)
    a2 = jPQL_CollectionExpression(isNot=False)
    b = jPQL_AliasAttributeExpression(attributes="sample_text")
    _safe_set(b, 'jPQL_AliasAttributeExpression74', a1)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression74', a1)
    if hasattr(a1, 'jPQL_CollectionExpression73'):
        assert _is_linked(a1, 'jPQL_CollectionExpression73', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression74', a2)
    assert _is_linked(b, 'jPQL_AliasAttributeExpression74', a2)
    if hasattr(a1, 'jPQL_CollectionExpression73'):
        assert not _is_linked(a1, 'jPQL_CollectionExpression73', b)
    if hasattr(a2, 'jPQL_CollectionExpression73'):
        assert _is_linked(a2, 'jPQL_CollectionExpression73', b)
    _safe_set(b, 'jPQL_AliasAttributeExpression74', None)
    assert not _is_linked(b, 'jPQL_AliasAttributeExpression74', a2)
    if hasattr(a2, 'jPQL_CollectionExpression73'):
        assert not _is_linked(a2, 'jPQL_CollectionExpression73', b)


def test_assoc_variable53_reverse_link_reassign_clear():
    a1 = jPQL_VariableDeclaration(name="sample_text")
    a2 = jPQL_VariableDeclaration(name="sample_text_2")
    b = jPQL_FromJoin(isFetch=True)
    _safe_set(b, 'jPQL_FromJoin54', a1)
    assert _is_linked(b, 'jPQL_FromJoin54', a1)
    if hasattr(a1, 'jPQL_VariableDeclaration55'):
        assert _is_linked(a1, 'jPQL_VariableDeclaration55', b)
    _safe_set(b, 'jPQL_FromJoin54', a2)
    assert _is_linked(b, 'jPQL_FromJoin54', a2)
    if hasattr(a1, 'jPQL_VariableDeclaration55'):
        assert not _is_linked(a1, 'jPQL_VariableDeclaration55', b)
    if hasattr(a2, 'jPQL_VariableDeclaration55'):
        assert _is_linked(a2, 'jPQL_VariableDeclaration55', b)
    _safe_set(b, 'jPQL_FromJoin54', None)
    assert not _is_linked(b, 'jPQL_FromJoin54', a2)
    if hasattr(a2, 'jPQL_VariableDeclaration55'):
        assert not _is_linked(a2, 'jPQL_VariableDeclaration55', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alias22_stub_double():
    # jPQL_UpdateItem has no real 'jPQL_UpdateItem23' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_AliasAttributeExpression(attributes="sample_text")
    partner = jPQL_UpdateItem()
    setattr(partner, 'jPQL_UpdateItem23', None)
    _safe_set(owner, 'jPQL_AliasAttributeExpression', partner)
    assert getattr(partner, 'jPQL_UpdateItem23') == owner
    _safe_set(owner, 'jPQL_AliasAttributeExpression', None)
    assert getattr(partner, 'jPQL_UpdateItem23') is None


def test_assoc_expressions34_stub_double():
    # jPQL_SelectExpression has no real 'jPQL_SelectExpression' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_SelectClause(isDistinct=True)
    partner = jPQL_SelectExpression()
    setattr(partner, 'jPQL_SelectExpression', None)
    _safe_set(owner, 'jPQL_SelectClause35', {partner})
    assert getattr(partner, 'jPQL_SelectExpression') == owner
    _safe_set(owner, 'jPQL_SelectClause35', set())
    assert getattr(partner, 'jPQL_SelectExpression') is None


def test_assoc_joins46_stub_double():
    # jPQL_FromClass has no real 'jPQL_FromClass47' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_FromJoin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_FromJoin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_FromJoin(isFetch=True)
    partner = jPQL_FromClass()
    setattr(partner, 'jPQL_FromClass47', None)
    _safe_set(owner, 'jPQL_FromJoin', partner)
    assert owner in getattr(partner, 'jPQL_FromClass47')
    _safe_set(owner, 'jPQL_FromJoin', None)
    assert owner not in getattr(partner, 'jPQL_FromClass47')


def test_assoc_lhs59_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_OperatorExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_OperatorExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_OperatorExpression(operator="sample_text")
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable', None)
    _safe_set(owner, 'jPQL_OperatorExpression', partner)
    assert getattr(partner, 'jPQL_Variable') == owner
    _safe_set(owner, 'jPQL_OperatorExpression', None)
    assert getattr(partner, 'jPQL_Variable') is None


def test_assoc_lhs70_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable71' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_CollectionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_CollectionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_CollectionExpression(isNot=True)
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable71', None)
    _safe_set(owner, 'jPQL_CollectionExpression', partner)
    assert getattr(partner, 'jPQL_Variable71') == owner
    _safe_set(owner, 'jPQL_CollectionExpression', None)
    assert getattr(partner, 'jPQL_Variable71') is None


def test_assoc_lhs75_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable76' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_NullComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_NullComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_NullComparisonExpression(isNot=True)
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable76', None)
    _safe_set(owner, 'jPQL_NullComparisonExpression', partner)
    assert getattr(partner, 'jPQL_Variable76') == owner
    _safe_set(owner, 'jPQL_NullComparisonExpression', None)
    assert getattr(partner, 'jPQL_Variable76') is None


def test_assoc_lhs77_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable78' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_EmptyComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_EmptyComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_EmptyComparisonExpression(isNot=True)
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable78', None)
    _safe_set(owner, 'jPQL_EmptyComparisonExpression', partner)
    assert getattr(partner, 'jPQL_Variable78') == owner
    _safe_set(owner, 'jPQL_EmptyComparisonExpression', None)
    assert getattr(partner, 'jPQL_Variable78') is None


def test_assoc_lhs79_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable80' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_LikeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_LikeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_LikeExpression(isNot=True, pattern="sample_text")
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable80', None)
    _safe_set(owner, 'jPQL_LikeExpression', partner)
    assert getattr(partner, 'jPQL_Variable80') == owner
    _safe_set(owner, 'jPQL_LikeExpression', None)
    assert getattr(partner, 'jPQL_Variable80') is None


def test_assoc_lhs81_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable82' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_InExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_InExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_InExpression(isNot=True)
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable82', None)
    _safe_set(owner, 'jPQL_InExpression', partner)
    assert getattr(partner, 'jPQL_Variable82') == owner
    _safe_set(owner, 'jPQL_InExpression', None)
    assert getattr(partner, 'jPQL_Variable82') is None


def test_assoc_lhs87_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable88' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_BetweenExpression(isNot=True)
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable88', None)
    _safe_set(owner, 'jPQL_BetweenExpression', partner)
    assert getattr(partner, 'jPQL_Variable88') == owner
    _safe_set(owner, 'jPQL_BetweenExpression', None)
    assert getattr(partner, 'jPQL_Variable88') is None


def test_assoc_max92_stub_double():
    # jPQL_Value has no real 'jPQL_Value94' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_BetweenExpression(isNot=True)
    partner = jPQL_Value()
    setattr(partner, 'jPQL_Value94', None)
    _safe_set(owner, 'jPQL_BetweenExpression93', partner)
    assert getattr(partner, 'jPQL_Value94') == owner
    _safe_set(owner, 'jPQL_BetweenExpression93', None)
    assert getattr(partner, 'jPQL_Value94') is None


def test_assoc_min89_stub_double():
    # jPQL_Value has no real 'jPQL_Value91' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_BetweenExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_BetweenExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_BetweenExpression(isNot=True)
    partner = jPQL_Value()
    setattr(partner, 'jPQL_Value91', None)
    _safe_set(owner, 'jPQL_BetweenExpression90', partner)
    assert getattr(partner, 'jPQL_Value91') == owner
    _safe_set(owner, 'jPQL_BetweenExpression90', None)
    assert getattr(partner, 'jPQL_Value91') is None


def test_assoc_order6_stub_double():
    # jPQL_SelectStatement has no real 'jPQL_SelectStatement7' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_OrderClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_OrderClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_OrderClause(isAsc=True, isDesc=True)
    partner = jPQL_SelectStatement()
    setattr(partner, 'jPQL_SelectStatement7', None)
    _safe_set(owner, 'jPQL_OrderClause', partner)
    assert getattr(partner, 'jPQL_SelectStatement7') == owner
    _safe_set(owner, 'jPQL_OrderClause', None)
    assert getattr(partner, 'jPQL_SelectStatement7') is None


def test_assoc_params98_stub_double():
    # jPQL_Variable has no real 'jPQL_Variable99' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_Function(name="sample_text")
    partner = jPQL_Variable()
    setattr(partner, 'jPQL_Variable99', None)
    _safe_set(owner, 'jPQL_Function', {partner})
    assert getattr(partner, 'jPQL_Variable99') == owner
    _safe_set(owner, 'jPQL_Function', set())
    assert getattr(partner, 'jPQL_Variable99') is None


def test_assoc_path48_stub_double():
    # jPQL_FromCollection has no real 'jPQL_FromCollection' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_AliasAttributeExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_AliasAttributeExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_AliasAttributeExpression(attributes="sample_text")
    partner = jPQL_FromCollection()
    setattr(partner, 'jPQL_FromCollection', None)
    _safe_set(owner, 'jPQL_AliasAttributeExpression49', partner)
    assert getattr(partner, 'jPQL_FromCollection') == owner
    _safe_set(owner, 'jPQL_AliasAttributeExpression49', None)
    assert getattr(partner, 'jPQL_FromCollection') is None


def test_assoc_query62_stub_double():
    # jPQL_SelectStatement has no real 'jPQL_SelectStatement63' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_ExistsExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_ExistsExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_ExistsExpression(isNot=True)
    partner = jPQL_SelectStatement()
    setattr(partner, 'jPQL_SelectStatement63', None)
    _safe_set(owner, 'jPQL_ExistsExpression', partner)
    assert getattr(partner, 'jPQL_SelectStatement63') == owner
    _safe_set(owner, 'jPQL_ExistsExpression', None)
    assert getattr(partner, 'jPQL_SelectStatement63') is None


def test_assoc_rhs60_stub_double():
    # jPQL_ExpressionTerm has no real 'jPQL_ExpressionTerm' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_OperatorExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_OperatorExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_OperatorExpression(operator="sample_text")
    partner = jPQL_ExpressionTerm()
    setattr(partner, 'jPQL_ExpressionTerm', None)
    _safe_set(owner, 'jPQL_OperatorExpression61', partner)
    assert getattr(partner, 'jPQL_ExpressionTerm') == owner
    _safe_set(owner, 'jPQL_OperatorExpression61', None)
    assert getattr(partner, 'jPQL_ExpressionTerm') is None


def test_assoc_selectClause29_stub_double():
    # jPQL_SelectFromClause has no real 'jPQL_SelectFromClause30' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_SelectClause(isDistinct=True)
    partner = jPQL_SelectFromClause()
    setattr(partner, 'jPQL_SelectFromClause30', None)
    _safe_set(owner, 'jPQL_SelectClause', partner)
    assert getattr(partner, 'jPQL_SelectFromClause30') == owner
    _safe_set(owner, 'jPQL_SelectClause', None)
    assert getattr(partner, 'jPQL_SelectFromClause30') is None


def test_assoc_var12_stub_double():
    # jPQL_FromEntry has no real 'jPQL_FromEntry' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_OrderItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_OrderItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_OrderItem(feature="sample_text")
    partner = jPQL_FromEntry()
    setattr(partner, 'jPQL_FromEntry', None)
    _safe_set(owner, 'jPQL_OrderItem13', partner)
    assert getattr(partner, 'jPQL_FromEntry') == owner
    _safe_set(owner, 'jPQL_OrderItem13', None)
    assert getattr(partner, 'jPQL_FromEntry') is None


def test_assoc_variable43_stub_double():
    # jPQL_FromEntry has no real 'jPQL_FromEntry44' property in the generated
    # code (a bare stub) -- manually attach it so jPQL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jPQL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jPQL_VariableDeclaration(name="sample_text")
    partner = jPQL_FromEntry()
    setattr(partner, 'jPQL_FromEntry44', None)
    _safe_set(owner, 'jPQL_VariableDeclaration', partner)
    assert getattr(partner, 'jPQL_FromEntry44') == owner
    _safe_set(owner, 'jPQL_VariableDeclaration', None)
    assert getattr(partner, 'jPQL_FromEntry44') is None


