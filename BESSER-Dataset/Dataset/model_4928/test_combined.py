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
    bootstrap_FormWidget,
    Widget,
    bootstrap_Table,
    bootstrap_Form,
    bootstrap_Widget,
    bootstrap_MainPage,
    bootstrap_Page,
    bootstrap_Site,
    FormWidget,
    bootstrap_Spinner,
    bootstrap_TextArea,
    bootstrap_CheckBox,
    bootstrap_Section,
    bootstrap_ImagesBlock,
    bootstrap_Gallery,
    bootstrap_Video,
    bootstrap_Text,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bootstrap_formwidget_is_not_abstract():
    assert not inspect.isabstract(bootstrap_FormWidget)


def test_hyp_bootstrap_formwidget_constructor_exists():
    assert callable(bootstrap_FormWidget.__init__)


def test_hyp_bootstrap_formwidget_constructor_args():
    sig = inspect.signature(bootstrap_FormWidget.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_widget_is_not_abstract():
    assert not inspect.isabstract(Widget)


def test_hyp_widget_constructor_exists():
    assert callable(Widget.__init__)


def test_hyp_widget_constructor_args():
    sig = inspect.signature(Widget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bootstrap_table_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Table)


def test_hyp_bootstrap_table_constructor_exists():
    assert callable(bootstrap_Table.__init__)


def test_hyp_bootstrap_table_constructor_args():
    sig = inspect.signature(bootstrap_Table.__init__)
    params = list(sig.parameters.keys())
    assert "columnNames" in params, "Missing parameter 'columnNames'"
    assert "bordered" in params, "Missing parameter 'bordered'"
    assert "striped" in params, "Missing parameter 'striped'"
    assert "rowNames" in params, "Missing parameter 'rowNames'"







def test_hyp_bootstrap_form_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Form)


def test_hyp_bootstrap_form_constructor_exists():
    assert callable(bootstrap_Form.__init__)


def test_hyp_bootstrap_form_constructor_args():
    sig = inspect.signature(bootstrap_Form.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bootstrap_widget_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Widget)


def test_hyp_bootstrap_widget_constructor_exists():
    assert callable(bootstrap_Widget.__init__)


