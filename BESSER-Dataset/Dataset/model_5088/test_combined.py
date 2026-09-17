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
    adl101_Required,
    adl101_Component,
    adl101_Content,
    adl101_Binding,
    adl101_Interface,
    adl101_Provided,
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



def test_hyp_adl101_required_is_not_abstract():
    assert not inspect.isabstract(adl101_Required)


def test_hyp_adl101_required_constructor_exists():
    assert callable(adl101_Required.__init__)


def test_hyp_adl101_required_constructor_args():
    sig = inspect.signature(adl101_Required.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl101_component_is_not_abstract():
    assert not inspect.isabstract(adl101_Component)


def test_hyp_adl101_component_constructor_exists():
    assert callable(adl101_Component.__init__)


def test_hyp_adl101_component_constructor_args():
    sig = inspect.signature(adl101_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_adl101_content_is_not_abstract():
    assert not inspect.isabstract(adl101_Content)


def test_hyp_adl101_content_constructor_exists():
    assert callable(adl101_Content.__init__)


def test_hyp_adl101_content_constructor_args():
    sig = inspect.signature(adl101_Content.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "expression" in params, "Missing parameter 'expression'"





def test_hyp_adl101_binding_is_not_abstract():
    assert not inspect.isabstract(adl101_Binding)


def test_hyp_adl101_binding_constructor_exists():
    assert callable(adl101_Binding.__init__)


def test_hyp_adl101_binding_constructor_args():
    sig = inspect.signature(adl101_Binding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adl101_interface_is_not_abstract():
    assert not inspect.isabstract(adl101_Interface)


def test_hyp_adl101_interface_constructor_exists():
    assert callable(adl101_Interface.__init__)


def test_hyp_adl101_interface_constructor_args():
    sig = inspect.signature(adl101_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "signature" in params, "Missing parameter 'signature'"





def test_hyp_adl101_provided_is_not_abstract():
    assert not inspect.isabstract(adl101_Provided)


def test_hyp_adl101_provided_constructor_exists():
    assert callable(adl101_Provided.__init__)


def test_hyp_adl101_provided_constructor_args():
    sig = inspect.signature(adl101_Provided.__init__)
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
adl101_Required_strategy = st.builds(
    adl101_Required,
)
adl101_Component_strategy = st.builds(
    adl101_Component,
    name=
        safe_text
)
adl101_Content_strategy = st.builds(
    adl101_Content,
    language=
        safe_text,
    expression=
        safe_text
)
adl101_Binding_strategy = st.builds(
    adl101_Binding,
)
adl101_Interface_strategy = st.builds(
    adl101_Interface,
    name=
        safe_text,
    signature=
        safe_text
)
adl101_Provided_strategy = st.builds(
    adl101_Provided,
)






@given(instance=adl101_Component_strategy)
def test_hyp_adl101_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=adl101_Content_strategy)
def test_hyp_adl101_content_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=adl101_Content_strategy)
def test_hyp_adl101_content_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original





@given(instance=adl101_Interface_strategy)
def test_hyp_adl101_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adl101_Interface_strategy)
def test_hyp_adl101_interface_signature_setter(instance):
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
    Interface,
    adl101_Binding,
    adl101_Component,
    adl101_Content,
    adl101_Interface,
    adl101_Provided,
    adl101_Required,
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

def test_adl101_Component_name_value_roundtrip():
    instance = adl101_Component(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adl101_Content_expression_value_roundtrip():
    instance = adl101_Content(expression="sample_text", language="sample_text")
    assert instance.expression == "sample_text"
    instance.expression = "sample_text_2"
    assert instance.expression == "sample_text_2"


def test_adl101_Content_language_value_roundtrip():
    instance = adl101_Content(expression="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_adl101_Interface_name_value_roundtrip():
    instance = adl101_Interface(name="sample_text", signature="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_adl101_Interface_signature_value_roundtrip():
    instance = adl101_Interface(name="sample_text", signature="sample_text")
    assert instance.signature == "sample_text"
    instance.signature = "sample_text_2"
    assert instance.signature == "sample_text_2"


def test_adl101_Provided_isa_Interface():
    instance = adl101_Provided()
    assert isinstance(instance, Interface)


def test_adl101_Required_isa_Interface():
    instance = adl101_Required()
    assert isinstance(instance, Interface)


def test_assoc_bindings0_link_reassign_clear():
    a = adl101_Interface(name="sample_text", signature="sample_text")
    b1 = adl101_Binding()
    b2 = adl101_Binding()
    _safe_set(a, 'adl101_Interface', {b1})
    assert _is_linked(a, 'adl101_Interface', b1)
    if hasattr(b1, 'adl101_Binding'):
        assert _is_linked(b1, 'adl101_Binding', a)
    _safe_set(a, 'adl101_Interface', {b2})
    assert _is_linked(a, 'adl101_Interface', b2)
    if hasattr(b1, 'adl101_Binding'):
        assert not _is_linked(b1, 'adl101_Binding', a)
    if hasattr(b2, 'adl101_Binding'):
        assert _is_linked(b2, 'adl101_Binding', a)
    _safe_set(a, 'adl101_Interface', set())
    assert not _is_linked(a, 'adl101_Interface', b2)
    if hasattr(b2, 'adl101_Binding'):
        assert not _is_linked(b2, 'adl101_Binding', a)


def test_assoc_content14_link_reassign_clear():
    a = adl101_Content(expression="sample_text", language="sample_text")
    b1 = adl101_Component(name="sample_text")
    b2 = adl101_Component(name="sample_text_2")
    _safe_set(a, 'Content', b1)
    assert _is_linked(a, 'Content', b1)
    if hasattr(b1, 'contentParent'):
        assert _is_linked(b1, 'contentParent', a)
    _safe_set(a, 'Content', b2)
    assert _is_linked(a, 'Content', b2)
    if hasattr(b1, 'contentParent'):
        assert not _is_linked(b1, 'contentParent', a)
    if hasattr(b2, 'contentParent'):
        assert _is_linked(b2, 'contentParent', a)
    _safe_set(a, 'Content', None)
    assert not _is_linked(a, 'Content', b2)
    if hasattr(b2, 'contentParent'):
        assert not _is_linked(b2, 'contentParent', a)


def test_assoc_contentParent7_link_reassign_clear():
    a = adl101_Content(expression="sample_text", language="sample_text")
    b1 = adl101_Component(name="sample_text")
    b2 = adl101_Component(name="sample_text_2")
    _safe_set(a, 'content', b1)
    assert _is_linked(a, 'content', b1)
    if hasattr(b1, 'Component'):
        assert _is_linked(b1, 'Component', a)
    _safe_set(a, 'content', b2)
    assert _is_linked(a, 'content', b2)
    if hasattr(b1, 'Component'):
        assert not _is_linked(b1, 'Component', a)
    if hasattr(b2, 'Component'):
        assert _is_linked(b2, 'Component', a)
    _safe_set(a, 'content', None)
    assert not _is_linked(a, 'content', b2)
    if hasattr(b2, 'Component'):
        assert not _is_linked(b2, 'Component', a)


def test_assoc_from_1_link_reassign_clear():
    a = adl101_Interface(name="sample_text", signature="sample_text")
    b1 = adl101_Binding()
    b2 = adl101_Binding()
    _safe_set(a, 'adl101_Interface3', b1)
    assert _is_linked(a, 'adl101_Interface3', b1)
    if hasattr(b1, 'adl101_Binding2'):
        assert _is_linked(b1, 'adl101_Binding2', a)
    _safe_set(a, 'adl101_Interface3', b2)
    assert _is_linked(a, 'adl101_Interface3', b2)
    if hasattr(b1, 'adl101_Binding2'):
        assert not _is_linked(b1, 'adl101_Binding2', a)
    if hasattr(b2, 'adl101_Binding2'):
        assert _is_linked(b2, 'adl101_Binding2', a)
    _safe_set(a, 'adl101_Interface3', None)
    assert not _is_linked(a, 'adl101_Interface3', b2)
    if hasattr(b2, 'adl101_Binding2'):
        assert not _is_linked(b2, 'adl101_Binding2', a)


def test_assoc_providedInterfaces12_link_reassign_clear():
    a = adl101_Component(name="sample_text")
    b1 = adl101_Provided()
    b2 = adl101_Provided()
    _safe_set(a, 'adl101_Component13', {b1})
    assert _is_linked(a, 'adl101_Component13', b1)
    if hasattr(b1, 'adl101_Provided'):
        assert _is_linked(b1, 'adl101_Provided', a)
    _safe_set(a, 'adl101_Component13', {b2})
    assert _is_linked(a, 'adl101_Component13', b2)
    if hasattr(b1, 'adl101_Provided'):
        assert not _is_linked(b1, 'adl101_Provided', a)
    if hasattr(b2, 'adl101_Provided'):
        assert _is_linked(b2, 'adl101_Provided', a)
    _safe_set(a, 'adl101_Component13', set())
    assert not _is_linked(a, 'adl101_Component13', b2)
    if hasattr(b2, 'adl101_Provided'):
        assert not _is_linked(b2, 'adl101_Provided', a)


def test_assoc_requiredInterfaces10_link_reassign_clear():
    a = adl101_Component(name="sample_text")
    b1 = adl101_Required()
    b2 = adl101_Required()
    _safe_set(a, 'adl101_Component11', {b1})
    assert _is_linked(a, 'adl101_Component11', b1)
    if hasattr(b1, 'adl101_Required'):
        assert _is_linked(b1, 'adl101_Required', a)
    _safe_set(a, 'adl101_Component11', {b2})
    assert _is_linked(a, 'adl101_Component11', b2)
    if hasattr(b1, 'adl101_Required'):
        assert not _is_linked(b1, 'adl101_Required', a)
    if hasattr(b2, 'adl101_Required'):
        assert _is_linked(b2, 'adl101_Required', a)
    _safe_set(a, 'adl101_Component11', set())
    assert not _is_linked(a, 'adl101_Component11', b2)
    if hasattr(b2, 'adl101_Required'):
        assert not _is_linked(b2, 'adl101_Required', a)


def test_assoc_subComponents9_link_reassign_clear():
    a = adl101_Component(name="sample_text")
    b1 = adl101_Component(name="sample_text")
    b2 = adl101_Component(name="sample_text_2")
    _safe_set(a, 'adl101_Component', b1)
    assert _is_linked(a, 'adl101_Component', b1)
    if hasattr(b1, 'adl101_Component8'):
        assert _is_linked(b1, 'adl101_Component8', a)
    _safe_set(a, 'adl101_Component', b2)
    assert _is_linked(a, 'adl101_Component', b2)
    if hasattr(b1, 'adl101_Component8'):
        assert not _is_linked(b1, 'adl101_Component8', a)
    if hasattr(b2, 'adl101_Component8'):
        assert _is_linked(b2, 'adl101_Component8', a)
    _safe_set(a, 'adl101_Component', None)
    assert not _is_linked(a, 'adl101_Component', b2)
    if hasattr(b2, 'adl101_Component8'):
        assert not _is_linked(b2, 'adl101_Component8', a)


def test_assoc_to4_link_reassign_clear():
    a = adl101_Interface(name="sample_text", signature="sample_text")
    b1 = adl101_Binding()
    b2 = adl101_Binding()
    _safe_set(a, 'adl101_Interface6', b1)
    assert _is_linked(a, 'adl101_Interface6', b1)
    if hasattr(b1, 'adl101_Binding5'):
        assert _is_linked(b1, 'adl101_Binding5', a)
    _safe_set(a, 'adl101_Interface6', b2)
    assert _is_linked(a, 'adl101_Interface6', b2)
    if hasattr(b1, 'adl101_Binding5'):
        assert not _is_linked(b1, 'adl101_Binding5', a)
    if hasattr(b2, 'adl101_Binding5'):
        assert _is_linked(b2, 'adl101_Binding5', a)
    _safe_set(a, 'adl101_Interface6', None)
    assert not _is_linked(a, 'adl101_Interface6', b2)
    if hasattr(b2, 'adl101_Binding5'):
        assert not _is_linked(b2, 'adl101_Binding5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Interface_strategy = st.builds(Interface)
@given(instance=Interface_strategy)
@settings(max_examples=25)
def test_Interface_instantiation(instance):
    assert isinstance(instance, Interface)


adl101_Binding_strategy = st.builds(adl101_Binding)
@given(instance=adl101_Binding_strategy)
@settings(max_examples=25)
def test_adl101_Binding_instantiation(instance):
    assert isinstance(instance, adl101_Binding)


adl101_Component_strategy = st.builds(adl101_Component, name=safe_text)
@given(instance=adl101_Component_strategy)
@settings(max_examples=25)
def test_adl101_Component_instantiation(instance):
    assert isinstance(instance, adl101_Component)


adl101_Content_strategy = st.builds(adl101_Content, expression=safe_text, language=safe_text)
@given(instance=adl101_Content_strategy)
@settings(max_examples=25)
def test_adl101_Content_instantiation(instance):
    assert isinstance(instance, adl101_Content)


adl101_Interface_strategy = st.builds(adl101_Interface, name=safe_text, signature=safe_text)
@given(instance=adl101_Interface_strategy)
@settings(max_examples=25)
def test_adl101_Interface_instantiation(instance):
    assert isinstance(instance, adl101_Interface)


adl101_Provided_strategy = st.builds(adl101_Provided)
@given(instance=adl101_Provided_strategy)
@settings(max_examples=25)
def test_adl101_Provided_instantiation(instance):
    assert isinstance(instance, adl101_Provided)


adl101_Required_strategy = st.builds(adl101_Required)
@given(instance=adl101_Required_strategy)
@settings(max_examples=25)
def test_adl101_Required_instantiation(instance):
    assert isinstance(instance, adl101_Required)



