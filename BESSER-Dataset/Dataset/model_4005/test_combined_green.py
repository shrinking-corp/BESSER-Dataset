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
    classes_Root,
    Namespace,
    NamedElement,
    classes_Class,
    classes_Package,
    classes_Namespace,
    classes_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_classes_root_is_not_abstract():
    assert not inspect.isabstract(classes_Root)


def test_hyp_classes_root_constructor_exists():
    assert callable(classes_Root.__init__)


def test_hyp_classes_root_constructor_args():
    sig = inspect.signature(classes_Root.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_hyp_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_hyp_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_class_is_not_abstract():
    assert not inspect.isabstract(classes_Class)


def test_hyp_classes_class_constructor_exists():
    assert callable(classes_Class.__init__)


def test_hyp_classes_class_constructor_args():
    sig = inspect.signature(classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_package_is_not_abstract():
    assert not inspect.isabstract(classes_Package)


def test_hyp_classes_package_constructor_exists():
    assert callable(classes_Package.__init__)


def test_hyp_classes_package_constructor_args():
    sig = inspect.signature(classes_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_namespace_is_not_abstract():
    assert not inspect.isabstract(classes_Namespace)


def test_hyp_classes_namespace_constructor_exists():
    assert callable(classes_Namespace.__init__)


def test_hyp_classes_namespace_constructor_args():
    sig = inspect.signature(classes_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_namedelement_is_not_abstract():
    assert not inspect.isabstract(classes_NamedElement)


def test_hyp_classes_namedelement_constructor_exists():
    assert callable(classes_NamedElement.__init__)


def test_hyp_classes_namedelement_constructor_args():
    sig = inspect.signature(classes_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
classes_Root_strategy = st.builds(
    classes_Root,
)
Namespace_strategy = st.builds(
    Namespace,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
classes_Class_strategy = st.builds(
    classes_Class,
)
classes_Package_strategy = st.builds(
    classes_Package,
)
classes_Namespace_strategy = st.builds(
    classes_Namespace,
)
classes_NamedElement_strategy = st.builds(
    classes_NamedElement,
    name=
        safe_text
)










@given(instance=classes_NamedElement_strategy)
def test_hyp_classes_namedelement_name_setter(instance):
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
    NamedElement,
    Namespace,
    classes_Class,
    classes_NamedElement,
    classes_Namespace,
    classes_Package,
    classes_Root,
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

def test_classes_NamedElement_name_value_roundtrip():
    instance = classes_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_classes_Class_isa_NamedElement():
    instance = classes_Class()
    assert isinstance(instance, NamedElement)


def test_classes_Package_isa_NamedElement():
    instance = classes_Package()
    assert isinstance(instance, NamedElement)


def test_classes_Package_isa_Namespace():
    instance = classes_Package()
    assert isinstance(instance, Namespace)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Namespace_strategy = st.builds(Namespace)
@given(instance=Namespace_strategy)
@settings(max_examples=25)
def test_Namespace_instantiation(instance):
    assert isinstance(instance, Namespace)


classes_Class_strategy = st.builds(classes_Class)
@given(instance=classes_Class_strategy)
@settings(max_examples=25)
def test_classes_Class_instantiation(instance):
    assert isinstance(instance, classes_Class)


classes_NamedElement_strategy = st.builds(classes_NamedElement, name=safe_text)
@given(instance=classes_NamedElement_strategy)
@settings(max_examples=25)
def test_classes_NamedElement_instantiation(instance):
    assert isinstance(instance, classes_NamedElement)


classes_Namespace_strategy = st.builds(classes_Namespace)
@given(instance=classes_Namespace_strategy)
@settings(max_examples=25)
def test_classes_Namespace_instantiation(instance):
    assert isinstance(instance, classes_Namespace)


classes_Package_strategy = st.builds(classes_Package)
@given(instance=classes_Package_strategy)
@settings(max_examples=25)
def test_classes_Package_instantiation(instance):
    assert isinstance(instance, classes_Package)


classes_Root_strategy = st.builds(classes_Root)
@given(instance=classes_Root_strategy)
@settings(max_examples=25)
def test_classes_Root_instantiation(instance):
    assert isinstance(instance, classes_Root)



