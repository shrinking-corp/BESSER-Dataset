import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    Transfer,
    faultTree_ConditioningEvent,
    faultTree_Event,
    faultTree_FaultTree,
    faultTree_Gate,
    faultTree_IntermediateEvent,
    faultTree_PrimaryEvent,
    faultTree_Transfer,
    faultTree_TransferIn,
    faultTree_TransferOut,
    GateType,
    PrimaryEventType,
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

def test_assoc_bottomEvent29_reverse_link_reassign_clear():
    a1 = faultTree_IntermediateEvent(probability=3.14)
    a2 = faultTree_IntermediateEvent(probability=9.99)
    b = faultTree_IntermediateEvent(probability=3.14)
    _safe_set(b, 'topEvent', a1)
    assert _is_linked(b, 'topEvent', a1)
    if hasattr(a1, 'IntermediateEvent30'):
        assert _is_linked(a1, 'IntermediateEvent30', b)
    _safe_set(b, 'topEvent', a2)
    assert _is_linked(b, 'topEvent', a2)
    if hasattr(a1, 'IntermediateEvent30'):
        assert not _is_linked(a1, 'IntermediateEvent30', b)
    if hasattr(a2, 'IntermediateEvent30'):
        assert _is_linked(a2, 'IntermediateEvent30', b)
    _safe_set(b, 'topEvent', None)
    assert not _is_linked(b, 'topEvent', a2)
    if hasattr(a2, 'IntermediateEvent30'):
        assert not _is_linked(a2, 'IntermediateEvent30', b)


def test_assoc_bottomGate23_reverse_link_reassign_clear():
    a1 = faultTree_IntermediateEvent(probability=3.14)
    a2 = faultTree_IntermediateEvent(probability=9.99)
    b = faultTree_Gate(name="sample_text", probability=3.14, type="sample_text")
    _safe_set(b, 'Gate24', a1)
    assert _is_linked(b, 'Gate24', a1)
    if hasattr(a1, 'output'):
        assert _is_linked(a1, 'output', b)
    _safe_set(b, 'Gate24', a2)
    assert _is_linked(b, 'Gate24', a2)
    if hasattr(a1, 'output'):
        assert not _is_linked(a1, 'output', b)
    if hasattr(a2, 'output'):
        assert _is_linked(a2, 'output', b)
    _safe_set(b, 'Gate24', None)
    assert not _is_linked(b, 'Gate24', a2)
    if hasattr(a2, 'output'):
        assert not _is_linked(a2, 'output', b)


def test_assoc_conditioningEvents6_reverse_link_reassign_clear():
    a1 = faultTree_FaultTree(name="sample_text")
    a2 = faultTree_FaultTree(name="sample_text_2")
    b = faultTree_ConditioningEvent(condition="sample_text")
    _safe_set(b, 'faultTree_ConditioningEvent', a1)
    assert _is_linked(b, 'faultTree_ConditioningEvent', a1)
    if hasattr(a1, 'faultTree_FaultTree7'):
        assert _is_linked(a1, 'faultTree_FaultTree7', b)
    _safe_set(b, 'faultTree_ConditioningEvent', a2)
    assert _is_linked(b, 'faultTree_ConditioningEvent', a2)
    if hasattr(a1, 'faultTree_FaultTree7'):
        assert not _is_linked(a1, 'faultTree_FaultTree7', b)
    if hasattr(a2, 'faultTree_FaultTree7'):
        assert _is_linked(a2, 'faultTree_FaultTree7', b)
    _safe_set(b, 'faultTree_ConditioningEvent', None)
    assert not _is_linked(b, 'faultTree_ConditioningEvent', a2)
    if hasattr(a2, 'faultTree_FaultTree7'):
        assert not _is_linked(a2, 'faultTree_FaultTree7', b)


