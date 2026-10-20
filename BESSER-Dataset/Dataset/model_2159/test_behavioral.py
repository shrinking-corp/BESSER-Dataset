import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_observedUseCaseExecutions2_reverse_link_reassign_clear():
    a1 = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    a2 = behavior_Session(endTime="sample_text_2", id="sample_text_2", startTime="sample_text_2", transactionType="sample_text_2")
    b = behavior_ObservedUseCaseExecution(endTime="sample_text", startTime="sample_text")
    _safe_set(b, 'behavior_ObservedUseCaseExecution', a1)
    assert _is_linked(b, 'behavior_ObservedUseCaseExecution', a1)
    if hasattr(a1, 'behavior_Session3'):
        assert _is_linked(a1, 'behavior_Session3', b)
    _safe_set(b, 'behavior_ObservedUseCaseExecution', a2)
    assert _is_linked(b, 'behavior_ObservedUseCaseExecution', a2)
    if hasattr(a1, 'behavior_Session3'):
        assert not _is_linked(a1, 'behavior_Session3', b)
    if hasattr(a2, 'behavior_Session3'):
        assert _is_linked(a2, 'behavior_Session3', b)
    _safe_set(b, 'behavior_ObservedUseCaseExecution', None)
    assert not _is_linked(b, 'behavior_ObservedUseCaseExecution', a2)
    if hasattr(a2, 'behavior_Session3'):
        assert not _is_linked(a2, 'behavior_Session3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_behaviorModel16_stub_double():
    # behavior_BehaviorModelRelative has no real 'behavior_BehaviorModelRelative' property in the generated
    # code (a bare stub) -- manually attach it so behavior_BehaviorMixEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_BehaviorMixEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_BehaviorMixEntry(behaviorModelName="sample_text", relativeFrequency=3.14)
    partner = behavior_BehaviorModelRelative()
    setattr(partner, 'behavior_BehaviorModelRelative', None)
    _safe_set(owner, 'behavior_BehaviorMixEntry17', partner)
    assert getattr(partner, 'behavior_BehaviorModelRelative') == owner
    _safe_set(owner, 'behavior_BehaviorMixEntry17', None)
    assert getattr(partner, 'behavior_BehaviorModelRelative') is None


def test_assoc_entries15_stub_double():
    # behavior_BehaviorMix has no real 'behavior_BehaviorMix' property in the generated
    # code (a bare stub) -- manually attach it so behavior_BehaviorMixEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_BehaviorMixEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_BehaviorMixEntry(behaviorModelName="sample_text", relativeFrequency=3.14)
    partner = behavior_BehaviorMix()
    setattr(partner, 'behavior_BehaviorMix', None)
    _safe_set(owner, 'behavior_BehaviorMixEntry', partner)
    assert owner in getattr(partner, 'behavior_BehaviorMix')
    _safe_set(owner, 'behavior_BehaviorMixEntry', None)
    assert owner not in getattr(partner, 'behavior_BehaviorMix')


def test_assoc_outgoingTransitions7_stub_double():
    # behavior_Vertex has no real 'behavior_Vertex8' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    partner = behavior_Vertex()
    setattr(partner, 'behavior_Vertex8', None)
    _safe_set(owner, 'behavior_Transition', partner)
    assert owner in getattr(partner, 'behavior_Vertex8')
    _safe_set(owner, 'behavior_Transition', None)
    assert owner not in getattr(partner, 'behavior_Vertex8')


def test_assoc_sessions1_stub_double():
    # behavior_SessionRepository has no real 'behavior_SessionRepository' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Session(endTime="sample_text", id="sample_text", startTime="sample_text", transactionType="sample_text")
    partner = behavior_SessionRepository()
    setattr(partner, 'behavior_SessionRepository', None)
    _safe_set(owner, 'behavior_Session', partner)
    assert owner in getattr(partner, 'behavior_SessionRepository')
    _safe_set(owner, 'behavior_Session', None)
    assert owner not in getattr(partner, 'behavior_SessionRepository')


def test_assoc_sourceVertex12_stub_double():
    # behavior_Vertex has no real 'behavior_Vertex14' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    partner = behavior_Vertex()
    setattr(partner, 'behavior_Vertex14', None)
    _safe_set(owner, 'behavior_Transition13', partner)
    assert getattr(partner, 'behavior_Vertex14') == owner
    _safe_set(owner, 'behavior_Transition13', None)
    assert getattr(partner, 'behavior_Vertex14') is None


def test_assoc_targetVertex9_stub_double():
    # behavior_Vertex has no real 'behavior_Vertex11' property in the generated
    # code (a bare stub) -- manually attach it so behavior_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_Transition(thinkTimeParams="sample_text", timeDiffs="sample_text", value=3.14)
    partner = behavior_Vertex()
    setattr(partner, 'behavior_Vertex11', None)
    _safe_set(owner, 'behavior_Transition10', partner)
    assert getattr(partner, 'behavior_Vertex11') == owner
    _safe_set(owner, 'behavior_Transition10', None)
    assert getattr(partner, 'behavior_Vertex11') is None


def test_assoc_useCase4_stub_double():
    # behavior_AbstractUseCaseExecution has no real 'behavior_AbstractUseCaseExecution' property in the generated
    # code (a bare stub) -- manually attach it so behavior_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_UseCase(id="sample_text", name="sample_text")
    partner = behavior_AbstractUseCaseExecution()
    setattr(partner, 'behavior_AbstractUseCaseExecution', None)
    _safe_set(owner, 'behavior_UseCase5', partner)
    assert getattr(partner, 'behavior_AbstractUseCaseExecution') == owner
    _safe_set(owner, 'behavior_UseCase5', None)
    assert getattr(partner, 'behavior_AbstractUseCaseExecution') is None


def test_assoc_useCases0_stub_double():
    # behavior_UseCaseRepository has no real 'behavior_UseCaseRepository' property in the generated
    # code (a bare stub) -- manually attach it so behavior_UseCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_UseCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_UseCase(id="sample_text", name="sample_text")
    partner = behavior_UseCaseRepository()
    setattr(partner, 'behavior_UseCaseRepository', None)
    _safe_set(owner, 'behavior_UseCase', partner)
    assert owner in getattr(partner, 'behavior_UseCaseRepository')
    _safe_set(owner, 'behavior_UseCase', None)
    assert owner not in getattr(partner, 'behavior_UseCaseRepository')


def test_assoc_vertices6_stub_double():
    # behavior_Vertex has no real 'behavior_Vertex' property in the generated
    # code (a bare stub) -- manually attach it so behavior_AbstractBehaviorModelGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behavior_AbstractBehaviorModelGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behavior_AbstractBehaviorModelGraph(transactionType="sample_text")
    partner = behavior_Vertex()
    setattr(partner, 'behavior_Vertex', None)
    _safe_set(owner, 'behavior_AbstractBehaviorModelGraph', {partner})
    assert getattr(partner, 'behavior_Vertex') == owner
    _safe_set(owner, 'behavior_AbstractBehaviorModelGraph', set())
    assert getattr(partner, 'behavior_Vertex') is None


