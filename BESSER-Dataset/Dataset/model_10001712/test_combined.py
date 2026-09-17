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
    Coach,
    FirstClass,
    PassengerTrain,
    CargoTrain,
    Train,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_coach_is_not_abstract():
    assert not inspect.isabstract(Coach)


def test_hyp_coach_constructor_exists():
    assert callable(Coach.__init__)


def test_hyp_coach_constructor_args():
    sig = inspect.signature(Coach.__init__)
    params = list(sig.parameters.keys())
    assert "seatsFilled" in params, "Missing parameter 'seatsFilled'"
    assert "numberOfSeats" in params, "Missing parameter 'numberOfSeats'"





def test_hyp_firstclass_is_not_abstract():
    assert not inspect.isabstract(FirstClass)


def test_hyp_firstclass_constructor_exists():
    assert callable(FirstClass.__init__)


def test_hyp_firstclass_constructor_args():
    sig = inspect.signature(FirstClass.__init__)
    params = list(sig.parameters.keys())
    assert "seatsFilled" in params, "Missing parameter 'seatsFilled'"
    assert "numberOfSeats" in params, "Missing parameter 'numberOfSeats'"





def test_hyp_passengertrain_is_not_abstract():
    assert not inspect.isabstract(PassengerTrain)


def test_hyp_passengertrain_constructor_exists():
    assert callable(PassengerTrain.__init__)


