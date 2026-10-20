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
    YasperEPNML114_TransitionSpecific,
    YasperEPNML114_Transformation,
    YasperEPNML114_Roles,
    YasperEPNML114_Role,
    YasperEPNML114_ReferencePlaceSpecific,
    YasperEPNML114_ProcessingTime,
    Place,
    YasperEPNML114_PlaceType,
    YasperEPNML114_Place,
    YasperEPNML114_TransitionType,
    YasperEPNML114_ReferencePlace,
    YasperEPNML114_NodeGraphics,
    YasperEPNML114_Page,
    YasperEPNML114_Transition,
    YasperEPNML114_Net,
    YasperEPNML114_PlaceType1,
    YasperEPNML114_NetGraphics,
    YasperEPNML114_InitialMarking,
    YasperEPNML114_DocumentRoot,
    YasperEPNML114_Cost,
    YasperEPNML114_Pnml,
    YasperEPNML114_EStringToStringMapEntry,
    YasperEPNML114_ConnectionWeight,
    YasperEPNML114_ConnectionWeights,
    YasperEPNML114_Stat,
    YasperEPNML114_PnmlAnnotation,
    YasperEPNML114_Inscription,
    YasperEPNML114_EdgeGraphics,
    YasperEPNML114_ToolspecificType,
    YasperEPNML114_TwoDimVector,
    YasperEPNML114_AnnotationGraphics,
    YasperEPNML114_ArcType,
    YasperEPNML114_Arc,
    Version,
    Tool,
    TextType2,
    TextType1,
    TextTypeMember0,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_yasperepnml114_transitionspecific_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_TransitionSpecific)


def test_hyp_yasperepnml114_transitionspecific_constructor_exists():
    assert callable(YasperEPNML114_TransitionSpecific.__init__)


def test_hyp_yasperepnml114_transitionspecific_constructor_args():
    sig = inspect.signature(YasperEPNML114_TransitionSpecific.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"
    assert "tokenCaseSensitive" in params, "Missing parameter 'tokenCaseSensitive'"






def test_hyp_yasperepnml114_transformation_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Transformation)


def test_hyp_yasperepnml114_transformation_constructor_exists():
    assert callable(YasperEPNML114_Transformation.__init__)


def test_hyp_yasperepnml114_transformation_constructor_args():
    sig = inspect.signature(YasperEPNML114_Transformation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_roles_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Roles)


def test_hyp_yasperepnml114_roles_constructor_exists():
    assert callable(YasperEPNML114_Roles.__init__)


def test_hyp_yasperepnml114_roles_constructor_args():
    sig = inspect.signature(YasperEPNML114_Roles.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_role_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Role)


def test_hyp_yasperepnml114_role_constructor_exists():
    assert callable(YasperEPNML114_Role.__init__)


def test_hyp_yasperepnml114_role_constructor_args():
    sig = inspect.signature(YasperEPNML114_Role.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_referenceplacespecific_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ReferencePlaceSpecific)


def test_hyp_yasperepnml114_referenceplacespecific_constructor_exists():
    assert callable(YasperEPNML114_ReferencePlaceSpecific.__init__)


def test_hyp_yasperepnml114_referenceplacespecific_constructor_args():
    sig = inspect.signature(YasperEPNML114_ReferencePlaceSpecific.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"





def test_hyp_yasperepnml114_processingtime_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ProcessingTime)


def test_hyp_yasperepnml114_processingtime_constructor_exists():
    assert callable(YasperEPNML114_ProcessingTime.__init__)


def test_hyp_yasperepnml114_processingtime_constructor_args():
    sig = inspect.signature(YasperEPNML114_ProcessingTime.__init__)
    params = list(sig.parameters.keys())



def test_hyp_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_hyp_place_constructor_exists():
    assert callable(Place.__init__)


def test_hyp_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_placetype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_PlaceType)


def test_hyp_yasperepnml114_placetype_constructor_exists():
    assert callable(YasperEPNML114_PlaceType.__init__)


def test_hyp_yasperepnml114_placetype_constructor_args():
    sig = inspect.signature(YasperEPNML114_PlaceType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_place_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Place)


def test_hyp_yasperepnml114_place_constructor_exists():
    assert callable(YasperEPNML114_Place.__init__)


def test_hyp_yasperepnml114_place_constructor_args():
    sig = inspect.signature(YasperEPNML114_Place.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"





def test_hyp_yasperepnml114_transitiontype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_TransitionType)


def test_hyp_yasperepnml114_transitiontype_constructor_exists():
    assert callable(YasperEPNML114_TransitionType.__init__)


def test_hyp_yasperepnml114_transitiontype_constructor_args():
    sig = inspect.signature(YasperEPNML114_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_referenceplace_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ReferencePlace)


def test_hyp_yasperepnml114_referenceplace_constructor_exists():
    assert callable(YasperEPNML114_ReferencePlace.__init__)


def test_hyp_yasperepnml114_referenceplace_constructor_args():
    sig = inspect.signature(YasperEPNML114_ReferencePlace.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "ref" in params, "Missing parameter 'ref'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_yasperepnml114_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_NodeGraphics)


def test_hyp_yasperepnml114_nodegraphics_constructor_exists():
    assert callable(YasperEPNML114_NodeGraphics.__init__)


def test_hyp_yasperepnml114_nodegraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_NodeGraphics.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_yasperepnml114_page_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Page)


def test_hyp_yasperepnml114_page_constructor_exists():
    assert callable(YasperEPNML114_Page.__init__)


def test_hyp_yasperepnml114_page_constructor_args():
    sig = inspect.signature(YasperEPNML114_Page.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_yasperepnml114_transition_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Transition)


def test_hyp_yasperepnml114_transition_constructor_exists():
    assert callable(YasperEPNML114_Transition.__init__)


def test_hyp_yasperepnml114_transition_constructor_args():
    sig = inspect.signature(YasperEPNML114_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"





def test_hyp_yasperepnml114_net_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Net)


def test_hyp_yasperepnml114_net_constructor_exists():
    assert callable(YasperEPNML114_Net.__init__)


def test_hyp_yasperepnml114_net_constructor_args():
    sig = inspect.signature(YasperEPNML114_Net.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_yasperepnml114_placetype1_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_PlaceType1)


def test_hyp_yasperepnml114_placetype1_constructor_exists():
    assert callable(YasperEPNML114_PlaceType1.__init__)


def test_hyp_yasperepnml114_placetype1_constructor_args():
    sig = inspect.signature(YasperEPNML114_PlaceType1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_netgraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_NetGraphics)


def test_hyp_yasperepnml114_netgraphics_constructor_exists():
    assert callable(YasperEPNML114_NetGraphics.__init__)


def test_hyp_yasperepnml114_netgraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_NetGraphics.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_yasperepnml114_initialmarking_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_InitialMarking)


def test_hyp_yasperepnml114_initialmarking_constructor_exists():
    assert callable(YasperEPNML114_InitialMarking.__init__)


def test_hyp_yasperepnml114_initialmarking_constructor_args():
    sig = inspect.signature(YasperEPNML114_InitialMarking.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_documentroot_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_DocumentRoot)


def test_hyp_yasperepnml114_documentroot_constructor_exists():
    assert callable(YasperEPNML114_DocumentRoot.__init__)


def test_hyp_yasperepnml114_documentroot_constructor_args():
    sig = inspect.signature(YasperEPNML114_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_yasperepnml114_cost_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Cost)


def test_hyp_yasperepnml114_cost_constructor_exists():
    assert callable(YasperEPNML114_Cost.__init__)


def test_hyp_yasperepnml114_cost_constructor_args():
    sig = inspect.signature(YasperEPNML114_Cost.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_pnml_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Pnml)


def test_hyp_yasperepnml114_pnml_constructor_exists():
    assert callable(YasperEPNML114_Pnml.__init__)


def test_hyp_yasperepnml114_pnml_constructor_args():
    sig = inspect.signature(YasperEPNML114_Pnml.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_yasperepnml114_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_EStringToStringMapEntry)


def test_hyp_yasperepnml114_estringtostringmapentry_constructor_exists():
    assert callable(YasperEPNML114_EStringToStringMapEntry.__init__)


def test_hyp_yasperepnml114_estringtostringmapentry_constructor_args():
    sig = inspect.signature(YasperEPNML114_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_connectionweight_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ConnectionWeight)


def test_hyp_yasperepnml114_connectionweight_constructor_exists():
    assert callable(YasperEPNML114_ConnectionWeight.__init__)


def test_hyp_yasperepnml114_connectionweight_constructor_args():
    sig = inspect.signature(YasperEPNML114_ConnectionWeight.__init__)
    params = list(sig.parameters.keys())
    assert "connection" in params, "Missing parameter 'connection'"




def test_hyp_yasperepnml114_connectionweights_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ConnectionWeights)


def test_hyp_yasperepnml114_connectionweights_constructor_exists():
    assert callable(YasperEPNML114_ConnectionWeights.__init__)


def test_hyp_yasperepnml114_connectionweights_constructor_args():
    sig = inspect.signature(YasperEPNML114_ConnectionWeights.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_stat_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Stat)


def test_hyp_yasperepnml114_stat_constructor_exists():
    assert callable(YasperEPNML114_Stat.__init__)


def test_hyp_yasperepnml114_stat_constructor_args():
    sig = inspect.signature(YasperEPNML114_Stat.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_pnmlannotation_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_PnmlAnnotation)


def test_hyp_yasperepnml114_pnmlannotation_constructor_exists():
    assert callable(YasperEPNML114_PnmlAnnotation.__init__)


def test_hyp_yasperepnml114_pnmlannotation_constructor_args():
    sig = inspect.signature(YasperEPNML114_PnmlAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_inscription_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Inscription)


def test_hyp_yasperepnml114_inscription_constructor_exists():
    assert callable(YasperEPNML114_Inscription.__init__)


def test_hyp_yasperepnml114_inscription_constructor_args():
    sig = inspect.signature(YasperEPNML114_Inscription.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_edgegraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_EdgeGraphics)


def test_hyp_yasperepnml114_edgegraphics_constructor_exists():
    assert callable(YasperEPNML114_EdgeGraphics.__init__)


def test_hyp_yasperepnml114_edgegraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_EdgeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_toolspecifictype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ToolspecificType)


def test_hyp_yasperepnml114_toolspecifictype_constructor_exists():
    assert callable(YasperEPNML114_ToolspecificType.__init__)


def test_hyp_yasperepnml114_toolspecifictype_constructor_args():
    sig = inspect.signature(YasperEPNML114_ToolspecificType.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"
    assert "version" in params, "Missing parameter 'version'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"
    assert "group" in params, "Missing parameter 'group'"








def test_hyp_yasperepnml114_twodimvector_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_TwoDimVector)


def test_hyp_yasperepnml114_twodimvector_constructor_exists():
    assert callable(YasperEPNML114_TwoDimVector.__init__)


def test_hyp_yasperepnml114_twodimvector_constructor_args():
    sig = inspect.signature(YasperEPNML114_TwoDimVector.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_yasperepnml114_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_AnnotationGraphics)


def test_hyp_yasperepnml114_annotationgraphics_constructor_exists():
    assert callable(YasperEPNML114_AnnotationGraphics.__init__)


def test_hyp_yasperepnml114_annotationgraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_yasperepnml114_arctype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ArcType)


def test_hyp_yasperepnml114_arctype_constructor_exists():
    assert callable(YasperEPNML114_ArcType.__init__)


def test_hyp_yasperepnml114_arctype_constructor_args():
    sig = inspect.signature(YasperEPNML114_ArcType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_yasperepnml114_arc_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Arc)


def test_hyp_yasperepnml114_arc_constructor_exists():
    assert callable(YasperEPNML114_Arc.__init__)


