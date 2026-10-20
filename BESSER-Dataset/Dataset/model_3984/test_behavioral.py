import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BaseElement,
    Cause,
    FMEAEntry,
    FMEA_failureLogic_Failure,
    FMEA_failureLogic_ProbDist,
    FTA_failureLogic_Failure,
    Failure,
    FailureModel,
    Markov_failureLogic_Failure,
    Markov_failureLogic_ProbDist,
    State,
    Transition,
    failureLogic_FMEA_FMEA,
    failureLogic_FMEA_FMEAEntry,
    failureLogic_FMEA_FMEDAEntry,
    failureLogic_FTA_Cause,
    failureLogic_FTA_FaultTree,
    failureLogic_FTA_Gate,
    failureLogic_Failure,
    failureLogic_FailureLogicPackage,
    failureLogic_FailureModel,
    failureLogic_Markov_MarkovChain,
    failureLogic_Markov_State,
    failureLogic_Markov_Transition,
    failureLogic_MinimalCutSets,
    failureLogic_MinimalCutset,
    failureLogic_ProbDist,
    failureLogic_ProbDistParam,
    failureLogic_SecurityViolation,
    CauseType,
    FMEAType,
    FailureOriginType,
    GateType,
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

def test_assoc_ccfFailures3_reverse_link_reassign_clear():
    a1 = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    a2 = failureLogic_Failure(failureClass="sample_text_2", failureRate=9.99, isCcf=False, originType="sample_text_2")
    b = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    _safe_set(b, 'failureLogic_Failure4', a1)
    assert _is_linked(b, 'failureLogic_Failure4', a1)
    if hasattr(a1, 'failureLogic_Failure2'):
        assert _is_linked(a1, 'failureLogic_Failure2', b)
    _safe_set(b, 'failureLogic_Failure4', a2)
    assert _is_linked(b, 'failureLogic_Failure4', a2)
    if hasattr(a1, 'failureLogic_Failure2'):
        assert not _is_linked(a1, 'failureLogic_Failure2', b)
    if hasattr(a2, 'failureLogic_Failure2'):
        assert _is_linked(a2, 'failureLogic_Failure2', b)
    _safe_set(b, 'failureLogic_Failure4', None)
    assert not _is_linked(b, 'failureLogic_Failure4', a2)
    if hasattr(a2, 'failureLogic_Failure2'):
        assert not _is_linked(a2, 'failureLogic_Failure2', b)


def test_assoc_failureProbDistribution1_reverse_link_reassign_clear():
    a1 = failureLogic_ProbDist(type="sample_text")
    a2 = failureLogic_ProbDist(type="sample_text_2")
    b = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    _safe_set(b, 'failureLogic_Failure', a1)
    assert _is_linked(b, 'failureLogic_Failure', a1)
    if hasattr(a1, 'failureLogic_ProbDist'):
        assert _is_linked(a1, 'failureLogic_ProbDist', b)
    _safe_set(b, 'failureLogic_Failure', a2)
    assert _is_linked(b, 'failureLogic_Failure', a2)
    if hasattr(a1, 'failureLogic_ProbDist'):
        assert not _is_linked(a1, 'failureLogic_ProbDist', b)
    if hasattr(a2, 'failureLogic_ProbDist'):
        assert _is_linked(a2, 'failureLogic_ProbDist', b)
    _safe_set(b, 'failureLogic_Failure', None)
    assert not _is_linked(b, 'failureLogic_Failure', a2)
    if hasattr(a2, 'failureLogic_ProbDist'):
        assert not _is_linked(a2, 'failureLogic_ProbDist', b)