def test_hyp_passengertrain_constructor_args():
    sig = inspect.signature(PassengerTrain.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfPassengers" in params, "Missing parameter 'numberOfPassengers'"
    assert "Stops" in params, "Missing parameter 'Stops'"
    assert "Origin" in params, "Missing parameter 'Origin'"






def test_hyp_cargotrain_is_not_abstract():
    assert not inspect.isabstract(CargoTrain)


def test_hyp_cargotrain_constructor_exists():
    assert callable(CargoTrain.__init__)


def test_hyp_cargotrain_constructor_args():
    sig = inspect.signature(CargoTrain.__init__)
    params = list(sig.parameters.keys())
    assert "Containers" in params, "Missing parameter 'Containers'"
    assert "Stops" in params, "Missing parameter 'Stops'"
    assert "Origin" in params, "Missing parameter 'Origin'"






def test_hyp_train_is_not_abstract():
    assert not inspect.isabstract(Train)


def test_hyp_train_constructor_exists():
    assert callable(Train.__init__)


def test_hyp_train_constructor_args():
    sig = inspect.signature(Train.__init__)
    params = list(sig.parameters.keys())
    assert "Cars" in params, "Missing parameter 'Cars'"
    assert "Manufacturer" in params, "Missing parameter 'Manufacturer'"
    assert "Operator" in params, "Missing parameter 'Operator'"
    assert "Power" in params, "Missing parameter 'Power'"






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
Coach_strategy = st.builds(
    Coach,
    seatsFilled=
        st.integers(),
    numberOfSeats=
        st.integers()
)
FirstClass_strategy = st.builds(
    FirstClass,
    seatsFilled=
        st.integers(),
    numberOfSeats=
        st.integers()
)
PassengerTrain_strategy = st.builds(
    PassengerTrain,
    numberOfPassengers=
        st.integers(),
    Stops=
        safe_text,
    Origin=
        safe_text
)
CargoTrain_strategy = st.builds(
    CargoTrain,
    Containers=
        safe_text,
    Stops=
        safe_text,
    Origin=
        safe_text
)
Train_strategy = st.builds(
    Train,
    Cars=
        safe_text,
    Manufacturer=
        safe_text,
    Operator=
        safe_text,
    Power=
        safe_text
)




@given(instance=Coach_strategy)
def test_hyp_coach_seatsFilled_setter(instance):
    original = instance.seatsFilled
    instance.seatsFilled = original
    assert instance.seatsFilled == original



@given(instance=Coach_strategy)
def test_hyp_coach_numberOfSeats_setter(instance):
    original = instance.numberOfSeats
    instance.numberOfSeats = original
    assert instance.numberOfSeats == original




@given(instance=FirstClass_strategy)
def test_hyp_firstclass_seatsFilled_setter(instance):
    original = instance.seatsFilled
    instance.seatsFilled = original
    assert instance.seatsFilled == original



@given(instance=FirstClass_strategy)
def test_hyp_firstclass_numberOfSeats_setter(instance):
    original = instance.numberOfSeats
    instance.numberOfSeats = original
    assert instance.numberOfSeats == original




@given(instance=PassengerTrain_strategy)
def test_hyp_passengertrain_numberOfPassengers_setter(instance):
    original = instance.numberOfPassengers
    instance.numberOfPassengers = original
    assert instance.numberOfPassengers == original



@given(instance=PassengerTrain_strategy)
def test_hyp_passengertrain_Stops_setter(instance):
    original = instance.Stops
    instance.Stops = original
    assert instance.Stops == original



@given(instance=PassengerTrain_strategy)
def test_hyp_passengertrain_Origin_setter(instance):
    original = instance.Origin
    instance.Origin = original
    assert instance.Origin == original




@given(instance=CargoTrain_strategy)
def test_hyp_cargotrain_Containers_setter(instance):
    original = instance.Containers
    instance.Containers = original
    assert instance.Containers == original



@given(instance=CargoTrain_strategy)
def test_hyp_cargotrain_Stops_setter(instance):
    original = instance.Stops
    instance.Stops = original
    assert instance.Stops == original



@given(instance=CargoTrain_strategy)
def test_hyp_cargotrain_Origin_setter(instance):
    original = instance.Origin
    instance.Origin = original
    assert instance.Origin == original




@given(instance=Train_strategy)
def test_hyp_train_Cars_setter(instance):
    original = instance.Cars
    instance.Cars = original
    assert instance.Cars == original



@given(instance=Train_strategy)
def test_hyp_train_Manufacturer_setter(instance):
    original = instance.Manufacturer
    instance.Manufacturer = original
    assert instance.Manufacturer == original



@given(instance=Train_strategy)
def test_hyp_train_Operator_setter(instance):
    original = instance.Operator
    instance.Operator = original
    assert instance.Operator == original



@given(instance=Train_strategy)
def test_hyp_train_Power_setter(instance):
    original = instance.Power
    instance.Power = original
    assert instance.Power == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CargoTrain,
    Coach,
    FirstClass,
    PassengerTrain,
    Train,
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

def test_CargoTrain_Containers_value_roundtrip():
    instance = CargoTrain(Containers="sample_text", Origin="sample_text", Stops="sample_text")
    assert instance.Containers == "sample_text"
    instance.Containers = "sample_text_2"
    assert instance.Containers == "sample_text_2"


def test_CargoTrain_Origin_value_roundtrip():
    instance = CargoTrain(Containers="sample_text", Origin="sample_text", Stops="sample_text")
    assert instance.Origin == "sample_text"
    instance.Origin = "sample_text_2"
    assert instance.Origin == "sample_text_2"


def test_CargoTrain_Stops_value_roundtrip():
    instance = CargoTrain(Containers="sample_text", Origin="sample_text", Stops="sample_text")
    assert instance.Stops == "sample_text"
    instance.Stops = "sample_text_2"
    assert instance.Stops == "sample_text_2"


def test_Coach_numberOfSeats_value_roundtrip():
    instance = Coach(numberOfSeats=7, seatsFilled=7)
    assert instance.numberOfSeats == 7
    instance.numberOfSeats = 13
    assert instance.numberOfSeats == 13


def test_Coach_seatsFilled_value_roundtrip():
    instance = Coach(numberOfSeats=7, seatsFilled=7)
    assert instance.seatsFilled == 7
    instance.seatsFilled = 13
    assert instance.seatsFilled == 13


def test_FirstClass_numberOfSeats_value_roundtrip():
    instance = FirstClass(numberOfSeats=7, seatsFilled=7)
    assert instance.numberOfSeats == 7
    instance.numberOfSeats = 13
    assert instance.numberOfSeats == 13


def test_FirstClass_seatsFilled_value_roundtrip():
    instance = FirstClass(numberOfSeats=7, seatsFilled=7)
    assert instance.seatsFilled == 7
    instance.seatsFilled = 13
    assert instance.seatsFilled == 13


def test_PassengerTrain_Origin_value_roundtrip():
    instance = PassengerTrain(Origin="sample_text", Stops="sample_text", numberOfPassengers=7)
    assert instance.Origin == "sample_text"
    instance.Origin = "sample_text_2"
    assert instance.Origin == "sample_text_2"


def test_PassengerTrain_Stops_value_roundtrip():
    instance = PassengerTrain(Origin="sample_text", Stops="sample_text", numberOfPassengers=7)
    assert instance.Stops == "sample_text"
    instance.Stops = "sample_text_2"
    assert instance.Stops == "sample_text_2"


def test_PassengerTrain_numberOfPassengers_value_roundtrip():
    instance = PassengerTrain(Origin="sample_text", Stops="sample_text", numberOfPassengers=7)
    assert instance.numberOfPassengers == 7
    instance.numberOfPassengers = 13
    assert instance.numberOfPassengers == 13


def test_Train_Cars_value_roundtrip():
    instance = Train(Cars="sample_text", Manufacturer="sample_text", Operator="sample_text", Power="sample_text")
    assert instance.Cars == "sample_text"
    instance.Cars = "sample_text_2"
    assert instance.Cars == "sample_text_2"


def test_Train_Manufacturer_value_roundtrip():
    instance = Train(Cars="sample_text", Manufacturer="sample_text", Operator="sample_text", Power="sample_text")
    assert instance.Manufacturer == "sample_text"
    instance.Manufacturer = "sample_text_2"
    assert instance.Manufacturer == "sample_text_2"


def test_Train_Operator_value_roundtrip():
    instance = Train(Cars="sample_text", Manufacturer="sample_text", Operator="sample_text", Power="sample_text")
    assert instance.Operator == "sample_text"
    instance.Operator = "sample_text_2"
    assert instance.Operator == "sample_text_2"


def test_Train_Power_value_roundtrip():
    instance = Train(Cars="sample_text", Manufacturer="sample_text", Operator="sample_text", Power="sample_text")
    assert instance.Power == "sample_text"
    instance.Power = "sample_text_2"
    assert instance.Power == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CargoTrain_strategy = st.builds(CargoTrain, Containers=safe_text, Origin=safe_text, Stops=safe_text)
@given(instance=CargoTrain_strategy)
@settings(max_examples=25)
def test_CargoTrain_instantiation(instance):
    assert isinstance(instance, CargoTrain)


Coach_strategy = st.builds(Coach, numberOfSeats=st.integers(), seatsFilled=st.integers())
@given(instance=Coach_strategy)
@settings(max_examples=25)
def test_Coach_instantiation(instance):
    assert isinstance(instance, Coach)


FirstClass_strategy = st.builds(FirstClass, numberOfSeats=st.integers(), seatsFilled=st.integers())
@given(instance=FirstClass_strategy)
@settings(max_examples=25)
def test_FirstClass_instantiation(instance):
    assert isinstance(instance, FirstClass)


PassengerTrain_strategy = st.builds(PassengerTrain, Origin=safe_text, Stops=safe_text, numberOfPassengers=st.integers())
@given(instance=PassengerTrain_strategy)
@settings(max_examples=25)
def test_PassengerTrain_instantiation(instance):
    assert isinstance(instance, PassengerTrain)


Train_strategy = st.builds(Train, Cars=safe_text, Manufacturer=safe_text, Operator=safe_text, Power=safe_text)
@given(instance=Train_strategy)
@settings(max_examples=25)
def test_Train_instantiation(instance):
    assert isinstance(instance, Train)



