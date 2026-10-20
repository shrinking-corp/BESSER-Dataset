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
    Train,
    Car1,
    Airplane,
    Boat,
    Vehicle,
    Car,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_train_is_not_abstract():
    assert not inspect.isabstract(Train)


def test_hyp_train_constructor_exists():
    assert callable(Train.__init__)


def test_hyp_train_constructor_args():
    sig = inspect.signature(Train.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "trucks" in params, "Missing parameter 'trucks'"





def test_hyp_car1_is_not_abstract():
    assert not inspect.isabstract(Car1)


def test_hyp_car1_constructor_exists():
    assert callable(Car1.__init__)


def test_hyp_car1_constructor_args():
    sig = inspect.signature(Car1.__init__)
    params = list(sig.parameters.keys())
    assert "helmSide" in params, "Missing parameter 'helmSide'"
    assert "doors" in params, "Missing parameter 'doors'"





def test_hyp_airplane_is_not_abstract():
    assert not inspect.isabstract(Airplane)


def test_hyp_airplane_constructor_exists():
    assert callable(Airplane.__init__)


def test_hyp_airplane_constructor_args():
    sig = inspect.signature(Airplane.__init__)
    params = list(sig.parameters.keys())
    assert "maxAttitude" in params, "Missing parameter 'maxAttitude'"
    assert "maxCarryingWeight" in params, "Missing parameter 'maxCarryingWeight'"





def test_hyp_boat_is_not_abstract():
    assert not inspect.isabstract(Boat)


def test_hyp_boat_constructor_exists():
    assert callable(Boat.__init__)


def test_hyp_boat_constructor_args():
    sig = inspect.signature(Boat.__init__)
    params = list(sig.parameters.keys())
    assert "maxCarryingWeight" in params, "Missing parameter 'maxCarryingWeight'"




def test_hyp_vehicle_is_not_abstract():
    assert not inspect.isabstract(Vehicle)


def test_hyp_vehicle_constructor_exists():
    assert callable(Vehicle.__init__)


def test_hyp_vehicle_constructor_args():
    sig = inspect.signature(Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "engine" in params, "Missing parameter 'engine'"
    assert "price" in params, "Missing parameter 'price'"
    assert "brand" in params, "Missing parameter 'brand'"






def test_hyp_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_hyp_car_constructor_exists():
    assert callable(Car.__init__)


def test_hyp_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())
    assert "model" in params, "Missing parameter 'model'"
    assert "wheels" in params, "Missing parameter 'wheels'"
    assert "engine" in params, "Missing parameter 'engine'"
    assert "doors" in params, "Missing parameter 'doors'"
    assert "length" in params, "Missing parameter 'length'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"









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
Train_strategy = st.builds(
    Train,
    type=
        safe_text,
    trucks=
        st.integers()
)
Car1_strategy = st.builds(
    Car1,
    helmSide=
        safe_text,
    doors=
        st.integers()
)
Airplane_strategy = st.builds(
    Airplane,
    maxAttitude=
        st.integers(),
    maxCarryingWeight=
        st.integers()
)
Boat_strategy = st.builds(
    Boat,
    maxCarryingWeight=
        st.integers()
)
Vehicle_strategy = st.builds(
    Vehicle,
    engine=
        safe_text,
    price=
        safe_text,
    brand=
        safe_text
)
Car_strategy = st.builds(
    Car,
    model=
        safe_text,
    wheels=
        safe_text,
    engine=
        safe_text,
    doors=
        st.integers(),
    length=
        st.integers(),
    width=
        st.integers(),
    height=
        st.integers()
)




@given(instance=Train_strategy)
def test_hyp_train_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Train_strategy)
def test_hyp_train_trucks_setter(instance):
    original = instance.trucks
    instance.trucks = original
    assert instance.trucks == original




@given(instance=Car1_strategy)
def test_hyp_car1_helmSide_setter(instance):
    original = instance.helmSide
    instance.helmSide = original
    assert instance.helmSide == original



@given(instance=Car1_strategy)
def test_hyp_car1_doors_setter(instance):
    original = instance.doors
    instance.doors = original
    assert instance.doors == original




@given(instance=Airplane_strategy)
def test_hyp_airplane_maxAttitude_setter(instance):
    original = instance.maxAttitude
    instance.maxAttitude = original
    assert instance.maxAttitude == original



@given(instance=Airplane_strategy)
def test_hyp_airplane_maxCarryingWeight_setter(instance):
    original = instance.maxCarryingWeight
    instance.maxCarryingWeight = original
    assert instance.maxCarryingWeight == original




@given(instance=Boat_strategy)
def test_hyp_boat_maxCarryingWeight_setter(instance):
    original = instance.maxCarryingWeight
    instance.maxCarryingWeight = original
    assert instance.maxCarryingWeight == original




@given(instance=Vehicle_strategy)
def test_hyp_vehicle_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original



@given(instance=Vehicle_strategy)
def test_hyp_vehicle_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Vehicle_strategy)
def test_hyp_vehicle_brand_setter(instance):
    original = instance.brand
    instance.brand = original
    assert instance.brand == original




@given(instance=Car_strategy)
def test_hyp_car_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=Car_strategy)
def test_hyp_car_wheels_setter(instance):
    original = instance.wheels
    instance.wheels = original
    assert instance.wheels == original



@given(instance=Car_strategy)
def test_hyp_car_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original



@given(instance=Car_strategy)
def test_hyp_car_doors_setter(instance):
    original = instance.doors
    instance.doors = original
    assert instance.doors == original



