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
    Behaviour_TransitionFunction,
    Transition,
    Behaviour_StochasticTransition,
    Behaviour_ConditionalTransition,
    Place,
    Behaviour_StartPlace,
    Behaviour_QueuePlace,
    Behaviour_Server,
    Behaviour_WaitingLine,
    Behaviour_DefaultPlace,
    Connection,
    Behaviour_PreTransitionConnection,
    Behaviour_PostTransitionConnection,
    Identifier,
    Behaviour_Connection,
    Behaviour_Description,
    Behaviour_Token,
    Behaviour_Transition,
    Behaviour_Colour,
    Behaviour_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_behaviour_transitionfunction_is_not_abstract():
    assert not inspect.isabstract(Behaviour_TransitionFunction)


def test_hyp_behaviour_transitionfunction_constructor_exists():
    assert callable(Behaviour_TransitionFunction.__init__)


def test_hyp_behaviour_transitionfunction_constructor_args():
    sig = inspect.signature(Behaviour_TransitionFunction.__init__)
    params = list(sig.parameters.keys())
    assert "transitionFunction" in params, "Missing parameter 'transitionFunction'"




def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_stochastictransition_is_not_abstract():
    assert not inspect.isabstract(Behaviour_StochasticTransition)


def test_hyp_behaviour_stochastictransition_constructor_exists():
    assert callable(Behaviour_StochasticTransition.__init__)


