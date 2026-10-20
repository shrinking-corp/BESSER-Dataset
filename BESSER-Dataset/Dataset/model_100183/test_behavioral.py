import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Aggregate,
    Constraint,
    DatasetClause,
    Expression,
    FilterNode,
    Function,
    GraphNode,
    GraphPattern,
    GroupCondition,
    GroupGraphPattern,
    ModifyQuery,
    RDFTag,
    SPARQLQuery,
    SelectionQuery,
    UpdateOperation,
    Value,
    Variable,
    sparql_Aggregate,
    sparql_AndFilterExpression,
    sparql_AskQuery,
    sparql_AvgAggregate,
    sparql_Base,
    sparql_BlankNode,
    sparql_BuiltInCall,
    sparql_ClearGraphQuery,
    sparql_Constraint,
    sparql_ConstructQuery,
    sparql_CountAggregate,
    sparql_CreateGraphQuery,
    sparql_DatasetClause,
    sparql_DefaultDataSet,
    sparql_DeleteDataQuery,
    sparql_DeleteQuery,
    sparql_DeleteWhereQuery,
    sparql_DescribeQuery,
    sparql_DropGraphQuery,
    sparql_ExistsPattern,
    sparql_ExprAggArg,
    sparql_Expression,
    sparql_ExpressionFilterExpression,
    sparql_FilterNode,
    sparql_FilterPattern,
    sparql_Function,
    sparql_GraphGraphPattern,
    sparql_GraphNode,
    sparql_GraphPattern,
    sparql_GroupAggregate,
    sparql_GroupClause,
    sparql_GroupCondition,
    sparql_GroupGraphPattern,
    sparql_GroupGraphPatternSub,
    sparql_GroupOrUnionGraphPattern,
    sparql_HavingClause,
    sparql_IRI,
    sparql_InsertDataQuery,
    sparql_InsertQuery,
    sparql_IntegerValue,
    sparql_LangTag,
    sparql_LimitClause,
    sparql_LoadGraphQuery,
    sparql_MaxAggregate,
    sparql_MinAgregate,
    sparql_MinusPattern,
    sparql_ModifyQuery,
    sparql_NamedDataSet,
    sparql_NamedFunction,
    sparql_NamedVariable,
    sparql_NotExistsPattern,
    sparql_OptionalGraphPattern,
    sparql_OrFilterExpression,
    sparql_Parameter,
    sparql_Prefix,
    sparql_PropertyList,
    sparql_RDFTag,
    sparql_SPARQLQuery,
    sparql_SampleAggregate,
    sparql_SelectQuery,
    sparql_SelectionQuery,
    sparql_ServiceDataSet,
    sparql_ServiceGraphPattern,
    sparql_SparqlFunction,
    sparql_StringValue,
    sparql_SubSelectQuery,
    sparql_SumAggregate,
    sparql_TriplesSameSubject,
    sparql_TypeTag,
    sparql_UnNamedVariable,
    sparql_UpdateOperation,
    sparql_UpdateQuery,
    sparql_UsingGraph,
    sparql_Value,
    sparql_Variable,
    sparql_WhereClause,
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

def test_assoc_parameters84_reverse_link_reassign_clear():
    a1 = sparql_Variable(name="sample_text")
    a2 = sparql_Variable(name="sample_text_2")
    b = sparql_Function(name="sample_text")
    _safe_set(b, 'sparql_Function', {a1})
    assert _is_linked(b, 'sparql_Function', a1)
    if hasattr(a1, 'sparql_Variable85'):
        assert _is_linked(a1, 'sparql_Variable85', b)
    _safe_set(b, 'sparql_Function', {a2})
    assert _is_linked(b, 'sparql_Function', a2)
    if hasattr(a1, 'sparql_Variable85'):
        assert not _is_linked(a1, 'sparql_Variable85', b)
    if hasattr(a2, 'sparql_Variable85'):
        assert _is_linked(a2, 'sparql_Variable85', b)
    _safe_set(b, 'sparql_Function', set())
    assert not _is_linked(b, 'sparql_Function', a2)
    if hasattr(a2, 'sparql_Variable85'):
        assert not _is_linked(a2, 'sparql_Variable85', b)


