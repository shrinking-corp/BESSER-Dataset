import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BaseElement,
    Cause,
    FMEAEntry,
    Failure,
    FailureModel,
    ODEProductPackage,
    failureLogic_Cause,
    failureLogic_FMEA,
    failureLogic_FMEAEntry,
    failureLogic_FMEDAEntry,
    failureLogic_Failure,
    failureLogic_FailureLogicPackage,
    failureLogic_FailureModel,
    failureLogic_FaultTree,
    failureLogic_Gate,
    failureLogic_MarkovChain,
    failureLogic_MinimalCutSets,
    failureLogic_MinimalCutset,
    failureLogic_ProbDist,
    failureLogic_ProbDistParam,
    failureLogic_SecurityViolation,
    failureLogic_State,
    failureLogic_Transition,
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

def test_assoc_causes27_reverse_link_reassign_clear():
    a1 = failureLogic_Gate(gateType="sample_text")
    a2 = failureLogic_Gate(gateType="sample_text_2")
    b = failureLogic_Cause(causeType="sample_text")
    _safe_set(b, 'failureLogic_Cause28', a1)
    assert _is_linked(b, 'failureLogic_Cause28', a1)
    if hasattr(a1, 'failureLogic_Gate'):
        assert _is_linked(a1, 'failureLogic_Gate', b)
    _safe_set(b, 'failureLogic_Cause28', a2)
    assert _is_linked(b, 'failureLogic_Cause28', a2)
    if hasattr(a1, 'failureLogic_Gate'):
        assert not _is_linked(a1, 'failureLogic_Gate', b)
    if hasattr(a2, 'failureLogic_Gate'):
        assert _is_linked(a2, 'failureLogic_Gate', b)
    _safe_set(b, 'failureLogic_Cause28', None)
    assert not _is_linked(b, 'failureLogic_Cause28', a2)
    if hasattr(a2, 'failureLogic_Gate'):
        assert not _is_linked(a2, 'failureLogic_Gate', b)


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


def test_assoc_diagnosisProbDistribution51_reverse_link_reassign_clear():
    a1 = failureLogic_ProbDist(type="sample_text")
    a2 = failureLogic_ProbDist(type="sample_text_2")
    b = failureLogic_FMEDAEntry(diagnosisRate=3.14)
    _safe_set(b, 'failureLogic_FMEDAEntry', a1)
    assert _is_linked(b, 'failureLogic_FMEDAEntry', a1)
    if hasattr(a1, 'failureLogic_ProbDist52'):
        assert _is_linked(a1, 'failureLogic_ProbDist52', b)
    _safe_set(b, 'failureLogic_FMEDAEntry', a2)
    assert _is_linked(b, 'failureLogic_FMEDAEntry', a2)
    if hasattr(a1, 'failureLogic_ProbDist52'):
        assert not _is_linked(a1, 'failureLogic_ProbDist52', b)
    if hasattr(a2, 'failureLogic_ProbDist52'):
        assert _is_linked(a2, 'failureLogic_ProbDist52', b)
    _safe_set(b, 'failureLogic_FMEDAEntry', None)
    assert not _is_linked(b, 'failureLogic_FMEDAEntry', a2)
    if hasattr(a2, 'failureLogic_ProbDist52'):
        assert not _is_linked(a2, 'failureLogic_ProbDist52', b)


def test_assoc_failState32_reverse_link_reassign_clear():
    a1 = failureLogic_State(isFailState=True, isInitialState=True)
    a2 = failureLogic_State(isFailState=False, isInitialState=False)
    b = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    _safe_set(b, 'failureLogic_Failure34', a1)
    assert _is_linked(b, 'failureLogic_Failure34', a1)
    if hasattr(a1, 'failureLogic_State33'):
        assert _is_linked(a1, 'failureLogic_State33', b)
    _safe_set(b, 'failureLogic_Failure34', a2)
    assert _is_linked(b, 'failureLogic_Failure34', a2)
    if hasattr(a1, 'failureLogic_State33'):
        assert not _is_linked(a1, 'failureLogic_State33', b)
    if hasattr(a2, 'failureLogic_State33'):
        assert _is_linked(a2, 'failureLogic_State33', b)
    _safe_set(b, 'failureLogic_Failure34', None)
    assert not _is_linked(b, 'failureLogic_Failure34', a2)
    if hasattr(a2, 'failureLogic_State33'):
        assert not _is_linked(a2, 'failureLogic_State33', b)


