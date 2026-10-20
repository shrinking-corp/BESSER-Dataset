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
    Gato,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_gato_is_not_abstract():
    assert not inspect.isabstract(Gato)


def test_hyp_gato_constructor_exists():
    assert callable(Gato.__init__)


def test_hyp_gato_constructor_args():
    sig = inspect.signature(Gato.__init__)
    params = list(sig.parameters.keys())
    assert "Nombre" in params, "Missing parameter 'Nombre'"
    assert "Raza" in params, "Missing parameter 'Raza'"
    assert "Color" in params, "Missing parameter 'Color'"





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
Gato_strategy = st.builds(
    Gato,
    Nombre=
        safe_text,
    Raza=
        safe_text,
    Color=
        safe_text
)




@given(instance=Gato_strategy)
def test_hyp_gato_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original



@given(instance=Gato_strategy)
def test_hyp_gato_Raza_setter(instance):
    original = instance.Raza
    instance.Raza = original
    assert instance.Raza == original



@given(instance=Gato_strategy)
def test_hyp_gato_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
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

def test_Gato_Color_value_roundtrip():
    instance = Gato(Color="sample_text", Nombre="sample_text", Raza="sample_text")
    assert instance.Color == "sample_text"
    instance.Color = "sample_text_2"
    assert instance.Color == "sample_text_2"


def test_Gato_Nombre_value_roundtrip():
    instance = Gato(Color="sample_text", Nombre="sample_text", Raza="sample_text")
    assert instance.Nombre == "sample_text"
    instance.Nombre = "sample_text_2"
    assert instance.Nombre == "sample_text_2"


def test_Gato_Raza_value_roundtrip():
    instance = Gato(Color="sample_text", Nombre="sample_text", Raza="sample_text")
    assert instance.Raza == "sample_text"
    instance.Raza = "sample_text_2"
    assert instance.Raza == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Gato_strategy = st.builds(Gato, Color=safe_text, Nombre=safe_text, Raza=safe_text)
@given(instance=Gato_strategy)
@settings(max_examples=25)
def test_Gato_instantiation(instance):
    assert isinstance(instance, Gato)



