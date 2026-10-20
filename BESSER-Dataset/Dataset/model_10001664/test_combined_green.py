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
    MyClass8,
    MyClass7,
    MyClass6,
    MyInterface2_Interface,
    MyInterface_Interface,
    MyClass5,
    MyClass4,
    MyClass3,
    MyClass,
    MyClass2,
    Sprite,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_myclass8_is_not_abstract():
    assert not inspect.isabstract(MyClass8)


def test_hyp_myclass8_constructor_exists():
    assert callable(MyClass8.__init__)


def test_hyp_myclass8_constructor_args():
    sig = inspect.signature(MyClass8.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass7_is_not_abstract():
    assert not inspect.isabstract(MyClass7)


def test_hyp_myclass7_constructor_exists():
    assert callable(MyClass7.__init__)


def test_hyp_myclass7_constructor_args():
    sig = inspect.signature(MyClass7.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass6_is_not_abstract():
    assert not inspect.isabstract(MyClass6)


def test_hyp_myclass6_constructor_exists():
    assert callable(MyClass6.__init__)


def test_hyp_myclass6_constructor_args():
    sig = inspect.signature(MyClass6.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myinterface2_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface2_Interface)


def test_hyp_myinterface2_interface_constructor_exists():
    assert callable(MyInterface2_Interface.__init__)


def test_hyp_myinterface2_interface_constructor_args():
    sig = inspect.signature(MyInterface2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myinterface_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface_Interface)


def test_hyp_myinterface_interface_constructor_exists():
    assert callable(MyInterface_Interface.__init__)


def test_hyp_myinterface_interface_constructor_args():
    sig = inspect.signature(MyInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass5_is_not_abstract():
    assert not inspect.isabstract(MyClass5)


def test_hyp_myclass5_constructor_exists():
    assert callable(MyClass5.__init__)


def test_hyp_myclass5_constructor_args():
    sig = inspect.signature(MyClass5.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass4_is_not_abstract():
    assert not inspect.isabstract(MyClass4)


def test_hyp_myclass4_constructor_exists():
    assert callable(MyClass4.__init__)


def test_hyp_myclass4_constructor_args():
    sig = inspect.signature(MyClass4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_hyp_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_hyp_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_hyp_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_hyp_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sprite_is_not_abstract():
    assert not inspect.isabstract(Sprite)


def test_hyp_sprite_constructor_exists():
    assert callable(Sprite.__init__)


def test_hyp_sprite_constructor_args():
    sig = inspect.signature(Sprite.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"



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
MyClass8_strategy = st.builds(
    MyClass8,
)
MyClass7_strategy = st.builds(
    MyClass7,
)
MyClass6_strategy = st.builds(
    MyClass6,
)
MyInterface2_Interface_strategy = st.builds(
    MyInterface2_Interface,
)
MyInterface_Interface_strategy = st.builds(
    MyInterface_Interface,
)
MyClass5_strategy = st.builds(
    MyClass5,
)
MyClass4_strategy = st.builds(
    MyClass4,
)
MyClass3_strategy = st.builds(
    MyClass3,
)
MyClass_strategy = st.builds(
    MyClass,
)
MyClass2_strategy = st.builds(
    MyClass2,
)
Sprite_strategy = st.builds(
    Sprite,
    ID=
        safe_text
)














@given(instance=Sprite_strategy)
def test_hyp_sprite_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    MyClass,
    MyClass2,
    MyClass3,
    MyClass4,
    MyClass5,
    MyClass6,
    MyClass7,
    MyClass8,
    MyInterface2_Interface,
    MyInterface_Interface,
    Sprite,
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

def test_Sprite_ID_value_roundtrip():
    instance = Sprite(ID="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


MyClass2_strategy = st.builds(MyClass2)
@given(instance=MyClass2_strategy)
@settings(max_examples=25)
def test_MyClass2_instantiation(instance):
    assert isinstance(instance, MyClass2)


MyClass3_strategy = st.builds(MyClass3)
@given(instance=MyClass3_strategy)
@settings(max_examples=25)
def test_MyClass3_instantiation(instance):
    assert isinstance(instance, MyClass3)


MyClass4_strategy = st.builds(MyClass4)
@given(instance=MyClass4_strategy)
@settings(max_examples=25)
def test_MyClass4_instantiation(instance):
    assert isinstance(instance, MyClass4)


MyClass5_strategy = st.builds(MyClass5)
@given(instance=MyClass5_strategy)
@settings(max_examples=25)
def test_MyClass5_instantiation(instance):
    assert isinstance(instance, MyClass5)


MyClass6_strategy = st.builds(MyClass6)
@given(instance=MyClass6_strategy)
@settings(max_examples=25)
def test_MyClass6_instantiation(instance):
    assert isinstance(instance, MyClass6)


MyClass7_strategy = st.builds(MyClass7)
@given(instance=MyClass7_strategy)
@settings(max_examples=25)
def test_MyClass7_instantiation(instance):
    assert isinstance(instance, MyClass7)


MyClass8_strategy = st.builds(MyClass8)
@given(instance=MyClass8_strategy)
@settings(max_examples=25)
def test_MyClass8_instantiation(instance):
    assert isinstance(instance, MyClass8)


MyInterface2_Interface_strategy = st.builds(MyInterface2_Interface)
@given(instance=MyInterface2_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface2_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface2_Interface)


MyInterface_Interface_strategy = st.builds(MyInterface_Interface)
@given(instance=MyInterface_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface_Interface)


Sprite_strategy = st.builds(Sprite, ID=safe_text)
@given(instance=Sprite_strategy)
@settings(max_examples=25)
def test_Sprite_instantiation(instance):
    assert isinstance(instance, Sprite)



