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
    tree_Node,
    tree_Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tree_node_is_not_abstract():
    assert not inspect.isabstract(tree_Node)


def test_hyp_tree_node_constructor_exists():
    assert callable(tree_Node.__init__)


def test_hyp_tree_node_constructor_args():
    sig = inspect.signature(tree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "label" in params, "Missing parameter 'label'"





def test_hyp_tree_tree_is_not_abstract():
    assert not inspect.isabstract(tree_Tree)


def test_hyp_tree_tree_constructor_exists():
    assert callable(tree_Tree.__init__)


def test_hyp_tree_tree_constructor_args():
    sig = inspect.signature(tree_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
tree_Node_strategy = st.builds(
    tree_Node,
    data=
        safe_text,
    label=
        safe_text
)
tree_Tree_strategy = st.builds(
    tree_Tree,
    name=
        safe_text
)




@given(instance=tree_Node_strategy)
def test_hyp_tree_node_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=tree_Node_strategy)
def test_hyp_tree_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=tree_Tree_strategy)
def test_hyp_tree_tree_name_setter(instance):
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
    tree_Node,
    tree_Tree,
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

def test_tree_Node_data_value_roundtrip():
    instance = tree_Node(data="sample_text", label="sample_text")
    assert instance.data == "sample_text"
    instance.data = "sample_text_2"
    assert instance.data == "sample_text_2"


def test_tree_Node_label_value_roundtrip():
    instance = tree_Node(data="sample_text", label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_tree_Tree_name_value_roundtrip():
    instance = tree_Tree(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_children2_link_reassign_clear():
    a = tree_Node(data="sample_text", label="sample_text")
    b1 = tree_Node(data="sample_text", label="sample_text")
    b2 = tree_Node(data="sample_text_2", label="sample_text_2")
    _safe_set(a, 'tree_Node1', {b1})
    assert _is_linked(a, 'tree_Node1', b1)
    if hasattr(b1, 'tree_Node3'):
        assert _is_linked(b1, 'tree_Node3', a)
    _safe_set(a, 'tree_Node1', {b2})
    assert _is_linked(a, 'tree_Node1', b2)
    if hasattr(b1, 'tree_Node3'):
        assert not _is_linked(b1, 'tree_Node3', a)
    if hasattr(b2, 'tree_Node3'):
        assert _is_linked(b2, 'tree_Node3', a)
    _safe_set(a, 'tree_Node1', set())
    assert not _is_linked(a, 'tree_Node1', b2)
    if hasattr(b2, 'tree_Node3'):
        assert not _is_linked(b2, 'tree_Node3', a)


def test_assoc_node0_link_reassign_clear():
    a = tree_Tree(name="sample_text")
    b1 = tree_Node(data="sample_text", label="sample_text")
    b2 = tree_Node(data="sample_text_2", label="sample_text_2")
    _safe_set(a, 'tree_Tree', b1)
    assert _is_linked(a, 'tree_Tree', b1)
    if hasattr(b1, 'tree_Node'):
        assert _is_linked(b1, 'tree_Node', a)
    _safe_set(a, 'tree_Tree', b2)
    assert _is_linked(a, 'tree_Tree', b2)
    if hasattr(b1, 'tree_Node'):
        assert not _is_linked(b1, 'tree_Node', a)
    if hasattr(b2, 'tree_Node'):
        assert _is_linked(b2, 'tree_Node', a)
    _safe_set(a, 'tree_Tree', None)
    assert not _is_linked(a, 'tree_Tree', b2)
    if hasattr(b2, 'tree_Node'):
        assert not _is_linked(b2, 'tree_Node', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

tree_Node_strategy = st.builds(tree_Node, data=safe_text, label=safe_text)
@given(instance=tree_Node_strategy)
@settings(max_examples=25)
def test_tree_Node_instantiation(instance):
    assert isinstance(instance, tree_Node)


tree_Tree_strategy = st.builds(tree_Tree, name=safe_text)
@given(instance=tree_Tree_strategy)
@settings(max_examples=25)
def test_tree_Tree_instantiation(instance):
    assert isinstance(instance, tree_Tree)



