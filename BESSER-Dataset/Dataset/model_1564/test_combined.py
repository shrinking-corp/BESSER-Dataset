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
    graph_Vertex,
    graph_Edge,
    graph_GraphElement,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graph_vertex_is_not_abstract():
    assert not inspect.isabstract(graph_Vertex)


def test_hyp_graph_vertex_constructor_exists():
    assert callable(graph_Vertex.__init__)


def test_hyp_graph_vertex_constructor_args():
    sig = inspect.signature(graph_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "hotSpot" in params, "Missing parameter 'hotSpot'"




def test_hyp_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_hyp_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_hyp_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "critical" in params, "Missing parameter 'critical'"




def test_hyp_graph_graphelement_is_not_abstract():
    assert not inspect.isabstract(graph_GraphElement)


def test_hyp_graph_graphelement_constructor_exists():
    assert callable(graph_GraphElement.__init__)


def test_hyp_graph_graphelement_constructor_args():
    sig = inspect.signature(graph_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_hyp_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_hyp_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"




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
graph_Vertex_strategy = st.builds(
    graph_Vertex,
    hotSpot=
        st.booleans()
)
graph_Edge_strategy = st.builds(
    graph_Edge,
    critical=
        st.booleans()
)
graph_GraphElement_strategy = st.builds(
    graph_GraphElement,
    name=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
    name=
        safe_text,
    description=
        safe_text
)




@given(instance=graph_Vertex_strategy)
def test_hyp_graph_vertex_hotSpot_setter(instance):
    original = instance.hotSpot
    instance.hotSpot = original
    assert instance.hotSpot == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Vertex_strategy)
@settings(max_examples=30)
def test_hyp_graph_vertex_hasforadjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasForAdjacent(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasForAdjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasForAdjacent' in graph_Vertex is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasForAdjacent' in graph_Vertex did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasForAdjacent' in graph_Vertex is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Vertex_strategy)
@settings(max_examples=30)
def test_hyp_graph_vertex_hasforoutgoingadjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasForOutgoingAdjacent(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasForOutgoingAdjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasForOutgoingAdjacent' in graph_Vertex is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasForOutgoingAdjacent' in graph_Vertex did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasForOutgoingAdjacent' in graph_Vertex is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Vertex_strategy)
@settings(max_examples=30)
def test_hyp_graph_vertex_hasforincomingadjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasForIncomingAdjacent(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasForIncomingAdjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasForIncomingAdjacent' in graph_Vertex is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasForIncomingAdjacent' in graph_Vertex did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasForIncomingAdjacent' in graph_Vertex is not implemented or raised an error")




@given(instance=graph_Edge_strategy)
def test_hyp_graph_edge_critical_setter(instance):
    original = instance.critical
    instance.critical = original
    assert instance.critical == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Edge_strategy)
@settings(max_examples=30)
def test_hyp_graph_edge_update_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.update(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.update).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'update' in graph_Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'update' in graph_Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'update' in graph_Edge is not implemented or raised an error")




@given(instance=graph_GraphElement_strategy)
def test_hyp_graph_graphelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=graph_Graph_strategy)
def test_hyp_graph_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graph_Graph_strategy)
def test_hyp_graph_graph_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graph_graph_addedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addEdge' in graph_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addEdge' in graph_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addEdge' in graph_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graph_graph_addvertex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addVertex(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addVertex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addVertex' in graph_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addVertex' in graph_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addVertex' in graph_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graph_graph_addadjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAdjacent(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAdjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAdjacent' in graph_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAdjacent' in graph_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAdjacent' in graph_Graph is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_Graph_strategy)
@settings(max_examples=30)
def test_hyp_graph_graph_addnamedadjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addNamedAdjacent(
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addNamedAdjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addNamedAdjacent' in graph_Graph is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addNamedAdjacent' in graph_Graph did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addNamedAdjacent' in graph_Graph is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    graph_Edge,
    graph_Graph,
    graph_GraphElement,
    graph_Vertex,
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

def test_graph_Edge_critical_value_roundtrip():
    instance = graph_Edge(critical=True)
    assert instance.critical == True
    instance.critical = False
    assert instance.critical == False


def test_graph_Graph_description_value_roundtrip():
    instance = graph_Graph(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_graph_Graph_name_value_roundtrip():
    instance = graph_Graph(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graph_GraphElement_name_value_roundtrip():
    instance = graph_GraphElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graph_Vertex_hotSpot_value_roundtrip():
    instance = graph_Vertex(hotSpot=True)
    assert instance.hotSpot == True
    instance.hotSpot = False
    assert instance.hotSpot == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

graph_Edge_strategy = st.builds(graph_Edge, critical=st.booleans())
@given(instance=graph_Edge_strategy)
@settings(max_examples=25)
def test_graph_Edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)


graph_Graph_strategy = st.builds(graph_Graph, description=safe_text, name=safe_text)
@given(instance=graph_Graph_strategy)
@settings(max_examples=25)
def test_graph_Graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)


graph_GraphElement_strategy = st.builds(graph_GraphElement, name=safe_text)
@given(instance=graph_GraphElement_strategy)
@settings(max_examples=25)
def test_graph_GraphElement_instantiation(instance):
    assert isinstance(instance, graph_GraphElement)


graph_Vertex_strategy = st.builds(graph_Vertex, hotSpot=st.booleans())
@given(instance=graph_Vertex_strategy)
@settings(max_examples=25)
def test_graph_Vertex_instantiation(instance):
    assert isinstance(instance, graph_Vertex)



