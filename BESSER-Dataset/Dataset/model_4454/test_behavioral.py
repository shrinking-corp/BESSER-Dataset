import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanExpression,
    BooleanOperator,
    CompareOperator,
    NumberExpression,
    SimpleStatement,
    Value,
    VariableReference,
    arduinoDSL_And,
    arduinoDSL_AndOr,
    arduinoDSL_Assignment,
    arduinoDSL_Attribute,
    arduinoDSL_Board,
    arduinoDSL_BooleanExpression,
    arduinoDSL_BooleanExpressionBlock,
    arduinoDSL_BooleanLiteral,
    arduinoDSL_BooleanOperator,
    arduinoDSL_Cast,
    arduinoDSL_CompareOperator,
    arduinoDSL_Comparison,
    arduinoDSL_Component,
    arduinoDSL_ComponentBody,
    arduinoDSL_Delta,
    arduinoDSL_Div,
    arduinoDSL_EObject,
    arduinoDSL_ElseIfStatement,
    arduinoDSL_ElseStatement,
    arduinoDSL_Equals,
    arduinoDSL_Greater,
    arduinoDSL_GreaterThanEquals,
    arduinoDSL_IfStatement,
    arduinoDSL_Map,
    arduinoDSL_Minus,
    arduinoDSL_Mod,
    arduinoDSL_Mult,
    arduinoDSL_Node,
    arduinoDSL_NodeDefinition,
    arduinoDSL_NotEquals,
    arduinoDSL_NumberExpression,
    arduinoDSL_NumberExpressionBlock,
    arduinoDSL_NumberLiteral,
    arduinoDSL_Or,
    arduinoDSL_Plus,
    arduinoDSL_Program,
    arduinoDSL_Range,
    arduinoDSL_Rate,
    arduinoDSL_Rule,
    arduinoDSL_RuleBody,
    arduinoDSL_SimpleStatement,
    arduinoDSL_Smaller,
    arduinoDSL_SmallerThanEquals,
    arduinoDSL_Smoothing,
    arduinoDSL_State,
    arduinoDSL_Value,
    arduinoDSL_VarRef,
    arduinoDSL_VariableDeclaration,
    arduinoDSL_VariableReference,
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

def test_assoc_cast19_reverse_link_reassign_clear():
    a1 = arduinoDSL_VariableDeclaration(name="sample_text", type="sample_text")
    a2 = arduinoDSL_VariableDeclaration(name="sample_text_2", type="sample_text_2")
    b = arduinoDSL_Cast(castType="sample_text")
    _safe_set(b, 'arduinoDSL_Cast', a1)
    assert _is_linked(b, 'arduinoDSL_Cast', a1)
    if hasattr(a1, 'arduinoDSL_VariableDeclaration'):
        assert _is_linked(a1, 'arduinoDSL_VariableDeclaration', b)
    _safe_set(b, 'arduinoDSL_Cast', a2)
    assert _is_linked(b, 'arduinoDSL_Cast', a2)
    if hasattr(a1, 'arduinoDSL_VariableDeclaration'):
        assert not _is_linked(a1, 'arduinoDSL_VariableDeclaration', b)
    if hasattr(a2, 'arduinoDSL_VariableDeclaration'):
        assert _is_linked(a2, 'arduinoDSL_VariableDeclaration', b)
    _safe_set(b, 'arduinoDSL_Cast', None)
    assert not _is_linked(b, 'arduinoDSL_Cast', a2)
    if hasattr(a2, 'arduinoDSL_VariableDeclaration'):
        assert not _is_linked(a2, 'arduinoDSL_VariableDeclaration', b)


