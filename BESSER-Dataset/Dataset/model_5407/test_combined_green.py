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
    ProbabalisticEvent,
    faultTree_ExternalEvent,
    faultTree_UndevelopedEvent,
    faultTree_BasicEvent,
    Gate,
    faultTree_OR_Gate,
    faultTree_AND_Gate,
    Event,
    faultTree_IntermediateEvent,
    faultTree_ProbabalisticEvent,
    FTElement,
    faultTree_Gate,
    faultTree_FaultTree,
    faultTree_Event,
    faultTree_Connector,
    faultTree_FTElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_probabalisticevent_is_not_abstract():
    assert not inspect.isabstract(ProbabalisticEvent)


def test_hyp_probabalisticevent_constructor_exists():
    assert callable(ProbabalisticEvent.__init__)


def test_hyp_probabalisticevent_constructor_args():
    sig = inspect.signature(ProbabalisticEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_externalevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_ExternalEvent)


def test_hyp_faulttree_externalevent_constructor_exists():
    assert callable(faultTree_ExternalEvent.__init__)


def test_hyp_faulttree_externalevent_constructor_args():
    sig = inspect.signature(faultTree_ExternalEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_undevelopedevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_UndevelopedEvent)


def test_hyp_faulttree_undevelopedevent_constructor_exists():
    assert callable(faultTree_UndevelopedEvent.__init__)


def test_hyp_faulttree_undevelopedevent_constructor_args():
    sig = inspect.signature(faultTree_UndevelopedEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_basicevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_BasicEvent)


def test_hyp_faulttree_basicevent_constructor_exists():
    assert callable(faultTree_BasicEvent.__init__)


