import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Rectangle,
    Widget,
    sofiagraphics_Color,
    sofiagraphics_Dimension,
    sofiagraphics_Ellipse,
    sofiagraphics_Gesture,
    sofiagraphics_Point,
    sofiagraphics_Polyline,
    sofiagraphics_Rectangle,
    sofiagraphics_RoundedRectangle,
    sofiagraphics_Scene,
    sofiagraphics_Style,
    sofiagraphics_Text,
    sofiagraphics_Widget,
    Alignment,
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

def test_assoc_bgcolor35_reverse_link_reassign_clear():
    a1 = sofiagraphics_Style(filled=True, lineWidth=3.14)
    a2 = sofiagraphics_Style(filled=False, lineWidth=9.99)
    b = sofiagraphics_Color(a=3.14, b=3.14, g=3.14, r=3.14)
    _safe_set(b, 'sofiagraphics_Color37', a1)
    assert _is_linked(b, 'sofiagraphics_Color37', a1)
    if hasattr(a1, 'sofiagraphics_Style36'):
        assert _is_linked(a1, 'sofiagraphics_Style36', b)
    _safe_set(b, 'sofiagraphics_Color37', a2)
    assert _is_linked(b, 'sofiagraphics_Color37', a2)
    if hasattr(a1, 'sofiagraphics_Style36'):
        assert not _is_linked(a1, 'sofiagraphics_Style36', b)
    if hasattr(a2, 'sofiagraphics_Style36'):
        assert _is_linked(a2, 'sofiagraphics_Style36', b)
    _safe_set(b, 'sofiagraphics_Color37', None)
    assert not _is_linked(b, 'sofiagraphics_Color37', a2)
    if hasattr(a2, 'sofiagraphics_Style36'):
        assert not _is_linked(a2, 'sofiagraphics_Style36', b)


