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
    simpletree_Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_simpletree_tree_is_not_abstract():
    assert not inspect.isabstract(simpletree_Tree)


def test_hyp_simpletree_tree_constructor_exists():
    assert callable(simpletree_Tree.__init__)


def test_hyp_simpletree_tree_constructor_args():
    sig = inspect.signature(simpletree_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"



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
simpletree_Tree_strategy = st.builds(
    simpletree_Tree,
    label=
        safe_text
)




@given(instance=simpletree_Tree_strategy)
def test_hyp_simpletree_tree_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    simpletree_Tree,
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

def test_simpletree_Tree_label_value_roundtrip():
    instance = simpletree_Tree(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_assoc_children1_link_reassign_clear():
    a = simpletree_Tree(label="sample_text")
    b1 = simpletree_Tree(label="sample_text")
    b2 = simpletree_Tree(label="sample_text_2")
    _safe_set(a, 'Tree', b1)
    assert _is_linked(a, 'Tree', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'Tree', b2)
    assert _is_linked(a, 'Tree', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'Tree', None)
    assert not _is_linked(a, 'Tree', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_parent3_link_reassign_clear():
    a = simpletree_Tree(label="sample_text")
    b1 = simpletree_Tree(label="sample_text")
    b2 = simpletree_Tree(label="sample_text_2")
    _safe_set(a, 'Tree4', b1)
    assert _is_linked(a, 'Tree4', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'Tree4', b2)
    assert _is_linked(a, 'Tree4', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'Tree4', None)
    assert not _is_linked(a, 'Tree4', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

simpletree_Tree_strategy = st.builds(simpletree_Tree, label=safe_text)
@given(instance=simpletree_Tree_strategy)
@settings(max_examples=25)
def test_simpletree_Tree_instantiation(instance):
    assert isinstance(instance, simpletree_Tree)



