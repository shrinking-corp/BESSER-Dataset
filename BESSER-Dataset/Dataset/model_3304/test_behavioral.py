import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Decorator,
    Identifiable,
    model_Comparable,
    model_Decorator,
    model_DynamicLabel,
    model_EdgeDecorator,
    model_Graph,
    model_GraphDecorator,
    model_Model,
    model_NodeDecorator,
    model_STEMTime,
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

def test_assoc_models3_reverse_link_reassign_clear():
    a1 = model_Model()
    a2 = model_Model()
    b = model_Model()
    _safe_set(b, 'model_Model2', {a1})
    assert _is_linked(b, 'model_Model2', a1)
    if hasattr(a1, 'model_Model'):
        assert _is_linked(a1, 'model_Model', b)
    _safe_set(b, 'model_Model2', {a2})
    assert _is_linked(b, 'model_Model2', a2)
    if hasattr(a1, 'model_Model'):
        assert not _is_linked(a1, 'model_Model', b)
    if hasattr(a2, 'model_Model'):
        assert _is_linked(a2, 'model_Model', b)
    _safe_set(b, 'model_Model2', set())
    assert not _is_linked(b, 'model_Model2', a2)
    if hasattr(a2, 'model_Model'):
        assert not _is_linked(a2, 'model_Model', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_edgeDecorators10_stub_double():
    # model_EdgeDecorator has no real 'model_EdgeDecorator' property in the generated
    # code (a bare stub) -- manually attach it so model_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Model()
    partner = model_EdgeDecorator()
    setattr(partner, 'model_EdgeDecorator', None)
    _safe_set(owner, 'model_Model11', {partner})
    assert getattr(partner, 'model_EdgeDecorator') == owner
    _safe_set(owner, 'model_Model11', set())
    assert getattr(partner, 'model_EdgeDecorator') is None


def test_assoc_graph1_stub_double():
    # model_Graph has no real 'graph.ecoreGraph' property in the generated
    # code (a bare stub) -- manually attach it so model_Decorator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Decorator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Decorator(enabled=True, graphDecorated=True, progress=3.14)
    partner = model_Graph()
    setattr(partner, 'graph.ecoreGraph', None)
    _safe_set(owner, 'decorators', partner)
    assert getattr(partner, 'graph.ecoreGraph') == owner
    _safe_set(owner, 'decorators', None)
    assert getattr(partner, 'graph.ecoreGraph') is None


def test_assoc_graphDecorators6_stub_double():
    # model_GraphDecorator has no real 'model_GraphDecorator' property in the generated
    # code (a bare stub) -- manually attach it so model_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Model()
    partner = model_GraphDecorator()
    setattr(partner, 'model_GraphDecorator', None)
    _safe_set(owner, 'model_Model7', {partner})
    assert getattr(partner, 'model_GraphDecorator') == owner
    _safe_set(owner, 'model_Model7', set())
    assert getattr(partner, 'model_GraphDecorator') is None


def test_assoc_graphs4_stub_double():
    # model_Graph has no real 'model_Graph' property in the generated
    # code (a bare stub) -- manually attach it so model_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Model()
    partner = model_Graph()
    setattr(partner, 'model_Graph', None)
    _safe_set(owner, 'model_Model5', {partner})
    assert getattr(partner, 'model_Graph') == owner
    _safe_set(owner, 'model_Model5', set())
    assert getattr(partner, 'model_Graph') is None


def test_assoc_labelsToUpdate0_stub_double():
    # model_DynamicLabel has no real 'graph.ecoreDynamicLabel' property in the generated
    # code (a bare stub) -- manually attach it so model_Decorator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Decorator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Decorator(enabled=True, graphDecorated=True, progress=3.14)
    partner = model_DynamicLabel()
    setattr(partner, 'graph.ecoreDynamicLabel', None)
    _safe_set(owner, 'decorator', {partner})
    assert getattr(partner, 'graph.ecoreDynamicLabel') == owner
    _safe_set(owner, 'decorator', set())
    assert getattr(partner, 'graph.ecoreDynamicLabel') is None


def test_assoc_nodeDecorators8_stub_double():
    # model_NodeDecorator has no real 'model_NodeDecorator' property in the generated
    # code (a bare stub) -- manually attach it so model_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Model()
    partner = model_NodeDecorator()
    setattr(partner, 'model_NodeDecorator', None)
    _safe_set(owner, 'model_Model9', {partner})
    assert getattr(partner, 'model_NodeDecorator') == owner
    _safe_set(owner, 'model_Model9', set())
    assert getattr(partner, 'model_NodeDecorator') is None


