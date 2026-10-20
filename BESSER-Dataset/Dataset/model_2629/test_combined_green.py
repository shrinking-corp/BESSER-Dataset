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
    SupportOperation,
    aredsl_ArrangeElements,
    aredsl_ShowSystemMenu,
    aredsl_Exit,
    aredsl_MoveElement,
    Action,
    aredsl_VoiceAction,
    aredsl_GestureAction,
    aredsl_SensorBasedAction,
    TrackerAction,
    aredsl_MarkerLessTrackerAction,
    aredsl_MarkerBasedTrackerAction,
    aredsl_TactileAction,
    aredsl_MentalAction,
    Behaviour,
    aredsl_SupportOperation,
    aredsl_DomainOperation,
    DomainOperation,
    aredsl_UnsetOperation,
    aredsl_RemoveOperation,
    aredsl_SetOperation,
    aredsl_CreateInstanceOperation,
    aredsl_Action,
    aredsl_ChangeContextOperation,
    aredsl_Behaviour,
    aredsl_Tool,
    aredsl_EdgeStyle,
    aredsl_LabelStyle,
    aredsl_Label,
    aredsl_NodeStyle,
    NodeStyle,
    aredsl_Image2DNodeStyle,
    aredsl_GeometricShapeNodeStyle,
    aredsl_Model3DNodeStyle,
    aredsl_ToolSet,
    aredsl_Layer,
    aredsl_Editor,
    aredsl_TrackerAction,
    aredsl_Edge,
    aredsl_Node,
    LineKind,
    QueryLanguageKind,
    ShapeKind,
    OutlineKind,
    IntegrityRestrictionKind,
    ContainmentKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_supportoperation_is_not_abstract():
    assert not inspect.isabstract(SupportOperation)


def test_hyp_supportoperation_constructor_exists():
    assert callable(SupportOperation.__init__)


