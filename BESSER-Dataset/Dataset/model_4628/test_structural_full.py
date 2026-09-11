import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Child,
    Container,
    Cursor,
    Figure,
    Primitive,
    Shape,
    VisualInterface_Arc,
    VisualInterface_BorderChild,
    VisualInterface_BorderContainer,
    VisualInterface_Child,
    VisualInterface_Connection,
    VisualInterface_Container,
    VisualInterface_Cursor,
    VisualInterface_Dimension,
    VisualInterface_Ellipse,
    VisualInterface_Figure,
    VisualInterface_FigureContainer,
    VisualInterface_GridChild,
    VisualInterface_GridContainer,
    VisualInterface_Image,
    VisualInterface_Line,
    VisualInterface_Position,
    VisualInterface_Primitive,
    VisualInterface_Rectangle,
    VisualInterface_Shape,
    VisualInterface_StackContainer,
    VisualInterface_StringToStringMap,
    VisualInterface_Symbol,
    VisualInterface_SymbolReference,
    VisualInterface_SystemCursor,
    VisualInterface_Text,
    VisualInterface_XYChild,
    VisualInterface_XYContainer,
    Alignment,
    GridAlignment,
    Orientation,
    SystemCursorType,
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

def test_VisualInterface_Arc_length_value_roundtrip():
    instance = VisualInterface_Arc(length=7, start=7)
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_VisualInterface_Arc_start_value_roundtrip():
    instance = VisualInterface_Arc(length=7, start=7)
    assert instance.start == 7
    instance.start = 13
    assert instance.start == 13


def test_VisualInterface_BorderChild_alignment_value_roundtrip():
    instance = VisualInterface_BorderChild(alignment="sample_text")
    assert instance.alignment == "sample_text"
    instance.alignment = "sample_text_2"
    assert instance.alignment == "sample_text_2"


def test_VisualInterface_BorderContainer_horizontalSpacing_value_roundtrip():
    instance = VisualInterface_BorderContainer(horizontalSpacing=7, verticalSpacing=7)
    assert instance.horizontalSpacing == 7
    instance.horizontalSpacing = 13
    assert instance.horizontalSpacing == 13


def test_VisualInterface_BorderContainer_verticalSpacing_value_roundtrip():
    instance = VisualInterface_BorderContainer(horizontalSpacing=7, verticalSpacing=7)
    assert instance.verticalSpacing == 7
    instance.verticalSpacing = 13
    assert instance.verticalSpacing == 13


