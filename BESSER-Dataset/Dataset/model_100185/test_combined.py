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
    Provides,
    sql_SqlProvides,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_provides_is_not_abstract():
    assert not inspect.isabstract(Provides)


def test_hyp_provides_constructor_exists():
    assert callable(Provides.__init__)


def test_hyp_provides_constructor_args():
    sig = inspect.signature(Provides.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sql_sqlprovides_is_not_abstract():
    assert not inspect.isabstract(sql_SqlProvides)


def test_hyp_sql_sqlprovides_constructor_exists():
    assert callable(sql_SqlProvides.__init__)


def test_hyp_sql_sqlprovides_constructor_args():
    sig = inspect.signature(sql_SqlProvides.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "maxActive" in params, "Missing parameter 'maxActive'"
    assert "storedProcedure" in params, "Missing parameter 'storedProcedure'"
    assert "url" in params, "Missing parameter 'url'"
    assert "maxIdle" in params, "Missing parameter 'maxIdle'"
    assert "metadata" in params, "Missing parameter 'metadata'"
    assert "maxWait" in params, "Missing parameter 'maxWait'"
    assert "driver" in params, "Missing parameter 'driver'"
    assert "user" in params, "Missing parameter 'user'"
    assert "minIdle" in params, "Missing parameter 'minIdle'"
    assert "timeBetweenEvictionRunsMillis" in params, "Missing parameter 'timeBetweenEvictionRunsMillis'"













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
Provides_strategy = st.builds(
    Provides,
)
sql_SqlProvides_strategy = st.builds(
    sql_SqlProvides,
    password=
        safe_text,
    maxActive=
        safe_text,
    storedProcedure=
        safe_text,
    url=
        safe_text,
    maxIdle=
        safe_text,
    metadata=
        safe_text,
    maxWait=
        safe_text,
    driver=
        safe_text,
    user=
        safe_text,
    minIdle=
        safe_text,
    timeBetweenEvictionRunsMillis=
        safe_text
)





@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_maxActive_setter(instance):
    original = instance.maxActive
    instance.maxActive = original
    assert instance.maxActive == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_storedProcedure_setter(instance):
    original = instance.storedProcedure
    instance.storedProcedure = original
    assert instance.storedProcedure == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_maxIdle_setter(instance):
    original = instance.maxIdle
    instance.maxIdle = original
    assert instance.maxIdle == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_metadata_setter(instance):
    original = instance.metadata
    instance.metadata = original
    assert instance.metadata == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_maxWait_setter(instance):
    original = instance.maxWait
    instance.maxWait = original
    assert instance.maxWait == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_driver_setter(instance):
    original = instance.driver
    instance.driver = original
    assert instance.driver == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_minIdle_setter(instance):
    original = instance.minIdle
    instance.minIdle = original
    assert instance.minIdle == original



@given(instance=sql_SqlProvides_strategy)
def test_hyp_sql_sqlprovides_timeBetweenEvictionRunsMillis_setter(instance):
    original = instance.timeBetweenEvictionRunsMillis
    instance.timeBetweenEvictionRunsMillis = original
    assert instance.timeBetweenEvictionRunsMillis == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Provides,
    sql_SqlProvides,
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

def test_sql_SqlProvides_driver_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.driver == "sample_text"
    instance.driver = "sample_text_2"
    assert instance.driver == "sample_text_2"


def test_sql_SqlProvides_maxActive_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.maxActive == "sample_text"
    instance.maxActive = "sample_text_2"
    assert instance.maxActive == "sample_text_2"


def test_sql_SqlProvides_maxIdle_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.maxIdle == "sample_text"
    instance.maxIdle = "sample_text_2"
    assert instance.maxIdle == "sample_text_2"


def test_sql_SqlProvides_maxWait_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.maxWait == "sample_text"
    instance.maxWait = "sample_text_2"
    assert instance.maxWait == "sample_text_2"


def test_sql_SqlProvides_metadata_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.metadata == "sample_text"
    instance.metadata = "sample_text_2"
    assert instance.metadata == "sample_text_2"


def test_sql_SqlProvides_minIdle_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.minIdle == "sample_text"
    instance.minIdle = "sample_text_2"
    assert instance.minIdle == "sample_text_2"


def test_sql_SqlProvides_password_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_sql_SqlProvides_storedProcedure_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.storedProcedure == "sample_text"
    instance.storedProcedure = "sample_text_2"
    assert instance.storedProcedure == "sample_text_2"


def test_sql_SqlProvides_timeBetweenEvictionRunsMillis_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.timeBetweenEvictionRunsMillis == "sample_text"
    instance.timeBetweenEvictionRunsMillis = "sample_text_2"
    assert instance.timeBetweenEvictionRunsMillis == "sample_text_2"


def test_sql_SqlProvides_url_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_sql_SqlProvides_user_value_roundtrip():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert instance.user == "sample_text"
    instance.user = "sample_text_2"
    assert instance.user == "sample_text_2"


def test_sql_SqlProvides_isa_Provides():
    instance = sql_SqlProvides(driver="sample_text", maxActive="sample_text", maxIdle="sample_text", maxWait="sample_text", metadata="sample_text", minIdle="sample_text", password="sample_text", storedProcedure="sample_text", timeBetweenEvictionRunsMillis="sample_text", url="sample_text", user="sample_text")
    assert isinstance(instance, Provides)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Provides_strategy = st.builds(Provides)
@given(instance=Provides_strategy)
@settings(max_examples=25)
def test_Provides_instantiation(instance):
    assert isinstance(instance, Provides)


sql_SqlProvides_strategy = st.builds(sql_SqlProvides, driver=safe_text, maxActive=safe_text, maxIdle=safe_text, maxWait=safe_text, metadata=safe_text, minIdle=safe_text, password=safe_text, storedProcedure=safe_text, timeBetweenEvictionRunsMillis=safe_text, url=safe_text, user=safe_text)
@given(instance=sql_SqlProvides_strategy)
@settings(max_examples=25)
def test_sql_SqlProvides_instantiation(instance):
    assert isinstance(instance, sql_SqlProvides)



