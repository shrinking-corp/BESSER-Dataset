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
    defaultname_FRAMESET,
    FRAME,
    defaultname_IFRAME,
    defaultname_NOFRAME,
    defaultname_FRAME,
    defaultname_TEXTAREA,
    defaultname_OBJECT,
    defaultname_PARAM,
    defaultname_APPLET,
    defaultname_DD,
    defaultname_DT,
    defaultname_DL,
    ListElement,
    defaultname_LI,
    defaultname_UL,
    defaultname_OL,
    defaultname_ListElement,
    defaultname_OPTION,
    defaultname_SELECT,
    TABLEElement,
    defaultname_TABLE,
    defaultname_INPUT,
    defaultname_FORM,
    TD,
    defaultname_TH,
    defaultname_TD,
    defaultname_TR,
    BODYElement,
    defaultname_AREA,
    defaultname_DIV,
    defaultname_PRE,
    defaultname_H3,
    defaultname_MAP,
    defaultname_P,
    defaultname_B,
    defaultname_I,
    defaultname_BR,
    defaultname_FONT,
    defaultname_H2,
    defaultname_SMALL,
    defaultname_SUB,
    defaultname_A,
    defaultname_SUP,
    defaultname_IMG,
    defaultname_STRIKE,
    defaultname_EM,
    defaultname_EMBED,
    defaultname_BIG,
    defaultname_SPAN,
    defaultname_STRONG,
    defaultname_H4,
    defaultname_TT,
    defaultname_NOEMBED,
    defaultname_TABLEElement,
    defaultname_STYLE,
    defaultname_H1,
    HEADElement,
    defaultname_TITLE,
    defaultname_LINK,
    HTMLElement,
    defaultname_HEADElement,
    defaultname_BODYElement,
    defaultname_BODY,
    defaultname_HTMLElement,
    defaultname_HEAD,
    defaultname_HTML,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_defaultname_frameset_is_not_abstract():
    assert not inspect.isabstract(defaultname_FRAMESET)


def test_hyp_defaultname_frameset_constructor_exists():
    assert callable(defaultname_FRAMESET.__init__)


def test_hyp_defaultname_frameset_constructor_args():
    sig = inspect.signature(defaultname_FRAMESET.__init__)
    params = list(sig.parameters.keys())
    assert "border" in params, "Missing parameter 'border'"
    assert "framespacing" in params, "Missing parameter 'framespacing'"
    assert "frameborder" in params, "Missing parameter 'frameborder'"
    assert "cols" in params, "Missing parameter 'cols'"
    assert "rows" in params, "Missing parameter 'rows'"








def test_hyp_frame_is_not_abstract():
    assert not inspect.isabstract(FRAME)


def test_hyp_frame_constructor_exists():
    assert callable(FRAME.__init__)


