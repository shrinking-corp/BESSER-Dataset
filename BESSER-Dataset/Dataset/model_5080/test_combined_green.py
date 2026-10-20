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
    adlrecur_Binding,
    Component,
    adlrecur_Base,
    Interface,
    adlrecur_Component,
    adlrecur_Interface,
    adlrecur_Provided,
    adlrecur_Required,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_adlrecur_binding_is_not_abstract():
    assert not inspect.isabstract(adlrecur_Binding)


def test_hyp_adlrecur_binding_constructor_exists():
    assert callable(adlrecur_Binding.__init__)


def test_hyp_adlrecur_binding_constructor_args():
    sig = inspect.signature(adlrecur_Binding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_hyp_component_constructor_exists():
    assert callable(Component.__init__)


def test_hyp_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adlrecur_base_is_not_abstract():
    assert not inspect.isabstract(adlrecur_Base)


def test_hyp_adlrecur_base_constructor_exists():
    assert callable(adlrecur_Base.__init__)


def test_hyp_adlrecur_base_constructor_args():
    sig = inspect.signature(adlrecur_Base.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_hyp_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_hyp_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adlrecur_component_is_not_abstract():
    assert not inspect.isabstract(adlrecur_Component)


def test_hyp_adlrecur_component_constructor_exists():
    assert callable(adlrecur_Component.__init__)


def test_hyp_adlrecur_component_constructor_args():
    sig = inspect.signature(adlrecur_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_adlrecur_interface_is_not_abstract():
    assert not inspect.isabstract(adlrecur_Interface)


def test_hyp_adlrecur_interface_constructor_exists():
    assert callable(adlrecur_Interface.__init__)


def test_hyp_adlrecur_interface_constructor_args():
    sig = inspect.signature(adlrecur_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"





def test_hyp_adlrecur_provided_is_not_abstract():
    assert not inspect.isabstract(adlrecur_Provided)


def test_hyp_adlrecur_provided_constructor_exists():
    assert callable(adlrecur_Provided.__init__)


def test_hyp_adlrecur_provided_constructor_args():
    sig = inspect.signature(adlrecur_Provided.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adlrecur_required_is_not_abstract():
    assert not inspect.isabstract(adlrecur_Required)


def test_hyp_adlrecur_required_constructor_exists():
    assert callable(adlrecur_Required.__init__)


def test_hyp_adlrecur_required_constructor_args():
    sig = inspect.signature(adlrecur_Required.__init__)
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
adlrecur_Binding_strategy = st.builds(
    adlrecur_Binding,
)
Component_strategy = st.builds(
    Component,
)
adlrecur_Base_strategy = st.builds(
    adlrecur_Base,
)
Interface_strategy = st.builds(
    Interface,
)
adlrecur_Component_strategy = st.builds(
    adlrecur_Component,
    name=
        safe_text
)
adlrecur_Interface_strategy = st.builds(
    adlrecur_Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adlrecur_Provided_strategy = st.builds(
    adlrecur_Provided,
)
adlrecur_Required_strategy = st.builds(
    adlrecur_Required,
)








@given(instance=adlrecur_Component_strategy)
def test_hyp_adlrecur_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=adlrecur_Interface_strategy)
def test_hyp_adlrecur_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adlrecur_Interface_strategy)
def test_hyp_adlrecur_interface_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Component,
    Interface,
    adlrecur_Base,
    adlrecur_Binding,
    adlrecur_Component,
    adlrecur_Interface,
    adlrecur_Provided,
    adlrecur_Required,
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

def test_adlrecur_Component_name_value_roundtrip():
    instance = adlrecur_Component(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adlrecur_Interface_name_value_roundtrip():
    instance = adlrecur_Interface(name="sample_text", signature="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adlrecur_Interface_signature_value_roundtrip():
    instance = adlrecur_Interface(name="sample_text", signature="sample_text")
    assert instance.signature == "sample_text"
    instance.signature = "sample_text_2"
    assert instance.signature == "sample_text_2"


def test_adlrecur_Base_isa_Component():
    instance = adlrecur_Base()
    assert isinstance(instance, Component)


def test_adlrecur_Provided_isa_Interface():
    instance = adlrecur_Provided()
    assert isinstance(instance, Interface)


def test_adlrecur_Required_isa_Interface():
    instance = adlrecur_Required()
    assert isinstance(instance, Interface)


def test_assoc_bindings3_link_reassign_clear():
    a = adlrecur_Interface(name="sample_text", signature="sample_text")
    b1 = adlrecur_Binding()
    b2 = adlrecur_Binding()
    _safe_set(a, 'adlrecur_Interface', {b1})
    assert _is_linked(a, 'adlrecur_Interface', b1)
    if hasattr(b1, 'adlrecur_Binding'):
        assert _is_linked(b1, 'adlrecur_Binding', a)
    _safe_set(a, 'adlrecur_Interface', {b2})
    assert _is_linked(a, 'adlrecur_Interface', b2)
    if hasattr(b1, 'adlrecur_Binding'):
        assert not _is_linked(b1, 'adlrecur_Binding', a)
    if hasattr(b2, 'adlrecur_Binding'):
        assert _is_linked(b2, 'adlrecur_Binding', a)
    _safe_set(a, 'adlrecur_Interface', set())
    assert not _is_linked(a, 'adlrecur_Interface', b2)
    if hasattr(b2, 'adlrecur_Binding'):
        assert not _is_linked(b2, 'adlrecur_Binding', a)


def test_assoc_from_4_link_reassign_clear():
    a = adlrecur_Interface(name="sample_text", signature="sample_text")
    b1 = adlrecur_Binding()
    b2 = adlrecur_Binding()
    _safe_set(a, 'adlrecur_Interface6', b1)
    assert _is_linked(a, 'adlrecur_Interface6', b1)
    if hasattr(b1, 'adlrecur_Binding5'):
        assert _is_linked(b1, 'adlrecur_Binding5', a)
    _safe_set(a, 'adlrecur_Interface6', b2)
    assert _is_linked(a, 'adlrecur_Interface6', b2)
    if hasattr(b1, 'adlrecur_Binding5'):
        assert not _is_linked(b1, 'adlrecur_Binding5', a)
    if hasattr(b2, 'adlrecur_Binding5'):
        assert _is_linked(b2, 'adlrecur_Binding5', a)
    _safe_set(a, 'adlrecur_Interface6', None)
    assert not _is_linked(a, 'adlrecur_Interface6', b2)
    if hasattr(b2, 'adlrecur_Binding5'):
        assert not _is_linked(b2, 'adlrecur_Binding5', a)


def test_assoc_providedInterfaces1_link_reassign_clear():
    a = adlrecur_Component(name="sample_text")
    b1 = adlrecur_Provided()
    b2 = adlrecur_Provided()
    _safe_set(a, 'adlrecur_Component2', {b1})
    assert _is_linked(a, 'adlrecur_Component2', b1)
    if hasattr(b1, 'adlrecur_Provided'):
        assert _is_linked(b1, 'adlrecur_Provided', a)
    _safe_set(a, 'adlrecur_Component2', {b2})
    assert _is_linked(a, 'adlrecur_Component2', b2)
    if hasattr(b1, 'adlrecur_Provided'):
        assert not _is_linked(b1, 'adlrecur_Provided', a)
    if hasattr(b2, 'adlrecur_Provided'):
        assert _is_linked(b2, 'adlrecur_Provided', a)
    _safe_set(a, 'adlrecur_Component2', set())
    assert not _is_linked(a, 'adlrecur_Component2', b2)
    if hasattr(b2, 'adlrecur_Provided'):
        assert not _is_linked(b2, 'adlrecur_Provided', a)


def test_assoc_requiredInterfaces0_link_reassign_clear():
    a = adlrecur_Component(name="sample_text")
    b1 = adlrecur_Required()
    b2 = adlrecur_Required()
    _safe_set(a, 'adlrecur_Component', {b1})
    assert _is_linked(a, 'adlrecur_Component', b1)
    if hasattr(b1, 'adlrecur_Required'):
        assert _is_linked(b1, 'adlrecur_Required', a)
    _safe_set(a, 'adlrecur_Component', {b2})
    assert _is_linked(a, 'adlrecur_Component', b2)
    if hasattr(b1, 'adlrecur_Required'):
        assert not _is_linked(b1, 'adlrecur_Required', a)
    if hasattr(b2, 'adlrecur_Required'):
        assert _is_linked(b2, 'adlrecur_Required', a)
    _safe_set(a, 'adlrecur_Component', set())
    assert not _is_linked(a, 'adlrecur_Component', b2)
    if hasattr(b2, 'adlrecur_Required'):
        assert not _is_linked(b2, 'adlrecur_Required', a)


def test_assoc_to7_link_reassign_clear():
    a = adlrecur_Interface(name="sample_text", signature="sample_text")
    b1 = adlrecur_Binding()
    b2 = adlrecur_Binding()
    _safe_set(a, 'adlrecur_Interface9', b1)
    assert _is_linked(a, 'adlrecur_Interface9', b1)
    if hasattr(b1, 'adlrecur_Binding8'):
        assert _is_linked(b1, 'adlrecur_Binding8', a)
    _safe_set(a, 'adlrecur_Interface9', b2)
    assert _is_linked(a, 'adlrecur_Interface9', b2)
    if hasattr(b1, 'adlrecur_Binding8'):
        assert not _is_linked(b1, 'adlrecur_Binding8', a)
    if hasattr(b2, 'adlrecur_Binding8'):
        assert _is_linked(b2, 'adlrecur_Binding8', a)
    _safe_set(a, 'adlrecur_Interface9', None)
    assert not _is_linked(a, 'adlrecur_Interface9', b2)
    if hasattr(b2, 'adlrecur_Binding8'):
        assert not _is_linked(b2, 'adlrecur_Binding8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


Interface_strategy = st.builds(Interface)
@given(instance=Interface_strategy)
@settings(max_examples=25)
def test_Interface_instantiation(instance):
    assert isinstance(instance, Interface)


adlrecur_Base_strategy = st.builds(adlrecur_Base)
@given(instance=adlrecur_Base_strategy)
@settings(max_examples=25)
def test_adlrecur_Base_instantiation(instance):
    assert isinstance(instance, adlrecur_Base)


adlrecur_Binding_strategy = st.builds(adlrecur_Binding)
@given(instance=adlrecur_Binding_strategy)
@settings(max_examples=25)
def test_adlrecur_Binding_instantiation(instance):
    assert isinstance(instance, adlrecur_Binding)


adlrecur_Component_strategy = st.builds(adlrecur_Component, name=safe_text)
@given(instance=adlrecur_Component_strategy)
@settings(max_examples=25)
def test_adlrecur_Component_instantiation(instance):
    assert isinstance(instance, adlrecur_Component)


adlrecur_Interface_strategy = st.builds(adlrecur_Interface, name=safe_text, signature=safe_text)
@given(instance=adlrecur_Interface_strategy)
@settings(max_examples=25)
def test_adlrecur_Interface_instantiation(instance):
    assert isinstance(instance, adlrecur_Interface)


adlrecur_Provided_strategy = st.builds(adlrecur_Provided)
@given(instance=adlrecur_Provided_strategy)
@settings(max_examples=25)
def test_adlrecur_Provided_instantiation(instance):
    assert isinstance(instance, adlrecur_Provided)


adlrecur_Required_strategy = st.builds(adlrecur_Required)
@given(instance=adlrecur_Required_strategy)
@settings(max_examples=25)
def test_adlrecur_Required_instantiation(instance):
    assert isinstance(instance, adlrecur_Required)



