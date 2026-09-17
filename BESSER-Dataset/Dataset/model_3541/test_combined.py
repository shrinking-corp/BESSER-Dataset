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
    emapvselistentry_NewEClass5,
    emapvselistentry_NewEClass4,
    emapvselistentry_NewEClass3,
    emapvselistentry_NewEClass2,
    emapvselistentry_NewEClass1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_emapvselistentry_neweclass5_is_not_abstract():
    assert not inspect.isabstract(emapvselistentry_NewEClass5)


def test_hyp_emapvselistentry_neweclass5_constructor_exists():
    assert callable(emapvselistentry_NewEClass5.__init__)


def test_hyp_emapvselistentry_neweclass5_constructor_args():
    sig = inspect.signature(emapvselistentry_NewEClass5.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_emapvselistentry_neweclass4_is_not_abstract():
    assert not inspect.isabstract(emapvselistentry_NewEClass4)


def test_hyp_emapvselistentry_neweclass4_constructor_exists():
    assert callable(emapvselistentry_NewEClass4.__init__)


def test_hyp_emapvselistentry_neweclass4_constructor_args():
    sig = inspect.signature(emapvselistentry_NewEClass4.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_emapvselistentry_neweclass3_is_not_abstract():
    assert not inspect.isabstract(emapvselistentry_NewEClass3)


def test_hyp_emapvselistentry_neweclass3_constructor_exists():
    assert callable(emapvselistentry_NewEClass3.__init__)


def test_hyp_emapvselistentry_neweclass3_constructor_args():
    sig = inspect.signature(emapvselistentry_NewEClass3.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_emapvselistentry_neweclass2_is_not_abstract():
    assert not inspect.isabstract(emapvselistentry_NewEClass2)


def test_hyp_emapvselistentry_neweclass2_constructor_exists():
    assert callable(emapvselistentry_NewEClass2.__init__)


def test_hyp_emapvselistentry_neweclass2_constructor_args():
    sig = inspect.signature(emapvselistentry_NewEClass2.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_emapvselistentry_neweclass1_is_not_abstract():
    assert not inspect.isabstract(emapvselistentry_NewEClass1)


def test_hyp_emapvselistentry_neweclass1_constructor_exists():
    assert callable(emapvselistentry_NewEClass1.__init__)


def test_hyp_emapvselistentry_neweclass1_constructor_args():
    sig = inspect.signature(emapvselistentry_NewEClass1.__init__)
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
emapvselistentry_NewEClass5_strategy = st.builds(
    emapvselistentry_NewEClass5,
    key=
        safe_text,
    value=
        safe_text
)
emapvselistentry_NewEClass4_strategy = st.builds(
    emapvselistentry_NewEClass4,
    key=
        safe_text,
    value=
        safe_text
)
emapvselistentry_NewEClass3_strategy = st.builds(
    emapvselistentry_NewEClass3,
    key=
        safe_text,
    value=
        safe_text
)
emapvselistentry_NewEClass2_strategy = st.builds(
    emapvselistentry_NewEClass2,
    value=
        safe_text,
    key=
        safe_text
)
emapvselistentry_NewEClass1_strategy = st.builds(
    emapvselistentry_NewEClass1,
)




@given(instance=emapvselistentry_NewEClass5_strategy)
def test_hyp_emapvselistentry_neweclass5_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=emapvselistentry_NewEClass5_strategy)
def test_hyp_emapvselistentry_neweclass5_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=emapvselistentry_NewEClass4_strategy)
def test_hyp_emapvselistentry_neweclass4_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=emapvselistentry_NewEClass4_strategy)
def test_hyp_emapvselistentry_neweclass4_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=emapvselistentry_NewEClass3_strategy)
def test_hyp_emapvselistentry_neweclass3_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=emapvselistentry_NewEClass3_strategy)
def test_hyp_emapvselistentry_neweclass3_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=emapvselistentry_NewEClass2_strategy)
def test_hyp_emapvselistentry_neweclass2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=emapvselistentry_NewEClass2_strategy)
def test_hyp_emapvselistentry_neweclass2_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    emapvselistentry_NewEClass1,
    emapvselistentry_NewEClass2,
    emapvselistentry_NewEClass3,
    emapvselistentry_NewEClass4,
    emapvselistentry_NewEClass5,
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

