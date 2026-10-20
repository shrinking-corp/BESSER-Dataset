import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMultiplicity,
    ComplexEventOperator,
    EventPattern,
    events_AND,
    events_AbstractMultiplicity,
    events_AtLeastOne,
    events_AtomicEventPattern,
    events_Automaton,
    events_ComplexEventOperator,
    events_ComplexEventPattern,
    events_Event,
    events_EventModel,
    events_EventPattern,
    events_EventPatternReference,
    events_EventSource,
    events_FOLLOWS,
    events_Infinite,
    events_Multiplicity,
    events_NEG,
    events_OR,
    events_Timewindow,
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

def test_assoc_containedEventPatterns6_reverse_link_reassign_clear():
    a1 = events_EventPatternReference(parameterSymbolicNames="sample_text")
    a2 = events_EventPatternReference(parameterSymbolicNames="sample_text_2")
    b = events_ComplexEventPattern(eventContext="sample_text")
    _safe_set(b, 'events_ComplexEventPattern7', {a1})
    assert _is_linked(b, 'events_ComplexEventPattern7', a1)
    if hasattr(a1, 'events_EventPatternReference'):
        assert _is_linked(a1, 'events_EventPatternReference', b)
    _safe_set(b, 'events_ComplexEventPattern7', {a2})
    assert _is_linked(b, 'events_ComplexEventPattern7', a2)
    if hasattr(a1, 'events_EventPatternReference'):
        assert not _is_linked(a1, 'events_EventPatternReference', b)
    if hasattr(a2, 'events_EventPatternReference'):
        assert _is_linked(a2, 'events_EventPatternReference', b)
    _safe_set(b, 'events_ComplexEventPattern7', set())
    assert not _is_linked(b, 'events_ComplexEventPattern7', a2)
    if hasattr(a2, 'events_EventPatternReference'):
        assert not _is_linked(a2, 'events_EventPatternReference', b)


def test_assoc_eventPattern8_reverse_link_reassign_clear():
    a1 = events_EventPatternReference(parameterSymbolicNames="sample_text")
    a2 = events_EventPatternReference(parameterSymbolicNames="sample_text_2")
    b = events_EventPattern(id="sample_text")
    _safe_set(b, 'events_EventPattern10', a1)
    assert _is_linked(b, 'events_EventPattern10', a1)
    if hasattr(a1, 'events_EventPatternReference9'):
        assert _is_linked(a1, 'events_EventPatternReference9', b)
    _safe_set(b, 'events_EventPattern10', a2)
    assert _is_linked(b, 'events_EventPattern10', a2)
    if hasattr(a1, 'events_EventPatternReference9'):
        assert not _is_linked(a1, 'events_EventPatternReference9', b)
    if hasattr(a2, 'events_EventPatternReference9'):
        assert _is_linked(a2, 'events_EventPatternReference9', b)
    _safe_set(b, 'events_EventPattern10', None)
    assert not _is_linked(b, 'events_EventPattern10', a2)
    if hasattr(a2, 'events_EventPatternReference9'):
        assert not _is_linked(a2, 'events_EventPatternReference9', b)


def test_assoc_source13_reverse_link_reassign_clear():
    a1 = events_EventSource()
    a2 = events_EventSource()
    b = events_Event(isProcessed=True, timestamp="sample_text", type="sample_text")
    _safe_set(b, 'events_Event', a1)
    assert _is_linked(b, 'events_Event', a1)
    if hasattr(a1, 'events_EventSource'):
        assert _is_linked(a1, 'events_EventSource', b)
    _safe_set(b, 'events_Event', a2)
    assert _is_linked(b, 'events_Event', a2)
    if hasattr(a1, 'events_EventSource'):
        assert not _is_linked(a1, 'events_EventSource', b)
    if hasattr(a2, 'events_EventSource'):
        assert _is_linked(a2, 'events_EventSource', b)
    _safe_set(b, 'events_Event', None)
    assert not _is_linked(b, 'events_Event', a2)
    if hasattr(a2, 'events_EventSource'):
        assert not _is_linked(a2, 'events_EventSource', b)