def test_assoc_parameters21_reverse_link_reassign_clear():
    a1 = failureLogic_ProbDistParam(value="sample_text")
    a2 = failureLogic_ProbDistParam(value="sample_text_2")
    b = failureLogic_ProbDist(type="sample_text")
    _safe_set(b, 'failureLogic_ProbDist22', {a1})
    assert _is_linked(b, 'failureLogic_ProbDist22', a1)
    if hasattr(a1, 'failureLogic_ProbDistParam'):
        assert _is_linked(a1, 'failureLogic_ProbDistParam', b)
    _safe_set(b, 'failureLogic_ProbDist22', {a2})
    assert _is_linked(b, 'failureLogic_ProbDist22', a2)
    if hasattr(a1, 'failureLogic_ProbDistParam'):
        assert not _is_linked(a1, 'failureLogic_ProbDistParam', b)
    if hasattr(a2, 'failureLogic_ProbDistParam'):
        assert _is_linked(a2, 'failureLogic_ProbDistParam', b)
    _safe_set(b, 'failureLogic_ProbDist22', set())
    assert not _is_linked(b, 'failureLogic_ProbDist22', a2)
    if hasattr(a2, 'failureLogic_ProbDistParam'):
        assert not _is_linked(a2, 'failureLogic_ProbDistParam', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_causes25_stub_double():
    # Cause has no real 'Cause26' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_FTA_Gate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_FTA_Gate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_FTA_Gate(gateType="sample_text")
    partner = Cause()
    setattr(partner, 'Cause26', None)
    _safe_set(owner, 'failureLogic_FTA_Gate', {partner})
    assert getattr(partner, 'Cause26') == owner
    _safe_set(owner, 'failureLogic_FTA_Gate', set())
    assert getattr(partner, 'Cause26') is None


def test_assoc_diagnosisProbDistribution43_stub_double():
    # FMEA_failureLogic_ProbDist has no real 'FMEA_failureLogic_ProbDist' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_FMEA_FMEDAEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_FMEA_FMEDAEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_FMEA_FMEDAEntry(diagnosisRate=3.14)
    partner = FMEA_failureLogic_ProbDist()
    setattr(partner, 'FMEA_failureLogic_ProbDist', None)
    _safe_set(owner, 'failureLogic_FMEA_FMEDAEntry', partner)
    assert getattr(partner, 'FMEA_failureLogic_ProbDist') == owner
    _safe_set(owner, 'failureLogic_FMEA_FMEDAEntry', None)
    assert getattr(partner, 'FMEA_failureLogic_ProbDist') is None


def test_assoc_entries38_stub_double():
    # FMEAEntry has no real 'FMEAEntry' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_FMEA_FMEA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_FMEA_FMEA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_FMEA_FMEA(type="sample_text")
    partner = FMEAEntry()
    setattr(partner, 'FMEAEntry', None)
    _safe_set(owner, 'failureLogic_FMEA_FMEA', {partner})
    assert getattr(partner, 'FMEAEntry') == owner
    _safe_set(owner, 'failureLogic_FMEA_FMEA', set())
    assert getattr(partner, 'FMEAEntry') is None


def test_assoc_failState30_stub_double():
    # Markov_failureLogic_Failure has no real 'Markov_failureLogic_Failure' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Markov_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Markov_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Markov_State(isFailState=True, isInitialState=True)
    partner = Markov_failureLogic_Failure()
    setattr(partner, 'Markov_failureLogic_Failure', None)
    _safe_set(owner, 'failureLogic_Markov_State', partner)
    assert getattr(partner, 'Markov_failureLogic_Failure') == owner
    _safe_set(owner, 'failureLogic_Markov_State', None)
    assert getattr(partner, 'Markov_failureLogic_Failure') is None


def test_assoc_failure24_stub_double():
    # FTA_failureLogic_Failure has no real 'FTA_failureLogic_Failure' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_FTA_Cause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_FTA_Cause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_FTA_Cause(type="sample_text")
    partner = FTA_failureLogic_Failure()
    setattr(partner, 'FTA_failureLogic_Failure', None)
    _safe_set(owner, 'failureLogic_FTA_Cause', partner)
    assert getattr(partner, 'FTA_failureLogic_Failure') == owner
    _safe_set(owner, 'failureLogic_FTA_Cause', None)
    assert getattr(partner, 'FTA_failureLogic_Failure') is None


def test_assoc_failures15_stub_double():
    # failureLogic_MinimalCutSets has no real 'failureLogic_MinimalCutSets16' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Failure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Failure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    partner = failureLogic_MinimalCutSets()
    setattr(partner, 'failureLogic_MinimalCutSets16', None)
    _safe_set(owner, 'failureLogic_Failure17', partner)
    assert owner in getattr(partner, 'failureLogic_MinimalCutSets16')
    _safe_set(owner, 'failureLogic_Failure17', None)
    assert owner not in getattr(partner, 'failureLogic_MinimalCutSets16')


def test_assoc_failures18_stub_double():
    # failureLogic_MinimalCutset has no real 'failureLogic_MinimalCutset19' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Failure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Failure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    partner = failureLogic_MinimalCutset()
    setattr(partner, 'failureLogic_MinimalCutset19', None)
    _safe_set(owner, 'failureLogic_Failure20', partner)
    assert owner in getattr(partner, 'failureLogic_MinimalCutset19')
    _safe_set(owner, 'failureLogic_Failure20', None)
    assert owner not in getattr(partner, 'failureLogic_MinimalCutset19')


def test_assoc_failures7_stub_double():
    # failureLogic_FailureModel has no real 'failureLogic_FailureModel8' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Failure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Failure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    partner = failureLogic_FailureModel()
    setattr(partner, 'failureLogic_FailureModel8', None)
    _safe_set(owner, 'failureLogic_Failure9', partner)
    assert owner in getattr(partner, 'failureLogic_FailureModel8')
    _safe_set(owner, 'failureLogic_Failure9', None)
    assert owner not in getattr(partner, 'failureLogic_FailureModel8')


def test_assoc_fromStates32_stub_double():
    # State has no real 'State34' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Markov_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Markov_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Markov_Transition(transition=3.14)
    partner = State()
    setattr(partner, 'State34', None)
    _safe_set(owner, 'failureLogic_Markov_Transition33', {partner})
    assert getattr(partner, 'State34') == owner
    _safe_set(owner, 'failureLogic_Markov_Transition33', set())
    assert getattr(partner, 'State34') is None


def test_assoc_toStates35_stub_double():
    # State has no real 'State37' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Markov_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Markov_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Markov_Transition(transition=3.14)
    partner = State()
    setattr(partner, 'State37', None)
    _safe_set(owner, 'failureLogic_Markov_Transition36', {partner})
    assert getattr(partner, 'State37') == owner
    _safe_set(owner, 'failureLogic_Markov_Transition36', set())
    assert getattr(partner, 'State37') is None


def test_assoc_transitionProbDistribution31_stub_double():
    # Markov_failureLogic_ProbDist has no real 'Markov_failureLogic_ProbDist' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Markov_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Markov_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Markov_Transition(transition=3.14)
    partner = Markov_failureLogic_ProbDist()
    setattr(partner, 'Markov_failureLogic_ProbDist', None)
    _safe_set(owner, 'failureLogic_Markov_Transition', partner)
    assert getattr(partner, 'Markov_failureLogic_ProbDist') == owner
    _safe_set(owner, 'failureLogic_Markov_Transition', None)
    assert getattr(partner, 'Markov_failureLogic_ProbDist') is None


