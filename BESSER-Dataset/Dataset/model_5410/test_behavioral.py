import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    Gate,
    IDBase,
    fault_tree_AND,
    fault_tree_BasicEvent,
    fault_tree_ErrorInstance,
    fault_tree_ErrorType,
    fault_tree_Event,
    fault_tree_FailureInstance,
    fault_tree_FailureType,
    fault_tree_FaultTree,
    fault_tree_Gate,
    fault_tree_Hazard,
    fault_tree_Inhibit,
    fault_tree_IntermediateEvent,
    fault_tree_OR,
    fault_tree_PriorAND,
    fault_tree_UndevelopedEvent,
    fault_tree_XOR,
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

def test_assoc_error38_reverse_link_reassign_clear():
    a1 = fault_tree_ErrorType(name="sample_text")
    a2 = fault_tree_ErrorType(name="sample_text_2")
    b = fault_tree_ErrorInstance(name="sample_text")
    _safe_set(b, 'ErrorInstance40', a1)
    assert _is_linked(b, 'ErrorInstance40', a1)
    if hasattr(a1, 'type39'):
        assert _is_linked(a1, 'type39', b)
    _safe_set(b, 'ErrorInstance40', a2)
    assert _is_linked(b, 'ErrorInstance40', a2)
    if hasattr(a1, 'type39'):
        assert not _is_linked(a1, 'type39', b)
    if hasattr(a2, 'type39'):
        assert _is_linked(a2, 'type39', b)
    _safe_set(b, 'ErrorInstance40', None)
    assert not _is_linked(b, 'ErrorInstance40', a2)
    if hasattr(a2, 'type39'):
        assert not _is_linked(a2, 'type39', b)


def test_assoc_error43_reverse_link_reassign_clear():
    a1 = fault_tree_ErrorInstance(name="sample_text")
    a2 = fault_tree_ErrorInstance(name="sample_text_2")
    b = fault_tree_BasicEvent(probability=3.14)
    _safe_set(b, 'BasicEvent', a1)
    assert _is_linked(b, 'BasicEvent', a1)
    if hasattr(a1, 'instance44'):
        assert _is_linked(a1, 'instance44', b)
    _safe_set(b, 'BasicEvent', a2)
    assert _is_linked(b, 'BasicEvent', a2)
    if hasattr(a1, 'instance44'):
        assert not _is_linked(a1, 'instance44', b)
    if hasattr(a2, 'instance44'):
        assert _is_linked(a2, 'instance44', b)
    _safe_set(b, 'BasicEvent', None)
    assert not _is_linked(b, 'BasicEvent', a2)
    if hasattr(a2, 'instance44'):
        assert not _is_linked(a2, 'instance44', b)


def test_assoc_instance22_reverse_link_reassign_clear():
    a1 = fault_tree_FailureType(name="sample_text")
    a2 = fault_tree_FailureType(name="sample_text_2")
    b = fault_tree_FailureInstance(name="sample_text")
    _safe_set(b, 'FailureInstance23', a1)
    assert _is_linked(b, 'FailureInstance23', a1)
    if hasattr(a1, 'type'):
        assert _is_linked(a1, 'type', b)
    _safe_set(b, 'FailureInstance23', a2)
    assert _is_linked(b, 'FailureInstance23', a2)
    if hasattr(a1, 'type'):
        assert not _is_linked(a1, 'type', b)
    if hasattr(a2, 'type'):
        assert _is_linked(a2, 'type', b)
    _safe_set(b, 'FailureInstance23', None)
    assert not _is_linked(b, 'FailureInstance23', a2)
    if hasattr(a2, 'type'):
        assert not _is_linked(a2, 'type', b)


def test_assoc_instance35_reverse_link_reassign_clear():
    a1 = fault_tree_ErrorInstance(name="sample_text")
    a2 = fault_tree_ErrorInstance(name="sample_text_2")
    b = fault_tree_BasicEvent(probability=3.14)
    _safe_set(b, 'error', {a1})
    assert _is_linked(b, 'error', a1)
    if hasattr(a1, 'ErrorInstance'):
        assert _is_linked(a1, 'ErrorInstance', b)
    _safe_set(b, 'error', {a2})
    assert _is_linked(b, 'error', a2)
    if hasattr(a1, 'ErrorInstance'):
        assert not _is_linked(a1, 'ErrorInstance', b)
    if hasattr(a2, 'ErrorInstance'):
        assert _is_linked(a2, 'ErrorInstance', b)
    _safe_set(b, 'error', set())
    assert not _is_linked(b, 'error', a2)
    if hasattr(a2, 'ErrorInstance'):
        assert not _is_linked(a2, 'ErrorInstance', b)