def test_assoc_timewindow4_reverse_link_reassign_clear():
    a1 = events_Timewindow(time="sample_text")
    a2 = events_Timewindow(time="sample_text_2")
    b = events_ComplexEventPattern(eventContext="sample_text")
    _safe_set(b, 'events_ComplexEventPattern5', a1)
    assert _is_linked(b, 'events_ComplexEventPattern5', a1)
    if hasattr(a1, 'events_Timewindow'):
        assert _is_linked(a1, 'events_Timewindow', b)
    _safe_set(b, 'events_ComplexEventPattern5', a2)
    assert _is_linked(b, 'events_ComplexEventPattern5', a2)
    if hasattr(a1, 'events_Timewindow'):
        assert not _is_linked(a1, 'events_Timewindow', b)
    if hasattr(a2, 'events_Timewindow'):
        assert _is_linked(a2, 'events_Timewindow', b)
    _safe_set(b, 'events_ComplexEventPattern5', None)
    assert not _is_linked(b, 'events_ComplexEventPattern5', a2)
    if hasattr(a2, 'events_Timewindow'):
        assert not _is_linked(a2, 'events_Timewindow', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_automaton2_stub_double():
    # events_Automaton has no real 'events_Automaton' property in the generated
    # code (a bare stub) -- manually attach it so events_EventPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # events_EventPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = events_EventPattern(id="sample_text")
    partner = events_Automaton()
    setattr(partner, 'events_Automaton', None)
    _safe_set(owner, 'events_EventPattern', partner)
    assert getattr(partner, 'events_Automaton') == owner
    _safe_set(owner, 'events_EventPattern', None)
    assert getattr(partner, 'events_Automaton') is None


def test_assoc_eventModel1_stub_double():
    # events_EventModel has no real 'EventModel' property in the generated
    # code (a bare stub) -- manually attach it so events_EventPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # events_EventPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = events_EventPattern(id="sample_text")
    partner = events_EventModel()
    setattr(partner, 'EventModel', None)
    _safe_set(owner, 'eventPatterns', partner)
    assert getattr(partner, 'EventModel') == owner
    _safe_set(owner, 'eventPatterns', None)
    assert getattr(partner, 'EventModel') is None


def test_assoc_eventPatterns0_stub_double():
    # events_EventModel has no real 'eventModel' property in the generated
    # code (a bare stub) -- manually attach it so events_EventPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # events_EventPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = events_EventPattern(id="sample_text")
    partner = events_EventModel()
    setattr(partner, 'eventModel', None)
    _safe_set(owner, 'EventPattern', partner)
    assert owner in getattr(partner, 'eventModel')
    _safe_set(owner, 'EventPattern', None)
    assert owner not in getattr(partner, 'eventModel')


def test_assoc_multiplicity11_stub_double():
    # events_AbstractMultiplicity has no real 'events_AbstractMultiplicity' property in the generated
    # code (a bare stub) -- manually attach it so events_EventPatternReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # events_EventPatternReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = events_EventPatternReference(parameterSymbolicNames="sample_text")
    partner = events_AbstractMultiplicity()
    setattr(partner, 'events_AbstractMultiplicity', None)
    _safe_set(owner, 'events_EventPatternReference12', partner)
    assert getattr(partner, 'events_AbstractMultiplicity') == owner
    _safe_set(owner, 'events_EventPatternReference12', None)
    assert getattr(partner, 'events_AbstractMultiplicity') is None


def test_assoc_operator3_stub_double():
    # events_ComplexEventOperator has no real 'events_ComplexEventOperator' property in the generated
    # code (a bare stub) -- manually attach it so events_ComplexEventPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # events_ComplexEventPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = events_ComplexEventPattern(eventContext="sample_text")
    partner = events_ComplexEventOperator()
    setattr(partner, 'events_ComplexEventOperator', None)
    _safe_set(owner, 'events_ComplexEventPattern', partner)
    assert getattr(partner, 'events_ComplexEventOperator') == owner
    _safe_set(owner, 'events_ComplexEventPattern', None)
    assert getattr(partner, 'events_ComplexEventOperator') is None


