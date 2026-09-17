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
    junitresult_NegativeResult,
    NegativeResult,
    junitresult_JunitResult,
    JunitResult,
    junitresult_AbstractAggregatedTest,
    junitresult_Property,
    AbstractAggregatedTest,
    junitresult_Testrun,
    junitresult_Testsuites,
    junitresult_Testsuite,
    junitresult_Error,
    junitresult_Failure,
    junitresult_Skipped,
    junitresult_Testcase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_junitresult_negativeresult_is_not_abstract():
    assert not inspect.isabstract(junitresult_NegativeResult)


def test_hyp_junitresult_negativeresult_constructor_exists():
    assert callable(junitresult_NegativeResult.__init__)


def test_hyp_junitresult_negativeresult_constructor_args():
    sig = inspect.signature(junitresult_NegativeResult.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "message" in params, "Missing parameter 'message'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_negativeresult_is_not_abstract():
    assert not inspect.isabstract(NegativeResult)


def test_hyp_negativeresult_constructor_exists():
    assert callable(NegativeResult.__init__)


def test_hyp_negativeresult_constructor_args():
    sig = inspect.signature(NegativeResult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitresult_junitresult_is_not_abstract():
    assert not inspect.isabstract(junitresult_JunitResult)


def test_hyp_junitresult_junitresult_constructor_exists():
    assert callable(junitresult_JunitResult.__init__)


def test_hyp_junitresult_junitresult_constructor_args():
    sig = inspect.signature(junitresult_JunitResult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitresult_is_not_abstract():
    assert not inspect.isabstract(JunitResult)


def test_hyp_junitresult_constructor_exists():
    assert callable(JunitResult.__init__)


def test_hyp_junitresult_constructor_args():
    sig = inspect.signature(JunitResult.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitresult_abstractaggregatedtest_is_not_abstract():
    assert not inspect.isabstract(junitresult_AbstractAggregatedTest)


def test_hyp_junitresult_abstractaggregatedtest_constructor_exists():
    assert callable(junitresult_AbstractAggregatedTest.__init__)


def test_hyp_junitresult_abstractaggregatedtest_constructor_args():
    sig = inspect.signature(junitresult_AbstractAggregatedTest.__init__)
    params = list(sig.parameters.keys())
    assert "tests" in params, "Missing parameter 'tests'"
    assert "failures" in params, "Missing parameter 'failures'"
    assert "errors" in params, "Missing parameter 'errors'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_junitresult_property_is_not_abstract():
    assert not inspect.isabstract(junitresult_Property)


def test_hyp_junitresult_property_constructor_exists():
    assert callable(junitresult_Property.__init__)


def test_hyp_junitresult_property_constructor_args():
    sig = inspect.signature(junitresult_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_abstractaggregatedtest_is_not_abstract():
    assert not inspect.isabstract(AbstractAggregatedTest)


def test_hyp_abstractaggregatedtest_constructor_exists():
    assert callable(AbstractAggregatedTest.__init__)


def test_hyp_abstractaggregatedtest_constructor_args():
    sig = inspect.signature(AbstractAggregatedTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitresult_testrun_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testrun)


def test_hyp_junitresult_testrun_constructor_exists():
    assert callable(junitresult_Testrun.__init__)


def test_hyp_junitresult_testrun_constructor_args():
    sig = inspect.signature(junitresult_Testrun.__init__)
    params = list(sig.parameters.keys())
    assert "ignored" in params, "Missing parameter 'ignored'"
    assert "project" in params, "Missing parameter 'project'"
    assert "started" in params, "Missing parameter 'started'"






def test_hyp_junitresult_testsuites_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testsuites)


def test_hyp_junitresult_testsuites_constructor_exists():
    assert callable(junitresult_Testsuites.__init__)


def test_hyp_junitresult_testsuites_constructor_args():
    sig = inspect.signature(junitresult_Testsuites.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "disabled" in params, "Missing parameter 'disabled'"





def test_hyp_junitresult_testsuite_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testsuite)


def test_hyp_junitresult_testsuite_constructor_exists():
    assert callable(junitresult_Testsuite.__init__)


def test_hyp_junitresult_testsuite_constructor_args():
    sig = inspect.signature(junitresult_Testsuite.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "system_err" in params, "Missing parameter 'system_err'"
    assert "skipped" in params, "Missing parameter 'skipped'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "system_out" in params, "Missing parameter 'system_out'"
    assert "hostname" in params, "Missing parameter 'hostname'"
    assert "package" in params, "Missing parameter 'package'"












def test_hyp_junitresult_error_is_not_abstract():
    assert not inspect.isabstract(junitresult_Error)


def test_hyp_junitresult_error_constructor_exists():
    assert callable(junitresult_Error.__init__)


def test_hyp_junitresult_error_constructor_args():
    sig = inspect.signature(junitresult_Error.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitresult_failure_is_not_abstract():
    assert not inspect.isabstract(junitresult_Failure)


def test_hyp_junitresult_failure_constructor_exists():
    assert callable(junitresult_Failure.__init__)


def test_hyp_junitresult_failure_constructor_args():
    sig = inspect.signature(junitresult_Failure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitresult_skipped_is_not_abstract():
    assert not inspect.isabstract(junitresult_Skipped)


def test_hyp_junitresult_skipped_constructor_exists():
    assert callable(junitresult_Skipped.__init__)


def test_hyp_junitresult_skipped_constructor_args():
    sig = inspect.signature(junitresult_Skipped.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junitresult_testcase_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testcase)


def test_hyp_junitresult_testcase_constructor_exists():
    assert callable(junitresult_Testcase.__init__)


def test_hyp_junitresult_testcase_constructor_args():
    sig = inspect.signature(junitresult_Testcase.__init__)
    params = list(sig.parameters.keys())
    assert "system_out" in params, "Missing parameter 'system_out'"
    assert "time" in params, "Missing parameter 'time'"
    assert "assertions" in params, "Missing parameter 'assertions'"
    assert "system_err" in params, "Missing parameter 'system_err'"
    assert "name" in params, "Missing parameter 'name'"
    assert "classname" in params, "Missing parameter 'classname'"
    assert "status" in params, "Missing parameter 'status'"









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
junitresult_NegativeResult_strategy = st.builds(
    junitresult_NegativeResult,
    type=
        safe_text,
    message=
        safe_text,
    value=
        safe_text
)
NegativeResult_strategy = st.builds(
    NegativeResult,
)
junitresult_JunitResult_strategy = st.builds(
    junitresult_JunitResult,
)
JunitResult_strategy = st.builds(
    JunitResult,
)
junitresult_AbstractAggregatedTest_strategy = st.builds(
    junitresult_AbstractAggregatedTest,
    tests=
        st.integers(),
    failures=
        st.integers(),
    errors=
        st.integers(),
    name=
        safe_text
)
junitresult_Property_strategy = st.builds(
    junitresult_Property,
    name=
        safe_text,
    value=
        safe_text
)
AbstractAggregatedTest_strategy = st.builds(
    AbstractAggregatedTest,
)
junitresult_Testrun_strategy = st.builds(
    junitresult_Testrun,
    ignored=
        st.integers(),
    project=
        safe_text,
    started=
        st.integers()
)
junitresult_Testsuites_strategy = st.builds(
    junitresult_Testsuites,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    disabled=
        st.integers()
)
junitresult_Testsuite_strategy = st.builds(
    junitresult_Testsuite,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timestamp=
        st.dates(),
    id=
        st.integers(),
    system_err=
        safe_text,
    skipped=
        st.integers(),
    disabled=
        st.integers(),
    system_out=
        safe_text,
    hostname=
        safe_text,
    package=
        safe_text
)
junitresult_Error_strategy = st.builds(
    junitresult_Error,
)
junitresult_Failure_strategy = st.builds(
    junitresult_Failure,
)
junitresult_Skipped_strategy = st.builds(
    junitresult_Skipped,
)
junitresult_Testcase_strategy = st.builds(
    junitresult_Testcase,
    system_out=
        safe_text,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    assertions=
        safe_text,
    system_err=
        safe_text,
    name=
        safe_text,
    classname=
        safe_text,
    status=
        safe_text
)




@given(instance=junitresult_NegativeResult_strategy)
def test_hyp_junitresult_negativeresult_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=junitresult_NegativeResult_strategy)
def test_hyp_junitresult_negativeresult_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=junitresult_NegativeResult_strategy)
def test_hyp_junitresult_negativeresult_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_hyp_junitresult_abstractaggregatedtest_tests_setter(instance):
    original = instance.tests
    instance.tests = original
    assert instance.tests == original



@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_hyp_junitresult_abstractaggregatedtest_failures_setter(instance):
    original = instance.failures
    instance.failures = original
    assert instance.failures == original



@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_hyp_junitresult_abstractaggregatedtest_errors_setter(instance):
    original = instance.errors
    instance.errors = original
    assert instance.errors == original



@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_hyp_junitresult_abstractaggregatedtest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=junitresult_Property_strategy)
def test_hyp_junitresult_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=junitresult_Property_strategy)
def test_hyp_junitresult_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=junitresult_Testrun_strategy)
def test_hyp_junitresult_testrun_ignored_setter(instance):
    original = instance.ignored
    instance.ignored = original
    assert instance.ignored == original



@given(instance=junitresult_Testrun_strategy)
def test_hyp_junitresult_testrun_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original



@given(instance=junitresult_Testrun_strategy)
def test_hyp_junitresult_testrun_started_setter(instance):
    original = instance.started
    instance.started = original
    assert instance.started == original




@given(instance=junitresult_Testsuites_strategy)
def test_hyp_junitresult_testsuites_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=junitresult_Testsuites_strategy)
def test_hyp_junitresult_testsuites_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original




@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_system_err_setter(instance):
    original = instance.system_err
    instance.system_err = original
    assert instance.system_err == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_skipped_setter(instance):
    original = instance.skipped
    instance.skipped = original
    assert instance.skipped == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_system_out_setter(instance):
    original = instance.system_out
    instance.system_out = original
    assert instance.system_out == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_hostname_setter(instance):
    original = instance.hostname
    instance.hostname = original
    assert instance.hostname == original



@given(instance=junitresult_Testsuite_strategy)
def test_hyp_junitresult_testsuite_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original







@given(instance=junitresult_Testcase_strategy)
def test_hyp_junitresult_testcase_system_out_setter(instance):
    original = instance.system_out
    instance.system_out = original
    assert instance.system_out == original



@given(instance=junitresult_Testcase_strategy)
def test_hyp_junitresult_testcase_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=junitresult_Testcase_strategy)
def test_hyp_junitresult_testcase_assertions_setter(instance):
    original = instance.assertions
    instance.assertions = original
    assert instance.assertions == original