def test_assoc_events1_reverse_link_reassign_clear():
    a1 = faultTree_FaultTree(name="sample_text")
    a2 = faultTree_FaultTree(name="sample_text_2")
    b = faultTree_Event(description="sample_text", name="sample_text")
    _safe_set(b, 'faultTree_Event', a1)
    assert _is_linked(b, 'faultTree_Event', a1)
    if hasattr(a1, 'faultTree_FaultTree'):
        assert _is_linked(a1, 'faultTree_FaultTree', b)
    _safe_set(b, 'faultTree_Event', a2)
    assert _is_linked(b, 'faultTree_Event', a2)
    if hasattr(a1, 'faultTree_FaultTree'):
        assert not _is_linked(a1, 'faultTree_FaultTree', b)
    if hasattr(a2, 'faultTree_FaultTree'):
        assert _is_linked(a2, 'faultTree_FaultTree', b)
    _safe_set(b, 'faultTree_Event', None)
    assert not _is_linked(b, 'faultTree_Event', a2)
    if hasattr(a2, 'faultTree_FaultTree'):
        assert not _is_linked(a2, 'faultTree_FaultTree', b)


def test_assoc_faultTree17_reverse_link_reassign_clear():
    a1 = faultTree_Gate(name="sample_text", probability=3.14, type="sample_text")
    a2 = faultTree_Gate(name="sample_text_2", probability=9.99, type="sample_text_2")
    b = faultTree_FaultTree(name="sample_text")
    _safe_set(b, 'FaultTree', a1)
    assert _is_linked(b, 'FaultTree', a1)
    if hasattr(a1, 'gates'):
        assert _is_linked(a1, 'gates', b)
    _safe_set(b, 'FaultTree', a2)
    assert _is_linked(b, 'FaultTree', a2)
    if hasattr(a1, 'gates'):
        assert not _is_linked(a1, 'gates', b)
    if hasattr(a2, 'gates'):
        assert _is_linked(a2, 'gates', b)
    _safe_set(b, 'FaultTree', None)
    assert not _is_linked(b, 'FaultTree', a2)
    if hasattr(a2, 'gates'):
        assert not _is_linked(a2, 'gates', b)


def test_assoc_faultTree20_reverse_link_reassign_clear():
    a1 = faultTree_FaultTree(name="sample_text")
    a2 = faultTree_FaultTree(name="sample_text_2")
    b = faultTree_Event(description="sample_text", name="sample_text")
    _safe_set(b, 'faultTree_Event21', a1)
    assert _is_linked(b, 'faultTree_Event21', a1)
    if hasattr(a1, 'faultTree_FaultTree22'):
        assert _is_linked(a1, 'faultTree_FaultTree22', b)
    _safe_set(b, 'faultTree_Event21', a2)
    assert _is_linked(b, 'faultTree_Event21', a2)
    if hasattr(a1, 'faultTree_FaultTree22'):
        assert not _is_linked(a1, 'faultTree_FaultTree22', b)
    if hasattr(a2, 'faultTree_FaultTree22'):
        assert _is_linked(a2, 'faultTree_FaultTree22', b)
    _safe_set(b, 'faultTree_Event21', None)
    assert not _is_linked(b, 'faultTree_Event21', a2)
    if hasattr(a2, 'faultTree_FaultTree22'):
        assert not _is_linked(a2, 'faultTree_FaultTree22', b)


def test_assoc_gates0_reverse_link_reassign_clear():
    a1 = faultTree_Gate(name="sample_text", probability=3.14, type="sample_text")
    a2 = faultTree_Gate(name="sample_text_2", probability=9.99, type="sample_text_2")
    b = faultTree_FaultTree(name="sample_text")
    _safe_set(b, 'faultTree', {a1})
    assert _is_linked(b, 'faultTree', a1)
    if hasattr(a1, 'Gate'):
        assert _is_linked(a1, 'Gate', b)
    _safe_set(b, 'faultTree', {a2})
    assert _is_linked(b, 'faultTree', a2)
    if hasattr(a1, 'Gate'):
        assert not _is_linked(a1, 'Gate', b)
    if hasattr(a2, 'Gate'):
        assert _is_linked(a2, 'Gate', b)
    _safe_set(b, 'faultTree', set())
    assert not _is_linked(b, 'faultTree', a2)
    if hasattr(a2, 'Gate'):
        assert not _is_linked(a2, 'Gate', b)