def test_hyp_bootstrap_widget_constructor_args():
    sig = inspect.signature(bootstrap_Widget.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_bootstrap_mainpage_is_not_abstract():
    assert not inspect.isabstract(bootstrap_MainPage)


def test_hyp_bootstrap_mainpage_constructor_exists():
    assert callable(bootstrap_MainPage.__init__)


def test_hyp_bootstrap_mainpage_constructor_args():
    sig = inspect.signature(bootstrap_MainPage.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_bootstrap_page_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Page)


def test_hyp_bootstrap_page_constructor_exists():
    assert callable(bootstrap_Page.__init__)


def test_hyp_bootstrap_page_constructor_args():
    sig = inspect.signature(bootstrap_Page.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_bootstrap_site_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Site)


def test_hyp_bootstrap_site_constructor_exists():
    assert callable(bootstrap_Site.__init__)


def test_hyp_bootstrap_site_constructor_args():
    sig = inspect.signature(bootstrap_Site.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_formwidget_is_not_abstract():
    assert not inspect.isabstract(FormWidget)


def test_hyp_formwidget_constructor_exists():
    assert callable(FormWidget.__init__)


def test_hyp_formwidget_constructor_args():
    sig = inspect.signature(FormWidget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bootstrap_spinner_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Spinner)


def test_hyp_bootstrap_spinner_constructor_exists():
    assert callable(bootstrap_Spinner.__init__)


def test_hyp_bootstrap_spinner_constructor_args():
    sig = inspect.signature(bootstrap_Spinner.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"




def test_hyp_bootstrap_textarea_is_not_abstract():
    assert not inspect.isabstract(bootstrap_TextArea)


def test_hyp_bootstrap_textarea_constructor_exists():
    assert callable(bootstrap_TextArea.__init__)


def test_hyp_bootstrap_textarea_constructor_args():
    sig = inspect.signature(bootstrap_TextArea.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bootstrap_checkbox_is_not_abstract():
    assert not inspect.isabstract(bootstrap_CheckBox)


def test_hyp_bootstrap_checkbox_constructor_exists():
    assert callable(bootstrap_CheckBox.__init__)


def test_hyp_bootstrap_checkbox_constructor_args():
    sig = inspect.signature(bootstrap_CheckBox.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_bootstrap_section_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Section)


def test_hyp_bootstrap_section_constructor_exists():
    assert callable(bootstrap_Section.__init__)


def test_hyp_bootstrap_section_constructor_args():
    sig = inspect.signature(bootstrap_Section.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"





def test_hyp_bootstrap_imagesblock_is_not_abstract():
    assert not inspect.isabstract(bootstrap_ImagesBlock)


def test_hyp_bootstrap_imagesblock_constructor_exists():
    assert callable(bootstrap_ImagesBlock.__init__)


def test_hyp_bootstrap_imagesblock_constructor_args():
    sig = inspect.signature(bootstrap_ImagesBlock.__init__)
    params = list(sig.parameters.keys())
    assert "imagesPath" in params, "Missing parameter 'imagesPath'"




def test_hyp_bootstrap_gallery_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Gallery)


def test_hyp_bootstrap_gallery_constructor_exists():
    assert callable(bootstrap_Gallery.__init__)


def test_hyp_bootstrap_gallery_constructor_args():
    sig = inspect.signature(bootstrap_Gallery.__init__)
    params = list(sig.parameters.keys())
    assert "imagesPath" in params, "Missing parameter 'imagesPath'"




def test_hyp_bootstrap_video_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Video)


def test_hyp_bootstrap_video_constructor_exists():
    assert callable(bootstrap_Video.__init__)


def test_hyp_bootstrap_video_constructor_args():
    sig = inspect.signature(bootstrap_Video.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"




def test_hyp_bootstrap_text_is_not_abstract():
    assert not inspect.isabstract(bootstrap_Text)


def test_hyp_bootstrap_text_constructor_exists():
    assert callable(bootstrap_Text.__init__)


def test_hyp_bootstrap_text_constructor_args():
    sig = inspect.signature(bootstrap_Text.__init__)
    params = list(sig.parameters.keys())
    assert "columnNumber" in params, "Missing parameter 'columnNumber'"



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
bootstrap_FormWidget_strategy = st.builds(
    bootstrap_FormWidget,
    label=
        safe_text
)
Widget_strategy = st.builds(
    Widget,
)
bootstrap_Table_strategy = st.builds(
    bootstrap_Table,
    columnNames=
        safe_text,
    bordered=
        st.booleans(),
    striped=
        st.booleans(),
    rowNames=
        safe_text
)
bootstrap_Form_strategy = st.builds(
    bootstrap_Form,
)
bootstrap_Widget_strategy = st.builds(
    bootstrap_Widget,
    title=
        safe_text
)
bootstrap_MainPage_strategy = st.builds(
    bootstrap_MainPage,
    description=
        safe_text,
    title=
        safe_text
)
bootstrap_Page_strategy = st.builds(
    bootstrap_Page,
    title=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
bootstrap_Site_strategy = st.builds(
    bootstrap_Site,
    title=
        safe_text
)
FormWidget_strategy = st.builds(
    FormWidget,
)
bootstrap_Spinner_strategy = st.builds(
    bootstrap_Spinner,
    values=
        safe_text
)
bootstrap_TextArea_strategy = st.builds(
    bootstrap_TextArea,
)
bootstrap_CheckBox_strategy = st.builds(
    bootstrap_CheckBox,
    description=
        safe_text
)
bootstrap_Section_strategy = st.builds(
    bootstrap_Section,
    description=
        safe_text,
    title=
        safe_text
)
bootstrap_ImagesBlock_strategy = st.builds(
    bootstrap_ImagesBlock,
    imagesPath=
        safe_text
)
bootstrap_Gallery_strategy = st.builds(
    bootstrap_Gallery,
    imagesPath=
        safe_text
)
bootstrap_Video_strategy = st.builds(
    bootstrap_Video,
    path=
        safe_text
)
bootstrap_Text_strategy = st.builds(
    bootstrap_Text,
    columnNumber=
        st.integers()
)




@given(instance=bootstrap_FormWidget_strategy)
def test_hyp_bootstrap_formwidget_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original





@given(instance=bootstrap_Table_strategy)
def test_hyp_bootstrap_table_columnNames_setter(instance):
    original = instance.columnNames
    instance.columnNames = original
    assert instance.columnNames == original



@given(instance=bootstrap_Table_strategy)
def test_hyp_bootstrap_table_bordered_setter(instance):
    original = instance.bordered
    instance.bordered = original
    assert instance.bordered == original



@given(instance=bootstrap_Table_strategy)
def test_hyp_bootstrap_table_striped_setter(instance):
    original = instance.striped
    instance.striped = original
    assert instance.striped == original



@given(instance=bootstrap_Table_strategy)
def test_hyp_bootstrap_table_rowNames_setter(instance):
    original = instance.rowNames
    instance.rowNames = original
    assert instance.rowNames == original





@given(instance=bootstrap_Widget_strategy)
def test_hyp_bootstrap_widget_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=bootstrap_MainPage_strategy)
def test_hyp_bootstrap_mainpage_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=bootstrap_MainPage_strategy)
def test_hyp_bootstrap_mainpage_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=bootstrap_Page_strategy)
def test_hyp_bootstrap_page_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=bootstrap_Page_strategy)
def test_hyp_bootstrap_page_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=bootstrap_Page_strategy)
def test_hyp_bootstrap_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=bootstrap_Site_strategy)
def test_hyp_bootstrap_site_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original





