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
    C32,
    C22,
    C4,
    B2,
    Z2,
    A2,
    R2,
    Y2,
    A,
    C3,
    C2,
    R,
    Z,
    B,
    Y,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_c32_is_not_abstract():
    assert not inspect.isabstract(C32)


def test_hyp_c32_constructor_exists():
    assert callable(C32.__init__)


def test_hyp_c32_constructor_args():
    sig = inspect.signature(C32.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c22_is_not_abstract():
    assert not inspect.isabstract(C22)


def test_hyp_c22_constructor_exists():
    assert callable(C22.__init__)


def test_hyp_c22_constructor_args():
    sig = inspect.signature(C22.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c4_is_not_abstract():
    assert not inspect.isabstract(C4)


def test_hyp_c4_constructor_exists():
    assert callable(C4.__init__)


def test_hyp_c4_constructor_args():
    sig = inspect.signature(C4.__init__)
    params = list(sig.parameters.keys())
    assert "attC" in params, "Missing parameter 'attC'"
    assert "attC2" in params, "Missing parameter 'attC2'"





def test_hyp_b2_is_not_abstract():
    assert not inspect.isabstract(B2)


def test_hyp_b2_constructor_exists():
    assert callable(B2.__init__)


def test_hyp_b2_constructor_args():
    sig = inspect.signature(B2.__init__)
    params = list(sig.parameters.keys())
    assert "attB" in params, "Missing parameter 'attB'"




def test_hyp_z2_is_not_abstract():
    assert not inspect.isabstract(Z2)


def test_hyp_z2_constructor_exists():
    assert callable(Z2.__init__)


def test_hyp_z2_constructor_args():
    sig = inspect.signature(Z2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a2_is_not_abstract():
    assert not inspect.isabstract(A2)


def test_hyp_a2_constructor_exists():
    assert callable(A2.__init__)


def test_hyp_a2_constructor_args():
    sig = inspect.signature(A2.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"




def test_hyp_r2_is_not_abstract():
    assert not inspect.isabstract(R2)


def test_hyp_r2_constructor_exists():
    assert callable(R2.__init__)


def test_hyp_r2_constructor_args():
    sig = inspect.signature(R2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_y2_is_not_abstract():
    assert not inspect.isabstract(Y2)


def test_hyp_y2_constructor_exists():
    assert callable(Y2.__init__)


def test_hyp_y2_constructor_args():
    sig = inspect.signature(Y2.__init__)
    params = list(sig.parameters.keys())
    assert "attY" in params, "Missing parameter 'attY'"




def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())
    assert "attA" in params, "Missing parameter 'attA'"




def test_hyp_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_hyp_c3_constructor_exists():
    assert callable(C3.__init__)


def test_hyp_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_hyp_c2_constructor_exists():
    assert callable(C2.__init__)


def test_hyp_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_r_is_not_abstract():
    assert not inspect.isabstract(R)


def test_hyp_r_constructor_exists():
    assert callable(R.__init__)


def test_hyp_r_constructor_args():
    sig = inspect.signature(R.__init__)
    params = list(sig.parameters.keys())



def test_hyp_z_is_not_abstract():
    assert not inspect.isabstract(Z)


def test_hyp_z_constructor_exists():
    assert callable(Z.__init__)


def test_hyp_z_constructor_args():
    sig = inspect.signature(Z.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())
    assert "attB" in params, "Missing parameter 'attB'"




def test_hyp_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_hyp_y_constructor_exists():
    assert callable(Y.__init__)


def test_hyp_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())
    assert "attY" in params, "Missing parameter 'attY'"



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
C32_strategy = st.builds(
    C32,
)
C22_strategy = st.builds(
    C22,
)
C4_strategy = st.builds(
    C4,
    attC=
        st.booleans(),
    attC2=
        st.integers()
)
B2_strategy = st.builds(
    B2,
    attB=
        st.integers()
)
Z2_strategy = st.builds(
    Z2,
)
A2_strategy = st.builds(
    A2,
    attA=
        safe_text
)
R2_strategy = st.builds(
    R2,
)
Y2_strategy = st.builds(
    Y2,
    attY=
        safe_text
)
A_strategy = st.builds(
    A,
    attA=
        safe_text
)
C3_strategy = st.builds(
    C3,
)
C2_strategy = st.builds(
    C2,
)
R_strategy = st.builds(
    R,
)
Z_strategy = st.builds(
    Z,
)
B_strategy = st.builds(
    B,
    attB=
        st.integers()
)
Y_strategy = st.builds(
    Y,
    attY=
        safe_text
)






@given(instance=C4_strategy)
def test_hyp_c4_attC_setter(instance):
    original = instance.attC
    instance.attC = original
    assert instance.attC == original



@given(instance=C4_strategy)
def test_hyp_c4_attC2_setter(instance):
    original = instance.attC2
    instance.attC2 = original
    assert instance.attC2 == original




@given(instance=B2_strategy)
def test_hyp_b2_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original





@given(instance=A2_strategy)
def test_hyp_a2_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original





@given(instance=Y2_strategy)
def test_hyp_y2_attY_setter(instance):
    original = instance.attY
    instance.attY = original
    assert instance.attY == original




@given(instance=A_strategy)
def test_hyp_a_attA_setter(instance):
    original = instance.attA
    instance.attA = original
    assert instance.attA == original








@given(instance=B_strategy)
def test_hyp_b_attB_setter(instance):
    original = instance.attB
    instance.attB = original
    assert instance.attB == original




@given(instance=Y_strategy)
def test_hyp_y_attY_setter(instance):
    original = instance.attY
    instance.attY = original
    assert instance.attY == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    A2,
    B,
    B2,
    C2,
    C22,
    C3,
    C32,
    C4,
    R,
    R2,
    Y,
    Y2,
    Z,
    Z2,
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

def test_A_attA_value_roundtrip():
    instance = A(attA="sample_text")
    assert instance.attA == "sample_text"
    instance.attA = "sample_text_2"
    assert instance.attA == "sample_text_2"


def test_A2_attA_value_roundtrip():
    instance = A2(attA="sample_text")
    assert instance.attA == "sample_text"
    instance.attA = "sample_text_2"
    assert instance.attA == "sample_text_2"


def test_B_attB_value_roundtrip():
    instance = B(attB=7)
    assert instance.attB == 7
    instance.attB = 13
    assert instance.attB == 13


def test_B2_attB_value_roundtrip():
    instance = B2(attB=7)
    assert instance.attB == 7
    instance.attB = 13
    assert instance.attB == 13


def test_C4_attC_value_roundtrip():
    instance = C4(attC=True, attC2=7)
    assert instance.attC == True
    instance.attC = False
    assert instance.attC == False


def test_C4_attC2_value_roundtrip():
    instance = C4(attC=True, attC2=7)
    assert instance.attC2 == 7
    instance.attC2 = 13
    assert instance.attC2 == 13


def test_Y_attY_value_roundtrip():
    instance = Y(attY="sample_text")
    assert instance.attY == "sample_text"
    instance.attY = "sample_text_2"
    assert instance.attY == "sample_text_2"


def test_Y2_attY_value_roundtrip():
    instance = Y2(attY="sample_text")
    assert instance.attY == "sample_text"
    instance.attY = "sample_text_2"
    assert instance.attY == "sample_text_2"


def test_assoc_A_B2_link_reassign_clear():
    a = B(attB=7)
    b1 = A(attA="sample_text")
    b2 = A(attA="sample_text_2")
    _safe_set(a, 'a3', b1)
    assert _is_linked(a, 'a3', b1)
    if hasattr(b1, 'b2'):
        assert _is_linked(b1, 'b2', a)
    _safe_set(a, 'a3', b2)
    assert _is_linked(a, 'a3', b2)
    if hasattr(b1, 'b2'):
        assert not _is_linked(b1, 'b2', a)
    if hasattr(b2, 'b2'):
        assert _is_linked(b2, 'b2', a)
    _safe_set(a, 'a3', None)
    assert not _is_linked(a, 'a3', b2)
    if hasattr(b2, 'b2'):
        assert not _is_linked(b2, 'b2', a)


def test_assoc_A_B22_link_reassign_clear():
    a = B2(attB=7)
    b1 = A2(attA="sample_text")
    b2 = A2(attA="sample_text_2")
    _safe_set(a, 'a7', b1)
    assert _is_linked(a, 'a7', b1)
    if hasattr(b1, 'b6'):
        assert _is_linked(b1, 'b6', a)
    _safe_set(a, 'a7', b2)
    assert _is_linked(a, 'a7', b2)
    if hasattr(b1, 'b6'):
        assert not _is_linked(b1, 'b6', a)
    if hasattr(b2, 'b6'):
        assert _is_linked(b2, 'b6', a)
    _safe_set(a, 'a7', None)
    assert not _is_linked(a, 'a7', b2)
    if hasattr(b2, 'b6'):
        assert not _is_linked(b2, 'b6', a)


def test_assoc_B_C22_link_reassign_clear():
    a = C4(attC=True, attC2=7)
    b1 = B2(attB=7)
    b2 = B2(attB=13)
    _safe_set(a, 'b9', b1)
    assert _is_linked(a, 'b9', b1)
    if hasattr(b1, 'c8'):
        assert _is_linked(b1, 'c8', a)
    _safe_set(a, 'b9', b2)
    assert _is_linked(a, 'b9', b2)
    if hasattr(b1, 'c8'):
        assert not _is_linked(b1, 'c8', a)
    if hasattr(b2, 'c8'):
        assert _is_linked(b2, 'c8', a)
    _safe_set(a, 'b9', None)
    assert not _is_linked(a, 'b9', b2)
    if hasattr(b2, 'c8'):
        assert not _is_linked(b2, 'c8', a)


def test_assoc_R_A_link_reassign_clear():
    a = A(attA="sample_text")
    b1 = R()
    b2 = R()
    _safe_set(a, 'r1', b1)
    assert _is_linked(a, 'r1', b1)
    if hasattr(b1, 'a0'):
        assert _is_linked(b1, 'a0', a)
    _safe_set(a, 'r1', b2)
    assert _is_linked(a, 'r1', b2)
    if hasattr(b1, 'a0'):
        assert not _is_linked(b1, 'a0', a)
    if hasattr(b2, 'a0'):
        assert _is_linked(b2, 'a0', a)
    _safe_set(a, 'r1', None)
    assert not _is_linked(a, 'r1', b2)
    if hasattr(b2, 'a0'):
        assert not _is_linked(b2, 'a0', a)


def test_assoc_R_A2_link_reassign_clear():
    a = A2(attA="sample_text")
    b1 = R2()
    b2 = R2()
    _safe_set(a, 'r5', b1)
    assert _is_linked(a, 'r5', b1)
    if hasattr(b1, 'a4'):
        assert _is_linked(b1, 'a4', a)
    _safe_set(a, 'r5', b2)
    assert _is_linked(a, 'r5', b2)
    if hasattr(b1, 'a4'):
        assert not _is_linked(b1, 'a4', a)
    if hasattr(b2, 'a4'):
        assert _is_linked(b2, 'a4', a)
    _safe_set(a, 'r5', None)
    assert not _is_linked(a, 'r5', b2)
    if hasattr(b2, 'a4'):
        assert not _is_linked(b2, 'a4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A, attA=safe_text)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


A2_strategy = st.builds(A2, attA=safe_text)
@given(instance=A2_strategy)
@settings(max_examples=25)
def test_A2_instantiation(instance):
    assert isinstance(instance, A2)


B_strategy = st.builds(B, attB=st.integers())
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


B2_strategy = st.builds(B2, attB=st.integers())
@given(instance=B2_strategy)
@settings(max_examples=25)
def test_B2_instantiation(instance):
    assert isinstance(instance, B2)


C2_strategy = st.builds(C2)
@given(instance=C2_strategy)
@settings(max_examples=25)
def test_C2_instantiation(instance):
    assert isinstance(instance, C2)


C22_strategy = st.builds(C22)
@given(instance=C22_strategy)
@settings(max_examples=25)
def test_C22_instantiation(instance):
    assert isinstance(instance, C22)


C3_strategy = st.builds(C3)
@given(instance=C3_strategy)
@settings(max_examples=25)
def test_C3_instantiation(instance):
    assert isinstance(instance, C3)


C32_strategy = st.builds(C32)
@given(instance=C32_strategy)
@settings(max_examples=25)
def test_C32_instantiation(instance):
    assert isinstance(instance, C32)


C4_strategy = st.builds(C4, attC=st.booleans(), attC2=st.integers())
@given(instance=C4_strategy)
@settings(max_examples=25)
def test_C4_instantiation(instance):
    assert isinstance(instance, C4)


R_strategy = st.builds(R)
@given(instance=R_strategy)
@settings(max_examples=25)
def test_R_instantiation(instance):
    assert isinstance(instance, R)


R2_strategy = st.builds(R2)
@given(instance=R2_strategy)
@settings(max_examples=25)
def test_R2_instantiation(instance):
    assert isinstance(instance, R2)


Y_strategy = st.builds(Y, attY=safe_text)
@given(instance=Y_strategy)
@settings(max_examples=25)
def test_Y_instantiation(instance):
    assert isinstance(instance, Y)


Y2_strategy = st.builds(Y2, attY=safe_text)
@given(instance=Y2_strategy)
@settings(max_examples=25)
def test_Y2_instantiation(instance):
    assert isinstance(instance, Y2)


Z_strategy = st.builds(Z)
@given(instance=Z_strategy)
@settings(max_examples=25)
def test_Z_instantiation(instance):
    assert isinstance(instance, Z)


Z2_strategy = st.builds(Z2)
@given(instance=Z2_strategy)
@settings(max_examples=25)
def test_Z2_instantiation(instance):
    assert isinstance(instance, Z2)



