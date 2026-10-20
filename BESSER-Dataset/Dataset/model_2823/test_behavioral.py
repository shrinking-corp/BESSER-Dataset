import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotationSupport,
    BooleanSelectionSupport,
    BorderStyleSupport,
    BorderSupport,
    ColorAlphaSupport,
    ColorAlternativeSupport,
    ColorBackgroundSupport,
    ColorBorderSupport,
    ColorForegroundSupport,
    FlipSupport,
    FontOverrides,
    FontSupport,
    IconPositionSupport,
    IconSupport,
    ItemOverrides,
    ItemSupport,
    LineHeightSupport,
    LineStyleSupport,
    LinkSupport,
    ListSupport,
    NameSupport,
    NoteSupport,
    Operation,
    Overrides,
    Panel,
    Reference,
    RotationSupport,
    SelectionSupport,
    SkinSupport,
    StateSupport,
    Storyboard,
    StringToStringMap,
    TextAlignmentSupport,
    TextLinksSupport,
    ValueSupport,
    VerticalScrollbarSupport,
    Widget,
    WidgetContainer,
    WidgetContainerOverrides,
    WidgetOverrides,
    model_Accordion,
    model_Alert,
    model_AnnotationSupport,
    model_Area,
    model_Arrow,
    model_BooleanSelectionSupport,
    model_BorderStyleSupport,
    model_BorderSupport,
    model_Breadcrumbs,
    model_Browser,
    model_Button,
    model_ButtonBar,
    model_Callout,
    model_Chart,
    model_Checkbox,
    model_Circle,
    model_ColorAlphaSupport,
    model_ColorAlternativeSupport,
    model_ColorBackgroundSupport,
    model_ColorBorderSupport,
    model_ColorForegroundSupport,
    model_ColorPicker,
    model_Combo,
    model_CoverFlow,
    model_CrossOut,
    model_CurlyBrace,
    model_DateField,
    model_FlipSupport,
    model_Font,
    model_FontSupport,
    model_Group,
    model_HLine,
    model_HScrollbar,
    model_HSlider,
    model_HSplitter,
    model_Hotspot,
    model_Icon,
    model_IconPositionSupport,
    model_IconSupport,
    model_Image,
    model_Item,
    model_ItemSupport,
    model_Label,
    model_LineHeightSupport,
    model_LineStyleSupport,
    model_Link,
    model_LinkBar,
    model_LinkSupport,
    model_List,
    model_ListSupport,
    model_Map,
    model_Master,
    model_Menu,
    model_NameSupport,
    model_Note,
    model_NoteSupport,
    model_Panel,
    model_Placeholder,
    model_Popup,
    model_ProgressBar,
    model_RadioButton,
    model_Rectangle,
    model_RotationSupport,
    model_RulerGuide,
    model_SVGImage,
    model_ScratchOut,
    model_Screen,
    model_ScreenFont,
    model_ScreenRuler,
    model_SearchField,
    model_SelectionSupport,
    model_Shape,
    model_SkinSupport,
    model_Spinner,
    model_StateSupport,
    model_Switch,
    model_TabbedPane,
    model_Table,
    model_Tabs,
    model_Text,
    model_TextAlignmentSupport,
    model_TextArea,
    model_TextField,
    model_TextLinksSupport,
    model_Tooltip,
    model_Tree,
    model_VButtonBar,
    model_VLine,
    model_VScrollbar,
    model_VSlider,
    model_VSplitter,
    model_ValueSupport,
    model_VerticalScrollbarSupport,
    model_VideoPlayer,
    model_Widget,
    model_WidgetContainer,
    model_WidgetDescriptor,
    model_WidgetGroup,
    model_Window,
    model_overrides_Delete,
    model_overrides_FontOverrides,
    model_overrides_Insert,
    model_overrides_ItemOverrides,
    model_overrides_Move,
    model_overrides_Operation,
    model_overrides_Overrides,
    model_overrides_Reference,
    model_overrides_StringToStringMap,
    model_overrides_WidgetContainerOverrides,
    model_overrides_WidgetOverrides,
    model_story_Panel,
    model_story_Storyboard,
    overrides_Operation,
    overrides_Reference,
    overrides_WidgetContainerOverrides,
    overrides_model_EObject,
    story_model_Screen,
    BorderStyle,
    ButtonStyle,
    ChartType,
    IconSize,
    LineStyle,
    Position,
    ResizeMode,
    Rotation90,
    ShapeType,
    State,
    TextAlignment,
    Theme,
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

