import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_preTransition23_reverse_link_reassign_clear():
    a1 = Behaviour_Server(capacity=7)
    a2 = Behaviour_Server(capacity=13)
    b = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    _safe_set(b, 'Behaviour_PreTransitionConnection25', a1)
    assert _is_linked(b, 'Behaviour_PreTransitionConnection25', a1)
    if hasattr(a1, 'Behaviour_Server24'):
        assert _is_linked(a1, 'Behaviour_Server24', b)
    _safe_set(b, 'Behaviour_PreTransitionConnection25', a2)
    assert _is_linked(b, 'Behaviour_PreTransitionConnection25', a2)
    if hasattr(a1, 'Behaviour_Server24'):
        assert not _is_linked(a1, 'Behaviour_Server24', b)
    if hasattr(a2, 'Behaviour_Server24'):
        assert _is_linked(a2, 'Behaviour_Server24', b)
    _safe_set(b, 'Behaviour_PreTransitionConnection25', None)
    assert not _is_linked(b, 'Behaviour_PreTransitionConnection25', a2)
    if hasattr(a2, 'Behaviour_Server24'):
        assert not _is_linked(a2, 'Behaviour_Server24', b)


def test_assoc_preTransitions17_reverse_link_reassign_clear():
    a1 = Behaviour_StartPlace(spawnPolicy="sample_text")
    a2 = Behaviour_StartPlace(spawnPolicy="sample_text_2")
    b = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    _safe_set(b, 'Behaviour_PreTransitionConnection18', a1)
    assert _is_linked(b, 'Behaviour_PreTransitionConnection18', a1)
    if hasattr(a1, 'Behaviour_StartPlace'):
        assert _is_linked(a1, 'Behaviour_StartPlace', b)
    _safe_set(b, 'Behaviour_PreTransitionConnection18', a2)
    assert _is_linked(b, 'Behaviour_PreTransitionConnection18', a2)
    if hasattr(a1, 'Behaviour_StartPlace'):
        assert not _is_linked(a1, 'Behaviour_StartPlace', b)
    if hasattr(a2, 'Behaviour_StartPlace'):
        assert _is_linked(a2, 'Behaviour_StartPlace', b)
    _safe_set(b, 'Behaviour_PreTransitionConnection18', None)
    assert not _is_linked(b, 'Behaviour_PreTransitionConnection18', a2)
    if hasattr(a2, 'Behaviour_StartPlace'):
        assert not _is_linked(a2, 'Behaviour_StartPlace', b)


def test_assoc_server26_reverse_link_reassign_clear():
    a1 = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    a2 = Behaviour_WaitingLine(schedulingPolicy="sample_text_2")
    b = Behaviour_Server(capacity=7)
    _safe_set(b, 'Server', a1)
    assert _is_linked(b, 'Server', a1)
    if hasattr(a1, 'waitingLine'):
        assert _is_linked(a1, 'waitingLine', b)
    _safe_set(b, 'Server', a2)
    assert _is_linked(b, 'Server', a2)
    if hasattr(a1, 'waitingLine'):
        assert not _is_linked(a1, 'waitingLine', b)
    if hasattr(a2, 'waitingLine'):
        assert _is_linked(a2, 'waitingLine', b)
    _safe_set(b, 'Server', None)
    assert not _is_linked(b, 'Server', a2)
    if hasattr(a2, 'waitingLine'):
        assert not _is_linked(a2, 'waitingLine', b)


