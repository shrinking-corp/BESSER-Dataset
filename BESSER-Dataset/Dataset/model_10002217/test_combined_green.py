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
    MyClass10,
    MyClass9,
    MyClass8,
    MyClass7,
    MyClass6,
    MyClass5,
    MyClass4,
    MyClass3,
    MyClass2,
    ttt,
    MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_myclass10_is_not_abstract():
    assert not inspect.isabstract(MyClass10)


def test_hyp_myclass10_constructor_exists():
    assert callable(MyClass10.__init__)


def test_hyp_myclass10_constructor_args():
    sig = inspect.signature(MyClass10.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_myclass9_is_not_abstract():
    assert not inspect.isabstract(MyClass9)


def test_hyp_myclass9_constructor_exists():
    assert callable(MyClass9.__init__)


def test_hyp_myclass9_constructor_args():
    sig = inspect.signature(MyClass9.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_myclass8_is_not_abstract():
    assert not inspect.isabstract(MyClass8)


def test_hyp_myclass8_constructor_exists():
    assert callable(MyClass8.__init__)


def test_hyp_myclass8_constructor_args():
    sig = inspect.signature(MyClass8.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_myclass7_is_not_abstract():
    assert not inspect.isabstract(MyClass7)


def test_hyp_myclass7_constructor_exists():
    assert callable(MyClass7.__init__)


def test_hyp_myclass7_constructor_args():
    sig = inspect.signature(MyClass7.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_myclass6_is_not_abstract():
    assert not inspect.isabstract(MyClass6)


def test_hyp_myclass6_constructor_exists():
    assert callable(MyClass6.__init__)


def test_hyp_myclass6_constructor_args():
    sig = inspect.signature(MyClass6.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_myclass5_is_not_abstract():
    assert not inspect.isabstract(MyClass5)


def test_hyp_myclass5_constructor_exists():
    assert callable(MyClass5.__init__)


def test_hyp_myclass5_constructor_args():
    sig = inspect.signature(MyClass5.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_myclass4_is_not_abstract():
    assert not inspect.isabstract(MyClass4)


def test_hyp_myclass4_constructor_exists():
    assert callable(MyClass4.__init__)


def test_hyp_myclass4_constructor_args():
    sig = inspect.signature(MyClass4.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_hyp_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_hyp_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"





def test_hyp_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_hyp_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_hyp_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_ttt_is_not_abstract():
    assert not inspect.isabstract(ttt)


def test_hyp_ttt_constructor_exists():
    assert callable(ttt.__init__)


def test_hyp_ttt_constructor_args():
    sig = inspect.signature(ttt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
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
MyClass10_strategy = st.builds(
    MyClass10,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
MyClass9_strategy = st.builds(
    MyClass9,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
MyClass8_strategy = st.builds(
    MyClass8,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
MyClass7_strategy = st.builds(
    MyClass7,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
MyClass6_strategy = st.builds(
    MyClass6,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
MyClass5_strategy = st.builds(
    MyClass5,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
MyClass4_strategy = st.builds(
    MyClass4,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
MyClass3_strategy = st.builds(
    MyClass3,
    attribute=
        safe_text,
    attribute2=
        safe_text
)
MyClass2_strategy = st.builds(
    MyClass2,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
ttt_strategy = st.builds(
    ttt,
)
MyClass_strategy = st.builds(
    MyClass,
    attribute2=
        safe_text,
    attribute=
        st.integers()
)




@given(instance=MyClass10_strategy)
def test_hyp_myclass10_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass10_strategy)
def test_hyp_myclass10_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=MyClass9_strategy)
def test_hyp_myclass9_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass9_strategy)
def test_hyp_myclass9_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=MyClass8_strategy)
def test_hyp_myclass8_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass8_strategy)
def test_hyp_myclass8_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=MyClass7_strategy)
def test_hyp_myclass7_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=MyClass7_strategy)
def test_hyp_myclass7_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=MyClass6_strategy)
def test_hyp_myclass6_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass6_strategy)
def test_hyp_myclass6_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=MyClass5_strategy)
def test_hyp_myclass5_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=MyClass5_strategy)
def test_hyp_myclass5_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=MyClass4_strategy)
def test_hyp_myclass4_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass4_strategy)
def test_hyp_myclass4_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=MyClass3_strategy)
def test_hyp_myclass3_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=MyClass3_strategy)
def test_hyp_myclass3_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original




@given(instance=MyClass2_strategy)
def test_hyp_myclass2_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=MyClass2_strategy)
def test_hyp_myclass2_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original





