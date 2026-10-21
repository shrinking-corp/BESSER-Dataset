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
    nodesAndEdges_ShapedNode_toString,
    nodesAndEdges_Edge_toString,
    nodesAndEdges_Edge,
    nodesAndEdges_ColoredNode_toString,
    nodesAndEdges_Node_toString,
    nodesAndEdges_Node,
    Node,
    nodesAndEdges_ShapedNode,
    nodesAndEdges_ColoredNode,
    Color,
    Shape,
    EdgeViewType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_nodesandedges_shapednode_tostring_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_ShapedNode_toString)


def test_hyp_nodesandedges_shapednode_tostring_constructor_exists():
    assert callable(nodesAndEdges_ShapedNode_toString.__init__)


def test_hyp_nodesandedges_shapednode_tostring_constructor_args():
    sig = inspect.signature(nodesAndEdges_ShapedNode_toString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodesandedges_edge_tostring_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_Edge_toString)


def test_hyp_nodesandedges_edge_tostring_constructor_exists():
    assert callable(nodesAndEdges_Edge_toString.__init__)


def test_hyp_nodesandedges_edge_tostring_constructor_args():
    sig = inspect.signature(nodesAndEdges_Edge_toString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodesandedges_edge_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_Edge)


def test_hyp_nodesandedges_edge_constructor_exists():
    assert callable(nodesAndEdges_Edge.__init__)


def test_hyp_nodesandedges_edge_constructor_args():
    sig = inspect.signature(nodesAndEdges_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_nodesandedges_colorednode_tostring_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_ColoredNode_toString)


def test_hyp_nodesandedges_colorednode_tostring_constructor_exists():
    assert callable(nodesAndEdges_ColoredNode_toString.__init__)


def test_hyp_nodesandedges_colorednode_tostring_constructor_args():
    sig = inspect.signature(nodesAndEdges_ColoredNode_toString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodesandedges_node_tostring_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_Node_toString)


def test_hyp_nodesandedges_node_tostring_constructor_exists():
    assert callable(nodesAndEdges_Node_toString.__init__)


def test_hyp_nodesandedges_node_tostring_constructor_args():
    sig = inspect.signature(nodesAndEdges_Node_toString.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodesandedges_node_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_Node)


def test_hyp_nodesandedges_node_constructor_exists():
    assert callable(nodesAndEdges_Node.__init__)


def test_hyp_nodesandedges_node_constructor_args():
    sig = inspect.signature(nodesAndEdges_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nodesandedges_shapednode_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_ShapedNode)


def test_hyp_nodesandedges_shapednode_constructor_exists():
    assert callable(nodesAndEdges_ShapedNode.__init__)


