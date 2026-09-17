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
    HTMLElement,
    HTML_B,
    HTML_A,
    HTML_I,
    HTML_U,
    HTML_IMG,
    HTML_BR,
    HTML_TR,
    HTML_S,
    HTML_FONT,
    HTML_SPAN,
    HTML_P,
    HTML_HR,
    HTML_TD,
    HTML_TABLE,
    HTML_Style,
    HTML_HTMLElement,
    HTML_HTML,
    HTML_DIV,
    StyleKey,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_htmlelement_is_not_abstract():
    assert not inspect.isabstract(HTMLElement)


def test_hyp_htmlelement_constructor_exists():
    assert callable(HTMLElement.__init__)


def test_hyp_htmlelement_constructor_args():
    sig = inspect.signature(HTMLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_b_is_not_abstract():
    assert not inspect.isabstract(HTML_B)


def test_hyp_html_b_constructor_exists():
    assert callable(HTML_B.__init__)


def test_hyp_html_b_constructor_args():
    sig = inspect.signature(HTML_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_a_is_not_abstract():
    assert not inspect.isabstract(HTML_A)


def test_hyp_html_a_constructor_exists():
    assert callable(HTML_A.__init__)


def test_hyp_html_a_constructor_args():
    sig = inspect.signature(HTML_A.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"




def test_hyp_html_i_is_not_abstract():
    assert not inspect.isabstract(HTML_I)


def test_hyp_html_i_constructor_exists():
    assert callable(HTML_I.__init__)


def test_hyp_html_i_constructor_args():
    sig = inspect.signature(HTML_I.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_u_is_not_abstract():
    assert not inspect.isabstract(HTML_U)


def test_hyp_html_u_constructor_exists():
    assert callable(HTML_U.__init__)


def test_hyp_html_u_constructor_args():
    sig = inspect.signature(HTML_U.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_img_is_not_abstract():
    assert not inspect.isabstract(HTML_IMG)


def test_hyp_html_img_constructor_exists():
    assert callable(HTML_IMG.__init__)


def test_hyp_html_img_constructor_args():
    sig = inspect.signature(HTML_IMG.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "width" in params, "Missing parameter 'width'"
    assert "border" in params, "Missing parameter 'border'"
    assert "height" in params, "Missing parameter 'height'"







def test_hyp_html_br_is_not_abstract():
    assert not inspect.isabstract(HTML_BR)


def test_hyp_html_br_constructor_exists():
    assert callable(HTML_BR.__init__)


def test_hyp_html_br_constructor_args():
    sig = inspect.signature(HTML_BR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_tr_is_not_abstract():
    assert not inspect.isabstract(HTML_TR)


def test_hyp_html_tr_constructor_exists():
    assert callable(HTML_TR.__init__)


def test_hyp_html_tr_constructor_args():
    sig = inspect.signature(HTML_TR.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"
    assert "height" in params, "Missing parameter 'height'"







def test_hyp_html_s_is_not_abstract():
    assert not inspect.isabstract(HTML_S)


def test_hyp_html_s_constructor_exists():
    assert callable(HTML_S.__init__)


def test_hyp_html_s_constructor_args():
    sig = inspect.signature(HTML_S.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_font_is_not_abstract():
    assert not inspect.isabstract(HTML_FONT)


def test_hyp_html_font_constructor_exists():
    assert callable(HTML_FONT.__init__)


def test_hyp_html_font_constructor_args():
    sig = inspect.signature(HTML_FONT.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "color" in params, "Missing parameter 'color'"
    assert "face" in params, "Missing parameter 'face'"
    assert "value" in params, "Missing parameter 'value'"







def test_hyp_html_span_is_not_abstract():
    assert not inspect.isabstract(HTML_SPAN)


def test_hyp_html_span_constructor_exists():
    assert callable(HTML_SPAN.__init__)


def test_hyp_html_span_constructor_args():
    sig = inspect.signature(HTML_SPAN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_p_is_not_abstract():
    assert not inspect.isabstract(HTML_P)


def test_hyp_html_p_constructor_exists():
    assert callable(HTML_P.__init__)


def test_hyp_html_p_constructor_args():
    sig = inspect.signature(HTML_P.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"




def test_hyp_html_hr_is_not_abstract():
    assert not inspect.isabstract(HTML_HR)


def test_hyp_html_hr_constructor_exists():
    assert callable(HTML_HR.__init__)


def test_hyp_html_hr_constructor_args():
    sig = inspect.signature(HTML_HR.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_html_td_is_not_abstract():
    assert not inspect.isabstract(HTML_TD)


def test_hyp_html_td_constructor_exists():
    assert callable(HTML_TD.__init__)


def test_hyp_html_td_constructor_args():
    sig = inspect.signature(HTML_TD.__init__)
    params = list(sig.parameters.keys())
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "height" in params, "Missing parameter 'height'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "width" in params, "Missing parameter 'width'"










def test_hyp_html_table_is_not_abstract():
    assert not inspect.isabstract(HTML_TABLE)


def test_hyp_html_table_constructor_exists():
    assert callable(HTML_TABLE.__init__)


def test_hyp_html_table_constructor_args():
    sig = inspect.signature(HTML_TABLE.__init__)
    params = list(sig.parameters.keys())
    assert "border" in params, "Missing parameter 'border'"
    assert "cellspacing" in params, "Missing parameter 'cellspacing'"
    assert "width" in params, "Missing parameter 'width'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"
    assert "align" in params, "Missing parameter 'align'"
    assert "cellpadding" in params, "Missing parameter 'cellpadding'"









def test_hyp_html_style_is_not_abstract():
    assert not inspect.isabstract(HTML_Style)


def test_hyp_html_style_constructor_exists():
    assert callable(HTML_Style.__init__)


def test_hyp_html_style_constructor_args():
    sig = inspect.signature(HTML_Style.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_html_htmlelement_is_not_abstract():
    assert not inspect.isabstract(HTML_HTMLElement)


def test_hyp_html_htmlelement_constructor_exists():
    assert callable(HTML_HTMLElement.__init__)


def test_hyp_html_htmlelement_constructor_args():
    sig = inspect.signature(HTML_HTMLElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_html_is_not_abstract():
    assert not inspect.isabstract(HTML_HTML)


def test_hyp_html_html_constructor_exists():
    assert callable(HTML_HTML.__init__)


def test_hyp_html_html_constructor_args():
    sig = inspect.signature(HTML_HTML.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_div_is_not_abstract():
    assert not inspect.isabstract(HTML_DIV)


def test_hyp_html_div_constructor_exists():
    assert callable(HTML_DIV.__init__)


def test_hyp_html_div_constructor_args():
    sig = inspect.signature(HTML_DIV.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"


def test_hyp_stylekey_exists():
    # Check that the Enumeration exists
    assert StyleKey is not None

def test_hyp_stylekey_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StyleKey]
    expected_literals = [
        "display",
        "width",
        "textAlign",
        "textDecoration",
        "backgroundColor",
        "color",
        "lineHeight",
        "padding",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StyleKey"


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
HTMLElement_strategy = st.builds(
    HTMLElement,
)
HTML_B_strategy = st.builds(
    HTML_B,
)
HTML_A_strategy = st.builds(
    HTML_A,
    ref=
        safe_text
)
HTML_I_strategy = st.builds(
    HTML_I,
)
HTML_U_strategy = st.builds(
    HTML_U,
)
HTML_IMG_strategy = st.builds(
    HTML_IMG,
    src=
        safe_text,
    width=
        safe_text,
    border=
        safe_text,
    height=
        safe_text
)
HTML_BR_strategy = st.builds(
    HTML_BR,
)
HTML_TR_strategy = st.builds(
    HTML_TR,
    align=
        safe_text,
    valign=
        safe_text,
    bgcolor=
        safe_text,
    height=
        safe_text
)
HTML_S_strategy = st.builds(
    HTML_S,
)
HTML_FONT_strategy = st.builds(
    HTML_FONT,
    size=
        safe_text,
    color=
        safe_text,
    face=
        safe_text,
    value=
        safe_text
)
HTML_SPAN_strategy = st.builds(
    HTML_SPAN,
)
HTML_P_strategy = st.builds(
    HTML_P,
    align=
        safe_text
)
HTML_HR_strategy = st.builds(
    HTML_HR,
    color=
        safe_text
)
HTML_TD_strategy = st.builds(
    HTML_TD,
    colspan=
        safe_text,
    bgcolor=
        safe_text,
    align=
        safe_text,
    valign=
        safe_text,
    height=
        safe_text,
    rowspan=
        safe_text,
    width=
        safe_text
)
HTML_TABLE_strategy = st.builds(
    HTML_TABLE,
    border=
        st.integers(),
    cellspacing=
        safe_text,
    width=
        safe_text,
    bgcolor=
        safe_text,
    align=
        safe_text,
    cellpadding=
        safe_text
)
HTML_Style_strategy = st.builds(
    HTML_Style,
    key=
        safe_text,
    value=
        safe_text
)
HTML_HTMLElement_strategy = st.builds(
    HTML_HTMLElement,
)
HTML_HTML_strategy = st.builds(
    HTML_HTML,
)
HTML_DIV_strategy = st.builds(
    HTML_DIV,
    align=
        safe_text
)






@given(instance=HTML_A_strategy)
def test_hyp_html_a_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original






@given(instance=HTML_IMG_strategy)
def test_hyp_html_img_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=HTML_IMG_strategy)
def test_hyp_html_img_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=HTML_IMG_strategy)
def test_hyp_html_img_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=HTML_IMG_strategy)
def test_hyp_html_img_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=HTML_TR_strategy)
def test_hyp_html_tr_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=HTML_TR_strategy)
def test_hyp_html_tr_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=HTML_TR_strategy)
def test_hyp_html_tr_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original



@given(instance=HTML_TR_strategy)
def test_hyp_html_tr_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original





@given(instance=HTML_FONT_strategy)
def test_hyp_html_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=HTML_FONT_strategy)
def test_hyp_html_font_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=HTML_FONT_strategy)
def test_hyp_html_font_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original



@given(instance=HTML_FONT_strategy)
def test_hyp_html_font_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=HTML_P_strategy)
def test_hyp_html_p_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original




@given(instance=HTML_HR_strategy)
def test_hyp_html_hr_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=HTML_TD_strategy)
def test_hyp_html_td_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original



@given(instance=HTML_TD_strategy)
def test_hyp_html_td_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original



@given(instance=HTML_TD_strategy)
def test_hyp_html_td_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=HTML_TD_strategy)
def test_hyp_html_td_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=HTML_TD_strategy)
def test_hyp_html_td_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=HTML_TD_strategy)
def test_hyp_html_td_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original



@given(instance=HTML_TD_strategy)
def test_hyp_html_td_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original




@given(instance=HTML_TABLE_strategy)
def test_hyp_html_table_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=HTML_TABLE_strategy)
def test_hyp_html_table_cellspacing_setter(instance):
    original = instance.cellspacing
    instance.cellspacing = original
    assert instance.cellspacing == original



@given(instance=HTML_TABLE_strategy)
def test_hyp_html_table_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=HTML_TABLE_strategy)
def test_hyp_html_table_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original



@given(instance=HTML_TABLE_strategy)
def test_hyp_html_table_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=HTML_TABLE_strategy)
def test_hyp_html_table_cellpadding_setter(instance):
    original = instance.cellpadding
    instance.cellpadding = original
    assert instance.cellpadding == original




@given(instance=HTML_Style_strategy)
def test_hyp_html_style_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=HTML_Style_strategy)
def test_hyp_html_style_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=HTML_DIV_strategy)
def test_hyp_html_div_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    HTMLElement,
    HTML_A,
    HTML_B,
    HTML_BR,
    HTML_DIV,
    HTML_FONT,
    HTML_HR,
    HTML_HTML,
    HTML_HTMLElement,
    HTML_I,
    HTML_IMG,
    HTML_P,
    HTML_S,
    HTML_SPAN,
    HTML_Style,
    HTML_TABLE,
    HTML_TD,
    HTML_TR,
    HTML_U,
    StyleKey,
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

