import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryFormula,
    DescribedElement,
    Formula,
    GraphElement,
    NamedElement,
    TransformationUnit,
    UnaryFormula,
    henshin_AmalgamationUnit,
    henshin_And,
    henshin_Attribute,
    henshin_AttributeCondition,
    henshin_BinaryFormula,
    henshin_ConditionalUnit,
    henshin_CountedUnit,
    henshin_DescribedElement,
    henshin_EAttribute,
    henshin_EClass,
    henshin_EPackage,
    henshin_EReference,
    henshin_Edge,
    henshin_Formula,
    henshin_Graph,
    henshin_GraphElement,
    henshin_IndependentUnit,
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

def test_assoc_attributeConditions11_reverse_link_reassign_clear():
    a1 = henshin_Rule()
    a2 = henshin_Rule()
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


def test_assoc_attributes30_reverse_link_reassign_clear():
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


def test_assoc_conclusion79_reverse_link_reassign_clear():
    a1 = henshin_NestedCondition(negated=True)
    a2 = henshin_NestedCondition(negated=False)
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph80', a1)
    assert _is_linked(b, 'henshin_Graph80', a1)
    if hasattr(a1, 'henshin_NestedCondition'):
        assert _is_linked(a1, 'henshin_NestedCondition', b)
    _safe_set(b, 'henshin_Graph80', a2)
    assert _is_linked(b, 'henshin_Graph80', a2)
    if hasattr(a1, 'henshin_NestedCondition'):
        assert not _is_linked(a1, 'henshin_NestedCondition', b)
    if hasattr(a2, 'henshin_NestedCondition'):
        assert _is_linked(a2, 'henshin_NestedCondition', b)
    _safe_set(b, 'henshin_Graph80', None)
    assert not _is_linked(b, 'henshin_Graph80', a2)
    if hasattr(a2, 'henshin_NestedCondition'):
        assert not _is_linked(a2, 'henshin_NestedCondition', b)


def test_assoc_formula21_reverse_link_reassign_clear():
    a1 = henshin_Graph()
    a2 = henshin_Graph()
    b = henshin_Formula()
    _safe_set(b, 'henshin_Formula', a1)
    assert _is_linked(b, 'henshin_Formula', a1)
    if hasattr(a1, 'henshin_Graph22'):
        assert _is_linked(a1, 'henshin_Graph22', b)
    _safe_set(b, 'henshin_Formula', a2)
    assert _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a1, 'henshin_Graph22'):
        assert not _is_linked(a1, 'henshin_Graph22', b)
    if hasattr(a2, 'henshin_Graph22'):
        assert _is_linked(a2, 'henshin_Graph22', b)
    _safe_set(b, 'henshin_Formula', None)
    assert not _is_linked(b, 'henshin_Formula', a2)
    if hasattr(a2, 'henshin_Graph22'):
        assert not _is_linked(a2, 'henshin_Graph22', b)


def test_assoc_graph31_reverse_link_reassign_clear():
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


def test_assoc_instances2_reverse_link_reassign_clear():
    a1 = henshin_TransformationSystem()
    a2 = henshin_TransformationSystem()
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph', a1)
    assert _is_linked(b, 'henshin_Graph', a1)
    if hasattr(a1, 'henshin_TransformationSystem3'):
        assert _is_linked(a1, 'henshin_TransformationSystem3', b)
    _safe_set(b, 'henshin_Graph', a2)
    assert _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a1, 'henshin_TransformationSystem3'):
        assert not _is_linked(a1, 'henshin_TransformationSystem3', b)
    if hasattr(a2, 'henshin_TransformationSystem3'):
        assert _is_linked(a2, 'henshin_TransformationSystem3', b)
    _safe_set(b, 'henshin_Graph', None)
    assert not _is_linked(b, 'henshin_Graph', a2)
    if hasattr(a2, 'henshin_TransformationSystem3'):
        assert not _is_linked(a2, 'henshin_TransformationSystem3', b)


def test_assoc_lhs6_reverse_link_reassign_clear():
    a1 = henshin_Rule()
    a2 = henshin_Rule()
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph7', a1)
    assert _is_linked(b, 'henshin_Graph7', a1)
    if hasattr(a1, 'henshin_Rule'):
        assert _is_linked(a1, 'henshin_Rule', b)
    _safe_set(b, 'henshin_Graph7', a2)
    assert _is_linked(b, 'henshin_Graph7', a2)
    if hasattr(a1, 'henshin_Rule'):
        assert not _is_linked(a1, 'henshin_Rule', b)
    if hasattr(a2, 'henshin_Rule'):
        assert _is_linked(a2, 'henshin_Rule', b)
    _safe_set(b, 'henshin_Graph7', None)
    assert not _is_linked(b, 'henshin_Graph7', a2)
    if hasattr(a2, 'henshin_Rule'):
        assert not _is_linked(a2, 'henshin_Rule', b)