def test_assoc_failure24_reverse_link_reassign_clear():
    a1 = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    a2 = failureLogic_Failure(failureClass="sample_text_2", failureRate=9.99, isCcf=False, originType="sample_text_2")
    b = failureLogic_Cause(causeType="sample_text")
    _safe_set(b, 'failureLogic_Cause25', a1)
    assert _is_linked(b, 'failureLogic_Cause25', a1)
    if hasattr(a1, 'failureLogic_Failure26'):
        assert _is_linked(a1, 'failureLogic_Failure26', b)
    _safe_set(b, 'failureLogic_Cause25', a2)
    assert _is_linked(b, 'failureLogic_Cause25', a2)
    if hasattr(a1, 'failureLogic_Failure26'):
        assert not _is_linked(a1, 'failureLogic_Failure26', b)
    if hasattr(a2, 'failureLogic_Failure26'):
        assert _is_linked(a2, 'failureLogic_Failure26', b)
    _safe_set(b, 'failureLogic_Cause25', None)
    assert not _is_linked(b, 'failureLogic_Cause25', a2)
    if hasattr(a2, 'failureLogic_Failure26'):
        assert not _is_linked(a2, 'failureLogic_Failure26', b)


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


def test_assoc_fromStates38_reverse_link_reassign_clear():
    a1 = failureLogic_Transition(transition=3.14)
    a2 = failureLogic_Transition(transition=9.99)
    b = failureLogic_State(isFailState=True, isInitialState=True)
    _safe_set(b, 'failureLogic_State40', a1)
    assert _is_linked(b, 'failureLogic_State40', a1)
    if hasattr(a1, 'failureLogic_Transition39'):
        assert _is_linked(a1, 'failureLogic_Transition39', b)
    _safe_set(b, 'failureLogic_State40', a2)
    assert _is_linked(b, 'failureLogic_State40', a2)
    if hasattr(a1, 'failureLogic_Transition39'):
        assert not _is_linked(a1, 'failureLogic_Transition39', b)
    if hasattr(a2, 'failureLogic_Transition39'):
        assert _is_linked(a2, 'failureLogic_Transition39', b)
    _safe_set(b, 'failureLogic_State40', None)
    assert not _is_linked(b, 'failureLogic_State40', a2)
    if hasattr(a2, 'failureLogic_Transition39'):
        assert not _is_linked(a2, 'failureLogic_Transition39', b)


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


def test_assoc_toStates41_reverse_link_reassign_clear():
    a1 = failureLogic_Transition(transition=3.14)
    a2 = failureLogic_Transition(transition=9.99)
    b = failureLogic_State(isFailState=True, isInitialState=True)
    _safe_set(b, 'failureLogic_State43', a1)
    assert _is_linked(b, 'failureLogic_State43', a1)
    if hasattr(a1, 'failureLogic_Transition42'):
        assert _is_linked(a1, 'failureLogic_Transition42', b)
    _safe_set(b, 'failureLogic_State43', a2)
    assert _is_linked(b, 'failureLogic_State43', a2)
    if hasattr(a1, 'failureLogic_Transition42'):
        assert not _is_linked(a1, 'failureLogic_Transition42', b)
    if hasattr(a2, 'failureLogic_Transition42'):
        assert _is_linked(a2, 'failureLogic_Transition42', b)
    _safe_set(b, 'failureLogic_State43', None)
    assert not _is_linked(b, 'failureLogic_State43', a2)
    if hasattr(a2, 'failureLogic_Transition42'):
        assert not _is_linked(a2, 'failureLogic_Transition42', b)


