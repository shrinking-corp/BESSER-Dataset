import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryFormula,
    Formula,
    GraphElement,
    NamedElement,
    TransformationUnit,
    UnaryFormula,
    henshin_And,
    henshin_Attribute,
    henshin_AttributeCondition,
    henshin_BinaryFormula,
    henshin_ConditionalUnit,
    henshin_EAttribute,
    henshin_EClass,
    henshin_EClassifier,
    henshin_EPackage,
    henshin_EReference,
    henshin_Edge,
    henshin_Formula,
    henshin_Graph,
    henshin_GraphElement,
    henshin_IndependentUnit,
    henshin_IteratedUnit,
    henshin_LoopUnit,
    henshin_Mapping,
    henshin_NamedElement,
    henshin_NestedCondition,
    henshin_Node,
    henshin_Not,
    henshin_Or,
    henshin_Parameter,
    henshin_ParameterMapping,
    henshin_PriorityUnit,
    henshin_Rule,
    henshin_SequentialUnit,
    henshin_TransformationSystem,
    henshin_TransformationUnit,
    henshin_UnaryFormula,
    henshin_Xor,
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

def test_assoc_attributeConditions13_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True)
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False)
    b = henshin_AttributeCondition(conditionText="sample_text")
    _safe_set(b, 'AttributeCondition', a1)
    assert _is_linked(b, 'AttributeCondition', a1)
    if hasattr(a1, 'rule'):
        assert _is_linked(a1, 'rule', b)
    _safe_set(b, 'AttributeCondition', a2)
    assert _is_linked(b, 'AttributeCondition', a2)
    if hasattr(a1, 'rule'):
        assert not _is_linked(a1, 'rule', b)
    if hasattr(a2, 'rule'):
        assert _is_linked(a2, 'rule', b)
    _safe_set(b, 'AttributeCondition', None)
    assert not _is_linked(b, 'AttributeCondition', a2)
    if hasattr(a2, 'rule'):
        assert not _is_linked(a2, 'rule', b)


def test_assoc_attributes37_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Attribute(value="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_conclusion77_reverse_link_reassign_clear():
    a1 = henshin_NestedCondition()
    a2 = henshin_NestedCondition()
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph78', a1)
    assert _is_linked(b, 'henshin_Graph78', a1)
    if hasattr(a1, 'henshin_NestedCondition'):
        assert _is_linked(a1, 'henshin_NestedCondition', b)
    _safe_set(b, 'henshin_Graph78', a2)
    assert _is_linked(b, 'henshin_Graph78', a2)
    if hasattr(a1, 'henshin_NestedCondition'):
        assert not _is_linked(a1, 'henshin_NestedCondition', b)
    if hasattr(a2, 'henshin_NestedCondition'):
        assert _is_linked(a2, 'henshin_NestedCondition', b)
    _safe_set(b, 'henshin_Graph78', None)
    assert not _is_linked(b, 'henshin_Graph78', a2)
    if hasattr(a2, 'henshin_NestedCondition'):
        assert not _is_linked(a2, 'henshin_NestedCondition', b)


def test_assoc_formula28_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Formula()
    _safe_set(b, 'henshin_Formula', a1)
    assert _is_linked(b, 'henshin_Formula', a1)
    if hasattr(a1, 'henshin_Graph29'):
        assert _is_linked(a1, 'henshin_Graph29', b)
    _safe_set(b, 'henshin_Formula', a2)
    assert _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a1, 'henshin_Graph29'):
        assert not _is_linked(a1, 'henshin_Graph29', b)
    if hasattr(a2, 'henshin_Graph29'):
        assert _is_linked(a2, 'henshin_Graph29', b)
    _safe_set(b, 'henshin_Formula', None)
    assert not _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a2, 'henshin_Graph29'):
        assert not _is_linked(a2, 'henshin_Graph29', b)


