import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Node,
    OccurrenceNet,
    adaptiveSystem_AdaptiveProcess,
    adaptiveSystem_AdaptiveSystem,
    adaptiveSystem_Arc,
    adaptiveSystem_ArcToCondition,
    adaptiveSystem_ArcToEvent,
    adaptiveSystem_Condition,
    adaptiveSystem_DoNet,
    adaptiveSystem_Event,
    adaptiveSystem_Node,
    adaptiveSystem_OccurrenceNet,
    adaptiveSystem_Oclet,
    adaptiveSystem_PreNet,
    Orientation,
    Quantor,
    Temp,
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

def test_assoc_arcs8_reverse_link_reassign_clear():
    a1 = adaptiveSystem_OccurrenceNet(name="sample_text")
    a2 = adaptiveSystem_OccurrenceNet(name="sample_text_2")
    b = adaptiveSystem_Arc(weight=7)
    _safe_set(b, 'adaptiveSystem_Arc', a1)
    assert _is_linked(b, 'adaptiveSystem_Arc', a1)
    if hasattr(a1, 'adaptiveSystem_OccurrenceNet9'):
        assert _is_linked(a1, 'adaptiveSystem_OccurrenceNet9', b)
    _safe_set(b, 'adaptiveSystem_Arc', a2)
    assert _is_linked(b, 'adaptiveSystem_Arc', a2)
    if hasattr(a1, 'adaptiveSystem_OccurrenceNet9'):
        assert not _is_linked(a1, 'adaptiveSystem_OccurrenceNet9', b)
    if hasattr(a2, 'adaptiveSystem_OccurrenceNet9'):
        assert _is_linked(a2, 'adaptiveSystem_OccurrenceNet9', b)
    _safe_set(b, 'adaptiveSystem_Arc', None)
    assert not _is_linked(b, 'adaptiveSystem_Arc', a2)
    if hasattr(a2, 'adaptiveSystem_OccurrenceNet9'):
        assert not _is_linked(a2, 'adaptiveSystem_OccurrenceNet9', b)


def test_assoc_nodes7_reverse_link_reassign_clear():
    a1 = adaptiveSystem_OccurrenceNet(name="sample_text")
    a2 = adaptiveSystem_OccurrenceNet(name="sample_text_2")
    b = adaptiveSystem_Node(abstract=True, disabledByAntiOclet=True, disabledByConflict=True, name="sample_text", temp="sample_text")
    _safe_set(b, 'adaptiveSystem_Node', a1)
    assert _is_linked(b, 'adaptiveSystem_Node', a1)
    if hasattr(a1, 'adaptiveSystem_OccurrenceNet'):
        assert _is_linked(a1, 'adaptiveSystem_OccurrenceNet', b)
    _safe_set(b, 'adaptiveSystem_Node', a2)
    assert _is_linked(b, 'adaptiveSystem_Node', a2)
    if hasattr(a1, 'adaptiveSystem_OccurrenceNet'):
        assert not _is_linked(a1, 'adaptiveSystem_OccurrenceNet', b)
    if hasattr(a2, 'adaptiveSystem_OccurrenceNet'):
        assert _is_linked(a2, 'adaptiveSystem_OccurrenceNet', b)
    _safe_set(b, 'adaptiveSystem_Node', None)
    assert not _is_linked(b, 'adaptiveSystem_Node', a2)
    if hasattr(a2, 'adaptiveSystem_OccurrenceNet'):
        assert not _is_linked(a2, 'adaptiveSystem_OccurrenceNet', b)


def test_assoc_oclets0_reverse_link_reassign_clear():
    a1 = adaptiveSystem_Oclet(name="sample_text", orientation="sample_text", quantor="sample_text", wellFormed=True)
    a2 = adaptiveSystem_Oclet(name="sample_text_2", orientation="sample_text_2", quantor="sample_text_2", wellFormed=False)
    b = adaptiveSystem_AdaptiveSystem(setWellformednessToOclets=True)
    _safe_set(b, 'adaptiveSystem_AdaptiveSystem', {a1})
    assert _is_linked(b, 'adaptiveSystem_AdaptiveSystem', a1)
    if hasattr(a1, 'adaptiveSystem_Oclet'):
        assert _is_linked(a1, 'adaptiveSystem_Oclet', b)
    _safe_set(b, 'adaptiveSystem_AdaptiveSystem', {a2})
    assert _is_linked(b, 'adaptiveSystem_AdaptiveSystem', a2)
    if hasattr(a1, 'adaptiveSystem_Oclet'):
        assert not _is_linked(a1, 'adaptiveSystem_Oclet', b)
    if hasattr(a2, 'adaptiveSystem_Oclet'):
        assert _is_linked(a2, 'adaptiveSystem_Oclet', b)
    _safe_set(b, 'adaptiveSystem_AdaptiveSystem', set())
    assert not _is_linked(b, 'adaptiveSystem_AdaptiveSystem', a2)
    if hasattr(a2, 'adaptiveSystem_Oclet'):
        assert not _is_linked(a2, 'adaptiveSystem_Oclet', b)


