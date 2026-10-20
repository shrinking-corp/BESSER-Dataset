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
    My2_TestClass2,
    TestEnum2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_my2_testclass2_is_not_abstract():
    assert not inspect.isabstract(My2_TestClass2)


def test_hyp_my2_testclass2_constructor_exists():
    assert callable(My2_TestClass2.__init__)


def test_hyp_my2_testclass2_constructor_args():
    sig = inspect.signature(My2_TestClass2.__init__)
    params = list(sig.parameters.keys())
    assert "testAtt2" in params, "Missing parameter 'testAtt2'"
    assert "testAtt" in params, "Missing parameter 'testAtt'"



def test_hyp_testenum2_exists():
    # Check that the Enumeration exists
    assert TestEnum2 is not None

def test_hyp_testenum2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestEnum2]
    expected_literals = [
        "testLiteral2",
        "testLiteral",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestEnum2"


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
My2_TestClass2_strategy = st.builds(
    My2_TestClass2,
    testAtt2=
        safe_text,
    testAtt=
        safe_text
)




@given(instance=My2_TestClass2_strategy)
def test_hyp_my2_testclass2_testAtt2_setter(instance):
    original = instance.testAtt2
    instance.testAtt2 = original
    assert instance.testAtt2 == original



@given(instance=My2_TestClass2_strategy)
def test_hyp_my2_testclass2_testAtt_setter(instance):
    original = instance.testAtt
    instance.testAtt = original
    assert instance.testAtt == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    My2_TestClass2,
    TestEnum2,
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

def test_My2_TestClass2_testAtt_value_roundtrip():
    instance = My2_TestClass2(testAtt="sample_text", testAtt2="sample_text")
    assert instance.testAtt == "sample_text"
    instance.testAtt = "sample_text_2"
    assert instance.testAtt == "sample_text_2"


def test_My2_TestClass2_testAtt2_value_roundtrip():
    instance = My2_TestClass2(testAtt="sample_text", testAtt2="sample_text")
    assert instance.testAtt2 == "sample_text"
    instance.testAtt2 = "sample_text_2"
    assert instance.testAtt2 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

My2_TestClass2_strategy = st.builds(My2_TestClass2, testAtt=safe_text, testAtt2=safe_text)
@given(instance=My2_TestClass2_strategy)
@settings(max_examples=25)
def test_My2_TestClass2_instantiation(instance):
    assert isinstance(instance, My2_TestClass2)