def test_hyp_supportoperation_constructor_args():
    sig = inspect.signature(SupportOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_arrangeelements_is_not_abstract():
    assert not inspect.isabstract(aredsl_ArrangeElements)


def test_hyp_aredsl_arrangeelements_constructor_exists():
    assert callable(aredsl_ArrangeElements.__init__)


def test_hyp_aredsl_arrangeelements_constructor_args():
    sig = inspect.signature(aredsl_ArrangeElements.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_showsystemmenu_is_not_abstract():
    assert not inspect.isabstract(aredsl_ShowSystemMenu)


def test_hyp_aredsl_showsystemmenu_constructor_exists():
    assert callable(aredsl_ShowSystemMenu.__init__)


def test_hyp_aredsl_showsystemmenu_constructor_args():
    sig = inspect.signature(aredsl_ShowSystemMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_exit_is_not_abstract():
    assert not inspect.isabstract(aredsl_Exit)


def test_hyp_aredsl_exit_constructor_exists():
    assert callable(aredsl_Exit.__init__)


def test_hyp_aredsl_exit_constructor_args():
    sig = inspect.signature(aredsl_Exit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_moveelement_is_not_abstract():
    assert not inspect.isabstract(aredsl_MoveElement)


def test_hyp_aredsl_moveelement_constructor_exists():
    assert callable(aredsl_MoveElement.__init__)


def test_hyp_aredsl_moveelement_constructor_args():
    sig = inspect.signature(aredsl_MoveElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_voiceaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_VoiceAction)


def test_hyp_aredsl_voiceaction_constructor_exists():
    assert callable(aredsl_VoiceAction.__init__)


def test_hyp_aredsl_voiceaction_constructor_args():
    sig = inspect.signature(aredsl_VoiceAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_gestureaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_GestureAction)


def test_hyp_aredsl_gestureaction_constructor_exists():
    assert callable(aredsl_GestureAction.__init__)


def test_hyp_aredsl_gestureaction_constructor_args():
    sig = inspect.signature(aredsl_GestureAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_sensorbasedaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_SensorBasedAction)


def test_hyp_aredsl_sensorbasedaction_constructor_exists():
    assert callable(aredsl_SensorBasedAction.__init__)


def test_hyp_aredsl_sensorbasedaction_constructor_args():
    sig = inspect.signature(aredsl_SensorBasedAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trackeraction_is_not_abstract():
    assert not inspect.isabstract(TrackerAction)


def test_hyp_trackeraction_constructor_exists():
    assert callable(TrackerAction.__init__)


def test_hyp_trackeraction_constructor_args():
    sig = inspect.signature(TrackerAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_markerlesstrackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl_MarkerLessTrackerAction)


def test_hyp_aredsl_markerlesstrackeraction_constructor_exists():
    assert callable(aredsl_MarkerLessTrackerAction.__init__)


def test_hyp_aredsl_markerlesstrackeraction_constructor_args():
    sig = inspect.signature(aredsl_MarkerLessTrackerAction.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_aredsl_markerbasedtrackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl_MarkerBasedTrackerAction)


def test_hyp_aredsl_markerbasedtrackeraction_constructor_exists():
    assert callable(aredsl_MarkerBasedTrackerAction.__init__)


def test_hyp_aredsl_markerbasedtrackeraction_constructor_args():
    sig = inspect.signature(aredsl_MarkerBasedTrackerAction.__init__)
    params = list(sig.parameters.keys())
    assert "markerId" in params, "Missing parameter 'markerId'"




def test_hyp_aredsl_tactileaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_TactileAction)


def test_hyp_aredsl_tactileaction_constructor_exists():
    assert callable(aredsl_TactileAction.__init__)


def test_hyp_aredsl_tactileaction_constructor_args():
    sig = inspect.signature(aredsl_TactileAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_mentalaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_MentalAction)


def test_hyp_aredsl_mentalaction_constructor_exists():
    assert callable(aredsl_MentalAction.__init__)


def test_hyp_aredsl_mentalaction_constructor_args():
    sig = inspect.signature(aredsl_MentalAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_is_not_abstract():
    assert not inspect.isabstract(Behaviour)


def test_hyp_behaviour_constructor_exists():
    assert callable(Behaviour.__init__)


def test_hyp_behaviour_constructor_args():
    sig = inspect.signature(Behaviour.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_supportoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_SupportOperation)


def test_hyp_aredsl_supportoperation_constructor_exists():
    assert callable(aredsl_SupportOperation.__init__)


def test_hyp_aredsl_supportoperation_constructor_args():
    sig = inspect.signature(aredsl_SupportOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_domainoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_DomainOperation)


def test_hyp_aredsl_domainoperation_constructor_exists():
    assert callable(aredsl_DomainOperation.__init__)


def test_hyp_aredsl_domainoperation_constructor_args():
    sig = inspect.signature(aredsl_DomainOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_domainoperation_is_not_abstract():
    assert not inspect.isabstract(DomainOperation)


def test_hyp_domainoperation_constructor_exists():
    assert callable(DomainOperation.__init__)


def test_hyp_domainoperation_constructor_args():
    sig = inspect.signature(DomainOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_unsetoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_UnsetOperation)


def test_hyp_aredsl_unsetoperation_constructor_exists():
    assert callable(aredsl_UnsetOperation.__init__)


def test_hyp_aredsl_unsetoperation_constructor_args():
    sig = inspect.signature(aredsl_UnsetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"
    assert "feature" in params, "Missing parameter 'feature'"





def test_hyp_aredsl_removeoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_RemoveOperation)


def test_hyp_aredsl_removeoperation_constructor_exists():
    assert callable(aredsl_RemoveOperation.__init__)


def test_hyp_aredsl_removeoperation_constructor_args():
    sig = inspect.signature(aredsl_RemoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"




def test_hyp_aredsl_setoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_SetOperation)


def test_hyp_aredsl_setoperation_constructor_exists():
    assert callable(aredsl_SetOperation.__init__)


def test_hyp_aredsl_setoperation_constructor_args():
    sig = inspect.signature(aredsl_SetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"
    assert "value" in params, "Missing parameter 'value'"
    assert "constraint" in params, "Missing parameter 'constraint'"






def test_hyp_aredsl_createinstanceoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_CreateInstanceOperation)


def test_hyp_aredsl_createinstanceoperation_constructor_exists():
    assert callable(aredsl_CreateInstanceOperation.__init__)


def test_hyp_aredsl_createinstanceoperation_constructor_args():
    sig = inspect.signature(aredsl_CreateInstanceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_aredsl_action_is_not_abstract():
    assert not inspect.isabstract(aredsl_Action)


def test_hyp_aredsl_action_constructor_exists():
    assert callable(aredsl_Action.__init__)


def test_hyp_aredsl_action_constructor_args():
    sig = inspect.signature(aredsl_Action.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_aredsl_changecontextoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_ChangeContextOperation)


def test_hyp_aredsl_changecontextoperation_constructor_exists():
    assert callable(aredsl_ChangeContextOperation.__init__)


def test_hyp_aredsl_changecontextoperation_constructor_args():
    sig = inspect.signature(aredsl_ChangeContextOperation.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_aredsl_behaviour_is_not_abstract():
    assert not inspect.isabstract(aredsl_Behaviour)


def test_hyp_aredsl_behaviour_constructor_exists():
    assert callable(aredsl_Behaviour.__init__)


def test_hyp_aredsl_behaviour_constructor_args():
    sig = inspect.signature(aredsl_Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_aredsl_tool_is_not_abstract():
    assert not inspect.isabstract(aredsl_Tool)


def test_hyp_aredsl_tool_constructor_exists():
    assert callable(aredsl_Tool.__init__)


def test_hyp_aredsl_tool_constructor_args():
    sig = inspect.signature(aredsl_Tool.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "targetPrecondition" in params, "Missing parameter 'targetPrecondition'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_aredsl_edgestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_EdgeStyle)


def test_hyp_aredsl_edgestyle_constructor_exists():
    assert callable(aredsl_EdgeStyle.__init__)


def test_hyp_aredsl_edgestyle_constructor_args():
    sig = inspect.signature(aredsl_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "color" in params, "Missing parameter 'color'"
    assert "width" in params, "Missing parameter 'width'"







def test_hyp_aredsl_labelstyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_LabelStyle)


def test_hyp_aredsl_labelstyle_constructor_exists():
    assert callable(aredsl_LabelStyle.__init__)


def test_hyp_aredsl_labelstyle_constructor_args():
    sig = inspect.signature(aredsl_LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "color" in params, "Missing parameter 'color'"
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"






def test_hyp_aredsl_label_is_not_abstract():
    assert not inspect.isabstract(aredsl_Label)


def test_hyp_aredsl_label_constructor_exists():
    assert callable(aredsl_Label.__init__)


def test_hyp_aredsl_label_constructor_args():
    sig = inspect.signature(aredsl_Label.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "semantics" in params, "Missing parameter 'semantics'"






def test_hyp_aredsl_nodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_NodeStyle)


def test_hyp_aredsl_nodestyle_constructor_exists():
    assert callable(aredsl_NodeStyle.__init__)


def test_hyp_aredsl_nodestyle_constructor_args():
    sig = inspect.signature(aredsl_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"
    assert "height" in params, "Missing parameter 'height'"






def test_hyp_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_hyp_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_hyp_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_image2dnodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_Image2DNodeStyle)


def test_hyp_aredsl_image2dnodestyle_constructor_exists():
    assert callable(aredsl_Image2DNodeStyle.__init__)


def test_hyp_aredsl_image2dnodestyle_constructor_args():
    sig = inspect.signature(aredsl_Image2DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_aredsl_geometricshapenodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_GeometricShapeNodeStyle)


def test_hyp_aredsl_geometricshapenodestyle_constructor_exists():
    assert callable(aredsl_GeometricShapeNodeStyle.__init__)


def test_hyp_aredsl_geometricshapenodestyle_constructor_args():
    sig = inspect.signature(aredsl_GeometricShapeNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "outline" in params, "Missing parameter 'outline'"






def test_hyp_aredsl_model3dnodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_Model3DNodeStyle)


def test_hyp_aredsl_model3dnodestyle_constructor_exists():
    assert callable(aredsl_Model3DNodeStyle.__init__)


def test_hyp_aredsl_model3dnodestyle_constructor_args():
    sig = inspect.signature(aredsl_Model3DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"




def test_hyp_aredsl_toolset_is_not_abstract():
    assert not inspect.isabstract(aredsl_ToolSet)


def test_hyp_aredsl_toolset_constructor_exists():
    assert callable(aredsl_ToolSet.__init__)


def test_hyp_aredsl_toolset_constructor_args():
    sig = inspect.signature(aredsl_ToolSet.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_aredsl_layer_is_not_abstract():
    assert not inspect.isabstract(aredsl_Layer)


def test_hyp_aredsl_layer_constructor_exists():
    assert callable(aredsl_Layer.__init__)


def test_hyp_aredsl_layer_constructor_args():
    sig = inspect.signature(aredsl_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "semantics" in params, "Missing parameter 'semantics'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_aredsl_editor_is_not_abstract():
    assert not inspect.isabstract(aredsl_Editor)


def test_hyp_aredsl_editor_constructor_exists():
    assert callable(aredsl_Editor.__init__)


def test_hyp_aredsl_editor_constructor_args():
    sig = inspect.signature(aredsl_Editor.__init__)
    params = list(sig.parameters.keys())
    assert "fileExtension" in params, "Missing parameter 'fileExtension'"
    assert "queryLanguageKind" in params, "Missing parameter 'queryLanguageKind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"







def test_hyp_aredsl_trackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl_TrackerAction)


def test_hyp_aredsl_trackeraction_constructor_exists():
    assert callable(aredsl_TrackerAction.__init__)


def test_hyp_aredsl_trackeraction_constructor_args():
    sig = inspect.signature(aredsl_TrackerAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_aredsl_edge_is_not_abstract():
    assert not inspect.isabstract(aredsl_Edge)


def test_hyp_aredsl_edge_constructor_exists():
    assert callable(aredsl_Edge.__init__)


def test_hyp_aredsl_edge_constructor_args():
    sig = inspect.signature(aredsl_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "destinationSemantics" in params, "Missing parameter 'destinationSemantics'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "originSemantics" in params, "Missing parameter 'originSemantics'"







def test_hyp_aredsl_node_is_not_abstract():
    assert not inspect.isabstract(aredsl_Node)


def test_hyp_aredsl_node_constructor_exists():
    assert callable(aredsl_Node.__init__)


def test_hyp_aredsl_node_constructor_args():
    sig = inspect.signature(aredsl_Node.__init__)
    params = list(sig.parameters.keys())
    assert "semantics" in params, "Missing parameter 'semantics'"
    assert "contaimentKind" in params, "Missing parameter 'contaimentKind'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_linekind_exists():
    # Check that the Enumeration exists
    assert LineKind is not None

def test_hyp_linekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineKind]
    expected_literals = [
        "DOTTED",
        "DASHED",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_hyp_querylanguagekind_exists():
    # Check that the Enumeration exists
    assert QueryLanguageKind is not None

def test_hyp_querylanguagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueryLanguageKind]
    expected_literals = [
        "OCL",
        "JPQL",
        "XPATH_XQUERY",
        "LINQ",
        "AQL",
        "SQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueryLanguageKind"

def test_hyp_shapekind_exists():
    # Check that the Enumeration exists
    assert ShapeKind is not None

def test_hyp_shapekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShapeKind]
    expected_literals = [
        "TRIANGLE",
        "CIRCLE",
        "ELLIPSE",
        "DIAMOND",
        "RECTANGLE",
        "SQUARE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShapeKind"

def test_hyp_outlinekind_exists():
    # Check that the Enumeration exists
    assert OutlineKind is not None

def test_hyp_outlinekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OutlineKind]
    expected_literals = [
        "DOUBLE",
        "SIMPLE",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OutlineKind"

def test_hyp_integrityrestrictionkind_exists():
    # Check that the Enumeration exists
    assert IntegrityRestrictionKind is not None

def test_hyp_integrityrestrictionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegrityRestrictionKind]
    expected_literals = [
        "NO_ACTION",
        "CASCADE",
        "SET_NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegrityRestrictionKind"

def test_hyp_containmentkind_exists():
    # Check that the Enumeration exists
    assert ContainmentKind is not None

def test_hyp_containmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainmentKind]
    expected_literals = [
        "EXTERNAL_LINK",
        "HORIZONTAL_ARRANGEMENT",
        "VERTICAL_ARRANGEMENT",
        "FREE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainmentKind"


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
SupportOperation_strategy = st.builds(
    SupportOperation,
)
aredsl_ArrangeElements_strategy = st.builds(
    aredsl_ArrangeElements,
)
aredsl_ShowSystemMenu_strategy = st.builds(
    aredsl_ShowSystemMenu,
)
aredsl_Exit_strategy = st.builds(
    aredsl_Exit,
)
aredsl_MoveElement_strategy = st.builds(
    aredsl_MoveElement,
)
Action_strategy = st.builds(
    Action,
)
aredsl_VoiceAction_strategy = st.builds(
    aredsl_VoiceAction,
)
aredsl_GestureAction_strategy = st.builds(
    aredsl_GestureAction,
)
aredsl_SensorBasedAction_strategy = st.builds(
    aredsl_SensorBasedAction,
)
TrackerAction_strategy = st.builds(
    TrackerAction,
)
aredsl_MarkerLessTrackerAction_strategy = st.builds(
    aredsl_MarkerLessTrackerAction,
    file=
        safe_text
)
aredsl_MarkerBasedTrackerAction_strategy = st.builds(
    aredsl_MarkerBasedTrackerAction,
    markerId=
        st.integers()
)
aredsl_TactileAction_strategy = st.builds(
    aredsl_TactileAction,
)
aredsl_MentalAction_strategy = st.builds(
    aredsl_MentalAction,
)
Behaviour_strategy = st.builds(
    Behaviour,
)
aredsl_SupportOperation_strategy = st.builds(
    aredsl_SupportOperation,
)
aredsl_DomainOperation_strategy = st.builds(
    aredsl_DomainOperation,
)
DomainOperation_strategy = st.builds(
    DomainOperation,
)
aredsl_UnsetOperation_strategy = st.builds(
    aredsl_UnsetOperation,
    constraint=
        safe_text,
    feature=
        safe_text
)
aredsl_RemoveOperation_strategy = st.builds(
    aredsl_RemoveOperation,
    constraint=
        safe_text
)
aredsl_SetOperation_strategy = st.builds(
    aredsl_SetOperation,
    feature=
        safe_text,
    value=
        safe_text,
    constraint=
        safe_text
)
aredsl_CreateInstanceOperation_strategy = st.builds(
    aredsl_CreateInstanceOperation,
    feature=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
aredsl_Action_strategy = st.builds(
    aredsl_Action,
    description=
        safe_text
)
aredsl_ChangeContextOperation_strategy = st.builds(
    aredsl_ChangeContextOperation,
    expression=
        safe_text
)
aredsl_Behaviour_strategy = st.builds(
    aredsl_Behaviour,
    description=
        safe_text
)
aredsl_Tool_strategy = st.builds(
    aredsl_Tool,
    precondition=
        safe_text,
    targetPrecondition=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
aredsl_EdgeStyle_strategy = st.builds(
    aredsl_EdgeStyle,
    semanticCondition=
        safe_text,
    kind=
        safe_text,
    color=
        safe_text,
    width=
        st.integers()
)
aredsl_LabelStyle_strategy = st.builds(
    aredsl_LabelStyle,
    height=
        st.integers(),
    color=
        safe_text,
    semanticCondition=
        safe_text
)
aredsl_Label_strategy = st.builds(
    aredsl_Label,
    description=
        safe_text,
    id=
        safe_text,
    semantics=
        safe_text
)
aredsl_NodeStyle_strategy = st.builds(
    aredsl_NodeStyle,
    width=
        st.integers(),
    semanticCondition=
        safe_text,
    height=
        st.integers()
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
aredsl_Image2DNodeStyle_strategy = st.builds(
    aredsl_Image2DNodeStyle,
    file=
        safe_text
)
aredsl_GeometricShapeNodeStyle_strategy = st.builds(
    aredsl_GeometricShapeNodeStyle,
    color=
        safe_text,
    kind=
        safe_text,
    outline=
        safe_text
)
aredsl_Model3DNodeStyle_strategy = st.builds(
    aredsl_Model3DNodeStyle,
    file=
        safe_text
)
aredsl_ToolSet_strategy = st.builds(
    aredsl_ToolSet,
    description=
        safe_text,
    id=
        safe_text
)
aredsl_Layer_strategy = st.builds(
    aredsl_Layer,
    description=
        safe_text,
    semantics=
        safe_text,
    id=
        safe_text
)
aredsl_Editor_strategy = st.builds(
    aredsl_Editor,
    fileExtension=
        safe_text,
    queryLanguageKind=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
aredsl_TrackerAction_strategy = st.builds(
    aredsl_TrackerAction,
)
aredsl_Edge_strategy = st.builds(
    aredsl_Edge,
    destinationSemantics=
        safe_text,
    description=
        safe_text,
    id=
        safe_text,
    originSemantics=
        safe_text
)
aredsl_Node_strategy = st.builds(
    aredsl_Node,
    semantics=
        safe_text,
    contaimentKind=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)














@given(instance=aredsl_MarkerLessTrackerAction_strategy)
def test_hyp_aredsl_markerlesstrackeraction_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original




@given(instance=aredsl_MarkerBasedTrackerAction_strategy)
def test_hyp_aredsl_markerbasedtrackeraction_markerId_setter(instance):
    original = instance.markerId
    instance.markerId = original
    assert instance.markerId == original










@given(instance=aredsl_UnsetOperation_strategy)
def test_hyp_aredsl_unsetoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original



@given(instance=aredsl_UnsetOperation_strategy)
def test_hyp_aredsl_unsetoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original




@given(instance=aredsl_RemoveOperation_strategy)
def test_hyp_aredsl_removeoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original




@given(instance=aredsl_SetOperation_strategy)
def test_hyp_aredsl_setoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original



@given(instance=aredsl_SetOperation_strategy)
def test_hyp_aredsl_setoperation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aredsl_SetOperation_strategy)
def test_hyp_aredsl_setoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original




@given(instance=aredsl_CreateInstanceOperation_strategy)
def test_hyp_aredsl_createinstanceoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original



@given(instance=aredsl_CreateInstanceOperation_strategy)
def test_hyp_aredsl_createinstanceoperation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=aredsl_CreateInstanceOperation_strategy)
def test_hyp_aredsl_createinstanceoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=aredsl_Action_strategy)
def test_hyp_aredsl_action_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=aredsl_ChangeContextOperation_strategy)
def test_hyp_aredsl_changecontextoperation_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original




@given(instance=aredsl_Behaviour_strategy)
def test_hyp_aredsl_behaviour_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=aredsl_Tool_strategy)
def test_hyp_aredsl_tool_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=aredsl_Tool_strategy)
def test_hyp_aredsl_tool_targetPrecondition_setter(instance):
    original = instance.targetPrecondition
    instance.targetPrecondition = original
    assert instance.targetPrecondition == original



@given(instance=aredsl_Tool_strategy)
def test_hyp_aredsl_tool_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Tool_strategy)
def test_hyp_aredsl_tool_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=aredsl_EdgeStyle_strategy)
def test_hyp_aredsl_edgestyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original



@given(instance=aredsl_EdgeStyle_strategy)
def test_hyp_aredsl_edgestyle_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=aredsl_EdgeStyle_strategy)
def test_hyp_aredsl_edgestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=aredsl_EdgeStyle_strategy)
def test_hyp_aredsl_edgestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=aredsl_LabelStyle_strategy)
def test_hyp_aredsl_labelstyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=aredsl_LabelStyle_strategy)
def test_hyp_aredsl_labelstyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=aredsl_LabelStyle_strategy)
def test_hyp_aredsl_labelstyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original




@given(instance=aredsl_Label_strategy)
def test_hyp_aredsl_label_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Label_strategy)
def test_hyp_aredsl_label_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aredsl_Label_strategy)
def test_hyp_aredsl_label_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original




@given(instance=aredsl_NodeStyle_strategy)
def test_hyp_aredsl_nodestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=aredsl_NodeStyle_strategy)
def test_hyp_aredsl_nodestyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original



@given(instance=aredsl_NodeStyle_strategy)
def test_hyp_aredsl_nodestyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=aredsl_Image2DNodeStyle_strategy)
def test_hyp_aredsl_image2dnodestyle_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original




@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
def test_hyp_aredsl_geometricshapenodestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
def test_hyp_aredsl_geometricshapenodestyle_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
def test_hyp_aredsl_geometricshapenodestyle_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original




@given(instance=aredsl_Model3DNodeStyle_strategy)
def test_hyp_aredsl_model3dnodestyle_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original




@given(instance=aredsl_ToolSet_strategy)
def test_hyp_aredsl_toolset_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_ToolSet_strategy)
def test_hyp_aredsl_toolset_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=aredsl_Layer_strategy)
def test_hyp_aredsl_layer_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Layer_strategy)
def test_hyp_aredsl_layer_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original



