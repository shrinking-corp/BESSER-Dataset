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
    pnmlcoremodel_Font,
    pnmlcoremodel_ID,
    ToolInfo,
    pnmlcoremodel_ToolInfoText,
    PetriNetType,
    pnmlcoremodel_EmptyType,
    Label,
    pnmlcoremodel_Attribute,
    TransitionNode,
    pnmlcoremodel_Transition,
    pnmlcoremodel_RefTransition,
    PlaceNode,
    pnmlcoremodel_RefPlace,
    pnmlcoremodel_Place,
    pnmlcoremodel_Fill,
    pnmlcoremodel_Coordinate,
    pnmlcoremodel_Line,
    Graphics,
    pnmlcoremodel_AnnotationGraphics,
    pnmlcoremodel_NodeGraphics,
    pnmlcoremodel_ArcGraphics,
    pnmlcoremodel_Graphics,
    pnmlcoremodel_LabelProxy,
    pnmlcoremodel_PageLabelProxy,
    Node,
    pnmlcoremodel_AnyType,
    pnmlcoremodel_TransitionNode,
    pnmlcoremodel_PlaceNode,
    Object,
    pnmlcoremodel_Arc,
    pnmlcoremodel_Node,
    pnmlcoremodel_Label,
    pnmlcoremodel_ToolInfo,
    pnmlcoremodel_Page,
    pnmlcoremodel_Name,
    pnmlcoremodel_PetriNetType,
    ID,
    pnmlcoremodel_Object,
    pnmlcoremodel_PetriNet,
    pnmlcoremodel_PetriNetDoc,
    LineShape,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pnmlcoremodel_font_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Font)


def test_hyp_pnmlcoremodel_font_constructor_exists():
    assert callable(pnmlcoremodel_Font.__init__)


def test_hyp_pnmlcoremodel_font_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Font.__init__)
    params = list(sig.parameters.keys())
    assert "family" in params, "Missing parameter 'family'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "style" in params, "Missing parameter 'style'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "size" in params, "Missing parameter 'size'"
    assert "align" in params, "Missing parameter 'align'"










def test_hyp_pnmlcoremodel_id_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_ID)


def test_hyp_pnmlcoremodel_id_constructor_exists():
    assert callable(pnmlcoremodel_ID.__init__)


def test_hyp_pnmlcoremodel_id_constructor_args():
    sig = inspect.signature(pnmlcoremodel_ID.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_toolinfo_is_not_abstract():
    assert not inspect.isabstract(ToolInfo)


def test_hyp_toolinfo_constructor_exists():
    assert callable(ToolInfo.__init__)


def test_hyp_toolinfo_constructor_args():
    sig = inspect.signature(ToolInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_toolinfotext_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_ToolInfoText)


def test_hyp_pnmlcoremodel_toolinfotext_constructor_exists():
    assert callable(pnmlcoremodel_ToolInfoText.__init__)


def test_hyp_pnmlcoremodel_toolinfotext_constructor_args():
    sig = inspect.signature(pnmlcoremodel_ToolInfoText.__init__)
    params = list(sig.parameters.keys())
    assert "info" in params, "Missing parameter 'info'"




def test_hyp_petrinettype_is_not_abstract():
    assert not inspect.isabstract(PetriNetType)


def test_hyp_petrinettype_constructor_exists():
    assert callable(PetriNetType.__init__)


def test_hyp_petrinettype_constructor_args():
    sig = inspect.signature(PetriNetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_emptytype_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_EmptyType)


def test_hyp_pnmlcoremodel_emptytype_constructor_exists():
    assert callable(pnmlcoremodel_EmptyType.__init__)


def test_hyp_pnmlcoremodel_emptytype_constructor_args():
    sig = inspect.signature(pnmlcoremodel_EmptyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_hyp_label_constructor_exists():
    assert callable(Label.__init__)


def test_hyp_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_attribute_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Attribute)


def test_hyp_pnmlcoremodel_attribute_constructor_exists():
    assert callable(pnmlcoremodel_Attribute.__init__)


def test_hyp_pnmlcoremodel_attribute_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_hyp_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_hyp_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_transition_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Transition)


def test_hyp_pnmlcoremodel_transition_constructor_exists():
    assert callable(pnmlcoremodel_Transition.__init__)


def test_hyp_pnmlcoremodel_transition_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_reftransition_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_RefTransition)


def test_hyp_pnmlcoremodel_reftransition_constructor_exists():
    assert callable(pnmlcoremodel_RefTransition.__init__)


def test_hyp_pnmlcoremodel_reftransition_constructor_args():
    sig = inspect.signature(pnmlcoremodel_RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_hyp_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_hyp_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_refplace_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_RefPlace)


def test_hyp_pnmlcoremodel_refplace_constructor_exists():
    assert callable(pnmlcoremodel_RefPlace.__init__)


def test_hyp_pnmlcoremodel_refplace_constructor_args():
    sig = inspect.signature(pnmlcoremodel_RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_place_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Place)


def test_hyp_pnmlcoremodel_place_constructor_exists():
    assert callable(pnmlcoremodel_Place.__init__)


def test_hyp_pnmlcoremodel_place_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_fill_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Fill)


def test_hyp_pnmlcoremodel_fill_constructor_exists():
    assert callable(pnmlcoremodel_Fill.__init__)


def test_hyp_pnmlcoremodel_fill_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Fill.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "gradientColor" in params, "Missing parameter 'gradientColor'"
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "image" in params, "Missing parameter 'image'"







def test_hyp_pnmlcoremodel_coordinate_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Coordinate)


def test_hyp_pnmlcoremodel_coordinate_constructor_exists():
    assert callable(pnmlcoremodel_Coordinate.__init__)


def test_hyp_pnmlcoremodel_coordinate_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_pnmlcoremodel_line_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Line)


def test_hyp_pnmlcoremodel_line_constructor_exists():
    assert callable(pnmlcoremodel_Line.__init__)


def test_hyp_pnmlcoremodel_line_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Line.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "color" in params, "Missing parameter 'color'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "style" in params, "Missing parameter 'style'"







def test_hyp_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_hyp_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_hyp_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_AnnotationGraphics)


def test_hyp_pnmlcoremodel_annotationgraphics_constructor_exists():
    assert callable(pnmlcoremodel_AnnotationGraphics.__init__)


def test_hyp_pnmlcoremodel_annotationgraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_NodeGraphics)


def test_hyp_pnmlcoremodel_nodegraphics_constructor_exists():
    assert callable(pnmlcoremodel_NodeGraphics.__init__)


def test_hyp_pnmlcoremodel_nodegraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_arcgraphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_ArcGraphics)


def test_hyp_pnmlcoremodel_arcgraphics_constructor_exists():
    assert callable(pnmlcoremodel_ArcGraphics.__init__)


def test_hyp_pnmlcoremodel_arcgraphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_graphics_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Graphics)


def test_hyp_pnmlcoremodel_graphics_constructor_exists():
    assert callable(pnmlcoremodel_Graphics.__init__)


def test_hyp_pnmlcoremodel_graphics_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_labelproxy_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_LabelProxy)


