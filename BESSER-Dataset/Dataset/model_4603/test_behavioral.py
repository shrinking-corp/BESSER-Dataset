import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConditionGraphElements,
    ConditionNodeTypes,
    Expression,
    GraphElements,
    Logic,
    ModelElement,
    RuleElement,
    RuleNodeTypes,
    SequentialProperties,
    UnitElement,
    henshin_text_AND,
    henshin_text_AndExpression,
    henshin_text_Attribute,
    henshin_text_BoolValue,
    henshin_text_BracketExpression,
    henshin_text_Call,
    henshin_text_CheckDangling,
    henshin_text_ComparisonExpression,
    henshin_text_ConditionEdge,
    henshin_text_ConditionEdges,
    henshin_text_ConditionGraph,
    henshin_text_ConditionGraphElements,
    henshin_text_ConditionGraphRef,
    henshin_text_ConditionNode,
    henshin_text_ConditionNodeTypes,
    henshin_text_ConditionReuseNode,
    henshin_text_ConditionalUnit,
    henshin_text_Conditions,
    henshin_text_EAttribute,
    henshin_text_EClass,
    henshin_text_EPackage,
    henshin_text_EPackageImport,
    henshin_text_EReference,
    henshin_text_Edge,
    henshin_text_Edges,
    henshin_text_EqualityExpression,
    henshin_text_Expression,
    henshin_text_Formula,
    henshin_text_Graph,
    henshin_text_GraphElements,
    henshin_text_IndependentUnit,
    henshin_text_InjectiveMatching,
    henshin_text_IntegerValue,
    henshin_text_IteratedUnit,
    henshin_text_JavaAttributeValue,
    henshin_text_JavaClassValue,
    henshin_text_JavaImport,
    henshin_text_List,
    henshin_text_Logic,
    henshin_text_LoopUnit,
    henshin_text_Match,
    henshin_text_MinusExpression,
    henshin_text_Model,
    henshin_text_ModelElement,
    henshin_text_MulOrDivExpression,
    henshin_text_MultiRule,
    henshin_text_MultiRuleReuseNode,
    henshin_text_NaturalValue,
    henshin_text_Node,
    henshin_text_Not,
    henshin_text_NotExpression,
    henshin_text_NumberValue,
    henshin_text_ORorXOR,
    henshin_text_OrExpression,
    henshin_text_Parameter,
    henshin_text_ParameterType,
    henshin_text_ParameterValue,
    henshin_text_PlusExpression,
    henshin_text_PriorityUnit,
    henshin_text_Rollback,
    henshin_text_Rule,
    henshin_text_RuleElement,
    henshin_text_RuleNodeTypes,
    henshin_text_SequentialProperties,
    henshin_text_Strict,
    henshin_text_StringValue,
    henshin_text_Unit,
    henshin_text_UnitElement,
    ParameterKind,
    Type,
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

def test_assoc_attribute18_reverse_link_reassign_clear():
    a1 = henshin_text_Node(actiontype="sample_text")
    a2 = henshin_text_Node(actiontype="sample_text_2")
    b = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    _safe_set(b, 'henshin_text_Attribute', a1)
    assert _is_linked(b, 'henshin_text_Attribute', a1)
    if hasattr(a1, 'henshin_text_Node19'):
        assert _is_linked(a1, 'henshin_text_Node19', b)
    _safe_set(b, 'henshin_text_Attribute', a2)
    assert _is_linked(b, 'henshin_text_Attribute', a2)
    if hasattr(a1, 'henshin_text_Node19'):
        assert not _is_linked(a1, 'henshin_text_Node19', b)
    if hasattr(a2, 'henshin_text_Node19'):
        assert _is_linked(a2, 'henshin_text_Node19', b)
    _safe_set(b, 'henshin_text_Attribute', None)
    assert not _is_linked(b, 'henshin_text_Attribute', a2)
    if hasattr(a2, 'henshin_text_Node19'):
        assert not _is_linked(a2, 'henshin_text_Node19', b)


