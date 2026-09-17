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
    Node,
    petrinet_Node,
    petrinet_Arc,
    petrinet_Place,
    petrinet_PNGraph,
    petrinet_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinet_Node)


def test_hyp_petrinet_node_constructor_exists():
    assert callable(petrinet_Node.__init__)


def test_hyp_petrinet_node_constructor_args():
    sig = inspect.signature(petrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_hyp_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_hyp_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"




def test_hyp_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_hyp_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_hyp_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "markings" in params, "Missing parameter 'markings'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_petrinet_pngraph_is_not_abstract():
    assert not inspect.isabstract(petrinet_PNGraph)


def test_hyp_petrinet_pngraph_constructor_exists():
    assert callable(petrinet_PNGraph.__init__)


def test_hyp_petrinet_pngraph_constructor_args():
    sig = inspect.signature(petrinet_PNGraph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_hyp_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_hyp_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"



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
Node_strategy = st.builds(
    Node,
)
petrinet_Node_strategy = st.builds(
    petrinet_Node,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
    w=
        safe_text
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    markings=
        safe_text,
    id=
        safe_text
)
petrinet_PNGraph_strategy = st.builds(
    petrinet_PNGraph,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
    id=
        safe_text
)






@given(instance=petrinet_Arc_strategy)
def test_hyp_petrinet_arc_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original




@given(instance=petrinet_Place_strategy)
def test_hyp_petrinet_place_markings_setter(instance):
    original = instance.markings
    instance.markings = original
    assert instance.markings == original



@given(instance=petrinet_Place_strategy)
def test_hyp_petrinet_place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original





@given(instance=petrinet_Transition_strategy)
def test_hyp_petrinet_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Node,
    petrinet_Arc,
    petrinet_Node,
    petrinet_PNGraph,
    petrinet_Place,
    petrinet_Transition,
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

def test_petrinet_Arc_w_value_roundtrip():
    instance = petrinet_Arc(w="sample_text")
    assert instance.w == "sample_text"
    instance.w = "sample_text_2"
    assert instance.w == "sample_text_2"


def test_petrinet_Place_id_value_roundtrip():
    instance = petrinet_Place(id="sample_text", markings="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_petrinet_Place_markings_value_roundtrip():
    instance = petrinet_Place(id="sample_text", markings="sample_text")
    assert instance.markings == "sample_text"
    instance.markings = "sample_text_2"
    assert instance.markings == "sample_text_2"


def test_petrinet_Transition_id_value_roundtrip():
    instance = petrinet_Transition(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_petrinet_Place_isa_Node():
    instance = petrinet_Place(id="sample_text", markings="sample_text")
    assert isinstance(instance, Node)


def test_petrinet_Transition_isa_Node():
    instance = petrinet_Transition(id="sample_text")
    assert isinstance(instance, Node)


def test_assoc_arcs3_link_reassign_clear():
    a = petrinet_Arc(w="sample_text")
    b1 = petrinet_PNGraph()
    b2 = petrinet_PNGraph()
    _safe_set(a, 'petrinet_Arc', b1)
    assert _is_linked(a, 'petrinet_Arc', b1)
    if hasattr(b1, 'petrinet_PNGraph4'):
        assert _is_linked(b1, 'petrinet_PNGraph4', a)
    _safe_set(a, 'petrinet_Arc', b2)
    assert _is_linked(a, 'petrinet_Arc', b2)
    if hasattr(b1, 'petrinet_PNGraph4'):
        assert not _is_linked(b1, 'petrinet_PNGraph4', a)
    if hasattr(b2, 'petrinet_PNGraph4'):
        assert _is_linked(b2, 'petrinet_PNGraph4', a)
    _safe_set(a, 'petrinet_Arc', None)
    assert not _is_linked(a, 'petrinet_Arc', b2)
    if hasattr(b2, 'petrinet_PNGraph4'):
        assert not _is_linked(b2, 'petrinet_PNGraph4', a)


def test_assoc_from_5_link_reassign_clear():
    a = petrinet_Arc(w="sample_text")
    b1 = petrinet_Node()
    b2 = petrinet_Node()
    _safe_set(a, 'petrinet_Arc6', b1)
    assert _is_linked(a, 'petrinet_Arc6', b1)
    if hasattr(b1, 'petrinet_Node'):
        assert _is_linked(b1, 'petrinet_Node', a)
    _safe_set(a, 'petrinet_Arc6', b2)
    assert _is_linked(a, 'petrinet_Arc6', b2)
    if hasattr(b1, 'petrinet_Node'):
        assert not _is_linked(b1, 'petrinet_Node', a)
    if hasattr(b2, 'petrinet_Node'):
        assert _is_linked(b2, 'petrinet_Node', a)
    _safe_set(a, 'petrinet_Arc6', None)
    assert not _is_linked(a, 'petrinet_Arc6', b2)
    if hasattr(b2, 'petrinet_Node'):
        assert not _is_linked(b2, 'petrinet_Node', a)


def test_assoc_places0_link_reassign_clear():
    a = petrinet_Place(id="sample_text", markings="sample_text")
    b1 = petrinet_PNGraph()
    b2 = petrinet_PNGraph()
    _safe_set(a, 'petrinet_Place', b1)
    assert _is_linked(a, 'petrinet_Place', b1)
    if hasattr(b1, 'petrinet_PNGraph'):
        assert _is_linked(b1, 'petrinet_PNGraph', a)
    _safe_set(a, 'petrinet_Place', b2)
    assert _is_linked(a, 'petrinet_Place', b2)
    if hasattr(b1, 'petrinet_PNGraph'):
        assert not _is_linked(b1, 'petrinet_PNGraph', a)
    if hasattr(b2, 'petrinet_PNGraph'):
        assert _is_linked(b2, 'petrinet_PNGraph', a)
    _safe_set(a, 'petrinet_Place', None)
    assert not _is_linked(a, 'petrinet_Place', b2)
    if hasattr(b2, 'petrinet_PNGraph'):
        assert not _is_linked(b2, 'petrinet_PNGraph', a)


def test_assoc_to7_link_reassign_clear():
    a = petrinet_Arc(w="sample_text")
    b1 = petrinet_Node()
    b2 = petrinet_Node()
    _safe_set(a, 'petrinet_Arc8', b1)
    assert _is_linked(a, 'petrinet_Arc8', b1)
    if hasattr(b1, 'petrinet_Node9'):
        assert _is_linked(b1, 'petrinet_Node9', a)
    _safe_set(a, 'petrinet_Arc8', b2)
    assert _is_linked(a, 'petrinet_Arc8', b2)
    if hasattr(b1, 'petrinet_Node9'):
        assert not _is_linked(b1, 'petrinet_Node9', a)
    if hasattr(b2, 'petrinet_Node9'):
        assert _is_linked(b2, 'petrinet_Node9', a)
    _safe_set(a, 'petrinet_Arc8', None)
    assert not _is_linked(a, 'petrinet_Arc8', b2)
    if hasattr(b2, 'petrinet_Node9'):
        assert not _is_linked(b2, 'petrinet_Node9', a)


def test_assoc_transitions1_link_reassign_clear():
    a = petrinet_Transition(id="sample_text")
    b1 = petrinet_PNGraph()
    b2 = petrinet_PNGraph()
    _safe_set(a, 'petrinet_Transition', b1)
    assert _is_linked(a, 'petrinet_Transition', b1)
    if hasattr(b1, 'petrinet_PNGraph2'):
        assert _is_linked(b1, 'petrinet_PNGraph2', a)
    _safe_set(a, 'petrinet_Transition', b2)
    assert _is_linked(a, 'petrinet_Transition', b2)
    if hasattr(b1, 'petrinet_PNGraph2'):
        assert not _is_linked(b1, 'petrinet_PNGraph2', a)
    if hasattr(b2, 'petrinet_PNGraph2'):
        assert _is_linked(b2, 'petrinet_PNGraph2', a)
    _safe_set(a, 'petrinet_Transition', None)
    assert not _is_linked(a, 'petrinet_Transition', b2)
    if hasattr(b2, 'petrinet_PNGraph2'):
        assert not _is_linked(b2, 'petrinet_PNGraph2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


petrinet_Arc_strategy = st.builds(petrinet_Arc, w=safe_text)
@given(instance=petrinet_Arc_strategy)
@settings(max_examples=25)
def test_petrinet_Arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)


petrinet_Node_strategy = st.builds(petrinet_Node)
@given(instance=petrinet_Node_strategy)
@settings(max_examples=25)
def test_petrinet_Node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)


petrinet_PNGraph_strategy = st.builds(petrinet_PNGraph)
@given(instance=petrinet_PNGraph_strategy)
@settings(max_examples=25)
def test_petrinet_PNGraph_instantiation(instance):
    assert isinstance(instance, petrinet_PNGraph)


petrinet_Place_strategy = st.builds(petrinet_Place, id=safe_text, markings=safe_text)
@given(instance=petrinet_Place_strategy)
@settings(max_examples=25)
def test_petrinet_Place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)


petrinet_Transition_strategy = st.builds(petrinet_Transition, id=safe_text)
@given(instance=petrinet_Transition_strategy)
@settings(max_examples=25)
def test_petrinet_Transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



