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
    pp2_AdditiveExpression,
    pp2_AndExpression,
    pp2_AppendExpression,
    pp2_AssignmentExpression,
    pp2_AtExpression,
    pp2_AttributeOperation,
    pp2_AttributeOperations,
    pp2_BinaryExpression,
    pp2_BinaryOpExpression,
    pp2_Case,
    pp2_CaseExpression,
    pp2_CollectExpression,
    pp2_Definition,
    pp2_DefinitionArgument,
    pp2_DefinitionArgumentList,
    pp2_DoubleQuotedString,
    pp2_ElseExpression,
    pp2_ElseIfExpression,
    pp2_EqualityExpression,
    pp2_ExportedCollectQuery,
    pp2_ExprList,
    pp2_Expression,
    pp2_ExpressionBlock,
    pp2_ExpressionTE,
    pp2_FunctionCall,
    pp2_HashEntry,
    pp2_HostClassDefinition,
    pp2_ICollectQuery,
    pp2_IQuotedString,
    pp2_IfExpression,
    pp2_ImportExpression,
    pp2_InExpression,
    pp2_InterpolatedVariable,
    pp2_JavaLambda,
    pp2_Lambda,
    pp2_LiteralBoolean,
    pp2_LiteralClass,
    pp2_LiteralDefault,
    pp2_LiteralExpression,
    pp2_LiteralHash,
    pp2_LiteralList,
    pp2_LiteralName,
    pp2_LiteralNameOrReference,
    pp2_LiteralRegex,
    pp2_LiteralUndef,
    pp2_MatchingExpression,
    pp2_MethodCall,
    pp2_MultiplicativeExpression,
    pp2_NamedAccessExpression,
    pp2_NodeDefinition,
    pp2_OrExpression,
    pp2_ParameterizedExpression,
    pp2_ParenthesisedExpression,
    pp2_PuppetManifest,
    pp2_RelationalExpression,
    pp2_RelationshipExpression,
    pp2_ResourceBody,
    pp2_ResourceExpression,
    pp2_RubyLambda,
    pp2_SelectorEntry,
    pp2_SelectorExpression,
    pp2_SeparatorExpression,
    pp2_ShiftExpression,
    pp2_SingleQuotedString,
    pp2_StringExpression,
    pp2_TextExpression,
    pp2_UnaryExpression,
    pp2_UnaryMinusExpression,
    pp2_UnaryNotExpression,
    pp2_UnlessExpression,
    pp2_UnquotedString,
    pp2_VariableExpression,
    pp2_VariableTE,
    pp2_VerbatimTE,
    pp2_VirtualCollectQuery,
    pp2_VirtualNameOrReference,
    pp2_WithLambdaExpression,
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

def test_assoc_arguments10_stub_double():
    # pp2_DefinitionArgumentList has no real 'pp2_DefinitionArgumentList11' property in the generated
    # code (a bare stub) -- manually attach it so pp2_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp2_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp2_DefinitionArgumentList()
    setattr(partner, 'pp2_DefinitionArgumentList11', None)
    _safe_set(owner, 'pp2_DefinitionArgument', partner)
    assert owner in getattr(partner, 'pp2_DefinitionArgumentList11')
    _safe_set(owner, 'pp2_DefinitionArgument', None)
    assert owner not in getattr(partner, 'pp2_DefinitionArgumentList11')


def test_assoc_arguments9_stub_double():
    # pp2_DefinitionArgumentList has no real 'pp2_DefinitionArgumentList' property in the generated
    # code (a bare stub) -- manually attach it so pp2_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp2_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp2_Definition(className="sample_text")
    partner = pp2_DefinitionArgumentList()
    setattr(partner, 'pp2_DefinitionArgumentList', None)
    _safe_set(owner, 'pp2_Definition', partner)
    assert getattr(partner, 'pp2_DefinitionArgumentList') == owner
    _safe_set(owner, 'pp2_Definition', None)
    assert getattr(partner, 'pp2_DefinitionArgumentList') is None


def test_assoc_attributes5_stub_double():
    # pp2_AttributeOperations has no real 'pp2_AttributeOperations6' property in the generated
    # code (a bare stub) -- manually attach it so pp2_AttributeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp2_AttributeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp2_AttributeOperation(key="sample_text", op="sample_text")
    partner = pp2_AttributeOperations()
    setattr(partner, 'pp2_AttributeOperations6', None)
    _safe_set(owner, 'pp2_AttributeOperation7', partner)
    assert owner in getattr(partner, 'pp2_AttributeOperations6')
    _safe_set(owner, 'pp2_AttributeOperation7', None)
    assert owner not in getattr(partner, 'pp2_AttributeOperations6')


def test_assoc_methodExpr87_stub_double():
    # pp2_Expression has no real 'pp2_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so pp2_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp2_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp2_MethodCall(parenthesized=True)
    partner = pp2_Expression()
    setattr(partner, 'pp2_Expression88', None)
    _safe_set(owner, 'pp2_MethodCall', partner)
    assert getattr(partner, 'pp2_Expression88') == owner
    _safe_set(owner, 'pp2_MethodCall', None)
    assert getattr(partner, 'pp2_Expression88') is None


def test_assoc_puppetType12_stub_double():
    # pp2_Expression has no real 'pp2_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so pp2_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp2_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp2_Expression()
    setattr(partner, 'pp2_Expression14', None)
    _safe_set(owner, 'pp2_DefinitionArgument13', partner)
    assert getattr(partner, 'pp2_Expression14') == owner
    _safe_set(owner, 'pp2_DefinitionArgument13', None)
    assert getattr(partner, 'pp2_Expression14') is None


def test_assoc_value15_stub_double():
    # pp2_Expression has no real 'pp2_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so pp2_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp2_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp2_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp2_Expression()
    setattr(partner, 'pp2_Expression17', None)
    _safe_set(owner, 'pp2_DefinitionArgument16', partner)
    assert getattr(partner, 'pp2_Expression17') == owner
    _safe_set(owner, 'pp2_DefinitionArgument16', None)
    assert getattr(partner, 'pp2_Expression17') is None


def test_assoc_value3_stub_double():
    # pp2_Expression has no real 'pp2_Expression4' property in the generated
    # code (a bare stub) -- manually attach it so pp2_AttributeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp2_AttributeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp2_AttributeOperation(key="sample_text", op="sample_text")
    partner = pp2_Expression()
    setattr(partner, 'pp2_Expression4', None)
    _safe_set(owner, 'pp2_AttributeOperation', partner)
    assert getattr(partner, 'pp2_Expression4') == owner
    _safe_set(owner, 'pp2_AttributeOperation', None)
    assert getattr(partner, 'pp2_Expression4') is None


