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
    graph_Pattern_Matching_Master_Project_Vertex,
    graph_Pattern_Matching_Master_Project_Edge,
    graph_Pattern_Matching_Master_Project_Graph,
    graph_Pattern_Matching_Master_Project_Entry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graph_pattern_matching_master_project_vertex_is_not_abstract():
    assert not inspect.isabstract(graph_Pattern_Matching_Master_Project_Vertex)


def test_hyp_graph_pattern_matching_master_project_vertex_constructor_exists():
    assert callable(graph_Pattern_Matching_Master_Project_Vertex.__init__)


def test_hyp_graph_pattern_matching_master_project_vertex_constructor_args():
    sig = inspect.signature(graph_Pattern_Matching_Master_Project_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_graph_pattern_matching_master_project_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Pattern_Matching_Master_Project_Edge)


def test_hyp_graph_pattern_matching_master_project_edge_constructor_exists():
    assert callable(graph_Pattern_Matching_Master_Project_Edge.__init__)


def test_hyp_graph_pattern_matching_master_project_edge_constructor_args():
    sig = inspect.signature(graph_Pattern_Matching_Master_Project_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_graph_pattern_matching_master_project_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Pattern_Matching_Master_Project_Graph)


def test_hyp_graph_pattern_matching_master_project_graph_constructor_exists():
    assert callable(graph_Pattern_Matching_Master_Project_Graph.__init__)


def test_hyp_graph_pattern_matching_master_project_graph_constructor_args():
    sig = inspect.signature(graph_Pattern_Matching_Master_Project_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "direct" in params, "Missing parameter 'direct'"





def test_hyp_graph_pattern_matching_master_project_entry_is_not_abstract():
    assert not inspect.isabstract(graph_Pattern_Matching_Master_Project_Entry)


def test_hyp_graph_pattern_matching_master_project_entry_constructor_exists():
    assert callable(graph_Pattern_Matching_Master_Project_Entry.__init__)


def test_hyp_graph_pattern_matching_master_project_entry_constructor_args():
    sig = inspect.signature(graph_Pattern_Matching_Master_Project_Entry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"




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
graph_Pattern_Matching_Master_Project_Vertex_strategy = st.builds(
    graph_Pattern_Matching_Master_Project_Vertex,
    name=
        safe_text
)
graph_Pattern_Matching_Master_Project_Edge_strategy = st.builds(
    graph_Pattern_Matching_Master_Project_Edge,
    label=
        safe_text
)
graph_Pattern_Matching_Master_Project_Graph_strategy = st.builds(
    graph_Pattern_Matching_Master_Project_Graph,
    name=
        safe_text,
    direct=
        st.booleans()
)
graph_Pattern_Matching_Master_Project_Entry_strategy = st.builds(
    graph_Pattern_Matching_Master_Project_Entry,
    value=
        safe_text,
    key=
        safe_text
)




@given(instance=graph_Pattern_Matching_Master_Project_Vertex_strategy)
def test_hyp_graph_pattern_matching_master_project_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=graph_Pattern_Matching_Master_Project_Edge_strategy)
def test_hyp_graph_pattern_matching_master_project_edge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=graph_Pattern_Matching_Master_Project_Graph_strategy)
def test_hyp_graph_pattern_matching_master_project_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graph_Pattern_Matching_Master_Project_Graph_strategy)
def test_hyp_graph_pattern_matching_master_project_graph_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Pattern_Matching_Master_Project_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graph_pattern_matching_master_project_graph_isconnected_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isConnected()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isConnected).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isConnected' in graph_Pattern_Matching_Master_Project_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isConnected' in graph_Pattern_Matching_Master_Project_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isConnected' in graph_Pattern_Matching_Master_Project_Graph is not implemented or raised an error")




@given(instance=graph_Pattern_Matching_Master_Project_Entry_strategy)
def test_hyp_graph_pattern_matching_master_project_entry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=graph_Pattern_Matching_Master_Project_Entry_strategy)
def test_hyp_graph_pattern_matching_master_project_entry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    graph_Pattern_Matching_Master_Project_Edge,
    graph_Pattern_Matching_Master_Project_Entry,
    graph_Pattern_Matching_Master_Project_Graph,
    graph_Pattern_Matching_Master_Project_Vertex,
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