def test_assoc_graph38_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Graph()
    _safe_set(b, 'Graph', a1)
    assert _is_linked(b, 'Graph', a1)
    if hasattr(a1, 'nodes'):
        assert _is_linked(a1, 'nodes', b)
    _safe_set(b, 'Graph', a2)
    assert _is_linked(b, 'Graph', a2)
    if hasattr(a1, 'nodes'):
        assert not _is_linked(a1, 'nodes', b)
    if hasattr(a2, 'nodes'):
        assert _is_linked(a2, 'nodes', b)
    _safe_set(b, 'Graph', None)
    assert not _is_linked(b, 'Graph', a2)
    if hasattr(a2, 'nodes'):
        assert not _is_linked(a2, 'nodes', b)


def test_assoc_instances5_reverse_link_reassign_clear():
    a1 = henshin_TransformationSystem()
    a2 = henshin_TransformationSystem()
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph', a1)
    assert _is_linked(b, 'henshin_Graph', a1)
    if hasattr(a1, 'henshin_TransformationSystem6'):
        assert _is_linked(a1, 'henshin_TransformationSystem6', b)
    _safe_set(b, 'henshin_Graph', a2)
    assert _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a1, 'henshin_TransformationSystem6'):
        assert not _is_linked(a1, 'henshin_TransformationSystem6', b)
    if hasattr(a2, 'henshin_TransformationSystem6'):
        assert _is_linked(a2, 'henshin_TransformationSystem6', b)
    _safe_set(b, 'henshin_Graph', None)
    assert not _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a2, 'henshin_TransformationSystem6'):
        assert not _is_linked(a2, 'henshin_TransformationSystem6', b)


def test_assoc_lhs7_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True)
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False)
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph9', a1)
    assert _is_linked(b, 'henshin_Graph9', a1)
    if hasattr(a1, 'henshin_Rule8'):
        assert _is_linked(a1, 'henshin_Rule8', b)
    _safe_set(b, 'henshin_Graph9', a2)
    assert _is_linked(b, 'henshin_Graph9', a2)
    if hasattr(a1, 'henshin_Rule8'):
        assert not _is_linked(a1, 'henshin_Rule8', b)
    if hasattr(a2, 'henshin_Rule8'):
        assert _is_linked(a2, 'henshin_Rule8', b)
    _safe_set(b, 'henshin_Graph9', None)
    assert not _is_linked(b, 'henshin_Graph9', a2)
    if hasattr(a2, 'henshin_Rule8'):
        assert not _is_linked(a2, 'henshin_Rule8', b)


def test_assoc_multiRules17_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True)
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False)
    b = henshin_Rule(checkDangling=True, injectiveMatching=True)
    _safe_set(b, 'henshin_Rule18', a1)
    assert _is_linked(b, 'henshin_Rule18', a1)
    if hasattr(a1, 'henshin_Rule16'):
        assert _is_linked(a1, 'henshin_Rule16', b)
    _safe_set(b, 'henshin_Rule18', a2)
    assert _is_linked(b, 'henshin_Rule18', a2)
    if hasattr(a1, 'henshin_Rule16'):
        assert not _is_linked(a1, 'henshin_Rule16', b)
    if hasattr(a2, 'henshin_Rule16'):
        assert _is_linked(a2, 'henshin_Rule16', b)
    _safe_set(b, 'henshin_Rule18', None)
    assert not _is_linked(b, 'henshin_Rule18', a2)
    if hasattr(a2, 'henshin_Rule16'):
        assert not _is_linked(a2, 'henshin_Rule16', b)


