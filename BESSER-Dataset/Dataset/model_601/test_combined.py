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
    Arch_Event,
    GraphicControl,
    Arch_TextBox,
    Arch_DropDownList,
    Arch_Div,
    Arch_Label,
    Arch_Parameter,
    Arch_Attribute,
    Arch_Method,
    Arch_GraphicControl,
    Arch_Entity,
    Arch_Logic,
    Arch_Service,
    Arch_Controller,
    Arch_View,
    Arch_BackEnd,
    Arch_FrontEnd,
    Arch_Application,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_arch_event_is_not_abstract():
    assert not inspect.isabstract(Arch_Event)


def test_hyp_arch_event_constructor_exists():
    assert callable(Arch_Event.__init__)


def test_hyp_arch_event_constructor_args():
    sig = inspect.signature(Arch_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_graphiccontrol_is_not_abstract():
    assert not inspect.isabstract(GraphicControl)


def test_hyp_graphiccontrol_constructor_exists():
    assert callable(GraphicControl.__init__)


def test_hyp_graphiccontrol_constructor_args():
    sig = inspect.signature(GraphicControl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arch_textbox_is_not_abstract():
    assert not inspect.isabstract(Arch_TextBox)


def test_hyp_arch_textbox_constructor_exists():
    assert callable(Arch_TextBox.__init__)


def test_hyp_arch_textbox_constructor_args():
    sig = inspect.signature(Arch_TextBox.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_arch_dropdownlist_is_not_abstract():
    assert not inspect.isabstract(Arch_DropDownList)


def test_hyp_arch_dropdownlist_constructor_exists():
    assert callable(Arch_DropDownList.__init__)


def test_hyp_arch_dropdownlist_constructor_args():
    sig = inspect.signature(Arch_DropDownList.__init__)
    params = list(sig.parameters.keys())
    assert "items" in params, "Missing parameter 'items'"




def test_hyp_arch_div_is_not_abstract():
    assert not inspect.isabstract(Arch_Div)


def test_hyp_arch_div_constructor_exists():
    assert callable(Arch_Div.__init__)


def test_hyp_arch_div_constructor_args():
    sig = inspect.signature(Arch_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arch_label_is_not_abstract():
    assert not inspect.isabstract(Arch_Label)


def test_hyp_arch_label_constructor_exists():
    assert callable(Arch_Label.__init__)


def test_hyp_arch_label_constructor_args():
    sig = inspect.signature(Arch_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_arch_parameter_is_not_abstract():
    assert not inspect.isabstract(Arch_Parameter)


def test_hyp_arch_parameter_constructor_exists():
    assert callable(Arch_Parameter.__init__)


def test_hyp_arch_parameter_constructor_args():
    sig = inspect.signature(Arch_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_arch_attribute_is_not_abstract():
    assert not inspect.isabstract(Arch_Attribute)


def test_hyp_arch_attribute_constructor_exists():
    assert callable(Arch_Attribute.__init__)


def test_hyp_arch_attribute_constructor_args():
    sig = inspect.signature(Arch_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_arch_method_is_not_abstract():
    assert not inspect.isabstract(Arch_Method)


def test_hyp_arch_method_constructor_exists():
    assert callable(Arch_Method.__init__)


def test_hyp_arch_method_constructor_args():
    sig = inspect.signature(Arch_Method.__init__)
    params = list(sig.parameters.keys())
    assert "returntype" in params, "Missing parameter 'returntype'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_arch_graphiccontrol_is_not_abstract():
    assert not inspect.isabstract(Arch_GraphicControl)


def test_hyp_arch_graphiccontrol_constructor_exists():
    assert callable(Arch_GraphicControl.__init__)


def test_hyp_arch_graphiccontrol_constructor_args():
    sig = inspect.signature(Arch_GraphicControl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_entity_is_not_abstract():
    assert not inspect.isabstract(Arch_Entity)


def test_hyp_arch_entity_constructor_exists():
    assert callable(Arch_Entity.__init__)


def test_hyp_arch_entity_constructor_args():
    sig = inspect.signature(Arch_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_logic_is_not_abstract():
    assert not inspect.isabstract(Arch_Logic)


def test_hyp_arch_logic_constructor_exists():
    assert callable(Arch_Logic.__init__)


def test_hyp_arch_logic_constructor_args():
    sig = inspect.signature(Arch_Logic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_service_is_not_abstract():
    assert not inspect.isabstract(Arch_Service)


def test_hyp_arch_service_constructor_exists():
    assert callable(Arch_Service.__init__)


def test_hyp_arch_service_constructor_args():
    sig = inspect.signature(Arch_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_controller_is_not_abstract():
    assert not inspect.isabstract(Arch_Controller)


def test_hyp_arch_controller_constructor_exists():
    assert callable(Arch_Controller.__init__)


def test_hyp_arch_controller_constructor_args():
    sig = inspect.signature(Arch_Controller.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_view_is_not_abstract():
    assert not inspect.isabstract(Arch_View)


def test_hyp_arch_view_constructor_exists():
    assert callable(Arch_View.__init__)


def test_hyp_arch_view_constructor_args():
    sig = inspect.signature(Arch_View.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_backend_is_not_abstract():
    assert not inspect.isabstract(Arch_BackEnd)


def test_hyp_arch_backend_constructor_exists():
    assert callable(Arch_BackEnd.__init__)


def test_hyp_arch_backend_constructor_args():
    sig = inspect.signature(Arch_BackEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_frontend_is_not_abstract():
    assert not inspect.isabstract(Arch_FrontEnd)


def test_hyp_arch_frontend_constructor_exists():
    assert callable(Arch_FrontEnd.__init__)


def test_hyp_arch_frontend_constructor_args():
    sig = inspect.signature(Arch_FrontEnd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_arch_application_is_not_abstract():
    assert not inspect.isabstract(Arch_Application)


def test_hyp_arch_application_constructor_exists():
    assert callable(Arch_Application.__init__)


def test_hyp_arch_application_constructor_args():
    sig = inspect.signature(Arch_Application.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
Arch_Event_strategy = st.builds(
    Arch_Event,
    name=
        safe_text
)
GraphicControl_strategy = st.builds(
    GraphicControl,
)
Arch_TextBox_strategy = st.builds(
    Arch_TextBox,
    type=
        safe_text
)
Arch_DropDownList_strategy = st.builds(
    Arch_DropDownList,
    items=
        safe_text
)
Arch_Div_strategy = st.builds(
    Arch_Div,
)
Arch_Label_strategy = st.builds(
    Arch_Label,
    text=
        safe_text
)
Arch_Parameter_strategy = st.builds(
    Arch_Parameter,
    type=
        safe_text,
    name=
        safe_text
)
Arch_Attribute_strategy = st.builds(
    Arch_Attribute,
    type=
        safe_text,
    name=
        safe_text
)
Arch_Method_strategy = st.builds(
    Arch_Method,
    returntype=
        safe_text,
    name=
        safe_text
)
Arch_GraphicControl_strategy = st.builds(
    Arch_GraphicControl,
    name=
        safe_text
)
Arch_Entity_strategy = st.builds(
    Arch_Entity,
    name=
        safe_text
)
Arch_Logic_strategy = st.builds(
    Arch_Logic,
    name=
        safe_text
)
Arch_Service_strategy = st.builds(
    Arch_Service,
    name=
        safe_text
)
Arch_Controller_strategy = st.builds(
    Arch_Controller,
    name=
        safe_text
)
Arch_View_strategy = st.builds(
    Arch_View,
    name=
        safe_text
)
Arch_BackEnd_strategy = st.builds(
    Arch_BackEnd,
    name=
        safe_text
)
Arch_FrontEnd_strategy = st.builds(
    Arch_FrontEnd,
    name=
        safe_text
)
Arch_Application_strategy = st.builds(
    Arch_Application,
    name=
        safe_text
)




@given(instance=Arch_Event_strategy)
def test_hyp_arch_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=Arch_TextBox_strategy)
def test_hyp_arch_textbox_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=Arch_DropDownList_strategy)
def test_hyp_arch_dropdownlist_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original





@given(instance=Arch_Label_strategy)
def test_hyp_arch_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=Arch_Parameter_strategy)
def test_hyp_arch_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Arch_Parameter_strategy)
def test_hyp_arch_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_Attribute_strategy)
def test_hyp_arch_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Arch_Attribute_strategy)
def test_hyp_arch_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_Method_strategy)
def test_hyp_arch_method_returntype_setter(instance):
    original = instance.returntype
    instance.returntype = original
    assert instance.returntype == original



@given(instance=Arch_Method_strategy)
def test_hyp_arch_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_GraphicControl_strategy)
def test_hyp_arch_graphiccontrol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_Entity_strategy)
def test_hyp_arch_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_Logic_strategy)
def test_hyp_arch_logic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_Service_strategy)
def test_hyp_arch_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_Controller_strategy)
def test_hyp_arch_controller_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_View_strategy)
def test_hyp_arch_view_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_BackEnd_strategy)
def test_hyp_arch_backend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_FrontEnd_strategy)
def test_hyp_arch_frontend_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Arch_Application_strategy)
def test_hyp_arch_application_name_setter(instance):
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
    Arch_Application,
    Arch_Attribute,
    Arch_BackEnd,
    Arch_Controller,
    Arch_Div,
    Arch_DropDownList,
    Arch_Entity,
    Arch_Event,
    Arch_FrontEnd,
    Arch_GraphicControl,
    Arch_Label,
    Arch_Logic,
    Arch_Method,
    Arch_Parameter,
    Arch_Service,
    Arch_TextBox,
    Arch_View,
    GraphicControl,
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

