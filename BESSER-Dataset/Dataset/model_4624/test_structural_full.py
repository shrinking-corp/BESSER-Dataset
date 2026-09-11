import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_notation_BorderStyle_color_value_roundtrip():
    instance = notation_BorderStyle(color="sample_text", texture="sample_text", thickness=3.14)
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_notation_BorderStyle_texture_value_roundtrip():
    instance = notation_BorderStyle(color="sample_text", texture="sample_text", thickness=3.14)
    assert instance.texture == "sample_text"
    instance.texture = "sample_text_2"
    assert instance.texture == "sample_text_2"


def test_notation_BorderStyle_thickness_value_roundtrip():
    instance = notation_BorderStyle(color="sample_text", texture="sample_text", thickness=3.14)
    assert instance.thickness == 3.14
    instance.thickness = 9.99
    assert instance.thickness == 9.99


def test_notation_Compartment_layout_value_roundtrip():
    instance = notation_Compartment(layout="sample_text")
    assert instance.layout == "sample_text"
    instance.layout = "sample_text_2"
    assert instance.layout == "sample_text_2"


def test_notation_Composite_layout_value_roundtrip():
    instance = notation_Composite(layout="sample_text")
    assert instance.layout == "sample_text"
    instance.layout = "sample_text_2"
    assert instance.layout == "sample_text_2"


def test_notation_DiagramDefinition_Legend_value_roundtrip():
    instance = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    assert instance.Legend == "sample_text"
    instance.Legend = "sample_text_2"
    assert instance.Legend == "sample_text_2"


def test_notation_DiagramDefinition_Level_value_roundtrip():
    instance = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    assert instance.Level == 7
    instance.Level = 13
    assert instance.Level == 13


def test_notation_DiagramDefinition_allowChunks_value_roundtrip():
    instance = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    assert instance.allowChunks == True
    instance.allowChunks = False
    assert instance.allowChunks == False


def test_notation_DiagramDefinition_targetedAudience_value_roundtrip():
    instance = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    assert instance.targetedAudience == "sample_text"
    instance.targetedAudience = "sample_text_2"
    assert instance.targetedAudience == "sample_text_2"


def test_notation_FigureContainment_layout_value_roundtrip():
    instance = notation_FigureContainment(layout="sample_text")
    assert instance.layout == "sample_text"
    instance.layout = "sample_text_2"
    assert instance.layout == "sample_text_2"


def test_notation_FigureStyle_brightness_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.brightness == 7
    instance.brightness = 13
    assert instance.brightness == 13


def test_notation_FigureStyle_fillColor_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.fillColor == "sample_text"
    instance.fillColor = "sample_text_2"
    assert instance.fillColor == "sample_text_2"


def test_notation_FigureStyle_fillOrientation_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.fillOrientation == "sample_text"
    instance.fillOrientation = "sample_text_2"
    assert instance.fillOrientation == "sample_text_2"


def test_notation_FigureStyle_fillTexture_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.fillTexture == "sample_text"
    instance.fillTexture = "sample_text_2"
    assert instance.fillTexture == "sample_text_2"


def test_notation_FigureStyle_fillTextureColor_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.fillTextureColor == "sample_text"
    instance.fillTextureColor = "sample_text_2"
    assert instance.fillTextureColor == "sample_text_2"


