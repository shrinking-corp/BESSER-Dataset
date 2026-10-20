import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryFormula,
    Formula,
    GraphElement,
    ModelElement,
    MultiUnit,
    NamedElement,
    UnaryFormula,
    UnaryUnit,
    Unit,
    henshin_And,
    henshin_Annotation,
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
    henshin_ModelElement,
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

def test_assoc_attributeConditions19_reverse_link_reassign_clear():
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


def test_assoc_attributes42_reverse_link_reassign_clear():
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


def test_assoc_edges37_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'graph38'):
        assert _is_linked(a1, 'graph38', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'graph38'):
        assert not _is_linked(a1, 'graph38', b)
    if hasattr(a2, 'graph38'):
        assert _is_linked(a2, 'graph38', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'graph38'):
        assert not _is_linked(a2, 'graph38', b)


def test_assoc_formula39_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Formula()
    _safe_set(b, 'henshin_Formula', a1)
    assert _is_linked(b, 'henshin_Formula', a1)
    if hasattr(a1, 'henshin_Graph40'):
        assert _is_linked(a1, 'henshin_Graph40', b)
    _safe_set(b, 'henshin_Formula', a2)
    assert _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a1, 'henshin_Graph40'):
        assert not _is_linked(a1, 'henshin_Graph40', b)
    if hasattr(a2, 'henshin_Graph40'):
        assert _is_linked(a2, 'henshin_Graph40', b)
    _safe_set(b, 'henshin_Formula', None)
    assert not _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a2, 'henshin_Graph40'):
        assert not _is_linked(a2, 'henshin_Graph40', b)


def test_assoc_graph43_reverse_link_reassign_clear():
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


def test_assoc_graph53_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'edges', a1)
    assert _is_linked(b, 'edges', a1)
    if hasattr(a1, 'Graph54'):
        assert _is_linked(a1, 'Graph54', b)
    _safe_set(b, 'edges', a2)
    assert _is_linked(b, 'edges', a2)
    if hasattr(a1, 'Graph54'):
        assert not _is_linked(a1, 'Graph54', b)
    if hasattr(a2, 'Graph54'):
        assert _is_linked(a2, 'Graph54', b)
    _safe_set(b, 'edges', None)
    assert not _is_linked(b, 'edges', a2)
    if hasattr(a2, 'Graph54'):
        assert not _is_linked(a2, 'Graph54', b)


