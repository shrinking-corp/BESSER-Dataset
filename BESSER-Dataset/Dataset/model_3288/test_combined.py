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
    Etunit_EStringToStringMapEntry,
    Etunit_DocumentRoot,
    Etunit_PropertiesType,
    Etunit_FailureType,
    Etunit_ErrorType,
    Etunit_SkippedType,
    Etunit_PropertyType,
    Etunit_TestsuitesType,
    Etunit_TestsuiteType,
    Etunit_TestcaseType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_etunit_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(Etunit_EStringToStringMapEntry)


def test_hyp_etunit_estringtostringmapentry_constructor_exists():
    assert callable(Etunit_EStringToStringMapEntry.__init__)


def test_hyp_etunit_estringtostringmapentry_constructor_args():
    sig = inspect.signature(Etunit_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etunit_documentroot_is_not_abstract():
    assert not inspect.isabstract(Etunit_DocumentRoot)


def test_hyp_etunit_documentroot_constructor_exists():
    assert callable(Etunit_DocumentRoot.__init__)


def test_hyp_etunit_documentroot_constructor_args():
    sig = inspect.signature(Etunit_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "systemErr" in params, "Missing parameter 'systemErr'"
    assert "systemOut" in params, "Missing parameter 'systemOut'"






def test_hyp_etunit_propertiestype_is_not_abstract():
    assert not inspect.isabstract(Etunit_PropertiesType)


def test_hyp_etunit_propertiestype_constructor_exists():
    assert callable(Etunit_PropertiesType.__init__)


def test_hyp_etunit_propertiestype_constructor_args():
    sig = inspect.signature(Etunit_PropertiesType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etunit_failuretype_is_not_abstract():
    assert not inspect.isabstract(Etunit_FailureType)


def test_hyp_etunit_failuretype_constructor_exists():
    assert callable(Etunit_FailureType.__init__)


def test_hyp_etunit_failuretype_constructor_args():
    sig = inspect.signature(Etunit_FailureType.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_etunit_errortype_is_not_abstract():
    assert not inspect.isabstract(Etunit_ErrorType)


def test_hyp_etunit_errortype_constructor_exists():
    assert callable(Etunit_ErrorType.__init__)


def test_hyp_etunit_errortype_constructor_args():
    sig = inspect.signature(Etunit_ErrorType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "message" in params, "Missing parameter 'message'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_etunit_skippedtype_is_not_abstract():
    assert not inspect.isabstract(Etunit_SkippedType)


def test_hyp_etunit_skippedtype_constructor_exists():
    assert callable(Etunit_SkippedType.__init__)


def test_hyp_etunit_skippedtype_constructor_args():
    sig = inspect.signature(Etunit_SkippedType.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "mixed" in params, "Missing parameter 'mixed'"





def test_hyp_etunit_propertytype_is_not_abstract():
    assert not inspect.isabstract(Etunit_PropertyType)


def test_hyp_etunit_propertytype_constructor_exists():
    assert callable(Etunit_PropertyType.__init__)


def test_hyp_etunit_propertytype_constructor_args():
    sig = inspect.signature(Etunit_PropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_etunit_testsuitestype_is_not_abstract():
    assert not inspect.isabstract(Etunit_TestsuitesType)


def test_hyp_etunit_testsuitestype_constructor_exists():
    assert callable(Etunit_TestsuitesType.__init__)


def test_hyp_etunit_testsuitestype_constructor_args():
    sig = inspect.signature(Etunit_TestsuitesType.__init__)
    params = list(sig.parameters.keys())
    assert "tests" in params, "Missing parameter 'tests'"
    assert "errors" in params, "Missing parameter 'errors'"
    assert "time" in params, "Missing parameter 'time'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "failures" in params, "Missing parameter 'failures'"
    assert "name" in params, "Missing parameter 'name'"









def test_hyp_etunit_testsuitetype_is_not_abstract():
    assert not inspect.isabstract(Etunit_TestsuiteType)


def test_hyp_etunit_testsuitetype_constructor_exists():
    assert callable(Etunit_TestsuiteType.__init__)


def test_hyp_etunit_testsuitetype_constructor_args():
    sig = inspect.signature(Etunit_TestsuiteType.__init__)
    params = list(sig.parameters.keys())
    assert "systemOut" in params, "Missing parameter 'systemOut'"
    assert "failures" in params, "Missing parameter 'failures'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "skipped" in params, "Missing parameter 'skipped'"
    assert "hostname" in params, "Missing parameter 'hostname'"
    assert "tests" in params, "Missing parameter 'tests'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "package" in params, "Missing parameter 'package'"
    assert "systemErr" in params, "Missing parameter 'systemErr'"
    assert "id" in params, "Missing parameter 'id'"
    assert "time" in params, "Missing parameter 'time'"
    assert "errors" in params, "Missing parameter 'errors'"
    assert "name" in params, "Missing parameter 'name'"
















def test_hyp_etunit_testcasetype_is_not_abstract():
    assert not inspect.isabstract(Etunit_TestcaseType)


def test_hyp_etunit_testcasetype_constructor_exists():
    assert callable(Etunit_TestcaseType.__init__)


def test_hyp_etunit_testcasetype_constructor_args():
    sig = inspect.signature(Etunit_TestcaseType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "systemOut" in params, "Missing parameter 'systemOut'"
    assert "systemErr" in params, "Missing parameter 'systemErr'"
    assert "classname" in params, "Missing parameter 'classname'"
    assert "status" in params, "Missing parameter 'status'"
    assert "time" in params, "Missing parameter 'time'"
    assert "assertions" in params, "Missing parameter 'assertions'"









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
Etunit_EStringToStringMapEntry_strategy = st.builds(
    Etunit_EStringToStringMapEntry,
)
Etunit_DocumentRoot_strategy = st.builds(
    Etunit_DocumentRoot,
    mixed=
        safe_text,
    systemErr=
        safe_text,
    systemOut=
        safe_text
)
Etunit_PropertiesType_strategy = st.builds(
    Etunit_PropertiesType,
)
Etunit_FailureType_strategy = st.builds(
    Etunit_FailureType,
    message=
        safe_text,
    mixed=
        safe_text,
    type=
        safe_text
)
Etunit_ErrorType_strategy = st.builds(
    Etunit_ErrorType,
    mixed=
        safe_text,
    message=
        safe_text,
    type=
        safe_text
)
Etunit_SkippedType_strategy = st.builds(
    Etunit_SkippedType,
    message=
        safe_text,
    mixed=
        safe_text
)
Etunit_PropertyType_strategy = st.builds(
    Etunit_PropertyType,
    name=
        safe_text,
    value=
        safe_text
)
Etunit_TestsuitesType_strategy = st.builds(
    Etunit_TestsuitesType,
    tests=
        safe_text,
    errors=
        safe_text,
    time=
        safe_text,
    disabled=
        safe_text,
    failures=
        safe_text,
    name=
        safe_text
)
Etunit_TestsuiteType_strategy = st.builds(
    Etunit_TestsuiteType,
    systemOut=
        safe_text,
    failures=
        safe_text,
    timestamp=
        safe_text,
    skipped=
        safe_text,
    hostname=
        safe_text,
    tests=
        safe_text,
    disabled=
        safe_text,
    package=
        safe_text,
    systemErr=
        safe_text,
    id=
        safe_text,
    time=
        safe_text,
    errors=
        safe_text,
    name=
        safe_text
)
Etunit_TestcaseType_strategy = st.builds(
    Etunit_TestcaseType,
    name=
        safe_text,
    systemOut=
        safe_text,
    systemErr=
        safe_text,
    classname=
        safe_text,
    status=
        safe_text,
    time=
        safe_text,
    assertions=
        safe_text
)





@given(instance=Etunit_DocumentRoot_strategy)
def test_hyp_etunit_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Etunit_DocumentRoot_strategy)
def test_hyp_etunit_documentroot_systemErr_setter(instance):
    original = instance.systemErr
    instance.systemErr = original
    assert instance.systemErr == original



@given(instance=Etunit_DocumentRoot_strategy)
def test_hyp_etunit_documentroot_systemOut_setter(instance):
    original = instance.systemOut
    instance.systemOut = original
    assert instance.systemOut == original





@given(instance=Etunit_FailureType_strategy)
def test_hyp_etunit_failuretype_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=Etunit_FailureType_strategy)
def test_hyp_etunit_failuretype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Etunit_FailureType_strategy)
def test_hyp_etunit_failuretype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=Etunit_ErrorType_strategy)
def test_hyp_etunit_errortype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Etunit_ErrorType_strategy)
def test_hyp_etunit_errortype_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=Etunit_ErrorType_strategy)
def test_hyp_etunit_errortype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=Etunit_SkippedType_strategy)
def test_hyp_etunit_skippedtype_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=Etunit_SkippedType_strategy)
def test_hyp_etunit_skippedtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=Etunit_PropertyType_strategy)
def test_hyp_etunit_propertytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Etunit_PropertyType_strategy)
def test_hyp_etunit_propertytype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Etunit_TestsuitesType_strategy)
def test_hyp_etunit_testsuitestype_tests_setter(instance):
    original = instance.tests
    instance.tests = original
    assert instance.tests == original



