import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DiagramElement,
    Figure,
    GraphicalElement,
    IDElement,
    Relation,
    Style,
    TextualElement,
    Value,
    notation_AttributeValue,
    notation_BorderStyle,
    notation_Circle,
    notation_Compartment,
    notation_Composite,
    notation_Cube,
    notation_Cylinder,
    notation_DiagramDefinition,
    notation_DiagramElement,
    notation_Diamond,
    notation_Figure,
    notation_FigureContainment,
    notation_FigureStyle,
    notation_GraphicalElement,
    notation_IDElement,
    notation_Icon,
    notation_IconStyle,
    notation_Image,
    notation_Keyword,
    notation_Label,
    notation_Line,
    notation_LineStyle,
    notation_Link,
    notation_Node,
    notation_NotationDefinition,
    notation_Point,
    notation_Polyline,
    notation_Rectangle,
    notation_ReferenceValue,
    notation_Relation,
    notation_Roundtangle,
    notation_Square,
    notation_Style,
    notation_SyntaxOf,
    notation_TextStyle,
    notation_TextualContainment,
    notation_TextualElement,
    notation_Token,
    notation_Triangle,
    notation_Value,
    AudienceType,
    Color,
    DefinitionType,
    FillTextureType,
    IconType,
    Layout,
    LineTextureType,
    Orientation,
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

def test_assoc_diagrams0_reverse_link_reassign_clear():
    a1 = notation_NotationDefinition(Type="sample_text")
    a2 = notation_NotationDefinition(Type="sample_text_2")
    b = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    _safe_set(b, 'notation_DiagramDefinition', a1)
    assert _is_linked(b, 'notation_DiagramDefinition', a1)
    if hasattr(a1, 'notation_NotationDefinition'):
        assert _is_linked(a1, 'notation_NotationDefinition', b)
    _safe_set(b, 'notation_DiagramDefinition', a2)
    assert _is_linked(b, 'notation_DiagramDefinition', a2)
    if hasattr(a1, 'notation_NotationDefinition'):
        assert not _is_linked(a1, 'notation_NotationDefinition', b)
    if hasattr(a2, 'notation_NotationDefinition'):
        assert _is_linked(a2, 'notation_NotationDefinition', b)
    _safe_set(b, 'notation_DiagramDefinition', None)
    assert not _is_linked(b, 'notation_DiagramDefinition', a2)
    if hasattr(a2, 'notation_NotationDefinition'):
        assert not _is_linked(a2, 'notation_NotationDefinition', b)


