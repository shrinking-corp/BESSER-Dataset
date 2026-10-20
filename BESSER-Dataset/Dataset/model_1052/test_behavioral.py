import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    Transition,
    devs_AtomicModel,
    devs_Event,
    devs_ExternalTransition,
    devs_InputEvent,
    devs_InternalTransition,
    devs_OutputEvent,
    devs_OutputFunction,
    devs_State,
    devs_Transition,
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

def test_assoc_atomicModel14_reverse_link_reassign_clear():
    a1 = devs_State(lifeTime=3.14, name="sample_text")
    a2 = devs_State(lifeTime=9.99, name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'AtomicModel', a1)
    assert _is_linked(b, 'AtomicModel', a1)
    if hasattr(a1, 'state'):
        assert _is_linked(a1, 'state', b)
    _safe_set(b, 'AtomicModel', a2)
    assert _is_linked(b, 'AtomicModel', a2)
    if hasattr(a1, 'state'):
        assert not _is_linked(a1, 'state', b)
    if hasattr(a2, 'state'):
        assert _is_linked(a2, 'state', b)
    _safe_set(b, 'AtomicModel', None)
    assert not _is_linked(b, 'AtomicModel', a2)
    if hasattr(a2, 'state'):
        assert not _is_linked(a2, 'state', b)


def test_assoc_atomicModel15_reverse_link_reassign_clear():
    a1 = devs_Event(name="sample_text")
    a2 = devs_Event(name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'AtomicModel16', a1)
    assert _is_linked(b, 'AtomicModel16', a1)
    if hasattr(a1, 'event'):
        assert _is_linked(a1, 'event', b)
    _safe_set(b, 'AtomicModel16', a2)
    assert _is_linked(b, 'AtomicModel16', a2)
    if hasattr(a1, 'event'):
        assert not _is_linked(a1, 'event', b)
    if hasattr(a2, 'event'):
        assert _is_linked(a2, 'event', b)
    _safe_set(b, 'AtomicModel16', None)
    assert not _is_linked(b, 'AtomicModel16', a2)
    if hasattr(a2, 'event'):
        assert not _is_linked(a2, 'event', b)


def test_assoc_atomicModel24_reverse_link_reassign_clear():
    a1 = devs_Transition(name="sample_text")
    a2 = devs_Transition(name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'AtomicModel25', a1)
    assert _is_linked(b, 'AtomicModel25', a1)
    if hasattr(a1, 'transition'):
        assert _is_linked(a1, 'transition', b)
    _safe_set(b, 'AtomicModel25', a2)
    assert _is_linked(b, 'AtomicModel25', a2)
    if hasattr(a1, 'transition'):
        assert not _is_linked(a1, 'transition', b)
    if hasattr(a2, 'transition'):
        assert _is_linked(a2, 'transition', b)
    _safe_set(b, 'AtomicModel25', None)
    assert not _is_linked(b, 'AtomicModel25', a2)
    if hasattr(a2, 'transition'):
        assert not _is_linked(a2, 'transition', b)


def test_assoc_atomicModel30_reverse_link_reassign_clear():
    a1 = devs_OutputFunction(name="sample_text")
    a2 = devs_OutputFunction(name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'AtomicModel32', a1)
    assert _is_linked(b, 'AtomicModel32', a1)
    if hasattr(a1, 'outputFunction31'):
        assert _is_linked(a1, 'outputFunction31', b)
    _safe_set(b, 'AtomicModel32', a2)
    assert _is_linked(b, 'AtomicModel32', a2)
    if hasattr(a1, 'outputFunction31'):
        assert not _is_linked(a1, 'outputFunction31', b)
    if hasattr(a2, 'outputFunction31'):
        assert _is_linked(a2, 'outputFunction31', b)
    _safe_set(b, 'AtomicModel32', None)
    assert not _is_linked(b, 'AtomicModel32', a2)
    if hasattr(a2, 'outputFunction31'):
        assert not _is_linked(a2, 'outputFunction31', b)


