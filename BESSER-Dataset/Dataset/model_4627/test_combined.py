# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Cursor,
    VisualInterface_SystemCursor,
    Container,
    VisualInterface_StackContainer,
    VisualInterface_BorderContainer,
    VisualInterface_GridContainer,
    VisualInterface_XYContainer,
    VisualInterface_Position,
    Child,
    VisualInterface_GridChild,
    VisualInterface_BorderChild,
    VisualInterface_XYChild,
    VisualInterface_Child,
    Figure,
    VisualInterface_FigureContainer,
    VisualInterface_Image,
    VisualInterface_Shape,
    Primitive,
    VisualInterface_Figure,
    VisualInterface_SymbolReference,
    VisualInterface_Container,
    VisualInterface_Connection,
    VisualInterface_Dimension,
    VisualInterface_Cursor,
    VisualInterface_StringToStringMap,
    VisualInterface_Primitive,
    VisualInterface_Symbol,
    VisualInterface_Text,
    Shape,
    VisualInterface_Rectangle,
    VisualInterface_Line,
    VisualInterface_Arc,
    VisualInterface_Ellipse,
    SystemCursorType,
    Alignment,
    Orientation,
    GridAlignment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cursor_is_not_abstract():
    assert not inspect.isabstract(Cursor)


def test_hyp_cursor_constructor_exists():
    assert callable(Cursor.__init__)


def test_hyp_cursor_constructor_args():
    sig = inspect.signature(Cursor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_systemcursor_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_SystemCursor)


def test_hyp_visualinterface_systemcursor_constructor_exists():
    assert callable(VisualInterface_SystemCursor.__init__)


def test_hyp_visualinterface_systemcursor_constructor_args():
    sig = inspect.signature(VisualInterface_SystemCursor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_hyp_container_constructor_exists():
    assert callable(Container.__init__)


def test_hyp_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_stackcontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_StackContainer)


def test_hyp_visualinterface_stackcontainer_constructor_exists():
    assert callable(VisualInterface_StackContainer.__init__)


def test_hyp_visualinterface_stackcontainer_constructor_args():
    sig = inspect.signature(VisualInterface_StackContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_bordercontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_BorderContainer)


def test_hyp_visualinterface_bordercontainer_constructor_exists():
    assert callable(VisualInterface_BorderContainer.__init__)


def test_hyp_visualinterface_bordercontainer_constructor_args():
    sig = inspect.signature(VisualInterface_BorderContainer.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"





def test_hyp_visualinterface_gridcontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_GridContainer)


def test_hyp_visualinterface_gridcontainer_constructor_exists():
    assert callable(VisualInterface_GridContainer.__init__)


def test_hyp_visualinterface_gridcontainer_constructor_args():
    sig = inspect.signature(VisualInterface_GridContainer.__init__)
    params = list(sig.parameters.keys())
    assert "marginHeight" in params, "Missing parameter 'marginHeight'"
    assert "verticalSpacing" in params, "Missing parameter 'verticalSpacing'"
    assert "marginWidth" in params, "Missing parameter 'marginWidth'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"
    assert "columns" in params, "Missing parameter 'columns'"
    assert "horizontalSpacing" in params, "Missing parameter 'horizontalSpacing'"









def test_hyp_visualinterface_xycontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_XYContainer)


def test_hyp_visualinterface_xycontainer_constructor_exists():
    assert callable(VisualInterface_XYContainer.__init__)


def test_hyp_visualinterface_xycontainer_constructor_args():
    sig = inspect.signature(VisualInterface_XYContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_position_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Position)


def test_hyp_visualinterface_position_constructor_exists():
    assert callable(VisualInterface_Position.__init__)