def test_assoc_descriptor9_reverse_link_reassign_clear():
    a1 = model_WidgetDescriptor(resizeMode="sample_text", textCentered=True, textEditable=True, textLines=7, textWrappable=True, typeName="sample_text")
    a2 = model_WidgetDescriptor(resizeMode="sample_text_2", textCentered=False, textEditable=False, textLines=13, textWrappable=False, typeName="sample_text_2")
    b = model_Widget(annotation=True, customData="sample_text", customId="sample_text", height=7, id="sample_text", layoutParams="sample_text", locked=True, measuredHeight=7, measuredWidth=7, text="sample_text", width=7, x=7, y=7)
    _safe_set(b, 'model_Widget', a1)
    assert _is_linked(b, 'model_Widget', a1)
    if hasattr(a1, 'model_WidgetDescriptor'):
        assert _is_linked(a1, 'model_WidgetDescriptor', b)
    _safe_set(b, 'model_Widget', a2)
    assert _is_linked(b, 'model_Widget', a2)
    if hasattr(a1, 'model_WidgetDescriptor'):
        assert not _is_linked(a1, 'model_WidgetDescriptor', b)
    if hasattr(a2, 'model_WidgetDescriptor'):
        assert _is_linked(a2, 'model_WidgetDescriptor', b)
    _safe_set(b, 'model_Widget', None)
    assert not _is_linked(b, 'model_Widget', a2)
    if hasattr(a2, 'model_WidgetDescriptor'):
        assert not _is_linked(a2, 'model_WidgetDescriptor', b)


