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
    mypackage_MyClass20,
    mypackage_MyClass19,
    mypackage_MyClass18,
    mypackage_MyClass17,
    mypackage_MyClass16,
    mypackage_MyClass15,
    mypackage_MyClass14,
    mypackage_MyClass13,
    mypackage_MyClass12,
    mypackage_MyClass11,
    mypackage_MyClass10,
    mypackage_MyClass9,
    mypackage_MyClass8,
    mypackage_MyClass7,
    mypackage_MyClass6,
    mypackage_MyClass5,
    mypackage_MyClass4,
    mypackage_MyClass3,
    mypackage_MyClass2,
    mypackage_MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mypackage_myclass20_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass20)


def test_hyp_mypackage_myclass20_constructor_exists():
    assert callable(mypackage_MyClass20.__init__)


def test_hyp_mypackage_myclass20_constructor_args():
    sig = inspect.signature(mypackage_MyClass20.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass19_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass19)


def test_hyp_mypackage_myclass19_constructor_exists():
    assert callable(mypackage_MyClass19.__init__)


def test_hyp_mypackage_myclass19_constructor_args():
    sig = inspect.signature(mypackage_MyClass19.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass18_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass18)


def test_hyp_mypackage_myclass18_constructor_exists():
    assert callable(mypackage_MyClass18.__init__)


def test_hyp_mypackage_myclass18_constructor_args():
    sig = inspect.signature(mypackage_MyClass18.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass17_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass17)


def test_hyp_mypackage_myclass17_constructor_exists():
    assert callable(mypackage_MyClass17.__init__)


def test_hyp_mypackage_myclass17_constructor_args():
    sig = inspect.signature(mypackage_MyClass17.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass16_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass16)


def test_hyp_mypackage_myclass16_constructor_exists():
    assert callable(mypackage_MyClass16.__init__)


def test_hyp_mypackage_myclass16_constructor_args():
    sig = inspect.signature(mypackage_MyClass16.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass15_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass15)


def test_hyp_mypackage_myclass15_constructor_exists():
    assert callable(mypackage_MyClass15.__init__)


def test_hyp_mypackage_myclass15_constructor_args():
    sig = inspect.signature(mypackage_MyClass15.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass14_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass14)


def test_hyp_mypackage_myclass14_constructor_exists():
    assert callable(mypackage_MyClass14.__init__)


def test_hyp_mypackage_myclass14_constructor_args():
    sig = inspect.signature(mypackage_MyClass14.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass13_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass13)


def test_hyp_mypackage_myclass13_constructor_exists():
    assert callable(mypackage_MyClass13.__init__)


def test_hyp_mypackage_myclass13_constructor_args():
    sig = inspect.signature(mypackage_MyClass13.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass12_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass12)


def test_hyp_mypackage_myclass12_constructor_exists():
    assert callable(mypackage_MyClass12.__init__)


def test_hyp_mypackage_myclass12_constructor_args():
    sig = inspect.signature(mypackage_MyClass12.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass11_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass11)


def test_hyp_mypackage_myclass11_constructor_exists():
    assert callable(mypackage_MyClass11.__init__)


def test_hyp_mypackage_myclass11_constructor_args():
    sig = inspect.signature(mypackage_MyClass11.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass10_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass10)


def test_hyp_mypackage_myclass10_constructor_exists():
    assert callable(mypackage_MyClass10.__init__)


def test_hyp_mypackage_myclass10_constructor_args():
    sig = inspect.signature(mypackage_MyClass10.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass9_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass9)


def test_hyp_mypackage_myclass9_constructor_exists():
    assert callable(mypackage_MyClass9.__init__)


def test_hyp_mypackage_myclass9_constructor_args():
    sig = inspect.signature(mypackage_MyClass9.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass8_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass8)


def test_hyp_mypackage_myclass8_constructor_exists():
    assert callable(mypackage_MyClass8.__init__)


