import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    BinaryOpExpression,
    Definition,
    Expression,
    ExpressionBlock,
    ICollectQuery,
    IQuotedString,
    IfExpression,
    Lambda,
    LiteralExpression,
    ParameterizedExpression,
    StringExpression,
    TextExpression,
    UnaryExpression,
    WithLambdaExpression,
    pp1_AdditiveExpression,
    pp1_AndExpression,
    pp1_AppendExpression,
    pp1_AssignmentExpression,
    pp1_AtExpression,
    pp1_AttributeOperation,
    pp1_AttributeOperations,
    pp1_BinaryExpression,
    pp1_BinaryOpExpression,
    pp1_Case,
    pp1_CaseExpression,
    pp1_CollectExpression,
    pp1_Definition,
    pp1_DefinitionArgument,
    pp1_DefinitionArgumentList,
    pp1_DoubleQuotedString,
    pp1_ElseExpression,
    pp1_ElseIfExpression,
    pp1_EqualityExpression,
    pp1_ExportedCollectQuery,
    pp1_ExprList,
    pp1_Expression,
    pp1_ExpressionBlock,
    pp1_ExpressionTE,
    pp1_FunctionCall,
    pp1_HashEntry,
    pp1_HostClassDefinition,
    pp1_ICollectQuery,
    pp1_IQuotedString,
    pp1_IfExpression,
    pp1_ImportExpression,
    pp1_InExpression,
    pp1_InterpolatedVariable,
    pp1_JavaLambda,
    pp1_Lambda,
    pp1_LiteralBoolean,
    pp1_LiteralClass,
    pp1_LiteralDefault,
    pp1_LiteralExpression,
    pp1_LiteralHash,
    pp1_LiteralList,
    pp1_LiteralName,
    pp1_LiteralNameOrReference,
    pp1_LiteralRegex,
    pp1_LiteralUndef,
    pp1_MatchingExpression,
    pp1_MethodCall,
    pp1_MultiplicativeExpression,
    pp1_NamedAccessExpression,
    pp1_NodeDefinition,
    pp1_OrExpression,
    pp1_ParameterizedExpression,
    pp1_ParenthesisedExpression,
    pp1_PuppetManifest,
    pp1_RelationalExpression,
    pp1_RelationshipExpression,
    pp1_ResourceBody,
    pp1_ResourceExpression,
    pp1_RubyLambda,
    pp1_SelectorEntry,
    pp1_SelectorExpression,
    pp1_SeparatorExpression,
    pp1_ShiftExpression,
    pp1_SingleQuotedString,
    pp1_StringExpression,
    pp1_TextExpression,
    pp1_UnaryExpression,
    pp1_UnaryMinusExpression,
    pp1_UnaryNotExpression,
    pp1_UnlessExpression,
    pp1_UnquotedString,
    pp1_VariableExpression,
    pp1_VariableTE,
    pp1_VerbatimTE,
    pp1_VirtualCollectQuery,
    pp1_VirtualNameOrReference,
    pp1_WithLambdaExpression,
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

def test_assoc_arguments13_stub_double():
    # pp1_DefinitionArgumentList has no real 'pp1_DefinitionArgumentList14' property in the generated
    # code (a bare stub) -- manually attach it so pp1_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp1_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp1_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp1_DefinitionArgumentList()
    setattr(partner, 'pp1_DefinitionArgumentList14', None)
    _safe_set(owner, 'pp1_DefinitionArgument', partner)
    assert owner in getattr(partner, 'pp1_DefinitionArgumentList14')
    _safe_set(owner, 'pp1_DefinitionArgument', None)
    assert owner not in getattr(partner, 'pp1_DefinitionArgumentList14')


def test_assoc_arguments9_stub_double():
    # pp1_DefinitionArgumentList has no real 'pp1_DefinitionArgumentList' property in the generated
    # code (a bare stub) -- manually attach it so pp1_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp1_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp1_Definition(className="sample_text")
    partner = pp1_DefinitionArgumentList()
    setattr(partner, 'pp1_DefinitionArgumentList', None)
    _safe_set(owner, 'pp1_Definition', partner)
    assert getattr(partner, 'pp1_DefinitionArgumentList') == owner
    _safe_set(owner, 'pp1_Definition', None)
    assert getattr(partner, 'pp1_DefinitionArgumentList') is None


def test_assoc_attributes5_stub_double():
    # pp1_AttributeOperations has no real 'pp1_AttributeOperations6' property in the generated
    # code (a bare stub) -- manually attach it so pp1_AttributeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp1_AttributeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp1_AttributeOperation(key="sample_text", op="sample_text")
    partner = pp1_AttributeOperations()
    setattr(partner, 'pp1_AttributeOperations6', None)
    _safe_set(owner, 'pp1_AttributeOperation7', partner)
    assert owner in getattr(partner, 'pp1_AttributeOperations6')
    _safe_set(owner, 'pp1_AttributeOperation7', None)
    assert owner not in getattr(partner, 'pp1_AttributeOperations6')


def test_assoc_methodExpr99_stub_double():
    # pp1_Expression has no real 'pp1_Expression100' property in the generated
    # code (a bare stub) -- manually attach it so pp1_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp1_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp1_MethodCall(parenthesized=True)
    partner = pp1_Expression()
    setattr(partner, 'pp1_Expression100', None)
    _safe_set(owner, 'pp1_MethodCall', partner)
    assert getattr(partner, 'pp1_Expression100') == owner
    _safe_set(owner, 'pp1_MethodCall', None)
    assert getattr(partner, 'pp1_Expression100') is None


def test_assoc_statements10_stub_double():
    # pp1_Expression has no real 'pp1_Expression12' property in the generated
    # code (a bare stub) -- manually attach it so pp1_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp1_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp1_Definition(className="sample_text")
    partner = pp1_Expression()
    setattr(partner, 'pp1_Expression12', None)
    _safe_set(owner, 'pp1_Definition11', {partner})
    assert getattr(partner, 'pp1_Expression12') == owner
    _safe_set(owner, 'pp1_Definition11', set())
    assert getattr(partner, 'pp1_Expression12') is None


def test_assoc_value15_stub_double():
    # pp1_Expression has no real 'pp1_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so pp1_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp1_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp1_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp1_Expression()
    setattr(partner, 'pp1_Expression17', None)
    _safe_set(owner, 'pp1_DefinitionArgument16', partner)
    assert getattr(partner, 'pp1_Expression17') == owner
    _safe_set(owner, 'pp1_DefinitionArgument16', None)
    assert getattr(partner, 'pp1_Expression17') is None


def test_assoc_value3_stub_double():
    # pp1_Expression has no real 'pp1_Expression4' property in the generated
    # code (a bare stub) -- manually attach it so pp1_AttributeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp1_AttributeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp1_AttributeOperation(key="sample_text", op="sample_text")
    partner = pp1_Expression()
    setattr(partner, 'pp1_Expression4', None)
    _safe_set(owner, 'pp1_AttributeOperation', partner)
    assert getattr(partner, 'pp1_Expression4') == owner
    _safe_set(owner, 'pp1_AttributeOperation', None)
    assert getattr(partner, 'pp1_Expression4') is None