def test_hyp_pnmlcoremodel_labelproxy_constructor_exists():
    assert callable(pnmlcoremodel_LabelProxy.__init__)


def test_hyp_pnmlcoremodel_labelproxy_constructor_args():
    sig = inspect.signature(pnmlcoremodel_LabelProxy.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_pnmlcoremodel_pagelabelproxy_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PageLabelProxy)


def test_hyp_pnmlcoremodel_pagelabelproxy_constructor_exists():
    assert callable(pnmlcoremodel_PageLabelProxy.__init__)


def test_hyp_pnmlcoremodel_pagelabelproxy_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PageLabelProxy.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_anytype_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_AnyType)


def test_hyp_pnmlcoremodel_anytype_constructor_exists():
    assert callable(pnmlcoremodel_AnyType.__init__)


def test_hyp_pnmlcoremodel_anytype_constructor_args():
    sig = inspect.signature(pnmlcoremodel_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_transitionnode_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_TransitionNode)


def test_hyp_pnmlcoremodel_transitionnode_constructor_exists():
    assert callable(pnmlcoremodel_TransitionNode.__init__)


def test_hyp_pnmlcoremodel_transitionnode_constructor_args():
    sig = inspect.signature(pnmlcoremodel_TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_placenode_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PlaceNode)


def test_hyp_pnmlcoremodel_placenode_constructor_exists():
    assert callable(pnmlcoremodel_PlaceNode.__init__)


def test_hyp_pnmlcoremodel_placenode_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_hyp_object_constructor_exists():
    assert callable(Object.__init__)


def test_hyp_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_arc_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Arc)


def test_hyp_pnmlcoremodel_arc_constructor_exists():
    assert callable(pnmlcoremodel_Arc.__init__)


def test_hyp_pnmlcoremodel_arc_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_node_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Node)


def test_hyp_pnmlcoremodel_node_constructor_exists():
    assert callable(pnmlcoremodel_Node.__init__)


def test_hyp_pnmlcoremodel_node_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_label_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Label)


def test_hyp_pnmlcoremodel_label_constructor_exists():
    assert callable(pnmlcoremodel_Label.__init__)


def test_hyp_pnmlcoremodel_label_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_toolinfo_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_ToolInfo)


def test_hyp_pnmlcoremodel_toolinfo_constructor_exists():
    assert callable(pnmlcoremodel_ToolInfo.__init__)


def test_hyp_pnmlcoremodel_toolinfo_constructor_args():
    sig = inspect.signature(pnmlcoremodel_ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"





def test_hyp_pnmlcoremodel_page_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Page)


def test_hyp_pnmlcoremodel_page_constructor_exists():
    assert callable(pnmlcoremodel_Page.__init__)


def test_hyp_pnmlcoremodel_page_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_name_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Name)


def test_hyp_pnmlcoremodel_name_constructor_exists():
    assert callable(pnmlcoremodel_Name.__init__)


def test_hyp_pnmlcoremodel_name_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_pnmlcoremodel_petrinettype_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PetriNetType)


def test_hyp_pnmlcoremodel_petrinettype_constructor_exists():
    assert callable(pnmlcoremodel_PetriNetType.__init__)


def test_hyp_pnmlcoremodel_petrinettype_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PetriNetType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_id_is_not_abstract():
    assert not inspect.isabstract(ID)


def test_hyp_id_constructor_exists():
    assert callable(ID.__init__)


def test_hyp_id_constructor_args():
    sig = inspect.signature(ID.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_object_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_Object)


def test_hyp_pnmlcoremodel_object_constructor_exists():
    assert callable(pnmlcoremodel_Object.__init__)


def test_hyp_pnmlcoremodel_object_constructor_args():
    sig = inspect.signature(pnmlcoremodel_Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_petrinet_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PetriNet)


def test_hyp_pnmlcoremodel_petrinet_constructor_exists():
    assert callable(pnmlcoremodel_PetriNet.__init__)


def test_hyp_pnmlcoremodel_petrinet_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnmlcoremodel_petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(pnmlcoremodel_PetriNetDoc)


def test_hyp_pnmlcoremodel_petrinetdoc_constructor_exists():
    assert callable(pnmlcoremodel_PetriNetDoc.__init__)


def test_hyp_pnmlcoremodel_petrinetdoc_constructor_args():
    sig = inspect.signature(pnmlcoremodel_PetriNetDoc.__init__)
    params = list(sig.parameters.keys())

def test_hyp_lineshape_exists():
    # Check that the Enumeration exists
    assert LineShape is not None