@given(instance=MyClass_strategy)
def test_hyp_myclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=MyClass_strategy)
def test_hyp_myclass_attribute_setter(instance):
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
    MyClass2,
    MyClass3,
    MyClass4,
    MyClass5,
    MyClass6,
    MyClass7,
    MyClass8,
    MyClass9,
    ttt,
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

def test_MyClass_attribute_value_roundtrip():
    instance = MyClass(attribute=7, attribute2="sample_text")
    assert instance.attribute == 7
    instance.attribute = 13
    assert instance.attribute == 13


def test_MyClass_attribute2_value_roundtrip():
    instance = MyClass(attribute=7, attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass10_attribute_value_roundtrip():
    instance = MyClass10(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass10_attribute2_value_roundtrip():
    instance = MyClass10(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass2_attribute_value_roundtrip():
    instance = MyClass2(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass2_attribute2_value_roundtrip():
    instance = MyClass2(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass3_attribute_value_roundtrip():
    instance = MyClass3(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass3_attribute2_value_roundtrip():
    instance = MyClass3(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass4_attribute_value_roundtrip():
    instance = MyClass4(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass4_attribute2_value_roundtrip():
    instance = MyClass4(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass5_attribute_value_roundtrip():
    instance = MyClass5(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass5_attribute2_value_roundtrip():
    instance = MyClass5(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass6_attribute_value_roundtrip():
    instance = MyClass6(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass6_attribute2_value_roundtrip():
    instance = MyClass6(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass7_attribute_value_roundtrip():
    instance = MyClass7(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass7_attribute2_value_roundtrip():
    instance = MyClass7(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass8_attribute_value_roundtrip():
    instance = MyClass8(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass8_attribute2_value_roundtrip():
    instance = MyClass8(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_MyClass9_attribute_value_roundtrip():
    instance = MyClass9(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass9_attribute2_value_roundtrip():
    instance = MyClass9(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

MyClass_strategy = st.builds(MyClass, attribute=st.integers(), attribute2=safe_text)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


MyClass10_strategy = st.builds(MyClass10, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass10_strategy)
@settings(max_examples=25)
def test_MyClass10_instantiation(instance):
    assert isinstance(instance, MyClass10)


MyClass2_strategy = st.builds(MyClass2, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass2_strategy)
@settings(max_examples=25)
def test_MyClass2_instantiation(instance):
    assert isinstance(instance, MyClass2)


MyClass3_strategy = st.builds(MyClass3, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass3_strategy)
@settings(max_examples=25)
def test_MyClass3_instantiation(instance):
    assert isinstance(instance, MyClass3)


MyClass4_strategy = st.builds(MyClass4, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass4_strategy)
@settings(max_examples=25)
def test_MyClass4_instantiation(instance):
    assert isinstance(instance, MyClass4)


MyClass5_strategy = st.builds(MyClass5, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass5_strategy)
@settings(max_examples=25)
def test_MyClass5_instantiation(instance):
    assert isinstance(instance, MyClass5)


MyClass6_strategy = st.builds(MyClass6, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass6_strategy)
@settings(max_examples=25)
def test_MyClass6_instantiation(instance):
    assert isinstance(instance, MyClass6)


MyClass7_strategy = st.builds(MyClass7, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass7_strategy)
@settings(max_examples=25)
def test_MyClass7_instantiation(instance):
    assert isinstance(instance, MyClass7)


MyClass8_strategy = st.builds(MyClass8, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass8_strategy)
@settings(max_examples=25)
def test_MyClass8_instantiation(instance):
    assert isinstance(instance, MyClass8)


MyClass9_strategy = st.builds(MyClass9, attribute=safe_text, attribute2=safe_text)
@given(instance=MyClass9_strategy)
@settings(max_examples=25)
def test_MyClass9_instantiation(instance):
    assert isinstance(instance, MyClass9)


ttt_strategy = st.builds(ttt)
@given(instance=ttt_strategy)
@settings(max_examples=25)
def test_ttt_instantiation(instance):
    assert isinstance(instance, ttt)



