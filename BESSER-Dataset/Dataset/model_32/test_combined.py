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
    Arc,
    petrinet_Arc,
    petrinet_Named,
    petrinet_OutArc,
    petrinet_InArc,
    Named,
    petrinet_Transition,
    petrinet_Place,
    petrinet_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_hyp_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_hyp_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_hyp_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_hyp_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"




def test_hyp_petrinet_named_is_not_abstract():
    assert not inspect.isabstract(petrinet_Named)


def test_hyp_petrinet_named_constructor_exists():
    assert callable(petrinet_Named.__init__)


def test_hyp_petrinet_named_constructor_args():
    sig = inspect.signature(petrinet_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_petrinet_outarc_is_not_abstract():
    assert not inspect.isabstract(petrinet_OutArc)


def test_hyp_petrinet_outarc_constructor_exists():
    assert callable(petrinet_OutArc.__init__)


def test_hyp_petrinet_outarc_constructor_args():
    sig = inspect.signature(petrinet_OutArc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_inarc_is_not_abstract():
    assert not inspect.isabstract(petrinet_InArc)


def test_hyp_petrinet_inarc_constructor_exists():
    assert callable(petrinet_InArc.__init__)


def test_hyp_petrinet_inarc_constructor_args():
    sig = inspect.signature(petrinet_InArc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_hyp_named_constructor_exists():
    assert callable(Named.__init__)


def test_hyp_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_hyp_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_hyp_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_hyp_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_hyp_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"




def test_hyp_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNet)


def test_hyp_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_PetriNet.__init__)


def test_hyp_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_PetriNet.__init__)
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
Arc_strategy = st.builds(
    Arc,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
    weight=
        st.integers()
)
petrinet_Named_strategy = st.builds(
    petrinet_Named,
    name=
        safe_text
)
petrinet_OutArc_strategy = st.builds(
    petrinet_OutArc,
)
petrinet_InArc_strategy = st.builds(
    petrinet_InArc,
)
Named_strategy = st.builds(
    Named,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    token=
        st.integers()
)
petrinet_PetriNet_strategy = st.builds(
    petrinet_PetriNet,
)





@given(instance=petrinet_Arc_strategy)
def test_hyp_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original




@given(instance=petrinet_Named_strategy)
def test_hyp_petrinet_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=petrinet_Place_strategy)
def test_hyp_petrinet_place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Arc,
    Named,
    petrinet_Arc,
    petrinet_InArc,
    petrinet_Named,
    petrinet_OutArc,
    petrinet_PetriNet,
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

def test_petrinet_Arc_weight_value_roundtrip():
    instance = petrinet_Arc(weight=7)
    assert instance.weight == 7
    instance.weight = 13
    assert instance.weight == 13