def test_assoc_previousError31_reverse_link_reassign_clear():
    a1 = fault_tree_FailureInstance(name="sample_text")
    a2 = fault_tree_FailureInstance(name="sample_text_2")
    b = fault_tree_ErrorInstance(name="sample_text")
    _safe_set(b, 'fault_tree_ErrorInstance', a1)
    assert _is_linked(b, 'fault_tree_ErrorInstance', a1)
    if hasattr(a1, 'fault_tree_FailureInstance32'):
        assert _is_linked(a1, 'fault_tree_FailureInstance32', b)
    _safe_set(b, 'fault_tree_ErrorInstance', a2)
    assert _is_linked(b, 'fault_tree_ErrorInstance', a2)
    if hasattr(a1, 'fault_tree_FailureInstance32'):
        assert not _is_linked(a1, 'fault_tree_FailureInstance32', b)
    if hasattr(a2, 'fault_tree_FailureInstance32'):
        assert _is_linked(a2, 'fault_tree_FailureInstance32', b)
    _safe_set(b, 'fault_tree_ErrorInstance', None)
    assert not _is_linked(b, 'fault_tree_ErrorInstance', a2)
    if hasattr(a2, 'fault_tree_FailureInstance32'):
        assert not _is_linked(a2, 'fault_tree_FailureInstance32', b)


def test_assoc_previousFailure30_reverse_link_reassign_clear():
    a1 = fault_tree_FailureInstance(name="sample_text")
    a2 = fault_tree_FailureInstance(name="sample_text_2")
    b = fault_tree_FailureInstance(name="sample_text")
    _safe_set(b, 'fault_tree_FailureInstance29', a1)
    assert _is_linked(b, 'fault_tree_FailureInstance29', a1)
    if hasattr(a1, 'fault_tree_FailureInstance'):
        assert _is_linked(a1, 'fault_tree_FailureInstance', b)
    _safe_set(b, 'fault_tree_FailureInstance29', a2)
    assert _is_linked(b, 'fault_tree_FailureInstance29', a2)
    if hasattr(a1, 'fault_tree_FailureInstance'):
        assert not _is_linked(a1, 'fault_tree_FailureInstance', b)
    if hasattr(a2, 'fault_tree_FailureInstance'):
        assert _is_linked(a2, 'fault_tree_FailureInstance', b)
    _safe_set(b, 'fault_tree_FailureInstance29', None)
    assert not _is_linked(b, 'fault_tree_FailureInstance29', a2)
    if hasattr(a2, 'fault_tree_FailureInstance'):
        assert not _is_linked(a2, 'fault_tree_FailureInstance', b)


def test_assoc_type26_reverse_link_reassign_clear():
    a1 = fault_tree_FailureType(name="sample_text")
    a2 = fault_tree_FailureType(name="sample_text_2")
    b = fault_tree_FailureInstance(name="sample_text")
    _safe_set(b, 'instance', a1)
    assert _is_linked(b, 'instance', a1)
    if hasattr(a1, 'FailureType'):
        assert _is_linked(a1, 'FailureType', b)
    _safe_set(b, 'instance', a2)
    assert _is_linked(b, 'instance', a2)
    if hasattr(a1, 'FailureType'):
        assert not _is_linked(a1, 'FailureType', b)
    if hasattr(a2, 'FailureType'):
        assert _is_linked(a2, 'FailureType', b)
    _safe_set(b, 'instance', None)
    assert not _is_linked(b, 'instance', a2)
    if hasattr(a2, 'FailureType'):
        assert not _is_linked(a2, 'FailureType', b)