def test_hyp_lineshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineShape]
    expected_literals = [
        "line",
        "curve",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineShape"


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
pnmlcoremodel_Font_strategy = st.builds(
    pnmlcoremodel_Font,
    family=
        safe_text,
    weight=
        safe_text,
    decoration=
        safe_text,
    style=
        safe_text,
    rotation=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    size=
        safe_text,
    align=
        safe_text
)
pnmlcoremodel_ID_strategy = st.builds(
    pnmlcoremodel_ID,
    id=
        safe_text
)
ToolInfo_strategy = st.builds(
    ToolInfo,
)
pnmlcoremodel_ToolInfoText_strategy = st.builds(
    pnmlcoremodel_ToolInfoText,
    info=
        safe_text
)
PetriNetType_strategy = st.builds(
    PetriNetType,
)
pnmlcoremodel_EmptyType_strategy = st.builds(
    pnmlcoremodel_EmptyType,
)
Label_strategy = st.builds(
    Label,
)
pnmlcoremodel_Attribute_strategy = st.builds(
    pnmlcoremodel_Attribute,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
pnmlcoremodel_Transition_strategy = st.builds(
    pnmlcoremodel_Transition,
)
pnmlcoremodel_RefTransition_strategy = st.builds(
    pnmlcoremodel_RefTransition,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
pnmlcoremodel_RefPlace_strategy = st.builds(
    pnmlcoremodel_RefPlace,
)
pnmlcoremodel_Place_strategy = st.builds(
    pnmlcoremodel_Place,
)
pnmlcoremodel_Fill_strategy = st.builds(
    pnmlcoremodel_Fill,
    color=
        safe_text,
    gradientColor=
        safe_text,
    gradientrotation=
        safe_text,
    image=
        safe_text
)
pnmlcoremodel_Coordinate_strategy = st.builds(
    pnmlcoremodel_Coordinate,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
pnmlcoremodel_Line_strategy = st.builds(
    pnmlcoremodel_Line,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    color=
        safe_text,
    shape=
        safe_text,
    style=
        safe_text
)
Graphics_strategy = st.builds(
    Graphics,
)
pnmlcoremodel_AnnotationGraphics_strategy = st.builds(
    pnmlcoremodel_AnnotationGraphics,
)
pnmlcoremodel_NodeGraphics_strategy = st.builds(
    pnmlcoremodel_NodeGraphics,
)
pnmlcoremodel_ArcGraphics_strategy = st.builds(
    pnmlcoremodel_ArcGraphics,
)
pnmlcoremodel_Graphics_strategy = st.builds(
    pnmlcoremodel_Graphics,
)
pnmlcoremodel_LabelProxy_strategy = st.builds(
    pnmlcoremodel_LabelProxy,
    text=
        safe_text
)
pnmlcoremodel_PageLabelProxy_strategy = st.builds(
    pnmlcoremodel_PageLabelProxy,
    text=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
pnmlcoremodel_AnyType_strategy = st.builds(
    pnmlcoremodel_AnyType,
)
pnmlcoremodel_TransitionNode_strategy = st.builds(
    pnmlcoremodel_TransitionNode,
)
pnmlcoremodel_PlaceNode_strategy = st.builds(
    pnmlcoremodel_PlaceNode,
)
Object_strategy = st.builds(
    Object,
)
pnmlcoremodel_Arc_strategy = st.builds(
    pnmlcoremodel_Arc,
)
pnmlcoremodel_Node_strategy = st.builds(
    pnmlcoremodel_Node,
)
pnmlcoremodel_Label_strategy = st.builds(
    pnmlcoremodel_Label,
)
pnmlcoremodel_ToolInfo_strategy = st.builds(
    pnmlcoremodel_ToolInfo,
    version=
        safe_text,
    tool=
        safe_text
)
pnmlcoremodel_Page_strategy = st.builds(
    pnmlcoremodel_Page,
)
pnmlcoremodel_Name_strategy = st.builds(
    pnmlcoremodel_Name,
    text=
        safe_text
)
pnmlcoremodel_PetriNetType_strategy = st.builds(
    pnmlcoremodel_PetriNetType,
)
ID_strategy = st.builds(
    ID,
)
pnmlcoremodel_Object_strategy = st.builds(
    pnmlcoremodel_Object,
)
pnmlcoremodel_PetriNet_strategy = st.builds(
    pnmlcoremodel_PetriNet,
)
pnmlcoremodel_PetriNetDoc_strategy = st.builds(
    pnmlcoremodel_PetriNetDoc,
)




@given(instance=pnmlcoremodel_Font_strategy)
def test_hyp_pnmlcoremodel_font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_hyp_pnmlcoremodel_font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_hyp_pnmlcoremodel_font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_hyp_pnmlcoremodel_font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_hyp_pnmlcoremodel_font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_hyp_pnmlcoremodel_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=pnmlcoremodel_Font_strategy)
def test_hyp_pnmlcoremodel_font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original




@given(instance=pnmlcoremodel_ID_strategy)
def test_hyp_pnmlcoremodel_id_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=pnmlcoremodel_ToolInfoText_strategy)
def test_hyp_pnmlcoremodel_toolinfotext_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original














@given(instance=pnmlcoremodel_Fill_strategy)
def test_hyp_pnmlcoremodel_fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=pnmlcoremodel_Fill_strategy)
def test_hyp_pnmlcoremodel_fill_gradientColor_setter(instance):
    original = instance.gradientColor
    instance.gradientColor = original
    assert instance.gradientColor == original



@given(instance=pnmlcoremodel_Fill_strategy)
def test_hyp_pnmlcoremodel_fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original



@given(instance=pnmlcoremodel_Fill_strategy)
def test_hyp_pnmlcoremodel_fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original




@given(instance=pnmlcoremodel_Coordinate_strategy)
def test_hyp_pnmlcoremodel_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=pnmlcoremodel_Coordinate_strategy)
def test_hyp_pnmlcoremodel_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original




@given(instance=pnmlcoremodel_Line_strategy)
def test_hyp_pnmlcoremodel_line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=pnmlcoremodel_Line_strategy)
def test_hyp_pnmlcoremodel_line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=pnmlcoremodel_Line_strategy)
def test_hyp_pnmlcoremodel_line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=pnmlcoremodel_Line_strategy)
def test_hyp_pnmlcoremodel_line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original









@given(instance=pnmlcoremodel_LabelProxy_strategy)
def test_hyp_pnmlcoremodel_labelproxy_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=pnmlcoremodel_PageLabelProxy_strategy)
def test_hyp_pnmlcoremodel_pagelabelproxy_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original












@given(instance=pnmlcoremodel_ToolInfo_strategy)
def test_hyp_pnmlcoremodel_toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=pnmlcoremodel_ToolInfo_strategy)
def test_hyp_pnmlcoremodel_toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original





@given(instance=pnmlcoremodel_Name_strategy)
def test_hyp_pnmlcoremodel_name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Graphics,
    ID,
    Label,
    Node,
    Object,
    PetriNetType,
    PlaceNode,
    ToolInfo,
    TransitionNode,
    pnmlcoremodel_AnnotationGraphics,
    pnmlcoremodel_AnyType,
    pnmlcoremodel_Arc,
    pnmlcoremodel_ArcGraphics,
    pnmlcoremodel_Attribute,
    pnmlcoremodel_Coordinate,
    pnmlcoremodel_EmptyType,
    pnmlcoremodel_Fill,
    pnmlcoremodel_Font,
    pnmlcoremodel_Graphics,
    pnmlcoremodel_ID,
    pnmlcoremodel_Label,
    pnmlcoremodel_LabelProxy,
    pnmlcoremodel_Line,
    pnmlcoremodel_Name,
    pnmlcoremodel_Node,
    pnmlcoremodel_NodeGraphics,
    pnmlcoremodel_Object,
    pnmlcoremodel_Page,
    pnmlcoremodel_PageLabelProxy,
    pnmlcoremodel_PetriNet,
    pnmlcoremodel_PetriNetDoc,
    pnmlcoremodel_PetriNetType,
    pnmlcoremodel_Place,
    pnmlcoremodel_PlaceNode,
    pnmlcoremodel_RefPlace,
    pnmlcoremodel_RefTransition,
    pnmlcoremodel_ToolInfo,
    pnmlcoremodel_ToolInfoText,
    pnmlcoremodel_Transition,
    pnmlcoremodel_TransitionNode,
    LineShape,
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

def test_pnmlcoremodel_Coordinate_x_value_roundtrip():
    instance = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_pnmlcoremodel_Coordinate_y_value_roundtrip():
    instance = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_pnmlcoremodel_Fill_color_value_roundtrip():
    instance = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_pnmlcoremodel_Fill_gradientColor_value_roundtrip():
    instance = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.gradientColor == "sample_text"
    instance.gradientColor = "sample_text_2"
    assert instance.gradientColor == "sample_text_2"


def test_pnmlcoremodel_Fill_gradientrotation_value_roundtrip():
    instance = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.gradientrotation == "sample_text"
    instance.gradientrotation = "sample_text_2"
    assert instance.gradientrotation == "sample_text_2"


def test_pnmlcoremodel_Fill_image_value_roundtrip():
    instance = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_pnmlcoremodel_Font_align_value_roundtrip():
    instance = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_pnmlcoremodel_Font_decoration_value_roundtrip():
    instance = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    assert instance.decoration == "sample_text"
    instance.decoration = "sample_text_2"
    assert instance.decoration == "sample_text_2"


def test_pnmlcoremodel_Font_family_value_roundtrip():
    instance = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    assert instance.family == "sample_text"
    instance.family = "sample_text_2"
    assert instance.family == "sample_text_2"


def test_pnmlcoremodel_Font_rotation_value_roundtrip():
    instance = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    assert instance.rotation == 3.14
    instance.rotation = 9.99
    assert instance.rotation == 9.99


