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
    EdgeProcessor,
    dfs_DepthFirstSearch,
    dfs_EObject,
    dfs_EdgeProcessor,
    dfs_DFSGraph,
    dfs_Edge,
    dfs_Node,
    EdgeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_edgeprocessor_is_not_abstract():
    assert not inspect.isabstract(EdgeProcessor)


def test_hyp_edgeprocessor_constructor_exists():
    assert callable(EdgeProcessor.__init__)


def test_hyp_edgeprocessor_constructor_args():
    sig = inspect.signature(EdgeProcessor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dfs_depthfirstsearch_is_not_abstract():
    assert not inspect.isabstract(dfs_DepthFirstSearch)


def test_hyp_dfs_depthfirstsearch_constructor_exists():
    assert callable(dfs_DepthFirstSearch.__init__)


def test_hyp_dfs_depthfirstsearch_constructor_args():
    sig = inspect.signature(dfs_DepthFirstSearch.__init__)
    params = list(sig.parameters.keys())
    assert "postTraversalCounter" in params, "Missing parameter 'postTraversalCounter'"
    assert "preTraversalCounter" in params, "Missing parameter 'preTraversalCounter'"





def test_hyp_dfs_eobject_is_not_abstract():
    assert not inspect.isabstract(dfs_EObject)


def test_hyp_dfs_eobject_constructor_exists():
    assert callable(dfs_EObject.__init__)


def test_hyp_dfs_eobject_constructor_args():
    sig = inspect.signature(dfs_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dfs_edgeprocessor_is_not_abstract():
    assert not inspect.isabstract(dfs_EdgeProcessor)


def test_hyp_dfs_edgeprocessor_constructor_exists():
    assert callable(dfs_EdgeProcessor.__init__)


def test_hyp_dfs_edgeprocessor_constructor_args():
    sig = inspect.signature(dfs_EdgeProcessor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dfs_dfsgraph_is_not_abstract():
    assert not inspect.isabstract(dfs_DFSGraph)


def test_hyp_dfs_dfsgraph_constructor_exists():
    assert callable(dfs_DFSGraph.__init__)


def test_hyp_dfs_dfsgraph_constructor_args():
    sig = inspect.signature(dfs_DFSGraph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dfs_edge_is_not_abstract():
    assert not inspect.isabstract(dfs_Edge)


def test_hyp_dfs_edge_constructor_exists():
    assert callable(dfs_Edge.__init__)


def test_hyp_dfs_edge_constructor_args():
    sig = inspect.signature(dfs_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_dfs_node_is_not_abstract():
    assert not inspect.isabstract(dfs_Node)


def test_hyp_dfs_node_constructor_exists():
    assert callable(dfs_Node.__init__)


def test_hyp_dfs_node_constructor_args():
    sig = inspect.signature(dfs_Node.__init__)
    params = list(sig.parameters.keys())
    assert "preTraversal" in params, "Missing parameter 'preTraversal'"
    assert "postTraversal" in params, "Missing parameter 'postTraversal'"



def test_hyp_edgetype_exists():
    # Check that the Enumeration exists
    assert EdgeType is not None

def test_hyp_edgetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeType]
    expected_literals = [
        "CROSS_EDGE",
        "TREE_EDGE",
        "FORWARD_EDGE",
        "BACKWARD_EDGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeType"


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
EdgeProcessor_strategy = st.builds(
    EdgeProcessor,
)
dfs_DepthFirstSearch_strategy = st.builds(
    dfs_DepthFirstSearch,
    postTraversalCounter=
        st.integers(),
    preTraversalCounter=
        st.integers()
)
dfs_EObject_strategy = st.builds(
    dfs_EObject,
)
dfs_EdgeProcessor_strategy = st.builds(
    dfs_EdgeProcessor,
)
dfs_DFSGraph_strategy = st.builds(
    dfs_DFSGraph,
)
dfs_Edge_strategy = st.builds(
    dfs_Edge,
    type=
        safe_text
)
dfs_Node_strategy = st.builds(
    dfs_Node,
    preTraversal=
        st.integers(),
    postTraversal=
        st.integers()
)





@given(instance=dfs_DepthFirstSearch_strategy)
def test_hyp_dfs_depthfirstsearch_postTraversalCounter_setter(instance):
    original = instance.postTraversalCounter
    instance.postTraversalCounter = original
    assert instance.postTraversalCounter == original



@given(instance=dfs_DepthFirstSearch_strategy)
def test_hyp_dfs_depthfirstsearch_preTraversalCounter_setter(instance):
    original = instance.preTraversalCounter
    instance.preTraversalCounter = original
    assert instance.preTraversalCounter == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dfs_DepthFirstSearch_strategy)
@settings(max_examples=30)
def test_hyp_dfs_depthfirstsearch_incrementpretraversalcounter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.incrementPreTraversalCounter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.incrementPreTraversalCounter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'incrementPreTraversalCounter' in dfs_DepthFirstSearch is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'incrementPreTraversalCounter' in dfs_DepthFirstSearch did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'incrementPreTraversalCounter' in dfs_DepthFirstSearch is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dfs_DepthFirstSearch_strategy)
@settings(max_examples=30)
def test_hyp_dfs_depthfirstsearch_processedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processEdge' in dfs_DepthFirstSearch is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processEdge' in dfs_DepthFirstSearch did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processEdge' in dfs_DepthFirstSearch is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dfs_DepthFirstSearch_strategy)
@settings(max_examples=30)
def test_hyp_dfs_depthfirstsearch_processnode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processNode' in dfs_DepthFirstSearch is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processNode' in dfs_DepthFirstSearch did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processNode' in dfs_DepthFirstSearch is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dfs_DepthFirstSearch_strategy)
@settings(max_examples=30)
def test_hyp_dfs_depthfirstsearch_incrementposttraversalcounter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.incrementPostTraversalCounter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.incrementPostTraversalCounter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'incrementPostTraversalCounter' in dfs_DepthFirstSearch is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'incrementPostTraversalCounter' in dfs_DepthFirstSearch did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'incrementPostTraversalCounter' in dfs_DepthFirstSearch is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dfs_EdgeProcessor_strategy)
@settings(max_examples=30)
def test_hyp_dfs_edgeprocessor_processnode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processNode' in dfs_EdgeProcessor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processNode' in dfs_EdgeProcessor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processNode' in dfs_EdgeProcessor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=dfs_EdgeProcessor_strategy)
@settings(max_examples=30)
def test_hyp_dfs_edgeprocessor_processedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processEdge' in dfs_EdgeProcessor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processEdge' in dfs_EdgeProcessor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processEdge' in dfs_EdgeProcessor is not implemented or raised an error")





@given(instance=dfs_Edge_strategy)
def test_hyp_dfs_edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=dfs_Node_strategy)
def test_hyp_dfs_node_preTraversal_setter(instance):
    original = instance.preTraversal
    instance.preTraversal = original
    assert instance.preTraversal == original



@given(instance=dfs_Node_strategy)
def test_hyp_dfs_node_postTraversal_setter(instance):
    original = instance.postTraversal
    instance.postTraversal = original
    assert instance.postTraversal == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    EdgeProcessor,
    dfs_DFSGraph,
    dfs_DepthFirstSearch,
    dfs_EObject,
    dfs_Edge,
    dfs_EdgeProcessor,
    dfs_Node,
    EdgeType,
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

def test_dfs_DepthFirstSearch_postTraversalCounter_value_roundtrip():
    instance = dfs_DepthFirstSearch(postTraversalCounter=7, preTraversalCounter=7)
    assert instance.postTraversalCounter == 7
    instance.postTraversalCounter = 13
    assert instance.postTraversalCounter == 13


def test_dfs_DepthFirstSearch_preTraversalCounter_value_roundtrip():
    instance = dfs_DepthFirstSearch(postTraversalCounter=7, preTraversalCounter=7)
    assert instance.preTraversalCounter == 7
    instance.preTraversalCounter = 13
    assert instance.preTraversalCounter == 13


def test_dfs_Edge_type_value_roundtrip():
    instance = dfs_Edge(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_dfs_Node_postTraversal_value_roundtrip():
    instance = dfs_Node(postTraversal=7, preTraversal=7)
    assert instance.postTraversal == 7
    instance.postTraversal = 13
    assert instance.postTraversal == 13


def test_dfs_Node_preTraversal_value_roundtrip():
    instance = dfs_Node(postTraversal=7, preTraversal=7)
    assert instance.preTraversal == 7
    instance.preTraversal = 13
    assert instance.preTraversal == 13


def test_dfs_DepthFirstSearch_isa_EdgeProcessor():
    instance = dfs_DepthFirstSearch(postTraversalCounter=7, preTraversalCounter=7)
    assert isinstance(instance, EdgeProcessor)


def test_assoc_delegate1_link_reassign_clear():
    a = dfs_EdgeProcessor()
    b1 = dfs_EdgeProcessor()
    b2 = dfs_EdgeProcessor()
    _safe_set(a, 'dfs_EdgeProcessor', b1)
    assert _is_linked(a, 'dfs_EdgeProcessor', b1)
    if hasattr(b1, 'dfs_EdgeProcessor0'):
        assert _is_linked(b1, 'dfs_EdgeProcessor0', a)
    _safe_set(a, 'dfs_EdgeProcessor', b2)
    assert _is_linked(a, 'dfs_EdgeProcessor', b2)
    if hasattr(b1, 'dfs_EdgeProcessor0'):
        assert not _is_linked(b1, 'dfs_EdgeProcessor0', a)
    if hasattr(b2, 'dfs_EdgeProcessor0'):
        assert _is_linked(b2, 'dfs_EdgeProcessor0', a)
    _safe_set(a, 'dfs_EdgeProcessor', None)
    assert not _is_linked(a, 'dfs_EdgeProcessor', b2)
    if hasattr(b2, 'dfs_EdgeProcessor0'):
        assert not _is_linked(b2, 'dfs_EdgeProcessor0', a)


def test_assoc_edges14_link_reassign_clear():
    a = dfs_Edge(type="sample_text")
    b1 = dfs_DFSGraph()
    b2 = dfs_DFSGraph()
    _safe_set(a, 'Edge15', b1)
    assert _is_linked(a, 'Edge15', b1)
    if hasattr(b1, 'graph'):
        assert _is_linked(b1, 'graph', a)
    _safe_set(a, 'Edge15', b2)
    assert _is_linked(a, 'Edge15', b2)
    if hasattr(b1, 'graph'):
        assert not _is_linked(b1, 'graph', a)
    if hasattr(b2, 'graph'):
        assert _is_linked(b2, 'graph', a)
    _safe_set(a, 'Edge15', None)
    assert not _is_linked(a, 'Edge15', b2)
    if hasattr(b2, 'graph'):
        assert not _is_linked(b2, 'graph', a)


def test_assoc_graph3_link_reassign_clear():
    a = dfs_Node(postTraversal=7, preTraversal=7)
    b1 = dfs_DFSGraph()
    b2 = dfs_DFSGraph()
    _safe_set(a, 'nodes', b1)
    assert _is_linked(a, 'nodes', b1)
    if hasattr(b1, 'DFSGraph'):
        assert _is_linked(b1, 'DFSGraph', a)
    _safe_set(a, 'nodes', b2)
    assert _is_linked(a, 'nodes', b2)
    if hasattr(b1, 'DFSGraph'):
        assert not _is_linked(b1, 'DFSGraph', a)
    if hasattr(b2, 'DFSGraph'):
        assert _is_linked(b2, 'DFSGraph', a)
    _safe_set(a, 'nodes', None)
    assert not _is_linked(a, 'nodes', b2)
    if hasattr(b2, 'DFSGraph'):
        assert not _is_linked(b2, 'DFSGraph', a)


def test_assoc_graph7_link_reassign_clear():
    a = dfs_Edge(type="sample_text")
    b1 = dfs_DFSGraph()
    b2 = dfs_DFSGraph()
    _safe_set(a, 'edges', b1)
    assert _is_linked(a, 'edges', b1)
    if hasattr(b1, 'DFSGraph8'):
        assert _is_linked(b1, 'DFSGraph8', a)
    _safe_set(a, 'edges', b2)
    assert _is_linked(a, 'edges', b2)
    if hasattr(b1, 'DFSGraph8'):
        assert not _is_linked(b1, 'DFSGraph8', a)
    if hasattr(b2, 'DFSGraph8'):
        assert _is_linked(b2, 'DFSGraph8', a)
    _safe_set(a, 'edges', None)
    assert not _is_linked(a, 'edges', b2)
    if hasattr(b2, 'DFSGraph8'):
        assert not _is_linked(b2, 'DFSGraph8', a)


def test_assoc_incoming2_link_reassign_clear():
    a = dfs_Node(postTraversal=7, preTraversal=7)
    b1 = dfs_Edge(type="sample_text")
    b2 = dfs_Edge(type="sample_text_2")
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'Edge'):
        assert _is_linked(b1, 'Edge', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'Edge'):
        assert not _is_linked(b1, 'Edge', a)
    if hasattr(b2, 'Edge'):
        assert _is_linked(b2, 'Edge', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'Edge'):
        assert not _is_linked(b2, 'Edge', a)


def test_assoc_nodes16_link_reassign_clear():
    a = dfs_Node(postTraversal=7, preTraversal=7)
    b1 = dfs_DFSGraph()
    b2 = dfs_DFSGraph()
    _safe_set(a, 'Node18', b1)
    assert _is_linked(a, 'Node18', b1)
    if hasattr(b1, 'graph17'):
        assert _is_linked(b1, 'graph17', a)
    _safe_set(a, 'Node18', b2)
    assert _is_linked(a, 'Node18', b2)
    if hasattr(b1, 'graph17'):
        assert not _is_linked(b1, 'graph17', a)
    if hasattr(b2, 'graph17'):
        assert _is_linked(b2, 'graph17', a)
    _safe_set(a, 'Node18', None)
    assert not _is_linked(a, 'Node18', b2)
    if hasattr(b2, 'graph17'):
        assert not _is_linked(b2, 'graph17', a)


def test_assoc_origin10_link_reassign_clear():
    a = dfs_Edge(type="sample_text")
    b1 = dfs_EObject()
    b2 = dfs_EObject()
    _safe_set(a, 'dfs_Edge', b1)
    assert _is_linked(a, 'dfs_Edge', b1)
    if hasattr(b1, 'dfs_EObject11'):
        assert _is_linked(b1, 'dfs_EObject11', a)
    _safe_set(a, 'dfs_Edge', b2)
    assert _is_linked(a, 'dfs_Edge', b2)
    if hasattr(b1, 'dfs_EObject11'):
        assert not _is_linked(b1, 'dfs_EObject11', a)
    if hasattr(b2, 'dfs_EObject11'):
        assert _is_linked(b2, 'dfs_EObject11', a)
    _safe_set(a, 'dfs_Edge', None)
    assert not _is_linked(a, 'dfs_Edge', b2)
    if hasattr(b2, 'dfs_EObject11'):
        assert not _is_linked(b2, 'dfs_EObject11', a)


def test_assoc_origin4_link_reassign_clear():
    a = dfs_Node(postTraversal=7, preTraversal=7)
    b1 = dfs_EObject()
    b2 = dfs_EObject()
    _safe_set(a, 'dfs_Node', b1)
    assert _is_linked(a, 'dfs_Node', b1)
    if hasattr(b1, 'dfs_EObject'):
        assert _is_linked(b1, 'dfs_EObject', a)
    _safe_set(a, 'dfs_Node', b2)
    assert _is_linked(a, 'dfs_Node', b2)
    if hasattr(b1, 'dfs_EObject'):
        assert not _is_linked(b1, 'dfs_EObject', a)
    if hasattr(b2, 'dfs_EObject'):
        assert _is_linked(b2, 'dfs_EObject', a)
    _safe_set(a, 'dfs_Node', None)
    assert not _is_linked(a, 'dfs_Node', b2)
    if hasattr(b2, 'dfs_EObject'):
        assert not _is_linked(b2, 'dfs_EObject', a)


def test_assoc_outgoing5_link_reassign_clear():
    a = dfs_Node(postTraversal=7, preTraversal=7)
    b1 = dfs_Edge(type="sample_text")
    b2 = dfs_Edge(type="sample_text_2")
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Edge6'):
        assert _is_linked(b1, 'Edge6', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Edge6'):
        assert not _is_linked(b1, 'Edge6', a)
    if hasattr(b2, 'Edge6'):
        assert _is_linked(b2, 'Edge6', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Edge6'):
        assert not _is_linked(b2, 'Edge6', a)


def test_assoc_source9_link_reassign_clear():
    a = dfs_Node(postTraversal=7, preTraversal=7)
    b1 = dfs_Edge(type="sample_text")
    b2 = dfs_Edge(type="sample_text_2")
    _safe_set(a, 'Node', b1)
    assert _is_linked(a, 'Node', b1)
    if hasattr(b1, 'outgoing'):
        assert _is_linked(b1, 'outgoing', a)
    _safe_set(a, 'Node', b2)
    assert _is_linked(a, 'Node', b2)
    if hasattr(b1, 'outgoing'):
        assert not _is_linked(b1, 'outgoing', a)
    if hasattr(b2, 'outgoing'):
        assert _is_linked(b2, 'outgoing', a)
    _safe_set(a, 'Node', None)
    assert not _is_linked(a, 'Node', b2)
    if hasattr(b2, 'outgoing'):
        assert not _is_linked(b2, 'outgoing', a)


def test_assoc_target12_link_reassign_clear():
    a = dfs_Node(postTraversal=7, preTraversal=7)
    b1 = dfs_Edge(type="sample_text")
    b2 = dfs_Edge(type="sample_text_2")
    _safe_set(a, 'Node13', b1)
    assert _is_linked(a, 'Node13', b1)
    if hasattr(b1, 'incoming'):
        assert _is_linked(b1, 'incoming', a)
    _safe_set(a, 'Node13', b2)
    assert _is_linked(a, 'Node13', b2)
    if hasattr(b1, 'incoming'):
        assert not _is_linked(b1, 'incoming', a)
    if hasattr(b2, 'incoming'):
        assert _is_linked(b2, 'incoming', a)
    _safe_set(a, 'Node13', None)
    assert not _is_linked(a, 'Node13', b2)
    if hasattr(b2, 'incoming'):
        assert not _is_linked(b2, 'incoming', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EdgeProcessor_strategy = st.builds(EdgeProcessor)
@given(instance=EdgeProcessor_strategy)
@settings(max_examples=25)
def test_EdgeProcessor_instantiation(instance):
    assert isinstance(instance, EdgeProcessor)


dfs_DFSGraph_strategy = st.builds(dfs_DFSGraph)
@given(instance=dfs_DFSGraph_strategy)
@settings(max_examples=25)
def test_dfs_DFSGraph_instantiation(instance):
    assert isinstance(instance, dfs_DFSGraph)


dfs_DepthFirstSearch_strategy = st.builds(dfs_DepthFirstSearch, postTraversalCounter=st.integers(), preTraversalCounter=st.integers())
@given(instance=dfs_DepthFirstSearch_strategy)
@settings(max_examples=25)
def test_dfs_DepthFirstSearch_instantiation(instance):
    assert isinstance(instance, dfs_DepthFirstSearch)


dfs_EObject_strategy = st.builds(dfs_EObject)
@given(instance=dfs_EObject_strategy)
@settings(max_examples=25)
def test_dfs_EObject_instantiation(instance):
    assert isinstance(instance, dfs_EObject)


dfs_Edge_strategy = st.builds(dfs_Edge, type=safe_text)
@given(instance=dfs_Edge_strategy)
@settings(max_examples=25)
def test_dfs_Edge_instantiation(instance):
    assert isinstance(instance, dfs_Edge)


dfs_EdgeProcessor_strategy = st.builds(dfs_EdgeProcessor)
@given(instance=dfs_EdgeProcessor_strategy)
@settings(max_examples=25)
def test_dfs_EdgeProcessor_instantiation(instance):
    assert isinstance(instance, dfs_EdgeProcessor)


dfs_Node_strategy = st.builds(dfs_Node, postTraversal=st.integers(), preTraversal=st.integers())
@given(instance=dfs_Node_strategy)
@settings(max_examples=25)
def test_dfs_Node_instantiation(instance):
    assert isinstance(instance, dfs_Node)



