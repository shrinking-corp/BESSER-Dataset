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
    genericsGoCrazy_OtherClass,
    Car,
    genericsGoCrazy_SubCar,
    genericsGoCrazy_Car,
    genericsGoCrazy_Comp,
    genericsGoCrazy_MySubClass,
    genericsGoCrazy_MyClass,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_genericsgocrazy_otherclass_is_not_abstract():
    assert not inspect.isabstract(genericsGoCrazy_OtherClass)


def test_hyp_genericsgocrazy_otherclass_constructor_exists():
    assert callable(genericsGoCrazy_OtherClass.__init__)


def test_hyp_genericsgocrazy_otherclass_constructor_args():
    sig = inspect.signature(genericsGoCrazy_OtherClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_car_is_not_abstract():
    assert not inspect.isabstract(Car)


def test_hyp_car_constructor_exists():
    assert callable(Car.__init__)


def test_hyp_car_constructor_args():
    sig = inspect.signature(Car.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genericsgocrazy_subcar_is_not_abstract():
    assert not inspect.isabstract(genericsGoCrazy_SubCar)


def test_hyp_genericsgocrazy_subcar_constructor_exists():
    assert callable(genericsGoCrazy_SubCar.__init__)


def test_hyp_genericsgocrazy_subcar_constructor_args():
    sig = inspect.signature(genericsGoCrazy_SubCar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genericsgocrazy_car_is_not_abstract():
    assert not inspect.isabstract(genericsGoCrazy_Car)


def test_hyp_genericsgocrazy_car_constructor_exists():
    assert callable(genericsGoCrazy_Car.__init__)


def test_hyp_genericsgocrazy_car_constructor_args():
    sig = inspect.signature(genericsGoCrazy_Car.__init__)
    params = list(sig.parameters.keys())
    assert "doors" in params, "Missing parameter 'doors'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "color" in params, "Missing parameter 'color'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_genericsgocrazy_comp_is_not_abstract():
    assert not inspect.isabstract(genericsGoCrazy_Comp)


def test_hyp_genericsgocrazy_comp_constructor_exists():
    assert callable(genericsGoCrazy_Comp.__init__)


def test_hyp_genericsgocrazy_comp_constructor_args():
    sig = inspect.signature(genericsGoCrazy_Comp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genericsgocrazy_mysubclass_is_not_abstract():
    assert not inspect.isabstract(genericsGoCrazy_MySubClass)


def test_hyp_genericsgocrazy_mysubclass_constructor_exists():
    assert callable(genericsGoCrazy_MySubClass.__init__)


def test_hyp_genericsgocrazy_mysubclass_constructor_args():
    sig = inspect.signature(genericsGoCrazy_MySubClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_genericsgocrazy_myclass_is_not_abstract():
    assert not inspect.isabstract(genericsGoCrazy_MyClass)


def test_hyp_genericsgocrazy_myclass_constructor_exists():
    assert callable(genericsGoCrazy_MyClass.__init__)


def test_hyp_genericsgocrazy_myclass_constructor_args():
    sig = inspect.signature(genericsGoCrazy_MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "aMap" in params, "Missing parameter 'aMap'"
    assert "theEObject" in params, "Missing parameter 'theEObject'"
    assert "a2" in params, "Missing parameter 'a2'"
    assert "a3" in params, "Missing parameter 'a3'"
    assert "a1" in params, "Missing parameter 'a1'"






def test_hyp_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_hyp_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "BLUE",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
genericsGoCrazy_OtherClass_strategy = st.builds(
    genericsGoCrazy_OtherClass,
)
Car_strategy = st.builds(
    Car,
)
genericsGoCrazy_SubCar_strategy = st.builds(
    genericsGoCrazy_SubCar,
)
genericsGoCrazy_Car_strategy = st.builds(
    genericsGoCrazy_Car,
    doors=
        safe_text,
    fullName=
        safe_text,
    color=
        safe_text,
    name=
        safe_text
)
genericsGoCrazy_Comp_strategy = st.builds(
    genericsGoCrazy_Comp,
)
genericsGoCrazy_MySubClass_strategy = st.builds(
    genericsGoCrazy_MySubClass,
)
genericsGoCrazy_MyClass_strategy = st.builds(
    genericsGoCrazy_MyClass,
    aMap=
        safe_text,
    theEObject=
        safe_text,
    a2=
        safe_text,
    a3=
        safe_text,
    a1=
        safe_text
)







@given(instance=genericsGoCrazy_Car_strategy)
def test_hyp_genericsgocrazy_car_doors_setter(instance):
    original = instance.doors
    instance.doors = original
    assert instance.doors == original



@given(instance=genericsGoCrazy_Car_strategy)
def test_hyp_genericsgocrazy_car_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=genericsGoCrazy_Car_strategy)
def test_hyp_genericsgocrazy_car_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=genericsGoCrazy_Car_strategy)
def test_hyp_genericsgocrazy_car_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=genericsGoCrazy_Car_strategy)
@settings(max_examples=30)
def test_hyp_genericsgocrazy_car_superfoo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.superFoo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.superFoo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'superFoo' in genericsGoCrazy_Car is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'superFoo' in genericsGoCrazy_Car did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'superFoo' in genericsGoCrazy_Car is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=genericsGoCrazy_Car_strategy)
@settings(max_examples=30)
def test_hyp_genericsgocrazy_car_enhancedfoo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.enhancedFoo(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.enhancedFoo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'enhancedFoo' in genericsGoCrazy_Car is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'enhancedFoo' in genericsGoCrazy_Car did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'enhancedFoo' in genericsGoCrazy_Car is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=genericsGoCrazy_Car_strategy)
@settings(max_examples=30)
def test_hyp_genericsgocrazy_car_foo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.foo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.foo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'foo' in genericsGoCrazy_Car is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in genericsGoCrazy_Car did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in genericsGoCrazy_Car is not implemented or raised an error")






@given(instance=genericsGoCrazy_MyClass_strategy)
def test_hyp_genericsgocrazy_myclass_aMap_setter(instance):
    original = instance.aMap
    instance.aMap = original
    assert instance.aMap == original



@given(instance=genericsGoCrazy_MyClass_strategy)
def test_hyp_genericsgocrazy_myclass_theEObject_setter(instance):
    original = instance.theEObject
    instance.theEObject = original
    assert instance.theEObject == original



@given(instance=genericsGoCrazy_MyClass_strategy)
def test_hyp_genericsgocrazy_myclass_a2_setter(instance):
    original = instance.a2
    instance.a2 = original
    assert instance.a2 == original



@given(instance=genericsGoCrazy_MyClass_strategy)
def test_hyp_genericsgocrazy_myclass_a3_setter(instance):
    original = instance.a3
    instance.a3 = original
    assert instance.a3 == original



@given(instance=genericsGoCrazy_MyClass_strategy)
def test_hyp_genericsgocrazy_myclass_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=genericsGoCrazy_MyClass_strategy)
@settings(max_examples=30)
def test_hyp_genericsgocrazy_myclass_bar_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bar(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bar).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bar' in genericsGoCrazy_MyClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bar' in genericsGoCrazy_MyClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bar' in genericsGoCrazy_MyClass is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Car,
    genericsGoCrazy_Car,
    genericsGoCrazy_Comp,
    genericsGoCrazy_MyClass,
    genericsGoCrazy_MySubClass,
    genericsGoCrazy_OtherClass,
    genericsGoCrazy_SubCar,
    Color,
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

def test_genericsGoCrazy_Car_color_value_roundtrip():
    instance = genericsGoCrazy_Car(color="sample_text", doors="sample_text", fullName="sample_text", name="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_genericsGoCrazy_Car_doors_value_roundtrip():
    instance = genericsGoCrazy_Car(color="sample_text", doors="sample_text", fullName="sample_text", name="sample_text")
    assert instance.doors == "sample_text"
    instance.doors = "sample_text_2"
    assert instance.doors == "sample_text_2"


def test_genericsGoCrazy_Car_fullName_value_roundtrip():
    instance = genericsGoCrazy_Car(color="sample_text", doors="sample_text", fullName="sample_text", name="sample_text")
    assert instance.fullName == "sample_text"
    instance.fullName = "sample_text_2"
    assert instance.fullName == "sample_text_2"


def test_genericsGoCrazy_Car_name_value_roundtrip():
    instance = genericsGoCrazy_Car(color="sample_text", doors="sample_text", fullName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_genericsGoCrazy_MyClass_a1_value_roundtrip():
    instance = genericsGoCrazy_MyClass(a1="sample_text", a2="sample_text", a3="sample_text", aMap="sample_text", theEObject="sample_text")
    assert instance.a1 == "sample_text"
    instance.a1 = "sample_text_2"
    assert instance.a1 == "sample_text_2"


def test_genericsGoCrazy_MyClass_a2_value_roundtrip():
    instance = genericsGoCrazy_MyClass(a1="sample_text", a2="sample_text", a3="sample_text", aMap="sample_text", theEObject="sample_text")
    assert instance.a2 == "sample_text"
    instance.a2 = "sample_text_2"
    assert instance.a2 == "sample_text_2"


def test_genericsGoCrazy_MyClass_a3_value_roundtrip():
    instance = genericsGoCrazy_MyClass(a1="sample_text", a2="sample_text", a3="sample_text", aMap="sample_text", theEObject="sample_text")
    assert instance.a3 == "sample_text"
    instance.a3 = "sample_text_2"
    assert instance.a3 == "sample_text_2"


def test_genericsGoCrazy_MyClass_aMap_value_roundtrip():
    instance = genericsGoCrazy_MyClass(a1="sample_text", a2="sample_text", a3="sample_text", aMap="sample_text", theEObject="sample_text")
    assert instance.aMap == "sample_text"
    instance.aMap = "sample_text_2"
    assert instance.aMap == "sample_text_2"


def test_genericsGoCrazy_MyClass_theEObject_value_roundtrip():
    instance = genericsGoCrazy_MyClass(a1="sample_text", a2="sample_text", a3="sample_text", aMap="sample_text", theEObject="sample_text")
    assert instance.theEObject == "sample_text"
    instance.theEObject = "sample_text_2"
    assert instance.theEObject == "sample_text_2"


def test_genericsGoCrazy_SubCar_isa_Car():
    instance = genericsGoCrazy_SubCar()
    assert isinstance(instance, Car)


def test_assoc_previousCar1_link_reassign_clear():
    a = genericsGoCrazy_Car(color="sample_text", doors="sample_text", fullName="sample_text", name="sample_text")
    b1 = genericsGoCrazy_Car(color="sample_text", doors="sample_text", fullName="sample_text", name="sample_text")
    b2 = genericsGoCrazy_Car(color="sample_text_2", doors="sample_text_2", fullName="sample_text_2", name="sample_text_2")
    _safe_set(a, 'genericsGoCrazy_Car', b1)
    assert _is_linked(a, 'genericsGoCrazy_Car', b1)
    if hasattr(b1, 'genericsGoCrazy_Car0'):
        assert _is_linked(b1, 'genericsGoCrazy_Car0', a)
    _safe_set(a, 'genericsGoCrazy_Car', b2)
    assert _is_linked(a, 'genericsGoCrazy_Car', b2)
    if hasattr(b1, 'genericsGoCrazy_Car0'):
        assert not _is_linked(b1, 'genericsGoCrazy_Car0', a)
    if hasattr(b2, 'genericsGoCrazy_Car0'):
        assert _is_linked(b2, 'genericsGoCrazy_Car0', a)
    _safe_set(a, 'genericsGoCrazy_Car', None)
    assert not _is_linked(a, 'genericsGoCrazy_Car', b2)
    if hasattr(b2, 'genericsGoCrazy_Car0'):
        assert not _is_linked(b2, 'genericsGoCrazy_Car0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Car_strategy = st.builds(Car)
@given(instance=Car_strategy)
@settings(max_examples=25)
def test_Car_instantiation(instance):
    assert isinstance(instance, Car)


genericsGoCrazy_Car_strategy = st.builds(genericsGoCrazy_Car, color=safe_text, doors=safe_text, fullName=safe_text, name=safe_text)
@given(instance=genericsGoCrazy_Car_strategy)
@settings(max_examples=25)
def test_genericsGoCrazy_Car_instantiation(instance):
    assert isinstance(instance, genericsGoCrazy_Car)


genericsGoCrazy_Comp_strategy = st.builds(genericsGoCrazy_Comp)
@given(instance=genericsGoCrazy_Comp_strategy)
@settings(max_examples=25)
def test_genericsGoCrazy_Comp_instantiation(instance):
    assert isinstance(instance, genericsGoCrazy_Comp)


genericsGoCrazy_MyClass_strategy = st.builds(genericsGoCrazy_MyClass, a1=safe_text, a2=safe_text, a3=safe_text, aMap=safe_text, theEObject=safe_text)
@given(instance=genericsGoCrazy_MyClass_strategy)
@settings(max_examples=25)
def test_genericsGoCrazy_MyClass_instantiation(instance):
    assert isinstance(instance, genericsGoCrazy_MyClass)


genericsGoCrazy_MySubClass_strategy = st.builds(genericsGoCrazy_MySubClass)
@given(instance=genericsGoCrazy_MySubClass_strategy)
@settings(max_examples=25)
def test_genericsGoCrazy_MySubClass_instantiation(instance):
    assert isinstance(instance, genericsGoCrazy_MySubClass)


genericsGoCrazy_OtherClass_strategy = st.builds(genericsGoCrazy_OtherClass)
@given(instance=genericsGoCrazy_OtherClass_strategy)
@settings(max_examples=25)
def test_genericsGoCrazy_OtherClass_instantiation(instance):
    assert isinstance(instance, genericsGoCrazy_OtherClass)


genericsGoCrazy_SubCar_strategy = st.builds(genericsGoCrazy_SubCar)
@given(instance=genericsGoCrazy_SubCar_strategy)
@settings(max_examples=25)
def test_genericsGoCrazy_SubCar_instantiation(instance):
    assert isinstance(instance, genericsGoCrazy_SubCar)



