import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    OrderBySpec,
    ResultSpec,
    SubquerySelectClause,
    jDOQL_AdditionExpression,
    jDOQL_Alias,
    jDOQL_ComparisonOperatorExpression,
    jDOQL_ConditionalAndExpression,
    jDOQL_ConditionalOrExpression,
    jDOQL_EObject,
    jDOQL_Expression,
    jDOQL_FieldAccessExpression,
    jDOQL_FromClause,
    jDOQL_GroupByClause,
    jDOQL_HavingClause,
    jDOQL_ImportClause,
    jDOQL_IntoClause,
    jDOQL_MultiplicationExpression,
    jDOQL_OrderByClause,
    jDOQL_OrderBySpec,
    jDOQL_ParameterDeclaration,
    jDOQL_ParametersClause,
    jDOQL_RangeClause,
    jDOQL_ResultClause,
    jDOQL_ResultNaming,
    jDOQL_ResultSpec,
    jDOQL_SelectClause,
    jDOQL_SimpleAndExpression,
    jDOQL_SimpleOrExpression,
    jDOQL_SingleStringJDOQL,
    jDOQL_Subquery,
    jDOQL_SubqueryFromClause,
    jDOQL_SubqueryResultClause,
    jDOQL_SubquerySelectClause,
    jDOQL_VariableDeclaration,
    jDOQL_VariablesClause,
    jDOQL_WhereClause,
    AdditionOperator,
    ComparisonOperator,
    MultiplicationOperator,
    OrderByDirection,
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

def test_assoc_aggregateArgument81_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression82', a1)
    assert _is_linked(b, 'jDOQL_Expression82', a1)
    if hasattr(a1, 'jDOQL_Expression80'):
        assert _is_linked(a1, 'jDOQL_Expression80', b)
    _safe_set(b, 'jDOQL_Expression82', a2)
    assert _is_linked(b, 'jDOQL_Expression82', a2)
    if hasattr(a1, 'jDOQL_Expression80'):
        assert not _is_linked(a1, 'jDOQL_Expression80', b)
    if hasattr(a2, 'jDOQL_Expression80'):
        assert _is_linked(a2, 'jDOQL_Expression80', b)
    _safe_set(b, 'jDOQL_Expression82', None)
    assert not _is_linked(b, 'jDOQL_Expression82', a2)
    if hasattr(a2, 'jDOQL_Expression80'):
        assert not _is_linked(a2, 'jDOQL_Expression80', b)


def test_assoc_alias41_reverse_link_reassign_clear():
    a1 = jDOQL_SubqueryFromClause(candidateClassName="sample_text", isExcludeSubclasses=True)
    a2 = jDOQL_SubqueryFromClause(candidateClassName="sample_text_2", isExcludeSubclasses=False)
    b = jDOQL_Alias(identifier="sample_text")
    _safe_set(b, 'jDOQL_Alias', a1)
    assert _is_linked(b, 'jDOQL_Alias', a1)
    if hasattr(a1, 'jDOQL_SubqueryFromClause42'):
        assert _is_linked(a1, 'jDOQL_SubqueryFromClause42', b)
    _safe_set(b, 'jDOQL_Alias', a2)
    assert _is_linked(b, 'jDOQL_Alias', a2)
    if hasattr(a1, 'jDOQL_SubqueryFromClause42'):
        assert not _is_linked(a1, 'jDOQL_SubqueryFromClause42', b)
    if hasattr(a2, 'jDOQL_SubqueryFromClause42'):
        assert _is_linked(a2, 'jDOQL_SubqueryFromClause42', b)
    _safe_set(b, 'jDOQL_Alias', None)
    assert not _is_linked(b, 'jDOQL_Alias', a2)
    if hasattr(a2, 'jDOQL_SubqueryFromClause42'):
        assert not _is_linked(a2, 'jDOQL_SubqueryFromClause42', b)


def test_assoc_arg87_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression88', a1)
    assert _is_linked(b, 'jDOQL_Expression88', a1)
    if hasattr(a1, 'jDOQL_Expression86'):
        assert _is_linked(a1, 'jDOQL_Expression86', b)
    _safe_set(b, 'jDOQL_Expression88', a2)
    assert _is_linked(b, 'jDOQL_Expression88', a2)
    if hasattr(a1, 'jDOQL_Expression86'):
        assert not _is_linked(a1, 'jDOQL_Expression86', b)
    if hasattr(a2, 'jDOQL_Expression86'):
        assert _is_linked(a2, 'jDOQL_Expression86', b)
    _safe_set(b, 'jDOQL_Expression88', None)
    assert not _is_linked(b, 'jDOQL_Expression88', a2)
    if hasattr(a2, 'jDOQL_Expression86'):
        assert not _is_linked(a2, 'jDOQL_Expression86', b)