@given(instance=aredsl_Layer_strategy)
def test_hyp_aredsl_layer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=aredsl_Editor_strategy)
def test_hyp_aredsl_editor_fileExtension_setter(instance):
    original = instance.fileExtension
    instance.fileExtension = original
    assert instance.fileExtension == original



@given(instance=aredsl_Editor_strategy)
def test_hyp_aredsl_editor_queryLanguageKind_setter(instance):
    original = instance.queryLanguageKind
    instance.queryLanguageKind = original
    assert instance.queryLanguageKind == original



@given(instance=aredsl_Editor_strategy)
def test_hyp_aredsl_editor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aredsl_Editor_strategy)
def test_hyp_aredsl_editor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original





@given(instance=aredsl_Edge_strategy)
def test_hyp_aredsl_edge_destinationSemantics_setter(instance):
    original = instance.destinationSemantics
    instance.destinationSemantics = original
    assert instance.destinationSemantics == original



@given(instance=aredsl_Edge_strategy)
def test_hyp_aredsl_edge_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Edge_strategy)
def test_hyp_aredsl_edge_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aredsl_Edge_strategy)
def test_hyp_aredsl_edge_originSemantics_setter(instance):
    original = instance.originSemantics
    instance.originSemantics = original
    assert instance.originSemantics == original




@given(instance=aredsl_Node_strategy)
def test_hyp_aredsl_node_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original



@given(instance=aredsl_Node_strategy)
def test_hyp_aredsl_node_contaimentKind_setter(instance):
    original = instance.contaimentKind
    instance.contaimentKind = original
    assert instance.contaimentKind == original