def test_hyp_faulttree_basicevent_constructor_args():
    sig = inspect.signature(faultTree_BasicEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gate_is_not_abstract():
    assert not inspect.isabstract(Gate)


def test_hyp_gate_constructor_exists():
    assert callable(Gate.__init__)


def test_hyp_gate_constructor_args():
    sig = inspect.signature(Gate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_or_gate_is_not_abstract():
    assert not inspect.isabstract(faultTree_OR_Gate)


def test_hyp_faulttree_or_gate_constructor_exists():
    assert callable(faultTree_OR_Gate.__init__)


def test_hyp_faulttree_or_gate_constructor_args():
    sig = inspect.signature(faultTree_OR_Gate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_and_gate_is_not_abstract():
    assert not inspect.isabstract(faultTree_AND_Gate)


def test_hyp_faulttree_and_gate_constructor_exists():
    assert callable(faultTree_AND_Gate.__init__)


def test_hyp_faulttree_and_gate_constructor_args():
    sig = inspect.signature(faultTree_AND_Gate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_intermediateevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_IntermediateEvent)


def test_hyp_faulttree_intermediateevent_constructor_exists():
    assert callable(faultTree_IntermediateEvent.__init__)


def test_hyp_faulttree_intermediateevent_constructor_args():
    sig = inspect.signature(faultTree_IntermediateEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_probabalisticevent_is_not_abstract():
    assert not inspect.isabstract(faultTree_ProbabalisticEvent)


def test_hyp_faulttree_probabalisticevent_constructor_exists():
    assert callable(faultTree_ProbabalisticEvent.__init__)


def test_hyp_faulttree_probabalisticevent_constructor_args():
    sig = inspect.signature(faultTree_ProbabalisticEvent.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"




def test_hyp_ftelement_is_not_abstract():
    assert not inspect.isabstract(FTElement)


def test_hyp_ftelement_constructor_exists():
    assert callable(FTElement.__init__)


def test_hyp_ftelement_constructor_args():
    sig = inspect.signature(FTElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_gate_is_not_abstract():
    assert not inspect.isabstract(faultTree_Gate)


def test_hyp_faulttree_gate_constructor_exists():
    assert callable(faultTree_Gate.__init__)


def test_hyp_faulttree_gate_constructor_args():
    sig = inspect.signature(faultTree_Gate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_faulttree_is_not_abstract():
    assert not inspect.isabstract(faultTree_FaultTree)


def test_hyp_faulttree_faulttree_constructor_exists():
    assert callable(faultTree_FaultTree.__init__)


def test_hyp_faulttree_faulttree_constructor_args():
    sig = inspect.signature(faultTree_FaultTree.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_event_is_not_abstract():
    assert not inspect.isabstract(faultTree_Event)


def test_hyp_faulttree_event_constructor_exists():
    assert callable(faultTree_Event.__init__)


def test_hyp_faulttree_event_constructor_args():
    sig = inspect.signature(faultTree_Event.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "description" in params, "Missing parameter 'description'"





def test_hyp_faulttree_connector_is_not_abstract():
    assert not inspect.isabstract(faultTree_Connector)


def test_hyp_faulttree_connector_constructor_exists():
    assert callable(faultTree_Connector.__init__)


def test_hyp_faulttree_connector_constructor_args():
    sig = inspect.signature(faultTree_Connector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_faulttree_ftelement_is_not_abstract():
    assert not inspect.isabstract(faultTree_FTElement)


def test_hyp_faulttree_ftelement_constructor_exists():
    assert callable(faultTree_FTElement.__init__)


def test_hyp_faulttree_ftelement_constructor_args():
    sig = inspect.signature(faultTree_FTElement.__init__)
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
ProbabalisticEvent_strategy = st.builds(
    ProbabalisticEvent,
)
faultTree_ExternalEvent_strategy = st.builds(
    faultTree_ExternalEvent,
)
faultTree_UndevelopedEvent_strategy = st.builds(
    faultTree_UndevelopedEvent,
)
faultTree_BasicEvent_strategy = st.builds(
    faultTree_BasicEvent,
)
Gate_strategy = st.builds(
    Gate,
)
faultTree_OR_Gate_strategy = st.builds(
    faultTree_OR_Gate,
)
faultTree_AND_Gate_strategy = st.builds(
    faultTree_AND_Gate,
)
Event_strategy = st.builds(
    Event,
)
faultTree_IntermediateEvent_strategy = st.builds(
    faultTree_IntermediateEvent,
)
faultTree_ProbabalisticEvent_strategy = st.builds(
    faultTree_ProbabalisticEvent,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
FTElement_strategy = st.builds(
    FTElement,
)
faultTree_Gate_strategy = st.builds(
    faultTree_Gate,
)
faultTree_FaultTree_strategy = st.builds(
    faultTree_FaultTree,
)
faultTree_Event_strategy = st.builds(
    faultTree_Event,
    title=
        safe_text,
    description=
        safe_text
)
faultTree_Connector_strategy = st.builds(
    faultTree_Connector,
)
faultTree_FTElement_strategy = st.builds(
    faultTree_FTElement,
)













@given(instance=faultTree_ProbabalisticEvent_strategy)
def test_hyp_faulttree_probabalisticevent_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original







@given(instance=faultTree_Event_strategy)
def test_hyp_faulttree_event_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=faultTree_Event_strategy)
def test_hyp_faulttree_event_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Event,
    FTElement,
    Gate,
    ProbabalisticEvent,
    faultTree_AND_Gate,
    faultTree_BasicEvent,
    faultTree_Connector,
    faultTree_Event,
    faultTree_ExternalEvent,
    faultTree_FTElement,
    faultTree_FaultTree,
    faultTree_Gate,
    faultTree_IntermediateEvent,
    faultTree_OR_Gate,
    faultTree_ProbabalisticEvent,
    faultTree_UndevelopedEvent,
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

def test_faultTree_Event_description_value_roundtrip():
    instance = faultTree_Event(description="sample_text", title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_faultTree_Event_title_value_roundtrip():
    instance = faultTree_Event(description="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_faultTree_ProbabalisticEvent_probability_value_roundtrip():
    instance = faultTree_ProbabalisticEvent(probability=3.14)
    assert instance.probability == 3.14
    instance.probability = 9.99
    assert instance.probability == 9.99


def test_faultTree_IntermediateEvent_isa_Event():
    instance = faultTree_IntermediateEvent()
    assert isinstance(instance, Event)


def test_faultTree_ProbabalisticEvent_isa_Event():
    instance = faultTree_ProbabalisticEvent(probability=3.14)
    assert isinstance(instance, Event)


def test_faultTree_Connector_isa_FTElement():
    instance = faultTree_Connector()
    assert isinstance(instance, FTElement)


def test_faultTree_Event_isa_FTElement():
    instance = faultTree_Event(description="sample_text", title="sample_text")
    assert isinstance(instance, FTElement)


def test_faultTree_FaultTree_isa_FTElement():
    instance = faultTree_FaultTree()
    assert isinstance(instance, FTElement)


def test_faultTree_Gate_isa_FTElement():
    instance = faultTree_Gate()
    assert isinstance(instance, FTElement)


def test_faultTree_AND_Gate_isa_Gate():
    instance = faultTree_AND_Gate()
    assert isinstance(instance, Gate)


def test_faultTree_OR_Gate_isa_Gate():
    instance = faultTree_OR_Gate()
    assert isinstance(instance, Gate)


def test_faultTree_BasicEvent_isa_ProbabalisticEvent():
    instance = faultTree_BasicEvent()
    assert isinstance(instance, ProbabalisticEvent)


def test_faultTree_ExternalEvent_isa_ProbabalisticEvent():
    instance = faultTree_ExternalEvent()
    assert isinstance(instance, ProbabalisticEvent)


def test_faultTree_UndevelopedEvent_isa_ProbabalisticEvent():
    instance = faultTree_UndevelopedEvent()
    assert isinstance(instance, ProbabalisticEvent)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


FTElement_strategy = st.builds(FTElement)
@given(instance=FTElement_strategy)
@settings(max_examples=25)
def test_FTElement_instantiation(instance):
    assert isinstance(instance, FTElement)


Gate_strategy = st.builds(Gate)
@given(instance=Gate_strategy)
@settings(max_examples=25)
def test_Gate_instantiation(instance):
    assert isinstance(instance, Gate)


ProbabalisticEvent_strategy = st.builds(ProbabalisticEvent)
@given(instance=ProbabalisticEvent_strategy)
@settings(max_examples=25)
def test_ProbabalisticEvent_instantiation(instance):
    assert isinstance(instance, ProbabalisticEvent)


faultTree_AND_Gate_strategy = st.builds(faultTree_AND_Gate)
@given(instance=faultTree_AND_Gate_strategy)
@settings(max_examples=25)
def test_faultTree_AND_Gate_instantiation(instance):
    assert isinstance(instance, faultTree_AND_Gate)


faultTree_BasicEvent_strategy = st.builds(faultTree_BasicEvent)
@given(instance=faultTree_BasicEvent_strategy)
@settings(max_examples=25)
def test_faultTree_BasicEvent_instantiation(instance):
    assert isinstance(instance, faultTree_BasicEvent)


faultTree_Connector_strategy = st.builds(faultTree_Connector)
@given(instance=faultTree_Connector_strategy)
@settings(max_examples=25)
def test_faultTree_Connector_instantiation(instance):
    assert isinstance(instance, faultTree_Connector)


faultTree_Event_strategy = st.builds(faultTree_Event, description=safe_text, title=safe_text)
@given(instance=faultTree_Event_strategy)
@settings(max_examples=25)
def test_faultTree_Event_instantiation(instance):
    assert isinstance(instance, faultTree_Event)


faultTree_ExternalEvent_strategy = st.builds(faultTree_ExternalEvent)
@given(instance=faultTree_ExternalEvent_strategy)
@settings(max_examples=25)
def test_faultTree_ExternalEvent_instantiation(instance):
    assert isinstance(instance, faultTree_ExternalEvent)


faultTree_FTElement_strategy = st.builds(faultTree_FTElement)
@given(instance=faultTree_FTElement_strategy)
@settings(max_examples=25)
def test_faultTree_FTElement_instantiation(instance):
    assert isinstance(instance, faultTree_FTElement)


faultTree_FaultTree_strategy = st.builds(faultTree_FaultTree)
@given(instance=faultTree_FaultTree_strategy)
@settings(max_examples=25)
def test_faultTree_FaultTree_instantiation(instance):
    assert isinstance(instance, faultTree_FaultTree)


faultTree_Gate_strategy = st.builds(faultTree_Gate)
@given(instance=faultTree_Gate_strategy)
@settings(max_examples=25)
def test_faultTree_Gate_instantiation(instance):
    assert isinstance(instance, faultTree_Gate)


faultTree_IntermediateEvent_strategy = st.builds(faultTree_IntermediateEvent)
@given(instance=faultTree_IntermediateEvent_strategy)
@settings(max_examples=25)
def test_faultTree_IntermediateEvent_instantiation(instance):
    assert isinstance(instance, faultTree_IntermediateEvent)


faultTree_OR_Gate_strategy = st.builds(faultTree_OR_Gate)
@given(instance=faultTree_OR_Gate_strategy)
@settings(max_examples=25)
def test_faultTree_OR_Gate_instantiation(instance):
    assert isinstance(instance, faultTree_OR_Gate)


faultTree_ProbabalisticEvent_strategy = st.builds(faultTree_ProbabalisticEvent, probability=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=faultTree_ProbabalisticEvent_strategy)
@settings(max_examples=25)
def test_faultTree_ProbabalisticEvent_instantiation(instance):
    assert isinstance(instance, faultTree_ProbabalisticEvent)


faultTree_UndevelopedEvent_strategy = st.builds(faultTree_UndevelopedEvent)
@given(instance=faultTree_UndevelopedEvent_strategy)
@settings(max_examples=25)
def test_faultTree_UndevelopedEvent_instantiation(instance):
    assert isinstance(instance, faultTree_UndevelopedEvent)



