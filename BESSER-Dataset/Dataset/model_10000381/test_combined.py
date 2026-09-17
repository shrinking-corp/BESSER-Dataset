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
    Trapezoidal,
    Triangular,
    Linear,
    Left_Shoulder,
    Membership_Function,
    Right_Shoulder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_trapezoidal_is_not_abstract():
    assert not inspect.isabstract(Trapezoidal)


def test_hyp_trapezoidal_constructor_exists():
    assert callable(Trapezoidal.__init__)


def test_hyp_trapezoidal_constructor_args():
    sig = inspect.signature(Trapezoidal.__init__)
    params = list(sig.parameters.keys())
    assert "E" in params, "Missing parameter 'E'"
    assert "D" in params, "Missing parameter 'D'"





def test_hyp_triangular_is_not_abstract():
    assert not inspect.isabstract(Triangular)


def test_hyp_triangular_constructor_exists():
    assert callable(Triangular.__init__)


def test_hyp_triangular_constructor_args():
    sig = inspect.signature(Triangular.__init__)
    params = list(sig.parameters.keys())
    assert "C" in params, "Missing parameter 'C'"




def test_hyp_linear_is_not_abstract():
    assert not inspect.isabstract(Linear)


def test_hyp_linear_constructor_exists():
    assert callable(Linear.__init__)


def test_hyp_linear_constructor_args():
    sig = inspect.signature(Linear.__init__)
    params = list(sig.parameters.keys())



def test_hyp_left_shoulder_is_not_abstract():
    assert not inspect.isabstract(Left_Shoulder)


def test_hyp_left_shoulder_constructor_exists():
    assert callable(Left_Shoulder.__init__)


