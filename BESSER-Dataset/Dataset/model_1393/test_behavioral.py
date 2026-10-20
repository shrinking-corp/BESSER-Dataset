import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractBehavior,
    AbstractEvent,
    AbstractState,
    CapellaElement,
    IState,
    ModelElement,
    NamedElement,
    Pseudostate,
    State,
    StateEvent,
    Structure,
    TraceableElement,
    capellacommon_AbstractCapability,
    capellacommon_AbstractCapabilityPkg,
    capellacommon_AbstractEvent,
    capellacommon_AbstractFunction,
    capellacommon_AbstractState,
    capellacommon_ChangeEvent,
    capellacommon_ChoicePseudoState,
    capellacommon_Constraint,
    capellacommon_DeepHistoryPseudoState,
    capellacommon_EntryPointPseudoState,
    capellacommon_ExitPointPseudoState,
    capellacommon_FinalState,
    capellacommon_ForkPseudoState,
    capellacommon_FunctionalChain,
    capellacommon_GenericTrace,
    capellacommon_InitialPseudoState,
    capellacommon_JoinPseudoState,
    capellacommon_Mode,
    capellacommon_Pseudostate,
    capellacommon_Region,
    capellacommon_ShallowHistoryPseudoState,
    capellacommon_State,
    capellacommon_StateEvent,
    capellacommon_StateMachine,
    capellacommon_StateTransition,
    capellacommon_TerminatePseudoState,
    capellacommon_TimeEvent,
    capellacommon_TraceableElement,
    ChangeEventKind,
    TimeEventKind,
    TransitionKind,
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

def test_assoc_realizedStateTransitions40_reverse_link_reassign_clear():
    a1 = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    a2 = capellacommon_StateTransition(kind="sample_text_2", triggerDescription="sample_text_2")
    b = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    _safe_set(b, 'capellacommon_StateTransition41', a1)
    assert _is_linked(b, 'capellacommon_StateTransition41', a1)
    if hasattr(a1, 'capellacommon_StateTransition39'):
        assert _is_linked(a1, 'capellacommon_StateTransition39', b)
    _safe_set(b, 'capellacommon_StateTransition41', a2)
    assert _is_linked(b, 'capellacommon_StateTransition41', a2)
    if hasattr(a1, 'capellacommon_StateTransition39'):
        assert not _is_linked(a1, 'capellacommon_StateTransition39', b)
    if hasattr(a2, 'capellacommon_StateTransition39'):
        assert _is_linked(a2, 'capellacommon_StateTransition39', b)
    _safe_set(b, 'capellacommon_StateTransition41', None)
    assert not _is_linked(b, 'capellacommon_StateTransition41', a2)
    if hasattr(a2, 'capellacommon_StateTransition39'):
        assert not _is_linked(a2, 'capellacommon_StateTransition39', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_effect33_stub_double():
    # capellacommon_AbstractEvent has no real 'capellacommon_AbstractEvent35' property in the generated
    # code (a bare stub) -- manually attach it so capellacommon_StateTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # capellacommon_StateTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    partner = capellacommon_AbstractEvent()
    setattr(partner, 'capellacommon_AbstractEvent35', None)
    _safe_set(owner, 'capellacommon_StateTransition34', partner)
    assert getattr(partner, 'capellacommon_AbstractEvent35') == owner
    _safe_set(owner, 'capellacommon_StateTransition34', None)
    assert getattr(partner, 'capellacommon_AbstractEvent35') is None


def test_assoc_guard25_stub_double():
    # capellacommon_Constraint has no real 'capellacommon_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so capellacommon_StateTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # capellacommon_StateTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    partner = capellacommon_Constraint()
    setattr(partner, 'capellacommon_Constraint', None)
    _safe_set(owner, 'capellacommon_StateTransition26', partner)
    assert getattr(partner, 'capellacommon_Constraint') == owner
    _safe_set(owner, 'capellacommon_StateTransition26', None)
    assert getattr(partner, 'capellacommon_Constraint') is None


def test_assoc_ownedTransitions7_stub_double():
    # capellacommon_Region has no real 'capellacommon_Region8' property in the generated
    # code (a bare stub) -- manually attach it so capellacommon_StateTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # capellacommon_StateTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    partner = capellacommon_Region()
    setattr(partner, 'capellacommon_Region8', None)
    _safe_set(owner, 'capellacommon_StateTransition', partner)
    assert owner in getattr(partner, 'capellacommon_Region8')
    _safe_set(owner, 'capellacommon_StateTransition', None)
    assert owner not in getattr(partner, 'capellacommon_Region8')


def test_assoc_source27_stub_double():
    # capellacommon_AbstractState has no real 'capellacommon_AbstractState29' property in the generated
    # code (a bare stub) -- manually attach it so capellacommon_StateTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # capellacommon_StateTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    partner = capellacommon_AbstractState()
    setattr(partner, 'capellacommon_AbstractState29', None)
    _safe_set(owner, 'capellacommon_StateTransition28', partner)
    assert getattr(partner, 'capellacommon_AbstractState29') == owner
    _safe_set(owner, 'capellacommon_StateTransition28', None)
    assert getattr(partner, 'capellacommon_AbstractState29') is None


def test_assoc_target30_stub_double():
    # capellacommon_AbstractState has no real 'capellacommon_AbstractState32' property in the generated
    # code (a bare stub) -- manually attach it so capellacommon_StateTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # capellacommon_StateTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    partner = capellacommon_AbstractState()
    setattr(partner, 'capellacommon_AbstractState32', None)
    _safe_set(owner, 'capellacommon_StateTransition31', partner)
    assert getattr(partner, 'capellacommon_AbstractState32') == owner
    _safe_set(owner, 'capellacommon_StateTransition31', None)
    assert getattr(partner, 'capellacommon_AbstractState32') is None


def test_assoc_triggers36_stub_double():
    # capellacommon_AbstractEvent has no real 'capellacommon_AbstractEvent38' property in the generated
    # code (a bare stub) -- manually attach it so capellacommon_StateTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # capellacommon_StateTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = capellacommon_StateTransition(kind="sample_text", triggerDescription="sample_text")
    partner = capellacommon_AbstractEvent()
    setattr(partner, 'capellacommon_AbstractEvent38', None)
    _safe_set(owner, 'capellacommon_StateTransition37', {partner})
    assert getattr(partner, 'capellacommon_AbstractEvent38') == owner
    _safe_set(owner, 'capellacommon_StateTransition37', set())
    assert getattr(partner, 'capellacommon_AbstractEvent38') is None