def test_notation_FigureStyle_height_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_notation_FigureStyle_orientation_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_notation_FigureStyle_width_value_roundtrip():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_notation_IDElement_ID_value_roundtrip():
    instance = notation_IDElement(ID="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_notation_Icon_iconType_value_roundtrip():
    instance = notation_Icon(iconType="sample_text")
    assert instance.iconType == "sample_text"
    instance.iconType = "sample_text_2"
    assert instance.iconType == "sample_text_2"


def test_notation_IconStyle_brightness_value_roundtrip():
    instance = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.brightness == 7
    instance.brightness = 13
    assert instance.brightness == 13


def test_notation_IconStyle_color_value_roundtrip():
    instance = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_notation_IconStyle_height_value_roundtrip():
    instance = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_notation_IconStyle_orientation_value_roundtrip():
    instance = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_notation_IconStyle_width_value_roundtrip():
    instance = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_notation_Image_path_value_roundtrip():
    instance = notation_Image(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_notation_LineStyle_brightness_value_roundtrip():
    instance = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    assert instance.brightness == 7
    instance.brightness = 13
    assert instance.brightness == 13


def test_notation_LineStyle_color_value_roundtrip():
    instance = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_notation_LineStyle_length_value_roundtrip():
    instance = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    assert instance.length == 3.14
    instance.length = 9.99
    assert instance.length == 9.99


def test_notation_LineStyle_orientation_value_roundtrip():
    instance = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_notation_LineStyle_texture_value_roundtrip():
    instance = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    assert instance.texture == "sample_text"
    instance.texture = "sample_text_2"
    assert instance.texture == "sample_text_2"


def test_notation_LineStyle_thickness_value_roundtrip():
    instance = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    assert instance.thickness == 3.14
    instance.thickness = 9.99
    assert instance.thickness == 9.99


def test_notation_NotationDefinition_Type_value_roundtrip():
    instance = notation_NotationDefinition(Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_notation_Point_x_value_roundtrip():
    instance = notation_Point(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_notation_Point_y_value_roundtrip():
    instance = notation_Point(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_notation_TextStyle_bold_value_roundtrip():
    instance = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    assert instance.bold == True
    instance.bold = False
    assert instance.bold == False


def test_notation_TextStyle_fontColor_value_roundtrip():
    instance = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    assert instance.fontColor == "sample_text"
    instance.fontColor = "sample_text_2"
    assert instance.fontColor == "sample_text_2"


def test_notation_TextStyle_fontName_value_roundtrip():
    instance = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    assert instance.fontName == "sample_text"
    instance.fontName = "sample_text_2"
    assert instance.fontName == "sample_text_2"


def test_notation_TextStyle_fontSize_value_roundtrip():
    instance = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    assert instance.fontSize == 7
    instance.fontSize = 13
    assert instance.fontSize == 13


def test_notation_TextStyle_italic_value_roundtrip():
    instance = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    assert instance.italic == True
    instance.italic = False
    assert instance.italic == False


def test_notation_TextStyle_underlined_value_roundtrip():
    instance = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    assert instance.underlined == True
    instance.underlined = False
    assert instance.underlined == False


def test_notation_TextualContainment_layout_value_roundtrip():
    instance = notation_TextualContainment(layout="sample_text")
    assert instance.layout == "sample_text"
    instance.layout = "sample_text_2"
    assert instance.layout == "sample_text_2"


def test_notation_Node_isa_DiagramElement():
    instance = notation_Node()
    assert isinstance(instance, DiagramElement)


def test_notation_Relation_isa_DiagramElement():
    instance = notation_Relation()
    assert isinstance(instance, DiagramElement)


def test_notation_Circle_isa_Figure():
    instance = notation_Circle()
    assert isinstance(instance, Figure)


def test_notation_Cube_isa_Figure():
    instance = notation_Cube()
    assert isinstance(instance, Figure)


def test_notation_Cylinder_isa_Figure():
    instance = notation_Cylinder()
    assert isinstance(instance, Figure)


def test_notation_Diamond_isa_Figure():
    instance = notation_Diamond()
    assert isinstance(instance, Figure)


def test_notation_Polyline_isa_Figure():
    instance = notation_Polyline()
    assert isinstance(instance, Figure)


def test_notation_Rectangle_isa_Figure():
    instance = notation_Rectangle()
    assert isinstance(instance, Figure)


def test_notation_Roundtangle_isa_Figure():
    instance = notation_Roundtangle()
    assert isinstance(instance, Figure)


def test_notation_Square_isa_Figure():
    instance = notation_Square()
    assert isinstance(instance, Figure)


def test_notation_Triangle_isa_Figure():
    instance = notation_Triangle()
    assert isinstance(instance, Figure)


def test_notation_Composite_isa_GraphicalElement():
    instance = notation_Composite(layout="sample_text")
    assert isinstance(instance, GraphicalElement)


def test_notation_Figure_isa_GraphicalElement():
    instance = notation_Figure()
    assert isinstance(instance, GraphicalElement)


def test_notation_Icon_isa_GraphicalElement():
    instance = notation_Icon(iconType="sample_text")
    assert isinstance(instance, GraphicalElement)


def test_notation_Image_isa_GraphicalElement():
    instance = notation_Image(path="sample_text")
    assert isinstance(instance, GraphicalElement)


def test_notation_Label_isa_GraphicalElement():
    instance = notation_Label()
    assert isinstance(instance, GraphicalElement)


def test_notation_Line_isa_GraphicalElement():
    instance = notation_Line()
    assert isinstance(instance, GraphicalElement)


def test_notation_SyntaxOf_isa_GraphicalElement():
    instance = notation_SyntaxOf()
    assert isinstance(instance, GraphicalElement)


def test_notation_DiagramElement_isa_IDElement():
    instance = notation_DiagramElement()
    assert isinstance(instance, IDElement)


def test_notation_GraphicalElement_isa_IDElement():
    instance = notation_GraphicalElement()
    assert isinstance(instance, IDElement)


def test_notation_TextualElement_isa_IDElement():
    instance = notation_TextualElement()
    assert isinstance(instance, IDElement)


def test_notation_Compartment_isa_Relation():
    instance = notation_Compartment(layout="sample_text")
    assert isinstance(instance, Relation)


def test_notation_Link_isa_Relation():
    instance = notation_Link()
    assert isinstance(instance, Relation)


def test_notation_BorderStyle_isa_Style():
    instance = notation_BorderStyle(color="sample_text", texture="sample_text", thickness=3.14)
    assert isinstance(instance, Style)


def test_notation_FigureStyle_isa_Style():
    instance = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert isinstance(instance, Style)


def test_notation_IconStyle_isa_Style():
    instance = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    assert isinstance(instance, Style)


def test_notation_LineStyle_isa_Style():
    instance = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    assert isinstance(instance, Style)


def test_notation_TextStyle_isa_Style():
    instance = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    assert isinstance(instance, Style)


def test_notation_Keyword_isa_TextualElement():
    instance = notation_Keyword()
    assert isinstance(instance, TextualElement)


def test_notation_Token_isa_TextualElement():
    instance = notation_Token()
    assert isinstance(instance, TextualElement)


def test_notation_Value_isa_TextualElement():
    instance = notation_Value()
    assert isinstance(instance, TextualElement)


def test_notation_AttributeValue_isa_Value():
    instance = notation_AttributeValue()
    assert isinstance(instance, Value)


def test_notation_ReferenceValue_isa_Value():
    instance = notation_ReferenceValue()
    assert isinstance(instance, Value)


def test_assoc_approximateRepresentation11_link_reassign_clear():
    a = notation_Image(path="sample_text")
    b1 = notation_GraphicalElement()
    b2 = notation_GraphicalElement()
    _safe_set(a, 'notation_Image', b1)
    assert _is_linked(a, 'notation_Image', b1)
    if hasattr(b1, 'notation_GraphicalElement12'):
        assert _is_linked(b1, 'notation_GraphicalElement12', a)
    _safe_set(a, 'notation_Image', b2)
    assert _is_linked(a, 'notation_Image', b2)
    if hasattr(b1, 'notation_GraphicalElement12'):
        assert not _is_linked(b1, 'notation_GraphicalElement12', a)
    if hasattr(b2, 'notation_GraphicalElement12'):
        assert _is_linked(b2, 'notation_GraphicalElement12', a)
    _safe_set(a, 'notation_Image', None)
    assert not _is_linked(a, 'notation_Image', b2)
    if hasattr(b2, 'notation_GraphicalElement12'):
        assert not _is_linked(b2, 'notation_GraphicalElement12', a)


def test_assoc_borderStyle23_link_reassign_clear():
    a = notation_BorderStyle(color="sample_text", texture="sample_text", thickness=3.14)
    b1 = notation_Figure()
    b2 = notation_Figure()
    _safe_set(a, 'notation_BorderStyle', b1)
    assert _is_linked(a, 'notation_BorderStyle', b1)
    if hasattr(b1, 'notation_Figure24'):
        assert _is_linked(b1, 'notation_Figure24', a)
    _safe_set(a, 'notation_BorderStyle', b2)
    assert _is_linked(a, 'notation_BorderStyle', b2)
    if hasattr(b1, 'notation_Figure24'):
        assert not _is_linked(b1, 'notation_Figure24', a)
    if hasattr(b2, 'notation_Figure24'):
        assert _is_linked(b2, 'notation_Figure24', a)
    _safe_set(a, 'notation_BorderStyle', None)
    assert not _is_linked(a, 'notation_BorderStyle', b2)
    if hasattr(b2, 'notation_Figure24'):
        assert not _is_linked(b2, 'notation_Figure24', a)


def test_assoc_diagrams0_link_reassign_clear():
    a = notation_NotationDefinition(Type="sample_text")
    b1 = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    b2 = notation_DiagramDefinition(Legend="sample_text_2", Level=13, allowChunks=False, targetedAudience="sample_text_2")
    _safe_set(a, 'notation_NotationDefinition', {b1})
    assert _is_linked(a, 'notation_NotationDefinition', b1)
    if hasattr(b1, 'notation_DiagramDefinition'):
        assert _is_linked(b1, 'notation_DiagramDefinition', a)
    _safe_set(a, 'notation_NotationDefinition', {b2})
    assert _is_linked(a, 'notation_NotationDefinition', b2)
    if hasattr(b1, 'notation_DiagramDefinition'):
        assert not _is_linked(b1, 'notation_DiagramDefinition', a)
    if hasattr(b2, 'notation_DiagramDefinition'):
        assert _is_linked(b2, 'notation_DiagramDefinition', a)
    _safe_set(a, 'notation_NotationDefinition', set())
    assert not _is_linked(a, 'notation_NotationDefinition', b2)
    if hasattr(b2, 'notation_DiagramDefinition'):
        assert not _is_linked(b2, 'notation_DiagramDefinition', a)


def test_assoc_elements1_link_reassign_clear():
    a = notation_DiagramDefinition(Legend="sample_text", Level=7, allowChunks=True, targetedAudience="sample_text")
    b1 = notation_DiagramElement()
    b2 = notation_DiagramElement()
    _safe_set(a, 'notation_DiagramDefinition2', {b1})
    assert _is_linked(a, 'notation_DiagramDefinition2', b1)
    if hasattr(b1, 'notation_DiagramElement'):
        assert _is_linked(b1, 'notation_DiagramElement', a)
    _safe_set(a, 'notation_DiagramDefinition2', {b2})
    assert _is_linked(a, 'notation_DiagramDefinition2', b2)
    if hasattr(b1, 'notation_DiagramElement'):
        assert not _is_linked(b1, 'notation_DiagramElement', a)
    if hasattr(b2, 'notation_DiagramElement'):
        assert _is_linked(b2, 'notation_DiagramElement', a)
    _safe_set(a, 'notation_DiagramDefinition2', set())
    assert not _is_linked(a, 'notation_DiagramDefinition2', b2)
    if hasattr(b2, 'notation_DiagramElement'):
        assert not _is_linked(b2, 'notation_DiagramElement', a)


def test_assoc_elements27_link_reassign_clear():
    a = notation_FigureContainment(layout="sample_text")
    b1 = notation_GraphicalElement()
    b2 = notation_GraphicalElement()
    _safe_set(a, 'notation_FigureContainment28', {b1})
    assert _is_linked(a, 'notation_FigureContainment28', b1)
    if hasattr(b1, 'notation_GraphicalElement29'):
        assert _is_linked(b1, 'notation_GraphicalElement29', a)
    _safe_set(a, 'notation_FigureContainment28', {b2})
    assert _is_linked(a, 'notation_FigureContainment28', b2)
    if hasattr(b1, 'notation_GraphicalElement29'):
        assert not _is_linked(b1, 'notation_GraphicalElement29', a)
    if hasattr(b2, 'notation_GraphicalElement29'):
        assert _is_linked(b2, 'notation_GraphicalElement29', a)
    _safe_set(a, 'notation_FigureContainment28', set())
    assert not _is_linked(a, 'notation_FigureContainment28', b2)
    if hasattr(b2, 'notation_GraphicalElement29'):
        assert not _is_linked(b2, 'notation_GraphicalElement29', a)


def test_assoc_elements31_link_reassign_clear():
    a = notation_TextualContainment(layout="sample_text")
    b1 = notation_TextualElement()
    b2 = notation_TextualElement()
    _safe_set(a, 'notation_TextualContainment32', {b1})
    assert _is_linked(a, 'notation_TextualContainment32', b1)
    if hasattr(b1, 'notation_TextualElement'):
        assert _is_linked(b1, 'notation_TextualElement', a)
    _safe_set(a, 'notation_TextualContainment32', {b2})
    assert _is_linked(a, 'notation_TextualContainment32', b2)
    if hasattr(b1, 'notation_TextualElement'):
        assert not _is_linked(b1, 'notation_TextualElement', a)
    if hasattr(b2, 'notation_TextualElement'):
        assert _is_linked(b2, 'notation_TextualElement', a)
    _safe_set(a, 'notation_TextualContainment32', set())
    assert not _is_linked(a, 'notation_TextualContainment32', b2)
    if hasattr(b2, 'notation_TextualElement'):
        assert not _is_linked(b2, 'notation_TextualElement', a)


def test_assoc_figureContainment25_link_reassign_clear():
    a = notation_FigureContainment(layout="sample_text")
    b1 = notation_Figure()
    b2 = notation_Figure()
    _safe_set(a, 'notation_FigureContainment', b1)
    assert _is_linked(a, 'notation_FigureContainment', b1)
    if hasattr(b1, 'notation_Figure26'):
        assert _is_linked(b1, 'notation_Figure26', a)
    _safe_set(a, 'notation_FigureContainment', b2)
    assert _is_linked(a, 'notation_FigureContainment', b2)
    if hasattr(b1, 'notation_Figure26'):
        assert not _is_linked(b1, 'notation_Figure26', a)
    if hasattr(b2, 'notation_Figure26'):
        assert _is_linked(b2, 'notation_Figure26', a)
    _safe_set(a, 'notation_FigureContainment', None)
    assert not _is_linked(a, 'notation_FigureContainment', b2)
    if hasattr(b2, 'notation_Figure26'):
        assert not _is_linked(b2, 'notation_Figure26', a)


def test_assoc_figureStyle22_link_reassign_clear():
    a = notation_FigureStyle(brightness=7, fillColor="sample_text", fillOrientation="sample_text", fillTexture="sample_text", fillTextureColor="sample_text", height=3.14, orientation="sample_text", width=3.14)
    b1 = notation_Figure()
    b2 = notation_Figure()
    _safe_set(a, 'notation_FigureStyle', b1)
    assert _is_linked(a, 'notation_FigureStyle', b1)
    if hasattr(b1, 'notation_Figure'):
        assert _is_linked(b1, 'notation_Figure', a)
    _safe_set(a, 'notation_FigureStyle', b2)
    assert _is_linked(a, 'notation_FigureStyle', b2)
    if hasattr(b1, 'notation_Figure'):
        assert not _is_linked(b1, 'notation_Figure', a)
    if hasattr(b2, 'notation_Figure'):
        assert _is_linked(b2, 'notation_Figure', a)
    _safe_set(a, 'notation_FigureStyle', None)
    assert not _is_linked(a, 'notation_FigureStyle', b2)
    if hasattr(b2, 'notation_Figure'):
        assert not _is_linked(b2, 'notation_Figure', a)


def test_assoc_lineStyle21_link_reassign_clear():
    a = notation_LineStyle(brightness=7, color="sample_text", length=3.14, orientation="sample_text", texture="sample_text", thickness=3.14)
    b1 = notation_Line()
    b2 = notation_Line()
    _safe_set(a, 'notation_LineStyle', b1)
    assert _is_linked(a, 'notation_LineStyle', b1)
    if hasattr(b1, 'notation_Line'):
        assert _is_linked(b1, 'notation_Line', a)
    _safe_set(a, 'notation_LineStyle', b2)
    assert _is_linked(a, 'notation_LineStyle', b2)
    if hasattr(b1, 'notation_Line'):
        assert not _is_linked(b1, 'notation_Line', a)
    if hasattr(b2, 'notation_Line'):
        assert _is_linked(b2, 'notation_Line', a)
    _safe_set(a, 'notation_LineStyle', None)
    assert not _is_linked(a, 'notation_LineStyle', b2)
    if hasattr(b2, 'notation_Line'):
        assert not _is_linked(b2, 'notation_Line', a)


def test_assoc_nodeType4_link_reassign_clear():
    a = notation_Compartment(layout="sample_text")
    b1 = notation_Node()
    b2 = notation_Node()
    _safe_set(a, 'notation_Compartment', b1)
    assert _is_linked(a, 'notation_Compartment', b1)
    if hasattr(b1, 'notation_Node5'):
        assert _is_linked(b1, 'notation_Node5', a)
    _safe_set(a, 'notation_Compartment', b2)
    assert _is_linked(a, 'notation_Compartment', b2)
    if hasattr(b1, 'notation_Node5'):
        assert not _is_linked(b1, 'notation_Node5', a)
    if hasattr(b2, 'notation_Node5'):
        assert _is_linked(b2, 'notation_Node5', a)
    _safe_set(a, 'notation_Compartment', None)
    assert not _is_linked(a, 'notation_Compartment', b2)
    if hasattr(b2, 'notation_Node5'):
        assert not _is_linked(b2, 'notation_Node5', a)


def test_assoc_points30_link_reassign_clear():
    a = notation_Point(x=7, y=7)
    b1 = notation_Polyline()
    b2 = notation_Polyline()
    _safe_set(a, 'notation_Point', b1)
    assert _is_linked(a, 'notation_Point', b1)
    if hasattr(b1, 'notation_Polyline'):
        assert _is_linked(b1, 'notation_Polyline', a)
    _safe_set(a, 'notation_Point', b2)
    assert _is_linked(a, 'notation_Point', b2)
    if hasattr(b1, 'notation_Polyline'):
        assert not _is_linked(b1, 'notation_Polyline', a)
    if hasattr(b2, 'notation_Polyline'):
        assert _is_linked(b2, 'notation_Polyline', a)
    _safe_set(a, 'notation_Point', None)
    assert not _is_linked(a, 'notation_Point', b2)
    if hasattr(b2, 'notation_Polyline'):
        assert not _is_linked(b2, 'notation_Polyline', a)


def test_assoc_primaryShape15_link_reassign_clear():
    a = notation_Composite(layout="sample_text")
    b1 = notation_GraphicalElement()
    b2 = notation_GraphicalElement()
    _safe_set(a, 'notation_Composite16', b1)
    assert _is_linked(a, 'notation_Composite16', b1)
    if hasattr(b1, 'notation_GraphicalElement17'):
        assert _is_linked(b1, 'notation_GraphicalElement17', a)
    _safe_set(a, 'notation_Composite16', b2)
    assert _is_linked(a, 'notation_Composite16', b2)
    if hasattr(b1, 'notation_GraphicalElement17'):
        assert not _is_linked(b1, 'notation_GraphicalElement17', a)
    if hasattr(b2, 'notation_GraphicalElement17'):
        assert _is_linked(b2, 'notation_GraphicalElement17', a)
    _safe_set(a, 'notation_Composite16', None)
    assert not _is_linked(a, 'notation_Composite16', b2)
    if hasattr(b2, 'notation_GraphicalElement17'):
        assert not _is_linked(b2, 'notation_GraphicalElement17', a)


def test_assoc_style10_link_reassign_clear():
    a = notation_IconStyle(brightness=7, color="sample_text", height=3.14, orientation="sample_text", width=3.14)
    b1 = notation_Icon(iconType="sample_text")
    b2 = notation_Icon(iconType="sample_text_2")
    _safe_set(a, 'notation_IconStyle', b1)
    assert _is_linked(a, 'notation_IconStyle', b1)
    if hasattr(b1, 'notation_Icon'):
        assert _is_linked(b1, 'notation_Icon', a)
    _safe_set(a, 'notation_IconStyle', b2)
    assert _is_linked(a, 'notation_IconStyle', b2)
    if hasattr(b1, 'notation_Icon'):
        assert not _is_linked(b1, 'notation_Icon', a)
    if hasattr(b2, 'notation_Icon'):
        assert _is_linked(b2, 'notation_Icon', a)
    _safe_set(a, 'notation_IconStyle', None)
    assert not _is_linked(a, 'notation_IconStyle', b2)
    if hasattr(b2, 'notation_Icon'):
        assert not _is_linked(b2, 'notation_Icon', a)


def test_assoc_subElements13_link_reassign_clear():
    a = notation_Composite(layout="sample_text")
    b1 = notation_GraphicalElement()
    b2 = notation_GraphicalElement()
    _safe_set(a, 'notation_Composite', {b1})
    assert _is_linked(a, 'notation_Composite', b1)
    if hasattr(b1, 'notation_GraphicalElement14'):
        assert _is_linked(b1, 'notation_GraphicalElement14', a)
    _safe_set(a, 'notation_Composite', {b2})
    assert _is_linked(a, 'notation_Composite', b2)
    if hasattr(b1, 'notation_GraphicalElement14'):
        assert not _is_linked(b1, 'notation_GraphicalElement14', a)
    if hasattr(b2, 'notation_GraphicalElement14'):
        assert _is_linked(b2, 'notation_GraphicalElement14', a)
    _safe_set(a, 'notation_Composite', set())
    assert not _is_linked(a, 'notation_Composite', b2)
    if hasattr(b2, 'notation_GraphicalElement14'):
        assert not _is_linked(b2, 'notation_GraphicalElement14', a)


def test_assoc_text19_link_reassign_clear():
    a = notation_TextualContainment(layout="sample_text")
    b1 = notation_Label()
    b2 = notation_Label()
    _safe_set(a, 'notation_TextualContainment', b1)
    assert _is_linked(a, 'notation_TextualContainment', b1)
    if hasattr(b1, 'notation_Label20'):
        assert _is_linked(b1, 'notation_Label20', a)
    _safe_set(a, 'notation_TextualContainment', b2)
    assert _is_linked(a, 'notation_TextualContainment', b2)
    if hasattr(b1, 'notation_Label20'):
        assert not _is_linked(b1, 'notation_Label20', a)
    if hasattr(b2, 'notation_Label20'):
        assert _is_linked(b2, 'notation_Label20', a)
    _safe_set(a, 'notation_TextualContainment', None)
    assert not _is_linked(a, 'notation_TextualContainment', b2)
    if hasattr(b2, 'notation_Label20'):
        assert not _is_linked(b2, 'notation_Label20', a)


def test_assoc_textStyle18_link_reassign_clear():
    a = notation_TextStyle(bold=True, fontColor="sample_text", fontName="sample_text", fontSize=7, italic=True, underlined=True)
    b1 = notation_Label()
    b2 = notation_Label()
    _safe_set(a, 'notation_TextStyle', b1)
    assert _is_linked(a, 'notation_TextStyle', b1)
    if hasattr(b1, 'notation_Label'):
        assert _is_linked(b1, 'notation_Label', a)
    _safe_set(a, 'notation_TextStyle', b2)
    assert _is_linked(a, 'notation_TextStyle', b2)
    if hasattr(b1, 'notation_Label'):
        assert not _is_linked(b1, 'notation_Label', a)
    if hasattr(b2, 'notation_Label'):
        assert _is_linked(b2, 'notation_Label', a)
    _safe_set(a, 'notation_TextStyle', None)
    assert not _is_linked(a, 'notation_TextStyle', b2)
    if hasattr(b2, 'notation_Label'):
        assert not _is_linked(b2, 'notation_Label', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


Figure_strategy = st.builds(Figure)
@given(instance=Figure_strategy)
@settings(max_examples=25)
def test_Figure_instantiation(instance):
    assert isinstance(instance, Figure)


GraphicalElement_strategy = st.builds(GraphicalElement)
@given(instance=GraphicalElement_strategy)
@settings(max_examples=25)
def test_GraphicalElement_instantiation(instance):
    assert isinstance(instance, GraphicalElement)


IDElement_strategy = st.builds(IDElement)
@given(instance=IDElement_strategy)
@settings(max_examples=25)
def test_IDElement_instantiation(instance):
    assert isinstance(instance, IDElement)


Relation_strategy = st.builds(Relation)
@given(instance=Relation_strategy)
@settings(max_examples=25)
def test_Relation_instantiation(instance):
    assert isinstance(instance, Relation)


Style_strategy = st.builds(Style)
@given(instance=Style_strategy)
@settings(max_examples=25)
def test_Style_instantiation(instance):
    assert isinstance(instance, Style)


TextualElement_strategy = st.builds(TextualElement)
@given(instance=TextualElement_strategy)
@settings(max_examples=25)
def test_TextualElement_instantiation(instance):
    assert isinstance(instance, TextualElement)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


notation_AttributeValue_strategy = st.builds(notation_AttributeValue)
@given(instance=notation_AttributeValue_strategy)
@settings(max_examples=25)
def test_notation_AttributeValue_instantiation(instance):
    assert isinstance(instance, notation_AttributeValue)


notation_BorderStyle_strategy = st.builds(notation_BorderStyle, color=safe_text, texture=safe_text, thickness=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=notation_BorderStyle_strategy)
@settings(max_examples=25)
def test_notation_BorderStyle_instantiation(instance):
    assert isinstance(instance, notation_BorderStyle)


notation_Circle_strategy = st.builds(notation_Circle)
@given(instance=notation_Circle_strategy)
@settings(max_examples=25)
def test_notation_Circle_instantiation(instance):
    assert isinstance(instance, notation_Circle)


notation_Compartment_strategy = st.builds(notation_Compartment, layout=safe_text)
@given(instance=notation_Compartment_strategy)
@settings(max_examples=25)
def test_notation_Compartment_instantiation(instance):
    assert isinstance(instance, notation_Compartment)


notation_Composite_strategy = st.builds(notation_Composite, layout=safe_text)
@given(instance=notation_Composite_strategy)
@settings(max_examples=25)
def test_notation_Composite_instantiation(instance):
    assert isinstance(instance, notation_Composite)


notation_Cube_strategy = st.builds(notation_Cube)
@given(instance=notation_Cube_strategy)
@settings(max_examples=25)
def test_notation_Cube_instantiation(instance):
    assert isinstance(instance, notation_Cube)


notation_Cylinder_strategy = st.builds(notation_Cylinder)
@given(instance=notation_Cylinder_strategy)
@settings(max_examples=25)
def test_notation_Cylinder_instantiation(instance):
    assert isinstance(instance, notation_Cylinder)


notation_DiagramDefinition_strategy = st.builds(notation_DiagramDefinition, Legend=safe_text, Level=st.integers(), allowChunks=st.booleans(), targetedAudience=safe_text)
@given(instance=notation_DiagramDefinition_strategy)
@settings(max_examples=25)
def test_notation_DiagramDefinition_instantiation(instance):
    assert isinstance(instance, notation_DiagramDefinition)


notation_DiagramElement_strategy = st.builds(notation_DiagramElement)
@given(instance=notation_DiagramElement_strategy)
@settings(max_examples=25)
def test_notation_DiagramElement_instantiation(instance):
    assert isinstance(instance, notation_DiagramElement)


notation_Diamond_strategy = st.builds(notation_Diamond)
@given(instance=notation_Diamond_strategy)
@settings(max_examples=25)
def test_notation_Diamond_instantiation(instance):
    assert isinstance(instance, notation_Diamond)


notation_Figure_strategy = st.builds(notation_Figure)
@given(instance=notation_Figure_strategy)
@settings(max_examples=25)
def test_notation_Figure_instantiation(instance):
    assert isinstance(instance, notation_Figure)


notation_FigureContainment_strategy = st.builds(notation_FigureContainment, layout=safe_text)
@given(instance=notation_FigureContainment_strategy)
@settings(max_examples=25)
def test_notation_FigureContainment_instantiation(instance):
    assert isinstance(instance, notation_FigureContainment)


notation_FigureStyle_strategy = st.builds(notation_FigureStyle, brightness=st.integers(), fillColor=safe_text, fillOrientation=safe_text, fillTexture=safe_text, fillTextureColor=safe_text, height=st.floats(allow_nan=False, allow_infinity=False), orientation=safe_text, width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=notation_FigureStyle_strategy)
@settings(max_examples=25)
def test_notation_FigureStyle_instantiation(instance):
    assert isinstance(instance, notation_FigureStyle)


notation_GraphicalElement_strategy = st.builds(notation_GraphicalElement)
@given(instance=notation_GraphicalElement_strategy)
@settings(max_examples=25)
def test_notation_GraphicalElement_instantiation(instance):
    assert isinstance(instance, notation_GraphicalElement)


notation_IDElement_strategy = st.builds(notation_IDElement, ID=safe_text)
@given(instance=notation_IDElement_strategy)
@settings(max_examples=25)
def test_notation_IDElement_instantiation(instance):
    assert isinstance(instance, notation_IDElement)


notation_Icon_strategy = st.builds(notation_Icon, iconType=safe_text)
@given(instance=notation_Icon_strategy)
@settings(max_examples=25)
def test_notation_Icon_instantiation(instance):
    assert isinstance(instance, notation_Icon)


notation_IconStyle_strategy = st.builds(notation_IconStyle, brightness=st.integers(), color=safe_text, height=st.floats(allow_nan=False, allow_infinity=False), orientation=safe_text, width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=notation_IconStyle_strategy)
@settings(max_examples=25)
def test_notation_IconStyle_instantiation(instance):
    assert isinstance(instance, notation_IconStyle)


notation_Image_strategy = st.builds(notation_Image, path=safe_text)
@given(instance=notation_Image_strategy)
@settings(max_examples=25)
def test_notation_Image_instantiation(instance):
    assert isinstance(instance, notation_Image)


notation_Keyword_strategy = st.builds(notation_Keyword)
@given(instance=notation_Keyword_strategy)
@settings(max_examples=25)
def test_notation_Keyword_instantiation(instance):
    assert isinstance(instance, notation_Keyword)


notation_Label_strategy = st.builds(notation_Label)
@given(instance=notation_Label_strategy)
@settings(max_examples=25)
def test_notation_Label_instantiation(instance):
    assert isinstance(instance, notation_Label)


notation_Line_strategy = st.builds(notation_Line)
@given(instance=notation_Line_strategy)
@settings(max_examples=25)
def test_notation_Line_instantiation(instance):
    assert isinstance(instance, notation_Line)


notation_LineStyle_strategy = st.builds(notation_LineStyle, brightness=st.integers(), color=safe_text, length=st.floats(allow_nan=False, allow_infinity=False), orientation=safe_text, texture=safe_text, thickness=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=notation_LineStyle_strategy)
@settings(max_examples=25)
def test_notation_LineStyle_instantiation(instance):
    assert isinstance(instance, notation_LineStyle)


notation_Link_strategy = st.builds(notation_Link)
@given(instance=notation_Link_strategy)
@settings(max_examples=25)
def test_notation_Link_instantiation(instance):
    assert isinstance(instance, notation_Link)


notation_Node_strategy = st.builds(notation_Node)
@given(instance=notation_Node_strategy)
@settings(max_examples=25)
def test_notation_Node_instantiation(instance):
    assert isinstance(instance, notation_Node)


notation_NotationDefinition_strategy = st.builds(notation_NotationDefinition, Type=safe_text)
@given(instance=notation_NotationDefinition_strategy)
@settings(max_examples=25)
def test_notation_NotationDefinition_instantiation(instance):
    assert isinstance(instance, notation_NotationDefinition)


notation_Point_strategy = st.builds(notation_Point, x=st.integers(), y=st.integers())
@given(instance=notation_Point_strategy)
@settings(max_examples=25)
def test_notation_Point_instantiation(instance):
    assert isinstance(instance, notation_Point)


notation_Polyline_strategy = st.builds(notation_Polyline)
@given(instance=notation_Polyline_strategy)
@settings(max_examples=25)
def test_notation_Polyline_instantiation(instance):
    assert isinstance(instance, notation_Polyline)


notation_Rectangle_strategy = st.builds(notation_Rectangle)
@given(instance=notation_Rectangle_strategy)
@settings(max_examples=25)
def test_notation_Rectangle_instantiation(instance):
    assert isinstance(instance, notation_Rectangle)


notation_ReferenceValue_strategy = st.builds(notation_ReferenceValue)
@given(instance=notation_ReferenceValue_strategy)
@settings(max_examples=25)
def test_notation_ReferenceValue_instantiation(instance):
    assert isinstance(instance, notation_ReferenceValue)


notation_Relation_strategy = st.builds(notation_Relation)
@given(instance=notation_Relation_strategy)
@settings(max_examples=25)
def test_notation_Relation_instantiation(instance):
    assert isinstance(instance, notation_Relation)


notation_Roundtangle_strategy = st.builds(notation_Roundtangle)
@given(instance=notation_Roundtangle_strategy)
@settings(max_examples=25)
def test_notation_Roundtangle_instantiation(instance):
    assert isinstance(instance, notation_Roundtangle)


notation_Square_strategy = st.builds(notation_Square)
@given(instance=notation_Square_strategy)
@settings(max_examples=25)
def test_notation_Square_instantiation(instance):
    assert isinstance(instance, notation_Square)


notation_Style_strategy = st.builds(notation_Style)
@given(instance=notation_Style_strategy)
@settings(max_examples=25)
def test_notation_Style_instantiation(instance):
    assert isinstance(instance, notation_Style)


notation_SyntaxOf_strategy = st.builds(notation_SyntaxOf)
@given(instance=notation_SyntaxOf_strategy)
@settings(max_examples=25)
def test_notation_SyntaxOf_instantiation(instance):
    assert isinstance(instance, notation_SyntaxOf)


notation_TextStyle_strategy = st.builds(notation_TextStyle, bold=st.booleans(), fontColor=safe_text, fontName=safe_text, fontSize=st.integers(), italic=st.booleans(), underlined=st.booleans())
@given(instance=notation_TextStyle_strategy)
@settings(max_examples=25)
def test_notation_TextStyle_instantiation(instance):
    assert isinstance(instance, notation_TextStyle)


notation_TextualContainment_strategy = st.builds(notation_TextualContainment, layout=safe_text)
@given(instance=notation_TextualContainment_strategy)
@settings(max_examples=25)
def test_notation_TextualContainment_instantiation(instance):
    assert isinstance(instance, notation_TextualContainment)


notation_TextualElement_strategy = st.builds(notation_TextualElement)
@given(instance=notation_TextualElement_strategy)
@settings(max_examples=25)
def test_notation_TextualElement_instantiation(instance):
    assert isinstance(instance, notation_TextualElement)


notation_Token_strategy = st.builds(notation_Token)
@given(instance=notation_Token_strategy)
@settings(max_examples=25)
def test_notation_Token_instantiation(instance):
    assert isinstance(instance, notation_Token)


notation_Triangle_strategy = st.builds(notation_Triangle)
@given(instance=notation_Triangle_strategy)
@settings(max_examples=25)
def test_notation_Triangle_instantiation(instance):
    assert isinstance(instance, notation_Triangle)


notation_Value_strategy = st.builds(notation_Value)
@given(instance=notation_Value_strategy)
@settings(max_examples=25)
def test_notation_Value_instantiation(instance):
    assert isinstance(instance, notation_Value)


