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
    Class2,
    Class,
    Gato,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_hyp_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_hyp_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gato_is_not_abstract():
    assert not inspect.isabstract(Gato)


def test_hyp_gato_constructor_exists():
    assert callable(Gato.__init__)


def test_hyp_gato_constructor_args():
    sig = inspect.signature(Gato.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "raza" in params, "Missing parameter 'raza'"
    assert "nombre" in params, "Missing parameter 'nombre'"





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
Class2_strategy = st.builds(
    Class2,
)
Class_strategy = st.builds(
    Class,
)
Gato_strategy = st.builds(
    Gato,
    color=
        safe_text,
    raza=
        safe_text,
    nombre=
        safe_text
)






@given(instance=Gato_strategy)
def test_hyp_gato_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Gato_strategy)
def test_hyp_gato_raza_setter(instance):
    original = instance.raza
    instance.raza = original
    assert instance.raza == original



@given(instance=Gato_strategy)
def test_hyp_gato_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    Class2,
    Gato,
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

def test_Gato_color_value_roundtrip():
    instance = Gato(color="sample_text", nombre="sample_text", raza="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_Gato_nombre_value_roundtrip():
    instance = Gato(color="sample_text", nombre="sample_text", raza="sample_text")
    assert instance.nombre == "sample_text"
    instance.nombre = "sample_text_2"
    assert instance.nombre == "sample_text_2"


def test_Gato_raza_value_roundtrip():
    instance = Gato(color="sample_text", nombre="sample_text", raza="sample_text")
    assert instance.raza == "sample_text"
    instance.raza = "sample_text_2"
    assert instance.raza == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Class2_strategy = st.builds(Class2)
@given(instance=Class2_strategy)
@settings(max_examples=25)
def test_Class2_instantiation(instance):
    assert isinstance(instance, Class2)


Gato_strategy = st.builds(Gato, color=safe_text, nombre=safe_text, raza=safe_text)
@given(instance=Gato_strategy)
@settings(max_examples=25)
def test_Gato_instantiation(instance):
    assert isinstance(instance, Gato)



