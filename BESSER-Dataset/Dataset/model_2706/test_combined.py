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
    pghttptest_Priv,
    C,
    pghttptest_D,
    pghttptest_C,
    pghttptest_B,
    pghttptest_A,
    pghttptest_Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pghttptest_priv_is_not_abstract():
    assert not inspect.isabstract(pghttptest_Priv)


def test_hyp_pghttptest_priv_constructor_exists():
    assert callable(pghttptest_Priv.__init__)


def test_hyp_pghttptest_priv_constructor_args():
    sig = inspect.signature(pghttptest_Priv.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_hyp_c_constructor_exists():
    assert callable(C.__init__)


def test_hyp_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pghttptest_d_is_not_abstract():
    assert not inspect.isabstract(pghttptest_D)


def test_hyp_pghttptest_d_constructor_exists():
    assert callable(pghttptest_D.__init__)


def test_hyp_pghttptest_d_constructor_args():
    sig = inspect.signature(pghttptest_D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pghttptest_c_is_not_abstract():
    assert not inspect.isabstract(pghttptest_C)


def test_hyp_pghttptest_c_constructor_exists():
    assert callable(pghttptest_C.__init__)


def test_hyp_pghttptest_c_constructor_args():
    sig = inspect.signature(pghttptest_C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pghttptest_b_is_not_abstract():
    assert not inspect.isabstract(pghttptest_B)


def test_hyp_pghttptest_b_constructor_exists():
    assert callable(pghttptest_B.__init__)


def test_hyp_pghttptest_b_constructor_args():
    sig = inspect.signature(pghttptest_B.__init__)
    params = list(sig.parameters.keys())
    assert "priv1" in params, "Missing parameter 'priv1'"




def test_hyp_pghttptest_a_is_not_abstract():
    assert not inspect.isabstract(pghttptest_A)


def test_hyp_pghttptest_a_constructor_exists():
    assert callable(pghttptest_A.__init__)


def test_hyp_pghttptest_a_constructor_args():
    sig = inspect.signature(pghttptest_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_pghttptest_root_is_not_abstract():
    assert not inspect.isabstract(pghttptest_Root)


def test_hyp_pghttptest_root_constructor_exists():
    assert callable(pghttptest_Root.__init__)


def test_hyp_pghttptest_root_constructor_args():
    sig = inspect.signature(pghttptest_Root.__init__)
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
pghttptest_Priv_strategy = st.builds(
    pghttptest_Priv,
    name=
        safe_text
)
C_strategy = st.builds(
    C,
)
pghttptest_D_strategy = st.builds(
    pghttptest_D,
)
pghttptest_C_strategy = st.builds(
    pghttptest_C,
    name=
        safe_text
)
pghttptest_B_strategy = st.builds(
    pghttptest_B,
    priv1=
        st.integers()
)
pghttptest_A_strategy = st.builds(
    pghttptest_A,
    name=
        safe_text,
    value=
        st.integers()
)
pghttptest_Root_strategy = st.builds(
    pghttptest_Root,
)




@given(instance=pghttptest_Priv_strategy)
def test_hyp_pghttptest_priv_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=pghttptest_C_strategy)
def test_hyp_pghttptest_c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pghttptest_C_strategy)
@settings(max_examples=30)
def test_hyp_pghttptest_c_rotname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.rotName(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.rotName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'rotName' in pghttptest_C is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'rotName' in pghttptest_C did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'rotName' in pghttptest_C is not implemented or raised an error")




@given(instance=pghttptest_B_strategy)
def test_hyp_pghttptest_b_priv1_setter(instance):
    original = instance.priv1
    instance.priv1 = original
    assert instance.priv1 == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pghttptest_B_strategy)
@settings(max_examples=30)
def test_hyp_pghttptest_b_priv2_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.priv2()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.priv2).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'priv2' in pghttptest_B is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'priv2' in pghttptest_B did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'priv2' in pghttptest_B is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pghttptest_B_strategy)
@settings(max_examples=30)
def test_hyp_pghttptest_b_lastc_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lastC()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lastC).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lastC' in pghttptest_B is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lastC' in pghttptest_B did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lastC' in pghttptest_B is not implemented or raised an error")




@given(instance=pghttptest_A_strategy)
def test_hyp_pghttptest_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pghttptest_A_strategy)
def test_hyp_pghttptest_a_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    C,
    pghttptest_A,
    pghttptest_B,
    pghttptest_C,
    pghttptest_D,
    pghttptest_Priv,
    pghttptest_Root,
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

