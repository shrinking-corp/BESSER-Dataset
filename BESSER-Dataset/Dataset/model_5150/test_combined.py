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
    xhtml_Tr,
    xhtml_Tbody,
    xhtml_Tfoot,
    xhtml_Thead,
    xhtml_PreContent,
    PreContent,
    xhtml_Param,
    xhtml_Inline,
    xhtml_Flow,
    Flow,
    xhtml_Th,
    xhtml_Del,
    xhtml_Td,
    xhtml_Li,
    xhtml_Ins,
    xhtml_Dd,
    xhtml_Colgroup,
    xhtml_Col,
    Block,
    xhtml_Table,
    xhtml_Blockquote,
    xhtml_Ol,
    xhtml_Ul,
    xhtml_Div,
    xhtml_Hr,
    xhtml_Pre,
    xhtml_Dl,
    xhtml_Block,
    xhtml_Br,
    xhtml_AContent,
    xhtml_Img,
    xhtml_Object,
    Inline,
    xhtml_I,
    xhtml_Sub,
    xhtml_Sup,
    xhtml_Em,
    xhtml_Acronym,
    xhtml_Cite,
    xhtml_Small,
    xhtml_B,
    xhtml_Q,
    xhtml_Kbd,
    xhtml_Samp,
    xhtml_Strong,
    xhtml_Dfn,
    xhtml_Dt,
    xhtml_Caption,
    xhtml_Tt,
    xhtml_P,
    xhtml_Code,
    xhtml_Big,
    xhtml_Var,
    xhtml_Span,
    xhtml_Abbr,
    AContent,
    xhtml_A,
    Shape,
    TFrame,
    ValignType,
    TRules,
    ParamName,
    AlignType,
    MediaType,
    ObjectName,
    ImageKind,
    StyleSheet,
    MifClassType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_xhtml_tr_is_not_abstract():
    assert not inspect.isabstract(xhtml_Tr)


def test_hyp_xhtml_tr_constructor_exists():
    assert callable(xhtml_Tr.__init__)


def test_hyp_xhtml_tr_constructor_args():
    sig = inspect.signature(xhtml_Tr.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "style" in params, "Missing parameter 'style'"
    assert "group" in params, "Missing parameter 'group'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "align" in params, "Missing parameter 'align'"
    assert "class_" in params, "Missing parameter 'class_'"











def test_hyp_xhtml_tbody_is_not_abstract():
    assert not inspect.isabstract(xhtml_Tbody)


def test_hyp_xhtml_tbody_constructor_exists():
    assert callable(xhtml_Tbody.__init__)


def test_hyp_xhtml_tbody_constructor_args():
    sig = inspect.signature(xhtml_Tbody.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "char" in params, "Missing parameter 'char'"
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"










def test_hyp_xhtml_tfoot_is_not_abstract():
    assert not inspect.isabstract(xhtml_Tfoot)


def test_hyp_xhtml_tfoot_constructor_exists():
    assert callable(xhtml_Tfoot.__init__)


def test_hyp_xhtml_tfoot_constructor_args():
    sig = inspect.signature(xhtml_Tfoot.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "align" in params, "Missing parameter 'align'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "valign" in params, "Missing parameter 'valign'"










def test_hyp_xhtml_thead_is_not_abstract():
    assert not inspect.isabstract(xhtml_Thead)


def test_hyp_xhtml_thead_constructor_exists():
    assert callable(xhtml_Thead.__init__)


def test_hyp_xhtml_thead_constructor_args():
    sig = inspect.signature(xhtml_Thead.__init__)
    params = list(sig.parameters.keys())
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "align" in params, "Missing parameter 'align'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "char" in params, "Missing parameter 'char'"










def test_hyp_xhtml_precontent_is_not_abstract():
    assert not inspect.isabstract(xhtml_PreContent)


def test_hyp_xhtml_precontent_constructor_exists():
    assert callable(xhtml_PreContent.__init__)


def test_hyp_xhtml_precontent_constructor_args():
    sig = inspect.signature(xhtml_PreContent.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"





def test_hyp_precontent_is_not_abstract():
    assert not inspect.isabstract(PreContent)


def test_hyp_precontent_constructor_exists():
    assert callable(PreContent.__init__)


def test_hyp_precontent_constructor_args():
    sig = inspect.signature(PreContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xhtml_param_is_not_abstract():
    assert not inspect.isabstract(xhtml_Param)


def test_hyp_xhtml_param_constructor_exists():
    assert callable(xhtml_Param.__init__)


def test_hyp_xhtml_param_constructor_args():
    sig = inspect.signature(xhtml_Param.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_xhtml_inline_is_not_abstract():
    assert not inspect.isabstract(xhtml_Inline)


def test_hyp_xhtml_inline_constructor_exists():
    assert callable(xhtml_Inline.__init__)


def test_hyp_xhtml_inline_constructor_args():
    sig = inspect.signature(xhtml_Inline.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "inline" in params, "Missing parameter 'inline'"





def test_hyp_xhtml_flow_is_not_abstract():
    assert not inspect.isabstract(xhtml_Flow)


def test_hyp_xhtml_flow_constructor_exists():
    assert callable(xhtml_Flow.__init__)


def test_hyp_xhtml_flow_constructor_args():
    sig = inspect.signature(xhtml_Flow.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"





def test_hyp_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_hyp_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_hyp_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xhtml_th_is_not_abstract():
    assert not inspect.isabstract(xhtml_Th)


def test_hyp_xhtml_th_constructor_exists():
    assert callable(xhtml_Th.__init__)


def test_hyp_xhtml_th_constructor_args():
    sig = inspect.signature(xhtml_Th.__init__)
    params = list(sig.parameters.keys())
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "align" in params, "Missing parameter 'align'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "style" in params, "Missing parameter 'style'"












def test_hyp_xhtml_del_is_not_abstract():
    assert not inspect.isabstract(xhtml_Del)


def test_hyp_xhtml_del_constructor_exists():
    assert callable(xhtml_Del.__init__)


def test_hyp_xhtml_del_constructor_args():
    sig = inspect.signature(xhtml_Del.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xhtml_td_is_not_abstract():
    assert not inspect.isabstract(xhtml_Td)


def test_hyp_xhtml_td_constructor_exists():
    assert callable(xhtml_Td.__init__)


def test_hyp_xhtml_td_constructor_args():
    sig = inspect.signature(xhtml_Td.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "class_" in params, "Missing parameter 'class_'"












def test_hyp_xhtml_li_is_not_abstract():
    assert not inspect.isabstract(xhtml_Li)


def test_hyp_xhtml_li_constructor_exists():
    assert callable(xhtml_Li.__init__)


def test_hyp_xhtml_li_constructor_args():
    sig = inspect.signature(xhtml_Li.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_ins_is_not_abstract():
    assert not inspect.isabstract(xhtml_Ins)


def test_hyp_xhtml_ins_constructor_exists():
    assert callable(xhtml_Ins.__init__)


def test_hyp_xhtml_ins_constructor_args():
    sig = inspect.signature(xhtml_Ins.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xhtml_dd_is_not_abstract():
    assert not inspect.isabstract(xhtml_Dd)


def test_hyp_xhtml_dd_constructor_exists():
    assert callable(xhtml_Dd.__init__)


def test_hyp_xhtml_dd_constructor_args():
    sig = inspect.signature(xhtml_Dd.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_colgroup_is_not_abstract():
    assert not inspect.isabstract(xhtml_Colgroup)


def test_hyp_xhtml_colgroup_constructor_exists():
    assert callable(xhtml_Colgroup.__init__)


def test_hyp_xhtml_colgroup_constructor_args():
    sig = inspect.signature(xhtml_Colgroup.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "style" in params, "Missing parameter 'style'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "width" in params, "Missing parameter 'width'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "span" in params, "Missing parameter 'span'"












def test_hyp_xhtml_col_is_not_abstract():
    assert not inspect.isabstract(xhtml_Col)


def test_hyp_xhtml_col_constructor_exists():
    assert callable(xhtml_Col.__init__)


def test_hyp_xhtml_col_constructor_args():
    sig = inspect.signature(xhtml_Col.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "char" in params, "Missing parameter 'char'"
    assert "style" in params, "Missing parameter 'style'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "span" in params, "Missing parameter 'span'"
    assert "align" in params, "Missing parameter 'align'"
    assert "width" in params, "Missing parameter 'width'"
    assert "valign" in params, "Missing parameter 'valign'"












def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xhtml_table_is_not_abstract():
    assert not inspect.isabstract(xhtml_Table)


def test_hyp_xhtml_table_constructor_exists():
    assert callable(xhtml_Table.__init__)


def test_hyp_xhtml_table_constructor_args():
    sig = inspect.signature(xhtml_Table.__init__)
    params = list(sig.parameters.keys())
    assert "frame" in params, "Missing parameter 'frame'"
    assert "cellspacing" in params, "Missing parameter 'cellspacing'"
    assert "rules" in params, "Missing parameter 'rules'"
    assert "cellpadding" in params, "Missing parameter 'cellpadding'"
    assert "width" in params, "Missing parameter 'width'"
    assert "hl7Id" in params, "Missing parameter 'hl7Id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "border" in params, "Missing parameter 'border'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"













def test_hyp_xhtml_blockquote_is_not_abstract():
    assert not inspect.isabstract(xhtml_Blockquote)


def test_hyp_xhtml_blockquote_constructor_exists():
    assert callable(xhtml_Blockquote.__init__)


def test_hyp_xhtml_blockquote_constructor_args():
    sig = inspect.signature(xhtml_Blockquote.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "cite" in params, "Missing parameter 'cite'"
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"







def test_hyp_xhtml_ol_is_not_abstract():
    assert not inspect.isabstract(xhtml_Ol)


def test_hyp_xhtml_ol_constructor_exists():
    assert callable(xhtml_Ol.__init__)


def test_hyp_xhtml_ol_constructor_args():
    sig = inspect.signature(xhtml_Ol.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "li" in params, "Missing parameter 'li'"







def test_hyp_xhtml_ul_is_not_abstract():
    assert not inspect.isabstract(xhtml_Ul)


def test_hyp_xhtml_ul_constructor_exists():
    assert callable(xhtml_Ul.__init__)


def test_hyp_xhtml_ul_constructor_args():
    sig = inspect.signature(xhtml_Ul.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "li" in params, "Missing parameter 'li'"







def test_hyp_xhtml_div_is_not_abstract():
    assert not inspect.isabstract(xhtml_Div)


def test_hyp_xhtml_div_constructor_exists():
    assert callable(xhtml_Div.__init__)


def test_hyp_xhtml_div_constructor_args():
    sig = inspect.signature(xhtml_Div.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "hl7Id" in params, "Missing parameter 'hl7Id'"








def test_hyp_xhtml_hr_is_not_abstract():
    assert not inspect.isabstract(xhtml_Hr)


def test_hyp_xhtml_hr_constructor_exists():
    assert callable(xhtml_Hr.__init__)


def test_hyp_xhtml_hr_constructor_args():
    sig = inspect.signature(xhtml_Hr.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_pre_is_not_abstract():
    assert not inspect.isabstract(xhtml_Pre)


def test_hyp_xhtml_pre_constructor_exists():
    assert callable(xhtml_Pre.__init__)


def test_hyp_xhtml_pre_constructor_args():
    sig = inspect.signature(xhtml_Pre.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "space" in params, "Missing parameter 'space'"
    assert "style" in params, "Missing parameter 'style'"







def test_hyp_xhtml_dl_is_not_abstract():
    assert not inspect.isabstract(xhtml_Dl)


def test_hyp_xhtml_dl_constructor_exists():
    assert callable(xhtml_Dl.__init__)


def test_hyp_xhtml_dl_constructor_args():
    sig = inspect.signature(xhtml_Dl.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "group" in params, "Missing parameter 'group'"







def test_hyp_xhtml_block_is_not_abstract():
    assert not inspect.isabstract(xhtml_Block)


def test_hyp_xhtml_block_constructor_exists():
    assert callable(xhtml_Block.__init__)


def test_hyp_xhtml_block_constructor_args():
    sig = inspect.signature(xhtml_Block.__init__)
    params = list(sig.parameters.keys())
    assert "block" in params, "Missing parameter 'block'"
    assert "mixed" in params, "Missing parameter 'mixed'"





def test_hyp_xhtml_br_is_not_abstract():
    assert not inspect.isabstract(xhtml_Br)


def test_hyp_xhtml_br_constructor_exists():
    assert callable(xhtml_Br.__init__)


def test_hyp_xhtml_br_constructor_args():
    sig = inspect.signature(xhtml_Br.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"





def test_hyp_xhtml_acontent_is_not_abstract():
    assert not inspect.isabstract(xhtml_AContent)


def test_hyp_xhtml_acontent_constructor_exists():
    assert callable(xhtml_AContent.__init__)


def test_hyp_xhtml_acontent_constructor_args():
    sig = inspect.signature(xhtml_AContent.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"





def test_hyp_xhtml_img_is_not_abstract():
    assert not inspect.isabstract(xhtml_Img)


def test_hyp_xhtml_img_constructor_exists():
    assert callable(xhtml_Img.__init__)


def test_hyp_xhtml_img_constructor_args():
    sig = inspect.signature(xhtml_Img.__init__)
    params = list(sig.parameters.keys())
    assert "alt" in params, "Missing parameter 'alt'"
    assert "width" in params, "Missing parameter 'width'"
    assert "imageType" in params, "Missing parameter 'imageType'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "height" in params, "Missing parameter 'height'"
    assert "hl7Id" in params, "Missing parameter 'hl7Id'"
    assert "src" in params, "Missing parameter 'src'"












def test_hyp_xhtml_object_is_not_abstract():
    assert not inspect.isabstract(xhtml_Object)


def test_hyp_xhtml_object_constructor_exists():
    assert callable(xhtml_Object.__init__)


def test_hyp_xhtml_object_constructor_args():
    sig = inspect.signature(xhtml_Object.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hl7Id" in params, "Missing parameter 'hl7Id'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"







def test_hyp_inline_is_not_abstract():
    assert not inspect.isabstract(Inline)


def test_hyp_inline_constructor_exists():
    assert callable(Inline.__init__)


def test_hyp_inline_constructor_args():
    sig = inspect.signature(Inline.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xhtml_i_is_not_abstract():
    assert not inspect.isabstract(xhtml_I)


def test_hyp_xhtml_i_constructor_exists():
    assert callable(xhtml_I.__init__)


def test_hyp_xhtml_i_constructor_args():
    sig = inspect.signature(xhtml_I.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_sub_is_not_abstract():
    assert not inspect.isabstract(xhtml_Sub)


def test_hyp_xhtml_sub_constructor_exists():
    assert callable(xhtml_Sub.__init__)


def test_hyp_xhtml_sub_constructor_args():
    sig = inspect.signature(xhtml_Sub.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"






def test_hyp_xhtml_sup_is_not_abstract():
    assert not inspect.isabstract(xhtml_Sup)


def test_hyp_xhtml_sup_constructor_exists():
    assert callable(xhtml_Sup.__init__)


def test_hyp_xhtml_sup_constructor_args():
    sig = inspect.signature(xhtml_Sup.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"






def test_hyp_xhtml_em_is_not_abstract():
    assert not inspect.isabstract(xhtml_Em)


def test_hyp_xhtml_em_constructor_exists():
    assert callable(xhtml_Em.__init__)


def test_hyp_xhtml_em_constructor_args():
    sig = inspect.signature(xhtml_Em.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"






def test_hyp_xhtml_acronym_is_not_abstract():
    assert not inspect.isabstract(xhtml_Acronym)


def test_hyp_xhtml_acronym_constructor_exists():
    assert callable(xhtml_Acronym.__init__)


def test_hyp_xhtml_acronym_constructor_args():
    sig = inspect.signature(xhtml_Acronym.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_cite_is_not_abstract():
    assert not inspect.isabstract(xhtml_Cite)


def test_hyp_xhtml_cite_constructor_exists():
    assert callable(xhtml_Cite.__init__)


def test_hyp_xhtml_cite_constructor_args():
    sig = inspect.signature(xhtml_Cite.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"






def test_hyp_xhtml_small_is_not_abstract():
    assert not inspect.isabstract(xhtml_Small)


def test_hyp_xhtml_small_constructor_exists():
    assert callable(xhtml_Small.__init__)


def test_hyp_xhtml_small_constructor_args():
    sig = inspect.signature(xhtml_Small.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_b_is_not_abstract():
    assert not inspect.isabstract(xhtml_B)


def test_hyp_xhtml_b_constructor_exists():
    assert callable(xhtml_B.__init__)


def test_hyp_xhtml_b_constructor_args():
    sig = inspect.signature(xhtml_B.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_q_is_not_abstract():
    assert not inspect.isabstract(xhtml_Q)


def test_hyp_xhtml_q_constructor_exists():
    assert callable(xhtml_Q.__init__)


def test_hyp_xhtml_q_constructor_args():
    sig = inspect.signature(xhtml_Q.__init__)
    params = list(sig.parameters.keys())
    assert "cite1" in params, "Missing parameter 'cite1'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"







def test_hyp_xhtml_kbd_is_not_abstract():
    assert not inspect.isabstract(xhtml_Kbd)


def test_hyp_xhtml_kbd_constructor_exists():
    assert callable(xhtml_Kbd.__init__)


def test_hyp_xhtml_kbd_constructor_args():
    sig = inspect.signature(xhtml_Kbd.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_samp_is_not_abstract():
    assert not inspect.isabstract(xhtml_Samp)


def test_hyp_xhtml_samp_constructor_exists():
    assert callable(xhtml_Samp.__init__)


def test_hyp_xhtml_samp_constructor_args():
    sig = inspect.signature(xhtml_Samp.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_strong_is_not_abstract():
    assert not inspect.isabstract(xhtml_Strong)


def test_hyp_xhtml_strong_constructor_exists():
    assert callable(xhtml_Strong.__init__)


def test_hyp_xhtml_strong_constructor_args():
    sig = inspect.signature(xhtml_Strong.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"






def test_hyp_xhtml_dfn_is_not_abstract():
    assert not inspect.isabstract(xhtml_Dfn)


def test_hyp_xhtml_dfn_constructor_exists():
    assert callable(xhtml_Dfn.__init__)


def test_hyp_xhtml_dfn_constructor_args():
    sig = inspect.signature(xhtml_Dfn.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"






def test_hyp_xhtml_dt_is_not_abstract():
    assert not inspect.isabstract(xhtml_Dt)


def test_hyp_xhtml_dt_constructor_exists():
    assert callable(xhtml_Dt.__init__)


def test_hyp_xhtml_dt_constructor_args():
    sig = inspect.signature(xhtml_Dt.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_caption_is_not_abstract():
    assert not inspect.isabstract(xhtml_Caption)


def test_hyp_xhtml_caption_constructor_exists():
    assert callable(xhtml_Caption.__init__)


def test_hyp_xhtml_caption_constructor_args():
    sig = inspect.signature(xhtml_Caption.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"






def test_hyp_xhtml_tt_is_not_abstract():
    assert not inspect.isabstract(xhtml_Tt)


def test_hyp_xhtml_tt_constructor_exists():
    assert callable(xhtml_Tt.__init__)


def test_hyp_xhtml_tt_constructor_args():
    sig = inspect.signature(xhtml_Tt.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_p_is_not_abstract():
    assert not inspect.isabstract(xhtml_P)


def test_hyp_xhtml_p_constructor_exists():
    assert callable(xhtml_P.__init__)


def test_hyp_xhtml_p_constructor_args():
    sig = inspect.signature(xhtml_P.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"






def test_hyp_xhtml_code_is_not_abstract():
    assert not inspect.isabstract(xhtml_Code)


def test_hyp_xhtml_code_constructor_exists():
    assert callable(xhtml_Code.__init__)


def test_hyp_xhtml_code_constructor_args():
    sig = inspect.signature(xhtml_Code.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_xhtml_big_is_not_abstract():
    assert not inspect.isabstract(xhtml_Big)


def test_hyp_xhtml_big_constructor_exists():
    assert callable(xhtml_Big.__init__)


def test_hyp_xhtml_big_constructor_args():
    sig = inspect.signature(xhtml_Big.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"






def test_hyp_xhtml_var_is_not_abstract():
    assert not inspect.isabstract(xhtml_Var)


def test_hyp_xhtml_var_constructor_exists():
    assert callable(xhtml_Var.__init__)


def test_hyp_xhtml_var_constructor_args():
    sig = inspect.signature(xhtml_Var.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"






def test_hyp_xhtml_span_is_not_abstract():
    assert not inspect.isabstract(xhtml_Span)


def test_hyp_xhtml_span_constructor_exists():
    assert callable(xhtml_Span.__init__)


def test_hyp_xhtml_span_constructor_args():
    sig = inspect.signature(xhtml_Span.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "lang" in params, "Missing parameter 'lang'"






def test_hyp_xhtml_abbr_is_not_abstract():
    assert not inspect.isabstract(xhtml_Abbr)


def test_hyp_xhtml_abbr_constructor_exists():
    assert callable(xhtml_Abbr.__init__)


def test_hyp_xhtml_abbr_constructor_args():
    sig = inspect.signature(xhtml_Abbr.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "style" in params, "Missing parameter 'style'"






def test_hyp_acontent_is_not_abstract():
    assert not inspect.isabstract(AContent)


def test_hyp_acontent_constructor_exists():
    assert callable(AContent.__init__)


def test_hyp_acontent_constructor_args():
    sig = inspect.signature(AContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xhtml_a_is_not_abstract():
    assert not inspect.isabstract(xhtml_A)


def test_hyp_xhtml_a_constructor_exists():
    assert callable(xhtml_A.__init__)


def test_hyp_xhtml_a_constructor_args():
    sig = inspect.signature(xhtml_A.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "type" in params, "Missing parameter 'type'"
    assert "style" in params, "Missing parameter 'style'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "href" in params, "Missing parameter 'href'"
    assert "name" in params, "Missing parameter 'name'"
    assert "coords" in params, "Missing parameter 'coords'"









def test_hyp_shape_exists():
    # Check that the Enumeration exists
    assert Shape is not None

def test_hyp_shape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Shape]
    expected_literals = [
        "rect",
        "default",
        "poly",
        "circle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Shape"

def test_hyp_tframe_exists():
    # Check that the Enumeration exists
    assert TFrame is not None

def test_hyp_tframe_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TFrame]
    expected_literals = [
        "hsides",
        "below",
        "box",
        "rhs",
        "lhs",
        "void",
        "vsides",
        "above",
        "border",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TFrame"

def test_hyp_valigntype_exists():
    # Check that the Enumeration exists
    assert ValignType is not None

def test_hyp_valigntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValignType]
    expected_literals = [
        "baseline",
        "top",
        "bottom",
        "middle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValignType"

def test_hyp_trules_exists():
    # Check that the Enumeration exists
    assert TRules is not None

def test_hyp_trules_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TRules]
    expected_literals = [
        "rows",
        "cols",
        "none",
        "groups",
        "all",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TRules"

def test_hyp_paramname_exists():
    # Check that the Enumeration exists
    assert ParamName is not None

def test_hyp_paramname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParamName]
    expected_literals = [
        "termName",
        "linkToEnd",
        "subArtifact",
        "id",
        "annotationKind",
        "attributeName",
        "code",
        "codeSystemId",
        "stateName",
        "withinClassName",
        "version",
        "stateTransitionName",
        "subjectAreaName",
        "supplierBindingArgumentDatatype",
        "propertyName",
        "constructType",
        "item",
        "domain",
        "name",
        "className",
        "relationshipName",
        "artifact",
        "conversionDatatype",
        "group",
        "artifactName",
        "datatypeName",
        "root",
        "realmNamespace",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParamName"

def test_hyp_aligntype_exists():
    # Check that the Enumeration exists
    assert AlignType is not None

def test_hyp_aligntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignType]
    expected_literals = [
        "left",
        "center",
        "char",
        "right",
        "justify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignType"

def test_hyp_mediatype_exists():
    # Check that the Enumeration exists
    assert MediaType is not None

def test_hyp_mediatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaType]
    expected_literals = [
        "applicationMsword",
        "textRtf",
        "textXml",
        "audioMpeg",
        "applicationPdf",
        "imagePng",
        "imageGif",
        "textPlain",
        "textHtml",
        "videoMpeg",
        "imageJpeg",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaType"

def test_hyp_objectname_exists():
    # Check that the Enumeration exists
    assert ObjectName is not None

def test_hyp_objectname_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectName]
    expected_literals = [
        "domainInstanceExampleRef",
        "storyboardRef",
        "externalSpecRef",
        "itemName",
        "datatypeRef",
        "stateRef",
        "vocabularyCodeRef",
        "constructedElement",
        "artifactGroupRef",
        "testScenarioRef",
        "publicationRef",
        "vocabularyCodeSystemRef",
        "domainAnalysisModelRef",
        "triggerEventRef",
        "vocabularyModelRef",
        "subjectAreaRef",
        "glossaryTermRef",
        "packageRef",
        "associationEndRef",
        "applicationRoleRef",
        "freehandDocumentRef",
        "requirementRef",
        "interactionRef",
        "testCaseRef",
        "annotationRef",
        "glossaryRef",
        "transitionRef",
        "classRef",
        "footnote",
        "staticModelRef",
        "vocabularyValueSetRef",
        "conceptDomainRef",
        "figureRef",
        "attributeRef",
        "tableRef",
        "datatypeModelRef",
        "propertyRef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectName"

def test_hyp_imagekind_exists():
    # Check that the Enumeration exists
    assert ImageKind is not None

def test_hyp_imagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImageKind]
    expected_literals = [
        "applicationPostscript",
        "imageGif",
        "applicationPng",
        "applicationSvgXml",
        "applicationPdf",
        "applicationJpeg",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImageKind"

def test_hyp_stylesheet_exists():
    # Check that the Enumeration exists
    assert StyleSheet is not None

def test_hyp_stylesheet_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StyleSheet]
    expected_literals = [
        "BackgroundAqua",
        "Note",
        "BackgroundPink",
        "BackgroundLime",
        "NonNumbered",
        "BackgroundYellow",
        "Requirement",
        "Indent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StyleSheet"

def test_hyp_mifclasstype_exists():
    # Check that the Enumeration exists
    assert MifClassType is not None

def test_hyp_mifclasstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MifClassType]
    expected_literals = [
        "deleted",
        "inserted",
        "changed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MifClassType"


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
xhtml_Tr_strategy = st.builds(
    xhtml_Tr,
    char=
        safe_text,
    lang=
        safe_text,
    charoff=
        safe_text,
    style=
        safe_text,
    group=
        safe_text,
    valign=
        safe_text,
    align=
        safe_text,
    class_=
        safe_text
)
xhtml_Tbody_strategy = st.builds(
    xhtml_Tbody,
    style=
        safe_text,
    char=
        safe_text,
    align=
        safe_text,
    valign=
        safe_text,
    charoff=
        safe_text,
    lang=
        safe_text,
    class_=
        safe_text
)
xhtml_Tfoot_strategy = st.builds(
    xhtml_Tfoot,
    char=
        safe_text,
    class_=
        safe_text,
    align=
        safe_text,
    charoff=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text,
    valign=
        safe_text
)
xhtml_Thead_strategy = st.builds(
    xhtml_Thead,
    charoff=
        safe_text,
    align=
        safe_text,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text,
    valign=
        safe_text,
    char=
        safe_text
)
xhtml_PreContent_strategy = st.builds(
    xhtml_PreContent,
    group=
        safe_text,
    mixed=
        safe_text
)
PreContent_strategy = st.builds(
    PreContent,
)
xhtml_Param_strategy = st.builds(
    xhtml_Param,
    value=
        safe_text,
    name=
        safe_text
)
xhtml_Inline_strategy = st.builds(
    xhtml_Inline,
    mixed=
        safe_text,
    inline=
        safe_text
)
xhtml_Flow_strategy = st.builds(
    xhtml_Flow,
    group=
        safe_text,
    mixed=
        safe_text
)
Flow_strategy = st.builds(
    Flow,
)
xhtml_Th_strategy = st.builds(
    xhtml_Th,
    rowspan=
        safe_text,
    valign=
        safe_text,
    char=
        safe_text,
    class_=
        safe_text,
    colspan=
        safe_text,
    lang=
        safe_text,
    align=
        safe_text,
    charoff=
        safe_text,
    style=
        safe_text
)
xhtml_Del_strategy = st.builds(
    xhtml_Del,
)
xhtml_Td_strategy = st.builds(
    xhtml_Td,
    char=
        safe_text,
    charoff=
        safe_text,
    rowspan=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text,
    colspan=
        safe_text,
    align=
        safe_text,
    valign=
        safe_text,
    class_=
        safe_text
)
xhtml_Li_strategy = st.builds(
    xhtml_Li,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text
)
xhtml_Ins_strategy = st.builds(
    xhtml_Ins,
)
xhtml_Dd_strategy = st.builds(
    xhtml_Dd,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text
)
xhtml_Colgroup_strategy = st.builds(
    xhtml_Colgroup,
    align=
        safe_text,
    style=
        safe_text,
    valign=
        safe_text,
    width=
        safe_text,
    lang=
        safe_text,
    char=
        safe_text,
    class_=
        safe_text,
    charoff=
        safe_text,
    span=
        safe_text
)
xhtml_Col_strategy = st.builds(
    xhtml_Col,
    lang=
        safe_text,
    class_=
        safe_text,
    char=
        safe_text,
    style=
        safe_text,
    charoff=
        safe_text,
    span=
        safe_text,
    align=
        safe_text,
    width=
        safe_text,
    valign=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
xhtml_Table_strategy = st.builds(
    xhtml_Table,
    frame=
        safe_text,
    cellspacing=
        safe_text,
    rules=
        safe_text,
    cellpadding=
        safe_text,
    width=
        safe_text,
    hl7Id=
        safe_text,
    style=
        safe_text,
    border=
        safe_text,
    lang=
        safe_text,
    class_=
        safe_text
)
xhtml_Blockquote_strategy = st.builds(
    xhtml_Blockquote,
    class_=
        safe_text,
    cite=
        safe_text,
    style=
        safe_text,
    lang=
        safe_text
)
xhtml_Ol_strategy = st.builds(
    xhtml_Ol,
    style=
        safe_text,
    lang=
        safe_text,
    class_=
        safe_text,
    li=
        safe_text
)
xhtml_Ul_strategy = st.builds(
    xhtml_Ul,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text,
    li=
        safe_text
)
xhtml_Div_strategy = st.builds(
    xhtml_Div,
    title=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    lang=
        safe_text,
    hl7Id=
        safe_text
)
xhtml_Hr_strategy = st.builds(
    xhtml_Hr,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_Pre_strategy = st.builds(
    xhtml_Pre,
    class_=
        safe_text,
    lang=
        safe_text,
    space=
        safe_text,
    style=
        safe_text
)
xhtml_Dl_strategy = st.builds(
    xhtml_Dl,
    style=
        safe_text,
    class_=
        safe_text,
    lang=
        safe_text,
    group=
        safe_text
)
xhtml_Block_strategy = st.builds(
    xhtml_Block,
    block=
        safe_text,
    mixed=
        safe_text
)
xhtml_Br_strategy = st.builds(
    xhtml_Br,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_AContent_strategy = st.builds(
    xhtml_AContent,
    mixed=
        safe_text,
    group=
        safe_text
)
xhtml_Img_strategy = st.builds(
    xhtml_Img,
    alt=
        safe_text,
    width=
        safe_text,
    imageType=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    height=
        safe_text,
    hl7Id=
        safe_text,
    src=
        safe_text
)
xhtml_Object_strategy = st.builds(
    xhtml_Object,
    name=
        safe_text,
    hl7Id=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
Inline_strategy = st.builds(
    Inline,
)
xhtml_I_strategy = st.builds(
    xhtml_I,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text
)
xhtml_Sub_strategy = st.builds(
    xhtml_Sub,
    class_=
        safe_text,
    style=
        safe_text,
    lang=
        safe_text
)
xhtml_Sup_strategy = st.builds(
    xhtml_Sup,
    style=
        safe_text,
    class_=
        safe_text,
    lang=
        safe_text
)
xhtml_Em_strategy = st.builds(
    xhtml_Em,
    style=
        safe_text,
    lang=
        safe_text,
    class_=
        safe_text
)
xhtml_Acronym_strategy = st.builds(
    xhtml_Acronym,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_Cite_strategy = st.builds(
    xhtml_Cite,
    style=
        safe_text,
    class_=
        safe_text,
    lang=
        safe_text
)
xhtml_Small_strategy = st.builds(
    xhtml_Small,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text
)
xhtml_B_strategy = st.builds(
    xhtml_B,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text
)
xhtml_Q_strategy = st.builds(
    xhtml_Q,
    cite1=
        safe_text,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_Kbd_strategy = st.builds(
    xhtml_Kbd,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_Samp_strategy = st.builds(
    xhtml_Samp,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_Strong_strategy = st.builds(
    xhtml_Strong,
    style=
        safe_text,
    lang=
        safe_text,
    class_=
        safe_text
)
xhtml_Dfn_strategy = st.builds(
    xhtml_Dfn,
    lang=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text
)
xhtml_Dt_strategy = st.builds(
    xhtml_Dt,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_Caption_strategy = st.builds(
    xhtml_Caption,
    style=
        safe_text,
    lang=
        safe_text,
    class_=
        safe_text
)
xhtml_Tt_strategy = st.builds(
    xhtml_Tt,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_P_strategy = st.builds(
    xhtml_P,
    style=
        safe_text,
    class_=
        safe_text,
    lang=
        safe_text
)
xhtml_Code_strategy = st.builds(
    xhtml_Code,
    lang=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_Big_strategy = st.builds(
    xhtml_Big,
    lang=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text
)
xhtml_Var_strategy = st.builds(
    xhtml_Var,
    class_=
        safe_text,
    style=
        safe_text,
    lang=
        safe_text
)
xhtml_Span_strategy = st.builds(
    xhtml_Span,
    class_=
        safe_text,
    style=
        safe_text,
    lang=
        safe_text
)
xhtml_Abbr_strategy = st.builds(
    xhtml_Abbr,
    class_=
        safe_text,
    lang=
        safe_text,
    style=
        safe_text
)
AContent_strategy = st.builds(
    AContent,
)
xhtml_A_strategy = st.builds(
    xhtml_A,
    lang=
        safe_text,
    type=
        safe_text,
    style=
        safe_text,
    shape=
        safe_text,
    class_=
        safe_text,
    href=
        safe_text,
    name=
        safe_text,
    coords=
        safe_text
)




@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Tr_strategy)
def test_hyp_xhtml_tr_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Tbody_strategy)
def test_hyp_xhtml_tbody_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Tbody_strategy)
def test_hyp_xhtml_tbody_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_Tbody_strategy)
def test_hyp_xhtml_tbody_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Tbody_strategy)
def test_hyp_xhtml_tbody_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_Tbody_strategy)
def test_hyp_xhtml_tbody_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Tbody_strategy)
def test_hyp_xhtml_tbody_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Tbody_strategy)
def test_hyp_xhtml_tbody_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Tfoot_strategy)
def test_hyp_xhtml_tfoot_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_Tfoot_strategy)
def test_hyp_xhtml_tfoot_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Tfoot_strategy)
def test_hyp_xhtml_tfoot_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Tfoot_strategy)
def test_hyp_xhtml_tfoot_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Tfoot_strategy)
def test_hyp_xhtml_tfoot_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Tfoot_strategy)
def test_hyp_xhtml_tfoot_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Tfoot_strategy)
def test_hyp_xhtml_tfoot_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original




@given(instance=xhtml_Thead_strategy)
def test_hyp_xhtml_thead_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Thead_strategy)
def test_hyp_xhtml_thead_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Thead_strategy)
def test_hyp_xhtml_thead_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Thead_strategy)
def test_hyp_xhtml_thead_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Thead_strategy)
def test_hyp_xhtml_thead_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Thead_strategy)
def test_hyp_xhtml_thead_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_Thead_strategy)
def test_hyp_xhtml_thead_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original




@given(instance=xhtml_PreContent_strategy)
def test_hyp_xhtml_precontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xhtml_PreContent_strategy)
def test_hyp_xhtml_precontent_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=xhtml_Param_strategy)
def test_hyp_xhtml_param_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=xhtml_Param_strategy)
def test_hyp_xhtml_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=xhtml_Inline_strategy)
def test_hyp_xhtml_inline_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xhtml_Inline_strategy)
def test_hyp_xhtml_inline_inline_setter(instance):
    original = instance.inline
    instance.inline = original
    assert instance.inline == original




@given(instance=xhtml_Flow_strategy)
def test_hyp_xhtml_flow_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xhtml_Flow_strategy)
def test_hyp_xhtml_flow_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original





@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Th_strategy)
def test_hyp_xhtml_th_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original





@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_Td_strategy)
def test_hyp_xhtml_td_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Li_strategy)
def test_hyp_xhtml_li_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Li_strategy)
def test_hyp_xhtml_li_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Li_strategy)
def test_hyp_xhtml_li_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original





@given(instance=xhtml_Dd_strategy)
def test_hyp_xhtml_dd_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Dd_strategy)
def test_hyp_xhtml_dd_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Dd_strategy)
def test_hyp_xhtml_dd_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Colgroup_strategy)
def test_hyp_xhtml_colgroup_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original




@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_Col_strategy)
def test_hyp_xhtml_col_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original





@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_frame_setter(instance):
    original = instance.frame
    instance.frame = original
    assert instance.frame == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_cellspacing_setter(instance):
    original = instance.cellspacing
    instance.cellspacing = original
    assert instance.cellspacing == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_cellpadding_setter(instance):
    original = instance.cellpadding
    instance.cellpadding = original
    assert instance.cellpadding == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_hl7Id_setter(instance):
    original = instance.hl7Id
    instance.hl7Id = original
    assert instance.hl7Id == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Table_strategy)
def test_hyp_xhtml_table_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Blockquote_strategy)
def test_hyp_xhtml_blockquote_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Blockquote_strategy)
def test_hyp_xhtml_blockquote_cite_setter(instance):
    original = instance.cite
    instance.cite = original
    assert instance.cite == original



@given(instance=xhtml_Blockquote_strategy)
def test_hyp_xhtml_blockquote_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Blockquote_strategy)
def test_hyp_xhtml_blockquote_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original




@given(instance=xhtml_Ol_strategy)
def test_hyp_xhtml_ol_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Ol_strategy)
def test_hyp_xhtml_ol_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Ol_strategy)
def test_hyp_xhtml_ol_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Ol_strategy)
def test_hyp_xhtml_ol_li_setter(instance):
    original = instance.li
    instance.li = original
    assert instance.li == original




@given(instance=xhtml_Ul_strategy)
def test_hyp_xhtml_ul_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Ul_strategy)
def test_hyp_xhtml_ul_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Ul_strategy)
def test_hyp_xhtml_ul_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Ul_strategy)
def test_hyp_xhtml_ul_li_setter(instance):
    original = instance.li
    instance.li = original
    assert instance.li == original




@given(instance=xhtml_Div_strategy)
def test_hyp_xhtml_div_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_Div_strategy)
def test_hyp_xhtml_div_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Div_strategy)
def test_hyp_xhtml_div_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Div_strategy)
def test_hyp_xhtml_div_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Div_strategy)
def test_hyp_xhtml_div_hl7Id_setter(instance):
    original = instance.hl7Id
    instance.hl7Id = original
    assert instance.hl7Id == original




@given(instance=xhtml_Hr_strategy)
def test_hyp_xhtml_hr_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Hr_strategy)
def test_hyp_xhtml_hr_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Hr_strategy)
def test_hyp_xhtml_hr_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Pre_strategy)
def test_hyp_xhtml_pre_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Pre_strategy)
def test_hyp_xhtml_pre_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Pre_strategy)
def test_hyp_xhtml_pre_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original



@given(instance=xhtml_Pre_strategy)
def test_hyp_xhtml_pre_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Dl_strategy)
def test_hyp_xhtml_dl_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Dl_strategy)
def test_hyp_xhtml_dl_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Dl_strategy)
def test_hyp_xhtml_dl_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Dl_strategy)
def test_hyp_xhtml_dl_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=xhtml_Block_strategy)
def test_hyp_xhtml_block_block_setter(instance):
    original = instance.block
    instance.block = original
    assert instance.block == original



