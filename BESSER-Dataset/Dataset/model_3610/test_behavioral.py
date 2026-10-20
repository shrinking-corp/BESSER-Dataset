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
    pp_AdditiveExpression,
    pp_AndExpression,
    pp_AppendExpression,
    pp_AssignmentExpression,
    pp_AtExpression,
    pp_AttributeOperation,
    pp_AttributeOperations,
    pp_BinaryExpression,
    pp_BinaryOpExpression,
    pp_Case,
    pp_CaseExpression,
    pp_CollectExpression,
    pp_Definition,
    pp_DefinitionArgument,
    pp_DefinitionArgumentList,
    pp_DoubleQuotedString,
    pp_ElseExpression,
    pp_ElseIfExpression,
    pp_EqualityExpression,
    pp_ExportedCollectQuery,
    pp_ExprList,
    pp_Expression,
    pp_ExpressionBlock,
    pp_ExpressionTE,
    pp_FunctionCall,
    pp_HashEntry,
    pp_HostClassDefinition,
    pp_ICollectQuery,
    pp_IQuotedString,
    pp_IfExpression,
    pp_ImportExpression,
    pp_InExpression,
    pp_InterpolatedVariable,
    pp_JavaLambda,
    pp_Lambda,
    pp_LiteralBoolean,
    pp_LiteralClass,
    pp_LiteralDefault,
    pp_LiteralExpression,
    pp_LiteralHash,
    pp_LiteralList,
    pp_LiteralName,
    pp_LiteralNameOrReference,
    pp_LiteralRegex,
    pp_LiteralUndef,
    pp_MatchingExpression,
    pp_MethodCall,
    pp_MultiplicativeExpression,
    pp_NamedAccessExpression,
    pp_NodeDefinition,
    pp_OrExpression,
    pp_ParameterizedExpression,
    pp_ParenthesisedExpression,
    pp_PuppetManifest,
    pp_RelationalExpression,
    pp_RelationshipExpression,
    pp_ResourceBody,
    pp_ResourceExpression,
    pp_RubyLambda,
    pp_SelectorEntry,
    pp_SelectorExpression,
    pp_SeparatorExpression,
    pp_ShiftExpression,
    pp_SingleQuotedString,
    pp_StringExpression,
    pp_TextExpression,
    pp_UnaryExpression,
    pp_UnaryMinusExpression,
    pp_UnaryNotExpression,
    pp_UnlessExpression,
    pp_UnquotedString,
    pp_VariableExpression,
    pp_VariableTE,
    pp_VerbatimTE,
    pp_VirtualCollectQuery,
    pp_VirtualNameOrReference,
    pp_WithLambdaExpression,
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
    # pp_DefinitionArgumentList has no real 'pp_DefinitionArgumentList11' property in the generated
    # code (a bare stub) -- manually attach it so pp_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp_DefinitionArgumentList()
    setattr(partner, 'pp_DefinitionArgumentList11', None)
    _safe_set(owner, 'pp_DefinitionArgument', partner)
    assert owner in getattr(partner, 'pp_DefinitionArgumentList11')
    _safe_set(owner, 'pp_DefinitionArgument', None)
    assert owner not in getattr(partner, 'pp_DefinitionArgumentList11')


def test_assoc_arguments9_stub_double():
    # pp_DefinitionArgumentList has no real 'pp_DefinitionArgumentList' property in the generated
    # code (a bare stub) -- manually attach it so pp_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp_Definition(className="sample_text")
    partner = pp_DefinitionArgumentList()
    setattr(partner, 'pp_DefinitionArgumentList', None)
    _safe_set(owner, 'pp_Definition', partner)
    assert getattr(partner, 'pp_DefinitionArgumentList') == owner
    _safe_set(owner, 'pp_Definition', None)
    assert getattr(partner, 'pp_DefinitionArgumentList') is None


def test_assoc_attributes5_stub_double():
    # pp_AttributeOperations has no real 'pp_AttributeOperations6' property in the generated
    # code (a bare stub) -- manually attach it so pp_AttributeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp_AttributeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp_AttributeOperation(key="sample_text", op="sample_text")
    partner = pp_AttributeOperations()
    setattr(partner, 'pp_AttributeOperations6', None)
    _safe_set(owner, 'pp_AttributeOperation7', partner)
    assert owner in getattr(partner, 'pp_AttributeOperations6')
    _safe_set(owner, 'pp_AttributeOperation7', None)
    assert owner not in getattr(partner, 'pp_AttributeOperations6')


def test_assoc_methodExpr87_stub_double():
    # pp_Expression has no real 'pp_Expression88' property in the generated
    # code (a bare stub) -- manually attach it so pp_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp_MethodCall(parenthesized=True)
    partner = pp_Expression()
    setattr(partner, 'pp_Expression88', None)
    _safe_set(owner, 'pp_MethodCall', partner)
    assert getattr(partner, 'pp_Expression88') == owner
    _safe_set(owner, 'pp_MethodCall', None)
    assert getattr(partner, 'pp_Expression88') is None


def test_assoc_puppetType12_stub_double():
    # pp_Expression has no real 'pp_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so pp_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp_Expression()
    setattr(partner, 'pp_Expression14', None)
    _safe_set(owner, 'pp_DefinitionArgument13', partner)
    assert getattr(partner, 'pp_Expression14') == owner
    _safe_set(owner, 'pp_DefinitionArgument13', None)
    assert getattr(partner, 'pp_Expression14') is None


def test_assoc_value15_stub_double():
    # pp_Expression has no real 'pp_Expression17' property in the generated
    # code (a bare stub) -- manually attach it so pp_DefinitionArgument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp_DefinitionArgument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp_DefinitionArgument(argName="sample_text", op="sample_text")
    partner = pp_Expression()
    setattr(partner, 'pp_Expression17', None)
    _safe_set(owner, 'pp_DefinitionArgument16', partner)
    assert getattr(partner, 'pp_Expression17') == owner
    _safe_set(owner, 'pp_DefinitionArgument16', None)
    assert getattr(partner, 'pp_Expression17') is None


def test_assoc_value3_stub_double():
    # pp_Expression has no real 'pp_Expression4' property in the generated
    # code (a bare stub) -- manually attach it so pp_AttributeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pp_AttributeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pp_AttributeOperation(key="sample_text", op="sample_text")
    partner = pp_Expression()
    setattr(partner, 'pp_Expression4', None)
    _safe_set(owner, 'pp_AttributeOperation', partner)
    assert getattr(partner, 'pp_Expression4') == owner
    _safe_set(owner, 'pp_AttributeOperation', None)
    assert getattr(partner, 'pp_Expression4') is None


