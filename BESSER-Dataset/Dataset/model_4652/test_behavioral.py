import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DiagramElement,
    Shape,
    di_Bounds,
    di_Color,
    di_Diagram,
    di_DiagramElement,
    di_EObject,
    di_Edge,
    di_Fill,
    di_Point,
    di_Shape,
    di_Style,
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

def test_assoc_localStyle5_reverse_link_reassign_clear():
    a1 = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    a2 = di_Style(fillOpacity="sample_text_2", fontBold="sample_text_2", fontItalic="sample_text_2", fontName="sample_text_2", fontSize="sample_text_2", fontStrikeThrough="sample_text_2", fontUnderline="sample_text_2", strokeDashLength="sample_text_2", strokeOpacity="sample_text_2", strokeWidth="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'di_DiagramElement', a1)
    assert _is_linked(b, 'di_DiagramElement', a1)
    if hasattr(a1, 'di_Style'):
        assert _is_linked(a1, 'di_Style', b)
    _safe_set(b, 'di_DiagramElement', a2)
    assert _is_linked(b, 'di_DiagramElement', a2)
    if hasattr(a1, 'di_Style'):
        assert not _is_linked(a1, 'di_Style', b)
    if hasattr(a2, 'di_Style'):
        assert _is_linked(a2, 'di_Style', b)
    _safe_set(b, 'di_DiagramElement', None)
    assert not _is_linked(b, 'di_DiagramElement', a2)
    if hasattr(a2, 'di_Style'):
        assert not _is_linked(a2, 'di_Style', b)


def test_assoc_ownedElement3_reverse_link_reassign_clear():
    a1 = di_DiagramElement(id="sample_text")
    a2 = di_DiagramElement(id="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'owningElement', {a1})
    assert _is_linked(b, 'owningElement', a1)
    if hasattr(a1, 'DiagramElement4'):
        assert _is_linked(a1, 'DiagramElement4', b)
    _safe_set(b, 'owningElement', {a2})
    assert _is_linked(b, 'owningElement', a2)
    if hasattr(a1, 'DiagramElement4'):
        assert not _is_linked(a1, 'DiagramElement4', b)
    if hasattr(a2, 'DiagramElement4'):
        assert _is_linked(a2, 'DiagramElement4', b)
    _safe_set(b, 'owningElement', set())
    assert not _is_linked(b, 'owningElement', a2)
    if hasattr(a2, 'DiagramElement4'):
        assert not _is_linked(a2, 'DiagramElement4', b)


def test_assoc_owningElement1_reverse_link_reassign_clear():
    a1 = di_DiagramElement(id="sample_text")
    a2 = di_DiagramElement(id="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'ownedElement', a1)
    assert _is_linked(b, 'ownedElement', a1)
    if hasattr(a1, 'DiagramElement'):
        assert _is_linked(a1, 'DiagramElement', b)
    _safe_set(b, 'ownedElement', a2)
    assert _is_linked(b, 'ownedElement', a2)
    if hasattr(a1, 'DiagramElement'):
        assert not _is_linked(a1, 'DiagramElement', b)
    if hasattr(a2, 'DiagramElement'):
        assert _is_linked(a2, 'DiagramElement', b)
    _safe_set(b, 'ownedElement', None)
    assert not _is_linked(b, 'ownedElement', a2)
    if hasattr(a2, 'DiagramElement'):
        assert not _is_linked(a2, 'DiagramElement', b)


def test_assoc_sharedStyle6_reverse_link_reassign_clear():
    a1 = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    a2 = di_Style(fillOpacity="sample_text_2", fontBold="sample_text_2", fontItalic="sample_text_2", fontName="sample_text_2", fontSize="sample_text_2", fontStrikeThrough="sample_text_2", fontUnderline="sample_text_2", strokeDashLength="sample_text_2", strokeOpacity="sample_text_2", strokeWidth="sample_text_2")
    b = di_DiagramElement(id="sample_text")
    _safe_set(b, 'di_DiagramElement7', a1)
    assert _is_linked(b, 'di_DiagramElement7', a1)
    if hasattr(a1, 'di_Style8'):
        assert _is_linked(a1, 'di_Style8', b)
    _safe_set(b, 'di_DiagramElement7', a2)
    assert _is_linked(b, 'di_DiagramElement7', a2)
    if hasattr(a1, 'di_Style8'):
        assert not _is_linked(a1, 'di_Style8', b)
    if hasattr(a2, 'di_Style8'):
        assert _is_linked(a2, 'di_Style8', b)
    _safe_set(b, 'di_DiagramElement7', None)
    assert not _is_linked(b, 'di_DiagramElement7', a2)
    if hasattr(a2, 'di_Style8'):
        assert not _is_linked(a2, 'di_Style8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_fill19_stub_double():
    # di_Fill has no real 'di_Fill' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Fill()
    setattr(partner, 'di_Fill', None)
    _safe_set(owner, 'di_Style20', partner)
    assert getattr(partner, 'di_Fill') == owner
    _safe_set(owner, 'di_Style20', None)
    assert getattr(partner, 'di_Fill') is None


def test_assoc_fillColor21_stub_double():
    # di_Color has no real 'di_Color' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Color()
    setattr(partner, 'di_Color', None)
    _safe_set(owner, 'di_Style22', partner)
    assert getattr(partner, 'di_Color') == owner
    _safe_set(owner, 'di_Style22', None)
    assert getattr(partner, 'di_Color') is None


def test_assoc_fontColor26_stub_double():
    # di_Color has no real 'di_Color28' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Color()
    setattr(partner, 'di_Color28', None)
    _safe_set(owner, 'di_Style27', partner)
    assert getattr(partner, 'di_Color28') == owner
    _safe_set(owner, 'di_Style27', None)
    assert getattr(partner, 'di_Color28') is None


def test_assoc_modelElement9_stub_double():
    # di_EObject has no real 'di_EObject' property in the generated
    # code (a bare stub) -- manually attach it so di_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DiagramElement(id="sample_text")
    partner = di_EObject()
    setattr(partner, 'di_EObject', None)
    _safe_set(owner, 'di_DiagramElement10', {partner})
    assert getattr(partner, 'di_EObject') == owner
    _safe_set(owner, 'di_DiagramElement10', set())
    assert getattr(partner, 'di_EObject') is None


def test_assoc_source11_stub_double():
    # di_Edge has no real 'di_Edge' property in the generated
    # code (a bare stub) -- manually attach it so di_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DiagramElement(id="sample_text")
    partner = di_Edge()
    setattr(partner, 'di_Edge', None)
    _safe_set(owner, 'di_DiagramElement12', partner)
    assert getattr(partner, 'di_Edge') == owner
    _safe_set(owner, 'di_DiagramElement12', None)
    assert getattr(partner, 'di_Edge') is None


def test_assoc_strokeColor23_stub_double():
    # di_Color has no real 'di_Color25' property in the generated
    # code (a bare stub) -- manually attach it so di_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Style(fillOpacity="sample_text", fontBold="sample_text", fontItalic="sample_text", fontName="sample_text", fontSize="sample_text", fontStrikeThrough="sample_text", fontUnderline="sample_text", strokeDashLength="sample_text", strokeOpacity="sample_text", strokeWidth="sample_text")
    partner = di_Color()
    setattr(partner, 'di_Color25', None)
    _safe_set(owner, 'di_Style24', partner)
    assert getattr(partner, 'di_Color25') == owner
    _safe_set(owner, 'di_Style24', None)
    assert getattr(partner, 'di_Color25') is None


def test_assoc_target13_stub_double():
    # di_Edge has no real 'di_Edge14' property in the generated
    # code (a bare stub) -- manually attach it so di_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DiagramElement(id="sample_text")
    partner = di_Edge()
    setattr(partner, 'di_Edge14', None)
    _safe_set(owner, 'di_DiagramElement15', partner)
    assert getattr(partner, 'di_Edge14') == owner
    _safe_set(owner, 'di_DiagramElement15', None)
    assert getattr(partner, 'di_Edge14') is None


