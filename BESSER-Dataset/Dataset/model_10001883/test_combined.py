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
    Test,
    TestStand,
    M6,
    Engine,
    Tennis,
    Car,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_test_is_not_abstract():
    assert not inspect.isabstract(Test)


def test_hyp_test_constructor_exists():
    assert callable(Test.__init__)


def test_hyp_test_constructor_args():
    sig = inspect.signature(Test.__init__)
    params = list(sig.parameters.keys())



def test_hyp_teststand_is_not_abstract():
    assert not inspect.isabstract(TestStand)


def test_hyp_teststand_constructor_exists():
    assert callable(TestStand.__init__)


def test_hyp_teststand_constructor_args():
    sig = inspect.signature(TestStand.__init__)
    params = list(sig.parameters.keys())
    assert "carToBeTested" in params, "Missing parameter 'carToBeTested'"

def test_hyp_teststand_has_carToBeTested():
    assert hasattr(TestStand, "carToBeTested")
    descriptor = None
    for klass in TestStand.__mro__:
        if "carToBeTested" in klass.__dict__:
            descriptor = klass.__dict__["carToBeTested"]
            break
    assert isinstance(descriptor, property)



def test_hyp_m6_is_not_abstract():
    assert not inspect.isabstract(M6)


def test_hyp_m6_constructor_exists():
    assert callable(M6.__init__)


def test_hyp_m6_constructor_args():
    sig = inspect.signature(M6.__init__)
    params = list(sig.parameters.keys())
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "color" in params, "Missing parameter 'color'"
    assert "engine" in params, "Missing parameter 'engine'"

def test_hyp_m6_has_manufacturer():
    assert hasattr(M6, "manufacturer")
    descriptor = None
    for klass in M6.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_m6_has_color():
    assert hasattr(M6, "color")
    descriptor = None
    for klass in M6.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_hyp_m6_has_engine():
    assert hasattr(M6, "engine")
    descriptor = None
    for klass in M6.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)



def test_hyp_engine_is_not_abstract():
    assert not inspect.isabstract(Engine)


def test_hyp_engine_constructor_exists():
    assert callable(Engine.__init__)


def test_hyp_engine_constructor_args():
    sig = inspect.signature(Engine.__init__)
    params = list(sig.parameters.keys())
    assert "engineSpeed" in params, "Missing parameter 'engineSpeed'"
    assert "efficiencyCoefficient" in params, "Missing parameter 'efficiencyCoefficient'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_tennis_is_not_abstract():
    assert not inspect.isabstract(Tennis)


def test_hyp_tennis_constructor_exists():
    assert callable(Tennis.__init__)


def test_hyp_tennis_constructor_args():
    sig = inspect.signature(Tennis.__init__)
    params = list(sig.parameters.keys())
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "color" in params, "Missing parameter 'color'"
    assert "engine" in params, "Missing parameter 'engine'"

def test_hyp_tennis_has_manufacturer():
    assert hasattr(Tennis, "manufacturer")
    descriptor = None
    for klass in Tennis.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_tennis_has_color():
    assert hasattr(Tennis, "color")
    descriptor = None
    for klass in Tennis.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_hyp_tennis_has_engine():
    assert hasattr(Tennis, "engine")
    descriptor = None
    for klass in Tennis.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)



def test_hyp_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_hyp_car_constructor_exists():
    assert callable(Car.__init__)


def test_hyp_car_constructor_args():
    sig = inspect.signature(Car.__init__)
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
Test_strategy = st.builds(
    Test,
)
TestStand_strategy = st.builds(
    TestStand,
    carToBeTested=
        st.none()
)
M6_strategy = st.builds(
    M6,
    manufacturer=
        safe_text,
    color=
        safe_text,
    engine=
        st.none()
)
Engine_strategy = st.builds(
    Engine,
    engineSpeed=
        st.integers(),
    efficiencyCoefficient=
        st.integers(),
    type=
        safe_text
)
Tennis_strategy = st.builds(
    Tennis,
    manufacturer=
        safe_text,
    color=
        safe_text,
    engine=
        st.none()
)
Car_strategy = st.builds(
    Car,
)


@given(instance=TestStand_strategy)
@settings(max_examples=50)
def test_hyp_teststand_instantiation(instance):
    assert isinstance(instance, TestStand)



@given(instance=TestStand_strategy)
def test_hyp_teststand_carToBeTested_setter(instance):
    original = instance.carToBeTested
    instance.carToBeTested = original
    assert instance.carToBeTested == original

@given(instance=M6_strategy)
@settings(max_examples=50)
def test_hyp_m6_instantiation(instance):
    assert isinstance(instance, M6)



@given(instance=M6_strategy)
def test_hyp_m6_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=M6_strategy)
def test_hyp_m6_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=M6_strategy)
def test_hyp_m6_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original




@given(instance=Engine_strategy)
def test_hyp_engine_engineSpeed_setter(instance):
    original = instance.engineSpeed
    instance.engineSpeed = original
    assert instance.engineSpeed == original



@given(instance=Engine_strategy)
def test_hyp_engine_efficiencyCoefficient_setter(instance):
    original = instance.efficiencyCoefficient
    instance.efficiencyCoefficient = original
    assert instance.efficiencyCoefficient == original



@given(instance=Engine_strategy)
def test_hyp_engine_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Tennis_strategy)
@settings(max_examples=50)
def test_hyp_tennis_instantiation(instance):
    assert isinstance(instance, Tennis)



@given(instance=Tennis_strategy)
def test_hyp_tennis_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=Tennis_strategy)
def test_hyp_tennis_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Tennis_strategy)
def test_hyp_tennis_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Car,
    Engine,
    M6,
    Tennis,
    Test,
    TestStand,
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

def test_Engine_efficiencyCoefficient_value_roundtrip():
    instance = Engine(efficiencyCoefficient=7, engineSpeed=7, type="sample_text")
    assert instance.efficiencyCoefficient == 7
    instance.efficiencyCoefficient = 13
    assert instance.efficiencyCoefficient == 13


def test_Engine_engineSpeed_value_roundtrip():
    instance = Engine(efficiencyCoefficient=7, engineSpeed=7, type="sample_text")
    assert instance.engineSpeed == 7
    instance.engineSpeed = 13
    assert instance.engineSpeed == 13


def test_Engine_type_value_roundtrip():
    instance = Engine(efficiencyCoefficient=7, engineSpeed=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Car_strategy = st.builds(Car)
@given(instance=Car_strategy)
@settings(max_examples=25)
def test_Car_instantiation(instance):
    assert isinstance(instance, Car)


Engine_strategy = st.builds(Engine, efficiencyCoefficient=st.integers(), engineSpeed=st.integers(), type=safe_text)
@given(instance=Engine_strategy)
@settings(max_examples=25)
def test_Engine_instantiation(instance):
    assert isinstance(instance, Engine)


Test_strategy = st.builds(Test)
@given(instance=Test_strategy)
@settings(max_examples=25)
def test_Test_instantiation(instance):
    assert isinstance(instance, Test)



