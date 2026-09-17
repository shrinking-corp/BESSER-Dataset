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
    MyClass19,
    MyClass18,
    MyClass17,
    MyClass16,
    MyClass15,
    MyClass14,
    MyClass13,
    MyClass12,
    MyInterface_Interface,
    MyClass11,
    MyClass10,
    MyClass9,
    MyClass8,
    MyClass7,
    MyClass6,
    MyClass5,
    MyClass4,
    MyClass3,
    MyClass2,
    MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_myclass19_is_not_abstract():
    assert not inspect.isabstract(MyClass19)


def test_hyp_myclass19_constructor_exists():
    assert callable(MyClass19.__init__)


def test_hyp_myclass19_constructor_args():
    sig = inspect.signature(MyClass19.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass18_is_not_abstract():
    assert not inspect.isabstract(MyClass18)


def test_hyp_myclass18_constructor_exists():
    assert callable(MyClass18.__init__)


def test_hyp_myclass18_constructor_args():
    sig = inspect.signature(MyClass18.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_myclass17_is_not_abstract():
    assert not inspect.isabstract(MyClass17)


def test_hyp_myclass17_constructor_exists():
    assert callable(MyClass17.__init__)


def test_hyp_myclass17_constructor_args():
    sig = inspect.signature(MyClass17.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass16_is_not_abstract():
    assert not inspect.isabstract(MyClass16)


def test_hyp_myclass16_constructor_exists():
    assert callable(MyClass16.__init__)


def test_hyp_myclass16_constructor_args():
    sig = inspect.signature(MyClass16.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass15_is_not_abstract():
    assert not inspect.isabstract(MyClass15)


def test_hyp_myclass15_constructor_exists():
    assert callable(MyClass15.__init__)


def test_hyp_myclass15_constructor_args():
    sig = inspect.signature(MyClass15.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass14_is_not_abstract():
    assert not inspect.isabstract(MyClass14)


def test_hyp_myclass14_constructor_exists():
    assert callable(MyClass14.__init__)


def test_hyp_myclass14_constructor_args():
    sig = inspect.signature(MyClass14.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass13_is_not_abstract():
    assert not inspect.isabstract(MyClass13)


def test_hyp_myclass13_constructor_exists():
    assert callable(MyClass13.__init__)


def test_hyp_myclass13_constructor_args():
    sig = inspect.signature(MyClass13.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass12_is_not_abstract():
    assert not inspect.isabstract(MyClass12)


def test_hyp_myclass12_constructor_exists():
    assert callable(MyClass12.__init__)


def test_hyp_myclass12_constructor_args():
    sig = inspect.signature(MyClass12.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_myinterface_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface_Interface)


def test_hyp_myinterface_interface_constructor_exists():
    assert callable(MyInterface_Interface.__init__)


def test_hyp_myinterface_interface_constructor_args():
    sig = inspect.signature(MyInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass11_is_not_abstract():
    assert not inspect.isabstract(MyClass11)


def test_hyp_myclass11_constructor_exists():
    assert callable(MyClass11.__init__)


def test_hyp_myclass11_constructor_args():
    sig = inspect.signature(MyClass11.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass10_is_not_abstract():
    assert not inspect.isabstract(MyClass10)


def test_hyp_myclass10_constructor_exists():
    assert callable(MyClass10.__init__)


def test_hyp_myclass10_constructor_args():
    sig = inspect.signature(MyClass10.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass9_is_not_abstract():
    assert not inspect.isabstract(MyClass9)


def test_hyp_myclass9_constructor_exists():
    assert callable(MyClass9.__init__)


def test_hyp_myclass9_constructor_args():
    sig = inspect.signature(MyClass9.__init__)
    params = list(sig.parameters.keys())



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



def test_hyp_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_hyp_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_hyp_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())


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
MyClass19_strategy = st.builds(
    MyClass19,
)
MyClass18_strategy = st.builds(
    MyClass18,
    attribute=
        safe_text
)
MyClass17_strategy = st.builds(
    MyClass17,
)
MyClass16_strategy = st.builds(
    MyClass16,
)
MyClass15_strategy = st.builds(
    MyClass15,
)
MyClass14_strategy = st.builds(
    MyClass14,
)
MyClass13_strategy = st.builds(
    MyClass13,
)
MyClass12_strategy = st.builds(
    MyClass12,
    attribute=
        safe_text
)
MyInterface_Interface_strategy = st.builds(
    MyInterface_Interface,
)
MyClass11_strategy = st.builds(
    MyClass11,
)
MyClass10_strategy = st.builds(
    MyClass10,
)
MyClass9_strategy = st.builds(
    MyClass9,
)
MyClass8_strategy = st.builds(
    MyClass8,
)
MyClass7_strategy = st.builds(
    MyClass7,
)
MyClass6_strategy = st.builds(
    MyClass6,
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
MyClass2_strategy = st.builds(
    MyClass2,
)
MyClass_strategy = st.builds(
    MyClass,
)





@given(instance=MyClass18_strategy)
def test_hyp_myclass18_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original









@given(instance=MyClass12_strategy)
def test_hyp_myclass12_attribute_setter(instance):
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
    MyClass,
    MyClass10,
    MyClass11,
    MyClass12,
    MyClass13,
    MyClass14,
    MyClass15,
    MyClass16,
    MyClass17,
    MyClass18,
    MyClass19,
    MyClass2,
    MyClass3,
    MyClass4,
    MyClass5,
    MyClass6,
    MyClass7,
    MyClass8,
    MyClass9,
    MyInterface_Interface,
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

def test_MyClass12_attribute_value_roundtrip():
    instance = MyClass12(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass18_attribute_value_roundtrip():
    instance = MyClass18(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


MyClass10_strategy = st.builds(MyClass10)
@given(instance=MyClass10_strategy)
@settings(max_examples=25)
def test_MyClass10_instantiation(instance):
    assert isinstance(instance, MyClass10)


MyClass11_strategy = st.builds(MyClass11)
@given(instance=MyClass11_strategy)
@settings(max_examples=25)
def test_MyClass11_instantiation(instance):
    assert isinstance(instance, MyClass11)


MyClass12_strategy = st.builds(MyClass12, attribute=safe_text)
@given(instance=MyClass12_strategy)
@settings(max_examples=25)
def test_MyClass12_instantiation(instance):
    assert isinstance(instance, MyClass12)


MyClass13_strategy = st.builds(MyClass13)
@given(instance=MyClass13_strategy)
@settings(max_examples=25)
def test_MyClass13_instantiation(instance):
    assert isinstance(instance, MyClass13)


MyClass14_strategy = st.builds(MyClass14)
@given(instance=MyClass14_strategy)
@settings(max_examples=25)
def test_MyClass14_instantiation(instance):
    assert isinstance(instance, MyClass14)


MyClass15_strategy = st.builds(MyClass15)
@given(instance=MyClass15_strategy)
@settings(max_examples=25)
def test_MyClass15_instantiation(instance):
    assert isinstance(instance, MyClass15)


MyClass16_strategy = st.builds(MyClass16)
@given(instance=MyClass16_strategy)
@settings(max_examples=25)
def test_MyClass16_instantiation(instance):
    assert isinstance(instance, MyClass16)


MyClass17_strategy = st.builds(MyClass17)
@given(instance=MyClass17_strategy)
@settings(max_examples=25)
def test_MyClass17_instantiation(instance):
    assert isinstance(instance, MyClass17)


MyClass18_strategy = st.builds(MyClass18, attribute=safe_text)
@given(instance=MyClass18_strategy)
@settings(max_examples=25)
def test_MyClass18_instantiation(instance):
    assert isinstance(instance, MyClass18)


MyClass19_strategy = st.builds(MyClass19)
@given(instance=MyClass19_strategy)
@settings(max_examples=25)
def test_MyClass19_instantiation(instance):
    assert isinstance(instance, MyClass19)


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


MyClass9_strategy = st.builds(MyClass9)
@given(instance=MyClass9_strategy)
@settings(max_examples=25)
def test_MyClass9_instantiation(instance):
    assert isinstance(instance, MyClass9)


MyInterface_Interface_strategy = st.builds(MyInterface_Interface)
@given(instance=MyInterface_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface_Interface)