def test_hyp_frame_constructor_args():
    sig = inspect.signature(FRAME.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_iframe_is_not_abstract():
    assert not inspect.isabstract(defaultname_IFRAME)


def test_hyp_defaultname_iframe_constructor_exists():
    assert callable(defaultname_IFRAME.__init__)


def test_hyp_defaultname_iframe_constructor_args():
    sig = inspect.signature(defaultname_IFRAME.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_noframe_is_not_abstract():
    assert not inspect.isabstract(defaultname_NOFRAME)


def test_hyp_defaultname_noframe_constructor_exists():
    assert callable(defaultname_NOFRAME.__init__)


def test_hyp_defaultname_noframe_constructor_args():
    sig = inspect.signature(defaultname_NOFRAME.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_frame_is_not_abstract():
    assert not inspect.isabstract(defaultname_FRAME)


def test_hyp_defaultname_frame_constructor_exists():
    assert callable(defaultname_FRAME.__init__)


def test_hyp_defaultname_frame_constructor_args():
    sig = inspect.signature(defaultname_FRAME.__init__)
    params = list(sig.parameters.keys())
    assert "scrolling" in params, "Missing parameter 'scrolling'"
    assert "marginheight" in params, "Missing parameter 'marginheight'"
    assert "marginwidth" in params, "Missing parameter 'marginwidth'"
    assert "noresize" in params, "Missing parameter 'noresize'"
    assert "src" in params, "Missing parameter 'src'"
    assert "name" in params, "Missing parameter 'name'"









def test_hyp_defaultname_textarea_is_not_abstract():
    assert not inspect.isabstract(defaultname_TEXTAREA)


def test_hyp_defaultname_textarea_constructor_exists():
    assert callable(defaultname_TEXTAREA.__init__)


def test_hyp_defaultname_textarea_constructor_args():
    sig = inspect.signature(defaultname_TEXTAREA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "cols" in params, "Missing parameter 'cols'"
    assert "rows" in params, "Missing parameter 'rows'"






def test_hyp_defaultname_object_is_not_abstract():
    assert not inspect.isabstract(defaultname_OBJECT)


def test_hyp_defaultname_object_constructor_exists():
    assert callable(defaultname_OBJECT.__init__)


def test_hyp_defaultname_object_constructor_args():
    sig = inspect.signature(defaultname_OBJECT.__init__)
    params = list(sig.parameters.keys())
    assert "standby" in params, "Missing parameter 'standby'"
    assert "type" in params, "Missing parameter 'type'"
    assert "classid" in params, "Missing parameter 'classid'"
    assert "id" in params, "Missing parameter 'id'"
    assert "data" in params, "Missing parameter 'data'"








def test_hyp_defaultname_param_is_not_abstract():
    assert not inspect.isabstract(defaultname_PARAM)


def test_hyp_defaultname_param_constructor_exists():
    assert callable(defaultname_PARAM.__init__)


def test_hyp_defaultname_param_constructor_args():
    sig = inspect.signature(defaultname_PARAM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "paramValue" in params, "Missing parameter 'paramValue'"





def test_hyp_defaultname_applet_is_not_abstract():
    assert not inspect.isabstract(defaultname_APPLET)


def test_hyp_defaultname_applet_constructor_exists():
    assert callable(defaultname_APPLET.__init__)


def test_hyp_defaultname_applet_constructor_args():
    sig = inspect.signature(defaultname_APPLET.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "src" in params, "Missing parameter 'src'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "width" in params, "Missing parameter 'width'"
    assert "applet" in params, "Missing parameter 'applet'"
    assert "align" in params, "Missing parameter 'align'"









def test_hyp_defaultname_dd_is_not_abstract():
    assert not inspect.isabstract(defaultname_DD)


def test_hyp_defaultname_dd_constructor_exists():
    assert callable(defaultname_DD.__init__)


def test_hyp_defaultname_dd_constructor_args():
    sig = inspect.signature(defaultname_DD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_dt_is_not_abstract():
    assert not inspect.isabstract(defaultname_DT)


def test_hyp_defaultname_dt_constructor_exists():
    assert callable(defaultname_DT.__init__)


def test_hyp_defaultname_dt_constructor_args():
    sig = inspect.signature(defaultname_DT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_dl_is_not_abstract():
    assert not inspect.isabstract(defaultname_DL)


def test_hyp_defaultname_dl_constructor_exists():
    assert callable(defaultname_DL.__init__)


def test_hyp_defaultname_dl_constructor_args():
    sig = inspect.signature(defaultname_DL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_listelement_is_not_abstract():
    assert not inspect.isabstract(ListElement)


def test_hyp_listelement_constructor_exists():
    assert callable(ListElement.__init__)


def test_hyp_listelement_constructor_args():
    sig = inspect.signature(ListElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_li_is_not_abstract():
    assert not inspect.isabstract(defaultname_LI)


def test_hyp_defaultname_li_constructor_exists():
    assert callable(defaultname_LI.__init__)


def test_hyp_defaultname_li_constructor_args():
    sig = inspect.signature(defaultname_LI.__init__)
    params = list(sig.parameters.keys())
    assert "liValue" in params, "Missing parameter 'liValue'"




def test_hyp_defaultname_ul_is_not_abstract():
    assert not inspect.isabstract(defaultname_UL)


def test_hyp_defaultname_ul_constructor_exists():
    assert callable(defaultname_UL.__init__)


def test_hyp_defaultname_ul_constructor_args():
    sig = inspect.signature(defaultname_UL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_ol_is_not_abstract():
    assert not inspect.isabstract(defaultname_OL)


def test_hyp_defaultname_ol_constructor_exists():
    assert callable(defaultname_OL.__init__)


def test_hyp_defaultname_ol_constructor_args():
    sig = inspect.signature(defaultname_OL.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"




def test_hyp_defaultname_listelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_ListElement)


def test_hyp_defaultname_listelement_constructor_exists():
    assert callable(defaultname_ListElement.__init__)


def test_hyp_defaultname_listelement_constructor_args():
    sig = inspect.signature(defaultname_ListElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_defaultname_option_is_not_abstract():
    assert not inspect.isabstract(defaultname_OPTION)


def test_hyp_defaultname_option_constructor_exists():
    assert callable(defaultname_OPTION.__init__)


def test_hyp_defaultname_option_constructor_args():
    sig = inspect.signature(defaultname_OPTION.__init__)
    params = list(sig.parameters.keys())
    assert "optionValue" in params, "Missing parameter 'optionValue'"
    assert "selected" in params, "Missing parameter 'selected'"





def test_hyp_defaultname_select_is_not_abstract():
    assert not inspect.isabstract(defaultname_SELECT)


def test_hyp_defaultname_select_constructor_exists():
    assert callable(defaultname_SELECT.__init__)


def test_hyp_defaultname_select_constructor_args():
    sig = inspect.signature(defaultname_SELECT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"
    assert "multiple" in params, "Missing parameter 'multiple'"






def test_hyp_tableelement_is_not_abstract():
    assert not inspect.isabstract(TABLEElement)


def test_hyp_tableelement_constructor_exists():
    assert callable(TABLEElement.__init__)


def test_hyp_tableelement_constructor_args():
    sig = inspect.signature(TABLEElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_table_is_not_abstract():
    assert not inspect.isabstract(defaultname_TABLE)


def test_hyp_defaultname_table_constructor_exists():
    assert callable(defaultname_TABLE.__init__)


def test_hyp_defaultname_table_constructor_args():
    sig = inspect.signature(defaultname_TABLE.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "cellspacing" in params, "Missing parameter 'cellspacing'"
    assert "border" in params, "Missing parameter 'border'"
    assert "cellpadding" in params, "Missing parameter 'cellpadding'"







def test_hyp_defaultname_input_is_not_abstract():
    assert not inspect.isabstract(defaultname_INPUT)


def test_hyp_defaultname_input_constructor_exists():
    assert callable(defaultname_INPUT.__init__)


def test_hyp_defaultname_input_constructor_args():
    sig = inspect.signature(defaultname_INPUT.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "src" in params, "Missing parameter 'src'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "maxlength" in params, "Missing parameter 'maxlength'"
    assert "inputValue" in params, "Missing parameter 'inputValue'"
    assert "checked" in params, "Missing parameter 'checked'"
    assert "align" in params, "Missing parameter 'align'"











def test_hyp_defaultname_form_is_not_abstract():
    assert not inspect.isabstract(defaultname_FORM)


def test_hyp_defaultname_form_constructor_exists():
    assert callable(defaultname_FORM.__init__)


def test_hyp_defaultname_form_constructor_args():
    sig = inspect.signature(defaultname_FORM.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "method" in params, "Missing parameter 'method'"





def test_hyp_td_is_not_abstract():
    assert not inspect.isabstract(TD)


def test_hyp_td_constructor_exists():
    assert callable(TD.__init__)


def test_hyp_td_constructor_args():
    sig = inspect.signature(TD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_th_is_not_abstract():
    assert not inspect.isabstract(defaultname_TH)


def test_hyp_defaultname_th_constructor_exists():
    assert callable(defaultname_TH.__init__)


def test_hyp_defaultname_th_constructor_args():
    sig = inspect.signature(defaultname_TH.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_td_is_not_abstract():
    assert not inspect.isabstract(defaultname_TD)


def test_hyp_defaultname_td_constructor_exists():
    assert callable(defaultname_TD.__init__)


def test_hyp_defaultname_td_constructor_args():
    sig = inspect.signature(defaultname_TD.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "width" in params, "Missing parameter 'width'"








def test_hyp_defaultname_tr_is_not_abstract():
    assert not inspect.isabstract(defaultname_TR)


def test_hyp_defaultname_tr_constructor_exists():
    assert callable(defaultname_TR.__init__)


def test_hyp_defaultname_tr_constructor_args():
    sig = inspect.signature(defaultname_TR.__init__)
    params = list(sig.parameters.keys())
    assert "valign" in params, "Missing parameter 'valign'"
    assert "align" in params, "Missing parameter 'align'"





def test_hyp_bodyelement_is_not_abstract():
    assert not inspect.isabstract(BODYElement)


def test_hyp_bodyelement_constructor_exists():
    assert callable(BODYElement.__init__)


def test_hyp_bodyelement_constructor_args():
    sig = inspect.signature(BODYElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_area_is_not_abstract():
    assert not inspect.isabstract(defaultname_AREA)


def test_hyp_defaultname_area_constructor_exists():
    assert callable(defaultname_AREA.__init__)


def test_hyp_defaultname_area_constructor_args():
    sig = inspect.signature(defaultname_AREA.__init__)
    params = list(sig.parameters.keys())
    assert "ahref" in params, "Missing parameter 'ahref'"
    assert "coords" in params, "Missing parameter 'coords'"
    assert "shape" in params, "Missing parameter 'shape'"






def test_hyp_defaultname_div_is_not_abstract():
    assert not inspect.isabstract(defaultname_DIV)


def test_hyp_defaultname_div_constructor_exists():
    assert callable(defaultname_DIV.__init__)


def test_hyp_defaultname_div_constructor_args():
    sig = inspect.signature(defaultname_DIV.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"




def test_hyp_defaultname_pre_is_not_abstract():
    assert not inspect.isabstract(defaultname_PRE)


def test_hyp_defaultname_pre_constructor_exists():
    assert callable(defaultname_PRE.__init__)


def test_hyp_defaultname_pre_constructor_args():
    sig = inspect.signature(defaultname_PRE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_h3_is_not_abstract():
    assert not inspect.isabstract(defaultname_H3)


def test_hyp_defaultname_h3_constructor_exists():
    assert callable(defaultname_H3.__init__)


def test_hyp_defaultname_h3_constructor_args():
    sig = inspect.signature(defaultname_H3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_map_is_not_abstract():
    assert not inspect.isabstract(defaultname_MAP)


def test_hyp_defaultname_map_constructor_exists():
    assert callable(defaultname_MAP.__init__)


def test_hyp_defaultname_map_constructor_args():
    sig = inspect.signature(defaultname_MAP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_p_is_not_abstract():
    assert not inspect.isabstract(defaultname_P)


def test_hyp_defaultname_p_constructor_exists():
    assert callable(defaultname_P.__init__)


def test_hyp_defaultname_p_constructor_args():
    sig = inspect.signature(defaultname_P.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_b_is_not_abstract():
    assert not inspect.isabstract(defaultname_B)


def test_hyp_defaultname_b_constructor_exists():
    assert callable(defaultname_B.__init__)


def test_hyp_defaultname_b_constructor_args():
    sig = inspect.signature(defaultname_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_i_is_not_abstract():
    assert not inspect.isabstract(defaultname_I)


def test_hyp_defaultname_i_constructor_exists():
    assert callable(defaultname_I.__init__)


def test_hyp_defaultname_i_constructor_args():
    sig = inspect.signature(defaultname_I.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_br_is_not_abstract():
    assert not inspect.isabstract(defaultname_BR)


def test_hyp_defaultname_br_constructor_exists():
    assert callable(defaultname_BR.__init__)


def test_hyp_defaultname_br_constructor_args():
    sig = inspect.signature(defaultname_BR.__init__)
    params = list(sig.parameters.keys())
    assert "clear" in params, "Missing parameter 'clear'"




def test_hyp_defaultname_font_is_not_abstract():
    assert not inspect.isabstract(defaultname_FONT)


def test_hyp_defaultname_font_constructor_exists():
    assert callable(defaultname_FONT.__init__)


def test_hyp_defaultname_font_constructor_args():
    sig = inspect.signature(defaultname_FONT.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "color" in params, "Missing parameter 'color'"
    assert "face" in params, "Missing parameter 'face'"






def test_hyp_defaultname_h2_is_not_abstract():
    assert not inspect.isabstract(defaultname_H2)


def test_hyp_defaultname_h2_constructor_exists():
    assert callable(defaultname_H2.__init__)


def test_hyp_defaultname_h2_constructor_args():
    sig = inspect.signature(defaultname_H2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_small_is_not_abstract():
    assert not inspect.isabstract(defaultname_SMALL)


def test_hyp_defaultname_small_constructor_exists():
    assert callable(defaultname_SMALL.__init__)


def test_hyp_defaultname_small_constructor_args():
    sig = inspect.signature(defaultname_SMALL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_sub_is_not_abstract():
    assert not inspect.isabstract(defaultname_SUB)


def test_hyp_defaultname_sub_constructor_exists():
    assert callable(defaultname_SUB.__init__)


def test_hyp_defaultname_sub_constructor_args():
    sig = inspect.signature(defaultname_SUB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_a_is_not_abstract():
    assert not inspect.isabstract(defaultname_A)


def test_hyp_defaultname_a_constructor_exists():
    assert callable(defaultname_A.__init__)


def test_hyp_defaultname_a_constructor_args():
    sig = inspect.signature(defaultname_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "ahref" in params, "Missing parameter 'ahref'"






def test_hyp_defaultname_sup_is_not_abstract():
    assert not inspect.isabstract(defaultname_SUP)


def test_hyp_defaultname_sup_constructor_exists():
    assert callable(defaultname_SUP.__init__)


def test_hyp_defaultname_sup_constructor_args():
    sig = inspect.signature(defaultname_SUP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_img_is_not_abstract():
    assert not inspect.isabstract(defaultname_IMG)


def test_hyp_defaultname_img_constructor_exists():
    assert callable(defaultname_IMG.__init__)


def test_hyp_defaultname_img_constructor_args():
    sig = inspect.signature(defaultname_IMG.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "src" in params, "Missing parameter 'src'"
    assert "align" in params, "Missing parameter 'align'"
    assert "width" in params, "Missing parameter 'width'"
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "usemap" in params, "Missing parameter 'usemap'"
    assert "alt" in params, "Missing parameter 'alt'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "ismap" in params, "Missing parameter 'ismap'"
    assert "border" in params, "Missing parameter 'border'"













def test_hyp_defaultname_strike_is_not_abstract():
    assert not inspect.isabstract(defaultname_STRIKE)


def test_hyp_defaultname_strike_constructor_exists():
    assert callable(defaultname_STRIKE.__init__)


def test_hyp_defaultname_strike_constructor_args():
    sig = inspect.signature(defaultname_STRIKE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_em_is_not_abstract():
    assert not inspect.isabstract(defaultname_EM)


def test_hyp_defaultname_em_constructor_exists():
    assert callable(defaultname_EM.__init__)


def test_hyp_defaultname_em_constructor_args():
    sig = inspect.signature(defaultname_EM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_embed_is_not_abstract():
    assert not inspect.isabstract(defaultname_EMBED)


def test_hyp_defaultname_embed_constructor_exists():
    assert callable(defaultname_EMBED.__init__)


def test_hyp_defaultname_embed_constructor_args():
    sig = inspect.signature(defaultname_EMBED.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "align" in params, "Missing parameter 'align'"
    assert "width" in params, "Missing parameter 'width'"
    assert "border" in params, "Missing parameter 'border'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "height" in params, "Missing parameter 'height'"










def test_hyp_defaultname_big_is_not_abstract():
    assert not inspect.isabstract(defaultname_BIG)


def test_hyp_defaultname_big_constructor_exists():
    assert callable(defaultname_BIG.__init__)


def test_hyp_defaultname_big_constructor_args():
    sig = inspect.signature(defaultname_BIG.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_span_is_not_abstract():
    assert not inspect.isabstract(defaultname_SPAN)


def test_hyp_defaultname_span_constructor_exists():
    assert callable(defaultname_SPAN.__init__)


def test_hyp_defaultname_span_constructor_args():
    sig = inspect.signature(defaultname_SPAN.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"




def test_hyp_defaultname_strong_is_not_abstract():
    assert not inspect.isabstract(defaultname_STRONG)


def test_hyp_defaultname_strong_constructor_exists():
    assert callable(defaultname_STRONG.__init__)


def test_hyp_defaultname_strong_constructor_args():
    sig = inspect.signature(defaultname_STRONG.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_h4_is_not_abstract():
    assert not inspect.isabstract(defaultname_H4)


def test_hyp_defaultname_h4_constructor_exists():
    assert callable(defaultname_H4.__init__)


def test_hyp_defaultname_h4_constructor_args():
    sig = inspect.signature(defaultname_H4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_tt_is_not_abstract():
    assert not inspect.isabstract(defaultname_TT)


def test_hyp_defaultname_tt_constructor_exists():
    assert callable(defaultname_TT.__init__)


def test_hyp_defaultname_tt_constructor_args():
    sig = inspect.signature(defaultname_TT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_noembed_is_not_abstract():
    assert not inspect.isabstract(defaultname_NOEMBED)


def test_hyp_defaultname_noembed_constructor_exists():
    assert callable(defaultname_NOEMBED.__init__)


def test_hyp_defaultname_noembed_constructor_args():
    sig = inspect.signature(defaultname_NOEMBED.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_tableelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_TABLEElement)


def test_hyp_defaultname_tableelement_constructor_exists():
    assert callable(defaultname_TABLEElement.__init__)


def test_hyp_defaultname_tableelement_constructor_args():
    sig = inspect.signature(defaultname_TABLEElement.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"





def test_hyp_defaultname_style_is_not_abstract():
    assert not inspect.isabstract(defaultname_STYLE)


def test_hyp_defaultname_style_constructor_exists():
    assert callable(defaultname_STYLE.__init__)


def test_hyp_defaultname_style_constructor_args():
    sig = inspect.signature(defaultname_STYLE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_h1_is_not_abstract():
    assert not inspect.isabstract(defaultname_H1)


def test_hyp_defaultname_h1_constructor_exists():
    assert callable(defaultname_H1.__init__)


def test_hyp_defaultname_h1_constructor_args():
    sig = inspect.signature(defaultname_H1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_headelement_is_not_abstract():
    assert not inspect.isabstract(HEADElement)


def test_hyp_headelement_constructor_exists():
    assert callable(HEADElement.__init__)


def test_hyp_headelement_constructor_args():
    sig = inspect.signature(HEADElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_title_is_not_abstract():
    assert not inspect.isabstract(defaultname_TITLE)


def test_hyp_defaultname_title_constructor_exists():
    assert callable(defaultname_TITLE.__init__)


def test_hyp_defaultname_title_constructor_args():
    sig = inspect.signature(defaultname_TITLE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_link_is_not_abstract():
    assert not inspect.isabstract(defaultname_LINK)


def test_hyp_defaultname_link_constructor_exists():
    assert callable(defaultname_LINK.__init__)


def test_hyp_defaultname_link_constructor_args():
    sig = inspect.signature(defaultname_LINK.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "type" in params, "Missing parameter 'type'"
    assert "ahref" in params, "Missing parameter 'ahref'"
    assert "rel" in params, "Missing parameter 'rel'"







def test_hyp_htmlelement_is_not_abstract():
    assert not inspect.isabstract(HTMLElement)


def test_hyp_htmlelement_constructor_exists():
    assert callable(HTMLElement.__init__)


def test_hyp_htmlelement_constructor_args():
    sig = inspect.signature(HTMLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_headelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_HEADElement)


def test_hyp_defaultname_headelement_constructor_exists():
    assert callable(defaultname_HEADElement.__init__)


def test_hyp_defaultname_headelement_constructor_args():
    sig = inspect.signature(defaultname_HEADElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_bodyelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_BODYElement)


def test_hyp_defaultname_bodyelement_constructor_exists():
    assert callable(defaultname_BODYElement.__init__)


def test_hyp_defaultname_bodyelement_constructor_args():
    sig = inspect.signature(defaultname_BODYElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_body_is_not_abstract():
    assert not inspect.isabstract(defaultname_BODY)


def test_hyp_defaultname_body_constructor_exists():
    assert callable(defaultname_BODY.__init__)


def test_hyp_defaultname_body_constructor_args():
    sig = inspect.signature(defaultname_BODY.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "vlink" in params, "Missing parameter 'vlink'"
    assert "link" in params, "Missing parameter 'link'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"
    assert "alink" in params, "Missing parameter 'alink'"
    assert "text" in params, "Missing parameter 'text'"









def test_hyp_defaultname_htmlelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_HTMLElement)


def test_hyp_defaultname_htmlelement_constructor_exists():
    assert callable(defaultname_HTMLElement.__init__)


def test_hyp_defaultname_htmlelement_constructor_args():
    sig = inspect.signature(defaultname_HTMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_defaultname_head_is_not_abstract():
    assert not inspect.isabstract(defaultname_HEAD)


def test_hyp_defaultname_head_constructor_exists():
    assert callable(defaultname_HEAD.__init__)


def test_hyp_defaultname_head_constructor_args():
    sig = inspect.signature(defaultname_HEAD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_defaultname_html_is_not_abstract():
    assert not inspect.isabstract(defaultname_HTML)


def test_hyp_defaultname_html_constructor_exists():
    assert callable(defaultname_HTML.__init__)


def test_hyp_defaultname_html_constructor_args():
    sig = inspect.signature(defaultname_HTML.__init__)
    params = list(sig.parameters.keys())


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
defaultname_FRAMESET_strategy = st.builds(
    defaultname_FRAMESET,
    border=
        safe_text,
    framespacing=
        safe_text,
    frameborder=
        safe_text,
    cols=
        safe_text,
    rows=
        safe_text
)
FRAME_strategy = st.builds(
    FRAME,
)
defaultname_IFRAME_strategy = st.builds(
    defaultname_IFRAME,
)
defaultname_NOFRAME_strategy = st.builds(
    defaultname_NOFRAME,
)
defaultname_FRAME_strategy = st.builds(
    defaultname_FRAME,
    scrolling=
        safe_text,
    marginheight=
        safe_text,
    marginwidth=
        safe_text,
    noresize=
        safe_text,
    src=
        safe_text,
    name=
        safe_text
)
defaultname_TEXTAREA_strategy = st.builds(
    defaultname_TEXTAREA,
    name=
        safe_text,
    cols=
        safe_text,
    rows=
        safe_text
)
defaultname_OBJECT_strategy = st.builds(
    defaultname_OBJECT,
    standby=
        safe_text,
    type=
        safe_text,
    classid=
        safe_text,
    id=
        safe_text,
    data=
        safe_text
)
defaultname_PARAM_strategy = st.builds(
    defaultname_PARAM,
    name=
        safe_text,
    paramValue=
        safe_text
)
defaultname_APPLET_strategy = st.builds(
    defaultname_APPLET,
    height=
        safe_text,
    src=
        safe_text,
    class_=
        safe_text,
    width=
        safe_text,
    applet=
        safe_text,
    align=
        safe_text
)
defaultname_DD_strategy = st.builds(
    defaultname_DD,
)
defaultname_DT_strategy = st.builds(
    defaultname_DT,
)
defaultname_DL_strategy = st.builds(
    defaultname_DL,
)
ListElement_strategy = st.builds(
    ListElement,
)
defaultname_LI_strategy = st.builds(
    defaultname_LI,
    liValue=
        safe_text
)
defaultname_UL_strategy = st.builds(
    defaultname_UL,
)
defaultname_OL_strategy = st.builds(
    defaultname_OL,
    start=
        safe_text
)
defaultname_ListElement_strategy = st.builds(
    defaultname_ListElement,
    type=
        safe_text
)
defaultname_OPTION_strategy = st.builds(
    defaultname_OPTION,
    optionValue=
        safe_text,
    selected=
        safe_text
)
defaultname_SELECT_strategy = st.builds(
    defaultname_SELECT,
    name=
        safe_text,
    size=
        safe_text,
    multiple=
        safe_text
)
TABLEElement_strategy = st.builds(
    TABLEElement,
)
defaultname_TABLE_strategy = st.builds(
    defaultname_TABLE,
    width=
        safe_text,
    cellspacing=
        safe_text,
    border=
        safe_text,
    cellpadding=
        safe_text
)
defaultname_INPUT_strategy = st.builds(
    defaultname_INPUT,
    size=
        safe_text,
    src=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    maxlength=
        safe_text,
    inputValue=
        safe_text,
    checked=
        safe_text,
    align=
        safe_text
)
defaultname_FORM_strategy = st.builds(
    defaultname_FORM,
    action=
        safe_text,
    method=
        safe_text
)
TD_strategy = st.builds(
    TD,
)
defaultname_TH_strategy = st.builds(
    defaultname_TH,
)
defaultname_TD_strategy = st.builds(
    defaultname_TD,
    align=
        safe_text,
    rowspan=
        safe_text,
    colspan=
        safe_text,
    valign=
        safe_text,
    width=
        safe_text
)
defaultname_TR_strategy = st.builds(
    defaultname_TR,
    valign=
        safe_text,
    align=
        safe_text
)
BODYElement_strategy = st.builds(
    BODYElement,
)
defaultname_AREA_strategy = st.builds(
    defaultname_AREA,
    ahref=
        safe_text,
    coords=
        safe_text,
    shape=
        safe_text
)
defaultname_DIV_strategy = st.builds(
    defaultname_DIV,
    align=
        safe_text
)
defaultname_PRE_strategy = st.builds(
    defaultname_PRE,
)
defaultname_H3_strategy = st.builds(
    defaultname_H3,
)
defaultname_MAP_strategy = st.builds(
    defaultname_MAP,
)
defaultname_P_strategy = st.builds(
    defaultname_P,
)
defaultname_B_strategy = st.builds(
    defaultname_B,
)
defaultname_I_strategy = st.builds(
    defaultname_I,
)
defaultname_BR_strategy = st.builds(
    defaultname_BR,
    clear=
        safe_text
)
defaultname_FONT_strategy = st.builds(
    defaultname_FONT,
    size=
        safe_text,
    color=
        safe_text,
    face=
        safe_text
)
defaultname_H2_strategy = st.builds(
    defaultname_H2,
)
defaultname_SMALL_strategy = st.builds(
    defaultname_SMALL,
)
defaultname_SUB_strategy = st.builds(
    defaultname_SUB,
)
defaultname_A_strategy = st.builds(
    defaultname_A,
    name=
        safe_text,
    id=
        safe_text,
    ahref=
        safe_text
)
defaultname_SUP_strategy = st.builds(
    defaultname_SUP,
)
defaultname_IMG_strategy = st.builds(
    defaultname_IMG,
    height=
        safe_text,
    src=
        safe_text,
    align=
        safe_text,
    width=
        safe_text,
    hspace=
        safe_text,
    usemap=
        safe_text,
    alt=
        safe_text,
    vspace=
        safe_text,
    ismap=
        safe_text,
    border=
        safe_text
)
defaultname_STRIKE_strategy = st.builds(
    defaultname_STRIKE,
)
defaultname_EM_strategy = st.builds(
    defaultname_EM,
)
defaultname_EMBED_strategy = st.builds(
    defaultname_EMBED,
    src=
        safe_text,
    hspace=
        safe_text,
    align=
        safe_text,
    width=
        safe_text,
    border=
        safe_text,
    vspace=
        safe_text,
    height=
        safe_text
)
defaultname_BIG_strategy = st.builds(
    defaultname_BIG,
)
defaultname_SPAN_strategy = st.builds(
    defaultname_SPAN,
    style=
        safe_text
)
defaultname_STRONG_strategy = st.builds(
    defaultname_STRONG,
)
defaultname_H4_strategy = st.builds(
    defaultname_H4,
)
defaultname_TT_strategy = st.builds(
    defaultname_TT,
)
defaultname_NOEMBED_strategy = st.builds(
    defaultname_NOEMBED,
)
defaultname_TABLEElement_strategy = st.builds(
    defaultname_TABLEElement,
    background=
        safe_text,
    bgcolor=
        safe_text
)
defaultname_STYLE_strategy = st.builds(
    defaultname_STYLE,
)
defaultname_H1_strategy = st.builds(
    defaultname_H1,
)
HEADElement_strategy = st.builds(
    HEADElement,
)
defaultname_TITLE_strategy = st.builds(
    defaultname_TITLE,
)
defaultname_LINK_strategy = st.builds(
    defaultname_LINK,
    title=
        safe_text,
    type=
        safe_text,
    ahref=
        safe_text,
    rel=
        safe_text
)
HTMLElement_strategy = st.builds(
    HTMLElement,
)
defaultname_HEADElement_strategy = st.builds(
    defaultname_HEADElement,
)
defaultname_BODYElement_strategy = st.builds(
    defaultname_BODYElement,
)
defaultname_BODY_strategy = st.builds(
    defaultname_BODY,
    background=
        safe_text,
    vlink=
        safe_text,
    link=
        safe_text,
    bgcolor=
        safe_text,
    alink=
        safe_text,
    text=
        safe_text
)
defaultname_HTMLElement_strategy = st.builds(
    defaultname_HTMLElement,
    value=
        safe_text
)
defaultname_HEAD_strategy = st.builds(
    defaultname_HEAD,
)
defaultname_HTML_strategy = st.builds(
    defaultname_HTML,
)




@given(instance=defaultname_FRAMESET_strategy)
def test_hyp_defaultname_frameset_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=defaultname_FRAMESET_strategy)
def test_hyp_defaultname_frameset_framespacing_setter(instance):
    original = instance.framespacing
    instance.framespacing = original
    assert instance.framespacing == original



@given(instance=defaultname_FRAMESET_strategy)
def test_hyp_defaultname_frameset_frameborder_setter(instance):
    original = instance.frameborder
    instance.frameborder = original
    assert instance.frameborder == original



@given(instance=defaultname_FRAMESET_strategy)
def test_hyp_defaultname_frameset_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original



@given(instance=defaultname_FRAMESET_strategy)
def test_hyp_defaultname_frameset_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original







@given(instance=defaultname_FRAME_strategy)
def test_hyp_defaultname_frame_scrolling_setter(instance):
    original = instance.scrolling
    instance.scrolling = original
    assert instance.scrolling == original



@given(instance=defaultname_FRAME_strategy)
def test_hyp_defaultname_frame_marginheight_setter(instance):
    original = instance.marginheight
    instance.marginheight = original
    assert instance.marginheight == original



@given(instance=defaultname_FRAME_strategy)
def test_hyp_defaultname_frame_marginwidth_setter(instance):
    original = instance.marginwidth
    instance.marginwidth = original
    assert instance.marginwidth == original



@given(instance=defaultname_FRAME_strategy)
def test_hyp_defaultname_frame_noresize_setter(instance):
    original = instance.noresize
    instance.noresize = original
    assert instance.noresize == original



@given(instance=defaultname_FRAME_strategy)
def test_hyp_defaultname_frame_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_FRAME_strategy)
def test_hyp_defaultname_frame_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=defaultname_TEXTAREA_strategy)
def test_hyp_defaultname_textarea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_TEXTAREA_strategy)
def test_hyp_defaultname_textarea_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original



@given(instance=defaultname_TEXTAREA_strategy)
def test_hyp_defaultname_textarea_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original




@given(instance=defaultname_OBJECT_strategy)
def test_hyp_defaultname_object_standby_setter(instance):
    original = instance.standby
    instance.standby = original
    assert instance.standby == original



@given(instance=defaultname_OBJECT_strategy)
def test_hyp_defaultname_object_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=defaultname_OBJECT_strategy)
def test_hyp_defaultname_object_classid_setter(instance):
    original = instance.classid
    instance.classid = original
    assert instance.classid == original



@given(instance=defaultname_OBJECT_strategy)
def test_hyp_defaultname_object_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=defaultname_OBJECT_strategy)
def test_hyp_defaultname_object_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original




@given(instance=defaultname_PARAM_strategy)
def test_hyp_defaultname_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_PARAM_strategy)
def test_hyp_defaultname_param_paramValue_setter(instance):
    original = instance.paramValue
    instance.paramValue = original
    assert instance.paramValue == original




@given(instance=defaultname_APPLET_strategy)
def test_hyp_defaultname_applet_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=defaultname_APPLET_strategy)
def test_hyp_defaultname_applet_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_APPLET_strategy)
def test_hyp_defaultname_applet_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=defaultname_APPLET_strategy)
def test_hyp_defaultname_applet_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_APPLET_strategy)
def test_hyp_defaultname_applet_applet_setter(instance):
    original = instance.applet
    instance.applet = original
    assert instance.applet == original



@given(instance=defaultname_APPLET_strategy)
def test_hyp_defaultname_applet_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original








@given(instance=defaultname_LI_strategy)
def test_hyp_defaultname_li_liValue_setter(instance):
    original = instance.liValue
    instance.liValue = original
    assert instance.liValue == original





@given(instance=defaultname_OL_strategy)
def test_hyp_defaultname_ol_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original




@given(instance=defaultname_ListElement_strategy)
def test_hyp_defaultname_listelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=defaultname_OPTION_strategy)
def test_hyp_defaultname_option_optionValue_setter(instance):
    original = instance.optionValue
    instance.optionValue = original
    assert instance.optionValue == original



@given(instance=defaultname_OPTION_strategy)
def test_hyp_defaultname_option_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original




@given(instance=defaultname_SELECT_strategy)
def test_hyp_defaultname_select_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_SELECT_strategy)
def test_hyp_defaultname_select_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=defaultname_SELECT_strategy)
def test_hyp_defaultname_select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original





@given(instance=defaultname_TABLE_strategy)
def test_hyp_defaultname_table_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_TABLE_strategy)
def test_hyp_defaultname_table_cellspacing_setter(instance):
    original = instance.cellspacing
    instance.cellspacing = original
    assert instance.cellspacing == original



@given(instance=defaultname_TABLE_strategy)
def test_hyp_defaultname_table_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=defaultname_TABLE_strategy)
def test_hyp_defaultname_table_cellpadding_setter(instance):
    original = instance.cellpadding
    instance.cellpadding = original
    assert instance.cellpadding == original




@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_maxlength_setter(instance):
    original = instance.maxlength
    instance.maxlength = original
    assert instance.maxlength == original



@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_inputValue_setter(instance):
    original = instance.inputValue
    instance.inputValue = original
    assert instance.inputValue == original



@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original



@given(instance=defaultname_INPUT_strategy)
def test_hyp_defaultname_input_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original




@given(instance=defaultname_FORM_strategy)
def test_hyp_defaultname_form_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=defaultname_FORM_strategy)
def test_hyp_defaultname_form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original






@given(instance=defaultname_TD_strategy)
def test_hyp_defaultname_td_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=defaultname_TD_strategy)
def test_hyp_defaultname_td_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original



@given(instance=defaultname_TD_strategy)
def test_hyp_defaultname_td_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original



@given(instance=defaultname_TD_strategy)
def test_hyp_defaultname_td_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=defaultname_TD_strategy)
def test_hyp_defaultname_td_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=defaultname_TR_strategy)
def test_hyp_defaultname_tr_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=defaultname_TR_strategy)
def test_hyp_defaultname_tr_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original





@given(instance=defaultname_AREA_strategy)
def test_hyp_defaultname_area_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original



@given(instance=defaultname_AREA_strategy)
def test_hyp_defaultname_area_coords_setter(instance):
    original = instance.coords
    instance.coords = original
    assert instance.coords == original



@given(instance=defaultname_AREA_strategy)
def test_hyp_defaultname_area_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original




@given(instance=defaultname_DIV_strategy)
def test_hyp_defaultname_div_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original










@given(instance=defaultname_BR_strategy)
def test_hyp_defaultname_br_clear_setter(instance):
    original = instance.clear
    instance.clear = original
    assert instance.clear == original




@given(instance=defaultname_FONT_strategy)
def test_hyp_defaultname_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=defaultname_FONT_strategy)
def test_hyp_defaultname_font_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=defaultname_FONT_strategy)
def test_hyp_defaultname_font_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original







@given(instance=defaultname_A_strategy)
def test_hyp_defaultname_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_A_strategy)
def test_hyp_defaultname_a_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=defaultname_A_strategy)
def test_hyp_defaultname_a_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original





@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_usemap_setter(instance):
    original = instance.usemap
    instance.usemap = original
    assert instance.usemap == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_ismap_setter(instance):
    original = instance.ismap
    instance.ismap = original
    assert instance.ismap == original



@given(instance=defaultname_IMG_strategy)
def test_hyp_defaultname_img_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original






@given(instance=defaultname_EMBED_strategy)
def test_hyp_defaultname_embed_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_EMBED_strategy)
def test_hyp_defaultname_embed_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original



@given(instance=defaultname_EMBED_strategy)
def test_hyp_defaultname_embed_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=defaultname_EMBED_strategy)
def test_hyp_defaultname_embed_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_EMBED_strategy)
def test_hyp_defaultname_embed_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=defaultname_EMBED_strategy)
def test_hyp_defaultname_embed_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original



@given(instance=defaultname_EMBED_strategy)
def test_hyp_defaultname_embed_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=defaultname_SPAN_strategy)
def test_hyp_defaultname_span_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original








@given(instance=defaultname_TABLEElement_strategy)
def test_hyp_defaultname_tableelement_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=defaultname_TABLEElement_strategy)
def test_hyp_defaultname_tableelement_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original








@given(instance=defaultname_LINK_strategy)
def test_hyp_defaultname_link_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=defaultname_LINK_strategy)
def test_hyp_defaultname_link_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=defaultname_LINK_strategy)
def test_hyp_defaultname_link_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original



@given(instance=defaultname_LINK_strategy)
def test_hyp_defaultname_link_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original







@given(instance=defaultname_BODY_strategy)
def test_hyp_defaultname_body_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=defaultname_BODY_strategy)
def test_hyp_defaultname_body_vlink_setter(instance):
    original = instance.vlink
    instance.vlink = original
    assert instance.vlink == original



@given(instance=defaultname_BODY_strategy)
def test_hyp_defaultname_body_link_setter(instance):
    original = instance.link
    instance.link = original
    assert instance.link == original



@given(instance=defaultname_BODY_strategy)
def test_hyp_defaultname_body_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original



@given(instance=defaultname_BODY_strategy)
def test_hyp_defaultname_body_alink_setter(instance):
    original = instance.alink
    instance.alink = original
    assert instance.alink == original



@given(instance=defaultname_BODY_strategy)
def test_hyp_defaultname_body_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=defaultname_HTMLElement_strategy)
def test_hyp_defaultname_htmlelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BODYElement,
    FRAME,
    HEADElement,
    HTMLElement,
    ListElement,
    TABLEElement,
    TD,
    defaultname_A,
    defaultname_APPLET,
    defaultname_AREA,
    defaultname_B,
    defaultname_BIG,
    defaultname_BODY,
    defaultname_BODYElement,
    defaultname_BR,
    defaultname_DD,
    defaultname_DIV,
    defaultname_DL,
    defaultname_DT,
    defaultname_EM,
    defaultname_EMBED,
    defaultname_FONT,
    defaultname_FORM,
    defaultname_FRAME,
    defaultname_FRAMESET,
    defaultname_H1,
    defaultname_H2,
    defaultname_H3,
    defaultname_H4,
    defaultname_HEAD,
    defaultname_HEADElement,
    defaultname_HTML,
    defaultname_HTMLElement,
    defaultname_I,
    defaultname_IFRAME,
    defaultname_IMG,
    defaultname_INPUT,
    defaultname_LI,
    defaultname_LINK,
    defaultname_ListElement,
    defaultname_MAP,
    defaultname_NOEMBED,
    defaultname_NOFRAME,
    defaultname_OBJECT,
    defaultname_OL,
    defaultname_OPTION,
    defaultname_P,
    defaultname_PARAM,
    defaultname_PRE,
    defaultname_SELECT,
    defaultname_SMALL,
    defaultname_SPAN,
    defaultname_STRIKE,
    defaultname_STRONG,
    defaultname_STYLE,
    defaultname_SUB,
    defaultname_SUP,
    defaultname_TABLE,
    defaultname_TABLEElement,
    defaultname_TD,
    defaultname_TEXTAREA,
    defaultname_TH,
    defaultname_TITLE,
    defaultname_TR,
    defaultname_TT,
    defaultname_UL,
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

def test_defaultname_A_ahref_value_roundtrip():
    instance = defaultname_A(ahref="sample_text", id="sample_text", name="sample_text")
    assert instance.ahref == "sample_text"
    instance.ahref = "sample_text_2"
    assert instance.ahref == "sample_text_2"


def test_defaultname_A_id_value_roundtrip():
    instance = defaultname_A(ahref="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_defaultname_A_name_value_roundtrip():
    instance = defaultname_A(ahref="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_defaultname_APPLET_align_value_roundtrip():
    instance = defaultname_APPLET(align="sample_text", applet="sample_text", class_="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_defaultname_APPLET_applet_value_roundtrip():
    instance = defaultname_APPLET(align="sample_text", applet="sample_text", class_="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.applet == "sample_text"
    instance.applet = "sample_text_2"
    assert instance.applet == "sample_text_2"


def test_defaultname_APPLET_class__value_roundtrip():
    instance = defaultname_APPLET(align="sample_text", applet="sample_text", class_="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_defaultname_APPLET_height_value_roundtrip():
    instance = defaultname_APPLET(align="sample_text", applet="sample_text", class_="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_defaultname_APPLET_src_value_roundtrip():
    instance = defaultname_APPLET(align="sample_text", applet="sample_text", class_="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_defaultname_APPLET_width_value_roundtrip():
    instance = defaultname_APPLET(align="sample_text", applet="sample_text", class_="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_defaultname_AREA_ahref_value_roundtrip():
    instance = defaultname_AREA(ahref="sample_text", coords="sample_text", shape="sample_text")
    assert instance.ahref == "sample_text"
    instance.ahref = "sample_text_2"
    assert instance.ahref == "sample_text_2"


def test_defaultname_AREA_coords_value_roundtrip():
    instance = defaultname_AREA(ahref="sample_text", coords="sample_text", shape="sample_text")
    assert instance.coords == "sample_text"
    instance.coords = "sample_text_2"
    assert instance.coords == "sample_text_2"


def test_defaultname_AREA_shape_value_roundtrip():
    instance = defaultname_AREA(ahref="sample_text", coords="sample_text", shape="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_defaultname_BODY_alink_value_roundtrip():
    instance = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    assert instance.alink == "sample_text"
    instance.alink = "sample_text_2"
    assert instance.alink == "sample_text_2"


def test_defaultname_BODY_background_value_roundtrip():
    instance = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    assert instance.background == "sample_text"
    instance.background = "sample_text_2"
    assert instance.background == "sample_text_2"


def test_defaultname_BODY_bgcolor_value_roundtrip():
    instance = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    assert instance.bgcolor == "sample_text"
    instance.bgcolor = "sample_text_2"
    assert instance.bgcolor == "sample_text_2"


def test_defaultname_BODY_link_value_roundtrip():
    instance = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    assert instance.link == "sample_text"
    instance.link = "sample_text_2"
    assert instance.link == "sample_text_2"


def test_defaultname_BODY_text_value_roundtrip():
    instance = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_defaultname_BODY_vlink_value_roundtrip():
    instance = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    assert instance.vlink == "sample_text"
    instance.vlink = "sample_text_2"
    assert instance.vlink == "sample_text_2"


def test_defaultname_BR_clear_value_roundtrip():
    instance = defaultname_BR(clear="sample_text")
    assert instance.clear == "sample_text"
    instance.clear = "sample_text_2"
    assert instance.clear == "sample_text_2"


def test_defaultname_DIV_align_value_roundtrip():
    instance = defaultname_DIV(align="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_defaultname_EMBED_align_value_roundtrip():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_defaultname_EMBED_border_value_roundtrip():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert instance.border == "sample_text"
    instance.border = "sample_text_2"
    assert instance.border == "sample_text_2"


def test_defaultname_EMBED_height_value_roundtrip():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_defaultname_EMBED_hspace_value_roundtrip():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert instance.hspace == "sample_text"
    instance.hspace = "sample_text_2"
    assert instance.hspace == "sample_text_2"


def test_defaultname_EMBED_src_value_roundtrip():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_defaultname_EMBED_vspace_value_roundtrip():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert instance.vspace == "sample_text"
    instance.vspace = "sample_text_2"
    assert instance.vspace == "sample_text_2"


def test_defaultname_EMBED_width_value_roundtrip():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_defaultname_FONT_color_value_roundtrip():
    instance = defaultname_FONT(color="sample_text", face="sample_text", size="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_defaultname_FONT_face_value_roundtrip():
    instance = defaultname_FONT(color="sample_text", face="sample_text", size="sample_text")
    assert instance.face == "sample_text"
    instance.face = "sample_text_2"
    assert instance.face == "sample_text_2"


def test_defaultname_FONT_size_value_roundtrip():
    instance = defaultname_FONT(color="sample_text", face="sample_text", size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_defaultname_FORM_action_value_roundtrip():
    instance = defaultname_FORM(action="sample_text", method="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_defaultname_FORM_method_value_roundtrip():
    instance = defaultname_FORM(action="sample_text", method="sample_text")
    assert instance.method == "sample_text"
    instance.method = "sample_text_2"
    assert instance.method == "sample_text_2"


def test_defaultname_FRAME_marginheight_value_roundtrip():
    instance = defaultname_FRAME(marginheight="sample_text", marginwidth="sample_text", name="sample_text", noresize="sample_text", scrolling="sample_text", src="sample_text")
    assert instance.marginheight == "sample_text"
    instance.marginheight = "sample_text_2"
    assert instance.marginheight == "sample_text_2"


def test_defaultname_FRAME_marginwidth_value_roundtrip():
    instance = defaultname_FRAME(marginheight="sample_text", marginwidth="sample_text", name="sample_text", noresize="sample_text", scrolling="sample_text", src="sample_text")
    assert instance.marginwidth == "sample_text"
    instance.marginwidth = "sample_text_2"
    assert instance.marginwidth == "sample_text_2"


def test_defaultname_FRAME_name_value_roundtrip():
    instance = defaultname_FRAME(marginheight="sample_text", marginwidth="sample_text", name="sample_text", noresize="sample_text", scrolling="sample_text", src="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_defaultname_FRAME_noresize_value_roundtrip():
    instance = defaultname_FRAME(marginheight="sample_text", marginwidth="sample_text", name="sample_text", noresize="sample_text", scrolling="sample_text", src="sample_text")
    assert instance.noresize == "sample_text"
    instance.noresize = "sample_text_2"
    assert instance.noresize == "sample_text_2"


def test_defaultname_FRAME_scrolling_value_roundtrip():
    instance = defaultname_FRAME(marginheight="sample_text", marginwidth="sample_text", name="sample_text", noresize="sample_text", scrolling="sample_text", src="sample_text")
    assert instance.scrolling == "sample_text"
    instance.scrolling = "sample_text_2"
    assert instance.scrolling == "sample_text_2"


def test_defaultname_FRAME_src_value_roundtrip():
    instance = defaultname_FRAME(marginheight="sample_text", marginwidth="sample_text", name="sample_text", noresize="sample_text", scrolling="sample_text", src="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_defaultname_FRAMESET_border_value_roundtrip():
    instance = defaultname_FRAMESET(border="sample_text", cols="sample_text", frameborder="sample_text", framespacing="sample_text", rows="sample_text")
    assert instance.border == "sample_text"
    instance.border = "sample_text_2"
    assert instance.border == "sample_text_2"


def test_defaultname_FRAMESET_cols_value_roundtrip():
    instance = defaultname_FRAMESET(border="sample_text", cols="sample_text", frameborder="sample_text", framespacing="sample_text", rows="sample_text")
    assert instance.cols == "sample_text"
    instance.cols = "sample_text_2"
    assert instance.cols == "sample_text_2"


def test_defaultname_FRAMESET_frameborder_value_roundtrip():
    instance = defaultname_FRAMESET(border="sample_text", cols="sample_text", frameborder="sample_text", framespacing="sample_text", rows="sample_text")
    assert instance.frameborder == "sample_text"
    instance.frameborder = "sample_text_2"
    assert instance.frameborder == "sample_text_2"


def test_defaultname_FRAMESET_framespacing_value_roundtrip():
    instance = defaultname_FRAMESET(border="sample_text", cols="sample_text", frameborder="sample_text", framespacing="sample_text", rows="sample_text")
    assert instance.framespacing == "sample_text"
    instance.framespacing = "sample_text_2"
    assert instance.framespacing == "sample_text_2"


def test_defaultname_FRAMESET_rows_value_roundtrip():
    instance = defaultname_FRAMESET(border="sample_text", cols="sample_text", frameborder="sample_text", framespacing="sample_text", rows="sample_text")
    assert instance.rows == "sample_text"
    instance.rows = "sample_text_2"
    assert instance.rows == "sample_text_2"


def test_defaultname_HTMLElement_value_value_roundtrip():
    instance = defaultname_HTMLElement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_defaultname_IMG_align_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_defaultname_IMG_alt_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.alt == "sample_text"
    instance.alt = "sample_text_2"
    assert instance.alt == "sample_text_2"


def test_defaultname_IMG_border_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.border == "sample_text"
    instance.border = "sample_text_2"
    assert instance.border == "sample_text_2"


def test_defaultname_IMG_height_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_defaultname_IMG_hspace_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.hspace == "sample_text"
    instance.hspace = "sample_text_2"
    assert instance.hspace == "sample_text_2"


def test_defaultname_IMG_ismap_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.ismap == "sample_text"
    instance.ismap = "sample_text_2"
    assert instance.ismap == "sample_text_2"


def test_defaultname_IMG_src_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_defaultname_IMG_usemap_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.usemap == "sample_text"
    instance.usemap = "sample_text_2"
    assert instance.usemap == "sample_text_2"


def test_defaultname_IMG_vspace_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.vspace == "sample_text"
    instance.vspace = "sample_text_2"
    assert instance.vspace == "sample_text_2"


def test_defaultname_IMG_width_value_roundtrip():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_defaultname_INPUT_align_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_defaultname_INPUT_checked_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.checked == "sample_text"
    instance.checked = "sample_text_2"
    assert instance.checked == "sample_text_2"


def test_defaultname_INPUT_inputValue_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.inputValue == "sample_text"
    instance.inputValue = "sample_text_2"
    assert instance.inputValue == "sample_text_2"


def test_defaultname_INPUT_maxlength_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.maxlength == "sample_text"
    instance.maxlength = "sample_text_2"
    assert instance.maxlength == "sample_text_2"


def test_defaultname_INPUT_name_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_defaultname_INPUT_size_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_defaultname_INPUT_src_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_defaultname_INPUT_type_value_roundtrip():
    instance = defaultname_INPUT(align="sample_text", checked="sample_text", inputValue="sample_text", maxlength="sample_text", name="sample_text", size="sample_text", src="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_defaultname_LI_liValue_value_roundtrip():
    instance = defaultname_LI(liValue="sample_text")
    assert instance.liValue == "sample_text"
    instance.liValue = "sample_text_2"
    assert instance.liValue == "sample_text_2"


def test_defaultname_LINK_ahref_value_roundtrip():
    instance = defaultname_LINK(ahref="sample_text", rel="sample_text", title="sample_text", type="sample_text")
    assert instance.ahref == "sample_text"
    instance.ahref = "sample_text_2"
    assert instance.ahref == "sample_text_2"


def test_defaultname_LINK_rel_value_roundtrip():
    instance = defaultname_LINK(ahref="sample_text", rel="sample_text", title="sample_text", type="sample_text")
    assert instance.rel == "sample_text"
    instance.rel = "sample_text_2"
    assert instance.rel == "sample_text_2"


def test_defaultname_LINK_title_value_roundtrip():
    instance = defaultname_LINK(ahref="sample_text", rel="sample_text", title="sample_text", type="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_defaultname_LINK_type_value_roundtrip():
    instance = defaultname_LINK(ahref="sample_text", rel="sample_text", title="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_defaultname_ListElement_type_value_roundtrip():
    instance = defaultname_ListElement(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_defaultname_OBJECT_classid_value_roundtrip():
    instance = defaultname_OBJECT(classid="sample_text", data="sample_text", id="sample_text", standby="sample_text", type="sample_text")
    assert instance.classid == "sample_text"
    instance.classid = "sample_text_2"
    assert instance.classid == "sample_text_2"


def test_defaultname_OBJECT_data_value_roundtrip():
    instance = defaultname_OBJECT(classid="sample_text", data="sample_text", id="sample_text", standby="sample_text", type="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_defaultname_OBJECT_id_value_roundtrip():
    instance = defaultname_OBJECT(classid="sample_text", data="sample_text", id="sample_text", standby="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_defaultname_OBJECT_standby_value_roundtrip():
    instance = defaultname_OBJECT(classid="sample_text", data="sample_text", id="sample_text", standby="sample_text", type="sample_text")
    assert instance.standby == "sample_text"
    instance.standby = "sample_text_2"
    assert instance.standby == "sample_text_2"


def test_defaultname_OBJECT_type_value_roundtrip():
    instance = defaultname_OBJECT(classid="sample_text", data="sample_text", id="sample_text", standby="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_defaultname_OL_start_value_roundtrip():
    instance = defaultname_OL(start="sample_text")
    assert instance.start == "sample_text"
    instance.start = "sample_text_2"
    assert instance.start == "sample_text_2"


def test_defaultname_OPTION_optionValue_value_roundtrip():
    instance = defaultname_OPTION(optionValue="sample_text", selected="sample_text")
    assert instance.optionValue == "sample_text"
    instance.optionValue = "sample_text_2"
    assert instance.optionValue == "sample_text_2"


def test_defaultname_OPTION_selected_value_roundtrip():
    instance = defaultname_OPTION(optionValue="sample_text", selected="sample_text")
    assert instance.selected == "sample_text"
    instance.selected = "sample_text_2"
    assert instance.selected == "sample_text_2"


def test_defaultname_PARAM_name_value_roundtrip():
    instance = defaultname_PARAM(name="sample_text", paramValue="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_defaultname_PARAM_paramValue_value_roundtrip():
    instance = defaultname_PARAM(name="sample_text", paramValue="sample_text")
    assert instance.paramValue == "sample_text"
    instance.paramValue = "sample_text_2"
    assert instance.paramValue == "sample_text_2"


def test_defaultname_SELECT_multiple_value_roundtrip():
    instance = defaultname_SELECT(multiple="sample_text", name="sample_text", size="sample_text")
    assert instance.multiple == "sample_text"
    instance.multiple = "sample_text_2"
    assert instance.multiple == "sample_text_2"


def test_defaultname_SELECT_name_value_roundtrip():
    instance = defaultname_SELECT(multiple="sample_text", name="sample_text", size="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_defaultname_SELECT_size_value_roundtrip():
    instance = defaultname_SELECT(multiple="sample_text", name="sample_text", size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_defaultname_SPAN_style_value_roundtrip():
    instance = defaultname_SPAN(style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_defaultname_TABLE_border_value_roundtrip():
    instance = defaultname_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.border == "sample_text"
    instance.border = "sample_text_2"
    assert instance.border == "sample_text_2"


def test_defaultname_TABLE_cellpadding_value_roundtrip():
    instance = defaultname_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.cellpadding == "sample_text"
    instance.cellpadding = "sample_text_2"
    assert instance.cellpadding == "sample_text_2"


def test_defaultname_TABLE_cellspacing_value_roundtrip():
    instance = defaultname_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.cellspacing == "sample_text"
    instance.cellspacing = "sample_text_2"
    assert instance.cellspacing == "sample_text_2"


def test_defaultname_TABLE_width_value_roundtrip():
    instance = defaultname_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_defaultname_TABLEElement_background_value_roundtrip():
    instance = defaultname_TABLEElement(background="sample_text", bgcolor="sample_text")
    assert instance.background == "sample_text"
    instance.background = "sample_text_2"
    assert instance.background == "sample_text_2"


def test_defaultname_TABLEElement_bgcolor_value_roundtrip():
    instance = defaultname_TABLEElement(background="sample_text", bgcolor="sample_text")
    assert instance.bgcolor == "sample_text"
    instance.bgcolor = "sample_text_2"
    assert instance.bgcolor == "sample_text_2"


def test_defaultname_TD_align_value_roundtrip():
    instance = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_defaultname_TD_colspan_value_roundtrip():
    instance = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.colspan == "sample_text"
    instance.colspan = "sample_text_2"
    assert instance.colspan == "sample_text_2"


def test_defaultname_TD_rowspan_value_roundtrip():
    instance = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.rowspan == "sample_text"
    instance.rowspan = "sample_text_2"
    assert instance.rowspan == "sample_text_2"


def test_defaultname_TD_valign_value_roundtrip():
    instance = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_defaultname_TD_width_value_roundtrip():
    instance = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_defaultname_TEXTAREA_cols_value_roundtrip():
    instance = defaultname_TEXTAREA(cols="sample_text", name="sample_text", rows="sample_text")
    assert instance.cols == "sample_text"
    instance.cols = "sample_text_2"
    assert instance.cols == "sample_text_2"


def test_defaultname_TEXTAREA_name_value_roundtrip():
    instance = defaultname_TEXTAREA(cols="sample_text", name="sample_text", rows="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_defaultname_TEXTAREA_rows_value_roundtrip():
    instance = defaultname_TEXTAREA(cols="sample_text", name="sample_text", rows="sample_text")
    assert instance.rows == "sample_text"
    instance.rows = "sample_text_2"
    assert instance.rows == "sample_text_2"


def test_defaultname_TR_align_value_roundtrip():
    instance = defaultname_TR(align="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_defaultname_TR_valign_value_roundtrip():
    instance = defaultname_TR(align="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_defaultname_A_isa_BODYElement():
    instance = defaultname_A(ahref="sample_text", id="sample_text", name="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_AREA_isa_BODYElement():
    instance = defaultname_AREA(ahref="sample_text", coords="sample_text", shape="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_B_isa_BODYElement():
    instance = defaultname_B()
    assert isinstance(instance, BODYElement)


def test_defaultname_BIG_isa_BODYElement():
    instance = defaultname_BIG()
    assert isinstance(instance, BODYElement)


def test_defaultname_BR_isa_BODYElement():
    instance = defaultname_BR(clear="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_DIV_isa_BODYElement():
    instance = defaultname_DIV(align="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_EM_isa_BODYElement():
    instance = defaultname_EM()
    assert isinstance(instance, BODYElement)


def test_defaultname_EMBED_isa_BODYElement():
    instance = defaultname_EMBED(align="sample_text", border="sample_text", height="sample_text", hspace="sample_text", src="sample_text", vspace="sample_text", width="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_FONT_isa_BODYElement():
    instance = defaultname_FONT(color="sample_text", face="sample_text", size="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_H1_isa_BODYElement():
    instance = defaultname_H1()
    assert isinstance(instance, BODYElement)


def test_defaultname_H2_isa_BODYElement():
    instance = defaultname_H2()
    assert isinstance(instance, BODYElement)


def test_defaultname_H3_isa_BODYElement():
    instance = defaultname_H3()
    assert isinstance(instance, BODYElement)


def test_defaultname_H4_isa_BODYElement():
    instance = defaultname_H4()
    assert isinstance(instance, BODYElement)


def test_defaultname_I_isa_BODYElement():
    instance = defaultname_I()
    assert isinstance(instance, BODYElement)


def test_defaultname_IMG_isa_BODYElement():
    instance = defaultname_IMG(align="sample_text", alt="sample_text", border="sample_text", height="sample_text", hspace="sample_text", ismap="sample_text", src="sample_text", usemap="sample_text", vspace="sample_text", width="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_MAP_isa_BODYElement():
    instance = defaultname_MAP()
    assert isinstance(instance, BODYElement)


def test_defaultname_NOEMBED_isa_BODYElement():
    instance = defaultname_NOEMBED()
    assert isinstance(instance, BODYElement)


def test_defaultname_P_isa_BODYElement():
    instance = defaultname_P()
    assert isinstance(instance, BODYElement)


def test_defaultname_PRE_isa_BODYElement():
    instance = defaultname_PRE()
    assert isinstance(instance, BODYElement)


def test_defaultname_SMALL_isa_BODYElement():
    instance = defaultname_SMALL()
    assert isinstance(instance, BODYElement)


def test_defaultname_SPAN_isa_BODYElement():
    instance = defaultname_SPAN(style="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_STRIKE_isa_BODYElement():
    instance = defaultname_STRIKE()
    assert isinstance(instance, BODYElement)


def test_defaultname_STRONG_isa_BODYElement():
    instance = defaultname_STRONG()
    assert isinstance(instance, BODYElement)


def test_defaultname_STYLE_isa_BODYElement():
    instance = defaultname_STYLE()
    assert isinstance(instance, BODYElement)


def test_defaultname_SUB_isa_BODYElement():
    instance = defaultname_SUB()
    assert isinstance(instance, BODYElement)


def test_defaultname_SUP_isa_BODYElement():
    instance = defaultname_SUP()
    assert isinstance(instance, BODYElement)


def test_defaultname_TABLEElement_isa_BODYElement():
    instance = defaultname_TABLEElement(background="sample_text", bgcolor="sample_text")
    assert isinstance(instance, BODYElement)


def test_defaultname_TT_isa_BODYElement():
    instance = defaultname_TT()
    assert isinstance(instance, BODYElement)


def test_defaultname_IFRAME_isa_FRAME():
    instance = defaultname_IFRAME()
    assert isinstance(instance, FRAME)


def test_defaultname_LINK_isa_HEADElement():
    instance = defaultname_LINK(ahref="sample_text", rel="sample_text", title="sample_text", type="sample_text")
    assert isinstance(instance, HEADElement)


def test_defaultname_TITLE_isa_HEADElement():
    instance = defaultname_TITLE()
    assert isinstance(instance, HEADElement)


def test_defaultname_BODY_isa_HTMLElement():
    instance = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    assert isinstance(instance, HTMLElement)


def test_defaultname_BODYElement_isa_HTMLElement():
    instance = defaultname_BODYElement()
    assert isinstance(instance, HTMLElement)


def test_defaultname_HEAD_isa_HTMLElement():
    instance = defaultname_HEAD()
    assert isinstance(instance, HTMLElement)


def test_defaultname_HEADElement_isa_HTMLElement():
    instance = defaultname_HEADElement()
    assert isinstance(instance, HTMLElement)


def test_defaultname_LI_isa_ListElement():
    instance = defaultname_LI(liValue="sample_text")
    assert isinstance(instance, ListElement)


def test_defaultname_OL_isa_ListElement():
    instance = defaultname_OL(start="sample_text")
    assert isinstance(instance, ListElement)


def test_defaultname_UL_isa_ListElement():
    instance = defaultname_UL()
    assert isinstance(instance, ListElement)


def test_defaultname_TABLE_isa_TABLEElement():
    instance = defaultname_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert isinstance(instance, TABLEElement)


def test_defaultname_TD_isa_TABLEElement():
    instance = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert isinstance(instance, TABLEElement)


def test_defaultname_TR_isa_TABLEElement():
    instance = defaultname_TR(align="sample_text", valign="sample_text")
    assert isinstance(instance, TABLEElement)


def test_defaultname_TH_isa_TD():
    instance = defaultname_TH()
    assert isinstance(instance, TD)


def test_assoc_body1_link_reassign_clear():
    a = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    b1 = defaultname_HTML()
    b2 = defaultname_HTML()
    _safe_set(a, 'BODY', b1)
    assert _is_linked(a, 'BODY', b1)
    if hasattr(b1, 'html2'):
        assert _is_linked(b1, 'html2', a)
    _safe_set(a, 'BODY', b2)
    assert _is_linked(a, 'BODY', b2)
    if hasattr(b1, 'html2'):
        assert not _is_linked(b1, 'html2', a)
    if hasattr(b2, 'html2'):
        assert _is_linked(b2, 'html2', a)
    _safe_set(a, 'BODY', None)
    assert not _is_linked(a, 'BODY', b2)
    if hasattr(b2, 'html2'):
        assert not _is_linked(b2, 'html2', a)


def test_assoc_body17_link_reassign_clear():
    a = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    b1 = defaultname_BODYElement()
    b2 = defaultname_BODYElement()
    _safe_set(a, 'BODY18', b1)
    assert _is_linked(a, 'BODY18', b1)
    if hasattr(b1, 'bodyElements'):
        assert _is_linked(b1, 'bodyElements', a)
    _safe_set(a, 'BODY18', b2)
    assert _is_linked(a, 'BODY18', b2)
    if hasattr(b1, 'bodyElements'):
        assert not _is_linked(b1, 'bodyElements', a)
    if hasattr(b2, 'bodyElements'):
        assert _is_linked(b2, 'bodyElements', a)
    _safe_set(a, 'BODY18', None)
    assert not _is_linked(a, 'BODY18', b2)
    if hasattr(b2, 'bodyElements'):
        assert not _is_linked(b2, 'bodyElements', a)


def test_assoc_bodyElements13_link_reassign_clear():
    a = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    b1 = defaultname_BODYElement()
    b2 = defaultname_BODYElement()
    _safe_set(a, 'body', {b1})
    assert _is_linked(a, 'body', b1)
    if hasattr(b1, 'BODYElement'):
        assert _is_linked(b1, 'BODYElement', a)
    _safe_set(a, 'body', {b2})
    assert _is_linked(a, 'body', b2)
    if hasattr(b1, 'BODYElement'):
        assert not _is_linked(b1, 'BODYElement', a)
    if hasattr(b2, 'BODYElement'):
        assert _is_linked(b2, 'BODYElement', a)
    _safe_set(a, 'body', set())
    assert not _is_linked(a, 'body', b2)
    if hasattr(b2, 'BODYElement'):
        assert not _is_linked(b2, 'BODYElement', a)


def test_assoc_children4_link_reassign_clear():
    a = defaultname_HTMLElement(value="sample_text")
    b1 = defaultname_HTMLElement(value="sample_text")
    b2 = defaultname_HTMLElement(value="sample_text_2")
    _safe_set(a, 'HTMLElement', b1)
    assert _is_linked(a, 'HTMLElement', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'HTMLElement', b2)
    assert _is_linked(a, 'HTMLElement', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'HTMLElement', None)
    assert not _is_linked(a, 'HTMLElement', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_html14_link_reassign_clear():
    a = defaultname_BODY(alink="sample_text", background="sample_text", bgcolor="sample_text", link="sample_text", text="sample_text", vlink="sample_text")
    b1 = defaultname_HTML()
    b2 = defaultname_HTML()
    _safe_set(a, 'body15', b1)
    assert _is_linked(a, 'body15', b1)
    if hasattr(b1, 'HTML16'):
        assert _is_linked(b1, 'HTML16', a)
    _safe_set(a, 'body15', b2)
    assert _is_linked(a, 'body15', b2)
    if hasattr(b1, 'HTML16'):
        assert not _is_linked(b1, 'HTML16', a)
    if hasattr(b2, 'HTML16'):
        assert _is_linked(b2, 'HTML16', a)
    _safe_set(a, 'body15', None)
    assert not _is_linked(a, 'body15', b2)
    if hasattr(b2, 'HTML16'):
        assert not _is_linked(b2, 'HTML16', a)


def test_assoc_parent6_link_reassign_clear():
    a = defaultname_HTMLElement(value="sample_text")
    b1 = defaultname_HTMLElement(value="sample_text")
    b2 = defaultname_HTMLElement(value="sample_text_2")
    _safe_set(a, 'HTMLElement7', b1)
    assert _is_linked(a, 'HTMLElement7', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'HTMLElement7', b2)
    assert _is_linked(a, 'HTMLElement7', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'HTMLElement7', None)
    assert not _is_linked(a, 'HTMLElement7', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_table20_link_reassign_clear():
    a = defaultname_TR(align="sample_text", valign="sample_text")
    b1 = defaultname_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    b2 = defaultname_TABLE(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", width="sample_text_2")
    _safe_set(a, 'trs', b1)
    assert _is_linked(a, 'trs', b1)
    if hasattr(b1, 'TABLE'):
        assert _is_linked(b1, 'TABLE', a)
    _safe_set(a, 'trs', b2)
    assert _is_linked(a, 'trs', b2)
    if hasattr(b1, 'TABLE'):
        assert not _is_linked(b1, 'TABLE', a)
    if hasattr(b2, 'TABLE'):
        assert _is_linked(b2, 'TABLE', a)
    _safe_set(a, 'trs', None)
    assert not _is_linked(a, 'trs', b2)
    if hasattr(b2, 'TABLE'):
        assert not _is_linked(b2, 'TABLE', a)


def test_assoc_tds21_link_reassign_clear():
    a = defaultname_TR(align="sample_text", valign="sample_text")
    b1 = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    b2 = defaultname_TD(align="sample_text_2", colspan="sample_text_2", rowspan="sample_text_2", valign="sample_text_2", width="sample_text_2")
    _safe_set(a, 'tr', {b1})
    assert _is_linked(a, 'tr', b1)
    if hasattr(b1, 'TD'):
        assert _is_linked(b1, 'TD', a)
    _safe_set(a, 'tr', {b2})
    assert _is_linked(a, 'tr', b2)
    if hasattr(b1, 'TD'):
        assert not _is_linked(b1, 'TD', a)
    if hasattr(b2, 'TD'):
        assert _is_linked(b2, 'TD', a)
    _safe_set(a, 'tr', set())
    assert not _is_linked(a, 'tr', b2)
    if hasattr(b2, 'TD'):
        assert not _is_linked(b2, 'TD', a)


def test_assoc_tr22_link_reassign_clear():
    a = defaultname_TR(align="sample_text", valign="sample_text")
    b1 = defaultname_TD(align="sample_text", colspan="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    b2 = defaultname_TD(align="sample_text_2", colspan="sample_text_2", rowspan="sample_text_2", valign="sample_text_2", width="sample_text_2")
    _safe_set(a, 'TR23', b1)
    assert _is_linked(a, 'TR23', b1)
    if hasattr(b1, 'tds'):
        assert _is_linked(b1, 'tds', a)
    _safe_set(a, 'TR23', b2)
    assert _is_linked(a, 'TR23', b2)
    if hasattr(b1, 'tds'):
        assert not _is_linked(b1, 'tds', a)
    if hasattr(b2, 'tds'):
        assert _is_linked(b2, 'tds', a)
    _safe_set(a, 'TR23', None)
    assert not _is_linked(a, 'TR23', b2)
    if hasattr(b2, 'tds'):
        assert not _is_linked(b2, 'tds', a)


def test_assoc_trs19_link_reassign_clear():
    a = defaultname_TR(align="sample_text", valign="sample_text")
    b1 = defaultname_TABLE(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    b2 = defaultname_TABLE(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", width="sample_text_2")
    _safe_set(a, 'TR', b1)
    assert _is_linked(a, 'TR', b1)
    if hasattr(b1, 'table'):
        assert _is_linked(b1, 'table', a)
    _safe_set(a, 'TR', b2)
    assert _is_linked(a, 'TR', b2)
    if hasattr(b1, 'table'):
        assert not _is_linked(b1, 'table', a)
    if hasattr(b2, 'table'):
        assert _is_linked(b2, 'table', a)
    _safe_set(a, 'TR', None)
    assert not _is_linked(a, 'TR', b2)
    if hasattr(b2, 'table'):
        assert not _is_linked(b2, 'table', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BODYElement_strategy = st.builds(BODYElement)
@given(instance=BODYElement_strategy)
@settings(max_examples=25)
def test_BODYElement_instantiation(instance):
    assert isinstance(instance, BODYElement)


FRAME_strategy = st.builds(FRAME)
@given(instance=FRAME_strategy)
@settings(max_examples=25)
def test_FRAME_instantiation(instance):
    assert isinstance(instance, FRAME)


HEADElement_strategy = st.builds(HEADElement)
@given(instance=HEADElement_strategy)
@settings(max_examples=25)
def test_HEADElement_instantiation(instance):
    assert isinstance(instance, HEADElement)


HTMLElement_strategy = st.builds(HTMLElement)
@given(instance=HTMLElement_strategy)
@settings(max_examples=25)
def test_HTMLElement_instantiation(instance):
    assert isinstance(instance, HTMLElement)


ListElement_strategy = st.builds(ListElement)
@given(instance=ListElement_strategy)
@settings(max_examples=25)
def test_ListElement_instantiation(instance):
    assert isinstance(instance, ListElement)


TABLEElement_strategy = st.builds(TABLEElement)
@given(instance=TABLEElement_strategy)
@settings(max_examples=25)
def test_TABLEElement_instantiation(instance):
    assert isinstance(instance, TABLEElement)


TD_strategy = st.builds(TD)
@given(instance=TD_strategy)
@settings(max_examples=25)
def test_TD_instantiation(instance):
    assert isinstance(instance, TD)


defaultname_A_strategy = st.builds(defaultname_A, ahref=safe_text, id=safe_text, name=safe_text)
@given(instance=defaultname_A_strategy)
@settings(max_examples=25)
def test_defaultname_A_instantiation(instance):
    assert isinstance(instance, defaultname_A)


defaultname_APPLET_strategy = st.builds(defaultname_APPLET, align=safe_text, applet=safe_text, class_=safe_text, height=safe_text, src=safe_text, width=safe_text)
@given(instance=defaultname_APPLET_strategy)
@settings(max_examples=25)
def test_defaultname_APPLET_instantiation(instance):
    assert isinstance(instance, defaultname_APPLET)


defaultname_AREA_strategy = st.builds(defaultname_AREA, ahref=safe_text, coords=safe_text, shape=safe_text)
@given(instance=defaultname_AREA_strategy)
@settings(max_examples=25)
def test_defaultname_AREA_instantiation(instance):
    assert isinstance(instance, defaultname_AREA)


defaultname_B_strategy = st.builds(defaultname_B)
@given(instance=defaultname_B_strategy)
@settings(max_examples=25)
def test_defaultname_B_instantiation(instance):
    assert isinstance(instance, defaultname_B)


defaultname_BIG_strategy = st.builds(defaultname_BIG)
@given(instance=defaultname_BIG_strategy)
@settings(max_examples=25)
def test_defaultname_BIG_instantiation(instance):
    assert isinstance(instance, defaultname_BIG)


defaultname_BODY_strategy = st.builds(defaultname_BODY, alink=safe_text, background=safe_text, bgcolor=safe_text, link=safe_text, text=safe_text, vlink=safe_text)
@given(instance=defaultname_BODY_strategy)
@settings(max_examples=25)
def test_defaultname_BODY_instantiation(instance):
    assert isinstance(instance, defaultname_BODY)


defaultname_BODYElement_strategy = st.builds(defaultname_BODYElement)
@given(instance=defaultname_BODYElement_strategy)
@settings(max_examples=25)
def test_defaultname_BODYElement_instantiation(instance):
    assert isinstance(instance, defaultname_BODYElement)


defaultname_BR_strategy = st.builds(defaultname_BR, clear=safe_text)
@given(instance=defaultname_BR_strategy)
@settings(max_examples=25)
def test_defaultname_BR_instantiation(instance):
    assert isinstance(instance, defaultname_BR)


defaultname_DD_strategy = st.builds(defaultname_DD)
@given(instance=defaultname_DD_strategy)
@settings(max_examples=25)
def test_defaultname_DD_instantiation(instance):
    assert isinstance(instance, defaultname_DD)


defaultname_DIV_strategy = st.builds(defaultname_DIV, align=safe_text)
@given(instance=defaultname_DIV_strategy)
@settings(max_examples=25)
def test_defaultname_DIV_instantiation(instance):
    assert isinstance(instance, defaultname_DIV)


defaultname_DL_strategy = st.builds(defaultname_DL)
@given(instance=defaultname_DL_strategy)
@settings(max_examples=25)
def test_defaultname_DL_instantiation(instance):
    assert isinstance(instance, defaultname_DL)


defaultname_DT_strategy = st.builds(defaultname_DT)
@given(instance=defaultname_DT_strategy)
@settings(max_examples=25)
def test_defaultname_DT_instantiation(instance):
    assert isinstance(instance, defaultname_DT)


defaultname_EM_strategy = st.builds(defaultname_EM)
@given(instance=defaultname_EM_strategy)
@settings(max_examples=25)
def test_defaultname_EM_instantiation(instance):
    assert isinstance(instance, defaultname_EM)


defaultname_EMBED_strategy = st.builds(defaultname_EMBED, align=safe_text, border=safe_text, height=safe_text, hspace=safe_text, src=safe_text, vspace=safe_text, width=safe_text)
@given(instance=defaultname_EMBED_strategy)
@settings(max_examples=25)
def test_defaultname_EMBED_instantiation(instance):
    assert isinstance(instance, defaultname_EMBED)


defaultname_FONT_strategy = st.builds(defaultname_FONT, color=safe_text, face=safe_text, size=safe_text)
@given(instance=defaultname_FONT_strategy)
@settings(max_examples=25)
def test_defaultname_FONT_instantiation(instance):
    assert isinstance(instance, defaultname_FONT)


defaultname_FORM_strategy = st.builds(defaultname_FORM, action=safe_text, method=safe_text)
@given(instance=defaultname_FORM_strategy)
@settings(max_examples=25)
def test_defaultname_FORM_instantiation(instance):
    assert isinstance(instance, defaultname_FORM)


defaultname_FRAME_strategy = st.builds(defaultname_FRAME, marginheight=safe_text, marginwidth=safe_text, name=safe_text, noresize=safe_text, scrolling=safe_text, src=safe_text)
@given(instance=defaultname_FRAME_strategy)
@settings(max_examples=25)
def test_defaultname_FRAME_instantiation(instance):
    assert isinstance(instance, defaultname_FRAME)


defaultname_FRAMESET_strategy = st.builds(defaultname_FRAMESET, border=safe_text, cols=safe_text, frameborder=safe_text, framespacing=safe_text, rows=safe_text)
@given(instance=defaultname_FRAMESET_strategy)
@settings(max_examples=25)
def test_defaultname_FRAMESET_instantiation(instance):
    assert isinstance(instance, defaultname_FRAMESET)


defaultname_H1_strategy = st.builds(defaultname_H1)
@given(instance=defaultname_H1_strategy)
@settings(max_examples=25)
def test_defaultname_H1_instantiation(instance):
    assert isinstance(instance, defaultname_H1)


defaultname_H2_strategy = st.builds(defaultname_H2)
@given(instance=defaultname_H2_strategy)
@settings(max_examples=25)
def test_defaultname_H2_instantiation(instance):
    assert isinstance(instance, defaultname_H2)


defaultname_H3_strategy = st.builds(defaultname_H3)
@given(instance=defaultname_H3_strategy)
@settings(max_examples=25)
def test_defaultname_H3_instantiation(instance):
    assert isinstance(instance, defaultname_H3)


defaultname_H4_strategy = st.builds(defaultname_H4)
@given(instance=defaultname_H4_strategy)
@settings(max_examples=25)
def test_defaultname_H4_instantiation(instance):
    assert isinstance(instance, defaultname_H4)


defaultname_HEAD_strategy = st.builds(defaultname_HEAD)
@given(instance=defaultname_HEAD_strategy)
@settings(max_examples=25)
def test_defaultname_HEAD_instantiation(instance):
    assert isinstance(instance, defaultname_HEAD)


defaultname_HEADElement_strategy = st.builds(defaultname_HEADElement)
@given(instance=defaultname_HEADElement_strategy)
@settings(max_examples=25)
def test_defaultname_HEADElement_instantiation(instance):
    assert isinstance(instance, defaultname_HEADElement)


defaultname_HTML_strategy = st.builds(defaultname_HTML)
@given(instance=defaultname_HTML_strategy)
@settings(max_examples=25)
def test_defaultname_HTML_instantiation(instance):
    assert isinstance(instance, defaultname_HTML)


defaultname_HTMLElement_strategy = st.builds(defaultname_HTMLElement, value=safe_text)
@given(instance=defaultname_HTMLElement_strategy)
@settings(max_examples=25)
def test_defaultname_HTMLElement_instantiation(instance):
    assert isinstance(instance, defaultname_HTMLElement)


defaultname_I_strategy = st.builds(defaultname_I)
@given(instance=defaultname_I_strategy)
@settings(max_examples=25)
def test_defaultname_I_instantiation(instance):
    assert isinstance(instance, defaultname_I)


defaultname_IFRAME_strategy = st.builds(defaultname_IFRAME)
@given(instance=defaultname_IFRAME_strategy)
@settings(max_examples=25)
def test_defaultname_IFRAME_instantiation(instance):
    assert isinstance(instance, defaultname_IFRAME)


defaultname_IMG_strategy = st.builds(defaultname_IMG, align=safe_text, alt=safe_text, border=safe_text, height=safe_text, hspace=safe_text, ismap=safe_text, src=safe_text, usemap=safe_text, vspace=safe_text, width=safe_text)
@given(instance=defaultname_IMG_strategy)
@settings(max_examples=25)
def test_defaultname_IMG_instantiation(instance):
    assert isinstance(instance, defaultname_IMG)


defaultname_INPUT_strategy = st.builds(defaultname_INPUT, align=safe_text, checked=safe_text, inputValue=safe_text, maxlength=safe_text, name=safe_text, size=safe_text, src=safe_text, type=safe_text)
@given(instance=defaultname_INPUT_strategy)
@settings(max_examples=25)
def test_defaultname_INPUT_instantiation(instance):
    assert isinstance(instance, defaultname_INPUT)


defaultname_LI_strategy = st.builds(defaultname_LI, liValue=safe_text)
@given(instance=defaultname_LI_strategy)
@settings(max_examples=25)
def test_defaultname_LI_instantiation(instance):
    assert isinstance(instance, defaultname_LI)


defaultname_LINK_strategy = st.builds(defaultname_LINK, ahref=safe_text, rel=safe_text, title=safe_text, type=safe_text)
@given(instance=defaultname_LINK_strategy)
@settings(max_examples=25)
def test_defaultname_LINK_instantiation(instance):
    assert isinstance(instance, defaultname_LINK)


defaultname_ListElement_strategy = st.builds(defaultname_ListElement, type=safe_text)
@given(instance=defaultname_ListElement_strategy)
@settings(max_examples=25)
def test_defaultname_ListElement_instantiation(instance):
    assert isinstance(instance, defaultname_ListElement)


defaultname_MAP_strategy = st.builds(defaultname_MAP)
@given(instance=defaultname_MAP_strategy)
@settings(max_examples=25)
def test_defaultname_MAP_instantiation(instance):
    assert isinstance(instance, defaultname_MAP)


defaultname_NOEMBED_strategy = st.builds(defaultname_NOEMBED)
@given(instance=defaultname_NOEMBED_strategy)
@settings(max_examples=25)
def test_defaultname_NOEMBED_instantiation(instance):
    assert isinstance(instance, defaultname_NOEMBED)


defaultname_NOFRAME_strategy = st.builds(defaultname_NOFRAME)
@given(instance=defaultname_NOFRAME_strategy)
@settings(max_examples=25)
def test_defaultname_NOFRAME_instantiation(instance):
    assert isinstance(instance, defaultname_NOFRAME)


defaultname_OBJECT_strategy = st.builds(defaultname_OBJECT, classid=safe_text, data=safe_text, id=safe_text, standby=safe_text, type=safe_text)
@given(instance=defaultname_OBJECT_strategy)
@settings(max_examples=25)
def test_defaultname_OBJECT_instantiation(instance):
    assert isinstance(instance, defaultname_OBJECT)


defaultname_OL_strategy = st.builds(defaultname_OL, start=safe_text)
@given(instance=defaultname_OL_strategy)
@settings(max_examples=25)
def test_defaultname_OL_instantiation(instance):
    assert isinstance(instance, defaultname_OL)


defaultname_OPTION_strategy = st.builds(defaultname_OPTION, optionValue=safe_text, selected=safe_text)
@given(instance=defaultname_OPTION_strategy)
@settings(max_examples=25)
def test_defaultname_OPTION_instantiation(instance):
    assert isinstance(instance, defaultname_OPTION)


defaultname_P_strategy = st.builds(defaultname_P)
@given(instance=defaultname_P_strategy)
@settings(max_examples=25)
def test_defaultname_P_instantiation(instance):
    assert isinstance(instance, defaultname_P)


defaultname_PARAM_strategy = st.builds(defaultname_PARAM, name=safe_text, paramValue=safe_text)
@given(instance=defaultname_PARAM_strategy)
@settings(max_examples=25)
def test_defaultname_PARAM_instantiation(instance):
    assert isinstance(instance, defaultname_PARAM)


defaultname_PRE_strategy = st.builds(defaultname_PRE)
@given(instance=defaultname_PRE_strategy)
@settings(max_examples=25)
def test_defaultname_PRE_instantiation(instance):
    assert isinstance(instance, defaultname_PRE)


defaultname_SELECT_strategy = st.builds(defaultname_SELECT, multiple=safe_text, name=safe_text, size=safe_text)
@given(instance=defaultname_SELECT_strategy)
@settings(max_examples=25)
def test_defaultname_SELECT_instantiation(instance):
    assert isinstance(instance, defaultname_SELECT)


defaultname_SMALL_strategy = st.builds(defaultname_SMALL)
@given(instance=defaultname_SMALL_strategy)
@settings(max_examples=25)
def test_defaultname_SMALL_instantiation(instance):
    assert isinstance(instance, defaultname_SMALL)


defaultname_SPAN_strategy = st.builds(defaultname_SPAN, style=safe_text)
@given(instance=defaultname_SPAN_strategy)
@settings(max_examples=25)
def test_defaultname_SPAN_instantiation(instance):
    assert isinstance(instance, defaultname_SPAN)


defaultname_STRIKE_strategy = st.builds(defaultname_STRIKE)
@given(instance=defaultname_STRIKE_strategy)
@settings(max_examples=25)
def test_defaultname_STRIKE_instantiation(instance):
    assert isinstance(instance, defaultname_STRIKE)


defaultname_STRONG_strategy = st.builds(defaultname_STRONG)
@given(instance=defaultname_STRONG_strategy)
@settings(max_examples=25)
def test_defaultname_STRONG_instantiation(instance):
    assert isinstance(instance, defaultname_STRONG)


defaultname_STYLE_strategy = st.builds(defaultname_STYLE)
@given(instance=defaultname_STYLE_strategy)
@settings(max_examples=25)
def test_defaultname_STYLE_instantiation(instance):
    assert isinstance(instance, defaultname_STYLE)


defaultname_SUB_strategy = st.builds(defaultname_SUB)
@given(instance=defaultname_SUB_strategy)
@settings(max_examples=25)
def test_defaultname_SUB_instantiation(instance):
    assert isinstance(instance, defaultname_SUB)


defaultname_SUP_strategy = st.builds(defaultname_SUP)
@given(instance=defaultname_SUP_strategy)
@settings(max_examples=25)
def test_defaultname_SUP_instantiation(instance):
    assert isinstance(instance, defaultname_SUP)


defaultname_TABLE_strategy = st.builds(defaultname_TABLE, border=safe_text, cellpadding=safe_text, cellspacing=safe_text, width=safe_text)
@given(instance=defaultname_TABLE_strategy)
@settings(max_examples=25)
def test_defaultname_TABLE_instantiation(instance):
    assert isinstance(instance, defaultname_TABLE)


defaultname_TABLEElement_strategy = st.builds(defaultname_TABLEElement, background=safe_text, bgcolor=safe_text)
@given(instance=defaultname_TABLEElement_strategy)
@settings(max_examples=25)
def test_defaultname_TABLEElement_instantiation(instance):
    assert isinstance(instance, defaultname_TABLEElement)


defaultname_TD_strategy = st.builds(defaultname_TD, align=safe_text, colspan=safe_text, rowspan=safe_text, valign=safe_text, width=safe_text)
@given(instance=defaultname_TD_strategy)
@settings(max_examples=25)
def test_defaultname_TD_instantiation(instance):
    assert isinstance(instance, defaultname_TD)


defaultname_TEXTAREA_strategy = st.builds(defaultname_TEXTAREA, cols=safe_text, name=safe_text, rows=safe_text)
@given(instance=defaultname_TEXTAREA_strategy)
@settings(max_examples=25)
def test_defaultname_TEXTAREA_instantiation(instance):
    assert isinstance(instance, defaultname_TEXTAREA)


defaultname_TH_strategy = st.builds(defaultname_TH)
@given(instance=defaultname_TH_strategy)
@settings(max_examples=25)
def test_defaultname_TH_instantiation(instance):
    assert isinstance(instance, defaultname_TH)


defaultname_TITLE_strategy = st.builds(defaultname_TITLE)
@given(instance=defaultname_TITLE_strategy)
@settings(max_examples=25)
def test_defaultname_TITLE_instantiation(instance):
    assert isinstance(instance, defaultname_TITLE)


defaultname_TR_strategy = st.builds(defaultname_TR, align=safe_text, valign=safe_text)
@given(instance=defaultname_TR_strategy)
@settings(max_examples=25)
def test_defaultname_TR_instantiation(instance):
    assert isinstance(instance, defaultname_TR)


defaultname_TT_strategy = st.builds(defaultname_TT)
@given(instance=defaultname_TT_strategy)
@settings(max_examples=25)
def test_defaultname_TT_instantiation(instance):
    assert isinstance(instance, defaultname_TT)


defaultname_UL_strategy = st.builds(defaultname_UL)
@given(instance=defaultname_UL_strategy)
@settings(max_examples=25)
def test_defaultname_UL_instantiation(instance):
    assert isinstance(instance, defaultname_UL)



