from python_code import model_Arrow

def test_model_Arrow___init__():
    assert model_Arrow.__init__(model_Arrow(False, False, '\x00\x00'), False, False, '') == None


from python_code import model_BooleanSelectionSupport

def test_model_BooleanSelectionSupport___init__():
    assert model_BooleanSelectionSupport.__init__(model_BooleanSelectionSupport(True), False) == None


from python_code import model_BorderStyleSupport

def test_model_BorderStyleSupport___init__():
    assert model_BorderStyleSupport.__init__(model_BorderStyleSupport(''), '') == None


from python_code import model_BorderSupport

def test_model_BorderSupport___init__():
    assert model_BorderSupport.__init__(model_BorderSupport(True), False) == None


from python_code import model_Button

def test_model_Button___init__():
    assert model_Button.__init__(model_Button(''), '') == None


from python_code import model_Chart

def test_model_Chart___init__():
    assert model_Chart.__init__(model_Chart(''), '') == None


from python_code import model_ClickSupport

def test_model_ClickSupport___init__():
    assert model_ClickSupport.__init__(model_ClickSupport()) == None

def test_model_ClickSupport_doClick():
    assert model_ClickSupport.doClick(model_ClickSupport()) == None


from python_code import model_ColorAlphaSupport

def test_model_ColorAlphaSupport___init__():
    assert model_ColorAlphaSupport.__init__(model_ColorAlphaSupport(0), 0) == None


from python_code import model_ColorAlternativeSupport

def test_model_ColorAlternativeSupport___init__():
    assert model_ColorAlternativeSupport.__init__(model_ColorAlternativeSupport(''), '') == None


from python_code import model_ColorBackgroundSupport

def test_model_ColorBackgroundSupport___init__():
    assert model_ColorBackgroundSupport.__init__(model_ColorBackgroundSupport(''), '') == None


from python_code import model_ColorBorderSupport

def test_model_ColorBorderSupport___init__():
    assert model_ColorBorderSupport.__init__(model_ColorBorderSupport(''), '') == None


from python_code import model_ColorForegroundSupport

def test_model_ColorForegroundSupport___init__():
    assert model_ColorForegroundSupport.__init__(model_ColorForegroundSupport(''), '') == None


from python_code import model_CurlyBrace

def test_model_CurlyBrace___init__():
    assert model_CurlyBrace.__init__(model_CurlyBrace(''), '') == None


from python_code import model_DoubleClickSupport

def test_model_DoubleClickSupport___init__():
    assert model_DoubleClickSupport.__init__(model_DoubleClickSupport()) == None

def test_model_DoubleClickSupport_doDoubleClick():
    assert model_DoubleClickSupport.doDoubleClick(model_DoubleClickSupport()) == None


from python_code import model_FlipSupport

def test_model_FlipSupport___init__():
    assert model_FlipSupport.__init__(model_FlipSupport(False, False), False, False) == None


from python_code import model_Font
from python_code import model_FontSupport

def test_model_Font___init__():
    assert model_Font.__init__(model_Font('\x00\x00', '', '', '', model_Font=model_FontSupport()), '', '', '', '', model_Font=model_FontSupport()) == None


from python_code import model_IconPositionSupport

def test_model_IconPositionSupport___init__():
    assert model_IconPositionSupport.__init__(model_IconPositionSupport(''), '') == None


from python_code import model_IconSupport

def test_model_IconSupport___init__():
    assert model_IconSupport.__init__(model_IconSupport('', '\x00'), '\x00\x00', '') == None


from python_code import model_Image

def test_model_Image___init__():
    assert model_Image.__init__(model_Image('', False), '', False) == None


from python_code import model_Item
from python_code import model_ItemSupport

def test_model_Item___init__():
    assert model_Item.__init__(model_Item('', 0, 0, 0, 0, model_Item=model_ItemSupport()), '', 0, 0, 0, 0, model_Item=model_ItemSupport()) == None


from python_code import model_LineHeightSupport