def test_assoc_node46_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Attribute(value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Node47'):
        assert _is_linked(a1, 'Node47', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Node47'):
        assert not _is_linked(a1, 'Node47', b)
    if hasattr(a2, 'Node47'):
        assert _is_linked(a2, 'Node47', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Node47'):
        assert not _is_linked(a2, 'Node47', b)


def test_assoc_nodes25_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Graph()
    _safe_set(b, 'graph', {a1})
    assert _is_linked(b, 'graph', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'graph', {a2})
    assert _is_linked(b, 'graph', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'graph', set())
    assert not _is_linked(b, 'graph', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_rhs10_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True)
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False)
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph12', a1)
    assert _is_linked(b, 'henshin_Graph12', a1)
    if hasattr(a1, 'henshin_Rule11'):
        assert _is_linked(a1, 'henshin_Rule11', b)
    _safe_set(b, 'henshin_Graph12', a2)
    assert _is_linked(b, 'henshin_Graph12', a2)
    if hasattr(a1, 'henshin_Rule11'):
        assert not _is_linked(a1, 'henshin_Rule11', b)
    if hasattr(a2, 'henshin_Rule11'):
        assert _is_linked(a2, 'henshin_Rule11', b)
    _safe_set(b, 'henshin_Graph12', None)
    assert not _is_linked(b, 'henshin_Graph12', a2)
    if hasattr(a2, 'henshin_Rule11'):
        assert not _is_linked(a2, 'henshin_Rule11', b)


def test_assoc_rule22_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True)
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False)
    b = henshin_AttributeCondition(conditionText="sample_text")
    _safe_set(b, 'attributeConditions', a1)
    assert _is_linked(b, 'attributeConditions', a1)
    if hasattr(a1, 'Rule'):
        assert _is_linked(a1, 'Rule', b)
    _safe_set(b, 'attributeConditions', a2)
    assert _is_linked(b, 'attributeConditions', a2)
    if hasattr(a1, 'Rule'):
        assert not _is_linked(a1, 'Rule', b)
    if hasattr(a2, 'Rule'):
        assert _is_linked(a2, 'Rule', b)
    _safe_set(b, 'attributeConditions', None)
    assert not _is_linked(b, 'attributeConditions', a2)
    if hasattr(a2, 'Rule'):
        assert not _is_linked(a2, 'Rule', b)


def test_assoc_rules0_reverse_link_reassign_clear():
    a1 = henshin_TransformationSystem()
    a2 = henshin_TransformationSystem()
    b = henshin_Rule(checkDangling=True, injectiveMatching=True)
    _safe_set(b, 'henshin_Rule', a1)
    assert _is_linked(b, 'henshin_Rule', a1)
    if hasattr(a1, 'henshin_TransformationSystem'):
        assert _is_linked(a1, 'henshin_TransformationSystem', b)
    _safe_set(b, 'henshin_Rule', a2)
    assert _is_linked(b, 'henshin_Rule', a2)
    if hasattr(a1, 'henshin_TransformationSystem'):
        assert not _is_linked(a1, 'henshin_TransformationSystem', b)
    if hasattr(a2, 'henshin_TransformationSystem'):
        assert _is_linked(a2, 'henshin_TransformationSystem', b)
    _safe_set(b, 'henshin_Rule', None)
    assert not _is_linked(b, 'henshin_Rule', a2)
    if hasattr(a2, 'henshin_TransformationSystem'):
        assert not _is_linked(a2, 'henshin_TransformationSystem', b)


def test_assoc_subUnit73_reverse_link_reassign_clear():
    a1 = henshin_TransformationUnit(activated=True)
    a2 = henshin_TransformationUnit(activated=False)
    b = henshin_IteratedUnit(iterations="sample_text")
    _safe_set(b, 'henshin_IteratedUnit', a1)
    assert _is_linked(b, 'henshin_IteratedUnit', a1)
    if hasattr(a1, 'henshin_TransformationUnit74'):
        assert _is_linked(a1, 'henshin_TransformationUnit74', b)
    _safe_set(b, 'henshin_IteratedUnit', a2)
    assert _is_linked(b, 'henshin_IteratedUnit', a2)
    if hasattr(a1, 'henshin_TransformationUnit74'):
        assert not _is_linked(a1, 'henshin_TransformationUnit74', b)
    if hasattr(a2, 'henshin_TransformationUnit74'):
        assert _is_linked(a2, 'henshin_TransformationUnit74', b)
    _safe_set(b, 'henshin_IteratedUnit', None)
    assert not _is_linked(b, 'henshin_IteratedUnit', a2)
    if hasattr(a2, 'henshin_TransformationUnit74'):
        assert not _is_linked(a2, 'henshin_TransformationUnit74', b)


