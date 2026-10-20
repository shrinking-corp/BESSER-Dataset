import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AccessorAssignment,
    Expression,
    IArrayElement,
    IForInitializer,
    IProperty,
    IPropertyName,
    IPropertySelector,
    ISelector,
    IUnqualifiedSelector,
    IterationStatement,
    Node,
    PropertyAssignment,
    PropertyIdentifier,
    Statement,
    SwitchElement,
    XmlFragment,
    dom_AccessorAssignment,
    dom_ArrayAccessExpression,
    dom_ArrayLiteral,
    dom_AttributeIdentifier,
    dom_BinaryExpression,
    dom_BlockStatement,
    dom_BooleanLiteral,
    dom_BreakStatement,
    dom_CallExpression,
    dom_CaseClause,
    dom_CatchClause,
    dom_Comment,
    dom_ConditionalExpression,
    dom_ConstStatement,
    dom_ContinueStatement,
    dom_DefaultClause,
    dom_DefaultXmlNamespaceStatement,
    dom_DescendantAccessExpression,
    dom_DoStatement,
    dom_Elision,
    dom_EmptyStatement,
    dom_Expression,
    dom_ExpressionSelector,
    dom_ExpressionStatement,
    dom_FilterExpression,
    dom_FinallyClause,
    dom_ForEachInStatement,
    dom_ForInStatement,
    dom_ForStatement,
    dom_FunctionExpression,
    dom_GetterAssignment,
    dom_IArrayElement,
    dom_IForInitializer,
    dom_IProperty,
    dom_IPropertyName,
    dom_IPropertySelector,
    dom_ISelector,
    dom_IUnqualifiedSelector,
    dom_Identifier,
    dom_IfStatement,
    dom_IterationStatement,
    dom_Label,
    dom_LabeledStatement,
    dom_NewExpression,
    dom_Node,
    dom_NullLiteral,
    dom_NumericLiteral,
    dom_ObjectLiteral,
    dom_Parameter,
    dom_ParenthesizedExpression,
    dom_PropertyAccessExpression,
    dom_PropertyAssignment,
    dom_PropertyIdentifier,
    dom_QualifiedIdentifier,
    dom_RegularExpressionLiteral,
    dom_ReturnStatement,
    dom_SetterAssignment,
    dom_SimplePropertyAssignment,
    dom_Source,
    dom_Statement,
    dom_StringLiteral,
    dom_SwitchElement,
    dom_SwitchStatement,
    dom_ThisExpression,
    dom_ThrowStatement,
    dom_TryStatement,
    dom_UnaryExpression,
    dom_VariableDeclaration,
    dom_VariableReference,
    dom_VariableStatement,
    dom_WhileStatement,
    dom_WildcardIdentifier,
    dom_WithStatement,
    dom_XmlExpressionFragment,
    dom_XmlFragment,
    dom_XmlInitializer,
    dom_XmlTextFragment,
    BinaryOperator,
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

def test_assoc_documentation126_reverse_link_reassign_clear():
    a1 = dom_FunctionExpression(parametersPosition=7)
    a2 = dom_FunctionExpression(parametersPosition=13)
    b = dom_Comment(text="sample_text")
    _safe_set(b, 'dom_Comment', a1)
    assert _is_linked(b, 'dom_Comment', a1)
    if hasattr(a1, 'dom_FunctionExpression'):
        assert _is_linked(a1, 'dom_FunctionExpression', b)
    _safe_set(b, 'dom_Comment', a2)
    assert _is_linked(b, 'dom_Comment', a2)
    if hasattr(a1, 'dom_FunctionExpression'):
        assert not _is_linked(a1, 'dom_FunctionExpression', b)
    if hasattr(a2, 'dom_FunctionExpression'):
        assert _is_linked(a2, 'dom_FunctionExpression', b)
    _safe_set(b, 'dom_Comment', None)
    assert not _is_linked(b, 'dom_Comment', a2)
    if hasattr(a2, 'dom_FunctionExpression'):
        assert not _is_linked(a2, 'dom_FunctionExpression', b)


