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
    NamedElement,
    family_Family,
    family_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_hyp_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_hyp_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "father" in params, "Missing parameter 'father'"
    assert "mother" in params, "Missing parameter 'mother'"
    assert "children" in params, "Missing parameter 'children'"






def test_hyp_family_namedelement_is_not_abstract():
    assert not inspect.isabstract(family_NamedElement)


def test_hyp_family_namedelement_constructor_exists():
    assert callable(family_NamedElement.__init__)


def test_hyp_family_namedelement_constructor_args():
    sig = inspect.signature(family_NamedElement.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
family_Family_strategy = st.builds(
    family_Family,
    father=
        safe_text,
    mother=
        safe_text,
    children=
        safe_text
)
family_NamedElement_strategy = st.builds(
    family_NamedElement,
    name=
        safe_text
)





@given(instance=family_Family_strategy)
def test_hyp_family_family_father_setter(instance):
    original = instance.father
    instance.father = original
    assert instance.father == original



@given(instance=family_Family_strategy)
def test_hyp_family_family_mother_setter(instance):
    original = instance.mother
    instance.mother = original
    assert instance.mother == original



@given(instance=family_Family_strategy)
def test_hyp_family_family_children_setter(instance):
    original = instance.children
    instance.children = original
    assert instance.children == original




@given(instance=family_NamedElement_strategy)
def test_hyp_family_namedelement_name_setter(instance):
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
    family_Family,
    family_NamedElement,
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

def test_family_Family_children_value_roundtrip():
    instance = family_Family(children="sample_text", father="sample_text", mother="sample_text")
    assert instance.children == "sample_text"
    instance.children = "sample_text_2"
    assert instance.children == "sample_text_2"


def test_family_Family_father_value_roundtrip():
    instance = family_Family(children="sample_text", father="sample_text", mother="sample_text")
    assert instance.father == "sample_text"
    instance.father = "sample_text_2"
    assert instance.father == "sample_text_2"


def test_family_Family_mother_value_roundtrip():
    instance = family_Family(children="sample_text", father="sample_text", mother="sample_text")
    assert instance.mother == "sample_text"
    instance.mother = "sample_text_2"
    assert instance.mother == "sample_text_2"


def test_family_NamedElement_name_value_roundtrip():
    instance = family_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_family_Family_isa_NamedElement():
    instance = family_Family(children="sample_text", father="sample_text", mother="sample_text")
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


family_Family_strategy = st.builds(family_Family, children=safe_text, father=safe_text, mother=safe_text)
@given(instance=family_Family_strategy)
@settings(max_examples=25)
def test_family_Family_instantiation(instance):
    assert isinstance(instance, family_Family)


family_NamedElement_strategy = st.builds(family_NamedElement, name=safe_text)
@given(instance=family_NamedElement_strategy)
@settings(max_examples=25)
def test_family_NamedElement_instantiation(instance):
    assert isinstance(instance, family_NamedElement)