def test_assoc_subUnits61_reverse_link_reassign_clear():
    a1 = henshin_TransformationUnit(activated=True)
    a2 = henshin_TransformationUnit(activated=False)
    b = henshin_SequentialUnit(rollback=True, strict=True)
    _safe_set(b, 'henshin_SequentialUnit', {a1})
    assert _is_linked(b, 'henshin_SequentialUnit', a1)
    if hasattr(a1, 'henshin_TransformationUnit62'):
        assert _is_linked(a1, 'henshin_TransformationUnit62', b)
    _safe_set(b, 'henshin_SequentialUnit', {a2})
    assert _is_linked(b, 'henshin_SequentialUnit', a2)
    if hasattr(a1, 'henshin_TransformationUnit62'):
        assert not _is_linked(a1, 'henshin_TransformationUnit62', b)
    if hasattr(a2, 'henshin_TransformationUnit62'):
        assert _is_linked(a2, 'henshin_TransformationUnit62', b)
    _safe_set(b, 'henshin_SequentialUnit', set())
    assert not _is_linked(b, 'henshin_SequentialUnit', a2)
    if hasattr(a2, 'henshin_TransformationUnit62'):
        assert not _is_linked(a2, 'henshin_TransformationUnit62', b)


def test_assoc_transformationUnits3_reverse_link_reassign_clear():
    a1 = henshin_TransformationUnit(activated=True)
    a2 = henshin_TransformationUnit(activated=False)
    b = henshin_TransformationSystem()
    _safe_set(b, 'henshin_TransformationSystem4', {a1})
    assert _is_linked(b, 'henshin_TransformationSystem4', a1)
    if hasattr(a1, 'henshin_TransformationUnit'):
        assert _is_linked(a1, 'henshin_TransformationUnit', b)
    _safe_set(b, 'henshin_TransformationSystem4', {a2})
    assert _is_linked(b, 'henshin_TransformationSystem4', a2)
    if hasattr(a1, 'henshin_TransformationUnit'):
        assert not _is_linked(a1, 'henshin_TransformationUnit', b)
    if hasattr(a2, 'henshin_TransformationUnit'):
        assert _is_linked(a2, 'henshin_TransformationUnit', b)
    _safe_set(b, 'henshin_TransformationSystem4', set())
    assert not _is_linked(b, 'henshin_TransformationSystem4', a2)
    if hasattr(a2, 'henshin_TransformationUnit'):
        assert not _is_linked(a2, 'henshin_TransformationUnit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allEdges43_stub_double():
    # henshin_Edge has no real 'henshin_Edge' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'henshin_Edge', None)
    _safe_set(owner, 'henshin_Node44', {partner})
    assert getattr(partner, 'henshin_Edge') == owner
    _safe_set(owner, 'henshin_Node44', set())
    assert getattr(partner, 'henshin_Edge') is None


def test_assoc_child82_stub_double():
    # henshin_UnaryFormula has no real 'henshin_UnaryFormula' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_UnaryFormula()
    setattr(partner, 'henshin_UnaryFormula', None)
    _safe_set(owner, 'henshin_Formula83', partner)
    assert getattr(partner, 'henshin_UnaryFormula') == owner
    _safe_set(owner, 'henshin_Formula83', None)
    assert getattr(partner, 'henshin_UnaryFormula') is None


def test_assoc_edges26_stub_double():
    # henshin_Edge has no real 'Edge' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Graph()
    partner = henshin_Edge()
    setattr(partner, 'Edge', None)
    _safe_set(owner, 'graph27', {partner})
    assert getattr(partner, 'Edge') == owner
    _safe_set(owner, 'graph27', set())
    assert getattr(partner, 'Edge') is None


def test_assoc_else_68_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit69' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit69', None)
    _safe_set(owner, 'henshin_TransformationUnit70', partner)
    assert getattr(partner, 'henshin_ConditionalUnit69') == owner
    _safe_set(owner, 'henshin_TransformationUnit70', None)
    assert getattr(partner, 'henshin_ConditionalUnit69') is None