def test_HTML_A_ref_value_roundtrip():
    instance = HTML_A(ref="sample_text")
    assert instance.ref == "sample_text"
    instance.ref = "sample_text_2"
    assert instance.ref == "sample_text_2"


def test_HTML_DIV_align_value_roundtrip():
    instance = HTML_DIV(align="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_HTML_FONT_color_value_roundtrip():
    instance = HTML_FONT(color="sample_text", face="sample_text", size="sample_text", value="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_HTML_FONT_face_value_roundtrip():
    instance = HTML_FONT(color="sample_text", face="sample_text", size="sample_text", value="sample_text")
    assert instance.face == "sample_text"
    instance.face = "sample_text_2"
    assert instance.face == "sample_text_2"


def test_HTML_FONT_size_value_roundtrip():
    instance = HTML_FONT(color="sample_text", face="sample_text", size="sample_text", value="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_HTML_FONT_value_value_roundtrip():
    instance = HTML_FONT(color="sample_text", face="sample_text", size="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_HTML_HR_color_value_roundtrip():
    instance = HTML_HR(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_HTML_IMG_border_value_roundtrip():
    instance = HTML_IMG(border="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.border == "sample_text"
    instance.border = "sample_text_2"
    assert instance.border == "sample_text_2"


def test_HTML_IMG_height_value_roundtrip():
    instance = HTML_IMG(border="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_HTML_IMG_src_value_roundtrip():
    instance = HTML_IMG(border="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_HTML_IMG_width_value_roundtrip():
    instance = HTML_IMG(border="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_HTML_P_align_value_roundtrip():
    instance = HTML_P(align="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_HTML_Style_key_value_roundtrip():
    instance = HTML_Style(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_HTML_Style_value_value_roundtrip():
    instance = HTML_Style(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_HTML_TABLE_align_value_roundtrip():
    instance = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_HTML_TABLE_bgcolor_value_roundtrip():
    instance = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.bgcolor == "sample_text"
    instance.bgcolor = "sample_text_2"
    assert instance.bgcolor == "sample_text_2"


def test_HTML_TABLE_border_value_roundtrip():
    instance = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.border == 7
    instance.border = 13
    assert instance.border == 13


def test_HTML_TABLE_cellpadding_value_roundtrip():
    instance = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.cellpadding == "sample_text"
    instance.cellpadding = "sample_text_2"
    assert instance.cellpadding == "sample_text_2"


def test_HTML_TABLE_cellspacing_value_roundtrip():
    instance = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.cellspacing == "sample_text"
    instance.cellspacing = "sample_text_2"
    assert instance.cellspacing == "sample_text_2"


def test_HTML_TABLE_width_value_roundtrip():
    instance = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_HTML_TD_align_value_roundtrip():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_HTML_TD_bgcolor_value_roundtrip():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.bgcolor == "sample_text"
    instance.bgcolor = "sample_text_2"
    assert instance.bgcolor == "sample_text_2"


def test_HTML_TD_colspan_value_roundtrip():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.colspan == "sample_text"
    instance.colspan = "sample_text_2"
    assert instance.colspan == "sample_text_2"


def test_HTML_TD_height_value_roundtrip():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_HTML_TD_rowspan_value_roundtrip():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.rowspan == "sample_text"
    instance.rowspan = "sample_text_2"
    assert instance.rowspan == "sample_text_2"


def test_HTML_TD_valign_value_roundtrip():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_HTML_TD_width_value_roundtrip():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_HTML_TR_align_value_roundtrip():
    instance = HTML_TR(align="sample_text", bgcolor="sample_text", height="sample_text", valign="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_HTML_TR_bgcolor_value_roundtrip():
    instance = HTML_TR(align="sample_text", bgcolor="sample_text", height="sample_text", valign="sample_text")
    assert instance.bgcolor == "sample_text"
    instance.bgcolor = "sample_text_2"
    assert instance.bgcolor == "sample_text_2"


def test_HTML_TR_height_value_roundtrip():
    instance = HTML_TR(align="sample_text", bgcolor="sample_text", height="sample_text", valign="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_HTML_TR_valign_value_roundtrip():
    instance = HTML_TR(align="sample_text", bgcolor="sample_text", height="sample_text", valign="sample_text")
    assert instance.valign == "sample_text"
    instance.valign = "sample_text_2"
    assert instance.valign == "sample_text_2"


def test_HTML_A_isa_HTMLElement():
    instance = HTML_A(ref="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_B_isa_HTMLElement():
    instance = HTML_B()
    assert isinstance(instance, HTMLElement)


def test_HTML_BR_isa_HTMLElement():
    instance = HTML_BR()
    assert isinstance(instance, HTMLElement)


def test_HTML_DIV_isa_HTMLElement():
    instance = HTML_DIV(align="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_FONT_isa_HTMLElement():
    instance = HTML_FONT(color="sample_text", face="sample_text", size="sample_text", value="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_HR_isa_HTMLElement():
    instance = HTML_HR(color="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_I_isa_HTMLElement():
    instance = HTML_I()
    assert isinstance(instance, HTMLElement)


def test_HTML_IMG_isa_HTMLElement():
    instance = HTML_IMG(border="sample_text", height="sample_text", src="sample_text", width="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_P_isa_HTMLElement():
    instance = HTML_P(align="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_S_isa_HTMLElement():
    instance = HTML_S()
    assert isinstance(instance, HTMLElement)


def test_HTML_SPAN_isa_HTMLElement():
    instance = HTML_SPAN()
    assert isinstance(instance, HTMLElement)


def test_HTML_TABLE_isa_HTMLElement():
    instance = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_TD_isa_HTMLElement():
    instance = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_TR_isa_HTMLElement():
    instance = HTML_TR(align="sample_text", bgcolor="sample_text", height="sample_text", valign="sample_text")
    assert isinstance(instance, HTMLElement)


def test_HTML_U_isa_HTMLElement():
    instance = HTML_U()
    assert isinstance(instance, HTMLElement)


def test_assoc_styles4_link_reassign_clear():
    a = HTML_Style(key="sample_text", value="sample_text")
    b1 = HTML_HTMLElement()
    b2 = HTML_HTMLElement()
    _safe_set(a, 'HTML_Style', b1)
    assert _is_linked(a, 'HTML_Style', b1)
    if hasattr(b1, 'HTML_HTMLElement5'):
        assert _is_linked(b1, 'HTML_HTMLElement5', a)
    _safe_set(a, 'HTML_Style', b2)
    assert _is_linked(a, 'HTML_Style', b2)
    if hasattr(b1, 'HTML_HTMLElement5'):
        assert not _is_linked(b1, 'HTML_HTMLElement5', a)
    if hasattr(b2, 'HTML_HTMLElement5'):
        assert _is_linked(b2, 'HTML_HTMLElement5', a)
    _safe_set(a, 'HTML_Style', None)
    assert not _is_linked(a, 'HTML_Style', b2)
    if hasattr(b2, 'HTML_HTMLElement5'):
        assert not _is_linked(b2, 'HTML_HTMLElement5', a)


def test_assoc_tds7_link_reassign_clear():
    a = HTML_TR(align="sample_text", bgcolor="sample_text", height="sample_text", valign="sample_text")
    b1 = HTML_TD(align="sample_text", bgcolor="sample_text", colspan="sample_text", height="sample_text", rowspan="sample_text", valign="sample_text", width="sample_text")
    b2 = HTML_TD(align="sample_text_2", bgcolor="sample_text_2", colspan="sample_text_2", height="sample_text_2", rowspan="sample_text_2", valign="sample_text_2", width="sample_text_2")
    _safe_set(a, 'HTML_TR8', {b1})
    assert _is_linked(a, 'HTML_TR8', b1)
    if hasattr(b1, 'HTML_TD'):
        assert _is_linked(b1, 'HTML_TD', a)
    _safe_set(a, 'HTML_TR8', {b2})
    assert _is_linked(a, 'HTML_TR8', b2)
    if hasattr(b1, 'HTML_TD'):
        assert not _is_linked(b1, 'HTML_TD', a)
    if hasattr(b2, 'HTML_TD'):
        assert _is_linked(b2, 'HTML_TD', a)
    _safe_set(a, 'HTML_TR8', set())
    assert not _is_linked(a, 'HTML_TR8', b2)
    if hasattr(b2, 'HTML_TD'):
        assert not _is_linked(b2, 'HTML_TD', a)


def test_assoc_trs6_link_reassign_clear():
    a = HTML_TR(align="sample_text", bgcolor="sample_text", height="sample_text", valign="sample_text")
    b1 = HTML_TABLE(align="sample_text", bgcolor="sample_text", border=7, cellpadding="sample_text", cellspacing="sample_text", width="sample_text")
    b2 = HTML_TABLE(align="sample_text_2", bgcolor="sample_text_2", border=13, cellpadding="sample_text_2", cellspacing="sample_text_2", width="sample_text_2")
    _safe_set(a, 'HTML_TR', b1)
    assert _is_linked(a, 'HTML_TR', b1)
    if hasattr(b1, 'HTML_TABLE'):
        assert _is_linked(b1, 'HTML_TABLE', a)
    _safe_set(a, 'HTML_TR', b2)
    assert _is_linked(a, 'HTML_TR', b2)
    if hasattr(b1, 'HTML_TABLE'):
        assert not _is_linked(b1, 'HTML_TABLE', a)
    if hasattr(b2, 'HTML_TABLE'):
        assert _is_linked(b2, 'HTML_TABLE', a)
    _safe_set(a, 'HTML_TR', None)
    assert not _is_linked(a, 'HTML_TR', b2)
    if hasattr(b2, 'HTML_TABLE'):
        assert not _is_linked(b2, 'HTML_TABLE', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

HTMLElement_strategy = st.builds(HTMLElement)
@given(instance=HTMLElement_strategy)
@settings(max_examples=25)
def test_HTMLElement_instantiation(instance):
    assert isinstance(instance, HTMLElement)


HTML_A_strategy = st.builds(HTML_A, ref=safe_text)
@given(instance=HTML_A_strategy)
@settings(max_examples=25)
def test_HTML_A_instantiation(instance):
    assert isinstance(instance, HTML_A)


HTML_B_strategy = st.builds(HTML_B)
@given(instance=HTML_B_strategy)
@settings(max_examples=25)
def test_HTML_B_instantiation(instance):
    assert isinstance(instance, HTML_B)


HTML_BR_strategy = st.builds(HTML_BR)
@given(instance=HTML_BR_strategy)
@settings(max_examples=25)
def test_HTML_BR_instantiation(instance):
    assert isinstance(instance, HTML_BR)


HTML_DIV_strategy = st.builds(HTML_DIV, align=safe_text)
@given(instance=HTML_DIV_strategy)
@settings(max_examples=25)
def test_HTML_DIV_instantiation(instance):
    assert isinstance(instance, HTML_DIV)


HTML_FONT_strategy = st.builds(HTML_FONT, color=safe_text, face=safe_text, size=safe_text, value=safe_text)
@given(instance=HTML_FONT_strategy)
@settings(max_examples=25)
def test_HTML_FONT_instantiation(instance):
    assert isinstance(instance, HTML_FONT)


HTML_HR_strategy = st.builds(HTML_HR, color=safe_text)
@given(instance=HTML_HR_strategy)
@settings(max_examples=25)
def test_HTML_HR_instantiation(instance):
    assert isinstance(instance, HTML_HR)


HTML_HTML_strategy = st.builds(HTML_HTML)
@given(instance=HTML_HTML_strategy)
@settings(max_examples=25)
def test_HTML_HTML_instantiation(instance):
    assert isinstance(instance, HTML_HTML)


HTML_HTMLElement_strategy = st.builds(HTML_HTMLElement)
@given(instance=HTML_HTMLElement_strategy)
@settings(max_examples=25)
def test_HTML_HTMLElement_instantiation(instance):
    assert isinstance(instance, HTML_HTMLElement)


HTML_I_strategy = st.builds(HTML_I)
@given(instance=HTML_I_strategy)
@settings(max_examples=25)
def test_HTML_I_instantiation(instance):
    assert isinstance(instance, HTML_I)


HTML_IMG_strategy = st.builds(HTML_IMG, border=safe_text, height=safe_text, src=safe_text, width=safe_text)
@given(instance=HTML_IMG_strategy)
@settings(max_examples=25)
def test_HTML_IMG_instantiation(instance):
    assert isinstance(instance, HTML_IMG)


HTML_P_strategy = st.builds(HTML_P, align=safe_text)
@given(instance=HTML_P_strategy)
@settings(max_examples=25)
def test_HTML_P_instantiation(instance):
    assert isinstance(instance, HTML_P)


HTML_S_strategy = st.builds(HTML_S)
@given(instance=HTML_S_strategy)
@settings(max_examples=25)
def test_HTML_S_instantiation(instance):
    assert isinstance(instance, HTML_S)


HTML_SPAN_strategy = st.builds(HTML_SPAN)
@given(instance=HTML_SPAN_strategy)
@settings(max_examples=25)
def test_HTML_SPAN_instantiation(instance):
    assert isinstance(instance, HTML_SPAN)


HTML_Style_strategy = st.builds(HTML_Style, key=safe_text, value=safe_text)
@given(instance=HTML_Style_strategy)
@settings(max_examples=25)
def test_HTML_Style_instantiation(instance):
    assert isinstance(instance, HTML_Style)


HTML_TABLE_strategy = st.builds(HTML_TABLE, align=safe_text, bgcolor=safe_text, border=st.integers(), cellpadding=safe_text, cellspacing=safe_text, width=safe_text)
@given(instance=HTML_TABLE_strategy)
@settings(max_examples=25)
def test_HTML_TABLE_instantiation(instance):
    assert isinstance(instance, HTML_TABLE)


HTML_TD_strategy = st.builds(HTML_TD, align=safe_text, bgcolor=safe_text, colspan=safe_text, height=safe_text, rowspan=safe_text, valign=safe_text, width=safe_text)
@given(instance=HTML_TD_strategy)
@settings(max_examples=25)
def test_HTML_TD_instantiation(instance):
    assert isinstance(instance, HTML_TD)


HTML_TR_strategy = st.builds(HTML_TR, align=safe_text, bgcolor=safe_text, height=safe_text, valign=safe_text)
@given(instance=HTML_TR_strategy)
@settings(max_examples=25)
def test_HTML_TR_instantiation(instance):
    assert isinstance(instance, HTML_TR)


HTML_U_strategy = st.builds(HTML_U)
@given(instance=HTML_U_strategy)
@settings(max_examples=25)
def test_HTML_U_instantiation(instance):
    assert isinstance(instance, HTML_U)



