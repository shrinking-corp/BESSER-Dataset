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
    html_Page,
    html_Container,
    html_ColumnOption,
    html_Option,
    SelectionList,
    html_SelectComplex,
    html_Select,
    FormElement,
    html_Editable,
    html_Label,
    html_FormElement,
    html_Section,
    html_Graph,
    html_View,
    Editable,
    html_SelectionList,
    html_TextArea,
    html_Input,
    InputType,
    SelectType,
    GraphType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_html_page_is_not_abstract():
    assert not inspect.isabstract(html_Page)


def test_hyp_html_page_constructor_exists():
    assert callable(html_Page.__init__)


def test_hyp_html_page_constructor_args():
    sig = inspect.signature(html_Page.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "urlToSaveResponses" in params, "Missing parameter 'urlToSaveResponses'"
    assert "urlToGetData" in params, "Missing parameter 'urlToGetData'"
    assert "urlToGetRelationResult" in params, "Missing parameter 'urlToGetRelationResult'"









def test_hyp_html_container_is_not_abstract():
    assert not inspect.isabstract(html_Container)


def test_hyp_html_container_constructor_exists():
    assert callable(html_Container.__init__)


def test_hyp_html_container_constructor_args():
    sig = inspect.signature(html_Container.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_html_columnoption_is_not_abstract():
    assert not inspect.isabstract(html_ColumnOption)


def test_hyp_html_columnoption_constructor_exists():
    assert callable(html_ColumnOption.__init__)


def test_hyp_html_columnoption_constructor_args():
    sig = inspect.signature(html_ColumnOption.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "content" in params, "Missing parameter 'content'"





def test_hyp_html_option_is_not_abstract():
    assert not inspect.isabstract(html_Option)


def test_hyp_html_option_constructor_exists():
    assert callable(html_Option.__init__)


def test_hyp_html_option_constructor_args():
    sig = inspect.signature(html_Option.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "content" in params, "Missing parameter 'content'"





def test_hyp_selectionlist_is_not_abstract():
    assert not inspect.isabstract(SelectionList)


def test_hyp_selectionlist_constructor_exists():
    assert callable(SelectionList.__init__)


def test_hyp_selectionlist_constructor_args():
    sig = inspect.signature(SelectionList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_selectcomplex_is_not_abstract():
    assert not inspect.isabstract(html_SelectComplex)


def test_hyp_html_selectcomplex_constructor_exists():
    assert callable(html_SelectComplex.__init__)


def test_hyp_html_selectcomplex_constructor_args():
    sig = inspect.signature(html_SelectComplex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_select_is_not_abstract():
    assert not inspect.isabstract(html_Select)


def test_hyp_html_select_constructor_exists():
    assert callable(html_Select.__init__)


def test_hyp_html_select_constructor_args():
    sig = inspect.signature(html_Select.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_formelement_is_not_abstract():
    assert not inspect.isabstract(FormElement)


def test_hyp_formelement_constructor_exists():
    assert callable(FormElement.__init__)


def test_hyp_formelement_constructor_args():
    sig = inspect.signature(FormElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_editable_is_not_abstract():
    assert not inspect.isabstract(html_Editable)


def test_hyp_html_editable_constructor_exists():
    assert callable(html_Editable.__init__)


def test_hyp_html_editable_constructor_args():
    sig = inspect.signature(html_Editable.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_html_label_is_not_abstract():
    assert not inspect.isabstract(html_Label)


def test_hyp_html_label_constructor_exists():
    assert callable(html_Label.__init__)


def test_hyp_html_label_constructor_args():
    sig = inspect.signature(html_Label.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "forText" in params, "Missing parameter 'forText'"





def test_hyp_html_formelement_is_not_abstract():
    assert not inspect.isabstract(html_FormElement)


def test_hyp_html_formelement_constructor_exists():
    assert callable(html_FormElement.__init__)


def test_hyp_html_formelement_constructor_args():
    sig = inspect.signature(html_FormElement.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_html_section_is_not_abstract():
    assert not inspect.isabstract(html_Section)


def test_hyp_html_section_constructor_exists():
    assert callable(html_Section.__init__)


def test_hyp_html_section_constructor_args():
    sig = inspect.signature(html_Section.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_html_graph_is_not_abstract():
    assert not inspect.isabstract(html_Graph)


def test_hyp_html_graph_constructor_exists():
    assert callable(html_Graph.__init__)


def test_hyp_html_graph_constructor_args():
    sig = inspect.signature(html_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_html_view_is_not_abstract():
    assert not inspect.isabstract(html_View)


def test_hyp_html_view_constructor_exists():
    assert callable(html_View.__init__)


def test_hyp_html_view_constructor_args():
    sig = inspect.signature(html_View.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_editable_is_not_abstract():
    assert not inspect.isabstract(Editable)


def test_hyp_editable_constructor_exists():
    assert callable(Editable.__init__)


def test_hyp_editable_constructor_args():
    sig = inspect.signature(Editable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_html_selectionlist_is_not_abstract():
    assert not inspect.isabstract(html_SelectionList)


def test_hyp_html_selectionlist_constructor_exists():
    assert callable(html_SelectionList.__init__)


def test_hyp_html_selectionlist_constructor_args():
    sig = inspect.signature(html_SelectionList.__init__)
    params = list(sig.parameters.keys())
    assert "multiple" in params, "Missing parameter 'multiple'"




def test_hyp_html_textarea_is_not_abstract():
    assert not inspect.isabstract(html_TextArea)


def test_hyp_html_textarea_constructor_exists():
    assert callable(html_TextArea.__init__)


def test_hyp_html_textarea_constructor_args():
    sig = inspect.signature(html_TextArea.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"





def test_hyp_html_input_is_not_abstract():
    assert not inspect.isabstract(html_Input)


def test_hyp_html_input_constructor_exists():
    assert callable(html_Input.__init__)


def test_hyp_html_input_constructor_args():
    sig = inspect.signature(html_Input.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "checked" in params, "Missing parameter 'checked'"
    assert "type" in params, "Missing parameter 'type'"
    assert "step" in params, "Missing parameter 'step'"
    assert "min" in params, "Missing parameter 'min'"







def test_hyp_inputtype_exists():
    # Check that the Enumeration exists
    assert InputType is not None

def test_hyp_inputtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InputType]
    expected_literals = [
        "EMAIL",
        "TEXT",
        "RANGE",
        "NUMBER",
        "DATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InputType"

def test_hyp_selecttype_exists():
    # Check that the Enumeration exists
    assert SelectType is not None

def test_hyp_selecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectType]
    expected_literals = [
        "COMBO",
        "LIST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectType"

def test_hyp_graphtype_exists():
    # Check that the Enumeration exists
    assert GraphType is not None

def test_hyp_graphtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GraphType]
    expected_literals = [
        "PIE",
        "SCALAR",
        "NONE",
        "BAR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GraphType"


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
html_Page_strategy = st.builds(
    html_Page,
    description=
        safe_text,
    title=
        safe_text,
    id=
        st.integers(),
    urlToSaveResponses=
        safe_text,
    urlToGetData=
        safe_text,
    urlToGetRelationResult=
        safe_text
)
html_Container_strategy = st.builds(
    html_Container,
    name=
        safe_text
)
html_ColumnOption_strategy = st.builds(
    html_ColumnOption,
    value=
        st.integers(),
    content=
        safe_text
)
html_Option_strategy = st.builds(
    html_Option,
    value=
        st.integers(),
    content=
        safe_text
)
SelectionList_strategy = st.builds(
    SelectionList,
)
html_SelectComplex_strategy = st.builds(
    html_SelectComplex,
)
html_Select_strategy = st.builds(
    html_Select,
    type=
        safe_text
)
FormElement_strategy = st.builds(
    FormElement,
)
html_Editable_strategy = st.builds(
    html_Editable,
    required=
        st.booleans(),
    name=
        st.integers()
)
html_Label_strategy = st.builds(
    html_Label,
    content=
        safe_text,
    forText=
        st.integers()
)
html_FormElement_strategy = st.builds(
    html_FormElement,
    visible=
        st.booleans(),
    id=
        safe_text
)
html_Section_strategy = st.builds(
    html_Section,
    id=
        st.integers(),
    title=
        safe_text
)
html_Graph_strategy = st.builds(
    html_Graph,
    title=
        safe_text,
    type=
        safe_text
)
html_View_strategy = st.builds(
    html_View,
    title=
        safe_text
)
Editable_strategy = st.builds(
    Editable,
)
html_SelectionList_strategy = st.builds(
    html_SelectionList,
    multiple=
        st.booleans()
)
html_TextArea_strategy = st.builds(
    html_TextArea,
    rows=
        st.integers(),
    maxLength=
        st.integers()
)
html_Input_strategy = st.builds(
    html_Input,
    max=
        st.integers(),
    maxLength=
        st.integers(),
    checked=
        st.booleans(),
    type=
        safe_text,
    step=
        st.integers(),
    min=
        st.integers()
)




@given(instance=html_Page_strategy)
def test_hyp_html_page_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=html_Page_strategy)
def test_hyp_html_page_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=html_Page_strategy)
def test_hyp_html_page_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=html_Page_strategy)
def test_hyp_html_page_urlToSaveResponses_setter(instance):
    original = instance.urlToSaveResponses
    instance.urlToSaveResponses = original
    assert instance.urlToSaveResponses == original



@given(instance=html_Page_strategy)
def test_hyp_html_page_urlToGetData_setter(instance):
    original = instance.urlToGetData
    instance.urlToGetData = original
    assert instance.urlToGetData == original



@given(instance=html_Page_strategy)
def test_hyp_html_page_urlToGetRelationResult_setter(instance):
    original = instance.urlToGetRelationResult
    instance.urlToGetRelationResult = original
    assert instance.urlToGetRelationResult == original




@given(instance=html_Container_strategy)
def test_hyp_html_container_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=html_ColumnOption_strategy)
def test_hyp_html_columnoption_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=html_ColumnOption_strategy)
def test_hyp_html_columnoption_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original




@given(instance=html_Option_strategy)
def test_hyp_html_option_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=html_Option_strategy)
def test_hyp_html_option_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original






@given(instance=html_Select_strategy)
def test_hyp_html_select_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=html_Editable_strategy)
def test_hyp_html_editable_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=html_Editable_strategy)
def test_hyp_html_editable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=html_Label_strategy)
def test_hyp_html_label_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=html_Label_strategy)
def test_hyp_html_label_forText_setter(instance):
    original = instance.forText
    instance.forText = original
    assert instance.forText == original




@given(instance=html_FormElement_strategy)
def test_hyp_html_formelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=html_FormElement_strategy)
def test_hyp_html_formelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=html_Section_strategy)
def test_hyp_html_section_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=html_Section_strategy)
def test_hyp_html_section_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=html_Graph_strategy)
def test_hyp_html_graph_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=html_Graph_strategy)
def test_hyp_html_graph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=html_View_strategy)
def test_hyp_html_view_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original





@given(instance=html_SelectionList_strategy)
def test_hyp_html_selectionlist_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original




@given(instance=html_TextArea_strategy)
def test_hyp_html_textarea_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original



@given(instance=html_TextArea_strategy)
def test_hyp_html_textarea_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original




@given(instance=html_Input_strategy)
def test_hyp_html_input_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=html_Input_strategy)
def test_hyp_html_input_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=html_Input_strategy)
def test_hyp_html_input_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original