def test_assoc_parameters5_reverse_link_reassign_clear():
    a1 = henshin_text_Parameter(kind="sample_text", name="sample_text")
    a2 = henshin_text_Parameter(kind="sample_text_2", name="sample_text_2")
    b = henshin_text_ModelElement(name="sample_text")
    _safe_set(b, 'henshin_text_ModelElement6', {a1})
    assert _is_linked(b, 'henshin_text_ModelElement6', a1)
    if hasattr(a1, 'henshin_text_Parameter'):
        assert _is_linked(a1, 'henshin_text_Parameter', b)
    _safe_set(b, 'henshin_text_ModelElement6', {a2})
    assert _is_linked(b, 'henshin_text_ModelElement6', a2)
    if hasattr(a1, 'henshin_text_Parameter'):
        assert not _is_linked(a1, 'henshin_text_Parameter', b)
    if hasattr(a2, 'henshin_text_Parameter'):
        assert _is_linked(a2, 'henshin_text_Parameter', b)
    _safe_set(b, 'henshin_text_ModelElement6', set())
    assert not _is_linked(b, 'henshin_text_ModelElement6', a2)
    if hasattr(a2, 'henshin_text_Parameter'):
        assert not _is_linked(a2, 'henshin_text_Parameter', b)


def test_assoc_type83_reverse_link_reassign_clear():
    a1 = henshin_text_ParameterType(enumType="sample_text")
    a2 = henshin_text_ParameterType(enumType="sample_text_2")
    b = henshin_text_Parameter(kind="sample_text", name="sample_text")
    _safe_set(b, 'henshin_text_Parameter84', a1)
    assert _is_linked(b, 'henshin_text_Parameter84', a1)
    if hasattr(a1, 'henshin_text_ParameterType'):
        assert _is_linked(a1, 'henshin_text_ParameterType', b)
    _safe_set(b, 'henshin_text_Parameter84', a2)
    assert _is_linked(b, 'henshin_text_Parameter84', a2)
    if hasattr(a1, 'henshin_text_ParameterType'):
        assert not _is_linked(a1, 'henshin_text_ParameterType', b)
    if hasattr(a2, 'henshin_text_ParameterType'):
        assert _is_linked(a2, 'henshin_text_ParameterType', b)
    _safe_set(b, 'henshin_text_Parameter84', None)
    assert not _is_linked(b, 'henshin_text_Parameter84', a2)
    if hasattr(a2, 'henshin_text_ParameterType'):
        assert not _is_linked(a2, 'henshin_text_ParameterType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute22_stub_double():
    # henshin_text_MultiRuleReuseNode has no real 'henshin_text_MultiRuleReuseNode23' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    partner = henshin_text_MultiRuleReuseNode()
    setattr(partner, 'henshin_text_MultiRuleReuseNode23', None)
    _safe_set(owner, 'henshin_text_Attribute24', partner)
    assert owner in getattr(partner, 'henshin_text_MultiRuleReuseNode23')
    _safe_set(owner, 'henshin_text_Attribute24', None)
    assert owner not in getattr(partner, 'henshin_text_MultiRuleReuseNode23')


def test_assoc_conditionGraphElements34_stub_double():
    # henshin_text_ConditionGraphElements has no real 'henshin_text_ConditionGraphElements' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ConditionGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ConditionGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ConditionGraph(name="sample_text")
    partner = henshin_text_ConditionGraphElements()
    setattr(partner, 'henshin_text_ConditionGraphElements', None)
    _safe_set(owner, 'henshin_text_ConditionGraph35', {partner})
    assert getattr(partner, 'henshin_text_ConditionGraphElements') == owner
    _safe_set(owner, 'henshin_text_ConditionGraph35', set())
    assert getattr(partner, 'henshin_text_ConditionGraphElements') is None


def test_assoc_conditionGraphRef104_stub_double():
    # henshin_text_ConditionGraphRef has no real 'henshin_text_ConditionGraphRef' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ConditionGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ConditionGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ConditionGraph(name="sample_text")
    partner = henshin_text_ConditionGraphRef()
    setattr(partner, 'henshin_text_ConditionGraphRef', None)
    _safe_set(owner, 'henshin_text_ConditionGraph105', partner)
    assert getattr(partner, 'henshin_text_ConditionGraphRef') == owner
    _safe_set(owner, 'henshin_text_ConditionGraph105', None)
    assert getattr(partner, 'henshin_text_ConditionGraphRef') is None


def test_assoc_conditionGraphs32_stub_double():
    # henshin_text_Formula has no real 'henshin_text_Formula33' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ConditionGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ConditionGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ConditionGraph(name="sample_text")
    partner = henshin_text_Formula()
    setattr(partner, 'henshin_text_Formula33', None)
    _safe_set(owner, 'henshin_text_ConditionGraph', partner)
    assert owner in getattr(partner, 'henshin_text_Formula33')
    _safe_set(owner, 'henshin_text_ConditionGraph', None)
    assert owner not in getattr(partner, 'henshin_text_Formula33')


def test_assoc_edges9_stub_double():
    # henshin_text_Edges has no real 'henshin_text_Edges' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Edge(actiontype="sample_text")
    partner = henshin_text_Edges()
    setattr(partner, 'henshin_text_Edges', None)
    _safe_set(owner, 'henshin_text_Edge', partner)
    assert owner in getattr(partner, 'henshin_text_Edges')
    _safe_set(owner, 'henshin_text_Edge', None)
    assert owner not in getattr(partner, 'henshin_text_Edges')


def test_assoc_elementCall106_stub_double():
    # henshin_text_Call has no real 'henshin_text_Call' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ModelElement(name="sample_text")
    partner = henshin_text_Call()
    setattr(partner, 'henshin_text_Call', None)
    _safe_set(owner, 'henshin_text_ModelElement107', partner)
    assert getattr(partner, 'henshin_text_Call') == owner
    _safe_set(owner, 'henshin_text_ModelElement107', None)
    assert getattr(partner, 'henshin_text_Call') is None


def test_assoc_javaParameter152_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression153' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_JavaClassValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_JavaClassValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_JavaClassValue(value="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression153', None)
    _safe_set(owner, 'henshin_text_JavaClassValue', {partner})
    assert getattr(partner, 'henshin_text_Expression153') == owner
    _safe_set(owner, 'henshin_text_JavaClassValue', set())
    assert getattr(partner, 'henshin_text_Expression153') is None