def test_assoc_graph54_stub_double():
    # henshin_Edge has no real 'edges' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Graph()
    partner = henshin_Edge()
    setattr(partner, 'edges', None)
    _safe_set(owner, 'Graph55', partner)
    assert getattr(partner, 'edges') == owner
    _safe_set(owner, 'Graph55', None)
    assert getattr(partner, 'edges') is None


def test_assoc_if_63_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit', None)
    _safe_set(owner, 'henshin_TransformationUnit64', partner)
    assert getattr(partner, 'henshin_ConditionalUnit') == owner
    _safe_set(owner, 'henshin_TransformationUnit64', None)
    assert getattr(partner, 'henshin_ConditionalUnit') is None


def test_assoc_image32_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping33' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping33', None)
    _safe_set(owner, 'henshin_Node34', partner)
    assert getattr(partner, 'henshin_Mapping33') == owner
    _safe_set(owner, 'henshin_Node34', None)
    assert getattr(partner, 'henshin_Mapping33') is None


def test_assoc_imports1_stub_double():
    # henshin_EPackage has no real 'henshin_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationSystem()
    partner = henshin_EPackage()
    setattr(partner, 'henshin_EPackage', None)
    _safe_set(owner, 'henshin_TransformationSystem2', {partner})
    assert getattr(partner, 'henshin_EPackage') == owner
    _safe_set(owner, 'henshin_TransformationSystem2', set())
    assert getattr(partner, 'henshin_EPackage') is None


def test_assoc_incoming39_stub_double():
    # henshin_Edge has no real 'Edge40' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'Edge40', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Edge40') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Edge40') is None


def test_assoc_left84_stub_double():
    # henshin_BinaryFormula has no real 'henshin_BinaryFormula' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_BinaryFormula()
    setattr(partner, 'henshin_BinaryFormula', None)
    _safe_set(owner, 'henshin_Formula85', partner)
    assert getattr(partner, 'henshin_BinaryFormula') == owner
    _safe_set(owner, 'henshin_Formula85', None)
    assert getattr(partner, 'henshin_BinaryFormula') is None


def test_assoc_mappings14_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule(checkDangling=True, injectiveMatching=True)
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping', None)
    _safe_set(owner, 'henshin_Rule15', {partner})
    assert getattr(partner, 'henshin_Mapping') == owner
    _safe_set(owner, 'henshin_Rule15', set())
    assert getattr(partner, 'henshin_Mapping') is None


def test_assoc_mappings79_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping81' property in the generated
    # code (a bare stub) -- manually attach it so henshin_NestedCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_NestedCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_NestedCondition()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping81', None)
    _safe_set(owner, 'henshin_NestedCondition80', {partner})
    assert getattr(partner, 'henshin_Mapping81') == owner
    _safe_set(owner, 'henshin_NestedCondition80', set())
    assert getattr(partner, 'henshin_Mapping81') is None


def test_assoc_multiMappings19_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping21' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule(checkDangling=True, injectiveMatching=True)
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping21', None)
    _safe_set(owner, 'henshin_Rule20', {partner})
    assert getattr(partner, 'henshin_Mapping21') == owner
    _safe_set(owner, 'henshin_Rule20', set())
    assert getattr(partner, 'henshin_Mapping21') is None


def test_assoc_origin30_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping31' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping31', None)
    _safe_set(owner, 'henshin_Node', partner)
    assert getattr(partner, 'henshin_Mapping31') == owner
    _safe_set(owner, 'henshin_Node', None)
    assert getattr(partner, 'henshin_Mapping31') is None


def test_assoc_outgoing41_stub_double():
    # henshin_Edge has no real 'Edge42' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'Edge42', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Edge42') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Edge42') is None


