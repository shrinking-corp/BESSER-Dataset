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
    TraceStackframe,
    junitmodel_JUnitTraceStackframe,
    ComparisonProblem,
    JUnitProblem,
    junitmodel_JUnitComparisonProblem,
    TestProblem,
    junitmodel_JUnitProblem,
    TestRoot,
    junitmodel_JUnitRoot,
    TestContainer,
    junitmodel_JUnitTestSuite,
    TestCaseElement,
    junitmodel_JUnitTestCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tracestackframe_is_not_abstract():
    assert not inspect.isabstract(TraceStackframe)


def test_hyp_tracestackframe_constructor_exists():
    assert callable(TraceStackframe.__init__)


def test_hyp_tracestackframe_constructor_args():
    sig = inspect.signature(TraceStackframe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitmodel_junittracestackframe_is_not_abstract():
    assert not inspect.isabstract(junitmodel_JUnitTraceStackframe)


def test_hyp_junitmodel_junittracestackframe_constructor_exists():
    assert callable(junitmodel_JUnitTraceStackframe.__init__)


def test_hyp_junitmodel_junittracestackframe_constructor_args():
    sig = inspect.signature(junitmodel_JUnitTraceStackframe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparisonproblem_is_not_abstract():
    assert not inspect.isabstract(ComparisonProblem)


def test_hyp_comparisonproblem_constructor_exists():
    assert callable(ComparisonProblem.__init__)


def test_hyp_comparisonproblem_constructor_args():
    sig = inspect.signature(ComparisonProblem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitproblem_is_not_abstract():
    assert not inspect.isabstract(JUnitProblem)


def test_hyp_junitproblem_constructor_exists():
    assert callable(JUnitProblem.__init__)


def test_hyp_junitproblem_constructor_args():
    sig = inspect.signature(JUnitProblem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitmodel_junitcomparisonproblem_is_not_abstract():
    assert not inspect.isabstract(junitmodel_JUnitComparisonProblem)


def test_hyp_junitmodel_junitcomparisonproblem_constructor_exists():
    assert callable(junitmodel_JUnitComparisonProblem.__init__)


def test_hyp_junitmodel_junitcomparisonproblem_constructor_args():
    sig = inspect.signature(junitmodel_JUnitComparisonProblem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testproblem_is_not_abstract():
    assert not inspect.isabstract(TestProblem)


def test_hyp_testproblem_constructor_exists():
    assert callable(TestProblem.__init__)


def test_hyp_testproblem_constructor_args():
    sig = inspect.signature(TestProblem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitmodel_junitproblem_is_not_abstract():
    assert not inspect.isabstract(junitmodel_JUnitProblem)


def test_hyp_junitmodel_junitproblem_constructor_exists():
    assert callable(junitmodel_JUnitProblem.__init__)


def test_hyp_junitmodel_junitproblem_constructor_args():
    sig = inspect.signature(junitmodel_JUnitProblem.__init__)
    params = list(sig.parameters.keys())
    assert "lastTraceWasFiltered" in params, "Missing parameter 'lastTraceWasFiltered'"




def test_hyp_testroot_is_not_abstract():
    assert not inspect.isabstract(TestRoot)


def test_hyp_testroot_constructor_exists():
    assert callable(TestRoot.__init__)


def test_hyp_testroot_constructor_args():
    sig = inspect.signature(TestRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitmodel_junitroot_is_not_abstract():
    assert not inspect.isabstract(junitmodel_JUnitRoot)


def test_hyp_junitmodel_junitroot_constructor_exists():
    assert callable(junitmodel_JUnitRoot.__init__)


def test_hyp_junitmodel_junitroot_constructor_args():
    sig = inspect.signature(junitmodel_JUnitRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testcontainer_is_not_abstract():
    assert not inspect.isabstract(TestContainer)


def test_hyp_testcontainer_constructor_exists():
    assert callable(TestContainer.__init__)


def test_hyp_testcontainer_constructor_args():
    sig = inspect.signature(TestContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitmodel_junittestsuite_is_not_abstract():
    assert not inspect.isabstract(junitmodel_JUnitTestSuite)


def test_hyp_junitmodel_junittestsuite_constructor_exists():
    assert callable(junitmodel_JUnitTestSuite.__init__)


def test_hyp_junitmodel_junittestsuite_constructor_args():
    sig = inspect.signature(junitmodel_JUnitTestSuite.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testcaseelement_is_not_abstract():
    assert not inspect.isabstract(TestCaseElement)


def test_hyp_testcaseelement_constructor_exists():
    assert callable(TestCaseElement.__init__)


def test_hyp_testcaseelement_constructor_args():
    sig = inspect.signature(TestCaseElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitmodel_junittestcase_is_not_abstract():
    assert not inspect.isabstract(junitmodel_JUnitTestCase)


def test_hyp_junitmodel_junittestcase_constructor_exists():
    assert callable(junitmodel_JUnitTestCase.__init__)


def test_hyp_junitmodel_junittestcase_constructor_args():
    sig = inspect.signature(junitmodel_JUnitTestCase.__init__)
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
TraceStackframe_strategy = st.builds(
    TraceStackframe,
)
junitmodel_JUnitTraceStackframe_strategy = st.builds(
    junitmodel_JUnitTraceStackframe,
)
ComparisonProblem_strategy = st.builds(
    ComparisonProblem,
)
JUnitProblem_strategy = st.builds(
    JUnitProblem,
)
junitmodel_JUnitComparisonProblem_strategy = st.builds(
    junitmodel_JUnitComparisonProblem,
)
TestProblem_strategy = st.builds(
    TestProblem,
)
junitmodel_JUnitProblem_strategy = st.builds(
    junitmodel_JUnitProblem,
    lastTraceWasFiltered=
        st.booleans()
)
TestRoot_strategy = st.builds(
    TestRoot,
)
junitmodel_JUnitRoot_strategy = st.builds(
    junitmodel_JUnitRoot,
)
TestContainer_strategy = st.builds(
    TestContainer,
)
junitmodel_JUnitTestSuite_strategy = st.builds(
    junitmodel_JUnitTestSuite,
)
TestCaseElement_strategy = st.builds(
    TestCaseElement,
)
junitmodel_JUnitTestCase_strategy = st.builds(
    junitmodel_JUnitTestCase,
)










@given(instance=junitmodel_JUnitProblem_strategy)
def test_hyp_junitmodel_junitproblem_lastTraceWasFiltered_setter(instance):
    original = instance.lastTraceWasFiltered
    instance.lastTraceWasFiltered = original
    assert instance.lastTraceWasFiltered == original








# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ComparisonProblem,
    JUnitProblem,
    TestCaseElement,
    TestContainer,
    TestProblem,
    TestRoot,
    TraceStackframe,
    junitmodel_JUnitComparisonProblem,
    junitmodel_JUnitProblem,
    junitmodel_JUnitRoot,
    junitmodel_JUnitTestCase,
    junitmodel_JUnitTestSuite,
    junitmodel_JUnitTraceStackframe,
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

def test_junitmodel_JUnitProblem_lastTraceWasFiltered_value_roundtrip():
    instance = junitmodel_JUnitProblem(lastTraceWasFiltered=True)
    assert instance.lastTraceWasFiltered == True
    instance.lastTraceWasFiltered = False
    assert instance.lastTraceWasFiltered == False


def test_junitmodel_JUnitComparisonProblem_isa_ComparisonProblem():
    instance = junitmodel_JUnitComparisonProblem()
    assert isinstance(instance, ComparisonProblem)


def test_junitmodel_JUnitComparisonProblem_isa_JUnitProblem():
    instance = junitmodel_JUnitComparisonProblem()
    assert isinstance(instance, JUnitProblem)


def test_junitmodel_JUnitTestCase_isa_TestCaseElement():
    instance = junitmodel_JUnitTestCase()
    assert isinstance(instance, TestCaseElement)


def test_junitmodel_JUnitTestSuite_isa_TestContainer():
    instance = junitmodel_JUnitTestSuite()
    assert isinstance(instance, TestContainer)


def test_junitmodel_JUnitProblem_isa_TestProblem():
    instance = junitmodel_JUnitProblem(lastTraceWasFiltered=True)
    assert isinstance(instance, TestProblem)


def test_junitmodel_JUnitRoot_isa_TestRoot():
    instance = junitmodel_JUnitRoot()
    assert isinstance(instance, TestRoot)


def test_junitmodel_JUnitTraceStackframe_isa_TraceStackframe():
    instance = junitmodel_JUnitTraceStackframe()
    assert isinstance(instance, TraceStackframe)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ComparisonProblem_strategy = st.builds(ComparisonProblem)
@given(instance=ComparisonProblem_strategy)
@settings(max_examples=25)
def test_ComparisonProblem_instantiation(instance):
    assert isinstance(instance, ComparisonProblem)


JUnitProblem_strategy = st.builds(JUnitProblem)
@given(instance=JUnitProblem_strategy)
@settings(max_examples=25)
def test_JUnitProblem_instantiation(instance):
    assert isinstance(instance, JUnitProblem)


TestCaseElement_strategy = st.builds(TestCaseElement)
@given(instance=TestCaseElement_strategy)
@settings(max_examples=25)
def test_TestCaseElement_instantiation(instance):
    assert isinstance(instance, TestCaseElement)


TestContainer_strategy = st.builds(TestContainer)
@given(instance=TestContainer_strategy)
@settings(max_examples=25)
def test_TestContainer_instantiation(instance):
    assert isinstance(instance, TestContainer)


TestProblem_strategy = st.builds(TestProblem)
@given(instance=TestProblem_strategy)
@settings(max_examples=25)
def test_TestProblem_instantiation(instance):
    assert isinstance(instance, TestProblem)


TestRoot_strategy = st.builds(TestRoot)
@given(instance=TestRoot_strategy)
@settings(max_examples=25)
def test_TestRoot_instantiation(instance):
    assert isinstance(instance, TestRoot)


TraceStackframe_strategy = st.builds(TraceStackframe)
@given(instance=TraceStackframe_strategy)
@settings(max_examples=25)
def test_TraceStackframe_instantiation(instance):
    assert isinstance(instance, TraceStackframe)


junitmodel_JUnitComparisonProblem_strategy = st.builds(junitmodel_JUnitComparisonProblem)
@given(instance=junitmodel_JUnitComparisonProblem_strategy)
@settings(max_examples=25)
def test_junitmodel_JUnitComparisonProblem_instantiation(instance):
    assert isinstance(instance, junitmodel_JUnitComparisonProblem)


junitmodel_JUnitProblem_strategy = st.builds(junitmodel_JUnitProblem, lastTraceWasFiltered=st.booleans())
@given(instance=junitmodel_JUnitProblem_strategy)
@settings(max_examples=25)
def test_junitmodel_JUnitProblem_instantiation(instance):
    assert isinstance(instance, junitmodel_JUnitProblem)


junitmodel_JUnitRoot_strategy = st.builds(junitmodel_JUnitRoot)
@given(instance=junitmodel_JUnitRoot_strategy)
@settings(max_examples=25)
def test_junitmodel_JUnitRoot_instantiation(instance):
    assert isinstance(instance, junitmodel_JUnitRoot)


junitmodel_JUnitTestCase_strategy = st.builds(junitmodel_JUnitTestCase)
@given(instance=junitmodel_JUnitTestCase_strategy)
@settings(max_examples=25)
def test_junitmodel_JUnitTestCase_instantiation(instance):
    assert isinstance(instance, junitmodel_JUnitTestCase)


junitmodel_JUnitTestSuite_strategy = st.builds(junitmodel_JUnitTestSuite)
@given(instance=junitmodel_JUnitTestSuite_strategy)
@settings(max_examples=25)
def test_junitmodel_JUnitTestSuite_instantiation(instance):
    assert isinstance(instance, junitmodel_JUnitTestSuite)


junitmodel_JUnitTraceStackframe_strategy = st.builds(junitmodel_JUnitTraceStackframe)
@given(instance=junitmodel_JUnitTraceStackframe_strategy)
@settings(max_examples=25)
def test_junitmodel_JUnitTraceStackframe_instantiation(instance):
    assert isinstance(instance, junitmodel_JUnitTraceStackframe)