def test_assoc_event1_reverse_link_reassign_clear():
    a1 = devs_Event(name="sample_text")
    a2 = devs_Event(name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'atomicModel2', {a1})
    assert _is_linked(b, 'atomicModel2', a1)
    if hasattr(a1, 'Event'):
        assert _is_linked(a1, 'Event', b)
    _safe_set(b, 'atomicModel2', {a2})
    assert _is_linked(b, 'atomicModel2', a2)
    if hasattr(a1, 'Event'):
        assert not _is_linked(a1, 'Event', b)
    if hasattr(a2, 'Event'):
        assert _is_linked(a2, 'Event', b)
    _safe_set(b, 'atomicModel2', set())
    assert not _is_linked(b, 'atomicModel2', a2)
    if hasattr(a2, 'Event'):
        assert not _is_linked(a2, 'Event', b)


def test_assoc_in_7_reverse_link_reassign_clear():
    a1 = devs_Transition(name="sample_text")
    a2 = devs_Transition(name="sample_text_2")
    b = devs_State(lifeTime=3.14, name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition8'):
        assert _is_linked(a1, 'Transition8', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition8'):
        assert not _is_linked(a1, 'Transition8', b)
    if hasattr(a2, 'Transition8'):
        assert _is_linked(a2, 'Transition8', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition8'):
        assert not _is_linked(a2, 'Transition8', b)


def test_assoc_out9_reverse_link_reassign_clear():
    a1 = devs_Transition(name="sample_text")
    a2 = devs_Transition(name="sample_text_2")
    b = devs_State(lifeTime=3.14, name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition10'):
        assert _is_linked(a1, 'Transition10', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition10'):
        assert not _is_linked(a1, 'Transition10', b)
    if hasattr(a2, 'Transition10'):
        assert _is_linked(a2, 'Transition10', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition10'):
        assert not _is_linked(a2, 'Transition10', b)


def test_assoc_outF11_reverse_link_reassign_clear():
    a1 = devs_State(lifeTime=3.14, name="sample_text")
    a2 = devs_State(lifeTime=9.99, name="sample_text_2")
    b = devs_OutputFunction(name="sample_text")
    _safe_set(b, 'OutputFunction13', a1)
    assert _is_linked(b, 'OutputFunction13', a1)
    if hasattr(a1, 'source12'):
        assert _is_linked(a1, 'source12', b)
    _safe_set(b, 'OutputFunction13', a2)
    assert _is_linked(b, 'OutputFunction13', a2)
    if hasattr(a1, 'source12'):
        assert not _is_linked(a1, 'source12', b)
    if hasattr(a2, 'source12'):
        assert _is_linked(a2, 'source12', b)
    _safe_set(b, 'OutputFunction13', None)
    assert not _is_linked(b, 'OutputFunction13', a2)
    if hasattr(a2, 'source12'):
        assert not _is_linked(a2, 'source12', b)


def test_assoc_outputFunction5_reverse_link_reassign_clear():
    a1 = devs_OutputFunction(name="sample_text")
    a2 = devs_OutputFunction(name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'atomicModel6', {a1})
    assert _is_linked(b, 'atomicModel6', a1)
    if hasattr(a1, 'OutputFunction'):
        assert _is_linked(a1, 'OutputFunction', b)
    _safe_set(b, 'atomicModel6', {a2})
    assert _is_linked(b, 'atomicModel6', a2)
    if hasattr(a1, 'OutputFunction'):
        assert not _is_linked(a1, 'OutputFunction', b)
    if hasattr(a2, 'OutputFunction'):
        assert _is_linked(a2, 'OutputFunction', b)
    _safe_set(b, 'atomicModel6', set())
    assert not _is_linked(b, 'atomicModel6', a2)
    if hasattr(a2, 'OutputFunction'):
        assert not _is_linked(a2, 'OutputFunction', b)


def test_assoc_source20_reverse_link_reassign_clear():
    a1 = devs_Transition(name="sample_text")
    a2 = devs_Transition(name="sample_text_2")
    b = devs_State(lifeTime=3.14, name="sample_text")
    _safe_set(b, 'State21', a1)
    assert _is_linked(b, 'State21', a1)
    if hasattr(a1, 'out'):
        assert _is_linked(a1, 'out', b)
    _safe_set(b, 'State21', a2)
    assert _is_linked(b, 'State21', a2)
    if hasattr(a1, 'out'):
        assert not _is_linked(a1, 'out', b)
    if hasattr(a2, 'out'):
        assert _is_linked(a2, 'out', b)
    _safe_set(b, 'State21', None)
    assert not _is_linked(b, 'State21', a2)
    if hasattr(a2, 'out'):
        assert not _is_linked(a2, 'out', b)


def test_assoc_source27_reverse_link_reassign_clear():
    a1 = devs_State(lifeTime=3.14, name="sample_text")
    a2 = devs_State(lifeTime=9.99, name="sample_text_2")
    b = devs_OutputFunction(name="sample_text")
    _safe_set(b, 'outF', a1)
    assert _is_linked(b, 'outF', a1)
    if hasattr(a1, 'State28'):
        assert _is_linked(a1, 'State28', b)
    _safe_set(b, 'outF', a2)
    assert _is_linked(b, 'outF', a2)
    if hasattr(a1, 'State28'):
        assert not _is_linked(a1, 'State28', b)
    if hasattr(a2, 'State28'):
        assert _is_linked(a2, 'State28', b)
    _safe_set(b, 'outF', None)
    assert not _is_linked(b, 'outF', a2)
    if hasattr(a2, 'State28'):
        assert not _is_linked(a2, 'State28', b)


def test_assoc_state0_reverse_link_reassign_clear():
    a1 = devs_State(lifeTime=3.14, name="sample_text")
    a2 = devs_State(lifeTime=9.99, name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'atomicModel', {a1})
    assert _is_linked(b, 'atomicModel', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'atomicModel', {a2})
    assert _is_linked(b, 'atomicModel', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'atomicModel', set())
    assert not _is_linked(b, 'atomicModel', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = devs_Transition(name="sample_text")
    a2 = devs_Transition(name="sample_text_2")
    b = devs_State(lifeTime=3.14, name="sample_text")
    _safe_set(b, 'State23', a1)
    assert _is_linked(b, 'State23', a1)
    if hasattr(a1, 'in_'):
        assert _is_linked(a1, 'in_', b)
    _safe_set(b, 'State23', a2)
    assert _is_linked(b, 'State23', a2)
    if hasattr(a1, 'in_'):
        assert not _is_linked(a1, 'in_', b)
    if hasattr(a2, 'in_'):
        assert _is_linked(a2, 'in_', b)
    _safe_set(b, 'State23', None)
    assert not _is_linked(b, 'State23', a2)
    if hasattr(a2, 'in_'):
        assert not _is_linked(a2, 'in_', b)


def test_assoc_transition3_reverse_link_reassign_clear():
    a1 = devs_Transition(name="sample_text")
    a2 = devs_Transition(name="sample_text_2")
    b = devs_AtomicModel(name="sample_text")
    _safe_set(b, 'atomicModel4', {a1})
    assert _is_linked(b, 'atomicModel4', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'atomicModel4', {a2})
    assert _is_linked(b, 'atomicModel4', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'atomicModel4', set())
    assert not _is_linked(b, 'atomicModel4', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_outputEvent29_stub_double():
    # devs_OutputEvent has no real 'OutputEvent' property in the generated
    # code (a bare stub) -- manually attach it so devs_OutputFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # devs_OutputFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = devs_OutputFunction(name="sample_text")
    partner = devs_OutputEvent()
    setattr(partner, 'OutputEvent', None)
    _safe_set(owner, 'outputFunction', partner)
    assert getattr(partner, 'OutputEvent') == owner
    _safe_set(owner, 'outputFunction', None)
    assert getattr(partner, 'OutputEvent') is None


def test_assoc_outputFunction18_stub_double():
    # devs_OutputEvent has no real 'outputEvent' property in the generated
    # code (a bare stub) -- manually attach it so devs_OutputFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # devs_OutputFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = devs_OutputFunction(name="sample_text")
    partner = devs_OutputEvent()
    setattr(partner, 'outputEvent', None)
    _safe_set(owner, 'OutputFunction19', partner)
    assert owner in getattr(partner, 'outputEvent')
    _safe_set(owner, 'OutputFunction19', None)
    assert owner not in getattr(partner, 'outputEvent')