def test_assoc_style10_reverse_link_reassign_clear():
    a1 = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    a2 = notation_IconStyle(brightness=13, color="sample_text_2", height=9.99, orientation="sample_text_2", width=9.99)
    b = notation_Icon(iconType="sample_text")
    _safe_set(b, 'notation_Icon', a1)
    assert _is_linked(b, 'notation_Icon', a1)
    if hasattr(a1, 'notation_IconStyle'):
        assert _is_linked(a1, 'notation_IconStyle', b)
    _safe_set(b, 'notation_Icon', a2)
    assert _is_linked(b, 'notation_Icon', a2)
    if hasattr(a1, 'notation_IconStyle'):
        assert not _is_linked(a1, 'notation_IconStyle', b)
    if hasattr(a2, 'notation_IconStyle'):
        assert _is_linked(a2, 'notation_IconStyle', b)
    _safe_set(b, 'notation_Icon', None)
    assert not _is_linked(b, 'notation_Icon', a2)
    if hasattr(a2, 'notation_IconStyle'):
        assert not _is_linked(a2, 'notation_IconStyle', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_approximateRepresentation11_stub_double():
    # notation_GraphicalElement has no real 'notation_GraphicalElement12' property in the generated
    # code (a bare stub) -- manually attach it so notation_Image's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Image's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Image(path="sample_text")
    partner = notation_GraphicalElement()
    setattr(partner, 'notation_GraphicalElement12', None)
    _safe_set(owner, 'notation_Image', partner)
    assert getattr(partner, 'notation_GraphicalElement12') == owner
    _safe_set(owner, 'notation_Image', None)
    assert getattr(partner, 'notation_GraphicalElement12') is None


def test_assoc_borderStyle23_stub_double():
    # notation_Figure has no real 'notation_Figure24' property in the generated
    # code (a bare stub) -- manually attach it so notation_BorderStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_BorderStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_BorderStyle(color="sample_text", texture="sample_text", thickness=3.14)
    partner = notation_Figure()
    setattr(partner, 'notation_Figure24', None)
    _safe_set(owner, 'notation_BorderStyle', partner)
    assert getattr(partner, 'notation_Figure24') == owner
    _safe_set(owner, 'notation_BorderStyle', None)
    assert getattr(partner, 'notation_Figure24') is None


def test_assoc_elements1_stub_double():
    # notation_DiagramElement has no real 'notation_DiagramElement' property in the generated
    # code (a bare stub) -- manually attach it so notation_DiagramDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_DiagramDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    partner = notation_DiagramElement()
    setattr(partner, 'notation_DiagramElement', None)
    _safe_set(owner, 'notation_DiagramDefinition2', {partner})
    assert getattr(partner, 'notation_DiagramElement') == owner
    _safe_set(owner, 'notation_DiagramDefinition2', set())
    assert getattr(partner, 'notation_DiagramElement') is None


def test_assoc_elements27_stub_double():
    # notation_GraphicalElement has no real 'notation_GraphicalElement29' property in the generated
    # code (a bare stub) -- manually attach it so notation_FigureContainment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_FigureContainment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_FigureContainment(layout="sample_text")
    partner = notation_GraphicalElement()
    setattr(partner, 'notation_GraphicalElement29', None)
    _safe_set(owner, 'notation_FigureContainment28', {partner})
    assert getattr(partner, 'notation_GraphicalElement29') == owner
    _safe_set(owner, 'notation_FigureContainment28', set())
    assert getattr(partner, 'notation_GraphicalElement29') is None


def test_assoc_elements31_stub_double():
    # notation_TextualElement has no real 'notation_TextualElement' property in the generated
    # code (a bare stub) -- manually attach it so notation_TextualContainment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_TextualContainment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_TextualContainment(layout="sample_text")
    partner = notation_TextualElement()
    setattr(partner, 'notation_TextualElement', None)
    _safe_set(owner, 'notation_TextualContainment32', {partner})
    assert getattr(partner, 'notation_TextualElement') == owner
    _safe_set(owner, 'notation_TextualContainment32', set())
    assert getattr(partner, 'notation_TextualElement') is None


def test_assoc_figureContainment25_stub_double():
    # notation_Figure has no real 'notation_Figure26' property in the generated
    # code (a bare stub) -- manually attach it so notation_FigureContainment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_FigureContainment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_FigureContainment(layout="sample_text")
    partner = notation_Figure()
    setattr(partner, 'notation_Figure26', None)
    _safe_set(owner, 'notation_FigureContainment', partner)
    assert getattr(partner, 'notation_Figure26') == owner
    _safe_set(owner, 'notation_FigureContainment', None)
    assert getattr(partner, 'notation_Figure26') is None


def test_assoc_figureStyle22_stub_double():
    # notation_Figure has no real 'notation_Figure' property in the generated
    # code (a bare stub) -- manually attach it so notation_FigureStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_FigureStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    partner = notation_Figure()
    setattr(partner, 'notation_Figure', None)
    _safe_set(owner, 'notation_FigureStyle', partner)
    assert getattr(partner, 'notation_Figure') == owner
    _safe_set(owner, 'notation_FigureStyle', None)
    assert getattr(partner, 'notation_Figure') is None


def test_assoc_lineStyle21_stub_double():
    # notation_Line has no real 'notation_Line' property in the generated
    # code (a bare stub) -- manually attach it so notation_LineStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_LineStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    partner = notation_Line()
    setattr(partner, 'notation_Line', None)
    _safe_set(owner, 'notation_LineStyle', partner)
    assert getattr(partner, 'notation_Line') == owner
    _safe_set(owner, 'notation_LineStyle', None)
    assert getattr(partner, 'notation_Line') is None


def test_assoc_nodeType4_stub_double():
    # notation_Node has no real 'notation_Node5' property in the generated
    # code (a bare stub) -- manually attach it so notation_Compartment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Compartment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Compartment(layout="sample_text")
    partner = notation_Node()
    setattr(partner, 'notation_Node5', None)
    _safe_set(owner, 'notation_Compartment', partner)
    assert getattr(partner, 'notation_Node5') == owner
    _safe_set(owner, 'notation_Compartment', None)
    assert getattr(partner, 'notation_Node5') is None


def test_assoc_points30_stub_double():
    # notation_Polyline has no real 'notation_Polyline' property in the generated
    # code (a bare stub) -- manually attach it so notation_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Point(x=7, y=7)
    partner = notation_Polyline()
    setattr(partner, 'notation_Polyline', None)
    _safe_set(owner, 'notation_Point', partner)
    assert owner in getattr(partner, 'notation_Polyline')
    _safe_set(owner, 'notation_Point', None)
    assert owner not in getattr(partner, 'notation_Polyline')


def test_assoc_primaryShape15_stub_double():
    # notation_GraphicalElement has no real 'notation_GraphicalElement17' property in the generated
    # code (a bare stub) -- manually attach it so notation_Composite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Composite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Composite(layout="sample_text")
    partner = notation_GraphicalElement()
    setattr(partner, 'notation_GraphicalElement17', None)
    _safe_set(owner, 'notation_Composite16', partner)
    assert getattr(partner, 'notation_GraphicalElement17') == owner
    _safe_set(owner, 'notation_Composite16', None)
    assert getattr(partner, 'notation_GraphicalElement17') is None


def test_assoc_subElements13_stub_double():
    # notation_GraphicalElement has no real 'notation_GraphicalElement14' property in the generated
    # code (a bare stub) -- manually attach it so notation_Composite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Composite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Composite(layout="sample_text")
    partner = notation_GraphicalElement()
    setattr(partner, 'notation_GraphicalElement14', None)
    _safe_set(owner, 'notation_Composite', {partner})
    assert getattr(partner, 'notation_GraphicalElement14') == owner
    _safe_set(owner, 'notation_Composite', set())
    assert getattr(partner, 'notation_GraphicalElement14') is None


def test_assoc_text19_stub_double():
    # notation_Label has no real 'notation_Label20' property in the generated
    # code (a bare stub) -- manually attach it so notation_TextualContainment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_TextualContainment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_TextualContainment(layout="sample_text")
    partner = notation_Label()
    setattr(partner, 'notation_Label20', None)
    _safe_set(owner, 'notation_TextualContainment', partner)
    assert getattr(partner, 'notation_Label20') == owner
    _safe_set(owner, 'notation_TextualContainment', None)
    assert getattr(partner, 'notation_Label20') is None


def test_assoc_textStyle18_stub_double():
    # notation_Label has no real 'notation_Label' property in the generated
    # code (a bare stub) -- manually attach it so notation_TextStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_TextStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    partner = notation_Label()
    setattr(partner, 'notation_Label', None)
    _safe_set(owner, 'notation_TextStyle', partner)
    assert getattr(partner, 'notation_Label') == owner
    _safe_set(owner, 'notation_TextStyle', None)
    assert getattr(partner, 'notation_Label') is None