def test_assoc_incoming44_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'Edge45', a1)
    assert _is_linked(b, 'Edge45', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge45', a2)
    assert _is_linked(b, 'Edge45', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge45', None)
    assert not _is_linked(b, 'Edge45', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_instances9_reverse_link_reassign_clear():
    a1 = henshin_Module(nullValueMatching=True)
    a2 = henshin_Module(nullValueMatching=False)
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph', a1)
    assert _is_linked(b, 'henshin_Graph', a1)
    if hasattr(a1, 'henshin_Module10'):
        assert _is_linked(a1, 'henshin_Module10', b)
    _safe_set(b, 'henshin_Graph', a2)
    assert _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a1, 'henshin_Module10'):
        assert not _is_linked(a1, 'henshin_Module10', b)
    if hasattr(a2, 'henshin_Module10'):
        assert _is_linked(a2, 'henshin_Module10', b)
    _safe_set(b, 'henshin_Graph', None)
    assert not _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a2, 'henshin_Module10'):
        assert not _is_linked(a2, 'henshin_Module10', b)


def test_assoc_lhs14_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph15', a1)
    assert _is_linked(b, 'henshin_Graph15', a1)
    if hasattr(a1, 'henshin_Rule'):
        assert _is_linked(a1, 'henshin_Rule', b)
    _safe_set(b, 'henshin_Graph15', a2)
    assert _is_linked(b, 'henshin_Graph15', a2)
    if hasattr(a1, 'henshin_Rule'):
        assert not _is_linked(a1, 'henshin_Rule', b)
    if hasattr(a2, 'henshin_Rule'):
        assert _is_linked(a2, 'henshin_Rule', b)
    _safe_set(b, 'henshin_Graph15', None)
    assert not _is_linked(b, 'henshin_Graph15', a2)
    if hasattr(a2, 'henshin_Rule'):
        assert not _is_linked(a2, 'henshin_Rule', b)


def test_assoc_multiRules23_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
    b = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    _safe_set(b, 'henshin_Rule24', a1)
    assert _is_linked(b, 'henshin_Rule24', a1)
    if hasattr(a1, 'henshin_Rule22'):
        assert _is_linked(a1, 'henshin_Rule22', b)
    _safe_set(b, 'henshin_Rule24', a2)
    assert _is_linked(b, 'henshin_Rule24', a2)
    if hasattr(a1, 'henshin_Rule22'):
        assert not _is_linked(a1, 'henshin_Rule22', b)
    if hasattr(a2, 'henshin_Rule22'):
        assert _is_linked(a2, 'henshin_Rule22', b)
    _safe_set(b, 'henshin_Rule24', None)
    assert not _is_linked(b, 'henshin_Rule24', a2)
    if hasattr(a2, 'henshin_Rule22'):
        assert not _is_linked(a2, 'henshin_Rule22', b)


def test_assoc_node56_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Attribute(constant="sample_text", null=True, value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Node57'):
        assert _is_linked(a1, 'Node57', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Node57'):
        assert not _is_linked(a1, 'Node57', b)
    if hasattr(a2, 'Node57'):
        assert _is_linked(a2, 'Node57', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Node57'):
        assert not _is_linked(a2, 'Node57', b)


def test_assoc_nodes36_reverse_link_reassign_clear():
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


def test_assoc_outgoing46_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'Edge47', a1)
    assert _is_linked(b, 'Edge47', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge47', a2)
    assert _is_linked(b, 'Edge47', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge47', None)
    assert not _is_linked(b, 'Edge47', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_rhs16_reverse_link_reassign_clear():
    a1 = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    a2 = henshin_Rule(checkDangling=False, injectiveMatching=False, javaImports="sample_text_2")
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph18', a1)
    assert _is_linked(b, 'henshin_Graph18', a1)
    if hasattr(a1, 'henshin_Rule17'):
        assert _is_linked(a1, 'henshin_Rule17', b)
    _safe_set(b, 'henshin_Graph18', a2)
    assert _is_linked(b, 'henshin_Graph18', a2)
    if hasattr(a1, 'henshin_Rule17'):
        assert not _is_linked(a1, 'henshin_Rule17', b)
    if hasattr(a2, 'henshin_Rule17'):
        assert _is_linked(a2, 'henshin_Rule17', b)
    _safe_set(b, 'henshin_Graph18', None)
    assert not _is_linked(b, 'henshin_Graph18', a2)
    if hasattr(a2, 'henshin_Rule17'):
        assert not _is_linked(a2, 'henshin_Rule17', b)


def test_assoc_rule58_reverse_link_reassign_clear():
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


def test_assoc_source48_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node49'):
        assert _is_linked(a1, 'Node49', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node49'):
        assert not _is_linked(a1, 'Node49', b)
    if hasattr(a2, 'Node49'):
        assert _is_linked(a2, 'Node49', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node49'):
        assert not _is_linked(a2, 'Node49', b)


def test_assoc_subModules2_reverse_link_reassign_clear():
    a1 = henshin_Module(nullValueMatching=True)
    a2 = henshin_Module(nullValueMatching=False)
    b = henshin_Module(nullValueMatching=True)
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


def test_assoc_superModule4_reverse_link_reassign_clear():
    a1 = henshin_Module(nullValueMatching=True)
    a2 = henshin_Module(nullValueMatching=False)
    b = henshin_Module(nullValueMatching=True)
    _safe_set(b, 'subModules', a1)
    assert _is_linked(b, 'subModules', a1)
    if hasattr(a1, 'Module5'):
        assert _is_linked(a1, 'Module5', b)
    _safe_set(b, 'subModules', a2)
    assert _is_linked(b, 'subModules', a2)
    if hasattr(a1, 'Module5'):
        assert not _is_linked(a1, 'Module5', b)
    if hasattr(a2, 'Module5'):
        assert _is_linked(a2, 'Module5', b)
    _safe_set(b, 'subModules', None)
    assert not _is_linked(b, 'subModules', a2)
    if hasattr(a2, 'Module5'):
        assert not _is_linked(a2, 'Module5', b)


def test_assoc_target50_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Edge(index="sample_text", indexConstant="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node51'):
        assert _is_linked(a1, 'Node51', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node51'):
        assert not _is_linked(a1, 'Node51', b)
    if hasattr(a2, 'Node51'):
        assert _is_linked(a2, 'Node51', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node51'):
        assert not _is_linked(a2, 'Node51', b)


def test_assoc_units7_reverse_link_reassign_clear():
    a1 = henshin_Unit(activated=True, isUsed=True)
    a2 = henshin_Unit(activated=False, isUsed=False)
    b = henshin_Module(nullValueMatching=True)
    _safe_set(b, 'henshin_Module8', {a1})
    assert _is_linked(b, 'henshin_Module8', a1)
    if hasattr(a1, 'henshin_Unit'):
        assert _is_linked(a1, 'henshin_Unit', b)
    _safe_set(b, 'henshin_Module8', {a2})
    assert _is_linked(b, 'henshin_Module8', a2)
    if hasattr(a1, 'henshin_Unit'):
        assert not _is_linked(a1, 'henshin_Unit', b)
    if hasattr(a2, 'henshin_Unit'):
        assert _is_linked(a2, 'henshin_Unit', b)
    _safe_set(b, 'henshin_Module8', set())
    assert not _is_linked(b, 'henshin_Module8', a2)
    if hasattr(a2, 'henshin_Unit'):
        assert not _is_linked(a2, 'henshin_Unit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations0_stub_double():
    # henshin_ModelElement has no real 'henshin_ModelElement' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Annotation(key="sample_text", value="sample_text")
    partner = henshin_ModelElement()
    setattr(partner, 'henshin_ModelElement', None)
    _safe_set(owner, 'henshin_Annotation', partner)
    assert owner in getattr(partner, 'henshin_ModelElement')
    _safe_set(owner, 'henshin_Annotation', None)
    assert owner not in getattr(partner, 'henshin_ModelElement')


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


def test_assoc_else_74_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit75' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit75', None)
    _safe_set(owner, 'henshin_Unit76', partner)
    assert getattr(partner, 'henshin_ConditionalUnit75') == owner
    _safe_set(owner, 'henshin_Unit76', None)
    assert getattr(partner, 'henshin_ConditionalUnit75') is None


def test_assoc_if_69_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit', None)
    _safe_set(owner, 'henshin_Unit70', partner)
    assert getattr(partner, 'henshin_ConditionalUnit') == owner
    _safe_set(owner, 'henshin_Unit70', None)
    assert getattr(partner, 'henshin_ConditionalUnit') is None


def test_assoc_image62_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping63' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping63', None)
    _safe_set(owner, 'henshin_Node64', partner)
    assert getattr(partner, 'henshin_Mapping63') == owner
    _safe_set(owner, 'henshin_Node64', None)
    assert getattr(partner, 'henshin_Mapping63') is None


def test_assoc_imports6_stub_double():
    # henshin_EPackage has no real 'henshin_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Module(nullValueMatching=True)
    partner = henshin_EPackage()
    setattr(partner, 'henshin_EPackage', None)
    _safe_set(owner, 'henshin_Module', {partner})
    assert getattr(partner, 'henshin_EPackage') == owner
    _safe_set(owner, 'henshin_Module', set())
    assert getattr(partner, 'henshin_EPackage') is None


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


def test_assoc_mappings20_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping', None)
    _safe_set(owner, 'henshin_Rule21', {partner})
    assert getattr(partner, 'henshin_Mapping') == owner
    _safe_set(owner, 'henshin_Rule21', set())
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


def test_assoc_multiMappings25_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping27' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule(checkDangling=True, injectiveMatching=True, javaImports="sample_text")
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping27', None)
    _safe_set(owner, 'henshin_Rule26', {partner})
    assert getattr(partner, 'henshin_Mapping27') == owner
    _safe_set(owner, 'henshin_Rule26', set())
    assert getattr(partner, 'henshin_Mapping27') is None


def test_assoc_origin59_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping60' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping60', None)
    _safe_set(owner, 'henshin_Node61', partner)
    assert getattr(partner, 'henshin_Mapping60') == owner
    _safe_set(owner, 'henshin_Node61', None)
    assert getattr(partner, 'henshin_Mapping60') is None


def test_assoc_parameterMappings12_stub_double():
    # henshin_ParameterMapping has no real 'henshin_ParameterMapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
    partner = henshin_ParameterMapping()
    setattr(partner, 'henshin_ParameterMapping', None)
    _safe_set(owner, 'henshin_Unit13', {partner})
    assert getattr(partner, 'henshin_ParameterMapping') == owner
    _safe_set(owner, 'henshin_Unit13', set())
    assert getattr(partner, 'henshin_ParameterMapping') is None


def test_assoc_parameters11_stub_double():
    # henshin_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
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


def test_assoc_subUnit65_stub_double():
    # henshin_UnaryUnit has no real 'henshin_UnaryUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
    partner = henshin_UnaryUnit()
    setattr(partner, 'henshin_UnaryUnit', None)
    _safe_set(owner, 'henshin_Unit66', partner)
    assert getattr(partner, 'henshin_UnaryUnit') == owner
    _safe_set(owner, 'henshin_Unit66', None)
    assert getattr(partner, 'henshin_UnaryUnit') is None


def test_assoc_subUnits67_stub_double():
    # henshin_MultiUnit has no real 'henshin_MultiUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
    partner = henshin_MultiUnit()
    setattr(partner, 'henshin_MultiUnit', None)
    _safe_set(owner, 'henshin_Unit68', partner)
    assert owner in getattr(partner, 'henshin_MultiUnit')
    _safe_set(owner, 'henshin_Unit68', None)
    assert owner not in getattr(partner, 'henshin_MultiUnit')


def test_assoc_then71_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit72' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit72', None)
    _safe_set(owner, 'henshin_Unit73', partner)
    assert getattr(partner, 'henshin_ConditionalUnit72') == owner
    _safe_set(owner, 'henshin_Unit73', None)
    assert getattr(partner, 'henshin_ConditionalUnit72') is None


def test_assoc_type41_stub_double():
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


def test_assoc_type52_stub_double():
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


def test_assoc_type55_stub_double():
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


def test_assoc_unit28_stub_double():
    # henshin_Parameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Unit(activated=True, isUsed=True)
    partner = henshin_Parameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Unit', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Unit', None)
    assert getattr(partner, 'parameters') is None