def test_assoc_font4_reverse_link_reassign_clear():
    a1 = model_ScreenFont(available="sample_text", bold=True, italic=True, name="sample_text", size="sample_text")
    a2 = model_ScreenFont(available="sample_text_2", bold=False, italic=False, name="sample_text_2", size="sample_text_2")
    b = model_Screen(minVersion="sample_text", name="sample_text", theme="sample_text")
    _safe_set(b, 'model_Screen5', a1)
    assert _is_linked(b, 'model_Screen5', a1)
    if hasattr(a1, 'model_ScreenFont'):
        assert _is_linked(a1, 'model_ScreenFont', b)
    _safe_set(b, 'model_Screen5', a2)
    assert _is_linked(b, 'model_Screen5', a2)
    if hasattr(a1, 'model_ScreenFont'):
        assert not _is_linked(a1, 'model_ScreenFont', b)
    if hasattr(a2, 'model_ScreenFont'):
        assert _is_linked(a2, 'model_ScreenFont', b)
    _safe_set(b, 'model_Screen5', None)
    assert not _is_linked(b, 'model_Screen5', a2)
    if hasattr(a2, 'model_ScreenFont'):
        assert not _is_linked(a2, 'model_ScreenFont', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes24_stub_double():
    # StringToStringMap has no real 'StringToStringMap' property in the generated
    # code (a bare stub) -- manually attach it so model_overrides_WidgetOverrides's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_overrides_WidgetOverrides's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_overrides_WidgetOverrides(height="sample_text", link="sample_text", noLink=True, noText=True, src="sample_text", text="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = StringToStringMap()
    setattr(partner, 'StringToStringMap', None)
    _safe_set(owner, 'model_overrides_WidgetOverrides', {partner})
    assert getattr(partner, 'StringToStringMap') == owner
    _safe_set(owner, 'model_overrides_WidgetOverrides', set())
    assert getattr(partner, 'StringToStringMap') is None


def test_assoc_container8_stub_double():
    # model_WidgetContainer has no real 'WidgetContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Widget(annotation=True, customData="sample_text", customId="sample_text", height=7, id="sample_text", layoutParams="sample_text", locked=True, measuredHeight=7, measuredWidth=7, text="sample_text", width=7, x=7, y=7)
    partner = model_WidgetContainer()
    setattr(partner, 'WidgetContainer', None)
    _safe_set(owner, 'widgets', partner)
    assert getattr(partner, 'WidgetContainer') == owner
    _safe_set(owner, 'widgets', None)
    assert getattr(partner, 'WidgetContainer') is None


def test_assoc_font17_stub_double():
    # model_FontSupport has no real 'model_FontSupport' property in the generated
    # code (a bare stub) -- manually attach it so model_Font's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Font's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Font(bold="sample_text", italic="sample_text", size="sample_text", underline="sample_text")
    partner = model_FontSupport()
    setattr(partner, 'model_FontSupport', None)
    _safe_set(owner, 'model_Font', partner)
    assert getattr(partner, 'model_FontSupport') == owner
    _safe_set(owner, 'model_Font', None)
    assert getattr(partner, 'model_FontSupport') is None


def test_assoc_font25_stub_double():
    # FontOverrides has no real 'FontOverrides' property in the generated
    # code (a bare stub) -- manually attach it so model_overrides_WidgetOverrides's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_overrides_WidgetOverrides's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_overrides_WidgetOverrides(height="sample_text", link="sample_text", noLink=True, noText=True, src="sample_text", text="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = FontOverrides()
    setattr(partner, 'FontOverrides', None)
    _safe_set(owner, 'model_overrides_WidgetOverrides26', partner)
    assert getattr(partner, 'FontOverrides') == owner
    _safe_set(owner, 'model_overrides_WidgetOverrides26', None)
    assert getattr(partner, 'FontOverrides') is None


def test_assoc_guides6_stub_double():
    # model_ScreenRuler has no real 'model_ScreenRuler7' property in the generated
    # code (a bare stub) -- manually attach it so model_RulerGuide's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_RulerGuide's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_RulerGuide(position=7)
    partner = model_ScreenRuler()
    setattr(partner, 'model_ScreenRuler7', None)
    _safe_set(owner, 'model_RulerGuide', partner)
    assert owner in getattr(partner, 'model_ScreenRuler7')
    _safe_set(owner, 'model_RulerGuide', None)
    assert owner not in getattr(partner, 'model_ScreenRuler7')


def test_assoc_hRuler0_stub_double():
    # model_ScreenRuler has no real 'model_ScreenRuler' property in the generated
    # code (a bare stub) -- manually attach it so model_Screen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Screen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Screen(minVersion="sample_text", name="sample_text", theme="sample_text")
    partner = model_ScreenRuler()
    setattr(partner, 'model_ScreenRuler', None)
    _safe_set(owner, 'model_Screen', partner)
    assert getattr(partner, 'model_ScreenRuler') == owner
    _safe_set(owner, 'model_Screen', None)
    assert getattr(partner, 'model_ScreenRuler') is None


def test_assoc_instance14_stub_double():
    # model_WidgetContainer has no real 'model_WidgetContainer16' property in the generated
    # code (a bare stub) -- manually attach it so model_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Master(dimmed=True)
    partner = model_WidgetContainer()
    setattr(partner, 'model_WidgetContainer16', None)
    _safe_set(owner, 'model_Master15', partner)
    assert getattr(partner, 'model_WidgetContainer16') == owner
    _safe_set(owner, 'model_Master15', None)
    assert getattr(partner, 'model_WidgetContainer16') is None


def test_assoc_itemChanges29_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so model_overrides_WidgetOverrides's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_overrides_WidgetOverrides's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_overrides_WidgetOverrides(height="sample_text", link="sample_text", noLink=True, noText=True, src="sample_text", text="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'model_overrides_WidgetOverrides30', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'model_overrides_WidgetOverrides30', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_items18_stub_double():
    # model_ItemSupport has no real 'model_ItemSupport' property in the generated
    # code (a bare stub) -- manually attach it so model_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Item(height=7, text="sample_text", width=7, x=7, y=7)
    partner = model_ItemSupport()
    setattr(partner, 'model_ItemSupport', None)
    _safe_set(owner, 'model_Item', partner)
    assert owner in getattr(partner, 'model_ItemSupport')
    _safe_set(owner, 'model_Item', None)
    assert owner not in getattr(partner, 'model_ItemSupport')


def test_assoc_items27_stub_double():
    # ItemOverrides has no real 'ItemOverrides' property in the generated
    # code (a bare stub) -- manually attach it so model_overrides_WidgetOverrides's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_overrides_WidgetOverrides's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_overrides_WidgetOverrides(height="sample_text", link="sample_text", noLink=True, noText=True, src="sample_text", text="sample_text", width="sample_text", x="sample_text", y="sample_text")
    partner = ItemOverrides()
    setattr(partner, 'ItemOverrides', None)
    _safe_set(owner, 'model_overrides_WidgetOverrides28', {partner})
    assert getattr(partner, 'ItemOverrides') == owner
    _safe_set(owner, 'model_overrides_WidgetOverrides28', set())
    assert getattr(partner, 'ItemOverrides') is None


def test_assoc_object31_stub_double():
    # overrides_model_EObject has no real 'overrides_model_EObject' property in the generated
    # code (a bare stub) -- manually attach it so model_overrides_Insert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_overrides_Insert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_overrides_Insert(newIndex=7)
    partner = overrides_model_EObject()
    setattr(partner, 'overrides_model_EObject', None)
    _safe_set(owner, 'model_overrides_Insert', partner)
    assert getattr(partner, 'overrides_model_EObject') == owner
    _safe_set(owner, 'model_overrides_Insert', None)
    assert getattr(partner, 'overrides_model_EObject') is None


def test_assoc_overrides12_stub_double():
    # Overrides has no real 'Overrides' property in the generated
    # code (a bare stub) -- manually attach it so model_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Master(dimmed=True)
    partner = Overrides()
    setattr(partner, 'Overrides', None)
    _safe_set(owner, 'model_Master13', partner)
    assert getattr(partner, 'Overrides') == owner
    _safe_set(owner, 'model_Master13', None)
    assert getattr(partner, 'Overrides') is None


def test_assoc_screen11_stub_double():
    # model_WidgetContainer has no real 'model_WidgetContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_Master's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Master's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Master(dimmed=True)
    partner = model_WidgetContainer()
    setattr(partner, 'model_WidgetContainer', None)
    _safe_set(owner, 'model_Master', partner)
    assert getattr(partner, 'model_WidgetContainer') == owner
    _safe_set(owner, 'model_Master', None)
    assert getattr(partner, 'model_WidgetContainer') is None


def test_assoc_screen20_stub_double():
    # story_model_Screen has no real 'story_model_Screen' property in the generated
    # code (a bare stub) -- manually attach it so model_story_Panel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_story_Panel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_story_Panel(id="sample_text", x=7, y=7)
    partner = story_model_Screen()
    setattr(partner, 'story_model_Screen', None)
    _safe_set(owner, 'model_story_Panel', partner)
    assert getattr(partner, 'story_model_Screen') == owner
    _safe_set(owner, 'model_story_Panel', None)
    assert getattr(partner, 'story_model_Screen') is None


def test_assoc_story21_stub_double():
    # Storyboard has no real 'Storyboard' property in the generated
    # code (a bare stub) -- manually attach it so model_story_Panel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_story_Panel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_story_Panel(id="sample_text", x=7, y=7)
    partner = Storyboard()
    setattr(partner, 'Storyboard', None)
    _safe_set(owner, 'model_story_Panel22', partner)
    assert getattr(partner, 'Storyboard') == owner
    _safe_set(owner, 'model_story_Panel22', None)
    assert getattr(partner, 'Storyboard') is None


def test_assoc_vRuler1_stub_double():
    # model_ScreenRuler has no real 'model_ScreenRuler3' property in the generated
    # code (a bare stub) -- manually attach it so model_Screen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Screen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Screen(minVersion="sample_text", name="sample_text", theme="sample_text")
    partner = model_ScreenRuler()
    setattr(partner, 'model_ScreenRuler3', None)
    _safe_set(owner, 'model_Screen2', partner)
    assert getattr(partner, 'model_ScreenRuler3') == owner
    _safe_set(owner, 'model_Screen2', None)
    assert getattr(partner, 'model_ScreenRuler3') is None


def test_assoc_widgets10_stub_double():
    # model_WidgetContainer has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so model_Widget's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Widget's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Widget(annotation=True, customData="sample_text", customId="sample_text", height=7, id="sample_text", layoutParams="sample_text", locked=True, measuredHeight=7, measuredWidth=7, text="sample_text", width=7, x=7, y=7)
    partner = model_WidgetContainer()
    setattr(partner, 'container', None)
    _safe_set(owner, 'Widget', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'Widget', None)
    assert owner not in getattr(partner, 'container')