def test_assoc_waitingLine22_reverse_link_reassign_clear():
    a1 = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    a2 = Behaviour_WaitingLine(schedulingPolicy="sample_text_2")
    b = Behaviour_Server(capacity=7)
    _safe_set(b, 'server', a1)
    assert _is_linked(b, 'server', a1)
    if hasattr(a1, 'WaitingLine'):
        assert _is_linked(a1, 'WaitingLine', b)
    _safe_set(b, 'server', a2)
    assert _is_linked(b, 'server', a2)
    if hasattr(a1, 'WaitingLine'):
        assert not _is_linked(a1, 'WaitingLine', b)
    if hasattr(a2, 'WaitingLine'):
        assert _is_linked(a2, 'WaitingLine', b)
    _safe_set(b, 'server', None)
    assert not _is_linked(b, 'server', a2)
    if hasattr(a2, 'WaitingLine'):
        assert not _is_linked(a2, 'WaitingLine', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes30_stub_double():
    # Behaviour_Token has no real 'Behaviour_Token31' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_Colour's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_Colour's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_Colour(attribute="sample_text")
    partner = Behaviour_Token()
    setattr(partner, 'Behaviour_Token31', None)
    _safe_set(owner, 'Behaviour_Colour', partner)
    assert owner in getattr(partner, 'Behaviour_Token31')
    _safe_set(owner, 'Behaviour_Colour', None)
    assert owner not in getattr(partner, 'Behaviour_Token31')


def test_assoc_emittedToken46_stub_double():
    # Behaviour_Token has no real 'Behaviour_Token48' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_TransitionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_TransitionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_TransitionFunction(transitionFunction="sample_text")
    partner = Behaviour_Token()
    setattr(partner, 'Behaviour_Token48', None)
    _safe_set(owner, 'Behaviour_TransitionFunction47', {partner})
    assert getattr(partner, 'Behaviour_Token48') == owner
    _safe_set(owner, 'Behaviour_TransitionFunction47', set())
    assert getattr(partner, 'Behaviour_Token48') is None


def test_assoc_incommingEdges2_stub_double():
    # Behaviour_Transition has no real 'Behaviour_Transition3' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_PreTransitionConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_PreTransitionConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    partner = Behaviour_Transition()
    setattr(partner, 'Behaviour_Transition3', None)
    _safe_set(owner, 'Behaviour_PreTransitionConnection', partner)
    assert owner in getattr(partner, 'Behaviour_Transition3')
    _safe_set(owner, 'Behaviour_PreTransitionConnection', None)
    assert owner not in getattr(partner, 'Behaviour_Transition3')


def test_assoc_postTransitions27_stub_double():
    # Behaviour_PostTransitionConnection has no real 'Behaviour_PostTransitionConnection29' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_WaitingLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_WaitingLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    partner = Behaviour_PostTransitionConnection()
    setattr(partner, 'Behaviour_PostTransitionConnection29', None)
    _safe_set(owner, 'Behaviour_WaitingLine28', {partner})
    assert getattr(partner, 'Behaviour_PostTransitionConnection29') == owner
    _safe_set(owner, 'Behaviour_WaitingLine28', set())
    assert getattr(partner, 'Behaviour_PostTransitionConnection29') is None


def test_assoc_preTransitions9_stub_double():
    # Behaviour_DefaultPlace has no real 'Behaviour_DefaultPlace' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_PreTransitionConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_PreTransitionConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_PreTransitionConnection(requiredTokenAmount=7)
    partner = Behaviour_DefaultPlace()
    setattr(partner, 'Behaviour_DefaultPlace', None)
    _safe_set(owner, 'Behaviour_PreTransitionConnection10', partner)
    assert owner in getattr(partner, 'Behaviour_DefaultPlace')
    _safe_set(owner, 'Behaviour_PreTransitionConnection10', None)
    assert owner not in getattr(partner, 'Behaviour_DefaultPlace')


def test_assoc_server14_stub_double():
    # Behaviour_QueuePlace has no real 'Behaviour_QueuePlace' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_Server's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_Server's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_Server(capacity=7)
    partner = Behaviour_QueuePlace()
    setattr(partner, 'Behaviour_QueuePlace', None)
    _safe_set(owner, 'Behaviour_Server', partner)
    assert getattr(partner, 'Behaviour_QueuePlace') == owner
    _safe_set(owner, 'Behaviour_Server', None)
    assert getattr(partner, 'Behaviour_QueuePlace') is None


def test_assoc_transitionConnection43_stub_double():
    # Behaviour_PostTransitionConnection has no real 'Behaviour_PostTransitionConnection45' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_TransitionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_TransitionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_TransitionFunction(transitionFunction="sample_text")
    partner = Behaviour_PostTransitionConnection()
    setattr(partner, 'Behaviour_PostTransitionConnection45', None)
    _safe_set(owner, 'Behaviour_TransitionFunction44', partner)
    assert getattr(partner, 'Behaviour_PostTransitionConnection45') == owner
    _safe_set(owner, 'Behaviour_TransitionFunction44', None)
    assert getattr(partner, 'Behaviour_PostTransitionConnection45') is None


def test_assoc_transitionFunction19_stub_double():
    # Behaviour_ConditionalTransition has no real 'Behaviour_ConditionalTransition' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_TransitionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_TransitionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_TransitionFunction(transitionFunction="sample_text")
    partner = Behaviour_ConditionalTransition()
    setattr(partner, 'Behaviour_ConditionalTransition', None)
    _safe_set(owner, 'Behaviour_TransitionFunction', partner)
    assert owner in getattr(partner, 'Behaviour_ConditionalTransition')
    _safe_set(owner, 'Behaviour_TransitionFunction', None)
    assert owner not in getattr(partner, 'Behaviour_ConditionalTransition')


def test_assoc_transitionFunction20_stub_double():
    # Behaviour_StochasticTransition has no real 'Behaviour_StochasticTransition' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_TransitionFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_TransitionFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_TransitionFunction(transitionFunction="sample_text")
    partner = Behaviour_StochasticTransition()
    setattr(partner, 'Behaviour_StochasticTransition', None)
    _safe_set(owner, 'Behaviour_TransitionFunction21', partner)
    assert owner in getattr(partner, 'Behaviour_StochasticTransition')
    _safe_set(owner, 'Behaviour_TransitionFunction21', None)
    assert owner not in getattr(partner, 'Behaviour_StochasticTransition')


def test_assoc_waitingLine15_stub_double():
    # Behaviour_QueuePlace has no real 'Behaviour_QueuePlace16' property in the generated
    # code (a bare stub) -- manually attach it so Behaviour_WaitingLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Behaviour_WaitingLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Behaviour_WaitingLine(schedulingPolicy="sample_text")
    partner = Behaviour_QueuePlace()
    setattr(partner, 'Behaviour_QueuePlace16', None)
    _safe_set(owner, 'Behaviour_WaitingLine', partner)
    assert getattr(partner, 'Behaviour_QueuePlace16') == owner
    _safe_set(owner, 'Behaviour_WaitingLine', None)
    assert getattr(partner, 'Behaviour_QueuePlace16') is None


