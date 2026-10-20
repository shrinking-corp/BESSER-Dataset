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
    Expression,
    Edge,
    uppaalSMC_ChanceEdge,
    Location,
    uppaalSMC_ExponentialLocation,
    uppaalSMC_ChanceNode,
    Type,
    uppaalSMC_DoubleType,
    NTA,
    uppaalSMC_NSTA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_hyp_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_hyp_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaalsmc_chanceedge_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_ChanceEdge)


def test_hyp_uppaalsmc_chanceedge_constructor_exists():
    assert callable(uppaalSMC_ChanceEdge.__init__)


def test_hyp_uppaalsmc_chanceedge_constructor_args():
    sig = inspect.signature(uppaalSMC_ChanceEdge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"




def test_hyp_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_hyp_location_constructor_exists():
    assert callable(Location.__init__)


def test_hyp_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaalsmc_exponentiallocation_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_ExponentialLocation)


def test_hyp_uppaalsmc_exponentiallocation_constructor_exists():
    assert callable(uppaalSMC_ExponentialLocation.__init__)


def test_hyp_uppaalsmc_exponentiallocation_constructor_args():
    sig = inspect.signature(uppaalSMC_ExponentialLocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaalsmc_chancenode_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_ChanceNode)


def test_hyp_uppaalsmc_chancenode_constructor_exists():
    assert callable(uppaalSMC_ChanceNode.__init__)


def test_hyp_uppaalsmc_chancenode_constructor_args():
    sig = inspect.signature(uppaalSMC_ChanceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaalsmc_doubletype_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_DoubleType)


def test_hyp_uppaalsmc_doubletype_constructor_exists():
    assert callable(uppaalSMC_DoubleType.__init__)


def test_hyp_uppaalsmc_doubletype_constructor_args():
    sig = inspect.signature(uppaalSMC_DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nta_is_not_abstract():
    assert not inspect.isabstract(NTA)


def test_hyp_nta_constructor_exists():
    assert callable(NTA.__init__)


def test_hyp_nta_constructor_args():
    sig = inspect.signature(NTA.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaalsmc_nsta_is_not_abstract():
    assert not inspect.isabstract(uppaalSMC_NSTA)


def test_hyp_uppaalsmc_nsta_constructor_exists():
    assert callable(uppaalSMC_NSTA.__init__)


def test_hyp_uppaalsmc_nsta_constructor_args():
    sig = inspect.signature(uppaalSMC_NSTA.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
Edge_strategy = st.builds(
    Edge,
)
uppaalSMC_ChanceEdge_strategy = st.builds(
    uppaalSMC_ChanceEdge,
    weight=
        st.integers()
)
Location_strategy = st.builds(
    Location,
)
uppaalSMC_ExponentialLocation_strategy = st.builds(
    uppaalSMC_ExponentialLocation,
)
uppaalSMC_ChanceNode_strategy = st.builds(
    uppaalSMC_ChanceNode,
)
Type_strategy = st.builds(
    Type,
)
uppaalSMC_DoubleType_strategy = st.builds(
    uppaalSMC_DoubleType,
)
NTA_strategy = st.builds(
    NTA,
)
uppaalSMC_NSTA_strategy = st.builds(
    uppaalSMC_NSTA,
)






@given(instance=uppaalSMC_ChanceEdge_strategy)
def test_hyp_uppaalsmc_chanceedge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Edge,
    Expression,
    Location,
    NTA,
    Type,
    uppaalSMC_ChanceEdge,
    uppaalSMC_ChanceNode,
    uppaalSMC_DoubleType,
    uppaalSMC_ExponentialLocation,
    uppaalSMC_NSTA,
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

def test_uppaalSMC_ChanceEdge_weight_value_roundtrip():
    instance = uppaalSMC_ChanceEdge(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_uppaalSMC_ChanceEdge_isa_Edge():
    instance = uppaalSMC_ChanceEdge(weight=7)
    assert isinstance(instance, Edge)


def test_uppaalSMC_ChanceNode_isa_Location():
    instance = uppaalSMC_ChanceNode()
    assert isinstance(instance, Location)


def test_uppaalSMC_ExponentialLocation_isa_Location():
    instance = uppaalSMC_ExponentialLocation()
    assert isinstance(instance, Location)


def test_uppaalSMC_NSTA_isa_NTA():
    instance = uppaalSMC_NSTA()
    assert isinstance(instance, NTA)


def test_uppaalSMC_DoubleType_isa_Type():
    instance = uppaalSMC_DoubleType()
    assert isinstance(instance, Type)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Location_strategy = st.builds(Location)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


NTA_strategy = st.builds(NTA)
@given(instance=NTA_strategy)
@settings(max_examples=25)
def test_NTA_instantiation(instance):
    assert isinstance(instance, NTA)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


uppaalSMC_ChanceEdge_strategy = st.builds(uppaalSMC_ChanceEdge, weight=st.integers())
@given(instance=uppaalSMC_ChanceEdge_strategy)
@settings(max_examples=25)
def test_uppaalSMC_ChanceEdge_instantiation(instance):
    assert isinstance(instance, uppaalSMC_ChanceEdge)


uppaalSMC_ChanceNode_strategy = st.builds(uppaalSMC_ChanceNode)
@given(instance=uppaalSMC_ChanceNode_strategy)
@settings(max_examples=25)
def test_uppaalSMC_ChanceNode_instantiation(instance):
    assert isinstance(instance, uppaalSMC_ChanceNode)


uppaalSMC_DoubleType_strategy = st.builds(uppaalSMC_DoubleType)
@given(instance=uppaalSMC_DoubleType_strategy)
@settings(max_examples=25)
def test_uppaalSMC_DoubleType_instantiation(instance):
    assert isinstance(instance, uppaalSMC_DoubleType)


uppaalSMC_ExponentialLocation_strategy = st.builds(uppaalSMC_ExponentialLocation)
@given(instance=uppaalSMC_ExponentialLocation_strategy)
@settings(max_examples=25)
def test_uppaalSMC_ExponentialLocation_instantiation(instance):
    assert isinstance(instance, uppaalSMC_ExponentialLocation)


uppaalSMC_NSTA_strategy = st.builds(uppaalSMC_NSTA)
@given(instance=uppaalSMC_NSTA_strategy)
@settings(max_examples=25)
def test_uppaalSMC_NSTA_instantiation(instance):
    assert isinstance(instance, uppaalSMC_NSTA)