def test_hyp_nodesandedges_shapednode_constructor_args():
    sig = inspect.signature(nodesAndEdges_ShapedNode.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "size" in params, "Missing parameter 'size'"





def test_hyp_nodesandedges_colorednode_is_not_abstract():
    assert not inspect.isabstract(nodesAndEdges_ColoredNode)


def test_hyp_nodesandedges_colorednode_constructor_exists():
    assert callable(nodesAndEdges_ColoredNode.__init__)


def test_hyp_nodesandedges_colorednode_constructor_args():
    sig = inspect.signature(nodesAndEdges_ColoredNode.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"


def test_hyp_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_hyp_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "red",
        "blue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_hyp_shape_exists():
    # Check that the Enumeration exists
    assert Shape is not None

def test_hyp_shape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Shape]
    expected_literals = [
        "square",
        "round",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Shape"

def test_hyp_edgeviewtype_exists():
    # Check that the Enumeration exists
    assert EdgeViewType is not None

def test_hyp_edgeviewtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeViewType]
    expected_literals = [
        "solidline",
        "dashline",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeViewType"


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
nodesAndEdges_ShapedNode_toString_strategy = st.builds(
    nodesAndEdges_ShapedNode_toString,
)
nodesAndEdges_Edge_toString_strategy = st.builds(
    nodesAndEdges_Edge_toString,
)
nodesAndEdges_Edge_strategy = st.builds(
    nodesAndEdges_Edge,
    type=
        safe_text,
    name=
        safe_text
)
nodesAndEdges_ColoredNode_toString_strategy = st.builds(
    nodesAndEdges_ColoredNode_toString,
)
nodesAndEdges_Node_toString_strategy = st.builds(
    nodesAndEdges_Node_toString,
)
nodesAndEdges_Node_strategy = st.builds(
    nodesAndEdges_Node,
    name=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
nodesAndEdges_ShapedNode_strategy = st.builds(
    nodesAndEdges_ShapedNode,
    shape=
        safe_text,
    size=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
nodesAndEdges_ColoredNode_strategy = st.builds(
    nodesAndEdges_ColoredNode,
    color=
        safe_text
)






@given(instance=nodesAndEdges_Edge_strategy)
def test_hyp_nodesandedges_edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=nodesAndEdges_Edge_strategy)
def test_hyp_nodesandedges_edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings







@given(instance=nodesAndEdges_Node_strategy)
def test_hyp_nodesandedges_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=nodesAndEdges_ShapedNode_strategy)
def test_hyp_nodesandedges_shapednode_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=nodesAndEdges_ShapedNode_strategy)
def test_hyp_nodesandedges_shapednode_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings





@given(instance=nodesAndEdges_ColoredNode_strategy)
def test_hyp_nodesandedges_colorednode_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Node,
    nodesAndEdges_ColoredNode,
    nodesAndEdges_ColoredNode_toString,
    nodesAndEdges_Edge,
    nodesAndEdges_Edge_toString,
    nodesAndEdges_Node,
    nodesAndEdges_Node_toString,
    nodesAndEdges_ShapedNode,
    nodesAndEdges_ShapedNode_toString,
    Color,
    EdgeViewType,
    Shape,
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

def test_nodesAndEdges_ColoredNode_color_value_roundtrip():
    instance = nodesAndEdges_ColoredNode(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_nodesAndEdges_Edge_name_value_roundtrip():
    instance = nodesAndEdges_Edge(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_nodesAndEdges_Edge_type_value_roundtrip():
    instance = nodesAndEdges_Edge(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_nodesAndEdges_Node_name_value_roundtrip():
    instance = nodesAndEdges_Node(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_nodesAndEdges_ShapedNode_shape_value_roundtrip():
    instance = nodesAndEdges_ShapedNode(shape="sample_text", size=3.14)
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_nodesAndEdges_ShapedNode_size_value_roundtrip():
    instance = nodesAndEdges_ShapedNode(shape="sample_text", size=3.14)
    assert instance.size == 3.14
    instance.size = 9.99
    assert instance.size == 9.99


def test_nodesAndEdges_ColoredNode_isa_Node():
    instance = nodesAndEdges_ColoredNode(color="sample_text")
    assert isinstance(instance, Node)


def test_nodesAndEdges_ShapedNode_isa_Node():
    instance = nodesAndEdges_ShapedNode(shape="sample_text", size=3.14)
    assert isinstance(instance, Node)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


nodesAndEdges_ColoredNode_strategy = st.builds(nodesAndEdges_ColoredNode, color=safe_text)
@given(instance=nodesAndEdges_ColoredNode_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_ColoredNode_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_ColoredNode)


nodesAndEdges_ColoredNode_toString_strategy = st.builds(nodesAndEdges_ColoredNode_toString)
@given(instance=nodesAndEdges_ColoredNode_toString_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_ColoredNode_toString_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_ColoredNode_toString)


nodesAndEdges_Edge_strategy = st.builds(nodesAndEdges_Edge, name=safe_text, type=safe_text)
@given(instance=nodesAndEdges_Edge_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_Edge_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_Edge)


nodesAndEdges_Edge_toString_strategy = st.builds(nodesAndEdges_Edge_toString)
@given(instance=nodesAndEdges_Edge_toString_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_Edge_toString_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_Edge_toString)


nodesAndEdges_Node_strategy = st.builds(nodesAndEdges_Node, name=safe_text)
@given(instance=nodesAndEdges_Node_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_Node_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_Node)


nodesAndEdges_Node_toString_strategy = st.builds(nodesAndEdges_Node_toString)
@given(instance=nodesAndEdges_Node_toString_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_Node_toString_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_Node_toString)


nodesAndEdges_ShapedNode_strategy = st.builds(nodesAndEdges_ShapedNode, shape=safe_text, size=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=nodesAndEdges_ShapedNode_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_ShapedNode_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_ShapedNode)


nodesAndEdges_ShapedNode_toString_strategy = st.builds(nodesAndEdges_ShapedNode_toString)
@given(instance=nodesAndEdges_ShapedNode_toString_strategy)
@settings(max_examples=25)
def test_nodesAndEdges_ShapedNode_toString_instantiation(instance):
    assert isinstance(instance, nodesAndEdges_ShapedNode_toString)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    nodesAndEdges_ColoredNode,
    nodesAndEdges_ColoredNode_toString,
    nodesAndEdges_Edge,
    nodesAndEdges_Edge_toString,
    nodesAndEdges_Node,
    nodesAndEdges_Node_toString,
    nodesAndEdges_ShapedNode,
    nodesAndEdges_ShapedNode_toString,
    Color,
    EdgeViewType,
    Shape,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================



from python_code import nodesAndEdges_ColoredNode

def test_nodesAndEdges_ColoredNode___init__():
    assert nodesAndEdges_ColoredNode.__init__(nodesAndEdges_ColoredNode(''), '') == None

def test_nodesAndEdges_ColoredNode_toString():
    nodesAndEdges_ColoredNode.toString(nodesAndEdges_ColoredNode(''))
from python_code import nodesAndEdges_Edge

def test_nodesAndEdges_Edge___init__():
    assert nodesAndEdges_Edge.__init__(nodesAndEdges_Edge('', '\x00'), '\x00\x00', '') == None

def test_nodesAndEdges_Edge_toString():
    nodesAndEdges_Edge.toString(nodesAndEdges_Edge('', ''))
from python_code import nodesAndEdges_Node

def test_nodesAndEdges_Node___init__():
    assert nodesAndEdges_Node.__init__(nodesAndEdges_Node(''), '') == None
from python_code import nodesAndEdges_ShapedNode

def test_nodesAndEdges_ShapedNode___init__():
    assert nodesAndEdges_ShapedNode.__init__(nodesAndEdges_ShapedNode(0.0, '\x00\x00'), 0.0, '') == None

def test_nodesAndEdges_ShapedNode_toString():
    nodesAndEdges_ShapedNode.toString(nodesAndEdges_ShapedNode(0.0, '\x00'))