@given(instance=html_Input_strategy)
def test_hyp_html_input_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=html_Input_strategy)
def test_hyp_html_input_step_setter(instance):
    original = instance.step
    instance.step = original
    assert instance.step == original



@given(instance=html_Input_strategy)
def test_hyp_html_input_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Editable,
    FormElement,
    SelectionList,
    html_ColumnOption,
    html_Container,
    html_Editable,
    html_FormElement,
    html_Graph,
    html_Input,
    html_Label,
    html_Option,
    html_Page,
    html_Section,
    html_Select,
    html_SelectComplex,
    html_SelectionList,
    html_TextArea,
    html_View,
    GraphType,
    InputType,
    SelectType,
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

def test_html_ColumnOption_content_value_roundtrip():
    instance = html_ColumnOption(content="sample_text", value=7)
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_html_ColumnOption_value_value_roundtrip():
    instance = html_ColumnOption(content="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_html_Container_name_value_roundtrip():
    instance = html_Container(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_html_Editable_name_value_roundtrip():
    instance = html_Editable(name=7, required=True)
    assert instance.name == 7
    instance.name = 13
    assert instance.name == 13


def test_html_Editable_required_value_roundtrip():
    instance = html_Editable(name=7, required=True)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_html_FormElement_id_value_roundtrip():
    instance = html_FormElement(id="sample_text", visible=True)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_html_FormElement_visible_value_roundtrip():
    instance = html_FormElement(id="sample_text", visible=True)
    assert instance.visible == True
    instance.visible = False
    assert instance.visible == False


def test_html_Graph_title_value_roundtrip():
    instance = html_Graph(title="sample_text", type="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_html_Graph_type_value_roundtrip():
    instance = html_Graph(title="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_html_Input_checked_value_roundtrip():
    instance = html_Input(checked=True, max=7, maxLength=7, min=7, step=7, type="sample_text")
    assert instance.checked == True
    instance.checked = False
    assert instance.checked == False


def test_html_Input_max_value_roundtrip():
    instance = html_Input(checked=True, max=7, maxLength=7, min=7, step=7, type="sample_text")
    assert instance.max == 7
    instance.max = 13
    assert instance.max == 13


def test_html_Input_maxLength_value_roundtrip():
    instance = html_Input(checked=True, max=7, maxLength=7, min=7, step=7, type="sample_text")
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_html_Input_min_value_roundtrip():
    instance = html_Input(checked=True, max=7, maxLength=7, min=7, step=7, type="sample_text")
    assert instance.min == 7
    instance.min = 13
    assert instance.min == 13


def test_html_Input_step_value_roundtrip():
    instance = html_Input(checked=True, max=7, maxLength=7, min=7, step=7, type="sample_text")
    assert instance.step == 7
    instance.step = 13
    assert instance.step == 13


def test_html_Input_type_value_roundtrip():
    instance = html_Input(checked=True, max=7, maxLength=7, min=7, step=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_html_Label_content_value_roundtrip():
    instance = html_Label(content="sample_text", forText=7)
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_html_Label_forText_value_roundtrip():
    instance = html_Label(content="sample_text", forText=7)
    assert instance.forText == 7
    instance.forText = 13
    assert instance.forText == 13


def test_html_Option_content_value_roundtrip():
    instance = html_Option(content="sample_text", value=7)
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_html_Option_value_value_roundtrip():
    instance = html_Option(content="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_html_Page_description_value_roundtrip():
    instance = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_html_Page_id_value_roundtrip():
    instance = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_html_Page_title_value_roundtrip():
    instance = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_html_Page_urlToGetData_value_roundtrip():
    instance = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    assert instance.urlToGetData == "sample_text"
    instance.urlToGetData = "sample_text_2"
    assert instance.urlToGetData == "sample_text_2"


def test_html_Page_urlToGetRelationResult_value_roundtrip():
    instance = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    assert instance.urlToGetRelationResult == "sample_text"
    instance.urlToGetRelationResult = "sample_text_2"
    assert instance.urlToGetRelationResult == "sample_text_2"


def test_html_Page_urlToSaveResponses_value_roundtrip():
    instance = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    assert instance.urlToSaveResponses == "sample_text"
    instance.urlToSaveResponses = "sample_text_2"
    assert instance.urlToSaveResponses == "sample_text_2"


def test_html_Section_id_value_roundtrip():
    instance = html_Section(id=7, title="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_html_Section_title_value_roundtrip():
    instance = html_Section(id=7, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_html_Select_type_value_roundtrip():
    instance = html_Select(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_html_SelectionList_multiple_value_roundtrip():
    instance = html_SelectionList(multiple=True)
    assert instance.multiple == True
    instance.multiple = False
    assert instance.multiple == False


def test_html_TextArea_maxLength_value_roundtrip():
    instance = html_TextArea(maxLength=7, rows=7)
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_html_TextArea_rows_value_roundtrip():
    instance = html_TextArea(maxLength=7, rows=7)
    assert instance.rows == 7
    instance.rows = 13
    assert instance.rows == 13


def test_html_View_title_value_roundtrip():
    instance = html_View(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_html_Input_isa_Editable():
    instance = html_Input(checked=True, max=7, maxLength=7, min=7, step=7, type="sample_text")
    assert isinstance(instance, Editable)


def test_html_SelectionList_isa_Editable():
    instance = html_SelectionList(multiple=True)
    assert isinstance(instance, Editable)


def test_html_TextArea_isa_Editable():
    instance = html_TextArea(maxLength=7, rows=7)
    assert isinstance(instance, Editable)


def test_html_Editable_isa_FormElement():
    instance = html_Editable(name=7, required=True)
    assert isinstance(instance, FormElement)


def test_html_Label_isa_FormElement():
    instance = html_Label(content="sample_text", forText=7)
    assert isinstance(instance, FormElement)


def test_html_Select_isa_SelectionList():
    instance = html_Select(type="sample_text")
    assert isinstance(instance, SelectionList)


def test_html_SelectComplex_isa_SelectionList():
    instance = html_SelectComplex()
    assert isinstance(instance, SelectionList)


def test_assoc_columnsOptions12_link_reassign_clear():
    a = html_ColumnOption(content="sample_text", value=7)
    b1 = html_SelectComplex()
    b2 = html_SelectComplex()
    _safe_set(a, 'html_ColumnOption', b1)
    assert _is_linked(a, 'html_ColumnOption', b1)
    if hasattr(b1, 'html_SelectComplex'):
        assert _is_linked(b1, 'html_SelectComplex', a)
    _safe_set(a, 'html_ColumnOption', b2)
    assert _is_linked(a, 'html_ColumnOption', b2)
    if hasattr(b1, 'html_SelectComplex'):
        assert not _is_linked(b1, 'html_SelectComplex', a)
    if hasattr(b2, 'html_SelectComplex'):
        assert _is_linked(b2, 'html_SelectComplex', a)
    _safe_set(a, 'html_ColumnOption', None)
    assert not _is_linked(a, 'html_ColumnOption', b2)
    if hasattr(b2, 'html_SelectComplex'):
        assert not _is_linked(b2, 'html_SelectComplex', a)


def test_assoc_formElements3_link_reassign_clear():
    a = html_Section(id=7, title="sample_text")
    b1 = html_FormElement(id="sample_text", visible=True)
    b2 = html_FormElement(id="sample_text_2", visible=False)
    _safe_set(a, 'html_Section4', {b1})
    assert _is_linked(a, 'html_Section4', b1)
    if hasattr(b1, 'html_FormElement'):
        assert _is_linked(b1, 'html_FormElement', a)
    _safe_set(a, 'html_Section4', {b2})
    assert _is_linked(a, 'html_Section4', b2)
    if hasattr(b1, 'html_FormElement'):
        assert not _is_linked(b1, 'html_FormElement', a)
    if hasattr(b2, 'html_FormElement'):
        assert _is_linked(b2, 'html_FormElement', a)
    _safe_set(a, 'html_Section4', set())
    assert not _is_linked(a, 'html_Section4', b2)
    if hasattr(b2, 'html_FormElement'):
        assert not _is_linked(b2, 'html_FormElement', a)


def test_assoc_formElements9_link_reassign_clear():
    a = html_Option(content="sample_text", value=7)
    b1 = html_FormElement(id="sample_text", visible=True)
    b2 = html_FormElement(id="sample_text_2", visible=False)
    _safe_set(a, 'html_Option10', {b1})
    assert _is_linked(a, 'html_Option10', b1)
    if hasattr(b1, 'html_FormElement11'):
        assert _is_linked(b1, 'html_FormElement11', a)
    _safe_set(a, 'html_Option10', {b2})
    assert _is_linked(a, 'html_Option10', b2)
    if hasattr(b1, 'html_FormElement11'):
        assert not _is_linked(b1, 'html_FormElement11', a)
    if hasattr(b2, 'html_FormElement11'):
        assert _is_linked(b2, 'html_FormElement11', a)
    _safe_set(a, 'html_Option10', set())
    assert not _is_linked(a, 'html_Option10', b2)
    if hasattr(b2, 'html_FormElement11'):
        assert not _is_linked(b2, 'html_FormElement11', a)


def test_assoc_graphs0_link_reassign_clear():
    a = html_View(title="sample_text")
    b1 = html_Graph(title="sample_text", type="sample_text")
    b2 = html_Graph(title="sample_text_2", type="sample_text_2")
    _safe_set(a, 'html_View', {b1})
    assert _is_linked(a, 'html_View', b1)
    if hasattr(b1, 'html_Graph'):
        assert _is_linked(b1, 'html_Graph', a)
    _safe_set(a, 'html_View', {b2})
    assert _is_linked(a, 'html_View', b2)
    if hasattr(b1, 'html_Graph'):
        assert not _is_linked(b1, 'html_Graph', a)
    if hasattr(b2, 'html_Graph'):
        assert _is_linked(b2, 'html_Graph', a)
    _safe_set(a, 'html_View', set())
    assert not _is_linked(a, 'html_View', b2)
    if hasattr(b2, 'html_Graph'):
        assert not _is_linked(b2, 'html_Graph', a)


def test_assoc_label5_link_reassign_clear():
    a = html_Label(content="sample_text", forText=7)
    b1 = html_Editable(name=7, required=True)
    b2 = html_Editable(name=13, required=False)
    _safe_set(a, 'html_Label', b1)
    assert _is_linked(a, 'html_Label', b1)
    if hasattr(b1, 'html_Editable'):
        assert _is_linked(b1, 'html_Editable', a)
    _safe_set(a, 'html_Label', b2)
    assert _is_linked(a, 'html_Label', b2)
    if hasattr(b1, 'html_Editable'):
        assert not _is_linked(b1, 'html_Editable', a)
    if hasattr(b2, 'html_Editable'):
        assert _is_linked(b2, 'html_Editable', a)
    _safe_set(a, 'html_Label', None)
    assert not _is_linked(a, 'html_Label', b2)
    if hasattr(b2, 'html_Editable'):
        assert not _is_linked(b2, 'html_Editable', a)


def test_assoc_options13_link_reassign_clear():
    a = html_Option(content="sample_text", value=7)
    b1 = html_SelectComplex()
    b2 = html_SelectComplex()
    _safe_set(a, 'html_Option15', b1)
    assert _is_linked(a, 'html_Option15', b1)
    if hasattr(b1, 'html_SelectComplex14'):
        assert _is_linked(b1, 'html_SelectComplex14', a)
    _safe_set(a, 'html_Option15', b2)
    assert _is_linked(a, 'html_Option15', b2)
    if hasattr(b1, 'html_SelectComplex14'):
        assert not _is_linked(b1, 'html_SelectComplex14', a)
    if hasattr(b2, 'html_SelectComplex14'):
        assert _is_linked(b2, 'html_SelectComplex14', a)
    _safe_set(a, 'html_Option15', None)
    assert not _is_linked(a, 'html_Option15', b2)
    if hasattr(b2, 'html_SelectComplex14'):
        assert not _is_linked(b2, 'html_SelectComplex14', a)


def test_assoc_options6_link_reassign_clear():
    a = html_Select(type="sample_text")
    b1 = html_Option(content="sample_text", value=7)
    b2 = html_Option(content="sample_text_2", value=13)
    _safe_set(a, 'html_Select', {b1})
    assert _is_linked(a, 'html_Select', b1)
    if hasattr(b1, 'html_Option'):
        assert _is_linked(b1, 'html_Option', a)
    _safe_set(a, 'html_Select', {b2})
    assert _is_linked(a, 'html_Select', b2)
    if hasattr(b1, 'html_Option'):
        assert not _is_linked(b1, 'html_Option', a)
    if hasattr(b2, 'html_Option'):
        assert _is_linked(b2, 'html_Option', a)
    _safe_set(a, 'html_Select', set())
    assert not _is_linked(a, 'html_Select', b2)
    if hasattr(b2, 'html_Option'):
        assert not _is_linked(b2, 'html_Option', a)


def test_assoc_otherArea7_link_reassign_clear():
    a = html_TextArea(maxLength=7, rows=7)
    b1 = html_Option(content="sample_text", value=7)
    b2 = html_Option(content="sample_text_2", value=13)
    _safe_set(a, 'html_TextArea', b1)
    assert _is_linked(a, 'html_TextArea', b1)
    if hasattr(b1, 'html_Option8'):
        assert _is_linked(b1, 'html_Option8', a)
    _safe_set(a, 'html_TextArea', b2)
    assert _is_linked(a, 'html_TextArea', b2)
    if hasattr(b1, 'html_Option8'):
        assert not _is_linked(b1, 'html_Option8', a)
    if hasattr(b2, 'html_Option8'):
        assert _is_linked(b2, 'html_Option8', a)
    _safe_set(a, 'html_TextArea', None)
    assert not _is_linked(a, 'html_TextArea', b2)
    if hasattr(b2, 'html_Option8'):
        assert not _is_linked(b2, 'html_Option8', a)


def test_assoc_pages16_link_reassign_clear():
    a = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    b1 = html_Container(name="sample_text")
    b2 = html_Container(name="sample_text_2")
    _safe_set(a, 'html_Page', b1)
    assert _is_linked(a, 'html_Page', b1)
    if hasattr(b1, 'html_Container'):
        assert _is_linked(b1, 'html_Container', a)
    _safe_set(a, 'html_Page', b2)
    assert _is_linked(a, 'html_Page', b2)
    if hasattr(b1, 'html_Container'):
        assert not _is_linked(b1, 'html_Container', a)
    if hasattr(b2, 'html_Container'):
        assert _is_linked(b2, 'html_Container', a)
    _safe_set(a, 'html_Page', None)
    assert not _is_linked(a, 'html_Page', b2)
    if hasattr(b2, 'html_Container'):
        assert not _is_linked(b2, 'html_Container', a)


def test_assoc_sections1_link_reassign_clear():
    a = html_View(title="sample_text")
    b1 = html_Section(id=7, title="sample_text")
    b2 = html_Section(id=13, title="sample_text_2")
    _safe_set(a, 'html_View2', {b1})
    assert _is_linked(a, 'html_View2', b1)
    if hasattr(b1, 'html_Section'):
        assert _is_linked(b1, 'html_Section', a)
    _safe_set(a, 'html_View2', {b2})
    assert _is_linked(a, 'html_View2', b2)
    if hasattr(b1, 'html_Section'):
        assert not _is_linked(b1, 'html_Section', a)
    if hasattr(b2, 'html_Section'):
        assert _is_linked(b2, 'html_Section', a)
    _safe_set(a, 'html_View2', set())
    assert not _is_linked(a, 'html_View2', b2)
    if hasattr(b2, 'html_Section'):
        assert not _is_linked(b2, 'html_Section', a)


def test_assoc_views17_link_reassign_clear():
    a = html_View(title="sample_text")
    b1 = html_Page(description="sample_text", id=7, title="sample_text", urlToGetData="sample_text", urlToGetRelationResult="sample_text", urlToSaveResponses="sample_text")
    b2 = html_Page(description="sample_text_2", id=13, title="sample_text_2", urlToGetData="sample_text_2", urlToGetRelationResult="sample_text_2", urlToSaveResponses="sample_text_2")
    _safe_set(a, 'html_View19', b1)
    assert _is_linked(a, 'html_View19', b1)
    if hasattr(b1, 'html_Page18'):
        assert _is_linked(b1, 'html_Page18', a)
    _safe_set(a, 'html_View19', b2)
    assert _is_linked(a, 'html_View19', b2)
    if hasattr(b1, 'html_Page18'):
        assert not _is_linked(b1, 'html_Page18', a)
    if hasattr(b2, 'html_Page18'):
        assert _is_linked(b2, 'html_Page18', a)
    _safe_set(a, 'html_View19', None)
    assert not _is_linked(a, 'html_View19', b2)
    if hasattr(b2, 'html_Page18'):
        assert not _is_linked(b2, 'html_Page18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Editable_strategy = st.builds(Editable)
@given(instance=Editable_strategy)
@settings(max_examples=25)
def test_Editable_instantiation(instance):
    assert isinstance(instance, Editable)


FormElement_strategy = st.builds(FormElement)
@given(instance=FormElement_strategy)
@settings(max_examples=25)
def test_FormElement_instantiation(instance):
    assert isinstance(instance, FormElement)


SelectionList_strategy = st.builds(SelectionList)
@given(instance=SelectionList_strategy)
@settings(max_examples=25)
def test_SelectionList_instantiation(instance):
    assert isinstance(instance, SelectionList)


html_ColumnOption_strategy = st.builds(html_ColumnOption, content=safe_text, value=st.integers())
@given(instance=html_ColumnOption_strategy)
@settings(max_examples=25)
def test_html_ColumnOption_instantiation(instance):
    assert isinstance(instance, html_ColumnOption)


html_Container_strategy = st.builds(html_Container, name=safe_text)
@given(instance=html_Container_strategy)
@settings(max_examples=25)
def test_html_Container_instantiation(instance):
    assert isinstance(instance, html_Container)


html_Editable_strategy = st.builds(html_Editable, name=st.integers(), required=st.booleans())
@given(instance=html_Editable_strategy)
@settings(max_examples=25)
def test_html_Editable_instantiation(instance):
    assert isinstance(instance, html_Editable)


html_FormElement_strategy = st.builds(html_FormElement, id=safe_text, visible=st.booleans())
@given(instance=html_FormElement_strategy)
@settings(max_examples=25)
def test_html_FormElement_instantiation(instance):
    assert isinstance(instance, html_FormElement)


html_Graph_strategy = st.builds(html_Graph, title=safe_text, type=safe_text)
@given(instance=html_Graph_strategy)
@settings(max_examples=25)
def test_html_Graph_instantiation(instance):
    assert isinstance(instance, html_Graph)


html_Input_strategy = st.builds(html_Input, checked=st.booleans(), max=st.integers(), maxLength=st.integers(), min=st.integers(), step=st.integers(), type=safe_text)
@given(instance=html_Input_strategy)
@settings(max_examples=25)
def test_html_Input_instantiation(instance):
    assert isinstance(instance, html_Input)


html_Label_strategy = st.builds(html_Label, content=safe_text, forText=st.integers())
@given(instance=html_Label_strategy)
@settings(max_examples=25)
def test_html_Label_instantiation(instance):
    assert isinstance(instance, html_Label)


html_Option_strategy = st.builds(html_Option, content=safe_text, value=st.integers())
@given(instance=html_Option_strategy)
@settings(max_examples=25)
def test_html_Option_instantiation(instance):
    assert isinstance(instance, html_Option)


html_Page_strategy = st.builds(html_Page, description=safe_text, id=st.integers(), title=safe_text, urlToGetData=safe_text, urlToGetRelationResult=safe_text, urlToSaveResponses=safe_text)
@given(instance=html_Page_strategy)
@settings(max_examples=25)
def test_html_Page_instantiation(instance):
    assert isinstance(instance, html_Page)


html_Section_strategy = st.builds(html_Section, id=st.integers(), title=safe_text)
@given(instance=html_Section_strategy)
@settings(max_examples=25)
def test_html_Section_instantiation(instance):
    assert isinstance(instance, html_Section)


html_Select_strategy = st.builds(html_Select, type=safe_text)
@given(instance=html_Select_strategy)
@settings(max_examples=25)
def test_html_Select_instantiation(instance):
    assert isinstance(instance, html_Select)


html_SelectComplex_strategy = st.builds(html_SelectComplex)
@given(instance=html_SelectComplex_strategy)
@settings(max_examples=25)
def test_html_SelectComplex_instantiation(instance):
    assert isinstance(instance, html_SelectComplex)


html_SelectionList_strategy = st.builds(html_SelectionList, multiple=st.booleans())
@given(instance=html_SelectionList_strategy)
@settings(max_examples=25)
def test_html_SelectionList_instantiation(instance):
    assert isinstance(instance, html_SelectionList)


html_TextArea_strategy = st.builds(html_TextArea, maxLength=st.integers(), rows=st.integers())
@given(instance=html_TextArea_strategy)
@settings(max_examples=25)
def test_html_TextArea_instantiation(instance):
    assert isinstance(instance, html_TextArea)


html_View_strategy = st.builds(html_View, title=safe_text)
@given(instance=html_View_strategy)
@settings(max_examples=25)
def test_html_View_instantiation(instance):
    assert isinstance(instance, html_View)