def test_model_LineHeightSupport___init__():
    assert model_LineHeightSupport.__init__(model_LineHeightSupport(''), '') == None


from python_code import model_LineStyleSupport

def test_model_LineStyleSupport___init__():
    assert model_LineStyleSupport.__init__(model_LineStyleSupport(''), '') == None


from python_code import model_LinkSupport

def test_model_LinkSupport___init__():
    assert model_LinkSupport.__init__(model_LinkSupport(''), '') == None


from python_code import model_List

def test_model_List___init__():
    assert model_List.__init__(model_List(True), False) == None


from python_code import model_ListSupport

def test_model_ListSupport___init__():
    assert model_ListSupport.__init__(model_ListSupport(0, False), 0, False) == None


from python_code import Overrides
from python_code import model_Master
from python_code import model_WidgetContainer

def test_model_Master___init__():
    assert model_Master.__init__(model_Master(True, model_Master15=model_WidgetContainer(), model_Master=model_WidgetContainer(), model_Master13=Overrides()), False, model_Master15=model_WidgetContainer(), model_Master=model_WidgetContainer(), model_Master13=Overrides()) == None


from python_code import model_NameSupport

def test_model_NameSupport___init__():
    assert model_NameSupport.__init__(model_NameSupport(''), '') == None


from python_code import model_NoteSupport

def test_model_NoteSupport___init__():
    assert model_NoteSupport.__init__(model_NoteSupport(''), '') == None


from python_code import model_RotationSupport

def test_model_RotationSupport___init__():
    assert model_RotationSupport.__init__(model_RotationSupport(''), '') == None


from python_code import model_RulerGuide
from python_code import model_ScreenRuler

def test_model_RulerGuide___init__():
    assert model_RulerGuide.__init__(model_RulerGuide(0, model_RulerGuide=model_ScreenRuler()), 0, model_RulerGuide=model_ScreenRuler()) == None


from python_code import model_SVGImage

def test_model_SVGImage___init__():
    assert model_SVGImage.__init__(model_SVGImage(''), '') == None


from python_code import model_SelectionSupport

def test_model_SelectionSupport___init__():
    assert model_SelectionSupport.__init__(model_SelectionSupport(''), '') == None

def test_model_SelectionSupport_doSelect():
    assert model_SelectionSupport.doSelect(model_SelectionSupport('')) == None


from python_code import model_Shape

def test_model_Shape___init__():
    assert model_Shape.__init__(model_Shape(''), '') == None

def test_model_Shape_isRotatable():
    assert model_Shape.isRotatable(model_Shape('')) == None


from python_code import model_SkinSupport

def test_model_SkinSupport___init__():
    assert model_SkinSupport.__init__(model_SkinSupport(''), '') == None


from python_code import model_StateSupport

def test_model_StateSupport___init__():
    assert model_StateSupport.__init__(model_StateSupport(''), '') == None

def test_model_StateSupport_isValidState():
    assert model_StateSupport.isValidState(model_StateSupport(''), 0) == None


from python_code import model_TabbedPane

def test_model_TabbedPane___init__():
    assert model_TabbedPane.__init__(model_TabbedPane(''), '') == None


from python_code import model_Table

def test_model_Table___init__():
    assert model_Table.__init__(model_Table(False, False), False, False) == None


from python_code import model_Text

def test_model_Text___init__():
    assert model_Text.__init__(model_Text(True), False) == None


from python_code import model_TextAlignmentSupport

def test_model_TextAlignmentSupport___init__():
    assert model_TextAlignmentSupport.__init__(model_TextAlignmentSupport(''), '') == None


from python_code import model_TextInputSupport

def test_model_TextInputSupport___init__():
    assert model_TextInputSupport.__init__(model_TextInputSupport()) == None

def test_model_TextInputSupport_doEnter():
    assert model_TextInputSupport.doEnter(model_TextInputSupport()) == None


from python_code import model_Tooltip

def test_model_Tooltip___init__():
    assert model_Tooltip.__init__(model_Tooltip(''), '') == None


