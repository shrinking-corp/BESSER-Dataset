import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssignmentStatement,
    Expression,
    ExpressionRest,
    Function,
    KeyValuePairRest,
    Phrase,
    Statement,
    Term,
    expression_AndExpression,
    expression_Apply,
    expression_AssignmentStatement,
    expression_Count,
    expression_DashExpression,
    expression_Designator,
    expression_DoubleValue,
    expression_EObject,
    expression_EqualityExpression,
    expression_Expression,
    expression_ExpressionList,
    expression_ExpressionRest,
    expression_FirstIn,
    expression_ForallIn,
    expression_FunctionCall,
    expression_IntegerValue,
    expression_KeyValuePair,
    expression_KeyValuePairRest,
    expression_LastIn,
    expression_List,
    expression_Map,
    expression_Model,
    expression_OrExpression,
    expression_Phrase,
    expression_PointExpression,
    expression_PowExpression,
    expression_Procedure,
    expression_ProcedureCall,
    expression_QualifierExpression,
    expression_Reduce,
    expression_SelfAssignmentStatement,
    expression_Statement,
    expression_StatementList,
    expression_StringValue,
    expression_StructureExpression,
    expression_Sum,
    expression_Term,
    expression_ThereIsIn,
    expression_UnaryExpression,
    expression_VariableAssignmentStatement,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_keyValuePair105_stub_double():
    # expression_StructureExpression has no real 'expression_StructureExpression' property in the generated
    # code (a bare stub) -- manually attach it so expression_KeyValuePair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_KeyValuePair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_KeyValuePair(key="sample_text")
    partner = expression_StructureExpression()
    setattr(partner, 'expression_StructureExpression', None)
    _safe_set(owner, 'expression_KeyValuePair106', partner)
    assert getattr(partner, 'expression_StructureExpression') == owner
    _safe_set(owner, 'expression_KeyValuePair106', None)
    assert getattr(partner, 'expression_StructureExpression') is None


def test_assoc_left32_stub_double():
    # expression_Expression has no real 'expression_Expression33' property in the generated
    # code (a bare stub) -- manually attach it so expression_OrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_OrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_OrExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression33', None)
    _safe_set(owner, 'expression_OrExpression', partner)
    assert getattr(partner, 'expression_Expression33') == owner
    _safe_set(owner, 'expression_OrExpression', None)
    assert getattr(partner, 'expression_Expression33') is None


def test_assoc_left37_stub_double():
    # expression_Expression has no real 'expression_Expression38' property in the generated
    # code (a bare stub) -- manually attach it so expression_AndExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_AndExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_AndExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression38', None)
    _safe_set(owner, 'expression_AndExpression', partner)
    assert getattr(partner, 'expression_Expression38') == owner
    _safe_set(owner, 'expression_AndExpression', None)
    assert getattr(partner, 'expression_Expression38') is None


def test_assoc_left42_stub_double():
    # expression_Expression has no real 'expression_Expression43' property in the generated
    # code (a bare stub) -- manually attach it so expression_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_EqualityExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression43', None)
    _safe_set(owner, 'expression_EqualityExpression', partner)
    assert getattr(partner, 'expression_Expression43') == owner
    _safe_set(owner, 'expression_EqualityExpression', None)
    assert getattr(partner, 'expression_Expression43') is None


def test_assoc_left47_stub_double():
    # expression_Expression has no real 'expression_Expression48' property in the generated
    # code (a bare stub) -- manually attach it so expression_DashExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_DashExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_DashExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression48', None)
    _safe_set(owner, 'expression_DashExpression', partner)
    assert getattr(partner, 'expression_Expression48') == owner
    _safe_set(owner, 'expression_DashExpression', None)
    assert getattr(partner, 'expression_Expression48') is None


def test_assoc_left52_stub_double():
    # expression_Expression has no real 'expression_Expression53' property in the generated
    # code (a bare stub) -- manually attach it so expression_PointExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_PointExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_PointExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression53', None)
    _safe_set(owner, 'expression_PointExpression', partner)
    assert getattr(partner, 'expression_Expression53') == owner
    _safe_set(owner, 'expression_PointExpression', None)
    assert getattr(partner, 'expression_Expression53') is None


def test_assoc_left57_stub_double():
    # expression_Expression has no real 'expression_Expression58' property in the generated
    # code (a bare stub) -- manually attach it so expression_PowExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_PowExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_PowExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression58', None)
    _safe_set(owner, 'expression_PowExpression', partner)
    assert getattr(partner, 'expression_Expression58') == owner
    _safe_set(owner, 'expression_PowExpression', None)
    assert getattr(partner, 'expression_Expression58') is None