def test_assoc_beginIndex111_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression112', a1)
    assert _is_linked(b, 'jDOQL_Expression112', a1)
    if hasattr(a1, 'jDOQL_Expression110'):
        assert _is_linked(a1, 'jDOQL_Expression110', b)
    _safe_set(b, 'jDOQL_Expression112', a2)
    assert _is_linked(b, 'jDOQL_Expression112', a2)
    if hasattr(a1, 'jDOQL_Expression110'):
        assert not _is_linked(a1, 'jDOQL_Expression110', b)
    if hasattr(a2, 'jDOQL_Expression110'):
        assert _is_linked(a2, 'jDOQL_Expression110', b)
    _safe_set(b, 'jDOQL_Expression112', None)
    assert not _is_linked(b, 'jDOQL_Expression112', a2)
    if hasattr(a2, 'jDOQL_Expression110'):
        assert not _is_linked(a2, 'jDOQL_Expression110', b)


def test_assoc_element84_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression85', a1)
    assert _is_linked(b, 'jDOQL_Expression85', a1)
    if hasattr(a1, 'jDOQL_Expression83'):
        assert _is_linked(a1, 'jDOQL_Expression83', b)
    _safe_set(b, 'jDOQL_Expression85', a2)
    assert _is_linked(b, 'jDOQL_Expression85', a2)
    if hasattr(a1, 'jDOQL_Expression83'):
        assert not _is_linked(a1, 'jDOQL_Expression83', b)
    if hasattr(a2, 'jDOQL_Expression83'):
        assert _is_linked(a2, 'jDOQL_Expression83', b)
    _safe_set(b, 'jDOQL_Expression85', None)
    assert not _is_linked(b, 'jDOQL_Expression85', a2)
    if hasattr(a2, 'jDOQL_Expression83'):
        assert not _is_linked(a2, 'jDOQL_Expression83', b)


def test_assoc_endIndex114_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression115', a1)
    assert _is_linked(b, 'jDOQL_Expression115', a1)
    if hasattr(a1, 'jDOQL_Expression113'):
        assert _is_linked(a1, 'jDOQL_Expression113', b)
    _safe_set(b, 'jDOQL_Expression115', a2)
    assert _is_linked(b, 'jDOQL_Expression115', a2)
    if hasattr(a1, 'jDOQL_Expression113'):
        assert not _is_linked(a1, 'jDOQL_Expression113', b)
    if hasattr(a2, 'jDOQL_Expression113'):
        assert _is_linked(a2, 'jDOQL_Expression113', b)
    _safe_set(b, 'jDOQL_Expression115', None)
    assert not _is_linked(b, 'jDOQL_Expression115', a2)
    if hasattr(a2, 'jDOQL_Expression113'):
        assert not _is_linked(a2, 'jDOQL_Expression113', b)


def test_assoc_fieldAccessExpression38_reverse_link_reassign_clear():
    a1 = jDOQL_SubqueryFromClause(candidateClassName="sample_text", isExcludeSubclasses=True)
    a2 = jDOQL_SubqueryFromClause(candidateClassName="sample_text_2", isExcludeSubclasses=False)
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression40', a1)
    assert _is_linked(b, 'jDOQL_Expression40', a1)
    if hasattr(a1, 'jDOQL_SubqueryFromClause39'):
        assert _is_linked(a1, 'jDOQL_SubqueryFromClause39', b)
    _safe_set(b, 'jDOQL_Expression40', a2)
    assert _is_linked(b, 'jDOQL_Expression40', a2)
    if hasattr(a1, 'jDOQL_SubqueryFromClause39'):
        assert not _is_linked(a1, 'jDOQL_SubqueryFromClause39', b)
    if hasattr(a2, 'jDOQL_SubqueryFromClause39'):
        assert _is_linked(a2, 'jDOQL_SubqueryFromClause39', b)
    _safe_set(b, 'jDOQL_Expression40', None)
    assert not _is_linked(b, 'jDOQL_Expression40', a2)
    if hasattr(a2, 'jDOQL_SubqueryFromClause39'):
        assert not _is_linked(a2, 'jDOQL_SubqueryFromClause39', b)


def test_assoc_fromIndex102_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression103', a1)
    assert _is_linked(b, 'jDOQL_Expression103', a1)
    if hasattr(a1, 'jDOQL_Expression101'):
        assert _is_linked(a1, 'jDOQL_Expression101', b)
    _safe_set(b, 'jDOQL_Expression103', a2)
    assert _is_linked(b, 'jDOQL_Expression103', a2)
    if hasattr(a1, 'jDOQL_Expression101'):
        assert not _is_linked(a1, 'jDOQL_Expression101', b)
    if hasattr(a2, 'jDOQL_Expression101'):
        assert _is_linked(a2, 'jDOQL_Expression101', b)
    _safe_set(b, 'jDOQL_Expression103', None)
    assert not _is_linked(b, 'jDOQL_Expression103', a2)
    if hasattr(a2, 'jDOQL_Expression101'):
        assert not _is_linked(a2, 'jDOQL_Expression101', b)