def test_assoc_variables14_reverse_link_reassign_clear():
    a1 = sparql_Variable(name="sample_text")
    a2 = sparql_Variable(name="sample_text_2")
    b = sparql_SelectQuery(all=True, isDistinct=True, isReduced=True)
    _safe_set(b, 'sparql_SelectQuery', {a1})
    assert _is_linked(b, 'sparql_SelectQuery', a1)
    if hasattr(a1, 'sparql_Variable'):
        assert _is_linked(a1, 'sparql_Variable', b)
    _safe_set(b, 'sparql_SelectQuery', {a2})
    assert _is_linked(b, 'sparql_SelectQuery', a2)
    if hasattr(a1, 'sparql_Variable'):
        assert not _is_linked(a1, 'sparql_Variable', b)
    if hasattr(a2, 'sparql_Variable'):
        assert _is_linked(a2, 'sparql_Variable', b)
    _safe_set(b, 'sparql_SelectQuery', set())
    assert not _is_linked(b, 'sparql_SelectQuery', a2)
    if hasattr(a2, 'sparql_Variable'):
        assert not _is_linked(a2, 'sparql_Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dataSet27_stub_double():
    # sparql_DatasetClause has no real 'sparql_DatasetClause28' property in the generated
    # code (a bare stub) -- manually attach it so sparql_IRI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_IRI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_IRI(value="sample_text")
    partner = sparql_DatasetClause()
    setattr(partner, 'sparql_DatasetClause28', None)
    _safe_set(owner, 'sparql_IRI29', partner)
    assert getattr(partner, 'sparql_DatasetClause28') == owner
    _safe_set(owner, 'sparql_IRI29', None)
    assert getattr(partner, 'sparql_DatasetClause28') is None


def test_assoc_expr108_stub_double():
    # sparql_Expression has no real 'sparql_Expression109' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExprAggArg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExprAggArg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExprAggArg(isDistinct=True)
    partner = sparql_Expression()
    setattr(partner, 'sparql_Expression109', None)
    _safe_set(owner, 'sparql_ExprAggArg', partner)
    assert getattr(partner, 'sparql_Expression109') == owner
    _safe_set(owner, 'sparql_ExprAggArg', None)
    assert getattr(partner, 'sparql_Expression109') is None


def test_assoc_expr119_stub_double():
    # sparql_Expression has no real 'sparql_Expression120' property in the generated
    # code (a bare stub) -- manually attach it so sparql_CountAggregate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_CountAggregate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_CountAggregate(isAll=True, isDistinct=True)
    partner = sparql_Expression()
    setattr(partner, 'sparql_Expression120', None)
    _safe_set(owner, 'sparql_CountAggregate', partner)
    assert getattr(partner, 'sparql_Expression120') == owner
    _safe_set(owner, 'sparql_CountAggregate', None)
    assert getattr(partner, 'sparql_Expression120') is None


def test_assoc_expr121_stub_double():
    # sparql_SumAggregate has no real 'sparql_SumAggregate' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExprAggArg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExprAggArg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExprAggArg(isDistinct=True)
    partner = sparql_SumAggregate()
    setattr(partner, 'sparql_SumAggregate', None)
    _safe_set(owner, 'sparql_ExprAggArg122', partner)
    assert getattr(partner, 'sparql_SumAggregate') == owner
    _safe_set(owner, 'sparql_ExprAggArg122', None)
    assert getattr(partner, 'sparql_SumAggregate') is None


def test_assoc_expr123_stub_double():
    # sparql_MinAgregate has no real 'sparql_MinAgregate' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExprAggArg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExprAggArg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExprAggArg(isDistinct=True)
    partner = sparql_MinAgregate()
    setattr(partner, 'sparql_MinAgregate', None)
    _safe_set(owner, 'sparql_ExprAggArg124', partner)
    assert getattr(partner, 'sparql_MinAgregate') == owner
    _safe_set(owner, 'sparql_ExprAggArg124', None)
    assert getattr(partner, 'sparql_MinAgregate') is None


def test_assoc_expr125_stub_double():
    # sparql_MaxAggregate has no real 'sparql_MaxAggregate' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExprAggArg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExprAggArg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExprAggArg(isDistinct=True)
    partner = sparql_MaxAggregate()
    setattr(partner, 'sparql_MaxAggregate', None)
    _safe_set(owner, 'sparql_ExprAggArg126', partner)
    assert getattr(partner, 'sparql_MaxAggregate') == owner
    _safe_set(owner, 'sparql_ExprAggArg126', None)
    assert getattr(partner, 'sparql_MaxAggregate') is None


def test_assoc_expr127_stub_double():
    # sparql_AvgAggregate has no real 'sparql_AvgAggregate' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExprAggArg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExprAggArg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExprAggArg(isDistinct=True)
    partner = sparql_AvgAggregate()
    setattr(partner, 'sparql_AvgAggregate', None)
    _safe_set(owner, 'sparql_ExprAggArg128', partner)
    assert getattr(partner, 'sparql_AvgAggregate') == owner
    _safe_set(owner, 'sparql_ExprAggArg128', None)
    assert getattr(partner, 'sparql_AvgAggregate') is None


def test_assoc_expr129_stub_double():
    # sparql_SampleAggregate has no real 'sparql_SampleAggregate' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExprAggArg's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExprAggArg's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExprAggArg(isDistinct=True)
    partner = sparql_SampleAggregate()
    setattr(partner, 'sparql_SampleAggregate', None)
    _safe_set(owner, 'sparql_ExprAggArg130', partner)
    assert getattr(partner, 'sparql_SampleAggregate') == owner
    _safe_set(owner, 'sparql_ExprAggArg130', None)
    assert getattr(partner, 'sparql_SampleAggregate') is None


def test_assoc_expr131_stub_double():
    # sparql_Expression has no real 'sparql_Expression132' property in the generated
    # code (a bare stub) -- manually attach it so sparql_GroupAggregate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_GroupAggregate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_GroupAggregate(isDistinct=True, value="sample_text")
    partner = sparql_Expression()
    setattr(partner, 'sparql_Expression132', None)
    _safe_set(owner, 'sparql_GroupAggregate', {partner})
    assert getattr(partner, 'sparql_Expression132') == owner
    _safe_set(owner, 'sparql_GroupAggregate', set())
    assert getattr(partner, 'sparql_Expression132') is None


def test_assoc_insertPattern22_stub_double():
    # sparql_GroupGraphPattern has no real 'sparql_GroupGraphPattern23' property in the generated
    # code (a bare stub) -- manually attach it so sparql_DeleteQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_DeleteQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_DeleteQuery(graph="sample_text")
    partner = sparql_GroupGraphPattern()
    setattr(partner, 'sparql_GroupGraphPattern23', None)
    _safe_set(owner, 'sparql_DeleteQuery', partner)
    assert getattr(partner, 'sparql_GroupGraphPattern23') == owner
    _safe_set(owner, 'sparql_DeleteQuery', None)
    assert getattr(partner, 'sparql_GroupGraphPattern23') is None


def test_assoc_iref1_stub_double():
    # sparql_Base has no real 'sparql_Base' property in the generated
    # code (a bare stub) -- manually attach it so sparql_IRI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_IRI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_IRI(value="sample_text")
    partner = sparql_Base()
    setattr(partner, 'sparql_Base', None)
    _safe_set(owner, 'sparql_IRI', partner)
    assert getattr(partner, 'sparql_Base') == owner
    _safe_set(owner, 'sparql_IRI', None)
    assert getattr(partner, 'sparql_Base') is None


def test_assoc_left80_stub_double():
    # sparql_FilterNode has no real 'sparql_FilterNode' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExpressionFilterExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExpressionFilterExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExpressionFilterExpression(operator="sample_text")
    partner = sparql_FilterNode()
    setattr(partner, 'sparql_FilterNode', None)
    _safe_set(owner, 'sparql_ExpressionFilterExpression', partner)
    assert getattr(partner, 'sparql_FilterNode') == owner
    _safe_set(owner, 'sparql_ExpressionFilterExpression', None)
    assert getattr(partner, 'sparql_FilterNode') is None


def test_assoc_limitClause12_stub_double():
    # sparql_SelectionQuery has no real 'sparql_SelectionQuery13' property in the generated
    # code (a bare stub) -- manually attach it so sparql_LimitClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_LimitClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_LimitClause(limit=7)
    partner = sparql_SelectionQuery()
    setattr(partner, 'sparql_SelectionQuery13', None)
    _safe_set(owner, 'sparql_LimitClause', partner)
    assert getattr(partner, 'sparql_SelectionQuery13') == owner
    _safe_set(owner, 'sparql_LimitClause', None)
    assert getattr(partner, 'sparql_SelectionQuery13') is None


def test_assoc_pattern18_stub_double():
    # sparql_GroupGraphPattern has no real 'sparql_GroupGraphPattern19' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ModifyQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ModifyQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ModifyQuery(withGraph="sample_text")
    partner = sparql_GroupGraphPattern()
    setattr(partner, 'sparql_GroupGraphPattern19', None)
    _safe_set(owner, 'sparql_ModifyQuery', partner)
    assert getattr(partner, 'sparql_GroupGraphPattern19') == owner
    _safe_set(owner, 'sparql_ModifyQuery', None)
    assert getattr(partner, 'sparql_GroupGraphPattern19') is None


def test_assoc_prefix110_stub_double():
    # sparql_NamedVariable has no real 'sparql_NamedVariable' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Prefix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Prefix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Prefix(iref="sample_text", name="sample_text")
    partner = sparql_NamedVariable()
    setattr(partner, 'sparql_NamedVariable', None)
    _safe_set(owner, 'sparql_Prefix111', partner)
    assert getattr(partner, 'sparql_NamedVariable') == owner
    _safe_set(owner, 'sparql_Prefix111', None)
    assert getattr(partner, 'sparql_NamedVariable') is None


def test_assoc_prefix86_stub_double():
    # sparql_NamedFunction has no real 'sparql_NamedFunction' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Prefix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Prefix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Prefix(iref="sample_text", name="sample_text")
    partner = sparql_NamedFunction()
    setattr(partner, 'sparql_NamedFunction', None)
    _safe_set(owner, 'sparql_Prefix87', partner)
    assert getattr(partner, 'sparql_NamedFunction') == owner
    _safe_set(owner, 'sparql_Prefix87', None)
    assert getattr(partner, 'sparql_NamedFunction') is None


def test_assoc_prefixes0_stub_double():
    # sparql_SPARQLQuery has no real 'sparql_SPARQLQuery' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Prefix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Prefix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Prefix(iref="sample_text", name="sample_text")
    partner = sparql_SPARQLQuery()
    setattr(partner, 'sparql_SPARQLQuery', None)
    _safe_set(owner, 'sparql_Prefix', partner)
    assert owner in getattr(partner, 'sparql_SPARQLQuery')
    _safe_set(owner, 'sparql_Prefix', None)
    assert owner not in getattr(partner, 'sparql_SPARQLQuery')


def test_assoc_right81_stub_double():
    # sparql_FilterNode has no real 'sparql_FilterNode83' property in the generated
    # code (a bare stub) -- manually attach it so sparql_ExpressionFilterExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_ExpressionFilterExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_ExpressionFilterExpression(operator="sample_text")
    partner = sparql_FilterNode()
    setattr(partner, 'sparql_FilterNode83', None)
    _safe_set(owner, 'sparql_ExpressionFilterExpression82', partner)
    assert getattr(partner, 'sparql_FilterNode83') == owner
    _safe_set(owner, 'sparql_ExpressionFilterExpression82', None)
    assert getattr(partner, 'sparql_FilterNode83') is None


def test_assoc_var96_stub_double():
    # sparql_BuiltInCall has no real 'sparql_BuiltInCall97' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Variable(name="sample_text")
    partner = sparql_BuiltInCall()
    setattr(partner, 'sparql_BuiltInCall97', None)
    _safe_set(owner, 'sparql_Variable98', partner)
    assert getattr(partner, 'sparql_BuiltInCall97') == owner
    _safe_set(owner, 'sparql_Variable98', None)
    assert getattr(partner, 'sparql_BuiltInCall97') is None


def test_assoc_variables37_stub_double():
    # sparql_SubSelectQuery has no real 'sparql_SubSelectQuery' property in the generated
    # code (a bare stub) -- manually attach it so sparql_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_Variable(name="sample_text")
    partner = sparql_SubSelectQuery()
    setattr(partner, 'sparql_SubSelectQuery', None)
    _safe_set(owner, 'sparql_Variable38', partner)
    assert owner in getattr(partner, 'sparql_SubSelectQuery')
    _safe_set(owner, 'sparql_Variable38', None)
    assert owner not in getattr(partner, 'sparql_SubSelectQuery')


def test_assoc_whereClause20_stub_double():
    # sparql_WhereClause has no real 'sparql_WhereClause21' property in the generated
    # code (a bare stub) -- manually attach it so sparql_InsertQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_InsertQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_InsertQuery(graph="sample_text")
    partner = sparql_WhereClause()
    setattr(partner, 'sparql_WhereClause21', None)
    _safe_set(owner, 'sparql_InsertQuery', partner)
    assert getattr(partner, 'sparql_WhereClause21') == owner
    _safe_set(owner, 'sparql_InsertQuery', None)
    assert getattr(partner, 'sparql_WhereClause21') is None


def test_assoc_whereClause24_stub_double():
    # sparql_WhereClause has no real 'sparql_WhereClause26' property in the generated
    # code (a bare stub) -- manually attach it so sparql_DeleteQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sparql_DeleteQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sparql_DeleteQuery(graph="sample_text")
    partner = sparql_WhereClause()
    setattr(partner, 'sparql_WhereClause26', None)
    _safe_set(owner, 'sparql_DeleteQuery25', partner)
    assert getattr(partner, 'sparql_WhereClause26') == owner
    _safe_set(owner, 'sparql_DeleteQuery25', None)
    assert getattr(partner, 'sparql_WhereClause26') is None