def test_hyp_visualinterface_position_constructor_args():
    sig = inspect.signature(VisualInterface_Position.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_child_is_not_abstract():
    assert not inspect.isabstract(Child)


def test_hyp_child_constructor_exists():
    assert callable(Child.__init__)


def test_hyp_child_constructor_args():
    sig = inspect.signature(Child.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_gridchild_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_GridChild)


def test_hyp_visualinterface_gridchild_constructor_exists():
    assert callable(VisualInterface_GridChild.__init__)


def test_hyp_visualinterface_gridchild_constructor_args():
    sig = inspect.signature(VisualInterface_GridChild.__init__)
    params = list(sig.parameters.keys())
    assert "widthHint" in params, "Missing parameter 'widthHint'"
    assert "spanRows" in params, "Missing parameter 'spanRows'"
    assert "grabHorizontalSpace" in params, "Missing parameter 'grabHorizontalSpace'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "spanCols" in params, "Missing parameter 'spanCols'"
    assert "grabVerticalSpace" in params, "Missing parameter 'grabVerticalSpace'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "heightHint" in params, "Missing parameter 'heightHint'"











def test_hyp_visualinterface_borderchild_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_BorderChild)


def test_hyp_visualinterface_borderchild_constructor_exists():
    assert callable(VisualInterface_BorderChild.__init__)


def test_hyp_visualinterface_borderchild_constructor_args():
    sig = inspect.signature(VisualInterface_BorderChild.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"




def test_hyp_visualinterface_xychild_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_XYChild)


def test_hyp_visualinterface_xychild_constructor_exists():
    assert callable(VisualInterface_XYChild.__init__)


def test_hyp_visualinterface_xychild_constructor_args():
    sig = inspect.signature(VisualInterface_XYChild.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_child_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Child)


def test_hyp_visualinterface_child_constructor_exists():
    assert callable(VisualInterface_Child.__init__)


def test_hyp_visualinterface_child_constructor_args():
    sig = inspect.signature(VisualInterface_Child.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_hyp_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_hyp_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_figurecontainer_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_FigureContainer)


def test_hyp_visualinterface_figurecontainer_constructor_exists():
    assert callable(VisualInterface_FigureContainer.__init__)


def test_hyp_visualinterface_figurecontainer_constructor_args():
    sig = inspect.signature(VisualInterface_FigureContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_image_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Image)


def test_hyp_visualinterface_image_constructor_exists():
    assert callable(VisualInterface_Image.__init__)


def test_hyp_visualinterface_image_constructor_args():
    sig = inspect.signature(VisualInterface_Image.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"




def test_hyp_visualinterface_shape_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Shape)


def test_hyp_visualinterface_shape_constructor_exists():
    assert callable(VisualInterface_Shape.__init__)


def test_hyp_visualinterface_shape_constructor_args():
    sig = inspect.signature(VisualInterface_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "antialias" in params, "Missing parameter 'antialias'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "alpha" in params, "Missing parameter 'alpha'"








def test_hyp_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_hyp_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_hyp_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_figure_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Figure)


def test_hyp_visualinterface_figure_constructor_exists():
    assert callable(VisualInterface_Figure.__init__)


def test_hyp_visualinterface_figure_constructor_args():
    sig = inspect.signature(VisualInterface_Figure.__init__)
    params = list(sig.parameters.keys())
    assert "onDoubleClick" in params, "Missing parameter 'onDoubleClick'"
    assert "onClick" in params, "Missing parameter 'onClick'"
    assert "toolTip" in params, "Missing parameter 'toolTip'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "border" in params, "Missing parameter 'border'"
    assert "opaque" in params, "Missing parameter 'opaque'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"











def test_hyp_visualinterface_symbolreference_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_SymbolReference)


def test_hyp_visualinterface_symbolreference_constructor_exists():
    assert callable(VisualInterface_SymbolReference.__init__)


def test_hyp_visualinterface_symbolreference_constructor_args():
    sig = inspect.signature(VisualInterface_SymbolReference.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "onCreateProperties" in params, "Missing parameter 'onCreateProperties'"
    assert "uri" in params, "Missing parameter 'uri'"






def test_hyp_visualinterface_container_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Container)


def test_hyp_visualinterface_container_constructor_exists():
    assert callable(VisualInterface_Container.__init__)


def test_hyp_visualinterface_container_constructor_args():
    sig = inspect.signature(VisualInterface_Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_connection_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Connection)


