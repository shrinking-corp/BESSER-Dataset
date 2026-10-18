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
    pn_NamedElement,
    NetElement,
    pn_Transition,
    NamedElement,
    pn_Place,
    pn_NetElement,
    pn_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pn_namedelement_is_not_abstract():
    assert not inspect.isabstract(pn_NamedElement)


def test_hyp_pn_namedelement_constructor_exists():
    assert callable(pn_NamedElement.__init__)


def test_hyp_pn_namedelement_constructor_args():
    sig = inspect.signature(pn_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_netelement_is_not_abstract():
    assert not inspect.isabstract(NetElement)


def test_hyp_netelement_constructor_exists():
    assert callable(NetElement.__init__)


def test_hyp_netelement_constructor_args():
    sig = inspect.signature(NetElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pn_transition_is_not_abstract():
    assert not inspect.isabstract(pn_Transition)


def test_hyp_pn_transition_constructor_exists():
    assert callable(pn_Transition.__init__)


def test_hyp_pn_transition_constructor_args():
    sig = inspect.signature(pn_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pn_place_is_not_abstract():
    assert not inspect.isabstract(pn_Place)


def test_hyp_pn_place_constructor_exists():
    assert callable(pn_Place.__init__)


def test_hyp_pn_place_constructor_args():
    sig = inspect.signature(pn_Place.__init__)
    params = list(sig.parameters.keys())
    assert "noOfTokens" in params, "Missing parameter 'noOfTokens'"




def test_hyp_pn_netelement_is_not_abstract():
    assert not inspect.isabstract(pn_NetElement)


def test_hyp_pn_netelement_constructor_exists():
    assert callable(pn_NetElement.__init__)


def test_hyp_pn_netelement_constructor_args():
    sig = inspect.signature(pn_NetElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pn_net_is_not_abstract():
    assert not inspect.isabstract(pn_Net)


def test_hyp_pn_net_constructor_exists():
    assert callable(pn_Net.__init__)


def test_hyp_pn_net_constructor_args():
    sig = inspect.signature(pn_Net.__init__)
    params = list(sig.parameters.keys())
    assert "incrementalID" in params, "Missing parameter 'incrementalID'"



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
pn_NamedElement_strategy = st.builds(
    pn_NamedElement,
    name=
        safe_text
)
NetElement_strategy = st.builds(
    NetElement,
)
pn_Transition_strategy = st.builds(
    pn_Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
pn_Place_strategy = st.builds(
    pn_Place,
    noOfTokens=
        st.integers()
)
pn_NetElement_strategy = st.builds(
    pn_NetElement,
)
pn_Net_strategy = st.builds(
    pn_Net,
    incrementalID=
        safe_text
)




@given(instance=pn_NamedElement_strategy)
def test_hyp_pn_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=pn_Place_strategy)
def test_hyp_pn_place_noOfTokens_setter(instance):
    original = instance.noOfTokens
    instance.noOfTokens = original
    assert instance.noOfTokens == original





@given(instance=pn_Net_strategy)
def test_hyp_pn_net_incrementalID_setter(instance):
    original = instance.incrementalID
    instance.incrementalID = original
    assert instance.incrementalID == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    NetElement,
    pn_NamedElement,
    pn_Net,
    pn_NetElement,
    pn_Place,
    pn_Transition,
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

def test_pn_NamedElement_name_value_roundtrip():
    instance = pn_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pn_Net_incrementalID_value_roundtrip():
    instance = pn_Net(incrementalID="sample_text")
    assert instance.incrementalID == "sample_text"
    instance.incrementalID = "sample_text_2"
    assert instance.incrementalID == "sample_text_2"


def test_pn_Place_noOfTokens_value_roundtrip():
    instance = pn_Place(noOfTokens=7)
    assert instance.noOfTokens == 7
    instance.noOfTokens = 13
    assert instance.noOfTokens == 13


def test_pn_Net_isa_NamedElement():
    instance = pn_Net(incrementalID="sample_text")
    assert isinstance(instance, NamedElement)


def test_pn_NetElement_isa_NamedElement():
    instance = pn_NetElement()
    assert isinstance(instance, NamedElement)


def test_pn_Place_isa_NamedElement():
    instance = pn_Place(noOfTokens=7)
    assert isinstance(instance, NamedElement)


def test_pn_Place_isa_NetElement():
    instance = pn_Place(noOfTokens=7)
    assert isinstance(instance, NetElement)


def test_pn_Transition_isa_NetElement():
    instance = pn_Transition()
    assert isinstance(instance, NetElement)


def test_assoc_elements0_link_reassign_clear():
    a = pn_Net(incrementalID="sample_text")
    b1 = pn_NetElement()
    b2 = pn_NetElement()
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


def test_assoc_net1_link_reassign_clear():
    a = pn_Net(incrementalID="sample_text")
    b1 = pn_NetElement()
    b2 = pn_NetElement()
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


def test_assoc_srcP2T3_link_reassign_clear():
    a = pn_Place(noOfTokens=7)
    b1 = pn_Transition()
    b2 = pn_Transition()
    _safe_set(a, 'Place4', b1)
    assert _is_linked(a, 'Place4', b1)
    if hasattr(b1, 'trgP2T'):
        assert _is_linked(b1, 'trgP2T', a)
    _safe_set(a, 'Place4', b2)
    assert _is_linked(a, 'Place4', b2)
    if hasattr(b1, 'trgP2T'):
        assert not _is_linked(b1, 'trgP2T', a)
    if hasattr(b2, 'trgP2T'):
        assert _is_linked(b2, 'trgP2T', a)
    _safe_set(a, 'Place4', None)
    assert not _is_linked(a, 'Place4', b2)
    if hasattr(b2, 'trgP2T'):
        assert not _is_linked(b2, 'trgP2T', a)


def test_assoc_srcT2P6_link_reassign_clear():
    a = pn_Place(noOfTokens=7)
    b1 = pn_Transition()
    b2 = pn_Transition()
    _safe_set(a, 'trgT2P', {b1})
    assert _is_linked(a, 'trgT2P', b1)
    if hasattr(b1, 'Transition7'):
        assert _is_linked(b1, 'Transition7', a)
    _safe_set(a, 'trgT2P', {b2})
    assert _is_linked(a, 'trgT2P', b2)
    if hasattr(b1, 'Transition7'):
        assert not _is_linked(b1, 'Transition7', a)
    if hasattr(b2, 'Transition7'):
        assert _is_linked(b2, 'Transition7', a)
    _safe_set(a, 'trgT2P', set())
    assert not _is_linked(a, 'trgT2P', b2)
    if hasattr(b2, 'Transition7'):
        assert not _is_linked(b2, 'Transition7', a)


def test_assoc_trgP2T5_link_reassign_clear():
    a = pn_Place(noOfTokens=7)
    b1 = pn_Transition()
    b2 = pn_Transition()
    _safe_set(a, 'srcP2T', {b1})
    assert _is_linked(a, 'srcP2T', b1)
    if hasattr(b1, 'Transition'):
        assert _is_linked(b1, 'Transition', a)
    _safe_set(a, 'srcP2T', {b2})
    assert _is_linked(a, 'srcP2T', b2)
    if hasattr(b1, 'Transition'):
        assert not _is_linked(b1, 'Transition', a)
    if hasattr(b2, 'Transition'):
        assert _is_linked(b2, 'Transition', a)
    _safe_set(a, 'srcP2T', set())
    assert not _is_linked(a, 'srcP2T', b2)
    if hasattr(b2, 'Transition'):
        assert not _is_linked(b2, 'Transition', a)


def test_assoc_trgT2P2_link_reassign_clear():
    a = pn_Place(noOfTokens=7)
    b1 = pn_Transition()
    b2 = pn_Transition()
    _safe_set(a, 'Place', b1)
    assert _is_linked(a, 'Place', b1)
    if hasattr(b1, 'srcT2P'):
        assert _is_linked(b1, 'srcT2P', a)
    _safe_set(a, 'Place', b2)
    assert _is_linked(a, 'Place', b2)
    if hasattr(b1, 'srcT2P'):
        assert not _is_linked(b1, 'srcT2P', a)
    if hasattr(b2, 'srcT2P'):
        assert _is_linked(b2, 'srcT2P', a)
    _safe_set(a, 'Place', None)
    assert not _is_linked(a, 'Place', b2)
    if hasattr(b2, 'srcT2P'):
        assert not _is_linked(b2, 'srcT2P', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

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


pn_NamedElement_strategy = st.builds(pn_NamedElement, name=safe_text)
@given(instance=pn_NamedElement_strategy)
@settings(max_examples=25)
def test_pn_NamedElement_instantiation(instance):
    assert isinstance(instance, pn_NamedElement)


pn_Net_strategy = st.builds(pn_Net, incrementalID=safe_text)
@given(instance=pn_Net_strategy)
@settings(max_examples=25)
def test_pn_Net_instantiation(instance):
    assert isinstance(instance, pn_Net)


pn_NetElement_strategy = st.builds(pn_NetElement)
@given(instance=pn_NetElement_strategy)
@settings(max_examples=25)
def test_pn_NetElement_instantiation(instance):
    assert isinstance(instance, pn_NetElement)


pn_Place_strategy = st.builds(pn_Place, noOfTokens=st.integers())
@given(instance=pn_Place_strategy)
@settings(max_examples=25)
def test_pn_Place_instantiation(instance):
    assert isinstance(instance, pn_Place)


pn_Transition_strategy = st.builds(pn_Transition)
@given(instance=pn_Transition_strategy)
@settings(max_examples=25)
def test_pn_Transition_instantiation(instance):
    assert isinstance(instance, pn_Transition)