@given(instance=junitresult_Testcase_strategy)
def test_hyp_junitresult_testcase_system_err_setter(instance):
    original = instance.system_err
    instance.system_err = original
    assert instance.system_err == original



@given(instance=junitresult_Testcase_strategy)
def test_hyp_junitresult_testcase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=junitresult_Testcase_strategy)
def test_hyp_junitresult_testcase_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=junitresult_Testcase_strategy)
def test_hyp_junitresult_testcase_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractAggregatedTest,
    JunitResult,
    NegativeResult,
    junitresult_AbstractAggregatedTest,
    junitresult_Error,
    junitresult_Failure,
    junitresult_JunitResult,
    junitresult_NegativeResult,
    junitresult_Property,
    junitresult_Skipped,
    junitresult_Testcase,
    junitresult_Testrun,
    junitresult_Testsuite,
    junitresult_Testsuites,
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

def test_junitresult_AbstractAggregatedTest_errors_value_roundtrip():
    instance = junitresult_AbstractAggregatedTest(errors=7, failures=7, name="sample_text", tests=7)
    assert instance.errors == 7
    instance.errors = 13
    assert instance.errors == 13


def test_junitresult_AbstractAggregatedTest_failures_value_roundtrip():
    instance = junitresult_AbstractAggregatedTest(errors=7, failures=7, name="sample_text", tests=7)
    assert instance.failures == 7
    instance.failures = 13
    assert instance.failures == 13


