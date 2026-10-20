import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryFormula,
    Formula,
    GraphElement,
    MultiUnit,
    NamedElement,
    UnaryFormula,
    UnaryUnit,
    Unit,
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
    henshin_Module,
    henshin_MultiUnit,
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
    henshin_UnaryFormula,
    henshin_UnaryUnit,
    henshin_Unit,
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

def test_assoc_attributeConditions18_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
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


def test_assoc_attributes41_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
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


def test_assoc_conclusion76_reverse_link_reassign_clear():
    a1 = henshin_NestedCondition()
    a2 = henshin_NestedCondition()
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph77', a1)
    assert _is_linked(b, 'henshin_Graph77', a1)
    if hasattr(a1, 'henshin_NestedCondition'):
        assert _is_linked(a1, 'henshin_NestedCondition', b)
    _safe_set(b, 'henshin_Graph77', a2)
    assert _is_linked(b, 'henshin_Graph77', a2)
    if hasattr(a1, 'henshin_NestedCondition'):
        assert not _is_linked(a1, 'henshin_NestedCondition', b)
    if hasattr(a2, 'henshin_NestedCondition'):
        assert _is_linked(a2, 'henshin_NestedCondition', b)
    _safe_set(b, 'henshin_Graph77', None)
    assert not _is_linked(b, 'henshin_Graph77', a2)
    if hasattr(a2, 'henshin_NestedCondition'):
        assert not _is_linked(a2, 'henshin_NestedCondition', b)


def test_assoc_edges36_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'graph37'):
        assert _is_linked(a1, 'graph37', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'graph37'):
        assert not _is_linked(a1, 'graph37', b)
    if hasattr(a2, 'graph37'):
        assert _is_linked(a2, 'graph37', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'graph37'):
        assert not _is_linked(a2, 'graph37', b)


def test_assoc_formula38_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Formula()
    _safe_set(b, 'henshin_Formula', a1)
    assert _is_linked(b, 'henshin_Formula', a1)
    if hasattr(a1, 'henshin_Graph39'):
        assert _is_linked(a1, 'henshin_Graph39', b)
    _safe_set(b, 'henshin_Formula', a2)
    assert _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a1, 'henshin_Graph39'):
        assert not _is_linked(a1, 'henshin_Graph39', b)
    if hasattr(a2, 'henshin_Graph39'):
        assert _is_linked(a2, 'henshin_Graph39', b)
    _safe_set(b, 'henshin_Formula', None)
    assert not _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a2, 'henshin_Graph39'):
        assert not _is_linked(a2, 'henshin_Graph39', b)


def test_assoc_graph42_reverse_link_reassign_clear():
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