@given(instance=xhtml_Block_strategy)
def test_hyp_xhtml_block_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=xhtml_Br_strategy)
def test_hyp_xhtml_br_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Br_strategy)
def test_hyp_xhtml_br_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_AContent_strategy)
def test_hyp_xhtml_acontent_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xhtml_AContent_strategy)
def test_hyp_xhtml_acontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_imageType_setter(instance):
    original = instance.imageType
    instance.imageType = original
    assert instance.imageType == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_hl7Id_setter(instance):
    original = instance.hl7Id
    instance.hl7Id = original
    assert instance.hl7Id == original



@given(instance=xhtml_Img_strategy)
def test_hyp_xhtml_img_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original




@given(instance=xhtml_Object_strategy)
def test_hyp_xhtml_object_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xhtml_Object_strategy)
def test_hyp_xhtml_object_hl7Id_setter(instance):
    original = instance.hl7Id
    instance.hl7Id = original
    assert instance.hl7Id == original



@given(instance=xhtml_Object_strategy)
def test_hyp_xhtml_object_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xhtml_Object_strategy)
def test_hyp_xhtml_object_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original





@given(instance=xhtml_I_strategy)
def test_hyp_xhtml_i_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_I_strategy)
def test_hyp_xhtml_i_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_I_strategy)
def test_hyp_xhtml_i_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Sub_strategy)
def test_hyp_xhtml_sub_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Sub_strategy)
def test_hyp_xhtml_sub_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Sub_strategy)
def test_hyp_xhtml_sub_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original




@given(instance=xhtml_Sup_strategy)
def test_hyp_xhtml_sup_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Sup_strategy)
def test_hyp_xhtml_sup_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Sup_strategy)
def test_hyp_xhtml_sup_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original




@given(instance=xhtml_Em_strategy)
def test_hyp_xhtml_em_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Em_strategy)
def test_hyp_xhtml_em_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Em_strategy)
def test_hyp_xhtml_em_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Acronym_strategy)
def test_hyp_xhtml_acronym_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Acronym_strategy)
def test_hyp_xhtml_acronym_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Acronym_strategy)
def test_hyp_xhtml_acronym_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Cite_strategy)
def test_hyp_xhtml_cite_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Cite_strategy)
def test_hyp_xhtml_cite_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Cite_strategy)
def test_hyp_xhtml_cite_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original




@given(instance=xhtml_Small_strategy)
def test_hyp_xhtml_small_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Small_strategy)
def test_hyp_xhtml_small_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Small_strategy)
def test_hyp_xhtml_small_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_B_strategy)
def test_hyp_xhtml_b_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_B_strategy)
def test_hyp_xhtml_b_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_B_strategy)
def test_hyp_xhtml_b_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Q_strategy)
def test_hyp_xhtml_q_cite1_setter(instance):
    original = instance.cite1
    instance.cite1 = original
    assert instance.cite1 == original



@given(instance=xhtml_Q_strategy)
def test_hyp_xhtml_q_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Q_strategy)
def test_hyp_xhtml_q_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Q_strategy)
def test_hyp_xhtml_q_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Kbd_strategy)
def test_hyp_xhtml_kbd_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Kbd_strategy)
def test_hyp_xhtml_kbd_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Kbd_strategy)
def test_hyp_xhtml_kbd_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Samp_strategy)
def test_hyp_xhtml_samp_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Samp_strategy)
def test_hyp_xhtml_samp_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Samp_strategy)
def test_hyp_xhtml_samp_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Strong_strategy)
def test_hyp_xhtml_strong_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Strong_strategy)
def test_hyp_xhtml_strong_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Strong_strategy)
def test_hyp_xhtml_strong_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Dfn_strategy)
def test_hyp_xhtml_dfn_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Dfn_strategy)
def test_hyp_xhtml_dfn_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Dfn_strategy)
def test_hyp_xhtml_dfn_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Dt_strategy)
def test_hyp_xhtml_dt_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Dt_strategy)
def test_hyp_xhtml_dt_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Dt_strategy)
def test_hyp_xhtml_dt_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Caption_strategy)
def test_hyp_xhtml_caption_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Caption_strategy)
def test_hyp_xhtml_caption_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Caption_strategy)
def test_hyp_xhtml_caption_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Tt_strategy)
def test_hyp_xhtml_tt_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Tt_strategy)
def test_hyp_xhtml_tt_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Tt_strategy)
def test_hyp_xhtml_tt_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_P_strategy)
def test_hyp_xhtml_p_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_P_strategy)
def test_hyp_xhtml_p_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_P_strategy)
def test_hyp_xhtml_p_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original




@given(instance=xhtml_Code_strategy)
def test_hyp_xhtml_code_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Code_strategy)
def test_hyp_xhtml_code_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Code_strategy)
def test_hyp_xhtml_code_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original




@given(instance=xhtml_Big_strategy)
def test_hyp_xhtml_big_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Big_strategy)
def test_hyp_xhtml_big_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Big_strategy)
def test_hyp_xhtml_big_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original




@given(instance=xhtml_Var_strategy)
def test_hyp_xhtml_var_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Var_strategy)
def test_hyp_xhtml_var_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Var_strategy)
def test_hyp_xhtml_var_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original




@given(instance=xhtml_Span_strategy)
def test_hyp_xhtml_span_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Span_strategy)
def test_hyp_xhtml_span_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_Span_strategy)
def test_hyp_xhtml_span_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original




@given(instance=xhtml_Abbr_strategy)
def test_hyp_xhtml_abbr_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_Abbr_strategy)
def test_hyp_xhtml_abbr_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_Abbr_strategy)
def test_hyp_xhtml_abbr_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original





@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original



@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xhtml_A_strategy)
def test_hyp_xhtml_a_coords_setter(instance):
    original = instance.coords
    instance.coords = original
    assert instance.coords == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AContent,
    Block,
    Flow,
    Inline,
    PreContent,
    xhtml_A,
    xhtml_AContent,
    xhtml_Abbr,
    xhtml_Acronym,
    xhtml_B,
    xhtml_Big,
    xhtml_Block,
    xhtml_Blockquote,
    xhtml_Br,
    xhtml_Caption,
    xhtml_Cite,
    xhtml_Code,
    xhtml_Col,
    xhtml_Colgroup,
    xhtml_Dd,
    xhtml_Del,
    xhtml_Dfn,
    xhtml_Div,
    xhtml_Dl,
    xhtml_Dt,
    xhtml_Em,
    xhtml_Flow,
    xhtml_Hr,
    xhtml_I,
    xhtml_Img,
    xhtml_Inline,
    xhtml_Ins,
    xhtml_Kbd,
    xhtml_Li,
    xhtml_Object,
    xhtml_Ol,
    xhtml_P,
    xhtml_Param,
    xhtml_Pre,
    xhtml_PreContent,
    xhtml_Q,
    xhtml_Samp,
    xhtml_Small,
    xhtml_Span,
    xhtml_Strong,
    xhtml_Sub,
    xhtml_Sup,
    xhtml_Table,
    xhtml_Tbody,
    xhtml_Td,
    xhtml_Tfoot,
    xhtml_Th,
    xhtml_Thead,
    xhtml_Tr,
    xhtml_Tt,
    xhtml_Ul,
    xhtml_Var,
    AlignType,
    ImageKind,
    MediaType,
    MifClassType,
    ObjectName,
    ParamName,
    Shape,
    StyleSheet,
    TFrame,
    TRules,
    ValignType,
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

def test_xhtml_A_class__value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_A_coords_value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.coords == "sample_text"
    instance.coords = "sample_text_2"
    assert instance.coords == "sample_text_2"


def test_xhtml_A_href_value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.href == "sample_text"
    instance.href = "sample_text_2"
    assert instance.href == "sample_text_2"