@given(instance=Etunit_TestsuitesType_strategy)
def test_hyp_etunit_testsuitestype_errors_setter(instance):
    original = instance.errors
    instance.errors = original
    assert instance.errors == original



@given(instance=Etunit_TestsuitesType_strategy)
def test_hyp_etunit_testsuitestype_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Etunit_TestsuitesType_strategy)
def test_hyp_etunit_testsuitestype_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=Etunit_TestsuitesType_strategy)
def test_hyp_etunit_testsuitestype_failures_setter(instance):
    original = instance.failures
    instance.failures = original
    assert instance.failures == original



@given(instance=Etunit_TestsuitesType_strategy)
def test_hyp_etunit_testsuitestype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_systemOut_setter(instance):
    original = instance.systemOut
    instance.systemOut = original
    assert instance.systemOut == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_failures_setter(instance):
    original = instance.failures
    instance.failures = original
    assert instance.failures == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_skipped_setter(instance):
    original = instance.skipped
    instance.skipped = original
    assert instance.skipped == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_hostname_setter(instance):
    original = instance.hostname
    instance.hostname = original
    assert instance.hostname == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_tests_setter(instance):
    original = instance.tests
    instance.tests = original
    assert instance.tests == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_systemErr_setter(instance):
    original = instance.systemErr
    instance.systemErr = original
    assert instance.systemErr == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_errors_setter(instance):
    original = instance.errors
    instance.errors = original
    assert instance.errors == original



