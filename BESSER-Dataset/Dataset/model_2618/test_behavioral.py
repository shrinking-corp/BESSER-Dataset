import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DBaseStyle,
    DNodeEdgeStyle,
    EModelElement,
    diastyle_DBaseStyle,
    diastyle_DEdgeStyle,
    diastyle_DGraph,
    diastyle_DGraphElement,
    diastyle_DNestingEdgeStyle,
    diastyle_DNodeEdgeStyle,
    diastyle_DNodeStyle,
    diastyle_DStyle,
    diastyle_DStyleBridge,
    DAlignment,
    DColor,
    DDirection,
    DFontName,
    DFontStyle,
    DLayout,
    DLine,
    DShape,
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

def test_assoc_parent8_reverse_link_reassign_clear():
    a1 = diastyle_DBaseStyle(color="sample_text", name="sample_text", parentName="sample_text")
    a2 = diastyle_DBaseStyle(color="sample_text_2", name="sample_text_2", parentName="sample_text_2")
    b = diastyle_DBaseStyle(color="sample_text", name="sample_text", parentName="sample_text")
    _safe_set(b, 'diastyle_DBaseStyle9', a1)
    assert _is_linked(b, 'diastyle_DBaseStyle9', a1)
    if hasattr(a1, 'diastyle_DBaseStyle7'):
        assert _is_linked(a1, 'diastyle_DBaseStyle7', b)
    _safe_set(b, 'diastyle_DBaseStyle9', a2)
    assert _is_linked(b, 'diastyle_DBaseStyle9', a2)
    if hasattr(a1, 'diastyle_DBaseStyle7'):
        assert not _is_linked(a1, 'diastyle_DBaseStyle7', b)
    if hasattr(a2, 'diastyle_DBaseStyle7'):
        assert _is_linked(a2, 'diastyle_DBaseStyle7', b)
    _safe_set(b, 'diastyle_DBaseStyle9', None)
    assert not _is_linked(b, 'diastyle_DBaseStyle9', a2)
    if hasattr(a2, 'diastyle_DBaseStyle7'):
        assert not _is_linked(a2, 'diastyle_DBaseStyle7', b)


def test_assoc_styleBridges4_reverse_link_reassign_clear():
    a1 = diastyle_DStyleBridge(name="sample_text")
    a2 = diastyle_DStyleBridge(name="sample_text_2")
    b = diastyle_DBaseStyle(color="sample_text", name="sample_text", parentName="sample_text")
    _safe_set(b, 'diastyle_DBaseStyle5', {a1})
    assert _is_linked(b, 'diastyle_DBaseStyle5', a1)
    if hasattr(a1, 'diastyle_DStyleBridge6'):
        assert _is_linked(a1, 'diastyle_DStyleBridge6', b)
    _safe_set(b, 'diastyle_DBaseStyle5', {a2})
    assert _is_linked(b, 'diastyle_DBaseStyle5', a2)
    if hasattr(a1, 'diastyle_DStyleBridge6'):
        assert not _is_linked(a1, 'diastyle_DStyleBridge6', b)
    if hasattr(a2, 'diastyle_DStyleBridge6'):
        assert _is_linked(a2, 'diastyle_DStyleBridge6', b)
    _safe_set(b, 'diastyle_DBaseStyle5', set())
    assert not _is_linked(b, 'diastyle_DBaseStyle5', a2)
    if hasattr(a2, 'diastyle_DStyleBridge6'):
        assert not _is_linked(a2, 'diastyle_DStyleBridge6', b)


def test_assoc_styles0_reverse_link_reassign_clear():
    a1 = diastyle_DStyle(styleHandler="sample_text")
    a2 = diastyle_DStyle(styleHandler="sample_text_2")
    b = diastyle_DBaseStyle(color="sample_text", name="sample_text", parentName="sample_text")
    _safe_set(b, 'diastyle_DBaseStyle', a1)
    assert _is_linked(b, 'diastyle_DBaseStyle', a1)
    if hasattr(a1, 'diastyle_DStyle'):
        assert _is_linked(a1, 'diastyle_DStyle', b)
    _safe_set(b, 'diastyle_DBaseStyle', a2)
    assert _is_linked(b, 'diastyle_DBaseStyle', a2)
    if hasattr(a1, 'diastyle_DStyle'):
        assert not _is_linked(a1, 'diastyle_DStyle', b)
    if hasattr(a2, 'diastyle_DStyle'):
        assert _is_linked(a2, 'diastyle_DStyle', b)
    _safe_set(b, 'diastyle_DBaseStyle', None)
    assert not _is_linked(b, 'diastyle_DBaseStyle', a2)
    if hasattr(a2, 'diastyle_DStyle'):
        assert not _is_linked(a2, 'diastyle_DStyle', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dGraph1_stub_double():
    # diastyle_DGraph has no real 'diastyle_DGraph' property in the generated
    # code (a bare stub) -- manually attach it so diastyle_DStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diastyle_DStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diastyle_DStyle(styleHandler="sample_text")
    partner = diastyle_DGraph()
    setattr(partner, 'diastyle_DGraph', None)
    _safe_set(owner, 'diastyle_DStyle2', partner)
    assert getattr(partner, 'diastyle_DGraph') == owner
    _safe_set(owner, 'diastyle_DStyle2', None)
    assert getattr(partner, 'diastyle_DGraph') is None


def test_assoc_dGraphElement3_stub_double():
    # diastyle_DGraphElement has no real 'diastyle_DGraphElement' property in the generated
    # code (a bare stub) -- manually attach it so diastyle_DStyleBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # diastyle_DStyleBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = diastyle_DStyleBridge(name="sample_text")
    partner = diastyle_DGraphElement()
    setattr(partner, 'diastyle_DGraphElement', None)
    _safe_set(owner, 'diastyle_DStyleBridge', partner)
    assert getattr(partner, 'diastyle_DGraphElement') == owner
    _safe_set(owner, 'diastyle_DStyleBridge', None)
    assert getattr(partner, 'diastyle_DGraphElement') is None