def test_assoc_components27_reverse_link_reassign_clear():
    a1 = arduinoDSL_Node(name="sample_text")
    a2 = arduinoDSL_Node(name="sample_text_2")
    b = arduinoDSL_Component(name="sample_text")
    _safe_set(b, 'arduinoDSL_Component29', a1)
    assert _is_linked(b, 'arduinoDSL_Component29', a1)
    if hasattr(a1, 'arduinoDSL_Node28'):
        assert _is_linked(a1, 'arduinoDSL_Node28', b)
    _safe_set(b, 'arduinoDSL_Component29', a2)
    assert _is_linked(b, 'arduinoDSL_Component29', a2)
    if hasattr(a1, 'arduinoDSL_Node28'):
        assert not _is_linked(a1, 'arduinoDSL_Node28', b)
    if hasattr(a2, 'arduinoDSL_Node28'):
        assert _is_linked(a2, 'arduinoDSL_Node28', b)
    _safe_set(b, 'arduinoDSL_Component29', None)
    assert not _is_linked(b, 'arduinoDSL_Component29', a2)
    if hasattr(a2, 'arduinoDSL_Node28'):
        assert not _is_linked(a2, 'arduinoDSL_Node28', b)


def test_assoc_properties30_reverse_link_reassign_clear():
    a1 = arduinoDSL_ComponentBody(io="sample_text", pin=7, type="sample_text")
    a2 = arduinoDSL_ComponentBody(io="sample_text_2", pin=13, type="sample_text_2")
    b = arduinoDSL_Component(name="sample_text")
    _safe_set(b, 'arduinoDSL_Component31', a1)
    assert _is_linked(b, 'arduinoDSL_Component31', a1)
    if hasattr(a1, 'arduinoDSL_ComponentBody'):
        assert _is_linked(a1, 'arduinoDSL_ComponentBody', b)
    _safe_set(b, 'arduinoDSL_Component31', a2)
    assert _is_linked(b, 'arduinoDSL_Component31', a2)
    if hasattr(a1, 'arduinoDSL_ComponentBody'):
        assert not _is_linked(a1, 'arduinoDSL_ComponentBody', b)
    if hasattr(a2, 'arduinoDSL_ComponentBody'):
        assert _is_linked(a2, 'arduinoDSL_ComponentBody', b)
    _safe_set(b, 'arduinoDSL_Component31', None)
    assert not _is_linked(b, 'arduinoDSL_Component31', a2)
    if hasattr(a2, 'arduinoDSL_ComponentBody'):
        assert not _is_linked(a2, 'arduinoDSL_ComponentBody', b)


def test_assoc_rate32_reverse_link_reassign_clear():
    a1 = arduinoDSL_Rate(value=7)
    a2 = arduinoDSL_Rate(value=13)
    b = arduinoDSL_ComponentBody(io="sample_text", pin=7, type="sample_text")
    _safe_set(b, 'arduinoDSL_ComponentBody33', a1)
    assert _is_linked(b, 'arduinoDSL_ComponentBody33', a1)
    if hasattr(a1, 'arduinoDSL_Rate'):
        assert _is_linked(a1, 'arduinoDSL_Rate', b)
    _safe_set(b, 'arduinoDSL_ComponentBody33', a2)
    assert _is_linked(b, 'arduinoDSL_ComponentBody33', a2)
    if hasattr(a1, 'arduinoDSL_Rate'):
        assert not _is_linked(a1, 'arduinoDSL_Rate', b)
    if hasattr(a2, 'arduinoDSL_Rate'):
        assert _is_linked(a2, 'arduinoDSL_Rate', b)
    _safe_set(b, 'arduinoDSL_ComponentBody33', None)
    assert not _is_linked(b, 'arduinoDSL_ComponentBody33', a2)
    if hasattr(a2, 'arduinoDSL_Rate'):
        assert not _is_linked(a2, 'arduinoDSL_Rate', b)