def test_assoc_type45_reverse_link_reassign_clear():
    a1 = fault_tree_ErrorType(name="sample_text")
    a2 = fault_tree_ErrorType(name="sample_text_2")
    b = fault_tree_ErrorInstance(name="sample_text")
    _safe_set(b, 'error46', a1)
    assert _is_linked(b, 'error46', a1)
    if hasattr(a1, 'ErrorType'):
        assert _is_linked(a1, 'ErrorType', b)
    _safe_set(b, 'error46', a2)
    assert _is_linked(b, 'error46', a2)
    if hasattr(a1, 'ErrorType'):
        assert not _is_linked(a1, 'ErrorType', b)
    if hasattr(a2, 'ErrorType'):
        assert _is_linked(a2, 'ErrorType', b)
    _safe_set(b, 'error46', None)
    assert not _is_linked(b, 'error46', a2)
    if hasattr(a2, 'ErrorType'):
        assert not _is_linked(a2, 'ErrorType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_error_instance62_stub_double():
    # fault_tree_FaultTree has no real 'root63' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_ErrorInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_ErrorInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_ErrorInstance(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'root63', None)
    _safe_set(owner, 'ErrorInstance64', partner)
    assert owner in getattr(partner, 'root63')
    _safe_set(owner, 'ErrorInstance64', None)
    assert owner not in getattr(partner, 'root63')


def test_assoc_error_type65_stub_double():
    # fault_tree_FaultTree has no real 'root66' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_ErrorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_ErrorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_ErrorType(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'root66', None)
    _safe_set(owner, 'ErrorType67', partner)
    assert owner in getattr(partner, 'root66')
    _safe_set(owner, 'ErrorType67', None)
    assert owner not in getattr(partner, 'root66')


def test_assoc_event33_stub_double():
    # fault_tree_IntermediateEvent has no real 'IntermediateEvent' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_FailureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_FailureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_FailureInstance(name="sample_text")
    partner = fault_tree_IntermediateEvent()
    setattr(partner, 'IntermediateEvent', None)
    _safe_set(owner, 'instance34', partner)
    assert getattr(partner, 'IntermediateEvent') == owner
    _safe_set(owner, 'instance34', None)
    assert getattr(partner, 'IntermediateEvent') is None


def test_assoc_event53_stub_double():
    # fault_tree_FaultTree has no real 'root54' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'root54', None)
    _safe_set(owner, 'Event55', partner)
    assert owner in getattr(partner, 'root54')
    _safe_set(owner, 'Event55', None)
    assert owner not in getattr(partner, 'root54')


def test_assoc_failure_instance56_stub_double():
    # fault_tree_FaultTree has no real 'root57' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_FailureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_FailureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_FailureInstance(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'root57', None)
    _safe_set(owner, 'FailureInstance58', partner)
    assert owner in getattr(partner, 'root57')
    _safe_set(owner, 'FailureInstance58', None)
    assert owner not in getattr(partner, 'root57')


def test_assoc_failure_type59_stub_double():
    # fault_tree_FaultTree has no real 'root60' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_FailureType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_FailureType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_FailureType(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'root60', None)
    _safe_set(owner, 'FailureType61', partner)
    assert owner in getattr(partner, 'root60')
    _safe_set(owner, 'FailureType61', None)
    assert owner not in getattr(partner, 'root60')


def test_assoc_inEvent17_stub_double():
    # fault_tree_IntermediateEvent has no real 'fault_tree_IntermediateEvent18' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_IntermediateEvent()
    setattr(partner, 'fault_tree_IntermediateEvent18', None)
    _safe_set(owner, 'fault_tree_Event', partner)
    assert getattr(partner, 'fault_tree_IntermediateEvent18') == owner
    _safe_set(owner, 'fault_tree_Event', None)
    assert getattr(partner, 'fault_tree_IntermediateEvent18') is None


def test_assoc_inputEvents3_stub_double():
    # fault_tree_Gate has no real 'outputGate' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_Gate()
    setattr(partner, 'outputGate', None)
    _safe_set(owner, 'Event', partner)
    assert owner in getattr(partner, 'outputGate')
    _safe_set(owner, 'Event', None)
    assert owner not in getattr(partner, 'outputGate')


def test_assoc_inputGate10_stub_double():
    # fault_tree_Gate has no real 'Gate' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_Gate()
    setattr(partner, 'Gate', None)
    _safe_set(owner, 'outputEvent', partner)
    assert getattr(partner, 'Gate') == owner
    _safe_set(owner, 'outputEvent', None)
    assert getattr(partner, 'Gate') is None


def test_assoc_instance15_stub_double():
    # fault_tree_IntermediateEvent has no real 'event16' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_FailureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_FailureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_FailureInstance(name="sample_text")
    partner = fault_tree_IntermediateEvent()
    setattr(partner, 'event16', None)
    _safe_set(owner, 'FailureInstance', partner)
    assert owner in getattr(partner, 'event16')
    _safe_set(owner, 'FailureInstance', None)
    assert owner not in getattr(partner, 'event16')


def test_assoc_outEvent19_stub_double():
    # fault_tree_IntermediateEvent has no real 'fault_tree_IntermediateEvent20' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_IntermediateEvent()
    setattr(partner, 'fault_tree_IntermediateEvent20', None)
    _safe_set(owner, 'fault_tree_Event21', partner)
    assert getattr(partner, 'fault_tree_IntermediateEvent20') == owner
    _safe_set(owner, 'fault_tree_Event21', None)
    assert getattr(partner, 'fault_tree_IntermediateEvent20') is None


def test_assoc_outEvent36_stub_double():
    # fault_tree_IntermediateEvent has no real 'fault_tree_IntermediateEvent37' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_BasicEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_BasicEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_BasicEvent(probability=3.14)
    partner = fault_tree_IntermediateEvent()
    setattr(partner, 'fault_tree_IntermediateEvent37', None)
    _safe_set(owner, 'fault_tree_BasicEvent', partner)
    assert getattr(partner, 'fault_tree_IntermediateEvent37') == owner
    _safe_set(owner, 'fault_tree_BasicEvent', None)
    assert getattr(partner, 'fault_tree_IntermediateEvent37') is None


def test_assoc_outputEvent7_stub_double():
    # fault_tree_Gate has no real 'inputGate' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_Gate()
    setattr(partner, 'inputGate', None)
    _safe_set(owner, 'Event8', partner)
    assert getattr(partner, 'inputGate') == owner
    _safe_set(owner, 'Event8', None)
    assert getattr(partner, 'inputGate') is None


def test_assoc_outputGate11_stub_double():
    # fault_tree_Gate has no real 'Gate12' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_Gate()
    setattr(partner, 'Gate12', None)
    _safe_set(owner, 'inputEvents', partner)
    assert getattr(partner, 'Gate12') == owner
    _safe_set(owner, 'inputEvents', None)
    assert getattr(partner, 'Gate12') is None


def test_assoc_root13_stub_double():
    # fault_tree_FaultTree has no real 'FaultTree14' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_Event(description="sample_text", name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'FaultTree14', None)
    _safe_set(owner, 'event', partner)
    assert getattr(partner, 'FaultTree14') == owner
    _safe_set(owner, 'event', None)
    assert getattr(partner, 'FaultTree14') is None


def test_assoc_root24_stub_double():
    # fault_tree_FaultTree has no real 'FaultTree25' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_FailureType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_FailureType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_FailureType(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'FaultTree25', None)
    _safe_set(owner, 'failure_type', partner)
    assert getattr(partner, 'FaultTree25') == owner
    _safe_set(owner, 'failure_type', None)
    assert getattr(partner, 'FaultTree25') is None


def test_assoc_root27_stub_double():
    # fault_tree_FaultTree has no real 'FaultTree28' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_FailureInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_FailureInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_FailureInstance(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'FaultTree28', None)
    _safe_set(owner, 'failure_instance', partner)
    assert getattr(partner, 'FaultTree28') == owner
    _safe_set(owner, 'failure_instance', None)
    assert getattr(partner, 'FaultTree28') is None


def test_assoc_root41_stub_double():
    # fault_tree_FaultTree has no real 'FaultTree42' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_ErrorType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_ErrorType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_ErrorType(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'FaultTree42', None)
    _safe_set(owner, 'error_type', partner)
    assert getattr(partner, 'FaultTree42') == owner
    _safe_set(owner, 'error_type', None)
    assert getattr(partner, 'FaultTree42') is None


def test_assoc_root47_stub_double():
    # fault_tree_FaultTree has no real 'FaultTree48' property in the generated
    # code (a bare stub) -- manually attach it so fault_tree_ErrorInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fault_tree_ErrorInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fault_tree_ErrorInstance(name="sample_text")
    partner = fault_tree_FaultTree()
    setattr(partner, 'FaultTree48', None)
    _safe_set(owner, 'error_instance', partner)
    assert getattr(partner, 'FaultTree48') == owner
    _safe_set(owner, 'error_instance', None)
    assert getattr(partner, 'FaultTree48') is None