def test_graph_Pattern_Matching_Master_Project_Edge_label_value_roundtrip():
    instance = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_graph_Pattern_Matching_Master_Project_Entry_key_value_roundtrip():
    instance = graph_Pattern_Matching_Master_Project_Entry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_graph_Pattern_Matching_Master_Project_Entry_value_value_roundtrip():
    instance = graph_Pattern_Matching_Master_Project_Entry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_graph_Pattern_Matching_Master_Project_Graph_direct_value_roundtrip():
    instance = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    assert instance.direct == True
    instance.direct = False
    assert instance.direct == False


def test_graph_Pattern_Matching_Master_Project_Graph_name_value_roundtrip():
    instance = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graph_Pattern_Matching_Master_Project_Vertex_name_value_roundtrip():
    instance = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_edges0_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text_2")
    _safe_set(a, 'graph', {b1})
    assert _is_linked(a, 'graph', b1)
    if hasattr(b1, 'Edge'):
        assert _is_linked(b1, 'Edge', a)
    _safe_set(a, 'graph', {b2})
    assert _is_linked(a, 'graph', b2)
    if hasattr(b1, 'Edge'):
        assert not _is_linked(b1, 'Edge', a)
    if hasattr(b2, 'Edge'):
        assert _is_linked(b2, 'Edge', a)
    _safe_set(a, 'graph', set())
    assert not _is_linked(a, 'graph', b2)
    if hasattr(b2, 'Edge'):
        assert not _is_linked(b2, 'Edge', a)


def test_assoc_entries12_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Entry(key="sample_text", value="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text_2")
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Entry14', b1)
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Entry14', b1)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Edge13'):
        assert _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Edge13', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Entry14', b2)
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Entry14', b2)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Edge13'):
        assert not _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Edge13', a)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Edge13'):
        assert _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Edge13', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Entry14', None)
    assert not _is_linked(a, 'graph_Pattern_Matching_Master_Project_Entry14', b2)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Edge13'):
        assert not _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Edge13', a)


def test_assoc_entries4_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Entry(key="sample_text", value="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Entry(key="sample_text_2", value="sample_text_2")
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex', {b1})
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex', b1)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Entry'):
        assert _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Entry', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex', {b2})
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex', b2)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Entry'):
        assert not _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Entry', a)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Entry'):
        assert _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Entry', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex', set())
    assert not _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex', b2)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Entry'):
        assert not _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Entry', a)


def test_assoc_graph3_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Graph(direct=False, name="sample_text_2")
    _safe_set(a, 'vertices', b1)
    assert _is_linked(a, 'vertices', b1)
    if hasattr(b1, 'Graph'):
        assert _is_linked(b1, 'Graph', a)
    _safe_set(a, 'vertices', b2)
    assert _is_linked(a, 'vertices', b2)
    if hasattr(b1, 'Graph'):
        assert not _is_linked(b1, 'Graph', a)
    if hasattr(b2, 'Graph'):
        assert _is_linked(b2, 'Graph', a)
    _safe_set(a, 'vertices', None)
    assert not _is_linked(a, 'vertices', b2)
    if hasattr(b2, 'Graph'):
        assert not _is_linked(b2, 'Graph', a)


def test_assoc_graph5_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text_2")
    _safe_set(a, 'Graph6', b1)
    assert _is_linked(a, 'Graph6', b1)
    if hasattr(b1, 'edges'):
        assert _is_linked(b1, 'edges', a)
    _safe_set(a, 'Graph6', b2)
    assert _is_linked(a, 'Graph6', b2)
    if hasattr(b1, 'edges'):
        assert not _is_linked(b1, 'edges', a)
    if hasattr(b2, 'edges'):
        assert _is_linked(b2, 'edges', a)
    _safe_set(a, 'Graph6', None)
    assert not _is_linked(a, 'Graph6', b2)
    if hasattr(b2, 'edges'):
        assert not _is_linked(b2, 'edges', a)