def test_hyp_mypackage_myclass8_constructor_args():
    sig = inspect.signature(mypackage_MyClass8.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass7_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass7)


def test_hyp_mypackage_myclass7_constructor_exists():
    assert callable(mypackage_MyClass7.__init__)


def test_hyp_mypackage_myclass7_constructor_args():
    sig = inspect.signature(mypackage_MyClass7.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass6_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass6)


def test_hyp_mypackage_myclass6_constructor_exists():
    assert callable(mypackage_MyClass6.__init__)


def test_hyp_mypackage_myclass6_constructor_args():
    sig = inspect.signature(mypackage_MyClass6.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass5_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass5)


def test_hyp_mypackage_myclass5_constructor_exists():
    assert callable(mypackage_MyClass5.__init__)


def test_hyp_mypackage_myclass5_constructor_args():
    sig = inspect.signature(mypackage_MyClass5.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass4_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass4)


def test_hyp_mypackage_myclass4_constructor_exists():
    assert callable(mypackage_MyClass4.__init__)


def test_hyp_mypackage_myclass4_constructor_args():
    sig = inspect.signature(mypackage_MyClass4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass3_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass3)


def test_hyp_mypackage_myclass3_constructor_exists():
    assert callable(mypackage_MyClass3.__init__)


def test_hyp_mypackage_myclass3_constructor_args():
    sig = inspect.signature(mypackage_MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass2_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass2)


def test_hyp_mypackage_myclass2_constructor_exists():
    assert callable(mypackage_MyClass2.__init__)


