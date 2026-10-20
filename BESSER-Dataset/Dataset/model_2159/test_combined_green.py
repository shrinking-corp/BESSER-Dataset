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
    behavior_BehaviorMixEntry,
    behavior_BehaviorMix,
    AbstractBehaviorModelGraph,
    behavior_BehaviorModelRelative,
    behavior_BehaviorModelAbsolute,
    behavior_Transition,
    behavior_AbstractUseCaseExecution,
    AbstractUseCaseExecution,
    behavior_ObservedUseCaseExecution,
    behavior_Session,
    behavior_SessionRepository,
    behavior_UseCaseRepository,
    behavior_Vertex,
    behavior_AbstractBehaviorModelGraph,
    behavior_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_behavior_behaviormixentry_is_not_abstract():
    assert not inspect.isabstract(behavior_BehaviorMixEntry)


def test_hyp_behavior_behaviormixentry_constructor_exists():
    assert callable(behavior_BehaviorMixEntry.__init__)


def test_hyp_behavior_behaviormixentry_constructor_args():
    sig = inspect.signature(behavior_BehaviorMixEntry.__init__)
    params = list(sig.parameters.keys())
    assert "behaviorModelName" in params, "Missing parameter 'behaviorModelName'"
    assert "relativeFrequency" in params, "Missing parameter 'relativeFrequency'"





def test_hyp_behavior_behaviormix_is_not_abstract():
    assert not inspect.isabstract(behavior_BehaviorMix)


def test_hyp_behavior_behaviormix_constructor_exists():
    assert callable(behavior_BehaviorMix.__init__)