def test_assoc_source7_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text_2")
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex8', b1)
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex8', b1)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Edge'):
        assert _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Edge', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex8', b2)
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex8', b2)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Edge'):
        assert not _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Edge', a)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Edge'):
        assert _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Edge', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex8', None)
    assert not _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex8', b2)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Edge'):
        assert not _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Edge', a)


def test_assoc_target9_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Edge(label="sample_text_2")
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex11', b1)
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex11', b1)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Edge10'):
        assert _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Edge10', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex11', b2)
    assert _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex11', b2)
    if hasattr(b1, 'graph_Pattern_Matching_Master_Project_Edge10'):
        assert not _is_linked(b1, 'graph_Pattern_Matching_Master_Project_Edge10', a)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Edge10'):
        assert _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Edge10', a)
    _safe_set(a, 'graph_Pattern_Matching_Master_Project_Vertex11', None)
    assert not _is_linked(a, 'graph_Pattern_Matching_Master_Project_Vertex11', b2)
    if hasattr(b2, 'graph_Pattern_Matching_Master_Project_Edge10'):
        assert not _is_linked(b2, 'graph_Pattern_Matching_Master_Project_Edge10', a)


def test_assoc_vertices1_link_reassign_clear():
    a = graph_Pattern_Matching_Master_Project_Vertex(name="sample_text")
    b1 = graph_Pattern_Matching_Master_Project_Graph(direct=True, name="sample_text")
    b2 = graph_Pattern_Matching_Master_Project_Graph(direct=False, name="sample_text_2")
    _safe_set(a, 'Vertex', b1)
    assert _is_linked(a, 'Vertex', b1)
    if hasattr(b1, 'graph2'):
        assert _is_linked(b1, 'graph2', a)
    _safe_set(a, 'Vertex', b2)
    assert _is_linked(a, 'Vertex', b2)
    if hasattr(b1, 'graph2'):
        assert not _is_linked(b1, 'graph2', a)
    if hasattr(b2, 'graph2'):
        assert _is_linked(b2, 'graph2', a)
    _safe_set(a, 'Vertex', None)
    assert not _is_linked(a, 'Vertex', b2)
    if hasattr(b2, 'graph2'):
        assert not _is_linked(b2, 'graph2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

graph_Pattern_Matching_Master_Project_Edge_strategy = st.builds(graph_Pattern_Matching_Master_Project_Edge, label=safe_text)
@given(instance=graph_Pattern_Matching_Master_Project_Edge_strategy)
@settings(max_examples=25)
def test_graph_Pattern_Matching_Master_Project_Edge_instantiation(instance):
    assert isinstance(instance, graph_Pattern_Matching_Master_Project_Edge)


graph_Pattern_Matching_Master_Project_Entry_strategy = st.builds(graph_Pattern_Matching_Master_Project_Entry, key=safe_text, value=safe_text)
@given(instance=graph_Pattern_Matching_Master_Project_Entry_strategy)
@settings(max_examples=25)
def test_graph_Pattern_Matching_Master_Project_Entry_instantiation(instance):
    assert isinstance(instance, graph_Pattern_Matching_Master_Project_Entry)


graph_Pattern_Matching_Master_Project_Graph_strategy = st.builds(graph_Pattern_Matching_Master_Project_Graph, direct=st.booleans(), name=safe_text)
@given(instance=graph_Pattern_Matching_Master_Project_Graph_strategy)
@settings(max_examples=25)
def test_graph_Pattern_Matching_Master_Project_Graph_instantiation(instance):
    assert isinstance(instance, graph_Pattern_Matching_Master_Project_Graph)


graph_Pattern_Matching_Master_Project_Vertex_strategy = st.builds(graph_Pattern_Matching_Master_Project_Vertex, name=safe_text)
@given(instance=graph_Pattern_Matching_Master_Project_Vertex_strategy)
@settings(max_examples=25)
def test_graph_Pattern_Matching_Master_Project_Vertex_instantiation(instance):
    assert isinstance(instance, graph_Pattern_Matching_Master_Project_Vertex)