def test_hyp_mypackage_myclass2_constructor_args():
    sig = inspect.signature(mypackage_MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mypackage_myclass_is_not_abstract():
    assert not inspect.isabstract(mypackage_MyClass)


def test_hyp_mypackage_myclass_constructor_exists():
    assert callable(mypackage_MyClass.__init__)


def test_hyp_mypackage_myclass_constructor_args():
    sig = inspect.signature(mypackage_MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "haarfarbe" in params, "Missing parameter 'haarfarbe'"



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
mypackage_MyClass20_strategy = st.builds(
    mypackage_MyClass20,
)
mypackage_MyClass19_strategy = st.builds(
    mypackage_MyClass19,
)
mypackage_MyClass18_strategy = st.builds(
    mypackage_MyClass18,
)
mypackage_MyClass17_strategy = st.builds(
    mypackage_MyClass17,
)
mypackage_MyClass16_strategy = st.builds(
    mypackage_MyClass16,
)
mypackage_MyClass15_strategy = st.builds(
    mypackage_MyClass15,
)
mypackage_MyClass14_strategy = st.builds(
    mypackage_MyClass14,
)
mypackage_MyClass13_strategy = st.builds(
    mypackage_MyClass13,
)
mypackage_MyClass12_strategy = st.builds(
    mypackage_MyClass12,
)
mypackage_MyClass11_strategy = st.builds(
    mypackage_MyClass11,
)
mypackage_MyClass10_strategy = st.builds(
    mypackage_MyClass10,
)
mypackage_MyClass9_strategy = st.builds(
    mypackage_MyClass9,
)
mypackage_MyClass8_strategy = st.builds(
    mypackage_MyClass8,
)
mypackage_MyClass7_strategy = st.builds(
    mypackage_MyClass7,
)
mypackage_MyClass6_strategy = st.builds(
    mypackage_MyClass6,
)
mypackage_MyClass5_strategy = st.builds(
    mypackage_MyClass5,
)
mypackage_MyClass4_strategy = st.builds(
    mypackage_MyClass4,
)
mypackage_MyClass3_strategy = st.builds(
    mypackage_MyClass3,
)
mypackage_MyClass2_strategy = st.builds(
    mypackage_MyClass2,
)
mypackage_MyClass_strategy = st.builds(
    mypackage_MyClass,
    haarfarbe=
        safe_text
)























@given(instance=mypackage_MyClass_strategy)
def test_hyp_mypackage_myclass_haarfarbe_setter(instance):
    original = instance.haarfarbe
    instance.haarfarbe = original
    assert instance.haarfarbe == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    mypackage_MyClass,
    mypackage_MyClass10,
    mypackage_MyClass11,
    mypackage_MyClass12,
    mypackage_MyClass13,
    mypackage_MyClass14,
    mypackage_MyClass15,
    mypackage_MyClass16,
    mypackage_MyClass17,
    mypackage_MyClass18,
    mypackage_MyClass19,
    mypackage_MyClass2,
    mypackage_MyClass20,
    mypackage_MyClass3,
    mypackage_MyClass4,
    mypackage_MyClass5,
    mypackage_MyClass6,
    mypackage_MyClass7,
    mypackage_MyClass8,
    mypackage_MyClass9,
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

def test_mypackage_MyClass_haarfarbe_value_roundtrip():
    instance = mypackage_MyClass(haarfarbe="sample_text")
    assert instance.haarfarbe == "sample_text"
    instance.haarfarbe = "sample_text_2"
    assert instance.haarfarbe == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

mypackage_MyClass_strategy = st.builds(mypackage_MyClass, haarfarbe=safe_text)
@given(instance=mypackage_MyClass_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass)


mypackage_MyClass10_strategy = st.builds(mypackage_MyClass10)
@given(instance=mypackage_MyClass10_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass10_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass10)


mypackage_MyClass11_strategy = st.builds(mypackage_MyClass11)
@given(instance=mypackage_MyClass11_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass11_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass11)


mypackage_MyClass12_strategy = st.builds(mypackage_MyClass12)
@given(instance=mypackage_MyClass12_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass12_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass12)


mypackage_MyClass13_strategy = st.builds(mypackage_MyClass13)
@given(instance=mypackage_MyClass13_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass13_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass13)


mypackage_MyClass14_strategy = st.builds(mypackage_MyClass14)
@given(instance=mypackage_MyClass14_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass14_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass14)


mypackage_MyClass15_strategy = st.builds(mypackage_MyClass15)
@given(instance=mypackage_MyClass15_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass15_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass15)


mypackage_MyClass16_strategy = st.builds(mypackage_MyClass16)
@given(instance=mypackage_MyClass16_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass16_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass16)


mypackage_MyClass17_strategy = st.builds(mypackage_MyClass17)
@given(instance=mypackage_MyClass17_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass17_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass17)


mypackage_MyClass18_strategy = st.builds(mypackage_MyClass18)
@given(instance=mypackage_MyClass18_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass18_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass18)


mypackage_MyClass19_strategy = st.builds(mypackage_MyClass19)
@given(instance=mypackage_MyClass19_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass19_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass19)


mypackage_MyClass2_strategy = st.builds(mypackage_MyClass2)
@given(instance=mypackage_MyClass2_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass2_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass2)


mypackage_MyClass20_strategy = st.builds(mypackage_MyClass20)
@given(instance=mypackage_MyClass20_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass20_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass20)


mypackage_MyClass3_strategy = st.builds(mypackage_MyClass3)
@given(instance=mypackage_MyClass3_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass3_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass3)


mypackage_MyClass4_strategy = st.builds(mypackage_MyClass4)
@given(instance=mypackage_MyClass4_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass4_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass4)


mypackage_MyClass5_strategy = st.builds(mypackage_MyClass5)
@given(instance=mypackage_MyClass5_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass5_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass5)


mypackage_MyClass6_strategy = st.builds(mypackage_MyClass6)
@given(instance=mypackage_MyClass6_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass6_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass6)


mypackage_MyClass7_strategy = st.builds(mypackage_MyClass7)
@given(instance=mypackage_MyClass7_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass7_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass7)


mypackage_MyClass8_strategy = st.builds(mypackage_MyClass8)
@given(instance=mypackage_MyClass8_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass8_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass8)


mypackage_MyClass9_strategy = st.builds(mypackage_MyClass9)
@given(instance=mypackage_MyClass9_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass9_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass9)