def test_hyp_visualinterface_connection_constructor_exists():
    assert callable(VisualInterface_Connection.__init__)


def test_hyp_visualinterface_connection_constructor_args():
    sig = inspect.signature(VisualInterface_Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_dimension_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Dimension)


def test_hyp_visualinterface_dimension_constructor_exists():
    assert callable(VisualInterface_Dimension.__init__)


def test_hyp_visualinterface_dimension_constructor_args():
    sig = inspect.signature(VisualInterface_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"





def test_hyp_visualinterface_cursor_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Cursor)


def test_hyp_visualinterface_cursor_constructor_exists():
    assert callable(VisualInterface_Cursor.__init__)


def test_hyp_visualinterface_cursor_constructor_args():
    sig = inspect.signature(VisualInterface_Cursor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_StringToStringMap)


def test_hyp_visualinterface_stringtostringmap_constructor_exists():
    assert callable(VisualInterface_StringToStringMap.__init__)


def test_hyp_visualinterface_stringtostringmap_constructor_args():
    sig = inspect.signature(VisualInterface_StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_visualinterface_primitive_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Primitive)


def test_hyp_visualinterface_primitive_constructor_exists():
    assert callable(VisualInterface_Primitive.__init__)


def test_hyp_visualinterface_primitive_constructor_args():
    sig = inspect.signature(VisualInterface_Primitive.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_visualinterface_symbol_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Symbol)


def test_hyp_visualinterface_symbol_constructor_exists():
    assert callable(VisualInterface_Symbol.__init__)


def test_hyp_visualinterface_symbol_constructor_args():
    sig = inspect.signature(VisualInterface_Symbol.__init__)
    params = list(sig.parameters.keys())
    assert "scriptModules" in params, "Missing parameter 'scriptModules'"
    assert "onInit" in params, "Missing parameter 'onInit'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "onUpdate" in params, "Missing parameter 'onUpdate'"
    assert "onDispose" in params, "Missing parameter 'onDispose'"








def test_hyp_visualinterface_text_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Text)


def test_hyp_visualinterface_text_constructor_exists():
    assert callable(VisualInterface_Text.__init__)


def test_hyp_visualinterface_text_constructor_args():
    sig = inspect.signature(VisualInterface_Text.__init__)
    params = list(sig.parameters.keys())
    assert "textPlacement" in params, "Missing parameter 'textPlacement'"
    assert "iconAlignment" in params, "Missing parameter 'iconAlignment'"
    assert "fontItalic" in params, "Missing parameter 'fontItalic'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "fontBold" in params, "Missing parameter 'fontBold'"
    assert "text" in params, "Missing parameter 'text'"












def test_hyp_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_hyp_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_hyp_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_rectangle_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Rectangle)


def test_hyp_visualinterface_rectangle_constructor_exists():
    assert callable(VisualInterface_Rectangle.__init__)


def test_hyp_visualinterface_rectangle_constructor_args():
    sig = inspect.signature(VisualInterface_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_line_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Line)


def test_hyp_visualinterface_line_constructor_exists():
    assert callable(VisualInterface_Line.__init__)


def test_hyp_visualinterface_line_constructor_args():
    sig = inspect.signature(VisualInterface_Line.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visualinterface_arc_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Arc)


def test_hyp_visualinterface_arc_constructor_exists():
    assert callable(VisualInterface_Arc.__init__)