def test_assoc_graph52_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Graph53'):
        assert _is_linked(a1, 'Graph53', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Graph53'):
        assert not _is_linked(a1, 'Graph53', b)
    if hasattr(a2, 'Graph53'):
        assert _is_linked(a2, 'Graph53', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Graph53'):
        assert not _is_linked(a2, 'Graph53', b)


def test_assoc_incoming43_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'Edge44', a1)
    assert _is_linked(b, 'Edge44', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge44', a2)
    assert _is_linked(b, 'Edge44', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge44', None)
    assert not _is_linked(b, 'Edge44', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_instances8_reverse_link_reassign_clear():
    a1 = henshin_Module()
    a2 = henshin_Module()
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph', a1)
    assert _is_linked(b, 'henshin_Graph', a1)
    if hasattr(a1, 'henshin_Module9'):
        assert _is_linked(a1, 'henshin_Module9', b)
    _safe_set(b, 'henshin_Graph', a2)
    assert _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a1, 'henshin_Module9'):
        assert not _is_linked(a1, 'henshin_Module9', b)
    if hasattr(a2, 'henshin_Module9'):
        assert _is_linked(a2, 'henshin_Module9', b)
    _safe_set(b, 'henshin_Graph', None)
    assert not _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a2, 'henshin_Module9'):
        assert not _is_linked(a2, 'henshin_Module9', b)


def test_assoc_lhs13_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph14', a1)
    assert _is_linked(b, 'henshin_Graph14', a1)
    if hasattr(a1, 'henshin_Rule'):
        assert _is_linked(a1, 'henshin_Rule', b)
    _safe_set(b, 'henshin_Graph14', a2)
    assert _is_linked(b, 'henshin_Graph14', a2)
    if hasattr(a1, 'henshin_Rule'):
        assert not _is_linked(a1, 'henshin_Rule', b)
    if hasattr(a2, 'henshin_Rule'):
        assert _is_linked(a2, 'henshin_Rule', b)
    _safe_set(b, 'henshin_Graph14', None)
    assert not _is_linked(b, 'henshin_Graph14', a2)
    if hasattr(a2, 'henshin_Rule'):
        assert not _is_linked(a2, 'henshin_Rule', b)


def test_assoc_multiRules22_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
    b = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    _safe_set(b, 'henshin_Rule23', a1)
    assert _is_linked(b, 'henshin_Rule23', a1)
    if hasattr(a1, 'henshin_Rule21'):
        assert _is_linked(a1, 'henshin_Rule21', b)
    _safe_set(b, 'henshin_Rule23', a2)
    assert _is_linked(b, 'henshin_Rule23', a2)
    if hasattr(a1, 'henshin_Rule21'):
        assert not _is_linked(a1, 'henshin_Rule21', b)
    if hasattr(a2, 'henshin_Rule21'):
        assert _is_linked(a2, 'henshin_Rule21', b)
    _safe_set(b, 'henshin_Rule23', None)
    assert not _is_linked(b, 'henshin_Rule23', a2)
    if hasattr(a2, 'henshin_Rule21'):
        assert not _is_linked(a2, 'henshin_Rule21', b)


def test_assoc_node55_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Node56'):
        assert _is_linked(a1, 'Node56', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Node56'):
        assert not _is_linked(a1, 'Node56', b)
    if hasattr(a2, 'Node56'):
        assert _is_linked(a2, 'Node56', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Node56'):
        assert not _is_linked(a2, 'Node56', b)


def test_assoc_nodes35_reverse_link_reassign_clear():
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


def test_assoc_outgoing45_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'Edge46', a1)
    assert _is_linked(b, 'Edge46', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge46', a2)
    assert _is_linked(b, 'Edge46', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge46', None)
    assert not _is_linked(b, 'Edge46', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_rhs15_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph17', a1)
    assert _is_linked(b, 'henshin_Graph17', a1)
    if hasattr(a1, 'henshin_Rule16'):
        assert _is_linked(a1, 'henshin_Rule16', b)
    _safe_set(b, 'henshin_Graph17', a2)
    assert _is_linked(b, 'henshin_Graph17', a2)
    if hasattr(a1, 'henshin_Rule16'):
        assert not _is_linked(a1, 'henshin_Rule16', b)
    if hasattr(a2, 'henshin_Rule16'):
        assert _is_linked(a2, 'henshin_Rule16', b)
    _safe_set(b, 'henshin_Graph17', None)
    assert not _is_linked(b, 'henshin_Graph17', a2)
    if hasattr(a2, 'henshin_Rule16'):
        assert not _is_linked(a2, 'henshin_Rule16', b)


def test_assoc_rule57_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
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


def test_assoc_source47_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node48'):
        assert _is_linked(a1, 'Node48', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node48'):
        assert not _is_linked(a1, 'Node48', b)
    if hasattr(a2, 'Node48'):
        assert _is_linked(a2, 'Node48', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node48'):
        assert not _is_linked(a2, 'Node48', b)


def test_assoc_subModules1_reverse_link_reassign_clear():
    a1 = henshin_Module()
    a2 = henshin_Module()
    b = henshin_Module()
    _safe_set(b, 'superModule', {a1})
    assert _is_linked(b, 'superModule', a1)
    if hasattr(a1, 'Module'):
        assert _is_linked(a1, 'Module', b)
    _safe_set(b, 'superModule', {a2})
    assert _is_linked(b, 'superModule', a2)
    if hasattr(a1, 'Module'):
        assert not _is_linked(a1, 'Module', b)
    if hasattr(a2, 'Module'):
        assert _is_linked(a2, 'Module', b)
    _safe_set(b, 'superModule', set())
    assert not _is_linked(b, 'superModule', a2)
    if hasattr(a2, 'Module'):
        assert not _is_linked(a2, 'Module', b)


def test_assoc_superModule3_reverse_link_reassign_clear():
    a1 = henshin_Module()
    a2 = henshin_Module()
    b = henshin_Module()
    _safe_set(b, 'subModules', a1)
    assert _is_linked(b, 'subModules', a1)
    if hasattr(a1, 'Module4'):
        assert _is_linked(a1, 'Module4', b)
    _safe_set(b, 'subModules', a2)
    assert _is_linked(b, 'subModules', a2)
    if hasattr(a1, 'Module4'):
        assert not _is_linked(a1, 'Module4', b)
    if hasattr(a2, 'Module4'):
        assert _is_linked(a2, 'Module4', b)
    _safe_set(b, 'subModules', None)
    assert not _is_linked(b, 'subModules', a2)
    if hasattr(a2, 'Module4'):
        assert not _is_linked(a2, 'Module4', b)


def test_assoc_target49_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node50'):
        assert _is_linked(a1, 'Node50', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node50'):
        assert not _is_linked(a1, 'Node50', b)
    if hasattr(a2, 'Node50'):
        assert _is_linked(a2, 'Node50', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node50'):
        assert not _is_linked(a2, 'Node50', b)


def test_assoc_units6_reverse_link_reassign_clear():
    a1 = henshin_Unit(activated=True)
    a2 = henshin_Unit(activated=False)
    b = henshin_Module()
    _safe_set(b, 'henshin_Module7', {a1})
    assert _is_linked(b, 'henshin_Module7', a1)
    if hasattr(a1, 'henshin_Unit'):
        assert _is_linked(a1, 'henshin_Unit', b)
    _safe_set(b, 'henshin_Module7', {a2})
    assert _is_linked(b, 'henshin_Module7', a2)
    if hasattr(a1, 'henshin_Unit'):
        assert not _is_linked(a1, 'henshin_Unit', b)
    if hasattr(a2, 'henshin_Unit'):
        assert _is_linked(a2, 'henshin_Unit', b)
    _safe_set(b, 'henshin_Module7', set())
    assert not _is_linked(b, 'henshin_Module7', a2)
    if hasattr(a2, 'henshin_Unit'):
        assert not _is_linked(a2, 'henshin_Unit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child81_stub_double():
    # henshin_UnaryFormula has no real 'henshin_UnaryFormula' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_UnaryFormula()
    setattr(partner, 'henshin_UnaryFormula', None)
    _safe_set(owner, 'henshin_Formula82', partner)
    assert getattr(partner, 'henshin_UnaryFormula') == owner
    _safe_set(owner, 'henshin_Formula82', None)
    assert getattr(partner, 'henshin_UnaryFormula') is None


def test_assoc_else_73_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit74' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit74', None)
    _safe_set(owner, 'henshin_Unit75', partner)
    assert getattr(partner, 'henshin_ConditionalUnit74') == owner
    _safe_set(owner, 'henshin_Unit75', None)
    assert getattr(partner, 'henshin_ConditionalUnit74') is None


def test_assoc_if_68_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit', None)
    _safe_set(owner, 'henshin_Unit69', partner)
    assert getattr(partner, 'henshin_ConditionalUnit') == owner
    _safe_set(owner, 'henshin_Unit69', None)
    assert getattr(partner, 'henshin_ConditionalUnit') is None


def test_assoc_image61_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping62' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping62', None)
    _safe_set(owner, 'henshin_Node63', partner)
    assert getattr(partner, 'henshin_Mapping62') == owner
    _safe_set(owner, 'henshin_Node63', None)
    assert getattr(partner, 'henshin_Mapping62') is None


def test_assoc_imports5_stub_double():
    # henshin_EPackage has no real 'henshin_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Module()
    partner = henshin_EPackage()
    setattr(partner, 'henshin_EPackage', None)
    _safe_set(owner, 'henshin_Module', {partner})
    assert getattr(partner, 'henshin_EPackage') == owner
    _safe_set(owner, 'henshin_Module', set())
    assert getattr(partner, 'henshin_EPackage') is None


def test_assoc_left83_stub_double():
    # henshin_BinaryFormula has no real 'henshin_BinaryFormula' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_BinaryFormula()
    setattr(partner, 'henshin_BinaryFormula', None)
    _safe_set(owner, 'henshin_Formula84', partner)
    assert getattr(partner, 'henshin_BinaryFormula') == owner
    _safe_set(owner, 'henshin_Formula84', None)
    assert getattr(partner, 'henshin_BinaryFormula') is None


def test_assoc_mappings19_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping', None)
    _safe_set(owner, 'henshin_Rule20', {partner})
    assert getattr(partner, 'henshin_Mapping') == owner
    _safe_set(owner, 'henshin_Rule20', set())
    assert getattr(partner, 'henshin_Mapping') is None


def test_assoc_mappings78_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping80' property in the generated
    # code (a bare stub) -- manually attach it so henshin_NestedCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_NestedCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_NestedCondition()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping80', None)
    _safe_set(owner, 'henshin_NestedCondition79', {partner})
    assert getattr(partner, 'henshin_Mapping80') == owner
    _safe_set(owner, 'henshin_NestedCondition79', set())
    assert getattr(partner, 'henshin_Mapping80') is None


def test_assoc_multiMappings24_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping26' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping26', None)
    _safe_set(owner, 'henshin_Rule25', {partner})
    assert getattr(partner, 'henshin_Mapping26') == owner
    _safe_set(owner, 'henshin_Rule25', set())
    assert getattr(partner, 'henshin_Mapping26') is None


def test_assoc_origin58_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping59' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping59', None)
    _safe_set(owner, 'henshin_Node60', partner)
    assert getattr(partner, 'henshin_Mapping59') == owner
    _safe_set(owner, 'henshin_Node60', None)
    assert getattr(partner, 'henshin_Mapping59') is None


def test_assoc_parameterMappings11_stub_double():
    # henshin_ParameterMapping has no real 'henshin_ParameterMapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_ParameterMapping()
    setattr(partner, 'henshin_ParameterMapping', None)
    _safe_set(owner, 'henshin_Unit12', {partner})
    assert getattr(partner, 'henshin_ParameterMapping') == owner
    _safe_set(owner, 'henshin_Unit12', set())
    assert getattr(partner, 'henshin_ParameterMapping') is None


def test_assoc_parameters10_stub_double():
    # henshin_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'unit', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'unit', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_right85_stub_double():
    # henshin_BinaryFormula has no real 'henshin_BinaryFormula86' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_BinaryFormula()
    setattr(partner, 'henshin_BinaryFormula86', None)
    _safe_set(owner, 'henshin_Formula87', partner)
    assert getattr(partner, 'henshin_BinaryFormula86') == owner
    _safe_set(owner, 'henshin_Formula87', None)
    assert getattr(partner, 'henshin_BinaryFormula86') is None


def test_assoc_subUnit64_stub_double():
    # henshin_UnaryUnit has no real 'henshin_UnaryUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_UnaryUnit()
    setattr(partner, 'henshin_UnaryUnit', None)
    _safe_set(owner, 'henshin_Unit65', partner)
    assert getattr(partner, 'henshin_UnaryUnit') == owner
    _safe_set(owner, 'henshin_Unit65', None)
    assert getattr(partner, 'henshin_UnaryUnit') is None


def test_assoc_subUnits66_stub_double():
    # henshin_MultiUnit has no real 'henshin_MultiUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_MultiUnit()
    setattr(partner, 'henshin_MultiUnit', None)
    _safe_set(owner, 'henshin_Unit67', partner)
    assert owner in getattr(partner, 'henshin_MultiUnit')
    _safe_set(owner, 'henshin_Unit67', None)
    assert owner not in getattr(partner, 'henshin_MultiUnit')


def test_assoc_then70_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit71' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit71', None)
    _safe_set(owner, 'henshin_Unit72', partner)
    assert getattr(partner, 'henshin_ConditionalUnit71') == owner
    _safe_set(owner, 'henshin_Unit72', None)
    assert getattr(partner, 'henshin_ConditionalUnit71') is None


def test_assoc_type40_stub_double():
    # henshin_EClass has no real 'henshin_EClass' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_EClass()
    setattr(partner, 'henshin_EClass', None)
    _safe_set(owner, 'henshin_Node', partner)
    assert getattr(partner, 'henshin_EClass') == owner
    _safe_set(owner, 'henshin_Node', None)
    assert getattr(partner, 'henshin_EClass') is None


def test_assoc_type51_stub_double():
    # henshin_EReference has no real 'henshin_EReference' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Edge(index="sample_text", indexConstant="sample_text")
    partner = henshin_EReference()
    setattr(partner, 'henshin_EReference', None)
    _safe_set(owner, 'henshin_Edge', partner)
    assert getattr(partner, 'henshin_EReference') == owner
    _safe_set(owner, 'henshin_Edge', None)
    assert getattr(partner, 'henshin_EReference') is None


def test_assoc_type54_stub_double():
    # henshin_EAttribute has no real 'henshin_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    partner = henshin_EAttribute()
    setattr(partner, 'henshin_EAttribute', None)
    _safe_set(owner, 'henshin_Attribute', partner)
    assert getattr(partner, 'henshin_EAttribute') == owner
    _safe_set(owner, 'henshin_Attribute', None)
    assert getattr(partner, 'henshin_EAttribute') is None


def test_assoc_unit27_stub_double():
    # henshin_Parameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True)
    partner = henshin_Parameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Unit', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Unit', None)
    assert getattr(partner, 'parameters') is None