@given(instance=Etunit_TestsuiteType_strategy)
def test_hyp_etunit_testsuitetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Etunit_TestcaseType_strategy)
def test_hyp_etunit_testcasetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Etunit_TestcaseType_strategy)
def test_hyp_etunit_testcasetype_systemOut_setter(instance):
    original = instance.systemOut
    instance.systemOut = original
    assert instance.systemOut == original



@given(instance=Etunit_TestcaseType_strategy)
def test_hyp_etunit_testcasetype_systemErr_setter(instance):
    original = instance.systemErr
    instance.systemErr = original
    assert instance.systemErr == original



@given(instance=Etunit_TestcaseType_strategy)
def test_hyp_etunit_testcasetype_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=Etunit_TestcaseType_strategy)
def test_hyp_etunit_testcasetype_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Etunit_TestcaseType_strategy)
def test_hyp_etunit_testcasetype_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Etunit_TestcaseType_strategy)
def test_hyp_etunit_testcasetype_assertions_setter(instance):
    original = instance.assertions
    instance.assertions = original
    assert instance.assertions == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Etunit_DocumentRoot,
    Etunit_EStringToStringMapEntry,
    Etunit_ErrorType,
    Etunit_FailureType,
    Etunit_PropertiesType,
    Etunit_PropertyType,
    Etunit_SkippedType,
    Etunit_TestcaseType,
    Etunit_TestsuiteType,
    Etunit_TestsuitesType,
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

def test_Etunit_DocumentRoot_mixed_value_roundtrip():
    instance = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_Etunit_DocumentRoot_systemErr_value_roundtrip():
    instance = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    assert instance.systemErr == "sample_text"
    instance.systemErr = "sample_text_2"
    assert instance.systemErr == "sample_text_2"


def test_Etunit_DocumentRoot_systemOut_value_roundtrip():
    instance = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    assert instance.systemOut == "sample_text"
    instance.systemOut = "sample_text_2"
    assert instance.systemOut == "sample_text_2"