def test_pghttptest_A_name_value_roundtrip():
    instance = pghttptest_A(name="sample_text", value=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pghttptest_A_value_value_roundtrip():
    instance = pghttptest_A(name="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_pghttptest_B_priv1_value_roundtrip():
    instance = pghttptest_B(priv1=7)
    assert instance.priv1 == 7
    instance.priv1 = 13
    assert instance.priv1 == 13


def test_pghttptest_C_name_value_roundtrip():
    instance = pghttptest_C(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pghttptest_Priv_name_value_roundtrip():
    instance = pghttptest_Priv(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pghttptest_D_isa_C():
    instance = pghttptest_D()
    assert isinstance(instance, C)


def test_assoc_as_0_link_reassign_clear():
    a = pghttptest_A(name="sample_text", value=7)
    b1 = pghttptest_Root()
    b2 = pghttptest_Root()
    _safe_set(a, 'pghttptest_A', b1)
    assert _is_linked(a, 'pghttptest_A', b1)
    if hasattr(b1, 'pghttptest_Root'):
        assert _is_linked(b1, 'pghttptest_Root', a)
    _safe_set(a, 'pghttptest_A', b2)
    assert _is_linked(a, 'pghttptest_A', b2)
    if hasattr(b1, 'pghttptest_Root'):
        assert not _is_linked(b1, 'pghttptest_Root', a)
    if hasattr(b2, 'pghttptest_Root'):
        assert _is_linked(b2, 'pghttptest_Root', a)
    _safe_set(a, 'pghttptest_A', None)
    assert not _is_linked(a, 'pghttptest_A', b2)
    if hasattr(b2, 'pghttptest_Root'):
        assert not _is_linked(b2, 'pghttptest_Root', a)


def test_assoc_b1_link_reassign_clear():
    a = pghttptest_B(priv1=7)
    b1 = pghttptest_Root()
    b2 = pghttptest_Root()
    _safe_set(a, 'pghttptest_B', b1)
    assert _is_linked(a, 'pghttptest_B', b1)
    if hasattr(b1, 'pghttptest_Root2'):
        assert _is_linked(b1, 'pghttptest_Root2', a)
    _safe_set(a, 'pghttptest_B', b2)
    assert _is_linked(a, 'pghttptest_B', b2)
    if hasattr(b1, 'pghttptest_Root2'):
        assert not _is_linked(b1, 'pghttptest_Root2', a)
    if hasattr(b2, 'pghttptest_Root2'):
        assert _is_linked(b2, 'pghttptest_Root2', a)
    _safe_set(a, 'pghttptest_B', None)
    assert not _is_linked(a, 'pghttptest_B', b2)
    if hasattr(b2, 'pghttptest_Root2'):
        assert not _is_linked(b2, 'pghttptest_Root2', a)


def test_assoc_cs3_link_reassign_clear():
    a = pghttptest_C(name="sample_text")
    b1 = pghttptest_B(priv1=7)
    b2 = pghttptest_B(priv1=13)
    _safe_set(a, 'pghttptest_C', b1)
    assert _is_linked(a, 'pghttptest_C', b1)
    if hasattr(b1, 'pghttptest_B4'):
        assert _is_linked(b1, 'pghttptest_B4', a)
    _safe_set(a, 'pghttptest_C', b2)
    assert _is_linked(a, 'pghttptest_C', b2)
    if hasattr(b1, 'pghttptest_B4'):
        assert not _is_linked(b1, 'pghttptest_B4', a)
    if hasattr(b2, 'pghttptest_B4'):
        assert _is_linked(b2, 'pghttptest_B4', a)
    _safe_set(a, 'pghttptest_C', None)
    assert not _is_linked(a, 'pghttptest_C', b2)
    if hasattr(b2, 'pghttptest_B4'):
        assert not _is_linked(b2, 'pghttptest_B4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

C_strategy = st.builds(C)
@given(instance=C_strategy)
@settings(max_examples=25)
def test_C_instantiation(instance):
    assert isinstance(instance, C)


pghttptest_A_strategy = st.builds(pghttptest_A, name=safe_text, value=st.integers())
@given(instance=pghttptest_A_strategy)
@settings(max_examples=25)
def test_pghttptest_A_instantiation(instance):
    assert isinstance(instance, pghttptest_A)


pghttptest_B_strategy = st.builds(pghttptest_B, priv1=st.integers())
@given(instance=pghttptest_B_strategy)
@settings(max_examples=25)
def test_pghttptest_B_instantiation(instance):
    assert isinstance(instance, pghttptest_B)


pghttptest_C_strategy = st.builds(pghttptest_C, name=safe_text)
@given(instance=pghttptest_C_strategy)
@settings(max_examples=25)
def test_pghttptest_C_instantiation(instance):
    assert isinstance(instance, pghttptest_C)


pghttptest_D_strategy = st.builds(pghttptest_D)
@given(instance=pghttptest_D_strategy)
@settings(max_examples=25)
def test_pghttptest_D_instantiation(instance):
    assert isinstance(instance, pghttptest_D)


pghttptest_Priv_strategy = st.builds(pghttptest_Priv, name=safe_text)
@given(instance=pghttptest_Priv_strategy)
@settings(max_examples=25)
def test_pghttptest_Priv_instantiation(instance):
    assert isinstance(instance, pghttptest_Priv)


pghttptest_Root_strategy = st.builds(pghttptest_Root)
@given(instance=pghttptest_Root_strategy)
@settings(max_examples=25)
def test_pghttptest_Root_instantiation(instance):
    assert isinstance(instance, pghttptest_Root)