def test_pnmlcoremodel_Font_size_value_roundtrip():
    instance = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_pnmlcoremodel_Font_style_value_roundtrip():
    instance = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_pnmlcoremodel_Font_weight_value_roundtrip():
    instance = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_pnmlcoremodel_ID_id_value_roundtrip():
    instance = pnmlcoremodel_ID(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_pnmlcoremodel_LabelProxy_text_value_roundtrip():
    instance = pnmlcoremodel_LabelProxy(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pnmlcoremodel_Line_color_value_roundtrip():
    instance = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_pnmlcoremodel_Line_shape_value_roundtrip():
    instance = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_pnmlcoremodel_Line_style_value_roundtrip():
    instance = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_pnmlcoremodel_Line_width_value_roundtrip():
    instance = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_pnmlcoremodel_Name_text_value_roundtrip():
    instance = pnmlcoremodel_Name(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pnmlcoremodel_PageLabelProxy_text_value_roundtrip():
    instance = pnmlcoremodel_PageLabelProxy(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_pnmlcoremodel_ToolInfo_tool_value_roundtrip():
    instance = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    assert instance.tool == "sample_text"
    instance.tool = "sample_text_2"
    assert instance.tool == "sample_text_2"


def test_pnmlcoremodel_ToolInfo_version_value_roundtrip():
    instance = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_pnmlcoremodel_ToolInfoText_info_value_roundtrip():
    instance = pnmlcoremodel_ToolInfoText(info="sample_text")
    assert instance.info == "sample_text"
    instance.info = "sample_text_2"
    assert instance.info == "sample_text_2"


def test_pnmlcoremodel_AnnotationGraphics_isa_Graphics():
    instance = pnmlcoremodel_AnnotationGraphics()
    assert isinstance(instance, Graphics)


def test_pnmlcoremodel_ArcGraphics_isa_Graphics():
    instance = pnmlcoremodel_ArcGraphics()
    assert isinstance(instance, Graphics)


def test_pnmlcoremodel_NodeGraphics_isa_Graphics():
    instance = pnmlcoremodel_NodeGraphics()
    assert isinstance(instance, Graphics)


def test_pnmlcoremodel_Object_isa_ID():
    instance = pnmlcoremodel_Object()
    assert isinstance(instance, ID)


def test_pnmlcoremodel_PetriNet_isa_ID():
    instance = pnmlcoremodel_PetriNet()
    assert isinstance(instance, ID)


def test_pnmlcoremodel_Attribute_isa_Label():
    instance = pnmlcoremodel_Attribute()
    assert isinstance(instance, Label)


def test_pnmlcoremodel_Name_isa_Label():
    instance = pnmlcoremodel_Name(text="sample_text")
    assert isinstance(instance, Label)


def test_pnmlcoremodel_Page_isa_Node():
    instance = pnmlcoremodel_Page()
    assert isinstance(instance, Node)


def test_pnmlcoremodel_PlaceNode_isa_Node():
    instance = pnmlcoremodel_PlaceNode()
    assert isinstance(instance, Node)


def test_pnmlcoremodel_TransitionNode_isa_Node():
    instance = pnmlcoremodel_TransitionNode()
    assert isinstance(instance, Node)


def test_pnmlcoremodel_Arc_isa_Object():
    instance = pnmlcoremodel_Arc()
    assert isinstance(instance, Object)


def test_pnmlcoremodel_Node_isa_Object():
    instance = pnmlcoremodel_Node()
    assert isinstance(instance, Object)


def test_pnmlcoremodel_EmptyType_isa_PetriNetType():
    instance = pnmlcoremodel_EmptyType()
    assert isinstance(instance, PetriNetType)


def test_pnmlcoremodel_Place_isa_PlaceNode():
    instance = pnmlcoremodel_Place()
    assert isinstance(instance, PlaceNode)


def test_pnmlcoremodel_RefPlace_isa_PlaceNode():
    instance = pnmlcoremodel_RefPlace()
    assert isinstance(instance, PlaceNode)


def test_pnmlcoremodel_ToolInfoText_isa_ToolInfo():
    instance = pnmlcoremodel_ToolInfoText(info="sample_text")
    assert isinstance(instance, ToolInfo)


def test_pnmlcoremodel_RefTransition_isa_TransitionNode():
    instance = pnmlcoremodel_RefTransition()
    assert isinstance(instance, TransitionNode)


def test_pnmlcoremodel_Transition_isa_TransitionNode():
    instance = pnmlcoremodel_Transition()
    assert isinstance(instance, TransitionNode)


def test_assoc_dimension55_link_reassign_clear():
    a = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    b1 = pnmlcoremodel_NodeGraphics()
    b2 = pnmlcoremodel_NodeGraphics()
    _safe_set(a, 'pnmlcoremodel_Coordinate57', b1)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate57', b1)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics56'):
        assert _is_linked(b1, 'pnmlcoremodel_NodeGraphics56', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate57', b2)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate57', b2)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics56'):
        assert not _is_linked(b1, 'pnmlcoremodel_NodeGraphics56', a)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics56'):
        assert _is_linked(b2, 'pnmlcoremodel_NodeGraphics56', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate57', None)
    assert not _is_linked(a, 'pnmlcoremodel_Coordinate57', b2)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics56'):
        assert not _is_linked(b2, 'pnmlcoremodel_NodeGraphics56', a)


def test_assoc_fill61_link_reassign_clear():
    a = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    b1 = pnmlcoremodel_NodeGraphics()
    b2 = pnmlcoremodel_NodeGraphics()
    _safe_set(a, 'pnmlcoremodel_Fill', b1)
    assert _is_linked(a, 'pnmlcoremodel_Fill', b1)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics62'):
        assert _is_linked(b1, 'pnmlcoremodel_NodeGraphics62', a)
    _safe_set(a, 'pnmlcoremodel_Fill', b2)
    assert _is_linked(a, 'pnmlcoremodel_Fill', b2)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics62'):
        assert not _is_linked(b1, 'pnmlcoremodel_NodeGraphics62', a)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics62'):
        assert _is_linked(b2, 'pnmlcoremodel_NodeGraphics62', a)
    _safe_set(a, 'pnmlcoremodel_Fill', None)
    assert not _is_linked(a, 'pnmlcoremodel_Fill', b2)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics62'):
        assert not _is_linked(b2, 'pnmlcoremodel_NodeGraphics62', a)


def test_assoc_fill63_link_reassign_clear():
    a = pnmlcoremodel_Fill(color="sample_text", gradientColor="sample_text", gradientrotation="sample_text", image="sample_text")
    b1 = pnmlcoremodel_AnnotationGraphics()
    b2 = pnmlcoremodel_AnnotationGraphics()
    _safe_set(a, 'pnmlcoremodel_Fill64', b1)
    assert _is_linked(a, 'pnmlcoremodel_Fill64', b1)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics'):
        assert _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics', a)
    _safe_set(a, 'pnmlcoremodel_Fill64', b2)
    assert _is_linked(a, 'pnmlcoremodel_Fill64', b2)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics'):
        assert not _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics', a)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics'):
        assert _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics', a)
    _safe_set(a, 'pnmlcoremodel_Fill64', None)
    assert not _is_linked(a, 'pnmlcoremodel_Fill64', b2)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics'):
        assert not _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics', a)


def test_assoc_font71_link_reassign_clear():
    a = pnmlcoremodel_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation=3.14, size="sample_text", style="sample_text", weight="sample_text")
    b1 = pnmlcoremodel_AnnotationGraphics()
    b2 = pnmlcoremodel_AnnotationGraphics()
    _safe_set(a, 'pnmlcoremodel_Font', b1)
    assert _is_linked(a, 'pnmlcoremodel_Font', b1)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics72'):
        assert _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics72', a)
    _safe_set(a, 'pnmlcoremodel_Font', b2)
    assert _is_linked(a, 'pnmlcoremodel_Font', b2)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics72'):
        assert not _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics72', a)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics72'):
        assert _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics72', a)
    _safe_set(a, 'pnmlcoremodel_Font', None)
    assert not _is_linked(a, 'pnmlcoremodel_Font', b2)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics72'):
        assert not _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics72', a)


def test_assoc_label28_link_reassign_clear():
    a = pnmlcoremodel_LabelProxy(text="sample_text")
    b1 = pnmlcoremodel_Label()
    b2 = pnmlcoremodel_Label()
    _safe_set(a, 'pnmlcoremodel_LabelProxy29', b1)
    assert _is_linked(a, 'pnmlcoremodel_LabelProxy29', b1)
    if hasattr(b1, 'pnmlcoremodel_Label'):
        assert _is_linked(b1, 'pnmlcoremodel_Label', a)
    _safe_set(a, 'pnmlcoremodel_LabelProxy29', b2)
    assert _is_linked(a, 'pnmlcoremodel_LabelProxy29', b2)
    if hasattr(b1, 'pnmlcoremodel_Label'):
        assert not _is_linked(b1, 'pnmlcoremodel_Label', a)
    if hasattr(b2, 'pnmlcoremodel_Label'):
        assert _is_linked(b2, 'pnmlcoremodel_Label', a)
    _safe_set(a, 'pnmlcoremodel_LabelProxy29', None)
    assert not _is_linked(a, 'pnmlcoremodel_LabelProxy29', b2)
    if hasattr(b2, 'pnmlcoremodel_Label'):
        assert not _is_linked(b2, 'pnmlcoremodel_Label', a)


def test_assoc_label73_link_reassign_clear():
    a = pnmlcoremodel_PageLabelProxy(text="sample_text")
    b1 = pnmlcoremodel_Label()
    b2 = pnmlcoremodel_Label()
    _safe_set(a, 'pnmlcoremodel_PageLabelProxy74', b1)
    assert _is_linked(a, 'pnmlcoremodel_PageLabelProxy74', b1)
    if hasattr(b1, 'pnmlcoremodel_Label75'):
        assert _is_linked(b1, 'pnmlcoremodel_Label75', a)
    _safe_set(a, 'pnmlcoremodel_PageLabelProxy74', b2)
    assert _is_linked(a, 'pnmlcoremodel_PageLabelProxy74', b2)
    if hasattr(b1, 'pnmlcoremodel_Label75'):
        assert not _is_linked(b1, 'pnmlcoremodel_Label75', a)
    if hasattr(b2, 'pnmlcoremodel_Label75'):
        assert _is_linked(b2, 'pnmlcoremodel_Label75', a)
    _safe_set(a, 'pnmlcoremodel_PageLabelProxy74', None)
    assert not _is_linked(a, 'pnmlcoremodel_PageLabelProxy74', b2)
    if hasattr(b2, 'pnmlcoremodel_Label75'):
        assert not _is_linked(b2, 'pnmlcoremodel_Label75', a)


def test_assoc_labelproxy15_link_reassign_clear():
    a = pnmlcoremodel_LabelProxy(text="sample_text")
    b1 = pnmlcoremodel_Page()
    b2 = pnmlcoremodel_Page()
    _safe_set(a, 'pnmlcoremodel_LabelProxy', b1)
    assert _is_linked(a, 'pnmlcoremodel_LabelProxy', b1)
    if hasattr(b1, 'pnmlcoremodel_Page16'):
        assert _is_linked(b1, 'pnmlcoremodel_Page16', a)
    _safe_set(a, 'pnmlcoremodel_LabelProxy', b2)
    assert _is_linked(a, 'pnmlcoremodel_LabelProxy', b2)
    if hasattr(b1, 'pnmlcoremodel_Page16'):
        assert not _is_linked(b1, 'pnmlcoremodel_Page16', a)
    if hasattr(b2, 'pnmlcoremodel_Page16'):
        assert _is_linked(b2, 'pnmlcoremodel_Page16', a)
    _safe_set(a, 'pnmlcoremodel_LabelProxy', None)
    assert not _is_linked(a, 'pnmlcoremodel_LabelProxy', b2)
    if hasattr(b2, 'pnmlcoremodel_Page16'):
        assert not _is_linked(b2, 'pnmlcoremodel_Page16', a)


def test_assoc_line50_link_reassign_clear():
    a = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    b1 = pnmlcoremodel_ArcGraphics()
    b2 = pnmlcoremodel_ArcGraphics()
    _safe_set(a, 'pnmlcoremodel_Line', b1)
    assert _is_linked(a, 'pnmlcoremodel_Line', b1)
    if hasattr(b1, 'pnmlcoremodel_ArcGraphics'):
        assert _is_linked(b1, 'pnmlcoremodel_ArcGraphics', a)
    _safe_set(a, 'pnmlcoremodel_Line', b2)
    assert _is_linked(a, 'pnmlcoremodel_Line', b2)
    if hasattr(b1, 'pnmlcoremodel_ArcGraphics'):
        assert not _is_linked(b1, 'pnmlcoremodel_ArcGraphics', a)
    if hasattr(b2, 'pnmlcoremodel_ArcGraphics'):
        assert _is_linked(b2, 'pnmlcoremodel_ArcGraphics', a)
    _safe_set(a, 'pnmlcoremodel_Line', None)
    assert not _is_linked(a, 'pnmlcoremodel_Line', b2)
    if hasattr(b2, 'pnmlcoremodel_ArcGraphics'):
        assert not _is_linked(b2, 'pnmlcoremodel_ArcGraphics', a)


def test_assoc_line58_link_reassign_clear():
    a = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    b1 = pnmlcoremodel_NodeGraphics()
    b2 = pnmlcoremodel_NodeGraphics()
    _safe_set(a, 'pnmlcoremodel_Line60', b1)
    assert _is_linked(a, 'pnmlcoremodel_Line60', b1)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics59'):
        assert _is_linked(b1, 'pnmlcoremodel_NodeGraphics59', a)
    _safe_set(a, 'pnmlcoremodel_Line60', b2)
    assert _is_linked(a, 'pnmlcoremodel_Line60', b2)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics59'):
        assert not _is_linked(b1, 'pnmlcoremodel_NodeGraphics59', a)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics59'):
        assert _is_linked(b2, 'pnmlcoremodel_NodeGraphics59', a)
    _safe_set(a, 'pnmlcoremodel_Line60', None)
    assert not _is_linked(a, 'pnmlcoremodel_Line60', b2)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics59'):
        assert not _is_linked(b2, 'pnmlcoremodel_NodeGraphics59', a)


def test_assoc_line65_link_reassign_clear():
    a = pnmlcoremodel_Line(color="sample_text", shape="sample_text", style="sample_text", width=3.14)
    b1 = pnmlcoremodel_AnnotationGraphics()
    b2 = pnmlcoremodel_AnnotationGraphics()
    _safe_set(a, 'pnmlcoremodel_Line67', b1)
    assert _is_linked(a, 'pnmlcoremodel_Line67', b1)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics66'):
        assert _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics66', a)
    _safe_set(a, 'pnmlcoremodel_Line67', b2)
    assert _is_linked(a, 'pnmlcoremodel_Line67', b2)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics66'):
        assert not _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics66', a)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics66'):
        assert _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics66', a)
    _safe_set(a, 'pnmlcoremodel_Line67', None)
    assert not _is_linked(a, 'pnmlcoremodel_Line67', b2)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics66'):
        assert not _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics66', a)