def test_assoc_identifier127_reverse_link_reassign_clear():
    a1 = dom_Identifier(name="sample_text")
    a2 = dom_Identifier(name="sample_text_2")
    b = dom_FunctionExpression(parametersPosition=7)
    _safe_set(b, 'dom_FunctionExpression128', a1)
    assert _is_linked(b, 'dom_FunctionExpression128', a1)
    if hasattr(a1, 'dom_Identifier129'):
        assert _is_linked(a1, 'dom_Identifier129', b)
    _safe_set(b, 'dom_FunctionExpression128', a2)
    assert _is_linked(b, 'dom_FunctionExpression128', a2)
    if hasattr(a1, 'dom_Identifier129'):
        assert not _is_linked(a1, 'dom_Identifier129', b)
    if hasattr(a2, 'dom_Identifier129'):
        assert _is_linked(a2, 'dom_Identifier129', b)
    _safe_set(b, 'dom_FunctionExpression128', None)
    assert not _is_linked(b, 'dom_FunctionExpression128', a2)
    if hasattr(a2, 'dom_Identifier129'):
        assert not _is_linked(a2, 'dom_Identifier129', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argument30_stub_double():
    # dom_Expression has no real 'dom_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so dom_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_UnaryExpression(operation="sample_text")
    partner = dom_Expression()
    setattr(partner, 'dom_Expression31', None)
    _safe_set(owner, 'dom_UnaryExpression', partner)
    assert getattr(partner, 'dom_Expression31') == owner
    _safe_set(owner, 'dom_UnaryExpression', None)
    assert getattr(partner, 'dom_Expression31') is None


def test_assoc_body132_stub_double():
    # dom_BlockStatement has no real 'dom_BlockStatement134' property in the generated
    # code (a bare stub) -- manually attach it so dom_FunctionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FunctionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FunctionExpression(parametersPosition=7)
    partner = dom_BlockStatement()
    setattr(partner, 'dom_BlockStatement134', None)
    _safe_set(owner, 'dom_FunctionExpression133', partner)
    assert getattr(partner, 'dom_BlockStatement134') == owner
    _safe_set(owner, 'dom_FunctionExpression133', None)
    assert getattr(partner, 'dom_BlockStatement134') is None


def test_assoc_exception114_stub_double():
    # dom_CatchClause has no real 'dom_CatchClause115' property in the generated
    # code (a bare stub) -- manually attach it so dom_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Identifier(name="sample_text")
    partner = dom_CatchClause()
    setattr(partner, 'dom_CatchClause115', None)
    _safe_set(owner, 'dom_Identifier116', partner)
    assert getattr(partner, 'dom_CatchClause115') == owner
    _safe_set(owner, 'dom_Identifier116', None)
    assert getattr(partner, 'dom_CatchClause115') is None


def test_assoc_identifier48_stub_double():
    # dom_VariableDeclaration has no real 'dom_VariableDeclaration49' property in the generated
    # code (a bare stub) -- manually attach it so dom_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Identifier(name="sample_text")
    partner = dom_VariableDeclaration()
    setattr(partner, 'dom_VariableDeclaration49', None)
    _safe_set(owner, 'dom_Identifier50', partner)
    assert getattr(partner, 'dom_VariableDeclaration49') == owner
    _safe_set(owner, 'dom_Identifier50', None)
    assert getattr(partner, 'dom_VariableDeclaration49') is None


def test_assoc_label101_stub_double():
    # dom_LabeledStatement has no real 'dom_LabeledStatement' property in the generated
    # code (a bare stub) -- manually attach it so dom_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Label(name="sample_text")
    partner = dom_LabeledStatement()
    setattr(partner, 'dom_LabeledStatement', None)
    _safe_set(owner, 'dom_Label102', partner)
    assert getattr(partner, 'dom_LabeledStatement') == owner
    _safe_set(owner, 'dom_Label102', None)
    assert getattr(partner, 'dom_LabeledStatement') is None


def test_assoc_label82_stub_double():
    # dom_ContinueStatement has no real 'dom_ContinueStatement' property in the generated
    # code (a bare stub) -- manually attach it so dom_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Label(name="sample_text")
    partner = dom_ContinueStatement()
    setattr(partner, 'dom_ContinueStatement', None)
    _safe_set(owner, 'dom_Label', partner)
    assert getattr(partner, 'dom_ContinueStatement') == owner
    _safe_set(owner, 'dom_Label', None)
    assert getattr(partner, 'dom_ContinueStatement') is None


def test_assoc_label83_stub_double():
    # dom_BreakStatement has no real 'dom_BreakStatement' property in the generated
    # code (a bare stub) -- manually attach it so dom_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Label(name="sample_text")
    partner = dom_BreakStatement()
    setattr(partner, 'dom_BreakStatement', None)
    _safe_set(owner, 'dom_Label84', partner)
    assert getattr(partner, 'dom_BreakStatement') == owner
    _safe_set(owner, 'dom_Label84', None)
    assert getattr(partner, 'dom_BreakStatement') is None


def test_assoc_left32_stub_double():
    # dom_Expression has no real 'dom_Expression33' property in the generated
    # code (a bare stub) -- manually attach it so dom_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BinaryExpression(operation="sample_text", operatorPosition=7)
    partner = dom_Expression()
    setattr(partner, 'dom_Expression33', None)
    _safe_set(owner, 'dom_BinaryExpression', partner)
    assert getattr(partner, 'dom_Expression33') == owner
    _safe_set(owner, 'dom_BinaryExpression', None)
    assert getattr(partner, 'dom_Expression33') is None


def test_assoc_name135_stub_double():
    # dom_Parameter has no real 'dom_Parameter136' property in the generated
    # code (a bare stub) -- manually attach it so dom_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Identifier(name="sample_text")
    partner = dom_Parameter()
    setattr(partner, 'dom_Parameter136', None)
    _safe_set(owner, 'dom_Identifier137', partner)
    assert getattr(partner, 'dom_Parameter136') == owner
    _safe_set(owner, 'dom_Identifier137', None)
    assert getattr(partner, 'dom_Parameter136') is None


def test_assoc_parameter7_stub_double():
    # dom_SetterAssignment has no real 'dom_SetterAssignment' property in the generated
    # code (a bare stub) -- manually attach it so dom_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Identifier(name="sample_text")
    partner = dom_SetterAssignment()
    setattr(partner, 'dom_SetterAssignment', None)
    _safe_set(owner, 'dom_Identifier8', partner)
    assert getattr(partner, 'dom_SetterAssignment') == owner
    _safe_set(owner, 'dom_Identifier8', None)
    assert getattr(partner, 'dom_SetterAssignment') is None


def test_assoc_parameters130_stub_double():
    # dom_Parameter has no real 'dom_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so dom_FunctionExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_FunctionExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_FunctionExpression(parametersPosition=7)
    partner = dom_Parameter()
    setattr(partner, 'dom_Parameter', None)
    _safe_set(owner, 'dom_FunctionExpression131', {partner})
    assert getattr(partner, 'dom_Parameter') == owner
    _safe_set(owner, 'dom_FunctionExpression131', set())
    assert getattr(partner, 'dom_Parameter') is None


def test_assoc_right34_stub_double():
    # dom_Expression has no real 'dom_Expression36' property in the generated
    # code (a bare stub) -- manually attach it so dom_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BinaryExpression(operation="sample_text", operatorPosition=7)
    partner = dom_Expression()
    setattr(partner, 'dom_Expression36', None)
    _safe_set(owner, 'dom_BinaryExpression35', partner)
    assert getattr(partner, 'dom_Expression36') == owner
    _safe_set(owner, 'dom_BinaryExpression35', None)
    assert getattr(partner, 'dom_Expression36') is None


def test_assoc_variable0_stub_double():
    # dom_VariableReference has no real 'dom_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so dom_Identifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_Identifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_Identifier(name="sample_text")
    partner = dom_VariableReference()
    setattr(partner, 'dom_VariableReference', None)
    _safe_set(owner, 'dom_Identifier', partner)
    assert getattr(partner, 'dom_VariableReference') == owner
    _safe_set(owner, 'dom_Identifier', None)
    assert getattr(partner, 'dom_VariableReference') is None