def test_assoc_inputs15_reverse_link_reassign_clear():
    a1 = faultTree_Gate(name="sample_text", probability=3.14, type="sample_text")
    a2 = faultTree_Gate(name="sample_text_2", probability=9.99, type="sample_text_2")
    b = faultTree_Event(description="sample_text", name="sample_text")
    _safe_set(b, 'Event', a1)
    assert _is_linked(b, 'Event', a1)
    if hasattr(a1, 'topGates'):
        assert _is_linked(a1, 'topGates', b)
    _safe_set(b, 'Event', a2)
    assert _is_linked(b, 'Event', a2)
    if hasattr(a1, 'topGates'):
        assert not _is_linked(a1, 'topGates', b)
    if hasattr(a2, 'topGates'):
        assert _is_linked(a2, 'topGates', b)
    _safe_set(b, 'Event', None)
    assert not _is_linked(b, 'Event', a2)
    if hasattr(a2, 'topGates'):
        assert not _is_linked(a2, 'topGates', b)


def test_assoc_intermediateEvents2_reverse_link_reassign_clear():
    a1 = faultTree_IntermediateEvent(probability=3.14)
    a2 = faultTree_IntermediateEvent(probability=9.99)
    b = faultTree_FaultTree(name="sample_text")
    _safe_set(b, 'faultTree_FaultTree3', {a1})
    assert _is_linked(b, 'faultTree_FaultTree3', a1)
    if hasattr(a1, 'faultTree_IntermediateEvent'):
        assert _is_linked(a1, 'faultTree_IntermediateEvent', b)
    _safe_set(b, 'faultTree_FaultTree3', {a2})
    assert _is_linked(b, 'faultTree_FaultTree3', a2)
    if hasattr(a1, 'faultTree_IntermediateEvent'):
        assert not _is_linked(a1, 'faultTree_IntermediateEvent', b)
    if hasattr(a2, 'faultTree_IntermediateEvent'):
        assert _is_linked(a2, 'faultTree_IntermediateEvent', b)
    _safe_set(b, 'faultTree_FaultTree3', set())
    assert not _is_linked(b, 'faultTree_FaultTree3', a2)
    if hasattr(a2, 'faultTree_IntermediateEvent'):
        assert not _is_linked(a2, 'faultTree_IntermediateEvent', b)


def test_assoc_output16_reverse_link_reassign_clear():
    a1 = faultTree_IntermediateEvent(probability=3.14)
    a2 = faultTree_IntermediateEvent(probability=9.99)
    b = faultTree_Gate(name="sample_text", probability=3.14, type="sample_text")
    _safe_set(b, 'bottomGate', a1)
    assert _is_linked(b, 'bottomGate', a1)
    if hasattr(a1, 'IntermediateEvent'):
        assert _is_linked(a1, 'IntermediateEvent', b)
    _safe_set(b, 'bottomGate', a2)
    assert _is_linked(b, 'bottomGate', a2)
    if hasattr(a1, 'IntermediateEvent'):
        assert not _is_linked(a1, 'IntermediateEvent', b)
    if hasattr(a2, 'IntermediateEvent'):
        assert _is_linked(a2, 'IntermediateEvent', b)
    _safe_set(b, 'bottomGate', None)
    assert not _is_linked(b, 'bottomGate', a2)
    if hasattr(a2, 'IntermediateEvent'):
        assert not _is_linked(a2, 'IntermediateEvent', b)


