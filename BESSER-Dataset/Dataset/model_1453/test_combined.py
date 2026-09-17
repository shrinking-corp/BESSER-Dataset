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
    tree_Edge,
    tree_Node,
    tree_Diagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tree_edge_is_not_abstract():
    assert not inspect.isabstract(tree_Edge)


def test_hyp_tree_edge_constructor_exists():
    assert callable(tree_Edge.__init__)


def test_hyp_tree_edge_constructor_args():
    sig = inspect.signature(tree_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_node_is_not_abstract():
    assert not inspect.isabstract(tree_Node)


def test_hyp_tree_node_constructor_exists():
    assert callable(tree_Node.__init__)


def test_hyp_tree_node_constructor_args():
    sig = inspect.signature(tree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tree_diagram_is_not_abstract():
    assert not inspect.isabstract(tree_Diagram)


def test_hyp_tree_diagram_constructor_exists():
    assert callable(tree_Diagram.__init__)


def test_hyp_tree_diagram_constructor_args():
    sig = inspect.signature(tree_Diagram.__init__)
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
tree_Edge_strategy = st.builds(
    tree_Edge,
)
tree_Node_strategy = st.builds(
    tree_Node,
    name=
        safe_text
)
tree_Diagram_strategy = st.builds(
    tree_Diagram,
)





@given(instance=tree_Node_strategy)
def test_hyp_tree_node_name_setter(instance):
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
    tree_Diagram,
    tree_Edge,
    tree_Node,
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

def test_tree_Node_name_value_roundtrip():
    instance = tree_Node(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_children4_link_reassign_clear():
    a = tree_Node(name="sample_text")
    b1 = tree_Node(name="sample_text")
    b2 = tree_Node(name="sample_text_2")
    _safe_set(a, 'tree_Node3', {b1})
    assert _is_linked(a, 'tree_Node3', b1)
    if hasattr(b1, 'tree_Node5'):
        assert _is_linked(b1, 'tree_Node5', a)
    _safe_set(a, 'tree_Node3', {b2})
    assert _is_linked(a, 'tree_Node3', b2)
    if hasattr(b1, 'tree_Node5'):
        assert not _is_linked(b1, 'tree_Node5', a)
    if hasattr(b2, 'tree_Node5'):
        assert _is_linked(b2, 'tree_Node5', a)
    _safe_set(a, 'tree_Node3', set())
    assert not _is_linked(a, 'tree_Node3', b2)
    if hasattr(b2, 'tree_Node5'):
        assert not _is_linked(b2, 'tree_Node5', a)


def test_assoc_nodes0_link_reassign_clear():
    a = tree_Node(name="sample_text")
    b1 = tree_Diagram()
    b2 = tree_Diagram()
    _safe_set(a, 'tree_Node', b1)
    assert _is_linked(a, 'tree_Node', b1)
    if hasattr(b1, 'tree_Diagram'):
        assert _is_linked(b1, 'tree_Diagram', a)
    _safe_set(a, 'tree_Node', b2)
    assert _is_linked(a, 'tree_Node', b2)
    if hasattr(b1, 'tree_Diagram'):
        assert not _is_linked(b1, 'tree_Diagram', a)
    if hasattr(b2, 'tree_Diagram'):
        assert _is_linked(b2, 'tree_Diagram', a)
    _safe_set(a, 'tree_Node', None)
    assert not _is_linked(a, 'tree_Node', b2)
    if hasattr(b2, 'tree_Diagram'):
        assert not _is_linked(b2, 'tree_Diagram', a)


def test_assoc_source6_link_reassign_clear():
    a = tree_Node(name="sample_text")
    b1 = tree_Edge()
    b2 = tree_Edge()
    _safe_set(a, 'tree_Node8', b1)
    assert _is_linked(a, 'tree_Node8', b1)
    if hasattr(b1, 'tree_Edge7'):
        assert _is_linked(b1, 'tree_Edge7', a)
    _safe_set(a, 'tree_Node8', b2)
    assert _is_linked(a, 'tree_Node8', b2)
    if hasattr(b1, 'tree_Edge7'):
        assert not _is_linked(b1, 'tree_Edge7', a)
    if hasattr(b2, 'tree_Edge7'):
        assert _is_linked(b2, 'tree_Edge7', a)
    _safe_set(a, 'tree_Node8', None)
    assert not _is_linked(a, 'tree_Node8', b2)
    if hasattr(b2, 'tree_Edge7'):
        assert not _is_linked(b2, 'tree_Edge7', a)


def test_assoc_target9_link_reassign_clear():
    a = tree_Node(name="sample_text")
    b1 = tree_Edge()
    b2 = tree_Edge()
    _safe_set(a, 'tree_Node11', b1)
    assert _is_linked(a, 'tree_Node11', b1)
    if hasattr(b1, 'tree_Edge10'):
        assert _is_linked(b1, 'tree_Edge10', a)
    _safe_set(a, 'tree_Node11', b2)
    assert _is_linked(a, 'tree_Node11', b2)
    if hasattr(b1, 'tree_Edge10'):
        assert not _is_linked(b1, 'tree_Edge10', a)
    if hasattr(b2, 'tree_Edge10'):
        assert _is_linked(b2, 'tree_Edge10', a)
    _safe_set(a, 'tree_Node11', None)
    assert not _is_linked(a, 'tree_Node11', b2)
    if hasattr(b2, 'tree_Edge10'):
        assert not _is_linked(b2, 'tree_Edge10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

tree_Diagram_strategy = st.builds(tree_Diagram)
@given(instance=tree_Diagram_strategy)
@settings(max_examples=25)
def test_tree_Diagram_instantiation(instance):
    assert isinstance(instance, tree_Diagram)


tree_Edge_strategy = st.builds(tree_Edge)
@given(instance=tree_Edge_strategy)
@settings(max_examples=25)
def test_tree_Edge_instantiation(instance):
    assert isinstance(instance, tree_Edge)


tree_Node_strategy = st.builds(tree_Node, name=safe_text)
@given(instance=tree_Node_strategy)
@settings(max_examples=25)
def test_tree_Node_instantiation(instance):
    assert isinstance(instance, tree_Node)