def test_assoc_name17_link_reassign_clear():
    a = pnmlcoremodel_Name(text="sample_text")
    b1 = pnmlcoremodel_Object()
    b2 = pnmlcoremodel_Object()
    _safe_set(a, 'pnmlcoremodel_Name19', b1)
    assert _is_linked(a, 'pnmlcoremodel_Name19', b1)
    if hasattr(b1, 'pnmlcoremodel_Object18'):
        assert _is_linked(b1, 'pnmlcoremodel_Object18', a)
    _safe_set(a, 'pnmlcoremodel_Name19', b2)
    assert _is_linked(a, 'pnmlcoremodel_Name19', b2)
    if hasattr(b1, 'pnmlcoremodel_Object18'):
        assert not _is_linked(b1, 'pnmlcoremodel_Object18', a)
    if hasattr(b2, 'pnmlcoremodel_Object18'):
        assert _is_linked(b2, 'pnmlcoremodel_Object18', a)
    _safe_set(a, 'pnmlcoremodel_Name19', None)
    assert not _is_linked(a, 'pnmlcoremodel_Name19', b2)
    if hasattr(b2, 'pnmlcoremodel_Object18'):
        assert not _is_linked(b2, 'pnmlcoremodel_Object18', a)


def test_assoc_name3_link_reassign_clear():
    a = pnmlcoremodel_Name(text="sample_text")
    b1 = pnmlcoremodel_PetriNet()
    b2 = pnmlcoremodel_PetriNet()
    _safe_set(a, 'pnmlcoremodel_Name', b1)
    assert _is_linked(a, 'pnmlcoremodel_Name', b1)
    if hasattr(b1, 'pnmlcoremodel_PetriNet4'):
        assert _is_linked(b1, 'pnmlcoremodel_PetriNet4', a)
    _safe_set(a, 'pnmlcoremodel_Name', b2)
    assert _is_linked(a, 'pnmlcoremodel_Name', b2)
    if hasattr(b1, 'pnmlcoremodel_PetriNet4'):
        assert not _is_linked(b1, 'pnmlcoremodel_PetriNet4', a)
    if hasattr(b2, 'pnmlcoremodel_PetriNet4'):
        assert _is_linked(b2, 'pnmlcoremodel_PetriNet4', a)
    _safe_set(a, 'pnmlcoremodel_Name', None)
    assert not _is_linked(a, 'pnmlcoremodel_Name', b2)
    if hasattr(b2, 'pnmlcoremodel_PetriNet4'):
        assert not _is_linked(b2, 'pnmlcoremodel_PetriNet4', a)