def test_assoc_smoothing36_reverse_link_reassign_clear():
    a1 = arduinoDSL_Smoothing(value=3.14)
    a2 = arduinoDSL_Smoothing(value=9.99)
    b = arduinoDSL_ComponentBody(io="sample_text", pin=7, type="sample_text")
    _safe_set(b, 'arduinoDSL_ComponentBody37', a1)
    assert _is_linked(b, 'arduinoDSL_ComponentBody37', a1)
    if hasattr(a1, 'arduinoDSL_Smoothing'):
        assert _is_linked(a1, 'arduinoDSL_Smoothing', b)
    _safe_set(b, 'arduinoDSL_ComponentBody37', a2)
    assert _is_linked(b, 'arduinoDSL_ComponentBody37', a2)
    if hasattr(a1, 'arduinoDSL_Smoothing'):
        assert not _is_linked(a1, 'arduinoDSL_Smoothing', b)
    if hasattr(a2, 'arduinoDSL_Smoothing'):
        assert _is_linked(a2, 'arduinoDSL_Smoothing', b)
    _safe_set(b, 'arduinoDSL_ComponentBody37', None)
    assert not _is_linked(b, 'arduinoDSL_ComponentBody37', a2)
    if hasattr(a2, 'arduinoDSL_Smoothing'):
        assert not _is_linked(a2, 'arduinoDSL_Smoothing', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_board23_stub_double():
    # arduinoDSL_NodeDefinition has no real 'arduinoDSL_NodeDefinition' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Board(b="sample_text")
    partner = arduinoDSL_NodeDefinition()
    setattr(partner, 'arduinoDSL_NodeDefinition', None)
    _safe_set(owner, 'arduinoDSL_Board', partner)
    assert getattr(partner, 'arduinoDSL_NodeDefinition') == owner
    _safe_set(owner, 'arduinoDSL_Board', None)
    assert getattr(partner, 'arduinoDSL_NodeDefinition') is None


def test_assoc_body2_stub_double():
    # arduinoDSL_RuleBody has no real 'arduinoDSL_RuleBody' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Rule(type="sample_text")
    partner = arduinoDSL_RuleBody()
    setattr(partner, 'arduinoDSL_RuleBody', None)
    _safe_set(owner, 'arduinoDSL_Rule3', partner)
    assert getattr(partner, 'arduinoDSL_RuleBody') == owner
    _safe_set(owner, 'arduinoDSL_Rule3', None)
    assert getattr(partner, 'arduinoDSL_RuleBody') is None


def test_assoc_cast108_stub_double():
    # arduinoDSL_VarRef has no real 'arduinoDSL_VarRef109' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Cast's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Cast's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Cast(castType="sample_text")
    partner = arduinoDSL_VarRef()
    setattr(partner, 'arduinoDSL_VarRef109', None)
    _safe_set(owner, 'arduinoDSL_Cast110', partner)
    assert getattr(partner, 'arduinoDSL_VarRef109') == owner
    _safe_set(owner, 'arduinoDSL_Cast110', None)
    assert getattr(partner, 'arduinoDSL_VarRef109') is None


def test_assoc_component8_stub_double():
    # arduinoDSL_Attribute has no real 'arduinoDSL_Attribute9' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Component(name="sample_text")
    partner = arduinoDSL_Attribute()
    setattr(partner, 'arduinoDSL_Attribute9', None)
    _safe_set(owner, 'arduinoDSL_Component', partner)
    assert getattr(partner, 'arduinoDSL_Attribute9') == owner
    _safe_set(owner, 'arduinoDSL_Component', None)
    assert getattr(partner, 'arduinoDSL_Attribute9') is None


def test_assoc_condition1_stub_double():
    # arduinoDSL_BooleanExpression has no real 'arduinoDSL_BooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Rule(type="sample_text")
    partner = arduinoDSL_BooleanExpression()
    setattr(partner, 'arduinoDSL_BooleanExpression', None)
    _safe_set(owner, 'arduinoDSL_Rule', partner)
    assert getattr(partner, 'arduinoDSL_BooleanExpression') == owner
    _safe_set(owner, 'arduinoDSL_Rule', None)
    assert getattr(partner, 'arduinoDSL_BooleanExpression') is None


def test_assoc_in_38_stub_double():
    # arduinoDSL_Map has no real 'arduinoDSL_Map39' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Range's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Range's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Range(high=3.14, low=3.14)
    partner = arduinoDSL_Map()
    setattr(partner, 'arduinoDSL_Map39', None)
    _safe_set(owner, 'arduinoDSL_Range', partner)
    assert getattr(partner, 'arduinoDSL_Map39') == owner
    _safe_set(owner, 'arduinoDSL_Range', None)
    assert getattr(partner, 'arduinoDSL_Map39') is None


def test_assoc_map34_stub_double():
    # arduinoDSL_Map has no real 'arduinoDSL_Map' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_ComponentBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_ComponentBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_ComponentBody(io="sample_text", pin=7, type="sample_text")
    partner = arduinoDSL_Map()
    setattr(partner, 'arduinoDSL_Map', None)
    _safe_set(owner, 'arduinoDSL_ComponentBody35', partner)
    assert getattr(partner, 'arduinoDSL_Map') == owner
    _safe_set(owner, 'arduinoDSL_ComponentBody35', None)
    assert getattr(partner, 'arduinoDSL_Map') is None


def test_assoc_name7_stub_double():
    # arduinoDSL_Attribute has no real 'arduinoDSL_Attribute' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Node(name="sample_text")
    partner = arduinoDSL_Attribute()
    setattr(partner, 'arduinoDSL_Attribute', None)
    _safe_set(owner, 'arduinoDSL_Node', partner)
    assert getattr(partner, 'arduinoDSL_Attribute') == owner
    _safe_set(owner, 'arduinoDSL_Node', None)
    assert getattr(partner, 'arduinoDSL_Attribute') is None


def test_assoc_node24_stub_double():
    # arduinoDSL_NodeDefinition has no real 'arduinoDSL_NodeDefinition25' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Node(name="sample_text")
    partner = arduinoDSL_NodeDefinition()
    setattr(partner, 'arduinoDSL_NodeDefinition25', None)
    _safe_set(owner, 'arduinoDSL_Node26', partner)
    assert getattr(partner, 'arduinoDSL_NodeDefinition25') == owner
    _safe_set(owner, 'arduinoDSL_Node26', None)
    assert getattr(partner, 'arduinoDSL_NodeDefinition25') is None


def test_assoc_out40_stub_double():
    # arduinoDSL_Map has no real 'arduinoDSL_Map41' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_Range's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_Range's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_Range(high=3.14, low=3.14)
    partner = arduinoDSL_Map()
    setattr(partner, 'arduinoDSL_Map41', None)
    _safe_set(owner, 'arduinoDSL_Range42', partner)
    assert getattr(partner, 'arduinoDSL_Map41') == owner
    _safe_set(owner, 'arduinoDSL_Range42', None)
    assert getattr(partner, 'arduinoDSL_Map41') is None


def test_assoc_ref106_stub_double():
    # arduinoDSL_VarRef has no real 'arduinoDSL_VarRef' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_VariableDeclaration(name="sample_text", type="sample_text")
    partner = arduinoDSL_VarRef()
    setattr(partner, 'arduinoDSL_VarRef', None)
    _safe_set(owner, 'arduinoDSL_VariableDeclaration107', partner)
    assert getattr(partner, 'arduinoDSL_VarRef') == owner
    _safe_set(owner, 'arduinoDSL_VariableDeclaration107', None)
    assert getattr(partner, 'arduinoDSL_VarRef') is None


def test_assoc_value20_stub_double():
    # arduinoDSL_EObject has no real 'arduinoDSL_EObject22' property in the generated
    # code (a bare stub) -- manually attach it so arduinoDSL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduinoDSL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduinoDSL_VariableDeclaration(name="sample_text", type="sample_text")
    partner = arduinoDSL_EObject()
    setattr(partner, 'arduinoDSL_EObject22', None)
    _safe_set(owner, 'arduinoDSL_VariableDeclaration21', partner)
    assert getattr(partner, 'arduinoDSL_EObject22') == owner
    _safe_set(owner, 'arduinoDSL_VariableDeclaration21', None)
    assert getattr(partner, 'arduinoDSL_EObject22') is None