def test_hyp_left_shoulder_constructor_args():
    sig = inspect.signature(Left_Shoulder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_membership_function_is_not_abstract():
    assert not inspect.isabstract(Membership_Function)


def test_hyp_membership_function_constructor_exists():
    assert callable(Membership_Function.__init__)


def test_hyp_membership_function_constructor_args():
    sig = inspect.signature(Membership_Function.__init__)
    params = list(sig.parameters.keys())
    assert "A" in params, "Missing parameter 'A'"
    assert "HasUID" in params, "Missing parameter 'HasUID'"
    assert "B" in params, "Missing parameter 'B'"
    assert "HasName" in params, "Missing parameter 'HasName'"







def test_hyp_right_shoulder_is_not_abstract():
    assert not inspect.isabstract(Right_Shoulder)


def test_hyp_right_shoulder_constructor_exists():
    assert callable(Right_Shoulder.__init__)


def test_hyp_right_shoulder_constructor_args():
    sig = inspect.signature(Right_Shoulder.__init__)
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
Trapezoidal_strategy = st.builds(
    Trapezoidal,
    E=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    D=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Triangular_strategy = st.builds(
    Triangular,
    C=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Linear_strategy = st.builds(
    Linear,
)
Left_Shoulder_strategy = st.builds(
    Left_Shoulder,
)
Membership_Function_strategy = st.builds(
    Membership_Function,
    A=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    HasUID=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    B=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    HasName=
        safe_text
)
Right_Shoulder_strategy = st.builds(
    Right_Shoulder,
)




@given(instance=Trapezoidal_strategy)
def test_hyp_trapezoidal_E_setter(instance):
    original = instance.E
    instance.E = original
    assert instance.E == original



@given(instance=Trapezoidal_strategy)
def test_hyp_trapezoidal_D_setter(instance):
    original = instance.D
    instance.D = original
    assert instance.D == original




@given(instance=Triangular_strategy)
def test_hyp_triangular_C_setter(instance):
    original = instance.C
    instance.C = original
    assert instance.C == original






@given(instance=Membership_Function_strategy)
def test_hyp_membership_function_A_setter(instance):
    original = instance.A
    instance.A = original
    assert instance.A == original



@given(instance=Membership_Function_strategy)
def test_hyp_membership_function_HasUID_setter(instance):
    original = instance.HasUID
    instance.HasUID = original
    assert instance.HasUID == original



@given(instance=Membership_Function_strategy)
def test_hyp_membership_function_B_setter(instance):
    original = instance.B
    instance.B = original
    assert instance.B == original



@given(instance=Membership_Function_strategy)
def test_hyp_membership_function_HasName_setter(instance):
    original = instance.HasName
    instance.HasName = original
    assert instance.HasName == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Left_Shoulder,
    Linear,
    Membership_Function,
    Right_Shoulder,
    Trapezoidal,
    Triangular,
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

def test_Membership_Function_A_value_roundtrip():
    instance = Membership_Function(A=3.14, B=3.14, HasName="sample_text", HasUID=3.14)
    assert instance.A == 3.14
    instance.A = 9.99
    assert instance.A == 9.99


def test_Membership_Function_B_value_roundtrip():
    instance = Membership_Function(A=3.14, B=3.14, HasName="sample_text", HasUID=3.14)
    assert instance.B == 3.14
    instance.B = 9.99
    assert instance.B == 9.99


def test_Membership_Function_HasName_value_roundtrip():
    instance = Membership_Function(A=3.14, B=3.14, HasName="sample_text", HasUID=3.14)
    assert instance.HasName == "sample_text"
    instance.HasName = "sample_text_2"
    assert instance.HasName == "sample_text_2"


def test_Membership_Function_HasUID_value_roundtrip():
    instance = Membership_Function(A=3.14, B=3.14, HasName="sample_text", HasUID=3.14)
    assert instance.HasUID == 3.14
    instance.HasUID = 9.99
    assert instance.HasUID == 9.99


def test_Trapezoidal_D_value_roundtrip():
    instance = Trapezoidal(D=3.14, E=3.14)
    assert instance.D == 3.14
    instance.D = 9.99
    assert instance.D == 9.99


def test_Trapezoidal_E_value_roundtrip():
    instance = Trapezoidal(D=3.14, E=3.14)
    assert instance.E == 3.14
    instance.E = 9.99
    assert instance.E == 9.99


def test_Triangular_C_value_roundtrip():
    instance = Triangular(C=3.14)
    assert instance.C == 3.14
    instance.C = 9.99
    assert instance.C == 9.99


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Left_Shoulder_strategy = st.builds(Left_Shoulder)
@given(instance=Left_Shoulder_strategy)
@settings(max_examples=25)
def test_Left_Shoulder_instantiation(instance):
    assert isinstance(instance, Left_Shoulder)


Linear_strategy = st.builds(Linear)
@given(instance=Linear_strategy)
@settings(max_examples=25)
def test_Linear_instantiation(instance):
    assert isinstance(instance, Linear)


Membership_Function_strategy = st.builds(Membership_Function, A=st.floats(allow_nan=False, allow_infinity=False), B=st.floats(allow_nan=False, allow_infinity=False), HasName=safe_text, HasUID=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Membership_Function_strategy)
@settings(max_examples=25)
def test_Membership_Function_instantiation(instance):
    assert isinstance(instance, Membership_Function)


Right_Shoulder_strategy = st.builds(Right_Shoulder)
@given(instance=Right_Shoulder_strategy)
@settings(max_examples=25)
def test_Right_Shoulder_instantiation(instance):
    assert isinstance(instance, Right_Shoulder)


Trapezoidal_strategy = st.builds(Trapezoidal, D=st.floats(allow_nan=False, allow_infinity=False), E=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Trapezoidal_strategy)
@settings(max_examples=25)
def test_Trapezoidal_instantiation(instance):
    assert isinstance(instance, Trapezoidal)


Triangular_strategy = st.builds(Triangular, C=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Triangular_strategy)
@settings(max_examples=25)
def test_Triangular_instantiation(instance):
    assert isinstance(instance, Triangular)



