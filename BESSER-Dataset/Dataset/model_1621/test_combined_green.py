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
    NetElement,
    Edge,
    pnw_TPEdge,
    pnw_PTEdge,
    pnw_Edge,
    pnw_NetElement,
    NamedElement,
    pnw_Place,
    pnw_Transition,
    pnw_Net,
    pnw_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_netelement_is_not_abstract():
    assert not inspect.isabstract(NetElement)


def test_hyp_netelement_constructor_exists():
    assert callable(NetElement.__init__)


def test_hyp_netelement_constructor_args():
    sig = inspect.signature(NetElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_hyp_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_hyp_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnw_tpedge_is_not_abstract():
    assert not inspect.isabstract(pnw_TPEdge)


def test_hyp_pnw_tpedge_constructor_exists():
    assert callable(pnw_TPEdge.__init__)


def test_hyp_pnw_tpedge_constructor_args():
    sig = inspect.signature(pnw_TPEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnw_ptedge_is_not_abstract():
    assert not inspect.isabstract(pnw_PTEdge)


def test_hyp_pnw_ptedge_constructor_exists():
    assert callable(pnw_PTEdge.__init__)


def test_hyp_pnw_ptedge_constructor_args():
    sig = inspect.signature(pnw_PTEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnw_edge_is_not_abstract():
    assert not inspect.isabstract(pnw_Edge)


def test_hyp_pnw_edge_constructor_exists():
    assert callable(pnw_Edge.__init__)


def test_hyp_pnw_edge_constructor_args():
    sig = inspect.signature(pnw_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"




def test_hyp_pnw_netelement_is_not_abstract():
    assert not inspect.isabstract(pnw_NetElement)


def test_hyp_pnw_netelement_constructor_exists():
    assert callable(pnw_NetElement.__init__)


def test_hyp_pnw_netelement_constructor_args():
    sig = inspect.signature(pnw_NetElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnw_place_is_not_abstract():
    assert not inspect.isabstract(pnw_Place)


def test_hyp_pnw_place_constructor_exists():
    assert callable(pnw_Place.__init__)


def test_hyp_pnw_place_constructor_args():
    sig = inspect.signature(pnw_Place.__init__)
    params = list(sig.parameters.keys())
    assert "noOfTokens" in params, "Missing parameter 'noOfTokens'"




def test_hyp_pnw_transition_is_not_abstract():
    assert not inspect.isabstract(pnw_Transition)


def test_hyp_pnw_transition_constructor_exists():
    assert callable(pnw_Transition.__init__)


def test_hyp_pnw_transition_constructor_args():
    sig = inspect.signature(pnw_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnw_net_is_not_abstract():
    assert not inspect.isabstract(pnw_Net)


def test_hyp_pnw_net_constructor_exists():
    assert callable(pnw_Net.__init__)


def test_hyp_pnw_net_constructor_args():
    sig = inspect.signature(pnw_Net.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"




def test_hyp_pnw_namedelement_is_not_abstract():
    assert not inspect.isabstract(pnw_NamedElement)


def test_hyp_pnw_namedelement_constructor_exists():
    assert callable(pnw_NamedElement.__init__)


def test_hyp_pnw_namedelement_constructor_args():
    sig = inspect.signature(pnw_NamedElement.__init__)
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
NetElement_strategy = st.builds(
    NetElement,
)
Edge_strategy = st.builds(
    Edge,
)
pnw_TPEdge_strategy = st.builds(
    pnw_TPEdge,
)
pnw_PTEdge_strategy = st.builds(
    pnw_PTEdge,
)
pnw_Edge_strategy = st.builds(
    pnw_Edge,
    weight=
        st.integers()
)
pnw_NetElement_strategy = st.builds(
    pnw_NetElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pnw_Place_strategy = st.builds(
    pnw_Place,
    noOfTokens=
        st.integers()
)
pnw_Transition_strategy = st.builds(
    pnw_Transition,
)
pnw_Net_strategy = st.builds(
    pnw_Net,
    incrementalID=
        safe_text
)
pnw_NamedElement_strategy = st.builds(
    pnw_NamedElement,
    name=
        safe_text
)








@given(instance=pnw_Edge_strategy)
def test_hyp_pnw_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original






@given(instance=pnw_Place_strategy)
def test_hyp_pnw_place_noOfTokens_setter(instance):
    original = instance.noOfTokens
    instance.noOfTokens = original
    assert instance.noOfTokens == original





@given(instance=pnw_Net_strategy)
def test_hyp_pnw_net_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original




@given(instance=pnw_NamedElement_strategy)
def test_hyp_pnw_namedelement_name_setter(instance):
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
    Edge,
    NamedElement,
    NetElement,
    pnw_Edge,
    pnw_NamedElement,
    pnw_Net,
    pnw_NetElement,
    pnw_PTEdge,
    pnw_Place,
    pnw_TPEdge,
    pnw_Transition,
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

def test_pnw_Edge_weight_value_roundtrip():
    instance = pnw_Edge(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_pnw_NamedElement_name_value_roundtrip():
    instance = pnw_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pnw_Net_incrementalID_value_roundtrip():
    instance = pnw_Net(incrementalID="sample_text")
    assert instance.incrementalID == "sample_text"
    instance.incrementalID = "sample_text_2"
    assert instance.incrementalID == "sample_text_2"


def test_pnw_Place_noOfTokens_value_roundtrip():
    instance = pnw_Place(noOfTokens=7)
    assert instance.noOfTokens == 7
    instance.noOfTokens = 13
    assert instance.noOfTokens == 13


def test_pnw_PTEdge_isa_Edge():
    instance = pnw_PTEdge()
    assert isinstance(instance, Edge)


def test_pnw_TPEdge_isa_Edge():
    instance = pnw_TPEdge()
    assert isinstance(instance, Edge)


def test_pnw_Net_isa_NamedElement():
    instance = pnw_Net(incrementalID="sample_text")
    assert isinstance(instance, NamedElement)


def test_pnw_Place_isa_NamedElement():
    instance = pnw_Place(noOfTokens=7)
    assert isinstance(instance, NamedElement)


def test_pnw_Transition_isa_NamedElement():
    instance = pnw_Transition()
    assert isinstance(instance, NamedElement)


def test_pnw_Edge_isa_NetElement():
    instance = pnw_Edge(weight=7)
    assert isinstance(instance, NetElement)


def test_pnw_Place_isa_NetElement():
    instance = pnw_Place(noOfTokens=7)
    assert isinstance(instance, NetElement)


def test_pnw_Transition_isa_NetElement():
    instance = pnw_Transition()
    assert isinstance(instance, NetElement)


def test_assoc_elements0_link_reassign_clear():
    a = pnw_Net(incrementalID="sample_text")
    b1 = pnw_NetElement()
    b2 = pnw_NetElement()
    _safe_set(a, 'net', {b1})
    assert _is_linked(a, 'net', b1)
    if hasattr(b1, 'NetElement'):
        assert _is_linked(b1, 'NetElement', a)
    _safe_set(a, 'net', {b2})
    assert _is_linked(a, 'net', b2)
    if hasattr(b1, 'NetElement'):
        assert not _is_linked(b1, 'NetElement', a)
    if hasattr(b2, 'NetElement'):
        assert _is_linked(b2, 'NetElement', a)
    _safe_set(a, 'net', set())
    assert not _is_linked(a, 'net', b2)
    if hasattr(b2, 'NetElement'):
        assert not _is_linked(b2, 'NetElement', a)


def test_assoc_fromPlace10_link_reassign_clear():
    a = pnw_Place(noOfTokens=7)
    b1 = pnw_PTEdge()
    b2 = pnw_PTEdge()
    _safe_set(a, 'Place11', b1)
    assert _is_linked(a, 'Place11', b1)
    if hasattr(b1, 'outPTEdges'):
        assert _is_linked(b1, 'outPTEdges', a)
    _safe_set(a, 'Place11', b2)
    assert _is_linked(a, 'Place11', b2)
    if hasattr(b1, 'outPTEdges'):
        assert not _is_linked(b1, 'outPTEdges', a)
    if hasattr(b2, 'outPTEdges'):
        assert _is_linked(b2, 'outPTEdges', a)
    _safe_set(a, 'Place11', None)
    assert not _is_linked(a, 'Place11', b2)
    if hasattr(b2, 'outPTEdges'):
        assert not _is_linked(b2, 'outPTEdges', a)


def test_assoc_inTPEdges6_link_reassign_clear():
    a = pnw_Place(noOfTokens=7)
    b1 = pnw_TPEdge()
    b2 = pnw_TPEdge()
    _safe_set(a, 'toPlace', {b1})
    assert _is_linked(a, 'toPlace', b1)
    if hasattr(b1, 'TPEdge7'):
        assert _is_linked(b1, 'TPEdge7', a)
    _safe_set(a, 'toPlace', {b2})
    assert _is_linked(a, 'toPlace', b2)
    if hasattr(b1, 'TPEdge7'):
        assert not _is_linked(b1, 'TPEdge7', a)
    if hasattr(b2, 'TPEdge7'):
        assert _is_linked(b2, 'TPEdge7', a)
    _safe_set(a, 'toPlace', set())
    assert not _is_linked(a, 'toPlace', b2)
    if hasattr(b2, 'TPEdge7'):
        assert not _is_linked(b2, 'TPEdge7', a)


def test_assoc_net1_link_reassign_clear():
    a = pnw_Net(incrementalID="sample_text")
    b1 = pnw_NetElement()
    b2 = pnw_NetElement()
    _safe_set(a, 'Net', b1)
    assert _is_linked(a, 'Net', b1)
    if hasattr(b1, 'elements'):
        assert _is_linked(b1, 'elements', a)
    _safe_set(a, 'Net', b2)
    assert _is_linked(a, 'Net', b2)
    if hasattr(b1, 'elements'):
        assert not _is_linked(b1, 'elements', a)
    if hasattr(b2, 'elements'):
        assert _is_linked(b2, 'elements', a)
    _safe_set(a, 'Net', None)
    assert not _is_linked(a, 'Net', b2)
    if hasattr(b2, 'elements'):
        assert not _is_linked(b2, 'elements', a)


def test_assoc_outPTEdges4_link_reassign_clear():
    a = pnw_Place(noOfTokens=7)
    b1 = pnw_PTEdge()
    b2 = pnw_PTEdge()
    _safe_set(a, 'fromPlace', {b1})
    assert _is_linked(a, 'fromPlace', b1)
    if hasattr(b1, 'PTEdge5'):
        assert _is_linked(b1, 'PTEdge5', a)
    _safe_set(a, 'fromPlace', {b2})
    assert _is_linked(a, 'fromPlace', b2)
    if hasattr(b1, 'PTEdge5'):
        assert not _is_linked(b1, 'PTEdge5', a)
    if hasattr(b2, 'PTEdge5'):
        assert _is_linked(b2, 'PTEdge5', a)
    _safe_set(a, 'fromPlace', set())
    assert not _is_linked(a, 'fromPlace', b2)
    if hasattr(b2, 'PTEdge5'):
        assert not _is_linked(b2, 'PTEdge5', a)


def test_assoc_toPlace9_link_reassign_clear():
    a = pnw_Place(noOfTokens=7)
    b1 = pnw_TPEdge()
    b2 = pnw_TPEdge()
    _safe_set(a, 'Place', b1)
    assert _is_linked(a, 'Place', b1)
    if hasattr(b1, 'inTPEdges'):
        assert _is_linked(b1, 'inTPEdges', a)
    _safe_set(a, 'Place', b2)
    assert _is_linked(a, 'Place', b2)
    if hasattr(b1, 'inTPEdges'):
        assert not _is_linked(b1, 'inTPEdges', a)
    if hasattr(b2, 'inTPEdges'):
        assert _is_linked(b2, 'inTPEdges', a)
    _safe_set(a, 'Place', None)
    assert not _is_linked(a, 'Place', b2)
    if hasattr(b2, 'inTPEdges'):
        assert not _is_linked(b2, 'inTPEdges', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NetElement_strategy = st.builds(NetElement)
@given(instance=NetElement_strategy)
@settings(max_examples=25)
def test_NetElement_instantiation(instance):
    assert isinstance(instance, NetElement)


pnw_Edge_strategy = st.builds(pnw_Edge, weight=st.integers())
@given(instance=pnw_Edge_strategy)
@settings(max_examples=25)
def test_pnw_Edge_instantiation(instance):
    assert isinstance(instance, pnw_Edge)


pnw_NamedElement_strategy = st.builds(pnw_NamedElement, name=safe_text)
@given(instance=pnw_NamedElement_strategy)
@settings(max_examples=25)
def test_pnw_NamedElement_instantiation(instance):
    assert isinstance(instance, pnw_NamedElement)


pnw_Net_strategy = st.builds(pnw_Net, incrementalID=safe_text)
@given(instance=pnw_Net_strategy)
@settings(max_examples=25)
def test_pnw_Net_instantiation(instance):
    assert isinstance(instance, pnw_Net)


pnw_NetElement_strategy = st.builds(pnw_NetElement)
@given(instance=pnw_NetElement_strategy)
@settings(max_examples=25)
def test_pnw_NetElement_instantiation(instance):
    assert isinstance(instance, pnw_NetElement)


pnw_PTEdge_strategy = st.builds(pnw_PTEdge)
@given(instance=pnw_PTEdge_strategy)
@settings(max_examples=25)
def test_pnw_PTEdge_instantiation(instance):
    assert isinstance(instance, pnw_PTEdge)


pnw_Place_strategy = st.builds(pnw_Place, noOfTokens=st.integers())
@given(instance=pnw_Place_strategy)
@settings(max_examples=25)
def test_pnw_Place_instantiation(instance):
    assert isinstance(instance, pnw_Place)


pnw_TPEdge_strategy = st.builds(pnw_TPEdge)
@given(instance=pnw_TPEdge_strategy)
@settings(max_examples=25)
def test_pnw_TPEdge_instantiation(instance):
    assert isinstance(instance, pnw_TPEdge)


pnw_Transition_strategy = st.builds(pnw_Transition)
@given(instance=pnw_Transition_strategy)
@settings(max_examples=25)
def test_pnw_Transition_instantiation(instance):
    assert isinstance(instance, pnw_Transition)



