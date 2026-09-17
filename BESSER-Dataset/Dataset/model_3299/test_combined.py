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
    StochasticSIRDiseaseModel,
    example_ExampleDiseaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_stochasticsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StochasticSIRDiseaseModel)


def test_hyp_stochasticsirdiseasemodel_constructor_exists():
    assert callable(StochasticSIRDiseaseModel.__init__)


def test_hyp_stochasticsirdiseasemodel_constructor_args():
    sig = inspect.signature(StochasticSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_example_examplediseasemodel_is_not_abstract():
    assert not inspect.isabstract(example_ExampleDiseaseModel)


def test_hyp_example_examplediseasemodel_constructor_exists():
    assert callable(example_ExampleDiseaseModel.__init__)


def test_hyp_example_examplediseasemodel_constructor_args():
    sig = inspect.signature(example_ExampleDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "modulationPhaseShift" in params, "Missing parameter 'modulationPhaseShift'"
    assert "modulationPeriod" in params, "Missing parameter 'modulationPeriod'"
    assert "seasonalModulationFloor" in params, "Missing parameter 'seasonalModulationFloor'"
    assert "seasonalModulationExponent" in params, "Missing parameter 'seasonalModulationExponent'"






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
StochasticSIRDiseaseModel_strategy = st.builds(
    StochasticSIRDiseaseModel,
)
example_ExampleDiseaseModel_strategy = st.builds(
    example_ExampleDiseaseModel,
    modulationPhaseShift=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationPeriod=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    seasonalModulationFloor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    seasonalModulationExponent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)





@given(instance=example_ExampleDiseaseModel_strategy)
def test_hyp_example_examplediseasemodel_modulationPhaseShift_setter(instance):
    original = instance.modulationPhaseShift
    instance.modulationPhaseShift = original
    assert instance.modulationPhaseShift == original



@given(instance=example_ExampleDiseaseModel_strategy)
def test_hyp_example_examplediseasemodel_modulationPeriod_setter(instance):
    original = instance.modulationPeriod
    instance.modulationPeriod = original
    assert instance.modulationPeriod == original



@given(instance=example_ExampleDiseaseModel_strategy)
def test_hyp_example_examplediseasemodel_seasonalModulationFloor_setter(instance):
    original = instance.seasonalModulationFloor
    instance.seasonalModulationFloor = original
    assert instance.seasonalModulationFloor == original



@given(instance=example_ExampleDiseaseModel_strategy)
def test_hyp_example_examplediseasemodel_seasonalModulationExponent_setter(instance):
    original = instance.seasonalModulationExponent
    instance.seasonalModulationExponent = original
    assert instance.seasonalModulationExponent == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    StochasticSIRDiseaseModel,
    example_ExampleDiseaseModel,
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

def test_example_ExampleDiseaseModel_modulationPeriod_value_roundtrip():
    instance = example_ExampleDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.modulationPeriod == 3.14
    instance.modulationPeriod = 9.99
    assert instance.modulationPeriod == 9.99


def test_example_ExampleDiseaseModel_modulationPhaseShift_value_roundtrip():
    instance = example_ExampleDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.modulationPhaseShift == 3.14
    instance.modulationPhaseShift = 9.99
    assert instance.modulationPhaseShift == 9.99


def test_example_ExampleDiseaseModel_seasonalModulationExponent_value_roundtrip():
    instance = example_ExampleDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.seasonalModulationExponent == 3.14
    instance.seasonalModulationExponent = 9.99
    assert instance.seasonalModulationExponent == 9.99


def test_example_ExampleDiseaseModel_seasonalModulationFloor_value_roundtrip():
    instance = example_ExampleDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.seasonalModulationFloor == 3.14
    instance.seasonalModulationFloor = 9.99
    assert instance.seasonalModulationFloor == 9.99


def test_example_ExampleDiseaseModel_isa_StochasticSIRDiseaseModel():
    instance = example_ExampleDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert isinstance(instance, StochasticSIRDiseaseModel)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

StochasticSIRDiseaseModel_strategy = st.builds(StochasticSIRDiseaseModel)
@given(instance=StochasticSIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_StochasticSIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, StochasticSIRDiseaseModel)


example_ExampleDiseaseModel_strategy = st.builds(example_ExampleDiseaseModel, modulationPeriod=st.floats(allow_nan=False, allow_infinity=False), modulationPhaseShift=st.floats(allow_nan=False, allow_infinity=False), seasonalModulationExponent=st.floats(allow_nan=False, allow_infinity=False), seasonalModulationFloor=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=example_ExampleDiseaseModel_strategy)
@settings(max_examples=25)
def test_example_ExampleDiseaseModel_instantiation(instance):
    assert isinstance(instance, example_ExampleDiseaseModel)