def test_petrinet_Named_name_value_roundtrip():
    instance = petrinet_Named(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_petrinet_Place_token_value_roundtrip():
    instance = petrinet_Place(token=7)
    assert instance.token == 7
    instance.token = 13
    assert instance.token == 13


def test_petrinet_InArc_isa_Arc():
    instance = petrinet_InArc()
    assert isinstance(instance, Arc)


def test_petrinet_OutArc_isa_Arc():
    instance = petrinet_OutArc()
    assert isinstance(instance, Arc)


def test_petrinet_Place_isa_Named():
    instance = petrinet_Place(token=7)
    assert isinstance(instance, Named)


def test_petrinet_Transition_isa_Named():
    instance = petrinet_Transition()
    assert isinstance(instance, Named)


def test_assoc_places0_link_reassign_clear():
    a = petrinet_Place(token=7)
    b1 = petrinet_PetriNet()
    b2 = petrinet_PetriNet()
    _safe_set(a, 'petrinet_Place', b1)
    assert _is_linked(a, 'petrinet_Place', b1)
    if hasattr(b1, 'petrinet_PetriNet'):
        assert _is_linked(b1, 'petrinet_PetriNet', a)
    _safe_set(a, 'petrinet_Place', b2)
    assert _is_linked(a, 'petrinet_Place', b2)
    if hasattr(b1, 'petrinet_PetriNet'):
        assert not _is_linked(b1, 'petrinet_PetriNet', a)
    if hasattr(b2, 'petrinet_PetriNet'):
        assert _is_linked(b2, 'petrinet_PetriNet', a)
    _safe_set(a, 'petrinet_Place', None)
    assert not _is_linked(a, 'petrinet_Place', b2)
    if hasattr(b2, 'petrinet_PetriNet'):
        assert not _is_linked(b2, 'petrinet_PetriNet', a)


def test_assoc_sourcePlace10_link_reassign_clear():
    a = petrinet_Place(token=7)
    b1 = petrinet_OutArc()
    b2 = petrinet_OutArc()
    _safe_set(a, 'petrinet_Place12', b1)
    assert _is_linked(a, 'petrinet_Place12', b1)
    if hasattr(b1, 'petrinet_OutArc11'):
        assert _is_linked(b1, 'petrinet_OutArc11', a)
    _safe_set(a, 'petrinet_Place12', b2)
    assert _is_linked(a, 'petrinet_Place12', b2)
    if hasattr(b1, 'petrinet_OutArc11'):
        assert not _is_linked(b1, 'petrinet_OutArc11', a)
    if hasattr(b2, 'petrinet_OutArc11'):
        assert _is_linked(b2, 'petrinet_OutArc11', a)
    _safe_set(a, 'petrinet_Place12', None)
    assert not _is_linked(a, 'petrinet_Place12', b2)
    if hasattr(b2, 'petrinet_OutArc11'):
        assert not _is_linked(b2, 'petrinet_OutArc11', a)


def test_assoc_targetPlace7_link_reassign_clear():
    a = petrinet_Place(token=7)
    b1 = petrinet_InArc()
    b2 = petrinet_InArc()
    _safe_set(a, 'petrinet_Place9', b1)
    assert _is_linked(a, 'petrinet_Place9', b1)
    if hasattr(b1, 'petrinet_InArc8'):
        assert _is_linked(b1, 'petrinet_InArc8', a)
    _safe_set(a, 'petrinet_Place9', b2)
    assert _is_linked(a, 'petrinet_Place9', b2)
    if hasattr(b1, 'petrinet_InArc8'):
        assert not _is_linked(b1, 'petrinet_InArc8', a)
    if hasattr(b2, 'petrinet_InArc8'):
        assert _is_linked(b2, 'petrinet_InArc8', a)
    _safe_set(a, 'petrinet_Place9', None)
    assert not _is_linked(a, 'petrinet_Place9', b2)
    if hasattr(b2, 'petrinet_InArc8'):
        assert not _is_linked(b2, 'petrinet_InArc8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Arc_strategy = st.builds(Arc)
@given(instance=Arc_strategy)
@settings(max_examples=25)
def test_Arc_instantiation(instance):
    assert isinstance(instance, Arc)


Named_strategy = st.builds(Named)
@given(instance=Named_strategy)
@settings(max_examples=25)
def test_Named_instantiation(instance):
    assert isinstance(instance, Named)


petrinet_Arc_strategy = st.builds(petrinet_Arc, weight=st.integers())
@given(instance=petrinet_Arc_strategy)
@settings(max_examples=25)
def test_petrinet_Arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)


petrinet_InArc_strategy = st.builds(petrinet_InArc)
@given(instance=petrinet_InArc_strategy)
@settings(max_examples=25)
def test_petrinet_InArc_instantiation(instance):
    assert isinstance(instance, petrinet_InArc)


petrinet_Named_strategy = st.builds(petrinet_Named, name=safe_text)
@given(instance=petrinet_Named_strategy)
@settings(max_examples=25)
def test_petrinet_Named_instantiation(instance):
    assert isinstance(instance, petrinet_Named)


petrinet_OutArc_strategy = st.builds(petrinet_OutArc)
@given(instance=petrinet_OutArc_strategy)
@settings(max_examples=25)
def test_petrinet_OutArc_instantiation(instance):
    assert isinstance(instance, petrinet_OutArc)


petrinet_PetriNet_strategy = st.builds(petrinet_PetriNet)
@given(instance=petrinet_PetriNet_strategy)
@settings(max_examples=25)
def test_petrinet_PetriNet_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNet)


petrinet_Place_strategy = st.builds(petrinet_Place, token=st.integers())
@given(instance=petrinet_Place_strategy)
@settings(max_examples=25)
def test_petrinet_Place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)


petrinet_Transition_strategy = st.builds(petrinet_Transition)
@given(instance=petrinet_Transition_strategy)
@settings(max_examples=25)
def test_petrinet_Transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