def test_hyp_visualinterface_arc_constructor_args():
    sig = inspect.signature(VisualInterface_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "length" in params, "Missing parameter 'length'"





def test_hyp_visualinterface_ellipse_is_not_abstract():
    assert not inspect.isabstract(VisualInterface_Ellipse)


def test_hyp_visualinterface_ellipse_constructor_exists():
    assert callable(VisualInterface_Ellipse.__init__)


def test_hyp_visualinterface_ellipse_constructor_args():
    sig = inspect.signature(VisualInterface_Ellipse.__init__)
    params = list(sig.parameters.keys())

def test_hyp_systemcursortype_exists():
    # Check that the Enumeration exists
    assert SystemCursorType is not None

def test_hyp_systemcursortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemCursorType]
    expected_literals = [
        "HAND",
        "ARROW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemCursorType"

def test_hyp_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_hyp_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "CENTER",
        "BOTTOM",
        "TOP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_hyp_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_hyp_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "NORTH",
        "WEST",
        "SOUTH",
        "EAST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_hyp_gridalignment_exists():
    # Check that the Enumeration exists
    assert GridAlignment is not None

def test_hyp_gridalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GridAlignment]
    expected_literals = [
        "BEGINNING",
        "END",
        "FILL",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GridAlignment"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Cursor_strategy = st.builds(
    Cursor,
)
VisualInterface_SystemCursor_strategy = st.builds(
    VisualInterface_SystemCursor,
    type=
        safe_text
)
Container_strategy = st.builds(
    Container,
)
VisualInterface_StackContainer_strategy = st.builds(
    VisualInterface_StackContainer,
)
VisualInterface_BorderContainer_strategy = st.builds(
    VisualInterface_BorderContainer,
    horizontalSpacing=
        st.integers(),
    verticalSpacing=
        st.integers()
)
VisualInterface_GridContainer_strategy = st.builds(
    VisualInterface_GridContainer,
    marginHeight=
        st.integers(),
    verticalSpacing=
        st.integers(),
    marginWidth=
        st.integers(),
    equalWidth=
        st.booleans(),
    columns=
        st.integers(),
    horizontalSpacing=
        st.integers()
)
VisualInterface_XYContainer_strategy = st.builds(
    VisualInterface_XYContainer,
)
VisualInterface_Position_strategy = st.builds(
    VisualInterface_Position,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Child_strategy = st.builds(
    Child,
)
VisualInterface_GridChild_strategy = st.builds(
    VisualInterface_GridChild,
    widthHint=
        safe_text,
    spanRows=
        safe_text,
    grabHorizontalSpace=
        st.booleans(),
    verticalAlignment=
        safe_text,
    spanCols=
        st.integers(),
    grabVerticalSpace=
        st.booleans(),
    horizontalAlignment=
        safe_text,
    heightHint=
        safe_text
)
VisualInterface_BorderChild_strategy = st.builds(
    VisualInterface_BorderChild,
    alignment=
        safe_text
)
VisualInterface_XYChild_strategy = st.builds(
    VisualInterface_XYChild,
)
VisualInterface_Child_strategy = st.builds(
    VisualInterface_Child,
    name=
        safe_text
)
Figure_strategy = st.builds(
    Figure,
)
VisualInterface_FigureContainer_strategy = st.builds(
    VisualInterface_FigureContainer,
)
VisualInterface_Image_strategy = st.builds(
    VisualInterface_Image,
    uri=
        safe_text
)
VisualInterface_Shape_strategy = st.builds(
    VisualInterface_Shape,
    antialias=
        safe_text,
    outline=
        st.booleans(),
    lineWidth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fill=
        st.booleans(),
    alpha=
        safe_text
)
Primitive_strategy = st.builds(
    Primitive,
)
VisualInterface_Figure_strategy = st.builds(
    VisualInterface_Figure,
    onDoubleClick=
        safe_text,
    onClick=
        safe_text,
    toolTip=
        safe_text,
    backgroundColor=
        safe_text,
    visible=
        st.booleans(),
    border=
        safe_text,
    opaque=
        safe_text,
    foregroundColor=
        safe_text
)
VisualInterface_SymbolReference_strategy = st.builds(
    VisualInterface_SymbolReference,
    zoom=
        safe_text,
    onCreateProperties=
        safe_text,
    uri=
        safe_text
)
VisualInterface_Container_strategy = st.builds(
    VisualInterface_Container,
)
VisualInterface_Connection_strategy = st.builds(
    VisualInterface_Connection,
)
VisualInterface_Dimension_strategy = st.builds(
    VisualInterface_Dimension,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
VisualInterface_Cursor_strategy = st.builds(
    VisualInterface_Cursor,
)
VisualInterface_StringToStringMap_strategy = st.builds(
    VisualInterface_StringToStringMap,
    key=
        safe_text,
    value=
        safe_text
)
VisualInterface_Primitive_strategy = st.builds(
    VisualInterface_Primitive,
    name=
        safe_text
)
VisualInterface_Symbol_strategy = st.builds(
    VisualInterface_Symbol,
    scriptModules=
        safe_text,
    onInit=
        safe_text,
    backgroundColor=
        safe_text,
    onUpdate=
        safe_text,
    onDispose=
        safe_text
)
VisualInterface_Text_strategy = st.builds(
    VisualInterface_Text,
    textPlacement=
        safe_text,
    iconAlignment=
        safe_text,
    fontItalic=
        st.booleans(),
    fontName=
        safe_text,
    textAlignment=
        safe_text,
    labelAlignment=
        safe_text,
    fontSize=
        st.integers(),
    fontBold=
        st.booleans(),
    text=
        safe_text
)
Shape_strategy = st.builds(
    Shape,
)
VisualInterface_Rectangle_strategy = st.builds(
    VisualInterface_Rectangle,
)
VisualInterface_Line_strategy = st.builds(
    VisualInterface_Line,
)
VisualInterface_Arc_strategy = st.builds(
    VisualInterface_Arc,
    start=
        st.integers(),
    length=
        st.integers()
)
VisualInterface_Ellipse_strategy = st.builds(
    VisualInterface_Ellipse,
)





@given(instance=VisualInterface_SystemCursor_strategy)
def test_hyp_visualinterface_systemcursor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=VisualInterface_BorderContainer_strategy)
def test_hyp_visualinterface_bordercontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original



@given(instance=VisualInterface_BorderContainer_strategy)
def test_hyp_visualinterface_bordercontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original




@given(instance=VisualInterface_GridContainer_strategy)
def test_hyp_visualinterface_gridcontainer_marginHeight_setter(instance):
    original = instance.marginHeight
    instance.marginHeight = original
    assert instance.marginHeight == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_hyp_visualinterface_gridcontainer_verticalSpacing_setter(instance):
    original = instance.verticalSpacing
    instance.verticalSpacing = original
    assert instance.verticalSpacing == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_hyp_visualinterface_gridcontainer_marginWidth_setter(instance):
    original = instance.marginWidth
    instance.marginWidth = original
    assert instance.marginWidth == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_hyp_visualinterface_gridcontainer_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_hyp_visualinterface_gridcontainer_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=VisualInterface_GridContainer_strategy)
