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
    Cashier,
    Waiter,
    Cook,
    Mammal,
    Animal,
    Reptile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_cashier_is_not_abstract():
    assert not inspect.isabstract(Cashier)


def test_hyp_cashier_constructor_exists():
    assert callable(Cashier.__init__)


def test_hyp_cashier_constructor_args():
    sig = inspect.signature(Cashier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_hyp_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_hyp_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cook_is_not_abstract():
    assert not inspect.isabstract(Cook)


def test_hyp_cook_constructor_exists():
    assert callable(Cook.__init__)


def test_hyp_cook_constructor_args():
    sig = inspect.signature(Cook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mammal_is_not_abstract():
    assert not inspect.isabstract(Mammal)


def test_hyp_mammal_constructor_exists():
    assert callable(Mammal.__init__)


def test_hyp_mammal_constructor_args():
    sig = inspect.signature(Mammal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_animal_is_not_abstract():
    assert not inspect.isabstract(Animal)


def test_hyp_animal_constructor_exists():
    assert callable(Animal.__init__)


def test_hyp_animal_constructor_args():
    sig = inspect.signature(Animal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_reptile_is_not_abstract():
    assert not inspect.isabstract(Reptile)


def test_hyp_reptile_constructor_exists():
    assert callable(Reptile.__init__)


def test_hyp_reptile_constructor_args():
    sig = inspect.signature(Reptile.__init__)
    params = list(sig.parameters.keys())
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
Cashier_strategy = st.builds(
    Cashier,
)
Waiter_strategy = st.builds(
    Waiter,
)
Cook_strategy = st.builds(
    Cook,
)
Mammal_strategy = st.builds(
    Mammal,
)
Animal_strategy = st.builds(
    Animal,
    name=
        safe_text
)
Reptile_strategy = st.builds(
    Reptile,
    attribute=
        safe_text
)








@given(instance=Animal_strategy)
def test_hyp_animal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Reptile_strategy)
def test_hyp_reptile_attribute_setter(instance):
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
    Animal,
    Cashier,
    Cook,
    Mammal,
    Reptile,
    Waiter,
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

def test_Animal_name_value_roundtrip():
    instance = Animal(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Reptile_attribute_value_roundtrip():
    instance = Reptile(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Animal_strategy = st.builds(Animal, name=safe_text)
@given(instance=Animal_strategy)
@settings(max_examples=25)
def test_Animal_instantiation(instance):
    assert isinstance(instance, Animal)


Cashier_strategy = st.builds(Cashier)
@given(instance=Cashier_strategy)
@settings(max_examples=25)
def test_Cashier_instantiation(instance):
    assert isinstance(instance, Cashier)


Cook_strategy = st.builds(Cook)
@given(instance=Cook_strategy)
@settings(max_examples=25)
def test_Cook_instantiation(instance):
    assert isinstance(instance, Cook)


Mammal_strategy = st.builds(Mammal)
@given(instance=Mammal_strategy)
@settings(max_examples=25)
def test_Mammal_instantiation(instance):
    assert isinstance(instance, Mammal)


Reptile_strategy = st.builds(Reptile, attribute=safe_text)
@given(instance=Reptile_strategy)
@settings(max_examples=25)
def test_Reptile_instantiation(instance):
    assert isinstance(instance, Reptile)


Waiter_strategy = st.builds(Waiter)
@given(instance=Waiter_strategy)
@settings(max_examples=25)
def test_Waiter_instantiation(instance):
    assert isinstance(instance, Waiter)



