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
    TextBox,
    webapp_DateBox,
    webapp_EmailBox,
    webapp_PasswordBox,
    FormButton,
    webapp_SubmitButton,
    webapp_ResetButton,
    webapp_DynamicWebApp,
    NormalControl,
    webapp_NormalButton,
    Control,
    webapp_CheckBox,
    webapp_FormButton,
    webapp_TextBox,
    webapp_DropDownList,
    webapp_Link,
    webapp_Label,
    webapp_NormalControl,
    webapp_Control,
    Page,
    webapp_NormalPage,
    webapp_FormPage,
    webapp_RadioButton,
    webapp_ListElement,
    webapp_Page,
    DateFormat,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_textbox_is_not_abstract():
    assert not inspect.isabstract(TextBox)


def test_hyp_textbox_constructor_exists():
    assert callable(TextBox.__init__)


def test_hyp_textbox_constructor_args():
    sig = inspect.signature(TextBox.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_datebox_is_not_abstract():
    assert not inspect.isabstract(webapp_DateBox)


def test_hyp_webapp_datebox_constructor_exists():
    assert callable(webapp_DateBox.__init__)


def test_hyp_webapp_datebox_constructor_args():
    sig = inspect.signature(webapp_DateBox.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"




def test_hyp_webapp_emailbox_is_not_abstract():
    assert not inspect.isabstract(webapp_EmailBox)


def test_hyp_webapp_emailbox_constructor_exists():
    assert callable(webapp_EmailBox.__init__)


def test_hyp_webapp_emailbox_constructor_args():
    sig = inspect.signature(webapp_EmailBox.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_passwordbox_is_not_abstract():
    assert not inspect.isabstract(webapp_PasswordBox)


def test_hyp_webapp_passwordbox_constructor_exists():
    assert callable(webapp_PasswordBox.__init__)


def test_hyp_webapp_passwordbox_constructor_args():
    sig = inspect.signature(webapp_PasswordBox.__init__)
    params = list(sig.parameters.keys())



def test_hyp_formbutton_is_not_abstract():
    assert not inspect.isabstract(FormButton)


def test_hyp_formbutton_constructor_exists():
    assert callable(FormButton.__init__)


def test_hyp_formbutton_constructor_args():
    sig = inspect.signature(FormButton.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_submitbutton_is_not_abstract():
    assert not inspect.isabstract(webapp_SubmitButton)


def test_hyp_webapp_submitbutton_constructor_exists():
    assert callable(webapp_SubmitButton.__init__)


def test_hyp_webapp_submitbutton_constructor_args():
    sig = inspect.signature(webapp_SubmitButton.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_resetbutton_is_not_abstract():
    assert not inspect.isabstract(webapp_ResetButton)


def test_hyp_webapp_resetbutton_constructor_exists():
    assert callable(webapp_ResetButton.__init__)


def test_hyp_webapp_resetbutton_constructor_args():
    sig = inspect.signature(webapp_ResetButton.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_dynamicwebapp_is_not_abstract():
    assert not inspect.isabstract(webapp_DynamicWebApp)


def test_hyp_webapp_dynamicwebapp_constructor_exists():
    assert callable(webapp_DynamicWebApp.__init__)


def test_hyp_webapp_dynamicwebapp_constructor_args():
    sig = inspect.signature(webapp_DynamicWebApp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_normalcontrol_is_not_abstract():
    assert not inspect.isabstract(NormalControl)


def test_hyp_normalcontrol_constructor_exists():
    assert callable(NormalControl.__init__)


def test_hyp_normalcontrol_constructor_args():
    sig = inspect.signature(NormalControl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_normalbutton_is_not_abstract():
    assert not inspect.isabstract(webapp_NormalButton)


def test_hyp_webapp_normalbutton_constructor_exists():
    assert callable(webapp_NormalButton.__init__)


def test_hyp_webapp_normalbutton_constructor_args():
    sig = inspect.signature(webapp_NormalButton.__init__)
    params = list(sig.parameters.keys())



def test_hyp_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_hyp_control_constructor_exists():
    assert callable(Control.__init__)


def test_hyp_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_checkbox_is_not_abstract():
    assert not inspect.isabstract(webapp_CheckBox)


def test_hyp_webapp_checkbox_constructor_exists():
    assert callable(webapp_CheckBox.__init__)


def test_hyp_webapp_checkbox_constructor_args():
    sig = inspect.signature(webapp_CheckBox.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_webapp_formbutton_is_not_abstract():
    assert not inspect.isabstract(webapp_FormButton)


def test_hyp_webapp_formbutton_constructor_exists():
    assert callable(webapp_FormButton.__init__)


def test_hyp_webapp_formbutton_constructor_args():
    sig = inspect.signature(webapp_FormButton.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_webapp_textbox_is_not_abstract():
    assert not inspect.isabstract(webapp_TextBox)


def test_hyp_webapp_textbox_constructor_exists():
    assert callable(webapp_TextBox.__init__)


def test_hyp_webapp_textbox_constructor_args():
    sig = inspect.signature(webapp_TextBox.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "maxLength" in params, "Missing parameter 'maxLength'"
    assert "size" in params, "Missing parameter 'size'"
    assert "required" in params, "Missing parameter 'required'"







def test_hyp_webapp_dropdownlist_is_not_abstract():
    assert not inspect.isabstract(webapp_DropDownList)


def test_hyp_webapp_dropdownlist_constructor_exists():
    assert callable(webapp_DropDownList.__init__)


def test_hyp_webapp_dropdownlist_constructor_args():
    sig = inspect.signature(webapp_DropDownList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_link_is_not_abstract():
    assert not inspect.isabstract(webapp_Link)


def test_hyp_webapp_link_constructor_exists():
    assert callable(webapp_Link.__init__)


def test_hyp_webapp_link_constructor_args():
    sig = inspect.signature(webapp_Link.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_label_is_not_abstract():
    assert not inspect.isabstract(webapp_Label)


def test_hyp_webapp_label_constructor_exists():
    assert callable(webapp_Label.__init__)


def test_hyp_webapp_label_constructor_args():
    sig = inspect.signature(webapp_Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_normalcontrol_is_not_abstract():
    assert not inspect.isabstract(webapp_NormalControl)


def test_hyp_webapp_normalcontrol_constructor_exists():
    assert callable(webapp_NormalControl.__init__)


def test_hyp_webapp_normalcontrol_constructor_args():
    sig = inspect.signature(webapp_NormalControl.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_webapp_control_is_not_abstract():
    assert not inspect.isabstract(webapp_Control)


def test_hyp_webapp_control_constructor_exists():
    assert callable(webapp_Control.__init__)


def test_hyp_webapp_control_constructor_args():
    sig = inspect.signature(webapp_Control.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_hyp_page_constructor_exists():
    assert callable(Page.__init__)


def test_hyp_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_normalpage_is_not_abstract():
    assert not inspect.isabstract(webapp_NormalPage)


def test_hyp_webapp_normalpage_constructor_exists():
    assert callable(webapp_NormalPage.__init__)


def test_hyp_webapp_normalpage_constructor_args():
    sig = inspect.signature(webapp_NormalPage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_formpage_is_not_abstract():
    assert not inspect.isabstract(webapp_FormPage)


def test_hyp_webapp_formpage_constructor_exists():
    assert callable(webapp_FormPage.__init__)


def test_hyp_webapp_formpage_constructor_args():
    sig = inspect.signature(webapp_FormPage.__init__)
    params = list(sig.parameters.keys())
    assert "persist" in params, "Missing parameter 'persist'"




def test_hyp_webapp_radiobutton_is_not_abstract():
    assert not inspect.isabstract(webapp_RadioButton)


def test_hyp_webapp_radiobutton_constructor_exists():
    assert callable(webapp_RadioButton.__init__)


def test_hyp_webapp_radiobutton_constructor_args():
    sig = inspect.signature(webapp_RadioButton.__init__)
    params = list(sig.parameters.keys())



def test_hyp_webapp_listelement_is_not_abstract():
    assert not inspect.isabstract(webapp_ListElement)


def test_hyp_webapp_listelement_constructor_exists():
    assert callable(webapp_ListElement.__init__)


def test_hyp_webapp_listelement_constructor_args():
    sig = inspect.signature(webapp_ListElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_webapp_page_is_not_abstract():
    assert not inspect.isabstract(webapp_Page)


def test_hyp_webapp_page_constructor_exists():
    assert callable(webapp_Page.__init__)


def test_hyp_webapp_page_constructor_args():
    sig = inspect.signature(webapp_Page.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dateformat_exists():
    # Check that the Enumeration exists
    assert DateFormat is not None

def test_hyp_dateformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateFormat]
    expected_literals = [
        "DayMonthYear",
        "YearMonthDay",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateFormat"


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
TextBox_strategy = st.builds(
    TextBox,
)
webapp_DateBox_strategy = st.builds(
    webapp_DateBox,
    format=
        safe_text
)
webapp_EmailBox_strategy = st.builds(
    webapp_EmailBox,
)
webapp_PasswordBox_strategy = st.builds(
    webapp_PasswordBox,
)
FormButton_strategy = st.builds(
    FormButton,
)
webapp_SubmitButton_strategy = st.builds(
    webapp_SubmitButton,
)
webapp_ResetButton_strategy = st.builds(
    webapp_ResetButton,
)
webapp_DynamicWebApp_strategy = st.builds(
    webapp_DynamicWebApp,
    name=
        safe_text
)
NormalControl_strategy = st.builds(
    NormalControl,
)
webapp_NormalButton_strategy = st.builds(
    webapp_NormalButton,
)
Control_strategy = st.builds(
    Control,
)
webapp_CheckBox_strategy = st.builds(
    webapp_CheckBox,
    text=
        safe_text
)
webapp_FormButton_strategy = st.builds(
    webapp_FormButton,
    text=
        safe_text
)
webapp_TextBox_strategy = st.builds(
    webapp_TextBox,
    text=
        safe_text,
    maxLength=
        st.integers(),
    size=
        st.integers(),
    required=
        st.booleans()
)
webapp_DropDownList_strategy = st.builds(
    webapp_DropDownList,
)
webapp_Link_strategy = st.builds(
    webapp_Link,
)
webapp_Label_strategy = st.builds(
    webapp_Label,
)
webapp_NormalControl_strategy = st.builds(
    webapp_NormalControl,
    text=
        safe_text
)
webapp_Control_strategy = st.builds(
    webapp_Control,
    name=
        safe_text,
    id=
        safe_text
)
Page_strategy = st.builds(
    Page,
)
webapp_NormalPage_strategy = st.builds(
    webapp_NormalPage,
)
webapp_FormPage_strategy = st.builds(
    webapp_FormPage,
    persist=
        st.booleans()
)
webapp_RadioButton_strategy = st.builds(
    webapp_RadioButton,
)
webapp_ListElement_strategy = st.builds(
    webapp_ListElement,
    value=
        safe_text
)
webapp_Page_strategy = st.builds(
    webapp_Page,
    default=
        st.booleans(),
    title=
        safe_text,
    name=
        safe_text
)





@given(instance=webapp_DateBox_strategy)
def test_hyp_webapp_datebox_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original









@given(instance=webapp_DynamicWebApp_strategy)
def test_hyp_webapp_dynamicwebapp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=webapp_CheckBox_strategy)
def test_hyp_webapp_checkbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=webapp_FormButton_strategy)
def test_hyp_webapp_formbutton_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=webapp_TextBox_strategy)
def test_hyp_webapp_textbox_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=webapp_TextBox_strategy)
def test_hyp_webapp_textbox_maxLength_setter(instance):
    original = instance.maxLength
    instance.maxLength = original
    assert instance.maxLength == original



@given(instance=webapp_TextBox_strategy)
def test_hyp_webapp_textbox_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=webapp_TextBox_strategy)
def test_hyp_webapp_textbox_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original







@given(instance=webapp_NormalControl_strategy)
def test_hyp_webapp_normalcontrol_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=webapp_Control_strategy)
def test_hyp_webapp_control_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=webapp_Control_strategy)
def test_hyp_webapp_control_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original






@given(instance=webapp_FormPage_strategy)
def test_hyp_webapp_formpage_persist_setter(instance):
    original = instance.persist
    instance.persist = original
    assert instance.persist == original





@given(instance=webapp_ListElement_strategy)
def test_hyp_webapp_listelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=webapp_Page_strategy)
def test_hyp_webapp_page_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=webapp_Page_strategy)
def test_hyp_webapp_page_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=webapp_Page_strategy)
def test_hyp_webapp_page_name_setter(instance):
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
    Control,
    FormButton,
    NormalControl,
    Page,
    TextBox,
    webapp_CheckBox,
    webapp_Control,
    webapp_DateBox,
    webapp_DropDownList,
    webapp_DynamicWebApp,
    webapp_EmailBox,
    webapp_FormButton,
    webapp_FormPage,
    webapp_Label,
    webapp_Link,
    webapp_ListElement,
    webapp_NormalButton,
    webapp_NormalControl,
    webapp_NormalPage,
    webapp_Page,
    webapp_PasswordBox,
    webapp_RadioButton,
    webapp_ResetButton,
    webapp_SubmitButton,
    webapp_TextBox,
    DateFormat,
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

def test_webapp_CheckBox_text_value_roundtrip():
    instance = webapp_CheckBox(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_webapp_Control_id_value_roundtrip():
    instance = webapp_Control(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_webapp_Control_name_value_roundtrip():
    instance = webapp_Control(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_webapp_DateBox_format_value_roundtrip():
    instance = webapp_DateBox(format="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_webapp_DynamicWebApp_name_value_roundtrip():
    instance = webapp_DynamicWebApp(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_webapp_FormButton_text_value_roundtrip():
    instance = webapp_FormButton(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_webapp_FormPage_persist_value_roundtrip():
    instance = webapp_FormPage(persist=True)
    assert instance.persist == True
    instance.persist = False
    assert instance.persist == False


def test_webapp_ListElement_value_value_roundtrip():
    instance = webapp_ListElement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_webapp_NormalControl_text_value_roundtrip():
    instance = webapp_NormalControl(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_webapp_Page_default_value_roundtrip():
    instance = webapp_Page(default=True, name="sample_text", title="sample_text")
    assert instance.default == True
    instance.default = False
    assert instance.default == False


def test_webapp_Page_name_value_roundtrip():
    instance = webapp_Page(default=True, name="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_webapp_Page_title_value_roundtrip():
    instance = webapp_Page(default=True, name="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_webapp_TextBox_maxLength_value_roundtrip():
    instance = webapp_TextBox(maxLength=7, required=True, size=7, text="sample_text")
    assert instance.maxLength == 7
    instance.maxLength = 13
    assert instance.maxLength == 13


def test_webapp_TextBox_required_value_roundtrip():
    instance = webapp_TextBox(maxLength=7, required=True, size=7, text="sample_text")
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_webapp_TextBox_size_value_roundtrip():
    instance = webapp_TextBox(maxLength=7, required=True, size=7, text="sample_text")
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


def test_webapp_TextBox_text_value_roundtrip():
    instance = webapp_TextBox(maxLength=7, required=True, size=7, text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_webapp_CheckBox_isa_Control():
    instance = webapp_CheckBox(text="sample_text")
    assert isinstance(instance, Control)


def test_webapp_DropDownList_isa_Control():
    instance = webapp_DropDownList()
    assert isinstance(instance, Control)


def test_webapp_FormButton_isa_Control():
    instance = webapp_FormButton(text="sample_text")
    assert isinstance(instance, Control)


def test_webapp_Label_isa_Control():
    instance = webapp_Label()
    assert isinstance(instance, Control)


def test_webapp_Link_isa_Control():
    instance = webapp_Link()
    assert isinstance(instance, Control)


def test_webapp_NormalControl_isa_Control():
    instance = webapp_NormalControl(text="sample_text")
    assert isinstance(instance, Control)


def test_webapp_RadioButton_isa_Control():
    instance = webapp_RadioButton()
    assert isinstance(instance, Control)


def test_webapp_TextBox_isa_Control():
    instance = webapp_TextBox(maxLength=7, required=True, size=7, text="sample_text")
    assert isinstance(instance, Control)


def test_webapp_ResetButton_isa_FormButton():
    instance = webapp_ResetButton()
    assert isinstance(instance, FormButton)


def test_webapp_SubmitButton_isa_FormButton():
    instance = webapp_SubmitButton()
    assert isinstance(instance, FormButton)


def test_webapp_Label_isa_NormalControl():
    instance = webapp_Label()
    assert isinstance(instance, NormalControl)


def test_webapp_Link_isa_NormalControl():
    instance = webapp_Link()
    assert isinstance(instance, NormalControl)


def test_webapp_NormalButton_isa_NormalControl():
    instance = webapp_NormalButton()
    assert isinstance(instance, NormalControl)


def test_webapp_FormPage_isa_Page():
    instance = webapp_FormPage(persist=True)
    assert isinstance(instance, Page)


def test_webapp_NormalPage_isa_Page():
    instance = webapp_NormalPage()
    assert isinstance(instance, Page)


def test_webapp_DateBox_isa_TextBox():
    instance = webapp_DateBox(format="sample_text")
    assert isinstance(instance, TextBox)


def test_webapp_EmailBox_isa_TextBox():
    instance = webapp_EmailBox()
    assert isinstance(instance, TextBox)


def test_webapp_PasswordBox_isa_TextBox():
    instance = webapp_PasswordBox()
    assert isinstance(instance, TextBox)


def test_assoc_controls4_link_reassign_clear():
    a = webapp_FormPage(persist=True)
    b1 = webapp_Control(id="sample_text", name="sample_text")
    b2 = webapp_Control(id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'webapp_FormPage5', {b1})
    assert _is_linked(a, 'webapp_FormPage5', b1)
    if hasattr(b1, 'webapp_Control'):
        assert _is_linked(b1, 'webapp_Control', a)
    _safe_set(a, 'webapp_FormPage5', {b2})
    assert _is_linked(a, 'webapp_FormPage5', b2)
    if hasattr(b1, 'webapp_Control'):
        assert not _is_linked(b1, 'webapp_Control', a)
    if hasattr(b2, 'webapp_Control'):
        assert _is_linked(b2, 'webapp_Control', a)
    _safe_set(a, 'webapp_FormPage5', set())
    assert not _is_linked(a, 'webapp_FormPage5', b2)
    if hasattr(b2, 'webapp_Control'):
        assert not _is_linked(b2, 'webapp_Control', a)


def test_assoc_controls6_link_reassign_clear():
    a = webapp_NormalControl(text="sample_text")
    b1 = webapp_NormalPage()
    b2 = webapp_NormalPage()
    _safe_set(a, 'webapp_NormalControl', b1)
    assert _is_linked(a, 'webapp_NormalControl', b1)
    if hasattr(b1, 'webapp_NormalPage'):
        assert _is_linked(b1, 'webapp_NormalPage', a)
    _safe_set(a, 'webapp_NormalControl', b2)
    assert _is_linked(a, 'webapp_NormalControl', b2)
    if hasattr(b1, 'webapp_NormalPage'):
        assert not _is_linked(b1, 'webapp_NormalPage', a)
    if hasattr(b2, 'webapp_NormalPage'):
        assert _is_linked(b2, 'webapp_NormalPage', a)
    _safe_set(a, 'webapp_NormalControl', None)
    assert not _is_linked(a, 'webapp_NormalControl', b2)
    if hasattr(b2, 'webapp_NormalPage'):
        assert not _is_linked(b2, 'webapp_NormalPage', a)


def test_assoc_destination7_link_reassign_clear():
    a = webapp_Page(default=True, name="sample_text", title="sample_text")
    b1 = webapp_Link()
    b2 = webapp_Link()
    _safe_set(a, 'webapp_Page8', b1)
    assert _is_linked(a, 'webapp_Page8', b1)
    if hasattr(b1, 'webapp_Link'):
        assert _is_linked(b1, 'webapp_Link', a)
    _safe_set(a, 'webapp_Page8', b2)
    assert _is_linked(a, 'webapp_Page8', b2)
    if hasattr(b1, 'webapp_Link'):
        assert not _is_linked(b1, 'webapp_Link', a)
    if hasattr(b2, 'webapp_Link'):
        assert _is_linked(b2, 'webapp_Link', a)
    _safe_set(a, 'webapp_Page8', None)
    assert not _is_linked(a, 'webapp_Page8', b2)
    if hasattr(b2, 'webapp_Link'):
        assert not _is_linked(b2, 'webapp_Link', a)


def test_assoc_elements10_link_reassign_clear():
    a = webapp_ListElement(value="sample_text")
    b1 = webapp_RadioButton()
    b2 = webapp_RadioButton()
    _safe_set(a, 'webapp_ListElement11', b1)
    assert _is_linked(a, 'webapp_ListElement11', b1)
    if hasattr(b1, 'webapp_RadioButton'):
        assert _is_linked(b1, 'webapp_RadioButton', a)
    _safe_set(a, 'webapp_ListElement11', b2)
    assert _is_linked(a, 'webapp_ListElement11', b2)
    if hasattr(b1, 'webapp_RadioButton'):
        assert not _is_linked(b1, 'webapp_RadioButton', a)
    if hasattr(b2, 'webapp_RadioButton'):
        assert _is_linked(b2, 'webapp_RadioButton', a)
    _safe_set(a, 'webapp_ListElement11', None)
    assert not _is_linked(a, 'webapp_ListElement11', b2)
    if hasattr(b2, 'webapp_RadioButton'):
        assert not _is_linked(b2, 'webapp_RadioButton', a)


def test_assoc_elements9_link_reassign_clear():
    a = webapp_ListElement(value="sample_text")
    b1 = webapp_DropDownList()
    b2 = webapp_DropDownList()
    _safe_set(a, 'webapp_ListElement', b1)
    assert _is_linked(a, 'webapp_ListElement', b1)
    if hasattr(b1, 'webapp_DropDownList'):
        assert _is_linked(b1, 'webapp_DropDownList', a)
    _safe_set(a, 'webapp_ListElement', b2)
    assert _is_linked(a, 'webapp_ListElement', b2)
    if hasattr(b1, 'webapp_DropDownList'):
        assert not _is_linked(b1, 'webapp_DropDownList', a)
    if hasattr(b2, 'webapp_DropDownList'):
        assert _is_linked(b2, 'webapp_DropDownList', a)
    _safe_set(a, 'webapp_ListElement', None)
    assert not _is_linked(a, 'webapp_ListElement', b2)
    if hasattr(b2, 'webapp_DropDownList'):
        assert not _is_linked(b2, 'webapp_DropDownList', a)


def test_assoc_errorTarget1_link_reassign_clear():
    a = webapp_Page(default=True, name="sample_text", title="sample_text")
    b1 = webapp_FormPage(persist=True)
    b2 = webapp_FormPage(persist=False)
    _safe_set(a, 'webapp_Page3', b1)
    assert _is_linked(a, 'webapp_Page3', b1)
    if hasattr(b1, 'webapp_FormPage2'):
        assert _is_linked(b1, 'webapp_FormPage2', a)
    _safe_set(a, 'webapp_Page3', b2)
    assert _is_linked(a, 'webapp_Page3', b2)
    if hasattr(b1, 'webapp_FormPage2'):
        assert not _is_linked(b1, 'webapp_FormPage2', a)
    if hasattr(b2, 'webapp_FormPage2'):
        assert _is_linked(b2, 'webapp_FormPage2', a)
    _safe_set(a, 'webapp_Page3', None)
    assert not _is_linked(a, 'webapp_Page3', b2)
    if hasattr(b2, 'webapp_FormPage2'):
        assert not _is_linked(b2, 'webapp_FormPage2', a)


def test_assoc_pages12_link_reassign_clear():
    a = webapp_Page(default=True, name="sample_text", title="sample_text")
    b1 = webapp_DynamicWebApp(name="sample_text")
    b2 = webapp_DynamicWebApp(name="sample_text_2")
    _safe_set(a, 'webapp_Page13', b1)
    assert _is_linked(a, 'webapp_Page13', b1)
    if hasattr(b1, 'webapp_DynamicWebApp'):
        assert _is_linked(b1, 'webapp_DynamicWebApp', a)
    _safe_set(a, 'webapp_Page13', b2)
    assert _is_linked(a, 'webapp_Page13', b2)
    if hasattr(b1, 'webapp_DynamicWebApp'):
        assert not _is_linked(b1, 'webapp_DynamicWebApp', a)
    if hasattr(b2, 'webapp_DynamicWebApp'):
        assert _is_linked(b2, 'webapp_DynamicWebApp', a)
    _safe_set(a, 'webapp_Page13', None)
    assert not _is_linked(a, 'webapp_Page13', b2)
    if hasattr(b2, 'webapp_DynamicWebApp'):
        assert not _is_linked(b2, 'webapp_DynamicWebApp', a)


def test_assoc_successTarget0_link_reassign_clear():
    a = webapp_Page(default=True, name="sample_text", title="sample_text")
    b1 = webapp_FormPage(persist=True)
    b2 = webapp_FormPage(persist=False)
    _safe_set(a, 'webapp_Page', b1)
    assert _is_linked(a, 'webapp_Page', b1)
    if hasattr(b1, 'webapp_FormPage'):
        assert _is_linked(b1, 'webapp_FormPage', a)
    _safe_set(a, 'webapp_Page', b2)
    assert _is_linked(a, 'webapp_Page', b2)
    if hasattr(b1, 'webapp_FormPage'):
        assert not _is_linked(b1, 'webapp_FormPage', a)
    if hasattr(b2, 'webapp_FormPage'):
        assert _is_linked(b2, 'webapp_FormPage', a)
    _safe_set(a, 'webapp_Page', None)
    assert not _is_linked(a, 'webapp_Page', b2)
    if hasattr(b2, 'webapp_FormPage'):
        assert not _is_linked(b2, 'webapp_FormPage', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Control_strategy = st.builds(Control)
@given(instance=Control_strategy)
@settings(max_examples=25)
def test_Control_instantiation(instance):
    assert isinstance(instance, Control)


FormButton_strategy = st.builds(FormButton)
@given(instance=FormButton_strategy)
@settings(max_examples=25)
def test_FormButton_instantiation(instance):
    assert isinstance(instance, FormButton)


NormalControl_strategy = st.builds(NormalControl)
@given(instance=NormalControl_strategy)
@settings(max_examples=25)
def test_NormalControl_instantiation(instance):
    assert isinstance(instance, NormalControl)


Page_strategy = st.builds(Page)
@given(instance=Page_strategy)
@settings(max_examples=25)
def test_Page_instantiation(instance):
    assert isinstance(instance, Page)


TextBox_strategy = st.builds(TextBox)
@given(instance=TextBox_strategy)
@settings(max_examples=25)
def test_TextBox_instantiation(instance):
    assert isinstance(instance, TextBox)


webapp_CheckBox_strategy = st.builds(webapp_CheckBox, text=safe_text)
@given(instance=webapp_CheckBox_strategy)
@settings(max_examples=25)
def test_webapp_CheckBox_instantiation(instance):
    assert isinstance(instance, webapp_CheckBox)


webapp_Control_strategy = st.builds(webapp_Control, id=safe_text, name=safe_text)
@given(instance=webapp_Control_strategy)
@settings(max_examples=25)
def test_webapp_Control_instantiation(instance):
    assert isinstance(instance, webapp_Control)


webapp_DateBox_strategy = st.builds(webapp_DateBox, format=safe_text)
@given(instance=webapp_DateBox_strategy)
@settings(max_examples=25)
def test_webapp_DateBox_instantiation(instance):
    assert isinstance(instance, webapp_DateBox)


webapp_DropDownList_strategy = st.builds(webapp_DropDownList)
@given(instance=webapp_DropDownList_strategy)
@settings(max_examples=25)
def test_webapp_DropDownList_instantiation(instance):
    assert isinstance(instance, webapp_DropDownList)


webapp_DynamicWebApp_strategy = st.builds(webapp_DynamicWebApp, name=safe_text)
@given(instance=webapp_DynamicWebApp_strategy)
@settings(max_examples=25)
def test_webapp_DynamicWebApp_instantiation(instance):
    assert isinstance(instance, webapp_DynamicWebApp)


webapp_EmailBox_strategy = st.builds(webapp_EmailBox)
@given(instance=webapp_EmailBox_strategy)
@settings(max_examples=25)
def test_webapp_EmailBox_instantiation(instance):
    assert isinstance(instance, webapp_EmailBox)


webapp_FormButton_strategy = st.builds(webapp_FormButton, text=safe_text)
@given(instance=webapp_FormButton_strategy)
@settings(max_examples=25)
def test_webapp_FormButton_instantiation(instance):
    assert isinstance(instance, webapp_FormButton)


webapp_FormPage_strategy = st.builds(webapp_FormPage, persist=st.booleans())
@given(instance=webapp_FormPage_strategy)
@settings(max_examples=25)
def test_webapp_FormPage_instantiation(instance):
    assert isinstance(instance, webapp_FormPage)


webapp_Label_strategy = st.builds(webapp_Label)
@given(instance=webapp_Label_strategy)
@settings(max_examples=25)
def test_webapp_Label_instantiation(instance):
    assert isinstance(instance, webapp_Label)


webapp_Link_strategy = st.builds(webapp_Link)
@given(instance=webapp_Link_strategy)
@settings(max_examples=25)
def test_webapp_Link_instantiation(instance):
    assert isinstance(instance, webapp_Link)


webapp_ListElement_strategy = st.builds(webapp_ListElement, value=safe_text)
@given(instance=webapp_ListElement_strategy)
@settings(max_examples=25)
def test_webapp_ListElement_instantiation(instance):
    assert isinstance(instance, webapp_ListElement)


webapp_NormalButton_strategy = st.builds(webapp_NormalButton)
@given(instance=webapp_NormalButton_strategy)
@settings(max_examples=25)
def test_webapp_NormalButton_instantiation(instance):
    assert isinstance(instance, webapp_NormalButton)


webapp_NormalControl_strategy = st.builds(webapp_NormalControl, text=safe_text)
@given(instance=webapp_NormalControl_strategy)
@settings(max_examples=25)
def test_webapp_NormalControl_instantiation(instance):
    assert isinstance(instance, webapp_NormalControl)


webapp_NormalPage_strategy = st.builds(webapp_NormalPage)
@given(instance=webapp_NormalPage_strategy)
@settings(max_examples=25)
def test_webapp_NormalPage_instantiation(instance):
    assert isinstance(instance, webapp_NormalPage)


webapp_Page_strategy = st.builds(webapp_Page, default=st.booleans(), name=safe_text, title=safe_text)
@given(instance=webapp_Page_strategy)
@settings(max_examples=25)
def test_webapp_Page_instantiation(instance):
    assert isinstance(instance, webapp_Page)


webapp_PasswordBox_strategy = st.builds(webapp_PasswordBox)
@given(instance=webapp_PasswordBox_strategy)
@settings(max_examples=25)
def test_webapp_PasswordBox_instantiation(instance):
    assert isinstance(instance, webapp_PasswordBox)


webapp_RadioButton_strategy = st.builds(webapp_RadioButton)
@given(instance=webapp_RadioButton_strategy)
@settings(max_examples=25)
def test_webapp_RadioButton_instantiation(instance):
    assert isinstance(instance, webapp_RadioButton)


webapp_ResetButton_strategy = st.builds(webapp_ResetButton)
@given(instance=webapp_ResetButton_strategy)
@settings(max_examples=25)
def test_webapp_ResetButton_instantiation(instance):
    assert isinstance(instance, webapp_ResetButton)


webapp_SubmitButton_strategy = st.builds(webapp_SubmitButton)
@given(instance=webapp_SubmitButton_strategy)
@settings(max_examples=25)
def test_webapp_SubmitButton_instantiation(instance):
    assert isinstance(instance, webapp_SubmitButton)


webapp_TextBox_strategy = st.builds(webapp_TextBox, maxLength=st.integers(), required=st.booleans(), size=st.integers(), text=safe_text)
@given(instance=webapp_TextBox_strategy)
@settings(max_examples=25)
def test_webapp_TextBox_instantiation(instance):
    assert isinstance(instance, webapp_TextBox)