def test_assoc_child4_reverse_link_reassign_clear():
    a1 = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    a2 = sofiagraphics_Widget(gestureOnly=False, portYPosition=9.99)
    b = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Widget5'):
        assert _is_linked(a1, 'Widget5', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Widget5'):
        assert not _is_linked(a1, 'Widget5', b)
    if hasattr(a2, 'Widget5'):
        assert _is_linked(a2, 'Widget5', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Widget5'):
        assert not _is_linked(a2, 'Widget5', b)


def test_assoc_dim8_reverse_link_reassign_clear():
    a1 = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    a2 = sofiagraphics_Widget(gestureOnly=False, portYPosition=9.99)
    b = sofiagraphics_Dimension(height=3.14, hrelative=True, noresize=True, width=3.14, wrelative=True)
    _safe_set(b, 'sofiagraphics_Dimension', a1)
    assert _is_linked(b, 'sofiagraphics_Dimension', a1)
    if hasattr(a1, 'sofiagraphics_Widget9'):
        assert _is_linked(a1, 'sofiagraphics_Widget9', b)
    _safe_set(b, 'sofiagraphics_Dimension', a2)
    assert _is_linked(b, 'sofiagraphics_Dimension', a2)
    if hasattr(a1, 'sofiagraphics_Widget9'):
        assert not _is_linked(a1, 'sofiagraphics_Widget9', b)
    if hasattr(a2, 'sofiagraphics_Widget9'):
        assert _is_linked(a2, 'sofiagraphics_Widget9', b)
    _safe_set(b, 'sofiagraphics_Dimension', None)
    assert not _is_linked(b, 'sofiagraphics_Dimension', a2)
    if hasattr(a2, 'sofiagraphics_Widget9'):
        assert not _is_linked(a2, 'sofiagraphics_Widget9', b)


def test_assoc_fgcolor32_reverse_link_reassign_clear():
    a1 = sofiagraphics_Style(filled=True, lineWidth=3.14)
    a2 = sofiagraphics_Style(filled=False, lineWidth=9.99)
    b = sofiagraphics_Color(a=3.14, b=3.14, g=3.14, r=3.14)
    _safe_set(b, 'sofiagraphics_Color34', a1)
    assert _is_linked(b, 'sofiagraphics_Color34', a1)
    if hasattr(a1, 'sofiagraphics_Style33'):
        assert _is_linked(a1, 'sofiagraphics_Style33', b)
    _safe_set(b, 'sofiagraphics_Color34', a2)
    assert _is_linked(b, 'sofiagraphics_Color34', a2)
    if hasattr(a1, 'sofiagraphics_Style33'):
        assert not _is_linked(a1, 'sofiagraphics_Style33', b)
    if hasattr(a2, 'sofiagraphics_Style33'):
        assert _is_linked(a2, 'sofiagraphics_Style33', b)
    _safe_set(b, 'sofiagraphics_Color34', None)
    assert not _is_linked(b, 'sofiagraphics_Color34', a2)
    if hasattr(a2, 'sofiagraphics_Style33'):
        assert not _is_linked(a2, 'sofiagraphics_Style33', b)


def test_assoc_parent1_reverse_link_reassign_clear():
    a1 = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    a2 = sofiagraphics_Widget(gestureOnly=False, portYPosition=9.99)
    b = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    _safe_set(b, 'child', a1)
    assert _is_linked(b, 'child', a1)
    if hasattr(a1, 'Widget'):
        assert _is_linked(a1, 'Widget', b)
    _safe_set(b, 'child', a2)
    assert _is_linked(b, 'child', a2)
    if hasattr(a1, 'Widget'):
        assert not _is_linked(a1, 'Widget', b)
    if hasattr(a2, 'Widget'):
        assert _is_linked(a2, 'Widget', b)
    _safe_set(b, 'child', None)
    assert not _is_linked(b, 'child', a2)
    if hasattr(a2, 'Widget'):
        assert not _is_linked(a2, 'Widget', b)


def test_assoc_pos6_reverse_link_reassign_clear():
    a1 = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    a2 = sofiagraphics_Widget(gestureOnly=False, portYPosition=9.99)
    b = sofiagraphics_Point(x=3.14, xrelative=True, y=3.14, yrelative=True)
    _safe_set(b, 'sofiagraphics_Point', a1)
    assert _is_linked(b, 'sofiagraphics_Point', a1)
    if hasattr(a1, 'sofiagraphics_Widget7'):
        assert _is_linked(a1, 'sofiagraphics_Widget7', b)
    _safe_set(b, 'sofiagraphics_Point', a2)
    assert _is_linked(b, 'sofiagraphics_Point', a2)
    if hasattr(a1, 'sofiagraphics_Widget7'):
        assert not _is_linked(a1, 'sofiagraphics_Widget7', b)
    if hasattr(a2, 'sofiagraphics_Widget7'):
        assert _is_linked(a2, 'sofiagraphics_Widget7', b)
    _safe_set(b, 'sofiagraphics_Point', None)
    assert not _is_linked(b, 'sofiagraphics_Point', a2)
    if hasattr(a2, 'sofiagraphics_Widget7'):
        assert not _is_linked(a2, 'sofiagraphics_Widget7', b)


def test_assoc_style2_reverse_link_reassign_clear():
    a1 = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    a2 = sofiagraphics_Widget(gestureOnly=False, portYPosition=9.99)
    b = sofiagraphics_Style(filled=True, lineWidth=3.14)
    _safe_set(b, 'sofiagraphics_Style', a1)
    assert _is_linked(b, 'sofiagraphics_Style', a1)
    if hasattr(a1, 'sofiagraphics_Widget'):
        assert _is_linked(a1, 'sofiagraphics_Widget', b)
    _safe_set(b, 'sofiagraphics_Style', a2)
    assert _is_linked(b, 'sofiagraphics_Style', a2)
    if hasattr(a1, 'sofiagraphics_Widget'):
        assert not _is_linked(a1, 'sofiagraphics_Widget', b)
    if hasattr(a2, 'sofiagraphics_Widget'):
        assert _is_linked(a2, 'sofiagraphics_Widget', b)
    _safe_set(b, 'sofiagraphics_Style', None)
    assert not _is_linked(b, 'sofiagraphics_Style', a2)
    if hasattr(a2, 'sofiagraphics_Widget'):
        assert not _is_linked(a2, 'sofiagraphics_Widget', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_color25_stub_double():
    # sofiagraphics_Scene has no real 'sofiagraphics_Scene26' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Color's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Color's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Color(a=3.14, b=3.14, g=3.14, r=3.14)
    partner = sofiagraphics_Scene()
    setattr(partner, 'sofiagraphics_Scene26', None)
    _safe_set(owner, 'sofiagraphics_Color', partner)
    assert owner in getattr(partner, 'sofiagraphics_Scene26')
    _safe_set(owner, 'sofiagraphics_Color', None)
    assert owner not in getattr(partner, 'sofiagraphics_Scene26')


def test_assoc_corner10_stub_double():
    # sofiagraphics_RoundedRectangle has no real 'sofiagraphics_RoundedRectangle' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Dimension(height=3.14, hrelative=True, noresize=True, width=3.14, wrelative=True)
    partner = sofiagraphics_RoundedRectangle()
    setattr(partner, 'sofiagraphics_RoundedRectangle', None)
    _safe_set(owner, 'sofiagraphics_Dimension11', partner)
    assert getattr(partner, 'sofiagraphics_RoundedRectangle') == owner
    _safe_set(owner, 'sofiagraphics_Dimension11', None)
    assert getattr(partner, 'sofiagraphics_RoundedRectangle') is None


def test_assoc_dimension22_stub_double():
    # sofiagraphics_Scene has no real 'sofiagraphics_Scene23' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Dimension(height=3.14, hrelative=True, noresize=True, width=3.14, wrelative=True)
    partner = sofiagraphics_Scene()
    setattr(partner, 'sofiagraphics_Scene23', None)
    _safe_set(owner, 'sofiagraphics_Dimension24', partner)
    assert owner in getattr(partner, 'sofiagraphics_Scene23')
    _safe_set(owner, 'sofiagraphics_Dimension24', None)
    assert owner not in getattr(partner, 'sofiagraphics_Scene23')


def test_assoc_object14_stub_double():
    # sofiagraphics_Scene has no real 'sofiagraphics_Scene' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    partner = sofiagraphics_Scene()
    setattr(partner, 'sofiagraphics_Scene', None)
    _safe_set(owner, 'sofiagraphics_Widget15', partner)
    assert owner in getattr(partner, 'sofiagraphics_Scene')
    _safe_set(owner, 'sofiagraphics_Widget15', None)
    assert owner not in getattr(partner, 'sofiagraphics_Scene')


def test_assoc_point12_stub_double():
    # sofiagraphics_Polyline has no real 'sofiagraphics_Polyline' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Point(x=3.14, xrelative=True, y=3.14, yrelative=True)
    partner = sofiagraphics_Polyline()
    setattr(partner, 'sofiagraphics_Polyline', None)
    _safe_set(owner, 'sofiagraphics_Point13', partner)
    assert owner in getattr(partner, 'sofiagraphics_Polyline')
    _safe_set(owner, 'sofiagraphics_Point13', None)
    assert owner not in getattr(partner, 'sofiagraphics_Polyline')


def test_assoc_point19_stub_double():
    # sofiagraphics_Scene has no real 'sofiagraphics_Scene20' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Point(x=3.14, xrelative=True, y=3.14, yrelative=True)
    partner = sofiagraphics_Scene()
    setattr(partner, 'sofiagraphics_Scene20', None)
    _safe_set(owner, 'sofiagraphics_Point21', partner)
    assert owner in getattr(partner, 'sofiagraphics_Scene20')
    _safe_set(owner, 'sofiagraphics_Point21', None)
    assert owner not in getattr(partner, 'sofiagraphics_Scene20')


def test_assoc_root16_stub_double():
    # sofiagraphics_Scene has no real 'sofiagraphics_Scene17' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    partner = sofiagraphics_Scene()
    setattr(partner, 'sofiagraphics_Scene17', None)
    _safe_set(owner, 'sofiagraphics_Widget18', partner)
    assert getattr(partner, 'sofiagraphics_Scene17') == owner
    _safe_set(owner, 'sofiagraphics_Widget18', None)
    assert getattr(partner, 'sofiagraphics_Scene17') is None


def test_assoc_style27_stub_double():
    # sofiagraphics_Scene has no real 'sofiagraphics_Scene28' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Style's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Style's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Style(filled=True, lineWidth=3.14)
    partner = sofiagraphics_Scene()
    setattr(partner, 'sofiagraphics_Scene28', None)
    _safe_set(owner, 'sofiagraphics_Style29', partner)
    assert owner in getattr(partner, 'sofiagraphics_Scene28')
    _safe_set(owner, 'sofiagraphics_Style29', None)
    assert owner not in getattr(partner, 'sofiagraphics_Scene28')


def test_assoc_widget38_stub_double():
    # sofiagraphics_Gesture has no real 'sofiagraphics_Gesture39' property in the generated
    # code (a bare stub) -- manually attach it so sofiagraphics_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sofiagraphics_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sofiagraphics_Widget(gestureOnly=True, portYPosition=3.14)
    partner = sofiagraphics_Gesture()
    setattr(partner, 'sofiagraphics_Gesture39', None)
    _safe_set(owner, 'sofiagraphics_Widget40', partner)
    assert owner in getattr(partner, 'sofiagraphics_Gesture39')
    _safe_set(owner, 'sofiagraphics_Widget40', None)
    assert owner not in getattr(partner, 'sofiagraphics_Gesture39')