from python_code import model_ValueSupport

def test_model_ValueSupport___init__():
    assert model_ValueSupport.__init__(model_ValueSupport(0), 0) == None


from python_code import model_VerticalScrollbarSupport

def test_model_VerticalScrollbarSupport___init__():
    assert model_VerticalScrollbarSupport.__init__(model_VerticalScrollbarSupport(True), False) == None


from python_code import model_VisibleSupport

def test_model_VisibleSupport___init__():
    assert model_VisibleSupport.__init__(model_VisibleSupport(True), False) == None


from python_code import model_Window

def test_model_Window___init__():
    assert model_Window.__init__(model_Window(False, False, False), False, False, False) == None


from python_code import model_overrides_FontOverrides

def test_model_overrides_FontOverrides___init__():
    assert model_overrides_FontOverrides.__init__(model_overrides_FontOverrides('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import FontOverrides
from python_code import model_overrides_Insert
from python_code import model_overrides_WidgetContainerOverrides
from python_code import model_overrides_WidgetOverrides
from python_code import overrides_model_EObject

def test_model_overrides_Insert___init__():
    assert model_overrides_Insert.__init__(model_overrides_Insert(0, model_overrides_Insert=overrides_model_EObject(), Operation=model_overrides_WidgetOverrides('', '\x00', '\x00', '', '', '', False, '', False, model_overrides_WidgetOverrides=set(), model_overrides_WidgetOverrides26=FontOverrides(), model_overrides_WidgetOverrides28=set(), model_overrides_WidgetOverrides30=set()), Operation33=model_overrides_WidgetContainerOverrides()), 0, model_overrides_Insert=overrides_model_EObject(), Operation=model_overrides_WidgetOverrides('', '', '', '', '', '', False, '', False, model_overrides_WidgetOverrides=set(), model_overrides_WidgetOverrides26=FontOverrides(), model_overrides_WidgetOverrides28=set(), model_overrides_WidgetOverrides30=set()), Operation33=model_overrides_WidgetContainerOverrides()) == None


from python_code import model_overrides_ItemOverrides

def test_model_overrides_ItemOverrides___init__():
    assert model_overrides_ItemOverrides.__init__(model_overrides_ItemOverrides('', '', False), '\x00', '', False) == None


from python_code import model_overrides_Move

def test_model_overrides_Move___init__():
    assert model_overrides_Move.__init__(model_overrides_Move(0), 0) == None


from python_code import model_overrides_Reference

def test_model_overrides_Reference___init__():
    assert model_overrides_Reference.__init__(model_overrides_Reference(''), '') == None


from python_code import model_overrides_StringToStringMap

def test_model_overrides_StringToStringMap___init__():
    assert model_overrides_StringToStringMap.__init__(model_overrides_StringToStringMap('', '\x00'), '\x00\x00', '') == None


from python_code import FontOverrides
from python_code import model_overrides_WidgetOverrides

def test_model_overrides_WidgetOverrides___init__():
    assert model_overrides_WidgetOverrides.__init__(model_overrides_WidgetOverrides('', '', '', '', '\x00', '', False, '', True, model_overrides_WidgetOverrides=set(), model_overrides_WidgetOverrides26=FontOverrides(), model_overrides_WidgetOverrides28=set(), model_overrides_WidgetOverrides30=set()), '', '', '', '', '', '', True, '', False, model_overrides_WidgetOverrides=set(), model_overrides_WidgetOverrides26=FontOverrides(), model_overrides_WidgetOverrides28=set(), model_overrides_WidgetOverrides30=set()) == None


from python_code import Storyboard
from python_code import model_story_Panel
from python_code import story_model_Screen

def test_model_story_Panel___init__():
    assert model_story_Panel.__init__(model_story_Panel('', 0, 0, model_story_Panel=story_model_Screen(), model_story_Panel22=Storyboard()), '\x00', 0, 0, model_story_Panel=story_model_Screen(), model_story_Panel22=Storyboard()) == None