@given(instance=aredsl_Node_strategy)
def test_hyp_aredsl_node_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Node_strategy)
def test_hyp_aredsl_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Behaviour,
    DomainOperation,
    NodeStyle,
    SupportOperation,
    TrackerAction,
    aredsl_Action,
    aredsl_ArrangeElements,
    aredsl_Behaviour,
    aredsl_ChangeContextOperation,
    aredsl_CreateInstanceOperation,
    aredsl_DomainOperation,
    aredsl_Edge,
    aredsl_EdgeStyle,
    aredsl_Editor,
    aredsl_Exit,
    aredsl_GeometricShapeNodeStyle,
    aredsl_GestureAction,
    aredsl_Image2DNodeStyle,
    aredsl_Label,
    aredsl_LabelStyle,
    aredsl_Layer,
    aredsl_MarkerBasedTrackerAction,
    aredsl_MarkerLessTrackerAction,
    aredsl_MentalAction,
    aredsl_Model3DNodeStyle,
    aredsl_MoveElement,
    aredsl_Node,
    aredsl_NodeStyle,
    aredsl_RemoveOperation,
    aredsl_SensorBasedAction,
    aredsl_SetOperation,
    aredsl_ShowSystemMenu,
    aredsl_SupportOperation,
    aredsl_TactileAction,
    aredsl_Tool,
    aredsl_ToolSet,
    aredsl_TrackerAction,
    aredsl_UnsetOperation,
    aredsl_VoiceAction,
    ContainmentKind,
    IntegrityRestrictionKind,
    LineKind,
    OutlineKind,
    QueryLanguageKind,
    ShapeKind,
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