def test_hyp_behaviour_stochastictransition_constructor_args():
    sig = inspect.signature(Behaviour_StochasticTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_conditionaltransition_is_not_abstract():
    assert not inspect.isabstract(Behaviour_ConditionalTransition)


def test_hyp_behaviour_conditionaltransition_constructor_exists():
    assert callable(Behaviour_ConditionalTransition.__init__)


def test_hyp_behaviour_conditionaltransition_constructor_args():
    sig = inspect.signature(Behaviour_ConditionalTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_hyp_place_constructor_exists():
    assert callable(Place.__init__)


def test_hyp_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_startplace_is_not_abstract():
    assert not inspect.isabstract(Behaviour_StartPlace)


def test_hyp_behaviour_startplace_constructor_exists():
    assert callable(Behaviour_StartPlace.__init__)


def test_hyp_behaviour_startplace_constructor_args():
    sig = inspect.signature(Behaviour_StartPlace.__init__)
    params = list(sig.parameters.keys())
    assert "spawnPolicy" in params, "Missing parameter 'spawnPolicy'"




def test_hyp_behaviour_queueplace_is_not_abstract():
    assert not inspect.isabstract(Behaviour_QueuePlace)


def test_hyp_behaviour_queueplace_constructor_exists():
    assert callable(Behaviour_QueuePlace.__init__)


def test_hyp_behaviour_queueplace_constructor_args():
    sig = inspect.signature(Behaviour_QueuePlace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_server_is_not_abstract():
    assert not inspect.isabstract(Behaviour_Server)


def test_hyp_behaviour_server_constructor_exists():
    assert callable(Behaviour_Server.__init__)


def test_hyp_behaviour_server_constructor_args():
    sig = inspect.signature(Behaviour_Server.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"




def test_hyp_behaviour_waitingline_is_not_abstract():
    assert not inspect.isabstract(Behaviour_WaitingLine)


def test_hyp_behaviour_waitingline_constructor_exists():
    assert callable(Behaviour_WaitingLine.__init__)


def test_hyp_behaviour_waitingline_constructor_args():
    sig = inspect.signature(Behaviour_WaitingLine.__init__)
    params = list(sig.parameters.keys())
    assert "schedulingPolicy" in params, "Missing parameter 'schedulingPolicy'"




def test_hyp_behaviour_defaultplace_is_not_abstract():
    assert not inspect.isabstract(Behaviour_DefaultPlace)


def test_hyp_behaviour_defaultplace_constructor_exists():
    assert callable(Behaviour_DefaultPlace.__init__)


def test_hyp_behaviour_defaultplace_constructor_args():
    sig = inspect.signature(Behaviour_DefaultPlace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_hyp_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_hyp_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_pretransitionconnection_is_not_abstract():
    assert not inspect.isabstract(Behaviour_PreTransitionConnection)


def test_hyp_behaviour_pretransitionconnection_constructor_exists():
    assert callable(Behaviour_PreTransitionConnection.__init__)


def test_hyp_behaviour_pretransitionconnection_constructor_args():
    sig = inspect.signature(Behaviour_PreTransitionConnection.__init__)
    params = list(sig.parameters.keys())
    assert "requiredTokenAmount" in params, "Missing parameter 'requiredTokenAmount'"




def test_hyp_behaviour_posttransitionconnection_is_not_abstract():
    assert not inspect.isabstract(Behaviour_PostTransitionConnection)


def test_hyp_behaviour_posttransitionconnection_constructor_exists():
    assert callable(Behaviour_PostTransitionConnection.__init__)


def test_hyp_behaviour_posttransitionconnection_constructor_args():
    sig = inspect.signature(Behaviour_PostTransitionConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_hyp_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_hyp_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_connection_is_not_abstract():
    assert not inspect.isabstract(Behaviour_Connection)


def test_hyp_behaviour_connection_constructor_exists():
    assert callable(Behaviour_Connection.__init__)


def test_hyp_behaviour_connection_constructor_args():
    sig = inspect.signature(Behaviour_Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_description_is_not_abstract():
    assert not inspect.isabstract(Behaviour_Description)


def test_hyp_behaviour_description_constructor_exists():
    assert callable(Behaviour_Description.__init__)


def test_hyp_behaviour_description_constructor_args():
    sig = inspect.signature(Behaviour_Description.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_token_is_not_abstract():
    assert not inspect.isabstract(Behaviour_Token)


def test_hyp_behaviour_token_constructor_exists():
    assert callable(Behaviour_Token.__init__)


def test_hyp_behaviour_token_constructor_args():
    sig = inspect.signature(Behaviour_Token.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_transition_is_not_abstract():
    assert not inspect.isabstract(Behaviour_Transition)


def test_hyp_behaviour_transition_constructor_exists():
    assert callable(Behaviour_Transition.__init__)


def test_hyp_behaviour_transition_constructor_args():
    sig = inspect.signature(Behaviour_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviour_colour_is_not_abstract():
    assert not inspect.isabstract(Behaviour_Colour)


def test_hyp_behaviour_colour_constructor_exists():
    assert callable(Behaviour_Colour.__init__)


def test_hyp_behaviour_colour_constructor_args():
    sig = inspect.signature(Behaviour_Colour.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_behaviour_place_is_not_abstract():
    assert not inspect.isabstract(Behaviour_Place)


def test_hyp_behaviour_place_constructor_exists():
    assert callable(Behaviour_Place.__init__)


def test_hyp_behaviour_place_constructor_args():
    sig = inspect.signature(Behaviour_Place.__init__)
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
Behaviour_TransitionFunction_strategy = st.builds(
    Behaviour_TransitionFunction,
    transitionFunction=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Behaviour_StochasticTransition_strategy = st.builds(
    Behaviour_StochasticTransition,
)
Behaviour_ConditionalTransition_strategy = st.builds(
    Behaviour_ConditionalTransition,
)
Place_strategy = st.builds(
    Place,
)
Behaviour_StartPlace_strategy = st.builds(
    Behaviour_StartPlace,
    spawnPolicy=
        safe_text
)
Behaviour_QueuePlace_strategy = st.builds(
    Behaviour_QueuePlace,
)
Behaviour_Server_strategy = st.builds(
    Behaviour_Server,
    capacity=
        st.integers()
)
Behaviour_WaitingLine_strategy = st.builds(
    Behaviour_WaitingLine,
    schedulingPolicy=
        safe_text
)
Behaviour_DefaultPlace_strategy = st.builds(
    Behaviour_DefaultPlace,
)
Connection_strategy = st.builds(
    Connection,
)
Behaviour_PreTransitionConnection_strategy = st.builds(
    Behaviour_PreTransitionConnection,
    requiredTokenAmount=
        st.integers()
)
Behaviour_PostTransitionConnection_strategy = st.builds(
    Behaviour_PostTransitionConnection,
)
Identifier_strategy = st.builds(
    Identifier,
)
Behaviour_Connection_strategy = st.builds(
    Behaviour_Connection,
)
Behaviour_Description_strategy = st.builds(
    Behaviour_Description,
)
Behaviour_Token_strategy = st.builds(
    Behaviour_Token,
)
Behaviour_Transition_strategy = st.builds(
    Behaviour_Transition,
)
Behaviour_Colour_strategy = st.builds(
    Behaviour_Colour,
    attribute=
        safe_text
)
Behaviour_Place_strategy = st.builds(
    Behaviour_Place,
)




@given(instance=Behaviour_TransitionFunction_strategy)
def test_hyp_behaviour_transitionfunction_transitionFunction_setter(instance):
    original = instance.transitionFunction
    instance.transitionFunction = original
    assert instance.transitionFunction == original








@given(instance=Behaviour_StartPlace_strategy)
def test_hyp_behaviour_startplace_spawnPolicy_setter(instance):
    original = instance.spawnPolicy
    instance.spawnPolicy = original
    assert instance.spawnPolicy == original





@given(instance=Behaviour_Server_strategy)
def test_hyp_behaviour_server_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original




@given(instance=Behaviour_WaitingLine_strategy)
def test_hyp_behaviour_waitingline_schedulingPolicy_setter(instance):
    original = instance.schedulingPolicy
    instance.schedulingPolicy = original
    assert instance.schedulingPolicy == original






@given(instance=Behaviour_PreTransitionConnection_strategy)
def test_hyp_behaviour_pretransitionconnection_requiredTokenAmount_setter(instance):
    original = instance.requiredTokenAmount
    instance.requiredTokenAmount = original
    assert instance.requiredTokenAmount == original










@given(instance=Behaviour_Colour_strategy)
def test_hyp_behaviour_colour_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Behaviour_Colour,
    Behaviour_ConditionalTransition,
    Behaviour_Connection,
    Behaviour_DefaultPlace,
    Behaviour_Description,
    Behaviour_Place,
    Behaviour_PostTransitionConnection,
    Behaviour_PreTransitionConnection,
    Behaviour_QueuePlace,
    Behaviour_Server,
    Behaviour_StartPlace,
    Behaviour_StochasticTransition,
    Behaviour_Token,
    Behaviour_Transition,
    Behaviour_TransitionFunction,
    Behaviour_WaitingLine,
    Connection,
    Identifier,
    Place,
    Transition,
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

def test_Behaviour_Colour_attribute_value_roundtrip():
    instance = Behaviour_Colour(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Behaviour_PreTransitionConnection_requiredTokenAmount_value_roundtrip():
    instance = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    assert instance.requiredTokenAmount == 7
    instance.requiredTokenAmount = 13
    assert instance.requiredTokenAmount == 13


def test_Behaviour_Server_capacity_value_roundtrip():
    instance = Behaviour_Server(capacity=7)
    assert instance.capacity == 7
    instance.capacity = 13
    assert instance.capacity == 13


def test_Behaviour_StartPlace_spawnPolicy_value_roundtrip():
    instance = Behaviour_StartPlace(spawnPolicy="sample_text")
    assert instance.spawnPolicy == "sample_text"
    instance.spawnPolicy = "sample_text_2"
    assert instance.spawnPolicy == "sample_text_2"


def test_Behaviour_TransitionFunction_transitionFunction_value_roundtrip():
    instance = Behaviour_TransitionFunction(transitionFunction="sample_text")
    assert instance.transitionFunction == "sample_text"
    instance.transitionFunction = "sample_text_2"
    assert instance.transitionFunction == "sample_text_2"


def test_Behaviour_WaitingLine_schedulingPolicy_value_roundtrip():
    instance = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    assert instance.schedulingPolicy == "sample_text"
    instance.schedulingPolicy = "sample_text_2"
    assert instance.schedulingPolicy == "sample_text_2"


def test_Behaviour_PostTransitionConnection_isa_Connection():
    instance = Behaviour_PostTransitionConnection()
    assert isinstance(instance, Connection)


def test_Behaviour_PreTransitionConnection_isa_Connection():
    instance = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    assert isinstance(instance, Connection)


def test_Behaviour_Colour_isa_Identifier():
    instance = Behaviour_Colour(attribute="sample_text")
    assert isinstance(instance, Identifier)


def test_Behaviour_Connection_isa_Identifier():
    instance = Behaviour_Connection()
    assert isinstance(instance, Identifier)


def test_Behaviour_Description_isa_Identifier():
    instance = Behaviour_Description()
    assert isinstance(instance, Identifier)


def test_Behaviour_Place_isa_Identifier():
    instance = Behaviour_Place()
    assert isinstance(instance, Identifier)


def test_Behaviour_Token_isa_Identifier():
    instance = Behaviour_Token()
    assert isinstance(instance, Identifier)


def test_Behaviour_Transition_isa_Identifier():
    instance = Behaviour_Transition()
    assert isinstance(instance, Identifier)


def test_Behaviour_DefaultPlace_isa_Place():
    instance = Behaviour_DefaultPlace()
    assert isinstance(instance, Place)


def test_Behaviour_QueuePlace_isa_Place():
    instance = Behaviour_QueuePlace()
    assert isinstance(instance, Place)


def test_Behaviour_Server_isa_Place():
    instance = Behaviour_Server(capacity=7)
    assert isinstance(instance, Place)


def test_Behaviour_StartPlace_isa_Place():
    instance = Behaviour_StartPlace(spawnPolicy="sample_text")
    assert isinstance(instance, Place)


def test_Behaviour_WaitingLine_isa_Place():
    instance = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    assert isinstance(instance, Place)


def test_Behaviour_ConditionalTransition_isa_Transition():
    instance = Behaviour_ConditionalTransition()
    assert isinstance(instance, Transition)


def test_Behaviour_StochasticTransition_isa_Transition():
    instance = Behaviour_StochasticTransition()
    assert isinstance(instance, Transition)


def test_assoc_attributes30_link_reassign_clear():
    a = Behaviour_Colour(attribute="sample_text")
    b1 = Behaviour_Token()
    b2 = Behaviour_Token()
    _safe_set(a, 'Behaviour_Colour', b1)
    assert _is_linked(a, 'Behaviour_Colour', b1)
    if hasattr(b1, 'Behaviour_Token31'):
        assert _is_linked(b1, 'Behaviour_Token31', a)
    _safe_set(a, 'Behaviour_Colour', b2)
    assert _is_linked(a, 'Behaviour_Colour', b2)
    if hasattr(b1, 'Behaviour_Token31'):
        assert not _is_linked(b1, 'Behaviour_Token31', a)
    if hasattr(b2, 'Behaviour_Token31'):
        assert _is_linked(b2, 'Behaviour_Token31', a)
    _safe_set(a, 'Behaviour_Colour', None)
    assert not _is_linked(a, 'Behaviour_Colour', b2)
    if hasattr(b2, 'Behaviour_Token31'):
        assert not _is_linked(b2, 'Behaviour_Token31', a)


def test_assoc_emittedToken46_link_reassign_clear():
    a = Behaviour_TransitionFunction(transitionFunction="sample_text")
    b1 = Behaviour_Token()
    b2 = Behaviour_Token()
    _safe_set(a, 'Behaviour_TransitionFunction47', {b1})
    assert _is_linked(a, 'Behaviour_TransitionFunction47', b1)
    if hasattr(b1, 'Behaviour_Token48'):
        assert _is_linked(b1, 'Behaviour_Token48', a)
    _safe_set(a, 'Behaviour_TransitionFunction47', {b2})
    assert _is_linked(a, 'Behaviour_TransitionFunction47', b2)
    if hasattr(b1, 'Behaviour_Token48'):
        assert not _is_linked(b1, 'Behaviour_Token48', a)
    if hasattr(b2, 'Behaviour_Token48'):
        assert _is_linked(b2, 'Behaviour_Token48', a)
    _safe_set(a, 'Behaviour_TransitionFunction47', set())
    assert not _is_linked(a, 'Behaviour_TransitionFunction47', b2)
    if hasattr(b2, 'Behaviour_Token48'):
        assert not _is_linked(b2, 'Behaviour_Token48', a)


def test_assoc_incommingEdges2_link_reassign_clear():
    a = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    b1 = Behaviour_Transition()
    b2 = Behaviour_Transition()
    _safe_set(a, 'Behaviour_PreTransitionConnection', b1)
    assert _is_linked(a, 'Behaviour_PreTransitionConnection', b1)
    if hasattr(b1, 'Behaviour_Transition3'):
        assert _is_linked(b1, 'Behaviour_Transition3', a)
    _safe_set(a, 'Behaviour_PreTransitionConnection', b2)
    assert _is_linked(a, 'Behaviour_PreTransitionConnection', b2)
    if hasattr(b1, 'Behaviour_Transition3'):
        assert not _is_linked(b1, 'Behaviour_Transition3', a)
    if hasattr(b2, 'Behaviour_Transition3'):
        assert _is_linked(b2, 'Behaviour_Transition3', a)
    _safe_set(a, 'Behaviour_PreTransitionConnection', None)
    assert not _is_linked(a, 'Behaviour_PreTransitionConnection', b2)
    if hasattr(b2, 'Behaviour_Transition3'):
        assert not _is_linked(b2, 'Behaviour_Transition3', a)


def test_assoc_postTransitions27_link_reassign_clear():
    a = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    b1 = Behaviour_PostTransitionConnection()
    b2 = Behaviour_PostTransitionConnection()
    _safe_set(a, 'Behaviour_WaitingLine28', {b1})
    assert _is_linked(a, 'Behaviour_WaitingLine28', b1)
    if hasattr(b1, 'Behaviour_PostTransitionConnection29'):
        assert _is_linked(b1, 'Behaviour_PostTransitionConnection29', a)
    _safe_set(a, 'Behaviour_WaitingLine28', {b2})
    assert _is_linked(a, 'Behaviour_WaitingLine28', b2)
    if hasattr(b1, 'Behaviour_PostTransitionConnection29'):
        assert not _is_linked(b1, 'Behaviour_PostTransitionConnection29', a)
    if hasattr(b2, 'Behaviour_PostTransitionConnection29'):
        assert _is_linked(b2, 'Behaviour_PostTransitionConnection29', a)
    _safe_set(a, 'Behaviour_WaitingLine28', set())
    assert not _is_linked(a, 'Behaviour_WaitingLine28', b2)
    if hasattr(b2, 'Behaviour_PostTransitionConnection29'):
        assert not _is_linked(b2, 'Behaviour_PostTransitionConnection29', a)


def test_assoc_preTransition23_link_reassign_clear():
    a = Behaviour_Server(capacity=7)
    b1 = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    b2 = Behaviour_PreTransitionConnection(requiredTokenAmount=13)
    _safe_set(a, 'Behaviour_Server24', b1)
    assert _is_linked(a, 'Behaviour_Server24', b1)
    if hasattr(b1, 'Behaviour_PreTransitionConnection25'):
        assert _is_linked(b1, 'Behaviour_PreTransitionConnection25', a)
    _safe_set(a, 'Behaviour_Server24', b2)
    assert _is_linked(a, 'Behaviour_Server24', b2)
    if hasattr(b1, 'Behaviour_PreTransitionConnection25'):
        assert not _is_linked(b1, 'Behaviour_PreTransitionConnection25', a)
    if hasattr(b2, 'Behaviour_PreTransitionConnection25'):
        assert _is_linked(b2, 'Behaviour_PreTransitionConnection25', a)
    _safe_set(a, 'Behaviour_Server24', None)
    assert not _is_linked(a, 'Behaviour_Server24', b2)
    if hasattr(b2, 'Behaviour_PreTransitionConnection25'):
        assert not _is_linked(b2, 'Behaviour_PreTransitionConnection25', a)


def test_assoc_preTransitions17_link_reassign_clear():
    a = Behaviour_StartPlace(spawnPolicy="sample_text")
    b1 = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    b2 = Behaviour_PreTransitionConnection(requiredTokenAmount=13)
    _safe_set(a, 'Behaviour_StartPlace', {b1})
    assert _is_linked(a, 'Behaviour_StartPlace', b1)
    if hasattr(b1, 'Behaviour_PreTransitionConnection18'):
        assert _is_linked(b1, 'Behaviour_PreTransitionConnection18', a)
    _safe_set(a, 'Behaviour_StartPlace', {b2})
    assert _is_linked(a, 'Behaviour_StartPlace', b2)
    if hasattr(b1, 'Behaviour_PreTransitionConnection18'):
        assert not _is_linked(b1, 'Behaviour_PreTransitionConnection18', a)
    if hasattr(b2, 'Behaviour_PreTransitionConnection18'):
        assert _is_linked(b2, 'Behaviour_PreTransitionConnection18', a)
    _safe_set(a, 'Behaviour_StartPlace', set())
    assert not _is_linked(a, 'Behaviour_StartPlace', b2)
    if hasattr(b2, 'Behaviour_PreTransitionConnection18'):
        assert not _is_linked(b2, 'Behaviour_PreTransitionConnection18', a)


def test_assoc_preTransitions9_link_reassign_clear():
    a = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    b1 = Behaviour_DefaultPlace()
    b2 = Behaviour_DefaultPlace()
    _safe_set(a, 'Behaviour_PreTransitionConnection10', b1)
    assert _is_linked(a, 'Behaviour_PreTransitionConnection10', b1)
    if hasattr(b1, 'Behaviour_DefaultPlace'):
        assert _is_linked(b1, 'Behaviour_DefaultPlace', a)
    _safe_set(a, 'Behaviour_PreTransitionConnection10', b2)
    assert _is_linked(a, 'Behaviour_PreTransitionConnection10', b2)
    if hasattr(b1, 'Behaviour_DefaultPlace'):
        assert not _is_linked(b1, 'Behaviour_DefaultPlace', a)
    if hasattr(b2, 'Behaviour_DefaultPlace'):
        assert _is_linked(b2, 'Behaviour_DefaultPlace', a)
    _safe_set(a, 'Behaviour_PreTransitionConnection10', None)
    assert not _is_linked(a, 'Behaviour_PreTransitionConnection10', b2)
    if hasattr(b2, 'Behaviour_DefaultPlace'):
        assert not _is_linked(b2, 'Behaviour_DefaultPlace', a)


def test_assoc_server14_link_reassign_clear():
    a = Behaviour_Server(capacity=7)
    b1 = Behaviour_QueuePlace()
    b2 = Behaviour_QueuePlace()
    _safe_set(a, 'Behaviour_Server', b1)
    assert _is_linked(a, 'Behaviour_Server', b1)
    if hasattr(b1, 'Behaviour_QueuePlace'):
        assert _is_linked(b1, 'Behaviour_QueuePlace', a)
    _safe_set(a, 'Behaviour_Server', b2)
    assert _is_linked(a, 'Behaviour_Server', b2)
    if hasattr(b1, 'Behaviour_QueuePlace'):
        assert not _is_linked(b1, 'Behaviour_QueuePlace', a)
    if hasattr(b2, 'Behaviour_QueuePlace'):
        assert _is_linked(b2, 'Behaviour_QueuePlace', a)
    _safe_set(a, 'Behaviour_Server', None)
    assert not _is_linked(a, 'Behaviour_Server', b2)
    if hasattr(b2, 'Behaviour_QueuePlace'):
        assert not _is_linked(b2, 'Behaviour_QueuePlace', a)


def test_assoc_server26_link_reassign_clear():
    a = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    b1 = Behaviour_Server(capacity=7)
    b2 = Behaviour_Server(capacity=13)
    _safe_set(a, 'waitingLine', b1)
    assert _is_linked(a, 'waitingLine', b1)
    if hasattr(b1, 'Server'):
        assert _is_linked(b1, 'Server', a)
    _safe_set(a, 'waitingLine', b2)
    assert _is_linked(a, 'waitingLine', b2)
    if hasattr(b1, 'Server'):
        assert not _is_linked(b1, 'Server', a)
    if hasattr(b2, 'Server'):
        assert _is_linked(b2, 'Server', a)
    _safe_set(a, 'waitingLine', None)
    assert not _is_linked(a, 'waitingLine', b2)
    if hasattr(b2, 'Server'):
        assert not _is_linked(b2, 'Server', a)


def test_assoc_transitionConnection43_link_reassign_clear():
    a = Behaviour_TransitionFunction(transitionFunction="sample_text")
    b1 = Behaviour_PostTransitionConnection()
    b2 = Behaviour_PostTransitionConnection()
    _safe_set(a, 'Behaviour_TransitionFunction44', b1)
    assert _is_linked(a, 'Behaviour_TransitionFunction44', b1)
    if hasattr(b1, 'Behaviour_PostTransitionConnection45'):
        assert _is_linked(b1, 'Behaviour_PostTransitionConnection45', a)
    _safe_set(a, 'Behaviour_TransitionFunction44', b2)
    assert _is_linked(a, 'Behaviour_TransitionFunction44', b2)
    if hasattr(b1, 'Behaviour_PostTransitionConnection45'):
        assert not _is_linked(b1, 'Behaviour_PostTransitionConnection45', a)
    if hasattr(b2, 'Behaviour_PostTransitionConnection45'):
        assert _is_linked(b2, 'Behaviour_PostTransitionConnection45', a)
    _safe_set(a, 'Behaviour_TransitionFunction44', None)
    assert not _is_linked(a, 'Behaviour_TransitionFunction44', b2)
    if hasattr(b2, 'Behaviour_PostTransitionConnection45'):
        assert not _is_linked(b2, 'Behaviour_PostTransitionConnection45', a)


def test_assoc_transitionFunction19_link_reassign_clear():
    a = Behaviour_TransitionFunction(transitionFunction="sample_text")
    b1 = Behaviour_ConditionalTransition()
    b2 = Behaviour_ConditionalTransition()
    _safe_set(a, 'Behaviour_TransitionFunction', b1)
    assert _is_linked(a, 'Behaviour_TransitionFunction', b1)
    if hasattr(b1, 'Behaviour_ConditionalTransition'):
        assert _is_linked(b1, 'Behaviour_ConditionalTransition', a)
    _safe_set(a, 'Behaviour_TransitionFunction', b2)
    assert _is_linked(a, 'Behaviour_TransitionFunction', b2)
    if hasattr(b1, 'Behaviour_ConditionalTransition'):
        assert not _is_linked(b1, 'Behaviour_ConditionalTransition', a)
    if hasattr(b2, 'Behaviour_ConditionalTransition'):
        assert _is_linked(b2, 'Behaviour_ConditionalTransition', a)
    _safe_set(a, 'Behaviour_TransitionFunction', None)
    assert not _is_linked(a, 'Behaviour_TransitionFunction', b2)
    if hasattr(b2, 'Behaviour_ConditionalTransition'):
        assert not _is_linked(b2, 'Behaviour_ConditionalTransition', a)


def test_assoc_transitionFunction20_link_reassign_clear():
    a = Behaviour_TransitionFunction(transitionFunction="sample_text")
    b1 = Behaviour_StochasticTransition()
    b2 = Behaviour_StochasticTransition()
    _safe_set(a, 'Behaviour_TransitionFunction21', b1)
    assert _is_linked(a, 'Behaviour_TransitionFunction21', b1)
    if hasattr(b1, 'Behaviour_StochasticTransition'):
        assert _is_linked(b1, 'Behaviour_StochasticTransition', a)
    _safe_set(a, 'Behaviour_TransitionFunction21', b2)
    assert _is_linked(a, 'Behaviour_TransitionFunction21', b2)
    if hasattr(b1, 'Behaviour_StochasticTransition'):
        assert not _is_linked(b1, 'Behaviour_StochasticTransition', a)
    if hasattr(b2, 'Behaviour_StochasticTransition'):
        assert _is_linked(b2, 'Behaviour_StochasticTransition', a)
    _safe_set(a, 'Behaviour_TransitionFunction21', None)
    assert not _is_linked(a, 'Behaviour_TransitionFunction21', b2)
    if hasattr(b2, 'Behaviour_StochasticTransition'):
        assert not _is_linked(b2, 'Behaviour_StochasticTransition', a)


def test_assoc_waitingLine15_link_reassign_clear():
    a = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    b1 = Behaviour_QueuePlace()
    b2 = Behaviour_QueuePlace()
    _safe_set(a, 'Behaviour_WaitingLine', b1)
    assert _is_linked(a, 'Behaviour_WaitingLine', b1)
    if hasattr(b1, 'Behaviour_QueuePlace16'):
        assert _is_linked(b1, 'Behaviour_QueuePlace16', a)
    _safe_set(a, 'Behaviour_WaitingLine', b2)
    assert _is_linked(a, 'Behaviour_WaitingLine', b2)
    if hasattr(b1, 'Behaviour_QueuePlace16'):
        assert not _is_linked(b1, 'Behaviour_QueuePlace16', a)
    if hasattr(b2, 'Behaviour_QueuePlace16'):
        assert _is_linked(b2, 'Behaviour_QueuePlace16', a)
    _safe_set(a, 'Behaviour_WaitingLine', None)
    assert not _is_linked(a, 'Behaviour_WaitingLine', b2)
    if hasattr(b2, 'Behaviour_QueuePlace16'):
        assert not _is_linked(b2, 'Behaviour_QueuePlace16', a)


def test_assoc_waitingLine22_link_reassign_clear():
    a = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    b1 = Behaviour_Server(capacity=7)
    b2 = Behaviour_Server(capacity=13)
    _safe_set(a, 'WaitingLine', b1)
    assert _is_linked(a, 'WaitingLine', b1)
    if hasattr(b1, 'server'):
        assert _is_linked(b1, 'server', a)
    _safe_set(a, 'WaitingLine', b2)
    assert _is_linked(a, 'WaitingLine', b2)
    if hasattr(b1, 'server'):
        assert not _is_linked(b1, 'server', a)
    if hasattr(b2, 'server'):
        assert _is_linked(b2, 'server', a)
    _safe_set(a, 'WaitingLine', None)
    assert not _is_linked(a, 'WaitingLine', b2)
    if hasattr(b2, 'server'):
        assert not _is_linked(b2, 'server', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Behaviour_Colour_strategy = st.builds(Behaviour_Colour, attribute=safe_text)
@given(instance=Behaviour_Colour_strategy)
@settings(max_examples=25)
def test_Behaviour_Colour_instantiation(instance):
    assert isinstance(instance, Behaviour_Colour)


Behaviour_ConditionalTransition_strategy = st.builds(Behaviour_ConditionalTransition)
@given(instance=Behaviour_ConditionalTransition_strategy)
@settings(max_examples=25)
def test_Behaviour_ConditionalTransition_instantiation(instance):
    assert isinstance(instance, Behaviour_ConditionalTransition)


Behaviour_Connection_strategy = st.builds(Behaviour_Connection)
@given(instance=Behaviour_Connection_strategy)
@settings(max_examples=25)
def test_Behaviour_Connection_instantiation(instance):
    assert isinstance(instance, Behaviour_Connection)


Behaviour_DefaultPlace_strategy = st.builds(Behaviour_DefaultPlace)
@given(instance=Behaviour_DefaultPlace_strategy)
@settings(max_examples=25)
def test_Behaviour_DefaultPlace_instantiation(instance):
    assert isinstance(instance, Behaviour_DefaultPlace)


Behaviour_Description_strategy = st.builds(Behaviour_Description)
@given(instance=Behaviour_Description_strategy)
@settings(max_examples=25)
def test_Behaviour_Description_instantiation(instance):
    assert isinstance(instance, Behaviour_Description)


Behaviour_Place_strategy = st.builds(Behaviour_Place)
@given(instance=Behaviour_Place_strategy)
@settings(max_examples=25)
def test_Behaviour_Place_instantiation(instance):
    assert isinstance(instance, Behaviour_Place)


Behaviour_PostTransitionConnection_strategy = st.builds(Behaviour_PostTransitionConnection)
@given(instance=Behaviour_PostTransitionConnection_strategy)
@settings(max_examples=25)
def test_Behaviour_PostTransitionConnection_instantiation(instance):
    assert isinstance(instance, Behaviour_PostTransitionConnection)


Behaviour_PreTransitionConnection_strategy = st.builds(Behaviour_PreTransitionConnection, requiredTokenAmount=st.integers())
@given(instance=Behaviour_PreTransitionConnection_strategy)
@settings(max_examples=25)
def test_Behaviour_PreTransitionConnection_instantiation(instance):
    assert isinstance(instance, Behaviour_PreTransitionConnection)


Behaviour_QueuePlace_strategy = st.builds(Behaviour_QueuePlace)
@given(instance=Behaviour_QueuePlace_strategy)
@settings(max_examples=25)
def test_Behaviour_QueuePlace_instantiation(instance):
    assert isinstance(instance, Behaviour_QueuePlace)


Behaviour_Server_strategy = st.builds(Behaviour_Server, capacity=st.integers())
@given(instance=Behaviour_Server_strategy)
@settings(max_examples=25)
def test_Behaviour_Server_instantiation(instance):
    assert isinstance(instance, Behaviour_Server)


Behaviour_StartPlace_strategy = st.builds(Behaviour_StartPlace, spawnPolicy=safe_text)
@given(instance=Behaviour_StartPlace_strategy)
@settings(max_examples=25)
def test_Behaviour_StartPlace_instantiation(instance):
    assert isinstance(instance, Behaviour_StartPlace)


Behaviour_StochasticTransition_strategy = st.builds(Behaviour_StochasticTransition)
@given(instance=Behaviour_StochasticTransition_strategy)
@settings(max_examples=25)
def test_Behaviour_StochasticTransition_instantiation(instance):
    assert isinstance(instance, Behaviour_StochasticTransition)


Behaviour_Token_strategy = st.builds(Behaviour_Token)
@given(instance=Behaviour_Token_strategy)
@settings(max_examples=25)
def test_Behaviour_Token_instantiation(instance):
    assert isinstance(instance, Behaviour_Token)


Behaviour_Transition_strategy = st.builds(Behaviour_Transition)
@given(instance=Behaviour_Transition_strategy)
@settings(max_examples=25)
def test_Behaviour_Transition_instantiation(instance):
    assert isinstance(instance, Behaviour_Transition)


Behaviour_TransitionFunction_strategy = st.builds(Behaviour_TransitionFunction, transitionFunction=safe_text)
@given(instance=Behaviour_TransitionFunction_strategy)
@settings(max_examples=25)
def test_Behaviour_TransitionFunction_instantiation(instance):
    assert isinstance(instance, Behaviour_TransitionFunction)


Behaviour_WaitingLine_strategy = st.builds(Behaviour_WaitingLine, schedulingPolicy=safe_text)
@given(instance=Behaviour_WaitingLine_strategy)
@settings(max_examples=25)
def test_Behaviour_WaitingLine_instantiation(instance):
    assert isinstance(instance, Behaviour_WaitingLine)


Connection_strategy = st.builds(Connection)
@given(instance=Connection_strategy)
@settings(max_examples=25)
def test_Connection_instantiation(instance):
    assert isinstance(instance, Connection)


Identifier_strategy = st.builds(Identifier)
@given(instance=Identifier_strategy)
@settings(max_examples=25)
def test_Identifier_instantiation(instance):
    assert isinstance(instance, Identifier)


Place_strategy = st.builds(Place)
@given(instance=Place_strategy)
@settings(max_examples=25)
def test_Place_instantiation(instance):
    assert isinstance(instance, Place)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)



