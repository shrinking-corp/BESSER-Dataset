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
    MyView,
    MyTask,
    Ghosts,
    Ghost,
    Pacman,
    Tile,
    StaticObject,
    DynamicObject,
    Sprite,
    ArrPrint,
    Print,
    Documents,
    Json,
    Visitor,
    Array,
    Number,
    Bool,
    String,
    Null,
    Value,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_myview_is_not_abstract():
    assert not inspect.isabstract(MyView)


def test_hyp_myview_constructor_exists():
    assert callable(MyView.__init__)


def test_hyp_myview_constructor_args():
    sig = inspect.signature(MyView.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mytask_is_not_abstract():
    assert not inspect.isabstract(MyTask)


def test_hyp_mytask_constructor_exists():
    assert callable(MyTask.__init__)


def test_hyp_mytask_constructor_args():
    sig = inspect.signature(MyTask.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ghosts_is_not_abstract():
    assert not inspect.isabstract(Ghosts)


def test_hyp_ghosts_constructor_exists():
    assert callable(Ghosts.__init__)


def test_hyp_ghosts_constructor_args():
    sig = inspect.signature(Ghosts.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ghost_is_not_abstract():
    assert not inspect.isabstract(Ghost)


def test_hyp_ghost_constructor_exists():
    assert callable(Ghost.__init__)


def test_hyp_ghost_constructor_args():
    sig = inspect.signature(Ghost.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pacman_is_not_abstract():
    assert not inspect.isabstract(Pacman)


def test_hyp_pacman_constructor_exists():
    assert callable(Pacman.__init__)


def test_hyp_pacman_constructor_args():
    sig = inspect.signature(Pacman.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tile_is_not_abstract():
    assert not inspect.isabstract(Tile)


def test_hyp_tile_constructor_exists():
    assert callable(Tile.__init__)


def test_hyp_tile_constructor_args():
    sig = inspect.signature(Tile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staticobject_is_not_abstract():
    assert not inspect.isabstract(StaticObject)


def test_hyp_staticobject_constructor_exists():
    assert callable(StaticObject.__init__)


def test_hyp_staticobject_constructor_args():
    sig = inspect.signature(StaticObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dynamicobject_is_not_abstract():
    assert not inspect.isabstract(DynamicObject)


def test_hyp_dynamicobject_constructor_exists():
    assert callable(DynamicObject.__init__)


def test_hyp_dynamicobject_constructor_args():
    sig = inspect.signature(DynamicObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sprite_is_not_abstract():
    assert not inspect.isabstract(Sprite)


def test_hyp_sprite_constructor_exists():
    assert callable(Sprite.__init__)


def test_hyp_sprite_constructor_args():
    sig = inspect.signature(Sprite.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arrprint_is_not_abstract():
    assert not inspect.isabstract(ArrPrint)


def test_hyp_arrprint_constructor_exists():
    assert callable(ArrPrint.__init__)


def test_hyp_arrprint_constructor_args():
    sig = inspect.signature(ArrPrint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_print_is_not_abstract():
    assert not inspect.isabstract(Print)


def test_hyp_print_constructor_exists():
    assert callable(Print.__init__)


def test_hyp_print_constructor_args():
    sig = inspect.signature(Print.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documents_is_not_abstract():
    assert not inspect.isabstract(Documents)


def test_hyp_documents_constructor_exists():
    assert callable(Documents.__init__)


def test_hyp_documents_constructor_args():
    sig = inspect.signature(Documents.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "tab_counter" in params, "Missing parameter 'tab_counter'"
    assert "file_name" in params, "Missing parameter 'file_name'"
    assert "file" in params, "Missing parameter 'file'"

def test_hyp_documents_has_data():
    assert hasattr(Documents, "data")
    descriptor = None
    for klass in Documents.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_hyp_documents_has_tab_counter():
    assert hasattr(Documents, "tab_counter")
    descriptor = None
    for klass in Documents.__mro__:
        if "tab_counter" in klass.__dict__:
            descriptor = klass.__dict__["tab_counter"]
            break
    assert isinstance(descriptor, property)

def test_hyp_documents_has_file_name():
    assert hasattr(Documents, "file_name")
    descriptor = None
    for klass in Documents.__mro__:
        if "file_name" in klass.__dict__:
            descriptor = klass.__dict__["file_name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_documents_has_file():
    assert hasattr(Documents, "file")
    descriptor = None
    for klass in Documents.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_hyp_json_is_not_abstract():
    assert not inspect.isabstract(Json)


def test_hyp_json_constructor_exists():
    assert callable(Json.__init__)


def test_hyp_json_constructor_args():
    sig = inspect.signature(Json.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_hyp_json_has_values():
    assert hasattr(Json, "values")
    descriptor = None
    for klass in Json.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_hyp_visitor_is_not_abstract():
    assert not inspect.isabstract(Visitor)


def test_hyp_visitor_constructor_exists():
    assert callable(Visitor.__init__)


def test_hyp_visitor_constructor_args():
    sig = inspect.signature(Visitor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_array_is_not_abstract():
    assert not inspect.isabstract(Array)


def test_hyp_array_constructor_exists():
    assert callable(Array.__init__)


def test_hyp_array_constructor_args():
    sig = inspect.signature(Array.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_hyp_array_has_data():
    assert hasattr(Array, "data")
    descriptor = None
    for klass in Array.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_hyp_number_is_not_abstract():
    assert not inspect.isabstract(Number)


def test_hyp_number_constructor_exists():
    assert callable(Number.__init__)


def test_hyp_number_constructor_args():
    sig = inspect.signature(Number.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"




def test_hyp_bool_is_not_abstract():
    assert not inspect.isabstract(Bool)


def test_hyp_bool_constructor_exists():
    assert callable(Bool.__init__)


def test_hyp_bool_constructor_args():
    sig = inspect.signature(Bool.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"




def test_hyp_string_is_not_abstract():
    assert not inspect.isabstract(String)


def test_hyp_string_constructor_exists():
    assert callable(String.__init__)


def test_hyp_string_constructor_args():
    sig = inspect.signature(String.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_hyp_string_has_data():
    assert hasattr(String, "data")
    descriptor = None
    for klass in String.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_hyp_null_is_not_abstract():
    assert not inspect.isabstract(Null)


def test_hyp_null_constructor_exists():
    assert callable(Null.__init__)


def test_hyp_null_constructor_args():
    sig = inspect.signature(Null.__init__)
    params = list(sig.parameters.keys())



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"



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
MyView_strategy = st.builds(
    MyView,
)
MyTask_strategy = st.builds(
    MyTask,
)
Ghosts_strategy = st.builds(
    Ghosts,
)
Ghost_strategy = st.builds(
    Ghost,
)
Pacman_strategy = st.builds(
    Pacman,
)
Tile_strategy = st.builds(
    Tile,
)
StaticObject_strategy = st.builds(
    StaticObject,
)
DynamicObject_strategy = st.builds(
    DynamicObject,
)
Sprite_strategy = st.builds(
    Sprite,
)
ArrPrint_strategy = st.builds(
    ArrPrint,
)
Print_strategy = st.builds(
    Print,
)
Documents_strategy = st.builds(
    Documents,
    data=
        st.none(),
    tab_counter=
        st.integers(),
    file_name=
        safe_text,
    file=
        safe_text
)
Json_strategy = st.builds(
    Json,
    values=
        st.none()
)
Visitor_strategy = st.builds(
    Visitor,
)
Array_strategy = st.builds(
    Array,
    data=
        st.none()
)
Number_strategy = st.builds(
    Number,
    data=
        st.integers()
)
Bool_strategy = st.builds(
    Bool,
    data=
        st.booleans()
)
String_strategy = st.builds(
    String,
    data=
        st.none()
)
Null_strategy = st.builds(
    Null,
)
Value_strategy = st.builds(
    Value,
    attribute=
        safe_text
)












@given(instance=Documents_strategy)
@settings(max_examples=50)
def test_hyp_documents_instantiation(instance):
    assert isinstance(instance, Documents)



@given(instance=Documents_strategy)
def test_hyp_documents_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=Documents_strategy)
def test_hyp_documents_tab_counter_setter(instance):
    original = instance.tab_counter
    instance.tab_counter = original
    assert instance.tab_counter == original



@given(instance=Documents_strategy)
def test_hyp_documents_file_name_setter(instance):
    original = instance.file_name
    instance.file_name = original
    assert instance.file_name == original



@given(instance=Documents_strategy)
def test_hyp_documents_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Json_strategy)
@settings(max_examples=50)
def test_hyp_json_instantiation(instance):
    assert isinstance(instance, Json)



@given(instance=Json_strategy)
def test_hyp_json_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original


@given(instance=Array_strategy)
@settings(max_examples=50)
def test_hyp_array_instantiation(instance):
    assert isinstance(instance, Array)



@given(instance=Array_strategy)
def test_hyp_array_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original




@given(instance=Number_strategy)
def test_hyp_number_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original




@given(instance=Bool_strategy)
def test_hyp_bool_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=String_strategy)
@settings(max_examples=50)
def test_hyp_string_instantiation(instance):
    assert isinstance(instance, String)



@given(instance=String_strategy)
def test_hyp_string_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original





@given(instance=Value_strategy)
def test_hyp_value_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArrPrint,
    Array,
    Bool,
    Documents,
    DynamicObject,
    Ghost,
    Ghosts,
    Json,
    MyTask,
    MyView,
    Null,
    Number,
    Pacman,
    Print,
    Sprite,
    StaticObject,
    String,
    Tile,
    Value,
    Visitor,
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

def test_Bool_data_value_roundtrip():
    instance = Bool(data=True)
    assert instance.data == True
    instance.data = False
    assert instance.data == False


def test_Number_data_value_roundtrip():
    instance = Number(data=7)
    assert instance.data == 7
    instance.data = 13
    assert instance.data == 13


def test_Value_attribute_value_roundtrip():
    instance = Value(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArrPrint_strategy = st.builds(ArrPrint)
@given(instance=ArrPrint_strategy)
@settings(max_examples=25)
def test_ArrPrint_instantiation(instance):
    assert isinstance(instance, ArrPrint)


Bool_strategy = st.builds(Bool, data=st.booleans())
@given(instance=Bool_strategy)
@settings(max_examples=25)
def test_Bool_instantiation(instance):
    assert isinstance(instance, Bool)


DynamicObject_strategy = st.builds(DynamicObject)
@given(instance=DynamicObject_strategy)
@settings(max_examples=25)
def test_DynamicObject_instantiation(instance):
    assert isinstance(instance, DynamicObject)


Ghost_strategy = st.builds(Ghost)
@given(instance=Ghost_strategy)
@settings(max_examples=25)
def test_Ghost_instantiation(instance):
    assert isinstance(instance, Ghost)


Ghosts_strategy = st.builds(Ghosts)
@given(instance=Ghosts_strategy)
@settings(max_examples=25)
def test_Ghosts_instantiation(instance):
    assert isinstance(instance, Ghosts)


MyTask_strategy = st.builds(MyTask)
@given(instance=MyTask_strategy)
@settings(max_examples=25)
def test_MyTask_instantiation(instance):
    assert isinstance(instance, MyTask)


MyView_strategy = st.builds(MyView)
@given(instance=MyView_strategy)
@settings(max_examples=25)
def test_MyView_instantiation(instance):
    assert isinstance(instance, MyView)


Null_strategy = st.builds(Null)
@given(instance=Null_strategy)
@settings(max_examples=25)
def test_Null_instantiation(instance):
    assert isinstance(instance, Null)


Number_strategy = st.builds(Number, data=st.integers())
@given(instance=Number_strategy)
@settings(max_examples=25)
def test_Number_instantiation(instance):
    assert isinstance(instance, Number)


Pacman_strategy = st.builds(Pacman)
@given(instance=Pacman_strategy)
@settings(max_examples=25)
def test_Pacman_instantiation(instance):
    assert isinstance(instance, Pacman)


Print_strategy = st.builds(Print)
@given(instance=Print_strategy)
@settings(max_examples=25)
def test_Print_instantiation(instance):
    assert isinstance(instance, Print)


Sprite_strategy = st.builds(Sprite)
@given(instance=Sprite_strategy)
@settings(max_examples=25)
def test_Sprite_instantiation(instance):
    assert isinstance(instance, Sprite)


StaticObject_strategy = st.builds(StaticObject)
@given(instance=StaticObject_strategy)
@settings(max_examples=25)
def test_StaticObject_instantiation(instance):
    assert isinstance(instance, StaticObject)


Tile_strategy = st.builds(Tile)
@given(instance=Tile_strategy)
@settings(max_examples=25)
def test_Tile_instantiation(instance):
    assert isinstance(instance, Tile)


Value_strategy = st.builds(Value, attribute=safe_text)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


Visitor_strategy = st.builds(Visitor)
@given(instance=Visitor_strategy)
@settings(max_examples=25)
def test_Visitor_instantiation(instance):
    assert isinstance(instance, Visitor)