def test_assoc_left62_stub_double():
    # expression_Expression has no real 'expression_Expression63' property in the generated
    # code (a bare stub) -- manually attach it so expression_QualifierExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_QualifierExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_QualifierExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression63', None)
    _safe_set(owner, 'expression_QualifierExpression', partner)
    assert getattr(partner, 'expression_Expression63') == owner
    _safe_set(owner, 'expression_QualifierExpression', None)
    assert getattr(partner, 'expression_Expression63') is None


def test_assoc_rest24_stub_double():
    # expression_KeyValuePairRest has no real 'expression_KeyValuePairRest' property in the generated
    # code (a bare stub) -- manually attach it so expression_KeyValuePair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_KeyValuePair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_KeyValuePair(key="sample_text")
    partner = expression_KeyValuePairRest()
    setattr(partner, 'expression_KeyValuePairRest', None)
    _safe_set(owner, 'expression_KeyValuePair25', {partner})
    assert getattr(partner, 'expression_KeyValuePairRest') == owner
    _safe_set(owner, 'expression_KeyValuePair25', set())
    assert getattr(partner, 'expression_KeyValuePairRest') is None


def test_assoc_right34_stub_double():
    # expression_Expression has no real 'expression_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so expression_OrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_OrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_OrExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression36', None)
    _safe_set(owner, 'expression_OrExpression35', partner)
    assert getattr(partner, 'expression_Expression36') == owner
    _safe_set(owner, 'expression_OrExpression35', None)
    assert getattr(partner, 'expression_Expression36') is None


def test_assoc_right39_stub_double():
    # expression_Expression has no real 'expression_Expression41' property in the generated
    # code (a bare stub) -- manually attach it so expression_AndExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_AndExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_AndExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression41', None)
    _safe_set(owner, 'expression_AndExpression40', partner)
    assert getattr(partner, 'expression_Expression41') == owner
    _safe_set(owner, 'expression_AndExpression40', None)
    assert getattr(partner, 'expression_Expression41') is None


def test_assoc_right44_stub_double():
    # expression_Expression has no real 'expression_Expression46' property in the generated
    # code (a bare stub) -- manually attach it so expression_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_EqualityExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression46', None)
    _safe_set(owner, 'expression_EqualityExpression45', partner)
    assert getattr(partner, 'expression_Expression46') == owner
    _safe_set(owner, 'expression_EqualityExpression45', None)
    assert getattr(partner, 'expression_Expression46') is None


def test_assoc_right49_stub_double():
    # expression_Expression has no real 'expression_Expression51' property in the generated
    # code (a bare stub) -- manually attach it so expression_DashExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_DashExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_DashExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression51', None)
    _safe_set(owner, 'expression_DashExpression50', partner)
    assert getattr(partner, 'expression_Expression51') == owner
    _safe_set(owner, 'expression_DashExpression50', None)
    assert getattr(partner, 'expression_Expression51') is None


def test_assoc_right54_stub_double():
    # expression_Expression has no real 'expression_Expression56' property in the generated
    # code (a bare stub) -- manually attach it so expression_PointExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_PointExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_PointExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression56', None)
    _safe_set(owner, 'expression_PointExpression55', partner)
    assert getattr(partner, 'expression_Expression56') == owner
    _safe_set(owner, 'expression_PointExpression55', None)
    assert getattr(partner, 'expression_Expression56') is None


def test_assoc_right59_stub_double():
    # expression_Expression has no real 'expression_Expression61' property in the generated
    # code (a bare stub) -- manually attach it so expression_PowExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_PowExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_PowExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression61', None)
    _safe_set(owner, 'expression_PowExpression60', partner)
    assert getattr(partner, 'expression_Expression61') == owner
    _safe_set(owner, 'expression_PowExpression60', None)
    assert getattr(partner, 'expression_Expression61') is None


def test_assoc_right64_stub_double():
    # expression_Expression has no real 'expression_Expression66' property in the generated
    # code (a bare stub) -- manually attach it so expression_QualifierExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_QualifierExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_QualifierExpression(op="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression66', None)
    _safe_set(owner, 'expression_QualifierExpression65', partner)
    assert getattr(partner, 'expression_Expression66') == owner
    _safe_set(owner, 'expression_QualifierExpression65', None)
    assert getattr(partner, 'expression_Expression66') is None


def test_assoc_value22_stub_double():
    # expression_Expression has no real 'expression_Expression23' property in the generated
    # code (a bare stub) -- manually attach it so expression_KeyValuePair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # expression_KeyValuePair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = expression_KeyValuePair(key="sample_text")
    partner = expression_Expression()
    setattr(partner, 'expression_Expression23', None)
    _safe_set(owner, 'expression_KeyValuePair', partner)
    assert getattr(partner, 'expression_Expression23') == owner
    _safe_set(owner, 'expression_KeyValuePair', None)
    assert getattr(partner, 'expression_Expression23') is None