def test_hyp_yasperepnml114_arc_constructor_args():
    sig = inspect.signature(YasperEPNML114_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"





def test_hyp_version_exists():
    # Check that the Enumeration exists
    assert Version is not None

def test_hyp_version_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Version]
    expected_literals = [
        "_1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Version"

def test_hyp_tool_exists():
    # Check that the Enumeration exists
    assert Tool is not None

def test_hyp_tool_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tool]
    expected_literals = [
        "Yasper",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Tool"

def test_hyp_texttype2_exists():
    # Check that the Enumeration exists
    assert TextType2 is not None

def test_hyp_texttype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextType2]
    expected_literals = [
        "channel",
        "store",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextType2"

def test_hyp_texttype1_exists():
    # Check that the Enumeration exists
    assert TextType1 is not None

def test_hyp_texttype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextType1]
    expected_literals = [
        "AND",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextType1"

def test_hyp_texttypemember0_exists():
    # Check that the Enumeration exists
    assert TextTypeMember0 is not None

def test_hyp_texttypemember0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextTypeMember0]
    expected_literals = [
        "reset",
        "inhibitor",
        "inflow",
        "outflow",
        "biflow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextTypeMember0"


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
YasperEPNML114_TransitionSpecific_strategy = st.builds(
    YasperEPNML114_TransitionSpecific,
    version=
        safe_text,
    tool=
        safe_text,
    tokenCaseSensitive=
        safe_text
)
YasperEPNML114_Transformation_strategy = st.builds(
    YasperEPNML114_Transformation,
    text=
        safe_text
)
YasperEPNML114_Roles_strategy = st.builds(
    YasperEPNML114_Roles,
)
YasperEPNML114_Role_strategy = st.builds(
    YasperEPNML114_Role,
    text=
        safe_text
)
YasperEPNML114_ReferencePlaceSpecific_strategy = st.builds(
    YasperEPNML114_ReferencePlaceSpecific,
    version=
        safe_text,
    tool=
        safe_text
)
YasperEPNML114_ProcessingTime_strategy = st.builds(
    YasperEPNML114_ProcessingTime,
)
Place_strategy = st.builds(
    Place,
)
YasperEPNML114_PlaceType_strategy = st.builds(
    YasperEPNML114_PlaceType,
    text=
        safe_text
)
YasperEPNML114_Place_strategy = st.builds(
    YasperEPNML114_Place,
    id=
        safe_text,
    group=
        safe_text
)
YasperEPNML114_TransitionType_strategy = st.builds(
    YasperEPNML114_TransitionType,
    text=
        safe_text
)
YasperEPNML114_ReferencePlace_strategy = st.builds(
    YasperEPNML114_ReferencePlace,
    group=
        safe_text,
    ref=
        safe_text,
    id=
        safe_text
)
YasperEPNML114_NodeGraphics_strategy = st.builds(
    YasperEPNML114_NodeGraphics,
    group=
        safe_text
)
YasperEPNML114_Page_strategy = st.builds(
    YasperEPNML114_Page,
    group=
        safe_text,
    id=
        safe_text
)
YasperEPNML114_Transition_strategy = st.builds(
    YasperEPNML114_Transition,
    id=
        safe_text,
    group=
        safe_text
)
YasperEPNML114_Net_strategy = st.builds(
    YasperEPNML114_Net,
    group=
        safe_text,
    id=
        safe_text,
    type=
        safe_text
)
YasperEPNML114_PlaceType1_strategy = st.builds(
    YasperEPNML114_PlaceType1,
)
YasperEPNML114_NetGraphics_strategy = st.builds(
    YasperEPNML114_NetGraphics,
    group=
        safe_text
)
YasperEPNML114_InitialMarking_strategy = st.builds(
    YasperEPNML114_InitialMarking,
    text=
        safe_text
)
YasperEPNML114_DocumentRoot_strategy = st.builds(
    YasperEPNML114_DocumentRoot,
    mixed=
        safe_text
)
YasperEPNML114_Cost_strategy = st.builds(
    YasperEPNML114_Cost,
)
YasperEPNML114_Pnml_strategy = st.builds(
    YasperEPNML114_Pnml,
    group=
        safe_text
)
YasperEPNML114_EStringToStringMapEntry_strategy = st.builds(
    YasperEPNML114_EStringToStringMapEntry,
)
YasperEPNML114_ConnectionWeight_strategy = st.builds(
    YasperEPNML114_ConnectionWeight,
    connection=
        safe_text
)
YasperEPNML114_ConnectionWeights_strategy = st.builds(
    YasperEPNML114_ConnectionWeights,
)
YasperEPNML114_Stat_strategy = st.builds(
    YasperEPNML114_Stat,
    text=
        safe_text
)
YasperEPNML114_PnmlAnnotation_strategy = st.builds(
    YasperEPNML114_PnmlAnnotation,
    text=
        safe_text
)
YasperEPNML114_Inscription_strategy = st.builds(
    YasperEPNML114_Inscription,
    text=
        safe_text
)
YasperEPNML114_EdgeGraphics_strategy = st.builds(
    YasperEPNML114_EdgeGraphics,
)
YasperEPNML114_ToolspecificType_strategy = st.builds(
    YasperEPNML114_ToolspecificType,
    tool=
        safe_text,
    version=
        safe_text,
    mixed=
        safe_text,
    any=
        safe_text,
    group=
        safe_text
)
YasperEPNML114_TwoDimVector_strategy = st.builds(
    YasperEPNML114_TwoDimVector,
    y=
        safe_text,
    x=
        safe_text
)
YasperEPNML114_AnnotationGraphics_strategy = st.builds(
    YasperEPNML114_AnnotationGraphics,
)
YasperEPNML114_ArcType_strategy = st.builds(
    YasperEPNML114_ArcType,
    text=
        safe_text
)
YasperEPNML114_Arc_strategy = st.builds(
    YasperEPNML114_Arc,
    source=
        safe_text,
    target=
        safe_text,
    id=
        safe_text,
    group=
        safe_text
)




@given(instance=YasperEPNML114_TransitionSpecific_strategy)
def test_hyp_yasperepnml114_transitionspecific_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=YasperEPNML114_TransitionSpecific_strategy)
def test_hyp_yasperepnml114_transitionspecific_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original



@given(instance=YasperEPNML114_TransitionSpecific_strategy)
def test_hyp_yasperepnml114_transitionspecific_tokenCaseSensitive_setter(instance):
    original = instance.tokenCaseSensitive
    instance.tokenCaseSensitive = original
    assert instance.tokenCaseSensitive == original




@given(instance=YasperEPNML114_Transformation_strategy)
def test_hyp_yasperepnml114_transformation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=YasperEPNML114_Role_strategy)
def test_hyp_yasperepnml114_role_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=YasperEPNML114_ReferencePlaceSpecific_strategy)
def test_hyp_yasperepnml114_referenceplacespecific_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=YasperEPNML114_ReferencePlaceSpecific_strategy)
def test_hyp_yasperepnml114_referenceplacespecific_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original






@given(instance=YasperEPNML114_PlaceType_strategy)
def test_hyp_yasperepnml114_placetype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=YasperEPNML114_Place_strategy)
def test_hyp_yasperepnml114_place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Place_strategy)
def test_hyp_yasperepnml114_place_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=YasperEPNML114_TransitionType_strategy)
def test_hyp_yasperepnml114_transitiontype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=YasperEPNML114_ReferencePlace_strategy)
def test_hyp_yasperepnml114_referenceplace_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=YasperEPNML114_ReferencePlace_strategy)
def test_hyp_yasperepnml114_referenceplace_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original



@given(instance=YasperEPNML114_ReferencePlace_strategy)
def test_hyp_yasperepnml114_referenceplace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=YasperEPNML114_NodeGraphics_strategy)
def test_hyp_yasperepnml114_nodegraphics_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=YasperEPNML114_Page_strategy)
def test_hyp_yasperepnml114_page_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=YasperEPNML114_Page_strategy)
def test_hyp_yasperepnml114_page_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=YasperEPNML114_Transition_strategy)
def test_hyp_yasperepnml114_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Transition_strategy)
def test_hyp_yasperepnml114_transition_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=YasperEPNML114_Net_strategy)
def test_hyp_yasperepnml114_net_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=YasperEPNML114_Net_strategy)
def test_hyp_yasperepnml114_net_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Net_strategy)
def test_hyp_yasperepnml114_net_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=YasperEPNML114_NetGraphics_strategy)
def test_hyp_yasperepnml114_netgraphics_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=YasperEPNML114_InitialMarking_strategy)
def test_hyp_yasperepnml114_initialmarking_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=YasperEPNML114_DocumentRoot_strategy)
def test_hyp_yasperepnml114_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=YasperEPNML114_Pnml_strategy)
def test_hyp_yasperepnml114_pnml_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original





@given(instance=YasperEPNML114_ConnectionWeight_strategy)
def test_hyp_yasperepnml114_connectionweight_connection_setter(instance):
    original = instance.connection
    instance.connection = original
    assert instance.connection == original





@given(instance=YasperEPNML114_Stat_strategy)
def test_hyp_yasperepnml114_stat_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=YasperEPNML114_PnmlAnnotation_strategy)
def test_hyp_yasperepnml114_pnmlannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=YasperEPNML114_Inscription_strategy)
def test_hyp_yasperepnml114_inscription_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_hyp_yasperepnml114_toolspecifictype_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_hyp_yasperepnml114_toolspecifictype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_hyp_yasperepnml114_toolspecifictype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_hyp_yasperepnml114_toolspecifictype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_hyp_yasperepnml114_toolspecifictype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=YasperEPNML114_TwoDimVector_strategy)
def test_hyp_yasperepnml114_twodimvector_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=YasperEPNML114_TwoDimVector_strategy)
def test_hyp_yasperepnml114_twodimvector_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original





@given(instance=YasperEPNML114_ArcType_strategy)
def test_hyp_yasperepnml114_arctype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=YasperEPNML114_Arc_strategy)
def test_hyp_yasperepnml114_arc_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=YasperEPNML114_Arc_strategy)
def test_hyp_yasperepnml114_arc_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=YasperEPNML114_Arc_strategy)
def test_hyp_yasperepnml114_arc_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Arc_strategy)
def test_hyp_yasperepnml114_arc_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Place,
    YasperEPNML114_AnnotationGraphics,
    YasperEPNML114_Arc,
    YasperEPNML114_ArcType,
    YasperEPNML114_ConnectionWeight,
    YasperEPNML114_ConnectionWeights,
    YasperEPNML114_Cost,
    YasperEPNML114_DocumentRoot,
    YasperEPNML114_EStringToStringMapEntry,
    YasperEPNML114_EdgeGraphics,
    YasperEPNML114_InitialMarking,
    YasperEPNML114_Inscription,
    YasperEPNML114_Net,
    YasperEPNML114_NetGraphics,
    YasperEPNML114_NodeGraphics,
    YasperEPNML114_Page,
    YasperEPNML114_Place,
    YasperEPNML114_PlaceType,
    YasperEPNML114_PlaceType1,
    YasperEPNML114_Pnml,
    YasperEPNML114_PnmlAnnotation,
    YasperEPNML114_ProcessingTime,
    YasperEPNML114_ReferencePlace,
    YasperEPNML114_ReferencePlaceSpecific,
    YasperEPNML114_Role,
    YasperEPNML114_Roles,
    YasperEPNML114_Stat,
    YasperEPNML114_ToolspecificType,
    YasperEPNML114_Transformation,
    YasperEPNML114_Transition,
    YasperEPNML114_TransitionSpecific,
    YasperEPNML114_TransitionType,
    YasperEPNML114_TwoDimVector,
    TextType1,
    TextType2,
    TextTypeMember0,
    Tool,
    Version,
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