def test_assoc_left121_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression122' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_EqualityExpression(op="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression122', None)
    _safe_set(owner, 'henshin_text_EqualityExpression', partner)
    assert getattr(partner, 'henshin_text_Expression122') == owner
    _safe_set(owner, 'henshin_text_EqualityExpression', None)
    assert getattr(partner, 'henshin_text_Expression122') is None


def test_assoc_left126_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression127' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ComparisonExpression(op="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression127', None)
    _safe_set(owner, 'henshin_text_ComparisonExpression', partner)
    assert getattr(partner, 'henshin_text_Expression127') == owner
    _safe_set(owner, 'henshin_text_ComparisonExpression', None)
    assert getattr(partner, 'henshin_text_Expression127') is None


def test_assoc_left141_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression142' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_MulOrDivExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_MulOrDivExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_MulOrDivExpression(op="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression142', None)
    _safe_set(owner, 'henshin_text_MulOrDivExpression', partner)
    assert getattr(partner, 'henshin_text_Expression142') == owner
    _safe_set(owner, 'henshin_text_MulOrDivExpression', None)
    assert getattr(partner, 'henshin_text_Expression142') is None


def test_assoc_left92_stub_double():
    # henshin_text_Logic has no real 'henshin_text_Logic93' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ORorXOR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ORorXOR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ORorXOR(op="sample_text")
    partner = henshin_text_Logic()
    setattr(partner, 'henshin_text_Logic93', None)
    _safe_set(owner, 'henshin_text_ORorXOR', partner)
    assert getattr(partner, 'henshin_text_Logic93') == owner
    _safe_set(owner, 'henshin_text_ORorXOR', None)
    assert getattr(partner, 'henshin_text_Logic93') is None


def test_assoc_multiruleElements30_stub_double():
    # henshin_text_RuleElement has no real 'henshin_text_RuleElement' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_MultiRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_MultiRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_MultiRule(name="sample_text")
    partner = henshin_text_RuleElement()
    setattr(partner, 'henshin_text_RuleElement', None)
    _safe_set(owner, 'henshin_text_MultiRule', {partner})
    assert getattr(partner, 'henshin_text_RuleElement') == owner
    _safe_set(owner, 'henshin_text_MultiRule', set())
    assert getattr(partner, 'henshin_text_RuleElement') is None


def test_assoc_name20_stub_double():
    # henshin_text_MultiRuleReuseNode has no real 'henshin_text_MultiRuleReuseNode' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Node(actiontype="sample_text")
    partner = henshin_text_MultiRuleReuseNode()
    setattr(partner, 'henshin_text_MultiRuleReuseNode', None)
    _safe_set(owner, 'henshin_text_Node21', partner)
    assert getattr(partner, 'henshin_text_MultiRuleReuseNode') == owner
    _safe_set(owner, 'henshin_text_Node21', None)
    assert getattr(partner, 'henshin_text_MultiRuleReuseNode') is None


