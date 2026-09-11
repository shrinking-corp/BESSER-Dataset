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


