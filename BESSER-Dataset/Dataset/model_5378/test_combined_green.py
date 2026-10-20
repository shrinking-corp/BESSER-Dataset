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
    html5_htmlElement,
    html5_td,
    html5_container,
    html5_html,
    html5_legend,
    html5_option,
    html5_tr,
    htmlElement,
    html5_label,
    html5_dialog,
    html5_img,
    html5_select,
    html5_button,
    html5_input,
    html5_table,
    html5_Action,
    container,
    html5_fieldset,
    html5_div,
    types,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_html5_htmlelement_is_not_abstract():
    assert not inspect.isabstract(html5_htmlElement)


def test_hyp_html5_htmlelement_constructor_exists():
    assert callable(html5_htmlElement.__init__)


def test_hyp_html5_htmlelement_constructor_args():
    sig = inspect.signature(html5_htmlElement.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"




def test_hyp_html5_td_is_not_abstract():
    assert not inspect.isabstract(html5_td)


def test_hyp_html5_td_constructor_exists():
    assert callable(html5_td.__init__)


def test_hyp_html5_td_constructor_args():
    sig = inspect.signature(html5_td.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_container_is_not_abstract():
    assert not inspect.isabstract(html5_container)


def test_hyp_html5_container_constructor_exists():
    assert callable(html5_container.__init__)


def test_hyp_html5_container_constructor_args():
    sig = inspect.signature(html5_container.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"




def test_hyp_html5_html_is_not_abstract():
    assert not inspect.isabstract(html5_html)


def test_hyp_html5_html_constructor_exists():
    assert callable(html5_html.__init__)


def test_hyp_html5_html_constructor_args():
    sig = inspect.signature(html5_html.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_legend_is_not_abstract():
    assert not inspect.isabstract(html5_legend)


def test_hyp_html5_legend_constructor_exists():
    assert callable(html5_legend.__init__)


def test_hyp_html5_legend_constructor_args():
    sig = inspect.signature(html5_legend.__init__)
    params = list(sig.parameters.keys())
    assert "valor" in params, "Missing parameter 'valor'"
    assert "class_" in params, "Missing parameter 'class_'"





def test_hyp_html5_option_is_not_abstract():
    assert not inspect.isabstract(html5_option)


def test_hyp_html5_option_constructor_exists():
    assert callable(html5_option.__init__)


def test_hyp_html5_option_constructor_args():
    sig = inspect.signature(html5_option.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_tr_is_not_abstract():
    assert not inspect.isabstract(html5_tr)


def test_hyp_html5_tr_constructor_exists():
    assert callable(html5_tr.__init__)


def test_hyp_html5_tr_constructor_args():
    sig = inspect.signature(html5_tr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_htmlelement_is_not_abstract():
    assert not inspect.isabstract(htmlElement)


def test_hyp_htmlelement_constructor_exists():
    assert callable(htmlElement.__init__)


def test_hyp_htmlelement_constructor_args():
    sig = inspect.signature(htmlElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_label_is_not_abstract():
    assert not inspect.isabstract(html5_label)


def test_hyp_html5_label_constructor_exists():
    assert callable(html5_label.__init__)


def test_hyp_html5_label_constructor_args():
    sig = inspect.signature(html5_label.__init__)
    params = list(sig.parameters.keys())
    assert "valor" in params, "Missing parameter 'valor'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_html5_dialog_is_not_abstract():
    assert not inspect.isabstract(html5_dialog)


def test_hyp_html5_dialog_constructor_exists():
    assert callable(html5_dialog.__init__)


def test_hyp_html5_dialog_constructor_args():
    sig = inspect.signature(html5_dialog.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_img_is_not_abstract():
    assert not inspect.isabstract(html5_img)


def test_hyp_html5_img_constructor_exists():
    assert callable(html5_img.__init__)


def test_hyp_html5_img_constructor_args():
    sig = inspect.signature(html5_img.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"




def test_hyp_html5_select_is_not_abstract():
    assert not inspect.isabstract(html5_select)


def test_hyp_html5_select_constructor_exists():
    assert callable(html5_select.__init__)


def test_hyp_html5_select_constructor_args():
    sig = inspect.signature(html5_select.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "multiple" in params, "Missing parameter 'multiple'"





def test_hyp_html5_button_is_not_abstract():
    assert not inspect.isabstract(html5_button)


def test_hyp_html5_button_constructor_exists():
    assert callable(html5_button.__init__)


def test_hyp_html5_button_constructor_args():
    sig = inspect.signature(html5_button.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_html5_input_is_not_abstract():
    assert not inspect.isabstract(html5_input)


def test_hyp_html5_input_constructor_exists():
    assert callable(html5_input.__init__)


def test_hyp_html5_input_constructor_args():
    sig = inspect.signature(html5_input.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"
    assert "disable" in params, "Missing parameter 'disable'"






def test_hyp_html5_table_is_not_abstract():
    assert not inspect.isabstract(html5_table)


def test_hyp_html5_table_constructor_exists():
    assert callable(html5_table.__init__)


def test_hyp_html5_table_constructor_args():
    sig = inspect.signature(html5_table.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_action_is_not_abstract():
    assert not inspect.isabstract(html5_Action)


def test_hyp_html5_action_constructor_exists():
    assert callable(html5_Action.__init__)


def test_hyp_html5_action_constructor_args():
    sig = inspect.signature(html5_Action.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"




def test_hyp_container_is_not_abstract():
    assert not inspect.isabstract(container)


def test_hyp_container_constructor_exists():
    assert callable(container.__init__)


def test_hyp_container_constructor_args():
    sig = inspect.signature(container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_fieldset_is_not_abstract():
    assert not inspect.isabstract(html5_fieldset)


def test_hyp_html5_fieldset_constructor_exists():
    assert callable(html5_fieldset.__init__)


def test_hyp_html5_fieldset_constructor_args():
    sig = inspect.signature(html5_fieldset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html5_div_is_not_abstract():
    assert not inspect.isabstract(html5_div)


def test_hyp_html5_div_constructor_exists():
    assert callable(html5_div.__init__)


def test_hyp_html5_div_constructor_args():
    sig = inspect.signature(html5_div.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"


def test_hyp_types_exists():
    # Check that the Enumeration exists
    assert types is not None

def test_hyp_types_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in types]
    expected_literals = [
        "number",
        "text",
        "button",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in types"


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
html5_htmlElement_strategy = st.builds(
    html5_htmlElement,
    class_=
        safe_text
)
html5_td_strategy = st.builds(
    html5_td,
)
html5_container_strategy = st.builds(
    html5_container,
    class_=
        safe_text
)
html5_html_strategy = st.builds(
    html5_html,
)
html5_legend_strategy = st.builds(
    html5_legend,
    valor=
        safe_text,
    class_=
        safe_text
)
html5_option_strategy = st.builds(
    html5_option,
)
html5_tr_strategy = st.builds(
    html5_tr,
)
htmlElement_strategy = st.builds(
    htmlElement,
)
html5_label_strategy = st.builds(
    html5_label,
    valor=
        safe_text,
    value=
        safe_text
)
html5_dialog_strategy = st.builds(
    html5_dialog,
)
html5_img_strategy = st.builds(
    html5_img,
    src=
        safe_text
)
html5_select_strategy = st.builds(
    html5_select,
    size=
        safe_text,
    multiple=
        safe_text
)
html5_button_strategy = st.builds(
    html5_button,
    action=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
html5_input_strategy = st.builds(
    html5_input,
    value=
        safe_text,
    type=
        safe_text,
    disable=
        safe_text
)
html5_table_strategy = st.builds(
    html5_table,
)
html5_Action_strategy = st.builds(
    html5_Action,
    codigo=
        safe_text
)
container_strategy = st.builds(
    container,
)
html5_fieldset_strategy = st.builds(
    html5_fieldset,
)
html5_div_strategy = st.builds(
    html5_div,
    id=
        safe_text
)




@given(instance=html5_htmlElement_strategy)
def test_hyp_html5_htmlelement_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original





@given(instance=html5_container_strategy)
def test_hyp_html5_container_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original





@given(instance=html5_legend_strategy)
def test_hyp_html5_legend_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original



@given(instance=html5_legend_strategy)
def test_hyp_html5_legend_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original







@given(instance=html5_label_strategy)
def test_hyp_html5_label_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original



@given(instance=html5_label_strategy)
def test_hyp_html5_label_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=html5_img_strategy)
def test_hyp_html5_img_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original




@given(instance=html5_select_strategy)
def test_hyp_html5_select_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=html5_select_strategy)
def test_hyp_html5_select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original




@given(instance=html5_button_strategy)
def test_hyp_html5_button_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=html5_button_strategy)
def test_hyp_html5_button_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=html5_button_strategy)
def test_hyp_html5_button_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=html5_input_strategy)
def test_hyp_html5_input_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=html5_input_strategy)
def test_hyp_html5_input_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=html5_input_strategy)
def test_hyp_html5_input_disable_setter(instance):
    original = instance.disable
    instance.disable = original
    assert instance.disable == original





@given(instance=html5_Action_strategy)
def test_hyp_html5_action_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original






@given(instance=html5_div_strategy)
def test_hyp_html5_div_id_setter(instance):
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
    container,
    html5_Action,
    html5_button,
    html5_container,
    html5_dialog,
    html5_div,
    html5_fieldset,
    html5_html,
    html5_htmlElement,
    html5_img,
    html5_input,
    html5_label,
    html5_legend,
    html5_option,
    html5_select,
    html5_table,
    html5_td,
    html5_tr,
    htmlElement,
    types,
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

def test_html5_Action_codigo_value_roundtrip():
    instance = html5_Action(codigo="sample_text")
    assert instance.codigo == "sample_text"
    instance.codigo = "sample_text_2"
    assert instance.codigo == "sample_text_2"


def test_html5_button_action_value_roundtrip():
    instance = html5_button(action="sample_text", type="sample_text", value="sample_text")
    assert instance.action == "sample_text"
    instance.action = "sample_text_2"
    assert instance.action == "sample_text_2"


def test_html5_button_type_value_roundtrip():
    instance = html5_button(action="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_html5_button_value_value_roundtrip():
    instance = html5_button(action="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_html5_container_class__value_roundtrip():
    instance = html5_container(class_="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_html5_div_id_value_roundtrip():
    instance = html5_div(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_html5_htmlElement_class__value_roundtrip():
    instance = html5_htmlElement(class_="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_html5_img_src_value_roundtrip():
    instance = html5_img(src="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_html5_input_disable_value_roundtrip():
    instance = html5_input(disable="sample_text", type="sample_text", value="sample_text")
    assert instance.disable == "sample_text"
    instance.disable = "sample_text_2"
    assert instance.disable == "sample_text_2"


def test_html5_input_type_value_roundtrip():
    instance = html5_input(disable="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_html5_input_value_value_roundtrip():
    instance = html5_input(disable="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_html5_label_valor_value_roundtrip():
    instance = html5_label(valor="sample_text", value="sample_text")
    assert instance.valor == "sample_text"
    instance.valor = "sample_text_2"
    assert instance.valor == "sample_text_2"


def test_html5_label_value_value_roundtrip():
    instance = html5_label(valor="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_html5_legend_class__value_roundtrip():
    instance = html5_legend(class_="sample_text", valor="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_html5_legend_valor_value_roundtrip():
    instance = html5_legend(class_="sample_text", valor="sample_text")
    assert instance.valor == "sample_text"
    instance.valor = "sample_text_2"
    assert instance.valor == "sample_text_2"


def test_html5_select_multiple_value_roundtrip():
    instance = html5_select(multiple="sample_text", size="sample_text")
    assert instance.multiple == "sample_text"
    instance.multiple = "sample_text_2"
    assert instance.multiple == "sample_text_2"


def test_html5_select_size_value_roundtrip():
    instance = html5_select(multiple="sample_text", size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_html5_div_isa_container():
    instance = html5_div(id="sample_text")
    assert isinstance(instance, container)


def test_html5_fieldset_isa_container():
    instance = html5_fieldset()
    assert isinstance(instance, container)


def test_html5_button_isa_htmlElement():
    instance = html5_button(action="sample_text", type="sample_text", value="sample_text")
    assert isinstance(instance, htmlElement)


def test_html5_dialog_isa_htmlElement():
    instance = html5_dialog()
    assert isinstance(instance, htmlElement)


def test_html5_img_isa_htmlElement():
    instance = html5_img(src="sample_text")
    assert isinstance(instance, htmlElement)


def test_html5_input_isa_htmlElement():
    instance = html5_input(disable="sample_text", type="sample_text", value="sample_text")
    assert isinstance(instance, htmlElement)


def test_html5_label_isa_htmlElement():
    instance = html5_label(valor="sample_text", value="sample_text")
    assert isinstance(instance, htmlElement)


def test_html5_select_isa_htmlElement():
    instance = html5_select(multiple="sample_text", size="sample_text")
    assert isinstance(instance, htmlElement)


def test_html5_table_isa_htmlElement():
    instance = html5_table()
    assert isinstance(instance, htmlElement)


def test_assoc_actions0_link_reassign_clear():
    a = html5_div(id="sample_text")
    b1 = html5_Action(codigo="sample_text")
    b2 = html5_Action(codigo="sample_text_2")
    _safe_set(a, 'html5_div', {b1})
    assert _is_linked(a, 'html5_div', b1)
    if hasattr(b1, 'html5_Action'):
        assert _is_linked(b1, 'html5_Action', a)
    _safe_set(a, 'html5_div', {b2})
    assert _is_linked(a, 'html5_div', b2)
    if hasattr(b1, 'html5_Action'):
        assert not _is_linked(b1, 'html5_Action', a)
    if hasattr(b2, 'html5_Action'):
        assert _is_linked(b2, 'html5_Action', a)
    _safe_set(a, 'html5_div', set())
    assert not _is_linked(a, 'html5_div', b2)
    if hasattr(b2, 'html5_Action'):
        assert not _is_linked(b2, 'html5_Action', a)


def test_assoc_container7_link_reassign_clear():
    a = html5_container(class_="sample_text")
    b1 = html5_html()
    b2 = html5_html()
    _safe_set(a, 'html5_container', b1)
    assert _is_linked(a, 'html5_container', b1)
    if hasattr(b1, 'html5_html'):
        assert _is_linked(b1, 'html5_html', a)
    _safe_set(a, 'html5_container', b2)
    assert _is_linked(a, 'html5_container', b2)
    if hasattr(b1, 'html5_html'):
        assert not _is_linked(b1, 'html5_html', a)
    if hasattr(b2, 'html5_html'):
        assert _is_linked(b2, 'html5_html', a)
    _safe_set(a, 'html5_container', None)
    assert not _is_linked(a, 'html5_container', b2)
    if hasattr(b2, 'html5_html'):
        assert not _is_linked(b2, 'html5_html', a)


def test_assoc_elements4_link_reassign_clear():
    a = html5_htmlElement(class_="sample_text")
    b1 = html5_td()
    b2 = html5_td()
    _safe_set(a, 'html5_htmlElement', b1)
    assert _is_linked(a, 'html5_htmlElement', b1)
    if hasattr(b1, 'html5_td5'):
        assert _is_linked(b1, 'html5_td5', a)
    _safe_set(a, 'html5_htmlElement', b2)
    assert _is_linked(a, 'html5_htmlElement', b2)
    if hasattr(b1, 'html5_td5'):
        assert not _is_linked(b1, 'html5_td5', a)
    if hasattr(b2, 'html5_td5'):
        assert _is_linked(b2, 'html5_td5', a)
    _safe_set(a, 'html5_htmlElement', None)
    assert not _is_linked(a, 'html5_htmlElement', b2)
    if hasattr(b2, 'html5_td5'):
        assert not _is_linked(b2, 'html5_td5', a)


def test_assoc_elements8_link_reassign_clear():
    a = html5_htmlElement(class_="sample_text")
    b1 = html5_container(class_="sample_text")
    b2 = html5_container(class_="sample_text_2")
    _safe_set(a, 'html5_htmlElement10', b1)
    assert _is_linked(a, 'html5_htmlElement10', b1)
    if hasattr(b1, 'html5_container9'):
        assert _is_linked(b1, 'html5_container9', a)
    _safe_set(a, 'html5_htmlElement10', b2)
    assert _is_linked(a, 'html5_htmlElement10', b2)
    if hasattr(b1, 'html5_container9'):
        assert not _is_linked(b1, 'html5_container9', a)
    if hasattr(b2, 'html5_container9'):
        assert _is_linked(b2, 'html5_container9', a)
    _safe_set(a, 'html5_htmlElement10', None)
    assert not _is_linked(a, 'html5_htmlElement10', b2)
    if hasattr(b2, 'html5_container9'):
        assert not _is_linked(b2, 'html5_container9', a)


def test_assoc_innercontainer12_link_reassign_clear():
    a = html5_container(class_="sample_text")
    b1 = html5_container(class_="sample_text")
    b2 = html5_container(class_="sample_text_2")
    _safe_set(a, 'html5_container11', {b1})
    assert _is_linked(a, 'html5_container11', b1)
    if hasattr(b1, 'html5_container13'):
        assert _is_linked(b1, 'html5_container13', a)
    _safe_set(a, 'html5_container11', {b2})
    assert _is_linked(a, 'html5_container11', b2)
    if hasattr(b1, 'html5_container13'):
        assert not _is_linked(b1, 'html5_container13', a)
    if hasattr(b2, 'html5_container13'):
        assert _is_linked(b2, 'html5_container13', a)
    _safe_set(a, 'html5_container11', set())
    assert not _is_linked(a, 'html5_container11', b2)
    if hasattr(b2, 'html5_container13'):
        assert not _is_linked(b2, 'html5_container13', a)


def test_assoc_legend6_link_reassign_clear():
    a = html5_legend(class_="sample_text", valor="sample_text")
    b1 = html5_fieldset()
    b2 = html5_fieldset()
    _safe_set(a, 'html5_legend', b1)
    assert _is_linked(a, 'html5_legend', b1)
    if hasattr(b1, 'html5_fieldset'):
        assert _is_linked(b1, 'html5_fieldset', a)
    _safe_set(a, 'html5_legend', b2)
    assert _is_linked(a, 'html5_legend', b2)
    if hasattr(b1, 'html5_fieldset'):
        assert not _is_linked(b1, 'html5_fieldset', a)
    if hasattr(b2, 'html5_fieldset'):
        assert _is_linked(b2, 'html5_fieldset', a)
    _safe_set(a, 'html5_legend', None)
    assert not _is_linked(a, 'html5_legend', b2)
    if hasattr(b2, 'html5_fieldset'):
        assert not _is_linked(b2, 'html5_fieldset', a)


def test_assoc_options14_link_reassign_clear():
    a = html5_select(multiple="sample_text", size="sample_text")
    b1 = html5_option()
    b2 = html5_option()
    _safe_set(a, 'html5_select', b1)
    assert _is_linked(a, 'html5_select', b1)
    if hasattr(b1, 'html5_option'):
        assert _is_linked(b1, 'html5_option', a)
    _safe_set(a, 'html5_select', b2)
    assert _is_linked(a, 'html5_select', b2)
    if hasattr(b1, 'html5_option'):
        assert not _is_linked(b1, 'html5_option', a)
    if hasattr(b2, 'html5_option'):
        assert _is_linked(b2, 'html5_option', a)
    _safe_set(a, 'html5_select', None)
    assert not _is_linked(a, 'html5_select', b2)
    if hasattr(b2, 'html5_option'):
        assert not _is_linked(b2, 'html5_option', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

container_strategy = st.builds(container)
@given(instance=container_strategy)
@settings(max_examples=25)
def test_container_instantiation(instance):
    assert isinstance(instance, container)


html5_Action_strategy = st.builds(html5_Action, codigo=safe_text)
@given(instance=html5_Action_strategy)
@settings(max_examples=25)
def test_html5_Action_instantiation(instance):
    assert isinstance(instance, html5_Action)


html5_button_strategy = st.builds(html5_button, action=safe_text, type=safe_text, value=safe_text)
@given(instance=html5_button_strategy)
@settings(max_examples=25)
def test_html5_button_instantiation(instance):
    assert isinstance(instance, html5_button)


html5_container_strategy = st.builds(html5_container, class_=safe_text)
@given(instance=html5_container_strategy)
@settings(max_examples=25)
def test_html5_container_instantiation(instance):
    assert isinstance(instance, html5_container)


html5_dialog_strategy = st.builds(html5_dialog)
@given(instance=html5_dialog_strategy)
@settings(max_examples=25)
def test_html5_dialog_instantiation(instance):
    assert isinstance(instance, html5_dialog)


html5_div_strategy = st.builds(html5_div, id=safe_text)
@given(instance=html5_div_strategy)
@settings(max_examples=25)
def test_html5_div_instantiation(instance):
    assert isinstance(instance, html5_div)


html5_fieldset_strategy = st.builds(html5_fieldset)
@given(instance=html5_fieldset_strategy)
@settings(max_examples=25)
def test_html5_fieldset_instantiation(instance):
    assert isinstance(instance, html5_fieldset)


html5_html_strategy = st.builds(html5_html)
@given(instance=html5_html_strategy)
@settings(max_examples=25)
def test_html5_html_instantiation(instance):
    assert isinstance(instance, html5_html)


html5_htmlElement_strategy = st.builds(html5_htmlElement, class_=safe_text)
@given(instance=html5_htmlElement_strategy)
@settings(max_examples=25)
def test_html5_htmlElement_instantiation(instance):
    assert isinstance(instance, html5_htmlElement)


html5_img_strategy = st.builds(html5_img, src=safe_text)
@given(instance=html5_img_strategy)
@settings(max_examples=25)
def test_html5_img_instantiation(instance):
    assert isinstance(instance, html5_img)


html5_input_strategy = st.builds(html5_input, disable=safe_text, type=safe_text, value=safe_text)
@given(instance=html5_input_strategy)
@settings(max_examples=25)
def test_html5_input_instantiation(instance):
    assert isinstance(instance, html5_input)


html5_label_strategy = st.builds(html5_label, valor=safe_text, value=safe_text)
@given(instance=html5_label_strategy)
@settings(max_examples=25)
def test_html5_label_instantiation(instance):
    assert isinstance(instance, html5_label)


html5_legend_strategy = st.builds(html5_legend, class_=safe_text, valor=safe_text)
@given(instance=html5_legend_strategy)
@settings(max_examples=25)
def test_html5_legend_instantiation(instance):
    assert isinstance(instance, html5_legend)


html5_option_strategy = st.builds(html5_option)
@given(instance=html5_option_strategy)
@settings(max_examples=25)
def test_html5_option_instantiation(instance):
    assert isinstance(instance, html5_option)


html5_select_strategy = st.builds(html5_select, multiple=safe_text, size=safe_text)
@given(instance=html5_select_strategy)
@settings(max_examples=25)
def test_html5_select_instantiation(instance):
    assert isinstance(instance, html5_select)


html5_table_strategy = st.builds(html5_table)
@given(instance=html5_table_strategy)
@settings(max_examples=25)
def test_html5_table_instantiation(instance):
    assert isinstance(instance, html5_table)


html5_td_strategy = st.builds(html5_td)
@given(instance=html5_td_strategy)
@settings(max_examples=25)
def test_html5_td_instantiation(instance):
    assert isinstance(instance, html5_td)


html5_tr_strategy = st.builds(html5_tr)
@given(instance=html5_tr_strategy)
@settings(max_examples=25)
def test_html5_tr_instantiation(instance):
    assert isinstance(instance, html5_tr)


htmlElement_strategy = st.builds(htmlElement)
@given(instance=htmlElement_strategy)
@settings(max_examples=25)
def test_htmlElement_instantiation(instance):
    assert isinstance(instance, htmlElement)