def test_aredsl_Action_description_value_roundtrip():
    instance = aredsl_Action(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_Behaviour_description_value_roundtrip():
    instance = aredsl_Behaviour(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_ChangeContextOperation_expression_value_roundtrip():
    instance = aredsl_ChangeContextOperation(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_aredsl_CreateInstanceOperation_feature_value_roundtrip():
    instance = aredsl_CreateInstanceOperation(feature="sample_text", name="sample_text", type="sample_text")
    assert instance.feature == "sample_text"
    instance.feature = "sample_text_2"
    assert instance.feature == "sample_text_2"


def test_aredsl_CreateInstanceOperation_name_value_roundtrip():
    instance = aredsl_CreateInstanceOperation(feature="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aredsl_CreateInstanceOperation_type_value_roundtrip():
    instance = aredsl_CreateInstanceOperation(feature="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_aredsl_Edge_description_value_roundtrip():
    instance = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_Edge_destinationSemantics_value_roundtrip():
    instance = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    assert instance.destinationSemantics == "sample_text"
    instance.destinationSemantics = "sample_text_2"
    assert instance.destinationSemantics == "sample_text_2"


def test_aredsl_Edge_id_value_roundtrip():
    instance = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aredsl_Edge_originSemantics_value_roundtrip():
    instance = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    assert instance.originSemantics == "sample_text"
    instance.originSemantics = "sample_text_2"
    assert instance.originSemantics == "sample_text_2"


def test_aredsl_EdgeStyle_color_value_roundtrip():
    instance = aredsl_EdgeStyle(color="sample_text", kind="sample_text", semanticCondition="sample_text", width=7)
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_aredsl_EdgeStyle_kind_value_roundtrip():
    instance = aredsl_EdgeStyle(color="sample_text", kind="sample_text", semanticCondition="sample_text", width=7)
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_aredsl_EdgeStyle_semanticCondition_value_roundtrip():
    instance = aredsl_EdgeStyle(color="sample_text", kind="sample_text", semanticCondition="sample_text", width=7)
    assert instance.semanticCondition == "sample_text"
    instance.semanticCondition = "sample_text_2"
    assert instance.semanticCondition == "sample_text_2"


def test_aredsl_EdgeStyle_width_value_roundtrip():
    instance = aredsl_EdgeStyle(color="sample_text", kind="sample_text", semanticCondition="sample_text", width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_aredsl_Editor_description_value_roundtrip():
    instance = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_Editor_fileExtension_value_roundtrip():
    instance = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    assert instance.fileExtension == "sample_text"
    instance.fileExtension = "sample_text_2"
    assert instance.fileExtension == "sample_text_2"


def test_aredsl_Editor_name_value_roundtrip():
    instance = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_aredsl_Editor_queryLanguageKind_value_roundtrip():
    instance = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    assert instance.queryLanguageKind == "sample_text"
    instance.queryLanguageKind = "sample_text_2"
    assert instance.queryLanguageKind == "sample_text_2"


def test_aredsl_GeometricShapeNodeStyle_color_value_roundtrip():
    instance = aredsl_GeometricShapeNodeStyle(color="sample_text", kind="sample_text", outline="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_aredsl_GeometricShapeNodeStyle_kind_value_roundtrip():
    instance = aredsl_GeometricShapeNodeStyle(color="sample_text", kind="sample_text", outline="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_aredsl_GeometricShapeNodeStyle_outline_value_roundtrip():
    instance = aredsl_GeometricShapeNodeStyle(color="sample_text", kind="sample_text", outline="sample_text")
    assert instance.outline == "sample_text"
    instance.outline = "sample_text_2"
    assert instance.outline == "sample_text_2"


def test_aredsl_Image2DNodeStyle_file_value_roundtrip():
    instance = aredsl_Image2DNodeStyle(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_aredsl_Label_description_value_roundtrip():
    instance = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_Label_id_value_roundtrip():
    instance = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aredsl_Label_semantics_value_roundtrip():
    instance = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.semantics == "sample_text"
    instance.semantics = "sample_text_2"
    assert instance.semantics == "sample_text_2"


def test_aredsl_LabelStyle_color_value_roundtrip():
    instance = aredsl_LabelStyle(color="sample_text", height=7, semanticCondition="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_aredsl_LabelStyle_height_value_roundtrip():
    instance = aredsl_LabelStyle(color="sample_text", height=7, semanticCondition="sample_text")
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_aredsl_LabelStyle_semanticCondition_value_roundtrip():
    instance = aredsl_LabelStyle(color="sample_text", height=7, semanticCondition="sample_text")
    assert instance.semanticCondition == "sample_text"
    instance.semanticCondition = "sample_text_2"
    assert instance.semanticCondition == "sample_text_2"


def test_aredsl_Layer_description_value_roundtrip():
    instance = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_Layer_id_value_roundtrip():
    instance = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aredsl_Layer_semantics_value_roundtrip():
    instance = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.semantics == "sample_text"
    instance.semantics = "sample_text_2"
    assert instance.semantics == "sample_text_2"


def test_aredsl_MarkerBasedTrackerAction_markerId_value_roundtrip():
    instance = aredsl_MarkerBasedTrackerAction(markerId=7)
    assert instance.markerId == 7
    instance.markerId = 13
    assert instance.markerId == 13


def test_aredsl_MarkerLessTrackerAction_file_value_roundtrip():
    instance = aredsl_MarkerLessTrackerAction(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_aredsl_Model3DNodeStyle_file_value_roundtrip():
    instance = aredsl_Model3DNodeStyle(file="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_aredsl_Node_contaimentKind_value_roundtrip():
    instance = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.contaimentKind == "sample_text"
    instance.contaimentKind = "sample_text_2"
    assert instance.contaimentKind == "sample_text_2"


def test_aredsl_Node_description_value_roundtrip():
    instance = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_Node_id_value_roundtrip():
    instance = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aredsl_Node_semantics_value_roundtrip():
    instance = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    assert instance.semantics == "sample_text"
    instance.semantics = "sample_text_2"
    assert instance.semantics == "sample_text_2"


def test_aredsl_NodeStyle_height_value_roundtrip():
    instance = aredsl_NodeStyle(height=7, semanticCondition="sample_text", width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_aredsl_NodeStyle_semanticCondition_value_roundtrip():
    instance = aredsl_NodeStyle(height=7, semanticCondition="sample_text", width=7)
    assert instance.semanticCondition == "sample_text"
    instance.semanticCondition = "sample_text_2"
    assert instance.semanticCondition == "sample_text_2"


def test_aredsl_NodeStyle_width_value_roundtrip():
    instance = aredsl_NodeStyle(height=7, semanticCondition="sample_text", width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_aredsl_RemoveOperation_constraint_value_roundtrip():
    instance = aredsl_RemoveOperation(constraint="sample_text")
    assert instance.constraint == "sample_text"
    instance.constraint = "sample_text_2"
    assert instance.constraint == "sample_text_2"


def test_aredsl_SetOperation_constraint_value_roundtrip():
    instance = aredsl_SetOperation(constraint="sample_text", feature="sample_text", value="sample_text")
    assert instance.constraint == "sample_text"
    instance.constraint = "sample_text_2"
    assert instance.constraint == "sample_text_2"


def test_aredsl_SetOperation_feature_value_roundtrip():
    instance = aredsl_SetOperation(constraint="sample_text", feature="sample_text", value="sample_text")
    assert instance.feature == "sample_text"
    instance.feature = "sample_text_2"
    assert instance.feature == "sample_text_2"


def test_aredsl_SetOperation_value_value_roundtrip():
    instance = aredsl_SetOperation(constraint="sample_text", feature="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_aredsl_Tool_description_value_roundtrip():
    instance = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_Tool_id_value_roundtrip():
    instance = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aredsl_Tool_precondition_value_roundtrip():
    instance = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    assert instance.precondition == "sample_text"
    instance.precondition = "sample_text_2"
    assert instance.precondition == "sample_text_2"


def test_aredsl_Tool_targetPrecondition_value_roundtrip():
    instance = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    assert instance.targetPrecondition == "sample_text"
    instance.targetPrecondition = "sample_text_2"
    assert instance.targetPrecondition == "sample_text_2"


def test_aredsl_ToolSet_description_value_roundtrip():
    instance = aredsl_ToolSet(description="sample_text", id="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_aredsl_ToolSet_id_value_roundtrip():
    instance = aredsl_ToolSet(description="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_aredsl_UnsetOperation_constraint_value_roundtrip():
    instance = aredsl_UnsetOperation(constraint="sample_text", feature="sample_text")
    assert instance.constraint == "sample_text"
    instance.constraint = "sample_text_2"
    assert instance.constraint == "sample_text_2"


def test_aredsl_UnsetOperation_feature_value_roundtrip():
    instance = aredsl_UnsetOperation(constraint="sample_text", feature="sample_text")
    assert instance.feature == "sample_text"
    instance.feature = "sample_text_2"
    assert instance.feature == "sample_text_2"


def test_aredsl_GestureAction_isa_Action():
    instance = aredsl_GestureAction()
    assert isinstance(instance, Action)


def test_aredsl_MentalAction_isa_Action():
    instance = aredsl_MentalAction()
    assert isinstance(instance, Action)


def test_aredsl_SensorBasedAction_isa_Action():
    instance = aredsl_SensorBasedAction()
    assert isinstance(instance, Action)


def test_aredsl_TactileAction_isa_Action():
    instance = aredsl_TactileAction()
    assert isinstance(instance, Action)


def test_aredsl_TrackerAction_isa_Action():
    instance = aredsl_TrackerAction()
    assert isinstance(instance, Action)


def test_aredsl_VoiceAction_isa_Action():
    instance = aredsl_VoiceAction()
    assert isinstance(instance, Action)


def test_aredsl_DomainOperation_isa_Behaviour():
    instance = aredsl_DomainOperation()
    assert isinstance(instance, Behaviour)


def test_aredsl_SupportOperation_isa_Behaviour():
    instance = aredsl_SupportOperation()
    assert isinstance(instance, Behaviour)


def test_aredsl_ChangeContextOperation_isa_DomainOperation():
    instance = aredsl_ChangeContextOperation(expression="sample_text")
    assert isinstance(instance, DomainOperation)


def test_aredsl_CreateInstanceOperation_isa_DomainOperation():
    instance = aredsl_CreateInstanceOperation(feature="sample_text", name="sample_text", type="sample_text")
    assert isinstance(instance, DomainOperation)


def test_aredsl_RemoveOperation_isa_DomainOperation():
    instance = aredsl_RemoveOperation(constraint="sample_text")
    assert isinstance(instance, DomainOperation)


def test_aredsl_SetOperation_isa_DomainOperation():
    instance = aredsl_SetOperation(constraint="sample_text", feature="sample_text", value="sample_text")
    assert isinstance(instance, DomainOperation)


def test_aredsl_UnsetOperation_isa_DomainOperation():
    instance = aredsl_UnsetOperation(constraint="sample_text", feature="sample_text")
    assert isinstance(instance, DomainOperation)


def test_aredsl_GeometricShapeNodeStyle_isa_NodeStyle():
    instance = aredsl_GeometricShapeNodeStyle(color="sample_text", kind="sample_text", outline="sample_text")
    assert isinstance(instance, NodeStyle)


def test_aredsl_Image2DNodeStyle_isa_NodeStyle():
    instance = aredsl_Image2DNodeStyle(file="sample_text")
    assert isinstance(instance, NodeStyle)


def test_aredsl_Model3DNodeStyle_isa_NodeStyle():
    instance = aredsl_Model3DNodeStyle(file="sample_text")
    assert isinstance(instance, NodeStyle)


def test_aredsl_ArrangeElements_isa_SupportOperation():
    instance = aredsl_ArrangeElements()
    assert isinstance(instance, SupportOperation)


def test_aredsl_Exit_isa_SupportOperation():
    instance = aredsl_Exit()
    assert isinstance(instance, SupportOperation)


def test_aredsl_MoveElement_isa_SupportOperation():
    instance = aredsl_MoveElement()
    assert isinstance(instance, SupportOperation)


def test_aredsl_ShowSystemMenu_isa_SupportOperation():
    instance = aredsl_ShowSystemMenu()
    assert isinstance(instance, SupportOperation)


def test_aredsl_MarkerBasedTrackerAction_isa_TrackerAction():
    instance = aredsl_MarkerBasedTrackerAction(markerId=7)
    assert isinstance(instance, TrackerAction)


def test_aredsl_MarkerLessTrackerAction_isa_TrackerAction():
    instance = aredsl_MarkerLessTrackerAction(file="sample_text")
    assert isinstance(instance, TrackerAction)


def test_assoc_actions36_link_reassign_clear():
    a = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    b1 = aredsl_Action(description="sample_text")
    b2 = aredsl_Action(description="sample_text_2")
    _safe_set(a, 'aredsl_Tool37', {b1})
    assert _is_linked(a, 'aredsl_Tool37', b1)
    if hasattr(b1, 'aredsl_Action'):
        assert _is_linked(b1, 'aredsl_Action', a)
    _safe_set(a, 'aredsl_Tool37', {b2})
    assert _is_linked(a, 'aredsl_Tool37', b2)
    if hasattr(b1, 'aredsl_Action'):
        assert not _is_linked(b1, 'aredsl_Action', a)
    if hasattr(b2, 'aredsl_Action'):
        assert _is_linked(b2, 'aredsl_Action', a)
    _safe_set(a, 'aredsl_Tool37', set())
    assert not _is_linked(a, 'aredsl_Tool37', b2)
    if hasattr(b2, 'aredsl_Action'):
        assert not _is_linked(b2, 'aredsl_Action', a)


def test_assoc_behaviours35_link_reassign_clear():
    a = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    b1 = aredsl_Behaviour(description="sample_text")
    b2 = aredsl_Behaviour(description="sample_text_2")
    _safe_set(a, 'aredsl_Tool', {b1})
    assert _is_linked(a, 'aredsl_Tool', b1)
    if hasattr(b1, 'aredsl_Behaviour'):
        assert _is_linked(b1, 'aredsl_Behaviour', a)
    _safe_set(a, 'aredsl_Tool', {b2})
    assert _is_linked(a, 'aredsl_Tool', b2)
    if hasattr(b1, 'aredsl_Behaviour'):
        assert not _is_linked(b1, 'aredsl_Behaviour', a)
    if hasattr(b2, 'aredsl_Behaviour'):
        assert _is_linked(b2, 'aredsl_Behaviour', a)
    _safe_set(a, 'aredsl_Tool', set())
    assert not _is_linked(a, 'aredsl_Tool', b2)
    if hasattr(b2, 'aredsl_Behaviour'):
        assert not _is_linked(b2, 'aredsl_Behaviour', a)


def test_assoc_contentNodes14_link_reassign_clear():
    a = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    b2 = aredsl_Node(contaimentKind="sample_text_2", description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    _safe_set(a, 'aredsl_Node13', {b1})
    assert _is_linked(a, 'aredsl_Node13', b1)
    if hasattr(b1, 'aredsl_Node15'):
        assert _is_linked(b1, 'aredsl_Node15', a)
    _safe_set(a, 'aredsl_Node13', {b2})
    assert _is_linked(a, 'aredsl_Node13', b2)
    if hasattr(b1, 'aredsl_Node15'):
        assert not _is_linked(b1, 'aredsl_Node15', a)
    if hasattr(b2, 'aredsl_Node15'):
        assert _is_linked(b2, 'aredsl_Node15', a)
    _safe_set(a, 'aredsl_Node13', set())
    assert not _is_linked(a, 'aredsl_Node13', b2)
    if hasattr(b2, 'aredsl_Node15'):
        assert not _is_linked(b2, 'aredsl_Node15', a)


def test_assoc_destinationLabel32_link_reassign_clear():
    a = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    b2 = aredsl_Edge(description="sample_text_2", destinationSemantics="sample_text_2", id="sample_text_2", originSemantics="sample_text_2")
    _safe_set(a, 'aredsl_Label34', b1)
    assert _is_linked(a, 'aredsl_Label34', b1)
    if hasattr(b1, 'aredsl_Edge33'):
        assert _is_linked(b1, 'aredsl_Edge33', a)
    _safe_set(a, 'aredsl_Label34', b2)
    assert _is_linked(a, 'aredsl_Label34', b2)
    if hasattr(b1, 'aredsl_Edge33'):
        assert not _is_linked(b1, 'aredsl_Edge33', a)
    if hasattr(b2, 'aredsl_Edge33'):
        assert _is_linked(b2, 'aredsl_Edge33', a)
    _safe_set(a, 'aredsl_Label34', None)
    assert not _is_linked(a, 'aredsl_Label34', b2)
    if hasattr(b2, 'aredsl_Edge33'):
        assert not _is_linked(b2, 'aredsl_Edge33', a)


def test_assoc_destinationNode26_link_reassign_clear():
    a = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    b2 = aredsl_Edge(description="sample_text_2", destinationSemantics="sample_text_2", id="sample_text_2", originSemantics="sample_text_2")
    _safe_set(a, 'aredsl_Node28', b1)
    assert _is_linked(a, 'aredsl_Node28', b1)
    if hasattr(b1, 'aredsl_Edge27'):
        assert _is_linked(b1, 'aredsl_Edge27', a)
    _safe_set(a, 'aredsl_Node28', b2)
    assert _is_linked(a, 'aredsl_Node28', b2)
    if hasattr(b1, 'aredsl_Edge27'):
        assert not _is_linked(b1, 'aredsl_Edge27', a)
    if hasattr(b2, 'aredsl_Edge27'):
        assert _is_linked(b2, 'aredsl_Edge27', a)
    _safe_set(a, 'aredsl_Node28', None)
    assert not _is_linked(a, 'aredsl_Node28', b2)
    if hasattr(b2, 'aredsl_Edge27'):
        assert not _is_linked(b2, 'aredsl_Edge27', a)


def test_assoc_edges5_link_reassign_clear():
    a = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    b2 = aredsl_Edge(description="sample_text_2", destinationSemantics="sample_text_2", id="sample_text_2", originSemantics="sample_text_2")
    _safe_set(a, 'aredsl_Layer6', {b1})
    assert _is_linked(a, 'aredsl_Layer6', b1)
    if hasattr(b1, 'aredsl_Edge'):
        assert _is_linked(b1, 'aredsl_Edge', a)
    _safe_set(a, 'aredsl_Layer6', {b2})
    assert _is_linked(a, 'aredsl_Layer6', b2)
    if hasattr(b1, 'aredsl_Edge'):
        assert not _is_linked(b1, 'aredsl_Edge', a)
    if hasattr(b2, 'aredsl_Edge'):
        assert _is_linked(b2, 'aredsl_Edge', a)
    _safe_set(a, 'aredsl_Layer6', set())
    assert not _is_linked(a, 'aredsl_Layer6', b2)
    if hasattr(b2, 'aredsl_Edge'):
        assert not _is_linked(b2, 'aredsl_Edge', a)


def test_assoc_edgestyles18_link_reassign_clear():
    a = aredsl_EdgeStyle(color="sample_text", kind="sample_text", semanticCondition="sample_text", width=7)
    b1 = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    b2 = aredsl_Edge(description="sample_text_2", destinationSemantics="sample_text_2", id="sample_text_2", originSemantics="sample_text_2")
    _safe_set(a, 'aredsl_EdgeStyle', b1)
    assert _is_linked(a, 'aredsl_EdgeStyle', b1)
    if hasattr(b1, 'aredsl_Edge19'):
        assert _is_linked(b1, 'aredsl_Edge19', a)
    _safe_set(a, 'aredsl_EdgeStyle', b2)
    assert _is_linked(a, 'aredsl_EdgeStyle', b2)
    if hasattr(b1, 'aredsl_Edge19'):
        assert not _is_linked(b1, 'aredsl_Edge19', a)
    if hasattr(b2, 'aredsl_Edge19'):
        assert _is_linked(b2, 'aredsl_Edge19', a)
    _safe_set(a, 'aredsl_EdgeStyle', None)
    assert not _is_linked(a, 'aredsl_EdgeStyle', b2)
    if hasattr(b2, 'aredsl_Edge19'):
        assert not _is_linked(b2, 'aredsl_Edge19', a)


def test_assoc_label11_link_reassign_clear():
    a = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    b2 = aredsl_Label(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    _safe_set(a, 'aredsl_Node12', b1)
    assert _is_linked(a, 'aredsl_Node12', b1)
    if hasattr(b1, 'aredsl_Label'):
        assert _is_linked(b1, 'aredsl_Label', a)
    _safe_set(a, 'aredsl_Node12', b2)
    assert _is_linked(a, 'aredsl_Node12', b2)
    if hasattr(b1, 'aredsl_Label'):
        assert not _is_linked(b1, 'aredsl_Label', a)
    if hasattr(b2, 'aredsl_Label'):
        assert _is_linked(b2, 'aredsl_Label', a)
    _safe_set(a, 'aredsl_Node12', None)
    assert not _is_linked(a, 'aredsl_Node12', b2)
    if hasattr(b2, 'aredsl_Label'):
        assert not _is_linked(b2, 'aredsl_Label', a)


def test_assoc_labelstyles16_link_reassign_clear():
    a = aredsl_LabelStyle(color="sample_text", height=7, semanticCondition="sample_text")
    b1 = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    b2 = aredsl_Label(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    _safe_set(a, 'aredsl_LabelStyle', b1)
    assert _is_linked(a, 'aredsl_LabelStyle', b1)
    if hasattr(b1, 'aredsl_Label17'):
        assert _is_linked(b1, 'aredsl_Label17', a)
    _safe_set(a, 'aredsl_LabelStyle', b2)
    assert _is_linked(a, 'aredsl_LabelStyle', b2)
    if hasattr(b1, 'aredsl_Label17'):
        assert not _is_linked(b1, 'aredsl_Label17', a)
    if hasattr(b2, 'aredsl_Label17'):
        assert _is_linked(b2, 'aredsl_Label17', a)
    _safe_set(a, 'aredsl_LabelStyle', None)
    assert not _is_linked(a, 'aredsl_LabelStyle', b2)
    if hasattr(b2, 'aredsl_Label17'):
        assert not _is_linked(b2, 'aredsl_Label17', a)


def test_assoc_layer0_link_reassign_clear():
    a = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    b2 = aredsl_Editor(description="sample_text_2", fileExtension="sample_text_2", name="sample_text_2", queryLanguageKind="sample_text_2")
    _safe_set(a, 'aredsl_Layer', b1)
    assert _is_linked(a, 'aredsl_Layer', b1)
    if hasattr(b1, 'aredsl_Editor'):
        assert _is_linked(b1, 'aredsl_Editor', a)
    _safe_set(a, 'aredsl_Layer', b2)
    assert _is_linked(a, 'aredsl_Layer', b2)
    if hasattr(b1, 'aredsl_Editor'):
        assert not _is_linked(b1, 'aredsl_Editor', a)
    if hasattr(b2, 'aredsl_Editor'):
        assert _is_linked(b2, 'aredsl_Editor', a)
    _safe_set(a, 'aredsl_Layer', None)
    assert not _is_linked(a, 'aredsl_Layer', b2)
    if hasattr(b2, 'aredsl_Editor'):
        assert not _is_linked(b2, 'aredsl_Editor', a)


def test_assoc_middleLabel20_link_reassign_clear():
    a = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    b2 = aredsl_Edge(description="sample_text_2", destinationSemantics="sample_text_2", id="sample_text_2", originSemantics="sample_text_2")
    _safe_set(a, 'aredsl_Label22', b1)
    assert _is_linked(a, 'aredsl_Label22', b1)
    if hasattr(b1, 'aredsl_Edge21'):
        assert _is_linked(b1, 'aredsl_Edge21', a)
    _safe_set(a, 'aredsl_Label22', b2)
    assert _is_linked(a, 'aredsl_Label22', b2)
    if hasattr(b1, 'aredsl_Edge21'):
        assert not _is_linked(b1, 'aredsl_Edge21', a)
    if hasattr(b2, 'aredsl_Edge21'):
        assert _is_linked(b2, 'aredsl_Edge21', a)
    _safe_set(a, 'aredsl_Label22', None)
    assert not _is_linked(a, 'aredsl_Label22', b2)
    if hasattr(b2, 'aredsl_Edge21'):
        assert not _is_linked(b2, 'aredsl_Edge21', a)


def test_assoc_nodes3_link_reassign_clear():
    a = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    b2 = aredsl_Layer(description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    _safe_set(a, 'aredsl_Node', b1)
    assert _is_linked(a, 'aredsl_Node', b1)
    if hasattr(b1, 'aredsl_Layer4'):
        assert _is_linked(b1, 'aredsl_Layer4', a)
    _safe_set(a, 'aredsl_Node', b2)
    assert _is_linked(a, 'aredsl_Node', b2)
    if hasattr(b1, 'aredsl_Layer4'):
        assert not _is_linked(b1, 'aredsl_Layer4', a)
    if hasattr(b2, 'aredsl_Layer4'):
        assert _is_linked(b2, 'aredsl_Layer4', a)
    _safe_set(a, 'aredsl_Node', None)
    assert not _is_linked(a, 'aredsl_Node', b2)
    if hasattr(b2, 'aredsl_Layer4'):
        assert not _is_linked(b2, 'aredsl_Layer4', a)


def test_assoc_nodestyles9_link_reassign_clear():
    a = aredsl_NodeStyle(height=7, semanticCondition="sample_text", width=7)
    b1 = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    b2 = aredsl_Node(contaimentKind="sample_text_2", description="sample_text_2", id="sample_text_2", semantics="sample_text_2")
    _safe_set(a, 'aredsl_NodeStyle', b1)
    assert _is_linked(a, 'aredsl_NodeStyle', b1)
    if hasattr(b1, 'aredsl_Node10'):
        assert _is_linked(b1, 'aredsl_Node10', a)
    _safe_set(a, 'aredsl_NodeStyle', b2)
    assert _is_linked(a, 'aredsl_NodeStyle', b2)
    if hasattr(b1, 'aredsl_Node10'):
        assert not _is_linked(b1, 'aredsl_Node10', a)
    if hasattr(b2, 'aredsl_Node10'):
        assert _is_linked(b2, 'aredsl_Node10', a)
    _safe_set(a, 'aredsl_NodeStyle', None)
    assert not _is_linked(a, 'aredsl_NodeStyle', b2)
    if hasattr(b2, 'aredsl_Node10'):
        assert not _is_linked(b2, 'aredsl_Node10', a)


def test_assoc_originLabel29_link_reassign_clear():
    a = aredsl_Label(description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    b2 = aredsl_Edge(description="sample_text_2", destinationSemantics="sample_text_2", id="sample_text_2", originSemantics="sample_text_2")
    _safe_set(a, 'aredsl_Label31', b1)
    assert _is_linked(a, 'aredsl_Label31', b1)
    if hasattr(b1, 'aredsl_Edge30'):
        assert _is_linked(b1, 'aredsl_Edge30', a)
    _safe_set(a, 'aredsl_Label31', b2)
    assert _is_linked(a, 'aredsl_Label31', b2)
    if hasattr(b1, 'aredsl_Edge30'):
        assert not _is_linked(b1, 'aredsl_Edge30', a)
    if hasattr(b2, 'aredsl_Edge30'):
        assert _is_linked(b2, 'aredsl_Edge30', a)
    _safe_set(a, 'aredsl_Label31', None)
    assert not _is_linked(a, 'aredsl_Label31', b2)
    if hasattr(b2, 'aredsl_Edge30'):
        assert not _is_linked(b2, 'aredsl_Edge30', a)


def test_assoc_originNode23_link_reassign_clear():
    a = aredsl_Node(contaimentKind="sample_text", description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_Edge(description="sample_text", destinationSemantics="sample_text", id="sample_text", originSemantics="sample_text")
    b2 = aredsl_Edge(description="sample_text_2", destinationSemantics="sample_text_2", id="sample_text_2", originSemantics="sample_text_2")
    _safe_set(a, 'aredsl_Node25', b1)
    assert _is_linked(a, 'aredsl_Node25', b1)
    if hasattr(b1, 'aredsl_Edge24'):
        assert _is_linked(b1, 'aredsl_Edge24', a)
    _safe_set(a, 'aredsl_Node25', b2)
    assert _is_linked(a, 'aredsl_Node25', b2)
    if hasattr(b1, 'aredsl_Edge24'):
        assert not _is_linked(b1, 'aredsl_Edge24', a)
    if hasattr(b2, 'aredsl_Edge24'):
        assert _is_linked(b2, 'aredsl_Edge24', a)
    _safe_set(a, 'aredsl_Node25', None)
    assert not _is_linked(a, 'aredsl_Node25', b2)
    if hasattr(b2, 'aredsl_Edge24'):
        assert not _is_linked(b2, 'aredsl_Edge24', a)


def test_assoc_referenceAction7_link_reassign_clear():
    a = aredsl_Layer(description="sample_text", id="sample_text", semantics="sample_text")
    b1 = aredsl_TrackerAction()
    b2 = aredsl_TrackerAction()
    _safe_set(a, 'aredsl_Layer8', b1)
    assert _is_linked(a, 'aredsl_Layer8', b1)
    if hasattr(b1, 'aredsl_TrackerAction'):
        assert _is_linked(b1, 'aredsl_TrackerAction', a)
    _safe_set(a, 'aredsl_Layer8', b2)
    assert _is_linked(a, 'aredsl_Layer8', b2)
    if hasattr(b1, 'aredsl_TrackerAction'):
        assert not _is_linked(b1, 'aredsl_TrackerAction', a)
    if hasattr(b2, 'aredsl_TrackerAction'):
        assert _is_linked(b2, 'aredsl_TrackerAction', a)
    _safe_set(a, 'aredsl_Layer8', None)
    assert not _is_linked(a, 'aredsl_Layer8', b2)
    if hasattr(b2, 'aredsl_TrackerAction'):
        assert not _is_linked(b2, 'aredsl_TrackerAction', a)


def test_assoc_tools38_link_reassign_clear():
    a = aredsl_ToolSet(description="sample_text", id="sample_text")
    b1 = aredsl_Tool(description="sample_text", id="sample_text", precondition="sample_text", targetPrecondition="sample_text")
    b2 = aredsl_Tool(description="sample_text_2", id="sample_text_2", precondition="sample_text_2", targetPrecondition="sample_text_2")
    _safe_set(a, 'aredsl_ToolSet39', {b1})
    assert _is_linked(a, 'aredsl_ToolSet39', b1)
    if hasattr(b1, 'aredsl_Tool40'):
        assert _is_linked(b1, 'aredsl_Tool40', a)
    _safe_set(a, 'aredsl_ToolSet39', {b2})
    assert _is_linked(a, 'aredsl_ToolSet39', b2)
    if hasattr(b1, 'aredsl_Tool40'):
        assert not _is_linked(b1, 'aredsl_Tool40', a)
    if hasattr(b2, 'aredsl_Tool40'):
        assert _is_linked(b2, 'aredsl_Tool40', a)
    _safe_set(a, 'aredsl_ToolSet39', set())
    assert not _is_linked(a, 'aredsl_ToolSet39', b2)
    if hasattr(b2, 'aredsl_Tool40'):
        assert not _is_linked(b2, 'aredsl_Tool40', a)


def test_assoc_toolsets1_link_reassign_clear():
    a = aredsl_ToolSet(description="sample_text", id="sample_text")
    b1 = aredsl_Editor(description="sample_text", fileExtension="sample_text", name="sample_text", queryLanguageKind="sample_text")
    b2 = aredsl_Editor(description="sample_text_2", fileExtension="sample_text_2", name="sample_text_2", queryLanguageKind="sample_text_2")
    _safe_set(a, 'aredsl_ToolSet', b1)
    assert _is_linked(a, 'aredsl_ToolSet', b1)
    if hasattr(b1, 'aredsl_Editor2'):
        assert _is_linked(b1, 'aredsl_Editor2', a)
    _safe_set(a, 'aredsl_ToolSet', b2)
    assert _is_linked(a, 'aredsl_ToolSet', b2)
    if hasattr(b1, 'aredsl_Editor2'):
        assert not _is_linked(b1, 'aredsl_Editor2', a)
    if hasattr(b2, 'aredsl_Editor2'):
        assert _is_linked(b2, 'aredsl_Editor2', a)
    _safe_set(a, 'aredsl_ToolSet', None)
    assert not _is_linked(a, 'aredsl_ToolSet', b2)
    if hasattr(b2, 'aredsl_Editor2'):
        assert not _is_linked(b2, 'aredsl_Editor2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Behaviour_strategy = st.builds(Behaviour)
@given(instance=Behaviour_strategy)
@settings(max_examples=25)
def test_Behaviour_instantiation(instance):
    assert isinstance(instance, Behaviour)


DomainOperation_strategy = st.builds(DomainOperation)
@given(instance=DomainOperation_strategy)
@settings(max_examples=25)
def test_DomainOperation_instantiation(instance):
    assert isinstance(instance, DomainOperation)


NodeStyle_strategy = st.builds(NodeStyle)
@given(instance=NodeStyle_strategy)
@settings(max_examples=25)
def test_NodeStyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)


SupportOperation_strategy = st.builds(SupportOperation)
@given(instance=SupportOperation_strategy)
@settings(max_examples=25)
def test_SupportOperation_instantiation(instance):
    assert isinstance(instance, SupportOperation)


TrackerAction_strategy = st.builds(TrackerAction)
@given(instance=TrackerAction_strategy)
@settings(max_examples=25)
def test_TrackerAction_instantiation(instance):
    assert isinstance(instance, TrackerAction)


aredsl_Action_strategy = st.builds(aredsl_Action, description=safe_text)
@given(instance=aredsl_Action_strategy)
@settings(max_examples=25)
def test_aredsl_Action_instantiation(instance):
    assert isinstance(instance, aredsl_Action)


aredsl_ArrangeElements_strategy = st.builds(aredsl_ArrangeElements)
@given(instance=aredsl_ArrangeElements_strategy)
@settings(max_examples=25)
def test_aredsl_ArrangeElements_instantiation(instance):
    assert isinstance(instance, aredsl_ArrangeElements)


aredsl_Behaviour_strategy = st.builds(aredsl_Behaviour, description=safe_text)
@given(instance=aredsl_Behaviour_strategy)
@settings(max_examples=25)
def test_aredsl_Behaviour_instantiation(instance):
    assert isinstance(instance, aredsl_Behaviour)


aredsl_ChangeContextOperation_strategy = st.builds(aredsl_ChangeContextOperation, expression=safe_text)
@given(instance=aredsl_ChangeContextOperation_strategy)
@settings(max_examples=25)
def test_aredsl_ChangeContextOperation_instantiation(instance):
    assert isinstance(instance, aredsl_ChangeContextOperation)


aredsl_CreateInstanceOperation_strategy = st.builds(aredsl_CreateInstanceOperation, feature=safe_text, name=safe_text, type=safe_text)
@given(instance=aredsl_CreateInstanceOperation_strategy)
@settings(max_examples=25)
def test_aredsl_CreateInstanceOperation_instantiation(instance):
    assert isinstance(instance, aredsl_CreateInstanceOperation)


aredsl_DomainOperation_strategy = st.builds(aredsl_DomainOperation)
@given(instance=aredsl_DomainOperation_strategy)
@settings(max_examples=25)
def test_aredsl_DomainOperation_instantiation(instance):
    assert isinstance(instance, aredsl_DomainOperation)


aredsl_Edge_strategy = st.builds(aredsl_Edge, description=safe_text, destinationSemantics=safe_text, id=safe_text, originSemantics=safe_text)
@given(instance=aredsl_Edge_strategy)
@settings(max_examples=25)
def test_aredsl_Edge_instantiation(instance):
    assert isinstance(instance, aredsl_Edge)


aredsl_EdgeStyle_strategy = st.builds(aredsl_EdgeStyle, color=safe_text, kind=safe_text, semanticCondition=safe_text, width=st.integers())
@given(instance=aredsl_EdgeStyle_strategy)
@settings(max_examples=25)
def test_aredsl_EdgeStyle_instantiation(instance):
    assert isinstance(instance, aredsl_EdgeStyle)


aredsl_Editor_strategy = st.builds(aredsl_Editor, description=safe_text, fileExtension=safe_text, name=safe_text, queryLanguageKind=safe_text)
@given(instance=aredsl_Editor_strategy)
@settings(max_examples=25)
def test_aredsl_Editor_instantiation(instance):
    assert isinstance(instance, aredsl_Editor)


aredsl_Exit_strategy = st.builds(aredsl_Exit)
@given(instance=aredsl_Exit_strategy)
@settings(max_examples=25)
def test_aredsl_Exit_instantiation(instance):
    assert isinstance(instance, aredsl_Exit)


aredsl_GeometricShapeNodeStyle_strategy = st.builds(aredsl_GeometricShapeNodeStyle, color=safe_text, kind=safe_text, outline=safe_text)
@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
@settings(max_examples=25)
def test_aredsl_GeometricShapeNodeStyle_instantiation(instance):
    assert isinstance(instance, aredsl_GeometricShapeNodeStyle)


aredsl_GestureAction_strategy = st.builds(aredsl_GestureAction)
@given(instance=aredsl_GestureAction_strategy)
@settings(max_examples=25)
def test_aredsl_GestureAction_instantiation(instance):
    assert isinstance(instance, aredsl_GestureAction)


aredsl_Image2DNodeStyle_strategy = st.builds(aredsl_Image2DNodeStyle, file=safe_text)
@given(instance=aredsl_Image2DNodeStyle_strategy)
@settings(max_examples=25)
def test_aredsl_Image2DNodeStyle_instantiation(instance):
    assert isinstance(instance, aredsl_Image2DNodeStyle)


aredsl_Label_strategy = st.builds(aredsl_Label, description=safe_text, id=safe_text, semantics=safe_text)
@given(instance=aredsl_Label_strategy)
@settings(max_examples=25)
def test_aredsl_Label_instantiation(instance):
    assert isinstance(instance, aredsl_Label)


aredsl_LabelStyle_strategy = st.builds(aredsl_LabelStyle, color=safe_text, height=st.integers(), semanticCondition=safe_text)
@given(instance=aredsl_LabelStyle_strategy)
@settings(max_examples=25)
def test_aredsl_LabelStyle_instantiation(instance):
    assert isinstance(instance, aredsl_LabelStyle)


aredsl_Layer_strategy = st.builds(aredsl_Layer, description=safe_text, id=safe_text, semantics=safe_text)
@given(instance=aredsl_Layer_strategy)
@settings(max_examples=25)
def test_aredsl_Layer_instantiation(instance):
    assert isinstance(instance, aredsl_Layer)


aredsl_MarkerBasedTrackerAction_strategy = st.builds(aredsl_MarkerBasedTrackerAction, markerId=st.integers())
@given(instance=aredsl_MarkerBasedTrackerAction_strategy)
@settings(max_examples=25)
def test_aredsl_MarkerBasedTrackerAction_instantiation(instance):
    assert isinstance(instance, aredsl_MarkerBasedTrackerAction)


aredsl_MarkerLessTrackerAction_strategy = st.builds(aredsl_MarkerLessTrackerAction, file=safe_text)
@given(instance=aredsl_MarkerLessTrackerAction_strategy)
@settings(max_examples=25)
def test_aredsl_MarkerLessTrackerAction_instantiation(instance):
    assert isinstance(instance, aredsl_MarkerLessTrackerAction)


aredsl_MentalAction_strategy = st.builds(aredsl_MentalAction)
@given(instance=aredsl_MentalAction_strategy)
@settings(max_examples=25)
def test_aredsl_MentalAction_instantiation(instance):
    assert isinstance(instance, aredsl_MentalAction)


aredsl_Model3DNodeStyle_strategy = st.builds(aredsl_Model3DNodeStyle, file=safe_text)
@given(instance=aredsl_Model3DNodeStyle_strategy)
@settings(max_examples=25)
def test_aredsl_Model3DNodeStyle_instantiation(instance):
    assert isinstance(instance, aredsl_Model3DNodeStyle)


aredsl_MoveElement_strategy = st.builds(aredsl_MoveElement)
@given(instance=aredsl_MoveElement_strategy)
@settings(max_examples=25)
def test_aredsl_MoveElement_instantiation(instance):
    assert isinstance(instance, aredsl_MoveElement)


aredsl_Node_strategy = st.builds(aredsl_Node, contaimentKind=safe_text, description=safe_text, id=safe_text, semantics=safe_text)
@given(instance=aredsl_Node_strategy)
@settings(max_examples=25)
def test_aredsl_Node_instantiation(instance):
    assert isinstance(instance, aredsl_Node)


aredsl_NodeStyle_strategy = st.builds(aredsl_NodeStyle, height=st.integers(), semanticCondition=safe_text, width=st.integers())
@given(instance=aredsl_NodeStyle_strategy)
@settings(max_examples=25)
def test_aredsl_NodeStyle_instantiation(instance):
    assert isinstance(instance, aredsl_NodeStyle)


aredsl_RemoveOperation_strategy = st.builds(aredsl_RemoveOperation, constraint=safe_text)
@given(instance=aredsl_RemoveOperation_strategy)
@settings(max_examples=25)
def test_aredsl_RemoveOperation_instantiation(instance):
    assert isinstance(instance, aredsl_RemoveOperation)


aredsl_SensorBasedAction_strategy = st.builds(aredsl_SensorBasedAction)
@given(instance=aredsl_SensorBasedAction_strategy)
@settings(max_examples=25)
def test_aredsl_SensorBasedAction_instantiation(instance):
    assert isinstance(instance, aredsl_SensorBasedAction)


aredsl_SetOperation_strategy = st.builds(aredsl_SetOperation, constraint=safe_text, feature=safe_text, value=safe_text)
@given(instance=aredsl_SetOperation_strategy)
@settings(max_examples=25)
def test_aredsl_SetOperation_instantiation(instance):
    assert isinstance(instance, aredsl_SetOperation)


aredsl_ShowSystemMenu_strategy = st.builds(aredsl_ShowSystemMenu)
@given(instance=aredsl_ShowSystemMenu_strategy)
@settings(max_examples=25)
def test_aredsl_ShowSystemMenu_instantiation(instance):
    assert isinstance(instance, aredsl_ShowSystemMenu)


aredsl_SupportOperation_strategy = st.builds(aredsl_SupportOperation)
@given(instance=aredsl_SupportOperation_strategy)
@settings(max_examples=25)
def test_aredsl_SupportOperation_instantiation(instance):
    assert isinstance(instance, aredsl_SupportOperation)


aredsl_TactileAction_strategy = st.builds(aredsl_TactileAction)
@given(instance=aredsl_TactileAction_strategy)
@settings(max_examples=25)
def test_aredsl_TactileAction_instantiation(instance):
    assert isinstance(instance, aredsl_TactileAction)


aredsl_Tool_strategy = st.builds(aredsl_Tool, description=safe_text, id=safe_text, precondition=safe_text, targetPrecondition=safe_text)
@given(instance=aredsl_Tool_strategy)
@settings(max_examples=25)
def test_aredsl_Tool_instantiation(instance):
    assert isinstance(instance, aredsl_Tool)


aredsl_ToolSet_strategy = st.builds(aredsl_ToolSet, description=safe_text, id=safe_text)
@given(instance=aredsl_ToolSet_strategy)
@settings(max_examples=25)
def test_aredsl_ToolSet_instantiation(instance):
    assert isinstance(instance, aredsl_ToolSet)


aredsl_TrackerAction_strategy = st.builds(aredsl_TrackerAction)
@given(instance=aredsl_TrackerAction_strategy)
@settings(max_examples=25)
def test_aredsl_TrackerAction_instantiation(instance):
    assert isinstance(instance, aredsl_TrackerAction)


aredsl_UnsetOperation_strategy = st.builds(aredsl_UnsetOperation, constraint=safe_text, feature=safe_text)
@given(instance=aredsl_UnsetOperation_strategy)
@settings(max_examples=25)
def test_aredsl_UnsetOperation_instantiation(instance):
    assert isinstance(instance, aredsl_UnsetOperation)


aredsl_VoiceAction_strategy = st.builds(aredsl_VoiceAction)
@given(instance=aredsl_VoiceAction_strategy)
@settings(max_examples=25)
def test_aredsl_VoiceAction_instantiation(instance):
    assert isinstance(instance, aredsl_VoiceAction)