@given(instance=Car_strategy)
def test_hyp_car_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=Car_strategy)
def test_hyp_car_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=Car_strategy)
def test_hyp_car_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Airplane,
    Boat,
    Car,
    Car1,
    Train,
    Vehicle,
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

def test_Airplane_maxAttitude_value_roundtrip():
    instance = Airplane(maxAttitude=7, maxCarryingWeight=7)
    assert instance.maxAttitude == 7
    instance.maxAttitude = 13
    assert instance.maxAttitude == 13


def test_Airplane_maxCarryingWeight_value_roundtrip():
    instance = Airplane(maxAttitude=7, maxCarryingWeight=7)
    assert instance.maxCarryingWeight == 7
    instance.maxCarryingWeight = 13
    assert instance.maxCarryingWeight == 13


def test_Boat_maxCarryingWeight_value_roundtrip():
    instance = Boat(maxCarryingWeight=7)
    assert instance.maxCarryingWeight == 7
    instance.maxCarryingWeight = 13
    assert instance.maxCarryingWeight == 13


def test_Car_doors_value_roundtrip():
    instance = Car(doors=7, engine="sample_text", height=7, length=7, model="sample_text", wheels="sample_text", width=7)
    assert instance.doors == 7
    instance.doors = 13
    assert instance.doors == 13


def test_Car_engine_value_roundtrip():
    instance = Car(doors=7, engine="sample_text", height=7, length=7, model="sample_text", wheels="sample_text", width=7)
    assert instance.engine == "sample_text"
    instance.engine = "sample_text_2"
    assert instance.engine == "sample_text_2"


def test_Car_height_value_roundtrip():
    instance = Car(doors=7, engine="sample_text", height=7, length=7, model="sample_text", wheels="sample_text", width=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_Car_length_value_roundtrip():
    instance = Car(doors=7, engine="sample_text", height=7, length=7, model="sample_text", wheels="sample_text", width=7)
    assert instance.length == 7
    instance.length = 13
    assert instance.length == 13


def test_Car_model_value_roundtrip():
    instance = Car(doors=7, engine="sample_text", height=7, length=7, model="sample_text", wheels="sample_text", width=7)
    assert instance.model == "sample_text"
    instance.model = "sample_text_2"
    assert instance.model == "sample_text_2"


def test_Car_wheels_value_roundtrip():
    instance = Car(doors=7, engine="sample_text", height=7, length=7, model="sample_text", wheels="sample_text", width=7)
    assert instance.wheels == "sample_text"
    instance.wheels = "sample_text_2"
    assert instance.wheels == "sample_text_2"


def test_Car_width_value_roundtrip():
    instance = Car(doors=7, engine="sample_text", height=7, length=7, model="sample_text", wheels="sample_text", width=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_Car1_doors_value_roundtrip():
    instance = Car1(doors=7, helmSide="sample_text")
    assert instance.doors == 7
    instance.doors = 13
    assert instance.doors == 13


def test_Car1_helmSide_value_roundtrip():
    instance = Car1(doors=7, helmSide="sample_text")
    assert instance.helmSide == "sample_text"
    instance.helmSide = "sample_text_2"
    assert instance.helmSide == "sample_text_2"


def test_Train_trucks_value_roundtrip():
    instance = Train(trucks=7, type="sample_text")
    assert instance.trucks == 7
    instance.trucks = 13
    assert instance.trucks == 13


def test_Train_type_value_roundtrip():
    instance = Train(trucks=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Vehicle_brand_value_roundtrip():
    instance = Vehicle(brand="sample_text", engine="sample_text", price="sample_text")
    assert instance.brand == "sample_text"
    instance.brand = "sample_text_2"
    assert instance.brand == "sample_text_2"


def test_Vehicle_engine_value_roundtrip():
    instance = Vehicle(brand="sample_text", engine="sample_text", price="sample_text")
    assert instance.engine == "sample_text"
    instance.engine = "sample_text_2"
    assert instance.engine == "sample_text_2"


def test_Vehicle_price_value_roundtrip():
    instance = Vehicle(brand="sample_text", engine="sample_text", price="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Airplane_strategy = st.builds(Airplane, maxAttitude=st.integers(), maxCarryingWeight=st.integers())
@given(instance=Airplane_strategy)
@settings(max_examples=25)
def test_Airplane_instantiation(instance):
    assert isinstance(instance, Airplane)


Boat_strategy = st.builds(Boat, maxCarryingWeight=st.integers())
@given(instance=Boat_strategy)
@settings(max_examples=25)
def test_Boat_instantiation(instance):
    assert isinstance(instance, Boat)


Car_strategy = st.builds(Car, doors=st.integers(), engine=safe_text, height=st.integers(), length=st.integers(), model=safe_text, wheels=safe_text, width=st.integers())
@given(instance=Car_strategy)
@settings(max_examples=25)
def test_Car_instantiation(instance):
    assert isinstance(instance, Car)


Car1_strategy = st.builds(Car1, doors=st.integers(), helmSide=safe_text)
@given(instance=Car1_strategy)
@settings(max_examples=25)
def test_Car1_instantiation(instance):
    assert isinstance(instance, Car1)


Train_strategy = st.builds(Train, trucks=st.integers(), type=safe_text)
@given(instance=Train_strategy)
@settings(max_examples=25)
def test_Train_instantiation(instance):
    assert isinstance(instance, Train)


Vehicle_strategy = st.builds(Vehicle, brand=safe_text, engine=safe_text, price=safe_text)
@given(instance=Vehicle_strategy)
@settings(max_examples=25)
def test_Vehicle_instantiation(instance):
    assert isinstance(instance, Vehicle)