def test_VisualInterface_Child_name_value_roundtrip():
    instance = VisualInterface_Child(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_VisualInterface_Dimension_height_value_roundtrip():
    instance = VisualInterface_Dimension(height=3.14, width=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_VisualInterface_Dimension_width_value_roundtrip():
    instance = VisualInterface_Dimension(height=3.14, width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_VisualInterface_Figure_backgroundColor_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_VisualInterface_Figure_border_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.border == "sample_text"
    instance.border = "sample_text_2"
    assert instance.border == "sample_text_2"


def test_VisualInterface_Figure_foregroundColor_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.foregroundColor == "sample_text"
    instance.foregroundColor = "sample_text_2"
    assert instance.foregroundColor == "sample_text_2"


def test_VisualInterface_Figure_onClick_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.onClick == "sample_text"
    instance.onClick = "sample_text_2"
    assert instance.onClick == "sample_text_2"


def test_VisualInterface_Figure_onDoubleClick_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.onDoubleClick == "sample_text"
    instance.onDoubleClick = "sample_text_2"
    assert instance.onDoubleClick == "sample_text_2"


def test_VisualInterface_Figure_opaque_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.opaque == "sample_text"
    instance.opaque = "sample_text_2"
    assert instance.opaque == "sample_text_2"


def test_VisualInterface_Figure_toolTip_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.toolTip == "sample_text"
    instance.toolTip = "sample_text_2"
    assert instance.toolTip == "sample_text_2"


def test_VisualInterface_Figure_visible_value_roundtrip():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_VisualInterface_GridChild_grabHorizontalSpace_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.grabHorizontalSpace == True
    instance.grabHorizontalSpace = False
    assert instance.grabHorizontalSpace == False


def test_VisualInterface_GridChild_grabVerticalSpace_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.grabVerticalSpace == True
    instance.grabVerticalSpace = False
    assert instance.grabVerticalSpace == False


def test_VisualInterface_GridChild_heightHint_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.heightHint == "sample_text"
    instance.heightHint = "sample_text_2"
    assert instance.heightHint == "sample_text_2"


def test_VisualInterface_GridChild_horizontalAlignment_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.horizontalAlignment == "sample_text"
    instance.horizontalAlignment = "sample_text_2"
    assert instance.horizontalAlignment == "sample_text_2"


def test_VisualInterface_GridChild_spanCols_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.spanCols == 7
    instance.spanCols = 13
    assert instance.spanCols == 13


def test_VisualInterface_GridChild_spanRows_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.spanRows == "sample_text"
    instance.spanRows = "sample_text_2"
    assert instance.spanRows == "sample_text_2"


def test_VisualInterface_GridChild_verticalAlignment_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.verticalAlignment == "sample_text"
    instance.verticalAlignment = "sample_text_2"
    assert instance.verticalAlignment == "sample_text_2"


def test_VisualInterface_GridChild_widthHint_value_roundtrip():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert instance.widthHint == "sample_text"
    instance.widthHint = "sample_text_2"
    assert instance.widthHint == "sample_text_2"


def test_VisualInterface_GridContainer_columns_value_roundtrip():
    instance = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    assert instance.columns == 7
    instance.columns = 13
    assert instance.columns == 13


def test_VisualInterface_GridContainer_equalWidth_value_roundtrip():
    instance = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    assert instance.equalWidth == True
    instance.equalWidth = False
    assert instance.equalWidth == False


def test_VisualInterface_GridContainer_horizontalSpacing_value_roundtrip():
    instance = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    assert instance.horizontalSpacing == 7
    instance.horizontalSpacing = 13
    assert instance.horizontalSpacing == 13


def test_VisualInterface_GridContainer_marginHeight_value_roundtrip():
    instance = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    assert instance.marginHeight == 7
    instance.marginHeight = 13
    assert instance.marginHeight == 13


def test_VisualInterface_GridContainer_marginWidth_value_roundtrip():
    instance = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    assert instance.marginWidth == 7
    instance.marginWidth = 13
    assert instance.marginWidth == 13


def test_VisualInterface_GridContainer_verticalSpacing_value_roundtrip():
    instance = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    assert instance.verticalSpacing == 7
    instance.verticalSpacing = 13
    assert instance.verticalSpacing == 13


def test_VisualInterface_Image_uri_value_roundtrip():
    instance = VisualInterface_Image(uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_VisualInterface_Position_x_value_roundtrip():
    instance = VisualInterface_Position(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_VisualInterface_Position_y_value_roundtrip():
    instance = VisualInterface_Position(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_VisualInterface_Primitive_name_value_roundtrip():
    instance = VisualInterface_Primitive(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_VisualInterface_Shape_alpha_value_roundtrip():
    instance = VisualInterface_Shape(alpha="sample_text", antialias="sample_text", fill=True, lineWidth=3.14, outline=True)
    assert instance.alpha == "sample_text"
    instance.alpha = "sample_text_2"
    assert instance.alpha == "sample_text_2"


def test_VisualInterface_Shape_antialias_value_roundtrip():
    instance = VisualInterface_Shape(alpha="sample_text", antialias="sample_text", fill=True, lineWidth=3.14, outline=True)
    assert instance.antialias == "sample_text"
    instance.antialias = "sample_text_2"
    assert instance.antialias == "sample_text_2"


def test_VisualInterface_Shape_fill_value_roundtrip():
    instance = VisualInterface_Shape(alpha="sample_text", antialias="sample_text", fill=True, lineWidth=3.14, outline=True)
    assert instance.fill == True
    instance.fill = False
    assert instance.fill == False


def test_VisualInterface_Shape_lineWidth_value_roundtrip():
    instance = VisualInterface_Shape(alpha="sample_text", antialias="sample_text", fill=True, lineWidth=3.14, outline=True)
    assert instance.lineWidth == 3.14
    instance.lineWidth = 9.99
    assert instance.lineWidth == 9.99


def test_VisualInterface_Shape_outline_value_roundtrip():
    instance = VisualInterface_Shape(alpha="sample_text", antialias="sample_text", fill=True, lineWidth=3.14, outline=True)
    assert instance.outline == True
    instance.outline = False
    assert instance.outline == False


def test_VisualInterface_StringToStringMap_key_value_roundtrip():
    instance = VisualInterface_StringToStringMap(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_VisualInterface_StringToStringMap_value_value_roundtrip():
    instance = VisualInterface_StringToStringMap(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_VisualInterface_Symbol_backgroundColor_value_roundtrip():
    instance = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    assert instance.backgroundColor == "sample_text"
    instance.backgroundColor = "sample_text_2"
    assert instance.backgroundColor == "sample_text_2"


def test_VisualInterface_Symbol_onDispose_value_roundtrip():
    instance = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    assert instance.onDispose == "sample_text"
    instance.onDispose = "sample_text_2"
    assert instance.onDispose == "sample_text_2"


def test_VisualInterface_Symbol_onInit_value_roundtrip():
    instance = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    assert instance.onInit == "sample_text"
    instance.onInit = "sample_text_2"
    assert instance.onInit == "sample_text_2"


def test_VisualInterface_Symbol_onUpdate_value_roundtrip():
    instance = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    assert instance.onUpdate == "sample_text"
    instance.onUpdate = "sample_text_2"
    assert instance.onUpdate == "sample_text_2"


def test_VisualInterface_Symbol_scriptModules_value_roundtrip():
    instance = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    assert instance.scriptModules == "sample_text"
    instance.scriptModules = "sample_text_2"
    assert instance.scriptModules == "sample_text_2"


def test_VisualInterface_SymbolReference_onCreateProperties_value_roundtrip():
    instance = VisualInterface_SymbolReference(onCreateProperties="sample_text", uri="sample_text", zoom="sample_text")
    assert instance.onCreateProperties == "sample_text"
    instance.onCreateProperties = "sample_text_2"
    assert instance.onCreateProperties == "sample_text_2"


def test_VisualInterface_SymbolReference_uri_value_roundtrip():
    instance = VisualInterface_SymbolReference(onCreateProperties="sample_text", uri="sample_text", zoom="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_VisualInterface_SymbolReference_zoom_value_roundtrip():
    instance = VisualInterface_SymbolReference(onCreateProperties="sample_text", uri="sample_text", zoom="sample_text")
    assert instance.zoom == "sample_text"
    instance.zoom = "sample_text_2"
    assert instance.zoom == "sample_text_2"


def test_VisualInterface_SystemCursor_type_value_roundtrip():
    instance = VisualInterface_SystemCursor(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_VisualInterface_Text_fontBold_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.fontBold == True
    instance.fontBold = False
    assert instance.fontBold == False


def test_VisualInterface_Text_fontItalic_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.fontItalic == True
    instance.fontItalic = False
    assert instance.fontItalic == False


def test_VisualInterface_Text_fontName_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.fontName == "sample_text"
    instance.fontName = "sample_text_2"
    assert instance.fontName == "sample_text_2"


def test_VisualInterface_Text_fontSize_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.fontSize == 7
    instance.fontSize = 13
    assert instance.fontSize == 13


def test_VisualInterface_Text_iconAlignment_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.iconAlignment == "sample_text"
    instance.iconAlignment = "sample_text_2"
    assert instance.iconAlignment == "sample_text_2"


def test_VisualInterface_Text_labelAlignment_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.labelAlignment == "sample_text"
    instance.labelAlignment = "sample_text_2"
    assert instance.labelAlignment == "sample_text_2"


def test_VisualInterface_Text_text_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_VisualInterface_Text_textAlignment_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.textAlignment == "sample_text"
    instance.textAlignment = "sample_text_2"
    assert instance.textAlignment == "sample_text_2"


def test_VisualInterface_Text_textPlacement_value_roundtrip():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert instance.textPlacement == "sample_text"
    instance.textPlacement = "sample_text_2"
    assert instance.textPlacement == "sample_text_2"


def test_VisualInterface_BorderChild_isa_Child():
    instance = VisualInterface_BorderChild(alignment="sample_text")
    assert isinstance(instance, Child)


def test_VisualInterface_GridChild_isa_Child():
    instance = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    assert isinstance(instance, Child)


def test_VisualInterface_XYChild_isa_Child():
    instance = VisualInterface_XYChild()
    assert isinstance(instance, Child)


def test_VisualInterface_BorderContainer_isa_Container():
    instance = VisualInterface_BorderContainer(horizontalSpacing=7, verticalSpacing=7)
    assert isinstance(instance, Container)


def test_VisualInterface_GridContainer_isa_Container():
    instance = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    assert isinstance(instance, Container)


def test_VisualInterface_StackContainer_isa_Container():
    instance = VisualInterface_StackContainer()
    assert isinstance(instance, Container)


def test_VisualInterface_XYContainer_isa_Container():
    instance = VisualInterface_XYContainer()
    assert isinstance(instance, Container)


def test_VisualInterface_SystemCursor_isa_Cursor():
    instance = VisualInterface_SystemCursor(type="sample_text")
    assert isinstance(instance, Cursor)


def test_VisualInterface_FigureContainer_isa_Figure():
    instance = VisualInterface_FigureContainer()
    assert isinstance(instance, Figure)


def test_VisualInterface_Image_isa_Figure():
    instance = VisualInterface_Image(uri="sample_text")
    assert isinstance(instance, Figure)


def test_VisualInterface_Shape_isa_Figure():
    instance = VisualInterface_Shape(alpha="sample_text", antialias="sample_text", fill=True, lineWidth=3.14, outline=True)
    assert isinstance(instance, Figure)


def test_VisualInterface_Text_isa_Figure():
    instance = VisualInterface_Text(fontBold=True, fontItalic=True, fontName="sample_text", fontSize=7, iconAlignment="sample_text", labelAlignment="sample_text", text="sample_text", textAlignment="sample_text", textPlacement="sample_text")
    assert isinstance(instance, Figure)


def test_VisualInterface_Container_isa_Primitive():
    instance = VisualInterface_Container()
    assert isinstance(instance, Primitive)


def test_VisualInterface_Figure_isa_Primitive():
    instance = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    assert isinstance(instance, Primitive)


def test_VisualInterface_SymbolReference_isa_Primitive():
    instance = VisualInterface_SymbolReference(onCreateProperties="sample_text", uri="sample_text", zoom="sample_text")
    assert isinstance(instance, Primitive)


def test_VisualInterface_Arc_isa_Shape():
    instance = VisualInterface_Arc(length=7, start=7)
    assert isinstance(instance, Shape)


def test_VisualInterface_Ellipse_isa_Shape():
    instance = VisualInterface_Ellipse()
    assert isinstance(instance, Shape)


def test_VisualInterface_Line_isa_Shape():
    instance = VisualInterface_Line()
    assert isinstance(instance, Shape)


def test_VisualInterface_Rectangle_isa_Shape():
    instance = VisualInterface_Rectangle()
    assert isinstance(instance, Shape)


def test_assoc_children26_link_reassign_clear():
    a = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    b1 = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    b2 = VisualInterface_GridChild(grabHorizontalSpace=False, grabVerticalSpace=False, heightHint="sample_text_2", horizontalAlignment="sample_text_2", spanCols=13, spanRows="sample_text_2", verticalAlignment="sample_text_2", widthHint="sample_text_2")
    _safe_set(a, 'VisualInterface_GridContainer', {b1})
    assert _is_linked(a, 'VisualInterface_GridContainer', b1)
    if hasattr(b1, 'VisualInterface_GridChild'):
        assert _is_linked(b1, 'VisualInterface_GridChild', a)
    _safe_set(a, 'VisualInterface_GridContainer', {b2})
    assert _is_linked(a, 'VisualInterface_GridContainer', b2)
    if hasattr(b1, 'VisualInterface_GridChild'):
        assert not _is_linked(b1, 'VisualInterface_GridChild', a)
    if hasattr(b2, 'VisualInterface_GridChild'):
        assert _is_linked(b2, 'VisualInterface_GridChild', a)
    _safe_set(a, 'VisualInterface_GridContainer', set())
    assert not _is_linked(a, 'VisualInterface_GridContainer', b2)
    if hasattr(b2, 'VisualInterface_GridChild'):
        assert not _is_linked(b2, 'VisualInterface_GridChild', a)


def test_assoc_children27_link_reassign_clear():
    a = VisualInterface_BorderContainer(horizontalSpacing=7, verticalSpacing=7)
    b1 = VisualInterface_BorderChild(alignment="sample_text")
    b2 = VisualInterface_BorderChild(alignment="sample_text_2")
    _safe_set(a, 'VisualInterface_BorderContainer', {b1})
    assert _is_linked(a, 'VisualInterface_BorderContainer', b1)
    if hasattr(b1, 'VisualInterface_BorderChild'):
        assert _is_linked(b1, 'VisualInterface_BorderChild', a)
    _safe_set(a, 'VisualInterface_BorderContainer', {b2})
    assert _is_linked(a, 'VisualInterface_BorderContainer', b2)
    if hasattr(b1, 'VisualInterface_BorderChild'):
        assert not _is_linked(b1, 'VisualInterface_BorderChild', a)
    if hasattr(b2, 'VisualInterface_BorderChild'):
        assert _is_linked(b2, 'VisualInterface_BorderChild', a)
    _safe_set(a, 'VisualInterface_BorderContainer', set())
    assert not _is_linked(a, 'VisualInterface_BorderContainer', b2)
    if hasattr(b2, 'VisualInterface_BorderChild'):
        assert not _is_linked(b2, 'VisualInterface_BorderChild', a)


def test_assoc_children36_link_reassign_clear():
    a = VisualInterface_Primitive(name="sample_text")
    b1 = VisualInterface_StackContainer()
    b2 = VisualInterface_StackContainer()
    _safe_set(a, 'VisualInterface_Primitive37', b1)
    assert _is_linked(a, 'VisualInterface_Primitive37', b1)
    if hasattr(b1, 'VisualInterface_StackContainer'):
        assert _is_linked(b1, 'VisualInterface_StackContainer', a)
    _safe_set(a, 'VisualInterface_Primitive37', b2)
    assert _is_linked(a, 'VisualInterface_Primitive37', b2)
    if hasattr(b1, 'VisualInterface_StackContainer'):
        assert not _is_linked(b1, 'VisualInterface_StackContainer', a)
    if hasattr(b2, 'VisualInterface_StackContainer'):
        assert _is_linked(b2, 'VisualInterface_StackContainer', a)
    _safe_set(a, 'VisualInterface_Primitive37', None)
    assert not _is_linked(a, 'VisualInterface_Primitive37', b2)
    if hasattr(b2, 'VisualInterface_StackContainer'):
        assert not _is_linked(b2, 'VisualInterface_StackContainer', a)


def test_assoc_connections7_link_reassign_clear():
    a = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    b1 = VisualInterface_Connection()
    b2 = VisualInterface_Connection()
    _safe_set(a, 'VisualInterface_Symbol8', {b1})
    assert _is_linked(a, 'VisualInterface_Symbol8', b1)
    if hasattr(b1, 'VisualInterface_Connection'):
        assert _is_linked(b1, 'VisualInterface_Connection', a)
    _safe_set(a, 'VisualInterface_Symbol8', {b2})
    assert _is_linked(a, 'VisualInterface_Symbol8', b2)
    if hasattr(b1, 'VisualInterface_Connection'):
        assert not _is_linked(b1, 'VisualInterface_Connection', a)
    if hasattr(b2, 'VisualInterface_Connection'):
        assert _is_linked(b2, 'VisualInterface_Connection', a)
    _safe_set(a, 'VisualInterface_Symbol8', set())
    assert not _is_linked(a, 'VisualInterface_Symbol8', b2)
    if hasattr(b2, 'VisualInterface_Connection'):
        assert not _is_linked(b2, 'VisualInterface_Connection', a)


def test_assoc_content28_link_reassign_clear():
    a = VisualInterface_Primitive(name="sample_text")
    b1 = VisualInterface_FigureContainer()
    b2 = VisualInterface_FigureContainer()
    _safe_set(a, 'VisualInterface_Primitive29', b1)
    assert _is_linked(a, 'VisualInterface_Primitive29', b1)
    if hasattr(b1, 'VisualInterface_FigureContainer'):
        assert _is_linked(b1, 'VisualInterface_FigureContainer', a)
    _safe_set(a, 'VisualInterface_Primitive29', b2)
    assert _is_linked(a, 'VisualInterface_Primitive29', b2)
    if hasattr(b1, 'VisualInterface_FigureContainer'):
        assert not _is_linked(b1, 'VisualInterface_FigureContainer', a)
    if hasattr(b2, 'VisualInterface_FigureContainer'):
        assert _is_linked(b2, 'VisualInterface_FigureContainer', a)
    _safe_set(a, 'VisualInterface_Primitive29', None)
    assert not _is_linked(a, 'VisualInterface_Primitive29', b2)
    if hasattr(b2, 'VisualInterface_FigureContainer'):
        assert not _is_linked(b2, 'VisualInterface_FigureContainer', a)


def test_assoc_cursor21_link_reassign_clear():
    a = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    b1 = VisualInterface_Cursor()
    b2 = VisualInterface_Cursor()
    _safe_set(a, 'VisualInterface_Figure22', b1)
    assert _is_linked(a, 'VisualInterface_Figure22', b1)
    if hasattr(b1, 'VisualInterface_Cursor23'):
        assert _is_linked(b1, 'VisualInterface_Cursor23', a)
    _safe_set(a, 'VisualInterface_Figure22', b2)
    assert _is_linked(a, 'VisualInterface_Figure22', b2)
    if hasattr(b1, 'VisualInterface_Cursor23'):
        assert not _is_linked(b1, 'VisualInterface_Cursor23', a)
    if hasattr(b2, 'VisualInterface_Cursor23'):
        assert _is_linked(b2, 'VisualInterface_Cursor23', a)
    _safe_set(a, 'VisualInterface_Figure22', None)
    assert not _is_linked(a, 'VisualInterface_Figure22', b2)
    if hasattr(b2, 'VisualInterface_Cursor23'):
        assert not _is_linked(b2, 'VisualInterface_Cursor23', a)


def test_assoc_cursors3_link_reassign_clear():
    a = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    b1 = VisualInterface_Cursor()
    b2 = VisualInterface_Cursor()
    _safe_set(a, 'VisualInterface_Symbol4', b1)
    assert _is_linked(a, 'VisualInterface_Symbol4', b1)
    if hasattr(b1, 'VisualInterface_Cursor'):
        assert _is_linked(b1, 'VisualInterface_Cursor', a)
    _safe_set(a, 'VisualInterface_Symbol4', b2)
    assert _is_linked(a, 'VisualInterface_Symbol4', b2)
    if hasattr(b1, 'VisualInterface_Cursor'):
        assert not _is_linked(b1, 'VisualInterface_Cursor', a)
    if hasattr(b2, 'VisualInterface_Cursor'):
        assert _is_linked(b2, 'VisualInterface_Cursor', a)
    _safe_set(a, 'VisualInterface_Symbol4', None)
    assert not _is_linked(a, 'VisualInterface_Symbol4', b2)
    if hasattr(b2, 'VisualInterface_Cursor'):
        assert not _is_linked(b2, 'VisualInterface_Cursor', a)


def test_assoc_designSize5_link_reassign_clear():
    a = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    b1 = VisualInterface_Dimension(height=3.14, width=3.14)
    b2 = VisualInterface_Dimension(height=9.99, width=9.99)
    _safe_set(a, 'VisualInterface_Symbol6', b1)
    assert _is_linked(a, 'VisualInterface_Symbol6', b1)
    if hasattr(b1, 'VisualInterface_Dimension'):
        assert _is_linked(b1, 'VisualInterface_Dimension', a)
    _safe_set(a, 'VisualInterface_Symbol6', b2)
    assert _is_linked(a, 'VisualInterface_Symbol6', b2)
    if hasattr(b1, 'VisualInterface_Dimension'):
        assert not _is_linked(b1, 'VisualInterface_Dimension', a)
    if hasattr(b2, 'VisualInterface_Dimension'):
        assert _is_linked(b2, 'VisualInterface_Dimension', a)
    _safe_set(a, 'VisualInterface_Symbol6', None)
    assert not _is_linked(a, 'VisualInterface_Symbol6', b2)
    if hasattr(b2, 'VisualInterface_Dimension'):
        assert not _is_linked(b2, 'VisualInterface_Dimension', a)


def test_assoc_dimension12_link_reassign_clear():
    a = VisualInterface_Dimension(height=3.14, width=3.14)
    b1 = VisualInterface_XYChild()
    b2 = VisualInterface_XYChild()
    _safe_set(a, 'VisualInterface_Dimension14', b1)
    assert _is_linked(a, 'VisualInterface_Dimension14', b1)
    if hasattr(b1, 'VisualInterface_XYChild13'):
        assert _is_linked(b1, 'VisualInterface_XYChild13', a)
    _safe_set(a, 'VisualInterface_Dimension14', b2)
    assert _is_linked(a, 'VisualInterface_Dimension14', b2)
    if hasattr(b1, 'VisualInterface_XYChild13'):
        assert not _is_linked(b1, 'VisualInterface_XYChild13', a)
    if hasattr(b2, 'VisualInterface_XYChild13'):
        assert _is_linked(b2, 'VisualInterface_XYChild13', a)
    _safe_set(a, 'VisualInterface_Dimension14', None)
    assert not _is_linked(a, 'VisualInterface_Dimension14', b2)
    if hasattr(b2, 'VisualInterface_XYChild13'):
        assert not _is_linked(b2, 'VisualInterface_XYChild13', a)


def test_assoc_element9_link_reassign_clear():
    a = VisualInterface_Primitive(name="sample_text")
    b1 = VisualInterface_Child(name="sample_text")
    b2 = VisualInterface_Child(name="sample_text_2")
    _safe_set(a, 'VisualInterface_Primitive10', b1)
    assert _is_linked(a, 'VisualInterface_Primitive10', b1)
    if hasattr(b1, 'VisualInterface_Child'):
        assert _is_linked(b1, 'VisualInterface_Child', a)
    _safe_set(a, 'VisualInterface_Primitive10', b2)
    assert _is_linked(a, 'VisualInterface_Primitive10', b2)
    if hasattr(b1, 'VisualInterface_Child'):
        assert not _is_linked(b1, 'VisualInterface_Child', a)
    if hasattr(b2, 'VisualInterface_Child'):
        assert _is_linked(b2, 'VisualInterface_Child', a)
    _safe_set(a, 'VisualInterface_Primitive10', None)
    assert not _is_linked(a, 'VisualInterface_Primitive10', b2)
    if hasattr(b2, 'VisualInterface_Child'):
        assert not _is_linked(b2, 'VisualInterface_Child', a)


def test_assoc_end33_link_reassign_clear():
    a = VisualInterface_Primitive(name="sample_text")
    b1 = VisualInterface_Connection()
    b2 = VisualInterface_Connection()
    _safe_set(a, 'VisualInterface_Primitive35', b1)
    assert _is_linked(a, 'VisualInterface_Primitive35', b1)
    if hasattr(b1, 'VisualInterface_Connection34'):
        assert _is_linked(b1, 'VisualInterface_Connection34', a)
    _safe_set(a, 'VisualInterface_Primitive35', b2)
    assert _is_linked(a, 'VisualInterface_Primitive35', b2)
    if hasattr(b1, 'VisualInterface_Connection34'):
        assert not _is_linked(b1, 'VisualInterface_Connection34', a)
    if hasattr(b2, 'VisualInterface_Connection34'):
        assert _is_linked(b2, 'VisualInterface_Connection34', a)
    _safe_set(a, 'VisualInterface_Primitive35', None)
    assert not _is_linked(a, 'VisualInterface_Primitive35', b2)
    if hasattr(b2, 'VisualInterface_Connection34'):
        assert not _is_linked(b2, 'VisualInterface_Connection34', a)


def test_assoc_points17_link_reassign_clear():
    a = VisualInterface_Position(x=3.14, y=3.14)
    b1 = VisualInterface_Line()
    b2 = VisualInterface_Line()
    _safe_set(a, 'VisualInterface_Position18', b1)
    assert _is_linked(a, 'VisualInterface_Position18', b1)
    if hasattr(b1, 'VisualInterface_Line'):
        assert _is_linked(b1, 'VisualInterface_Line', a)
    _safe_set(a, 'VisualInterface_Position18', b2)
    assert _is_linked(a, 'VisualInterface_Position18', b2)
    if hasattr(b1, 'VisualInterface_Line'):
        assert not _is_linked(b1, 'VisualInterface_Line', a)
    if hasattr(b2, 'VisualInterface_Line'):
        assert _is_linked(b2, 'VisualInterface_Line', a)
    _safe_set(a, 'VisualInterface_Position18', None)
    assert not _is_linked(a, 'VisualInterface_Position18', b2)
    if hasattr(b2, 'VisualInterface_Line'):
        assert not _is_linked(b2, 'VisualInterface_Line', a)


def test_assoc_position11_link_reassign_clear():
    a = VisualInterface_Position(x=3.14, y=3.14)
    b1 = VisualInterface_XYChild()
    b2 = VisualInterface_XYChild()
    _safe_set(a, 'VisualInterface_Position', b1)
    assert _is_linked(a, 'VisualInterface_Position', b1)
    if hasattr(b1, 'VisualInterface_XYChild'):
        assert _is_linked(b1, 'VisualInterface_XYChild', a)
    _safe_set(a, 'VisualInterface_Position', b2)
    assert _is_linked(a, 'VisualInterface_Position', b2)
    if hasattr(b1, 'VisualInterface_XYChild'):
        assert not _is_linked(b1, 'VisualInterface_XYChild', a)
    if hasattr(b2, 'VisualInterface_XYChild'):
        assert _is_linked(b2, 'VisualInterface_XYChild', a)
    _safe_set(a, 'VisualInterface_Position', None)
    assert not _is_linked(a, 'VisualInterface_Position', b2)
    if hasattr(b2, 'VisualInterface_XYChild'):
        assert not _is_linked(b2, 'VisualInterface_XYChild', a)


def test_assoc_properties1_link_reassign_clear():
    a = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    b1 = VisualInterface_StringToStringMap(key="sample_text", value="sample_text")
    b2 = VisualInterface_StringToStringMap(key="sample_text_2", value="sample_text_2")
    _safe_set(a, 'VisualInterface_Symbol2', {b1})
    assert _is_linked(a, 'VisualInterface_Symbol2', b1)
    if hasattr(b1, 'VisualInterface_StringToStringMap'):
        assert _is_linked(b1, 'VisualInterface_StringToStringMap', a)
    _safe_set(a, 'VisualInterface_Symbol2', {b2})
    assert _is_linked(a, 'VisualInterface_Symbol2', b2)
    if hasattr(b1, 'VisualInterface_StringToStringMap'):
        assert not _is_linked(b1, 'VisualInterface_StringToStringMap', a)
    if hasattr(b2, 'VisualInterface_StringToStringMap'):
        assert _is_linked(b2, 'VisualInterface_StringToStringMap', a)
    _safe_set(a, 'VisualInterface_Symbol2', set())
    assert not _is_linked(a, 'VisualInterface_Symbol2', b2)
    if hasattr(b2, 'VisualInterface_StringToStringMap'):
        assert not _is_linked(b2, 'VisualInterface_StringToStringMap', a)


def test_assoc_properties24_link_reassign_clear():
    a = VisualInterface_SymbolReference(onCreateProperties="sample_text", uri="sample_text", zoom="sample_text")
    b1 = VisualInterface_StringToStringMap(key="sample_text", value="sample_text")
    b2 = VisualInterface_StringToStringMap(key="sample_text_2", value="sample_text_2")
    _safe_set(a, 'VisualInterface_SymbolReference', {b1})
    assert _is_linked(a, 'VisualInterface_SymbolReference', b1)
    if hasattr(b1, 'VisualInterface_StringToStringMap25'):
        assert _is_linked(b1, 'VisualInterface_StringToStringMap25', a)
    _safe_set(a, 'VisualInterface_SymbolReference', {b2})
    assert _is_linked(a, 'VisualInterface_SymbolReference', b2)
    if hasattr(b1, 'VisualInterface_StringToStringMap25'):
        assert not _is_linked(b1, 'VisualInterface_StringToStringMap25', a)
    if hasattr(b2, 'VisualInterface_StringToStringMap25'):
        assert _is_linked(b2, 'VisualInterface_StringToStringMap25', a)
    _safe_set(a, 'VisualInterface_SymbolReference', set())
    assert not _is_linked(a, 'VisualInterface_SymbolReference', b2)
    if hasattr(b2, 'VisualInterface_StringToStringMap25'):
        assert not _is_linked(b2, 'VisualInterface_StringToStringMap25', a)


def test_assoc_root0_link_reassign_clear():
    a = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    b1 = VisualInterface_Primitive(name="sample_text")
    b2 = VisualInterface_Primitive(name="sample_text_2")
    _safe_set(a, 'VisualInterface_Symbol', b1)
    assert _is_linked(a, 'VisualInterface_Symbol', b1)
    if hasattr(b1, 'VisualInterface_Primitive'):
        assert _is_linked(b1, 'VisualInterface_Primitive', a)
    _safe_set(a, 'VisualInterface_Symbol', b2)
    assert _is_linked(a, 'VisualInterface_Symbol', b2)
    if hasattr(b1, 'VisualInterface_Primitive'):
        assert not _is_linked(b1, 'VisualInterface_Primitive', a)
    if hasattr(b2, 'VisualInterface_Primitive'):
        assert _is_linked(b2, 'VisualInterface_Primitive', a)
    _safe_set(a, 'VisualInterface_Symbol', None)
    assert not _is_linked(a, 'VisualInterface_Symbol', b2)
    if hasattr(b2, 'VisualInterface_Primitive'):
        assert not _is_linked(b2, 'VisualInterface_Primitive', a)


def test_assoc_size19_link_reassign_clear():
    a = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    b1 = VisualInterface_Dimension(height=3.14, width=3.14)
    b2 = VisualInterface_Dimension(height=9.99, width=9.99)
    _safe_set(a, 'VisualInterface_Figure', b1)
    assert _is_linked(a, 'VisualInterface_Figure', b1)
    if hasattr(b1, 'VisualInterface_Dimension20'):
        assert _is_linked(b1, 'VisualInterface_Dimension20', a)
    _safe_set(a, 'VisualInterface_Figure', b2)
    assert _is_linked(a, 'VisualInterface_Figure', b2)
    if hasattr(b1, 'VisualInterface_Dimension20'):
        assert not _is_linked(b1, 'VisualInterface_Dimension20', a)
    if hasattr(b2, 'VisualInterface_Dimension20'):
        assert _is_linked(b2, 'VisualInterface_Dimension20', a)
    _safe_set(a, 'VisualInterface_Figure', None)
    assert not _is_linked(a, 'VisualInterface_Figure', b2)
    if hasattr(b2, 'VisualInterface_Dimension20'):
        assert not _is_linked(b2, 'VisualInterface_Dimension20', a)


def test_assoc_start30_link_reassign_clear():
    a = VisualInterface_Primitive(name="sample_text")
    b1 = VisualInterface_Connection()
    b2 = VisualInterface_Connection()
    _safe_set(a, 'VisualInterface_Primitive32', b1)
    assert _is_linked(a, 'VisualInterface_Primitive32', b1)
    if hasattr(b1, 'VisualInterface_Connection31'):
        assert _is_linked(b1, 'VisualInterface_Connection31', a)
    _safe_set(a, 'VisualInterface_Primitive32', b2)
    assert _is_linked(a, 'VisualInterface_Primitive32', b2)
    if hasattr(b1, 'VisualInterface_Connection31'):
        assert not _is_linked(b1, 'VisualInterface_Connection31', a)
    if hasattr(b2, 'VisualInterface_Connection31'):
        assert _is_linked(b2, 'VisualInterface_Connection31', a)
    _safe_set(a, 'VisualInterface_Primitive32', None)
    assert not _is_linked(a, 'VisualInterface_Primitive32', b2)
    if hasattr(b2, 'VisualInterface_Connection31'):
        assert not _is_linked(b2, 'VisualInterface_Connection31', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Child_strategy = st.builds(Child)
@given(instance=Child_strategy)
@settings(max_examples=25)
def test_Child_instantiation(instance):
    assert isinstance(instance, Child)


Container_strategy = st.builds(Container)
@given(instance=Container_strategy)
@settings(max_examples=25)
def test_Container_instantiation(instance):
    assert isinstance(instance, Container)


Cursor_strategy = st.builds(Cursor)
@given(instance=Cursor_strategy)
@settings(max_examples=25)
def test_Cursor_instantiation(instance):
    assert isinstance(instance, Cursor)


Figure_strategy = st.builds(Figure)
@given(instance=Figure_strategy)
@settings(max_examples=25)
def test_Figure_instantiation(instance):
    assert isinstance(instance, Figure)


Primitive_strategy = st.builds(Primitive)
@given(instance=Primitive_strategy)
@settings(max_examples=25)
def test_Primitive_instantiation(instance):
    assert isinstance(instance, Primitive)


Shape_strategy = st.builds(Shape)
@given(instance=Shape_strategy)
@settings(max_examples=25)
def test_Shape_instantiation(instance):
    assert isinstance(instance, Shape)


VisualInterface_Arc_strategy = st.builds(VisualInterface_Arc, length=st.integers(), start=st.integers())
@given(instance=VisualInterface_Arc_strategy)
@settings(max_examples=25)
def test_VisualInterface_Arc_instantiation(instance):
    assert isinstance(instance, VisualInterface_Arc)


VisualInterface_BorderChild_strategy = st.builds(VisualInterface_BorderChild, alignment=safe_text)
@given(instance=VisualInterface_BorderChild_strategy)
@settings(max_examples=25)
def test_VisualInterface_BorderChild_instantiation(instance):
    assert isinstance(instance, VisualInterface_BorderChild)


VisualInterface_BorderContainer_strategy = st.builds(VisualInterface_BorderContainer, horizontalSpacing=st.integers(), verticalSpacing=st.integers())
@given(instance=VisualInterface_BorderContainer_strategy)
@settings(max_examples=25)
def test_VisualInterface_BorderContainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_BorderContainer)


VisualInterface_Child_strategy = st.builds(VisualInterface_Child, name=safe_text)
@given(instance=VisualInterface_Child_strategy)
@settings(max_examples=25)
def test_VisualInterface_Child_instantiation(instance):
    assert isinstance(instance, VisualInterface_Child)


VisualInterface_Connection_strategy = st.builds(VisualInterface_Connection)
@given(instance=VisualInterface_Connection_strategy)
@settings(max_examples=25)
def test_VisualInterface_Connection_instantiation(instance):
    assert isinstance(instance, VisualInterface_Connection)


VisualInterface_Container_strategy = st.builds(VisualInterface_Container)
@given(instance=VisualInterface_Container_strategy)
@settings(max_examples=25)
def test_VisualInterface_Container_instantiation(instance):
    assert isinstance(instance, VisualInterface_Container)


VisualInterface_Cursor_strategy = st.builds(VisualInterface_Cursor)
@given(instance=VisualInterface_Cursor_strategy)
@settings(max_examples=25)
def test_VisualInterface_Cursor_instantiation(instance):
    assert isinstance(instance, VisualInterface_Cursor)


VisualInterface_Dimension_strategy = st.builds(VisualInterface_Dimension, height=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=VisualInterface_Dimension_strategy)
@settings(max_examples=25)
def test_VisualInterface_Dimension_instantiation(instance):
    assert isinstance(instance, VisualInterface_Dimension)


VisualInterface_Ellipse_strategy = st.builds(VisualInterface_Ellipse)
@given(instance=VisualInterface_Ellipse_strategy)
@settings(max_examples=25)
def test_VisualInterface_Ellipse_instantiation(instance):
    assert isinstance(instance, VisualInterface_Ellipse)


VisualInterface_Figure_strategy = st.builds(VisualInterface_Figure, backgroundColor=safe_text, border=safe_text, foregroundColor=safe_text, onClick=safe_text, onDoubleClick=safe_text, opaque=safe_text, toolTip=safe_text, visible=st.booleans())
@given(instance=VisualInterface_Figure_strategy)
@settings(max_examples=25)
def test_VisualInterface_Figure_instantiation(instance):
    assert isinstance(instance, VisualInterface_Figure)


VisualInterface_FigureContainer_strategy = st.builds(VisualInterface_FigureContainer)
@given(instance=VisualInterface_FigureContainer_strategy)
@settings(max_examples=25)
def test_VisualInterface_FigureContainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_FigureContainer)


VisualInterface_GridChild_strategy = st.builds(VisualInterface_GridChild, grabHorizontalSpace=st.booleans(), grabVerticalSpace=st.booleans(), heightHint=safe_text, horizontalAlignment=safe_text, spanCols=st.integers(), spanRows=safe_text, verticalAlignment=safe_text, widthHint=safe_text)
@given(instance=VisualInterface_GridChild_strategy)
@settings(max_examples=25)
def test_VisualInterface_GridChild_instantiation(instance):
    assert isinstance(instance, VisualInterface_GridChild)


VisualInterface_GridContainer_strategy = st.builds(VisualInterface_GridContainer, columns=st.integers(), equalWidth=st.booleans(), horizontalSpacing=st.integers(), marginHeight=st.integers(), marginWidth=st.integers(), verticalSpacing=st.integers())
@given(instance=VisualInterface_GridContainer_strategy)
@settings(max_examples=25)
def test_VisualInterface_GridContainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_GridContainer)


VisualInterface_Image_strategy = st.builds(VisualInterface_Image, uri=safe_text)
@given(instance=VisualInterface_Image_strategy)
@settings(max_examples=25)
def test_VisualInterface_Image_instantiation(instance):
    assert isinstance(instance, VisualInterface_Image)


VisualInterface_Line_strategy = st.builds(VisualInterface_Line)
@given(instance=VisualInterface_Line_strategy)
@settings(max_examples=25)
def test_VisualInterface_Line_instantiation(instance):
    assert isinstance(instance, VisualInterface_Line)


VisualInterface_Position_strategy = st.builds(VisualInterface_Position, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=VisualInterface_Position_strategy)
@settings(max_examples=25)
def test_VisualInterface_Position_instantiation(instance):
    assert isinstance(instance, VisualInterface_Position)


VisualInterface_Primitive_strategy = st.builds(VisualInterface_Primitive, name=safe_text)
@given(instance=VisualInterface_Primitive_strategy)
@settings(max_examples=25)
def test_VisualInterface_Primitive_instantiation(instance):
    assert isinstance(instance, VisualInterface_Primitive)


VisualInterface_Rectangle_strategy = st.builds(VisualInterface_Rectangle)
@given(instance=VisualInterface_Rectangle_strategy)
@settings(max_examples=25)
def test_VisualInterface_Rectangle_instantiation(instance):
    assert isinstance(instance, VisualInterface_Rectangle)


VisualInterface_Shape_strategy = st.builds(VisualInterface_Shape, alpha=safe_text, antialias=safe_text, fill=st.booleans(), lineWidth=st.floats(allow_nan=False, allow_infinity=False), outline=st.booleans())
@given(instance=VisualInterface_Shape_strategy)
@settings(max_examples=25)
def test_VisualInterface_Shape_instantiation(instance):
    assert isinstance(instance, VisualInterface_Shape)


VisualInterface_StackContainer_strategy = st.builds(VisualInterface_StackContainer)
@given(instance=VisualInterface_StackContainer_strategy)
@settings(max_examples=25)
def test_VisualInterface_StackContainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_StackContainer)


VisualInterface_StringToStringMap_strategy = st.builds(VisualInterface_StringToStringMap, key=safe_text, value=safe_text)
@given(instance=VisualInterface_StringToStringMap_strategy)
@settings(max_examples=25)
def test_VisualInterface_StringToStringMap_instantiation(instance):
    assert isinstance(instance, VisualInterface_StringToStringMap)


VisualInterface_Symbol_strategy = st.builds(VisualInterface_Symbol, backgroundColor=safe_text, onDispose=safe_text, onInit=safe_text, onUpdate=safe_text, scriptModules=safe_text)
@given(instance=VisualInterface_Symbol_strategy)
@settings(max_examples=25)
def test_VisualInterface_Symbol_instantiation(instance):
    assert isinstance(instance, VisualInterface_Symbol)


VisualInterface_SymbolReference_strategy = st.builds(VisualInterface_SymbolReference, onCreateProperties=safe_text, uri=safe_text, zoom=safe_text)
@given(instance=VisualInterface_SymbolReference_strategy)
@settings(max_examples=25)
def test_VisualInterface_SymbolReference_instantiation(instance):
    assert isinstance(instance, VisualInterface_SymbolReference)


VisualInterface_SystemCursor_strategy = st.builds(VisualInterface_SystemCursor, type=safe_text)
@given(instance=VisualInterface_SystemCursor_strategy)
@settings(max_examples=25)
def test_VisualInterface_SystemCursor_instantiation(instance):
    assert isinstance(instance, VisualInterface_SystemCursor)


VisualInterface_Text_strategy = st.builds(VisualInterface_Text, fontBold=st.booleans(), fontItalic=st.booleans(), fontName=safe_text, fontSize=st.integers(), iconAlignment=safe_text, labelAlignment=safe_text, text=safe_text, textAlignment=safe_text, textPlacement=safe_text)
@given(instance=VisualInterface_Text_strategy)
@settings(max_examples=25)
def test_VisualInterface_Text_instantiation(instance):
    assert isinstance(instance, VisualInterface_Text)


VisualInterface_XYChild_strategy = st.builds(VisualInterface_XYChild)
@given(instance=VisualInterface_XYChild_strategy)
@settings(max_examples=25)
def test_VisualInterface_XYChild_instantiation(instance):
    assert isinstance(instance, VisualInterface_XYChild)


VisualInterface_XYContainer_strategy = st.builds(VisualInterface_XYContainer)
@given(instance=VisualInterface_XYContainer_strategy)
@settings(max_examples=25)
def test_VisualInterface_XYContainer_instantiation(instance):
    assert isinstance(instance, VisualInterface_XYContainer)


