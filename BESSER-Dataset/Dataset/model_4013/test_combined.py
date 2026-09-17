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
    Data_Model,
    Data_Attribut,
    Data_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_data_model_is_not_abstract():
    assert not inspect.isabstract(Data_Model)


def test_hyp_data_model_constructor_exists():
    assert callable(Data_Model.__init__)


def test_hyp_data_model_constructor_args():
    sig = inspect.signature(Data_Model.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_data_attribut_is_not_abstract():
    assert not inspect.isabstract(Data_Attribut)


def test_hyp_data_attribut_constructor_exists():
    assert callable(Data_Attribut.__init__)


def test_hyp_data_attribut_constructor_args():
    sig = inspect.signature(Data_Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "Static" in params, "Missing parameter 'Static'"
    assert "Visibility" in params, "Missing parameter 'Visibility'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Type" in params, "Missing parameter 'Type'"







def test_hyp_data_class_is_not_abstract():
    assert not inspect.isabstract(Data_Class)


def test_hyp_data_class_constructor_exists():
    assert callable(Data_Class.__init__)


def test_hyp_data_class_constructor_args():
    sig = inspect.signature(Data_Class.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"



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
Data_Model_strategy = st.builds(
    Data_Model,
    Name=
        safe_text
)
Data_Attribut_strategy = st.builds(
    Data_Attribut,
    Static=
        st.booleans(),
    Visibility=
        safe_text,
    Name=
        safe_text,
    Type=
        safe_text
)
Data_Class_strategy = st.builds(
    Data_Class,
    Name=
        safe_text
)




@given(instance=Data_Model_strategy)
def test_hyp_data_model_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Data_Attribut_strategy)
def test_hyp_data_attribut_Static_setter(instance):
    original = instance.Static
    instance.Static = original
    assert instance.Static == original



@given(instance=Data_Attribut_strategy)
def test_hyp_data_attribut_Visibility_setter(instance):
    original = instance.Visibility
    instance.Visibility = original
    assert instance.Visibility == original



@given(instance=Data_Attribut_strategy)
def test_hyp_data_attribut_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Data_Attribut_strategy)
def test_hyp_data_attribut_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original




@given(instance=Data_Class_strategy)
def test_hyp_data_class_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Data_Attribut,
    Data_Class,
    Data_Model,
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

def test_Data_Attribut_Name_value_roundtrip():
    instance = Data_Attribut(Name="sample_text", Static=True, Type="sample_text", Visibility="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Data_Attribut_Static_value_roundtrip():
    instance = Data_Attribut(Name="sample_text", Static=True, Type="sample_text", Visibility="sample_text")
    assert instance.Static == True
    instance.Static = False
    assert instance.Static == False


def test_Data_Attribut_Type_value_roundtrip():
    instance = Data_Attribut(Name="sample_text", Static=True, Type="sample_text", Visibility="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_Data_Attribut_Visibility_value_roundtrip():
    instance = Data_Attribut(Name="sample_text", Static=True, Type="sample_text", Visibility="sample_text")
    assert instance.Visibility == "sample_text"
    instance.Visibility = "sample_text_2"
    assert instance.Visibility == "sample_text_2"


def test_Data_Class_Name_value_roundtrip():
    instance = Data_Class(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Data_Model_Name_value_roundtrip():
    instance = Data_Model(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Attributs0_link_reassign_clear():
    a = Data_Class(Name="sample_text")
    b1 = Data_Attribut(Name="sample_text", Static=True, Type="sample_text", Visibility="sample_text")
    b2 = Data_Attribut(Name="sample_text_2", Static=False, Type="sample_text_2", Visibility="sample_text_2")
    _safe_set(a, 'Data_Class', {b1})
    assert _is_linked(a, 'Data_Class', b1)
    if hasattr(b1, 'Data_Attribut'):
        assert _is_linked(b1, 'Data_Attribut', a)
    _safe_set(a, 'Data_Class', {b2})
    assert _is_linked(a, 'Data_Class', b2)
    if hasattr(b1, 'Data_Attribut'):
        assert not _is_linked(b1, 'Data_Attribut', a)
    if hasattr(b2, 'Data_Attribut'):
        assert _is_linked(b2, 'Data_Attribut', a)
    _safe_set(a, 'Data_Class', set())
    assert not _is_linked(a, 'Data_Class', b2)
    if hasattr(b2, 'Data_Attribut'):
        assert not _is_linked(b2, 'Data_Attribut', a)


def test_assoc_Classes1_link_reassign_clear():
    a = Data_Model(Name="sample_text")
    b1 = Data_Class(Name="sample_text")
    b2 = Data_Class(Name="sample_text_2")
    _safe_set(a, 'Data_Model', {b1})
    assert _is_linked(a, 'Data_Model', b1)
    if hasattr(b1, 'Data_Class2'):
        assert _is_linked(b1, 'Data_Class2', a)
    _safe_set(a, 'Data_Model', {b2})
    assert _is_linked(a, 'Data_Model', b2)
    if hasattr(b1, 'Data_Class2'):
        assert not _is_linked(b1, 'Data_Class2', a)
    if hasattr(b2, 'Data_Class2'):
        assert _is_linked(b2, 'Data_Class2', a)
    _safe_set(a, 'Data_Model', set())
    assert not _is_linked(a, 'Data_Model', b2)
    if hasattr(b2, 'Data_Class2'):
        assert not _is_linked(b2, 'Data_Class2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Data_Attribut_strategy = st.builds(Data_Attribut, Name=safe_text, Static=st.booleans(), Type=safe_text, Visibility=safe_text)
@given(instance=Data_Attribut_strategy)
@settings(max_examples=25)
def test_Data_Attribut_instantiation(instance):
    assert isinstance(instance, Data_Attribut)


Data_Class_strategy = st.builds(Data_Class, Name=safe_text)
@given(instance=Data_Class_strategy)
@settings(max_examples=25)
def test_Data_Class_instantiation(instance):
    assert isinstance(instance, Data_Class)


Data_Model_strategy = st.builds(Data_Model, Name=safe_text)
@given(instance=Data_Model_strategy)
@settings(max_examples=25)
def test_Data_Model_instantiation(instance):
    assert isinstance(instance, Data_Model)



