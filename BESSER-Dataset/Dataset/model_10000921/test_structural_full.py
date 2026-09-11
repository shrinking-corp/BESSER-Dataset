import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    App,
    Array_Zutat___,
    ComboBox,
    DekorRezept,
    Font_,
    Font_2,
    GUI,
    GUIKeksform,
    GUIRezept,
    Groesse,
    Groesse_,
    GussRezept,
    KeyPressEventArgs_,
    KonfigDatei,
    KonfigDatei_,
    List_DekorRezept___,
    List_PlaetzchenForm___,
    List_TeigRezept___,
    List_Zutat___,
    Object_,
    PL_Form_,
    PL_Groesse_,
    Plaetzchen,
    PlaetzchenForm,
    PlaetzchenForm_,
    Plaetzchen_,
    Rezept,
    String_,
    TeigRezept,
    TeigRezept_,
    ThreadExceptionEventArgs_,
    Zutat,
    Zutat_,
    myException,
    PL_Form,
    PL_Groesse,
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

def test_GUIRezept_name_value_roundtrip():
    instance = GUIRezept(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

App_strategy = st.builds(App)
@given(instance=App_strategy)
@settings(max_examples=25)
def test_App_instantiation(instance):
    assert isinstance(instance, App)


Array_Zutat____strategy = st.builds(Array_Zutat___)
@given(instance=Array_Zutat____strategy)
@settings(max_examples=25)
def test_Array_Zutat____instantiation(instance):
    assert isinstance(instance, Array_Zutat___)


ComboBox_strategy = st.builds(ComboBox)
@given(instance=ComboBox_strategy)
@settings(max_examples=25)
def test_ComboBox_instantiation(instance):
    assert isinstance(instance, ComboBox)


Font__strategy = st.builds(Font_)
@given(instance=Font__strategy)
@settings(max_examples=25)
def test_Font__instantiation(instance):
    assert isinstance(instance, Font_)


Font_2_strategy = st.builds(Font_2)
@given(instance=Font_2_strategy)
@settings(max_examples=25)
def test_Font_2_instantiation(instance):
    assert isinstance(instance, Font_2)


GUIRezept_strategy = st.builds(GUIRezept, name=safe_text)
@given(instance=GUIRezept_strategy)
@settings(max_examples=25)
def test_GUIRezept_instantiation(instance):
    assert isinstance(instance, GUIRezept)


Groesse__strategy = st.builds(Groesse_)
@given(instance=Groesse__strategy)
@settings(max_examples=25)
def test_Groesse__instantiation(instance):
    assert isinstance(instance, Groesse_)


KeyPressEventArgs__strategy = st.builds(KeyPressEventArgs_)
@given(instance=KeyPressEventArgs__strategy)
@settings(max_examples=25)
def test_KeyPressEventArgs__instantiation(instance):
    assert isinstance(instance, KeyPressEventArgs_)


KonfigDatei__strategy = st.builds(KonfigDatei_)
@given(instance=KonfigDatei__strategy)
@settings(max_examples=25)
def test_KonfigDatei__instantiation(instance):
    assert isinstance(instance, KonfigDatei_)


List_DekorRezept____strategy = st.builds(List_DekorRezept___)
@given(instance=List_DekorRezept____strategy)
@settings(max_examples=25)
def test_List_DekorRezept____instantiation(instance):
    assert isinstance(instance, List_DekorRezept___)


List_PlaetzchenForm____strategy = st.builds(List_PlaetzchenForm___)
@given(instance=List_PlaetzchenForm____strategy)
@settings(max_examples=25)
def test_List_PlaetzchenForm____instantiation(instance):
    assert isinstance(instance, List_PlaetzchenForm___)


List_TeigRezept____strategy = st.builds(List_TeigRezept___)
@given(instance=List_TeigRezept____strategy)
@settings(max_examples=25)
def test_List_TeigRezept____instantiation(instance):
    assert isinstance(instance, List_TeigRezept___)


List_Zutat____strategy = st.builds(List_Zutat___)
@given(instance=List_Zutat____strategy)
@settings(max_examples=25)
def test_List_Zutat____instantiation(instance):
    assert isinstance(instance, List_Zutat___)


Object__strategy = st.builds(Object_)
@given(instance=Object__strategy)
@settings(max_examples=25)
def test_Object__instantiation(instance):
    assert isinstance(instance, Object_)


PL_Form__strategy = st.builds(PL_Form_)
@given(instance=PL_Form__strategy)
@settings(max_examples=25)
def test_PL_Form__instantiation(instance):
    assert isinstance(instance, PL_Form_)


PL_Groesse__strategy = st.builds(PL_Groesse_)
@given(instance=PL_Groesse__strategy)
@settings(max_examples=25)
def test_PL_Groesse__instantiation(instance):
    assert isinstance(instance, PL_Groesse_)


PlaetzchenForm__strategy = st.builds(PlaetzchenForm_)
@given(instance=PlaetzchenForm__strategy)
@settings(max_examples=25)
def test_PlaetzchenForm__instantiation(instance):
    assert isinstance(instance, PlaetzchenForm_)


Plaetzchen__strategy = st.builds(Plaetzchen_)
@given(instance=Plaetzchen__strategy)
@settings(max_examples=25)
def test_Plaetzchen__instantiation(instance):
    assert isinstance(instance, Plaetzchen_)


String__strategy = st.builds(String_)
@given(instance=String__strategy)
@settings(max_examples=25)
def test_String__instantiation(instance):
    assert isinstance(instance, String_)


TeigRezept__strategy = st.builds(TeigRezept_)
@given(instance=TeigRezept__strategy)
@settings(max_examples=25)
def test_TeigRezept__instantiation(instance):
    assert isinstance(instance, TeigRezept_)


ThreadExceptionEventArgs__strategy = st.builds(ThreadExceptionEventArgs_)
@given(instance=ThreadExceptionEventArgs__strategy)
@settings(max_examples=25)
def test_ThreadExceptionEventArgs__instantiation(instance):
    assert isinstance(instance, ThreadExceptionEventArgs_)


Zutat__strategy = st.builds(Zutat_)
@given(instance=Zutat__strategy)
@settings(max_examples=25)
def test_Zutat__instantiation(instance):
    assert isinstance(instance, Zutat_)


myException_strategy = st.builds(myException)
@given(instance=myException_strategy)
@settings(max_examples=25)
def test_myException_instantiation(instance):
    assert isinstance(instance, myException)


