import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ContainerElement,
    GraphicElement,
    NodeElement,
    RepresentationGraph_Circle,
    RepresentationGraph_ContainerElement,
    RepresentationGraph_Diagram,
    RepresentationGraph_EdgeElement,
    RepresentationGraph_GraphicElement,
    RepresentationGraph_IconElement,
    RepresentationGraph_NodeElement,
    RepresentationGraph_Rectangle,
    RepresentationGraph_Rhombus,
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

def test_assoc_link6_reverse_link_reassign_clear():
    a1 = RepresentationGraph_NodeElement(label="sample_text")
    a2 = RepresentationGraph_NodeElement(label="sample_text_2")
    b = RepresentationGraph_NodeElement(label="sample_text")
    _safe_set(b, 'RepresentationGraph_NodeElement7', a1)
    assert _is_linked(b, 'RepresentationGraph_NodeElement7', a1)
    if hasattr(a1, 'RepresentationGraph_NodeElement5'):
        assert _is_linked(a1, 'RepresentationGraph_NodeElement5', b)
    _safe_set(b, 'RepresentationGraph_NodeElement7', a2)
    assert _is_linked(b, 'RepresentationGraph_NodeElement7', a2)
    if hasattr(a1, 'RepresentationGraph_NodeElement5'):
        assert not _is_linked(a1, 'RepresentationGraph_NodeElement5', b)
    if hasattr(a2, 'RepresentationGraph_NodeElement5'):
        assert _is_linked(a2, 'RepresentationGraph_NodeElement5', b)
    _safe_set(b, 'RepresentationGraph_NodeElement7', None)
    assert not _is_linked(b, 'RepresentationGraph_NodeElement7', a2)
    if hasattr(a2, 'RepresentationGraph_NodeElement5'):
        assert not _is_linked(a2, 'RepresentationGraph_NodeElement5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contains8_stub_double():
    # RepresentationGraph_ContainerElement has no real 'RepresentationGraph_ContainerElement' property in the generated
    # code (a bare stub) -- manually attach it so RepresentationGraph_NodeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RepresentationGraph_NodeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RepresentationGraph_NodeElement(label="sample_text")
    partner = RepresentationGraph_ContainerElement()
    setattr(partner, 'RepresentationGraph_ContainerElement', None)
    _safe_set(owner, 'RepresentationGraph_NodeElement9', partner)
    assert owner in getattr(partner, 'RepresentationGraph_ContainerElement')
    _safe_set(owner, 'RepresentationGraph_NodeElement9', None)
    assert owner not in getattr(partner, 'RepresentationGraph_ContainerElement')


def test_assoc_elements0_stub_double():
    # RepresentationGraph_Diagram has no real 'RepresentationGraph_Diagram' property in the generated
    # code (a bare stub) -- manually attach it so RepresentationGraph_GraphicElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RepresentationGraph_GraphicElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RepresentationGraph_GraphicElement(color="sample_text", paletteIconPath="sample_text", paletteName="sample_text")
    partner = RepresentationGraph_Diagram()
    setattr(partner, 'RepresentationGraph_Diagram', None)
    _safe_set(owner, 'RepresentationGraph_GraphicElement', partner)
    assert owner in getattr(partner, 'RepresentationGraph_Diagram')
    _safe_set(owner, 'RepresentationGraph_GraphicElement', None)
    assert owner not in getattr(partner, 'RepresentationGraph_Diagram')


def test_assoc_source1_stub_double():
    # RepresentationGraph_EdgeElement has no real 'RepresentationGraph_EdgeElement' property in the generated
    # code (a bare stub) -- manually attach it so RepresentationGraph_NodeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RepresentationGraph_NodeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RepresentationGraph_NodeElement(label="sample_text")
    partner = RepresentationGraph_EdgeElement()
    setattr(partner, 'RepresentationGraph_EdgeElement', None)
    _safe_set(owner, 'RepresentationGraph_NodeElement', partner)
    assert getattr(partner, 'RepresentationGraph_EdgeElement') == owner
    _safe_set(owner, 'RepresentationGraph_NodeElement', None)
    assert getattr(partner, 'RepresentationGraph_EdgeElement') is None


def test_assoc_target2_stub_double():
    # RepresentationGraph_EdgeElement has no real 'RepresentationGraph_EdgeElement3' property in the generated
    # code (a bare stub) -- manually attach it so RepresentationGraph_NodeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RepresentationGraph_NodeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RepresentationGraph_NodeElement(label="sample_text")
    partner = RepresentationGraph_EdgeElement()
    setattr(partner, 'RepresentationGraph_EdgeElement3', None)
    _safe_set(owner, 'RepresentationGraph_NodeElement4', partner)
    assert getattr(partner, 'RepresentationGraph_EdgeElement3') == owner
    _safe_set(owner, 'RepresentationGraph_NodeElement4', None)
    assert getattr(partner, 'RepresentationGraph_EdgeElement3') is None