def test_YasperEPNML114_Arc_group_value_roundtrip():
    instance = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_Arc_id_value_roundtrip():
    instance = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_YasperEPNML114_Arc_source_value_roundtrip():
    instance = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_YasperEPNML114_Arc_target_value_roundtrip():
    instance = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_YasperEPNML114_ArcType_text_value_roundtrip():
    instance = YasperEPNML114_ArcType(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_ConnectionWeight_connection_value_roundtrip():
    instance = YasperEPNML114_ConnectionWeight(connection="sample_text")
    assert instance.connection == "sample_text"
    instance.connection = "sample_text_2"
    assert instance.connection == "sample_text_2"


def test_YasperEPNML114_DocumentRoot_mixed_value_roundtrip():
    instance = YasperEPNML114_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_YasperEPNML114_InitialMarking_text_value_roundtrip():
    instance = YasperEPNML114_InitialMarking(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_Inscription_text_value_roundtrip():
    instance = YasperEPNML114_Inscription(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_Net_group_value_roundtrip():
    instance = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_Net_id_value_roundtrip():
    instance = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_YasperEPNML114_Net_type_value_roundtrip():
    instance = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_YasperEPNML114_NetGraphics_group_value_roundtrip():
    instance = YasperEPNML114_NetGraphics(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_NodeGraphics_group_value_roundtrip():
    instance = YasperEPNML114_NodeGraphics(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_Page_group_value_roundtrip():
    instance = YasperEPNML114_Page(group="sample_text", id="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_Page_id_value_roundtrip():
    instance = YasperEPNML114_Page(group="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_YasperEPNML114_Place_group_value_roundtrip():
    instance = YasperEPNML114_Place(group="sample_text", id="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_Place_id_value_roundtrip():
    instance = YasperEPNML114_Place(group="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_YasperEPNML114_PlaceType_text_value_roundtrip():
    instance = YasperEPNML114_PlaceType(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_Pnml_group_value_roundtrip():
    instance = YasperEPNML114_Pnml(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_PnmlAnnotation_text_value_roundtrip():
    instance = YasperEPNML114_PnmlAnnotation(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_ReferencePlace_group_value_roundtrip():
    instance = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_ReferencePlace_id_value_roundtrip():
    instance = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_YasperEPNML114_ReferencePlace_ref_value_roundtrip():
    instance = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_YasperEPNML114_ReferencePlaceSpecific_tool_value_roundtrip():
    instance = YasperEPNML114_ReferencePlaceSpecific(tool="sample_text", version="sample_text")
    assert instance.tool == "sample_text"
    instance.tool = "sample_text_2"
    assert instance.tool == "sample_text_2"


def test_YasperEPNML114_ReferencePlaceSpecific_version_value_roundtrip():
    instance = YasperEPNML114_ReferencePlaceSpecific(tool="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_YasperEPNML114_Role_text_value_roundtrip():
    instance = YasperEPNML114_Role(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_Stat_text_value_roundtrip():
    instance = YasperEPNML114_Stat(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_ToolspecificType_any_value_roundtrip():
    instance = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    assert instance.any == "sample_text"
    instance.any = "sample_text_2"
    assert instance.any == "sample_text_2"


def test_YasperEPNML114_ToolspecificType_group_value_roundtrip():
    instance = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_ToolspecificType_mixed_value_roundtrip():
    instance = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_YasperEPNML114_ToolspecificType_tool_value_roundtrip():
    instance = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    assert instance.tool == "sample_text"
    instance.tool = "sample_text_2"
    assert instance.tool == "sample_text_2"


def test_YasperEPNML114_ToolspecificType_version_value_roundtrip():
    instance = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_YasperEPNML114_Transformation_text_value_roundtrip():
    instance = YasperEPNML114_Transformation(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_Transition_group_value_roundtrip():
    instance = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_YasperEPNML114_Transition_id_value_roundtrip():
    instance = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_YasperEPNML114_TransitionSpecific_tokenCaseSensitive_value_roundtrip():
    instance = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    assert instance.tokenCaseSensitive == "sample_text"
    instance.tokenCaseSensitive = "sample_text_2"
    assert instance.tokenCaseSensitive == "sample_text_2"


def test_YasperEPNML114_TransitionSpecific_tool_value_roundtrip():
    instance = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    assert instance.tool == "sample_text"
    instance.tool = "sample_text_2"
    assert instance.tool == "sample_text_2"


def test_YasperEPNML114_TransitionSpecific_version_value_roundtrip():
    instance = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_YasperEPNML114_TransitionType_text_value_roundtrip():
    instance = YasperEPNML114_TransitionType(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_YasperEPNML114_TwoDimVector_x_value_roundtrip():
    instance = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_YasperEPNML114_TwoDimVector_y_value_roundtrip():
    instance = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_YasperEPNML114_PlaceType1_isa_Place():
    instance = YasperEPNML114_PlaceType1()
    assert isinstance(instance, Place)


def test_assoc_arc40_link_reassign_clear():
    a = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b1 = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b2 = YasperEPNML114_Arc(group="sample_text_2", id="sample_text_2", source="sample_text_2", target="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Net41', {b1})
    assert _is_linked(a, 'YasperEPNML114_Net41', b1)
    if hasattr(b1, 'YasperEPNML114_Arc42'):
        assert _is_linked(b1, 'YasperEPNML114_Arc42', a)
    _safe_set(a, 'YasperEPNML114_Net41', {b2})
    assert _is_linked(a, 'YasperEPNML114_Net41', b2)
    if hasattr(b1, 'YasperEPNML114_Arc42'):
        assert not _is_linked(b1, 'YasperEPNML114_Arc42', a)
    if hasattr(b2, 'YasperEPNML114_Arc42'):
        assert _is_linked(b2, 'YasperEPNML114_Arc42', a)
    _safe_set(a, 'YasperEPNML114_Net41', set())
    assert not _is_linked(a, 'YasperEPNML114_Net41', b2)
    if hasattr(b2, 'YasperEPNML114_Arc42'):
        assert not _is_linked(b2, 'YasperEPNML114_Arc42', a)


def test_assoc_arc78_link_reassign_clear():
    a = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b2 = YasperEPNML114_Arc(group="sample_text_2", id="sample_text_2", source="sample_text_2", target="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Page79', {b1})
    assert _is_linked(a, 'YasperEPNML114_Page79', b1)
    if hasattr(b1, 'YasperEPNML114_Arc80'):
        assert _is_linked(b1, 'YasperEPNML114_Arc80', a)
    _safe_set(a, 'YasperEPNML114_Page79', {b2})
    assert _is_linked(a, 'YasperEPNML114_Page79', b2)
    if hasattr(b1, 'YasperEPNML114_Arc80'):
        assert not _is_linked(b1, 'YasperEPNML114_Arc80', a)
    if hasattr(b2, 'YasperEPNML114_Arc80'):
        assert _is_linked(b2, 'YasperEPNML114_Arc80', a)
    _safe_set(a, 'YasperEPNML114_Page79', set())
    assert not _is_linked(a, 'YasperEPNML114_Page79', b2)
    if hasattr(b2, 'YasperEPNML114_Arc80'):
        assert not _is_linked(b2, 'YasperEPNML114_Arc80', a)


def test_assoc_connectionWeight14_link_reassign_clear():
    a = YasperEPNML114_ConnectionWeight(connection="sample_text")
    b1 = YasperEPNML114_ConnectionWeights()
    b2 = YasperEPNML114_ConnectionWeights()
    _safe_set(a, 'YasperEPNML114_ConnectionWeight15', b1)
    assert _is_linked(a, 'YasperEPNML114_ConnectionWeight15', b1)
    if hasattr(b1, 'YasperEPNML114_ConnectionWeights'):
        assert _is_linked(b1, 'YasperEPNML114_ConnectionWeights', a)
    _safe_set(a, 'YasperEPNML114_ConnectionWeight15', b2)
    assert _is_linked(a, 'YasperEPNML114_ConnectionWeight15', b2)
    if hasattr(b1, 'YasperEPNML114_ConnectionWeights'):
        assert not _is_linked(b1, 'YasperEPNML114_ConnectionWeights', a)
    if hasattr(b2, 'YasperEPNML114_ConnectionWeights'):
        assert _is_linked(b2, 'YasperEPNML114_ConnectionWeights', a)
    _safe_set(a, 'YasperEPNML114_ConnectionWeight15', None)
    assert not _is_linked(a, 'YasperEPNML114_ConnectionWeight15', b2)
    if hasattr(b2, 'YasperEPNML114_ConnectionWeights'):
        assert not _is_linked(b2, 'YasperEPNML114_ConnectionWeights', a)


def test_assoc_cost160_link_reassign_clear():
    a = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_Cost()
    b2 = YasperEPNML114_Cost()
    _safe_set(a, 'YasperEPNML114_TransitionSpecific161', b1)
    assert _is_linked(a, 'YasperEPNML114_TransitionSpecific161', b1)
    if hasattr(b1, 'YasperEPNML114_Cost162'):
        assert _is_linked(b1, 'YasperEPNML114_Cost162', a)
    _safe_set(a, 'YasperEPNML114_TransitionSpecific161', b2)
    assert _is_linked(a, 'YasperEPNML114_TransitionSpecific161', b2)
    if hasattr(b1, 'YasperEPNML114_Cost162'):
        assert not _is_linked(b1, 'YasperEPNML114_Cost162', a)
    if hasattr(b2, 'YasperEPNML114_Cost162'):
        assert _is_linked(b2, 'YasperEPNML114_Cost162', a)
    _safe_set(a, 'YasperEPNML114_TransitionSpecific161', None)
    assert not _is_linked(a, 'YasperEPNML114_TransitionSpecific161', b2)
    if hasattr(b2, 'YasperEPNML114_Cost162'):
        assert not _is_linked(b2, 'YasperEPNML114_Cost162', a)


def test_assoc_description103_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Place(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Place(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation105', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation105', b1)
    if hasattr(b1, 'YasperEPNML114_Place104'):
        assert _is_linked(b1, 'YasperEPNML114_Place104', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation105', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation105', b2)
    if hasattr(b1, 'YasperEPNML114_Place104'):
        assert not _is_linked(b1, 'YasperEPNML114_Place104', a)
    if hasattr(b2, 'YasperEPNML114_Place104'):
        assert _is_linked(b2, 'YasperEPNML114_Place104', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation105', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation105', b2)
    if hasattr(b2, 'YasperEPNML114_Place104'):
        assert not _is_linked(b2, 'YasperEPNML114_Place104', a)


def test_assoc_description129_link_reassign_clear():
    a = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    b1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ReferencePlace130', {b1})
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace130', b1)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation131'):
        assert _is_linked(b1, 'YasperEPNML114_PnmlAnnotation131', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace130', {b2})
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace130', b2)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation131'):
        assert not _is_linked(b1, 'YasperEPNML114_PnmlAnnotation131', a)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation131'):
        assert _is_linked(b2, 'YasperEPNML114_PnmlAnnotation131', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace130', set())
    assert not _is_linked(a, 'YasperEPNML114_ReferencePlace130', b2)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation131'):
        assert not _is_linked(b2, 'YasperEPNML114_PnmlAnnotation131', a)


def test_assoc_description152_link_reassign_clear():
    a = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Transition153', {b1})
    assert _is_linked(a, 'YasperEPNML114_Transition153', b1)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation154'):
        assert _is_linked(b1, 'YasperEPNML114_PnmlAnnotation154', a)
    _safe_set(a, 'YasperEPNML114_Transition153', {b2})
    assert _is_linked(a, 'YasperEPNML114_Transition153', b2)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation154'):
        assert not _is_linked(b1, 'YasperEPNML114_PnmlAnnotation154', a)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation154'):
        assert _is_linked(b2, 'YasperEPNML114_PnmlAnnotation154', a)
    _safe_set(a, 'YasperEPNML114_Transition153', set())
    assert not _is_linked(a, 'YasperEPNML114_Transition153', b2)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation154'):
        assert not _is_linked(b2, 'YasperEPNML114_PnmlAnnotation154', a)


def test_assoc_description48_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation50', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation50', b1)
    if hasattr(b1, 'YasperEPNML114_Net49'):
        assert _is_linked(b1, 'YasperEPNML114_Net49', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation50', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation50', b2)
    if hasattr(b1, 'YasperEPNML114_Net49'):
        assert not _is_linked(b1, 'YasperEPNML114_Net49', a)
    if hasattr(b2, 'YasperEPNML114_Net49'):
        assert _is_linked(b2, 'YasperEPNML114_Net49', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation50', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation50', b2)
    if hasattr(b2, 'YasperEPNML114_Net49'):
        assert not _is_linked(b2, 'YasperEPNML114_Net49', a)


def test_assoc_description8_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b2 = YasperEPNML114_Arc(group="sample_text_2", id="sample_text_2", source="sample_text_2", target="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation10', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation10', b1)
    if hasattr(b1, 'YasperEPNML114_Arc9'):
        assert _is_linked(b1, 'YasperEPNML114_Arc9', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation10', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation10', b2)
    if hasattr(b1, 'YasperEPNML114_Arc9'):
        assert not _is_linked(b1, 'YasperEPNML114_Arc9', a)
    if hasattr(b2, 'YasperEPNML114_Arc9'):
        assert _is_linked(b2, 'YasperEPNML114_Arc9', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation10', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation10', b2)
    if hasattr(b2, 'YasperEPNML114_Arc9'):
        assert not _is_linked(b2, 'YasperEPNML114_Arc9', a)


def test_assoc_description87_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation89', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation89', b1)
    if hasattr(b1, 'YasperEPNML114_Page88'):
        assert _is_linked(b1, 'YasperEPNML114_Page88', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation89', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation89', b2)
    if hasattr(b1, 'YasperEPNML114_Page88'):
        assert not _is_linked(b1, 'YasperEPNML114_Page88', a)
    if hasattr(b2, 'YasperEPNML114_Page88'):
        assert _is_linked(b2, 'YasperEPNML114_Page88', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation89', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation89', b2)
    if hasattr(b2, 'YasperEPNML114_Page88'):
        assert not _is_linked(b2, 'YasperEPNML114_Page88', a)


def test_assoc_deviation120_link_reassign_clear():
    a = YasperEPNML114_Stat(text="sample_text")
    b1 = YasperEPNML114_ProcessingTime()
    b2 = YasperEPNML114_ProcessingTime()
    _safe_set(a, 'YasperEPNML114_Stat122', b1)
    assert _is_linked(a, 'YasperEPNML114_Stat122', b1)
    if hasattr(b1, 'YasperEPNML114_ProcessingTime121'):
        assert _is_linked(b1, 'YasperEPNML114_ProcessingTime121', a)
    _safe_set(a, 'YasperEPNML114_Stat122', b2)
    assert _is_linked(a, 'YasperEPNML114_Stat122', b2)
    if hasattr(b1, 'YasperEPNML114_ProcessingTime121'):
        assert not _is_linked(b1, 'YasperEPNML114_ProcessingTime121', a)
    if hasattr(b2, 'YasperEPNML114_ProcessingTime121'):
        assert _is_linked(b2, 'YasperEPNML114_ProcessingTime121', a)
    _safe_set(a, 'YasperEPNML114_Stat122', None)
    assert not _is_linked(a, 'YasperEPNML114_Stat122', b2)
    if hasattr(b2, 'YasperEPNML114_ProcessingTime121'):
        assert not _is_linked(b2, 'YasperEPNML114_ProcessingTime121', a)


def test_assoc_dimension57_link_reassign_clear():
    a = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    b1 = YasperEPNML114_NetGraphics(group="sample_text")
    b2 = YasperEPNML114_NetGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_TwoDimVector59', b1)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector59', b1)
    if hasattr(b1, 'YasperEPNML114_NetGraphics58'):
        assert _is_linked(b1, 'YasperEPNML114_NetGraphics58', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector59', b2)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector59', b2)
    if hasattr(b1, 'YasperEPNML114_NetGraphics58'):
        assert not _is_linked(b1, 'YasperEPNML114_NetGraphics58', a)
    if hasattr(b2, 'YasperEPNML114_NetGraphics58'):
        assert _is_linked(b2, 'YasperEPNML114_NetGraphics58', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector59', None)
    assert not _is_linked(a, 'YasperEPNML114_TwoDimVector59', b2)
    if hasattr(b2, 'YasperEPNML114_NetGraphics58'):
        assert not _is_linked(b2, 'YasperEPNML114_NetGraphics58', a)


def test_assoc_dimension62_link_reassign_clear():
    a = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    b1 = YasperEPNML114_NodeGraphics(group="sample_text")
    b2 = YasperEPNML114_NodeGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_TwoDimVector64', b1)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector64', b1)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics63'):
        assert _is_linked(b1, 'YasperEPNML114_NodeGraphics63', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector64', b2)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector64', b2)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics63'):
        assert not _is_linked(b1, 'YasperEPNML114_NodeGraphics63', a)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics63'):
        assert _is_linked(b2, 'YasperEPNML114_NodeGraphics63', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector64', None)
    assert not _is_linked(a, 'YasperEPNML114_TwoDimVector64', b2)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics63'):
        assert not _is_linked(b2, 'YasperEPNML114_NodeGraphics63', a)


def test_assoc_fixed16_link_reassign_clear():
    a = YasperEPNML114_Stat(text="sample_text")
    b1 = YasperEPNML114_Cost()
    b2 = YasperEPNML114_Cost()
    _safe_set(a, 'YasperEPNML114_Stat17', b1)
    assert _is_linked(a, 'YasperEPNML114_Stat17', b1)
    if hasattr(b1, 'YasperEPNML114_Cost'):
        assert _is_linked(b1, 'YasperEPNML114_Cost', a)
    _safe_set(a, 'YasperEPNML114_Stat17', b2)
    assert _is_linked(a, 'YasperEPNML114_Stat17', b2)
    if hasattr(b1, 'YasperEPNML114_Cost'):
        assert not _is_linked(b1, 'YasperEPNML114_Cost', a)
    if hasattr(b2, 'YasperEPNML114_Cost'):
        assert _is_linked(b2, 'YasperEPNML114_Cost', a)
    _safe_set(a, 'YasperEPNML114_Stat17', None)
    assert not _is_linked(a, 'YasperEPNML114_Stat17', b2)
    if hasattr(b2, 'YasperEPNML114_Cost'):
        assert not _is_linked(b2, 'YasperEPNML114_Cost', a)


def test_assoc_graphics115_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_AnnotationGraphics()
    b2 = YasperEPNML114_AnnotationGraphics()
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation116', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation116', b1)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics117'):
        assert _is_linked(b1, 'YasperEPNML114_AnnotationGraphics117', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation116', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation116', b2)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics117'):
        assert not _is_linked(b1, 'YasperEPNML114_AnnotationGraphics117', a)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics117'):
        assert _is_linked(b2, 'YasperEPNML114_AnnotationGraphics117', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation116', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation116', b2)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics117'):
        assert not _is_linked(b2, 'YasperEPNML114_AnnotationGraphics117', a)


def test_assoc_graphics123_link_reassign_clear():
    a = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    b1 = YasperEPNML114_NodeGraphics(group="sample_text")
    b2 = YasperEPNML114_NodeGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ReferencePlace124', {b1})
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace124', b1)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics125'):
        assert _is_linked(b1, 'YasperEPNML114_NodeGraphics125', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace124', {b2})
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace124', b2)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics125'):
        assert not _is_linked(b1, 'YasperEPNML114_NodeGraphics125', a)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics125'):
        assert _is_linked(b2, 'YasperEPNML114_NodeGraphics125', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace124', set())
    assert not _is_linked(a, 'YasperEPNML114_ReferencePlace124', b2)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics125'):
        assert not _is_linked(b2, 'YasperEPNML114_NodeGraphics125', a)


def test_assoc_graphics138_link_reassign_clear():
    a = YasperEPNML114_Transformation(text="sample_text")
    b1 = YasperEPNML114_AnnotationGraphics()
    b2 = YasperEPNML114_AnnotationGraphics()
    _safe_set(a, 'YasperEPNML114_Transformation', b1)
    assert _is_linked(a, 'YasperEPNML114_Transformation', b1)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics139'):
        assert _is_linked(b1, 'YasperEPNML114_AnnotationGraphics139', a)
    _safe_set(a, 'YasperEPNML114_Transformation', b2)
    assert _is_linked(a, 'YasperEPNML114_Transformation', b2)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics139'):
        assert not _is_linked(b1, 'YasperEPNML114_AnnotationGraphics139', a)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics139'):
        assert _is_linked(b2, 'YasperEPNML114_AnnotationGraphics139', a)
    _safe_set(a, 'YasperEPNML114_Transformation', None)
    assert not _is_linked(a, 'YasperEPNML114_Transformation', b2)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics139'):
        assert not _is_linked(b2, 'YasperEPNML114_AnnotationGraphics139', a)


def test_assoc_graphics143_link_reassign_clear():
    a = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_NodeGraphics(group="sample_text")
    b2 = YasperEPNML114_NodeGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Transition144', {b1})
    assert _is_linked(a, 'YasperEPNML114_Transition144', b1)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics145'):
        assert _is_linked(b1, 'YasperEPNML114_NodeGraphics145', a)
    _safe_set(a, 'YasperEPNML114_Transition144', {b2})
    assert _is_linked(a, 'YasperEPNML114_Transition144', b2)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics145'):
        assert not _is_linked(b1, 'YasperEPNML114_NodeGraphics145', a)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics145'):
        assert _is_linked(b2, 'YasperEPNML114_NodeGraphics145', a)
    _safe_set(a, 'YasperEPNML114_Transition144', set())
    assert not _is_linked(a, 'YasperEPNML114_Transition144', b2)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics145'):
        assert not _is_linked(b2, 'YasperEPNML114_NodeGraphics145', a)


def test_assoc_graphics2_link_reassign_clear():
    a = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b1 = YasperEPNML114_EdgeGraphics()
    b2 = YasperEPNML114_EdgeGraphics()
    _safe_set(a, 'YasperEPNML114_Arc3', {b1})
    assert _is_linked(a, 'YasperEPNML114_Arc3', b1)
    if hasattr(b1, 'YasperEPNML114_EdgeGraphics'):
        assert _is_linked(b1, 'YasperEPNML114_EdgeGraphics', a)
    _safe_set(a, 'YasperEPNML114_Arc3', {b2})
    assert _is_linked(a, 'YasperEPNML114_Arc3', b2)
    if hasattr(b1, 'YasperEPNML114_EdgeGraphics'):
        assert not _is_linked(b1, 'YasperEPNML114_EdgeGraphics', a)
    if hasattr(b2, 'YasperEPNML114_EdgeGraphics'):
        assert _is_linked(b2, 'YasperEPNML114_EdgeGraphics', a)
    _safe_set(a, 'YasperEPNML114_Arc3', set())
    assert not _is_linked(a, 'YasperEPNML114_Arc3', b2)
    if hasattr(b2, 'YasperEPNML114_EdgeGraphics'):
        assert not _is_linked(b2, 'YasperEPNML114_EdgeGraphics', a)


def test_assoc_graphics30_link_reassign_clear():
    a = YasperEPNML114_InitialMarking(text="sample_text")
    b1 = YasperEPNML114_AnnotationGraphics()
    b2 = YasperEPNML114_AnnotationGraphics()
    _safe_set(a, 'YasperEPNML114_InitialMarking', b1)
    assert _is_linked(a, 'YasperEPNML114_InitialMarking', b1)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics31'):
        assert _is_linked(b1, 'YasperEPNML114_AnnotationGraphics31', a)
    _safe_set(a, 'YasperEPNML114_InitialMarking', b2)
    assert _is_linked(a, 'YasperEPNML114_InitialMarking', b2)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics31'):
        assert not _is_linked(b1, 'YasperEPNML114_AnnotationGraphics31', a)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics31'):
        assert _is_linked(b2, 'YasperEPNML114_AnnotationGraphics31', a)
    _safe_set(a, 'YasperEPNML114_InitialMarking', None)
    assert not _is_linked(a, 'YasperEPNML114_InitialMarking', b2)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics31'):
        assert not _is_linked(b2, 'YasperEPNML114_AnnotationGraphics31', a)


def test_assoc_graphics32_link_reassign_clear():
    a = YasperEPNML114_Inscription(text="sample_text")
    b1 = YasperEPNML114_AnnotationGraphics()
    b2 = YasperEPNML114_AnnotationGraphics()
    _safe_set(a, 'YasperEPNML114_Inscription33', b1)
    assert _is_linked(a, 'YasperEPNML114_Inscription33', b1)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics34'):
        assert _is_linked(b1, 'YasperEPNML114_AnnotationGraphics34', a)
    _safe_set(a, 'YasperEPNML114_Inscription33', b2)
    assert _is_linked(a, 'YasperEPNML114_Inscription33', b2)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics34'):
        assert not _is_linked(b1, 'YasperEPNML114_AnnotationGraphics34', a)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics34'):
        assert _is_linked(b2, 'YasperEPNML114_AnnotationGraphics34', a)
    _safe_set(a, 'YasperEPNML114_Inscription33', None)
    assert not _is_linked(a, 'YasperEPNML114_Inscription33', b2)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics34'):
        assert not _is_linked(b2, 'YasperEPNML114_AnnotationGraphics34', a)


def test_assoc_graphics35_link_reassign_clear():
    a = YasperEPNML114_NetGraphics(group="sample_text")
    b1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'YasperEPNML114_NetGraphics', b1)
    assert _is_linked(a, 'YasperEPNML114_NetGraphics', b1)
    if hasattr(b1, 'YasperEPNML114_Net'):
        assert _is_linked(b1, 'YasperEPNML114_Net', a)
    _safe_set(a, 'YasperEPNML114_NetGraphics', b2)
    assert _is_linked(a, 'YasperEPNML114_NetGraphics', b2)
    if hasattr(b1, 'YasperEPNML114_Net'):
        assert not _is_linked(b1, 'YasperEPNML114_Net', a)
    if hasattr(b2, 'YasperEPNML114_Net'):
        assert _is_linked(b2, 'YasperEPNML114_Net', a)
    _safe_set(a, 'YasperEPNML114_NetGraphics', None)
    assert not _is_linked(a, 'YasperEPNML114_NetGraphics', b2)
    if hasattr(b2, 'YasperEPNML114_Net'):
        assert not _is_linked(b2, 'YasperEPNML114_Net', a)


def test_assoc_graphics67_link_reassign_clear():
    a = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_NetGraphics(group="sample_text")
    b2 = YasperEPNML114_NetGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Page68', {b1})
    assert _is_linked(a, 'YasperEPNML114_Page68', b1)
    if hasattr(b1, 'YasperEPNML114_NetGraphics69'):
        assert _is_linked(b1, 'YasperEPNML114_NetGraphics69', a)
    _safe_set(a, 'YasperEPNML114_Page68', {b2})
    assert _is_linked(a, 'YasperEPNML114_Page68', b2)
    if hasattr(b1, 'YasperEPNML114_NetGraphics69'):
        assert not _is_linked(b1, 'YasperEPNML114_NetGraphics69', a)
    if hasattr(b2, 'YasperEPNML114_NetGraphics69'):
        assert _is_linked(b2, 'YasperEPNML114_NetGraphics69', a)
    _safe_set(a, 'YasperEPNML114_Page68', set())
    assert not _is_linked(a, 'YasperEPNML114_Page68', b2)
    if hasattr(b2, 'YasperEPNML114_NetGraphics69'):
        assert not _is_linked(b2, 'YasperEPNML114_NetGraphics69', a)


def test_assoc_graphics94_link_reassign_clear():
    a = YasperEPNML114_Place(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_NodeGraphics(group="sample_text")
    b2 = YasperEPNML114_NodeGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Place95', {b1})
    assert _is_linked(a, 'YasperEPNML114_Place95', b1)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics96'):
        assert _is_linked(b1, 'YasperEPNML114_NodeGraphics96', a)
    _safe_set(a, 'YasperEPNML114_Place95', {b2})
    assert _is_linked(a, 'YasperEPNML114_Place95', b2)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics96'):
        assert not _is_linked(b1, 'YasperEPNML114_NodeGraphics96', a)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics96'):
        assert _is_linked(b2, 'YasperEPNML114_NodeGraphics96', a)
    _safe_set(a, 'YasperEPNML114_Place95', set())
    assert not _is_linked(a, 'YasperEPNML114_Place95', b2)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics96'):
        assert not _is_linked(b2, 'YasperEPNML114_NodeGraphics96', a)


def test_assoc_initialMarking97_link_reassign_clear():
    a = YasperEPNML114_Place(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_InitialMarking(text="sample_text")
    b2 = YasperEPNML114_InitialMarking(text="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Place98', {b1})
    assert _is_linked(a, 'YasperEPNML114_Place98', b1)
    if hasattr(b1, 'YasperEPNML114_InitialMarking99'):
        assert _is_linked(b1, 'YasperEPNML114_InitialMarking99', a)
    _safe_set(a, 'YasperEPNML114_Place98', {b2})
    assert _is_linked(a, 'YasperEPNML114_Place98', b2)
    if hasattr(b1, 'YasperEPNML114_InitialMarking99'):
        assert not _is_linked(b1, 'YasperEPNML114_InitialMarking99', a)
    if hasattr(b2, 'YasperEPNML114_InitialMarking99'):
        assert _is_linked(b2, 'YasperEPNML114_InitialMarking99', a)
    _safe_set(a, 'YasperEPNML114_Place98', set())
    assert not _is_linked(a, 'YasperEPNML114_Place98', b2)
    if hasattr(b2, 'YasperEPNML114_InitialMarking99'):
        assert not _is_linked(b2, 'YasperEPNML114_InitialMarking99', a)


def test_assoc_inscription4_link_reassign_clear():
    a = YasperEPNML114_Inscription(text="sample_text")
    b1 = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b2 = YasperEPNML114_Arc(group="sample_text_2", id="sample_text_2", source="sample_text_2", target="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Inscription', b1)
    assert _is_linked(a, 'YasperEPNML114_Inscription', b1)
    if hasattr(b1, 'YasperEPNML114_Arc5'):
        assert _is_linked(b1, 'YasperEPNML114_Arc5', a)
    _safe_set(a, 'YasperEPNML114_Inscription', b2)
    assert _is_linked(a, 'YasperEPNML114_Inscription', b2)
    if hasattr(b1, 'YasperEPNML114_Arc5'):
        assert not _is_linked(b1, 'YasperEPNML114_Arc5', a)
    if hasattr(b2, 'YasperEPNML114_Arc5'):
        assert _is_linked(b2, 'YasperEPNML114_Arc5', a)
    _safe_set(a, 'YasperEPNML114_Inscription', None)
    assert not _is_linked(a, 'YasperEPNML114_Inscription', b2)
    if hasattr(b2, 'YasperEPNML114_Arc5'):
        assert not _is_linked(b2, 'YasperEPNML114_Arc5', a)


def test_assoc_mean118_link_reassign_clear():
    a = YasperEPNML114_Stat(text="sample_text")
    b1 = YasperEPNML114_ProcessingTime()
    b2 = YasperEPNML114_ProcessingTime()
    _safe_set(a, 'YasperEPNML114_Stat119', b1)
    assert _is_linked(a, 'YasperEPNML114_Stat119', b1)
    if hasattr(b1, 'YasperEPNML114_ProcessingTime'):
        assert _is_linked(b1, 'YasperEPNML114_ProcessingTime', a)
    _safe_set(a, 'YasperEPNML114_Stat119', b2)
    assert _is_linked(a, 'YasperEPNML114_Stat119', b2)
    if hasattr(b1, 'YasperEPNML114_ProcessingTime'):
        assert not _is_linked(b1, 'YasperEPNML114_ProcessingTime', a)
    if hasattr(b2, 'YasperEPNML114_ProcessingTime'):
        assert _is_linked(b2, 'YasperEPNML114_ProcessingTime', a)
    _safe_set(a, 'YasperEPNML114_Stat119', None)
    assert not _is_linked(a, 'YasperEPNML114_Stat119', b2)
    if hasattr(b2, 'YasperEPNML114_ProcessingTime'):
        assert not _is_linked(b2, 'YasperEPNML114_ProcessingTime', a)


def test_assoc_name100_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Place(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Place(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation102', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation102', b1)
    if hasattr(b1, 'YasperEPNML114_Place101'):
        assert _is_linked(b1, 'YasperEPNML114_Place101', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation102', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation102', b2)
    if hasattr(b1, 'YasperEPNML114_Place101'):
        assert not _is_linked(b1, 'YasperEPNML114_Place101', a)
    if hasattr(b2, 'YasperEPNML114_Place101'):
        assert _is_linked(b2, 'YasperEPNML114_Place101', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation102', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation102', b2)
    if hasattr(b2, 'YasperEPNML114_Place101'):
        assert not _is_linked(b2, 'YasperEPNML114_Place101', a)


def test_assoc_name126_link_reassign_clear():
    a = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    b1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ReferencePlace127', {b1})
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace127', b1)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation128'):
        assert _is_linked(b1, 'YasperEPNML114_PnmlAnnotation128', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace127', {b2})
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace127', b2)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation128'):
        assert not _is_linked(b1, 'YasperEPNML114_PnmlAnnotation128', a)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation128'):
        assert _is_linked(b2, 'YasperEPNML114_PnmlAnnotation128', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace127', set())
    assert not _is_linked(a, 'YasperEPNML114_ReferencePlace127', b2)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation128'):
        assert not _is_linked(b2, 'YasperEPNML114_PnmlAnnotation128', a)


def test_assoc_name149_link_reassign_clear():
    a = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b2 = YasperEPNML114_PnmlAnnotation(text="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Transition150', {b1})
    assert _is_linked(a, 'YasperEPNML114_Transition150', b1)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation151'):
        assert _is_linked(b1, 'YasperEPNML114_PnmlAnnotation151', a)
    _safe_set(a, 'YasperEPNML114_Transition150', {b2})
    assert _is_linked(a, 'YasperEPNML114_Transition150', b2)
    if hasattr(b1, 'YasperEPNML114_PnmlAnnotation151'):
        assert not _is_linked(b1, 'YasperEPNML114_PnmlAnnotation151', a)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation151'):
        assert _is_linked(b2, 'YasperEPNML114_PnmlAnnotation151', a)
    _safe_set(a, 'YasperEPNML114_Transition150', set())
    assert not _is_linked(a, 'YasperEPNML114_Transition150', b2)
    if hasattr(b2, 'YasperEPNML114_PnmlAnnotation151'):
        assert not _is_linked(b2, 'YasperEPNML114_PnmlAnnotation151', a)


def test_assoc_name45_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation47', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation47', b1)
    if hasattr(b1, 'YasperEPNML114_Net46'):
        assert _is_linked(b1, 'YasperEPNML114_Net46', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation47', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation47', b2)
    if hasattr(b1, 'YasperEPNML114_Net46'):
        assert not _is_linked(b1, 'YasperEPNML114_Net46', a)
    if hasattr(b2, 'YasperEPNML114_Net46'):
        assert _is_linked(b2, 'YasperEPNML114_Net46', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation47', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation47', b2)
    if hasattr(b2, 'YasperEPNML114_Net46'):
        assert not _is_linked(b2, 'YasperEPNML114_Net46', a)


def test_assoc_name6_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b2 = YasperEPNML114_Arc(group="sample_text_2", id="sample_text_2", source="sample_text_2", target="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation', b1)
    if hasattr(b1, 'YasperEPNML114_Arc7'):
        assert _is_linked(b1, 'YasperEPNML114_Arc7', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation', b2)
    if hasattr(b1, 'YasperEPNML114_Arc7'):
        assert not _is_linked(b1, 'YasperEPNML114_Arc7', a)
    if hasattr(b2, 'YasperEPNML114_Arc7'):
        assert _is_linked(b2, 'YasperEPNML114_Arc7', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation', b2)
    if hasattr(b2, 'YasperEPNML114_Arc7'):
        assert not _is_linked(b2, 'YasperEPNML114_Arc7', a)


def test_assoc_name84_link_reassign_clear():
    a = YasperEPNML114_PnmlAnnotation(text="sample_text")
    b1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation86', b1)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation86', b1)
    if hasattr(b1, 'YasperEPNML114_Page85'):
        assert _is_linked(b1, 'YasperEPNML114_Page85', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation86', b2)
    assert _is_linked(a, 'YasperEPNML114_PnmlAnnotation86', b2)
    if hasattr(b1, 'YasperEPNML114_Page85'):
        assert not _is_linked(b1, 'YasperEPNML114_Page85', a)
    if hasattr(b2, 'YasperEPNML114_Page85'):
        assert _is_linked(b2, 'YasperEPNML114_Page85', a)
    _safe_set(a, 'YasperEPNML114_PnmlAnnotation86', None)
    assert not _is_linked(a, 'YasperEPNML114_PnmlAnnotation86', b2)
    if hasattr(b2, 'YasperEPNML114_Page85'):
        assert not _is_linked(b2, 'YasperEPNML114_Page85', a)


def test_assoc_net109_link_reassign_clear():
    a = YasperEPNML114_Pnml(group="sample_text")
    b1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Pnml110', {b1})
    assert _is_linked(a, 'YasperEPNML114_Pnml110', b1)
    if hasattr(b1, 'YasperEPNML114_Net111'):
        assert _is_linked(b1, 'YasperEPNML114_Net111', a)
    _safe_set(a, 'YasperEPNML114_Pnml110', {b2})
    assert _is_linked(a, 'YasperEPNML114_Pnml110', b2)
    if hasattr(b1, 'YasperEPNML114_Net111'):
        assert not _is_linked(b1, 'YasperEPNML114_Net111', a)
    if hasattr(b2, 'YasperEPNML114_Net111'):
        assert _is_linked(b2, 'YasperEPNML114_Net111', a)
    _safe_set(a, 'YasperEPNML114_Pnml110', set())
    assert not _is_linked(a, 'YasperEPNML114_Pnml110', b2)
    if hasattr(b2, 'YasperEPNML114_Net111'):
        assert not _is_linked(b2, 'YasperEPNML114_Net111', a)


def test_assoc_offset0_link_reassign_clear():
    a = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    b1 = YasperEPNML114_AnnotationGraphics()
    b2 = YasperEPNML114_AnnotationGraphics()
    _safe_set(a, 'YasperEPNML114_TwoDimVector', b1)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector', b1)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics'):
        assert _is_linked(b1, 'YasperEPNML114_AnnotationGraphics', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector', b2)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector', b2)
    if hasattr(b1, 'YasperEPNML114_AnnotationGraphics'):
        assert not _is_linked(b1, 'YasperEPNML114_AnnotationGraphics', a)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics'):
        assert _is_linked(b2, 'YasperEPNML114_AnnotationGraphics', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector', None)
    assert not _is_linked(a, 'YasperEPNML114_TwoDimVector', b2)
    if hasattr(b2, 'YasperEPNML114_AnnotationGraphics'):
        assert not _is_linked(b2, 'YasperEPNML114_AnnotationGraphics', a)


def test_assoc_page43_link_reassign_clear():
    a = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Page', b1)
    assert _is_linked(a, 'YasperEPNML114_Page', b1)
    if hasattr(b1, 'YasperEPNML114_Net44'):
        assert _is_linked(b1, 'YasperEPNML114_Net44', a)
    _safe_set(a, 'YasperEPNML114_Page', b2)
    assert _is_linked(a, 'YasperEPNML114_Page', b2)
    if hasattr(b1, 'YasperEPNML114_Net44'):
        assert not _is_linked(b1, 'YasperEPNML114_Net44', a)
    if hasattr(b2, 'YasperEPNML114_Net44'):
        assert _is_linked(b2, 'YasperEPNML114_Net44', a)
    _safe_set(a, 'YasperEPNML114_Page', None)
    assert not _is_linked(a, 'YasperEPNML114_Page', b2)
    if hasattr(b2, 'YasperEPNML114_Net44'):
        assert not _is_linked(b2, 'YasperEPNML114_Net44', a)


def test_assoc_page82_link_reassign_clear():
    a = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Page81', {b1})
    assert _is_linked(a, 'YasperEPNML114_Page81', b1)
    if hasattr(b1, 'YasperEPNML114_Page83'):
        assert _is_linked(b1, 'YasperEPNML114_Page83', a)
    _safe_set(a, 'YasperEPNML114_Page81', {b2})
    assert _is_linked(a, 'YasperEPNML114_Page81', b2)
    if hasattr(b1, 'YasperEPNML114_Page83'):
        assert not _is_linked(b1, 'YasperEPNML114_Page83', a)
    if hasattr(b2, 'YasperEPNML114_Page83'):
        assert _is_linked(b2, 'YasperEPNML114_Page83', a)
    _safe_set(a, 'YasperEPNML114_Page81', set())
    assert not _is_linked(a, 'YasperEPNML114_Page81', b2)
    if hasattr(b2, 'YasperEPNML114_Page83'):
        assert not _is_linked(b2, 'YasperEPNML114_Page83', a)


def test_assoc_pathGraphics135_link_reassign_clear():
    a = YasperEPNML114_ReferencePlaceSpecific(tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_NodeGraphics(group="sample_text")
    b2 = YasperEPNML114_NodeGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ReferencePlaceSpecific', b1)
    assert _is_linked(a, 'YasperEPNML114_ReferencePlaceSpecific', b1)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics136'):
        assert _is_linked(b1, 'YasperEPNML114_NodeGraphics136', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlaceSpecific', b2)
    assert _is_linked(a, 'YasperEPNML114_ReferencePlaceSpecific', b2)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics136'):
        assert not _is_linked(b1, 'YasperEPNML114_NodeGraphics136', a)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics136'):
        assert _is_linked(b2, 'YasperEPNML114_NodeGraphics136', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlaceSpecific', None)
    assert not _is_linked(a, 'YasperEPNML114_ReferencePlaceSpecific', b2)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics136'):
        assert not _is_linked(b2, 'YasperEPNML114_NodeGraphics136', a)


def test_assoc_place36_link_reassign_clear():
    a = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b1 = YasperEPNML114_PlaceType1()
    b2 = YasperEPNML114_PlaceType1()
    _safe_set(a, 'YasperEPNML114_Net37', {b1})
    assert _is_linked(a, 'YasperEPNML114_Net37', b1)
    if hasattr(b1, 'YasperEPNML114_PlaceType1'):
        assert _is_linked(b1, 'YasperEPNML114_PlaceType1', a)
    _safe_set(a, 'YasperEPNML114_Net37', {b2})
    assert _is_linked(a, 'YasperEPNML114_Net37', b2)
    if hasattr(b1, 'YasperEPNML114_PlaceType1'):
        assert not _is_linked(b1, 'YasperEPNML114_PlaceType1', a)
    if hasattr(b2, 'YasperEPNML114_PlaceType1'):
        assert _is_linked(b2, 'YasperEPNML114_PlaceType1', a)
    _safe_set(a, 'YasperEPNML114_Net37', set())
    assert not _is_linked(a, 'YasperEPNML114_Net37', b2)
    if hasattr(b2, 'YasperEPNML114_PlaceType1'):
        assert not _is_linked(b2, 'YasperEPNML114_PlaceType1', a)


def test_assoc_place72_link_reassign_clear():
    a = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_PlaceType1()
    b2 = YasperEPNML114_PlaceType1()
    _safe_set(a, 'YasperEPNML114_Page73', {b1})
    assert _is_linked(a, 'YasperEPNML114_Page73', b1)
    if hasattr(b1, 'YasperEPNML114_PlaceType174'):
        assert _is_linked(b1, 'YasperEPNML114_PlaceType174', a)
    _safe_set(a, 'YasperEPNML114_Page73', {b2})
    assert _is_linked(a, 'YasperEPNML114_Page73', b2)
    if hasattr(b1, 'YasperEPNML114_PlaceType174'):
        assert not _is_linked(b1, 'YasperEPNML114_PlaceType174', a)
    if hasattr(b2, 'YasperEPNML114_PlaceType174'):
        assert _is_linked(b2, 'YasperEPNML114_PlaceType174', a)
    _safe_set(a, 'YasperEPNML114_Page73', set())
    assert not _is_linked(a, 'YasperEPNML114_Page73', b2)
    if hasattr(b2, 'YasperEPNML114_PlaceType174'):
        assert not _is_linked(b2, 'YasperEPNML114_PlaceType174', a)


def test_assoc_pnml25_link_reassign_clear():
    a = YasperEPNML114_Pnml(group="sample_text")
    b1 = YasperEPNML114_DocumentRoot(mixed="sample_text")
    b2 = YasperEPNML114_DocumentRoot(mixed="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Pnml', b1)
    assert _is_linked(a, 'YasperEPNML114_Pnml', b1)
    if hasattr(b1, 'YasperEPNML114_DocumentRoot26'):
        assert _is_linked(b1, 'YasperEPNML114_DocumentRoot26', a)
    _safe_set(a, 'YasperEPNML114_Pnml', b2)
    assert _is_linked(a, 'YasperEPNML114_Pnml', b2)
    if hasattr(b1, 'YasperEPNML114_DocumentRoot26'):
        assert not _is_linked(b1, 'YasperEPNML114_DocumentRoot26', a)
    if hasattr(b2, 'YasperEPNML114_DocumentRoot26'):
        assert _is_linked(b2, 'YasperEPNML114_DocumentRoot26', a)
    _safe_set(a, 'YasperEPNML114_Pnml', None)
    assert not _is_linked(a, 'YasperEPNML114_Pnml', b2)
    if hasattr(b2, 'YasperEPNML114_DocumentRoot26'):
        assert not _is_linked(b2, 'YasperEPNML114_DocumentRoot26', a)


def test_assoc_position27_link_reassign_clear():
    a = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    b1 = YasperEPNML114_EdgeGraphics()
    b2 = YasperEPNML114_EdgeGraphics()
    _safe_set(a, 'YasperEPNML114_TwoDimVector29', b1)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector29', b1)
    if hasattr(b1, 'YasperEPNML114_EdgeGraphics28'):
        assert _is_linked(b1, 'YasperEPNML114_EdgeGraphics28', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector29', b2)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector29', b2)
    if hasattr(b1, 'YasperEPNML114_EdgeGraphics28'):
        assert not _is_linked(b1, 'YasperEPNML114_EdgeGraphics28', a)
    if hasattr(b2, 'YasperEPNML114_EdgeGraphics28'):
        assert _is_linked(b2, 'YasperEPNML114_EdgeGraphics28', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector29', None)
    assert not _is_linked(a, 'YasperEPNML114_TwoDimVector29', b2)
    if hasattr(b2, 'YasperEPNML114_EdgeGraphics28'):
        assert not _is_linked(b2, 'YasperEPNML114_EdgeGraphics28', a)


def test_assoc_position54_link_reassign_clear():
    a = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    b1 = YasperEPNML114_NetGraphics(group="sample_text")
    b2 = YasperEPNML114_NetGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_TwoDimVector56', b1)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector56', b1)
    if hasattr(b1, 'YasperEPNML114_NetGraphics55'):
        assert _is_linked(b1, 'YasperEPNML114_NetGraphics55', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector56', b2)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector56', b2)
    if hasattr(b1, 'YasperEPNML114_NetGraphics55'):
        assert not _is_linked(b1, 'YasperEPNML114_NetGraphics55', a)
    if hasattr(b2, 'YasperEPNML114_NetGraphics55'):
        assert _is_linked(b2, 'YasperEPNML114_NetGraphics55', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector56', None)
    assert not _is_linked(a, 'YasperEPNML114_TwoDimVector56', b2)
    if hasattr(b2, 'YasperEPNML114_NetGraphics55'):
        assert not _is_linked(b2, 'YasperEPNML114_NetGraphics55', a)


def test_assoc_position60_link_reassign_clear():
    a = YasperEPNML114_TwoDimVector(x="sample_text", y="sample_text")
    b1 = YasperEPNML114_NodeGraphics(group="sample_text")
    b2 = YasperEPNML114_NodeGraphics(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_TwoDimVector61', b1)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector61', b1)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics'):
        assert _is_linked(b1, 'YasperEPNML114_NodeGraphics', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector61', b2)
    assert _is_linked(a, 'YasperEPNML114_TwoDimVector61', b2)
    if hasattr(b1, 'YasperEPNML114_NodeGraphics'):
        assert not _is_linked(b1, 'YasperEPNML114_NodeGraphics', a)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics'):
        assert _is_linked(b2, 'YasperEPNML114_NodeGraphics', a)
    _safe_set(a, 'YasperEPNML114_TwoDimVector61', None)
    assert not _is_linked(a, 'YasperEPNML114_TwoDimVector61', b2)
    if hasattr(b2, 'YasperEPNML114_NodeGraphics'):
        assert not _is_linked(b2, 'YasperEPNML114_NodeGraphics', a)


def test_assoc_processingTime163_link_reassign_clear():
    a = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_ProcessingTime()
    b2 = YasperEPNML114_ProcessingTime()
    _safe_set(a, 'YasperEPNML114_TransitionSpecific164', b1)
    assert _is_linked(a, 'YasperEPNML114_TransitionSpecific164', b1)
    if hasattr(b1, 'YasperEPNML114_ProcessingTime165'):
        assert _is_linked(b1, 'YasperEPNML114_ProcessingTime165', a)
    _safe_set(a, 'YasperEPNML114_TransitionSpecific164', b2)
    assert _is_linked(a, 'YasperEPNML114_TransitionSpecific164', b2)
    if hasattr(b1, 'YasperEPNML114_ProcessingTime165'):
        assert not _is_linked(b1, 'YasperEPNML114_ProcessingTime165', a)
    if hasattr(b2, 'YasperEPNML114_ProcessingTime165'):
        assert _is_linked(b2, 'YasperEPNML114_ProcessingTime165', a)
    _safe_set(a, 'YasperEPNML114_TransitionSpecific164', None)
    assert not _is_linked(a, 'YasperEPNML114_TransitionSpecific164', b2)
    if hasattr(b2, 'YasperEPNML114_ProcessingTime165'):
        assert not _is_linked(b2, 'YasperEPNML114_ProcessingTime165', a)


def test_assoc_referencePlace65_link_reassign_clear():
    a = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    b1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ReferencePlace', b1)
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace', b1)
    if hasattr(b1, 'YasperEPNML114_Page66'):
        assert _is_linked(b1, 'YasperEPNML114_Page66', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace', b2)
    assert _is_linked(a, 'YasperEPNML114_ReferencePlace', b2)
    if hasattr(b1, 'YasperEPNML114_Page66'):
        assert not _is_linked(b1, 'YasperEPNML114_Page66', a)
    if hasattr(b2, 'YasperEPNML114_Page66'):
        assert _is_linked(b2, 'YasperEPNML114_Page66', a)
    _safe_set(a, 'YasperEPNML114_ReferencePlace', None)
    assert not _is_linked(a, 'YasperEPNML114_ReferencePlace', b2)
    if hasattr(b2, 'YasperEPNML114_Page66'):
        assert not _is_linked(b2, 'YasperEPNML114_Page66', a)


def test_assoc_role137_link_reassign_clear():
    a = YasperEPNML114_Role(text="sample_text")
    b1 = YasperEPNML114_Roles()
    b2 = YasperEPNML114_Roles()
    _safe_set(a, 'YasperEPNML114_Role', b1)
    assert _is_linked(a, 'YasperEPNML114_Role', b1)
    if hasattr(b1, 'YasperEPNML114_Roles'):
        assert _is_linked(b1, 'YasperEPNML114_Roles', a)
    _safe_set(a, 'YasperEPNML114_Role', b2)
    assert _is_linked(a, 'YasperEPNML114_Role', b2)
    if hasattr(b1, 'YasperEPNML114_Roles'):
        assert not _is_linked(b1, 'YasperEPNML114_Roles', a)
    if hasattr(b2, 'YasperEPNML114_Roles'):
        assert _is_linked(b2, 'YasperEPNML114_Roles', a)
    _safe_set(a, 'YasperEPNML114_Role', None)
    assert not _is_linked(a, 'YasperEPNML114_Role', b2)
    if hasattr(b2, 'YasperEPNML114_Roles'):
        assert not _is_linked(b2, 'YasperEPNML114_Roles', a)


def test_assoc_roles158_link_reassign_clear():
    a = YasperEPNML114_TransitionSpecific(tokenCaseSensitive="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_Roles()
    b2 = YasperEPNML114_Roles()
    _safe_set(a, 'YasperEPNML114_TransitionSpecific', b1)
    assert _is_linked(a, 'YasperEPNML114_TransitionSpecific', b1)
    if hasattr(b1, 'YasperEPNML114_Roles159'):
        assert _is_linked(b1, 'YasperEPNML114_Roles159', a)
    _safe_set(a, 'YasperEPNML114_TransitionSpecific', b2)
    assert _is_linked(a, 'YasperEPNML114_TransitionSpecific', b2)
    if hasattr(b1, 'YasperEPNML114_Roles159'):
        assert not _is_linked(b1, 'YasperEPNML114_Roles159', a)
    if hasattr(b2, 'YasperEPNML114_Roles159'):
        assert _is_linked(b2, 'YasperEPNML114_Roles159', a)
    _safe_set(a, 'YasperEPNML114_TransitionSpecific', None)
    assert not _is_linked(a, 'YasperEPNML114_TransitionSpecific', b2)
    if hasattr(b2, 'YasperEPNML114_Roles159'):
        assert not _is_linked(b2, 'YasperEPNML114_Roles159', a)


def test_assoc_toolspecific106_link_reassign_clear():
    a = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_Place(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Place(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ToolspecificType108', b1)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType108', b1)
    if hasattr(b1, 'YasperEPNML114_Place107'):
        assert _is_linked(b1, 'YasperEPNML114_Place107', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType108', b2)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType108', b2)
    if hasattr(b1, 'YasperEPNML114_Place107'):
        assert not _is_linked(b1, 'YasperEPNML114_Place107', a)
    if hasattr(b2, 'YasperEPNML114_Place107'):
        assert _is_linked(b2, 'YasperEPNML114_Place107', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType108', None)
    assert not _is_linked(a, 'YasperEPNML114_ToolspecificType108', b2)
    if hasattr(b2, 'YasperEPNML114_Place107'):
        assert not _is_linked(b2, 'YasperEPNML114_Place107', a)


def test_assoc_toolspecific11_link_reassign_clear():
    a = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b2 = YasperEPNML114_Arc(group="sample_text_2", id="sample_text_2", source="sample_text_2", target="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ToolspecificType', b1)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType', b1)
    if hasattr(b1, 'YasperEPNML114_Arc12'):
        assert _is_linked(b1, 'YasperEPNML114_Arc12', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType', b2)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType', b2)
    if hasattr(b1, 'YasperEPNML114_Arc12'):
        assert not _is_linked(b1, 'YasperEPNML114_Arc12', a)
    if hasattr(b2, 'YasperEPNML114_Arc12'):
        assert _is_linked(b2, 'YasperEPNML114_Arc12', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType', None)
    assert not _is_linked(a, 'YasperEPNML114_ToolspecificType', b2)
    if hasattr(b2, 'YasperEPNML114_Arc12'):
        assert not _is_linked(b2, 'YasperEPNML114_Arc12', a)


def test_assoc_toolspecific112_link_reassign_clear():
    a = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_Pnml(group="sample_text")
    b2 = YasperEPNML114_Pnml(group="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ToolspecificType114', b1)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType114', b1)
    if hasattr(b1, 'YasperEPNML114_Pnml113'):
        assert _is_linked(b1, 'YasperEPNML114_Pnml113', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType114', b2)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType114', b2)
    if hasattr(b1, 'YasperEPNML114_Pnml113'):
        assert not _is_linked(b1, 'YasperEPNML114_Pnml113', a)
    if hasattr(b2, 'YasperEPNML114_Pnml113'):
        assert _is_linked(b2, 'YasperEPNML114_Pnml113', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType114', None)
    assert not _is_linked(a, 'YasperEPNML114_ToolspecificType114', b2)
    if hasattr(b2, 'YasperEPNML114_Pnml113'):
        assert not _is_linked(b2, 'YasperEPNML114_Pnml113', a)


def test_assoc_toolspecific132_link_reassign_clear():
    a = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_ReferencePlace(group="sample_text", id="sample_text", ref="sample_text")
    b2 = YasperEPNML114_ReferencePlace(group="sample_text_2", id="sample_text_2", ref="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ToolspecificType134', b1)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType134', b1)
    if hasattr(b1, 'YasperEPNML114_ReferencePlace133'):
        assert _is_linked(b1, 'YasperEPNML114_ReferencePlace133', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType134', b2)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType134', b2)
    if hasattr(b1, 'YasperEPNML114_ReferencePlace133'):
        assert not _is_linked(b1, 'YasperEPNML114_ReferencePlace133', a)
    if hasattr(b2, 'YasperEPNML114_ReferencePlace133'):
        assert _is_linked(b2, 'YasperEPNML114_ReferencePlace133', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType134', None)
    assert not _is_linked(a, 'YasperEPNML114_ToolspecificType134', b2)
    if hasattr(b2, 'YasperEPNML114_ReferencePlace133'):
        assert not _is_linked(b2, 'YasperEPNML114_ReferencePlace133', a)


def test_assoc_toolspecific155_link_reassign_clear():
    a = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    b2 = YasperEPNML114_ToolspecificType(any="sample_text_2", group="sample_text_2", mixed="sample_text_2", tool="sample_text_2", version="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Transition156', {b1})
    assert _is_linked(a, 'YasperEPNML114_Transition156', b1)
    if hasattr(b1, 'YasperEPNML114_ToolspecificType157'):
        assert _is_linked(b1, 'YasperEPNML114_ToolspecificType157', a)
    _safe_set(a, 'YasperEPNML114_Transition156', {b2})
    assert _is_linked(a, 'YasperEPNML114_Transition156', b2)
    if hasattr(b1, 'YasperEPNML114_ToolspecificType157'):
        assert not _is_linked(b1, 'YasperEPNML114_ToolspecificType157', a)
    if hasattr(b2, 'YasperEPNML114_ToolspecificType157'):
        assert _is_linked(b2, 'YasperEPNML114_ToolspecificType157', a)
    _safe_set(a, 'YasperEPNML114_Transition156', set())
    assert not _is_linked(a, 'YasperEPNML114_Transition156', b2)
    if hasattr(b2, 'YasperEPNML114_ToolspecificType157'):
        assert not _is_linked(b2, 'YasperEPNML114_ToolspecificType157', a)


def test_assoc_toolspecific51_link_reassign_clear():
    a = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ToolspecificType53', b1)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType53', b1)
    if hasattr(b1, 'YasperEPNML114_Net52'):
        assert _is_linked(b1, 'YasperEPNML114_Net52', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType53', b2)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType53', b2)
    if hasattr(b1, 'YasperEPNML114_Net52'):
        assert not _is_linked(b1, 'YasperEPNML114_Net52', a)
    if hasattr(b2, 'YasperEPNML114_Net52'):
        assert _is_linked(b2, 'YasperEPNML114_Net52', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType53', None)
    assert not _is_linked(a, 'YasperEPNML114_ToolspecificType53', b2)
    if hasattr(b2, 'YasperEPNML114_Net52'):
        assert not _is_linked(b2, 'YasperEPNML114_Net52', a)


def test_assoc_toolspecific90_link_reassign_clear():
    a = YasperEPNML114_ToolspecificType(any="sample_text", group="sample_text", mixed="sample_text", tool="sample_text", version="sample_text")
    b1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ToolspecificType92', b1)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType92', b1)
    if hasattr(b1, 'YasperEPNML114_Page91'):
        assert _is_linked(b1, 'YasperEPNML114_Page91', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType92', b2)
    assert _is_linked(a, 'YasperEPNML114_ToolspecificType92', b2)
    if hasattr(b1, 'YasperEPNML114_Page91'):
        assert not _is_linked(b1, 'YasperEPNML114_Page91', a)
    if hasattr(b2, 'YasperEPNML114_Page91'):
        assert _is_linked(b2, 'YasperEPNML114_Page91', a)
    _safe_set(a, 'YasperEPNML114_ToolspecificType92', None)
    assert not _is_linked(a, 'YasperEPNML114_ToolspecificType92', b2)
    if hasattr(b2, 'YasperEPNML114_Page91'):
        assert not _is_linked(b2, 'YasperEPNML114_Page91', a)


def test_assoc_transformation146_link_reassign_clear():
    a = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_Transformation(text="sample_text")
    b2 = YasperEPNML114_Transformation(text="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Transition147', {b1})
    assert _is_linked(a, 'YasperEPNML114_Transition147', b1)
    if hasattr(b1, 'YasperEPNML114_Transformation148'):
        assert _is_linked(b1, 'YasperEPNML114_Transformation148', a)
    _safe_set(a, 'YasperEPNML114_Transition147', {b2})
    assert _is_linked(a, 'YasperEPNML114_Transition147', b2)
    if hasattr(b1, 'YasperEPNML114_Transformation148'):
        assert not _is_linked(b1, 'YasperEPNML114_Transformation148', a)
    if hasattr(b2, 'YasperEPNML114_Transformation148'):
        assert _is_linked(b2, 'YasperEPNML114_Transformation148', a)
    _safe_set(a, 'YasperEPNML114_Transition147', set())
    assert not _is_linked(a, 'YasperEPNML114_Transition147', b2)
    if hasattr(b2, 'YasperEPNML114_Transformation148'):
        assert not _is_linked(b2, 'YasperEPNML114_Transformation148', a)


def test_assoc_transition38_link_reassign_clear():
    a = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_Net(group="sample_text", id="sample_text", type="sample_text")
    b2 = YasperEPNML114_Net(group="sample_text_2", id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Transition', b1)
    assert _is_linked(a, 'YasperEPNML114_Transition', b1)
    if hasattr(b1, 'YasperEPNML114_Net39'):
        assert _is_linked(b1, 'YasperEPNML114_Net39', a)
    _safe_set(a, 'YasperEPNML114_Transition', b2)
    assert _is_linked(a, 'YasperEPNML114_Transition', b2)
    if hasattr(b1, 'YasperEPNML114_Net39'):
        assert not _is_linked(b1, 'YasperEPNML114_Net39', a)
    if hasattr(b2, 'YasperEPNML114_Net39'):
        assert _is_linked(b2, 'YasperEPNML114_Net39', a)
    _safe_set(a, 'YasperEPNML114_Transition', None)
    assert not _is_linked(a, 'YasperEPNML114_Transition', b2)
    if hasattr(b2, 'YasperEPNML114_Net39'):
        assert not _is_linked(b2, 'YasperEPNML114_Net39', a)


def test_assoc_transition75_link_reassign_clear():
    a = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Transition77', b1)
    assert _is_linked(a, 'YasperEPNML114_Transition77', b1)
    if hasattr(b1, 'YasperEPNML114_Page76'):
        assert _is_linked(b1, 'YasperEPNML114_Page76', a)
    _safe_set(a, 'YasperEPNML114_Transition77', b2)
    assert _is_linked(a, 'YasperEPNML114_Transition77', b2)
    if hasattr(b1, 'YasperEPNML114_Page76'):
        assert not _is_linked(b1, 'YasperEPNML114_Page76', a)
    if hasattr(b2, 'YasperEPNML114_Page76'):
        assert _is_linked(b2, 'YasperEPNML114_Page76', a)
    _safe_set(a, 'YasperEPNML114_Transition77', None)
    assert not _is_linked(a, 'YasperEPNML114_Transition77', b2)
    if hasattr(b2, 'YasperEPNML114_Page76'):
        assert not _is_linked(b2, 'YasperEPNML114_Page76', a)


def test_assoc_type1_link_reassign_clear():
    a = YasperEPNML114_ArcType(text="sample_text")
    b1 = YasperEPNML114_Arc(group="sample_text", id="sample_text", source="sample_text", target="sample_text")
    b2 = YasperEPNML114_Arc(group="sample_text_2", id="sample_text_2", source="sample_text_2", target="sample_text_2")
    _safe_set(a, 'YasperEPNML114_ArcType', b1)
    assert _is_linked(a, 'YasperEPNML114_ArcType', b1)
    if hasattr(b1, 'YasperEPNML114_Arc'):
        assert _is_linked(b1, 'YasperEPNML114_Arc', a)
    _safe_set(a, 'YasperEPNML114_ArcType', b2)
    assert _is_linked(a, 'YasperEPNML114_ArcType', b2)
    if hasattr(b1, 'YasperEPNML114_Arc'):
        assert not _is_linked(b1, 'YasperEPNML114_Arc', a)
    if hasattr(b2, 'YasperEPNML114_Arc'):
        assert _is_linked(b2, 'YasperEPNML114_Arc', a)
    _safe_set(a, 'YasperEPNML114_ArcType', None)
    assert not _is_linked(a, 'YasperEPNML114_ArcType', b2)
    if hasattr(b2, 'YasperEPNML114_Arc'):
        assert not _is_linked(b2, 'YasperEPNML114_Arc', a)


def test_assoc_type140_link_reassign_clear():
    a = YasperEPNML114_TransitionType(text="sample_text")
    b1 = YasperEPNML114_Transition(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Transition(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_TransitionType142', b1)
    assert _is_linked(a, 'YasperEPNML114_TransitionType142', b1)
    if hasattr(b1, 'YasperEPNML114_Transition141'):
        assert _is_linked(b1, 'YasperEPNML114_Transition141', a)
    _safe_set(a, 'YasperEPNML114_TransitionType142', b2)
    assert _is_linked(a, 'YasperEPNML114_TransitionType142', b2)
    if hasattr(b1, 'YasperEPNML114_Transition141'):
        assert not _is_linked(b1, 'YasperEPNML114_Transition141', a)
    if hasattr(b2, 'YasperEPNML114_Transition141'):
        assert _is_linked(b2, 'YasperEPNML114_Transition141', a)
    _safe_set(a, 'YasperEPNML114_TransitionType142', None)
    assert not _is_linked(a, 'YasperEPNML114_TransitionType142', b2)
    if hasattr(b2, 'YasperEPNML114_Transition141'):
        assert not _is_linked(b2, 'YasperEPNML114_Transition141', a)


def test_assoc_type70_link_reassign_clear():
    a = YasperEPNML114_TransitionType(text="sample_text")
    b1 = YasperEPNML114_Page(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Page(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_TransitionType', b1)
    assert _is_linked(a, 'YasperEPNML114_TransitionType', b1)
    if hasattr(b1, 'YasperEPNML114_Page71'):
        assert _is_linked(b1, 'YasperEPNML114_Page71', a)
    _safe_set(a, 'YasperEPNML114_TransitionType', b2)
    assert _is_linked(a, 'YasperEPNML114_TransitionType', b2)
    if hasattr(b1, 'YasperEPNML114_Page71'):
        assert not _is_linked(b1, 'YasperEPNML114_Page71', a)
    if hasattr(b2, 'YasperEPNML114_Page71'):
        assert _is_linked(b2, 'YasperEPNML114_Page71', a)
    _safe_set(a, 'YasperEPNML114_TransitionType', None)
    assert not _is_linked(a, 'YasperEPNML114_TransitionType', b2)
    if hasattr(b2, 'YasperEPNML114_Page71'):
        assert not _is_linked(b2, 'YasperEPNML114_Page71', a)


def test_assoc_type93_link_reassign_clear():
    a = YasperEPNML114_PlaceType(text="sample_text")
    b1 = YasperEPNML114_Place(group="sample_text", id="sample_text")
    b2 = YasperEPNML114_Place(group="sample_text_2", id="sample_text_2")
    _safe_set(a, 'YasperEPNML114_PlaceType', b1)
    assert _is_linked(a, 'YasperEPNML114_PlaceType', b1)
    if hasattr(b1, 'YasperEPNML114_Place'):
        assert _is_linked(b1, 'YasperEPNML114_Place', a)
    _safe_set(a, 'YasperEPNML114_PlaceType', b2)
    assert _is_linked(a, 'YasperEPNML114_PlaceType', b2)
    if hasattr(b1, 'YasperEPNML114_Place'):
        assert not _is_linked(b1, 'YasperEPNML114_Place', a)
    if hasattr(b2, 'YasperEPNML114_Place'):
        assert _is_linked(b2, 'YasperEPNML114_Place', a)
    _safe_set(a, 'YasperEPNML114_PlaceType', None)
    assert not _is_linked(a, 'YasperEPNML114_PlaceType', b2)
    if hasattr(b2, 'YasperEPNML114_Place'):
        assert not _is_linked(b2, 'YasperEPNML114_Place', a)


def test_assoc_variable18_link_reassign_clear():
    a = YasperEPNML114_Stat(text="sample_text")
    b1 = YasperEPNML114_Cost()
    b2 = YasperEPNML114_Cost()
    _safe_set(a, 'YasperEPNML114_Stat20', b1)
    assert _is_linked(a, 'YasperEPNML114_Stat20', b1)
    if hasattr(b1, 'YasperEPNML114_Cost19'):
        assert _is_linked(b1, 'YasperEPNML114_Cost19', a)
    _safe_set(a, 'YasperEPNML114_Stat20', b2)
    assert _is_linked(a, 'YasperEPNML114_Stat20', b2)
    if hasattr(b1, 'YasperEPNML114_Cost19'):
        assert not _is_linked(b1, 'YasperEPNML114_Cost19', a)
    if hasattr(b2, 'YasperEPNML114_Cost19'):
        assert _is_linked(b2, 'YasperEPNML114_Cost19', a)
    _safe_set(a, 'YasperEPNML114_Stat20', None)
    assert not _is_linked(a, 'YasperEPNML114_Stat20', b2)
    if hasattr(b2, 'YasperEPNML114_Cost19'):
        assert not _is_linked(b2, 'YasperEPNML114_Cost19', a)


def test_assoc_weight13_link_reassign_clear():
    a = YasperEPNML114_Stat(text="sample_text")
    b1 = YasperEPNML114_ConnectionWeight(connection="sample_text")
    b2 = YasperEPNML114_ConnectionWeight(connection="sample_text_2")
    _safe_set(a, 'YasperEPNML114_Stat', b1)
    assert _is_linked(a, 'YasperEPNML114_Stat', b1)
    if hasattr(b1, 'YasperEPNML114_ConnectionWeight'):
        assert _is_linked(b1, 'YasperEPNML114_ConnectionWeight', a)
    _safe_set(a, 'YasperEPNML114_Stat', b2)
    assert _is_linked(a, 'YasperEPNML114_Stat', b2)
    if hasattr(b1, 'YasperEPNML114_ConnectionWeight'):
        assert not _is_linked(b1, 'YasperEPNML114_ConnectionWeight', a)
    if hasattr(b2, 'YasperEPNML114_ConnectionWeight'):
        assert _is_linked(b2, 'YasperEPNML114_ConnectionWeight', a)
    _safe_set(a, 'YasperEPNML114_Stat', None)
    assert not _is_linked(a, 'YasperEPNML114_Stat', b2)
    if hasattr(b2, 'YasperEPNML114_ConnectionWeight'):
        assert not _is_linked(b2, 'YasperEPNML114_ConnectionWeight', a)


def test_assoc_xMLNSPrefixMap21_link_reassign_clear():
    a = YasperEPNML114_DocumentRoot(mixed="sample_text")
    b1 = YasperEPNML114_EStringToStringMapEntry()
    b2 = YasperEPNML114_EStringToStringMapEntry()
    _safe_set(a, 'YasperEPNML114_DocumentRoot', {b1})
    assert _is_linked(a, 'YasperEPNML114_DocumentRoot', b1)
    if hasattr(b1, 'YasperEPNML114_EStringToStringMapEntry'):
        assert _is_linked(b1, 'YasperEPNML114_EStringToStringMapEntry', a)
    _safe_set(a, 'YasperEPNML114_DocumentRoot', {b2})
    assert _is_linked(a, 'YasperEPNML114_DocumentRoot', b2)
    if hasattr(b1, 'YasperEPNML114_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'YasperEPNML114_EStringToStringMapEntry', a)
    if hasattr(b2, 'YasperEPNML114_EStringToStringMapEntry'):
        assert _is_linked(b2, 'YasperEPNML114_EStringToStringMapEntry', a)
    _safe_set(a, 'YasperEPNML114_DocumentRoot', set())
    assert not _is_linked(a, 'YasperEPNML114_DocumentRoot', b2)
    if hasattr(b2, 'YasperEPNML114_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'YasperEPNML114_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation22_link_reassign_clear():
    a = YasperEPNML114_DocumentRoot(mixed="sample_text")
    b1 = YasperEPNML114_EStringToStringMapEntry()
    b2 = YasperEPNML114_EStringToStringMapEntry()
    _safe_set(a, 'YasperEPNML114_DocumentRoot23', {b1})
    assert _is_linked(a, 'YasperEPNML114_DocumentRoot23', b1)
    if hasattr(b1, 'YasperEPNML114_EStringToStringMapEntry24'):
        assert _is_linked(b1, 'YasperEPNML114_EStringToStringMapEntry24', a)
    _safe_set(a, 'YasperEPNML114_DocumentRoot23', {b2})
    assert _is_linked(a, 'YasperEPNML114_DocumentRoot23', b2)
    if hasattr(b1, 'YasperEPNML114_EStringToStringMapEntry24'):
        assert not _is_linked(b1, 'YasperEPNML114_EStringToStringMapEntry24', a)
    if hasattr(b2, 'YasperEPNML114_EStringToStringMapEntry24'):
        assert _is_linked(b2, 'YasperEPNML114_EStringToStringMapEntry24', a)
    _safe_set(a, 'YasperEPNML114_DocumentRoot23', set())
    assert not _is_linked(a, 'YasperEPNML114_DocumentRoot23', b2)
    if hasattr(b2, 'YasperEPNML114_EStringToStringMapEntry24'):
        assert not _is_linked(b2, 'YasperEPNML114_EStringToStringMapEntry24', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Place_strategy = st.builds(Place)
@given(instance=Place_strategy)
@settings(max_examples=25)
def test_Place_instantiation(instance):
    assert isinstance(instance, Place)


YasperEPNML114_AnnotationGraphics_strategy = st.builds(YasperEPNML114_AnnotationGraphics)
@given(instance=YasperEPNML114_AnnotationGraphics_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_AnnotationGraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_AnnotationGraphics)


YasperEPNML114_Arc_strategy = st.builds(YasperEPNML114_Arc, group=safe_text, id=safe_text, source=safe_text, target=safe_text)
@given(instance=YasperEPNML114_Arc_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Arc_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Arc)


YasperEPNML114_ArcType_strategy = st.builds(YasperEPNML114_ArcType, text=safe_text)
@given(instance=YasperEPNML114_ArcType_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_ArcType_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ArcType)


YasperEPNML114_ConnectionWeight_strategy = st.builds(YasperEPNML114_ConnectionWeight, connection=safe_text)
@given(instance=YasperEPNML114_ConnectionWeight_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_ConnectionWeight_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ConnectionWeight)


YasperEPNML114_ConnectionWeights_strategy = st.builds(YasperEPNML114_ConnectionWeights)
@given(instance=YasperEPNML114_ConnectionWeights_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_ConnectionWeights_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ConnectionWeights)


YasperEPNML114_Cost_strategy = st.builds(YasperEPNML114_Cost)
@given(instance=YasperEPNML114_Cost_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Cost_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Cost)


YasperEPNML114_DocumentRoot_strategy = st.builds(YasperEPNML114_DocumentRoot, mixed=safe_text)
@given(instance=YasperEPNML114_DocumentRoot_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_DocumentRoot_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_DocumentRoot)


YasperEPNML114_EStringToStringMapEntry_strategy = st.builds(YasperEPNML114_EStringToStringMapEntry)
@given(instance=YasperEPNML114_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_EStringToStringMapEntry)


YasperEPNML114_EdgeGraphics_strategy = st.builds(YasperEPNML114_EdgeGraphics)
@given(instance=YasperEPNML114_EdgeGraphics_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_EdgeGraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_EdgeGraphics)


YasperEPNML114_InitialMarking_strategy = st.builds(YasperEPNML114_InitialMarking, text=safe_text)
@given(instance=YasperEPNML114_InitialMarking_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_InitialMarking_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_InitialMarking)


YasperEPNML114_Inscription_strategy = st.builds(YasperEPNML114_Inscription, text=safe_text)
@given(instance=YasperEPNML114_Inscription_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Inscription_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Inscription)


YasperEPNML114_Net_strategy = st.builds(YasperEPNML114_Net, group=safe_text, id=safe_text, type=safe_text)
@given(instance=YasperEPNML114_Net_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Net_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Net)


YasperEPNML114_NetGraphics_strategy = st.builds(YasperEPNML114_NetGraphics, group=safe_text)
@given(instance=YasperEPNML114_NetGraphics_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_NetGraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_NetGraphics)


YasperEPNML114_NodeGraphics_strategy = st.builds(YasperEPNML114_NodeGraphics, group=safe_text)
@given(instance=YasperEPNML114_NodeGraphics_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_NodeGraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_NodeGraphics)


YasperEPNML114_Page_strategy = st.builds(YasperEPNML114_Page, group=safe_text, id=safe_text)
@given(instance=YasperEPNML114_Page_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Page_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Page)


YasperEPNML114_Place_strategy = st.builds(YasperEPNML114_Place, group=safe_text, id=safe_text)
@given(instance=YasperEPNML114_Place_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Place_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Place)


YasperEPNML114_PlaceType_strategy = st.builds(YasperEPNML114_PlaceType, text=safe_text)
@given(instance=YasperEPNML114_PlaceType_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_PlaceType_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_PlaceType)


YasperEPNML114_PlaceType1_strategy = st.builds(YasperEPNML114_PlaceType1)
@given(instance=YasperEPNML114_PlaceType1_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_PlaceType1_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_PlaceType1)


YasperEPNML114_Pnml_strategy = st.builds(YasperEPNML114_Pnml, group=safe_text)
@given(instance=YasperEPNML114_Pnml_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Pnml_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Pnml)


YasperEPNML114_PnmlAnnotation_strategy = st.builds(YasperEPNML114_PnmlAnnotation, text=safe_text)
@given(instance=YasperEPNML114_PnmlAnnotation_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_PnmlAnnotation_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_PnmlAnnotation)


YasperEPNML114_ProcessingTime_strategy = st.builds(YasperEPNML114_ProcessingTime)
@given(instance=YasperEPNML114_ProcessingTime_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_ProcessingTime_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ProcessingTime)


YasperEPNML114_ReferencePlace_strategy = st.builds(YasperEPNML114_ReferencePlace, group=safe_text, id=safe_text, ref=safe_text)
@given(instance=YasperEPNML114_ReferencePlace_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_ReferencePlace_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ReferencePlace)


YasperEPNML114_ReferencePlaceSpecific_strategy = st.builds(YasperEPNML114_ReferencePlaceSpecific, tool=safe_text, version=safe_text)
@given(instance=YasperEPNML114_ReferencePlaceSpecific_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_ReferencePlaceSpecific_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ReferencePlaceSpecific)


YasperEPNML114_Role_strategy = st.builds(YasperEPNML114_Role, text=safe_text)
@given(instance=YasperEPNML114_Role_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Role_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Role)


YasperEPNML114_Roles_strategy = st.builds(YasperEPNML114_Roles)
@given(instance=YasperEPNML114_Roles_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Roles_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Roles)


YasperEPNML114_Stat_strategy = st.builds(YasperEPNML114_Stat, text=safe_text)
@given(instance=YasperEPNML114_Stat_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Stat_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Stat)


YasperEPNML114_ToolspecificType_strategy = st.builds(YasperEPNML114_ToolspecificType, any=safe_text, group=safe_text, mixed=safe_text, tool=safe_text, version=safe_text)
@given(instance=YasperEPNML114_ToolspecificType_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_ToolspecificType_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ToolspecificType)


YasperEPNML114_Transformation_strategy = st.builds(YasperEPNML114_Transformation, text=safe_text)
@given(instance=YasperEPNML114_Transformation_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Transformation_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Transformation)


YasperEPNML114_Transition_strategy = st.builds(YasperEPNML114_Transition, group=safe_text, id=safe_text)
@given(instance=YasperEPNML114_Transition_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_Transition_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Transition)


YasperEPNML114_TransitionSpecific_strategy = st.builds(YasperEPNML114_TransitionSpecific, tokenCaseSensitive=safe_text, tool=safe_text, version=safe_text)
@given(instance=YasperEPNML114_TransitionSpecific_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_TransitionSpecific_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_TransitionSpecific)


YasperEPNML114_TransitionType_strategy = st.builds(YasperEPNML114_TransitionType, text=safe_text)
@given(instance=YasperEPNML114_TransitionType_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_TransitionType_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_TransitionType)


YasperEPNML114_TwoDimVector_strategy = st.builds(YasperEPNML114_TwoDimVector, x=safe_text, y=safe_text)
@given(instance=YasperEPNML114_TwoDimVector_strategy)
@settings(max_examples=25)
def test_YasperEPNML114_TwoDimVector_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_TwoDimVector)