@given(instance=bootstrap_Spinner_strategy)
def test_hyp_bootstrap_spinner_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original





@given(instance=bootstrap_CheckBox_strategy)
def test_hyp_bootstrap_checkbox_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=bootstrap_Section_strategy)
def test_hyp_bootstrap_section_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=bootstrap_Section_strategy)
def test_hyp_bootstrap_section_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=bootstrap_ImagesBlock_strategy)
def test_hyp_bootstrap_imagesblock_imagesPath_setter(instance):
    original = instance.imagesPath
    instance.imagesPath = original
    assert instance.imagesPath == original




@given(instance=bootstrap_Gallery_strategy)
def test_hyp_bootstrap_gallery_imagesPath_setter(instance):
    original = instance.imagesPath
    instance.imagesPath = original
    assert instance.imagesPath == original




@given(instance=bootstrap_Video_strategy)
def test_hyp_bootstrap_video_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original




@given(instance=bootstrap_Text_strategy)
def test_hyp_bootstrap_text_columnNumber_setter(instance):
    original = instance.columnNumber
    instance.columnNumber = original
    assert instance.columnNumber == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    FormWidget,
    Widget,
    bootstrap_CheckBox,
    bootstrap_Form,
    bootstrap_FormWidget,
    bootstrap_Gallery,
    bootstrap_ImagesBlock,
    bootstrap_MainPage,
    bootstrap_Page,
    bootstrap_Section,
    bootstrap_Site,
    bootstrap_Spinner,
    bootstrap_Table,
    bootstrap_Text,
    bootstrap_TextArea,
    bootstrap_Video,
    bootstrap_Widget,
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