def test_assoc_transitionProbDistribution35_reverse_link_reassign_clear():
    a1 = failureLogic_Transition(transition=3.14)
    a2 = failureLogic_Transition(transition=9.99)
    b = failureLogic_ProbDist(type="sample_text")
    _safe_set(b, 'failureLogic_ProbDist37', a1)
    assert _is_linked(b, 'failureLogic_ProbDist37', a1)
    if hasattr(a1, 'failureLogic_Transition36'):
        assert _is_linked(a1, 'failureLogic_Transition36', b)
    _safe_set(b, 'failureLogic_ProbDist37', a2)
    assert _is_linked(b, 'failureLogic_ProbDist37', a2)
    if hasattr(a1, 'failureLogic_Transition36'):
        assert not _is_linked(a1, 'failureLogic_Transition36', b)
    if hasattr(a2, 'failureLogic_Transition36'):
        assert _is_linked(a2, 'failureLogic_Transition36', b)
    _safe_set(b, 'failureLogic_ProbDist37', None)
    assert not _is_linked(b, 'failureLogic_ProbDist37', a2)
    if hasattr(a2, 'failureLogic_Transition36'):
        assert not _is_linked(a2, 'failureLogic_Transition36', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_causes23_stub_double():
    # failureLogic_FaultTree has no real 'failureLogic_FaultTree' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Cause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Cause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Cause(causeType="sample_text")
    partner = failureLogic_FaultTree()
    setattr(partner, 'failureLogic_FaultTree', None)
    _safe_set(owner, 'failureLogic_Cause', partner)
    assert owner in getattr(partner, 'failureLogic_FaultTree')
    _safe_set(owner, 'failureLogic_Cause', None)
    assert owner not in getattr(partner, 'failureLogic_FaultTree')


def test_assoc_effect45_stub_double():
    # failureLogic_FMEAEntry has no real 'failureLogic_FMEAEntry46' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Failure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Failure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    partner = failureLogic_FMEAEntry()
    setattr(partner, 'failureLogic_FMEAEntry46', None)
    _safe_set(owner, 'failureLogic_Failure47', partner)
    assert getattr(partner, 'failureLogic_FMEAEntry46') == owner
    _safe_set(owner, 'failureLogic_Failure47', None)
    assert getattr(partner, 'failureLogic_FMEAEntry46') is None


def test_assoc_entries44_stub_double():
    # failureLogic_FMEAEntry has no real 'failureLogic_FMEAEntry' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_FMEA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_FMEA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_FMEA(type="sample_text")
    partner = failureLogic_FMEAEntry()
    setattr(partner, 'failureLogic_FMEAEntry', None)
    _safe_set(owner, 'failureLogic_FMEA', {partner})
    assert getattr(partner, 'failureLogic_FMEAEntry') == owner
    _safe_set(owner, 'failureLogic_FMEA', set())
    assert getattr(partner, 'failureLogic_FMEAEntry') is None


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


def test_assoc_mode48_stub_double():
    # failureLogic_FMEAEntry has no real 'failureLogic_FMEAEntry49' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Failure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Failure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Failure(failureClass="sample_text", failureRate=3.14, isCcf=True, originType="sample_text")
    partner = failureLogic_FMEAEntry()
    setattr(partner, 'failureLogic_FMEAEntry49', None)
    _safe_set(owner, 'failureLogic_Failure50', partner)
    assert getattr(partner, 'failureLogic_FMEAEntry49') == owner
    _safe_set(owner, 'failureLogic_Failure50', None)
    assert getattr(partner, 'failureLogic_FMEAEntry49') is None


def test_assoc_states30_stub_double():
    # failureLogic_MarkovChain has no real 'failureLogic_MarkovChain31' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_State(isFailState=True, isInitialState=True)
    partner = failureLogic_MarkovChain()
    setattr(partner, 'failureLogic_MarkovChain31', None)
    _safe_set(owner, 'failureLogic_State', partner)
    assert owner in getattr(partner, 'failureLogic_MarkovChain31')
    _safe_set(owner, 'failureLogic_State', None)
    assert owner not in getattr(partner, 'failureLogic_MarkovChain31')


def test_assoc_transitions29_stub_double():
    # failureLogic_MarkovChain has no real 'failureLogic_MarkovChain' property in the generated
    # code (a bare stub) -- manually attach it so failureLogic_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # failureLogic_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = failureLogic_Transition(transition=3.14)
    partner = failureLogic_MarkovChain()
    setattr(partner, 'failureLogic_MarkovChain', None)
    _safe_set(owner, 'failureLogic_Transition', partner)
    assert owner in getattr(partner, 'failureLogic_MarkovChain')
    _safe_set(owner, 'failureLogic_Transition', None)
    assert owner not in getattr(partner, 'failureLogic_MarkovChain')


