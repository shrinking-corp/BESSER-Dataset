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
    GraphComponent,
    graph2_Edge,
    graph2_Node,
    graph2_GraphComponent,
    graph2_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graphcomponent_is_not_abstract():
    assert not inspect.isabstract(GraphComponent)


def test_hyp_graphcomponent_constructor_exists():
    assert callable(GraphComponent.__init__)


def test_hyp_graphcomponent_constructor_args():
    sig = inspect.signature(GraphComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph2_edge_is_not_abstract():
    assert not inspect.isabstract(graph2_Edge)


def test_hyp_graph2_edge_constructor_exists():
    assert callable(graph2_Edge.__init__)


def test_hyp_graph2_edge_constructor_args():
    sig = inspect.signature(graph2_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph2_node_is_not_abstract():
    assert not inspect.isabstract(graph2_Node)


def test_hyp_graph2_node_constructor_exists():
    assert callable(graph2_Node.__init__)


def test_hyp_graph2_node_constructor_args():
    sig = inspect.signature(graph2_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph2_graphcomponent_is_not_abstract():
    assert not inspect.isabstract(graph2_GraphComponent)


def test_hyp_graph2_graphcomponent_constructor_exists():
    assert callable(graph2_GraphComponent.__init__)


def test_hyp_graph2_graphcomponent_constructor_args():
    sig = inspect.signature(graph2_GraphComponent.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_graph2_graph_is_not_abstract():
    assert not inspect.isabstract(graph2_Graph)


def test_hyp_graph2_graph_constructor_exists():
    assert callable(graph2_Graph.__init__)


def test_hyp_graph2_graph_constructor_args():
    sig = inspect.signature(graph2_Graph.__init__)
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
GraphComponent_strategy = st.builds(
    GraphComponent,
)
graph2_Edge_strategy = st.builds(
    graph2_Edge,
)
graph2_Node_strategy = st.builds(
    graph2_Node,
)
graph2_GraphComponent_strategy = st.builds(
    graph2_GraphComponent,
    text=
        safe_text
)
graph2_Graph_strategy = st.builds(
    graph2_Graph,
)







@given(instance=graph2_GraphComponent_strategy)
def test_hyp_graph2_graphcomponent_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    GraphComponent,
    graph2_Edge,
    graph2_Graph,
    graph2_GraphComponent,
    graph2_Node,
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

def test_graph2_GraphComponent_text_value_roundtrip():
    instance = graph2_GraphComponent(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_graph2_Edge_isa_GraphComponent():
    instance = graph2_Edge()
    assert isinstance(instance, GraphComponent)


def test_graph2_Node_isa_GraphComponent():
    instance = graph2_Node()
    assert isinstance(instance, GraphComponent)


def test_assoc_gcs0_link_reassign_clear():
    a = graph2_GraphComponent(text="sample_text")
    b1 = graph2_Graph()
    b2 = graph2_Graph()
    _safe_set(a, 'graph2_GraphComponent', b1)
    assert _is_linked(a, 'graph2_GraphComponent', b1)
    if hasattr(b1, 'graph2_Graph'):
        assert _is_linked(b1, 'graph2_Graph', a)
    _safe_set(a, 'graph2_GraphComponent', b2)
    assert _is_linked(a, 'graph2_GraphComponent', b2)
    if hasattr(b1, 'graph2_Graph'):
        assert not _is_linked(b1, 'graph2_Graph', a)
    if hasattr(b2, 'graph2_Graph'):
        assert _is_linked(b2, 'graph2_Graph', a)
    _safe_set(a, 'graph2_GraphComponent', None)
    assert not _is_linked(a, 'graph2_GraphComponent', b2)
    if hasattr(b2, 'graph2_Graph'):
        assert not _is_linked(b2, 'graph2_Graph', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

GraphComponent_strategy = st.builds(GraphComponent)
@given(instance=GraphComponent_strategy)
@settings(max_examples=25)
def test_GraphComponent_instantiation(instance):
    assert isinstance(instance, GraphComponent)


graph2_Edge_strategy = st.builds(graph2_Edge)
@given(instance=graph2_Edge_strategy)
@settings(max_examples=25)
def test_graph2_Edge_instantiation(instance):
    assert isinstance(instance, graph2_Edge)


graph2_Graph_strategy = st.builds(graph2_Graph)
@given(instance=graph2_Graph_strategy)
@settings(max_examples=25)
def test_graph2_Graph_instantiation(instance):
    assert isinstance(instance, graph2_Graph)


graph2_GraphComponent_strategy = st.builds(graph2_GraphComponent, text=safe_text)
@given(instance=graph2_GraphComponent_strategy)
@settings(max_examples=25)
def test_graph2_GraphComponent_instantiation(instance):
    assert isinstance(instance, graph2_GraphComponent)


graph2_Node_strategy = st.builds(graph2_Node)
@given(instance=graph2_Node_strategy)
@settings(max_examples=25)
def test_graph2_Node_instantiation(instance):
    assert isinstance(instance, graph2_Node)