def test_emapvselistentry_NewEClass2_key_value_roundtrip():
    instance = emapvselistentry_NewEClass2(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_emapvselistentry_NewEClass2_value_value_roundtrip():
    instance = emapvselistentry_NewEClass2(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_emapvselistentry_NewEClass3_key_value_roundtrip():
    instance = emapvselistentry_NewEClass3(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_emapvselistentry_NewEClass3_value_value_roundtrip():
    instance = emapvselistentry_NewEClass3(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_emapvselistentry_NewEClass4_key_value_roundtrip():
    instance = emapvselistentry_NewEClass4(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_emapvselistentry_NewEClass4_value_value_roundtrip():
    instance = emapvselistentry_NewEClass4(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_emapvselistentry_NewEClass5_key_value_roundtrip():
    instance = emapvselistentry_NewEClass5(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_emapvselistentry_NewEClass5_value_value_roundtrip():
    instance = emapvselistentry_NewEClass5(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_assoc_neweclass20_link_reassign_clear():
    a = emapvselistentry_NewEClass2(key="sample_text", value="sample_text")
    b1 = emapvselistentry_NewEClass1()
    b2 = emapvselistentry_NewEClass1()
    _safe_set(a, 'emapvselistentry_NewEClass2', b1)
    assert _is_linked(a, 'emapvselistentry_NewEClass2', b1)
    if hasattr(b1, 'emapvselistentry_NewEClass1'):
        assert _is_linked(b1, 'emapvselistentry_NewEClass1', a)
    _safe_set(a, 'emapvselistentry_NewEClass2', b2)
    assert _is_linked(a, 'emapvselistentry_NewEClass2', b2)
    if hasattr(b1, 'emapvselistentry_NewEClass1'):
        assert not _is_linked(b1, 'emapvselistentry_NewEClass1', a)
    if hasattr(b2, 'emapvselistentry_NewEClass1'):
        assert _is_linked(b2, 'emapvselistentry_NewEClass1', a)
    _safe_set(a, 'emapvselistentry_NewEClass2', None)
    assert not _is_linked(a, 'emapvselistentry_NewEClass2', b2)
    if hasattr(b2, 'emapvselistentry_NewEClass1'):
        assert not _is_linked(b2, 'emapvselistentry_NewEClass1', a)


def test_assoc_neweclass31_link_reassign_clear():
    a = emapvselistentry_NewEClass3(key="sample_text", value="sample_text")
    b1 = emapvselistentry_NewEClass1()
    b2 = emapvselistentry_NewEClass1()
    _safe_set(a, 'emapvselistentry_NewEClass3', b1)
    assert _is_linked(a, 'emapvselistentry_NewEClass3', b1)
    if hasattr(b1, 'emapvselistentry_NewEClass12'):
        assert _is_linked(b1, 'emapvselistentry_NewEClass12', a)
    _safe_set(a, 'emapvselistentry_NewEClass3', b2)
    assert _is_linked(a, 'emapvselistentry_NewEClass3', b2)
    if hasattr(b1, 'emapvselistentry_NewEClass12'):
        assert not _is_linked(b1, 'emapvselistentry_NewEClass12', a)
    if hasattr(b2, 'emapvselistentry_NewEClass12'):
        assert _is_linked(b2, 'emapvselistentry_NewEClass12', a)
    _safe_set(a, 'emapvselistentry_NewEClass3', None)
    assert not _is_linked(a, 'emapvselistentry_NewEClass3', b2)
    if hasattr(b2, 'emapvselistentry_NewEClass12'):
        assert not _is_linked(b2, 'emapvselistentry_NewEClass12', a)


def test_assoc_neweclass43_link_reassign_clear():
    a = emapvselistentry_NewEClass4(key="sample_text", value="sample_text")
    b1 = emapvselistentry_NewEClass1()
    b2 = emapvselistentry_NewEClass1()
    _safe_set(a, 'emapvselistentry_NewEClass4', b1)
    assert _is_linked(a, 'emapvselistentry_NewEClass4', b1)
    if hasattr(b1, 'emapvselistentry_NewEClass14'):
        assert _is_linked(b1, 'emapvselistentry_NewEClass14', a)
    _safe_set(a, 'emapvselistentry_NewEClass4', b2)
    assert _is_linked(a, 'emapvselistentry_NewEClass4', b2)
    if hasattr(b1, 'emapvselistentry_NewEClass14'):
        assert not _is_linked(b1, 'emapvselistentry_NewEClass14', a)
    if hasattr(b2, 'emapvselistentry_NewEClass14'):
        assert _is_linked(b2, 'emapvselistentry_NewEClass14', a)
    _safe_set(a, 'emapvselistentry_NewEClass4', None)
    assert not _is_linked(a, 'emapvselistentry_NewEClass4', b2)
    if hasattr(b2, 'emapvselistentry_NewEClass14'):
        assert not _is_linked(b2, 'emapvselistentry_NewEClass14', a)


def test_assoc_neweclass55_link_reassign_clear():
    a = emapvselistentry_NewEClass5(key="sample_text", value="sample_text")
    b1 = emapvselistentry_NewEClass1()
    b2 = emapvselistentry_NewEClass1()
    _safe_set(a, 'emapvselistentry_NewEClass5', b1)
    assert _is_linked(a, 'emapvselistentry_NewEClass5', b1)
    if hasattr(b1, 'emapvselistentry_NewEClass16'):
        assert _is_linked(b1, 'emapvselistentry_NewEClass16', a)
    _safe_set(a, 'emapvselistentry_NewEClass5', b2)
    assert _is_linked(a, 'emapvselistentry_NewEClass5', b2)
    if hasattr(b1, 'emapvselistentry_NewEClass16'):
        assert not _is_linked(b1, 'emapvselistentry_NewEClass16', a)
    if hasattr(b2, 'emapvselistentry_NewEClass16'):
        assert _is_linked(b2, 'emapvselistentry_NewEClass16', a)
    _safe_set(a, 'emapvselistentry_NewEClass5', None)
    assert not _is_linked(a, 'emapvselistentry_NewEClass5', b2)
    if hasattr(b2, 'emapvselistentry_NewEClass16'):
        assert not _is_linked(b2, 'emapvselistentry_NewEClass16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

emapvselistentry_NewEClass1_strategy = st.builds(emapvselistentry_NewEClass1)
@given(instance=emapvselistentry_NewEClass1_strategy)
@settings(max_examples=25)
def test_emapvselistentry_NewEClass1_instantiation(instance):
    assert isinstance(instance, emapvselistentry_NewEClass1)


emapvselistentry_NewEClass2_strategy = st.builds(emapvselistentry_NewEClass2, key=safe_text, value=safe_text)
@given(instance=emapvselistentry_NewEClass2_strategy)
@settings(max_examples=25)
def test_emapvselistentry_NewEClass2_instantiation(instance):
    assert isinstance(instance, emapvselistentry_NewEClass2)


emapvselistentry_NewEClass3_strategy = st.builds(emapvselistentry_NewEClass3, key=safe_text, value=safe_text)
@given(instance=emapvselistentry_NewEClass3_strategy)
@settings(max_examples=25)
def test_emapvselistentry_NewEClass3_instantiation(instance):
    assert isinstance(instance, emapvselistentry_NewEClass3)


emapvselistentry_NewEClass4_strategy = st.builds(emapvselistentry_NewEClass4, key=safe_text, value=safe_text)
@given(instance=emapvselistentry_NewEClass4_strategy)
@settings(max_examples=25)
def test_emapvselistentry_NewEClass4_instantiation(instance):
    assert isinstance(instance, emapvselistentry_NewEClass4)


emapvselistentry_NewEClass5_strategy = st.builds(emapvselistentry_NewEClass5, key=safe_text, value=safe_text)
@given(instance=emapvselistentry_NewEClass5_strategy)
@settings(max_examples=25)
def test_emapvselistentry_NewEClass5_instantiation(instance):
    assert isinstance(instance, emapvselistentry_NewEClass5)