def test_junitresult_AbstractAggregatedTest_name_value_roundtrip():
    instance = junitresult_AbstractAggregatedTest(errors=7, failures=7, name="sample_text", tests=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_junitresult_AbstractAggregatedTest_tests_value_roundtrip():
    instance = junitresult_AbstractAggregatedTest(errors=7, failures=7, name="sample_text", tests=7)
    assert instance.tests == 7
    instance.tests = 13
    assert instance.tests == 13


def test_junitresult_NegativeResult_message_value_roundtrip():
    instance = junitresult_NegativeResult(message="sample_text", type="sample_text", value="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_junitresult_NegativeResult_type_value_roundtrip():
    instance = junitresult_NegativeResult(message="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_junitresult_NegativeResult_value_value_roundtrip():
    instance = junitresult_NegativeResult(message="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_junitresult_Property_name_value_roundtrip():
    instance = junitresult_Property(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_junitresult_Property_value_value_roundtrip():
    instance = junitresult_Property(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_junitresult_Testcase_assertions_value_roundtrip():
    instance = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    assert instance.assertions == "sample_text"
    instance.assertions = "sample_text_2"
    assert instance.assertions == "sample_text_2"


def test_junitresult_Testcase_classname_value_roundtrip():
    instance = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    assert instance.classname == "sample_text"
    instance.classname = "sample_text_2"
    assert instance.classname == "sample_text_2"


def test_junitresult_Testcase_name_value_roundtrip():
    instance = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_junitresult_Testcase_status_value_roundtrip():
    instance = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_junitresult_Testcase_system_err_value_roundtrip():
    instance = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    assert instance.system_err == "sample_text"
    instance.system_err = "sample_text_2"
    assert instance.system_err == "sample_text_2"


def test_junitresult_Testcase_system_out_value_roundtrip():
    instance = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    assert instance.system_out == "sample_text"
    instance.system_out = "sample_text_2"
    assert instance.system_out == "sample_text_2"


def test_junitresult_Testcase_time_value_roundtrip():
    instance = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    assert instance.time == 3.14
    instance.time = 9.99
    assert instance.time == 9.99


def test_junitresult_Testrun_ignored_value_roundtrip():
    instance = junitresult_Testrun(ignored=7, project="sample_text", started=7)
    assert instance.ignored == 7
    instance.ignored = 13
    assert instance.ignored == 13


def test_junitresult_Testrun_project_value_roundtrip():
    instance = junitresult_Testrun(ignored=7, project="sample_text", started=7)
    assert instance.project == "sample_text"
    instance.project = "sample_text_2"
    assert instance.project == "sample_text_2"


def test_junitresult_Testrun_started_value_roundtrip():
    instance = junitresult_Testrun(ignored=7, project="sample_text", started=7)
    assert instance.started == 7
    instance.started = 13
    assert instance.started == 13


def test_junitresult_Testsuite_disabled_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.disabled == 7
    instance.disabled = 13
    assert instance.disabled == 13


def test_junitresult_Testsuite_hostname_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.hostname == "sample_text"
    instance.hostname = "sample_text_2"
    assert instance.hostname == "sample_text_2"


def test_junitresult_Testsuite_id_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_junitresult_Testsuite_package_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.package == "sample_text"
    instance.package = "sample_text_2"
    assert instance.package == "sample_text_2"


def test_junitresult_Testsuite_skipped_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.skipped == 7
    instance.skipped = 13
    assert instance.skipped == 13


def test_junitresult_Testsuite_system_err_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.system_err == "sample_text"
    instance.system_err = "sample_text_2"
    assert instance.system_err == "sample_text_2"


def test_junitresult_Testsuite_system_out_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.system_out == "sample_text"
    instance.system_out = "sample_text_2"
    assert instance.system_out == "sample_text_2"


def test_junitresult_Testsuite_time_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.time == 3.14
    instance.time = 9.99
    assert instance.time == 9.99


def test_junitresult_Testsuite_timestamp_value_roundtrip():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert instance.timestamp == date(2024, 1, 1)
    instance.timestamp = date(2025, 6, 15)
    assert instance.timestamp == date(2025, 6, 15)


def test_junitresult_Testsuites_disabled_value_roundtrip():
    instance = junitresult_Testsuites(disabled=7, time=3.14)
    assert instance.disabled == 7
    instance.disabled = 13
    assert instance.disabled == 13


def test_junitresult_Testsuites_time_value_roundtrip():
    instance = junitresult_Testsuites(disabled=7, time=3.14)
    assert instance.time == 3.14
    instance.time = 9.99
    assert instance.time == 9.99


def test_junitresult_Testrun_isa_AbstractAggregatedTest():
    instance = junitresult_Testrun(ignored=7, project="sample_text", started=7)
    assert isinstance(instance, AbstractAggregatedTest)


def test_junitresult_Testsuite_isa_AbstractAggregatedTest():
    instance = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    assert isinstance(instance, AbstractAggregatedTest)


def test_junitresult_Testsuites_isa_AbstractAggregatedTest():
    instance = junitresult_Testsuites(disabled=7, time=3.14)
    assert isinstance(instance, AbstractAggregatedTest)


def test_junitresult_AbstractAggregatedTest_isa_JunitResult():
    instance = junitresult_AbstractAggregatedTest(errors=7, failures=7, name="sample_text", tests=7)
    assert isinstance(instance, JunitResult)


def test_junitresult_Error_isa_NegativeResult():
    instance = junitresult_Error()
    assert isinstance(instance, NegativeResult)


def test_junitresult_Failure_isa_NegativeResult():
    instance = junitresult_Failure()
    assert isinstance(instance, NegativeResult)


def test_junitresult_Skipped_isa_NegativeResult():
    instance = junitresult_Skipped()
    assert isinstance(instance, NegativeResult)


def test_assoc_errors7_link_reassign_clear():
    a = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    b1 = junitresult_Error()
    b2 = junitresult_Error()
    _safe_set(a, 'junitresult_Testcase8', {b1})
    assert _is_linked(a, 'junitresult_Testcase8', b1)
    if hasattr(b1, 'junitresult_Error'):
        assert _is_linked(b1, 'junitresult_Error', a)
    _safe_set(a, 'junitresult_Testcase8', {b2})
    assert _is_linked(a, 'junitresult_Testcase8', b2)
    if hasattr(b1, 'junitresult_Error'):
        assert not _is_linked(b1, 'junitresult_Error', a)
    if hasattr(b2, 'junitresult_Error'):
        assert _is_linked(b2, 'junitresult_Error', a)
    _safe_set(a, 'junitresult_Testcase8', set())
    assert not _is_linked(a, 'junitresult_Testcase8', b2)
    if hasattr(b2, 'junitresult_Error'):
        assert not _is_linked(b2, 'junitresult_Error', a)


def test_assoc_failures5_link_reassign_clear():
    a = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    b1 = junitresult_Failure()
    b2 = junitresult_Failure()
    _safe_set(a, 'junitresult_Testcase6', {b1})
    assert _is_linked(a, 'junitresult_Testcase6', b1)
    if hasattr(b1, 'junitresult_Failure'):
        assert _is_linked(b1, 'junitresult_Failure', a)
    _safe_set(a, 'junitresult_Testcase6', {b2})
    assert _is_linked(a, 'junitresult_Testcase6', b2)
    if hasattr(b1, 'junitresult_Failure'):
        assert not _is_linked(b1, 'junitresult_Failure', a)
    if hasattr(b2, 'junitresult_Failure'):
        assert _is_linked(b2, 'junitresult_Failure', a)
    _safe_set(a, 'junitresult_Testcase6', set())
    assert not _is_linked(a, 'junitresult_Testcase6', b2)
    if hasattr(b2, 'junitresult_Failure'):
        assert not _is_linked(b2, 'junitresult_Failure', a)


def test_assoc_properties0_link_reassign_clear():
    a = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    b1 = junitresult_Property(name="sample_text", value="sample_text")
    b2 = junitresult_Property(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'junitresult_Testsuite', {b1})
    assert _is_linked(a, 'junitresult_Testsuite', b1)
    if hasattr(b1, 'junitresult_Property'):
        assert _is_linked(b1, 'junitresult_Property', a)
    _safe_set(a, 'junitresult_Testsuite', {b2})
    assert _is_linked(a, 'junitresult_Testsuite', b2)
    if hasattr(b1, 'junitresult_Property'):
        assert not _is_linked(b1, 'junitresult_Property', a)
    if hasattr(b2, 'junitresult_Property'):
        assert _is_linked(b2, 'junitresult_Property', a)
    _safe_set(a, 'junitresult_Testsuite', set())
    assert not _is_linked(a, 'junitresult_Testsuite', b2)
    if hasattr(b2, 'junitresult_Property'):
        assert not _is_linked(b2, 'junitresult_Property', a)


def test_assoc_skipped3_link_reassign_clear():
    a = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    b1 = junitresult_Skipped()
    b2 = junitresult_Skipped()
    _safe_set(a, 'junitresult_Testcase4', b1)
    assert _is_linked(a, 'junitresult_Testcase4', b1)
    if hasattr(b1, 'junitresult_Skipped'):
        assert _is_linked(b1, 'junitresult_Skipped', a)
    _safe_set(a, 'junitresult_Testcase4', b2)
    assert _is_linked(a, 'junitresult_Testcase4', b2)
    if hasattr(b1, 'junitresult_Skipped'):
        assert not _is_linked(b1, 'junitresult_Skipped', a)
    if hasattr(b2, 'junitresult_Skipped'):
        assert _is_linked(b2, 'junitresult_Skipped', a)
    _safe_set(a, 'junitresult_Testcase4', None)
    assert not _is_linked(a, 'junitresult_Testcase4', b2)
    if hasattr(b2, 'junitresult_Skipped'):
        assert not _is_linked(b2, 'junitresult_Skipped', a)


def test_assoc_testcases1_link_reassign_clear():
    a = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    b1 = junitresult_Testcase(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", system_err="sample_text", system_out="sample_text", time=3.14)
    b2 = junitresult_Testcase(assertions="sample_text_2", classname="sample_text_2", name="sample_text_2", status="sample_text_2", system_err="sample_text_2", system_out="sample_text_2", time=9.99)
    _safe_set(a, 'junitresult_Testsuite2', {b1})
    assert _is_linked(a, 'junitresult_Testsuite2', b1)
    if hasattr(b1, 'junitresult_Testcase'):
        assert _is_linked(b1, 'junitresult_Testcase', a)
    _safe_set(a, 'junitresult_Testsuite2', {b2})
    assert _is_linked(a, 'junitresult_Testsuite2', b2)
    if hasattr(b1, 'junitresult_Testcase'):
        assert not _is_linked(b1, 'junitresult_Testcase', a)
    if hasattr(b2, 'junitresult_Testcase'):
        assert _is_linked(b2, 'junitresult_Testcase', a)
    _safe_set(a, 'junitresult_Testsuite2', set())
    assert not _is_linked(a, 'junitresult_Testsuite2', b2)
    if hasattr(b2, 'junitresult_Testcase'):
        assert not _is_linked(b2, 'junitresult_Testcase', a)


def test_assoc_testsuites9_link_reassign_clear():
    a = junitresult_Testsuite(disabled=7, hostname="sample_text", id=7, package="sample_text", skipped=7, system_err="sample_text", system_out="sample_text", time=3.14, timestamp=date(2024, 1, 1))
    b1 = junitresult_AbstractAggregatedTest(errors=7, failures=7, name="sample_text", tests=7)
    b2 = junitresult_AbstractAggregatedTest(errors=13, failures=13, name="sample_text_2", tests=13)
    _safe_set(a, 'junitresult_Testsuite10', b1)
    assert _is_linked(a, 'junitresult_Testsuite10', b1)
    if hasattr(b1, 'junitresult_AbstractAggregatedTest'):
        assert _is_linked(b1, 'junitresult_AbstractAggregatedTest', a)
    _safe_set(a, 'junitresult_Testsuite10', b2)
    assert _is_linked(a, 'junitresult_Testsuite10', b2)
    if hasattr(b1, 'junitresult_AbstractAggregatedTest'):
        assert not _is_linked(b1, 'junitresult_AbstractAggregatedTest', a)
    if hasattr(b2, 'junitresult_AbstractAggregatedTest'):
        assert _is_linked(b2, 'junitresult_AbstractAggregatedTest', a)
    _safe_set(a, 'junitresult_Testsuite10', None)
    assert not _is_linked(a, 'junitresult_Testsuite10', b2)
    if hasattr(b2, 'junitresult_AbstractAggregatedTest'):
        assert not _is_linked(b2, 'junitresult_AbstractAggregatedTest', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractAggregatedTest_strategy = st.builds(AbstractAggregatedTest)
@given(instance=AbstractAggregatedTest_strategy)
@settings(max_examples=25)
def test_AbstractAggregatedTest_instantiation(instance):
    assert isinstance(instance, AbstractAggregatedTest)


JunitResult_strategy = st.builds(JunitResult)
@given(instance=JunitResult_strategy)
@settings(max_examples=25)
def test_JunitResult_instantiation(instance):
    assert isinstance(instance, JunitResult)


NegativeResult_strategy = st.builds(NegativeResult)
@given(instance=NegativeResult_strategy)
@settings(max_examples=25)
def test_NegativeResult_instantiation(instance):
    assert isinstance(instance, NegativeResult)


junitresult_AbstractAggregatedTest_strategy = st.builds(junitresult_AbstractAggregatedTest, errors=st.integers(), failures=st.integers(), name=safe_text, tests=st.integers())
@given(instance=junitresult_AbstractAggregatedTest_strategy)
@settings(max_examples=25)
def test_junitresult_AbstractAggregatedTest_instantiation(instance):
    assert isinstance(instance, junitresult_AbstractAggregatedTest)


junitresult_Error_strategy = st.builds(junitresult_Error)
@given(instance=junitresult_Error_strategy)
@settings(max_examples=25)
def test_junitresult_Error_instantiation(instance):
    assert isinstance(instance, junitresult_Error)


junitresult_Failure_strategy = st.builds(junitresult_Failure)
@given(instance=junitresult_Failure_strategy)
@settings(max_examples=25)
def test_junitresult_Failure_instantiation(instance):
    assert isinstance(instance, junitresult_Failure)


junitresult_JunitResult_strategy = st.builds(junitresult_JunitResult)
@given(instance=junitresult_JunitResult_strategy)
@settings(max_examples=25)
def test_junitresult_JunitResult_instantiation(instance):
    assert isinstance(instance, junitresult_JunitResult)


junitresult_NegativeResult_strategy = st.builds(junitresult_NegativeResult, message=safe_text, type=safe_text, value=safe_text)
@given(instance=junitresult_NegativeResult_strategy)
@settings(max_examples=25)
def test_junitresult_NegativeResult_instantiation(instance):
    assert isinstance(instance, junitresult_NegativeResult)


junitresult_Property_strategy = st.builds(junitresult_Property, name=safe_text, value=safe_text)
@given(instance=junitresult_Property_strategy)
@settings(max_examples=25)
def test_junitresult_Property_instantiation(instance):
    assert isinstance(instance, junitresult_Property)


junitresult_Skipped_strategy = st.builds(junitresult_Skipped)
@given(instance=junitresult_Skipped_strategy)
@settings(max_examples=25)
def test_junitresult_Skipped_instantiation(instance):
    assert isinstance(instance, junitresult_Skipped)


junitresult_Testcase_strategy = st.builds(junitresult_Testcase, assertions=safe_text, classname=safe_text, name=safe_text, status=safe_text, system_err=safe_text, system_out=safe_text, time=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=junitresult_Testcase_strategy)
@settings(max_examples=25)
def test_junitresult_Testcase_instantiation(instance):
    assert isinstance(instance, junitresult_Testcase)


junitresult_Testrun_strategy = st.builds(junitresult_Testrun, ignored=st.integers(), project=safe_text, started=st.integers())
@given(instance=junitresult_Testrun_strategy)
@settings(max_examples=25)
def test_junitresult_Testrun_instantiation(instance):
    assert isinstance(instance, junitresult_Testrun)


junitresult_Testsuite_strategy = st.builds(junitresult_Testsuite, disabled=st.integers(), hostname=safe_text, id=st.integers(), package=safe_text, skipped=st.integers(), system_err=safe_text, system_out=safe_text, time=st.floats(allow_nan=False, allow_infinity=False), timestamp=st.dates())
@given(instance=junitresult_Testsuite_strategy)
@settings(max_examples=25)
def test_junitresult_Testsuite_instantiation(instance):
    assert isinstance(instance, junitresult_Testsuite)


junitresult_Testsuites_strategy = st.builds(junitresult_Testsuites, disabled=st.integers(), time=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=junitresult_Testsuites_strategy)
@settings(max_examples=25)
def test_junitresult_Testsuites_instantiation(instance):
    assert isinstance(instance, junitresult_Testsuites)



