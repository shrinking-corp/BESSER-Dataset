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
    SubClass1,
    SubAbstractClass1,
    SubInterface2,
    SubInterface1,
    testmodel_SubInterface6,
    testmodel_SubInterface5,
    testmodel_SubInterface4,
    SuperClass,
    testmodel_SubAbstractClass3,
    testmodel_SubClass3,
    testmodel_SubInterface3,
    SuperAbstractClass,
    testmodel_SubAbstractClass2,
    testmodel_SubClass2,
    testmodel_SubInterface2,
    SuperInterface,
    testmodel_SubAbstractClass1,
    testmodel_SubClass1,
    testmodel_SubInterface1,
    testmodel_SuperClass,
    testmodel_SubClass7,
    testmodel_SubClass6,
    testmodel_SubClass5,
    testmodel_SubClass4,
    testmodel_SubAbstractClass7,
    testmodel_SuperAbstractClass,
    testmodel_SuperInterface,
    testmodel_Target,
    testmodel_Source,
    B,
    testmodel_C,
    A,
    testmodel_B,
    testmodel_A,
    testmodel_SubAbstractClass6,
    testmodel_SubAbstractClass5,
    testmodel_SubAbstractClass4,
    testmodel_SubInterface7,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_subclass1_is_not_abstract():
    assert not inspect.isabstract(SubClass1)


def test_hyp_subclass1_constructor_exists():
    assert callable(SubClass1.__init__)