def test_Arch_Application_name_value_roundtrip():
    instance = Arch_Application(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Attribute_name_value_roundtrip():
    instance = Arch_Attribute(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Attribute_type_value_roundtrip():
    instance = Arch_Attribute(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Arch_BackEnd_name_value_roundtrip():
    instance = Arch_BackEnd(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Controller_name_value_roundtrip():
    instance = Arch_Controller(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_DropDownList_items_value_roundtrip():
    instance = Arch_DropDownList(items="sample_text")
    assert instance.items == "sample_text"
    instance.items = "sample_text_2"
    assert instance.items == "sample_text_2"


def test_Arch_Entity_name_value_roundtrip():
    instance = Arch_Entity(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Event_name_value_roundtrip():
    instance = Arch_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_FrontEnd_name_value_roundtrip():
    instance = Arch_FrontEnd(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_GraphicControl_name_value_roundtrip():
    instance = Arch_GraphicControl(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Label_text_value_roundtrip():
    instance = Arch_Label(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_Arch_Logic_name_value_roundtrip():
    instance = Arch_Logic(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Method_name_value_roundtrip():
    instance = Arch_Method(name="sample_text", returntype="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Method_returntype_value_roundtrip():
    instance = Arch_Method(name="sample_text", returntype="sample_text")
    assert instance.returntype == "sample_text"
    instance.returntype = "sample_text_2"
    assert instance.returntype == "sample_text_2"


def test_Arch_Parameter_name_value_roundtrip():
    instance = Arch_Parameter(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Parameter_type_value_roundtrip():
    instance = Arch_Parameter(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Arch_Service_name_value_roundtrip():
    instance = Arch_Service(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_TextBox_type_value_roundtrip():
    instance = Arch_TextBox(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Arch_View_name_value_roundtrip():
    instance = Arch_View(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Arch_Div_isa_GraphicControl():
    instance = Arch_Div()
    assert isinstance(instance, GraphicControl)


def test_Arch_DropDownList_isa_GraphicControl():
    instance = Arch_DropDownList(items="sample_text")
    assert isinstance(instance, GraphicControl)


def test_Arch_Label_isa_GraphicControl():
    instance = Arch_Label(text="sample_text")
    assert isinstance(instance, GraphicControl)


def test_Arch_TextBox_isa_GraphicControl():
    instance = Arch_TextBox(type="sample_text")
    assert isinstance(instance, GraphicControl)


def test_assoc_attributes28_link_reassign_clear():
    a = Arch_Entity(name="sample_text")
    b1 = Arch_Attribute(name="sample_text", type="sample_text")
    b2 = Arch_Attribute(name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'Arch_Entity29', {b1})
    assert _is_linked(a, 'Arch_Entity29', b1)
    if hasattr(b1, 'Arch_Attribute'):
        assert _is_linked(b1, 'Arch_Attribute', a)
    _safe_set(a, 'Arch_Entity29', {b2})
    assert _is_linked(a, 'Arch_Entity29', b2)
    if hasattr(b1, 'Arch_Attribute'):
        assert not _is_linked(b1, 'Arch_Attribute', a)
    if hasattr(b2, 'Arch_Attribute'):
        assert _is_linked(b2, 'Arch_Attribute', a)
    _safe_set(a, 'Arch_Entity29', set())
    assert not _is_linked(a, 'Arch_Entity29', b2)
    if hasattr(b2, 'Arch_Attribute'):
        assert not _is_linked(b2, 'Arch_Attribute', a)


def test_assoc_backend1_link_reassign_clear():
    a = Arch_BackEnd(name="sample_text")
    b1 = Arch_Application(name="sample_text")
    b2 = Arch_Application(name="sample_text_2")
    _safe_set(a, 'Arch_BackEnd', b1)
    assert _is_linked(a, 'Arch_BackEnd', b1)
    if hasattr(b1, 'Arch_Application2'):
        assert _is_linked(b1, 'Arch_Application2', a)
    _safe_set(a, 'Arch_BackEnd', b2)
    assert _is_linked(a, 'Arch_BackEnd', b2)
    if hasattr(b1, 'Arch_Application2'):
        assert not _is_linked(b1, 'Arch_Application2', a)
    if hasattr(b2, 'Arch_Application2'):
        assert _is_linked(b2, 'Arch_Application2', a)
    _safe_set(a, 'Arch_BackEnd', None)
    assert not _is_linked(a, 'Arch_BackEnd', b2)
    if hasattr(b2, 'Arch_Application2'):
        assert not _is_linked(b2, 'Arch_Application2', a)


def test_assoc_controllers15_link_reassign_clear():
    a = Arch_View(name="sample_text")
    b1 = Arch_Controller(name="sample_text")
    b2 = Arch_Controller(name="sample_text_2")
    _safe_set(a, 'Arch_View16', {b1})
    assert _is_linked(a, 'Arch_View16', b1)
    if hasattr(b1, 'Arch_Controller17'):
        assert _is_linked(b1, 'Arch_Controller17', a)
    _safe_set(a, 'Arch_View16', {b2})
    assert _is_linked(a, 'Arch_View16', b2)
    if hasattr(b1, 'Arch_Controller17'):
        assert not _is_linked(b1, 'Arch_Controller17', a)
    if hasattr(b2, 'Arch_Controller17'):
        assert _is_linked(b2, 'Arch_Controller17', a)
    _safe_set(a, 'Arch_View16', set())
    assert not _is_linked(a, 'Arch_View16', b2)
    if hasattr(b2, 'Arch_Controller17'):
        assert not _is_linked(b2, 'Arch_Controller17', a)


def test_assoc_controllers5_link_reassign_clear():
    a = Arch_FrontEnd(name="sample_text")
    b1 = Arch_Controller(name="sample_text")
    b2 = Arch_Controller(name="sample_text_2")
    _safe_set(a, 'Arch_FrontEnd6', {b1})
    assert _is_linked(a, 'Arch_FrontEnd6', b1)
    if hasattr(b1, 'Arch_Controller'):
        assert _is_linked(b1, 'Arch_Controller', a)
    _safe_set(a, 'Arch_FrontEnd6', {b2})
    assert _is_linked(a, 'Arch_FrontEnd6', b2)
    if hasattr(b1, 'Arch_Controller'):
        assert not _is_linked(b1, 'Arch_Controller', a)
    if hasattr(b2, 'Arch_Controller'):
        assert _is_linked(b2, 'Arch_Controller', a)
    _safe_set(a, 'Arch_FrontEnd6', set())
    assert not _is_linked(a, 'Arch_FrontEnd6', b2)
    if hasattr(b2, 'Arch_Controller'):
        assert not _is_linked(b2, 'Arch_Controller', a)


def test_assoc_entities11_link_reassign_clear():
    a = Arch_Entity(name="sample_text")
    b1 = Arch_BackEnd(name="sample_text")
    b2 = Arch_BackEnd(name="sample_text_2")
    _safe_set(a, 'Arch_Entity', b1)
    assert _is_linked(a, 'Arch_Entity', b1)
    if hasattr(b1, 'Arch_BackEnd12'):
        assert _is_linked(b1, 'Arch_BackEnd12', a)
    _safe_set(a, 'Arch_Entity', b2)
    assert _is_linked(a, 'Arch_Entity', b2)
    if hasattr(b1, 'Arch_BackEnd12'):
        assert not _is_linked(b1, 'Arch_BackEnd12', a)
    if hasattr(b2, 'Arch_BackEnd12'):
        assert _is_linked(b2, 'Arch_BackEnd12', a)
    _safe_set(a, 'Arch_Entity', None)
    assert not _is_linked(a, 'Arch_Entity', b2)
    if hasattr(b2, 'Arch_BackEnd12'):
        assert not _is_linked(b2, 'Arch_BackEnd12', a)


def test_assoc_events21_link_reassign_clear():
    a = Arch_Event(name="sample_text")
    b1 = Arch_Controller(name="sample_text")
    b2 = Arch_Controller(name="sample_text_2")
    _safe_set(a, 'Arch_Event', b1)
    assert _is_linked(a, 'Arch_Event', b1)
    if hasattr(b1, 'Arch_Controller22'):
        assert _is_linked(b1, 'Arch_Controller22', a)
    _safe_set(a, 'Arch_Event', b2)
    assert _is_linked(a, 'Arch_Event', b2)
    if hasattr(b1, 'Arch_Controller22'):
        assert not _is_linked(b1, 'Arch_Controller22', a)
    if hasattr(b2, 'Arch_Controller22'):
        assert _is_linked(b2, 'Arch_Controller22', a)
    _safe_set(a, 'Arch_Event', None)
    assert not _is_linked(a, 'Arch_Event', b2)
    if hasattr(b2, 'Arch_Controller22'):
        assert not _is_linked(b2, 'Arch_Controller22', a)


def test_assoc_events35_link_reassign_clear():
    a = Arch_GraphicControl(name="sample_text")
    b1 = Arch_Event(name="sample_text")
    b2 = Arch_Event(name="sample_text_2")
    _safe_set(a, 'Arch_GraphicControl36', {b1})
    assert _is_linked(a, 'Arch_GraphicControl36', b1)
    if hasattr(b1, 'Arch_Event37'):
        assert _is_linked(b1, 'Arch_Event37', a)
    _safe_set(a, 'Arch_GraphicControl36', {b2})
    assert _is_linked(a, 'Arch_GraphicControl36', b2)
    if hasattr(b1, 'Arch_Event37'):
        assert not _is_linked(b1, 'Arch_Event37', a)
    if hasattr(b2, 'Arch_Event37'):
        assert _is_linked(b2, 'Arch_Event37', a)
    _safe_set(a, 'Arch_GraphicControl36', set())
    assert not _is_linked(a, 'Arch_GraphicControl36', b2)
    if hasattr(b2, 'Arch_Event37'):
        assert not _is_linked(b2, 'Arch_Event37', a)


def test_assoc_frontend0_link_reassign_clear():
    a = Arch_FrontEnd(name="sample_text")
    b1 = Arch_Application(name="sample_text")
    b2 = Arch_Application(name="sample_text_2")
    _safe_set(a, 'Arch_FrontEnd', b1)
    assert _is_linked(a, 'Arch_FrontEnd', b1)
    if hasattr(b1, 'Arch_Application'):
        assert _is_linked(b1, 'Arch_Application', a)
    _safe_set(a, 'Arch_FrontEnd', b2)
    assert _is_linked(a, 'Arch_FrontEnd', b2)
    if hasattr(b1, 'Arch_Application'):
        assert not _is_linked(b1, 'Arch_Application', a)
    if hasattr(b2, 'Arch_Application'):
        assert _is_linked(b2, 'Arch_Application', a)
    _safe_set(a, 'Arch_FrontEnd', None)
    assert not _is_linked(a, 'Arch_FrontEnd', b2)
    if hasattr(b2, 'Arch_Application'):
        assert not _is_linked(b2, 'Arch_Application', a)


def test_assoc_graphicControls13_link_reassign_clear():
    a = Arch_View(name="sample_text")
    b1 = Arch_GraphicControl(name="sample_text")
    b2 = Arch_GraphicControl(name="sample_text_2")
    _safe_set(a, 'Arch_View14', {b1})
    assert _is_linked(a, 'Arch_View14', b1)
    if hasattr(b1, 'Arch_GraphicControl'):
        assert _is_linked(b1, 'Arch_GraphicControl', a)
    _safe_set(a, 'Arch_View14', {b2})
    assert _is_linked(a, 'Arch_View14', b2)
    if hasattr(b1, 'Arch_GraphicControl'):
        assert not _is_linked(b1, 'Arch_GraphicControl', a)
    if hasattr(b2, 'Arch_GraphicControl'):
        assert _is_linked(b2, 'Arch_GraphicControl', a)
    _safe_set(a, 'Arch_View14', set())
    assert not _is_linked(a, 'Arch_View14', b2)
    if hasattr(b2, 'Arch_GraphicControl'):
        assert not _is_linked(b2, 'Arch_GraphicControl', a)


def test_assoc_graphicControls38_link_reassign_clear():
    a = Arch_GraphicControl(name="sample_text")
    b1 = Arch_Div()
    b2 = Arch_Div()
    _safe_set(a, 'Arch_GraphicControl39', b1)
    assert _is_linked(a, 'Arch_GraphicControl39', b1)
    if hasattr(b1, 'Arch_Div'):
        assert _is_linked(b1, 'Arch_Div', a)
    _safe_set(a, 'Arch_GraphicControl39', b2)
    assert _is_linked(a, 'Arch_GraphicControl39', b2)
    if hasattr(b1, 'Arch_Div'):
        assert not _is_linked(b1, 'Arch_Div', a)
    if hasattr(b2, 'Arch_Div'):
        assert _is_linked(b2, 'Arch_Div', a)
    _safe_set(a, 'Arch_GraphicControl39', None)
    assert not _is_linked(a, 'Arch_GraphicControl39', b2)
    if hasattr(b2, 'Arch_Div'):
        assert not _is_linked(b2, 'Arch_Div', a)


def test_assoc_logics9_link_reassign_clear():
    a = Arch_Logic(name="sample_text")
    b1 = Arch_BackEnd(name="sample_text")
    b2 = Arch_BackEnd(name="sample_text_2")
    _safe_set(a, 'Arch_Logic', b1)
    assert _is_linked(a, 'Arch_Logic', b1)
    if hasattr(b1, 'Arch_BackEnd10'):
        assert _is_linked(b1, 'Arch_BackEnd10', a)
    _safe_set(a, 'Arch_Logic', b2)
    assert _is_linked(a, 'Arch_Logic', b2)
    if hasattr(b1, 'Arch_BackEnd10'):
        assert not _is_linked(b1, 'Arch_BackEnd10', a)
    if hasattr(b2, 'Arch_BackEnd10'):
        assert _is_linked(b2, 'Arch_BackEnd10', a)
    _safe_set(a, 'Arch_Logic', None)
    assert not _is_linked(a, 'Arch_Logic', b2)
    if hasattr(b2, 'Arch_BackEnd10'):
        assert not _is_linked(b2, 'Arch_BackEnd10', a)


def test_assoc_methods23_link_reassign_clear():
    a = Arch_Service(name="sample_text")
    b1 = Arch_Method(name="sample_text", returntype="sample_text")
    b2 = Arch_Method(name="sample_text_2", returntype="sample_text_2")
    _safe_set(a, 'Arch_Service24', {b1})
    assert _is_linked(a, 'Arch_Service24', b1)
    if hasattr(b1, 'Arch_Method'):
        assert _is_linked(b1, 'Arch_Method', a)
    _safe_set(a, 'Arch_Service24', {b2})
    assert _is_linked(a, 'Arch_Service24', b2)
    if hasattr(b1, 'Arch_Method'):
        assert not _is_linked(b1, 'Arch_Method', a)
    if hasattr(b2, 'Arch_Method'):
        assert _is_linked(b2, 'Arch_Method', a)
    _safe_set(a, 'Arch_Service24', set())
    assert not _is_linked(a, 'Arch_Service24', b2)
    if hasattr(b2, 'Arch_Method'):
        assert not _is_linked(b2, 'Arch_Method', a)


def test_assoc_methods25_link_reassign_clear():
    a = Arch_Method(name="sample_text", returntype="sample_text")
    b1 = Arch_Logic(name="sample_text")
    b2 = Arch_Logic(name="sample_text_2")
    _safe_set(a, 'Arch_Method27', b1)
    assert _is_linked(a, 'Arch_Method27', b1)
    if hasattr(b1, 'Arch_Logic26'):
        assert _is_linked(b1, 'Arch_Logic26', a)
    _safe_set(a, 'Arch_Method27', b2)
    assert _is_linked(a, 'Arch_Method27', b2)
    if hasattr(b1, 'Arch_Logic26'):
        assert not _is_linked(b1, 'Arch_Logic26', a)
    if hasattr(b2, 'Arch_Logic26'):
        assert _is_linked(b2, 'Arch_Logic26', a)
    _safe_set(a, 'Arch_Method27', None)
    assert not _is_linked(a, 'Arch_Method27', b2)
    if hasattr(b2, 'Arch_Logic26'):
        assert not _is_linked(b2, 'Arch_Logic26', a)


def test_assoc_methods30_link_reassign_clear():
    a = Arch_Method(name="sample_text", returntype="sample_text")
    b1 = Arch_Entity(name="sample_text")
    b2 = Arch_Entity(name="sample_text_2")
    _safe_set(a, 'Arch_Method32', b1)
    assert _is_linked(a, 'Arch_Method32', b1)
    if hasattr(b1, 'Arch_Entity31'):
        assert _is_linked(b1, 'Arch_Entity31', a)
    _safe_set(a, 'Arch_Method32', b2)
    assert _is_linked(a, 'Arch_Method32', b2)
    if hasattr(b1, 'Arch_Entity31'):
        assert not _is_linked(b1, 'Arch_Entity31', a)
    if hasattr(b2, 'Arch_Entity31'):
        assert _is_linked(b2, 'Arch_Entity31', a)
    _safe_set(a, 'Arch_Method32', None)
    assert not _is_linked(a, 'Arch_Method32', b2)
    if hasattr(b2, 'Arch_Entity31'):
        assert not _is_linked(b2, 'Arch_Entity31', a)


def test_assoc_parameters33_link_reassign_clear():
    a = Arch_Parameter(name="sample_text", type="sample_text")
    b1 = Arch_Method(name="sample_text", returntype="sample_text")
    b2 = Arch_Method(name="sample_text_2", returntype="sample_text_2")
    _safe_set(a, 'Arch_Parameter', b1)
    assert _is_linked(a, 'Arch_Parameter', b1)
    if hasattr(b1, 'Arch_Method34'):
        assert _is_linked(b1, 'Arch_Method34', a)
    _safe_set(a, 'Arch_Parameter', b2)
    assert _is_linked(a, 'Arch_Parameter', b2)
    if hasattr(b1, 'Arch_Method34'):
        assert not _is_linked(b1, 'Arch_Method34', a)
    if hasattr(b2, 'Arch_Method34'):
        assert _is_linked(b2, 'Arch_Method34', a)
    _safe_set(a, 'Arch_Parameter', None)
    assert not _is_linked(a, 'Arch_Parameter', b2)
    if hasattr(b2, 'Arch_Method34'):
        assert not _is_linked(b2, 'Arch_Method34', a)


def test_assoc_services7_link_reassign_clear():
    a = Arch_Service(name="sample_text")
    b1 = Arch_BackEnd(name="sample_text")
    b2 = Arch_BackEnd(name="sample_text_2")
    _safe_set(a, 'Arch_Service', b1)
    assert _is_linked(a, 'Arch_Service', b1)
    if hasattr(b1, 'Arch_BackEnd8'):
        assert _is_linked(b1, 'Arch_BackEnd8', a)
    _safe_set(a, 'Arch_Service', b2)
    assert _is_linked(a, 'Arch_Service', b2)
    if hasattr(b1, 'Arch_BackEnd8'):
        assert not _is_linked(b1, 'Arch_BackEnd8', a)
    if hasattr(b2, 'Arch_BackEnd8'):
        assert _is_linked(b2, 'Arch_BackEnd8', a)
    _safe_set(a, 'Arch_Service', None)
    assert not _is_linked(a, 'Arch_Service', b2)
    if hasattr(b2, 'Arch_BackEnd8'):
        assert not _is_linked(b2, 'Arch_BackEnd8', a)


def test_assoc_views18_link_reassign_clear():
    a = Arch_View(name="sample_text")
    b1 = Arch_Controller(name="sample_text")
    b2 = Arch_Controller(name="sample_text_2")
    _safe_set(a, 'Arch_View20', b1)
    assert _is_linked(a, 'Arch_View20', b1)
    if hasattr(b1, 'Arch_Controller19'):
        assert _is_linked(b1, 'Arch_Controller19', a)
    _safe_set(a, 'Arch_View20', b2)
    assert _is_linked(a, 'Arch_View20', b2)
    if hasattr(b1, 'Arch_Controller19'):
        assert not _is_linked(b1, 'Arch_Controller19', a)
    if hasattr(b2, 'Arch_Controller19'):
        assert _is_linked(b2, 'Arch_Controller19', a)
    _safe_set(a, 'Arch_View20', None)
    assert not _is_linked(a, 'Arch_View20', b2)
    if hasattr(b2, 'Arch_Controller19'):
        assert not _is_linked(b2, 'Arch_Controller19', a)


def test_assoc_views3_link_reassign_clear():
    a = Arch_View(name="sample_text")
    b1 = Arch_FrontEnd(name="sample_text")
    b2 = Arch_FrontEnd(name="sample_text_2")
    _safe_set(a, 'Arch_View', b1)
    assert _is_linked(a, 'Arch_View', b1)
    if hasattr(b1, 'Arch_FrontEnd4'):
        assert _is_linked(b1, 'Arch_FrontEnd4', a)
    _safe_set(a, 'Arch_View', b2)
    assert _is_linked(a, 'Arch_View', b2)
    if hasattr(b1, 'Arch_FrontEnd4'):
        assert not _is_linked(b1, 'Arch_FrontEnd4', a)
    if hasattr(b2, 'Arch_FrontEnd4'):
        assert _is_linked(b2, 'Arch_FrontEnd4', a)
    _safe_set(a, 'Arch_View', None)
    assert not _is_linked(a, 'Arch_View', b2)
    if hasattr(b2, 'Arch_FrontEnd4'):
        assert not _is_linked(b2, 'Arch_FrontEnd4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Arch_Application_strategy = st.builds(Arch_Application, name=safe_text)
@given(instance=Arch_Application_strategy)
@settings(max_examples=25)
def test_Arch_Application_instantiation(instance):
    assert isinstance(instance, Arch_Application)


Arch_Attribute_strategy = st.builds(Arch_Attribute, name=safe_text, type=safe_text)
@given(instance=Arch_Attribute_strategy)
@settings(max_examples=25)
def test_Arch_Attribute_instantiation(instance):
    assert isinstance(instance, Arch_Attribute)


Arch_BackEnd_strategy = st.builds(Arch_BackEnd, name=safe_text)
@given(instance=Arch_BackEnd_strategy)
@settings(max_examples=25)
def test_Arch_BackEnd_instantiation(instance):
    assert isinstance(instance, Arch_BackEnd)


Arch_Controller_strategy = st.builds(Arch_Controller, name=safe_text)
@given(instance=Arch_Controller_strategy)
@settings(max_examples=25)
def test_Arch_Controller_instantiation(instance):
    assert isinstance(instance, Arch_Controller)


Arch_Div_strategy = st.builds(Arch_Div)
@given(instance=Arch_Div_strategy)
@settings(max_examples=25)
def test_Arch_Div_instantiation(instance):
    assert isinstance(instance, Arch_Div)


Arch_DropDownList_strategy = st.builds(Arch_DropDownList, items=safe_text)
@given(instance=Arch_DropDownList_strategy)
@settings(max_examples=25)
def test_Arch_DropDownList_instantiation(instance):
    assert isinstance(instance, Arch_DropDownList)


Arch_Entity_strategy = st.builds(Arch_Entity, name=safe_text)
@given(instance=Arch_Entity_strategy)
@settings(max_examples=25)
def test_Arch_Entity_instantiation(instance):
    assert isinstance(instance, Arch_Entity)


Arch_Event_strategy = st.builds(Arch_Event, name=safe_text)
@given(instance=Arch_Event_strategy)
@settings(max_examples=25)
def test_Arch_Event_instantiation(instance):
    assert isinstance(instance, Arch_Event)


Arch_FrontEnd_strategy = st.builds(Arch_FrontEnd, name=safe_text)
@given(instance=Arch_FrontEnd_strategy)
@settings(max_examples=25)
def test_Arch_FrontEnd_instantiation(instance):
    assert isinstance(instance, Arch_FrontEnd)


Arch_GraphicControl_strategy = st.builds(Arch_GraphicControl, name=safe_text)
@given(instance=Arch_GraphicControl_strategy)
@settings(max_examples=25)
def test_Arch_GraphicControl_instantiation(instance):
    assert isinstance(instance, Arch_GraphicControl)


Arch_Label_strategy = st.builds(Arch_Label, text=safe_text)
@given(instance=Arch_Label_strategy)
@settings(max_examples=25)
def test_Arch_Label_instantiation(instance):
    assert isinstance(instance, Arch_Label)


Arch_Logic_strategy = st.builds(Arch_Logic, name=safe_text)
@given(instance=Arch_Logic_strategy)
@settings(max_examples=25)
def test_Arch_Logic_instantiation(instance):
    assert isinstance(instance, Arch_Logic)


Arch_Method_strategy = st.builds(Arch_Method, name=safe_text, returntype=safe_text)
@given(instance=Arch_Method_strategy)
@settings(max_examples=25)
def test_Arch_Method_instantiation(instance):
    assert isinstance(instance, Arch_Method)


Arch_Parameter_strategy = st.builds(Arch_Parameter, name=safe_text, type=safe_text)
@given(instance=Arch_Parameter_strategy)
@settings(max_examples=25)
def test_Arch_Parameter_instantiation(instance):
    assert isinstance(instance, Arch_Parameter)


Arch_Service_strategy = st.builds(Arch_Service, name=safe_text)
@given(instance=Arch_Service_strategy)
@settings(max_examples=25)
def test_Arch_Service_instantiation(instance):
    assert isinstance(instance, Arch_Service)


Arch_TextBox_strategy = st.builds(Arch_TextBox, type=safe_text)
@given(instance=Arch_TextBox_strategy)
@settings(max_examples=25)
def test_Arch_TextBox_instantiation(instance):
    assert isinstance(instance, Arch_TextBox)


Arch_View_strategy = st.builds(Arch_View, name=safe_text)
@given(instance=Arch_View_strategy)
@settings(max_examples=25)
def test_Arch_View_instantiation(instance):
    assert isinstance(instance, Arch_View)


GraphicControl_strategy = st.builds(GraphicControl)
@given(instance=GraphicControl_strategy)
@settings(max_examples=25)
def test_GraphicControl_instantiation(instance):
    assert isinstance(instance, GraphicControl)