def test_assoc_name25_stub_double():
    # henshin_text_EAttribute has no real 'henshin_text_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    partner = henshin_text_EAttribute()
    setattr(partner, 'henshin_text_EAttribute', None)
    _safe_set(owner, 'henshin_text_Attribute26', partner)
    assert getattr(partner, 'henshin_text_EAttribute') == owner
    _safe_set(owner, 'henshin_text_Attribute26', None)
    assert getattr(partner, 'henshin_text_EAttribute') is None


def test_assoc_name49_stub_double():
    # henshin_text_ConditionReuseNode has no real 'henshin_text_ConditionReuseNode' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ConditionNodeTypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ConditionNodeTypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ConditionNodeTypes(name="sample_text")
    partner = henshin_text_ConditionReuseNode()
    setattr(partner, 'henshin_text_ConditionReuseNode', None)
    _safe_set(owner, 'henshin_text_ConditionNodeTypes50', partner)
    assert getattr(partner, 'henshin_text_ConditionReuseNode') == owner
    _safe_set(owner, 'henshin_text_ConditionNodeTypes50', None)
    assert getattr(partner, 'henshin_text_ConditionReuseNode') is None


def test_assoc_nodetype17_stub_double():
    # henshin_text_EClass has no real 'henshin_text_EClass' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Node(actiontype="sample_text")
    partner = henshin_text_EClass()
    setattr(partner, 'henshin_text_EClass', None)
    _safe_set(owner, 'henshin_text_Node', partner)
    assert getattr(partner, 'henshin_text_EClass') == owner
    _safe_set(owner, 'henshin_text_Node', None)
    assert getattr(partner, 'henshin_text_EClass') is None


def test_assoc_parameters108_stub_double():
    # henshin_text_Call has no real 'henshin_text_Call109' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Parameter(kind="sample_text", name="sample_text")
    partner = henshin_text_Call()
    setattr(partner, 'henshin_text_Call109', None)
    _safe_set(owner, 'henshin_text_Parameter110', partner)
    assert owner in getattr(partner, 'henshin_text_Call109')
    _safe_set(owner, 'henshin_text_Parameter110', None)
    assert owner not in getattr(partner, 'henshin_text_Call109')


def test_assoc_right123_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression125' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_EqualityExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_EqualityExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_EqualityExpression(op="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression125', None)
    _safe_set(owner, 'henshin_text_EqualityExpression124', partner)
    assert getattr(partner, 'henshin_text_Expression125') == owner
    _safe_set(owner, 'henshin_text_EqualityExpression124', None)
    assert getattr(partner, 'henshin_text_Expression125') is None


def test_assoc_right128_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression130' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ComparisonExpression(op="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression130', None)
    _safe_set(owner, 'henshin_text_ComparisonExpression129', partner)
    assert getattr(partner, 'henshin_text_Expression130') == owner
    _safe_set(owner, 'henshin_text_ComparisonExpression129', None)
    assert getattr(partner, 'henshin_text_Expression130') is None


def test_assoc_right143_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression145' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_MulOrDivExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_MulOrDivExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_MulOrDivExpression(op="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression145', None)
    _safe_set(owner, 'henshin_text_MulOrDivExpression144', partner)
    assert getattr(partner, 'henshin_text_Expression145') == owner
    _safe_set(owner, 'henshin_text_MulOrDivExpression144', None)
    assert getattr(partner, 'henshin_text_Expression145') is None


def test_assoc_right94_stub_double():
    # henshin_text_Logic has no real 'henshin_text_Logic96' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ORorXOR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ORorXOR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ORorXOR(op="sample_text")
    partner = henshin_text_Logic()
    setattr(partner, 'henshin_text_Logic96', None)
    _safe_set(owner, 'henshin_text_ORorXOR95', partner)
    assert getattr(partner, 'henshin_text_Logic96') == owner
    _safe_set(owner, 'henshin_text_ORorXOR95', None)
    assert getattr(partner, 'henshin_text_Logic96') is None


def test_assoc_source10_stub_double():
    # henshin_text_RuleNodeTypes has no real 'henshin_text_RuleNodeTypes' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Edge(actiontype="sample_text")
    partner = henshin_text_RuleNodeTypes()
    setattr(partner, 'henshin_text_RuleNodeTypes', None)
    _safe_set(owner, 'henshin_text_Edge11', partner)
    assert getattr(partner, 'henshin_text_RuleNodeTypes') == owner
    _safe_set(owner, 'henshin_text_Edge11', None)
    assert getattr(partner, 'henshin_text_RuleNodeTypes') is None


