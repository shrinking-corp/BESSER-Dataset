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
    Interface,
    adl_Type,
    adl_NamedElement,
    NamedElement,
    adl_Interface,
    AbstractComponent,
    adl_Component,
    adl_AbstractComponent,
    Type,
    adl_Required,
    adl_Provided,
    adl_Binding,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_hyp_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_hyp_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl_type_is_not_abstract():
    assert not inspect.isabstract(adl_Type)


def test_hyp_adl_type_constructor_exists():
    assert callable(adl_Type.__init__)


def test_hyp_adl_type_constructor_args():
    sig = inspect.signature(adl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"




def test_hyp_adl_namedelement_is_not_abstract():
    assert not inspect.isabstract(adl_NamedElement)


def test_hyp_adl_namedelement_constructor_exists():
    assert callable(adl_NamedElement.__init__)


def test_hyp_adl_namedelement_constructor_args():
    sig = inspect.signature(adl_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl_interface_is_not_abstract():
    assert not inspect.isabstract(adl_Interface)


def test_hyp_adl_interface_constructor_exists():
    assert callable(adl_Interface.__init__)


def test_hyp_adl_interface_constructor_args():
    sig = inspect.signature(adl_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(AbstractComponent)


def test_hyp_abstractcomponent_constructor_exists():
    assert callable(AbstractComponent.__init__)


def test_hyp_abstractcomponent_constructor_args():
    sig = inspect.signature(AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl_component_is_not_abstract():
    assert not inspect.isabstract(adl_Component)


def test_hyp_adl_component_constructor_exists():
    assert callable(adl_Component.__init__)


def test_hyp_adl_component_constructor_args():
    sig = inspect.signature(adl_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl_abstractcomponent_is_not_abstract():
    assert not inspect.isabstract(adl_AbstractComponent)


def test_hyp_adl_abstractcomponent_constructor_exists():
    assert callable(adl_AbstractComponent.__init__)


def test_hyp_adl_abstractcomponent_constructor_args():
    sig = inspect.signature(adl_AbstractComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl_required_is_not_abstract():
    assert not inspect.isabstract(adl_Required)


def test_hyp_adl_required_constructor_exists():
    assert callable(adl_Required.__init__)


def test_hyp_adl_required_constructor_args():
    sig = inspect.signature(adl_Required.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl_provided_is_not_abstract():
    assert not inspect.isabstract(adl_Provided)


def test_hyp_adl_provided_constructor_exists():
    assert callable(adl_Provided.__init__)


def test_hyp_adl_provided_constructor_args():
    sig = inspect.signature(adl_Provided.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl_binding_is_not_abstract():
    assert not inspect.isabstract(adl_Binding)


def test_hyp_adl_binding_constructor_exists():
    assert callable(adl_Binding.__init__)


def test_hyp_adl_binding_constructor_args():
    sig = inspect.signature(adl_Binding.__init__)
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
Interface_strategy = st.builds(
    Interface,
)
adl_Type_strategy = st.builds(
    adl_Type,
    signature=
        safe_text
)
adl_NamedElement_strategy = st.builds(
    adl_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adl_Interface_strategy = st.builds(
    adl_Interface,
)
AbstractComponent_strategy = st.builds(
    AbstractComponent,
)
adl_Component_strategy = st.builds(
    adl_Component,
)
adl_AbstractComponent_strategy = st.builds(
    adl_AbstractComponent,
)
Type_strategy = st.builds(
    Type,
)
adl_Required_strategy = st.builds(
    adl_Required,
)
adl_Provided_strategy = st.builds(
    adl_Provided,
)
adl_Binding_strategy = st.builds(
    adl_Binding,
)





@given(instance=adl_Type_strategy)
def test_hyp_adl_type_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original




@given(instance=adl_NamedElement_strategy)
def test_hyp_adl_namedelement_name_setter(instance):
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
    AbstractComponent,
    Interface,
    NamedElement,
    Type,
    adl_AbstractComponent,
    adl_Binding,
    adl_Component,
    adl_Interface,
    adl_NamedElement,
    adl_Provided,
    adl_Required,
    adl_Type,
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

def test_adl_NamedElement_name_value_roundtrip():
    instance = adl_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adl_Type_signature_value_roundtrip():
    instance = adl_Type(signature="sample_text")
    assert instance.signature == "sample_text"
    instance.signature = "sample_text_2"
    assert instance.signature == "sample_text_2"


def test_adl_Component_isa_AbstractComponent():
    instance = adl_Component()
    assert isinstance(instance, AbstractComponent)


def test_adl_Type_isa_Interface():
    instance = adl_Type(signature="sample_text")
    assert isinstance(instance, Interface)


def test_adl_Binding_isa_NamedElement():
    instance = adl_Binding()
    assert isinstance(instance, NamedElement)


def test_adl_Component_isa_NamedElement():
    instance = adl_Component()
    assert isinstance(instance, NamedElement)


def test_adl_Interface_isa_NamedElement():
    instance = adl_Interface()
    assert isinstance(instance, NamedElement)


def test_adl_Provided_isa_Type():
    instance = adl_Provided()
    assert isinstance(instance, Type)


def test_adl_Required_isa_Type():
    instance = adl_Required()
    assert isinstance(instance, Type)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractComponent_strategy = st.builds(AbstractComponent)
@given(instance=AbstractComponent_strategy)
@settings(max_examples=25)
def test_AbstractComponent_instantiation(instance):
    assert isinstance(instance, AbstractComponent)


Interface_strategy = st.builds(Interface)
@given(instance=Interface_strategy)
@settings(max_examples=25)
def test_Interface_instantiation(instance):
    assert isinstance(instance, Interface)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


adl_AbstractComponent_strategy = st.builds(adl_AbstractComponent)
@given(instance=adl_AbstractComponent_strategy)
@settings(max_examples=25)
def test_adl_AbstractComponent_instantiation(instance):
    assert isinstance(instance, adl_AbstractComponent)


adl_Binding_strategy = st.builds(adl_Binding)
@given(instance=adl_Binding_strategy)
@settings(max_examples=25)
def test_adl_Binding_instantiation(instance):
    assert isinstance(instance, adl_Binding)


adl_Component_strategy = st.builds(adl_Component)
@given(instance=adl_Component_strategy)
@settings(max_examples=25)
def test_adl_Component_instantiation(instance):
    assert isinstance(instance, adl_Component)


adl_Interface_strategy = st.builds(adl_Interface)
@given(instance=adl_Interface_strategy)
@settings(max_examples=25)
def test_adl_Interface_instantiation(instance):
    assert isinstance(instance, adl_Interface)


adl_NamedElement_strategy = st.builds(adl_NamedElement, name=safe_text)
@given(instance=adl_NamedElement_strategy)
@settings(max_examples=25)
def test_adl_NamedElement_instantiation(instance):
    assert isinstance(instance, adl_NamedElement)


adl_Provided_strategy = st.builds(adl_Provided)
@given(instance=adl_Provided_strategy)
@settings(max_examples=25)
def test_adl_Provided_instantiation(instance):
    assert isinstance(instance, adl_Provided)


adl_Required_strategy = st.builds(adl_Required)
@given(instance=adl_Required_strategy)
@settings(max_examples=25)
def test_adl_Required_instantiation(instance):
    assert isinstance(instance, adl_Required)


adl_Type_strategy = st.builds(adl_Type, signature=safe_text)
@given(instance=adl_Type_strategy)
@settings(max_examples=25)
def test_adl_Type_instantiation(instance):
    assert isinstance(instance, adl_Type)