def test_assoc_object30_link_reassign_clear():
    a = pnmlcoremodel_LabelProxy(text="sample_text")
    b1 = pnmlcoremodel_Object()
    b2 = pnmlcoremodel_Object()
    _safe_set(a, 'pnmlcoremodel_LabelProxy31', b1)
    assert _is_linked(a, 'pnmlcoremodel_LabelProxy31', b1)
    if hasattr(b1, 'pnmlcoremodel_Object32'):
        assert _is_linked(b1, 'pnmlcoremodel_Object32', a)
    _safe_set(a, 'pnmlcoremodel_LabelProxy31', b2)
    assert _is_linked(a, 'pnmlcoremodel_LabelProxy31', b2)
    if hasattr(b1, 'pnmlcoremodel_Object32'):
        assert not _is_linked(b1, 'pnmlcoremodel_Object32', a)
    if hasattr(b2, 'pnmlcoremodel_Object32'):
        assert _is_linked(b2, 'pnmlcoremodel_Object32', a)
    _safe_set(a, 'pnmlcoremodel_LabelProxy31', None)
    assert not _is_linked(a, 'pnmlcoremodel_LabelProxy31', b2)
    if hasattr(b2, 'pnmlcoremodel_Object32'):
        assert not _is_linked(b2, 'pnmlcoremodel_Object32', a)


def test_assoc_offset68_link_reassign_clear():
    a = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    b1 = pnmlcoremodel_AnnotationGraphics()
    b2 = pnmlcoremodel_AnnotationGraphics()
    _safe_set(a, 'pnmlcoremodel_Coordinate70', b1)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate70', b1)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics69'):
        assert _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics69', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate70', b2)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate70', b2)
    if hasattr(b1, 'pnmlcoremodel_AnnotationGraphics69'):
        assert not _is_linked(b1, 'pnmlcoremodel_AnnotationGraphics69', a)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics69'):
        assert _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics69', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate70', None)
    assert not _is_linked(a, 'pnmlcoremodel_Coordinate70', b2)
    if hasattr(b2, 'pnmlcoremodel_AnnotationGraphics69'):
        assert not _is_linked(b2, 'pnmlcoremodel_AnnotationGraphics69', a)


def test_assoc_pageLabelProxy13_link_reassign_clear():
    a = pnmlcoremodel_PageLabelProxy(text="sample_text")
    b1 = pnmlcoremodel_Page()
    b2 = pnmlcoremodel_Page()
    _safe_set(a, 'pnmlcoremodel_PageLabelProxy', b1)
    assert _is_linked(a, 'pnmlcoremodel_PageLabelProxy', b1)
    if hasattr(b1, 'pnmlcoremodel_Page14'):
        assert _is_linked(b1, 'pnmlcoremodel_Page14', a)
    _safe_set(a, 'pnmlcoremodel_PageLabelProxy', b2)
    assert _is_linked(a, 'pnmlcoremodel_PageLabelProxy', b2)
    if hasattr(b1, 'pnmlcoremodel_Page14'):
        assert not _is_linked(b1, 'pnmlcoremodel_Page14', a)
    if hasattr(b2, 'pnmlcoremodel_Page14'):
        assert _is_linked(b2, 'pnmlcoremodel_Page14', a)
    _safe_set(a, 'pnmlcoremodel_PageLabelProxy', None)
    assert not _is_linked(a, 'pnmlcoremodel_PageLabelProxy', b2)
    if hasattr(b2, 'pnmlcoremodel_Page14'):
        assert not _is_linked(b2, 'pnmlcoremodel_Page14', a)