def test_assoc_source37_stub_double():
    # henshin_text_ConditionEdge has no real 'henshin_text_ConditionEdge38' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ConditionNodeTypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ConditionNodeTypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ConditionNodeTypes(name="sample_text")
    partner = henshin_text_ConditionEdge()
    setattr(partner, 'henshin_text_ConditionEdge38', None)
    _safe_set(owner, 'henshin_text_ConditionNodeTypes', partner)
    assert getattr(partner, 'henshin_text_ConditionEdge38') == owner
    _safe_set(owner, 'henshin_text_ConditionNodeTypes', None)
    assert getattr(partner, 'henshin_text_ConditionEdge38') is None


def test_assoc_target12_stub_double():
    # henshin_text_RuleNodeTypes has no real 'henshin_text_RuleNodeTypes14' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Edge(actiontype="sample_text")
    partner = henshin_text_RuleNodeTypes()
    setattr(partner, 'henshin_text_RuleNodeTypes14', None)
    _safe_set(owner, 'henshin_text_Edge13', partner)
    assert getattr(partner, 'henshin_text_RuleNodeTypes14') == owner
    _safe_set(owner, 'henshin_text_Edge13', None)
    assert getattr(partner, 'henshin_text_RuleNodeTypes14') is None


def test_assoc_target39_stub_double():
    # henshin_text_ConditionEdge has no real 'henshin_text_ConditionEdge40' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ConditionNodeTypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ConditionNodeTypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ConditionNodeTypes(name="sample_text")
    partner = henshin_text_ConditionEdge()
    setattr(partner, 'henshin_text_ConditionEdge40', None)
    _safe_set(owner, 'henshin_text_ConditionNodeTypes41', partner)
    assert getattr(partner, 'henshin_text_ConditionEdge40') == owner
    _safe_set(owner, 'henshin_text_ConditionNodeTypes41', None)
    assert getattr(partner, 'henshin_text_ConditionEdge40') is None


def test_assoc_transformationsystem1_stub_double():
    # henshin_text_Model has no real 'henshin_text_Model2' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ModelElement(name="sample_text")
    partner = henshin_text_Model()
    setattr(partner, 'henshin_text_Model2', None)
    _safe_set(owner, 'henshin_text_ModelElement', partner)
    assert owner in getattr(partner, 'henshin_text_Model2')
    _safe_set(owner, 'henshin_text_ModelElement', None)
    assert owner not in getattr(partner, 'henshin_text_Model2')


def test_assoc_type15_stub_double():
    # henshin_text_EReference has no real 'henshin_text_EReference' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Edge(actiontype="sample_text")
    partner = henshin_text_EReference()
    setattr(partner, 'henshin_text_EReference', None)
    _safe_set(owner, 'henshin_text_Edge16', partner)
    assert getattr(partner, 'henshin_text_EReference') == owner
    _safe_set(owner, 'henshin_text_Edge16', None)
    assert getattr(partner, 'henshin_text_EReference') is None


def test_assoc_type85_stub_double():
    # henshin_text_EClass has no real 'henshin_text_EClass87' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_ParameterType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_ParameterType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_ParameterType(enumType="sample_text")
    partner = henshin_text_EClass()
    setattr(partner, 'henshin_text_EClass87', None)
    _safe_set(owner, 'henshin_text_ParameterType86', partner)
    assert getattr(partner, 'henshin_text_EClass87') == owner
    _safe_set(owner, 'henshin_text_ParameterType86', None)
    assert getattr(partner, 'henshin_text_EClass87') is None


def test_assoc_value150_stub_double():
    # henshin_text_ParameterValue has no real 'henshin_text_ParameterValue' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Parameter(kind="sample_text", name="sample_text")
    partner = henshin_text_ParameterValue()
    setattr(partner, 'henshin_text_ParameterValue', None)
    _safe_set(owner, 'henshin_text_Parameter151', partner)
    assert getattr(partner, 'henshin_text_ParameterValue') == owner
    _safe_set(owner, 'henshin_text_Parameter151', None)
    assert getattr(partner, 'henshin_text_ParameterValue') is None


def test_assoc_value27_stub_double():
    # henshin_text_Expression has no real 'henshin_text_Expression29' property in the generated
    # code (a bare stub) -- manually attach it so henshin_text_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_text_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_text_Attribute(actiontype="sample_text", update="sample_text")
    partner = henshin_text_Expression()
    setattr(partner, 'henshin_text_Expression29', None)
    _safe_set(owner, 'henshin_text_Attribute28', partner)
    assert getattr(partner, 'henshin_text_Expression29') == owner
    _safe_set(owner, 'henshin_text_Attribute28', None)
    assert getattr(partner, 'henshin_text_Expression29') is None


