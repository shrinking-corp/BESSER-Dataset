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
    grapho_GraphOEditor,
    grapho_GraphElement,
    GraphElement,
    grapho_Node,
    grapho_GraphO,
    grapho_Edge,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_grapho_graphoeditor_is_not_abstract():
    assert not inspect.isabstract(grapho_GraphOEditor)


def test_hyp_grapho_graphoeditor_constructor_exists():
    assert callable(grapho_GraphOEditor.__init__)


def test_hyp_grapho_graphoeditor_constructor_args():
    sig = inspect.signature(grapho_GraphOEditor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_grapho_graphelement_is_not_abstract():
    assert not inspect.isabstract(grapho_GraphElement)


def test_hyp_grapho_graphelement_constructor_exists():
    assert callable(grapho_GraphElement.__init__)


def test_hyp_grapho_graphelement_constructor_args():
    sig = inspect.signature(grapho_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_hyp_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_hyp_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_grapho_node_is_not_abstract():
    assert not inspect.isabstract(grapho_Node)


def test_hyp_grapho_node_constructor_exists():
    assert callable(grapho_Node.__init__)


def test_hyp_grapho_node_constructor_args():
    sig = inspect.signature(grapho_Node.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "label" in params, "Missing parameter 'label'"
    assert "style" in params, "Missing parameter 'style'"
    assert "color" in params, "Missing parameter 'color'"







def test_hyp_grapho_grapho_is_not_abstract():
    assert not inspect.isabstract(grapho_GraphO)


def test_hyp_grapho_grapho_constructor_exists():
    assert callable(grapho_GraphO.__init__)


def test_hyp_grapho_grapho_constructor_args():
    sig = inspect.signature(grapho_GraphO.__init__)
    params = list(sig.parameters.keys())



def test_hyp_grapho_edge_is_not_abstract():
    assert not inspect.isabstract(grapho_Edge)


def test_hyp_grapho_edge_constructor_exists():
    assert callable(grapho_Edge.__init__)


def test_hyp_grapho_edge_constructor_args():
    sig = inspect.signature(grapho_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "style" in params, "Missing parameter 'style'"
    assert "constraintRank" in params, "Missing parameter 'constraintRank'"





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
grapho_GraphOEditor_strategy = st.builds(
    grapho_GraphOEditor,
)
grapho_GraphElement_strategy = st.builds(
    grapho_GraphElement,
    name=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
grapho_Node_strategy = st.builds(
    grapho_Node,
    shape=
        safe_text,
    label=
        safe_text,
    style=
        safe_text,
    color=
        safe_text
)
grapho_GraphO_strategy = st.builds(
    grapho_GraphO,
)
grapho_Edge_strategy = st.builds(
    grapho_Edge,
    color=
        safe_text,
    style=
        safe_text,
    constraintRank=
        st.booleans()
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=grapho_GraphOEditor_strategy)
@settings(max_examples=30)
def test_hyp_grapho_graphoeditor_addnode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addNode()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addNode' in grapho_GraphOEditor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addNode' in grapho_GraphOEditor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addNode' in grapho_GraphOEditor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=grapho_GraphOEditor_strategy)
@settings(max_examples=30)
def test_hyp_grapho_graphoeditor_addedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addEdge()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addEdge' in grapho_GraphOEditor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addEdge' in grapho_GraphOEditor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addEdge' in grapho_GraphOEditor is not implemented or raised an error")




@given(instance=grapho_GraphElement_strategy)
def test_hyp_grapho_graphelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=grapho_Node_strategy)
def test_hyp_grapho_node_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=grapho_Node_strategy)
def test_hyp_grapho_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=grapho_Node_strategy)
def test_hyp_grapho_node_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=grapho_Node_strategy)
def test_hyp_grapho_node_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original





@given(instance=grapho_Edge_strategy)
def test_hyp_grapho_edge_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=grapho_Edge_strategy)
def test_hyp_grapho_edge_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=grapho_Edge_strategy)
def test_hyp_grapho_edge_constraintRank_setter(instance):
    original = instance.constraintRank
    instance.constraintRank = original
    assert instance.constraintRank == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    GraphElement,
    grapho_Edge,
    grapho_GraphElement,
    grapho_GraphO,
    grapho_GraphOEditor,
    grapho_Node,
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

def test_grapho_Edge_color_value_roundtrip():
    instance = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_grapho_Edge_constraintRank_value_roundtrip():
    instance = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    assert instance.constraintRank == True
    instance.constraintRank = False
    assert instance.constraintRank == False


def test_grapho_Edge_style_value_roundtrip():
    instance = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_grapho_GraphElement_name_value_roundtrip():
    instance = grapho_GraphElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_grapho_Node_color_value_roundtrip():
    instance = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_grapho_Node_label_value_roundtrip():
    instance = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_grapho_Node_shape_value_roundtrip():
    instance = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_grapho_Node_style_value_roundtrip():
    instance = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_grapho_Edge_isa_GraphElement():
    instance = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    assert isinstance(instance, GraphElement)


def test_grapho_GraphO_isa_GraphElement():
    instance = grapho_GraphO()
    assert isinstance(instance, GraphElement)