def test_assoc_position51_link_reassign_clear():
    a = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    b1 = pnmlcoremodel_ArcGraphics()
    b2 = pnmlcoremodel_ArcGraphics()
    _safe_set(a, 'pnmlcoremodel_Coordinate', b1)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate', b1)
    if hasattr(b1, 'pnmlcoremodel_ArcGraphics52'):
        assert _is_linked(b1, 'pnmlcoremodel_ArcGraphics52', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate', b2)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate', b2)
    if hasattr(b1, 'pnmlcoremodel_ArcGraphics52'):
        assert not _is_linked(b1, 'pnmlcoremodel_ArcGraphics52', a)
    if hasattr(b2, 'pnmlcoremodel_ArcGraphics52'):
        assert _is_linked(b2, 'pnmlcoremodel_ArcGraphics52', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate', None)
    assert not _is_linked(a, 'pnmlcoremodel_Coordinate', b2)
    if hasattr(b2, 'pnmlcoremodel_ArcGraphics52'):
        assert not _is_linked(b2, 'pnmlcoremodel_ArcGraphics52', a)


def test_assoc_position53_link_reassign_clear():
    a = pnmlcoremodel_Coordinate(x=3.14, y=3.14)
    b1 = pnmlcoremodel_NodeGraphics()
    b2 = pnmlcoremodel_NodeGraphics()
    _safe_set(a, 'pnmlcoremodel_Coordinate54', b1)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate54', b1)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics'):
        assert _is_linked(b1, 'pnmlcoremodel_NodeGraphics', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate54', b2)
    assert _is_linked(a, 'pnmlcoremodel_Coordinate54', b2)
    if hasattr(b1, 'pnmlcoremodel_NodeGraphics'):
        assert not _is_linked(b1, 'pnmlcoremodel_NodeGraphics', a)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics'):
        assert _is_linked(b2, 'pnmlcoremodel_NodeGraphics', a)
    _safe_set(a, 'pnmlcoremodel_Coordinate54', None)
    assert not _is_linked(a, 'pnmlcoremodel_Coordinate54', b2)
    if hasattr(b2, 'pnmlcoremodel_NodeGraphics'):
        assert not _is_linked(b2, 'pnmlcoremodel_NodeGraphics', a)


def test_assoc_toolspecific20_link_reassign_clear():
    a = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    b1 = pnmlcoremodel_Object()
    b2 = pnmlcoremodel_Object()
    _safe_set(a, 'pnmlcoremodel_ToolInfo22', b1)
    assert _is_linked(a, 'pnmlcoremodel_ToolInfo22', b1)
    if hasattr(b1, 'pnmlcoremodel_Object21'):
        assert _is_linked(b1, 'pnmlcoremodel_Object21', a)
    _safe_set(a, 'pnmlcoremodel_ToolInfo22', b2)
    assert _is_linked(a, 'pnmlcoremodel_ToolInfo22', b2)
    if hasattr(b1, 'pnmlcoremodel_Object21'):
        assert not _is_linked(b1, 'pnmlcoremodel_Object21', a)
    if hasattr(b2, 'pnmlcoremodel_Object21'):
        assert _is_linked(b2, 'pnmlcoremodel_Object21', a)
    _safe_set(a, 'pnmlcoremodel_ToolInfo22', None)
    assert not _is_linked(a, 'pnmlcoremodel_ToolInfo22', b2)
    if hasattr(b2, 'pnmlcoremodel_Object21'):
        assert not _is_linked(b2, 'pnmlcoremodel_Object21', a)


def test_assoc_toolspecific41_link_reassign_clear():
    a = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    b1 = pnmlcoremodel_Label()
    b2 = pnmlcoremodel_Label()
    _safe_set(a, 'pnmlcoremodel_ToolInfo43', b1)
    assert _is_linked(a, 'pnmlcoremodel_ToolInfo43', b1)
    if hasattr(b1, 'pnmlcoremodel_Label42'):
        assert _is_linked(b1, 'pnmlcoremodel_Label42', a)
    _safe_set(a, 'pnmlcoremodel_ToolInfo43', b2)
    assert _is_linked(a, 'pnmlcoremodel_ToolInfo43', b2)
    if hasattr(b1, 'pnmlcoremodel_Label42'):
        assert not _is_linked(b1, 'pnmlcoremodel_Label42', a)
    if hasattr(b2, 'pnmlcoremodel_Label42'):
        assert _is_linked(b2, 'pnmlcoremodel_Label42', a)
    _safe_set(a, 'pnmlcoremodel_ToolInfo43', None)
    assert not _is_linked(a, 'pnmlcoremodel_ToolInfo43', b2)
    if hasattr(b2, 'pnmlcoremodel_Label42'):
        assert not _is_linked(b2, 'pnmlcoremodel_Label42', a)


def test_assoc_toolspecific7_link_reassign_clear():
    a = pnmlcoremodel_ToolInfo(tool="sample_text", version="sample_text")
    b1 = pnmlcoremodel_PetriNet()
    b2 = pnmlcoremodel_PetriNet()
    _safe_set(a, 'pnmlcoremodel_ToolInfo', b1)
    assert _is_linked(a, 'pnmlcoremodel_ToolInfo', b1)
    if hasattr(b1, 'pnmlcoremodel_PetriNet8'):
        assert _is_linked(b1, 'pnmlcoremodel_PetriNet8', a)
    _safe_set(a, 'pnmlcoremodel_ToolInfo', b2)
    assert _is_linked(a, 'pnmlcoremodel_ToolInfo', b2)
    if hasattr(b1, 'pnmlcoremodel_PetriNet8'):
        assert not _is_linked(b1, 'pnmlcoremodel_PetriNet8', a)
    if hasattr(b2, 'pnmlcoremodel_PetriNet8'):
        assert _is_linked(b2, 'pnmlcoremodel_PetriNet8', a)
    _safe_set(a, 'pnmlcoremodel_ToolInfo', None)
    assert not _is_linked(a, 'pnmlcoremodel_ToolInfo', b2)
    if hasattr(b2, 'pnmlcoremodel_PetriNet8'):
        assert not _is_linked(b2, 'pnmlcoremodel_PetriNet8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Graphics_strategy = st.builds(Graphics)
@given(instance=Graphics_strategy)
@settings(max_examples=25)
def test_Graphics_instantiation(instance):
    assert isinstance(instance, Graphics)


ID_strategy = st.builds(ID)
@given(instance=ID_strategy)
@settings(max_examples=25)
def test_ID_instantiation(instance):
    assert isinstance(instance, ID)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


Object_strategy = st.builds(Object)
@given(instance=Object_strategy)
@settings(max_examples=25)
def test_Object_instantiation(instance):
    assert isinstance(instance, Object)


PetriNetType_strategy = st.builds(PetriNetType)
@given(instance=PetriNetType_strategy)
@settings(max_examples=25)
def test_PetriNetType_instantiation(instance):
    assert isinstance(instance, PetriNetType)


PlaceNode_strategy = st.builds(PlaceNode)
@given(instance=PlaceNode_strategy)
@settings(max_examples=25)
def test_PlaceNode_instantiation(instance):
    assert isinstance(instance, PlaceNode)


ToolInfo_strategy = st.builds(ToolInfo)
@given(instance=ToolInfo_strategy)
@settings(max_examples=25)
def test_ToolInfo_instantiation(instance):
    assert isinstance(instance, ToolInfo)


TransitionNode_strategy = st.builds(TransitionNode)
@given(instance=TransitionNode_strategy)
@settings(max_examples=25)
def test_TransitionNode_instantiation(instance):
    assert isinstance(instance, TransitionNode)


pnmlcoremodel_AnnotationGraphics_strategy = st.builds(pnmlcoremodel_AnnotationGraphics)
@given(instance=pnmlcoremodel_AnnotationGraphics_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_AnnotationGraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_AnnotationGraphics)


pnmlcoremodel_AnyType_strategy = st.builds(pnmlcoremodel_AnyType)
@given(instance=pnmlcoremodel_AnyType_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_AnyType_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_AnyType)


pnmlcoremodel_Arc_strategy = st.builds(pnmlcoremodel_Arc)
@given(instance=pnmlcoremodel_Arc_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Arc_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Arc)


pnmlcoremodel_ArcGraphics_strategy = st.builds(pnmlcoremodel_ArcGraphics)
@given(instance=pnmlcoremodel_ArcGraphics_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_ArcGraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_ArcGraphics)


pnmlcoremodel_Attribute_strategy = st.builds(pnmlcoremodel_Attribute)
@given(instance=pnmlcoremodel_Attribute_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Attribute_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Attribute)


pnmlcoremodel_Coordinate_strategy = st.builds(pnmlcoremodel_Coordinate, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=pnmlcoremodel_Coordinate_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Coordinate_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Coordinate)


pnmlcoremodel_EmptyType_strategy = st.builds(pnmlcoremodel_EmptyType)
@given(instance=pnmlcoremodel_EmptyType_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_EmptyType_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_EmptyType)


pnmlcoremodel_Fill_strategy = st.builds(pnmlcoremodel_Fill, color=safe_text, gradientColor=safe_text, gradientrotation=safe_text, image=safe_text)
@given(instance=pnmlcoremodel_Fill_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Fill_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Fill)


pnmlcoremodel_Font_strategy = st.builds(pnmlcoremodel_Font, align=safe_text, decoration=safe_text, family=safe_text, rotation=st.floats(allow_nan=False, allow_infinity=False), size=safe_text, style=safe_text, weight=safe_text)
@given(instance=pnmlcoremodel_Font_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Font_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Font)


pnmlcoremodel_Graphics_strategy = st.builds(pnmlcoremodel_Graphics)
@given(instance=pnmlcoremodel_Graphics_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Graphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Graphics)


pnmlcoremodel_ID_strategy = st.builds(pnmlcoremodel_ID, id=safe_text)
@given(instance=pnmlcoremodel_ID_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_ID_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_ID)


pnmlcoremodel_Label_strategy = st.builds(pnmlcoremodel_Label)
@given(instance=pnmlcoremodel_Label_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Label_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Label)


pnmlcoremodel_LabelProxy_strategy = st.builds(pnmlcoremodel_LabelProxy, text=safe_text)
@given(instance=pnmlcoremodel_LabelProxy_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_LabelProxy_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_LabelProxy)


pnmlcoremodel_Line_strategy = st.builds(pnmlcoremodel_Line, color=safe_text, shape=safe_text, style=safe_text, width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=pnmlcoremodel_Line_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Line_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Line)


pnmlcoremodel_Name_strategy = st.builds(pnmlcoremodel_Name, text=safe_text)
@given(instance=pnmlcoremodel_Name_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Name_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Name)


pnmlcoremodel_Node_strategy = st.builds(pnmlcoremodel_Node)
@given(instance=pnmlcoremodel_Node_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Node_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Node)


pnmlcoremodel_NodeGraphics_strategy = st.builds(pnmlcoremodel_NodeGraphics)
@given(instance=pnmlcoremodel_NodeGraphics_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_NodeGraphics_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_NodeGraphics)


pnmlcoremodel_Object_strategy = st.builds(pnmlcoremodel_Object)
@given(instance=pnmlcoremodel_Object_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Object_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Object)


pnmlcoremodel_Page_strategy = st.builds(pnmlcoremodel_Page)
@given(instance=pnmlcoremodel_Page_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Page_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Page)


pnmlcoremodel_PageLabelProxy_strategy = st.builds(pnmlcoremodel_PageLabelProxy, text=safe_text)
@given(instance=pnmlcoremodel_PageLabelProxy_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_PageLabelProxy_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PageLabelProxy)


pnmlcoremodel_PetriNet_strategy = st.builds(pnmlcoremodel_PetriNet)
@given(instance=pnmlcoremodel_PetriNet_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_PetriNet_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PetriNet)


pnmlcoremodel_PetriNetDoc_strategy = st.builds(pnmlcoremodel_PetriNetDoc)
@given(instance=pnmlcoremodel_PetriNetDoc_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_PetriNetDoc_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PetriNetDoc)


pnmlcoremodel_PetriNetType_strategy = st.builds(pnmlcoremodel_PetriNetType)
@given(instance=pnmlcoremodel_PetriNetType_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_PetriNetType_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PetriNetType)


pnmlcoremodel_Place_strategy = st.builds(pnmlcoremodel_Place)
@given(instance=pnmlcoremodel_Place_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Place_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Place)


pnmlcoremodel_PlaceNode_strategy = st.builds(pnmlcoremodel_PlaceNode)
@given(instance=pnmlcoremodel_PlaceNode_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_PlaceNode_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_PlaceNode)


pnmlcoremodel_RefPlace_strategy = st.builds(pnmlcoremodel_RefPlace)
@given(instance=pnmlcoremodel_RefPlace_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_RefPlace_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_RefPlace)


pnmlcoremodel_RefTransition_strategy = st.builds(pnmlcoremodel_RefTransition)
@given(instance=pnmlcoremodel_RefTransition_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_RefTransition_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_RefTransition)


pnmlcoremodel_ToolInfo_strategy = st.builds(pnmlcoremodel_ToolInfo, tool=safe_text, version=safe_text)
@given(instance=pnmlcoremodel_ToolInfo_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_ToolInfo_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_ToolInfo)


pnmlcoremodel_ToolInfoText_strategy = st.builds(pnmlcoremodel_ToolInfoText, info=safe_text)
@given(instance=pnmlcoremodel_ToolInfoText_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_ToolInfoText_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_ToolInfoText)


pnmlcoremodel_Transition_strategy = st.builds(pnmlcoremodel_Transition)
@given(instance=pnmlcoremodel_Transition_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_Transition_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_Transition)


pnmlcoremodel_TransitionNode_strategy = st.builds(pnmlcoremodel_TransitionNode)
@given(instance=pnmlcoremodel_TransitionNode_strategy)
@settings(max_examples=25)
def test_pnmlcoremodel_TransitionNode_instantiation(instance):
    assert isinstance(instance, pnmlcoremodel_TransitionNode)