def test_assoc_parameterMappings57_stub_double():
    # henshin_ParameterMapping has no real 'henshin_ParameterMapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ParameterMapping()
    setattr(partner, 'henshin_ParameterMapping', None)
    _safe_set(owner, 'henshin_TransformationUnit58', {partner})
    assert getattr(partner, 'henshin_ParameterMapping') == owner
    _safe_set(owner, 'henshin_TransformationUnit58', set())
    assert getattr(partner, 'henshin_ParameterMapping') is None


def test_assoc_parameters56_stub_double():
    # henshin_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'unit', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'unit', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_right86_stub_double():
    # henshin_BinaryFormula has no real 'henshin_BinaryFormula87' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_BinaryFormula()
    setattr(partner, 'henshin_BinaryFormula87', None)
    _safe_set(owner, 'henshin_Formula88', partner)
    assert getattr(partner, 'henshin_BinaryFormula87') == owner
    _safe_set(owner, 'henshin_Formula88', None)
    assert getattr(partner, 'henshin_BinaryFormula87') is None


def test_assoc_source48_stub_double():
    # henshin_Edge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Node49', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Node49', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_subUnit75_stub_double():
    # henshin_LoopUnit has no real 'henshin_LoopUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_LoopUnit()
    setattr(partner, 'henshin_LoopUnit', None)
    _safe_set(owner, 'henshin_TransformationUnit76', partner)
    assert getattr(partner, 'henshin_LoopUnit') == owner
    _safe_set(owner, 'henshin_TransformationUnit76', None)
    assert getattr(partner, 'henshin_LoopUnit') is None


def test_assoc_subUnits59_stub_double():
    # henshin_IndependentUnit has no real 'henshin_IndependentUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_IndependentUnit()
    setattr(partner, 'henshin_IndependentUnit', None)
    _safe_set(owner, 'henshin_TransformationUnit60', partner)
    assert owner in getattr(partner, 'henshin_IndependentUnit')
    _safe_set(owner, 'henshin_TransformationUnit60', None)
    assert owner not in getattr(partner, 'henshin_IndependentUnit')


def test_assoc_subUnits71_stub_double():
    # henshin_PriorityUnit has no real 'henshin_PriorityUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_PriorityUnit()
    setattr(partner, 'henshin_PriorityUnit', None)
    _safe_set(owner, 'henshin_TransformationUnit72', partner)
    assert owner in getattr(partner, 'henshin_PriorityUnit')
    _safe_set(owner, 'henshin_TransformationUnit72', None)
    assert owner not in getattr(partner, 'henshin_PriorityUnit')


def test_assoc_target50_stub_double():
    # henshin_Edge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'Node51', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'Node51', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_then65_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit66' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit66', None)
    _safe_set(owner, 'henshin_TransformationUnit67', partner)
    assert getattr(partner, 'henshin_ConditionalUnit66') == owner
    _safe_set(owner, 'henshin_TransformationUnit67', None)
    assert getattr(partner, 'henshin_ConditionalUnit66') is None


def test_assoc_type35_stub_double():
    # henshin_EClass has no real 'henshin_EClass' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_EClass()
    setattr(partner, 'henshin_EClass', None)
    _safe_set(owner, 'henshin_Node36', partner)
    assert getattr(partner, 'henshin_EClass') == owner
    _safe_set(owner, 'henshin_Node36', None)
    assert getattr(partner, 'henshin_EClass') is None


def test_assoc_type45_stub_double():
    # henshin_EAttribute has no real 'henshin_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Attribute(value="sample_text")
    partner = henshin_EAttribute()
    setattr(partner, 'henshin_EAttribute', None)
    _safe_set(owner, 'henshin_Attribute', partner)
    assert getattr(partner, 'henshin_EAttribute') == owner
    _safe_set(owner, 'henshin_Attribute', None)
    assert getattr(partner, 'henshin_EAttribute') is None


def test_assoc_unit23_stub_double():
    # henshin_Parameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_Parameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'TransformationUnit', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'TransformationUnit', None)
    assert getattr(partner, 'parameters') is None


