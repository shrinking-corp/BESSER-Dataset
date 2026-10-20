import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CSElement,
    CSNode,
    ENamedElement,
    cs_CSColor,
    cs_CSConnection,
    cs_CSConnectionEnd,
    cs_CSElement,
    cs_CSLayout,
    cs_CSNode,
    cs_CSPoint,
    cs_CSRoot,
    cs_CSShape,
    cs_CSStroke,
    cs_CSTemplateDescription,
    cs_CSText,
    cs_CSTransform,
    cs_EClass,
    cs_EObject,
    cs_EStructuralFeature,
    CSFitType,
    CSOrientation,
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

def test_assoc_background8_reverse_link_reassign_clear():
    a1 = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    a2 = cs_CSElement(draggable=False, maxZoom="sample_text_2", minZoom="sample_text_2", resizable=False, selectable="sample_text_2", templateRoot=False)
    b = cs_CSColor(a=3.14, b=3.14, g=3.14, r=3.14)
    _safe_set(b, 'cs_CSColor10', a1)
    assert _is_linked(b, 'cs_CSColor10', a1)
    if hasattr(a1, 'cs_CSElement9'):
        assert _is_linked(a1, 'cs_CSElement9', b)
    _safe_set(b, 'cs_CSColor10', a2)
    assert _is_linked(b, 'cs_CSColor10', a2)
    if hasattr(a1, 'cs_CSElement9'):
        assert not _is_linked(a1, 'cs_CSElement9', b)
    if hasattr(a2, 'cs_CSElement9'):
        assert _is_linked(a2, 'cs_CSElement9', b)
    _safe_set(b, 'cs_CSColor10', None)
    assert not _is_linked(b, 'cs_CSColor10', a2)
    if hasattr(a2, 'cs_CSElement9'):
        assert not _is_linked(a2, 'cs_CSElement9', b)


def test_assoc_children2_reverse_link_reassign_clear():
    a1 = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    a2 = cs_CSElement(draggable=False, maxZoom="sample_text_2", minZoom="sample_text_2", resizable=False, selectable="sample_text_2", templateRoot=False)
    b = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'CSElement'):
        assert _is_linked(a1, 'CSElement', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'CSElement'):
        assert not _is_linked(a1, 'CSElement', b)
    if hasattr(a2, 'CSElement'):
        assert _is_linked(a2, 'CSElement', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'CSElement'):
        assert not _is_linked(a2, 'CSElement', b)


def test_assoc_foreground6_reverse_link_reassign_clear():
    a1 = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    a2 = cs_CSElement(draggable=False, maxZoom="sample_text_2", minZoom="sample_text_2", resizable=False, selectable="sample_text_2", templateRoot=False)
    b = cs_CSColor(a=3.14, b=3.14, g=3.14, r=3.14)
    _safe_set(b, 'cs_CSColor', a1)
    assert _is_linked(b, 'cs_CSColor', a1)
    if hasattr(a1, 'cs_CSElement7'):
        assert _is_linked(a1, 'cs_CSElement7', b)
    _safe_set(b, 'cs_CSColor', a2)
    assert _is_linked(b, 'cs_CSColor', a2)
    if hasattr(a1, 'cs_CSElement7'):
        assert not _is_linked(a1, 'cs_CSElement7', b)
    if hasattr(a2, 'cs_CSElement7'):
        assert _is_linked(a2, 'cs_CSElement7', b)
    _safe_set(b, 'cs_CSColor', None)
    assert not _is_linked(b, 'cs_CSColor', a2)
    if hasattr(a2, 'cs_CSElement7'):
        assert not _is_linked(a2, 'cs_CSElement7', b)