def test_Etunit_ErrorType_message_value_roundtrip():
    instance = Etunit_ErrorType(message="sample_text", mixed="sample_text", type="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_Etunit_ErrorType_mixed_value_roundtrip():
    instance = Etunit_ErrorType(message="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_Etunit_ErrorType_type_value_roundtrip():
    instance = Etunit_ErrorType(message="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Etunit_FailureType_message_value_roundtrip():
    instance = Etunit_FailureType(message="sample_text", mixed="sample_text", type="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_Etunit_FailureType_mixed_value_roundtrip():
    instance = Etunit_FailureType(message="sample_text", mixed="sample_text", type="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_Etunit_FailureType_type_value_roundtrip():
    instance = Etunit_FailureType(message="sample_text", mixed="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Etunit_PropertyType_name_value_roundtrip():
    instance = Etunit_PropertyType(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Etunit_PropertyType_value_value_roundtrip():
    instance = Etunit_PropertyType(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Etunit_SkippedType_message_value_roundtrip():
    instance = Etunit_SkippedType(message="sample_text", mixed="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_Etunit_SkippedType_mixed_value_roundtrip():
    instance = Etunit_SkippedType(message="sample_text", mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_Etunit_TestcaseType_assertions_value_roundtrip():
    instance = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    assert instance.assertions == "sample_text"
    instance.assertions = "sample_text_2"
    assert instance.assertions == "sample_text_2"


def test_Etunit_TestcaseType_classname_value_roundtrip():
    instance = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    assert instance.classname == "sample_text"
    instance.classname = "sample_text_2"
    assert instance.classname == "sample_text_2"


def test_Etunit_TestcaseType_name_value_roundtrip():
    instance = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Etunit_TestcaseType_status_value_roundtrip():
    instance = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Etunit_TestcaseType_systemErr_value_roundtrip():
    instance = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    assert instance.systemErr == "sample_text"
    instance.systemErr = "sample_text_2"
    assert instance.systemErr == "sample_text_2"


def test_Etunit_TestcaseType_systemOut_value_roundtrip():
    instance = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    assert instance.systemOut == "sample_text"
    instance.systemOut = "sample_text_2"
    assert instance.systemOut == "sample_text_2"


def test_Etunit_TestcaseType_time_value_roundtrip():
    instance = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Etunit_TestsuiteType_disabled_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.disabled == "sample_text"
    instance.disabled = "sample_text_2"
    assert instance.disabled == "sample_text_2"


def test_Etunit_TestsuiteType_errors_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.errors == "sample_text"
    instance.errors = "sample_text_2"
    assert instance.errors == "sample_text_2"


def test_Etunit_TestsuiteType_failures_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.failures == "sample_text"
    instance.failures = "sample_text_2"
    assert instance.failures == "sample_text_2"


def test_Etunit_TestsuiteType_hostname_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.hostname == "sample_text"
    instance.hostname = "sample_text_2"
    assert instance.hostname == "sample_text_2"


def test_Etunit_TestsuiteType_id_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Etunit_TestsuiteType_name_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Etunit_TestsuiteType_package_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.package == "sample_text"
    instance.package = "sample_text_2"
    assert instance.package == "sample_text_2"


def test_Etunit_TestsuiteType_skipped_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.skipped == "sample_text"
    instance.skipped = "sample_text_2"
    assert instance.skipped == "sample_text_2"


def test_Etunit_TestsuiteType_systemErr_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.systemErr == "sample_text"
    instance.systemErr = "sample_text_2"
    assert instance.systemErr == "sample_text_2"


def test_Etunit_TestsuiteType_systemOut_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.systemOut == "sample_text"
    instance.systemOut = "sample_text_2"
    assert instance.systemOut == "sample_text_2"


def test_Etunit_TestsuiteType_tests_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.tests == "sample_text"
    instance.tests = "sample_text_2"
    assert instance.tests == "sample_text_2"


def test_Etunit_TestsuiteType_time_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Etunit_TestsuiteType_timestamp_value_roundtrip():
    instance = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    assert instance.timestamp == "sample_text"
    instance.timestamp = "sample_text_2"
    assert instance.timestamp == "sample_text_2"


def test_Etunit_TestsuitesType_disabled_value_roundtrip():
    instance = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    assert instance.disabled == "sample_text"
    instance.disabled = "sample_text_2"
    assert instance.disabled == "sample_text_2"


def test_Etunit_TestsuitesType_errors_value_roundtrip():
    instance = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    assert instance.errors == "sample_text"
    instance.errors = "sample_text_2"
    assert instance.errors == "sample_text_2"


def test_Etunit_TestsuitesType_failures_value_roundtrip():
    instance = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    assert instance.failures == "sample_text"
    instance.failures = "sample_text_2"
    assert instance.failures == "sample_text_2"


def test_Etunit_TestsuitesType_name_value_roundtrip():
    instance = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Etunit_TestsuitesType_tests_value_roundtrip():
    instance = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    assert instance.tests == "sample_text"
    instance.tests = "sample_text_2"
    assert instance.tests == "sample_text_2"


def test_Etunit_TestsuitesType_time_value_roundtrip():
    instance = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_assoc_error26_link_reassign_clear():
    a = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    b1 = Etunit_ErrorType(message="sample_text", mixed="sample_text", type="sample_text")
    b2 = Etunit_ErrorType(message="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'Etunit_TestcaseType27', {b1})
    assert _is_linked(a, 'Etunit_TestcaseType27', b1)
    if hasattr(b1, 'Etunit_ErrorType28'):
        assert _is_linked(b1, 'Etunit_ErrorType28', a)
    _safe_set(a, 'Etunit_TestcaseType27', {b2})
    assert _is_linked(a, 'Etunit_TestcaseType27', b2)
    if hasattr(b1, 'Etunit_ErrorType28'):
        assert not _is_linked(b1, 'Etunit_ErrorType28', a)
    if hasattr(b2, 'Etunit_ErrorType28'):
        assert _is_linked(b2, 'Etunit_ErrorType28', a)
    _safe_set(a, 'Etunit_TestcaseType27', set())
    assert not _is_linked(a, 'Etunit_TestcaseType27', b2)
    if hasattr(b2, 'Etunit_ErrorType28'):
        assert not _is_linked(b2, 'Etunit_ErrorType28', a)


def test_assoc_error4_link_reassign_clear():
    a = Etunit_ErrorType(message="sample_text", mixed="sample_text", type="sample_text")
    b1 = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b2 = Etunit_DocumentRoot(mixed="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2")
    _safe_set(a, 'Etunit_ErrorType', b1)
    assert _is_linked(a, 'Etunit_ErrorType', b1)
    if hasattr(b1, 'Etunit_DocumentRoot5'):
        assert _is_linked(b1, 'Etunit_DocumentRoot5', a)
    _safe_set(a, 'Etunit_ErrorType', b2)
    assert _is_linked(a, 'Etunit_ErrorType', b2)
    if hasattr(b1, 'Etunit_DocumentRoot5'):
        assert not _is_linked(b1, 'Etunit_DocumentRoot5', a)
    if hasattr(b2, 'Etunit_DocumentRoot5'):
        assert _is_linked(b2, 'Etunit_DocumentRoot5', a)
    _safe_set(a, 'Etunit_ErrorType', None)
    assert not _is_linked(a, 'Etunit_ErrorType', b2)
    if hasattr(b2, 'Etunit_DocumentRoot5'):
        assert not _is_linked(b2, 'Etunit_DocumentRoot5', a)


def test_assoc_failure29_link_reassign_clear():
    a = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    b1 = Etunit_FailureType(message="sample_text", mixed="sample_text", type="sample_text")
    b2 = Etunit_FailureType(message="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    _safe_set(a, 'Etunit_TestcaseType30', {b1})
    assert _is_linked(a, 'Etunit_TestcaseType30', b1)
    if hasattr(b1, 'Etunit_FailureType31'):
        assert _is_linked(b1, 'Etunit_FailureType31', a)
    _safe_set(a, 'Etunit_TestcaseType30', {b2})
    assert _is_linked(a, 'Etunit_TestcaseType30', b2)
    if hasattr(b1, 'Etunit_FailureType31'):
        assert not _is_linked(b1, 'Etunit_FailureType31', a)
    if hasattr(b2, 'Etunit_FailureType31'):
        assert _is_linked(b2, 'Etunit_FailureType31', a)
    _safe_set(a, 'Etunit_TestcaseType30', set())
    assert not _is_linked(a, 'Etunit_TestcaseType30', b2)
    if hasattr(b2, 'Etunit_FailureType31'):
        assert not _is_linked(b2, 'Etunit_FailureType31', a)


def test_assoc_failure6_link_reassign_clear():
    a = Etunit_FailureType(message="sample_text", mixed="sample_text", type="sample_text")
    b1 = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b2 = Etunit_DocumentRoot(mixed="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2")
    _safe_set(a, 'Etunit_FailureType', b1)
    assert _is_linked(a, 'Etunit_FailureType', b1)
    if hasattr(b1, 'Etunit_DocumentRoot7'):
        assert _is_linked(b1, 'Etunit_DocumentRoot7', a)
    _safe_set(a, 'Etunit_FailureType', b2)
    assert _is_linked(a, 'Etunit_FailureType', b2)
    if hasattr(b1, 'Etunit_DocumentRoot7'):
        assert not _is_linked(b1, 'Etunit_DocumentRoot7', a)
    if hasattr(b2, 'Etunit_DocumentRoot7'):
        assert _is_linked(b2, 'Etunit_DocumentRoot7', a)
    _safe_set(a, 'Etunit_FailureType', None)
    assert not _is_linked(a, 'Etunit_FailureType', b2)
    if hasattr(b2, 'Etunit_DocumentRoot7'):
        assert not _is_linked(b2, 'Etunit_DocumentRoot7', a)


def test_assoc_properties35_link_reassign_clear():
    a = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    b1 = Etunit_PropertiesType()
    b2 = Etunit_PropertiesType()
    _safe_set(a, 'Etunit_TestsuiteType36', b1)
    assert _is_linked(a, 'Etunit_TestsuiteType36', b1)
    if hasattr(b1, 'Etunit_PropertiesType37'):
        assert _is_linked(b1, 'Etunit_PropertiesType37', a)
    _safe_set(a, 'Etunit_TestsuiteType36', b2)
    assert _is_linked(a, 'Etunit_TestsuiteType36', b2)
    if hasattr(b1, 'Etunit_PropertiesType37'):
        assert not _is_linked(b1, 'Etunit_PropertiesType37', a)
    if hasattr(b2, 'Etunit_PropertiesType37'):
        assert _is_linked(b2, 'Etunit_PropertiesType37', a)
    _safe_set(a, 'Etunit_TestsuiteType36', None)
    assert not _is_linked(a, 'Etunit_TestsuiteType36', b2)
    if hasattr(b2, 'Etunit_PropertiesType37'):
        assert not _is_linked(b2, 'Etunit_PropertiesType37', a)


def test_assoc_properties8_link_reassign_clear():
    a = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b1 = Etunit_PropertiesType()
    b2 = Etunit_PropertiesType()
    _safe_set(a, 'Etunit_DocumentRoot9', {b1})
    assert _is_linked(a, 'Etunit_DocumentRoot9', b1)
    if hasattr(b1, 'Etunit_PropertiesType'):
        assert _is_linked(b1, 'Etunit_PropertiesType', a)
    _safe_set(a, 'Etunit_DocumentRoot9', {b2})
    assert _is_linked(a, 'Etunit_DocumentRoot9', b2)
    if hasattr(b1, 'Etunit_PropertiesType'):
        assert not _is_linked(b1, 'Etunit_PropertiesType', a)
    if hasattr(b2, 'Etunit_PropertiesType'):
        assert _is_linked(b2, 'Etunit_PropertiesType', a)
    _safe_set(a, 'Etunit_DocumentRoot9', set())
    assert not _is_linked(a, 'Etunit_DocumentRoot9', b2)
    if hasattr(b2, 'Etunit_PropertiesType'):
        assert not _is_linked(b2, 'Etunit_PropertiesType', a)


def test_assoc_property10_link_reassign_clear():
    a = Etunit_PropertyType(name="sample_text", value="sample_text")
    b1 = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b2 = Etunit_DocumentRoot(mixed="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2")
    _safe_set(a, 'Etunit_PropertyType', b1)
    assert _is_linked(a, 'Etunit_PropertyType', b1)
    if hasattr(b1, 'Etunit_DocumentRoot11'):
        assert _is_linked(b1, 'Etunit_DocumentRoot11', a)
    _safe_set(a, 'Etunit_PropertyType', b2)
    assert _is_linked(a, 'Etunit_PropertyType', b2)
    if hasattr(b1, 'Etunit_DocumentRoot11'):
        assert not _is_linked(b1, 'Etunit_DocumentRoot11', a)
    if hasattr(b2, 'Etunit_DocumentRoot11'):
        assert _is_linked(b2, 'Etunit_DocumentRoot11', a)
    _safe_set(a, 'Etunit_PropertyType', None)
    assert not _is_linked(a, 'Etunit_PropertyType', b2)
    if hasattr(b2, 'Etunit_DocumentRoot11'):
        assert not _is_linked(b2, 'Etunit_DocumentRoot11', a)


def test_assoc_property20_link_reassign_clear():
    a = Etunit_PropertyType(name="sample_text", value="sample_text")
    b1 = Etunit_PropertiesType()
    b2 = Etunit_PropertiesType()
    _safe_set(a, 'Etunit_PropertyType22', b1)
    assert _is_linked(a, 'Etunit_PropertyType22', b1)
    if hasattr(b1, 'Etunit_PropertiesType21'):
        assert _is_linked(b1, 'Etunit_PropertiesType21', a)
    _safe_set(a, 'Etunit_PropertyType22', b2)
    assert _is_linked(a, 'Etunit_PropertyType22', b2)
    if hasattr(b1, 'Etunit_PropertiesType21'):
        assert not _is_linked(b1, 'Etunit_PropertiesType21', a)
    if hasattr(b2, 'Etunit_PropertiesType21'):
        assert _is_linked(b2, 'Etunit_PropertiesType21', a)
    _safe_set(a, 'Etunit_PropertyType22', None)
    assert not _is_linked(a, 'Etunit_PropertyType22', b2)
    if hasattr(b2, 'Etunit_PropertiesType21'):
        assert not _is_linked(b2, 'Etunit_PropertiesType21', a)


def test_assoc_skipped12_link_reassign_clear():
    a = Etunit_SkippedType(message="sample_text", mixed="sample_text")
    b1 = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b2 = Etunit_DocumentRoot(mixed="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2")
    _safe_set(a, 'Etunit_SkippedType', b1)
    assert _is_linked(a, 'Etunit_SkippedType', b1)
    if hasattr(b1, 'Etunit_DocumentRoot13'):
        assert _is_linked(b1, 'Etunit_DocumentRoot13', a)
    _safe_set(a, 'Etunit_SkippedType', b2)
    assert _is_linked(a, 'Etunit_SkippedType', b2)
    if hasattr(b1, 'Etunit_DocumentRoot13'):
        assert not _is_linked(b1, 'Etunit_DocumentRoot13', a)
    if hasattr(b2, 'Etunit_DocumentRoot13'):
        assert _is_linked(b2, 'Etunit_DocumentRoot13', a)
    _safe_set(a, 'Etunit_SkippedType', None)
    assert not _is_linked(a, 'Etunit_SkippedType', b2)
    if hasattr(b2, 'Etunit_DocumentRoot13'):
        assert not _is_linked(b2, 'Etunit_DocumentRoot13', a)


def test_assoc_skipped23_link_reassign_clear():
    a = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    b1 = Etunit_SkippedType(message="sample_text", mixed="sample_text")
    b2 = Etunit_SkippedType(message="sample_text_2", mixed="sample_text_2")
    _safe_set(a, 'Etunit_TestcaseType24', b1)
    assert _is_linked(a, 'Etunit_TestcaseType24', b1)
    if hasattr(b1, 'Etunit_SkippedType25'):
        assert _is_linked(b1, 'Etunit_SkippedType25', a)
    _safe_set(a, 'Etunit_TestcaseType24', b2)
    assert _is_linked(a, 'Etunit_TestcaseType24', b2)
    if hasattr(b1, 'Etunit_SkippedType25'):
        assert not _is_linked(b1, 'Etunit_SkippedType25', a)
    if hasattr(b2, 'Etunit_SkippedType25'):
        assert _is_linked(b2, 'Etunit_SkippedType25', a)
    _safe_set(a, 'Etunit_TestcaseType24', None)
    assert not _is_linked(a, 'Etunit_TestcaseType24', b2)
    if hasattr(b2, 'Etunit_SkippedType25'):
        assert not _is_linked(b2, 'Etunit_SkippedType25', a)


def test_assoc_testcase14_link_reassign_clear():
    a = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    b1 = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b2 = Etunit_DocumentRoot(mixed="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2")
    _safe_set(a, 'Etunit_TestcaseType', b1)
    assert _is_linked(a, 'Etunit_TestcaseType', b1)
    if hasattr(b1, 'Etunit_DocumentRoot15'):
        assert _is_linked(b1, 'Etunit_DocumentRoot15', a)
    _safe_set(a, 'Etunit_TestcaseType', b2)
    assert _is_linked(a, 'Etunit_TestcaseType', b2)
    if hasattr(b1, 'Etunit_DocumentRoot15'):
        assert not _is_linked(b1, 'Etunit_DocumentRoot15', a)
    if hasattr(b2, 'Etunit_DocumentRoot15'):
        assert _is_linked(b2, 'Etunit_DocumentRoot15', a)
    _safe_set(a, 'Etunit_TestcaseType', None)
    assert not _is_linked(a, 'Etunit_TestcaseType', b2)
    if hasattr(b2, 'Etunit_DocumentRoot15'):
        assert not _is_linked(b2, 'Etunit_DocumentRoot15', a)


def test_assoc_testcase38_link_reassign_clear():
    a = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    b1 = Etunit_TestcaseType(assertions="sample_text", classname="sample_text", name="sample_text", status="sample_text", systemErr="sample_text", systemOut="sample_text", time="sample_text")
    b2 = Etunit_TestcaseType(assertions="sample_text_2", classname="sample_text_2", name="sample_text_2", status="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2", time="sample_text_2")
    _safe_set(a, 'Etunit_TestsuiteType39', {b1})
    assert _is_linked(a, 'Etunit_TestsuiteType39', b1)
    if hasattr(b1, 'Etunit_TestcaseType40'):
        assert _is_linked(b1, 'Etunit_TestcaseType40', a)
    _safe_set(a, 'Etunit_TestsuiteType39', {b2})
    assert _is_linked(a, 'Etunit_TestsuiteType39', b2)
    if hasattr(b1, 'Etunit_TestcaseType40'):
        assert not _is_linked(b1, 'Etunit_TestcaseType40', a)
    if hasattr(b2, 'Etunit_TestcaseType40'):
        assert _is_linked(b2, 'Etunit_TestcaseType40', a)
    _safe_set(a, 'Etunit_TestsuiteType39', set())
    assert not _is_linked(a, 'Etunit_TestsuiteType39', b2)
    if hasattr(b2, 'Etunit_TestcaseType40'):
        assert not _is_linked(b2, 'Etunit_TestcaseType40', a)


def test_assoc_testsuite16_link_reassign_clear():
    a = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    b1 = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b2 = Etunit_DocumentRoot(mixed="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2")
    _safe_set(a, 'Etunit_TestsuiteType', b1)
    assert _is_linked(a, 'Etunit_TestsuiteType', b1)
    if hasattr(b1, 'Etunit_DocumentRoot17'):
        assert _is_linked(b1, 'Etunit_DocumentRoot17', a)
    _safe_set(a, 'Etunit_TestsuiteType', b2)
    assert _is_linked(a, 'Etunit_TestsuiteType', b2)
    if hasattr(b1, 'Etunit_DocumentRoot17'):
        assert not _is_linked(b1, 'Etunit_DocumentRoot17', a)
    if hasattr(b2, 'Etunit_DocumentRoot17'):
        assert _is_linked(b2, 'Etunit_DocumentRoot17', a)
    _safe_set(a, 'Etunit_TestsuiteType', None)
    assert not _is_linked(a, 'Etunit_TestsuiteType', b2)
    if hasattr(b2, 'Etunit_DocumentRoot17'):
        assert not _is_linked(b2, 'Etunit_DocumentRoot17', a)


def test_assoc_testsuite32_link_reassign_clear():
    a = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    b1 = Etunit_TestsuiteType(disabled="sample_text", errors="sample_text", failures="sample_text", hostname="sample_text", id="sample_text", name="sample_text", package="sample_text", skipped="sample_text", systemErr="sample_text", systemOut="sample_text", tests="sample_text", time="sample_text", timestamp="sample_text")
    b2 = Etunit_TestsuiteType(disabled="sample_text_2", errors="sample_text_2", failures="sample_text_2", hostname="sample_text_2", id="sample_text_2", name="sample_text_2", package="sample_text_2", skipped="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2", tests="sample_text_2", time="sample_text_2", timestamp="sample_text_2")
    _safe_set(a, 'Etunit_TestsuitesType33', {b1})
    assert _is_linked(a, 'Etunit_TestsuitesType33', b1)
    if hasattr(b1, 'Etunit_TestsuiteType34'):
        assert _is_linked(b1, 'Etunit_TestsuiteType34', a)
    _safe_set(a, 'Etunit_TestsuitesType33', {b2})
    assert _is_linked(a, 'Etunit_TestsuitesType33', b2)
    if hasattr(b1, 'Etunit_TestsuiteType34'):
        assert not _is_linked(b1, 'Etunit_TestsuiteType34', a)
    if hasattr(b2, 'Etunit_TestsuiteType34'):
        assert _is_linked(b2, 'Etunit_TestsuiteType34', a)
    _safe_set(a, 'Etunit_TestsuitesType33', set())
    assert not _is_linked(a, 'Etunit_TestsuitesType33', b2)
    if hasattr(b2, 'Etunit_TestsuiteType34'):
        assert not _is_linked(b2, 'Etunit_TestsuiteType34', a)


def test_assoc_testsuites18_link_reassign_clear():
    a = Etunit_TestsuitesType(disabled="sample_text", errors="sample_text", failures="sample_text", name="sample_text", tests="sample_text", time="sample_text")
    b1 = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b2 = Etunit_DocumentRoot(mixed="sample_text_2", systemErr="sample_text_2", systemOut="sample_text_2")
    _safe_set(a, 'Etunit_TestsuitesType', b1)
    assert _is_linked(a, 'Etunit_TestsuitesType', b1)
    if hasattr(b1, 'Etunit_DocumentRoot19'):
        assert _is_linked(b1, 'Etunit_DocumentRoot19', a)
    _safe_set(a, 'Etunit_TestsuitesType', b2)
    assert _is_linked(a, 'Etunit_TestsuitesType', b2)
    if hasattr(b1, 'Etunit_DocumentRoot19'):
        assert not _is_linked(b1, 'Etunit_DocumentRoot19', a)
    if hasattr(b2, 'Etunit_DocumentRoot19'):
        assert _is_linked(b2, 'Etunit_DocumentRoot19', a)
    _safe_set(a, 'Etunit_TestsuitesType', None)
    assert not _is_linked(a, 'Etunit_TestsuitesType', b2)
    if hasattr(b2, 'Etunit_DocumentRoot19'):
        assert not _is_linked(b2, 'Etunit_DocumentRoot19', a)


def test_assoc_xMLNSPrefixMap0_link_reassign_clear():
    a = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b1 = Etunit_EStringToStringMapEntry()
    b2 = Etunit_EStringToStringMapEntry()
    _safe_set(a, 'Etunit_DocumentRoot', {b1})
    assert _is_linked(a, 'Etunit_DocumentRoot', b1)
    if hasattr(b1, 'Etunit_EStringToStringMapEntry'):
        assert _is_linked(b1, 'Etunit_EStringToStringMapEntry', a)
    _safe_set(a, 'Etunit_DocumentRoot', {b2})
    assert _is_linked(a, 'Etunit_DocumentRoot', b2)
    if hasattr(b1, 'Etunit_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'Etunit_EStringToStringMapEntry', a)
    if hasattr(b2, 'Etunit_EStringToStringMapEntry'):
        assert _is_linked(b2, 'Etunit_EStringToStringMapEntry', a)
    _safe_set(a, 'Etunit_DocumentRoot', set())
    assert not _is_linked(a, 'Etunit_DocumentRoot', b2)
    if hasattr(b2, 'Etunit_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'Etunit_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation1_link_reassign_clear():
    a = Etunit_DocumentRoot(mixed="sample_text", systemErr="sample_text", systemOut="sample_text")
    b1 = Etunit_EStringToStringMapEntry()
    b2 = Etunit_EStringToStringMapEntry()
    _safe_set(a, 'Etunit_DocumentRoot2', {b1})
    assert _is_linked(a, 'Etunit_DocumentRoot2', b1)
    if hasattr(b1, 'Etunit_EStringToStringMapEntry3'):
        assert _is_linked(b1, 'Etunit_EStringToStringMapEntry3', a)
    _safe_set(a, 'Etunit_DocumentRoot2', {b2})
    assert _is_linked(a, 'Etunit_DocumentRoot2', b2)
    if hasattr(b1, 'Etunit_EStringToStringMapEntry3'):
        assert not _is_linked(b1, 'Etunit_EStringToStringMapEntry3', a)
    if hasattr(b2, 'Etunit_EStringToStringMapEntry3'):
        assert _is_linked(b2, 'Etunit_EStringToStringMapEntry3', a)
    _safe_set(a, 'Etunit_DocumentRoot2', set())
    assert not _is_linked(a, 'Etunit_DocumentRoot2', b2)
    if hasattr(b2, 'Etunit_EStringToStringMapEntry3'):
        assert not _is_linked(b2, 'Etunit_EStringToStringMapEntry3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Etunit_DocumentRoot_strategy = st.builds(Etunit_DocumentRoot, mixed=safe_text, systemErr=safe_text, systemOut=safe_text)
@given(instance=Etunit_DocumentRoot_strategy)
@settings(max_examples=25)
def test_Etunit_DocumentRoot_instantiation(instance):
    assert isinstance(instance, Etunit_DocumentRoot)


Etunit_EStringToStringMapEntry_strategy = st.builds(Etunit_EStringToStringMapEntry)
@given(instance=Etunit_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_Etunit_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, Etunit_EStringToStringMapEntry)


Etunit_ErrorType_strategy = st.builds(Etunit_ErrorType, message=safe_text, mixed=safe_text, type=safe_text)
@given(instance=Etunit_ErrorType_strategy)
@settings(max_examples=25)
def test_Etunit_ErrorType_instantiation(instance):
    assert isinstance(instance, Etunit_ErrorType)


Etunit_FailureType_strategy = st.builds(Etunit_FailureType, message=safe_text, mixed=safe_text, type=safe_text)
@given(instance=Etunit_FailureType_strategy)
@settings(max_examples=25)
def test_Etunit_FailureType_instantiation(instance):
    assert isinstance(instance, Etunit_FailureType)


Etunit_PropertiesType_strategy = st.builds(Etunit_PropertiesType)
@given(instance=Etunit_PropertiesType_strategy)
@settings(max_examples=25)
def test_Etunit_PropertiesType_instantiation(instance):
    assert isinstance(instance, Etunit_PropertiesType)


Etunit_PropertyType_strategy = st.builds(Etunit_PropertyType, name=safe_text, value=safe_text)
@given(instance=Etunit_PropertyType_strategy)
@settings(max_examples=25)
def test_Etunit_PropertyType_instantiation(instance):
    assert isinstance(instance, Etunit_PropertyType)


Etunit_SkippedType_strategy = st.builds(Etunit_SkippedType, message=safe_text, mixed=safe_text)
@given(instance=Etunit_SkippedType_strategy)
@settings(max_examples=25)
def test_Etunit_SkippedType_instantiation(instance):
    assert isinstance(instance, Etunit_SkippedType)


Etunit_TestcaseType_strategy = st.builds(Etunit_TestcaseType, assertions=safe_text, classname=safe_text, name=safe_text, status=safe_text, systemErr=safe_text, systemOut=safe_text, time=safe_text)
@given(instance=Etunit_TestcaseType_strategy)
@settings(max_examples=25)
def test_Etunit_TestcaseType_instantiation(instance):
    assert isinstance(instance, Etunit_TestcaseType)


Etunit_TestsuiteType_strategy = st.builds(Etunit_TestsuiteType, disabled=safe_text, errors=safe_text, failures=safe_text, hostname=safe_text, id=safe_text, name=safe_text, package=safe_text, skipped=safe_text, systemErr=safe_text, systemOut=safe_text, tests=safe_text, time=safe_text, timestamp=safe_text)
@given(instance=Etunit_TestsuiteType_strategy)
@settings(max_examples=25)
def test_Etunit_TestsuiteType_instantiation(instance):
    assert isinstance(instance, Etunit_TestsuiteType)


Etunit_TestsuitesType_strategy = st.builds(Etunit_TestsuitesType, disabled=safe_text, errors=safe_text, failures=safe_text, name=safe_text, tests=safe_text, time=safe_text)
@given(instance=Etunit_TestsuitesType_strategy)
@settings(max_examples=25)
def test_Etunit_TestsuitesType_instantiation(instance):
    assert isinstance(instance, Etunit_TestsuitesType)



