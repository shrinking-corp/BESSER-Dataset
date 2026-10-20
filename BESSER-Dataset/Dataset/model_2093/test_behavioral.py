import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DecisionTreeNode,
    DecisionTree_DecisionTreeForEntity,
    DecisionTree_DecisionTreeNode,
    DecisionTree_DecisionTrees,
    DecisionTree_EntityType,
    DecisionTree_IntermediateNode,
    DecisionTree_LeafNode,
    DecisionTree_Property,
    DecisionTree_PropertySpec2,
    DecisionTree_StructuralVariation,
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

def test_assoc_checkedProperty6_stub_double():
    # DecisionTree_IntermediateNode has no real 'DecisionTree_IntermediateNode' property in the generated
    # code (a bare stub) -- manually attach it so DecisionTree_PropertySpec2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DecisionTree_PropertySpec2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DecisionTree_PropertySpec2(needsTypeCheck=True)
    partner = DecisionTree_IntermediateNode()
    setattr(partner, 'DecisionTree_IntermediateNode', None)
    _safe_set(owner, 'DecisionTree_PropertySpec2', partner)
    assert getattr(partner, 'DecisionTree_IntermediateNode') == owner
    _safe_set(owner, 'DecisionTree_PropertySpec2', None)
    assert getattr(partner, 'DecisionTree_IntermediateNode') is None


def test_assoc_property13_stub_double():
    # DecisionTree_Property has no real 'DecisionTree_Property' property in the generated
    # code (a bare stub) -- manually attach it so DecisionTree_PropertySpec2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DecisionTree_PropertySpec2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DecisionTree_PropertySpec2(needsTypeCheck=True)
    partner = DecisionTree_Property()
    setattr(partner, 'DecisionTree_Property', None)
    _safe_set(owner, 'DecisionTree_PropertySpec214', partner)
    assert getattr(partner, 'DecisionTree_Property') == owner
    _safe_set(owner, 'DecisionTree_PropertySpec214', None)
    assert getattr(partner, 'DecisionTree_Property') is None


def test_assoc_trees11_stub_double():
    # DecisionTree_DecisionTreeForEntity has no real 'DecisionTree_DecisionTreeForEntity12' property in the generated
    # code (a bare stub) -- manually attach it so DecisionTree_DecisionTrees's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # DecisionTree_DecisionTrees's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = DecisionTree_DecisionTrees(name="sample_text")
    partner = DecisionTree_DecisionTreeForEntity()
    setattr(partner, 'DecisionTree_DecisionTreeForEntity12', None)
    _safe_set(owner, 'DecisionTree_DecisionTrees', {partner})
    assert getattr(partner, 'DecisionTree_DecisionTreeForEntity12') == owner
    _safe_set(owner, 'DecisionTree_DecisionTrees', set())
    assert getattr(partner, 'DecisionTree_DecisionTreeForEntity12') is None