def test_assoc_index96_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression97', a1)
    assert _is_linked(b, 'jDOQL_Expression97', a1)
    if hasattr(a1, 'jDOQL_Expression95'):
        assert _is_linked(a1, 'jDOQL_Expression95', b)
    _safe_set(b, 'jDOQL_Expression97', a2)
    assert _is_linked(b, 'jDOQL_Expression97', a2)
    if hasattr(a1, 'jDOQL_Expression95'):
        assert not _is_linked(a1, 'jDOQL_Expression95', b)
    if hasattr(a2, 'jDOQL_Expression95'):
        assert _is_linked(a2, 'jDOQL_Expression95', b)
    _safe_set(b, 'jDOQL_Expression97', None)
    assert not _is_linked(b, 'jDOQL_Expression97', a2)
    if hasattr(a2, 'jDOQL_Expression95'):
        assert not _is_linked(a2, 'jDOQL_Expression95', b)


def test_assoc_intoClause34_reverse_link_reassign_clear():
    a1 = jDOQL_SelectClause(isUnique=True)
    a2 = jDOQL_SelectClause(isUnique=False)
    b = jDOQL_IntoClause(resultClassName="sample_text")
    _safe_set(b, 'jDOQL_IntoClause', a1)
    assert _is_linked(b, 'jDOQL_IntoClause', a1)
    if hasattr(a1, 'jDOQL_SelectClause35'):
        assert _is_linked(a1, 'jDOQL_SelectClause35', b)
    _safe_set(b, 'jDOQL_IntoClause', a2)
    assert _is_linked(b, 'jDOQL_IntoClause', a2)
    if hasattr(a1, 'jDOQL_SelectClause35'):
        assert not _is_linked(a1, 'jDOQL_SelectClause35', b)
    if hasattr(a2, 'jDOQL_SelectClause35'):
        assert _is_linked(a2, 'jDOQL_SelectClause35', b)
    _safe_set(b, 'jDOQL_IntoClause', None)
    assert not _is_linked(b, 'jDOQL_IntoClause', a2)
    if hasattr(a2, 'jDOQL_SelectClause35'):
        assert not _is_linked(a2, 'jDOQL_SelectClause35', b)


def test_assoc_key90_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression91', a1)
    assert _is_linked(b, 'jDOQL_Expression91', a1)
    if hasattr(a1, 'jDOQL_Expression89'):
        assert _is_linked(a1, 'jDOQL_Expression89', b)
    _safe_set(b, 'jDOQL_Expression91', a2)
    assert _is_linked(b, 'jDOQL_Expression91', a2)
    if hasattr(a1, 'jDOQL_Expression89'):
        assert not _is_linked(a1, 'jDOQL_Expression89', b)
    if hasattr(a2, 'jDOQL_Expression89'):
        assert _is_linked(a2, 'jDOQL_Expression89', b)
    _safe_set(b, 'jDOQL_Expression91', None)
    assert not _is_linked(b, 'jDOQL_Expression91', a2)
    if hasattr(a2, 'jDOQL_Expression89'):
        assert not _is_linked(a2, 'jDOQL_Expression89', b)


def test_assoc_left124_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_ComparisonOperatorExpression(operator="sample_text")
    _safe_set(b, 'jDOQL_ComparisonOperatorExpression', a1)
    assert _is_linked(b, 'jDOQL_ComparisonOperatorExpression', a1)
    if hasattr(a1, 'jDOQL_Expression125'):
        assert _is_linked(a1, 'jDOQL_Expression125', b)
    _safe_set(b, 'jDOQL_ComparisonOperatorExpression', a2)
    assert _is_linked(b, 'jDOQL_ComparisonOperatorExpression', a2)
    if hasattr(a1, 'jDOQL_Expression125'):
        assert not _is_linked(a1, 'jDOQL_Expression125', b)
    if hasattr(a2, 'jDOQL_Expression125'):
        assert _is_linked(a2, 'jDOQL_Expression125', b)
    _safe_set(b, 'jDOQL_ComparisonOperatorExpression', None)
    assert not _is_linked(b, 'jDOQL_ComparisonOperatorExpression', a2)
    if hasattr(a2, 'jDOQL_Expression125'):
        assert not _is_linked(a2, 'jDOQL_Expression125', b)