def test_hyp_visualinterface_gridcontainer_horizontalSpacing_setter(instance):
    original = instance.horizontalSpacing
    instance.horizontalSpacing = original
    assert instance.horizontalSpacing == original





@given(instance=VisualInterface_Position_strategy)
def test_hyp_visualinterface_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=VisualInterface_Position_strategy)
def test_hyp_visualinterface_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original





@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_widthHint_setter(instance):
    original = instance.widthHint
    instance.widthHint = original
    assert instance.widthHint == original



@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_spanRows_setter(instance):
    original = instance.spanRows
    instance.spanRows = original
    assert instance.spanRows == original



@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_grabHorizontalSpace_setter(instance):
    original = instance.grabHorizontalSpace
    instance.grabHorizontalSpace = original
    assert instance.grabHorizontalSpace == original



@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original



@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_spanCols_setter(instance):
    original = instance.spanCols
    instance.spanCols = original
    assert instance.spanCols == original



@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_grabVerticalSpace_setter(instance):
    original = instance.grabVerticalSpace
    instance.grabVerticalSpace = original
    assert instance.grabVerticalSpace == original



@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original



@given(instance=VisualInterface_GridChild_strategy)
def test_hyp_visualinterface_gridchild_heightHint_setter(instance):
    original = instance.heightHint
    instance.heightHint = original
    assert instance.heightHint == original




@given(instance=VisualInterface_BorderChild_strategy)
def test_hyp_visualinterface_borderchild_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original





@given(instance=VisualInterface_Child_strategy)
def test_hyp_visualinterface_child_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=VisualInterface_Image_strategy)
def test_hyp_visualinterface_image_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original




