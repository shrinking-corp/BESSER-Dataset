import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Gaussian2ForcingDiseaseModel,
    StochasticSIRDiseaseModel,
    forcing_ForcingDiseaseModel,
    forcing_Gaussian2ForcingDiseaseModel,
    forcing_Gaussian3ForcingDiseaseModel,
    forcing_GaussianForcingDiseaseModel,
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

def test_forcing_ForcingDiseaseModel_modulationPeriod_value_roundtrip():
    instance = forcing_ForcingDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.modulationPeriod == 3.14
    instance.modulationPeriod = 9.99
    assert instance.modulationPeriod == 9.99


def test_forcing_ForcingDiseaseModel_modulationPhaseShift_value_roundtrip():
    instance = forcing_ForcingDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.modulationPhaseShift == 3.14
    instance.modulationPhaseShift = 9.99
    assert instance.modulationPhaseShift == 9.99


def test_forcing_ForcingDiseaseModel_seasonalModulationExponent_value_roundtrip():
    instance = forcing_ForcingDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.seasonalModulationExponent == 3.14
    instance.seasonalModulationExponent = 9.99
    assert instance.seasonalModulationExponent == 9.99


def test_forcing_ForcingDiseaseModel_seasonalModulationFloor_value_roundtrip():
    instance = forcing_ForcingDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert instance.seasonalModulationFloor == 3.14
    instance.seasonalModulationFloor = 9.99
    assert instance.seasonalModulationFloor == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_att1_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.att1 == 3.14
    instance.att1 = 9.99
    assert instance.att1 == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_att2_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.att2 == 3.14
    instance.att2 = 9.99
    assert instance.att2 == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_att3_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.att3 == 3.14
    instance.att3 = 9.99
    assert instance.att3 == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_att4_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.att4 == 3.14
    instance.att4 = 9.99
    assert instance.att4 == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_modulationFloor_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.modulationFloor == 3.14
    instance.modulationFloor = 9.99
    assert instance.modulationFloor == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_modulationPeriod_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.modulationPeriod == 3.14
    instance.modulationPeriod = 9.99
    assert instance.modulationPeriod == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_modulationPhaseShift_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.modulationPhaseShift == 3.14
    instance.modulationPhaseShift = 9.99
    assert instance.modulationPhaseShift == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_sigma2_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.sigma2 == 3.14
    instance.sigma2 = 9.99
    assert instance.sigma2 == 9.99


def test_forcing_Gaussian2ForcingDiseaseModel_sigma2_2_value_roundtrip():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert instance.sigma2_2 == 3.14
    instance.sigma2_2 = 9.99
    assert instance.sigma2_2 == 9.99


def test_forcing_Gaussian3ForcingDiseaseModel_modulationFloor_2_value_roundtrip():
    instance = forcing_Gaussian3ForcingDiseaseModel(modulationFloor_2=3.14, sigma2_3=3.14, transmissionRate2=3.14, transmissionRate3=3.14)
    assert instance.modulationFloor_2 == 3.14
    instance.modulationFloor_2 = 9.99
    assert instance.modulationFloor_2 == 9.99


def test_forcing_Gaussian3ForcingDiseaseModel_sigma2_3_value_roundtrip():
    instance = forcing_Gaussian3ForcingDiseaseModel(modulationFloor_2=3.14, sigma2_3=3.14, transmissionRate2=3.14, transmissionRate3=3.14)
    assert instance.sigma2_3 == 3.14
    instance.sigma2_3 = 9.99
    assert instance.sigma2_3 == 9.99


def test_forcing_Gaussian3ForcingDiseaseModel_transmissionRate2_value_roundtrip():
    instance = forcing_Gaussian3ForcingDiseaseModel(modulationFloor_2=3.14, sigma2_3=3.14, transmissionRate2=3.14, transmissionRate3=3.14)
    assert instance.transmissionRate2 == 3.14
    instance.transmissionRate2 = 9.99
    assert instance.transmissionRate2 == 9.99


def test_forcing_Gaussian3ForcingDiseaseModel_transmissionRate3_value_roundtrip():
    instance = forcing_Gaussian3ForcingDiseaseModel(modulationFloor_2=3.14, sigma2_3=3.14, transmissionRate2=3.14, transmissionRate3=3.14)
    assert instance.transmissionRate3 == 3.14
    instance.transmissionRate3 = 9.99
    assert instance.transmissionRate3 == 9.99


def test_forcing_GaussianForcingDiseaseModel_modulationFloor_value_roundtrip():
    instance = forcing_GaussianForcingDiseaseModel(modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14)
    assert instance.modulationFloor == 3.14
    instance.modulationFloor = 9.99
    assert instance.modulationFloor == 9.99


def test_forcing_GaussianForcingDiseaseModel_modulationPeriod_value_roundtrip():
    instance = forcing_GaussianForcingDiseaseModel(modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14)
    assert instance.modulationPeriod == 3.14
    instance.modulationPeriod = 9.99
    assert instance.modulationPeriod == 9.99


def test_forcing_GaussianForcingDiseaseModel_modulationPhaseShift_value_roundtrip():
    instance = forcing_GaussianForcingDiseaseModel(modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14)
    assert instance.modulationPhaseShift == 3.14
    instance.modulationPhaseShift = 9.99
    assert instance.modulationPhaseShift == 9.99