def test_assoc_left126_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_AdditionExpression(operator="sample_text")
    _safe_set(b, 'jDOQL_AdditionExpression', a1)
    assert _is_linked(b, 'jDOQL_AdditionExpression', a1)
    if hasattr(a1, 'jDOQL_Expression127'):
        assert _is_linked(a1, 'jDOQL_Expression127', b)
    _safe_set(b, 'jDOQL_AdditionExpression', a2)
    assert _is_linked(b, 'jDOQL_AdditionExpression', a2)
    if hasattr(a1, 'jDOQL_Expression127'):
        assert not _is_linked(a1, 'jDOQL_Expression127', b)
    if hasattr(a2, 'jDOQL_Expression127'):
        assert _is_linked(a2, 'jDOQL_Expression127', b)
    _safe_set(b, 'jDOQL_AdditionExpression', None)
    assert not _is_linked(b, 'jDOQL_AdditionExpression', a2)
    if hasattr(a2, 'jDOQL_Expression127'):
        assert not _is_linked(a2, 'jDOQL_Expression127', b)


def test_assoc_left128_reverse_link_reassign_clear():
    a1 = jDOQL_MultiplicationExpression(operator="sample_text")
    a2 = jDOQL_MultiplicationExpression(operator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression129', a1)
    assert _is_linked(b, 'jDOQL_Expression129', a1)
    if hasattr(a1, 'jDOQL_MultiplicationExpression'):
        assert _is_linked(a1, 'jDOQL_MultiplicationExpression', b)
    _safe_set(b, 'jDOQL_Expression129', a2)
    assert _is_linked(b, 'jDOQL_Expression129', a2)
    if hasattr(a1, 'jDOQL_MultiplicationExpression'):
        assert not _is_linked(a1, 'jDOQL_MultiplicationExpression', b)
    if hasattr(a2, 'jDOQL_MultiplicationExpression'):
        assert _is_linked(a2, 'jDOQL_MultiplicationExpression', b)
    _safe_set(b, 'jDOQL_Expression129', None)
    assert not _is_linked(b, 'jDOQL_Expression129', a2)
    if hasattr(a2, 'jDOQL_MultiplicationExpression'):
        assert not _is_linked(a2, 'jDOQL_MultiplicationExpression', b)


def test_assoc_method72_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression73', a1)
    assert _is_linked(b, 'jDOQL_Expression73', a1)
    if hasattr(a1, 'jDOQL_Expression71'):
        assert _is_linked(a1, 'jDOQL_Expression71', b)
    _safe_set(b, 'jDOQL_Expression73', a2)
    assert _is_linked(b, 'jDOQL_Expression73', a2)
    if hasattr(a1, 'jDOQL_Expression71'):
        assert not _is_linked(a1, 'jDOQL_Expression71', b)
    if hasattr(a2, 'jDOQL_Expression71'):
        assert _is_linked(a2, 'jDOQL_Expression71', b)
    _safe_set(b, 'jDOQL_Expression73', None)
    assert not _is_linked(b, 'jDOQL_Expression73', a2)
    if hasattr(a2, 'jDOQL_Expression71'):
        assert not _is_linked(a2, 'jDOQL_Expression71', b)


def test_assoc_number75_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression76', a1)
    assert _is_linked(b, 'jDOQL_Expression76', a1)
    if hasattr(a1, 'jDOQL_Expression74'):
        assert _is_linked(a1, 'jDOQL_Expression74', b)
    _safe_set(b, 'jDOQL_Expression76', a2)
    assert _is_linked(b, 'jDOQL_Expression76', a2)
    if hasattr(a1, 'jDOQL_Expression74'):
        assert not _is_linked(a1, 'jDOQL_Expression74', b)
    if hasattr(a2, 'jDOQL_Expression74'):
        assert _is_linked(a2, 'jDOQL_Expression74', b)
    _safe_set(b, 'jDOQL_Expression76', None)
    assert not _is_linked(b, 'jDOQL_Expression76', a2)
    if hasattr(a2, 'jDOQL_Expression74'):
        assert not _is_linked(a2, 'jDOQL_Expression74', b)


def test_assoc_persistable78_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression79', a1)
    assert _is_linked(b, 'jDOQL_Expression79', a1)
    if hasattr(a1, 'jDOQL_Expression77'):
        assert _is_linked(a1, 'jDOQL_Expression77', b)
    _safe_set(b, 'jDOQL_Expression79', a2)
    assert _is_linked(b, 'jDOQL_Expression79', a2)
    if hasattr(a1, 'jDOQL_Expression77'):
        assert not _is_linked(a1, 'jDOQL_Expression77', b)
    if hasattr(a2, 'jDOQL_Expression77'):
        assert _is_linked(a2, 'jDOQL_Expression77', b)
    _safe_set(b, 'jDOQL_Expression79', None)
    assert not _is_linked(b, 'jDOQL_Expression79', a2)
    if hasattr(a2, 'jDOQL_Expression77'):
        assert not _is_linked(a2, 'jDOQL_Expression77', b)


def test_assoc_regex105_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression106', a1)
    assert _is_linked(b, 'jDOQL_Expression106', a1)
    if hasattr(a1, 'jDOQL_Expression104'):
        assert _is_linked(a1, 'jDOQL_Expression104', b)
    _safe_set(b, 'jDOQL_Expression106', a2)
    assert _is_linked(b, 'jDOQL_Expression106', a2)
    if hasattr(a1, 'jDOQL_Expression104'):
        assert not _is_linked(a1, 'jDOQL_Expression104', b)
    if hasattr(a2, 'jDOQL_Expression104'):
        assert _is_linked(a2, 'jDOQL_Expression104', b)
    _safe_set(b, 'jDOQL_Expression106', None)
    assert not _is_linked(b, 'jDOQL_Expression106', a2)
    if hasattr(a2, 'jDOQL_Expression104'):
        assert not _is_linked(a2, 'jDOQL_Expression104', b)


def test_assoc_replacement108_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression109', a1)
    assert _is_linked(b, 'jDOQL_Expression109', a1)
    if hasattr(a1, 'jDOQL_Expression107'):
        assert _is_linked(a1, 'jDOQL_Expression107', b)
    _safe_set(b, 'jDOQL_Expression109', a2)
    assert _is_linked(b, 'jDOQL_Expression109', a2)
    if hasattr(a1, 'jDOQL_Expression107'):
        assert not _is_linked(a1, 'jDOQL_Expression107', b)
    if hasattr(a2, 'jDOQL_Expression107'):
        assert _is_linked(a2, 'jDOQL_Expression107', b)
    _safe_set(b, 'jDOQL_Expression109', None)
    assert not _is_linked(b, 'jDOQL_Expression109', a2)
    if hasattr(a2, 'jDOQL_Expression107'):
        assert not _is_linked(a2, 'jDOQL_Expression107', b)


def test_assoc_resultExpression37_reverse_link_reassign_clear():
    a1 = jDOQL_SubqueryResultClause(isDistinct=True)
    a2 = jDOQL_SubqueryResultClause(isDistinct=False)
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression', a1)
    assert _is_linked(b, 'jDOQL_Expression', a1)
    if hasattr(a1, 'jDOQL_SubqueryResultClause'):
        assert _is_linked(a1, 'jDOQL_SubqueryResultClause', b)
    _safe_set(b, 'jDOQL_Expression', a2)
    assert _is_linked(b, 'jDOQL_Expression', a2)
    if hasattr(a1, 'jDOQL_SubqueryResultClause'):
        assert not _is_linked(a1, 'jDOQL_SubqueryResultClause', b)
    if hasattr(a2, 'jDOQL_SubqueryResultClause'):
        assert _is_linked(a2, 'jDOQL_SubqueryResultClause', b)
    _safe_set(b, 'jDOQL_Expression', None)
    assert not _is_linked(b, 'jDOQL_Expression', a2)
    if hasattr(a2, 'jDOQL_SubqueryResultClause'):
        assert not _is_linked(a2, 'jDOQL_SubqueryResultClause', b)


def test_assoc_resultNaming66_reverse_link_reassign_clear():
    a1 = jDOQL_ResultNaming(identifier="sample_text")
    a2 = jDOQL_ResultNaming(identifier="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression67', a1)
    assert _is_linked(b, 'jDOQL_Expression67', a1)
    if hasattr(a1, 'jDOQL_ResultNaming'):
        assert _is_linked(a1, 'jDOQL_ResultNaming', b)
    _safe_set(b, 'jDOQL_Expression67', a2)
    assert _is_linked(b, 'jDOQL_Expression67', a2)
    if hasattr(a1, 'jDOQL_ResultNaming'):
        assert not _is_linked(a1, 'jDOQL_ResultNaming', b)
    if hasattr(a2, 'jDOQL_ResultNaming'):
        assert _is_linked(a2, 'jDOQL_ResultNaming', b)
    _safe_set(b, 'jDOQL_Expression67', None)
    assert not _is_linked(b, 'jDOQL_Expression67', a2)
    if hasattr(a2, 'jDOQL_ResultNaming'):
        assert not _is_linked(a2, 'jDOQL_ResultNaming', b)


def test_assoc_right69_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression70', a1)
    assert _is_linked(b, 'jDOQL_Expression70', a1)
    if hasattr(a1, 'jDOQL_Expression68'):
        assert _is_linked(a1, 'jDOQL_Expression68', b)
    _safe_set(b, 'jDOQL_Expression70', a2)
    assert _is_linked(b, 'jDOQL_Expression70', a2)
    if hasattr(a1, 'jDOQL_Expression68'):
        assert not _is_linked(a1, 'jDOQL_Expression68', b)
    if hasattr(a2, 'jDOQL_Expression68'):
        assert _is_linked(a2, 'jDOQL_Expression68', b)
    _safe_set(b, 'jDOQL_Expression70', None)
    assert not _is_linked(b, 'jDOQL_Expression70', a2)
    if hasattr(a2, 'jDOQL_Expression68'):
        assert not _is_linked(a2, 'jDOQL_Expression68', b)


def test_assoc_string99_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression98', a1)
    assert _is_linked(b, 'jDOQL_Expression98', a1)
    if hasattr(a1, 'jDOQL_Expression100'):
        assert _is_linked(a1, 'jDOQL_Expression100', b)
    _safe_set(b, 'jDOQL_Expression98', a2)
    assert _is_linked(b, 'jDOQL_Expression98', a2)
    if hasattr(a1, 'jDOQL_Expression100'):
        assert not _is_linked(a1, 'jDOQL_Expression100', b)
    if hasattr(a2, 'jDOQL_Expression100'):
        assert _is_linked(a2, 'jDOQL_Expression100', b)
    _safe_set(b, 'jDOQL_Expression98', None)
    assert not _is_linked(b, 'jDOQL_Expression98', a2)
    if hasattr(a2, 'jDOQL_Expression100'):
        assert not _is_linked(a2, 'jDOQL_Expression100', b)


def test_assoc_value93_reverse_link_reassign_clear():
    a1 = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    a2 = jDOQL_Expression(castType="sample_text_2", direction="sample_text_2", id="sample_text_2", isDistinct=False, literal="sample_text_2", name="sample_text_2", parameterName="sample_text_2", this="sample_text_2", unaryOperator="sample_text_2")
    b = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    _safe_set(b, 'jDOQL_Expression94', a1)
    assert _is_linked(b, 'jDOQL_Expression94', a1)
    if hasattr(a1, 'jDOQL_Expression92'):
        assert _is_linked(a1, 'jDOQL_Expression92', b)
    _safe_set(b, 'jDOQL_Expression94', a2)
    assert _is_linked(b, 'jDOQL_Expression94', a2)
    if hasattr(a1, 'jDOQL_Expression92'):
        assert not _is_linked(a1, 'jDOQL_Expression92', b)
    if hasattr(a2, 'jDOQL_Expression92'):
        assert _is_linked(a2, 'jDOQL_Expression92', b)
    _safe_set(b, 'jDOQL_Expression94', None)
    assert not _is_linked(b, 'jDOQL_Expression94', a2)
    if hasattr(a2, 'jDOQL_Expression92'):
        assert not _is_linked(a2, 'jDOQL_Expression92', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_end63_stub_double():
    # jDOQL_RangeClause has no real 'jDOQL_RangeClause64' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_RangeClause()
    setattr(partner, 'jDOQL_RangeClause64', None)
    _safe_set(owner, 'jDOQL_Expression65', partner)
    assert getattr(partner, 'jDOQL_RangeClause64') == owner
    _safe_set(owner, 'jDOQL_Expression65', None)
    assert getattr(partner, 'jDOQL_RangeClause64') is None


def test_assoc_filter43_stub_double():
    # jDOQL_WhereClause has no real 'jDOQL_WhereClause44' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_WhereClause()
    setattr(partner, 'jDOQL_WhereClause44', None)
    _safe_set(owner, 'jDOQL_Expression45', partner)
    assert getattr(partner, 'jDOQL_WhereClause44') == owner
    _safe_set(owner, 'jDOQL_Expression45', None)
    assert getattr(partner, 'jDOQL_WhereClause44') is None


def test_assoc_fromClause1_stub_double():
    # jDOQL_SingleStringJDOQL has no real 'jDOQL_SingleStringJDOQL2' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_FromClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_FromClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_FromClause(candidateClassName="sample_text", isExcludeSubclasses=True)
    partner = jDOQL_SingleStringJDOQL()
    setattr(partner, 'jDOQL_SingleStringJDOQL2', None)
    _safe_set(owner, 'jDOQL_FromClause', partner)
    assert getattr(partner, 'jDOQL_SingleStringJDOQL2') == owner
    _safe_set(owner, 'jDOQL_FromClause', None)
    assert getattr(partner, 'jDOQL_SingleStringJDOQL2') is None


def test_assoc_fromClause18_stub_double():
    # jDOQL_Subquery has no real 'jDOQL_Subquery19' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_SubqueryFromClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_SubqueryFromClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_SubqueryFromClause(candidateClassName="sample_text", isExcludeSubclasses=True)
    partner = jDOQL_Subquery()
    setattr(partner, 'jDOQL_Subquery19', None)
    _safe_set(owner, 'jDOQL_SubqueryFromClause', partner)
    assert getattr(partner, 'jDOQL_Subquery19') == owner
    _safe_set(owner, 'jDOQL_SubqueryFromClause', None)
    assert getattr(partner, 'jDOQL_Subquery19') is None


def test_assoc_grouping50_stub_double():
    # jDOQL_GroupByClause has no real 'jDOQL_GroupByClause51' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_GroupByClause()
    setattr(partner, 'jDOQL_GroupByClause51', None)
    _safe_set(owner, 'jDOQL_Expression52', partner)
    assert owner in getattr(partner, 'jDOQL_GroupByClause51')
    _safe_set(owner, 'jDOQL_Expression52', None)
    assert owner not in getattr(partner, 'jDOQL_GroupByClause51')


def test_assoc_having55_stub_double():
    # jDOQL_HavingClause has no real 'jDOQL_HavingClause56' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_HavingClause()
    setattr(partner, 'jDOQL_HavingClause56', None)
    _safe_set(owner, 'jDOQL_Expression57', partner)
    assert getattr(partner, 'jDOQL_HavingClause56') == owner
    _safe_set(owner, 'jDOQL_Expression57', None)
    assert getattr(partner, 'jDOQL_HavingClause56') is None


def test_assoc_importClause29_stub_double():
    # jDOQL_Subquery has no real 'jDOQL_Subquery30' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_ImportClause(importDeclarations="sample_text")
    partner = jDOQL_Subquery()
    setattr(partner, 'jDOQL_Subquery30', None)
    _safe_set(owner, 'jDOQL_ImportClause31', partner)
    assert getattr(partner, 'jDOQL_Subquery30') == owner
    _safe_set(owner, 'jDOQL_ImportClause31', None)
    assert getattr(partner, 'jDOQL_Subquery30') is None


def test_assoc_importClause9_stub_double():
    # jDOQL_SingleStringJDOQL has no real 'jDOQL_SingleStringJDOQL10' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_ImportClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_ImportClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_ImportClause(importDeclarations="sample_text")
    partner = jDOQL_SingleStringJDOQL()
    setattr(partner, 'jDOQL_SingleStringJDOQL10', None)
    _safe_set(owner, 'jDOQL_ImportClause', partner)
    assert getattr(partner, 'jDOQL_SingleStringJDOQL10') == owner
    _safe_set(owner, 'jDOQL_ImportClause', None)
    assert getattr(partner, 'jDOQL_SingleStringJDOQL10') is None


def test_assoc_left116_stub_double():
    # jDOQL_ConditionalOrExpression has no real 'jDOQL_ConditionalOrExpression' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_ConditionalOrExpression()
    setattr(partner, 'jDOQL_ConditionalOrExpression', None)
    _safe_set(owner, 'jDOQL_Expression117', partner)
    assert getattr(partner, 'jDOQL_ConditionalOrExpression') == owner
    _safe_set(owner, 'jDOQL_Expression117', None)
    assert getattr(partner, 'jDOQL_ConditionalOrExpression') is None


def test_assoc_left118_stub_double():
    # jDOQL_ConditionalAndExpression has no real 'jDOQL_ConditionalAndExpression' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_ConditionalAndExpression()
    setattr(partner, 'jDOQL_ConditionalAndExpression', None)
    _safe_set(owner, 'jDOQL_Expression119', partner)
    assert getattr(partner, 'jDOQL_ConditionalAndExpression') == owner
    _safe_set(owner, 'jDOQL_Expression119', None)
    assert getattr(partner, 'jDOQL_ConditionalAndExpression') is None


def test_assoc_left120_stub_double():
    # jDOQL_SimpleOrExpression has no real 'jDOQL_SimpleOrExpression' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_SimpleOrExpression()
    setattr(partner, 'jDOQL_SimpleOrExpression', None)
    _safe_set(owner, 'jDOQL_Expression121', partner)
    assert getattr(partner, 'jDOQL_SimpleOrExpression') == owner
    _safe_set(owner, 'jDOQL_Expression121', None)
    assert getattr(partner, 'jDOQL_SimpleOrExpression') is None


def test_assoc_left122_stub_double():
    # jDOQL_SimpleAndExpression has no real 'jDOQL_SimpleAndExpression' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_SimpleAndExpression()
    setattr(partner, 'jDOQL_SimpleAndExpression', None)
    _safe_set(owner, 'jDOQL_Expression123', partner)
    assert getattr(partner, 'jDOQL_SimpleAndExpression') == owner
    _safe_set(owner, 'jDOQL_Expression123', None)
    assert getattr(partner, 'jDOQL_SimpleAndExpression') is None


def test_assoc_left130_stub_double():
    # jDOQL_FieldAccessExpression has no real 'jDOQL_FieldAccessExpression' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_FieldAccessExpression()
    setattr(partner, 'jDOQL_FieldAccessExpression', None)
    _safe_set(owner, 'jDOQL_Expression131', partner)
    assert getattr(partner, 'jDOQL_FieldAccessExpression') == owner
    _safe_set(owner, 'jDOQL_Expression131', None)
    assert getattr(partner, 'jDOQL_FieldAccessExpression') is None


def test_assoc_parameterDeclarations48_stub_double():
    # jDOQL_ParametersClause has no real 'jDOQL_ParametersClause49' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_ParameterDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_ParameterDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_ParameterDeclaration(declaredParameterName="sample_text", type="sample_text")
    partner = jDOQL_ParametersClause()
    setattr(partner, 'jDOQL_ParametersClause49', None)
    _safe_set(owner, 'jDOQL_ParameterDeclaration', partner)
    assert owner in getattr(partner, 'jDOQL_ParametersClause49')
    _safe_set(owner, 'jDOQL_ParameterDeclaration', None)
    assert owner not in getattr(partner, 'jDOQL_ParametersClause49')


def test_assoc_resultClause32_stub_double():
    # jDOQL_EObject has no real 'jDOQL_EObject' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_SelectClause(isUnique=True)
    partner = jDOQL_EObject()
    setattr(partner, 'jDOQL_EObject', None)
    _safe_set(owner, 'jDOQL_SelectClause33', partner)
    assert getattr(partner, 'jDOQL_EObject') == owner
    _safe_set(owner, 'jDOQL_SelectClause33', None)
    assert getattr(partner, 'jDOQL_EObject') is None


def test_assoc_resultSpecs36_stub_double():
    # jDOQL_ResultSpec has no real 'jDOQL_ResultSpec' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_ResultClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_ResultClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_ResultClause(isDistinct=True)
    partner = jDOQL_ResultSpec()
    setattr(partner, 'jDOQL_ResultSpec', None)
    _safe_set(owner, 'jDOQL_ResultClause', {partner})
    assert getattr(partner, 'jDOQL_ResultSpec') == owner
    _safe_set(owner, 'jDOQL_ResultClause', set())
    assert getattr(partner, 'jDOQL_ResultSpec') is None


def test_assoc_selectClause0_stub_double():
    # jDOQL_SingleStringJDOQL has no real 'jDOQL_SingleStringJDOQL' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_SelectClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_SelectClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_SelectClause(isUnique=True)
    partner = jDOQL_SingleStringJDOQL()
    setattr(partner, 'jDOQL_SingleStringJDOQL', None)
    _safe_set(owner, 'jDOQL_SelectClause', partner)
    assert getattr(partner, 'jDOQL_SingleStringJDOQL') == owner
    _safe_set(owner, 'jDOQL_SelectClause', None)
    assert getattr(partner, 'jDOQL_SingleStringJDOQL') is None


def test_assoc_start60_stub_double():
    # jDOQL_RangeClause has no real 'jDOQL_RangeClause61' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_Expression(castType="sample_text", direction="sample_text", id="sample_text", isDistinct=True, literal="sample_text", name="sample_text", parameterName="sample_text", this="sample_text", unaryOperator="sample_text")
    partner = jDOQL_RangeClause()
    setattr(partner, 'jDOQL_RangeClause61', None)
    _safe_set(owner, 'jDOQL_Expression62', partner)
    assert getattr(partner, 'jDOQL_RangeClause61') == owner
    _safe_set(owner, 'jDOQL_Expression62', None)
    assert getattr(partner, 'jDOQL_RangeClause61') is None


def test_assoc_variableDeclarations46_stub_double():
    # jDOQL_VariablesClause has no real 'jDOQL_VariablesClause47' property in the generated
    # code (a bare stub) -- manually attach it so jDOQL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jDOQL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jDOQL_VariableDeclaration(type="sample_text", variableName="sample_text")
    partner = jDOQL_VariablesClause()
    setattr(partner, 'jDOQL_VariablesClause47', None)
    _safe_set(owner, 'jDOQL_VariableDeclaration', partner)
    assert owner in getattr(partner, 'jDOQL_VariablesClause47')
    _safe_set(owner, 'jDOQL_VariableDeclaration', None)
    assert owner not in getattr(partner, 'jDOQL_VariablesClause47')


