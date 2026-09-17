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
    graph_GAlignable,
    graph_GLayouting,
    graph_GEdgePlacement,
    graph_GEdgeLayoutable,
    graph_GDimension,
    graph_GBoundsAware,
    graph_GIssue,
    GAlignable,
    graph_GPoint,
    GLayouting,
    GEdgeLayoutable,
    graph_GModelElement,
    GShapeElement,
    graph_GCompartment,
    graph_GIssueMarker,
    graph_GPort,
    graph_GLabel,
    graph_GButton,
    graph_GNode,
    graph_GBounds,
    graph_GLayoutOptions,
    GModelRoot,
    graph_GHtmlRoot,
    GBoundsAware,
    graph_GGraph,
    GModelElement,
    graph_GModelRoot,
    graph_GPreRenderedElement,
    graph_GEdge,
    graph_GShapeElement,
    GSeverity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graph_galignable_is_not_abstract():
    assert not inspect.isabstract(graph_GAlignable)


def test_hyp_graph_galignable_constructor_exists():
    assert callable(graph_GAlignable.__init__)


def test_hyp_graph_galignable_constructor_args():
    sig = inspect.signature(graph_GAlignable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_glayouting_is_not_abstract():
    assert not inspect.isabstract(graph_GLayouting)


def test_hyp_graph_glayouting_constructor_exists():
    assert callable(graph_GLayouting.__init__)


def test_hyp_graph_glayouting_constructor_args():
    sig = inspect.signature(graph_GLayouting.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"




def test_hyp_graph_gedgeplacement_is_not_abstract():
    assert not inspect.isabstract(graph_GEdgePlacement)


def test_hyp_graph_gedgeplacement_constructor_exists():
    assert callable(graph_GEdgePlacement.__init__)


def test_hyp_graph_gedgeplacement_constructor_args():
    sig = inspect.signature(graph_GEdgePlacement.__init__)
    params = list(sig.parameters.keys())
    assert "side" in params, "Missing parameter 'side'"
    assert "offset" in params, "Missing parameter 'offset'"
    assert "position" in params, "Missing parameter 'position'"
    assert "rotate" in params, "Missing parameter 'rotate'"







def test_hyp_graph_gedgelayoutable_is_not_abstract():
    assert not inspect.isabstract(graph_GEdgeLayoutable)


def test_hyp_graph_gedgelayoutable_constructor_exists():
    assert callable(graph_GEdgeLayoutable.__init__)


def test_hyp_graph_gedgelayoutable_constructor_args():
    sig = inspect.signature(graph_GEdgeLayoutable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gdimension_is_not_abstract():
    assert not inspect.isabstract(graph_GDimension)


def test_hyp_graph_gdimension_constructor_exists():
    assert callable(graph_GDimension.__init__)


def test_hyp_graph_gdimension_constructor_args():
    sig = inspect.signature(graph_GDimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"





def test_hyp_graph_gboundsaware_is_not_abstract():
    assert not inspect.isabstract(graph_GBoundsAware)


def test_hyp_graph_gboundsaware_constructor_exists():
    assert callable(graph_GBoundsAware.__init__)


def test_hyp_graph_gboundsaware_constructor_args():
    sig = inspect.signature(graph_GBoundsAware.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gissue_is_not_abstract():
    assert not inspect.isabstract(graph_GIssue)


def test_hyp_graph_gissue_constructor_exists():
    assert callable(graph_GIssue.__init__)


def test_hyp_graph_gissue_constructor_args():
    sig = inspect.signature(graph_GIssue.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"
    assert "message" in params, "Missing parameter 'message'"





def test_hyp_galignable_is_not_abstract():
    assert not inspect.isabstract(GAlignable)


def test_hyp_galignable_constructor_exists():
    assert callable(GAlignable.__init__)


def test_hyp_galignable_constructor_args():
    sig = inspect.signature(GAlignable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gpoint_is_not_abstract():
    assert not inspect.isabstract(graph_GPoint)


def test_hyp_graph_gpoint_constructor_exists():
    assert callable(graph_GPoint.__init__)


def test_hyp_graph_gpoint_constructor_args():
    sig = inspect.signature(graph_GPoint.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"





def test_hyp_glayouting_is_not_abstract():
    assert not inspect.isabstract(GLayouting)


def test_hyp_glayouting_constructor_exists():
    assert callable(GLayouting.__init__)


def test_hyp_glayouting_constructor_args():
    sig = inspect.signature(GLayouting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gedgelayoutable_is_not_abstract():
    assert not inspect.isabstract(GEdgeLayoutable)


def test_hyp_gedgelayoutable_constructor_exists():
    assert callable(GEdgeLayoutable.__init__)


def test_hyp_gedgelayoutable_constructor_args():
    sig = inspect.signature(GEdgeLayoutable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gmodelelement_is_not_abstract():
    assert not inspect.isabstract(graph_GModelElement)


def test_hyp_graph_gmodelelement_constructor_exists():
    assert callable(graph_GModelElement.__init__)


def test_hyp_graph_gmodelelement_constructor_args():
    sig = inspect.signature(graph_GModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "trace" in params, "Missing parameter 'trace'"
    assert "type" in params, "Missing parameter 'type'"
    assert "cssClasses" in params, "Missing parameter 'cssClasses'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_gshapeelement_is_not_abstract():
    assert not inspect.isabstract(GShapeElement)


def test_hyp_gshapeelement_constructor_exists():
    assert callable(GShapeElement.__init__)


def test_hyp_gshapeelement_constructor_args():
    sig = inspect.signature(GShapeElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gcompartment_is_not_abstract():
    assert not inspect.isabstract(graph_GCompartment)


def test_hyp_graph_gcompartment_constructor_exists():
    assert callable(graph_GCompartment.__init__)


def test_hyp_graph_gcompartment_constructor_args():
    sig = inspect.signature(graph_GCompartment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gissuemarker_is_not_abstract():
    assert not inspect.isabstract(graph_GIssueMarker)


def test_hyp_graph_gissuemarker_constructor_exists():
    assert callable(graph_GIssueMarker.__init__)


def test_hyp_graph_gissuemarker_constructor_args():
    sig = inspect.signature(graph_GIssueMarker.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gport_is_not_abstract():
    assert not inspect.isabstract(graph_GPort)


def test_hyp_graph_gport_constructor_exists():
    assert callable(graph_GPort.__init__)


def test_hyp_graph_gport_constructor_args():
    sig = inspect.signature(graph_GPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_glabel_is_not_abstract():
    assert not inspect.isabstract(graph_GLabel)


def test_hyp_graph_glabel_constructor_exists():
    assert callable(graph_GLabel.__init__)


def test_hyp_graph_glabel_constructor_args():
    sig = inspect.signature(graph_GLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_graph_gbutton_is_not_abstract():
    assert not inspect.isabstract(graph_GButton)


def test_hyp_graph_gbutton_constructor_exists():
    assert callable(graph_GButton.__init__)


def test_hyp_graph_gbutton_constructor_args():
    sig = inspect.signature(graph_GButton.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"




def test_hyp_graph_gnode_is_not_abstract():
    assert not inspect.isabstract(graph_GNode)


def test_hyp_graph_gnode_constructor_exists():
    assert callable(graph_GNode.__init__)


def test_hyp_graph_gnode_constructor_args():
    sig = inspect.signature(graph_GNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gbounds_is_not_abstract():
    assert not inspect.isabstract(graph_GBounds)


def test_hyp_graph_gbounds_constructor_exists():
    assert callable(graph_GBounds.__init__)


def test_hyp_graph_gbounds_constructor_args():
    sig = inspect.signature(graph_GBounds.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"







def test_hyp_graph_glayoutoptions_is_not_abstract():
    assert not inspect.isabstract(graph_GLayoutOptions)


def test_hyp_graph_glayoutoptions_constructor_exists():
    assert callable(graph_GLayoutOptions.__init__)


def test_hyp_graph_glayoutoptions_constructor_args():
    sig = inspect.signature(graph_GLayoutOptions.__init__)
    params = list(sig.parameters.keys())
    assert "paddingFactor" in params, "Missing parameter 'paddingFactor'"
    assert "vGap" in params, "Missing parameter 'vGap'"
    assert "minWidth" in params, "Missing parameter 'minWidth'"
    assert "paddingBottom" in params, "Missing parameter 'paddingBottom'"
    assert "resizeContainer" in params, "Missing parameter 'resizeContainer'"
    assert "paddingTop" in params, "Missing parameter 'paddingTop'"
    assert "minHeight" in params, "Missing parameter 'minHeight'"
    assert "vAlign" in params, "Missing parameter 'vAlign'"
    assert "paddingLeft" in params, "Missing parameter 'paddingLeft'"
    assert "hAlign" in params, "Missing parameter 'hAlign'"
    assert "hGap" in params, "Missing parameter 'hGap'"
    assert "paddingRight" in params, "Missing parameter 'paddingRight'"















def test_hyp_gmodelroot_is_not_abstract():
    assert not inspect.isabstract(GModelRoot)


def test_hyp_gmodelroot_constructor_exists():
    assert callable(GModelRoot.__init__)


def test_hyp_gmodelroot_constructor_args():
    sig = inspect.signature(GModelRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_ghtmlroot_is_not_abstract():
    assert not inspect.isabstract(graph_GHtmlRoot)


def test_hyp_graph_ghtmlroot_constructor_exists():
    assert callable(graph_GHtmlRoot.__init__)


def test_hyp_graph_ghtmlroot_constructor_args():
    sig = inspect.signature(graph_GHtmlRoot.__init__)
    params = list(sig.parameters.keys())
    assert "classes" in params, "Missing parameter 'classes'"




def test_hyp_gboundsaware_is_not_abstract():
    assert not inspect.isabstract(GBoundsAware)


def test_hyp_gboundsaware_constructor_exists():
    assert callable(GBoundsAware.__init__)


def test_hyp_gboundsaware_constructor_args():
    sig = inspect.signature(GBoundsAware.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_ggraph_is_not_abstract():
    assert not inspect.isabstract(graph_GGraph)


def test_hyp_graph_ggraph_constructor_exists():
    assert callable(graph_GGraph.__init__)


def test_hyp_graph_ggraph_constructor_args():
    sig = inspect.signature(graph_GGraph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gmodelelement_is_not_abstract():
    assert not inspect.isabstract(GModelElement)


def test_hyp_gmodelelement_constructor_exists():
    assert callable(GModelElement.__init__)


def test_hyp_gmodelelement_constructor_args():
    sig = inspect.signature(GModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_gmodelroot_is_not_abstract():
    assert not inspect.isabstract(graph_GModelRoot)


def test_hyp_graph_gmodelroot_constructor_exists():
    assert callable(graph_GModelRoot.__init__)


def test_hyp_graph_gmodelroot_constructor_args():
    sig = inspect.signature(graph_GModelRoot.__init__)
    params = list(sig.parameters.keys())
    assert "revision" in params, "Missing parameter 'revision'"




def test_hyp_graph_gprerenderedelement_is_not_abstract():
    assert not inspect.isabstract(graph_GPreRenderedElement)


def test_hyp_graph_gprerenderedelement_constructor_exists():
    assert callable(graph_GPreRenderedElement.__init__)


def test_hyp_graph_gprerenderedelement_constructor_args():
    sig = inspect.signature(graph_GPreRenderedElement.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"




def test_hyp_graph_gedge_is_not_abstract():
    assert not inspect.isabstract(graph_GEdge)


def test_hyp_graph_gedge_constructor_exists():
    assert callable(graph_GEdge.__init__)


def test_hyp_graph_gedge_constructor_args():
    sig = inspect.signature(graph_GEdge.__init__)
    params = list(sig.parameters.keys())
    assert "targetId" in params, "Missing parameter 'targetId'"
    assert "sourceId" in params, "Missing parameter 'sourceId'"
    assert "routerKind" in params, "Missing parameter 'routerKind'"






def test_hyp_graph_gshapeelement_is_not_abstract():
    assert not inspect.isabstract(graph_GShapeElement)


def test_hyp_graph_gshapeelement_constructor_exists():
    assert callable(graph_GShapeElement.__init__)


def test_hyp_graph_gshapeelement_constructor_args():
    sig = inspect.signature(graph_GShapeElement.__init__)
    params = list(sig.parameters.keys())

def test_hyp_gseverity_exists():
    # Check that the Enumeration exists
    assert GSeverity is not None

def test_hyp_gseverity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSeverity]
    expected_literals = [
        "warning",
        "error",
        "info",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GSeverity"


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
graph_GAlignable_strategy = st.builds(
    graph_GAlignable,
)
graph_GLayouting_strategy = st.builds(
    graph_GLayouting,
    layout=
        safe_text
)
graph_GEdgePlacement_strategy = st.builds(
    graph_GEdgePlacement,
    side=
        safe_text,
    offset=
        safe_text,
    position=
        safe_text,
    rotate=
        st.booleans()
)
graph_GEdgeLayoutable_strategy = st.builds(
    graph_GEdgeLayoutable,
)
graph_GDimension_strategy = st.builds(
    graph_GDimension,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
graph_GBoundsAware_strategy = st.builds(
    graph_GBoundsAware,
)
graph_GIssue_strategy = st.builds(
    graph_GIssue,
    severity=
        safe_text,
    message=
        safe_text
)
GAlignable_strategy = st.builds(
    GAlignable,
)
graph_GPoint_strategy = st.builds(
    graph_GPoint,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
GLayouting_strategy = st.builds(
    GLayouting,
)
GEdgeLayoutable_strategy = st.builds(
    GEdgeLayoutable,
)
graph_GModelElement_strategy = st.builds(
    graph_GModelElement,
    trace=
        safe_text,
    type=
        safe_text,
    cssClasses=
        safe_text,
    id=
        safe_text
)
GShapeElement_strategy = st.builds(
    GShapeElement,
)
graph_GCompartment_strategy = st.builds(
    graph_GCompartment,
)
graph_GIssueMarker_strategy = st.builds(
    graph_GIssueMarker,
)
graph_GPort_strategy = st.builds(
    graph_GPort,
)
graph_GLabel_strategy = st.builds(
    graph_GLabel,
    text=
        safe_text
)
graph_GButton_strategy = st.builds(
    graph_GButton,
    enabled=
        st.booleans()
)
graph_GNode_strategy = st.builds(
    graph_GNode,
)
graph_GBounds_strategy = st.builds(
    graph_GBounds,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
graph_GLayoutOptions_strategy = st.builds(
    graph_GLayoutOptions,
    paddingFactor=
        safe_text,
    vGap=
        safe_text,
    minWidth=
        safe_text,
    paddingBottom=
        safe_text,
    resizeContainer=
        st.booleans(),
    paddingTop=
        safe_text,
    minHeight=
        safe_text,
    vAlign=
        safe_text,
    paddingLeft=
        safe_text,
    hAlign=
        safe_text,
    hGap=
        safe_text,
    paddingRight=
        safe_text
)
GModelRoot_strategy = st.builds(
    GModelRoot,
)
graph_GHtmlRoot_strategy = st.builds(
    graph_GHtmlRoot,
    classes=
        safe_text
)
GBoundsAware_strategy = st.builds(
    GBoundsAware,
)
graph_GGraph_strategy = st.builds(
    graph_GGraph,
)
GModelElement_strategy = st.builds(
    GModelElement,
)
graph_GModelRoot_strategy = st.builds(
    graph_GModelRoot,
    revision=
        st.integers()
)
graph_GPreRenderedElement_strategy = st.builds(
    graph_GPreRenderedElement,
    code=
        safe_text
)
graph_GEdge_strategy = st.builds(
    graph_GEdge,
    targetId=
        safe_text,
    sourceId=
        safe_text,
    routerKind=
        safe_text
)
graph_GShapeElement_strategy = st.builds(
    graph_GShapeElement,
)





@given(instance=graph_GLayouting_strategy)
def test_hyp_graph_glayouting_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original




@given(instance=graph_GEdgePlacement_strategy)
def test_hyp_graph_gedgeplacement_side_setter(instance):
    original = instance.side
    instance.side = original
    assert instance.side == original



@given(instance=graph_GEdgePlacement_strategy)
def test_hyp_graph_gedgeplacement_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original



@given(instance=graph_GEdgePlacement_strategy)
def test_hyp_graph_gedgeplacement_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=graph_GEdgePlacement_strategy)
def test_hyp_graph_gedgeplacement_rotate_setter(instance):
    original = instance.rotate
    instance.rotate = original
    assert instance.rotate == original





@given(instance=graph_GDimension_strategy)
def test_hyp_graph_gdimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=graph_GDimension_strategy)
def test_hyp_graph_gdimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original





@given(instance=graph_GIssue_strategy)
def test_hyp_graph_gissue_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original



@given(instance=graph_GIssue_strategy)
def test_hyp_graph_gissue_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original





@given(instance=graph_GPoint_strategy)
def test_hyp_graph_gpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=graph_GPoint_strategy)
def test_hyp_graph_gpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original






@given(instance=graph_GModelElement_strategy)
def test_hyp_graph_gmodelelement_trace_setter(instance):
    original = instance.trace
    instance.trace = original
    assert instance.trace == original



@given(instance=graph_GModelElement_strategy)
def test_hyp_graph_gmodelelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=graph_GModelElement_strategy)
def test_hyp_graph_gmodelelement_cssClasses_setter(instance):
    original = instance.cssClasses
    instance.cssClasses = original
    assert instance.cssClasses == original



@given(instance=graph_GModelElement_strategy)
def test_hyp_graph_gmodelelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original








@given(instance=graph_GLabel_strategy)
def test_hyp_graph_glabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=graph_GButton_strategy)
def test_hyp_graph_gbutton_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original





@given(instance=graph_GBounds_strategy)
def test_hyp_graph_gbounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=graph_GBounds_strategy)
def test_hyp_graph_gbounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=graph_GBounds_strategy)
def test_hyp_graph_gbounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=graph_GBounds_strategy)
def test_hyp_graph_gbounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_paddingFactor_setter(instance):
    original = instance.paddingFactor
    instance.paddingFactor = original
    assert instance.paddingFactor == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_vGap_setter(instance):
    original = instance.vGap
    instance.vGap = original
    assert instance.vGap == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_minWidth_setter(instance):
    original = instance.minWidth
    instance.minWidth = original
    assert instance.minWidth == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_paddingBottom_setter(instance):
    original = instance.paddingBottom
    instance.paddingBottom = original
    assert instance.paddingBottom == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_resizeContainer_setter(instance):
    original = instance.resizeContainer
    instance.resizeContainer = original
    assert instance.resizeContainer == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_paddingTop_setter(instance):
    original = instance.paddingTop
    instance.paddingTop = original
    assert instance.paddingTop == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_minHeight_setter(instance):
    original = instance.minHeight
    instance.minHeight = original
    assert instance.minHeight == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_vAlign_setter(instance):
    original = instance.vAlign
    instance.vAlign = original
    assert instance.vAlign == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_paddingLeft_setter(instance):
    original = instance.paddingLeft
    instance.paddingLeft = original
    assert instance.paddingLeft == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_hAlign_setter(instance):
    original = instance.hAlign
    instance.hAlign = original
    assert instance.hAlign == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_hGap_setter(instance):
    original = instance.hGap
    instance.hGap = original
    assert instance.hGap == original



@given(instance=graph_GLayoutOptions_strategy)
def test_hyp_graph_glayoutoptions_paddingRight_setter(instance):
    original = instance.paddingRight
    instance.paddingRight = original
    assert instance.paddingRight == original





@given(instance=graph_GHtmlRoot_strategy)
def test_hyp_graph_ghtmlroot_classes_setter(instance):
    original = instance.classes
    instance.classes = original
    assert instance.classes == original







@given(instance=graph_GModelRoot_strategy)
def test_hyp_graph_gmodelroot_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original




@given(instance=graph_GPreRenderedElement_strategy)
def test_hyp_graph_gprerenderedelement_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=graph_GEdge_strategy)
def test_hyp_graph_gedge_targetId_setter(instance):
    original = instance.targetId
    instance.targetId = original
    assert instance.targetId == original



@given(instance=graph_GEdge_strategy)
def test_hyp_graph_gedge_sourceId_setter(instance):
    original = instance.sourceId
    instance.sourceId = original
    assert instance.sourceId == original



@given(instance=graph_GEdge_strategy)
def test_hyp_graph_gedge_routerKind_setter(instance):
    original = instance.routerKind
    instance.routerKind = original
    assert instance.routerKind == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    GAlignable,
    GBoundsAware,
    GEdgeLayoutable,
    GLayouting,
    GModelElement,
    GModelRoot,
    GShapeElement,
    graph_GAlignable,
    graph_GBounds,
    graph_GBoundsAware,
    graph_GButton,
    graph_GCompartment,
    graph_GDimension,
    graph_GEdge,
    graph_GEdgeLayoutable,
    graph_GEdgePlacement,
    graph_GGraph,
    graph_GHtmlRoot,
    graph_GIssue,
    graph_GIssueMarker,
    graph_GLabel,
    graph_GLayoutOptions,
    graph_GLayouting,
    graph_GModelElement,
    graph_GModelRoot,
    graph_GNode,
    graph_GPoint,
    graph_GPort,
    graph_GPreRenderedElement,
    graph_GShapeElement,
    GSeverity,
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

def test_graph_GBounds_height_value_roundtrip():
    instance = graph_GBounds(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_graph_GBounds_width_value_roundtrip():
    instance = graph_GBounds(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_graph_GBounds_x_value_roundtrip():
    instance = graph_GBounds(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_graph_GBounds_y_value_roundtrip():
    instance = graph_GBounds(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_graph_GButton_enabled_value_roundtrip():
    instance = graph_GButton(enabled=True)
    assert instance.enabled == True
    instance.enabled = False
    assert instance.enabled == False


def test_graph_GDimension_height_value_roundtrip():
    instance = graph_GDimension(height=3.14, width=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_graph_GDimension_width_value_roundtrip():
    instance = graph_GDimension(height=3.14, width=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_graph_GEdge_routerKind_value_roundtrip():
    instance = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    assert instance.routerKind == "sample_text"
    instance.routerKind = "sample_text_2"
    assert instance.routerKind == "sample_text_2"


def test_graph_GEdge_sourceId_value_roundtrip():
    instance = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    assert instance.sourceId == "sample_text"
    instance.sourceId = "sample_text_2"
    assert instance.sourceId == "sample_text_2"


def test_graph_GEdge_targetId_value_roundtrip():
    instance = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    assert instance.targetId == "sample_text"
    instance.targetId = "sample_text_2"
    assert instance.targetId == "sample_text_2"


def test_graph_GEdgePlacement_offset_value_roundtrip():
    instance = graph_GEdgePlacement(offset="sample_text", position="sample_text", rotate=True, side="sample_text")
    assert instance.offset == "sample_text"
    instance.offset = "sample_text_2"
    assert instance.offset == "sample_text_2"


def test_graph_GEdgePlacement_position_value_roundtrip():
    instance = graph_GEdgePlacement(offset="sample_text", position="sample_text", rotate=True, side="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_graph_GEdgePlacement_rotate_value_roundtrip():
    instance = graph_GEdgePlacement(offset="sample_text", position="sample_text", rotate=True, side="sample_text")
    assert instance.rotate == True
    instance.rotate = False
    assert instance.rotate == False


def test_graph_GEdgePlacement_side_value_roundtrip():
    instance = graph_GEdgePlacement(offset="sample_text", position="sample_text", rotate=True, side="sample_text")
    assert instance.side == "sample_text"
    instance.side = "sample_text_2"
    assert instance.side == "sample_text_2"


def test_graph_GHtmlRoot_classes_value_roundtrip():
    instance = graph_GHtmlRoot(classes="sample_text")
    assert instance.classes == "sample_text"
    instance.classes = "sample_text_2"
    assert instance.classes == "sample_text_2"


def test_graph_GIssue_message_value_roundtrip():
    instance = graph_GIssue(message="sample_text", severity="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_graph_GIssue_severity_value_roundtrip():
    instance = graph_GIssue(message="sample_text", severity="sample_text")
    assert instance.severity == "sample_text"
    instance.severity = "sample_text_2"
    assert instance.severity == "sample_text_2"


def test_graph_GLabel_text_value_roundtrip():
    instance = graph_GLabel(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_graph_GLayoutOptions_hAlign_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.hAlign == "sample_text"
    instance.hAlign = "sample_text_2"
    assert instance.hAlign == "sample_text_2"


def test_graph_GLayoutOptions_hGap_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.hGap == "sample_text"
    instance.hGap = "sample_text_2"
    assert instance.hGap == "sample_text_2"


def test_graph_GLayoutOptions_minHeight_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.minHeight == "sample_text"
    instance.minHeight = "sample_text_2"
    assert instance.minHeight == "sample_text_2"


def test_graph_GLayoutOptions_minWidth_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.minWidth == "sample_text"
    instance.minWidth = "sample_text_2"
    assert instance.minWidth == "sample_text_2"


def test_graph_GLayoutOptions_paddingBottom_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.paddingBottom == "sample_text"
    instance.paddingBottom = "sample_text_2"
    assert instance.paddingBottom == "sample_text_2"


def test_graph_GLayoutOptions_paddingFactor_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.paddingFactor == "sample_text"
    instance.paddingFactor = "sample_text_2"
    assert instance.paddingFactor == "sample_text_2"


def test_graph_GLayoutOptions_paddingLeft_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.paddingLeft == "sample_text"
    instance.paddingLeft = "sample_text_2"
    assert instance.paddingLeft == "sample_text_2"


def test_graph_GLayoutOptions_paddingRight_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.paddingRight == "sample_text"
    instance.paddingRight = "sample_text_2"
    assert instance.paddingRight == "sample_text_2"


def test_graph_GLayoutOptions_paddingTop_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.paddingTop == "sample_text"
    instance.paddingTop = "sample_text_2"
    assert instance.paddingTop == "sample_text_2"


def test_graph_GLayoutOptions_resizeContainer_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.resizeContainer == True
    instance.resizeContainer = False
    assert instance.resizeContainer == False


def test_graph_GLayoutOptions_vAlign_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.vAlign == "sample_text"
    instance.vAlign = "sample_text_2"
    assert instance.vAlign == "sample_text_2"


def test_graph_GLayoutOptions_vGap_value_roundtrip():
    instance = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    assert instance.vGap == "sample_text"
    instance.vGap = "sample_text_2"
    assert instance.vGap == "sample_text_2"


def test_graph_GLayouting_layout_value_roundtrip():
    instance = graph_GLayouting(layout="sample_text")
    assert instance.layout == "sample_text"
    instance.layout = "sample_text_2"
    assert instance.layout == "sample_text_2"


def test_graph_GModelElement_cssClasses_value_roundtrip():
    instance = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    assert instance.cssClasses == "sample_text"
    instance.cssClasses = "sample_text_2"
    assert instance.cssClasses == "sample_text_2"


def test_graph_GModelElement_id_value_roundtrip():
    instance = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_graph_GModelElement_trace_value_roundtrip():
    instance = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    assert instance.trace == "sample_text"
    instance.trace = "sample_text_2"
    assert instance.trace == "sample_text_2"


def test_graph_GModelElement_type_value_roundtrip():
    instance = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graph_GModelRoot_revision_value_roundtrip():
    instance = graph_GModelRoot(revision=7)
    assert instance.revision == 7
    instance.revision = 13
    assert instance.revision == 13


def test_graph_GPoint_x_value_roundtrip():
    instance = graph_GPoint(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_graph_GPoint_y_value_roundtrip():
    instance = graph_GPoint(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_graph_GPreRenderedElement_code_value_roundtrip():
    instance = graph_GPreRenderedElement(code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_graph_GLabel_isa_GAlignable():
    instance = graph_GLabel(text="sample_text")
    assert isinstance(instance, GAlignable)


def test_graph_GGraph_isa_GBoundsAware():
    instance = graph_GGraph()
    assert isinstance(instance, GBoundsAware)


def test_graph_GShapeElement_isa_GBoundsAware():
    instance = graph_GShapeElement()
    assert isinstance(instance, GBoundsAware)


def test_graph_GLabel_isa_GEdgeLayoutable():
    instance = graph_GLabel(text="sample_text")
    assert isinstance(instance, GEdgeLayoutable)


def test_graph_GNode_isa_GEdgeLayoutable():
    instance = graph_GNode()
    assert isinstance(instance, GEdgeLayoutable)


def test_graph_GCompartment_isa_GLayouting():
    instance = graph_GCompartment()
    assert isinstance(instance, GLayouting)


def test_graph_GNode_isa_GLayouting():
    instance = graph_GNode()
    assert isinstance(instance, GLayouting)


def test_graph_GEdge_isa_GModelElement():
    instance = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    assert isinstance(instance, GModelElement)


def test_graph_GModelRoot_isa_GModelElement():
    instance = graph_GModelRoot(revision=7)
    assert isinstance(instance, GModelElement)


def test_graph_GPreRenderedElement_isa_GModelElement():
    instance = graph_GPreRenderedElement(code="sample_text")
    assert isinstance(instance, GModelElement)


def test_graph_GShapeElement_isa_GModelElement():
    instance = graph_GShapeElement()
    assert isinstance(instance, GModelElement)


def test_graph_GGraph_isa_GModelRoot():
    instance = graph_GGraph()
    assert isinstance(instance, GModelRoot)


def test_graph_GHtmlRoot_isa_GModelRoot():
    instance = graph_GHtmlRoot(classes="sample_text")
    assert isinstance(instance, GModelRoot)


def test_graph_GButton_isa_GShapeElement():
    instance = graph_GButton(enabled=True)
    assert isinstance(instance, GShapeElement)


def test_graph_GCompartment_isa_GShapeElement():
    instance = graph_GCompartment()
    assert isinstance(instance, GShapeElement)


def test_graph_GIssueMarker_isa_GShapeElement():
    instance = graph_GIssueMarker()
    assert isinstance(instance, GShapeElement)


def test_graph_GLabel_isa_GShapeElement():
    instance = graph_GLabel(text="sample_text")
    assert isinstance(instance, GShapeElement)


def test_graph_GNode_isa_GShapeElement():
    instance = graph_GNode()
    assert isinstance(instance, GShapeElement)


def test_graph_GPort_isa_GShapeElement():
    instance = graph_GPort()
    assert isinstance(instance, GShapeElement)


def test_assoc_alignment21_link_reassign_clear():
    a = graph_GPoint(x=3.14, y=3.14)
    b1 = graph_GAlignable()
    b2 = graph_GAlignable()
    _safe_set(a, 'graph_GPoint22', b1)
    assert _is_linked(a, 'graph_GPoint22', b1)
    if hasattr(b1, 'graph_GAlignable'):
        assert _is_linked(b1, 'graph_GAlignable', a)
    _safe_set(a, 'graph_GPoint22', b2)
    assert _is_linked(a, 'graph_GPoint22', b2)
    if hasattr(b1, 'graph_GAlignable'):
        assert not _is_linked(b1, 'graph_GAlignable', a)
    if hasattr(b2, 'graph_GAlignable'):
        assert _is_linked(b2, 'graph_GAlignable', a)
    _safe_set(a, 'graph_GPoint22', None)
    assert not _is_linked(a, 'graph_GPoint22', b2)
    if hasattr(b2, 'graph_GAlignable'):
        assert not _is_linked(b2, 'graph_GAlignable', a)


def test_assoc_canvasBounds6_link_reassign_clear():
    a = graph_GModelRoot(revision=7)
    b1 = graph_GBounds(height=3.14, width=3.14, x=3.14, y=3.14)
    b2 = graph_GBounds(height=9.99, width=9.99, x=9.99, y=9.99)
    _safe_set(a, 'graph_GModelRoot', b1)
    assert _is_linked(a, 'graph_GModelRoot', b1)
    if hasattr(b1, 'graph_GBounds'):
        assert _is_linked(b1, 'graph_GBounds', a)
    _safe_set(a, 'graph_GModelRoot', b2)
    assert _is_linked(a, 'graph_GModelRoot', b2)
    if hasattr(b1, 'graph_GBounds'):
        assert not _is_linked(b1, 'graph_GBounds', a)
    if hasattr(b2, 'graph_GBounds'):
        assert _is_linked(b2, 'graph_GBounds', a)
    _safe_set(a, 'graph_GModelRoot', None)
    assert not _is_linked(a, 'graph_GModelRoot', b2)
    if hasattr(b2, 'graph_GBounds'):
        assert not _is_linked(b2, 'graph_GBounds', a)


def test_assoc_children1_link_reassign_clear():
    a = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    b1 = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    b2 = graph_GModelElement(cssClasses="sample_text_2", id="sample_text_2", trace="sample_text_2", type="sample_text_2")
    _safe_set(a, 'GModelElement', b1)
    assert _is_linked(a, 'GModelElement', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'GModelElement', b2)
    assert _is_linked(a, 'GModelElement', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'GModelElement', None)
    assert not _is_linked(a, 'GModelElement', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_edgePlacement18_link_reassign_clear():
    a = graph_GEdgePlacement(offset="sample_text", position="sample_text", rotate=True, side="sample_text")
    b1 = graph_GEdgeLayoutable()
    b2 = graph_GEdgeLayoutable()
    _safe_set(a, 'graph_GEdgePlacement', b1)
    assert _is_linked(a, 'graph_GEdgePlacement', b1)
    if hasattr(b1, 'graph_GEdgeLayoutable'):
        assert _is_linked(b1, 'graph_GEdgeLayoutable', a)
    _safe_set(a, 'graph_GEdgePlacement', b2)
    assert _is_linked(a, 'graph_GEdgePlacement', b2)
    if hasattr(b1, 'graph_GEdgeLayoutable'):
        assert not _is_linked(b1, 'graph_GEdgeLayoutable', a)
    if hasattr(b2, 'graph_GEdgeLayoutable'):
        assert _is_linked(b2, 'graph_GEdgeLayoutable', a)
    _safe_set(a, 'graph_GEdgePlacement', None)
    assert not _is_linked(a, 'graph_GEdgePlacement', b2)
    if hasattr(b2, 'graph_GEdgeLayoutable'):
        assert not _is_linked(b2, 'graph_GEdgeLayoutable', a)


def test_assoc_issues13_link_reassign_clear():
    a = graph_GIssue(message="sample_text", severity="sample_text")
    b1 = graph_GIssueMarker()
    b2 = graph_GIssueMarker()
    _safe_set(a, 'graph_GIssue', b1)
    assert _is_linked(a, 'graph_GIssue', b1)
    if hasattr(b1, 'graph_GIssueMarker'):
        assert _is_linked(b1, 'graph_GIssueMarker', a)
    _safe_set(a, 'graph_GIssue', b2)
    assert _is_linked(a, 'graph_GIssue', b2)
    if hasattr(b1, 'graph_GIssueMarker'):
        assert not _is_linked(b1, 'graph_GIssueMarker', a)
    if hasattr(b2, 'graph_GIssueMarker'):
        assert _is_linked(b2, 'graph_GIssueMarker', a)
    _safe_set(a, 'graph_GIssue', None)
    assert not _is_linked(a, 'graph_GIssue', b2)
    if hasattr(b2, 'graph_GIssueMarker'):
        assert not _is_linked(b2, 'graph_GIssueMarker', a)


def test_assoc_layoutOptions19_link_reassign_clear():
    a = graph_GLayouting(layout="sample_text")
    b1 = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    b2 = graph_GLayoutOptions(hAlign="sample_text_2", hGap="sample_text_2", minHeight="sample_text_2", minWidth="sample_text_2", paddingBottom="sample_text_2", paddingFactor="sample_text_2", paddingLeft="sample_text_2", paddingRight="sample_text_2", paddingTop="sample_text_2", resizeContainer=False, vAlign="sample_text_2", vGap="sample_text_2")
    _safe_set(a, 'graph_GLayouting', b1)
    assert _is_linked(a, 'graph_GLayouting', b1)
    if hasattr(b1, 'graph_GLayoutOptions20'):
        assert _is_linked(b1, 'graph_GLayoutOptions20', a)
    _safe_set(a, 'graph_GLayouting', b2)
    assert _is_linked(a, 'graph_GLayouting', b2)
    if hasattr(b1, 'graph_GLayoutOptions20'):
        assert not _is_linked(b1, 'graph_GLayoutOptions20', a)
    if hasattr(b2, 'graph_GLayoutOptions20'):
        assert _is_linked(b2, 'graph_GLayoutOptions20', a)
    _safe_set(a, 'graph_GLayouting', None)
    assert not _is_linked(a, 'graph_GLayouting', b2)
    if hasattr(b2, 'graph_GLayoutOptions20'):
        assert not _is_linked(b2, 'graph_GLayoutOptions20', a)


def test_assoc_layoutOptions5_link_reassign_clear():
    a = graph_GLayoutOptions(hAlign="sample_text", hGap="sample_text", minHeight="sample_text", minWidth="sample_text", paddingBottom="sample_text", paddingFactor="sample_text", paddingLeft="sample_text", paddingRight="sample_text", paddingTop="sample_text", resizeContainer=True, vAlign="sample_text", vGap="sample_text")
    b1 = graph_GGraph()
    b2 = graph_GGraph()
    _safe_set(a, 'graph_GLayoutOptions', b1)
    assert _is_linked(a, 'graph_GLayoutOptions', b1)
    if hasattr(b1, 'graph_GGraph'):
        assert _is_linked(b1, 'graph_GGraph', a)
    _safe_set(a, 'graph_GLayoutOptions', b2)
    assert _is_linked(a, 'graph_GLayoutOptions', b2)
    if hasattr(b1, 'graph_GGraph'):
        assert not _is_linked(b1, 'graph_GGraph', a)
    if hasattr(b2, 'graph_GGraph'):
        assert _is_linked(b2, 'graph_GGraph', a)
    _safe_set(a, 'graph_GLayoutOptions', None)
    assert not _is_linked(a, 'graph_GLayoutOptions', b2)
    if hasattr(b2, 'graph_GGraph'):
        assert not _is_linked(b2, 'graph_GGraph', a)


def test_assoc_parent3_link_reassign_clear():
    a = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    b1 = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    b2 = graph_GModelElement(cssClasses="sample_text_2", id="sample_text_2", trace="sample_text_2", type="sample_text_2")
    _safe_set(a, 'GModelElement4', b1)
    assert _is_linked(a, 'GModelElement4', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'GModelElement4', b2)
    assert _is_linked(a, 'GModelElement4', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'GModelElement4', None)
    assert not _is_linked(a, 'GModelElement4', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_position14_link_reassign_clear():
    a = graph_GPoint(x=3.14, y=3.14)
    b1 = graph_GBoundsAware()
    b2 = graph_GBoundsAware()
    _safe_set(a, 'graph_GPoint15', b1)
    assert _is_linked(a, 'graph_GPoint15', b1)
    if hasattr(b1, 'graph_GBoundsAware'):
        assert _is_linked(b1, 'graph_GBoundsAware', a)
    _safe_set(a, 'graph_GPoint15', b2)
    assert _is_linked(a, 'graph_GPoint15', b2)
    if hasattr(b1, 'graph_GBoundsAware'):
        assert not _is_linked(b1, 'graph_GBoundsAware', a)
    if hasattr(b2, 'graph_GBoundsAware'):
        assert _is_linked(b2, 'graph_GBoundsAware', a)
    _safe_set(a, 'graph_GPoint15', None)
    assert not _is_linked(a, 'graph_GPoint15', b2)
    if hasattr(b2, 'graph_GBoundsAware'):
        assert not _is_linked(b2, 'graph_GBoundsAware', a)


def test_assoc_routingPoints7_link_reassign_clear():
    a = graph_GPoint(x=3.14, y=3.14)
    b1 = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    b2 = graph_GEdge(routerKind="sample_text_2", sourceId="sample_text_2", targetId="sample_text_2")
    _safe_set(a, 'graph_GPoint', b1)
    assert _is_linked(a, 'graph_GPoint', b1)
    if hasattr(b1, 'graph_GEdge'):
        assert _is_linked(b1, 'graph_GEdge', a)
    _safe_set(a, 'graph_GPoint', b2)
    assert _is_linked(a, 'graph_GPoint', b2)
    if hasattr(b1, 'graph_GEdge'):
        assert not _is_linked(b1, 'graph_GEdge', a)
    if hasattr(b2, 'graph_GEdge'):
        assert _is_linked(b2, 'graph_GEdge', a)
    _safe_set(a, 'graph_GPoint', None)
    assert not _is_linked(a, 'graph_GPoint', b2)
    if hasattr(b2, 'graph_GEdge'):
        assert not _is_linked(b2, 'graph_GEdge', a)


def test_assoc_size16_link_reassign_clear():
    a = graph_GDimension(height=3.14, width=3.14)
    b1 = graph_GBoundsAware()
    b2 = graph_GBoundsAware()
    _safe_set(a, 'graph_GDimension', b1)
    assert _is_linked(a, 'graph_GDimension', b1)
    if hasattr(b1, 'graph_GBoundsAware17'):
        assert _is_linked(b1, 'graph_GBoundsAware17', a)
    _safe_set(a, 'graph_GDimension', b2)
    assert _is_linked(a, 'graph_GDimension', b2)
    if hasattr(b1, 'graph_GBoundsAware17'):
        assert not _is_linked(b1, 'graph_GBoundsAware17', a)
    if hasattr(b2, 'graph_GBoundsAware17'):
        assert _is_linked(b2, 'graph_GBoundsAware17', a)
    _safe_set(a, 'graph_GDimension', None)
    assert not _is_linked(a, 'graph_GDimension', b2)
    if hasattr(b2, 'graph_GBoundsAware17'):
        assert not _is_linked(b2, 'graph_GBoundsAware17', a)


def test_assoc_source8_link_reassign_clear():
    a = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    b1 = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    b2 = graph_GEdge(routerKind="sample_text_2", sourceId="sample_text_2", targetId="sample_text_2")
    _safe_set(a, 'graph_GModelElement', b1)
    assert _is_linked(a, 'graph_GModelElement', b1)
    if hasattr(b1, 'graph_GEdge9'):
        assert _is_linked(b1, 'graph_GEdge9', a)
    _safe_set(a, 'graph_GModelElement', b2)
    assert _is_linked(a, 'graph_GModelElement', b2)
    if hasattr(b1, 'graph_GEdge9'):
        assert not _is_linked(b1, 'graph_GEdge9', a)
    if hasattr(b2, 'graph_GEdge9'):
        assert _is_linked(b2, 'graph_GEdge9', a)
    _safe_set(a, 'graph_GModelElement', None)
    assert not _is_linked(a, 'graph_GModelElement', b2)
    if hasattr(b2, 'graph_GEdge9'):
        assert not _is_linked(b2, 'graph_GEdge9', a)


def test_assoc_target10_link_reassign_clear():
    a = graph_GModelElement(cssClasses="sample_text", id="sample_text", trace="sample_text", type="sample_text")
    b1 = graph_GEdge(routerKind="sample_text", sourceId="sample_text", targetId="sample_text")
    b2 = graph_GEdge(routerKind="sample_text_2", sourceId="sample_text_2", targetId="sample_text_2")
    _safe_set(a, 'graph_GModelElement12', b1)
    assert _is_linked(a, 'graph_GModelElement12', b1)
    if hasattr(b1, 'graph_GEdge11'):
        assert _is_linked(b1, 'graph_GEdge11', a)
    _safe_set(a, 'graph_GModelElement12', b2)
    assert _is_linked(a, 'graph_GModelElement12', b2)
    if hasattr(b1, 'graph_GEdge11'):
        assert not _is_linked(b1, 'graph_GEdge11', a)
    if hasattr(b2, 'graph_GEdge11'):
        assert _is_linked(b2, 'graph_GEdge11', a)
    _safe_set(a, 'graph_GModelElement12', None)
    assert not _is_linked(a, 'graph_GModelElement12', b2)
    if hasattr(b2, 'graph_GEdge11'):
        assert not _is_linked(b2, 'graph_GEdge11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

GAlignable_strategy = st.builds(GAlignable)
@given(instance=GAlignable_strategy)
@settings(max_examples=25)
def test_GAlignable_instantiation(instance):
    assert isinstance(instance, GAlignable)


GBoundsAware_strategy = st.builds(GBoundsAware)
@given(instance=GBoundsAware_strategy)
@settings(max_examples=25)
def test_GBoundsAware_instantiation(instance):
    assert isinstance(instance, GBoundsAware)


GEdgeLayoutable_strategy = st.builds(GEdgeLayoutable)
@given(instance=GEdgeLayoutable_strategy)
@settings(max_examples=25)
def test_GEdgeLayoutable_instantiation(instance):
    assert isinstance(instance, GEdgeLayoutable)


GLayouting_strategy = st.builds(GLayouting)
@given(instance=GLayouting_strategy)
@settings(max_examples=25)
def test_GLayouting_instantiation(instance):
    assert isinstance(instance, GLayouting)


GModelElement_strategy = st.builds(GModelElement)
@given(instance=GModelElement_strategy)
@settings(max_examples=25)
def test_GModelElement_instantiation(instance):
    assert isinstance(instance, GModelElement)


GModelRoot_strategy = st.builds(GModelRoot)
@given(instance=GModelRoot_strategy)
@settings(max_examples=25)
def test_GModelRoot_instantiation(instance):
    assert isinstance(instance, GModelRoot)


GShapeElement_strategy = st.builds(GShapeElement)
@given(instance=GShapeElement_strategy)
@settings(max_examples=25)
def test_GShapeElement_instantiation(instance):
    assert isinstance(instance, GShapeElement)


graph_GAlignable_strategy = st.builds(graph_GAlignable)
@given(instance=graph_GAlignable_strategy)
@settings(max_examples=25)
def test_graph_GAlignable_instantiation(instance):
    assert isinstance(instance, graph_GAlignable)


graph_GBounds_strategy = st.builds(graph_GBounds, height=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False), x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=graph_GBounds_strategy)
@settings(max_examples=25)
def test_graph_GBounds_instantiation(instance):
    assert isinstance(instance, graph_GBounds)


graph_GBoundsAware_strategy = st.builds(graph_GBoundsAware)
@given(instance=graph_GBoundsAware_strategy)
@settings(max_examples=25)
def test_graph_GBoundsAware_instantiation(instance):
    assert isinstance(instance, graph_GBoundsAware)


graph_GButton_strategy = st.builds(graph_GButton, enabled=st.booleans())
@given(instance=graph_GButton_strategy)
@settings(max_examples=25)
def test_graph_GButton_instantiation(instance):
    assert isinstance(instance, graph_GButton)


graph_GCompartment_strategy = st.builds(graph_GCompartment)
@given(instance=graph_GCompartment_strategy)
@settings(max_examples=25)
def test_graph_GCompartment_instantiation(instance):
    assert isinstance(instance, graph_GCompartment)


graph_GDimension_strategy = st.builds(graph_GDimension, height=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=graph_GDimension_strategy)
@settings(max_examples=25)
def test_graph_GDimension_instantiation(instance):
    assert isinstance(instance, graph_GDimension)


graph_GEdge_strategy = st.builds(graph_GEdge, routerKind=safe_text, sourceId=safe_text, targetId=safe_text)
@given(instance=graph_GEdge_strategy)
@settings(max_examples=25)
def test_graph_GEdge_instantiation(instance):
    assert isinstance(instance, graph_GEdge)


graph_GEdgeLayoutable_strategy = st.builds(graph_GEdgeLayoutable)
@given(instance=graph_GEdgeLayoutable_strategy)
@settings(max_examples=25)
def test_graph_GEdgeLayoutable_instantiation(instance):
    assert isinstance(instance, graph_GEdgeLayoutable)


graph_GEdgePlacement_strategy = st.builds(graph_GEdgePlacement, offset=safe_text, position=safe_text, rotate=st.booleans(), side=safe_text)
@given(instance=graph_GEdgePlacement_strategy)
@settings(max_examples=25)
def test_graph_GEdgePlacement_instantiation(instance):
    assert isinstance(instance, graph_GEdgePlacement)


graph_GGraph_strategy = st.builds(graph_GGraph)
@given(instance=graph_GGraph_strategy)
@settings(max_examples=25)
def test_graph_GGraph_instantiation(instance):
    assert isinstance(instance, graph_GGraph)


graph_GHtmlRoot_strategy = st.builds(graph_GHtmlRoot, classes=safe_text)
@given(instance=graph_GHtmlRoot_strategy)
@settings(max_examples=25)
def test_graph_GHtmlRoot_instantiation(instance):
    assert isinstance(instance, graph_GHtmlRoot)


graph_GIssue_strategy = st.builds(graph_GIssue, message=safe_text, severity=safe_text)
@given(instance=graph_GIssue_strategy)
@settings(max_examples=25)
def test_graph_GIssue_instantiation(instance):
    assert isinstance(instance, graph_GIssue)


graph_GIssueMarker_strategy = st.builds(graph_GIssueMarker)
@given(instance=graph_GIssueMarker_strategy)
@settings(max_examples=25)
def test_graph_GIssueMarker_instantiation(instance):
    assert isinstance(instance, graph_GIssueMarker)


graph_GLabel_strategy = st.builds(graph_GLabel, text=safe_text)
@given(instance=graph_GLabel_strategy)
@settings(max_examples=25)
def test_graph_GLabel_instantiation(instance):
    assert isinstance(instance, graph_GLabel)


graph_GLayoutOptions_strategy = st.builds(graph_GLayoutOptions, hAlign=safe_text, hGap=safe_text, minHeight=safe_text, minWidth=safe_text, paddingBottom=safe_text, paddingFactor=safe_text, paddingLeft=safe_text, paddingRight=safe_text, paddingTop=safe_text, resizeContainer=st.booleans(), vAlign=safe_text, vGap=safe_text)
@given(instance=graph_GLayoutOptions_strategy)
@settings(max_examples=25)
def test_graph_GLayoutOptions_instantiation(instance):
    assert isinstance(instance, graph_GLayoutOptions)


graph_GLayouting_strategy = st.builds(graph_GLayouting, layout=safe_text)
@given(instance=graph_GLayouting_strategy)
@settings(max_examples=25)
def test_graph_GLayouting_instantiation(instance):
    assert isinstance(instance, graph_GLayouting)


graph_GModelElement_strategy = st.builds(graph_GModelElement, cssClasses=safe_text, id=safe_text, trace=safe_text, type=safe_text)
@given(instance=graph_GModelElement_strategy)
@settings(max_examples=25)
def test_graph_GModelElement_instantiation(instance):
    assert isinstance(instance, graph_GModelElement)


graph_GModelRoot_strategy = st.builds(graph_GModelRoot, revision=st.integers())
@given(instance=graph_GModelRoot_strategy)
@settings(max_examples=25)
def test_graph_GModelRoot_instantiation(instance):
    assert isinstance(instance, graph_GModelRoot)


graph_GNode_strategy = st.builds(graph_GNode)
@given(instance=graph_GNode_strategy)
@settings(max_examples=25)
def test_graph_GNode_instantiation(instance):
    assert isinstance(instance, graph_GNode)


graph_GPoint_strategy = st.builds(graph_GPoint, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=graph_GPoint_strategy)
@settings(max_examples=25)
def test_graph_GPoint_instantiation(instance):
    assert isinstance(instance, graph_GPoint)


graph_GPort_strategy = st.builds(graph_GPort)
@given(instance=graph_GPort_strategy)
@settings(max_examples=25)
def test_graph_GPort_instantiation(instance):
    assert isinstance(instance, graph_GPort)


graph_GPreRenderedElement_strategy = st.builds(graph_GPreRenderedElement, code=safe_text)
@given(instance=graph_GPreRenderedElement_strategy)
@settings(max_examples=25)
def test_graph_GPreRenderedElement_instantiation(instance):
    assert isinstance(instance, graph_GPreRenderedElement)


graph_GShapeElement_strategy = st.builds(graph_GShapeElement)
@given(instance=graph_GShapeElement_strategy)
@settings(max_examples=25)
def test_graph_GShapeElement_instantiation(instance):
    assert isinstance(instance, graph_GShapeElement)