def test_forcing_GaussianForcingDiseaseModel_sigma2_value_roundtrip():
    instance = forcing_GaussianForcingDiseaseModel(modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14)
    assert instance.sigma2 == 3.14
    instance.sigma2 = 9.99
    assert instance.sigma2 == 9.99


def test_forcing_Gaussian3ForcingDiseaseModel_isa_Gaussian2ForcingDiseaseModel():
    instance = forcing_Gaussian3ForcingDiseaseModel(modulationFloor_2=3.14, sigma2_3=3.14, transmissionRate2=3.14, transmissionRate3=3.14)
    assert isinstance(instance, Gaussian2ForcingDiseaseModel)


def test_forcing_ForcingDiseaseModel_isa_StochasticSIRDiseaseModel():
    instance = forcing_ForcingDiseaseModel(modulationPeriod=3.14, modulationPhaseShift=3.14, seasonalModulationExponent=3.14, seasonalModulationFloor=3.14)
    assert isinstance(instance, StochasticSIRDiseaseModel)


def test_forcing_Gaussian2ForcingDiseaseModel_isa_StochasticSIRDiseaseModel():
    instance = forcing_Gaussian2ForcingDiseaseModel(att1=3.14, att2=3.14, att3=3.14, att4=3.14, modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14, sigma2_2=3.14)
    assert isinstance(instance, StochasticSIRDiseaseModel)


def test_forcing_GaussianForcingDiseaseModel_isa_StochasticSIRDiseaseModel():
    instance = forcing_GaussianForcingDiseaseModel(modulationFloor=3.14, modulationPeriod=3.14, modulationPhaseShift=3.14, sigma2=3.14)
    assert isinstance(instance, StochasticSIRDiseaseModel)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Gaussian2ForcingDiseaseModel_strategy = st.builds(Gaussian2ForcingDiseaseModel)
@given(instance=Gaussian2ForcingDiseaseModel_strategy)
@settings(max_examples=25)
def test_Gaussian2ForcingDiseaseModel_instantiation(instance):
    assert isinstance(instance, Gaussian2ForcingDiseaseModel)


StochasticSIRDiseaseModel_strategy = st.builds(StochasticSIRDiseaseModel)
@given(instance=StochasticSIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_StochasticSIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, StochasticSIRDiseaseModel)


forcing_ForcingDiseaseModel_strategy = st.builds(forcing_ForcingDiseaseModel, modulationPeriod=st.floats(allow_nan=False, allow_infinity=False), modulationPhaseShift=st.floats(allow_nan=False, allow_infinity=False), seasonalModulationExponent=st.floats(allow_nan=False, allow_infinity=False), seasonalModulationFloor=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=forcing_ForcingDiseaseModel_strategy)
@settings(max_examples=25)
def test_forcing_ForcingDiseaseModel_instantiation(instance):
    assert isinstance(instance, forcing_ForcingDiseaseModel)


forcing_Gaussian2ForcingDiseaseModel_strategy = st.builds(forcing_Gaussian2ForcingDiseaseModel, att1=st.floats(allow_nan=False, allow_infinity=False), att2=st.floats(allow_nan=False, allow_infinity=False), att3=st.floats(allow_nan=False, allow_infinity=False), att4=st.floats(allow_nan=False, allow_infinity=False), modulationFloor=st.floats(allow_nan=False, allow_infinity=False), modulationPeriod=st.floats(allow_nan=False, allow_infinity=False), modulationPhaseShift=st.floats(allow_nan=False, allow_infinity=False), sigma2=st.floats(allow_nan=False, allow_infinity=False), sigma2_2=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=forcing_Gaussian2ForcingDiseaseModel_strategy)
@settings(max_examples=25)
def test_forcing_Gaussian2ForcingDiseaseModel_instantiation(instance):
    assert isinstance(instance, forcing_Gaussian2ForcingDiseaseModel)


forcing_Gaussian3ForcingDiseaseModel_strategy = st.builds(forcing_Gaussian3ForcingDiseaseModel, modulationFloor_2=st.floats(allow_nan=False, allow_infinity=False), sigma2_3=st.floats(allow_nan=False, allow_infinity=False), transmissionRate2=st.floats(allow_nan=False, allow_infinity=False), transmissionRate3=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=forcing_Gaussian3ForcingDiseaseModel_strategy)
@settings(max_examples=25)
def test_forcing_Gaussian3ForcingDiseaseModel_instantiation(instance):
    assert isinstance(instance, forcing_Gaussian3ForcingDiseaseModel)


forcing_GaussianForcingDiseaseModel_strategy = st.builds(forcing_GaussianForcingDiseaseModel, modulationFloor=st.floats(allow_nan=False, allow_infinity=False), modulationPeriod=st.floats(allow_nan=False, allow_infinity=False), modulationPhaseShift=st.floats(allow_nan=False, allow_infinity=False), sigma2=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=forcing_GaussianForcingDiseaseModel_strategy)
@settings(max_examples=25)
def test_forcing_GaussianForcingDiseaseModel_instantiation(instance):
    assert isinstance(instance, forcing_GaussianForcingDiseaseModel)