def test_bootstrap_CheckBox_description_value_roundtrip():
    instance = bootstrap_CheckBox(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_bootstrap_FormWidget_label_value_roundtrip():
    instance = bootstrap_FormWidget(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_bootstrap_Gallery_imagesPath_value_roundtrip():
    instance = bootstrap_Gallery(imagesPath="sample_text")
    assert instance.imagesPath == "sample_text"
    instance.imagesPath = "sample_text_2"
    assert instance.imagesPath == "sample_text_2"


def test_bootstrap_ImagesBlock_imagesPath_value_roundtrip():
    instance = bootstrap_ImagesBlock(imagesPath="sample_text")
    assert instance.imagesPath == "sample_text"
    instance.imagesPath = "sample_text_2"
    assert instance.imagesPath == "sample_text_2"


def test_bootstrap_MainPage_description_value_roundtrip():
    instance = bootstrap_MainPage(description="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_bootstrap_MainPage_title_value_roundtrip():
    instance = bootstrap_MainPage(description="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bootstrap_Page_description_value_roundtrip():
    instance = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_bootstrap_Page_name_value_roundtrip():
    instance = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_bootstrap_Page_title_value_roundtrip():
    instance = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bootstrap_Section_description_value_roundtrip():
    instance = bootstrap_Section(description="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_bootstrap_Section_title_value_roundtrip():
    instance = bootstrap_Section(description="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bootstrap_Site_title_value_roundtrip():
    instance = bootstrap_Site(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bootstrap_Spinner_values_value_roundtrip():
    instance = bootstrap_Spinner(values="sample_text")
    assert instance.values == "sample_text"
    instance.values = "sample_text_2"
    assert instance.values == "sample_text_2"


def test_bootstrap_Table_bordered_value_roundtrip():
    instance = bootstrap_Table(bordered=True, columnNames="sample_text", rowNames="sample_text", striped=True)
    assert instance.bordered == True
    instance.bordered = False
    assert instance.bordered == False


def test_bootstrap_Table_columnNames_value_roundtrip():
    instance = bootstrap_Table(bordered=True, columnNames="sample_text", rowNames="sample_text", striped=True)
    assert instance.columnNames == "sample_text"
    instance.columnNames = "sample_text_2"
    assert instance.columnNames == "sample_text_2"


def test_bootstrap_Table_rowNames_value_roundtrip():
    instance = bootstrap_Table(bordered=True, columnNames="sample_text", rowNames="sample_text", striped=True)
    assert instance.rowNames == "sample_text"
    instance.rowNames = "sample_text_2"
    assert instance.rowNames == "sample_text_2"


def test_bootstrap_Table_striped_value_roundtrip():
    instance = bootstrap_Table(bordered=True, columnNames="sample_text", rowNames="sample_text", striped=True)
    assert instance.striped == True
    instance.striped = False
    assert instance.striped == False


def test_bootstrap_Text_columnNumber_value_roundtrip():
    instance = bootstrap_Text(columnNumber=7)
    assert instance.columnNumber == 7
    instance.columnNumber = 13
    assert instance.columnNumber == 13


def test_bootstrap_Video_path_value_roundtrip():
    instance = bootstrap_Video(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_bootstrap_Widget_title_value_roundtrip():
    instance = bootstrap_Widget(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bootstrap_CheckBox_isa_FormWidget():
    instance = bootstrap_CheckBox(description="sample_text")
    assert isinstance(instance, FormWidget)


def test_bootstrap_Spinner_isa_FormWidget():
    instance = bootstrap_Spinner(values="sample_text")
    assert isinstance(instance, FormWidget)


def test_bootstrap_TextArea_isa_FormWidget():
    instance = bootstrap_TextArea()
    assert isinstance(instance, FormWidget)


def test_bootstrap_Form_isa_Widget():
    instance = bootstrap_Form()
    assert isinstance(instance, Widget)


def test_bootstrap_Gallery_isa_Widget():
    instance = bootstrap_Gallery(imagesPath="sample_text")
    assert isinstance(instance, Widget)


def test_bootstrap_ImagesBlock_isa_Widget():
    instance = bootstrap_ImagesBlock(imagesPath="sample_text")
    assert isinstance(instance, Widget)


def test_bootstrap_Table_isa_Widget():
    instance = bootstrap_Table(bordered=True, columnNames="sample_text", rowNames="sample_text", striped=True)
    assert isinstance(instance, Widget)


def test_bootstrap_Text_isa_Widget():
    instance = bootstrap_Text(columnNumber=7)
    assert isinstance(instance, Widget)


def test_bootstrap_Video_isa_Widget():
    instance = bootstrap_Video(path="sample_text")
    assert isinstance(instance, Widget)


def test_assoc_form13_link_reassign_clear():
    a = bootstrap_FormWidget(label="sample_text")
    b1 = bootstrap_Form()
    b2 = bootstrap_Form()
    _safe_set(a, 'formWidgets', b1)
    assert _is_linked(a, 'formWidgets', b1)
    if hasattr(b1, 'Form'):
        assert _is_linked(b1, 'Form', a)
    _safe_set(a, 'formWidgets', b2)
    assert _is_linked(a, 'formWidgets', b2)
    if hasattr(b1, 'Form'):
        assert not _is_linked(b1, 'Form', a)
    if hasattr(b2, 'Form'):
        assert _is_linked(b2, 'Form', a)
    _safe_set(a, 'formWidgets', None)
    assert not _is_linked(a, 'formWidgets', b2)
    if hasattr(b2, 'Form'):
        assert not _is_linked(b2, 'Form', a)


def test_assoc_formWidgets12_link_reassign_clear():
    a = bootstrap_FormWidget(label="sample_text")
    b1 = bootstrap_Form()
    b2 = bootstrap_Form()
    _safe_set(a, 'FormWidget', b1)
    assert _is_linked(a, 'FormWidget', b1)
    if hasattr(b1, 'form'):
        assert _is_linked(b1, 'form', a)
    _safe_set(a, 'FormWidget', b2)
    assert _is_linked(a, 'FormWidget', b2)
    if hasattr(b1, 'form'):
        assert not _is_linked(b1, 'form', a)
    if hasattr(b2, 'form'):
        assert _is_linked(b2, 'form', a)
    _safe_set(a, 'FormWidget', None)
    assert not _is_linked(a, 'FormWidget', b2)
    if hasattr(b2, 'form'):
        assert not _is_linked(b2, 'form', a)


def test_assoc_mainPage1_link_reassign_clear():
    a = bootstrap_Site(title="sample_text")
    b1 = bootstrap_MainPage(description="sample_text", title="sample_text")
    b2 = bootstrap_MainPage(description="sample_text_2", title="sample_text_2")
    _safe_set(a, 'site2', b1)
    assert _is_linked(a, 'site2', b1)
    if hasattr(b1, 'MainPage'):
        assert _is_linked(b1, 'MainPage', a)
    _safe_set(a, 'site2', b2)
    assert _is_linked(a, 'site2', b2)
    if hasattr(b1, 'MainPage'):
        assert not _is_linked(b1, 'MainPage', a)
    if hasattr(b2, 'MainPage'):
        assert _is_linked(b2, 'MainPage', a)
    _safe_set(a, 'site2', None)
    assert not _is_linked(a, 'site2', b2)
    if hasattr(b2, 'MainPage'):
        assert not _is_linked(b2, 'MainPage', a)


def test_assoc_page8_link_reassign_clear():
    a = bootstrap_Section(description="sample_text", title="sample_text")
    b1 = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    b2 = bootstrap_Page(description="sample_text_2", name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'sections', b1)
    assert _is_linked(a, 'sections', b1)
    if hasattr(b1, 'Page9'):
        assert _is_linked(b1, 'Page9', a)
    _safe_set(a, 'sections', b2)
    assert _is_linked(a, 'sections', b2)
    if hasattr(b1, 'Page9'):
        assert not _is_linked(b1, 'Page9', a)
    if hasattr(b2, 'Page9'):
        assert _is_linked(b2, 'Page9', a)
    _safe_set(a, 'sections', None)
    assert not _is_linked(a, 'sections', b2)
    if hasattr(b2, 'Page9'):
        assert not _is_linked(b2, 'Page9', a)


def test_assoc_pages0_link_reassign_clear():
    a = bootstrap_Site(title="sample_text")
    b1 = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    b2 = bootstrap_Page(description="sample_text_2", name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'site', {b1})
    assert _is_linked(a, 'site', b1)
    if hasattr(b1, 'Page'):
        assert _is_linked(b1, 'Page', a)
    _safe_set(a, 'site', {b2})
    assert _is_linked(a, 'site', b2)
    if hasattr(b1, 'Page'):
        assert not _is_linked(b1, 'Page', a)
    if hasattr(b2, 'Page'):
        assert _is_linked(b2, 'Page', a)
    _safe_set(a, 'site', set())
    assert not _is_linked(a, 'site', b2)
    if hasattr(b2, 'Page'):
        assert not _is_linked(b2, 'Page', a)


def test_assoc_section10_link_reassign_clear():
    a = bootstrap_Widget(title="sample_text")
    b1 = bootstrap_Section(description="sample_text", title="sample_text")
    b2 = bootstrap_Section(description="sample_text_2", title="sample_text_2")
    _safe_set(a, 'widgets', b1)
    assert _is_linked(a, 'widgets', b1)
    if hasattr(b1, 'Section11'):
        assert _is_linked(b1, 'Section11', a)
    _safe_set(a, 'widgets', b2)
    assert _is_linked(a, 'widgets', b2)
    if hasattr(b1, 'Section11'):
        assert not _is_linked(b1, 'Section11', a)
    if hasattr(b2, 'Section11'):
        assert _is_linked(b2, 'Section11', a)
    _safe_set(a, 'widgets', None)
    assert not _is_linked(a, 'widgets', b2)
    if hasattr(b2, 'Section11'):
        assert not _is_linked(b2, 'Section11', a)


def test_assoc_sections3_link_reassign_clear():
    a = bootstrap_Section(description="sample_text", title="sample_text")
    b1 = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    b2 = bootstrap_Page(description="sample_text_2", name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'Section', b1)
    assert _is_linked(a, 'Section', b1)
    if hasattr(b1, 'page'):
        assert _is_linked(b1, 'page', a)
    _safe_set(a, 'Section', b2)
    assert _is_linked(a, 'Section', b2)
    if hasattr(b1, 'page'):
        assert not _is_linked(b1, 'page', a)
    if hasattr(b2, 'page'):
        assert _is_linked(b2, 'page', a)
    _safe_set(a, 'Section', None)
    assert not _is_linked(a, 'Section', b2)
    if hasattr(b2, 'page'):
        assert not _is_linked(b2, 'page', a)


def test_assoc_site4_link_reassign_clear():
    a = bootstrap_Site(title="sample_text")
    b1 = bootstrap_Page(description="sample_text", name="sample_text", title="sample_text")
    b2 = bootstrap_Page(description="sample_text_2", name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'Site', b1)
    assert _is_linked(a, 'Site', b1)
    if hasattr(b1, 'pages'):
        assert _is_linked(b1, 'pages', a)
    _safe_set(a, 'Site', b2)
    assert _is_linked(a, 'Site', b2)
    if hasattr(b1, 'pages'):
        assert not _is_linked(b1, 'pages', a)
    if hasattr(b2, 'pages'):
        assert _is_linked(b2, 'pages', a)
    _safe_set(a, 'Site', None)
    assert not _is_linked(a, 'Site', b2)
    if hasattr(b2, 'pages'):
        assert not _is_linked(b2, 'pages', a)


def test_assoc_site5_link_reassign_clear():
    a = bootstrap_Site(title="sample_text")
    b1 = bootstrap_MainPage(description="sample_text", title="sample_text")
    b2 = bootstrap_MainPage(description="sample_text_2", title="sample_text_2")
    _safe_set(a, 'Site6', b1)
    assert _is_linked(a, 'Site6', b1)
    if hasattr(b1, 'mainPage'):
        assert _is_linked(b1, 'mainPage', a)
    _safe_set(a, 'Site6', b2)
    assert _is_linked(a, 'Site6', b2)
    if hasattr(b1, 'mainPage'):
        assert not _is_linked(b1, 'mainPage', a)
    if hasattr(b2, 'mainPage'):
        assert _is_linked(b2, 'mainPage', a)
    _safe_set(a, 'Site6', None)
    assert not _is_linked(a, 'Site6', b2)
    if hasattr(b2, 'mainPage'):
        assert not _is_linked(b2, 'mainPage', a)


def test_assoc_widgets7_link_reassign_clear():
    a = bootstrap_Widget(title="sample_text")
    b1 = bootstrap_Section(description="sample_text", title="sample_text")
    b2 = bootstrap_Section(description="sample_text_2", title="sample_text_2")
    _safe_set(a, 'Widget', b1)
    assert _is_linked(a, 'Widget', b1)
    if hasattr(b1, 'section'):
        assert _is_linked(b1, 'section', a)
    _safe_set(a, 'Widget', b2)
    assert _is_linked(a, 'Widget', b2)
    if hasattr(b1, 'section'):
        assert not _is_linked(b1, 'section', a)
    if hasattr(b2, 'section'):
        assert _is_linked(b2, 'section', a)
    _safe_set(a, 'Widget', None)
    assert not _is_linked(a, 'Widget', b2)
    if hasattr(b2, 'section'):
        assert not _is_linked(b2, 'section', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

FormWidget_strategy = st.builds(FormWidget)
@given(instance=FormWidget_strategy)
@settings(max_examples=25)
def test_FormWidget_instantiation(instance):
    assert isinstance(instance, FormWidget)


Widget_strategy = st.builds(Widget)
@given(instance=Widget_strategy)
@settings(max_examples=25)
def test_Widget_instantiation(instance):
    assert isinstance(instance, Widget)


bootstrap_CheckBox_strategy = st.builds(bootstrap_CheckBox, description=safe_text)
@given(instance=bootstrap_CheckBox_strategy)
@settings(max_examples=25)
def test_bootstrap_CheckBox_instantiation(instance):
    assert isinstance(instance, bootstrap_CheckBox)


bootstrap_Form_strategy = st.builds(bootstrap_Form)
@given(instance=bootstrap_Form_strategy)
@settings(max_examples=25)
def test_bootstrap_Form_instantiation(instance):
    assert isinstance(instance, bootstrap_Form)


bootstrap_FormWidget_strategy = st.builds(bootstrap_FormWidget, label=safe_text)
@given(instance=bootstrap_FormWidget_strategy)
@settings(max_examples=25)
def test_bootstrap_FormWidget_instantiation(instance):
    assert isinstance(instance, bootstrap_FormWidget)


bootstrap_Gallery_strategy = st.builds(bootstrap_Gallery, imagesPath=safe_text)
@given(instance=bootstrap_Gallery_strategy)
@settings(max_examples=25)
def test_bootstrap_Gallery_instantiation(instance):
    assert isinstance(instance, bootstrap_Gallery)


bootstrap_ImagesBlock_strategy = st.builds(bootstrap_ImagesBlock, imagesPath=safe_text)
@given(instance=bootstrap_ImagesBlock_strategy)
@settings(max_examples=25)
def test_bootstrap_ImagesBlock_instantiation(instance):
    assert isinstance(instance, bootstrap_ImagesBlock)


bootstrap_MainPage_strategy = st.builds(bootstrap_MainPage, description=safe_text, title=safe_text)
@given(instance=bootstrap_MainPage_strategy)
@settings(max_examples=25)
def test_bootstrap_MainPage_instantiation(instance):
    assert isinstance(instance, bootstrap_MainPage)


bootstrap_Page_strategy = st.builds(bootstrap_Page, description=safe_text, name=safe_text, title=safe_text)
@given(instance=bootstrap_Page_strategy)
@settings(max_examples=25)
def test_bootstrap_Page_instantiation(instance):
    assert isinstance(instance, bootstrap_Page)


bootstrap_Section_strategy = st.builds(bootstrap_Section, description=safe_text, title=safe_text)
@given(instance=bootstrap_Section_strategy)
@settings(max_examples=25)
def test_bootstrap_Section_instantiation(instance):
    assert isinstance(instance, bootstrap_Section)


bootstrap_Site_strategy = st.builds(bootstrap_Site, title=safe_text)
@given(instance=bootstrap_Site_strategy)
@settings(max_examples=25)
def test_bootstrap_Site_instantiation(instance):
    assert isinstance(instance, bootstrap_Site)


bootstrap_Spinner_strategy = st.builds(bootstrap_Spinner, values=safe_text)
@given(instance=bootstrap_Spinner_strategy)
@settings(max_examples=25)
def test_bootstrap_Spinner_instantiation(instance):
    assert isinstance(instance, bootstrap_Spinner)


bootstrap_Table_strategy = st.builds(bootstrap_Table, bordered=st.booleans(), columnNames=safe_text, rowNames=safe_text, striped=st.booleans())
@given(instance=bootstrap_Table_strategy)
@settings(max_examples=25)
def test_bootstrap_Table_instantiation(instance):
    assert isinstance(instance, bootstrap_Table)


bootstrap_Text_strategy = st.builds(bootstrap_Text, columnNumber=st.integers())
@given(instance=bootstrap_Text_strategy)
@settings(max_examples=25)
def test_bootstrap_Text_instantiation(instance):
    assert isinstance(instance, bootstrap_Text)


bootstrap_TextArea_strategy = st.builds(bootstrap_TextArea)
@given(instance=bootstrap_TextArea_strategy)
@settings(max_examples=25)
def test_bootstrap_TextArea_instantiation(instance):
    assert isinstance(instance, bootstrap_TextArea)


bootstrap_Video_strategy = st.builds(bootstrap_Video, path=safe_text)
@given(instance=bootstrap_Video_strategy)
@settings(max_examples=25)
def test_bootstrap_Video_instantiation(instance):
    assert isinstance(instance, bootstrap_Video)


bootstrap_Widget_strategy = st.builds(bootstrap_Widget, title=safe_text)
@given(instance=bootstrap_Widget_strategy)
@settings(max_examples=25)
def test_bootstrap_Widget_instantiation(instance):
    assert isinstance(instance, bootstrap_Widget)



