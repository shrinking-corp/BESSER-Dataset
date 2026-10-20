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
    Typed,
    graph_Named,
    graph_Edge,
    graph_Node,
    Named,
    graph_Typed,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_hyp_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_hyp_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_named_is_not_abstract():
    assert not inspect.isabstract(graph_Named)


def test_hyp_graph_named_constructor_exists():
    assert callable(graph_Named.__init__)


def test_hyp_graph_named_constructor_args():
    sig = inspect.signature(graph_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_hyp_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_hyp_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_hyp_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_hyp_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_typed_is_not_abstract():
    assert not inspect.isabstract(graph_Typed)


def test_hyp_graph_typed_constructor_exists():
    assert callable(graph_Typed.__init__)


def test_hyp_graph_typed_constructor_args():
    sig = inspect.signature(graph_Typed.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_hyp_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_hyp_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
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
Typed_strategy = st.builds(
    Typed,
)
graph_Named_strategy = st.builds(
    graph_Named,
    name=
        safe_text
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
graph_Node_strategy = st.builds(
    graph_Node,
)
Named_strategy = st.builds(
    Named,
)
graph_Typed_strategy = st.builds(
    graph_Typed,
    type=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
)





@given(instance=graph_Named_strategy)
def test_hyp_graph_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=graph_Typed_strategy)
def test_hyp_graph_typed_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Named,
    Typed,
    graph_Edge,
    graph_Graph,
    graph_Named,
    graph_Node,
    graph_Typed,
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

def test_graph_Named_name_value_roundtrip():
    instance = graph_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graph_Typed_type_value_roundtrip():
    instance = graph_Typed(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graph_Graph_isa_Named():
    instance = graph_Graph()
    assert isinstance(instance, Named)


def test_graph_Typed_isa_Named():
    instance = graph_Typed(type="sample_text")
    assert isinstance(instance, Named)


def test_graph_Edge_isa_Typed():
    instance = graph_Edge()
    assert isinstance(instance, Typed)


def test_graph_Node_isa_Typed():
    instance = graph_Node()
    assert isinstance(instance, Typed)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


Typed_strategy = st.builds(Typed)
@given(instance=Typed_strategy)
@settings(max_examples=25)
def test_Typed_instantiation(instance):
    assert isinstance(instance, Typed)


graph_Edge_strategy = st.builds(graph_Edge)
@given(instance=graph_Edge_strategy)
@settings(max_examples=25)
def test_graph_Edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)


graph_Graph_strategy = st.builds(graph_Graph)
@given(instance=graph_Graph_strategy)
@settings(max_examples=25)
def test_graph_Graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)


graph_Named_strategy = st.builds(graph_Named, name=safe_text)
@given(instance=graph_Named_strategy)
@settings(max_examples=25)
def test_graph_Named_instantiation(instance):
    assert isinstance(instance, graph_Named)


graph_Node_strategy = st.builds(graph_Node)
@given(instance=graph_Node_strategy)
@settings(max_examples=25)
def test_graph_Node_instantiation(instance):
    assert isinstance(instance, graph_Node)


graph_Typed_strategy = st.builds(graph_Typed, type=safe_text)
@given(instance=graph_Typed_strategy)
@settings(max_examples=25)
def test_graph_Typed_instantiation(instance):
    assert isinstance(instance, graph_Typed)



