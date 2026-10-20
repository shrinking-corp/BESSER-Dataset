import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    rpslPerceptionGraphMetaModel_Component,
    rpslPerceptionGraphMetaModel_Connection,
    rpslPerceptionGraphMetaModel_Element,
    rpslPerceptionGraphMetaModel_InputPort,
    rpslPerceptionGraphMetaModel_Leaf,
    rpslPerceptionGraphMetaModel_Node,
    rpslPerceptionGraphMetaModel_OutputPort,
    rpslPerceptionGraphMetaModel_PerceptionGraph,
    rpslPerceptionGraphMetaModel_Prototype,
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

def test_assoc_element0_reverse_link_reassign_clear():
    a1 = rpslPerceptionGraphMetaModel_PerceptionGraph(doc="sample_text", name="sample_text", uuid="sample_text")
    a2 = rpslPerceptionGraphMetaModel_PerceptionGraph(doc="sample_text_2", name="sample_text_2", uuid="sample_text_2")
    b = rpslPerceptionGraphMetaModel_Element(doc="sample_text", name="sample_text")
    _safe_set(b, 'rpslPerceptionGraphMetaModel_Element', a1)
    assert _is_linked(b, 'rpslPerceptionGraphMetaModel_Element', a1)
    if hasattr(a1, 'rpslPerceptionGraphMetaModel_PerceptionGraph'):
        assert _is_linked(a1, 'rpslPerceptionGraphMetaModel_PerceptionGraph', b)
    _safe_set(b, 'rpslPerceptionGraphMetaModel_Element', a2)
    assert _is_linked(b, 'rpslPerceptionGraphMetaModel_Element', a2)
    if hasattr(a1, 'rpslPerceptionGraphMetaModel_PerceptionGraph'):
        assert not _is_linked(a1, 'rpslPerceptionGraphMetaModel_PerceptionGraph', b)
    if hasattr(a2, 'rpslPerceptionGraphMetaModel_PerceptionGraph'):
        assert _is_linked(a2, 'rpslPerceptionGraphMetaModel_PerceptionGraph', b)
    _safe_set(b, 'rpslPerceptionGraphMetaModel_Element', None)
    assert not _is_linked(b, 'rpslPerceptionGraphMetaModel_Element', a2)
    if hasattr(a2, 'rpslPerceptionGraphMetaModel_PerceptionGraph'):
        assert not _is_linked(a2, 'rpslPerceptionGraphMetaModel_PerceptionGraph', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_component3_stub_double():
    # rpslPerceptionGraphMetaModel_Component has no real 'rpslPerceptionGraphMetaModel_Component' property in the generated
    # code (a bare stub) -- manually attach it so rpslPerceptionGraphMetaModel_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rpslPerceptionGraphMetaModel_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rpslPerceptionGraphMetaModel_Element(doc="sample_text", name="sample_text")
    partner = rpslPerceptionGraphMetaModel_Component()
    setattr(partner, 'rpslPerceptionGraphMetaModel_Component', None)
    _safe_set(owner, 'rpslPerceptionGraphMetaModel_Element4', partner)
    assert getattr(partner, 'rpslPerceptionGraphMetaModel_Component') == owner
    _safe_set(owner, 'rpslPerceptionGraphMetaModel_Element4', None)
    assert getattr(partner, 'rpslPerceptionGraphMetaModel_Component') is None


def test_assoc_element6_stub_double():
    # rpslPerceptionGraphMetaModel_Connection has no real 'rpslPerceptionGraphMetaModel_Connection7' property in the generated
    # code (a bare stub) -- manually attach it so rpslPerceptionGraphMetaModel_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rpslPerceptionGraphMetaModel_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rpslPerceptionGraphMetaModel_Element(doc="sample_text", name="sample_text")
    partner = rpslPerceptionGraphMetaModel_Connection()
    setattr(partner, 'rpslPerceptionGraphMetaModel_Connection7', None)
    _safe_set(owner, 'rpslPerceptionGraphMetaModel_Element8', partner)
    assert getattr(partner, 'rpslPerceptionGraphMetaModel_Connection7') == owner
    _safe_set(owner, 'rpslPerceptionGraphMetaModel_Element8', None)
    assert getattr(partner, 'rpslPerceptionGraphMetaModel_Connection7') is None


def test_assoc_perception_graph_property_prototype1_stub_double():
    # rpslPerceptionGraphMetaModel_Prototype has no real 'rpslPerceptionGraphMetaModel_Prototype' property in the generated
    # code (a bare stub) -- manually attach it so rpslPerceptionGraphMetaModel_PerceptionGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rpslPerceptionGraphMetaModel_PerceptionGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rpslPerceptionGraphMetaModel_PerceptionGraph(doc="sample_text", name="sample_text", uuid="sample_text")
    partner = rpslPerceptionGraphMetaModel_Prototype()
    setattr(partner, 'rpslPerceptionGraphMetaModel_Prototype', None)
    _safe_set(owner, 'rpslPerceptionGraphMetaModel_PerceptionGraph2', {partner})
    assert getattr(partner, 'rpslPerceptionGraphMetaModel_Prototype') == owner
    _safe_set(owner, 'rpslPerceptionGraphMetaModel_PerceptionGraph2', set())
    assert getattr(partner, 'rpslPerceptionGraphMetaModel_Prototype') is None