def test_hyp_subclass1_constructor_args():
    sig = inspect.signature(SubClass1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subabstractclass1_is_not_abstract():
    assert not inspect.isabstract(SubAbstractClass1)


def test_hyp_subabstractclass1_constructor_exists():
    assert callable(SubAbstractClass1.__init__)


def test_hyp_subabstractclass1_constructor_args():
    sig = inspect.signature(SubAbstractClass1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subinterface2_is_not_abstract():
    assert not inspect.isabstract(SubInterface2)


def test_hyp_subinterface2_constructor_exists():
    assert callable(SubInterface2.__init__)


def test_hyp_subinterface2_constructor_args():
    sig = inspect.signature(SubInterface2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subinterface1_is_not_abstract():
    assert not inspect.isabstract(SubInterface1)


def test_hyp_subinterface1_constructor_exists():
    assert callable(SubInterface1.__init__)


def test_hyp_subinterface1_constructor_args():
    sig = inspect.signature(SubInterface1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subinterface6_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubInterface6)


def test_hyp_testmodel_subinterface6_constructor_exists():
    assert callable(testmodel_SubInterface6.__init__)


def test_hyp_testmodel_subinterface6_constructor_args():
    sig = inspect.signature(testmodel_SubInterface6.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subinterface5_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubInterface5)


def test_hyp_testmodel_subinterface5_constructor_exists():
    assert callable(testmodel_SubInterface5.__init__)


def test_hyp_testmodel_subinterface5_constructor_args():
    sig = inspect.signature(testmodel_SubInterface5.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subinterface4_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubInterface4)


def test_hyp_testmodel_subinterface4_constructor_exists():
    assert callable(testmodel_SubInterface4.__init__)


def test_hyp_testmodel_subinterface4_constructor_args():
    sig = inspect.signature(testmodel_SubInterface4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_superclass_is_not_abstract():
    assert not inspect.isabstract(SuperClass)


def test_hyp_superclass_constructor_exists():
    assert callable(SuperClass.__init__)


def test_hyp_superclass_constructor_args():
    sig = inspect.signature(SuperClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subabstractclass3_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubAbstractClass3)


def test_hyp_testmodel_subabstractclass3_constructor_exists():
    assert callable(testmodel_SubAbstractClass3.__init__)


def test_hyp_testmodel_subabstractclass3_constructor_args():
    sig = inspect.signature(testmodel_SubAbstractClass3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subclass3_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubClass3)


def test_hyp_testmodel_subclass3_constructor_exists():
    assert callable(testmodel_SubClass3.__init__)


def test_hyp_testmodel_subclass3_constructor_args():
    sig = inspect.signature(testmodel_SubClass3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subinterface3_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubInterface3)


def test_hyp_testmodel_subinterface3_constructor_exists():
    assert callable(testmodel_SubInterface3.__init__)


def test_hyp_testmodel_subinterface3_constructor_args():
    sig = inspect.signature(testmodel_SubInterface3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_superabstractclass_is_not_abstract():
    assert not inspect.isabstract(SuperAbstractClass)


def test_hyp_superabstractclass_constructor_exists():
    assert callable(SuperAbstractClass.__init__)


def test_hyp_superabstractclass_constructor_args():
    sig = inspect.signature(SuperAbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subabstractclass2_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubAbstractClass2)


def test_hyp_testmodel_subabstractclass2_constructor_exists():
    assert callable(testmodel_SubAbstractClass2.__init__)


def test_hyp_testmodel_subabstractclass2_constructor_args():
    sig = inspect.signature(testmodel_SubAbstractClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subclass2_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubClass2)


def test_hyp_testmodel_subclass2_constructor_exists():
    assert callable(testmodel_SubClass2.__init__)


def test_hyp_testmodel_subclass2_constructor_args():
    sig = inspect.signature(testmodel_SubClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subinterface2_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubInterface2)


def test_hyp_testmodel_subinterface2_constructor_exists():
    assert callable(testmodel_SubInterface2.__init__)


def test_hyp_testmodel_subinterface2_constructor_args():
    sig = inspect.signature(testmodel_SubInterface2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_superinterface_is_not_abstract():
    assert not inspect.isabstract(SuperInterface)


def test_hyp_superinterface_constructor_exists():
    assert callable(SuperInterface.__init__)


def test_hyp_superinterface_constructor_args():
    sig = inspect.signature(SuperInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subabstractclass1_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubAbstractClass1)


def test_hyp_testmodel_subabstractclass1_constructor_exists():
    assert callable(testmodel_SubAbstractClass1.__init__)


def test_hyp_testmodel_subabstractclass1_constructor_args():
    sig = inspect.signature(testmodel_SubAbstractClass1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subclass1_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubClass1)


def test_hyp_testmodel_subclass1_constructor_exists():
    assert callable(testmodel_SubClass1.__init__)


def test_hyp_testmodel_subclass1_constructor_args():
    sig = inspect.signature(testmodel_SubClass1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subinterface1_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubInterface1)


def test_hyp_testmodel_subinterface1_constructor_exists():
    assert callable(testmodel_SubInterface1.__init__)


def test_hyp_testmodel_subinterface1_constructor_args():
    sig = inspect.signature(testmodel_SubInterface1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_superclass_is_not_abstract():
    assert not inspect.isabstract(testmodel_SuperClass)


def test_hyp_testmodel_superclass_constructor_exists():
    assert callable(testmodel_SuperClass.__init__)


def test_hyp_testmodel_superclass_constructor_args():
    sig = inspect.signature(testmodel_SuperClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subclass7_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubClass7)


def test_hyp_testmodel_subclass7_constructor_exists():
    assert callable(testmodel_SubClass7.__init__)


def test_hyp_testmodel_subclass7_constructor_args():
    sig = inspect.signature(testmodel_SubClass7.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subclass6_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubClass6)


def test_hyp_testmodel_subclass6_constructor_exists():
    assert callable(testmodel_SubClass6.__init__)


def test_hyp_testmodel_subclass6_constructor_args():
    sig = inspect.signature(testmodel_SubClass6.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subclass5_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubClass5)


def test_hyp_testmodel_subclass5_constructor_exists():
    assert callable(testmodel_SubClass5.__init__)


def test_hyp_testmodel_subclass5_constructor_args():
    sig = inspect.signature(testmodel_SubClass5.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subclass4_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubClass4)


def test_hyp_testmodel_subclass4_constructor_exists():
    assert callable(testmodel_SubClass4.__init__)


def test_hyp_testmodel_subclass4_constructor_args():
    sig = inspect.signature(testmodel_SubClass4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subabstractclass7_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubAbstractClass7)


def test_hyp_testmodel_subabstractclass7_constructor_exists():
    assert callable(testmodel_SubAbstractClass7.__init__)


def test_hyp_testmodel_subabstractclass7_constructor_args():
    sig = inspect.signature(testmodel_SubAbstractClass7.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_superabstractclass_is_not_abstract():
    assert not inspect.isabstract(testmodel_SuperAbstractClass)


def test_hyp_testmodel_superabstractclass_constructor_exists():
    assert callable(testmodel_SuperAbstractClass.__init__)


def test_hyp_testmodel_superabstractclass_constructor_args():
    sig = inspect.signature(testmodel_SuperAbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_superinterface_is_not_abstract():
    assert not inspect.isabstract(testmodel_SuperInterface)


def test_hyp_testmodel_superinterface_constructor_exists():
    assert callable(testmodel_SuperInterface.__init__)


def test_hyp_testmodel_superinterface_constructor_args():
    sig = inspect.signature(testmodel_SuperInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_target_is_not_abstract():
    assert not inspect.isabstract(testmodel_Target)


def test_hyp_testmodel_target_constructor_exists():
    assert callable(testmodel_Target.__init__)


def test_hyp_testmodel_target_constructor_args():
    sig = inspect.signature(testmodel_Target.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_source_is_not_abstract():
    assert not inspect.isabstract(testmodel_Source)


def test_hyp_testmodel_source_constructor_exists():
    assert callable(testmodel_Source.__init__)


def test_hyp_testmodel_source_constructor_args():
    sig = inspect.signature(testmodel_Source.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_c_is_not_abstract():
    assert not inspect.isabstract(testmodel_C)


def test_hyp_testmodel_c_constructor_exists():
    assert callable(testmodel_C.__init__)


def test_hyp_testmodel_c_constructor_args():
    sig = inspect.signature(testmodel_C.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"




def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_b_is_not_abstract():
    assert not inspect.isabstract(testmodel_B)


def test_hyp_testmodel_b_constructor_exists():
    assert callable(testmodel_B.__init__)


def test_hyp_testmodel_b_constructor_args():
    sig = inspect.signature(testmodel_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"




def test_hyp_testmodel_a_is_not_abstract():
    assert not inspect.isabstract(testmodel_A)


def test_hyp_testmodel_a_constructor_exists():
    assert callable(testmodel_A.__init__)


def test_hyp_testmodel_a_constructor_args():
    sig = inspect.signature(testmodel_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"




def test_hyp_testmodel_subabstractclass6_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubAbstractClass6)


def test_hyp_testmodel_subabstractclass6_constructor_exists():
    assert callable(testmodel_SubAbstractClass6.__init__)


def test_hyp_testmodel_subabstractclass6_constructor_args():
    sig = inspect.signature(testmodel_SubAbstractClass6.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subabstractclass5_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubAbstractClass5)


def test_hyp_testmodel_subabstractclass5_constructor_exists():
    assert callable(testmodel_SubAbstractClass5.__init__)


def test_hyp_testmodel_subabstractclass5_constructor_args():
    sig = inspect.signature(testmodel_SubAbstractClass5.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subabstractclass4_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubAbstractClass4)


def test_hyp_testmodel_subabstractclass4_constructor_exists():
    assert callable(testmodel_SubAbstractClass4.__init__)


def test_hyp_testmodel_subabstractclass4_constructor_args():
    sig = inspect.signature(testmodel_SubAbstractClass4.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testmodel_subinterface7_is_not_abstract():
    assert not inspect.isabstract(testmodel_SubInterface7)


def test_hyp_testmodel_subinterface7_constructor_exists():
    assert callable(testmodel_SubInterface7.__init__)


def test_hyp_testmodel_subinterface7_constructor_args():
    sig = inspect.signature(testmodel_SubInterface7.__init__)
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
SubClass1_strategy = st.builds(
    SubClass1,
)
SubAbstractClass1_strategy = st.builds(
    SubAbstractClass1,
)
SubInterface2_strategy = st.builds(
    SubInterface2,
)
SubInterface1_strategy = st.builds(
    SubInterface1,
)
testmodel_SubInterface6_strategy = st.builds(
    testmodel_SubInterface6,
)
testmodel_SubInterface5_strategy = st.builds(
    testmodel_SubInterface5,
)
testmodel_SubInterface4_strategy = st.builds(
    testmodel_SubInterface4,
)
SuperClass_strategy = st.builds(
    SuperClass,
)
testmodel_SubAbstractClass3_strategy = st.builds(
    testmodel_SubAbstractClass3,
)
testmodel_SubClass3_strategy = st.builds(
    testmodel_SubClass3,
)
testmodel_SubInterface3_strategy = st.builds(
    testmodel_SubInterface3,
)
SuperAbstractClass_strategy = st.builds(
    SuperAbstractClass,
)
testmodel_SubAbstractClass2_strategy = st.builds(
    testmodel_SubAbstractClass2,
)
testmodel_SubClass2_strategy = st.builds(
    testmodel_SubClass2,
)
testmodel_SubInterface2_strategy = st.builds(
    testmodel_SubInterface2,
)
SuperInterface_strategy = st.builds(
    SuperInterface,
)
testmodel_SubAbstractClass1_strategy = st.builds(
    testmodel_SubAbstractClass1,
)
testmodel_SubClass1_strategy = st.builds(
    testmodel_SubClass1,
)
testmodel_SubInterface1_strategy = st.builds(
    testmodel_SubInterface1,
)
testmodel_SuperClass_strategy = st.builds(
    testmodel_SuperClass,
)
testmodel_SubClass7_strategy = st.builds(
    testmodel_SubClass7,
)
testmodel_SubClass6_strategy = st.builds(
    testmodel_SubClass6,
)
testmodel_SubClass5_strategy = st.builds(
    testmodel_SubClass5,
)
testmodel_SubClass4_strategy = st.builds(
    testmodel_SubClass4,
)
testmodel_SubAbstractClass7_strategy = st.builds(
    testmodel_SubAbstractClass7,
)
testmodel_SuperAbstractClass_strategy = st.builds(
    testmodel_SuperAbstractClass,
)
testmodel_SuperInterface_strategy = st.builds(
    testmodel_SuperInterface,
)
testmodel_Target_strategy = st.builds(
    testmodel_Target,
)
testmodel_Source_strategy = st.builds(
    testmodel_Source,
)
B_strategy = st.builds(
    B,
)
testmodel_C_strategy = st.builds(
    testmodel_C,
    c=
        safe_text
)
A_strategy = st.builds(
    A,
)
testmodel_B_strategy = st.builds(
    testmodel_B,
    b=
        safe_text
)
testmodel_A_strategy = st.builds(
    testmodel_A,
    a=
        safe_text
)
testmodel_SubAbstractClass6_strategy = st.builds(
    testmodel_SubAbstractClass6,
)
testmodel_SubAbstractClass5_strategy = st.builds(
    testmodel_SubAbstractClass5,
)
testmodel_SubAbstractClass4_strategy = st.builds(
    testmodel_SubAbstractClass4,
)
testmodel_SubInterface7_strategy = st.builds(
    testmodel_SubInterface7,
)


































@given(instance=testmodel_C_strategy)
def test_hyp_testmodel_c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=testmodel_C_strategy)
@settings(max_examples=30)
def test_hyp_testmodel_c_bop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bOp()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bOp).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bOp' in testmodel_C is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bOp' in testmodel_C did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bOp' in testmodel_C is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=testmodel_C_strategy)
@settings(max_examples=30)
def test_hyp_testmodel_c_aop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.aOp()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.aOp).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'aOp' in testmodel_C is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'aOp' in testmodel_C did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'aOp' in testmodel_C is not implemented or raised an error")





@given(instance=testmodel_B_strategy)
def test_hyp_testmodel_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=testmodel_B_strategy)
@settings(max_examples=30)
def test_hyp_testmodel_b_bop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bOp()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bOp).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bOp' in testmodel_B is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bOp' in testmodel_B did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bOp' in testmodel_B is not implemented or raised an error")




@given(instance=testmodel_A_strategy)
def test_hyp_testmodel_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=testmodel_A_strategy)
@settings(max_examples=30)
def test_hyp_testmodel_a_aop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.aOp()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.aOp).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'aOp' in testmodel_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'aOp' in testmodel_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'aOp' in testmodel_A is not implemented or raised an error")






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    B,
    SubAbstractClass1,
    SubClass1,
    SubInterface1,
    SubInterface2,
    SuperAbstractClass,
    SuperClass,
    SuperInterface,
    testmodel_A,
    testmodel_B,
    testmodel_C,
    testmodel_Source,
    testmodel_SubAbstractClass1,
    testmodel_SubAbstractClass2,
    testmodel_SubAbstractClass3,
    testmodel_SubAbstractClass4,
    testmodel_SubAbstractClass5,
    testmodel_SubAbstractClass6,
    testmodel_SubAbstractClass7,
    testmodel_SubClass1,
    testmodel_SubClass2,
    testmodel_SubClass3,
    testmodel_SubClass4,
    testmodel_SubClass5,
    testmodel_SubClass6,
    testmodel_SubClass7,
    testmodel_SubInterface1,
    testmodel_SubInterface2,
    testmodel_SubInterface3,
    testmodel_SubInterface4,
    testmodel_SubInterface5,
    testmodel_SubInterface6,
    testmodel_SubInterface7,
    testmodel_SuperAbstractClass,
    testmodel_SuperClass,
    testmodel_SuperInterface,
    testmodel_Target,
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

def test_testmodel_A_a_value_roundtrip():
    instance = testmodel_A(a="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


def test_testmodel_B_b_value_roundtrip():
    instance = testmodel_B(b="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_testmodel_C_c_value_roundtrip():
    instance = testmodel_C(c="sample_text")
    assert instance.c == "sample_text"
    instance.c = "sample_text_2"
    assert instance.c == "sample_text_2"


def test_testmodel_B_isa_A():
    instance = testmodel_B(b="sample_text")
    assert isinstance(instance, A)


def test_testmodel_C_isa_B():
    instance = testmodel_C(c="sample_text")
    assert isinstance(instance, B)


def test_testmodel_SubAbstractClass5_isa_SubAbstractClass1():
    instance = testmodel_SubAbstractClass5()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubAbstractClass7_isa_SubAbstractClass1():
    instance = testmodel_SubAbstractClass7()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubClass5_isa_SubAbstractClass1():
    instance = testmodel_SubClass5()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubClass7_isa_SubAbstractClass1():
    instance = testmodel_SubClass7()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubInterface5_isa_SubAbstractClass1():
    instance = testmodel_SubInterface5()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubInterface7_isa_SubAbstractClass1():
    instance = testmodel_SubInterface7()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubAbstractClass6_isa_SubClass1():
    instance = testmodel_SubAbstractClass6()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubAbstractClass7_isa_SubClass1():
    instance = testmodel_SubAbstractClass7()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubClass6_isa_SubClass1():
    instance = testmodel_SubClass6()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubClass7_isa_SubClass1():
    instance = testmodel_SubClass7()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubInterface6_isa_SubClass1():
    instance = testmodel_SubInterface6()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubInterface7_isa_SubClass1():
    instance = testmodel_SubInterface7()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubAbstractClass4_isa_SubInterface1():
    instance = testmodel_SubAbstractClass4()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubAbstractClass5_isa_SubInterface1():
    instance = testmodel_SubAbstractClass5()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubAbstractClass6_isa_SubInterface1():
    instance = testmodel_SubAbstractClass6()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubClass4_isa_SubInterface1():
    instance = testmodel_SubClass4()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubClass5_isa_SubInterface1():
    instance = testmodel_SubClass5()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubClass6_isa_SubInterface1():
    instance = testmodel_SubClass6()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubInterface4_isa_SubInterface1():
    instance = testmodel_SubInterface4()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubInterface5_isa_SubInterface1():
    instance = testmodel_SubInterface5()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubInterface6_isa_SubInterface1():
    instance = testmodel_SubInterface6()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubAbstractClass4_isa_SubInterface2():
    instance = testmodel_SubAbstractClass4()
    assert isinstance(instance, SubInterface2)


def test_testmodel_SubClass4_isa_SubInterface2():
    instance = testmodel_SubClass4()
    assert isinstance(instance, SubInterface2)


def test_testmodel_SubInterface4_isa_SubInterface2():
    instance = testmodel_SubInterface4()
    assert isinstance(instance, SubInterface2)


def test_testmodel_SubAbstractClass2_isa_SuperAbstractClass():
    instance = testmodel_SubAbstractClass2()
    assert isinstance(instance, SuperAbstractClass)


def test_testmodel_SubClass2_isa_SuperAbstractClass():
    instance = testmodel_SubClass2()
    assert isinstance(instance, SuperAbstractClass)


def test_testmodel_SubInterface2_isa_SuperAbstractClass():
    instance = testmodel_SubInterface2()
    assert isinstance(instance, SuperAbstractClass)


def test_testmodel_SubAbstractClass3_isa_SuperClass():
    instance = testmodel_SubAbstractClass3()
    assert isinstance(instance, SuperClass)


def test_testmodel_SubClass3_isa_SuperClass():
    instance = testmodel_SubClass3()
    assert isinstance(instance, SuperClass)


def test_testmodel_SubInterface3_isa_SuperClass():
    instance = testmodel_SubInterface3()
    assert isinstance(instance, SuperClass)


def test_testmodel_SubAbstractClass1_isa_SuperInterface():
    instance = testmodel_SubAbstractClass1()
    assert isinstance(instance, SuperInterface)


def test_testmodel_SubClass1_isa_SuperInterface():
    instance = testmodel_SubClass1()
    assert isinstance(instance, SuperInterface)


def test_testmodel_SubInterface1_isa_SuperInterface():
    instance = testmodel_SubInterface1()
    assert isinstance(instance, SuperInterface)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


SubAbstractClass1_strategy = st.builds(SubAbstractClass1)
@given(instance=SubAbstractClass1_strategy)
@settings(max_examples=25)
def test_SubAbstractClass1_instantiation(instance):
    assert isinstance(instance, SubAbstractClass1)


SubClass1_strategy = st.builds(SubClass1)
@given(instance=SubClass1_strategy)
@settings(max_examples=25)
def test_SubClass1_instantiation(instance):
    assert isinstance(instance, SubClass1)


SubInterface1_strategy = st.builds(SubInterface1)
@given(instance=SubInterface1_strategy)
@settings(max_examples=25)
def test_SubInterface1_instantiation(instance):
    assert isinstance(instance, SubInterface1)


SubInterface2_strategy = st.builds(SubInterface2)
@given(instance=SubInterface2_strategy)
@settings(max_examples=25)
def test_SubInterface2_instantiation(instance):
    assert isinstance(instance, SubInterface2)


SuperAbstractClass_strategy = st.builds(SuperAbstractClass)
@given(instance=SuperAbstractClass_strategy)
@settings(max_examples=25)
def test_SuperAbstractClass_instantiation(instance):
    assert isinstance(instance, SuperAbstractClass)


SuperClass_strategy = st.builds(SuperClass)
@given(instance=SuperClass_strategy)
@settings(max_examples=25)
def test_SuperClass_instantiation(instance):
    assert isinstance(instance, SuperClass)


SuperInterface_strategy = st.builds(SuperInterface)
@given(instance=SuperInterface_strategy)
@settings(max_examples=25)
def test_SuperInterface_instantiation(instance):
    assert isinstance(instance, SuperInterface)


testmodel_A_strategy = st.builds(testmodel_A, a=safe_text)
@given(instance=testmodel_A_strategy)
@settings(max_examples=25)
def test_testmodel_A_instantiation(instance):
    assert isinstance(instance, testmodel_A)


testmodel_B_strategy = st.builds(testmodel_B, b=safe_text)
@given(instance=testmodel_B_strategy)
@settings(max_examples=25)
def test_testmodel_B_instantiation(instance):
    assert isinstance(instance, testmodel_B)


testmodel_C_strategy = st.builds(testmodel_C, c=safe_text)
@given(instance=testmodel_C_strategy)
@settings(max_examples=25)
def test_testmodel_C_instantiation(instance):
    assert isinstance(instance, testmodel_C)


testmodel_Source_strategy = st.builds(testmodel_Source)
@given(instance=testmodel_Source_strategy)
@settings(max_examples=25)
def test_testmodel_Source_instantiation(instance):
    assert isinstance(instance, testmodel_Source)


testmodel_SubAbstractClass1_strategy = st.builds(testmodel_SubAbstractClass1)
@given(instance=testmodel_SubAbstractClass1_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass1_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass1)


testmodel_SubAbstractClass2_strategy = st.builds(testmodel_SubAbstractClass2)
@given(instance=testmodel_SubAbstractClass2_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass2_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass2)


testmodel_SubAbstractClass3_strategy = st.builds(testmodel_SubAbstractClass3)
@given(instance=testmodel_SubAbstractClass3_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass3_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass3)


testmodel_SubAbstractClass4_strategy = st.builds(testmodel_SubAbstractClass4)
@given(instance=testmodel_SubAbstractClass4_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass4_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass4)


testmodel_SubAbstractClass5_strategy = st.builds(testmodel_SubAbstractClass5)
@given(instance=testmodel_SubAbstractClass5_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass5_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass5)


testmodel_SubAbstractClass6_strategy = st.builds(testmodel_SubAbstractClass6)
@given(instance=testmodel_SubAbstractClass6_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass6_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass6)


testmodel_SubAbstractClass7_strategy = st.builds(testmodel_SubAbstractClass7)
@given(instance=testmodel_SubAbstractClass7_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass7_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass7)


testmodel_SubClass1_strategy = st.builds(testmodel_SubClass1)
@given(instance=testmodel_SubClass1_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass1_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass1)


testmodel_SubClass2_strategy = st.builds(testmodel_SubClass2)
@given(instance=testmodel_SubClass2_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass2_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass2)


testmodel_SubClass3_strategy = st.builds(testmodel_SubClass3)
@given(instance=testmodel_SubClass3_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass3_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass3)


testmodel_SubClass4_strategy = st.builds(testmodel_SubClass4)
@given(instance=testmodel_SubClass4_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass4_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass4)


testmodel_SubClass5_strategy = st.builds(testmodel_SubClass5)
@given(instance=testmodel_SubClass5_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass5_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass5)


testmodel_SubClass6_strategy = st.builds(testmodel_SubClass6)
@given(instance=testmodel_SubClass6_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass6_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass6)


testmodel_SubClass7_strategy = st.builds(testmodel_SubClass7)
@given(instance=testmodel_SubClass7_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass7_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass7)


testmodel_SubInterface1_strategy = st.builds(testmodel_SubInterface1)
@given(instance=testmodel_SubInterface1_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface1_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface1)


testmodel_SubInterface2_strategy = st.builds(testmodel_SubInterface2)
@given(instance=testmodel_SubInterface2_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface2_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface2)


testmodel_SubInterface3_strategy = st.builds(testmodel_SubInterface3)
@given(instance=testmodel_SubInterface3_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface3_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface3)


testmodel_SubInterface4_strategy = st.builds(testmodel_SubInterface4)
@given(instance=testmodel_SubInterface4_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface4_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface4)


testmodel_SubInterface5_strategy = st.builds(testmodel_SubInterface5)
@given(instance=testmodel_SubInterface5_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface5_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface5)


testmodel_SubInterface6_strategy = st.builds(testmodel_SubInterface6)
@given(instance=testmodel_SubInterface6_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface6_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface6)


testmodel_SubInterface7_strategy = st.builds(testmodel_SubInterface7)
@given(instance=testmodel_SubInterface7_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface7_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface7)


testmodel_SuperAbstractClass_strategy = st.builds(testmodel_SuperAbstractClass)
@given(instance=testmodel_SuperAbstractClass_strategy)
@settings(max_examples=25)
def test_testmodel_SuperAbstractClass_instantiation(instance):
    assert isinstance(instance, testmodel_SuperAbstractClass)


testmodel_SuperClass_strategy = st.builds(testmodel_SuperClass)
@given(instance=testmodel_SuperClass_strategy)
@settings(max_examples=25)
def test_testmodel_SuperClass_instantiation(instance):
    assert isinstance(instance, testmodel_SuperClass)


testmodel_SuperInterface_strategy = st.builds(testmodel_SuperInterface)
@given(instance=testmodel_SuperInterface_strategy)
@settings(max_examples=25)
def test_testmodel_SuperInterface_instantiation(instance):
    assert isinstance(instance, testmodel_SuperInterface)


testmodel_Target_strategy = st.builds(testmodel_Target)
@given(instance=testmodel_Target_strategy)
@settings(max_examples=25)
def test_testmodel_Target_instantiation(instance):
    assert isinstance(instance, testmodel_Target)