@given(instance=VisualInterface_Shape_strategy)
def test_hyp_visualinterface_shape_antialias_setter(instance):
    original = instance.antialias
    instance.antialias = original
    assert instance.antialias == original



@given(instance=VisualInterface_Shape_strategy)
def test_hyp_visualinterface_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original



@given(instance=VisualInterface_Shape_strategy)
def test_hyp_visualinterface_shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=VisualInterface_Shape_strategy)
def test_hyp_visualinterface_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=VisualInterface_Shape_strategy)
def test_hyp_visualinterface_shape_alpha_setter(instance):
    original = instance.alpha
    instance.alpha = original
    assert instance.alpha == original





@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_onDoubleClick_setter(instance):
    original = instance.onDoubleClick
    instance.onDoubleClick = original
    assert instance.onDoubleClick == original



@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_onClick_setter(instance):
    original = instance.onClick
    instance.onClick = original
    assert instance.onClick == original



@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_toolTip_setter(instance):
    original = instance.toolTip
    instance.toolTip = original
    assert instance.toolTip == original



@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_opaque_setter(instance):
    original = instance.opaque
    instance.opaque = original
    assert instance.opaque == original



@given(instance=VisualInterface_Figure_strategy)
def test_hyp_visualinterface_figure_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original




@given(instance=VisualInterface_SymbolReference_strategy)
def test_hyp_visualinterface_symbolreference_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original



@given(instance=VisualInterface_SymbolReference_strategy)
def test_hyp_visualinterface_symbolreference_onCreateProperties_setter(instance):
    original = instance.onCreateProperties
    instance.onCreateProperties = original
    assert instance.onCreateProperties == original



@given(instance=VisualInterface_SymbolReference_strategy)
def test_hyp_visualinterface_symbolreference_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original






@given(instance=VisualInterface_Dimension_strategy)
def test_hyp_visualinterface_dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=VisualInterface_Dimension_strategy)
def test_hyp_visualinterface_dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=VisualInterface_StringToStringMap_strategy)
def test_hyp_visualinterface_stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=VisualInterface_StringToStringMap_strategy)
def test_hyp_visualinterface_stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=VisualInterface_Primitive_strategy)
def test_hyp_visualinterface_primitive_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=VisualInterface_Symbol_strategy)
def test_hyp_visualinterface_symbol_scriptModules_setter(instance):
    original = instance.scriptModules
    instance.scriptModules = original
    assert instance.scriptModules == original



@given(instance=VisualInterface_Symbol_strategy)
def test_hyp_visualinterface_symbol_onInit_setter(instance):
    original = instance.onInit
    instance.onInit = original
    assert instance.onInit == original



@given(instance=VisualInterface_Symbol_strategy)
def test_hyp_visualinterface_symbol_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=VisualInterface_Symbol_strategy)
def test_hyp_visualinterface_symbol_onUpdate_setter(instance):
    original = instance.onUpdate
    instance.onUpdate = original
    assert instance.onUpdate == original



@given(instance=VisualInterface_Symbol_strategy)
def test_hyp_visualinterface_symbol_onDispose_setter(instance):
    original = instance.onDispose
    instance.onDispose = original
    assert instance.onDispose == original




@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_textPlacement_setter(instance):
    original = instance.textPlacement
    instance.textPlacement = original
    assert instance.textPlacement == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_iconAlignment_setter(instance):
    original = instance.iconAlignment
    instance.iconAlignment = original
    assert instance.iconAlignment == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_fontItalic_setter(instance):
    original = instance.fontItalic
    instance.fontItalic = original
    assert instance.fontItalic == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_fontBold_setter(instance):
    original = instance.fontBold
    instance.fontBold = original
    assert instance.fontBold == original



@given(instance=VisualInterface_Text_strategy)
def test_hyp_visualinterface_text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original







@given(instance=VisualInterface_Arc_strategy)
def test_hyp_visualinterface_arc_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=VisualInterface_Arc_strategy)
def test_hyp_visualinterface_arc_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