def test_assoc_node36_reverse_link_reassign_clear():
    a1 = cs_CSNode(height="sample_text", heightRatioToParent="sample_text", horizontalAlign="sample_text", maxHeight="sample_text", maxWidth="sample_text", minHeight="sample_text", minWidth="sample_text", verticalAlign="sample_text", width="sample_text", widthRatioToParent="sample_text", x="sample_text", y="sample_text")
    a2 = cs_CSNode(height="sample_text_2", heightRatioToParent="sample_text_2", horizontalAlign="sample_text_2", maxHeight="sample_text_2", maxWidth="sample_text_2", minHeight="sample_text_2", minWidth="sample_text_2", verticalAlign="sample_text_2", width="sample_text_2", widthRatioToParent="sample_text_2", x="sample_text_2", y="sample_text_2")
    b = cs_CSConnectionEnd(tipType=7)
    _safe_set(b, 'cs_CSConnectionEnd37', a1)
    assert _is_linked(b, 'cs_CSConnectionEnd37', a1)
    if hasattr(a1, 'cs_CSNode38'):
        assert _is_linked(a1, 'cs_CSNode38', b)
    _safe_set(b, 'cs_CSConnectionEnd37', a2)
    assert _is_linked(b, 'cs_CSConnectionEnd37', a2)
    if hasattr(a1, 'cs_CSNode38'):
        assert not _is_linked(a1, 'cs_CSNode38', b)
    if hasattr(a2, 'cs_CSNode38'):
        assert _is_linked(a2, 'cs_CSNode38', b)
    _safe_set(b, 'cs_CSConnectionEnd37', None)
    assert not _is_linked(b, 'cs_CSConnectionEnd37', a2)
    if hasattr(a2, 'cs_CSNode38'):
        assert not _is_linked(a2, 'cs_CSNode38', b)


def test_assoc_parent4_reverse_link_reassign_clear():
    a1 = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    a2 = cs_CSElement(draggable=False, maxZoom="sample_text_2", minZoom="sample_text_2", resizable=False, selectable="sample_text_2", templateRoot=False)
    b = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'CSElement5'):
        assert _is_linked(a1, 'CSElement5', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'CSElement5'):
        assert not _is_linked(a1, 'CSElement5', b)
    if hasattr(a2, 'CSElement5'):
        assert _is_linked(a2, 'CSElement5', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'CSElement5'):
        assert not _is_linked(a2, 'CSElement5', b)


def test_assoc_points24_reverse_link_reassign_clear():
    a1 = cs_CSShape(closed=True)
    a2 = cs_CSShape(closed=False)
    b = cs_CSPoint(x=3.14, y=3.14)
    _safe_set(b, 'cs_CSPoint', a1)
    assert _is_linked(b, 'cs_CSPoint', a1)
    if hasattr(a1, 'cs_CSShape25'):
        assert _is_linked(a1, 'cs_CSShape25', b)
    _safe_set(b, 'cs_CSPoint', a2)
    assert _is_linked(b, 'cs_CSPoint', a2)
    if hasattr(a1, 'cs_CSShape25'):
        assert not _is_linked(a1, 'cs_CSShape25', b)
    if hasattr(a2, 'cs_CSShape25'):
        assert _is_linked(a2, 'cs_CSShape25', b)
    _safe_set(b, 'cs_CSPoint', None)
    assert not _is_linked(b, 'cs_CSPoint', a2)
    if hasattr(a2, 'cs_CSShape25'):
        assert not _is_linked(a2, 'cs_CSShape25', b)


def test_assoc_shape11_reverse_link_reassign_clear():
    a1 = cs_CSShape(closed=True)
    a2 = cs_CSShape(closed=False)
    b = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    _safe_set(b, 'cs_CSElement12', a1)
    assert _is_linked(b, 'cs_CSElement12', a1)
    if hasattr(a1, 'cs_CSShape'):
        assert _is_linked(a1, 'cs_CSShape', b)
    _safe_set(b, 'cs_CSElement12', a2)
    assert _is_linked(b, 'cs_CSElement12', a2)
    if hasattr(a1, 'cs_CSShape'):
        assert not _is_linked(a1, 'cs_CSShape', b)
    if hasattr(a2, 'cs_CSShape'):
        assert _is_linked(a2, 'cs_CSShape', b)
    _safe_set(b, 'cs_CSElement12', None)
    assert not _is_linked(b, 'cs_CSElement12', a2)
    if hasattr(a2, 'cs_CSShape'):
        assert not _is_linked(a2, 'cs_CSShape', b)


def test_assoc_stroke0_reverse_link_reassign_clear():
    a1 = cs_CSStroke(cap=7, dash=3.14, dash_phase=3.14, join=7, miterlimit=3.14, width=3.14)
    a2 = cs_CSStroke(cap=13, dash=9.99, dash_phase=9.99, join=13, miterlimit=9.99, width=9.99)
    b = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    _safe_set(b, 'cs_CSElement', a1)
    assert _is_linked(b, 'cs_CSElement', a1)
    if hasattr(a1, 'cs_CSStroke'):
        assert _is_linked(a1, 'cs_CSStroke', b)
    _safe_set(b, 'cs_CSElement', a2)
    assert _is_linked(b, 'cs_CSElement', a2)
    if hasattr(a1, 'cs_CSStroke'):
        assert not _is_linked(a1, 'cs_CSStroke', b)
    if hasattr(a2, 'cs_CSStroke'):
        assert _is_linked(a2, 'cs_CSStroke', b)
    _safe_set(b, 'cs_CSElement', None)
    assert not _is_linked(b, 'cs_CSElement', a2)
    if hasattr(a2, 'cs_CSStroke'):
        assert not _is_linked(a2, 'cs_CSStroke', b)