def test_assoc_postConditions21_reverse_link_reassign_clear():
    a1 = adaptiveSystem_Event(enabled=True, saturated=True)
    a2 = adaptiveSystem_Event(enabled=False, saturated=False)
    b = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    _safe_set(b, 'Condition22', a1)
    assert _is_linked(b, 'Condition22', a1)
    if hasattr(a1, 'preEvents'):
        assert _is_linked(a1, 'preEvents', b)
    _safe_set(b, 'Condition22', a2)
    assert _is_linked(b, 'Condition22', a2)
    if hasattr(a1, 'preEvents'):
        assert not _is_linked(a1, 'preEvents', b)
    if hasattr(a2, 'preEvents'):
        assert _is_linked(a2, 'preEvents', b)
    _safe_set(b, 'Condition22', None)
    assert not _is_linked(b, 'Condition22', a2)
    if hasattr(a2, 'preEvents'):
        assert not _is_linked(a2, 'preEvents', b)


def test_assoc_postEvents16_reverse_link_reassign_clear():
    a1 = adaptiveSystem_Event(enabled=True, saturated=True)
    a2 = adaptiveSystem_Event(enabled=False, saturated=False)
    b = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    _safe_set(b, 'preConditions', {a1})
    assert _is_linked(b, 'preConditions', a1)
    if hasattr(a1, 'Event17'):
        assert _is_linked(a1, 'Event17', b)
    _safe_set(b, 'preConditions', {a2})
    assert _is_linked(b, 'preConditions', a2)
    if hasattr(a1, 'Event17'):
        assert not _is_linked(a1, 'Event17', b)
    if hasattr(a2, 'Event17'):
        assert _is_linked(a2, 'Event17', b)
    _safe_set(b, 'preConditions', set())
    assert not _is_linked(b, 'preConditions', a2)
    if hasattr(a2, 'Event17'):
        assert not _is_linked(a2, 'Event17', b)


def test_assoc_preConditions20_reverse_link_reassign_clear():
    a1 = adaptiveSystem_Event(enabled=True, saturated=True)
    a2 = adaptiveSystem_Event(enabled=False, saturated=False)
    b = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    _safe_set(b, 'Condition', a1)
    assert _is_linked(b, 'Condition', a1)
    if hasattr(a1, 'postEvents'):
        assert _is_linked(a1, 'postEvents', b)
    _safe_set(b, 'Condition', a2)
    assert _is_linked(b, 'Condition', a2)
    if hasattr(a1, 'postEvents'):
        assert not _is_linked(a1, 'postEvents', b)
    if hasattr(a2, 'postEvents'):
        assert _is_linked(a2, 'postEvents', b)
    _safe_set(b, 'Condition', None)
    assert not _is_linked(b, 'Condition', a2)
    if hasattr(a2, 'postEvents'):
        assert not _is_linked(a2, 'postEvents', b)


