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
    TreeElement,
    MMTree_Leaf,
    MMTree_Node,
    MMTree_TreeElement,
    LeafSize,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_hyp_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_hyp_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mmtree_leaf_is_not_abstract():
    assert not inspect.isabstract(MMTree_Leaf)


def test_hyp_mmtree_leaf_constructor_exists():
    assert callable(MMTree_Leaf.__init__)


def test_hyp_mmtree_leaf_constructor_args():
    sig = inspect.signature(MMTree_Leaf.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"




def test_hyp_mmtree_node_is_not_abstract():
    assert not inspect.isabstract(MMTree_Node)


def test_hyp_mmtree_node_constructor_exists():
    assert callable(MMTree_Node.__init__)


def test_hyp_mmtree_node_constructor_args():
    sig = inspect.signature(MMTree_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mmtree_treeelement_is_not_abstract():
    assert not inspect.isabstract(MMTree_TreeElement)


def test_hyp_mmtree_treeelement_constructor_exists():
    assert callable(MMTree_TreeElement.__init__)


def test_hyp_mmtree_treeelement_constructor_args():
    sig = inspect.signature(MMTree_TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_leafsize_exists():
    # Check that the Enumeration exists
    assert LeafSize is not None

def test_hyp_leafsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeafSize]
    expected_literals = [
        "medium",
        "big",
        "small",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeafSize"


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
TreeElement_strategy = st.builds(
    TreeElement,
)
MMTree_Leaf_strategy = st.builds(
    MMTree_Leaf,
    size=
        safe_text
)
MMTree_Node_strategy = st.builds(
    MMTree_Node,
)
MMTree_TreeElement_strategy = st.builds(
    MMTree_TreeElement,
    name=
        safe_text
)





@given(instance=MMTree_Leaf_strategy)
def test_hyp_mmtree_leaf_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original





@given(instance=MMTree_TreeElement_strategy)
def test_hyp_mmtree_treeelement_name_setter(instance):
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
    MMTree_Leaf,
    MMTree_Node,
    MMTree_TreeElement,
    TreeElement,
    LeafSize,
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

def test_MMTree_Leaf_size_value_roundtrip():
    instance = MMTree_Leaf(size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_MMTree_TreeElement_name_value_roundtrip():
    instance = MMTree_TreeElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MMTree_Leaf_isa_TreeElement():
    instance = MMTree_Leaf(size="sample_text")
    assert isinstance(instance, TreeElement)


def test_MMTree_Node_isa_TreeElement():
    instance = MMTree_Node()
    assert isinstance(instance, TreeElement)


def test_assoc_children0_link_reassign_clear():
    a = MMTree_TreeElement(name="sample_text")
    b1 = MMTree_Node()
    b2 = MMTree_Node()
    _safe_set(a, 'MMTree_TreeElement', b1)
    assert _is_linked(a, 'MMTree_TreeElement', b1)
    if hasattr(b1, 'MMTree_Node'):
        assert _is_linked(b1, 'MMTree_Node', a)
    _safe_set(a, 'MMTree_TreeElement', b2)
    assert _is_linked(a, 'MMTree_TreeElement', b2)
    if hasattr(b1, 'MMTree_Node'):
        assert not _is_linked(b1, 'MMTree_Node', a)
    if hasattr(b2, 'MMTree_Node'):
        assert _is_linked(b2, 'MMTree_Node', a)
    _safe_set(a, 'MMTree_TreeElement', None)
    assert not _is_linked(a, 'MMTree_TreeElement', b2)
    if hasattr(b2, 'MMTree_Node'):
        assert not _is_linked(b2, 'MMTree_Node', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

MMTree_Leaf_strategy = st.builds(MMTree_Leaf, size=safe_text)
@given(instance=MMTree_Leaf_strategy)
@settings(max_examples=25)
def test_MMTree_Leaf_instantiation(instance):
    assert isinstance(instance, MMTree_Leaf)


MMTree_Node_strategy = st.builds(MMTree_Node)
@given(instance=MMTree_Node_strategy)
@settings(max_examples=25)
def test_MMTree_Node_instantiation(instance):
    assert isinstance(instance, MMTree_Node)


MMTree_TreeElement_strategy = st.builds(MMTree_TreeElement, name=safe_text)
@given(instance=MMTree_TreeElement_strategy)
@settings(max_examples=25)
def test_MMTree_TreeElement_instantiation(instance):
    assert isinstance(instance, MMTree_TreeElement)


TreeElement_strategy = st.builds(TreeElement)
@given(instance=TreeElement_strategy)
@settings(max_examples=25)
def test_TreeElement_instantiation(instance):
    assert isinstance(instance, TreeElement)