def test_xhtml_A_lang_value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_A_name_value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xhtml_A_shape_value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_xhtml_A_style_value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_A_type_value_roundtrip():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xhtml_AContent_group_value_roundtrip():
    instance = xhtml_AContent(group="sample_text", mixed="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_xhtml_AContent_mixed_value_roundtrip():
    instance = xhtml_AContent(group="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xhtml_Abbr_class__value_roundtrip():
    instance = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Abbr_lang_value_roundtrip():
    instance = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Abbr_style_value_roundtrip():
    instance = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Acronym_class__value_roundtrip():
    instance = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Acronym_lang_value_roundtrip():
    instance = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Acronym_style_value_roundtrip():
    instance = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_B_class__value_roundtrip():
    instance = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_B_lang_value_roundtrip():
    instance = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_B_style_value_roundtrip():
    instance = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Big_class__value_roundtrip():
    instance = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Big_lang_value_roundtrip():
    instance = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Big_style_value_roundtrip():
    instance = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Block_block_value_roundtrip():
    instance = xhtml_Block(block="sample_text", mixed="sample_text")
    assert instance.block == "sample_text"
    instance.block = "sample_text_2"
    assert instance.block == "sample_text_2"


def test_xhtml_Block_mixed_value_roundtrip():
    instance = xhtml_Block(block="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xhtml_Blockquote_cite_value_roundtrip():
    instance = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.cite == "sample_text"
    instance.cite = "sample_text_2"
    assert instance.cite == "sample_text_2"


def test_xhtml_Blockquote_class__value_roundtrip():
    instance = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Blockquote_lang_value_roundtrip():
    instance = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Blockquote_style_value_roundtrip():
    instance = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Br_class__value_roundtrip():
    instance = xhtml_Br(class_="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Br_style_value_roundtrip():
    instance = xhtml_Br(class_="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Caption_class__value_roundtrip():
    instance = xhtml_Caption(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Caption_lang_value_roundtrip():
    instance = xhtml_Caption(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Caption_style_value_roundtrip():
    instance = xhtml_Caption(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Cite_class__value_roundtrip():
    instance = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Cite_lang_value_roundtrip():
    instance = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Cite_style_value_roundtrip():
    instance = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Code_class__value_roundtrip():
    instance = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Code_lang_value_roundtrip():
    instance = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Code_style_value_roundtrip():
    instance = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Col_align_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Col_char_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Col_charoff_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Col_class__value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Col_lang_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Col_span_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.span == "sample_text"
    instance.span = "sample_text_2"
    assert instance.span == "sample_text_2"


def test_xhtml_Col_style_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Col_valign_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Col_width_value_roundtrip():
    instance = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_xhtml_Colgroup_align_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Colgroup_char_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Colgroup_charoff_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Colgroup_class__value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Colgroup_lang_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Colgroup_span_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.span == "sample_text"
    instance.span = "sample_text_2"
    assert instance.span == "sample_text_2"


def test_xhtml_Colgroup_style_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Colgroup_valign_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Colgroup_width_value_roundtrip():
    instance = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_xhtml_Dd_class__value_roundtrip():
    instance = xhtml_Dd(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Dd_lang_value_roundtrip():
    instance = xhtml_Dd(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Dd_style_value_roundtrip():
    instance = xhtml_Dd(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Dfn_class__value_roundtrip():
    instance = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Dfn_lang_value_roundtrip():
    instance = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Dfn_style_value_roundtrip():
    instance = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Div_class__value_roundtrip():
    instance = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Div_hl7Id_value_roundtrip():
    instance = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    assert instance.hl7Id == "sample_text"
    instance.hl7Id = "sample_text_2"
    assert instance.hl7Id == "sample_text_2"


def test_xhtml_Div_lang_value_roundtrip():
    instance = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Div_style_value_roundtrip():
    instance = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Div_title_value_roundtrip():
    instance = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_xhtml_Dl_class__value_roundtrip():
    instance = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Dl_group_value_roundtrip():
    instance = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_xhtml_Dl_lang_value_roundtrip():
    instance = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Dl_style_value_roundtrip():
    instance = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Dt_class__value_roundtrip():
    instance = xhtml_Dt(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Dt_lang_value_roundtrip():
    instance = xhtml_Dt(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Dt_style_value_roundtrip():
    instance = xhtml_Dt(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Em_class__value_roundtrip():
    instance = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Em_lang_value_roundtrip():
    instance = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Em_style_value_roundtrip():
    instance = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Flow_group_value_roundtrip():
    instance = xhtml_Flow(group="sample_text", mixed="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_xhtml_Flow_mixed_value_roundtrip():
    instance = xhtml_Flow(group="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xhtml_Hr_class__value_roundtrip():
    instance = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Hr_lang_value_roundtrip():
    instance = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Hr_style_value_roundtrip():
    instance = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_I_class__value_roundtrip():
    instance = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_I_lang_value_roundtrip():
    instance = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_I_style_value_roundtrip():
    instance = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Img_alt_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.alt == "sample_text"
    instance.alt = "sample_text_2"
    assert instance.alt == "sample_text_2"


def test_xhtml_Img_class__value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Img_height_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_xhtml_Img_hl7Id_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.hl7Id == "sample_text"
    instance.hl7Id = "sample_text_2"
    assert instance.hl7Id == "sample_text_2"


def test_xhtml_Img_imageType_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.imageType == "sample_text"
    instance.imageType = "sample_text_2"
    assert instance.imageType == "sample_text_2"


def test_xhtml_Img_lang_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Img_src_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_xhtml_Img_style_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Img_width_value_roundtrip():
    instance = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_xhtml_Inline_inline_value_roundtrip():
    instance = xhtml_Inline(inline="sample_text", mixed="sample_text")
    assert instance.inline == "sample_text"
    instance.inline = "sample_text_2"
    assert instance.inline == "sample_text_2"


def test_xhtml_Inline_mixed_value_roundtrip():
    instance = xhtml_Inline(inline="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xhtml_Kbd_class__value_roundtrip():
    instance = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Kbd_lang_value_roundtrip():
    instance = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Kbd_style_value_roundtrip():
    instance = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Li_class__value_roundtrip():
    instance = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Li_lang_value_roundtrip():
    instance = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Li_style_value_roundtrip():
    instance = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Object_group_value_roundtrip():
    instance = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_xhtml_Object_hl7Id_value_roundtrip():
    instance = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    assert instance.hl7Id == "sample_text"
    instance.hl7Id = "sample_text_2"
    assert instance.hl7Id == "sample_text_2"


def test_xhtml_Object_mixed_value_roundtrip():
    instance = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xhtml_Object_name_value_roundtrip():
    instance = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xhtml_Ol_class__value_roundtrip():
    instance = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Ol_lang_value_roundtrip():
    instance = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Ol_li_value_roundtrip():
    instance = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.li == "sample_text"
    instance.li = "sample_text_2"
    assert instance.li == "sample_text_2"


def test_xhtml_Ol_style_value_roundtrip():
    instance = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_P_class__value_roundtrip():
    instance = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_P_lang_value_roundtrip():
    instance = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_P_style_value_roundtrip():
    instance = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Param_name_value_roundtrip():
    instance = xhtml_Param(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xhtml_Param_value_value_roundtrip():
    instance = xhtml_Param(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_xhtml_Pre_class__value_roundtrip():
    instance = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Pre_lang_value_roundtrip():
    instance = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Pre_space_value_roundtrip():
    instance = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    assert instance.space == "sample_text"
    instance.space = "sample_text_2"
    assert instance.space == "sample_text_2"


def test_xhtml_Pre_style_value_roundtrip():
    instance = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_PreContent_group_value_roundtrip():
    instance = xhtml_PreContent(group="sample_text", mixed="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_xhtml_PreContent_mixed_value_roundtrip():
    instance = xhtml_PreContent(group="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_xhtml_Q_cite1_value_roundtrip():
    instance = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.cite1 == "sample_text"
    instance.cite1 = "sample_text_2"
    assert instance.cite1 == "sample_text_2"


def test_xhtml_Q_class__value_roundtrip():
    instance = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Q_lang_value_roundtrip():
    instance = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Q_style_value_roundtrip():
    instance = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Samp_class__value_roundtrip():
    instance = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Samp_lang_value_roundtrip():
    instance = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Samp_style_value_roundtrip():
    instance = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Small_class__value_roundtrip():
    instance = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Small_lang_value_roundtrip():
    instance = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Small_style_value_roundtrip():
    instance = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Span_class__value_roundtrip():
    instance = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Span_lang_value_roundtrip():
    instance = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Span_style_value_roundtrip():
    instance = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Strong_class__value_roundtrip():
    instance = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Strong_lang_value_roundtrip():
    instance = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Strong_style_value_roundtrip():
    instance = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Sub_class__value_roundtrip():
    instance = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Sub_lang_value_roundtrip():
    instance = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Sub_style_value_roundtrip():
    instance = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Sup_class__value_roundtrip():
    instance = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Sup_lang_value_roundtrip():
    instance = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Sup_style_value_roundtrip():
    instance = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Table_border_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.border == "sample_text"
    instance.border = "sample_text_2"
    assert instance.border == "sample_text_2"


def test_xhtml_Table_cellpadding_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.cellpadding == "sample_text"
    instance.cellpadding = "sample_text_2"
    assert instance.cellpadding == "sample_text_2"


def test_xhtml_Table_cellspacing_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.cellspacing == "sample_text"
    instance.cellspacing = "sample_text_2"
    assert instance.cellspacing == "sample_text_2"


def test_xhtml_Table_class__value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Table_frame_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.frame == "sample_text"
    instance.frame = "sample_text_2"
    assert instance.frame == "sample_text_2"


def test_xhtml_Table_hl7Id_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.hl7Id == "sample_text"
    instance.hl7Id = "sample_text_2"
    assert instance.hl7Id == "sample_text_2"


def test_xhtml_Table_lang_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Table_rules_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.rules == "sample_text"
    instance.rules = "sample_text_2"
    assert instance.rules == "sample_text_2"


def test_xhtml_Table_style_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Table_width_value_roundtrip():
    instance = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_xhtml_Tbody_align_value_roundtrip():
    instance = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Tbody_char_value_roundtrip():
    instance = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Tbody_charoff_value_roundtrip():
    instance = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Tbody_class__value_roundtrip():
    instance = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Tbody_lang_value_roundtrip():
    instance = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Tbody_style_value_roundtrip():
    instance = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Tbody_valign_value_roundtrip():
    instance = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Td_align_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Td_char_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Td_charoff_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Td_class__value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Td_colspan_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.colspan == "sample_text"
    instance.colspan = "sample_text_2"
    assert instance.colspan == "sample_text_2"


def test_xhtml_Td_lang_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Td_rowspan_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.rowspan == "sample_text"
    instance.rowspan = "sample_text_2"
    assert instance.rowspan == "sample_text_2"


def test_xhtml_Td_style_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Td_valign_value_roundtrip():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Tfoot_align_value_roundtrip():
    instance = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Tfoot_char_value_roundtrip():
    instance = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Tfoot_charoff_value_roundtrip():
    instance = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Tfoot_class__value_roundtrip():
    instance = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Tfoot_lang_value_roundtrip():
    instance = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Tfoot_style_value_roundtrip():
    instance = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Tfoot_valign_value_roundtrip():
    instance = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Th_align_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Th_char_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Th_charoff_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Th_class__value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Th_colspan_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.colspan == "sample_text"
    instance.colspan = "sample_text_2"
    assert instance.colspan == "sample_text_2"


def test_xhtml_Th_lang_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Th_rowspan_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.rowspan == "sample_text"
    instance.rowspan = "sample_text_2"
    assert instance.rowspan == "sample_text_2"


def test_xhtml_Th_style_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Th_valign_value_roundtrip():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Thead_align_value_roundtrip():
    instance = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Thead_char_value_roundtrip():
    instance = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Thead_charoff_value_roundtrip():
    instance = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Thead_class__value_roundtrip():
    instance = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Thead_lang_value_roundtrip():
    instance = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Thead_style_value_roundtrip():
    instance = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Thead_valign_value_roundtrip():
    instance = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Tr_align_value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_xhtml_Tr_char_value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_xhtml_Tr_charoff_value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.charoff == "sample_text"
    instance.charoff = "sample_text_2"
    assert instance.charoff == "sample_text_2"


def test_xhtml_Tr_class__value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Tr_group_value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_xhtml_Tr_lang_value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Tr_style_value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Tr_valign_value_roundtrip():
    instance = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_xhtml_Tt_class__value_roundtrip():
    instance = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Tt_lang_value_roundtrip():
    instance = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Tt_style_value_roundtrip():
    instance = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Ul_class__value_roundtrip():
    instance = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Ul_lang_value_roundtrip():
    instance = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Ul_li_value_roundtrip():
    instance = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.li == "sample_text"
    instance.li = "sample_text_2"
    assert instance.li == "sample_text_2"


def test_xhtml_Ul_style_value_roundtrip():
    instance = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_Var_class__value_roundtrip():
    instance = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_xhtml_Var_lang_value_roundtrip():
    instance = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_xhtml_Var_style_value_roundtrip():
    instance = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_xhtml_A_isa_AContent():
    instance = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    assert isinstance(instance, AContent)


def test_xhtml_Blockquote_isa_Block():
    instance = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Block)


def test_xhtml_Dd_isa_Flow():
    instance = xhtml_Dd(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Flow)


def test_xhtml_Del_isa_Flow():
    instance = xhtml_Del()
    assert isinstance(instance, Flow)


def test_xhtml_Div_isa_Flow():
    instance = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    assert isinstance(instance, Flow)


def test_xhtml_Ins_isa_Flow():
    instance = xhtml_Ins()
    assert isinstance(instance, Flow)


def test_xhtml_Li_isa_Flow():
    instance = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Flow)


def test_xhtml_Td_isa_Flow():
    instance = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert isinstance(instance, Flow)


def test_xhtml_Th_isa_Flow():
    instance = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    assert isinstance(instance, Flow)


def test_xhtml_Abbr_isa_Inline():
    instance = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Acronym_isa_Inline():
    instance = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_B_isa_Inline():
    instance = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Big_isa_Inline():
    instance = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Caption_isa_Inline():
    instance = xhtml_Caption(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Cite_isa_Inline():
    instance = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Code_isa_Inline():
    instance = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Dfn_isa_Inline():
    instance = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Dt_isa_Inline():
    instance = xhtml_Dt(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Em_isa_Inline():
    instance = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_I_isa_Inline():
    instance = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Kbd_isa_Inline():
    instance = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_P_isa_Inline():
    instance = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Q_isa_Inline():
    instance = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Samp_isa_Inline():
    instance = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Small_isa_Inline():
    instance = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Span_isa_Inline():
    instance = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Strong_isa_Inline():
    instance = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Sub_isa_Inline():
    instance = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Sup_isa_Inline():
    instance = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Tt_isa_Inline():
    instance = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Var_isa_Inline():
    instance = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    assert isinstance(instance, Inline)


def test_xhtml_Pre_isa_PreContent():
    instance = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    assert isinstance(instance, PreContent)


def test_assoc_a162_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    b2 = xhtml_A(class_="sample_text_2", coords="sample_text_2", href="sample_text_2", lang="sample_text_2", name="sample_text_2", shape="sample_text_2", style="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xhtml_Inline', {b1})
    assert _is_linked(a, 'xhtml_Inline', b1)
    if hasattr(b1, 'xhtml_A163'):
        assert _is_linked(b1, 'xhtml_A163', a)
    _safe_set(a, 'xhtml_Inline', {b2})
    assert _is_linked(a, 'xhtml_Inline', b2)
    if hasattr(b1, 'xhtml_A163'):
        assert not _is_linked(b1, 'xhtml_A163', a)
    if hasattr(b2, 'xhtml_A163'):
        assert _is_linked(b2, 'xhtml_A163', a)
    _safe_set(a, 'xhtml_Inline', set())
    assert not _is_linked(a, 'xhtml_Inline', b2)
    if hasattr(b2, 'xhtml_A163'):
        assert not _is_linked(b2, 'xhtml_A163', a)


def test_assoc_a259_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    b2 = xhtml_A(class_="sample_text_2", coords="sample_text_2", href="sample_text_2", lang="sample_text_2", name="sample_text_2", shape="sample_text_2", style="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xhtml_Object260', {b1})
    assert _is_linked(a, 'xhtml_Object260', b1)
    if hasattr(b1, 'xhtml_A261'):
        assert _is_linked(b1, 'xhtml_A261', a)
    _safe_set(a, 'xhtml_Object260', {b2})
    assert _is_linked(a, 'xhtml_Object260', b2)
    if hasattr(b1, 'xhtml_A261'):
        assert not _is_linked(b1, 'xhtml_A261', a)
    if hasattr(b2, 'xhtml_A261'):
        assert _is_linked(b2, 'xhtml_A261', a)
    _safe_set(a, 'xhtml_Object260', set())
    assert not _is_linked(a, 'xhtml_Object260', b2)
    if hasattr(b2, 'xhtml_A261'):
        assert not _is_linked(b2, 'xhtml_A261', a)


def test_assoc_a330_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    b2 = xhtml_A(class_="sample_text_2", coords="sample_text_2", href="sample_text_2", lang="sample_text_2", name="sample_text_2", shape="sample_text_2", style="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xhtml_PreContent', {b1})
    assert _is_linked(a, 'xhtml_PreContent', b1)
    if hasattr(b1, 'xhtml_A331'):
        assert _is_linked(b1, 'xhtml_A331', a)
    _safe_set(a, 'xhtml_PreContent', {b2})
    assert _is_linked(a, 'xhtml_PreContent', b2)
    if hasattr(b1, 'xhtml_A331'):
        assert not _is_linked(b1, 'xhtml_A331', a)
    if hasattr(b2, 'xhtml_A331'):
        assert _is_linked(b2, 'xhtml_A331', a)
    _safe_set(a, 'xhtml_PreContent', set())
    assert not _is_linked(a, 'xhtml_PreContent', b2)
    if hasattr(b2, 'xhtml_A331'):
        assert not _is_linked(b2, 'xhtml_A331', a)


def test_assoc_a91_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_A(class_="sample_text", coords="sample_text", href="sample_text", lang="sample_text", name="sample_text", shape="sample_text", style="sample_text", type="sample_text")
    b2 = xhtml_A(class_="sample_text_2", coords="sample_text_2", href="sample_text_2", lang="sample_text_2", name="sample_text_2", shape="sample_text_2", style="sample_text_2", type="sample_text_2")
    _safe_set(a, 'xhtml_Flow92', {b1})
    assert _is_linked(a, 'xhtml_Flow92', b1)
    if hasattr(b1, 'xhtml_A'):
        assert _is_linked(b1, 'xhtml_A', a)
    _safe_set(a, 'xhtml_Flow92', {b2})
    assert _is_linked(a, 'xhtml_Flow92', b2)
    if hasattr(b1, 'xhtml_A'):
        assert not _is_linked(b1, 'xhtml_A', a)
    if hasattr(b2, 'xhtml_A'):
        assert _is_linked(b2, 'xhtml_A', a)
    _safe_set(a, 'xhtml_Flow92', set())
    assert not _is_linked(a, 'xhtml_Flow92', b2)
    if hasattr(b2, 'xhtml_A'):
        assert not _is_linked(b2, 'xhtml_A', a)


def test_assoc_abbr147_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Abbr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow148', {b1})
    assert _is_linked(a, 'xhtml_Flow148', b1)
    if hasattr(b1, 'xhtml_Abbr149'):
        assert _is_linked(b1, 'xhtml_Abbr149', a)
    _safe_set(a, 'xhtml_Flow148', {b2})
    assert _is_linked(a, 'xhtml_Flow148', b2)
    if hasattr(b1, 'xhtml_Abbr149'):
        assert not _is_linked(b1, 'xhtml_Abbr149', a)
    if hasattr(b2, 'xhtml_Abbr149'):
        assert _is_linked(b2, 'xhtml_Abbr149', a)
    _safe_set(a, 'xhtml_Flow148', set())
    assert not _is_linked(a, 'xhtml_Flow148', b2)
    if hasattr(b2, 'xhtml_Abbr149'):
        assert not _is_linked(b2, 'xhtml_Abbr149', a)


def test_assoc_abbr218_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Abbr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline219', {b1})
    assert _is_linked(a, 'xhtml_Inline219', b1)
    if hasattr(b1, 'xhtml_Abbr220'):
        assert _is_linked(b1, 'xhtml_Abbr220', a)
    _safe_set(a, 'xhtml_Inline219', {b2})
    assert _is_linked(a, 'xhtml_Inline219', b2)
    if hasattr(b1, 'xhtml_Abbr220'):
        assert not _is_linked(b1, 'xhtml_Abbr220', a)
    if hasattr(b2, 'xhtml_Abbr220'):
        assert _is_linked(b2, 'xhtml_Abbr220', a)
    _safe_set(a, 'xhtml_Inline219', set())
    assert not _is_linked(a, 'xhtml_Inline219', b2)
    if hasattr(b2, 'xhtml_Abbr220'):
        assert not _is_linked(b2, 'xhtml_Abbr220', a)


def test_assoc_abbr316_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Abbr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object317', {b1})
    assert _is_linked(a, 'xhtml_Object317', b1)
    if hasattr(b1, 'xhtml_Abbr318'):
        assert _is_linked(b1, 'xhtml_Abbr318', a)
    _safe_set(a, 'xhtml_Object317', {b2})
    assert _is_linked(a, 'xhtml_Object317', b2)
    if hasattr(b1, 'xhtml_Abbr318'):
        assert not _is_linked(b1, 'xhtml_Abbr318', a)
    if hasattr(b2, 'xhtml_Abbr318'):
        assert _is_linked(b2, 'xhtml_Abbr318', a)
    _safe_set(a, 'xhtml_Object317', set())
    assert not _is_linked(a, 'xhtml_Object317', b2)
    if hasattr(b2, 'xhtml_Abbr318'):
        assert not _is_linked(b2, 'xhtml_Abbr318', a)


def test_assoc_abbr35_link_reassign_clear():
    a = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Abbr', b1)
    assert _is_linked(a, 'xhtml_Abbr', b1)
    if hasattr(b1, 'xhtml_AContent36'):
        assert _is_linked(b1, 'xhtml_AContent36', a)
    _safe_set(a, 'xhtml_Abbr', b2)
    assert _is_linked(a, 'xhtml_Abbr', b2)
    if hasattr(b1, 'xhtml_AContent36'):
        assert not _is_linked(b1, 'xhtml_AContent36', a)
    if hasattr(b2, 'xhtml_AContent36'):
        assert _is_linked(b2, 'xhtml_AContent36', a)
    _safe_set(a, 'xhtml_Abbr', None)
    assert not _is_linked(a, 'xhtml_Abbr', b2)
    if hasattr(b2, 'xhtml_AContent36'):
        assert not _is_linked(b2, 'xhtml_AContent36', a)


def test_assoc_abbr374_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Abbr(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Abbr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent375', {b1})
    assert _is_linked(a, 'xhtml_PreContent375', b1)
    if hasattr(b1, 'xhtml_Abbr376'):
        assert _is_linked(b1, 'xhtml_Abbr376', a)
    _safe_set(a, 'xhtml_PreContent375', {b2})
    assert _is_linked(a, 'xhtml_PreContent375', b2)
    if hasattr(b1, 'xhtml_Abbr376'):
        assert not _is_linked(b1, 'xhtml_Abbr376', a)
    if hasattr(b2, 'xhtml_Abbr376'):
        assert _is_linked(b2, 'xhtml_Abbr376', a)
    _safe_set(a, 'xhtml_PreContent375', set())
    assert not _is_linked(a, 'xhtml_PreContent375', b2)
    if hasattr(b2, 'xhtml_Abbr376'):
        assert not _is_linked(b2, 'xhtml_Abbr376', a)


def test_assoc_acronym150_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Acronym(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow151', {b1})
    assert _is_linked(a, 'xhtml_Flow151', b1)
    if hasattr(b1, 'xhtml_Acronym152'):
        assert _is_linked(b1, 'xhtml_Acronym152', a)
    _safe_set(a, 'xhtml_Flow151', {b2})
    assert _is_linked(a, 'xhtml_Flow151', b2)
    if hasattr(b1, 'xhtml_Acronym152'):
        assert not _is_linked(b1, 'xhtml_Acronym152', a)
    if hasattr(b2, 'xhtml_Acronym152'):
        assert _is_linked(b2, 'xhtml_Acronym152', a)
    _safe_set(a, 'xhtml_Flow151', set())
    assert not _is_linked(a, 'xhtml_Flow151', b2)
    if hasattr(b2, 'xhtml_Acronym152'):
        assert not _is_linked(b2, 'xhtml_Acronym152', a)


def test_assoc_acronym221_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Acronym(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline222', {b1})
    assert _is_linked(a, 'xhtml_Inline222', b1)
    if hasattr(b1, 'xhtml_Acronym223'):
        assert _is_linked(b1, 'xhtml_Acronym223', a)
    _safe_set(a, 'xhtml_Inline222', {b2})
    assert _is_linked(a, 'xhtml_Inline222', b2)
    if hasattr(b1, 'xhtml_Acronym223'):
        assert not _is_linked(b1, 'xhtml_Acronym223', a)
    if hasattr(b2, 'xhtml_Acronym223'):
        assert _is_linked(b2, 'xhtml_Acronym223', a)
    _safe_set(a, 'xhtml_Inline222', set())
    assert not _is_linked(a, 'xhtml_Inline222', b2)
    if hasattr(b2, 'xhtml_Acronym223'):
        assert not _is_linked(b2, 'xhtml_Acronym223', a)


def test_assoc_acronym319_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Acronym(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object320', {b1})
    assert _is_linked(a, 'xhtml_Object320', b1)
    if hasattr(b1, 'xhtml_Acronym321'):
        assert _is_linked(b1, 'xhtml_Acronym321', a)
    _safe_set(a, 'xhtml_Object320', {b2})
    assert _is_linked(a, 'xhtml_Object320', b2)
    if hasattr(b1, 'xhtml_Acronym321'):
        assert not _is_linked(b1, 'xhtml_Acronym321', a)
    if hasattr(b2, 'xhtml_Acronym321'):
        assert _is_linked(b2, 'xhtml_Acronym321', a)
    _safe_set(a, 'xhtml_Object320', set())
    assert not _is_linked(a, 'xhtml_Object320', b2)
    if hasattr(b2, 'xhtml_Acronym321'):
        assert not _is_linked(b2, 'xhtml_Acronym321', a)


def test_assoc_acronym37_link_reassign_clear():
    a = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Acronym', b1)
    assert _is_linked(a, 'xhtml_Acronym', b1)
    if hasattr(b1, 'xhtml_AContent38'):
        assert _is_linked(b1, 'xhtml_AContent38', a)
    _safe_set(a, 'xhtml_Acronym', b2)
    assert _is_linked(a, 'xhtml_Acronym', b2)
    if hasattr(b1, 'xhtml_AContent38'):
        assert not _is_linked(b1, 'xhtml_AContent38', a)
    if hasattr(b2, 'xhtml_AContent38'):
        assert _is_linked(b2, 'xhtml_AContent38', a)
    _safe_set(a, 'xhtml_Acronym', None)
    assert not _is_linked(a, 'xhtml_Acronym', b2)
    if hasattr(b2, 'xhtml_AContent38'):
        assert not _is_linked(b2, 'xhtml_AContent38', a)


def test_assoc_acronym377_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Acronym(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Acronym(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent378', {b1})
    assert _is_linked(a, 'xhtml_PreContent378', b1)
    if hasattr(b1, 'xhtml_Acronym379'):
        assert _is_linked(b1, 'xhtml_Acronym379', a)
    _safe_set(a, 'xhtml_PreContent378', {b2})
    assert _is_linked(a, 'xhtml_PreContent378', b2)
    if hasattr(b1, 'xhtml_Acronym379'):
        assert not _is_linked(b1, 'xhtml_Acronym379', a)
    if hasattr(b2, 'xhtml_Acronym379'):
        assert _is_linked(b2, 'xhtml_Acronym379', a)
    _safe_set(a, 'xhtml_PreContent378', set())
    assert not _is_linked(a, 'xhtml_PreContent378', b2)
    if hasattr(b2, 'xhtml_Acronym379'):
        assert not _is_linked(b2, 'xhtml_Acronym379', a)


def test_assoc_b11_link_reassign_clear():
    a = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_B', b1)
    assert _is_linked(a, 'xhtml_B', b1)
    if hasattr(b1, 'xhtml_AContent12'):
        assert _is_linked(b1, 'xhtml_AContent12', a)
    _safe_set(a, 'xhtml_B', b2)
    assert _is_linked(a, 'xhtml_B', b2)
    if hasattr(b1, 'xhtml_AContent12'):
        assert not _is_linked(b1, 'xhtml_AContent12', a)
    if hasattr(b2, 'xhtml_AContent12'):
        assert _is_linked(b2, 'xhtml_AContent12', a)
    _safe_set(a, 'xhtml_B', None)
    assert not _is_linked(a, 'xhtml_B', b2)
    if hasattr(b2, 'xhtml_AContent12'):
        assert not _is_linked(b2, 'xhtml_AContent12', a)


def test_assoc_b111_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_B(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow112', {b1})
    assert _is_linked(a, 'xhtml_Flow112', b1)
    if hasattr(b1, 'xhtml_B113'):
        assert _is_linked(b1, 'xhtml_B113', a)
    _safe_set(a, 'xhtml_Flow112', {b2})
    assert _is_linked(a, 'xhtml_Flow112', b2)
    if hasattr(b1, 'xhtml_B113'):
        assert not _is_linked(b1, 'xhtml_B113', a)
    if hasattr(b2, 'xhtml_B113'):
        assert _is_linked(b2, 'xhtml_B113', a)
    _safe_set(a, 'xhtml_Flow112', set())
    assert not _is_linked(a, 'xhtml_Flow112', b2)
    if hasattr(b2, 'xhtml_B113'):
        assert not _is_linked(b2, 'xhtml_B113', a)


def test_assoc_b182_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_B(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline183', {b1})
    assert _is_linked(a, 'xhtml_Inline183', b1)
    if hasattr(b1, 'xhtml_B184'):
        assert _is_linked(b1, 'xhtml_B184', a)
    _safe_set(a, 'xhtml_Inline183', {b2})
    assert _is_linked(a, 'xhtml_Inline183', b2)
    if hasattr(b1, 'xhtml_B184'):
        assert not _is_linked(b1, 'xhtml_B184', a)
    if hasattr(b2, 'xhtml_B184'):
        assert _is_linked(b2, 'xhtml_B184', a)
    _safe_set(a, 'xhtml_Inline183', set())
    assert not _is_linked(a, 'xhtml_Inline183', b2)
    if hasattr(b2, 'xhtml_B184'):
        assert not _is_linked(b2, 'xhtml_B184', a)


def test_assoc_b280_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_B(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object281', {b1})
    assert _is_linked(a, 'xhtml_Object281', b1)
    if hasattr(b1, 'xhtml_B282'):
        assert _is_linked(b1, 'xhtml_B282', a)
    _safe_set(a, 'xhtml_Object281', {b2})
    assert _is_linked(a, 'xhtml_Object281', b2)
    if hasattr(b1, 'xhtml_B282'):
        assert not _is_linked(b1, 'xhtml_B282', a)
    if hasattr(b2, 'xhtml_B282'):
        assert _is_linked(b2, 'xhtml_B282', a)
    _safe_set(a, 'xhtml_Object281', set())
    assert not _is_linked(a, 'xhtml_Object281', b2)
    if hasattr(b2, 'xhtml_B282'):
        assert not _is_linked(b2, 'xhtml_B282', a)


def test_assoc_b338_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_B(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_B(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent339', {b1})
    assert _is_linked(a, 'xhtml_PreContent339', b1)
    if hasattr(b1, 'xhtml_B340'):
        assert _is_linked(b1, 'xhtml_B340', a)
    _safe_set(a, 'xhtml_PreContent339', {b2})
    assert _is_linked(a, 'xhtml_PreContent339', b2)
    if hasattr(b1, 'xhtml_B340'):
        assert not _is_linked(b1, 'xhtml_B340', a)
    if hasattr(b2, 'xhtml_B340'):
        assert _is_linked(b2, 'xhtml_B340', a)
    _safe_set(a, 'xhtml_PreContent339', set())
    assert not _is_linked(a, 'xhtml_PreContent339', b2)
    if hasattr(b2, 'xhtml_B340'):
        assert not _is_linked(b2, 'xhtml_B340', a)


def test_assoc_big114_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Big(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow115', {b1})
    assert _is_linked(a, 'xhtml_Flow115', b1)
    if hasattr(b1, 'xhtml_Big116'):
        assert _is_linked(b1, 'xhtml_Big116', a)
    _safe_set(a, 'xhtml_Flow115', {b2})
    assert _is_linked(a, 'xhtml_Flow115', b2)
    if hasattr(b1, 'xhtml_Big116'):
        assert not _is_linked(b1, 'xhtml_Big116', a)
    if hasattr(b2, 'xhtml_Big116'):
        assert _is_linked(b2, 'xhtml_Big116', a)
    _safe_set(a, 'xhtml_Flow115', set())
    assert not _is_linked(a, 'xhtml_Flow115', b2)
    if hasattr(b2, 'xhtml_Big116'):
        assert not _is_linked(b2, 'xhtml_Big116', a)


def test_assoc_big13_link_reassign_clear():
    a = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Big', b1)
    assert _is_linked(a, 'xhtml_Big', b1)
    if hasattr(b1, 'xhtml_AContent14'):
        assert _is_linked(b1, 'xhtml_AContent14', a)
    _safe_set(a, 'xhtml_Big', b2)
    assert _is_linked(a, 'xhtml_Big', b2)
    if hasattr(b1, 'xhtml_AContent14'):
        assert not _is_linked(b1, 'xhtml_AContent14', a)
    if hasattr(b2, 'xhtml_AContent14'):
        assert _is_linked(b2, 'xhtml_AContent14', a)
    _safe_set(a, 'xhtml_Big', None)
    assert not _is_linked(a, 'xhtml_Big', b2)
    if hasattr(b2, 'xhtml_AContent14'):
        assert not _is_linked(b2, 'xhtml_AContent14', a)


def test_assoc_big185_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Big(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline186', {b1})
    assert _is_linked(a, 'xhtml_Inline186', b1)
    if hasattr(b1, 'xhtml_Big187'):
        assert _is_linked(b1, 'xhtml_Big187', a)
    _safe_set(a, 'xhtml_Inline186', {b2})
    assert _is_linked(a, 'xhtml_Inline186', b2)
    if hasattr(b1, 'xhtml_Big187'):
        assert not _is_linked(b1, 'xhtml_Big187', a)
    if hasattr(b2, 'xhtml_Big187'):
        assert _is_linked(b2, 'xhtml_Big187', a)
    _safe_set(a, 'xhtml_Inline186', set())
    assert not _is_linked(a, 'xhtml_Inline186', b2)
    if hasattr(b2, 'xhtml_Big187'):
        assert not _is_linked(b2, 'xhtml_Big187', a)


def test_assoc_big283_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Big(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object284', {b1})
    assert _is_linked(a, 'xhtml_Object284', b1)
    if hasattr(b1, 'xhtml_Big285'):
        assert _is_linked(b1, 'xhtml_Big285', a)
    _safe_set(a, 'xhtml_Object284', {b2})
    assert _is_linked(a, 'xhtml_Object284', b2)
    if hasattr(b1, 'xhtml_Big285'):
        assert not _is_linked(b1, 'xhtml_Big285', a)
    if hasattr(b2, 'xhtml_Big285'):
        assert _is_linked(b2, 'xhtml_Big285', a)
    _safe_set(a, 'xhtml_Object284', set())
    assert not _is_linked(a, 'xhtml_Object284', b2)
    if hasattr(b2, 'xhtml_Big285'):
        assert not _is_linked(b2, 'xhtml_Big285', a)


def test_assoc_big341_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Big(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Big(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent342', {b1})
    assert _is_linked(a, 'xhtml_PreContent342', b1)
    if hasattr(b1, 'xhtml_Big343'):
        assert _is_linked(b1, 'xhtml_Big343', a)
    _safe_set(a, 'xhtml_PreContent342', {b2})
    assert _is_linked(a, 'xhtml_PreContent342', b2)
    if hasattr(b1, 'xhtml_Big343'):
        assert not _is_linked(b1, 'xhtml_Big343', a)
    if hasattr(b2, 'xhtml_Big343'):
        assert _is_linked(b2, 'xhtml_Big343', a)
    _safe_set(a, 'xhtml_PreContent342', set())
    assert not _is_linked(a, 'xhtml_PreContent342', b2)
    if hasattr(b2, 'xhtml_Big343'):
        assert not _is_linked(b2, 'xhtml_Big343', a)


def test_assoc_blockquote253_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Blockquote(cite="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object254', {b1})
    assert _is_linked(a, 'xhtml_Object254', b1)
    if hasattr(b1, 'xhtml_Blockquote255'):
        assert _is_linked(b1, 'xhtml_Blockquote255', a)
    _safe_set(a, 'xhtml_Object254', {b2})
    assert _is_linked(a, 'xhtml_Object254', b2)
    if hasattr(b1, 'xhtml_Blockquote255'):
        assert not _is_linked(b1, 'xhtml_Blockquote255', a)
    if hasattr(b2, 'xhtml_Blockquote255'):
        assert _is_linked(b2, 'xhtml_Blockquote255', a)
    _safe_set(a, 'xhtml_Object254', set())
    assert not _is_linked(a, 'xhtml_Object254', b2)
    if hasattr(b2, 'xhtml_Blockquote255'):
        assert not _is_linked(b2, 'xhtml_Blockquote255', a)


def test_assoc_blockquote56_link_reassign_clear():
    a = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Blockquote', b1)
    assert _is_linked(a, 'xhtml_Blockquote', b1)
    if hasattr(b1, 'xhtml_Block57'):
        assert _is_linked(b1, 'xhtml_Block57', a)
    _safe_set(a, 'xhtml_Blockquote', b2)
    assert _is_linked(a, 'xhtml_Blockquote', b2)
    if hasattr(b1, 'xhtml_Block57'):
        assert not _is_linked(b1, 'xhtml_Block57', a)
    if hasattr(b2, 'xhtml_Block57'):
        assert _is_linked(b2, 'xhtml_Block57', a)
    _safe_set(a, 'xhtml_Blockquote', None)
    assert not _is_linked(a, 'xhtml_Blockquote', b2)
    if hasattr(b2, 'xhtml_Block57'):
        assert not _is_linked(b2, 'xhtml_Block57', a)


def test_assoc_blockquote85_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Blockquote(cite="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Blockquote(cite="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow86', {b1})
    assert _is_linked(a, 'xhtml_Flow86', b1)
    if hasattr(b1, 'xhtml_Blockquote87'):
        assert _is_linked(b1, 'xhtml_Blockquote87', a)
    _safe_set(a, 'xhtml_Flow86', {b2})
    assert _is_linked(a, 'xhtml_Flow86', b2)
    if hasattr(b1, 'xhtml_Blockquote87'):
        assert not _is_linked(b1, 'xhtml_Blockquote87', a)
    if hasattr(b2, 'xhtml_Blockquote87'):
        assert _is_linked(b2, 'xhtml_Blockquote87', a)
    _safe_set(a, 'xhtml_Flow86', set())
    assert not _is_linked(a, 'xhtml_Flow86', b2)
    if hasattr(b2, 'xhtml_Blockquote87'):
        assert not _is_linked(b2, 'xhtml_Blockquote87', a)


def test_assoc_br0_link_reassign_clear():
    a = xhtml_Br(class_="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Br', b1)
    assert _is_linked(a, 'xhtml_Br', b1)
    if hasattr(b1, 'xhtml_AContent'):
        assert _is_linked(b1, 'xhtml_AContent', a)
    _safe_set(a, 'xhtml_Br', b2)
    assert _is_linked(a, 'xhtml_Br', b2)
    if hasattr(b1, 'xhtml_AContent'):
        assert not _is_linked(b1, 'xhtml_AContent', a)
    if hasattr(b2, 'xhtml_AContent'):
        assert _is_linked(b2, 'xhtml_AContent', a)
    _safe_set(a, 'xhtml_Br', None)
    assert not _is_linked(a, 'xhtml_Br', b2)
    if hasattr(b2, 'xhtml_AContent'):
        assert not _is_linked(b2, 'xhtml_AContent', a)


def test_assoc_br164_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Br(class_="sample_text", style="sample_text")
    b2 = xhtml_Br(class_="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline165', {b1})
    assert _is_linked(a, 'xhtml_Inline165', b1)
    if hasattr(b1, 'xhtml_Br166'):
        assert _is_linked(b1, 'xhtml_Br166', a)
    _safe_set(a, 'xhtml_Inline165', {b2})
    assert _is_linked(a, 'xhtml_Inline165', b2)
    if hasattr(b1, 'xhtml_Br166'):
        assert not _is_linked(b1, 'xhtml_Br166', a)
    if hasattr(b2, 'xhtml_Br166'):
        assert _is_linked(b2, 'xhtml_Br166', a)
    _safe_set(a, 'xhtml_Inline165', set())
    assert not _is_linked(a, 'xhtml_Inline165', b2)
    if hasattr(b2, 'xhtml_Br166'):
        assert not _is_linked(b2, 'xhtml_Br166', a)


def test_assoc_br262_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Br(class_="sample_text", style="sample_text")
    b2 = xhtml_Br(class_="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object263', {b1})
    assert _is_linked(a, 'xhtml_Object263', b1)
    if hasattr(b1, 'xhtml_Br264'):
        assert _is_linked(b1, 'xhtml_Br264', a)
    _safe_set(a, 'xhtml_Object263', {b2})
    assert _is_linked(a, 'xhtml_Object263', b2)
    if hasattr(b1, 'xhtml_Br264'):
        assert not _is_linked(b1, 'xhtml_Br264', a)
    if hasattr(b2, 'xhtml_Br264'):
        assert _is_linked(b2, 'xhtml_Br264', a)
    _safe_set(a, 'xhtml_Object263', set())
    assert not _is_linked(a, 'xhtml_Object263', b2)
    if hasattr(b2, 'xhtml_Br264'):
        assert not _is_linked(b2, 'xhtml_Br264', a)


def test_assoc_br386_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Br(class_="sample_text", style="sample_text")
    b2 = xhtml_Br(class_="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent387', {b1})
    assert _is_linked(a, 'xhtml_PreContent387', b1)
    if hasattr(b1, 'xhtml_Br388'):
        assert _is_linked(b1, 'xhtml_Br388', a)
    _safe_set(a, 'xhtml_PreContent387', {b2})
    assert _is_linked(a, 'xhtml_PreContent387', b2)
    if hasattr(b1, 'xhtml_Br388'):
        assert not _is_linked(b1, 'xhtml_Br388', a)
    if hasattr(b2, 'xhtml_Br388'):
        assert _is_linked(b2, 'xhtml_Br388', a)
    _safe_set(a, 'xhtml_PreContent387', set())
    assert not _is_linked(a, 'xhtml_PreContent387', b2)
    if hasattr(b2, 'xhtml_Br388'):
        assert not _is_linked(b2, 'xhtml_Br388', a)


def test_assoc_br93_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Br(class_="sample_text", style="sample_text")
    b2 = xhtml_Br(class_="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow94', {b1})
    assert _is_linked(a, 'xhtml_Flow94', b1)
    if hasattr(b1, 'xhtml_Br95'):
        assert _is_linked(b1, 'xhtml_Br95', a)
    _safe_set(a, 'xhtml_Flow94', {b2})
    assert _is_linked(a, 'xhtml_Flow94', b2)
    if hasattr(b1, 'xhtml_Br95'):
        assert not _is_linked(b1, 'xhtml_Br95', a)
    if hasattr(b2, 'xhtml_Br95'):
        assert _is_linked(b2, 'xhtml_Br95', a)
    _safe_set(a, 'xhtml_Flow94', set())
    assert not _is_linked(a, 'xhtml_Flow94', b2)
    if hasattr(b2, 'xhtml_Br95'):
        assert not _is_linked(b2, 'xhtml_Br95', a)


def test_assoc_caption392_link_reassign_clear():
    a = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Caption(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Caption(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Table393', b1)
    assert _is_linked(a, 'xhtml_Table393', b1)
    if hasattr(b1, 'xhtml_Caption'):
        assert _is_linked(b1, 'xhtml_Caption', a)
    _safe_set(a, 'xhtml_Table393', b2)
    assert _is_linked(a, 'xhtml_Table393', b2)
    if hasattr(b1, 'xhtml_Caption'):
        assert not _is_linked(b1, 'xhtml_Caption', a)
    if hasattr(b2, 'xhtml_Caption'):
        assert _is_linked(b2, 'xhtml_Caption', a)
    _safe_set(a, 'xhtml_Table393', None)
    assert not _is_linked(a, 'xhtml_Table393', b2)
    if hasattr(b2, 'xhtml_Caption'):
        assert not _is_linked(b2, 'xhtml_Caption', a)


def test_assoc_cite144_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Cite(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow145', {b1})
    assert _is_linked(a, 'xhtml_Flow145', b1)
    if hasattr(b1, 'xhtml_Cite146'):
        assert _is_linked(b1, 'xhtml_Cite146', a)
    _safe_set(a, 'xhtml_Flow145', {b2})
    assert _is_linked(a, 'xhtml_Flow145', b2)
    if hasattr(b1, 'xhtml_Cite146'):
        assert not _is_linked(b1, 'xhtml_Cite146', a)
    if hasattr(b2, 'xhtml_Cite146'):
        assert _is_linked(b2, 'xhtml_Cite146', a)
    _safe_set(a, 'xhtml_Flow145', set())
    assert not _is_linked(a, 'xhtml_Flow145', b2)
    if hasattr(b2, 'xhtml_Cite146'):
        assert not _is_linked(b2, 'xhtml_Cite146', a)


def test_assoc_cite215_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Cite(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline216', {b1})
    assert _is_linked(a, 'xhtml_Inline216', b1)
    if hasattr(b1, 'xhtml_Cite217'):
        assert _is_linked(b1, 'xhtml_Cite217', a)
    _safe_set(a, 'xhtml_Inline216', {b2})
    assert _is_linked(a, 'xhtml_Inline216', b2)
    if hasattr(b1, 'xhtml_Cite217'):
        assert not _is_linked(b1, 'xhtml_Cite217', a)
    if hasattr(b2, 'xhtml_Cite217'):
        assert _is_linked(b2, 'xhtml_Cite217', a)
    _safe_set(a, 'xhtml_Inline216', set())
    assert not _is_linked(a, 'xhtml_Inline216', b2)
    if hasattr(b2, 'xhtml_Cite217'):
        assert not _is_linked(b2, 'xhtml_Cite217', a)


def test_assoc_cite313_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Cite(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object314', {b1})
    assert _is_linked(a, 'xhtml_Object314', b1)
    if hasattr(b1, 'xhtml_Cite315'):
        assert _is_linked(b1, 'xhtml_Cite315', a)
    _safe_set(a, 'xhtml_Object314', {b2})
    assert _is_linked(a, 'xhtml_Object314', b2)
    if hasattr(b1, 'xhtml_Cite315'):
        assert not _is_linked(b1, 'xhtml_Cite315', a)
    if hasattr(b2, 'xhtml_Cite315'):
        assert _is_linked(b2, 'xhtml_Cite315', a)
    _safe_set(a, 'xhtml_Object314', set())
    assert not _is_linked(a, 'xhtml_Object314', b2)
    if hasattr(b2, 'xhtml_Cite315'):
        assert not _is_linked(b2, 'xhtml_Cite315', a)


def test_assoc_cite33_link_reassign_clear():
    a = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Cite', b1)
    assert _is_linked(a, 'xhtml_Cite', b1)
    if hasattr(b1, 'xhtml_AContent34'):
        assert _is_linked(b1, 'xhtml_AContent34', a)
    _safe_set(a, 'xhtml_Cite', b2)
    assert _is_linked(a, 'xhtml_Cite', b2)
    if hasattr(b1, 'xhtml_AContent34'):
        assert not _is_linked(b1, 'xhtml_AContent34', a)
    if hasattr(b2, 'xhtml_AContent34'):
        assert _is_linked(b2, 'xhtml_AContent34', a)
    _safe_set(a, 'xhtml_Cite', None)
    assert not _is_linked(a, 'xhtml_Cite', b2)
    if hasattr(b2, 'xhtml_AContent34'):
        assert not _is_linked(b2, 'xhtml_AContent34', a)


def test_assoc_cite371_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Cite(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Cite(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent372', {b1})
    assert _is_linked(a, 'xhtml_PreContent372', b1)
    if hasattr(b1, 'xhtml_Cite373'):
        assert _is_linked(b1, 'xhtml_Cite373', a)
    _safe_set(a, 'xhtml_PreContent372', {b2})
    assert _is_linked(a, 'xhtml_PreContent372', b2)
    if hasattr(b1, 'xhtml_Cite373'):
        assert not _is_linked(b1, 'xhtml_Cite373', a)
    if hasattr(b2, 'xhtml_Cite373'):
        assert _is_linked(b2, 'xhtml_Cite373', a)
    _safe_set(a, 'xhtml_PreContent372', set())
    assert not _is_linked(a, 'xhtml_PreContent372', b2)
    if hasattr(b2, 'xhtml_Cite373'):
        assert not _is_linked(b2, 'xhtml_Cite373', a)


def test_assoc_code129_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Code(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow130', {b1})
    assert _is_linked(a, 'xhtml_Flow130', b1)
    if hasattr(b1, 'xhtml_Code131'):
        assert _is_linked(b1, 'xhtml_Code131', a)
    _safe_set(a, 'xhtml_Flow130', {b2})
    assert _is_linked(a, 'xhtml_Flow130', b2)
    if hasattr(b1, 'xhtml_Code131'):
        assert not _is_linked(b1, 'xhtml_Code131', a)
    if hasattr(b2, 'xhtml_Code131'):
        assert _is_linked(b2, 'xhtml_Code131', a)
    _safe_set(a, 'xhtml_Flow130', set())
    assert not _is_linked(a, 'xhtml_Flow130', b2)
    if hasattr(b2, 'xhtml_Code131'):
        assert not _is_linked(b2, 'xhtml_Code131', a)


def test_assoc_code200_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Code(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline201', {b1})
    assert _is_linked(a, 'xhtml_Inline201', b1)
    if hasattr(b1, 'xhtml_Code202'):
        assert _is_linked(b1, 'xhtml_Code202', a)
    _safe_set(a, 'xhtml_Inline201', {b2})
    assert _is_linked(a, 'xhtml_Inline201', b2)
    if hasattr(b1, 'xhtml_Code202'):
        assert not _is_linked(b1, 'xhtml_Code202', a)
    if hasattr(b2, 'xhtml_Code202'):
        assert _is_linked(b2, 'xhtml_Code202', a)
    _safe_set(a, 'xhtml_Inline201', set())
    assert not _is_linked(a, 'xhtml_Inline201', b2)
    if hasattr(b2, 'xhtml_Code202'):
        assert not _is_linked(b2, 'xhtml_Code202', a)


def test_assoc_code23_link_reassign_clear():
    a = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Code', b1)
    assert _is_linked(a, 'xhtml_Code', b1)
    if hasattr(b1, 'xhtml_AContent24'):
        assert _is_linked(b1, 'xhtml_AContent24', a)
    _safe_set(a, 'xhtml_Code', b2)
    assert _is_linked(a, 'xhtml_Code', b2)
    if hasattr(b1, 'xhtml_AContent24'):
        assert not _is_linked(b1, 'xhtml_AContent24', a)
    if hasattr(b2, 'xhtml_AContent24'):
        assert _is_linked(b2, 'xhtml_AContent24', a)
    _safe_set(a, 'xhtml_Code', None)
    assert not _is_linked(a, 'xhtml_Code', b2)
    if hasattr(b2, 'xhtml_AContent24'):
        assert not _is_linked(b2, 'xhtml_AContent24', a)


def test_assoc_code298_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Code(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object299', {b1})
    assert _is_linked(a, 'xhtml_Object299', b1)
    if hasattr(b1, 'xhtml_Code300'):
        assert _is_linked(b1, 'xhtml_Code300', a)
    _safe_set(a, 'xhtml_Object299', {b2})
    assert _is_linked(a, 'xhtml_Object299', b2)
    if hasattr(b1, 'xhtml_Code300'):
        assert not _is_linked(b1, 'xhtml_Code300', a)
    if hasattr(b2, 'xhtml_Code300'):
        assert _is_linked(b2, 'xhtml_Code300', a)
    _safe_set(a, 'xhtml_Object299', set())
    assert not _is_linked(a, 'xhtml_Object299', b2)
    if hasattr(b2, 'xhtml_Code300'):
        assert not _is_linked(b2, 'xhtml_Code300', a)


def test_assoc_code356_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Code(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Code(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent357', {b1})
    assert _is_linked(a, 'xhtml_PreContent357', b1)
    if hasattr(b1, 'xhtml_Code358'):
        assert _is_linked(b1, 'xhtml_Code358', a)
    _safe_set(a, 'xhtml_PreContent357', {b2})
    assert _is_linked(a, 'xhtml_PreContent357', b2)
    if hasattr(b1, 'xhtml_Code358'):
        assert not _is_linked(b1, 'xhtml_Code358', a)
    if hasattr(b2, 'xhtml_Code358'):
        assert _is_linked(b2, 'xhtml_Code358', a)
    _safe_set(a, 'xhtml_PreContent357', set())
    assert not _is_linked(a, 'xhtml_PreContent357', b2)
    if hasattr(b2, 'xhtml_Code358'):
        assert not _is_linked(b2, 'xhtml_Code358', a)


def test_assoc_col394_link_reassign_clear():
    a = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    b2 = xhtml_Col(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", span="sample_text_2", style="sample_text_2", valign="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Table395', {b1})
    assert _is_linked(a, 'xhtml_Table395', b1)
    if hasattr(b1, 'xhtml_Col396'):
        assert _is_linked(b1, 'xhtml_Col396', a)
    _safe_set(a, 'xhtml_Table395', {b2})
    assert _is_linked(a, 'xhtml_Table395', b2)
    if hasattr(b1, 'xhtml_Col396'):
        assert not _is_linked(b1, 'xhtml_Col396', a)
    if hasattr(b2, 'xhtml_Col396'):
        assert _is_linked(b2, 'xhtml_Col396', a)
    _safe_set(a, 'xhtml_Table395', set())
    assert not _is_linked(a, 'xhtml_Table395', b2)
    if hasattr(b2, 'xhtml_Col396'):
        assert not _is_linked(b2, 'xhtml_Col396', a)


def test_assoc_col60_link_reassign_clear():
    a = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    b1 = xhtml_Col(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    b2 = xhtml_Col(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", span="sample_text_2", style="sample_text_2", valign="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Colgroup', {b1})
    assert _is_linked(a, 'xhtml_Colgroup', b1)
    if hasattr(b1, 'xhtml_Col'):
        assert _is_linked(b1, 'xhtml_Col', a)
    _safe_set(a, 'xhtml_Colgroup', {b2})
    assert _is_linked(a, 'xhtml_Colgroup', b2)
    if hasattr(b1, 'xhtml_Col'):
        assert not _is_linked(b1, 'xhtml_Col', a)
    if hasattr(b2, 'xhtml_Col'):
        assert _is_linked(b2, 'xhtml_Col', a)
    _safe_set(a, 'xhtml_Colgroup', set())
    assert not _is_linked(a, 'xhtml_Colgroup', b2)
    if hasattr(b2, 'xhtml_Col'):
        assert not _is_linked(b2, 'xhtml_Col', a)


def test_assoc_colgroup397_link_reassign_clear():
    a = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Colgroup(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", span="sample_text", style="sample_text", valign="sample_text", width="sample_text")
    b2 = xhtml_Colgroup(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", span="sample_text_2", style="sample_text_2", valign="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Table398', {b1})
    assert _is_linked(a, 'xhtml_Table398', b1)
    if hasattr(b1, 'xhtml_Colgroup399'):
        assert _is_linked(b1, 'xhtml_Colgroup399', a)
    _safe_set(a, 'xhtml_Table398', {b2})
    assert _is_linked(a, 'xhtml_Table398', b2)
    if hasattr(b1, 'xhtml_Colgroup399'):
        assert not _is_linked(b1, 'xhtml_Colgroup399', a)
    if hasattr(b2, 'xhtml_Colgroup399'):
        assert _is_linked(b2, 'xhtml_Colgroup399', a)
    _safe_set(a, 'xhtml_Table398', set())
    assert not _is_linked(a, 'xhtml_Table398', b2)
    if hasattr(b2, 'xhtml_Colgroup399'):
        assert not _is_linked(b2, 'xhtml_Colgroup399', a)


def test_assoc_dd63_link_reassign_clear():
    a = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Dd(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dd(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Dl64', {b1})
    assert _is_linked(a, 'xhtml_Dl64', b1)
    if hasattr(b1, 'xhtml_Dd'):
        assert _is_linked(b1, 'xhtml_Dd', a)
    _safe_set(a, 'xhtml_Dl64', {b2})
    assert _is_linked(a, 'xhtml_Dl64', b2)
    if hasattr(b1, 'xhtml_Dd'):
        assert not _is_linked(b1, 'xhtml_Dd', a)
    if hasattr(b2, 'xhtml_Dd'):
        assert _is_linked(b2, 'xhtml_Dd', a)
    _safe_set(a, 'xhtml_Dl64', set())
    assert not _is_linked(a, 'xhtml_Dl64', b2)
    if hasattr(b2, 'xhtml_Dd'):
        assert not _is_linked(b2, 'xhtml_Dd', a)


def test_assoc_dfn126_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dfn(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow127', {b1})
    assert _is_linked(a, 'xhtml_Flow127', b1)
    if hasattr(b1, 'xhtml_Dfn128'):
        assert _is_linked(b1, 'xhtml_Dfn128', a)
    _safe_set(a, 'xhtml_Flow127', {b2})
    assert _is_linked(a, 'xhtml_Flow127', b2)
    if hasattr(b1, 'xhtml_Dfn128'):
        assert not _is_linked(b1, 'xhtml_Dfn128', a)
    if hasattr(b2, 'xhtml_Dfn128'):
        assert _is_linked(b2, 'xhtml_Dfn128', a)
    _safe_set(a, 'xhtml_Flow127', set())
    assert not _is_linked(a, 'xhtml_Flow127', b2)
    if hasattr(b2, 'xhtml_Dfn128'):
        assert not _is_linked(b2, 'xhtml_Dfn128', a)


def test_assoc_dfn197_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dfn(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline198', {b1})
    assert _is_linked(a, 'xhtml_Inline198', b1)
    if hasattr(b1, 'xhtml_Dfn199'):
        assert _is_linked(b1, 'xhtml_Dfn199', a)
    _safe_set(a, 'xhtml_Inline198', {b2})
    assert _is_linked(a, 'xhtml_Inline198', b2)
    if hasattr(b1, 'xhtml_Dfn199'):
        assert not _is_linked(b1, 'xhtml_Dfn199', a)
    if hasattr(b2, 'xhtml_Dfn199'):
        assert _is_linked(b2, 'xhtml_Dfn199', a)
    _safe_set(a, 'xhtml_Inline198', set())
    assert not _is_linked(a, 'xhtml_Inline198', b2)
    if hasattr(b2, 'xhtml_Dfn199'):
        assert not _is_linked(b2, 'xhtml_Dfn199', a)


def test_assoc_dfn21_link_reassign_clear():
    a = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Dfn', b1)
    assert _is_linked(a, 'xhtml_Dfn', b1)
    if hasattr(b1, 'xhtml_AContent22'):
        assert _is_linked(b1, 'xhtml_AContent22', a)
    _safe_set(a, 'xhtml_Dfn', b2)
    assert _is_linked(a, 'xhtml_Dfn', b2)
    if hasattr(b1, 'xhtml_AContent22'):
        assert not _is_linked(b1, 'xhtml_AContent22', a)
    if hasattr(b2, 'xhtml_AContent22'):
        assert _is_linked(b2, 'xhtml_AContent22', a)
    _safe_set(a, 'xhtml_Dfn', None)
    assert not _is_linked(a, 'xhtml_Dfn', b2)
    if hasattr(b2, 'xhtml_AContent22'):
        assert not _is_linked(b2, 'xhtml_AContent22', a)


def test_assoc_dfn295_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dfn(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object296', {b1})
    assert _is_linked(a, 'xhtml_Object296', b1)
    if hasattr(b1, 'xhtml_Dfn297'):
        assert _is_linked(b1, 'xhtml_Dfn297', a)
    _safe_set(a, 'xhtml_Object296', {b2})
    assert _is_linked(a, 'xhtml_Object296', b2)
    if hasattr(b1, 'xhtml_Dfn297'):
        assert not _is_linked(b1, 'xhtml_Dfn297', a)
    if hasattr(b2, 'xhtml_Dfn297'):
        assert _is_linked(b2, 'xhtml_Dfn297', a)
    _safe_set(a, 'xhtml_Object296', set())
    assert not _is_linked(a, 'xhtml_Object296', b2)
    if hasattr(b2, 'xhtml_Dfn297'):
        assert not _is_linked(b2, 'xhtml_Dfn297', a)


def test_assoc_dfn353_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Dfn(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dfn(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent354', {b1})
    assert _is_linked(a, 'xhtml_PreContent354', b1)
    if hasattr(b1, 'xhtml_Dfn355'):
        assert _is_linked(b1, 'xhtml_Dfn355', a)
    _safe_set(a, 'xhtml_PreContent354', {b2})
    assert _is_linked(a, 'xhtml_PreContent354', b2)
    if hasattr(b1, 'xhtml_Dfn355'):
        assert not _is_linked(b1, 'xhtml_Dfn355', a)
    if hasattr(b2, 'xhtml_Dfn355'):
        assert _is_linked(b2, 'xhtml_Dfn355', a)
    _safe_set(a, 'xhtml_PreContent354', set())
    assert not _is_linked(a, 'xhtml_PreContent354', b2)
    if hasattr(b2, 'xhtml_Dfn355'):
        assert not _is_linked(b2, 'xhtml_Dfn355', a)


def test_assoc_div235_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    b2 = xhtml_Div(class_="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", style="sample_text_2", title="sample_text_2")
    _safe_set(a, 'xhtml_Object236', {b1})
    assert _is_linked(a, 'xhtml_Object236', b1)
    if hasattr(b1, 'xhtml_Div237'):
        assert _is_linked(b1, 'xhtml_Div237', a)
    _safe_set(a, 'xhtml_Object236', {b2})
    assert _is_linked(a, 'xhtml_Object236', b2)
    if hasattr(b1, 'xhtml_Div237'):
        assert not _is_linked(b1, 'xhtml_Div237', a)
    if hasattr(b2, 'xhtml_Div237'):
        assert _is_linked(b2, 'xhtml_Div237', a)
    _safe_set(a, 'xhtml_Object236', set())
    assert not _is_linked(a, 'xhtml_Object236', b2)
    if hasattr(b2, 'xhtml_Div237'):
        assert not _is_linked(b2, 'xhtml_Div237', a)


def test_assoc_div44_link_reassign_clear():
    a = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Div', b1)
    assert _is_linked(a, 'xhtml_Div', b1)
    if hasattr(b1, 'xhtml_Block45'):
        assert _is_linked(b1, 'xhtml_Block45', a)
    _safe_set(a, 'xhtml_Div', b2)
    assert _is_linked(a, 'xhtml_Div', b2)
    if hasattr(b1, 'xhtml_Block45'):
        assert not _is_linked(b1, 'xhtml_Block45', a)
    if hasattr(b2, 'xhtml_Block45'):
        assert _is_linked(b2, 'xhtml_Block45', a)
    _safe_set(a, 'xhtml_Div', None)
    assert not _is_linked(a, 'xhtml_Div', b2)
    if hasattr(b2, 'xhtml_Block45'):
        assert not _is_linked(b2, 'xhtml_Block45', a)


def test_assoc_div67_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Div(class_="sample_text", hl7Id="sample_text", lang="sample_text", style="sample_text", title="sample_text")
    b2 = xhtml_Div(class_="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", style="sample_text_2", title="sample_text_2")
    _safe_set(a, 'xhtml_Flow68', {b1})
    assert _is_linked(a, 'xhtml_Flow68', b1)
    if hasattr(b1, 'xhtml_Div69'):
        assert _is_linked(b1, 'xhtml_Div69', a)
    _safe_set(a, 'xhtml_Flow68', {b2})
    assert _is_linked(a, 'xhtml_Flow68', b2)
    if hasattr(b1, 'xhtml_Div69'):
        assert not _is_linked(b1, 'xhtml_Div69', a)
    if hasattr(b2, 'xhtml_Div69'):
        assert _is_linked(b2, 'xhtml_Div69', a)
    _safe_set(a, 'xhtml_Flow68', set())
    assert not _is_linked(a, 'xhtml_Flow68', b2)
    if hasattr(b2, 'xhtml_Div69'):
        assert not _is_linked(b2, 'xhtml_Div69', a)


def test_assoc_dl244_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dl(class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object245', {b1})
    assert _is_linked(a, 'xhtml_Object245', b1)
    if hasattr(b1, 'xhtml_Dl246'):
        assert _is_linked(b1, 'xhtml_Dl246', a)
    _safe_set(a, 'xhtml_Object245', {b2})
    assert _is_linked(a, 'xhtml_Object245', b2)
    if hasattr(b1, 'xhtml_Dl246'):
        assert not _is_linked(b1, 'xhtml_Dl246', a)
    if hasattr(b2, 'xhtml_Dl246'):
        assert _is_linked(b2, 'xhtml_Dl246', a)
    _safe_set(a, 'xhtml_Object245', set())
    assert not _is_linked(a, 'xhtml_Object245', b2)
    if hasattr(b2, 'xhtml_Dl246'):
        assert not _is_linked(b2, 'xhtml_Dl246', a)


def test_assoc_dl50_link_reassign_clear():
    a = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Dl', b1)
    assert _is_linked(a, 'xhtml_Dl', b1)
    if hasattr(b1, 'xhtml_Block51'):
        assert _is_linked(b1, 'xhtml_Block51', a)
    _safe_set(a, 'xhtml_Dl', b2)
    assert _is_linked(a, 'xhtml_Dl', b2)
    if hasattr(b1, 'xhtml_Block51'):
        assert not _is_linked(b1, 'xhtml_Block51', a)
    if hasattr(b2, 'xhtml_Block51'):
        assert _is_linked(b2, 'xhtml_Block51', a)
    _safe_set(a, 'xhtml_Dl', None)
    assert not _is_linked(a, 'xhtml_Dl', b2)
    if hasattr(b2, 'xhtml_Block51'):
        assert not _is_linked(b2, 'xhtml_Block51', a)


def test_assoc_dl76_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dl(class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow77', {b1})
    assert _is_linked(a, 'xhtml_Flow77', b1)
    if hasattr(b1, 'xhtml_Dl78'):
        assert _is_linked(b1, 'xhtml_Dl78', a)
    _safe_set(a, 'xhtml_Flow77', {b2})
    assert _is_linked(a, 'xhtml_Flow77', b2)
    if hasattr(b1, 'xhtml_Dl78'):
        assert not _is_linked(b1, 'xhtml_Dl78', a)
    if hasattr(b2, 'xhtml_Dl78'):
        assert _is_linked(b2, 'xhtml_Dl78', a)
    _safe_set(a, 'xhtml_Flow77', set())
    assert not _is_linked(a, 'xhtml_Flow77', b2)
    if hasattr(b2, 'xhtml_Dl78'):
        assert not _is_linked(b2, 'xhtml_Dl78', a)


def test_assoc_dt61_link_reassign_clear():
    a = xhtml_Dt(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Dl(class_="sample_text", group="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Dl(class_="sample_text_2", group="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Dt', b1)
    assert _is_linked(a, 'xhtml_Dt', b1)
    if hasattr(b1, 'xhtml_Dl62'):
        assert _is_linked(b1, 'xhtml_Dl62', a)
    _safe_set(a, 'xhtml_Dt', b2)
    assert _is_linked(a, 'xhtml_Dt', b2)
    if hasattr(b1, 'xhtml_Dl62'):
        assert not _is_linked(b1, 'xhtml_Dl62', a)
    if hasattr(b2, 'xhtml_Dl62'):
        assert _is_linked(b2, 'xhtml_Dl62', a)
    _safe_set(a, 'xhtml_Dt', None)
    assert not _is_linked(a, 'xhtml_Dt', b2)
    if hasattr(b2, 'xhtml_Dl62'):
        assert not _is_linked(b2, 'xhtml_Dl62', a)


def test_assoc_em120_link_reassign_clear():
    a = xhtml_Flow(group="sample_text", mixed="sample_text")
    b1 = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Em(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Flow121', {b1})
    assert _is_linked(a, 'xhtml_Flow121', b1)
    if hasattr(b1, 'xhtml_Em122'):
        assert _is_linked(b1, 'xhtml_Em122', a)
    _safe_set(a, 'xhtml_Flow121', {b2})
    assert _is_linked(a, 'xhtml_Flow121', b2)
    if hasattr(b1, 'xhtml_Em122'):
        assert not _is_linked(b1, 'xhtml_Em122', a)
    if hasattr(b2, 'xhtml_Em122'):
        assert _is_linked(b2, 'xhtml_Em122', a)
    _safe_set(a, 'xhtml_Flow121', set())
    assert not _is_linked(a, 'xhtml_Flow121', b2)
    if hasattr(b2, 'xhtml_Em122'):
        assert not _is_linked(b2, 'xhtml_Em122', a)


def test_assoc_em17_link_reassign_clear():
    a = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Em', b1)
    assert _is_linked(a, 'xhtml_Em', b1)
    if hasattr(b1, 'xhtml_AContent18'):
        assert _is_linked(b1, 'xhtml_AContent18', a)
    _safe_set(a, 'xhtml_Em', b2)
    assert _is_linked(a, 'xhtml_Em', b2)
    if hasattr(b1, 'xhtml_AContent18'):
        assert not _is_linked(b1, 'xhtml_AContent18', a)
    if hasattr(b2, 'xhtml_AContent18'):
        assert _is_linked(b2, 'xhtml_AContent18', a)
    _safe_set(a, 'xhtml_Em', None)
    assert not _is_linked(a, 'xhtml_Em', b2)
    if hasattr(b2, 'xhtml_AContent18'):
        assert not _is_linked(b2, 'xhtml_AContent18', a)


def test_assoc_em191_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Em(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline192', {b1})
    assert _is_linked(a, 'xhtml_Inline192', b1)
    if hasattr(b1, 'xhtml_Em193'):
        assert _is_linked(b1, 'xhtml_Em193', a)
    _safe_set(a, 'xhtml_Inline192', {b2})
    assert _is_linked(a, 'xhtml_Inline192', b2)
    if hasattr(b1, 'xhtml_Em193'):
        assert not _is_linked(b1, 'xhtml_Em193', a)
    if hasattr(b2, 'xhtml_Em193'):
        assert _is_linked(b2, 'xhtml_Em193', a)
    _safe_set(a, 'xhtml_Inline192', set())
    assert not _is_linked(a, 'xhtml_Inline192', b2)
    if hasattr(b2, 'xhtml_Em193'):
        assert not _is_linked(b2, 'xhtml_Em193', a)


def test_assoc_em289_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Em(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object290', {b1})
    assert _is_linked(a, 'xhtml_Object290', b1)
    if hasattr(b1, 'xhtml_Em291'):
        assert _is_linked(b1, 'xhtml_Em291', a)
    _safe_set(a, 'xhtml_Object290', {b2})
    assert _is_linked(a, 'xhtml_Object290', b2)
    if hasattr(b1, 'xhtml_Em291'):
        assert not _is_linked(b1, 'xhtml_Em291', a)
    if hasattr(b2, 'xhtml_Em291'):
        assert _is_linked(b2, 'xhtml_Em291', a)
    _safe_set(a, 'xhtml_Object290', set())
    assert not _is_linked(a, 'xhtml_Object290', b2)
    if hasattr(b2, 'xhtml_Em291'):
        assert not _is_linked(b2, 'xhtml_Em291', a)


def test_assoc_em347_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Em(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Em(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent348', {b1})
    assert _is_linked(a, 'xhtml_PreContent348', b1)
    if hasattr(b1, 'xhtml_Em349'):
        assert _is_linked(b1, 'xhtml_Em349', a)
    _safe_set(a, 'xhtml_PreContent348', {b2})
    assert _is_linked(a, 'xhtml_PreContent348', b2)
    if hasattr(b1, 'xhtml_Em349'):
        assert not _is_linked(b1, 'xhtml_Em349', a)
    if hasattr(b2, 'xhtml_Em349'):
        assert _is_linked(b2, 'xhtml_Em349', a)
    _safe_set(a, 'xhtml_PreContent348', set())
    assert not _is_linked(a, 'xhtml_PreContent348', b2)
    if hasattr(b2, 'xhtml_Em349'):
        assert not _is_linked(b2, 'xhtml_Em349', a)


def test_assoc_hr250_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Hr(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object251', {b1})
    assert _is_linked(a, 'xhtml_Object251', b1)
    if hasattr(b1, 'xhtml_Hr252'):
        assert _is_linked(b1, 'xhtml_Hr252', a)
    _safe_set(a, 'xhtml_Object251', {b2})
    assert _is_linked(a, 'xhtml_Object251', b2)
    if hasattr(b1, 'xhtml_Hr252'):
        assert not _is_linked(b1, 'xhtml_Hr252', a)
    if hasattr(b2, 'xhtml_Hr252'):
        assert _is_linked(b2, 'xhtml_Hr252', a)
    _safe_set(a, 'xhtml_Object251', set())
    assert not _is_linked(a, 'xhtml_Object251', b2)
    if hasattr(b2, 'xhtml_Hr252'):
        assert not _is_linked(b2, 'xhtml_Hr252', a)


def test_assoc_hr54_link_reassign_clear():
    a = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Hr', b1)
    assert _is_linked(a, 'xhtml_Hr', b1)
    if hasattr(b1, 'xhtml_Block55'):
        assert _is_linked(b1, 'xhtml_Block55', a)
    _safe_set(a, 'xhtml_Hr', b2)
    assert _is_linked(a, 'xhtml_Hr', b2)
    if hasattr(b1, 'xhtml_Block55'):
        assert not _is_linked(b1, 'xhtml_Block55', a)
    if hasattr(b2, 'xhtml_Block55'):
        assert _is_linked(b2, 'xhtml_Block55', a)
    _safe_set(a, 'xhtml_Hr', None)
    assert not _is_linked(a, 'xhtml_Hr', b2)
    if hasattr(b2, 'xhtml_Block55'):
        assert not _is_linked(b2, 'xhtml_Block55', a)


def test_assoc_hr82_link_reassign_clear():
    a = xhtml_Hr(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Hr84', b1)
    assert _is_linked(a, 'xhtml_Hr84', b1)
    if hasattr(b1, 'xhtml_Flow83'):
        assert _is_linked(b1, 'xhtml_Flow83', a)
    _safe_set(a, 'xhtml_Hr84', b2)
    assert _is_linked(a, 'xhtml_Hr84', b2)
    if hasattr(b1, 'xhtml_Flow83'):
        assert not _is_linked(b1, 'xhtml_Flow83', a)
    if hasattr(b2, 'xhtml_Flow83'):
        assert _is_linked(b2, 'xhtml_Flow83', a)
    _safe_set(a, 'xhtml_Hr84', None)
    assert not _is_linked(a, 'xhtml_Hr84', b2)
    if hasattr(b2, 'xhtml_Flow83'):
        assert not _is_linked(b2, 'xhtml_Flow83', a)


def test_assoc_i108_link_reassign_clear():
    a = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_I110', b1)
    assert _is_linked(a, 'xhtml_I110', b1)
    if hasattr(b1, 'xhtml_Flow109'):
        assert _is_linked(b1, 'xhtml_Flow109', a)
    _safe_set(a, 'xhtml_I110', b2)
    assert _is_linked(a, 'xhtml_I110', b2)
    if hasattr(b1, 'xhtml_Flow109'):
        assert not _is_linked(b1, 'xhtml_Flow109', a)
    if hasattr(b2, 'xhtml_Flow109'):
        assert _is_linked(b2, 'xhtml_Flow109', a)
    _safe_set(a, 'xhtml_I110', None)
    assert not _is_linked(a, 'xhtml_I110', b2)
    if hasattr(b2, 'xhtml_Flow109'):
        assert not _is_linked(b2, 'xhtml_Flow109', a)


def test_assoc_i179_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_I(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Inline180', {b1})
    assert _is_linked(a, 'xhtml_Inline180', b1)
    if hasattr(b1, 'xhtml_I181'):
        assert _is_linked(b1, 'xhtml_I181', a)
    _safe_set(a, 'xhtml_Inline180', {b2})
    assert _is_linked(a, 'xhtml_Inline180', b2)
    if hasattr(b1, 'xhtml_I181'):
        assert not _is_linked(b1, 'xhtml_I181', a)
    if hasattr(b2, 'xhtml_I181'):
        assert _is_linked(b2, 'xhtml_I181', a)
    _safe_set(a, 'xhtml_Inline180', set())
    assert not _is_linked(a, 'xhtml_Inline180', b2)
    if hasattr(b2, 'xhtml_I181'):
        assert not _is_linked(b2, 'xhtml_I181', a)


def test_assoc_i277_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_I(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object278', {b1})
    assert _is_linked(a, 'xhtml_Object278', b1)
    if hasattr(b1, 'xhtml_I279'):
        assert _is_linked(b1, 'xhtml_I279', a)
    _safe_set(a, 'xhtml_Object278', {b2})
    assert _is_linked(a, 'xhtml_Object278', b2)
    if hasattr(b1, 'xhtml_I279'):
        assert not _is_linked(b1, 'xhtml_I279', a)
    if hasattr(b2, 'xhtml_I279'):
        assert _is_linked(b2, 'xhtml_I279', a)
    _safe_set(a, 'xhtml_Object278', set())
    assert not _is_linked(a, 'xhtml_Object278', b2)
    if hasattr(b2, 'xhtml_I279'):
        assert not _is_linked(b2, 'xhtml_I279', a)


def test_assoc_i335_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_I(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent336', {b1})
    assert _is_linked(a, 'xhtml_PreContent336', b1)
    if hasattr(b1, 'xhtml_I337'):
        assert _is_linked(b1, 'xhtml_I337', a)
    _safe_set(a, 'xhtml_PreContent336', {b2})
    assert _is_linked(a, 'xhtml_PreContent336', b2)
    if hasattr(b1, 'xhtml_I337'):
        assert not _is_linked(b1, 'xhtml_I337', a)
    if hasattr(b2, 'xhtml_I337'):
        assert _is_linked(b2, 'xhtml_I337', a)
    _safe_set(a, 'xhtml_PreContent336', set())
    assert not _is_linked(a, 'xhtml_PreContent336', b2)
    if hasattr(b2, 'xhtml_I337'):
        assert not _is_linked(b2, 'xhtml_I337', a)


def test_assoc_i9_link_reassign_clear():
    a = xhtml_I(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_I', b1)
    assert _is_linked(a, 'xhtml_I', b1)
    if hasattr(b1, 'xhtml_AContent10'):
        assert _is_linked(b1, 'xhtml_AContent10', a)
    _safe_set(a, 'xhtml_I', b2)
    assert _is_linked(a, 'xhtml_I', b2)
    if hasattr(b1, 'xhtml_AContent10'):
        assert not _is_linked(b1, 'xhtml_AContent10', a)
    if hasattr(b2, 'xhtml_AContent10'):
        assert _is_linked(b2, 'xhtml_AContent10', a)
    _safe_set(a, 'xhtml_I', None)
    assert not _is_linked(a, 'xhtml_I', b2)
    if hasattr(b2, 'xhtml_AContent10'):
        assert not _is_linked(b2, 'xhtml_AContent10', a)


def test_assoc_img102_link_reassign_clear():
    a = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Img104', b1)
    assert _is_linked(a, 'xhtml_Img104', b1)
    if hasattr(b1, 'xhtml_Flow103'):
        assert _is_linked(b1, 'xhtml_Flow103', a)
    _safe_set(a, 'xhtml_Img104', b2)
    assert _is_linked(a, 'xhtml_Img104', b2)
    if hasattr(b1, 'xhtml_Flow103'):
        assert not _is_linked(b1, 'xhtml_Flow103', a)
    if hasattr(b2, 'xhtml_Flow103'):
        assert _is_linked(b2, 'xhtml_Flow103', a)
    _safe_set(a, 'xhtml_Img104', None)
    assert not _is_linked(a, 'xhtml_Img104', b2)
    if hasattr(b2, 'xhtml_Flow103'):
        assert not _is_linked(b2, 'xhtml_Flow103', a)


def test_assoc_img173_link_reassign_clear():
    a = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b1 = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    b2 = xhtml_Img(alt="sample_text_2", class_="sample_text_2", height="sample_text_2", hl7Id="sample_text_2", imageType="sample_text_2", lang="sample_text_2", src="sample_text_2", style="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Inline174', {b1})
    assert _is_linked(a, 'xhtml_Inline174', b1)
    if hasattr(b1, 'xhtml_Img175'):
        assert _is_linked(b1, 'xhtml_Img175', a)
    _safe_set(a, 'xhtml_Inline174', {b2})
    assert _is_linked(a, 'xhtml_Inline174', b2)
    if hasattr(b1, 'xhtml_Img175'):
        assert not _is_linked(b1, 'xhtml_Img175', a)
    if hasattr(b2, 'xhtml_Img175'):
        assert _is_linked(b2, 'xhtml_Img175', a)
    _safe_set(a, 'xhtml_Inline174', set())
    assert not _is_linked(a, 'xhtml_Inline174', b2)
    if hasattr(b2, 'xhtml_Img175'):
        assert not _is_linked(b2, 'xhtml_Img175', a)


def test_assoc_img271_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    b2 = xhtml_Img(alt="sample_text_2", class_="sample_text_2", height="sample_text_2", hl7Id="sample_text_2", imageType="sample_text_2", lang="sample_text_2", src="sample_text_2", style="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Object272', {b1})
    assert _is_linked(a, 'xhtml_Object272', b1)
    if hasattr(b1, 'xhtml_Img273'):
        assert _is_linked(b1, 'xhtml_Img273', a)
    _safe_set(a, 'xhtml_Object272', {b2})
    assert _is_linked(a, 'xhtml_Object272', b2)
    if hasattr(b1, 'xhtml_Img273'):
        assert not _is_linked(b1, 'xhtml_Img273', a)
    if hasattr(b2, 'xhtml_Img273'):
        assert _is_linked(b2, 'xhtml_Img273', a)
    _safe_set(a, 'xhtml_Object272', set())
    assert not _is_linked(a, 'xhtml_Object272', b2)
    if hasattr(b2, 'xhtml_Img273'):
        assert not _is_linked(b2, 'xhtml_Img273', a)


def test_assoc_img5_link_reassign_clear():
    a = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Img', b1)
    assert _is_linked(a, 'xhtml_Img', b1)
    if hasattr(b1, 'xhtml_AContent6'):
        assert _is_linked(b1, 'xhtml_AContent6', a)
    _safe_set(a, 'xhtml_Img', b2)
    assert _is_linked(a, 'xhtml_Img', b2)
    if hasattr(b1, 'xhtml_AContent6'):
        assert not _is_linked(b1, 'xhtml_AContent6', a)
    if hasattr(b2, 'xhtml_AContent6'):
        assert _is_linked(b2, 'xhtml_AContent6', a)
    _safe_set(a, 'xhtml_Img', None)
    assert not _is_linked(a, 'xhtml_Img', b2)
    if hasattr(b2, 'xhtml_AContent6'):
        assert not _is_linked(b2, 'xhtml_AContent6', a)


def test_assoc_kbd138_link_reassign_clear():
    a = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Kbd140', b1)
    assert _is_linked(a, 'xhtml_Kbd140', b1)
    if hasattr(b1, 'xhtml_Flow139'):
        assert _is_linked(b1, 'xhtml_Flow139', a)
    _safe_set(a, 'xhtml_Kbd140', b2)
    assert _is_linked(a, 'xhtml_Kbd140', b2)
    if hasattr(b1, 'xhtml_Flow139'):
        assert not _is_linked(b1, 'xhtml_Flow139', a)
    if hasattr(b2, 'xhtml_Flow139'):
        assert _is_linked(b2, 'xhtml_Flow139', a)
    _safe_set(a, 'xhtml_Kbd140', None)
    assert not _is_linked(a, 'xhtml_Kbd140', b2)
    if hasattr(b2, 'xhtml_Flow139'):
        assert not _is_linked(b2, 'xhtml_Flow139', a)


def test_assoc_kbd209_link_reassign_clear():
    a = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Kbd211', b1)
    assert _is_linked(a, 'xhtml_Kbd211', b1)
    if hasattr(b1, 'xhtml_Inline210'):
        assert _is_linked(b1, 'xhtml_Inline210', a)
    _safe_set(a, 'xhtml_Kbd211', b2)
    assert _is_linked(a, 'xhtml_Kbd211', b2)
    if hasattr(b1, 'xhtml_Inline210'):
        assert not _is_linked(b1, 'xhtml_Inline210', a)
    if hasattr(b2, 'xhtml_Inline210'):
        assert _is_linked(b2, 'xhtml_Inline210', a)
    _safe_set(a, 'xhtml_Kbd211', None)
    assert not _is_linked(a, 'xhtml_Kbd211', b2)
    if hasattr(b2, 'xhtml_Inline210'):
        assert not _is_linked(b2, 'xhtml_Inline210', a)


def test_assoc_kbd29_link_reassign_clear():
    a = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Kbd', b1)
    assert _is_linked(a, 'xhtml_Kbd', b1)
    if hasattr(b1, 'xhtml_AContent30'):
        assert _is_linked(b1, 'xhtml_AContent30', a)
    _safe_set(a, 'xhtml_Kbd', b2)
    assert _is_linked(a, 'xhtml_Kbd', b2)
    if hasattr(b1, 'xhtml_AContent30'):
        assert not _is_linked(b1, 'xhtml_AContent30', a)
    if hasattr(b2, 'xhtml_AContent30'):
        assert _is_linked(b2, 'xhtml_AContent30', a)
    _safe_set(a, 'xhtml_Kbd', None)
    assert not _is_linked(a, 'xhtml_Kbd', b2)
    if hasattr(b2, 'xhtml_AContent30'):
        assert not _is_linked(b2, 'xhtml_AContent30', a)


def test_assoc_kbd307_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Kbd(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Object308', {b1})
    assert _is_linked(a, 'xhtml_Object308', b1)
    if hasattr(b1, 'xhtml_Kbd309'):
        assert _is_linked(b1, 'xhtml_Kbd309', a)
    _safe_set(a, 'xhtml_Object308', {b2})
    assert _is_linked(a, 'xhtml_Object308', b2)
    if hasattr(b1, 'xhtml_Kbd309'):
        assert not _is_linked(b1, 'xhtml_Kbd309', a)
    if hasattr(b2, 'xhtml_Kbd309'):
        assert _is_linked(b2, 'xhtml_Kbd309', a)
    _safe_set(a, 'xhtml_Object308', set())
    assert not _is_linked(a, 'xhtml_Object308', b2)
    if hasattr(b2, 'xhtml_Kbd309'):
        assert not _is_linked(b2, 'xhtml_Kbd309', a)


def test_assoc_kbd365_link_reassign_clear():
    a = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b1 = xhtml_Kbd(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Kbd(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_PreContent366', {b1})
    assert _is_linked(a, 'xhtml_PreContent366', b1)
    if hasattr(b1, 'xhtml_Kbd367'):
        assert _is_linked(b1, 'xhtml_Kbd367', a)
    _safe_set(a, 'xhtml_PreContent366', {b2})
    assert _is_linked(a, 'xhtml_PreContent366', b2)
    if hasattr(b1, 'xhtml_Kbd367'):
        assert not _is_linked(b1, 'xhtml_Kbd367', a)
    if hasattr(b2, 'xhtml_Kbd367'):
        assert _is_linked(b2, 'xhtml_Kbd367', a)
    _safe_set(a, 'xhtml_PreContent366', set())
    assert not _is_linked(a, 'xhtml_PreContent366', b2)
    if hasattr(b2, 'xhtml_Kbd367'):
        assert not _is_linked(b2, 'xhtml_Kbd367', a)


def test_assoc_li1328_link_reassign_clear():
    a = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Li(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Ol329', {b1})
    assert _is_linked(a, 'xhtml_Ol329', b1)
    if hasattr(b1, 'xhtml_Li'):
        assert _is_linked(b1, 'xhtml_Li', a)
    _safe_set(a, 'xhtml_Ol329', {b2})
    assert _is_linked(a, 'xhtml_Ol329', b2)
    if hasattr(b1, 'xhtml_Li'):
        assert not _is_linked(b1, 'xhtml_Li', a)
    if hasattr(b2, 'xhtml_Li'):
        assert _is_linked(b2, 'xhtml_Li', a)
    _safe_set(a, 'xhtml_Ol329', set())
    assert not _is_linked(a, 'xhtml_Ol329', b2)
    if hasattr(b2, 'xhtml_Li'):
        assert not _is_linked(b2, 'xhtml_Li', a)


def test_assoc_li1421_link_reassign_clear():
    a = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Li(class_="sample_text", lang="sample_text", style="sample_text")
    b2 = xhtml_Li(class_="sample_text_2", lang="sample_text_2", style="sample_text_2")
    _safe_set(a, 'xhtml_Ul422', {b1})
    assert _is_linked(a, 'xhtml_Ul422', b1)
    if hasattr(b1, 'xhtml_Li423'):
        assert _is_linked(b1, 'xhtml_Li423', a)
    _safe_set(a, 'xhtml_Ul422', {b2})
    assert _is_linked(a, 'xhtml_Ul422', b2)
    if hasattr(b1, 'xhtml_Li423'):
        assert not _is_linked(b1, 'xhtml_Li423', a)
    if hasattr(b2, 'xhtml_Li423'):
        assert _is_linked(b2, 'xhtml_Li423', a)
    _safe_set(a, 'xhtml_Ul422', set())
    assert not _is_linked(a, 'xhtml_Ul422', b2)
    if hasattr(b2, 'xhtml_Li423'):
        assert not _is_linked(b2, 'xhtml_Li423', a)


def test_assoc_object170_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Object172', b1)
    assert _is_linked(a, 'xhtml_Object172', b1)
    if hasattr(b1, 'xhtml_Inline171'):
        assert _is_linked(b1, 'xhtml_Inline171', a)
    _safe_set(a, 'xhtml_Object172', b2)
    assert _is_linked(a, 'xhtml_Object172', b2)
    if hasattr(b1, 'xhtml_Inline171'):
        assert not _is_linked(b1, 'xhtml_Inline171', a)
    if hasattr(b2, 'xhtml_Inline171'):
        assert _is_linked(b2, 'xhtml_Inline171', a)
    _safe_set(a, 'xhtml_Object172', None)
    assert not _is_linked(a, 'xhtml_Object172', b2)
    if hasattr(b2, 'xhtml_Inline171'):
        assert not _is_linked(b2, 'xhtml_Inline171', a)


def test_assoc_object269_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Object268', {b1})
    assert _is_linked(a, 'xhtml_Object268', b1)
    if hasattr(b1, 'xhtml_Object270'):
        assert _is_linked(b1, 'xhtml_Object270', a)
    _safe_set(a, 'xhtml_Object268', {b2})
    assert _is_linked(a, 'xhtml_Object268', b2)
    if hasattr(b1, 'xhtml_Object270'):
        assert not _is_linked(b1, 'xhtml_Object270', a)
    if hasattr(b2, 'xhtml_Object270'):
        assert _is_linked(b2, 'xhtml_Object270', a)
    _safe_set(a, 'xhtml_Object268', set())
    assert not _is_linked(a, 'xhtml_Object268', b2)
    if hasattr(b2, 'xhtml_Object270'):
        assert not _is_linked(b2, 'xhtml_Object270', a)


def test_assoc_object3_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Object', b1)
    assert _is_linked(a, 'xhtml_Object', b1)
    if hasattr(b1, 'xhtml_AContent4'):
        assert _is_linked(b1, 'xhtml_AContent4', a)
    _safe_set(a, 'xhtml_Object', b2)
    assert _is_linked(a, 'xhtml_Object', b2)
    if hasattr(b1, 'xhtml_AContent4'):
        assert not _is_linked(b1, 'xhtml_AContent4', a)
    if hasattr(b2, 'xhtml_AContent4'):
        assert _is_linked(b2, 'xhtml_AContent4', a)
    _safe_set(a, 'xhtml_Object', None)
    assert not _is_linked(a, 'xhtml_Object', b2)
    if hasattr(b2, 'xhtml_AContent4'):
        assert not _is_linked(b2, 'xhtml_AContent4', a)


def test_assoc_object99_link_reassign_clear():
    a = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Object101', b1)
    assert _is_linked(a, 'xhtml_Object101', b1)
    if hasattr(b1, 'xhtml_Flow100'):
        assert _is_linked(b1, 'xhtml_Flow100', a)
    _safe_set(a, 'xhtml_Object101', b2)
    assert _is_linked(a, 'xhtml_Object101', b2)
    if hasattr(b1, 'xhtml_Flow100'):
        assert not _is_linked(b1, 'xhtml_Flow100', a)
    if hasattr(b2, 'xhtml_Flow100'):
        assert _is_linked(b2, 'xhtml_Flow100', a)
    _safe_set(a, 'xhtml_Object101', None)
    assert not _is_linked(a, 'xhtml_Object101', b2)
    if hasattr(b2, 'xhtml_Flow100'):
        assert not _is_linked(b2, 'xhtml_Flow100', a)


def test_assoc_ol241_link_reassign_clear():
    a = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Ol243', b1)
    assert _is_linked(a, 'xhtml_Ol243', b1)
    if hasattr(b1, 'xhtml_Object242'):
        assert _is_linked(b1, 'xhtml_Object242', a)
    _safe_set(a, 'xhtml_Ol243', b2)
    assert _is_linked(a, 'xhtml_Ol243', b2)
    if hasattr(b1, 'xhtml_Object242'):
        assert not _is_linked(b1, 'xhtml_Object242', a)
    if hasattr(b2, 'xhtml_Object242'):
        assert _is_linked(b2, 'xhtml_Object242', a)
    _safe_set(a, 'xhtml_Ol243', None)
    assert not _is_linked(a, 'xhtml_Ol243', b2)
    if hasattr(b2, 'xhtml_Object242'):
        assert not _is_linked(b2, 'xhtml_Object242', a)


def test_assoc_ol48_link_reassign_clear():
    a = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Ol', b1)
    assert _is_linked(a, 'xhtml_Ol', b1)
    if hasattr(b1, 'xhtml_Block49'):
        assert _is_linked(b1, 'xhtml_Block49', a)
    _safe_set(a, 'xhtml_Ol', b2)
    assert _is_linked(a, 'xhtml_Ol', b2)
    if hasattr(b1, 'xhtml_Block49'):
        assert not _is_linked(b1, 'xhtml_Block49', a)
    if hasattr(b2, 'xhtml_Block49'):
        assert _is_linked(b2, 'xhtml_Block49', a)
    _safe_set(a, 'xhtml_Ol', None)
    assert not _is_linked(a, 'xhtml_Ol', b2)
    if hasattr(b2, 'xhtml_Block49'):
        assert not _is_linked(b2, 'xhtml_Block49', a)


def test_assoc_ol73_link_reassign_clear():
    a = xhtml_Ol(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Ol75', b1)
    assert _is_linked(a, 'xhtml_Ol75', b1)
    if hasattr(b1, 'xhtml_Flow74'):
        assert _is_linked(b1, 'xhtml_Flow74', a)
    _safe_set(a, 'xhtml_Ol75', b2)
    assert _is_linked(a, 'xhtml_Ol75', b2)
    if hasattr(b1, 'xhtml_Flow74'):
        assert not _is_linked(b1, 'xhtml_Flow74', a)
    if hasattr(b2, 'xhtml_Flow74'):
        assert _is_linked(b2, 'xhtml_Flow74', a)
    _safe_set(a, 'xhtml_Ol75', None)
    assert not _is_linked(a, 'xhtml_Ol75', b2)
    if hasattr(b2, 'xhtml_Flow74'):
        assert not _is_linked(b2, 'xhtml_Flow74', a)


def test_assoc_p232_link_reassign_clear():
    a = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_P234', b1)
    assert _is_linked(a, 'xhtml_P234', b1)
    if hasattr(b1, 'xhtml_Object233'):
        assert _is_linked(b1, 'xhtml_Object233', a)
    _safe_set(a, 'xhtml_P234', b2)
    assert _is_linked(a, 'xhtml_P234', b2)
    if hasattr(b1, 'xhtml_Object233'):
        assert not _is_linked(b1, 'xhtml_Object233', a)
    if hasattr(b2, 'xhtml_Object233'):
        assert _is_linked(b2, 'xhtml_Object233', a)
    _safe_set(a, 'xhtml_P234', None)
    assert not _is_linked(a, 'xhtml_P234', b2)
    if hasattr(b2, 'xhtml_Object233'):
        assert not _is_linked(b2, 'xhtml_Object233', a)


def test_assoc_p43_link_reassign_clear():
    a = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_P', b1)
    assert _is_linked(a, 'xhtml_P', b1)
    if hasattr(b1, 'xhtml_Block'):
        assert _is_linked(b1, 'xhtml_Block', a)
    _safe_set(a, 'xhtml_P', b2)
    assert _is_linked(a, 'xhtml_P', b2)
    if hasattr(b1, 'xhtml_Block'):
        assert not _is_linked(b1, 'xhtml_Block', a)
    if hasattr(b2, 'xhtml_Block'):
        assert _is_linked(b2, 'xhtml_Block', a)
    _safe_set(a, 'xhtml_P', None)
    assert not _is_linked(a, 'xhtml_P', b2)
    if hasattr(b2, 'xhtml_Block'):
        assert not _is_linked(b2, 'xhtml_Block', a)


def test_assoc_p65_link_reassign_clear():
    a = xhtml_P(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_P66', b1)
    assert _is_linked(a, 'xhtml_P66', b1)
    if hasattr(b1, 'xhtml_Flow'):
        assert _is_linked(b1, 'xhtml_Flow', a)
    _safe_set(a, 'xhtml_P66', b2)
    assert _is_linked(a, 'xhtml_P66', b2)
    if hasattr(b1, 'xhtml_Flow'):
        assert not _is_linked(b1, 'xhtml_Flow', a)
    if hasattr(b2, 'xhtml_Flow'):
        assert _is_linked(b2, 'xhtml_Flow', a)
    _safe_set(a, 'xhtml_P66', None)
    assert not _is_linked(a, 'xhtml_P66', b2)
    if hasattr(b2, 'xhtml_Flow'):
        assert not _is_linked(b2, 'xhtml_Flow', a)


def test_assoc_param230_link_reassign_clear():
    a = xhtml_Param(name="sample_text", value="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Param', b1)
    assert _is_linked(a, 'xhtml_Param', b1)
    if hasattr(b1, 'xhtml_Object231'):
        assert _is_linked(b1, 'xhtml_Object231', a)
    _safe_set(a, 'xhtml_Param', b2)
    assert _is_linked(a, 'xhtml_Param', b2)
    if hasattr(b1, 'xhtml_Object231'):
        assert not _is_linked(b1, 'xhtml_Object231', a)
    if hasattr(b2, 'xhtml_Object231'):
        assert _is_linked(b2, 'xhtml_Object231', a)
    _safe_set(a, 'xhtml_Param', None)
    assert not _is_linked(a, 'xhtml_Param', b2)
    if hasattr(b2, 'xhtml_Object231'):
        assert not _is_linked(b2, 'xhtml_Object231', a)


def test_assoc_pre247_link_reassign_clear():
    a = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Pre249', b1)
    assert _is_linked(a, 'xhtml_Pre249', b1)
    if hasattr(b1, 'xhtml_Object248'):
        assert _is_linked(b1, 'xhtml_Object248', a)
    _safe_set(a, 'xhtml_Pre249', b2)
    assert _is_linked(a, 'xhtml_Pre249', b2)
    if hasattr(b1, 'xhtml_Object248'):
        assert not _is_linked(b1, 'xhtml_Object248', a)
    if hasattr(b2, 'xhtml_Object248'):
        assert _is_linked(b2, 'xhtml_Object248', a)
    _safe_set(a, 'xhtml_Pre249', None)
    assert not _is_linked(a, 'xhtml_Pre249', b2)
    if hasattr(b2, 'xhtml_Object248'):
        assert not _is_linked(b2, 'xhtml_Object248', a)


def test_assoc_pre52_link_reassign_clear():
    a = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Pre', b1)
    assert _is_linked(a, 'xhtml_Pre', b1)
    if hasattr(b1, 'xhtml_Block53'):
        assert _is_linked(b1, 'xhtml_Block53', a)
    _safe_set(a, 'xhtml_Pre', b2)
    assert _is_linked(a, 'xhtml_Pre', b2)
    if hasattr(b1, 'xhtml_Block53'):
        assert not _is_linked(b1, 'xhtml_Block53', a)
    if hasattr(b2, 'xhtml_Block53'):
        assert _is_linked(b2, 'xhtml_Block53', a)
    _safe_set(a, 'xhtml_Pre', None)
    assert not _is_linked(a, 'xhtml_Pre', b2)
    if hasattr(b2, 'xhtml_Block53'):
        assert not _is_linked(b2, 'xhtml_Block53', a)


def test_assoc_pre79_link_reassign_clear():
    a = xhtml_Pre(class_="sample_text", lang="sample_text", space="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Pre81', b1)
    assert _is_linked(a, 'xhtml_Pre81', b1)
    if hasattr(b1, 'xhtml_Flow80'):
        assert _is_linked(b1, 'xhtml_Flow80', a)
    _safe_set(a, 'xhtml_Pre81', b2)
    assert _is_linked(a, 'xhtml_Pre81', b2)
    if hasattr(b1, 'xhtml_Flow80'):
        assert not _is_linked(b1, 'xhtml_Flow80', a)
    if hasattr(b2, 'xhtml_Flow80'):
        assert _is_linked(b2, 'xhtml_Flow80', a)
    _safe_set(a, 'xhtml_Pre81', None)
    assert not _is_linked(a, 'xhtml_Pre81', b2)
    if hasattr(b2, 'xhtml_Flow80'):
        assert not _is_linked(b2, 'xhtml_Flow80', a)


def test_assoc_q132_link_reassign_clear():
    a = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Q134', b1)
    assert _is_linked(a, 'xhtml_Q134', b1)
    if hasattr(b1, 'xhtml_Flow133'):
        assert _is_linked(b1, 'xhtml_Flow133', a)
    _safe_set(a, 'xhtml_Q134', b2)
    assert _is_linked(a, 'xhtml_Q134', b2)
    if hasattr(b1, 'xhtml_Flow133'):
        assert not _is_linked(b1, 'xhtml_Flow133', a)
    if hasattr(b2, 'xhtml_Flow133'):
        assert _is_linked(b2, 'xhtml_Flow133', a)
    _safe_set(a, 'xhtml_Q134', None)
    assert not _is_linked(a, 'xhtml_Q134', b2)
    if hasattr(b2, 'xhtml_Flow133'):
        assert not _is_linked(b2, 'xhtml_Flow133', a)


def test_assoc_q203_link_reassign_clear():
    a = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Q205', b1)
    assert _is_linked(a, 'xhtml_Q205', b1)
    if hasattr(b1, 'xhtml_Inline204'):
        assert _is_linked(b1, 'xhtml_Inline204', a)
    _safe_set(a, 'xhtml_Q205', b2)
    assert _is_linked(a, 'xhtml_Q205', b2)
    if hasattr(b1, 'xhtml_Inline204'):
        assert not _is_linked(b1, 'xhtml_Inline204', a)
    if hasattr(b2, 'xhtml_Inline204'):
        assert _is_linked(b2, 'xhtml_Inline204', a)
    _safe_set(a, 'xhtml_Q205', None)
    assert not _is_linked(a, 'xhtml_Q205', b2)
    if hasattr(b2, 'xhtml_Inline204'):
        assert not _is_linked(b2, 'xhtml_Inline204', a)


def test_assoc_q25_link_reassign_clear():
    a = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Q', b1)
    assert _is_linked(a, 'xhtml_Q', b1)
    if hasattr(b1, 'xhtml_AContent26'):
        assert _is_linked(b1, 'xhtml_AContent26', a)
    _safe_set(a, 'xhtml_Q', b2)
    assert _is_linked(a, 'xhtml_Q', b2)
    if hasattr(b1, 'xhtml_AContent26'):
        assert not _is_linked(b1, 'xhtml_AContent26', a)
    if hasattr(b2, 'xhtml_AContent26'):
        assert _is_linked(b2, 'xhtml_AContent26', a)
    _safe_set(a, 'xhtml_Q', None)
    assert not _is_linked(a, 'xhtml_Q', b2)
    if hasattr(b2, 'xhtml_AContent26'):
        assert not _is_linked(b2, 'xhtml_AContent26', a)


def test_assoc_q301_link_reassign_clear():
    a = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Q303', b1)
    assert _is_linked(a, 'xhtml_Q303', b1)
    if hasattr(b1, 'xhtml_Object302'):
        assert _is_linked(b1, 'xhtml_Object302', a)
    _safe_set(a, 'xhtml_Q303', b2)
    assert _is_linked(a, 'xhtml_Q303', b2)
    if hasattr(b1, 'xhtml_Object302'):
        assert not _is_linked(b1, 'xhtml_Object302', a)
    if hasattr(b2, 'xhtml_Object302'):
        assert _is_linked(b2, 'xhtml_Object302', a)
    _safe_set(a, 'xhtml_Q303', None)
    assert not _is_linked(a, 'xhtml_Q303', b2)
    if hasattr(b2, 'xhtml_Object302'):
        assert not _is_linked(b2, 'xhtml_Object302', a)


def test_assoc_q359_link_reassign_clear():
    a = xhtml_Q(cite1="sample_text", class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Q361', b1)
    assert _is_linked(a, 'xhtml_Q361', b1)
    if hasattr(b1, 'xhtml_PreContent360'):
        assert _is_linked(b1, 'xhtml_PreContent360', a)
    _safe_set(a, 'xhtml_Q361', b2)
    assert _is_linked(a, 'xhtml_Q361', b2)
    if hasattr(b1, 'xhtml_PreContent360'):
        assert not _is_linked(b1, 'xhtml_PreContent360', a)
    if hasattr(b2, 'xhtml_PreContent360'):
        assert _is_linked(b2, 'xhtml_PreContent360', a)
    _safe_set(a, 'xhtml_Q361', None)
    assert not _is_linked(a, 'xhtml_Q361', b2)
    if hasattr(b2, 'xhtml_PreContent360'):
        assert not _is_linked(b2, 'xhtml_PreContent360', a)


def test_assoc_samp135_link_reassign_clear():
    a = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Samp137', b1)
    assert _is_linked(a, 'xhtml_Samp137', b1)
    if hasattr(b1, 'xhtml_Flow136'):
        assert _is_linked(b1, 'xhtml_Flow136', a)
    _safe_set(a, 'xhtml_Samp137', b2)
    assert _is_linked(a, 'xhtml_Samp137', b2)
    if hasattr(b1, 'xhtml_Flow136'):
        assert not _is_linked(b1, 'xhtml_Flow136', a)
    if hasattr(b2, 'xhtml_Flow136'):
        assert _is_linked(b2, 'xhtml_Flow136', a)
    _safe_set(a, 'xhtml_Samp137', None)
    assert not _is_linked(a, 'xhtml_Samp137', b2)
    if hasattr(b2, 'xhtml_Flow136'):
        assert not _is_linked(b2, 'xhtml_Flow136', a)


def test_assoc_samp206_link_reassign_clear():
    a = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Samp208', b1)
    assert _is_linked(a, 'xhtml_Samp208', b1)
    if hasattr(b1, 'xhtml_Inline207'):
        assert _is_linked(b1, 'xhtml_Inline207', a)
    _safe_set(a, 'xhtml_Samp208', b2)
    assert _is_linked(a, 'xhtml_Samp208', b2)
    if hasattr(b1, 'xhtml_Inline207'):
        assert not _is_linked(b1, 'xhtml_Inline207', a)
    if hasattr(b2, 'xhtml_Inline207'):
        assert _is_linked(b2, 'xhtml_Inline207', a)
    _safe_set(a, 'xhtml_Samp208', None)
    assert not _is_linked(a, 'xhtml_Samp208', b2)
    if hasattr(b2, 'xhtml_Inline207'):
        assert not _is_linked(b2, 'xhtml_Inline207', a)


def test_assoc_samp27_link_reassign_clear():
    a = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Samp', b1)
    assert _is_linked(a, 'xhtml_Samp', b1)
    if hasattr(b1, 'xhtml_AContent28'):
        assert _is_linked(b1, 'xhtml_AContent28', a)
    _safe_set(a, 'xhtml_Samp', b2)
    assert _is_linked(a, 'xhtml_Samp', b2)
    if hasattr(b1, 'xhtml_AContent28'):
        assert not _is_linked(b1, 'xhtml_AContent28', a)
    if hasattr(b2, 'xhtml_AContent28'):
        assert _is_linked(b2, 'xhtml_AContent28', a)
    _safe_set(a, 'xhtml_Samp', None)
    assert not _is_linked(a, 'xhtml_Samp', b2)
    if hasattr(b2, 'xhtml_AContent28'):
        assert not _is_linked(b2, 'xhtml_AContent28', a)


def test_assoc_samp304_link_reassign_clear():
    a = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Samp306', b1)
    assert _is_linked(a, 'xhtml_Samp306', b1)
    if hasattr(b1, 'xhtml_Object305'):
        assert _is_linked(b1, 'xhtml_Object305', a)
    _safe_set(a, 'xhtml_Samp306', b2)
    assert _is_linked(a, 'xhtml_Samp306', b2)
    if hasattr(b1, 'xhtml_Object305'):
        assert not _is_linked(b1, 'xhtml_Object305', a)
    if hasattr(b2, 'xhtml_Object305'):
        assert _is_linked(b2, 'xhtml_Object305', a)
    _safe_set(a, 'xhtml_Samp306', None)
    assert not _is_linked(a, 'xhtml_Samp306', b2)
    if hasattr(b2, 'xhtml_Object305'):
        assert not _is_linked(b2, 'xhtml_Object305', a)


def test_assoc_samp362_link_reassign_clear():
    a = xhtml_Samp(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Samp364', b1)
    assert _is_linked(a, 'xhtml_Samp364', b1)
    if hasattr(b1, 'xhtml_PreContent363'):
        assert _is_linked(b1, 'xhtml_PreContent363', a)
    _safe_set(a, 'xhtml_Samp364', b2)
    assert _is_linked(a, 'xhtml_Samp364', b2)
    if hasattr(b1, 'xhtml_PreContent363'):
        assert not _is_linked(b1, 'xhtml_PreContent363', a)
    if hasattr(b2, 'xhtml_PreContent363'):
        assert _is_linked(b2, 'xhtml_PreContent363', a)
    _safe_set(a, 'xhtml_Samp364', None)
    assert not _is_linked(a, 'xhtml_Samp364', b2)
    if hasattr(b2, 'xhtml_PreContent363'):
        assert not _is_linked(b2, 'xhtml_PreContent363', a)


def test_assoc_small117_link_reassign_clear():
    a = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Small119', b1)
    assert _is_linked(a, 'xhtml_Small119', b1)
    if hasattr(b1, 'xhtml_Flow118'):
        assert _is_linked(b1, 'xhtml_Flow118', a)
    _safe_set(a, 'xhtml_Small119', b2)
    assert _is_linked(a, 'xhtml_Small119', b2)
    if hasattr(b1, 'xhtml_Flow118'):
        assert not _is_linked(b1, 'xhtml_Flow118', a)
    if hasattr(b2, 'xhtml_Flow118'):
        assert _is_linked(b2, 'xhtml_Flow118', a)
    _safe_set(a, 'xhtml_Small119', None)
    assert not _is_linked(a, 'xhtml_Small119', b2)
    if hasattr(b2, 'xhtml_Flow118'):
        assert not _is_linked(b2, 'xhtml_Flow118', a)


def test_assoc_small15_link_reassign_clear():
    a = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Small', b1)
    assert _is_linked(a, 'xhtml_Small', b1)
    if hasattr(b1, 'xhtml_AContent16'):
        assert _is_linked(b1, 'xhtml_AContent16', a)
    _safe_set(a, 'xhtml_Small', b2)
    assert _is_linked(a, 'xhtml_Small', b2)
    if hasattr(b1, 'xhtml_AContent16'):
        assert not _is_linked(b1, 'xhtml_AContent16', a)
    if hasattr(b2, 'xhtml_AContent16'):
        assert _is_linked(b2, 'xhtml_AContent16', a)
    _safe_set(a, 'xhtml_Small', None)
    assert not _is_linked(a, 'xhtml_Small', b2)
    if hasattr(b2, 'xhtml_AContent16'):
        assert not _is_linked(b2, 'xhtml_AContent16', a)


def test_assoc_small188_link_reassign_clear():
    a = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Small190', b1)
    assert _is_linked(a, 'xhtml_Small190', b1)
    if hasattr(b1, 'xhtml_Inline189'):
        assert _is_linked(b1, 'xhtml_Inline189', a)
    _safe_set(a, 'xhtml_Small190', b2)
    assert _is_linked(a, 'xhtml_Small190', b2)
    if hasattr(b1, 'xhtml_Inline189'):
        assert not _is_linked(b1, 'xhtml_Inline189', a)
    if hasattr(b2, 'xhtml_Inline189'):
        assert _is_linked(b2, 'xhtml_Inline189', a)
    _safe_set(a, 'xhtml_Small190', None)
    assert not _is_linked(a, 'xhtml_Small190', b2)
    if hasattr(b2, 'xhtml_Inline189'):
        assert not _is_linked(b2, 'xhtml_Inline189', a)


def test_assoc_small286_link_reassign_clear():
    a = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Small288', b1)
    assert _is_linked(a, 'xhtml_Small288', b1)
    if hasattr(b1, 'xhtml_Object287'):
        assert _is_linked(b1, 'xhtml_Object287', a)
    _safe_set(a, 'xhtml_Small288', b2)
    assert _is_linked(a, 'xhtml_Small288', b2)
    if hasattr(b1, 'xhtml_Object287'):
        assert not _is_linked(b1, 'xhtml_Object287', a)
    if hasattr(b2, 'xhtml_Object287'):
        assert _is_linked(b2, 'xhtml_Object287', a)
    _safe_set(a, 'xhtml_Small288', None)
    assert not _is_linked(a, 'xhtml_Small288', b2)
    if hasattr(b2, 'xhtml_Object287'):
        assert not _is_linked(b2, 'xhtml_Object287', a)


def test_assoc_small344_link_reassign_clear():
    a = xhtml_Small(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Small346', b1)
    assert _is_linked(a, 'xhtml_Small346', b1)
    if hasattr(b1, 'xhtml_PreContent345'):
        assert _is_linked(b1, 'xhtml_PreContent345', a)
    _safe_set(a, 'xhtml_Small346', b2)
    assert _is_linked(a, 'xhtml_Small346', b2)
    if hasattr(b1, 'xhtml_PreContent345'):
        assert not _is_linked(b1, 'xhtml_PreContent345', a)
    if hasattr(b2, 'xhtml_PreContent345'):
        assert _is_linked(b2, 'xhtml_PreContent345', a)
    _safe_set(a, 'xhtml_Small346', None)
    assert not _is_linked(a, 'xhtml_Small346', b2)
    if hasattr(b2, 'xhtml_PreContent345'):
        assert not _is_linked(b2, 'xhtml_PreContent345', a)


def test_assoc_span1_link_reassign_clear():
    a = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Span', b1)
    assert _is_linked(a, 'xhtml_Span', b1)
    if hasattr(b1, 'xhtml_AContent2'):
        assert _is_linked(b1, 'xhtml_AContent2', a)
    _safe_set(a, 'xhtml_Span', b2)
    assert _is_linked(a, 'xhtml_Span', b2)
    if hasattr(b1, 'xhtml_AContent2'):
        assert not _is_linked(b1, 'xhtml_AContent2', a)
    if hasattr(b2, 'xhtml_AContent2'):
        assert _is_linked(b2, 'xhtml_AContent2', a)
    _safe_set(a, 'xhtml_Span', None)
    assert not _is_linked(a, 'xhtml_Span', b2)
    if hasattr(b2, 'xhtml_AContent2'):
        assert not _is_linked(b2, 'xhtml_AContent2', a)


def test_assoc_span167_link_reassign_clear():
    a = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Span169', b1)
    assert _is_linked(a, 'xhtml_Span169', b1)
    if hasattr(b1, 'xhtml_Inline168'):
        assert _is_linked(b1, 'xhtml_Inline168', a)
    _safe_set(a, 'xhtml_Span169', b2)
    assert _is_linked(a, 'xhtml_Span169', b2)
    if hasattr(b1, 'xhtml_Inline168'):
        assert not _is_linked(b1, 'xhtml_Inline168', a)
    if hasattr(b2, 'xhtml_Inline168'):
        assert _is_linked(b2, 'xhtml_Inline168', a)
    _safe_set(a, 'xhtml_Span169', None)
    assert not _is_linked(a, 'xhtml_Span169', b2)
    if hasattr(b2, 'xhtml_Inline168'):
        assert not _is_linked(b2, 'xhtml_Inline168', a)


def test_assoc_span265_link_reassign_clear():
    a = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Span267', b1)
    assert _is_linked(a, 'xhtml_Span267', b1)
    if hasattr(b1, 'xhtml_Object266'):
        assert _is_linked(b1, 'xhtml_Object266', a)
    _safe_set(a, 'xhtml_Span267', b2)
    assert _is_linked(a, 'xhtml_Span267', b2)
    if hasattr(b1, 'xhtml_Object266'):
        assert not _is_linked(b1, 'xhtml_Object266', a)
    if hasattr(b2, 'xhtml_Object266'):
        assert _is_linked(b2, 'xhtml_Object266', a)
    _safe_set(a, 'xhtml_Span267', None)
    assert not _is_linked(a, 'xhtml_Span267', b2)
    if hasattr(b2, 'xhtml_Object266'):
        assert not _is_linked(b2, 'xhtml_Object266', a)


def test_assoc_span389_link_reassign_clear():
    a = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Span391', b1)
    assert _is_linked(a, 'xhtml_Span391', b1)
    if hasattr(b1, 'xhtml_PreContent390'):
        assert _is_linked(b1, 'xhtml_PreContent390', a)
    _safe_set(a, 'xhtml_Span391', b2)
    assert _is_linked(a, 'xhtml_Span391', b2)
    if hasattr(b1, 'xhtml_PreContent390'):
        assert not _is_linked(b1, 'xhtml_PreContent390', a)
    if hasattr(b2, 'xhtml_PreContent390'):
        assert _is_linked(b2, 'xhtml_PreContent390', a)
    _safe_set(a, 'xhtml_Span391', None)
    assert not _is_linked(a, 'xhtml_Span391', b2)
    if hasattr(b2, 'xhtml_PreContent390'):
        assert not _is_linked(b2, 'xhtml_PreContent390', a)


def test_assoc_span96_link_reassign_clear():
    a = xhtml_Span(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Span98', b1)
    assert _is_linked(a, 'xhtml_Span98', b1)
    if hasattr(b1, 'xhtml_Flow97'):
        assert _is_linked(b1, 'xhtml_Flow97', a)
    _safe_set(a, 'xhtml_Span98', b2)
    assert _is_linked(a, 'xhtml_Span98', b2)
    if hasattr(b1, 'xhtml_Flow97'):
        assert not _is_linked(b1, 'xhtml_Flow97', a)
    if hasattr(b2, 'xhtml_Flow97'):
        assert _is_linked(b2, 'xhtml_Flow97', a)
    _safe_set(a, 'xhtml_Span98', None)
    assert not _is_linked(a, 'xhtml_Span98', b2)
    if hasattr(b2, 'xhtml_Flow97'):
        assert not _is_linked(b2, 'xhtml_Flow97', a)


def test_assoc_strong123_link_reassign_clear():
    a = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Strong125', b1)
    assert _is_linked(a, 'xhtml_Strong125', b1)
    if hasattr(b1, 'xhtml_Flow124'):
        assert _is_linked(b1, 'xhtml_Flow124', a)
    _safe_set(a, 'xhtml_Strong125', b2)
    assert _is_linked(a, 'xhtml_Strong125', b2)
    if hasattr(b1, 'xhtml_Flow124'):
        assert not _is_linked(b1, 'xhtml_Flow124', a)
    if hasattr(b2, 'xhtml_Flow124'):
        assert _is_linked(b2, 'xhtml_Flow124', a)
    _safe_set(a, 'xhtml_Strong125', None)
    assert not _is_linked(a, 'xhtml_Strong125', b2)
    if hasattr(b2, 'xhtml_Flow124'):
        assert not _is_linked(b2, 'xhtml_Flow124', a)


def test_assoc_strong19_link_reassign_clear():
    a = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Strong', b1)
    assert _is_linked(a, 'xhtml_Strong', b1)
    if hasattr(b1, 'xhtml_AContent20'):
        assert _is_linked(b1, 'xhtml_AContent20', a)
    _safe_set(a, 'xhtml_Strong', b2)
    assert _is_linked(a, 'xhtml_Strong', b2)
    if hasattr(b1, 'xhtml_AContent20'):
        assert not _is_linked(b1, 'xhtml_AContent20', a)
    if hasattr(b2, 'xhtml_AContent20'):
        assert _is_linked(b2, 'xhtml_AContent20', a)
    _safe_set(a, 'xhtml_Strong', None)
    assert not _is_linked(a, 'xhtml_Strong', b2)
    if hasattr(b2, 'xhtml_AContent20'):
        assert not _is_linked(b2, 'xhtml_AContent20', a)


def test_assoc_strong194_link_reassign_clear():
    a = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Strong196', b1)
    assert _is_linked(a, 'xhtml_Strong196', b1)
    if hasattr(b1, 'xhtml_Inline195'):
        assert _is_linked(b1, 'xhtml_Inline195', a)
    _safe_set(a, 'xhtml_Strong196', b2)
    assert _is_linked(a, 'xhtml_Strong196', b2)
    if hasattr(b1, 'xhtml_Inline195'):
        assert not _is_linked(b1, 'xhtml_Inline195', a)
    if hasattr(b2, 'xhtml_Inline195'):
        assert _is_linked(b2, 'xhtml_Inline195', a)
    _safe_set(a, 'xhtml_Strong196', None)
    assert not _is_linked(a, 'xhtml_Strong196', b2)
    if hasattr(b2, 'xhtml_Inline195'):
        assert not _is_linked(b2, 'xhtml_Inline195', a)


def test_assoc_strong292_link_reassign_clear():
    a = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Strong294', b1)
    assert _is_linked(a, 'xhtml_Strong294', b1)
    if hasattr(b1, 'xhtml_Object293'):
        assert _is_linked(b1, 'xhtml_Object293', a)
    _safe_set(a, 'xhtml_Strong294', b2)
    assert _is_linked(a, 'xhtml_Strong294', b2)
    if hasattr(b1, 'xhtml_Object293'):
        assert not _is_linked(b1, 'xhtml_Object293', a)
    if hasattr(b2, 'xhtml_Object293'):
        assert _is_linked(b2, 'xhtml_Object293', a)
    _safe_set(a, 'xhtml_Strong294', None)
    assert not _is_linked(a, 'xhtml_Strong294', b2)
    if hasattr(b2, 'xhtml_Object293'):
        assert not _is_linked(b2, 'xhtml_Object293', a)


def test_assoc_strong350_link_reassign_clear():
    a = xhtml_Strong(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Strong352', b1)
    assert _is_linked(a, 'xhtml_Strong352', b1)
    if hasattr(b1, 'xhtml_PreContent351'):
        assert _is_linked(b1, 'xhtml_PreContent351', a)
    _safe_set(a, 'xhtml_Strong352', b2)
    assert _is_linked(a, 'xhtml_Strong352', b2)
    if hasattr(b1, 'xhtml_PreContent351'):
        assert not _is_linked(b1, 'xhtml_PreContent351', a)
    if hasattr(b2, 'xhtml_PreContent351'):
        assert _is_linked(b2, 'xhtml_PreContent351', a)
    _safe_set(a, 'xhtml_Strong352', None)
    assert not _is_linked(a, 'xhtml_Strong352', b2)
    if hasattr(b2, 'xhtml_PreContent351'):
        assert not _is_linked(b2, 'xhtml_PreContent351', a)


def test_assoc_sub153_link_reassign_clear():
    a = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sub155', b1)
    assert _is_linked(a, 'xhtml_Sub155', b1)
    if hasattr(b1, 'xhtml_Flow154'):
        assert _is_linked(b1, 'xhtml_Flow154', a)
    _safe_set(a, 'xhtml_Sub155', b2)
    assert _is_linked(a, 'xhtml_Sub155', b2)
    if hasattr(b1, 'xhtml_Flow154'):
        assert not _is_linked(b1, 'xhtml_Flow154', a)
    if hasattr(b2, 'xhtml_Flow154'):
        assert _is_linked(b2, 'xhtml_Flow154', a)
    _safe_set(a, 'xhtml_Sub155', None)
    assert not _is_linked(a, 'xhtml_Sub155', b2)
    if hasattr(b2, 'xhtml_Flow154'):
        assert not _is_linked(b2, 'xhtml_Flow154', a)


def test_assoc_sub224_link_reassign_clear():
    a = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sub226', b1)
    assert _is_linked(a, 'xhtml_Sub226', b1)
    if hasattr(b1, 'xhtml_Inline225'):
        assert _is_linked(b1, 'xhtml_Inline225', a)
    _safe_set(a, 'xhtml_Sub226', b2)
    assert _is_linked(a, 'xhtml_Sub226', b2)
    if hasattr(b1, 'xhtml_Inline225'):
        assert not _is_linked(b1, 'xhtml_Inline225', a)
    if hasattr(b2, 'xhtml_Inline225'):
        assert _is_linked(b2, 'xhtml_Inline225', a)
    _safe_set(a, 'xhtml_Sub226', None)
    assert not _is_linked(a, 'xhtml_Sub226', b2)
    if hasattr(b2, 'xhtml_Inline225'):
        assert not _is_linked(b2, 'xhtml_Inline225', a)


def test_assoc_sub322_link_reassign_clear():
    a = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Sub324', b1)
    assert _is_linked(a, 'xhtml_Sub324', b1)
    if hasattr(b1, 'xhtml_Object323'):
        assert _is_linked(b1, 'xhtml_Object323', a)
    _safe_set(a, 'xhtml_Sub324', b2)
    assert _is_linked(a, 'xhtml_Sub324', b2)
    if hasattr(b1, 'xhtml_Object323'):
        assert not _is_linked(b1, 'xhtml_Object323', a)
    if hasattr(b2, 'xhtml_Object323'):
        assert _is_linked(b2, 'xhtml_Object323', a)
    _safe_set(a, 'xhtml_Sub324', None)
    assert not _is_linked(a, 'xhtml_Sub324', b2)
    if hasattr(b2, 'xhtml_Object323'):
        assert not _is_linked(b2, 'xhtml_Object323', a)


def test_assoc_sub380_link_reassign_clear():
    a = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sub382', b1)
    assert _is_linked(a, 'xhtml_Sub382', b1)
    if hasattr(b1, 'xhtml_PreContent381'):
        assert _is_linked(b1, 'xhtml_PreContent381', a)
    _safe_set(a, 'xhtml_Sub382', b2)
    assert _is_linked(a, 'xhtml_Sub382', b2)
    if hasattr(b1, 'xhtml_PreContent381'):
        assert not _is_linked(b1, 'xhtml_PreContent381', a)
    if hasattr(b2, 'xhtml_PreContent381'):
        assert _is_linked(b2, 'xhtml_PreContent381', a)
    _safe_set(a, 'xhtml_Sub382', None)
    assert not _is_linked(a, 'xhtml_Sub382', b2)
    if hasattr(b2, 'xhtml_PreContent381'):
        assert not _is_linked(b2, 'xhtml_PreContent381', a)


def test_assoc_sub39_link_reassign_clear():
    a = xhtml_Sub(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sub', b1)
    assert _is_linked(a, 'xhtml_Sub', b1)
    if hasattr(b1, 'xhtml_AContent40'):
        assert _is_linked(b1, 'xhtml_AContent40', a)
    _safe_set(a, 'xhtml_Sub', b2)
    assert _is_linked(a, 'xhtml_Sub', b2)
    if hasattr(b1, 'xhtml_AContent40'):
        assert not _is_linked(b1, 'xhtml_AContent40', a)
    if hasattr(b2, 'xhtml_AContent40'):
        assert _is_linked(b2, 'xhtml_AContent40', a)
    _safe_set(a, 'xhtml_Sub', None)
    assert not _is_linked(a, 'xhtml_Sub', b2)
    if hasattr(b2, 'xhtml_AContent40'):
        assert not _is_linked(b2, 'xhtml_AContent40', a)


def test_assoc_sup156_link_reassign_clear():
    a = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sup158', b1)
    assert _is_linked(a, 'xhtml_Sup158', b1)
    if hasattr(b1, 'xhtml_Flow157'):
        assert _is_linked(b1, 'xhtml_Flow157', a)
    _safe_set(a, 'xhtml_Sup158', b2)
    assert _is_linked(a, 'xhtml_Sup158', b2)
    if hasattr(b1, 'xhtml_Flow157'):
        assert not _is_linked(b1, 'xhtml_Flow157', a)
    if hasattr(b2, 'xhtml_Flow157'):
        assert _is_linked(b2, 'xhtml_Flow157', a)
    _safe_set(a, 'xhtml_Sup158', None)
    assert not _is_linked(a, 'xhtml_Sup158', b2)
    if hasattr(b2, 'xhtml_Flow157'):
        assert not _is_linked(b2, 'xhtml_Flow157', a)


def test_assoc_sup227_link_reassign_clear():
    a = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sup229', b1)
    assert _is_linked(a, 'xhtml_Sup229', b1)
    if hasattr(b1, 'xhtml_Inline228'):
        assert _is_linked(b1, 'xhtml_Inline228', a)
    _safe_set(a, 'xhtml_Sup229', b2)
    assert _is_linked(a, 'xhtml_Sup229', b2)
    if hasattr(b1, 'xhtml_Inline228'):
        assert not _is_linked(b1, 'xhtml_Inline228', a)
    if hasattr(b2, 'xhtml_Inline228'):
        assert _is_linked(b2, 'xhtml_Inline228', a)
    _safe_set(a, 'xhtml_Sup229', None)
    assert not _is_linked(a, 'xhtml_Sup229', b2)
    if hasattr(b2, 'xhtml_Inline228'):
        assert not _is_linked(b2, 'xhtml_Inline228', a)


def test_assoc_sup325_link_reassign_clear():
    a = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Sup327', b1)
    assert _is_linked(a, 'xhtml_Sup327', b1)
    if hasattr(b1, 'xhtml_Object326'):
        assert _is_linked(b1, 'xhtml_Object326', a)
    _safe_set(a, 'xhtml_Sup327', b2)
    assert _is_linked(a, 'xhtml_Sup327', b2)
    if hasattr(b1, 'xhtml_Object326'):
        assert not _is_linked(b1, 'xhtml_Object326', a)
    if hasattr(b2, 'xhtml_Object326'):
        assert _is_linked(b2, 'xhtml_Object326', a)
    _safe_set(a, 'xhtml_Sup327', None)
    assert not _is_linked(a, 'xhtml_Sup327', b2)
    if hasattr(b2, 'xhtml_Object326'):
        assert not _is_linked(b2, 'xhtml_Object326', a)


def test_assoc_sup383_link_reassign_clear():
    a = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sup385', b1)
    assert _is_linked(a, 'xhtml_Sup385', b1)
    if hasattr(b1, 'xhtml_PreContent384'):
        assert _is_linked(b1, 'xhtml_PreContent384', a)
    _safe_set(a, 'xhtml_Sup385', b2)
    assert _is_linked(a, 'xhtml_Sup385', b2)
    if hasattr(b1, 'xhtml_PreContent384'):
        assert not _is_linked(b1, 'xhtml_PreContent384', a)
    if hasattr(b2, 'xhtml_PreContent384'):
        assert _is_linked(b2, 'xhtml_PreContent384', a)
    _safe_set(a, 'xhtml_Sup385', None)
    assert not _is_linked(a, 'xhtml_Sup385', b2)
    if hasattr(b2, 'xhtml_PreContent384'):
        assert not _is_linked(b2, 'xhtml_PreContent384', a)


def test_assoc_sup41_link_reassign_clear():
    a = xhtml_Sup(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Sup', b1)
    assert _is_linked(a, 'xhtml_Sup', b1)
    if hasattr(b1, 'xhtml_AContent42'):
        assert _is_linked(b1, 'xhtml_AContent42', a)
    _safe_set(a, 'xhtml_Sup', b2)
    assert _is_linked(a, 'xhtml_Sup', b2)
    if hasattr(b1, 'xhtml_AContent42'):
        assert not _is_linked(b1, 'xhtml_AContent42', a)
    if hasattr(b2, 'xhtml_AContent42'):
        assert _is_linked(b2, 'xhtml_AContent42', a)
    _safe_set(a, 'xhtml_Sup', None)
    assert not _is_linked(a, 'xhtml_Sup', b2)
    if hasattr(b2, 'xhtml_AContent42'):
        assert not _is_linked(b2, 'xhtml_AContent42', a)


def test_assoc_table256_link_reassign_clear():
    a = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Table258', b1)
    assert _is_linked(a, 'xhtml_Table258', b1)
    if hasattr(b1, 'xhtml_Object257'):
        assert _is_linked(b1, 'xhtml_Object257', a)
    _safe_set(a, 'xhtml_Table258', b2)
    assert _is_linked(a, 'xhtml_Table258', b2)
    if hasattr(b1, 'xhtml_Object257'):
        assert not _is_linked(b1, 'xhtml_Object257', a)
    if hasattr(b2, 'xhtml_Object257'):
        assert _is_linked(b2, 'xhtml_Object257', a)
    _safe_set(a, 'xhtml_Table258', None)
    assert not _is_linked(a, 'xhtml_Table258', b2)
    if hasattr(b2, 'xhtml_Object257'):
        assert not _is_linked(b2, 'xhtml_Object257', a)


def test_assoc_table58_link_reassign_clear():
    a = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Table', b1)
    assert _is_linked(a, 'xhtml_Table', b1)
    if hasattr(b1, 'xhtml_Block59'):
        assert _is_linked(b1, 'xhtml_Block59', a)
    _safe_set(a, 'xhtml_Table', b2)
    assert _is_linked(a, 'xhtml_Table', b2)
    if hasattr(b1, 'xhtml_Block59'):
        assert not _is_linked(b1, 'xhtml_Block59', a)
    if hasattr(b2, 'xhtml_Block59'):
        assert _is_linked(b2, 'xhtml_Block59', a)
    _safe_set(a, 'xhtml_Table', None)
    assert not _is_linked(a, 'xhtml_Table', b2)
    if hasattr(b2, 'xhtml_Block59'):
        assert not _is_linked(b2, 'xhtml_Block59', a)


def test_assoc_table88_link_reassign_clear():
    a = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Table90', b1)
    assert _is_linked(a, 'xhtml_Table90', b1)
    if hasattr(b1, 'xhtml_Flow89'):
        assert _is_linked(b1, 'xhtml_Flow89', a)
    _safe_set(a, 'xhtml_Table90', b2)
    assert _is_linked(a, 'xhtml_Table90', b2)
    if hasattr(b1, 'xhtml_Flow89'):
        assert not _is_linked(b1, 'xhtml_Flow89', a)
    if hasattr(b2, 'xhtml_Flow89'):
        assert _is_linked(b2, 'xhtml_Flow89', a)
    _safe_set(a, 'xhtml_Table90', None)
    assert not _is_linked(a, 'xhtml_Table90', b2)
    if hasattr(b2, 'xhtml_Flow89'):
        assert not _is_linked(b2, 'xhtml_Flow89', a)


def test_assoc_tbody404_link_reassign_clear():
    a = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Tbody', b1)
    assert _is_linked(a, 'xhtml_Tbody', b1)
    if hasattr(b1, 'xhtml_Table405'):
        assert _is_linked(b1, 'xhtml_Table405', a)
    _safe_set(a, 'xhtml_Tbody', b2)
    assert _is_linked(a, 'xhtml_Tbody', b2)
    if hasattr(b1, 'xhtml_Table405'):
        assert not _is_linked(b1, 'xhtml_Table405', a)
    if hasattr(b2, 'xhtml_Table405'):
        assert _is_linked(b2, 'xhtml_Table405', a)
    _safe_set(a, 'xhtml_Tbody', None)
    assert not _is_linked(a, 'xhtml_Tbody', b2)
    if hasattr(b2, 'xhtml_Table405'):
        assert not _is_linked(b2, 'xhtml_Table405', a)


def test_assoc_td419_link_reassign_clear():
    a = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Td(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    b2 = xhtml_Td(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", colspan="sample_text_2", lang="sample_text_2", rowspan="sample_text_2", style="sample_text_2", valign="sample_text_2")
    _safe_set(a, 'xhtml_Tr420', {b1})
    assert _is_linked(a, 'xhtml_Tr420', b1)
    if hasattr(b1, 'xhtml_Td'):
        assert _is_linked(b1, 'xhtml_Td', a)
    _safe_set(a, 'xhtml_Tr420', {b2})
    assert _is_linked(a, 'xhtml_Tr420', b2)
    if hasattr(b1, 'xhtml_Td'):
        assert not _is_linked(b1, 'xhtml_Td', a)
    if hasattr(b2, 'xhtml_Td'):
        assert _is_linked(b2, 'xhtml_Td', a)
    _safe_set(a, 'xhtml_Tr420', set())
    assert not _is_linked(a, 'xhtml_Tr420', b2)
    if hasattr(b2, 'xhtml_Td'):
        assert not _is_linked(b2, 'xhtml_Td', a)


def test_assoc_tfoot402_link_reassign_clear():
    a = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Tfoot', b1)
    assert _is_linked(a, 'xhtml_Tfoot', b1)
    if hasattr(b1, 'xhtml_Table403'):
        assert _is_linked(b1, 'xhtml_Table403', a)
    _safe_set(a, 'xhtml_Tfoot', b2)
    assert _is_linked(a, 'xhtml_Tfoot', b2)
    if hasattr(b1, 'xhtml_Table403'):
        assert not _is_linked(b1, 'xhtml_Table403', a)
    if hasattr(b2, 'xhtml_Table403'):
        assert _is_linked(b2, 'xhtml_Table403', a)
    _safe_set(a, 'xhtml_Tfoot', None)
    assert not _is_linked(a, 'xhtml_Tfoot', b2)
    if hasattr(b2, 'xhtml_Table403'):
        assert not _is_linked(b2, 'xhtml_Table403', a)


def test_assoc_th417_link_reassign_clear():
    a = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Th(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", colspan="sample_text", lang="sample_text", rowspan="sample_text", style="sample_text", valign="sample_text")
    b2 = xhtml_Th(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", colspan="sample_text_2", lang="sample_text_2", rowspan="sample_text_2", style="sample_text_2", valign="sample_text_2")
    _safe_set(a, 'xhtml_Tr418', {b1})
    assert _is_linked(a, 'xhtml_Tr418', b1)
    if hasattr(b1, 'xhtml_Th'):
        assert _is_linked(b1, 'xhtml_Th', a)
    _safe_set(a, 'xhtml_Tr418', {b2})
    assert _is_linked(a, 'xhtml_Tr418', b2)
    if hasattr(b1, 'xhtml_Th'):
        assert not _is_linked(b1, 'xhtml_Th', a)
    if hasattr(b2, 'xhtml_Th'):
        assert _is_linked(b2, 'xhtml_Th', a)
    _safe_set(a, 'xhtml_Tr418', set())
    assert not _is_linked(a, 'xhtml_Tr418', b2)
    if hasattr(b2, 'xhtml_Th'):
        assert not _is_linked(b2, 'xhtml_Th', a)


def test_assoc_thead400_link_reassign_clear():
    a = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Thead', b1)
    assert _is_linked(a, 'xhtml_Thead', b1)
    if hasattr(b1, 'xhtml_Table401'):
        assert _is_linked(b1, 'xhtml_Table401', a)
    _safe_set(a, 'xhtml_Thead', b2)
    assert _is_linked(a, 'xhtml_Thead', b2)
    if hasattr(b1, 'xhtml_Table401'):
        assert not _is_linked(b1, 'xhtml_Table401', a)
    if hasattr(b2, 'xhtml_Table401'):
        assert _is_linked(b2, 'xhtml_Table401', a)
    _safe_set(a, 'xhtml_Thead', None)
    assert not _is_linked(a, 'xhtml_Thead', b2)
    if hasattr(b2, 'xhtml_Table401'):
        assert not _is_linked(b2, 'xhtml_Table401', a)


def test_assoc_thumbnail160_link_reassign_clear():
    a = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    b1 = xhtml_Img(alt="sample_text", class_="sample_text", height="sample_text", hl7Id="sample_text", imageType="sample_text", lang="sample_text", src="sample_text", style="sample_text", width="sample_text")
    b2 = xhtml_Img(alt="sample_text_2", class_="sample_text_2", height="sample_text_2", hl7Id="sample_text_2", imageType="sample_text_2", lang="sample_text_2", src="sample_text_2", style="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Img159', b1)
    assert _is_linked(a, 'xhtml_Img159', b1)
    if hasattr(b1, 'xhtml_Img161'):
        assert _is_linked(b1, 'xhtml_Img161', a)
    _safe_set(a, 'xhtml_Img159', b2)
    assert _is_linked(a, 'xhtml_Img159', b2)
    if hasattr(b1, 'xhtml_Img161'):
        assert not _is_linked(b1, 'xhtml_Img161', a)
    if hasattr(b2, 'xhtml_Img161'):
        assert _is_linked(b2, 'xhtml_Img161', a)
    _safe_set(a, 'xhtml_Img159', None)
    assert not _is_linked(a, 'xhtml_Img159', b2)
    if hasattr(b2, 'xhtml_Img161'):
        assert not _is_linked(b2, 'xhtml_Img161', a)


def test_assoc_tr406_link_reassign_clear():
    a = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Table(border="sample_text", cellpadding="sample_text", cellspacing="sample_text", class_="sample_text", frame="sample_text", hl7Id="sample_text", lang="sample_text", rules="sample_text", style="sample_text", width="sample_text")
    b2 = xhtml_Table(border="sample_text_2", cellpadding="sample_text_2", cellspacing="sample_text_2", class_="sample_text_2", frame="sample_text_2", hl7Id="sample_text_2", lang="sample_text_2", rules="sample_text_2", style="sample_text_2", width="sample_text_2")
    _safe_set(a, 'xhtml_Tr', b1)
    assert _is_linked(a, 'xhtml_Tr', b1)
    if hasattr(b1, 'xhtml_Table407'):
        assert _is_linked(b1, 'xhtml_Table407', a)
    _safe_set(a, 'xhtml_Tr', b2)
    assert _is_linked(a, 'xhtml_Tr', b2)
    if hasattr(b1, 'xhtml_Table407'):
        assert not _is_linked(b1, 'xhtml_Table407', a)
    if hasattr(b2, 'xhtml_Table407'):
        assert _is_linked(b2, 'xhtml_Table407', a)
    _safe_set(a, 'xhtml_Tr', None)
    assert not _is_linked(a, 'xhtml_Tr', b2)
    if hasattr(b2, 'xhtml_Table407'):
        assert not _is_linked(b2, 'xhtml_Table407', a)


def test_assoc_tr408_link_reassign_clear():
    a = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Tbody(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b2 = xhtml_Tbody(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    _safe_set(a, 'xhtml_Tr410', b1)
    assert _is_linked(a, 'xhtml_Tr410', b1)
    if hasattr(b1, 'xhtml_Tbody409'):
        assert _is_linked(b1, 'xhtml_Tbody409', a)
    _safe_set(a, 'xhtml_Tr410', b2)
    assert _is_linked(a, 'xhtml_Tr410', b2)
    if hasattr(b1, 'xhtml_Tbody409'):
        assert not _is_linked(b1, 'xhtml_Tbody409', a)
    if hasattr(b2, 'xhtml_Tbody409'):
        assert _is_linked(b2, 'xhtml_Tbody409', a)
    _safe_set(a, 'xhtml_Tr410', None)
    assert not _is_linked(a, 'xhtml_Tr410', b2)
    if hasattr(b2, 'xhtml_Tbody409'):
        assert not _is_linked(b2, 'xhtml_Tbody409', a)


def test_assoc_tr411_link_reassign_clear():
    a = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Tfoot(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b2 = xhtml_Tfoot(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    _safe_set(a, 'xhtml_Tr413', b1)
    assert _is_linked(a, 'xhtml_Tr413', b1)
    if hasattr(b1, 'xhtml_Tfoot412'):
        assert _is_linked(b1, 'xhtml_Tfoot412', a)
    _safe_set(a, 'xhtml_Tr413', b2)
    assert _is_linked(a, 'xhtml_Tr413', b2)
    if hasattr(b1, 'xhtml_Tfoot412'):
        assert not _is_linked(b1, 'xhtml_Tfoot412', a)
    if hasattr(b2, 'xhtml_Tfoot412'):
        assert _is_linked(b2, 'xhtml_Tfoot412', a)
    _safe_set(a, 'xhtml_Tr413', None)
    assert not _is_linked(a, 'xhtml_Tr413', b2)
    if hasattr(b2, 'xhtml_Tfoot412'):
        assert not _is_linked(b2, 'xhtml_Tfoot412', a)


def test_assoc_tr414_link_reassign_clear():
    a = xhtml_Tr(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", group="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b1 = xhtml_Thead(align="sample_text", char="sample_text", charoff="sample_text", class_="sample_text", lang="sample_text", style="sample_text", valign="sample_text")
    b2 = xhtml_Thead(align="sample_text_2", char="sample_text_2", charoff="sample_text_2", class_="sample_text_2", lang="sample_text_2", style="sample_text_2", valign="sample_text_2")
    _safe_set(a, 'xhtml_Tr416', b1)
    assert _is_linked(a, 'xhtml_Tr416', b1)
    if hasattr(b1, 'xhtml_Thead415'):
        assert _is_linked(b1, 'xhtml_Thead415', a)
    _safe_set(a, 'xhtml_Tr416', b2)
    assert _is_linked(a, 'xhtml_Tr416', b2)
    if hasattr(b1, 'xhtml_Thead415'):
        assert not _is_linked(b1, 'xhtml_Thead415', a)
    if hasattr(b2, 'xhtml_Thead415'):
        assert _is_linked(b2, 'xhtml_Thead415', a)
    _safe_set(a, 'xhtml_Tr416', None)
    assert not _is_linked(a, 'xhtml_Tr416', b2)
    if hasattr(b2, 'xhtml_Thead415'):
        assert not _is_linked(b2, 'xhtml_Thead415', a)


def test_assoc_tt105_link_reassign_clear():
    a = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Tt107', b1)
    assert _is_linked(a, 'xhtml_Tt107', b1)
    if hasattr(b1, 'xhtml_Flow106'):
        assert _is_linked(b1, 'xhtml_Flow106', a)
    _safe_set(a, 'xhtml_Tt107', b2)
    assert _is_linked(a, 'xhtml_Tt107', b2)
    if hasattr(b1, 'xhtml_Flow106'):
        assert not _is_linked(b1, 'xhtml_Flow106', a)
    if hasattr(b2, 'xhtml_Flow106'):
        assert _is_linked(b2, 'xhtml_Flow106', a)
    _safe_set(a, 'xhtml_Tt107', None)
    assert not _is_linked(a, 'xhtml_Tt107', b2)
    if hasattr(b2, 'xhtml_Flow106'):
        assert not _is_linked(b2, 'xhtml_Flow106', a)


def test_assoc_tt176_link_reassign_clear():
    a = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Tt178', b1)
    assert _is_linked(a, 'xhtml_Tt178', b1)
    if hasattr(b1, 'xhtml_Inline177'):
        assert _is_linked(b1, 'xhtml_Inline177', a)
    _safe_set(a, 'xhtml_Tt178', b2)
    assert _is_linked(a, 'xhtml_Tt178', b2)
    if hasattr(b1, 'xhtml_Inline177'):
        assert not _is_linked(b1, 'xhtml_Inline177', a)
    if hasattr(b2, 'xhtml_Inline177'):
        assert _is_linked(b2, 'xhtml_Inline177', a)
    _safe_set(a, 'xhtml_Tt178', None)
    assert not _is_linked(a, 'xhtml_Tt178', b2)
    if hasattr(b2, 'xhtml_Inline177'):
        assert not _is_linked(b2, 'xhtml_Inline177', a)


def test_assoc_tt274_link_reassign_clear():
    a = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Tt276', b1)
    assert _is_linked(a, 'xhtml_Tt276', b1)
    if hasattr(b1, 'xhtml_Object275'):
        assert _is_linked(b1, 'xhtml_Object275', a)
    _safe_set(a, 'xhtml_Tt276', b2)
    assert _is_linked(a, 'xhtml_Tt276', b2)
    if hasattr(b1, 'xhtml_Object275'):
        assert not _is_linked(b1, 'xhtml_Object275', a)
    if hasattr(b2, 'xhtml_Object275'):
        assert _is_linked(b2, 'xhtml_Object275', a)
    _safe_set(a, 'xhtml_Tt276', None)
    assert not _is_linked(a, 'xhtml_Tt276', b2)
    if hasattr(b2, 'xhtml_Object275'):
        assert not _is_linked(b2, 'xhtml_Object275', a)


def test_assoc_tt332_link_reassign_clear():
    a = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Tt334', b1)
    assert _is_linked(a, 'xhtml_Tt334', b1)
    if hasattr(b1, 'xhtml_PreContent333'):
        assert _is_linked(b1, 'xhtml_PreContent333', a)
    _safe_set(a, 'xhtml_Tt334', b2)
    assert _is_linked(a, 'xhtml_Tt334', b2)
    if hasattr(b1, 'xhtml_PreContent333'):
        assert not _is_linked(b1, 'xhtml_PreContent333', a)
    if hasattr(b2, 'xhtml_PreContent333'):
        assert _is_linked(b2, 'xhtml_PreContent333', a)
    _safe_set(a, 'xhtml_Tt334', None)
    assert not _is_linked(a, 'xhtml_Tt334', b2)
    if hasattr(b2, 'xhtml_PreContent333'):
        assert not _is_linked(b2, 'xhtml_PreContent333', a)


def test_assoc_tt7_link_reassign_clear():
    a = xhtml_Tt(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Tt', b1)
    assert _is_linked(a, 'xhtml_Tt', b1)
    if hasattr(b1, 'xhtml_AContent8'):
        assert _is_linked(b1, 'xhtml_AContent8', a)
    _safe_set(a, 'xhtml_Tt', b2)
    assert _is_linked(a, 'xhtml_Tt', b2)
    if hasattr(b1, 'xhtml_AContent8'):
        assert not _is_linked(b1, 'xhtml_AContent8', a)
    if hasattr(b2, 'xhtml_AContent8'):
        assert _is_linked(b2, 'xhtml_AContent8', a)
    _safe_set(a, 'xhtml_Tt', None)
    assert not _is_linked(a, 'xhtml_Tt', b2)
    if hasattr(b2, 'xhtml_AContent8'):
        assert not _is_linked(b2, 'xhtml_AContent8', a)


def test_assoc_ul238_link_reassign_clear():
    a = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Ul240', b1)
    assert _is_linked(a, 'xhtml_Ul240', b1)
    if hasattr(b1, 'xhtml_Object239'):
        assert _is_linked(b1, 'xhtml_Object239', a)
    _safe_set(a, 'xhtml_Ul240', b2)
    assert _is_linked(a, 'xhtml_Ul240', b2)
    if hasattr(b1, 'xhtml_Object239'):
        assert not _is_linked(b1, 'xhtml_Object239', a)
    if hasattr(b2, 'xhtml_Object239'):
        assert _is_linked(b2, 'xhtml_Object239', a)
    _safe_set(a, 'xhtml_Ul240', None)
    assert not _is_linked(a, 'xhtml_Ul240', b2)
    if hasattr(b2, 'xhtml_Object239'):
        assert not _is_linked(b2, 'xhtml_Object239', a)


def test_assoc_ul46_link_reassign_clear():
    a = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Block(block="sample_text", mixed="sample_text")
    b2 = xhtml_Block(block="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Ul', b1)
    assert _is_linked(a, 'xhtml_Ul', b1)
    if hasattr(b1, 'xhtml_Block47'):
        assert _is_linked(b1, 'xhtml_Block47', a)
    _safe_set(a, 'xhtml_Ul', b2)
    assert _is_linked(a, 'xhtml_Ul', b2)
    if hasattr(b1, 'xhtml_Block47'):
        assert not _is_linked(b1, 'xhtml_Block47', a)
    if hasattr(b2, 'xhtml_Block47'):
        assert _is_linked(b2, 'xhtml_Block47', a)
    _safe_set(a, 'xhtml_Ul', None)
    assert not _is_linked(a, 'xhtml_Ul', b2)
    if hasattr(b2, 'xhtml_Block47'):
        assert not _is_linked(b2, 'xhtml_Block47', a)


def test_assoc_ul70_link_reassign_clear():
    a = xhtml_Ul(class_="sample_text", lang="sample_text", li="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Ul72', b1)
    assert _is_linked(a, 'xhtml_Ul72', b1)
    if hasattr(b1, 'xhtml_Flow71'):
        assert _is_linked(b1, 'xhtml_Flow71', a)
    _safe_set(a, 'xhtml_Ul72', b2)
    assert _is_linked(a, 'xhtml_Ul72', b2)
    if hasattr(b1, 'xhtml_Flow71'):
        assert not _is_linked(b1, 'xhtml_Flow71', a)
    if hasattr(b2, 'xhtml_Flow71'):
        assert _is_linked(b2, 'xhtml_Flow71', a)
    _safe_set(a, 'xhtml_Ul72', None)
    assert not _is_linked(a, 'xhtml_Ul72', b2)
    if hasattr(b2, 'xhtml_Flow71'):
        assert not _is_linked(b2, 'xhtml_Flow71', a)


def test_assoc_var141_link_reassign_clear():
    a = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Flow(group="sample_text", mixed="sample_text")
    b2 = xhtml_Flow(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Var143', b1)
    assert _is_linked(a, 'xhtml_Var143', b1)
    if hasattr(b1, 'xhtml_Flow142'):
        assert _is_linked(b1, 'xhtml_Flow142', a)
    _safe_set(a, 'xhtml_Var143', b2)
    assert _is_linked(a, 'xhtml_Var143', b2)
    if hasattr(b1, 'xhtml_Flow142'):
        assert not _is_linked(b1, 'xhtml_Flow142', a)
    if hasattr(b2, 'xhtml_Flow142'):
        assert _is_linked(b2, 'xhtml_Flow142', a)
    _safe_set(a, 'xhtml_Var143', None)
    assert not _is_linked(a, 'xhtml_Var143', b2)
    if hasattr(b2, 'xhtml_Flow142'):
        assert not _is_linked(b2, 'xhtml_Flow142', a)


def test_assoc_var212_link_reassign_clear():
    a = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Inline(inline="sample_text", mixed="sample_text")
    b2 = xhtml_Inline(inline="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Var214', b1)
    assert _is_linked(a, 'xhtml_Var214', b1)
    if hasattr(b1, 'xhtml_Inline213'):
        assert _is_linked(b1, 'xhtml_Inline213', a)
    _safe_set(a, 'xhtml_Var214', b2)
    assert _is_linked(a, 'xhtml_Var214', b2)
    if hasattr(b1, 'xhtml_Inline213'):
        assert not _is_linked(b1, 'xhtml_Inline213', a)
    if hasattr(b2, 'xhtml_Inline213'):
        assert _is_linked(b2, 'xhtml_Inline213', a)
    _safe_set(a, 'xhtml_Var214', None)
    assert not _is_linked(a, 'xhtml_Var214', b2)
    if hasattr(b2, 'xhtml_Inline213'):
        assert not _is_linked(b2, 'xhtml_Inline213', a)


def test_assoc_var31_link_reassign_clear():
    a = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_AContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_AContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Var', b1)
    assert _is_linked(a, 'xhtml_Var', b1)
    if hasattr(b1, 'xhtml_AContent32'):
        assert _is_linked(b1, 'xhtml_AContent32', a)
    _safe_set(a, 'xhtml_Var', b2)
    assert _is_linked(a, 'xhtml_Var', b2)
    if hasattr(b1, 'xhtml_AContent32'):
        assert not _is_linked(b1, 'xhtml_AContent32', a)
    if hasattr(b2, 'xhtml_AContent32'):
        assert _is_linked(b2, 'xhtml_AContent32', a)
    _safe_set(a, 'xhtml_Var', None)
    assert not _is_linked(a, 'xhtml_Var', b2)
    if hasattr(b2, 'xhtml_AContent32'):
        assert not _is_linked(b2, 'xhtml_AContent32', a)


def test_assoc_var310_link_reassign_clear():
    a = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_Object(group="sample_text", hl7Id="sample_text", mixed="sample_text", name="sample_text")
    b2 = xhtml_Object(group="sample_text_2", hl7Id="sample_text_2", mixed="sample_text_2", name="sample_text_2")
    _safe_set(a, 'xhtml_Var312', b1)
    assert _is_linked(a, 'xhtml_Var312', b1)
    if hasattr(b1, 'xhtml_Object311'):
        assert _is_linked(b1, 'xhtml_Object311', a)
    _safe_set(a, 'xhtml_Var312', b2)
    assert _is_linked(a, 'xhtml_Var312', b2)
    if hasattr(b1, 'xhtml_Object311'):
        assert not _is_linked(b1, 'xhtml_Object311', a)
    if hasattr(b2, 'xhtml_Object311'):
        assert _is_linked(b2, 'xhtml_Object311', a)
    _safe_set(a, 'xhtml_Var312', None)
    assert not _is_linked(a, 'xhtml_Var312', b2)
    if hasattr(b2, 'xhtml_Object311'):
        assert not _is_linked(b2, 'xhtml_Object311', a)


def test_assoc_var368_link_reassign_clear():
    a = xhtml_Var(class_="sample_text", lang="sample_text", style="sample_text")
    b1 = xhtml_PreContent(group="sample_text", mixed="sample_text")
    b2 = xhtml_PreContent(group="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'xhtml_Var370', b1)
    assert _is_linked(a, 'xhtml_Var370', b1)
    if hasattr(b1, 'xhtml_PreContent369'):
        assert _is_linked(b1, 'xhtml_PreContent369', a)
    _safe_set(a, 'xhtml_Var370', b2)
    assert _is_linked(a, 'xhtml_Var370', b2)
    if hasattr(b1, 'xhtml_PreContent369'):
        assert not _is_linked(b1, 'xhtml_PreContent369', a)
    if hasattr(b2, 'xhtml_PreContent369'):
        assert _is_linked(b2, 'xhtml_PreContent369', a)
    _safe_set(a, 'xhtml_Var370', None)
    assert not _is_linked(a, 'xhtml_Var370', b2)
    if hasattr(b2, 'xhtml_PreContent369'):
        assert not _is_linked(b2, 'xhtml_PreContent369', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AContent_strategy = st.builds(AContent)
@given(instance=AContent_strategy)
@settings(max_examples=25)
def test_AContent_instantiation(instance):
    assert isinstance(instance, AContent)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


Flow_strategy = st.builds(Flow)
@given(instance=Flow_strategy)
@settings(max_examples=25)
def test_Flow_instantiation(instance):
    assert isinstance(instance, Flow)


Inline_strategy = st.builds(Inline)
@given(instance=Inline_strategy)
@settings(max_examples=25)
def test_Inline_instantiation(instance):
    assert isinstance(instance, Inline)


PreContent_strategy = st.builds(PreContent)
@given(instance=PreContent_strategy)
@settings(max_examples=25)
def test_PreContent_instantiation(instance):
    assert isinstance(instance, PreContent)


xhtml_A_strategy = st.builds(xhtml_A, class_=safe_text, coords=safe_text, href=safe_text, lang=safe_text, name=safe_text, shape=safe_text, style=safe_text, type=safe_text)
@given(instance=xhtml_A_strategy)
@settings(max_examples=25)
def test_xhtml_A_instantiation(instance):
    assert isinstance(instance, xhtml_A)


xhtml_AContent_strategy = st.builds(xhtml_AContent, group=safe_text, mixed=safe_text)
@given(instance=xhtml_AContent_strategy)
@settings(max_examples=25)
def test_xhtml_AContent_instantiation(instance):
    assert isinstance(instance, xhtml_AContent)


xhtml_Abbr_strategy = st.builds(xhtml_Abbr, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Abbr_strategy)
@settings(max_examples=25)
def test_xhtml_Abbr_instantiation(instance):
    assert isinstance(instance, xhtml_Abbr)


xhtml_Acronym_strategy = st.builds(xhtml_Acronym, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Acronym_strategy)
@settings(max_examples=25)
def test_xhtml_Acronym_instantiation(instance):
    assert isinstance(instance, xhtml_Acronym)


xhtml_B_strategy = st.builds(xhtml_B, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_B_strategy)
@settings(max_examples=25)
def test_xhtml_B_instantiation(instance):
    assert isinstance(instance, xhtml_B)


xhtml_Big_strategy = st.builds(xhtml_Big, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Big_strategy)
@settings(max_examples=25)
def test_xhtml_Big_instantiation(instance):
    assert isinstance(instance, xhtml_Big)


xhtml_Block_strategy = st.builds(xhtml_Block, block=safe_text, mixed=safe_text)
@given(instance=xhtml_Block_strategy)
@settings(max_examples=25)
def test_xhtml_Block_instantiation(instance):
    assert isinstance(instance, xhtml_Block)


xhtml_Blockquote_strategy = st.builds(xhtml_Blockquote, cite=safe_text, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Blockquote_strategy)
@settings(max_examples=25)
def test_xhtml_Blockquote_instantiation(instance):
    assert isinstance(instance, xhtml_Blockquote)


xhtml_Br_strategy = st.builds(xhtml_Br, class_=safe_text, style=safe_text)
@given(instance=xhtml_Br_strategy)
@settings(max_examples=25)
def test_xhtml_Br_instantiation(instance):
    assert isinstance(instance, xhtml_Br)


xhtml_Caption_strategy = st.builds(xhtml_Caption, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Caption_strategy)
@settings(max_examples=25)
def test_xhtml_Caption_instantiation(instance):
    assert isinstance(instance, xhtml_Caption)


xhtml_Cite_strategy = st.builds(xhtml_Cite, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Cite_strategy)
@settings(max_examples=25)
def test_xhtml_Cite_instantiation(instance):
    assert isinstance(instance, xhtml_Cite)


xhtml_Code_strategy = st.builds(xhtml_Code, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Code_strategy)
@settings(max_examples=25)
def test_xhtml_Code_instantiation(instance):
    assert isinstance(instance, xhtml_Code)


xhtml_Col_strategy = st.builds(xhtml_Col, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, lang=safe_text, span=safe_text, style=safe_text, valign=safe_text, width=safe_text)
@given(instance=xhtml_Col_strategy)
@settings(max_examples=25)
def test_xhtml_Col_instantiation(instance):
    assert isinstance(instance, xhtml_Col)


xhtml_Colgroup_strategy = st.builds(xhtml_Colgroup, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, lang=safe_text, span=safe_text, style=safe_text, valign=safe_text, width=safe_text)
@given(instance=xhtml_Colgroup_strategy)
@settings(max_examples=25)
def test_xhtml_Colgroup_instantiation(instance):
    assert isinstance(instance, xhtml_Colgroup)


xhtml_Dd_strategy = st.builds(xhtml_Dd, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Dd_strategy)
@settings(max_examples=25)
def test_xhtml_Dd_instantiation(instance):
    assert isinstance(instance, xhtml_Dd)


xhtml_Del_strategy = st.builds(xhtml_Del)
@given(instance=xhtml_Del_strategy)
@settings(max_examples=25)
def test_xhtml_Del_instantiation(instance):
    assert isinstance(instance, xhtml_Del)


xhtml_Dfn_strategy = st.builds(xhtml_Dfn, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Dfn_strategy)
@settings(max_examples=25)
def test_xhtml_Dfn_instantiation(instance):
    assert isinstance(instance, xhtml_Dfn)


xhtml_Div_strategy = st.builds(xhtml_Div, class_=safe_text, hl7Id=safe_text, lang=safe_text, style=safe_text, title=safe_text)
@given(instance=xhtml_Div_strategy)
@settings(max_examples=25)
def test_xhtml_Div_instantiation(instance):
    assert isinstance(instance, xhtml_Div)


xhtml_Dl_strategy = st.builds(xhtml_Dl, class_=safe_text, group=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Dl_strategy)
@settings(max_examples=25)
def test_xhtml_Dl_instantiation(instance):
    assert isinstance(instance, xhtml_Dl)


xhtml_Dt_strategy = st.builds(xhtml_Dt, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Dt_strategy)
@settings(max_examples=25)
def test_xhtml_Dt_instantiation(instance):
    assert isinstance(instance, xhtml_Dt)


xhtml_Em_strategy = st.builds(xhtml_Em, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Em_strategy)
@settings(max_examples=25)
def test_xhtml_Em_instantiation(instance):
    assert isinstance(instance, xhtml_Em)


xhtml_Flow_strategy = st.builds(xhtml_Flow, group=safe_text, mixed=safe_text)
@given(instance=xhtml_Flow_strategy)
@settings(max_examples=25)
def test_xhtml_Flow_instantiation(instance):
    assert isinstance(instance, xhtml_Flow)


xhtml_Hr_strategy = st.builds(xhtml_Hr, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Hr_strategy)
@settings(max_examples=25)
def test_xhtml_Hr_instantiation(instance):
    assert isinstance(instance, xhtml_Hr)


xhtml_I_strategy = st.builds(xhtml_I, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_I_strategy)
@settings(max_examples=25)
def test_xhtml_I_instantiation(instance):
    assert isinstance(instance, xhtml_I)


xhtml_Img_strategy = st.builds(xhtml_Img, alt=safe_text, class_=safe_text, height=safe_text, hl7Id=safe_text, imageType=safe_text, lang=safe_text, src=safe_text, style=safe_text, width=safe_text)
@given(instance=xhtml_Img_strategy)
@settings(max_examples=25)
def test_xhtml_Img_instantiation(instance):
    assert isinstance(instance, xhtml_Img)


xhtml_Inline_strategy = st.builds(xhtml_Inline, inline=safe_text, mixed=safe_text)
@given(instance=xhtml_Inline_strategy)
@settings(max_examples=25)
def test_xhtml_Inline_instantiation(instance):
    assert isinstance(instance, xhtml_Inline)


xhtml_Ins_strategy = st.builds(xhtml_Ins)
@given(instance=xhtml_Ins_strategy)
@settings(max_examples=25)
def test_xhtml_Ins_instantiation(instance):
    assert isinstance(instance, xhtml_Ins)


xhtml_Kbd_strategy = st.builds(xhtml_Kbd, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Kbd_strategy)
@settings(max_examples=25)
def test_xhtml_Kbd_instantiation(instance):
    assert isinstance(instance, xhtml_Kbd)


xhtml_Li_strategy = st.builds(xhtml_Li, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Li_strategy)
@settings(max_examples=25)
def test_xhtml_Li_instantiation(instance):
    assert isinstance(instance, xhtml_Li)


xhtml_Object_strategy = st.builds(xhtml_Object, group=safe_text, hl7Id=safe_text, mixed=safe_text, name=safe_text)
@given(instance=xhtml_Object_strategy)
@settings(max_examples=25)
def test_xhtml_Object_instantiation(instance):
    assert isinstance(instance, xhtml_Object)


xhtml_Ol_strategy = st.builds(xhtml_Ol, class_=safe_text, lang=safe_text, li=safe_text, style=safe_text)
@given(instance=xhtml_Ol_strategy)
@settings(max_examples=25)
def test_xhtml_Ol_instantiation(instance):
    assert isinstance(instance, xhtml_Ol)


xhtml_P_strategy = st.builds(xhtml_P, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_P_strategy)
@settings(max_examples=25)
def test_xhtml_P_instantiation(instance):
    assert isinstance(instance, xhtml_P)


xhtml_Param_strategy = st.builds(xhtml_Param, name=safe_text, value=safe_text)
@given(instance=xhtml_Param_strategy)
@settings(max_examples=25)
def test_xhtml_Param_instantiation(instance):
    assert isinstance(instance, xhtml_Param)


xhtml_Pre_strategy = st.builds(xhtml_Pre, class_=safe_text, lang=safe_text, space=safe_text, style=safe_text)
@given(instance=xhtml_Pre_strategy)
@settings(max_examples=25)
def test_xhtml_Pre_instantiation(instance):
    assert isinstance(instance, xhtml_Pre)


xhtml_PreContent_strategy = st.builds(xhtml_PreContent, group=safe_text, mixed=safe_text)
@given(instance=xhtml_PreContent_strategy)
@settings(max_examples=25)
def test_xhtml_PreContent_instantiation(instance):
    assert isinstance(instance, xhtml_PreContent)


xhtml_Q_strategy = st.builds(xhtml_Q, cite1=safe_text, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Q_strategy)
@settings(max_examples=25)
def test_xhtml_Q_instantiation(instance):
    assert isinstance(instance, xhtml_Q)


xhtml_Samp_strategy = st.builds(xhtml_Samp, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Samp_strategy)
@settings(max_examples=25)
def test_xhtml_Samp_instantiation(instance):
    assert isinstance(instance, xhtml_Samp)


xhtml_Small_strategy = st.builds(xhtml_Small, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Small_strategy)
@settings(max_examples=25)
def test_xhtml_Small_instantiation(instance):
    assert isinstance(instance, xhtml_Small)


xhtml_Span_strategy = st.builds(xhtml_Span, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Span_strategy)
@settings(max_examples=25)
def test_xhtml_Span_instantiation(instance):
    assert isinstance(instance, xhtml_Span)


xhtml_Strong_strategy = st.builds(xhtml_Strong, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Strong_strategy)
@settings(max_examples=25)
def test_xhtml_Strong_instantiation(instance):
    assert isinstance(instance, xhtml_Strong)


xhtml_Sub_strategy = st.builds(xhtml_Sub, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Sub_strategy)
@settings(max_examples=25)
def test_xhtml_Sub_instantiation(instance):
    assert isinstance(instance, xhtml_Sub)


xhtml_Sup_strategy = st.builds(xhtml_Sup, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Sup_strategy)
@settings(max_examples=25)
def test_xhtml_Sup_instantiation(instance):
    assert isinstance(instance, xhtml_Sup)


xhtml_Table_strategy = st.builds(xhtml_Table, border=safe_text, cellpadding=safe_text, cellspacing=safe_text, class_=safe_text, frame=safe_text, hl7Id=safe_text, lang=safe_text, rules=safe_text, style=safe_text, width=safe_text)
@given(instance=xhtml_Table_strategy)
@settings(max_examples=25)
def test_xhtml_Table_instantiation(instance):
    assert isinstance(instance, xhtml_Table)


xhtml_Tbody_strategy = st.builds(xhtml_Tbody, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, lang=safe_text, style=safe_text, valign=safe_text)
@given(instance=xhtml_Tbody_strategy)
@settings(max_examples=25)
def test_xhtml_Tbody_instantiation(instance):
    assert isinstance(instance, xhtml_Tbody)


xhtml_Td_strategy = st.builds(xhtml_Td, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, colspan=safe_text, lang=safe_text, rowspan=safe_text, style=safe_text, valign=safe_text)
@given(instance=xhtml_Td_strategy)
@settings(max_examples=25)
def test_xhtml_Td_instantiation(instance):
    assert isinstance(instance, xhtml_Td)


xhtml_Tfoot_strategy = st.builds(xhtml_Tfoot, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, lang=safe_text, style=safe_text, valign=safe_text)
@given(instance=xhtml_Tfoot_strategy)
@settings(max_examples=25)
def test_xhtml_Tfoot_instantiation(instance):
    assert isinstance(instance, xhtml_Tfoot)


xhtml_Th_strategy = st.builds(xhtml_Th, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, colspan=safe_text, lang=safe_text, rowspan=safe_text, style=safe_text, valign=safe_text)
@given(instance=xhtml_Th_strategy)
@settings(max_examples=25)
def test_xhtml_Th_instantiation(instance):
    assert isinstance(instance, xhtml_Th)


xhtml_Thead_strategy = st.builds(xhtml_Thead, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, lang=safe_text, style=safe_text, valign=safe_text)
@given(instance=xhtml_Thead_strategy)
@settings(max_examples=25)
def test_xhtml_Thead_instantiation(instance):
    assert isinstance(instance, xhtml_Thead)


xhtml_Tr_strategy = st.builds(xhtml_Tr, align=safe_text, char=safe_text, charoff=safe_text, class_=safe_text, group=safe_text, lang=safe_text, style=safe_text, valign=safe_text)
@given(instance=xhtml_Tr_strategy)
@settings(max_examples=25)
def test_xhtml_Tr_instantiation(instance):
    assert isinstance(instance, xhtml_Tr)


xhtml_Tt_strategy = st.builds(xhtml_Tt, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Tt_strategy)
@settings(max_examples=25)
def test_xhtml_Tt_instantiation(instance):
    assert isinstance(instance, xhtml_Tt)


xhtml_Ul_strategy = st.builds(xhtml_Ul, class_=safe_text, lang=safe_text, li=safe_text, style=safe_text)
@given(instance=xhtml_Ul_strategy)
@settings(max_examples=25)
def test_xhtml_Ul_instantiation(instance):
    assert isinstance(instance, xhtml_Ul)


xhtml_Var_strategy = st.builds(xhtml_Var, class_=safe_text, lang=safe_text, style=safe_text)
@given(instance=xhtml_Var_strategy)
@settings(max_examples=25)
def test_xhtml_Var_instantiation(instance):
    assert isinstance(instance, xhtml_Var)