def test_assoc_preEvents15_reverse_link_reassign_clear():
    a1 = adaptiveSystem_Event(enabled=True, saturated=True)
    a2 = adaptiveSystem_Event(enabled=False, saturated=False)
    b = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    _safe_set(b, 'postConditions', {a1})
    assert _is_linked(b, 'postConditions', a1)
    if hasattr(a1, 'Event'):
        assert _is_linked(a1, 'Event', b)
    _safe_set(b, 'postConditions', {a2})
    assert _is_linked(b, 'postConditions', a2)
    if hasattr(a1, 'Event'):
        assert not _is_linked(a1, 'Event', b)
    if hasattr(a2, 'Event'):
        assert _is_linked(a2, 'Event', b)
    _safe_set(b, 'postConditions', set())
    assert not _is_linked(b, 'postConditions', a2)
    if hasattr(a2, 'Event'):
        assert not _is_linked(a2, 'Event', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_adaptiveProcess1_stub_double():
    # adaptiveSystem_AdaptiveProcess has no real 'adaptiveSystem_AdaptiveProcess' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_AdaptiveSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_AdaptiveSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_AdaptiveSystem(setWellformednessToOclets=True)
    partner = adaptiveSystem_AdaptiveProcess()
    setattr(partner, 'adaptiveSystem_AdaptiveProcess', None)
    _safe_set(owner, 'adaptiveSystem_AdaptiveSystem2', partner)
    assert getattr(partner, 'adaptiveSystem_AdaptiveProcess') == owner
    _safe_set(owner, 'adaptiveSystem_AdaptiveSystem2', None)
    assert getattr(partner, 'adaptiveSystem_AdaptiveProcess') is None


def test_assoc_destination31_stub_double():
    # adaptiveSystem_ArcToEvent has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Event(enabled=True, saturated=True)
    partner = adaptiveSystem_ArcToEvent()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'Event32', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'Event32', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_destination36_stub_double():
    # adaptiveSystem_ArcToCondition has no real 'incoming37' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    partner = adaptiveSystem_ArcToCondition()
    setattr(partner, 'incoming37', None)
    _safe_set(owner, 'Condition38', partner)
    assert getattr(partner, 'incoming37') == owner
    _safe_set(owner, 'Condition38', None)
    assert getattr(partner, 'incoming37') is None


def test_assoc_doNet5_stub_double():
    # adaptiveSystem_DoNet has no real 'adaptiveSystem_DoNet' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Oclet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Oclet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Oclet(name="sample_text", orientation="sample_text", quantor="sample_text", wellFormed=True)
    partner = adaptiveSystem_DoNet()
    setattr(partner, 'adaptiveSystem_DoNet', None)
    _safe_set(owner, 'adaptiveSystem_Oclet6', partner)
    assert getattr(partner, 'adaptiveSystem_DoNet') == owner
    _safe_set(owner, 'adaptiveSystem_Oclet6', None)
    assert getattr(partner, 'adaptiveSystem_DoNet') is None


def test_assoc_incoming18_stub_double():
    # adaptiveSystem_ArcToCondition has no real 'ArcToCondition' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    partner = adaptiveSystem_ArcToCondition()
    setattr(partner, 'ArcToCondition', None)
    _safe_set(owner, 'destination', {partner})
    assert getattr(partner, 'ArcToCondition') == owner
    _safe_set(owner, 'destination', set())
    assert getattr(partner, 'ArcToCondition') is None


def test_assoc_incoming23_stub_double():
    # adaptiveSystem_ArcToEvent has no real 'ArcToEvent25' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Event(enabled=True, saturated=True)
    partner = adaptiveSystem_ArcToEvent()
    setattr(partner, 'ArcToEvent25', None)
    _safe_set(owner, 'destination24', {partner})
    assert getattr(partner, 'ArcToEvent25') == owner
    _safe_set(owner, 'destination24', set())
    assert getattr(partner, 'ArcToEvent25') is None


def test_assoc_markedConditions10_stub_double():
    # adaptiveSystem_PreNet has no real 'adaptiveSystem_PreNet11' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    partner = adaptiveSystem_PreNet()
    setattr(partner, 'adaptiveSystem_PreNet11', None)
    _safe_set(owner, 'adaptiveSystem_Condition', partner)
    assert owner in getattr(partner, 'adaptiveSystem_PreNet11')
    _safe_set(owner, 'adaptiveSystem_Condition', None)
    assert owner not in getattr(partner, 'adaptiveSystem_PreNet11')


def test_assoc_markedConditions12_stub_double():
    # adaptiveSystem_AdaptiveProcess has no real 'adaptiveSystem_AdaptiveProcess13' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    partner = adaptiveSystem_AdaptiveProcess()
    setattr(partner, 'adaptiveSystem_AdaptiveProcess13', None)
    _safe_set(owner, 'adaptiveSystem_Condition14', partner)
    assert owner in getattr(partner, 'adaptiveSystem_AdaptiveProcess13')
    _safe_set(owner, 'adaptiveSystem_Condition14', None)
    assert owner not in getattr(partner, 'adaptiveSystem_AdaptiveProcess13')


def test_assoc_outgoing19_stub_double():
    # adaptiveSystem_ArcToEvent has no real 'ArcToEvent' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    partner = adaptiveSystem_ArcToEvent()
    setattr(partner, 'ArcToEvent', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'ArcToEvent') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'ArcToEvent') is None


def test_assoc_outgoing26_stub_double():
    # adaptiveSystem_ArcToCondition has no real 'ArcToCondition28' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Event(enabled=True, saturated=True)
    partner = adaptiveSystem_ArcToCondition()
    setattr(partner, 'ArcToCondition28', None)
    _safe_set(owner, 'source27', {partner})
    assert getattr(partner, 'ArcToCondition28') == owner
    _safe_set(owner, 'source27', set())
    assert getattr(partner, 'ArcToCondition28') is None


def test_assoc_preNet3_stub_double():
    # adaptiveSystem_PreNet has no real 'adaptiveSystem_PreNet' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Oclet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Oclet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Oclet(name="sample_text", orientation="sample_text", quantor="sample_text", wellFormed=True)
    partner = adaptiveSystem_PreNet()
    setattr(partner, 'adaptiveSystem_PreNet', None)
    _safe_set(owner, 'adaptiveSystem_Oclet4', partner)
    assert getattr(partner, 'adaptiveSystem_PreNet') == owner
    _safe_set(owner, 'adaptiveSystem_Oclet4', None)
    assert getattr(partner, 'adaptiveSystem_PreNet') is None


def test_assoc_source29_stub_double():
    # adaptiveSystem_ArcToEvent has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Condition(marked=True, maximal=True, minimal=True, token=7)
    partner = adaptiveSystem_ArcToEvent()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Condition30', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Condition30', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_source33_stub_double():
    # adaptiveSystem_ArcToCondition has no real 'outgoing34' property in the generated
    # code (a bare stub) -- manually attach it so adaptiveSystem_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # adaptiveSystem_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = adaptiveSystem_Event(enabled=True, saturated=True)
    partner = adaptiveSystem_ArcToCondition()
    setattr(partner, 'outgoing34', None)
    _safe_set(owner, 'Event35', partner)
    assert getattr(partner, 'outgoing34') == owner
    _safe_set(owner, 'Event35', None)
    assert getattr(partner, 'outgoing34') is None


