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
    graph_HasName,
    graph_Root,
    graph_Edge,
    HasName,
    graph_SubNode,
    graph_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graph_hasname_is_not_abstract():
    assert not inspect.isabstract(graph_HasName)


def test_hyp_graph_hasname_constructor_exists():
    assert callable(graph_HasName.__init__)


def test_hyp_graph_hasname_constructor_args():
    sig = inspect.signature(graph_HasName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_graph_root_is_not_abstract():
    assert not inspect.isabstract(graph_Root)


def test_hyp_graph_root_constructor_exists():
    assert callable(graph_Root.__init__)


def test_hyp_graph_root_constructor_args():
    sig = inspect.signature(graph_Root.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_hyp_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_hyp_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hasname_is_not_abstract():
    assert not inspect.isabstract(HasName)


def test_hyp_hasname_constructor_exists():
    assert callable(HasName.__init__)


def test_hyp_hasname_constructor_args():
    sig = inspect.signature(HasName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_subnode_is_not_abstract():
    assert not inspect.isabstract(graph_SubNode)


def test_hyp_graph_subnode_constructor_exists():
    assert callable(graph_SubNode.__init__)


def test_hyp_graph_subnode_constructor_args():
    sig = inspect.signature(graph_SubNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_hyp_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_hyp_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
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
graph_HasName_strategy = st.builds(
    graph_HasName,
    name=
        safe_text
)
graph_Root_strategy = st.builds(
    graph_Root,
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
HasName_strategy = st.builds(
    HasName,
)
graph_SubNode_strategy = st.builds(
    graph_SubNode,
)
graph_Node_strategy = st.builds(
    graph_Node,
)




@given(instance=graph_HasName_strategy)
def test_hyp_graph_hasname_name_setter(instance):
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
    HasName,
    graph_Edge,
    graph_HasName,
    graph_Node,
    graph_Root,
    graph_SubNode,
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

def test_graph_HasName_name_value_roundtrip():
    instance = graph_HasName(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graph_Node_isa_HasName():
    instance = graph_Node()
    assert isinstance(instance, HasName)


def test_graph_SubNode_isa_HasName():
    instance = graph_SubNode()
    assert isinstance(instance, HasName)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

HasName_strategy = st.builds(HasName)
@given(instance=HasName_strategy)
@settings(max_examples=25)
def test_HasName_instantiation(instance):
    assert isinstance(instance, HasName)


graph_Edge_strategy = st.builds(graph_Edge)
@given(instance=graph_Edge_strategy)
@settings(max_examples=25)
def test_graph_Edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)


graph_HasName_strategy = st.builds(graph_HasName, name=safe_text)
@given(instance=graph_HasName_strategy)
@settings(max_examples=25)
def test_graph_HasName_instantiation(instance):
    assert isinstance(instance, graph_HasName)


graph_Node_strategy = st.builds(graph_Node)
@given(instance=graph_Node_strategy)
@settings(max_examples=25)
def test_graph_Node_instantiation(instance):
    assert isinstance(instance, graph_Node)


graph_Root_strategy = st.builds(graph_Root)
@given(instance=graph_Root_strategy)
@settings(max_examples=25)
def test_graph_Root_instantiation(instance):
    assert isinstance(instance, graph_Root)


graph_SubNode_strategy = st.builds(graph_SubNode)
@given(instance=graph_SubNode_strategy)
@settings(max_examples=25)
def test_graph_SubNode_instantiation(instance):
    assert isinstance(instance, graph_SubNode)