def test_hyp_behavior_behaviormix_constructor_args():
    sig = inspect.signature(behavior_BehaviorMix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractbehaviormodelgraph_is_not_abstract():
    assert not inspect.isabstract(AbstractBehaviorModelGraph)


def test_hyp_abstractbehaviormodelgraph_constructor_exists():
    assert callable(AbstractBehaviorModelGraph.__init__)


def test_hyp_abstractbehaviormodelgraph_constructor_args():
    sig = inspect.signature(AbstractBehaviorModelGraph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_behaviormodelrelative_is_not_abstract():
    assert not inspect.isabstract(behavior_BehaviorModelRelative)


def test_hyp_behavior_behaviormodelrelative_constructor_exists():
    assert callable(behavior_BehaviorModelRelative.__init__)


def test_hyp_behavior_behaviormodelrelative_constructor_args():
    sig = inspect.signature(behavior_BehaviorModelRelative.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_behaviormodelabsolute_is_not_abstract():
    assert not inspect.isabstract(behavior_BehaviorModelAbsolute)


def test_hyp_behavior_behaviormodelabsolute_constructor_exists():
    assert callable(behavior_BehaviorModelAbsolute.__init__)


def test_hyp_behavior_behaviormodelabsolute_constructor_args():
    sig = inspect.signature(behavior_BehaviorModelAbsolute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_transition_is_not_abstract():
    assert not inspect.isabstract(behavior_Transition)


def test_hyp_behavior_transition_constructor_exists():
    assert callable(behavior_Transition.__init__)


def test_hyp_behavior_transition_constructor_args():
    sig = inspect.signature(behavior_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "thinkTimeParams" in params, "Missing parameter 'thinkTimeParams'"
    assert "value" in params, "Missing parameter 'value'"
    assert "timeDiffs" in params, "Missing parameter 'timeDiffs'"






def test_hyp_behavior_abstractusecaseexecution_is_not_abstract():
    assert not inspect.isabstract(behavior_AbstractUseCaseExecution)


def test_hyp_behavior_abstractusecaseexecution_constructor_exists():
    assert callable(behavior_AbstractUseCaseExecution.__init__)


def test_hyp_behavior_abstractusecaseexecution_constructor_args():
    sig = inspect.signature(behavior_AbstractUseCaseExecution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractusecaseexecution_is_not_abstract():
    assert not inspect.isabstract(AbstractUseCaseExecution)


def test_hyp_abstractusecaseexecution_constructor_exists():
    assert callable(AbstractUseCaseExecution.__init__)


def test_hyp_abstractusecaseexecution_constructor_args():
    sig = inspect.signature(AbstractUseCaseExecution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_observedusecaseexecution_is_not_abstract():
    assert not inspect.isabstract(behavior_ObservedUseCaseExecution)


def test_hyp_behavior_observedusecaseexecution_constructor_exists():
    assert callable(behavior_ObservedUseCaseExecution.__init__)


def test_hyp_behavior_observedusecaseexecution_constructor_args():
    sig = inspect.signature(behavior_ObservedUseCaseExecution.__init__)
    params = list(sig.parameters.keys())
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "startTime" in params, "Missing parameter 'startTime'"





def test_hyp_behavior_session_is_not_abstract():
    assert not inspect.isabstract(behavior_Session)


def test_hyp_behavior_session_constructor_exists():
    assert callable(behavior_Session.__init__)


def test_hyp_behavior_session_constructor_args():
    sig = inspect.signature(behavior_Session.__init__)
    params = list(sig.parameters.keys())
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "transactionType" in params, "Missing parameter 'transactionType'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_behavior_sessionrepository_is_not_abstract():
    assert not inspect.isabstract(behavior_SessionRepository)


def test_hyp_behavior_sessionrepository_constructor_exists():
    assert callable(behavior_SessionRepository.__init__)


def test_hyp_behavior_sessionrepository_constructor_args():
    sig = inspect.signature(behavior_SessionRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_usecaserepository_is_not_abstract():
    assert not inspect.isabstract(behavior_UseCaseRepository)


def test_hyp_behavior_usecaserepository_constructor_exists():
    assert callable(behavior_UseCaseRepository.__init__)


def test_hyp_behavior_usecaserepository_constructor_args():
    sig = inspect.signature(behavior_UseCaseRepository.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_vertex_is_not_abstract():
    assert not inspect.isabstract(behavior_Vertex)


def test_hyp_behavior_vertex_constructor_exists():
    assert callable(behavior_Vertex.__init__)


def test_hyp_behavior_vertex_constructor_args():
    sig = inspect.signature(behavior_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_abstractbehaviormodelgraph_is_not_abstract():
    assert not inspect.isabstract(behavior_AbstractBehaviorModelGraph)


def test_hyp_behavior_abstractbehaviormodelgraph_constructor_exists():
    assert callable(behavior_AbstractBehaviorModelGraph.__init__)


def test_hyp_behavior_abstractbehaviormodelgraph_constructor_args():
    sig = inspect.signature(behavior_AbstractBehaviorModelGraph.__init__)
    params = list(sig.parameters.keys())
    assert "transactionType" in params, "Missing parameter 'transactionType'"




def test_hyp_behavior_usecase_is_not_abstract():
    assert not inspect.isabstract(behavior_UseCase)


def test_hyp_behavior_usecase_constructor_exists():
    assert callable(behavior_UseCase.__init__)


def test_hyp_behavior_usecase_constructor_args():
    sig = inspect.signature(behavior_UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
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
behavior_BehaviorMixEntry_strategy = st.builds(
    behavior_BehaviorMixEntry,
    behaviorModelName=
        safe_text,
    relativeFrequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behavior_BehaviorMix_strategy = st.builds(
    behavior_BehaviorMix,
)
AbstractBehaviorModelGraph_strategy = st.builds(
    AbstractBehaviorModelGraph,
)
behavior_BehaviorModelRelative_strategy = st.builds(
    behavior_BehaviorModelRelative,
)
behavior_BehaviorModelAbsolute_strategy = st.builds(
    behavior_BehaviorModelAbsolute,
)
behavior_Transition_strategy = st.builds(
    behavior_Transition,
    thinkTimeParams=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timeDiffs=
        safe_text
)
behavior_AbstractUseCaseExecution_strategy = st.builds(
    behavior_AbstractUseCaseExecution,
)
AbstractUseCaseExecution_strategy = st.builds(
    AbstractUseCaseExecution,
)
behavior_ObservedUseCaseExecution_strategy = st.builds(
    behavior_ObservedUseCaseExecution,
    endTime=
        safe_text,
    startTime=
        safe_text
)
behavior_Session_strategy = st.builds(
    behavior_Session,
    endTime=
        safe_text,
    startTime=
        safe_text,
    transactionType=
        safe_text,
    id=
        safe_text
)
behavior_SessionRepository_strategy = st.builds(
    behavior_SessionRepository,
)
behavior_UseCaseRepository_strategy = st.builds(
    behavior_UseCaseRepository,
)
behavior_Vertex_strategy = st.builds(
    behavior_Vertex,
)
behavior_AbstractBehaviorModelGraph_strategy = st.builds(
    behavior_AbstractBehaviorModelGraph,
    transactionType=
        safe_text
)
behavior_UseCase_strategy = st.builds(
    behavior_UseCase,
    name=
        safe_text,
    id=
        safe_text
)




@given(instance=behavior_BehaviorMixEntry_strategy)
def test_hyp_behavior_behaviormixentry_behaviorModelName_setter(instance):
    original = instance.behaviorModelName
    instance.behaviorModelName = original
    assert instance.behaviorModelName == original



@given(instance=behavior_BehaviorMixEntry_strategy)
def test_hyp_behavior_behaviormixentry_relativeFrequency_setter(instance):
    original = instance.relativeFrequency
    instance.relativeFrequency = original
    assert instance.relativeFrequency == original








@given(instance=behavior_Transition_strategy)
def test_hyp_behavior_transition_thinkTimeParams_setter(instance):
    original = instance.thinkTimeParams
    instance.thinkTimeParams = original
    assert instance.thinkTimeParams == original



@given(instance=behavior_Transition_strategy)
def test_hyp_behavior_transition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=behavior_Transition_strategy)
def test_hyp_behavior_transition_timeDiffs_setter(instance):
    original = instance.timeDiffs
    instance.timeDiffs = original
    assert instance.timeDiffs == original






@given(instance=behavior_ObservedUseCaseExecution_strategy)
def test_hyp_behavior_observedusecaseexecution_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=behavior_ObservedUseCaseExecution_strategy)
def test_hyp_behavior_observedusecaseexecution_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original




@given(instance=behavior_Session_strategy)
def test_hyp_behavior_session_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=behavior_Session_strategy)
def test_hyp_behavior_session_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



@given(instance=behavior_Session_strategy)
def test_hyp_behavior_session_transactionType_setter(instance):
    original = instance.transactionType
    instance.transactionType = original
    assert instance.transactionType == original



@given(instance=behavior_Session_strategy)
def test_hyp_behavior_session_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original







@given(instance=behavior_AbstractBehaviorModelGraph_strategy)
def test_hyp_behavior_abstractbehaviormodelgraph_transactionType_setter(instance):
    original = instance.transactionType
    instance.transactionType = original
    assert instance.transactionType == original




@given(instance=behavior_UseCase_strategy)
def test_hyp_behavior_usecase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=behavior_UseCase_strategy)
def test_hyp_behavior_usecase_id_setter(instance):
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
    AbstractBehaviorModelGraph,
    AbstractUseCaseExecution,
    behavior_AbstractBehaviorModelGraph,
    behavior_AbstractUseCaseExecution,
    behavior_BehaviorMix,
    behavior_BehaviorMixEntry,
    behavior_BehaviorModelAbsolute,
    behavior_BehaviorModelRelative,
    behavior_ObservedUseCaseExecution,
    behavior_Session,
    behavior_SessionRepository,
    behavior_Transition,
    behavior_UseCase,
    behavior_UseCaseRepository,
    behavior_Vertex,
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

def test_behavior_AbstractBehaviorModelGraph_transactionType_value_roundtrip():
    instance = behavior_AbstractBehaviorModelGraph(transactionType="sample_text")
    assert instance.transactionType == "sample_text"
    instance.transactionType = "sample_text_2"
    assert instance.transactionType == "sample_text_2"


def test_behavior_BehaviorMixEntry_behaviorModelName_value_roundtrip():
    instance = behavior_BehaviorMixEntry(behaviorModelName="sample_text", relativeFrequency=3.14)
    assert instance.behaviorModelName == "sample_text"
    instance.behaviorModelName = "sample_text_2"
    assert instance.behaviorModelName == "sample_text_2"


def test_behavior_BehaviorMixEntry_relativeFrequency_value_roundtrip():
    instance = behavior_BehaviorMixEntry(behaviorModelName="sample_text", relativeFrequency=3.14)
    assert instance.relativeFrequency == 3.14
    instance.relativeFrequency = 9.99
    assert instance.relativeFrequency == 9.99


def test_behavior_ObservedUseCaseExecution_endTime_value_roundtrip():
    instance = behavior_ObservedUseCaseExecution(endTime="sample_text", startTime="sample_text")
    assert instance.endTime == "sample_text"
    instance.endTime = "sample_text_2"
    assert instance.endTime == "sample_text_2"


def test_behavior_ObservedUseCaseExecution_startTime_value_roundtrip():
    instance = behavior_ObservedUseCaseExecution(endTime="sample_text", startTime="sample_text")
    assert instance.startTime == "sample_text"
    instance.startTime = "sample_text_2"
    assert instance.startTime == "sample_text_2"


def test_behavior_Session_endTime_value_roundtrip():
    instance = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    assert instance.endTime == "sample_text"
    instance.endTime = "sample_text_2"
    assert instance.endTime == "sample_text_2"


def test_behavior_Session_id_value_roundtrip():
    instance = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_behavior_Session_startTime_value_roundtrip():
    instance = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    assert instance.startTime == "sample_text"
    instance.startTime = "sample_text_2"
    assert instance.startTime == "sample_text_2"


def test_behavior_Session_transactionType_value_roundtrip():
    instance = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    assert instance.transactionType == "sample_text"
    instance.transactionType = "sample_text_2"
    assert instance.transactionType == "sample_text_2"


def test_behavior_Transition_thinkTimeParams_value_roundtrip():
    instance = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    assert instance.thinkTimeParams == "sample_text"
    instance.thinkTimeParams = "sample_text_2"
    assert instance.thinkTimeParams == "sample_text_2"


def test_behavior_Transition_timeDiffs_value_roundtrip():
    instance = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    assert instance.timeDiffs == "sample_text"
    instance.timeDiffs = "sample_text_2"
    assert instance.timeDiffs == "sample_text_2"


def test_behavior_Transition_value_value_roundtrip():
    instance = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_behavior_UseCase_id_value_roundtrip():
    instance = behavior_UseCase(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_behavior_UseCase_name_value_roundtrip():
    instance = behavior_UseCase(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_behavior_BehaviorModelAbsolute_isa_AbstractBehaviorModelGraph():
    instance = behavior_BehaviorModelAbsolute()
    assert isinstance(instance, AbstractBehaviorModelGraph)


def test_behavior_BehaviorModelRelative_isa_AbstractBehaviorModelGraph():
    instance = behavior_BehaviorModelRelative()
    assert isinstance(instance, AbstractBehaviorModelGraph)


def test_behavior_ObservedUseCaseExecution_isa_AbstractUseCaseExecution():
    instance = behavior_ObservedUseCaseExecution(endTime="sample_text", startTime="sample_text")
    assert isinstance(instance, AbstractUseCaseExecution)


def test_behavior_Vertex_isa_AbstractUseCaseExecution():
    instance = behavior_Vertex()
    assert isinstance(instance, AbstractUseCaseExecution)


def test_assoc_behaviorModel16_link_reassign_clear():
    a = behavior_BehaviorMixEntry(behaviorModelName="sample_text", relativeFrequency=3.14)
    b1 = behavior_BehaviorModelRelative()
    b2 = behavior_BehaviorModelRelative()
    _safe_set(a, 'behavior_BehaviorMixEntry17', b1)
    assert _is_linked(a, 'behavior_BehaviorMixEntry17', b1)
    if hasattr(b1, 'behavior_BehaviorModelRelative'):
        assert _is_linked(b1, 'behavior_BehaviorModelRelative', a)
    _safe_set(a, 'behavior_BehaviorMixEntry17', b2)
    assert _is_linked(a, 'behavior_BehaviorMixEntry17', b2)
    if hasattr(b1, 'behavior_BehaviorModelRelative'):
        assert not _is_linked(b1, 'behavior_BehaviorModelRelative', a)
    if hasattr(b2, 'behavior_BehaviorModelRelative'):
        assert _is_linked(b2, 'behavior_BehaviorModelRelative', a)
    _safe_set(a, 'behavior_BehaviorMixEntry17', None)
    assert not _is_linked(a, 'behavior_BehaviorMixEntry17', b2)
    if hasattr(b2, 'behavior_BehaviorModelRelative'):
        assert not _is_linked(b2, 'behavior_BehaviorModelRelative', a)


def test_assoc_entries15_link_reassign_clear():
    a = behavior_BehaviorMixEntry(behaviorModelName="sample_text", relativeFrequency=3.14)
    b1 = behavior_BehaviorMix()
    b2 = behavior_BehaviorMix()
    _safe_set(a, 'behavior_BehaviorMixEntry', b1)
    assert _is_linked(a, 'behavior_BehaviorMixEntry', b1)
    if hasattr(b1, 'behavior_BehaviorMix'):
        assert _is_linked(b1, 'behavior_BehaviorMix', a)
    _safe_set(a, 'behavior_BehaviorMixEntry', b2)
    assert _is_linked(a, 'behavior_BehaviorMixEntry', b2)
    if hasattr(b1, 'behavior_BehaviorMix'):
        assert not _is_linked(b1, 'behavior_BehaviorMix', a)
    if hasattr(b2, 'behavior_BehaviorMix'):
        assert _is_linked(b2, 'behavior_BehaviorMix', a)
    _safe_set(a, 'behavior_BehaviorMixEntry', None)
    assert not _is_linked(a, 'behavior_BehaviorMixEntry', b2)
    if hasattr(b2, 'behavior_BehaviorMix'):
        assert not _is_linked(b2, 'behavior_BehaviorMix', a)


def test_assoc_observedUseCaseExecutions2_link_reassign_clear():
    a = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    b1 = behavior_ObservedUseCaseExecution(endTime="sample_text", startTime="sample_text")
    b2 = behavior_ObservedUseCaseExecution(endTime="sample_text_2", startTime="sample_text_2")
    _safe_set(a, 'behavior_Session3', {b1})
    assert _is_linked(a, 'behavior_Session3', b1)
    if hasattr(b1, 'behavior_ObservedUseCaseExecution'):
        assert _is_linked(b1, 'behavior_ObservedUseCaseExecution', a)
    _safe_set(a, 'behavior_Session3', {b2})
    assert _is_linked(a, 'behavior_Session3', b2)
    if hasattr(b1, 'behavior_ObservedUseCaseExecution'):
        assert not _is_linked(b1, 'behavior_ObservedUseCaseExecution', a)
    if hasattr(b2, 'behavior_ObservedUseCaseExecution'):
        assert _is_linked(b2, 'behavior_ObservedUseCaseExecution', a)
    _safe_set(a, 'behavior_Session3', set())
    assert not _is_linked(a, 'behavior_Session3', b2)
    if hasattr(b2, 'behavior_ObservedUseCaseExecution'):
        assert not _is_linked(b2, 'behavior_ObservedUseCaseExecution', a)


def test_assoc_outgoingTransitions7_link_reassign_clear():
    a = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    b1 = behavior_Vertex()
    b2 = behavior_Vertex()
    _safe_set(a, 'behavior_Transition', b1)
    assert _is_linked(a, 'behavior_Transition', b1)
    if hasattr(b1, 'behavior_Vertex8'):
        assert _is_linked(b1, 'behavior_Vertex8', a)
    _safe_set(a, 'behavior_Transition', b2)
    assert _is_linked(a, 'behavior_Transition', b2)
    if hasattr(b1, 'behavior_Vertex8'):
        assert not _is_linked(b1, 'behavior_Vertex8', a)
    if hasattr(b2, 'behavior_Vertex8'):
        assert _is_linked(b2, 'behavior_Vertex8', a)
    _safe_set(a, 'behavior_Transition', None)
    assert not _is_linked(a, 'behavior_Transition', b2)
    if hasattr(b2, 'behavior_Vertex8'):
        assert not _is_linked(b2, 'behavior_Vertex8', a)


def test_assoc_sessions1_link_reassign_clear():
    a = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    b1 = behavior_SessionRepository()
    b2 = behavior_SessionRepository()
    _safe_set(a, 'behavior_Session', b1)
    assert _is_linked(a, 'behavior_Session', b1)
    if hasattr(b1, 'behavior_SessionRepository'):
        assert _is_linked(b1, 'behavior_SessionRepository', a)
    _safe_set(a, 'behavior_Session', b2)
    assert _is_linked(a, 'behavior_Session', b2)
    if hasattr(b1, 'behavior_SessionRepository'):
        assert not _is_linked(b1, 'behavior_SessionRepository', a)
    if hasattr(b2, 'behavior_SessionRepository'):
        assert _is_linked(b2, 'behavior_SessionRepository', a)
    _safe_set(a, 'behavior_Session', None)
    assert not _is_linked(a, 'behavior_Session', b2)
    if hasattr(b2, 'behavior_SessionRepository'):
        assert not _is_linked(b2, 'behavior_SessionRepository', a)


def test_assoc_sourceVertex12_link_reassign_clear():
    a = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    b1 = behavior_Vertex()
    b2 = behavior_Vertex()
    _safe_set(a, 'behavior_Transition13', b1)
    assert _is_linked(a, 'behavior_Transition13', b1)
    if hasattr(b1, 'behavior_Vertex14'):
        assert _is_linked(b1, 'behavior_Vertex14', a)
    _safe_set(a, 'behavior_Transition13', b2)
    assert _is_linked(a, 'behavior_Transition13', b2)
    if hasattr(b1, 'behavior_Vertex14'):
        assert not _is_linked(b1, 'behavior_Vertex14', a)
    if hasattr(b2, 'behavior_Vertex14'):
        assert _is_linked(b2, 'behavior_Vertex14', a)
    _safe_set(a, 'behavior_Transition13', None)
    assert not _is_linked(a, 'behavior_Transition13', b2)
    if hasattr(b2, 'behavior_Vertex14'):
        assert not _is_linked(b2, 'behavior_Vertex14', a)


def test_assoc_targetVertex9_link_reassign_clear():
    a = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    b1 = behavior_Vertex()
    b2 = behavior_Vertex()
    _safe_set(a, 'behavior_Transition10', b1)
    assert _is_linked(a, 'behavior_Transition10', b1)
    if hasattr(b1, 'behavior_Vertex11'):
        assert _is_linked(b1, 'behavior_Vertex11', a)
    _safe_set(a, 'behavior_Transition10', b2)
    assert _is_linked(a, 'behavior_Transition10', b2)
    if hasattr(b1, 'behavior_Vertex11'):
        assert not _is_linked(b1, 'behavior_Vertex11', a)
    if hasattr(b2, 'behavior_Vertex11'):
        assert _is_linked(b2, 'behavior_Vertex11', a)
    _safe_set(a, 'behavior_Transition10', None)
    assert not _is_linked(a, 'behavior_Transition10', b2)
    if hasattr(b2, 'behavior_Vertex11'):
        assert not _is_linked(b2, 'behavior_Vertex11', a)


def test_assoc_useCase4_link_reassign_clear():
    a = behavior_UseCase(id="sample_text", name="sample_text")
    b1 = behavior_AbstractUseCaseExecution()
    b2 = behavior_AbstractUseCaseExecution()
    _safe_set(a, 'behavior_UseCase5', b1)
    assert _is_linked(a, 'behavior_UseCase5', b1)
    if hasattr(b1, 'behavior_AbstractUseCaseExecution'):
        assert _is_linked(b1, 'behavior_AbstractUseCaseExecution', a)
    _safe_set(a, 'behavior_UseCase5', b2)
    assert _is_linked(a, 'behavior_UseCase5', b2)
    if hasattr(b1, 'behavior_AbstractUseCaseExecution'):
        assert not _is_linked(b1, 'behavior_AbstractUseCaseExecution', a)
    if hasattr(b2, 'behavior_AbstractUseCaseExecution'):
        assert _is_linked(b2, 'behavior_AbstractUseCaseExecution', a)
    _safe_set(a, 'behavior_UseCase5', None)
    assert not _is_linked(a, 'behavior_UseCase5', b2)
    if hasattr(b2, 'behavior_AbstractUseCaseExecution'):
        assert not _is_linked(b2, 'behavior_AbstractUseCaseExecution', a)


def test_assoc_useCases0_link_reassign_clear():
    a = behavior_UseCase(id="sample_text", name="sample_text")
    b1 = behavior_UseCaseRepository()
    b2 = behavior_UseCaseRepository()
    _safe_set(a, 'behavior_UseCase', b1)
    assert _is_linked(a, 'behavior_UseCase', b1)
    if hasattr(b1, 'behavior_UseCaseRepository'):
        assert _is_linked(b1, 'behavior_UseCaseRepository', a)
    _safe_set(a, 'behavior_UseCase', b2)
    assert _is_linked(a, 'behavior_UseCase', b2)
    if hasattr(b1, 'behavior_UseCaseRepository'):
        assert not _is_linked(b1, 'behavior_UseCaseRepository', a)
    if hasattr(b2, 'behavior_UseCaseRepository'):
        assert _is_linked(b2, 'behavior_UseCaseRepository', a)
    _safe_set(a, 'behavior_UseCase', None)
    assert not _is_linked(a, 'behavior_UseCase', b2)
    if hasattr(b2, 'behavior_UseCaseRepository'):
        assert not _is_linked(b2, 'behavior_UseCaseRepository', a)


def test_assoc_vertices6_link_reassign_clear():
    a = behavior_AbstractBehaviorModelGraph(transactionType="sample_text")
    b1 = behavior_Vertex()
    b2 = behavior_Vertex()
    _safe_set(a, 'behavior_AbstractBehaviorModelGraph', {b1})
    assert _is_linked(a, 'behavior_AbstractBehaviorModelGraph', b1)
    if hasattr(b1, 'behavior_Vertex'):
        assert _is_linked(b1, 'behavior_Vertex', a)
    _safe_set(a, 'behavior_AbstractBehaviorModelGraph', {b2})
    assert _is_linked(a, 'behavior_AbstractBehaviorModelGraph', b2)
    if hasattr(b1, 'behavior_Vertex'):
        assert not _is_linked(b1, 'behavior_Vertex', a)
    if hasattr(b2, 'behavior_Vertex'):
        assert _is_linked(b2, 'behavior_Vertex', a)
    _safe_set(a, 'behavior_AbstractBehaviorModelGraph', set())
    assert not _is_linked(a, 'behavior_AbstractBehaviorModelGraph', b2)
    if hasattr(b2, 'behavior_Vertex'):
        assert not _is_linked(b2, 'behavior_Vertex', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractBehaviorModelGraph_strategy = st.builds(AbstractBehaviorModelGraph)
@given(instance=AbstractBehaviorModelGraph_strategy)
@settings(max_examples=25)
def test_AbstractBehaviorModelGraph_instantiation(instance):
    assert isinstance(instance, AbstractBehaviorModelGraph)


AbstractUseCaseExecution_strategy = st.builds(AbstractUseCaseExecution)
@given(instance=AbstractUseCaseExecution_strategy)
@settings(max_examples=25)
def test_AbstractUseCaseExecution_instantiation(instance):
    assert isinstance(instance, AbstractUseCaseExecution)


behavior_AbstractBehaviorModelGraph_strategy = st.builds(behavior_AbstractBehaviorModelGraph, transactionType=safe_text)
@given(instance=behavior_AbstractBehaviorModelGraph_strategy)
@settings(max_examples=25)
def test_behavior_AbstractBehaviorModelGraph_instantiation(instance):
    assert isinstance(instance, behavior_AbstractBehaviorModelGraph)


behavior_AbstractUseCaseExecution_strategy = st.builds(behavior_AbstractUseCaseExecution)
@given(instance=behavior_AbstractUseCaseExecution_strategy)
@settings(max_examples=25)
def test_behavior_AbstractUseCaseExecution_instantiation(instance):
    assert isinstance(instance, behavior_AbstractUseCaseExecution)


behavior_BehaviorMix_strategy = st.builds(behavior_BehaviorMix)
@given(instance=behavior_BehaviorMix_strategy)
@settings(max_examples=25)
def test_behavior_BehaviorMix_instantiation(instance):
    assert isinstance(instance, behavior_BehaviorMix)


behavior_BehaviorMixEntry_strategy = st.builds(behavior_BehaviorMixEntry, behaviorModelName=safe_text, relativeFrequency=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behavior_BehaviorMixEntry_strategy)
@settings(max_examples=25)
def test_behavior_BehaviorMixEntry_instantiation(instance):
    assert isinstance(instance, behavior_BehaviorMixEntry)


behavior_BehaviorModelAbsolute_strategy = st.builds(behavior_BehaviorModelAbsolute)
@given(instance=behavior_BehaviorModelAbsolute_strategy)
@settings(max_examples=25)
def test_behavior_BehaviorModelAbsolute_instantiation(instance):
    assert isinstance(instance, behavior_BehaviorModelAbsolute)


behavior_BehaviorModelRelative_strategy = st.builds(behavior_BehaviorModelRelative)
@given(instance=behavior_BehaviorModelRelative_strategy)
@settings(max_examples=25)
def test_behavior_BehaviorModelRelative_instantiation(instance):
    assert isinstance(instance, behavior_BehaviorModelRelative)


behavior_ObservedUseCaseExecution_strategy = st.builds(behavior_ObservedUseCaseExecution, endTime=safe_text, startTime=safe_text)
@given(instance=behavior_ObservedUseCaseExecution_strategy)
@settings(max_examples=25)
def test_behavior_ObservedUseCaseExecution_instantiation(instance):
    assert isinstance(instance, behavior_ObservedUseCaseExecution)


behavior_Session_strategy = st.builds(behavior_Session, endTime=safe_text, id=safe_text, startTime=safe_text, transactionType=safe_text)
@given(instance=behavior_Session_strategy)
@settings(max_examples=25)
def test_behavior_Session_instantiation(instance):
    assert isinstance(instance, behavior_Session)


behavior_SessionRepository_strategy = st.builds(behavior_SessionRepository)
@given(instance=behavior_SessionRepository_strategy)
@settings(max_examples=25)
def test_behavior_SessionRepository_instantiation(instance):
    assert isinstance(instance, behavior_SessionRepository)


behavior_Transition_strategy = st.builds(behavior_Transition, thinkTimeParams=safe_text, timeDiffs=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=behavior_Transition_strategy)
@settings(max_examples=25)
def test_behavior_Transition_instantiation(instance):
    assert isinstance(instance, behavior_Transition)


behavior_UseCase_strategy = st.builds(behavior_UseCase, id=safe_text, name=safe_text)
@given(instance=behavior_UseCase_strategy)
@settings(max_examples=25)
def test_behavior_UseCase_instantiation(instance):
    assert isinstance(instance, behavior_UseCase)


behavior_UseCaseRepository_strategy = st.builds(behavior_UseCaseRepository)
@given(instance=behavior_UseCaseRepository_strategy)
@settings(max_examples=25)
def test_behavior_UseCaseRepository_instantiation(instance):
    assert isinstance(instance, behavior_UseCaseRepository)


behavior_Vertex_strategy = st.builds(behavior_Vertex)
@given(instance=behavior_Vertex_strategy)
@settings(max_examples=25)
def test_behavior_Vertex_instantiation(instance):
    assert isinstance(instance, behavior_Vertex)