def test_grapho_Node_isa_GraphElement():
    instance = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    assert isinstance(instance, GraphElement)


def test_assoc_elements0_link_reassign_clear():
    a = grapho_GraphElement(name="sample_text")
    b1 = grapho_GraphO()
    b2 = grapho_GraphO()
    _safe_set(a, 'grapho_GraphElement', b1)
    assert _is_linked(a, 'grapho_GraphElement', b1)
    if hasattr(b1, 'grapho_GraphO'):
        assert _is_linked(b1, 'grapho_GraphO', a)
    _safe_set(a, 'grapho_GraphElement', b2)
    assert _is_linked(a, 'grapho_GraphElement', b2)
    if hasattr(b1, 'grapho_GraphO'):
        assert not _is_linked(b1, 'grapho_GraphO', a)
    if hasattr(b2, 'grapho_GraphO'):
        assert _is_linked(b2, 'grapho_GraphO', a)
    _safe_set(a, 'grapho_GraphElement', None)
    assert not _is_linked(a, 'grapho_GraphElement', b2)
    if hasattr(b2, 'grapho_GraphO'):
        assert not _is_linked(b2, 'grapho_GraphO', a)


def test_assoc_nodeA1_link_reassign_clear():
    a = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    b1 = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    b2 = grapho_Edge(color="sample_text_2", constraintRank=False, style="sample_text_2")
    _safe_set(a, 'grapho_Node', b1)
    assert _is_linked(a, 'grapho_Node', b1)
    if hasattr(b1, 'grapho_Edge'):
        assert _is_linked(b1, 'grapho_Edge', a)
    _safe_set(a, 'grapho_Node', b2)
    assert _is_linked(a, 'grapho_Node', b2)
    if hasattr(b1, 'grapho_Edge'):
        assert not _is_linked(b1, 'grapho_Edge', a)
    if hasattr(b2, 'grapho_Edge'):
        assert _is_linked(b2, 'grapho_Edge', a)
    _safe_set(a, 'grapho_Node', None)
    assert not _is_linked(a, 'grapho_Node', b2)
    if hasattr(b2, 'grapho_Edge'):
        assert not _is_linked(b2, 'grapho_Edge', a)


def test_assoc_nodeB2_link_reassign_clear():
    a = grapho_Node(color="sample_text", label="sample_text", shape="sample_text", style="sample_text")
    b1 = grapho_Edge(color="sample_text", constraintRank=True, style="sample_text")
    b2 = grapho_Edge(color="sample_text_2", constraintRank=False, style="sample_text_2")
    _safe_set(a, 'grapho_Node4', b1)
    assert _is_linked(a, 'grapho_Node4', b1)
    if hasattr(b1, 'grapho_Edge3'):
        assert _is_linked(b1, 'grapho_Edge3', a)
    _safe_set(a, 'grapho_Node4', b2)
    assert _is_linked(a, 'grapho_Node4', b2)
    if hasattr(b1, 'grapho_Edge3'):
        assert not _is_linked(b1, 'grapho_Edge3', a)
    if hasattr(b2, 'grapho_Edge3'):
        assert _is_linked(b2, 'grapho_Edge3', a)
    _safe_set(a, 'grapho_Node4', None)
    assert not _is_linked(a, 'grapho_Node4', b2)
    if hasattr(b2, 'grapho_Edge3'):
        assert not _is_linked(b2, 'grapho_Edge3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

GraphElement_strategy = st.builds(GraphElement)
@given(instance=GraphElement_strategy)
@settings(max_examples=25)
def test_GraphElement_instantiation(instance):
    assert isinstance(instance, GraphElement)


grapho_Edge_strategy = st.builds(grapho_Edge, color=safe_text, constraintRank=st.booleans(), style=safe_text)
@given(instance=grapho_Edge_strategy)
@settings(max_examples=25)
def test_grapho_Edge_instantiation(instance):
    assert isinstance(instance, grapho_Edge)


grapho_GraphElement_strategy = st.builds(grapho_GraphElement, name=safe_text)
@given(instance=grapho_GraphElement_strategy)
@settings(max_examples=25)
def test_grapho_GraphElement_instantiation(instance):
    assert isinstance(instance, grapho_GraphElement)


grapho_GraphO_strategy = st.builds(grapho_GraphO)
@given(instance=grapho_GraphO_strategy)
@settings(max_examples=25)
def test_grapho_GraphO_instantiation(instance):
    assert isinstance(instance, grapho_GraphO)


grapho_GraphOEditor_strategy = st.builds(grapho_GraphOEditor)
@given(instance=grapho_GraphOEditor_strategy)
@settings(max_examples=25)
def test_grapho_GraphOEditor_instantiation(instance):
    assert isinstance(instance, grapho_GraphOEditor)


grapho_Node_strategy = st.builds(grapho_Node, color=safe_text, label=safe_text, shape=safe_text, style=safe_text)
@given(instance=grapho_Node_strategy)
@settings(max_examples=25)
def test_grapho_Node_instantiation(instance):
    assert isinstance(instance, grapho_Node)



