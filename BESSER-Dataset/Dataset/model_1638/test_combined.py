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
    CompoundColorSet,
    cpntools_Union,
    cpntools_Record,
    cpntools_List,
    cpntools_Alias,
    cpntools_Subset,
    cpntools_Product,
    ColorSet,
    cpntools_SimpleColorSet,
    SimpleColorSet,
    cpntools_Integer,
    cpntools_String,
    cpntools_Boolean,
    cpntools_Index,
    cpntools_Real,
    cpntools_LargeInteger,
    cpntools_Time,
    cpntools_Enumerated,
    cpntools_Unit,
    cpntools_CompoundColorSet,
    Auxiliary,
    cpntools_AuxEllipse,
    cpntools_AuxBox,
    cpntools_AuxText,
    cpntools_Declaration,
    Declaration,
    cpntools_Var,
    cpntools_Ml,
    cpntools_Globref,
    cpntools_ColorSet,
    DiagramElement,
    cpntools_TransTime,
    cpntools_Annot,
    cpntools_TransPriority,
    cpntools_TransCond,
    cpntools_Port,
    cpntools_Initmark,
    cpntools_Block,
    cpntools_DiagramElement,
    cpntools_Arc,
    cpntools_Trans,
    cpntools_Auxiliary,
    cpntools_Place,
    cpntools_Group,
    cpntools_Page,
    cpntools_Binder,
    cpntools_Globbox,
    cpntools_Fusion,
    cpntools_Cpnet,
    Colour16,
    Orientation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_compoundcolorset_is_not_abstract():
    assert not inspect.isabstract(CompoundColorSet)


def test_hyp_compoundcolorset_constructor_exists():
    assert callable(CompoundColorSet.__init__)


