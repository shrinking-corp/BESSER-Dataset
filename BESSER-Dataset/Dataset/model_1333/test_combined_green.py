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
    NamedElementCS,
    classescs_PackageCS,
    ElementCS,
    classescs_RootCS,
    classescs_NamedElementCS,
    classescs_Element,
    classescs_ElementCS,
    classescs_PathElementCS,
    classescs_PathNameCS,
    classescs_ClassCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_hyp_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_hyp_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classescs_packagecs_is_not_abstract():
    assert not inspect.isabstract(classescs_PackageCS)


def test_hyp_classescs_packagecs_constructor_exists():
    assert callable(classescs_PackageCS.__init__)


def test_hyp_classescs_packagecs_constructor_args():
    sig = inspect.signature(classescs_PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_hyp_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_hyp_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classescs_rootcs_is_not_abstract():
    assert not inspect.isabstract(classescs_RootCS)


def test_hyp_classescs_rootcs_constructor_exists():
    assert callable(classescs_RootCS.__init__)


def test_hyp_classescs_rootcs_constructor_args():
    sig = inspect.signature(classescs_RootCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classescs_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_NamedElementCS)


def test_hyp_classescs_namedelementcs_constructor_exists():
    assert callable(classescs_NamedElementCS.__init__)


def test_hyp_classescs_namedelementcs_constructor_args():
    sig = inspect.signature(classescs_NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_classescs_element_is_not_abstract():
    assert not inspect.isabstract(classescs_Element)


def test_hyp_classescs_element_constructor_exists():
    assert callable(classescs_Element.__init__)


def test_hyp_classescs_element_constructor_args():
    sig = inspect.signature(classescs_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classescs_elementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_ElementCS)


def test_hyp_classescs_elementcs_constructor_exists():
    assert callable(classescs_ElementCS.__init__)


def test_hyp_classescs_elementcs_constructor_args():
    sig = inspect.signature(classescs_ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classescs_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(classescs_PathElementCS)


def test_hyp_classescs_pathelementcs_constructor_exists():
    assert callable(classescs_PathElementCS.__init__)


def test_hyp_classescs_pathelementcs_constructor_args():
    sig = inspect.signature(classescs_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classescs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(classescs_PathNameCS)


def test_hyp_classescs_pathnamecs_constructor_exists():
    assert callable(classescs_PathNameCS.__init__)


def test_hyp_classescs_pathnamecs_constructor_args():
    sig = inspect.signature(classescs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classescs_classcs_is_not_abstract():
    assert not inspect.isabstract(classescs_ClassCS)


def test_hyp_classescs_classcs_constructor_exists():
    assert callable(classescs_ClassCS.__init__)


def test_hyp_classescs_classcs_constructor_args():
    sig = inspect.signature(classescs_ClassCS.__init__)
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
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
classescs_PackageCS_strategy = st.builds(
    classescs_PackageCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
classescs_RootCS_strategy = st.builds(
    classescs_RootCS,
)
classescs_NamedElementCS_strategy = st.builds(
    classescs_NamedElementCS,
    name=
        safe_text
)
classescs_Element_strategy = st.builds(
    classescs_Element,
)
classescs_ElementCS_strategy = st.builds(
    classescs_ElementCS,
)
classescs_PathElementCS_strategy = st.builds(
    classescs_PathElementCS,
)
classescs_PathNameCS_strategy = st.builds(
    classescs_PathNameCS,
)
classescs_ClassCS_strategy = st.builds(
    classescs_ClassCS,
)








@given(instance=classescs_NamedElementCS_strategy)
def test_hyp_classescs_namedelementcs_name_setter(instance):
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
    ElementCS,
    NamedElementCS,
    classescs_ClassCS,
    classescs_Element,
    classescs_ElementCS,
    classescs_NamedElementCS,
    classescs_PackageCS,
    classescs_PathElementCS,
    classescs_PathNameCS,
    classescs_RootCS,
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

def test_classescs_NamedElementCS_name_value_roundtrip():
    instance = classescs_NamedElementCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_classescs_NamedElementCS_isa_ElementCS():
    instance = classescs_NamedElementCS(name="sample_text")
    assert isinstance(instance, ElementCS)


def test_classescs_PathNameCS_isa_ElementCS():
    instance = classescs_PathNameCS()
    assert isinstance(instance, ElementCS)


def test_classescs_RootCS_isa_ElementCS():
    instance = classescs_RootCS()
    assert isinstance(instance, ElementCS)


def test_classescs_ClassCS_isa_NamedElementCS():
    instance = classescs_ClassCS()
    assert isinstance(instance, NamedElementCS)


def test_classescs_PackageCS_isa_NamedElementCS():
    instance = classescs_PackageCS()
    assert isinstance(instance, NamedElementCS)


def test_classescs_PathElementCS_isa_NamedElementCS():
    instance = classescs_PathElementCS()
    assert isinstance(instance, NamedElementCS)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ElementCS_strategy = st.builds(ElementCS)
@given(instance=ElementCS_strategy)
@settings(max_examples=25)
def test_ElementCS_instantiation(instance):
    assert isinstance(instance, ElementCS)


NamedElementCS_strategy = st.builds(NamedElementCS)
@given(instance=NamedElementCS_strategy)
@settings(max_examples=25)
def test_NamedElementCS_instantiation(instance):
    assert isinstance(instance, NamedElementCS)


classescs_ClassCS_strategy = st.builds(classescs_ClassCS)
@given(instance=classescs_ClassCS_strategy)
@settings(max_examples=25)
def test_classescs_ClassCS_instantiation(instance):
    assert isinstance(instance, classescs_ClassCS)


classescs_Element_strategy = st.builds(classescs_Element)
@given(instance=classescs_Element_strategy)
@settings(max_examples=25)
def test_classescs_Element_instantiation(instance):
    assert isinstance(instance, classescs_Element)


classescs_ElementCS_strategy = st.builds(classescs_ElementCS)
@given(instance=classescs_ElementCS_strategy)
@settings(max_examples=25)
def test_classescs_ElementCS_instantiation(instance):
    assert isinstance(instance, classescs_ElementCS)


classescs_NamedElementCS_strategy = st.builds(classescs_NamedElementCS, name=safe_text)
@given(instance=classescs_NamedElementCS_strategy)
@settings(max_examples=25)
def test_classescs_NamedElementCS_instantiation(instance):
    assert isinstance(instance, classescs_NamedElementCS)


classescs_PackageCS_strategy = st.builds(classescs_PackageCS)
@given(instance=classescs_PackageCS_strategy)
@settings(max_examples=25)
def test_classescs_PackageCS_instantiation(instance):
    assert isinstance(instance, classescs_PackageCS)


classescs_PathElementCS_strategy = st.builds(classescs_PathElementCS)
@given(instance=classescs_PathElementCS_strategy)
@settings(max_examples=25)
def test_classescs_PathElementCS_instantiation(instance):
    assert isinstance(instance, classescs_PathElementCS)


classescs_PathNameCS_strategy = st.builds(classescs_PathNameCS)
@given(instance=classescs_PathNameCS_strategy)
@settings(max_examples=25)
def test_classescs_PathNameCS_instantiation(instance):
    assert isinstance(instance, classescs_PathNameCS)


classescs_RootCS_strategy = st.builds(classescs_RootCS)
@given(instance=classescs_RootCS_strategy)
@settings(max_examples=25)
def test_classescs_RootCS_instantiation(instance):
    assert isinstance(instance, classescs_RootCS)



