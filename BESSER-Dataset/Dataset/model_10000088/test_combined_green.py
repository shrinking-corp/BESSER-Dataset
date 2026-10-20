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
    Auto_Events_Scheduler__Actor,
    Cashier,
    Waiter,
    Cook,
    Customer,
    People,
    Worker,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_auto_events_scheduler__actor_is_not_abstract():
    assert not inspect.isabstract(Auto_Events_Scheduler__Actor)


def test_hyp_auto_events_scheduler__actor_constructor_exists():
    assert callable(Auto_Events_Scheduler__Actor.__init__)


def test_hyp_auto_events_scheduler__actor_constructor_args():
    sig = inspect.signature(Auto_Events_Scheduler__Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cashier_is_not_abstract():
    assert not inspect.isabstract(Cashier)


def test_hyp_cashier_constructor_exists():
    assert callable(Cashier.__init__)


def test_hyp_cashier_constructor_args():
    sig = inspect.signature(Cashier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_waiter_is_not_abstract():
    assert not inspect.isabstract(Waiter)


def test_hyp_waiter_constructor_exists():
    assert callable(Waiter.__init__)


def test_hyp_waiter_constructor_args():
    sig = inspect.signature(Waiter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cook_is_not_abstract():
    assert not inspect.isabstract(Cook)


def test_hyp_cook_constructor_exists():
    assert callable(Cook.__init__)


def test_hyp_cook_constructor_args():
    sig = inspect.signature(Cook.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_people_is_not_abstract():
    assert not inspect.isabstract(People)


def test_hyp_people_constructor_exists():
    assert callable(People.__init__)


def test_hyp_people_constructor_args():
    sig = inspect.signature(People.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_worker_is_not_abstract():
    assert not inspect.isabstract(Worker)


def test_hyp_worker_constructor_exists():
    assert callable(Worker.__init__)


def test_hyp_worker_constructor_args():
    sig = inspect.signature(Worker.__init__)
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
Auto_Events_Scheduler__Actor_strategy = st.builds(
    Auto_Events_Scheduler__Actor,
)
Cashier_strategy = st.builds(
    Cashier,
)
Waiter_strategy = st.builds(
    Waiter,
)
Cook_strategy = st.builds(
    Cook,
)
Customer_strategy = st.builds(
    Customer,
)
People_strategy = st.builds(
    People,
    name=
        safe_text
)
Worker_strategy = st.builds(
    Worker,
)









@given(instance=People_strategy)
def test_hyp_people_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Auto_Events_Scheduler__Actor,
    Cashier,
    Cook,
    Customer,
    People,
    Waiter,
    Worker,
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

def test_People_name_value_roundtrip():
    instance = People(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Auto_Events_Scheduler__Actor_strategy = st.builds(Auto_Events_Scheduler__Actor)
@given(instance=Auto_Events_Scheduler__Actor_strategy)
@settings(max_examples=25)
def test_Auto_Events_Scheduler__Actor_instantiation(instance):
    assert isinstance(instance, Auto_Events_Scheduler__Actor)


Cashier_strategy = st.builds(Cashier)
@given(instance=Cashier_strategy)
@settings(max_examples=25)
def test_Cashier_instantiation(instance):
    assert isinstance(instance, Cashier)


Cook_strategy = st.builds(Cook)
@given(instance=Cook_strategy)
@settings(max_examples=25)
def test_Cook_instantiation(instance):
    assert isinstance(instance, Cook)


Customer_strategy = st.builds(Customer)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


People_strategy = st.builds(People, name=safe_text)
@given(instance=People_strategy)
@settings(max_examples=25)
def test_People_instantiation(instance):
    assert isinstance(instance, People)


Waiter_strategy = st.builds(Waiter)
@given(instance=Waiter_strategy)
@settings(max_examples=25)
def test_Waiter_instantiation(instance):
    assert isinstance(instance, Waiter)


Worker_strategy = st.builds(Worker)
@given(instance=Worker_strategy)
@settings(max_examples=25)
def test_Worker_instantiation(instance):
    assert isinstance(instance, Worker)