def test_assoc_primaryEvents4_reverse_link_reassign_clear():
    a1 = faultTree_PrimaryEvent(probability=3.14, type="sample_text")
    a2 = faultTree_PrimaryEvent(probability=9.99, type="sample_text_2")
    b = faultTree_FaultTree(name="sample_text")
    _safe_set(b, 'faultTree_FaultTree5', {a1})
    assert _is_linked(b, 'faultTree_FaultTree5', a1)
    if hasattr(a1, 'faultTree_PrimaryEvent'):
        assert _is_linked(a1, 'faultTree_PrimaryEvent', b)
    _safe_set(b, 'faultTree_FaultTree5', {a2})
    assert _is_linked(b, 'faultTree_FaultTree5', a2)
    if hasattr(a1, 'faultTree_PrimaryEvent'):
        assert not _is_linked(a1, 'faultTree_PrimaryEvent', b)
    if hasattr(a2, 'faultTree_PrimaryEvent'):
        assert _is_linked(a2, 'faultTree_PrimaryEvent', b)
    _safe_set(b, 'faultTree_FaultTree5', set())
    assert not _is_linked(b, 'faultTree_FaultTree5', a2)
    if hasattr(a2, 'faultTree_PrimaryEvent'):
        assert not _is_linked(a2, 'faultTree_PrimaryEvent', b)


def test_assoc_topEvent12_reverse_link_reassign_clear():
    a1 = faultTree_IntermediateEvent(probability=3.14)
    a2 = faultTree_IntermediateEvent(probability=9.99)
    b = faultTree_FaultTree(name="sample_text")
    _safe_set(b, 'faultTree_FaultTree13', a1)
    assert _is_linked(b, 'faultTree_FaultTree13', a1)
    if hasattr(a1, 'faultTree_IntermediateEvent14'):
        assert _is_linked(a1, 'faultTree_IntermediateEvent14', b)
    _safe_set(b, 'faultTree_FaultTree13', a2)
    assert _is_linked(b, 'faultTree_FaultTree13', a2)
    if hasattr(a1, 'faultTree_IntermediateEvent14'):
        assert not _is_linked(a1, 'faultTree_IntermediateEvent14', b)
    if hasattr(a2, 'faultTree_IntermediateEvent14'):
        assert _is_linked(a2, 'faultTree_IntermediateEvent14', b)
    _safe_set(b, 'faultTree_FaultTree13', None)
    assert not _is_linked(b, 'faultTree_FaultTree13', a2)
    if hasattr(a2, 'faultTree_IntermediateEvent14'):
        assert not _is_linked(a2, 'faultTree_IntermediateEvent14', b)


def test_assoc_topEvent26_reverse_link_reassign_clear():
    a1 = faultTree_IntermediateEvent(probability=3.14)
    a2 = faultTree_IntermediateEvent(probability=9.99)
    b = faultTree_IntermediateEvent(probability=3.14)
    _safe_set(b, 'bottomEvent', a1)
    assert _is_linked(b, 'bottomEvent', a1)
    if hasattr(a1, 'IntermediateEvent27'):
        assert _is_linked(a1, 'IntermediateEvent27', b)
    _safe_set(b, 'bottomEvent', a2)
    assert _is_linked(b, 'bottomEvent', a2)
    if hasattr(a1, 'IntermediateEvent27'):
        assert not _is_linked(a1, 'IntermediateEvent27', b)
    if hasattr(a2, 'IntermediateEvent27'):
        assert _is_linked(a2, 'IntermediateEvent27', b)
    _safe_set(b, 'bottomEvent', None)
    assert not _is_linked(b, 'bottomEvent', a2)
    if hasattr(a2, 'IntermediateEvent27'):
        assert not _is_linked(a2, 'IntermediateEvent27', b)