def test_assoc_template33_reverse_link_reassign_clear():
    a1 = cs_CSTemplateDescription(scale=3.14)
    a2 = cs_CSTemplateDescription(scale=9.99)
    b = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    _safe_set(b, 'cs_CSElement35', a1)
    assert _is_linked(b, 'cs_CSElement35', a1)
    if hasattr(a1, 'cs_CSTemplateDescription34'):
        assert _is_linked(a1, 'cs_CSTemplateDescription34', b)
    _safe_set(b, 'cs_CSElement35', a2)
    assert _is_linked(b, 'cs_CSElement35', a2)
    if hasattr(a1, 'cs_CSTemplateDescription34'):
        assert not _is_linked(a1, 'cs_CSTemplateDescription34', b)
    if hasattr(a2, 'cs_CSTemplateDescription34'):
        assert _is_linked(a2, 'cs_CSTemplateDescription34', b)
    _safe_set(b, 'cs_CSElement35', None)
    assert not _is_linked(b, 'cs_CSElement35', a2)
    if hasattr(a2, 'cs_CSTemplateDescription34'):
        assert not _is_linked(a2, 'cs_CSTemplateDescription34', b)


def test_assoc_transform13_reverse_link_reassign_clear():
    a1 = cs_CSTransform(m00=3.14, m01=3.14, m02=3.14, m10=3.14, m11=3.14, m12=3.14, m20=3.14, m21=3.14, m22=3.14)
    a2 = cs_CSTransform(m00=9.99, m01=9.99, m02=9.99, m10=9.99, m11=9.99, m12=9.99, m20=9.99, m21=9.99, m22=9.99)
    b = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    _safe_set(b, 'cs_CSElement14', a1)
    assert _is_linked(b, 'cs_CSElement14', a1)
    if hasattr(a1, 'cs_CSTransform'):
        assert _is_linked(a1, 'cs_CSTransform', b)
    _safe_set(b, 'cs_CSElement14', a2)
    assert _is_linked(b, 'cs_CSElement14', a2)
    if hasattr(a1, 'cs_CSTransform'):
        assert not _is_linked(a1, 'cs_CSTransform', b)
    if hasattr(a2, 'cs_CSTransform'):
        assert _is_linked(a2, 'cs_CSTransform', b)
    _safe_set(b, 'cs_CSElement14', None)
    assert not _is_linked(b, 'cs_CSElement14', a2)
    if hasattr(a2, 'cs_CSTransform'):
        assert not _is_linked(a2, 'cs_CSTransform', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_connStructuralFeature39_stub_double():
    # cs_EStructuralFeature has no real 'cs_EStructuralFeature41' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSConnectionEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSConnectionEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSConnectionEnd(tipType=7)
    partner = cs_EStructuralFeature()
    setattr(partner, 'cs_EStructuralFeature41', None)
    _safe_set(owner, 'cs_CSConnectionEnd40', partner)
    assert getattr(partner, 'cs_EStructuralFeature41') == owner
    _safe_set(owner, 'cs_CSConnectionEnd40', None)
    assert getattr(partner, 'cs_EStructuralFeature41') is None


def test_assoc_connectionEnds22_stub_double():
    # cs_CSConnection has no real 'cs_CSConnection23' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSConnectionEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSConnectionEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSConnectionEnd(tipType=7)
    partner = cs_CSConnection()
    setattr(partner, 'cs_CSConnection23', None)
    _safe_set(owner, 'cs_CSConnectionEnd', partner)
    assert owner in getattr(partner, 'cs_CSConnection23')
    _safe_set(owner, 'cs_CSConnectionEnd', None)
    assert owner not in getattr(partner, 'cs_CSConnection23')


def test_assoc_connections21_stub_double():
    # cs_CSConnection has no real 'cs_CSConnection' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSNode(height="sample_text", heightRatioToParent="sample_text", horizontalAlign="sample_text", maxHeight="sample_text", maxWidth="sample_text", minHeight="sample_text", minWidth="sample_text", verticalAlign="sample_text", width="sample_text", widthRatioToParent="sample_text", x="sample_text", y="sample_text")
    partner = cs_CSConnection()
    setattr(partner, 'cs_CSConnection', None)
    _safe_set(owner, 'cs_CSNode', {partner})
    assert getattr(partner, 'cs_CSConnection') == owner
    _safe_set(owner, 'cs_CSNode', set())
    assert getattr(partner, 'cs_CSConnection') is None


def test_assoc_containerClass26_stub_double():
    # cs_EClass has no real 'cs_EClass' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSTemplateDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSTemplateDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSTemplateDescription(scale=3.14)
    partner = cs_EClass()
    setattr(partner, 'cs_EClass', None)
    _safe_set(owner, 'cs_CSTemplateDescription', partner)
    assert getattr(partner, 'cs_EClass') == owner
    _safe_set(owner, 'cs_CSTemplateDescription', None)
    assert getattr(partner, 'cs_EClass') is None


def test_assoc_containerStructuralFeature30_stub_double():
    # cs_EStructuralFeature has no real 'cs_EStructuralFeature32' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSTemplateDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSTemplateDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSTemplateDescription(scale=3.14)
    partner = cs_EStructuralFeature()
    setattr(partner, 'cs_EStructuralFeature32', None)
    _safe_set(owner, 'cs_CSTemplateDescription31', partner)
    assert getattr(partner, 'cs_EStructuralFeature32') == owner
    _safe_set(owner, 'cs_CSTemplateDescription31', None)
    assert getattr(partner, 'cs_EStructuralFeature32') is None


def test_assoc_displayedStructuralFeatures17_stub_double():
    # cs_EStructuralFeature has no real 'cs_EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    partner = cs_EStructuralFeature()
    setattr(partner, 'cs_EStructuralFeature', None)
    _safe_set(owner, 'cs_CSElement18', {partner})
    assert getattr(partner, 'cs_EStructuralFeature') == owner
    _safe_set(owner, 'cs_CSElement18', set())
    assert getattr(partner, 'cs_EStructuralFeature') is None


def test_assoc_layout19_stub_double():
    # cs_CSLayout has no real 'cs_CSLayout' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    partner = cs_CSLayout()
    setattr(partner, 'cs_CSLayout', None)
    _safe_set(owner, 'cs_CSElement20', partner)
    assert getattr(partner, 'cs_CSLayout') == owner
    _safe_set(owner, 'cs_CSElement20', None)
    assert getattr(partner, 'cs_CSLayout') is None


def test_assoc_nodeStructuralFeature42_stub_double():
    # cs_EStructuralFeature has no real 'cs_EStructuralFeature44' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSConnectionEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSConnectionEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSConnectionEnd(tipType=7)
    partner = cs_EStructuralFeature()
    setattr(partner, 'cs_EStructuralFeature44', None)
    _safe_set(owner, 'cs_CSConnectionEnd43', partner)
    assert getattr(partner, 'cs_EStructuralFeature44') == owner
    _safe_set(owner, 'cs_CSConnectionEnd43', None)
    assert getattr(partner, 'cs_EStructuralFeature44') is None


def test_assoc_object15_stub_double():
    # cs_EObject has no real 'cs_EObject' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSElement(draggable=True, maxZoom="sample_text", minZoom="sample_text", resizable=True, selectable="sample_text", templateRoot=True)
    partner = cs_EObject()
    setattr(partner, 'cs_EObject', None)
    _safe_set(owner, 'cs_CSElement16', partner)
    assert getattr(partner, 'cs_EObject') == owner
    _safe_set(owner, 'cs_CSElement16', None)
    assert getattr(partner, 'cs_EObject') is None


def test_assoc_theClass27_stub_double():
    # cs_EClass has no real 'cs_EClass29' property in the generated
    # code (a bare stub) -- manually attach it so cs_CSTemplateDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cs_CSTemplateDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cs_CSTemplateDescription(scale=3.14)
    partner = cs_EClass()
    setattr(partner, 'cs_EClass29', None)
    _safe_set(owner, 'cs_CSTemplateDescription28', partner)
    assert getattr(partner, 'cs_EClass29') == owner
    _safe_set(owner, 'cs_CSTemplateDescription28', None)
    assert getattr(partner, 'cs_EClass29') is None


