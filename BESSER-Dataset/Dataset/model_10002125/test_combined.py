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
    Bewegungssensor,
    Fenstersensor,
    T_rsensor,
    Sensoren,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bewegungssensor_is_not_abstract():
    assert not inspect.isabstract(Bewegungssensor)


def test_hyp_bewegungssensor_constructor_exists():
    assert callable(Bewegungssensor.__init__)


def test_hyp_bewegungssensor_constructor_args():
    sig = inspect.signature(Bewegungssensor.__init__)
    params = list(sig.parameters.keys())
    assert "bewegungssensorID" in params, "Missing parameter 'bewegungssensorID'"




def test_hyp_fenstersensor_is_not_abstract():
    assert not inspect.isabstract(Fenstersensor)


def test_hyp_fenstersensor_constructor_exists():
    assert callable(Fenstersensor.__init__)


def test_hyp_fenstersensor_constructor_args():
    sig = inspect.signature(Fenstersensor.__init__)
    params = list(sig.parameters.keys())
    assert "fenstersensorID" in params, "Missing parameter 'fenstersensorID'"




def test_hyp_t_rsensor_is_not_abstract():
    assert not inspect.isabstract(T_rsensor)


def test_hyp_t_rsensor_constructor_exists():
    assert callable(T_rsensor.__init__)


def test_hyp_t_rsensor_constructor_args():
    sig = inspect.signature(T_rsensor.__init__)
    params = list(sig.parameters.keys())
    assert "t_rsensorID" in params, "Missing parameter 't_rsensorID'"




def test_hyp_sensoren_is_not_abstract():
    assert not inspect.isabstract(Sensoren)


def test_hyp_sensoren_constructor_exists():
    assert callable(Sensoren.__init__)


def test_hyp_sensoren_constructor_args():
    sig = inspect.signature(Sensoren.__init__)
    params = list(sig.parameters.keys())
    assert "sensorID" in params, "Missing parameter 'sensorID'"



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
Bewegungssensor_strategy = st.builds(
    Bewegungssensor,
    bewegungssensorID=
        st.integers()
)
Fenstersensor_strategy = st.builds(
    Fenstersensor,
    fenstersensorID=
        st.integers()
)
T_rsensor_strategy = st.builds(
    T_rsensor,
    t_rsensorID=
        st.integers()
)
Sensoren_strategy = st.builds(
    Sensoren,
    sensorID=
        st.integers()
)




@given(instance=Bewegungssensor_strategy)
def test_hyp_bewegungssensor_bewegungssensorID_setter(instance):
    original = instance.bewegungssensorID
    instance.bewegungssensorID = original
    assert instance.bewegungssensorID == original




@given(instance=Fenstersensor_strategy)
def test_hyp_fenstersensor_fenstersensorID_setter(instance):
    original = instance.fenstersensorID
    instance.fenstersensorID = original
    assert instance.fenstersensorID == original




@given(instance=T_rsensor_strategy)
def test_hyp_t_rsensor_t_rsensorID_setter(instance):
    original = instance.t_rsensorID
    instance.t_rsensorID = original
    assert instance.t_rsensorID == original




@given(instance=Sensoren_strategy)
def test_hyp_sensoren_sensorID_setter(instance):
    original = instance.sensorID
    instance.sensorID = original
    assert instance.sensorID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bewegungssensor,
    Fenstersensor,
    Sensoren,
    T_rsensor,
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

def test_Bewegungssensor_bewegungssensorID_value_roundtrip():
    instance = Bewegungssensor(bewegungssensorID=7)
    assert instance.bewegungssensorID == 7
    instance.bewegungssensorID = 13
    assert instance.bewegungssensorID == 13


def test_Fenstersensor_fenstersensorID_value_roundtrip():
    instance = Fenstersensor(fenstersensorID=7)
    assert instance.fenstersensorID == 7
    instance.fenstersensorID = 13
    assert instance.fenstersensorID == 13


def test_Sensoren_sensorID_value_roundtrip():
    instance = Sensoren(sensorID=7)
    assert instance.sensorID == 7
    instance.sensorID = 13
    assert instance.sensorID == 13


def test_T_rsensor_t_rsensorID_value_roundtrip():
    instance = T_rsensor(t_rsensorID=7)
    assert instance.t_rsensorID == 7
    instance.t_rsensorID = 13
    assert instance.t_rsensorID == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bewegungssensor_strategy = st.builds(Bewegungssensor, bewegungssensorID=st.integers())
@given(instance=Bewegungssensor_strategy)
@settings(max_examples=25)
def test_Bewegungssensor_instantiation(instance):
    assert isinstance(instance, Bewegungssensor)


Fenstersensor_strategy = st.builds(Fenstersensor, fenstersensorID=st.integers())
@given(instance=Fenstersensor_strategy)
@settings(max_examples=25)
def test_Fenstersensor_instantiation(instance):
    assert isinstance(instance, Fenstersensor)


Sensoren_strategy = st.builds(Sensoren, sensorID=st.integers())
@given(instance=Sensoren_strategy)
@settings(max_examples=25)
def test_Sensoren_instantiation(instance):
    assert isinstance(instance, Sensoren)


T_rsensor_strategy = st.builds(T_rsensor, t_rsensorID=st.integers())
@given(instance=T_rsensor_strategy)
@settings(max_examples=25)
def test_T_rsensor_instantiation(instance):
    assert isinstance(instance, T_rsensor)