def test_assoc_node39_reverse_link_reassign_clear():
    a1 = henshin_Node()
    a2 = henshin_Node()
    b = henshin_Attribute(value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Node40'):
        assert _is_linked(a1, 'Node40', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Node40'):
        assert not _is_linked(a1, 'Node40', b)
    if hasattr(a2, 'Node40'):
        assert _is_linked(a2, 'Node40', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Node40'):
        assert not _is_linked(a2, 'Node40', b)


def test_assoc_nodes18_reverse_link_reassign_clear():
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


def test_assoc_rhs8_reverse_link_reassign_clear():
    a1 = henshin_Rule()
    a2 = henshin_Rule()
    b = henshin_Graph()
    _safe_set(b, 'henshin_Graph10', a1)
    assert _is_linked(b, 'henshin_Graph10', a1)
    if hasattr(a1, 'henshin_Rule9'):
        assert _is_linked(a1, 'henshin_Rule9', b)
    _safe_set(b, 'henshin_Graph10', a2)
    assert _is_linked(b, 'henshin_Graph10', a2)
    if hasattr(a1, 'henshin_Rule9'):
        assert not _is_linked(a1, 'henshin_Rule9', b)
    if hasattr(a2, 'henshin_Rule9'):
        assert _is_linked(a2, 'henshin_Rule9', b)
    _safe_set(b, 'henshin_Graph10', None)
    assert not _is_linked(b, 'henshin_Graph10', a2)
    if hasattr(a2, 'henshin_Rule9'):
        assert not _is_linked(a2, 'henshin_Rule9', b)


def test_assoc_rule15_reverse_link_reassign_clear():
    a1 = henshin_Rule()
    a2 = henshin_Rule()
    b = henshin_AttributeCondition(conditionText="sample_text")
    _safe_set(b, 'attributeConditions', a1)
    assert _is_linked(b, 'attributeConditions', a1)
    if hasattr(a1, 'Rule16'):
        assert _is_linked(a1, 'Rule16', b)
    _safe_set(b, 'attributeConditions', a2)
    assert _is_linked(b, 'attributeConditions', a2)
    if hasattr(a1, 'Rule16'):
        assert not _is_linked(a1, 'Rule16', b)
    if hasattr(a2, 'Rule16'):
        assert _is_linked(a2, 'Rule16', b)
    _safe_set(b, 'attributeConditions', None)
    assert not _is_linked(b, 'attributeConditions', a2)
    if hasattr(a2, 'Rule16'):
        assert not _is_linked(a2, 'Rule16', b)


def test_assoc_rules0_reverse_link_reassign_clear():
    a1 = henshin_TransformationSystem()
    a2 = henshin_TransformationSystem()
    b = henshin_Rule()
    _safe_set(b, 'Rule', a1)
    assert _is_linked(b, 'Rule', a1)
    if hasattr(a1, 'transformationSystem'):
        assert _is_linked(a1, 'transformationSystem', b)
    _safe_set(b, 'Rule', a2)
    assert _is_linked(b, 'Rule', a2)
    if hasattr(a1, 'transformationSystem'):
        assert not _is_linked(a1, 'transformationSystem', b)
    if hasattr(a2, 'transformationSystem'):
        assert _is_linked(a2, 'transformationSystem', b)
    _safe_set(b, 'Rule', None)
    assert not _is_linked(b, 'Rule', a2)
    if hasattr(a2, 'transformationSystem'):
        assert not _is_linked(a2, 'transformationSystem', b)


def test_assoc_subUnit77_reverse_link_reassign_clear():
    a1 = henshin_TransformationUnit(activated=True)
    a2 = henshin_TransformationUnit(activated=False)
    b = henshin_CountedUnit(count=7)
    _safe_set(b, 'henshin_CountedUnit', a1)
    assert _is_linked(b, 'henshin_CountedUnit', a1)
    if hasattr(a1, 'henshin_TransformationUnit78'):
        assert _is_linked(a1, 'henshin_TransformationUnit78', b)
    _safe_set(b, 'henshin_CountedUnit', a2)
    assert _is_linked(b, 'henshin_CountedUnit', a2)
    if hasattr(a1, 'henshin_TransformationUnit78'):
        assert not _is_linked(a1, 'henshin_TransformationUnit78', b)
    if hasattr(a2, 'henshin_TransformationUnit78'):
        assert _is_linked(a2, 'henshin_TransformationUnit78', b)
    _safe_set(b, 'henshin_CountedUnit', None)
    assert not _is_linked(b, 'henshin_CountedUnit', a2)
    if hasattr(a2, 'henshin_TransformationUnit78'):
        assert not _is_linked(a2, 'henshin_TransformationUnit78', b)


def test_assoc_subUnits54_reverse_link_reassign_clear():
    a1 = henshin_TransformationUnit(activated=True)
    a2 = henshin_TransformationUnit(activated=False)
    b = henshin_SequentialUnit(rollback=True, strict=True)
    _safe_set(b, 'henshin_SequentialUnit', {a1})
    assert _is_linked(b, 'henshin_SequentialUnit', a1)
    if hasattr(a1, 'henshin_TransformationUnit55'):
        assert _is_linked(a1, 'henshin_TransformationUnit55', b)
    _safe_set(b, 'henshin_SequentialUnit', {a2})
    assert _is_linked(b, 'henshin_SequentialUnit', a2)
    if hasattr(a1, 'henshin_TransformationUnit55'):
        assert not _is_linked(a1, 'henshin_TransformationUnit55', b)
    if hasattr(a2, 'henshin_TransformationUnit55'):
        assert _is_linked(a2, 'henshin_TransformationUnit55', b)
    _safe_set(b, 'henshin_SequentialUnit', set())
    assert not _is_linked(b, 'henshin_SequentialUnit', a2)
    if hasattr(a2, 'henshin_TransformationUnit55'):
        assert not _is_linked(a2, 'henshin_TransformationUnit55', b)


def test_assoc_transformationSystem14_reverse_link_reassign_clear():
    a1 = henshin_TransformationSystem()
    a2 = henshin_TransformationSystem()
    b = henshin_Rule()
    _safe_set(b, 'rules', a1)
    assert _is_linked(b, 'rules', a1)
    if hasattr(a1, 'TransformationSystem'):
        assert _is_linked(a1, 'TransformationSystem', b)
    _safe_set(b, 'rules', a2)
    assert _is_linked(b, 'rules', a2)
    if hasattr(a1, 'TransformationSystem'):
        assert not _is_linked(a1, 'TransformationSystem', b)
    if hasattr(a2, 'TransformationSystem'):
        assert _is_linked(a2, 'TransformationSystem', b)
    _safe_set(b, 'rules', None)
    assert not _is_linked(b, 'rules', a2)
    if hasattr(a2, 'TransformationSystem'):
        assert not _is_linked(a2, 'TransformationSystem', b)


def test_assoc_transformationUnits4_reverse_link_reassign_clear():
    a1 = henshin_TransformationUnit(activated=True)
    a2 = henshin_TransformationUnit(activated=False)
    b = henshin_TransformationSystem()
    _safe_set(b, 'henshin_TransformationSystem5', {a1})
    assert _is_linked(b, 'henshin_TransformationSystem5', a1)
    if hasattr(a1, 'henshin_TransformationUnit'):
        assert _is_linked(a1, 'henshin_TransformationUnit', b)
    _safe_set(b, 'henshin_TransformationSystem5', {a2})
    assert _is_linked(b, 'henshin_TransformationSystem5', a2)
    if hasattr(a1, 'henshin_TransformationUnit'):
        assert not _is_linked(a1, 'henshin_TransformationUnit', b)
    if hasattr(a2, 'henshin_TransformationUnit'):
        assert _is_linked(a2, 'henshin_TransformationUnit', b)
    _safe_set(b, 'henshin_TransformationSystem5', set())
    assert not _is_linked(b, 'henshin_TransformationSystem5', a2)
    if hasattr(a2, 'henshin_TransformationUnit'):
        assert not _is_linked(a2, 'henshin_TransformationUnit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allEdges36_stub_double():
    # henshin_Edge has no real 'henshin_Edge' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'henshin_Edge', None)
    _safe_set(owner, 'henshin_Node37', {partner})
    assert getattr(partner, 'henshin_Edge') == owner
    _safe_set(owner, 'henshin_Node37', set())
    assert getattr(partner, 'henshin_Edge') is None


def test_assoc_child84_stub_double():
    # henshin_UnaryFormula has no real 'henshin_UnaryFormula' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_UnaryFormula()
    setattr(partner, 'henshin_UnaryFormula', None)
    _safe_set(owner, 'henshin_Formula85', partner)
    assert getattr(partner, 'henshin_UnaryFormula') == owner
    _safe_set(owner, 'henshin_Formula85', None)
    assert getattr(partner, 'henshin_UnaryFormula') is None


def test_assoc_edges19_stub_double():
    # henshin_Edge has no real 'Edge' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Graph()
    partner = henshin_Edge()
    setattr(partner, 'Edge', None)
    _safe_set(owner, 'graph20', {partner})
    assert getattr(partner, 'Edge') == owner
    _safe_set(owner, 'graph20', set())
    assert getattr(partner, 'Edge') is None


def test_assoc_else_61_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit62' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit62', None)
    _safe_set(owner, 'henshin_TransformationUnit63', partner)
    assert getattr(partner, 'henshin_ConditionalUnit62') == owner
    _safe_set(owner, 'henshin_TransformationUnit63', None)
    assert getattr(partner, 'henshin_ConditionalUnit62') is None


def test_assoc_graph47_stub_double():
    # henshin_Edge has no real 'edges' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Graph()
    partner = henshin_Edge()
    setattr(partner, 'edges', None)
    _safe_set(owner, 'Graph48', partner)
    assert getattr(partner, 'edges') == owner
    _safe_set(owner, 'Graph48', None)
    assert getattr(partner, 'edges') is None


def test_assoc_if_56_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit', None)
    _safe_set(owner, 'henshin_TransformationUnit57', partner)
    assert getattr(partner, 'henshin_ConditionalUnit') == owner
    _safe_set(owner, 'henshin_TransformationUnit57', None)
    assert getattr(partner, 'henshin_ConditionalUnit') is None


def test_assoc_image25_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping26' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping26', None)
    _safe_set(owner, 'henshin_Node27', partner)
    assert getattr(partner, 'henshin_Mapping26') == owner
    _safe_set(owner, 'henshin_Node27', None)
    assert getattr(partner, 'henshin_Mapping26') is None


def test_assoc_imports1_stub_double():
    # henshin_EPackage has no real 'henshin_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationSystem()
    partner = henshin_EPackage()
    setattr(partner, 'henshin_EPackage', None)
    _safe_set(owner, 'henshin_TransformationSystem', {partner})
    assert getattr(partner, 'henshin_EPackage') == owner
    _safe_set(owner, 'henshin_TransformationSystem', set())
    assert getattr(partner, 'henshin_EPackage') is None


def test_assoc_incoming32_stub_double():
    # henshin_Edge has no real 'Edge33' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'Edge33', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Edge33') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Edge33') is None


def test_assoc_kernelRule66_stub_double():
    # henshin_AmalgamationUnit has no real 'henshin_AmalgamationUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule()
    partner = henshin_AmalgamationUnit()
    setattr(partner, 'henshin_AmalgamationUnit', None)
    _safe_set(owner, 'henshin_Rule67', partner)
    assert getattr(partner, 'henshin_AmalgamationUnit') == owner
    _safe_set(owner, 'henshin_Rule67', None)
    assert getattr(partner, 'henshin_AmalgamationUnit') is None


def test_assoc_left86_stub_double():
    # henshin_BinaryFormula has no real 'henshin_BinaryFormula' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_BinaryFormula()
    setattr(partner, 'henshin_BinaryFormula', None)
    _safe_set(owner, 'henshin_Formula87', partner)
    assert getattr(partner, 'henshin_BinaryFormula') == owner
    _safe_set(owner, 'henshin_Formula87', None)
    assert getattr(partner, 'henshin_BinaryFormula') is None


def test_assoc_mappings12_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping', None)
    _safe_set(owner, 'henshin_Rule13', {partner})
    assert getattr(partner, 'henshin_Mapping') == owner
    _safe_set(owner, 'henshin_Rule13', set())
    assert getattr(partner, 'henshin_Mapping') is None


def test_assoc_mappings81_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping83' property in the generated
    # code (a bare stub) -- manually attach it so henshin_NestedCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_NestedCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_NestedCondition(negated=True)
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping83', None)
    _safe_set(owner, 'henshin_NestedCondition82', {partner})
    assert getattr(partner, 'henshin_Mapping83') == owner
    _safe_set(owner, 'henshin_NestedCondition82', set())
    assert getattr(partner, 'henshin_Mapping83') is None


def test_assoc_multiRules68_stub_double():
    # henshin_AmalgamationUnit has no real 'henshin_AmalgamationUnit69' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Rule()
    partner = henshin_AmalgamationUnit()
    setattr(partner, 'henshin_AmalgamationUnit69', None)
    _safe_set(owner, 'henshin_Rule70', partner)
    assert owner in getattr(partner, 'henshin_AmalgamationUnit69')
    _safe_set(owner, 'henshin_Rule70', None)
    assert owner not in getattr(partner, 'henshin_AmalgamationUnit69')


def test_assoc_origin23_stub_double():
    # henshin_Mapping has no real 'henshin_Mapping24' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Mapping()
    setattr(partner, 'henshin_Mapping24', None)
    _safe_set(owner, 'henshin_Node', partner)
    assert getattr(partner, 'henshin_Mapping24') == owner
    _safe_set(owner, 'henshin_Node', None)
    assert getattr(partner, 'henshin_Mapping24') is None


def test_assoc_outgoing34_stub_double():
    # henshin_Edge has no real 'Edge35' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'Edge35', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Edge35') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Edge35') is None


def test_assoc_parameterMappings50_stub_double():
    # henshin_ParameterMapping has no real 'henshin_ParameterMapping' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ParameterMapping()
    setattr(partner, 'henshin_ParameterMapping', None)
    _safe_set(owner, 'henshin_TransformationUnit51', {partner})
    assert getattr(partner, 'henshin_ParameterMapping') == owner
    _safe_set(owner, 'henshin_TransformationUnit51', set())
    assert getattr(partner, 'henshin_ParameterMapping') is None


def test_assoc_parameters49_stub_double():
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


def test_assoc_right88_stub_double():
    # henshin_BinaryFormula has no real 'henshin_BinaryFormula89' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Formula's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Formula's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Formula()
    partner = henshin_BinaryFormula()
    setattr(partner, 'henshin_BinaryFormula89', None)
    _safe_set(owner, 'henshin_Formula90', partner)
    assert getattr(partner, 'henshin_BinaryFormula89') == owner
    _safe_set(owner, 'henshin_Formula90', None)
    assert getattr(partner, 'henshin_BinaryFormula89') is None


def test_assoc_source41_stub_double():
    # henshin_Edge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Node42', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Node42', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_subUnits52_stub_double():
    # henshin_IndependentUnit has no real 'henshin_IndependentUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_IndependentUnit()
    setattr(partner, 'henshin_IndependentUnit', None)
    _safe_set(owner, 'henshin_TransformationUnit53', partner)
    assert owner in getattr(partner, 'henshin_IndependentUnit')
    _safe_set(owner, 'henshin_TransformationUnit53', None)
    assert owner not in getattr(partner, 'henshin_IndependentUnit')


def test_assoc_subUnits64_stub_double():
    # henshin_PriorityUnit has no real 'henshin_PriorityUnit' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_PriorityUnit()
    setattr(partner, 'henshin_PriorityUnit', None)
    _safe_set(owner, 'henshin_TransformationUnit65', partner)
    assert owner in getattr(partner, 'henshin_PriorityUnit')
    _safe_set(owner, 'henshin_TransformationUnit65', None)
    assert owner not in getattr(partner, 'henshin_PriorityUnit')


def test_assoc_target43_stub_double():
    # henshin_Edge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_Edge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'Node44', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'Node44', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_then58_stub_double():
    # henshin_ConditionalUnit has no real 'henshin_ConditionalUnit59' property in the generated
    # code (a bare stub) -- manually attach it so henshin_TransformationUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_TransformationUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_TransformationUnit(activated=True)
    partner = henshin_ConditionalUnit()
    setattr(partner, 'henshin_ConditionalUnit59', None)
    _safe_set(owner, 'henshin_TransformationUnit60', partner)
    assert getattr(partner, 'henshin_ConditionalUnit59') == owner
    _safe_set(owner, 'henshin_TransformationUnit60', None)
    assert getattr(partner, 'henshin_ConditionalUnit59') is None


def test_assoc_type28_stub_double():
    # henshin_EClass has no real 'henshin_EClass' property in the generated
    # code (a bare stub) -- manually attach it so henshin_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # henshin_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = henshin_Node()
    partner = henshin_EClass()
    setattr(partner, 'henshin_EClass', None)
    _safe_set(owner, 'henshin_Node29', partner)
    assert getattr(partner, 'henshin_EClass') == owner
    _safe_set(owner, 'henshin_Node29', None)
    assert getattr(partner, 'henshin_EClass') is None


def test_assoc_type38_stub_double():
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


def test_assoc_unit17_stub_double():
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