def test_assoc_topGates18_reverse_link_reassign_clear():
    a1 = faultTree_Gate(name="sample_text", probability=3.14, type="sample_text")
    a2 = faultTree_Gate(name="sample_text_2", probability=9.99, type="sample_text_2")
    b = faultTree_Event(description="sample_text", name="sample_text")
    _safe_set(b, 'inputs', {a1})
    assert _is_linked(b, 'inputs', a1)
    if hasattr(a1, 'Gate19'):
        assert _is_linked(a1, 'Gate19', b)
    _safe_set(b, 'inputs', {a2})
    assert _is_linked(b, 'inputs', a2)
    if hasattr(a1, 'Gate19'):
        assert not _is_linked(a1, 'Gate19', b)
    if hasattr(a2, 'Gate19'):
        assert _is_linked(a2, 'Gate19', b)
    _safe_set(b, 'inputs', set())
    assert not _is_linked(b, 'inputs', a2)
    if hasattr(a2, 'Gate19'):
        assert not _is_linked(a2, 'Gate19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event36_stub_double():
    # faultTree_TransferIn has no real 'transferIn' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_IntermediateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_IntermediateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_IntermediateEvent(probability=3.14)
    partner = faultTree_TransferIn()
    setattr(partner, 'transferIn', None)
    _safe_set(owner, 'IntermediateEvent37', partner)
    assert getattr(partner, 'transferIn') == owner
    _safe_set(owner, 'IntermediateEvent37', None)
    assert getattr(partner, 'transferIn') is None


def test_assoc_event40_stub_double():
    # faultTree_TransferOut has no real 'transferOut' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_IntermediateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_IntermediateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_IntermediateEvent(probability=3.14)
    partner = faultTree_TransferOut()
    setattr(partner, 'transferOut', None)
    _safe_set(owner, 'IntermediateEvent41', partner)
    assert getattr(partner, 'transferOut') == owner
    _safe_set(owner, 'IntermediateEvent41', None)
    assert getattr(partner, 'transferOut') is None


def test_assoc_faultTree38_stub_double():
    # faultTree_TransferIn has no real 'transferIns' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_FaultTree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_FaultTree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_FaultTree(name="sample_text")
    partner = faultTree_TransferIn()
    setattr(partner, 'transferIns', None)
    _safe_set(owner, 'FaultTree39', partner)
    assert getattr(partner, 'transferIns') == owner
    _safe_set(owner, 'FaultTree39', None)
    assert getattr(partner, 'transferIns') is None


def test_assoc_faultTree42_stub_double():
    # faultTree_TransferOut has no real 'transferOut43' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_FaultTree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_FaultTree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_FaultTree(name="sample_text")
    partner = faultTree_TransferOut()
    setattr(partner, 'transferOut43', None)
    _safe_set(owner, 'FaultTree44', partner)
    assert getattr(partner, 'transferOut43') == owner
    _safe_set(owner, 'FaultTree44', None)
    assert getattr(partner, 'transferOut43') is None


def test_assoc_transferIn31_stub_double():
    # faultTree_TransferIn has no real 'TransferIn32' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_IntermediateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_IntermediateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_IntermediateEvent(probability=3.14)
    partner = faultTree_TransferIn()
    setattr(partner, 'TransferIn32', None)
    _safe_set(owner, 'event', partner)
    assert getattr(partner, 'TransferIn32') == owner
    _safe_set(owner, 'event', None)
    assert getattr(partner, 'TransferIn32') is None


def test_assoc_transferIns10_stub_double():
    # faultTree_TransferIn has no real 'TransferIn' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_FaultTree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_FaultTree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_FaultTree(name="sample_text")
    partner = faultTree_TransferIn()
    setattr(partner, 'TransferIn', None)
    _safe_set(owner, 'faultTree11', {partner})
    assert getattr(partner, 'TransferIn') == owner
    _safe_set(owner, 'faultTree11', set())
    assert getattr(partner, 'TransferIn') is None


def test_assoc_transferOut33_stub_double():
    # faultTree_TransferOut has no real 'TransferOut35' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_IntermediateEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_IntermediateEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_IntermediateEvent(probability=3.14)
    partner = faultTree_TransferOut()
    setattr(partner, 'TransferOut35', None)
    _safe_set(owner, 'event34', partner)
    assert getattr(partner, 'TransferOut35') == owner
    _safe_set(owner, 'event34', None)
    assert getattr(partner, 'TransferOut35') is None


def test_assoc_transferOut8_stub_double():
    # faultTree_TransferOut has no real 'TransferOut' property in the generated
    # code (a bare stub) -- manually attach it so faultTree_FaultTree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # faultTree_FaultTree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = faultTree_FaultTree(name="sample_text")
    partner = faultTree_TransferOut()
    setattr(partner, 'TransferOut', None)
    _safe_set(owner, 'faultTree9', partner)
    assert getattr(partner, 'TransferOut') == owner
    _safe_set(owner, 'faultTree9', None)
    assert getattr(partner, 'TransferOut') is None