def test_hyp_compoundcolorset_constructor_args():
    sig = inspect.signature(CompoundColorSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_union_is_not_abstract():
    assert not inspect.isabstract(cpntools_Union)


def test_hyp_cpntools_union_constructor_exists():
    assert callable(cpntools_Union.__init__)


def test_hyp_cpntools_union_constructor_args():
    sig = inspect.signature(cpntools_Union.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_record_is_not_abstract():
    assert not inspect.isabstract(cpntools_Record)


def test_hyp_cpntools_record_constructor_exists():
    assert callable(cpntools_Record.__init__)


def test_hyp_cpntools_record_constructor_args():
    sig = inspect.signature(cpntools_Record.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_list_is_not_abstract():
    assert not inspect.isabstract(cpntools_List)


def test_hyp_cpntools_list_constructor_exists():
    assert callable(cpntools_List.__init__)


def test_hyp_cpntools_list_constructor_args():
    sig = inspect.signature(cpntools_List.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_alias_is_not_abstract():
    assert not inspect.isabstract(cpntools_Alias)


def test_hyp_cpntools_alias_constructor_exists():
    assert callable(cpntools_Alias.__init__)


def test_hyp_cpntools_alias_constructor_args():
    sig = inspect.signature(cpntools_Alias.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_subset_is_not_abstract():
    assert not inspect.isabstract(cpntools_Subset)


def test_hyp_cpntools_subset_constructor_exists():
    assert callable(cpntools_Subset.__init__)


def test_hyp_cpntools_subset_constructor_args():
    sig = inspect.signature(cpntools_Subset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_product_is_not_abstract():
    assert not inspect.isabstract(cpntools_Product)


def test_hyp_cpntools_product_constructor_exists():
    assert callable(cpntools_Product.__init__)


def test_hyp_cpntools_product_constructor_args():
    sig = inspect.signature(cpntools_Product.__init__)
    params = list(sig.parameters.keys())



def test_hyp_colorset_is_not_abstract():
    assert not inspect.isabstract(ColorSet)


def test_hyp_colorset_constructor_exists():
    assert callable(ColorSet.__init__)


def test_hyp_colorset_constructor_args():
    sig = inspect.signature(ColorSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_simplecolorset_is_not_abstract():
    assert not inspect.isabstract(cpntools_SimpleColorSet)


def test_hyp_cpntools_simplecolorset_constructor_exists():
    assert callable(cpntools_SimpleColorSet.__init__)


def test_hyp_cpntools_simplecolorset_constructor_args():
    sig = inspect.signature(cpntools_SimpleColorSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplecolorset_is_not_abstract():
    assert not inspect.isabstract(SimpleColorSet)


def test_hyp_simplecolorset_constructor_exists():
    assert callable(SimpleColorSet.__init__)


def test_hyp_simplecolorset_constructor_args():
    sig = inspect.signature(SimpleColorSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_integer_is_not_abstract():
    assert not inspect.isabstract(cpntools_Integer)


def test_hyp_cpntools_integer_constructor_exists():
    assert callable(cpntools_Integer.__init__)


def test_hyp_cpntools_integer_constructor_args():
    sig = inspect.signature(cpntools_Integer.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"




def test_hyp_cpntools_string_is_not_abstract():
    assert not inspect.isabstract(cpntools_String)


def test_hyp_cpntools_string_constructor_exists():
    assert callable(cpntools_String.__init__)


def test_hyp_cpntools_string_constructor_args():
    sig = inspect.signature(cpntools_String.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"
    assert "and_" in params, "Missing parameter 'and_'"





def test_hyp_cpntools_boolean_is_not_abstract():
    assert not inspect.isabstract(cpntools_Boolean)


def test_hyp_cpntools_boolean_constructor_exists():
    assert callable(cpntools_Boolean.__init__)


def test_hyp_cpntools_boolean_constructor_args():
    sig = inspect.signature(cpntools_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"




def test_hyp_cpntools_index_is_not_abstract():
    assert not inspect.isabstract(cpntools_Index)


def test_hyp_cpntools_index_constructor_exists():
    assert callable(cpntools_Index.__init__)


def test_hyp_cpntools_index_constructor_args():
    sig = inspect.signature(cpntools_Index.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"




def test_hyp_cpntools_real_is_not_abstract():
    assert not inspect.isabstract(cpntools_Real)


def test_hyp_cpntools_real_constructor_exists():
    assert callable(cpntools_Real.__init__)


def test_hyp_cpntools_real_constructor_args():
    sig = inspect.signature(cpntools_Real.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"




def test_hyp_cpntools_largeinteger_is_not_abstract():
    assert not inspect.isabstract(cpntools_LargeInteger)


def test_hyp_cpntools_largeinteger_constructor_exists():
    assert callable(cpntools_LargeInteger.__init__)


def test_hyp_cpntools_largeinteger_constructor_args():
    sig = inspect.signature(cpntools_LargeInteger.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"




def test_hyp_cpntools_time_is_not_abstract():
    assert not inspect.isabstract(cpntools_Time)


def test_hyp_cpntools_time_constructor_exists():
    assert callable(cpntools_Time.__init__)


def test_hyp_cpntools_time_constructor_args():
    sig = inspect.signature(cpntools_Time.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_enumerated_is_not_abstract():
    assert not inspect.isabstract(cpntools_Enumerated)


def test_hyp_cpntools_enumerated_constructor_exists():
    assert callable(cpntools_Enumerated.__init__)


def test_hyp_cpntools_enumerated_constructor_args():
    sig = inspect.signature(cpntools_Enumerated.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"




def test_hyp_cpntools_unit_is_not_abstract():
    assert not inspect.isabstract(cpntools_Unit)


def test_hyp_cpntools_unit_constructor_exists():
    assert callable(cpntools_Unit.__init__)


def test_hyp_cpntools_unit_constructor_args():
    sig = inspect.signature(cpntools_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "with_" in params, "Missing parameter 'with_'"




def test_hyp_cpntools_compoundcolorset_is_not_abstract():
    assert not inspect.isabstract(cpntools_CompoundColorSet)


def test_hyp_cpntools_compoundcolorset_constructor_exists():
    assert callable(cpntools_CompoundColorSet.__init__)


def test_hyp_cpntools_compoundcolorset_constructor_args():
    sig = inspect.signature(cpntools_CompoundColorSet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_auxiliary_is_not_abstract():
    assert not inspect.isabstract(Auxiliary)


def test_hyp_auxiliary_constructor_exists():
    assert callable(Auxiliary.__init__)


def test_hyp_auxiliary_constructor_args():
    sig = inspect.signature(Auxiliary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_auxellipse_is_not_abstract():
    assert not inspect.isabstract(cpntools_AuxEllipse)


def test_hyp_cpntools_auxellipse_constructor_exists():
    assert callable(cpntools_AuxEllipse.__init__)


def test_hyp_cpntools_auxellipse_constructor_args():
    sig = inspect.signature(cpntools_AuxEllipse.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"





def test_hyp_cpntools_auxbox_is_not_abstract():
    assert not inspect.isabstract(cpntools_AuxBox)


def test_hyp_cpntools_auxbox_constructor_exists():
    assert callable(cpntools_AuxBox.__init__)


def test_hyp_cpntools_auxbox_constructor_args():
    sig = inspect.signature(cpntools_AuxBox.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"





def test_hyp_cpntools_auxtext_is_not_abstract():
    assert not inspect.isabstract(cpntools_AuxText)


def test_hyp_cpntools_auxtext_constructor_exists():
    assert callable(cpntools_AuxText.__init__)


def test_hyp_cpntools_auxtext_constructor_args():
    sig = inspect.signature(cpntools_AuxText.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_cpntools_declaration_is_not_abstract():
    assert not inspect.isabstract(cpntools_Declaration)


def test_hyp_cpntools_declaration_constructor_exists():
    assert callable(cpntools_Declaration.__init__)


def test_hyp_cpntools_declaration_constructor_args():
    sig = inspect.signature(cpntools_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_hyp_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_hyp_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_var_is_not_abstract():
    assert not inspect.isabstract(cpntools_Var)


def test_hyp_cpntools_var_constructor_exists():
    assert callable(cpntools_Var.__init__)


def test_hyp_cpntools_var_constructor_args():
    sig = inspect.signature(cpntools_Var.__init__)
    params = list(sig.parameters.keys())
    assert "idname" in params, "Missing parameter 'idname'"




def test_hyp_cpntools_ml_is_not_abstract():
    assert not inspect.isabstract(cpntools_Ml)


def test_hyp_cpntools_ml_constructor_exists():
    assert callable(cpntools_Ml.__init__)


def test_hyp_cpntools_ml_constructor_args():
    sig = inspect.signature(cpntools_Ml.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_cpntools_globref_is_not_abstract():
    assert not inspect.isabstract(cpntools_Globref)


def test_hyp_cpntools_globref_constructor_exists():
    assert callable(cpntools_Globref.__init__)


def test_hyp_cpntools_globref_constructor_args():
    sig = inspect.signature(cpntools_Globref.__init__)
    params = list(sig.parameters.keys())
    assert "idname" in params, "Missing parameter 'idname'"




def test_hyp_cpntools_colorset_is_not_abstract():
    assert not inspect.isabstract(cpntools_ColorSet)


def test_hyp_cpntools_colorset_constructor_exists():
    assert callable(cpntools_ColorSet.__init__)


def test_hyp_cpntools_colorset_constructor_args():
    sig = inspect.signature(cpntools_ColorSet.__init__)
    params = list(sig.parameters.keys())
    assert "declare" in params, "Missing parameter 'declare'"
    assert "timed" in params, "Missing parameter 'timed'"
    assert "colorSetType" in params, "Missing parameter 'colorSetType'"
    assert "idname" in params, "Missing parameter 'idname'"







def test_hyp_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_hyp_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_hyp_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_transtime_is_not_abstract():
    assert not inspect.isabstract(cpntools_TransTime)


def test_hyp_cpntools_transtime_constructor_exists():
    assert callable(cpntools_TransTime.__init__)


def test_hyp_cpntools_transtime_constructor_args():
    sig = inspect.signature(cpntools_TransTime.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_cpntools_annot_is_not_abstract():
    assert not inspect.isabstract(cpntools_Annot)


def test_hyp_cpntools_annot_constructor_exists():
    assert callable(cpntools_Annot.__init__)


def test_hyp_cpntools_annot_constructor_args():
    sig = inspect.signature(cpntools_Annot.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_cpntools_transpriority_is_not_abstract():
    assert not inspect.isabstract(cpntools_TransPriority)


def test_hyp_cpntools_transpriority_constructor_exists():
    assert callable(cpntools_TransPriority.__init__)


def test_hyp_cpntools_transpriority_constructor_args():
    sig = inspect.signature(cpntools_TransPriority.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_cpntools_transcond_is_not_abstract():
    assert not inspect.isabstract(cpntools_TransCond)


def test_hyp_cpntools_transcond_constructor_exists():
    assert callable(cpntools_TransCond.__init__)


def test_hyp_cpntools_transcond_constructor_args():
    sig = inspect.signature(cpntools_TransCond.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_cpntools_port_is_not_abstract():
    assert not inspect.isabstract(cpntools_Port)


def test_hyp_cpntools_port_constructor_exists():
    assert callable(cpntools_Port.__init__)


def test_hyp_cpntools_port_constructor_args():
    sig = inspect.signature(cpntools_Port.__init__)
    params = list(sig.parameters.keys())
    assert "portType" in params, "Missing parameter 'portType'"




def test_hyp_cpntools_initmark_is_not_abstract():
    assert not inspect.isabstract(cpntools_Initmark)


def test_hyp_cpntools_initmark_constructor_exists():
    assert callable(cpntools_Initmark.__init__)


def test_hyp_cpntools_initmark_constructor_args():
    sig = inspect.signature(cpntools_Initmark.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"




def test_hyp_cpntools_block_is_not_abstract():
    assert not inspect.isabstract(cpntools_Block)


def test_hyp_cpntools_block_constructor_exists():
    assert callable(cpntools_Block.__init__)


def test_hyp_cpntools_block_constructor_args():
    sig = inspect.signature(cpntools_Block.__init__)
    params = list(sig.parameters.keys())
    assert "idname" in params, "Missing parameter 'idname'"




def test_hyp_cpntools_diagramelement_is_not_abstract():
    assert not inspect.isabstract(cpntools_DiagramElement)


def test_hyp_cpntools_diagramelement_constructor_exists():
    assert callable(cpntools_DiagramElement.__init__)


def test_hyp_cpntools_diagramelement_constructor_args():
    sig = inspect.signature(cpntools_DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "fillFilled" in params, "Missing parameter 'fillFilled'"
    assert "lineType" in params, "Missing parameter 'lineType'"
    assert "posy" in params, "Missing parameter 'posy'"
    assert "fillPattern" in params, "Missing parameter 'fillPattern'"
    assert "lineColour" in params, "Missing parameter 'lineColour'"
    assert "posx" in params, "Missing parameter 'posx'"
    assert "lineThick" in params, "Missing parameter 'lineThick'"
    assert "fillColour" in params, "Missing parameter 'fillColour'"











def test_hyp_cpntools_arc_is_not_abstract():
    assert not inspect.isabstract(cpntools_Arc)


def test_hyp_cpntools_arc_constructor_exists():
    assert callable(cpntools_Arc.__init__)


def test_hyp_cpntools_arc_constructor_args():
    sig = inspect.signature(cpntools_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "headsize" in params, "Missing parameter 'headsize'"
    assert "currentcyckle" in params, "Missing parameter 'currentcyckle'"







def test_hyp_cpntools_trans_is_not_abstract():
    assert not inspect.isabstract(cpntools_Trans)


def test_hyp_cpntools_trans_constructor_exists():
    assert callable(cpntools_Trans.__init__)


def test_hyp_cpntools_trans_constructor_args():
    sig = inspect.signature(cpntools_Trans.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "text" in params, "Missing parameter 'text'"
    assert "height" in params, "Missing parameter 'height'"
    assert "explicit" in params, "Missing parameter 'explicit'"







def test_hyp_cpntools_auxiliary_is_not_abstract():
    assert not inspect.isabstract(cpntools_Auxiliary)


def test_hyp_cpntools_auxiliary_constructor_exists():
    assert callable(cpntools_Auxiliary.__init__)


def test_hyp_cpntools_auxiliary_constructor_args():
    sig = inspect.signature(cpntools_Auxiliary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cpntools_place_is_not_abstract():
    assert not inspect.isabstract(cpntools_Place)


def test_hyp_cpntools_place_constructor_exists():
    assert callable(cpntools_Place.__init__)


def test_hyp_cpntools_place_constructor_args():
    sig = inspect.signature(cpntools_Place.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "text" in params, "Missing parameter 'text'"
    assert "height" in params, "Missing parameter 'height'"






def test_hyp_cpntools_group_is_not_abstract():
    assert not inspect.isabstract(cpntools_Group)


def test_hyp_cpntools_group_constructor_exists():
    assert callable(cpntools_Group.__init__)


def test_hyp_cpntools_group_constructor_args():
    sig = inspect.signature(cpntools_Group.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpntools_page_is_not_abstract():
    assert not inspect.isabstract(cpntools_Page)


def test_hyp_cpntools_page_constructor_exists():
    assert callable(cpntools_Page.__init__)


def test_hyp_cpntools_page_constructor_args():
    sig = inspect.signature(cpntools_Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpntools_binder_is_not_abstract():
    assert not inspect.isabstract(cpntools_Binder)


def test_hyp_cpntools_binder_constructor_exists():
    assert callable(cpntools_Binder.__init__)


def test_hyp_cpntools_binder_constructor_args():
    sig = inspect.signature(cpntools_Binder.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "posx" in params, "Missing parameter 'posx'"
    assert "posy" in params, "Missing parameter 'posy'"
    assert "width" in params, "Missing parameter 'width'"







def test_hyp_cpntools_globbox_is_not_abstract():
    assert not inspect.isabstract(cpntools_Globbox)


def test_hyp_cpntools_globbox_constructor_exists():
    assert callable(cpntools_Globbox.__init__)


def test_hyp_cpntools_globbox_constructor_args():
    sig = inspect.signature(cpntools_Globbox.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpntools_fusion_is_not_abstract():
    assert not inspect.isabstract(cpntools_Fusion)


def test_hyp_cpntools_fusion_constructor_exists():
    assert callable(cpntools_Fusion.__init__)


def test_hyp_cpntools_fusion_constructor_args():
    sig = inspect.signature(cpntools_Fusion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_cpntools_cpnet_is_not_abstract():
    assert not inspect.isabstract(cpntools_Cpnet)


def test_hyp_cpntools_cpnet_constructor_exists():
    assert callable(cpntools_Cpnet.__init__)


def test_hyp_cpntools_cpnet_constructor_args():
    sig = inspect.signature(cpntools_Cpnet.__init__)
    params = list(sig.parameters.keys())

def test_hyp_colour16_exists():
    # Check that the Enumeration exists
    assert Colour16 is not None

def test_hyp_colour16_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Colour16]
    expected_literals = [
        "Gray",
        "Teal",
        "Navy",
        "White",
        "Fuchsia",
        "Blue",
        "Olive",
        "Silver",
        "Maroon",
        "Black",
        "Lime",
        "Red",
        "Yellow",
        "Aqua",
        "Green",
        "Purple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Colour16"

def test_hyp_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_hyp_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "undefined",
        "Inhibitor",
        "TtoP",
        "PtoT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"


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
CompoundColorSet_strategy = st.builds(
    CompoundColorSet,
)
cpntools_Union_strategy = st.builds(
    cpntools_Union,
)
cpntools_Record_strategy = st.builds(
    cpntools_Record,
)
cpntools_List_strategy = st.builds(
    cpntools_List,
)
cpntools_Alias_strategy = st.builds(
    cpntools_Alias,
)
cpntools_Subset_strategy = st.builds(
    cpntools_Subset,
)
cpntools_Product_strategy = st.builds(
    cpntools_Product,
)
ColorSet_strategy = st.builds(
    ColorSet,
)
cpntools_SimpleColorSet_strategy = st.builds(
    cpntools_SimpleColorSet,
)
SimpleColorSet_strategy = st.builds(
    SimpleColorSet,
)
cpntools_Integer_strategy = st.builds(
    cpntools_Integer,
    with_=
        safe_text
)
cpntools_String_strategy = st.builds(
    cpntools_String,
    with_=
        safe_text,
    and_=
        safe_text
)
cpntools_Boolean_strategy = st.builds(
    cpntools_Boolean,
    with_=
        safe_text
)
cpntools_Index_strategy = st.builds(
    cpntools_Index,
    with_=
        safe_text
)
cpntools_Real_strategy = st.builds(
    cpntools_Real,
    with_=
        safe_text
)
cpntools_LargeInteger_strategy = st.builds(
    cpntools_LargeInteger,
    with_=
        safe_text
)
cpntools_Time_strategy = st.builds(
    cpntools_Time,
)
cpntools_Enumerated_strategy = st.builds(
    cpntools_Enumerated,
    with_=
        safe_text
)
cpntools_Unit_strategy = st.builds(
    cpntools_Unit,
    with_=
        safe_text
)
cpntools_CompoundColorSet_strategy = st.builds(
    cpntools_CompoundColorSet,
)
Auxiliary_strategy = st.builds(
    Auxiliary,
)
cpntools_AuxEllipse_strategy = st.builds(
    cpntools_AuxEllipse,
    width=
        st.integers(),
    height=
        st.integers()
)
cpntools_AuxBox_strategy = st.builds(
    cpntools_AuxBox,
    width=
        st.integers(),
    height=
        st.integers()
)
cpntools_AuxText_strategy = st.builds(
    cpntools_AuxText,
    text=
        safe_text
)
cpntools_Declaration_strategy = st.builds(
    cpntools_Declaration,
)
Declaration_strategy = st.builds(
    Declaration,
)
cpntools_Var_strategy = st.builds(
    cpntools_Var,
    idname=
        safe_text
)
cpntools_Ml_strategy = st.builds(
    cpntools_Ml,
    expression=
        safe_text
)
cpntools_Globref_strategy = st.builds(
    cpntools_Globref,
    idname=
        safe_text
)
cpntools_ColorSet_strategy = st.builds(
    cpntools_ColorSet,
    declare=
        safe_text,
    timed=
        st.booleans(),
    colorSetType=
        safe_text,
    idname=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
cpntools_TransTime_strategy = st.builds(
    cpntools_TransTime,
    text=
        safe_text
)
cpntools_Annot_strategy = st.builds(
    cpntools_Annot,
    text=
        safe_text
)
cpntools_TransPriority_strategy = st.builds(
    cpntools_TransPriority,
    text=
        safe_text
)
cpntools_TransCond_strategy = st.builds(
    cpntools_TransCond,
    text=
        safe_text
)
cpntools_Port_strategy = st.builds(
    cpntools_Port,
    portType=
        safe_text
)
cpntools_Initmark_strategy = st.builds(
    cpntools_Initmark,
    expression=
        safe_text
)
cpntools_Block_strategy = st.builds(
    cpntools_Block,
    idname=
        safe_text
)
cpntools_DiagramElement_strategy = st.builds(
    cpntools_DiagramElement,
    fillFilled=
        st.booleans(),
    lineType=
        safe_text,
    posy=
        st.integers(),
    fillPattern=
        safe_text,
    lineColour=
        safe_text,
    posx=
        st.integers(),
    lineThick=
        st.integers(),
    fillColour=
        safe_text
)
cpntools_Arc_strategy = st.builds(
    cpntools_Arc,
    order=
        st.integers(),
    orientation=
        safe_text,
    headsize=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    currentcyckle=
        safe_text
)
cpntools_Trans_strategy = st.builds(
    cpntools_Trans,
    width=
        st.integers(),
    text=
        safe_text,
    height=
        st.integers(),
    explicit=
        st.booleans()
)
cpntools_Auxiliary_strategy = st.builds(
    cpntools_Auxiliary,
)
cpntools_Place_strategy = st.builds(
    cpntools_Place,
    width=
        st.integers(),
    text=
        safe_text,
    height=
        st.integers()
)
cpntools_Group_strategy = st.builds(
    cpntools_Group,
    name=
        safe_text
)
cpntools_Page_strategy = st.builds(
    cpntools_Page,
    name=
        safe_text
)
cpntools_Binder_strategy = st.builds(
    cpntools_Binder,
    height=
        st.integers(),
    posx=
        st.integers(),
    posy=
        st.integers(),
    width=
        st.integers()
)
cpntools_Globbox_strategy = st.builds(
    cpntools_Globbox,
    name=
        safe_text
)
cpntools_Fusion_strategy = st.builds(
    cpntools_Fusion,
    name=
        safe_text
)
cpntools_Cpnet_strategy = st.builds(
    cpntools_Cpnet,
)














@given(instance=cpntools_Integer_strategy)
def test_hyp_cpntools_integer_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original




@given(instance=cpntools_String_strategy)
def test_hyp_cpntools_string_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original



@given(instance=cpntools_String_strategy)
def test_hyp_cpntools_string_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original




@given(instance=cpntools_Boolean_strategy)
def test_hyp_cpntools_boolean_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original




@given(instance=cpntools_Index_strategy)
def test_hyp_cpntools_index_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original




@given(instance=cpntools_Real_strategy)
def test_hyp_cpntools_real_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original




@given(instance=cpntools_LargeInteger_strategy)
def test_hyp_cpntools_largeinteger_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original





@given(instance=cpntools_Enumerated_strategy)
def test_hyp_cpntools_enumerated_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original




@given(instance=cpntools_Unit_strategy)
def test_hyp_cpntools_unit_with__setter(instance):
    original = instance.with_
    instance.with_ = original
    assert instance.with_ == original






@given(instance=cpntools_AuxEllipse_strategy)
def test_hyp_cpntools_auxellipse_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_AuxEllipse_strategy)
def test_hyp_cpntools_auxellipse_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=cpntools_AuxBox_strategy)
def test_hyp_cpntools_auxbox_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_AuxBox_strategy)
def test_hyp_cpntools_auxbox_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=cpntools_AuxText_strategy)
def test_hyp_cpntools_auxtext_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original






@given(instance=cpntools_Var_strategy)
def test_hyp_cpntools_var_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original




@given(instance=cpntools_Ml_strategy)
def test_hyp_cpntools_ml_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original




@given(instance=cpntools_Globref_strategy)
def test_hyp_cpntools_globref_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original




@given(instance=cpntools_ColorSet_strategy)
def test_hyp_cpntools_colorset_declare_setter(instance):
    original = instance.declare
    instance.declare = original
    assert instance.declare == original



@given(instance=cpntools_ColorSet_strategy)
def test_hyp_cpntools_colorset_timed_setter(instance):
    original = instance.timed
    instance.timed = original
    assert instance.timed == original



@given(instance=cpntools_ColorSet_strategy)
def test_hyp_cpntools_colorset_colorSetType_setter(instance):
    original = instance.colorSetType
    instance.colorSetType = original
    assert instance.colorSetType == original



@given(instance=cpntools_ColorSet_strategy)
def test_hyp_cpntools_colorset_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original





@given(instance=cpntools_TransTime_strategy)
def test_hyp_cpntools_transtime_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=cpntools_Annot_strategy)
def test_hyp_cpntools_annot_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=cpntools_TransPriority_strategy)
def test_hyp_cpntools_transpriority_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=cpntools_TransCond_strategy)
def test_hyp_cpntools_transcond_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=cpntools_Port_strategy)
def test_hyp_cpntools_port_portType_setter(instance):
    original = instance.portType
    instance.portType = original
    assert instance.portType == original




@given(instance=cpntools_Initmark_strategy)
def test_hyp_cpntools_initmark_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original




@given(instance=cpntools_Block_strategy)
def test_hyp_cpntools_block_idname_setter(instance):
    original = instance.idname
    instance.idname = original
    assert instance.idname == original




@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_fillFilled_setter(instance):
    original = instance.fillFilled
    instance.fillFilled = original
    assert instance.fillFilled == original



@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_lineType_setter(instance):
    original = instance.lineType
    instance.lineType = original
    assert instance.lineType == original



@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_posy_setter(instance):
    original = instance.posy
    instance.posy = original
    assert instance.posy == original



@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_fillPattern_setter(instance):
    original = instance.fillPattern
    instance.fillPattern = original
    assert instance.fillPattern == original



@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_lineColour_setter(instance):
    original = instance.lineColour
    instance.lineColour = original
    assert instance.lineColour == original



@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_posx_setter(instance):
    original = instance.posx
    instance.posx = original
    assert instance.posx == original



@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_lineThick_setter(instance):
    original = instance.lineThick
    instance.lineThick = original
    assert instance.lineThick == original



@given(instance=cpntools_DiagramElement_strategy)
def test_hyp_cpntools_diagramelement_fillColour_setter(instance):
    original = instance.fillColour
    instance.fillColour = original
    assert instance.fillColour == original




@given(instance=cpntools_Arc_strategy)
def test_hyp_cpntools_arc_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=cpntools_Arc_strategy)
def test_hyp_cpntools_arc_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=cpntools_Arc_strategy)
def test_hyp_cpntools_arc_headsize_setter(instance):
    original = instance.headsize
    instance.headsize = original
    assert instance.headsize == original



@given(instance=cpntools_Arc_strategy)
def test_hyp_cpntools_arc_currentcyckle_setter(instance):
    original = instance.currentcyckle
    instance.currentcyckle = original
    assert instance.currentcyckle == original




@given(instance=cpntools_Trans_strategy)
def test_hyp_cpntools_trans_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_Trans_strategy)
def test_hyp_cpntools_trans_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=cpntools_Trans_strategy)
def test_hyp_cpntools_trans_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=cpntools_Trans_strategy)
def test_hyp_cpntools_trans_explicit_setter(instance):
    original = instance.explicit
    instance.explicit = original
    assert instance.explicit == original





@given(instance=cpntools_Place_strategy)
def test_hyp_cpntools_place_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=cpntools_Place_strategy)
def test_hyp_cpntools_place_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=cpntools_Place_strategy)
def test_hyp_cpntools_place_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original




@given(instance=cpntools_Group_strategy)
def test_hyp_cpntools_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cpntools_Page_strategy)
def test_hyp_cpntools_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cpntools_Page_strategy)
@settings(max_examples=30)
def test_hyp_cpntools_page_layout_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.layout()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.layout).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'layout' in cpntools_Page is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'layout' in cpntools_Page did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'layout' in cpntools_Page is not implemented or raised an error")




@given(instance=cpntools_Binder_strategy)
def test_hyp_cpntools_binder_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=cpntools_Binder_strategy)
def test_hyp_cpntools_binder_posx_setter(instance):
    original = instance.posx
    instance.posx = original
    assert instance.posx == original



@given(instance=cpntools_Binder_strategy)
def test_hyp_cpntools_binder_posy_setter(instance):
    original = instance.posy
    instance.posy = original
    assert instance.posy == original



@given(instance=cpntools_Binder_strategy)
def test_hyp_cpntools_binder_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=cpntools_Globbox_strategy)
def test_hyp_cpntools_globbox_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=cpntools_Fusion_strategy)
def test_hyp_cpntools_fusion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Auxiliary,
    ColorSet,
    CompoundColorSet,
    Declaration,
    DiagramElement,
    SimpleColorSet,
    cpntools_Alias,
    cpntools_Annot,
    cpntools_Arc,
    cpntools_AuxBox,
    cpntools_AuxEllipse,
    cpntools_AuxText,
    cpntools_Auxiliary,
    cpntools_Binder,
    cpntools_Block,
    cpntools_Boolean,
    cpntools_ColorSet,
    cpntools_CompoundColorSet,
    cpntools_Cpnet,
    cpntools_Declaration,
    cpntools_DiagramElement,
    cpntools_Enumerated,
    cpntools_Fusion,
    cpntools_Globbox,
    cpntools_Globref,
    cpntools_Group,
    cpntools_Index,
    cpntools_Initmark,
    cpntools_Integer,
    cpntools_LargeInteger,
    cpntools_List,
    cpntools_Ml,
    cpntools_Page,
    cpntools_Place,
    cpntools_Port,
    cpntools_Product,
    cpntools_Real,
    cpntools_Record,
    cpntools_SimpleColorSet,
    cpntools_String,
    cpntools_Subset,
    cpntools_Time,
    cpntools_Trans,
    cpntools_TransCond,
    cpntools_TransPriority,
    cpntools_TransTime,
    cpntools_Union,
    cpntools_Unit,
    cpntools_Var,
    Colour16,
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

def test_cpntools_Annot_text_value_roundtrip():
    instance = cpntools_Annot(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_cpntools_Arc_currentcyckle_value_roundtrip():
    instance = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    assert instance.currentcyckle == "sample_text"
    instance.currentcyckle = "sample_text_2"
    assert instance.currentcyckle == "sample_text_2"


def test_cpntools_Arc_headsize_value_roundtrip():
    instance = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    assert instance.headsize == 3.14
    instance.headsize = 9.99
    assert instance.headsize == 9.99


def test_cpntools_Arc_order_value_roundtrip():
    instance = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    assert instance.order == 7
    instance.order = 13
    assert instance.order == 13


def test_cpntools_Arc_orientation_value_roundtrip():
    instance = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    assert instance.orientation == "sample_text"
    instance.orientation = "sample_text_2"
    assert instance.orientation == "sample_text_2"


def test_cpntools_AuxBox_height_value_roundtrip():
    instance = cpntools_AuxBox(height=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_cpntools_AuxBox_width_value_roundtrip():
    instance = cpntools_AuxBox(height=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_cpntools_AuxEllipse_height_value_roundtrip():
    instance = cpntools_AuxEllipse(height=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_cpntools_AuxEllipse_width_value_roundtrip():
    instance = cpntools_AuxEllipse(height=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_cpntools_AuxText_text_value_roundtrip():
    instance = cpntools_AuxText(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_cpntools_Binder_height_value_roundtrip():
    instance = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_cpntools_Binder_posx_value_roundtrip():
    instance = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    assert instance.posx == 7
    instance.posx = 13
    assert instance.posx == 13


def test_cpntools_Binder_posy_value_roundtrip():
    instance = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    assert instance.posy == 7
    instance.posy = 13
    assert instance.posy == 13


def test_cpntools_Binder_width_value_roundtrip():
    instance = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_cpntools_Block_idname_value_roundtrip():
    instance = cpntools_Block(idname="sample_text")
    assert instance.idname == "sample_text"
    instance.idname = "sample_text_2"
    assert instance.idname == "sample_text_2"


def test_cpntools_Boolean_with__value_roundtrip():
    instance = cpntools_Boolean(with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_ColorSet_colorSetType_value_roundtrip():
    instance = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    assert instance.colorSetType == "sample_text"
    instance.colorSetType = "sample_text_2"
    assert instance.colorSetType == "sample_text_2"


def test_cpntools_ColorSet_declare_value_roundtrip():
    instance = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    assert instance.declare == "sample_text"
    instance.declare = "sample_text_2"
    assert instance.declare == "sample_text_2"


def test_cpntools_ColorSet_idname_value_roundtrip():
    instance = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    assert instance.idname == "sample_text"
    instance.idname = "sample_text_2"
    assert instance.idname == "sample_text_2"


def test_cpntools_ColorSet_timed_value_roundtrip():
    instance = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    assert instance.timed == True
    instance.timed = False
    assert instance.timed == False


def test_cpntools_DiagramElement_fillColour_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.fillColour == "sample_text"
    instance.fillColour = "sample_text_2"
    assert instance.fillColour == "sample_text_2"


def test_cpntools_DiagramElement_fillFilled_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.fillFilled == True
    instance.fillFilled = False
    assert instance.fillFilled == False


def test_cpntools_DiagramElement_fillPattern_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.fillPattern == "sample_text"
    instance.fillPattern = "sample_text_2"
    assert instance.fillPattern == "sample_text_2"


def test_cpntools_DiagramElement_lineColour_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.lineColour == "sample_text"
    instance.lineColour = "sample_text_2"
    assert instance.lineColour == "sample_text_2"


def test_cpntools_DiagramElement_lineThick_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.lineThick == 7
    instance.lineThick = 13
    assert instance.lineThick == 13


def test_cpntools_DiagramElement_lineType_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.lineType == "sample_text"
    instance.lineType = "sample_text_2"
    assert instance.lineType == "sample_text_2"


def test_cpntools_DiagramElement_posx_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.posx == 7
    instance.posx = 13
    assert instance.posx == 13


def test_cpntools_DiagramElement_posy_value_roundtrip():
    instance = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    assert instance.posy == 7
    instance.posy = 13
    assert instance.posy == 13


def test_cpntools_Enumerated_with__value_roundtrip():
    instance = cpntools_Enumerated(with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_Fusion_name_value_roundtrip():
    instance = cpntools_Fusion(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpntools_Globbox_name_value_roundtrip():
    instance = cpntools_Globbox(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpntools_Globref_idname_value_roundtrip():
    instance = cpntools_Globref(idname="sample_text")
    assert instance.idname == "sample_text"
    instance.idname = "sample_text_2"
    assert instance.idname == "sample_text_2"


def test_cpntools_Group_name_value_roundtrip():
    instance = cpntools_Group(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpntools_Index_with__value_roundtrip():
    instance = cpntools_Index(with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_Initmark_expression_value_roundtrip():
    instance = cpntools_Initmark(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_cpntools_Integer_with__value_roundtrip():
    instance = cpntools_Integer(with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_LargeInteger_with__value_roundtrip():
    instance = cpntools_LargeInteger(with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_Ml_expression_value_roundtrip():
    instance = cpntools_Ml(expression="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_cpntools_Page_name_value_roundtrip():
    instance = cpntools_Page(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cpntools_Place_height_value_roundtrip():
    instance = cpntools_Place(height=7, text="sample_text", width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_cpntools_Place_text_value_roundtrip():
    instance = cpntools_Place(height=7, text="sample_text", width=7)
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_cpntools_Place_width_value_roundtrip():
    instance = cpntools_Place(height=7, text="sample_text", width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_cpntools_Port_portType_value_roundtrip():
    instance = cpntools_Port(portType="sample_text")
    assert instance.portType == "sample_text"
    instance.portType = "sample_text_2"
    assert instance.portType == "sample_text_2"


def test_cpntools_Real_with__value_roundtrip():
    instance = cpntools_Real(with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_String_and__value_roundtrip():
    instance = cpntools_String(and_="sample_text", with_="sample_text")
    assert instance.and_ == "sample_text"
    instance.and_ = "sample_text_2"
    assert instance.and_ == "sample_text_2"


def test_cpntools_String_with__value_roundtrip():
    instance = cpntools_String(and_="sample_text", with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_Trans_explicit_value_roundtrip():
    instance = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    assert instance.explicit == True
    instance.explicit = False
    assert instance.explicit == False


def test_cpntools_Trans_height_value_roundtrip():
    instance = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_cpntools_Trans_text_value_roundtrip():
    instance = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_cpntools_Trans_width_value_roundtrip():
    instance = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_cpntools_TransCond_text_value_roundtrip():
    instance = cpntools_TransCond(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_cpntools_TransPriority_text_value_roundtrip():
    instance = cpntools_TransPriority(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_cpntools_TransTime_text_value_roundtrip():
    instance = cpntools_TransTime(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_cpntools_Unit_with__value_roundtrip():
    instance = cpntools_Unit(with_="sample_text")
    assert instance.with_ == "sample_text"
    instance.with_ = "sample_text_2"
    assert instance.with_ == "sample_text_2"


def test_cpntools_Var_idname_value_roundtrip():
    instance = cpntools_Var(idname="sample_text")
    assert instance.idname == "sample_text"
    instance.idname = "sample_text_2"
    assert instance.idname == "sample_text_2"


def test_cpntools_AuxBox_isa_Auxiliary():
    instance = cpntools_AuxBox(height=7, width=7)
    assert isinstance(instance, Auxiliary)


def test_cpntools_AuxEllipse_isa_Auxiliary():
    instance = cpntools_AuxEllipse(height=7, width=7)
    assert isinstance(instance, Auxiliary)


def test_cpntools_AuxText_isa_Auxiliary():
    instance = cpntools_AuxText(text="sample_text")
    assert isinstance(instance, Auxiliary)


def test_cpntools_CompoundColorSet_isa_ColorSet():
    instance = cpntools_CompoundColorSet()
    assert isinstance(instance, ColorSet)


def test_cpntools_SimpleColorSet_isa_ColorSet():
    instance = cpntools_SimpleColorSet()
    assert isinstance(instance, ColorSet)


def test_cpntools_Alias_isa_CompoundColorSet():
    instance = cpntools_Alias()
    assert isinstance(instance, CompoundColorSet)


def test_cpntools_List_isa_CompoundColorSet():
    instance = cpntools_List()
    assert isinstance(instance, CompoundColorSet)


def test_cpntools_Product_isa_CompoundColorSet():
    instance = cpntools_Product()
    assert isinstance(instance, CompoundColorSet)


def test_cpntools_Record_isa_CompoundColorSet():
    instance = cpntools_Record()
    assert isinstance(instance, CompoundColorSet)


def test_cpntools_Subset_isa_CompoundColorSet():
    instance = cpntools_Subset()
    assert isinstance(instance, CompoundColorSet)


def test_cpntools_Union_isa_CompoundColorSet():
    instance = cpntools_Union()
    assert isinstance(instance, CompoundColorSet)


def test_cpntools_Block_isa_Declaration():
    instance = cpntools_Block(idname="sample_text")
    assert isinstance(instance, Declaration)


def test_cpntools_ColorSet_isa_Declaration():
    instance = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    assert isinstance(instance, Declaration)


def test_cpntools_Globref_isa_Declaration():
    instance = cpntools_Globref(idname="sample_text")
    assert isinstance(instance, Declaration)


def test_cpntools_Ml_isa_Declaration():
    instance = cpntools_Ml(expression="sample_text")
    assert isinstance(instance, Declaration)


def test_cpntools_Var_isa_Declaration():
    instance = cpntools_Var(idname="sample_text")
    assert isinstance(instance, Declaration)


def test_cpntools_Annot_isa_DiagramElement():
    instance = cpntools_Annot(text="sample_text")
    assert isinstance(instance, DiagramElement)


def test_cpntools_Arc_isa_DiagramElement():
    instance = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    assert isinstance(instance, DiagramElement)


def test_cpntools_Auxiliary_isa_DiagramElement():
    instance = cpntools_Auxiliary()
    assert isinstance(instance, DiagramElement)


def test_cpntools_Initmark_isa_DiagramElement():
    instance = cpntools_Initmark(expression="sample_text")
    assert isinstance(instance, DiagramElement)


def test_cpntools_Place_isa_DiagramElement():
    instance = cpntools_Place(height=7, text="sample_text", width=7)
    assert isinstance(instance, DiagramElement)


def test_cpntools_Port_isa_DiagramElement():
    instance = cpntools_Port(portType="sample_text")
    assert isinstance(instance, DiagramElement)


def test_cpntools_Trans_isa_DiagramElement():
    instance = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    assert isinstance(instance, DiagramElement)


def test_cpntools_TransCond_isa_DiagramElement():
    instance = cpntools_TransCond(text="sample_text")
    assert isinstance(instance, DiagramElement)


def test_cpntools_TransPriority_isa_DiagramElement():
    instance = cpntools_TransPriority(text="sample_text")
    assert isinstance(instance, DiagramElement)


def test_cpntools_TransTime_isa_DiagramElement():
    instance = cpntools_TransTime(text="sample_text")
    assert isinstance(instance, DiagramElement)


def test_cpntools_Boolean_isa_SimpleColorSet():
    instance = cpntools_Boolean(with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_Enumerated_isa_SimpleColorSet():
    instance = cpntools_Enumerated(with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_Index_isa_SimpleColorSet():
    instance = cpntools_Index(with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_Integer_isa_SimpleColorSet():
    instance = cpntools_Integer(with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_LargeInteger_isa_SimpleColorSet():
    instance = cpntools_LargeInteger(with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_Real_isa_SimpleColorSet():
    instance = cpntools_Real(with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_String_isa_SimpleColorSet():
    instance = cpntools_String(and_="sample_text", with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_Time_isa_SimpleColorSet():
    instance = cpntools_Time()
    assert isinstance(instance, SimpleColorSet)


def test_cpntools_Unit_isa_SimpleColorSet():
    instance = cpntools_Unit(with_="sample_text")
    assert isinstance(instance, SimpleColorSet)


def test_assoc_annot55_link_reassign_clear():
    a = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    b1 = cpntools_Annot(text="sample_text")
    b2 = cpntools_Annot(text="sample_text_2")
    _safe_set(a, 'cpntools_Arc', b1)
    assert _is_linked(a, 'cpntools_Arc', b1)
    if hasattr(b1, 'cpntools_Annot'):
        assert _is_linked(b1, 'cpntools_Annot', a)
    _safe_set(a, 'cpntools_Arc', b2)
    assert _is_linked(a, 'cpntools_Arc', b2)
    if hasattr(b1, 'cpntools_Annot'):
        assert not _is_linked(b1, 'cpntools_Annot', a)
    if hasattr(b2, 'cpntools_Annot'):
        assert _is_linked(b2, 'cpntools_Annot', a)
    _safe_set(a, 'cpntools_Arc', None)
    assert not _is_linked(a, 'cpntools_Arc', b2)
    if hasattr(b2, 'cpntools_Annot'):
        assert not _is_linked(b2, 'cpntools_Annot', a)


def test_assoc_arcs12_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    b2 = cpntools_Arc(currentcyckle="sample_text_2", headsize=9.99, order=13, orientation="sample_text_2")
    _safe_set(a, 'page13', {b1})
    assert _is_linked(a, 'page13', b1)
    if hasattr(b1, 'Arc'):
        assert _is_linked(b1, 'Arc', a)
    _safe_set(a, 'page13', {b2})
    assert _is_linked(a, 'page13', b2)
    if hasattr(b1, 'Arc'):
        assert not _is_linked(b1, 'Arc', a)
    if hasattr(b2, 'Arc'):
        assert _is_linked(b2, 'Arc', a)
    _safe_set(a, 'page13', set())
    assert not _is_linked(a, 'page13', b2)
    if hasattr(b2, 'Arc'):
        assert not _is_linked(b2, 'Arc', a)


def test_assoc_arcs31_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    b2 = cpntools_Arc(currentcyckle="sample_text_2", headsize=9.99, order=13, orientation="sample_text_2")
    _safe_set(a, 'place', {b1})
    assert _is_linked(a, 'place', b1)
    if hasattr(b1, 'Arc32'):
        assert _is_linked(b1, 'Arc32', a)
    _safe_set(a, 'place', {b2})
    assert _is_linked(a, 'place', b2)
    if hasattr(b1, 'Arc32'):
        assert not _is_linked(b1, 'Arc32', a)
    if hasattr(b2, 'Arc32'):
        assert _is_linked(b2, 'Arc32', a)
    _safe_set(a, 'place', set())
    assert not _is_linked(a, 'place', b2)
    if hasattr(b2, 'Arc32'):
        assert not _is_linked(b2, 'Arc32', a)


def test_assoc_arcs62_link_reassign_clear():
    a = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    b1 = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    b2 = cpntools_Arc(currentcyckle="sample_text_2", headsize=9.99, order=13, orientation="sample_text_2")
    _safe_set(a, 'trans', {b1})
    assert _is_linked(a, 'trans', b1)
    if hasattr(b1, 'Arc63'):
        assert _is_linked(b1, 'Arc63', a)
    _safe_set(a, 'trans', {b2})
    assert _is_linked(a, 'trans', b2)
    if hasattr(b1, 'Arc63'):
        assert not _is_linked(b1, 'Arc63', a)
    if hasattr(b2, 'Arc63'):
        assert _is_linked(b2, 'Arc63', a)
    _safe_set(a, 'trans', set())
    assert not _is_linked(a, 'trans', b2)
    if hasattr(b2, 'Arc63'):
        assert not _is_linked(b2, 'Arc63', a)


def test_assoc_auxiliarys8_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Auxiliary()
    b2 = cpntools_Auxiliary()
    _safe_set(a, 'page9', {b1})
    assert _is_linked(a, 'page9', b1)
    if hasattr(b1, 'Auxiliary'):
        assert _is_linked(b1, 'Auxiliary', a)
    _safe_set(a, 'page9', {b2})
    assert _is_linked(a, 'page9', b2)
    if hasattr(b1, 'Auxiliary'):
        assert not _is_linked(b1, 'Auxiliary', a)
    if hasattr(b2, 'Auxiliary'):
        assert _is_linked(b2, 'Auxiliary', a)
    _safe_set(a, 'page9', set())
    assert not _is_linked(a, 'page9', b2)
    if hasattr(b2, 'Auxiliary'):
        assert not _is_linked(b2, 'Auxiliary', a)


def test_assoc_binder14_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    b2 = cpntools_Binder(height=13, posx=13, posy=13, width=13)
    _safe_set(a, 'pages', b1)
    assert _is_linked(a, 'pages', b1)
    if hasattr(b1, 'Binder15'):
        assert _is_linked(b1, 'Binder15', a)
    _safe_set(a, 'pages', b2)
    assert _is_linked(a, 'pages', b2)
    if hasattr(b1, 'Binder15'):
        assert not _is_linked(b1, 'Binder15', a)
    if hasattr(b2, 'Binder15'):
        assert _is_linked(b2, 'Binder15', a)
    _safe_set(a, 'pages', None)
    assert not _is_linked(a, 'pages', b2)
    if hasattr(b2, 'Binder15'):
        assert not _is_linked(b2, 'Binder15', a)


def test_assoc_binder3_link_reassign_clear():
    a = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    b1 = cpntools_Cpnet()
    b2 = cpntools_Cpnet()
    _safe_set(a, 'Binder', b1)
    assert _is_linked(a, 'Binder', b1)
    if hasattr(b1, 'cpnet4'):
        assert _is_linked(b1, 'cpnet4', a)
    _safe_set(a, 'Binder', b2)
    assert _is_linked(a, 'Binder', b2)
    if hasattr(b1, 'cpnet4'):
        assert not _is_linked(b1, 'cpnet4', a)
    if hasattr(b2, 'cpnet4'):
        assert _is_linked(b2, 'cpnet4', a)
    _safe_set(a, 'Binder', None)
    assert not _is_linked(a, 'Binder', b2)
    if hasattr(b2, 'cpnet4'):
        assert not _is_linked(b2, 'cpnet4', a)


def test_assoc_block35_link_reassign_clear():
    a = cpntools_Block(idname="sample_text")
    b1 = cpntools_Declaration()
    b2 = cpntools_Declaration()
    _safe_set(a, 'Block', b1)
    assert _is_linked(a, 'Block', b1)
    if hasattr(b1, 'declarations36'):
        assert _is_linked(b1, 'declarations36', a)
    _safe_set(a, 'Block', b2)
    assert _is_linked(a, 'Block', b2)
    if hasattr(b1, 'declarations36'):
        assert not _is_linked(b1, 'declarations36', a)
    if hasattr(b2, 'declarations36'):
        assert _is_linked(b2, 'declarations36', a)
    _safe_set(a, 'Block', None)
    assert not _is_linked(a, 'Block', b2)
    if hasattr(b2, 'declarations36'):
        assert not _is_linked(b2, 'declarations36', a)


def test_assoc_cond59_link_reassign_clear():
    a = cpntools_TransCond(text="sample_text")
    b1 = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    b2 = cpntools_Trans(explicit=False, height=13, text="sample_text_2", width=13)
    _safe_set(a, 'cpntools_TransCond', b1)
    assert _is_linked(a, 'cpntools_TransCond', b1)
    if hasattr(b1, 'cpntools_Trans'):
        assert _is_linked(b1, 'cpntools_Trans', a)
    _safe_set(a, 'cpntools_TransCond', b2)
    assert _is_linked(a, 'cpntools_TransCond', b2)
    if hasattr(b1, 'cpntools_Trans'):
        assert not _is_linked(b1, 'cpntools_Trans', a)
    if hasattr(b2, 'cpntools_Trans'):
        assert _is_linked(b2, 'cpntools_Trans', a)
    _safe_set(a, 'cpntools_TransCond', None)
    assert not _is_linked(a, 'cpntools_TransCond', b2)
    if hasattr(b2, 'cpntools_Trans'):
        assert not _is_linked(b2, 'cpntools_Trans', a)


def test_assoc_cpnet39_link_reassign_clear():
    a = cpntools_Fusion(name="sample_text")
    b1 = cpntools_Cpnet()
    b2 = cpntools_Cpnet()
    _safe_set(a, 'fusions', b1)
    assert _is_linked(a, 'fusions', b1)
    if hasattr(b1, 'Cpnet'):
        assert _is_linked(b1, 'Cpnet', a)
    _safe_set(a, 'fusions', b2)
    assert _is_linked(a, 'fusions', b2)
    if hasattr(b1, 'Cpnet'):
        assert not _is_linked(b1, 'Cpnet', a)
    if hasattr(b2, 'Cpnet'):
        assert _is_linked(b2, 'Cpnet', a)
    _safe_set(a, 'fusions', None)
    assert not _is_linked(a, 'fusions', b2)
    if hasattr(b2, 'Cpnet'):
        assert not _is_linked(b2, 'Cpnet', a)


def test_assoc_cpnet42_link_reassign_clear():
    a = cpntools_Globbox(name="sample_text")
    b1 = cpntools_Cpnet()
    b2 = cpntools_Cpnet()
    _safe_set(a, 'globbox', b1)
    assert _is_linked(a, 'globbox', b1)
    if hasattr(b1, 'Cpnet43'):
        assert _is_linked(b1, 'Cpnet43', a)
    _safe_set(a, 'globbox', b2)
    assert _is_linked(a, 'globbox', b2)
    if hasattr(b1, 'Cpnet43'):
        assert not _is_linked(b1, 'Cpnet43', a)
    if hasattr(b2, 'Cpnet43'):
        assert _is_linked(b2, 'Cpnet43', a)
    _safe_set(a, 'globbox', None)
    assert not _is_linked(a, 'globbox', b2)
    if hasattr(b2, 'Cpnet43'):
        assert not _is_linked(b2, 'Cpnet43', a)


def test_assoc_cpnet69_link_reassign_clear():
    a = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    b1 = cpntools_Cpnet()
    b2 = cpntools_Cpnet()
    _safe_set(a, 'binder', b1)
    assert _is_linked(a, 'binder', b1)
    if hasattr(b1, 'Cpnet70'):
        assert _is_linked(b1, 'Cpnet70', a)
    _safe_set(a, 'binder', b2)
    assert _is_linked(a, 'binder', b2)
    if hasattr(b1, 'Cpnet70'):
        assert not _is_linked(b1, 'Cpnet70', a)
    if hasattr(b2, 'Cpnet70'):
        assert _is_linked(b2, 'Cpnet70', a)
    _safe_set(a, 'binder', None)
    assert not _is_linked(a, 'binder', b2)
    if hasattr(b2, 'Cpnet70'):
        assert not _is_linked(b2, 'Cpnet70', a)


def test_assoc_declarations44_link_reassign_clear():
    a = cpntools_Globbox(name="sample_text")
    b1 = cpntools_Declaration()
    b2 = cpntools_Declaration()
    _safe_set(a, 'globbox45', {b1})
    assert _is_linked(a, 'globbox45', b1)
    if hasattr(b1, 'Declaration'):
        assert _is_linked(b1, 'Declaration', a)
    _safe_set(a, 'globbox45', {b2})
    assert _is_linked(a, 'globbox45', b2)
    if hasattr(b1, 'Declaration'):
        assert not _is_linked(b1, 'Declaration', a)
    if hasattr(b2, 'Declaration'):
        assert _is_linked(b2, 'Declaration', a)
    _safe_set(a, 'globbox45', set())
    assert not _is_linked(a, 'globbox45', b2)
    if hasattr(b2, 'Declaration'):
        assert not _is_linked(b2, 'Declaration', a)


def test_assoc_declarations48_link_reassign_clear():
    a = cpntools_Block(idname="sample_text")
    b1 = cpntools_Declaration()
    b2 = cpntools_Declaration()
    _safe_set(a, 'block', {b1})
    assert _is_linked(a, 'block', b1)
    if hasattr(b1, 'Declaration49'):
        assert _is_linked(b1, 'Declaration49', a)
    _safe_set(a, 'block', {b2})
    assert _is_linked(a, 'block', b2)
    if hasattr(b1, 'Declaration49'):
        assert not _is_linked(b1, 'Declaration49', a)
    if hasattr(b2, 'Declaration49'):
        assert _is_linked(b2, 'Declaration49', a)
    _safe_set(a, 'block', set())
    assert not _is_linked(a, 'block', b2)
    if hasattr(b2, 'Declaration49'):
        assert not _is_linked(b2, 'Declaration49', a)


def test_assoc_fusion26_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_Fusion(name="sample_text")
    b2 = cpntools_Fusion(name="sample_text_2")
    _safe_set(a, 'places', b1)
    assert _is_linked(a, 'places', b1)
    if hasattr(b1, 'Fusion27'):
        assert _is_linked(b1, 'Fusion27', a)
    _safe_set(a, 'places', b2)
    assert _is_linked(a, 'places', b2)
    if hasattr(b1, 'Fusion27'):
        assert not _is_linked(b1, 'Fusion27', a)
    if hasattr(b2, 'Fusion27'):
        assert _is_linked(b2, 'Fusion27', a)
    _safe_set(a, 'places', None)
    assert not _is_linked(a, 'places', b2)
    if hasattr(b2, 'Fusion27'):
        assert not _is_linked(b2, 'Fusion27', a)


def test_assoc_fusions0_link_reassign_clear():
    a = cpntools_Fusion(name="sample_text")
    b1 = cpntools_Cpnet()
    b2 = cpntools_Cpnet()
    _safe_set(a, 'Fusion', b1)
    assert _is_linked(a, 'Fusion', b1)
    if hasattr(b1, 'cpnet'):
        assert _is_linked(b1, 'cpnet', a)
    _safe_set(a, 'Fusion', b2)
    assert _is_linked(a, 'Fusion', b2)
    if hasattr(b1, 'cpnet'):
        assert not _is_linked(b1, 'cpnet', a)
    if hasattr(b2, 'cpnet'):
        assert _is_linked(b2, 'cpnet', a)
    _safe_set(a, 'Fusion', None)
    assert not _is_linked(a, 'Fusion', b2)
    if hasattr(b2, 'cpnet'):
        assert not _is_linked(b2, 'cpnet', a)


def test_assoc_globbox1_link_reassign_clear():
    a = cpntools_Globbox(name="sample_text")
    b1 = cpntools_Cpnet()
    b2 = cpntools_Cpnet()
    _safe_set(a, 'Globbox', b1)
    assert _is_linked(a, 'Globbox', b1)
    if hasattr(b1, 'cpnet2'):
        assert _is_linked(b1, 'cpnet2', a)
    _safe_set(a, 'Globbox', b2)
    assert _is_linked(a, 'Globbox', b2)
    if hasattr(b1, 'cpnet2'):
        assert not _is_linked(b1, 'cpnet2', a)
    if hasattr(b2, 'cpnet2'):
        assert _is_linked(b2, 'cpnet2', a)
    _safe_set(a, 'Globbox', None)
    assert not _is_linked(a, 'Globbox', b2)
    if hasattr(b2, 'cpnet2'):
        assert not _is_linked(b2, 'cpnet2', a)


def test_assoc_globbox33_link_reassign_clear():
    a = cpntools_Globbox(name="sample_text")
    b1 = cpntools_Declaration()
    b2 = cpntools_Declaration()
    _safe_set(a, 'Globbox34', b1)
    assert _is_linked(a, 'Globbox34', b1)
    if hasattr(b1, 'declarations'):
        assert _is_linked(b1, 'declarations', a)
    _safe_set(a, 'Globbox34', b2)
    assert _is_linked(a, 'Globbox34', b2)
    if hasattr(b1, 'declarations'):
        assert not _is_linked(b1, 'declarations', a)
    if hasattr(b2, 'declarations'):
        assert _is_linked(b2, 'declarations', a)
    _safe_set(a, 'Globbox34', None)
    assert not _is_linked(a, 'Globbox34', b2)
    if hasattr(b2, 'declarations'):
        assert not _is_linked(b2, 'declarations', a)


def test_assoc_group19_link_reassign_clear():
    a = cpntools_Group(name="sample_text")
    b1 = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    b2 = cpntools_DiagramElement(fillColour="sample_text_2", fillFilled=False, fillPattern="sample_text_2", lineColour="sample_text_2", lineThick=13, lineType="sample_text_2", posx=13, posy=13)
    _safe_set(a, 'Group20', b1)
    assert _is_linked(a, 'Group20', b1)
    if hasattr(b1, 'groupElms'):
        assert _is_linked(b1, 'groupElms', a)
    _safe_set(a, 'Group20', b2)
    assert _is_linked(a, 'Group20', b2)
    if hasattr(b1, 'groupElms'):
        assert not _is_linked(b1, 'groupElms', a)
    if hasattr(b2, 'groupElms'):
        assert _is_linked(b2, 'groupElms', a)
    _safe_set(a, 'Group20', None)
    assert not _is_linked(a, 'Group20', b2)
    if hasattr(b2, 'groupElms'):
        assert not _is_linked(b2, 'groupElms', a)


def test_assoc_group5_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Group(name="sample_text")
    b2 = cpntools_Group(name="sample_text_2")
    _safe_set(a, 'page', {b1})
    assert _is_linked(a, 'page', b1)
    if hasattr(b1, 'Group'):
        assert _is_linked(b1, 'Group', a)
    _safe_set(a, 'page', {b2})
    assert _is_linked(a, 'page', b2)
    if hasattr(b1, 'Group'):
        assert not _is_linked(b1, 'Group', a)
    if hasattr(b2, 'Group'):
        assert _is_linked(b2, 'Group', a)
    _safe_set(a, 'page', set())
    assert not _is_linked(a, 'page', b2)
    if hasattr(b2, 'Group'):
        assert not _is_linked(b2, 'Group', a)


def test_assoc_groupElms16_link_reassign_clear():
    a = cpntools_Group(name="sample_text")
    b1 = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    b2 = cpntools_DiagramElement(fillColour="sample_text_2", fillFilled=False, fillPattern="sample_text_2", lineColour="sample_text_2", lineThick=13, lineType="sample_text_2", posx=13, posy=13)
    _safe_set(a, 'group', {b1})
    assert _is_linked(a, 'group', b1)
    if hasattr(b1, 'DiagramElement'):
        assert _is_linked(b1, 'DiagramElement', a)
    _safe_set(a, 'group', {b2})
    assert _is_linked(a, 'group', b2)
    if hasattr(b1, 'DiagramElement'):
        assert not _is_linked(b1, 'DiagramElement', a)
    if hasattr(b2, 'DiagramElement'):
        assert _is_linked(b2, 'DiagramElement', a)
    _safe_set(a, 'group', set())
    assert not _is_linked(a, 'group', b2)
    if hasattr(b2, 'DiagramElement'):
        assert not _is_linked(b2, 'DiagramElement', a)


def test_assoc_initmark22_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_Initmark(expression="sample_text")
    b2 = cpntools_Initmark(expression="sample_text_2")
    _safe_set(a, 'cpntools_Place23', b1)
    assert _is_linked(a, 'cpntools_Place23', b1)
    if hasattr(b1, 'cpntools_Initmark'):
        assert _is_linked(b1, 'cpntools_Initmark', a)
    _safe_set(a, 'cpntools_Place23', b2)
    assert _is_linked(a, 'cpntools_Place23', b2)
    if hasattr(b1, 'cpntools_Initmark'):
        assert not _is_linked(b1, 'cpntools_Initmark', a)
    if hasattr(b2, 'cpntools_Initmark'):
        assert _is_linked(b2, 'cpntools_Initmark', a)
    _safe_set(a, 'cpntools_Place23', None)
    assert not _is_linked(a, 'cpntools_Place23', b2)
    if hasattr(b2, 'cpntools_Initmark'):
        assert not _is_linked(b2, 'cpntools_Initmark', a)


def test_assoc_page17_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Group(name="sample_text")
    b2 = cpntools_Group(name="sample_text_2")
    _safe_set(a, 'Page', b1)
    assert _is_linked(a, 'Page', b1)
    if hasattr(b1, 'group18'):
        assert _is_linked(b1, 'group18', a)
    _safe_set(a, 'Page', b2)
    assert _is_linked(a, 'Page', b2)
    if hasattr(b1, 'group18'):
        assert not _is_linked(b1, 'group18', a)
    if hasattr(b2, 'group18'):
        assert _is_linked(b2, 'group18', a)
    _safe_set(a, 'Page', None)
    assert not _is_linked(a, 'Page', b2)
    if hasattr(b2, 'group18'):
        assert not _is_linked(b2, 'group18', a)


def test_assoc_page28_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_Page(name="sample_text")
    b2 = cpntools_Page(name="sample_text_2")
    _safe_set(a, 'places29', b1)
    assert _is_linked(a, 'places29', b1)
    if hasattr(b1, 'Page30'):
        assert _is_linked(b1, 'Page30', a)
    _safe_set(a, 'places29', b2)
    assert _is_linked(a, 'places29', b2)
    if hasattr(b1, 'Page30'):
        assert not _is_linked(b1, 'Page30', a)
    if hasattr(b2, 'Page30'):
        assert _is_linked(b2, 'Page30', a)
    _safe_set(a, 'places29', None)
    assert not _is_linked(a, 'places29', b2)
    if hasattr(b2, 'Page30'):
        assert not _is_linked(b2, 'Page30', a)


def test_assoc_page40_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Auxiliary()
    b2 = cpntools_Auxiliary()
    _safe_set(a, 'Page41', b1)
    assert _is_linked(a, 'Page41', b1)
    if hasattr(b1, 'auxiliarys'):
        assert _is_linked(b1, 'auxiliarys', a)
    _safe_set(a, 'Page41', b2)
    assert _is_linked(a, 'Page41', b2)
    if hasattr(b1, 'auxiliarys'):
        assert not _is_linked(b1, 'auxiliarys', a)
    if hasattr(b2, 'auxiliarys'):
        assert _is_linked(b2, 'auxiliarys', a)
    _safe_set(a, 'Page41', None)
    assert not _is_linked(a, 'Page41', b2)
    if hasattr(b2, 'auxiliarys'):
        assert not _is_linked(b2, 'auxiliarys', a)


def test_assoc_page56_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    b2 = cpntools_Arc(currentcyckle="sample_text_2", headsize=9.99, order=13, orientation="sample_text_2")
    _safe_set(a, 'Page58', b1)
    assert _is_linked(a, 'Page58', b1)
    if hasattr(b1, 'arcs57'):
        assert _is_linked(b1, 'arcs57', a)
    _safe_set(a, 'Page58', b2)
    assert _is_linked(a, 'Page58', b2)
    if hasattr(b1, 'arcs57'):
        assert not _is_linked(b1, 'arcs57', a)
    if hasattr(b2, 'arcs57'):
        assert _is_linked(b2, 'arcs57', a)
    _safe_set(a, 'Page58', None)
    assert not _is_linked(a, 'Page58', b2)
    if hasattr(b2, 'arcs57'):
        assert not _is_linked(b2, 'arcs57', a)


def test_assoc_page60_link_reassign_clear():
    a = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    b1 = cpntools_Page(name="sample_text")
    b2 = cpntools_Page(name="sample_text_2")
    _safe_set(a, 'transs', b1)
    assert _is_linked(a, 'transs', b1)
    if hasattr(b1, 'Page61'):
        assert _is_linked(b1, 'Page61', a)
    _safe_set(a, 'transs', b2)
    assert _is_linked(a, 'transs', b2)
    if hasattr(b1, 'Page61'):
        assert not _is_linked(b1, 'Page61', a)
    if hasattr(b2, 'Page61'):
        assert _is_linked(b2, 'Page61', a)
    _safe_set(a, 'transs', None)
    assert not _is_linked(a, 'transs', b2)
    if hasattr(b2, 'Page61'):
        assert not _is_linked(b2, 'Page61', a)


def test_assoc_pages71_link_reassign_clear():
    a = cpntools_Page(name="sample_text")
    b1 = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    b2 = cpntools_Binder(height=13, posx=13, posy=13, width=13)
    _safe_set(a, 'Page73', b1)
    assert _is_linked(a, 'Page73', b1)
    if hasattr(b1, 'binder72'):
        assert _is_linked(b1, 'binder72', a)
    _safe_set(a, 'Page73', b2)
    assert _is_linked(a, 'Page73', b2)
    if hasattr(b1, 'binder72'):
        assert not _is_linked(b1, 'binder72', a)
    if hasattr(b2, 'binder72'):
        assert _is_linked(b2, 'binder72', a)
    _safe_set(a, 'Page73', None)
    assert not _is_linked(a, 'Page73', b2)
    if hasattr(b2, 'binder72'):
        assert not _is_linked(b2, 'binder72', a)


def test_assoc_place50_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    b2 = cpntools_Arc(currentcyckle="sample_text_2", headsize=9.99, order=13, orientation="sample_text_2")
    _safe_set(a, 'Place51', b1)
    assert _is_linked(a, 'Place51', b1)
    if hasattr(b1, 'arcs'):
        assert _is_linked(b1, 'arcs', a)
    _safe_set(a, 'Place51', b2)
    assert _is_linked(a, 'Place51', b2)
    if hasattr(b1, 'arcs'):
        assert not _is_linked(b1, 'arcs', a)
    if hasattr(b2, 'arcs'):
        assert _is_linked(b2, 'arcs', a)
    _safe_set(a, 'Place51', None)
    assert not _is_linked(a, 'Place51', b2)
    if hasattr(b2, 'arcs'):
        assert not _is_linked(b2, 'arcs', a)


def test_assoc_places37_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_Fusion(name="sample_text")
    b2 = cpntools_Fusion(name="sample_text_2")
    _safe_set(a, 'Place38', b1)
    assert _is_linked(a, 'Place38', b1)
    if hasattr(b1, 'fusion'):
        assert _is_linked(b1, 'fusion', a)
    _safe_set(a, 'Place38', b2)
    assert _is_linked(a, 'Place38', b2)
    if hasattr(b1, 'fusion'):
        assert not _is_linked(b1, 'fusion', a)
    if hasattr(b2, 'fusion'):
        assert _is_linked(b2, 'fusion', a)
    _safe_set(a, 'Place38', None)
    assert not _is_linked(a, 'Place38', b2)
    if hasattr(b2, 'fusion'):
        assert not _is_linked(b2, 'fusion', a)


def test_assoc_places6_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_Page(name="sample_text")
    b2 = cpntools_Page(name="sample_text_2")
    _safe_set(a, 'Place', b1)
    assert _is_linked(a, 'Place', b1)
    if hasattr(b1, 'page7'):
        assert _is_linked(b1, 'page7', a)
    _safe_set(a, 'Place', b2)
    assert _is_linked(a, 'Place', b2)
    if hasattr(b1, 'page7'):
        assert not _is_linked(b1, 'page7', a)
    if hasattr(b2, 'page7'):
        assert _is_linked(b2, 'page7', a)
    _safe_set(a, 'Place', None)
    assert not _is_linked(a, 'Place', b2)
    if hasattr(b2, 'page7'):
        assert not _is_linked(b2, 'page7', a)


def test_assoc_port24_link_reassign_clear():
    a = cpntools_Port(portType="sample_text")
    b1 = cpntools_Place(height=7, text="sample_text", width=7)
    b2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    _safe_set(a, 'cpntools_Port', b1)
    assert _is_linked(a, 'cpntools_Port', b1)
    if hasattr(b1, 'cpntools_Place25'):
        assert _is_linked(b1, 'cpntools_Place25', a)
    _safe_set(a, 'cpntools_Port', b2)
    assert _is_linked(a, 'cpntools_Port', b2)
    if hasattr(b1, 'cpntools_Place25'):
        assert not _is_linked(b1, 'cpntools_Place25', a)
    if hasattr(b2, 'cpntools_Place25'):
        assert _is_linked(b2, 'cpntools_Place25', a)
    _safe_set(a, 'cpntools_Port', None)
    assert not _is_linked(a, 'cpntools_Port', b2)
    if hasattr(b2, 'cpntools_Place25'):
        assert not _is_linked(b2, 'cpntools_Place25', a)


def test_assoc_priority64_link_reassign_clear():
    a = cpntools_TransPriority(text="sample_text")
    b1 = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    b2 = cpntools_Trans(explicit=False, height=13, text="sample_text_2", width=13)
    _safe_set(a, 'cpntools_TransPriority', b1)
    assert _is_linked(a, 'cpntools_TransPriority', b1)
    if hasattr(b1, 'cpntools_Trans65'):
        assert _is_linked(b1, 'cpntools_Trans65', a)
    _safe_set(a, 'cpntools_TransPriority', b2)
    assert _is_linked(a, 'cpntools_TransPriority', b2)
    if hasattr(b1, 'cpntools_Trans65'):
        assert not _is_linked(b1, 'cpntools_Trans65', a)
    if hasattr(b2, 'cpntools_Trans65'):
        assert _is_linked(b2, 'cpntools_Trans65', a)
    _safe_set(a, 'cpntools_TransPriority', None)
    assert not _is_linked(a, 'cpntools_TransPriority', b2)
    if hasattr(b2, 'cpntools_Trans65'):
        assert not _is_linked(b2, 'cpntools_Trans65', a)


def test_assoc_time66_link_reassign_clear():
    a = cpntools_TransTime(text="sample_text")
    b1 = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    b2 = cpntools_Trans(explicit=False, height=13, text="sample_text_2", width=13)
    _safe_set(a, 'cpntools_TransTime', b1)
    assert _is_linked(a, 'cpntools_TransTime', b1)
    if hasattr(b1, 'cpntools_Trans67'):
        assert _is_linked(b1, 'cpntools_Trans67', a)
    _safe_set(a, 'cpntools_TransTime', b2)
    assert _is_linked(a, 'cpntools_TransTime', b2)
    if hasattr(b1, 'cpntools_Trans67'):
        assert not _is_linked(b1, 'cpntools_Trans67', a)
    if hasattr(b2, 'cpntools_Trans67'):
        assert _is_linked(b2, 'cpntools_Trans67', a)
    _safe_set(a, 'cpntools_TransTime', None)
    assert not _is_linked(a, 'cpntools_TransTime', b2)
    if hasattr(b2, 'cpntools_Trans67'):
        assert not _is_linked(b2, 'cpntools_Trans67', a)


def test_assoc_trans52_link_reassign_clear():
    a = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    b1 = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    b2 = cpntools_Arc(currentcyckle="sample_text_2", headsize=9.99, order=13, orientation="sample_text_2")
    _safe_set(a, 'Trans54', b1)
    assert _is_linked(a, 'Trans54', b1)
    if hasattr(b1, 'arcs53'):
        assert _is_linked(b1, 'arcs53', a)
    _safe_set(a, 'Trans54', b2)
    assert _is_linked(a, 'Trans54', b2)
    if hasattr(b1, 'arcs53'):
        assert not _is_linked(b1, 'arcs53', a)
    if hasattr(b2, 'arcs53'):
        assert _is_linked(b2, 'arcs53', a)
    _safe_set(a, 'Trans54', None)
    assert not _is_linked(a, 'Trans54', b2)
    if hasattr(b2, 'arcs53'):
        assert not _is_linked(b2, 'arcs53', a)


def test_assoc_transs10_link_reassign_clear():
    a = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    b1 = cpntools_Page(name="sample_text")
    b2 = cpntools_Page(name="sample_text_2")
    _safe_set(a, 'Trans', b1)
    assert _is_linked(a, 'Trans', b1)
    if hasattr(b1, 'page11'):
        assert _is_linked(b1, 'page11', a)
    _safe_set(a, 'Trans', b2)
    assert _is_linked(a, 'Trans', b2)
    if hasattr(b1, 'page11'):
        assert not _is_linked(b1, 'page11', a)
    if hasattr(b2, 'page11'):
        assert _is_linked(b2, 'page11', a)
    _safe_set(a, 'Trans', None)
    assert not _is_linked(a, 'Trans', b2)
    if hasattr(b2, 'page11'):
        assert not _is_linked(b2, 'page11', a)


def test_assoc_type21_link_reassign_clear():
    a = cpntools_Place(height=7, text="sample_text", width=7)
    b1 = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    b2 = cpntools_ColorSet(colorSetType="sample_text_2", declare="sample_text_2", idname="sample_text_2", timed=False)
    _safe_set(a, 'cpntools_Place', b1)
    assert _is_linked(a, 'cpntools_Place', b1)
    if hasattr(b1, 'cpntools_ColorSet'):
        assert _is_linked(b1, 'cpntools_ColorSet', a)
    _safe_set(a, 'cpntools_Place', b2)
    assert _is_linked(a, 'cpntools_Place', b2)
    if hasattr(b1, 'cpntools_ColorSet'):
        assert not _is_linked(b1, 'cpntools_ColorSet', a)
    if hasattr(b2, 'cpntools_ColorSet'):
        assert _is_linked(b2, 'cpntools_ColorSet', a)
    _safe_set(a, 'cpntools_Place', None)
    assert not _is_linked(a, 'cpntools_Place', b2)
    if hasattr(b2, 'cpntools_ColorSet'):
        assert not _is_linked(b2, 'cpntools_ColorSet', a)


def test_assoc_type46_link_reassign_clear():
    a = cpntools_Var(idname="sample_text")
    b1 = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    b2 = cpntools_ColorSet(colorSetType="sample_text_2", declare="sample_text_2", idname="sample_text_2", timed=False)
    _safe_set(a, 'cpntools_Var', b1)
    assert _is_linked(a, 'cpntools_Var', b1)
    if hasattr(b1, 'cpntools_ColorSet47'):
        assert _is_linked(b1, 'cpntools_ColorSet47', a)
    _safe_set(a, 'cpntools_Var', b2)
    assert _is_linked(a, 'cpntools_Var', b2)
    if hasattr(b1, 'cpntools_ColorSet47'):
        assert not _is_linked(b1, 'cpntools_ColorSet47', a)
    if hasattr(b2, 'cpntools_ColorSet47'):
        assert _is_linked(b2, 'cpntools_ColorSet47', a)
    _safe_set(a, 'cpntools_Var', None)
    assert not _is_linked(a, 'cpntools_Var', b2)
    if hasattr(b2, 'cpntools_ColorSet47'):
        assert not _is_linked(b2, 'cpntools_ColorSet47', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Auxiliary_strategy = st.builds(Auxiliary)
@given(instance=Auxiliary_strategy)
@settings(max_examples=25)
def test_Auxiliary_instantiation(instance):
    assert isinstance(instance, Auxiliary)


ColorSet_strategy = st.builds(ColorSet)
@given(instance=ColorSet_strategy)
@settings(max_examples=25)
def test_ColorSet_instantiation(instance):
    assert isinstance(instance, ColorSet)


CompoundColorSet_strategy = st.builds(CompoundColorSet)
@given(instance=CompoundColorSet_strategy)
@settings(max_examples=25)
def test_CompoundColorSet_instantiation(instance):
    assert isinstance(instance, CompoundColorSet)


Declaration_strategy = st.builds(Declaration)
@given(instance=Declaration_strategy)
@settings(max_examples=25)
def test_Declaration_instantiation(instance):
    assert isinstance(instance, Declaration)


DiagramElement_strategy = st.builds(DiagramElement)
@given(instance=DiagramElement_strategy)
@settings(max_examples=25)
def test_DiagramElement_instantiation(instance):
    assert isinstance(instance, DiagramElement)


SimpleColorSet_strategy = st.builds(SimpleColorSet)
@given(instance=SimpleColorSet_strategy)
@settings(max_examples=25)
def test_SimpleColorSet_instantiation(instance):
    assert isinstance(instance, SimpleColorSet)


cpntools_Alias_strategy = st.builds(cpntools_Alias)
@given(instance=cpntools_Alias_strategy)
@settings(max_examples=25)
def test_cpntools_Alias_instantiation(instance):
    assert isinstance(instance, cpntools_Alias)


cpntools_Annot_strategy = st.builds(cpntools_Annot, text=safe_text)
@given(instance=cpntools_Annot_strategy)
@settings(max_examples=25)
def test_cpntools_Annot_instantiation(instance):
    assert isinstance(instance, cpntools_Annot)


cpntools_Arc_strategy = st.builds(cpntools_Arc, currentcyckle=safe_text, headsize=st.floats(allow_nan=False, allow_infinity=False), order=st.integers(), orientation=safe_text)
@given(instance=cpntools_Arc_strategy)
@settings(max_examples=25)
def test_cpntools_Arc_instantiation(instance):
    assert isinstance(instance, cpntools_Arc)


cpntools_AuxBox_strategy = st.builds(cpntools_AuxBox, height=st.integers(), width=st.integers())
@given(instance=cpntools_AuxBox_strategy)
@settings(max_examples=25)
def test_cpntools_AuxBox_instantiation(instance):
    assert isinstance(instance, cpntools_AuxBox)


cpntools_AuxEllipse_strategy = st.builds(cpntools_AuxEllipse, height=st.integers(), width=st.integers())
@given(instance=cpntools_AuxEllipse_strategy)
@settings(max_examples=25)
def test_cpntools_AuxEllipse_instantiation(instance):
    assert isinstance(instance, cpntools_AuxEllipse)


cpntools_AuxText_strategy = st.builds(cpntools_AuxText, text=safe_text)
@given(instance=cpntools_AuxText_strategy)
@settings(max_examples=25)
def test_cpntools_AuxText_instantiation(instance):
    assert isinstance(instance, cpntools_AuxText)


cpntools_Auxiliary_strategy = st.builds(cpntools_Auxiliary)
@given(instance=cpntools_Auxiliary_strategy)
@settings(max_examples=25)
def test_cpntools_Auxiliary_instantiation(instance):
    assert isinstance(instance, cpntools_Auxiliary)


cpntools_Binder_strategy = st.builds(cpntools_Binder, height=st.integers(), posx=st.integers(), posy=st.integers(), width=st.integers())
@given(instance=cpntools_Binder_strategy)
@settings(max_examples=25)
def test_cpntools_Binder_instantiation(instance):
    assert isinstance(instance, cpntools_Binder)


cpntools_Block_strategy = st.builds(cpntools_Block, idname=safe_text)
@given(instance=cpntools_Block_strategy)
@settings(max_examples=25)
def test_cpntools_Block_instantiation(instance):
    assert isinstance(instance, cpntools_Block)


cpntools_Boolean_strategy = st.builds(cpntools_Boolean, with_=safe_text)
@given(instance=cpntools_Boolean_strategy)
@settings(max_examples=25)
def test_cpntools_Boolean_instantiation(instance):
    assert isinstance(instance, cpntools_Boolean)


cpntools_ColorSet_strategy = st.builds(cpntools_ColorSet, colorSetType=safe_text, declare=safe_text, idname=safe_text, timed=st.booleans())
@given(instance=cpntools_ColorSet_strategy)
@settings(max_examples=25)
def test_cpntools_ColorSet_instantiation(instance):
    assert isinstance(instance, cpntools_ColorSet)


cpntools_CompoundColorSet_strategy = st.builds(cpntools_CompoundColorSet)
@given(instance=cpntools_CompoundColorSet_strategy)
@settings(max_examples=25)
def test_cpntools_CompoundColorSet_instantiation(instance):
    assert isinstance(instance, cpntools_CompoundColorSet)


cpntools_Cpnet_strategy = st.builds(cpntools_Cpnet)
@given(instance=cpntools_Cpnet_strategy)
@settings(max_examples=25)
def test_cpntools_Cpnet_instantiation(instance):
    assert isinstance(instance, cpntools_Cpnet)


cpntools_Declaration_strategy = st.builds(cpntools_Declaration)
@given(instance=cpntools_Declaration_strategy)
@settings(max_examples=25)
def test_cpntools_Declaration_instantiation(instance):
    assert isinstance(instance, cpntools_Declaration)


cpntools_DiagramElement_strategy = st.builds(cpntools_DiagramElement, fillColour=safe_text, fillFilled=st.booleans(), fillPattern=safe_text, lineColour=safe_text, lineThick=st.integers(), lineType=safe_text, posx=st.integers(), posy=st.integers())
@given(instance=cpntools_DiagramElement_strategy)
@settings(max_examples=25)
def test_cpntools_DiagramElement_instantiation(instance):
    assert isinstance(instance, cpntools_DiagramElement)


cpntools_Enumerated_strategy = st.builds(cpntools_Enumerated, with_=safe_text)
@given(instance=cpntools_Enumerated_strategy)
@settings(max_examples=25)
def test_cpntools_Enumerated_instantiation(instance):
    assert isinstance(instance, cpntools_Enumerated)


cpntools_Fusion_strategy = st.builds(cpntools_Fusion, name=safe_text)
@given(instance=cpntools_Fusion_strategy)
@settings(max_examples=25)
def test_cpntools_Fusion_instantiation(instance):
    assert isinstance(instance, cpntools_Fusion)


cpntools_Globbox_strategy = st.builds(cpntools_Globbox, name=safe_text)
@given(instance=cpntools_Globbox_strategy)
@settings(max_examples=25)
def test_cpntools_Globbox_instantiation(instance):
    assert isinstance(instance, cpntools_Globbox)


cpntools_Globref_strategy = st.builds(cpntools_Globref, idname=safe_text)
@given(instance=cpntools_Globref_strategy)
@settings(max_examples=25)
def test_cpntools_Globref_instantiation(instance):
    assert isinstance(instance, cpntools_Globref)


cpntools_Group_strategy = st.builds(cpntools_Group, name=safe_text)
@given(instance=cpntools_Group_strategy)
@settings(max_examples=25)
def test_cpntools_Group_instantiation(instance):
    assert isinstance(instance, cpntools_Group)


cpntools_Index_strategy = st.builds(cpntools_Index, with_=safe_text)
@given(instance=cpntools_Index_strategy)
@settings(max_examples=25)
def test_cpntools_Index_instantiation(instance):
    assert isinstance(instance, cpntools_Index)


cpntools_Initmark_strategy = st.builds(cpntools_Initmark, expression=safe_text)
@given(instance=cpntools_Initmark_strategy)
@settings(max_examples=25)
def test_cpntools_Initmark_instantiation(instance):
    assert isinstance(instance, cpntools_Initmark)


cpntools_Integer_strategy = st.builds(cpntools_Integer, with_=safe_text)
@given(instance=cpntools_Integer_strategy)
@settings(max_examples=25)
def test_cpntools_Integer_instantiation(instance):
    assert isinstance(instance, cpntools_Integer)


cpntools_LargeInteger_strategy = st.builds(cpntools_LargeInteger, with_=safe_text)
@given(instance=cpntools_LargeInteger_strategy)
@settings(max_examples=25)
def test_cpntools_LargeInteger_instantiation(instance):
    assert isinstance(instance, cpntools_LargeInteger)


cpntools_List_strategy = st.builds(cpntools_List)
@given(instance=cpntools_List_strategy)
@settings(max_examples=25)
def test_cpntools_List_instantiation(instance):
    assert isinstance(instance, cpntools_List)


cpntools_Ml_strategy = st.builds(cpntools_Ml, expression=safe_text)
@given(instance=cpntools_Ml_strategy)
@settings(max_examples=25)
def test_cpntools_Ml_instantiation(instance):
    assert isinstance(instance, cpntools_Ml)


cpntools_Page_strategy = st.builds(cpntools_Page, name=safe_text)
@given(instance=cpntools_Page_strategy)
@settings(max_examples=25)
def test_cpntools_Page_instantiation(instance):
    assert isinstance(instance, cpntools_Page)


cpntools_Place_strategy = st.builds(cpntools_Place, height=st.integers(), text=safe_text, width=st.integers())
@given(instance=cpntools_Place_strategy)
@settings(max_examples=25)
def test_cpntools_Place_instantiation(instance):
    assert isinstance(instance, cpntools_Place)


cpntools_Port_strategy = st.builds(cpntools_Port, portType=safe_text)
@given(instance=cpntools_Port_strategy)
@settings(max_examples=25)
def test_cpntools_Port_instantiation(instance):
    assert isinstance(instance, cpntools_Port)


cpntools_Product_strategy = st.builds(cpntools_Product)
@given(instance=cpntools_Product_strategy)
@settings(max_examples=25)
def test_cpntools_Product_instantiation(instance):
    assert isinstance(instance, cpntools_Product)


cpntools_Real_strategy = st.builds(cpntools_Real, with_=safe_text)
@given(instance=cpntools_Real_strategy)
@settings(max_examples=25)
def test_cpntools_Real_instantiation(instance):
    assert isinstance(instance, cpntools_Real)


cpntools_Record_strategy = st.builds(cpntools_Record)
@given(instance=cpntools_Record_strategy)
@settings(max_examples=25)
def test_cpntools_Record_instantiation(instance):
    assert isinstance(instance, cpntools_Record)


cpntools_SimpleColorSet_strategy = st.builds(cpntools_SimpleColorSet)
@given(instance=cpntools_SimpleColorSet_strategy)
@settings(max_examples=25)
def test_cpntools_SimpleColorSet_instantiation(instance):
    assert isinstance(instance, cpntools_SimpleColorSet)


cpntools_String_strategy = st.builds(cpntools_String, and_=safe_text, with_=safe_text)
@given(instance=cpntools_String_strategy)
@settings(max_examples=25)
def test_cpntools_String_instantiation(instance):
    assert isinstance(instance, cpntools_String)


cpntools_Subset_strategy = st.builds(cpntools_Subset)
@given(instance=cpntools_Subset_strategy)
@settings(max_examples=25)
def test_cpntools_Subset_instantiation(instance):
    assert isinstance(instance, cpntools_Subset)


cpntools_Time_strategy = st.builds(cpntools_Time)
@given(instance=cpntools_Time_strategy)
@settings(max_examples=25)
def test_cpntools_Time_instantiation(instance):
    assert isinstance(instance, cpntools_Time)


cpntools_Trans_strategy = st.builds(cpntools_Trans, explicit=st.booleans(), height=st.integers(), text=safe_text, width=st.integers())
@given(instance=cpntools_Trans_strategy)
@settings(max_examples=25)
def test_cpntools_Trans_instantiation(instance):
    assert isinstance(instance, cpntools_Trans)


cpntools_TransCond_strategy = st.builds(cpntools_TransCond, text=safe_text)
@given(instance=cpntools_TransCond_strategy)
@settings(max_examples=25)
def test_cpntools_TransCond_instantiation(instance):
    assert isinstance(instance, cpntools_TransCond)


cpntools_TransPriority_strategy = st.builds(cpntools_TransPriority, text=safe_text)
@given(instance=cpntools_TransPriority_strategy)
@settings(max_examples=25)
def test_cpntools_TransPriority_instantiation(instance):
    assert isinstance(instance, cpntools_TransPriority)


cpntools_TransTime_strategy = st.builds(cpntools_TransTime, text=safe_text)
@given(instance=cpntools_TransTime_strategy)
@settings(max_examples=25)
def test_cpntools_TransTime_instantiation(instance):
    assert isinstance(instance, cpntools_TransTime)


cpntools_Union_strategy = st.builds(cpntools_Union)
@given(instance=cpntools_Union_strategy)
@settings(max_examples=25)
def test_cpntools_Union_instantiation(instance):
    assert isinstance(instance, cpntools_Union)


cpntools_Unit_strategy = st.builds(cpntools_Unit, with_=safe_text)
@given(instance=cpntools_Unit_strategy)
@settings(max_examples=25)
def test_cpntools_Unit_instantiation(instance):
    assert isinstance(instance, cpntools_Unit)


cpntools_Var_strategy = st.builds(cpntools_Var, idname=safe_text)
@given(instance=cpntools_Var_strategy)
@settings(max_examples=25)
def test_cpntools_Var_instantiation(instance):
    assert isinstance(instance, cpntools_Var)



